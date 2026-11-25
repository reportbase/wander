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

**Data, recorded before analysis.** VizieR J/ApJ/837/30 (Gillessen et al. 2017), fetched 25 Nov 2026 through
vizier.cfa.harvard.edu as ASU-TSV with all columns; VizieR's licence (https://cds.unistra.fr/vizier-org/licences_vizier.html).
`table5.tsv` (the astrometric and radial-velocity data, 216 rows, offsets in mas from Sgr A*, dates in fractional years):
135,790 bytes, sha256 70db6570fb2966c0322512328a443aa10047b7322b254f5f396a316c27b48705. `table3.tsv` (the paper's
orbital elements, for the comparison only): 10,657 bytes, sha256
b0db1869b253457a8bd38e8f20cdd82f9b760643d8fd37439b5c87eada1e8bf7. Not committed. Only the header has been read.
Rows used: Flag "a" with S2's two offsets present; radial-velocity rows dropped.

### Run 2, as it came out (`runs/kpl/kpl2.py`, output `kpl-run2.txt`)

145 astrometric looks of S2, 1992.224 to 2016.530.
- **V1 killed**: e 0.8107 from the untimed places against 0.884 (the paper 0.8839).
- **V2 killed**: the untimed places give four solutions (i 42.6° or 137.4°, Ω 24.1° or 204.1°, ω with them), none within
  3° of (134°, 227°, 66°). Killed twice over: by the values, and by my letter, since untimed places cannot settle the
  sense of motion (it needs the order of the looks) nor which node is ascending (it needs a radial velocity), so no
  untimed method gives one solution. I had not stated that.
- **V3 not killed**: M/2π from place alone against the dates is a straight line, median |residual| 0.0050 of a period
  (max 0.045, near pericentre).
- **V4 killed**: the period 16.394 observer's years against 16.0 (the paper 16.00).
- **V5 killed**: a 111.16 mas against 125 (the paper 125.5). With R₀ = 8.3 kpc carried in, 923 au and 2.9·10⁶ suns
  (the paper's 4.3·10⁶).

Post hoc, a check of my code (`runs/kpl/kpl2-check.py`, output `kpl-run2-check.txt`): the paper's own orbit (table 3)
made into places at run 2's 145 dates. Noise-free, every step is exact (e 0.8839, P 16.000 yr, a 125.50 mas, the paper's
elements among the four untimed solutions and the dates leaving two). With the paper's stated errors added (one seeded
draw), the same method gives e 0.776, P 16.45 yr and a 111 mas, the run's numbers within their scatter. So the kills
are my method's, not the data's or the geometry's: a conic fitted to noisy places, most of them along the slow far side
and few through the fast pericentre, is pulled to a rounder, smaller ellipse (the reweighted algebraic fit is not the
distance to the curve, and the error at pericentre is a large share of the ellipse's width there). The frame (Sgr A*'s
place and drift, fitted by the paper) is not what moved it; the check has the focus exactly at the origin and is pulled alike.

Reading: what run 1 shows exactly holds on the measured orbit in its form (the clock from place alone is a straight line
in the observer's years, V3), but my untimed estimator does not recover the shape from these looks. A fair test of the
untimed shape needs an estimator that fits the distance from each look to the projected orbit itself (the eccentric
anomaly of each look a free number, still no date used), checked first on the paper's orbit with its errors. That would
be run 3, with its own predictions.

### Run 3: the untimed shape by distance to the projected orbit, predictions before the data (25 Nov 2026; Tom: "Merge and Proceed")

The estimator run 2's post hoc note asked for (`runs/kpl/kpl3.py`): the unknowns are the Thiele–Innes constants A, B, F,
G, the eccentricity e and one eccentric anomaly per look, a free number, so no date enters; each look's residual is its
offset from its own point on the projected orbit over the stated errors; started from run 2's conic. Steps 2–4 then as in
run 2 (the clock from place, the period in the observer's years, a in mas).

Checked first on the paper's orbit (table 3's elements) at run 2's 145 dates with the stated errors, 20 seeded draws
(seed 1214; `kpl-run3-check.txt`), before this record: e 0.8851 ± 0.0061, P 15.990 ± 0.050 yr, a 125.89 ± 2.36 mas,
against 0.8839, 16.000, 125.50. The estimator is unbiased to within its scatter here; run 2's conic was not.

Predictions on the data, bounds three of those scatters:
- **W1.** e within 0.02 of 0.884.
- **W2.** Among the untimed solutions, one within 5° of (134°, 227°, 66°) in each angle; and the untimed places give
  four solutions, the dates two (the sense of motion), none settling the node's side (stated now; run 2's V2 did not).
