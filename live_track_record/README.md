# Ps Index -- Live Track Record

## Started: May 1 2026

## Signal companies
| Ticker | Signal regime | Condition |
|--------|--------------|-----------|
| MSFT   | Positive     | Sticky platform |
| AMZN   | Positive     | Sticky platform |
| CRM    | Positive     | Sticky platform |
| SNOW   | Positive     | Sticky platform |
| DDOG   | Negative     | Competitive API |
| TWLO   | Negative     | Competitive API |

## Methodology
Ps Index computed on the first of each month using the
protocol defined in the SSRN working paper. Z-scores
committed before forward returns are observable.

## Files
- data/: Pre-processed historical merged files per company
- signals/live_signals.csv: Monthly live Ps Z-score readings
- signals/: Monthly signal snapshots (one file per month)
