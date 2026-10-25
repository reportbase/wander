# SKT: the reader's data structure, measured

*25 October 2026. Tom: "what data structure is best fit for situated reader and unsituated writer", then "yes,write the
plan" to a measurement of the reader's column. Exact where it can be (the index maps), seeded simulation for the rest;
no physics, no page.*

## The claim, before any run

The writer's structure is a dense array indexed by amount over a known extent: ⌊N·x/X⌋, needing X. The reader's
structures, built in different fields for their own reasons, are claimed to be one design: a fixed number K of cells,
indexed by a monotone function of x/H, ⌊K·F(x/H)⌋, needing only H (a zoom), with order kept per cell (counts, ranks,
medians), never the extent. They differ only in F:
- **the turn**, F = (2/π)·arctan: bounded at both ends, every x > 0 held, the corner at x = H, cells the half-Cauchy's
  quantiles (OFS §7.3, "Laid on the sweeps");
- **the reader's lay**, proportional up to H, then 1 + ln(x/H): the near field absolute, the far relative (OFS §8);
  in base 2 with linear steps inside each doubling it is the floating-point layout and HdrHistogram's;
- **the logarithm** (DDSketch): relative everywhere, no corner, unbounded at both ends, so a fixed K must collapse an end.

If the claim holds, each column's behaviour follows from its F: where it is fine, where it gives out, what scaling the
world does to it, and where the best H is. If it fails, the structures are a family only by analogy.

## Known beforehand

Classical or ours already, not tested as new:
- Quantile sketches: DDSketch (Masson, Rim and Lee 2019, relative error α from buckets ⌈log_γ x⌉, γ = (1 + α)/(1 − α),
  collapsing the lowest buckets past a limit); HdrHistogram (Tene: power-of-two buckets of S linear sub-buckets, a lowest
  discernible value); t-digest (Dunning: its k₁ scale function (δ/2π)·arcsin(2q − 1), an angle on the quantile, finer at
  the tails); KLL (Karnin, Lang and Liberty 2016); Greenwald and Khanna 2001.
- μ-law and A-law companding (ITU-T G.711): linear near zero, logarithmic beyond. A-law is the reader's lay's shape in
  telephony.
- DPR (`plans/dpr-plan.md`): a binary32 float is a reader's lay in base 2, subnormals the proportional part, 2²³ addresses
  a level; the depth buffer the in-place lay.
- The turn index and its cells: `array-sweeps.html`, OFS §7.3; Boyd's rational Chebyshev points, OFS §8.
- Computed beforehand by Claude, so not predictions:
  - A cell of the turn at s = x/H is (π/2K)·(1 + s²) wide in s, so (π/2K)·(s + 1/s) relative: least at the corner,
    π/K = 0.0123 at K = 256, and the same at s and 1/s.
  - DDSketch with K = 256 buckets spanning 12 decades has ln γ = 0.1079 (α = 0.0539) everywhere.
  - The turn is finer than it near the corner by 8.8 times, and coarser past s ≈ 17.5 or under 1/17.5 (1.24 decades
    either side).
  - log₂(1 + f) − f, the in-doubling deviation of the linear-sub-bucket layout from the smooth logarithm, is at most
    0.0861 of a doubling, at f = 1/ln 2 − 1.

## Set-up

- **Budget.** Every structure gets K = 256 cells (S = 16 sub-buckets × 16 doublings for HdrHistogram's layout; DDSketch
  with 256 buckets and collapse of the lowest).
- **The writer's array** is the control: 256 uniform cells over [0, X], X given exactly, then X off by 10× and 0.1×.
- **The reader's lay table** has n cells across [0, H] and the rest one per (ln 2)/m of level, m set so the cells reach
  2¹⁶·H.
- **Streams** (10⁶ values each, seeded): log-uniform over 10⁻⁶ … 10⁶; lognormal σ = 3; Pareto with α = 1 (no mean);
  two clusters six decades apart; and a narrow lognormal σ = 0.3.
- **Readings.** Quantiles at q = 0.001, 0.01, 0.25, 0.5, 0.75, 0.99, 0.999, each estimated from its cell, against the
  exact quantile. The measure is relative error.
