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

### Run 5 (13 November; the hook `cull()` and `exact()` in headless Chromium, the six poses of run 4)

| scales held | kept, start pose (six poses) | cells scanned |
|---|---|---|
| 0 … 8, flat share (run 4) | 4,351 (4,273–4,452) | 54,693 |
| 0 … 8, Cauchy share | 1,337 (1,322–1,367) | 17,581 |
| 0 … 16 | 1,340 | 17,753 |
| 0 … 40 | 1,340 | 18,065 |
| −10 … 8 | 2,195 (2,096–2,197) | 29,163 |
| −40 … 8 | 2,195 (2,096–2,197) | 29,569 |
| −40 … 8, eye scaled by 2⁻²⁰, focus −20 | 2,136 (2,121–2,211) | 29,637 |

- **C6 not killed.** Averaged over the six poses, scales 0 … 4 kept 481, 392, 229, 119 and 66 things: 1.00, 1.02, 1.01,
  1.00 and 1.10 of N₀·sech(k·ln 2).
- **C7 not killed.** Raising the top scale from 8 to 40 raised the total by 0.2%.
- **C8 killed.** Adding the scales below 0 raised the total by 858, against my bound of N₀ = 465. I expected the eye's
  height to cut the smaller scales off near −1; it cut them off only below −6. The scales below mirror the scales above
  (413, 248, 113, 62, 20 against 382, 242, 141, 62, 25). Going from −10 to −40 changed nothing, and the total, about
  4.5 to 4.7 N₀, is at or just past my 4.6 N₀ at three poses (the ideal is π/ln 2 ≈ 4.53).
- **C9 not killed.** Scaled by 2⁻²⁰ the totals were 2,121 to 2,211 against 2,096 to 2,197. The counts at −20 + k
  (k = −4 … 4) summed to 2,053 against the start's 2,128 (3.5% off).
- **C10 killed.** At three looks the target's pair slopes had 22 to 26 digits 2⁻²⁰ deep, against 22 to 26 at the start,
  not 4 to 30 more. K1, K2, K4 and K8 hold there. My reasoning was wrong: a slope is a ratio of two coordinates, and the
  depth's factor 2⁻²⁰ is in both, so it cancels (K4). The depth's cost is in the eye's own coordinates (about six more
  digits at 2⁻²⁰), not in any reading.
- **C11 not killed.** `trigFree` counted 0.

Changed on the page during the run, after the first results:
- The near cut of the screen and the stride now shrink with the focus's scale (at 2⁻²⁰ the old ones were a million
  times too large).
- With nothing under the crosshair, the focus falls back to the scale of the eye's own height.
- `set({focus: null})` releases the focus without resetting it.

**In short.** With each scale given its Cauchy share, scales without end, up or down, cost a fixed total: about 4.5 times
the focus scale's count. The view 2⁻²⁰ deep is the same view. The readings take no more digits at depth; only the
position does. The cull is classical. What is ours is the share law, and that no count of the world enters.

### Run 6 (13 November 2026; a check, no prediction): going half way

Tom: "lets keep improving this demo and then write an essay about what we learned about the classical / reader
distinction." The page gains G (go half way to the thing under the crosshair) and B (back off to twice as far). Both
move the eye in exact fractions along the line from the eye to the thing's centre, so the thing's direction does not
move and its breadth on the screen doubles or halves. G stops before the thing would be nearer than its own breadth. The
thing followed is kept while it stays under the crosshair, though nearer things may come between, and any turn or stride
lets it go. A panel, "a read and a write, by the digit", shows the eye's longest denominator, the slopes' digits, the
thing's distance in its own breadths and what is held. Hook `approach(n)`, `backOff(n)`, `digits()`.

As with run 3, this is a check, not a test: I knew the answer before running it (the depth's factor cancels in a ratio,
C10). Script in the scratchpad, not kept.

- The pose with the farthest thing in its own breadths (`q = 1`, `ky = 18`, a 4 × 4 × 3 box 23 of its breadths off):
  G four times, then stopped (a fifth would put the eye inside its breadth). The three pair slopes were the same
  fractions, digit for digit, at all five places (13 digits at most). K1, K2 and K4 held at each.
