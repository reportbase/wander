# ENG: the pool engine audited by read, write and blueprint

17 November 2026. SPN R1080. Tom: "i'm wondering if this helps our read/write thesis", then "yes", to an audit of the
trick-shot engine (wander's `play-trick.html`, moved whole into reportbase/games' `TRICK_APP`).

## The question

The engine plays pool from inside, each ball reading the others and writing its own state, and matches a referee to
rounding (POL). That is a demonstration, not evidence: it gives the same numbers as a positions-first simulation by
construction (R950). What it can show is which mathematics each part needs, R1062's table: reads (slopes, sums of
shares, comparisons against 1, no angle, no π), writes (amounts in a unit: masses, speeds, the cloth, the grip, counts),
and the blueprint (positions held whole in one frame, a shared clock, an integrator, trigonometry and π). If the physics
needs the blueprint only where we expect, the game is a counted case of the corpus's claim; if it needs it elsewhere,
that is worth knowing.

## What is audited

The engine's physics functions in `play-trick.html` (names from the file, bodies not read before this plan):
`image`, `respond`, `pairs`, `inAir`, `imageInCushion`, `cloth`, `own`, `firstStop`, `gripOf`, `simulate`. Aim and strike:
`strikeOf`, `aimAt`. Everything else (layouts, drawing, sound, controls) is outside the physics.

## Predictions (committed before reading the function bodies or running anything)

- **E1 (static, trig).** No call to Math.sin, cos, tan, asin, acos, atan, atan2 and no Math.PI or the degree constant D
  inside `image`, `respond`, `pairs`, `inAir`, `imageInCushion`, `cloth`, `own`, `firstStop`, `gripOf`. In `simulate`, trig
  appears at most where the aim angle is turned into a direction, before the first step. *Killed* by any trig call
  elsewhere in those functions.
- **E2 (dynamic, trig).** Over 60 seeded shots (the layouts rack, scatter, line, jump, masse and every challenge's
  reference shot, with spin and the cue raised), trig calls made during `simulate` and attributed by the call stack to
  the physics functions of E1 are 0, and the trig calls a shot makes in all are at most 8 and do not grow with the shot's
  number of steps. *Killed* by any physics-attributed trig call, or a shot with more than 8.
- **E3 (decisions are reads).** Every physics decision (balls in contact, a ball on a cushion, a ball taken by a pocket,
  the direction of a push) is made on a share or a direction: a reading v = r/d or its cushion form, compared against
  1 (or the pair's sum h + v against 1), or a unit vector from a difference of positions. *Killed* by a decision made on
  an absolute coordinate other than a fixed table plane or pocket centre, or on an amount compared against an amount
  without dividing them.
- **E4 (the blueprint the physics needs).** The blueprint parts are exactly these: each ball's state stored as world
  coordinates (positions read back only as differences or against the table's fixed planes), the table's planes and
  pockets in world coordinates, the shared tick (FRAME, SUB) and the integrator stepping every ball together. *Killed*
  by another blueprint part the physics needs (another use of a world frame, a total over all balls used in a
  decision).
- **E5 (writes).** The amounts carried in are the constants (R, MU, MU_S, MU_SP, MU_C, MU_TIP, E_BALL, E_RAIL, G, E_TABLE,
  the grip's fit, M_PER_UNIT) and each ball's r and m, speeds and spins. Measured, not a kill: which of them enter a
  decision (E3) and which only an amount's update.
- **E6 (roots, measured).** Math.sqrt and Math.hypot calls per substep, attributed by function: the one square root R793
  allows, reported.

## What this does not test

That the engine is right about pool (CUE did, against pooltool); that nature works this way (R261); that the single
standpoint beats the classical form (R950: they agree). The scale test is POR's (R439), not repeated.

## Runs
