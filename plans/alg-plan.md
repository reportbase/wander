# ALG: classical algorithms from one standpoint and from none

16 Nov 2026. SPN R1052. Tom: "Let's find more dhv and shv comparisons with classical algorithms", then "Yes, write the
plan and run the test".

## The question

Essay 28 sorted classical theorems into three kinds: whole (an exact form rational in the slope), only renamed, and not
at all (completions). Do classical algorithms sort the same way? Some look already single-vantage (Bresenham, atan2, the
perspective divide, medians, inverse depth, rational turns); some have a blueprint form and a single-vantage
counterpart (rotation by angle against composing slopes; the mean against the median); some look like completions with no
single-vantage form (CORDIC's gain, the DFT's roots of unity). Each is checked here exactly or seeded, predictions first.

## Predictions (committed before any run; `runs/alg/alg.py`)

**C. CORDIC.** Iterations i = 0 … n − 1, x ← x − σ·y·2⁻ⁱ, y ← y + σ·x·2⁻ⁱ, in exact fractions.
- C1. The final y/x equals the composed slope σ₀·2⁰ ⊕ σ₁·2⁻¹ ⊕ … (tangent addition, s ⊕ a = (s + a)/(1 − sa)) of the
  start's slope, exactly, for 200 seeded σ sequences and starts (n = 24). The gain is not used.
- C2. The length squared grows by exactly ∏(1 + 4⁻ⁱ); its inverse square root K_n tends to 0.6072529350 (10 digits by
  n = 30).
- C3. Rotation mode chooses σᵢ by the sign of the angle left, z − Σσⱼ·atan 2⁻ʲ, from an arctangent table. Choosing
  instead by the sign of the slope left (the target slope ⊖ the current slope, tangent subtraction, no table) gives the
  same σ sequence for 1,000 seeded target angles in (−1.74, 1.74) rad, n = 32. Kill if any sequence differs.

**B. Bresenham.** For 1,000 seeded segments from (0, 0) to (dx, dy), 0 ≤ dy ≤ dx ≤ 10⁶ (sampled x), the integer
algorithm with D = 2dy − dx, step when D > 0:
- B1. matches the exact rational line rounded half down, ⌈dy·x/dx − ½⌉, at every x sampled (up to 2,000 x per segment),
  with no division in the loop.
- B2. A float DDA (y = (dy/dx)·x in binary64, rounded half down) disagrees with the exact line at least once over the
  1,000 segments. Kill if it never does.

**T. atan2 against atan.** For 10,000 seeded directions over the whole circle:
- T1. atan(y/x) gives d and −d the same value for every direction (the facing lost); atan2 gives values π apart (kept).
- T2. At x = 0, y ≠ 0, y/x raises in exact and float division, atan2 returns ±π/2.

**R. Rotation drift.** Rotate (1, 0) n times forward and n times back.
- R1. By the rational turn (63/65, 16/65) (half-slope 1/8) in fractions, the return is exact (error 0) for n = 10, 100,
  1,000, 4,000; the denominator's digits grow as n·log₁₀ 65 within 1%.
- R2. By binary64 cos θ, sin θ with θ = 2·atan(1/8), the return error is nonzero at n = 10³, 10⁴, 10⁵ and grows with n
  (larger at 10⁵ than at 10³).

**M. Median and mean under increasing maps.** 1,001 seeded draws, maps x³, eˣ, ln(x + 10):
- M1. median(f(X)) = f(median(X)) exactly in every case.
- M2. mean(f(X)) differs from f(mean(X)) by more than 10⁻⁶ relative for each of the three maps.

**I. Inverse depth and homogeneous points.** A point at distance d along a seeded unit direction, d = 10³⁰⁰, 10³¹⁰, ∞:
- I1. As binary64 xyz, d = 10³¹⁰ and ∞ overflow and the normalized direction is NaN; as (direction, ρ = 1/d) the
  direction is exact and ρ = 0 at ∞.
- I2. Seen from a second camera a unit baseline away, the inverse-depth form gives the bearing direction − ρ·B
  normalized, finite at ρ = 0 and equal to the first bearing; the xyz form gives NaN for d = 10³¹⁰ and ∞.

