# TWK: three thumbs, walking, checked exactly

*13 November 2026, SPN R930. Tom: "I want to see the math in action with the 3 thumbs and omega, 3d cauchy and the
simplifed euhler's identity. Lets talk about how we can make that rigorous, and let the user walk around looking at his
environment."; then "new page, use omega, flat screen default, walking with w a s d. No support for mobile, desktop only."
A demo, `thumbs-walk.html`, not a test of the world. This plan says what the page must show exactly and how each claim is
checked. It is written and committed before the page. Nothing above the "Runs" line is edited afterwards.*

## What makes it exact

- **The world on whole numbers.** Every vertex is an integer point, made from its ground cell by a seeded hash, so no N
  is stored (R689). The eye starts on a whole point.
- **Turns by rational slopes, no angle computed.** A turn is the matrix of a rational half-slope u = p/q:
  ((q² − p²)/(q² + p²), 2pq/(q² + p²)). The three thumbs are the columns of a product of such matrices. The frame is
  therefore exactly orthonormal in fractions, and its transpose is its inverse.
- **The look is the thumbs' diagonal**, by definition, so the crosshair is the triple corner (R670, THM).
- **Walking by counted strides.** W, A, S, D move the eye by a stride of ¼ along the turned heading, itself a rational
  direction, so the eye stays a rational point.
- **Every check uses exact fractions (BigInt)**, except where the identity involves Ω itself, which is a limit. Those are
  checked in floating point and marked so.
- **The flat screen square to the look** is the default. Projection is one division per point, so wireframe edges stay
  straight, and the heat per unit of screen is cos³ off the look: 1/(4Ω(1 + r²)^(3/2)) with r in focal lengths.

## What the page shows, and the check for each (fixed now)

For the thing under the crosshair, its centre C seen from the eye E has thumb coordinates x = Tᵀ(C − E), three fractions.

- **K1, three thumbs close.** The pair slopes s_ab = x_b/x_a, s_bc = x_c/x_b, s_ca = x_a/x_c multiply to exactly 1.
  This is an identity; the check is of the arithmetic, and the content is that two slopes are free and the third closes.
  A negative coordinate means the thing lies in another facing, and the page says so.
- **K2, Euler simplified.** For each pair, w(s) = (1 − s² + 2is)/(1 + s²) and w(1/s) multiply to exactly −1, and
  |w(s)|² = 1 exactly (a Pythagorean triple). At the corner (s = 1), w = i.
- **K3, the exchange in Ω.** The share of a pair's sweep below s plus the share below 1/s is the whole sweep. Each share
  is out of Ω, and they add to Ω. Checked in floating point to 10⁻¹².
- **K4, scaling the world.** Multiplying every vertex and the eye by k (2, 7, 1/3) leaves every pair slope equal, exactly.
- **K5, a counted walk.** Holding the frame fixed and walking straight, each stride lowers the target's reach along the
  look (m = (x_a + x_b + x_c)/3) by the same amount, exactly. The strides left, from two looks one stride apart, equal
  m₂/(m₁ − m₂), the count to the plane through the target square to the look, exactly. They are computed from the
  apparent breadth b/m, a ratio, so the result does not depend on b.
- **K6, the 3D Cauchy on the sky.** A seeded sky of 40,000 directions uniform on the sphere. The share of the front
  hemisphere within r of the look is 1 − 1/√(1 + r²) (half within √3). Checked at r = ½, 1, √3, 3, within 4 standard
  errors.
- **K7, the heat's total.** 1/(4Ω(1 + r²)^(3/2)) integrated over the whole flat screen is 1. A numeric integral to 10⁻⁶.
- **K8, the thumb as overlay.** H defaults to the target's m, so the target is one thumb out and the corner is on what is
  looked at (R701). Other things are coloured by m/H: near teal, far violet in ratios one in 2, 4, 8. Changing H with the
  wheel moves no pair slope (exact), only the colouring.

## What would and would not be shown

- These are identities among slopes, checked exactly on a world that is itself exact. The page shows the series' kit
  working in one view (R908: the slope, the exchange, the weight with total Ω, the facings). It tests nothing about any
  observer or the physical world.
- K6 is statistical (a seeded sample), K3 and K7 are floating point. All others are exact.
- Desktop only; no touch support (Tom).

