# DVG: the chart rule, predicted first

15 November 2026. Tom: "test the chart rule". DVF (R1001) left a reading after the fact: across DVE and DVF the laws
whose π or e restates (NTN's rule) are those whose transcendental is a chart of a ratio of two coordinates, circular (an
angle) or hyperbolic (a rapidity), with no amount inside the function and no whole turn taken as a total. DVE's and
DVF's entry rules each missed a kind of notation (halves and complements; then rapidities, e^(iθ) and a coefficient
vector's phase). This run writes the chart rule down first and tests it on an eighth list.

## The list (fixed before anything is fetched)

Ten Wikipedia articles, none used on an earlier list: Rapidity; Velocity-addition formula; Thomas precession; Euler
angles; Kepler orbit; Harmonic oscillator; Lens; Diffraction; Wave interference; Torque.

The steps are DVF's, unchanged but for the paths (`runs/dvg/`): fetch, candidates, a fresh agent's list (DVF's brief),
a seeded sample of 120 if more (seed 15112026).

## Blind class, the chart rule (a fresh agent, given only `runs/dvg/laws.md` and this definition)

For each law, where does π or e (in any form: π, a degree constant, e, exp, log, ln, a circular or hyperbolic function or
its inverse, e^(iθ)) enter?
- **chart**: only inside circular or hyperbolic functions, their inverses, or exponentials e^(iθ), e^(±ζ), whose argument
  is an angle or a rapidity that is itself the chart of a ratio of two like quantities (a direction's angle; a
  rapidity, the chart of a velocity ratio; a phase that is the direction of a pair of like coefficients), or is built from
  such by adding, subtracting, halving, doubling, whole-number multiples, or a complement or supplement (π/2 − θ, π − θ).
  No time, length, frequency or other amount inside the function. Amounts may appear anywhere outside the functions,
  multiplying or adding to them, including an angle's or a rapidity's own rate.
- **other**: anywhere else, in whole or in part: a whole or half turn as a total or a free constant (2π, π, 360°) not a
  complement or supplement inside such a function; a function whose argument contains an amount (ωt, kx, t/τ, E/kT, a
  phase built from a time or a length, a mean anomaly from a time); a logarithm; a limit, series, product or integral; a
  numerical value given in place of a relation; an approximation.
Writes `runs/dvg/chart.md`, one line a law, `n. chart|other: reason`.

## Restatements (a second fresh agent, given the list, NTN's rule and the checker, not the classes or predictions)

DVF's brief, unchanged, to `runs/dvg/restate.py`, checked by NTX's checker (`runs/dvg/check.py`). I read every passing
restatement and record, before counting, any I judge not the same relation; the count by the rule is the one scored.

## Predictions (committed before any fetch)

- **G1** Laws judged chart are notation at 85% or more. Kill: under 85%; void if fewer than 15 chart laws.
- **G2** Laws judged other are notation at 10% or less. Kill: over 10%; void if fewer than 15 other laws.
- **G3** The overall notation share is (0.92·n(chart) + 0.03·n(other))/n, computed from the blind classes before the
  restatements are checked, and the true share is within 8 percentage points of it. Kill: further.

The rates are DVE's and DVF's, unchanged.

## Runs

(appended below as they come out; nothing above this line edited afterwards)

### Run 1 (15 Nov 2026; `runs/dvg/fetch.py`, list `runs/dvg/laws-all.md` sampled by `runs/dvg/sample.py` to
### `runs/dvg/laws.md`, class `runs/dvg/chart.md`, restatements `runs/dvg/restate.py`, each by its own fresh agent; scored
### by `runs/dvg/dvg.py`, G3's expectation `runs/dvg/dvg-expect.txt` committed before the check, output `runs/dvg/dvg-run1.txt`)

Pages fetched (revision id, timestamp, sha256 of the wikitext; the wikitext not committed):

| page | revision | timestamp | sha256 |
|---|---|---|---|
| Rapidity | 1383473035 | 2026-11-02T21:47:20Z | 9b7170bfd67ce37ea218386fe8972a8a7a08a97d9ed90f94fdecd33feef68362 |
| Velocity-addition formula | 1379283888 | 2026-10-09T01:32:57Z | b59dd5371ea1d9e793b8a86db767c0467bb95029eba40eb7a5355b97b85f8d40 |
| Thomas precession | 1385580159 | 2026-11-14T01:19:00Z | 783bf2eb9f8a3636dfaad7ede46f3c26d405d55dcb9633051aef59b86fd99403 |
| Euler angles | 1381977340 | 2026-10-25T21:54:51Z | caf18013cbd54c079224749e7f1cd99bad48990672401542b293048ee7478f82 |
| Kepler orbit | 1383915216 | 2026-11-05T15:36:32Z | a77c04be4ab984bf3fae90c3bcb31115a9e31bb027f09b597bf841e5a351a59a |
| Harmonic oscillator | 1373924880 | 2026-09-08T19:43:44Z | aa84e72c0ea7cefaeeecb5612a793407cfb9a469216cad0e495ea40640086b09 |
| Lens | 1384860947 | 2026-11-10T12:52:39Z | ee43e541f46f3c2db0220ed960418ce6f3dda0e3c5774e155d783f8bac88c5ce |
| Diffraction | 1383422735 | 2026-11-02T16:22:04Z | 849887b5a686b218e304ede261142adac3fcc7d89c29d5cfb76b2591179a9404 |
| Wave interference | 1383568553 | 2026-11-03T11:22:04Z | 9aea464d3df63ab8d80d4f4b143d916176e1f797ddb753e81cf768f3161c5bfd |
| Torque | 1382438427 | 2026-10-28T18:24:48Z | 415f2e8b44e2f3cebf6333dcbbcbca89e8763b0438642290af4642e1ea4ad6d3 |

251 candidate blocks; the list agent kept 207 laws (dropped 42, merged 2), so a seeded sample of 120. Class, blind, by
the chart rule: chart 69, other 51. G3's expectation, written before the check: (0.92·69 + 0.03·51)/120 = 54.2%. The
restater (DVF's brief) claimed 60 notation; all 60 pass the check. Read before counting, I judge two not the same
relation: 17 and 18, approximations whose restatement keeps the exact part and drops the "≈" step. By the rule all 60
count.

- **G1 killed, narrowly**: 58 of 69 laws judged chart are notation (84.1%, under 85%).
- **G2 not killed**: 2 of 51 laws judged other are notation (3.9%), and they are the two I judge not the same relation.
- **G3 not killed**: 60 of 120 = 50.0%, against the 54.2% expected (4.2 points).

Said plainly: for the first time the content side held. Written down before the list, the chart rule left out no kind of
notation: of 51 laws it put elsewhere, none restated by the rule but two approximations restated in part. Its chart side
missed its bound by one law. Nine of the eleven chart laws called content are the Euler angles read back from a frame or
a rotation matrix (34, 37–44: α = arctan(R₃₂/R₂₂), β = arcsin(−R₁₂), …), which the restater called content because "the
angle is the output"; the other two are a matrix exponential of a sum (5) and the rapidity as artanh β (24), the same
reason. Earlier restaters took a law giving an angle by an inverse function as notation, stated as the direction's slope
(DVC 16, the critical angle; DVE 18, arctan 4; DVF 10, 16). So the miss turns on one call that the restaters' brief does
not settle: whether "θ = arctan(x)" is restated by "the slope of θ is x". By the earlier restaters' call G1 would be
69 − 2 = 67 of 69 (97%); that count is post hoc and not scored.

Post hoc, untested: the chart rule sorts these lists as well as the restatement rule itself; what is left open is not the
entry but the restaters' treatment of an angle given as an output.

### Run 2, the brief fixed (predictions committed before the restater runs)

Run 1's G1 turned on a call the brief did not settle: a law that gives an angle by an inverse function (θ = arctan x,
β = arcsin(−R₁₂)) was content to run 1's restater ("the angle is the output") and notation to the earlier ones (DVC 16,
DVE 18, DVF 10, 16). Run 2 settles it in the brief, the same for every law: **where a law gives a direction's angle by an
inverse circular or hyperbolic function of quantities, it is restated by saying the angle's slope (or share, or
half-slope) equals the same expression; that is the same relation, since on the range a direction's angle and its slope
determine each other.** Nothing else in the brief changes; a fresh restater, given only `runs/dvg/laws.md`, the rule with
this sentence added and the checker, writes `runs/dvg/restate2.py`; `runs/dvg/check2.py` is `check.py` reading it. The
list, the blind classes (`runs/dvg/chart.md`) and G3's expectation (54.2%) are run 1's, unchanged.

