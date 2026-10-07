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

### Run 1 (7 October, `python3 plans/cal/cal.py`, seed 91, 20,000 trials at each setting): P1 and P2 killed, at r = 0.7

| r | depth slope per doubling of V/c, measured | predicted, 1/log₂(1/r) | adaptive net / oracle's, over V/c 10 … 10⁶ |
|---|---|---|---|
| 0.3 | 0.597 | 0.576 (+4%) | 1.000 at every V/c |
| 0.5 | 0.980 | 1.000 (−2%) | 0.980 to 1.000 |
| **0.7** | **1.478** | **1.943 (−24%)** | **0.86, 0.81, 0.81**, 0.98, 1.00, 1.00 |

At r = 0.3 and 0.5 the adaptive reader stops at or next to the oracle's depth (V/c = 1,000, r = 0.5: 8.97 against 9),
and beats "everywhere" (30 levels) and "never" at every V/c. At r = 0.7 it stops far too early: 7.3 levels against the
oracle's 16 at V/c = 1,000. Its net there (796) falls below "everywhere" (970), and it stays below "everywhere" up to
V/c = 10⁶.

- **P1 killed** at r = 0.7: slope 1.48 against 1.94, 24% short. It holds at r = 0.3 and 0.5 (within 4%).
- **P2 killed** at r = 0.7:
  - adaptive is under 90% of the oracle at V/c = 10, 100 and 1,000;
  - it is under "everywhere" from V/c = 1,000 on.

  It holds at r = 0.3 and 0.5.

**Why, read after the run (the kills stand).** The reader estimates how fast detail fades from the ratio of two noisy
looks. When detail fades slowly (r near 1), the gain it expects from the next level, V·oₖ·(1 − r̂), turns on the
small number 1 − r̂ (0.3 here), and noise in r̂ swings it widely. Whenever noise makes r̂ look close to 1, the reader
judges the next level worthless and quits. So a noisy situated reader underprices slowly fading detail, and stops early
exactly where depth is most worth having. Where detail fades fast (r = 0.3, 0.5), the same noise barely matters.

**What CAL says, so far.**
- **Supported (r = 0.3 and 0.5):** priced observation stops at a finite depth even though the thing never concludes.
  That depth grows by a fixed number of levels for each doubling of what the reading is worth: the logarithm, from the
  price of looking.
- **Not supported in general:** a reader that prices each level from its own two last looks fails on slowly fading
  detail. A fix (pricing from a running estimate over all the levels seen, not just the last two) would be a new run with
  its own prediction.

### Run 2: pricing from a running estimate (prediction written before run 2)

Tom: "do complete any tests that are planned." Run 1's fix, as a new run. Everything is as in run 1 except the adaptive
reader's estimate of r. Instead of the ratio of its last two looks, it fits a straight line to log oₖ against k over
all the levels it has seen, and takes r̂ from the slope (r̂ = ½ before it has two looks). Noise then averages out as it
goes deeper.

- **P1″ (the kill): the slope recovers.** The depth slope per doubling of V/c is within 20% of 1/log₂(1/r) for all
  three r, including r = 0.7, where run 1 fell 24% short.
- **P2″ (the kill): the net recovers.** At every V/c and r the adaptive net is at least 90% of the oracle's, and above
  both "everywhere" and "never".
- **Expected trouble:** at V/c = 10 and r = 0.7 the reader has seen only one or two levels when it decides, so the
  running estimate is no better than run 1's there. This is the setting most likely to fall under 90%.

**Informed by run 1, and said so.** The fix was chosen after seeing why run 1 failed.

### Run 2 (7 October, `cal.run2()`, seed 92, 5,000 trials at each setting): P1″ not killed; P2″ killed, at r = 0.7

| r | depth slope (predicted) | adaptive net / oracle's, V/c 10 … 10⁶ | below "everywhere"? |
|---|---|---|---|
| 0.3 | 0.595 (0.576, +3%) | 1.000 at every V/c | never |
| 0.5 | 1.000 (1.000, 0%) | 0.988 to 1.000 | never |
| 0.7 | 2.006 (1.943, +3%) | **0.890**, 0.922, 0.942, 1.000, 1.000, 1.000 | **at V/c = 1,000** (924 against 970), and by 0.01 at 10⁵ |

- **P1″ not killed.** With the running estimate the slope is within 3% of 1/log₂(1/r) for all three r, including
  r = 0.7, where run 1 fell 24% short.
- **P2″ killed** at r = 0.7.
  - At V/c = 10 the net is 0.890 of the oracle's, the trouble predicted: the reader has seen one or two levels when it
    decides.
  - At V/c = 1,000 its mean depth is close to the best (15.2 against 16), but noisy early stops on some trials pull the
    mean net below "everywhere" (924 against 970).
  - At V/c = 10⁵ it trails "everywhere" by 0.01 of 99,968. There "everywhere"'s fixed 30 levels happen to sit next to
    the best depth, 29, so this is a tie in all but name. It still counts.
- **Fast-fading detail** (r = 0.3, 0.5): the adaptive reader is at the oracle, within 1.2%, at every V/c.

**What CAL says, after two runs.** Depth is the logarithm of worth: with an estimate that averages its looks, each
doubling of V/c buys 1/log₂(1/r) levels, within 3%, at every rate of fading. Even so, a reader pricing by its own noisy
looks pays for slow-fading detail. It lands near the best depth on average, but sometimes stops early, and where
detail fades slowly that costs it against a reader that recurses everywhere. Depth where needed beats depth everywhere
cleanly only where detail fades fast enough for the reader to see it fading.
