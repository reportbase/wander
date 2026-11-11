# ONE: are the walk's read × count and R804's π/2 × 2/π = 1 one statement?

11 Nov 2026. Tom: "merge. then 1." (to Claude's first proposed next step: "an exact test of whether the walk's read ×
count and R804's π/2 × 2/π = 1 are one statement or two"; `plans/discussion-note.md` item 13, its open end).

## Setting

The walk as WLK (`plans/wlk-plan.md`): thumb over arm H/L = 1/30, stride S = 0.7 m, house, tower and mountain
(V* = 12 m, 60 m, 3 km), the reading s = v/h = d_c/d, x = h/v = d/d_c, one stride taking δ = S/d_c from x.

R804: along a sweep from home to the horizon the up share v goes from 0 to 1 with dv/dℓ = h on the circle, so (mean
read) × (length walked) = 1 on every path: circle 2/π × π/2, chord 1/√2 × √2, square ½ × 2.

Two kinds of "= 1" are in play and are kept apart here: **pointwise** (a number times its reciprocal, s·(1/s), R809)
and **summed** (a mean step times a count of steps equals the whole that was crossed; a telescoping sum).

Charts used for the walk's readings as unit relations: the capped chart (the larger of h, v set to 1: before the corner
(h, v) = (1, 1/x), after it (x, 1); the square's two edges) and the round chart ((h, v) = (x, 1)/√(1 + x²), the circle).

Known beforehand: the summed identities are the fundamental theorem (a sum of differences is the difference of the
ends), so each check below is near trivial as arithmetic. What is tested is the identification: which path, which
measure and which 1 the walk has, and whether π appears. Exact arithmetic (fractions), 50 digits (mpmath) where a
root or π is needed.

## Predictions (committed before the run)

- **J1, R804 has a twin.** On the circle, the chord and the square's edges, home to horizon, the thumb's share h
  empties by exactly 1 as v fills by exactly 1: Σ|Δh| = Σ Δv = 1 on each, so mean |dh/dℓ| × length = 1 with the same
  three splits (2/π × π/2, 1/√2 × √2, ½ × 2). *Killed* if any sum is not 1 or any split differs.
- **J2, corner to foot is the square's far edge, walked evenly.** In the capped chart the walk's places from the corner
  to the foot lie on v = 1, evenly spaced in h by δ; the count of strides N = 1/δ (3600/7, 18000/7, 900000/7), so
  step × count = δ·N = 1 exactly, the edge's length 1, the mean read |dh/dℓ| = 1. *Killed* if the spacing is uneven
  or δ·N ≠ 1 for any thing.
- **J3, the pointwise product is the summed one applied to what is left.** At every place, before and after the
  corner, x = (strides left) × δ, so s × (strides left) × δ = 1: read × count × step. *Killed* if it fails at any of
  1,000 places per thing.
- **J4, far start to the corner is the square's near edge, and needs the far start.** In the capped chart, from x₀ to
  the corner the places lie on h = 1 with v = 1/x, unevenly spaced (steps δ/(x(x − δ))), and Σ Δv = 1 − 1/x₀ exactly:
  short of the edge by 1/x₀, whole only for a walk begun without end. So the whole walk, from the horizon behind to
  the foot, is the square path whole: length 2, Δv = 1 on the first edge and −Δh = 1 on the second, R804's ½ × 2.
  *Killed* if the sum differs from 1 − 1/x₀ (x₀ = 2, 30, 10⁶) or the steps are even.
- **J5, the walk's split is never the turn's.** In the round chart the walk from the corner to the foot crosses
  Δv = 1 − 1/√2 and −Δh = 1/√2 (sum 1) over an arc π/4, but its strides are not even along the arc: the first
  stride's arc over the last's is 1/2 to leading order (arc per stride δ/(1 + x²)). Weighted by strides (the walk's
  own measure), the mean of h from the corner to the foot is √2 − 1 = 0.41421…, and from far off to the foot the mean
  of v per corner walked tends to 0; in no stretch of the walk is the stride-weighted mean read 2/π. The 2/π × π/2
  split belongs to steps even in turn (the elliptic pace), the walk's to the square (1 × 1 an edge). *Killed* if the
  stride-weighted mean of h or of v over corner-to-foot equals 2/π to 10 digits, or the arc ratio is not within 1% of
  ½ for the mountain.
- **J6, the fixed share never closes the 1.** Covering a fixed share r of what is left from the corner (r = 1/10, 1/2),
  after m steps Σ|Δh| = 1 − (1 − r)^m < 1 in the capped chart: the count is unbounded, the mean step tends to 0, and
  mean step × count = 1 − (1 − r)^m, reaching 1 only as a limit. *Killed* if the sum reaches 1 at any finite m ≤ 500
  (exactly, in fractions).
- **J7, the verdict I expect.** One statement in form, two in content: both are "a mean step times a count is the
  whole crossed", and the whole is the same 1 (the thumb in the thumb; the corner in corners); the walk's is R804 on
  the square path counted in strides, R804's circle form is the same sum counted in turn. π enters only with the
  turn's measure. Not a prediction with a kill of its own; it stands or falls with J2, J4 and J5.

## Runs
