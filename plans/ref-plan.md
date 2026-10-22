# REF: the corner as the reference sphere

*Plan, predictions and kills written 10 October 2026, before the script was written or run, and before the relief
settings in `res/make-bodies.mjs` were read (Claude; Tom: "proceed with #4", the fourth correspondence offered at
`levels.html`: geodesy measures a world's heights against a reference surface; wander's bodies are a ball plus relief).
The lab rules hold: nothing above the "Runs" line is edited after the run.*

## The claim

SPN §1 ("The corner is the circle, and depth is measured from it"): a shape's depth is its difference from the corner's
circle once its size is divided out, counted in levels, log₂ s. On a body in three dimensions the corner is a sphere.
Geodesy does the same thing with amounts: heights above a reference surface, a sphere or an ellipsoid of a world's own
size. The claim is that the two are one operation, and that it sorts bodies as the eye does: a world reads as its corner
to within a sliver of a level, and a rock does not.

## Keep the case

A body's radius in a direction is an amount. Its ratio to the geometric mean radius, r/r̄, is a ratio: depth in levels,
log₂(r/r̄), is geometry, the same for a pebble and a planet of the same form. The bridge back to heights in metres is the
size, r̄. Wander's files hold their own units (the body's height is 1). The published figures below are amounts in km,
used only through their ratios.

## The model

**Wander's bodies** (`res/*.tvf3d`). Each file holds the radius ρ(θ, h) from the body's axis at height h ∈ [0, 1], in
units of the body's height. It is a series in cos(nπh) and cos/sin(mθ). The point on the surface is at axial height
z = h − ½, so its distance from the centre is R(θ, h) = √(ρ² + z²). Weight every (θ, h) alike: on a sphere, area is
uniform in z (Archimedes). Then:
- the **corner sphere** is the geometric mean R̄;
- the **depth** in a direction is log₂(R/R̄);
- the **depth range** is the most minus the least.

The **bands** split the relief as the flying page's shaders do, by the finest wave in a term, max(n, m): broad under 10,
middle 10 to 23, fine 24 and up. A band's share is the variance of the depth when only that band's terms are kept on the
ball (m = 0 ball terms removed as `fieldGrid` removes them).

**Published worlds** (the NASA planetary fact sheet's equatorial and polar radii; relief extremes from standard
references). These are given only as ratios, so only their levels matter.

## Predictions

- **P1 (the corner is the ball).** For every body in `res/`, the geometric mean distance R̄ is within 1% of ½ (the ball
  the files are built on, which the flying page draws when a body is far off). *Killed* if any body's R̄ misses ½ by more
  than 1%.
- **P2 (worlds are their corner; rocks are not).** The depth range is under 0.1 levels for every sun, planet and moon in
  `res/`, and over 0.3 levels for both asteroids. *Killed* if any body is on the wrong side of its threshold.
- **P3 (broad first).** For every body, the broad band holds more of the depth's variance than the middle, and the middle
  more than the fine. This is the order in which the shaders add the bands as a body comes near. *Killed* if any body's
  order differs.
- **P4 (real worlds, by their published radii).** From equatorial and polar radii alone, the flattening in levels is
  log₂(a/c):
  - Earth (6378.1 / 6356.8 km) about 0.0048;
  - Mars (3396.2 / 3376.2) about 0.0085;
  - the Moon (1738.1 / 1736.0) about 0.0017;
  - Jupiter (71492 / 66854) about 0.097;
  - Saturn (60268 / 54364) about 0.149.

  So the rocky worlds sit within a hundredth of a level of their corner by shape, and the fast-spinning giants a tenth or
  more. *Killed* if any computed value misses the one given here by more than 0.0005 levels (an arithmetic check of this
  plan), or if any rocky world reaches 0.01 levels.
- **P5 (relief on Earth).** From Challenger Deep (−10.9 km) to Everest (+8.8 km) about a mean radius of 6371 km, Earth's
  relief spans about 0.0045 levels. With its flattening, the whole Earth lies within 0.01 levels of its corner. *Killed*
  if the computed span exceeds 0.006 levels, or the two together reach 0.01.

