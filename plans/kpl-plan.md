# KPL: an orbit's clock from looks alone, in its own period

25 Nov 2026. SPN R1210. Tom: "Kepler test", taking up Claude's offer after Gemini's question (does ORB's r/a payload
connect to time to contact?). Claude's answer then: in both, a ratio gives time in the system's own unit (τ in the
observer's ticks; Kepler's mean anomaly in the orbit's period), and seconds need an amount carried in (a clock; GM and
a). This test puts the orbit half to exact arithmetic.

## Set-up

A planet on a Kepler ellipse (eccentricity e, perihelion direction ω, semi-major axis a, period P = 2π√(a³/GM)), looked at
from the focus. Each look gives two numbers: the direction ν (a slope tan(ν/2), the writer's angle only as notation) and
the planet's angular size α, which for a planet of fixed radius is proportional to 1/r. The observer also counts ticks of
its own clock, in an unknown unit (a tick is c seconds, c unknown). Looks are taken at N ticks.

Three observers, by what each holds:
- **D:** directions only, untimed (a set of looks with no order).
- **DT:** directions and ticks.
- **DS:** directions and angular sizes, untimed.
- **DST:** all three.

Nothing an observer holds carries a, GM, the planet's radius or the tick's length in seconds.

## Predictions (committed before any code)

- **K1 (shape from DS, no time).** The ratios α/α_max give r_p/r. With the directions, 1/r ∝ 1 + e·cos(ν − ω) is linear
  in (1, cos ν, sin ν), so e and ω come from three looks exactly, and from N noise-free looks by least squares to 10⁻¹².
  No time and no unit enter.
- **K2 (the clock as geometry).** Given e and ν, the mean anomaly M = E − e·sin E, with tan(E/2) = √((1 − e)/(1 + e))·tan(ν/2),
  is a function of position alone: the fraction of the period spent from perihelion, M/2π, is known from DS with no clock.
- **K3 (DST: period in ticks).** M/2π against the observer's ticks is a straight line exactly (noise-free, residual under
  10⁻¹²); its slope gives P in ticks. Two looks suffice once e and ω are known.
