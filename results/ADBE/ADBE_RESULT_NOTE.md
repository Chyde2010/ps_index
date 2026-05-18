# ADBE (Adobe Inc.) Assessment Result
## Date: May 2026
## Exchange: NASDAQ

## Assessment stage: C6 domain diagnostic
## No pipeline run -- eliminated at diagnostic stage.

## Classification: C6 FAIL -- community handover

---

## Seven-condition assessment

C1 -- Consumption/usage-based revenue: PASS
  Creative Cloud charges per seat per month. Document Cloud
  and Experience Cloud subscription-based. Revenue scales
  with seat count and usage.

C2 -- Embedded platform, high switching costs: PARTIAL PASS
  Creative Cloud switching costs are real but contested.
  Canva, Figma and Affinity have all demonstrated switching
  is possible for meaningful user segments. Lower switching
  cost than Atlassian or Autodesk AEC. Partial pass.

C3 -- Frictionless consumption uplift: PASS
  Seat additions as creative teams grow. Experience Cloud
  scales with customer data volume. Clear pass.

C4 -- Near-term revenue realisation: PASS
  Monthly subscription fees recognised as earned. Clear pass.

C5 -- Product revenue primacy: PASS
  Pure software platform. No hardware. Clear pass.

C6 -- Open-source observability: FAIL
  See diagnostic results below.

C7 -- Engineering investment compounds the moat: LEAN PASS
  Case for pass:
  - Adobe Firefly generative AI compounds through proprietary
    training data from Adobe Stock -- competitors cannot
    replicate the dataset.
  - Spectrum design system underlies all Adobe products --
    each new component compounds platform coherence.
  - Experience Cloud data flywheel is genuine.
  Case against:
  - Canva built a competitive design tool without Spectrum.
  - Figma threatened Adobe enough to attempt $20bn acquisition
    (blocked by regulators in 2023).
  - Competitive threats are ongoing and well-capitalised.
  Net: C7 lean pass -- same nuance as DOTD.

---

## C6 Domain Diagnostic Results (May 2026)

Corporate domain: adobe.com
Study window: Jan 2017 to Mar 2026
Sample size: 100 commits per repo

| Repo                      | Corp% | Top non-Adobe domain    | Verdict |
|---------------------------|-------|-------------------------|---------|
| react-spectrum            | 17%   | reidbarber.com (19x)    | WEAK    |
| spectrum-web-components   | 13%   | sapo.pt (23x)           | WEAK    |
| spacecat-api-service      |  6%   | martynus.net (46x)      | WEAK    |
| spacecat-audit-worker     |  6%   | martynus.net (46x)      | WEAK    |
| aem-sidekick              |  1%   | martynus.net (48x)      | FAIL    |

Strong repos (>=50%): 0
Moderate repos (20-50%): 0

---

## C6 Failure Mechanism: Community Handover

Same failure type as INTU (C6 Type 8) but with a distinct
pattern. Adobe's community handover is more comprehensive
than Intuit's -- even the repos that should be internally
dominated (spacecat infrastructure, aem-sidekick) show
overwhelming external contribution.

Key findings:

1. react-spectrum community handover confirmed.
   reidbarber.com (Reid Barber) is a well-known external
   contributor who is not an Adobe employee. 44 gmail
   addresses confirm widespread community contribution.
   Adobe engineers (rsnow@adobe.com) are a minority in
   their own flagship design system despite it powering
   every Adobe product interface.

2. spacecat repos dominated by single external contributor.
   martynus.net appears in both spacecat-api-service and
   spacecat-audit-worker at 46 commits each -- more than
   all Adobe engineers combined in those repos. These were
   described as internal AEM platform engineering but have
   been effectively open-sourced with community ownership.

3. aem-sidekick completely community-owned.
   martynus.net (48), rofe.com (22), only 1 Adobe engineer
   commit in 100 sampled. This is a product-adjacent repo
   that Adobe has fully handed to external developers and
   AEM implementation partners.

4. Corporate email format confirmed valid.
   rsnow@adobe.com, abdulr@adobe.com, ttomar@adobe.com,
   seckles@adobe.com -- first name or abbreviated name
   format confirmed. Domain is observable where Adobe
   engineers commit. The problem is that they rarely do
   in public repos.

---

## Why a second diagnostic round was not pursued

With 1,096 repos in the adobe org there may be repos with
higher corporate rates. However two structural problems
prevent proceeding even if higher corporate rate repos
are found:

1. Revenue segment mismatch risk (same as ADSK):
   AEM represents ~20-25% of Adobe revenue. Creative
   Cloud (~55%) and Document Cloud (~15%) engineering
   is entirely private. If the only viable signal repos
   are AEM infrastructure, the observable segment is
   too small -- same C6 Type 9 partial observability
   risk as ADSK.

2. Community handover is pervasive:
   The fact that react-spectrum -- Adobe's own flagship
   design system that they maintain and use in every
   product -- shows only 17% corporate rate confirms
   that Adobe's open-source culture has systematically
   produced community handover across the org. Even
   if additional repos pass the corporate rate threshold,
   the signal quality will be compromised by the same
   community dilution pattern.

---

## NASDAQ 100 Tier 1 Expansion -- Final Summary

All four Tier 1 candidates assessed. None added to live universe.

| Ticker | Company   | Result                        | Failure mode              |
|--------|-----------|-------------------------------|---------------------------|
| TEAM   | Atlassian | Signal present, regime-depend | AI disruption re-rating   |
| INTU   | Intuit    | C6 fail                       | Type 8: community handover|
| ADSK   | Autodesk  | No signal                     | Type 9: partial observ.   |
| ADBE   | Adobe     | C6 fail                       | Type 8: community handover|

Pattern: NASDAQ 100 large-cap software companies either have
private engineering (ADSK GHE 19,000 repos) or have
open-sourced their tooling so thoroughly that community
contributors dominate the commit history (INTU, ADBE).

The original positive universe companies (MSFT, AMZN, CRM,
SNOW, BABA) succeeded because their observable engineering
represents core platform work with high corporate email rates.
Finding equivalent companies in the NASDAQ 100 requires
looking beyond the largest caps to mid-cap software platforms
where the core product is genuinely observable.

---

## Recommended next steps for universe expansion

Options beyond the NASDAQ 100 Tier 1 shortlist:

1. NASDAQ 100 Tier 2 candidates (not yet assessed):
   - HUBS (HubSpot): marketing CRM, consumption model,
     github.com/HubSpot org exists with active repos
   - TTD (The Trade Desk): programmatic advertising,
     less likely but worth a quick check
   - OKTA: identity platform, likely private engineering

2. Mid-cap software platforms (outside NASDAQ 100):
   Companies where the core product IS the open-source
   product -- HashiCorp model but still listed.
   Examples: Elastic (ESTC -- already assessed no signal),
   Confluent (C6 fail), MongoDB (MDB -- no signal).
   The challenge: most mid-cap open-source software
   companies have already been assessed.

3. International listed software platforms:
   Similar to DOTD and GBG assessment -- UK/European
   AIM or main market listed SaaS companies where
   the engineering is more observable.

4. Accept current universe as sufficient:
   The live universe (MSFT, AMZN, CRM, SNOW, BABA long;
   DDOG, TWLO, GTLB, MNDY short) is already a credible
   and validated signal with 22+ companies assessed.
   Focus on live track record rather than expansion.
