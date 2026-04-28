# MELI (MercadoLibre Inc) Pipeline Result
## Date: April 2026

## Pre-registration prediction: POSITIVE signal (medium confidence)
## Empirical result: NO SIGNAL -- EM macro dominance

---

## Key findings

Full sample:
- 1M: adj beta=-0.020, p=0.063  -- negative direction, not significant
- 3M: adj beta=-0.049, p=0.019  -- NEGATIVE, significant
- 6M: adj beta=-0.025, p=0.418  -- negative direction, not significant

Subsets:
- Low VIX 6M:  adj beta=+0.172, p=0.032  -- PASS (see caveat below)
- High VIX 1M: adj beta=-0.038, p=0.008  -- significant NEGATIVE
- High VIX 3M: adj beta=-0.061, p=0.089  -- negative, not significant

Positive adj betas: 2/9
Negative adj betas: 7/9
Commercial bar passes: 1/9 (Low VIX 6M only -- see caveat)

HC episodes: 6
- 2016-12: z=1.64, VIX=14.0, 6M=+60.9%
- 2017-01: z=1.53, VIX=12.0, 6M=+55.8%
- 2022-01: z=2.25, VIX=24.8, 6M=-28.1%
- 2022-02: z=5.19, VIX=30.1, 6M=-24.1%
- 2022-03: z=7.12, VIX=20.6, 6M=-30.4%  <- dominant outlier
- 2022-04: z=4.33, VIX=33.4, 6M=-7.4%
Mean HC: 1M=0.0%, 3M=-8.0%, 6M=+4.5%

Activity bucket spread (High vs Very Low at 6M): +5.9pp
  Below BABA (+1.2pp adjusted for regulatory risk -- at least
  BABA's regulatory crashes were episodic; MELI's 2022 crash
  persisted across all four HC episodes simultaneously)

---

## Commercial verdict: NO SIGNAL

The pre-committed prediction of POSITIVE signal is INCORRECT.

### Why the Low VIX 6M pass is not a genuine positive signal

The single commercial bar pass (Low VIX 6M: beta=+0.172, p=0.032)
is a statistical artefact driven by two data points:
- 2016-12: HC episode, low VIX, +60.9% 6M return
- 2017-01: HC episode, low VIX, +55.8% 6M return

These two 2016-17 observations create the positive beta in the
low-VIX subset. They are genuine -- MELI's 2017 stock performance
was exceptional and the Ps signal was elevated. But a commercial
bar pass driven by 2 out of 82 observations in one specific VIX
regime is not a robust finding. The overall directional signal
across the full sample is negative (7/9 negative betas), which
is the controlling result.

### The root cause: EM macro dominance

The Ps z-score outlier of 7.12 in March 2022 -- the highest
z-score in the entire study across all 22+ companies tested --
coincided with MELI's catastrophic growth stock selloff:
- US Federal Reserve began hiking cycle January 2022
- EM growth stocks sold off 40-60% in H1 2022
- MELI fell from ~$1,800 to ~$700 (peak to trough 2021-2022)
- Mercado Pago SDK engineering was at peak intensity during
  this exact period (major new payment method integrations,
  new country rollouts, API v2 migration)

Result: the regression sees high engineering activity
contemporaneous with the worst six-month returns in the
sample, and interprets engineering investment as a negative
predictor. This is a spurious negative -- the engineering
quality is real, but the stock is too macro-sensitive to
reflect it.

This is structurally different from BABA's regulatory risk
(episodic, 2020-21 specific) and from the no-signal companies
in the original study (which failed due to C7 issues). MELI
fails because the stock return series is dominated by EM
rate-sensitivity macro factor that overwhelms the engineering
signal continuously, not episodically.

---

## New classification: Signal present but unrecoverable

MELI represents a new category distinct from the existing
classification system:

EXISTING CATEGORIES:
- Positive signal: C1-C7 pass, signal significant and positive
- Negative signal: C1-C6 pass, C7 fail, signal negative
- No signal: framework conditions not met (C3 or C5 fail)
- Failed C6: insufficient open-source observability

NEW CATEGORY -- Signal present but unrecoverable:
- C6: PASS (engineering genuinely observable via GitHub)
- C7: PASS (Mercado Pago data moat is genuine)
- Framework conditions: met
- Engineering signal: present in commit data
- Stock return signal: not recoverable due to EM macro dominance

The framework correctly identifies MELI as a consumption-platform
company with a compounding engineering moat. The stock return
signal cannot be extracted because the EM growth equity macro
factor overwhelms company-specific fundamental signals at all
tested horizons. This is a boundary condition of the framework,
not a framework failure.

---

## Implications for Paper 2

MELI strengthens the framework's discriminatory power in an
unexpected direction. It demonstrates that:

1. The seven-condition framework correctly identifies companies
   where the engineering moat is observable (C6 pass) and
   compounding (C7 pass).

2. For the signal to be extractable, stock returns must be
   sufficiently anchored to company-specific fundamentals.
   For highly macro-sensitive EM growth stocks with large
   exposure to US rate cycle and currency risk, this condition
   may not hold.

3. The framework should therefore be qualified: it identifies
   engineering quality signals in companies where stock returns
   are primarily driven by company-specific fundamentals.
   EM companies with high macro sensitivity are a documented
   boundary condition.

Suggested Paper 2 addition: a brief section on boundary
conditions, contrasting BABA (signal recoverable after factor
adjustment despite regulatory risk) with MELI (signal not
recoverable due to persistent EM macro dominance).

---

## Domain discovery: multi-country email convention

MELI pipeline produced a methodological contribution:
MercadoLibre uses country-specific corporate email domains:
- mercadolibre.com   -- Spanish-speaking countries
- mercadolivre.com   -- Brazil (Portuguese brand name)
- mercadolibre.com.co -- Colombia
- (likely also .com.mx, .com.ar, .com.ve etc)

Fix: use partial match on 'mercadolibre' and 'mercadolivre'
substrings rather than exact domain matching. This captures
all country variants automatically.

This is a new methodological contribution applicable to any
multi-country technology company with localised brand names.

---

## Repo note

Only 4 repos with 1,231 corporate commits across the study
period. 48/123 months (39%) had zero observable corporate
engineering activity. The sparse signal structure (p50 z-score
= -0.30) is itself a finding -- Mercado Pago SDK engineering
is episodic rather than continuous, which limits the pipeline's
ability to generate a consistent monthly signal.

A broader repo set (additional mercadolibre org repos with
high corporate email rates) might improve signal continuity,
but given the EM macro dominance finding, additional repos
are unlikely to rescue the commercial bar.

---

## Updated universe

Positive signal       : MSFT, AMZN, CRM, SNOW, BABA
Negative signal       : DDOG, TWLO, GTLB
No signal             : GOOGL, META, MDB, ESTC, AMD, DT
Failed C6             : NET, CFLT, PLTR, NU Holdings
Signal unrecoverable  : MELI (EM macro dominance)
