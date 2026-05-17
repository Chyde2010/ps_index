# TEAM (Atlassian Corporation Plc) Pipeline Result
## Date: May 2026
## Exchange: NASDAQ
## Ticker: TEAM

## Pre-registration prediction: POSITIVE (high confidence)
## Empirical result: SIGNAL PRESENT, REGIME-DEPENDENT
##   Not commercially viable at 6M horizon in current environment.

---

## Classification: SIGNAL PRESENT -- REGIME-DEPENDENT

Pre-registration prediction was positive at high confidence.
Pipeline produced a time-split result across two structurally
distinct periods. Prediction was correct for 2018-2020 but
the 2025 HC episodes signal the same AI-disruption/restructuring
inflection mechanism as DOTD and MNDY.

Not added to live positive signal universe.
Not classified as negative regime.
Classified as: signal present, regime-dependent.

---

## Key findings

Regression summary (9 specifications):
  Positive adj betas: 3/9
  Negative adj betas: 6/9
  Adj significant   : 1/9
  Commercial bar    : 0/9

One significant result:
  High VIX 6M: adj beta=+0.115, p=0.047, n=33
  Raw beta=+0.194, p=0.0003 -- signal strongest in high stress
  Retention 59.5% -- below 70% commercial bar

HC episodes: 13
  2018-2020 cluster (11 episodes): strongly positive
  2025 cluster (2 episodes): strongly negative

Mean HC: 1M=+2.6%, 3M=+7.8%, 6M=+14.2%
  (positive overall but driven by 2018-2020 cluster)

Q4 vs Q1 spread at 6M: +13.7pp
  (positive direction -- but time-split caveat applies)

---

## HC episode detail

2018-2020 cluster (11 episodes) -- POSITIVE:
  2018-12 z=1.93 VIX=25.4: 6M=+47.0%
  2019-01 z=1.78 VIX=16.6: 6M=+42.4%
  2019-05 z=1.75 VIX=18.7: 6M= +1.0%
  2019-07 z=1.60 VIX=16.1: 6M= +4.9%
  2019-08 z=1.84 VIX=19.0: 6M= +7.8%
  2019-09 z=2.67 VIX=16.2: 6M= +9.4%
  2019-10 z=2.90 VIX=13.2: 6M=+28.7%
  2019-11 z=2.44 VIX=12.6: 6M=+45.8%
  2019-12 z=1.70 VIX=13.8: 6M=+49.8%
  2020-02 z=1.75 VIX=40.1: 6M=+32.3%
  2020-03 z=1.58 VIX=53.5: 6M=+32.4%
  Mean 6M (11 episodes): +27.4%

2025 cluster (2 episodes) -- NEGATIVE:
  2025-09 z=1.87 VIX=16.3: 6M=-57.3%
  2025-10 z=1.66 VIX=17.4: 6M=-59.5%
  Mean 6M (2 episodes): -58.4%

---

## Why the 2025 HC episodes turned negative

TEAM stock is down 57% in 2026 (as of March 2026).
Causes documented post-pipeline:

1. Workforce restructuring (March 2026): Atlassian announced
   layoffs of ~1,600 employees (10% of workforce) as it
   shifts resources toward AI and enterprise sales.
   Expected charges of $225-236 million.

2. AI disruption re-rating: Market repriced the TEAM multiple
   as investors reassessed which enterprise software business
   models are most vulnerable to AI seat compression.
   "Seat compression" concerns -- AI tools reducing per-team
   headcount which directly reduces Atlassian's per-seat
   revenue.

3. Tariff-driven risk-off: Broader macro de-rating of software
   stocks in February-March 2026. Atlassian fell 8.3% on
   February 23, 2026 alone amid software sector selloff.

4. Business fundamentals remained strong throughout:
   Q3 FY2026 revenue: $1.787bn, +32% YoY
   RPO: $3.996bn, +37% YoY
   The de-rating was multiple compression, not fundamental
   deterioration -- same mechanism as DOTD and MNDY.

---

## The signal mechanism

The 2025 HC episodes detected elevated engineering investment
at precisely the moment AI disruption risk was being priced
into the multiple. This is structurally identical to:
  - DOTD (2021): peak engineering intensity preceding
    Klaviyo/Braze competitive inflection and de-rating
  - MNDY (2021): peak investment preceding growth stock
    de-rating
  - DDOG (2026): active HC short signal