## What would not be shown

- That geodesy needs levels: it works in metres, and levels add nothing to its numbers. The claim is only that measuring
  heights against a world's own reference sphere is the same operation as SPN's depth from the corner.
- Anything about why worlds are round. P4 and P5 only say how near round they are, in levels. That spin flattens the
  giants is known physics, quoted, not derived.

## Runs

### Run 1 (10 October 2026)

`node plans/ref/ref.mjs res`, output in `plans/ref/ref-run1.txt` (✗ marks a body on the wrong side of a prediction):

```
asteroid-dark   R̄ 0.49351 (-1.30%) ✗  range 0.4917 levels  bands 85.6% / 13.6% / 0.7%
asteroid-grey   R̄ 0.49782 (-0.44%)  range 0.4371 levels  bands 81.6% / 17.2% / 1.2%
moon-callisto   R̄ 0.49968 (-0.06%)  range 0.0733 levels  bands 19.1% / 63.9% / 17.0% ✗
moon-ice        R̄ 0.50010 (0.02%)  range 0.0107 levels  bands 26.4% / 52.1% / 21.5% ✗
moon-io         R̄ 0.50086 (0.17%)  range 0.0504 levels  bands 88.3% / 10.9% / 0.8%
moon-luna       R̄ 0.49859 (-0.28%)  range 0.2478 levels ✗  bands 48.9% / 46.4% / 4.7%
moon-rust       R̄ 0.49947 (-0.11%)  range 0.1688 levels ✗  bands 36.7% / 58.2% / 5.1% ✗
planet-alien    R̄ 0.50144 (0.29%)  range 0.0325 levels  bands 86.9% / 12.1% / 1.0%
planet-jupiter  R̄ 0.50002 (0.00%)  range 0.0020 levels  bands 42.0% / 53.5% / 4.5% ✗
planet-lava     R̄ 0.49832 (-0.34%)  range 0.0444 levels  bands 47.4% / 43.3% / 9.3%
planet-mars     R̄ 0.49939 (-0.12%)  range 0.1354 levels ✗  bands 36.9% / 55.9% / 7.2% ✗
planet-neptune  R̄ 0.50001 (0.00%)  range 0.0023 levels  bands 25.7% / 67.6% / 6.7% ✗
planet-ocean    R̄ 0.50001 (0.00%)  range 0.0002 levels  bands 97.5% / 2.3% / 0.2%
planet-saturn   R̄ 0.50001 (0.00%)  range 0.0013 levels  bands 49.6% / 49.4% / 0.9%
planet-terra    R̄ 0.50271 (0.54%)  range 0.0424 levels  bands 91.2% / 7.9% / 0.9%
planet-uranus   R̄ 0.50001 (0.00%)  range 0.0009 levels  bands 83.4% / 16.6% / 0.0%
planet-venus    R̄ 0.50001 (0.00%)  range 0.0031 levels  bands 32.6% / 65.3% / 2.1% ✗
sun-blue        R̄ 0.50001 (0.00%)  range 0.0010 levels  bands 38.1% / 57.0% / 4.8% ✗
sun-orange      R̄ 0.50001 (0.00%)  range 0.0138 levels  bands 21.7% / 58.4% / 19.9% ✗
sun-red         R̄ 0.50001 (0.00%)  range 0.0069 levels  bands 42.7% / 55.0% / 2.3% ✗
sun-white       R̄ 0.50001 (0.00%)  range 0.0002 levels  bands 98.1% / 1.8% / 0.1%
sun-yellow      R̄ 0.49993 (-0.01%)  range 0.0160 levels  bands 30.9% / 58.0% / 11.0% ✗
P1: KILLED. every corner sphere within 1% of the ball, 1/2
P2: KILLED. suns, planets, moons under 0.1 levels; asteroids over 0.3
P3: KILLED. broad > middle > fine in every body
P4: not killed. flattening in levels, log2(a/c): Earth 0.00483, Mars 0.00852, Moon 0.00174, Jupiter 0.09677, Saturn 0.14874
P5: not killed. Earth's relief 0.00446 levels; with its flattening 0.00929
```

