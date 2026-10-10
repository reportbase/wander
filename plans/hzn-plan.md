# HZN: standing on the outline is standing on a planet

*Plan, predictions and kills written 10 October 2026, before the script was written or run (Claude; Tom: "proceed. whats
next?", after ISQ; the fifth correspondence offered at `levels.html`, "standing on the outline is standing on a planet").
The lab rules hold: nothing above the "Runs" line is edited after the run.*

## The claim

`levels.html` in draw reads a shape from a place on its outline: in each direction, the distance to the nearest wall.
On a circle, that is a reader standing on a round world. Two things a reader on a planet meets should come out of the
geometry alone, in ratios to the radius (no amounts):
- the horizon, which lies in the directions along the tangent, at home;
- the horizon's distance as the reader rises, the classical √(2·R·height).

## Keep the case

Everything here is in ratios of the circle's own radius. The height is e (a share of the radius) and the distances are
in radii: geometry. The bridge to a planet is one amount, its radius R. A height is then e·R, a distance t·R, and the
formula √(2·R·height) is t·R with t = √(2e). Nothing below needs R, so nothing below is physics until R is given.

## The model

A circle of radius 1. A standpoint at distance 1 + e from its centre: on the outline when e = 0, above it when e > 0.
- **On the outline (e = 0).** A direction makes an angle φ with the tangent, 0 < φ < π, turning inward. The nearest wall
  in that direction is the chord, 2·sin φ. The directions outward meet nothing.
- **Above it (e > 0).** The horizon is the tangent from the standpoint, at distance t(e) = √((1 + e)² − 1) = √(2e + e²).
- **The reader's corner.** As on the levels page, the reader divides out the size: the geometric mean of its readings.
  Its corner is where a reading equals that mean.

## Predictions

- **P1 (home is the horizon).** On the outline the chord, 2·sin φ, goes to 0 along the tangent. So the horizon is at home,
  and reading toward it is proportion: the log-log slope of the chord against φ tends to 1 as φ → 0. Each halving of the
  angle is one level further in. *Killed* if the slope over φ in [2^−20, 2^−10] misses 1 by more than 1e−6.
- **P2 (the corner is the radius, at 30°).** The geometric mean of the chords over the inward half-turn is exactly the
  radius, since ∫₀^π ln(2 sin φ) dφ = 0. So the reader's corner is a chord equal to the radius, at φ = 30° (and 150°)
  from the tangent. The deepest reading, the diameter straight down, is exactly one level past the corner (2 = 2¹), and
  the horizon is infinitely many levels within it. *Killed* if the numerical geometric mean misses 1 by more than 1e−6
  at 10⁶ directions, or the corner's angle misses 30° by more than 0.01°.
- **P3 (the ball, by solid angle).** On a sphere, from a point on its surface, weight each inward direction by its solid
  angle (cos φ dφ, φ the depression below the tangent plane, from 0 to π/2). The geometric mean of the chords 2·sin φ is
  then exactly 2/e ≈ 0.7358 of the radius, not the radius, since ∫₀^{π/2} cos φ · ln(2 sin φ) dφ = ln 2 − 1. So in three
  dimensions the corner falls at a chord of 2/e. *Killed* if the numerical mean misses 2/e by more than 1e−6.
- **P4 (rising, half a level per doubling).** Above the outline the horizon's distance is t(e) = √(2e + e²). For small e it
  is √(2e), so the horizon moves out half a level per doubling of the height (log-log slope ½). This is the classical
  horizon distance √(2·R·h) once a radius R is given. *Killed* if t(e)/√(2e) misses 1 by more than e (its leading
  correction is e/4), or the slope over e in [2^−30, 2^−20] misses ½ by more than 1e−6.
- **P5 (the levels page agrees).** Draw's `gallery/levels.html` LEVELS module, reading a 512-leaf circle from a place on
  its outline, gives readings within 1e−3 of 2·sin φ, meets a wall in half the directions (within 1%), and gives a
  geometric mean within 1e−3 of the radius. *Killed* if any is outside its band. (Run in Node with that page's LEVELS
  code and the shared tvf.js, or, if that cannot be done without a browser, in the browser through `levelsCheck`'s
  helpers.)

## What would not be shown

- Anything about a real planet's horizon beyond the classical formula, which is old. The new part, if it holds, is that
  the reader's own corner on a round world is the radius (in two dimensions) or 2/e of it (in three), with no amounts
  in it.
- Whether a reader on a planet uses a geometric mean. That is the levels page's rule for dividing out the size, a choice
  this lab inherits.

## Runs

### Run 1 (10 October 2026)

`python3 plans/hzn/hzn.py` and `node plans/hzn/hzn-p5.mjs <draw>/gallery/levels.html`, output in
`plans/hzn/hzn-run1.txt`:

```
P1: not killed. log-log slope of the chord against phi, phi in [2^-20, 2^-10]: 0.999999977
P2: not killed. geometric mean of the chords 1.000000693 of the radius; the corner at 30.00002 deg from the tangent; the diameter 0.999999 levels past it
P3: not killed. geometric mean on the ball 0.735759283 of the radius; 2/e = 0.735758882; its depression 21.5849 deg
P4: not killed. max of |t/sqrt(2e) - 1| - e over e = 2^-1 .. 2^-30: -6.985e-10 (<= 0 holds); log-log slope over [2^-30, 2^-20]: 0.500000034
P5: KILLED. draw's LEVELS on a 512-leaf circle from its outline: readings within 1.02e-3 of 2 sin(phi); walls met in 49.88% of directions; geometric mean 1.014247 of the radius
```

- **P1 to P4 not killed.** The geometry holds as predicted:
  - the horizon is at home;
  - the corner is the radius, at 30° from the tangent, with the diameter one level past it;
  - on the ball the corner is 2/e of the radius;
  - rising, the horizon moves half a level per doubling of the height.
- **P5 killed.** Draw's levels page reads the circle's geometric mean 1.4% high. Its readings miss 2·sin φ by 1.02e−3,
  just past the band. It stays killed.
- **The cause, a reading after the run.** The page presents the circle as a 1,024-sided polygon and skips the segment
  the reader stands on. So in the directions within about one segment of the tangent, the nearest wall it finds is the
  next segment along, roughly a segment's length away, where the true chord goes to 0. Near home every reading is held
  up at about one segment: a grain. The geometric mean, which weighs the smallest readings most, comes out high. This is
  the resolution limit again: the page cannot read nearer home than one of its own segments.

### Run 2 (10 October 2026): prediction, written before it ran

If the cause above is right, the error belongs to the presentation's grain, not to the reading:
- **P5b.** With the circle presented at P = 1024, 2048, 4096 and 8192 points (the same page code, 512 leaves), the
  geometric mean's excess over the radius falls by a factor of 2 (between 1.5 and 2.5) per doubling of P.
- **P5c.** The worst miss against 2·sin φ, over directions more than four segments from the tangent, stays under 1e−4 at
  every P.

*Killed* if any doubling's factor is outside [1.5, 2.5], or P5c's miss reaches 1e−4 at any P.