- B four times put the eye back where it started, exactly (its denominators back to 1 digit).
- Before the lock, G's first halving brought a nearer, smaller thing (scale −2) under the crosshair, and the next three
  halvings went toward it. With the lock, the thing followed stays the same.
- The eye's denominators went from 1 digit to 2 over four halvings: one binary digit a halving, as the place is a sum
  of halves.

**In short.** Going half way doubles every reach along the thumbs alike, so every slope is unmoved: the read pays nothing
for nearness. The place pays a binary digit a halving. B undoes G exactly.

### Run 7, plan (13 November 2026; Tom: "1", to holding things by their size on the screen wherever the eye stands; written and committed before the change)

**What the page does now** (measured before writing this, the pose `q = 1`, `ky = 18`, eye `(X, 2, X − 30)`, scales −8 to 8):

| X | kept | cells scanned | target | slope digits | K1, K2, K4, K8 |
|---|---|---|---|---|---|
| 0 | 2,153 | 29,053 | box at (88.5, 2, −56) | 26 | hold |
| 10⁵ | 2,140 | 29,085 | box at (100015, 2, 99967) | 22 | hold |
| 10¹² | 2,078 | 29,085 | box at (1000000000112, 2, 999999999943) | 24 | hold |
| 10¹⁵ | the page hangs | | | | |

At 10¹⁵ the smallest scale's cell index, 10¹⁵ ÷ (24/256) ≈ 10¹⁶, is past 2⁵³, where a double cannot count by one: the
scan's `i++` stops moving. The eye's place is exact (fractions) but the cull reads it as a double. So "wherever the eye
stands" holds only up to about 10¹² units.

**The change.** The cull works from the exact eye: each scale's cell index is the floor of the eye's fraction over the
cell's width, a BigInt; cells are hashed from their whole index (the same hash as now wherever the index is under 2⁵³, so
the world is unchanged where the page worked); each thing keeps its centre as an exact fraction, and everything drawn,
picked or culled is computed relative to the eye (the eye's fraction subtracted exactly, then made a double). This is the
classical floating origin (camera-relative coordinates, as games with large worlds use), done here in exact arithmetic.

**Predictions** (same pose):
- **D1.** At X = 10¹⁵, 10³⁰ and 10¹⁰⁰, and at 10¹⁰⁰ with the eye and the world scaled by 2⁻²⁰, `cull()` returns in under
  2 s; the total kept is between 2,000 and 2,250 and the cells scanned within 1% of 29,085. *Killed* if any is outside.
- **D2.** At X = 0, 10⁵ and 10¹², the counts kept, the cells scanned and the target are exactly those in the table above.
  *Killed* if any differs.
- **D3.** K1, K2, K4 and K8 hold at every place, and the target's slopes have 18 to 30 digits at every X (not growing with
  the distance). *Killed* if a check fails or a slope has more than 30 digits.
- **D4.** The eye's place takes at least as many digits as X has (a write paying by the digit). *Killed* if fewer.
- **D5.** `trigFree` counts 0 at X = 10¹⁰⁰. *Killed* if not.

### Run 7 (13 November 2026; the hook in headless Chromium, the pose `q = 1`, `ky = 18`, eye `(X, 2, X − 30)`)

| X | scales | kept | cells scanned | focus | target | slope digits | eye's place, characters | `cull()` |
|---|---|---|---|---|---|---|---|---|
| 0 | −8 … 8 | 2,153 | 29,053 | | box at (88.5, 2, −56) | 26 | 2 | 128 ms |
| 10⁵ | −8 … 8 | 2,140 | 29,085 | | box at (100015, 2, 99967) | 22 | | 175 ms |
| 10¹² | −8 … 8 | 2,078 | 29,085 | | box at (1000000000112, 2, 999999999943) | 24 | | 193 ms |
| 10¹⁵ | −8 … 8 | 1,997 | 28,709 | −3 | tower | 24 | 16 | 228 ms |
| 10³⁰ | −8 … 8 | 2,137 | 29,053 | −1 | pyramid | 24 | 31 | 239 ms |
| 10¹⁰⁰ | −8 … 8 | 2,038 | 28,933 | −2 | box | 24 | 101 | 318 ms |
| 10¹⁰⁰ × 2⁻²⁰ | −8 … 8 | 1,287 | 17,753 | −8 | none | | 107 | 331 ms |
| 10¹⁰⁰ | −40 … 8 | 2,210 | 29,569 | 0 | none | | 101 | 542 ms |
| 10¹⁰⁰ × 2⁻²⁰ | −40 … 8 | 2,143 | 29,637 | −20 | none | | 107 | 463 ms |

