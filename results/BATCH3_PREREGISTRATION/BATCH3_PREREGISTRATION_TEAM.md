# Batch 3 Universe Expansion -- Pre-Registration
## Ticker: TEAM (Atlassian Corporation Plc)
## Exchange: NASDAQ
## Date: May 2026
## Pre-committed before any pipeline execution

---

## Methodology Note

Formula: Ps = V x phi x (1 - H)
- V   = 90-day rolling corporate commit count
- phi = structural commit density (churn floor 100 lines)
- (1-H) = entropy gap

Corporate email domain: atlassian.com
  Secondary domain: connect.atlassian.com (found in diagnostic)
  Verified via GitHub organisation domain verification on
  atlassian-labs organisation.
  Western email convention confirmed.
  Australian company, Sydney and San Francisco headquarters.
  Email format: firstname@atlassian.com confirmed across all
  passing repos.

Bot email exclusions documented:
  bots.bitbucket.org -- Bitbucket pipeline bot commits
  users.noreply.github.com -- GitHub privacy-masked addresses
  github@atlassian.com -- monorepo mirror sync bot

Commercial bar: factor-adjusted 6M p<0.05, retention >70%,
beta POSITIVE (positive regime prediction).

---

## New C6 failure type documented during assessment

C6 Type 7: One-way monorepo mirror
  atlassian/pragmatic-drag-and-drop is a one-way mirror of
  Atlassian's internal monorepo. All commits attributed to
  github@atlassian.com service account. No real PRs. FPP=0.000.
  Code is publicly visible but engineering is private.
  Distinct from C6 Type 6 (self-hosted GitLab) and
  C6 Type 1 (GitHub Enterprise private concentration).

---

## Candidate -- Atlassian Corporation (TEAM)

### Predicted signal: POSITIVE (high confidence)

Highest confidence prediction since MSFT and AMZN in the
original study. All seven conditions pass convincingly.
The Jira/Confluence/Bitbucket ecosystem creates one of the
deepest structural moats in the enterprise software sector.

### Seven-condition assessment

C1 -- Consumption or usage-based revenue: PASS
  Atlassian charges per user per month across Jira, Confluence,
  Trello, Bitbucket and JSM. Cloud migration from server
  licences to cloud subscriptions now largely complete.
  Revenue scales directly with seat count and usage. Free tier
  converts to paid as teams grow -- genuinely frictionless
  consumption uplift built into the pricing model. Clear pass.

C2 -- Embedded platform, high switching costs: PASS
  Strongest C2 in the NASDAQ 100 shortlist. Every software
  engineering team running Jira for issue tracking, Confluence
  for documentation, Bitbucket for code and JSM for IT service
  management has built years of workflow history, custom fields,
  automation rules and integrations inside Atlassian. Switching
  means migrating every ticket, every document, every
  automation. The switching cost compounds with every year of
  usage. Exceptionally clear pass.

C3 -- Frictionless consumption uplift: PASS
  Atlassian's viral bottom-up growth model is the textbook
  example of frictionless consumption uplift. Teams adopt Jira
  free, grow past the free tier threshold, convert to paid, add
  seats as the team grows, and expand into Confluence and JSM
  without a top-down sales cycle. Net revenue retention
  consistently above 120%. Clear pass.

C4 -- Near-term revenue realisation: PASS
  Monthly cloud subscription fees recognised as earned.
  No revenue lag. Clear pass.

C5 -- Product revenue primacy: PASS
  Pure software platform revenue. No hardware. Professional
  services minimal. Stock trades on ARR, cloud revenue growth
  and operating leverage. Clear pass.

