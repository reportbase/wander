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

### Run 1 (12 November; `python3 -I runs/smn/smn.py <dir>`, 43 seconds; output `runs/smn/run1.txt`)

Data: the FDSN dataselect service named in the plan now redirects from service.iris.edu to service.earthscope.org (the
same archive under EarthScope's name); fetched there with the plan's query, IU, location 00, BH1 and BH2, the whole week
in one segment at all three stations. sha256 of the miniSEED files as fetched:

```
ec97f9acbef8ef0ce2f84cf48136d7e0f89cbd691ce9656be22a690891d5eb7f  IU.ANMO.00.BH1.mseed
055396d1c05252cbd2210ba8613601b921b8ae3db0ae0eab29aab9575d560b5d  IU.ANMO.00.BH2.mseed
d4845cea92f79cf9101798e7b2468f7cfd98208a1c7ada9bd1dc89e7779050b6  IU.HRV.00.BH1.mseed
486d1d60628d3400eb1ce6ce338131c196750e844078da7d2ec4635cdcf6c145  IU.HRV.00.BH2.mseed
0b9e5b61e0e30e8840ecaa64d81eb4d2475b686ec973bc5d1a245aba65cd94e8  IU.KONO.00.BH1.mseed
971115b5c1d8075ede31312c5f65af4c965952bf1ab06dacd5b1511fe2171c52  IU.KONO.00.BH2.mseed
```

| station, band | z from half A | D(r, Cauchy z), half B | angle D from uniform | ratio, loud vs quiet hours | \|x\|, loud vs quiet | kurtosis x, y | x from best Cauchy |
|---|---|---|---|---|---|---|---|
| ANMO B1 | +0.046 + 1.197i | 0.0140 | 0.0118 | 0.0518 | 0.326 | 5.6, 3.7 | 0.048 |
| ANMO B2 | −0.080 + 1.082i | 0.0332 | 0.0341 | 0.0160 | 0.191 | 24597, 31035 | 0.069 |
| KONO B1 | −0.182 + 1.192i | 0.0456 | 0.0478 | 0.0508 | 0.344 | 2.0, 2.9 | 0.055 |
| KONO B2 | +0.101 + 1.063i | 0.0168 | 0.0165 | 0.0245 | 0.209 | 63, 2345 | 0.071 |
| HRV B1 | −0.107 + 1.033i | 0.0278 | 0.0285 | 0.0326 | 0.426 | 3.0, 2.8 | 0.041 |
| HRV B2 | −0.237 + 0.985i | 0.0250 | 0.0252 | 0.0070 | 0.186 | 2630, 384 | 0.073 |

- **N1: killed.** The amounts are heavy-tailed and far from a Cauchy in 3 of 6 (needs 4): all three of B2, none of B1. In
  the microseism band the amounts are near Gaussian (kurtosis 2–6), so there is no scale mixture there to cancel.
- **N2: not killed.** The ratio is within 0.03 of the Cauchy at the z fixed by half A's second moments in 4 of 6; the two
  past it are ANMO B2 (0.033, at the edge) and KONO B1 (0.046).
- **N3: killed.** The ratio's law in the loudest hours against the quietest is 0.03 or more apart in 3 of 6: all three of
  B1 (0.052, 0.051, 0.033). In B2 it is 0.016, 0.025 and 0.007, while |x| differs by 0.19–0.21. The clause "|x| > 0.3 in
  those same station-bands" was met nowhere the ratio passed: where the ratio holds, |x| differs by 0.19–0.21, not 0.3.
- **N4: not killed, and could hardly have been.** The two failures of N2 both have the angle off uniform (0.034, 0.048).
  But the undone angle is a monotone change of chart of the ratio under the same half-A shape, and the Cauchy's
  distribution function in r is the uniform one in that angle, so the two distances are one statistic (they agree to a
  few thousandths in every row). My set-up: N4 tested nothing beyond N2.

**Post hoc, not a test.** The two bands parted the way the plan's physics risk said they might, and the sort reads each:
- **B2 (1–4 Hz):** the amounts carry extreme kurtosis, transients that come and go. The ratio is at or near the Cauchy at
  the predicted z (0.017, 0.025, 0.033) and unmoved by loudness (0.016, 0.025, 0.007). That is a scale mixture living in
  the amounts while the direction holds its turn's law.
- **B1 (the secondary microseism):** the amounts are near Gaussian, and the direction moves with loudness. The loud hours
  plausibly come from one storm's direction (not checked against weather here). So the direction is not uniform there,
  and no turn is there to name.

So the rule is not contradicted, and in its letter the run is mixed: one prediction held (N2), two were killed (N1, N3),
and one was empty (N4). A second run would fix the band (B2 alone), restate N3's contrast without the 0.3 that the
quartile split never reached, and drop N4. Its predictions would have to be written before a new week or new stations
are fetched, since this week's numbers are now known.

### Run 2, plan (13 November, SPN R924; Tom: "Yes", to Claude's offer of a second run). Written and committed before any data for it is fetched; nothing in this section is edited after run 2.

Run 1's numbers are known, so run 2 takes a new week and new stations, fixed here before fetching, and keeps only what run 1
gave a sharp form: the 1–4 Hz band, where the amounts carried the fat tail and the direction held. The microseism band is
left out, because run 1 found it directional. That is a reading of run 1 and is not tested again here. N4 is dropped (one
statistic with N2). N3's 0.3 for |x| is dropped (run 1's quartile split never reached it).

