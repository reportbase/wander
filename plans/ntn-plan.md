# NTN: is a law's π notation or content?

14 November 2026. Tom: "merge and run the notation test" (after PIE run 1, R989, whose post hoc reading was untested:
the eight projections and three angle identities are the read's shares h, v dressed in an angle, so their π is notation).

## The rule (fixed before anything runs)

A law's π or e **is notation** if the same relation can be stated with the slope s = v/h (and, for several directions,
several slopes; for space, s and s₂), the shares h = 1/√(1 + s²), v = s/√(1 + s²), rational operations and square roots
of rational expressions only, with **no** π, Ω, e, exponential, logarithm, circular or hyperbolic function in it, and the
restatement agrees with the original exactly (to 10⁻³⁰ at 50 digits) at three or more points of its domain. The relation
must be the same one: not a ratio of it, a part of it, or the original with a constant moved to the other side. Otherwise
the π or e **is content**.

## Method

1. A fresh agent gets `runs/pie/flagged.md` (the 82 laws) and the rule above, not the predictions, PIE's classes or any
   earlier sort, and for each law writes either a restatement or NONE with a reason, as a pair of Python functions in
   `runs/ntn/restate.py` (the original as stated, the restatement), mpmath at 50 digits, with three or more sample points,
   and the restatement also as a plain-text expression.
2. I run it (`runs/ntn/check.py`): each pair must agree to 10⁻³⁰ at every point, and the restatement's text must contain
   none of the forbidden tokens (PIE's flag pattern). A law counts as notation only if both hold. I read every claimed
   restatement and record any I judge not the same relation, before counting.
3. Counts by PIE's blind classes and groups.

## Predictions (committed before any run)

- **N1** Of the eleven projections and identities (21, 34, 35, 48, 53, 58, 61, 88, 80, 93, 108), at least 9 are notation.
  Kill: fewer than 9.
- **N2** Of the five others PIE left (the holonomy laws 89, 90, 92, 102; Kepler 83), at most 1 is notation. Kill: 2 or
  more.
- **N3** Of the 32 laws PIE classed L (limits), at most 8 are notation. Kill: more than 8.
- **N4** Of the 34 laws PIE classed A (charts), at least 17 are notation (the chart written out in the slope). Kill:
  fewer than 17.

## Runs

(appended below as they come out; nothing above this line edited afterwards)

### Run 1 (14 Nov 2026; restatements `runs/ntn/restate.py` by a fresh agent, checked by `runs/ntn/check.py`, output
### `runs/ntn/ntn-run1.txt`)

The checker failed twice before counting, both mine: it read the restatement's source line, which it shares with the
original's lambda, so the original's atan and exp were charged to the restatement; and it could not compare laws stated
in two parts. It now checks the names the restatement's own code uses, and compares parts one by one. The rule was not
changed. The agent claimed 33 notation; 30 pass the check; 89, 90 and 92 fail it because their restated text keeps
cos(Θ/2), cosh ζ or tan(Θ/2) for the loop's leftover. I read all 30 and judge every one the same relation; two are on
the edge and counted: 108 (Ω·1/Ω = 1 restated as x·1/x = 1, the identity not resting on Ω's value) and 123 (two
half-angles summing to π restated as their half-slopes multiplying to 1).

- N1 not killed: 10 of the 11 projections and identities are notation (21, 34, 35, 48, 53, 58, 61, 80, 88, 108); 93,
  (θ/sin θ)(sin θ/θ) = 1, is not (the two measures need the arc itself).
- N2 not killed: none of the five (89, 90, 92, 102 the holonomy laws; 83 Kepler) is notation by the rule.
- N3 not killed: 0 of the 32 limits.
- N4 not killed: 20 of the 34 charts (1, 2, 14, 17, 18, 20, 30, 43, 44, 45, 60, 73, 74, 75, 81, 82, 87, 91, 95, 123).

Of the 82 laws carrying π or e, 30 carry it as notation. Said plainly, post hoc: what is left, where π or e is content,
is the 32 limits (series, products, totals that normalize a density, integrals to Ω), and fourteen chart laws whose
subject is the chart itself or a total (13 the slope joined to the angle, 16 the share of the turn, 28 the turn's
measure dθ, 38 the exponential semigroup, 49 pseudorapidity, 51 places even in angle, 56 the dial, 67 an angle rate; 24,
25, 50, 55, 104, 118 a normalizing total), plus 93, the four holonomy laws and Kepler's whole turn. The holonomy laws
failed only on their left side: written with the leftover's own half-slope, τ = tan(Θ/2), each would be rational too,
which is untested and, by the rule as written, not counted. So the reading R989 left untested holds: where π or e is
not notation, it is a limit, or a chart or a total is itself what the law states.
