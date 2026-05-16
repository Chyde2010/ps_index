# Batch 3 Universe Expansion -- Pre-Registration
## Ticker: DOTD (dotDigital Group plc)
## Exchange: AIM (London Stock Exchange)
## Date: May 2026
## Pre-committed before any pipeline execution

---

## Methodology Note

Formula: Ps = V x phi x (1 - H)
- V   = 90-day rolling corporate commit count
- phi = structural commit density (churn floor 100 lines)
- (1-H) = entropy gap

Corporate email domains: dotdigital.com AND dotmailer.com
  dotmailer.com = legacy corporate domain pre-2019 rebrand.
  dotDigital rebranded from dotmailer to dotdigital in 2019.
  Engineers who joined pre-rebrand retained dotmailer.com addresses.
  Both domains confirmed as genuine corporate in domain diagnostic.
  Email format: firstname.lastname@[domain] confirmed.

This is the same dual-domain finding as MELI
(mercadolibre.com / mercadolivre.com) -- a methodological
discovery documented before pipeline execution.

Commercial bar: factor-adjusted 6M p<0.05, retention >70%,
beta POSITIVE (positive regime prediction).

---

## Candidate -- dotDigital Group (DOTD)

### Predicted signal: POSITIVE (medium confidence)

Confidence qualifier: C7 is a lean pass rather than a
clear pass. The connector ecosystem compounding argument is
plausible but not as structurally unambiguous as MSFT or AMZN.
Medium confidence reflects this nuance.

### Seven-condition assessment

C1 -- Consumption or usage-based revenue: PASS
  dotDigital charges per contact in the database and per email
  sent -- pure consumption model. Revenue scales directly with
  platform usage. Every additional contact added or email sent
  generates incremental revenue. One of the cleanest consumption
  models in the Edison TMT universe -- closer to SNOW than CRM.

C2 -- Embedded platform, high switching costs: PASS
  dotDigital integrates deeply with e-commerce platforms --
  Magento, Shopware, WooCommerce, Salesforce Commerce Cloud,
  WordPress. The integration layer, historical campaign data,
  customer segments, automation workflows and transactional
  email templates are all embedded inside the platform.
  Switching to a competitor (Klaviyo, Braze, Mailchimp) means
  rebuilding all platform integrations, recreating historical
  segments and re-importing campaign data. High switching cost
  for established e-commerce retailer. Clear pass.

C3 -- Frictionless consumption uplift: PASS
  As a retailer's customer database grows, dotDigital contact
  count grows automatically -- generating more revenue without
  a new sales cycle. More products mean more transactional
  emails. More customers mean more campaigns. New use cases
  (SMS, push, live chat) expand revenue within existing
  relationships frictionlessly. Net revenue retention above
  100% confirms genuine frictionless expansion. Clear pass.

C4 -- Near-term revenue realisation: PASS
  SaaS subscription and usage fees recognised monthly.
  No revenue lag. Clear pass.

C5 -- Product revenue primacy: PASS
  Pure software platform revenue. No hardware. Professional
  services minimal and declining as percentage of total revenue
  as platform matures. Stock trades on ARR growth and net
  revenue retention. Clear pass.

C6 -- Open-source observability: PASS
  Domain diagnostic (May 2026):
    dotmailer/dotmailer-magento2-extension: 100% dotdigital.com
    dotmailer/dotdigital-for-woocommerce  : 90% combined
    dotmailer/dotdigital-for-shopware     : 89% combined
    dotmailer/segment-action-destinations : 2% EXCLUDED
    dotdigitalgroup/keycloak-rabbitmq     : 0% EXCLUDED

  FPP pre-screen (May 2026): 4/5 repos pass FPP >= 0.05
    FAIL magento2-extension    FPP=0.030 n=100 EXCLUDED
         (maintenance-dominated -- mature connector
          in compatibility mode for Magento release cycle)
    PASS dotdigital-for-woocommerce    FPP=0.080 n=100
    PASS dotdigital-for-shopware       FPP=0.210 n=81
    PASS dotmailer-magento2-ext-sms    FPP=0.080 n=100
    PASS dotdigital-for-wordpress      FPP=0.100 n=100

  Note on anchor repo exclusion: magento2-extension excluded
  despite being the highest-volume repo (2,577 commits) because
  FPP=0.030 indicates maintenance dominance -- the connector is
  feature-complete and in compatibility maintenance mode.
  The four passing repos represent active structural engineering
  on newer platform integrations. This is the correct signal.

