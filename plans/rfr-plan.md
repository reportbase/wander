# RFR: REF revisited (the corner as the reference sphere, and one octave a level)

*Plan, predictions and kills written 22 October 2026, before `runs/rfr/rfr.py` was written or run (Claude, in a
sub-session revisiting REF in the light of what is settled since: address and payload (OFS §7.2), reading and writing
(OFS §9, "The test: scale the world"), the fixed count K and the Cauchy's height as a built-in level of detail (OFS §8,
"A fixed count, aimed by H", "A resolution, not cells", "What the height fixes"), a₀ never read (OFS §7.4; SPN R292), a
corner a median only under a reciprocal-symmetric law, and SPN R250, a .tvf3d a pre-read signal). The lab rules hold:
nothing above the "Runs" line is edited after the run. Exact arithmetic only (mpmath); no data is downloaded: the plan
of REF records only the first eight hex digits of each file's sha256, which is not enough to verify a fresh download, and
nothing below needs the shape models.*

## Known beforehand

- REF run 1 (`plans/ref-plan.md`): the "corner sphere" was defined as the **geometric mean** of the radius over the
  sphere, R̄ = exp(mean ln r), and depth as log₂(r/R̄). P4, P5: rocky worlds' flattening under 0.01 levels (Earth
  0.00483, Mars 0.00852, Moon 0.00174), giants about a tenth (Jupiter 0.09677, Saturn 0.14874).
- REF run 2: the reader's side was stated as exact and untested: "a body of radius R spanning a addresses across its
  disc holds the degrees up to about l_max = πa/2 (two addresses a wave at the disc's middle, where an address covers
  2R/a of surface) … past the corner a halves with each level of distance, so each level drops one octave … inside the
  corner the octaves held do not change. Nothing to test: it follows from the lay." (`plans/ref-plan.md` lines 142–145.)
  ρ_k = RMS_k·2^(k+1)/(πR) was offered as "an octave's relief in the reader's own addresses at the level where it is the
  finest held", 0.0002 to 0.07.
- Classical: a spheroid's area is uniform in the height μ = cos(colatitude) of directions from its centre (Archimedes);
  harmonic measure on a circle of radius R from a point at distance d > R is the Poisson kernel, mode n kept as (R/d)^n
  (the circle's own Cauchy, CIW's wrapped Cauchy); on a line seen from height γ mode κ is kept as e^(−κγ) and z ↦ 2z is an
  isometry (DYH run 2: the kept share depends only on γ/w′). The ray–sphere footprint is elementary.
- Draw's labs: not consulted for this plan (no reader of shapes is built here; the geometry is a sphere's).

## The reading to test

1. **The corner sphere is a₀, a mean, and the depth is a reading.** The geometric mean over the central reader's
   uniform directions is exp of the degree-0 term of ln r, which is a₀ = ln(V*/H): never read. The depth ln r − a₀ is the
   shape (every degree ≥ 1), a ratio of amounts in one unread unit, unchanged by scaling the world: a reading. The
   sphere's radius r̄ in metres, and heights above it, are writings (the bridge r̄). So REF's "corner" is the zero of the
   shape, a **mean of log-amounts**, a payload statistic, not a median; it is the median only when the depth's law is
   symmetric.
2. **One octave per level is the foot's, exactly, in levels of the altitude.** At the point under the reader (altitude a
   above a sphere of radius R), one address of angular width ε covers a·ε of surface (first order in ε), so the finest
   degree held there, two addresses a wave, is l* = πR/(aε): it doubles exactly as the altitude halves, at every altitude,
   with no corner in it. Run 2's disc rule (l = πα/ε, α = arcsin(R/d), the orthographic disc) is the far-field form; near
   the body the two part.
3. **The Cauchy's height gives one octave per level only on the plane.** Seen from altitude a over the tangent plane, the
   height cut e^(−κa) at κ = l/R moves exactly one octave per level of a (the isometry). The world's own Cauchy from
   d = R + a keeps (R/d)^n, cut at n ≈ 1/ln(1 + a/R): one octave per level only while a ≪ R. The K addresses' cut and the
   planar height's sit a fixed log₂(2K) octaves apart: K alone sets that gap.
