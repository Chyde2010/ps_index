# Live Track Record -- Methodology Note
## Updated: April 2026

## What changed from original workflow

The live track record has been updated to align with
the two-stage methodology validated in Paper 2.

### Original approach
- Cross-sectional normalisation of raw Ps values across
  signal companies at each month
- Single Ps Z-score output
- No explicit Stage 1 / Stage 2 distinction
- GTLB missing from short overlay

### Updated approach (this version)
- Stage 1: Own-history Z-score (signal identification)
  Each company normalised against its own history.
  HC flag triggers at +1.5 sigma on own-history Z-score.
- Stage 2: Cross-sectional ranking of own-history Z-scores
  for portfolio weighting. Valid because all own-history
  Z-scores are already on identical scale (mean=0, std=1).
- GTLB added to short overlay (negative regime confirmed)
- Output includes both own_z (Stage 1) and cs_z (Stage 2)
- All Ps components included in output (V, phi, H, entropy_gap)
- Output structured as alt data feed format

## Universe
Positive regime (long): MSFT, AMZN, CRM, SNOW
Negative regime (short): DDOG, TWLO, GTLB

## Signal logic
- HC flag (hc_flag): own_z >= 1.5 -- primary signal
- HC CS flag (hc_cs_flag): cs_z >= 1.5 -- secondary signal
- Long: positive regime company with hc_flag = True
- Short: negative regime company with hc_flag = True

## Calibration factors (from cross-sectional validation)
MSFT=0.378, AMZN=0.253, CRM=0.524, SNOW=0.528
DDOG=0.511, TWLO=0.903, GTLB=0.511 (approximated)

## Output file
live_track_record/ps_signal_history.csv

## Own-history series files
live_track_record/ps_series/{TICKER}_ps_series.csv
One file per company. Accumulates each month.
Used to compute own-history Z-scores in Stage 1.

## Why this is methodologically consistent with Paper 2
Paper 2 found that own-history normalisation is required
to detect the negative regime signal. Cross-sectional
normalisation of raw Ps values on a heterogeneous universe
conflates repository scale with signal intensity and
suppresses the negative signal entirely.

Own-history normalisation asks: is this company elevated
relative to its own baseline? This is the theoretically
correct question for regime identification. The live
track record now uses the same methodology as the paper
to ensure the commercial product is internally consistent
with the academic evidence.
