# SIT: the situations with V₂, organized by the relations

*14 October 2026 (Tom's local date). Tom, about 4:02: "we should expand the readers situations. to accomodate V2." Then,
to Claude's proposal (one entry per party, the old five as the one-party case), about 4:13: "i'm open to how to organize
the situations, or relations. we have three, h=[0,1], v=[0,1], v2=[0,1]. Each has a breadth, H, V, and V2. They are known
in the unsituated view, unknown in the unsituated view. unsituated view kickstarts the geomery by assigning V and V2 to
his choosen H. this creates a set of [h,v,v2]. which represents all possile ways those three relations can be
represented relative to each other. this set is created by the intersection of their three rays." Then, to Claude's
reading of the two places where "unsituated" stood for "situated", about 4:16: "yes, your correction is correct. I mixed
the to up." SPN R239. Exact arithmetic (mpmath at 50 digits); predictions written before the script (`runs/sit/sit.py`)
exists.*

## Set-up, with the case kept

**The relations.** n + 1 unit relations h, v, v₂, …, each in [0, 1], each with its breadth H, V, V₂, …. Known breadths
are the unsituated view; unknown, the situated view. The situated reader chooses H and draws every other party at it,
V = V₂ = H, which gives the set of every [h, v, v₂], the unit cube of relations: its directions the wedge (one facing
of every freedom), its sum cut h + v + v₂ = 1 the triangle where the truth lies (R236, R238).

**The three rays** (Claude's reading of "the intersection of their three rays", not confirmed by Tom beyond the two
corrections): put the parties at the triangle's corners, A = (1, 0, 0), B = (0, 1, 0), C = (0, 0, 1), and ask where rays
from them meet with every pair at a right angle, as the flip paired the two rays of R235.

**The vantages of a hemisphere.** A reader taking a hemisphere of directions in at once (both sweeps parallel) reads its
area against its shadow on the base; one taking it one direction at a time reads the shadow against the area (the mean
height over it). In two unit relations these were π/2 and 2/π (OFS §3.4).

**Classical theory leaned on:** the right angle on a chord (Thales, *Elements* III.31) and the trirectangular corner of
solid geometry; the surface of a hemisphere is twice its base (Archimedes, *On the Sphere and Cylinder* I.33: a sphere's surface is four of its great circles), with
the hat-box theorem; the volume of the n-ball and the area of the n-sphere.

## Predictions

- **P1. Three rays meet square only at the reader.** The points P with (P − A)·(P − B) = (P − B)·(P − C) =
  (P − C)·(P − A) = 0 are exactly two: the reader's home (0, 0, 0) and its mirror across the triangle, (⅔, ⅔, ⅔). With
  n + 1 parties at the unit points, the same conditions give only t·(1, …, 1) with t = 0 or 2/(n + 1). With two parties
  (one condition) they give a whole circle, x² + y² = x + y, the circle on the chord from (1, 0) to (0, 1), which passes
  through home: the two-party reader is one point of an arc of possible standpoints, the three-party reader is pinned.
  **Killed if**, solving the conditions by Newton's method from 2,000 random starts in [−2, 3]ⁿ⁺¹ for n + 1 = 3, 4, 5,
  any converged root (residual below 1e-40) lies farther than 1e-30 from both predicted points; or either predicted point
  leaves a residual above 1e-45; or, for two parties, any of 500 points of the predicted circle leaves a residual above
  1e-45.
- **P2. The hemisphere's two readings.** For the hemisphere of the sphere in n dimensions (n − 1 sweeps), the reading
  taken at once, area over shadow, is √π·Γ((n + 1)/2)/Γ(n/2), and the reading taken one direction at a time, the mean of
  cos θ over the hemisphere by area, is its reciprocal; their product is 1. For n = 2, 3, 4: π/2, 2 and 3π/4, against
  2/π, ½ and 4/(3π). For n = 3 the 2 is Archimedes' "twice its base", and the ½ is the hat-box theorem (the height is even
  over the sphere, so its mean is ½). **Killed if**, computing the area and the shadow by numerical integration over the
  hemisphere (not from the Γ form) for n = 2, 3, 4, either reading differs from the closed form by more than 1e-40, or the
  product from 1 by more than 1e-40.
- **P3. The readings do not multiply sweep by sweep.** The three-relation hemisphere's 2 is not (π/2)² = 2.467, and its
  ½ is not (2/π)² = 0.405. **Killed if** either equality holds to within 0.1. (A guard against reading the two sweeps of
  a three-party reader as two independent two-party readers; how a mixed reader, one sweep at once and the other one
  direction at a time, reads a hemisphere is left open until it is defined.)

## What the run would and would not show

P1 and P2 are classical; the run checks the statements made of them here. The organization of the situations (one
entry per party, the old five the one-party case) is a choice of exposition, not a result, and is not tested.

## Runs

### Run 1 (14 October; `python3 runs/sit/sit.py`, about 75 s)

```
P1: not killed. 3 parties: 2000 of 2000 starts converged, all within 0.0 of t = 0 or 2/3; 4 parties: 2000 of 2000 starts converged, all within 1.2e-641 of t = 0 or 2/4; 5 parties: 2000 of 2000 starts converged, all within 6.7e-52 of t = 0 or 2/5; two parties: the circle on the chord, through home, to 5.3e-51
P2: not killed. n = 2: at once 1.570796327, one at a time 0.6366197724 (closed form to 2.7e-51); n = 3: at once 2.0, one at a time 0.5 (closed form to 0.0); n = 4: at once 2.35619449, one at a time 0.4244131816 (closed form to 0.0)
P3: KILLED. 2 against (π/2)² = 2.4674, off 0.4674; ½ against (2/π)² = 0.405285, off 0.09472
```

P1 and P2 not killed. **P3 killed by my set-up**: its kill condition, "either equality holds to within 0.1", was wider
than the gap I had written beside it on the inner side, ½ against (2/π)² = 0.405, 0.095 apart. Nothing about the
geometry; the threshold was mine. (A first draft of the script also tested a different condition from the plan's; it
was replaced by the plan's condition before the run.)

### Run 2 (prediction written before `runs/sit/sit2.py` exists)

- **P3′. The hemisphere's readings are the per-sweep products times a fixed factor, 8/π², and its reciprocal.** The
  reading at once, 2, is (π/2)² × 8/π², and the reading one direction at a time, ½, is (2/π)² × π²/8; 8/π² = 0.8106,
  so neither factor is 1, and the two sweeps of a three-party reader do not read as two independent two-party readers.
  **Killed if**, at 50 digits, either ratio differs from 8/π² or π²/8 by more than 1e-45, or 8/π² lies within 0.05 of 1.

```
P3': not killed. at once 2.0 = (π/2)² × 0.8105694691; one at a time 0.5 = (2/π)² × 1.23370055; 8/π² = 0.8105694691 (to 0.0)
```

**What it shows.** Rays from three parties at the unit points meet with every pair square only at the reader's home
and its mirror across the truth's triangle; with more parties the same, at t = 0 and 2/(n + 1); with two, on a whole
circle through home. So a three-party reader stands where the parties' rays meet square: its standpoint is fixed by
them, and from there every [h, v, v₂] is laid out. A hemisphere taken at once reads 2 (Archimedes: twice its base), one
direction at a time ½ (the hat-box theorem), product 1; in general √π·Γ((n + 1)/2)/Γ(n/2) and its reciprocal. These are
not the two-party readings squared: they differ from (π/2)² and (2/π)² by 8/π² and π²/8. How a mixed reader (one sweep at
once, the other one direction at a time) reads is left until it is defined.
