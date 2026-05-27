"""
Ps Index Live Track Record -- Monthly Signal Generator
=======================================================

Methodology (two-stage, consistent with Paper 2):

  Stage 1: Own-history Z-score (signal identification)
    Each company's ps_raw is normalised against its own
    historical distribution. HC flag triggers at +1.5 sigma.

  Stage 2: Cross-sectional rank of own-history Z-scores
    (portfolio weighting)

Universe:
  Positive regime : MSFT, AMZN, CRM, SNOW, BABA  (long book)
  Negative regime : DDOG, TWLO, GTLB, MNDY        (short overlay)

BABA added June 2026 following confirmed positive signal
in full pipeline (adj 6M beta=+0.040, p=0.006).
First non-Western company in the Ps universe.

HC threshold: +1.5 sigma on own-history Z-score
"""

import os, time, math, json, requests
import pandas as pd
import numpy as np
import yfinance as yf
from scipy.stats import entropy as scipy_entropy
from datetime import datetime, timezone

# ── Configuration ─────────────────────────────────────────────
GITHUB_TOKEN = os.environ.get('GITHUB_PAT', '')
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept':        'application/vnd.github.v3+json',
}

HC_THRESHOLD   = 1.5
CHURN_FLOOR    = 100
WINDOW_DAYS    = 90
BATCH_SIZE     = 20
NOTIONAL_TOTAL = 10000  # GBP notional per side for paper trading

OUTPUT_DIR   = 'live_track_record'
HISTORY_FILE = f'{OUTPUT_DIR}/ps_signal_history.csv'
WEIGHTS_FILE = f'{OUTPUT_DIR}/monthly_weights.csv'
SERIES_DIR   = f'{OUTPUT_DIR}/ps_series'
# Ensure SERIES_DIR is always absolute
if not os.path.isabs(SERIES_DIR):
    SERIES_DIR = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'ps_series')
os.makedirs(SERIES_DIR, exist_ok=True)

