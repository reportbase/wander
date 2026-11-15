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

### Run 1 (15 Nov 2026; `runs/dve/fetch.py`, list `runs/dve/laws-all.md` sampled by `runs/dve/sample.py` to
### `runs/dve/laws.md`, entry `runs/dve/entry.md`, restatements `runs/dve/restate.py`, each by its own fresh agent;
### scored by `runs/dve/dve.py`, E3's expectation `runs/dve/dve-expect.txt` committed before the check, output
### `runs/dve/dve-run1.txt`)

Pages fetched (revision id, timestamp, sha256 of the wikitext; the wikitext not committed):

| page | revision | timestamp | sha256 |
|---|---|---|---|
| Doppler effect | 1383797428 | 2026-11-04T22:54:41Z | b6993879679a1544b8f9677bd5414a1c305bc0dc93ee330db7b480d0daf942fe |
| Diffraction grating | 1375182649 | 2026-09-16T07:57:40Z | aa9d7f033be5012da142af26713647e6b7a550b1509dee3e1e568645a5bbe270 |
| Malus's law | 1314322852 | 2025-09-30T20:28:57Z | 2390bd35343b197a744f5cfbce87da8c8a6760a76fe89a5239194e8ef1a53856 |
| Projectile motion | 1377746192 | 2026-09-30T23:25:33Z | a016394e2147efb6a8444ab9d688f6a122595ebd16c7a4286d192ca177a4f50a |
| Pendulum (mechanics) | 1381752772 | 2026-10-24T15:46:11Z | 8197e8bc90ec2302090c8c4d8e7ac2e55b8db0e47b3da25698f4499e1de353ba |
| Compton scattering | 1384097258 | 2026-11-06T15:43:31Z | 37e9985b8bb391d3d044400375c0abc269df794464f5bb75360dcf1c911fb186 |
| Inclined plane | 1352121689 | 2026-05-02T05:00:09Z | 6721d72a981cc132c30e9487a8276200a64b10473f7940a5920ee9d7f69deb9c |
| Kepler's equation | 1360514786 | 2026-06-21T23:22:34Z | 63622e05a66a5909961ab347d9cbbf7fa1f987d6b4f5de39955ccc340293170f |
| Lambert's cosine law | 1381118238 | 2026-10-20T03:09:13Z | d7664b841ad6e4e854c4a8b2974970399a6793bfcd1761f80629b3d253c657ba |
| Rayleigh scattering | 1384103584 | 2026-11-06T16:26:46Z | e80ff99e50c64fe0ae0c9c77d09661e1445ecd1ce2a10bde8f4189cdbfa5699a |

251 candidate blocks (Projectile motion 89 and Pendulum 85 of them); the list agent kept 220 laws, so a seeded sample of
120. Entry, blind: dir 52, other 68. E3's expectation, written before the check: (0.92·52 + 0.03·68)/120 = 41.6%. The
restater claimed 65 notation; all 65 pass the check. Read before counting, I judge two not the same relation: 29 (it
restates one side, "the up share squared") and 85 (it says only that the two sides differ alike); 18 is doubtful (θ =
arctan 4 ≈ 76.0° restated as a family, "height k times range at slope 4k"). By the rule, as the plan says, all 65 count.

- **E1 not killed**: 52 of 52 laws judged dir are notation (100%).
- **E2 killed**: 13 of 68 laws judged other are notation (19.1%, over 10%): 18, 26, 28, 29, 43, 51, 53, 58, 63, 64, 71,
  104, 107. (Without my two, 12 of 68, 17.6%: still killed.)
- **E3 killed**: 65 of 120 = 54.2%, against the 41.6% expected (12.6 points).

Said plainly: the rule's first half held on a fresh list judged blind: where π or e entered only through a direction's
angle, every law restated. Its second half did not: about one in five laws the judge put elsewhere restated too, so the
rule as written sorts the notation laws in but also leaves some out, and the overall rate was missed.

Post hoc, untested: the 13 are the judge's boundary calls, named by the judge before the restatements: an angle halved
(58, 63, 64; 26 and 43 half an arccos), doubled through its inverse (104), the complement π/2 − θ (28, 29), an angle beside
its own rate (51, 53, 71 and 107, a derivative), and a stated value (18). A half, a double or a complement of a direction
is a direction, and its slope is a rational or square-root expression in the first's, so these may belong to dir; with
them moved, other would hold 5 notation laws of 59 or so, mostly an angle appearing beside its own rate. That is a sharper
rule read after the fact, and needs its own prediction.
