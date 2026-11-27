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

### Run 2 (26 Nov 2026; `runs/nbs/nbs2.mjs`, outputs `runs/nbs/nbs2-{cut,tworail}-{16,64}.json`, `nbs-run2.txt`)

Choices made in writing the runner, before any result was read: the leaves are Chebyshev–Lobatto (the span's ends
included, so every aim lies between two neighbouring leaves of some span; first-kind leaves would leave a change between
two spans unseen), and each aim is flown once (a cache; a shared end costs one flight); the scan's bisection steps are
counted as PEB run 5's loop takes them, 33 a jump. Two faults of mine found while running, fixed before the counted runs:
a span already narrower than 10⁻¹² that held a change was cut again for ever (now recorded as a jump), and the full
signature kept as a string filled the page's memory (now a 52-bit hash of its keys). The cut's numbers are the same
before and after both fixes.

| | cut | two rails |
| --- | --- | --- |
| flights, S = 16 | 9,149 (4,414 leaves, 4,735 bisection steps) | 200,007, capped |
| the scan's (1,024 + bisections) | 3,499 | 4,621 |
| jumps, pieces | 137, 348 | 24,748, 21,249 (24,645 and 20,943 inside 0.5352–0.5355) |
| PEB run 5's jumps found | 75 of 75 | 45 of 109 (47 of the 47 below where B′ stopped, by place) |
| pieces wider than 10⁻⁴ held to 10⁻⁶ by their 8 leaves | 222 of 222 (worst 2.9·10⁻⁹) | 151 of 151 (worst 5.6·10⁻⁹) |
| S = 64 against S = 16 | the same 137 jumps; flights 0.979 | capped at the same place; flights 1.000 |

- **C1 KILLED** by two rails, by the engine. Near the aim 0.53534 rad the white comes to rest touching the 1 and the
  event engine chatters: contact, stop, restart, up to 599,920 events a shot, the full signature different at every
  aim down to 10⁻¹⁴ rad (5,566 such flights). B′ finds a change between every two leaves there and bisects each, so it
  spent its cap in a window 3·10⁻⁴ rad wide and mapped nothing past 0.5353. The cut settles in 4 seconds.
- **C2 KILLED** by two rails' cap: the 62 jumps it missed lie past where it stopped; on the cut, and below 0.5353 on two
  rails, every one of PEB run 5's jumps is there (one, at 0.454072, matched by place only: B′ found it as two jumps
  8·10⁻¹³ apart, a sliver of another order between, which PEB's bracket straddled; my check's signatures, not a miss).
- **C3 not killed.** The cut's four flagged pieces each have a jump inside (0.124 two, the others one); two rails'
  0.3897–0.4064 has five, which my lookup (0.389 within 6·10⁻⁴, my code) did not find, so the report says 4 of 5; it is 5.
- **C4 not killed.** 373 of 373 pieces wider than 10⁻⁴ held to 10⁻⁶ on 200 aims each; the coefficient test was never
  fooled.
- **C5 KILLED** by two rails (both capped in the chatter, their jump lists differing there by a few); on the cut not
  killed: 16 or 64 starting spans give the same 137 jumps and flights within 2.1%.
- **C6 KILLED.** The cut cost 2.6 times the scan's flights, against my 2; two rails capped. The bound per piece and jump
  held on both (cut 9,149 against 39,573), but it is loose.

