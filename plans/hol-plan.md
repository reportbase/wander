# HOL: loops that come back turned

9 Nov 2026. Tom: "yes", to a section gathering the loops that come back turned, with a test that can fail on
published data. Predictions are written before any data is looked for.

## What is claimed

**A read is one standpoint at one moment** (*Reads and Writes* §1). A loop of reads joined end to end is a write: the
legs are held together and counted. The reading:
- **The plane.** Joined reads come home unturned whatever the loop, because turns of the plane commute.
- **The sphere of directions.** They come home turned by the area the loop encloses (Gauss–Bonnet), because turns of
  space do not commute.
- **The turn is a direction.** No amount enters it, so scaling the world leaves it alone, and no clock is needed to read
  it. A *rate* of turning (degrees an hour) needs a clock carried in.

**Known beforehand** (named so the runs do not claim them):
- **TWG.** `plans/twg-plan.md`: the Thomas–Wigner rotation read from three stars' directions alone, equal to the
  velocity triangle's area; the small loops' coefficients c_T = −1/12 and c_B = 1/3 + cos φ/4 (runs 1–3).
- **Essay 13.** A quarter turn about h, then about v, then back about each, comes home turned 90°, and the plane's same
  loop does not.
- ***Reads and Writes* §11.** Berry's phase: the geometric half is the solid angle, an address; the dynamical half is
  energy times time.
- **Classical throughout.** Gauss–Bonnet; Foucault's sin φ (1851); Berry (1984); Tomita and Chiao (1986); Thomas
  (1926). Nothing here is new physics.

## Predictions

### Exact (mpmath, 50 digits; `runs/hol/hol.py`)

- **H1 (the sphere).** Parallel transport round a closed loop on S² turns a vector by the loop's enclosed solid angle,
  mod 2π.
  - Latitude circles at 12 latitudes, and 200 random geodesic triangles and quadrilaterals.
  - Transport is computed by composing small rotations along the path (2,000 steps a side, Richardson-extrapolated), not
    from the formula.
  - **Killed** if any differs by more than 10⁻²⁰ after extrapolation.
- **H2 (the plane).** The same transport in the plane gives zero turn for every one of the same loops laid flat.
  **Killed** past 10⁻⁴⁰.
- **H3 (velocity space).** For boosts joined round a closed loop of velocities (H³, curvature −1 in rapidity), the
  Wigner turn equals minus the loop's hyperbolic area.
  - 200 random triangles, rapidities 0.01 to 3; this extends TWG from small loops to large ones.
  - **Killed** past 10⁻²⁰.
