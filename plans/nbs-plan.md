# NBS: a bridge behind the 9-ball computer's aim

26 November 2026. Tom: "Many games use the pool engine", then "2, write the plan" (to: test the bridge against the
computer's current aim search in 9-ball, first, here). PEB runs 4–5 found that a shot's outcome across the aim is
pieces, cut at the table's events, most held by about 6 leaves of the Tangent Bridge. This asks whether that is any use
to a player: the computer in reportbase/games' 9-ball. Predictions are written below before any script exists. Nothing in
`games.html` is changed; the test reads it.

## What the computer does now

`games.html` (games at `de6a98d`), `ninePlanGen(g, lv)`, the engine above "IN THE FIELD" (wander's `play-trick.html`
at 335fa6c, a fixed tick). For the lowest ball it takes the four nearest pockets; at each, the ghost-ball aim only
(skipped past a cut of about 75°); at that aim a few powers (two below level 3, four from 3) and from level 4 three tips;
each flown ahead in the engine (`simulate`) and scored (the 9 potted 10, the lowest potted 2 plus, from level 3, the leave
for the next ball, `leaveQ`; no pot a legal hit, from level 4 the one that leaves least). At most about 48 flights. Then
the hand's error, a Gaussian in the aim of `NINE_ERR` (3.2°, 1.8°, 0.8°, 0.4°, 0.15° at levels 1–5). It never looks
away from the ghost-ball line: no bank, kick or combination, and it does not know how wide its window is.

## What the bridge would add

Lay the outcome across the whole circle of aims (one power at a time): find where the shot's events change (the full
signature, PEB run 5: contacts with the grips' choices, cushions, pockets, phase ends, side spin's end), bisected to
10⁻¹⁰ rad. Each piece has one sequence of events, so whether it is a legal pot of the lowest ball (or of the 9) is read
once per piece, and the piece's width is the window. Within a pot piece the leave (the white's rest place and so
`leaveQ`) is held by the bridge on K leaves (PEB's Chebyshev points, in the root's chart at an end of a root's kind), so
the best place in the window to aim is read from K flights, not hundreds.

The planner tested, **B**: at powers 16 and 28 (no tip, no elevation), map the circle; keep the pieces that pot legally;
for each, weigh the window against the level's hand error (the share of a Gaussian of σ = `NINE_ERR` falling inside it,
aimed at the point that maximizes that share times the bridged leave score, `leaveQ` as level 3 uses it); choose the best.

The engine is the games' own fixed-tick engine, untouched (the bridge is laid on what it does). PEB run 1 found that
engine's pieces carry the tick's hidden jumps; for a pot/no-pot verdict that does not matter (the signature is unchanged
by them), for the leave it adds error the bridge cannot hold, which A4 measures.

## Positions

