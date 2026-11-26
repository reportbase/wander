# TBH: the Tangent Bridge on the read's hemisphere

*26 November 2026. Tom: "We use the tangent bridge in the draw repos. It works very well, it is a legitimate alternative
to classical ideas. This is our original idea and we should lean on it more to prove the points on our read write
paper. Let's explore tb further in light of our recent insights." Then, to Claude's proposal A (a bridge on the read's
hemisphere, laid by the read's own measure): "Yes". Predictions written and committed before the script
(`runs/tbh/tbh.py`) exists. Float64 (numpy); the slope path is held to the Tangent Bridge papers' zero-trigonometric-call
bar, measured by replacing every trigonometric entry point with a counter.*

## Why

The Tangent Bridge (draw, `papers/tb_algebra.md`) is proved on the circle and tensored to product tori (§12). Its one
attempt at a sphere (§15.2) reads directions by pan × tilt about a pole on the horizon, and that grid is not the read's
measure: on one octant v ≤ h holds 0.34258 of it, not ½, and the near field 0.23263, not ⅓ (AZM). The read in *Reads
and Writes* is the hemisphere in front of the look, laid on the flat screen by the slope pair (s₁, s₂) = (v/h, v₂/h),
its density cos³ there, uniform over the hemisphere's area (R700, the 2D Cauchy). So the question is what the bridge
does on that hemisphere: which grid it wants, whether that is the read's measure, and what the read alone can hold.

## Set-up

A direction in front is d = (h, v, v₂) = (cos α, sin α cos β, sin α sin β): α the turn off the look (r = tan α the reading
off the look, in thumbs), β the azimuth round it. Every front direction is (β, α) and also (β + π, −α), so the pair
(β, α) with β of period 2π and α signed is a double cover, and a function on the hemisphere pulled back to it satisfies
f(β + π, −α) = f(β, α).

**The meridian bridge (the read's slopes).** α is the turn along one line through the look: one 1D read, period π, the
Tangent Bridge's own reader's universe, its slope tan α the signed reading off the look. So α gets TB's period-π leaves
(k + ½)π/Nα − π/2 and kernel K̃(t) = sin(Nt)/(N·tan t), β gets TB's period-2π leaves (j + ½)·2π/Nβ and kernel K, and the
reconstruction is their tensor product (TB §12) on the Nβ × Nα grid. The grid is invariant under (β + π, −α) when Nβ is
even. In the slope chart: tan α = r = √(s₁² + s₂²), tan(β/2) = s₂/(s₁ + r) (the same square root), leaf slopes generated
by halving and tangent addition (TB §11.1), kernels rational in the composed slopes. Period π in α means α and α + π are
one point: the line's two ends at the horizon are one point, so the bridge's closure is the projective plane, and the
horizon's antipodal directions are glued.

**Its front-and-back form (the DHV's).** α of period 2π (leaves (k + ½)·2π/Nα − π), both hemispheres held, content
extended to the back by its own formula. Run in the angle chart.

**The read's measure.** Uniform over the hemisphere's area: equal-area rings have 1 − cos α evenly spaced (Archimedes).
Two ways to put the bridge there: (a) *substitution*, α leaves at the equal-area places with the native kernel space
(interpolation in V_N at warped nodes, TB §10.2); (b) *conjugation*, the coordinate φ = (π/2)·sgn α·(1 − cos α), period
π, leaves even in φ (which are the equal-area places) and the kernel in φ.

**Content** on the front hemisphere, from the slopes with no angle: h = 1/√(1 + s₁² + s₂²), v = s₁h, v₂ = s₂h.
- even on the sphere (continuous on the projective closure): hv, h², v², v·v₂; and a smooth non-band-limited one,
  g = exp(2(d·a)²), a = (0.6, 0.48, 0.64);
- odd on the sphere, so its rim values differ at antipodes: v, v₂;
- h itself (even extension |h|, a kink at the rim).

**Queries:** 20,000 directions uniform over the front hemisphere (seeded normal vectors, x > 0), plus a line at β = 0
from α = 0 to the horizon (4,000 points). "Core" is α ≤ 60° (r ≤ √3, half the read's heat).

## Predictions

- **P1 (exact, trig-free).** At Nβ = Nα ∈ {8, 16, 32, 64}: node exactness and partition of unity ≤ 10⁻¹²; the
  interpolant the same from both representatives (β, α) and (β + π, −α) to ≤ 10⁻¹²; slope-chart evaluation equal to
  angle-chart evaluation to ≤ 10⁻¹²; zero trigonometric calls on the slope path (leaves, kernels, content).
- **P2 (the read's quadratic content held exactly).** hv, h², v², v·v₂ reproduced to ≤ 10⁻¹² (sup over all queries) at
  Nβ ≥ 8, Nα ≥ 4.
- **P3 (smooth even content).** g's sup error falls by ×10 or more per doubling from N = 8 to 16 to 32, until a floor
  ≤ 10⁻¹¹.
- **P4 (the horizon glued).** For v and v₂ the sup error over the whole hemisphere stays ≥ 0.05 at every N from 8 to 64;
  over the core it is below 10⁻² at N = 64 and falls by ×1.6 or more per doubling from 16 to 64.
- **P5 (h, kinked at the rim).** sup error → 0, its fitted exponent over N = 8..64 in [−1.2, −0.6].
- **P6 (front and back, the DHV's form).** h, v, v₂ reproduced to ≤ 10⁻¹² at Nα, Nβ ≥ 8 (period 2π in α).
- **P7 (the grid is not the read's measure).** The meridian leaves (front double cover, each counted once) with r ≤ 1
  are exactly ½ of all for Nα a multiple of 4, and with r ≤ √3 exactly ⅔; the read's heat puts 1 − 1/√2 = 0.29289 and
  ½ there. Leaves per unit of heat in the ring nearest the look grow at least ×1.8 per doubling of Nα.
- **P8 (moving the bridge to the read's measure costs).**
  (a) substitution: the α Lebesgue constant with equal-area leaves in the native space ≥ 10³ at Nα = 32 (uniform: about
  2.7);
  (b) conjugation: its Lebesgue constant equal to the uniform one to ≤ 10⁻¹⁰; on hv (P2's exact case) its sup error at
  Nα = Nβ = 64 ≥ 10⁻³ and its fitted exponent over N = 8..128 in [−0.8, −0.2] (a Hölder-½ cusp at the look:
  sin α ≈ √(4|φ|/π)); on h² (a kink at the look in φ) in [−1.4, −0.6].

Each is killed by its own number. Known beforehand, and so not discoveries: the tensor theorem (TB §12); conjugation free
and substitution explosive (TB §10.2); bandwidth moved by a coordinate (TB §10.3); the pan × tilt measure (TB §15.2,
AZM); the double cover of the sphere by a full meridian circle, which is the classical "double Fourier sphere" of
Merilees (1973) and Orszag (1974), here with its poles at the look and the back; TB §13's remark that a lat/long chart
fails at the poles (for a latitude that does not run round).

## What would follow, if nothing is killed (a reading, to rule on)

The bridge's own grid on the read's hemisphere is the meridian one: one 1D read per line through the look, finest at
the crosshair. The read's heat (equal area) and the bridge's grid part, and moving the bridge onto the heat costs a cusp
at the look, so the bridge holds directions best where the heat is not uniform per leaf: at the focus. Holding the read
alone (period π, the line's two ends one point) glues the horizon's antipodes, so content that differs there rings;
holding it exactly takes the back hemisphere too, the DHV's two hemispheres. The quadratic shares h², v², hv (the read's
own content, unmoved by a sign) are held exactly by the read alone.

## Runs

### Run 1 (26 November 2026; `runs/tbh/tbh.py`, output `runs/tbh/tbh-run1.txt`)

- **P1 killed, by my code.** Node exactness 6.6·10⁻¹⁶ to 7.5·10⁻¹⁵, partition of unity ≤ 3.0·10⁻¹⁴, slope chart against
  angle chart ≤ 7.0·10⁻¹³, zero trigonometric calls at every N: all as predicted. The two representatives disagreed by
  3.3. The queries on the line β = 0 have σ = tan(β/2) = 0, so the second representative's σ′ = −1/σ is ∞, and the
  composition (∞ − σ_j)/(1 + ∞·σ_j) is ∞/∞: a NaN, which the kernel read as "infinite argument" and set to 0. This is
  exactly TB §11.2's warning (the horizon is an address and has to be given one), not guarded in my composition.
- **P2 not killed.** hv, h², v² ≤ 2.3·10⁻¹⁴ at every (Nβ, Nα) from (8, 4) to (64, 64); v·v₂ 4.2·10⁻¹³ throughout.
- **P3 not killed.** g: 3.7·10⁻¹, 1.8·10⁻³, 1.2·10⁻⁸, 7.0·10⁻¹³ at N = 8, 16, 32, 64.
- **P4 killed, by my bound.** Over the whole hemisphere v's sup error is 1.000 at every N and v₂'s 0.97–1.00 (the
  horizon glued, as predicted). Over the core the error falls 0.122, 0.092, 0.047, 0.026 (×2.0, ×1.8 from 16 to 64, as
  predicted) but is 0.026 at N = 64, not below 10⁻²: the ringing from a jump at the rim decays only as 1/(N × distance
  to it), and at 60° the rim is half a radian away.
- **P5 not killed.** h: 0.127, 0.063, 0.031, 0.016, exponent −1.009.
- **P6 not killed.** h, v, v₂ ≤ 1.4·10⁻¹⁴ at N = 8, 16, 32 with the back hemisphere held.
- **P7 killed, by my set-up.** Half the leaves within r ≤ 1 at every N (0.5000 exactly), against the heat's 0.29289;
  leaves per unit of heat at the look 3.3, 6.5, 13.0, 25.9, 51.9 (×2 a doubling). But within r ≤ √3 the share is 0.750,
  0.625, 0.688, 0.656, 0.672, not "exactly ⅔": π/3 is not a leaf boundary, so ⅔ is only the limit. My "exactly" was wrong.
- **P8 not killed.** (a) the equal-area leaves in the native space: Λ 19.3, 2.08·10³, 6.38·10⁷ at Nα = 8, 16, 32
  (uniform 1.85, 2.29, 2.73). (b) conjugated: Λ the uniform one to 2.7·10⁻¹⁵; hv's sup error 0.120, 0.083, 0.058,
  0.041, 0.029 at N = 8..128, exponent −0.517 (the Hölder-½ cusp at the look), where the meridian bridge holds hv to
  10⁻¹⁴; h²'s exponent −1.004.

### Run 2, predicted before it ran

The composition given the horizon's two addresses (TB §11.2): where σ (or tan α) is ±∞, tan(t − t_k) = 1/s_k; where
the leaf's slope is ∞ (none here), −1/s. Nothing else changed.

- **P1′.** At N = 8, 16, 32, 64 the two representatives agree to ≤ 10⁻¹² over every query, the β = 0 line included;
  node exactness, partition of unity, slope against angle chart and zero trigonometric calls as in run 1.