No thing kept was below the grain and none past the scan would have qualified, at every place.

- **D1 killed**, three ways. (a) At 10¹⁵ the total kept was 1,997, three under my 2,000. (b) The cells scanned are not
  fixed: they depend on the focus's scale, since each scale's scan is set by its grain, which is set by its distance in
  scales from the focus (run 5). The places differ in what is under the crosshair, so in the focus; my 1% band was taken
  from places that happened to share a focus. Across these places the scan ran 28,709 to 29,085, within 1.3%. (c) My
  set-up: the case scaled by 2⁻²⁰ needs the scales below −8, which the page holds only with `?below=40` (as run 5 used);
  with the default it held 1,287. Run again with `?below=40` (last two rows): 2,143 kept, 29,637 cells, the same as run 5
  at 2⁻²⁰ near the origin (2,136 and 29,637). `cull()` returned in under 0.6 s everywhere.
- **D2 not killed.** At 0, 10⁵ and 10¹², the counts kept by scale, the cells scanned and the target were exactly the
  table in the plan, digit for digit.
- **D3 not killed** where it could be tested: K1, K2, K4 and K8 held and the slopes had 22 to 26 digits wherever there was
  a target (24 at 10¹⁵, 10³⁰ and 10¹⁰⁰). At three places nothing was under the crosshair at this pose.
- **D4 not killed.** The eye's place took 16, 31, 101 and 107 characters.
- **D5 not killed.** `trigFree` counted 0.

Also checked, no prediction: at 10³⁰, G then B put the eye back exactly, the slopes were the same fractions after G, and
20 strides with W were all equal and two looks gave the strides left, exactly (K5).

**In short.** Before the change the page held its view only to about 10¹² units from where it began, because the cull
read the eye as a double. Now the eye's place is used exactly and everything else is worked out from the eye (a floating
origin, classical), so the same view, the same count held and the same exact checks hold 10¹⁰⁰ units out and a millionth
of the size there. The only thing that grows is the place: 101 digits at 10¹⁰⁰.

## Run 8: the read against a blueprint, thing for thing (planned 13 November 2026)

Tom: "let others make those statements.   lets actually prove it with undeniable results." The page will say nothing
about which view is better or what nature has; it will show results. The claim to test: **the read holds, from the eye
alone, exactly what a blueprint holds for that eye by the same rule, nothing missing and nothing extra, at every place
and every scale, while storing nothing.** The comparison is brute force: a blueprint reads every cell of a region and
keeps every thing in it with its exact centre; the read scans only its own cells about the eye.

What this can and cannot show. G1 and G3 set the cull against an exhaustive list under the same keep rule
(b ≥ g·d and d ≥ b), so they can fail only through an error in the cull: its scan radius, its exact eye, its cell hash
past 2⁵³, its floating origin. That is what they test. They do not compare totals, joins or anything else a blueprint
does from no standpoint, and they say nothing about which is better.

Predictions, committed before the hook `godTest()` is written:

- **G1.** At 20 seeded poses with the eye inside the stored blueprint's square (|x|, |z| ≤ 2,500, height 2, random
  q, ky, kp), the stored blueprint's things kept by the rule from the eye (worked out from the blueprint's own exact
  centres) are exactly the read's held things at scales 0 to 8 whose centres lie in the square: 0 missing, 0 extra, at
  every pose. *Killed* by any one.
- **G2.** At those poses the read uses under 2% of the blueprint's N = 35,013 things. *Killed* if 2% or more at any pose.
- **G3.** At the eye (X, 2, X − 30) with q = 1, ky = 18, for X = 0, 10⁵, 10¹⁵, 10³⁰, 10¹⁰⁰, a blueprint made about the
  eye at every scale −8 to 8, each over a square of cells twice its scan radius on a side about the eye's cell (every cell
  read, every centre exact from the cell's index, the rule applied to the exact centre less the exact eye), holds exactly
  the read's held set: 0 missing, 0 extra. *Killed* by any one.
