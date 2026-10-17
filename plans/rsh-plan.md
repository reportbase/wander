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
