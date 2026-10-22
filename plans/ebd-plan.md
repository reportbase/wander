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
