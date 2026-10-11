# CUE: the trick-shot engine against the published laws of the game

*Plan and predictions written 11 October 2026, before any reference value was opened (Claude; Tom: "1,3", to "test its
physics against published measurements" and to play and feel). The engine is `play-trick.html`'s, the one the trick shots
and the challenges play on. This tests the engine, not the corpus: a simulation measured against the physics of the game
as published, with the same standing as POL runs 11–18 checking their gas against Enskog and Henderson
(`papers/physics.md` §2.4). The lab rules hold: nothing above the "Runs" line is edited after the run.*

## The data, and what it is

The measurements themselves are not reachable from here: Alciatore's technical proofs (billiards.colostate.edu), the
journals and arXiv are all blocked (checked 11 October; only GitHub and PyPI answer). What is reachable is **pooltool**
(Evan Kiefl; Apache-2.0; `pooltool_billiards-0.6.0.tar.gz` from PyPI, sha256
`1915bfabd429603da12de0d3d55a15bc4147859b4585376dd12f7239c631e3b0`), an open-source billiards simulator whose physics
models name their sources: a ball–ball friction law fitted to measured throw (attributed there to Alciatore), the cushion
models of Mathavan et al. (2010) and Han (2005), and default constants for the cloth and the balls.

So the reference for run 1 is **published laws and constants as one careful implementation states them**, read from its
source text and re-implemented here (the downloaded code is not run). That is a step below raw measurements: a law fitted
to data, or a model checked against data in its paper. Only the file listing was looked at before this plan was
committed: no value, formula or constant from it was read. If Tom can supply the raw tables (Alciatore's throw
measurements; Mathavan's measured rebounds), run 2 tests the same predictions against them.

## What was known before writing this (disclosed)

From memory, not from any file opened here, and so not evidence: real cloth grips a sliding ball with a coefficient near
0.2 and drags a rolling one near 0.01; balls of phenolic resin rebound with e near 0.93–0.96; and the grip between two
balls is not a constant, but is largest at slow speed and falls as they meet faster, so a slow cut throws the struck ball
more than a fast one. The engine has none of that last: its grip between balls is the constant MU_B = 0.06 at every
speed. I therefore expect P3 below to be killed. It is written as the engine claims, because the engine is what is tested.

## Units, and the bridge

The engine's table is in units of 0.45 per ball radius. A real pool ball's radius is 2.8575 cm (2¼ in across), so one
unit is 6.35 cm and a speed of v units a second is 0.0635·v m/s. Its gravity is G = 154 units/s² (9.81 m/s² in those
units), so a coefficient of friction is an engine acceleration over G. The bridge is the ball's size, a known kind (the
standard ball). The engine's constants, so read:

| constant | engine | as a coefficient |
|---|---|---|
| cloth on a sliding ball | MU_S = 30 units/s² | 30/154 = 0.195 |
| cloth on a rolling ball | MU = 1.2 units/s² | 1.2/154 = 0.0078 |
| ball on ball | MU_B | 0.06, at every speed |
| ball on ball, restitution | E_BALL | 0.96 |
| cushion, restitution | E_RAIL | 0.8 |
| cushion, grip on the ball's side | MU_C | 0.2 |

Speeds below: slow 7 units/s (0.44 m/s), medium 21 (1.33 m/s), fast 49 (3.11 m/s).

## What the engine predicts (computed and committed before the reference was opened)

`plans/cue/engine.mjs` drives the engine through its own `simulate` hook; output in `plans/cue/cue-engine.txt`.

**Throw from a cut** (the struck ball's direction against the line of centres; the white on +x just short of contact,
so a stun stays a stun), in degrees, at cuts of 10°, 20°, 30° (half-ball), 45° and 60°:

| | 10° | 20° | 30° | 45° | 60° |
|---|---|---|---|---|---|
| stun, slow | 1.50 | 3.06 | 3.43 | 3.44 | 3.44 |
| stun, medium | 1.48 | 3.04 | 3.43 | 3.43 | 3.43 |
| stun, fast | 1.47 | 3.04 | 3.43 | 3.43 | 3.43 |
| rolling, slow | 0.61 | 1.21 | 1.77 | 2.50 | 3.05 |
| rolling, medium | 0.60 | 1.19 | 1.73 | 2.45 | 3.00 |
| rolling, fast | 0.60 | 1.18 | 1.72 | 2.44 | 2.99 |

**A rolling ball into a long cushion** (velocities in the frames just before and after the bounce): the angle out from
the cushion's normal, and the normal speed out over the normal speed in (eN):

| in | slow: out, eN | medium: out, eN | fast: out, eN |
|---|---|---|---|
| 15° | 17.8°, 0.62 | 14.7°, 0.74 | 13.9°, 0.77 |
| 30° | 35.6°, 0.60 | 29.7°, 0.73 | (not read) |
| 45° | 53.4°, 0.56 | 45.3°, 0.72 | (not read) |
| 60° | 72.2°, 0.46 | 63.7°, 0.69 | 61.4°, 0.75 |

(At the fast speed the probe's frame-by-frame reading missed the bounce at 30° and 45°; those cells are not predicted.)

## Predictions (the engine's claims; each with its kill)

The reference's numbers come from re-implementing its law or model at the same cut, speed, spin and incidence, with its
own constants.

- **P1, stun throw at half-ball, slow.** The reference throws within 1° of the engine's 3.43°. *Killed* if it differs by
  1° or more.
- **P2, stun throw at half-ball, fast.** Within 1° of 3.43°. *Killed* if 1° or more apart.
- **P3, throw does not depend on speed.** The reference's half-ball stun throw changes by less than 1° from slow to fast.
  *Killed* if it changes by 1° or more. (Expected killed; see "What was known".)
- **P4, rolling throw at half-ball, medium.** Within 1° of 1.73°. *Killed* if 1° or more apart.
- **P5, the cushion at medium speed, 30° in.** The reference's angle out within 5° of 29.7° and its eN within 0.1 of
  0.73. *Killed* if either is outside.
- **P6, the cushion's restitution at every speed.** At 15° in, the reference's eN within 0.1 of the engine's at slow,
  medium and fast (0.62, 0.74, 0.77). *Killed* if any is 0.1 or more apart.
- **P7, the cloth.** The reference's sliding coefficient within 0.05 of 0.195, and its rolling coefficient within a
  factor of 2 of 0.0078. *Killed* if either is outside.
- **P8, the balls.** The reference's ball–ball restitution within 0.03 of 0.96. *Killed* if 0.03 or more apart.

## What would follow

A kill names a constant or a law the engine should change. Changing it is a new run with its own predictions, and the
challenges' reference shots are then played again (the smoke test does), since a change of physics can move a solution.

## Runs
