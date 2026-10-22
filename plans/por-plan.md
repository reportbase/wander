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
