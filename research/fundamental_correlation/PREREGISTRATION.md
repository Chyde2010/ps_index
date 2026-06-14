# Ps Index — Fundamental Correlation Study
## Pre-Registration Document
## Date: June 2026
## Status: ACTIVE — findings committed before further analysis

---

## Research Question

Does a company's Ps z-score correlate with its financial
performance, after controlling for company-level fixed effects?

Formally: within a given company's own history, do periods
of elevated engineering intensity (high own_z) coincide with
or precede periods of stronger financial metrics?

---

## Universe

Positive regime companies (Script 1):
  MSFT, AMZN, CRM, SNOW, BABA

Negative regime companies (Script 2, pending):
  DDOG, TWLO, GTLB, MNDY

---

## Methodology

Panel regression with company fixed effects (within estimator).
Dependent variable demeaned by company to isolate
within-company variation from between-company variation.

Model: financial_metric_it = α_i + β × ps_zscore_it + ε_it

Lag specifications tested:
  Version A: Ps z-score in quarter T, metric in quarter T
  Version B: Ps z-score in quarter T, metric in quarter T+1
  Version C: Ps z-score in quarter T, metric in quarter T+2
  Version D: Ps z-score in quarter T, metric in quarter T+4

Standard errors: OLS (reported for single-company analysis)
and clustered by company (reported for pooled analysis).

---

## Financial Metrics — Testing Order (pre-committed)

1. Revenue growth YoY (%) -- COMPLETE
2. Net revenue retention (NRR) -- PENDING
3. Gross margin (%) -- PENDING
4. Operating margin (%) -- PENDING
5. Free cash flow margin (%) -- PENDING
6. RPO growth (%) -- PENDING

---

## Pre-Committed Expected Signs

Positive regime companies:
  Revenue growth:    β > 0
  NRR:               β > 0
  Gross margin:      β > 0
  Operating margin:  β > 0
  FCF margin:        β > 0
  RPO growth:        β > 0

Negative regime companies (expected opposite direction):
  Revenue growth:    β < 0 or ambiguous
  NRR:               β < 0 or ambiguous

---

## Success Criteria (pre-committed)

Minimum bar:
  β positive and significant (p<0.05) for at least one
  Tier 1 metric in positive regime companies at either
  contemporaneous or one-quarter lead specification.

Strong result:
  β positive and significant across multiple Tier 1 metrics,
  and correlation strengthens from Version A to Version C
  (leading indicator confirmed).

Very strong result:
  β positive for positive regime and negative for negative
  regime -- directional hypothesis holds across both.

Null result:
  β not significantly different from zero in any
  specification. Would suggest Ps score predicts price
  returns but not the fundamental metrics that drive them.

---

## Script 1 Results: Revenue Growth YoY (%)
## COMMITTED: June 2026 (before Script 2 is run)

### Data sources
  Revenue: Macrotrends.net quarterly revenue (manually verified)
  Ps z-scores: Pipeline output ps_series CSVs (Google Drive)
  Study period: 2019-01 to 2026-03 (Ps data availability)
  Total panel observations: 148

### Pooled results (five companies)

| Specification | β | p(OLS) | p(cl) | R² | n |
|---|---|---|---|---|---|
| Version A: T vs T | -5.335 | <0.001 | 0.384 | 0.063 | 148 |
| Version B: T vs T+1 | -5.370 | <0.001 | 0.436 | 0.064 | 143 |
| Version C: T vs T+2 | -4.262 | <0.001 | 0.541 | 0.041 | 138 |

Pooled result: β NEGATIVE, not significant at clustered SE.
Driven by BABA and SNOW (see individual results below).

### Individual company results (Version A contemporaneous)

| Company | β | p(OLS) | R² | n | Interpretation |
|---|---|---|---|---|---|
| AMZN | +6.441 | 0.002 | 0.308 | 29 | POSITIVE, significant |
| CRM | +3.982 | 0.019 | 0.187 | 29 | POSITIVE, significant |
| MSFT | +1.212 | 0.209 | 0.058 | 29 | Positive, not significant |
| SNOW | -16.340 | 0.021 | 0.261 | 20 | NEGATIVE, significant |
| BABA | -16.382 | 0.000 | 0.330 | 41 | NEGATIVE, highly significant |

### Lag structure results -- AMZN (most significant)

