# AMP: does error add, multiply or vanish across the levels?

*Plan, prediction and kill written 9 October 2026, before the script was written or run (Claude, on a review Gemini
offered and Tom passed on; Gemini then asked for this plan and for the metric to be fixed before any run). SPN §3.3
leaves open how "amplification grows with depth": it "appears to add across levels rather than multiply … not derived".
The measurements are the format paper's (§2.8), which is not in this repository, so amplification is defined here afresh.
Synthetic. The lab rules hold: nothing above the "Runs" line is edited after the run. **Not yet run: for Tom's review of
the metric first.***

## Keeping the case

Everything here is geometry, in fill levels: the sweep's coordinate g from 0 to 1, each level's own coordinate x from
0 to 1, and every value and error as a fill level of that level's range. No breadth H or V, no distance, no amount
enters (SPN's opening warning; §1, "Checking an argument").

## The levels

- **The lay:** the in-place lay on the bounded sweep. Level 0 runs from home to the far wall, g ∈ [0, 1]; level k is
  entered at its home g = 1 − 2⁻ᵏ and runs to the far wall, nested in its parent's back half. Its own coordinate is
  x = (g − (1 − 2⁻ᵏ)) / 2⁻ᵏ. K = 8 levels.
- **What a level holds:** N = 16 rows, a series in cos(nπx), n = 0 … 15, on its own support (the format's rows; flat at
  both ends, as the format's presentation is).
- **The target:** built so every level has detail of its own and the reconstruction is exact before any error is put in:
  T = Σₖ Tₖ, with Tₖ a seeded 16-row cosine series on level k's support, amplitudes 2⁻ᵏ (detail shrinking with depth).
  Baseline error below 10⁻¹².
- **The error in, for nestings 1 and 3:** δ = 10⁻³ (a fill level) added to level j's held values, in two shapes:
  - *flat:* a constant offset over level j's support (representable by any level's row n = 0);
  - *sloped:* a ramp δ·x over level j's support (not exactly representable by flat-ended rows; the wall's case, §3.3,
    "The walls").

## Three ways to nest

1. **Fixed frames, own band (P1).** Each level's support is laid by the geometry (its home at g = 1 − 2⁻ᵏ, fixed before
   anything arrives), and each level holds its own band Tₖ, decided beforehand, not re-read from what the levels above
   hold. A level's error therefore stays a level's error.
2. **Frames from the parent's reading (P2).** As 1, but each child's home is placed where its parent *reads* its own
   corner, not where the geometry lays it, and each child reads its own corner in its own coordinate the same way. The
   error in is a misreading of level j's corner by δ in level j's coordinate x; it moves the child's frame, which moves
   the grandchild's.
3. **The child re-reads the parent's leftover (P3).** Frames fixed as in 1, but each child holds what is left on its
   support after every level above it: Rₖ fits T − Σ_{i<k} Rᵢ there. The child sees the parent's error as residual.

## The metric

For each region k (the part of the sweep where level k is the deepest level entered, g ∈ [1 − 2⁻ᵏ, 1 − 2⁻⁽ᵏ⁺¹⁾), and
the last level's whole support), the error out is, for nestings 1 and 3, the largest |R − T| there (a value, a fill
level); for nesting 2, how far level k's frame stands from where the geometry lays it, **in level k's own coordinate x**
(so frames deep and shallow are compared alike; on the bounded g a deep level is tiny, and a shift measured in g would
look small for that reason alone). The amplification from j to k is

  A(j → k) = (error out in region k with δ put in at level j − the same without) / δ.

Why this and not the two alternatives Gemini asked about: the error at the deepest level alone hides the regions only a
parent covers, where a child cannot correct anything; an error integrated over all levels mixes regions of different
widths, so the bounded sweep's squeeze would decide the answer. Per region, in each level's own units, is the reading a
situated reader would have at that level.

Also measured: δ put in at several levels at once (j = 1, 3, 5), to see whether their effects in region 7 sum.

## Reasoning, before running

- **P1:** a level's band is its own, and its frame is the geometry's, so an error at level j appears in every region
  its rows reach (j and all below) once, unscaled, and nowhere else. Several errors meet in a deep region as a sum. This
  is the adding that §3.3 reports, derived from the levels being laid in advance.
- **P2:** a child's own coordinate is twice as fine as its parent's (its support is half as wide in g). A shift of δ
  in the parent's units is 2δ in the child's, 4δ in the grandchild's: doubling per level, compounding.
- **P3:** a flat error is exactly what a child's row n = 0 can hold, so every child below j takes it up and region k > j
  is left clean; a sloped error cannot be held at a child's flat ends, so a little is left beside each child's walls.

## Prediction

- **P1 (the kill): additive.** Flat error: A(j → k) = 1 within 1% for every k ≥ j, and 0 (below 10⁻⁹) for k < j; with δ
  at j = 1, 3, 5 together, the change in region 7 is 3δ within 1%. Sloped error: A(j → k) is the ramp's own largest value
  in region k, 1 − 2⁻⁽ᵏ⁻ʲ⁺¹⁾, within 1% (the error passes down unchanged, neither grown nor shrunk).
- **P2 (the kill): compounding by 2.** The frame shift A(j → k), k > j, grows by a factor between 1.8 and 2.2 per level.
- **P3 (the kill): masked.** For a flat error, A(j → k) below 10⁻⁶ for every k > j; for a sloped error, below 0.1 for
  every k > j, with at least 80% of what is left within the outer tenth of each child's support (beside its walls).

## Kill

- **P1 killed** if a flat A(j → k), k ≥ j, is outside 0.99–1.01, or above 10⁻⁹ for k < j, or the three-error sum in
  region 7 is outside 2.97δ–3.03δ, or a sloped A(j → k) is more than 1% from 1 − 2⁻⁽ᵏ⁻ʲ⁺¹⁾.
- **P2 killed** if the per-level growth is outside 1.8–2.2 at any depth.
- **P3 killed** if a flat error leaves A ≥ 10⁻⁶ below level j, or a sloped one leaves A ≥ 0.1, or less than 80% of the
  sloped leftover lies beside the walls.

## What it would mean

- If P1 and P2 hold, the adding in §3.3 is derived: it follows from the levels being geometry, laid before anything
  arrives, and a reader that placed its levels from its own readings would compound instead. That is a reason the
  levels must be compile time, beyond economy.
- If P3 holds, a reader that re-reads what the levels above left does better than adding: it masks the errors above it,
  except what the flat-ended rows cannot hold at the walls. The wall slope (§3.3, "The walls", 7 October) then sets the
  size of the only error that survives, and the measured "adding" would be the sum of those wall terms.
- Which of P1 and P3 the format paper's reader is, its definition will say; this plan does not decide it.

## Runs

*(none yet)*
