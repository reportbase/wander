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

**Run 1** (17 Nov; the static read of `play-trick.html`'s physics, lines 150–353, and `runs/eng/eng.mjs`, output
`runs/eng/eng-run1.txt`: 60 shots, 45 seeded over the rack, scatter, line, jump and massé layouts with random aim, power,
tip and the cue raised on the last two, and the 15 challenges' reference shots; 51,564 substeps, 140 contacts; every
Math trig and root call counted and attributed by its call stack).

- **E1 killed, in its letter.** No trig in `image`, `respond`, `pairs`, `inAir`, `imageInCushion`, `cloth`, `own` or
  `gripOf`. But trig is in two places my list or clause did not allow:
  - `firstStop`, which I listed as physics, is the aim alone: cos and sin of the aim angle, to find the ghost ball for the
    preview. No shot calls it (0 calls in run 1).
  - `simulate`'s contact log reports the first cut as an angle, `Math.asin(sinPhi)/D`, for the challenges' text. It is a
    record of the shot and decides nothing.
- **E2 killed, by my bound.** Trig calls attributed to the physics functions: 0. Every shot made 12 or 13 in all (10 in
  `strikeOf`: the aim, the tip and the cue's rise turned into a direction and a spin; 2 in `simulate`, the aim turned into
  the white's velocity; 1 in the log, the cut in degrees), against my 8. They do not grow with the shot: correlation with
  the shot's substeps −0.24.
- **E3 killed, in its letter.** The decisive contact test is a sum of shares: `ib.v + ia.v > 1` between balls,
  `im.v + im.v > 1` at a cushion, and the push runs along the unit vector of a difference of positions. But several tests
  are written with the denominator multiplied out, an amount against an amount, undivided:
  - between balls, a prefilter (r_a + r_b)² > d² before any root is taken;
  - a pocket, ex² + ez² < POCK² about its fixed centre, the comment's "v = POCK/d > 1, squared", with no share computed;
  - a cushion, the gap < r before the share is formed;
  - a ball in the air, d < r_a + r_b.
  Each is the share test times its denominator, so it is unmoved by scaling the world, but it is not stated as a share.
- **E4 killed.** The blueprint parts predicted are there: each ball's state in world coordinates (read back only as
  differences, or against the cushion planes and pocket centres), the shared tick (FRAME/SUB) and one integrator stepping
  every ball. Two more were found:
  - **the stop:** the shot ends when no ball anywhere moves (`moving()`), a decision over all balls at once (with a cap of
    2,700 frames);
  - **the order:** within a substep the pairs are resolved one after another in index order, each writing positions and
    velocities in place, so a ball in two contacts in one substep has its first write read by the second.
  (The frame snapshots and the contact log are records for drawing and sound, not physics.)
- **E5, measured.** The writes that enter decisions, not only updates:
  - sliding or rolling: |slip| ≤ 3.5·MU_S·h, an amount against the cloth's grip times the tick;
  - a landing bounce kept only if E_TABLE times the speed is over 1.5 units a second, an absolute speed;
  - flying over a cushion: the height against CUSH_H = 1.27 R; sunk only below 0.3 r (a share);
  - the push's size: (1 + e) and the mass ratio (h/v)³, a read standing for the masses only with one material assumed.
- **E6, measured.** 18.3 roots a substep: almost all `cloth`'s slip magnitude (937,098 of 942,428, one per moving ball per
  substep), then `inAir`, `respond`'s exact-contact root (378, about 2.7 a contact) and `image`. None is √(1 + s²); all are
  lengths of vectors in amounts, the cloth's friction direction among them.

## What the run shows (post hoc, not predicted)

- **Where two balls touch, which way they push, and the mass ratio are reads.** Every contact is decided on a sum of
  shares or the same test with its denominator multiplied out, and the push runs along the line of centres. No angle,
  no π and no trigonometry is in the physics.
- **Trigonometry enters only where a person aims.** The player gives an angle and a cue's rise, and the engine turns them
  into a direction once a shot, a fixed 12 calls whatever the shot does. The challenges' "cut in degrees" is a record.
- **How much, and when a ball stops sliding or bouncing, are writes.** Friction, restitution, gravity, the grip's fit and
  an absolute stopping speed are amounts carried in; they decide the sliding/rolling switch and the bounce, not contact.
- **The blueprint is in the integrator, and in two places I did not predict.** Positions are held in one world frame
  (scaffolding read back only as differences), one tick is shared, and the integrator also decides when the whole shot
  is over and in what order simultaneous contacts are written. Those two are a single standpoint's account only if
  something outside the balls holds all of them: the referee's part of the engine, not the balls'.
