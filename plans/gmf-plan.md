# GMF: "find the z" in a third domain, the geomagnetic field

*25 November 2026, SPN R1233. Tom: "1,2,3,4", item 3 ("back to the read": the read's own open questions, *Reads and Writes*
§12). Of §12's open items only O6 ("a second test that can fail") can fail on data. Real data, prediction first: plan,
data choice, method and predictions written and committed before any geomagnetic data is fetched. Nothing above the
"Runs" line is edited after the run.*

## Where O6 stands (said, since §12's text is behind)

O6 as written: "find the z" passed once in data (LIGO, LGO) and failed once (the seeds, TCF). Since then, and not yet in
§12: SMN (ambient seismic noise) passed in the 1–4 Hz band at 8 of 9 station-weeks and failed in the microseism band,
where the motion is directional, so no turn was there to name; WND (one-minute surface wind) failed, the turn not
nameable at the data's resolution. This is a third domain, chosen before the data, by SMN's method unchanged.

## The question

The turn here is the direction of the horizontal geomagnetic field's change. A magnetometer's two horizontal components,
north X and east Y, are two parties; the reading is the slope of the change, ΔY/ΔX (after a band filter), the direction
[ΔX : ΔY]. The amounts are the changes themselves, how disturbed the field is. The sort says: where the change's
direction is a turn (uniform once the drawing, the shape of the covariance, is undone), the slope carries the Cauchy at
z = m + iγ fixed by the second moments of a first stretch of data, whatever the field's loudness; the amounts carry a fat
tail that is not a Cauchy.

## Known beforehand

- **Classical**, as in SMN: for (x, y) elliptically contoured (a Gaussian or a scale mixture of one shape), y/x is exactly
  Cauchy with m = ρσy/σx, γ = (σy/σx)√(1 − ρ²). A common amplitude that varies cancels from the direction.
- **The physics risk.** Geomagnetic variations are not known to be isotropic in the horizontal plane. The daily solar
  quiet variation (Sq) and storm-time ring current act mainly along the north component at mid latitudes; pulsations
  (Pc3–Pc5) are often polarized; at high latitude the auroral electrojet drives strongly north–south changes during
  substorms. A loudness-dependent direction (storms more north–south than quiet times) would break the elliptical premise
  and fail N3. The band filter removes Sq's daily period in both bands. How strongly polarized these stations' changes
  are in the week chosen is not known to me; no data for it has been looked at.
- **The corpus.** SMN is the template; LGO the first pass; TCF and WND the failures.

## Data (fixed now)

- **Source.** The USGS Geomagnetism Program's web service (geomag.usgs.gov/ws/data/), definitive or best-available
  one-minute values, public domain (U.S. Government work). Elements X and Y (geographic north and east, nT). If the
  service does not answer, INTERMAGNET's BGS GIN service with the same stations, codes and dates; if neither, the run
  says so and stops. The sha256 of each file as fetched goes under the runs; the data is not committed.
- **Stations.** Three, fixed: BOU (Boulder, Colorado, mid latitude), FRD (Fredericksburg, Virginia, mid latitude), CMO
  (College, Alaska, auroral). A station with more than 10% of the week missing is dropped and the run says so (no
  replacement chosen afterwards).
- **Time.** 2026-10-01T00:00 to 2026-10-08T00:00 UTC. Half A the first 3.5 days, half B the rest.
- **Bands.** Two, fixed, on the one-minute series after removing each segment's mean and linear trend (gaps over 5
  minutes split segments; segments under 6 hours dropped; shorter gaps linearly filled): B1 periods 2–10 minutes, B2
  periods 10–60 minutes, each a 4-pole Butterworth band-pass, zero phase.
- **Samples.** Every second sample of the filtered series; the statistics read as distances between laws, not p-values.

## Method (fixed now; SMN's)

- **z from half A.** ρ, σx, σy from the sample covariance of the filtered (X, Y) over half A; m = ρσy/σx,
  γ = (σy/σx)√(1 − ρ²).
- **The direction on half B.** r = Y/X on half B against Cauchy(m, γ), the Kolmogorov–Smirnov distance D; also the median
  against m, the quartiles against m ± γ, the undone angle against uniform.
- **The discriminator.** Half B cut into hours, each hour's loudness the RMS of √(X² + Y²); the quietest quarter of hours
  against the loudest: D between their laws of r, and between their laws of |X| standardized by half A's σx.
- **The amounts.** Each component's excess kurtosis over the week; D of standardized X from the best Cauchy (median and
  half the interquartile range) and from the best Gaussian.

## Predictions (written before any data)

Six station-bands.

- **G1 (the amounts are a scale mixture).** In at least four of six, each component's excess kurtosis exceeds 3 and
  standardized X is at least 0.05 from the best Cauchy in D. *Killed* otherwise.
- **G2 (the turn named).** On half B, D(r, Cauchy(m, γ)) < 0.03, m and γ from half A, in at least four of six. *Killed* if in
  three or more D ≥ 0.03.
- **G3 (the mixture cancels from the direction).** The loudest quarter of hours against the quietest: the law of r within
  D < 0.03 in at least four of six, while |X|'s comparison gives D > 0.3 in those same station-bands. *Killed* if the ratio's
  D ≥ 0.03 in three or more.
- **G4 (where it fails, the angle is not uniform).** Where G2 fails, the undone angle is at least 0.03 from uniform in D.
  *Killed* if a failure of G2 comes with an angle within 0.03 of uniform.
- **G5 (where, if anywhere).** If G2 fails anywhere, it fails at CMO (auroral) before the mid-latitude stations, and in
  B2 before B1. Not a kill condition on its own; scored and reported.

My own expectation, said so it can be held against me: I expect G1 to hold (geomagnetic changes are notoriously
heavy-tailed), and G2 and G3 to be at risk, more likely failed than not at CMO, with the mid-latitude short band the best
chance of a pass.

## What would and would not be shown

- G2 and G3 not killed: a third domain where the Cauchy appears exactly where the turn is named, unmoved by loudness,
  with the amounts' fat tail not a Cauchy. The sort working; classical in its mathematics.
- G2 killed with G4 not killed: the change's direction is not a turn here (a polarization), so the rule predicts no
  Cauchy, and none is there: consistent with R719, the test failing in its letter.
- G4 killed: a Cauchy missing where the angle is uniform, against the rule as stated.
- Nothing about what drives the field.

## Runs
