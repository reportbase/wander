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

### Run 1 (22 October 2026)

`python3 runs/rfr/rfr.py`, 2.5 minutes; output in `runs/rfr/rfr-run1.txt`.

```
P1: not killed. geometric mean over uniform directions vs exp(a0): rel 5.89e-40; depth change under k = 1e-3, 7, 1e6: 1.47e-39 levels; rbar/(k*rbar0) - 1: 4.13e-40.
  Earth:   L 0.00482602; median at mu 0.5; median sphere above the geometric-mean sphere by 0.000401291 levels; dL/L 0.0831516
  Mars:    L 0.00852105; median at mu 0.5; 0.000707347 levels; dL/L 0.0830117
  Moon:    L 0.00174414; median at mu 0.5; 0.000145231 levels; dL/L 0.0832678
  Jupiter: L 0.0967679;  median at mu 0.5; 0.00769081 levels;  dL/L 0.0794768
  Saturn:  L 0.148741;   median at mu 0.5; 0.0114862 levels;   dL/L 0.0772227
P2: KILLED (every body outside its band)
  footprint/(a eps) - 1: 3.3e-13, 3.9e-13, 1.0e-12, 2.2e-11, 1.7e-7 at a/R 1e-3, 0.1, 1, 10, 1e3
  disc rule: -0.551328895422 octaves per level of altitude at a = R (-sqrt3/pi); -0.99900 at a = 1000R; l_disc/l* = pi/6 at a = R
  a/R 1e-3, 1e-2, 0.1, 1, 10, 100: l_disc/l* 0.0015, 0.014, 0.114, 0.524, 0.910, 0.990; disc octaves per level of altitude
    -0.0146, -0.0488, -0.174, -0.551, -0.912, -0.990; per level of distance d -14.6, -4.93, -1.91, -1.10, -1.003, -1.00003
P3: not killed
  (a) 0.0; (b) exterior Poisson coefficients vs (R/d)^n: 0.667; (c) 1024 = 2K, 10.0 octaves
  world's own Cauchy, octaves per level of altitude: a/R 1e-4 0.99993, 1e-2 0.99288, 0.05 0.96604, 0.1 0.93578, 0.25 0.86161,
    1 0.66445, 10 0.34445, 100 0.20052, 1e4 0.10467
P4: KILLED (by (b))
P5: KILLED. worst |shift/rho - 1| 0.0025
  bookkeeping: run 2's printed rho = 2 RMS/lambda for 55 octaves, worst difference 0.00007 (printed to 0.0001)
```

- **P1 not killed.** The corner sphere is exp(a₀) to 6·10⁻⁴⁰; scaling the world moves no depth (10⁻³⁹) and multiplies r̄
  by k. REF's depth is a reading (the shape, every degree ≥ 1); r̄ in km and heights above it are writings.
- **P2 killed by my set-up.** The plan's bands were meant for ΔL against its own first-order value L/12 (the sentence
  gives "first order ΔL = L/12"), but were written against ΔL/L, which is about 1/12 by that same sentence; every body
  fails the letter. Read as intended (ΔL/(L/12), computed from the printed numbers after the run): Earth 0.9978, Mars
  0.9961, Moon 0.9992, Jupiter 0.9537, Saturn 0.9267, inside the intended bands; but that reading was made after seeing
  the numbers and is not a test. The part not touched by the slip stands: on every spheroid the median radius is at
  μ = ½ (latitude 30°, the area-halving height, whatever a and c), and the geometric-mean "corner" sphere lies below it.
  Saturn 0.0115 levels, Earth 0.0004. The arithmetic mean is above the geometric by second order only (Earth 7·10⁻⁷
  levels, Saturn 7·10⁻⁴), so REF's choice of mean does not matter for worlds; median against mean does, at L/12.
- **P3 not killed.** At the foot one address covers a·ε of surface to 10⁻¹² for a/R up to 10 (1.7·10⁻⁷ at 10³, ε's own
  second order): the held degree l* = πR/(aε) doubles exactly per halving of the altitude, with no corner at a = R. Run 2's
  disc rule is the far-field form: at a = R it holds π/6 of the foot's degree and drops only √3/π = 0.551 octaves per level
  of altitude (exactly); near the surface it drops almost nothing per level of altitude (it saturates at α = 90°) while
  the foot keeps dropping one; per level of the distance d it drops more than one near the body (1.10 at a = R, 14.6 at
  a = 10⁻³R) and one only far off (1.003 at a = 10R).
- **P4 killed by my code.** (b) compared 2·∫P(φ)cos nφ dφ with (R/d)ⁿ; for a density normalised to 1 the coefficient is
  ∫P cos nφ dφ, without the 2, so the worst miss is (R/d)¹ at d = 1.5R, 0.667, exactly the factor. (a) and (c) pass as
  predicted, and the values computed from the closed form pass every bound: 0.9358 at a/R = 0.1, 0.66445 = log₂ log₂ 3 at
  a = R, 0.2005 at a = 100R (under 0.25), 0.105 at 10⁴R. Run 2 repeats (b) corrected.
