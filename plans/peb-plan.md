# PEB: the pool engine and the Tangent Bridge

*26 November 2026. Tom: "Let's take another look at the pool engine. It works very well for pool. Does it work with
tangent bridge.", then "Yes, write the plan". Plan only; predictions written before any script (`runs/peb/`) exists.
The engine is wander's `play-trick.html` (moved whole into reportbase/games as `TRICK_APP`; the test runs on wander's
copy, driven headless through `window.__trick` as ENG was).*

## What the engine is, and where the bridge can enter

ENG (R1080) found no trigonometric call in the physics (contact on h + v = 1, cushions as mirror images, spin and grip
written as amounts) and 12–13 a shot elsewhere: the aim angle turned into a direction (`Math.cos(ang)`, `Math.sin(ang)`
in `simulate`, `strikeOf`, `aimAt`), the cue's elevation, `atan2` for the struck direction and `asin` for the recorded
cut. The world frame, the shared tick and the integrator are the DHV's and stay so. The bridge can enter in two places.

1. **The aim in slopes.** Hold the aim as a half-slope t = tan(a/2): the direction is ((1 − t²)/(1 + t²), 2t/(1 + t²)),
   rational; a turn of the aim is tangent addition; fine aims are the leaf lattice (halving from the corner, TB §11.1), so
   an aim on the lattice is two integers (depth, k). The test copy (`runs/peb/play-trick-slope.html`, made by the
   script from `play-trick.html`, the original untouched) takes the struck direction as a pair, and turns `strikeOf`'s
   elevation and returned direction into slopes the same way.
2. **The shot map on the aim circle.** What a shot does as a function of the aim, at fixed power, spin and layout, is a
   function on the circle: where the cue ball and the object ball stop. Between aims where the shot's sequence of contacts
   (which ball or cushion, in which order) changes, it is smooth; at those aims it jumps. The bridge's policy for
   jumps (TB §15.1) is to carry each as a record (its aim, found by bisection) and bridge each smooth piece on its own.

## Predictions

Shots: the layouts rack, scatter, line, jump and masse, 12 seeded shots each (aim, power, tip, elevation as ENG), and
every challenge's reference shot.

- **P1 (the same shots, no trig).** Every shot struck through the slope path matches the angle path: every ball's final
  position within 10⁻⁹ table units and the same sequence of contacts; the trigonometric calls a shot makes through the
  slope path, counted on every Math entry point as ENG counted them, are 0.
- **P2 (an aim that replays).** For 60 seeded aims recorded as the engine records them (degrees, `ang / D`) and
  replayed (`deg * D`), at least one shot's final positions differ from the original by more than 10⁻⁹ (the round trip
  loses a bit and the contacts amplify it, POL run 8); recorded instead as lattice aims (depth 12, an integer k), all 60
  replay with every final position identical to the last bit.
