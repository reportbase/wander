# TWR: a tower of ratios, built while walking

27 Oct 2026. Tom: "When I think situated geometry, I think a tower of ratios, and as i move around, new ratios are added
and old ones are removed."; "yes, plan the test and lets build on other classical ideas … would it be possible for a reader
to build with ratios only, and not care about writing." The note this tests is `plans/tower-note.md`.

## The claim

A walking reader holds a tower in scale (links: a size over a size) and a tower in time (legs: each leg over the last).
Moving churns its addresses and leaves its links standing; each step adds a link; a loop checks the links; and a lone
reader builds everything it does alone from ratios in its own H (its first leg), with writing needed only for an amount
from outside or for another reader with nothing in view in common.

Known beforehand (cited as such): bearing rigidity (a framework fixed up to translation and scale by its bearings;
Eren et al. 2003, Zhao and Zelazo 2016); structure from motion and monocular SLAM recover a scene up to one scale, which
drifts along a walk and a loop corrects as a similarity (Strasdat, Montiel and Davison 2010); cycle consistency of ratios
on a graph (Hodge decomposition; Jiang et al. 2011); the Brownian bridge; OFS's tower of holds, "Closing a loop" and
"Sweeping from zero"; `room-walk.html` (things placed in H from bearings alone, legs in known directions); TGT (two
readers' holds related exactly by closure); RWT (steps to writing counted by the Jacobian's nullity). Draw's labs, read
for this plan at draw `ea07709`: `cyc` (the cycle sheet: ratios with no common unit, a ground exactly when every cycle
closes, the obstruction from the readings alone), `udv` (three standpoints give the figure up to size, one length the
size), `owt` (which quantities survive similarity, affine and projective accounts). What is ours: the reading (address
churn against link persistence, dropping and mending, and where writing first becomes unavoidable).

## Set-up

`runs/twr/twr.py`, mpmath at 50 digits for the exact parts, float64 with a seeded generator for the noisy ones.

