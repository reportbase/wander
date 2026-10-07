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
