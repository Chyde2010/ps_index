# PLTR — Palantir — Voluntary Methodology Boundary Case

**Classification:** Voluntary Methodology Boundary Case
**Lock date:** April 2026
**Protocol version:** v1.4

## Finding

Three repositories technically qualified under Protocol v1.4 from 55 screened.
All three represent internal developer tooling with no connection to Palantir's
revenue-generating products.

## Qualifying repos (not selected)

| Repo                          | Phi   | Corp commits |
|-------------------------------|-------|--------------|
| palantir/baseline-error-prone | 0.840 | 631          |
| palantir/gradle-baseline      | 0.835 | 640          |
| palantir/blueprint            | 0.270 | 1158         |

## Rationale

The three qualifying repos are internal Java static analysis tooling, Java build
configuration tooling and a React UI component library. None are connected to
AIP, Foundry, Gotham or Apollo. The most strategically central public repo —
palantir/osdk-ts with 1,690 corp commits — failed N1b with only 31 months active.

## Action

PLTR is included in the cross-sectional summary table with a Methodology
Boundary Case flag alongside NOW. No full pipeline will be run.
