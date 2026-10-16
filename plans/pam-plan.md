# PAM: the payload's mean and the addresses' median, kept apart

*15 October 2026 (Tom's local date). Tom, about 23:00: "4", choosing from Claude's list the exact test of R271 and R272
(the central sweep gets the payloads, read by their mean; the inscribed sweep gets the addresses, read by their median),
narrowed by R275 (a density that varies) and R277 (the normal payload a model under two premises).*

## The claim

Two things are read over one facing, and they answer to different laws:
- **The addresses.** The inscribed sweep's directions θ, read as s = v/h = tan θ, weighted by the density ρ(θ) of
  arrivals there. Their median sits at the corner, s = 1, whenever ρ weighs alike on both sides of it,
  ρ(θ) = ρ(π/2 − θ). This holds whatever the payload's law (OFS Theorem 6(e) with R275). They have no mean when ρ reaches
  the horizon, ρ(π/2) > 0.
- **The payloads.** The central sweep's values at each address, such as a relief's radius r(θ) = 1 + p(θ). Their mean is
  the average perturbation from the unit circle. Built from many independent components, the perturbation is close to
  normal by the central limit theorem for sums, whatever the components' own law (the premise R277 names).

The test checks that each holds, and that neither depends on the other: the median follows from ρ's symmetry alone, the
mean from the payload alone. Exact quadrature (mpmath, 30 digits) for A1–A3; a seeded simulation for A4. Unit relations
throughout: no amounts and no bridge.

## Predictions (written 15 Oct about 23:05, before any run)

Weights on [0, π/2]:
- (i) ρ = 1, the even turn;
- (ii) 1 + ½·cos 4θ, symmetric;
- (iii) a seeded random relief, symmetrised: ρ = ½(r(θ) + r(π/2 − θ)), with r = 1 + Σ_{n=1}^{12} c_n·cos(nθ + φ_n),
  c_n = 0.3/n and φ_n from numpy seed 7;
- (iv) (2 + cos 2θ)/3, not symmetric;
- (v) the same relief r itself, not symmetrised;
- (vi) sin² 2θ, symmetric and vanishing at the horizon.

- **A1. The symmetric weights put the median at the corner.** For (i), (ii), (iii) and (vi), the θ that halves ∫ρ is π/4
  to 10⁻²⁰, so the median of s is 1. *Killed if* any is off π/4 by more than 10⁻²⁰.
- **A2. The others move it, by the payload's weight alone.** For (iv) the median direction is 32.103° (known beforehand:
  the root of 2θ + ½ sin 2θ = π/2, given in OFS after Proposition 5(d)). For (v) it is off 45° by more than 0.1°, toward
  the side where r is larger, so its median reading s_m ≠ 1. *Killed if* (iv) is off 32.103° by more than 0.001°, or (v)
  is within 0.1° of 45°, or on the side where r is smaller.
- **A3. No mean where the weight reaches the horizon.** The mean of s truncated at S climbs (2/π)·(ρ(π/2)/ρ̄)·ln 10 per
  tenfold S, with ρ̄ the mean of ρ over [0, π/2]: 1.4659 for (i), 2.1988 for (ii) (ρ(π/2) = 3/2, ρ̄ = 1) and 0.7329 for
  (iv) (ρ(π/2) = 1/3, ρ̄ = 2/3). For (vi) the mean is finite: 4/π. *Killed if* the climb from S = 10⁶ to 10⁷ is off its
  value by more than 10⁻⁵, or (vi)'s mean is off 4/π by more than 10⁻²⁰.
- **A4. The payload's own law: normal by sums, whatever the components'.** At a fixed direction, the perturbation of a
  relief with K harmonics, p = Σ_{n=1}^{K} (a_n cos nθ + b_n sin nθ), has a_n and b_n independent and uniform on
  (−1, 1). Standardised by its exact variance K/3, it tends to the normal. Its Kolmogorov distance from N(0, 1), over
  2,000,000 seeded reliefs (seed 11) at θ = 0.3, is:
  - at most 0.03/K + 0.003 for K = 1, 2, 4, …, 64 (the 1/√K term of the Edgeworth series vanishes for symmetric
    components, so the leading error is in 1/K, plus sampling noise of about 0.0006);
  - more than 0.01 at K = 1, a single uniform pair, which is not normal.

  The mean of p over the full turn is 0 for every relief, to rounding: the average perturbation from the unit circle.
  *Killed if* any bound fails, or the full-turn mean exceeds 10⁻¹².

What a kill would mean:
- A1 or A3: OFS Theorem 6(e) or R275 is wrong as stated.
- A2: the median does not follow the payload's weight as R275 says.
- A4: the central limit theorem, as I have stated it, does not cover this payload. That would be my bound or my set-up,
  since the theorem itself is settled.

None of this is new mathematics. The test keeps the two readings apart on one example family.

## Runs

### Run 1 (15 Oct about 23:10, `pam/pam.py`, output in `pam/run1.txt`; 23 s)

- **A1 not killed.** For (i), (ii), (iii) and (vi) the median direction is π/4 to 4·10⁻³², so s_m = 1.
- **A2 not killed.**
  - (iv): 32.1031895°.
  - (v), the unsymmetrised relief: 47.128°, s_m = 1.0772. Its weight is 0.794 below 45° and 0.887 above, so the
    median moved toward the heavier side.
- **A3 not killed.** The climbs from 10⁶ to 10⁷ match their predictions to all twelve printed digits: 1.46587119776,
  2.19880679664 and 0.73293559888. (vi)'s mean is 4/π to 25 digits.
- **A4 killed, by my bound.** The Kolmogorov distances for K = 1 to 64 were 0.04689, 0.01109, 0.00518, 0.00256,
  0.00169, 0.00084 and 0.00085. K = 1 is past 0.033. The rest halve with each doubling of K down to the sampling floor
  (about 0.0006), as a 1/K law does. Post hoc: my constant, 0.03, was a guess, not derived. At K = 1 the pair's weights
  (cos 0.3, sin 0.3) are unequal, and the sum is nearly one uniform.

### Run 2, A4′ (prediction written 15 Oct about 23:15, before running)

From the Edgeworth series for a symmetric sum, F(z) − Φ(z) ≈ −(κ₄/24)·φ(z)·(z³ − 3z). Here κ₄ is the standardised excess
kurtosis of p: Σ_n (cos⁴ nθ + sin⁴ nθ)·(−2/15)/(K/3)², since a uniform on (−1, 1) has variance 1/3 and fourth cumulant
−2/15. The largest |φ(z)(z³ − 3z)| is 0.5506, at z = 0.742. So the predicted distance is (|κ₄|/24)·0.5506 at θ = 0.3:
- 0.00968 for K = 2;
- 0.00465 for K = 4;
- 0.00246 for K = 8;
- 0.00130 for K = 16;
- 0.00065 for K = 32;
- 0.00032 for K = 64.

**A4′.** A fresh sample, numpy seed 12, of 2,000,000 reliefs at θ = 0.3. *Killed if*, for K = 2, 4 or 8, the measured
distance is off its prediction by more than 25% of it plus 0.001; or, for K = 16, 32 or 64, it exceeds the prediction
by more than 0.0015 (where sampling dominates). K = 1 is outside the series' reach and has no prediction.
