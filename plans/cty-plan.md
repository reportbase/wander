# CTY: a sky city, read from where you fly (plan, 14 November 2026)

Tom: "have you ever seen a futuristic city downtown sky scripers, where cars fly instead of drive on the ground?",
then "yes", to sketching a plan for a page of our own. An original city, not a copy of any film's.

A new page, `sky-city.html`, after `thumbs-walk.html`: the same arithmetic (whole numbers and exact fractions, no
trigonometry in turning, projecting or moving), the same read (each thing held by the read's heat where it stands),
and nothing stored. This plan and its predictions are committed before any code.

## What the page is

- **The city, made from cells, never stored.** Ground cells at every scale 2^j (j from −4 to 8). A cell holds a
  block, and a block holds towers: each tower's footprint, height and setbacks come from a hash of its cell, so the
  city is the same every time it is made. A tower's height is a few times its footprint (a skyline, not a field of
  boxes), and blocks at scale j sit between streets of width 2^j. Towers at a finer scale stand on the roofs and
  terraces of coarser ones, so there is detail at every distance.
- **The cars, on their own loops, never stepped.** Each car flies a closed loop about its home cell at one lane
  height (lanes at heights 2^j·L for whole L), its own sides, heading, direction round, speed and phase, as run 16's
  movers do. Its place at tick T is worked out from T alone, an exact fraction. Some lanes cross, so cars pass above
  and below each other.
- **The eye flies.** W A S D move along the look and across it, Space and C up and down, the mouse or arrows turn the
  look in half-slope steps (run 12's integer heading), G goes half way to the thing under the crosshair and B back.
  The eye can pass through a tower (wireframe); the tower the eye is inside is never held.
- **What is held is the read's heat.** As `thumbs-walk.html` since R957: a thing of breadth b at distance d is kept
  when b ≥ g·d, g = (1/32)·√cosh(ln ρ)/cos^(3/2) α, ρ = d/(√3·H), nothing behind the look, H the reach to what is under
  the crosshair and staying with nothing there. No fade and no glides (R958, R959).
- **Every word behind the menu** (☰): what is held and from how many cells, the one assumption (R959's, stated), the
  checks below with a button for each, the blueprint beside it (a city stored to some radius, its cells counted, never
  made), and how to fly.
- Wireframe only, plain canvas, desktop and touch as `thumbs-walk.html` (R947).

## What would and would not be shown

Shown, if the predictions hold: a city at every scale flown through and held without a stored list; cars in the air
placed exactly from the tick; the same count of cells read wherever the eye flies. Not shown: that any city or any eye
works this way, that the read is better than a stored scene, or anything about real traffic. The page states results,
not judgements (R940). Level of detail by size on screen and seeded worlds are classical; the share law and no count
entering are the series' (R934).

## Predictions (committed before the code)

- **C1, the read is the blueprint's.** Along 40 poses of a seeded flight (street level, mid-height among towers,
  above the roofs, looking up, looking down), what the read holds equals, thing for thing, what a blueprint made from
  every cell within reach holds by the same rule from exact centres: 0 missing, 0 extra at every pose. Killed by any
  missing or extra thing.
- **C2, cars exact.** Over 200 ticks, every car the read holds is at exactly the place a stored list stepped one tick
  at a time gives (equal fractions), with the eye still, flying, and from T = 10³⁰. Killed by any difference.
- **C3, no trigonometry.** Over 300 steps of turning, flying and picking, `trigFree` counts 0 calls. Killed by any call.
- **C4, scale moves no reading.** Scaling the world by 10⁻³ and 10³ (eye, towers, lanes, cars) leaves every pair slope
  of the thing under the crosshair the same fraction. Killed by any change.
- **C5, the work is the read's.** The cells scanned a frame at one look are the same within 1% at the origin, 10⁶ and
  10¹⁰⁰ units out. Killed by more than 1%.
- **C6, the count, stated honestly.** Looking level along a street among towers, the read holds between 200 and 1,500
  things; looking straight up from a street, fewer than half that; looking down from above the roofs, more than looking
  level. This is a guess from run 20 (level looks 425–446 on open ground), so it is the prediction most likely to be
  killed; if it is, the numbers are reported as found.

## Open decisions (Tom's)

1. A new page (as planned here), or flying and towers added to `thumbs-walk.html`.
2. Towers on towers at every scale (as planned), or one scale of city with the scales only in what is far away.
3. Whether cars stop, turn at junctions or follow streets, which would need their state held (runs 15–17: own loops
   are exact from T; anything that reacts to anything else is not).

## Tom's decisions, and what they change (14 November 2026, before any code)

Tom: "1. yes, 2. skyscripaers and exterior elevators 3. lets try both". So: a new page; one scale of city, skyscrapers
with elevators running up their outside faces (in place of towers on towers at every scale); and both kinds of car, side
by side. Written and committed before any code; the predictions above stand except where this section replaces them.

- **The city.** Cells 48 units on a side; streets 12 wide on the cell lines; each block four lots, most with a
  skyscraper: a footprint of 8 to 16, a height from 24 to about 190 (heavy toward the low end), setbacks above 60% and
  85% of the height on the tallest, a mast on some. One tower is one thing: its breadth b the largest of its sizes, its
  centre the middle of its box. In place of `thumbs-walk.html`'s near cut d ≥ b (which would drop a tall tower while the
  eye stood beside it), only the tower the eye is inside is not held.
