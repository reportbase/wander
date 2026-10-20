# LOM: looming read as a ratio — does the Cauchy reading say anything classical results do not?

*17 October 2026 (Tom's local date). Tom, 22:14: "how does cauchy fit in so fare?"; Claude: so far as the address
layer's bookkeeping (the sweep is the Cauchy wedge, each Lambert cell an equal piece of it, what is met moving only the
median of what is met), its tail unused because directions, not ratios, were averaged; it would bite where a reading is
a ratio with a noisy denominator. Tom, 22:17: "yes, focus on cauchy to see if our cauchy insights have anything new to
say about classical results." Predictions written before any code.*

## The question, stated plainly

SKY run 1 found τ read worst for bodies far from contact. τ = 2s/ṡ is the reciprocal of a noisy rate r = ṡ/(2s), as a
parallax distance is the reciprocal of a noisy angle. The corpus's Cauchy readings say: a ratio is an address; its median
is the reader's and commutes with every monotone map (OFS Theorem 6(c)), its mean is the payload's and does not; the
reciprocal-symmetric pair has a corner where the two part. Does that predict anything about reading τ that classical
statistics and vision do not already say? **My prediction: no.** Every result below is expected to be classical; the test
is whether the framing gets them right without being told, and whether it adds anything beyond them.

## Known beforehand (classical, and ours)

