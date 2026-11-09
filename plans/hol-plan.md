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

(Nothing yet.)