- **Exterior elevators.** About half the towers have a car on one face, running from the ground to near the top and back
  at a steady speed: its height at tick T is a triangle wave in T alone, exact.
- **Flying.** W and S along the heading (level), A and D across it, Space and C up and down, a stride of one unit (shift:
  eight); the eye never goes below one unit. (The plan above said W moves along the look; level moves keep every place a
  rational point with the integer heading, so this is the change.)
- **Cars on their own loops** (from T alone): above the streets at lane heights 60, 76, 92, …, each round its own ring of
  1 to 3 blocks by 1 to 3 along the street lines, its own speed, direction and phase. Loops at one height can cross: these
  cars do not see each other.
- **Traffic** (cars that react, so their state is held): a district of 8 by 8 blocks at the origin, one-way streets
  alternating by line, north–south lanes at height 28 and east–west at 32 (so crossings never meet), the district's edges
  wrapped. 48 cars, speeds 1 or 2 units a step, a step every two ticks. A car moves one unit at a time only if no car is
  within 8 units ahead in its lane; at a junction it wants to turn (by a hash of the car, the junction and its count of
  junctions) and turns only if the other lane is clear within 8 units either side. Its state is stepped from the moment
  the page opens, one step at a time; nothing gives it from T alone. Each car also carries a ghost, the same rules with no
  other car, so the page can show which cars are off the path they would have flown alone.

Predictions C1–C6 stand as written, with C1's blueprint now towers, elevators and loop cars, and C2 now "cars on loops
and elevators". Added:

- **C7, traffic needs its state.** By 600 steps at least one car is off its ghost's path; stepping 0 → 600 at once and in
  ten pieces gives the same state exactly; the traffic's steps taken grow as cars × steps, while the loop cars' work does
  not grow with T at all.
- **C8, traffic keeps its rule.** Over 6,000 steps no two cars in one lane are ever nearer than 4 units (a car's length).
  Killed by any nearer pair.

## Runs

### Run 1 (14 November 2026; `runs/cty/run1.mjs`, the page's hook in headless Chromium, 1280 × 720; outputs `runs/cty/run1-out.json`, `run1-street.png`, `run1-above.png`)

- **C1 not killed.** At 40 poses of a seeded flight (eight each at street level, mid-height, above the roofs, looking
  straight up and looking straight down, up to 2,000 units from the origin) the read held, thing for thing, what a
  blueprint made from every cell within twice its reach held by the same rule from exact centres: 0 missing, 0 extra
  in all, towers, elevators and loop cars.
- **C2 not killed.** Elevators and loop cars stored and stepped one tick at a time over 200 ticks (about 7,800 stored,
  1.56 million additions), compared every 10 ticks: the same things held, at exactly the same places, with the eye
  still, flying, and from T = 10³⁰.
- **C3 not killed.** 300 steps of turning, flying (every direction, up and down included) and picking: 0 calls to any
  trigonometric function.
- **C4 not tested in run 1 (my set-up).** At the pose I chose, looking north down the avenue, nothing was under the
  crosshair, so there were no slopes to scale.
- **C5 not killed.** One look, the thumb held at 60: 6,625 cells scanned (reach 46 cells) at the origin, 10⁶ and 10¹⁰⁰
  units out, exactly the same; held 999, 1,035, 977.
- **C6 killed.** Level looks along a street held 156 to 1,284 (mean 651); one is under the predicted 200. The rest of it
  held: straight up held 79 to 281 (mean 226, under half the level mean), straight down 629 to 1,209 (mean 795, above the
  level mean). Mid-height looks held 401 to 2,983 and those above the roofs 809 to 3,145: a skyline seen whole is the
  most the read holds.
- **C7 not killed.** Traffic stepped 0 → 600 at once and in ten pieces: the same state exactly; 35 of 48 cars off their
  ghosts' paths; 28,800 car-steps (cars × steps), 3,086 waits, 225 turns, 39 refused.
- **C8 not killed.** Over 6,000 steps the nearest two cars in one lane ever came was 8 units (the gap the rule keeps); the
  first car left its ghost's path at step 6; 42 of 48 off by the end.
- No page errors.

### Run 1b (14 November 2026; `runs/cty/run1b.mjs`; C4 at poses with something under the crosshair, which run 1 lacked)

- **C4 not killed.** At five poses (street, low, mid-height, 2,000 units out, looking up), each with a tower under the
  crosshair: the world and the eye scaled by 1/1000, 1000 and 7/3 left the three pair slopes the same fractions, and
  they multiplied to exactly 1.
- Frame times in headless software rendering: looking up 3 ms, along a street 16 ms, at mid-height 25 ms, above the roofs
  36 ms.