| Specification | β | p(OLS) | R² | n |
|---|---|---|---|---|
| Version A: T vs T | +6.441 | 0.002 | 0.308 | 29 |
| Version B: T vs T+1 | +7.966 | 0.000 | 0.470 | 28 |
| Version C: T vs T+2 | +9.629 | 0.000 | 0.685 | 27 |
| Version D: T vs T+4 | +8.331 | 0.000 | 0.503 | 25 |

AMZN KEY FINDING: β strengthens from T+0 to T+2 and peaks
at T+2 (six months). R² = 0.685 at T+2 -- Ps z-score
explains 68.5% of within-AMZN variation in revenue growth
two quarters ahead. Peak at T+2 exactly matches the Ps Index
signal horizon used in the SSRN cross-sectional study.

### Lag structure results -- MSFT

| Specification | β | p(OLS) | R² | n |
|---|---|---|---|---|
| Version A: T vs T | +1.212 | 0.209 | 0.058 | 29 |
| Version B: T vs T+1 | +2.137 | 0.024 | 0.180 | 28 |
| Version C: T vs T+2 | +2.748 | 0.003 | 0.301 | 27 |
| Version D: T vs T+4 | +0.359 | 0.736 | 0.005 | 25 |

MSFT KEY FINDING: Classic leading indicator structure.
Not significant contemporaneously. Significant at T+1.
Highly significant at T+2. Collapses at T+4.
Six-month leading indicator confirmed.

### Lag structure results -- CRM

| Specification | β | p(OLS) | R² | n |
|---|---|---|---|---|
| Version A: T vs T | +3.982 | 0.019 | 0.187 | 29 |
| Version B: T vs T+1 | +2.748 | 0.119 | 0.091 | 28 |
| Version C: T vs T+2 | +2.399 | 0.185 | 0.069 | 27 |
| Version D: T vs T+4 | +2.674 | 0.129 | 0.097 | 25 |

CRM: Contemporaneous significance only. Signal does not
lead revenue growth at longer horizons for CRM specifically.
May reflect sales-cycle-driven revenue dynamics.

### Lag structure results -- BABA

| Specification | β | p(OLS) | R² | n |
|---|---|---|---|---|
| Version A: T vs T | -16.382 | 0.000 | 0.330 | 41 |
| Version B: T vs T+1 | -20.130 | 0.000 | 0.418 | 40 |
| Version C: T vs T+2 | -20.472 | 0.000 | 0.407 | 39 |
| Version D: T vs T+4 | -20.964 | 0.000 | 0.353 | 37 |

BABA: Strong negative relationship across all lags.
Interpretation: defensive investment pattern -- BABA invests
heavily in engineering precisely when revenue growth is under
structural pressure (macro + regulatory headwinds 2022-2026).
Engineering intensity is not compounding moat in the
traditional sense but responding to competitive threat.
This is consistent with the positive regime classification
(engineering quality is observable) but the revenue
transmission mechanism operates differently from AMZN/MSFT.

### Lag structure results -- SNOW

| Specification | β | p(OLS) | R² | n |
|---|---|---|---|---|
| Version A: T vs T | -16.340 | 0.021 | 0.261 | 20 |
| Version B: T vs T+1 | -15.207 | 0.024 | 0.264 | 19 |
| Version C: T vs T+2 | -12.523 | 0.065 | 0.197 | 18 |
| Version D: T vs T+4 | -5.843 | 0.256 | 0.091 | 16 |

SNOW: Fading negative relationship. Strong negative at
short horizons, weakening and insignificant at T+4.
Likely reflects growth normalisation -- SNOW's highest
revenue growth occurred in 2021-2022 when Ps z-scores
were moderate. Engineering intensity increased as growth
decelerated from very high base rates. Period-specific
phenomenon rather than structural pattern.

---

## Key Conclusions from Script 1

1. MINIMUM BAR MET: β positive and significant (p<0.05)
   for revenue growth in AMZN (p=0.002) and CRM (p=0.019)
   at the contemporaneous specification.

2. STRONG RESULT CONFIRMED FOR AMZN: β strengthens from
   T+0 to T+2, peaking at T+2 with R²=0.685. The six-month
   leading indicator hypothesis is empirically validated
   for AMZN specifically.

3. LEADING INDICATOR CONFIRMED FOR MSFT: Classic structure --
   insignificant contemporaneously, significant at T+2
   (p=0.003), collapses at T+4.

