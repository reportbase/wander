# GRS: the reader's addresses on the Grassmannian, k = 2

26 Oct 2026. Tom: "are you familiar with the grassmannian.", then "yes, check k = 2".

## The question

A reading from home is a direction, a point of Gr(1, n), the projective space of lines through home. Its uniform measure,
written in the chart [I ; X], is the Cauchy family: (1 + x²)⁻¹ for n = 2 (the sweep), (1 + a² + b²)^(−3/2) for n = 3
(the wedge, OFS Proposition 5(e)), the n-dimensional Cauchy for more parties (WDG run 2). Gr(k, n) is the space of
k-dimensional subspaces through home. Does what OFS says of the k = 1 case (a corner at the median, no mean, every pair at
its corner) carry to k = 2, a reader holding a plane of directions at once?

## Known beforehand

- The uniform (rotation-invariant) measure on Gr(k, n) in the chart X ((n − k) × k, the subspace the columns of [I ; X])
  has density proportional to det(I + XᵀX)^(−n/2): the matrix-variate t with one degree of freedom (Dickey 1967; it is
  the law of B·A⁻¹ for A (k × k) and B ((n − k) × k) independent standard normal).
- Principal angles between subspaces (Jordan 1875; James 1954 for their law under the uniform measure): the singular
  values of X are tan θ_i.
- Gr(2, 4) and the Klein quadric (Plücker coordinates); oriented Gr⁺(2, 4) = S² × S² (the self-dual and anti-self-dual
  parts of a unit 2-vector), uniform on both factors under SO(4) = SO(3) × SO(3) up to a double cover.
- Draw's labs and papers have nothing on Grassmannians, principal angles or the matrix Cauchy (searched 26 Oct).
- OFS: the k = 1 results (Propositions 3(e), 5(d), 5(e), "More parties").

## Set-up

Readings of a plane P through home against a reference plane E₀ (the reader's "h"): X = B·A⁻¹ in the chart, its
singular values t₁ ≤ t₂, t_i = tan θ_i, θ_i the principal angles. The corner is t = 1 (θ = 45°). For n = 2k the exchange
swaps E₀ with E₀⊥, sending X to X⁻¹ and θ_i to π/2 − θ_i (t to 1/t). The near field: both t ≤ 1.

Exact checks with sympy (rational rotations from the Cayley transform, so every number is a fraction) and mpmath; the
seeded Monte Carlo (numpy, N = 10⁶, Gaussian A, B) is a referee for laws only, its tolerance 4 standard errors.

## Predictions (written before any script)

- **G1.** For (k, n) = (1, 2), (1, 3), (2, 3), (2, 4), (2, 5), det(I + XᵀX)^(−n/2)·dX is unchanged by rotations acting on
  the chart, X ↦ (C + D·X)(A + B·X)⁻¹: f(g·X)·|J_g(X)| = f(X) exactly, at 5 rational rotations × 5 rational points each.
  Kill: any inequality.
- **G2.** k = 2, n = 3 adds nothing: the chart density is (1 + a² + b²)^(−3/2), the wedge's, and the plane's one
  principal angle is its normal's angle from the third axis. Kill: either not exact.
- **G3.** Gr(2, 4): the law is unchanged by X ↦ X⁻¹ (exact), and the principal angles' density is
  ∝ |cos²θ₁ − cos²θ₂| on [0, π/2]² (from the SVD Jacobian), unchanged by θ ↦ π/2 − θ. Kill: the exact check fails, or
  the Monte Carlo's E[cos²θ₁·cos²θ₂] or E[|cos²θ₁ − cos²θ₂|] off the density's by more than 4 SE.
- **G4.** The near field shrinks: P(t₂ ≤ 1) = P(t₁ ≥ 1) < ¼ (the angles repel), so straddling the corner,
  P(t₁ ≤ 1 ≤ t₂) > ½. Kill: the exact values break either inequality or the two equal shares differ by 10⁻²⁰; or the Monte
  Carlo is off them by 4 SE.
- **G5.** The corner is still the median where the exchange holds: median(t₁)·median(t₂) = 1 (to 10⁻²⁰) and
  median(t₁t₂) = 1. Kill: either off.
- **G6.** Every entry of X is a standard Cauchy (each a ratio of an isotropic pair in the S² × S² picture), so each entry's
  corner is its median: quartiles ±1. Kill: KS p < 0.001 against the Cauchy for any of the four entries, or a quartile off
  ±1 by 4 SE.
- **G7.** det X = p₃₄/p₁₂ (a Plücker ratio, and ±t₁t₂) is not a Cauchy: with α₁, β₁ independent uniform on [−1, 1]
  (Archimedes), det X = ±(α₁ − β₁)/(α₁ + β₁), the ratio of a uniform diamond's coordinates, density ½(1 + |r|)⁻². Its
  median |·| is 1 (the corner) and it has no mean, but its shape is not the turn's. Kill: KS p < 0.001 against
  ½(1 + |r|)⁻², or KS p > 10⁻⁶ against the Cauchy.
- **G8.** Without the exchange (Gr(2, 5)) the corner is not the median: median(t₁t₂) > 1. Kill: ≤ 1 (exact quadrature of
  the principal angles' law there, ∝ |cos²θ₁ − cos²θ₂|·sin θ₁·sin θ₂, with a Monte Carlo check).

## Not claimed

That a reader holds planes; that k = 2 belongs in OFS. This asks only whether the k = 1 geometry has the shape OFS gives
it one rank up.

## Runs