**F. Median and mean filters on Cauchy noise.** 200,000 seeded standard Cauchy values, windows of n = 25:
- F1. The mean filter's output has interquartile range within 10% of the raw noise's (2): averaging does not narrow a
  Cauchy.
- F2. The median filter's interquartile range over the raw noise's is within 15% of 0.212: the median's asymptotic
  spread for a unit Cauchy is π/(2√n) = 0.314, its interquartile range about 1.349 × 0.314 = 0.424, against the raw 2.

**N. The DFT's roots of unity.** For N = 1 … 64:
- N1. cos(2π/N) is rational exactly for N ∈ {1, 2, 3, 4, 6} (minimal polynomial of degree 1), and cos and sin of every
  2πk/N are both rational exactly for N ∈ {1, 2, 4} (Niven). So an exact DFT in fractions exists only for those N; every
  other N needs the turn completed.

Kill conditions are each prediction's own; a failed one stays failed, and a fix is a new run with its own prediction.

## Runs

**Run 1** (16 Nov, `runs/alg/alg.py`, output `runs/alg/alg-run1.txt`). The first attempt stopped at R1, n = 4,000, on
Python's limit for printing a 7,252-digit integer (my code); lifted (`sys.set_int_max_str_digits(0)`) and the whole
script run again, same seeds, before any verdict was read. 15 of 16 not killed; C3 killed.
- C1 not killed: in 200 seeded cases CORDIC's final y/x is the composed slope exactly; the gain is not used.
- C2 not killed: the length squared grows by exactly ∏(1 + 4⁻ⁱ); K₃₀ = 0.607252935009, K_∞ = 0.607252935008881.
- C3 killed: choosing σ by the sign of the slope left, (T − s)/(1 + Ts), gives the angle table's sequence for 891 of
  1,000 targets; every one that differs has |θ| > 1.5718 rad, past the quarter turn, where the single slope has lost
  the facing (the same loss as atan against atan2, T1). Post hoc, not a prediction: the slope left kept as a pair (its
  cross term x·b − y·a, the numerator of the tangent subtraction, with the target given as a pair) gave the table's
  sequence for 1,000 of 1,000, on the same seeds.
- B1 not killed: Bresenham equals the exact line rounded half down at all 1,061,045 points checked, with no division.
- B2 not killed: the binary64 DDA misses the exact line at 8 of them.
- T1, T2 not killed: atan(y/x) gives d and −d one value; atan2 keeps them π apart; at x = 0 division raises and atan2
  gives ±π/2.
- R1 not killed: the rational turn (63/65, 16/65) n times and back returns exactly at n = 10, 100, 1,000, 4,000; the
  denominator has 19, 182, 1,813, 7,252 digits against n·log₁₀ 65 = 18.1, 181.3, 1,812.9, 7,251.7.
- R2 not killed: the binary64 return error 4.2·10⁻¹⁵, 3.4·10⁻¹⁴, 2.9·10⁻¹³ at n = 10³, 10⁴, 10⁵, growing about as n.
- M1, M2 not killed: median(f(X)) = f(median X) exactly for x³, eˣ, ln(x + 10); the mean misses by 1.0, 0.39 and
  0.0022 relative.
- I1, I2 not killed: at d = 10³¹⁰ and ∞ the xyz direction and the second camera's bearing are NaN; the inverse-depth
  bearing is the direction itself, ρ = 10⁻³¹⁰ and 0 (at 10³⁰⁰ both forms finite).
- F1, F2 not killed: on Cauchy noise in windows of 25 the mean filter's interquartile range is 0.969 of the raw, the
  median filter's 0.209 (predicted 0.212).
- N1 not killed: cos(2π/N) rational only for N = 1, 2, 3, 4, 6; cos and sin both rational only for N = 1, 2, 4.

**Run 2** (prediction written before it runs): C3′, CORDIC's rotation mode with σ chosen by the sign of the cross term
x·b − y·a (the slope left kept as a pair, the target given as the pair (b : a)), on 1,000 fresh seeded targets in
(−1.74, 1.74) rad (seed 99, not run 1's), n = 32: the table's sequence every time. Kill if any differs.
