# DVB: a third list, the three-in-five predicted first

15 November 2026. Tom: "Do want to run a third list", then "Merge and run". DVA (R996) found, after the fact, that on two
lists every law taking a limit or total kept its π or e (74 of 74) and that laws relating only directions without a limit
were notation about three times in five (27 of 43 on *Reads and Writes*' list, 14 of 24 on NTX's standard formulas);
laws with an amount and no limit were notation at 43% (3 of 7) and 10% (4 of 41). That reading is untested. This run
tests it on a third list chosen by neither of us, with the numbers committed first.

## The list (fixed before anything is fetched)

The source is ten Wikipedia pages whose contents Wikipedia's editors chose, all physics:
List of equations in classical mechanics; List of equations in wave theory; List of equations in fluid mechanics; List of
equations in nuclear and particle physics; List of equations in quantum mechanics; List of electromagnetism equations;
List of equations in gravitation; List of photonics equations; List of relativistic equations; Table of thermodynamic
equations. (List of trigonometric identities was considered and left out: it is mathematics, not a list of laws of
physics, and would be nearly all directions.)

1. `runs/dvb/fetch.py` fetches each page's wikitext (`action=raw`) and records its revision id and sha256 in this plan's
   run entry. The wikitext is not committed (CC BY-SA, kept in the scratchpad).
2. The same script pulls every `<math>` block and every `{{math|…}}` block that contains π or e in any form: `\pi`, `π`,
   `e^`, `\exp`, `\ln`, `\log`, `\sin`, `\cos`, `\tan`, `\cot`, `\sec`, `\csc`, `\sinh`, `\cosh`, `\tanh`, `\arc…`,
   `\operatorname{…}` of those, and writes them with their page and the nearest heading or table label to
   `runs/dvb/candidates.md`.
3. A fresh agent gets `candidates.md` only (not this plan, not any earlier run or paper) and writes `runs/dvb/laws.md`,
   one law a line (`n. **name**: formula (page)`), in plain text, keeping every candidate that is an equation (a relation
   with an equals sign or a proportionality, or a defining formula of a quantity), merging exact duplicates, dropping only
   fragments that state no relation and formulas in which, written out, no π or e appears (a stray `e` for the charge).
   It records every dropped candidate and why at the foot of the file.
4. If more than 120 laws remain, `runs/dvb/sample.py` keeps a seeded sample of 120 (seed 15112026), in order.

## Blind sorting (each by its own fresh agent, given only `runs/dvb/laws.md` and the definitions, verbatim from before)

- **Class** (PIE's and NTX's definitions): **A** π or e enters through an additive chart, a coordinate in which turns or
  scalings add (an angle, a logarithm, an exponential as the chart's inverse); **L** through a limit, a series, an
  infinite product, or an integral over a whole or unbounded range, including a normalizing total; **X** neither. Writes
  `runs/dvb/blind-class.md`.
- **Tag** (DVA's definitions): **D** every quantity the law relates is a direction or a ratio of like quantities,
  dimensionless by construction (an angle, a slope, a share, a cosine, a rapidity, a ratio of two lengths or two
  intensities), and the law relates them among themselves; **A** an amount with a unit enters the law (a time, a length,
  an energy, a mass, a temperature, a frequency, a charge, a count), including where it is divided by a scale to make an
  exponent or an argument (t/τ, E/kT, ωt, x/a), or where the law's constant normalizes a density over amounts. Writes
  `runs/dvb/tags.md`.

## Restatements (a fourth fresh agent, given the list and the rule, not the classes, tags or predictions)

NTN's rule, unchanged: a law's π or e is notation if the same relation can be stated with slopes s = v/h (several for
several directions), the shares h = 1/√(1 + s²), v = s/√(1 + s²), rational operations and square roots of rational
expressions only, with no π, Ω, e, exponential, logarithm, circular or hyperbolic function, agreeing exactly (10⁻³⁰ at
50 digits) at three or more points; the same relation, not a ratio, a part, or the original with a constant moved.
Otherwise it is content. DVA's borderline, settled before: renaming an exponential of an amount (k = e^(−t/τ)) is not a
restatement. The agent writes `runs/dvb/restate.py` in NTN's format and is told that the checker rejects the forbidden
names anywhere in the restatement's text (so it writes "the slope's" in words, never "sin" or a lone "e").

`runs/dvb/check.py` is NTX's checker with the paths changed. I read every passing restatement and record, before
counting, any I judge not the same relation; the count by the rule is the one scored.

## Predictions (committed before any fetch)

Cells are the blind tag crossed with the blind class: "no limit" means class A or X, "a limit" class L.

- **Q1** Every law classed L is content. Kill: one notation law classed L.
- **Q2** Laws tagged D with no limit are notation at 45% to 75%. Kill: outside, or fewer than 10 such laws (then void).
- **Q3** Laws tagged A with no limit are notation at under 20%. Kill: 20% or more.
- **Q4** The overall notation share is 0.60·n(D, no limit) + 0.10·n(A, no limit), divided by the number of laws, computed
  from the blind tags and classes before the restatements are checked, and the true share is within 8 percentage points
  of it. Kill: further.

## Runs

(appended below as they come out; nothing above this line edited afterwards)
