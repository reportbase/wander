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

### Run 1 (15 Nov 2026; `runs/dvf/fetch.py`, list `runs/dvf/laws.md`, entry `runs/dvf/entry.md`, restatements
### `runs/dvf/restate.py`, each by its own fresh agent; scored by `runs/dvf/dvf.py`, F3's expectation
### `runs/dvf/dvf-expect.txt` committed before the check, output `runs/dvf/dvf-run1.txt`)

Pages fetched (revision id, timestamp, sha256 of the wikitext; the wikitext not committed):

| page | revision | timestamp | sha256 |
|---|---|---|---|
| Rutherford scattering | 1278074607 | 2025-02-28T09:49:33Z | 7921583abecbb7921e4c01383a3b43fab56daa9638caec83e2904e8044af25a2 |
| Polarizer | 1338353981 | 2026-02-14T17:53:54Z | 1fec304f0d1cb14185e05a7c93efa888983a2817a82af7cf46117cbb1d543d51 |
| Equation of time | 1381509323 | 2026-10-23T00:30:01Z | 80bfc3c456fab9f65956362becffa7275f55d1d01f7cdf13c193e24fdec01a99 |
| Lorentz transformation | 1385400869 | 2026-11-13T03:39:42Z | c96315da01436e818e3acc7d342bd7392a06f3f479a00f60e0d825cb93722f95 |
| Circular motion | 1380824345 | 2026-10-18T04:04:37Z | ab76d517ab6603f7f185bfb03eafce4a20852b8370d0e0d7bc9b1c939d29ffda |
| Simple harmonic motion | 1382617956 | 2026-10-29T14:05:05Z | 8a483e2f18a51dd359b8d5d5740c1a7a76808ae289bb90b7254d155319a9c066 |
| Range of a projectile | 1316627857 | 2025-10-13T16:19:52Z | c0bc7fa3bc5a8234a7589da576c9bf20bdbc972723c7874f26decae1ad8f800f |
| Sextant | 1381090940 | 2026-10-19T23:55:50Z | 46de0883752c2854578b1da135305d1a41ab711afc6e857c60501856bef3a737 |
| Celestial navigation | 1385516178 | 2026-11-13T18:13:48Z | fa2149c4cbfe6edc2585d85e30676bdd73e9336f4ff7450a4b4be8a3e85525b7 |
| Relativistic Doppler effect | 1381425946 | 2026-10-22T11:43:57Z | 003fb63c7ae0d1b675f15accecae0f5807ddc247a0d80a7752475407b6812578 |

96 candidate blocks (Range of a projectile, Sextant and Celestial navigation gave none carrying π or e; Rutherford
scattering's were all fragments or duplicates); the list agent kept 78 laws (dropped 14 fragments, merged 4 duplicates),
under 120, so no sample. Entry, blind, by the sharper rule: dir 13, other 65. F3's expectation, written before the check:
(0.92·13 + 0.03·65)/78 = 17.8%. Departures from DVE's briefs, for the record: the restater was also told to restate the
whole relation, never one side (after DVE's law 29), and to avoid whole words that the checker scans for. The restater
claimed 28 notation; all 28 pass the check, and read before counting I judge all 28 the same relation (law 18's implicit
α = λ − arcsin(y·sin(α + λ)) restated as its closed solution tan α = (1 − y)/(1 + y)·tan λ, with the same solutions).

- **F1 void**: 13 laws judged dir, under the 15 the plan asked for; all 13 are notation.
- **F2 killed**: 15 of 65 laws judged other are notation (23.1%, over 10%): 22, 34–38, 40, 41, 45, 53–55, 59, 60, 72.
- **F3 killed**: 28 of 78 = 35.9%, against the 17.8% expected (18.1 points).

Said plainly: the direction side held again (13 of 13 here, 52 of 52 in DVE, 65 of 65 across the two fresh lists), but
the other side leaked more than in DVE, and in new places. The sharper rule moved halves, doubles and complements into
dir; the leaks this time were cases its definition put in other on purpose: hyperbolic functions of a rapidity (8 laws,
each restated in the celerity slope s = sinh ζ, with cosh ζ = √(1 + s²)), complex exponentials of a direction's angle
(3, e^(iθ) written as across share plus i times up share), a phase that is the direction of a coefficient vector (3),
and one series in the mean anomaly (1). So "where π or e enters", written down before the list, has twice failed to
predict the content side; each list finds a new kind of notation the definition did not name.

Post hoc, untested: across DVE and DVF the notation laws are those whose transcendental is a chart of a ratio of two
coordinates, circular (an angle) or hyperbolic (a rapidity), with no time or length inside the function and no whole
turn taken as a total. That is closer to NTN's rule restated than to a rule about entry, which may be why every attempt
to name the entry beforehand has left something out.
