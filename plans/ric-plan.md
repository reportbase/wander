# RIC: a differential equation from one standpoint

18 Nov 2026. SPN R1101. Tom: "1 2 3", to: record CLC's N sorting (R1100), test differential equations from one
standpoint, then essay 31.

## The question

A numerical solver takes N steps and carries an error falling as 1/N^p. Does the read's own equation need N? The
slope's flow is the Riccati equation s′ = p + qs + rs². Written s = x/y it is the linear system (x, y)′ = B·(x, y),
B = [[q/2, p], [−r, −q/2]], so every flow map is a Möbius map of s, and B² = Δ·I with Δ = q²/4 − pr. For
s′ = 1 + κs² (p = 1, q = 0, r = κ) Δ = −κ: the turn (κ = 1), the boost (κ = −1), the stride (κ = 0), PYK's three kinds.

Claims (Claude's, from the reply to Tom):

1. With constant rational coefficients the equation is stepped exactly by rational Möbius maps M_u = I + u·B, u a
   rational step parameter: they compose by (u, v) ↦ (u + v)/(1 + Δuv), PYK's rule with κ = −Δ, and n steps are the
   exact flow at the elapsed time n·τ(u), τ(u) = artanh(u√Δ)/√Δ (arctan for Δ < 0, u itself for Δ = 0). No N, no
   error. The elapsed time τ is not rational in u: the clock time is where the completion enters (arctan, artanh).
2. A solver stepping in time (Euler, RK4) over the same elapsed time carries error ∝ N^(−1) and N^(−4) (classical).
3. With a coefficient that varies in time (s′ = t + s², the Airy Riccati) the flow maps are still Möbius, but they
   form no one-parameter group: maps over equal time steps do not commute and no rational step rule is known.

## Set-up

mpmath at 50 digits, `fractions` for the exact composition, seeded (`random.seed(1101)`).

## Predictions (committed before any run)

- **Q1** (claim 1, the turn). For s′ = 1 + s², s₀ = 0, u = 1/3, n = 3 steps: the composed fraction equals
  tan(3·arctan(1/3)) to 10⁻⁴⁵, and is 13/9.
- **Q2** (claim 1, general). For 100 seeded constant (p, q, r), integers in [−4, 4] with r ≠ 0, s₀ rational, u = 1/(k + 8)
  with k chosen so |u|·√|Δ| < 1, n = 5: (a) the product of the step matrices in fractions equals
  (1 + Δuv)·M_((u+v)/(1+Δuv)) exactly for every adjacent pair (100 of 100); (b) the five-step fraction equals the flow
  expm(5τB) applied to s₀ to 10⁻⁴⁰ in 100 of 100 (cases where the flow passes a pole are skipped and counted).
- **Q3** (claim 2). For Q1's equation and elapsed time, Euler and RK4 at N = 100, 200, …, 12,800: the log–log slope of
  the error against N within 0.1 of −1 and −4.
- **Q4** (claim 1, cost). Over Q2's cases the composed fraction's digits grow at most linearly in n (no faster than
  c·n for n up to 40, fitted on n = 10–40: the ratio digits(40)/digits(20) under 2.2).
- **Q5** (claim 3). For s′ = t + s², the flow maps M₀₁ (t from 0 to 1) and M₁₂ (1 to 2), each normalized to determinant
  1: (a) M₀₁·M₁₂ ≠ M₁₂·M₀₁, the largest entry of the difference over 10⁻³; (b) no entry of M₀₁ satisfies an integer
  relation with 1 of height ≤ 10⁴ by PSLQ at 40 digits (so no small rational map is the time-1 step).

## What could fail, and what could not

Q1, Q2 (a) and (b) are identities, failing only by my code. Q3 is classical and checks the solvers. Q4 can fail (the
digits could grow faster than linearly). Q5 (b) can fail by a small rational relation turning up; a pass is only that
none of small height exists, not that the entries are transcendental.

## Runs