- **P1 killed, by one body.** Every corner sphere is within 1% of the ball except the dark asteroid's (−1.3%). A lumpy
  rock's geometric mean is not its ball; every world's is, within 0.6%.
- **P2 killed, by three bodies.** Wander's Moon spans 0.248 levels, its rust moon 0.169 and its Mars 0.135. The other
  suns, planets and moons are under 0.1, most of them under 0.05. Both asteroids are over 0.3, as predicted.
- **P3 killed, by twelve bodies.** In most of the cratered bodies and in several smooth ones (Jupiter, Neptune, Venus,
  three suns), the middle band holds more of the depth than the broad. Broad first holds for the asteroids, Io, the alien
  planet, the ocean planet, Terra, Uranus and the white sun.
- **P4 and P5 not killed.** By their published radii, the rocky worlds' flattening is under a hundredth of a level and
  the giants' about a tenth (Jupiter 0.097, Saturn 0.149). Earth's relief, from Challenger Deep to Everest, spans 0.0045
  levels; with its flattening, the whole Earth is within 0.0093 levels of its corner.

## Reading (after the run; not ruled)

- **The physics side holds.** Measuring heights against a world's own reference sphere is the same operation as depth
  from the corner, in amounts rather than levels. Read so:
  - a real rocky world is its corner to within about a hundredth of a level;
  - a spinning giant is its corner to within about a tenth;
  - the real Moon's relief (+10.8 to −9.1 km about 1737 km) spans 0.0165 levels.
- **Wander's bodies are rougher than real ones.** Wander's Moon (0.248 levels) is about fifteen times the real Moon's
  span, and wander's Mars (0.135) about seven times the real Mars's (about 0.018 with its relief). They were made to look
  good close up (`res/`, "looks only"), not to scale. If the world is to correspond, their relief is the thing to scale.
  That is a change to `res/make-bodies.mjs`, for Tom to decide. The run changes nothing.
- **"Broad first" is the order of seeing, not of the relief.** The shaders add the broad band first because its features
  are the largest, so they cover a few pixels first. That order holds whatever share of the relief each band holds, and
  in most of wander's bodies the craters (the middle band) hold most of it. P3 confused the two orders. The kill stands.

### Run 2: real relief by octave (predictions written 14 October, before any data was downloaded)

*Tom, 15:49 (SPN R249), after Claude judged the games page's Levels application an illustration, not a proof: "whats new
is the tvf3d signal. it shows how the signal itself is packed." Then "ok", 15:53, to a plan testing it on real bodies.
Written before the files below were downloaded or the script written; the run is recorded below this section.*

