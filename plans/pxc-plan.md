# PXC: parallax from the corner

*12 October 2026. Tom: "show how parallax and situated observation are both needed. explore parallax from the perspective
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

### Run 1 (12 October, `pxc/pxc.py`)

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

### Run 2: predictions (12 October, written before `pxc/pxc2.py` exists)

Same set-up as P4 (ε = 10⁻⁶, 20,000 draws a point, k = 2^j for j from −8 to 8, each direction off by Gaussian ε/√2).
- **P5. Depth along the line of sight follows the bell.** The rms of (y − d)/d over ε·cosh(ln k) lies within 3% of 1 at
  every k. **Killed if** any point is off by more than 3%.
- **P6. The error is round at the corner.** The ratio of rms errors, along the line of sight over along the baseline,
  σ_y/σ_x, lies within 3% of d = 1/k at every k, so within 3% of 1 at the corner, above 1 outside the Thales circle and
  below it inside. **Killed if** any point is off by more than 3%.
- **P7. Run 1's P4 is the second-order term.** The rms relative error in the distance from the middle, over
  √(σ_y² + 3σ_x⁴/(4d²))/d with σ_y = (1 + d²)ε/2 and σ_x = σ_y/d, lies within 3% of 1 at every k. **Killed if** any
  point is off by more than 3%.

### Run 2 (12 October, `pxc/pxc2.py`)

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

**Corrections to the reading above** (12 October, later, after Tom's "does it belong in ofs?"; the run's numbers stand):
- "Falls by half with every level from the corner" holds only far off. The relative error per unit angle is
  cosh(j·ln 2) at j levels from the corner: 1, 1.25, 2.125, 4.06 and 8.03 for j = 0 to 4. The ratio from one level to
  the next tends to 2 and is 1.25, 1.7 and 1.91 for the first three. P1's wording above the Runs line ("halves its
  precision with every level away") is left as written; its kill condition was cosh(ln k) itself, which stands.
- "Least wrong at the corner" is true of the depth, the error along the line of sight, on the bisector, and of nothing
  more that this plan has shown. Worked out by hand to first order while answering Tom (and evaluated at seven points),
  with each direction off by independent errors of spread σ: across the line of sight the error over d is
  σ√2·(1 + k²)/2, which keeps falling with distance; both together give σ√2·(1 + k²)^(3/2)/(2k), least at
  d = √2·(B/2) (1.299σ√2, against √2·σ√2 at the corner). Off the bisector nothing was shown. Run 3 tests these.