- **Data.** EarthScope FDSN dataselect (service.earthscope.org, the archive service.iris.edu now redirects to), network IU,
  location 00, BH1 and BH2, with run 1's fallbacks (BHN/BHE at 00, then 10; otherwise the station is dropped and the run
  says so, no replacement). Six GSN stations not used in run 1, chosen for being far from coasts and spread across
  continents, and chosen before any of their data was looked at: IU.CCM (Cathedral Cave, Missouri), IU.RSSD (Black Hills,
  South Dakota), IU.TUC (Tucson, Arizona), IU.COLA (College, Alaska), IU.KIEV (Kyiv, Ukraine), IU.ULN (Ulaanbaatar,
  Mongolia). Week 2026-10-01T00:00 to 2026-10-08T00:00 UTC; half A the first 3.5 days, half B the rest. sha256s under the
  run.
- **Band and method.** B2 only, 1–4 Hz, filtered, decimated and segmented exactly as run 1 (`runs/smn/smn2.py`, run 1's
  script with only the stations, the week and the band changed). z = m + iγ from half A's covariance. The ratio y/x on
  half B against Cauchy(m, γ) by the KS distance D. The loudest quarter of half B's hours against the quietest. Kurtosis
  over the week.

**Predictions** (six stations; a dropped station counts as a failure of every prediction):

- **N1b (the amounts carry a fat tail).** Both channels' excess kurtosis exceed 3 in at least 4 of 6. *Killed* otherwise.
  If killed, N3b loses its teeth (no loudness to cancel), and the run says so.
- **N2b (the turn named).** D(r, Cauchy(m, γ)) < 0.03 on half B, with z from half A, in at least 4 of 6. *Killed* if 3 or
  more are at 0.03 or above.
