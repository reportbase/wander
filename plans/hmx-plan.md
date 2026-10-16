# HMX: why the central sweep's payload is Gaussian and the inscribed sweep's addresses Cauchy

*15–16 October 2026. Tom shared ChatGPT's comment on R271–R275 ("the Gaussian outside and Cauchy inside may not be two
competing descriptions of the same distribution … the outside retains magnitude, while the inside retains proportion";
`plans/ofs-review-11.md`), and to Claude's proposal (Herschel–Maxwell), "yes" (SPN R276).*

## The claim

Let the payload at the reader be two components, X on h's side and Y on v's, read in amounts (the bridge: X and Y are
amounts; their ratio Y/X is unitless and is the reading s = v/h, where the payload is all there is to read). The
reader's turns are undetectable (OFS Proposition 3(e), Jaynes's group). Add one premise: the two components vary
independently. Then:

- the payload law is the isotropic Gaussian (Herschel 1850, Maxwell 1860): the central sweep's;
- its direction is even and its ratio is the Cauchy: the inscribed sweep's addresses;
- its size is independent of its direction: the payload separates from the address exactly (OFS Theorem 6(a));
- unequal spreads σ_v ≠ σ_h are OFS Proposition 5(d)'s c = σ_v/σ_h, the corner kept only at c = 1;
- a payload whose centre is off the origin is no longer read as a Cauchy (R275's density varying with direction).

Everything here is classical; the run checks the reading given it, exactly (mpmath, 30 digits, quadrature).

## Predictions (written before any run)

- **P1. Turns and independence force the Gaussian.** For a product density f(x)·f(y), invariance under turns holds for
  f normal and fails for the Laplace, the uniform on [−1, 1] and Student's t with 3 degrees of freedom. *Killed if* the
  normal's density on the circle x² + y² = 1 varies by more than 1e-25 across 8 directions, or any of the other three
  varies by less than 1e-3.
- **P2. Its ratio is the Cauchy, with scale σ_v/σ_h.** For independent zero-mean normals with spreads σ_h, σ_v, the
  quadrant's reading s = |Y|/|X| has P(s ≤ r) = (2/π)·arctan(r·σ_h/σ_v), median σ_v/σ_h, at the corner only when
  σ_v = σ_h. *Killed if* at (σ_h, σ_v) = (1, 1), (1, 2), (3, 1) and r = ¼, 1, 4 the quadrature differs from the closed
  form by more than 1e-20.
- **P3. Size is independent of direction only when the spreads are equal.** For the isotropic normal,
  P(R ≤ a, θ ≤ t) = P(R ≤ a)·P(θ ≤ t) on the quadrant (R = √(X² + Y²), θ = arctan(|Y|/|X|)), with P(θ ≤ t) = 2t/π. *Killed
  if* the defect exceeds 1e-20 at (a, t) = (0.5, π/8), (1, π/4), (2, 3π/8), or if at σ_v = 2σ_h the defect is below 1e-3
  at any of them.
- **P4. A payload off centre is not read as a Cauchy.** With means (μ_h, μ_v) = (0, 1) and unit spreads, the reading
  |Y|/|X| has median above 1, and its law differs from the half-Cauchy with that same median by more than 1e-3 somewhere
  on r = ¼, ½, 2, 4. *Killed if* either fails.
- **P5. The payload has a mean; the address has none.** The components' mean absolute value is σ·√(2/π) (finite); the
  reading's mean over s ≤ M grows as (2/π)·ln M + o(1) (no limit). *Killed if* E|X| at σ = 1 differs from √(2/π) by more
  than 1e-25, or E[s; s ≤ M] − (2/π)·ln M changes by more than 1e-6 between M = 10⁶ and 10⁸ (it should settle at
  (1/π)·ln(1 + 1/M²)-corrected 0, i.e. the truncated mean is (1/π)·ln(1 + M²)).

## Runs

