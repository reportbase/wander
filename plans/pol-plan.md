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

Run 5 output (`node plans/pol/pol5.mjs`, in `plans/pol/pol-run5.txt`):

```
fields of 116 balls (levels 0-3: 4, 12, 36, 64), white struck at 14; errors against the referee at 1 s
  K = inf  E by level (median of 5): 2.12e-13, 1.80e-10, 6.23e-11, sunk differs   contact responses skipped 0 of 492 (0.0%)
         per field, level 0: 2.12e-13, 1.28e-1, 6.00e-12, 3.83e-14, 3.08e-14
  K = 1    E by level (median of 5): 2.32e+0, 2.06e+0, 8.53e+0, sunk differs   contact responses skipped 225 of 616 (36.5%)
         per field, level 0: 2.32e+0, 5.07e+0, 3.22e+0, 2.08e+0, 6.09e-1
  K = 2    E by level (median of 5): 6.09e-1, 1.56e+0, 1.44e+1, sunk differs   contact responses skipped 102 of 588 (17.3%)
         per field, level 0: 2.17e-1, 1.95e-1, 1.15e+0, 8.22e-1, 6.09e-1
  K = 3    E by level (median of 5): 1.44e-1, 1.29e+0, sunk differs, sunk differs   contact responses skipped 37 of 518 (7.1%)
         per field, level 0: 1.09e-1, 1.27e-1, 1.00e+0, 2.38e-1, 1.44e-1
P13: KILLED. K = inf against the referee: all levels within 1e-9 in all five fields
P14: KILLED. level-0 error falls by 3.81 (K 1 to 2) and 4.23 (K 2 to 3); band [4, 16]
```

- **P13 killed.** With nothing ignored, four of the five fields match the referee within 1e-9 at 1 s, but field 2 does
  not: its level-0 balls are 0.13 apart, and in every field some of the smallest balls fall into different pockets
  ("sunk differs"). The rack of 16 never diverged in 8 s (runs 1–2). A field of 116 balls in four size levels
  amplifies differences of rounding (about 1e-17 a contact) to the size of a ball within a second.
- **P14 killed.** The level-0 balls' error at 1 s falls by 3.81 from K = 1 to 2, and by 4.23 from K = 2 to 3: about 4
  per level, not the predicted 4 to 16 band's middle, and the first step just under its floor.
- *Measured:*
  - contact responses skipped: 36.5% at K = 1, 17.3% at K = 2, 7.1% at K = 3;
  - the smaller levels' errors are of the size of the table (2 to 14), with balls sunk differently.

## Reading of run 5 (not ruled)

- **Many levels make the table chaotic, and that bounds "the same game".** With four size levels, the view from
  inside and the view from nowhere agree only up to a horizon of about a second in one field of five. Past it, both
  are one rounding each of a chaotic game, and neither is more correct. This is not a failure of the situated view:
  it is the point past which no reader, situated or not, carries a game forward exactly.
- **Ignoring smaller balls costs about 4× less per level, but chaos is in the measure.** Each skipped response is
  exactly the mass ratio 8^(−k) of the larger ball's motion (that is an identity). What the run measures is that cost
  spread through a chaotic game, and the 4 may belong to the chaos rather than to the levels. A clean test measures
  before the chaos horizon, or per contact, with its own prediction.
- **Ignoring is worth a lot of work.** A larger ball that ignores everything one level or more smaller skips more
  than a third of all contact responses, and the smaller balls still bounce off it correctly.

**A bug found in run 5, after it ran.** On the page, the field's readout showed NaN. The cause: a small, fast ball can
cross a cushion's line within one tick, and the image's reading for a gap ≤ 0 was set to infinity. That turned the
response's arithmetic into NaN, and such balls left the table's arithmetic altogether. Run 5's numbers for the situated
table may therefore be partly the bug's. Run 5 stays recorded as it came out, kills and all, but it is not evidence.
The fix keeps the reading signed: v = r/(2·gap) is negative once the edge is behind, which still counts as contact, and
the push comes out exactly r − gap, as the referee's clamp. Runs 1 and 2 reproduce unchanged with the fix (their
output re-run, identical).

### Run 6 (10 October 2026): prediction, written before it ran

Run 5 again with the bug fixed, the same field, seeds and measure. The predictions are run 5's, unchanged:
- **P13′.** With K = ∞, the field from inside equals the referee within 1e-9 at 1 s in all five fields.
- **P14′.** The level-0 error falls by a factor between 4 and 16 from K = 1 to 2, and from K = 2 to 3.

Run 5's outcome (P13 killed by field 2 and by balls sunk differently) is known now, so P13′ is not blind. It is kept
as it was, not loosened.

Run 6 output (`node plans/pol/pol5.mjs`, in `plans/pol/pol-run6.txt`):

```
fields of 116 balls (levels 0-3: 4, 12, 36, 64), white struck at 14; errors against the referee at 1 s
  K = inf  E by level (median of 5): 2.12e-13, 2.15e-13, 6.23e-11, 1.10e-9   contact responses skipped 0 of 530 (0.0%)
         per field, level 0: 2.12e-13, 2.59e-10, 6.00e-12, 3.83e-14, 3.08e-14
  K = 1    E by level (median of 5): 2.32e+0, 2.06e+0, 8.53e+0, sunk differs   contact responses skipped 250 of 684 (36.5%)
         per field, level 0: 2.32e+0, 5.07e+0, 3.22e+0, 2.08e+0, 6.09e-1
  K = 2    E by level (median of 5): 6.09e-1, 1.56e+0, 1.44e+1, sunk differs   contact responses skipped 103 of 612 (16.8%)
         per field, level 0: 2.17e-1, 1.95e-1, 1.15e+0, 8.22e-1, 6.09e-1
  K = 3    E by level (median of 5): 1.44e-1, 7.95e-1, 5.98e+0, 8.86e+0   contact responses skipped 38 of 576 (6.6%)
         per field, level 0: 1.09e-1, 1.27e-1, 1.00e+0, 2.38e-1, 1.44e-1
P13: KILLED. K = inf against the referee: all levels within 1e-9 in all five fields
P14: KILLED. level-0 error falls by 3.81 (K 1 to 2) and 4.23 (K 2 to 3); band [4, 16]
```

- **P13′ killed, narrowly.** With the bug fixed and nothing ignored, the field from inside matches the referee to
  2e-13 (level 0), 2e-13 (level 1) and 6e-11 (level 2) at 1 s, median over the fields. The smallest balls' median is
  1.1e-9, just past the bar of 1e-9, and no ball sinks differently. Run 5's large divergence was the bug, not the
  field's chaos. Rounding grows a little among the smallest balls, but not to the size of a ball in a second.
- **P14′ killed.** The level-0 error falls by 3.81 and 4.23 per step of K, exactly as in run 5 (the bug never touched
  the large balls): about 4 per level, under the band's floor of 4 for the first step.
- *Measured:* responses skipped are 36.5% at K = 1, 16.8% at K = 2 and 6.6% at K = 3. By level difference, that is
  147 skipped at one level, 65 at two and 38 at three or more.

## Reading of runs 5–6 (not ruled)

- **The field from inside is still the referee's game.** With four size levels and 116 balls, the table played from
  inside agrees with the view from nowhere to about 1e-9 at 1 s, once the cushion's reading is kept signed. "The edge
  is behind me" is a reading too, negative.
- **Ignoring smaller balls costs about two levels per level of size, not three.** Each skipped response is the mass
  ratio, 8 per level, of the larger ball's motion: that is an identity. The game-level error at 1 s falls only about
  4 per level. The skipped contacts become fewer per level of difference (147, 65, 38), so their number does not
  explain the shortfall. Why the cost is a square and not a cube of the size is open. It needs its own run, measured
  per contact and over time, with a prediction.
- **Situated levels pay in work.** A ball that ignores everything one level smaller skips over a third of all contact
  responses, while the smaller balls still bounce off it.
- **The field has a chaos horizon of about two seconds** (measured after run 6, `runField` with nothing ignored, the
  largest error over all balls at 0.5, 1, 1.5, 2 and 3 s, seeds 1–5):

  ```
  1.0e-14 1.4e-11 9.3e-8 6.8e-3 4.5e+0
  7.4e-13 2.4e-9  1.8e-7 4.5e-4 (sunk differs)
  1.5e-14 5.4e-9  5.2e-4 4.8e+0 (sunk differs)
  7.2e-14 1.1e-9  2.3e-4 9.1e+0 (sunk differs)
  1.1e-14 1.2e-10 1.9e-6 1.8e-3 3.1e+0
  ```

  The difference grows about a hundredfold each half second, from rounding to the size of the table by 3 s. The rack
  of 16 never diverged in 8 s. Many small balls make the game chaotic. Past its horizon, the view from inside and the
  view from nowhere are each one rounding of the same chaotic game.

### Run 7 (10 October 2026): prediction, written before it ran (Tom: "yes", to measuring the cost of ignoring per contact)

Runs 5–6 left open why ignoring smaller balls costs about 4× less per level of size (3.81, 4.23), not the mass ratio's 8.
The game's error at 1 s mixes three things: what one ignored contact costs, how many there are, and how the chaos of the
field grows each one. This run takes them apart. It measures in the true game (K = ∞, nothing ignored, run 6's fields and
seeds), at every contact a level-0 ball has with a ball j levels smaller, the response that ignoring would skip.

