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
