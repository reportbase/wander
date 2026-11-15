# DVF: the sharper entry rule, predicted first

15 November 2026. Tom: "merge and test the sharper rule". DVE (R1000) tested the entry rule on a fresh list: every law
whose π or e entered only through a direction's angle restated (52 of 52), but 13 of 68 laws judged "other" restated too
(E2 killed). Read after the fact, the 13 were the judge's boundary calls: an angle halved, doubled or taken as a
complement (a half, a double or a complement of a direction is a direction), an angle standing beside its own rate, and
one stated value. The sharper rule moves those cases into the direction class. This run tests it on a sixth list, with
its rates committed first and a fresh blind judge given the sharper definition.

## The list (fixed before anything is fetched)

Ten Wikipedia articles, none used on an earlier list: Rutherford scattering; Polarizer; Equation of time; Lorentz
transformation; Circular motion; Simple harmonic motion; Range of a projectile; Sextant; Celestial navigation;
Relativistic Doppler effect.

The steps are DVE's, unchanged but for the paths (`runs/dvf/`): `runs/dvf/fetch.py` (DVE's script, pages changed) records
revision ids and sha256s (the wikitext not committed) and pulls every `<math>` and `{{math|…}}` block carrying π or e into
`runs/dvf/candidates.md`; a fresh agent, given only that file, writes `runs/dvf/laws.md` by DVE's instructions; if more
than 120 laws remain, `runs/dvf/sample.py` (DVE's, paths changed) keeps a seeded sample of 120 (seed 15112026), in order.

## Blind entry, the sharper rule (a fresh agent, given only `runs/dvf/laws.md` and this definition)

For each law, where does π or e (in any form: π, a degree constant, e, exp, log, ln, a circular or hyperbolic function or
its inverse) enter?
- **dir**: only inside circular functions (or their inverses) of angles that are directions or are built from directions
  by adding, subtracting, halving, doubling or taking a whole-number multiple, or by taking a complement or supplement
  (π/2 − θ, π − θ, 90° − θ). A direction is an angle between two lines or rays, a heading, an incidence, a scattering
  or polarization angle, a slope's angle, a position on the sky or an angle of a pendulum or arm. Amounts may appear
  anywhere outside those functions, multiplying or adding to them, including the angle's own rate or its derivative.
- **other**: anywhere else, in whole or in part: a whole or half turn as a total or a free constant (2π, π, 360°) not
  standing as a complement or supplement inside a circular function; a circular or exponential function of an amount or
  of a quantity built from amounts (ωt, kx, a phase, a mean anomaly or hour angle computed from a time); a logarithm or
  exponential of anything; a hyperbolic function; a limit, series, product or integral; a numerical value given in place
  of a relation; an approximation.
Writes `runs/dvf/entry.md`, one line a law, `n. dir|other: reason`.

## Restatements (a second fresh agent, given the list, NTN's rule and the checker, not the entry classes or predictions)

As DVE: NTN's rule and DVA's borderline, to `runs/dvf/restate.py`, checked by NTX's checker (`runs/dvf/check.py`). I read
every passing restatement and record, before counting, any I judge not the same relation; the count by the rule is the
one scored.

## Predictions (committed before any fetch)

- **F1** Laws judged dir are notation at 85% or more. Kill: under 85%; void if fewer than 15 dir laws.
- **F2** Laws judged other are notation at 10% or less. Kill: over 10%; void if fewer than 15 other laws.
- **F3** The overall notation share is (0.92·n(dir) + 0.03·n(other))/n, computed from the blind entry classes before the
  restatements are checked, and the true share is within 8 percentage points of it. Kill: further.

The rates are DVE's, kept unchanged; read through the sharper rule after the fact, DVE's list would have put about 61 of
61 dir laws and 5 of 59 other laws among the notation, so 0.92 and 0.03 are not tuned to it.

## Runs

(appended below as they come out; nothing above this line edited afterwards)
