# RDD: the radio dipole, sorted by the second test

*9 November 2026. Tom: "proceed per your recommendations", after "what did you learn, any new ideas?", where the first
recommendation was to put the second test (change what arrives) to a second, independent census. EBD (`plans/ebd-plan.md`,
run 1) found on the CatWISE quasars that four flux slices give one β, 2.7 times the microwave background's, while three
colour slices do not (the reddest third's dipole 60° off). A boost read through a payload weighting must give one β in
every slice of any census, at any wavelength. This plan asks the same of the radio sky, with the spectral index as the
colour. Written before any data were downloaded: only the column list and three rows of the catalogue were looked at
(below). Nothing above "Runs" is edited after a run.*

## Known beforehand

- **EBD run 1** (this repo): the Ellis–Baldwin split is exact (D² on the directions, D^(x(1+α)) the payload's weighting
  at a flux limit; a colour cut moves nothing for a boost). CatWISE: one β from four W1 slices,
  (3.31 ± 0.27)·10⁻³ by the Poisson bootstrap (the jackknife gave errors 1.7 times larger), axis (234.7°, 42.2°) by my
  estimator; Secrest's recipe 0.01558 at (238.5°, 28.6°), β̂ 2.61·10⁻³. Colour terciles disagree, p = 2.6·10⁻⁴.
- **Radio dipoles in print** (from memory; to check, not used in any verdict): NVSS's count dipole has been measured
  several times at two to five times the kinematic expectation (Blake and Wall 2002, consistent then; Singal 2011;
  Rubart and Schwarz 2013; Tiwari and Nusser 2016; Secrest et al. 2022 joining NVSS with CatWISE; Wagenveld, Klöckner and
  Schwarz 2023). TGSS's dipole is much larger again, around ten times (Bengaly, Maartens and Santos 2018; Singal 2019),
  and Siewert, Schmidt-Rhaesa and Schwarz 2021 found the radio dipole's amplitude growing toward low frequency. TGSS ADR1
  is known to carry direction-dependent flux-scale errors. Since the spectral index here is TGSS against NVSS, a
  TGSS flux error that depends on direction becomes an α that depends on direction: the colour slices below could fail
  for that reason, which the run cannot tell from a dipole in the sources themselves.
- **The catalogue** (de Gasperin, Intema and Frail 2018, MNRAS 474, 5008; VizieR J/MNRAS/474/5008/spidxcat, reached
  through the CfA mirror, since vizier.cds.unistra.fr and cdsarc do not answer from this environment): 1,396,515 sources,
  NVSS matched to TGSS ADR1 over the sky both cover (dec > −40°). Columns looked at: RAJ2000, DEJ2000, FtotNVSS and
  FtotTGSS (in Jy, **two decimals**, so a 10 mJy grid), SpIndex (S ∝ ν^SpIndex: three rows gave −0.61, −0.01, 0.02),
  Scode (S single, M multiple, C complex, I island, L a TGSS non-detection with an upper limit on the index, U an NVSS
  non-detection). Sources undetected by TGSS are kept, with their limits; sources undetected by NVSS (U) have
  FtotNVSS = 0 and fall below any cut here.

## Method (fixed before the data)

- **Download** RAJ2000, DEJ2000, FtotNVSS, SpIndex, Scode for all rows to /tmp/rdd_data (sha256 recorded under Runs;
  nothing committed).
- **α** = −SpIndex (S ∝ ν^(−α), EBD's convention), every source as given, limits included.
- **Sample**: FtotNVSS ≥ 0.02 Jy (as stored), Scode not U.
- **Mask** (HEALPix nside 64, pixel centres): keep a pixel if its centre and its antipode's both have |b| > 16° and
  dec > −39° (so |dec| < 39°: a mask symmetric under the antipode, which a dipole fit needs, and 1° inside the cuts
  applied to the sources, |b| > 15°, |dec| < 40°, so no kept pixel is part-cut).
- **Estimator**: healpy's `fit_dipole` on the counts of kept pixels; amplitude = dipole/monopole, axis its direction
  (Secrest's recipe, which reproduced their CatWISE result in EBD's post hoc).
- **Errors**: 400 Poisson resamplings of the pixel counts about the fitted model, and a jackknife over the nside-2
  regions that hold kept pixels; every verdict uses the larger of the two (EBD found the bootstrap 1.7 times too small).
  Angular radii from the same draws (the 99% radius of the jackknife-inflated draws: the bootstrap's axis scatter scaled
  by the ratio of the two amplitude errors).
- **x** at a flux S: the least-squares slope of −ln N(≥s) against ln s over the 0.01 Jy grid values s in
  [S/1.5, 1.5·S]. A slice [S₁, S₂) has x_eff = (x₁N₁ − x₂N₂)/(N₁ − N₂), N_i = N(≥S_i); an open top slice x_eff = x₁.
  α per slice its mean. Expectation [2 + x_eff(1 + α)]·β; β̂ = D_meas/[2 + x_eff(1 + α)].
- **Flux slices**: [0.02, 0.04), [0.04, 0.08), [0.08, 0.16), [0.16, ∞) Jy. **Colour slices**: terciles of α among
  sources ≥ 0.02 Jy, each with its own x (from its own counts) and mean α.

## Predictions

- **R1 (one β from every flux slice).** The four β̂ agree: χ² about their weighted mean, p > 0.01. *Killed* if
  p ≤ 0.01. As in EBD P6, the form a boost must take whatever its size.
- **R2 (one β from every colour slice).** The three α terciles' β̂ agree at p > 0.01. *Killed* if not. (A boost cannot
  separate them, EBD P2. Known beforehand: CatWISE's colours did separate, and TGSS's flux errors could make this fail
  here for a reason that is not the sources'.)
- **R3 (one motion, two wavelengths).** The radio β̂ from the four flux slices together (their weighted mean) agrees with
  CatWISE's flux-slice β̂, (3.31 ± 0.46)·10⁻³ (EBD's error times the 1.7 its jackknife found): |difference| under 2.58
  combined standard errors. *Killed* if not. A reader has one velocity; every census it takes, at any wavelength, must
  read the same β once each census's payload weighting is divided out.
- **R4 (one axis).** The radio dipole of the whole sample (≥ 0.02 Jy) points within the combined 99% radius of
  CatWISE's axis (234.7°, 42.2°), the radii added in quadrature (CatWISE's 99% bootstrap radius was 18.4°; times 1.7,
  31°). *Killed* if not.
- **R5 (not predicted).** β̂/β_CMB, and the axis's distance from the microwave background's (264.02°, 48.25°), are
  reported and not scored. The sort says what a boost must look like, not how fast we move.

## Data

(Filled when downloaded.)

## Runs

(Nothing above this line is edited after a run.)
