#!/usr/bin/env python3
"""
Ps Index Monthly Signal Computation
Runs on the first of each month via GitHub Actions.
Computes current Ps Z-score for each signal company
and commits the result to the repository.
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
    'Accept': 'application/vnd.github.v3+json'
}

HC_THRESHOLD = 1.5
CHURN_FLOOR  = 100

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

# Signal companies -- repos and domains
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
            'salesforce/einstein-platform',
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
        if resp.status_code not in [200]:
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

def compute_live_ps(ticker, company_config):
    """
    Compute the current month Ps Z-score for a company.
    Uses the 90-day rolling window ending today.
    Normalises against the historical Ps series from the
    merged file stored in the repository.
    """
    domain = company_config['domain']
    repos  = company_config['repos']

    # 90-day window
    now          = datetime.now(timezone.utc)
    window_start = now - pd.Timedelta(days=90)
    since_str    = window_start.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Fetch commits from each repo for the 90-day window
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
                    'message': msg[:200],
                    'kw_class': keyword_classify(msg),
                })
            if len(data) < 100:
                break
            page += 1
            time.sleep(0.25)

    if not all_commits:
        print(f'  {ticker}: No commits found')
        return None

    df      = pd.DataFrame(all_commits)
    corp    = df[df['is_corp']]
    V       = len(corp)
    struct  = corp[corp['kw_class'] == 'structural_candidate']

    # For live computation we use keyword classification only
    # without churn fetch -- churn fetch requires individual
    # commit API calls which would exceed rate limits monthly.
    # Live phi is therefore the keyword-only phi (no churn floor).
    # This is documented as a live track record methodology note.
    phi = len(struct) / V if V > 0 else 0.0
    H   = compute_entropy_normalised(
        struct['repo'], len(repos)) if len(struct) > 0 else 1.0
    ps_raw = V * phi * (1 - H)

    # Load historical Ps series to normalise
    hist_path = f'live_track_record/data/{ticker}_merged.csv'
    if not os.path.exists(hist_path):
        print(f'  {ticker}: Historical data not found')
        return None

    hist = pd.read_csv(hist_path)
    hist_mean = hist['ps_raw'].mean() if 'ps_raw' in hist.columns else 0
    hist_std  = hist['ps_raw'].std()  if 'ps_raw' in hist.columns else 1

    # Normalise using historical mean and std
    ps_zscore = ((ps_raw - hist_mean) / hist_std
                 if hist_std > 0 else 0.0)

    return {
        'ticker':          ticker,
        'signal_regime':   company_config['signal_regime'],
        'month':           now.strftime('%Y-%m'),
        'date_committed':  now.strftime('%Y-%m-%d'),
        'V':               V,
        'phi':             round(phi, 4),
        'H':               round(H, 4),
        'entropy_gap':     round(1 - H, 4),
        'ps_raw':          round(ps_raw, 4),
        'ps_zscore':       round(ps_zscore, 4),
        'high_conviction': ps_zscore >= HC_THRESHOLD,
        'n_corp':          V,
        'n_structural_kw': len(struct),
    }

def main():
    print('=' * 60)
    print('Ps Index Monthly Signal Computation')
    print(f'Date: {datetime.now(timezone.utc).strftime("%Y-%m-%d")}')
    print('=' * 60)

    results = []
    for ticker, config in COMPANIES.items():
        print(f'\nComputing {ticker}...')
        result = compute_live_ps(ticker, config)
        if result:
            results.append(result)
            hc = 'HC' if result['high_conviction'] else ''
            print(f'  Ps Z-score: {result["ps_zscore"]:.3f} '
                  f'({result["signal_regime"]}) {hc}')
            print(f'  V={result["V"]} '
                  f'phi={result["phi"]:.3f} '
                  f'entropy_gap={result["entropy_gap"]:.3f}')

    if not results:
        print('ERROR: No results computed.')
        return

    # Append to live signals file
    signals_path = 'live_track_record/signals/live_signals.csv'
    new_df = pd.DataFrame(results)

    if os.path.exists(signals_path):
        existing = pd.read_csv(signals_path)
        combined = pd.concat([existing, new_df],
                              ignore_index=True)
        combined = combined.drop_duplicates(
            subset=['month', 'ticker'], keep='last')
    else:
        combined = new_df

    combined.to_csv(signals_path, index=False)

    # Also save a monthly snapshot
    month_str    = datetime.now(timezone.utc).strftime('%Y-%m')
    snapshot_path = (f'live_track_record/signals/'
                     f'snapshot_{month_str}.csv')
    new_df.to_csv(snapshot_path, index=False)

    print('\n' + '=' * 60)
    print('SIGNAL SUMMARY')
    print('=' * 60)
    for r in results:
        hc = ' *** HIGH CONVICTION ***' if r['high_conviction'] else ''
        print(f'  {r["ticker"]:<6} '
              f'{r["signal_regime"]:<10} '
              f'Ps Z={r["ps_zscore"]:>7.3f}{hc}')

    print(f'\nResults saved to {signals_path}')
    print(f'Snapshot saved to {snapshot_path}')

if __name__ == '__main__':
    main()
