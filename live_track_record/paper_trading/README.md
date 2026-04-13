# Ps Index Paper Trading

## Model specification (pre-committed May 1 2026)

### Portfolio
- Size: GBP 1,000,000 notional
- Benchmark: QQQ (Nasdaq-100 ETF)
- Performance horizon: 6 months per position

### Long book (positive signal regime)
Companies: MSFT, AMZN, CRM, SNOW
- Neutral weight: 25% per company
- Tilt factor: 5pp per 1 sigma Ps Z-score
- Maximum weight: 45% per position
- Minimum weight: 5% per position
- Weights normalised to sum to 100%

### Short overlay (negative signal regime)
Companies: DDOG, TWLO
- Short weight: 3% per 1 sigma Ps Z-score
- Maximum short: 10% per position
- Only short when Z-score > 0
- Funded by reducing long book allocation

### Entry
- Monthly on the 1st of each month
- Entry price: closing price on day of run
- FX: USD converted to GBP at prevailing GBPUSD rate

### Exit
- 6 months after entry (rolling monthly positions)
- Alpha measured vs QQQ return over same period

## Files
- open_positions.csv: currently open positions
- settled_positions.csv: closed positions with returns
- performance_summary.csv: cumulative performance by month
