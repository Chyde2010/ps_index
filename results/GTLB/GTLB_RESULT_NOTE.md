# GTLB (GitLab) Pipeline Result
## Date: April 2026

## Pre-registration prediction: POSITIVE signal (high confidence)
## Empirical result: NEGATIVE signal

## Key findings
- Full 6M: adj beta=-0.1232, p=0.002, retention=123.2% -- NEGATIVE
- Low VIX 6M: adj beta=-0.1773, p=0.002 -- NEGATIVE
- High VIX 3M: adj beta=+0.1824, p=0.020, ret=144.8% -- PASS (positive)
- Q4 vs Q1 spread at 6M: -21.4pp (inverted -- negative signal)
- HC mean 6M return: -29.3% (all 4 HC episodes negative at 6M)
- Commercial bar passes: 1/9 (High VIX 3M only)

## Commercial verdict
NEGATIVE SIGNAL -- GTLB joins negative signal regime
alongside DDOG and TWLO.

The negative signal is significant and factor-adjusted at
the 6M horizon. GTLB adds to the short overlay universe.

## Framework learning
Pre-registration prediction was wrong. Five-condition framework
incorrectly classified GTLB as positive because it assessed
conditions in isolation rather than relative to competitive context.

Condition 7 added post-result: Engineering investment compounds
the moat. GTLB fails C7 because GitHub (Microsoft) can replicate
GitLab features with superior AI resources and network effects.
Engineering investment at GitLab maintains competitive parity
rather than compounding a proprietary technical advantage.

## Updated universe

Positive signal: MSFT, AMZN, CRM, SNOW
Negative signal: DDOG, TWLO, GTLB
No signal: GOOGL, META, MDB, ESTC, AMD
Failed C6: NET (original), CFLT
Failed C7 (post-hoc): GTLB

## Repos used (monorepo excluded)
- gitlabhq/gitlab-runner (CI execution)
- gitlabhq/gitlab-shell (Git access layer)
- gitlabhq/terraform-provider-gitlab (IaC integration)
- gitlabhq/omnibus-gitlab (platform packaging)

Note: gitlabhq/gitlabhq monorepo excluded due to size.
Supporting repos used as proxy for platform investment.
