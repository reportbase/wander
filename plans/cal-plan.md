# CAL: observation costs calories; depth is the logarithm of what it is worth

*Plan, prediction and kill written 7 October 2026, before the script was written or run (Claude). From Tom: "but math
is free, but real observation requires calories. how can we add a cost calculation"; "proceed". Synthetic. The lab
rules hold: nothing above the "Runs" line is edited after the run. `papers/number-line.md` §4.*

## The reader, the thing, the prices

- **The thing.** A quantity whose remainder, unread past level k, is aₖ = rᵏ (a₀ = 1): detail shrinking by a ratio r
  per level, as natural shapes' detail tends to. r is 0.3, 0.5 or 0.7.
- **The price.** Entering each level beyond the first look costs c calories.
- **The worth.** Reading to depth K is worth V·(1 − a_K), what the reading removes of the unread remainder. The net is
  V·(1 − a_K) − c·K.
- **What the reader sees.** It does not know r. At each level it sees the remainder with noise, oₖ = aₖ·e^ε, where ε
  is normal with sd 0.2.

## Four policies

- **Adaptive (the situated reader).** At level k it estimates r̂ = oₖ/oₖ₋₁ (r̂ = ½ before it has two), and enters the
  next level only if the expected gain V·oₖ·(1 − r̂) exceeds c.
- **Oracle.** Knows r and stops at the depth K* that maximizes the net. The ceiling.
- **Everywhere.** Always enters 30 levels: the ordinary number line's depth everywhere.
- **Never.** Stops at the first look (K = 0).

V/c runs over 10, 10², …, 10⁶. 20,000 trials at each setting.

## Prediction

- **P1 (the kill): depth is the logarithm of worth.** The adaptive reader's mean depth grows in a straight line with
  log₂(V/c), with slope 1/log₂(1/r): 0.58 for r = 0.3, 1 for r = 0.5, 1.94 for r = 0.7. Each doubling of what a
  reading is worth buys a fixed number of extra levels. Predicted within 20% of each slope, fitted over the six V/c.
- **P2 (the kill): spending where it is worth it pays.** At every V/c and r, the adaptive reader's mean net is at
  least 90% of the oracle's, and above both "everywhere" and "never".

## Kill

- **P1 killed** if any fitted slope is more than 20% off its predicted value.
- **P2 killed** if at any setting the adaptive reader's net is under 90% of the oracle's, or not above both "everywhere"
  and "never".

## What it would mean

Depth is finite for a third reason, besides a thing that concludes and a grain that stops the reader: the next level
is not worth its calories. It holds even where the thing never concludes. And the depth a priced reader chooses is the
logarithm of what the reading is worth to it. The logarithm comes from the price of looking.

## Runs
