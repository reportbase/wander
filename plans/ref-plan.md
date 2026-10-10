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
