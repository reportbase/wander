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

**Note before the run (10 October 2026, after the plan was committed, before any script).** The plan says the detector
is a small flat patch facing the source, but the line's formula, (1/d)·arctan(b/d), is what a detector counting light from
every direction receives (a small sphere), not a flat patch. The predictions stand as written, on the formulas as
written. The run derives each formula by integration and says which emitter and detector it belongs to. It also reports,
beside P3 and P4, the other detector's version, as information and not as predictions.

## Runs

### Run 1 (10 October 2026)

`python3 plans/nrf/nrf.py` (sympy 1.14, mpmath at 50 digits), output in `plans/nrf/nrf-run1.txt`:

```
Derivations (each from an integral over the source; L or lambda per unit area or length set to 1)
  Lambertian disc, flat patch: pi*a**2/(a**2 + d**2)   plan: True
  isotropic disc, flat patch: -2*pi*d/sqrt(a**2 + d**2) + 2*pi   = 2*pi*(1 - d/sqrt(d^2+a^2)): True
  isotropic disc, every direction (small sphere): log((a**2/d**2 + 1)**pi)
  isotropic line, every direction: 2*atan(1/d)/d   plan form (2/d)*atan(1/d): True
  isotropic line, flat patch: 2/(d*sqrt(d**2 + 1))
  Lambertian sphere from its centre: E = pi*L*(R/d)^2 for d >= R (standard; the sphere subtends sin^2 = (R/d)^2)

P1 Lambertian disc: sigma(s) = -2*s**2/(s**2 + 1)
   sigma(1) = -1.0 (halfway -1.0); sigma(s)+sigma(1/s) symbolic: -2; worst numeric miss from -2: 0.0
   10%-90% from s = 0.333333 to 3.0: width 3.16993 levels
P2 sphere from its centre: sigma = -2 at every d >= R
P2 Lambertian sphere, from its surface (s = gap/R): sigma(s) = -2*s/(s + 1)
   sigma(1) = -1.0 (halfway -1.0); sigma(s)+sigma(1/s) symbolic: -2; worst numeric miss from -2: 0.0
   10%-90% from s = 0.111111 to 9.0: width 6.33985 levels
P3 isotropic line, every direction (plan form): sigma(s) = (-s - (s**2 + 1)*atan(1/s))/((s**2 + 1)*atan(1/s))
   sigma(1) = -1.63661977236758 (halfway -1.5); sigma(s)+sigma(1/s) symbolic: -((s + (s**2 + 1)*atan(1/s))*atan(s) + (s + (s**2 + 1)*atan(s))*atan(1/s))/((s**2 + 1)*atan(1/s)*atan(s)); worst numeric miss from -3: 0.224
   10%-90% from s = 0.145642 to 2.40983: width 4.04843 levels
P4 isotropic disc, flat patch (plan form): sigma(s) = s/((s - sqrt(s**2 + 1))*(s**2 + 1))
   sigma(1) = -1.20710678118655 (halfway -1.0); sigma(s)+sigma(1/s) symbolic: s*(-s*(s - sqrt(s**2 + 1)) + sqrt(s**2 + 1) - 1)/((s - sqrt(s**2 + 1))*(s**2 + 1)*(sqrt(s**2 + 1) - 1)); worst numeric miss from -2: 0.342
   10%-90% from s = 0.173369 to 2.56677: width 3.88804 levels
information (not predictions):
  isotropic line, flat patch: sigma(s) = (-2*s**2 - 1)/(s**2 + 1)
   sigma(1) = -1.5 (halfway -1.5); sigma(s)+sigma(1/s) symbolic: -3; worst numeric miss from -3: 0.0
   10%-90% from s = 0.333333 to 3.0: width 3.16993 levels
  isotropic disc, every direction: sigma(s) = -2/((s**2 + 1)*log((s**2 + 1)/s**2))
   sigma(1) = -1.44269504088896 (halfway -1.0); sigma(s)+sigma(1/s) symbolic: -log((((s**2 + 1)/s**2)**(s**2)*(s**2 + 1))**(2/((s**2 + 1)*log((s**2 + 1)/s**2)*log(s**2 + 1)))); worst numeric miss from -2: 0.787
   10%-90% from s = 0.00673963 to 2.04418: width 8.24463 levels

P1: not killed (disc: sigma(1) = -1 and the flip identity)
P2: not killed (sphere: -2 from the centre; from the surface sigma(1) = -1 and the flip)
P3: KILLED (line: sigma(1) = -1.63661977237, flip miss 0.224)
P4: KILLED (solid-angle disc: sigma(1) = -1.20710678119, flip miss 0.342)
P5: KILLED (widths 3.17, 6.34, 4.048, 3.888 levels)
```

