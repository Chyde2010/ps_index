# ZS (Zscaler Inc.) Assessment Result
## Date: May 2026
## Exchange: NASDAQ

## Assessment stage: C6 qualitative assessment
## No diagnostic run -- eliminated on visual inspection.

## Classification: C6 FAIL -- developer relations surface only

---

## Seven-condition assessment

C1 -- Consumption or usage-based revenue: PASS
  Zscaler charges per user per month across platform tiers
  (Business, Transformation, Elite). Revenue scales with
  user count and feature adoption. As enterprises expand
  zero trust deployments, more users onboard automatically.
  Clear pass.

C2 -- Embedded platform, high switching costs: PASS
  Zscaler's zero trust platform sits in the critical path
  of every internet-bound connection for every enterprise
  user. Removing it requires rebuilding the entire network
  security architecture -- replacing policy rules,
  re-integrating identity providers, re-establishing branch
  office connectivity. Switching cost measured in months
  of enterprise IT effort. Clear pass.

C3 -- Frictionless consumption uplift: PASS
  As enterprises grow headcount, Zscaler revenue grows
  automatically. More cloud application access means more
  traffic through the platform. Upsell from Business to
  Transformation tier within existing relationships.
  Clear pass.

C4 -- Near-term revenue realisation: PASS
  Annual subscription fees recognised over contract term.
  Clear pass.

C5 -- Product revenue primacy: PASS
  Pure software platform. No hardware. Professional
  services a small and declining percentage of revenue.
  Clear pass.

C6 -- Open-source observability: FAIL
  See assessment below.

C7 -- Engineering investment compounds the moat: PASS
  Zero trust platform compounds with every enterprise
  deployment. More customers generate more threat
  intelligence data which improves detection accuracy
  which attracts more customers. ZIA and ZPA deepen
  with every policy integration. Data flywheel is genuine.
  Strategic acquisitions (Red Canary August 2025, SPLX
  November 2025) compound AI-powered security operations
  capability. Clear pass.

---

## C6 Assessment

The zscaler GitHub org (github.com/zscaler) has 57 repos.
Visual inspection confirms all are developer relations:
  - zscaler-sdk-python (Python API client)
  - zscaler-sdk-go (Go API client)
  - zscaler-sdk-android (Android SDK)
  - terraform-provider-zia (Terraform for ZIA)
  - terraform-provider-zpa (Terraform for ZPA)
  - terraform-aws/azure/gcp-cloud-connector-modules
  - zscaler-mcp-server (AI integration MCP server)
  - ZscalerCWP org: 6 repos, IaC scanning tooling

Every repo is either an API client SDK, a Terraform
deployment module, or a customer-facing integration tool.

The core zero trust exchange engineering -- SSL inspection
engine, policy enforcement layer, AI-powered threat
detection, SASE architecture -- is entirely private.
A security company publishing its inspection logic would
be handing attackers a blueprint. This is by design.

C6 failure mechanism: developer relations surface only.
Security by necessity -- same pattern as Corero, PagerDuty.
No diagnostic run required -- visual inspection sufficient.

---

## Security sector pattern

ZS confirms an emerging pattern in the security sector:
security companies keep strategic engineering private by
design. The C6 barrier is structural and permanent for
this category. Other security companies assessed:
  - Corero Network Security: C6 fail (same mechanism)
  - Palo Alto Networks (PANW): not formally assessed
    but expected same outcome

---

## Summary

| Ticker | Company   | Result  | Failure mode              |
|--------|-----------|---------|---------------------------|
| ZS     | Zscaler   | C6 fail | Developer relations       |
|        |           |         | surface only              |

Not added to signal universe. No pipeline run.
C1-C5 and C7 all pass -- C6 is the sole barrier.
Security sector engineering private by design.

---

## Updated no-signal/fail universe

GOOGL, META, MDB, ESTC, AMD, DT,
INTU, ADSK, ADBE, RBLX, APP, ZS
