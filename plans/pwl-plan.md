# PWL: where pipelines hit walls

13 November 2026. Tom: "engineered solutions of the blueprint have danced around these ideas, but they use trig and need
both hemisphers, so those engineerd solutions always hit a wall.", then "yes" to Claude's offer of a test. Claude's view
going in, said to Tom: the walls are real (precision far from the origin, turns drifting, depth precision) but they come
from number formats, not from trigonometry or the two hemispheres, and engineers mostly get past them with classical
fixes; what got `thumbs-walk.html` past them was exact arithmetic, the eye's place a write paid by the digit.

The question: does a standard first-person pipeline, with its classical fixes switched on, still hit a wall that
`thumbs-walk.html`'s pipeline does not, and is that wall due to trigonometry or the two hemispheres?

## Set-up (a script, `runs/pwl/pwl.mjs`, node; no page)

Three axes, four pipelines:

- **plain32**: world coordinates and the eye stored in float32 about a fixed origin, turns by sin/cos in float32, the
  frame composed by multiplying matrices.
- **plain64**: the same in float64.
- **fixed**: the classical fixes. A floating origin over a sector grid (sector index a 64-bit integer, sector 1,024 units,
  a float64 offset inside it), the frame re-squared (Gram–Schmidt) after every turn, or the heading kept as an integer
  angle (binary angle units, 2³² a turn), depth in reversed-Z float32 (n/d, far plane at infinity).
- **ours**: `thumbs-walk.html`'s, re-implemented: exact fractions for every place (BigInt), the look held as whole
  numbers (q quarter turns, half-slope ky/128, the eighth-turn crossing by tangent subtraction rounded), order of depth by
  exact comparison.

**A. Distance from the origin.** A box 10 units ahead of the eye (corners at offsets up to (3, 1, 10)), the eye at
X·(1, 0, 1) for X = 10^k, k = 0 to 100 in quarter steps; a screen 1,280 px wide, focal length 1,000 px. The error is each
corner's screen position against the exact one. A pipeline **breaks** at the first X where the error passes 0.5 px.

**B. Turns composed.** 10⁶ seeded steps, each a yaw of ±1 to ±12 half-slope units (k/128), then the same steps undone in
reverse order. Measured: how far the frame is from square (max |RᵀR − I|) after the steps out, and how far the frame is
from where it started after the way back (max |R − I|).

**C. Depth told apart.** Two things at d and d·(1 + r), d = 10^j, j = 0 to 9, near plane 0.1, far plane 10¹⁰ where a
format needs one. The finest r (r = 10^−m, m in quarter steps to 16) a format still orders correctly: the standard 24-bit
buffer, log depth in 24 bits, reversed-Z float32, ours.

## Predictions (committed before the script is written)

- **A1.** plain32 breaks between X = 2·10⁴ and 4·10⁵ (from ulp(X)·foc/d = 0.5 px, X ≈ 8·10⁴, within a factor of 4 each
  way). plain64 breaks between 10¹³ and 2·10¹⁴ (X ≈ 4.5·10¹³). *Killed* if either breaks outside its band.
- **A2.** fixed does not break up to the sector index's 64-bit limit (X ≈ 9.4·10²¹), and breaks past it (the index
  wraps). *Killed* if it breaks before or holds past.
- **A3.** ours does not break at any X tested (to 10¹⁰⁰); the eye's place takes more digits as X grows (at least as many
  as X has). *Killed* if it breaks, or the digits do not grow.
- **B1.** After 10⁶ steps out, plain32's frame is off square by more than 10⁻⁴, plain64's by more than 10⁻¹³ and under
  10⁻⁹. *Killed* otherwise.
- **B2.** With re-squaring, the frame stays square to within 10⁻⁶ (float32) but does not come back exactly after the way
  back (|R − I| > 0). With the integer heading, the way back is exact. *Killed* if re-squaring leaves it unsquare, or the
  integer heading does not come back exactly.
- **B3.** ours: the way back is exact when no step crosses an eighth of a turn; with crossings, at least one of 100 seeded
  walks does not come back exactly (the rounding at the crossing). *Killed* if every crossing walk comes back exactly, or a
  walk without crossings does not.
- **C1.** The standard 24-bit buffer cannot order r = 1% past d ≈ 1.7·10⁴ (within a factor of 4); reversed-Z float32
  orders r ≈ 10⁻⁶·⁵ ± 0.5 decades at every d; log depth 24-bit orders about the same r at every d (within a decade of
  10⁻⁵·⁵); ours orders every r tested at every d. *Killed* otherwise.
- **W (the question).** Every wall the fixed pipeline still hits within these ranges is a choice of number width (the 64-bit
  sector index, float32 depth's finite steps, the heading's 2³² units), none due to trigonometry or the two hemispheres;
  ours passes each by holding more digits, never by holding fewer readings. *Killed* if a fixed-pipeline wall is found that
  widening its numbers does not remove.

What this test cannot show: that exact arithmetic is ours. A classical pipeline can use BigInt too; the test measures
where each pipeline as built breaks, not whose idea it is.
