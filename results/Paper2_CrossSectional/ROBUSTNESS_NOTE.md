# Normalisation Robustness Test
## Date: April 2026

## Objective
Test whether regime classification results are robust
to the choice of normalisation method. Applied to the
7 confirmed signal companies (MSFT, AMZN, CRM, SNOW,
DDOG, TWLO, GTLB) where repository scales are reasonably
comparable.

## Methods tested
A1: Cross-sectional normalisation of ps_raw
    (original paper methodology)
A2: Cross-sectional normalisation of log(ps_raw)
B:  Cross-sectional normalisation of own-history Z-scores
    (Paper 2 methodology)
B0: Own-history Z-scores without cross-sectional step

## Key findings

### Positive regime
ALL four methods produce significant positive beta
at 3M and 6M horizons. The positive regime finding
is fully robust to normalisation choice.
  A1 6M multi: beta=+0.076, p=0.000
  A2 6M multi: beta=+0.057, p=0.001
  B  6M multi: beta=+0.052, p=0.000
  B0 6M multi: beta=+0.051, p=0.000

### Negative regime
Methods B and B0 (own-history) produce significant
negative beta. Methods A1 and A2 (cross-sectional
on raw/log Ps) do not reach significance.
  A1 6M multi: beta=-0.015, p=0.595 (not sig)
  A2 6M multi: beta=-0.022, p=0.506 (not sig)
  B  6M multi: beta=-0.119, p=0.001 (YES)
  B0 6M multi: beta=-0.098, p=0.002 (YES)

### Regime interaction
A1 produces significant interaction terms:
  ps_x_pos: p=0.0006 (YES)
  ps_x_neg: p=0.0345 (YES, marginal)
B produces highly significant interaction terms:
  ps_x_pos: p=0.0000 (YES)
  ps_x_neg: p=0.0000 (YES)

### Quartile spreads at 6M
Positive regime:
  A1: +13.5pp  A2: +15.2pp  B: +10.5pp  B0: +14.3pp
Negative regime:
  A1: -18.2pp  A2: -16.0pp  B: -32.6pp  B0: -34.4pp

## Conclusion
The positive regime finding is fully robust.
The negative regime finding is stronger under
own-history normalisation. The direction is
consistent across all methods but the magnitude
and significance differ. The reason is that
cross-sectional normalisation of raw Ps values
conflates absolute repository scale with
engineering intensity, obscuring the within-company
negative signal for DDOG, TWLO and GTLB.

## Implication for Paper 2
The paper can claim the positive regime result
as robust. The negative regime result should be
presented with the methodological explanation
of why own-history normalisation is more
appropriate for detecting within-company signal
dynamics.