- **H4 (scale and clock).**
  - The turn is unchanged when every length of the loop is scaled (the sphere's radius and the velocity unit cancel).
  - A two-leg loop (out and back on one line) encloses nothing and turns nothing.
  - **Killed** if not, to 10⁻⁴⁰.

### On published data (`runs/hol/hol2.py`, after the exact run)

- **H5 (Foucault).** The pendulum's plane turns, relative to the ground, by 360°·sin φ per sidereal day, φ the latitude:
  the area a latitude circle leaves out of the hemisphere.
  - Every published measurement found that gives a turn rate with an error, at a stated latitude, is reduced to degrees
    per sidereal day over sin φ.
  - Prediction: 360° within 3 combined errors at each site, and χ² across sites with p > 0.001.
  - Sites whose papers report a correction for ellipsoidal (Airy) precession are taken corrected; those that report none
    are listed but not counted, decided by the paper's text before its number is read.
  - **Untested** if fewer than three sites qualify.
- **H6 (Berry, light in a coiled fibre).** Tomita and Chiao 1986: the polarization turns by the solid angle the wave
  vector traces.
  - Prediction: a straight-line fit of the measured rotation against the solid angle has slope 1 and intercept 0, each
    within 3 errors.
  - The points are read from the paper's table or text, or from its figure by hand. The method is recorded; values read
    from a figure are marked as such.
  - **Untested** if neither can be reached.
- **H7 (reported, not counted).** Thomas's half in hydrogen's n = 2 fine structure. The measured 2P₃/₂–2P₁/₂ interval
  against the Dirac value (which contains the half), and against twice the spin–orbit part (which would hold without
  it). Classical; reported as the case where a joined loop's leftover is read in a spectrum.

## Bridges, named

- **The turn per loop:** none; a direction.
- **Foucault's rate per hour:** the sidereal day, a clock. The test is stated per sidereal day so that the clock enters
  only through the site's own reduction.
- **Berry's rotation against the solid angle:** none; the coil's pitch and radius give the solid angle as a ratio.
- **H7:** the Rydberg and α, carried in.

## Runs

### Run 1 (9 Nov; `runs/hol/hol.py`, output `runs/hol/hol-run1.txt`; `runs/hol/hol2.py`, output `runs/hol/hol-run1-data.txt`)

The exact run was started once at 32 digits, then stopped before it reported anything: the plan's 10⁻⁴⁰ for H2 and H4
was finer than that precision. It was restarted at 50 digits with the predictions unchanged, and its polygons spread over
four cores. It took 47 minutes.

**Exact: nothing killed.**
- **H1 (the sphere).**
  - 12 latitude circles turn by their cap's area to 2.7·10⁻⁵⁰.
  - 200 random geodesic triangles and quadrilaterals turn by their signed area to 1.0·10⁻⁴⁹.
  - Transport was integrated as an ODE; the area was computed separately.
- **H2 (the plane).** None of 50 loops turns. This was guaranteed in advance: flat transport is v′ = 0.
- **H3 (velocity space).** For 200 loops of boosts with rapidities 0.01 to 3, the Wigner turn equals minus the
  hyperbolic area to 1.5·10⁻⁴⁷, sign included. TWG's small loops carry to large ones.
- **H4 (scale).**
  - The turn is the same on spheres of radius 10⁻³, 7 and 10⁶, to 9·10⁻⁵⁰.
  - Loops out and back along one line turn nothing: 4.5·10⁻⁵¹ on the sphere, 2.5·10⁻⁴⁹ in velocity space.

**Data.**
- **H5 untested.** One site met the plan's rules: Schumacher and Tarbet 2009 (arXiv:0902.1829, sha256
  `e228c2d8eb1d78d79766176ee526a1f77cac39bdb542236cc46103ba5b2991ea`).
  - Their pendulum is driven so as to be free of ellipsoidal precession, decided from their text before their number
    was read.
  - Their weighted mean, −9.69 ± 0.09°/h at Pittsburgh (40°26′26″), is 357.6 ± 3.3° per sidereal day over sin φ: 0.74σ
    from 360°. Their simple mean, 363.5 ± 5.5°, is 0.63σ from 360°.
  - The plan asks for three sites, so this is reported, not counted.
  - Not counted:
    - an ASEE student study at York and San Nicolás (peer.asee.org; no ellipse correction, no error on the rate);
    - Foucault's 1851 Paris value and Kamerlingh Onnes's 1879 thesis, reached only as secondary accounts without the
      paper's own numbers;
    - arXiv:2502.12230 (a model of a pendulum, its measured rate given without an error).