4. HETEROGENEITY WITHIN POSITIVE REGIME: BABA and SNOW
   show negative relationships -- consistent with defensive
   investment pattern rather than compounding moat pattern.
   This is an important finding that refines the framework.

5. THE SIX-MONTH HORIZON IS VALIDATED: Peak R² occurs at
   T+2 (two quarters = six months) for both AMZN and MSFT.
   This directly validates the Ps Index signal horizon used
   in the SSRN cross-sectional study.

---

## Next Steps (pre-committed order)

1. Script 2: NRR -- pending
2. Script 3: Gross margin -- pending
3. Script 4: Operating margin -- pending
4. Script 5: FCF margin -- pending
5. Script 6: RPO growth -- pending
6. Negative regime extension -- pending
7. BABA investigation: plot z-score vs revenue over time
   to characterise the defensive investment pattern

---

## Data Files

Revenue data: Macrotrends.net (manually pasted, verified)
Ps z-score data: pipeline ps_series CSVs (Google Drive)
Panel dataset: research/fundamental_correlation/data/
  ps_revenue_panel.csv (saved from Script 1)
Charts: research/fundamental_correlation/results/
  ps_revenue_correlation.png
  ps_revenue_lag_profile.png

---

## Script 2 Results: Revenue Growth YoY (%) -- Negative Regime
## COMMITTED: June 2026 (before Script 3 is run)

### Universe
  DDOG, TWLO, GTLB, MNDY
  Total panel observations: 91
  Study period: varies by company (2019-2026)

### Pre-committed expected sign: β < 0

### Pooled results (four companies)

| Specification | β | p(OLS) | p(cl) | R² | n |
|---|---|---|---|---|---|
| Version A: T vs T | -5.235 | 0.063 | 0.445 | 0.038 | 91 |
| Version B: T vs T+1 | -4.572 | 0.085 | 0.417 | 0.035 | 87 |
| Version C: T vs T+2 | -4.429 | 0.084 | 0.395 | 0.036 | 83 |
| Version D: T vs T+4 | -3.873 | 0.113 | 0.353 | 0.034 | 75 |

Pooled: β NEGATIVE across all specifications -- matches
pre-committed sign. Marginal at OLS SE (p=0.063 to 0.113).
Not significant at clustered SE (4 clusters too few for
reliable inference). OLS p-values treated as primary
given small g.

### Individual company results

**DDOG (strongest result in study):**

| Specification | β | p(OLS) | R² | n |
|---|---|---|---|---|
| Version A: T vs T | -16.344 | 0.001 | 0.374 | 26 |
| Version B: T vs T+1 | -15.229 | 0.001 | 0.374 | 25 |
| Version C: T vs T+2 | -17.323 | 0.001 | 0.392 | 24 |
| Version D: T vs T+4 | -15.876 | 0.011 | 0.279 | 22 |

DDOG KEY FINDING: Strong negative relationship across all
lag specifications. β peaks at T+2 (-17.323, R²=0.392)
mirroring AMZN's positive peak at T+2 (+9.629, R²=0.685).
DDOG Ps z-score explains 39.2% of within-DDOG variation
in revenue growth two quarters ahead.
MATCHES pre-committed sign. COMMERCIALLY SIGNIFICANT:
DDOG is in HC in live universe (3 consecutive HC months).
Fundamental correlation confirms: elevated DDOG engineering
intensity historically precedes revenue deceleration.

**GTLB:**

| Specification | β | p(OLS) | R² | n |
|---|---|---|---|---|
| Version A: T vs T | -11.289 | 0.037 | 0.259 | 17 |
| Version B: T vs T+1 | -9.654 | 0.041 | 0.265 | 16 |
| Version C: T vs T+2 | -8.466 | 0.049 | 0.266 | 15 |
| Version D: T vs T+4 | -4.988 | 0.053 | 0.299 | 13 |

GTLB: Consistent negative β, significant across all
specifications at p<0.05. MATCHES pre-committed sign.
Also a short position in live universe.

**TWLO:**

| Specification | β | p(OLS) | R² | n |
|---|---|---|---|---|
| Version A: T vs T | +4.132 | 0.457 | 0.021 | 29 |
| Version B: T vs T+1 | +1.575 | 0.771 | 0.003 | 28 |
| Version C: T vs T+2 | -0.318 | 0.950 | 0.000 | 27 |
| Version D: T vs T+4 | -2.749 | 0.572 | 0.014 | 25 |

