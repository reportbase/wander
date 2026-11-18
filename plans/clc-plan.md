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

**Run 1** (`runs/clc/clc.py`, output `runs/clc/clc-run1.txt`). D1 killed by my code (296 of 300), D2 killed by my code
(193 of 200 against sympy; 200 of 200 against the product of the links), I2 killed by my code (82 of 100): I compared
with `sympy.nsimplify`, which approximates a large fraction through a float and so called equal values unequal, and I
passed improper fractions (numerator degree ≥ denominator degree) to `ratint_ratpart`, which expects the polynomial
part divided off first and left its unknown coefficients unsolved. S1 (first derivative unmoved 300 of 300, higher
orders moved 900 of 900), S2 (time-rates moved by k 1,196 of 1,196, their ratios unmoved 1,196 of 1,196), I1 (no
antiderivative rational, 0 of 200; every derivative rational, 200 of 200) and F1 (telescoping exact 100 of 100;
Riemann sums inexact 100 of 100; Euler–Maclaurin's n·error within 5% at n = 1000 in 99 of 100) not killed.
F1's Riemann clause was run at one partition, n = 7, not at every n from 1 to 50; my set-up, stated here.

**Run 2** (`runs/clc/clc2.py`, output `runs/clc/clc-run2.txt`; the same seed and cases, comparisons by `sp.Rational`
and `sp.cancel`, the polynomial part divided off before Hermite's reduction). Nothing killed: D1 300 of 300, D2 200
of 200 (and 200 of 200 against the links' product), S1 and S2 as run 1, I1 0 of 200 rational and 200 of 200
derivatives rational, I2 100 of 100 back to f with a nonzero log part in 100 of 100, F1 as run 1.

**What it shows.** Within the rational functions, differentiation is algebra on fractions with ε² = 0, the stride
kind: no limit is taken, and the chain rule's dual parts multiply link by link, the middle cancelling (the tower).
Only the first derivative of one length against another is unmoved by scaling the world (dⁿy/dxⁿ moves as k^(1−n)),
so a slope is a read and curvature, acceleration and every higher order a write; a rate against the clock is a write
at every order, and only ratios of rates of one order are unmoved. Integration leaves the rationals: Hermite's
rational part is had in rational arithmetic, but every one of 200 generic cases (300 with I2) kept a log part, which
needs ln or arctan, the completions. The fundamental theorem is exact as telescoping at every partition; the integrand's
own sum misses at every finite n by Euler–Maclaurin's −(b − a)(f(b) − f(a))/(2n), so the limit is needed only where the
integrand is summed in place of the antiderivative's differences. Classical throughout; the sorting ours. I1's count was
the one prediction that could fail as a result; the rest are identities checked, which could fail only by my code, as
run 1 did.
