# Batch 3 Universe Expansion -- Pre-Registration
## Ticker: ADSK (Autodesk Inc.)
## Exchange: NASDAQ
## Date: May 2026
## Pre-committed before any pipeline execution

---

## Methodology Note

Formula: Ps = V x phi x (1 - H)
- V   = 90-day rolling corporate commit count
- phi = structural commit density (churn floor 100 lines)
- (1-H) = entropy gap

Corporate email domain: autodesk.com
  Email format: firstname.lastname@autodesk.com (confirmed)
  Western email convention. San Francisco headquarters.
  Engineering team dominant in USD repos is Montreal-based.
  No multi-domain complexity.

Commercial bar: factor-adjusted 6M p<0.05, retention >70%,
beta POSITIVE (positive regime prediction).

---

## CRITICAL STRUCTURAL CAVEAT

Observable engineering is M&E segment only (~25-30% of revenue).
Autodesk has 19,000 private repos on GitHub Enterprise.
Only 85 repos are public -- open-source ecosystem connectors.
Strategic engineering for AutoCAD, Revit, Fusion 360,
Civil 3D and Inventor is entirely private.

The "Waiter" internal tool mirrors open-source repos to GHE.
All 5,000 Autodesk engineers work on GitHub Enterprise.

The pipeline will measure M&E USD engineering intensity
and regress it against ADSK total stock returns, which are
driven by the full business (AEC + Manufacturing + M&E).

This segment mismatch is the primary risk factor.
Medium confidence (not high) reflects this limitation.

---

## Candidate -- Autodesk Inc. (ADSK)

### Predicted signal: POSITIVE (medium confidence)

Confidence qualifier: Observable signal is M&E segment only.
Revenue segment mismatch may attenuate the signal.
Medium confidence reflects this structural caveat.

### Seven-condition assessment

C1 -- Consumption or usage-based revenue: PASS
  Autodesk completed its SaaS transition in 2021.
  All products are now subscription-only. Revenue scales
  with seat count and usage. AutoCAD, Revit, Fusion 360,
  Maya all on annual or monthly subscriptions. Clear pass.

C2 -- Embedded platform, high switching costs: PASS
  Deepest switching costs in design software. An architecture
  firm with a decade of Revit BIM workflows cannot switch
  without migrating every project file, family library and
  custom workflow. The .DWG and .RVT file format dependencies
  are themselves moats. A manufacturing company running
  Fusion 360 with custom CAM toolpaths faces similar lock-in.
  Exceptionally clear pass.

C3 -- Frictionless consumption uplift: PASS
  Architecture firms add seats as they grow. Manufacturers
  add CAM licences as they add machines. Autodesk Construction
  Cloud generates more data with every project, driving upsell
  into analytics. Clear pass.

C4 -- Near-term revenue realisation: PASS
  Annual subscription fees recognised over contract term.
  Clear pass.

C5 -- Product revenue primacy: PASS
  Pure software platform. No hardware. Professional services
  minimal and declining as percentage. Clear pass.

C6 -- Open-source observability: PASS (M&E segment only)
  Domain diagnostic (May 2026):
    bifrost-usd        : 93.8% corp n=64  STRONG
    arnold-usd         : 58.0% corp n=100 STRONG
    maya-usd           : 56.0% corp n=100 STRONG
    maya-hydra         : 27.0% corp n=100 MODERATE
    MachineControlFW   :  6.0% corp n=100 WEAK (excluded)

  FPP pre-screen (May 2026): 3/4 repos pass FPP >= 0.05
    PASS bifrost-usd   FPP=0.333 n=60 -- exceptional
    FAIL arnold-usd    FPP=0.040 n=100 -- maintenance dominated
    PASS maya-usd      FPP=0.100 n=100 -- solid
    PASS maya-hydra    FPP=0.151 n=93  -- solid

  bifrost-usd FPP=0.333 is the highest single-repo FPP
  in the entire Ps Index study across all companies tested.
  Bifrost is actively being built out -- structural engineering
  phase rather than maintenance phase.

  Corporate email pattern: firstname.lastname@autodesk.com
  Montreal engineering team confirmed across all repos:
    bifrost-usd: yves.boucher, guillaume.laforge
    arnold-usd : sebastien.blaineau.ortega
    maya-usd   : julien.deboise, anton.khelou,
                 ashley.handscomb.retallack
    maya-hydra : anais.lanthier, pierre.tremblay

  CRITICAL CAVEAT: Observable engineering is M&E only.
  AEC and Manufacturing (majority of ADSK revenue) is
  entirely private in 19,000 GitHub Enterprise repos.

