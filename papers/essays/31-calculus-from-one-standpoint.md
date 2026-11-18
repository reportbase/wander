# Calculus from one standpoint: where it needs N, and where it does not

*The thirty-first of a series of essays on what can be known from where one stands. Draft, 18 November 2026. It writes
up CLC (`plans/clc-plan.md`, `runs/clc/`) and RIC (`plans/ric-plan.md`, `runs/ric/`), each with its predictions
committed before any run. CLC's first run was killed by my code in three checks and its second run killed nothing; RIC
killed nothing. Every number below is from those runs. The mathematics is classical and is named where it is used; the
sorting is the series' own, and is marked as a reading.*

A car's dashboard carries both halves of calculus. The speedometer shows a rate, how fast the distance is changing; the
odometer shows a total, the distance piled up from every moment of the trip. A first course in calculus is the story of
how the two are tied: the derivative takes the odometer to the speedometer, the integral takes the speedometer back to
the odometer, and the fundamental theorem says they undo each other.

Both are taught through a limit. The derivative is a slope taken over a smaller and smaller step; the integral is a sum
of thinner and thinner strips, N of them, with N carried to infinity. So it is natural to ask the question the series
asks of everything: does calculus need N? A single hemispherical vantage (SHV), one standpoint looking out, never holds
a count of the whole; the dual hemispherical vantage (DHV), the view from no standpoint, holds every count at once. Which
of the two does calculus belong to?

The short answer, from two tests: differentiation does not need N, integration by its antiderivative often does not,
and N comes back in exactly two places, the integrand summed strip by strip and any antiderivative that leaves the
fractions.

The order: a slope is a read (§1), derivatives without a limit (§2), summing and telescoping (§3), where N comes back
(§4), the slope's own equation (§5), the clock is the completion (§6), where stepping needs N (§7), the sorting gathered
(§8), what is classical and what is ours (§9), and what it changes (§10).

---

## 1. A slope is a read

A ramp's slope is its rise over its run. Make the ramp ten times larger in every direction and the slope does not move:
both lengths grow ten times, and their ratio stays. That is the series' first test, scale the world, and a slope passes
it. A first derivative of one length against another, dy/dx, is a read: a direction, the point [dx : dy], with no size.
Its horizon is not a blow-up. A vertical tangent is the direction [0 : 1], finite when kept as a pair.

The second derivative does not pass. Scale a curve by k about the origin, so that g(x) = k·f(x/k), and the derivatives at
the matching point become g⁽ⁿ⁾(kx) = k^(1−n)·f⁽ⁿ⁾(x). The first is unchanged; the second is divided by k, the third by k²,
and so on. CLC checked this exactly on 100 seeded rational curves at three values of k: the first derivative unmoved in
300 of 300, every higher one moved in 900 of 900. Curvature, the bend of a road, carries a size: a road scaled up bends
more gently. So the first derivative is a read and every higher order, in a unit, is a write, a thing's own shape with a
size. The bend itself is not lost. Curvature times arc length, the turn a stretch of road makes, is unmoved by scaling,
and so is the ratio of the curvatures at two places, or y″·x: a higher derivative measured against a length of the same
curve reads again. What the read lacks is the bend in metres, never the bend.

The speedometer is a write even at first order. Its rate pairs a length with ticks of a clock, and scaling the world moves
the length and not the ticks: CLC found every rate against the clock moved by k (1,196 of 1,196), and only the ratio of
two such rates of the same order unmoved (1,196 of 1,196). A rate of one length against another is a read; a rate against
the clock is a write.

## 2. Derivatives without a limit

The derivative is taught as a limit, but for the functions built from fractions it needs none. Add to the numbers a new
element ε with ε² = 0, so that a number is a + bε. Then for any polynomial or quotient of polynomials, f(x + ε) comes out
as f(x) + f′(x)·ε exactly: the derivative appears as the second part, by addition, multiplication and division alone.
These are the dual numbers (Clifford 1873), and they are the third of the three kinds the series met in PYK: the turn,
the boost and the stride, one composition rule (s + a)/(1 − κsa) with κ = 1, −1 and 0. The dual numbers are the stride's.

