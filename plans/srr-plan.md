# SRR: special relativity and motion, revisited (addresses and payload; readings and writings; which corner)

*22 October 2026. A re-reading of MOT run 3 (`plans/mot-plan.md`) and EMC (`plans/emc-plan.md`) in the light of OFS §7.8
"Special relativity's sky" (SPN R395, SRA) and OFS Theorem 6(e): an arrival is an address (a direction, laid by a
uniform turn) times a payload; a corner (v = h of a named pair) is a median only under a reciprocal-symmetric law, and
otherwise a stationary point or a regime hand-over. Predictions written before `runs/srr/srr.py` exists. Exact at 50
digits (mpmath) where the claim is an identity; seeded sampling (numpy, seed 22) where it is an estimate.*

## Known beforehand

- **MOT run 3** (P13–P18, not killed): v = β, h = 1/γ with c the bridge, celerity w = γβ = v/h; the Doppler factor
  k = √((1 + β)/(1 − β)), rapidity η = ln k; three pairs and their "corners": rest (k ↔ 1/k), β = 1/√2 (w ↔ 1/w), the
  transverse plane (t = tan(θ/2) ↔ 1/t); γ even and γβ odd in ln k; pseudorapidity −ln tan(θ/2) panned by ln k under a
  boost; E's level-slope β², ½ at w = 1; uniform proper acceleration one level of k per ln 2/a of proper time.
- **EMC** (P1–P4, not killed): E² = (pc)² + (mc²)² divided by E is the unit circle (v, h) = (β, 1/γ); E = mc² home, E = pc
  the horizon; e_N(x) = e_U(1/x), both 6.07% high at pc = mc²; mc² the level-midpoint of the light-cone pair, unmoved by
  boosts.
- **SRA** (A1″–A5″, not killed): aberration is z ↦ z/k on the stereographic chart, a Möbius map of addresses with no
  frequency in it; a sky uniform in its sources' frame is seen as the spherical Cauchy, ρ = tanh(η/2), density D²/4π
  (wrapped Cauchy in 2 + 1); D = √(1 − β²)/(1 − β cos θ′) is the payload's weighting; beaming D⁴ = D² × D².
- **Textbook SR.** cos θ′ = (cos θ + β)/(1 + β cos θ); D = γ(1 + β cos θ) in the source's own angle; a source at 90° in
  its own frame is seen at cos θ′ = β; the D = 1 cone; for an isotropic emitter dN/dη_p = ½ sech²(η_p) (high-energy
  physics' pseudorapidity of an isotropic distribution); the Gudermannian gd links rapidity and the turn ruler
  (OFS §6: β = tanh η = sin χ, χ = gd η).
- **OFS §7.8** says uniform acceleration's corner γβ = 1 is a hand-over, not a median, since acceleration is uniform in
  η, not χ.

## The reading to test

MOT run 3 named three "corners" without saying which kind each is. Sorted by OFS:
- **The sky's pair (fore, aft)** is the only one of the three on the *addresses*. Its corner (the transverse plane) should
  be a **median** of a reciprocal-symmetric law, but only for a sky uniform in the frame doing the counting; the boost
  moves the seen median to pseudorapidity η exactly, and that is a **reading** (directions alone: no c, no clock, no rest
  frequency).
- **The turn ruler χ** of OFS §6 is itself an address angle: the seen sky's median is turned forward from the transverse
  plane by χ. So "uniform in χ" would be the seen median turning uniformly; acceleration turns it by gd(aτ).
- **The Doppler pair (sent, received)** is on the *payload*: D is a function on the addresses, k its value straight
  ahead. Its corner (rest, D = 1) is the **fixed point of a swap of who counts**: counted by sources (uniform in their
  frame) D is uniform on [1/k, k]; counted by the observer's own uniform turn of addresses 1/D is. Neither median is 1;
  their geometric mean is.
- **(β, 1/γ) and EMC's (pc, mc²)** are amounts with c the bridge (a **writing** to get β from a speed; or a reading from
  k, which needs a clock's two intervals). Their corner is a **regime hand-over** (E's level-slope ½; Newton and the
  massless form equally wrong), and a median only under uniform χ; EMC's mass is a **stationary point** (E's minimum over
  boosts), not a median.

