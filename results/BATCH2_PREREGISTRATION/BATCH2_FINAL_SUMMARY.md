# Batch 2 Universe Expansion -- Final Summary
## Date: April 2026

## Overview
Six candidates tested against the seven-condition framework.
Two produced testable pipeline results. Four were untestable
due to Condition 6 observability constraints.

## Results by company

| Company | Predicted | Result     | Correct | Notes |
|---------|-----------|------------|---------|-------|
| GTLB    | Positive  | Negative   | No      | C7 missed -- GitHub moat |
| DT      | Negative  | No signal  | No      | C6 insufficient -- core proprietary |
| PLTR    | Uncertain | Failed C6  | N/A     | Low corporate email rate |
| NET     | Uncertain | Uncertain  | N/A     | 42-month period too thin |
| IOT     | Positive  | Failed C6  | N/A     | SDK repos only, core proprietary |
| PATH    | No signal | No signal  | Yes     | C3 failure validated |

## Framework learnings

### Condition 7 added
GTLB produced a negative signal despite satisfying C1-C6.
Post-result analysis identified the missing condition:
engineering investment must compound the moat not merely
maintain competitive parity. GitHub (Microsoft) has
structurally superior AI resources and network effects.
GitLab's engineering investment is defensive not compounding.

C7 is now retrospectively consistent with all existing signal
classifications and adds discriminating power for companies
that pass C1-C6 but compete in markets with structurally
superior incumbents.

### C3 failure validated
PATH confirmed that Condition 3 failure (no frictionless
consumption uplift) correctly predicts no signal. The framework
correctly discriminates:
- C3 pass + C7 pass → positive signal
- C3 pass + C7 fail → negative signal
- C3 fail → no signal

### C6 observability constraint documented
Three of six candidates failed C6 due to reasons not
previously encountered:
- PLTR: low corporate email rate (4-11% palantir.com)
- IOT: SDK-only repos, core IoT platform proprietary
- DT: passing repos but peripheral to core platform

The C6 constraint is more binding than originally anticipated.
Companies whose core engineering is proprietary and whose
open-source presence is limited to developer tooling or SDKs
are not observable with the current methodology.

## Universe changes from Batch 2
- Added to negative signal: GTLB
- Added to no signal: DT, PATH
- Added to failed C6: PLTR, IOT
- Added to insufficient period: NET
- No new positive signal companies

## Updated universe

| Category           | Companies                              |
|--------------------|----------------------------------------|
| Positive signal    | MSFT, AMZN, CRM, SNOW                 |
| Negative signal    | DDOG, TWLO, GTLB                      |
| No signal          | GOOGL, META, MDB, ESTC, AMD, DT, PATH |
| Failed C6          | CFLT, PLTR, IOT                        |
| Insufficient period| NET                                    |

## Commercial implications
Batch 2 did not meaningfully expand the positive signal universe.
The long book remains four companies. The short overlay expanded
from two to three companies (DDOG, TWLO, GTLB).

The C6 observability constraint is the primary barrier to universe
expansion. Companies with largely proprietary core engineering
cannot be observed with the GitHub commit methodology regardless
of their five-condition profile.

## Next steps
1. Commit PATH and IOT results to GitHub
2. Pre-register FSLY (Fastly) for Batch 3
3. Consider Batch 3 candidates that have strong C6 coverage:
   - Companies with genuinely public platform substrate repos
   - Not just SDK and developer tooling repos
   - Avoid companies with primarily proprietary core engineering
4. MSFT cache rebuild (pending)
5. SSRN paper (highest commercial priority)
