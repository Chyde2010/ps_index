"""
Ps Index Paper Portfolio -- Monthly Rebalancer
==============================================

Runs automatically after generate_signal.py in the
GitHub Actions workflow. Reads the current month's
snapshot, computes signal-tilted weights, fetches
prices, records positions and P&L vs benchmark.

Structure:
  $1,000,000 starting capital
  Long book : $700,000 -- positive regime (MSFT, AMZN, CRM, SNOW)
  Short book : $300,000 -- negative regime (DDOG, TWLO, GTLB)

Signal tilt:
  HC signal (z >= 1.5) : 2.0x equal-weight
  z >= 0.5             : 1.2x equal-weight
  z >= 0.0             : 1.0x equal-weight (neutral)
  z <  0.0             : 0.8x equal-weight (underweight)

Benchmark:
  Equal-weight same universe, same 70/30 capital split.
  Rebalanced monthly. Any outperformance vs benchmark
  is attributable solely to the Ps signal tilts.

Output files (live_track_record/paper_portfolio/):
  portfolio_positions.csv  -- monthly position records
  portfolio_performance.csv -- monthly P&L vs benchmark
"""

import os, time, sys
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timezone

# ── Configuration ─────────────────────────────────────────────
STARTING_CAPITAL_USD = 1_000_000
LONG_CAPITAL         = STARTING_CAPITAL_USD * 0.70
SHORT_CAPITAL        = STARTING_CAPITAL_USD * 0.30
HC_THRESHOLD         = 1.5

OUTPUT_DIR     = 'live_track_record'
PORTFOLIO_DIR  = f'{OUTPUT_DIR}/paper_portfolio'
SNAPSHOT_DIR   = OUTPUT_DIR
POSITIONS_FILE = f'{PORTFOLIO_DIR}/portfolio_positions.csv'
PERF_FILE      = f'{PORTFOLIO_DIR}/portfolio_performance.csv'

LONG_TICKERS   = ['MSFT', 'AMZN', 'CRM', 'SNOW']
SHORT_TICKERS  = ['DDOG', 'TWLO', 'GTLB']
ALL_TICKERS    = LONG_TICKERS + SHORT_TICKERS

os.makedirs(PORTFOLIO_DIR, exist_ok=True)

# ── Determine current signal month ────────────────────────────
# Mirrors the logic in generate_signal.py --
# signal is for the month that just ended.
now = datetime.now(timezone.utc)
if now.month == 1:
    signal_year  = now.year - 1
    signal_month = 12
else:
    signal_year  = now.year
    signal_month = now.month - 1

MONTH = f'{signal_year}-{signal_month:02d}'
print('=' * 65)
print(f'Ps Index Portfolio Rebalancer -- {MONTH}')
print(f'Running: {now.strftime("%Y-%m-%d %H:%M UTC")}')
print('=' * 65)
print()

# ── Load signal snapshot ──────────────────────────────────────
# generate_signal.py writes snapshot_{MONTH}.csv
snapshot_path = f'{SNAPSHOT_DIR}/snapshot_{MONTH}.csv'

if not os.path.exists(snapshot_path):
    # Fall back to ps_signal_history.csv if no snapshot
    print(f'Snapshot not found at {snapshot_path}')
    print('Falling back to ps_signal_history.csv...')
    history_path = f'{OUTPUT_DIR}/ps_signal_history.csv'
    if not os.path.exists(history_path):
        print('ERROR: No signal data found. '
              'Rebalancing skipped.')
        sys.exit(0)
    hist = pd.read_csv(history_path)
    snap = hist[hist['month'] == MONTH].copy()
    if snap.empty:
        print(f'ERROR: No signal data for {MONTH}. '
              'Rebalancing skipped.')
        sys.exit(0)
    # Map column names
    snap = snap.rename(columns={
        'ps_own_z': 'ps_zscore',
        'hc_flag':  'high_conviction',
        'regime':   'signal_regime',
    })
else:
    snap = pd.read_csv(snapshot_path)

print('Signal data loaded:')
cols = ['ticker', 'signal_regime',
        'ps_zscore', 'high_conviction']
cols = [c for c in cols if c in snap.columns]
print(snap[cols].to_string(index=False))
print()

# Build signal dict -- handle missing tickers gracefully
signal = {}
for t in ALL_TICKERS:
    row = snap[snap['ticker'] == t]
    if row.empty:
        print(f'  WARNING: {t} missing from snapshot '
              f'-- using z=0.0, hc=False')
        signal[t] = {'ps_zscore': 0.0, 'hc': False}
    else:
        z  = float(row['ps_zscore'].iloc[0])
        hc = bool(row['high_conviction'].iloc[0])
        signal[t] = {'ps_zscore': z, 'hc': hc}

# ── Signal tilt ───────────────────────────────────────────────
def signal_tilt(z, hc):
    if hc or z >= HC_THRESHOLD:
        return 2.0
    elif z >= 0.5:
        return 1.2
    elif z >= 0.0:
        return 1.0
    else:
        return 0.8

