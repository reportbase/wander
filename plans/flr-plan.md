# FLR: Fieller's theorem, followed to its conclusion

26 Oct 2026. Tom: "why does statistics say about this, they seem to get upset when the cauchy addresses dont' create a
mean. why do they think cauchy creates a mean?", then "yes" to a second deep dive after CCA, on the classical result
where a ratio read as an amount gives intervals statisticians themselves call strange.

## The classical result, as it is stated

Fieller (1940, 1954). Two normal estimates a and b of the means μ_a and μ_b, with known variances v₁₁ = Var a,
v₂₂ = Var b and covariance v₁₂. Wanted: the ratio ρ = μ_a/μ_b, an amount (a potency, a relative risk, a calibration
point). Since a − ρb is normal with mean 0 and variance v₁₁ − 2ρv₁₂ + ρ²v₂₂ at the true ρ, the set

  F = {ρ : (a − ρb)² ≤ t²·(v₁₁ − 2ρv₁₂ + ρ²v₂₂)},  t² = 3.8415 (χ²₁ at 95%),

covers ρ with probability exactly 95%. F is where a quadratic in ρ is not positive, so it is one of three shapes:

1. a bounded interval [L, U], when b² > t²v₂₂ (the denominator clearly not zero);
2. an "exclusive" set, (−∞, L] ∪ [U, ∞), when b² < t²v₂₂ and the discriminant is positive;
3. the whole line, otherwise.

The classical reading: the bounded case is the answer; the exclusive set is "strange", "an interval containing infinity";
the whole line means "the data contain no information about the ratio". The usual alternative, the delta method
ρ̂ ± t·se(ρ̂) with ρ̂ = a/b, is always bounded and reported as the interval for the ratio. Gleser and Hwang (1987) proved
that any confidence procedure for such a ratio whose sets are bounded with probability 1 has worst-case coverage 0:
unbounded sets are forced. The conclusion classical work draws is about the payload: how big the ratio is, and when the
data cannot say.

## The same computation, read as addresses

The ratio μ_a/μ_b is the slope of the line through home toward the point (μ_b, μ_a): a direction [μ_b : μ_a], a point of
the projective line, written in the chart v/h. Fieller's condition (a − ρb)²/Var(a − ρb) ≤ t² is the squared Mahalanobis
distance from the estimate z = (b, a) to the line through home of slope ρ. So F is **the set of directions whose line
through home meets the confidence ellipse** {x : (x − z)ᵀV⁻¹(x − z) ≤ t²}: the cone from home tangent to the ellipse. On
the circle of directions it is always one arc, or the whole circle; the three classical shapes are the one arc in the
slope chart:

1. the arc misses the vertical direction (slope ±∞, the chart's horizon): a bounded interval;
2. the arc contains the vertical direction: in the slope chart it runs out through +∞ and back in from −∞, the exclusive
   set, an ordinary arc;
3. the ellipse contains home: every line through home meets it, every direction is possible, because the point may be at
   home, where there is no direction. This is the one case with no information, and it is no information about the
   direction, set by the distance from home, not by the denominator.

Known beforehand: Fieller's exact coverage; von Luxburg and Franz (2009, *Statistica Sinica*) drew F as the cone of the
ellipse; Gleser and Hwang (1987) the impossibility of bounded sets. What is ours is the reading: the ratio is an address,
the strange set the slope chart's view of one arc, and the honest limit distance from home, not the size of μ_b.

## Set-up

`runs/flr/flr.py`, numpy and scipy, seeded. Directions θ ∈ [0°, 180°) on a grid of 3,600 (0.05°), the slope ρ = tan θ,
θ = 90° the vertical (ρ = ±∞). Random cases: z uniform in a disc of radius 6, V a random positive-definite matrix with
eigenvalues in [0.1, 4]. Coverage by simulation, 100,000 a setting, tolerance 4 SE. t² = 3.8415 throughout.

## Predictions (written before any script)

- **F1 (Fieller's set is the cone of the ellipse).** On 10,000 random cases and the 3,600-direction grid, θ is in F (the
  quadratic in ρ = tan θ, with the vertical judged by its limit, b² ≤ t²v₂₂) exactly when the line through home at θ
  meets the ellipse (least Mahalanobis distance from z to the line ≤ t). Kill: any disagreement not within 10⁻⁹ of the
  boundary.
- **F2 (always one arc).** On 100,000 random cases F, on the circle of directions (wrapping 180° to 0°), is one connected
  arc or the whole circle, never empty, never two pieces; it is bounded in the slope chart exactly when the arc misses
  90°, exclusive exactly when it contains 90° and is not whole. Kill: any case otherwise.
- **F3 (the whole line is home inside the ellipse).** F is the whole line exactly when zᵀV⁻¹z ≤ t², on the same 100,000.
  Kill: any case otherwise.
- **F4 (the coverage is the direction's).** With V = I and |μ| = 3 at true directions 0°, 45°, 80°, 89° and 90°:
  (a) Fieller's set covers the true direction (90° included, where the ratio is ∞) 95% within 4 SE at all five;
  (b) the delta interval in the slope chart, ρ̂ ± t·se(ρ̂), covers at least 90% at 0° and 45°, at most 50% at 89°, and
      never at 90° (it is bounded and the truth is ±∞);
  (c) the delta interval in the angle chart, θ̂ ± t·se(θ̂), θ̂ = atan2(a, b) and se(θ̂) = 1/|ẑ|, covers alike at all five
      (each within 4 SE of their pooled value).
  Kill: any clause fails.
- **F5 (no information is set by the distance from home).** With V = I, |μ| = 2, at the same five directions: the
  whole-line rate equals P(χ²₂ with noncentrality 4 ≤ t²) within 4 SE at every direction; the exclusive rate rises
  through 0°, 45°, 80°, 89°, 90° (each at least the one before, less 4 SE). Kill: either fails.

## Not claimed

Fieller's theorem is exact and Gleser and Hwang's proof right; nothing about any study that reported a ratio (R364). The
question is only what the ratio is: an amount, or a direction written in a chart that puts one direction at infinity.

## Runs
