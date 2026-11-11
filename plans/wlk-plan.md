# WLK: the even ladder on the walk to the mountain

11 Nov 2026. Tom: "Yes, run the test." (to Claude's "the first thing I'd test is the even ladder in h/v, exactly,
against the walk demo"; `plans/discussion-note.md` item 7). Discussion mode (R865): no paper, essay or demo changes
from this; the result goes into the discussion note.

## Setting

As `approach.html` (R650): the thumb H = 2 cm held at arm's length L = 60 cm, H/L = 1/30; a thing of true breadth V*
(house 12 m, tower 60 m, mountain 3 km) at distance d; the reading v/h = (V*/d)/(H/L) = d_c/d with the corner at
d_c = V*·L/H; steady strides S = 0.7 m toward the foot. Write x = h/v = d/d_c for the reciprocal reading.
Exact arithmetic (Python fractions). The constants are read from `approach.html` itself.

A slip to record before running: the discussion note wrote "h/v = d/V*". With the thumb at arm's length it is
h/v = d/d_c = (H/L)·d/V*; d/V* is the thing read against itself (H/L = 1).

Known beforehand: `mountain.html`'s "walk one thumb" (d = H·s₂/(s₂ − s₁)); MOT's time to contact x/ẋ; R650's
V* = strides × H/L; R338 (the writer is the number line, no corner). So nothing here is expected to be new mathematics;
the test is whether the ladder is exactly as the note says, and what kind of thing it is.

## Predictions (committed before the run)

- **W1, the ladder is even.** Between any two looks one stride apart, x falls by exactly δ = S/d_c = S·(H/L)/V*, the
  same at every distance, before the corner and after it. *Killed* if any step differs from δ (exact comparison), at
  any of 1,000 starting distances per thing, including starts that are not whole strides from the foot.
- **W2, the count is the breadth.** From the corner (x = 1) to the foot (x = 0) the count of strides is 1/δ = d_c/S,
  equal to `approach.html`'s `stridesFromCorner`; times H/L it is V* in strides, times the stride in metres V* in
  metres: 12, 60, 3,000 exactly. The count is not a whole number in general (house 3600/7 = 514 2/7), so the last
  rung is a part stride. *Killed* if any of these fails exactly.
- **W3, the direct reading is not even.** In v/h = 1/x the steps grow without bound toward the foot: n strides before
  the foot, the step is 1/(δ·n·(n − 1)), each larger than the last. *Killed* if the steps in v/h are equal anywhere, or
  the formula fails.
- **W4, two scalings.** Scale the world by k with everything in it (V*, d, the stride, thumb and arm): no rung moves
  and the count is the same (the count is a write of the relation, R850). Scale V* and d but keep the stride: every
  x is unchanged at the scaled places, but δ and the count move by k (the stride then acts as a unit carried in).
  *Killed* if either fails, k = 1/100, 7, 100.
- **W5, the foot from two looks.** From any two looks one stride apart, with no walk to the foot: strides left
  = x₂/(x₁ − x₂), and the breadth in strides = (H/L)/(x₁ − x₂), exactly, at every distance. *Killed* if either fails
  at any of the 1,000 starts.
- **W6, no corner in the ladder.** x is the writer's proportional line in units of d_c: nothing in the sequence of
  steps marks x = 1 (the step just before and just after the corner are equal), and the ladder continues evenly past
  it to any distance. So the corner is met by looking (x = 1), not by the ladder. *Killed* if the steps either side of
  x = 1 differ.
- **W7, the even ladder against the even breath.** A pace that covers a fixed share q of what remains (the steady slide
  on Euler's plane, ln x falling by −ln(1 − q) a step) never reaches the foot: after n steps x = x₀(1 − q)ⁿ > 0 for
  every n. The steady stride reaches it in finitely many. The two are equal steps on two different rulers (x and
  ln x), and no pace is even on both. *Killed* if a sequence even in both x and ln x exists other than standing still
  (checked: equal differences and equal ratios force the step 0).

Expected reading if nothing is killed (Claude's, stated beforehand): the even ladder is real but it is the writer's
number line (R338), in units of d_c; walking with a counted stride is writing all the way (writes of the relation),
and the reciprocal reading is the chart in which that writing is even. The breath's "in" is each look, its "out" each
counted stride; the corner belongs to the looks, not to the strides.

## Runs

**Run 1** (11 Nov, `runs/wlk/wlk.py`, output `runs/wlk/wlk-run1.txt`; exact fractions, constants read from
`approach.html`: H/L = 1/30, stride 7/10 m). **Nothing killed.**

| thing | d_c | rung δ in h/v | strides, corner to foot | V* back |
|---|---|---|---|---|
| house | 360 m | 7/3600 | 3600/7 = 514.29 | 12 m |
| tower | 1,800 m | 7/18000 | 18000/7 = 2,571.43 | 60 m |
| mountain | 90 km | 7/900000 | 900000/7 = 128,571.43 | 3,000 m |

- W1 not killed: every step in h/v is exactly δ, at 1,000 starts a thing, out to 16 corners.
- W2 not killed: the count is d_c/S, the page's `stridesFromCorner` (its body is `cornerD(thing, k) / STRIDE`), and
  count × H/L × stride returns V* exactly. No count is a whole number here; the last rung is 2/7 or 3/7 of a stride.
- W3 not killed: the steps in v/h are 1/(δ·n·(n − 1)), growing at every stride toward the foot.
- W4 not killed: all scaled, same rung and count; the stride kept, the count moves by k.
- W5 not killed: strides left = x₂/(x₁ − x₂) and the breadth in strides = (H/L)/(x₁ − x₂), from any two looks.
- W6 not killed: the steps before, across and after x = 1 are equal.
- W7 not killed: (x − a)² − x(x − 2a) = a², so a pace even in x and in ln x is no pace; the fixed-share pace is still
  short of the foot after 2,000 steps (x ≈ 3·10⁻⁹²).

A fault of my set-up, recorded: the first execution stopped at W7 on `import sympy` (not installed here), after
printing W1–W6; W7's algebra was then checked in fractions instead and the script rerun whole. No prediction changed.

Read after the run (as stated beforehand): the ladder is real and exactly even, and it is the writer's number line in
units of d_c. What the test adds to the note: (1) the ladder has no corner, so the corner belongs to the looks and not
to the strides; (2) the foot does not have to be walked to: any two looks a counted stride apart give the strides left
and the breadth in strides (W5), which is parallax along the line of sight, `mountain.html`'s walk; (3) the even
stride and the even breath are equal steps on two rulers and cannot be the same pace (W7). All classical.
