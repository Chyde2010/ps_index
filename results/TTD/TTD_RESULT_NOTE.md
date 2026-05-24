# TTD (The Trade Desk Inc.) Assessment Result
## Date: May 2026
## Exchange: NASDAQ

## Assessment stage: C6 qualitative assessment
## No diagnostic run -- eliminated on visual inspection
## and UID2 transfer finding.

## Classification: C6 FAIL
## Mechanism: UID2 transferred to industry body;
##             core DSP engineering private.

---

## Seven-condition assessment

C1 -- Consumption or usage-based revenue: PASS
  The Trade Desk charges approximately 20% of advertising
  spend flowing through the platform as a platform fee.
  Revenue scales directly with ad spend volume. The more
  advertisers spend through the platform, the more TTD earns.
  Pure consumption model. Clear pass.

C2 -- Embedded platform, high switching costs: PASS
  Agencies and advertisers have years of audience segments,
  creative templates, campaign performance data and
  attribution models embedded in the platform. The UID2
  identity framework is increasingly embedded into publisher
  and advertiser workflows across the open internet.
  Switching to a competing DSP means losing campaign history
  and audience data. Clear pass.

C3 -- Frictionless consumption uplift: PASS
  As advertisers increase budgets, TTD revenue grows
  automatically. New ad formats (CTV, audio, retail media)
  expand addressable spend within existing customer
  relationships. Clear pass.

C4 -- Near-term revenue realisation: PASS
  Platform fees recognised as advertising runs.
  No revenue lag. Clear pass.

C5 -- Product revenue primacy: PASS
  Pure software platform revenue. No hardware. Professional
  services minimal. Clear pass.

C6 -- Open-source observability: FAIL
  See assessment below.

C7 -- Engineering investment compounds the moat: PASS
  Kokai AI bidding system compounds with every impression
  processed -- more data improves targeting accuracy which
  attracts more ad spend which generates more training data.
  UID2 ecosystem creates a network effect that deepens with
  every publisher and advertiser that adopts it.
  CTV expansion compounds the platform's cross-device reach.
  Strong C7 -- but the engineering driving this moat
  is entirely private. Clear pass on C7.

---

## C6 Assessment

The Trade Desk GitHub org (github.com/thetradedesk) has 38
repos. The critical finding is the UID2 transfer.

KEY FINDING: UID2 transferred to IAB Tech Lab (2021)
  The Trade Desk contributed the UID2 source code to PRAM's
  Technical Working Group run by IAB Tech Lab for open-source
  collaboration. The Trade Desk stated they would be "just
  like anybody else" as a contributor going forward.

  UID2 now lives under:
    IABTechLab/uid2docs (documentation)
    IABTechLab/uid2-operator (infrastructure)
  Not under thetradedesk org.

  The UnifiedID2 org has only 3 repos:
    uid2-docs-preview, check_version, uid2-tcportal
  None contain strategic engineering.

  This is the same community handover mechanism as INTU
  and ADBE -- The Trade Desk built the strategic asset,
  open-sourced it, then formally handed it to an industry
  body. After transfer, The Trade Desk engineers are
  contributors alongside many other companies.
  Corporate email rate on IABTechLab repos will be diluted
  across many companies -- not observable as TTD signal.

CORE DSP ENGINEERING: entirely private
  The Kokai AI bidding system, the real-time bidding engine,
  the audience platform, the data marketplace infrastructure --
  all entirely private. A DSP's competitive advantage is
  its proprietary bidding algorithms and data assets.
  These will never be open-sourced.

The 38 repos in thetradedesk org are almost certainly:
  - SDK integrations for publishers and advertisers
  - Developer tooling and API clients
  - Documentation
  No diagnostic run required -- pattern is clear.

---

## C6 Failure Mechanism

Industry body handover -- a specific variant of community
handover where the strategic open-source asset is formally
transferred to an industry consortium:

  INTU: karate --> community took over organically
  ADBE: react-spectrum --> community took over organically
  TTD:  UID2 --> formally transferred to IAB Tech Lab

The TTD case is more deliberate -- The Trade Desk
intentionally designed UID2 as an industry standard rather
than a proprietary moat. The open-sourcing was strategic
(to drive adoption) not accidental. But the result for
C6 observability is the same: TTD engineers are one
contributor among many, corporate email rate on UID2 repos
will be too diluted to produce a reliable Ps signal.

---

## Summary

| Ticker | Company        | Result  | Failure mode          |
|--------|----------------|---------|-----------------------|
| TTD    | The Trade Desk | C6 fail | UID2 transferred to   |
|        |                |         | industry body; core   |
|        |                |         | DSP engineering       |
|        |                |         | private               |

Not added to signal universe. No pipeline run.
C1-C5 and C7 all pass -- C6 is the sole barrier.

---

## Updated no-signal/fail universe

GOOGL, META, MDB, ESTC, AMD, DT,
INTU, ADSK, ADBE, RBLX, APP, ZS, HUBS, TTD