**What it says.** On the cut, R1263 holds as stated: B′ has no scan count, starts from 16 or 64 spans to the same map,
finds every jump the 1,024 scan found and 62 it stepped over (among them the five the scan's post hoc suspected), and
every piece is held by its own 8 leaves to 10⁻⁶; its flights are leaves and bisection steps, 26 a piece. It costs 2.6
times the scan because the scan's map was wrong by 62 jumps; a scan fine enough to find them all would cost more. On
two rails the same procedure meets a place where the engine has no pieces at all (a ball left touching another chatters
without end), and a map that will not stop until every piece is held spends everything there. The scan stepped over it
(PEB run 5 saw one jump at 0.535336). So B′ does what the scan cannot, says where the map has no pieces, and needs a rule
for such a place: stop halving a window whose leaves change at every width (here 10⁻¹⁴) and mark it unmapped, or an
engine that settles a touching pair. Neither is in this run.

### Run 3, planned (27 Nov 2026; Tom: "1"). Predictions written before any script changes

Run 2's B′ spent its cap on two rails in a window where a touching pair chatters, the full signature different at every
aim down to 10⁻¹⁴. Run 3 gives B′ a rule for a place with no pieces, and nothing else changes (the engine, the maps, K,
the tolerance, the cap). **The floor**: a span narrower than w₀ = 10⁻⁷ rad whose 8 leaves show three or more different
signatures (two changes or more among eight aims inside 10⁻⁷) is marked unmapped and not looked into again; a narrow
span with two signatures is bisected as before (one jump), and a narrow span whose leaves agree but whose coefficients
fail is marked unmapped too. Neighbouring unmapped spans are joined into windows. Everything else is run 2's B′.

- **D1 (it finishes).** Both maps finish under the cap at S = 16 and S = 64.
- **D2 (only where the engine chatters).** On two rails the unmapped windows total under 10⁻³ rad, and at least 90% of
  their measure lies within 0.5352–0.5356 (run 2's chattering window).
- **D3 (the jumps outside).** On two rails every jump of PEB run 5 not inside an unmapped window has a B′ jump within
  10⁻⁹ rad (by place; run 2 showed one true jump can come back as two 10⁻¹² apart, so signatures are not compared).
- **D4 (the cut unchanged).** On the cut the same 137 jumps as run 2, unmapped measure under 10⁻⁷ rad, flights within 5%
  of run 2's 9,149.
- **D5 (pieces held).** On two rails at least 95% of pieces wider than 10⁻⁴ rad held to 10⁻⁶ by their 8 leaves.
- **D6 (no N).** On two rails S = 16 and S = 64 find the same jumps outside unmapped windows, flights within 20%.
- **D7 (cost).** Two rails' flights at most 4 × the scan's 4,621.

Each killed by its own number. Known beforehand: run 2 (where the chatter is, the cut's numbers); D2's "at least 90%"
and D7 are guesses. If D1–D6 stand: a map with no scan count says where the table has pieces and where it does not, at a
cost of leaves and steps, and the window it gives up on is the engine's, not the table's.

### Run 3 (27 Nov 2026; `runs/nbs/nbs3.mjs`, outputs `runs/nbs/nbs3-{cut,tworail}-{16,64}.json`, `nbs-run3.txt`)

| | cut | two rails |
| --- | --- | --- |
| flights, S = 16 | 8,465 (run 2 9,149) | 200,004, capped |
| jumps, pieces | 137, 292 | 7,578, 2,940 (7,475 of the jumps at 0.53533–0.53537) |
| unmapped | 4 windows, 2.7·10⁻⁷ rad | 8 windows, 3.2·10⁻⁵ rad, 99.0% inside 0.5352–0.5356 |
| pieces wider than 10⁻⁴ held to 10⁻⁶ | 222 of 222 | 151 of 151 |

- **D1 KILLED** by two rails, by my floor. 10⁻⁷ is far below the chattering band, which runs at least from 0.53533 to
  0.53537 (4·10⁻⁵ rad): every span in it wider than the floor that holds a change is bisected (about 33 chattering flights
  a jump, up to 600,000 events each), and the cap went in finding 7,475 jumps there; the map reached 0.53537 and stopped.
- **D2 not killed.** What was marked unmapped on two rails is 3.2·10⁻⁵ rad, 99.0% of it in the chattering window.
- **D3 KILLED** by the cap again: 62 of PEB run 5's 104 jumps outside the unmapped windows lie past 0.5379, never reached;
  all 42 before it found.
- **D4 KILLED**: on the cut the floor marks four slow-converging ends (0.0596, 0.4115, 1.1015, 1.2798; 2.7·10⁻⁷ rad in
  all) that run 2 halved below 10⁻⁷ and held, and that saves 7.5% of the flights; the same 137 jumps.
- **D5 not killed**: 151 of 151 on two rails, 222 of 222 on the cut.
- **D6 KILLED**: both capped (flights 1.000); outside both runs' windows 98 of 100 and 98 of 99 jumps shared, the
  differences in the chattering band's edge.
- **D7 KILLED**: capped.

**What it says.** A floor on width cannot tell a place with no pieces from a place with many: the chattering band is
4·10⁻⁵ rad wide with jumps at every scale inside it, and the cut's slow ends are 10⁻⁷ rad wide with none. What tells them
apart is how many jumps a span holds for its width, not its width. A run 4 would mark a span unmapped when it has yielded
more than a set number of jumps (say 64) and none of its pieces is wider than its K-th part, with predictions written
first; or the engine settles a touching pair (step 2 of R1273's list). Not run.

### Run 4, planned (27 Nov 2026; Tom: "Run 4"). Predictions written before any script changes

Run 3 found that a floor on width cannot tell a place with no pieces from a place with many. Run 4 replaces the floor
with a count. **The busy rule**: every span B′ opens keeps a tally of the jumps found inside it and of the widest piece
held inside it. When a span has yielded more than J = 64 jumps and no piece inside it is wider than its K-th part
(w/8), it is marked unmapped and nothing still waiting inside it is opened. Neighbouring unmapped spans are joined into
windows. Run 3's floor is gone; everything else is run 2's B′ (the engine, K = 8, the tolerance 10⁻⁷, the cap of 200,000
flights, the bracket rule at 10⁻¹²). A span counts its jumps as they are found, depth first, so a span can be marked
before its later pieces are reached; that is part of the rule as tested.

- **E1 (it finishes).** Both maps finish under the cap at S = 16 and S = 64.
- **E2 (only where the engine chatters).** On two rails the unmapped windows total under 10⁻³ rad, at least 90% of their
  measure within 0.5352–0.5356.
- **E3 (the jumps outside).** On two rails every jump of PEB run 5 not inside an unmapped window has a B′ jump within
  10⁻⁹ rad (by place).
- **E4 (the cut unchanged).** On the cut nothing unmapped, the same 137 jumps as run 2, flights within 5% of its 9,149.
- **E5 (pieces held).** On two rails at least 95% of pieces wider than 10⁻⁴ rad held to 10⁻⁶ by their 8 leaves.
- **E6 (no N).** On two rails S = 16 and S = 64 find the same jumps outside both runs' unmapped windows, flights within 20%.
- **E7 (cost).** Two rails' flights at most 4 × the scan's 4,621.

Each killed by its own number. Known beforehand: runs 2 and 3 (the chattering band at least 0.53533–0.53537, 7,475 jumps
found in it before the cap; the cut's 137 jumps, none closer than run 2 held). J = 64 and the K-th part are my choices;
E2's 90% and E7 are guesses. If E1–E6 stand: the count a span yields tells a place with no pieces from a place with
many, and the map needs no N to say where the table has pieces.

### Run 4 (27 Nov 2026; `runs/nbs/nbs4.mjs`, outputs `runs/nbs/nbs4-{cut,tworail}-{16,64}.json`, `nbs-run4.txt`)

| | cut, S = 16 | cut, S = 64 | two rails, S = 16 | two rails, S = 64 |
| --- | --- | --- | --- | --- |
| flights | 9,149 | 8,954 | 12,600 | 14,548 |
| jumps, pieces | 137, 348 | 137, 378 | 201, 515 | 229, 614 |
| unmapped | none | none | 0.0612–0.7854 (0.724 rad) | 0.4909–0.5890 (0.098 rad) |

- **E1 not killed.** All four finish, two rails in 12,600 and 14,548 flights (runs 2 and 3 capped at 200,000).
- **E2 KILLED**, by my rule. The window given up is not the chatter but the largest span holding it: at S = 16 0.724
  rad, only 0.1% of it within 0.5352–0.5356; at S = 64 the whole starting span, 0.098 rad. The tally runs up the chain of
  spans, and a large span's count passes 64 as soon as its smallest one's does, with its count of jumps the sum of
  everything found in it; its widest piece is still under its eighth because the map, depth first, had not yet reached
  its wide pieces. I named this risk in the plan and kept the rule as written.
- **E3 not killed**: all 54 of PEB run 5's jumps outside the window found within 10⁻⁹.
- **E4 not killed**: the cut unchanged from run 2, 137 jumps, nothing unmapped, 9,149 flights.
- **E5 not killed**: 262 of 262 pieces wider than 10⁻⁴ held to 10⁻⁶ on two rails (worst 2.7·10⁻⁹), 222 of 222 on the cut.
- **E6 not killed**, in its letter: outside both windows (so outside the S = 16 run's 0.724 rad) the two runs share all
  70 jumps, flights 1.155 apart. With so much given up the clause tests little.
- **E7 not killed**: 12,600 flights against 4 × 4,621.

**What it says.** A count stops the map where a width could not: the chattering place is given up and every map
finishes, cheaply, without touching the cut. But the rule as written gives up the widest span that holds the chatter,
not the chatter: a tally counted up the whole chain of spans fires first at the top. The fix is to give up the smallest
span that qualifies (the one where the count passes J, checked only on the span being opened, not its ancestors), with
the jumps' count per width still the test. A run 5, predictions first, not run.

### Run 5, planned (27 Nov 2026; Tom: "Merge, then run 5"). Predictions written before any script changes

Run 4's count stopped the map but gave up the largest span holding the chatter. Run 5 changes only which span is given
up. **The smallest busy span**: each jump found adds one to the tally of every span it lies in, as in run 4; when a jump
takes one or more spans past J = 64 with no piece wider than their eighth, only the smallest of them is given up, and its
live tally is then taken off every span above it, so a span is given up only for jumps outside the windows already
given up. Everything else is run 4's (no width floor, K = 8, 10⁻⁷, the cap, the bracket rule at 10⁻¹²).

- **F1 (it finishes).** Both maps finish under the cap at S = 16 and S = 64.
- **F2 (only where the engine chatters).** On two rails the unmapped windows total under 10⁻³ rad, at least 90% of their
  measure within 0.5352–0.5356.
- **F3 (the jumps outside).** On two rails every jump of PEB run 5 not inside an unmapped window has a B′ jump within
  10⁻⁹ rad.
- **F4 (the cut unchanged).** On the cut nothing unmapped, the same 137 jumps, flights within 5% of 9,149.
- **F5 (pieces held).** On two rails at least 95% of pieces wider than 10⁻⁴ rad held to 10⁻⁶.
- **F6 (no N).** On two rails S = 16 and S = 64 find the same jumps outside both runs' windows, flights within 20%.
- **F7 (cost).** Two rails' flights at most 4 × 4,621.

Each killed by its own number. Known beforehand: runs 2–4 (the band at least 0.53533–0.53537; run 4's numbers); the
window's width under this rule I have not worked out, so F2 is the test that matters. If F1–F7 stand: a map with no scan
count says where the table has pieces and gives up only the place where the engine has none.

### Run 5 (27 Nov 2026; `runs/nbs/nbs5.mjs`, outputs `runs/nbs/nbs5-{cut,tworail}-{16,64}.json`, `nbs-run5.txt`)

Every number is run 4's to the flight: the cut 9,149 and 8,954 flights, 137 jumps, nothing unmapped; two rails 12,600 and
14,548 flights, 201 and 229 jumps, one window 0.0612–0.7854 (two starting spans, joined) at S = 16 and the starting span
0.4909–0.5890 at S = 64.

- **F1, F3–F7 not killed**, as E1, E3–E7 (54 of 54 outside jumps found, 262 of 262 wide pieces held, the cut unchanged,
  S = 16 and 64 sharing all 70 jumps outside both windows, 12,600 flights).
- **F2 KILLED**, by my rule again: 0.724 rad given up, 0.1% of it in the chattering window.

**Why the smallest busy span is the largest.** At S = 64 the window holds 65 jumps, 54 of them at one place, 0.5353361
(the touching pair's chatter), and no piece wider than 9.2·10⁻³ against its eighth, 1.2·10⁻². B′ cuts a span at each
jump it finds, so every span it makes ends at a jump: the chatter's jumps always sit at the edge of the spans that hold
them, each of which reaches back to a far end of the span it was cut from. No span B′ makes ever encloses the chatter
narrowly, and so no small span can hold 64 of its jumps; the first span that does is the one it started in. Run 4's
rule and run 5's give up the same span for this reason, not for the reason run 4 gave (the order of the tally). A count
has to be taken about a place, not over a span: for example, the jumps found within w/K of the new jump inside the span
being cut. A run 6, predictions first, not run.