The Ps signal correctly identified that elevated structural
engineering investment in Sep-Oct 2025 was a response to
competitive pressure (from AI/GitHub Copilot/Linear) rather
than genuinely compounding the moat.

CEO Mike Cannon-Brookes explicitly stated AI changes
"the mix of skills" and "the number of roles required" --
confirming the structural shift the signal detected.

---

## C6 methodology discoveries (documented for Paper 2)

Three diagnostic rounds required for C6 confirmation.
Key methodological findings:

1. C6 Type 7 (new, documented May 2026):
   One-way monorepo mirror. atlassian/pragmatic-drag-and-drop
   is a daily sync from Atlassian's internal monorepo.
   All commits attributed to github@atlassian.com service
   account. FPP=0.000 -- bot commit messages do not trigger
   structural keywords. PR commit diagnostic confirmed:
   only 1 merged PR in study window. The code is publicly
   visible but all engineering is private. Distinct from
   C6 Type 6 (self-hosted GitLab) and C6 Type 1
   (GitHub Enterprise private concentration).

2. Privacy masking pattern:
   High-star community repos (compiled, nadel,
   data-center-helm-charts) show 80-87% GitHub privacy-
   masked addresses. These repos pass on corporate email
   rate when unmasked but privacy masking makes them
   unviable for the methodology.

3. Bot email exclusion protocol established:
   bots.bitbucket.org, users.noreply.github.com,
   github@atlassian.com excluded before FPP calculation.
   This is a new methodology step documented here for
   future pipeline runs.

4. Signal dominated by atlascode (82.5% of structural events):
   The VS Code extension for Jira and Bitbucket is the
   primary observable engineering signal. This is a
   developer ecosystem repo, not core product engineering.
   The C6 complexity noted in pre-registration confirmed --
   observable repos are peripheral to core Jira/Confluence.

---

## Repo contribution

| Repo                              | Structural | Share |
|-----------------------------------|------------|-------|
| atlassian/atlascode               | 510        | 82.5% |
| atlassian/openapi-request-validator| 76        | 12.3% |
| atlassian/gostatsd                | 26         |  4.2% |
| atlassian/date-time-api           | 6          |  1.0% |

atlascode dominance (82.5%) means the signal primarily
reflects developer ecosystem investment, not core platform.
This is consistent with the C6 complexity note in the
pre-registration.

---

## Live universe decision

TEAM is NOT added to the live signal universe.

Reasons:
1. 2025 HC episodes show negative returns inconsistent with
   positive regime classification.
2. AI disruption re-rating introduces regime uncertainty
   that cannot be resolved without more data points.
3. C6 complexity -- observable repos are peripheral to core
   product. Signal may not fully capture Jira/Confluence moat.
4. Commercial bar: 0/9 passes. High VIX 6M adjusted beta
   +0.115 is significant (p=0.047) but retention 59.5%
   is below 70% commercial bar threshold.

Revisit in 12 months when:
  - AI disruption impact on Atlassian's seat count is clearer
  - More data points exist post-2025 HC episodes
  - atlascode structural event pattern in 2026 is observable

---

## Paper 2 implications

Three contributions from TEAM pipeline documented here:

1. C6 Type 7 classification (monorepo mirror)
2. Bot email exclusion protocol
3. Regime-dependent signal -- same mechanism as DOTD/MNDY
   but in a company with a genuinely strong C7 argument.
   TEAM suggests the compounding moat narrative can be
   disrupted by platform-level AI substitution even for
   companies with deep switching costs.

---

## Summary

| Ticker | Company    | Predicted | Result            | Confidence |
|--------|------------|-----------|-------------------|------------|
| TEAM   | Atlassian  | Positive  | Regime-dependent  | High       |

Pre-registration prediction: technically incorrect at 6M horizon
  (0/9 commercial bar passes).
Signal mechanism: present and interpretable.
2018-2020: strongly positive (+27.4% mean HC 6M).
2025: strongly negative (-58.4% mean HC 6M).
Not added to live universe. Documented for Paper 2.
