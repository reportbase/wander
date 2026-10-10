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

