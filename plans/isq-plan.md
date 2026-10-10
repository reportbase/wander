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

### Run 1 (10 October 2026)

`python3 plans/isq/isq.py`, output in `plans/isq/isq-run1.txt`:

```
P1: not killed. max |s^2 W'(s) - 1| = 2.2e-16 (as written), 8.6e-02 (central difference on W); level rooms 2^-(k+1) exactly: True; room per unit s over level k = 1/2 * 4^-k, quartering per doubling exactly: True
P2: not killed. max |W(1/u) + u - 2| = 2.2e-16 on u in (0, 1]: the far field is proportion in h/v, room 1 per unit u
P3: not killed. s^2 D'(s) from 0.5017 to 1.9931; at the geometric middles misses 1 by at most 2.2e-16; D - W at the walls 0.0e+00
P4: not killed. slopes: W -2.0000, D -1.9953, T (the sweep) -1.9961
P5: not killed. max |rho'(s) - 1| below the corner: 0.0e+00 (W and D), 5.3e-10 (W, central difference)
reading: the sweep T at s = 1 gives s^2 T' = 0.6366, at s = 2 1.0186, at 2^10 1.273238 (-> 4/pi = 1.273240)
```

- **All five not killed.** P1's kill was on ρ′ as written and on the exact level rooms; both hold to rounding.
- **The 8.6e−2 is rounding, not the lay.** A second, numerical check on P1 (a central difference taken on W itself) reads
  8.6e−2 at its worst. It is not part of the kill. It is floating-point cancellation: W is nearly 2 out there and the
  step changes it by about 1e−6/s. Measured by range after the run, its worst miss is:

  | s up to | worst miss |
  |---|---|
  | 2^5 | 3.4e−9 |
  | 2^10 | 9.5e−8 |
  | 2^15 | 3.2e−6 |
  | 2^20 | 7.9e−5 |

  It grows with s as rounding does. The exact level rooms, in fractions, are the check that does not round.
- **The sweep T** (the control) has room 1/s² only far out. There s²·T′ → 4/π, the sweep's constant, not 1. At the corner
  it is 2/π.

## Reading (after the run; not ruled)

- **The lay has the inverse square's form, and the form is the flip's.** Past the corner the in-place lay is plain
  proportion in the flipped reading u = 1/s = h/v (P2). Its room per unit s is therefore the flip's Jacobian, 1/s² (P1).
  Any lay that reaches a finite horizon smoothly in 1/s, the sweep included, ends with the same form far out (P4).
- **Which inverse square.**
  - Read s as a distance in units of a size, s = d/Δ (the bridge: amounts, needing Δ). Then 1/s is the angular size Δ/d,
    and the lay places a thing at its angular size, counted down from the horizon: 2 − ρ = 1/s.
  - The lay's 1/s² is then how fast an angular size shrinks with distance, |d(Δ/d)/dd| = Δ/d². That is an inverse square
    in one dimension.
  - Light's inverse square (`thin.html`) is the solid angle, (Δ/d)², the angular size squared: an inverse square in two
    dimensions.
  - Both come from the flip, s ↦ 1/s: one is the flipped reading's rate of change, the other its square. They are two
    readings of one fact, not two facts that happen to share a form. That is a reading of the arithmetic above, not a
    test of physics.
- **The near field is not.** Below the corner the lay is proportion in s itself (P5), so the inverse-square form belongs to
  the far field alone. That fits the paper's split: proportion before the corner, levels past it.
- **Draw's piecewise lay** is the inverse square level by level, not pointwise (P3). It is exact at each level's
  geometric middle and within a factor of 2 either side.