- **The formulas.** Every formula was derived by integration and matches the plan. As the note said, the line's form
  (and the solid-angle disc's, read as an isotropic emitter) belong to particular detectors: the line's arctan form is
  a detector counting light from every direction, and 1 − d/√(d² + a²) is an isotropic emitter seen by a flat patch.
- **P1 not killed.** For the Lambertian disc, σ(s) = −2s²/(1 + s²): σ(1) = −1 exactly, and σ(s) + σ(1/s) = −2 is an
  identity.
- **P2 not killed.**
  - From its centre, a Lambertian sphere falls exactly 2 levels per level of distance, everywhere outside it.
  - From its surface, σ = −2s/(1 + s): halfway at a gap of one radius, and flip-symmetric.
- **P3 killed.** The line, counted from every direction, gives σ(1) = −1.637, not −1.5, and misses the flip identity by
  up to 0.22.
- **P4 killed.** The isotropic disc on a flat patch gives σ(1) = −1.207, and misses the flip by up to 0.34.
- **P5 killed, by the sphere from its surface.** The widths are 3.17 levels for the disc, 6.34 for the sphere from its
  surface, 4.05 for the line and 3.89 for the solid-angle disc. The sphere's switch is twice as wide as the disc's, since
  its σ turns on s, not s².
- **Information (not predictions).**
  - The line on a flat patch: σ = −1 − s²/(1 + s²), halfway at s = 1 exactly, flip-symmetric, width 3.17.
  - The isotropic disc counted from every direction: σ(1) = −1.44, not symmetric, width 8.2.

## Reading (after the run; not ruled)

- **Where the corner holds, it holds exactly, and it is the share of a two-part split.** In every source that passed,
  the slope's way from near to far is a share:
  - the Lambertian disc: s²/(1 + s²);
  - the line on a flat patch: s²/(1 + s²);
  - the sphere from its surface: s/(1 + s).

  These are the forms `plans/near-far-classification.md` calls fair to the facings, f(s) + f(1/s) = 1, there for a
  reading and here for the slope of the light. The disc's share is sin²θ, with θ the half-angle the source subtends, and
  its fairness is Pythagoras.
- **Where it fails, an angle is counted instead of a share.** The line from every direction counts arctan(b/d), the
  angle it subtends. The isotropic emitter on a flat patch counts 1 − cos θ, its solid angle. Their slopes are not shares
  of a split, and their switches are off s = 1: the line's halfway point is at s = 0.719, the solid-angle disc's at
  0.786 (computed after the run). This is the classification's "components are not" fair, in light.
- **What decides it is the radiometry, not the source's shape.** The Lambertian emitter seen by a flat patch counts the
  *projected* solid angle (the cosine on both ends). That is the standard measure of irradiance, and it turns any source
  into a share. A disc and a line pass with it; the same disc and line fail with an angle or an unprojected solid angle.
  So the corner of the pair (size, distance) is exact for the light physics actually measures on a surface.
- **The width is set by the power in the share.** A share in s² switches over log₂ 9 ≈ 3.2 levels (10% to 90%), a share
  in s over twice that. The plan's band of [2, 5] guessed one width for all; there is one width per power, log₂(81)/k
  for a share in s^k.
- **The sphere from its centre has no near field at all.** Outside it, it is a point source of its own radiance times
  its projected area. The near field of a sphere appears only when distance is counted from its surface, and then its
  corner is a gap of one radius: the same corner HZN found reading a ball from its outline (`plans/hzn-plan.md`).
