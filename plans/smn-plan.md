# SMN: "find the z" in a second domain, ambient seismic noise

*12 November 2026, SPN R923. Tom: "Proceed", to Claude's offer of a second test of *Reads and Writes* §12 O6 ("A second
test that can fail"). Real data, prediction first. Plan, data choice, method and predictions written and committed before
any seismic data is fetched. Nothing above the "Runs" line is edited after the run.*

## The question

*Reads and Writes* §11 (R719) says a Cauchy-type law met in data is a turn's heat only where the turn can be named apart
from the law's shape, and that a fat tail alone is no evidence. It has passed once (LIGO's direction [H1 : L1], LGO) and
failed once (seed dispersal, TCF: the fat tail a mixture of amounts, no turn found). O6 asks for a second domain where the
turn is named before the data.

Here the turn is the direction of horizontal ground motion. A seismometer's two horizontal channels, x and y, are two
parties; the reading is the slope y/x, the direction [x : y]. The amounts are x and y themselves, and how loud the ground
is. The test sorts the two: the direction should carry a Cauchy fixed by the channels' second moments alone, while the
amounts carry a fat tail that is not a Cauchy and not a turn's.

## Known beforehand (stated so the test is not taken as blind where it is not)

- **Classical.** If (x, y) is elliptically contoured, any law of the form f(Q) with Q the quadratic form of a fixed shape
  matrix (a Gaussian, or a Gaussian whose overall scale varies at random, a scale mixture), then y/x is exactly Cauchy
  with location m = ρ·σy/σx and scale γ = (σy/σx)·√(1 − ρ²), ρ the correlation and σ the spreads of the shape matrix,
  whatever the mixture of scales. Equivalently the angle of (x, y), after the shape is undone, is uniform. So a common
  amplitude that varies over time cancels from the direction and stays in the amounts. This is the turn named: the
  direction, uniform once the drawing (the shape matrix) is undone, and z = m + iγ computed from it.
- **The physics risk.** Ambient seismic noise is not guaranteed isotropic. The secondary microseism (about 0.1–0.3 Hz)
  comes largely from ocean storms and travels as Rayleigh waves, whose horizontal motion is along the direction of travel,
  so a station often sees preferred azimuths that change with the weather; higher frequencies (about 1–5 Hz) are more
  local and cultural (traffic, wind, machinery) and can also be directional; earthquakes in the week arrive from one
  direction each. Any of these can make the direction law non-elliptical. That is how the test can fail.
- **The corpus.** LGO (`plans/lgo-plan.md`) found the LIGO amounts' tail a Student t and transients (a scale mixture), and
  the direction [H1 : L1] Cauchy with its corner at the drawing's c; TCF (`plans/tcf-plan.md`) killed the turn reading
  for seeds. R719: "a fat tail alone is no evidence." draw's labs (where many Cauchy questions were answered in controlled
  form) are not attached to this session and were not checked; this test is on real data, which they do not hold.
- What the seismic data looks like was not looked at before this plan; no station's polarization for the week chosen is
  known to me.

## Data (fixed now)

- **Source.** IRIS DMC FDSN dataselect web service (service.iris.edu), open, no login; the waveforms are the networks'
  (IU: GSN, IRIS/USGS), distributed openly. Fetched with ObsPy. The sha256 of each miniSEED file as fetched goes under the
  runs; the data is not committed.
- **Stations and channels.** Three GSN stations far from coasts and from each other: IU.ANMO (Albuquerque, New Mexico),
  IU.KONO (Kongsberg, Norway), IU.HRV (Harvard, Massachusetts). Location 00, the two horizontal broadband channels BH1 and
  BH2 (40 samples a second). Their azimuths do not matter: any two square horizontal channels give the same law up to a
  turn of the drawing, which z absorbs. If a station has no BH1/BH2 at location 00 for the week, BHN/BHE at 00, then 10;
  if neither, the station is dropped and the run says so (no replacement chosen afterwards).
- **Time.** 2026-09-01T00:00 to 2026-09-08T00:00 UTC, one week. Half A the first 3.5 days, half B the rest.
- **Bands.** Two, fixed: B1 0.1–0.3 Hz (the secondary microseism), B2 1–4 Hz. Each a 4-pole Butterworth, zero phase,
  applied to each channel after removing its mean and linear trend over each contiguous segment; gaps split segments, and
  segments shorter than an hour are dropped. Counts, not ground motion: both channels share one instrument, and a
  difference of gain is a change of drawing, absorbed into σy/σx.
- **Samples.** After filtering, every 10th sample (4 a second), so the samples are not all neighbours; the statistics are
  read as distances between laws, not p-values (neighbouring samples are correlated).

## Method (fixed now)

- **z from half A.** ρ, σx, σy from the sample covariance of (x, y) over half A in the band; m = ρσy/σx,
  γ = (σy/σx)√(1 − ρ²).
- **The direction on half B.** The ratio r = y/x on half B, compared with Cauchy(m, γ) by the Kolmogorov–Smirnov
  distance D (largest gap between the two distribution functions). Reported also: the median of r against m, the
  quartiles against m ± γ, and the angle of the undone pair (the drawing removed with half A's shape) against uniform.
- **The discriminator.** Half B cut into hours; each hour's loudness the RMS of √(x² + y²). The quietest quarter of hours
  against the loudest quarter: D between their laws of r, and D between their laws of |x| (standardized by half A's σx).
- **The amounts.** Each channel's excess kurtosis over the week; and the distance D of standardized x from the best-fitting
  Cauchy (location and scale by the median and half the interquartile range) and from the best Gaussian (by its standard
  deviation).

## Predictions (written before any data)

Six station-bands (three stations × two bands).

- **N1 (the amounts are a scale mixture, not a turn).** In at least four of six station-bands, each channel's excess
  kurtosis exceeds 3, and standardized x is at least 0.05 from the best Cauchy in D. *Killed* otherwise. (Background: if
  the amounts are near Gaussian the discriminator below has no teeth; reported, and the test goes on.)
- **N2 (the turn named: z from the second moments).** On half B, D(r, Cauchy(m, γ)) < 0.03, with m and γ from half A, in at
  least four of six station-bands. *Killed* if in three or more D ≥ 0.03.
- **N3 (the scale mixture cancels from the direction).** The law of r in the loudest quarter of hours against the quietest:
  D < 0.03 in at least four of six, while for |x| the same comparison gives D > 0.3 in those same station-bands. *Killed*
  if the ratio's D ≥ 0.03 in three or more.
- **N4 (the band matters, as the physics risk says).** Where N2 fails, the undone angle is not uniform (D from uniform
  ≥ 0.03), and the failure is in B1 more often than in B2. *Killed* if a failure of N2 comes with an angle within 0.03 of
  uniform (then the Cauchy failed for a reason the turn does not name).

## What would and would not be shown

- N2 and N3 not killed: in a second domain, a Cauchy appears exactly where the turn is named (the direction of the
  ground's horizontal motion, z from the drawing), unmoved by how loud the ground is, while the amounts carry a fat tail
  that is not a Cauchy. That is the sort working where the turn can be named before the data. It is classical (elliptical
  ratios); what is tested is whether the real noise field meets the premise, and whether the sort calls it right.
- N2 killed with N4 not killed: the direction is not uniform at that station and band (a preferred azimuth, a source),
  so no turn is there to name and the paper predicts no Cauchy; a failure of the noise field's isotropy, consistent with
  R719, and recorded as the test failing in its letter.
- N4 killed: a Cauchy missing where the angle is uniform would be against the rule as stated.
- Nothing about what seismic noise is made of, or about the brain, eyes or instruments in general.

## Runs
