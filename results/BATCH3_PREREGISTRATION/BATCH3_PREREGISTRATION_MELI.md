# Batch 3 Universe Expansion -- Pre-Registration
## Ticker: MELI (MercadoLibre Inc)
## Date: April 2026
## Pre-committed before any pipeline execution
 
This document records the predicted signal direction and
seven-condition assessment for MercadoLibre before any
pipeline is run.
 
---
 
## Methodology Note
 
Formula: Ps = V x phi x (1 - H)
- V   = 90-day rolling corporate commit count
- phi = structural commit density (churn floor 100 lines)
- (1-H) = entropy gap
 
Domain filter: PARTIAL MATCH on two substrings
- 'mercadolibre' -- captures mercadolibre.com, mercadolibre.com.co,
  mercadolibre.com.mx, mercadolibre.com.ar and all other
  Spanish-speaking country domain variants
- 'mercadolivre' -- captures mercadolivre.com, the Brazilian
  Portuguese corporate email domain used by ~27,000 Brazilian
  MercadoLibre employees (confirmed: first.last@mercadolivre.com
  at 96% of Brazilian staff per LeadIQ/RocketReach)
 
Note on domain confirmation: mercadolivre.com is NOT a consumer
domain. It is MercadoLibre's corporate email domain for Brazil,
equivalent to mercadolibre.com for Spanish-speaking markets.
The Brazilian entity (Mercado Livre Brasil) employs 27,000+
staff on this domain. Confirmed prior to pre-registration.
 
Commercial bar: factor-adjusted 6M p<0.05, retention >70%,
positive beta.
 
---
 
## Candidate -- MercadoLibre (MELI)
 
### Predicted signal: POSITIVE
 
### Seven-condition assessment
 
C1 -- Consumption or usage-based revenue: PARTIAL PASS
  Mercado Pago is volume-driven -- payment processing fees,
  fintech services and credit origination revenue all scale
  directly with transaction volume (Total Payment Volume).
  Mercado Libre marketplace charges commissions and
  advertising on GMV. Neither is pure consumption billing
  in the cloud software sense. Partial pass on the strength
  of Mercado Pago as the strategically decisive and
  growing segment. Same assessment applied to AMZN (AWS
  consumption vs retail) and BABA (Cloud vs e-commerce CMR).
 
C2 -- Embedded platform with high switching costs: PASS
  Merchants: entire storefront, inventory, Mercado Envios
  logistics, Mercado Pago payment processing, credit access
  via Mercado Credito -- all embedded in one ecosystem.
  Consumers: Mercado Pago wallet, credit history, BNPL,
  investments and insurance embedded in daily financial life.
  Network effects across 18 LatAm countries. Clear pass.
 
C3 -- Frictionless consumption uplift: PARTIAL PASS
  Mercado Pago processes more transactions for existing
  merchants and consumers as activity grows -- genuinely
  frictionless revenue uplift. Mercado Credito uses
  transaction data to extend credit which drives more
  platform spending. Marketplace requires active merchant
  acquisition. Partial pass.
 
C4 -- Near-term revenue realisation: PASS
  Payment processing revenue recognised at transaction.
  Marketplace commissions recognised at sale. Advertising
  recognised as delivered. No meaningful lag. Clear pass.
 
C5 -- Product revenue primacy: PASS
  Pure product revenue across marketplace and fintech.
  No professional services. Stock trades on GMV, TPV,
  fintech revenue mix and credit quality. Clear pass.
 
C6 -- Open-source observability continuity: PASS
  Pre-screen result (April 2026): 4/6 repos pass.
  - mercadopago/sdk-android: FPP=0.264 n=91  PASS
  - mercadopago/sdk-ios:     FPP=0.073 n=96  PASS
  - mercadopago/sdk-java:    FPP=0.130 n=100 PASS
  - mercadopago/sdk-python:  FPP=0.110 n=100 PASS
  - fury-core-ci:            FPP=0.020 n=100 FAIL (CI tooling)
  - mlbusiness-components:   FPP=0.040 n=100 FAIL (UI components)
  Domain breakdown: mercadolivre.com dominates SDK repos
  (91-99% of commits). mercadolibre.com dominates org repos.
  Both are confirmed corporate domains -- partial match filter
  captures all country variants.
  Only the 4 passing repos used in pipeline -- failing repos
  excluded to avoid noise without signal.
 
