#!/usr/bin/env python3
"""
Ps Index Monthly Signal Computation and Paper Trading v3
Runs on the first of each month via GitHub Actions.

Paper trading model:
- Portfolio size: GBP 1,000,000 notional
- Long book: MSFT, AMZN, CRM, SNOW (positive signal regime)
- Short overlay: DDOG, TWLO (negative signal regime)
- Position sizing: continuous signal scaling around neutral weight
- Benchmark: QQQ (technology sector ETF)
- Performance horizon: 6 months forward from entry
- Entry price: opening price on day of run (Yahoo Finance)
- FX: USD positions converted to GBP at prevailing GBPUSD rate

Long book tilt formula:
  position_weight = neutral_weight + (ps_zscore * TILT_FACTOR)
  weights normalised to sum to 100%
  capped at MAX_WEIGHT per position, floored at MIN_WEIGHT

Short overlay:
  short_weight = max(0, ps_zscore * SHORT_TILT_FACTOR)
  funded by reducing long book proportionally
"""

import os
import time
import math
import requests
import json
import pandas as pd
import numpy as np
from datetime import datetime, timezone, timedelta
from scipy.stats import entropy as scipy_entropy

# ── Configuration ─────────────────────────────────────────────
GITHUB_TOKEN = os.environ.get('PS_INDEX_PAT', '')
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept':        'application/vnd.github.v3+json'
}

HC_THRESHOLD       = 1.5
PORTFOLIO_GBP      = 1_000_000
NEUTRAL_WEIGHT     = 0.25       # 25% per long book company
TILT_FACTOR        = 0.05       # 5pp per 1 sigma Z-score
MAX_WEIGHT         = 0.45       # cap at 45% per position
MIN_WEIGHT         = 0.05       # floor at 5% per position
SHORT_TILT_FACTOR  = 0.03       # 3% short per 1 sigma Z-score
MAX_SHORT          = 0.10       # cap short at 10% per position
PERF_HORIZON_MONTHS = 6

STRUCTURAL_KEYWORDS = [
    'feature', 'api', 'add', 'new', 'implement', 'support',
    'introduce', 'enable', 'launch', 'release', 'capability',
    'extend', 'expose', 'create', 'build', 'integrate',
    'migrate', 'upgrade', 'enhance', 'generate', 'register',
    'replace', 'centralize', 'centralise', 'tune', 'optimize',
    'optimise', 'improve', 'expand', 'scale', 'port',
]
MAINTENANCE_KEYWORDS = [
    'fix', 'bug', 'patch', 'refactor', 'hotfix', 'revert',
    'deprecat', 'cleanup', 'clean up', 'typo', 'lint',
    'bump', 'changelog', 'merge branch', 'sync', 'pin',
    'update version', 'bump version', 'updating hashes',
    'update hashes', 'deploy', 'release notes',
]

COMPANIES = {
    'MSFT': {
        'signal_regime': 'positive',
        'domain': 'microsoft.com',
        'ticker_yf': 'MSFT',
        'repos': [
            'microsoft/onnxruntime',
            'microsoft/DeepSpeed',
            'Azure/azure-sdk-for-python',
            'microsoft/TypeChat',
            'microsoft/semantic-kernel',
        ]
    },
    'AMZN': {
        'signal_regime': 'positive',
        'domain': 'amazon.com',
        'ticker_yf': 'AMZN',
        'repos': [
            'aws/aws-cdk',
            'boto/boto3',
            'aws/amazon-sagemaker-examples',
            'aws/eks-distro',
            'aws/karpenter-provider-aws',
        ]
    },
    'CRM': {
        'signal_regime': 'positive',
        'domain': 'salesforce.com',
        'ticker_yf': 'CRM',
        'repos': [
            'salesforce/lwc',
            'forcedotcom/salesforcedx-vscode',
            'salesforce/CodeAnalyzer',
        ]
    },
    'SNOW': {
        'signal_regime': 'positive',
        'domain': 'snowflake.com',
        'ticker_yf': 'SNOW',
        'repos': [
            'snowflakedb/snowpark-python',
            'snowflakedb/snowflake-connector-python',
            'snowflakedb/snowflake-jdbc',
            'snowflakedb/gosnowflake',
            'snowflakedb/snowflake-connector-net',
            'snowflakedb/snowflake-kafka-connector',
        ]
    },
    'DDOG': {
        'signal_regime': 'negative',
        'domain': 'datadoghq.com',
        'ticker_yf': 'DDOG',
        'repos': [
            'DataDog/datadog-agent',
            'DataDog/integrations-core',
            'DataDog/dd-trace-py',
            'DataDog/dd-trace-go',
            'DataDog/datadog-operator',
        ]
    },
    'TWLO': {
        'signal_regime': 'negative',
        'domain': 'twilio.com',
        'ticker_yf': 'TWLO',
        'repos': [
            'twilio/twilio-python',
            'twilio/twilio-node',
            'twilio/twilio-go',
            'twilio/twilio-java',
            'twilio/twilio-cli',
            'twilio/twilio-ruby',
        ]
    },
}