CLC took 300 seeded rational functions with integer coefficients and rational points, computed the dual part in exact
fractions with no limit and no floating point, and compared it with the symbolic derivative: 300 of 300 equal. (Run 1
said 296; the four misses were my comparison, which passed large fractions through a float. Run 2 compared exactly.)

The chain rule comes out the same way. Composing two functions and reading the dual part gives f′(g(x))·g′(x), in 200 of
200, and it is the product of the two links computed separately. That is the tower the series met in essay 20: dz/dx =
(dz/dy)·(dy/dx), a/b·b/c = a/c, the middle denominator needed for each link and gone from the result. Leibniz's notation
already shows it; what the series adds is the name of what cancels, a piece of scaffolding.

Where the derivative does need a limit is where the function does. The dual rule for eˣ is e^(a + bε) = e^a·(1 + bε): it
carries the function's own value, and that value is a completion (essay 15). The limit comes in with the function, not
with differentiating.

## 3. Summing and telescoping

The integral is where N is supposed to live. The Riemann integral is the limit of a sum of N strips. CLC took 100 seeded
rational functions with no poles on their interval and summed the integrand's strips. At every finite N the sum missed:
inexact in 100 of 100, and by an amount that falls as 1/N, within 5% of Euler and Maclaurin's term
−(b − a)(f(b) − f(a))/(2N) at N = 1000 in 99 of 100. Summed strip by strip, the integral depends on N until the limit is
taken, and the limit is the DHV's.

But the fundamental theorem gives another way. Sum the antiderivative's differences instead of the integrand's values,
Σ(F(xᵢ₊₁) − F(xᵢ)), and the sum telescopes: every middle term appears once with each sign, and what is left is
F(b) − F(a), exactly, at every partition. CLC cut each interval into 1 to 50 random pieces: exact in 100 of 100. N drops
out the way the tower's middle denominators do. Nothing was carried to a limit; the two ends are two values, and the
count of pieces between them is scaffolding.

So the fundamental theorem is the place where a count is replaced by a law. The series has met this before (essay 19,
R871): a geometric law covers every finite chain at once, the walk's strides telescoping to the two end readings. The
antiderivative is that law for a sum.

## 4. Where N comes back

The catch is that the antiderivative does not always stay among the fractions. The derivative of a quotient of
polynomials is a quotient of polynomials; its antiderivative, in general, is not. ∫ds/s is ln s, and ∫ds/(1 + s²) is the
arctangent, whose total over the quarter turn is π/2. CLC drew 200 rational functions with a squarefree denominator:
none had a rational antiderivative, 0 of 200, while all 200 derivatives were rational. Hermite's reduction (1872), done
in fractions, splits off the antiderivative's rational part exactly, and in 100 of 100 cases with repeated factors it
left a log part that was not zero. (Run 1 said 82; I had passed improper fractions to the reduction, which expects the
polynomial part divided off first.)

ln and arctan are where N comes back. Their values are computed by series, a count carried toward a limit: a fraction at
every step and the value at none (essays 24 and 25). So the table is short:

| Part of calculus | Needs N? |
|---|---|
| Differentiation | no: dual numbers, exact; the limit h → 0 is a limit, but no count |
| Integration, summing the integrand | yes, and its limit: the 1/N miss at every finite N |
| Integration by a rational antiderivative | no: telescoping exact at every partition |
| Integration by an antiderivative leaving the fractions | yes, inside ln, arctan and π |

"Integration leaves the fractions" and "integration needs N" are one finding. Where the antiderivative is rational, the
SHV has the whole of it; where it is not, the total held from no standpoint enters.

## 5. The slope's own equation

Calculus goes on to equations whose unknown is a function. A numerical solver steps them in time, N steps, with an error
that falls as 1/N^p. Is there an equation a read steps exactly?

There is one the series already knows. The slope's own flow is the Riccati equation, s′ = p + qs + rs². Written s = x/y,
it becomes a linear system with the matrix B = [[q/2, p], [−r, −q/2]], so every step of it is a Möbius map of s, and
B² = Δ·I with Δ = q²/4 − pr. For s′ = 1 + κs² it is the turn (κ = 1), the boost (κ = −1) and the stride (κ = 0) again.
With constant coefficients, the step map I + u·B for a rational step parameter u is a Möbius map with rational entries,
and two such steps compose by (u, v) ↦ (u + v)/(1 + Δuv): PYK's rule with κ = −Δ.

