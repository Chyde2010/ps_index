# APP (AppLovin Corporation) Assessment Result
## Date: May 2026
## Exchange: NASDAQ

## Assessment stage: C6 qualitative assessment
## No diagnostic run -- eliminated on visual inspection.

## Classification: C6 FAIL -- developer relations surface only

---

## Seven-condition assessment

C1 -- Consumption or usage-based revenue: PASS
  AppLovin's software platform charges on a performance
  basis -- advertisers pay per install, per action or per
  impression. Revenue scales directly with ad spend flowing
  through the platform. The AXON AI engine optimises ad
  matching and charges based on outcomes. Pure consumption
  model on the platform side. Clear pass.

C2 -- Embedded platform, high switching costs: PASS
  App developers who integrate AppLovin's MAX mediation SDK
  into their apps are deeply embedded. MAX sits inside the
  app binary -- switching requires full SDK replacement,
  re-testing across devices and app store resubmission.
  AppDiscovery's AXON model learns from each developer's
  specific app and user base over time -- switching means
  losing that accumulated learning. Strong pass.

C3 -- Frictionless consumption uplift: PASS
  As the app economy grows and developers spend more on
  user acquisition, AppLovin revenue grows automatically.
  More ad spend generates more AXON training data which
  improves targeting which attracts more ad spend.
  Genuine frictionless flywheel. Clear pass.

C4 -- Near-term revenue realisation: PASS
  Software platform revenue recognised as ads are served
  and actions are completed. No revenue lag. Clear pass.

C5 -- Product revenue primacy: PASS
  Gaming studio portfolio sold in early 2024. Pure software
  platform revenue going forward. AppDiscovery and MAX
  are the entire business. Clear pass.

C6 -- Open-source observability: FAIL
  See assessment below.

C7 -- Engineering investment compounds the moat: PASS
  The AXON AI model compounds with every ad served.
  More ad events improve targeting accuracy, which improves
  ROI for advertisers, which attracts more ad spend, which
  generates more training data. Genuine data flywheel that
  competitors cannot replicate without equivalent scale.
  Revenue growing at 70%+ year-on-year confirms the moat
  is compounding. Clear pass.

---

## C6 Assessment

The AppLovin GitHub org (github.com/AppLovin) contains:
  - AppLovin-MAX-Unity-Plugin (C#, SDK)
  - AppLovin-MAX-Flutter (Objective-C, SDK)
  - AppLovin-MAX-Swift-Package (Swift, SDK)
  - MAX plugins for Defold, Android, iOS
  - Mirror of Apache Thrift (C++)
  - Mirror of XGBoost (C++)
  - airflow-prometheus-exporter (Python, inactive)

Every active repo is an SDK plugin for the MAX mediation
platform -- developer relations tooling that app developers
use to integrate AppLovin's ad network into their apps.
The Apache Thrift and XGBoost repos are mirrors of external
open-source projects, not AppLovin engineering.

The strategic engineering -- the AXON AI model that powers
ad matching, the MAX mediation auction engine, the
AppDiscovery platform -- is entirely private. AppLovin's
competitive moat is the AXON model trained on billions of
ad events. This will never be open-sourced.

C6 failure mechanism: developer relations surface only.
Same pattern as PagerDuty, Samsara, UiPath from the
original cross-sectional study.

No diagnostic run required -- visual inspection of the
GitHub org confirms the failure mechanism immediately.

---

## Methodological note

APP is a conceptually important finding for the Ps Index
methodology. AppLovin is arguably one of the most compelling
consumption-platform technology businesses in the NASDAQ 100:
  - Revenue growing at 70%+ year-on-year
  - Operating margins expanding rapidly
  - AXON model compounding demonstrably
  - C1-C5 all pass convincingly
  - C7 passes clearly

The framework correctly identifies APP as a positive regime
company on conditions C1-C7 but cannot generate a signal
because the strategic engineering is entirely private.

This is the correct outcome. The framework's C6 requirement
is not an arbitrary gate -- it is the condition that ensures
the signal is based on observable evidence rather than
inference. APP demonstrates that C6 correctly excludes
companies whose moat is real but not observable, preventing
false positive signals based on the framework's qualitative
assessment alone.

---

## Summary

| Ticker | Company   | Result  | Failure mode              |
|--------|-----------|---------|---------------------------|
| APP    | AppLovin  | C6 fail | Developer relations       |
|        |           |         | surface only              |

Not added to signal universe. No pipeline run.
C1-C5 and C7 all pass -- C6 is the sole barrier.

---

## Updated no-signal/fail universe

GOOGL, META, MDB, ESTC, AMD, DT,
INTU, ADSK, ADBE, RBLX, APP
