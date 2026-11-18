# CLC: calculus from one standpoint

18 Nov 2026. SPN R1099. Tom: "Let's compare shv to calculus.", then "Merge and proceed with your recomendations."

## The question

Calculus sorted by the corpus's tests (R1062: which tools a read needs, which a write needs, which only the dual
hemispherical vantage (DHV) needs). The claims, from Claude's comparison:

1. The first derivative of one length against another is a read (unmoved by scaling the world); every higher derivative
   carries a size, a write (dⁿy/dxⁿ scales as k^(1−n)).
2. A rate against the clock is a write at every order (scaling the world moves x, not the ticks).
3. The chain rule is the tower: the middle denominator is scaffolding (R883).
4. For rational functions, differentiation needs no limit: dual numbers (κ = 0, the stride kind of PYK and CPX) give
   the derivative exactly in rational arithmetic.
5. Integration leaves the rationals: a rational function's derivative is rational, its antiderivative generally needs
   ln or arctan (Liouville; Hermite's reduction gives the rational part in rational arithmetic, the rest is a log part).
6. The fundamental theorem is telescoping, exact at every partition; the limit is needed only where the integrand's sum
   (a Riemann sum) is taken in place of the antiderivative's differences, and its error falls as 1/n.

All classical (dual numbers, Clifford 1873; Hermite 1872; Liouville; Euler–Maclaurin). The sorting is ours.

## Set-up

Exact rational arithmetic (Python `fractions`, sympy 1.14.0 for symbolic derivatives and integrals), seeded
(`random.seed(1099)`). Rational functions with integer coefficients in [−9, 9], numerator degree 0–4, denominator
degree 1–3, a denominator rejected if it has a rational root at an evaluation point. Evaluation points rational,
numerator and denominator in [1, 20] with random sign.

## Predictions (committed before any run)

- **D1** (claim 4). For 300 seeded rational functions f and rational points x, the dual-number evaluation
  f(x + ε) = a + bε, done in `Fraction` arithmetic only (+, −, ×, ÷, no limit, no float), gives b equal to sympy's
  f′(x) exactly in 300 of 300.
- **D2** (claim 3). For 200 seeded pairs (f, g), dual-number evaluation of f(g(x + ε)) gives f′(g(x))·g′(x) exactly in
  200 of 200, and equals the product of the two links' dual parts computed separately.
- **S1** (claim 1). For 100 seeded rational f, the curve scaled about the origin by k (g(x) = k·f(x/k)) has, at the
  scaled point kx, g⁽ⁿ⁾(kx) = k^(1−n)·f⁽ⁿ⁾(x) exactly for n = 1, 2, 3, 4 and k ∈ {2, 7/3, 10}: the first derivative
  unchanged in all 300 (f, k), every higher one moved in every case where f⁽ⁿ⁾(x) ≠ 0.
- **S2** (claim 2). For the same f read as a path x(t) = f(t), the world scaled in space only (X(t) = k·f(t)) moves
  every dⁿX/dtⁿ by k (n = 1–4); the ratio of two paths' rates of the same order at the same t is unmoved, in all cases.
- **I1** (claim 5). For 200 seeded rational functions with a squarefree denominator of degree ≥ 1 and a numerator
  not a multiple of the denominator's derivative, sympy's antiderivative contains log or atan in at least 195 of 200
  (rational in at most 5). Every one of the 200 derivatives is rational (200 of 200).
- **I2** (claim 5). For 100 seeded rational functions with a repeated factor in the denominator, Hermite's reduction
  done in rational arithmetic (sympy's `ratint` rational part) differentiates back, with the log part's integrand,
  to f exactly in 100 of 100; the log part is nonzero in at least 95 of 100.
- **F1** (claim 6). For 100 seeded rational F without poles on [a, b] and random rational partitions of n = 1 … 50
  steps, Σ(F(xᵢ₊₁) − F(xᵢ)) = F(b) − F(a) exactly in every case; the left Riemann sum of F′ over a uniform partition
  is not exact (differs from F(b) − F(a)) in every case with F′ non-constant, and at n = 1000 its error times n is
  within 5% of −(b − a)(F′(b) − F′(a))/2 for at least 95 of 100.

## What could fail, and what could not

D1, D2, S1 (as stated), F1's first clause and I2 are identities: they can fail only by my code. What can fail as a
result: I1's count (if random rational functions often have rational antiderivatives), F1's Euler–Maclaurin clause
(the 5% at n = 1000), and the "every case" clauses where a zero value could make "moved" false by my set-up.

## Runs