# ── Universe ──────────────────────────────────────────────────
UNIVERSE = {
    'MSFT': {
        'regime':  'positive',
        'domains': ['microsoft.com'],
        'repos': [
            'microsoft/TypeScript',
            'microsoft/vscode',
            'microsoft/azure-sdk-for-python',
            'microsoft/semantic-kernel',
        ],
        'start': '2016-01-01T00:00:00Z',
        'calib': 0.378,
    },
    'AMZN': {
        'regime':  'positive',
        'domains': ['amazon.com'],
        'repos': [
            'aws/aws-sdk-js-v3',
            'aws/aws-cdk',
            'aws/amazon-sagemaker-examples',
            'aws/aws-cli',
        ],
        'start': '2016-01-01T00:00:00Z',
        'calib': 0.253,
    },
    'CRM': {
        'regime':  'positive',
        'domains': ['salesforce.com'],
        'repos': [
            'forcedotcom/salesforcedx-vscode',
            'salesforce/lwc',
            'salesforce/Argus',
            'forcedotcom/cli',
        ],
        'start': '2016-01-01T00:00:00Z',
        'calib': 0.524,
    },
    'SNOW': {
        'regime':  'positive',
        'domains': ['snowflake.com'],
        'repos': [
            'snowflakedb/snowflake-connector-python',
            'snowflakedb/gosnowflake',
            'snowflakedb/snowpark-python',
            'snowflakedb/snowflake-sqlalchemy',
        ],
        'start': '2019-01-01T00:00:00Z',
        'calib': 0.528,
    },
    'DDOG': {
        'regime':  'negative',
        'domains': ['datadoghq.com'],
        'repos': [
            'DataDog/datadog-agent',
            'DataDog/dd-trace-py',
            'DataDog/integrations-core',
            'DataDog/datadog-api-client-python',
        ],
        'start': '2016-01-01T00:00:00Z',
        'calib': 0.511,
    },
    'TWLO': {
        'regime':  'negative',
        'domains': ['twilio.com'],
        'repos': [
            'twilio/twilio-python',
            'twilio/twilio-node',
            'twilio/twilio-java',
            'twilio/twilio-go',
        ],
        'start': '2016-01-01T00:00:00Z',
        'calib': 0.903,
    },
    'GTLB': {
        'regime':  'negative',
        'domains': ['gitlab.com'],
        'repos': [
            # gitlab-foss replaces omnibus-gitlab which had
            # sparse corporate commits and caused silent drop
            'gitlab-org/gitlab-foss',
            'gitlabhq/gitlab-runner',
            'gitlabhq/terraform-provider-gitlab',
        ],
        'start': '2021-10-01T00:00:00Z',
        'calib': 0.511,
    },
    'MNDY': {
        'regime':  'negative',
        # Confirmed corporate domain: monday.com (single domain)
        # Israeli company -- Western email convention confirmed
        # Email format: firstname@ or shortname@monday.com
        # C6 pre-screen May 2026: 4/5 repos pass FPP >= 0.05
        # Pipeline result: 9/9 negative betas, 6M adj beta=-0.209
        # p=0.0001 -- strongest negative regime result in study
        'domains': ['monday.com'],
        'repos': [
            'mondaycom/vibe',              # FPP=0.140 anchor repo
            'mondaycom/monday-apps-cli',   # FPP=0.140
            'mondaycom/mcp',               # FPP=0.100 AI platform
            'mondaycom/monday-sdk-js',     # FPP=0.057 marginal
        ],
        'start': '2021-06-01T00:00:00Z',
        # Calibration approximated at 0.511 (same as DDOG)
        # pending cross-sectional calibration in Paper 2
        'calib': 0.511,
    },
    'BABA': {
        'regime':  'positive',
        # Both confirmed corporate email domains:
        # alibaba-inc.com: primary internal Alibaba Group domain
        # alibabacloud.com: Alibaba Cloud product engineering domain
        # Both confirmed in C6 pre-screen April 2026
        # aliyun org is domain-verified on GitHub
        'domains': ['alibaba-inc.com', 'alibabacloud.com'],
        'repos': [
            # Primary -- high corporate email rate, product engineering
            'aliyun/terraform-provider-alicloud',  # FPP=0.340
            'aliyun/alibabacloud-python-sdk',       # FPP=0.530
            'aliyun/alibabacloud-java-sdk',         # FPP=0.630
            # Secondary -- community-maintained, lower weight expected
            'alibaba/spring-cloud-alibaba',         # FPP=0.100
        ],
        'start': '2016-01-01T00:00:00Z',
        # Calibration factor approximated at 0.400 --
        # midpoint of positive regime range (0.253-0.528)
        # pending proper cross-sectional calibration in Paper 2
        'calib': 0.400,
    },
}

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

# ── Helpers ───────────────────────────────────────────────────
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
            resp = requests.get(
                url, headers=HEADERS,
                params=params, timeout=30)
        except Exception:
            return None
        if resp.status_code == 403:
            reset = int(resp.headers.get(
                'X-RateLimit-Reset',
                time.time() + 60))
            wait = max(reset - int(time.time()), 1)
            print(f'  Rate limit. Waiting {wait}s...')
            time.sleep(wait)
            continue
        if resp.status_code in [404, 451]:
            return None
        if resp.status_code != 200:
            return None
        return resp.json()

def compute_entropy(series, n_repos):
    counts = series.value_counts()
    if counts.sum() == 0:
        return 1.0
    probs = counts / counts.sum()
    H     = scipy_entropy(probs, base=2)
    H_max = math.log2(n_repos) if n_repos > 1 else 1.0
    return H / H_max if H_max > 0 else 0.0

def fetch_commits_90d(repo, domains, window_start, window_end):
    url    = f'https://api.github.com/repos/{repo}/commits'
    params = {
        'since':    window_start.isoformat(),
        'until':    window_end.isoformat(),
        'per_page': 100,
    }
    commits = []
    page    = 1
    consecutive_empty = 0

    while True:
        params['page'] = page
        data = api_get(url, params)
        if data is None or not isinstance(data, list) \
           or len(data) == 0:
            consecutive_empty += 1
            if consecutive_empty >= 3:
                break
            time.sleep(1)
            continue
        consecutive_empty = 0
        for c in data:
            email = ''
            if c.get('commit') and \
               c['commit'].get('author'):
                email = (c['commit']['author']
                         .get('email', '') or '')
            is_corp = any(
                d.lower() in email.lower()
                for d in domains)
            msg = ''
            if c.get('commit') and \
               c['commit'].get('message'):
                msg = c['commit']['message']
            commits.append({
                'sha':     c.get('sha', ''),
                'email':   email,
                'is_corp': is_corp,
                'message': msg[:200],
                'repo':    repo,
                'kw':      keyword_classify(msg),
            })
        page += 1
        time.sleep(0.25)

    return commits

