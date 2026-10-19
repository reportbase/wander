# SKY: a sky of moving bodies, tracked by the inscribed sweep alone

*17 October 2026 (Tom's local date). Tom, 21:38: "thats wonderful, so we can track a sky full of objects with the
inscribed sweep?"; Claude: yes in principle, with five things untested (which patch is which, occlusion, turning
profiles, bodies below one address, sizes). Tom, 21:41: "the next test is a sky of 40 moving bodies, written
prediction-first. It would check: each body's turn read exactly; time to contact for the resolved, unhidden bodies;
matching patches tick to tick from detections alone, correct everywhere except where patches touch or overlap; the far
ones tracked as single cells; nothing moving when the world is scaled." Geometry plus a clock; the predictions are
written before any code.*

## Known beforehand

- RSH run 4 (`plans/rsh-plan.md`): one reader's sweep of the whole wedge keeps its addresses whatever is met; a body's
  share × π/2 is its solid angle; scaling the world repaints nothing.
- MON (`plans/mon-plan.md`, run 2 and the smooth post hoc): one moon's turn ω read from its patch to 0.25%; its time to
  contact τ = 2s/ṡ exact for a smooth moon (1.2%) and off by up to 9% for one with relief over a 44° turn of the line of
  sight, the share taking in the profile turned; detections unmoved by scaling.
- MOT (`plans/mot-plan.md`): τ and the path angle from the clock alone.
- RSH run 3: occlusion orders bodies and never sizes them; a body nearer than another can hide it whole.
- Classical: multi-target tracking (data association: Reid 1979's multiple hypothesis tracking, Bar-Shalom's
  probabilistic data association; the simplest, gated nearest neighbour with a constant-velocity prediction, used here).
  Tracks are lost or swapped where targets are not resolved from one another; that is the known failure.

## Set-up

**The sky.** The reader at home O; 40 Levels bodies (`bodyOf(0 … 39)`, every band in full, stretched as Levels makes
them), their centres in directions within 30° of (1, 1, 1), at distances log-uniform on [16, 16384] (ten doublings),
seeded (seed 3); no two bounding balls meeting at any tick. 32 of them move freely; 8 are planted in 4 crossing pairs:
at the middle tick a far body lies on the ray from O through a near one's centre, at 1.5 to 3 times its distance, and the
two move across one another. Every body moves in a straight line at constant velocity: its turn as seen from O, at the
start, 3 to 10 cells a tick in a random direction across the line of sight, and its radial speed d/τ₀ with τ₀ drawn from
±[30, 300] ticks (approaching or receding). 25 ticks, t = 0 … 24.

**The inscribed sweep.** 2048 × 2048 addresses even in azimuth and height over the whole wedge (as RSH run 4, Lambert's
equal-area grid; one cell about 7.7·10⁻⁴ rad across). A cell is a detection when the ray through its middle meets a body,
and also the cell holding a body's centre direction (a body under a cell lights the cell it lies in, as a point source
lights its pixel); a detection says only "met", not which body. The referee (not the reader) labels each detection with
the body met first (nearest along the ray), or, for a lit centre cell no ray meets, with that body.

**From the detections alone.** Patches are the connected groups of detected cells (8-neighbours) each tick. A patch's
direction is the mean of its cells' directions, normalised; its share is its cell count × (π/2)/N. A tracker links each
tick's patches to the last: each track predicts its next direction from its last two (constant velocity on the sphere),
and takes the nearest unclaimed patch within a gate of 3 cells plus twice its last step; patches left over start new
tracks, tracks left over coast up to 2 ticks. Turn ω of a track: the angle between its directions 2 ticks apart, over 2;
over the whole run, its first and last directions over the ticks between. τ: 2 over the least-squares slope of ln s over
five ticks.

**Clean and touching.** A patch is clean at a tick when the referee's labels in it are all one body and that body's
detections are all in it. A body touches at a tick when its patch is not clean (another body's cells joined it, or it is
partly or wholly hidden behind a nearer body, its labels absent or split).

### Predictions

- **S1 (nothing moves when the world is scaled).** Scaling the world by k = 10⁻³, 7, 10³ (every place, size and speed, the
  same ticks) leaves every tick's set of detections the same, but for at most 10⁻⁴ of them. *Killed* if more differ.