## Runs

### Run 1 (13 November; the page's own checks, read through its hook in headless Chromium)

The target was a box 6 × 4 × 10 centred at (−112, 2, 40), seen from (0, 2, −30) at yaw −60°, in this wedge.

- **K1 holds**: the three pair slopes (0.953, 0.948, 1.106, each a fraction of 11 to 12 digits) multiply to exactly 1.
- **K2 holds**: w(s)·w(1/s) = −1 and |w|² = 1 exactly for all three pairs.
- **K3 holds** in floating point to 10⁻¹².
- **K4 holds**: scaling the world and the eye by 2, 7 and 1/3 leaves every pair slope exactly the same.
- **K5 holds**: six strides each lowered the reach along the look by exactly 5299993/36719436. The strides left from two
  looks (521.892) equal the count exactly.
- **K6 holds**: the sky's shares within r = ½, 1, √3, 3 were 0.1057, 0.2986, 0.5003, 0.6854, against 0.1056, 0.2929,
  0.5000, 0.6838, all within 4 standard errors (r = 1 is 1.8 off).
- **K7 holds**: the heat totals 1.00000000.
- **K8 holds**: changing the thumb moves no pair slope.

Nothing failed. K1, K2 and K5's two counts are identities, so these checks test the arithmetic and the construction (an
exactly orthonormal rational frame, an eye that stays rational), not any claim about the world. No page errors.

### Run 2, plan (13 November; Tom: "yes", to re-anchoring the eye at each change of heading; written before the change)