def get_churn(repo, sha):
    url  = (f'https://api.github.com/repos/'
            f'{repo}/commits/{sha}')
    data = api_get(url)
    if data:
        stats = data.get('stats', {})
        return (stats.get('additions', 0) +
                stats.get('deletions', 0))
    return 0

def compute_ps_month(ticker, cfg, month_period):
    month_end    = (month_period.to_timestamp(how='end')
                    .replace(tzinfo=timezone.utc))
    window_start = month_end - pd.Timedelta(days=WINDOW_DAYS)

    repos   = cfg['repos']
    domains = cfg['domains']
    n_repos = len(repos)

    all_corp   = []
    all_struct = []

    for repo in repos:
        try:
            commits = fetch_commits_90d(
                repo, domains, window_start, month_end)
            corp_commits = [
                c for c in commits if c['is_corp']]
            all_corp.extend(corp_commits)

            for c in corp_commits:
                if c['kw'] != 'structural_candidate':
                    continue
                churn = get_churn(repo, c['sha'])
                time.sleep(0.15)
                if churn >= CHURN_FLOOR:
                    all_struct.append(
                        {**c, 'churn': churn})
        except Exception as e:
            print(f'  WARNING: error fetching {repo}: {e}')
            continue

    V   = len(all_corp)
    phi = len(all_struct) / V if V > 0 else 0.0

    if len(all_struct) > 0:
        repo_series = pd.Series(
            [s['repo'] for s in all_struct])
        H = compute_entropy(repo_series, n_repos)
    else:
        H = 1.0

    ps_raw = V * phi * (1 - H)

    if V == 0:
        print(f'  WARNING: {ticker} V=0 -- '
              f'check repo config and PAT permissions.')

    return {
        'V':            V,
        'phi':          round(phi, 4),
        'H':            round(H, 4),
        'entropy_gap':  round(1 - H, 4),
        'ps_raw':       round(ps_raw, 4),
        'n_corp':       V,
        'n_structural': len(all_struct),
    }

def load_own_history(ticker):
    path = f'{SERIES_DIR}/{ticker}_ps_series.csv'
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame(columns=['month', 'ps_raw'])

def own_history_zscore(ps_raw, history_series):
    if len(history_series) < 3:
        return 0.0
    mean = history_series.mean()
    std  = history_series.std()
    if std == 0:
        return 0.0
    return round((ps_raw - mean) / std, 4)

def cross_sectional_zscore(own_z_dict):
    values = list(own_z_dict.values())
    if len(values) < 2:
        return {t: 0.0 for t in own_z_dict}
    mean = np.mean(values)
    std  = np.std(values, ddof=1)
    if std == 0:
        return {t: 0.0 for t in own_z_dict}
    return {
        t: round((v - mean) / std, 4)
        for t, v in own_z_dict.items()
    }

# ── Portfolio weights ─────────────────────────────────────────
def fetch_price_gbp(ticker):
    """Fetch latest price in USD and convert to GBP."""
    try:
        info      = yf.Ticker(ticker)
        hist      = info.history(period='5d')
        if hist.empty:
            return None, None, None
        price_usd = float(hist['Close'].iloc[-1])
        fx        = yf.Ticker('GBPUSD=X')
        fx_h      = fx.history(period='5d')
        if fx_h.empty:
            return price_usd, None, None
        gbpusd    = float(fx_h['Close'].iloc[-1])
        price_gbp = price_usd / gbpusd
        return (round(price_usd, 4),
                round(price_gbp, 4),
                round(gbpusd, 4))
    except Exception as e:
        print(f'  Price fetch error {ticker}: {e}')
        return None, None, None

def compute_cs_weights(hc_rows):
    """
    Cross-sectional Z-score tilted weights for HC rows.
    Shifts scores to positive before normalising so all
    weights are non-negative.
    """
    if not hc_rows:
        return []
    cs_scores = np.array(
        [r['cs_z'] for r in hc_rows], dtype=float)
    min_score = cs_scores.min()
    if min_score < 0:
        cs_scores = cs_scores - min_score + 0.01
    total = cs_scores.sum()
    weights = (cs_scores / total if total > 0
               else np.ones(len(hc_rows)) / len(hc_rows))
    return [
        {'ticker': r['ticker'], 'weight': round(w, 4)}
        for r, w in zip(hc_rows, weights)
    ]

