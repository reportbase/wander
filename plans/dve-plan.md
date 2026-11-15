# DVE: where π or e enters, predicted first

15 November 2026. Tom: "Merge and test". DVB (R998) and DVC (R999) each left the same reading after the fact: a law's
π or e is notation (restates in slopes and shares, NTN's rule) when it enters only through a direction's angle, used by
its circular functions or their inverses, and content when it enters any other way. On DVC's list 101 of 101 notation
laws fit it and the 18 content laws were a whole turn as a total, an exponential of a phase built from amounts, degrees
or day counts treated as amounts, or rounded examples. DVA's tag (whether an amount enters) did not predict the rate
(DVC Q3: 75.5% of amount laws notation). This run tests the entry rule on a fifth list, with a blind judge of the entry
and the rates committed first.

## The list (fixed before anything is fetched)

Ten Wikipedia articles, chosen to mix laws among directions with laws of amounts in time and space, none used on an
earlier list: Doppler effect; Diffraction grating; Malus's law; Projectile motion; Pendulum (mechanics); Compton
scattering; Inclined plane; Kepler's equation; Lambert's cosine law; Rayleigh scattering.

The steps are DVC's, unchanged but for the paths (`runs/dve/`): `runs/dve/fetch.py` (DVC's script, pages changed) fetches
the wikitext and records revision ids and sha256s (the wikitext not committed) and pulls every `<math>` and `{{math|…}}`
block carrying π or e into `runs/dve/candidates.md`; a fresh agent, given only that file, writes `runs/dve/laws.md` by
DVC's instructions; if more than 120 laws remain, a seeded sample of 120 (seed 15112026), in order.

## Blind entry (a fresh agent, given only `runs/dve/laws.md` and this definition)

For each law, where does π or e (in any form: π, a degree constant, e, exp, log, ln, a circular or hyperbolic function or
its inverse) enter?
- **dir**: only through one or more angles that are directions (an angle between two lines or rays, a heading, an
  incidence, a scattering or polarization angle, a slope's angle, a position on the sky), used only by circular functions
  or their inverses, or by adding and subtracting such angles;
- **other**: anywhere else, in whole or in part: a whole or half turn as a total or a constant (2π, π, 360°), a circular or
  exponential function of an amount or of a quantity built from amounts (ωt, kx, a phase, a mean anomaly from a time),
  a logarithm or exponential of anything, a hyperbolic function, a limit, series, product or integral, a numerical value
  given in place of a relation, or an approximation.
Writes `runs/dve/entry.md`, one line a law, `n. dir|other: reason`.

## Restatements (a second fresh agent, given the list and NTN's rule, not the entry classes or predictions)

NTN's rule and DVA's borderline, worded as in DVC, to `runs/dve/restate.py`, checked by NTX's checker
(`runs/dve/check.py`, which also reads the entry file for its summary). I read every passing restatement and record,
before counting, any I judge not the same relation; the count by the rule is the one scored.

## Predictions (committed before any fetch)

- **E1** Laws judged dir are notation at 85% or more. Kill: under 85%; void if fewer than 15 dir laws.
- **E2** Laws judged other are notation at 10% or less. Kill: over 10%; void if fewer than 15 other laws.
- **E3** The overall notation share is (0.92·n(dir) + 0.03·n(other))/n, computed from the blind entry classes before the
  restatements are checked, and the true share is within 8 percentage points of it. Kill: further.

The rates 0.92 and 0.03 are taken from DVC's list read through the rule after the fact (dir there about 101 of 110; other
about 0 of 9) and rounded toward the earlier lists; E1's and E2's bounds are set looser than either.

## Runs

(appended below as they come out; nothing above this line edited afterwards)
