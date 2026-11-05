# SWP: the shape swept whole, not the thumbs one by one

5 November 2026. Tom, after the three thumbs' hill (R670, R690): "the shape of the 3d cauchy shows why two cauchys combine
into another cauchy. seems like we have the sweep of three thumbs and that geometric structure that is created also sweeps
as a shape."; "the larger point is that this capability means the shape itself can be swept."; "so I think must actually
happen is not the sweep of each thumb individually, the thumbs are swept as part of the cauchy shape."; then "proceed".

The question: in three dimensions, does it matter whether each thumb is swept on its own (each through its own angle,
evenly) or the three thumbs are turned together as one rigid frame (every turn of the frame weighed alike)? And what does
"the shape can be swept" mean exactly? Exact checks (mpmath at 50 digits, sympy) and one seeded sample; nothing from
Wander's world.

**Known beforehand, stated.** AZM (`plans/azm-plan.md`): both angles even gives P(v ≤ h) 0.3426 and the near field 0.2326;
even in azimuth and height gives ½ and ⅓. WDG run 1: the even octant's readings are the 2D Cauchy. THM run 1: the look
down the diagonal, the thumbs at r = √2. EUL and `plane-sphere.html`: two quarter turns in the two orders end 120° apart.
The Poisson kernel's semigroup and the multivariate Cauchy's closure under projective maps (the gnomonic image of the
angular central Gaussian) are classical; a seeded scratch check in this session (2·10⁶ directions, one random 3 × 3 map)
agreed with the latter to three decimals before this plan was written. Haar's uniqueness and Euler's rotation theorem
are classical.

## Setting, with the case kept

Three thumbs, unit vectors square to each other at the eye: e₁ (h), e₂ (v, up), e₃ (v₂). A direction n in the octant
(every n·eᵢ ≥ 0) has readings s = v/h = (n·e₂)/(n·e₁) and s₂ = v₂/h. No amount enters.

- **Each thumb swept on its own** ("pan, then tilt"): the frame turned about the up thumb through the azimuth ψ, then
  tipped through the altitude a, each angle even on [0, 90°] and the two independent:
  n = (cos a cos ψ, sin a, cos a sin ψ).
- **The order the other way** ("tilt, then pan"): n′ = (cos a cos ψ, sin a cos ψ, sin ψ), the same two even angles.
- **The shape swept whole**: the frame turned as one rigid body, every turn alike (the Haar measure on the turns of space);
  the direction it carries home to is uniform on the sphere, and on the octant uniform over its area.

## Predictions (written before the script exists)

