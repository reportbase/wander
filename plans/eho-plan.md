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
