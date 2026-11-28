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
