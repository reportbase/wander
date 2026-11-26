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