## Predictions

Notation: ξ = −ln tan(θ/2) the pseudorapidity of a direction (θ from the motion), primed in the observer's frame; η the
boost's rapidity; ρ = tanh(η/2); β ∈ {0.1, 0.6, 1/√2, 0.99} unless stated.

- **P1. The sky's corner is a median only in the frame where the sky is uniform.** Push a sky uniform in its sources'
  frame through the aberration formula (not through the pan) and integrate by quadrature at 50 digits.
  - Source frame: the law of ξ is ½ sech²(ξ), so F(t) + F(1/t) = 1 for t = tan(θ/2) (reciprocal-symmetric), median and
    mean at the transverse plane.
  - Observer frame: the law of ξ′ is ½ sech²(ξ′ − η): median and mean exactly η, the boost's rapidity; the share seen
    ahead of the transverse plane is (1 + β)/2, not ½.
  - In 2 + 1 (sources uniform on a circle): ξ′ has density (1/π)·sech(ξ′ − η).
  - **Killed if** any density or CDF misses its closed form by more than 1e-40 on a grid of 41 ξ′ in [−6, 6], or the
    median (root-found) misses η by more than 1e-40.
- **P2. χ is the aberration of the seen median.** With β = sin χ:
  - the seen median direction (the cap holding half of a uniform sky) has half-angle exactly θ′ = π/2 − χ, so at the
    (β, 1/γ) corner (w = 1) it is 45°, and χ = gd(η);
  - under uniform proper acceleration from rest to rapidity Z, the share of proper time spent below w = 1 is
    asinh(1)/Z, ½ only at Z = 2·asinh 1 = 1.762747…; under χ uniform on [0, π/2] the share below w = 1 is ½ for every
    range symmetric in χ about 45°, i.e. w = 1 is the median of the half-Cauchy law of w (reciprocal-symmetric).
  - **Killed if** the root-found median cap misses π/2 − arcsin β by more than 1e-40, or either share misses its closed
    form by more than 1e-40.
