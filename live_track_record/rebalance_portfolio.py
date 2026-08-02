"""
Ps Index Paper Portfolio -- Monthly Rebalancer
==============================================

Runs automatically after monthly_signal.py in the
GitHub Actions workflow. Reads the current month signal
from live_signals.csv, computes signal-tilted weights,
fetches prices, records positions and P&L vs benchmark.

Structure:
  GBP 1,000,000 starting capital
  Long book : 70% -- positive regime (MSFT AMZN CRM SNOW BABA)
  Short book : 30% -- negative regime (DDOG TWLO GTLB MNDY)

Signal tilt (published methodology):
  HC signal (own_z >= 1.5) : 1.5x equal-weight share
  All other tickers        : 1.0x equal-weight share
  Weights normalised within each book.

Benchmark:
  Equal-weight same universe, same 70/30 capital split.
  Rebalanced monthly. Outperformance vs benchmark is
  attributable solely to the HC signal tilt.

P&L calculation:
  Uses stored sig_notional_usd and bm_notional_usd from
  prior month positions (canonical notional values).
  Converts USD P&L to GBP using prior month GBPUSD rate.

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
STARTING_CAPITAL_GBP = 1_000_000
LONG_PCT             = 0.70
SHORT_PCT            = 0.30
HC_MULTIPLIER        = 1.5
HC_THRESHOLD         = 1.5

OUTPUT_DIR     = 'live_track_record'
PORTFOLIO_DIR  = f'{OUTPUT_DIR}/paper_portfolio'
POSITIONS_FILE = f'{PORTFOLIO_DIR}/portfolio_positions.csv'
PERF_FILE      = f'{PORTFOLIO_DIR}/portfolio_performance.csv'

LONG_TICKERS   = ['MSFT', 'AMZN', 'CRM', 'SNOW', 'BABA']
SHORT_TICKERS  = ['DDOG', 'TWLO', 'GTLB', 'MNDY']
ALL_TICKERS    = LONG_TICKERS + SHORT_TICKERS

os.makedirs(PORTFOLIO_DIR, exist_ok=True)

# ── Determine current signal month ────────────────────────────
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

# ── Load signal from live_signals.csv ────────────────────────
live_signals_path = f'{OUTPUT_DIR}/signals/live_signals.csv'
if not os.path.exists(live_signals_path):
    print('ERROR: live_signals.csv not found.')
    sys.exit(1)

all_signals = pd.read_csv(live_signals_path)
snap = all_signals[all_signals['month'] == MONTH].copy()
if snap.empty:
    print(f'ERROR: No signal data for {MONTH}.')
    sys.exit(1)

print(f'Loading canonical signal from live_signals.csv')
print('Signal data loaded:')
cols = ['ticker', 'signal_regime', 'ps_zscore',
        'high_conviction']
print(snap[cols].to_string(index=False))
print()

# Build signal dict
signal = {}
for t in ALL_TICKERS:
    row = snap[snap['ticker'] == t]
    if row.empty:
        print(f'  WARNING: {t} missing -- z=0.0 hc=False')
        signal[t] = {'ps_zscore': 0.0, 'hc': False}
    else:
        signal[t] = {
            'ps_zscore': float(row['ps_zscore'].iloc[0]),
            'hc':        bool(row['high_conviction'].iloc[0]),
        }

# ── Signal weights (published methodology) ────────────────────
# HC = 1.5x share, non-HC = 1.0x share
# Normalised within each book
def compute_weights(tickers):
    raw   = {t: (HC_MULTIPLIER if signal[t]['hc']
                 else 1.0)
             for t in tickers}
    total = sum(raw.values())
    return {t: v/total for t, v in raw.items()}

long_weights  = compute_weights(LONG_TICKERS)
short_weights = compute_weights(SHORT_TICKERS)

ew_long  = 1.0 / len(LONG_TICKERS)
ew_short = 1.0 / len(SHORT_TICKERS)

print('Signal tilts:')
print(f'{"Ticker":<6} {"Z":>6} {"HC":<4}',
      f'{"SigWt":>7} {"BmWt":>7}')
print('-' * 36)
for t in LONG_TICKERS:
    z  = signal[t]['ps_zscore']
    hc = signal[t]['hc']
    print(f'{t:<6} {z:>6.2f} {"Y" if hc else "-":<4}',
          f'{long_weights[t]:>6.1%}',
          f'{ew_long:>6.1%}')
for t in SHORT_TICKERS:
    z  = signal[t]['ps_zscore']
    hc = signal[t]['hc']
    print(f'{t:<6} {z:>6.2f} {"Y" if hc else "-":<4}',
          f'{short_weights[t]:>6.1%}',
          f'{ew_short:>6.1%}')
print()

# ── Fetch prices ──────────────────────────────────────────────
def fetch_price(ticker, retries=3):
    for attempt in range(retries):
        try:
            h = yf.Ticker(ticker).history(period='5d')
            if not h.empty:
                return round(float(h['Close'].iloc[-1]), 4)
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2)
            else:
                print(f'  Price fetch failed {ticker}: {e}')
    return None

def fetch_gbpusd(retries=3):
    for attempt in range(retries):
        try:
            h = yf.Ticker('GBPUSD=X').history(period='5d')
            if not h.empty:
                return round(float(h['Close'].iloc[-1]), 4)
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2)
    return 1.30

print('Fetching prices...')
prices = {}
for t in ALL_TICKERS:
    prices[t] = fetch_price(t)
    print(f'  {t}: ${prices[t]}')

gbpusd = fetch_gbpusd()
print(f'  GBPUSD: {gbpusd}')
print()

# ── Compute P&L vs previous month ────────────────────────────
# Uses stored sig_notional_usd and bm_notional_usd
# from prior month positions (canonical notional values)
# Converts USD P&L to GBP using prior month GBPUSD rate
total_sig_pnl = 0.0
total_bm_pnl  = 0.0

if os.path.exists(POSITIONS_FILE):
    pos_hist    = pd.read_csv(POSITIONS_FILE)
    all_months  = sorted(pos_hist['month'].unique())
    prev_months = [m for m in all_months if m < MONTH]

    if prev_months:
        prev_month = prev_months[-1]
        prev_pos   = pos_hist[
            pos_hist['month'] == prev_month].copy()

        print(f'Computing P&L vs {prev_month}:')
        print(f'{"Ticker":<6} {"Side":<6}',
              f'{"Entry":>8} {"Exit":>8}',
              f'{"SigP&L":>10} {"BmP&L":>10}')
        print('-' * 55)

        for _, row in prev_pos.iterrows():
            t       = row['ticker']
            entry_p = float(row['entry_price_usd'])
            exit_p  = prices.get(t)
            sig_n   = float(row['sig_notional_usd'])
            bm_n    = float(row['bm_notional_usd'])
            side    = row['side']
            rate    = float(row['gbpusd'])

            if exit_p is None:
                print(f'  WARNING: no price for {t}')
                continue

            if side == 'long':
                ret = (exit_p - entry_p) / entry_p
            else:
                ret = (entry_p - exit_p) / entry_p

            s_pnl = ret * sig_n / rate
            b_pnl = ret * bm_n  / rate
            total_sig_pnl += s_pnl
            total_bm_pnl  += b_pnl

            print(f'{t:<6} {side:<6}',
                  f'${entry_p:>7.2f} ${exit_p:>7.2f}',
                  f'£{s_pnl:>+9,.0f} £{b_pnl:>+9,.0f}')

        sig_ret = round(
            total_sig_pnl / STARTING_CAPITAL_GBP * 100, 3)
        bm_ret  = round(
            total_bm_pnl  / STARTING_CAPITAL_GBP * 100, 3)
        excess  = round(sig_ret - bm_ret, 3)

        print('-' * 55)
        print(f'Signal P&L    : £{total_sig_pnl:>+,.0f}',
              f'({sig_ret:+.2f}%)')
        print(f'Benchmark P&L : £{total_bm_pnl:>+,.0f}',
              f'({bm_ret:+.2f}%)')
        print(f'Excess return : {excess:+.2f}%')
        print()

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
        print('No previous month -- P&L begins next month.')
        sig_ret = bm_ret = excess = 0.0
else:
    print('No position history -- first rebalance.')
    sig_ret = bm_ret = excess = 0.0

# ── Build new month positions ─────────────────────────────────
new_positions = []

for t in LONG_TICKERS:
    p  = prices[t]
    w  = long_weights[t]
    n_gbp    = STARTING_CAPITAL_GBP * LONG_PCT * w
    n_usd    = round(n_gbp * gbpusd, 2)
    bm_n_gbp = STARTING_CAPITAL_GBP * LONG_PCT * ew_long
    bm_n_usd = round(bm_n_gbp * gbpusd, 2)
    new_positions.append({
        'month':            MONTH,
        'ticker':           t,
        'side':             'long',
        'regime':           'positive',
        'ps_zscore':        signal[t]['ps_zscore'],
        'hc_flag':          signal[t]['hc'],
        'sig_weight':       round(w, 4),
        'sig_notional_usd': n_usd,
        'sig_shares':       round(n_usd/p, 4) if p else None,
        'entry_price_usd':  p,
        'bm_weight':        round(ew_long, 4),
        'bm_notional_usd':  bm_n_usd,
        'bm_shares':        round(bm_n_usd/p, 4) if p else None,
        'gbpusd':           gbpusd,
    })

for t in SHORT_TICKERS:
    p  = prices[t]
    w  = short_weights[t]
    n_gbp    = STARTING_CAPITAL_GBP * SHORT_PCT * w
    n_usd    = round(n_gbp * gbpusd, 2)
    bm_n_gbp = STARTING_CAPITAL_GBP * SHORT_PCT * ew_short
    bm_n_usd = round(bm_n_gbp * gbpusd, 2)
    new_positions.append({
        'month':            MONTH,
        'ticker':           t,
        'side':             'short',
        'regime':           'negative',
        'ps_zscore':        signal[t]['ps_zscore'],
        'hc_flag':          signal[t]['hc'],
        'sig_weight':       round(w, 4),
        'sig_notional_usd': n_usd,
        'sig_shares':       round(n_usd/p, 4) if p else None,
        'entry_price_usd':  p,
        'bm_weight':        round(ew_short, 4),
        'bm_notional_usd':  bm_n_usd,
        'bm_shares':        round(bm_n_usd/p, 4) if p else None,
        'gbpusd':           gbpusd,
    })

new_pos_df = pd.DataFrame(new_positions)
if os.path.exists(POSITIONS_FILE):
    pos_hist = pd.read_csv(POSITIONS_FILE)
    pos_hist = pos_hist[pos_hist['month'] != MONTH]
    pos_hist = pd.concat(
        [pos_hist, new_pos_df], ignore_index=True)
else:
    pos_hist = new_pos_df
pos_hist.to_csv(POSITIONS_FILE, index=False)

print()
print(f'NEW POSITIONS -- {MONTH}:')
print(f'{"Ticker":<6} {"Side":<6} {"SigWt":>6}',
      f'{"Notional GBP":>14} {"Shares":>10} {"Price":>8}')
print('-' * 58)
for _, row in new_pos_df.iterrows():
    n_gbp = row['sig_notional_usd'] / gbpusd
    print(f'{row["ticker"]:<6} {row["side"]:<6}',
          f'{row["sig_weight"]:>5.1%}',
          f'£{n_gbp:>13,.0f}',
          f'{row["sig_shares"]:>10.1f}',
          f'${row["entry_price_usd"]:>7.2f}')

print(f'\nPositions saved to {POSITIONS_FILE}')
print()
print('=' * 65)
print('REBALANCING COMPLETE')
print('=' * 65)
