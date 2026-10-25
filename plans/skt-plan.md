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

### Run 1 (25 October 2026, `runs/skt/skt.py`, output `runs/skt/skt.txt`, 21.6 s, seeded)

**K1 not killed.** HdrHistogram's integer bucket and sub-bucket index (S = 16 sub-buckets in each doubling, written from its
published rule) equals the floor form of the float-like lay on all 71,492 integer values from 0 to 10⁶. DDSketch's ⌈log_γ x⌉ is
⌈K·ln x/(K ln γ)⌉, the same form, on 200,000 values. The turn and the lay take this form by construction, so for those two the
check proves nothing.

**K2 not killed.** The largest gap from the smooth base-2 lay is 0.0860713 of a doubling, at f = 0.44269. The bound is
0.0860713, at f = 0.44270.

**K3 not killed, with two weaknesses in my set-up.** On every stream, every quantile's error lies inside its cell. But the
quantiles that fall in the horizon cell have an infinite width, so the check passes there trivially, and that includes the
two-cluster clause. The mirror line (k ↔ K − 2 − k) shows a mismatch of 0.60: my pairing of cells was wrong. That line only
reported a number and decided no verdict. The same-at-s-and-1/s clause is therefore untested here; it is exact
algebraically.

**K4 KILLED, in one clause.**
- On the narrow lognormal the turn beats DDSketch by 26.5, 8.7 and 26.0 times at the quartiles and the median. That holds.
- On 12 decades, DDSketch beats the turn at every quantile except the median. That holds.
- The lay past H is level to 3.7% across 16 doublings. Inside H its error at s ≈ 1/64, 1/16 and 1/4 is 0.499, 0.244 and
  0.056, which is ×4 a step, as 1/s. That holds.
- The clause that fails: the turn's error at the quartiles is 2.08 at q 0.25 but 0.672 at q 0.75, not over 1 at both.

Post hoc: q 0.75 (s ≈ 10³) falls in the horizon cell, which begins near 163 H. That cell's representative (≈ 326 H) is
nearer to s = 10³ than the cell rule implies. Past the last finite boundary the error depends on the representative chosen
for the horizon, not on (π/2K)(s + 1/s). My prediction ignored the horizon cell.

**K5 not killed.**
- With H fixed, the world scaled by 10⁻³ or 10³ moves DDSketch's errors by about 10⁻¹⁵ (a bucket is 0.108). The turn's and
  the lay's errors change enormously.
- With H moved with the world, nothing moves by more than 1.8·10⁻¹².
- The writer's array gives the same cells only with X moved with the world. With X ×10 its median error is 1.96·10⁴; with
  X ×0.1 it is 195, and 83,242 values fall past the extent.
- With X exact, its median error is already 1.96·10³: 256 uniform cells cannot resolve log-uniform data at all, so the
  writer needs more than the extent here.

**K6 KILLED.** For the turn, the H that minimizes the largest relative error is off from √(q_lo·q_hi) by these factors:

| Stream | Quartiles and median | q 0.01 to 0.99 |
|---|---|---|
| Pareto | ×4.80 | ×6.51 |
| lognormal σ = 3 | ×2.52 | ×1.79 |
| log-uniform | ×1.71 | ×1175 |

Only one of the six comes within 1.5. Post hoc: a minimax over a few quantiles is set by whichever quantile lands in the
widest cell, or in the horizon cell. As H moves it is jagged, with one cell boundary crossing after another, and its
minimum sits wherever a boundary or the horizon's representative happens to fall. The geometric middle is where the cells
are finest on both sides at once. It is not where the worst of a few points is least. The prediction ran the two together.

**K7 KILLED, in its mean clause.** All three structures keep the Pareto median inside its cell. The turn's midpoint mean
does not drift:

| N | 10⁵ | 2·10⁵ | 5·10⁵ | 10⁶ |
|---|---|---|---|---|
| turn | 7.716 | 7.728 | 7.755 | 7.767 |

Its last step is 0.16%. Post hoc: the turn's horizon cell has a finite representative, so it caps every value past about
163 H. The capped mean of an α = 1 Pareto grows only as the count past the cap, which barely moves. The turn settles the
mean by throwing away the tail's amounts, which is the turn's bounded chart at work, not a mean of the data. The lay (last
step 2.83%) and DDSketch (13.4%) still drift. DDSketch tracks the sample's own mean (10.83, 16.27, 15.31, 17.8), whose
drift is the data's.

**What run 1 says.**
- The family holds as a form. One floor of K·F(x/H) builds each structure (K1, K2), and scaling separates them exactly as
  their F predicts (K5).
- What the family does not give is a simple rule for where each column wins, or for the best H, once the turn's horizon
  cell is in play. That cell holds everything past the last boundary. It caps the mean and it sets the minimax.
- The narrow claim stands: the reader's structure is ⌊K·F(x/H)⌋ with order per cell. The wider claim, that each column's
  behaviour follows from F alone, needs the horizon's representative named as a second choice.
- A run 2 would need predictions that name that representative first.

### The search (25 October 2026, a fresh agent given the claim, not the predictions)

Sources were read in full unless marked as a snippet.

- **T1: found in part, as predicted.**
  - Hartmann and Schlossnagle 2020 (circllhist, arXiv:2001.06561) is the nearest prior work. It gives an abstract theory
    of binning maps and coarsening, covering HdrHistogram and DDSketch. Its log-linear binning is log first, linear
    inside each decade. It has no single F with a scale H and no arctangent.
  - DDSketch's paper (arXiv:1908.10693) treats its index mapping as swappable, but every option approximates the
    logarithm.
  - t-digest's scale functions k₀–k₃ (Dunning and Ertl, arXiv:1902.04023) are a family, but they act on the rank q,
    not on x.
  - No source writes ⌊K·F(x/H)⌋ with F as the design choice and the turn among its options.
- **T2: found in part, as predicted (rare).** The only tan-spaced grids with a chosen scale are Boyd's rational
  Chebyshev maps (r = L·cot²(t/2); L sets "the frontier between both regimes"). Those are spectral grids for
  interpolation, not bins for counting. Nothing was found that bins, sketches or compands by the arctangent.
- **T3: found, as predicted.**
  - circllhist proves (Proposition 3.11) that log-linear bin boundaries are the floating-point numbers, and that
    HdrHistogram is a log-linear histogram in base 2.
  - A-law's formula is linear to 1/A, then 1 + ln. A patent reads an A-law code as a float with 4 mantissa and 3
    exponent bits (a snippet).
  - Not found: any statement that HdrHistogram is A-law, or that subnormals are the proportional part of a logarithmic
    layout.
- **T4: half killed.** I predicted "not found".
  - Known against unknown extent is an axis in the literature: "fixed-universe" methods (q-digest) against the rest in
    Chen and Zhang's survey (arXiv:2004.08255). Cormode et al. (arXiv:2004.01668) note that q-digest "requires prior
    knowledge of the data universe U". DDSketch criticizes HdrHistogram's bounded range.
  - The reader–writer framing, as the axis of a survey, was not found.

What the search leaves ours is narrow. One F-family in value space with a scale H, with the turn (the arctangent) as one
member, and with its horizon cell. Each piece beside it is in print: the log and log-linear layouts, floats as
HdrHistogram, A-law, and the known-universe axis.


### A note added after the runs (25 October 2026, SPN R494)

Tom: "it seems like a writer thing not a reader thing". The sketches bin amounts against a chosen unit, a writer's act;
a reader's structure is indexed by direction. Kept out of the papers; see `plans/onl-skt-note.md`. The runs and verdicts
above stand.
