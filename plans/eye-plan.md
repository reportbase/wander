# EYE: give the bar eyes

19 Nov 2026. SPN R1121. Tom: "the geometry is a gift, available to everyone.   maybe if we gave the bar eyes, see what
happens." After R1119 (the geometry is any extent's) and R1120 (something must map it onto something held).

## The set-up

A bar of length 1, its pivot at the origin, its trace at the other end. An eye is a point that maps each direction
arriving at it onto one of K receptors laid uniformly by turn over its quarter turn (the receptor's width ε = (π/2)/K in
the writer's angle; its boundaries at slopes tan(kπ/2K)). Things are points of the plane at distances 0.05 to 10⁴ bars.
Three placings: (P) one eye at the pivot; (T) one eye at the trace, the bar turned by Δ about the pivot; (B) eyes at
both ends, the bar held still. "Scale the world" multiplies every thing's distance by k with the bar unchanged; "scale
all" multiplies the bar too.

Known beforehand: HTP (an eye off a turning axis is moved a chord 2r·sin(Δ/2), a baseline; reach r·sin Δ/ε), PXC (two
standpoints a baseline B apart, the corner at d = B/2, relative error ∝ cosh(ln(2d/B)), far edge about B/ε), R1110
(the pivot points, the trace walks). So these predictions are mostly known; what is asked is what each end of the bar
gives when it is the one with the eye.

## Predictions (written before the script)

- **E1 (pivot, a uniform sky).** Directions uniform by turn land 1/K on each receptor; the receptors' boundaries are the
  half-Cauchy's quantiles, half below slope 1. Kill: any share off 1/K by more than 10⁻¹² (exact turn), or the median
  boundary not at slope 1 for even K.
- **E2 (pivot, no distance).** Scaling the world by k = 10⁻³, 7, 10³ changes no receptor fired, for every thing, and the
  bar turned about the pivot changes every direction alike: no two things' receptor gap moves by more than one receptor
  (rounding at a boundary), and no distance is recoverable. Kill: a receptor fired changed by scaling the world.
- **E3 (trace, turning gives distance).** Two looks from the trace before and after a turn Δ, with exact directions
  (K → ∞) and Δ known, place every thing exactly, in bars (error under 10⁻²⁰ at 50 digits). Scaling the world by k moves
  every place by k (in bars); scaling all moves none. Kill: any place off by more than 10⁻²⁰, or a place unmoved by
  scaling the world alone.
- **E4 (trace, with K receptors).** With directions read to the receptor's middle, the relative place error stays under
  ½ up to about sin Δ/ε bars (the reach, HTP), and is over ½ past 4× that. Kill: the half-error distance off sin Δ/ε by
  more than a factor 2 at Δ = π/2, K = 64, 256, 1024.
- **E5 (both ends, still).** The baseline is the bar. The relative place error per unit direction error, on the
  perpendicular bisector, is least at d = ½ (half a bar from the middle) and equal at d and 1/(4d). Kill: the least off
  ½ by more than 1%, or the d ↔ 1/(4d) values differing by more than 10⁻¹⁰.
- **E6 (the reading).** The pivot's eye gives directions only, whatever K; the trace's eye, turned, gives distances in
  bars; two eyes give distances without turning. So the pivot points and the trace walks (R1110), and "the bar" is the
  ruler only once an eye rides its trace. Kill: the pivot's eye turned yields any distance (a nonzero baseline).

## Runs

**Run 1** (`runs/eye/eye.py`, output `runs/eye/eye-run1.txt`, 50 digits). E1 not killed (every share 1/K to 10⁻⁵¹,
the median boundary slope 1). E2's kill clause not killed (scaling the world by 10⁻³, 7, 10³ changed no receptor at
K = 64, 1024); its gap clause killed by my code: the receptor index wrapped angles below 0 to 2π, so a turn of 0.3
moved gaps by 4K + 1 (257, 4097). E3 not killed (400 things placed to 3·10⁻⁴⁷ at turns of 30°, 90°, 150°; the world
scaled by 7 moves each place by 7 in bars, everything scaled by 7 moves none). E4 killed by my factor: the median error
reaches ½ at 2.36 to 2.54 times sin Δ/ε, not within 2 (the chord is √2 and a receptor's middle errs by ε/4 typically, not
ε; my estimate took neither); at 4× the reach the median read fails (rays crossing behind or not at all). E5 not killed
(least at d = ½ bar exactly, 2.0 there; d and 1/(4d) equal to 10⁻⁴⁷). E6 not killed (the pivot's eye does not move when
the bar turns: baseline 0, no distance).

**Run 2** (`runs/eye/eye2.py`, `eye-run2.txt`): E2's gap clause, the index counted from the receptor's zero without the
wrap: turned by 0.3, −0.7 and 1.1, no pair's gap changed by more than one receptor at K = 64, 1024 (E2′ not killed).

**Reading.** Where the eye sits on the bar decides what the bar gives. At the pivot: directions laid on K receptors,
the heat binned, nothing a scaling of the world moves, no distance, turning only slides every direction alike. At the
trace: the turn carries the eye along a chord, so a turn becomes a step and every thing is placed in bars, exactly with
exact directions, out to a few times sin Δ/ε with K receptors; scaling the world (the bar kept) moves every place by k,
so a place in bars is a write against the bar as an amount. At both ends held still: the bar is the baseline, the best
reading half a bar out, the same at d and 1/(4d): the bar's own exchange (R1117) about its half. All classical (HTP,
PXC); what is shown is that the pivot points and the trace walks (R1110) once each end is given an eye. The 2 in the
corner at ½ is the bar's whole length against parallax's half-baseline: the pair's corner sits at the bar's middle,
not its tip.
