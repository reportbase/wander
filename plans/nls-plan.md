# NLS: the number-line split, on synthetic readers

*Plan, prediction and kill written 7 October 2026, before the script was written or run (Claude; Tom: "synthetic test are
fine, we are moving quickly over ideas … with synthetic data, we can precisely model the situation quickly"). It tests
`papers/number-line.md` §6. The lab rules hold: nothing above the "Runs" line is edited after the run.*

## What a synthetic run can and cannot say

It cannot say that people are situation-3 readers. It can say whether such readers, and the alternatives, leave
patterns that can be told apart, using the same instrument as NLE (`plans/nle/nle.py`: LIN, LOG, PWR1 and CNR, fitted by
least squares and compared by BIC). If they cannot be told apart even when built to differ, a real-data run 2 would be
pointless. If they can, the run says how cleanly, and at what noise.

## The two tasks

- **Bounded.** A line marked 0 and 100; place n. The whole is given.
- **Open.** A line marked 0 and 10, running on with no end; place n, in the same units. Only a unit is given (Cohen and
  Blanc-Goldhammer's unbounded task, as recalled; to be checked before any real-data use).

The same 24 targets as NLE's self-test, 2 to 96, in both tasks.

## Three kinds of reader, 200 each

| kind | bounded line | open line | what it stands for |
|---|---|---|---|
| **S, situated throughout** | CNR with its own unit h | CNR with the same h | a situation-3 reader that never uses the whole |
| **W, whole where given** | PWR1, proportion judgment | LIN: no end to anchor to, so it steps out the unit | a reader that only ever divides by a whole or a unit |
| **C, switching** (the paper's §5 claim) | PWR1 | CNR with its own h | holds the whole when given; situated when not |

Each reader draws its own h (log-normal, median 12, so most lie 5 to 30) and its own PWR1 exponent (0.5 to 0.75); noise
is normal with sd 8 in the line's units, as in NLE's self-test. Each task is scored by the model with the lowest BIC:
LIN, LOG, PWR1 and CNR on the bounded line; LIN, LOG and CNR on the open line (PWR1 needs an end).

## Prediction

- **P1 (the kill).** For C readers, the instrument names PWR1 on the bounded line and CNR on the open line for a majority
  of them.
- **P2.** Each kind's pattern is recovered for a majority of its readers: S (CNR, CNR), W (PWR1, LIN), C (PWR1, CNR).
- **P3 (reported).** For S and C readers, the open line's fitted h lies within a factor 2 of the true h for a majority.
- Expected trouble, from NLE's self-test: on the bounded line BIC gives some corner readers to LOG (55 of 200 there), so
  S's bounded pattern is the likeliest to fall short.

## Kill

- **P1 killed** if C's split is recovered for half or fewer. Then the split is not detectable by this instrument at this
  noise, and NLE run 2 on real data would need a better instrument first.
- **P2 killed** for a kind if its pattern is recovered for half or fewer of its readers.

## Also run, reported only

The same at noise sd 4 and 12, to show how the recovery depends on noise.

## Runs
