# FDZ: depth laid on Euler's circle, the corner on the crosshair

*13 November 2026, SPN R926. Tom: "i think our reframe of euhlers identity is quite interesting. I wonder if it would be
useful for first person games.", then "yes" to Claude's offer: a depth layout with the corner at the crosshair, tested as
a renderer would store it. The plan and the predictions are written and committed before any run. Nothing above the
"Runs" line is edited afterwards.*

## The question

The reframe puts a slope s on Euler's circle by w(s) = (1 + is)/(1 − is). Home lands at +1, the corner (s = 1) at i, and
the horizon at −1. The exchange s ↦ 1/s mirrors the circle about i, since w(s)·w(1/s) = −1. Read with s = d/f (f the
distance to what the crosshair is on), this gives a depth layout in which the thing looked at sits at the corner, nearer
things lie on one side and farther things on the other, mirrored by d ↦ f²/d.

The question is a practical one: does storing depth this way help a renderer tell two close surfaces apart (avoid
z-fighting) at the focus, against the layouts engines use, in the formats engines actually store?

## Known beforehand (stated so the test is not taken as blind where it is not)

- **FPV runs 1–5** (`plans/fpv-plan.md`): the turn about the focus, g = (2/π)·arctan(d/f), stored in K equal
  fixed-point steps, gives the focus the finest cell, π/K relative, whatever the range; at 32 bits fixed point it is 97
  times finer than reversed-Z at the focus, for about seven doublings either way. **That was fixed point.** Real GPUs
  mostly store depth as a 32-bit float, and FPV did not ask what happens then.
- **DPR** (`plans/dpr-plan.md`): reversed-Z (w = n/d in binary32) has a relative step between 2^(−24) and 2^(−23) at every
  distance; log depth and the standard buffer as the reader's and the in-place lay.
- **The real-form Cayley.** The landing point's real form is q = (x − 1)/(x + 1) = tanh(u/2), with x = d/f and u = ln x:
  the focus at 0, the near half on (−1, 0), the far half on (0, 1). A binary32 float is densest at 0, so a signed float
  depth with the focus at 0 should be very fine there. This is my derivation for the plan, not something run.
