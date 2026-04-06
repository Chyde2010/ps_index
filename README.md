# Structural Power Index (Ps) — Cross-Sectional Validation Study

**Status:** Pre-pipeline lock — repository selections confirmed, pipeline not yet run
**Protocol version:** v1.4
**Lock date:** April 2026
**Study period:** January 2019 – March 2026

---

## Overview

The Structural Power Index (Ps) is a quantitative signal derived from open-source
repository commit data that measures the structural engineering health of a technology
company. It is designed to capture the rate at which a company is building new
capabilities — as distinct from maintaining existing ones — through analysis of
commit velocity, engineering stability and the entropy of structural development
across a company's public open-source footprint.

This repository contains the code, data and methodology for a cross-sectional
validation study of the Ps Index across ten enterprise technology companies.

The baseline Ps analyses for Microsoft (MSFT) and NVIDIA (NVDA) were conducted
separately and are referenced throughout this study as the validation baseline.

---

## Methodology

The Ps Index is defined as:

Ps = Norm(V x phi x (1 - H))

Where:
- V   = Innovation Velocity — 90-day rolling corporate contributor commit count
- phi = Engineering Stability — ratio of Structural Events to total commits
- H   = Shannon Entropy of the structural commit distribution across repositories
- Norm = Z-score normalisation against each company's own historical mean and std

A high Ps score indicates a period of concentrated, structurally productive
engineering activity relative to the company's own baseline. The index is
company-relative rather than cross-company absolute.

A Ps reading above +1.5 sigma is defined as a high-conviction signal episode.

---

## Repository Selection Protocol

Repository selection follows Protocol v1.4, documented in full at
/protocol/repository_selection_protocol_v1.4.md

The protocol applies four necessary conditions to each candidate repository:

N1a: Minimum 200 verified corporate contributor commits across study period
N1b: Minimum 10 corporate commits per 90-day window in at least 48 of 87 months
N2:  Corporate contributor activity in at least 48 of 87 monthly windows
N3:  Corporate contributor ratio >= 15% (10% for mature OSS products)
N4:  Sample phi >= 0.05 based on keyword classification of 200 sampled commits

Repositories passing all necessary conditions are reviewed manually and up to 7
are selected per company based on documented strategic rationale. All selections
were finalised and committed to this repository before any regression pipeline
was run. The git commit timestamp on this README and the selection files in
/data/selections/ provides an independent record of the pre-commitment lock.

---

## Company Universe

| Ticker | Company        | Selected repos | Classification            |
|--------|----------------|----------------|---------------------------|
| MSFT   | Microsoft      | 5              | Full — baseline           |
| NVDA   | NVIDIA         | 6              | Full — baseline           |
| GOOGL  | Alphabet       | 7              | Full                      |
| AMZN   | Amazon         | 6              | Full                      |
| CRM    | Salesforce     | 5              | Full                      |
| AMD    | AMD            | 6              | Full                      |
| META   | Meta Platforms | 7              | Full                      |
| NOW    | ServiceNow     | 0              | Methodology boundary case |
| SNOW   | Snowflake      | 6              | Full                      |
| MDB    | MongoDB        | 7              | Full                      |
| ESTC   | Elastic        | 7              | Full                      |
| PLTR   | Palantir       | 0              | Voluntary boundary case   |

---

## Selected Repositories

### GOOGL — Alphabet (7 repos)
tensorflow/tensorflow              | phi=0.340 | corp=80344 | AI/ML infrastructure
google/perfetto                    | phi=0.285 | corp=68964 | Android/Chrome observability
google/jax                         | phi=0.210 | corp=29992 | AI/ML research framework
google/skia                        | phi=0.155 | corp=26439 | Android/Chrome/Flutter graphics
GCP/k8s-config-connector           | phi=0.350 | corp=8950  | Google Cloud infrastructure
google/gvisor                      | phi=0.275 | corp=9015  | Google Cloud security
GCP/magic-modules                  | phi=0.445 | corp=6814  | Google Cloud service velocity

### AMZN — Amazon (6 repos)
aws/eks-distro                     | phi=0.870 | corp=1650  | Container/Kubernetes platform
aws/aws-ofi-nccl                   | phi=0.405 | corp=1163  | AI/ML network infrastructure
aws/amazon-ecs-agent               | phi=0.385 | corp=1837  | Container compute runtime
boto/boto3                         | phi=0.665 | corp=5327  | Developer platform
aws/aws-cli                        | phi=0.325 | corp=6084  | AWS management interface
aws/s2n-tls                        | phi=0.280 | corp=1692  | Security infrastructure

### CRM — Salesforce (5 repos)
forcedotcom/source-deploy-retrieve | phi=0.860 | corp=1369  | Platform/DevOps
forcedotcom/sfdx-core              | phi=0.485 | corp=1774  | Platform/Developer
forcedotcom/code-analyzer          | phi=0.375 | corp=1249  | Platform/Developer
forcedotcom/source-tracking        | phi=0.335 | corp=1247  | Platform/DevOps
salesforce/lwc                     | phi=0.320 | corp=1207  | Core Product/UI

