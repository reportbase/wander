# WVP: the exterior reader's pattern built by the interior reader's arrivals

*15 October 2026 (Tom's local date). Tom, about 15:45: "exterior - wave like,   interior - particle liike" (SPN R270),
then "yes" to a plan with its predictions first.*

## The claim

R270 reads the exterior reader as wave-like: it holds one facing whole, a pattern, and reads it in squares at twice the
angle (R265). The interior reader is particle-like: it takes arrivals one direction at a time from home, each at one
address. With R267 (the payload is a wave of some kind) both read one payload. If so, the interior reader's arrivals,
counted, must build the exterior reader's pattern, and the way they converge is fixed by the geometry alone.

Everything below is in unit relations. Each arrival is one direction θ of the facing, drawn evenly on [0, π/2] (the even
turn, OFS §7.1), read as s = v/h = tan θ and as the square h² = cos²θ. No amounts, so no bridge is needed. The exterior
reader's pattern is the law itself: the readings half-Cauchy, the squares the arcsine law (OFS §3.4; JAY P2). This is a
simulation of our own checked against that law, not real data; it tests whether the reading is consistent, not physics.
A real-data follow-up (single-photon counts building an interference pattern) is named at the end, not run.

## Predictions (written before any run)

N is the number of arrivals; each estimate below is taken over 400 seeded runs (numpy, seeds 0–399), at
N = 10², 10³, 10⁴, 10⁵.

- **P1. The pattern is built at the rate √N.** The largest gap between the interior's counted shares (the empirical law
  of θ) and the exterior's pattern, the Kolmogorov distance D_N, has mean falling as N^(−1/2): the fitted slope of
  log mean D_N against log N is −0.50. *Killed if* the slope is outside [−0.55, −0.45], or √N·mean D_N at N = 10⁵ is
  outside 0.869 ± 0.05 (Kolmogorov's mean, √(π/2)·ln 2).
- **P2. The corner is found by count, with spread π/2 per √N.** The median of the arrivals' levels, ln s, sits at the
  corner, 0, and its spread across runs is (π/2)/√N: the density of ln s at 0 is 1/π, so the median's standard error is
  1/(2·(1/π)·√N). The exterior reading, π/2, sets how fast the interior finds the corner. *Killed if* the mean median
  is off 0 by more than 3 standard errors at any N, or √N × the spread is outside π/2 ± 5% at N ≥ 10³.
- **P3. The mean never settles; it climbs 2/π·ln 10 a decade.** The running mean of the readings s does not converge:
  its median across runs grows by (2/π)·ln 10 = 1.466 per tenfold N (the half-Cauchy's truncated mean, (2/π)·ln N + c).
  The interior reading, 2/π, sets the climb. *Killed if* any decade's step in the median of the mean is outside
  1.466 ± 0.15, or the spread of the mean across runs (its interquartile range) shrinks by more than a factor 2 from
  N = 10² to 10⁵ (a settling mean would shrink it by √1000 ≈ 32).
- **P4. In squares, the arcsine pattern and its middle.** The arrivals' squares h² average ½ (the corner's square) and
  the share with h² ≤ ¼ is (2/π)·arcsin(½) = ⅓. *Killed if* at N = 10⁵ the mean over runs of either is off by more than
  4 standard errors of that mean (σ/√(400·N), with σ² = ⅛ for h² and σ² = 2/9 for the share).
- **P5. The two readers' product.** The exterior holds the pattern whole and reads the arc over its line, π/2; the
  interior's arrivals give the mean shadow, the average of cos θ, which settles (it is bounded) at 2/π; the product of
  π/2 and the interior's counted mean shadow tends to 1 at rate N^(−1/2). *Killed if* at N = 10⁵ the mean over runs of
  (π/2)·(mean of cos θ) is off 1 by more than 4 standard errors (σ_cos = √(½ − 4/π²)).

What a kill would mean: P1, P4 and P5 are ordinary laws of large numbers and would fail only by my set-up; P2 and P3
are the claims that the exterior reading and the interior reading set the interior reader's convergence (π/2 the
spread of the corner's estimate, 2/π the mean's climb). Those two are the content.

## Runs

