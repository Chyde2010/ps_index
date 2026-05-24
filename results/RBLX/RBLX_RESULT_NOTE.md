# RBLX (Roblox Corporation) Assessment Result
## Date: May 2026
## Exchange: NYSE

## Assessment stage: C6 domain diagnostic (2 rounds)
## No pipeline run -- eliminated at diagnostic stage.

## Classification: C6 FAIL -- hybrid failure mechanism

---

## Seven-condition assessment

C1 -- Consumption or usage-based revenue: PASS
  Roblox generates revenue through Robux -- the in-platform
  currency users purchase to spend on virtual items, avatar
  accessories and developer-created experiences. Revenue
  scales directly with platform engagement and Robux
  purchases. Pure consumption model. Clear pass.

C2 -- Embedded platform, high switching costs: PARTIAL PASS
  Creator switching costs are high -- developers have built
  skills, audiences and revenue streams on Roblox's
  proprietary engine and APIs. Rebuilding on a competitor
  platform means starting from scratch. User switching costs
  are lower -- engagement is driven by social network effects
  rather than technical lock-in. Partial pass.

C3 -- Frictionless consumption uplift: PASS
  As user base grows and engagement increases, Robux spending
  grows automatically. Developer payouts grow with platform
  revenue share. The flywheel is genuinely frictionless --
  more users attract more developers who build better
  experiences which attract more users. Clear pass.

C4 -- Near-term revenue realisation: PARTIAL PASS
  Roblox defers Robux revenue over the estimated lifetime
  of a user (typically 23 months). Revenue recognition lags
  actual cash intake significantly. Partial pass -- the
  consumption model is real but the accounting treatment
  creates a lag.

C5 -- Product revenue primacy: PASS
  Pure platform revenue. No hardware. No professional
  services. Revenue entirely from Robux sales and developer
  exchange fees. Clear pass.

C6 -- Open-source observability: FAIL
  See diagnostic results below.

C7 -- Engineering investment compounds the moat: LEAN PASS
  Case for pass:
  - Luau programming language open-sourced and adopted
    externally (Alan Wake 2, Second Life, Warframe,
    Farming Simulator 2025). Language adoption compounds
    creator ecosystem lock-in.
  - Cube 3D mesh generation AI trained on Roblox proprietary
    mesh data -- competitors cannot replicate the dataset.
    1.8M+ assets generated since March 2025.
  - Creator ecosystem lock-in: developers invest years
    building skills and audiences on the platform.
  Case against:
  - Operating loss of $1.06bn in 2024 on $3.60bn revenue.
    Engineering investment not translating to profitability.
  - Tarmac (key developer tooling) now primarily maintained
    by engineer who left the company -- fragmentation signal.
  - Read-only mirror strategy suggests strategic engineering
    is private and not compounding publicly.
  Net: C7 lean pass with significant caveats.

---

## C6 Domain Diagnostic Results (May 2026)

Two diagnostic rounds conducted.

Corporate domain: roblox.com
Study window: Jan 2019 to Mar 2026

### Round 1

| Repo                    | Corp% | n    | Verdict  |
|-------------------------|-------|------|----------|
| luau-lang/luau          | 67%   | 100  | STRONG   |
| Roblox/cube             | 47%   | 34   | MODERATE |
| Roblox/secrets-scanning | -     | -    | NOT FOUND|
| Roblox/bloxy            | -     | -    | NOT FOUND|
| Roblox/place-ci-cd-demo | 40%   | 10   | MODERATE |

### Round 2

| Repo                    | Corp% | n    | Verdict  |
|-------------------------|-------|------|----------|
| luau-lang/luau-polyfill | -     | -    | NOT FOUND|
| Roblox/tarmac           | 11%   | 100  | WEAK     |
| Roblox/lune             | -     | -    | NOT FOUND|

Total strong repos (>=50%, n>=20): 1 (luau-lang/luau only)

---

## C6 Failure Mechanism: Hybrid

Two distinct failure patterns operating simultaneously.

### Pattern 1: Monorepo mirrors (C6 Type 7)
The primary Roblox GitHub org contains numerous read-only
mirrors from Roblox's internal monorepo:
  jest-roblox, luau-regexp, react-roblox, roact, testez
  and others explicitly described as "read-only mirrors"

These repos will show FPP=0.000 bot commit patterns
identical to Atlassian's pragmatic-drag-and-drop finding.
All excluded from diagnostic.

### Pattern 2: Community handover on non-mirror repos
The non-mirror repos that gained external traction have
been handed to the community or to engineers who left:

Roblox/tarmac: 75/100 commits from lpghatguy.com
  LPGHatGuy (Lucien Greathouse) built Tarmac while at
  Roblox and continues as primary maintainer after leaving.
  Same pattern as INTU karate and Adobe react-spectrum.

Roblox/lune: Lives under lune-org/lune not Roblox/lune.
  Created by a Roblox engineer but maintained in a
  separate community org.

luau-lang/luau: 67% corporate -- the one clean signal.
  Roblox language team still dominates commit history
  despite external adoption. But one repo is insufficient
  for a robust pipeline signal.

---

## C7 Note: Tarmac finding

The Tarmac finding is worth flagging beyond the C6 failure.
A company whose key open-source developer tooling is now
primarily maintained by an engineer who left the company
is showing engineering fragmentation consistent with high
entropy rather than low entropy. This is a mild negative
signal about the quality of the developer ecosystem moat
rather than a positive one.

---

## Summary

| Ticker | Company | Result  | Failure mode           |
|--------|---------|---------|------------------------|
| RBLX   | Roblox  | C6 fail | Hybrid: mirrors +      |
|        |         |         | community handover     |

Not added to signal universe. No pipeline run.

---

## Updated universe notes

No-signal / C6 fail universe now includes:
  GOOGL, META, MDB, ESTC, AMD, DT, INTU, ADSK, ADBE, RBLX

Regime-dependent (not added):
  TEAM (Atlassian)

Live positive universe: MSFT, AMZN, CRM, SNOW, BABA
Live negative universe: DDOG, TWLO, GTLB, MNDY
