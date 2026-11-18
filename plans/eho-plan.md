# EHO: the observer's geometry, the spacetime and the emission, sorted on the EHT's own data

18 Nov 2026. SPN R1090. Tom: "maybe we could do that for them with their own data?", then "yes", to Claude's three-part
plan. From discussion note item 21: black hole physicists separate the spacetime from the emission plainly and the
observer's geometry only as machinery (tetrads, Penrose–Terrell, Chang and Zhu 2021); no paper found sorts measured
numbers by layer. This test does that sorting on the Event Horizon Telescope's published numbers and public data. It
claims no new physics and nothing about what other work lacks (R335, R364): the value is the sorting.

## The three layers and the three tests

- **Observer's geometry (O):** what any standpoint has: the sky of directions, its local flatness, the effect of the
  observer's own motion (a conformal map of the sky, Penrose 1959). No mass, no G.
- **Spacetime (S):** the hole's metric, fixed by mass and spin; its sizes amounts in GM/c².
- **Emission (E):** the plasma's light: where it glows, how bright, its pattern.

Tests: (1) scale the world: read or write; (2) change what arrives (another day, another year, another band): address
or payload, here spacetime against emission; (3) change the route with the same source (subrings, light echoes): not
available at EHT resolution, so not run. A quantity is placed in the layer whose change moves it; one moved by two
layers is **mixed**.

## Known beforehand

EHT 2019 Paper VI (arXiv:1906.11243): ring 42 ± 3 μas, θ_g 3.8 ± 0.4 μas, mass 6.5 × 10⁹ M☉ with D = 16.8 Mpc, the
ring turned into θ_g by GRMHD calibration. EHT 2024 (A&A 681, A79): 2018 ring 43.3 (+1.5/−3.1) μas, the bright side
about 30° from 2017. EHT Paper IV (2019): the 2017 days' images alike in diameter, the bright side in the south.
The first null of the visibility amplitudes near 3.4 Gλ (Paper IV/VI, from memory; to check). Gralla, Holz and Wald
2019, Narayan, Johnson and Gammie 2019, Chang and Zhu 2021 (item 21). So part 2 restates a known result; what it can
fail is the sorting.

## Part 1: sort the reported quantities (a reading, with a kill)

Prediction, written now, for the quantities of EHT 2019 Papers IV and VI and EHT 2024:

