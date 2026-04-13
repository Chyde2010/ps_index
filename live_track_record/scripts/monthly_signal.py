#!/usr/bin/env python3
"""
Ps Index Monthly Signal + Paper Trading v4
Continuous monthly rebalancing model.

Each month:
1. Compute Ps Z-scores for all six companies
2. Compute target weights from Z-scores
3. Fetch current prices
4. Value existing portfolio at current prices
5. Rebalance to target weights
6. Record NAV vs QQQ benchmark
7. Commit all results to GitHub

Portfolio: GBP 1,000,000 notional (inception May 2026)
Benchmark: QQQ
Rebalancing: monthly on the 1st
Long book: MSFT, AMZN, CRM, SNOW
Short overlay: DDOG, TWLO
"""

import os
import time
import math
import requests
import pandas as pd
import numpy as np
from datetime import datetime, timezone
from scipy.stats import entropy as scipy_entropy

# ── Configuration ─────────────────────────────────────────────
GITHUB_TOKEN = os.environ.get('PS_INDEX_PAT', '')
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept':        'application/vnd.github.v3+json'
}

HC_THRESHOLD        = 1.5
PORTFOLIO_INCEPTION = 1_000_000.0  # GBP

# Long book parameters
NEUTRAL_WEIGHT  = 0.25   # 25% per stock at zero signal
TILT_FACTOR     = 0.05   # 5pp weight shift per 1 sigma
MAX_WEIGHT      = 0.45   # cap per position
MIN_WEIGHT      = 0.05   # floor per position

