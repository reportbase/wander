# NRF: where an extended source turns from near to far

*Plan, predictions and kills written 10 October 2026, before the script was written or run (Claude; Tom: "before we go
down this rabit hole of looking at pre-existing data. lets make sure we solid with the math and what is going on. the
inverse square law seems logical, first step", then "ok, proceed"). Exact arithmetic, no data. The lab rules hold:
nothing above the "Runs" line is edited after the run.*

## Disclosure

While answering Tom, before this plan, I worked two cases roughly in my head:
- the Lambertian disc's irradiance on its axis is 1/(1 + s²), which puts its halfway point at s = 1;
- the isotropic line's slope at s = 1 looked like about −1.64, not the halfway value −1.5.

So P1 is not blind, and P3 is written against what that rough sum suggested. Each is still checked exactly, and P3 is
written as the theory says, not as the rough sum says.

## The claim

The inverse square is exact only for a point source. A source of size a, at distance d, has a near field and a far
field. Near, the light hardly falls with distance; far, it falls 2 levels per level of distance. The reading is s = d/a,
a ratio. In levels, the local slope is

σ(s) = d log₂ E / d log₂ d.

σ runs from its near value to −2.

SPN's claim, carried over:
- **(a)** the switch from near to far is at the corner of the named pair (the source's size, the distance), s = 1, where
  σ is halfway between its near and far values;
- **(b)** the switch is symmetric under the flip s ↔ 1/s about that corner: σ(s) + σ(1/s) = σ_near + σ_far.

## Keep the case

d and a are amounts, and the bridge is the source's size a. s = d/a is a pure number. "The corner" here is the corner of
the pair (a, d), named as such. It is a point set by an amount, so in the terms of `CLAUDE.md` it is the resolution limit
of the source's own size, read as a corner of that pair. Nothing here is a fill level of the reader.

## The sources

Each is uniform, in empty space, with no absorption. The detector is a small flat patch facing the source, on its axis of
symmetry.

1. **Lambertian disc**, radius a, on its axis at distance d: E ∝ a²/(a² + d²). Near value 0, far −2.
2. **Lambertian sphere**, radius R:
   - from its centre, at distance d ≥ R: E ∝ (R/d)²;
   - from its surface, at gap x = d − R, with s = x/R.

   Near value (in s) 0, far −2.
3. **Isotropic line**, length 2b, perpendicular distance d from its middle, s = d/b: E ∝ (1/d)·arctan(b/d). Near value
   −1 (an infinite line falls as 1/d), far −2.
4. **Isotropic-intensity disc** (each patch radiating equally in all directions, the detector counting light from every
   direction, i.e. the solid angle's share): E ∝ 1 − d/√(d² + a²). Near value 0, far −2.

## Predictions

- **P1 (the disc).** σ(1) = −1 exactly, and σ(s) + σ(1/s) = −2 exactly for every s > 0. *Killed* if either fails as an
  identity (checked symbolically).
- **P2 (the sphere).**
  - From its centre, σ = −2 exactly at every d ≥ R: a sphere has no near field outside itself. This is a known result,
    stated as a check of the arithmetic.
  - From its surface, σ(1) = −1 and σ(s) + σ(1/s) = −2 exactly.

  *Killed* if any of these fails.
- **P3 (the line).** σ(1) = −1.5, and σ(s) + σ(1/s) = −3, both within 10⁻¹². *Killed* if either misses.
- **P4 (the solid angle's disc).** σ(1) = −1, and σ(s) + σ(1/s) = −2, both within 10⁻¹². *Killed* if either misses.
- **P5 (the width of the switch).** For the Lambertian disc, σ goes from 10% to 90% of its way from near to far over
  log₂ 9 ≈ 3.17 levels of s (s = 1/3 to 3). For each of the other sources the same width is between 2 and 5 levels.
  *Killed* if any source's width falls outside [2, 5].

## What would not be shown

- Anything about the inverse square itself. Physics has it from conservation and three dimensions, and has tested its
  exponent to within about 10⁻¹⁶ of 2 (`papers/physics.md`, "How physics holds the inverse square").
- Whether a reader's own corner sits at s = 1 for any source. Each corner here is the source's: the pair (size,
  distance).

## Runs

