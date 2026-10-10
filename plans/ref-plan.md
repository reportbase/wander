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

