# POR: pool revisited, in the light of address and payload, reading and writing, K and H

*Plan, predictions and kills written 22 October 2026, before any script in `runs/por/` existed (Claude, a sub-agent asked
to revisit POL, `plans/pol-plan.md`, against what OFS has since settled). Exact arithmetic, and the POL engine itself
(`pool.html`'s script, loaded read-only into node by `runs/por/loadpool.mjs`). Evidence about the geometry and about
computation, not about the world. The lab rules hold: nothing above "## Runs" is edited after the run.*

## Known beforehand

From OFS (the passages read): an arrival is an address (a direction laid by a uniform turn) times a payload (what comes
along it) (§7.2); one turn has two sweeps, the inscribed (from a point of the circle, s = v/h, unbounded, median) and the
central (from the centre, amounts along given directions, means) (§4, "Why there are two sweeps, and only two"); the chord
h + v = 1 needs only the two parties and their sum, no standpoint and no turn (§2, R234, R236); a reading is unchanged
when every length is scaled by k, a writing moves by k (§9, "The test: scale the world"); a corner is a median only for a
reciprocal-symmetric law (Theorem 6(e)), otherwise a stationary point (f(k) = f(1/k) gives f′(1) = 0; MOT P12), a
hand-over, or a swap's fixed point; K, the reader's count of addresses, comes before H, and H is only a zoom (§8, "A
fixed count, aimed by H").

From POL (runs 1–18, recorded in `plans/pol-plan.md`, numbers seen): contact h + v = 1 with v = r_b/d (a's reading of b,
the sine of b's half-span) and h = r_a/d (b's reading of a, told to a); the pair's ray v/h = r_b/r_a; a cushion is the
ball and its mirror image, always h = v; the carrying reader's error is small below one tick of lateness and on a plateau
of about 1.5e-2 above two (run 4); ignoring balls K levels smaller (run 6); the kick read from readings (run 10); a world
held by distance lost a pulse (run 18: 22% of the peak, inside the noise).

Worked out by hand before writing the predictions (identities; the script checks the arithmetic, they are not tests):
- **Contact is the sum cut, joined from two standpoints.** Each of h and v is one party's reading of the other's angular
  size (a reading: r/d is unchanged by k). Neither is the inscribed reading s = v/h: that is the pair's ray, fixed by the
  two sizes for the whole game, so it carries no news after the rack. Contact, h + v = 1, is the ℓ₁ cut of the pair's two
  readings, which no single standpoint holds (POL P3: one reading decides only when the sizes are equal). The game played
  from inside is the referee's because the exchange (each told the other's reading) supplies the second standpoint.
- **The three corners sort three ways.** With masses ρ³ (ρ = v/h, one material) and restitution e:
  - the share of the closing speed the reader takes, q(ρ) = (1 + e)·ρ³/(1 + ρ³), has q(ρ) + q(1/ρ) = 1 + e and
    dq/d ln ρ = 3(1 + e)/4 at ρ = 1: at the contact corner the momentum share is a **hand-over** (a swap's half-point,
    not stationary);
  - the energy passed to a resting ball, T(ρ) = (1 + e)²·ρ³/(1 + ρ³)², has T(ρ) = T(1/ρ): **stationary** (its most,
    (1 + e)²/4) at the same corner;
  - the cushion is a pair whose ray is ρ ≡ 1 by construction (the reader and its flip): a **swap's fixed point**, the
    corner occupied identically, with nothing to vary;
  - the time corner (lateness against the tick) is a **hand-over of amounts**: both are seconds, so it is not a corner
    of readings at all (P2 tests that it moves when the world is scaled).
  None is a median: POL measured no law over a uniform turn.
- **At contact, a size difference is an angular size.** On h + v = 1 with v/h = ρ, the smaller ball's reading is
  v = ρ/(1 + ρ): ⅓, ⅕, ⅑ for one, two, three levels smaller. So at the moment a response is decided, "K levels smaller"
  is "fills less than so much of my view": a threshold on one reading, the count of addresses it occupies (K_addr·arcsin
  v/π of a full turn of K_addr), halving per level. That is K's spending by size on screen. The reader's own radius (its
  H) enters nowhere.
- **Folding a payload into the address grid imposes the grid's law.** Cells held "at the corner of (breadth, distance)",
  a fixed count m to each doubling, have a breadth ∝ distance in each of the D dimensions. A payload of fixed size σ
  folded into such a cell at distance D₀ keeps its total and loses its peak by (σ/cell)^D ∝ D₀^(−D): a falloff with
  distance that is the address count's, not the payload's. The max principle (an average never exceeds what it
  averages) makes it irreversible: no later refinement of the cells brings the peak back.

## The reading to test

POL's results re-sort into readings (contact, the cushion, ignoring by size, aim lost per level: scale-free, the
address side) and the places where an amount was carried in (the clock and the signal's speed in the time corner; the
one material in the mass share; the totals of the infinite table, which are payload). "A signal must be held at its own
size until it arrives" is the address/payload split: the address grid may be laid in advance and coarsened by distance,
because an address is not a payload; the payload may not, because folding it is a mean, and a mean of the payload taken
at the address grid's grain writes the grid's 1/D^D into what arrives.

