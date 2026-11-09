# FRG: the Fisher–Rao geometry of the Cauchy family, checked exactly

9 Nov 2026. SPN R787. Tom: "proceed", to ChatGPT's suggestion (pasted) to investigate the Fisher–Rao geometry of the
Cauchy family first, "without editing Reads and Writes yet": the family C(m, γ), indexed by the standpoint z = m + iγ,
has the Fisher metric (dm² + dγ²)/(2γ²), half the Poincaré metric, and a Kullback–Leibler divergence that is a function
of the hyperbolic distance alone. The question is whether this adds a distinction to *Reads and Writes* or is another
language for one it already makes.

Lab rules: predictions first, from the theory alone; exact arithmetic (mpmath, 50 digits); a killed run stays killed.

## Known beforehand

- JAY P2 (`plans/jay-plan.md`): the arc's foot is Jeffreys's arcsine and its Fisher–Rao length is the facing 2θ; the
  Cauchy pushed through a real Möbius map is the Cauchy at g(z) (McCullagh 1996), to 10⁻⁶¹.
- DYH D2–D3 (`plans/dyh-plan.md`): the dyadic cells as points m + iγ tile the hyperbolic plane (Böröczky), every tile of
  hyperbolic area 1, parent to child arcosh(3/2); ADR: the hyperbolic distance between standpoints, its unit along the
  height ln 2 a doubling.
- HOL and TWG: loops on the sphere and the hyperboloid come back turned by the enclosed area (Gauss–Bonnet), so
  ChatGPT's second suggestion is done; the cross ratio of four stars unmoved by boosts is in the archived OFS §7.8.
- The closed form for the Cauchy's KL divergence is cited by ChatGPT to Chyzak and Nielsen (2019); not checked here.

## Predictions

- **F1.** The Fisher information of C(m, γ) (one observation) is diag(1/(2γ²), 1/(2γ²)), the off-diagonal 0, by
  quadrature at (m, γ) = (0, 1), (3, 0.2), (−7, 40). Killed if any entry is off by more than 10⁻⁴⁰ (relative).
- **F2.** KL(z₁ ‖ z₂) by quadrature equals ln(((m₁ − m₂)² + (γ₁ + γ₂)²)/(4γ₁γ₂)), equals KL(z₂ ‖ z₁), and equals
  2·ln cosh(d/2), d the Poincaré distance (cosh d = 1 + |z₁ − z₂|²/(2γ₁γ₂)), for six pairs. Killed past 10⁻⁴⁰.
- **F3.** KL is unchanged when one real Möbius map g (ad − bc > 0) acts on both standpoints: scaling the world z ↦ kz
  (k = 10⁻³, 7, 10⁶), a shift, the exchange z ↦ −1/z and two general maps; by quadrature on C(g(z₁)), C(g(z₂)).
  So distinguishability passes the scale test. Killed past 10⁻⁴⁰.
- **F4.** At one foot, heights γ and rγ: d = |ln r|, KL = ln((1 + r)²/(4r)) = −2·ln sech(½ ln r), the same at r and
  1/r, 0 only at r = 1; so e^(−KL/2) = sech(½ ln r), the overlay's sech at half the ratio. Killed past 10⁻⁴⁰.
- **F5.** Stepping both standpoints back by the same height s (z ↦ z + is, the relay: C(z) convolved with C(is)) lowers
  KL and d strictly for every s > 0 (data processing), toward 0 as s → ∞, for four pairs and s = 10⁻³ … 10³. Killed if
  any step up is not a decrease, or KL(s = 10⁶) exceeds 10⁻⁶.
- **F6.** The sample median's large-n variance π²γ²/(4n) against the Cramér–Rao bound 2γ²/n: efficiency 8/π² = 0.81057
  exactly; seeded (n = 1001, 20,000 repeats, γ = 1) the median's n·variance within 3% of π²/4 and the maximum-likelihood
  estimate of m (Newton from the median, γ known) within 3% of 2. Killed outside 3%.
- **F7.** Fisher area is half the hyperbolic area: a dyadic cell [k, k + 1]·2^(−j) × [2^(−j−1), 2^(−j)] has Fisher area
  ½ at every j. Killed past 10⁻⁴⁰.

## What would follow, if nothing is killed (a reading, to Tom)

Distinguishability of two standpoints is a function of their hyperbolic distance and of nothing else, so it passes
both tests of *Reads and Writes* (no scale, no payload). But it is a quantity between two standpoints: it joins reads,
so by R651 it is the writer's, a write unmoved by scaling (as R657 says the scale test is necessary, not sufficient).
Along the height it is ln of a ratio of thumbs: the across axis of Euler's plane, the writer's count ln(d/H), is the
hyperbolic distance. The median, the reader's statistic, is 8/π² as efficient as the best the joined reads allow.

## Runs

### Run 1 (9 Nov, `python3 runs/frg/frg.py`, 16 s; output `runs/frg/frg-run1.txt`)

```
F1: not killed. I = diag(1/2γ², 1/2γ²), off-diagonal 0, worst 1.71e-51
F2: not killed. KL closed form, symmetric, = 2 ln cosh(d/2), six pairs, worst 1.27e-49
F3: not killed. KL unmoved by 7 real Möbius maps (scale the world among them), worst 5.67e-51
F4: not killed. one foot: d = |ln r|, KL = ln((1+r)²/4r) = −2 ln sech(½ ln r), r ↔ 1/r, worst 2.67e-51
F5: not killed. stepping back lowers KL and d at every step; KL at s = 10⁶ at most 4.21e-10; quadrature check 2.46e-50
F6: not killed. efficiency 8/π² = 0.810569; n·var(median) 2.4893 (π²/4 = 2.4674), n·var(MLE) 1.9982 (2), ratio 0.8027
F7: not killed. every dyadic cell's Fisher area ½, j = −3 … 10, worst 0.0
```

Nothing killed. ChatGPT's mathematics holds as stated: the metric, the curvature −2, the closed KL, its symmetry and
2·ln cosh(d/2). All of it is classical; what it adds here, read against *Reads and Writes*:

- **Known in another language.** The hyperbolic plane of standpoints was already the corpus's (ADR's distance, DYH's
  tiling, JAY's Fisher–Rao length of the facing, the Möbius closure). Fisher–Rao supplies a statistical name for that
  distance, not a new structure.
- **One distinction it sharpens.** Distinguishability is unmoved by every real Möbius map (F3), so it passes the scale
  test, yet it is a quantity of two standpoints: it joins reads, so it is a write (R651). It is an example for R657's
  "the scale test is necessary, not sufficient", with a number attached.
- **The writer's count is the distance.** At one foot the distance is |ln r| (F4): Euler's plane's across axis, ln(d/H),
  is the hyperbolic distance between the standpoints, and e^(−KL/2) = sech(½ ln r), the overlay's sech, at half the ratio.
- **The relay forgets.** Stepping back (a relay of heights, SUM) lowers the distance at every step (F5): standing higher
  makes standpoints harder to tell apart, the data processing inequality on the plane of standpoints.
- **What the median costs.** The median, the reader's order statistic, has 8/π² = 0.811 of the efficiency the joined
  reads allow (F6; seeded 0.803): to know more than the median gives, the reads must be joined by a likelihood, a write.

Proposed, not made: one sentence in *Reads and Writes* §2 (the standpoints' plane carries the Fisher metric, half the
Poincaré; distinguishability is invariant yet joins two reads); Tom's call. Made (Tom: "yes"): §2, "How far
apart two standpoints are".