- **H choices.** H fixed at 1, with the world scaled by k = 10⁻³, 1, 10³; H moved with the world (H = k); H at the
  stream's own median.

## Predictions

*Each with its kill condition, written before `runs/skt/` exists.*

- **K1, one design.** Every reader-column structure, as built from its own published rule (DDSketch's ⌈log_γ x⌉,
  HdrHistogram's bucket and sub-bucket, the turn, the lay), is ⌊K·F(x/H)⌋ + c for one monotone F and a constant c, on
  every value of every stream. *Killed* if any index disagrees with its F form.
- **K2, HdrHistogram is the lay in base 2.** Its index as a fraction of a doubling differs from the smooth base-2 lay
  (log₂ past the first range, proportional inside it) by at most 0.0861 of a doubling, the bound attained to 10⁻⁶ on a
  dense sweep. *Killed* if exceeded or not approached.
- **K3, the turn's resolution.** On every stream, the turn table's quantile error is within one cell of
  (π/2K)·(s + 1/s), s = q/H, and the same at s and 1/s (on the two clusters placed at H·10³ and H·10⁻³). *Killed* if any
  quantile's error exceeds the cell bound, or the two clusters differ by more than one cell.
- **K4, where each wins.** H at each stream's median.
  - On the narrow lognormal (σ = 0.3, quartiles at s = e^(±0.2)) the turn beats DDSketch at q = 0.25, 0.5 and 0.75 by
    at least 5×.
  - On the log-uniform stream over 12 decades (quartiles at s = 10^(±3), past the crossover at 1.24 decades) DDSketch
    beats the turn at every quantile but the median, and the turn's relative error at the quartiles exceeds 1.
  - The lay: past H its relative error is the same on every level to 10%; inside H it grows as 1/s.

  *Killed* if any of the three fails on its stream.
- **K5, scaling the world.**
  - With H fixed: DDSketch's quantile errors are unchanged under k = 10⁻³ and 10³ to within bucket alignment (its index
    shifts by a constant), while the turn's and the lay's change.
  - With H moved with the world, all three are unchanged to within cell alignment.
  - The writer's array is unchanged only with X moved with the world. With X off by 10× its median error is over 50%,
    or its cells overflow.

  *Killed* if DDSketch's errors move by more than a bucket under k, or any reader structure's errors move with H = k.
- **K6, the best H is the corner of what is read.** For the turn table, the H that minimizes the largest relative
  error over the quartiles and the median is within a factor 1.5 of √(q₀.₂₅·q₀.₇₅). Over q = 0.01 to 0.99 it is within
  1.5 of √(q₀.₀₁·q₀.₉₉). *Killed* if either is off by more than 1.5.
- **K7, order per cell, not sums.** On the Pareto α = 1 stream every structure's median is within its cell bound. The
  mean estimated from cell midpoints drifts as more values arrive (no settling between 10⁵ and 10⁶). *Killed* if a median
  leaves its bound, or the midpoint mean settles to 1%.

## The search

A fresh agent, given the claim (not the predictions), looks for:
- **T1:** quantile sketches or histograms written as one family ⌊K·F(x/H)⌋ with F the design choice;
- **T2:** arctangent or tangent-spaced bins used for histograms or sketches of unbounded positive data (compactified
  axes, tan-spaced bins, Cauchy-quantile bins);
- **T3:** HdrHistogram or the float layout described as μ-law or A-law, or as linear-then-logarithmic around a chosen unit;
- **T4:** writer and reader, or known and unknown extent, as the organizing axis of a survey of streaming summaries.

Predicted: T3 found, since floats and companding are commonly compared; T1 found in part (t-digest's scale functions
are a family of this kind on the quantile, not on x); T2 rare; T4 not found.

## What would follow

If K1–K7 stand, a paragraph in the CS companion: the reader's data structure as ⌊K·F(x/H)⌋ with order per cell, F the
only choice, the writer's array beside it. OFS Appendix B only if the search leaves something ours. A demo only if it
helps to see. Tom rules.

## Runs

*(none yet)*