# Short overlay parameters
SHORT_TILT      = 0.03   # 3% short per 1 sigma
MAX_SHORT       = 0.10   # cap per short position

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
        'domain':        'microsoft.com',
        'ticker_yf':     'MSFT',
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
        'domain':        'amazon.com',
        'ticker_yf':     'AMZN',
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
        'domain':        'salesforce.com',
        'ticker_yf':     'CRM',
        'repos': [
            'salesforce/lwc',
            'forcedotcom/salesforcedx-vscode',
            'salesforce/CodeAnalyzer',
        ]
    },
    'SNOW': {
        'signal_regime': 'positive',
        'domain':        'snowflake.com',
        'ticker_yf':     'SNOW',
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
        'domain':        'datadoghq.com',
        'ticker_yf':     'DDOG',
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
        'domain':        'twilio.com',
        'ticker_yf':     'TWLO',
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

# ── Utility functions ─────────────────────────────────────────
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
            print(f'    Rate limit. Waiting {wait}s...')
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
    path = 'live_track_record/data/normalisation_lookup.csv'
    if not os.path.exists(path):
        return None
    df  = pd.read_csv(path)
    row = df[df['ticker'] == ticker]
    return row.iloc[0].to_dict() if len(row) > 0 else None

def fetch_price(ticker_yf):
    try:
        url  = (f'https://query1.finance.yahoo.com/v8/finance/'
                f'chart/{ticker_yf}?interval=1d&range=5d')
        resp = requests.get(
            url, timeout=15,
            headers={'User-Agent': 'Mozilla/5.0'})
        if resp.status_code != 200:
            return None
        data   = resp.json()
        closes = (data['chart']['result'][0]
                  ['indicators']['quote'][0]['close'])
        closes = [c for c in closes if c is not None]
        return round(closes[-1], 4) if closes else None
    except Exception:
        return None

def fetch_gbpusd():
    try:
        url  = ('https://query1.finance.yahoo.com/v8/finance/'
                'chart/GBPUSD=X?interval=1d&range=5d')
        resp = requests.get(
            url, timeout=15,
            headers={'User-Agent': 'Mozilla/5.0'})
        if resp.status_code != 200:
            return 1.27
        data   = resp.json()
        closes = (data['chart']['result'][0]
                  ['indicators']['quote'][0]['close'])
        closes = [c for c in closes if c is not None]
        return round(closes[-1], 4) if closes else 1.27
    except Exception:
        return 1.27

# ── Signal computation ────────────────────────────────────────
def compute_live_ps(ticker, config):
    norm = load_normalisation(ticker)
    if norm is None:
        return None

    ps_raw_mean     = norm['ps_raw_mean']
    ps_raw_std      = norm['ps_raw_std']
    phi_calibration = norm['phi_calibration']
    domain          = config['domain']
    repos           = config['repos']
    n_repos         = len(repos)

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
                is_corp  = domain.lower() in email.lower()
                msg      = ''
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

    phi_kw      = len(struct) / V if V > 0 else 0.0
    phi_adj     = phi_kw * phi_calibration
    H           = (compute_entropy_normalised(
                   struct['repo'], n_repos)
                   if len(struct) > 0 else 1.0)
    ps_raw_live = V * phi_adj * (1 - H)
    ps_zscore   = ((ps_raw_live - ps_raw_mean) / ps_raw_std
                   if ps_raw_std > 0 else 0.0)

    return {
        'ticker':          ticker,
        'signal_regime':   config['signal_regime'],
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

# ── Portfolio construction ────────────────────────────────────
def compute_target_weights(signals):
    """
    Compute target portfolio weights from current Z-scores.
    Returns dict of ticker -> {weight, side}.
    Long book weights sum to 1.0 before short deduction.
    """
    weights = {}

    # Long book
    long_tickers = [t for t, s in signals.items()
                    if s['signal_regime'] == 'positive']
    raw = {}
    for t in long_tickers:
        z    = signals[t]['ps_zscore']
        w    = NEUTRAL_WEIGHT + (z * TILT_FACTOR)
        w    = max(MIN_WEIGHT, min(MAX_WEIGHT, w))
        raw[t] = w
    total = sum(raw.values())
    for t in long_tickers:
        weights[t] = {
            'weight': round(raw[t] / total, 6),
            'side':   'long',
        }

    # Short overlay
    short_tickers = [t for t, s in signals.items()
                     if s['signal_regime'] == 'negative']
    for t in short_tickers:
        z = signals[t]['ps_zscore']
        w = max(0.0, min(MAX_SHORT, z * SHORT_TILT))
        weights[t] = {
            'weight': round(w, 6),
            'side':   'short',
        }

    return weights

def value_portfolio(prev_weights_path, prices, gbpusd,
                    prev_nav_gbp):
    """
    Value existing portfolio at current prices.
    Returns current portfolio NAV in GBP.
    If no previous weights exist returns inception value.
    """
    if not os.path.exists(prev_weights_path):
        return prev_nav_gbp

    prev = pd.read_csv(prev_weights_path)
    if len(prev) == 0:
        return prev_nav_gbp

    # Most recent month weights
    last_month = prev['month'].max()
    prev_month = prev[prev['month'] == last_month]

    current_value_gbp = 0.0
    for _, row in prev_month.iterrows():
        ticker    = row['ticker']
        price_now = prices.get(ticker)
        if price_now is None:
            continue

        entry_price_gbp = row['price_gbp']
        notional_gbp    = row['notional_gbp']
        shares          = row['shares']
        side            = row['side']

        price_now_gbp = price_now / gbpusd
        position_value = shares * price_now_gbp

        if side == 'long':
            current_value_gbp += position_value
        else:
            # Short: profit if price fell
            pnl = notional_gbp - position_value
            current_value_gbp += notional_gbp + pnl

    return round(current_value_gbp, 2)

def compute_new_positions(weights, prices, gbpusd,
                          portfolio_nav_gbp, month_str):
    """
    Translate target weights into notional GBP positions.
    Short overlay funded by proportional reduction of long book.
    """
    total_short_weight = sum(
        w['weight'] for w in weights.values()
        if w['side'] == 'short')
    long_allocation  = portfolio_nav_gbp * (1 - total_short_weight)
    short_allocation = portfolio_nav_gbp * total_short_weight

    long_weights_total = sum(
        w['weight'] for w in weights.values()
        if w['side'] == 'long')

    positions = []
    for ticker, w in weights.items():
        price_usd = prices.get(ticker)
        if price_usd is None:
            continue
        price_gbp = price_usd / gbpusd

        if w['side'] == 'long':
            notional = (long_allocation *
                        w['weight'] / long_weights_total
                        if long_weights_total > 0 else 0)
        else:
            notional = (short_allocation *
                        w['weight'] / total_short_weight
                        if total_short_weight > 0 else 0)

        shares = notional / price_gbp if price_gbp > 0 else 0

        positions.append({
            'month':       month_str,
            'ticker':      ticker,
            'side':        w['side'],
            'signal_regime': COMPANIES[ticker]['signal_regime'],
            'ps_zscore':   signals_global.get(
                           ticker, {}).get('ps_zscore', 0),
            'weight':      w['weight'],
            'price_usd':   price_usd,
            'price_gbp':   round(price_gbp, 4),
            'gbpusd':      gbpusd,
            'notional_gbp': round(notional, 2),
            'shares':      round(shares, 4),
        })

    return positions

def record_nav(month_str, portfolio_nav, qqq_nav,
               inception_nav, qqq_inception):
    """Record monthly NAV for portfolio and benchmark."""
    nav_path = ('live_track_record/paper_trading/'
                'monthly_nav.csv')

    port_return_inception = ((portfolio_nav - inception_nav)
                              / inception_nav * 100)
    qqq_return_inception  = ((qqq_nav - qqq_inception)
                              / qqq_inception * 100)
    alpha_inception       = (port_return_inception
                              - qqq_return_inception)

    # Month-on-month return
    if os.path.exists(nav_path):
        existing = pd.read_csv(nav_path)
        if len(existing) > 0:
            prev_port = existing['portfolio_nav_gbp'].iloc[-1]
            prev_qqq  = existing['qqq_nav_usd'].iloc[-1]
            mom_port  = (portfolio_nav - prev_port) / prev_port * 100
            mom_qqq   = (qqq_nav - prev_qqq) / prev_qqq * 100
            mom_alpha = mom_port - mom_qqq
        else:
            mom_port = mom_qqq = mom_alpha = 0.0
    else:
        mom_port = mom_qqq = mom_alpha = 0.0

    record = {
        'month':                   month_str,
        'portfolio_nav_gbp':       round(portfolio_nav, 2),
        'portfolio_gbp_pnl':       round(
            portfolio_nav - inception_nav, 2),
        'portfolio_return_pct':    round(
            port_return_inception, 2),
        'portfolio_mom_return_pct': round(mom_port, 2),
        'qqq_nav_usd':             round(qqq_nav, 4),
        'qqq_return_pct':          round(
            qqq_return_inception, 2),
        'qqq_mom_return_pct':      round(mom_qqq, 2),
        'alpha_inception_pct':     round(alpha_inception, 2),
        'alpha_mom_pct':           round(mom_alpha, 2),
        'gbpusd':                  gbpusd_global,
    }

    new_df = pd.DataFrame([record])
    if os.path.exists(nav_path):
        existing = pd.read_csv(nav_path)
        existing = existing[existing['month'] != month_str]
        combined = pd.concat([existing, new_df],
                              ignore_index=True)
    else:
        combined = new_df
    combined.to_csv(nav_path, index=False)
    return record

# ── Global state for position construction ────────────────────
signals_global = {}
gbpusd_global  = 1.27

def main():
    global signals_global, gbpusd_global

    print('=' * 60)
    print('Ps Index Monthly Signal + Paper Trading v4')
    print(f'Date: {datetime.now(timezone.utc).strftime("%Y-%m-%d")}')
    print(f'Portfolio: GBP {PORTFOLIO_INCEPTION:,.0f} notional')
    print('Continuous monthly rebalancing model.')
    print('=' * 60)

    os.makedirs('live_track_record/paper_trading', exist_ok=True)
    os.makedirs('live_track_record/signals', exist_ok=True)

    month_str    = datetime.now(timezone.utc).strftime('%Y-%m')
    weights_path = ('live_track_record/paper_trading/'
                    'monthly_weights.csv')
    nav_path     = ('live_track_record/paper_trading/'
                    'monthly_nav.csv')

    # ── Step 1: Compute Ps Z-scores ───────────────────────────
    print('\nStep 1: Computing Ps Z-scores...')
    for ticker, config in COMPANIES.items():
        print(f'  {ticker}...', end=' ', flush=True)
        result = compute_live_ps(ticker, config)
        if result:
            signals_global[ticker] = result
            hc = 'HC' if result['high_conviction'] else ''
            print(f'Z={result["ps_zscore"]:>7.3f} '
                  f'({result["signal_regime"]}) {hc}')
        else:
            print('FAILED')

    # ── Step 2: Fetch prices ──────────────────────────────────
    print('\nStep 2: Fetching prices...')
    gbpusd_global = fetch_gbpusd()
    print(f'  GBPUSD: {gbpusd_global:.4f}')

    prices = {}
    for ticker, config in COMPANIES.items():
        price = fetch_price(config['ticker_yf'])
        if price:
            prices[ticker] = price
            print(f'  {ticker}: ${price:.2f} '
                  f'(£{price/gbpusd_global:.2f})')
        else:
            print(f'  {ticker}: fetch failed')

    qqq_price = fetch_price('QQQ')
    print(f'  QQQ  : ${qqq_price:.2f}' if qqq_price
          else '  QQQ  : fetch failed')

    # ── Step 3: Value existing portfolio ──────────────────────
    print('\nStep 3: Valuing existing portfolio...')

    # Load inception values
    if os.path.exists(nav_path):
        nav_df         = pd.read_csv(nav_path)
        inception_nav  = PORTFOLIO_INCEPTION
        qqq_inception  = (nav_df['qqq_nav_usd'].iloc[0]
                          if len(nav_df) > 0 else qqq_price)
        current_nav    = value_portfolio(
            weights_path, prices, gbpusd_global,
            nav_df['portfolio_nav_gbp'].iloc[-1]
            if len(nav_df) > 0 else PORTFOLIO_INCEPTION)
    else:
        # First run -- inception
        inception_nav = PORTFOLIO_INCEPTION
        qqq_inception = qqq_price if qqq_price else 100.0
        current_nav   = PORTFOLIO_INCEPTION

    print(f'  Current portfolio NAV: £{current_nav:,.2f}')
    print(f'  P&L vs inception: '
          f'£{current_nav - PORTFOLIO_INCEPTION:+,.2f}')

    # ── Step 4: Compute target weights ────────────────────────
    print('\nStep 4: Computing target weights...')
    weights = compute_target_weights(signals_global)

    print(f'  {"Ticker":<6} {"Side":<6} '
          f'{"Weight":>7} {"Ps Z":>8}')
    print(f'  {"-"*32}')
    for ticker, w in weights.items():
        z = signals_global.get(ticker, {}).get('ps_zscore', 0)
        print(f'  {ticker:<6} {w["side"]:<6} '
              f'{w["weight"]*100:>6.1f}% '
              f'{z:>8.3f}')

    # ── Step 5: Compute new positions ────────────────────────
    print('\nStep 5: Computing new positions...')
    positions = compute_new_positions(
        weights, prices, gbpusd_global,
        current_nav, month_str)

    # Compare to previous weights to show rebalancing trades
    if os.path.exists(weights_path):
        prev_weights = pd.read_csv(weights_path)
        last_month   = prev_weights['month'].max()                        if len(prev_weights) > 0 else None
        if last_month:
            prev_month_df = prev_weights[
                prev_weights['month'] == last_month]
            print(f'\n  Rebalancing trades vs {last_month}:')
            for pos in positions:
                ticker   = pos['ticker']
                new_w    = pos['weight']
                prev_row = prev_month_df[
                    prev_month_df['ticker'] == ticker]
                if len(prev_row) > 0:
                    old_w   = prev_row['weight'].iloc[0]
                    delta_w = new_w - old_w
                    delta_n = pos['notional_gbp'] -                               prev_row['notional_gbp'].iloc[0]
                    direction = ('BUY ' if delta_w > 0.001
                                 else 'SELL' if delta_w < -0.001
                                 else 'HOLD')
                    print(f'    {ticker}: {direction} '
                          f'{abs(delta_w)*100:.1f}pp '
                          f'(£{delta_n:+,.0f})')
                else:
                    print(f'    {ticker}: NEW position '
                          f'{new_w*100:.1f}%')

    # Save new weights
    new_weights_df = pd.DataFrame(positions)
    if os.path.exists(weights_path):
        existing = pd.read_csv(weights_path)
        existing = existing[existing['month'] != month_str]
        combined = pd.concat([existing, new_weights_df],
                              ignore_index=True)
    else:
        combined = new_weights_df
    combined.to_csv(weights_path, index=False)

    # ── Step 6: Record NAV ───────────────────────────────────
    print('\nStep 6: Recording NAV...')
    nav_record = record_nav(
        month_str, current_nav,
        qqq_price if qqq_price else 0,
        inception_nav,
        qqq_inception if qqq_inception else 0)

    print(f'\n  PERFORMANCE SUMMARY')
    print(f'  {"="*40}')
    print(f'  Portfolio NAV    : '
          f'£{nav_record["portfolio_nav_gbp"]:>12,.2f}')
    print(f'  P&L vs inception : '
          f'£{nav_record["portfolio_gbp_pnl"]:>+12,.2f}')
    print(f'  Portfolio return : '
          f'{nav_record["portfolio_return_pct"]:>+8.2f}%')
    print(f'  QQQ return       : '
          f'{nav_record["qqq_return_pct"]:>+8.2f}%')
    print(f'  Alpha            : '
          f'{nav_record["alpha_inception_pct"]:>+8.2f}%')
    print(f'  Month-on-month   : '
          f'{nav_record["portfolio_mom_return_pct"]:>+8.2f}%')

    # ── Step 7: Save signal readings ─────────────────────────
    signals_path  = 'live_track_record/signals/live_signals.csv'
    snapshot_path = (f'live_track_record/signals/'
                     f'snapshot_{month_str}.csv')

    new_signals = pd.DataFrame(list(signals_global.values()))
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

    print(f'\nAll files saved.')
    print(f'Next run: 1st of next month.')
    print('Done.')

if __name__ == '__main__':
    main()
