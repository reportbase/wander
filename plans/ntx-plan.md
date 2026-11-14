# NTX: the notation test on laws this project did not write

14 November 2026. Tom: "1", to Claude's first suggestion after R994: NTN (R990) found 30 of the 82 laws of *Reads and
Writes* that carry π or e carry it as notation, but those laws were written by this project, in its own framing. Does
the same split hold on standard laws chosen by someone else?

## Method (fixed before anything runs)

1. **The list.** A fresh agent, told only to list about 100 well-known formulas from undergraduate physics, geometry,
   probability and engineering that contain π, e, an exponential, a logarithm, a circular or a hyperbolic function (one
   line each: number, name, formula, field), and not told why, writes `runs/ntx/laws.md`. Not shown this plan, NTN, PIE
   or any paper of this project.
2. **Blind classes.** A second fresh agent gets the list and PIE's three definitions verbatim (A an additive chart; L a
   limit, series, infinite product or integral over a whole or unbounded range, including a normalizing total; X
   neither), not the rule below or the predictions, and writes `runs/ntx/blind-class.md`.
3. **Restatements.** A third fresh agent gets the list and NTN's rule verbatim, not the classes or the predictions, and
   writes `runs/ntx/restate.py` in NTN's format (original and restatement as mpmath functions at 50 digits, three or more
   points, the restatement as text, or NONE with a reason).
4. **Check.** `runs/ntx/check.py` is NTN's checker with the paths changed and the group lines removed: a law is notation
   only if every point agrees to 10⁻³⁰ and the restatement's text and code carry no forbidden token. I read every passing
   restatement and record, before counting, any I judge not the same relation (NTN's rule: not a ratio, part, or the
   constant moved).

The rule (NTN's, unchanged): a law's π or e is notation if the same relation can be stated with slopes s = v/h (several
for several directions), the shares h = 1/√(1 + s²), v = s/√(1 + s²), rational operations and square roots of rational
expressions only, with no π, Ω, e, exponential, logarithm, circular or hyperbolic function, agreeing exactly (10⁻³⁰ at
50 digits) at three or more points; the same relation, not a ratio, a part, or the original with a constant moved.
Otherwise it is content.

## Predictions (committed before any run; NTN's numbers were 30/82, L 0/32, A 20/34, X 10/16)

- **X1** Between 20% and 55% of the listed laws are notation. Kill: outside.
- **X2** Of the laws classed L, at most 10% are notation. Kill: more.
- **X3** Of the laws classed A, at least 40% are notation. Kill: fewer.
- **X4** Of the laws classed X, at least 50% are notation. Kill: fewer (or no X laws: then X4 is void).
- **X5** The notation share among A exceeds that among L by at least 30 percentage points. Kill: less.

## Runs

(appended below as they come out; nothing above this line edited afterwards)

### Run 1 (14 Nov 2026; list `runs/ntx/laws.md`, blind classes `runs/ntx/blind-class.md`, restatements
### `runs/ntx/restate.py`, each by its own fresh agent; checked by `runs/ntx/check.py`, output `runs/ntx/ntx-run1.txt`)

107 formulas listed; blind classes A 63, L 42, X 2. The restater claimed 20 notation; 18 pass the check. 10 (sine
addition) and 68 (Snell) agree to 10⁻⁵¹ but fail on words in their prose ("sine of", "i.e."), and by the rule as fixed
they count as failed. Read before counting, I judge two of the 18 not to be what the rule asks: 37 (the derivative of
arctan restated as its right side alone, a part) and 101 (the Breit–Wigner line, which as listed carries no π or e at
all, a slip of the list). Counted by the rule as fixed (18), and by my reading (16 of 106 true carriers):

- **X1 killed**: 18 of 107 (16.8%; 16 of 106, 15.1%), under 20%.
- X2 not killed: 0 of 42 limits.
- **X3 killed**: 17 of 63 A (27%; 16, 25%), under 40%.
- X4 not killed in its letter, as good as void: 1 of 2 X, and that one is 101.
- **X5 killed**: A 27% against L 0%, 27 points (25 by my reading), under 30.

So the split does not carry over at NTN's rate. What carries over: no limit is notation (0 of 42 here, 0 of 32 there),
and the identities among angles are (Pythagoras, tangent and double-angle, the laws of cosines and sines, the half-angle,
Euler's and De Moivre's formulas in the half-angle slope, cosh² − sinh² = 1), with the optics and relativity laws whose
input is a direction (Malus, Brewster, a projectile's range, the Lorentz factor by rapidity, the Doppler factor,
aberration). Post hoc, untested: the 46 chart laws that stay content are nearly all laws whose chart's coordinate is an
amount, not a direction: a time (decay, RC, RL, a damped or harmonic oscillator, a plane wave's ωt), an energy over kT
(Boltzmann, Arrhenius, Fermi–Dirac), a height (the barometric formula), a mass ratio (Tsiolkovsky), a period counted in
seconds (pendulum, spring, LC, Kepler's 4π²). The laws of *Reads and Writes* are mostly among directions, which is why NTN
found 37%; a textbook's are mostly in amounts. The rule does not settle one borderline: a law like V = V₀(1 − e^(−t/τ))
could be "restated" with k = e^(−t/τ) as V = V₀(1 − k), which only renames the exponential; the restater called these
NONE, and NTN counted the like of its law 2 as notation. Read that way the sorting would be: π or e is notation where a
law relates directions, and content where it carries an amount (a time, an energy, a length in a unit) through a chart
or a limit. That is a reading to test, not a result.