- **G4.** In G3 the blueprints read at least 4 times the cells the read scans, at every place. *Killed* if fewer.

### Run 8 (13 November 2026; `runs/twk/run8.mjs`, the hook in headless Chromium)

G1, 20 seeded poses inside the stored blueprint's square (N = 35,013 things, scales 0 to 8, 83,840 cells read once):

| eye (x, z) | read holds (all scales) | of them in the blueprint's reach | blueprint keeps by the rule | missing | extra | share of N used |
|---|---|---|---|---|---|---|
| (776, −976) | 2,120 | 767 | 767 | 0 | 0 | 2.19% |
| (866, −1637) | 2,141 | 1,208 | 1,208 | 0 | 0 | 3.45% |
| (−1943, −148) | 2,002 | 223 | 223 | 0 | 0 | 0.64% |
| (−659, 2094) | 1,889 | 66 | 66 | 0 | 0 | 0.19% |
| (270, −257) | 2,172 | 1,304 | 1,304 | 0 | 0 | 3.72% |

(five of the twenty shown; all twenty had 0 missing and 0 extra, 66 to 1,304 in common, K 1,889 to 2,250.)

G3, the eye (X, 2, X − 30), q = 1, ky = 18, a blueprint made about the eye at every scale −8 to 8:

| X | read holds | blueprint, half-width 1 scan (as predicted) | cells | blueprint, half-width 2 scans | cells | read scans |
|---|---|---|---|---|---|---|
| 0 | 2,153 | 2,153, 0 missing, 0 extra | 38,473 | 2,153, 0 missing, 0 extra | 151,193 | 29,053 |
| 10⁵ | 2,140 | 2,140, 0, 0 | 38,513 | 2,140, 0, 0 | 151,345 | 29,085 |
| 10¹⁵ | 1,997 | 1,997, 0, 0 | 37,985 | 1,997, 0, 0 | 149,321 | 28,709 |
| 10³⁰ | 2,137 | 2,137, 0, 0 | 38,473 | 2,137, 0, 0 | 151,193 | 29,053 |
| 10¹⁰⁰ | 2,038 | 2,038, 0, 0 | 38,297 | 2,038, 0, 0 | 150,521 | 28,933 |

- **G1 not killed.** At all 20 poses the read held exactly the things the stored blueprint keeps by the same rule from
  the eye: none missing, none extra.
- **G2 killed.** The read used up to 3.72% of N, over my 2%. I had taken the figure from the start (243 of 35,013, 0.7%),
  where the eye looks out of the square's middle; inside it, looking across it, the read holds more of what is stored.
- **G3 not killed.** At every place, out to 10¹⁰⁰ units, a blueprint made about the eye from every cell (worked out from
  exact centres, no floating origin, no scan) held exactly the read's set; at twice the reach, the same, so nothing past
  the read's scan qualifies.
- **G4 killed by my set-up.** As written, a square "twice its scan radius on a side" is the scan circle's own bounding
  square, about 4/π of it: the blueprints read 1.32 times the read's cells, not 4. At twice the reach each side (not
  predicted) they read 5.2 times as many and agreed the same.

No page error. Post hoc, and as the plan said: G1 and G3 can fail only through an error in the cull, so what they show is
that the cull has none at these places; they compare nothing else a blueprint does.

**In short.** Wherever the eye stands, out to 10¹⁰⁰ units, the read holds thing for thing what a blueprint made by
reading every cell holds for that eye under the same rule, while scanning about a fifth of the cells that blueprint reads
and storing nothing. On the page, P runs the same check where the eye is.

## Runs 9, 10 and 11: along a walk, what is drawn, and the cost (planned 13 November 2026)

Tom: "1 2 then 3". Each checks the read against a blueprint by brute force, as run 8 did; each states counts, not
judgements. Predictions, committed before the hook functions are written:

