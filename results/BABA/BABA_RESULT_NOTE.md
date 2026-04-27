# BABA (Alibaba Group) Pipeline Result
## Date: April 2026

## Pre-registration prediction: POSITIVE signal (medium confidence)
## Empirical result: POSITIVE signal -- PASS

## Key findings
- Full 6M: adj beta=+0.0397, p=0.006, retention=201% -- PASS
- High VIX 6M: adj beta=+0.1928, p<0.0001, retention=335% -- PASS
- All 9 factor-adjusted betas positive -- perfectly consistent direction
- HC mean 6M return: +23.1% (16 episodes, clustering in 2024-2025)
- Q4 vs Q1 spread at 6M: +1.2pp (compressed -- see caveat below)
- Corporate commits: 29,080
- Structural events: 14,277

## Commercial verdict
POSITIVE SIGNAL -- BABA joins positive signal universe.
Pre-registration prediction correct.

BABA is the first non-US, non-Western company in the Ps Index
universe. This is a commercially significant result for the
emerging markets extension of the framework.

## Signal characteristics
The 6M signal emerges after factor adjustment with amplification
(retention 201%) indicating the Ps signal is negatively correlated
with KWEB sector and market returns. This means the signal performs
well specifically in periods when China tech macro headwinds are
suppressing returns -- the engineering moat signal cuts through
the macro noise at 6M but not at shorter horizons.

The High VIX 6M result (beta=+0.1928, p<0.0001) is the strongest
finding. During periods of elevated uncertainty about China tech
the market specifically rewards/punishes companies based on
underlying engineering quality in ways the Ps Index detects.
A spurious signal would wash out under stress -- this one intensifies.

HC episodes cluster in 2024-2025, precisely the period of Alibaba's
AI cloud pivot: Qwen model family launches, AI-native product
releases, triple-digit AI cloud revenue growth for 7 consecutive
quarters. Signal spikes when Alibaba makes its most aggressive
Cloud and AI engineering investments.

## Documented caveat -- regulatory macro risk
Q4-Q1 quartile spread of +1.2pp is compressed versus US positive
signal companies (SNOW +24.2pp, MSFT +15.1pp). This is explained
by China regulatory macro shocks creating large negative return
episodes in high-Ps months:
- 2020-2021: Ant Group IPO cancellation; $18bn regulatory fine;
  BABA stock fell 70%+ in 12 months
- 2025-09 HC episode shows -29.8% at 6M (US-China trade tension)

The regression partially controls for this via KWEB sector factor
and market return. The quartile analysis cannot. This is not a
framework failure -- it is a documented limitation specific to
EM companies with geopolitical/regulatory risk premium.

## Methodological note -- KWEB sector control
KWEB (KraneShares China Internet ETF) was used as sector control
rather than QQQ (which is inappropriate for a Chinese ADR).
KWEB contains BABA as a top holding (~10% weight) which creates
a mild mechanical relationship between the sector control and
the dependent variable. This is a robustness concern to note
in any publication. An alternative specification using no
sector control (market-only adjustment) should be run as
a sensitivity check before formal submission.

## Repos used
Primary (Cloud engineering):
- aliyun/terraform-provider-alicloud  (corp=7,144 struct=2,496 phi=0.349)
- aliyun/alibabacloud-python-sdk      (corp=9,896 struct=5,664 phi=0.572)
- aliyun/alibabacloud-java-sdk        (corp=11,882 struct=6,100 phi=0.513)

Secondary (Platform middleware):
- alibaba/spring-cloud-alibaba        (corp=158 struct=17 phi=0.108)

Note: spring-cloud-alibaba is community-maintained and contributes
only 0.1% of structural events. The signal is driven by the three
Alibaba Cloud repos. Future robustness check: rerun excluding
spring-cloud-alibaba to confirm signal persists with 3 repos only.

## Corporate email domains
- alibabacloud.com: 21,759 commits (74.8%)
- alibaba-inc.com:   7,321 commits (25.2%)

Both domains essential. alibabacloud.com dominates the SDK repos.
alibaba-inc.com dominates terraform and spring-cloud repos.
This is consistent with Alibaba Cloud having a distinct engineering
organisation from core Alibaba Group.

## C6 distinction from Tencent
Tencent failed C6 (Chinese developer email convention).
Alibaba passes C6 because Alibaba Cloud product repos use
corporate email addresses at 79-100% rates. This reflects
Alibaba Cloud's more structured DevOps culture and the aliyun
org's domain-verified status on GitHub. The C6 Type 4 failure
(Chinese developer email convention) is company-specific,
not universal to Chinese tech.

## Updated universe
Positive signal: MSFT, AMZN, CRM, SNOW, BABA
Negative signal: DDOG, TWLO, GTLB
No signal: GOOGL, META, MDB, ESTC, AMD, DT
Failed C6: NET, CFLT, PLTR

## Commercial applications
1. Emily Whiting / JPMorgan EMAP pitch:
   BABA is a $308m position in JMGI. The Ps signal on BABA
   provides a systematic pre-committed engineering quality
   signal for their largest China technology holding.
   The HC clustering in 2024-2025 coincides with the period
   when BABA's AI cloud narrative drove stock re-rating.

2. Paper 2 extension:
   BABA extends the cross-sectional validation to emerging
   markets. The positive signal with documented regulatory
   macro caveat is a genuine finding that adds to the
   framework's discriminatory power.

3. Universe expansion:
   The C6 pass on Alibaba Cloud repos suggests other Chinese
   tech companies with structured cloud engineering (ByteDance,
   Huawei Cloud) may be testable. Requires company-by-company
   C6 diagnostic.