**The claim.** A .tvf3d body is a series; ordered by the finest wave a term holds, its terms are the payload's own
levels, coarse first, and level of detail is how many of them are summed. The two sides meet at sampling:
- *The reader's side (geometry, exact).* A body of radius R spanning a addresses across its disc holds the degrees up
  to about l_max = πa/2 (two addresses a wave at the disc's middle, where an address covers 2R/a of surface and degree
  l's wave is 2πR/l). Past the corner a halves with each level of distance, so each level drops one octave of degrees,
  [2^k, 2^(k+1)); inside the corner the octaves held do not change. Nothing to test: it follows from the lay.
- *The payload's side (physics).* How much relief each octave carries is the world's, not the geometry's. The question
  Tom's remark raises is whether real worlds come packed the way the reader reads: with no preferred level (each level
  of distance dropping the same share of the relief), and in the one packing under which the reader sees the same thing
  at every level (each octave's relief in proportion to its wavelength, half the relief of the octave before).
  The first is the premise that gives the reader its logarithm, no rung preferred ((S)), carried from the reader's lay
  to the world's payload; the geometry does not require it. The second is the reader's lay matched to the world.

**Keep the case.** Relief is an amount (metres). Its RMS per octave enters only through ratios: the change in log₂ RMS
from one octave to the next (levels of relief per level of degree) is unitless, the same in metres or in radii, and
needs no bridge. For information only, an octave's relief in the reader's own addresses at the level where it is the
finest held, ρ_k = RMS_k·2^(k+1)/(πR), uses R, a body's mean radius, as the bridge.

**Data (fixed before download).** Seven rocky bodies, the published spherical-harmonic models of their physical
surfaces, as pyshtools lists them (SHTOOLS `pyshtools/datasets`, commit 98c15ef, with the sha256 each download must
match):
- Mars: Wieczorek 2024, MOLA shape, Zenodo 10.5281/zenodo.10820719, `Mars_MOLA_shape_1439.bshc.gz` (sha256 f12bcd82…).
- Moon: Wieczorek 2024, LOLA shape, 10.5281/zenodo.10820774, `Moon_LOLA_shape_1439.bshc.gz` (f5e8f1b7…).
- Mercury: USGS SPG shape, 10.5281/zenodo.10809345, `Mercury_shape_1439.sh.gz` (48d5ee57…; bshc inside).
- Venus: Wieczorek 2015, VenusTopo719, 10.5281/zenodo.3870926, `VenusTopo719.shape.gz` (9fcb04fb…).
- Earth: Hirt and Rexer 2015, Earth2014 physical surface (water and ice included: what reaches a reader), degree 2160,
  ddfe.curtin.edu.au, `Earth2014.SUR2014.degree2160.bshc` (5694260d…). Heights above mean sea level, not radii.
- Vesta: DLR SPG shape (Dawn), 10.5281/zenodo.10820681, `Vesta_DLR_SPG_shape_1439.bshc.gz` (99eae345…).
- Ceres: DLR SPG shape (Dawn), 10.5281/zenodo.10820608, `Ceres_DLR_SPG_shape_1439.bshc.gz` (ae3e9918…).

The 1439 files are the first degrees of each archive's full model (5759 or 5399), not a smoothing of it.

**Method (fixed before download).** Coefficients 4π-normalized (the archives' convention; checked against each file's
documentation before the run, converted if not). Degree power S_l = Σ_m (C_lm² + S_lm²), so the relief's variance over
the sphere is Σ_{l≥1} S_l. Octave k holds degrees 2^k ≤ l < 2^(k+1); its RMS relief is √(Σ S_l) over the octave.
Octaves k = 3 to 9 (degrees 8 to 1023; Venus k = 3 to 8, its model ending at 719). The lowest degrees are left out:
degree 1 is the offset of the centre of figure, 2 the spin's flattening (REF P4), and degrees under 8 a handful of
features each (Tharsis and the dichotomy, South Pole–Aitken, Rheasilvia). Per body, the least-squares line of
log₂ RMS_k against k, equal weights; its slope is the levels of relief per level of degree. Earth's relief is above the
geoid and the others' radii include theirs; at degree 8 and up the geoid's share is small, and this is noted, not
corrected.

**What I knew beforehand (from memory, not checked before writing).** Planetary topography is usually described as
roughly a power law in degree; Earth's profiles as near Brownian (power ∝ wavenumber⁻², Hurst ≈ ½; Vening Meinesz
1951, Bell 1975, Turcotte 1987), which is a slope of about −½ here; the terrestrial planets' spectra in Wieczorek
(2015) roughly parallel. I do not recall the others' slopes or breaks. So P7 is expected to be killed if memory serves;
P6 and P8 I cannot call.

**Predictions.**
- **P6 (no preferred level).** On every body, each octave's log₂ RMS lies within 0.25 of the body's fitted line, over
  k = 3 to 9 (Venus 3 to 8): each level of distance drops the same share of the relief. *Killed* if any octave on any
  body departs from its body's line by more than 0.25 (a factor 1.19 in relief).
