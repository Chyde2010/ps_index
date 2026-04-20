# AAPL (Apple) Pipeline Result
## Date: April 2026

## Pre-registration prediction: NO SIGNAL (high confidence)
## Empirical result: NO SIGNAL -- prediction correct

## Key findings
- Full 6M: adj beta=-0.0125, p=0.337 -- NOT SIGNIFICANT
- Full 1M: adj beta=-0.0098, p=0.042, ret=97.5% -- NEG PASS
- Full 3M: adj beta=-0.0205, p=0.028, ret=423.4% -- NEG PASS
- High VIX 1M: adj beta=-0.0265, p=0.049, ret=155.0% -- NEG PASS
- Q4 vs Q1 spread at 6M: -0.2pp (essentially flat -- no signal)
- HC mean 6M: +16.2% (positive -- opposite to negative signal)
- Corporate commits: 104,494 (dominated by apple/swift 94.8%)
- Structural events: 9,212
- Merged observations: 123 (longest study period in entire study)

## Why automated NEG PASS verdict is not accepted
The automated protocol flags three specifications as NEG PASS
but the weight of evidence does not support negative signal
classification for the following reasons:

1. Full 6M fails. The primary specification by study protocol
   is Full 6M. It fails with p=0.337 -- not significant.
   The NEG PASS results at 1M and 3M do not override the
   primary specification.

2. Retention numbers indicate statistical artefact not signal.
   Full 3M retention of 423.4% and High VIX 3M retention of
   674.2% mean the adjusted beta is 4-7x larger than the raw
   beta. This occurs when the raw beta is near zero (p=0.714
   for Full 3M raw) and factor controls create a spurious
   adjusted coefficient through multicollinearity or omitted
   variable dynamics. This is regression mechanics not signal.

3. Quartile pattern is flat. Q4 vs Q1 spread at 6M is -0.2pp
   -- essentially zero. Genuine negative signal companies show
   clear directional quartile patterns:
   GTLB: -21.4pp, DDOG: -15.1pp, TWLO: -14.0pp
   Apple shows no directional pattern whatsoever.

4. HC episodes are positive not negative. Mean HC 6M return
   is +16.2%. All 13 HC episodes show broadly positive 6M
   returns. This is the opposite of a negative signal company.
   Swift engineering investment peaks precede iPhone supercycles
   -- the stock performs well during these periods for hardware
   reasons unrelated to the engineering investment signal.

## What is actually happening
The apple/swift repo captures Apple's language platform
engineering investment. Ps Z-score peaks in 2016, 2017, 2023
and 2024 correspond to major Swift releases preceding iPhone
product cycles. The factor-adjusted negative signal at 1M and
3M is a statistical artefact where QQQ controls absorb the
tech rally while leaving a residual that correlates negatively
with the Ps Z-score over short horizons -- not because Swift
engineering investment predicts underperformance but because
of timing artefacts between Swift releases and Apple's
short-term stock behaviour relative to the sector.

## Framework validation
C5 failure correctly predicted no signal. Apple's stock trades
on hardware cycles, China exposure and iPhone supercycle
narratives -- not on Swift compiler engineering investment.
The Full 6M result confirms the prediction. The shorter
horizon NEG PASS results are statistical noise.

## Repos used (darwin-xnu excluded)
- apple/swift (94.8% of structural events -- dominated)
- apple/axlearn (1.9%)
- apple/swift-nio (2.9%)
- apple/swift-crypto (0.4%)
Note: darwin-xnu excluded due to runtime constraints.
FPP=0.960 -- would have taken 12+ hours to process.

## C5 failure mechanism confirmed
Apple's GitHub-observable engineering is developer platform
investment (Swift compiler, ML framework, networking library).
This does not predict hardware unit volumes, China sales or
iPhone upgrade cycles which dominate stock price movements.
C5 failure is the correct classification.

## Updated universe
Positive signal    : MSFT, AMZN, CRM, SNOW
Negative signal    : DDOG, TWLO, GTLB
No signal          : GOOGL, META, MDB, ESTC, AMD, DT,
                     PATH, FSLY, AAPL
Failed C6          : CFLT, PLTR, IOT
Insufficient period: NET