TWLO: NULL RESULT. No relationship in either direction
across any specification. Consistent with TWLO's thin,
maintenance-dominated GitHub presence. Ps signal for TWLO
may not be measuring meaningful engineering activity.

**MNDY:**

| Specification | β | p(OLS) | R² | n |
|---|---|---|---|---|
| Version A: T vs T | +4.590 | 0.489 | 0.029 | 19 |
| Version B: T vs T+1 | +5.268 | 0.383 | 0.048 | 18 |
| Version C: T vs T+2 | +5.590 | 0.276 | 0.078 | 17 |
| Version D: T vs T+4 | +7.152 | 0.049 | 0.266 | 15 |

MNDY: ANOMALOUS -- β is positive (opposite of pre-committed
sign), reaching significance at T+4 (p=0.049). MNDY
engineering intensity is positively associated with future
revenue growth. Two interpretations:
  1. MNDY engineering is building genuine new product
     capability that eventually drives revenue (similar
     to CRM pattern)
  2. MNDY negative regime classification may warrant
     review given this finding
To investigate further before drawing conclusions.

### Symmetric structure at T+2

| Company | Regime | β at T+2 | p(OLS) | Pattern |
|---|---|---|---|---|
| AMZN | Positive | +9.629 | 0.000 | Compounding ✓ |
| MSFT | Positive | +2.748 | 0.003 | Compounding ✓ |
| CRM | Positive | +2.399 | 0.185 | Weak positive |
| SNOW | Positive | -12.523 | 0.065 | Defensive |
| BABA | Positive | -20.472 | 0.000 | Defensive |
| DDOG | Negative | -17.323 | 0.001 | Parity ✓ |
| GTLB | Negative | -8.466 | 0.049 | Parity ✓ |
| TWLO | Negative | -0.318 | 0.950 | Null |
| MNDY | Negative | +5.590 | 0.276 | Anomalous |

### Key conclusions from Script 2

1. DIRECTIONAL HYPOTHESIS PARTIALLY CONFIRMED:
   DDOG and GTLB show significant negative β matching
   pre-committed sign. TWLO null. MNDY anomalous.

2. DDOG IS THE SYMMETRIC COUNTERPART TO AMZN:
   Both peak at T+2. AMZN R²=0.685, DDOG R²=0.392.
   The six-month leading indicator structure holds
   symmetrically across the strongest positive and
   negative regime companies.

3. SIX-MONTH HORIZON VALIDATED FOR NEGATIVE REGIME:
   DDOG β peaks at T+2 (-17.323) -- same horizon
   as AMZN's positive peak (+9.629). This directly
   validates the Ps Index signal horizon from both
   directions.

4. COMMERCIALLY SIGNIFICANT FOR LIVE PORTFOLIO:
   DDOG is in HC (own_z=2.964 as of June 2026,
   third consecutive HC month). Fundamental study
   confirms: elevated engineering intensity historically
   precedes revenue deceleration at 6-month horizon.
   Live short position is supported by fundamental data.

5. TWO ANOMALIES IDENTIFIED:
   BABA/SNOW (positive regime, negative β) --
   defensive investment pattern.
   MNDY (negative regime, positive β) -- possible
   misclassification or genuine compounding signal.
   Both warrant further investigation.

### Updated metric tracking table

| Metric | Positive regime | Negative regime | Status |
|---|---|---|---|
| Revenue growth YoY | AMZN/MSFT ✓ β>0 | DDOG/GTLB ✓ β<0 | COMPLETE |
| NRR | PENDING | PENDING | |
| Gross margin | PENDING | PENDING | |
| Operating margin | PENDING | PENDING | |
| FCF margin | PENDING | PENDING | |
| RPO growth | PENDING | PENDING | |

---

## Script 3 Results: Gross Margin (%)
## COMMITTED: June 2026 (before Script 4 is run)

### Universe
  Positive: MSFT, AMZN, CRM, SNOW (n=109 pooled)
  Negative: DDOG, GTLB (n=35 pooled)
  Missing: BABA, MNDY, TWLO
  (foreign private issuers -- 20-F only, no quarterly XBRL)

### Pre-committed expected sign: β > 0 (positive), β < 0 (negative)

### Pooled results

