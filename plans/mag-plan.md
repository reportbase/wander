# MAG: two levels of light per level of distance, on real stars

*Plan, predictions and kills written 10 October 2026, before the data was opened for anything but its column names
(Claude; Tom: "we should do the correct physics testing, UI is secondary or even not needed", then "yes, proceed" to
testing ISQ's correspondence on the Hipparcos stars). The lab rules hold: nothing above the "Runs" line is edited after
the run.*

## The claim

ISQ (`plans/isq-plan.md`) found that the in-place lay has the inverse square's form. Read s as d/Δ, the lay places a
thing at its angular size, and light's inverse square is that angular size squared. In levels, then, a thing of one kind
loses exactly two levels of light for each level of distance: each doubling of distance quarters its light. Here that is
tested on real stars, measured, not drawn.

## Keep the case

- **The amounts.** A star's distance d (parsecs, from its parallax: geometry in the sky, measured) and its flux F (from
  its apparent magnitude m) are amounts.
- **The levels.** Distance in levels is log₂(d/d₀), and light in levels is log₂(F/F₀) = −(log₂ 10 / 2.5)·m + const, about
  −1.3288 m. Both are ratios, so the zero points d₀ and F₀ drop out of every slope. Five magnitudes are exactly 6.644
  levels of light; this is a conversion, not a prediction.
- **The bridge.** "Of one kind" stands in for an equal luminosity L, an amount the reader does not have. Here it is
  supplied by the spectral type, read from each star's spectrum and independent of its distance. This is Part II's "a
  known kind".

## The data

The HYG database, v3.8 (`hyg/v3/hyg_v38.csv.gz` in github.com/astronexus/HYG-Database, CC BY-SA 2.5, sha256
`9e914eb4544c1d8f4a87e1184bbc5322de1a7d1b9cb3110e870d15bc01c91f9d`). It republishes the Hipparcos catalogue: distance
from the Hipparcos parallax (van Leeuwen 2007 reduction), V magnitude, and spectral type.
- **Used:** `hip` (the star is a Hipparcos star), `dist`, `mag`, `spect`.
- **Never used:** `absmag` and `lum`. They are derived with the inverse square, so using them would be circular.
- **Dropped:** stars with no distance (dist ≥ 100000) and stars flagged variable (`var` non-empty).

The astronomy archives (VizieR, CDS, ESA) were blocked by this environment's network policy. GitHub was reachable, so
HYG's republication is the source. The data is not committed to the repository: the script downloads it and checks the
sha256.

**Kinds** (by spectral type, parsed from `spect`):
- *K0 giants:* `spect` begins "K0III" or "K0 III", and not "K0IV" or "K0III-IV".
- *G dwarfs:* `spect` begins with G0 to G5 followed by "V" (not "IV").

## Predictions

- **P1 (the giants, where the catalogue is complete).** For K0 giants at 20 ≤ d ≤ 140 pc, the least-squares slope of light
  in levels against distance in levels is −2 within 0.15. 140 pc is where the faintest K0 giants (absolute V about +1.5)
  reach V = 7.3, Hipparcos's completeness limit, so no K0 giant is missing for being faint. *Killed* if the slope is
  outside [−2.15, −1.85], or fewer than 100 stars qualify.
- **P2 (the dwarfs, a second kind).** For G0–G5 dwarfs at d ≤ 23 pc (complete for absolute V to about +5.5), the slope is
  −2 within 0.3. *Killed* if outside [−2.3, −1.7], or fewer than 20 stars qualify.
- **P3 (past the limit, a control).** For K0 giants out to 400 pc, past completeness, the slope is flatter than −1.8:
  only the brighter of the kind are catalogued far off (Malmquist's bias). It is the catalogue's own resolution limit,
  in light. *Killed* if the slope is −1.8 or steeper.
- **P4 (the scatter is the kind's spread).** About P1's fit, the root-mean-square residual of light, in levels, is
  between 0.3 and 1.0: the K0 giants' spread in luminosity, roughly ±0.4 magnitude, is about 0.5 levels. *Killed* if
  outside [0.3, 1.0].

## What would not be shown

- That the inverse-square law holds. Physics has long known it; the slope here only checks that real data read in
  levels say what ISQ's reading says. The test is of the reading and its bookkeeping, not of the law.
- Anything about which inverse square the lay "is". ISQ's reading (one dimension against two) is not tested here.

## Runs

