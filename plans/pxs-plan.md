# PXS: parallax as a sum of reads

*2 November 2026 (Tom's local date), SPN R628.*

*Tom: "I wonder if parallax has a tighter cauchy connection? It connects two or more reads." Claude answered that parallax
combines two reads by the operations the Cauchy family is closed under (a sum of cotangents, then a reciprocal), and
offered a plan. Tom: "Yes".*

*Exact where a closed form exists (mpmath), seeded samples elsewhere (numpy, 10⁶ draws), thresholds in standard errors or
stated below. Scripts in `runs/pxs/`. Nothing is run before this plan is committed.*

## Known beforehand

- **Triangulation.** Two directions and a baseline place a point; the baseline is the one carried-in length (Snellius,
  Roy; *Reads and Writes* §8). With standpoints A = (−1, 0) and B = (1, 0) (half-baseline b = 1) and a target at (x, d),
  the interior angles α_A, α_B to the baseline have cot α_A = (x + 1)/d and cot α_B = (1 − x)/d, so
  - cot α_A + cot α_B = 2/d (the depth is the reciprocal of a sum of two reads, each in its h/v chart);
  - x = (cot α_A − cot α_B)/(cot α_A + cot α_B).
- **The Cauchy family under real Möbius maps** (McCullagh 1996). If X ~ Cauchy(z), z = m + iγ in the upper half-plane,
  then (aX + b)/(cX + d) ~ Cauchy((az + b)/(cz + d)) when ad − bc > 0, and Cauchy of the conjugate image when ad − bc < 0.
  Independent Cauchys add their points z (Lévy; SUM).
- **TRI** (`plans/tri-plan.md`), the same set-up: reads from a height γ, the angular error δ with tan δ ~ Cauchy(0, γ).
  - Run 1, T1: the relative depth error is Cauchy(0, 2γ·cosh(ln k)) on the bisector, k = d/b, **to first order**, tested
    at γ = 10⁻⁴; least at the pair's corner (PXC's bell).
  - Two standpoints' scales add linearly; averaging does not narrow them; rays that do not meet ahead are a visible share.
- **SUM** (`plans/sum-plan.md`): a sum of Cauchys is a relay of standpoints, the points m + iγ adding; the mean of n
  standard Cauchys is a standard Cauchy.
- **PXC** run 4, P14: a noisy parallax's inverse has no mean and keeps its median.
- **draw's labs.** UDV: three standpoints give a figure up to size, one agreed length the size. Two- and three-reader
  tests (`labs/two-reader-tests.js`, `labs/three-reader-tests.js`).

What is not known beforehand, as far as I know in this corpus: that under TRI's error model the depth is **exactly** a
Cauchy at every γ, with a point found by doing the triangulation on the reads' complex points; and what that point is at
the corner.

## The reading, before the run

A read under a uniform turn from a height is a Cauchy in its slope chart. Turning a direction by a known angle is a real
Möbius map of that chart, and so is passing to the other chart (the exchange). Parallax then does two things: it adds two
reads (in the cot chart) and takes a reciprocal. Every step stays in the family. So the depth is not merely Cauchy to first
order; it is a Cauchy exactly, and its point is the triangulation carried out on the reads' points instead of their values:
the standpoints compose, as in SUM, and the composite is one standpoint again.

Worked out before the run. Write c = cot α (the true read in the cot chart) and t = tan δ ~ Cauchy(iγ).

- cot(α + δ) = (c − t)/(1 + ct). As a map of t this has determinant −(1 + c²) < 0, so cot(α + δ) is Cauchy at the
  conjugate image of iγ, which works out to

      w(c) = (c + iγ)/(1 − iγc).

  (At γ → 0, w = c.)
- The sum Ŝ = ĉ_A + ĉ_B is Cauchy(w_A + w_B), the reads independent.
- The depth d̂ = 2/Ŝ: the map s ↦ 2/s has determinant −2 < 0, so d̂ ~ Cauchy(D) with

      D = 2 / conj(w_A + w_B).

  Its centre Re D is the depth's median; its scale Im D the depth's half-interquartile range. "No forward crossing"
  (d̂ < 0) is part of the same law: P = ½ − (1/π)·atan(Re D/Im D).
- **At the corner** (on the bisector, k = 1, c_A = c_B = 1): w = (1 + iγ)/(1 − iγ) = e^{2iφ}, φ = atan γ, so
  D = e^{2iφ} = d·e^{2iφ}. The depth's point sits on the circle of radius d, turned by **twice** the read's error angle,
  the facing (2θ) of the read's height. Its median is d·cos 2φ, a little short; its scale d·sin 2φ.
