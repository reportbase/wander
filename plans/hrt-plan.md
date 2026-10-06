# HRT: the 2 of the central hypothesis, with h taken from the parent's record

*Plan, prediction and kill written 6 October 2026, before any run (Claude; Tom: "not needed. proceed", so not ruled on).
The run SPN names as the one that "could show it, or fail to" (central hypothesis, Standing after the shape and signal
runs; §14, From the shapes). Script: `plans/hrt/hrt.py`. Results are added below the line, as they fall; nothing above
the line is edited after the run.*

## The question

R183: a reader's h is the front half of its octave, and the octave is 2h. The run that could test it: readers that take
their own h from their parent's record, reading signals built on ratios of 2, 3 and the golden ratio. If the ratio of a
parent's h to its child's settles at 2 whatever the signal, the 2 belongs to the reader; if it follows the signal's
ratio, it belongs to what is read.

## A caution, written before the run

SPN itself warns that "building readers in simulation cannot decide between the hypothesis and (c), since the builder
chooses". The same holds here, by a scaling argument: if the child rule is scale-free (scale the whole picture by λ and
every child's h scales by λ) and holds no number of its own, the only ratio left to set the parent-to-child ratio is the
signal's. A rule that holds a 2 (for example, a child's h taken as half of something) will tend to give 2 back. So this
run tests something narrower than R183: **whether a reader with no 2 built into it produces a 2 anyway.** If it does,
that is support for R183 the builder did not put in. If it does not, R183 is not refuted, only shown to need its 2 from
somewhere other than the record.

## Set-up

- **Signals.** Landscapes y(x) = A · Σₖ r⁻ᵏ cos(2π rᵏ x / P + φₖ), k = 0 … K − 1: every scale has the same shape, each
  r times finer and r times lower than the last. P = 64, A = 8. r = 2 (K = 7), 3 (K = 5), φ = 1.618… (K = 10), so the
  finest period is P/64, P/81 and P/76. Phases φₖ from a fixed seed. Three seeds per signal.
- **A reader** stands at a point of the landscape with its eye h above it. It lays N = 1,440 rays evenly in direction over
  the lower half (both facings) and records, for each, how many of its own h's along the ground the first meeting falls
  (none past 64 h: the horizon). That record is all it holds.
- **Hand-offs** (as in SIG): where neighbouring rays in one facing jump outward by more than a factor J = 1.5 in their
  meeting distance, the first ray grazed a crest and the next landed beyond it; between them is a stretch the reader
  could not see, of length L (read off the record, in the parent's h's, times its h).
- **The child rule, scale-free.** A child stands on that crest, and **its h is c · L: the stretch its parent could not see
  becomes its unit.** c = 1 is the run; c = ½ and c = 2 are a check on whether the rule's own number sets the result.
  Each parent hands off its three longest hidden stretches. A chain stops below the finest period, above 4P, or at
  six levels.
- **Roots.** Five places, three starting heights (P/2, P/3, P/5): fifteen roots per signal and seed, so that no one
  starting choice sets the result.
- **The reading.** The ratio h(parent)/h(child) for every hand-off past the first (the root's h is the builder's), and
  its median, compared with the nearest power of 2 and the nearest power of r.

## Prediction (written before the run)

Claude's expectation, from the scaling argument: **the ratio follows the signal.** For r = 3 and r = φ the median ratio at
c = 1 sits nearer a power of r than a power of 2, and is not within 10% of 2. (For r = 2 the two coincide, and the
signal says nothing.) The hand-offs should step down the signal's own levels, as SIG found the hand-offs following the
crest spacing.

R183's prediction: the ratio settles at 2 for every signal.

## Kill

The expectation is killed, and R183 gains support it was not built to have, if **for both r = 3 and r = φ the median
ratio at c = 1 is within 10% of 2.** If only one of them is, the run is undecided. If c = ½ or c = 2 gives 2 and c = 1
does not, that is the rule's number, not the reader's, and counts for nothing.

---

## Runs

*(none yet)*