LONG_TICKERS  = [t for t,c in COMPANIES.items()
                 if c['signal_regime'] == 'positive']
SHORT_TICKERS = [t for t,c in COMPANIES.items()
                 if c['signal_regime'] == 'negative']

def keyword_classify(message):
    msg = str(message).lower()
    if any(kw in msg for kw in MAINTENANCE_KEYWORDS):
        return 'maintenance'
    if any(kw in msg for kw in STRUCTURAL_KEYWORDS):
        return 'structural_candidate'
    return 'neutral'

def api_get(url, params=None):
    while True:
        try:
            resp = requests.get(url, headers=HEADERS,
                                params=params, timeout=30)
        except Exception:
            return None
        if resp.status_code == 403:
            reset = int(resp.headers.get(
                'X-RateLimit-Reset', time.time() + 60))
            wait = max(reset - int(time.time()), 1)
            print(f'Rate limit. Waiting {wait}s...')
            time.sleep(wait)
            continue
        if resp.status_code != 200:
            return None
        return resp.json()

def compute_entropy_normalised(series, n_repos):
    counts = series.value_counts()
    if counts.sum() == 0:
        return 1.0
    probs = counts / counts.sum()
    H     = scipy_entropy(probs, base=2)
    H_max = math.log2(n_repos) if n_repos > 1 else 1.0
    return H / H_max if H_max > 0 else 0.0

def load_normalisation(ticker):
    lookup_path = 'live_track_record/data/normalisation_lookup.csv'
    if not os.path.exists(lookup_path):
        return None
    df  = pd.read_csv(lookup_path)
    row = df[df['ticker'] == ticker]
    if len(row) == 0:
        return None
    return row.iloc[0].to_dict()

def fetch_price(ticker_yf):
    """Fetch current price from Yahoo Finance API."""
    try:
        url = (f'https://query1.finance.yahoo.com/v8/finance/'
               f'chart/{ticker_yf}?interval=1d&range=5d')
        resp = requests.get(url, timeout=15,
                            headers={'User-Agent': 'Mozilla/5.0'})
        if resp.status_code != 200:
            return None
        data = resp.json()
        closes = (data['chart']['result'][0]
                  ['indicators']['quote'][0]['close'])
        closes = [c for c in closes if c is not None]
        return closes[-1] if closes else None
    except Exception:
        return None

def fetch_gbpusd():
    """Fetch current GBPUSD rate from Yahoo Finance."""
    try:
        url = ('https://query1.finance.yahoo.com/v8/finance/'
               'chart/GBPUSD=X?interval=1d&range=5d')
        resp = requests.get(url, timeout=15,
                            headers={'User-Agent': 'Mozilla/5.0'})
        if resp.status_code != 200:
            return 1.27  # fallback
        data = resp.json()
        closes = (data['chart']['result'][0]
                  ['indicators']['quote'][0]['close'])
        closes = [c for c in closes if c is not None]
        return closes[-1] if closes else 1.27
    except Exception:
        return 1.27

