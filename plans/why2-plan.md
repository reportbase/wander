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
