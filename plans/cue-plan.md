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

### Run 1 (11 October 2026)

The reference opened after the plan was pushed (commit 5a0de07): `pooltool/physics/resolve/ball_ball/friction.py`,
`ball_ball/frictional_inelastic`, `ball_cushion/han_2005/{model,properties}.py`, `objects/ball/params.py`,
`objects/table/specs.py` and `physics/resolve/resolver.py`, read as text. What they say:

- The ball–ball friction of pooltool's default resolver is the fit u_b = a + b·e^(−c·v_rel) "used in David Alciatore's
  TP A-14", a = 9.951×10⁻³, b = 0.108, c = 1.088, v_rel the balls' relative surface speed at contact in m/s. The
  collision model around it (frictional inelastic) is the one the engine already uses: the engine reproduces its own
  throws from the closed form to 0.02° (stun 10°: 1.48 both), so the throw predictions test the friction law alone.
- The constants, "taken from or based off of" Alciatore's physical-properties page: sliding 0.2, rolling 0.01, ball–ball
  restitution 0.95, cushion restitution 0.85, cushion friction 0.2, the cushion's nose at 0.64 of the ball's height.
- The cushion: pooltool's default is a compliant contact (Stronge's, with a frequency ratio of 1.8), not computed here.
  Han (2005), one of the two models the plan named, is computed, as pooltool states it (its eqs 14–23), with the
  constant e = 0.85 its properties.py returns (citing van Balen's thesis). After that `return`, properties.py also holds
  a speed-dependent restitution, max(0.40, 0.50 + 0.257·v_n − 0.044·v_n²), which never runs; it is reported below,
  marked as such. Mathavan et al. (2010), the plan's other named cushion model, is a numerical integration (780 lines)
  and was not computed in this run.

`plans/cue/reference.mjs` re-implements these and prints the verdicts; output in `plans/cue/cue-run1.txt`:

```
throw (degrees) at cuts 10 20 30 45 60, the reference beside the engine
  stun    slow   (0.44 m/s)  ref 1.48  3.05  4.84  4.95  4.63   engine 1.5  3.06  3.43  3.44  3.44
  stun    medium (1.33 m/s)  ref 1.48  3.05  3.56  2.79  2.33   engine 1.48  3.04  3.43  3.43  3.43
  stun    fast   (3.11 m/s)  ref 1.48  2.51  1.71  1.13  0.90   engine 1.47  3.04  3.43  3.43  3.43
  rolling slow   (0.44 m/s)  ref 0.76  1.50  2.19  3.10  3.79   engine 0.61  1.21  1.77  2.5  3.05
  rolling medium (1.33 m/s)  ref 0.35  0.69  1.01  1.43  1.75   engine 0.6  1.19  1.73  2.45  3
  rolling fast   (3.11 m/s)  ref 0.14  0.27  0.39  0.55  0.68   engine 0.6  1.18  1.72  2.44  2.99
  (the reference's friction at half-ball, stun: slow 0.0948, medium 0.0622, fast 0.0298; rolling: slow 0.0765, medium 0.0353, fast 0.0136)
cushion, a rolling ball, Han 2005 (e 0.85, mu 0.2): out angle and eN, the reference beside the engine
  slow   15°: ref 12.4° 0.801  engine 17.8° 0.618 | 30°: ref 26.8° 0.791  engine 35.6° 0.599 | 45°: ref 44.0° 0.775  engine 53.4° 0.556 | 60°: ref 62.1° 0.755  engine 72.2° 0.459
  medium 15°: ref 12.4° 0.801  engine 14.7° 0.740 | 30°: ref 26.8° 0.791  engine 29.7° 0.733 | 45°: ref 44.0° 0.775  engine 45.3° 0.719 | 60°: ref 62.1° 0.755  engine 63.7° 0.687
  fast   15°: ref 12.4° 0.801  engine 13.9° 0.774 | 30°: ref 26.8° 0.791  engine (not read) | 45°: ref 44.0° 0.775  engine (not read) | 60°: ref 62.1° 0.755  engine 61.4° 0.752
  (with the speed-dependent restitution left unused in properties.py, at 15°: slow e 0.602 eN 0.560, medium e 0.758 eN 0.711, fast e 0.875 eN 0.825)

P1: KILLED. stun half-ball slow: reference 4.84° against the engine's 3.43° (within 1°)
P2: KILLED. stun half-ball fast: reference 1.71° against 3.43° (within 1°)
P3: KILLED. the reference's stun half-ball throw changes 3.13° from slow to fast (less than 1°)
P4: not killed. rolling half-ball medium: reference 1.01° against 1.73° (within 1°)
P5: not killed. cushion, medium, 30° in: reference out 26.8° (engine 29.7°, within 5°), eN 0.791 (engine 0.733, within 0.1)
P6: KILLED. cushion eN at 15°: v7 reference 0.801 engine 0.618, v21 reference 0.801 engine 0.74, v49 reference 0.801 engine 0.774 (each within 0.1)
P7: not killed. cloth: sliding 0.2 against 0.195 (within 0.05), rolling 0.01 against 0.0078 (within a factor of 2)
P8: not killed. ball–ball restitution 0.95 against 0.96 (within 0.03)
```

## Reading of run 1 (not ruled)

- **The grip between balls is the engine's largest departure from the published game.** The fitted grip falls threefold
  from a slow to a fast meeting (0.095 to 0.030 at a half-ball stun), and the engine's is one number, 0.06, right only
  near a medium hit. So a slow cut throws the struck ball about 1.4° more than the engine says, and a fast or thin one
  about 2° less; for rolling hits the engine is too much at medium and fast speeds (1.7° against 1.0° and 0.4° at
  half-ball). Over a table's length 2° is most of a pocket. P1–P3 name the change: the engine's MU_B as the fit's
  μ(v_rel). That is a new run with its own predictions (run 2), and the challenges' reference shots must be played
  again with it.
- **The cushion agrees at medium speed and parts at slow speed.** At medium and fast speeds the engine's rebound is
  within a few degrees and a few hundredths of Han's with e = 0.85 (P5). At a slow speed the engine's bounce is weaker
  (eN 0.46–0.62 against 0.76–0.80) and leaves wider (17.8° against 12.4° at 15° in). Noticed after the run, and so not
  a result: the engine's slow-to-fast rise (0.62, 0.74, 0.77 at 15°) is close to the speed-dependent restitution that
  pooltool keeps but does not use (0.56, 0.71, 0.83). Which is right for a real cushion is a question for measured data
  (Han's paper, Mathavan's), not for either implementation; the cushion is left as it is until those can be read.
- **The cloth and the balls' own constants agree** (P7, P8), within the plan's margins.
- **What this run can and cannot say.** It tests the engine against laws as a careful open-source simulator states
  them, with their sources named. Two steps remain between that and the game as measured: the fits' own agreement with
  their data, and which of several published models a real table follows. Both need the papers' tables.

### Run 2 (11 October 2026): prediction, written before it ran

**The change.** The engine's grip between balls, the constant MU_B = 0.06, becomes the fit run 1 read:
μ = 9.951×10⁻³ + 0.108·e^(−1.088·v_rel), v_rel the contact points' relative sliding speed in m/s, which the engine
already computes in its own units (the slide (s, sv) it grips against) and converts at 0.0635 m/s per unit. Nothing
else changes; `spinChecks` still turns the grip off for the textbook results.

**Worked out before the run** (the closed form, as run 1's reference computes it, at the engine's restitution 0.96): a
stun half-ball cut at the smoke test's speed (10 units/s, 0.64 m/s) meets the fit's grip 0.087, above the cap 0.084
that stops the sliding, so it throws atan(0.084) = 4.8°, past the smoke test's bound of 4.5° (set when the grip was
0.06). A full stun hit with the smoke test's right English (wy = 12) slides at 0.34 m/s, grip 0.084, where the cap
binds again: about 4.5°, on the smoke test's bound.

