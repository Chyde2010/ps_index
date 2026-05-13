# MNDY (Monday.com Ltd) Pipeline Result
## Date: May 2026

## Pre-registration prediction: NEGATIVE signal (medium-low confidence)
## Empirical result: NEGATIVE signal CONFIRMED -- strong

---

## Key findings

Full sample:
- 1M: adj beta=-0.019, p=0.419  -- negative, not significant
- 3M: adj beta=-0.093, p=0.019  -- NEGATIVE, significant, PASS
- 6M: adj beta=-0.209, p=0.0001 -- NEGATIVE, highly significant, PASS

Subsets:
- Low VIX 6M:  adj beta=-0.206, p=0.0004 -- PASS
- High VIX 6M: adj beta=-0.221, p=0.0018 -- PASS

Negative adj betas: 9/9 -- complete directional consistency
Positive adj betas: 0/9
Commercial bar passes: 4/9 (3M full, 6M full, Low VIX 6M, High VIX 6M)

HC episodes: 6
- 2021-08: z=2.53, VIX=16.5, 6M=-58.1%
- 2021-09: z=3.02, VIX=23.1, 6M=-51.5%
- 2021-10: z=1.88, VIX=16.3, 6M=-65.2%
- 2022-03: z=1.55, VIX=20.6, 6M=-28.3%
- 2024-05: z=1.71, VIX=12.9, 6M=+26.3%  <- single positive outlier
- 2025-07: z=1.58, VIX=16.7, 6M=-56.3%
Mean HC: 1M=-6.9%, 3M=-15.5%, 6M=-38.8%

Quartile spread (Q4 vs Q1 at 6M): -57.5pp
Largest quartile spread in the entire study -- negative direction.
Q4 (highest Ps): -40.0% mean 6M return
Q1 (lowest Ps):  +17.4% mean 6M return

---

## Commercial verdict: NEGATIVE SIGNAL CONFIRMED

Pre-registration prediction CORRECT.
MNDY joins negative signal universe alongside DDOG, TWLO, GTLB.

---

## Why the signal is so strong

The 6M adj beta of -0.209 is more than double DDOG (-0.098) and
TWLO at the same horizon. Two explanations documented:

1. IPO timing effect: MNDY listed June 2021 at peak growth stock
   valuations. Highest engineering intensity (2021-H2) coincided
   with peak multiple expansion followed by severe drawdown in 2022.
   Signal may partially capture mean reversion of a growth stock
   priced for perfection at IPO. This is a documented caveat but
   does not invalidate the finding.

2. Genuine C7 signal: Work OS market is genuinely contested.
   Monday.com's engineering investment maintains competitive parity
   against Microsoft Teams/365, Asana, ClickUp and Notion rather
   than compounding an insurmountable structural moat. Every period
   of peak engineering investment corresponds to a period where
   monday.com was spending heavily to keep up rather than pull ahead.
   The market eventually prices this in negatively.

Both mechanisms are plausible and not mutually exclusive. The
pre-commitment discipline means the result stands regardless of
the mechanism.

---

## Technical note

High VIX 1M signal retained % of 1711.2% is an artefact.
Raw beta near zero (-0.003) makes the retention calculation
unstable at this horizon/regime. Ignore this specific figure.
The adjusted beta of -0.045 (p=0.228) is the meaningful statistic.

---

## Signal strength comparison (6M adj beta)

| Company | Regime   | 6M adj beta | p-value |
|---------|----------|-------------|---------|
| MNDY    | Negative | -0.209      | 0.0001  |
| DDOG    | Negative | -0.098      | 0.0025  |
| TWLO    | Negative | -0.098      | 0.0025  |
| GTLB    | Negative | --          | --      |
| MSFT    | Positive | +0.051      | 0.0004  |
| BABA    | Positive | +0.040      | 0.006   |

MNDY produces the strongest individual company result in the
negative regime by a significant margin.

---

## Impact on negative regime universe

Negative regime now has 4 companies: DDOG, TWLO, GTLB, MNDY.
This directly addresses the GTLB dependency identified in the
block bootstrap sensitivity analysis, where the negative regime
CI included zero without GTLB. With MNDY added, the negative
regime is more robust to individual company sensitivity.

---

## C7 wildcard assessment post-pipeline

The mcp (AI agent MCP server) repo contributed 30 structural
events (10.3% of total). The AI tooling investment is real
and growing. However the pipeline result is unambiguous --
9/9 negative betas with a 6M adj beta of -0.209 does not
support reassignment to positive regime. The mcp wildcard
did not materialise as a positive signal driver. C7 FAIL
confirmed by the data.

---

## Repo contribution

| Repo                   | Structural events | Share |
|------------------------|-------------------|-------|
| mondaycom/vibe         | 230               | 78.8% |
| mondaycom/mcp          | 30                | 10.3% |
| mondaycom/monday-apps-cli | 29             |  9.9% |
| mondaycom/monday-sdk-js | 3               |  1.0% |

vibe dominates at 78.8% -- the React design system is the
primary signal driver. sdk-js marginal contribution (3 events)
confirms the thin volume warning from pre-screen was correct.

---

## Updated universe

Positive signal    : MSFT, AMZN, CRM, SNOW, BABA
Negative signal    : DDOG, TWLO, GTLB, MNDY
No signal          : GOOGL, META, MDB, ESTC, AMD, DT
Failed C6          : NET, CFLT, PLTR, NU Holdings, Sea Ltd
Signal unrecoverable: MELI (EM macro dominance)
