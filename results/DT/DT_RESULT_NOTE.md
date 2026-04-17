# DT (Dynatrace) Pipeline Result
## Date: April 2026

## Pre-registration prediction: NEGATIVE signal
## Empirical result: NO SIGNAL

## Key findings
- Zero significant results across all 9 specifications
- All p-values above 0.20
- HC mean 6M return: +18.7% (positive -- opposite to prediction)
- Q4 vs Q1 spread at 6M: -0.0pp (flat -- no directional pattern)
- Corporate commits: 3,352 (thin dataset)
- Structural events: 377

## Why prediction was wrong
DT produces no signal rather than negative signal for two reasons:

1. Insufficient open-source coverage. Dynatrace's core engineering
   (OneAgent, Davis AI platform) is entirely proprietary. The four
   public repos (operator, config-as-code, otel-collector, backstage
   plugin) are integration and tooling repos peripheral to the core
   platform. 3,352 corporate commits provides insufficient statistical
   power to detect a consistent directional signal.

2. HC episodes are positive not negative. All 8 HC episodes fall in
   Oct 2022 to Jul 2023 and show positive forward returns (mean +18.7%
   at 6M). This contradicts the competitive parity hypothesis -- during
   periods of elevated DT engineering investment the stock performed
   well, suggesting the market rewarded the investment rather than
   penalising it as cost pressure.

## Framework learning
The negative signal regime requires BOTH:
- C7 failure (parity maintenance not moat compounding)
- Sufficient C6 coverage of strategically relevant engineering

DT fails C7 theoretically but the C6 proxy is too thin to detect
the signal. DDOG and TWLO have both C7 failure AND deep C6 coverage
(60,611 and 3,962 corporate commits respectively from platform repos).
DT's public repos capture peripheral engineering only.

## Updated classification
DT joins no-signal companies alongside GOOGL, META, MDB, ESTC, AMD.
Not because the business model is wrong but because the open-source
proxy is insufficient.

## Repos used
- Dynatrace/dynatrace-operator
- Dynatrace/dynatrace-configuration-as-code
- Dynatrace/dynatrace-otel-collector
- Dynatrace/backstage-plugin
Note: dynatrace-for-ai excluded (0 corporate commits)

## Updated universe
Positive signal: MSFT, AMZN, CRM, SNOW
Negative signal: DDOG, TWLO, GTLB
No signal: GOOGL, META, MDB, ESTC, AMD, DT
Failed C6: NET (original), CFLT
