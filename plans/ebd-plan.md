# EBD: the Ellis–Baldwin dipole, as addresses and payload

*22 October 2026. A test asked for after SRR (`plans/srr-plan.md`), ISR (`plans/isr-plan.md`) and OFS §7.8 "Special
relativity's sky". SRR showed exactly that a uniform sky seen by a moving reader is shifted on the pseudorapidity by the
rapidity η: the boost is a reading, taken from directions alone, while a Doppler factor read as a frequency is a
writing (it needs a rest frequency). ISR sorted counts by flux as a reading (no distance in them). The Ellis–Baldwin
dipole joins the two: a count of sources (directions) above a flux limit (payload). This plan reads it through the
split, checks the exact part in mpmath at 50 digits, and measures it on the CatWISE2020 quasars of Secrest et al. 2021.
Written before any data were downloaded; nothing above "Runs" is edited after a run.*

## Known beforehand

- **Ellis and Baldwin 1984** (MNRAS 206, 377). A reader moving at β through sources isotropic in their own frame, with
  integral counts N(>S) ∝ S^(−x) at the flux limit and spectra S ∝ ν^(−α), counts a dipole N(θ) ∝ 1 + D·cos θ with
  D = [2 + x(1 + α)]·β, to first order in β. The 2 is aberration (solid angles squeezed forward, D² to first order); the
  x(1 + α) is the Doppler boost of every flux (by D^(1+α)) carrying sources across the limit.
- **The CMB dipole** (Planck 2018 I, check): β = 1.2336·10⁻³ (369.8 km/s), toward (l, b) = (264.02°, 48.25°).
- **Secrest et al. 2021** (ApJL 908, L51; arXiv 2009.14826): 1,355,352 CatWISE2020 AGN chosen by W1 − W2 ≥ 0.8,
  9 < W1 < 16.4, |b| > 30° and further masks (bright stars, nearby galaxies, planetary nebulae and the like, a mask
  file); a linear trend in ecliptic latitude (the WISE scan depth) removed. They found D = 0.01554 toward
  (l, b) = (238.2°, 28.8°), 27.8° from the CMB's; from x = 1.7 and mean α = 1.26 the expectation 0.0072; the excess at
  4.9σ (p ≈ 5·10⁻⁷) by simulated skies. These numbers are known to me now and stated as such (from memory; check against
  the paper).
- **Follow-ups I know of** (from memory, each to check): Secrest et al. 2022 (ApJL 937, L31) joined NVSS with
  CatWISE, about 5.7σ. Dam, Lewis and Brewer 2023 (MNRAS) a Bayesian estimator on CatWISE, about the same excess.
  Wagenveld, Klöckner and Schwarz 2023 (A&A 675, A72) Bayesian estimators on NVSS and WISE. Darling 2022 (ApJL 931, L14)
  VLASS + RACS, consistent with the CMB. Dalang and Bonvin 2022 (MNRAS 512, 3895): x and α that change with redshift
  change the expectation. Guandalin et al. 2023 (ApJ 953, 144): CatWISE's systematics. Mittal, Oayda and Lewis 2024
  (MNRAS) on Quaia, consistent with the CMB. Secrest et al. 2025, a review in Reviews of Modern Physics, "the cosmic dipole
  anomaly". The excess is contested: systematics of the WISE scan, the masks, the evolution of the population, and the
  estimator are all argued.
- **SRA, SRR** (in this repo): a uniform sky seen from a boost has density D²/4π (the spherical Cauchy, ρ = tanh(η/2));
  aberration is z ↦ z/k on the stereographic chart, with no frequency in it; D = √(1 − β²)/(1 − β cos θ′) a payload
  weighting on the addresses (SRR P3).

## The reading to test

The count is a census of directions. What is put into the census is set by the payload (the flux limit). So:
- **The direction is a reading.** The dipole's axis is a direction on the reader's sphere. Nothing in the payload can
  turn it (for an isotropic source population): the payload weighting D^(1+α) is a function of the same angle.
- **The "2" is the addresses'.** With no flux limit at all (every source counted), the seen density is D² per seen solid
  angle exactly (SRA): directions alone, no frequency, no flux, no kind. To first order that is 2β·cos θ.