C7 -- Engineering investment compounds the moat: PASS
  M&E USD moat compounds at multiple levels:

  1. USD integration depth. Autodesk's USD integrations for
     Maya, Arnold and Bifrost are foundational to the M&E
     pipeline. Every studio (ILM, Illumination Paris, Pixar,
     Disney) that builds their pipeline on Autodesk USD
     integrations increases switching costs. The depth of
     the USD schema coverage compounds with every release.

  2. Bifrost structural investment. FPP=0.333 confirms
     Bifrost is in active structural build-out phase.
     Every new Bifrost graph node, compound and USD schema
     expands the procedural VFX capability gap versus
     competitors (SideFX Houdini is the primary threat).
     Houdini cannot replicate Bifrost's Maya integration.

  3. File format moat. The .DWG format lock-in for AutoCAD
     and .RVT for Revit are not engineered on GitHub but
     compound independently. The observable USD engineering
     adds a third moat layer in M&E interoperability.

  CAVEAT: C7 argument is strongest for M&E segment.
  AEC moat (Revit/Civil 3D) and Manufacturing moat
  (Fusion 360/Inventor) are not observable and assumed
  to compound based on industry knowledge only.

### Study period
NASDAQ listed: 1985. SaaS transition completed 2021.
Study period: January 2018 to March 2026 (98 months).
Start date reflects when USD integration engineering
began appearing publicly (maya-usd first commits ~2018).

### Repos (pipeline -- 3 repos passing pre-screen)
- Autodesk/bifrost-usd  FPP=0.333 n=60  (anchor)
- Autodesk/maya-usd     FPP=0.100 n=100
- Autodesk/maya-hydra   FPP=0.151 n=93

arnold-usd EXCLUDED: FPP=0.040, below threshold.
Maintenance-dominated -- compatibility patches for new
USD versions rather than structural capability additions.

### Sector control
QQQ (Invesco NASDAQ 100) -- primary.
Autodesk is NASDAQ-listed. QQQ appropriate.
SPY as market control.

### Risk factors
1. Revenue segment mismatch (primary risk):
   Observable signal is M&E only (~25-30% of revenue).
   AEC and Manufacturing are private. Pipeline regresses
   M&E engineering intensity against total ADSK returns.
   Signal may attenuate or be absent if AEC/Manufacturing
   engineering drives stock returns more than M&E.

2. USD ecosystem dependency:
   maya-usd and maya-hydra include community contributions
   from ILM and other studios. Corporate rate 56-27%
   means signal includes some non-Autodesk engineering.
   Less clean than BABA or MSFT universe companies.

3. SaaS transition creates a structural break:
   Pre-2021 ADSK was perpetual licence. Post-2021 is SaaS.
   Regression across this break may show heteroscedasticity.
   Study period starts 2018 which includes both regimes.

4. bifrost-usd thin volume:
   Only 60 corporate commits across the study period.
   Monthly Ps signal will be sparse in early periods.

### Confidence level
MEDIUM. Three repos pass FPP pre-screen with strong scores.
bifrost-usd FPP=0.333 is exceptional. But revenue segment
mismatch is a genuine structural limitation that prevents
high confidence classification.

---

## Context

ADSK is the third NASDAQ 100 company assessed after TEAM
and INTU. TEAM showed regime-dependent signal. INTU failed
C6 (community handover). ADSK passes C6 via M&E segment
USD integration repos. This is the first NASDAQ 100 company
besides TEAM to reach the pipeline stage.

---

## Summary

| Ticker | Company   | Predicted | Confidence | Batch |
|--------|-----------|-----------|------------|-------|
| ADSK   | Autodesk  | Positive  | Medium     | 3     |

---

## Pre-commitment statement

The above prediction and condition assessment was committed
to GitHub before any ADSK pipeline was executed.

Signed: Charlotte Hyde
Date: May 2026
GitHub: Chyde2010/ps_index
