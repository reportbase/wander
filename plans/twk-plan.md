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
