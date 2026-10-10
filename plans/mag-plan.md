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

### Run 1 (10 October 2026)

`python3 plans/mag/mag.py` (data checked against the sha256 above), output in `plans/mag/mag-run1.txt`:

```
103016 Hipparcos stars with a distance and no variable flag; 5 magnitudes = 6.6439 levels of light
P1: not killed. K0 giants, 20-140 pc: n = 533, slope -1.927 light levels per distance level, over 2.72 levels of distance
P2: not killed. G0-G5 dwarfs within 23 pc: n = 83, slope -2.021, over 4.11 levels of distance, rms 0.639 levels
P3: not killed. K0 giants out to 400 pc: n = 2983, slope -1.607
P4: KILLED. rms residual about P1's fit: 1.413 levels of light (1.064 mag)
```

- **P1 not killed.** The 533 K0 giants between 20 and 140 pc lose 1.927 levels of light per level of distance, over 2.7
  levels of distance.
- **P2 not killed.** The 83 G0–G5 dwarfs within 23 pc lose 2.021 levels of light per level of distance, over 4.1 levels.
- **P3 not killed.** Out to 400 pc, past the catalogue's completeness, the K0 giants' slope flattens to −1.607: only the
  brighter of them are catalogued far off.
- **P4 killed.** The giants' scatter about P1's fit is 1.41 levels of light (1.06 magnitudes), past the band's 1.0. The
  plan took the kind's spread to be about ±0.4 magnitude. The spectral class K0 III is broader than that: it holds clump
  giants and giants still climbing the branch, and spectral classification has its own errors of a subclass or a
  luminosity class. The kill stands.

## Reading (after the run; not ruled)

- **On real stars, light falls two levels per level of distance.** The dwarfs give 2.02, and the giants, where complete,
  1.93. Both are measured from geometric distances and spectra. This is the inverse square, read in levels, as ISQ's
  reading said: the light of a thing of one kind is its angular size squared, two levels per level.
- **The giants sit a little flatter than 2.** It is within the band. It is also the direction a 1-magnitude spread pushes
  even inside the completeness limit: near that limit the faintest giants start to drop out. So the dwarfs, nearer and
  narrower in kind, are the cleaner reading of the two.
- **Past the limit, the catalogue reads only the bright: 1.61.** In light, this is the resolution limit of SPN and
  `ladder.html`. A reader with a faint limit does not lose a kind all at once; it keeps only the brightest of the kind,
  and the law looks flatter than it is.
- **The kind's spread is the bridge's error.** "Of one kind" stands in for one luminosity, and K0 III is a loose kind,
  ±1 magnitude, which is ±1.3 levels. Every distance read from such a kind by light alone carries that error. The
  luminosity class in the spectrum is the known-kind bridge of Part II, and here it is measured to be about a level wide.

### Note after CNT runs 2 and 3 (10 October 2026)

P1's range, 20 to 140 pc, was taken as complete for K0 giants. CNT runs 2 and 3 (`plans/cnt-plan.md`) found that it is
not: 19% of the stars labelled K0 III within 140 pc are fainter than V = 7.3, and about one in ten at any distance is
too faint to be a giant. P1's 1.927 was measured on that mixed, incomplete sample. It stays not killed, as recorded, but
the cleaner reading of the two is P2's dwarfs, 2.021.
