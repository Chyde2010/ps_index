# Ps Index Paper Trading

## Model specification (pre-committed May 1 2026)

### Portfolio
- Size: GBP 1,000,000 notional at inception
- Benchmark: QQQ (Nasdaq-100 ETF)
- Rebalancing: monthly on the 1st of each month
- Performance: tracked as continuous NAV vs benchmark

### Long book (positive signal regime)
Companies: MSFT, AMZN, CRM, SNOW
- Neutral weight: 25% per company at zero signal
- Tilt factor: 5 percentage points per 1 sigma Ps Z-score
- Maximum weight per position: 45%
- Minimum weight per position: 5%
- Weights normalised to sum to 100% of long allocation

### Short overlay (negative signal regime)
Companies: DDOG, TWLO
- Short weight: 3% of portfolio per 1 sigma Ps Z-score
- Maximum short per position: 10%
- Only short when Z-score is positive
- Funded by reducing long book proportionally

### Entry and exit
- No fixed holding period -- positions rebalance monthly
- Signal changes immediately reflected in weights
- Entry and exit prices are closing prices on the 1st

### FX
- All positions in USD, converted to GBP at prevailing rate
- GBPUSD fetched from Yahoo Finance at time of run

## Files
- monthly_nav.csv: portfolio NAV vs QQQ each month
- monthly_weights.csv: target weights and positions each month

## Key metrics reported
- Portfolio NAV (GBP)
- P&L vs inception (GBP and %)
- Alpha vs QQQ (inception to date and month on month)
- Month-on-month portfolio and benchmark return
- Rebalancing trades vs prior month
