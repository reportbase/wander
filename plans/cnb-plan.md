# CNB: a cannonball, where a unit enters the shape

17 Nov 2026; SPN R1084; Tom: "what about shooting a canning ball, what that be good way to study the read/write?", then
"yes".

## The question

A ball fired at launch slope s (rise over run) at speed v₀ under one pull g. In a vacuum its shape is all read: slopes from
s at the muzzle to −s at landing, the apex at half the range and s/4 of it high (seen from the cannon at slope s/2), the
range v₀²/g times 2s/(1 + s²), the same at s and 1/s and greatest at the corner s = 1 (MOT run 2's stationary corner). How
far and how long are writes (v₀ and g carried in; R971's bounce). Air brings in a length of its own, the drag length
L = 2m/(ρ·C_d·A). Where does that length enter the shape, and does it enter through one scale-free number?

The number: β = v₀²/(g·L), the vacuum's length v₀²/g over the drag length. Quadratic drag, dv/dt = −g·ŷ − |v|·v/L,
C_d constant (no Reynolds or Mach dependence), flat ground, launch and landing at one height.

## Predictions (committed before any run)

- **C1, the vacuum (β = 0), exact.** Range share 2s/(1 + s²) of v₀²/g; apex at exactly ½ the range, height s/4 of the
  range (seen from the cannon at slope s/2); landing slope −s; R(s) = R(1/s); the best s exactly 1. Checked in exact
  fractions for s = p/q, and the integrator reproducing it to 10⁻¹⁰. *Killed* by any departure past those tolerances.
- **C2, one number.** Every scale-free output (R·g/v₀², the best slope s*, the landing slope over the launch slope, the
  apex's share of the range, the apex's slope seen from the cannon) is the same for any v₀, g, L with one β: four
  triples per β at β = 0.1, 1, 10 agreeing to 10⁻⁸. *Killed* otherwise. (By dimensional analysis this cannot fail unless
  my code is wrong; it is stated so the code is checked.)
- **C3, the corner leaves.** For β > 0 the best slope s* is below 1 and falls strictly as β grows, over β = 0.01 … 100
  (20 values even in ln β). *Killed* if any s* ≥ 1 or any rise.
- **C4, the exchange breaks toward the flat shot.** For β > 0 and s < 1, R(s) > R(1/s): of two elevations either side of
  the corner, the flatter one carries farther. Tested at s = ¼, ½, ¾ over the same β. *Killed* by any R(s) ≤ R(1/s).
- **C5, the path leans forward.** For β > 0 the landing is steeper than the launch (|landing slope| > s) and the apex lies
  past half the range (its share > ½), at s = ¼, ½, 1, 2. *Killed* by any exception.
- **C6, size.** Same material, same v₀: doubling the ball's radius doubles L (m ∝ r³, A ∝ r²), halves β, and the best
  slope moves toward the corner (s* larger) and the apex share toward ½, from β = 4 to 2 to 1. *Killed* otherwise.
- **C7, the first departure.** For small β, 1 − s* = a·β + O(β²), with a > 0, read off β = 10⁻⁴ … 10⁻²; the value of a
  not predicted, only its sign and that (1 − s*)/β settles to three digits. *Killed* if it does not settle or a ≤ 0.

## What this does not test

Real guns (C_d varies with Mach, the shell spins and lifts, the ground and air vary); firing tables are data for a later
run. Linear drag. The spotter's triangulation.

## Runs

**Run 1** (`runs/cnb/cnb.py`, output `runs/cnb/cnb-run1.txt`; scipy DOP853 at rtol 10⁻¹², the landing and the apex as
events; the best slope by Brent's method on the range).
- **C1 not killed.** In exact fractions at s = ¼, ½, ⅔, 1, 3/2, 4: range share 2s/(1 + s²), the same at 1/s, the apex at
  ½ the range and s/4 high, seen at slope s/2; integrated, all to 10⁻¹⁰, landing slope −s; best s 0.99999999.
- **C2 not killed.** Four (v₀, g, L) per β (from (1, 1) to (300, 1.62) and (0.02, 274)), every scale-free output within
  1.3·10⁻¹¹.
- **C3 not killed.** s* falls strictly from 0.99791 at β = 0.01 to 0.92192 at 0.48, 0.80002 at 2.07, 0.65170 at 8.86 and
  0.46959 at 100.
- **C4 not killed.** The flatter of each pair carries farther at every β: R(½)/R(2) 1.0256 at β = 0.1, 1.1638 at 1,
  1.4258 at 10.
- **C5 not killed.** At β = 1, s = 1: range 0.589 of v₀²/g, landing slope −1.556, the apex at 0.552 of the range, seen
  from the cannon at slope 0.562 (vacuum 0.5).
- **C6 not killed.** Radius doubled twice (β 4 → 2 → 1): s* 0.7318, 0.8035, 0.8686; the apex share at s = 1 0.6036, 0.5766,
  0.5519, both toward the corner and ½.
- **C7 killed, by my set-up.** (1 − s*)/β reads 0.2079, 0.2102, 0.2099, 0.2097, 0.2087 at β = 10⁻⁴ … 10⁻²: positive, but
  not settled to three digits. At small β the maximum is flat, so a range good to 10⁻¹² fixes s* only to about 10⁻⁶,
  which at β = 10⁻⁴ is a hundredth of the quantity read.

**Run 2 prediction** (committed before run 2). C7′: s* found instead as the root of the range's central difference
(step 10⁻⁴; the range to 10⁻¹², so the slope of the range to about 10⁻⁸ and s* to about 10⁻⁸). Then (1 − s*)/β at
β = 10⁻⁴, 3·10⁻⁴, 10⁻³ agrees to three digits, between 0.205 and 0.215. *Killed* otherwise.
