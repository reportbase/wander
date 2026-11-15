# DVC: a fourth list, rich in laws among directions

15 November 2026. Tom: "Merge and run 4". DVB (R998) could not test the three-in-five reading: Wikipedia's physics
equation lists held only 4 laws relating directions alone (Q2 void). This run takes a list where such laws should be
common (refraction, reflection, diffraction by crystals, coordinates on the sky), chosen before anything is fetched, and
tests the same four predictions. DVA's reading (R996), untested: laws relating only directions without a limit are
notation about three times in five (27 of 43 and 14 of 24 on the first two lists); laws with an amount and no limit about
one time in ten (4 of 41; 7 of 64 on DVB's).

## The list (fixed before anything is fetched)

Ten Wikipedia articles, their equations as Wikipedia's editors wrote them:
Snell's law; Fresnel equations; Brewster's angle; Minimum deviation; Bragg's law; Miller index; Astronomical coordinate
systems; Position of the Sun; Sunrise equation; Aberration (astronomy).
(Spherical trigonometry and List of trigonometric identities were considered and left out: mathematics, not laws of
physics. Total internal reflection was left out as largely repeating Snell's law and the Fresnel equations.)

The steps are DVB's, unchanged but for the paths (`runs/dvc/`): `runs/dvc/fetch.py` fetches the wikitext and records
revision ids and sha256s in the run entry (the wikitext not committed); it pulls every `<math>` and `{{math|…}}` block
carrying π or e in any form (DVB's pattern) into `runs/dvc/candidates.md`; a fresh agent, given only that file, writes
`runs/dvc/laws.md` by DVB's instructions; if more than 120 laws remain, a seeded sample of 120 (seed 15112026), in order.

## Blind sorting and restatements

As DVB, each by its own fresh agent given only `runs/dvc/laws.md` and the definitions, verbatim: the class (A, L, X) to
`runs/dvc/blind-class.md`; the tag (D, A) to `runs/dvc/tags.md`; the restatements by NTN's rule, with DVA's borderline,
to `runs/dvc/restate.py`, checked by NTX's checker (`runs/dvc/check.py`). I read every passing restatement and record,
before counting, any I judge not the same relation; the count by the rule is the one scored.

## Predictions (committed before any fetch)

Cells are the blind tag crossed with the blind class: "no limit" means class A or X, "a limit" class L.

- **Q1** Every law classed L is content. Kill: one notation law classed L.
- **Q2** Laws tagged D with no limit are notation at 45% to 75%. Kill: outside, or fewer than 10 such laws (then void).
- **Q3** Laws tagged A with no limit are notation at under 20%. Kill: 20% or more; void if fewer than 10 such laws.
- **Q4** The overall notation share is 0.60·n(D, no limit) + 0.10·n(A, no limit), divided by the number of laws, computed
  from the blind tags and classes before the restatements are checked, and the true share is within 8 percentage points
  of it. Kill: further.

DVB's post hoc reading (π or e entering only through a direction's angle used by its cosine, sine or tangent) is not
tested here as a prediction; if the run bears on it, that is reported as post hoc.

## Runs

(appended below as they come out; nothing above this line edited afterwards)

### Run 1 (15 Nov 2026; `runs/dvc/fetch.py`, list `runs/dvc/laws.md`, tags `runs/dvc/tags.md`, classes
### `runs/dvc/blind-class.md`, restatements `runs/dvc/restate.py`, each by its own fresh agent; scored by `runs/dvc/dvc.py`,
### Q4's expectation `runs/dvc/dvc-expect.txt` committed before the check, output `runs/dvc/dvc-run1.txt`)

Pages fetched (revision id, timestamp, sha256 of the wikitext; the wikitext not committed). The first fetch was rate-limited
by Wikipedia after one page; the script was changed to look up all revisions in one call and reuse the page already saved.

| page | revision | timestamp | sha256 |
|---|---|---|---|
| Snell's law | 1379958766 | 2026-10-12T23:10:36Z | 5017bf88039e59cdf709776cc2ebe3d3ef5ad65285b550ee9ab4e82c268d14a9 |
| Fresnel equations | 1382000106 | 2026-10-26T00:13:51Z | 97db6a2212ccf88929c99f7076d90186d442f1204fd06e0b5bd8fdd17044fbbf |
| Brewster's angle | 1373604193 | 2026-09-06T21:29:39Z | 830c34f30412789b997c0b6ab0097ea64f5f46cb6ef396add20d66dc02db8ce6 |
| Minimum deviation | 1364567115 | 2026-07-17T06:57:24Z | 76800cd0be42f4058c5c5373902ebc23e647100cafd06f52d1c99360935be5b8 |
| Bragg's law | 1361393274 | 2026-06-27T17:46:35Z | eb78ea58bcbf9b3dba04192a00e15f8863ffed35384e7590c2750bd845d47011 |
| Miller index | 1379286464 | 2026-10-09T01:51:22Z | 11852c6f6d2459fa87fb264e0a2b021206c83801a089e6d31850fa9797c2415f |
| Astronomical coordinate systems | 1379791040 | 2026-10-11T23:51:53Z | 73183a308d13065c86412c416607a1a74a8a1d251d6d40bbf9ce6cc664871fdc |
| Position of the Sun | 1369082038 | 2026-08-12T20:08:59Z | ad2fbc1a857be6d3436531bbf730b6deaefedcd34f04c1e0ac3650e7354577e5 |
| Sunrise equation | 1379585755 | 2026-10-10T21:19:54Z | a5555be3cb0d39dd37cbc9cd7cbed27dadedf4781d81ff4338c8a57e9fabad42 |
| Aberration (astronomy) | 1380017575 | 2026-10-13T08:08:17Z | 0941719fdaa6a67c7a1d2fab8b9ea2911292d4b03240dbf7bdc6e878c8e3e5e4 |

145 candidate blocks; the list agent kept 119 laws (dropped 20, merged 6 duplicates), under 120, so no sample. Tags D 66,
A 53; classes A 119, L 0, X 0 (every law classed as entering through an angle's chart). Q4's expectation, written before
the check: (0.60·66 + 0.10·53)/119 = 37.7%. The restater claimed 101 notation; all 101 pass the check. Read before
counting, I judge all 101 the same relation; noted: 63, 67 and 71 equate angles (the minimum deviation, a worked step),
restated as equal slopes or half-slopes, which is one to one on the range used.

- **Q1 not killed, but untested**: no law was classed L, so there was nothing to fail.
- **Q2 killed**: 61 of 66 laws tagged D with no limit are notation (92.4%, above 75%).
- **Q3 killed**: 40 of 53 laws tagged A with no limit are notation (75.5%, against under 20%).
- **Q4 killed**: 101 of 119 = 84.9%, against the 37.7% expected (47 points off).

Said plainly: on a list rich in directions the three-in-five rate does not hold; nine in ten laws among directions are
notation, and so are three in four laws in which an amount enters. The tag (whether an amount enters) does not predict
the rate here: Bragg's 2d·sin θ, the Fresnel coefficients with admittances, the Sun's X = R·cos λ carry amounts, and π
enters them only through a direction's share, so they restate. The 18 content laws are where π or e enters otherwise: the
whole turn as a total (2π/λ, 2π/|g|: 8, 78, 79), an exponential of a phase built from amounts (e^(i k·r): 30–32, 37, 38),
angles made from day counts or degrees treated as amounts (87, 95–98, 103), rounded numerical examples (14, 15), the
small-angle approximation (110) and a half turn written as ½π (111).

Post hoc, untested: on four lists the cut that sorts notation from content is not the tag but where π or e enters: only
through a direction's angle, used by its cosine, sine or tangent (notation), or through a total, a limit, or a function of
an amount (content). This is DVB's post hoc reading again; it fits this list after the fact and needs a run with its own
prediction. A second caution: one fresh restater did this list and another the earlier ones; the checker confirms every
claimed restatement exactly, but a restater that misses restatements lowers a list's rate, which this design cannot see.
