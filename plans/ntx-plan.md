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
