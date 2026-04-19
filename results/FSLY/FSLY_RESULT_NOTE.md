# FSLY (Fastly) Pipeline Result
## Date: April 2026

## Pre-registration prediction: NEGATIVE (medium confidence)
## Empirical result: NO SIGNAL -- prediction partially wrong

## Key findings
- Zero significant adjusted results across all 9 specifications
- All full-sample p-values above 0.25
- HC episodes: 3, all May-Jul 2020 (COVID rally -- macro driven)
- HC mean 6M: +37.5% (strongly positive -- opposite direction)
- Q4 vs Q1 spread at 6M: -38.1pp (most negative in study)
- But quartile pattern non-monotonic -- dominated by outliers
- Corporate commits: 2,818
- Structural events: 495
- Merged observations: 76

## Why prediction was wrong
FSLY produces no signal rather than negative signal for two reasons:

1. HC episode confounding. All three HC episodes fall in May-Jul 2020
   -- the COVID reopening rally when every cloud/CDN company
   performed exceptionally well for macro reasons unrelated to
   engineering investment. The Ps Index peaked during this period
   but so did all cloud stocks. Factor adjustment cannot fully
   control for this extreme sector event. The signal is drowned
   out by macro noise during the most informative period.

2. Network layer invisibility. Fastly's strategically decisive
   engineering -- VCL configuration, edge POP software, network
   routing optimisation -- is entirely proprietary and never
   open-sourced. The five public repos (Viceroy, pushpin,
   js-compute-runtime, cli, go-fastly) capture the developer-facing
   layer but not the network infrastructure layer that differentiates
   Fastly's product and drives consumption revenue.

## New C6 constraint type identified
Three types of C6 failure now documented:

Type 1 -- Low corporate email observability (PLTR, IOT)
  Engineers commit with personal accounts. Domain filter captures
  too little of actual engineering activity.

Type 2 -- Peripheral repos only (DT)
  Corporate email observability good but passing repos are
  integration and tooling rather than platform substrate.

Type 3 -- Network layer invisibility (FSLY)
  Corporate email observability good and repos are platform-adjacent
  but strategically decisive engineering (CDN routing, network
  infrastructure) is never open-sourced by any company. Structural
  constraint specific to CDN and networking companies.

## Batch 3 implication
Avoid CDN and networking companies. Their core engineering is
structurally unobservable via GitHub regardless of open-source
presence. The public repos always capture developer-facing tooling
not the network layer that drives competitive differentiation.

## Repos used (5/5 pre-screen pass)
- fastly/Viceroy (FPP=0.140) -- edge compute runtime
- fastly/pushpin (FPP=0.220) -- real-time push infrastructure
- fastly/js-compute-runtime (FPP=0.120) -- JS edge runtime
- fastly/cli (FPP=0.150) -- developer toolchain
- fastly/go-fastly (FPP=0.290) -- API client

## Updated universe
Positive signal    : MSFT, AMZN, CRM, SNOW
Negative signal    : DDOG, TWLO, GTLB
No signal          : GOOGL, META, MDB, ESTC, AMD, DT, PATH, FSLY
Failed C6          : CFLT, PLTR, IOT
Insufficient period: NET