def compute_live_ps(ticker, company_config):
    """Compute current month Ps Z-score."""
    domain  = company_config['domain']
    repos   = company_config['repos']
    n_repos = len(repos)

    norm = load_normalisation(ticker)
    if norm is None:
        return None

    ps_raw_mean     = norm['ps_raw_mean']
    ps_raw_std      = norm['ps_raw_std']
    phi_calibration = norm['phi_calibration']

    now          = datetime.now(timezone.utc)
    window_start = now - pd.Timedelta(days=90)
    since_str    = window_start.strftime('%Y-%m-%dT%H:%M:%SZ')

    all_commits = []
    for repo in repos:
        url    = f'https://api.github.com/repos/{repo}/commits'
        params = {'since': since_str, 'per_page': 100}
        page   = 1
        consecutive_empty = 0
        while True:
            params['page'] = page
            data = api_get(url, params)
            if data is None or len(data) == 0:
                consecutive_empty += 1
                if consecutive_empty >= 2:
                    break
                time.sleep(1)
                continue
            consecutive_empty = 0
            for c in data:
                email = ''
                if c.get('commit') and c['commit'].get('author'):
                    email = (c['commit']['author']
                             .get('email', '') or '')
                is_corp = domain.lower() in email.lower()
                msg = ''
                if c.get('commit') and c['commit'].get('message'):
                    msg = c['commit']['message']
                all_commits.append({
                    'repo':    repo,
                    'is_corp': is_corp,
                    'kw_class': keyword_classify(msg),
                })
            if len(data) < 100:
                break
            page += 1
            time.sleep(0.25)

    if not all_commits:
        return None

    df     = pd.DataFrame(all_commits)
    corp   = df[df['is_corp']]
    V      = len(corp)
    struct = corp[corp['kw_class'] == 'structural_candidate']

    phi_kw  = len(struct) / V if V > 0 else 0.0
    phi_adj = phi_kw * phi_calibration
    H       = compute_entropy_normalised(
        struct['repo'], n_repos) if len(struct) > 0 else 1.0

    ps_raw_live = V * phi_adj * (1 - H)
    ps_zscore   = ((ps_raw_live - ps_raw_mean) / ps_raw_std
                   if ps_raw_std > 0 else 0.0)

    return {
        'ticker':          ticker,
        'signal_regime':   company_config['signal_regime'],
        'month':           now.strftime('%Y-%m'),
        'date_committed':  now.strftime('%Y-%m-%d'),
        'ps_zscore':       round(ps_zscore, 4),
        'high_conviction': ps_zscore >= HC_THRESHOLD,
        'V':               V,
        'phi_kw':          round(phi_kw, 4),
        'phi_adj':         round(phi_adj, 4),
        'phi_calibration': round(phi_calibration, 4),
        'H':               round(H, 4),
        'entropy_gap':     round(1 - H, 4),
        'ps_raw_live':     round(ps_raw_live, 4),
        'ps_raw_mean':     round(ps_raw_mean, 4),
        'ps_raw_std':      round(ps_raw_std, 4),
        'n_corp':          V,
        'n_structural_kw': len(struct),
    }

def compute_portfolio_weights(signal_results):
    """
    Compute tilted portfolio weights from Ps Z-scores.

    Long book: neutral 25% per stock, tilted by Z-score.
    Short overlay: proportional to Z-score for negative
    signal companies, funded by reducing long book.
    Returns weights as fractions summing to 1.0 for long book.
    Short weights are separate and additive.
    """
    weights = {}

    # Long book -- tilt around neutral
    long_results = {t: r for t, r in signal_results.items()
                    if r['signal_regime'] == 'positive'}

    raw_weights = {}
    for ticker, result in long_results.items():
        z    = result['ps_zscore']
        w    = NEUTRAL_WEIGHT + (z * TILT_FACTOR)
        w    = max(MIN_WEIGHT, min(MAX_WEIGHT, w))
        raw_weights[ticker] = w

    # Normalise long book to sum to 1.0
    total = sum(raw_weights.values())
    for ticker in raw_weights:
        weights[ticker] = {
            'weight':         round(raw_weights[ticker] / total, 4),
            'side':           'long',
            'signal_regime':  'positive',
            'ps_zscore':      signal_results[ticker]['ps_zscore'],
        }

    # Short overlay -- proportional to Z-score
    short_results = {t: r for t, r in signal_results.items()
                     if r['signal_regime'] == 'negative'}

    for ticker, result in short_results.items():
        z = result['ps_zscore']
        # Only short when Z-score is positive
        short_w = max(0.0, min(MAX_SHORT, z * SHORT_TILT_FACTOR))
        weights[ticker] = {
            'weight':        round(short_w, 4),
            'side':          'short',
            'signal_regime': 'negative',
            'ps_zscore':     result['ps_zscore'],
        }

    return weights

