# HUBS (HubSpot Inc.) Assessment Result
## Date: May 2026
## Exchange: NYSE

## Assessment stage: C6 domain diagnostic (1 round)
## No pipeline run -- eliminated at diagnostic stage.

## Classification: C6 FAIL
## Mechanism: Private repo migration policy +
##             insufficient strong repos

---

## Seven-condition assessment

C1 -- Consumption or usage-based revenue: PASS
  HubSpot charges per seat per month across its Hubs
  (Marketing, Sales, Service, CMS, Operations) with tiered
  pricing (Starter, Professional, Enterprise). Revenue scales
  with seat count, contact database size and feature adoption.
  Clear pass.

C2 -- Embedded platform, high switching costs: PASS
  HubSpot's CRM sits at the centre of a company's entire
  go-to-market operation. Years of contact history, deal
  pipelines, email sequences, workflow automations, reporting
  dashboards and website CMS all embedded. Switching means
  migrating all of that -- a multi-month project. Clear pass.

C3 -- Frictionless consumption uplift: PASS
  As a company's contact database grows, HubSpot revenue
  grows. As sales teams expand, more seats are added. Upsell
  from Starter to Professional to Enterprise within existing
  relationships. Net revenue retention consistently above 100%.
  Clear pass.

C4 -- Near-term revenue realisation: PASS
  Monthly subscription fees recognised as earned. Clear pass.

C5 -- Product revenue primacy: PASS
  Pure software platform. No hardware. Professional services
  minimal. Clear pass.

C6 -- Open-source observability: FAIL
  See diagnostic results and policy note below.

C7 -- Engineering investment compounds the moat: UNCERTAIN
  Case for pass:
  - CRM data flywheel compounds with every customer interaction
  - AI features built on years of sales and marketing data
  - Recent acquisitions: XFunnel (AI search, Nov 2025),
    Starter Story (content, Feb 2026)
  Case against:
  - Operating loss of $68M in 2024 on $2.63bn revenue
  - Contested CRM market vs Salesforce, Monday.com, Notion
  - Private repo migration suggests possible engineering
    coherence concerns
  - Same nuance as DOTD -- contested market, moat defence
    vs moat compounding unclear
  Net: C7 UNCERTAIN -- lean fail given contested market and
  private repo migration policy direction.

---

## C6 Diagnostic Results (May 2026)

Corporate domain: hubspot.com
Study window: Jan 2016 to Mar 2026

| Repo                   | Corp% | n    | Verdict           |
|------------------------|-------|------|-------------------|
| Rosetta                | 64%   | 100  | STRONG            |
| hubspot-local-dev-lib  | 40%   | 100  | MODERATE          |
| NullAway               | -     | -    | NOT FOUND         |
| async-http-client      | -     | -    | NOT FOUND         |
| boomslang              | -     | -    | NOT FOUND         |

Total strong repos: 1 (insufficient for pipeline)

---

## Key Finding: Private Repo Migration Policy

Critical finding from search (July 2025 HubSpot announcement):

"The public GitHub repository will no longer be used as our
main repository for the HubSpot CLI. Moving forward, HubSpot
CLI development work will be completed in a private repo with
periodic updates synced to the public repo."

This is an explicit statement of C6 Type 7 migration policy.
HubSpot has deliberately moved primary engineering to private
repos and is syncing updates publicly -- the same mechanism
as Atlassian's pragmatic-drag-and-drop and the pattern that
produced FPP=0.000 on mirror repos.

The three not-found repos (NullAway, async-http-client,
boomslang) have likely been moved to private repos or
transferred to community orgs following this same strategy.

This is not incidental -- it is a stated engineering policy.
The trend is toward less public observability, not more.

---

## C6 Failure Mechanism

Two compounding factors:

1. Stated private repo migration policy (July 2025):
   HubSpot is actively moving engineering private.
   Public repos are becoming mirrors or stubs.
   This is structural and will worsen over time.

2. Insufficient strong repos:
   Only 1 strong repo (Rosetta at 64%) from 5 tested.
   3 repos not found -- likely moved private.
   379 total repos but majority are SDK clients
   (developer relations surface) or private mirrors.

---

## C7 Note: Private Migration as Entropy Signal

The private repo migration decision is worth noting as a
potential C7 signal. A company that is explicitly pulling
engineering into private repos while the public presence
shows operating losses and a contested market may be:
  a) Making a legitimate IP protection decision, OR
  b) Reducing external visibility of engineering quality
     concerns

Cannot distinguish between these from external data.
But the direction of travel -- less public, more private --
combined with operating losses and a contested market is
consistent with the high entropy pattern seen in DOTD and MNDY
rather than the low entropy compounding seen in MSFT and AMZN.

---

## Summary

| Ticker | Company  | Result  | Failure mode           |
|--------|----------|---------|------------------------|
| HUBS   | HubSpot  | C6 fail | Private repo migration |
|        |          |         | + insufficient repos   |

Not added to signal universe. No pipeline run.
C1-C5 all pass. C7 uncertain (lean fail).

---

## Updated no-signal/fail universe

GOOGL, META, MDB, ESTC, AMD, DT,
INTU, ADSK, ADBE, RBLX, APP, ZS, HUBS