- **S2 (each body's turn).** For every body clean at t − 1, t and t + 1 and at least 50 cells, ω(t) from its patch within
  1% of the true angular rate of its centre seen from O; for every body under one cell all run long, its whole-run turn
  from its lit cells within 2 cells' angle (over 24 ticks) of the true. *Killed* if any misses.
- **S3 (time to contact).** For every body clean over five ticks t − 2 … t + 2 with at least 2,000 cells each tick, τ(t)
  within 3% of the true d/(−ḋ) (or its negative for a receding body). *Killed* if any misses.
- **S4 (matching from detections alone).** Every link the tracker makes between two ticks at which the linked patches are
  both clean joins the same body (no swap); every body clean at both ends of a tick pair is linked across it (no loss);
  every wrong or missing link falls at a tick pair where some body touches. At least one link is wrong or missing at a
  touch (the planted crossings), or the prediction's last clause is untested and I say so. *Killed* if any clean–clean
  link is wrong or missing.
- **S5 (the far ones as single cells).** Every body under one cell (its angular radius under half a cell) that is not
  hidden is exactly one detected cell each tick, the cell holding its centre direction, and its track is one tracker
  track over all 25 ticks. *Killed* if any is not.

S1 and S5's first part are near identities (a kill would be my code); S2 and S3 are MOT and MON's readings, many at once;
S4 is the claim that the inscribed sweep's detections alone keep the sky's bodies apart wherever their patches do not
meet.

## What would and would not be shown

That one sweep of fixed addresses tracks a sky of moving bodies at once, each in ratios and ticks, its identity kept
from tick to tick by its patch alone wherever patches stay apart, and lost only where they touch or one hides another;
that far bodies are tracked as single cells, with turn but without share. Not sizes or distances (no amount carried in),
not light, and not how a real sky's detections are made.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (17 Oct, `node runs/sky/sky.mjs`; output `runs/sky/sky-run1.txt`, 17 min)

One choice the plan left open, made before running: a track seen once has no last step, so its gate takes the largest
step a body is given, 10 cells. The sky: 40 bodies, d 23 to 15,218 at the middle tick, 36–40 patches a tick, 10 bodies
under one cell all run; touches at 18 of 25 ticks (up to 4 bodies at once, the planted crossings).

- **S1 not killed:** under k = 10⁻³, 7, 10³ none of 1,423,461 detections differs.
- **S2 killed:** 187 readings of ω on clean patches of 50 cells or more, worst 2.86% (median 0.3–0.7%); the 10 bodies
  under one cell, whole-run turn within 0.68 of a cell.
- **S3 killed:** 50 readings of τ on 4 bodies of 2,000 cells or more, worst 6.83%.
- **S4 not killed:** 44 tracks, 921 links; over 898 clean–clean tick pairs no link wrong and none missing; 17 links at
  touches joined a patch to another body's or a merged patch (the last clause tested).
- **S5 not killed:** all 10 bodies under one cell were one cell at their centre direction every tick, each one track over
  all 25 ticks.

**Post hoc** (`runs/sky/sky1-posthoc.mjs`; outputs `runs/sky/sky1-posthoc.txt` and, with the relief taken off,
`runs/sky/sky1-posthoc-smooth.txt`). τ: taking off the relief does not help (worst 7.41%). The error is the cells': ln s scatters
0.2–0.8% about its five-tick line (a patch's edge cells come and go), and τ = 2/slope turns that scatter into
σ·|τ|/(2√10) of τ, 3–9% for these bodies (true |τ| 30 to 150 ticks). The observed errors follow it (body 12, τ 34: 1.4%;
bodies 1, 17, 32, |τ| 115–150: 4–7%). My threshold took no account of |τ|: a body far from contact changes its share by
a few tenths of a percent a tick, near the cells' own scatter, so its τ is read worst. ω: without relief the patches of
1,000 cells or more read within 0.96% (worst 2.86% with it), and the small ones (50–200 cells) scatter to 2.75% either
way: S2's 1% was too tight for small patches (the centre's own cell scatter over a step of 6 to 20 cells) and, for large
ones, the relief's turning profile moves the centre as MON found.

**Reading.** The inscribed sweep's detections alone keep a sky of moving bodies apart: every clean link right, every
body under a cell held as one cell and one track, identity lost only where patches touch or one hides another, and
nothing moving when the world is scaled. What the detections give each body (ω, τ) is as good as its patch is many
cells: ω to well under 1% for large smooth patches, τ to the cells' scatter times |τ| over the window, so a body far from
contact (large |τ|) is read worst; the relief adds its turning profile to both.
