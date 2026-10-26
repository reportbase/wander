# CCA: canonical correlation, followed to its conclusion

26 Oct 2026. Tom: "what i want to do is do a deeper dive into a classical result that sees it as payloads, and follow
their logic all the way to their conclusion, about payloads, when it is actually addresses." After GRS (runs 1–4), whose
principal angles are, in statistics, the canonical correlations.

## The classical result, as it is stated

Hotelling (1936); Anderson, *An Introduction to Multivariate Statistical Analysis* (3rd ed. 2003), ch. 12.

1. Two sets of variables, x (p of them) and y (q), with covariances Σ₁₁, Σ₂₂, Σ₁₂. The **canonical correlations**
   ρ₁ ≥ … ≥ ρ_min(p,q) are the square roots of the eigenvalues of Σ₁₁⁻¹Σ₁₂Σ₂₂⁻¹Σ₂₁: the largest correlation between a
   linear combination of x and one of y, then the largest uncorrelated with those, and so on. Read as **the strength of
   the linear association** between the sets.
2. From N observations the sample canonical correlations r_i, the same formula on the sample covariances.
3. Independence, H₀: Σ₁₂ = 0. The likelihood ratio is **Wilks' Λ** = ∏(1 − r_i²) (Wilks 1932, 1935); Bartlett (1938,
   1941): −(N − 1 − (p + q + 1)/2)·ln Λ is about χ² with pq degrees of freedom.
4. Rejecting H₀, the analyst reports the first canonical pair as associated with strength r₁, and r₁² as **the share of
   variance the pair has in common** ("shared variance"; redundancy indices build on it). The conclusion is about the
   data's amounts: how much of one set's variance the other carries.

## The same computation, read as addresses

Centre the data. The N observations of the p x-variables are p vectors in ℝ^N, lying in the (N − 1)-dimensional space
orthogonal to (1, …, 1); they span a p-plane there, and the y-variables a q-plane. The sample canonical correlations are
**the cosines of the principal angles between the two planes** (Björck and Golub 1973): r_i = cos θ_i. So:

