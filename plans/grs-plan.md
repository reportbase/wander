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

### Run 2 (26 Oct; `runs/grs/grs2.py`, output `runs/grs/grs-run2.txt`, 70 s)

Nothing killed.

- **Q0 not killed.** ∫∫|cos x − cos y| over [0, π/2]² = 4 − π, E|a₁ − a₂| = 4(4 − π)/π², P(straddle) = π/4,
  symbolically; the exact count for k = 2 gives the same.
- **Q1 not killed.** The chart density is rotation invariant exactly at (2, 4), (3, 6), (4, 8), (3, 7) (the Jacobian as
  det(D − X′B)^k·det(A + BX)^(−m)).
- **Q2 not killed.** Exact counts of angles inside the corner against the Monte Carlo: every z within ±1.43.
- **Q3 not killed.** Every count symmetric about k/2, exactly.
- **Q4 not killed.** P(all k angles inside the corner):

  | k | exact | ≈ |
  |---|---|---|
  | 1 | 1/2 | 0.500000 |
  | 2 | 1/2 − π/8 | 0.107301 |
  | 3 | (π − 3)/(4π) | 0.011268 |
  | 4 | 19/256 − 3π/128 | 0.000588 |

  The full laws of the number inside: k = 3 (0.0113, 0.4887, 0.4887, 0.0113); k = 4 (0.0006, 3π/64 = 0.1473,
  109/128 − 3π/64 = 0.7043, 0.1473, 0.0006).
- **Q5 not killed.** P(∏t ≤ 1) 0.50033, 0.49973, 0.49954, 0.50006 at k = 1 … 4 (|z| ≤ 0.92).
- **Q6 not killed.** Every entry tested a standard Cauchy at (3, 6), (4, 8), (3, 7): KS p 0.052 to 0.970.
- **Q7 not killed.** Var ln|det X| = 2.4710 (π²/4 = 2.4674), 3.2930 (π²/3 = 3.2899), 3.7581, 4.0747 at k = 1 … 4,
  each about ±0.006; det X at k = 3 against the Cauchy KS p < 10⁻³⁰⁰.
- **Q8 not killed.** Gr(3, 7): P(∏t ≤ 1) = 0.228, median ∏t = 2.97.

## What run 2 says

Run 1's split holds at every rank tried. The exchange, which exists when the plane is half the space (n = 2k), keeps
the corner as the median of the whole (the product of the tangents) and keeps every count symmetric; without it
(Gr(3, 7)) the corner falls to under a quarter. The exact Cauchy stays with directions: every chart entry is a standard
Cauchy at every (k, n), by a one-line argument (an entry is a normal over the length of a normal's part off the other
rows), while the plane's own number is never one. Its spread in levels grows with k and slows (+0.82, +0.47, +0.32).

The near field shrinks faster than geometrically: ½, 0.107, 0.0113, 0.0006, each step a smaller fraction of the last
(0.21, 0.105, 0.052), because the angles repel (∏|cos²θ_i − cos²θ_j|, the β = 1 Jacobi ensemble on the arcsine law).
A reader holding a k-plane almost never has the whole plane inside the corner; the common case is about half its
angles inside, as the exchange makes it on average. Every share is a rational plus a rational multiple of π (π enters
through the arcsine law of each u = cos 2θ).

Not shown here: a general formula for P_in(k); why the variance of ln|det X| grows as it does.

### Run 3: predictions (26 Oct; Tom: "find the. general formula"), written before any run-3 script

**The formula, derived before the run.** With φ_i = 2θ_i uniform on [0, π] and the density ∏_{i<j}|cos φ_i − cos φ_j|, order
the φ's; the product is then ± a Vandermonde determinant det[c_r(cos φ_j)] for any polynomial basis c_r of degree r, and
Chebyshev's T_r(cos φ) = cos rφ is the natural one. Mark each angle inside the corner (φ < π/2) with a weight z. De
Bruijn's identity (1955) turns the ordered k-fold integral of a determinant into a Pfaffian, so the generating function
of the number j of angles inside the corner is

  G_k(z) = Σ_j P(j inside)·z^j = Pf A_k(z) / Pf A_k(1),

  A_k(z)_{rs} = ∫₀^π ∫₀^π sign(ψ − φ)·w(φ)·w(ψ)·cos rφ·cos sψ dφ dψ, r, s = 0 … k − 1, w = z on [0, π/2), 1 on [π/2, π],

