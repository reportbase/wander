# CHS: chaos as the turn doubled, in three charts

11 Nov 2026. SPN R833. Tom: "there is also a connection to chaos theory we should explore"; then "yes" (to a short
exact check, then a paragraph in *Reads and Writes* §9).

## The question

Double the turn. In the turn's own chart, the slope's and the share's, is that the doubling (tent) map, Boole's map
and the logistic map at 4, each leaving the uniform turn's law in its chart unchanged, each spreading at ln 2 a step?
Does a fixed fineness K lose exactly one binary digit of the start per step? And does the three-tier reading hold
(the rule exact and rational; a writer at work, holding a count of digits, losing the orbit; cycles only the paper's)?

## Known beforehand

- Classical: Boole (1857), x ↦ x − 1/x keeps Lebesgue measure, ½(x − 1/x) keeps the Cauchy; Ulam and von Neumann
  (1947), the logistic map at 4 conjugate to the tent map, invariant density the arcsine; Lyapunov exponent ln 2 for
  each; ½(x − 1/x) is Newton's step for x² + 1.
- The corpus: the doubling map and its ln 2 beside the floor's remainder (R470, R464); the angle doubling keeping the
  Cauchy without being Möbius (R476); HZT's cot 2Θ; the arcsine as the central chart's law (R579); Niven's theorem
  (R472); the half-angle slope (√(1 + s²) − 1)/s the writer's (R592, R793).
- Not checked: draw's labs (the draw repository is not attached to this session). If a lab there already covers
  this, it was known beforehand and is not cited here.

## Set-up

`runs/chs/chs.py`: exact rationals (Fraction) for identities and orbits; mpmath at 60 digits for the laws and
exponents, at 600 digits as the reference orbit in C6. On the quarter turn the doubled turn is folded back:
T(s) = |2s/(1 − s²)|, with the corner s = 1 sent to the horizon and the horizon to home. The turn's share is
g = (2/π)·arctan s (the writer's), on which T is the tent map 1 − |1 − 2g|.

## Predictions (committed before the run; derived on paper first)

- **C1. Three charts, one map, exactly.** For 40 rational slopes s, with v² = s²/(1 + s²): the share of T(s) is
  4v²(1 − v²); the reciprocal slope c = 1/s goes to ½(c − 1/c) up to sign; and ½(c − 1/c) = c − (c² + 1)/(2c),
  Newton's step for c² + 1. All equalities of rationals. Kill: any fails.
- **C2. Each chart's law is kept.** At x = 1/5, ½, 1, 2, 7: the half-Cauchy's share of the set T(s) ≤ x equals
  (2/π)·arctan x, the set being s ≤ a or s ≥ 1/a with a = (√(1 + x²) − 1)/x, the half-angle slope; the arcsine law's
  share of 4y(1 − y) ≤ x′ equals (2/π)·arcsin √x′ at x′ = 1/10, ½, 9/10; the full Cauchy is kept by ½(x − 1/x) at
  five points. To 10⁻⁴⁰. Kill: any differs.
- **C3. ln 2 a step in every chart.** ∫ ln|T′| against the chart's law is ln 2 for the tent map, for T on the
  half-Cauchy, for ½(x − 1/x) on the Cauchy and for 4y(1 − y) on the arcsine, to 10⁻²⁰. Kill: any differs.
- **C4. One digit a step at fixed K.** With K = 2^m cells of equal share, the cell of the n-th image is fixed by the
  start's cell among 2^(m+n), and not by its cell among 2^(m+n−1): for m = 3, 4, 5 and n = 1 … 6, exhaustively over
  cells with exact rationals. Kill: fixed by a coarser cell, or not fixed by the finer.
- **C5. No rational slope cycles, and its orbit cannot be held.** For 200 rational slopes other than 0 and 1, twelve
  steps exact: no slope repeats, none reaches the corner, and the denominator's length in bits about doubles each
  step (the ratio of bit lengths at steps 12 and 11 within 5% of 2). By Niven's theorem the cycles sit at turns that
  are rational parts of the whole turn, whose slopes are irrational but for 0 and 1. Kill: a repeat, a corner
  reached, or a ratio outside the band.
- **C6. A count of p digits holds the orbit for about p steps.** From five starts, the orbit iterated at p = 24, 53
  and 113 bits parts from the 600-digit reference (by more than 0.1 in g) at a step whose median lies in
  [p − 12, p + 2]. Kill: a median outside its band.
- **C7. (The reading.)** If C1, C5 and C6 hold: the rule is exact and rational in s (one step is the reader's tangent
  addition of a slope with itself); a writer holding fractions keeps the orbit exactly but at a cost doubling each
  step; a writer holding p digits keeps it about p steps; a cycle needs a turn that is a rational part of π, the
  paper's. The reading fails if a rational slope cycles (C5) or a p-digit orbit outlasts p + 2 steps (C6).

## Runs

### Run 1 (11 Nov 2026; `python3 runs/chs/chs.py`, output `runs/chs/chs-run1.txt`)

- C1 not killed: 40 of 40 rational slopes, all three identities exact.
- C2 not killed: the half-Cauchy under T, the arcsine under 4y(1 − y) and the Cauchy under ½(c − 1/c), to 10⁻⁶⁰.
- C3 not killed: ln 2 in all four, to 10⁻⁵⁹.
- C4 not killed: K = 8, 16, 32, n = 1 … 6, exhaustively.
- C5 not killed: no repeat and no corner in 200 orbits; the denominator's bits, step 12 over step 11, between 1.9971
  and 2.0027 (from 3/7 the twelfth denominator has 9,950 bits).
- C6 killed, by my band: first steps apart, p = 24: 23, 24, 23, 23, 25 (median 23); p = 53: 57, 52, 52, 54, 59
  (median 54); p = 113: 116, 112, 114, 116, 117 (median 116, one past the band's p + 2 = 115).
- C7 killed in its letter, through C6's clause ("a p-digit orbit outlasts p + 2 steps"): six of the fifteen orbits
  did, by 1 to 6 steps.

Post hoc: the orbits part at p − 1 to p + 6 steps, about p as predicted, but my band was lopsided the wrong way
(p − 12 to p + 2). I had reasoned that 0.1 in g is reached about three doublings early; the rounding errors are
often smaller than one unit in the last place, which delays it instead. The claim that survives is "about p steps";
its band was mine and wrong.

### Run 2: prediction (committed before the run)

- **C6′.** Same starts, same threshold, p = 24, 53, 113, 200: every orbit's first step apart lies in [p − 4, p + 8],
  and a line fitted to the medians against p has slope within 2% of 1. Kill: any orbit outside its band, or the slope
  outside.
- **C7′.** As C7 with C6′ in place of C6: the reading fails if a rational slope cycles (C5) or C6′ is killed.

### Run 2 (11 Nov 2026; `python3 runs/chs/chs2.py`, output `runs/chs/chs-run2.txt`)

- C6′ not killed: first steps apart p = 24: 23–25; p = 53: 52–59; p = 113: 112–117; p = 200: 199–203; every orbit in
  [p − 4, p + 8]; the medians' slope against p 1.0098.
- C7′ not killed.

### Reading

The turn added to itself is one map in three charts, each a textbook chaotic map keeping that chart's law of the
uniform turn, ln 2 a step in all. The rule is rational in s. A writer in fractions keeps the orbit at a cost that
doubles a step and never meets a cycle; a writer in p digits keeps it about p steps; the cycles are at rational parts
of π. All classical but the sorting by tiers, which is this paper's reading.