C7 -- Engineering investment compounds the moat: LEAN PASS
  The observable engineering -- connector ecosystem across
  Magento, WooCommerce, Shopware, WordPress -- compounds the
  platform moat in a specific and defensible way.

  Case for PASS:
  - Each new platform connector (WooCommerce, Shopware,
    WordPress) locks in additional merchant segments that
    cannot easily switch without rebuilding integrations.
  - Shopware connector FPP=0.210 indicates active structural
    engineering investment in a growing European e-commerce
    platform -- exactly the kind of compounding expansion
    that raises switching costs for new merchant cohorts.
  - The connector ecosystem creates a flywheel: more platform
    integrations attract more merchants, more merchants
    generate more usage data, more data improves automation
    and segmentation quality, better outcomes reduce churn.
  - The maintenance-dominated anchor repo (Magento 2) is
    consistent with a maturing connector that has locked in
    its merchant base -- structural work has shifted to
    newer platforms where growth is happening.

  Case AGAINST (documented uncertainty):
  - Competitors (Klaviyo, Braze, Mailchimp, Dotdigital's
    direct peers) are also building platform connectors.
    The connector engineering is not uniquely insurmountable.
  - dotDigital is an AIM-listed company with ~£150m market cap
    -- smaller than all other universe companies. Liquidity
    risk and small-cap premium may contaminate the signal.
  - The UK marketing automation market is competitive with
    no single dominant technical architecture.

  Net assessment: C7 LEAN PASS. Connector ecosystem
  compounds switching cost moat with each new platform
  integration. Not as structurally unambiguous as MSFT/AMZN
  but meaningfully more defensible than MNDY's contested
  Work OS market.

### Study period
AIM listed: 2000. Connector engineering emerged ~2016.
Study period: January 2017 to March 2026 (111 months).
Start date reflects when observable connector engineering
began rather than listing date.

### Repos (pipeline -- 4 repos, all passing pre-screen)
- dotmailer/dotdigital-for-woocommerce      FPP=0.080 n=100
- dotmailer/dotdigital-for-shopware-flowbuilder FPP=0.210 n=81
- dotmailer/dotmailer-magento2-extension-sms   FPP=0.080 n=100
- dotmailer/dotdigital-for-wordpress           FPP=0.100 n=100

dotmailer-magento2-extension EXCLUDED:
  FPP=0.030, below threshold. Maintenance-dominated.
  Including it would dilute signal with maintenance noise.

### Sector control
XLK (Technology Select Sector SPDR) -- primary.
Global SaaS software sector is the correct peer group for
a marketing automation platform regardless of listing venue.
SPY as market control.

### Risk factors
1. Small-cap premium: DOTD market cap ~£150m. Small-cap
   risk premium may contaminate signal at longer horizons.
   AIM liquidity is lower than main market or US-listed peers.
2. C7 uncertainty: connector engineering is replicable by
   well-resourced competitors. Moat is execution and
   distribution as much as engineering.
3. Dual domain complexity: dotmailer.com commits span
   pre-2019 period. Signal may reflect different engineering
   team composition in early years vs recent years.
4. Short observable history: 4 of the 5 repos were created
   after 2017 -- study period is shorter than most universe
   companies (111 months vs 82-118 for established names).

### Confidence level
Medium. C7 lean pass is genuine but less clear than MSFT/AMZN.
Positive regime prediction is the most defensible call given
the consumption model, embedding and connector flywheel.
Null or negative outcome would not be surprising given the
C7 uncertainty and small-cap risk factors.

---

## Context: Edison Group pitch

This pipeline is being run specifically to support a
commercial pitch to the Edison Group CEO. dotDigital is
the strongest candidate from a systematic screen of Edison's
TMT equity coverage list (20+ companies assessed).

GB Group (GBG) was the only other viable candidate.
GBG was eliminated at C6 -- public repos contain 3-14
commits total, all SDK demos. Core engineering entirely
private in gbgplc-internal organisation.

dotDigital was selected because:
1. Edison covers DOTD and publishes research on it
2. DOTD passes all seven conditions convincingly
3. Four repos pass FPP pre-screen with clean corporate
   email observability across dual domain
4. The finding is directly actionable for Edison analysts
   and their investor clients who hold DOTD

---

## Summary

| Ticker | Company     | Predicted | Confidence | Batch |
|--------|-------------|-----------|------------|-------|
| DOTD   | dotDigital  | Positive  | Medium     | 3     |

---

## Pre-commitment statement

The above prediction and condition assessment was committed
to GitHub before any DOTD pipeline was executed.

Signed: Charlotte Hyde
Date: May 2026
GitHub: Chyde2010/ps_index