### AMD — Advanced Micro Devices (6 repos)
ROCm/HIP                           | phi=0.420 | corp=2378  | GPU programming interface
ROCm/ROCR-Runtime                  | phi=0.380 | corp=2028  | Core GPU compute runtime
ROCm/rccl                          | phi=0.375 | corp=652   | Multi-GPU communications
ROCm/aomp                          | phi=0.310 | corp=4680  | OpenMP GPU compiler
ROCm/AMDMIGraphX                   | phi=0.245 | corp=1739  | AI graph inference engine
ROCm/MIOpen                        | phi=0.145 | corp=1032  | Deep learning primitives

### META — Meta Platforms (7 repos)
facebook/Ax                        | phi=0.415 | corp=4856  | AI/ML
facebook/hermes                    | phi=0.425 | corp=8804  | Mobile Platform
facebookresearch/faiss             | phi=0.355 | corp=1159  | AI/ML
pytorch/FBGEMM                     | phi=0.340 | corp=4444  | AI/ML
facebookincubator/fizz             | phi=0.310 | corp=4710  | Core Infrastructure
facebook/react-native              | phi=0.290 | corp=20080 | Mobile Platform
facebook/rocksdb                   | phi=0.260 | corp=3603  | Core Infrastructure

### SNOW — Snowflake (6 repos)
snowflakedb/snowpark-python        | phi=0.495 | corp=2283  | Data Engineering/AI
snowflakedb/snowflake-jdbc         | phi=0.365 | corp=1018  | Platform Connectivity
snowflakedb/snowflake-ingest-java  | phi=0.360 | corp=684   | Data Ingestion
snowflakedb/gosnowflake            | phi=0.310 | corp=577   | Platform Connectivity
snowflakedb/snowflake-connector-python | phi=0.275 | corp=954 | Platform Connectivity
snowflakedb/snowflake-connector-net | phi=0.220 | corp=355  | Platform Connectivity

### MDB — MongoDB (7 repos)
mongodb/mongo                      | phi=0.335 | corp=38623 | Core Database
mongodb/libmongocrypt              | phi=0.405 | corp=865   | Security
mongodb/mongo-java-driver          | phi=0.350 | corp=1293  | Platform/Drivers
mongodb/mongo-c-driver             | phi=0.310 | corp=881   | Platform/Drivers
mongodb/node-mongodb-native        | phi=0.225 | corp=1889  | Platform/Drivers
mongodb/specifications             | phi=0.205 | corp=749   | Platform Standards
mongodb/mongodb-atlas-cli          | phi=0.210 | corp=1352  | Atlas Platform

### ESTC — Elastic (7 repos)
elastic/kibana                     | phi=0.425 | corp=40747 | Core Platform/UI
elastic/elasticsearch-specification | phi=0.365 | corp=1195 | Platform Standards
elastic/elasticsearch              | phi=0.335 | corp=22605 | Core Platform/Search
elastic/logstash                   | phi=0.325 | corp=618   | Data Ingestion
elastic/apm-server                 | phi=0.310 | corp=1412  | Observability
elastic/cloud-on-k8s               | phi=0.295 | corp=1308  | Cloud Infrastructure
elastic/elastic-agent              | phi=0.285 | corp=2003  | Observability/Security

---

## Research Questions

RQ1: Does the Ps signal generalise across companies or is it a single-stock anomaly?
RQ2: Is signal character systematically determined by company and stock type?
RQ3: Is VIX 20 a universal regime threshold or company-specific?
RQ4: What is the minimum open-source footprint required for a meaningful signal?
RQ5: Can Ps rank companies cross-sectionally as a relative value signal?

---

## Known Methodology Limitations

Open-source visibility bias: Companies that invest heavily in open-source are more
visible to this methodology than companies that keep all engineering proprietary.

GitHub privacy-masked addresses: Users with email privacy enabled appear as
users.noreply.github.com — corporate ratios are lower bounds on true activity.

API fetch cap artefact: A 50-page fetch cap caused false N1b failures for very
large repositories. Affected repos were verified via full uncapped fetches.
Full details in /protocol/repository_selection_protocol_v1.4.md.

Cross-sectional comparability: Ps scores are Z-score normalised against each
company's own history. Cross-company comparisons are indicative not definitive.

SDK and connector inflation: Language SDK and connector repos exhibit elevated
phi scores. Documented in selection rationale for AMZN, SNOW and MDB.

---

## Repository Integrity

Pre-commitment lock date: April 2026
The git commit timestamp on this file and the selection files in /data/selections/
provides an independent record that all selections were finalised before any
regression pipeline was executed.

---

## Disclaimer

This repository is for research purposes only. Nothing herein constitutes
investment advice. The Ps Index is an experimental quantitative signal under
active development.

---

## Author

Charlotte Hyde
Structural Power Index methodology and cross-sectional validation study
