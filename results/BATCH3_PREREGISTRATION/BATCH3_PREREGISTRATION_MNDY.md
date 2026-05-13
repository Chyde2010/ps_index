# Batch 3 Universe Expansion -- Pre-Registration
## Ticker: MNDY (Monday.com Ltd)
## Date: May 2026
## Pre-committed before any pipeline execution

---

## Methodology Note

Formula: Ps = V x phi x (1 - H)
- V   = 90-day rolling corporate commit count
- phi = structural commit density (churn floor 100 lines)
- (1-H) = entropy gap

Corporate email domain: monday.com (single domain)
Email format: firstname@ or shortname@monday.com
Israeli company -- Western corporate email convention confirmed.
No country variant complexity. Single domain filter sufficient.

Commercial bar: factor-adjusted 6M p<0.05, retention >70%,
consistent directional beta.

---

## Candidate -- Monday.com (MNDY)

### Predicted signal: NEGATIVE (medium-low confidence)

Confidence qualifier: C7 is genuinely ambiguous for monday.com.
The AI agent tooling investment (mcp repo) is a wildcard that
could support a positive regime classification in future.
Medium-low confidence reflects this uncertainty. This is a
weaker C7 fail than DDOG, TWLO or GTLB where the failure
was unambiguous.

### Seven-condition assessment

C1 -- Consumption or usage-based revenue: PARTIAL PASS
  Per-seat SaaS subscription model. Revenue scales with seat
  count and tier upgrades rather than pure metered consumption.
  Closer to CRM model than SNOW. Partial pass on same basis
  as Salesforce -- usage-adjacent but not pure consumption.

C2 -- Embedded platform with high switching costs: PASS
  Work OS model maximises embedding by design. Enterprise
  customers build operational workflows -- project management,
  CRM pipelines, HR processes, product roadmaps -- inside
  monday.com using boards, columns, automations and integrations.
  Data lives inside the platform, workflows are custom-built,
  integrations are configured. Switching cost is genuinely high
  once embedded. Clear pass.

C3 -- Frictionless consumption uplift: PARTIAL PASS
  Seat expansion within existing accounts is relatively
  frictionless -- additional users added without new sales cycle.
  Net dollar retention above 110% confirms genuine expansion.
  Monday CRM, Monday Dev, Monday Service create additional
  cross-sell vectors within embedded accounts. Active customer
  success required for new department expansion. Partial pass,
  same basis as CRM.

C4 -- Near-term revenue realisation: PASS
  SaaS subscription recognised monthly over contract term.
  No significant revenue lag. Clear pass.

C5 -- Product revenue primacy: PASS
  Pure product revenue -- subscription fees. Professional
  services minimal and declining as percentage of revenue.
  Stock trades on ARR, net dollar retention, operating leverage
  and Rule of 40. Clear pass.

C6 -- Open-source observability: PASS
  Domain diagnostic (May 2026): 5/5 repos strong.
  Corporate email rates 53-98% across all repos.
  FPP pre-screen (May 2026): 4/5 repos pass FPP >= 0.05.

  Passing repos:
  - mondaycom/vibe            FPP=0.140 n=100 (Platform UI)
  - mondaycom/monday-apps-cli FPP=0.140 n=100 (Dev Tooling)
  - mondaycom/mcp             FPP=0.100 n=100 (AI Platform)
  - mondaycom/monday-sdk-js   FPP=0.057 n=35  (Dev SDK, marginal)

  Excluded repo:
  - mondaycom/monday-api-python-sdk FPP=0.044 n=68 FAIL
    Excluded: below FPP threshold, introduces noise without
    signal (cf. omnibus-gitlab in GTLB, fury-core-ci in MELI).

C7 -- Engineering investment compounds the moat: FAIL
  The four observable repos are all developer platform and SDK
  tooling -- the ecosystem that third-party app developers use
  to build on monday.com. None represent the core Work OS
  product itself (boards, columns, automations, AI features),
  which is entirely proprietary.

  Case for FAIL:
  - Work OS market is genuinely contested. Asana, ClickUp,
    Notion, Atlassian and Microsoft (Teams/365) are all
    investing in similar developer ecosystems.
  - The observable engineering -- React design system, JS SDK,
    CLI tooling -- is quality work but replicable by
    well-resourced competitors without structural barriers.
  - Microsoft's Teams and 365 ecosystem represents an
    engineering moat in productivity software that monday.com
    cannot overcome through SDK investment alone.
  - Engineering maintains competitive position in a contested
    market rather than compounding an insurmountable structural
    advantage.

  Case AGAINST fail (C7 ambiguity documented):
  - mondaycom/mcp (MCP server for AI agent integration) is the
    most interesting signal. Early investment in AI agent
    tooling could compound a developer ecosystem advantage as
    AI adoption grows. This is genuinely compounding if
    monday.com establishes AI-first Work OS positioning.
  - Platform flywheel argument: more SDK capability -> more
    third-party developers -> more apps -> more enterprise
    value -> higher switching costs. Each engineering cycle
    potentially compounds the ecosystem moat.
  - vibe (design system, FPP=0.140) suggests genuine product
    engineering investment, not just peripheral tooling.

  Net assessment: C7 FAIL on current evidence. The competitive
  dynamics of the Work OS market do not yet show the structural
  separation that characterises positive regime companies.
  The AI tooling investment is a wildcard -- if MNDY establishes
  genuine AI-first Work OS advantage, reassessment warranted.

### Study period
NASDAQ listed: June 2021 (IPO).
Study period: June 2021 to March 2026 (58 months).

### Repos (pipeline -- 4 repos, all passing pre-screen)
- mondaycom/vibe             (Platform UI,    FPP=0.140)
- mondaycom/monday-apps-cli  (Dev Tooling,    FPP=0.140)
- mondaycom/mcp              (AI Platform,    FPP=0.100)
- mondaycom/monday-sdk-js    (Dev SDK,        FPP=0.057)

monday-api-python-sdk EXCLUDED -- failed FPP pre-screen.

### Sector control
QQQ (Invesco NASDAQ 100 ETF) -- monday.com is a US-listed
NASDAQ technology company. Appropriate sector control.
IWF (Russell 1000 Growth) as secondary control if needed.

### Risk factors
1. C7 ambiguity -- mcp AI tooling investment could support
   positive regime if AI-first Work OS moat compounds.
   Six-month horizon result should be interpreted in context
   of AI adoption developments during study period.
2. Short study period -- MNDY listed June 2021, giving only
   58 months of data. Shorter than most universe companies.
3. Market context -- MNDY IPO coincided with peak growth
   stock valuations (2021) followed by significant drawdown
   (2022). Rate cycle impact may dominate early signal months.
4. monday-sdk-js marginal -- FPP=0.057, n=35. Thin volume
   may limit contribution to pipeline signal.

### Confidence level
Medium-low. C7 assessment is genuinely ambiguous.
Prediction is negative regime but weaker than DDOG/TWLO/GTLB.
Pipeline result should be interpreted carefully -- positive
or null outcome would not be surprising given the C7 ambiguity.

---

## Summary

| Ticker | Company      | Predicted | Confidence | Batch |
|--------|--------------|-----------|------------|-------|
| MNDY   | Monday.com   | Negative  | Medium-low | 3     |

---

## Pre-commitment statement

The above prediction and condition assessment was committed
to GitHub before any MNDY pipeline was executed.

Signed: Charlotte Hyde
Date: May 2026
GitHub: Chyde2010/ps_index
