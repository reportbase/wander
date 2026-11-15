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