- **The x(1 + α) is the payload's, and it is a reading of the payload, not a writing.** It needs x (the slope of the
  counts against flux, a ratio of counts at two fluxes) and α (a ratio of two bands' fluxes). Both are ratios measured in
  the same catalogue. No rest frequency, no distance, no clock enters. So β read from a count dipole is a reading in units
  of c, though SRR's frequency reading of D is a writing.
- **A colour cut adds nothing.** For a power-law spectrum the boost multiplies every band by the same D^(1+α) (ν → Dν,
  S_ν → D^(1+α) S_ν). A colour, a ratio of two bands, is unchanged. Only the flux limit brings the payload in.
- **No catalogue has no flux limit.** A detection is a flux above a threshold, so the 2 cannot be isolated in data. The
  direct test available is the other way round: slice the catalogue by flux. Every slice must give the same β once its
  own payload weighting is divided out; the 2 is the same in every slice, the x(1 + α) is each slice's own.
- **The excess is not predicted.** The framing sorts the parts; it says nothing about the size of the measured dipole
  beyond what Ellis–Baldwin already say. If the measured amplitude is twice the expectation, the framing does not explain
  it, and I fit nothing to it.

## Method (fixed before the data)

- **Data.** Secrest et al. 2021's own sample from Zenodo (record 8303800, "A Test of the Cosmological Principle with
  Quasars", CC BY 4.0): `catwise_agns_masked_final_w1lt16p5_alpha.fits` (W1 < 16.5, their masks applied, per-source α),
  and `MASKS_exclude_master_final.fits` if needed. Stored in /tmp/ebd_data only; sha256 recorded below; nothing
  committed. If it is not reachable, NVSS from VizieR, and I say so.
- **Cut.** 9 < W1 < 16.4 (their final cut), W1 − W2 ≥ 0.8 (already in the file), |b| > 30°, plus their masks as found in
  the file or mask file. If their masks cannot be applied, |b| > 30° alone, stated.
- **Estimator.** A linear least-squares fit of N_p = A·(1 + d·n̂_p) to the counts in equal-area HEALPix pixels (nside 64)
  whose centres are unmasked, with and without a linear term in |ecliptic latitude| (Secrest's correction). The fit is
  linear in (A, A·d). Error: 400 Poisson resamplings of the pixel counts about the fitted model (a parametric bootstrap),
  and a 12-region jackknife (by HEALPix base pixel) as a check.
- **x.** −d ln N(>S)/d ln S at the cut, from the counts in W1 within ±0.1 mag of the cut: x = d log₁₀ N(<W1)/(0.4·dW1),
  with S ∝ 10^(−0.4 W1).
- **α.** The file's per-source α if present (Secrest's); otherwise from W1 − W2 with Vega zero points 309.540 Jy and
  171.787 Jy at 3.3526 and 4.6028 μm. The expectation uses the mean α of the sample (as Secrest), and I also give
  the mean of x(1 + α) per source.
- **Slices.** Disjoint W1 bins 9–15.0, 15.0–15.5, 15.5–16.0, 16.0–16.4 (fixed now). A bin [S₂, S₁] has, to first order,
  the exponent 2 + (1 + α)·(x₁N₁ − x₂N₂)/(N₁ − N₂), N_i = N(>S_i) and x_i the local slopes at each edge (N₁ at the faint
  edge). Colour slices: three α terciles at 9 < W1 < 16.4.

## Predictions

Notation: θ from the motion (seen frame primed), c = cos θ in the sources' frame, β the speed in units of c,
D(θ′) = √(1 − β²)/(1 − β cos θ′) the Doppler factor, "dipole" the linear estimator's amplitude 3⟨cos θ′⟩ for a full sky.

- **P1 (the 2 is the addresses', exact).** Sources uniform in their own frame, counted with no flux limit by a reader at
  β: the seen density is D(θ′)²/4π; 3⟨cos θ′⟩ = 3/β − (3(1 − β²)/(2β²))·ln((1 + β)/(1 − β)) = 2β + (2/5)β³ + O(β⁵);
  the integrand holds angles only. *Killed* if quadrature of the density, or the expectation of
  cos θ′ = (c + β)/(1 + βc) over uniform c, misses the closed form by more than 10⁻⁴⁰ at β = 10⁻³, 1.2336·10⁻³, 0.1, 0.6,
  0.99, or the series misses by more than 10⁻⁴⁰ at the two smallest β (with the β⁵ term computed).
  *Corrected before any run (22 Oct), by my reading of my own clause:* the series clause as written could not pass,
  since the β⁷ term at β = 10⁻³ is about 10⁻²². It now reads: the closed form equals Σ 6β^(2m+1)/((2m+1)(2m+3)), whose
  first three terms are 2β, (2/5)β³, (6/35)β⁵, to 10⁻⁴⁰ when summed to 40 terms at the two smallest β. The clause as
  first written is recorded as killed by my set-up whatever the run gives.
- **P2 (the flux limit is the payload's, exact).** Sources with N(>S) = K·S^(−x) and S_ν ∝ ν^(−α), seen above a fixed
  S_cut: the seen density per seen solid angle is D^(2 + x(1+α)) times the rest one, exactly, at every S_cut; the
  first-order dipole is [2 + x(1 + α)]·β; the 2 does not depend on S_cut, x or α. A colour cut on these sources leaves the
  density unchanged. For a curved count (log N quadratic in log S) the exponent at first order is 2 + x(S_cut)(1 + α), x
  the local slope. *Killed* if the exact density misses D^(2+x(1+α)) by more than 10⁻⁴⁰ (x ∈ {1, 1.5, 1.7, 2.5},
  α ∈ {0, 0.75, 1.26}, β ∈ {1.2336·10⁻³, 0.1}), the colour cut moves the density by more than 10⁻⁴⁰, or the curved
  count's dipole misses the first-order exponent by more than 10β² relative.
  *Set-up named before any run (22 Oct):* the curved count is ln N(>S) = ln K − x₀u − κu²/2, u = ln(S/S_cut), with
  x₀ = 1.7, κ = 0.5, α = 1.26, at β = 1.2336·10⁻³ and 0.1; "relative" is |3⟨cos θ′⟩ − (2 + x₀(1 + α))β| over
  (2 + x₀(1 + α))β. The pure power law's dipole is checked against its exponent by the same measure.
- **P3 (the direction is a reading and is the CMB's).** The measured dipole's axis lies within the bootstrap's 99%
  angular radius of (264.02°, 48.25°). *Killed* if not. (Known beforehand: Secrest's axis is 27.8° off; I do not know
  their angular error.)
- **P4 (my set-up reproduces theirs; a check, not a test of the framing).** With the cut and masks above and the ecliptic
  term, the amplitude within 15% of 0.01554 and the axis within 10° of (238.2°, 28.8°); x at W1 = 16.4 within 0.1 of
  1.7; mean α within 0.05 of 1.26; the expectation within 5% of 0.0072. *Killed* (my set-up, if so) if any misses.
- **P5 (the payload part is a reading of the catalogue's own payload).** The expectation's payload part x(1 + α)·β is
  computed from the catalogue alone (counts against W1, and W1/W2); multiplying every flux and the cut by one factor
  changes neither x nor α nor the sample, so neither the expectation nor the measurement. *Killed* if the recomputed x
  and mean α after multiplying every flux and the cut by 10^(0.4·0.37) (a 0.37 mag zero-point shift, arbitrary) differ
  from the originals beyond rounding (10⁻¹²). (An identity on the data; it states that no zero point, rest frequency or
  distance enters.)
- **P6 (one β from every flux slice).** β̂ = D_meas/[2 + x_eff(1 + α)] in the four disjoint W1 bins agree: χ² of the
  four about their weighted mean has p > 0.01. The 2·β part of each expectation is the same in every bin; the payload part
  moves with each bin's x_eff and α. *Killed* if p ≤ 0.01. (This is what a boost, read through a payload weighting, must
  give whatever its size; the framing does not say what β̂ is.)
- **P7 (one β from every colour slice).** The same for three α terciles: β̂ agree at p > 0.01. *Killed* if not.
- **P8 (the size is not predicted).** No prediction on whether β̂ equals the CMB's β. I report β̂/β_CMB, and do not
  read any value as support for the framing.

## Data

Downloaded 22 October, before the run; only the column list and three rows were looked at before the script was written.
- Secrest, von Hausegger, Rameez, Mohayaee, Sarkar and Colin, "A Test of the Cosmological Principle with Quasars",
  Zenodo record 8303800 (doi:10.5281/zenodo.8303800), CC BY 4.0.
  - `catwise_agns_masked_final_w1lt16p5_alpha.fits`, https://zenodo.org/api/records/8303800/files/catwise_agns_masked_final_w1lt16p5_alpha.fits/content,
    389,880,000 bytes, 1,604,392 rows, sha256 1fc8bcfc19da3602037dc7bdaa1a044a1d0c13cc76816b21c9e97e68f014605d
    (md5 f77df7051007c459bc8f47f418af17a4, as Zenodo lists). Columns used: l, b, elat, w1, w2, alpha_W1. alpha_W1 is
    negative (−1.017 in the first row): their convention is S ∝ ν^(alpha_W1), so α = −alpha_W1 here.
  - `MASKS_exclude_master_final.fits` (same record), 23,040 bytes, sha256
    fcacb23a6805c2c0cc2fdd64c55d546fb56343555580c100f99fca80ebab6131: 292 circles (ra, dec, radius in degrees; ba, pa).
  - `Resultscode.tar.gz` (same record), sha256 81f0f9e6b83c080a2395564d868d5c59d5d303fa04e962153c4c173e6f549c73, read for
    how they masked (their `maskVectors` masks each circle and, "symmetric", its antipode). Not run.
- Stored in /tmp/ebd_data only; nothing committed.
- Fixed now, from the column list: the pixel mask is |b| > 30° plus every circle of the mask file and its antipode (their
  "symmetric"), at pixel centres; the one-sided mask (circles only) is reported beside it.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (22 Oct; `runs/ebd/ebd.py`, output `runs/ebd/ebd-run1.txt`, 35 s)

One attempt. Part A at 50 digits; part B on the 1,604,392 rows of the file (|b| ≥ 30° already, W1 − W2 ≥ 0.8, W1 to
16.5; 288 sources lie inside a mask circle, so the file is masked at the source level but not quite fully).

- **P1 not killed.** Worst quadrature miss 8.9·10⁻⁴⁶. With no flux limit the seen sky is D²/4π and its dipole
  3⟨cos θ′⟩ = 2β + (2/5)β³ + (6/35)β⁵ + …: 0.0024672008 at the CMB's β (2β = 0.0024672). Only angles enter. The 40-term
  series agrees to 8.9·10⁻⁴⁶. The series clause as first written (three terms to 10⁻⁴⁰) is killed by my set-up, as noted
  before the run (the three terms miss by 4·10⁻²² there).
- **P2 not killed.** Built from the aberration Jacobian (a numerical derivative) and I_ν/ν³ invariance, the seen count
  above a fixed limit is D^(2 + x(1+α)) to 9·10⁻⁵¹ at every x, α, β tried; a colour moves by 4·10⁻⁵¹ (not at all). The
  dipole against first order [2 + x(1 + α)]β: pure power law 1.30 β² relative, the curved count 1.55 β² (limit 10 β²);
  at the CMB's β, 0.0072067 first order, 0.0072067 exact.
- **P3 killed.** My estimator's axis is (234.7°, 42.2°), 21.4° from the CMB's; the Poisson bootstrap's 99% radius is
  18.4° (68%: 8.0°). The other three mask and ecliptic choices give 18.4°–21.8° off against 14.1°–15.8°.
- **P4 killed, by my set-up.** My estimator gave D = 0.01894 ± 0.00168 at (234.7°, 42.2°), 22% above Secrest's 0.01554
  and 13.7° from their axis. x = 1.757 at W1 = 16.4 (N(<16.3) = 1,122,298, N(<16.5) = 1,551,074), mean α 1.261 (their
  column; from W1 − W2 with Vega zero points 1.232, median difference per source 0.002), expectation 0.00737: these three
  pass. Post hoc (`runs/ebd/ebd1-posthoc.py`, output `ebd1-posthoc.txt`): Secrest's own recipe, read from their notebook
  (an nside-1024 mask degraded to nside 64 keeping only pixels wholly unmasked; the ecliptic trend fitted first and
  subtracted; healpy's fit_dipole), gives D = 0.01558 ± 0.00172 at (238.5°, 28.6°), 0.3° from theirs. The miss is my
  estimator's: pixels kept by their centres include part-masked pixels at |b| = 30° and at the circles (the catalogue is
  cut at the source level), and my ecliptic term was fitted jointly with the dipole.
- **P5 not killed.** With W1, W2 and the cut all moved by −0.37 mag, x moved by 0, the sample by 0 sources, the colour's
  α by 0. No zero point, rest frequency or distance enters the expectation.
- **P6 not killed.** p = 0.34 (χ² 3.34 on 3 dof). By W1 bin:

  | W1 | N | x_eff | α | 2 + x_eff(1 + α) | D measured | β̂ / β_CMB |
  |---|---|---|---|---|---|---|
  | 9.0–15.0 | 177,792 | 1.635 | 1.316 | 5.786 | 0.0183 ± 0.0033 | 2.56 |
  | 15.0–15.5 | 189,415 | 1.407 | 1.331 | 5.281 | 0.0231 ± 0.0040 | 3.54 |
  | 15.5–16.0 | 362,768 | 1.475 | 1.310 | 5.407 | 0.0199 ± 0.0032 | 2.98 |
  | 16.0–16.4 | 582,365 | 2.083 | 1.191 | 6.562 | 0.0192 ± 0.0026 | 2.37 |

  The 2 is the same in every bin (0.00247 of the expectation); the payload's part runs from 3.28 to 4.56 times β, about
  60–70% of the whole. One β fits all four: 3.31·10⁻³ ± 0.27·10⁻³, 2.68 times the CMB's. The axes wander (17°, 6°, 22°,
  36° from the CMB).
- **P7 killed.** p = 2.6·10⁻⁴ (χ² 16.5 on 2 dof). Terciles of α at 9 < W1 < 16.4: mean α 0.66, 1.17, 1.96; x 2.39, 1.63,
  1.24; D 0.0172, 0.0190, 0.0320; β̂ 2.34, 2.78, 4.57 times the CMB's. The reddest third's dipole points to (195°, 27°),
  60° from the CMB; the other two to (282°, 34°) and (270°, 47°). Post hoc, with Secrest's recipe the same (0.0142,
  0.0155, 0.0295; the reddest at (199°, 18°)), and the reddest third's dipole is there in every W1 slice (0.021, 0.032,
  0.035 at 9–15.5, 15.5–16.0, 16.0–16.4). Once its own payload weighting is divided out, a boost gives one β in every
  slice, and a colour cut cannot change that (P2). So the reddest third's dipole is not our motion's. It is either
  anisotropy of the sources in their own frame or a colour-dependent selection on the sky (the WISE scan, W2's depth,
  confusion). This run cannot tell which. I did not look for it before the run.
- **P8 (reported, not scored).** β̂ = 3.17·10⁻³ ± 0.28·10⁻³ from my estimator, 2.57 times the CMB's; with Secrest's
  recipe 0.01558/5.971 = 2.61·10⁻³, 2.12 times. The framing says nothing about this.

What the run says, read plainly:
- The split is exact (P1, P2, P5): with no flux limit a moving reader's census is D² on the addresses, angles only, 2β to
  first order. A flux limit multiplies it by D^(x(1+α)); x and α are ratios read from the same catalogue's payload. So
  β from a count dipole is a reading in units of c, with no rest frequency, but it is not "from directions alone": two
  thirds of the expected amplitude is the payload's.
- No catalogue has no flux limit, so the 2 cannot be measured alone. The flux slices agree on one β (P6), as a boost
  needs, at 2.7 times the CMB's. The colour slices do not (P7): part of the measured dipole is not a boost at all.
- Errors: the jackknife (12 base pixels) gives 0.0029 on the amplitude against the Poisson bootstrap's 0.0017, so the
  Poisson bootstrap understates, by about 1.7. P3's and P7's verdicts used the bootstrap, as fixed; they stand. Scaled by
  1.7, P3's 99% radius would be about 31° and would not kill (post hoc, not a verdict).

Earlier wording this bears on (not edited here): `papers/observation-from-somewhere.md` line 2136 ("A reader holding
directions alone reads its own rapidity"), `papers/physics.md` lines 177 and 235, and `plans/srr-plan.md` lines 33 and
146 say the boost is read from directions alone. That holds for a census whose membership does not depend on the payload,
and for sources isotropic in their own frame. A real census is flux-limited (the payload's weighting is then 60–70% of the
amplitude, read from x and α) and, here, not isotropic by colour.