Keep the case. The readings h, v are fill levels; the skipped change of speed, the closing speed and the times are amounts.
The bridge from readings to masses is run 1's: one material, m_b/m_a = (v/h)³ = 8^(−j).

**Worked out before writing this.** For one contact, the larger ball's change of speed is
Δu = (1 + e)·w·m/(M + m) = (1 + e)·w/(1 + 8^j), with w the closing speed along the line of centres and e = 0.96. At a
fixed closing speed this falls by 65/9 = 7.22 from j = 1 to 2, and 513/65 = 7.89 from j = 2 to 3: the "8" of P14. So a 4
per level must come from the closing speed w growing as the balls get smaller, or from the number of contacts, or from
the chaos.

**The mechanism predicted: lighter balls are kicked faster.** A ball struck by a larger one leaves at up to
(1 + e)·M/(M + m) of the striker's speed, about 1.74 to 1.96 times it. Smaller balls, struck in a cascade down the
levels, therefore move faster and close faster on the level-0 balls. So the momentum a smaller ball carries, not its mass
alone, sets what ignoring it costs.

- **P15 (one contact, an identity).** Through the hook's `respond`, a level-0 ball met head-on by a ball j levels smaller
  at closing speed 1 changes speed by (1 + e)/(1 + 8^j). The ratios from j = 1 to 2 and from 2 to 3 are 7.22 and 7.89,
  within 1e-9. *Killed* if either misses. This checks the code, not the idea.
- **P16 (smaller balls close faster).** Over 3 s of the true game, five fields, the median closing speed w at level-0
  contacts with level-j balls rises by a factor between 1.4 and 2.5 from j = 1 to 2, and again from j = 2 to 3.
  *Killed* if either step is outside the band. *Undecided*, not passed, if any j has fewer than 10 contacts.