- **Engines.** Depth-precision practice is well studied (reversed-Z and floating depth, log depth, the loss of precision
  from mapping OpenGL's [−1, 1] onto [0, 1]); I know it from memory and checked no source for this plan. WebGL clamps
  fragment depth to [0, 1], and a signed depth buffer needs an unrestricted depth range (an extension in desktop GL and
  Vulkan, from memory, not checked). WebGL guarantees only 16-bit fixed-point depth (DEPTH_COMPONENT16); WebGL2 adds
  24-bit fixed point and 32-bit float.
- draw's labs are not attached to this session and were not checked.

## Schemes

Distance d, focus f, x = d/f, u = ln x. The relative separation r(d) is Δd/d to the next distinct stored value farther
(in nats, the same as Δu to first order).

Binary32 (round to nearest, exact values to 50 digits, neighbours by IEEE next-after):
- **RZ32**, reversed-Z: w = n/d, n = 10⁻⁶ f.
- **T32**, the turn: g = (2/π)·arctan(x).
- **C32**, the Cayley, signed: q = (x − 1)/(x + 1).
- **S32**, reversed-Z shifted to the focus, signed: z = 1/x − 1 (screen-linear, so a projection matrix can produce it).

16-bit fixed point (2¹⁶ equal steps on [0, 1]), near n = 10⁻³ f, far 10³ f:
- **Z16**, the standard buffer: w = (1/n − 1/d)/(1/n − 1/far).
- **L16**, log depth: w = ln(d/n)/ln(far/n).
- **T16**, the turn: g = (2/π)·arctan(x).

## Predictions (Part A, exact arithmetic; written before any run)

From the closed forms: Δu = ulp(stored)/|d stored/du|.

- **F1 (RZ32 constant).** r ∈ (2^(−24), 2^(−23)] at every tested d, 10⁻⁵ f to 10⁶ f. (DPR D2; a check of the code.)
- **F2 (the turn does not survive floats).** T32 at the focus has r = π·2^(−24) = 1.87·10⁻⁷ (to 1%), coarser than RZ32's
  largest step; at every d ≥ f T32 is coarser than 2^(−23); on the near side it is never finer than 2^(−24). FPV's
  fixed-point advantage does not carry to binary32. *Killed* if T32 is finer than 2^(−24) anywhere, or finer than
  2^(−23) anywhere at d ≥ f.
- **F3 (the Cayley in a signed float).** C32 has r ∈ (sinh|u|·2^(−24), sinh|u|·2^(−23)], to 1%, for 10⁻³ ≤ |u| ≤ 15.
  It is finer than RZ32 for certain where |u| < asinh(½) = 0.481 nats (d from 0.62 f to 1.62 f), coarser for certain
  where |u| > asinh 2 = 1.444 nats (beyond 0.236 f and 4.24 f). Things farther than e^18.02·f (or nearer than
  e^(−18.02)·f) all round to ±1, one value each side. A pair at f(1 ± ε) is told apart for any ε down to the floats'
  smallest normals. *Killed* if any tested r falls outside the stated interval by more than 1%, or the merge point is off
  by more than 0.1 nats.
- **F4 (reversed-Z moved to the focus).** S32 has r ∈ (|1 − x|·2^(−24), |1 − x|·2^(−23)] to 1%: finer than RZ32 for
  certain on x ∈ (½, 3/2), coarser for certain at x > 3, and like RZ32 (within a factor 2) as x → 0. *Killed* as F3.
- **F5 (16-bit fixed point, where the layout should matter).** At the focus: T16 r = π·2^(−16) = 4.79·10⁻⁵, L16
  ln(10⁶)·2^(−16) = 2.11·10⁻⁴ (4.40 times T16's), Z16 1.53·10⁻² (about 318 times T16's). T16 finer than L16 for
  |u| < acosh(ln(10⁶)/π) = 2.16 nats. *Killed* if any of the three focus values is off by more than 2%, or the band edge
  by more than 0.05 nats.

**The prediction in words.** In binary32 depth, which is what engines use on desktop, reversed-Z is already within a
factor 2 of the float's own grain everywhere, so the reframe can only buy a narrow band about the focus (C32, about half
a nat each side), at the cost of coarser depth past about 1.4 nats and a depth buffer WebGL cannot hold. The turn stored
in a float is worse than reversed-Z at the focus. In 16-bit fixed point the turn about the focus is 4.4 times finer than
log depth there and over 300 times finer than the standard buffer, within about 2.2 nats either way. So I expect the
reframe to matter for 16-bit depth (WebGL's one guaranteed format, mobile, shadow maps) and hardly at all for 32-bit
floats.

## Part B (on a GPU through WebGL2; written before any run)

Headless Chromium, WebGL2, a 256 × 256 target. Two parallel quads square to the look, the far one at d(1 + δ) drawn
first, the near one at d drawn second with depth test LESS; z-fighting is the share of pixels showing the far quad.
For each scheme and d (eight distances, 10⁻² f to 10² f), δ is scanned down in steps of 2^(¼); δ* is the smallest δ with
fighting under 1%.

- Schemes on the GPU: Z16 by the projection; L16 and T16 by writing gl_FragDepth into DEPTH_COMPONENT16; RZ32 and T32 by
  writing gl_FragDepth into DEPTH_COMPONENT32F (so the buffer's storage is tested, not WebGL's projection). C32 and S32
  are signed and WebGL clamps depth to [0, 1], so they are not tested on the GPU.
- **F6.** δ* within a factor 2 of Part A's r(d) for each scheme at each distance. *Killed* if off by more than a factor 2
  at more than a quarter of the points.
- If WebGL2 or a format is not available in the headless browser, Part B (or that scheme) is reported as not run, and no
  replacement is chosen afterwards.

## What would and would not be shown

- F2–F6 not killed: the reframe's depth layout is worth having where depth is stored in few fixed-point bits, and
  barely where it is stored as a float; on floats its one gain needs signed depth no web renderer has.
- Not measured: the cost of writing gl_FragDepth (it turns off early depth rejection), visual quality, or a game.
- Nothing about eyes or players. Classical floating-point arithmetic; the layout is FPV's, the Cayley form ours.

## Runs

### Run 1, Part A (13 November; `python3 -I runs/fdz/fdz.py`, under a second; output `runs/fdz/run1.txt`)

- **F1 not killed.** RZ32's r between 6.02·10⁻⁸ and 1.19·10⁻⁷ at every d from 10⁻⁵ f to 10⁶ f.
- **F2 killed, by my set-up.** T32's r at the focus is 1.404·10⁻⁷, not π·2^(−24) = 1.873·10⁻⁷. The focus value g = ½ is
  a binade edge: the cell holding ½ reaches half a step below it, where steps are half as wide, so it is ¾ of 2^(−24)
  wide, and ¾·π·2^(−24) = 1.4044·10⁻⁷ exactly (checked after the run). The other clauses held: T32 is nowhere finer than
  2^(−24), and at d ≥ f nowhere finer than 2^(−23) (1.40·10⁻⁷ at the focus, 9.5·10⁻⁷ at 10 f, 9.4·10⁻⁵ at 1000 f,
  against RZ32's 7·10⁻⁸ to 1.2·10⁻⁷). The turn stored in a float is coarser than reversed-Z at the focus and beyond.
- **F3 killed, by my set-up.** C32 met its interval at every tested point with |u| < 13.6; five points from 13.6 to 14.9
  nats fell 2–6% below it. There a cell is 2.5–8.6% wide, and where a point sits inside its cell moves r by more than the
  1% I allowed (a first-order statement given a range where first order no longer holds). The merge into ±1 came at
  ±18.022 nats, as predicted; a pair at f(1 ± ε) stays apart down to ε = 10⁻³⁰. Against RZ32: at |u| = 0.01, 0.1, 0.3 C32
  is 120, 8 and 2.5 times finer; about equal at 1 nat; 3.2, 9, 68 times coarser at 1.44, 3 and 5 nats. The same both
  sides of the focus.
- **F4 killed, by my set-up**, in the same way: eight points at u ≥ 12.5 (x ≥ 2.7·10⁵) 1–8% below the interval, none
  elsewhere. S32 is 17 and 8 times finer than RZ32 at 0.9 f and 1.1 f, 2.5 and 1.9 times at 0.5 f and 1.5 f, about equal
  near the camera, 2.1 times coarser at 3 f and 67 times at 100 f.
- **F5 not killed.** At the focus T16 4.794·10⁻⁵, L16 2.108·10⁻⁴ (4.40 times), Z16 1.525·10⁻² (318 times); the band
  edge where T16 meets L16 at 2.161 nats, as predicted. At 0.1 f and 10 f T16 (2.42·10⁻⁴) is just past L16 (2.11·10⁻⁴);
  at 0.01 f and 100 f it is 11 times coarser.

**In short.** In 32-bit floats, the turn about the focus is worse than reversed-Z: it should not be stored as a float.
Storing depth as the signed Cayley q = (x − 1)/(x + 1), with the focus at the float's zero, gains up to two orders near
the focus and loses past about one nat each side; it needs signed depth, which WebGL does not allow. In 16-bit fixed
point the turn about the focus is 4.4 times finer than log depth at the focus and 318 times finer than the standard
buffer, within about two nats either side.

### Run 1, Part B (13 November; `node runs/fdz/gpu.mjs`, then `python3 -I runs/fdz/gpu_score.py`; output `runs/fdz/gpu-run1.json`, `gpu-run1.txt`)

Headless Chromium's WebGL2 (SwiftShader, renderer "WebKit WebGL"); DEPTH_COMPONENT16 and DEPTH_COMPONENT32F both
complete; all five schemes ran at the eight distances.

- **F6 killed, by my set-up.** δ* was outside [r/2, 2r] at 22 of 40 points (limit 10). δ* is how far d sits below the top
  of its stored cell, anywhere in (0, r], not the cell's width, so a factor-2 band about r was the wrong test: δ*/r ran
  from 0.00 to 1.54, never much past 1 (the scan's step is 2^(¼), and d is rounded to binary32 on the way in).
- **Post hoc, not a test:** a CPU replay of the same scan (d rounded to binary32, the scheme in float64, stored as 16-bit
  unorm or binary32) gives the GPU's δ* exactly at 35 of 40 points. The five misses are L16 at 0.01 f and 100 f and T32
  at 1.93 f, 26.8 f and 100 f, where the shader computes log or atan in float32. There the computation's own rounding is
  as large as the stored step, so storing the turn in a float is worse than Part A's storage-only figure: at 100 f the
  GPU's T32 needs δ ≈ 1.1·10⁻⁵, against 1.2·10⁻⁷ from storage alone. Every 16-bit fixed-point and reversed-Z point
  matched the arithmetic.

**Overall, run 1.** The 16-bit case came out as predicted (F5), and the GPU stores what the arithmetic says. In 32-bit
floats the turn about the focus is no gain (F2's sense), and the one float layout that gains at the focus (the signed
Cayley, F3) cannot be held in a WebGL depth buffer. Kills: F2, F3, F4, F6, all by my set-up (a binade edge at the focus;
a first-order tolerance applied where cells are several percent wide; a width test applied to a distance to a cell's
edge). Not tested: the cost of writing gl_FragDepth, a real scene.