- **W3.** M/2π from place alone against the dates, median |residual| under 0.01 of a period.
- **W4.** P within 0.15 yr of 16.0.
- **W5.** a within 7 mas of 125.5; nothing in au, GM or seconds without an amount carried in.
A miss is recorded as it comes out; the paper fits Sgr A*'s place and drift in its frame and the data here are used in
the frame as given, so a kill may be the frame's, and would be named so only with a check.

### Run 3, as it came out (`runs/kpl/kpl-run3.txt`)

The script printed its verdicts with run 2's bounds (its judging lines were reused unchanged): 3° for the angles, 1% for
P, 3% of 125 for a. The judgments below are by run 3's bounds as committed above.

- **W1 not killed**: e 0.8694 from the untimed places (0.015 from 0.884; χ²/dof 0.64).
- **W2 killed**: four untimed solutions as stated, the dates leaving two; the nearer (i 136.77°, Ω 222.39°, ω 60.36°) is
  2.6°, 4.6° and 5.6° from (134°, 227°, 66°): ω past 5°. The other is the same orbit with the node on the far side.
- **W3 not killed**: M/2π from place alone against the dates, median |residual| 0.0021 of a period (max 0.031).
- **W4 not killed**: P 16.130 observer's years (0.13 from 16.0).
- **W5 not killed**: a 119.29 mas (6.2 from 125.5); in au and suns only with R₀ carried in (990 au, 3.7·10⁶ suns at
  8.3 kpc).

Post hoc, not tested: against the check's scatter the data land e 2.4σ low, a 2.6σ low, P 2.8σ long, all three the
same way (a rounder, smaller, slower orbit). The check had the focus exactly at the origin; the paper fits Sgr A*'s place
and drift in this frame, which the run did not, so a frame offset is the first candidate. Not checked.

Reading: from places alone, with no date, the measured looks give S2's shape (e to 0.015, a to 5%) and its orientation up
to what places cannot hold (the sense of motion, the node's side); with the observer's years as ticks, the clock read from
place is a straight line, and the period comes out in those years (16.13). The size stays in mas: au, solar masses and
seconds come only with R₀ and the year carried in.

### Run 4: the frame (25 Nov 2026; Tom: "Merge, then check the frame"), the check before the data

Run 3's post hoc candidate: the paper fits Sgr A*'s place and drift in the astrometric frame, run 3 held both at zero.
`runs/kpl/kpl4.py` frees them in run 3's untimed fit, as a constant offset of the focus (still no date), or an offset and a
linear drift (the drift needs the dates). Checked first on the paper's orbit with its errors, 20 draws each (seed 1216;
`kpl-run4-check-offset.txt`, `kpl-run4-check-drift.txt`), before any data:
- offset: e 0.59 ± 0.10, P 17.3 ± 0.7 yr, a 105 ± 8 mas, the focus wandering 14 mas (truth 0.884, 16.0, 125.5, 0);
- offset and drift: e 0.47 ± 0.21, P 18.4 ± 1.5 yr, a 105 ± 11 mas, the focus wandering 41 mas.