- **P7 (the reader's lay matched).** On every body, the slope is −1 within ±0.15: each octave half the relief of the
  one before (degree power ∝ l⁻³), relief in proportion to wavelength, so the reader sees the same relief in its own
  addresses at every level. *Killed* if any body's slope lies outside [−1.15, −0.85].
- **P8 (the packing is geometric, not the world's).** A unitless number fixed by the geometry would be the same on
  every body (SPN R231: unitless values are fixed by the geometry or read from the world). *Killed* if the seven slopes
  do not all lie within ±0.1 of their mean.

For information, not predicted: each octave's share of the relief, ρ_k, and Earth's bedrock (Earth2014 BED2014, the
same archive) beside its surface.

**What would not be shown.** Anything about the reader's side, which is exact. Why a world's relief has the spectrum it
has (impacts, volcanism, erosion, isostasy are physics, quoted, not derived). And seven bodies are seven: a kill of P8
says the packing is read from the world, not that no reader could find a common one.

### Run 2 (14 October 2026)

`python3 -I plans/ref/ref2.py <data>`, two seconds; the full output, octave by octave, in `plans/ref/ref-run2.txt`.
All eight files matched the sha256 above on download (Earth2014's bedrock: 146dcc80…). The archives' own
documentation says 4π-normalized, Condon–Shortley phase excluded, metres (Zenodo records; Earth2014's readme, V1.1),
so nothing was converted. The data is CC BY 4.0 (the Zenodo archives) and Curtin's Earth2014 (cite Hirt and Rexer
2015); none of it is committed. Before the run the script was checked on synthetic spectra of known slope (−1.5 to 0):
it recovered each within 0.02.

```
Mercury: R 2439.5 km (model to degree 1439), relief RMS over degrees 1-1023 1092 m; slope -0.280 levels of relief per octave (degree power ~ l^-1.56)
Venus: R 6051.9 km (model to degree 719), relief RMS over degrees 1-511 958 m; slope -0.337 levels of relief per octave (degree power ~ l^-1.67)
Earth: R 6371.0 km (model to degree 2160), relief RMS over degrees 1-1023 634 m; slope -0.438 levels of relief per octave (degree power ~ l^-1.88)
Moon: R 1737.2 km (model to degree 1439), relief RMS over degrees 1-1023 2329 m; slope -0.208 levels of relief per octave (degree power ~ l^-1.42)
Mars: R 3389.5 km (model to degree 1439), relief RMS over degrees 1-1023 6688 m; slope -0.424 levels of relief per octave (degree power ~ l^-1.85)
Vesta: R 260.4 km (model to degree 1439), relief RMS over degrees 1-1023 18018 m; slope -0.982 levels of relief per octave (degree power ~ l^-2.96)
Ceres: R 469.5 km (model to degree 1439), relief RMS over degrees 1-1023 11143 m; slope -0.686 levels of relief per octave (degree power ~ l^-2.37)
Earth bedrock: R 6371.0 km (model to degree 2160), relief RMS over degrees 1-1023 2417 m; slope -0.426 levels of relief per octave (degree power ~ l^-1.85)
P6: KILLED. largest departure from a body's line 0.566 levels (Vesta, k = 9); threshold 0.25. Over 0.25: Mercury k=6 (+0.296), Mercury k=7 (+0.362), Mercury k=9 (-0.454), Moon k=3 (-0.274), Moon k=6 (+0.455), Moon k=7 (+0.389), Moon k=9 (-0.488), Vesta k=3 (-0.390), Vesta k=6 (+0.399), Vesta k=7 (+0.385), Vesta k=9 (-0.566), Ceres k=3 (-0.522), Ceres k=5 (+0.324), Ceres k=6 (+0.305), Ceres k=7 (+0.259), Ceres k=9 (-0.488)
P7: KILLED. slopes Mercury -0.280, Venus -0.337, Earth -0.438, Moon -0.208, Mars -0.424, Vesta -0.982, Ceres -0.686; outside [-1.15, -0.85]: Mercury, Venus, Earth, Moon, Mars, Ceres
P8: KILLED. mean slope -0.479, largest departure 0.503 (threshold 0.1)
```

All three killed.

- **P6 killed, by the four airless bodies.** Earth (largest departure 0.11), Mars (0.11) and Venus (0.25, at its edge)
  hold a straight line over their six or seven octaves. Mercury, the Moon, Vesta and Ceres do not: on each the middle
  octaves (degrees 64 to 255) stand 0.26 to 0.46 above the line and degrees 512 to 1023 fall 0.45 to 0.57 below it.
- **P7 killed, by six bodies.** The slopes run from −0.21 (the Moon) to −0.69 (Ceres); only Vesta's (−0.98) is in the
  band, and Vesta's spectrum is curved (P6), so its line is an average over a bend. Relief per octave falls more slowly
  than wavelength on every other body: the finer a band, the steeper its slopes.
- **P8 killed.** The seven slopes spread 0.50 about their mean (−0.48). The share a level drops is not one number.

**Reading (after the run; not ruled).**
- *The packing is the reader's; the share is the world's.* Every model here is a series by degree, and the reader
  drops one octave of it per level of distance, as the claim says. But how much relief each octave carries is read
  from the world (SPN R231: unitless, found, not derived): it differs from body to body, and on the airless bodies from
  level to level.
- *What the local slopes show* (log₂ of each octave's RMS over the one before, computed after the run from the table):
  Earth −0.24 to −0.57, Mars −0.30 to −0.60, Venus −0.05 to −0.58, each averaging about −0.4; Earth's bedrock the same
  as its surface (−0.43 against −0.44; the oceans lower the relief, 634 m against 2,417 m, not its slope). The Moon
  −0.11, +0.06, +0.15, −0.27, −0.60, −0.69 and Mercury −0.12, −0.39, +0.15, −0.21, −0.51, −0.87: relief per octave
  flat or rising to about degree 128, then falling ever faster. Vesta (−0.67 to −1.63) and Ceres (−0.09 to −1.22)
  steepen throughout. Earth's −0.44 is near the Brownian −½ recalled beforehand.
- *A preferred level on the airless bodies.* On all four, degrees 64 to 255 (wavelengths of about a tenth to a fortieth
  of the radius) stand above the body's line, from Vesta (260 km) to Mercury (2,440 km): the same octaves in the body's
  own size, not the same size in kilometres. On the Moon and Mercury the relief per octave itself rises there; on Vesta
  and Ceres it only falls more slowly there than further out (a bend, not a peak). That is the large craters and basins,
  and it would be a statement in unit relations, the crater's breadth against the body's. Post hoc, from four bodies: a
  prediction for a new run, not a result.
- *Relief far under the reader's grain.* At the level where a band is first held, its relief is 0.0002 to 0.07 of
  one of the reader's addresses (ρ, every body, every octave): dropping a band by distance moves the outline by far
  less than an address, so level of detail by octave is safe for the outline of every world here. On Earth, Mars,
  Venus, Mercury and the Moon ρ grows by 1.1 to 2.2 a level: coming nearer, each new level shows more relief in the
  reader's own addresses, not the same; seen in shading, a real world grows rougher as the reader approaches.
- *For the pictures.* The bands of wander's and the games page's bodies halve per octave (slope −1, chosen); real
  worlds keep more of their relief in the fine octaves (about −0.4). Scaling `res/` is still Tom's call (run 1).

**Correction (Tom, 16:26; SPN R250): "no, real signals are not packed tvf3d. tvf3d is like a pre-read signal."** Run 2's
claim read Tom's remark as saying the payload brings levels of its own, and asked whether real worlds come packed the
way the reader reads. That was not what was said. A real signal arrives unpacked. A .tvf3d is a signal already read:
the reader's levels with the payload placed in them, coarse first, so a later reader at any distance takes the levels
it holds there and reads nothing again. The packing is the reader's, done once and ahead of time. The predictions and
their kills stand as written: P6–P8 tested a claim nobody made. The measurement is kept for what it is. The published
models are themselves pre-read signals (each a modeller's reading of altimetry or images into degrees), and the run
shows how real relief fills such levels: not in equal shares, not in self-similar ones, and not alike from body to
body. (Claude's reading, unruled: a pre-read signal holds a whole approach at once, each prefix of the series what a
reader holds at one distance; SPN §3.3's levels existing whole, a thing's level set by its size.)

### Re-read, 22 October (RFR, `plans/rfr-plan.md`; SPN R439)
Appended; nothing above is changed. The "corner" sphere is exp(a₀), the mean of the log-radii, not a median (on a
spheroid the median sphere, at latitude 30°, lies about L/12 above it). The depth log₂(r/r̄) is a reading of shape; r̄ in
km and heights are writings. "l_max = πa/2 … inside the corner the octaves held do not change. Nothing to test" and run
2's "one octave of degree per level of distance (exact)" are angular: exact only at the point under the reader, per level
of altitude (l* = πR/(aε), doubling to the surface, no corner at a = R); per level of distance 1.10 octaves at a = R and
14.6 at 10⁻³R. ρ_k (0.0002–0.07) is the world's relief over wavelength, 2·RMS_k/λ_k, the same at every K. The sha256s
above are recorded to 8 hex digits only, too few to verify a fresh download.

### Checksums in full (22 October)
Appended; nothing above is changed. Each file downloaded afresh (22 October) and hashed; every one under 40 MB, so no
published checksum was used in place of a download. The Zenodo URLs are the records' versions as pyshtools lists them
(SHTOOLS `pyshtools/datasets`, commit 98c15ef); its registry's sha256 agrees with each download below, and each
Zenodo file's md5 agrees with the record's API. Earth2014 is V1.1 from Curtin (no published checksum there).
- Mars, Zenodo 10.5281/zenodo.10820719 (version 1.0.1),
  https://zenodo.org/records/10820719/files/Mars_MOLA_shape_1439.bshc.gz
  sha256 f12bcd824dcd2118bc2fb540d37985299735f6f57070ee775fc2487b97a5857c (prefix f12bcd82 matches)
- Moon, Zenodo 10.5281/zenodo.10820774 (version 1.0.1),
  https://zenodo.org/records/10820774/files/Moon_LOLA_shape_1439.bshc.gz
  sha256 f5e8f1b7acaab626db5828f9dc6f9ea1ce948bb5000e5bfcf1ff69b3141f1845 (prefix f5e8f1b7 matches)
- Mercury, Zenodo 10.5281/zenodo.10809345 (no version given),
  https://zenodo.org/records/10809345/files/Mercury_shape_1439.sh.gz
  sha256 48d5ee575b5ffe97fd84b1c1dd2a0c1be0b59d476f52df23373bfd9810d59288 (prefix 48d5ee57 matches)
- Venus, Zenodo 10.5281/zenodo.3870926 (no version given),
  https://zenodo.org/records/3870926/files/VenusTopo719.shape.gz
  sha256 9fcb04fb21eb7090df68e42458f6d7495a27ff62687b46534057ed608786cf3b (prefix 9fcb04fb matches)
- Earth (surface), Curtin,
  https://ddfe.curtin.edu.au/models/Earth2014/data_5min/shcs_to2160/Earth2014.SUR2014.degree2160.bshc
  sha256 5694260d135c17427270ed18d48af23f4788e5fbc1dfb9dcb19f1cf9b401c9ce (prefix 5694260d matches)
- Vesta, Zenodo 10.5281/zenodo.10820681 (version 1.0.2),
  https://zenodo.org/records/10820681/files/Vesta_DLR_SPG_shape_1439.bshc.gz
  sha256 99eae34532e93a4611be51436de7e3e9be8c3f64a799bc43444013ecf73ca6d3 (prefix 99eae345 matches)
- Ceres, Zenodo 10.5281/zenodo.10820608 (version 1.0.1),
  https://zenodo.org/records/10820608/files/Ceres_DLR_SPG_shape_1439.bshc.gz
  sha256 ae3e99187ccfae9c986772f4d0f9e932d51ea292f9d60214589468aae12d8f8e (prefix ae3e9918 matches)
- For information, Earth's bedrock, Curtin,
  https://ddfe.curtin.edu.au/models/Earth2014/data_5min/shcs_to2160/Earth2014.BED2014.degree2160.bshc
  sha256 146dcc80f17d201352d391aa90f487f5ed16006a6a3966add2d023b998727af7 (prefix 146dcc80 matches)