**Run 9, along a walk.** A seeded walk of 100 actions from each of three starts: the start (0, 2, −30); 10¹⁰⁰ out;
10³⁰ out with G pressed until the focus is below scale 0. Each action is one of: strides (W A S D, 1 to 6), a turn or
tilt (±1 to ±12 half-slopes), G, B. After each action the page draws a frame (so the focus and the target are its own),
and a blueprint is made about the eye at every scale −8 to 8, every cell out to 1.5 scan radii each side (beyond the
read's reach), the rule applied to exact centres.
- **W1.** At every one of the 300 poses: 0 missing, 0 extra. *Killed* by any one.
- **W2.** The walks exercise what could break it: across the three walks the focus takes at least 4 different values,
  the eye is re-anchored at least 10 times, G and B each act at least 5 times. *Killed* if any is short (then the walk
  did not test what it was meant to).

**Run 10, what is drawn.** At the same 300 poses, every thing the blueprint keeps is projected from the blueprint's own
record (its exact centre less the exact eye, rounded once to doubles; its box as stored) through the page's own
projection and near-plane clip, and set beside the read's segments as the page draws them.
- **D1.** At every pose the two give the same number of segments, thing for thing. *Killed* if not.
- **D2.** Every segment's ends agree to within 10⁻⁶ pixels on a 1280 × 720 screen. *Killed* by any larger difference.

**Run 11, the cost.** A blueprint of scales 0 to 8 built for squares of side 2·R0, R0 = 750, 1,500, 3,000, 6,000; and
the read's cells scanned with the eye at the middle of each square and at 10¹⁰⁰.
- **C1.** The blueprint's cells read are exactly Σ (2⌈R0/(24·2^j)⌉)² over j = 0 to 8, and grow by 4 ± 3% for each doubling
  of R0 past 1,500. *Killed* otherwise.
- **C2.** Its things N are 0.42 ± 0.01 of its cells (the hash's rate) at every R0. *Killed* otherwise.
- **C3.** At every one of those eyes, with the same pose and focus, the read scans the same number of cells, within 1.5%.
  *Killed* if not.
- **C4.** By the same formula, a blueprint holding scales −8 to 8 over the R0 = 3,000 square reads more than 10⁹ cells.
  *Killed* if fewer.

### Runs 9 and 10 (13 November 2026; `runs/twk/run9.mjs`, 1280 × 720, outputs `runs/twk/run9-*.json`)

| walk | poses | missing | extra | segments compared | segment counts differing | largest gap, px | foci | re-anchors | G, B acted |
|---|---|---|---|---|---|---|---|---|---|
| from the start | 100 | 0 | 0 | 449,702 | 0 | 1.07·10⁻⁶ | −8, −3, −1, 0, 2, 3, 6 | 16 | 3, 4 |
| 10¹⁰⁰ out | 100 | 0 | 0 | 76,512 | 0 | 2.5·10⁻⁷ | −8, 2, 3 | 15 | 0, 1 |
| 10³⁰ out, below scale 0 | 100 | 0 | 0 | 548,771 | 0 | 1.33·10⁻⁶ | −8, −3, −1, 0, 4, 6, 8 | 11 | 3, 6 |

The blueprints read 2.97 to 2.98 times the cells the read scanned. No page error.

- **W1 not killed.** All 300 poses: 0 missing, 0 extra.
- **W2 not killed** by its letter (foci 9 values, 42 re-anchors, G 6 and B 11 times). But post hoc the walks were weaker
  than meant: at 211 of the 300 poses the read held fewer than 100 things (most held none), with the focus at −8. The
  cause is a page bug the walks found: **B backs off along the line from the thing followed, and when that thing is above
  the eye the eye goes below the ground** (from the start, action 37 took the eye from y = 11.06 to y = −1,002). Below the
  ground nothing is under the crosshair, the focus falls to its floor and nothing is kept. So W1 held at 89 poses that
  tested much and 211 that tested little.
- **D1 not killed.** At every pose each thing gave the same number of segments both ways.
- **D2 killed**, narrowly: two poses past my 10⁻⁶ px (1.07·10⁻⁶ and 1.33·10⁻⁶, both just after a B or a stride with the
  focus at −3, so with things 1/8 the size close to the eye). The two routes round differently (the read's floating
  origin against the blueprint's exact centre rounded once); my bound was the guess, and the gap is a millionth of a pixel.

### Run 9b (planned 13 November 2026, after the fix)

The fix: G and B stop rather than put the eye at or below the ground (y ≤ 0). The same three walks, seeds and actions.
Predictions:
- **W1b.** All 300 poses: 0 missing, 0 extra. *Killed* by any one.
- **W3.** At least 250 of the 300 poses hold 1,000 things or more (the walk stays where there is something to test).
  *Killed* if fewer.
- **D2b.** Every segment's ends agree within 10⁻⁵ px (my bound loosened tenfold, said so, after run 10's 1.3·10⁻⁶).
  *Killed* by any larger.

### Run 9b (13 November 2026; the same script after the fix)

| walk | poses | missing | extra | held | segments | largest gap on screen, px | largest gap anywhere, px | foci | re-anchors | G, B acted |
|---|---|---|---|---|---|---|---|---|---|---|
| from the start | 100 | 0 | 0 | 1,699–2,226 | 1,232,831 | 4.5·10⁻¹³ | 1.7·10⁻⁶ | −3 … 7 (8 values) | 16 | 4, 3 |
| 10¹⁰⁰ out | 100 | 0 | 0 | 2,052–2,208 | 1,212,612 | 4.5·10⁻¹³ | 2.2·10⁻⁵ | −1 … 4 (6 values) | 15 | 9, 14 |
| 10³⁰ out, below scale 0 | 100 | 0 | 0 | 1,957–2,156 | 1,223,765 | 4.5·10⁻¹³ | 4.5·10⁻⁶ | −3 … 6 (6 values) | 11 | 5, 6 |

- **W1b not killed.** All 300 poses: 0 missing, 0 extra; every thing drew the same number of segments both ways.
- **W3 not killed.** All 300 poses held 1,699 things or more.
- **D2b killed.** At 10¹⁰⁰ one segment's end differed by 2.2·10⁻⁵ px, past my 10⁻⁵. Post hoc (the hook now reports the
  worst point): every gap over 10⁻⁶ px is at an end clipped at the near plane and lying 3 to 17 million pixels off the
  screen, a relative gap of about 10⁻¹², the two routes' doubles rounding apart; on the 1280 × 720 screen the largest gap
  at any pose was 4.5·10⁻¹³ px. The bound should have been relative, or on the screen.

### Run 11 (13 November 2026; `runs/twk/run11.mjs`)

| R0 | blueprint cells | the formula | things N | N / cells | build time |
|---|---|---|---|---|---|
| 750 | 5,472 | 5,472 | 2,215 | 0.405 | 4 ms |
| 1,500 | 21,344 | 21,344 | 8,749 | 0.410 | 28 ms |
| 3,000 | 83,840 | 83,840 | 35,013 | 0.418 | 161 ms |
| 6,000 | 333,836 | 333,836 | 140,043 | 0.420 | 858 ms |

The read at the start and at 10¹⁰⁰ (q = 1, ky = 18, focus 0): 29,085 cells scanned at both, 2,185 and 2,199 kept.
Scales −8 to 8 over the R0 = 3,000 square: 5,461,333,840 cells by the formula (scales 0 to 8 alone: 83,840).

- **C1 not killed.** The cells read are the formula exactly; each doubling of R0 past 1,500 multiplies them by 3.93 and
  3.98.
- **C2 killed** at the two small squares (0.405 and 0.410 against 0.42 ± 0.01). Post hoc: at small R0 the coarse scales'
  cells straddle the square's edge and many of their things have centres outside it, so are read but not counted; the
  ratio climbs toward the hash's 0.42 as the square grows (0.418, 0.420).
- **C3 not killed, and by my set-up barely a test**: the four squares share one middle (the start), so their reads are
  one eye four times. The case that tests it, the start against 10¹⁰⁰, scanned 29,085 cells at both.
- **C4 not killed.** 5.46·10⁹ cells, 65,000 times the same square at scales 0 to 8.

**In short, runs 9 to 11.** Along 300 poses of three walks (strides, turns, G and B, re-anchoring, the focus moving
through 12 scales, out to 10¹⁰⁰), the read held exactly what a blueprint made from every cell about the eye holds, and
drew it to 4.5·10⁻¹³ px on the screen, scanning a third of that blueprint's cells and storing nothing. The walks found a
bug (B could take the eye below the ground), now fixed. A stored blueprint's cells grow with its area, 4 times for each
doubling of its side, and 65,000 times again to hold the scales the read holds; the read scanned 29,085 cells at the
start and 10¹⁰⁰ out.

### Shown on the page (13 November 2026; R943; Tom: "we don't need to declare anything, show it. the blueprint does not scale to the universe.")

No prediction, a display. U takes the eye ten times farther from the start along x, exactly. With the blueprint shown (O) the
menu gives the cells a blueprint stored from the start out to the eye would have at the scales the read holds (−8 to 8),
counted exactly and never made (`toHere()`), beside the cells the read scans there. Pressed 100 times from the start
(headless Chromium, no page errors):

| eye from the start | blueprint's cells | read scans | read holds |
|---|---|---|---|
| 10 | 10⁵ | 29,085 | 2,195 |
| 10⁴ | 10¹⁰ | 29,053 | 2,187 |
| 10¹³ | 10²⁸ | 29,085 | 2,176 |
| 10²⁶ | 10⁵² | 28,709 | 2,016 |
| 10¹⁰³ | 6.06·10²¹⁰ | 29,053 | 2,085 |

(digits of the count, rounded to a power.) The blueprint's cells are four times as many for each doubling of the distance; the
read's scan is the same within 1.2% at every distance, storing nothing. The menu also says that with a unit of a metre the
observable universe is about 8.8·10²⁶ across.

### Run 12 (13 November 2026; R944; Tom: "yes", to making the return exact without trigonometry)

Not a prediction committed beforehand: a fix, checked by construction and by a probe. Until now an eighth of a turn
passed to the next quarter by tangent subtraction rounded to k/128, so a turn and its undoing did not always cancel
(PWL run 1: 93 of 100 long walks a step off). Now the heading is one whole number N of half-slope steps: q = 2m half
turns and ky = N − 256m in [−128, 127]. At ky = ±128 the half-slope is ±1, a quarter turn, so (2m, 128) and
(2m + 2, −128) are one heading exactly, and nothing is rounded. The step is 0.90° at ky = 0 and 0.45° at the seam (it was
0.90° to 0.77° in the old band).

Probe (headless Chromium, no page errors): 100 seeded walks of 2,000 turns of 1 to 12 steps each way, then undone:
**100 of 100 back at (0, 0) exactly** (up to three half turns out, every ky in [−128, 127] reached); the seam step from
(0, 127) lands on (2, −128) with every check holding; `trigFree(300)` still 0 calls. PWL's copy of the rule (run 3):
100 of 100 long walks back exactly, every walk crossing a half turn. Old links with an odd q and ky ≠ 0 now open a
slightly different heading (the steps are not even in angle); with ky = 0 the same.

## Runs 13 and 14: predictions (13 November 2026, written before any change or run; Tom: "1, 2, 3")

**Run 13, the world made denser (N per area).** `?dens=D` puts D things in each cell (D = 1 the world as it is; the
thing s > 0 its own hashes, its own key). Two ways to read it: the grain fixed (as now), or K held: the read keeps the
grain where its own held count stays near a target, moving the grain only by what it holds (no count of the world).
- M1 (grain fixed): held K grows about as D (×D within 30%); cells scanned unchanged (to the cell).
- M2 (K held, target 2,100): after settling, held within 15% of 2,100 at D = 1, 2, 4, 8, 16; things examined (cells
  scanned × D, the work) within a factor 2 of D = 1's; the grain coarsening about as √D.
- M3: a blueprint stored over the 6,000 square at scales 0 to 8 holds about D times as many things (within 15%).
- M4: at every D, in both ways, the read set beside a blueprint made about the eye by the same rule: 0 missing, 0 extra.

**Run 14, two ways, step by step.** One seeded walk of 300 poses, drawn twice: the page's way (half-slope steps,
rational turns, exact fractions) and a classical pipeline (yaw and pitch held as floats in radians, the frame built by
Math.cos and Math.sin each pose, the eye a float64 sum of strides). Counted, not judged.
- T1: the page's way makes 0 trigonometric calls; the classical way 8 a pose (4 of them the base frame, which a pipeline
  would compute once; counted both ways).
