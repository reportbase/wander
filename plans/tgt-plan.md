# TGT: the two-group tower, closure recovers the one factor that crosses (exact arithmetic)

*Plan written 11 October 2026, before `tgt/tgt.py` was written or run (Claude; Tom: "proceed according to your
recommendation"). The archived result (*The Order of Limits* §4.4, T3: "L ÷ unit = ρ: 0.5000, 2.0000 and 3.7003")
rests on a script not in this repository and on that paper's stitch machinery. This plan restates the claim in its
plainest exact form and tests that, before anything moves into `papers/observation-from-somewhere.md`.*

## The claim, restated (keep the case)

Two readers share one closed figure. Reader A records its part of the outline as edges, each a direction and a length
counted in A's own hold H_A; reader B records the rest the same way in its own hold H_B. Directions are exact; lengths
are counts of each reader's own unit. H_A and H_B are amounts and neither reader knows the other's; their ratio
ρ = H_B/H_A is the private part. Claim: **closure alone recovers ρ exactly**, and no more than ρ: the absolute size (one
hold) stays free. This is the denominator exchange (`papers/denominator-paradox.md`): one factor crosses between two
private rulers, and the shared fact (the figure closes) buys it.

## Derivation (written before the run)

Let A's edges be a_i·u_i (a_i its counts, u_i unit directions) and B's be b_j·w_j. In amounts the edges are
H_A·a_i·u_i and H_B·b_j·w_j, and closure says H_A·S_A + H_B·S_B = 0, with S_A = Σ a_i·u_i and S_B = Σ b_j·w_j. So
S_B = −(H_A/H_B)·S_A: the two sums are parallel and opposite, and ρ = H_B/H_A = |S_A|/|S_B|. This fails only when
S_A = 0, that is when A's part closes on its own (then so does B's, and nothing crosses). Rescaling both holds by one
factor leaves every count unchanged, so the absolute size is not recovered.

## Predictions

- **P1 (exact recovery).** On random closed polygons (3 to 40 edges, split at a random edge into A's part and B's),
  with ρ drawn from 0.01 to 100, closure recovers ρ to within 10⁻¹² relative. *Killed* otherwise.
- **P2 (the archive's three values).** For ρ = 0.5, 2 and 3.7 on a circle of 4000 edges split in half, the recovered
  value is 0.5000, 2.0000 and 3.7000 to four places. *Killed* otherwise.
- **P3 (only the ratio).** Multiplying both holds by any common factor leaves every count, and so the recovered ρ,
  unchanged: the absolute size is not recoverable from the counts. *Killed* if the counts change.
- **P4 (the degenerate case).** When each part closes on its own, |S_A| and |S_B| are both zero to rounding and the
  recovery is undefined. *Killed* if a finite ρ is returned without flagging it.
- **P5 (rounding to a step).** If each reader rounds its counts to whole steps of its own unit, the relative error in ρ
  is of the order of (number of edges)·(step)/|S_A| and falls as the step falls. *Killed* if the error does not fall
  with the step over three decades.

## Runs

**Run 1 (11 October 2026; `tgt/tgt.py`, seed 11).**
- **P1 not killed**: on 2000 random closed polygons (3–40 edges, ρ from 0.01 to 100, holds from 10⁻³ to 10³), the worst
  relative error in the recovered ρ is 5.3×10⁻¹⁵.
- **P2 not killed**: on a 4000-edge circle split in half, ρ = 0.5, 2 and 3.7 are recovered as 0.5000, 2.0000, 3.7000:
  the archive's T3 values, now from the plain closure argument.
- **P3 not killed**: scaling the figure and both holds by one factor (7.3) leaves every count unchanged, and the same ρ
  comes back (2.5000): closure gives the ratio of the holds and nothing about either one.
- **P4 not killed**: when each part closes on its own (two loops joined at a point), both sums vanish and the recovery
  is flagged undefined.
- **P5 not killed**: with counts rounded to whole steps, the relative error in ρ is 1.0×10⁻¹, 1.2×10⁻², 8.7×10⁻⁴ and
  2.1×10⁻⁴ for steps of 10⁻¹ to 10⁻⁴ of the unit: it falls with the step (about tenfold per decade, then fourfold).
