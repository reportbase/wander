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

### Run 2 (10 October 2026): prediction, written before it ran (Tom: "proceed")

Run 1 left the cushions and pockets to the referee, since a straight cushion has no size and so no reading r/d. Worked
out before writing this:
- **A cushion is the reader's own flip.** Striking a cushion is the same as meeting one's own mirror image: an equal
  ball, moving mirrored, at twice the gap. (This is the method of images, known in physics.)
  - The image's reading of the ball is v = r/(2·gap), and the image reads the ball the same, so h = v.
  - Contact with the cushion is h + v = 1 at h = v = ½: the corner, with the reader as both parties.
  - The bounce is the ball-on-ball response with an equal mass, the image's motion mirrored, and the cushion's
    restitution 0.8.
- **A pocket is a place, not a party.** The ball is in it when the pocket fills its whole view, v = POCK/d ≥ 1 (with
  the referee's strict test, v > 1).
- **The world's side** supplies, as for balls, only the arriving image: the image's direction and v. No ball reads a
  coordinate. How a reflection reaches a ball (an echo, a mirror) is physics; the bridge is travel, and it arrives at
  once in this version.

The table now runs from inside entirely, except the integrator that moves each ball by its own velocity (each ball's
own act) and the one clock.

- **P6 (the cushion at the corner).** At every substep, for every ball and cushion, the referee's test (the centre
  closer to the cushion's line than r) and the image's h + v > 1 agree, and every cushion contact has h = v exactly.
  *Killed* on any disagreement past 1e-12.
- **P7 (the pocket fills the view).** The referee's d < POCK and v > 1 agree at every substep. *Killed* on any
  disagreement past 1e-12.
- **P8 (the whole game from inside).** With cushions and pockets read from inside as well, the table matches the
  referee within 1e-9 through each break's first cushion contact. *Killed* if not.

  *Measured, with an expectation stated:* whether the two ever differ by more than 1e-3 in 8 s. One difference in the
  rules is known beforehand. The referee reverses a ball's motion at a cushion whenever the ball is past the line,
  even if it is already moving away (as after a push from another ball); the image responds only when closing. I
  expect this to make at least one of the 20 breaks diverge. If any do, the cause is to be named from the run, not
  guessed.

Run 2 output (`node plans/pol/pol2.mjs`, in `plans/pol/pol-run2.txt`):

```
20 breaks, cushions and pockets read from inside: 2392224 cushion readings, 3588432 pocket readings
P6: not killed. cushion: centre within r of the line against the image's h + v > 1 (h = v): 0 disagreements
P7: not killed. pocket: d < POCK against v > 1: 0 disagreements
P8: not killed. the whole game from inside against the referee:
  heavy break 0: first cushion at 0.800 s, differ 8.95e-16 then; past 1e-3 at never (8 s); sunk 1 / 1
  heavy break 1: first cushion at 0.800 s, differ 2.22e-16 then; past 1e-3 at never (8 s); sunk 1 / 1
  heavy break 2: first cushion at 0.817 s, differ 4.44e-16 then; past 1e-3 at never (8 s); sunk 1 / 1
  heavy break 3: first cushion at 0.817 s, differ 1.78e-15 then; past 1e-3 at never (8 s); sunk 1 / 1
  heavy break 4: first cushion at 0.833 s, differ 2.02e-15 then; past 1e-3 at never (8 s); sunk 0 / 0
  heavy break 5: first cushion at 0.833 s, differ 2.02e-15 then; past 1e-3 at never (8 s); sunk 0 / 0
  heavy break 6: first cushion at 0.817 s, differ 2.22e-16 then; past 1e-3 at never (8 s); sunk 1 / 1
  heavy break 7: first cushion at 0.817 s, differ 4.44e-16 then; past 1e-3 at never (8 s); sunk 1 / 1
  heavy break 8: first cushion at 0.800 s, differ 8.88e-16 then; past 1e-3 at never (8 s); sunk 1 / 1
  heavy break 9: first cushion at 0.800 s, differ 8.95e-16 then; past 1e-3 at never (8 s); sunk 1 / 1
  equal break 0: first cushion at 0.800 s, differ 8.95e-16 then; past 1e-3 at never (8 s); sunk 1 / 1
  equal break 1: first cushion at 0.800 s, differ 2.22e-16 then; past 1e-3 at never (8 s); sunk 1 / 1
  equal break 2: first cushion at 0.817 s, differ 4.44e-16 then; past 1e-3 at never (8 s); sunk 1 / 1
  equal break 3: first cushion at 0.817 s, differ 1.78e-15 then; past 1e-3 at never (8 s); sunk 1 / 1
  equal break 4: first cushion at 0.833 s, differ 2.02e-15 then; past 1e-3 at never (8 s); sunk 0 / 0
  equal break 5: first cushion at 0.833 s, differ 2.02e-15 then; past 1e-3 at never (8 s); sunk 0 / 0
  equal break 6: first cushion at 0.817 s, differ 2.22e-16 then; past 1e-3 at never (8 s); sunk 1 / 1
  equal break 7: first cushion at 0.817 s, differ 4.44e-16 then; past 1e-3 at never (8 s); sunk 1 / 1
  equal break 8: first cushion at 0.800 s, differ 2.22e-16 then; past 1e-3 at never (8 s); sunk 1 / 1
  equal break 9: first cushion at 0.800 s, differ 8.95e-16 then; past 1e-3 at never (8 s); sunk 1 / 1
  diverged past 1e-3: 0 of 20
```

- **P6 not killed.** Over 2.39 million cushion readings, the referee's test and the mirror image's h + v > 1 never
  disagree. Every cushion contact is at h = v, the corner, with the ball as both parties.
- **P7 not killed.** Over 3.59 million pocket readings, d < POCK and v > 1 never disagree.
- **P8 not killed.** At each break's first cushion contact (0.80–0.83 s), the two tables differ by at most 2e-15.
  *The expectation was wrong.* No break came 1e-3 apart in 8 s. The known difference in the rules (the referee reversing
  a ball already moving away from a cushion) never came into play. Every break sank the same balls on both tables.

## Reading of run 2 (not ruled)

- **An edge is where a reader meets itself.** A straight cushion has no size, so no reading r/d. But striking it is
  meeting one's own mirror image, and that pair has a reading: v = r/(2·gap), the same both ways. So contact with an
  edge is the corner, h = v = ½, with the reader as both parties. Of the three kinds of thing on the table:
  - another ball is a pair on its own ray;
  - an edge is the pair of a reader and its flip, always at the corner;
  - a pocket is not a party at all. It is a place, entered when it fills the whole view, v = 1.
- **The table now runs from inside entirely,** except one integrator moving each ball by its own velocity, and one
  clock. Played so, it is the same game as the view from nowhere, to about 1e-15, over 20 breaks of 8 s. In this
  simulation, the unsituated description is not needed to play pool. It serves as a referee.
- **What is left names the next step: time.** Each ball should read the others late, by their distance, as "Pool from
  Somewhere" does for its reader, and each ball should keep its own clock. A contact read late is a contact missed:
  how far ahead a ball must read, in levels, is the question.

### Run 3 (10 October 2026): prediction, written before it ran (Tom: "yes, continue")

Time. Runs 1–2 let every reading arrive at once. Now each ball sees each other as it was when its image left, the
image travelling at a speed c: the **retarded** image, found from the other's past, where c·(t − t_e) equals the
distance then. Worked out before writing this:
- **Lateness is levelled like distance.** It is d/c, so it doubles with each level farther from contact.
- **The relative uncertainty is the same at every level.** In its lateness, a ball moving at speed u can move u·d/c, the
  fraction u/c of the distance, at any distance. So delay sets no preferred level, and its only number is u/c: the pair
  (own speed, signal speed), whose corner u = c is the light cone. Here u ≤ 14, so u/c ≤ 0.56 at the slowest c used.
- **Each ball now decides alone.** a reads b late and b reads a late, so the two may judge contact at different
  moments. The pair's size ratio, its ray v/h = r_b/r_a, is told once, at the rack, and never changes, so each ball has
  h = v·r_a/r_b from its own reading.

**Two readers:**
- *naive*: takes the late image as the other's place now;
- *carrying*: carries the late image forward by its own lateness (t − t_e), along the other's reported motion at the
  moment the image left (straight on, as if nothing touched it since).

Cushions stay as in run 2, read at once. That is a named simplification: one's own reflection is late by 2·gap/c.

**The measure:** for each break and c, E(c) is the largest distance between the two tables' balls 0.05 s after the
referee's first contact, the median over the ten heavy-ball breaks. It is taken at c = 25, 50, 100, 200 and 400, plus
c = 10⁹ as a check. The slope of log₂ E against log₂ c is fitted by least squares over the five finite values.

- **P9 (naive: one level of error per level of c).** The naive reader's slope is between −1.3 and −0.7. Its error is the
  closing speed times the lateness, (r_a + r_b)/c.
- **P10 (carrying helps).** At every c ≥ 50, the carrying reader's E is at most a quarter of the naive reader's.
  *Measured, not predicted:* the carrying reader's slope. Straight-line carrying misses only the cloth's slowing,
  ½·0.6·τ², which would give −2, but it is blind to touches inside the lateness, which give −1. Which one dominates is
  the question.
- **P11 (the check).** At c = 10⁹ both readers reproduce run 2: E < 1e-9.
- *Measured, not predicted:* the share of contacts where the two balls of a pair judged contact at different substeps,
  at each c. Action and reaction no longer at one moment.

Run 3 output (`node plans/pol/pol3.mjs`, in `plans/pol/pol-run3.txt`):

```
median over the ten heavy-ball breaks of E(c): the largest distance between the tables 0.05 s after the first contact
  c = 25    naive 4.014e-1   carrying 1.048e-1   one-sided contact judgements: naive 98.1%, carrying 67.8%
  c = 50    naive 3.350e-1   carrying 2.968e-2   one-sided contact judgements: naive 84.8%, carrying 33.1%
  c = 100   naive 3.536e-1   carrying 1.989e-2   one-sided contact judgements: naive 74.5%, carrying 10.8%
  c = 200   naive 3.645e-1   carrying 8.436e-5   one-sided contact judgements: naive 66.7%, carrying 3.2%
  c = 400   naive 9.975e-2   carrying 3.671e-5   one-sided contact judgements: naive 33.3%, carrying 0.0%
  c = 1000000000 naive 7.412e-9   carrying 1.346e-11   one-sided contact judgements: naive 0.0%, carrying 0.0%
P9: KILLED. naive slope of log2 E against log2 c: -0.390
P10: not killed. carrying at most a quarter of naive at c >= 50: 11.3x, 17.8x, 4321.4x, 2717.4x; carrying slope (measured) -3.142
P11: KILLED. at c = 1e9: naive 7.41e-9, carrying 1.35e-11
```

- **P9 killed.** The naive reader's error does not fall one level per level of c over 25–400. Its slope there is
  −0.39: E sits near 0.35 (about a ball's radius) from c = 25 to 200, then falls. Computed after the run, from c = 400
  to 10⁹, the slope is −1.1, as the mechanism said. So the mechanism holds only once the error is small. While it is
  large, the break plays out differently, and the error is the size of the game's own differences, not of the delay.
- **P10 not killed.** The carrying reader is 11×, 18×, 4,321× and 2,717× closer than the naive reader at c = 50, 100,
  200 and 400. *Measured:* its slope is −3.1, steeper than the −2 of the cloth alone, because its error collapses
  between c = 100 and 200.
- **P11 killed (my threshold).** At c = 10⁹ the carrying reader is 1.3e-11 off, but the naive reader is 7.4e-9 off,
  past the bar of 1e-9. That is its 1/c error at c = 10⁹ (2.5e-9 from the c = 400 value scaled), and the bar was set
  without working that out.
- *Measured:* one-sided contact judgements, where one ball of a pair judged contact and the other not at that
  substep. Naive: 98%, 85%, 75%, 67%, 33% at c = 25 to 400. Carrying: 68%, 33%, 11%, 3%, 0%. Late reading splits
  action from reaction; carrying the image forward rejoins them.

## Reading of run 3 (not ruled)

- **Lateness is a reading too, and it has its own corner.** Computed after the run, the lateness at the contact
  distance, (r_a + r_b)/c, is 8.6, 4.3, 2.2, 1.1 and 0.5 ticks of the table's clock at c = 25 to 400. The carrying
  reader's error collapses (2.0e-2 to 8.4e-5) between 2.2 and 1.1 ticks. That suggests the pair (lateness, the tick)
  has its corner at one tick: later than a tick, touches happen unseen within the lateness; earlier, nothing can
  happen unseen. This is post hoc and needs its own run: hold c and change the tick.
- **Carrying forward is the situated reader's remedy for time.** A late image carried along its own reported motion
  reads nearly as if at once. What it cannot carry is what happened inside the lateness: a touch it has not yet seen.
- **Delay sets no level of its own.** Its only number is u/c, the same at every distance. What gave the error a corner
  was not the distance but the clock: the reader's tick.

### Run 4 (10 October 2026): prediction, written before it ran (Tom: "proceed")

Run 3's reading, made after the run, was that the carrying reader's error collapses where its lateness at contact,
(r_a + r_b)/c, falls below about one tick of the clock. Here that is tested with the tick changed as well as c. Both
tables (the referee and the carrying reader) run with SUB substeps a frame, so one tick is 1/(60·SUB) s. The lateness
at contact for two equal balls is then L = 0.9·60·SUB/c ticks.

**The grid:** c ∈ {50, 100, 200, 400} × SUB ∈ {1, 2, 4, 8, 16}, the carrying reader only. E as in run 3 (the largest
distance between the tables 0.05 s after the referee's first contact), median over breaks 0, 4 and 9 with the heavy
ball. L runs from 0.135 to 17.3 ticks.

- **P12 (the corner of lateness and tick at about one tick).**
  - Every cell with L < 1.5 has E < 1e-3.
  - Every cell with L > 3 has E > 1e-2.
  - Cells with L between 1.5 and 3 are not predicted.

  *Killed* by any cell outside its band.
- **The alternative, named so a kill can be read.** If the error is set by the lateness alone (touches happening
  unseen within d/c, whatever the tick), then E depends on c and not on SUB. P12 would then fail along the rows: a fine
  tick (large SUB) at large c would still be small.

Run 4 output (`node plans/pol/pol4.mjs`, in `plans/pol/pol-run4.txt`):

```
carrying reader, E = largest distance between the tables 0.05 s after the first contact, median of breaks 0, 4, 9
L = lateness at contact in ticks = 0.9·60·SUB/c; predicted: E < 1e-3 when L < 1.5, E > 1e-2 when L > 3
  c  50  SUB  1  L   1.08  E 3.66e-4  (3.7e-4, 3.7e-4, 1.3e-3)  small
  c  50  SUB  2  L   2.16  E 1.19e-2  (1.2e-2, 1.2e-2, 5.4e-2)  -
  c  50  SUB  4  L   4.32  E 2.34e-2  (2.3e-2, 2.3e-2, 3.6e-2)  large
  c  50  SUB  8  L   8.64  E 2.28e-2  (2.0e-2, 2.3e-2, 2.3e-2)  large
  c  50  SUB 16  L  17.28  E 1.68e-2  (1.7e-2, 1.7e-2, 2.3e-2)  large
  c 100  SUB  1  L   0.54  E 1.23e-4  (1.2e-4, 1.2e-4, 1.1e-3)  small
  c 100  SUB  2  L   1.08  E 1.92e-4  (1.9e-4, 1.9e-4, 1.4e-3)  small
  c 100  SUB  4  L   2.16  E 1.53e-2  (1.5e-2, 1.5e-2, 3.2e-2)  -
  c 100  SUB  8  L   4.32  E 2.31e-2  (1.9e-2, 2.3e-2, 2.3e-2)  large
  c 100  SUB 16  L   8.64  E 1.62e-2  (1.6e-2, 1.6e-2, 2.2e-2)  large
  c 200  SUB  1  L   0.27  E 4.88e-5  (4.9e-5, 4.9e-5, 1.0e-3)  small
  c 200  SUB  2  L   0.54  E 8.18e-5  (8.2e-5, 8.2e-5, 2.3e-4)  small
  c 200  SUB  4  L   1.08  E 8.08e-5  (8.1e-5, 8.1e-5, 3.9e-4)  small
  c 200  SUB  8  L   2.16  E 1.36e-2  (1.4e-2, 1.4e-2, 1.4e-2)  -
  c 200  SUB 16  L   4.32  E 1.58e-2  (1.6e-2, 1.6e-2, 2.1e-2)  large
  c 400  SUB  1  L   0.14  E 2.31e-5  (2.3e-5, 2.3e-5, 6.3e-4)  small
  c 400  SUB  2  L   0.27  E 3.73e-5  (3.7e-5, 3.7e-5, 3.5e-4)  small
  c 400  SUB  4  L   0.54  E 3.73e-5  (3.1e-5, 3.7e-5, 3.7e-5)  small
  c 400  SUB  8  L   1.08  E 3.88e-5  (3.9e-5, 3.9e-5, 8.1e-4)  small
  c 400  SUB 16  L   2.16  E 1.44e-2  (1.4e-2, 1.4e-2, 1.4e-2)  -
check, run 3's cell c = 100, SUB = 4, break 4: E 3.167e-2
P12: not killed (0 cells outside their band)
```

- **P12 not killed.** All 11 cells with L < 1.5 ticks have E below 1e-3 (2.3e-5 to 3.7e-4). All 5 cells with L > 3 have
  E above 1e-2 (1.6e-2 to 2.3e-2). The four cells at L = 2.16, not predicted, sit at the plateau, 1.2e-2 to 1.5e-2.
- **The alternative is killed.** E follows L, the lateness in ticks, and not c. At c = 400, the fastest signals, the
  table with the finest tick (SUB = 16, L = 2.16) is 370× further off than the table with SUB = 8 (L = 1.08). At equal
  L, c from 50 to 400 changes little.
- The check: run 3's cell, c = 100, SUB = 4, break 4, gives 3.2e-2, one of the three values in its cell here.

## Reading of run 4 (not ruled)

- **The corner of time is the reader's own tick, not the signal's speed.** A reader whose images are older than one of
  its own ticks judges contact out of step with the other ball: each pushes and turns at a different tick, and the
  table settles on a plateau of error (about 2% of a ball's radius here) that no faster signal removes. Below one tick,
  both judge from the same past tick, and the error is the small carrying error, falling with the lateness.
- **A finer clock is not always better for a situated reader.** Refining the tick at a fixed signal speed moves the
  lateness past the corner and makes things worse. The tick and the lateness are a pair (amounts, in seconds), and
  their ratio is a reading like any other, with its corner at one.
- **So the table has three corners, each of a named pair:**
  - contact, h + v = 1, of the pair's two sizes against their distance;
  - the cushion, the corner h = v, of a ball and its own reflection;
  - time, at one tick, of the lateness against the reader's own tick.

### Run 5 (10 October 2026): prediction, written before it ran (Tom: "level of detail might be smaller and smaller pool balls. that where situated levels become interesting.")

Level of detail as size. A table of balls in size levels: level k has radius 0.45/2^k, k = 0 to 3. Worked out before
writing this:
- **Rays at dyadic angles.** A pair's ray is v/h = r_b/r_a, so between levels it is 2^(k_a − k_b). Contact,
  h + v = 1, falls nearer and nearer the larger ball's end of the line.
- **Size and distance trade one for one in levels.** a reads v = r_b/d. In levels, log₂ v = −(size levels between
  them) − (distance levels), plus a constant. So a ball one level smaller reads exactly as a ball of one's own size one
  level farther: SPN's "a thing's level is set by its size".
- **Attention is asymmetric, and so is the cost of ignoring.** Near contact, a ball k levels smaller fills little of
  the larger's view, while the larger fills most of its own. One material: the smaller's mass is 8^(−k) of the larger's
  (three levels of mass per level of size). If the larger ignores it, the larger misses a change of speed of that order;
  the smaller, still reading, bounces correctly.

**The field.** Seeded, five fields:
- 4 balls of level 0 (the white among them), 12 of level 1, 36 of level 2, 64 of level 3;
- placed at random, not overlapping, on the table's right three-quarters;
- the white on the head spot, struck at speed 14 toward the field's middle.

Run 2's physics throughout (cushions as one's own mirror image, signals at once).

**The rule.** A ball ignores, does not respond to, any ball K or more levels smaller than itself, for K = 1, 2, 3
and ∞. The smaller one still responds.

- **P13 (the field from inside, with no ignoring).** With K = ∞, the field played from inside equals the referee
  within 1e-9 at 1 s, in all five fields. *Killed* if any field misses.
- **P14 (the cost of ignoring falls three levels per level).** Let E_K be the largest position error of the level-0
  balls against the referee at 1 s, the median over the five fields. From K = 1 to 2 and from 2 to 3, E_K falls by a
  factor between 4 and 16 each step (the mass ratio 8 per level). *Killed* if either step's factor is outside [4, 16].
- *Measured, not predicted:* the share of contact responses skipped at each K; and E_K for every level, not only
  level 0.
