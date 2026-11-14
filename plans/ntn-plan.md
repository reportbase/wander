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