- **W1.** Each thumb on its own: P(v₂ ≤ h) = ½ exactly (the azimuth's own pair); P(v ≤ h) = P(v ≤ v₂) =
  (4/π²)∫₀^{π/2} atan(cos ψ) dψ = 0.34258… (AZM's 0.3426); the near field (h the largest) 0.2326. The pair the two sweeps
  share, (v, h) and (v, v₂), is off its corner.
- **W2.** The shape swept whole: every pair ½, the near field ⅓, each of the six chambers ⅙ (exact by the symmetry of the
  frame; a seeded sample of 10⁶ uniform turns, as unit quaternions, within 4 standard errors of each).
- **W3.** The laws in the readings. Each thumb on its own: (4/π²)/(√(1 + s₂²)·(1 + s² + s₂²)) on the quadrant, which is not
  a function of s² + s₂² (at (1, 0) and (0, 1) it differs by √2: the hill is not round). The shape whole:
  (2/π)(1 + s² + s₂²)^(−3/2), round. Both integrate to 1. The sample's share in a few cells of the (s, s₂) quadrant agrees
  with each law within 4 standard errors.
- **W4.** Written in the thumbs' angles, the whole sweep is even in azimuth and even in height (sin a), independent: its
  weight on the altitude is cos a, which comes from the frame turning as one, not from either thumb. Against it, the
  thumb-by-thumb sweep's density per unit of solid angle is (2/π)/cos a times the uniform one: least, 2/π, on the horizon,
  and without bound toward the up thumb, where the azimuth's sweep shrinks to a point. Down the diagonal (the look of R670)
  its density at the crosshair is (2/π)·√(3/2) = 0.7797 of the uniform's, so its hill does not peak at the crosshair.
- **W5.** The order matters for each thumb on its own: tilt-then-pan gives P(v ≤ h) = ½ and P(v₂ ≤ h) = 0.34258…, the pair
  off its corner moving with the order. A quarter turn about e₁ then about e₂, and the same two the other way, are each one
  turn of 120° about one axis (Euler), the two axes different, and the second pose differs from the first by a turn of
  120°. The shape swept whole has no order: its law is the same whatever turns compose it (the Haar measure is unchanged
  by composing with any fixed turn, on either side).
- **W6.** Every pose a thumb-by-thumb sweep reaches is itself one turn of the whole frame (orthogonal, determinant 1, one
  axis and one angle): the two ways reach the same poses and differ only in how the poses are weighed.
- **W7.** Marks carried: for every turn R, (Rn)·(Reᵢ) = n·eᵢ, so every reading in the turned frame is the reading in the
  first; the thumbs land at r = √2 on the screen square to the turned look, the homes at 1/√2, at every turn.
- **W8.** In the plane, one thumb: the even turn is the Haar measure on the plane's turns, turns commute, the pair is at ½;
  the two ways are one.
- **W9.** "The shape can be swept": the readings of the even directions after any linear map M of the thumbs' space (a
  turn, a stretch, a shear, a tilt; a projective map of the screen) are an elliptical 2D Cauchy with location
  b = C₁₀/C₀₀ and scatter (C₁₁ − C₁₀C₀₁/C₀₀)/C₀₀, C = MMᵀ, read on the screen square to the first thumb. A turn
  (M orthogonal) leaves it the round hill. The family's standpoint is five numbers (two of place, three of shape), against
  the plane's two (m + iγ). Checked on three seeded maps: median and half the interquartile range along eight screen
  directions within 4 standard errors.
- **W10.** Stacking two hills: for independent elliptical Cauchys of one shape and scales γ₁, γ₂, the sum is that shape at
  γ₁ + γ₂ (characteristic function e^(−γ√(kᵀΣk))); for two shapes not proportional, the sum is not an elliptical Cauchy (its
  characteristic function is not e^(−√(kᵀΣ′k)) for any Σ′: the Σ′ fitted exactly on three directions k misses a fourth
  by more than 10⁻³).

Kill conditions: an exact identity off by more than 10⁻²⁰ at 50 digits; a sampled share more than 4 standard errors from
its prediction; W5's angles off 120° by more than 10⁻¹².

## Runs

(below this line, as they came out)

### Run 1 (5 Nov 2026; `runs/swp/swp.py`, output `runs/swp/swp-run1.txt`; about 3 minutes)

Nothing killed.

- W1 not killed: each thumb on its own, P(v₂ ≤ h) = ½, P(v ≤ h) = P(v ≤ v₂) = 0.342583477852475, the near field
  0.232631533384301.
- W2 not killed: the shape swept whole (10⁶ seeded unit quaternions), every pair 0.4996–0.5001, the near field 0.33352, a
  chamber 0.16677, all within 0.9 standard errors.
- W3 not killed: both laws integrate to 1 at 50 digits; the thumb-by-thumb law's f(1, 0)/f(0, 1) is √2 to 20 digits, so its
  hill is not round; four cells of the (s, s₂) quadrant agree with each law within 1.5 standard errors.
- W4 not killed: against the even law the thumb-by-thumb density per unit of solid angle is 2/π on the horizon,
  0.779696801234 down the diagonal (2/π·√(3/2)), 450 at sin a = 0.999999. The whole sweep, written in the thumbs' angles, is
  even in height and even in azimuth (ten bins each).
- W5 not killed: tilt-then-pan gives P(v ≤ h) = ½ and P(v₂ ≤ h) = 0.3426, the pair off its corner moved by the order. A
  quarter turn about e₁ then e₂ is one turn of 120° about (1, 1, 1)/√3, the other order 120° about (1, 1, −1)/√3, and the
  two poses differ by a turn of 120°. Composing the uniform turns with a fixed turn on either side keeps the near field and
  the pair at ⅓ and ½.
- W6 not killed: three thumb-by-thumb poses each a turn of the frame (orthogonal and determinant 1 to 10⁻⁵⁰), each one turn
  about one axis (65.09°, 69.59°, 56.13°).
- W7 not killed: readings unmoved by three turns to 10⁻⁵¹; the thumbs at √2 and the homes at 1/√2 on the turned screen.
- W8 not killed: the plane's turns commute.
- W9 not killed: three seeded maps, the readings an elliptical Cauchy with the predicted location and scatter, the worst of
  16 shares a map within 1.7 standard errors. The run's "a turn" line is trivial (a turn of uniform directions is uniform,
  C = I); the line's own parenthesis overstates it.
- W10 not killed: one shape stacks (0.7 + 1.6 = 2.3 exactly); two shapes do not (the Σ′ fitted on three directions misses
  a fourth by 0.0047).

What the math says. Three thumbs swept each through its own angle, evenly and one after the other, reach every pose a turn of
the whole frame reaches (W6), but weigh them otherwise: the directions pile toward the thumb the first sweep turns about,
where the second sweep shrinks to a point (W4); the hill in the readings is not round (W3); one pair leaves its corner
(W1); and which pair, and where the pile goes, depends on the order (W5). The three thumbs turned together, one rigid
frame, every turn alike, give the round hill, every pair at its corner, the near field a third, and no order (W2, W5): any
turns compose to one turn about one axis (Euler), and Haar's measure is the only law unchanged by composing them. Written
per thumb that sweep is even in azimuth and even in height (W4): the weight on the altitude comes from the frame turning as
one, not from either thumb, which is Archimedes' hat-box seen from the turns. Turning the frame carries the thumbs as
marks (W7). In the plane the two ways are one (W8), which is why the difference appears only with the third thumb. Beyond
turns, every linear map of the thumbs' space carries the even read to an elliptical 2D Cauchy (W9): the family the read
belongs to can itself be swept, its standpoint five numbers in space against the plane's m + iγ; stacking two hills gives
one only when they have one shape (W10). Classical throughout (Haar 1933, Euler's rotation theorem, Archimedes, the
multivariate Cauchy's closure); the reading, the three thumbs as marks of one shape swept, is ours.

### A note after run 1 (5 Nov 2026; SPN R696)

Tom: "the sweep is the quarter turn, not the semi-circle, sphere or circle."; "the demo shows what the cauchy would look
like if reader rotated his head 360 degrees." The predictions and the run stand as written. Two things in them are the
writer's, not the read: W2's sample drew uniform turns of the whole sphere and folded them into the octant, and the
reading's appeal to Haar's measure on every turn of space and to Euler's composition of turns. The read is the quarter
turn, the wedge, every pair from home to its horizon; within it the thumbs swept together fill the wedge evenly by area,
and nothing composes past a horizon. `read.html` now draws the wedge alone by default, the round of the look ("turned all
the way round") an option.
