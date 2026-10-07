# WHY2: does the cheapest dial step by 2?

*Plan, prediction and kill written 7 October 2026, before the script was written or run (Claude; Tom: "yes", to running
it). SPN's central open question is why its levels are doublings, the ratio between rungs (SPN §14; `CLAUDE.md`: "dyadic
levels … the layout's rule, not derived"). In GRN run 4 the slider halved its grain because it was made to. Here a
reader may step its grain by any ratio ρ, and pays for what it reads. Synthetic. The lab rules hold: nothing above the
"Runs" line is edited after the run.*

## The reader and its prices

- **The system:** a span of size s₀ in the reader's starting grain, unknown to it, somewhere between 2⁻²⁰ and 2⁻²
  (log-uniform): far below its corner.
- **The reader:** model-free, as in GRN runs 3 to 6. It looks at a fixed field. On look i its grain is ρ⁻ⁱ, finer by ρ
  each time, and it counts lit pixels, with the grid at a random offset on each look. It stops at the first look that
  lights two or more pixels. Below its corner that happens by chance, with probability s₀ρⁱ; from the corner on, always.
- **The price:** a look reads every grain of the field, so look i costs ρⁱ, the number of grains at that grain size.
  Finer looking costs more.
- **The ideal:** a reader that knew s₀ would look once, at the grain that puts the system at its corner, for 1/s₀. The
  measure is the cost ratio, total spent over 1/s₀.

ρ = 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.5, 4, 5, 6, 8. 200 values of s₀; 2,000 trials each.

## Reasoning, before running

Without luck below the corner, the reader stops at the first ρᵏ ≥ 1/s₀, having paid 1 + ρ + … + ρᵏ ≈ ρᵏ⁺¹/(ρ − 1).
- **Worst case** (s₀ just past a step): the ratio approaches ρ²/(ρ − 1), least at ρ = 2, where it is 4.
- **On average** over log-uniform s₀: the ratio is about ρ/ln ρ, least at ρ = e ≈ 2.72.

Lucky early stops lower both a little. They should not move the best ratios far.

## Prediction

- **P1 (the kill): against the worst case, the best step is 2.** The ratio ρ that minimizes the worst expected cost
  ratio over s₀ lies between 1.75 and 2.5.
- **P2 (the kill): on average, the best step is about e, not 2.** The ρ that minimizes the mean cost ratio over s₀ lies
  between 2.25 and 3.5.

## Kill

- **P1 killed** if the worst-case best ρ is outside 1.75 to 2.5.
- **P2 killed** if the average best ρ is outside 2.25 to 3.5.

## What it would mean

A reader that does not know where its corner is must pick how far to step its grain each look. If the costs are what
the reading reads:
- **A reader that must be sure of its worst case** steps by 2. Doublings would then be the levels of a reader that
  cannot gamble.
- **A reader that plays the odds** steps by about e.

That would make the 2 a choice of guarantee over gamble, not a fact of geometry. It is one candidate answer to SPN's
open question, under one cost model, stated as such.

## Runs

### Run 1 (7 October, `python3 plans/why2/why2.py`, seed 101): P1 and P2 killed

| ρ | 1.25 | 1.5 | 1.75 | 2 | 2.5 | 3 | 4 | 6 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| mean cost ratio | **1.000** | 1.004 | 1.018 | 1.036 | 1.091 | 1.155 | 1.290 | 1.568 | 1.835 |
| worst cost ratio | 1.061 | **1.043** | 1.067 | 1.083 | 1.187 | 1.285 | 1.503 | 1.968 | 2.470 |

The simulation matches the exact expectation to within its sampling (e.g. mean at ρ = 2: 1.036 simulated, 1.036 exact).

- **P1 killed.** The worst case is cheapest at ρ = 1.5, not in 1.75 to 2.5.
- **P2 killed.** The average is cheapest at ρ = 1.25, the smallest step tested, not near e.

**Why, read after the run (the kills stand).** The reasoning assumed that a look below the corner gives nothing, as in
the classic doubling search. But a model-free reader's look below the corner shows "two" by chance, with probability
s₀ρⁱ. A reader creeping in small steps takes many cheap looks, each with a growing chance, and tends to stop by luck
about when its looks have cost about 1/s₀ in all, near the ideal, whatever the step. So in this model the cheapest dial
has no preferred step, and finer is better: a continuous zoom.

That stop is the lucky "two" run 6 warned of, though: it is not a sure reading. So the run measured the cost of a
first, possibly lucky, sighting, not of a sure one. A fix is a new run with its own prediction, below.

### Run 2: the cost of a sure reading (prediction written before run 2)

Everything is as in run 1, except that the reader must confirm. After a look shows "two", it looks twice more at the same
grain, each look again costing ρⁱ. It stops only if all three show "two"; otherwise it steps finer and goes on. A lucky
"two" below the corner now survives the confirmation with probability (s₀ρⁱ)² only.

**Informed by run 1, and said so.** A reader that confirms pays for its steps below the corner, as the classic search
assumes, but still gets some luck. So the reasoning of the first prediction should now nearly hold.

- **P1″ (the kill): against the worst case, the best step is near 2.** The ρ minimizing the worst mean cost ratio lies
  between 1.5 and 2.5.
- **P2″ (reported, not a kill):** the ρ minimizing the average cost ratio, against e.
- **Also reported:** the same reader with no luck at all, stopping only once the system is past its corner (it could
  not know this; a check on the classic case): worst-case best at 2, average best at e, by construction.
