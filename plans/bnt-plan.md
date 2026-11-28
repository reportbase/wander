# BNT: Born's weight as the read's share, on a Bell test's counts

*Plan written 28 November 2026, before any data was fetched or looked at. SPN R1291. Tom: "Merge, then run the test that
can fail", of `plans/born-reread.md`'s second offer.*

## What is tested

`plans/born-reread.md` sorted Born's rule:
- the ray is a read;
- the weight of each outcome is the read's share, rational in the slope (here the half-slope t = tan(φ/2) of the Bloch
  angle φ between the two analysers);
- each click is a write, and a frequency is a count tending to the share.

The draft it re-read took the Cauchy's own share (an arctangent, linear in the angle) for Born's number. For a
singlet-like pair, the two rules give different correlations between the two sides' outcomes:
- **Born:** the read's share gives E(φ) = −v·(1 − t²)/(1 + t²) = −v·cos φ, with one visibility v for every setting.
- **The draft:** a share linear in the angle gives E(φ) = −v·(1 − 2φ/π), the shape of Bell's local model (TPR).

At φ = 0, 90° and 180° the two agree, so tomography in H/D/R bases cannot tell them apart (checked before choosing data:
the Innsbruck tomography set, Zenodo 10927445, uses only those). They part at 45° and 135°, where Born gives ±1/√2 and
the linear share ±½. A Bell test with CHSH settings (analysers 0°/45° on one side and 22.5°/67.5° on the other, Bloch
angles 45° and 135°) is the case.

## Data

Weihs et al. 1998 (PRL 81, 5039), Innsbruck, long distance, polarisation-entangled photons. Coincidence counts per
setting pair and outcome, as summarised in Gill et al., *Optimal statistical analyses of Bell experiments*
(arXiv:2209.00702). The raw time tags are on Zenodo 7185335 (1.1 GB) and are not used in this run: their coincidence
windowing is a known analysis choice of its own. The source, licence and sha256 are to be recorded below once fetched.
If the paper gives no counts per outcome, the run stops and says so.

## Predictions (fixed now)

**P1 (one visibility).** The four CHSH correlations E(a, b), each from its four coincidence counts, take the form
±v/√2 with one v fitted from all four.
- Killed if χ² on 3 degrees of freedom (binomial errors) has p < 0.001.
- Killed if the fitted v is above 1 by more than 3 standard errors.

**P2 (not the linear share).** With v ≤ 1, the linear share bounds |S| by 2. Prediction: |S| > 2 by at least 5
standard errors.
- Killed otherwise.
- If P2 holds, the draft's rule is killed for every v.

**P3 (the share has no other side's setting in it).** Each side's single-outcome share, taken from coincidences, does not
depend on the other side's setting.
- For each side and each of its settings, the two values (one per setting of the other side) agree within binomial
  error. Killed if any of the four comparisons has p < 0.001.

**P4 (no Cauchy in the counts).** P4 is untested on summary counts and is stated for the raw run only. Per-block
frequencies at one setting pair scatter binomially (dispersion index within [0.7, 1.5]), with no heavy tail.

## What it can and cannot show

- **Born's rule.** These are standard quantum results (S = 2.73 ± 0.02 is the published value, known before this plan).
  A P1–P3 pass therefore confirms Born's rule as the bridge, not the framing apart from quantum mechanics.
- **What can fail.** The rational share (cos φ in one visibility) against the draft's linear share. P2 kills one of them.
- **Not tested:** why no local assignment of writes gives P2. That is Bell's result, and the framing adds nothing to it.

## Runs

**Data, fetched after the predictions above were committed.** Gill, Larsson et al., *Optimal statistical analyses of
Bell experiments* (arXiv:2209.00702v3, Entropy version of 28 March 2023, CC BY 4.0), Appendix E: the raw counts of
Weihs et al. 1998 per setting pair and outcome, 14,573 coincidences in all. The PDF's sha256 is
bf820b1ebbc71ca97b3f916c25206ee56bd2af41db7a451769087f837aded72b; it is not committed. The counts are typed into
`runs/bnt/bnt.py`. The paper's own figure, S = 2.73, was known beforehand (stated above).

### Run 1 (28 Nov, `runs/bnt/bnt.py`, output in `runs/bnt/run1.txt`)

**P1 killed.**
- One visibility does not fit the four correlations. E = +0.614, +0.708, +0.696 and −0.709 (sd 0.011–0.013).
  v = 0.965 ± 0.009, but χ² = 40.1 on 3, p = 10⁻⁸.
- Setting (1, 1) alone sits at v = 0.87; the other three are 0.98–1.00.
- v is not above 1.

**P2 not killed.**
- S = 2.728 ± 0.024, 29.8 standard deviations past 2.
- The linear share fitted alone needs u = 1.365 ± 0.012, 30 standard deviations above its ceiling of 1. The draft's
  Cauchy share is killed for every visibility.
- Born at the fitted v gives 2√2·v = 2.729.

**P3 killed.** Each side's share, taken from coincidences, moves with the other side's setting: Alice's by z = +4.1 and
−7.9 (p 4·10⁻⁵, 4·10⁻¹⁵), Bob's by +2.8 and +2.0.

**P4 untested** (summary counts only, as the plan said).

### What the kills are

- **P1 is my set-up.** "One visibility" assumed the four analyser settings sat exactly 45° and 135° apart on the Bloch
  sphere, and that alignment and contrast were alike at every setting pair. Neither holds in a real apparatus: (1, 1) is
  off. With the setting angles free, Born fits any four correlations, so P1 had no edge against the draft that P2 does
  not have. It was a test of the apparatus, not of the share.
- **P3 is my set-up.** Shares taken from coincidences are selected by both sides detecting. Only about 1 pair in 400
  gave two detections (Gill et al. §5.5), so the selection can depend on both settings. This is the detection loophole
  and the fair-sampling assumption, and the Weihs data's coincidence marginals are known to vary in this way. A clean P3
  needs singles counted per setting, or an experiment with no such selection.

**Post hoc, not a prediction.** The same script's arithmetic on Zhang et al. 2022 (Munich, event-ready, atoms; Gill et
al. Appendix F, 1,649 trials), which has no coincidence selection:
- S = 2.578 ± 0.075, 7.7 standard deviations past 2.
- Every marginal is independent of the other side's setting: z = −1.3, +1.2, −0.4, +0.9.
- The four v's (0.94, 0.99, 0.85, 0.87, sd about 0.05) sit within a few sd of one mean.
This fits the reading of P3's kill as the Weihs selection's. It was seen after the run and is not counted.

**What stands.**
- The test that can fail is P2, and the draft's share failed it twice, at 30 σ and (post hoc) 7.7 σ.
- Born's weight, the read's share 1/(1 + t²) with t the half-slope, gives correlations of the form cos φ. That form is
  what reaches |S| > 2, and the data reach it.
- As the plan said, this confirms Born's rule as the bridge. It is quantum mechanics passing, not the framing apart from
  it.
