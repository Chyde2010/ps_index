# Batch 2 Universe Expansion -- Pre-Registration
## Date: April 2026
## Pre-committed before any pipeline execution

This document records the predicted signal direction and
five-condition assessment for each Batch 2 candidate
before any pipeline is run. This is the pre-commitment
discipline that protects against data mining and
post-hoc rationalisation.

---

## Methodology Note

All pipelines in Batch 2 use the ORIGINAL Ps Index formula:

    Ps = V x phi x (1 - H)

Where:
- V = 90-day rolling corporate commit count
- phi = structural commit density (churn floor 100 lines)
- (1-H) = entropy gap (Shannon entropy of structural
  commit distribution normalised by log2(n_repos))

The NoEntropy formula modification was tested empirically
in April 2026 and rejected. It destroyed four existing
signals while creating one spurious signal for AMD.
The original formula stands unchanged.

The commercial bar remains: factor-adjusted 6M p<0.05,
signal retention >70%, positive beta for positive
signal predictions.

---

## Candidate 1 -- GitLab (GTLB)

### Predicted signal: POSITIVE

### Five-condition assessment
- C1 Consumption revenue: PASS
  CI/CD compute minutes, storage and seats billed on
  consumption. Cloud revenue is majority consumption.
- C2 Embedded platform: PASS
  GitLab is the DevOps system of record. Source code,
  CI/CD pipelines, issue tracking and security scanning
  all embedded. Migration cost is extremely high.
- C3 Frictionless consumption uplift: PASS
  Platform improvements automatically consume more CI
  minutes for existing customer workloads. Faster
  runners, better caching, new pipeline features all
  generate additional consumption without customer
  action.
- C4 Near-term revenue realisation: PASS
  Consumption billing means improvements materialise
  in revenue within the same quarter.
- C5 Product revenue primacy: PASS
  Stock trades on cloud revenue mix and ARR growth.
  Direct product revenue. No advertising or hardware.
- C6 Open-source observability continuity: PASS
  gitlab-org repos public since 2011. Full commit
  history throughout any study period.

### Rationale
GitLab is the closest structural match to Snowflake
in the expansion universe. Consumption-billed DevOps
platform with deeply embedded customer relationships
and genuine frictionless uplift mechanism. The
strongest prior probability positive signal candidate
in Batch 2.

### Study period
IPO October 2021. Study period: October 2021 to
March 2026 (54 months).

### Repos to screen
- gitlab-org/gitlab (primary monorepo)
- gitlab-org/gitaly (Git RPC service)
- gitlab-org/gitlab-runner (CI execution)
- gitlab-org/container-registry
- gitlab-org/gitlab-pages

### Risk
Monorepo structure may produce very high commit
volumes. Domain filter for gitlab.com corporate
commits essential. Pre-screen required to confirm
FPP above threshold before full pipeline.

---

## Candidate 2 -- Dynatrace (DT)

### Predicted signal: NEGATIVE

### Five-condition assessment
- C1 Consumption revenue: PASS
  Davis Processing Units (DPUs) billed on consumption.
  Genuine consumption model similar to Datadog.
- C2 Embedded platform: PASS
  Observability platform deeply embedded in customer
  infrastructure. OneAgent deployed across all hosts.
- C3 Frictionless consumption uplift: PASS
  Platform improvements automatically consumed by
  existing monitored infrastructure.
- C4 Near-term revenue realisation: PASS
  DPU consumption changes materialise quickly.
- C5 Product revenue primacy: PASS
  Direct product revenue. No advertising or hardware.
- C6 Open-source observability continuity: PASS
  dynatrace-oss org has active repos. Check specific
  repo history before pipeline.

### Rationale
Dynatrace is structurally identical to Datadog --
observability platform, consumption-billed, deeply
embedded. The Datadog result (negative signal) was
explained by competitive API dynamics -- engineering
investment is competitive necessity rather than
platform deepening. The same mechanism should apply
to Dynatrace. Predicted negative signal for the same
theoretical reason as DDOG.

### Study period
IPO August 2019. Study period: August 2019 to
March 2026 (80 months).

### Repos to screen
- dynatrace-oss/dynatrace-operator
- dynatrace-oss/opentelemetry-metric-utils-dotnet
- dynatrace-oss/log-viewer
- Dynatrace/dynatrace-configuration-as-code
- dynatrace-oss/OneAgent-SDK-Python