# Compute tilted weights -- normalised within each book
long_raw = {t: (1 / len(LONG_TICKERS)) *
               signal_tilt(signal[t]['ps_zscore'],
                           signal[t]['hc'])
            for t in LONG_TICKERS}
long_total   = sum(long_raw.values())
long_weights = {t: v / long_total
                for t, v in long_raw.items()}

short_raw = {t: (1 / len(SHORT_TICKERS)) *
                signal_tilt(signal[t]['ps_zscore'],
                            signal[t]['hc'])
             for t in SHORT_TICKERS}
short_total   = sum(short_raw.values())
short_weights = {t: v / short_total
                 for t, v in short_raw.items()}

ew_long  = 1.0 / len(LONG_TICKERS)
ew_short = 1.0 / len(SHORT_TICKERS)

print('Signal tilts:')
print(f'{"Ticker":<6} {"Z":>6} {"HC":<4} '
      f'{"Tilt":>6} {"SigWt":>7} {"BmWt":>7}')
print('-' * 42)
for t in LONG_TICKERS:
    z    = signal[t]['ps_zscore']
    hc   = signal[t]['hc']
    tilt = signal_tilt(z, hc)
    print(f'{t:<6} {z:>6.2f} {"Y" if hc else "-":<4} '
          f'{tilt:>6.1f}x {long_weights[t]:>6.1%} '
          f'{ew_long:>6.1%}')
for t in SHORT_TICKERS:
    z    = signal[t]['ps_zscore']
    hc   = signal[t]['hc']
    tilt = signal_tilt(z, hc)
    print(f'{t:<6} {z:>6.2f} {"Y" if hc else "-":<4} '
          f'{tilt:>6.1f}x {short_weights[t]:>6.1%} '
          f'{ew_short:>6.1%}')
print()

# ── Fetch current prices ──────────────────────────────────────
def fetch_price(ticker, retries=3):
    for attempt in range(retries):
        try:
            hist = yf.Ticker(ticker).history(period='5d')
            if not hist.empty:
                return round(float(
                    hist['Close'].iloc[-1]), 4)
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2)
            else:
                print(f'  Price fetch failed {ticker}: {e}')
    return None

def fetch_gbpusd(retries=3):
    for attempt in range(retries):
        try:
            hist = yf.Ticker('GBPUSD=X').history(period='5d')
            if not hist.empty:
                return round(float(
                    hist['Close'].iloc[-1]), 4)
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2)
    return None

print('Fetching prices...')
prices = {}
for t in ALL_TICKERS:
    prices[t] = fetch_price(t)
    status = f'${prices[t]}' if prices[t] else 'FAILED'
    print(f'  {t}: {status}')

gbpusd = fetch_gbpusd()
print(f'  GBPUSD: {gbpusd}')
print()

# ── Compute P&L vs previous month ────────────────────────────
total_sig_pnl = 0.0
total_bm_pnl  = 0.0
perf_rows     = []

if os.path.exists(POSITIONS_FILE):
    pos_hist  = pd.read_csv(POSITIONS_FILE)
    all_months = sorted(pos_hist['month'].unique())
    prev_months = [m for m in all_months if m < MONTH]

    if prev_months:
        prev_month = prev_months[-1]
        prev_pos   = pos_hist[
            pos_hist['month'] == prev_month].copy()

        print(f'Computing P&L vs {prev_month}:')
        print(f'{"Ticker":<6} {"Side":<6} '
              f'{"Entry":>8} {"Exit":>8} '
              f'{"SigP&L":>10} {"BmP&L":>10}')
        print('-' * 55)

        for _, row in prev_pos.iterrows():
            t        = row['ticker']
            entry_p  = row.get('entry_price_usd')
            exit_p   = prices.get(t)
            sig_sh   = row.get('sig_shares')
            bm_sh    = row.get('bm_shares')
            side     = row['side']

            if not all([exit_p, entry_p, sig_sh, bm_sh]):
                continue

            direction = -1 if side == 'short' else 1
            sig_pnl   = direction * sig_sh * (exit_p - entry_p)
            bm_pnl    = direction * bm_sh  * (exit_p - entry_p)
            total_sig_pnl += sig_pnl
            total_bm_pnl  += bm_pnl

            perf_rows.append({
                'month':       MONTH,
                'ticker':      t,
                'side':        side,
                'entry_price': entry_p,
                'exit_price':  exit_p,
                'sig_shares':  sig_sh,
                'bm_shares':   bm_sh,
                'sig_pnl_usd': round(sig_pnl, 2),
                'bm_pnl_usd':  round(bm_pnl, 2),
            })

            print(f'{t:<6} {side:<6} '
                  f'${entry_p:>7.2f} ${exit_p:>7.2f} '
                  f'${sig_pnl:>+9,.0f} '
                  f'${bm_pnl:>+9,.0f}')

        sig_ret = round(
            total_sig_pnl / STARTING_CAPITAL_USD * 100, 3)
        bm_ret  = round(
            total_bm_pnl  / STARTING_CAPITAL_USD * 100, 3)
        excess  = round(sig_ret - bm_ret, 3)

        print('-' * 55)
        print(f'Signal P&L    : ${total_sig_pnl:>+,.0f} '
              f'({sig_ret:+.2f}%)')
        print(f'Benchmark P&L : ${total_bm_pnl:>+,.0f} '
              f'({bm_ret:+.2f}%)')
        print(f'Excess return : {excess:+.2f}%')
        print()

        # Save performance record
        month_perf = pd.DataFrame([{
            'month':             MONTH,
            'prev_month':        prev_month,
            'sig_pnl_usd':       round(total_sig_pnl, 2),
            'bm_pnl_usd':        round(total_bm_pnl, 2),
            'sig_return_pct':    sig_ret,
            'bm_return_pct':     bm_ret,
            'excess_return_pct': excess,
        }])
        if os.path.exists(PERF_FILE):
            perf_hist = pd.read_csv(PERF_FILE)
            perf_hist = perf_hist[
                perf_hist['month'] != MONTH]
            perf_hist = pd.concat(
                [perf_hist, month_perf],
                ignore_index=True)
        else:
            perf_hist = month_perf
        perf_hist.to_csv(PERF_FILE, index=False)
        print(f'Performance saved to {PERF_FILE}')
    else:
        print('No previous month found -- '
              'P&L will begin next month.')
        sig_ret = bm_ret = excess = 0.0