- The presets in `parallax.html` were off by a factor of 2 for the stars. Hipparcos's 1 mas and Gaia's 20 µas are
  precisions of the annual parallax p, the angle that 1 AU (half the baseline) subtends, so p = γ/2 and the step in γ is
  2 mas and 40 µas. The far edge, d ≈ B/ε with B = 2 AU, is then about 1 kpc and 50 kpc, not 2 kpc and 100 kpc
  (`physics.md`'s "about 2 kpc" likewise). Two eyes were right: stereo acuity is a threshold on the disparity, a
  difference in γ itself.

### Run 3: predictions (12 October, written before `pxc/pxc3.py` exists)

Exact first order: the Jacobian of the triangulation map (δ₁, δ₂) ↦ (x, y), the exact intersection of the two turned
lines, taken by complex step in mpmath at 50 digits, never from the formulas below. Each direction is off by an
independent error of spread σ = 1; the error's covariance is J·Jᵀ. Half-baseline b = 1, so k = 1/d on the bisector.
- **P8. On the bisector, which error is least where.** Over d, the spread along the line of sight is
  √2·cosh(ln k) (least at the corner, the same at k and 1/k); across it, √2·(1 + k²)/2 (falling with distance toward
  √2/2, no flip); both together, √2·(1 + k²)^(3/2)/(2k), least at k = 1/√2, that is d = √2·(B/2), where it is
  √2·3√3/4 ≈ 1.299·√2, against √2·√2 at the corner. **Killed if** any of the three misses its formula by more
  than 1e-12 (relative) for k = 2^(j/10), j from −100 to 100, or the least of the total, found by golden section on the
  exact Jacobian, lies off k = 1/√2 by more than 1e-9.
- **P9. On the circle the error is round only at its top.** Where the baseline is seen at a right angle the two lines
  cross square, so the error's ellipse has its axes along the lines' normals, of lengths r₁σ and r₂σ, r₁ and r₂ the
  place's distances from the two standpoints. Its aspect is max(r₁, r₂)/min(r₁, r₂), 1 only where r₁ = r₂, on the
  bisector. **Killed if** the aspect from the exact Jacobian's covariance misses max(r₁, r₂)/min(r₁, r₂) by more than
  1e-12 at points on the circle seen from the middle at 5°, 10°, …, 175° from the baseline.
- **P10. Off the bisector the radial error has no flip.** The radial error over the distance from the middle, along a ray
  at angle φ from the baseline, works out to √[r₁⁴(ρ − b cos φ)² + r₂⁴(ρ + b cos φ)²]/(2bρ² sin φ) (ρ the distance from
  the middle). On the bisector it is the same at ρ and b²/ρ; off it, not. **Killed if** along the ray at 60° it is the
  same at ρ = 2b and ρ = b/2 within 1%, or the exact Jacobian misses the formula by more than 1e-12 anywhere on rays at
  15°, 30°, …, 90°. Where along each ray it is least is measured, not predicted.

### Run 3 (12 October, `pxc/pxc3.py`)

mpmath at 50 digits; under a second.

| | prediction | result | |
|---|---|---|---|
| P8 | depth √2·cosh(ln k), across √2·(1 + k²)/2, total √2·(1 + k²)^(3/2)/(2k) over d; the total least at k = 1/√2 | all three to 1.3e-48; the total least at k = 0.707106781186548 (d = 1.41421356237 half-baselines), 1.2990·√2 against 1.4142·√2 at the corner | not killed |
| P9 | on the circle the aspect is max(r₁, r₂)/min(r₁, r₂), round only at the top | to 5.2e-50 at 5° … 175°; 7.60 at 15°, 2.414 at 45°, 1.303 at 75°, 1 at 90° | not killed |
| P10 | off the bisector, no flip; the radial formula exact | the formula to 6.7e-50; at 60°, 1.862 at ρ = 2b and 1.732 at ρ = b/2 | not killed |

Per √2, on the bisector (d in half-baselines):

| levels from the corner | d | depth | across | total |
|---|---|---|---|---|
| −4 | 16 | 8.031 | 0.502 | 8.047 |
| −2 | 4 | 2.125 | 0.531 | 2.190 |
| −1 | 2 | 1.25 | 0.625 | 1.398 |
| 0 | 1 | 1 | 1 | 1.414 |
| +1 | 0.5 | 1.25 | 2.5 | 2.795 |
| +2 | 0.25 | 2.125 | 8.5 | 8.762 |
| +4 | 0.0625 | 8.031 | 128.5 | 128.75 |

Least radial error along each ray from the middle (measured, not predicted), against its value on the circle:
15° at ρ = 0.968b (0.268 against 0.366), 30° at 0.892b (0.565 against 0.707), 45° at 0.826b (0.889 against 1),
60° at 0.830b (1.184 against 1.225), 75° at 0.936b (1.363 against 1.366), 90° at b (√2).

**Reading.**
- **The corner of parallax is the depth's, on the bisector.** There, and only there, is the error along the line of
  sight least (P8), the same at d and (B/2)²/d, and round (P9). That is the pair (half-baseline, distance) read along
  the bisector, where its reading is k.
- **The error across the line of sight is the direction's.** Over d it falls toward a constant, √2/2, as d grows: the
  direction, which one standpoint already holds, is held equally well at every distance far off. Parallax adds the
  depth, and the depth alone has the corner. Inside the circle the across error grows as 1/d² (the place between the
  standpoints, the two lines nearly one).
- **Together they are least past the corner, at d = √2·(B/2).** The total is not a reading of the pair, so it has no
  flip and its least is not at the corner. Which error a reader must keep small is the reader's question, not the
  geometry's.
- **Off the bisector the circle is not the best place.** Along a ray at 15°–75° the radial error is least inside the
  circle, at 0.83–0.97 of b. On the circle it is √2·sin φ (post hoc, from P10's formula at ρ = b: the numerator is
  8 sin⁴φ), falling toward the standpoints, where the distance from the middle is pinned. The aspect on the circle is
  r₁/r₂ = cot(φ/2) (post hoc), the reading of the pair (distance from A, distance from B), round at that pair's corner.
  The Thales circle is where the baseline is seen square; it is the corner of the depth only on the bisector.
