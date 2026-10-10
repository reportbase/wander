# ISQ: is the in-place lay the inverse square?

*Plan, predictions and kills written 10 October 2026, before the script was written or run (Claude; Tom, at `levels.html`:
"this will be helpful to find physics correspondance", then "yes, #1" to this one). The lab rules hold: nothing above the
"Runs" line is edited after the run.*

## The claim

On `levels.html` (and draw's `gallery/levels.html`) a reading s past the corner is laid at a radius, and each doubling of s
gets half the room of the last. In wander the lay is ρ(s) = 2 − 1/s for s ≥ 1. In draw it is linear within each level
and agrees with wander's at every level wall s = 2^k. The room the lay gives per unit of s is dρ/ds. For wander's lay
that is 1/s², the form of the inverse-square law (`thin.html`: the share of a signal one standpoint catches falls as
1/d²).

## Keep the case

s = v/h is a ratio of fill levels: geometry, with no scale. The inverse-square law is about a distance d: physics. The
bridge is to read s as d counted in the reader's own breadth, s = d/H, which needs H, and which is a reading of amounts.
So the most a run here can show is that the lay has the inverse square's **form**. It cannot show that the lay is light
or gravity. Whether the two share a cause is the reading after the runs, and it stays a reading.

## What is measured

Three lays, all with the corner at radius 1 and the horizon at radius 2:
- **W**, wander's: ρ = s for s ≤ 1, 2 − 1/s past it.
- **D**, draw's: ρ = s for s ≤ 1; in level k (2^k ≤ s ≤ 2^{k+1}), linear from 2 − 2^{−k} to 2 − 2^{−(k+1)}.
- **T**, the sweep, as a control: ρ = 2·(2/π)·atan(s), which also runs from 0 through 1 at the corner to 2 at the horizon.

For each lay:
- the room per unit reading, ρ′(s);
- the room each level gets, ρ(2^{k+1}) − ρ(2^k);
- the log-log slope of ρ′ against s over s from 2 to 2^20.

The flip is also measured: write the far field in the flipped reading u = 1/s, which is h/v.

## Predictions

- **P1 (exact, W).** ρ′(s) = s^(−2) for every s > 1, to rounding (relative error under 1e−12 at 2,000 points, s from 1 to
  2^30). Each level gets 2^{−(k+1)} of the room, so the room per unit s, averaged over level k, is ½·4^{−k}: it falls by a
  factor of exactly 4 per doubling of s, as the inverse square does. *Killed* if any point misses by more than 1e−12, or
  any level's room is not 2^{−(k+1)}.
- **P2 (the flip).** In the flipped reading u = 1/s ∈ (0, 1], wander's far field is ρ = 2 − u: plain proportion, room 1
  per unit u. So the inverse-square form in s is exactly the flip's Jacobian, |du/ds| = 1/s². *Killed* if ρ(1/u) + u − 2
  misses 0 by more than 1e−12 anywhere on u ∈ (0, 1].
- **P3 (D, draw's lay).** Within level k the room per unit s is constant, 2^{−(k+1)}/2^k. So s²·ρ′(s) runs from ½ at the
  level's inner wall to 2 at its outer wall, and is exactly 1 at its geometric middle, s = 2^{k+½}. Averaged over a
  level it is the inverse square, though not pointwise. *Killed* if s²·ρ′ leaves [½, 2] anywhere past the corner, or
  misses 1 at a geometric middle by more than 1e−12.
- **P4 (slopes).** The log-log slope of ρ′ against s over [2, 2^20] is −2 within 0.005 for W, and within 0.02 for D (a
  least-squares fit over 400 log-spaced points). For T it is also −2 within 0.02, because atan(s) = π/2 − 1/s + O(1/s³):
  far out, any lay that reaches a finite horizon as a smooth function of 1/s has room 1/s². *Killed* if any of the three
  is outside its band.
- **P5 (the near field is not).** Below the corner W and D give room 1 per unit s (proportion), not 1/s². The
  inverse-square form belongs to the far field only. *Killed* if ρ′ ≠ 1 on (0, 1) for W or D.

## What would not be shown

- That the lay is the cause of the inverse square, or the other way round.
- Which inverse square. Light's 1/d² is a solid angle, the square of an angle (two dimensions). The lay's 1/s² is the
  derivative of one angle-like quantity, 1/s (one dimension). P2 says the lay is linear in 1/s, which is the angular size
  Δ/d of a thing of size Δ at distance d. So the lay may correspond to an angular size, and the inverse square of light
  to that size squared. Two readings of one fact, or two facts with one form: that is for the reading after the runs, not
  for the runs.

## Runs