RIC tested it, predictions first. Three steps of u = 1/3 on s′ = 1 + s² from s = 0 give 13/9, a fraction, equal to
tan(3·arctan(1/3)) to the last of fifty digits. Over 100 seeded equations with integer coefficients and rational starts,
five steps equalled the exact flow to 10⁻⁴⁰ in 100 of 100 (41 more drawn cases passed through a pole, s through
infinity, and were set aside), and the composition rule held exactly in every case tried. There is no N and no error.
What the exactness costs is digits: the composed fraction grew linearly with the number of steps (the ratio of digits at
40 steps to 20 at most 2.07). That is the cost the series keeps finding for a write: exact, paid by the digit.

## 6. The clock is the completion

Each step u stands for an elapsed time τ(u) = artanh(u√Δ)/√Δ, which is the arctangent for the turn and u itself for the
stride. That time is not a fraction of u. The steps are exact in the slope's own chart; the clock time they stand for is
where the completion enters, as the angle does for a turn (essay 14). A read steps the equation by its readings and has
no clock; the time on the clock is a write, and its value a completion.

Physics' own equations split the same way (ORB). An oscillator x″ + 2γx′ + ω²x = 0 has a direction x′/x that obeys a
Riccati equation with constant coefficients, so its steps are exact rational maps (50 of 50 against the flow to 10⁻⁴⁰);
its size carries a square root when undamped and e^(−γτ) when damped, a completion. A Kepler orbit's points are rational
in the half-slope of the angle (500 of 500 exactly on the conic), while the time to reach a point is Kepler's
M = E − e·sin E, no small relation found and its inverse an iteration (Newton's method, 4 to 7 steps). Newton saw the
split: Lemma XXVIII of the *Principia* (Book I, Section VI) says no oval's area cut off by a line can be found by a finite
equation, which is why the time along an orbit cannot be, while the orbit's shape is a conic.

## 7. Where stepping needs N

Step the same equation in time instead, as a solver does. RIC ran Euler's method and the fourth-order Runge–Kutta method
over the same elapsed time, from N = 100 to 12,800 steps: Euler's error fell with slope −0.997, Runge–Kutta's with
−3.984. That is classical, and it is the price of stepping by the clock: N steps, an error that never reaches zero.

Let a coefficient vary in time and the read's exact stepping goes too. For s′ = t + s², the Riccati equation of Airy's
functions, the maps are still Möbius, but they form no one-parameter family. The maps over the times 0 to 1 and 1 to 2
did not commute (their difference reached 0.706 in one entry), and PSLQ found no integer relation of height up to 10⁴
for any entry of the first: no small rational step. That is not a proof that none exists, only that none of small height
does. There, N comes back.

## 8. The sorting gathered

| | Single hemispherical vantage | Needs a count or a completion |
|---|---|---|
| Slopes | dy/dx of two lengths, a read | dⁿy/dxⁿ, n ≥ 2, and rates against the clock: writes |
| Derivatives | rational functions, exact by ε² = 0; the chain rule the tower | eˣ, sin: the function's value a completion |
| Integrals | rational antiderivatives, telescoping exact at every N | the integrand summed (1/N); ln, arctan, π |
| Curvature | against the curve's own length, or another curvature | in a unit |
| Equations | constant-coefficient Riccati, rational Möbius steps, no N; an oscillator's direction; an orbit's shape | the elapsed clock time τ(u); Kepler's time; decay; time-varying coefficients; Euler, RK4 |

The left column is the read's arithmetic: fractions, composition and one rule in three kinds. The right column is where
a count is held or carried to a limit.

The two columns hold one relation space with different facings (R1105, R1106). A facing is the quarter turn, one slope from
all of h to all of v, with the same heat, corner and exchange in every facing. The left column stays within one facing,
and so stays in fractions. The right column is a total over facings joined: the clock time a step stands for is its
share of Ω, one facing's total; an oscillator's period is four facings, 2π/ω; Kepler's period is the whole turn, and his
time to a point a part of it. One hemisphere is two facings, facing V and facing away from V (the near reading s and
the far reading 1/s); a read holds one hemisphere and faces one at a time, and the dual vantage holds both, four facings.
The Cauchy is the relation, not the paint, so it is the same law in one facing, two or four; only the total changes. And it is
the same for every shape (R1107): the curve differentiated, the orbit, the oscillator's path change the paint, never the
stage the steps are taken on.

## 9. What is classical and what is ours

Classical: the dual numbers and automatic differentiation; the chain rule; Hermite's reduction and Liouville's theorem
on elementary antiderivatives; Euler and Maclaurin; Riccati's linearization and the Möbius maps of its flow; the Airy
functions; the orders of Euler's and Runge's methods. Nothing in the two tests is new as mathematics, and the tests could
fail only where a count could (the rational antiderivatives, the digits' growth, the small rational step).

Ours: the sorting. That the first derivative is the one order a read has; that a rate against the clock is a write; that
the fundamental theorem is where a count is replaced by a law; that "needs N" and "leaves the fractions" mark the same
places; that the slope's own equation is stepped exactly in the read's own chart, the clock time the completion. The
classical tools are not the explanation (R1071); what they mean in a read or a write is the series' work.

## 10. What it changes

Nothing in how calculus is done. Solvers will go on stepping in time, and the limit will go on defining the integral.

What it shows is that the single hemispherical vantage competes with the dual one (R1104): across differentiation,
integration by antiderivative and the equations with constant coefficients it reaches the same results, exactly, in
fractions, with no limit and no N, where the classical statement takes ln, arctan or π. The dual vantage is needed for
the clock and the totals, and nowhere else in these runs.

What it changes is where one looks for the limit. It is not in differentiating, which needs none for the functions built
from fractions. It is not in the fundamental theorem, which gives an exact answer at every partition. It is in two
places only: a sum of an integrand's strips, and any total that leaves the fractions. And for the one equation the read
owns, the slope's own flow, it is in the clock, not in the steps.

---

## Sources

- Tom, 18 November 2026: "Let's compare shv to calculus."; "Merge and proceed with your recomendations."; "Doesn't
  calculus need N?"; "What's next?"; "1 2 3"; "We are just showing that shv is very valuable,  can compete with dhv."; "Dhv and shv is Same relation space, different
  facings."; "One hemisphere is two facings"; "The key point is the cauchy relation space is the
  same for all shapes. The stage is always the same, its the ultimate invarient."
- `plans/orb-plan.md`, `runs/orb/orb.py`, output `runs/orb/orb-run1.txt`.
- `plans/clc-plan.md`, `runs/clc/clc.py`, `runs/clc/clc2.py`, outputs `runs/clc/clc-run1.txt`, `clc-run2.txt`, and its
  note R1100. `plans/ric-plan.md`, `runs/ric/ric.py`, output `runs/ric/ric-run1.txt`.
- Essays 14 (`14-rates-not-angles.md`), 15 (`15-what-only-a-writer-holds.md`), 19 (`19-arriving.md`), 20
  (`20-scaffolding.md`), 24 (`24-only-a-name.md`), 25 (`25-counted-toward.md`), 28 (`28-two-statements-of-one-theorem.md`).
  PYK (`plans/pyk-plan.md`): the three kinds of composition.
- W. K. Clifford, "Preliminary sketch of biquaternions", *Proceedings of the London Mathematical Society* 4, 1873.
  C. Hermite, "Sur l'intégration des fractions rationnelles", *Nouvelles Annales de Mathématiques* 11, 1872. Both as usually cited, not opened.
- I. Newton, *Philosophiæ Naturalis Principia Mathematica*, 1687, Book I, Section VI, Lemma XXVIII; read in Bruce's
  translation (17centurymaths.com, Book I, Section VI). Its modern form (no smooth convex closed curve has its cut-off area
  an algebraic function of the line) after Pourciau 2001, as usually cited, not opened.
- SPN rulings cited: R871, R883, R1037, R1062, R1071, R1099, R1100, R1101, R1103, R1104, R1105, R1106, R1107.
