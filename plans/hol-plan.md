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