- **The world** (the referee's, in metres, never read): a building 20 × 16 of four rooms 10 × 8; in each room three
  things, rectangles of seeded sizes and places; features are the 16 room corners and the 48 things' corners (64).
- **The walk**: a closed loop of N = 32 stops through the four rooms and back to the start, seeded jitter off a
  rectangle. The reader **reads its turns** (each leg's heading in its own frame, its first heading 0) and **never its
  leg lengths**. At each stop it holds the features within a view radius R = 6 m (the referee's cut, standing in for the
  held window and occlusion), and reads each held feature's direction.
- **The reader's map** (ratios only): leg 1 is H. Features seen from stops 0 and 1 are placed by crossing their rays.
  Each later leg's length is solved from any feature already placed and seen from the new stop (the new stop lies on its
  ray back and on the leg's known heading: two equations, two unknowns), then new features are placed by crossing. With
  noise every placed feature seen from the new stop votes (least squares on the leg length; crossings averaged over the
  stops that see a feature). No amount enters.
- **Links**: each thing's width and depth over its room's width; each pair of things in one room, their centres'
  distance over the room's width; each room's width over the building's (where both are placed).
- **Scaling the world**: k ∈ {10⁻³, 7, 10³} multiplies every referee length.
- **Memory**: a reader that keeps at most M features (those seen most recently), forgetting the rest and their places.
- **Noise**: every direction read off by a normal error of sd ε (10⁻³ rad unless stated), 400 seeded walks.

## Predictions (written before any script)

- **T1 (ratios only, exact).** At ε = 0 the reader's map of every feature it saw, in units of its first leg, equals the
  referee's map translated to the first stop, turned to the first heading, and divided by the first leg's true length,
  to 10⁻⁴⁰. Kill: any feature further off, or any leg not solvable on this walk.
- **T2 (scaling the world).** At every k every quantity the reader holds (map, legs in H, links) is unchanged to 10⁻⁴⁵.
  Kill: any change.
- **T3 (the ground floor churns, the upper floors stand).** (a) At every stop every held direction differs from the one
  read at the stop before (no direction survives a step), and on this walk at least one feature is added or dropped from
  the held set at every step. (b) Every link computed from the map of any two consecutive stops that see its features
  equals the referee's ratio to 10⁻⁴⁰, whichever pair is used. Kill: (a) a direction unchanged by a step, (b) a link
  differing.
- **T4 (dropping and mending).** With memory M, the tower in time breaks at a step exactly when no remembered feature is
  seen from the new stop off the leg's line; the map then falls into pieces, one more than the breaks, each in its own
  H. (a) At ε = 0, every link read within one piece equals the referee's to 10⁻⁴⁰ (pieces lose only their relative scale
  and place). (b) Two pieces that later see a common thing (two features) are rejoined by that one link: the ratio of
  their H's comes out exact to 10⁻⁴⁰, with no amount. (c) A link whose features were forgotten is read again on the
  loop's return, equal to its first reading to 10⁻⁴⁰. Kill: a break where the rule says none or none where it says one;
  any link or rejoining ratio off.
- **T5 (drift and the loop).** With ε = 10⁻³, the log of the reader's scale at stop i (its leg i over the referee's, over
  the same for leg 1) has sd growing as i^p over i = 4 … 16, with p = 0.5 ± 0.1 (a random walk). Closing the loop (stop N
  sees the features of stop 0, which gives the scale's closure ratio) and spreading the log closure evenly over the legs
  (the gradient projection on the cycle) leaves the sd at the loop's middle (i = 16) at 1/√2 of the open chain's there
  (the Brownian bridge), within 0.1, and at 0.5 ± 0.1 of the open chain's at its end (i = 32). Kill: p, or either ratio,
  outside its band.
- **T6 (what needs writing).** (a) Which of two things is bigger (all pairs, by area), (b) the shorter of two routes
  between rooms (through stated door points), (c) the direction home from every stop, (d) steps to reach a thing walking
  straight at it at a constant stride: from the map alone, every decision equals the referee's and every number its ratio
  at every k (all agree, 10⁻⁴⁰ for the numbers). (e) Seconds to arrive at 1.2 m/s: the map from readings to that amount
  has nullity 1 (one amount missing, RWT's count), nullity 0 with the first leg's metres carried in, and then exact.
  (f) Two readers with different walks and first legs: with one thing (two features) seen by both, their maps agree after
  one similarity found from that thing alone, every other feature to 10⁻⁴⁰, and the ratio of their H's is read, no amount
  passed; with no feature in common the ratio is undetermined (nullity 1). Kill: any decision off, any nullity other than
  stated, any feature off.

## Not claimed

Nothing about animals, robots or any field's results (R364); the classical anchors in the note are context. The view
radius stands in for the held window and occlusion and is the referee's, not a reading.

## Runs

### Run 1 (27 Oct; `runs/twr/twr.py`, output `runs/twr/twr-run1.txt`)

Crashed in T3 on my code (a set combined with a bool), after T1 and T2 had printed. No verdicts.

Set-up as built, differing from the text above: the room corners are the 9 distinct points of the 3 × 3 grid (the "16"
above counted shared corners twice), and four door points (the middles of the shared walls) were added as features for
T6(b)'s routes: 61 features. The walk: 32 stops round a rectangle (3, 3)–(17, 13) m, jitter ±0.5 m (seed 2).

### Run 2 (`runs/twr/twr-run2.txt`; the crash fixed, nothing else)

- **T1 not killed.** All 31 legs solved, no break, all 61 features placed; the map in units of the first leg equals the
  referee's to 1.5·10⁻⁴⁵ (legs 4·10⁻⁴⁶).
- **T2 killed, by my tolerance.** At k = 10⁻³, 7, 10³ the map moved by up to 5.4·10⁻⁴⁵, the legs 1.5·10⁻⁴⁵, the links
  8·10⁻⁴⁶: rounding at 50 digits, above my 10⁻⁴⁵. Nothing moved beyond rounding.
- **T3 killed in (a)'s second clause, by the walk.** No direction survived a step (the first clause holds), but at stops 5
  and 19 the held set did not change (a 6 m cut and steps of about 1.5 m). (b) not killed: 77 link readings from all 31
  consecutive pairs (37 distinct links), each the referee's to 1.5·10⁻⁴⁵.
- **T4 not killed.** M = 2 breaks the chain 5 times (6 pieces), M = 3 once, M ≥ 4 never. Within pieces every link the
  referee's (to 6·10⁻⁴⁶); 8 rejoinings at M = 2 and 1 at M = 3 give the ratio of two pieces' H from one thing, exact
  (to 5·10⁻⁴⁸); 13 links forgotten and read again equal their first reading. The rule's agreement is by construction
  (the reader breaks exactly when it finds no remembered, placed feature off the leg's line), a consistency check only.
- **T6 killed in (f)'s second clause, by my tolerance.** (a) all 66 pairs, (b) all 18 routes agree at every k; (c) home
  and (d) steps to 5·10⁻⁴⁵; (e) the readings identical at k = 1 and 7 while the seconds differ sevenfold (nullity 1),
  and with the first leg's metres carried in the seconds exact (3.6·10⁻⁴² at k = 10³); (f) two readers sharing 42
  features aligned by one thing alone, every other feature to 3·10⁻⁴⁵, H_B/H_A read 1.69566788164 against the true
  1.69566788164. The check that B's map is unmoved when only B's world is scaled failed at 1.6·10⁻⁴⁵ against my
  10⁻⁴⁵: rounding.
- **T5 crashed, no verdict; killed by my set-up.** With rays kept 4 stops (to keep the chain open), the least-squares
  leg flips sign at legs 13 or 29 in about one walk in twenty (walks 1, 2, 16, 34, 74, 103, 115, 167, 169, 199 of the
  first 200), so the log of the scale is undefined there; the legs are not short (1.0 and 1.9 m).

### Run 3: predictions (written before it)

- **T2′, T6(f)′.** The same claims at 60 digits, the bound 10⁻⁴⁵ unchanged. Kill: as before.
- **T5′.** Rays kept 8 stops (more parallax for each leg). No walk of the 400 flips a leg's sign (kill if any does),
  and, as before, p = 0.5 ± 0.1 over i = 4 … 16, the sd at the loop's middle after closure 1/√2 ± 0.1 of the open
  chain's there and 0.5 ± 0.1 of the open chain's at its end.

### Run 3 (`runs/twr/twr-run3.txt`; 60 digits, rays kept 8 stops)

- **T2′ not killed.** At k = 10⁻³, 7, 10³ nothing moves beyond 3·10⁻⁵⁵.
- **T6(f)′ not killed.** B's map unmoved when only B's world is scaled (to 10⁻⁵⁵): the ratio of the two H's is
  undetermined with nothing in common, read exactly with one thing in common.
- T1, T3, T4 and T6's other clauses as in run 2, at 10⁻⁵⁵ (T3 (a)'s second clause killed again by the walk).
- **T5′ killed.** 23 of 400 walks still flip a leg's sign, always at legs 13 or 29; over the 377 clean walks the
  log scale's sd is 0.021, 0.020, 0.183, 0.274 at stops 4, 8, 16, 32, a jump between 8 and 16, so p = 1.83, not ½. The
  closure ratios land in their bands (0.679 against 0.707, 0.453 against 0.5). Post hoc, those legs are not badly
  conditioned overall (9 and 13 candidate features, parallax up to 63° and 83°); the likely cause is my estimator: a
  feature placed from two nearby stops with little parallax lands far off, and least squares on the leg, blind to
  that, follows it. The chain is then not a sum of small independent steps.

### Run 4: prediction (written before it)

- **T5″.** Each leg the median of the per-feature leg estimates (each placed feature seen from the new stop gives one,
  cross(b, X − P)/cross(b, u)), rays kept 8 stops, everything else as run 3. No walk of the 400 flips a leg's sign (kill
  if any does), p = 0.5 ± 0.1 over i = 4 … 16, and the two closure ratios 1/√2 ± 0.1 and 0.5 ± 0.1.

### Run 4 (`runs/twr/twr-run4.txt`; the median leg, 60 digits, rays kept 8 stops)

- **T5″ killed, by my prediction of the growth.** No walk of the 400 flips a sign, and the log scale's sd is 0.0065,
  0.0072, 0.0082, 0.0100 at stops 4, 8, 16, 32 (about 30 times smaller than run 3's at 16). Closing the loop leaves
  0.649 of the open chain's sd at the middle (1/√2 = 0.707, within 0.1) and 0.531 of its sd at the end (0.5, within
  0.1). But the sd grows as i^0.26, not i^0.5. Post hoc: with rays kept 8 stops, neighbouring legs are read against
  mostly the same features, so their errors are not independent steps, and a random walk was the wrong model for this
  chain; the closure still spreads its error as a bridge would.
- T1, T2, T3 (b), T4, T6 as in run 3.

## What TWR says

A reader walking with nothing but its own turns and the directions to what it can see builds the whole map exactly in
units of its first leg (T1), and nothing it holds moves when the world is scaled (T2′). Its addresses change at every
step and its links do not: every ratio of lengths read from any two consecutive stops is the referee's (T3 (b)). The
held set need not change at every step (T3 (a)'s second clause, killed by this walk). With too little memory the chain
of legs breaks into pieces, each exact in its own unit, and one thing seen by two pieces rejoins them by a ratio, with
no amount (T4). Everything it does from where it stands, comparing sizes, choosing routes, finding home, counting steps,
needs no amount; an amount in seconds needs one carried in, and two readers that share one thing align with none (T6).
With noise, how the scale drifts depends on the estimator: least squares followed badly placed features and flipped the
scale (runs 2–3); the median did not, and closing the loop then shared out the drift as a bridge would, though the drift
itself grew more slowly than a random walk (run 4). The exact parts restate bearing rigidity and the scale ambiguity of
structure from motion; the reading (the tower, its churn and its links, writing as the one amount) is ours.