- T2: the two draw the same picture: every held thing's segment ends within 10⁻⁶ px (the walk stays within 10⁴ units).
- T3: both lay the world on a signed grid of cells and hold the eye in it (the page in exact fractions, the classical
  way in float64): stated, not scored.
- T4: retraced, the page's turn returns exactly (TWK run 12) and the classical float yaw returns to within 10⁻¹² rad.

### Runs 13 and 14 (13 November 2026; `runs/twk/run13.mjs`, output `runs/twk/run13-out.json`; headless Chromium, no page errors)

**Run 13.** At the start, scales −8 to 8:

| things a cell | grain fixed: held | cells scanned | things looked at | K held: held | grain × | cells | things looked at | stored blueprint N |
|---|---|---|---|---|---|---|---|---|
| 1 | 2,195 | 29,085 | 12,214 | 2,107 | 1.02 | 27,461 | 11,561 | 35,013 |
| 2 | 4,264 | 29,085 | 24,435 | 2,075 | 1.42 | 14,481 | 12,347 | 70,070 |
| 4 | 8,654 | 29,085 | 49,053 | 2,071 | 2.03 | 7,765 | 13,174 | 140,508 |
| 8 | 17,309 | 29,085 | 97,747 | 2,045 | 2.87 | 4,277 | 14,303 | 280,717 |
| 16 | 34,625 | 29,085 | 195,159 | 2,108 | 3.88 | 2,489 | 16,769 | 560,463 |

