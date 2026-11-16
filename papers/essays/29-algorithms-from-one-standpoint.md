# Algorithms from one standpoint: what a line on a screen and a calculator's sine button already knew

*The twenty-ninth of a series of essays on what can be known from where one stands. Draft, 16 November 2026. It writes
up ALG (`plans/alg-plan.md`, `runs/alg/`), sixteen predictions committed before any run, fifteen not killed in run 1,
the sixteenth killed and a second prediction not killed in run 2. Every number below is from those runs. The algorithms
are classical and are named where they are used; the sorting is the series' own, and is marked as a reading.*

Draw a straight line on a screen of pixels and it comes out as a staircase. Somewhere a program decided, for every
column, which pixel the line goes through, and it did so without ever dividing, without an angle and without a rounding
error. Press the sine key on a pocket calculator and something similar happens: a few dozen shifts and additions, and a
number appears.

Both are old algorithms, Bresenham's line (1965) and CORDIC (Volder 1959), and both are still everywhere. Neither was
designed from a standpoint. But looked at from one, they turn out to have done what the series keeps finding a single
vantage does: they kept a pair where a single number would have lost something, they composed slopes instead of adding
angles, and the one place each needs a completed whole is exactly the place a single vantage cannot reach.

Essay 28 sorted classical theorems three ways: those that come through whole from one standpoint, those that come
through only by renaming a constant, and those that do not come through at all because they state a completion. This
essay does the same for algorithms, with a test behind each entry.

The order: the two ways of computing (§1), the line (§2), the pair kept (§3), turning without drifting (§4), the
calculator's two parts (§5), the one prediction that failed (§6), order kept (§7), the horizon held (§8), what has no
single-vantage form (§9), the sorting gathered (§10), what is classical and what is ours (§11), and what it changes
(§12).

---

## 1. Two ways of computing

**From no standpoint**, the dual hemispherical vantage (DHV), the blueprint: the quantity is an amount in a frame that
holds everything at once. A direction is an angle measured round the whole turn; a point is three coordinates; a line is
y = mx + c with m a real number; a set of values is summarised by its mean.

**From one standpoint**, the single hemispherical vantage (SHV): a direction is a slope, v/h, or better the pair
[h : v] itself; turning is composing slopes, s ⊕ a = (s + a)/(1 − sa); a far point is a direction and how far its
reading has to go; values are kept by their order.

The two agree where both apply. They differ in what goes wrong when the computation is finite, and that is what the test
measured.

## 2. The line

Bresenham's algorithm draws from (0, 0) to (dx, dy) with one integer, the error D = 2·dy − dx. At each column it steps
up when D > 0 and adjusts D by whole numbers. The slope dy/dx is never formed. It is kept as the pair (dx, dy), and
the comparison that would need it is done by multiplying across.

The test: 1,000 seeded segments with dx up to a million. At all 1,061,045 points checked, Bresenham's pixel was the exact
line rounded half down (B1). The same line computed the blueprint's way, y = (dy/dx)·x in binary floating point and
rounded, missed the exact line at 8 of them (B2). Eight in a million is small, but it is not zero. Checked afterwards, every miss is a case where the exact answer is a
tie, x·dy/dx landing exactly on a half, and the floating-point division put it a hair to the wrong side.

**Kind: already single-vantage.** The slope as a pair of whole numbers, no division, exact.

## 3. The pair kept

Every library has two arctangents. atan(y/x) takes a single number, the slope. atan2(y, x) takes the pair.

The test (T1): over 10,000 seeded directions round the whole circle, atan(y/x) gave a direction and its opposite exactly
the same value, every time. Dividing y by x throws away which way the pair faces, since (−y)/(−x) = y/x. atan2 kept them
π apart. And at x = 0, the horizon of the slope, dividing raised an error in both floating-point and exact arithmetic,
while atan2 returned ±π/2 (T2).

In the series' terms, the slope v/h is a chart of the pair [h : v], and a chart loses the facing and sends the horizon
to infinity. The pair keeps both. atan2 is the classical admission that the pair is what has to be carried.

**Kind: already single-vantage**, provided the pair is kept. The lesson comes back in §6.

## 4. Turning without drifting

Turn the point (1, 0) n times by a small rotation and then n times back. The blueprint's way: cos θ and sin θ in
floating point, θ = 2·atan(1/8). The single vantage's way: the rational turn (63/65, 16/65), whose half-slope is
exactly 1/8, composed in fractions.

The test (R1, R2): the rational turn came back exactly, error 0, at n = 10, 100, 1,000 and 4,000. The floating-point
turn came back off by 4.2·10⁻¹⁵ after a thousand, 3.4·10⁻¹⁴ after ten thousand and 2.9·10⁻¹³ after a hundred thousand,
growing about as n.

The exact return has a price, and the run measured it: the fractions' denominators grew to 19, 182, 1,813 and 7,252
digits, against n·log₁₀ 65 = 18.1, 181.3, 1,812.9 and 7,251.7 predicted. Exactness is paid in digits, at a known rate.
The walk on `thumbs-walk.html` paid it another way, by holding the heading as one whole number of half-slope steps, so
that the return is exact and the digits never grow (TWK run 12).