## Predictions

Not computed before writing: any run of the engine scaled, any rule decision of P3, any number of P4–P5.

- **P1 (the table from inside is a reading; the referee's record a writing).** In POL's engine with every length (table,
  radii, pockets, gaps) and every speed (the strike, the cloth's deceleration) multiplied by k and the clock unchanged,
  over the ten heavy-ball breaks (8 s, run 1's measure) and run 6's five fields (1 s): every logged pair of readings
  (v, h) and every contact decision equals k = 1's, and the referee's positions are k times k = 1's.
  - at k = 2: exactly (bitwise; scaling by a power of two is exact in floating point);
  - at k = 7 and k = 10⁻³: readings within 1e-9 absolute, contact counts equal, referee positions over k within 1e-9 of
    the table's length.
  *Killed* if any of these fails.
- **P2 (the time corner is a corner of amounts: it moves under k).** In run 3–4's carrying reader (breaks 0, 4, 9, SUB
  4), scaling the world by k with the signal speed c unchanged is the same game as k = 1 at speed c/k:
  E(k, c)/k = E(1, c/k) for k = 2 and ½, to 1e-12 relative, at c = 100, 200, 400. Consequently at c = 200 the median E/k
  is below 1e-3 at k = 1 (lateness 1.08 ticks) and above 1e-2 at k = 2 (2.16 ticks): the same table, scaled, crosses
  the corner. *Killed* if any equality misses or the k = 2 median is not on the plateau. (Contact and the cushion, by P1,
  do not move.)
- **P3 (ignoring by size is spending K by size on screen).** In run 6's five fields (1 s, rules applied only to responses
  that push, as run 10's rule hook does), the size rule "ignore a ball K or more levels smaller" and the address rule
  "ignore any ball whose own reading v is at most v*_K", v*_K the geometric mean of the contact readings for 2^−K and
  2^−(K−1) (√(1/6), √(1/15), √(1/45) for K = 1, 2, 3), make the same decision at every response for K = 1, 2, 3, so the
  same game (level-0 errors bitwise equal). *Killed* by any differing decision. *Measured:* the largest reading at a
  response over its contact value ρ/(1 + ρ), in levels (how far a tick's overlap moves v).
- **P4 (in one dimension, a payload folded by distance falls as 1/D₀).** A Gaussian pulse of width σ = 1/8 starting at
  D₀ moves rigidly toward the reader at x = 0 (no falloff of its own). Address cells: m = 12 to [0, H] and to each
  [H·2^(j−1), H·2^j], H = 1. Read at arrival: the largest average over the reader's first cell [0, 1/12], over the truth's.
  - (a) folded once at birth (cell totals, uniform within a cell), then carried exactly: the slope of log₂ of the arrival
    over log₂ D₀, for D₀ = 2^p·(1 + U/8), p = 6 … 12, 32 seeded U a p, is in [−1.03, −0.97]; and its median over the U is
    within 3% of √(2π)σ·m/2^(p−1), the payload's total over the birth cell's breadth.
  - (b) held by distance throughout (moved exactly, re-totalled onto the cells every step): at every sample no higher than
    (a), and its slope in [−1.3, −0.7].
  - (c) refined when the time to arrival falls below τ* (cells finer than σ inside x < c·τ*): with τ* = D₀/(2c), no higher
    than (a) at any sample (the max principle; this checks the code); with τ* past D₀/c + 6σ, the truth to 1e-9.
  - (d) folded at birth but with the kind carried in (a Gaussian of known σ: the totals' sum and centroid give its height
    and place): the truth to 1e-9.
  *Killed* if any clause fails. (b) and (c) run for p = 6 … 9 only (time).
- **P5 (in two dimensions, as 1/D₀²).** A Gaussian blob of width σ = 1/8 at distance D₀ in polar address cells (radially
  as P4, 96 equal angles round the turn): folded at birth, the largest cell average over the blob's height has slope in
  [−2.06, −1.94] against D₀ for p = 6 … 12 (16 seeded places a p, distance and angle). *Killed* if not.

## Runs

### Run 1 (22 October 2026)

`node runs/por/por1.mjs` (P1–P3, 1.6 min), `python3 runs/por/por1.py` (identities, P4–P5, 19 s), then, after the run,
`node runs/por/por1-posthoc.mjs`; their three outputs are gathered in `runs/por/por-run1.txt`. The engine is
`pool.html`'s own script, read and run in node by `runs/por/loadpool.mjs`; it reproduces POL (run 6's field errors
2.32, 0.217, 0.109 …; run 4's cells 8.08e-5, 1.53e-2, 2.34e-2).

- **The identities** (arithmetic, as worked by hand): q(ρ) + q(1/ρ) = 1 + e to 10⁻⁴⁰ and dq/d ln ρ = 3(1 + e)/4 at the
  corner (1.47 at e = 0.96): the momentum share hands over there. T(ρ) = T(1/ρ), dT/d ln ρ = 0, d²T/d(ln ρ)² =
  −(9/8)(1 + e)² (−4.32): the energy passed is stationary, its most (1 + e)²/4 = 0.9604.
- **P1 killed, by my set-up (the field's tolerance).** At k = 2 every one of 2,181,420 rack and 7,946,156 field reading
  pairs, every contact (188, 265) and every referee position over k is bitwise k = 1's. At k = 7 and 10⁻³ the rack's
  readings agree to 2.9e-13 and 1.3e-12 and the referee's positions over k to 4e-12, with every count equal; but the
  field's readings part by 4.7e-6 and 6.2e-7, past my 1e-9. Post hoc: field 1 stays within 1e-11 all second; the parting
  is the field's chaos (run 6's horizon of about 2 s, faster in field 2) growing the different rounding of a non-binary k,
  not a reading that moved. The bitwise k = 2 result is the test; the 1e-9 clause for the field was set without run 6's
  growth in view.
- **P2 not killed.** E(k, c)/k equals E(1, c/k) with relative difference 0 (bitwise) in all six cells (k = 2 at c = 100,
  200, 400; k = ½ likewise). At c = 200 the median E/k is 8.08e-5 at k = 1 (1.08 ticks) and 1.53e-2 at k = 2 (2.16
  ticks): the same table, scaled, crosses the time corner, while P1 shows that contact and the cushion do not move.
- **P3 killed.** At K = 3 the one-reading rule and the size rule decide alike at all 576 responses and play the same game
  bitwise. At K = 2, 4 of 612 decisions differ, at K = 1, 55 of 684; the level-0 errors stay bitwise equal (the
  differences are among smaller balls), but the skip counts differ (K = 1: 26, 69, 43, 56, 56 against 20, 61, 38, 46,
  35). *Measured:* at a pushing response log₂(h + v) is 0.125 levels at the median, 0.51 at the 90th percentile and up to
  1.88: the tick lets pairs overlap, and responses repeat while they do. Post hoc: every differing decision is one where
  the size rule skips and the one reading keeps, at log₂(h + v) ≥ 0.29 (median 0.50), a smaller ball overlapping so far
  that it fills more of the view than its contact value by half a level. The ratio v/h, read from two readings, is the
  pair's ray and does not move with the overlap; one reading does. So ignoring by size is K's spending at contact only
  where contact is found exactly (as run 9 makes it); with a tick, the rule that reads the ray is the robust one.
- **P4 (a) killed, by my arithmetic; the slope stands.** The slope is −0.990 (band [−1.03, −0.97]). The medians are
  0.509 of the value I wrote: D₀ = 2^p(1 + U/8) lies in [2^p, 2^(p+1)], whose cells are 2^p/m, not 2^(p−1)/m. Against the
  cell it lies in, the medians are 1.0186 of √(2π)σ·m/2^p at every p, the 1.86% being the truth's own window average
  (0.982). (b) not killed: never above (a), slope −0.996 (a further loss of 3.7–4.1 times from re-totalling every step).
  (c) not killed: refined from D₀/2, 1.14–1.17 times (b) and never above (a); refined from birth, the truth to 1e-14.
  (d) not killed: the totals' sum and centroid with the kind (σ) carried in give back the truth to 2e-16.
- **P5 not killed.** Slope −1.988 (band [−2.06, −1.94]); the median falls about 4 a doubling (3.9e-3 at p = 6 to 9.9e-7
  at p = 12).

## Reading of run 1 (not ruled)

- **Contact is the sum cut, not a sweep.** Neither h nor v is the inscribed reading; the pair's ray v/h is fixed by the
  sizes for the whole game. Contact is the ℓ₁ cut h + v = 1 of two standpoints' readings, joined by the exchange. Every
  reading in the game is unchanged by k, bitwise at k = 2 (P1): the table from inside is a reading throughout. The
  referee's record moves by k: it is a writing, and plays the same game only because its rules are scale-covariant.
- **The corners sort.** Contact: the momentum share hands over (a swap's half-point), the energy passed is stationary;
  the cushion: a swap's fixed point by construction (ρ ≡ 1); time: a corner of two amounts, which moves when the world
  is scaled (P2). None is a median.
- **Ignoring by size is spending K by size on screen,** exactly where contact is exact. Under a tick it is the ray v/h,
  not one angular size, that keeps the decision (P3). H, the ball's own radius, enters neither.
- **"Level reads momentum" is the address carrying the payload through a bridge.** The level (v/h, or v at contact) is a
  reading; the momentum is a payload (mass, through the one material, a known kind, times the closing speed, through the
  clock). It held in POL's field because the kind's step (8 a level) outran the payload's spread (1.2–1.6); with mixed
  materials the bridge goes and the level would read nothing of the momentum (untested).
- **"Held at its own size until it arrives" is the address/payload split.** The address grid (m cells a doubling) may be
  laid in advance and coarsened by distance; folding the payload into it is a mean, irreversible (P4 (b), (c)), and
  writes the grid's own law into what arrives: 1/D₀ in one dimension, 1/D₀² in two (P4 (a), P5), a falloff with no
  physics in it. POL run 18's 22% is of that kind: a 20-unit disc folded into a 60-unit cell. Refining by time to arrival
  rescues nothing once folded; only holding from birth (the payload's own grain) or carrying in the kind (P4 (d)) does.
  So the fix for run 18 is a statement about the payload, not about the reader's levels.
