# WWP: water and wine, Jaynes's open case

*14 October 2026 (Tom's local date). After JAY (SPN R243, R244), Claude suggested von Mises's water and wine as the test
of the anchor: the case Jaynes left open as "overdetermined" (1973, §8). Tom, about 12:33: "ok, proceed". Exact
arithmetic: fractions where rational, mpmath at 50 digits elsewhere; predictions written before the script
(`wwp/wwp.py`) exists.*

## The problem and what has been said

Von Mises (1928): a liquid is wine and water, the ratio x of wine to water between two bounds; what is the chance that
x is below a threshold? In the form most of the literature uses (Mikkelson 2004; Deakin 2006, as quoted): 1/3 ≤ x ≤ 3,
P*(x ≤ 2)? Indifference over x gives 5/8; over the water-to-wine ratio y = 1/x it gives P(y ≥ ½) = 15/16. Read here:
- **Mikkelson** (2004, *Brit. J. Phil. Sci.* 55, 137–145, read in full): indifference over the quantities, the share of
  wine t = x/(1 + x) even on [¼, ¾], gives 5/6; he calls it invariant to the frame of reference and to the total.
  Averaging 5/8 and 15/16 ("super-indifference") gives 25/32.
- **Burock** (2005, PhilSci preprint; its text refused to this environment, its method as Gerville-Réache (2016) states
  it): the joint space of x and 1/x, even along the arc length of the hyperbola xy = 1 between (1/3, 3) and (3, 1/3),
  density ∝ √(1 + 1/x⁴): about 0.764.
- **Gerville-Réache** (2016, *Implications philosophiques*, read in full): every such answer satisfies
  P(x < c) + P(x < 1/c) = 1; adds that the density should vanish at both bounds and be continuous, and arrives at 15/16.
- **Deakin** (2006, *Gazette of the Australian Mathematical Society* 33(3), 200–; not reachable, quoted by Parker and
  Jeynes): any answer in ½ ≤ P* ≤ 1 can be had.
- **Parker and Jeynes** (2023, *Entropy* 25(8), 1242, read in full): maximum entropy with Benford's law, an exponential
  law in x; P* = 0.81595; its median is not at x = 1 (they say so).
- **Jaynes** (1973, §8), in his own form: "a mixture of water and wine contains at least half wine … What is the
  probability that it contains at least three-quarters wine?"; overdetermined, "the invariance group is too large, and
  no solution can conform to it".
- The log-uniform law on x (Jeffreys's rule for a ratio) was not found stated for this problem in what was read; whether
  it has been is to check.

Numbers known before writing these predictions (worked by hand while reading, stated so): 5/8, 15/16, 25/32, 5/6 and
0.764 are the literature's; ln 6/ln 9 ≈ 0.8155 (levels) and (π/4)/(arctan 3 − arctan ⅓) ≈ 0.8470 (the even turn; the
numerator is exact since arctan 2 − arctan ⅓ = π/4) were worked out in the course of choosing the predictions.

## What the anchor says, before any computing

The two unknowns are the two parties' sizes, wine and water; nothing in the statement prefers either, and nothing
gives the unit in which each is measured (volume, mass, or any other: a change of one liquid's unit multiplies x by a
constant, as Keynes's density and specific volume are each other's reciprocal). Jaynes's method, as for Bertrand: a
change of one party's unit (x ↦ λx, the bounds and the threshold with it) is the scale step; it leaves a family. The
exchange of the parties (x ↦ 1/x, the question restated as water to wine) is the second step; it picks the member.
The corpus's reading: these are the situated reader's rescaling and exchange (κ = V*/H for each party, R238, R239), and
the fixed point of the exchange is the corner x = 1.

## Predictions

- **P1. One party's unit leaves the powers; the exchange picks dx/x.** (a) A density on (0, ∞) keeps its form on every
  range when x ↦ λx (its restriction to [λa, λb], renormalized, is the image of its restriction to [a, b]) if and only
  if f(λx)/f(x) does not depend on x: the powers x^p. Of the candidates x^p (p = −3, −2, −1, −½, 0, 1), the even share
  2/(1 + x)², Burock's √(1 + 1/x⁴), the even turn 1/(1 + x²), the average (1 + 1/x²) and Parker and Jeynes's e^(−x),
  exactly the powers pass, at 200 rational (x, λ). (b) The exchange carries x^p to x^(−2 − p), so of the powers only
  p = −1, dx/x, is its own image. **Killed if** a candidate that is not a power passes (a), a power fails it, or any
  p ≠ −1 is its own image under the exchange (exact, at the 200 points).
- **P2. Fairness fixes the corner and leaves the rest open.** On [1/3, 3] every law with f(x) = f(1/x)/x² puts
  P(x ≤ 1) = ½, and so P(x ≤ 2) ≥ ½: Deakin's interval's floor is the corner. The fair ones: the average (25/32),
  the even share (5/6, Mikkelson), the hyperbola (≈ 0.764, Burock), the levels (ln 6/ln 9) and the even turn
  ((π/4)/(arctan 3 − arctan ⅓)); each has P(x ≤ 1) = ½. The unfair ones: indifference over x (5/8, P(x ≤ 1) = ¼) and
  over 1/x (15/16, ¾), each other's mirror; and Parker and Jeynes's e^(−λx) (median off 1). **Killed if** a fair law's
  P(x ≤ 1) is off ½ by more than 1e-45; Mikkelson's is not 5/6 exactly or the average not 25/32; Burock's, computed
  here from his density, differs from 0.764 in the third place; or the levels and the even turn differ from the closed
  forms above by more than 1e-45.
- **P3. Of the fair answers, only the levels survive a change of one party's unit.** Restate the problem with wine
  measured in a unit λ times larger relative to water (bounds λ/3 and 3λ, threshold 2λ) and apply each method afresh in
  the new statement. The levels give ln 6/ln 9 at every λ; the even share, the hyperbola, the even turn and the average
  each give a different number at λ = 2 and at λ = 0.99 (a density ratio near wine's to water's). **Killed if** the
  levels' answer moves by more than 1e-45 at λ = 2, 0.99, 10⁻³ or 10³, or any other fair method's answer is unchanged
  at λ = 2 to 1e-6.
- **P4. Jaynes's form has no answer in levels without a bound, and one in shares or turns.** "At least half wine"
  is x ≥ 1, the corner and everything past it; "at least three-quarters wine" is x ≥ 3. Under the levels dx/x is not
  normalizable on [1, ∞): on [1, 2^L] the answer is 1 − log₂ 3/L, which goes to 1 as L grows, and there is no answer
  without L, the number of levels held: Jaynes's verdict, with the missing number named. The even share on [½, 1]
  gives ½; the even turn on [45°, 90°) gives (90° − arctan 3)/45°. **Killed if** the levels' answer on [1, 2^L] differs
  from 1 − log₂ 3/L by more than 1e-45 for L = 2, 10, 40, or the share's or the turn's from these values.

## What the run would and would not show

It would show the bookkeeping: which proposed answers treat the parties alike (and so agree at the corner), and that
only the logarithmic one is also indifferent to the unit each party is measured in. That is Jaynes's method finishing a
case he left open, with the corpus's reading that the units are the situated reader's ignorance of each party's size.
It would not show that the unit is unspecified in the problem as von Mises meant it: if volume is given as the common
measure, a shared unit is an outside agreement (OFS §9), and Mikkelson's even share is then available as the measure of
the completed view. That is a reading of the problem, not a result.

## Runs

### Run 1 (14 October; `python3 wwp/wwp.py`, under a second)

```
P1: not killed. pass the unit's change: ['x^-3', 'x^-2', 'x^-1', 'x^-1/2', 'x^0', 'x^1']; powers their own image under the exchange: ['-1']
P2: not killed. average: P(x≤1) 0.5, P(x≤2) 0.78125; even share (Mikkelson): P(x≤1) 0.5, P(x≤2) 0.833333; hyperbola (Burock): P(x≤1) 0.5, P(x≤2) 0.763691; levels: P(x≤1) 0.5, P(x≤2) 0.815465; even turn: P(x≤1) 0.5, P(x≤2) 0.846977; over x: P(x≤1) 0.25, P(x≤2) 0.625; over 1/x: P(x≤1) 0.75, P(x≤2) 0.9375; e^(-λx) fair at no λ tried: True
P3: KILLED. levels move by 0.0; at λ = 2: levels 0.81546 -> 0.81546, even share 0.83333 -> 0.875, even turn 0.84698 -> 0.90237, hyperbola 0.76369 -> 0.65224, average 0.78125 -> 0.78125; at λ = 0.99: levels 0.815465, even share 0.832634, even turn 0.84589, hyperbola 0.765934, average 0.78125
P4: not killed. levels on [1, 2^L] = 1 - log2(3)/L to 1.34e-51 (L = 2: 0.20752, 10: 0.8415, 40: 0.96038); even share 0.5; even turn 0.409666
```

P3 killed, by the average, and not by my set-up: the prediction was wrong. Mikkelson's "super-indifference", the mean of
the answer from indifference over x and the answer from indifference over 1/x, keeps 25/32 at every unit, because each
of the two is unchanged by a change of unit (each is a power, x⁰ and x⁻², which P1 found keep their form) and so their
mean is too. P1 is about one density; the average is a rule that mixes two densities with weights fixed afresh for
each statement of the problem (on [1/3, 3] the two weigh alike only because the bounds sit evenly about 1). The other
fair methods do move (the even share 0.875, the even turn 0.902, the hyperbola 0.652 at λ = 2), and the levels do not.
Burock's value, from his density, 0.7637: his 0.764.

What separates the levels from the average is the rule Jaynes used for his scale step (1973, eq. 4): a solution on a
range, restricted to a smaller range inside it, must be the solution on the smaller range. One density for the whole
family of statements has it; a rule that renormalizes its mixture for each range need not.

**Prediction for run 2** (written before `wwp/wwp2.py` exists):
- **P3′. With Jaynes's restriction rule added, only the levels survive.** A method must give, on [a, c′] ⊂ [a, b],
  the answer its law on [a, b] gives conditioned on [a, c′]. On Deakin's bounds the levels, the even share, the even
  turn and the hyperbola pass this (each is one density), and the average fails it: conditioned on [1/3, 2], its law on
  [1/3, 3] holds its two parts as 2 : 3, where the average on [1/3, 2] holds them 1 : 1, so P(x ≤ 1) differs (P(x ≤ 1)
  on [1/3, 2] directly, against the conditioned law). With the unit's change of run 1, only the levels pass both.
  **Killed if** a single-density method fails the restriction rule at 50 random nested ranges by more than 1e-40; the
  average passes it at the stated nesting to 1e-6; or any method other than the levels passes both.

### Run 2 (14 October; `python3 wwp/wwp2.py`, a few seconds)

```
P3': not killed. restriction rule, worst gap over 50 nested ranges: levels 1.34e-51, even share 1.34e-51, even turn 1.34e-51, hyperbola 1.34e-51, average 0.181; the average on [1/3, 2] at x = 1: direct 0.6, conditioned from [1/3, 3] 0.64; unchanged by the unit: ['levels', 'average']; pass both: ['levels']
```

**What it shows.** The published fair answers to von Mises's water and wine (25/32, Mikkelson's 5/6, Burock's 0.764)
and the corpus's two drawings (the levels, 0.8155; the even turn, 0.8470) all put the median at x = 1, the corner, and
part past it; the two textbook answers are each other's mirror and favour one liquid (P(x ≤ 1) = ¼ and ¾). Fairness
fixes the corner and nothing more, so Deakin's floor of ½ is the corner. Jaynes's two steps for Bertrand finish the
case: the unit of each liquid is not given, and one law for every statement (restriction) unchanged by a change of one
liquid's unit leaves the powers of x; the exchange of the liquids picks dx/x, the levels, ln 6/ln 9 ≈ 0.8155. The
average of the two textbook answers is also unchanged by the unit, but it is no single law and fails the restriction
(run 1's kill, run 2). Jaynes's own form ("at least half wine", P(at least three-quarters)) has no answer in levels on
an unbounded range: on [1, 2^L] it is 1 − log₂ 3/L, so the missing number is the range held, the reader's levels; the
even share and the even turn, which do answer it (½, 0.4097), are not unchanged by the unit. Mikkelson's answer is
available where a shared unit (volume) is agreed beforehand, the completed view's measure; without one, the answer is
the situated reader's.

Not shown: that von Mises left the unit open. Read with volume as an agreed unit, the problem is the completed view's,
and the even share is its fair answer; that is a reading of the problem's statement, not a result.
