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

### Run 1 (26 Oct; `runs/grs/grs.py`, output `runs/grs/grs-run1.txt`, 3 minutes)

Nothing killed.

- **G1 not killed.** det(I + XᵀX)^(−n/2)·dX unchanged, exactly, by five rational rotations at five rational points each,
  for (k, n) = (1, 2), (1, 3), (2, 3), (2, 4), (2, 5).
- **G2 not killed.** Gr(2, 3): det(I + XᵀX) = 1 + a² + b², the wedge's law; the plane's principal angle is its normal's
  angle from the third axis.
- **G3 not killed.** Gr(2, 4): X ↦ X⁻¹ has |J| = |det X|⁻⁴ and det(I + X⁻ᵀX⁻¹) = det(I + XᵀX)/det(X)², so the law is
  kept; the principal angles' density ∝ |cos²θ₁ − cos²θ₂| is unchanged by θ ↦ π/2 − θ (to 6·10⁻⁵⁵);
  E[cos²θ₁cos²θ₂] = 0.1666666667 (Monte Carlo z −0.29), E|cos²θ₁ − cos²θ₂| = 0.6168502751 (z −0.17).
- **G4 not killed.** P(both t ≤ 1) = P(both t ≥ 1) = 0.107300918301276, straddling the corner 0.785398163397448
  (Monte Carlo 0.10718, 0.10716).
- **G5 not killed.** median t₁ 0.355357, median t₂ 2.814071, product 1 (to 10⁻²⁰); P(t₁t₂ ≤ 1) = ½; Monte Carlo
  median(t₁t₂) 0.99827.
- **G6 not killed.** Each entry of X against the Cauchy: KS p 0.632, 0.034, 0.799, 0.677; quartiles within 0.006 of ±1.
- **G7 not killed.** det X against ½(1 + |r|)⁻²: KS p 0.719; against the Cauchy p < 10⁻³⁰⁰. P(|det X| ≤ ⅓) 0.2499
  (the diamond's ¼; the Cauchy's 0.2048); median |det X| 0.998.
- **G8 not killed.** Gr(2, 5): P(t₁t₂ ≤ 1) = 0.25 (Monte Carlo 0.25023), median(t₁t₂) 2.41.

### After run 1 (post hoc; `runs/grs/grs1-posthoc.py`, `runs/grs/grs1-posthoc.txt`)

Closed forms suggested by the numbers, checked to 50 digits, not predicted: the straddling share is π/4, so the near field
and the far field are each (1 − π/4)/2; E|cos²θ₁ − cos²θ₂| = π²/16; E[cos²θ₁cos²θ₂] = 1/6; in Gr(2, 5),
P(t₁t₂ ≤ 1) = ¼ exactly.

## What run 1 says

One rank up, the shape OFS gives the k = 1 case survives where the exchange does, and changes where it should.

- **Every coordinate keeps its corner.** Each entry of X is a standard Cauchy: holding a plane, every ratio of an
  isotropic pair is still the turn's law, median at the corner.
- **The exchange keeps the corner as the median of the whole.** For n = 2k (Gr(2, 4)) the exchange sends X to X⁻¹ and
  each angle θ to π/2 − θ, so the product of the two tangents has its median at 1 and the two medians are reciprocal.
  Without it (Gr(2, 5)) the corner is only the lower quartile of the product.
- **A plane's own number is not the Cauchy.** det X = ±t₁t₂, the Plücker ratio p₃₄/p₁₂, has its corner at its median and
  no mean, but its law is the uniform diamond's ½(1 + |r|)⁻², not the turn's. The Cauchy belongs to directions; a plane's
  "how far turned as a whole" is a different, still reciprocal-symmetric, law (OFS Theorem 6(e)'s family, not 5(d)'s).
- **The near field shrinks.** The two angles repel (|cos²θ₁ − cos²θ₂|), so both inside the corner happens
  (1 − π/4)/2 ≈ 0.107 of the time, the same both outside, and straddling π/4 ≈ 0.785. At k = 1 the near field is ½.
- **k = 2, n = 3 is the wedge again**, by duality (a plane is its normal line).