Read before the data: the untimed places do not place the focus. An ellipse is fixed by its points; where its projected
focus sits inside it is not, and every point inside is the projected focus of some orbit through the same places, with
its own e. Run 3 had the focus given (Sgr A* at the origin of the frame); free it and the shape is gone. What places a
focus not seen, classically, is the timing: Kepler's second law, equal areas in equal times, holds about one point only.
So the frame cannot be checked untimed. Run 4 is the timed fit instead (below), and the untimed modes are not run on the
data.

### Run 4b: the timed fit with the frame freed, predictions before the data

Mode `timed` in `kpl4.py`: the orbit fitted to the places against their dates through Kepler's equation (A, B, F, G, e,
P, the time of pericentre), the focus at (x₀ + v_x(t − 2009), y₀ + v_y(t − 2009)); classical (Gauss's angles and times).
Two fits on the data, the frame held at zero and the frame freed; each checked first on the paper's orbit, 20 draws.
Predictions, written after the check and before the data:
- **Y1.** With the frame freed, e, P and a each within 3 of the check's scatters of the paper's values.
- **Y2.** With the frame freed the three move toward the paper's from the frame-at-zero fit (all three nearer).
- **Y3.** The fitted offset under 3 mas and the drift under 0.5 mas/yr (a frame's size, not an orbit's).
If Y1 and Y2 are killed, the frame is not what moved run 3.

Run 4b's checks, before the data (`kpl-run4b-check-timed.txt`, `kpl-run4b-check-timed0.txt`, 20 draws each, seed 1216):
the frame freed, e 0.8830 ± 0.0043, P 15.989 ± 0.041 yr, a 124.94 ± 2.02 mas, the offset's scatter 1.0 and 0.3 mas,
the drift's 0.09 and 0.05 mas/yr; the frame at zero, e 0.8843 ± 0.0019, P 15.994 ± 0.019 yr, a 125.56 ± 0.71 mas. So
Y1's bounds are e within 0.013, P within 0.12 yr, a within 6.1 mas of 0.884, 16.0, 125.5.

### Run 4b, as it came out (`runs/kpl/kpl-run4b.txt`)

The frame at zero: e 0.8793, P 16.091 yr, a 123.32 mas, χ²/dof 1.05, (i, Ω, ω) (134.79°, 224.95° or 44.95°, 63.54° or
243.54°). The frame freed: e 0.8752, P 16.125 yr, a 121.84 mas, χ²/dof 0.97, offset (0.742, 0.929) mas, drift (−0.043,
0.027) mas/yr, (135.27°, 223.61° or 43.61°, 62.60° or 242.60°).
- **Y1 killed**, narrowly, by P: 16.125 yr against 16.0 ± 0.12; e (0.009 off) and a (3.7 mas off) inside their bounds.
- **Y2 killed**: freeing the frame moves all three away from the paper's values (e 0.879 → 0.875, P 16.09 → 16.13,
  a 123.3 → 121.8), not toward them.
- **Y3 not killed**: the offset under 1 mas, the drift under 0.05 mas/yr.

So the frame is not what moved run 3: it is small, as the paper's is, and it moves the orbit the wrong way.

Seen after the run, not tested: the timed fit with the frame at zero is nearer the paper than run 3's untimed one (e 0.879
against 0.869, a 123.3 against 119.3, P 16.09 against 16.13), but still 2.6σ, 5σ and 3σ from it by its own check's
scatter. What the paper has and these runs do not: the radial velocities (fitted jointly, they pin e and the orientation
through pericentre, where the places are fewest), the Rømer delay (light-travel time across the orbit, a few days near
pericentre) and a joint fit of R₀. The velocities are the first candidate; they are amounts in a unit, so bringing them
in is the step from looks to writes, and would be a run of its own.

Reading: the untimed shape needs the focus given (run 4's check); with it given, the looks give S2's shape to about 1–2%
(runs 3, 4b); the remaining 1–3% gap to the paper's orbit is not the frame.