Sixty positions from seeded self-play: `rack9(idx)` for idx 0, 1, 2, …, both sides played by `ninePlan` at level 3, the
table recorded before each shot; the break (each rack's first shot) and shots with the white in hand left out; the
first 60 kept. Seed and idx list recorded in the run. Only the computer's planner and B are compared, both on the same
positions; both judged by the same referee: the engine's own flight of the shot.

## Predictions (written before any script exists)

- **A1 (more pots found).** B finds a legal pot (lowest or 9, white up, lowest met first) in every position where C (the
  current planner, level 5) does, and in at least 10% of the positions where C finds none (banks, kicks, combinations,
  aims off the ghost-ball line).
- **A2 (pots made under the hand's error).** With each planner's chosen shot flown 200 times under the hand's error, the
  share of legal pots, averaged over the 60 positions: at level 3 (σ 0.8°) B at least 5 points above C; at level 5
  (σ 0.15°) B not below C by more than 2 points.
- **A3 (the cost, stated).** B's flights per position (the map at two powers on 720 aims, the bisections, the leaves)
  median at most 4,000, which is at least 30 times C's. The bridge does not make the computer cheaper than the
  ghost-ball line; what it buys is the whole circle.
- **A4 (the leave held).** In legal-pot pieces wider than 10⁻³ rad, the white's rest place held to 0.05 table units
  (a ninth of a ball's radius) by the bridge with K ≤ 12 in at least 80% of pieces, on this tick engine.
- **A5 (the bridge chooses as flights would).** Within each chosen window, the aim B picks from the bridged leave score is
  within 0.1 of the best `leaveQ` found by flying 64 evenly spaced aims across the window, in at least 80% of positions.
- **A6 (the engine untouched).** The sha256 of `games.html`'s text above "IN THE FIELD" is the same before and after the
  run, and the referee's flights are its `simulate`.

Each is killed by its own number. Known beforehand: PEB runs 1–5 (the pieces, the tick's jumps, the full signature, about
6 leaves a piece), the planner's code read above, and the classical facts that a wider window forgives more aim error and
that banks and kicks exist where a ghost-ball search does not look. So A1's direction is expected; its 10% and A2's 5
points are the guesses. A2 could fail because a ghost-ball pot is already the widest window in most positions, or because
wide windows found by B leave the white badly.

What would follow if A1, A2 and A4 are not killed (a reading, to rule on): the shot map, cut at the table's events and held
by the bridge between them, is a usable plan for a player, finding pots a line search misses and aiming where the hand's
error is forgiven; its price is flights, not cleverness. Only then would carrying it into `games.html` (the computer's
turn, the engine untouched, step 3 of the proposal) be put to Tom.

## K is n, N is not (added 26 Nov, before any script; SPN R1263)

Tom: "This might seem like a lot extra work, but tb allows us to make real the idea that k is n. N is not n." Read here
as: the count a procedure runs over (its n) should be K, the leaves laid on what the table does, never N, the aims a
search could fly. A1–A6 as written do not test that: B finds its pieces on a fixed scan of 720 aims, so its cost still
grows with how finely the circle is scanned, and PEB run 5 found pieces the 1,024-aim scan stepped over. So a third
planner and one more prediction, written now:

**B′**: B with no fixed scan. Start from 16 even aims; a span is one piece when the full signature is the same at its K
Chebyshev leaves and the bridge's last two coefficients are under the tolerance (10⁻⁶ of the leave, PEB's), otherwise it
is halved, a change of signature bisected to 10⁻¹⁰ rad as before. Its flights are Σ over pieces (K + the bisections),
counted by the table's events alone.

- **A7 (K is n).** On the same 60 positions: (a) B′ keeps every legal-pot piece wider than 10⁻³ rad that B keeps, in at
  least 95% of positions; (b) with B's scan doubled to 1,440 aims, B's median flights rise by at least 1.6 times, B′'s
  (which has no scan) by none, its count identical; (c) B′'s median flights per position, divided by its median number of
  pieces, at most 3 × its median K (the leaves, not a scan, are what it pays for). Killed by any clause. (b)'s second half
  is true by construction and is stated only so the comparison is on the page; (a) and (c) can fail.

## How it will be run

`runs/nbs/nbs.mjs`, headless Chromium (playwright from /opt/node22/lib/node_modules), loading `games.html` from a local
clone given by `GAMES_HTML` (default `../games/games.html`), driving the 9-ball app's debug hooks (`rack9`, `ninePlanGen`,
and the trick app's `simulate`, `strikeOf`) and, where a hook is missing, a copy of the page served with one line exposing
it (the engine text not touched; A6 checks). Parts run in parallel on four cores; outputs `runs/nbs/nbs-*.json` and a report
`runs/nbs/nbs-run1.txt`.

## Runs

### Run 1 (26 Nov 2026; Tom: "Merge and run")

`node runs/nbs/nbs.mjs run`, then `report` (`runs/nbs/nbs-run1.txt`; one JSON a position, `runs/nbs/nbs-pos-*.json`;
the log `runs/nbs/run1.log`). games at `de6a98d`, the text above "IN THE FIELD" sha256 `8a5e806c…b97061e505471c0fd99d52ec8c1bc938e703b2e6497b24aca`
before and after. Sixty positions from racks 0–3 (15, 20, 17 and 8 shots), self-play seed 20261126; about 5.5 hours of
flights on four browsers. Choices I made in writing the runner, stated here because the plan did not fix them: the
fixed-tick engine records no grips' choices or phase ends, so the signature is the contacts, cushions and pockets in time
order; B bridges each pot piece on 8 leaves (counted in its flights) and picks the best of 64 aims in each piece by the
Gaussian share of that piece times the bridged score; B′ uses K = 8, its leave the white's place, tolerance 10⁻⁶ table
units, and a cap of 50,000 flights a power (after a trial of three positions in which a cap of 200,000 was hit at every
one); a planner with no pot in hand still flies its best shot under the hand's error.

| | | |
| --- | --- | --- |
| A1 | B finds a pot in all 35 positions where C does, and in 20 of the 25 where C finds none (80%) | not killed |
| A2 | legal pots under the hand's error, mean over positions: level 3 B 61.0%, C 32.8%; level 5 B 85.8%, C 47.2% | not killed |
| A3 | B's flights per position median 48,018 (6,896–105,419), C's 12: 4,001 times | **killed** (my guess of 4,000 at most) |
| A4 | 1,317 pot pieces wider than 10⁻³ rad; the white's rest place held to 0.05 by some K ≤ 12 in 1,085 (82.4%); median error 0.017, 0.015, 0.014 at K 6, 8, 12 | not killed (narrowly) |
| A5 | in 26 positions with a level-5 window potting the lowest ball, B's aim within 0.1 of the best of 64 flown aims in 24 (92.3%) | not killed |
| A6 | the engine text unchanged; the referee games' `simulate` | not killed |
| A7 | (a) B′ covers all of B's wide pot pieces in 5 of 60 positions; (b) the doubled scan costs B 1.13 times, not 1.6; (c) B′ hit its cap in every position at both powers, holding a median of no pot piece | **killed** in (a) and (b); (c) meaningless under the cap |

Post hoc, not predicted. Split by whether C's own aim pots: where it does (35), level 3 B 72.7% against C 54.7%, level 5
92.9% against 80.9%; where it does not (25), B 44.6% and 75.7% against C's 2.1% and 0.1% (its safeties). So most of A2's
margin is the 25 positions with no ghost-ball pot, where B finds banks, kicks and other lines; on the positions both can
pot, B's margin is the wider window it aims into (B's level-5 windows a median 0.0136 rad, about 0.78°). The fixed-tick
engine's map has a median 545 edges a power, pot windows a median 0.001 rad wide, and 481 of the bridged pot pieces had a
leaf off the piece's own events (hidden changes between scan aims, as PEB run 5 found on a 1,024 scan).

What it says. B, the map of the whole circle, is a better planner than the games' ghost-ball line on every measure tried,
and its price is about four thousand times the flights. A3's 4,000 was my guess and is killed by a factor of twelve. A7,
K is n (R1263), is killed on this engine, by the engine: the fixed tick puts jumps inside every span (PEB run 1), so a span
whose leave must be held to 10⁻⁶ is halved until the cap, and B′ never reaches a piece the size of a pot window. The test
of R1263 that can pass is on an engine whose pieces are smooth between its events (PEB runs 4–5, the event engine); a
B′ there is the next run, if wanted. Nothing in `games.html` was changed, and carrying B into it is not proposed on this run:
4,000 times the flights is minutes of thinking on a phone, against the 48 shots now.

### Run 2, planned (26 Nov 2026; Tom: "Continue if your still making progress"). Predictions written before any script exists

Run 1 left R1263 untested where it can pass: on the fixed-tick engine every span holds hidden jumps. Run 2 puts B′ on
PEB's event engine with its full signature (PEB run 5's copy `runs/peb/play-trick-event5.html`, motion unchanged), on
PEB run 5's two maps: the cut on the open table and the challenge "two rails", power 14, rest places of the white and the
object ball as the leave (PEB's four outputs). PEB run 5 mapped them by a scan of N = 1,024 aims, each change bisected
(cut 75 jumps, two rails 109, known beforehand), and its post hoc found five pieces with a jump the scan never saw (cut
0.124–0.141, 0.145–0.160, 2.387–2.424, 3.958–3.995; two rails 0.389–0.406).

**B′ as run** (`runs/nbs/nbs2.mjs`): start from S even spans of the circle. A span flies its K = 8 Chebyshev leaves. If two
neighbouring leaves differ in the full signature, the change between them is bisected to 10⁻¹² rad, one flight a step, and
the span is cut there; the pieces left are spans again. If all leaves agree, the span is a piece when the last two
Chebyshev coefficients of every output are under 10⁻⁷ table units; otherwise it is halved. Nothing is scanned: the leaves
are the only aims flown that are not bisection steps. A span under 10⁻¹² that still fails is counted as dropped. Cap
200,000 flights a map. Its flights are counted against the scan's: 1,024 + the bisection steps PEB run 5 took (60 at most a
jump), its bridges not counted.

