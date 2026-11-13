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
