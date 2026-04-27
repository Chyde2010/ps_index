# Batch 3 Universe Expansion -- Pre-Registration
## Ticker: BABA (Alibaba Group Holding Ltd)
## Date: April 2026
## Pre-committed before any pipeline execution

This document records the predicted signal direction and
seven-condition assessment for Alibaba Group before any
pipeline is run. This is the pre-commitment discipline
that protects against data mining and post-hoc rationalisation.

---

## Methodology Note

This pipeline uses the ORIGINAL Ps Index formula:

    Ps = V x phi x (1 - H)

Where:
- V = 90-day rolling corporate commit count
- phi = structural commit density (churn floor 100 lines)
- (1-H) = entropy gap (Shannon entropy of structural
  commit distribution normalised by log2(n_repos))

Corporate email domains:
- alibaba-inc.com  (primary internal Alibaba Group engineering)
- alibabacloud.com (Alibaba Cloud product engineering)

Both domains confirmed in C6 pre-screen (April 2026).
aliyun GitHub organisation is domain-verified.

The commercial bar remains: factor-adjusted 6M p<0.05,
signal retention >70%, positive beta.

---

## Candidate -- Alibaba Group (BABA)

### Predicted signal: POSITIVE

### Seven-condition assessment

C1 -- Consumption or usage-based revenue: PARTIAL PASS
  Alibaba Cloud (Aliyun) is explicitly consumption-billed --
  IaaS, PaaS and MaaS priced on usage, GPU rental,
  API token sales. Cloud was ~$16.5bn FY2025 growing at
  11% annually, accelerating to 34% in Q2 FY2026.
  China e-commerce (Taobao/Tmall) generates customer
  management revenue (CMR) -- advertising and commissions --
  which is not pure consumption billing. Partial pass on
  the strength of Cloud as the strategically relevant and
  growing segment. Same assessment as original study applied
  AMZN where AWS consumption-billing dominated the signal
  despite non-consumption retail revenue.

C2 -- Embedded platform with high switching costs: PASS
  Taobao/Tmall: merchant storefronts, customer bases,
  Alipay payment infrastructure, Cainiao logistics
  integration and Alibaba data flywheel create extremely
  high switching costs for Chinese merchants. Alibaba Cloud:
  enterprise customers embedded in proprietary tooling,
  DingTalk workflow integration and Qwen AI model
  dependency create high cloud switching costs. Clear pass.

C3 -- Frictionless consumption uplift: PARTIAL PASS
  Cloud consumption scales automatically with customer
  usage -- genuinely frictionless. E-commerce GMV growth
  is more dependent on active merchant acquisition
  investment. Partial pass on Cloud segment.

C4 -- Near-term revenue realisation: PASS
  Cloud billed monthly and recognised immediately.
  E-commerce commissions and advertising recognised
  at transaction. No significant lag. Clear pass.

C5 -- Product revenue primacy: PASS
  No material professional services revenue. Business
  is entirely product and platform revenue. Stock trades
  on Cloud growth, CMR growth and AI narrative. Clear pass.

C6 -- Open-source observability continuity: PASS
  Pre-screen result (April 2026): 4/4 repos pass.
  - aliyun/terraform-provider-alicloud: FPP=0.340 n=100
  - aliyun/alibabacloud-python-sdk: FPP=0.530 n=100
  - aliyun/alibabacloud-java-sdk: FPP=0.630 n=100
  - alibaba/spring-cloud-alibaba: FPP=0.100 n=100
  Corporate email rate: 79% alibaba-inc.com on
  terraform repo. Both domains confirmed active.
  aliyun org domain-verified on GitHub.
  Chinese developer email convention NOT a problem
  on Alibaba Cloud product repos -- clear corporate
  email usage distinguishes Alibaba from Tencent
  (which failed C6 for this reason).

C7 -- Engineering investment compounds the moat: PASS
  Alibaba Cloud's Qwen model family (open-weight AI
  models) compounds a technically proprietary advantage
  in Chinese AI infrastructure that Western peers
  (AWS, Azure, GCP) cannot replicate -- not due to
  resource constraints but due to regulatory access,
  data localisation requirements and Chinese language
  and enterprise context that requires domestic AI
  infrastructure. AI cloud revenue growing at triple-digit
  rates for seven consecutive quarters. Engineering
  investment is directly converting to revenue acceleration
  -- the C7 positive signal mechanism. The moat deepens
  with each Qwen model generation because the training
  data, fine-tuning and deployment infrastructure are
  increasingly embedded in Chinese enterprise workflows.

### Rationale
Alibaba is structurally similar to AMZN in the original
study -- a consumption-platform company where the dominant
revenue segment (e-commerce/retail for AMZN; e-commerce
CMR for Alibaba) is not pure consumption billing but the
strategically decisive engineering investment is in the
cloud and AI platform that IS consumption-billed and
IS compounding a structural moat. The Ps Index signal
for AMZN was driven by AWS engineering activity. The Ps
Index signal for Alibaba is expected to be driven by
Alibaba Cloud engineering activity.

If the signal passes, Alibaba becomes the first non-US,
non-Western company in the Ps Index universe. This is
commercially significant for the Emily Whiting / JPMorgan
EMAP pitch -- her fund holds BABA as a $308m position.

### Study period
NYSE listed September 2014. Open-source corporate GitHub
activity on aliyun org begins approximately 2016.
Study period: January 2016 to March 2026 (123 months).

### Repos
Primary (high corporate email rate, product engineering):
- aliyun/terraform-provider-alicloud (Infrastructure)
- aliyun/alibabacloud-python-sdk (Cloud SDK)
- aliyun/alibabacloud-java-sdk (Cloud SDK)

Secondary (community-maintained, lower weight expected):
- alibaba/spring-cloud-alibaba (Platform Middleware)

### Risk factors
1. E-commerce CMR dominates revenue but is not
   consumption-billed -- may dilute signal if pipeline
   cannot isolate Cloud engineering activity from
   e-commerce activity. However the repos selected are
   all Cloud-specific so the signal should reflect
   Cloud engineering investment.
2. spring-cloud-alibaba is community-maintained --
   diagnostic showed 0% corporate emails in recent
   sample. Historical corporate commits may be sparse.
   Pipeline will determine whether this repo adds
   signal or noise.
3. Regulatory and geopolitical risk affects BABA stock
   returns in ways unrelated to engineering investment
   (2020-2021 Ant Group regulatory action; VIE structure
   uncertainty). These macro shocks may reduce regression
   power. Factor adjustment for market and sector returns
   will partially control for this but not completely.
4. Study period of 123 months is the longest in the study
   -- increases statistical power but also includes the
   2020-2021 regulatory crash which was entirely
   non-engineering-driven.

---

## Summary Table

| Ticker | Company         | Predicted | Confidence | Batch |
|--------|-----------------|-----------|------------|-------|
| BABA   | Alibaba Group   | Positive  | Medium     | 3     |

Medium confidence rather than high because:
- C1 and C3 are partial passes
- Regulatory macro risk may obscure engineering signal
- spring-cloud-alibaba community-maintenance risk
- First non-Western company tested -- unknown unknowns

---

## Pre-commitment statement

The above prediction and condition assessment was committed
to GitHub before any BABA pipeline was executed.
Any subsequent changes to predictions or condition
assessments after pipeline results are known will be
documented as post-hoc revisions and clearly distinguished
from this pre-committed prediction.

Signed: Charlotte Hyde
Date: April 2026
GitHub: Chyde2010/ps_index