- **Off the corner** on the bisector (c = 1/k), |w| = √(1 + k²γ²)/√(k² + γ²), which is 1/k only at k = 1. So |D| = d
  only at the corner.
- **The place** x̂ = (ĉ_A − ĉ_B)/(ĉ_A + ĉ_B) is a ratio of two dependent sums, not one Möbius map of one Cauchy. I expect
  it to be Cauchy to first order only.

## Predictions

**X1 (the depth is exactly a Cauchy).** At γ ∈ {10⁻³, 0.1, 0.3} and targets (x, d) ∈ {(0, 1/8), (0, 1/2), (0, 1), (0, 2),
(0, 8), (0.6, 1.5), (−2, 3)} (seeded, 10⁶ draws each, d̂ taken from the crossed rays, no forward crossing kept as a
negative or infinite d̂):
- the Kolmogorov–Smirnov distance of d̂ to Cauchy(D), D from the formula above, is under 0.002;
- the share with d̂ < 0 is within 3 standard errors of ½ − (1/π)·atan(Re D/Im D).
- *Killed* if any case fails.

**X2 (first order is only first order).** At γ = 0.3 on the bisector at k = 1 and 8:
- the KS distance of the relative error (d̂ − d)/d to TRI's Cauchy(0, 2γ·cosh(ln k)) exceeds 0.01;
- at γ = 10⁻³ it is under 0.002.
- *Killed* if the first-order law is as good as the exact one at γ = 0.3.

**X3 (the corner keeps the distance).** Exactly (mpmath, 50 digits): |D| = d at k = 1 for γ ∈ {10⁻³, 0.1, 0.3, 1, 3},
and arg D = 2·atan γ; at k ∈ {1/8, 1/2, 2, 8} and γ = 0.3, |D| ≠ d by more than 10⁻³ of d.
- *Killed* if |D| = d off the corner, or not at it.

**X4 (the median and the mean).** For n independent repeats of the pair's reads at γ = 0.1, k = 1, n ∈ {1, 10, 100}
(10⁵ sets each):
- the mean of the n reciprocal depths 1/d̂ has half-interquartile range within 0.01 (relative) of Im of the n = 1 law of
  1/d̂ at every n: averaging gains nothing;
- the median of the n depths narrows, its half-interquartile range at n = 100 under a fifth of the n = 1 value.
- *Killed* if the mean narrows or the median does not.

**X5 (two uniform half turns).** Each standpoint turns uniformly over (0, π) from the baseline, independently (seeded,
10⁶ pairs): cot of each is a standard Cauchy, the sum Cauchy(2i), so d/b is exactly a standard Cauchy:
- the share crossing ahead is within 3 standard errors of ½;
- the crossings ahead have median depth within 0.005 of b, the half-baseline: the pair's corner;
- the KS distance of d/b to the standard Cauchy is under 0.002.
- *Killed* if any fails.

**X6 (two quarter turns are not closed).** Each standpoint turns uniformly over (0, π/2) only, so every pair crosses ahead
(seeded, 10⁶ pairs). The sum of two half-Cauchys is not a half-Cauchy:
- the KS distance of d/b to the half-Cauchy with the same median exceeds 0.01.
- *Killed* if it is under 0.01. (Less certain than X1–X5: I have not worked out the sum's law.)

**X7 (the place is Cauchy to first order only).** At k = 1 on the bisector, x̂ against the Cauchy fitted by its quartiles:
- KS distance under 0.002 at γ = 10⁻³;
- over 0.005 at γ = 0.3.
- *Killed* in its second clause if x̂ is as Cauchy at 0.3 as at 10⁻³ (then the place closes too, and I am wrong about it).
  Less certain than X1–X5.

**X8 (the verdict).** A judgment: if X1–X5 stand, parallax is the Cauchy's own composition carried out across two
standpoints. Each read is a standpoint's point; the triangulation done on the points gives the depth's point exactly; the
step between the standpoints is the one amount. A third standpoint enters only through another pair, and averaging the
pairs' depths gains nothing while their median does.
- *Killed* if X1 fails (then the closure holds only to first order, which TRI already showed).

## What would and would not be shown

- Shown, if not killed: the exact law of a triangulated depth under Cauchy read errors, and its point as the triangulation
  of the reads' points. Classical pieces (Möbius closure, Lévy's sum); the statement of parallax as that composition is
  ours.
- Not shown: anything about real instruments' errors (BER found a narrow core and wrong matches), or about the place
  across the line of sight beyond first order, or about three standpoints solved together by least squares.

## Runs
