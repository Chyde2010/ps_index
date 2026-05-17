# ADSK (Autodesk Inc.) Pipeline Result
## Date: May 2026
## Exchange: NASDAQ

## Pre-registration prediction: POSITIVE (medium confidence)
## Empirical result: NO SIGNAL -- C6 partial observability

---

## Classification: NO SIGNAL

Pre-registration predicted positive at medium confidence.
Pipeline produced 8/9 negative adjusted betas but all are
small in magnitude and mostly not statistically significant.
This is not a negative regime result -- it is a no-signal
result caused by fundamental C6 partial observability.

Not added to positive or negative signal universe.
Classified alongside GOOGL, META, MDB, ESTC, AMD, DT, INTU.

---

## Key findings

Regression summary:
  Positive adj betas: 1/9 (High VIX 6M: +0.006, p=0.807)
  Negative adj betas: 8/9
  Adj significant   : 1/9 (Low VIX 3M: -0.049, p=0.018)
  Commercial bar    : 0/9

HC episodes: 14
  Mean HC: 1M=+2.0%, 3M=-1.3%, 6M=+1.6%
  Essentially flat -- no directional HC signal

Q4 vs Q1 spread at 6M: -2.2pp
  Tiny negative -- effectively no relationship between
  Ps quartile and forward returns.

Structural events by repo:
  maya-usd   : 719 (95.5%) -- signal dominated by one repo
  bifrost-usd:  20 (2.7%)
  maya-hydra :  14 (1.9%)

---

## Why the prediction was wrong: C6 partial observability

NEW FAILURE MODE DOCUMENTED -- distinct from all previous
C6 classifications.

The Ps signal measured M&E USD engineering intensity
(bifrost-usd, maya-usd, maya-hydra). This segment represents
approximately 25-30% of Autodesk's total revenue.

ADSK stock returns are driven primarily by:
  - AEC segment: AutoCAD, Revit, Civil 3D (~45% of revenue)
  - Manufacturing: Fusion 360, Inventor, CAM (~30%)
  - M&E: Maya, Arnold, 3ds Max (~25%)

The AEC and Manufacturing engineering is entirely private
in Autodesk's 19,000 GitHub Enterprise repos. Only 85
repos are public -- open-source ecosystem connectors.

The observable M&E signal and the total ADSK stock return
are measuring different things. The mismatch produces
noise rather than signal. HC episodes track macro (pandemic
tech rally 2020, growth stock de-rating 2021-2022) rather
than company-specific engineering quality.

This is C6 partial observability -- distinct from:
  C6 Type 1: GitHub Enterprise private concentration
    (entire engineering is private)
  C6 Type 7: One-way monorepo mirror
    (mirror of private monorepo)
  C6 Type 8: Community handover (INTU)
    (community has taken over the repos)

C6 partial observability: a meaningful public engineering
presence exists but covers only a minority revenue segment.
The signal cannot predict total company returns because
the observable segment is insufficient.

Proposed classification: C6 Type 9: Partial observability
  Observable engineering represents <30% of revenue.
  Signal-to-noise ratio too low for commercial viability.

---

## HC episode analysis

2020 cluster (April-December, 8 episodes):
  Mean 6M return: +16.5%
  Context: pandemic tech rally lifted all SaaS/software
  stocks. HC episodes coincided with peak COVID momentum.
  Not company-specific signal -- macro-driven.

2021-2022 cluster (6 episodes):
  Mean 6M return: -17.6%
  Context: growth stock de-rating hit ADSK along with
  all SaaS. HC episodes coincided with rate rise fears.
  Not company-specific signal -- macro-driven.

The HC episodes are tracking macro rather than Autodesk
M&E engineering quality specifically. This confirms the
segment mismatch -- the M&E signal intensity correlates
with macro tech cycles, not ADSK-specific moat compounding.

---

## Pre-screen note: bifrost-usd FPP=0.333

The exceptional bifrost-usd FPP of 0.333 -- highest in
the entire study -- is real and reflects genuine structural
engineering investment in the Bifrost procedural VFX
platform. However with only 60 corporate commits and
only 20 structural events across the full study period,
bifrost-usd contributes only 2.7% of structural events
to the monthly Ps signal. The anchor repo (maya-usd)
at 95.5% of structural events drives the signal, and
maya-usd reflects M&E USD pipeline work that tracks
broadly with the M&E industry cycle, not ADSK returns.

---

## Implications for NASDAQ 100 universe expansion

ADSK confirms a pattern alongside INTU and TEAM:

Companies where C6 passes technically but the observable
engineering does not represent enough of the business
to produce a viable signal. INTU failed C6 due to
community handover. ADSK fails due to partial observability.
TEAM passed but showed regime-dependent signal tied to
AI disruption rather than clean positive or negative regime.

For NASDAQ 100 expansion, the viable candidates are those
where:
1. The observable engineering IS the core product
   (e.g. DDOG, SNOW, CRM -- already in universe)
2. OR the company has a dominant open-source strategy
   where the core product engineering is genuinely public

ADBE (Adobe) remains the last Tier 1 candidate.
Adobe's Spectrum design system and React Spectrum are
closer to core product engineering than Autodesk's
USD plugins. Worth assessing before concluding the
NASDAQ 100 expansion.

---

## Summary

| Ticker | Company   | Predicted | Result             |
|--------|-----------|-----------|--------------------|
| ADSK   | Autodesk  | Positive  | No signal          |

Failure mode: C6 Type 9 partial observability.
M&E segment signal (~25-30% revenue) does not predict
total ADSK returns. Observable engineering covers
minority revenue segment only.
Not added to live universe.
