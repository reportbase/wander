# RSH: recovering 3D shapes from addresses (games' Levels)

*17 October 2026 (Tom's local date). Tom, 15:36: "In draw.html we uses the address to recover the shape of two d
shapes with cauchy. Let's create a new lab that recovers 3d shapes."; 15:38: "Let's do this in levels application of
games.html. it has the 3d shapes." The lab lives in reportbase/games (`LEVELS_APP`, `games.html`); this plan holds its
predictions, written before the code exists, and its runs. Geometry, exact (floating point, no noise).*

## Known beforehand (draw's labs, read at `ea07709`)

- **RCC** (the recovered circle): one reader's readings v/h carry the turn and nothing else; they are Cauchy for every
  figure, and the census gives back the same unit circle from every one.
- **UDV** (undoing the division): three readers inside the figure, each holding only its own quotients, draw a line
  apiece toward every place on the outline; where two cross is the place. Knowing only the shape of their own triangle
  they recover the figure exactly up to its size; one length, how far apart two readers stand, gives the size.
  Which reading belongs to which place is given.
- **WHR, SMP**: walked along the outline, the arrival density is the arc element; not used here.
- wander: WDG (`plans/wdg-plan.md`): directions uniform over the octant read (v/h, v₂/h) as the two-dimensional
  Cauchy, every pair's median at its corner, the near field in both readings a third. OFS §9, "A sphere in a cube":
  the address the same at every size, the amounts needing the extent.

So this is UDV and RCC in three dimensions: nothing here is expected to be new geometry. What it adds is the third
relation (each reading a direction [h : v : v₂], two ratios) and the stretch: a body's extents differ by axis, which
the census cannot see and the readers can.

## The bodies

Every Levels board carries one body, seeded by its id (`bodyOf`): a ball with relief in four bands (five waves each,
frequency 3, 6, 12, 24), stretched by s = (s_x, s_y, s_z) ∈ [0.8, 1.3]. Its surface in the direction u from its
centre is c + diag(s)·R(u)·u, R(u) = ½(1 + Σ waves(u)), all four bands at full weight. It is star-shaped from its
centre: each direction from the centre meets it once.

## The lab

1. **One reader at the centre, addresses only** (RCC in 3D). It sweeps N = 4,096 directions d, even over the sphere (a
   Fibonacci lattice), and each meets the surface once; the reading is the direction to the point met, split per octant
   as [h : v : v₂] = |d|. The census (every direction drawn at the one length H) gives a sphere.
2. **Three readers inside, addresses only** (UDV in 3D). Readers at the centre plus 0.12 of the body's least half-extent
   along three directions (a triangle about the centre, tipped out of every axis plane), facing one common frame, each
   holding only the unit direction to every surface point; which point a direction belongs to is given. Each point is
   placed where the rays from the two readers that see it squarest cross (least squares on two rays). Every length is
   then laid in the one length the readers know of themselves: the side of their triangle, A to B.
3. **One length**: |AB| carried in, and the recovered body is in the world's units.

## Predictions (written before any code)

On 200 boards (ids 0–199):

- **P1 (one reader reads the sweep, not the body).** For every body the 4,096 readings equal the lattice's own
  directions to 10⁻¹², so the readings of any two bodies agree to 10⁻¹². Their shares: P(v ≤ h) = ½ and
  P(v ≤ h and v₂ ≤ h) = ⅓, each within 0.01 (WDG's exact values; the lattice's sampling error). The census returns the
  unit sphere from every body (every recovered radius 1, to 10⁻¹²). *Killed* if any body's readings differ from the
  lattice's, or a share is off by more than 0.01.
- **P2 (three readers recover the body up to its size).** Every point the readers see, laid in |AB|, equals the true
  point laid in |AB| to 10⁻⁹ (relative to the body's mean radius), on every body. *Killed* if any point misses.
- **P3 (the stretch is recovered, by the readers, not the census).** The recovered body's extents along the three axes
  stand in the true ratios (s_x : s_y : s_z times the relief's own) to 10⁻⁹; the census's are 1 : 1 : 1 on every body.
  *Killed* if either fails.
- **P4 (scale the world).** Scaling a body and its readers together by k = 10⁻³, 7, 10³ changes no reading of the one
  reader and no recovered point in |AB|, to 10⁻⁹. With |AB| carried in, the recovered body is the true one at each k,
  to 10⁻⁹ of its mean radius. *Killed* if any moves or misses.
- **P5 (what each sees).** A reader inside sees a surface point when the segment to it leaves the body nowhere before
  it (checked at 64 steps along the segment against the surface's radius in that direction). Prediction: on every body
  every point is seen by at least two readers. *Killed* if any point on any body is seen by fewer than two (then P2 is
  measured on the points seen by two, and the kill stands).
- **P6 (bodies told apart).** From the one reader no two bodies differ (P1); from the three readers in |AB| every pair
  of the first 20 bodies differs somewhere by more than 0.01 of the mean radius. *Killed* if any pair does not.

P1 and P4's one-reader part are near identities (a kill would be my code); P2, P3 and P4's recovery are the claim that
directions from a known triangle undo the division in three dimensions as in two; P5 says whether the bodies allow it.

## What would and would not be shown

Exactness, not robustness: no noise, no finite resolution, the correspondence given. That a sweep's readings are its
own addresses for every body, that three readers' directions and the shape of their own triangle give the body up to
size, and that one length gives the size. Not how a reader would find which direction belongs to which point, and
nothing about light or physics.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (17 Oct, `node rsh/rsh-run.mjs`, driving `games.html?app=levels` through `LEVELS_APP._debug.recover` in headless Chromium; output `rsh/rsh-run1.txt`, 5 min)

- P1 not killed: every body's 4,096 readings are the lattice's directions to 3·10⁻¹⁶, any two bodies' to 6·10⁻¹⁶;
  P(v ≤ h) = 0.5012 and P(v ≤ h, v₂ ≤ h) = 0.3342 on every body (the lattice's own, the same for all).
- P2 not killed: three readers, directions only, place every point in |AB| to 1.0·10⁻¹³ of the mean radius, on all 200.
- P3: the recovered extents stand in the true ratios to 4·10⁻¹⁴ (not killed). The census's extents are 1 : 1 : 1 to
  4.5·10⁻⁵, the Fibonacci lattice's own lopsidedness, the same on every body; I checked that clause against 0.01, but
  the plan put P3's tolerance at 10⁻⁹, so **in its letter the census clause is killed by my set-up** (a finite lattice's
  extents are not exactly equal); what it was there to show, that the census is one sphere for every body and carries
  no stretch, holds to 6·10⁻¹⁶ between bodies (P1).
- P4 not killed: at k = 10⁻³, 7, 10³ the readings and the points in |AB| move by at most 1.0·10⁻¹³; with |AB| carried in,
  the body is the true one to 7.8·10⁻¹⁴ of its mean radius.
- P5 not killed: every point on every body is seen by all three readers (fewest 3).
- P6 not killed: the first 20 bodies, read by three readers in |AB|, differ pairwise by at least 0.26 of the mean
  radius; from the one reader they do not differ at all (P1).

The code run was the first version of `recover`; later edits that day changed only how the clouds are drawn
(`recoverShow`), not the numbers. The smoke test in reportbase/games checks bodies 0 and 7 the same way.

**Reading.** Draw's RCC and UDV hold in three dimensions on the Levels bodies: one reader's readings are the sweep's
own addresses, [h : v : v₂] the same for every body, so the census gives one sphere and nothing of the body, its
stretch included; three readers holding only directions and the shape of their own triangle give the body exactly,
up to the triangle's size; the length between two of them gives the size. Each reading is a direction of three unit
relations, two ratios, and two rays crossing in space fix a point, so three dimensions need no more readers than two
did (UDV used three; two seeing a point squarely suffice for that point).

## Run 2: many bodies at once (predictions, written before the code)

*17 October 2026. Tom, 18:34: "what if the reader was looking at many 3d objects at once?"; 19:01: "both", to Claude's
offer of a run (this) and a mode in `recover.html`. Geometry, plus one physical amount, the readers' resolution ε.*

**Known beforehand.** Draw's OCC lab ("find what is hidden"): a point of an outline is seen if the reader's ray meets
the outline there first; from outside a reader sees only part, and what is hidden from every standpoint stays hidden.
Draw's UDV and run 1 above: three readers' directions and their own triangle give every point up to size, one length the
size. wander: PXC (`plans/pxc-plan.md`), parallax's band and its far edge d ≈ B/ε, the depth error growing as d²;
`room-walk.html` (SPN R325): near, shape and place; farther, place without shape; farthest, direction alone. Classical:
a solid angle falls as the inverse square of distance; a ball seen from distance d shows the cap (1 − r/d)/2 of its
surface; stereo's depth error εd²/B. So nothing here is new geometry: the run puts these together on one field.

**The field.** Three readers at the corners of an equilateral triangle of side B = 1 (|AB|), its plane square to
(1, 1, 1), centred at O. M = 40 Levels bodies (`bodyOf(0 … 39)`, every band in full, as run 1), each centre in a direction
within 30° of (1, 1, 1) (inside the first octant: the field lies in one wedge) at a distance d from O, log-uniform on
[4, 16384] (12 doublings), seeded; 12 of the 40 are planted behind an earlier one, on the ray from O through its centre,
at 1.3 to 2 times its distance (at least far enough that their bounding balls do not meet). No two bounding balls meet.
Each body carries 1,024 surface points (the Fibonacci lattice of directions from its centre, as run 1). A reader sees a
point when the segment to it leaves every body's inside nowhere before it (64 steps a segment, the point's own end
excluded). Which point of which body a reading belongs to is given, as in run 1.

**The census** is a fourth standpoint at O sweeping 2²⁰ lattice directions; each is painted by the first body its ray
meets (ray marched against every body whose bounding ball it meets, then bisected), or by none. Every direction's
reading is its own, as in run 1; what the many bodies change is only the painting.

**Resolution.** Each reader reads a direction on a flat screen square to (1, 1, 1) at unit distance (a gnomonic grid,
the screens of all three alike), rounded to pixels ε wide in both screen coordinates; ε = 10⁻³ and 10⁻⁴ (B/ε = 1,000 and
10,000). A point is placed by least squares on the rays of every reader that sees it, if two of those rounded readings
differ; if all coincide it is a ray. Per body: the share of its seen points that are rays; its place error
e_p = |centroid of the placed points − centroid of the same true points| / d; its shape error
e_s = rms |(placed − its centroid) − (true − its centroid)| / R̄ (R̄ the body's mean radius).

### Predictions

- **P7 (one standpoint reads the sky, breadth over distance).** (a) The world scaled about O by k = 10⁻³, 7, 10³ paints
  the same census: every direction the same body, but for at most 10⁻⁴ of the directions (grazing rays, rounding).
  (b) One body moved from d to 2d along its ray and doubled in size about O paints the same census, to the same 10⁻⁴.
  (c) Body 0 alone on the ray (1, 1, 1) at d = 4·2^j, j = 0 … 11: its solid angle (a lattice of 20,000 directions over its
  bounding cap) times d² settles; Ω(d)/Ω(2d) is within 2% of 4 for d ≥ 64 and within 0.5% for d ≥ 512.
  (d) Each body alone, seen from O: the share of its 1,024 points seen is within 0.08 of (1 − R̄/d)/2.
  *Killed* if any part fails.
- **P8 (occlusion gives order, not depth).** (a) From O, "i hides j" (some ray meets i first, then j) has no cycle, and
  every pair whose centre distances differ by more than the sum of their bounding radii is ordered as its centres are
  (near an identity: a check of my code). (b) Scaling by k (P7a) changes no pair. (c) With ε = 10⁻³: every hiding pair
  with both bodies nearer than 100 is ordered the same way by the placed centroids' distances; and of the hiding pairs
  with the hider past 4B/ε, at least one is misordered by the placed centroids or has a body all rays, while occlusion
  still orders it. *Killed* if any part fails.
- **P9 (the bands are the resolution's).** At ε = 10⁻³: (a) every body nearer than 10 has e_s < 0.1 (shape), every body
  farther than 100 has e_s > 0.1; (b) every body nearer than 100 has e_p < 0.1 (place), every body farther than 4,000
  has e_p > 0.1 or is all rays; (c) no body nearer than 250 has a ray; over the bodies farther than 4B/ε the mean ray share
  is at least 0.3; (d) fitted over the bodies from d = 8 with e < 1, e_s grows as d^(2.0 ± 0.25) and e_p as
  d^(1.0 ± 0.25); (e) at ε = 10⁻⁴ the same fits give errors smaller by 10 within a factor 1.5 (the error ∝ ε).
  *Killed* if any part fails.
- **P10 (the geometry has no bands; one length writes the field).** At ε = 0 every seen point of every body, laid in
  |AB|, is the true point laid in |AB| to 10⁻⁹ of its distance from O, from d = 4 to 16,384; scaling the world by
  k = 10⁻³, 7, 10³ moves none; with |AB| carried in, every point is in the world's units to the same 10⁻⁹. *Killed* if
  any point misses.

P7(a, b), P8(a, b) and P10 are near identities (a kill would be my code); P7(c, d) and P9 are classical laws met on
these bodies, where a kill would be my estimate of the constants; P8(c) says what occlusion keeps that parallax loses.

**What would and would not be shown.** That from one standpoint many bodies are a painting of the sky, each patch its
breadth over its distance, ordered by what hides what and never sized; that three readers' directions place every body
in their own length and one length writes the whole field; and that the near, middle and far bands come from the
resolution, not from the geometry. Not how a reader finds which reading belongs to which body (the correspondence is
given), nor anything of light.

### Run 2 (17 Oct, `node rsh/rsh2.mjs` as first committed; output `rsh/rsh-run2.txt`, 2 min)

All four killed, most by my code:
- **P7** killed. (a) held: k = 10⁻³, 7, 10³ painted every one of the 2²⁰ directions alike. (b) by my code: the body
  "moved to 2d and doubled" was placed at 4d (`placed` scales the centre it is given). (c) held: Ω(d)/Ω(2d) within
  0.02% of 4 from d = 64 on (4.0013 at 128, 4.0031 at 256 at worst; 4.0000–4.0006 from 512). (d) by my code: a reader saw
  every point of a body farther than about 64, its far side included: 64 steps along a segment thousands long step clean
  over a body one across.
- **P8** killed. (a), (b) held (6 hiding pairs, all separated and ordered as their centres, no cycle, the same under k).
  (c) by my set-up: the census's 2²⁰ directions, 3.5·10⁻³ apart, meet no body past about 250, so no hiding pair past
  4,000 was found; and a near pair failed on a body that no two readers see (wholly hidden), which has no place to order.
- **P9** killed. (b) by my set-up, on the same wholly hidden body (no place to measure). (d), (e) by my set-up for the
  shape (the fit took in far bodies whose points all fell in one or two pixels, so their spread is lost and e_s sits
  near 1, under the cut) and **for real for the place**: e_p grew as d^1.40 and fell 25-fold for a tenfold ε. Post hoc:
  a resolved body's centroid averages its points' errors over the pixels it spans, about (2R̄/(dε))² of them, so its
  place error grows faster than d and falls faster than ε; a body inside one pixel averages nothing. The visibility
  fault (P7d) also counted far sides as seen, so every P9 number is suspect.
- **P10** killed by my code: least squares on the normal equations squares the conditioning (the rays from three readers
  1 apart at d ≈ 26,000 are 4·10⁻⁵ from parallel), 8·10⁻⁷ of the distance; and the |AB|-carried-in check compared a
  placed point with the wrong true one (an index over all points, not the seen ones).

## Run 3: the same field, the code fixed (predictions, written before the fixed code runs)

The fixes: the moved body placed at 2d (P7b); a point seen when no body's inside is met along the ray before it (the ray
marched in 256 steps through each bounding ball it crosses, then bisected; the same `enter` as the census), not 64 steps
of the whole segment (P7d, P8, P9); the least squares solved in the frame of the rays' mean direction, the small
eigenvalue taken from the rays' cross products, not from 1 − (u·m)² (P10); the true point matched by its own index
(P10). The field, its seed, ε and every threshold as run 2.

- **P7′** = P7, unchanged.
- **P8′** = P8 but (c): its near clause over the hiding pairs with both bodies placed (seen by two readers somewhere);
  its far clause over the planted pairs whose hider lies past 4B/ε, the hiding read on the ray from O through both
  centres (`enter` on each), since no census direction meets them.
- **P9′** = P9 (a)–(c) over the bodies with at least 100 points seen by two readers (a wholly hidden body has neither
  place nor shape); (d) its shape clause only, over the bodies resolved by at least ten pixels across (2R̄/d > 10ε), with
  the slope 2.0 ± 0.25; (e) its shape clause only, the same bodies at both ε, the ratio 10 within a factor 1.5. The
  place clauses of (d), (e) stand killed (run 2); no new prediction is made on them.
- **P10′** = P10, unchanged.

### Run 3 (17 Oct, `node rsh/rsh2.mjs`; output `rsh/rsh-run3.txt`, 2.5 min)

- **P7′ killed**, in (d) alone, and not by my code: each body seen alone from O shows 0.345 to 0.526 of its points, off
  (1 − R̄/d)/2 by up to 0.127 (body 36 at d = 49: 0.368 against 0.495). (a) every direction painted alike at k = 10⁻³, 7,
  10³; (b) body 12 moved to 2d and doubled about O: every direction alike; (c) as run 2. Post hoc
  (`rsh/rsh3-p7d.mjs`): with the relief taken off (the same stretched bodies, R(u) = ½) every share is within 0.008 of
  (1 − R̄/d)/2; so the relief's own shadows, and its points laid by direction from the centre rather than by area,
  move the share both ways by more than my 0.08 allowed. The cap law holds for the bodies' broad form only.
- **P8′ not killed.** (a), (b) as run 2. (c) the 3 near hiding pairs with both bodies placed are ordered by the placed
  centroids as by occlusion; the 5 planted pairs past 4B/ε are all hidden on the ray through their centres, and the
  placed centroids lose 4 of them (13 hides 31 and 17 hides 39: the hider all rays; in those two and in 20 hides 34
  and 38 the hidden body is seen by no two readers, hidden from them too), keeping one (19 at 947 before 33 at 1,073, both far short of their 4,288 and 5,636).
- **P9′ not killed**, over the 26 bodies seen by two readers at 100 points or more. (a) shape: e_s < 0.1 for all four
  nearer than 10 (0.009–0.024), above 0.1 for all past 100; (b) place: e_p < 0.1 for all nearer than 100 (at most
  6·10⁻⁴), above 0.1 or all rays past 4,000; (c) no ray nearer than 250 (the first at 1,124, 1.7% of its points), the
  mean ray share past 4,000 0.747 (8 bodies; 4 all rays); (d) e_s ∝ d^1.90 over the 5 bodies resolved by ten pixels or
  more; (e) e_s 10.09 times smaller at ε = 10⁻⁴ (12 bodies). Not predicted: over the same resolved bodies e_p ∝ d^0.14
  and falls 6.2-fold for a tenfold ε. Post hoc: a resolved body's points fall at every phase of the pixel, so their
  rounding nearly cancels in the centroid, which is placed far better than any one point until the body shrinks to a
  few pixels; past that e_p jumps to 0.24–0.88 (d 1,124–7,286) and then to all rays.
- **P10′ not killed:** at ε = 0 every seen point of every body in |AB| to 2.8·10⁻¹² of its distance, from d = 4 to
  25,945 (the conditioning, ~10⁻¹⁶·d/B); k = 10⁻³, 7, 10³ move none by more than 4.2·10⁻¹²; with |AB| carried in,
  3.5·10⁻¹² in world units.

Of the 40 bodies 14 are seen by two readers at fewer than 100 points, 11 at none (nine of the twelve planted, and two
behind nearer bodies), so occlusion, not resolution, is what hides most.

**Reading.** From one standpoint many bodies are a painting of the sky: each direction one body or none, unchanged by
scaling the world or by moving a body out along its ray at its size times as far, so each patch is breadth over
distance (its solid angle falls as 1/d² to 0.02% from d = 64); what hides what orders them, and that order never
sizes them. Three readers' directions place every body in their own length exactly at every distance (ε = 0), and
one length writes the whole field: the geometry has no bands. The bands are the resolution's: shape while a body's
points are told apart in depth (εd²/B against its radius, e_s ∝ d^1.9, ∝ ε), place well past that (a resolved body's
centroid averages its pixels away), and past B/ε rays, where the readers' pixels coincide; occlusion still orders
pairs out there that the placed centroids lose. Draw's OCC lab's lesson holds in three dimensions and among bodies:
from outside a reader sees part, and here most of what is lost is lost to other bodies, not to distance.

## Run 4: the inscribed reader among many bodies (predictions, written before the code)

*17 October 2026. Tom, 20:50: "tell me abou this demo with multiple objects, is it using cauchy inscribed reader?";
Claude: partly (directions only, one length) but not the Cauchy: the census covered a 34° cap and painted which body,
never laying the readings as addresses; the readers' pixels were a flat screen (a count against a ruler, not the turn);
the placement was parallax. Tom, 20:53: "yes, build the inscribed version".*

**Known beforehand.** WDG (`plans/wdg-plan.md`) and AZM (`plans/azm-plan.md`): directions uniform over the octant are
the Cauchy wedge, uniform in azimuth ψ (v₂/h = tan ψ) and in height (Archimedes, Lambert), every pair's corner at its
median, P(v ≤ h) = ½, the near field in both a third. PAM (`plans/pam-plan.md`): the addresses' median is at the corner
for every exchange-symmetric weight and moves toward a lopsided weight's heavier side. Theorem 6 (OFS): what arrives
never moves an address. Draw's SMP: a uniform turn's census is the Cauchy whatever the figure. Run 3 above: the flat
screen's bands.

**The inscribed reader.** One reader at home O sweeps the whole wedge (the first octant, h → x, v → y, v₂ → z)
uniformly: N addresses, a grid uniform in azimuth ψ ∈ [0, π/2] and in height y ∈ [0, 1] (Archimedes: equal area, so
equal shares of the sweep), 2¹¹ × 2¹¹ = 4,194,304 cells, each read at its middle. Each address is painted by the first
body its ray meets, or by none; the reading is the address itself, [h : v : v₂]. A body's share is its addresses over
N. Three readers (as run 3) read with **equal-angle pixels**: altitude a (tan a = v/√(h² + v₂²)) and azimuth ψ each
rounded to steps of ε radians (the two sweeps counted by their own turns), in place of run 3's flat screen. The field
is run 3's (the same seed), and a **mirrored field**: 20 bodies placed in the half of the 30° cone where v < h, each
with its mirror across v = h (x ↔ y, the body reflected too), no two bounding balls meeting.

### Predictions

- **P11 (a body's share is its solid angle).** For every body of run 3's field with at least 200 addresses, its share
  times π/2 equals its solid angle (run 3's cap lattice of 20,000 directions, the body alone, unhidden bodies only)
  within 2%; the shares and the sky add to 1 exactly; the world scaled by k = 10⁻³, 7, 10³ changes no address's body
  but for at most 10⁻⁴ of them. *Killed* if any part fails.
- **P12 (the addresses are the sweep's, whatever the bodies).** Over all N addresses P(v ≤ h) is within 0.002 of ½ and
  the near field in both (v ≤ h and v₂ ≤ h) within 0.002 of ⅓, for the empty wedge, run 3's field and the mirrored
  field alike (the addresses do not depend on what is met). Over the addresses the mirrored field paints, P(v ≤ h) is
  within 0.01 of ½ (an exchange-symmetric payload keeps its median at the corner). Over those run 3's field paints, the
  share with v ≤ h is reported, not predicted. *Killed* if any predicted part fails.
- **P13 (equal-angle pixels).** With ε = 10⁻³ and 10⁻⁴: run 3's P9′(a)–(c) hold again (shape below 10 and lost past 100;
  place below 100 and lost past 4,000 or all rays; no ray below 250, mean ray share past 4,000 at least 0.3); for every
  body with a shape error under 1 at both pixel kinds, e_s(equal-angle)/e_s(flat screen) lies in [0.4, 2.5], their
  geometric mean in [0.7, 1.4] (around (1, 1, 1) a flat-screen pixel and an equal-angle pixel differ by at most cos²35°
  in altitude and cos 35° in azimuth). *Killed* if any part fails.
- **P14 (no size in an address).** With equal-angle pixels the three readers' rounded readings are unchanged by scaling
  the world (k = 10⁻³, 7, 10³), but for at most 10⁻⁴ of them (rounding at a pixel's edge), and at ε = 0 every seen point is
  placed in |AB| to 10⁻⁹ of its distance. *Killed* if either fails.

P11, P12's first part and P14 are near identities (a kill would be my code); P12's second part is PAM's corner for a
symmetric payload met among bodies; P13 says the bands do not hang on the pixel's shape.

**What would and would not be shown.** That the inscribed reader's sweep is the same Cauchy wedge whatever bodies lie
in it, each body taking a share of its addresses equal to its solid angle (breadth over distance, no size), the median
at the corner moved only by a lopsided payload; and that its own pixels, equal turns, give the same bands as a flat
screen. Not how the correspondence is found, nor anything of light.