M1 not killed (held ×1.94, 3.94, 7.89, 15.8; the scan the same). M2 not killed (held 2,045 to 2,108; things looked at
1.45 times D = 1's at D = 16; the grain 1.02, 1.42, 2.03, 2.87, 3.88 against √D 1, 1.41, 2, 2.83, 4). M3 not killed
(×2.00, 4.01, 8.02, 16.0). M4 not killed (0 missing, 0 extra at all ten). With K held the read keeps about 2,100 things
whatever the density, moved only by its own count; the stored blueprint's N goes as the density.

**Run 14.** 300 poses, 3.74 million segments: the page 0 trigonometric calls; the classical way 1,200 sines and 1,200
cosines (8 a pose, 4 of them the fixed base frame) and 600 arctangents, which my code used to make that base frame's
angles and a pipeline would hold as constants (T1 not killed as to sines and cosines; the arctangents my set-up). The two
pictures within 2.4·10⁻¹² px (T2 not killed). Both lay the world on a signed grid of cells and hold the eye in it (T3).
96 turns retraced: the page exactly, the classical float yaw 2.8·10⁻¹⁷ rad off (T4 not killed). On the page: n, k, c in
the menu's checks.

## Run 15: things that move (predictions, 13 November 2026, written and committed before any change; Tom: "Proceed", to
testing motion)

