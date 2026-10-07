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

### Run 1 (7 October, `python3 plans/arb/arb.py`, seeds 81 and 82): nothing killed

| task | float | fixed (depth everywhere) | recursing (depth where needed) |
|---|---|---|---|
| 1, mixed-depth column: truth inside the answer | n/a; error beyond its implied half-unit in **200 of 200** | claims 6 decimals; actual error a median **1.06 million** times that | interval holds the truth in **200 of 200** |
| 1, storage, against fixed | (16 digits a number) | 1 | **0.50** |
| 2, (10¹⁶ + 1) − 10¹⁶ | **0** | 1 | 1 |
| 3, control, storage against fixed | (16 digits a number) | 1 | **1.25** (holds the truth) |
| 4a, 0.1 + 0.2 = 0.3? | **false** | true | true |
| 4b, √2 · √2 = 2? | **false** (2.0000000000000004) | depends on its depth | **undecided at every depth 1 to 50** |

- **P1 not killed.** The recursing interval holds the truth in all 200 columns. Float's error exceeds its implied
  uncertainty in all 200.
- **P2 not killed.** Storage is 0.50 of fixed on the mixed column, and 1.25 on the control, where the depth tags cost
  without any saving.
- **P3 and P4 not killed.** Every answer is as predicted.

**What holds by construction, and what is measured.**
- *By construction:* that the recursing interval holds the truth (each measurement is rounded to nearest, so every cell
  holds its true value), and the float behaviour in tasks 2 and 4, which is well known.
- *Measured:*
  - the storage ratios, half on uneven depth and a quarter more on the control;
  - how far the ordinary line overclaims on the mixed column, writing 6 decimals for numbers known to 1 or 2.
    Its sum is then off by about a million times what those 6 decimals claim.

**What ARB says.** The line that recurses as needed is not better everywhere. Where depth is uneven it stores half as
much, and its answers say how much they know. Where depth is even it costs a quarter more, for tags that tell nothing
new. The ordinary line's real fault is not its cost. It is that it writes the same depth for every number and so claims
knowledge it does not have, by six orders of magnitude in task 1. And √2 · √2 = 2 stays undecided at every depth: the
recursing line cannot finish it, and says so. That is the correspondence with the corner, shown, not proved.
