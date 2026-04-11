# CRM Repository Selection — Protocol v1.4 + Amendment v1.4a

## Pre-Screen Date
April 2026

## Amendment Criterion
Any locked repo with sample full-pipeline phi < 0.05 is eligible
for replacement with the highest-ranked qualifying alternative
by sample full-pipeline phi. This criterion was pre-specified
before running the pre-screen.

## Locked Selection Results

| Repo | N4 phi | Sample FP phi | Status |
|---|---|---|---|
| salesforce/lwc | 0.320 | 0.240 | Confirmed |
| forcedotcom/code-analyzer | 0.375 | 0.150 | Confirmed |
| forcedotcom/source-deploy-retrieve | 0.860 | 0.090 | Confirmed |
| forcedotcom/sfdx-core | 0.485 | 0.070 | Confirmed |
| forcedotcom/source-tracking | 0.335 | 0.010 | BELOW THRESHOLD |

## Amendment

REPLACED: forcedotcom/source-tracking
- Sample full-pipeline phi: 0.010 (below threshold 0.05)
- Reason: Commits are characteristically small keyword-positive
  changes that collapse under the 100-line churn floor

WITH: forcedotcom/sfdx-scanner
- Sample full-pipeline phi: 0.150
- Pillar: Platform/Developer
- Rationale: Same pillar as source-tracking, materially higher
  structural signal, similar repo character to code-analyzer

## Final CRM Selection — Protocol v1.4a

| Repo | Sample FP phi | Source |
|---|---|---|
| salesforce/lwc | 0.240 | Locked v1.4 confirmed |
| forcedotcom/code-analyzer | 0.150 | Locked v1.4 confirmed |
| forcedotcom/sfdx-scanner | 0.150 | Amendment v1.4a |
| forcedotcom/source-deploy-retrieve | 0.090 | Locked v1.4 confirmed |
| forcedotcom/sfdx-core | 0.070 | Locked v1.4 confirmed |

## Keyword Specification
Protocol v1.4b applied — expanded keyword list motivated by
META neutral commit diagnostic (44% neutral rate identified).

Structural keywords added: extend, expose, create, build,
integrate, migrate, upgrade, enhance, generate, register,
replace, centralize, centralise, tune, optimize, optimise,
improve, expand, scale, port

Maintenance keywords added: bump, changelog, merge branch,
sync, pin, update version, bump version, updating hashes,
update hashes, deploy, release notes