def compute_portfolio_positions(weights, prices, gbpusd):
    """
    Translate weights into notional GBP positions.
    USD prices converted to GBP at prevailing rate.
    """
    positions = {}

    # Long book allocation
    long_allocation_gbp = PORTFOLIO_GBP

    # Reduce long allocation by short overlay size
    short_weights = {t: w for t, w in weights.items()
                     if w['side'] == 'short'}
    total_short_weight = sum(w['weight']
                             for w in short_weights.values())
    short_allocation_gbp = PORTFOLIO_GBP * total_short_weight
    long_allocation_gbp  = PORTFOLIO_GBP - short_allocation_gbp

    for ticker, w in weights.items():
        price_usd = prices.get(ticker)
        if price_usd is None:
            continue
        price_gbp = price_usd / gbpusd

        if w['side'] == 'long':
            notional_gbp = long_allocation_gbp * w['weight']
        else:
            notional_gbp = short_allocation_gbp * (
                w['weight'] / total_short_weight
                if total_short_weight > 0 else 0)

        shares = notional_gbp / price_gbp if price_gbp > 0 else 0

        positions[ticker] = {
            'side':          w['side'],
            'signal_regime': w['signal_regime'],
            'ps_zscore':     w['ps_zscore'],
            'weight':        w['weight'],
            'price_usd':     round(price_usd, 4),
            'price_gbp':     round(price_gbp, 4),
            'gbpusd':        round(gbpusd, 4),
            'notional_gbp':  round(notional_gbp, 2),
            'shares':        round(shares, 4),
        }

    return positions

def settle_matured_positions(month_str, prices, gbpusd):
    """
    Check if any positions opened 6 months ago are maturing.
    If so compute 6-month return vs QQQ benchmark.
    Returns list of settled position records.
    """
    positions_path = ('live_track_record/paper_trading/'
                      'open_positions.csv')
    settled_path   = ('live_track_record/paper_trading/'
                      'settled_positions.csv')
    perf_path      = ('live_track_record/paper_trading/'
                      'performance.csv')

    if not os.path.exists(positions_path):
        return []

    open_pos = pd.read_csv(positions_path)
    if len(open_pos) == 0:
        return []

    # Positions opened 6 months ago mature this month
    current_dt   = datetime.strptime(month_str, '%Y-%m')
    maturity_str = (current_dt - pd.DateOffset(months=6)
                    ).strftime('%Y-%m')

    maturing = open_pos[open_pos['entry_month'] == maturity_str]
    if len(maturing) == 0:
        return []

    # Fetch QQQ price for benchmark
    qqq_price_exit = fetch_price('QQQ')
    settled = []

    for _, pos in maturing.iterrows():
        ticker    = pos['ticker']
        exit_usd  = prices.get(ticker)
        if exit_usd is None:
            continue

        exit_gbp   = exit_usd / gbpusd
        entry_gbp  = pos['price_gbp']
        side       = pos['side']

        # Raw return
        if side == 'long':
            pct_return = (exit_gbp - entry_gbp) / entry_gbp
        else:
            pct_return = (entry_gbp - exit_gbp) / entry_gbp

        gbp_return = pos['notional_gbp'] * pct_return

        # QQQ benchmark return over same period
        qqq_entry  = pos.get('qqq_entry_price', None)
        if qqq_entry and qqq_price_exit:
            qqq_return = ((qqq_price_exit - float(qqq_entry))
                          / float(qqq_entry))
            alpha      = pct_return - qqq_return
        else:
            qqq_return = None
            alpha      = None

        record = {
            'entry_month':    pos['entry_month'],
            'exit_month':     month_str,
            'ticker':         ticker,
            'side':           side,
            'signal_regime':  pos['signal_regime'],
            'entry_ps_zscore': pos['ps_zscore'],
            'entry_price_gbp': round(entry_gbp, 4),
            'exit_price_gbp':  round(exit_gbp, 4),
            'notional_gbp':    pos['notional_gbp'],
            'pct_return':      round(pct_return * 100, 2),
            'gbp_return':      round(gbp_return, 2),
            'qqq_return_pct':  round(qqq_return * 100, 2)
                               if qqq_return else None,
            'alpha_pct':       round(alpha * 100, 2)
                               if alpha else None,
        }
        settled.append(record)

    return settled

def save_settled_positions(settled, month_str):
    """Append settled positions to performance record."""
    if not settled:
        return

    settled_path = ('live_track_record/paper_trading/'
                    'settled_positions.csv')
    new_df = pd.DataFrame(settled)

    if os.path.exists(settled_path):
        existing = pd.read_csv(settled_path)
        combined = pd.concat([existing, new_df],
                              ignore_index=True)
    else:
        combined = new_df

    combined.to_csv(settled_path, index=False)

