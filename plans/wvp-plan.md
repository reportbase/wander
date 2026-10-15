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

### Run 1 (15 Oct, `wvp/wvp.py`, output in `wvp/run1.txt`; 4 s)

| N | √N·mean D | median ln s | √N·sd of median | median of mean s | IQR of mean s | mean h² | share h² ≤ ¼ | (π/2)·mean shadow |
|---|---|---|---|---|---|---|---|---|
| 10² | 0.8656 | +0.0106 | 1.5881 | 3.583 | 2.284 | 0.49776 | 0.33355 | 0.99800 |
| 10³ | 0.8454 | −0.0018 | 1.5587 | 5.541 | 3.559 | 0.50049 | 0.33251 | 1.00067 |
| 10⁴ | 0.8514 | −0.0005 | 1.5139 | 6.784 | 2.986 | 0.50014 | 0.33310 | 1.00018 |
| 10⁵ | 0.8537 | −0.0001 | 1.5012 | 8.344 | 3.358 | 0.50003 | 0.33323 | 1.00003 |

- **P1 not killed.** Slope −0.5015; √N·mean D at 10⁵ 0.8537 against 0.8687 (inside ± 0.05).
- **P2 not killed.** The medians sit at the corner within 3 standard errors at every N; √N × their spread 1.559,
  1.514, 1.501 against π/2 = 1.571 (inside 5%; the last is 4.4% low).
- **P3 killed.** The mean did not settle (its interquartile range across runs grew, ×1/0.68 from 10² to 10⁵, where a
  settling mean would shrink it 32-fold), but the decade steps of its median were 1.958, 1.243 and 1.560 against
  1.466 ± 0.15: two outside. Over the three decades the climb averages 1.587 a decade, 8% above (2/π)·ln 10. Post hoc,
  my set-up: the median over 400 runs of a quantity whose spread across runs is about 3 carries a standard error near
  0.2 by itself, so a ±0.15 band on each step was narrower than the noise I chose. The climb's size is not tested by
  this run.
- **P4 not killed.** Mean h² off ½ by 0.55 standard errors; the share with h² ≤ ¼ off ⅓ by 1.36.
- **P5 not killed.** (π/2)·mean shadow off 1 by 0.41 standard errors at 10⁵.

### Run 2, P3′ (prediction written before running)

The climb of the mean, with the noise counted. **P3′.** With 4,000 seeded runs per N (seeds 10,000–13,999) at
N = 10², 10³, 10⁴, 10⁵, the median across runs of the running mean of s climbs (2/π)·ln 10 = 1.466 a decade on
average over the three decades, (median at 10⁵ − median at 10²)/3. Its standard error is taken from 1,000 bootstrap
resamples of the runs. *Killed if* the average climb is off 1.466 by more than 3 bootstrap standard errors, or the
interquartile range of the mean across runs shrinks by more than a factor 2 from 10² to 10⁵.

### Run 2 (15 Oct, `wvp/wvp2.py`, output in `wvp/run2.txt`; 5 s)

The median of the mean across 4,000 runs: 3.7919 at N = 10², 8.0673 at 10⁵. Average climb 1.4252 a decade against
(2/π)·ln 10 = 1.4659, bootstrap standard error 0.0165: off by 2.47 standard errors, inside 3. The interquartile range of
the mean across runs 2.962 at 10², 2.893 at 10⁵ (×1.02: it does not shrink). **P3′ not killed**, close to its edge.

## What it shows

On the even turn, the interior reader's arrivals, counted, build the exterior reader's pattern: the law of the
directions at the rate √N (P1), the squares' arcsine law and its middle (P4), the mean shadow 2/π, whose product with
the exterior's π/2 tends to 1 (P5). The two vantages' numbers set how the interior converges: the corner is found by
count with spread (π/2)/√N in levels (P2), and the mean of the readings never settles but climbs (2/π)·ln 10 a decade
(P3′; P3 killed by my tolerance). So the reading of R270 is consistent: one payload, held whole as a pattern by the
exterior reader, met one arrival at a time by the interior reader, which reaches the pattern's shares and its corner
but never a mean. This is a simulation of our own on a law chosen beforehand; it says nothing yet about physical
waves or particles.

**Next, not run.** Real data: published single-photon (or single-electron) build-ups of an interference pattern, where
counted arrivals are recorded one by one (Tonomura et al. 1989; Aspect, Grangier and Roger's single-photon experiments).
The prediction to write first: the counted pattern's Kolmogorov gap falls as N^(−1/2), and the pattern's own corner (in
whatever pair is named) is found by count with the spread its density sets. The bridge (counts and positions in amounts)
must be named before it is run.