### Risk
Dynatrace open-source presence may be thinner than
Datadog. If FPP is below threshold across all repos
the pipeline cannot be run and DT joins NET and CFLT
as failed on Condition 6.

---

## Candidate 3 -- Palantir (PLTR)

### Predicted signal: UNCERTAIN

### Five-condition assessment
- C1 Consumption revenue: PARTIAL
  AIP platform has consumption components but
  government contracts are largely fixed-price.
  Commercial AIP is consumption-billed but not
  yet revenue-dominant.
- C2 Embedded platform: PASS
  Palantir platforms are deeply embedded in
  customer decision-making workflows. Switching
  cost is extremely high.
- C3 Frictionless consumption uplift: PARTIAL
  AIP improvements flow to existing platform
  workloads but government contract revenue
  is not consumption-driven.
- C4 Near-term revenue realisation: PARTIAL
  Commercial AIP consumption realises quickly.
  Government contract revenue is lumpy.
- C5 Product revenue primacy: PASS
  Stock trades primarily on AIP revenue growth
  and commercial expansion.
- C6 Open-source observability continuity: PASS
  palantir org has multiple active repos
  going back to 2014.

### Rationale
Palantir is a genuine framework challenger. The
five-condition assessment is ambiguous -- partially
satisfying most conditions but not clearly passing
any except C2, C5 and C6. The empirical result
will test whether the framework correctly identifies
ambiguous cases as no-signal or whether the partial
satisfaction of conditions is sufficient for a signal.

### Study period
IPO September 2020 (direct listing). Study period:
September 2020 to March 2026 (66 months).

### Repos to screen
- palantir/palantir-java-format
- palantir/blueprint (if available)
- palantir/conjure
- palantir/tritium
- palantir/plottable

### Risk
Palantir's core platform engineering is largely
proprietary. Open-source repos are developer tooling
rather than platform substrate. FPP may be low
across all repos leading to Condition 6 failure.
This is the most likely failure mode for PLTR.

---

## Candidate 4 -- Cloudflare (NET) -- Revised

### Predicted signal: UNCERTAIN

### Previous result
NET tested in March 2026. Failed on Condition 6
due to late open-sourcing of workerd (Sep 2022)
and pingora (Feb 2024) during the study period.
The repo age problem corrupted the backtest.

### Revised approach
Exclude pingora entirely. Shorten study period
to start October 2022 when workerd became public.
This gives 42 months of clean data -- thin but
sufficient for a meaningful regression if the
signal is strong.

### Five-condition assessment (unchanged)
- C1: Partial -- Workers consumption but security
  subscriptions dominant
- C2: Pass -- Workers deeply embedded
- C3: Pass -- workerd improvements flow automatically
- C4: Partial -- Workers consumption realises quickly
- C5: Partial -- stock trades on security narrative
- C6: Pass (revised) -- all repos public Oct 2022+

### Repos (revised -- excludes pingora)
- cloudflare/workers-sdk
- cloudflare/workerd
- cloudflare/wrangler
- cloudflare/cloudflared

### Study period (revised)
October 2022 to March 2026 (42 months).

### Risk
42 months is the thinnest study period in the
entire study. Statistical power is low. Even a
genuine signal may not reach significance.
The previous incoherent beta pattern may persist.

---

## Candidate 5 -- Samsara (IOT)

### Predicted signal: POSITIVE

### Five-condition assessment
- C1 Consumption revenue: PASS
  Connected operations platform billed per connected
  device and per data volume processed.
- C2 Embedded platform: PASS
  IoT sensors embedded in customer fleet and
  operations. Hardware plus software switching
  cost is extremely high.
- C3 Frictionless consumption uplift: PASS
  Platform improvements automatically generate
  more data processing from existing connected
  devices. Better AI features consume more
  compute from existing sensor networks.
- C4 Near-term revenue realisation: PASS
  Consumption billing means improvements
  materialise within the quarter.
- C5 Product revenue primacy: PASS
  Direct product revenue from connected operations
  platform. Stock trades on ARR growth and
  connected device expansion.
- C6 Open-source observability continuity: PASS
  samsarahq org has repos going back to 2018.
  Check specific repo history before pipeline.