**Kind: a blueprint form and a single-vantage one.** Turning by an angle drifts; composing rational slopes does not.

## 5. The calculator's two parts

CORDIC turns a vector by a sequence of fixed small turns, each with slope ±2⁻ⁱ:

  x ← x − σ·y·2⁻ⁱ, y ← y + σ·x·2⁻ⁱ.

Multiplying by 2⁻ⁱ is a shift, so each step is two shifts and two additions. It is used for sines, cosines and
arctangents where multipliers are dear.

Looked at from one standpoint it has two parts that come apart cleanly.

**The direction.** Each step composes the vector's slope with ±2⁻ⁱ by tangent addition. The test (C1): in 200 seeded
cases, the final y/x was exactly the composed slope, s ⊕ σ₀ ⊕ σ₁/2 ⊕ …, in fractions, every time. Nothing else is
needed for the direction.

**The length.** Each step also stretches the vector, by √(1 + 4⁻ⁱ). The test (C2): the length squared grew by exactly
∏(1 + 4⁻ⁱ). To give a rotation rather than a rotation and a stretch, CORDIC multiplies at the end by the gain

  K = ∏ 1/√(1 + 4⁻ⁱ) = 0.6072529350…,

an infinite product, a completion. It reached that value to ten digits by thirty steps (K₃₀ = 0.607252935009).

The gain touches only the length, an amount. The direction never needed it. So CORDIC is a single vantage's algorithm
for the direction, with one blueprint constant attached to correct the amount; anyone who wants only the slope, or only
which way a vector points, can leave the gain out.

## 6. The one prediction that failed

CORDIC has a second dependence on the blueprint. To turn through a target angle θ it keeps the angle still to go,
z = θ − Σ σⱼ·atan 2⁻ʲ, and chooses each σᵢ by the sign of z. That needs a table of arctangents, angles measured round
the whole turn.

I predicted the table was not needed: that choosing σᵢ by the sign of the slope still to go, the target's slope minus
the current slope by tangent subtraction, (T − s)/(1 + Ts), would give the same choices for every target (C3).

It did not. The choices matched for 891 of 1,000 targets, and every one that differed had |θ| greater than 1.5718
radians, just past the quarter turn. Past a quarter turn a single slope can no longer say which side of the target the
vector is on, since a slope and its opposite are one number. It is atan's failure from §3 again: the facing is lost when the pair is divided
into one number.

The kill stays recorded. A second prediction (C3′, run 2), on fresh targets, kept the slope still to go as a pair, its
numerator x·b − y·a with the target as the pair (b : a). That gave the table's choices for 1,000 of 1,000. One caution
the plan states: the test made its targets from angles, by cos and sin, so the target was given in the blueprint's
terms. What needs no table is the steering, a sign at each step; making the target is a separate matter.

**Kind: a blueprint form and a single-vantage one**, with the condition the failure taught: keep the pair.

## 7. Order kept

The median of a set of values is the middle one. Apply any increasing map to every value, and the median moves with it:
median(f(X)) = f(median(X)). The mean does not: the mean of the cubes is not the cube of the mean.

The test (M1, M2): on 1,001 seeded values, for x³, eˣ and ln(x + 10), the median equality held exactly, while the
mean missed by 100%, 39% and 0.22% respectively. This is Theorem 6 of the series' archived paper in a computer: order
statistics are unchanged by any increasing change of the payload, sums are not.

The filtering test makes the same point with a Cauchy, the law of a uniform turn's slopes (F1, F2). On 200,000 values of
Cauchy noise taken in windows of 25, the mean filter's output was 0.969 as wide as the raw noise, by its interquartile
range: averaging 25 Cauchy values gives another Cauchy of the same width. The median filter's output was 0.209 as wide,
against a predicted 0.212.

**Kind: already single-vantage.** The median keeps the order; the mean needs the sum, and a slope's law has none.

## 8. The horizon held

A camera that tracks a far landmark can store it as three coordinates, x, y, z, or, as Civera, Davison and Montiel
proposed for monocular SLAM in 2008, as the direction it was first seen in together with the inverse of its distance,
ρ = 1/d.

The test (I1, I2): for a landmark at 10³¹⁰ and at infinity, the stored coordinates overflowed, and both the direction
and the bearing from a second camera a unit away came out as NaN. In the inverse-depth form the direction was exact and
ρ was 10⁻³¹⁰ or exactly 0, and the second camera's bearing, the direction minus ρ times the baseline, was finite and
equal to the first bearing: at the horizon there is no parallax, and the form says so.

**Kind: already single-vantage.** The direction kept, the horizon a value of ρ rather than an overflow.

## 9. What has no single-vantage form

Two of the tests found completions with no single-vantage form at all.

**CORDIC's gain** (§5): a product carried to its limit, acting only on the length.

**The discrete Fourier transform.** The DFT of N samples multiplies by the N-th roots of unity, e^(2πik/N). For an
exact transform in fractions, their cosines and sines would have to be rational. The test (N1), by minimal polynomials:
cos(2π/N) is rational only for N = 1, 2, 3, 4 and 6, and cosine and sine are both rational only for N = 1, 2 and 4
(Niven 1956). For every other N the transform needs the turn completed and cut into N equal parts, which is the
blueprint's.