else:
    print('No position history found -- '
          'this is the first rebalance.')
    sig_ret = bm_ret = excess = 0.0

# ── Build new month positions ─────────────────────────────────
new_positions = []

for t in LONG_TICKERS:
    p  = prices[t]
    w  = long_weights[t]
    n  = round(LONG_CAPITAL * w, 2)
    en = round(LONG_CAPITAL * ew_long, 2)
    new_positions.append({
        'month':             MONTH,
        'ticker':            t,
        'side':              'long',
        'regime':            'positive',
        'ps_zscore':         signal[t]['ps_zscore'],
        'hc_flag':           signal[t]['hc'],
        'sig_weight':        round(w, 4),
        'sig_notional_usd':  n,
        'sig_shares':        round(n / p, 4) if p else None,
        'entry_price_usd':   p,
        'bm_weight':         round(ew_long, 4),
        'bm_notional_usd':   en,
        'bm_shares':         round(en / p, 4) if p else None,
        'gbpusd':            gbpusd,
    })

for t in SHORT_TICKERS:
    p  = prices[t]
    w  = short_weights[t]
    n  = round(SHORT_CAPITAL * w, 2)
    en = round(SHORT_CAPITAL * ew_short, 2)
    new_positions.append({
        'month':             MONTH,
        'ticker':            t,
        'side':              'short',
        'regime':            'negative',
        'ps_zscore':         signal[t]['ps_zscore'],
        'hc_flag':           signal[t]['hc'],
        'sig_weight':        round(w, 4),
        'sig_notional_usd':  n,
        'sig_shares':        round(n / p, 4) if p else None,
        'entry_price_usd':   p,
        'bm_weight':         round(ew_short, 4),
        'bm_notional_usd':   en,
        'bm_shares':         round(en / p, 4) if p else None,
        'gbpusd':            gbpusd,
    })

# Append new positions to history
new_pos_df = pd.DataFrame(new_positions)
if os.path.exists(POSITIONS_FILE):
    pos_hist = pd.read_csv(POSITIONS_FILE)
    pos_hist = pos_hist[pos_hist['month'] != MONTH]
    pos_hist = pd.concat(
        [pos_hist, new_pos_df], ignore_index=True)
else:
    pos_hist = new_pos_df

pos_hist.to_csv(POSITIONS_FILE, index=False)

# ── Print new positions ───────────────────────────────────────
print()
print(f'NEW POSITIONS -- {MONTH}:')
print(f'{"Ticker":<6} {"Side":<6} {"SigWt":>6} '
      f'{"Notional":>12} {"Shares":>10} {"Price":>8}')
print('-' * 55)
for _, row in new_pos_df.iterrows():
    p_str = (f'${row["entry_price_usd"]:.2f}'
             if row['entry_price_usd'] else 'n/a')
    print(f'{row["ticker"]:<6} {row["side"]:<6} '
          f'{row["sig_weight"]:>5.1%} '
          f'${row["sig_notional_usd"]:>11,.0f} '
          f'{row["sig_shares"]:>10.1f} '
          f'{p_str:>8}')

print(f'\nPositions saved to {POSITIONS_FILE}')
print()
print('=' * 65)
print('REBALANCING COMPLETE')
print('=' * 65)