- **P17 (so one contact costs about 4 per level).** The median skipped change of speed per contact, |Δu|, falls by a
  factor between 3.2 and 5.7 from j = 1 to 2, and again from 2 to 3 (8 over P16's band). *Killed* if either step is
  outside. A fall near 7–8 would mean the closing speed does not depend on size, and the 4 lies elsewhere.
- **P18 (the game's 4 is the summed impulse, before chaos).** For each level-0 ball, the drift that ignoring would leave
  by 1 s if nothing else changed is D = |Σ Δu·(1 − t_c)|, summed over its contacts before 1 s with balls K or more levels
  smaller (t_c the contact's time; the cloth's slowing ignored). Take the largest over the level-0 balls and the median
  over the fields, as E_K in run 6. The ratios D₁/D₂ and D₂/D₃ are within a factor 1.5 of run 6's 3.81 and 4.23, that
  is in [2.54, 5.72] and [2.82, 6.35]. *Killed* if either is outside. If not killed, the 4 per level is the first-order
  cost of the skipped contacts, not the chaos's.
- *Measured, not predicted:* the number of level-0 contacts with each level; D_K against run 6's E_K (the chaos's gain).

Run 7 output (`node plans/pol/pol7.mjs`, in `plans/pol/pol-run7.txt`):

```
P15, one contact, closing speed 1, the larger ball at rest:
  j = 1: |du| = 2.178e-1  (1+e)/(1+8^j) = 2.178e-1
  j = 2: |du| = 3.015e-2  (1+e)/(1+8^j) = 3.015e-2
  j = 3: |du| = 3.821e-3  (1+e)/(1+8^j) = 3.821e-3
P15: not killed. ratios 7.222222222222 (65/9 = 7.222222222222), 7.892307692308 (513/65 = 7.892307692308)

level-0 contacts with smaller balls, true game (nothing ignored), five fields, 3 s:
  j = 1:   17 contacts (7 before 1 s); median closing speed 5.163, median |du| 1.124e+0, du/w 2.178e-1
  j = 2:   69 contacts (20 before 1 s); median closing speed 5.978, median |du| 1.802e-1, du/w 3.015e-2
  j = 3:  138 contacts (39 before 1 s); median closing speed 9.381, median |du| 3.584e-2, du/w 3.821e-3
P16: KILLED. closing speed rises by 1.16 (j 1 to 2) and 1.57 (j 2 to 3); band [1.4, 2.5]
P17: KILLED. per-contact |du| falls by 6.24 (j 1 to 2) and 5.03 (j 2 to 3); band [3.2, 5.7]

first-order drift by 1 s (median of the five fields' largest): D1 1.867e+0, D2 5.044e-1, D3 7.489e-2
  run 6's E at 1 s: 2.32, 0.609, 0.144; the chaos's gain E/D: 1.24, 1.21, 1.92
P18: KILLED. D falls by 3.70 (K 1 to 2; band [2.54, 5.72]) and 6.74 (K 2 to 3; band [2.82, 6.35])
```

- **P15 not killed.** One contact skips (1 + e)/(1 + 8^j) of the closing speed, and the ratios are 65/9 and 513/65 to
  twelve digits. The code does what the identity says.
- **P16 killed.** Smaller balls do close faster on the level-0 balls, but by 1.16 from j = 1 to 2 and 1.57 from 2 to 3,
  not the 1.4 to 2.5 of a cascade. The first step is under the band.
- **P17 killed.** One skipped contact costs 6.24 times less from j = 1 to 2 (outside the band) and 5.03 times less from
  2 to 3 (inside it). The faster closing takes the 7.2 and 7.9 down only part of the way to 4.
- **P18 killed, narrowly.** The first-order drift D falls by 3.70 from K = 1 to 2, within the band and close to run 6's
  3.81. From K = 2 to 3 it falls by 6.74, just past the band's 6.35, where the game's error fell by 4.23.
- *Measured:*
  - level-0 contacts with balls j levels smaller: 17, 69 and 138 over 3 s (7, 20 and 39 before 1 s). The smaller balls
    are many more, so there are more such contacts per level;
  - the chaos's gain at 1 s, E/D: 1.24, 1.21 and 1.92. At K = 1 and 2 the game's error is mostly the first-order drift
    itself; at K = 3 the chaos about doubles it.

## Reading of run 7 (not ruled)

- **The 8 is real, per contact, at a given closing speed.** The skipped change of speed is exactly the mass ratio's
  share of the closing speed (P15). Nothing about the situated reading changes that.
- **Three things bring it down toward 4, none alone.** Smaller balls close a little faster, so one contact costs
  about 5 to 6 times less per level, not 8. There are more of them, so the costs add up over more contacts. And at
  K = 3, where the drift is smallest, the field's chaos doubles it. From K = 1 to 2 the first two account for the
  game's 3.81 (D gives 3.70). From K = 2 to 3 they give 6.74, and the chaos brings it to 4.23.
- **So the "4" is not a law of the levels.** It is this field's mix: its counts per level (3, 12, 36, 64 balls), the
  speeds the break gives them, and its chaos horizon. A field with as many balls in each level should have fewer small
  contacts and a cost per level nearer the per-contact 5 to 6 (untested; it would need its own run). What stays general is the identity (8 per level at a fixed
  closing speed) and the decomposition: cost = per-contact share × closing speed × count, then the chaos's gain.
- **For a situated reader:** what it may ignore is set by the momentum the smaller things bring, not by their size
  alone. A small thing moving fast costs as much to ignore as a larger one moving slowly. Level of detail by size alone
  is right only where the smaller things are no faster.

### Run 8 (10 October 2026): prediction, written before it ran (Tom: "yes", to a prediction horizon for the trick-shot game)

`play-trick.html` previews a whole shot, but a player aims with some error, and every contact makes the outcome more
sensitive to the aim. This run measures, contact by contact, how many levels of aim precision a contact costs. The answer
sets how far ahead a situated player can see: the preview's level of detail, counted in contacts. The engine is the
game's (`play-trick.html`, its `simulate` through the hook): pool.html's table from inside, cloth slowing 1.2. Evidence
about the geometry and the computation, not the world.

Keep the case. s (the run from a ball's start to its contact), r (the radius) and the angles are amounts. The pair's
reading h + v = 2r/|SO|, from the striking ball's start S to the object's centre O, is a fill level. No bridge is needed:
the result is a ratio of angles.

**Worked out before writing this (and a correction).** In conversation I said a contact costs about log₂(2d/r) levels,
3 to 5 here. Derived properly it is smaller.
- The object ball leaves along the line of centres at contact, whatever the restitution: it is not reflected. Its
  direction is the ghost ball's (the striker at contact) direction to its centre, on a circle of radius 2r.
- Turn the striker's line by δψ about its start S. The object's offset from the line changes by (s + 2r·cos φ)·δψ, so
  the cut changes by that over 2r·cos φ. The object's direction is the line's angle plus the cut, so it turns by
  **A = s/(2r·cos φ)** times δψ (in magnitude; the +1 of the line's own turn cancels).
- Read from S, with h + v = 2r/|SO| and α the small angle between the line and SO:
  A = cos α/((h + v)·cos φ) − 1. For a full hit, **A = 2^L − 1, where L = log₂(1/(h + v)) is how many levels the pair
  starts from contact** (run 1's P5 count). The aim error grows by about as many levels as the run spanned.
- A ball struck from rest starts with no error in its place, only in its direction, so in a chain where each ball meets
  the next from rest, the factors multiply exactly, to first order: the chain loses Σ log₂ A_k levels.
- On this table, with s from 1 to 6 and 2r = 0.9, a full hit loses about 0.2 to 2.7 levels; a thin cut (cos φ small)
  loses more; a run shorter than 2r·cos φ gains (A < 1).

The engine detects contact a substep late, with the balls overlapping by up to a substep's travel (about 0.06 at speed
14, 7% of 2r). That moves the effective ghost ball and the cut a little, so the predictions allow 15%.

**The chains.** Seeded, 60 chains: the white and three object balls, each struck from rest by the one before, runs s
drawn from 1.2 to 5, cuts from −45° to 45°, power 20, nothing else on the table. A chain is used only if its first three
contacts are exactly white–1, 1–2, 2–3, in that order, and all four balls stay on the table. Each is run twice, the second
with the aim turned by δ = 1e-7 rad (and once by 1e-8, to check the response is linear). A ball's direction is read from
its frames between its start and its next contact.

- **P19 (one contact).** For at least 90% of the contacts, the measured factor |e_k/e_(k−1)| is within 15% of
  s_k/(2r·cos φ_k), from the chain's planned geometry (e_0 = δ, e_k the direction error of ball k). *Killed* if fewer.
- **P20 (the chain).** For at least 90% of the chains, the levels lost over the chain, log₂(e_3/δ), equal Σ log₂ A_k
  within 0.3 levels. *Killed* if fewer.
- **P21 (linear).** The factors at δ = 1e-8 equal those at 1e-7 within 1% for at least 95% of contacts. *Killed* if fewer.
- *Measured, not predicted:* levels lost per contact in the game's own layouts (the rack, scattered), and the depth in
  contacts at which an aim error of 0.1° grows past 3.6° (half a pocket's width seen from 8 units away): the horizon the
  preview's fade will use.

Run 8 output (`node plans/pol/pol8.mjs`, in `plans/pol/pol-run8.txt`):

```
60 chains (white and three, each struck from rest by the one before), power 20, aim turned by 1e-7 and 1e-8
  one contact: measured/predicted factor, median 0.9278, 5%–95% 0.208–1.324; within 15%: 92 of 180
  the chain: levels lost minus predicted, median -0.499, largest 10.162; within 0.3 levels: 19 of 60
P19: KILLED. 92 of 180 contacts within 15% of s/(2r cos φ) (90% needed)
P20: KILLED. 19 of 60 chains within 0.3 levels of the sum (90% needed)
P21: not killed. 180 of 180 factors the same at 1e-8 within 1% (95% needed)

measured, the game's layouts (scattered ×12, rack ×6, random aims, power 14): levels of aim error at each ball's first contact, by depth
  depth 1:  30 balls, median 3.32 levels
  depth 2:  40 balls, median 2.37 levels
  depth 3:  32 balls, median 1.54 levels
  depth 4:  33 balls, median -3.60 levels
  depth 5:  28 balls, median -9.64 levels
  a 0.1° aim error passes 3.6° (5.17 levels) at depth > the deepest measured
```

- **P19 killed.** Only 92 of 180 contacts are within 15% of s/(2r·cos φ). The measured factor is 0.93 of it at the median,
  but spreads from 0.21 to 1.32 (5% to 95%).
- **P20 killed.** Only 19 of 60 chains are within 0.3 levels of the sum; the median chain loses half a level less than
  predicted, the worst ten levels less.
- **P21 not killed.** Every factor is the same at δ = 1e-8 as at 1e-7, within 1%: the response is linear. The kills are
  not noise.
- *Measured:* in the game's own layouts, a ball's aim error at its first contact falls with depth after depth 3 (3.3, 2.4,
  1.5, then −3.6 and −9.6 levels at depths 4 and 5). Deep balls are mostly the rack's, struck from a few hundredths away,
  where s < 2r·cos φ and a contact gains levels (A < 1). The 3.6° horizon was not reached in five contacts.

## Reading of run 8 (not ruled)

- **The engine is not the geometry at thin cuts.** Checked after the run (`plans/pol/pol8-posthoc.mjs`, output in
  `pol-run8-posthoc.txt`): at near-full hits (|φ| < 15°) the measured factor is 1.03 of s/(2r·cos φ) at the median; at
  thin cuts (|φ| > 30°) 0.67, about cos²φ. The engine finds contact at a fixed tick, with the balls already overlapping
  (by 0.034 at the median, up to 0.077, against 2r = 0.9). The struck ball leaves along the line of centres *as found*,
  with the striker a fixed distance down its line. Turning the aim then turns that line by D·cos φ/ρ (ρ the overlapped
  distance between centres), not s/(2r·cos φ): a factor cos²φ less. This accounts for the median and for the thin cuts.
  It is not the whole story: only 67 of 180 contacts match D·cos φ/ρ within 1% (111 within 15%).
- **So the game's thin cuts are off by up to a few degrees at full power.** The preview and the shot agree (one engine),
  but a ½-ball hit at power 20 can leave a degree or more from where exact contact sends it. The fixed tick also makes
  the game less chaotic than the geometry at thin cuts.
- **The fix is the situated one.** Find the moment the pair's reading is exactly h + v = 1 (each ball can, in its own
  units, from the other's direction, its reading and its told motion), respond there, and carry on. That is a new run,
  with its own predictions.

### Run 9 (10 October 2026): prediction, written before it ran

Run 8 again, after making the game's contact exact, in the situated way. When a pair's reading has passed h + v = 1
within a tick, each ball works out, in its own units, how long ago the reading was exactly 1. It uses only what it has:
the other's direction n and the pair's readings h and v (the other's place relative to it, n/h, in its own radii), and
the other's told motion converted by v/h. It solves |n/h − w·τ| = 1 + v/h for τ ≥ 0 (w the relative motion), takes the
line of centres at that moment, responds along it, and corrects its own place by its change of motion times τ (it has
moved with the new motion since then). A cushion likewise: its image's reading was exactly ½ a time τ = (r − gap)/(its
speed toward the cushion) ago. Run 8's chains, seeds and measure are kept, and `play-trick.html` is changed only there.

Worked out before writing this: with contact exact, each struck ball leaves from rest along the true line of centres, so
a chain follows its planned geometry to rounding, and the first-order factor is exactly s/(2r·cos φ).

- **P22 (one contact).** At least 95% of the 180 contacts are within 2% of s/(2r·cos φ). *Killed* if fewer.
- **P23 (the chain).** At least 95% of the 60 chains lose Σ log₂ A_k levels within 0.05. *Killed* if fewer.
- **P24 (contact on the line).** At every corrected contact the pair's reading is h + v = 1 within 1e-9. *Killed* if
  any is not.
- *Kept from the game's checks:* the row of four still pots the 4, and the rack's first contact is still a full-ball hit.
- *Measured, not predicted:* in the game's layouts, levels lost by depth, and the depth at which a 0.1° aim error passes
  3.6°: the horizon for the preview's fade.

Run 9 output (`node plans/pol/pol9.mjs`, in `plans/pol/pol-run9.txt`; the measured part split by layout before recording):

```
60 chains (white and three, each struck from rest by the one before), power 20, aim turned by 1e-7 and 1e-8
  one contact: measured/predicted factor, median 1.0000, 5%–95% 1.000–1.000; within 2%: 180 of 180
  the chain: levels lost minus predicted, median 0.000, largest 0.000; within 0.05 levels: 60 of 60
P22: not killed. 180 of 180 contacts within 2% of s/(2r cos φ) (95% needed)
P23: not killed. 60 of 60 chains within 0.05 levels of the sum (95% needed)
P24: not killed. 209 contacts in the layouts, 0 set down overlapping (the old push); the rest on h + v = 1 to 2.2e-16
  (linear, as run 8's P21: 180 of 180 factors the same at 1e-8 within 1%; the row of four pots 4; the rack's first contact full-ball: true)

measured, the game's layouts (scattered ×12, rack ×6, random aims, power 14): levels of aim error at each ball's first contact, by depth
  scatter:
    depth 1:  26 balls, median 3.06 levels
    depth 2:  24 balls, median 4.62 levels
    depth 3:  18 balls, median 6.81 levels
    depth 4:  10 balls, median 8.60 levels
    depth 5:   4 balls, median 8.35 levels
    depth 6:   1 balls, median 12.52 levels
    a 0.1° aim error passes 3.6° (5.17 levels) at depth 3
  rack:
    depth 1:   6 balls, median 3.35 levels
    depth 2:  12 balls, median 1.13 levels
    depth 3:  16 balls, median -6.94 levels
    depth 4:  21 balls, median -8.43 levels
    depth 5:  25 balls, median -15.09 levels
    depth 6:   2 balls, median -17.89 levels
    a 0.1° aim error passes 3.6° (5.17 levels) at depth > the deepest measured
```

- **P22 not killed.** All 180 contacts give s/(2r·cos φ) to four figures (5% to 95%: 1.000 to 1.000).
- **P23 not killed.** All 60 chains lose Σ log₂ A_k levels to three decimals.
- **P24 not killed.** Every contact in the layouts is on h + v = 1 to 2.2e-16; none was set down overlapping.
- The game's own checks hold: the row of four pots the 4, the rack's first contact is a full-ball hit.
- *Measured:*
  - open table (scattered): a ball's aim error grows about 1.5 to 2 levels a contact (3.1, 4.6, 6.8, 8.6 levels at
    depths 1 to 4). A 0.1° aim error passes 3.6° at depth 3.
  - the rack: past the first two contacts, errors shrink (to −7 and −15 levels at depths 3 and 5). Balls in a cluster
    are struck from a few hundredths away, where s ≪ 2r·cos φ and A ≪ 1.

## Reading of run 9 (not ruled)

- **A contact costs as many levels as the run before it spanned.** With contact exact, the sensitivity is the geometry's,
  s/(2r·cos φ), to rounding; for a full hit 2^L − 1, L the levels the pair started from contact (h + v read from the
  striker's start). Each contact turns the levels a pair was apart into levels of aim lost.
- **So a situated player sees about three contacts deep on an open table**, with a tenth of a degree to spare at the
  aim and a half-pocket at the end. Past that the outcome is not theirs to see. That is the preview's horizon.
- **Clusters forgive.** Inside a rack the runs are shorter than the balls, and a contact gains levels: the cradle passes
  the hit along and forgets the aim. The break's chaos comes from the open table after it, not from the rack itself.
- **The fixed tick hid this.** Run 8's engine was cos²φ less sensitive at thin cuts. Finding the moment h + v = 1,
  each ball in its own units, makes the game's physics the geometry's.

### Run 10 (11 October 2026): prediction, written before it ran (Tom: "proceed", to level of detail by time to contact)

Run 7 found that what a larger ball may ignore is set by the momentum a smaller one brings, not by its size alone. This
run asks whether a ball can choose what to ignore from its own readings by that momentum, and whether that beats choosing
by size for the same work saved.

**Worked out before writing this (keep the case).** a reads b at v = r_b/d and is told b's reading of it, h = r_a/d.
- The size ratio is the reading v/h = r_b/r_a: one material, so b's share of the pair's mass is
  ρ³/(1 + ρ³), with ρ = v/h (run 1's bridge, a known kind).
- **The looming rate is a reading too.** As b nears, v grows: v̇/v = −ḋ/d. Its inverse, τ = v/v̇, is Lee's time to
  contact (the time until d would reach 0 at the present closing speed), an amount in seconds on the one clock (the
  tick, unsituated and named since run 2). a needs no distance and no speed to read it, only two looks at v.
- **So is the kick.** The closing speed in a's own radii per second is −ḋ/r_a = (v̇/v)·(d/r_a) = 1/(h·τ). The change of
  speed a would make (run 7, P15) is therefore, in a's own radii per second,

  kick = (1 + e) · ρ³/(1 + ρ³) · 1/(h·τ).

  Everything in it is a reading (v, h, and v's rate) and the one material. Size alone keeps only the factor ρ³/(1 + ρ³).
  τ alone keeps only the factor 1/τ. The kick keeps both.
- No ball may ignore its equal or a larger ball: an equal ball's kick is half the closing speed, and two equals each
  ignoring the other would pass through each other. So every rule here ignores only a ball read as smaller, v < h.

**The rules.** Run 6's five fields, seeds and measure (116 balls in four size levels, the white struck at 14, the level-0
balls' largest position error against the referee at 1 s, median over the fields). Each ball decides for itself, at
each contact response, from its own readings:
- **S(K), size:** ignore a ball read K or more levels smaller, v/h ≤ 2^(−K) (run 6's rule; K = 2, 3).
- **M(ε), the kick:** ignore a smaller ball when its kick, read as above from two looks, is below ε (in the reader's own
  radii per second).
- **T(τ\*), time alone:** ignore a smaller ball when its τ, read from two looks, is above τ\*.

The looming rate is read from the reader's last two looks at v, one tick apart: v̇ ≈ (v_now − v_then)/tick.

**Work matched.** At K = 1, S already ignores every smaller ball, so there is nothing for M or T to choose differently;
the comparison is at K = 2 and 3. For each K, ε and τ\* are set (by bisection, the same value in all five fields) so that
M and T skip as many contact responses in total over the five fields as S(K), within 2% or 2 responses,
whichever is larger. If no value gets that close, the comparison at that K is *undecided*, not passed.

- **P25 (the kick is read from two looks).** In the true game (nothing ignored), at the contact responses of a ball to a
  smaller one, the kick read from v, h and two looks is within 10% of the response it would skip, at 90% or more of them.
  *Killed* if fewer. The 10% allows for the tick: near contact the pair's distance curves within a tick when the pass is
  oblique, about 6% at the field's speeds (u·tick/d ≈ 10 × 1/240 / 0.7), and a contact just after another sees the old
  approach.
- **P26 (the kick beats size).** At K = 2 and at K = 3, with the work matched, the level-0 error under M is lower than
  under S(K) by a factor of at least 1.5. *Killed* if either factor is below 1.5. Reasoning: S skips every contact with a
  far smaller ball, fast and head-on ones too; M skips the smallest kicks wherever they are, glancing and slow ones of
  nearer sizes included, so the summed skipped kick, run 7's first-order cost, should be well below S's.
- **P27 (time alone is not enough).** At K = 2 and 3, with the work matched, the level-0 error under T is higher than under
  M. *Killed* if T's is lower or equal at either. Reasoning: run 7's per-contact cost falls by 5 to 6 per level of size
  but its closing speed only 1.2 to 1.6; the share, which τ leaves out, is most of the cost.
- *Measured, not predicted:* T against S; the summed skipped kick of the level-0 balls by 1 s for each rule (the
  first-order cost); how many of M's skips are of balls 1, 2 and 3 levels smaller.

Run 10 output (`node plans/pol/pol10.mjs`, in `plans/pol/pol-run10.txt`):

```
P25: the kick read from v, h and two looks over the response it would skip, 199 responses to smaller balls, five fields, 1 s, nothing ignored
  ratio: median 0.9194, 5% 0.5739, 95% 1.1792; within 10%: 101 of 199 (50.8%)
P25: KILLED. within 10% at 50.8% of responses (90% needed)

fields of 116 balls, white struck at 14; level-0 error against the referee at 1 s (median of five); skips are contact responses, total over the five fields
K = 1
  S(1), size             skipped  250 of  684   E level 0 2.32e+0  (all levels 2.32e+0, 2.06e+0, 8.53e+0, sunk differs)   level-0 skipped kick 5.71e+0   skips by levels smaller 1/2/3: 135/62/53
    per field, level 0: S 2.32e+0, 5.07e+0, 3.22e+0, 2.08e+0, 6.09e-1
K = 2
  S(2), size             skipped  103 of  612   E level 0 6.09e-1  (all levels 6.09e-1, 1.56e+0, 1.44e+1, sunk differs)   level-0 skipped kick 1.46e+0   skips by levels smaller 1/2/3: 0/58/45
  M(ε = 2.01), kick      skipped  102 of  606   E level 0 6.09e-1  (all levels 6.09e-1, 1.69e+0, 1.44e+1, sunk differs)   level-0 skipped kick 2.10e+0   skips by levels smaller 1/2/3: 5/51/46
  T(τ* = 0.0317 s), τ    skipped  103 of  622   E level 0 2.10e+0  (all levels 2.10e+0, 2.32e+0, sunk differs, sunk differs)   level-0 skipped kick 4.61e+0   skips by levels smaller 1/2/3: 26/38/39
    per field, level 0: S 2.17e-1, 1.95e-1, 1.15e+0, 8.22e-1, 6.09e-1
                        M 2.17e-1, 1.95e-1, 1.15e+0, 8.22e-1, 6.09e-1
                        T 2.10e+0, 4.09e+0, 3.25e+0, 2.07e+0, 5.14e-1
K = 3
  S(3), size             skipped   38 of  576   E level 0 1.44e-1  (all levels 1.44e-1, 7.95e-1, 5.98e+0, 8.86e+0)   level-0 skipped kick 3.60e-1   skips by levels smaller 1/2/3: 0/0/38
  M(ε = 0.191), kick     skipped   38 of  576   E level 0 1.44e-1  (all levels 1.44e-1, 7.95e-1, 5.98e+0, 8.86e+0)   level-0 skipped kick 3.34e-1   skips by levels smaller 1/2/3: 1/0/37
  T(τ* = 0.0712 s), τ    skipped   38 of  536   E level 0 1.40e-1  (all levels 1.40e-1, 5.65e-1, 1.87e+0, 3.90e+0)   level-0 skipped kick 6.23e-1   skips by levels smaller 1/2/3: 18/9/11
    per field, level 0: S 1.09e-1, 1.27e-1, 1.00e+0, 2.38e-1, 1.44e-1
                        M 1.09e-1, 1.27e-1, 9.90e-1, 2.38e-1, 1.44e-1
                        T 5.60e-1, 1.09e-1, 2.83e+0, 1.40e-1, 2.89e-2
P26 at K = 2: KILLED. S/M level-0 error 1.00 (at least 1.5)
P27 at K = 2: not killed. T 2.10e+0 against M 6.09e-1 (T higher)
P26 at K = 3: KILLED. S/M level-0 error 1.00 (at least 1.5)
P27 at K = 3: KILLED. T 1.40e-1 against M 1.44e-1 (T higher)
```

- **S reproduces run 6 exactly** (250, 103 and 38 responses skipped; level-0 errors 2.32, 0.609, 0.144, field by field).
  The rule hook changes nothing when the rule is size.
- **P25 killed.** The kick read from v, h and two looks is within 10% of the response at 50.8% of the 199 responses to
  smaller balls (median ratio 0.92, 5% to 95%: 0.57 to 1.18), not the 90% predicted.
- **P26 killed at both K.** With the work matched (102 against 103, 38 against 38), the kick rule's level-0 error equals
  size's: the factor is 1.00 at K = 2 and at K = 3. The kick rule skipped almost the same contacts: by levels smaller
  1/2/3, 5/51/46 against size's 0/58/45 at K = 2, and 1/0/37 against 0/0/38 at K = 3. Field by field the level-0 errors
  are the same to three figures (one field at K = 3: 0.990 against 1.00).
- **P27 not killed at K = 2, killed at K = 3.** At K = 2, τ alone leaves 3.4 times the error (2.10 against 0.609). At
  K = 3 its median is a little lower (0.140 against 0.144), and its fields scatter widely (0.029 to 2.83, against the kick
  rule's 0.109 to 0.990).
- *Measured:*
  - τ alone against size: 3.4 times worse at K = 2, the same at K = 3 (0.140 against 0.144).
  - The level-0 balls' summed skipped kick (median of the fields): at K = 2 size 1.46, the kick rule 2.10, τ alone 4.61;
    at K = 3 0.360, 0.334 and 0.623. A skipped response repeats while a pair stays overlapping, so this overcounts for
    every rule alike.
  - τ alone skips across the levels (26/38/39 at K = 2, 18/9/11 at K = 3): it ignores slow balls of nearer size.

**After the run (post hoc, not a test): why P25 failed.** `node plans/pol/pol10-posthoc.mjs`, in
`plans/pol/pol-run10-posthoc.txt`:

```
the kick read from two looks over the response, five fields, 1 s, nothing ignored (post hoc)
  run 10 rate, (v1 − v0)/(tick·v1)   n 199  median 0.9194  5% 0.5739  95% 1.1792  within 10% 50.8%
  log rate, ln(v1/v0)/tick           n 199  median 0.9690  5% 0.7491  95% 1.2610  within 10% 69.3%
    log rate, near head-on (cos > 0.9) n  65  median 0.9320  5% 0.7253  95% 0.9827  within 10% 60.0%
    log rate, oblique (cos ≤ 0.9)    n 134  median 0.9900  5% 0.8575  95% 1.3545  within 10% 73.9%
```

The rate in run 10 divided the change by the newer reading, (v_now − v_then)/(tick·v_now). That reads low by about
u·tick/d, the share of the distance closed in one tick: 7% at u = 10 and d = 0.6, more for the white's fast hits. A
difference of logs, ln(v_now/v_then)/tick, halves the bias (median 0.97, 69% within 10%). What is left is the tick itself:
near head-on, fast pairs still read 7% low, because one tick is about a tenth of their τ (τ ≈ d/u ≈ 0.04 s, the tick
1/240 s). Oblique passes scatter high, up to +35%, as P25's reasoning allowed. Neither was predicted, so P25 stays killed.

## Reading of run 10 (not ruled)

- **In this field, size already reads the kick.** The share falls by exactly ρ³/(1 + ρ³), about 8 per level. Closing
  speeds rise only 1.2 to 1.6 per level (run 7), and their spread within a level rarely bridges the 8: the kick rule
  swapped only 5 of 103 skips across a level. So ordering contacts by the kick is nearly ordering them by size. Matched in work, the two rules chose the same contacts and played the same game. Run 7's
  principle stands (what one may ignore is the momentum it brings), but where the levels span far more than the speeds,
  a ball's level alone is a sufficient reading of it. That supports SPN's "a thing's level is set by its size" as a rule
  of attention, here. A field where small balls are much faster than their level suggests would tell the rules apart.
  That is untested.
- **Time alone is the wrong reading.** τ says when, not how much. Ignoring by it skips slow balls of nearer size, whose
  share is large: 3.4 times the error at K = 2. At K = 3 the two are a draw inside the field's chaos.
- **Reading τ needs looks closer together than τ.** Two looks one tick apart read the fast pairs' kick several percent
  low, because the tick is a tenth of their time to contact. Time has a grain, as space does: run 4 found the same for
  lateness, which mattered once it passed about one tick. A reader that ranges by looming must look more often than its
  nearest τ.

### Run 11 (11 October 2026): prediction, written before it ran (Tom: "we could scale it up to infinite number of balls, but then zoom in to just see a small percentage of them, and only have to draw or calcualate the visible balls"; "yes")

Can a reader hold a world of any size and compute only what it can see? Runs 5–7 and 10 found that a reader may ignore
balls far below its own size, and that a ball's level alone tells it which. Distance trades one for one with size in
levels (run 5), so the same rule says: hold far balls as totals, not as balls. This run builds that and tests it against
a referee that computes every ball.

**The system (keep the case).** To keep a world alive without a driver we would have to choose, the table loses
nothing: no cloth, no cushions, and contacts perfectly elastic (e = 1). The balls are then a gas of hard discs, whose
equal-time statistics kinetic theory gives. The amounts: radius r = 0.45, area fraction φ = 0.15 (so the number density
is n = φ/(πr²) = 0.2358 balls per unit area), each velocity component spread with σ = 5 units a second, mass 1, tick
1/240 s. Contact is read from inside as before: each ball reads the other's v = r/d and is told h = r/d; equal balls touch
at h = v = ½, the corner, found exactly within the tick (run 9's method).

**The multiscale world.** The world is cut into world-fixed cells in dyadic levels: level 0 cells are 7.5 units wide,
level k cells 7.5·2^k. Around the reader:
- **The window:** a block of 6 × 6 level-0 cells (45 × 45 units) holds balls, one by one.
- **The view:** the middle 30 × 30 units of the window, leaving a margin of 7.5 units, about three mean free paths
  (λ = ⟨|u|⟩/ν = 2.58 units at the rates below).
- **Everything else is totals:** each other cell holds its count, momentum and kinetic energy, and nothing else. A cell is
  kept whole at the level where it reads at the corner from the reader, size/distance ≤ 1, and split while it reads
  larger. So the number of cells grows with the log of the world's size, one ring of cells per level.
- **The exchange:** a ball whose centre leaves the window is folded into the cell it enters (its count, momentum and
  energy added there). Balls enter the window from each neighbouring level-0 cell at that cell's one-way flux across a
  line, n·σ/√(2π) per unit length per second (exact for any fluid in equilibrium, since velocities do not depend on
  positions there). An entering ball is placed on the window's edge, moving in, with the flux's velocities (inward
  speed Rayleigh in σ, along the edge normal in σ, plus the cell's mean motion). Its count, momentum and energy are taken
  from the cell. If the place is occupied, another place along the edge is tried (a named approximation: entering
  balls avoid crowded spots of the edge; the margin is there to keep that from the view).
- **The cells among themselves:** neighbouring cells exchange count, momentum and energy by diffusion with the gas's
  kinetic coefficient D = λ⟨|u|⟩/2. This is a chosen model of the far field. It is not tested here: this run keeps the
  world in equilibrium.
- **Moving the reader** (panning or zooming) folds the window's cells that leave it into totals, and unfolds the cells
  that enter it into balls: as many balls as the cell holds, placed at random without overlap, seeded by the cell's
  place, with velocities from its σ shifted and scaled so that the balls carry exactly its momentum and energy. A
  fraction of a ball left over stays with a neighbouring cell's totals.

**The referee** computes every ball in a world of side L = 240 (32 × 32 level-0 cells, 13,581 balls), wrapped round at
its edges so that it has no edge at all. Every run starts from a referee state warmed up for 3 s (about seven contacts
a ball) from random placement. The multiscale world starts from the same state: the window's balls copied, everything
outside summed into cells. Measures are taken every 0.05 s for 60 s: in the referee, in each of the 64 views of
30 × 30 that tile its world; in the multiscale world, in its one view. Runs: 4 warmed states, 10 reader places each.

**Worked out before writing this (kinetic theory of hard discs).**
- **Contacts per ball per second** (Enskog, with Henderson's contact value of the pair distribution for discs,
  g = (1 − 7φ/16)/(1 − φ)² = 1.2933): ν = n·(2r)·σ·√π·g = 2.432.
- **Speeds:** Rayleigh in σ.
- **The count in a view fluctuates** with variance over mean equal to S(0) = 1/(∂(βp)/∂n) for a large open region,
  from Henderson's equation of state βp/n = (1 + φ²/8)/(1 − φ)². At φ = 0.15, S(0) = 0.530. A 30 × 30 square adds about
  +0.015 at its edge (the excluded discs near it), and the finite world takes off its share (1 − 900/57,600). So
  var/mean ≈ 0.54.
- **A closed window keeps its own count**, so its view's count fluctuates less: by the share of the window the view is
  not, 1 − 900/2025 = 0.56, so about 0.30.

**The control.** The same multiscale windows, closed: a ball reaching the window's edge is turned back (a mirror), and
nothing enters or leaves.

- **P28 (the books balance).** Over every 60 s run, and over a pan of ten window widths and back, the world's totals
  (the window's balls plus every cell) stay: the count within 1e-6, the momentum within 1e-6, the energy within 1e-9 of
  itself. *Killed* if any run misses. This checks the folding and unfolding, not the idea.
- **P29 (the engine is a gas of hard discs).** In the referee:
  - contacts per ball per second within 5% of 2.432;
  - the speeds' largest gap from Rayleigh (with σ read from the state's energy, σ² = E/N) below 0.01;
  - the view count's var/mean in [0.49, 0.61].

  *Killed* if any misses.
- **P30 (the view sees the same gas).** Averaged over the 40 multiscale runs, the view's density, its kinetic energy per
  ball and its contacts per ball per second are each within 3% of the referee's. *Killed* if any is not.
- **P31 (open, not closed).** The multiscale view's count var/mean is within 15% of the referee's, and the closed
  control's is at least 25% lower than the referee's. *Killed* if either fails.
- **P32 (the work is set by the view).** The multiscale world's work per simulated second (balls moved, pairs looked at,
  balls entering tried, cells updated) changes by less than 5% when the world grows from L = 240 to L = 3,840: 256 times
  the balls, four more levels of cells. *Killed* if it changes by 5% or more.
- *Measured, not predicted:*
  - the referee's work from L = 240 to 480;
  - the density across the window, from its edge inward: how far the entering balls' placement reaches;
  - the level-0 cells next to the window: how far their density drifts;
  - the view with no margin (a view as big as the window);
  - the view's density and energy just after a pan, when its balls have just been unfolded.

Run 11 output (`node plans/pol/pol11.mjs`, in `plans/pol/pol-run11.txt`; about 4 minutes):

```
the referee: 4 states of 13581 balls, 240 a side, wrapped; 60 s each, the 64 views of 30 × 30 sampled every 0.05 s
  contacts per ball per second 4.860 (the plan's 2.432; Enskog with the 2D cross-section, two diameters, 4.864)
  speeds against Rayleigh (σ = 4.998 from the energy): largest gap 0.0004 over 3259440 speeds
  view: density 0.2358 (n = 0.2358), energy per ball 24.984 (σ² = 24.983), count var/mean 0.526
P29: KILLED. contacts 4.860 against 2.432 (within 5%: false); Rayleigh gap 0.0004 (< 0.01: true); var/mean 0.526 (in [0.49, 0.61]: true)

the multiscale world: the window 45 × 45 (6 × 6 level-0 cells) and its middle 30 × 30 the view; 4 states × 10 places, 60 s each
  open              view: density 0.0989 (-58.1%), energy per ball 8.746 (-65.0%), contacts per ball 1.273 (-73.8%), count var/mean 9.551 (1714.7%)
  closed (control)  view: density 0.2319 (-1.6%), energy per ball 25.003 (0.1%), contacts per ball 4.758 (-2.1%), count var/mean 0.508 (-3.4%)
  open, the whole window as the view (no margin): density 0.1089 (-53.8%), count var/mean 15.225
  open: balls entered 183871, left 195549 over 40 runs; the window held 474 balls at the start and 182 at the end, on average
  open, density against the referee's by distance from the window's edge (1-unit bands, edge first):
    0.70 0.50 0.47 0.45 0.45 0.44 0.43 0.43 0.43 0.42 0.42 0.42 0.42 0.42 0.42 0.42 0.42 0.41 0.41 0.41 0.40 0.40 0.40
  level-0 cells beside the window, density over the world's: mean 1.317, lowest 0.390, highest 2.408
P30: KILLED. the open view's density, energy per ball and contacts per ball within 3% of the referee's: -58.1%, -65.0%, -73.8%
P31: KILLED. var/mean open 9.551 (1714.7% of the referee's; within 15%), closed 0.508 (-3.4%; at least 25% lower)

the books: over the 40 open runs, count off by at most 3.1e-11, momentum 1.8e-11, energy 2.1e-15 of itself
           over the pans of ten window widths and back: 1.0e+0, 9.1e+0, 1.2e-4
  just after a pan, the view's density 0.2179 (-7.6%), energy per ball 23.708
P28: KILLED. count within 1e-6, momentum within 1e-6, energy within 1e-9 of itself

the work per simulated second (balls moved, pairs looked at, balls entering tried, cells updated):
  multiscale, a world 240 a side (1.358e+4 balls, 52 cells): 1.854e+5
  multiscale, 3,840 a side (3.477e+6 balls, 100 cells): 1.923e+5 (3.7%)
  the referee, 240 a side (13581 balls): 7.473e+6; 480 a side (54325 balls): 2.990e+7 (×4.00)
P32: not killed. the multiscale work changes by 3.7% for 256 times the balls (less than 5%)
```

**Disclosed: a shakedown before the run.** Before the run, a short check of the engine (1 s of the referee, 5 s of one
open window) showed the referee at 4.83 contacts per ball per second and the open window losing balls. The run was
kept as planned, predictions unchanged. The first run of the script crashed while printing (after the simulations); it
was run again with the printing fixed, the simulations unchanged and seeded, so the output above is the run.

- **P29 killed, by my derivation.** The referee makes 4.860 contacts per ball per second, against the plan's 2.432. The
  plan took the discs' cross-section as one diameter. In two dimensions it is two: another centre within a diameter
  either side of the path meets it. With that, Enskog with Henderson's contact value gives 4.864, and the referee is
  within 0.1% of it. The plan's λ and the far field's D were both computed from the wrong rate. The real λ is 1.29, not
  2.58, so the margin was about six mean free paths, not three. The other two parts held:
  - the speeds are Rayleigh to 0.0004 (3.3 million speeds);
  - the count in a 30 × 30 view has var/mean 0.526, against Henderson's S(0) = 0.530.
- **P30 killed, and badly.** The open window drains. Its view holds 58% fewer balls than the referee's, 65% less energy
  per ball and 74% fewer contacts per ball. Its density is low everywhere, not only near its edge: from 0.70 of the
  referee's at the edge to 0.40 in the middle.
- **P31 killed.** The open view's count fluctuates 18 times too much: the window empties and refills. The closed control
  is only 3.4% below the referee's, not the 25% predicted. That part fails because of the measure, not the control. The
  variance was pooled over the 40 runs, and each closed window starts with an equilibrium sample of its count, so the
  pooled variance includes the open system's variation between windows. Within one run, a closed window's count is
  fixed. The prediction needed the variance within each run.
- **P28 killed, by a bug.** Without panning, the books balance to 1e-11 over all 40 runs. Over the pans they are off by
  exactly one ball, with its momentum and energy. Found after the run: when the window moves, a ball that has just
  stepped out of it (its centre past the edge, not yet folded) is folded into a new level-0 entry. If a coarser cell
  already holds that place, the coarser cell's totals are taken and the ball's are dropped. It happened once, on one
  pan across the world's wrap.
- **P32 not killed.** The multiscale world's work changes by 3.7% for 256 times the balls (52 cells to 100), while the
  referee's grows 4.00 times for 4 times the balls.
- *Measured:*
  - the window started with 474 balls on average and ended with 182;
  - the level-0 cells beside it rose to 1.32 of the world's density on average (0.39 to 2.41);
  - with no margin, the window as the view, the density is 54% low;
  - just after a pan, the view's density is 7.6% low.
  The bug touches only the pan's books, not these.

## Reading of run 11 (not ruled)

- **The idea's cost is right; its boundary is not.** Computing only the window costs the same in a world of 13,581
  balls and one of 3.5 million, while the referee's cost grows with its balls. That is the point Tom made, and it holds.
- **An open window needs the outside's push, not only its flux.** Run 11's window let balls in at the outside's one-way
  flux, which is exact for the balls that cross a line. But in a dense gas, part of the pressure is carried by contacts, not by
  balls crossing. At the window's edge, a contact between two balls inside sends one out and one in. The one sent out
  is gone, and nothing outside pushes back. So the edge is a sink for balls and for energy, and the whole window drains
  and cools: it keeps 38% of its balls and its energy per ball falls to a third. In the gas's terms, the window gets the
  outside's kinetic pressure but not its virial pressure (Z − 1 = 0.39 of the kinetic at φ = 0.15, so contacts carry 28%
  of the pressure).
- **A cell of a dozen balls cannot read its own flow.** The level-0 cells' mean motion is mostly the noise of a dozen
  velocities (σ/√13 ≈ 1.4 against σ = 5). Read as a flow, it takes about 1/13 off their spread, and it drives the balls
  they send in. A cell's reading of its flow needs a noise floor.
- **What a fix needs:** the outside's contacts at the window's edge. That means a band of balls there, held at what the
  cells say (density and temperature), which the window's balls can meet. Run 12 adds it, with its own predictions.

### Run 12 (11 October 2026): prediction, written before it ran

Run 11 with the window's edge given the outside's contacts. Everything else is as in run 11 (the gas, the cells, the
referee, the states, the places, the times), except four changes, named:

- **The band.** The window's outermost 2 units (a little over two diameters) are a band whose balls are held at what
  the cells beside the window say. Each level-0 stretch of the edge has its part of the band: the points nearer that
  edge than any other, less than 2 units in, of area 7.5 × 2 (13 at the window's corners). Each tick, for each part:
  - **Its count:** if it holds fewer balls than the cell beside it says, n·area, by more than half a ball, one ball is
    put at a free place in it. If it holds more by more than half a ball, one of its balls is taken out.
  - **Its warmth:** each of its balls has its velocity drawn afresh from the cell's spread, with chance ν·tick each tick
    (ν = 4.86, the gas's own contact rate, so about as often as it would meet another ball).
  - **Its books:** every ball put in, taken out or redrawn is charged to that cell, exactly.

  A ball whose centre leaves the window is still folded into the cell it enters. No ball enters at the edge any more:
  the band's count is kept instead. So the window's balls meet balls at its edge, at the outside's density and warmth,
  and the outside's push comes with them.
- **The cells read their flow above its noise.** A cell's mean motion is taken as a flow only where it is more than three
  times its own noise, |P|/N > 3σ/√N. Otherwise the flow is taken as none, and all its energy is warmth.
- **The far field's diffusion** uses the right λ = ⟨|u|⟩/ν = 1.29 (run 11's P29), so D = λ⟨|u|⟩/2 = 4.04. It is still a
  chosen model, and still not tested.
- **The fold bug** found after run 11 is fixed: a ball stepping out of the moving window is added to the cell that holds
  its place, whatever that cell's level.

The fluctuation measure is corrected. The count's variance over its mean is taken within each run, about that run's own
mean, then averaged over the runs. For the referee it is taken within each view's own time series, then averaged over
the views. The closed control keeps its window's count, so within a run its view's count should fluctuate less, by about
the share of the window that the view is not, 1 − 900/2025 = 0.56.

- **P28′ (run 11's P28, the bug fixed).** Over every run and every pan, the world's count stays within 1e-6, its
  momentum within 1e-6 and its energy within 1e-9 of itself. *Killed* if any run misses. (The bug was found after run 11,
  by looking for the lost ball, so this is not blind to it.)
- **P30′ (run 11's P30, with the band).** Averaged over the 40 open runs, the view's density, its kinetic energy per ball
  and its contacts per ball per second are each within 3% of the referee's. *Killed* if any is not.
- **P31′ (the measure corrected).** The open view's within-run var/mean is within 15% of the referee's within-view
  var/mean, and the closed control's is at least 25% lower than the referee's. *Killed* if either fails.
- **P32′ (run 11's P32, with the band).** The multiscale work per simulated second changes by less than 5% from
  L = 240 to L = 3,840. *Killed* if it changes by 5% or more.
- **P33 (the band reaches no further than itself).** In the open runs, the density at each distance from the window's
  edge, in 1-unit bands from 2 units inward, is within 5% of the referee's. *Killed* if any such band is off by more.
- *Measured, not predicted:*
  - the band's own density and energy per ball;
  - the level-0 cells beside the window;
  - the view just after a pan;
  - the band's share of the work.

Run 12 output (`node plans/pol/pol12.mjs`, in `plans/pol/pol-run12.txt`):

```
the referee (as run 11): 4 states of 13581 balls, 240 a side, wrapped; 60 s each, 64 views of 30 × 30 sampled every 0.05 s
  view: density 0.2358, energy per ball 24.984, contacts per ball per second 4.860; count var/mean within each view 0.462

the multiscale world, with the band: the window 45 × 45, its middle 30 × 30 the view; 4 states × 10 places, 60 s each
  open              view: density 0.0622 (-73.6%), energy per ball 9.662 (-61.3%), contacts per ball 1.313 (-73.0%), count var/mean within the run 29.640 (+6319.5%)
  closed (control)  view: density 0.2319 (-1.6%), energy per ball 25.003 (+0.1%), contacts per ball 4.758 (-2.1%), count var/mean within the run 0.309 (-33.0%)
  open: the band's density 0.3077 (+30.5%), energy per ball 21.384 (-14.4%); balls put in 1976157, taken out or left 1988829; the window held 474 at the start, 157 at the end, on average
  open, density against the referee's by distance from the window's edge (1-unit bands, edge first; the band is the first two):
    1.559 1.039 0.294 0.281 0.277 0.270 0.266 0.264 0.264 0.262 0.263 0.261 0.264 0.264 0.264 0.263 0.263 0.267 0.268 0.266 0.265 0.262 0.250
  level-0 cells beside the window, density over the world's: mean 1.413, lowest 0.383, highest 2.441
  just after a pan, the view's density 0.2265 (-3.9%), energy per ball 23.498 (-5.9%)
  the books: over the 40 open runs, count off by at most 2.2e-11, momentum 2.0e-11, energy 2.6e-15 of itself; over the pans 7.3e-12, 2.2e-12, 3.4e-16
  work per simulated second: 240 a side 1.029e+6 (52 cells), 3,840 a side 9.998e+5 (100 cells), -2.8%; run 11's window (no band) 1.854e+5

P28′: not killed. count within 1e-6, momentum within 1e-6, energy within 1e-9 of itself, over every run and pan
P30′: KILLED. the open view's density -73.6%, energy per ball -61.3%, contacts per ball -73.0% (each within 3%)
P31′: KILLED. within-run var/mean: open 29.640 (+6319.5%; within 15%), closed 0.309 (-33.0%; at least 25% lower)
P32′: not killed. the multiscale work changes by -2.8% for 256 times the balls (less than 5%)
P33: KILLED. from 2 units inward, the density is at most +75.0% from the referee's (within 5%)
```

- **P28′ not killed.** With the fold bug fixed, the books balance to 2e-11 over every run and every pan.
- **P30′ killed, worse than run 11.** The open view holds 74% fewer balls than the referee's, with 61% less energy per
  ball. Inside the band the window is drained to about a quarter of the referee's density (0.25 to 0.29, flat). The band
  itself is full (1.56 of the referee's density in its outer unit, 1.04 in its inner), and so are the level-0 cells beside
  the window (1.41 on average, 0.38 to 2.44).
- **P31′ killed for the open window, not for the control.** The open view's count swings 64 times too much. The closed
  control's within-run var/mean is 33% below the referee's (0.309 against 0.462), as predicted for a window that keeps its
  count.
- **P32′ not killed.** The work changes by −2.8% for 256 times the balls. The band costs: 1.03 million steps a simulated
  second, against run 11's window's 0.19 million.
- **P33 killed.** From 2 units inward the density is 71% to 75% below the referee's in every 1-unit band.
- *Measured:*
  - the band's balls churn: 1.98 million put in and 1.99 million taken out or gone over the 40 runs, about 820 a second
    per window against the 85 or so the band holds;
  - just after a pan, the view's density is 3.9% low and its energy per ball 5.9% low (now free of the fold bug).
- Run 11's script, run again on run 12's engine with run 11's options, reproduces its output line for line, except
  that the pans' books now balance (5.5e-12): the fix touched nothing else.

## Reading of run 12 (not ruled)

- **The band still opens onto nothing.** Its balls could still leave by the window's outer edge, and nothing outside sent
  any back. Half of each new band ball's motion is outward, and it crosses 2 units in about 0.2 s, so the band emptied
  outward about five times a second and was refilled from the cells. The window's own balls that drifted into the band
  left the same way. The band gave the window's edge contacts, but it was itself an open edge, one step further out.
- **The cells beside the window cannot hold the churn.** About 33 balls a second went in and out of each level-0 cell of
  a dozen balls. Their totals swung from 0.4 to 2.4 of the world's density, and the band's target swung with them. A
  reading of a dozen balls cannot serve as a reservoir for that.
- **What the closed control shows:** a window that keeps its count fluctuates 33% less within a run, the share of the
  window the view is not. So P31's measure can tell an open window from a closed one, once it is taken within each run.
- **The fix the two runs point to:** a window that loses no ball at its edge except through the cells' books. The band
  should be a mirror at its outer edge, its balls kept at the cells' count and warmth by putting in and taking out, never
  by flight. Run 13.

### Run 13 (11 October 2026): prediction, written before it ran

Run 12 with the band closed at its outer edge. Two changes, named; everything else is run 12's.
- **The window's outer edge is a mirror.** A ball reaching it is turned back, as in the closed control. No ball leaves
  the window by flight. Balls go in and out only through the band's keeping (one put at a free place, or one taken out,
  when its part's count is more than half a ball from its target), charged to the cell beside, exactly. The band still
  has its warmth redrawn from the cells', and the window's balls still meet the band's balls.
- **Each part of the band reads three cells.** Its target and its warmth come from the cells beside it pooled: the
  level-0 cell beside its stretch and the two either side of it along the edge (their counts, momenta, energies and
  areas summed; a coarser cell counted once). What it puts in or takes out is still charged to the cell beside it.

Worked out before writing this: a hard mirror in a gas of discs holds the density of centres at it at βp = n·Z = 1.39 n
(the wall contact theorem, Henderson's Z), falling to n within about a diameter. So the band's outer unit should be
denser than the referee, and its inner unit near n.

- **P28″ (the books).** Over every run and pan: count within 1e-6, momentum within 1e-6, energy within 1e-9 of itself.
  *Killed* if any run misses.
- **P30″ (the view sees the same gas).** Averaged over the 40 open runs, the view's density, kinetic energy per ball and
  contacts per ball per second are each within 3% of the referee's. *Killed* if any is not.
- **P31″ (open, not closed).** Within-run var/mean: the open view's within 15% of the referee's within-view value; the
  closed control's at least 25% lower than the referee's. *Killed* if either fails.
- **P32″ (the work).** The multiscale work per simulated second changes by less than 5% from L = 240 to L = 3,840.
  *Killed* if it changes by 5% or more.
- **P33′ (the band reaches no further than itself).** In the open runs, the density at each distance from the window's
  edge, in 1-unit bands from 2 units inward, is within 5% of the referee's. *Killed* if any is off by more.
- *Measured, not predicted:*
  - the band's two units against the referee (the mirror's layering);
  - the band's warmth;
  - the cells beside the window;
  - how many balls the band's keeping puts in and takes out;
  - the view just after a pan;
  - the work against run 11's window.

Run 13 output (`node plans/pol/pol13.mjs`, in `plans/pol/pol-run13.txt`; before it, a crash check only, 0.1 s of one window,
no statistics read):

```
the referee (as run 11): 4 states of 13581 balls, 240 a side, wrapped; 60 s each, 64 views of 30 × 30 sampled every 0.05 s
  view: density 0.2358, energy per ball 24.984, contacts per ball per second 4.860; count var/mean within each view 0.462

the multiscale world, the band closed by a mirror: the window 45 × 45, its middle 30 × 30 the view; 4 states × 10 places, 60 s each
  open              view: density 0.2219 (-5.9%), energy per ball 24.959 (-0.1%), contacts per ball 4.494 (-7.5%), count var/mean within the run 0.470 (+1.8%)
  closed (control)  view: density 0.2319 (-1.6%), energy per ball 25.003 (+0.1%), contacts per ball 4.758 (-2.1%), count var/mean within the run 0.309 (-33.0%)
  open: the band's density 0.2392 (+1.4%), energy per ball 24.577 (-1.6%); balls put in 725431, taken out or left 726377; the window held 474 at the start, 450 at the end, on average
  open, density against the referee's by distance from the window's edge (1-unit bands, edge first; the band is the first two):
    1.090 0.936 0.929 0.935 0.938 0.938 0.940 0.943 0.940 0.941 0.940 0.944 0.943 0.941 0.943 0.940 0.944 0.940 0.942 0.941 0.937 0.939 0.932
  level-0 cells beside the window, density over the world's: mean 1.020, lowest 0.004, highest 2.681
  just after a pan, the view's density 0.2325 (-1.4%), energy per ball 23.959 (-4.1%)
  the books: over the 40 open runs, count off by at most 2.7e-11, momentum 9.8e+2, energy 2.4e-15 of itself; over the pans 3.6e-12, 6.7e+2, 9.1e-4
  work per simulated second: 240 a side 6.790e+5 (52 cells), 3,840 a side 7.050e+5 (100 cells), +3.8%; run 11's window (no band) 1.854e+5

P28″: KILLED. count within 1e-6, momentum within 1e-6, energy within 1e-9 of itself, over every run and pan
P30″: KILLED. the open view's density -5.9%, energy per ball -0.1%, contacts per ball -7.5% (each within 3%)
P31″: not killed. within-run var/mean: open 0.470 (+1.8%; within 15%), closed 0.309 (-33.0%; at least 25% lower)
P32″: not killed. the multiscale work changes by +3.8% for 256 times the balls (less than 5%)
P33′: KILLED. from 2 units inward, the density is at most +7.1% from the referee's (within 5%)
```

- **P30″ killed, narrowly for energy, not for density.** Energy per ball is right (−0.1%). The view's density is 5.9%
  low and its contacts per ball 7.5% low, against 3%.
- **P31″ not killed.** The open view's count fluctuates as the referee's does (+1.8%); the closed control's is 33% lower.
  The window is open to the cells' count.
- **P32″ not killed.** +3.8% for 256 times the balls. The band costs about 3.7 times run 11's window (0.68 against 0.19
  million steps a simulated second).
- **P33′ killed.** Inside the band, the density is a flat 6% to 7% low, from 2 units in to the middle.
- **P28″ killed.**
  - **Momentum: a design flaw.** A mirror turns a ball back, which changes its momentum, and nothing was charged for it.
    In the gas, that push comes from the balls outside. Over a 60 s run, about 1,000 units of momentum (a ball's is ~5)
    went uncounted.
  - **Energy over the pans: also a flaw, found after the run.** Each operation of the band was charged to the one
    level-0 cell beside its stretch, a dozen balls, about 17 times a second. That cell's totals wandered far from any
    real state of a dozen balls: one cell held 0.4% of the world's density. When the window moved over such a cell, it
    was asked to unfold into balls with less energy than its own flow carries. No set of balls can be in that state. The
    unfold gave them the flow alone and created energy (up to 309 units at one step). Ticks and the folds keep energy to
    4e-10.
- *Measured:*
  - the band: 1.09 of the referee's density in its outer unit (the mirror holds centres at βp = 1.39 n against itself,
    falling within a diameter) and 0.94 in its inner;
  - the band's balls are put in and taken out about 300 times a second per window (a third of run 12's churn);
  - the cells beside the window: mean density 1.02 of the world's, but from 0.004 to 2.68;
  - just after a pan: density −1.4%, energy per ball −4.1%.

## Reading of run 13 (not ruled)

- **Closed by a mirror, the band works as a reservoir for warmth and for fluctuations.** The window's energy per ball is
  right to 0.1%, and its count fluctuates as an open region's does. What is left is a flat 6% shortfall of balls.
- **A count is the wrong thing to hold.** Against a hard mirror, a gas of discs crowds: centres pile up at the mirror
  (βp = 1.39 n at contact, by the wall contact theorem) and thin a little behind. The band's count was held at n times its
  area, which takes no account of that crowding. So the band was underfilled for a gas at the world's density, and the
  window settled to the density in balance with an underfilled band. What a reservoir fixes is not a count but a
  chemical potential: how readily a ball is put in. The band should be held at the cells' activity, which the gas's
  equation of state gives from their density.
- **A dozen balls cannot keep the books for the band.** Charging each of the band's operations to one level-0 cell of a
  dozen balls made that cell's totals wander out of any possible state. The band's operations should be charged across
  the cells it reads, and an unfold must keep the books even for a cell whose totals no set of balls could have.
- **The mirror pushes on the outside.** Each time it turns a ball back, the momentum it takes is the outside's. It must
  be charged to the cells beside the window, as the gas's own push would be.

### Run 14 (11 October 2026): prediction, written before it ran

Run 13 with the band held at the cells' chemical potential, and its books kept. Four changes, named; everything else is
run 13's (the mirror, the three cells read, the warmth redrawn, the measures).
- **The band is held at the cells' activity, not their count.** For hard discs, Henderson's equation of state
  Z = (1 + φ²/8)/(1 − φ)² gives the excess chemical potential in closed form, worked out before writing this:
  βμ_ex = (Z − 1) + (9/8)·φ/(1 − φ) − (7/8)·ln(1 − φ). At φ = 0.15 that is 0.7287, so the activity is z = n·e^0.7287 =
  2.072 n. In Widom's terms, 48% of random places are free for a new ball. Each tick, each part of the band, of area A:
  - tries Poisson(Γ·z·A·tick) new balls at random places in it, each kept only if free;
  - takes out each of its balls with chance Γ·tick.

  Here Γ = ν = 4.86 a second, so a band ball is replaced about as often as it would meet another. z comes from the
  pooled cells' density. This is grand-canonical keeping: the band fills to whatever a gas at the cells' chemical
  potential holds against the mirror, crowding included.
- **The mirror's push is charged to the outside.** A ball turned back at the window's edge changes its momentum by
  −2·v_n; the cells beside that stretch take +2·v_n.
- **The band's books are spread over the cells it reads.** Every ball put in, taken out or redrawn, and every push of
  the mirror, is charged to the three cells pooled, in proportion to their counts.
- **An unfold keeps the books for any cell.** A cell whose totals no set of balls could have (less energy than its flow
  carries) gives its balls the largest flow its energy allows (99% of it), and the rest of its momentum goes to the
  neighbouring cell with the fraction of a ball. A cell with no energy unfolds at rest, its momentum and energy to the
  neighbour.

- **P28‴ (the books).** Over every run and pan: count within 1e-6, momentum within 1e-6, energy within 1e-9 of itself.
  *Killed* if any run misses.
- **P30‴ (the view sees the same gas).** The open view's density, kinetic energy per ball and contacts per ball per
  second, averaged over the 40 runs, each within 3% of the referee's. *Killed* if any is not.
- **P31‴ (open, not closed).** Within-run var/mean: open within 15% of the referee's; the closed control at least 25%
  lower. *Killed* if either fails.
- **P32‴ (the work).** Changes by less than 5% from L = 240 to L = 3,840. *Killed* if 5% or more.
- **P33″ (the band reaches no further than itself).** From 2 units inward, the density in each 1-unit band within 5%
  of the referee's. *Killed* if any is off by more.
- *Measured, not predicted:*
  - the band's two units (the mirror's crowding);
  - how often the band's places are free (Widom's 48% in the bulk);
  - the cells beside the window;
  - the view just after a pan;
  - the work against run 11's window.