def build_weight_rows(hc_rows, side, regime,
                      month_period, notional_total):
    """Build weight rows for one side (long or short)."""
    rows = []
    for wt in compute_cs_weights(hc_rows):
        ticker = wt['ticker']
        row    = next(
            r for r in hc_rows
            if r['ticker'] == ticker)
        price_usd, price_gbp, gbpusd = \
            fetch_price_gbp(ticker)
        notional = round(notional_total * wt['weight'], 2)
        shares   = (round(notional / price_gbp, 4)
                    if price_gbp else None)
        rows.append({
            'month':         str(month_period),
            'ticker':        ticker,
            'side':          side,
            'signal_regime': regime,
            'ps_zscore':     row['ps_own_z'],
            'weight':        wt['weight'],
            'price_usd':     price_usd,
            'price_gbp':     price_gbp,
            'gbpusd':        gbpusd,
            'notional_gbp':  notional,
            'shares':        shares,
        })
        px_str = (f'@ £{price_gbp:.2f}'
                  if price_gbp else 'price n/a')
        print(f'  {side.upper():<5} {ticker}: '
              f'weight={wt["weight"]:.3f} '
              f'notional=£{notional:.0f} {px_str}')
    return rows

# ── Main ──────────────────────────────────────────────────────
def main():
    now = datetime.now(timezone.utc)
    if now.month == 1:
        signal_year  = now.year - 1
        signal_month = 12
    else:
        signal_year  = now.year
        signal_month = now.month - 1

    month_period = pd.Period(
        f'{signal_year}-{signal_month:02d}', freq='M')

    print('=' * 65)
    print(f'Ps Index Live Signal -- {month_period}')
    print('Stage 1: Own-history Z-score (signal id)')
    print('Stage 2: Cross-sectional rank (portfolio wt)')
    print(f'HC threshold: +{HC_THRESHOLD} sigma')
    print('Universe: MSFT, AMZN, CRM, SNOW, BABA (long)')
    print('          DDOG, TWLO, GTLB, MNDY (short overlay)')
    print('=' * 65)
    print()

    # ── Compute Ps for each company ───────────────────────────
    monthly_rows = {}
    own_z_dict   = {}

    for ticker, cfg in UNIVERSE.items():
        print(f'Computing {ticker} ({cfg["regime"]})...')
        try:
            ps_components = compute_ps_month(
                ticker, cfg, month_period)
        except Exception as e:
            print(f'  ERROR computing {ticker}: {e}')
            print(f'  Skipping {ticker} this month.')
            continue

        hist_df     = load_own_history(ticker)
        hist_raw    = list(hist_df['ps_raw'].values) + \
                      [ps_components['ps_raw']]
        hist_series = pd.Series(hist_raw)

        own_z = own_history_zscore(
            ps_components['ps_raw'], hist_series)
        own_z_dict[ticker] = own_z

        monthly_rows[ticker] = {
            'month':   str(month_period),
            'ticker':  ticker,
            'regime':  cfg['regime'],
            **ps_components,
            'ps_own_z': own_z,
        }

        new_row = pd.DataFrame([{
            'month':       str(month_period),
            'ps_raw':      ps_components['ps_raw'],
            'ps_own_z':    own_z,
            'V':           ps_components['V'],
            'phi':         ps_components['phi'],
            'H':           ps_components['H'],
            'entropy_gap': ps_components['entropy_gap'],
        }])
        updated = pd.concat(
            [hist_df, new_row], ignore_index=True)
        updated.to_csv(
            f'{SERIES_DIR}/{ticker}_ps_series.csv',
            index=False)
        print(f'  ps_raw={ps_components["ps_raw"]:.3f} '
              f'own_z={own_z:.3f}')

    print()

    # ── Stage 2: Cross-sectional Z-scores ────────────────────
    cs_z_dict = cross_sectional_zscore(own_z_dict)
    print('Cross-sectional Z-scores (Stage 2):')
    for ticker, cs_z in sorted(
            cs_z_dict.items(),
            key=lambda x: x[1], reverse=True):
        regime = UNIVERSE[ticker]['regime']
        print(f'  {ticker:<6} own_z={own_z_dict[ticker]:>6.3f} '
              f'cs_z={cs_z:>6.3f} [{regime}]')
    print()

    # ── Add Stage 2 and HC flags ──────────────────────────────
    output_rows = []
    for ticker, row in monthly_rows.items():
        own_z  = row['ps_own_z']
        cs_z   = cs_z_dict.get(ticker, 0.0)
        hc     = own_z >= HC_THRESHOLD
        hc_cs  = cs_z  >= HC_THRESHOLD
        output_rows.append({
            **row,
            'cs_z':       cs_z,
            'hc_flag':    hc,
            'hc_cs_flag': hc_cs,
        })

    # ── HC summary ────────────────────────────────────────────
    hc_pos = [r for r in output_rows
              if r['hc_flag'] and
              r['regime'] == 'positive']
    hc_neg = [r for r in output_rows
              if r['hc_flag'] and
              r['regime'] == 'negative']

    print('HC Episodes this month:')
    if hc_pos:
        print('  LONG signals (positive regime HC):')
        for r in hc_pos:
            print(f'    {r["ticker"]}: '
                  f'own_z={r["ps_own_z"]:.3f} '
                  f'cs_z={r["cs_z"]:.3f}')
    else:
        print('  No positive regime HC this month')

    if hc_neg:
        print('  SHORT signals (negative regime HC):')
        for r in hc_neg:
            print(f'    {r["ticker"]}: '
                  f'own_z={r["ps_own_z"]:.3f} '
                  f'cs_z={r["cs_z"]:.3f}')
    else:
        print('  No negative regime HC this month')
    print()

    # ── Save signal history ───────────────────────────────────
    if os.path.exists(HISTORY_FILE):
        history = pd.read_csv(HISTORY_FILE)
        history = history[
            history['month'] != str(month_period)]
    else:
        history = pd.DataFrame()

    new_rows_df = pd.DataFrame(output_rows)
    history     = pd.concat(
        [history, new_rows_df], ignore_index=True)
    history     = history.sort_values(
        ['month', 'ticker']).reset_index(drop=True)

    sig_cols = [
        'month', 'ticker', 'regime',
        'V', 'phi', 'H', 'entropy_gap',
        'ps_raw', 'ps_own_z', 'cs_z',
        'hc_flag', 'hc_cs_flag',
        'n_corp', 'n_structural',
    ]
    history = history[[
        c for c in sig_cols if c in history.columns]]
    history.to_csv(HISTORY_FILE, index=False)
    print(f'Signal saved to {HISTORY_FILE}')
    print(f'Total history rows: {len(history)}')
    print()

    # ── Portfolio weights ─────────────────────────────────────
    print('Computing portfolio weights...')
    weight_rows = []

    weight_rows += build_weight_rows(
        hc_pos, 'long', 'positive',
        month_period, NOTIONAL_TOTAL)

    weight_rows += build_weight_rows(
        hc_neg, 'short', 'negative',
        month_period, NOTIONAL_TOTAL)

    if not weight_rows:
        print('  No HC signals -- flat position this month')

    # Load and update weights history
    if os.path.exists(WEIGHTS_FILE):
        wt_hist = pd.read_csv(WEIGHTS_FILE)
        wt_hist = wt_hist[
            wt_hist['month'] != str(month_period)]
    else:
        wt_hist = pd.DataFrame()

    if weight_rows:
        new_wt_df = pd.DataFrame(weight_rows)
        wt_hist   = pd.concat(
            [wt_hist, new_wt_df], ignore_index=True)

    wt_cols = [
        'month', 'ticker', 'side', 'signal_regime',
        'ps_zscore', 'weight',
        'price_usd', 'price_gbp', 'gbpusd',
        'notional_gbp', 'shares',
    ]
    if not wt_hist.empty:
        wt_hist = wt_hist.sort_values(
            ['month', 'side', 'ticker']
        ).reset_index(drop=True)
        wt_hist = wt_hist[[
            c for c in wt_cols
            if c in wt_hist.columns]]

    wt_hist.to_csv(WEIGHTS_FILE, index=False)
    print(f'Weights saved to {WEIGHTS_FILE}')
    print()

    print('=' * 65)
    print('SIGNAL COMPLETE')
    print('=' * 65)


if __name__ == '__main__':
    main()