- **P3. The Doppler factor is a payload function on the addresses, and the Doppler pair's swap is a reflection of the
  pseudorapidity axis.** From D = √(1 − β²)/(1 − β cos θ′) at 41 ξ′ in [−6, 6]:
  - D = cosh ξ′ / cosh(ξ′ − η);
  - D(ξ′)·D(η − ξ′) = 1, so k ↔ 1/k is ξ′ ↔ η − ξ′, and D → k ahead (ξ′ → +∞), 1/k behind;
  - D = 1 exactly at ξ′ = η/2, i.e. cos θ′ = ρ = tanh(η/2) (the spherical Cauchy's own parameter);
  - the seen density in ξ′ is D² × ½ sech²(ξ′) (SRA's D² rewritten on the levels).
  - **Killed if** any misses by more than 1e-40 on the grid, or |D(ξ′ = 60) − k|/k or |D(ξ′ = −60) − 1/k|·k exceeds
    1e-40 (the remainder there is of order e^{−120}).
- **P4. The Doppler pair's corner (rest) is the swap of who counts, not a median.** Over a sky uniform in its sources'
  frame:
  - counted by source, D is uniform on [1/k, k]: median and mean γ; the share blueshifted k/(1 + k);
  - counted by the observer's uniform turn of addresses (each seen direction alike), 1/D is uniform on [1/k, k]: median
    1/γ, the share of addresses blueshifted 1/(1 + k);
  - the two medians' geometric mean is exactly 1 (rest), and the two blue shares' ratio is k.
  - **Killed if** the quadrature CDFs miss the uniform laws by more than 1e-40 at 21 points, or any median or share by
    more than 1e-40; or, in a seeded sample of 10⁶ sources and 10⁶ observer addresses per β, any sample median or share
    is more than 5 standard errors from its prediction.
- **P5. The boost is read from addresses alone, and the levels' law has a mean.** A reader holding only the directions
  of N = 2,000 sources (uniform in their frame, seeded), no clock, no c, no rest frequency, estimates η by the median and
  by the mean of ξ′. Over 400 trials at each β:
  - the RMS error of the median is 1/√N = 0.02236 and of the mean (π/(2√3))/√N = 0.02028 (the logistic's), each within
    15%; their ratio within [1.0, 1.2] (predicted √(12)/π = 1.1027);
  - the sources placed at random distances (0.1 to 10 units) and the whole world scaled by 10⁻³ and 10³ before the
    directions are taken changes no estimate by more than 1e-12 (a reading);
  - by contrast the payload needs an amount carried in: a reader taking η from frequencies, as ln(ν′/ν₀) of a source
    seen straight ahead, is right only with the true rest frequency ν₀; with ν₀ wrong by a factor f its estimate moves
    by exactly −ln f, while the address estimate (same sources) does not move at all.
  - **Killed if** an RMS is off by more than 15%, the ratio falls outside [1.0, 1.2], the scaled worlds move an estimate
    by more than 1e-12, or the frequency estimate does not move by −ln f
    to 1e-12 (f = 1.5, 0.8), or the address estimate moves.
- **P6. EMC's mass is a stationary point, and its Newton–massless hand-over is not a median.**
  - E′(η_b) = mc²·cosh(η − η_b) from the Lorentz transformation of (E, pc); dE′/dη_b = 0 only at η_b = η (rest), where
    E′ = mc², the minimum, and E′ is even about it (E′(η + δ) = E′(η − δ));
  - Newton's and the massless form's errors cross only at x = 1, and under a law uniform in rapidity of the particle over
    [0, Z] the share of states where Newton is the better is asinh(1)/Z (½ only at Z = 1.762747…), under χ uniform it is
    ½.
  - **Killed if** any of these misses by more than 1e-40 on 21 seeded (η, η_b, δ) at 50 digits, or the crossing
    root-finds anywhere but x = 1 to 1e-40.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (22 Oct; `runs/srr/srr.py`, output `runs/srr/srr-run1.txt`)

Five seconds. The first attempt stopped in P4 with an error before any verdict was printed: a secant root-finder,
started at 0, diverged at β = 0.99 (my code). The four root-finds in P4 were changed to a bracketed solver on [−1, 1]
(Illinois); nothing else was changed, and the output file is the second attempt's.

- **P1 not killed.** Worst miss 7.8·10⁻⁴⁹. In the sources' frame ξ is ½ sech²(ξ) and F(t) + F(1/t) = 1 (the transverse
  plane the median and the mean). Seen from the boosted frame, ξ′ is ½ sech²(ξ′ − η): median and mean equal η to 50
  digits (0.100335, 0.693147, 0.881374, 2.646652 at β = 0.1, 0.6, 1/√2, 0.99); the share ahead of 90° is (1 + β)/2
  (0.55, 0.8, 0.853553, 0.995). In 2 + 1 the levels' law is (1/π) sech(ξ′ − η).
- **P2 not killed.** Worst miss 2·10⁻⁵¹. The cap holding half of a uniform sky is θ′ = 90° − χ: 84.2608°, 53.1301°,
  45.0000°, 8.1096°; χ = gd η. Uniform in rapidity on [0, Z], the share below w = 1 is asinh(1)/Z (0.5876, 0.4407,
  0.2938 at Z = 1.5, 2, 3), ½ only at Z = 1.762747; uniform in χ it is ½ on every range symmetric about 45°.
- **P3 not killed.** Worst miss 1.1·10⁻⁴⁸. D = cosh ξ′/cosh(ξ′ − η); D(ξ′)·D(η − ξ′) = 1; D = 1 at ξ′ = η/2, cos θ′ = ρ
  (θ′ = 87.13°, 70.53°, 65.53°, 29.82°); D → k ahead, 1/k behind; the seen density is D² × ½ sech²(ξ′).
- **P4 not killed.** Identities to 1.1·10⁻⁴⁹; sampled, worst 1.93 standard errors. By source D is uniform on [1/k, k],
  median γ (1.00504, 1.25, 1.41421, 7.08881); by the observer's uniform turn 1/D is, median of D 1/γ (0.99499, 0.8,
  0.70711, 0.14107); product 1 exactly. Blueshifted: by source k/(1 + k) (0.5251, 0.6667, 0.7071, 0.9338), by address
  1/(1 + k) (0.4749, 0.3333, 0.2929, 0.0662).
- **P5 not killed.** RMS of the median 0.02265, 0.02244, 0.02191, 0.02175 (predicted 0.02236; within 3%); of the mean
  0.02037, 0.02094, 0.01989, 0.02028 (predicted 0.02028; within 3.2%); ratios 1.112, 1.072, 1.101, 1.072 (predicted
  1.103). Scaling the world by 10⁻³ and 10³ moved no estimate by more than 3.9·10⁻¹³ (the renormalised directions' last
  bits). The frequency estimate moved by −ln f to 2·10⁻¹⁶; the address estimate did not move.
- **P6 not killed.** Worst miss 4.1·10⁻⁴⁹. E′(η_b) = mc² cosh(η − η_b), stationary and least (mc²) at rest, even about
  it. Newton's and the massless form's errors cross at x = 1 only (from six starts); the share where Newton is the better
  is asinh(1)/Z under a uniform rapidity, ½ under uniform χ.

A caution on standing: P1–P4 and P6 are identities I could derive before running (the run checks them to 50 digits
and found no slip); none is new physics. All is classical SR (aberration, D = γ(1 + β cos θ), the isotropic
½ sech² in pseudorapidity, the D = 1 cone). What is new is the sorting.

**Reading.**
- **Of MOT run 3's three corners only the sky's is on the addresses, and only it is a median**, of the
  reciprocal-symmetric law of tan(θ/2) for a sky uniform in the counting frame. In the frame the reader counts from
  after a boost the law is the same, panned: the seen median sits at pseudorapidity η, the boost's own rapidity. So a
  reader holding directions alone (no c, no clock, no rest frequency; unchanged by scaling the world) reads η: a
  **reading**. On the levels ξ the address law (logistic) has a mean, and the mean is the better estimate (ratio
  √12/π); the missing mean belongs to the chart tan(θ/2) in 2 + 1, not to the levels.
- **The turn ruler's χ is an address angle**: the seen median is turned forward from the transverse plane by χ
  (θ′ = 90° − χ, β = sin χ), so the (β, 1/γ) corner w = 1 is the boost at which half the sky is seen within 45°.
  Uniform acceleration turns that median by gd(aτ), not uniformly: w = 1 is a median of time spent only for
  Z = 2 asinh 1. This agrees with OFS §7.8: as a statement about motion the corner is a hand-over (E's level-slope ½,
  Newton and the massless form equally wrong), a median only under uniform χ.
- **The Doppler pair is the payload's**: D is a function on the addresses, cosh ξ′/cosh(ξ′ − η), k its value ahead.
  Its corner, rest (D = 1), is not a median of anything counted: by source the median is γ, by the observer's uniform
  turn 1/γ. It is the fixed point of the swap of who counts (D ↔ 1/D), and on the sky the reflection of the levels
  about η/2, where the no-shift cone lies at cos θ′ = ρ, the spherical Cauchy's parameter. Reading D needs a rest
  frequency carried in (a known kind): a **writing**, moved by exactly −ln f when the carried amount is off by f.
- **EMC is all payload** (energies and momenta are amounts, c the bridge). Its corner pc = mc² is a regime hand-over,
  and mass is a stationary point (the least E over boosts), not a median.

### Re-read, 22 October (EBD, `plans/ebd-plan.md`; SPN R440)
Appended; nothing above is changed. "A reading (directions alone)" (P1, P5) holds for a census taken whatever the
brightness, of sources uniform in their own frame. A flux-limited census adds the payload weighting D^(x(1+α)), read from the
catalogue's own count slope and band ratio: still a reading (no rest frequency), but not of directions alone. On CatWISE
that weighting is two thirds of the expected dipole.