def update_open_positions(positions, month_str,
                          qqq_price, settled_months):
    """
    Update open positions file.
    Remove settled positions, add new ones.
    """
    positions_path = ('live_track_record/paper_trading/'
                      'open_positions.csv')

    # Load existing open positions
    if os.path.exists(positions_path):
        existing = pd.read_csv(positions_path)
        # Remove matured positions
        existing = existing[
            ~existing['entry_month'].isin(settled_months)]
    else:
        existing = pd.DataFrame()

    # Add new positions opened this month
    new_records = []
    for ticker, pos in positions.items():
        if pos['weight'] == 0:
            continue
        new_records.append({
            'entry_month':    month_str,
            'ticker':         ticker,
            'side':           pos['side'],
            'signal_regime':  pos['signal_regime'],
            'ps_zscore':      pos['ps_zscore'],
            'weight':         pos['weight'],
            'price_usd':      pos['price_usd'],
            'price_gbp':      pos['price_gbp'],
            'gbpusd':         pos['gbpusd'],
            'notional_gbp':   pos['notional_gbp'],
            'shares':         pos['shares'],
            'qqq_entry_price': round(qqq_price, 4)
                               if qqq_price else None,
        })

    if new_records:
        new_df = pd.DataFrame(new_records)
        combined = pd.concat([existing, new_df],
                              ignore_index=True)
    else:
        combined = existing

    combined.to_csv(positions_path, index=False)

def compute_portfolio_summary(month_str):
    """
    Compute cumulative portfolio performance summary.
    """
    settled_path = ('live_track_record/paper_trading/'
                    'settled_positions.csv')
    perf_path    = ('live_track_record/paper_trading/'
                    'performance_summary.csv')

    if not os.path.exists(settled_path):
        return

    settled = pd.read_csv(settled_path)
    if len(settled) == 0:
        return

    # Summary statistics
    total_gbp_return  = settled['gbp_return'].sum()
    total_pct_return  = (total_gbp_return / PORTFOLIO_GBP * 100)
    mean_alpha        = settled['alpha_pct'].mean()
    win_rate          = (settled['pct_return'] > 0).mean() * 100
    n_settled         = len(settled)

    long_trades  = settled[settled['side'] == 'long']
    short_trades = settled[settled['side'] == 'short']

    summary = {
        'as_of_month':          month_str,
        'portfolio_size_gbp':   PORTFOLIO_GBP,
        'total_gbp_return':     round(total_gbp_return, 2),
        'total_pct_return':     round(total_pct_return, 2),
        'mean_alpha_pct':       round(mean_alpha, 2)
                                if not pd.isna(mean_alpha) else None,
        'win_rate_pct':         round(win_rate, 1),
        'n_settled_positions':  n_settled,
        'long_mean_return_pct': round(
            long_trades['pct_return'].mean(), 2)
            if len(long_trades) > 0 else None,
        'short_mean_return_pct': round(
            short_trades['pct_return'].mean(), 2)
            if len(short_trades) > 0 else None,
    }

    summary_df = pd.DataFrame([summary])
    if os.path.exists(perf_path):
        existing = pd.read_csv(perf_path)
        combined = pd.concat([existing, summary_df],
                              ignore_index=True)
    else:
        combined = summary_df
    combined.to_csv(perf_path, index=False)

    print(f'\nPORTFOLIO PERFORMANCE SUMMARY')
    print(f'  Total GBP return : £{total_gbp_return:,.0f}')
    print(f'  Total pct return : {total_pct_return:.1f}%')
    print(f'  Mean alpha       : {mean_alpha:.1f}%'
          if not pd.isna(mean_alpha) else
          '  Mean alpha       : n/a (< 6 months running)')
    print(f'  Win rate         : {win_rate:.0f}%')
    print(f'  Settled positions: {n_settled}')