- **The multiplied-out tests are the share test written for cost.** They avoid a root and a division and decide exactly
  what the share decides. By R1062 the forms agree; what differs is what each needs: the share needs a division, the
  multiplied form needs both amounts in one unit.
- Classical in every part (impulse contact, Coulomb friction, a fixed-step integrator); the sorting is ours (R1062).

**Run 2 prediction** (committed before run 2; Tom: "run the varient and merge"). Run 1 found the engine's two referee
jobs: the stop (`moving()` over all balls) and the order (pairs written one after another in index order). Run 2 takes
them off it in a copy of the page served by the script (the page itself unchanged), and plays the same 60 shots:
- *own stop*: no look over all balls; the integrator runs the full cap (2,700 frames) and each ball's own state alone
  decides whether it does anything;
- *together*: within a substep every pair is resolved from the state at the substep's start, and each ball's changes
  from all its pairs are added at the end (Jacobi), so no pair sees another's write;
- *reversed*: the balls taken in reverse index order, with either rule.

- **V1.** With the own stop, every ball's final x, z and pocket are bitwise equal to the original on all 60 shots, and all
  15 challenges' reference shots still solve. *Killed* by any difference.
- **V2.** Together, on every shot in which no ball has two contacts in one substep, the final state is bitwise equal to
  the original. *Killed* by any difference on such a shot.
- **V3.** Together, at least 13 of the 15 reference shots still solve. *Killed* if fewer. Measured: how many shots have a
  substep with a ball in two contacts, and how far their outcomes move.
- **V4.** The original rule is order-dependent and the together rule is not: reversing the order moves some ball's final
  place by more than 10⁻⁶ on at least one shot under the original rule, and under the together rule leaves every ball's
  final place within 10⁻⁹ on at least 90% of the 60 shots. *Killed* otherwise.

**Run 2** (`runs/eng/eng2.mjs`, output `runs/eng/eng-run2.txt`; the page copied and changed in the script only: the stop
condition, a together rule wrapped round the original `pairs`, and the balls' order reversed on request).
- **V1 not killed.** With no look over all balls (the integrator runs the full 2,700 frames and each ball's own state
  alone decides what it does), every ball's final place and pocket is bitwise the original on all 60 shots, and all 15
  reference shots still solve. The stop was bookkeeping: it saves computing, and decides nothing in the game.
- **V2 killed.** On the 58 shots in which no ball has two contacts in one substep, together differs from the original on
  18. On 17 the difference is 5·10⁻¹⁷ to 1.2·10⁻¹⁴, my code: the together rule adds each pair's change back as
  (new − old), which is not bitwise the new value in floating point. On one, the throw challenge (a frozen pair), the
  white's final place moved 0.47: the original passes a push along the touching pair within one substep (white to 1, then
  1 to 2, in index order), the together rule a substep later, and my count of two contacts from the substep's start
  state does not see a contact that only begins inside the substep. The throw is still solved.
- **V3 not killed.** Together solves all 15 reference shots. Two shots had a ball in two contacts in one substep (a rack
  shot, 1 substep, and the break, 4); their outcomes moved 2.3 and 13.2 units, a different game, as a break is.
- **V4 not killed.** Reversing the order moves a final place by more than 10⁻⁶ under the original rule on 3 shots (the
  rack shot, the throw, the break); under the together rule every ball's final place is within 10⁻⁹ on 60 of 60 (zero
  on 58, 1.8·10⁻¹⁵ and 7.1·10⁻¹⁵ on two).

## What run 2 shows (post hoc)

- **The stop is not physics.** No ball needs to know the shot is over; each at rest does nothing, and the game is the
  same to the bit. Run 1's first unpredicted blueprint part is only the program's way of not computing an idle table.
- **The order is physics only where contacts chain within one tick.** Resolved together, every pair from the same start
  state, the game no longer depends on how the balls are numbered (60 of 60 within 10⁻⁹), solves every challenge, and is
  the original wherever contacts come one at a time. Where they chain (a rack, a frozen pair, the break) the original's
  index order decides how a push travels inside one tick, an artefact of a fixed step: neither rule is the true one, and
  the outcomes there part, chaotically on a break.
- **So the referee's two jobs come off it.** What stays the blueprint's is the world frame the state is kept in, the
  shared tick and the integrator. A finer tick, or contacts found in time order as the event-driven runs of MRB part 1
  did, would shrink the order's effect; the shared clock would remain.