- **P5 killed.** The worst miss, 0.0025, is at d = 1.01R with h/R = 10⁻⁴: the limb's tangent distance there is ℓ = 0.142R,
  and the shift's next term, h·R/(2ℓ²) relative, is 0.0025. My threshold forgot the second order in h/ℓ. Post hoc: in the
  ratio shift/ρ = Δα·ℓ/h, ε (so K) and the octave k cancel identically, and d enters only through that second-order term.
  Run 2 tests it.

### Run 2 (predictions written 22 October, after run 1, before `runs/rfr/rfr2.py` was written or run)

- **P4′(b).** The exterior Poisson kernel's coefficients ∫P(φ)·cos nφ dφ equal (R/d)ⁿ to 10⁻²⁰ for n = 1 … 8,
  d/R = 1.5, 3, 10. *Killed* if any misses.
- **P5′.** (a) shift/ρ is the same for k = 3 … 9 and for K = 64, 512, 4096 (ε set by K, not by the octave) to 10⁻³⁰ at
  each (d, h). (b) (shift/ρ − 1)/(h·R/(2ℓ²)) lies within 0.01 of 1 for d/R = 1.01, √2, 2, 10, 1000 and h/R = 10⁻⁵, 10⁻⁴.
  *Killed* if either fails.

### Run 2 (22 October 2026)

`python3 runs/rfr/rfr2.py`, seconds; output in `runs/rfr/rfr-run2.txt`.

```
P4'(b): not killed. worst |coefficient - (R/d)^n| 5.74e-42
  shift/rho - 1 over hR/(2 ell^2): 1.0005, 1.00504 (d = 1.01R, h/R 1e-5, 1e-4); 1.00001-1.00013 (sqrt2 R); 1.00001-1.00007 (2R);
  1.0-1.00003 (10R, 1000R); shift/rho - 1 from 0.0025 (1.01R, 1e-4) down to 5e-12 (1000R, 1e-5)
P5': not killed. (a) spread over k and K 0.0; (b) worst |ratio to hR/(2 ell^2) - 1| 0.00504
```

- **P4′(b) not killed.** The world's own Cauchy from distance d keeps degree n as (R/d)ⁿ = e^(−n·ln(d/R)).
- **P5′ not killed, (a) by construction.** As written, the script computes shift/ρ as Δα·ℓ/h, in which k and K are
  already cancelled by hand, so (a)'s zero spread is the algebra, not a computation (stated here; the cancellation itself
  is exact: ε = πR/(2^(k+1)ℓ) and ρ ∝ 2^(k+1) meet in the quotient). (b) holds: shift/ρ = 1 + h·R/(2ℓ²) + …, within 0.5%
  of that term even at d = 1.01R with h/R = 10⁻⁴.

## Reading (after the runs; not ruled)

- **REF re-sorted.** (i) Depth log₂(r/r̄) is a reading of the shape (degrees ≥ 1, a ratio of amounts in one unread unit,
  unmoved by k: P1); the sphere r̄ is exp(a₀), never read, and r̄ in km or heights in metres are writings. So "within a
  hundredth of a level of its corner" (REF P4, P5) is a statement about shape, true at every size. (ii) The "corner" REF
  measures from is a **mean** of log-amounts, the payload reader's, not a median: on a spheroid the median sphere sits at
  latitude 30° for every flattening and above the mean one by about L/12 (run 1, P2 kept to what its slip leaves). (iii)
  Relief per octave, and its slopes, are the payload's (the world's shares, R231); ρ_k = 2·RMS_k/λ_k is exactly a
  ratio of the world's relief to its wavelength, the same at every K and, to first order in h/ℓ, at every distance
  (run 2): REF's "0.0002 to 0.07 of an address" is the world's roughness, not a fact about the reader. (iv) "One octave per
  level" is K's level of detail, but exactly only at the foot, per level of the altitude (l* = πR/(aε), P3), through
  a = R with no corner. Run 2's disc rule (l = πa/2 over the orthographic disc) is its far-field form, π/6 of it at
  a = R and √3/π octaves per level of altitude there.
- **The Cauchy's height cut.** On the plane under the reader the built-in LOD e^(−κa) drops exactly one octave per level of
  altitude, a fixed log₂(2K) octaves coarser than the K addresses' cut (10 at K = 512). The world's own Cauchy keeps
  (R/d)ⁿ and drops one octave per level only while a ≪ R (0.936 at a = 0.1R, log₂ log₂ 3 = 0.664 at a = R, 0.20 at 100R):
  from far off it is the multipole cut (OFS §8, "From far off"), not the reader's address cut, and the two must not be
  run together.
