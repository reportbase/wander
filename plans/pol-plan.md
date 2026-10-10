# POL: pool from inside, contact as the line h + v = 1

*Plan, predictions and kills written 10 October 2026, before `pool.html` or any script existed (Claude; Tom, after sharing
"Pool from Somewhere": "i think were this is most useful is in situations like this. each pool ball can explore its
situation"; "they lean heavily on unsituated math … Ours is most situated math, and could be all situated math"; "My
intuition is that we push the situated math further, and the further we push, we will learn something more about the
geometry of situated readers, which is our goal"). Exact geometry and a simulation of our own: this is evidence about the
geometry and about computation, not about the physical world. The lab rules hold: nothing above the "Runs" line is edited
after the run.*

## What was derived before writing this (disclosed)

Working out contact from inside, before this plan:
- Ball a sees ball b at a half-span α with sin α = r_b/d. Call it **v_ab**: how far b fills a's view, a pure number
  from 0 to 1.
- Ball b sees a with sin β = r_a/d. Call it **h_ab**.
- They touch when d = r_a + r_b, which is exactly **h + v = 1**: the straight line from A to B of `facing.html`.
- Two equal balls touch at **h = v = ½, the corner**, where each spans 60° of the other's view.
- Approaching, the pair's point (h, v) moves out along a ray from the origin. Its angle is fixed by the sizes,
  v/h = r_b/r_a. Distance is radial: h + v = (r_a + r_b)/d, so each halving of h + v is one level farther from contact.

P1 and P2 below are therefore identities. The run checks the implementation and floating point at the boundary, not the
geometry. P3–P5 are not identities.

## Keep the case

- r_a, r_b and d are amounts. Their ratios r/d are pure numbers: readings of how far one ball fills the other's view
  (sine of the half-span). Here h and v are those readings, from 0 to 1. Contact, h + v = 1, needs no unit and no bridge.
- **Velocities and impulses are amounts.** In the situated table each ball works in its own size: its unit is its own
  radius, its H. Another ball's size in a's units is r_a·(v/h). The other's motion is reported by the other in *its*
  own size per second and converted by the same ratio.
- **The masses' bridge is a known kind:** all balls are of one material, so m_b/m_a = (r_b/r_a)³ = (v/h)³.
- What stays unsituated in this first version, and is named as such:
  - the cushions and the pockets: a straight cushion has no size, so it has no such reading (below, "Open");
  - the cloth's slowing, which is each ball's own and situated, but applied by the referee's integrator;
  - the clock: one tick for all, with signals arriving at once (no delay in this version).

## The model

- **The referee.** The table of "Pool from Somewhere", unsituated: world positions and velocities, every pair checked
  by d < r_a + r_b, impulses along the line of centres (restitution 0.96, cushions 0.8, the cloth's slowing 0.6 per
  second, four substeps a frame). Fifteen balls and the white; one heavy ball of radius 0.6 against 0.45, of mass
  (0.6/0.45)³.
- **The situated table**, a second copy of the same rack, struck the same way. No ball reads a world position. At each
  substep each ball, for each other ball:
  - reads the other's direction (its address in the plane) and v = sin(half-span);
  - is told the other's reading of it, h. That is the only exchange: two readers each reading the other.
  - If h + v ≥ 1 and they are closing, it changes its own velocity:
    - the normal is the direction it reads;
    - the closing speed is in its own units, from its own motion and the other's reported motion (the other's
      own-units motion times v/h);
    - the impulse uses the mass ratio (v/h)³.

  It then moves itself by its own velocity.

## Predictions

- **P1 (contact is the line h + v = 1).** Over 10 racks, each broken from the head spot at a fixed set of 10 angles (the
  white struck at speed 14, toward the apex turned by −1.8° + 0.4°·i, i = 0…9) and run 8 s in frames of 1/60 s, at every substep and for every pair, the referee's d < r_a + r_b and h + v > 1 agree. *Killed* if any pair
  disagrees with |h + v − 1| > 1e-12.
- **P2 (equal balls touch at the corner; the heavy ball on its own ray).** Every referee contact between two balls of
  radius 0.45 has |h − v| < 1e-12, so it sits at the corner. Every contact with the heavy ball has v/h equal to 4/3 or
  3/4 within 1e-12. *Killed* if any contact misses.
- **P3 (one reading decides only under calibration).** With every ball the same size (the heavy ball made 0.45), a
  ball's own reading alone decides contact: v ≥ ½ if and only if touching. With the heavy ball present, v ≥ ½ alone
  mis-decides at least one pair-substep per rack. This is SPN's settled view, that under V = H amounts equal fill
  levels, and otherwise the other's reading is needed. *Killed* if the equal-size runs show any disagreement, or the
  heavy-ball runs show none.
- **P4 (the game from inside matches the referee, until chaos).** The situated table's positions match the referee's
  within 1e-9 through the first contact of every break, and within 1e-6 for the first 0.5 s. *Killed* if either fails.
  *Measured, not predicted:* the time at which they first differ by more than 1e-3. A break is chaotic, so rounding
  differences of the order of 1e-16 are expected to grow.