4. **ρ_k is the payload's.** The outline's shift in addresses when an octave is first held, computed exactly at the limb,
   is 2·RMS/λ (λ the octave's top wavelength) at every distance and every ε: a ratio of the world's relief to its
   wavelength, with no reader (K, H, d) in it.

## Predictions

- **P1 (the corner sphere is a₀; depth a reading).** On a synthetic body ln r = a₀ + Σ c_lm·Y_lm (seeded, degrees 1–6),
  (a) the geometric mean of r over uniform directions (Gauss–Legendre in μ, trapezoid in azimuth, exact for these
  degrees) equals exp(a₀) to 10⁻³⁰; (b) scaling every length by k ∈ {10⁻³, 7, 10⁶} leaves every depth log₂(r/r̄) unchanged
  to 10⁻³⁰ and multiplies r̄ by k to 10⁻³⁰. *Killed* if any of these fails.
- **P2 (the corner sphere is not the median sphere).** For an oblate spheroid (equatorial a, polar c) read from its centre
  by uniform directions, the median radius is the radius at μ = ½ (latitude 30°) for every a, c (found by bisection on the
  exact law, to 10⁻³⁰), and it lies above the geometric-mean sphere by ΔL levels with ΔL/L in [0.99, 1.0] for Earth, Mars
  and the Moon and in [0.88, 0.99] for Jupiter and Saturn, L = log₂(a/c) on REF P4's radii (first order ΔL = L/12).
  *Killed* if the median misses μ = ½ by more than 10⁻²⁵ on any body, or any ratio falls outside its band.
- **P3 (one octave per level of altitude, at the foot).** By exact ray–sphere intersection, one address's footprint at
  the nadir over a·ε lies within 10⁻⁵ of 1 at ε = 10⁻⁶ for a/R = 10⁻³, 10⁻¹, 1, 10, 10³, so l* = πR/(aε) halves exactly per
  level of altitude through a = R. Run 2's disc rule drops d(log₂ l)/d(log₂ a) = −√3/π = −0.5513 octaves per level at
  a = R (exactly, to 10⁻²⁰), and its ratio to l* there is π/6 = 0.5236; at a = 10³R its rate is within 0.002 of −1.
  *Killed* if any of these fails.
- **P4 (the Cauchy's height cut).** (a) Planar: the kept share e^(−la/R) at (l, a) equals that at (2l, a/2) to 10⁻³⁰,
  one octave per level of a at every a. (b) The world's own Cauchy: the Fourier coefficients of the exterior Poisson kernel
  (quadrature, n = 1 … 8, d/R = 1.5, 3, 10) are (R/d)^n to 10⁻²⁰; its 1/e cut n_c = 1/ln(1 + a/R) moves
  log₂(ln(1 + 2a/R)/ln(1 + a/R)) octaves per level of altitude: at least 0.93 for a/R ≤ 0.1, 0.6644 at a = R (log₂ log₂ 3),
  under 0.25 at a = 100R. (c) At the foot the K-address cut over the planar height's cut is π/ε = 2K at every a: log₂(2K)
  octaves, 10 at K = 512. *Killed* if any value misses: (a), (c) and the coefficients by more than stated, the a = R value
  by more than 10⁻⁴, or a bound fails.
- **P5 (ρ_k is the payload's).** Put a sphere of radius R + h for relief h, and the reader at d with the limb's tangent
  distance ℓ = √(d² − R²); choose ε so that degree 2^(k+1) is first held along the limb (two addresses a wave over ℓε of
  surface: ε = πR/(2^(k+1)·ℓ)). The exact outline shift, [arcsin((R + h)/d) − arcsin(R/d)]/ε addresses, over
  ρ = h·2^(k+1)/(πR) (run 2's formula, with RMS → h) lies within 10⁻³ of 1 for d/R = 1.01, √2, 2, 10, 1000, k = 3 … 9 and
  h/R = 10⁻⁵, 10⁻⁴. So ρ_k = 2·RMS_k/λ_k (λ_k = 2πR/2^(k+1)), the same at every distance and every K. *Killed* if any
  ratio misses 1 by more than 10⁻³. Bookkeeping, not a prediction: run 2's printed ρ re-derived from its printed RMS as
  2·RMS/λ, to its printed digits.

## Not computed here

- The median of a real world's depth (Earth's hypsometry is bimodal; the median of SUR2014 sits at the sea surface): it
  needs the data, whose full hashes are not recorded.
- Shading (the disc's middle shows relief only through slope, not as a shift of any address).
- Which of the cuts a measured reader uses.

## Runs