for even k; for odd k, A_k is bordered by the column b_r = ∫₀^π w(φ)·cos rφ dφ (and −b_r as the row), a (k + 1) × (k + 1)
Pfaffian. Every entry is elementary (sines and cosines of multiples of π/2, polynomials in z, and π from the r = 0 row).
P_in(k) is the coefficient of z^k: the same Pfaffian with w = 1[φ < π/2], i.e. A on [0, π/2]² over A on [0, π]².

The leading asymptotic, by the log-gas (Coulomb gas) picture: for large k the arcsine weight is lower order, the charges'
equilibrium on [−1, 1] is the arcsine law (capacity ½, energy ln 2), confined to [0, 1] it is the arcsine law there
(capacity ¼, energy ln 4), and β = 1, so P_in(k) = exp(−(ln 2/2)·k² + O(k)) = 2^(−k²/2 + O(k)).

- **R1.** G_k(z) from the Pfaffian reproduces run 2's exact counts for k = 1 … 4, every coefficient symbolically. Kill:
  any differs.
- **R2.** G_k(1) = 1 and G_k(z) = z^k·G_k(1/z) (the exchange) for k ≤ 8, symbolically. Kill: either fails.
- **R3.** P_in(k) lies in ℚ + ℚ·π for even k and ℚ + ℚ/π for odd k, for k ≤ 8 (as at k ≤ 4). Kill: any other form
  (a π², 1/π² or mixed term surviving).
- **R4.** Brute-force check of the formula at k = 5 and 6: the Monte Carlo of the Grassmannian (N = 10⁶, seeded) within
  4 SE of every coefficient. Kill: any outside.
- **R5.** −ln P_in(k)/k² → (ln 2)/2 = 0.3466: a fit a·k² + b·k + c to −ln P_in(k) over k = 10 … 24 (50-digit
  Pfaffians) gives a within 0.02 of 0.3466. Kill: outside.

### Run 3 (26 Oct; `runs/grs/grs3.py`, output `runs/grs/grs-run3.txt`, 105 s)

Nothing killed.

- **R1 not killed.** The Pfaffian G_k(z) gives run 2's counts for k = 1 … 4, every coefficient symbolically.
- **R2 not killed.** G_k(1) = 1 and z^k·G_k(1/z) = G_k(z) for k ≤ 8.
- **R3 not killed.** P(all k angles inside the corner):

  | k | P_in(k) | ≈ |
  |---|---|---|
  | 1 | 1/2 | 0.5 |
  | 2 | 1/2 − π/8 | 0.107301 |
  | 3 | 1/4 − 3/(4π) | 0.0112676 |
  | 4 | 19/256 − 3π/128 | 5.877·10⁻⁴ |
  | 5 | 17/1536 − 5/(144π) | 1.528·10⁻⁵ |
  | 6 | 109/131072 − 555π/2097152 | 1.97·10⁻⁷ |
  | 7 | 41/1310720 − 161/(1638400π) | 1.3·10⁻⁹ |
  | 8 | (2529 − 805π)/2³² | 4.2·10⁻¹² |

  Even k in ℚ + ℚπ, odd k in ℚ + ℚ/π, every k ≤ 8. The full laws of the count are in the output (k = 5: 367/768 for
  two and for three inside; k = 6: 110805π/524288 for three inside).
- **R4 not killed.** The formula against the Monte Carlo at k = 5 and 6: every z within ±1.80.
- **R5 not killed.** 80-digit Pfaffians for k = 10 … 24 (checked against the symbolic values at k = 5 … 8 to 7·10⁻⁸³):
  −ln P_in(k) ≈ a·k² + b·k + c with a = 0.346595, against (ln 2)/2 = 0.346574; b = 0.5337, c = −0.250.

## What run 3 says