| quantity | test that moves it | layer |
|---|---|---|
| ring angular diameter (μas) | none of (1); not (2) | S, mixed with E (the emission ring sits off the shadow; the α calibration) |
| θ_g = GM/(Dc²) | none of (1); not (2) | S (through the calibration, so its error carries E) |
| mass in M☉ | (1) | a write: S's θ_g times D carried in |
| distance D | (1) | a write, carried in |
| ring width, fractional | (2) | E |
| brightness position angle | (2) | E (with spin's sense from S; mixed) |
| total compact flux (Jy) | (2), and (1) through D² | E, and a write |
| orientation on the sky of the whole image | none by the hole | O (the observer's frame on the sky) and S's spin axis, mixed |
| shadow depth (contrast) | (2) | E |

**Q1 (kill):** some reported quantity is moved by none of the three changes yet is not the observer's geometry, or
needs a fourth layer to be placed. Recorded as a table in the run; the judgement mine, so marked not blind.

## Part 2: the change-what-arrives test, rerun

From the public 2017 calibrated visibilities (four days, April 5, 6, 10, 11; two bands) and the 2018 data if public:
fit, per day and band, (a) the radius of the first minimum of the visibility amplitude against baseline length
(a thin ring of diameter d has its first null at u₀ = 2.405/(π d)), and (b) the bright side's position angle from a
simple crescent fit to closure phases and amplitudes (my code, numpy and scipy; no EHT pipeline).

- **Q2:** the null u₀ is the same over the four 2017 days within 5% (days 1 apart and 6 apart alike); killed if the
  spread exceeds 5%.
- **Q3:** the diameter from u₀ agrees with 42 μas within 15% (the thin-ring formula ignores width; known to read
  somewhat larger or smaller); killed if off by more.
- **Q4:** where 2018 data are public, its u₀ within 5% of 2017's while its bright-side angle differs by more than 15°;
  killed if u₀ moves more than 5%, or if the angle moves under 15° (then the payload did not change enough to test).
  Untested if 2018 visibilities are not public.
- **Q5:** within 2017 the bright-side angle changes by less than 20° across the days (Paper IV's images alike); the
  test of (2) within a week is weak; recorded, not a kill.

## Part 3: the observer's own layer, exact

A boost of the observer acts on the sky as a Möbius map. For a source of small angular size α at angle χ from the
velocity, it scales α by the Doppler factor D(χ) = 1/(γ(1 − β cos χ)) and rotates it by **zero**: a boost keeps the
great circles through its axis, so the local conformal map's rotation part vanishes at every point. Checked at 60
digits (mpmath) on a ring of 360 points.

- **Q6:** the scale is D to 10⁻⁵⁰ and the rotation zero to 10⁻⁵⁰ (first order and all orders) for β = 10⁻⁴, 10⁻³,
  5·10⁻³ at χ = 0°, 30°, 90°, 150°; the shape a circle to O(α²) only (finite size), the departure at α = 42 μas below
  10⁻²⁰ of the diameter.
- **Q7:** for the observer's motions that matter (Earth's orbit, β ≈ 10⁻⁴; Earth's spin, 1.5·10⁻⁶; the Sun against the
  CMB, 1.2·10⁻³), the ring's diameter changes by at most |β|·42 μas ≤ 0.05 μas, under 2% of the 3 μas error. So at EHT
  precision the observer's own motion is negligible, and the observer layer enters only as D carried in and the sky
  orientation. Killed if any listed motion gives more than 0.3 μas. The relative velocity along the line of sight
  (cosmological recession) is already in the angular diameter distance and is not counted twice.
- Post hoc, not a prediction: whether Chang and Zhu's rotation for Sgr A* comes from the finite-distance curved
  spacetime (S) rather than the flat boost, as Q6 implies for the flat part; checked by reading their paper, not run.

## Data

EHT public data (GitHub, eventhorizontelescope/2019-D01-01 for the 2017 M87 uvfits; the 2018 release to look for), to be
fetched only after this plan is committed. Source, licence and sha256 to be recorded here; data not committed. If the
data cannot be reached, parts 1 and 3 run alone and part 2 is untested.

## Runs

**Data (fetched after the plan's commit).** 2017: github.com/eventhorizontelescope/2019-D01-01 (commit 27ae76a), the
HOPS network-calibrated Stokes I csv files, four days (MJD 57848–57854; days 095, 096, 100, 101) × two bands; licence
ODC-PDDL. 2018: github.com/eventhorizontelescope/2024-D01-01 (commit fda41da; also CyVerse doi:10.25739/epm5-r371), the
HOPS network-calibrated csv files, days 111, 112, 115 × bands b1–b4; ODC-PDDL. Not committed. sha256:

```
1e7c2a63e79b1722dcc5d7fe73d8193309adec20c4e660b0659169ee66c63541  SR1_M87_2017_095_hi_hops_netcal_StokesI.csv
e11231fbb09a29762dbb318a733be329a1dfea2ba2cad4e13a6208766b0134a8  SR1_M87_2017_095_lo_hops_netcal_StokesI.csv
769e5ab12c47f3f4ad5da99e7ed44594111717e831c5aa5e4a5c366cfc0bd6b6  SR1_M87_2017_096_hi_hops_netcal_StokesI.csv
fd4d1b39ab2e561f502d70c93667d67a525aa9ac4af432ceed01669e039911c5  SR1_M87_2017_096_lo_hops_netcal_StokesI.csv
3e6f034e12212a862632e6242b26335e4b48c68cfa87647632834cd43714a353  SR1_M87_2017_100_hi_hops_netcal_StokesI.csv
1dc51e3e31a840ec34de5b5ff4d8a6af0cbb73cd8c6db85e917366ed3ec7924a  SR1_M87_2017_100_lo_hops_netcal_StokesI.csv
7710f9a5c830ded0749e4f52ced75438435faf8bfb0b6e11b9e3adec25489b92  SR1_M87_2017_101_hi_hops_netcal_StokesI.csv
6411680cdd4a0b6a651b56c8ada9069ae49659935877ff7e03acb9b173a80bb2  SR1_M87_2017_101_lo_hops_netcal_StokesI.csv
a89d6efd29322c9ed1437bf3f8bd9f5083f7360b996b3062858a432b52826d9b  L2V1_M87_2018_111_b1_hops_netcal_10s_StokesI.csv
d005092d7201304cd25b446d8f5d867d9ea449ed8055e57133327aca580c6314  L2V1_M87_2018_111_b2_hops_netcal_10s_StokesI.csv
79bdbcb5f8124323bff733095e6fa998071b8a5bce4edbbba26f4f83eb652187  L2V1_M87_2018_111_b3_hops_netcal_10s_StokesI.csv
ef1b5f61c06846129e027fb91b5e1d1a7361ad4581bd18b414e7362e77aded7d  L2V1_M87_2018_111_b4_hops_netcal_10s_StokesI.csv
6f79e4c2d00102465f51fb150add9d0ea7a124d44b17df7390fcfab97670a302  L2V1_M87_2018_112_b1_hops_netcal_10s_StokesI.csv
2ef696731ed39ad4380a984a2c6d6858b4df7b0aecf389bdf395ead2846e0b06  L2V1_M87_2018_112_b2_hops_netcal_10s_StokesI.csv
519f90e02f2a8c085ff3791cc0650d4144cdd642a8512eba5b26aa183465ed58  L2V1_M87_2018_112_b3_hops_netcal_10s_StokesI.csv
817e26d44486bea0e8f592886e68a34b672f5b21fcebc832deee2d2df4951ded  L2V1_M87_2018_112_b4_hops_netcal_10s_StokesI.csv
801aa7a65a7d079b820bb7a2f22378d2c2ab585895a609658f26b83815ee0eda  L2V1_M87_2018_115_b1_hops_netcal_10s_StokesI.csv
1020d904ce28ae7504df2878839d74d9fef6224e3efee2187e8c0b538ca410b5  L2V1_M87_2018_115_b2_hops_netcal_10s_StokesI.csv
cc0db19ee5110725d52d4dd79e9ce60daaf8a85cce60e8996d5ce50c8920a673  L2V1_M87_2018_115_b3_hops_netcal_10s_StokesI.csv
94dab15bb7333a3c17385d015eb47894f8343dc74a49c86bcc30f780d0a600cc  L2V1_M87_2018_115_b4_hops_netcal_10s_StokesI.csv
```

**Run 1** (18 Nov; `runs/eho/eho3.py`, `runs/eho/eho2.py`, outputs `.out`; run as
`python3 runs/eho/eho2.py "<dir>/2019-D01-01/csv/SR1_M87_2017_*_StokesI.csv" "<dir>/2024-D01-01/csv/L2V1_M87_2018_*_hops_netcal_10s_StokesI.csv"`).

- **Q6 killed by my sign, its content not.** The local scale of a boost on a small source is **1/D** of the seen
  direction (D = 1/(γ(1 − β cos χ′))), not D: sources ahead, where D > 1, look smaller (aberration crowds them toward the
  apex). Matched to 2·10⁻⁶¹ at all twelve (β, χ); the rotation exactly 0 at all twelve (the derivative of w ↦ e^(−η)w is
  real and positive); a ring of radius 21 μas maps to a circle to 1.3·10⁻⁴¹ (rounding; a Möbius map keeps circles).
- **Q7 not killed.** Largest change of a 42 μas ring: Earth's spin 6.5·10⁻⁵ μas, Earth's orbit 0.0042 μas, the Sun
  against the CMB 0.052 μas, all under 2% of the 3 μas error. At EHT precision the observer's own motion is negligible;
  the observer layer enters as D carried in (a write) and the sky's orientation.
- **Q2 not killed.** 2017, four days × two bands: the first null u₀ spread 2.7% (3.747–3.848 Gλ).
- **Q3 not killed.** 2017 mean diameter 41.80 μas (41.03–42.14), 0.5% from 42.
- **Q5 (recorded, my prediction wrong).** The bright side's angle in my fit spans 78° over the 2017 days (and 32° between
  the two bands of day 100), against my < 20°. The angle's zero is my model's convention (not checked against the EHT's
  position angle east of north); only differences are used.
- **Q4 killed.** 2018 day 111 (its four bands agreeing to 2.1% in u₀): u₀ 3.503 Gλ against 2017's 3.778, 7.3% off
  (diameter 45.1 against 41.8 μas); day 112 5.9% (sparse: 38–315 closure phases, χ²/n near 7); day 115 9.1% (bands b1, b2
  at 33.5 μas, plainly failed fits). The bright side moved: 69°, −18°, 50° from 2017's mean on days 111, 112, 115 (my
  convention), so the payload did change; but my fit's diameter moved past 5% too. The EHT's own 2018 diameter is 43.3
  (+1.5/−3.1) μas, consistent with 2017, so this is my simple fit, not a claim about M87*.
- **Post hoc** (`runs/eho/eho2-posthoc.py`, not a prediction): with the blur held fixed at 5, 10 or 15 μas for every
  day, 2018 (days 111, 115, bands b3, b4) still comes out 1.07–1.09 times 2017. So the width trade does not explain it.
  Not checked: station gains (fitting amplitudes directly leaves them in; closure amplitudes would not), the 2018 array's
  different coverage (GLT and KP added), and a model with more azimuthal terms. Unresolved.
- **Q1 not killed (a reading, mine, not blind).** Every quantity in the table placed: the ring's diameter steady within
  2017 and moved by emission's assumptions between fits (S mixed with E: in this run the fitted d is where E leaks in,
  as the EHT's calibration factor says); θ_g S through the calibration; mass and distance writes; width, brightness angle,
  contrast and flux E (the angle and the flux both changed day to day here, F 0.24–0.40 Jy in 2017); the image's
  orientation O with S's spin axis. None needed a fourth layer.
- **What the run says.** The observer's own layer is exact and negligible at this precision (Q6's content, Q7): the
  three-layer sorting is in practice two layers, spacetime and emission, plus the writes carried in. Separating those
  two from one array's data is where the difficulty is, as the field says: my one-model fit held the size across a week
  and lost it across a year.