- **P9, the engine is the fit.** Its throws, read as in run 1 (`plans/cue/engine.mjs`), match the reference's closed
  form within 0.15° at all 30 points (stun and rolling, three speeds, five cuts). *Killed* if any differs by 0.15° or
  more.
- **P10, the smoke test's throw bounds were the old constant's.** The cut throw at the smoke test's shot is 4.8 ± 0.2°
  and the side-spin throw −4.5 ± 0.2°. *Killed* if either is outside. (If not killed, the smoke test's bounds move to
  the fit's values with a margin, and say why.)
- **P11, the textbook results are untouched.** `spinChecks`' results 2–4 (follow, stun, draw), which run with the grip
  off, are the same to the last digit. *Killed* if any differs.
- **P12, the challenges.** Every challenge is still missed as set up and solved by its reference shot. *Killed* if any
  reference shot no longer solves it. (Uncertain: a degree of throw moves a pot over a few table lengths. If killed, the
  challenge's reference shot is searched again on the new engine, as it was first found, and its par recomputed.)

The change, in `play-trick.html`: `gripOf(slide)`, the fit at the slide's speed converted to m/s, in place of MU_B, at
the one line where the grip is applied; `spinChecks` sets the grip to 0 and back as before. The engine's side read again
by `plans/cue/engine.mjs` (`cue-engine-run2.txt`); the textbook results and the challenges, before and after, by
`plans/cue/checks.mjs` (`cue-checks-before.txt`, `cue-checks-after.txt`); the verdicts by `plans/cue/run2.mjs`
(`cue-run2.txt`):

```
throw stun v7      1.5  3.06  4.84  4.99  4.67
throw stun v21     1.48  3.04  3.57  2.8  2.34
throw stun v49     1.47  2.52  1.71  1.14  0.9
throw rolling v7   0.79  1.55  2.27  3.21  3.92
throw rolling v21  0.35  0.69  1.02  1.44  1.76
throw rolling v49  0.14  0.27  0.39  0.55  0.68
(the cushion unchanged, as run 1)

also: spin passed on -2.06 -> -2.66, backspin passed 3.18 -> 3.45, follow with the grip 0.2579 -> 0.2543

P9: not killed. the engine's 30 throws against the reference's closed form: largest gap 0.128° (rolling v7 cut 60°: engine 3.92, reference 3.79) (under 0.15°)
P10: KILLED. the smoke test's cut throw 3.51° (predicted 4.8 ± 0.2; before the change 2.53), side-spin throw -3.39° (predicted −4.5 ± 0.2; before -2.62)
P11: not killed. textbook results with the grip off: follow 0.2998460749102105 (before 0.2998460749102105), stun 0.02301369047619067 (0.02301369047619067), draw 0.23631398809522597 (0.23631398809522597)
P12: not killed. 13 of 13 challenges missed as set up and solved by their reference shot
```

## Reading of run 2 (not ruled)

- **The engine's throw is now the published fit's,** to 0.13° at the worst of 30 points and 0.04° at every stun. The
  gap that remains is largest for slow rolling hits at thin cuts and grows with the cut, which the closed form's
  restitution (0.95 against the engine's 0.96) does not explain, since there the grip is not capped; it is left as
  found.
- **P10 was killed by my set-up, not by the engine.** The prediction took the smoke test's throws as pure stuns. They
  are not: its white travels half a unit first and has begun to roll, so its throws lie between the stun's and the
  rolling ball's (3.51° and 3.39°, against 2.53° and 2.62° before). Both are inside the smoke test's bounds, which
  therefore stay as they are. The rule in the plan ("if not killed, the bounds move") did not come into play.
- **The textbook results and the challenges are untouched** (P11, P12). A throw that moved by a degree did not move any
  challenge's pot: their reference shots are full or near-full hits, or hits where the window of aim is wider than the
  change.
- **What is left from run 1:** the cushion at slow speed (P6), for measured data to decide between a constant
  restitution and a speed-dependent one.