What is added. Movers: things in the sky at every scale, each scale's movers sharing one velocity V_j per tick (a dyadic
fraction, a different heading each scale, about 2^j/16 units a tick), each mover's centre exact, C(T) = C₀ + V_j·T at
tick T (a whole number). A mover belongs to the cell of its start; the read finds the movers near the eye by scanning
the cells about eye − V_j·T at that scale (the eye in the movers' own frame), by the same keep rule as the ground. No list
of movers is kept, and no mover is stepped. The blueprint to set beside it is the classical one: every mover in a region
stored at tick T₀ and stepped one tick at a time (C += V_j), its kept set worked out by the same rule at each tick.

Predictions:
- V1: at every sampled tick, the movers the read holds are, key for key, the movers the stepped blueprint keeps (0 missing,
  0 extra), with the eye still and along a seeded walk; focus and grain held, so only motion changes what is kept.
- V2: the read's mover cells scanned the same at every tick (to the cell) and its movers held within ±30% of their mean
  over the run; the stepped blueprint's work N_stored × ticks.
- V3: a mover stepped tick by tick lands exactly (fraction equality) where the read puts it by C₀ + V·T, at T = 1, 10, 10²,
  10³, 10⁴; and at T = 10³⁰ the read still gives each held mover's exact place (the eye taken there), with the same count
  of cells scanned.
- V4: the ground world unmoved: with movers on, the ground things held are the same keys as with movers off; `?movers=0`
  gives run 13's 2,195 at the start.
- V5: for a mover under the crosshair, the exact checks (the three pair slopes multiply to 1; w(s)·w(1/s) = −1) hold at
  every sampled tick.
