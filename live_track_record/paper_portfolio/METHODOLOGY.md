# Ps Index Paper Portfolio -- Methodology
 
## Structure
 
Starting capital: $1,000,000 USD
Long book: $700,000 (70% of capital) -- positive regime companies
Short book: $300,000 (30% of capital, margin-funded) -- negative regime companies
 
Universe:
  Positive regime (long): MSFT, AMZN, CRM, SNOW
  Negative regime (short): DDOG, TWLO, GTLB
 
## Benchmark
 
Equal-weight portfolio of the same seven companies, rebalanced monthly.
Long book: 25% each across four positive regime companies.
Short book: 33.3% each across three negative regime companies.
Same 70/30 capital split as signal portfolio.
 
The benchmark isolates the Ps signal's contribution: any outperformance
vs equal-weight is attributable solely to the Ps signal tilts.
 
## Signal Tilt Logic
 
Each month, the Ps own-history Z-score drives weight adjustments:
 
  HC signal (z >= +1.5): 2.0x equal-weight allocation (maximum tilt)
  Moderate signal (z >= 0.5): 1.2x equal-weight
  Neutral (z >= 0.0): 1.0x equal-weight (no tilt)
  Below average (z < 0.0): 0.8x equal-weight (slight underweight)
 
Weights are renormalised within each book to sum to 1.0 after tilting.
Capital split (70/30) is held fixed each month.
 
For negative regime companies, a high Ps z-score means elevated
engineering activity in a company that fails Condition 7 --
engineering maintains parity but does not compound the moat.
The signal predicts negative returns: higher z = larger short weight.
 
## Rebalancing
 
Monthly, on the 1st of each month, coinciding with the automated
Ps signal run. Positions are sized based on closing prices on
the day of rebalancing.
 
## Pre-commitment
 
Signal z-scores are committed to GitHub with a timestamp before
any positions are recorded. The methodology and tilt logic are
documented here before any performance is observed. This protects
against post-hoc rationalisation.
 
## Performance Tracking
 
portfolio_positions.csv: monthly position records with entry prices,
  signal weights, benchmark weights, notional sizes and share counts.
portfolio_performance.csv: monthly P&L, signal return vs benchmark
  return, cumulative attribution.
 
## Inception
 
May 1 2026. Live track record began with GitHub Actions automated run.