The scaffolding reading (essay 20, R883): the frame is recomputed each pose from one current turn, so its denominators
stay bounded (the tower's middle terms cancel). The eye is a running total of strides along every heading taken, so its
denominator collects one factor per new heading (the scaffolding never taken down). The change: at each change of heading
the eye is re-anchored to the nearest point of the 1/16 grid. This is a write, and it gives up only the exact path back to
the start, which no check reads.

The method: a seeded random walk of 200 legs. Each leg is a new yaw (a whole degree in ±180) and 1 to 20 strides of W, A,
S or D, with the pitch fixed. It is run with and without the re-anchor, recording the eye's denominator digits after each
leg and, at the end, the digits of the target's readings and K1–K8 (K5 on the final leg).

- **A1.** With the re-anchor, the eye's denominator stays under 10 digits over all 200 legs. *Killed* if it ever exceeds 10.
- **A2.** Without it, the eye's denominator grows with the number of legs, past 100 digits by leg 50. *Killed* if under
  100 digits at leg 50.
- **A3.** With the re-anchor, the target's slopes stay under 40 digits. K1, K2, K4, K5 and K8 hold at the end of the walk
  in both runs. *Killed* if any of these fails.

### Run 2 (13 November; the page's hook in headless Chromium, the seeded walk of 200 legs, with and without the re-anchor)

| | eye's denominator, leg 10 | leg 50 | most over 200 legs | target's slopes | K1–K8 at the end |
|---|---|---|---|---|---|
| re-anchored (199 times) | 6 digits | 6 | 6 | 10 digits | all hold |
| not re-anchored | 34 | 102 | 129 | 136 digits | all hold |

- **A1 not killed**: with the re-anchor the eye's denominator never went past 6 digits.
- **A2 not killed**: without it, 102 digits by leg 50 (my bound was 100).
- **A3 not killed**: re-anchored, the target's slopes had 10 digits, and every check held in both runs.

Post hoc, not predicted: without the re-anchor the digits leveled off near 128 rather than growing on. Whole-degree yaws
give only about 107 distinct half-slopes k/128, so once each denominator has come into the running total, nothing new
enters. Finer turns would keep it growing. Either way the readings were exact; the cost of keeping the scaffolding was 13
times the digits in every slope read, with nothing on the page reading the path home it preserved.

### Run 3 (13 November; Tom: "yes,remove the trig"; a check of the change, no prediction written first)

The look is now held as whole numbers: q quarter turns and two half-slopes ky/128 (across) and kp/128 (up). A drag of two
pixels or an arrow key steps a half-slope by 1/128. Past an eighth of a turn (|ky| > 53) the half-slope passes to the next
quarter by tangent subtraction, u' = (u − 1)/(1 + u), rounded to the nearest 1/128. The screen's half-width is a slope of
6/5 from the look, so no tangent is taken. The rings are drawn through the rational points ((1 − t²)/(1 + t²), 2t/(1 + t²)).
The sky is uniform without an angle (a point uniform in the ball, normalized). Params are `?q=&ky=&kp=`.

- The hook's `trigFree(300)` replaces sin, cos, tan, atan, atan2, asin, acos, sinh, cosh and tanh with counters. It then
  runs 300 steps of turning, tilting, walking (re-anchoring included), drawing a frame and computing the exact readings.
  **Every count was 0.**
- `?q=-1&ky=34` is the old yaw −60° (half-slope tan 15° ≈ 34/128). It picks the same target as run 1 (the box at
  (−112, 2, 40)). K1–K4, K6–K8 hold; K5 waits for a walk.
- The one use of atan left is the Ω shares (K3 and their display), since Ω is a limit. Nothing in turning, projecting,
  picking or walking reads them.
- Limit: the wrap rounds, so turning a whole circle in steps does not return exactly to the start. 200 steps back from
  (q 2, ky −46) ended at (q 1, ky −40). Every pose is still an exact rational frame. Only the path of turns is not kept,
  which is the same kind of write as run 2's re-anchor.

### Run 4, plan (13 November; Tom: "4", to keeping things by their size on screen; written and committed before the change)

Tom's point (R932) was that this way needs only what is visible, not the whole world. In run 3 the page still held every
cell within a fixed radius (30 cells), a cut in units. The change is to make the world at every scale and keep a thing by
its size on screen, as `crosshairs.html` does (R689).

- **The world.** Level j = 0 … L has cells CELL·2^j wide. Each cell holds at most one thing, made from the cell by a seeded
  hash as now, with every length times 2^j (whole numbers still). Level 0 is the present world. `?levels=` sets L (default 8).
- **The cull.** A thing of breadth b (its largest of width, depth and height) at distance d from the eye is kept when
  b ≥ g·d, with g = 1/32. It is compared in squares (b² ≥ g²·d²), so no root or angle is needed. A thing with d < b (the eye
  inside its own breadth) is not drawn, at every level.
- **The scan.** Since b ≤ 32·2^j at level j, a kept thing lies within 32·2^j/g = 1024·2^j units, so the same number of
  cells (radius ⌈1024/24⌉ + 1 = 44 cells) is scanned at every level.

Predictions:

- **C1, one level costs the same as another.** From the start pose and five seeded poses at L = 8, the count of things
  kept at each of levels 1 … 8 is within 30% of their mean. *Killed* if any is outside.
- **C2, the work goes by levels, not by area.** The total kept at L = 2, 4, 8, divided by L + 1, agrees within 20%.
  A fixed radius reaching the same far things would scan cells in proportion to 4^L, by arithmetic. *Killed* if the
  per-level totals part by more than 20%.
- **C3, the cull is complete.** Every thing kept has b ≥ g·d. Within one extra ring of cells past the scan, at every level,
  no thing has b ≥ g·d (it was not missed). *Killed* if any is found.
- **C4, the scan's cost is fixed.** The cells scanned per frame are (L + 1) times the same count at every pose, wherever
  the eye is. *Killed* if they differ.
- **C5, nothing else breaks.** `trigFree` counts 0. K1–K4 and K8 hold on the target at the start pose. *Killed* otherwise.

What would and would not be shown:

- This is classical: quadtrees, level of detail and the "distant horizons" of streamed worlds all keep far things by size.
  The page would show the series' version on its own world: what is held is set by the grain g and the number of levels,
  and no count N of the world appears anywhere.
- With a world self-similar over L levels, the work is in proportion to L, the logarithm of the largest size over the
  smallest. That is not zero: a world with sizes without end would need levels without end. What is unbounded is the
  extent at each level, and it costs nothing.

### Run 4 (13 November; the page's hook `cull()` in headless Chromium, at L = 2, 4, 8, from the start pose and five seeded poses up to 10⁵ units out)

| L | things kept by level (start pose) | kept in all | per level | cells scanned (every pose) | frame |
|---|---|---|---|---|---|
| 2 | 465, 493, 487 | 1,445 | 482 | 18,231 | 6 ms |
| 4 | 465, 493, 487, 520, 481 | 2,446 | 489 | 30,385 | 13 ms |
| 8 | 465, 493, 487, 520, 481, 491, 466, 472, 476 | 4,351 | 483 | 54,693 | 21 ms |

- **C1 not killed.** Across all six poses at L = 8, levels 1–8 kept 455 to 520 things each, all within 30% of their mean
  (within 7%).
- **C2 not killed.** The total per level was 482, 489 and 483 at L = 2, 4 and 8. A fixed radius reaching level 8's far
  things (1024·2⁸ units) would scan about 3.7·10⁸ cells of the smallest size, against 54,693.
- **C3 not killed.** No kept thing was below the grain, and the extra ring past the scan held no thing that would qualify,
  at any pose or level.
- **C4 not killed.** The cells scanned were exactly 6,077·(L + 1) at every pose.
- **C5 killed by my set-up.** `trigFree` counted 0 in all three runs. But at the start pose (looking straight north)
  nothing is under the crosshair, so K1–K4 and K8 could not be checked there. At run 1's pose (`?q=-1&ky=34`) the target is
  the same box as before, and K1–K4 and K8 hold.

**In short.** What is held is set by the grain and the number of levels: about 480 things a level, the same at every
level and wherever the eye is, and no count of the world enters. The cost grows with the number of levels, which is the
logarithm of the largest size over the smallest; it does not grow with how far the world goes. This is classical (level of
detail, quadtrees); the page shows it on its own exact world.

### Run 5, plan (13 November; Tom: "yes", to sharing the view across scales by the Cauchy; written and committed before the change)

Run 4 gave every scale the same grain, so each scale held the same count (the flat share per ratio, total infinite over
scales without end). The change is to give each scale its Cauchy share. The Cauchy's heat per ratio is (1/π)·sech(ln s),
with total 1; per scale (ln 2 of ratio) the share falls as sech(k·ln 2) at k scales from the focus. On a ground the count
kept at a grain g goes as 1/g², so scale j gets the grain g·√cosh((j − j*)·ln 2), with j* the scale of the thing under the
crosshair. cosh is computed as (2^k + 2^−k)/2, so no Math function beyond the square root.

Also:
- Scales below 0 (`?below=`). At scale j < 0, lengths are dyadic fractions.
- Cell keys that do not repeat for large indices.
- Exact conversion of dyadic coordinates to fractions.
- The re-anchor grid scaled with the focus, so a tiny scale's positions are kept.
- `?share=flat|cauchy`, default cauchy.

Predictions, at the start pose and five seeded poses unless stated:

- **C6, the shape.** Averaged over the six poses, the count at scales j* + k (k = 0 … 4, upward from the focus at j* = 0)
  is within 20% of N₀·sech(k·ln 2), with N₀ the focus scale's count.
- **C7, scales above cost nothing.** Raising the top scale from 8 to 16 to 40 raises the total kept by under 1%.
- **C8, scales below cost nothing.** Adding scales below 0 down to −40 raises the total by at most N₀ (the sum
  Σ_{k≥1} sech(k ln 2) ≈ 1.77 is the ideal, but the eye's height of 2 above the ground cuts the smaller scales off). Going
  from −10 to −40 changes it by under 1%. The total stays under 4.6·N₀ (Σ over all k of sech(k ln 2) ≈ π/ln 2 ≈ 4.53).
- **C9, the same view at every depth.** The eye's place and height are scaled by 2⁻²⁰ (scales −40 … 8, focus j* = −20).
  The total kept is within 10% of the start pose's, and the counts at scales −20 + k (k = −4 … 4) sum within 10% of the
  start's at k. The hash differs per scale, so this holds statistically, not exactly.
- **C10, what depth costs.** At the focus 2⁻²⁰, the target's pair slopes take between 4 and 30 more decimal digits than at
  the start, and K1, K2, K4 and K8 hold there.
- **C11.** `trigFree` still counts 0.

What would and would not be shown:

- That holding scales without end costs a fixed total when each scale gets its Cauchy share, and that the view at any depth
  is the same view. The share law is ours. Culling by size on screen and per-scale budgets are classical.
- The digits grow with depth. That is the cost exactness pays where floating point would fail (near 2⁻⁵² of a distance).