- **P3 (the shot map, jumps carried, pieces held).** On three layouts (a single cut on the open table, the challenge
  "two rails", the rack's break) at fixed power and no spin, the aim scanned at 1,024 lattice aims round the circle;
  where the contact sequence differs between neighbouring aims, the jump located by bisection to 10⁻¹² rad. On every
  piece wider than 10⁻⁴ rad, the cue ball's and the object ball's final positions are held by a bridge on the piece
  (Chebyshev leaves from the lattice, barycentric) to ≤ 10⁻⁶ table units with some K in {6, 8, 12, …, 128}, for at least
  90% of those pieces.
- **P4 (a contact costs leaves).** Over the pieces of P3, the median K* grows with the number of ball-to-ball contacts in
  the piece's sequence: the median at two contacts at least 1.5 times the median at one, and at three at least 1.5 times
  that at two (POL run 8: an aim error grows about 2^L over L contacts, so a piece's outcome bends more with each).

Each is killed by its own number. Known beforehand: ENG (where the trig is), POL runs 8–9 (the aim's sensitivity, exact
contact), TB §11.1 (the lattice), §15.1 (jumps as records), CUE (the engine's grip, which is smooth in speed and so keeps
pieces smooth). P4's growth rate is a guess from POL; the pieces also narrow with more contacts, which works against it.

## What would follow, if nothing is killed (a reading, to rule on)

The engine runs whole with no trigonometric call, its aims are exact objects that replay anywhere, and what a shot does
across all aims is held by the bridge piece by piece, the pieces' edges the moments a contact begins or ends. The read's
form reaches the whole game; what stays the DHV's is the frame, the clock and the integrator, as ENG found.

## Runs

### Run 1 (26 November 2026; `runs/peb/peb.mjs`, output `runs/peb/peb-run1.txt`)

- **P1 not killed.** All 75 shots (five layouts × 12 and the 15 challenges' reference shots) struck through the slope path:
  largest difference from the angle path in any final position 6.2·10⁻¹³, the same contact sequence in 75 of 75, and 0
  trigonometric calls in every slope shot.
- **P2 killed, by my guess.** The degree round trip moved none of the 60 shots (largest difference 0): `(ang / D) * D`
  gave back the same double, or a bit the contacts did not amplify past 10⁻⁹, every time. The lattice aims replayed
  identically, as predicted, but so did the degrees: on this engine degrees replay too.
- **P3 killed.** 22 of 275 pieces held to 10⁻⁶ with K ≤ 128 (cut 5 of 36, two rails 8 of 45, rack 9 of 194).
- **P4 killed.** The median K* is "more than 128" at every count of contacts, so it cannot grow.

Post hoc (`runs/peb/peb1-posthoc.mjs`, not predicted): the pieces are not smooth. On the cut's piece round the direct hit
(aims 0.22604 to 0.27837 rad, one contact sequence throughout, the same cushion and the same frame count at the jump
found), scanning 100,000 aims 5.2·10⁻⁷ rad apart finds **26 jumps in the cue ball's or the object ball's rest position,
from 10⁻⁴ to 1.2·10⁻²**, where the usual step is 3·10⁻⁵. A bridge on that piece is stuck at about 5·10⁻³ from K = 12 to
K = 384, with its worst point at one of them. Their source is the integrator, not the table: a ball's slip that falls
below 3.5·MU_S·h is removed at once, "within this tick" (`cloth`), so the moment a ball starts to roll is a whole tick,
and as the aim moves that tick steps from one to the next, and the rest of the ball's path moves with it. The contact
sequence does not change, so P3's signature (contacts, cushions, pockets) never saw these jumps.

### Standing after run 1

Not killed: P1. Killed: P2 (my guess about rounding), P3 and P4 (the pieces carry the integrator's jumps).

- **The whole shot runs on slopes, with no trigonometric call** (P1): the aim as a half-slope, the elevation likewise and
  the recorded cut as its sine reproduce every shot of the angle path to 6·10⁻¹³ with the same contacts.
- **What a shot does across the aims is not the table's alone.** Between contacts the map from aim to outcome jumps
  wherever the integrator's tick for a ball's slip ending steps on. Those are the DHV's jumps: the clock and the
  integrator, which ENG had already left to the DHV. The bridge's policy (jumps as records, pieces bridged) holds only
  once the integrator's events are recorded as jumps too, or once the integrator gives the slip's end its exact moment, as
  POL run 9 gave contact its exact moment.

### Run 2, predicted before it runs

The slope copy's `cloth` given the slip's end at its exact moment within the tick: when the slip would be gone within h,
the ball slides for the time τ = |u|/(3.5·MU_S) it needs, then rolls for h − τ (its motion and spin set by the same
−(2/7)·u, the position advanced by the sliding part and the rolling part each for its own time). Everything else as run 1.

- **P1′.** As P1, on the new copy against itself through both paths: final positions within 10⁻⁹, the same contacts, 0
  trigonometric calls.
- **P3′.** As P3 on the new copy: at least 90% of the pieces wider than 10⁻⁴ rad held to 10⁻⁶ with K ≤ 128.
- **P4′.** As P4 on the new copy.
- **P5 (the hidden jumps gone).** On run 1's post hoc piece, at the same 100,000 aims, no step in a rest position exceeds
  20 times the median step.

The rolling ball's stop (`ns = max(0, sp − MU·h)`) is also clipped at a tick; P5 tests whether that clip leaves jumps of
its own (it should not: a stop clipped within a tick changes the rest position continuously).

### Run 2 (26 November 2026; `runs/peb/peb2.mjs`, output `runs/peb/peb-run2.txt`, copy `runs/peb/play-trick-slope2.html`)

- **P1′ not killed.** 75 shots, largest difference 5.8·10⁻¹³, the same contacts in 75 of 75, 0 trigonometric calls.
- **P3′ killed.** 23 of 285 pieces held (cut 6 of 36, two rails 7 of 45, rack 10 of 204).
- **P4′ killed.** Every median K* more than 128.
- **P5 killed.** On run 1's piece, 23 steps past twenty times the median (3.2·10⁻⁵), the largest 1.2·10⁻² (run 1: 26).

The slip's end was not the main source. Post hoc (`runs/peb/peb2-posthoc.mjs`): the largest remaining jump, bisected to
two aims 5.6·10⁻¹⁷ rad apart, has the one contact at the same moment (0.4041667 s, to 10⁻¹⁶: on a sub-tick boundary,
97 ticks of 1/240 s) and the two paths identical up to it, then 1.6·10⁻³ apart one frame later and growing. The contact
is found exactly (POL run 9) and the motion since it is moved forward (`du·τ`), but **the cloth's grip on the slip the
contact makes starts only at the next tick**: a contact just after a tick boundary waits almost a whole tick before the
cloth acts on it, one just before waits almost none. With the cloth's grip at MU_S = 30 that tick of free sliding is a
step in the balls' paths. A cushion contact (`tau` likewise) has the same delay.

### Run 3, predicted before it runs

The run 2 copy, and after every exact contact (ball on ball, and ball on cushion, where τ is the time since contact
within the tick) each ball touched is given the cloth for τ at once (`cloth(b, τ)`, with its position moved by what that
changes over τ), so the cloth acts from the moment of contact. Everything else as run 2.

- **P1″, P3″, P4″, P5″:** as P1′, P3′, P4′, P5 on the new copy (`runs/peb/play-trick-slope3.html`).

### Run 3 (26 November 2026; `runs/peb/peb3.mjs`, output `runs/peb/peb-run3.txt`, copy `runs/peb/play-trick-slope3.html`)

- **P1″ not killed.** 75 shots, largest difference 4.6·10⁻¹³, the same contacts in 75 of 75, 0 trigonometric calls.
- **P3″ killed.** 29 of 283 pieces held (cut 7 of 36, two rails 9 of 45, rack 13 of 202).
- **P4″ killed.** Every median K* more than 128.
- **P5″ killed.** 23 steps past twenty times the median; the largest now 3.3·10⁻³ (run 2: 1.2·10⁻²).

Post hoc (`runs/peb/peb3-posthoc.mjs`): the same contact on the same tick boundary, the paths now 6·10⁻⁵ apart one
frame after it and growing by about 8·10⁻⁵ a frame, a difference in speed of about 0.005 = MU·h. A contact found at the
end of a tick comes after `own` has already given both balls the cloth for that whole tick on their motion from before
the contact, including the τ after it; found at the start, it has not. So the balls carry τ of the old drag too many.

### Standing after runs 1–3

Not killed: P1, P1′, P1″. Killed: P2 (my guess), P3–P5 in every run.

- **The engine runs whole on slopes** (P1 three times): the aim and elevation as half-slopes, the cut as its sine, every
  shot the angle path's to 5·10⁻¹³ with the same contacts and no trigonometric call.
- **The shot map is the table's only once the integrator is.** Each run removed one way the fixed tick writes an event
  into a whole tick (the slip's end; the cloth after a contact) and the largest hidden jump fell (1.2·10⁻² → 1.2·10⁻² →
  3.3·10⁻³), but each event the integrator rounds to a tick is a jump in what a shot does across its aims, and there are
  more (the cloth before a contact, now; the cushion's likewise; a stop; a pocket). The pieces the bridge would hold are
  the pieces between the integrator's events, not between the table's.
- A reading, to rule on: the bridge's policy (jumps as records, smooth pieces bridged) asks of an engine that every event
  be placed at its own moment, as POL run 9 did for contact. That is event-driven integration, classical; the fixed tick
  is the DHV's clock, and its rounding is what the bridge sees.

A run 4 would take the cloth before a contact back to the contact's moment (each ball's cloth rate over the tick kept
by `own` and τ of it given back before the response). Not written as a prediction, since each run so far has found the
next rounding; whether to go on to a whole event-driven step is Tom's call.

### Run 4, planned (26 November 2026; Tom: "1a, write the plan"). Predictions written before any script exists

Runs 2–3 placed two of the fixed tick's events at their moments, and each time the next rounding showed. Run 4 replaces
the clock for the test: an **event-driven integrator** in a new copy (`runs/peb/play-trick-event.html`, made by a script
`runs/peb/peb4.mjs` from `play-trick.html`, the original untouched), as POL run 9 did for contact alone.

**The integrator.** On the cloth every ball's motion between events is a closed form in time, exactly as the engine's
own rules write it: sliding, the slip u shrinks at 3.5·MU_S along a fixed direction, so velocity is linear and position
quadratic in t; rolling, the speed falls at MU along a fixed direction, again linear and quadratic; side spin wears off
linearly and touches neither. The events, each found as the least root in the step ahead:
- a slip ends (t = |u|/(3.5·MU_S)); a rolling ball stops (t = speed/MU);
- two balls touch (|Δx(t)|² = (r_a + r_b)², a quartic in t, its least root found by bracketing on the quartic's own
  values and bisection to 10⁻¹⁵ s, then one Newton step; no trigonometric call);
- a ball reaches a cushion (gap = r, a quadratic) or a pocket fills its view (a quartic, as the engine's POCK test);
- the shot's end (no ball moving).
At each event the engine's own response is applied at that instant (`respond` and the grip for balls, the cushion's
mirror image and rail grip for cushions, the same constants), with τ = 0, so no correction is carried. Contacts that fall
within 10⁻¹² s of each other are resolved together, as ENG run 2 resolved them. Shots that leave the cloth (a jump, a
massé's lift) are out of scope: the layouts used here are all on the cloth, and a shot that leaves it is counted, not
run.

**Shots.** As P1 for the slope path (the layouts rack, scatter and line, 12 seeded shots each, elevation 0, and the
challenges whose reference shot stays on the cloth). As P3 for the shot maps (the cut on the open table, the challenge
"two rails", the rack's break; 1,024 aims; jumps bisected to 10⁻¹² rad on the contact signature).

- **Q1 (the referee).** The event engine is the fixed-tick engine's limit: on the 36 seeded shots, run 3's copy with
  SUB = 4, 16, 64 differs from the event engine in final positions by a median that falls at least ×3 for each ×4 in
  SUB (first order in the tick), and at SUB = 64 the contact sequence is the same in at least 30 of 36. If this fails
  the event engine is not the same table and nothing below counts.
- **Q2 (no hidden jumps).** On run 1's post-hoc piece of the cut (0.22604 to 0.27837 rad), at the same 100,000 aims, no
  step in a rest position exceeds twenty times the median step, and the largest step is under 10⁻⁴.
- **Q3 (pieces held).** On the three shot maps, at least 90% of pieces wider than 10⁻⁴ rad have both balls' rest
  positions held to 10⁻⁶ by the bridge on the piece (K in {6, 8, 12, …, 128}, as P3).
- **Q3a (a graze ends a piece with a square root).** Where a piece ends at a graze (a contact beginning or ending with
  the line of centres square to the closing velocity, |n·w| under 10⁻³ of |w| at the bisected aim), the rest positions
  near that end go as √(distance to the edge): a fit of log|Δx| against log(distance) over 10⁻⁹ to 10⁻⁵ rad gives a
  slope within 0.1 of ½ at at least 80% of graze ends. Ends that are not grazes give a slope within 0.1 of 1.
- **Q3b (the bridge in the root's chart).** On pieces with a graze end, bridged in u = √(a − a_edge) (or both ends'
  roots, for a piece with two graze ends the chart sending each end's root to ±1), at least 90% held to 10⁻⁶ with K ≤ 128.
- **Q4 (a contact costs leaves).** As P4 on the pieces held under Q3 or Q3b: the median K* at two ball contacts at least
  1.5 times that at one, and at three at least 1.5 times that at two.
- **Q5 (no trig).** The event engine's path, given the aim as a pair, makes 0 trigonometric calls (counted on every Math
  entry point, as P1).

Each is killed by its own number. Known beforehand: ENG run 2 (contacts resolved together, the stop taken off), POL runs
8–9 (exact contact, the aim's sensitivity), runs 1–3 here (the tick's jumps), and the classical form of a graze: a
contact's turn of the struck ball goes as the cut's sine, √(1 − f²) near f = 1, so a square root at the edge is expected
from geometry, not from the integrator. Q4's growth rate is the same guess as P4's; pieces also narrow with each contact.

What would follow if Q1–Q3b and Q5 are not killed (a reading, to rule on): with the clock's rounding removed, what a shot
does across all aims is held by the bridge piece by piece, the pieces' edges the table's events (a contact begun or ended,
a cushion, a pocket), the grazes square-root ends held in their root's chart; the fixed tick, the DHV's, was what the
bridge could not hold.