C6 -- Open-source observability: PASS
  Three diagnostic rounds required to identify clean repos.
  Key finding: atlassian/pragmatic-drag-and-drop is a one-way
  monorepo mirror (new C6 Type 7 classification) -- excluded.
  High-star community repos (compiled, nadel) show heavy GitHub
  privacy masking -- excluded.

  Final four repos passing FPP pre-screen:
  - atlassian/atlascode            FPP=0.090 n=100 (80% corp)
    VS Code extension for Jira and Bitbucket. Developer
    ecosystem tooling. Active: 90 open issues.
  - atlassian/date-time-api        FPP=0.081 n=74  (90% corp)
    JS datetime manipulation library. Internal utility.
    Individual engineers confirmed.
  - atlassian/openapi-request-validator FPP=0.080 n=100 (54%)
    OpenAPI request/response validation. Bot commits excluded.
    Individual engineer emails confirmed post-exclusion.
  - atlassian/gostatsd             FPP=0.050 n=100 (50% corp)
    Go StatsD daemon for internal monitoring. Low community
    exposure. Individual engineers confirmed.

  FPP consistency across four repos (0.050-0.090) suggests
  genuine characteristic of Atlassian engineering rather than
  noise from any single repo. Same pattern as BABA.

C7 -- Engineering investment compounds the moat: PASS
  Strongest C7 in the NASDAQ 100 shortlist. Multiple
  compounding mechanisms:

  1. Platform integration compounds with every release.
     Each new automation capability, each new integration
     between Jira/Confluence/Bitbucket/JSM, each new AI
     feature in Atlassian Intelligence makes the combined
     platform more valuable and harder to replicate.

  2. Developer ecosystem network effect. Thousands of
     marketplace apps built on Atlassian Connect framework
     create a network effect competitors cannot replicate
     without years of investment. ServiceNow, Linear and
     GitHub Projects are all attempting to compete but
     none have the breadth or depth of the Atlassian suite.

  3. atlaspack -- Atlassian built their own frontend bundler
     written in JavaScript and Rust. This is a serious
     structural engineering investment that compounds the
     platform's performance advantage and cannot be replicated
     by competitors without equivalent engineering commitment.

  4. AI compounding. Atlassian Intelligence is built on
     years of Jira issue history, Confluence documentation
     and JSM ticket data that only Atlassian possesses.
     The AI features improve with every customer interaction
     in a way competitors cannot replicate from scratch.

  Clear pass -- engineering compounds moat at multiple levels.

### Study period
NASDAQ listed: June 2015 (IPO). Cloud transition from ~2018.
Study period: January 2018 to March 2026 (98 months).
Start date reflects when cloud engineering became dominant
and observable via the four passing repos.

### Repos (pipeline -- 4 repos, all passing pre-screen)
- atlassian/atlascode                FPP=0.090 n=100
- atlassian/date-time-api            FPP=0.081 n=74
- atlassian/openapi-request-validator FPP=0.080 n=100
- atlassian/gostatsd                 FPP=0.050 n=100

### Sector control
QQQ (Invesco NASDAQ 100 ETF) -- primary.
Atlassian is NASDAQ-listed. QQQ appropriate.
SPY as market control.

### Risk factors
1. C6 complexity: required three diagnostic rounds and
   documented new C6 Type 7 failure mechanism. The four
   passing repos are platform tooling and infrastructure --
   not core Jira/Confluence product engineering. The core
   product engineering remains in the internal monorepo.
   Signal observability is real but peripheral to the
   primary product.
2. Cloud transition timing: the 2018 start date captures
   the cloud transition period but may miss the earlier
   server licence era which had different engineering dynamics.
3. Macro sensitivity: Atlassian de-rated significantly in
   2022 alongside the broader SaaS multiple compression.
   Rate cycle effects may influence signal clarity in that
   period.
4. gostatsd thin corporate rate (50%): just at the strong
   threshold. Community contributions from NewRelic engineers
   (1x newrelic.com observed) suggest some external exposure.

### Confidence level
HIGH. All seven conditions pass convincingly. C7 is the
strongest in the NASDAQ 100 shortlist. FPP scores are
consistent and above threshold across all four repos.
This is the highest confidence prediction since MSFT and
AMZN in the original study.

---

## Summary

| Ticker | Company    | Predicted | Confidence | Batch |
|--------|------------|-----------|------------|-------|
| TEAM   | Atlassian  | Positive  | High       | 3     |

---

## Pre-commitment statement

The above prediction and condition assessment was committed
to GitHub before any TEAM pipeline was executed.

Signed: Charlotte Hyde
Date: May 2026
GitHub: Chyde2010/ps_index
