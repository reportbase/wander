# ANL: a number line that recurses as needed

*Plan, prediction and kill written 7 October 2026, before the script was written or run (Claude). From Tom: "lets do a
thought experiment. lets create a number line that recurses as needed compared to just allowing an infinite number of
decimals"; after "situated observers only recurse into known perturbations. there is no point to having depth
everywhere, which what the number line does" and "the number line has infinite depth, even though, perturbations are
finite, they conclude." Synthetic. The lab rules hold: nothing above the "Runs" line is edited after the run.
`papers/number-line.md` §4.*

## The two lines

Hold N = 1,000 numbers in [0, 1), in binary, one doubling per level.

- **Depth everywhere (the ordinary line).** Every number gets the same number of digits b: enough to separate the
  closest pair anywhere, b = ⌈log₂(1/g)⌉ for the smallest gap g. Cost: N·b digits.
- **Depth where needed (a recursing line).** Start with one cell, [0, 1). Split a cell in half only if it holds two or
  more numbers; stop where each number stands alone. Each number gets as many digits as its depth in this tree. Cost:
  the digits written (the sum of the depths) plus one mark for each split, so the structure is paid for too.

## Three sets of numbers

- **E, evenly spaced:** (i + ½)/N. Detail is the same everywhere. The control.
- **U, uniform random.** Detail is scattered by chance; the closest pair is much closer than the typical gap.
- **C, clustered:** 50 clusters of 20 numbers, each cluster 10⁻⁶ wide, the cluster centres at random. Detail is in a
  few places.

Seeded, so each set is fixed.

## Prediction

The ratio is the recursing line's cost over the ordinary line's.

- **P1 (the kill): clustered numbers gain most.** For C, the ratio is under 0.3.
- **P2: uniform random numbers gain moderately.** For U, the ratio is between 0.4 and 0.75. The closest of 1,000
  random numbers is about 1/N² apart, so the ordinary line pays about 2 log₂ N digits a number, and the recursing line
  about log₂ N plus a little.
- **P3: evenly spaced numbers gain nothing.** For E, the ratio is between 0.9 and 1.6: no gain, and possibly a loss to
  the cost of the split marks.

## Kill

- **P1 killed** if C's ratio is 0.3 or more.
- **P2 killed** if U's ratio is outside 0.4 to 0.75.
- **P3 killed** if E's ratio is outside 0.9 to 1.6.

## What it would mean

Depth where needed pays exactly as much as the detail is uneven. Where detail is the same everywhere, as on the
ordinary number line's own grid, there is nothing to gain, so the ordinary line is the right tool for evenly spread
numbers and the wrong one for anything clustered. A situated reader's depth follows what it holds; the number line's
follows the worst case anywhere.

## Runs

### Run 1 (7 October, `python3 plans/anl/anl.py`, seed 71): P1 killed; P2 and P3 not killed

| set | depth everywhere | depth where needed (digits + splits) | mean depth | ratio |
|---|---|---|---|---|
| E, evenly spaced | 10,000 (10 a number) | 9,976 + 999 = 10,975 | 10.0 | **1.10** |
| U, uniform random | 22,000 (22 a number) | 11,357 + 1,457 = 12,814 | 11.4 | **0.58** |
| C, clustered | 36,000 (36 a number) | 25,470 + 2,222 = 27,692 | 25.5 | **0.77** |

- **P1 killed.** C's ratio is 0.77, not under 0.3.
- **P2 not killed.** U's ratio is 0.58: the ordinary line pays 22 digits a number for its single closest pair, while
  the recursing line pays 11.4 on average.
- **P3 not killed.** E's ratio is 1.10: no gain, and a small loss to the split marks, as predicted.

**Why P1 failed, read after the run (the kill stands).** The plan built C with *every* number inside a cluster 10⁻⁶
wide. So every number lives in fine detail and needs about 25 digits to stand alone; the recursing line saves only the
difference between each number's own neighbourhood and the single worst one (36). That is not "detail in a few
places". It is detail everywhere, at a finer scale. The design did not test what the plan said it would. A fix is a new
run with its own prediction, below.

### Run 2: a few perturbations in a plain line (prediction written before run 2)

**The set, P.** 1,000 numbers evenly spaced as in E, then 5 of them each given a twin 10⁻⁹ away (1,005 numbers in all).
Fine detail in 5 places; elsewhere the line is plain.

- **P1′ (the kill).** P's ratio is under 0.45. The ordinary line must pay about 30 digits for every number because of
  the 5 twins. The recursing line pays about 10 for most numbers and about 30 only for the 10 near the twins.
- **Reported:** how the ratio changes with 1, 5, 50 and 500 perturbed places. Predicted to rise toward E's 1.1 as the
  perturbations spread everywhere.

**Informed by run 1, and said so.** It was written after seeing run 1's numbers, so it tests the idea the plan meant to
test, not whether it was foreseen.
