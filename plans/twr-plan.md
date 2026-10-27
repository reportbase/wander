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

(none yet)
