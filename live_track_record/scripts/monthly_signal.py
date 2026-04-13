#!/usr/bin/env python3
"""
Ps Index Monthly Signal Computation -- v2
Corrected normalisation using phi calibration factor.
The calibration factor adjusts keyword-only phi to approximate
the churn-adjusted phi used in the backtest, enabling valid
normalisation against the historical ps_raw series.
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

HC_THRESHOLD = 1.5

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
        'repos': [
            'salesforce/lwc',
            'forcedotcom/salesforcedx-vscode',
            'salesforce/CodeAnalyzer',
        ]
    },
    'SNOW': {
        'signal_regime': 'positive',
        'domain': 'snowflake.com',
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
    """Load normalisation parameters from lookup file."""
    lookup_path = 'live_track_record/data/normalisation_lookup.csv'
    if not os.path.exists(lookup_path):
        return None
    df  = pd.read_csv(lookup_path)
    row = df[df['ticker'] == ticker]
    if len(row) == 0:
        return None
    return row.iloc[0].to_dict()

def compute_live_ps(ticker, company_config):
    """
    Compute current month Ps Z-score.

    Normalisation approach:
    1. Fetch 90-day rolling commits from all repos
    2. Classify by keyword (no churn fetch for rate limit reasons)
    3. Apply phi calibration factor to approximate churn-adjusted phi
    4. Compute ps_raw using calibrated phi
    5. Normalise against historical ps_raw mean and std
    """
    domain  = company_config['domain']
    repos   = company_config['repos']
    n_repos = len(repos)

    # Load normalisation parameters
    norm = load_normalisation(ticker)
    if norm is None:
        print(f'  {ticker}: Normalisation lookup not found')
        return None

    ps_raw_mean    = norm['ps_raw_mean']
    ps_raw_std     = norm['ps_raw_std']
    phi_calibration = norm['phi_calibration']

    # 90-day window
    now          = datetime.now(timezone.utc)
    window_start = now - pd.Timedelta(days=90)
    since_str    = window_start.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Fetch commits
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
                kw = keyword_classify(msg)
                all_commits.append({
                    'repo':    repo,
                    'is_corp': is_corp,
                    'kw_class': kw,
                })
            if len(data) < 100:
                break
            page += 1
            time.sleep(0.25)

    if not all_commits:
        print(f'  {ticker}: No commits found')
        return None

    df     = pd.DataFrame(all_commits)
    corp   = df[df['is_corp']]
    V      = len(corp)
    struct = corp[corp['kw_class'] == 'structural_candidate']

    # Keyword-only phi
    phi_kw = len(struct) / V if V > 0 else 0.0

    # Apply calibration factor to approximate churn-adjusted phi
    # calibration = hist_phi_mean / prescreen_fpp
    # phi_adj = phi_kw * calibration
    phi_adj = phi_kw * phi_calibration

    # Entropy gap
    H = compute_entropy_normalised(
        struct['repo'], n_repos) if len(struct) > 0 else 1.0

    # Compute calibrated ps_raw
    ps_raw_live = V * phi_adj * (1 - H)

    # Normalise against historical distribution
    ps_zscore = ((ps_raw_live - ps_raw_mean) / ps_raw_std
                 if ps_raw_std > 0 else 0.0)

    return {
        'date_committed':   now.strftime('%Y-%m-%d'),
        'ticker':           ticker,
        'signal_regime':    company_config['signal_regime'],
        'month':            now.strftime('%Y-%m'),
        'ps_zscore':        round(ps_zscore, 4),
        'high_conviction':  ps_zscore >= HC_THRESHOLD,
        'V':                V,
        'phi_kw':           round(phi_kw, 4),
        'phi_adj':          round(phi_adj, 4),
        'phi_calibration':  round(phi_calibration, 4),
        'H':                round(H, 4),
        'entropy_gap':      round(1 - H, 4),
        'ps_raw_live':      round(ps_raw_live, 4),
        'ps_raw_mean':      round(ps_raw_mean, 4),
        'ps_raw_std':       round(ps_raw_std, 4),
        'n_corp':           V,
        'n_structural_kw':  len(struct),
    }

def main():
    print('=' * 60)
    print('Ps Index Monthly Signal Computation v2')
    print(f'Date: {datetime.now(timezone.utc).strftime("%Y-%m-%d")}')
    print('Phi calibration applied to approximate churn floor.')
    print('=' * 60)

    results = []
    for ticker, config in COMPANIES.items():
        print(f'\nComputing {ticker}...')
        result = compute_live_ps(ticker, config)
        if result:
            results.append(result)
            hc = '*** HIGH CONVICTION ***' \
                 if result['high_conviction'] else ''
            print(f'  Ps Z-score  : {result["ps_zscore"]:>7.3f} '
                  f'({result["signal_regime"]}) {hc}')
            print(f'  V={result["V"]} '
                  f'phi_kw={result["phi_kw"]:.3f} '
                  f'phi_adj={result["phi_adj"]:.3f} '
                  f'H={result["H"]:.3f}')
            print(f'  ps_raw_live={result["ps_raw_live"]:.3f} '
                  f'(hist mean={result["ps_raw_mean"]:.3f} '
                  f'std={result["ps_raw_std"]:.3f})')

    if not results:
        print('ERROR: No results computed.')
        return

    # Save to live signals file
    signals_path = 'live_track_record/signals/live_signals.csv'
    new_df = pd.DataFrame(results)

    if os.path.exists(signals_path):
        existing = pd.read_csv(signals_path)
        # Remove any existing reading for this month
        existing = existing[
            ~((existing['month'] == new_df['month'].iloc[0]) &
              (existing['ticker'].isin(new_df['ticker'])))]
        combined = pd.concat([existing, new_df],
                              ignore_index=True)
    else:
        combined = new_df

    combined.to_csv(signals_path, index=False)

    # Monthly snapshot
    month_str     = datetime.now(timezone.utc).strftime('%Y-%m')
    snapshot_path = (f'live_track_record/signals/'
                     f'snapshot_{month_str}.csv')
    new_df.to_csv(snapshot_path, index=False)

    print('\n' + '=' * 60)
    print('MONTHLY SIGNAL SUMMARY')
    print('=' * 60)
    print(f'{"Ticker":<6} {"Regime":<10} '
          f'{"Ps Z":>8} {"HC":>5}')
    print('-' * 32)
    for r in results:
        hc = 'YES' if r['high_conviction'] else 'no'
        print(f'{r["ticker"]:<6} '
              f'{r["signal_regime"]:<10} '
              f'{r["ps_zscore"]:>8.3f} '
              f'{hc:>5}')

    print(f'\nSaved to {signals_path}')
    print(f'Snapshot: {snapshot_path}')

if __name__ == '__main__':
    main()