### Rationale
Samsara has the strongest five-condition profile
of any new candidate in Batch 2 -- cleaner even
than GitLab on Conditions 1 and 3 because the
consumption mechanism is direct and automatic.
IoT connected device data consumption is the
purest form of frictionless consumption uplift.
Platform improvements generate more data from
existing sensors without any customer action.

### Study period
IPO December 2021. Study period: December 2021
to March 2026 (52 months).

### Repos to screen
- samsarahq/samsara-sdks
- samsarahq/runbook
- samsarahq/thunder
- samsarahq/samsara-python
- samsarahq/api-examples

### Risk
Samsara's core platform engineering is largely
proprietary -- the connected operations AI and
IoT infrastructure. Open-source repos are
primarily SDKs and developer tooling. FPP may
be low leading to Condition 6 failure. This is
the primary risk for IOT.

---

## Candidate 6 -- UiPath (PATH)

### Predicted signal: NO SIGNAL

### Five-condition assessment
- C1 Consumption revenue: PARTIAL
  Automation consumption units have some
  consumption component but primarily per-seat.
- C2 Embedded platform: PASS
  RPA workflows deeply embedded in customer
  business processes.
- C3 Frictionless consumption uplift: FAIL
  Better automation requires active customer
  adoption decisions -- building new workflows,
  retraining staff. Improvements do not
  automatically generate more consumption from
  existing workloads. Same failure mode as
  PagerDuty.
- C4 Near-term revenue realisation: PARTIAL
  Automation unit consumption realises within
  a quarter but Condition 3 failure means
  improvements do not drive automatic uplift.
- C5 Product revenue primacy: PASS
  Direct product revenue. Stock trades on
  ARR and automation unit expansion.
- C6 Open-source observability continuity: PASS
  UiPath has public repos going back to 2018.

### Rationale
UiPath fails Condition 3 definitively -- the
same reason PagerDuty was excluded. Engineering
improvements to the automation platform require
active customer decisions to build new workflows
before generating additional consumption. There
is no automatic frictionless uplift mechanism.
Running the pipeline will validate whether the
framework correctly predicts no signal for
Condition 3 failures.

### Study period
IPO April 2021. Study period: April 2021 to
March 2026 (60 months).

### Repos to screen
- UiPath/uipath-python
- UiPath/UiPath.CoreIpc
- UiPath/orchestrator-powershell
- UiPath/uipath-robot-api
- UiPath/Specialized.Workflows

### Risk
Low FPP likely -- UiPath open-source presence
is thin. May fail Condition 6 pre-screen before
reaching the full pipeline. If it does fail
pre-screen it confirms that Condition 3 failures
correlate with limited open-source platform
investment.

---

## Summary Table

| Ticker | Company    | Predicted | Confidence |
|--------|------------|-----------|------------|
| GTLB   | GitLab     | Positive  | High       |
| DT     | Dynatrace  | Negative  | High       |
| PLTR   | Palantir   | Uncertain | Low        |
| NET    | Cloudflare | Uncertain | Low        |
| IOT    | Samsara    | Positive  | Medium     |
| PATH   | UiPath     | No signal | High       |

## Pattern-finding objective

The six candidates span all predicted outcome
categories. If the empirical results match the
predictions the five-condition framework is
validated as a generalisable selection tool.
If they do not match the mismatches indicate
which conditions need revision.

Specific hypotheses being tested:

H1: Companies with strong C1-C6 satisfaction
    produce positive signals (GTLB, IOT)

H2: Observability companies produce negative
    signals regardless of formula (DT vs DDOG)

H3: Condition 3 failures produce no signal
    (PATH, and partially PLTR)

H4: Framework ambiguity produces uncertain
    empirical results (PLTR, NET)

H5: The original formula correctly classifies
    companies the NoEntropy formula misclassifies

---

## Pre-commitment statement

The above predictions and condition assessments
were committed to GitHub on 15 April 2026 before
any Batch 2 pipeline was executed. Any subsequent
changes to predictions or condition assessments
after pipeline results are known will be documented
as post-hoc revisions and clearly distinguished
from the pre-committed predictions.

Signed: Charlotte Hyde
Date: 15 April 2026
GitHub: Chyde2010/ps_index
