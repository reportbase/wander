# PXC: parallax from the corner

*13 October 2026. Tom: "show how parallax and situated observation are both needed. explore parallax from the perspective
of the corner." Exact arithmetic and the complex step, with one Monte Carlo check of the first-order error. Predictions
written before the script (`pxc/pxc.py`) exists. It builds on SPN Proposition 9.6 (parallax as two situated directions
and the reader's own travel), MOT P6–P7 (`plans/mot-plan.md`: a baseline reads distance best at d = B/2, alike at d and
(B/2)²/d; sin γ = 2k/(1 + k²)) and COR's "parallax against the grain" (SPN §3, gives out at a shift of one address).*

## Set-up, with the case kept

**Amounts:** a baseline B between two standpoints (the reader's own travel, or two readers a known distance apart), a
target's distance d from the baseline's middle, the angular step ε (a share of a turn in radians, the reader's grain).

**The pair and its reading.** The pair is (half-baseline, distance), its reading k = (B/2)/d, an amount ratio, named. Its
corner is k = 1: d = B/2. On the perpendicular bisector the baseline subtends the parallax angle γ with tan(γ/2) = k, so
the corner is γ = 90°, and every point where the baseline subtends a right angle lies on the circle with the baseline as
its diameter (Thales). That circle is parallax's corner; inside it the near field (γ > 90°), outside the far field.

**Why both are needed.** One standpoint reads directions only: by OFS Proposition 8(a) scaling the world leaves every
reading unchanged, so it holds the figure's directions and order of turn but no distance. Parallax is the difference of
two such readings (the right side of SPN Proposition 9.6 is addresses alone) with one amount, B, as the bridge. Neither
alone gives distances: without the readings there is nothing to difference, and without B nothing fixes the scale.

## Predictions

- **P1. Parallax's precision is the parallel reader's bell, centred on the corner.** On the bisector, the relative error
  in distance per unit error in γ is |d ln d/dγ| = 1/sin γ = cosh(ln k).
  - Equivalently, the information per reading, sin γ = 2k/(1 + k²), is sech(ln k), the bell of OFS §7.1 (there ½ sech of
    the levels of v/h). It is least wrong at the corner and halves its precision with every level away, on either side.
  - **Killed if** |d ln d/dγ|, taken by complex step from d(γ) = (B/2)/tan(γ/2), misses cosh(ln k) by more than 1e-12
    (relative) anywhere over k from 2⁻³⁰ to 2³⁰, or sin γ misses sech(ln k) by more than 1e-12.
- **P2. The flip: a target at d and one at (B/2)²/d are read equally well.** **Killed if** the relative errors at k and
  1/k differ by more than 1e-12 over the same range.
- **P3. Parallax holds a band of levels about its corner.** With step ε, the relative error ε·cosh(ln k) stays at or
  below 1 for |ln k| ≤ acosh(1/ε): a band of acosh(1/ε)/ln 2 levels on each side of the corner, about log₂(2/ε).
  - Its far edge is at d ≈ B/ε, where the parallax angle is one step: COR's "a shift of one address" seen from the corner.
  - For ε = 10⁻³ the band is 10.97 levels each side.
  - **Killed if** the far edge's d·ε/B misses 1 by more than 1e-6 at ε = 10⁻⁶, or the band's half-width misses
    acosh(1/ε)/ln 2 at ε = 10⁻³ by more than 1e-9.
- **P4. The first-order error is the real one, near the corner.** Triangulating a target on the bisector from two
  standpoints, each direction read with Gaussian error ε/√2 (so the parallax angle's error is ε), at ε = 10⁻⁶ and
  20,000 draws per point: the rms relative error in distance divided by ε·cosh(ln k) lies within 3% of 1 for every
  k = 2^j, j from −8 to 8.
  - **Killed if** any point is off by more than 3%.

Known already: triangulation and its conditioning (1/sin γ), the inscribed-angle theorem behind the Thales circle, and
stereo's d²ε/B depth error far off. What PXC adds is the reading: parallax has a corner, the circle on its baseline; its
precision across levels is the parallel reader's bell; and its reach is a band of levels set by the step, the baseline
being a second zoom like H (`zoom.html`), sliding the band.

## Runs

### Run 1 (13 October, `pxc/pxc.py`)

mpmath at 50 digits for P1–P3; seed 13 for P4; under a second.

| | prediction | result | |
|---|---|---|---|
| P1 | \|d ln d/dγ\| = cosh(ln k), sin γ = sech(ln k), k from 2⁻³⁰ to 2³⁰ | both to 9.9e-43 | not killed |
| P2 | the error at k equals the error at 1/k | to 9.9e-43 | not killed |
| P3 | far edge d·ε/B → 1 at ε = 10⁻⁶; band acosh(1/ε)/ln 2 levels each side at ε = 10⁻³ | 1.0 (to 12 digits); 10.965783924 levels, by bisection on the error itself (log₂(2/ε) = 10.9657843) | not killed |
| P4 | rms relative error over ε·cosh(ln k) within 3% of 1, k = 2⁻⁸ … 2⁸ | within 1% for k ≤ 2⁶; 1.339 at 2⁷ and 7.225 at 2⁸ | **killed** |

The relative error per unit angle: 32.0, 2.125, 1, 2.125 and 32.0 at k = 1/64, ¼, 1, 4 and 64.

**P4 was killed by my measure.** I measured the triangulated point's distance from the baseline's middle, which takes in
the error along the baseline as well as along the line of sight. Worked through to first order for a target on the
bisector at distance d (half-baseline 1), with each direction off by δ:
- the error along the line of sight is σ_y = (1 + d²)·ε/2, which over d is ε·cosh(ln k), as predicted;
- the error along the baseline is σ_x = σ_y/d.

Inside the Thales circle (d < 1) the error along the baseline is the larger. It enters the distance from the middle only
in second order, as x²/(2d), but near the baseline that term outgrows σ_y. With it, the rms relative error is
√(σ_y² + 3σ_x⁴/(4d²))/d, which gives 1.35 at k = 2⁷ and 7.3 at k = 2⁸ against the 1.339 and 7.225 found. Run 2 measures
depth along the line of sight, as P1 is stated, and tests the shape of the error, a corner result found in working this
out: the ellipse's aspect ratio σ_y/σ_x is d = 1/k, the reading's flip, so **the error is round exactly at the corner**,
stretched along the line of sight outside the Thales circle and along the baseline inside it.

### Run 2: predictions (13 October, written before `pxc/pxc2.py` exists)

Same set-up as P4 (ε = 10⁻⁶, 20,000 draws a point, k = 2^j for j from −8 to 8, each direction off by Gaussian ε/√2).
- **P5. Depth along the line of sight follows the bell.** The rms of (y − d)/d over ε·cosh(ln k) lies within 3% of 1 at
  every k. **Killed if** any point is off by more than 3%.
- **P6. The error is round at the corner.** The ratio of rms errors, along the line of sight over along the baseline,
  σ_y/σ_x, lies within 3% of d = 1/k at every k, so within 3% of 1 at the corner, above 1 outside the Thales circle and
  below it inside. **Killed if** any point is off by more than 3%.
- **P7. Run 1's P4 is the second-order term.** The rms relative error in the distance from the middle, over
  √(σ_y² + 3σ_x⁴/(4d²))/d with σ_y = (1 + d²)ε/2 and σ_x = σ_y/d, lies within 3% of 1 at every k. **Killed if** any
  point is off by more than 3%.

### Run 2 (13 October, `pxc/pxc2.py`)

Seed 14, 20,000 draws at each of 17 points, a second.

| | prediction | result | |
|---|---|---|---|
| P5 | depth's rms relative error over ε·cosh(ln k) within 3% of 1 | 0.990 to 1.014 at every k | not killed |
| P6 | σ_y/σ_x within 3% of d = 1/k | 0.987 to 1.010 of d at every k; at the corner σ_y/σ_x = 1.008 | not killed |
| P7 | run 1's distance from the middle over √(σ_y² + 3σ_x⁴/(4d²))/d within 3% of 1 | 0.984 to 1.015 | not killed |

**Reading.**
- **Parallax has a corner: the circle on its baseline.** There the baseline subtends a right angle, the relative error
  per unit angle is least (exactly 1), and the error is **round**: as large along the baseline as along the line of
  sight. That last is new to the corpus and exact to first order: σ_y/σ_x = d/(B/2), the pair's reading flipped.
- **Its precision across levels is the parallel reader's bell.** sin γ = sech(ln k): the information in one reading of
  the parallax angle falls by half with every level from the corner, on either side, as OFS §7.1's bell does. Parallax
  is itself a parallel reading, two directions held at once.
- **Its reach is a band set by the step,** acosh(1/ε)/ln 2 ≈ log₂(2/ε) levels each side of the corner. The far edge is
  d ≈ B/ε, where the shift is one step (COR's "one address"). Choosing B slides the band, as choosing H slides the
  reader's window (`zoom.html`): the baseline is a second zoom.
- **Why parallax and situated observation are both needed.** Outside the corner the error stretches along the line of
  sight by the factor d/(B/2), until past the far edge a triangulated point is a ray: a direction with no distance, which
  is exactly what one standpoint holds alone. Parallax is two situated readings and one amount, B; far past its band it
  returns to situated observation. Neither alone gives distance: without the readings there is nothing to difference,
  and without B nothing fixes the scale (OFS Proposition 8). Past the band, distances go on only by ratios read from
  one standpoint against a kind calibrated inside it (the ladder; `plans/stc-plan.md`).
- **All of it is classical** (triangulation's 1/sin γ, the inscribed-angle theorem, stereo's depth error growing as d²).
  What PXC adds is the reading: the corner, the bell, the round error at the corner, and the band.
