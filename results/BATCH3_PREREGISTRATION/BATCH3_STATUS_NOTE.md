# Batch 3 Status Note
## Date: April 2026

## Batch 3 so far
One company tested: FSLY (Fastly) -- NO SIGNAL.
Prediction was NEGATIVE -- partially wrong.
New C6 constraint type identified: network layer invisibility.

## Batch 3 candidate selection criteria (updated)
Based on Batch 2 and FSLY learnings, Batch 3 candidates must:

1. Pass all seven conditions including C7
   (engineering compounds the moat, not parity maintenance)

2. Have strong C6 coverage of PLATFORM SUBSTRATE repos
   (not just SDK, developer tooling, or network infrastructure)

3. Avoid these categories now known to produce no signal:
   - CDN and networking companies (FSLY, NET) -- network layer
     engineering is never open-sourced
   - Companies with primarily proprietary core engineering
     where open-source is limited to developer relations
     (DT, IOT, PLTR)
   - RPA and workflow automation (PATH) -- C3 fails

4. Prefer companies where the open-source repos ARE the product
   (like SNOW with snowflake-connector-python, or DDOG with
   dd-agent) rather than peripheral tooling around a
   proprietary core

## Characteristics of successful signal companies
Looking at positive signal companies (SNOW, CRM, AMZN, MSFT)
and negative signal companies (DDOG, TWLO, GTLB):

All have:
- Consumption billing with direct revenue link
- Open-source repos that ARE the platform interface
  (not tooling around a proprietary core)
- High corporate email rates in repos
- 70+ months of study period data

## Potential Batch 3 candidates to evaluate
To be pre-registered before any screening:
- HashiCorp (HCP) -- infrastructure as code, strong open-source
- Confluent (CFLT) -- already tested, maintenance mode failed
- Elastic (ESTC) -- already tested, no signal
- PagerDuty (PD) -- C3 fail predicted, similar to PATH
- Supabase -- private
- MongoDB (MDB) -- already tested, no signal

## Decision
Pause Batch 3 pending strategic review.
Universe has not expanded meaningfully through Batch 2 or FSLY.
Priority should shift to:
1. SSRN paper -- highest commercial value action
2. MSFT cache rebuild -- complete the original universe
3. Strategic assessment of whether further batches are warranted
   given the C6 observability constraint
