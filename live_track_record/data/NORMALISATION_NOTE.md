# Normalisation Lookup -- Maintenance Note

## Status: Static reference file

The normalisation_lookup.csv contains ps_raw mean and std
for each ticker, used by monthly_signal.py to compute
own-history z-scores.

## Existing six tickers (MSFT AMZN CRM SNOW DDOG TWLO)
Derived from 87-month backfill using monthly_signal.py
formula (90-day rolling window). Stable and reliable.

## Three new tickers (BABA GTLB MNDY)
Derived from backfill run July 2026 using monthly_signal.py
formula from each company's start date:
  BABA: 2019-01 to 2026-06 (90 months)
  GTLB: 2021-10 to 2026-06 (57 months)
  MNDY: 2021-06 to 2026-06 (61 months)

## Update schedule
This file does NOT auto-update. Manual update recommended
every 6-12 months by re-running the backfill script:
  /mnt/user-data/outputs/monthly_signal_backfill.py

Next recommended update: January 2027.
