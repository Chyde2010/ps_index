# PATH (UiPath) Pipeline Result
## Date: April 2026

## Pre-registration prediction: NO SIGNAL (high confidence)
## Empirical result: NO SIGNAL -- prediction correct

## Key findings
- Zero significant results across all 9 specifications
- All full-sample p-values above 0.40
- Q4 vs Q1 spread at 6M: -10.1pp (weakly negative, not significant)
- HC episodes: 6, all Jun 2025 to Feb 2026 (AI integration surge)
- HC mean 6M: -3.2% (only 2 complete observations)
- Corporate commits: 3,054
- Structural events: 437
- Merged observations: 60

## Framework validation
PATH confirms the Condition 3 prediction. Companies that fail C3
(frictionless consumption uplift) produce no detectable signal.
Engineering improvements to the UiPath automation platform require
active customer decisions to build new workflows before generating
additional consumption. There is no automatic uplift mechanism.

This is the same failure mode predicted for PagerDuty (never tested)
and partially responsible for the AMD no-signal result under the
original formula.

## Condition 3 failure mechanism
C3 requires that platform improvements automatically generate more
consumption from existing customers without active adoption decisions.
For UiPath:
- Better automation features require customers to build new workflows
- New workflow construction requires active IT investment decisions
- Revenue uplift is indirect and delayed by procurement cycles
- Engineering investment is not directly observable in consumption bills

Contrast with SNOW (C3 pass): better query performance automatically
generates more compute consumption from existing queries running on
existing customer workloads -- no customer action required.

## Repos used
- UiPath/uipath-python (FPP=0.110)
- UiPath/Community.Activities (FPP=0.090)
- UiPath/uipath-langchain-python (FPP=0.090)
- UiPath/apollo-ui (FPP=0.110)
Note: CoreWF excluded (FPP=0.043, below threshold)

## Updated universe
Positive signal    : MSFT, AMZN, CRM, SNOW
Negative signal    : DDOG, TWLO, GTLB
No signal          : GOOGL, META, MDB, ESTC, AMD, DT, PATH
Failed C6          : CFLT, PLTR, IOT
Insufficient period: NET
