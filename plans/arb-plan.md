# ARB: an arithmetic baseline, the ordinary line against one that recurses as needed

*Plan, prediction and kill written 7 October 2026, before the script was written or run (Claude; Tom: "how would we
create a baseline to compare these two"; "yes"). `papers/number-line.md` §4, "Arithmetic on a line that recurses as
needed". Synthetic. The lab rules hold: nothing above the "Runs" line is edited after the run. Sorting is left out:
`plans/anl-plan.md` already measured it.*

## The referee and the contenders

- **Referee:** exact arithmetic (Python's `Fraction`, never rounded).
- **Float:** ordinary 53-binary-digit floating point, as computers use it. It always carries about 16 significant
  digits.
- **Fixed:** the ordinary line at a fixed depth everywhere, set by the deepest number in the task.
- **Recursing:** each number a cell, an interval as wide as its own depth, plus a one-digit tag for that depth (so the
  bookkeeping is paid for). Exact numbers stay exact; a result that does not conclude gives digits only on demand.

## Tasks

1. **A column of measurements at mixed depths.** 1,000 true values, uniform on [0, 10). Each is measured to its own
   depth: 70% to 1 decimal, 25% to 2, 5% to 6. The contenders see only the measurements; the truth is the sum of the
   true values. 200 columns.
2. **Cancellation.** (10¹⁶ + 1) − 10¹⁶.
3. **The control: a column at one depth.** 1,000 values, all measured to 3 decimals. Detail is the same everywhere.
4. **Equality.** (a) 0.1 + 0.2 = 0.3? (b) √2 · √2 = 2?, with √2 given as digits on demand, asked at depths up to 50.

## Measures

- **Storage**, in decimal digits: fixed, 1 + its depth for every number; recursing, 1 + each number's own depth + 1 for
  the tag.
- **Correctness:** is the truth inside the answer (recursing), or how far off is it (float, fixed)?
- **Honesty:** does the answer say how much it knows? Float's implied uncertainty is half a unit in its last place.

## Prediction

- **P1 (the kill): the recursing line is right and honest on task 1; float is not honest.** The recursing sum's interval
  contains the truth in all 200 columns. Float's actual error exceeds its implied uncertainty in at least 95% of them.
- **P2 (the kill): it saves where depth is uneven, and not on the control.** Storage, recursing over fixed: under 0.6
  on task 1, and 1 or more on task 3.
- **P3: cancellation.** Float gives 0; fixed and recursing give 1.
- **P4: equality.**
  - (a) Float says false; recursing says true, exactly.
  - (b) Float says false (2.0000000000000004). Recursing says "undecided" at every depth to 50: never true, never false.

## Kill

- **P1 killed** if the recursing interval misses the truth in any column, or float's error is within its implied
  uncertainty in more than 5% of columns.
- **P2 killed** if task 1's ratio is 0.6 or more, or task 3's is under 1.
- **P3 or P4 killed** if any answer differs from the one predicted.

## What it would mean

The recursing line wins where depth is uneven, and where float hides what it has lost; on the control it costs a little
more. It is not a better line everywhere. It is the line whose answers say how much they know.

## Runs
