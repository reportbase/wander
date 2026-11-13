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

## Runs

### Run 1 (13 November 2026; `runs/pwl/pwl.mjs`, output `runs/pwl/pwl-out.json`)

**A. Distance.** plain32 first breaks at X = 10^7.25 (1.8·10⁷), plain64 at 10^16; fixed and ours never break up to 10¹⁰⁰
(error 0 px throughout); ours' place takes k + 1 digits at 10^k.
- **A1 killed by my set-up.** Every coordinate in my scene was a whole number, and whole numbers are exact in float32 up to
  2²⁴ (1.7·10⁷) and in float64 up to 2⁵³ (9·10¹⁵): the breaks fall just past those, not where my ulp formula put them
  (a whole number does not round until the spacing passes 1).
- **A2 killed.** fixed did not break past the 64-bit index's limit: an index that wraps wraps the eye's and the thing's
  alike, so their difference, all that is drawn, stays right. Post hoc, what the wrap costs is identity, not drawing: the
  stored place cannot tell X from X + 2⁶⁴ sectors (my "alias" column, true by construction at every X), so a world made from
  its cells repeats every 2⁶⁴ sectors. A choice of width.
- **A3 not killed.**

**B. Turns.** After 10⁶ steps out:

| pipeline | off square, out | off the start, back |
|---|---|---|
| plain32 | 7.0·10⁻³ | 7.0·10⁻³ |
| plain64 | 2.0·10⁻¹¹ | 2.0·10⁻¹¹ |
| fixed32, re-squared | 3.4·10⁻⁸ | 2.6·10⁻⁵ |
| fixed64, re-squared | 0 | 6.2·10⁻¹⁴ |
| fixed, integer heading | (no matrix) | exactly back |

ours: of 100 walks of 10⁴ steps, every one crossed an eighth of a turn, and **7 came back exactly, 93 did not**; of 100
short walks that never crossed, all 100 came back exactly.
- **B1, B2, B3 not killed.**
- Post hoc, against my own pipeline: the page's turning is not exact on the way back. Its tangent subtraction at the
  eighth-turn crossing rounds to the nearest k/128, so crossing out and back can land a step off. The classical integer
  heading came back exactly every time. Here the classical fix does better than the page.

**C. Depth.** The finest r ordered, as log₁₀ r, d = 10⁰ … 10⁹:

| format | d = 1 | 10 | 10² | 10³ | 10⁴ | 10⁵ | 10⁶ | 10⁷ | 10⁸ | 10⁹ |
|---|---|---|---|---|---|---|---|---|---|---|
| standard 24-bit | −6 | −5.25 | −4.25 | −3.75 | −2.75 | −1.75 | −0.75 | none | none | none |
| log depth 24-bit | −6.5 | −5.75 | −6 | −7 | −5.75 | −6.25 | −5.75 | −6 | −6.25 | −5.75 |
| reversed-Z float32 | −7.5 | −7 | −7.75 | −7 | −7 | −7 | −7.5 | −7.25 | −7 | −7.5 |

The standard buffer last orders 1% at d = 10^4.25 (1.8·10⁴). ours orders every r > 0 at every d (exact comparison).
- **C1 killed** in two clauses: reversed-Z float32 is finer than I said (10⁻⁷ to 10⁻⁷·⁷⁵, my band −6.5 ± 0.5; float32's
  24-bit significand is 6·10⁻⁸, which I should have used), and log depth reached −7 once (d = 10³), outside my decade about
  −5.5. The standard buffer's 1% limit was where I said.

**W not killed.** Every wall the fixed pipeline hit is a choice of width or format: the index's 64 bits (identity, not
drawing), float32's re-squaring drift (6·10⁻¹⁴ in float64, gone with an integer heading), the depth formats' finite steps.
None came from trigonometry or the two hemispheres. And the page's own pipeline has a wall the classical integer heading does
not: its rounding at the eighth-turn crossing.

### Run 2 (planned; the same script with `FRAC=1`)

A1 again with the scene's offsets not whole (corners at x ∈ {1.3, 3.7}, y ∈ {0, 1}, z ∈ {8.1, 10.3}), so rounding begins at
once. **A1′.** plain32 breaks between 2·10⁴ and 4·10⁵, plain64 between 10¹³ and 2·10¹⁴ (as A1). fixed and ours still do
not break to 10¹⁰⁰. *Killed* if any falls outside.

### Run 2 (13 November 2026; `FRAC=1 node runs/pwl/pwl.mjs`, output `runs/pwl/pwl-out2.json`)

plain32 first breaks at X = 10^5.25 (1.8·10⁵; 0.42 px at 10⁵, 1.67 px at 10^5.5); plain64 at 10^14 (0.10 px at 10¹³,
0.74 px at 10¹⁴); fixed holds to 10¹⁰⁰ (6·10⁻¹² px at most); ours holds to 10¹⁰⁰ (1.4·10⁻¹⁴ px, the last division's
rounding). **A1′ not killed.**

**In short.** The plain pipelines hit the walls the formats predict (float32 near 10⁵ units out, float64 near 10¹⁴, turns
drifting, the standard depth buffer losing 1% past 2·10⁴). With the classical fixes on, none of those walls remained within
these ranges except as choices of width: a 64-bit sector index makes the world's identity repeat every 2⁶⁴ sectors, float
re-squaring leaves a drift that float64 makes 10⁻¹⁴ and an integer heading removes, depth formats have finite steps.
Nothing found was due to trigonometry or the two hemispheres. `thumbs-walk.html`'s pipeline passed each wall by holding
more digits (the eye's place k + 1 digits at 10^k), and has one wall the classical integer heading does not: its rounding
at the eighth-turn crossing, which left 93 of 100 long walks a step off on the way back.

### Run 3 (13 November 2026; R944; output `runs/pwl/pwl-out3.json`)

The page's turning changed (TWK run 12): the heading one whole number N of half-slope steps, no rounding. Its copy in
`walkOurs2`: 100 of 100 walks of 10⁴ turns back exactly, all crossing a half turn (the old rule 7 of 100). The integer
heading (binary angle units) also returns exactly, and does it by looking up sine and cosine in a table; the page's frame is
made from the half-slope's rational point ((1 − t²)/(1 + t²), 2t/(1 + t²)), with no table and no trigonometric call. On
this comparison the wall the page had is gone, and the two return alike.