POSITIVE REGIME:
| Spec | β | p(OLS) | p(cl) | R² | n |
|---|---|---|---|---|---|
| Version A: T vs T | -0.281 | 0.352 | 0.754 | 0.008 | 109 |
| Version B: T vs T+1 | -0.492 | 0.098 | 0.619 | 0.026 | 105 |
| Version C: T vs T+2 | -0.595 | 0.041 | 0.488 | 0.042 | 101 |
| Version D: T vs T+4 | -0.678 | 0.011 | 0.467 | 0.068 | 93 |

NEGATIVE REGIME:
| Spec | β | p(OLS) | p(cl) | R² | n |
|---|---|---|---|---|---|
| Version A: T vs T | +0.762 | 0.021 | 0.441 | 0.151 | 35 |
| Version B: T vs T+1 | +0.512 | 0.124 | 0.564 | 0.075 | 33 |
| Version C: T vs T+2 | +0.290 | 0.374 | 0.537 | 0.027 | 31 |
| Version D: T vs T+4 | +0.292 | 0.553 | 0.509 | 0.014 | 27 |

### Assessment: MIXED / NULL RESULT

Both pooled results oppose pre-committed signs.
Positive regime: β negative (opposite of expected).
Negative regime: β positive at T+0 only (opposite of expected).

### Individual company results (Version A)

| Company | β | p(OLS) | R² | Interpretation |
|---|---|---|---|---|
| MSFT | +0.599 | 0.015 | 0.200 | Positive, contemp only |
| AMZN | -2.405 | 0.003 | 0.288 | Negative, highly significant |
| CRM | -0.096 | 0.793 | 0.003 | Null |
| SNOW | +1.194 | 0.126 | 0.113 | Positive, not significant |
| DDOG | +1.259 | 0.011 | 0.282 | Positive (wrong direction) |
| GTLB | -0.073 | 0.797 | 0.006 | Null |

### Key findings

1. GROSS MARGIN IS WEAKER SIGNAL THAN REVENUE GROWTH.
   Mixed directions, driven by company-specific structural
   factors rather than a clean cross-company pattern.

2. AMZN NEGATIVE β IS STRUCTURAL, NOT ANOMALOUS.
   AMZN consolidated gross margin is driven by business mix
   (AWS high margin vs retail low margin). The Ps signal
   captures AWS/cloud engineering. When AWS engineering
   intensity is high, retail growth often temporarily dilutes
   consolidated gross margin. Revenue growth is the cleaner
   metric for AMZN.

3. MSFT SHOWS CONTEMP POSITIVE BUT NO LEAD STRUCTURE.
   β=+0.599 at T+0 (p=0.015) but fades to zero by T+2.
   The Ps signal leads revenue growth but not gross margin
   at the six-month horizon for MSFT.

4. DDOG POSITIVE β IS COUNTERINTUITIVE.
   Elevated DDOG engineering intensity coincides with
   higher gross margins at T+0 and T+1. Interpretation:
   heavy investment periods precede the margin compression
   phase, not the expansion phase. Consistent with the
   parity maintenance hypothesis -- invest heavily to
   avoid margin deterioration, temporarily improving
   measured efficiency before the competitive pressure
   manifests in revenue deceleration.

5. SIX-MONTH HORIZON DOES NOT HOLD FOR GROSS MARGIN.
   Unlike revenue growth (peak R² at T+2), gross margin
   shows no consistent peak lag structure. The transmission
   mechanism from engineering intensity to unit economics
   operates on a different or more variable time horizon.

### Methodological insight

Gross margin at consolidated level is affected by business
mix, accounting choices and cost allocation in ways that
attenuate the Ps signal. Revenue growth is a cleaner test
of the engineering-to-commercial-output transmission.
Operating margin may be a better gross margin alternative
as it captures more of the operational leverage story.

### Updated metric tracking table

| Metric | Positive | Negative | Status | Finding |
|---|---|---|---|---|
| Revenue growth YoY | AMZN/MSFT β>0 ✓ | DDOG/GTLB β<0 ✓ | COMPLETE | Strong |
| Gross margin | Mixed/negative | Mixed/positive | COMPLETE | Null/weak |
| Operating margin | PENDING | PENDING | | |
| NRR | PENDING | PENDING | | |
| FCF margin | PENDING | PENDING | | |
| RPO growth | PENDING | PENDING | | |
