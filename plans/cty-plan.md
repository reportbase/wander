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

## Runs