- **K4 (DT: directions and ticks alone suffice).** Without angular sizes, the directions at known ticks fix e, ω, P in
  ticks and the time of perihelion (a fit of ν(t) through Kepler's equation), to 10⁻¹⁰ from noise-free looks. Angles-only
  orbit determination, classical (Gauss 1809).
- **K5 (D alone fails).** Untimed directions alone fix nothing of the shape: any set of directions is met by every e
  (for each e, the same directions occur on the orbit). A sanity check, by argument and one numerical case.
- **K6 (no amount from any of them).** Scaling a by λ and the tick by λ^(3/2) (Kepler's third law with GM fixed), or
  GM by μ and the tick by μ^(−1/2) with a fixed, leaves every look and every tick count unchanged to rounding. So no
  observer here recovers a, GM or P in seconds; P in seconds needs one amount carried in (the tick's length), and a then
  needs GM as well (a³ = GM·P²/4π²).
- **K7 (with noise).** Directions with error 10⁻⁴ rad and angular sizes with relative error 10⁻³, 200 looks evenly in
  time over two periods, e = 0.3: e recovered within 3 standard errors of the truth by a seeded bootstrap (200 resamples),
  P in ticks within 3 standard errors, the bootstrap's relative error on P under 10⁻⁴.

## What a pass shows, stated now

Classical throughout (Kepler 1609, Gauss 1809's determination from angles and times). What is sorted: the clock of an
orbit, as a fraction of its period, is a function of position (K2), read from looks; time in seconds and the orbit's size
are amounts carried in (K6). This is the orbit's counterpart of time to contact counted in ticks (essay 6 §2). Not in any
paper until Tom says.

## Runs

### Run 1 (`runs/kpl/kpl.py`, output `kpl-run1.txt`): nothing killed

e = 0.3, ω = 0.7, a = 2.5, GM = 1.9, planet radius 0.01, a tick 0.0137 s (none of these known to the observers); 41
noise-free looks over two periods at 40 digits; then 200 noisy looks.

- **K1 not killed.** From directions and angular sizes, untimed: e to 1·10⁻⁴¹, ω exact.
- **K2, K3 not killed.** M from position alone, against ticks a straight line to 4·10⁻⁴⁰; the period 1315.20216084976
  ticks, to 2·10⁻⁴¹; from two looks, 1·10⁻⁴⁰.
- **K4 not killed.** From directions and ticks alone (no angular size), e, ω and P in ticks to double precision.
- **K5 not killed** (by argument; checked on ten looks for e = 0.05 and 0.9): untimed directions fix no shape.
- **K6 not killed.** Under a and the planet's radius scaled by λ with the tick by λ^(3/2), or GM by μ with the tick by
  μ^(−1/2) (three cases), no look and no tick count moves (5·10⁻⁴⁰): no observer recovers a, GM or seconds.
- **K7 not killed.** Directions to 10⁻⁴ rad and sizes to 10⁻³, 200 looks: e 0.299997 (0.46 standard errors from the
  truth), P 1315.2001 ticks (0.88 standard errors), the bootstrap's relative error on P 1.8·10⁻⁶.

**What it shows.** An orbit's clock, as a fraction of its period, is a function of position: e and ω come from looks with
no time (K1), the mean anomaly from e and the direction (K2), and one clock, the observer's own ticks, sets the period in
ticks (K3); directions and ticks alone do as well (K4). Nothing read gives the orbit's size, GM or seconds (K6): each is
an amount carried in, the tick's length in seconds first and then GM for a. The orbit's counterpart of time to contact in
the observer's ticks. Classical (Kepler, Gauss); K5 is trivial and was included as a check, not a finding.

### Run 2: a measured orbit, predictions before the data (25 Nov 2026; Tom: "Merge 509, then 1 and 2")

Run 1 was exact arithmetic with the observer at the focus. Here the observer is far off and sees the orbit projected on
the sky: each look gives the companion's place relative to the primary, two angles (offsets in RA and Dec), and the
observer's date, a tick (a year of its own orbit). Nothing it holds carries the distance to the system, GM or seconds.

The data: the star S2 about Sgr A*, the astrometry of Gillessen et al. 2017 ("An update on monitoring stellar orbits in
the Galactic Center", ApJ 837, 30), from VizieR (J/ApJ/837/30) through the CfA mirror; source, licence and sha256 to be
recorded before analysis. Radial velocities, if in the table, are not used: a velocity is an amount in a unit.

Known beforehand (not looked up for this run, from memory of the paper; to be checked when the data come): e 0.884,
i 134°, Ω 227°, ω 66°, P 16.0 yr, a 0.1255″ (125 mas), the mass 4.3·10⁶ suns at R₀ ≈ 8.3 kpc.

Method, fixed now:
1. **Untimed shape.** The places alone, dates dropped: a general conic fitted to them (least squares on
   Ax² + Bxy + Cy² + Dx + Ey = 1, weighted by the stated errors). Projection keeps ratios along a line, so the true
   eccentricity is the apparent ellipse's centre-to-primary distance over the half-chord through the primary along the
   same line (the primary at the origin, Sgr A*'s place in the paper's frame). Then the Thiele–Innes constants from the
   apparent ellipse and the focus (Kowalsky's method), giving i, Ω and ω, still with no dates.
2. **The clock as place.** With e from step 1, each look's eccentric anomaly from its place on the deprojected orbit,
   M = E − e·sin E, M/2π the share of a period passed since pericentre, from position alone.
3. **Period in ticks.** M/2π against the dates, a straight line; its slope gives P in the observer's years.
4. **Sizes.** The semi-major axis comes out in milliarcseconds only.

Predictions:
- **V1.** From the untimed places alone, e within 0.02 of 0.884.
- **V2.** From the untimed places alone, i, Ω and ω each within 3° of 134°, 227°, 66°.
- **V3.** M/2π from place alone (step 2) against the dates: the median |residual| from the straight line under 0.01 of
  a period.
- **V4.** The period from step 3 within 1% of 16.0 years.
- **V5.** a within 3% of 125 mas; and no step gives a in au, GM or the period in seconds without an amount carried in
  (R₀ for the first, R₀ and the year's seconds for GM). Reported with R₀ = 8.3 kpc as the classical check, not predicted.
Each killed if outside its bound. A kill from the frame (Sgr A* not at the origin of the positions, or a drift of the
frame) is recorded as such, not fixed in this run.
