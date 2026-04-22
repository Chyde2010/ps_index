# Universe Extension Test
## Date: April 2026

## Objective
Test whether the original paper methodology
(cross-sectional normalisation of raw Ps values,
pooled OLS, no regime classification) holds when
applied to a broader universe of 17 companies
beyond the original paper's 10-company cohort.

## Original paper result
beta=0.004042, p=0.048, n=866
Cohort: AAPL, ADBE, AMZN, GOOGL, META,
        MSFT, NET, NVDA, PLTR, SNOW

## Extended universe (17 companies)
Positive signal : MSFT, AMZN, CRM, SNOW
Negative signal : DDOG, TWLO, GTLB
No signal       : GOOGL, META, MDB, ESTC,
                  AMD, DT, PATH, FSLY, AAPL
Insufficient    : NET

## Key question
Does the original finding generalise?
See universe_extension_regression.csv for results.

## Known limitation
The 17-company universe includes companies with
very different repository scales. GOOGL and AAPL
have ps_raw values 10-20x larger than TWLO and CRM.
Cross-sectional normalisation of raw Ps values
across this heterogeneous universe may be dominated
by scale rather than signal. This is itself an
important finding -- the original methodology
requires a homogeneous cohort or a scale correction
to generalise beyond comparable-sized companies.