The mean (§7) belongs here too: it is a sum over everything, divided by how many there are.

## 10. The sorting gathered

| algorithm | from no standpoint | from one standpoint | what the run found |
|---|---|---|---|
| drawing a line | y = (dy/dx)·x in floats | Bresenham: the slope as an integer pair | exact at 1,061,045 points; floats 8 misses |
| the arctangent | atan(y/x) | atan2(y, x): the pair | the facing and the horizon kept |
| repeated turns | cos θ, sin θ in floats | rational turns composed | exact return, digits n·log₁₀ 65; floats 2.9·10⁻¹³ at 10⁵ |
| CORDIC, direction | — | slopes composed, s ⊕ σ·2⁻ⁱ | exact in 200 of 200 |
| CORDIC, steering | an arctangent table | the slope still to go, as a pair | single slope 891 of 1,000 (killed); pair 1,000 of 1,000 |
| CORDIC, length | the gain K | none | a completion, 0.6072529350 |
| summarising | the mean | the median | median exact under every map; mean off by up to 100% |
| filtering Cauchy noise | mean filter | median filter | 0.969 against 0.209 of the raw width |
| a far point | x, y, z | direction and ρ = 1/d | NaN against exact at 10³¹⁰ and ∞ |
| the DFT | roots of unity e^(2πik/N) | none | exact in fractions only for N = 1, 2, 4 |

The pattern is the one essay 28 found for theorems, now with a way the algorithms fail. Where the blueprint's form
divides a pair into a single number, adds angles or forms an amount, it misrounds, drifts, loses the facing or
overflows. Where the single vantage's form keeps the pair, composes the slopes or keeps the order, it was exact in every
case tested, paying in digits where it paid at all. And where an algorithm needs a completion, a product carried to its
limit, the turn cut into N parts, a sum over everything, there was no single-vantage form to find.

**A reading.** The tests check each algorithm's behaviour exactly; the sorting into kinds is the series' own, and other
cuts are possible. The single-vantage forms are not offered as faster or better: several are slower (fractions grow,
exact arithmetic costs), and the classical engineering that uses floating point does so knowingly, with fixes of its own
(essay 22, PWL). What the sorting says is where each kind of failure comes from.

## 11. What is classical and what is ours

Classical: every algorithm, and every fact the runs confirmed about them. Bresenham's integer line (1965); CORDIC and its
gain (Volder 1959); atan2 and its handling of quadrants; the drift of floating-point rotations and the exactness of
rational ones; the equivariance of the median under monotone maps; the Cauchy's mean having the Cauchy's width; inverse
depth (Civera, Davison and Montiel 2008); Niven's theorem (1956). The citations are given from memory, except Civera et
al., which the series has read in full.

Ours: the sorting. That Bresenham, atan2, the median, inverse depth and rational turns are the single vantage's forms;
that CORDIC splits into a single vantage's direction and a blueprint's length; that its angle table can be replaced by a
sign of a pair but not of a single slope, and that the place a single slope fails is the quarter turn, the same place
atan fails; and that the algorithms with no single-vantage form are exactly the completions.

## 12. What it changes

Nothing in how the algorithms are used. Bresenham's line and atan2 will go on being used for the reasons they always
were.

What it changes is the reason one can give. Bresenham is exact because it never turned a pair into a number. atan2
works where atan fails because it keeps the facing. Inverse depth survives the horizon because it holds the direction
and lets the distance's inverse be zero. CORDIC's direction is free and its length costs a constant, because the
direction is a read's and the length an amount. And the one prediction of mine that failed, failed for the same reason
atan does: a single slope was asked to do a pair's work past a quarter turn.

---

## Sources

- Tom, 16 November 2026: "Let's find more dhv and shv comparisons with classical algorithms"; "Yes, write the plan and
  run the test"; "Yes, write essay 29".
- `plans/alg-plan.md`, `runs/alg/alg.py`, `runs/alg/alg2.py`, outputs `runs/alg/alg-run1.txt`, `alg-run2.txt`.
- Essay 28 (`28-two-statements-of-one-theorem.md`): the theorems sorted. Essay 22 (`22-god-mode-and-a-vantage.md`): the
  walk on whole numbers, TWK and PWL. Essay 12 (`12-what-an-array-is.md`) §9: what a machine can keep. Essay 24
  (`24-only-a-name.md`): notation and content.
- J. E. Bresenham, "Algorithm for computer control of a digital plotter", *IBM Systems Journal* 4(1), 1965. J. E. Volder,
  "The CORDIC trigonometric computing technique", *IRE Transactions on Electronic Computers* EC-8(3), 1959. I. Niven,
  *Irrational Numbers*, 1956. J. Civera, A. J. Davison, J. M. M. Montiel, "Inverse depth parametrization for monocular
  SLAM", *IEEE Transactions on Robotics* 24(5), 2008.
- SPN rulings cited: R326, R841, R939, R950, R1037, R1051, R1052.