def main():
    print('=' * 60)
    print('Ps Index Monthly Signal + Paper Trading v3')
    print(f'Date: {datetime.now(timezone.utc).strftime("%Y-%m-%d")}')
    print(f'Portfolio: GBP {PORTFOLIO_GBP:,.0f} notional')
    print('=' * 60)

    os.makedirs('live_track_record/paper_trading', exist_ok=True)
    os.makedirs('live_track_record/signals', exist_ok=True)

    month_str = datetime.now(timezone.utc).strftime('%Y-%m')

    # ── Step 1: Compute Ps Z-scores ───────────────────────────
    print('\nStep 1: Computing Ps Z-scores...')
    signal_results = {}
    for ticker, config in COMPANIES.items():
        print(f'  {ticker}...', end=' ', flush=True)
        result = compute_live_ps(ticker, config)
        if result:
            signal_results[ticker] = result
            hc = 'HC' if result['high_conviction'] else ''
            print(f'Z={result["ps_zscore"]:>7.3f} '
                  f'({result["signal_regime"]}) {hc}')
        else:
            print('FAILED')

    # ── Step 2: Fetch prices ──────────────────────────────────
    print('\nStep 2: Fetching prices...')
    prices  = {}
    gbpusd  = fetch_gbpusd()
    print(f'  GBPUSD: {gbpusd:.4f}')

    for ticker, config in COMPANIES.items():
        price = fetch_price(config['ticker_yf'])
        if price:
            prices[ticker] = price
            print(f'  {ticker}: ${price:.2f} USD '
                  f'(£{price/gbpusd:.2f} GBP)')
        else:
            print(f'  {ticker}: price fetch failed')

    qqq_price = fetch_price('QQQ')
    print(f'  QQQ  : ${qqq_price:.2f} USD' if qqq_price
          else '  QQQ  : price fetch failed')

    # ── Step 3: Settle matured positions (from 6 months ago) ──
    print('\nStep 3: Settling matured positions...')
    settled = settle_matured_positions(month_str, prices, gbpusd)
    if settled:
        save_settled_positions(settled, month_str)
        print(f'  Settled {len(settled)} positions')
        for s in settled:
            print(f'  {s["ticker"]} {s["side"]}: '
                  f'{s["pct_return"]:+.1f}% return '
                  f'(£{s["gbp_return"]:+,.0f}) '
                  f'alpha: {s["alpha_pct"]:+.1f}%'
                  if s["alpha_pct"] else
                  f'  {s["ticker"]}: {s["pct_return"]:+.1f}%')
    else:
        print('  No positions maturing this month')

    # ── Step 4: Compute new portfolio weights ─────────────────
    print('\nStep 4: Computing portfolio weights...')
    weights   = compute_portfolio_weights(signal_results)
    positions = compute_portfolio_positions(
        weights, prices, gbpusd)

    print(f'\n  {"Ticker":<6} {"Side":<6} '
          f'{"Weight":>7} {"Ps Z":>7} '
          f'{"Notional GBP":>14}')
    print(f'  {"-"*45}')
    for ticker, pos in positions.items():
        print(f'  {ticker:<6} {pos["side"]:<6} '
              f'{pos["weight"]*100:>6.1f}% '
              f'{pos["ps_zscore"]:>7.3f} '
              f'£{pos["notional_gbp"]:>13,.0f}')

    total_long = sum(
        p['notional_gbp'] for p in positions.values()
        if p['side'] == 'long')
    total_short = sum(
        p['notional_gbp'] for p in positions.values()
        if p['side'] == 'short')
    print(f'\n  Total long : £{total_long:,.0f}')
    print(f'  Total short: £{total_short:,.0f}')
    print(f'  Net exposure: £{total_long - total_short:,.0f}')

    # ── Step 5: Update open positions ────────────────────────
    settled_months = list(set(
        s['entry_month'] for s in settled)) if settled else []
    update_open_positions(
        positions, month_str, qqq_price, settled_months)

    # ── Step 6: Performance summary ──────────────────────────
    compute_portfolio_summary(month_str)

    # ── Step 7: Save signal readings ─────────────────────────
    signals_path  = 'live_track_record/signals/live_signals.csv'
    snapshot_path = (f'live_track_record/signals/'
                     f'snapshot_{month_str}.csv')

    new_signals = pd.DataFrame(list(signal_results.values()))
    if os.path.exists(signals_path):
        existing = pd.read_csv(signals_path)
        existing = existing[
            ~((existing['month'] == month_str) &
              (existing['ticker'].isin(new_signals['ticker'])))]
        combined = pd.concat([existing, new_signals],
                              ignore_index=True)
    else:
        combined = new_signals

    combined.to_csv(signals_path, index=False)
    new_signals.to_csv(snapshot_path, index=False)

    print(f'\nSignals saved to {signals_path}')
    print(f'Snapshot saved to {snapshot_path}')
    print('\nDone.')

if __name__ == '__main__':
    main()