The general formula is a ratio of two Pfaffians of elementary integrals. With φ = 2θ (uniform on [0, π]) and
w(φ) = z below π/2 and 1 above,

  Σ_j P(j of the k principal angles inside the corner)·z^j = Pf A_k(z) / Pf A_k(1),
  A_k(z)_rs = ∫₀^π∫₀^π sign(ψ − φ)·w(φ)w(ψ)·cos rφ·cos sψ dφ dψ, r, s = 0 … k − 1,

bordered by b_r = ∫₀^π w(φ)·cos rφ dφ for odd k (de Bruijn 1955 on the β = 1 Jacobi ensemble with the arcsine weight).
The near field P_in(k) is its top coefficient: the Pfaffian on [0, π/2] over the Pfaffian on [0, π]. Every value is a
rational plus a rational times π (even k) or 1/π (odd k), as each entry carries at most one π from the r = 0 row and its
border. For large k, P_in(k) = 2^(−k²/2)·e^(−0.534k + 0.25 + …): the leading term is the log-gas's (the arcsine law confined
from [−1, 1] to [0, 1], its energy rising by ln 2, at β = 1), confirmed to 6·10⁻⁵ in the coefficient; the linear and
constant terms are measured, not derived.

Classical: de Bruijn's identity, the Jacobi ensemble, the Coulomb-gas large deviation (Dean and Majumdar's method for
the probability that all eigenvalues lie on one side). The reading as a reader's near field is ours.

### Run 4: predictions (26 Oct; Tom: "2,1,3", the third the linear term of the asymptotic), written before any run-4 script

**Disclosed first:** the closed form for b below was derived *after* run 3's fitted b = 0.5337 was seen. Run 3's fit
(k = 10 … 24, three terms, no ln k) cannot tell it apart from nearby numbers; run 4 is the test, at larger k and with the
terms the expansion says are there.

**The derivation.** In x = cos φ the angles are a β = 1 ensemble with weight w(x) = (1 − x²)^(−1/2), on [−1, 1] (the whole)
or [0, 1] (all inside the corner). For such an ensemble the expansion of the log of the partition function is

  ln Z_k = (β/2)·k²·E[μ] + k·[(1 − β/2)·S[μ] + ∫ ln w dμ] + O(ln k),

with μ the equilibrium law (the arcsine law on the interval), E[μ] = ∫∫ ln|x − y| dμ dμ = ln(L/4) and S[μ] = −∫ μ ln μ =
ln(πL/4) for an interval of length L. P_in = Z_k[0, 1]/Z_k[−1, 1], so, at β = 1:

- k²: ½·(ln ¼ − ln ½) = −(ln 2)/2 (run 3's leading term);
- k, entropy: ½·(ln(π/4) − ln(π/2)) = −(ln 2)/2;
- k, weight: ∫ ln w dμ is ln 2 on [−1, 1] and ln(1 + √2) on [0, 1] (by the arcsine law there), a change of ln(1 + √2) − ln 2.

So −ln P_in(k) = (ln 2/2)·k² + b·k + O(ln k), b = ln 2 − ln(1 + √2) + (ln 2)/2 … taken with the signs above,

  **b = ln(1 + √2) − (ln 2)/2 = ln(1 + 1/√2) = 0.534800**,

and the script computes the two integrals ∫ ln w dμ numerically as a check on this paragraph's arithmetic (kill if they
are not ln 2 and ln(1 + √2) to 10⁻³⁰; then the predictions below are void, not tested).

- **S1.** With a fixed at (ln 2)/2, a fit of −ln P_in(k) − (ln 2/2)·k² = b·k + d·ln k + c + e/k over k = 20 … 60 (Pfaffians
  in closed-form entries at enough digits, checked by recomputing at more) gives |b − 0.534800| ≤ 0.002. Kill: outside.
- **S2.** A free fit a·k² + b·k + d·ln k + c + e/k over the same k gives |a − (ln 2)/2| ≤ 10⁻⁴. Kill: outside.
- **S3.** With a and b fixed at the derived values, the rest, c + d·ln k + e/k + f/k², fits k = 20 … 60 with an rms
  residual under 10⁻⁶. Kill: over.

Not claimed: d and c (the ln k and constant terms; edge exponents and the β = 1 constants enter there); these are
reported as measured.