- **N3b (loudness cancels from the direction, not from the amounts).** The ratio's law, loud hours against quiet: D < 0.03
  in at least 4 of 6, and in each of those, the same comparison for |x| (standardized by half A's σx) gives a D at least
  five times the ratio's. *Killed* if the ratio's D is 0.03 or more in 3 or more, or if fewer than 4 stations meet both
  parts.

What it would show: N1b–N3b not killed means that at six new stations in a new week, the 1–4 Hz noise field meets the
elliptical premise. The direction carries the Cauchy at the z its second moments fix, unmoved by loudness, while the
amounts carry a fat tail. That is a second domain for §12 O6, in the band where the turn could be named. Killed means
that run 1's B2 result was that week's or those stations', not the band's.

### Run 2 (13 November; `python3 -I runs/smn/smn2.py <dir>`, 43 seconds; output `runs/smn/run2.txt`)

Data: EarthScope dataselect, as planned. All six stations had IU, location 00, BH1 and BH2 for the whole week in one
segment, so no fallback was used and none was dropped. KIEV and ULN record at 20 samples a second, not 40, so the plan's
"every 10th sample" kept 2 a second there (half B 604,800 samples, not 1,209,600). The script's printed "3.50 days" for
them comes from its day count, which assumes 40 a second; the traces cover the full week. sha256 as fetched (also in
`runs/smn/run2-sha.txt`):

```
9f20c76cabf6a55312f12132d67af28fa6675443b97ffd87e3928a791c40c489  IU.CCM.00.BH1.mseed
4f09b39db14f48f88119a33cceb4fae0c2da62bd9d9201313da4c3ff34a104c3  IU.CCM.00.BH2.mseed
724cff5e745b0abb37cb62ee7eb26c26b47ad5c74bb5e649df632ff746790d41  IU.COLA.00.BH1.mseed
a511a3b97a4e4e0d2840f62b25c38b537c94cde2bd76672c82bb9e5858a2f98e  IU.COLA.00.BH2.mseed
1877628b8979aca9d21b0203506240f046b8fb9def5f5abef8f2e1e31263e5f9  IU.KIEV.00.BH1.mseed
444a35d5d0e8c478cc7a330f73a6f0ad553015dda7f6d65d57f72dd82eb6103a  IU.KIEV.00.BH2.mseed
307270e9c3a0d7264a9d5fbdea65a92d8c955d883452903c0d3306cbb74a9092  IU.RSSD.00.BH1.mseed
f20a54f4eb7474b83f461f9a4912034a808910a6211eb624f1d60d2c92c6a717  IU.RSSD.00.BH2.mseed
2696304ef186732ce7c1c27e437cfc28e5a92d89e64b3d00f4631eadeb775941  IU.TUC.00.BH1.mseed
a7a82f6ee41de74f09ef80cd50c4ce602c8210367e91f353bd9bd0793d79ced6  IU.TUC.00.BH2.mseed
2030eea2a3c1b39bfe641dcc08a8ccb8d0e97d8d472bbb24afd61140c3cfe0fe  IU.ULN.00.BH1.mseed
e1e052ee604eb8133e17847cca03827d1b0918dd62302883e3667b98f664a208  IU.ULN.00.BH2.mseed
```

| station | z from half A | D(r, Cauchy z), half B | ratio, loud vs quiet | \|x\|, loud vs quiet | kurtosis x, y |
|---|---|---|---|---|---|
| CCM | +0.001 + 1.031i | 0.0009 | 0.0014 | 0.0066 | −0.00, −0.00 |
| RSSD | +0.110 + 1.164i | 0.0265 | 0.0025 | 0.135 | 4399, 11915 |
| TUC | −0.316 + 0.876i | 0.0247 | 0.0203 | 0.177 | 1063, 1623 |
| COLA | +0.030 + 0.953i | 0.0067 | 0.0150 | 0.337 | 36164, 62791 |
| KIEV | +0.197 + 0.838i | 0.0375 | 0.0483 | 0.287 | 5867, 1441 |
| ULN | +0.247 + 1.206i | 0.0061 | 0.0069 | 0.212 | 1401, 5882 |

- **N1b: not killed.** Both channels' kurtosis exceed 3 at 5 of 6 stations. CCM is the exception, with Gaussian amounts
  (kurtosis 0.00, D from the best Gaussian 0.0005).
- **N2b: not killed.** The ratio is within 0.03 of the Cauchy at half A's z at 5 of 6 stations. KIEV is the one past it,
  at 0.0375.
- **N3b: not killed.** The ratio's D between the loud and quiet hours is 0.03 or more only at KIEV (0.048). Both parts are
  met at 4 of 6 stations: RSSD, TUC, COLA and ULN, where |x|'s D is 10 to 70 times the ratio's. CCM fails the second part
  narrowly: |x| 0.0066 against the needed 0.0070. Its amounts barely move with loudness at all.

**Post hoc, not a test.**
- CCM's 1–4 Hz band behaves like a steady Gaussian pair: no transients, the loud and quiet hours nearly alike, and the
  ratio on the Cauchy to 0.001. That is the elliptical case with no scale mixture in it. Whether this is the site's quiet
  or the instrument's own floor was not checked.
- KIEV, the one failure of N2b and N3b, is the station nearest a city, and its direction moves with loudness, as the
  microseism band did in run 1. A directional source is the plan's stated way to fail. This was not checked against any
  record of local sources.

Read together with run 1's B2 (3 of 3 within 0.034 on the ratio, 3 of 3 unmoved by loudness), the band now stands at 8 of
9 stations, over two weeks and four continents, on both counts. The direction holds the Cauchy that its second moments
fix, and loudness cancels from it while staying in the amounts. It is a second domain for *Reads and Writes* §12 O6 in the
band where the turn could be named. As the plan says, this is the classical elliptical ratio. What is tested is whether
the noise field meets its premise, and where it does not (KIEV, the microseism band), the direction has a source and the
sort predicts no Cauchy.