### Run 2: predictions (26 Oct; Tom: "1", to finishing the Grassmannian), written before any run-2 script

**Derived before the run (by hand, to be checked exactly).** For Gr(k, 2k) the SVD Jacobian gives the chart measure
∏_{i<j}|t_i² − t_j²|·∏(1 + t_i²)^(−k)·dt; with t = tan θ every power of cos θ cancels, so the principal angles have density
∝ ∏_{i<j}|cos²θ_i − cos²θ_j| for every k (run 1's k = 2 form). With u = cos 2θ = cos φ, φ uniform on [0, π], it is
∝ ∏|u_i − u_j|: arcsine-distributed u's repelling linearly (a Jacobi ensemble, β = 1). For k = 2, write a = |u|
(a = cos ψ, ψ uniform on [0, π/2], E a = 2/π): opposite signs give |u₁ − u₂| = a₁ + a₂, the same sign |a₁ − a₂|, and
∫∫|cos x − cos y| over [0, π/2]² = 4 − π, so E|a₁ − a₂| = 16/π² − 4/π. Then
P(straddle) = ½·(4/π) / (½·(4/π) + ½·(16/π² − 4/π)) = (2/π)/(8/π²) = π/4.

Also derived: one entry of X = B·A⁻¹ is b·c with c = A⁻¹e₁; c is orthogonal to rows 2…k of A and a₁·c = 1, so
|c| = 1/|Z′| (the part of a₁ off the other rows, one standard normal), and b·c = |c|·Z: every entry is Z/|Z′|, a standard
Cauchy, for every k and n.

- **Q0.** P(straddle) for Gr(2, 4) is π/4 exactly (the integral 4 − π symbolic; the share to 50 digits). Kill: either not.
- **Q1.** The chart density det(I + XᵀX)^(−n/2) is rotation invariant for (k, n) = (3, 6), (4, 8), (3, 7), exactly, by
  the Jacobian of X ↦ (C + DX)(A + BX)⁻¹ as the linear map dX ↦ (D − X′B)·dX·(A + BX)⁻¹ (determinant det(D − X′B)^k ·
  det(A + BX)^(−m)), at 5 rational Cayley rotations × 5 rational points. Kill: any inequality.
- **Q2.** For n = 2k the principal angles' law is ∏_{i<j}|cos²θ_i − cos²θ_j|: at k = 3 and 4 the Monte Carlo
  (N = 10⁶) matches the exact count of angles inside the corner (below) within 4 SE in every count. Kill: any outside.
- **Q3.** The exchange makes the number of angles inside the corner symmetric about k/2 (exact). Kill: not exact.
- **Q4.** The near field (every angle inside the corner) shrinks fast: P_in(1) = ½, P_in(2) = (1 − π/4)/2 = 0.1073,
  P_in(3) < 0.054, P_in(4) < P_in(3)/2. Kill: any of the three inequalities fails.
- **Q5.** For n = 2k the product of the tangents (|det X|) has its median at 1 (exactly by the exchange; Monte Carlo
  within 4 SE at k = 3, 4). Kill: off.
- **Q6.** Every entry of X is a standard Cauchy at (3, 6), (4, 8), (3, 7): KS p ≥ 0.001 for each of four entries at each.
  Kill: any below.
- **Q7.** The plane's own number is not a Cauchy, and spreads in levels as k grows: ln|det X| symmetric about 0, its
  variance π²/4 = 2.467 at k = 1, π²/3 = 3.290 at k = 2 (the logistic, from run 1's ½(1 + |r|)⁻²), and strictly larger
  at k = 3 and again at k = 4. Kill: k = 2 off π²/3 by 4 SE, or not increasing, or det X at k = 3 with KS p > 10⁻⁶
  against the Cauchy.
- **Q8.** Without the exchange (Gr(3, 7)) the corner is not the median: P(∏t ≤ 1) < ½. Kill: ≥ ½ − 4 SE.

Exact counts: P(j of the k angles inside) by symbolic integration over the ordered φ's (sympy), for k = 2, 3, 4.