- Any invertible change of the x-variables among themselves (units, scalings, mixing: X ↦ XA) leaves their plane where it
  was, and the same for y. The amounts (each variable's size, the within-set covariances Σ₁₁, Σ₂₂) cancel from every
  r_i: the r_i are directions, a point of a Grassmannian, never amounts. (Classically: the r_i are the maximal invariants
  under GL(p) × GL(q); Anderson §12.2.)
- r_i² = cos² θ_i is the foot of the projection: the share of a unit vector's length that lies on the other plane, a
  share of 1, the h² of OFS §4. "Shared variance" names this foot as a share of the data's variance.
- Under H₀ with Gaussian data, the y-plane is uniform on Gr(q, N − 1) whatever x's plane is: the null law of the r_i is
  the uniform turn's measure on the Grassmannian, the addresses alone, depending on (N − 1, p, q) only.
- The population ρ_i are likewise the cosines of the principal angles between the spans of x's and y's components in the
  space of random variables (L²): "the strength of association" is an angle.

Known beforehand: Björck and Golub (1973) for the angles; the invariance and the null distribution's dependence on
(N, p, q) alone (Anderson ch. 12); Bartlett's χ²; that sample canonical correlations are biased upward and reach 1 when
p + q ≥ N − 1 (any multivariate text). GRS runs 1–4 for the Grassmannian's numbers. What is ours is the reading: which
step is address and which payload, and what the chain's conclusion is when the r_i are read as addresses. draw's labs
were not checked (the draw repository is not in this session); none is about canonical correlation as far as CLAUDE.md
lists them.

## Set-up

`runs/cca/cca.py`, numpy, seeded. Data X (N × p) and Y (N × q), centred; r_i the singular values of Q_xᵀQ_y (Q from the
QR of each centred block), which is the textbook computation. Monte Carlo of 200,000 datasets where a law is compared;
tolerances 4 standard errors.

## Predictions (written before any script)

- **C1 (the amounts cancel).** For random invertible A (p × p), B (q × q), any shift of each column, the r_i of (XA + 1a,
  YB + 1b) equal those of (X, Y) to 10⁻⁹, on 1,000 random datasets. Kill: any differ by more.
- **C2 (no association is the uniform Grassmannian).** Under H₀, with N = 2k + 1, p = q = k and two very different
  within-set covariances (identity, and one with eigenvalues spread over 10⁴), the count of r_i ≥ 1/√2 (θ_i ≤ 45°, inside
  the corner) follows GRS run 3's exact law for k = 2, 3 (½ − π/8, π/4, ½ − π/8; (π − 3)/4π, (π + 3)/4π, …). Kill: any
  frequency outside 4 SE.
- **C3 (pure noise reads as shared variance).** Under H₀ with N = 2k + 1, p = q = k: P(r₁² ≥ ½), the chance the first
  canonical pair "shares more than half its variance" with no association at all, is 1 − P(none inside) = ½, 0.8927,
  0.98873, 0.99941 for k = 1, 2, 3, 4. Kill: outside 4 SE.
- **C4 (the corner of Wilks' Λ is the exchange's).** With N − 1 = 2k, p = q = k: ∏ tan θ_i ≤ 1, that is
  Λ = ∏(1 − r_i²) ≤ ∏ r_i², has probability exactly ½ under H₀ (k = 1 … 4). With N − 1 = 2k + 1 it does not: ¼ at k = 2
  (Gr(2, 5)), 0.228 at k = 3. Kill: outside 4 SE of these.
- **C5 (a forced fit is geometry).** When p + q > N − 1, exactly p + q − (N − 1) of the r_i equal 1 (to 10⁻⁹) in every
  dataset, with or without association: two planes in too small a space must meet. Kill: any dataset otherwise.
- **C6 (association is an angle too).** Under H₁ with population canonical correlations ρ = (0.8, 0.3), p = q = 2,
  N = 30, the law of (r₁, r₂) is the same for two very different (Σ₁₁, Σ₂₂) with those ρ (KS p > 0.001 on r₁ and r₂,
  50,000 each) and different for ρ = (0.6, 0.3) (KS p < 10⁻⁶). Kill: either fails.
- **C7 (Bartlett's χ² is the near-horizon chart).** Under H₀ with N − 1 ≫ p + q, the planes sit near the horizon
  (θ_i → 90°, r_i → 0), and (N − 1)·Σ r_i² = (N − 1)·Σ cot² θ_i (to first order) follows χ²_pq: at N = 2,001, p = 3,
  q = 4, KS against χ²₁₂ p > 0.001. Kill: below.

## Not claimed

Nothing about any study that used canonical correlation, and nothing about the field (R364): the classical computation is
right, and its null distribution is the right one. The question is only what the numbers are: amounts or directions.

## Runs

### Run 1 (26 Oct; `runs/cca/cca.py`, output `runs/cca/cca-run1.txt`, 37 s)

- **C1 killed, by my set-up.** The largest change in any r_i under X ↦ XA + shift, Y ↦ YB + shift was 6.8·10⁻⁹, over my
  10⁻⁹: the transforms had column scales from 10⁻³ to 10³ and shifts of 10³, so double precision loses up to about
  10⁻¹⁶ times their condition. Not a change in the r_i; a test of the arithmetic. C1′ below.
- **C2 not killed.** With no association and N = 2k + 1, the count of r_i ≥ 1/√2 follows the uniform Grassmannian's
  exact law at k = 2 and 3, the same with identity covariances and with eigenvalues spread over 10⁴ (every |z| < 1.7).
- **C3 not killed.** With no association, P(r₁² ≥ ½) is 0.4994, 0.8930, 0.9886, 0.99948 for k = 1 … 4 (N = 3, 5, 7, 9),
  against 1 − P(none inside) = ½, 0.8927, 0.98873, 0.99941. Seven observations of three and three noise variables report a
  first pair "sharing more than half its variance" 98.9% of the time.
- **C4 not killed.** P(Λ ≤ ∏ r²) = 0.5003, 0.4991, 0.4979, 0.5010 for N − 1 = 2, 4, 6, 8 (the exchange); 0.2501 for
  N − 1 = 5, k = 2 (Gr(2, 5)'s ¼); 0.2267 for N − 1 = 7, k = 3 (run 2's 0.228, itself a Monte Carlo value).
- **C5 not killed.** p + q − (N − 1) of the r_i are 1 in every dataset, with or without association, in all four shapes.
- **C6 not killed.** With ρ = (0.8, 0.3), identity and spread covariances give one law (KS p 0.957 on r₁, 0.444 on r₂;
  medians 0.8223 and 0.8222); ρ₁ = 0.6 another (p < 10⁻³⁰⁰, median 0.6549).
- **C7 not killed.** At N = 2,001 the angles sit at 82.7° … 90.0°, median 87.9°: random planes in a large space are
  nearly perpendicular, at the horizon of the reading; (N − 1)·Σ r² against χ²₁₂ KS p 0.701, mean 11.954.

### C1′: predictions (written before the run-2 script)

- **C1′.** In 60-digit arithmetic (mpmath), the same 1,000 kinds of transform (column scales 10⁻³ … 10³, shifts 10³)
  change no r_i by more than 10⁻⁴⁰. Kill: more.