- **C1 (it settles).** On both maps B′ finishes under its cap with no span dropped wider than 10⁻⁹.
- **C2 (the same jumps).** Every jump of PEB run 5's map is found by B′ (a B′ jump within 10⁻⁹ rad, the same signatures
  either side).
- **C3 (and the hidden ones).** In at least 4 of the 5 pieces PEB run 5's post hoc flagged, B′ finds a jump inside.
- **C4 (pieces held).** Of B′'s pieces wider than 10⁻⁴, at least 95% have their K = 8 bridge hold all four outputs to 10⁻⁶
  on 200 aims spread through the piece (the coefficient test is not fooled).
- **C5 (no N).** With S = 64 starting spans instead of 16, B′ finds the same jumps (C2's sense, both ways) and its flights
  change by under 20%.
- **C6 (cost).** B′'s flights per map are at most 2 × the scan's (1,024 + its bisections), and at most 12 K per piece plus
  45 per jump.

Each killed by its own number. Known beforehand: PEB runs 4–5 (the jumps, the pieces held, 6 leaves the median, 19 pieces
converging slowly near their ends, where B′ will halve and pay), so C2 and C4 are not blind; C3, C5 and C6 can fail.
If C1–C6 stand: on an engine whose pieces are smooth between the table's events, the map's cost is counted in leaves a
piece and steps a jump, with no scan count in it, which is R1263 shown on one table; carrying it to the 9-ball computer
would need that engine in `games.html`, Tom's call.