C7 -- Engineering investment compounds the moat: PASS
  Mercado Pago's payment infrastructure compounds a data moat
  across 18 Latin American markets that competitors cannot
  replicate regardless of capital:
  - Each transaction generates behavioural data that improves
    Mercado Credito risk models -- cheaper credit to more
    merchants and consumers -- more platform activity -- more
    data. Compounding flywheel.
  - Cross-country payment infrastructure (local payment
    methods, regulatory compliance, currency handling across
    18 markets) took 25 years to build. Cannot be replicated
    by Stripe, PayPal or local entrants in any reasonable
    timeframe.
  - SDK engineering directly extends the payment surface --
    new payment methods, new checkout flows, new fraud
    detection -- each addition deepens merchant integration
    and switching costs.
  Marketplace C7 is weaker -- Amazon, Shopee and local
  competitors can replicate marketplace features. The signal
  is expected to be driven by Mercado Pago, not Mercado Libre.
  Net assessment: C7 PASS on the strength of Mercado Pago.
 
### Rationale
MELI is structurally analogous to AMZN in the original study.
AMZN's signal was driven by AWS engineering even though retail
dominated revenue. MELI's signal is expected to be driven by
Mercado Pago SDK engineering even though marketplace GMV is
the larger revenue segment. Both companies have a consumption-
platform technology business (AWS / Mercado Pago) embedded
within a larger e-commerce marketplace, and the Ps signal is
expected to reflect the technology platform's engineering
quality rather than the marketplace's operational activity.
 
If the signal passes, MELI becomes the second non-US,
non-Western company in the Ps Index universe after BABA,
and the first LatAm company. This strengthens the emerging
markets extension case for the Emily Whiting / JPMorgan
EMAP pitch -- her fund holds MELI as a $177m position.
 
### Study period
NYSE listed: July 2007 (NASDAQ: MELI).
Meaningful open-source GitHub activity on mercadopago SDK
org: approximately 2016 onwards.
Study period: January 2016 to March 2026 (123 months).
 
### Repos (pipeline only -- 4 repos, all passing pre-screen)
- mercadopago/sdk-android  (Payment SDK, FPP=0.264)
- mercadopago/sdk-ios      (Payment SDK, FPP=0.073)
- mercadopago/sdk-java     (Payment SDK, FPP=0.130)
- mercadopago/sdk-python   (Payment SDK, FPP=0.110)
 
fury-core-ci and mlbusiness-components-ios EXCLUDED --
both failed FPP pre-screen. Including failing repos
introduces noise without signal (cf. omnibus-gitlab
in GTLB pipeline).
 
### Sector control
ILF (iShares Latin America 40 ETF) -- more appropriate
than QQQ (US large-cap tech) or KWEB (China Internet).
MELI returns are heavily influenced by LatAm macro --
BRL/USD exchange rate, Argentine economic conditions,
regional interest rate cycles -- none of which QQQ or
KWEB captures. ILF tracks the 40 largest LatAm stocks
and provides appropriate regional factor control.
 
### Risk factors
1. LatAm macro dominates short-term returns -- currency
   volatility (BRL, ARS, MXN), interest rate cycles and
   political risk may mask engineering signal at 1-3M
   horizons. Signal expected at 6M only, same as BABA.
2. sdk-android FPP=0.264 is strong; sdk-ios FPP=0.073
   is marginal. If iOS and Python repos contribute
   sparse structural events, signal may be thin.
3. MELI stock is volatile -- Sharpe ratio lower than US
   Ps universe companies. Factor adjustment more critical.
4. Study period starts 2016 -- misses early Mercado Pago
   growth phase. Signal may be stronger in later years
   when Mercado Pago became the dominant revenue driver.
 
---
 
## Summary Table
 
| Ticker | Company       | Predicted | Confidence | Batch |
|--------|---------------|-----------|------------|-------|
| MELI   | MercadoLibre  | Positive  | Medium     | 3     |
 
Medium confidence because:
- C1 and C3 are partial passes (same as BABA)
- sdk-ios FPP marginal at 0.073
- LatAm macro risk significant
- Second non-US company tested
 
---
 
## Pre-commitment statement
 
The above prediction and condition assessment was committed
to GitHub before any MELI pipeline was executed.
 
Signed: Charlotte Hyde
Date: April 2026
GitHub: Chyde2010/ps_index