**Run 2, predictions** (18 Nov, committed before the fit; Tom: "merge, than try closures"). Run 1's Q4 left one cause
untested that the fit itself could remove: station gains. Run 1 fitted visibility amplitudes directly, and network
calibration leaves station gain errors of several percent to tens of percent on amplitudes, which a ring's size can
absorb. Closure amplitudes |V_ab||V_cd|/(|V_ac||V_bd|) over each quadrangle of four stations at one time, and closure
phases over each triangle, cancel every station gain. Run 2 fits the same m-ring (order 1, Gaussian blur) to closure
phases and log closure amplitudes only, with the flux fixed (closures carry no overall scale), the same baselines
(> 0.1 Gλ), each visibility's error with 10% in quadrature as before. `runs/eho/eho4.py`.

- **Q8:** 2017's diameter from closures stays steady over the four days and two bands: spread (max − min)/mean under 5%.
- **Q9:** 2018 days 111 and 115 (bands b3, b4, the best covered, as in run 1's post hoc), mean diameter within 5% of
  2017's closure mean. Killed if more than 5% apart. If killed, station gains are not the cause of Q4's gap, and what
  is left is the array's coverage or the model.
- **Q10 (recorded, not a kill):** 2018 day 112's fits, with 38 to 315 closure phases, are too sparse to count; reported only.

**Run 2** (18 Nov; `runs/eho/eho4.py`, `runs/eho/eho4.out`). The first pass crashed at day 112 (no quadrangle of four
stations at one time, so an empty array; my code), fixed and rerun with the predictions unchanged.

- **Q8 killed.** From closures alone 2017 splits in two: April 5–6 at 41.9–42.6 μas, April 10–11 at 46.8–48.0 μas, a
  spread of 13.7%. The blur w sits at its bound of 0 on all eight 2017 fits, so diameter and width are not held apart
  without the amplitudes' overall scale.
- **Q9 not killed, by its letter.** 2018 days 111 and 115 (bands b3, b4) average 45.9 μas against 2017's closure mean
  of 44.9, 2.3% apart; but that mean is the average of Q8's two groups, so the agreement means little.
- **Q10 (recorded).** Day 112 has no closure amplitudes and 38–315 closure phases; its fits range 41.7–61.5 μas, with
  errors up to ±970.
- **Post hoc, not a prediction.** Taking out the station gains did not settle the year-to-year question. It took away
  what had held 2017 steady in run 1. In closures this simple ring's diameter trades against its width and brightness
  contrast: the 2017 days with the larger contrast (b 0.39–0.42) come out larger, and 2018 fits a wider blur (w 12–17).
  So in this model the diameter carries the emission (E) whichever way it is fitted. That is the mixing of spacetime and
  emission the field describes, and why the EHT calibrates its ring against simulations. Separating them needs a richer
  emission model (more azimuthal terms, a thickness, the large-scale flux) or the photon subrings, not a simpler fit.
  Not run: such a model.

**Run 3, predictions** (18 Nov, committed before the fit; Tom: "merge, then try a richer model"). Run 2 found the
simple ring's diameter trading against its width and contrast. Run 3 gives the emission more room so that the diameter
need not carry it: an m-ring of order 3 (Johnson et al. 2020's family: V = Σ_k β_k J_k(π d ρ) e^{ik(φ − π/2)}, β₀ = 1,
β₋ₖ = β̄ₖ, three complex β), blurred by a circular Gaussian of FWHM w, plus a filled disc of the same diameter holding
a share f of the flux (a floor inside the ring). Nine parameters (d, w, f, β₁…β₃). Fitted, as in run 2, to closure
phases and log closure amplitudes only (station gains cancel), the same baselines and errors. `runs/eho/eho5.py`.

- **Q11:** 2017's diameter steady over the four days and two bands: spread under 5% (run 2 had 13.7%).
- **Q12:** 2018 days 111 and 115 (bands b3, b4) within 5% of 2017's mean.
- **Q13:** the fit improves: median χ²/n over the 2017 and 2018 b3/b4 fits lower than run 2's.
- **Q14 (recorded):** if Q11 or Q12 is killed with Q13 not, the extra room went to fitting noise, not to separating
  diameter from emission; the next step would be the subrings, which this array cannot resolve.

**Run 3** (18 Nov; `runs/eho/eho5.py`, `runs/eho/eho5.out`). The first pass, one file at a time, was stopped after five
files for time and rerun whole with the same fit and starts, one process per file; the five agree.

- **Q11 killed.** 2017's spread grew to 25% (38.4–49.8 μas), against run 2's 13.7%. April 5–6 at 38.4–44.3, April 10–11
  at 48.3–49.8; even one day's two bands differ by 3.1 μas (April 5) and 3.3 μas (April 6), where the errors are under 0.6.
- **Q12 not killed, by its letter.** 2018 days 111 and 115 (b3, b4) average 45.9 μas against 2017's 45.1, 1.8% apart; again
  a mean over 2017's spread, so it means little.
- **Q13 not killed.** The fits are better: median χ²/n 1.18 for 2017 (run 2's 1.29) and 1.32 for 2018 b3/b4 (run 2's 1.35).
- **Q14 applies.** The extra room improved the fit and loosened the diameter: the floor's share f takes 0.00 to 0.37 in
  2017, and the diameter moves with it (the days with f 0.35–0.37 the largest). More emission structure gave the
  diameter more to trade against, not less. From closures on this array, with these models, the ring's diameter is not
  separated from the emission; a richer model fits the payload better and leaves the spacetime's size less fixed.
- **What the three runs say together.** The EHT's steady 42 μas rests on what these fits lacked: amplitudes held by
  the a-priori calibration (run 1, which held 2017 to 2.7%), imaging and modelling pipelines tested on synthetic data,
  and the ring calibrated against simulated emission. That calibration is where the payload's assumptions enter (item
  21). The clean split the sorting asks for, size by spacetime alone, needs the route test (the subrings), which this
  array cannot resolve. Not run further here.
