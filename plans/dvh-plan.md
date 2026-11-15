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

### Run 1 (15 Nov 2026; `runs/dvh/fetch.py`, list `runs/dvh/laws-all.md` sampled by `runs/dvh/sample.py` to `runs/dvh/laws.md`,
### class `runs/dvh/chart.md`, restatements `runs/dvh/restate.py`, each by its own fresh agent; scored by `runs/dvh/dvh.py`,
### H3's expectation `runs/dvh/dvh-expect.txt` committed before the check, output `runs/dvh/dvh-run1.txt`)

Pages fetched (revision id, timestamp, sha256 of the wikitext; the wikitext not committed):

| page | revision | timestamp | sha256 |
|---|---|---|---|
| Rotation matrix | 1379939691 | 2026-10-12T20:36:16Z | 945e9a28e3db005e249174a3eadda3363dcba306a6dab52e9418e29aa851fd0e |
| Bloch sphere | 1381941389 | 2026-10-25T19:10:43Z | 8d9b5d8f406d7ca574d3c2ef0a6e0a8d90674800fe3829740a00718ee9062451 |
| Stokes parameters | 1345308547 | 2026-03-25T12:37:35Z | 7e18b6d935582fcbbaaf518cc93bc02e4b0375b09245fc307d05f67f065aa130 |
| Jones calculus | 1382498966 | 2026-10-29T00:20:58Z | 4d0f4c42f880755c21ff8bc26fa0a5efd0c5a3189d42c9ae8d41c88dc5f4f330 |
| Great-circle distance | 1375798565 | 2026-09-20T03:28:25Z | fb8fc8f16be8584dc15b975194f8520fefd6a3100382ae6dcd5a0f70da75fdf0 |
| Solar zenith angle | 1380715396 | 2026-10-17T11:51:46Z | e09e0f6445c221ed1cf7fc8557f399164263b70fb298efed9e82941c3df4c31d |
| Hyperbolic trajectory | 1346459260 | 2026-03-31T23:35:39Z | 521ec4b488f1ddb3b5111accac9c24338059239bd11d08790d7a8be4c77f0541 |
| Elastic collision | 1351860510 | 2026-04-30T16:16:45Z | 18277e40e65d85869384d08638795b35fd66ff613f6d65be51d40322a2b0a414 |
| Mercator projection | 1382928340 | 2026-10-31T01:24:15Z | ed68af44ec32b87980b4ef223cb32c620a71c836736f610d72c7b8667d56c4de |
| Coriolis force | 1385656361 | 2026-11-14T14:58:46Z | f8ca92dad5474013832c9f6d98755b2146d67681238d8a5bc68bc6c790301f83 |

206 candidate blocks; a fresh agent listed 146 laws (`runs/dvh/laws-all.md`), sampled to 120. The blind judge: chart 100,
other 20. H3's expectation, written before the check: (0.92·100 + 0.03·20)/120 = 77.2%. A fresh restater marked 104
notation, every one passing the checker (0 failed); the checker printed it no class split (it reads `chart.md` only when
the scorer runs it; committed before the restater finished). I read every passing restatement before counting.

Recorded before counting, my readings of passing restatements: 74 (the angle between asymptotes, 2π + 2·arctan(b/a)) is
not the same relation, since the restatement gives only the direction and drops the whole turn the stated angle carries;
30 (0 ≤ φ < 2π restated as "every direction once") is close to empty. 27, 29 (0 ≤ θ ≤ π as v ≥ 0) and 55 (γ ∈ [0, 2π] as
|w| = 1) I take as the same relation. Scored by the rule's count, as stated:

- **H1 not killed**: chart laws 98 of 100 notation (98.0%). The two content: 101 (sec φ as the derivative of Mercator's
  y) and 104 (sinh⁻¹(tan φ) and gd).
- **H2 killed**: other laws 6 of 20 notation (30.0%): 27, 29, 30, 55, 74, 108. Without 74 and 30, 4 of 20 (20%), still
  killed.
- **H3 killed**: 104 of 120 = 86.7%, against 77.2% ± 8 (9.5 points over).

Read, post hoc and untested. The chart side has now held on two lists with the angle-output sentence in the briefs (DVG
run 2 98.6%, DVH 98.0%). The other side leaked again, at one boundary: ranges of an angle and a whole turn added to one
(27, 29, 30, 55, 74), which the judge classed "a turn as a range or total" and the restater took as statements about
directions under the stated-value sentence, which named values, not ranges; 108 is an approximation (≅) whose right side
restates whole. So the stated-value sentence moved the boundary to ranges and turn totals and did not close it. The
content the judge named held: amounts inside functions (36, 51, 85), integrals and series (24, 71, 102), angles used as
arc amounts (100, 103, 106, 110, 113, 114) and W/2π (111) all stayed content. What is left is whether a range or a total
of a direction's angle is a statement about the direction, and both briefs would have to say the same about it.
