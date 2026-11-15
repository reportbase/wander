# DVI: the chart rule with ranges and turn totals settled, on a fresh list, predicted first

15 November 2026. Tom: "fx and test" (fix and test). DVH (R1004) held the chart side (98%) and leaked on the other side
at one boundary: ranges of an angle and a whole turn added to one (DVH 27, 29, 30, 55, 74), which the judge classed "a
turn as a range or total" and the restater took as statements about directions; and an approximation whose right side
restated whole (108). This run settles both in the same words in both briefs, keeps DVH's two sentences, and tests the
rule on a tenth list from ten Wikipedia articles not used before: Spherical coordinate system, Polar coordinate system,
Quaternions and spatial rotation, Haversine formula, Total internal reflection, Stereographic projection, Lorentz factor,
Waveplate, Precession, Ellipse.

## The sentences, in both briefs

DVH's two, unchanged:
1. **An angle given by an inverse circular or hyperbolic function of quantities** forming a ratio of like quantities is
   that ratio's chart: the judge classes it chart; the restater restates it by the angle's slope (or share, or
   half-slope) equal to the same expression.
2. **A stated value of a direction's angle** (θ = π/2, φ = 0, ±π) is a chart: chart; restated as the direction's shares
   or slope.

Added:
3. **A range of a direction's angle** (0 ≤ θ ≤ π, 0 ≤ φ < 2π) is a statement about which directions are meant: the
   judge classes it chart; the restater restates it as the same set of directions in shares or slopes. **But an angle
   carrying whole or half turns as an amount** (2π + 2·arctan(b/a), a total turned through, a number of turns, 2πn
   counted) is not a direction's angle: the judge classes it other; the restater marks it content, since its direction
   alone drops the turns.
4. **An approximation** (≈, ≅, ∼, O(·), "to first order") is not an exact relation: the judge classes it other; the
   restater marks it content, whatever its sides restate to.

## The list, the class, the restatements (as DVH)

`runs/dvi/fetch.py`, a fresh lister to `runs/dvi/laws.md`, `runs/dvi/sample.py` (seed 15112026, 120 if more); a fresh blind
judge with DVG's definition and the four sentences to `runs/dvi/chart.md`; a fresh restater with NTN's rule, the four
sentences and the checker to `runs/dvi/restate.py`, the checker printing no class split to it; I read every passing
restatement and record, before counting, any I judge not the same relation; the count by the rule is the one scored.

## Predictions (committed before any fetch)

- **I1** Laws judged chart are notation at 85% or more. Kill: under 85%; void if fewer than 15 chart laws.
- **I2** Laws judged other are notation at 10% or less. Kill: over 10%; void if fewer than 15 other laws.
- **I3** The overall notation share is (0.92·n(chart) + 0.03·n(other))/n, computed from the blind classes before the
  restatements are checked, and the true share is within 8 percentage points of it. Kill: further.

The rates are DVG's and DVH's, unchanged.

## Runs

(appended below as they come out; nothing above this line edited afterwards)
