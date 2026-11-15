# DVH: the chart rule on a fresh list, both briefs fixed, predicted first

15 November 2026. Tom: "test on a fresh list". DVG run 2 (R1003) settled the restater's call on angles given by an
inverse function and left the disagreement between the judge's brief and the restater's: angles solved for by an inverse
function of like quantities, and stated angle values, were "other" to the blind judge and notation to the restater. This
run gives both briefs the same two sentences and tests the chart rule on a ninth list, from ten Wikipedia articles not used
before: Rotation matrix, Bloch sphere, Stokes parameters, Jones calculus, Great-circle distance, Solar zenith angle,
Hyperbolic trajectory, Elastic collision, Mercator projection, Coriolis force.

## The list (as DVG)

`runs/dvh/fetch.py` pulls each article's wikitext (revision id, timestamp, sha256 recorded; wikitext not committed) and
every `<math>` or `{{math|}}` block carrying π or e in any form into `runs/dvh/candidates.md`. A fresh agent, given only
that file, writes `runs/dvh/laws.md`: each distinct law or relation stated (not a bare symbol or a definition by name),
one line, its source article. `runs/dvh/sample.py` takes a seeded 120 (seed 15112026) if more.

## The two sentences, in both briefs

1. **An angle given by an inverse circular or hyperbolic function of quantities** (arctan, arcsin, arccos, arg, artanh,
   or a logarithm that is one of these, ½·ln((1 + x)/(1 − x))), where the quantities form a ratio of like quantities, is
   that ratio's chart: the judge classes it chart, and the restater restates it by saying the angle's slope (or share, or
   half-slope) equals the same expression.
2. **A stated angle value** (θ = π/2, φ = 0, ±π, 2πn), where the angle is a direction's, is a chart: the judge classes it
   chart, and the restater restates it as the direction's shares or slope.

## Blind class (a fresh agent, given only `runs/dvh/laws.md` and this definition)

DVG's definition of chart and other, unchanged, with the two sentences above added to chart. Writes `runs/dvh/chart.md`,
one line a law, `n. chart|other: reason`.

## Restatements (a second fresh agent, given the list, NTN's rule, the two sentences and the checker; not the classes or
## predictions)

DVG run 2's brief with the second sentence added, to `runs/dvh/restate.py`, checked by NTX's checker (`runs/dvh/check.py`).
I read every passing restatement and record, before counting, any I judge not the same relation; the count by the rule is
the one scored.

## Predictions (committed before any fetch)

- **H1** Laws judged chart are notation at 85% or more. Kill: under 85%; void if fewer than 15 chart laws.
- **H2** Laws judged other are notation at 10% or less. Kill: over 10%; void if fewer than 15 other laws.
- **H3** The overall notation share is (0.92·n(chart) + 0.03·n(other))/n, computed from the blind classes before the
  restatements are checked, and the true share is within 8 percentage points of it. Kill: further.

The rates are DVG's, unchanged. Stated before the run: the list is rich in directions by choice of articles, so H2 may be
void if fewer than 15 laws are judged other.

## Runs

(appended below as they come out; nothing above this line edited afterwards)