- **H6 untested.** Tomita and Chiao 1986 could not be reached. The APS page refuses, and the reviews read (arXiv:1008.5331;
  Chiao and Wu's companion paper from the Utah repository) give no data.
- **H7 (reported, not counted).**
  - The Dirac value (Thomas's half included) of hydrogen's 2P₃/₂–2P₁/₂ is 10,949.648 MHz.
  - The measured interval, 10,969.045 MHz, is taken as 2S₁/₂–2P₃/₂ (Hagley and Pipkin 1994) plus the Lamb shift; both
    values are from memory, to check.
  - Measured over Dirac is 1.0018; the rest is QED (the electron's anomalous moment and the Lamb shifts). Measured over
    the interval without Thomas's half is 0.501.

**What the run says.**
- Joined reads come home turned by the area their loop encloses. This holds on the sphere of directions and, as the
  Wigner rotation, in velocity space; in the plane they come home unturned.
- The turn carries no amount: scaling the sphere moves nothing, and a loop with no area turns nothing.
- All of it is classical (Gauss–Bonnet, Wigner, Thomas). The data part could not be tested, for want of reachable
  measurements.

**Checked after the run (9 Nov; Tom: "1,2").** H7's two numbers, recorded above as from memory, were read from the
papers' abstracts (through OpenAlex; sha256 of the responses `81089927e757877a348ca83f74fa32bda997d153a6d561ddaf1a276b3b2039e7`
for Hagley and Pipkin 1994, PRL 72, 1172, and `359d111de2c7bfbd56fa2f68d3c2e80b3779ac5a3e83e203c86d528f2d37eddf` for
Lundeen and Pipkin 1981, PRL 46, 232): 2S₁/₂–2P₃/₂ = 9,911.200(12) MHz and the Lamb shift 1,057.845(9) MHz, both as used.
The measured interval is 10,969.045 ± 0.015 MHz; the ratios stand (1.00177, 0.500886). Hagley and Pipkin's own Lamb
shift implied by theirs is 1,057.839(12) MHz; the sum uses Lundeen and Pipkin's, measured apart. Still reported, not counted.

### Run 2 plan: the sphere's leftover in other data (9 Nov; Tom: "1,2"; written before any data is looked for)

Run 1's data part rested on one Foucault site. Run 2 looks for the same leftover (a turn equal to the solid angle a loop
of directions encloses, no amount entering) in measurements that report it against the solid angle.

**Known beforehand, from memory, to be checked against the papers:**
- Tomita and Chiao 1986 (PRL 57, 937): linearly polarized light in a helically wound fibre; the polarization turns by the
  solid angle the wave vector's direction encloses on its sphere, Ω = 2π(1 − cos θ), θ the helix's pitch angle; uniform
  and non-uniform coils; agreement said to be good. The numbers were not reached in run 1.
- Bitter and Dubbers 1987 (PRL 59, 251): polarized neutrons through a field whose direction is turned round a cone; the
  spin's extra turn equals the cone's solid angle, in the adiabatic limit, and departs from it as the passage gets fast.
- Later repeats likely exist (photons in a non-planar Mach–Zehnder, Chiao et al. 1988; spin-½ in NMR, Suter et al. 1987;
  neutron interferometry). Which give numbers with errors is not known.

**What counts.** A measurement counts if it reports, with errors, a turn (a polarization rotation or a spin's extra
precession angle) and the solid angle of its loop, or the loop's geometry from which the solid angle follows
(pitch angle, cone angle). The point's error is the paper's; a value read from a figure by hand is marked so, with a
reading error of half the smallest tick stated before it is read. Points the paper marks non-adiabatic (or that lie on
the fast side of its stated adiabaticity condition) are listed, not counted, decided from the text before the numbers
are read. A spin-½ state's phase is half the solid angle; what is compared is the rotation of the observed direction,
which is the whole solid angle (the two spin states' phases differ by Ω).

**Predictions.**
- **H8 (each experiment).** A straight-line fit of the measured turn against Ω has slope 1 and intercept 0, each within
  3 combined standard errors. Killed if either fails on an experiment with three or more counted points.
- **H9 (all together).** χ² of (turn − Ω)/σ over every counted point, p > 0.001. Killed if not.
- **H10 (no amount).** Where an experiment varies something that is an amount (fibre length at fixed pitch, field
  strength, neutron speed within the adiabatic range), the turn at fixed Ω does not move with it beyond 3 errors.
  Killed if it does.
- **H5 again (Foucault).** Any further site found under run 1's rules joins it; tested once three sites qualify.
- **Untested**, said plainly, if no experiment with three counted points can be read here.

**Bridges named.** None for the turn against Ω (two directions). For neutrons, the field strength and speed enter only
the adiabaticity condition and the dynamical phase, which the experiments separate; both amounts, both carried in.

**Sources found, before any number is read (9 Nov).**
- Tomita and Chiao 1986 and Bitter and Dubbers 1987: abstracts only (OpenAlex); the papers are not open here.
- **Leek et al. 2007** (Science 318, 1889; arXiv:0711.0218, source sha256
  `4a197a155bddf982c60b9394e1b8dac211335dc90f2ede79381106d73ea8abc6`): Berry's phase of a superconducting qubit, the
  field direction taken round cones of half-angle θ, Θ = 2π(1 − cos θ). From the text, before the figure was looked at:
  - every experiment adiabatic (A ≤ 0.04), so every point counts;
  - the sequence (loop, spin-echo π pulse, loop reversed) cancels the dynamical phase and leaves φ = 2γ_C, where γ_C is
    the relative phase of the two states over n loops, nΘ (each state ±Θ/2 a loop); so the turn compared is φ against
    the total solid angle 2nΘ, signed by the direction of the paths, with C₊₊ predicted zero. The text says "slope 2n";
    the caption's "slope n = ±1, ±1.5" disagrees, and the text's reading is the one fixed here;
  - the numbers are only in Fig. 3A, a raster image (fig3.eps holds a JPEG), so they are read by hand from it, each
    reading's error half the smallest tick on its axis unless the figure's own error bars are larger;
  - the paper's own summary: an r.m.s. deviation of 0.14 rad from the predicted lines across all sets.
  - H10 can be tried only with T: the text says the phase was independent of T, without numbers; reported, not counted.
- arXiv:2407.19425 (a 2024 theory paper on helical fibres, sha256 `8823785dbf80f4af954af2428333d26ab4118f77c4f4293743ea904927ec1b3b`)
  quotes no data; it names measurements in Ross 1984, Tomita and Chiao 1986, Hannonen 2020 and Ferrer-Garcia 2023, to be
  sought.

### Run 2 (9 Nov; `runs/hol/hol3.py`, output `runs/hol/hol-run2.txt`, points `runs/hol/leek2007-fig3a-points.json`)

**How it was read.** Leek et al.'s Fig. 3A was read by template matching on its raster (the JPEG inside fig3.eps,
sha256 `757794301c182c63904824477ddd693e6bde2b7557f5c8a224396e0542d5ed1c`): 89 filled and 137 open markers found, an
overlay checked by eye, label areas dropped, points with Θ < 0.3 dropped (there the five series meet and marker and sign
cannot tell them apart). The axes are the figure's own ticks. The paper's red lines, read the same way, have slope 2n in
Θ (2.01 and 3.01 at the right edge), which settles the text-against-caption question as the plan fixed it.

**The first execution read wrong (my code).** The phase scale was put through `np.interp` over the ticks at π, 0 and
−2π, which holds every point above π at π. Its output had two series' slopes 2.3σ and 5.1σ off and would have killed
H8; it was the reading, not the data. Recorded here; the reading was corrected (a line through the three ticks) and run
again with nothing else changed.

**Counted, by the plan's errors (half the smallest tick: π/2 in φ, π/8 in Θ).** Nothing killed; 192 points.
- **H8.** Slopes against Ω = 2nΘ: 1.014 ± 0.20 and 1.028 ± 0.20 (n = 1, the two directions), 1.002 ± 0.15 and
  1.031 ± 0.15 (n = 1.5); intercepts within 0.3σ. C₊₊ (Ω = 0): mean φ −0.19 rad, 0.7σ.
- **H9.** χ² 3.3 on 192.
- **H10.** Not tried: the paper says the phase did not move with the sequence time T, without numbers.
- **The test is weak as counted.** The tick rule, written for reading by eye, gives errors ten times the points'
  scatter; χ² 3.3 on 192 says so. It is kept because it was fixed first.

**Reported, not counted, with the paper's own scatter (0.14 rad a point).** One line through all 192: slope
1.013 ± 0.003, intercept +0.04 ± 0.01. Per series the slopes are within 1–3% of 1 (+0.8, +1.7, +0.2, +2.9 of these
errors). The r.m.s. of φ − Ω is 0.245 rad against the paper's 0.14, most of it two things: C₊₊ sits 0.19 rad below zero
throughout (12 of its own standard errors; visible in the figure), and n = 1 C₊₋ starts 0.19 rad above its line. A 1%
slope is within what reading a raster's axes can give (a pixel in 676). So the turn is the cone's solid angle, doubled
by the echo, at 1% on a qubit, with an offset of about 0.2 rad the paper does not discuss.

**Still untested.** H5 (Foucault): no further site found with an error and a stated ellipse correction. Tomita and Chiao,
Bitter and Dubbers: abstracts only. Ross 1984, Hannonen 2020 and Ferrer-Garcia 2023 (named by arXiv:2407.19425) were not
found on arXiv. One experiment counted, which the plan allows (H8 asks three points, H9 all counted points).

**What run 2 says.** On real data the loop's leftover is its solid angle: a qubit's phase follows 2nΘ over 192 points,
cones from 0.3 to 2.6 sr, both directions, one and one-and-a-half loops, and the loop that cancels itself (C₊₊) leaves
nothing but a small offset. The amounts (the field's strength, the time) enter nowhere in the comparison. Classical:
Berry 1984, measured by Leek et al.