Predictions, as run 1's: **G1′** chart laws notation at 85% or more; **G2′** other laws at 10% or less; **G3′** overall
within 8 points of 54.2%. Caution, stated before the run: this run is not a fresh test of the rule, since its list and its
misses were seen in run 1; it tests only whether the brief's one open call was what moved G1, and the chart rule still
needs a fresh list once the brief is fixed.

### Run 2 results (`runs/dvg/restate2.py`, `runs/dvg/dvg-run2.txt`)

A fresh restater, given only the list, the rule with the one settled sentence and the checker, marked 78 of 120 notation;
every one passed the checker (0 failed), and I read each before counting. Its template note: `check2.py` reads
`verdict`, so its `N` and `T` carry `verdict` beside the brief's `notation` flag (no change to any check).

- **G1′ not killed**: chart laws 68 of 69 notation (98.6%, against ≥ 85%). The one content chart law is 5 (a matrix
  exponential of a general matrix times amounts). The eleven run 1 misses (24, 34, 37–44 and the rest) are all notation:
  the angle given by arccos, arcsin, artanh or arg restated as its slope or share equal to the same expression.
- **G2′ killed**: other laws 10 of 51 notation (19.6%, against ≤ 10%): 11, 12, 17, 21, 29, 61, 87, 106, 108, 115.
- **G3′ killed**: 78 of 120 = 65.0%, against 54.2% ± 8.

Read, post hoc and untested. The ten "other" laws that went notation are of three kinds: angles given by an inverse
function of a ratio of like quantities, which the settled sentence now covers (11 and 12, rapidity as artanh or ½·ln of
energies; 61, the true anomaly by arg; 87, the phase by arctan + nπ); stated angle values, restated as the direction's
shares (21 and 29, π/2; 106 and 108, multiples of π; DVE's "a stated value" leak again); and a direction read from a sine
or cosine of an angle (17, the aberration's sine difference restated exactly and at first order; 115, cos(φ₁ − φ₂) read as
the share between two phasors). So the fix settled the chart side, as run 1's misses predicted, and moved the same laws
on the other side: the blind judge reads ln and artanh of energies, arg and a phase solved for as not charting a direction,
the brief now restates them as one. The disagreement left is between the judge's reading of "a ratio charted" and the
brief's, not the checker's. Not a fresh test (stated above); a fresh list with both the judge's brief and the restater's
carrying the same sentence on angle outputs and stated values would be.