- **P5 (each ball's world is a few levels deep).** Counting a pair's level as log₂(1/(h + v)), levels from contact:
  - no pair of equal balls is ever more than log₂(table diagonal / 0.9) = 4.63 levels from contact;
  - at the rack, before the break, the median level over all pairs is between 1 and 3.

  *Killed* if either fails.

## Open, not in this version

- **Cushions.** A straight cushion fills half the view at any distance, so it gives no reading r/d, and one look cannot
  tell how far it is. A ball would have to read it through features of known kind (its ends, the pockets), or by its own
  motion (parallax). How a situated reader ranges an edge is the next question this raises.
- **Signal delay.** Each ball sees the others late by their distance, as "Pool from Somewhere" does for its reader.
  Contact read late is contact missed; how far ahead a ball must read, in levels, is the version after this one.
- **Level of detail.** Each ball attending closely only to pairs within k levels of contact, the rest rarely. This
  counts the work and the misses (POL run 2, with its own predictions).

## Runs

### Run 1 (10 October 2026)

`node plans/pol/pol.mjs` (through `pool.html`'s hook), output in `plans/pol/pol-run1.txt`:

```
4362840 pair-substeps over 20 breaks (10 with the heavy ball, 10 all equal); 376 contacts
P1: not killed. d < r_a + r_b against h + v > 1: 0 disagreements past 1e-12 (0 within 1e-12 of the line)
P2: not killed. contacts off the corner (equal) or off the ray 4/3 (heavy): 0
P3: not killed. one reading alone (v >= 1/2) against touching: all equal 0 wrong; with the heavy ball, per break 3169, 5905, 3564, 3537, 3551, 3562, 2010, 3647, 3512, 1720
P4: not killed. inside against the referee:
  break 0: first contact at 0.650 s, differ 1.73e-18 then; most in the first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  break 1: first contact at 0.650 s, differ 2.78e-17 then; most in the first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  break 2: first contact at 0.650 s, differ 2.78e-17 then; most in the first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  break 3: first contact at 0.650 s, differ 1.73e-18 then; most in the first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  break 4: first contact at 0.650 s, differ 0.00e+0 then; most in the first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  break 5: first contact at 0.650 s, differ 0.00e+0 then; most in the first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  break 6: first contact at 0.650 s, differ 1.73e-18 then; most in the first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  break 7: first contact at 0.650 s, differ 1.73e-18 then; most in the first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  break 8: first contact at 0.650 s, differ 2.78e-17 then; most in the first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  break 9: first contact at 0.650 s, differ 1.73e-18 then; most in the first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  all equal, break 0: differ 1.73e-18 at first contact; first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  all equal, break 1: differ 2.78e-17 at first contact; first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  all equal, break 2: differ 2.78e-17 at first contact; first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  all equal, break 3: differ 1.73e-18 at first contact; first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  all equal, break 4: differ 0.00e+0 at first contact; first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  all equal, break 5: differ 0.00e+0 at first contact; first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  all equal, break 6: differ 1.73e-18 at first contact; first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  all equal, break 7: differ 1.73e-18 at first contact; first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  all equal, break 8: differ 2.78e-17 at first contact; first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
  all equal, break 9: differ 1.73e-18 at first contact; first 0.5 s 0.00e+0; past 1e-3 at never (8 s)
P5: not killed. most levels from touching (equal balls) 4.459 (bound 4.63); rack medians 1.44, 1.44, 1.44, 1.44, 1.44, 1.44, 1.44, 1.44, 1.44, 1.44
```

- **P1 not killed.** Over 4.36 million pair-substeps, the referee's d < r_a + r_b and the two readings' h + v > 1 never
  disagree, not even within 1e-12 of the line.
- **P2 not killed.** All 376 contacts lie on the corner (equal balls) or on the heavy ball's ray, 4/3 or 3/4.
- **P3 not killed.** With all balls alike, a ball's own reading alone (v ≥ ½) decides contact without error. With the
  heavy ball, it mis-decides between 1,720 and 5,905 pair-substeps per break.
- **P4 not killed.** At the first contact (0.65 s in every break) the two tables differ by at most 3e-17, and by nothing
  in the first half second. *Measured:* they never came 1e-3 apart in 8 s, in any of the 20 breaks; the most seen on the
  page is of order 1e-14. The chaos the plan expected did not show: about 19 contacts a break, slowed by the cloth, did
  not amplify rounding that far.
- **P5 not killed.** The farthest two equal balls ever were 4.46 levels from touching (bound 4.63). The rack's median
  level is 1.44.

## Reading (after the run; not ruled)

- **Contact, read from inside, is the facing's straight line.** Each ball's reading of the other, sin of the half-span,
  is a pure number. The pair's two readings, h and v, add to (r_a + r_b)/d, so contact is h + v = 1, the line from A to
  B of `facing.html`. Equal balls touch at its middle, the corner. The geometry needs no unit and no coordinates.
- **A pair's sweep is a ray, and distance is levels along it.** The sizes fix the ray's angle (v/h = r_b/r_a), and
  approach moves the point out along it, one level for each halving of the gap's measure h + v. The pair's "facing" in
  this space is set by what the two are, and its "distance" by where they are.
- **One reader alone decides only under calibration.** A ball's own reading v ≥ ½ is contact exactly when every ball
  is its own size: SPN's V = H, under which amounts equal fill levels. With one ball of another size, a single reading
  errs thousands of times a break, and contact needs the other's reading: two parties for a relation.
- **The whole game can be played from inside.** Each ball, in its own size, with the size ratio v/h and one material
  for the masses, plays the same game as the view from nowhere, to rounding. In this simulation the separation is
  robust: no world coordinate is read for any contact.
- **What is still from nowhere** names the next questions. A straight cushion has no size, so no reading r/d. Signals
  arrive at once. And every ball reads every other at every substep, with no level of detail.