- The ratio of normal variables (Geary 1930; Marsaglia 1965; Hinkley 1969): approximately normal while the denominator's
  coefficient of variation is small (Geary's working condition, about ⅓ or less); otherwise a heavy, Cauchy-like tail. The
  reciprocal of a normal variable has no mean at all. The delta method: E[1/r̂] ≈ (1/r)(1 + CV²).
- Distances from noisy parallaxes (Lutz and Kelker 1973; Bailer-Jones 2015): do not invert a noisy parallax; the median
  survives the inversion. PXC run 4, P14 (`plans/pxc-plan.md`): the expected distance diverges, the median goes through.
- Looming (Lee 1976; Hoyle 1957): τ = θ/θ̇; in vision the expansion rate θ̇/θ (= 1/τ) is commonly used beside τ.
- The median of a sample commutes with every monotone map (the order statistic is equivariant): median(1/x) = 1/median(x)
  for an odd sample with no zero. OFS Theorem 6(c).
- SKY run 1: τ's error carried in proportion to |τ| by the cells' scatter.

## Set-up (simulation with real quantization, no added noise)

A smooth sphere of radius ½ (a Levels body without relief, so the only noise is the cells'), seen from home, its centre
starting in a random direction within 5° of (1, 1, 1) at distance 32 (angular radius about 20 cells: about 1,250 cells),
moving across the line of sight 5 cells a tick in a random direction (so the cells' errors decorrelate from tick to tick)
and radially at the speed that makes its true τ at the middle tick one of τ = 10, 30, 100, 300, 1,000, 3,000, 10,000 ticks
(approaching). The inscribed sweep: the Lambert grid of the whole wedge, 2048 × 2048 cells, a cell detected when its
middle's direction lies inside the sphere's cap (exact for a sphere). Five ticks t = −2 … 2 per repeat; the share s(t) from
the detections; the rate r̂ = ½ × the least-squares slope of ln s; τ̂ = 1/r̂. 4,000 independent repeats per τ (seeded),
and 40,000 for τ = 1,000 and 3,000. CV = sd(r̂)/r, measured.

### Predictions

- **L1 (Theorem 6(c), exact).** For every τ, over any odd number of repeats, median(τ̂) = 1/median(r̂) exactly (to rounding);
  mean(τ̂) ≠ 1/mean(r̂) once CV ≥ 0.05 (they differ by more than 10⁻⁴ relative). *Killed* if the median identity fails.
- **L2 (small CV: the delta method).** For every τ with CV ≤ 0.3: mean(τ̂)/τ − 1 within a factor 1.5 of CV² (or within 0.01 of
  it when CV² < 0.01); median(τ̂)/τ − 1 smaller in size than mean(τ̂)/τ − 1. *Killed* if either fails.
- **L3 (large CV: the tail).** For every τ with CV ≥ 1: at least 15% of τ̂ have the wrong sign (the body read as receding);
  the median of τ̂ within 25% of τ; the mean of τ̂ over the first 4,000 and over all 40,000 repeats (τ = 3,000) differing by
  more than three of the larger repeats' standard errors, or either being negative (it has not settled). *Killed* if any part
  fails, or if no τ reaches CV ≥ 1 (then I say so: untested).
- **L4 (the rate is the bounded reading).** r̂ is close to normal at every τ: its mean within 3 standard errors of the true
  rate 1/τ, and its sd the same at every τ within 20% (the cells' scatter does not depend on the rate). *Killed* if either
  fails.
- **L5 (the verdict).** Nothing in L1–L4 departs from the classical results above, and the Cauchy framing's one decision rule
  (read the time τ while CV < 1, the rate r past it; report the median of either, which is the same reading) is the
  classical advice (Bailer-Jones; the expansion-rate practice) restated. *Killed* if any result above departs from its
  classical expectation in a way the framing predicted and the classical results did not.

L1 is an identity; L2 and L3 are Geary and Lutz–Kelker on looming; L4 is the cells' scatter; L5 is the honest question.

## What would and would not be shown

Whether the Cauchy readings (median as the reader's, the reciprocal pair, the corner) predict τ's behaviour under real
quantization, and whether they add anything to the classical statistics of ratios. A "no" in L5 is a useful result: it
places the framing as a restatement here, not a discovery. Not a test of real vision or real tracking data.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (17 Oct, `node runs/lom/lom.mjs`; output `runs/lom/lom-run1.txt`, 40 s)

CV of the rate, by τ = 10 … 10,000: 0.003, 0.008, 0.027, 0.082, 0.256, 0.760, 2.553; the rate's sd the same at every τ
within 8% (2.5–2.7·10⁻⁴ a tick: the cells' scatter does not depend on the rate). All four of L1–L4 killed:
- **L1 killed** at τ = 1,000, 3,000 and 10,000: median(τ̂)·median(r̂) − 1 = 2·10⁻⁶, 0.13, 0.73. The reciprocal is monotone
  on each side of 0, not across it; where some r̂ are 0 (exactly: equal counts) or negative, the order is cut and the
  median does not go through. I wrote "no zero" among the known facts and left it out of L1.
- **L2 killed:** at τ = 10 the five-tick slope over a straight approach reads τ 1.15% short (my set-up: ln d is not
  linear in t; the slope carries (1/τ)(1 + 34/(30τ²)), 1.13% at τ = 10); at τ = 1,000 (CV 0.26) a repeat with r̂ = 0
  exactly makes mean(τ̂) infinite. The middle τ (30–300) follow the delta method (0.93% against CV² 0.67% at τ = 300).
- **L3 killed:** τ = 10,000 (CV 2.55) has 35% of τ̂ with the wrong sign, but the median of τ̂ is 73% short of τ (the
  negative readings sit below every positive one on the τ line); τ = 3,000 (CV 0.76) did not reach CV 1, so the settling
  clause was untested.
- **L4 killed** by my set-up at τ = 10 and 30 (r̂'s mean 278 and 9.9 standard errors off 1/τ, the t³ term above); its sd
  clause held (×1.08).

**Post hoc** (`runs/lom/lom1-posthoc.mjs`, output `runs/lom/lom1-posthoc.txt`): against the slope's own expectation r̂'s mean is
within 2 standard errors for τ ≥ 30 (6.6 at τ = 10, the next term); r̂ = 0 exactly in 0.17% (τ = 3,000) and 0.37%
(τ = 10,000) of repeats; and **1/median(r̂) reads τ to −0.12%, −2.4% and +2.5% at τ = 1,000, 3,000, 10,000**, where the
median of τ̂ is off −0.12%, −15% and −73%.

**L5 (the verdict), read against the classical results: not killed.** Everything above is classical: the reciprocal of a
noisy rate has no mean (r̂ reaches 0), the delta method's CV² bias, Geary's normal approximation failing as the denominator's
CV grows, and Bailer-Jones's advice (infer on the parallax, the rate, and flip). The corpus's framing gets each right, and
gives one way of saying why the median must be taken on the rate side: τ̂ and r̂ are one reading, the direction [r̂ : 1]
on the projective line, and the reciprocal is a turn of that circle. A turn keeps the circle's order but moves where the
circle is cut to make a line; a median goes through only if the cut falls outside the readings. On the rate's chart the
cut is at r = ∞ (τ = 0, never read); on τ's chart it is at τ = ∞ (r = 0), inside the readings once CV nears 1. That is
the address picture (a reading is a direction, R306; the horizon is where a chart is cut), and it is the classical advice
restated, not a new result.
