# TIM: how a Cauchy keeps time

*18 October 2026 (Tom's local date). Tom asked: "How does cauchy handle time." Claude answered in three parts.*
- *Time turns z. A Cauchy's characteristic function e^{imt − γ|t|} is a phasor e^{izt}, z = m + iγ: it turns at its foot
  m and fades at its height γ.*
- *Running time raises the standpoint. The Cauchy process at time t is C(0, t).*
- *The clock is hidden. In Spitzer's construction the Cauchy's time is the depth descended, and the Brownian clock under
  it has no mean.*

*Claude's reading: the Cauchy process is self-similar with index 1, so the constant joining time to place is a speed.
Order is free, as addresses; a duration is an amount; the bridge between them is a speed. Claude offered a prediction-first
plan, and Tom said "Yes". Exact mathematics (mpmath) and seeded samples, with thresholds in standard errors from the start
(SUM run 1's lesson). One prediction is on real data.*

## Known beforehand

**Classical.**
- **The Fourier pair.** The Lorentzian of centre m and half-width γ is the Fourier pair of e^{imt − γ|t|}. A damped
  oscillation e^{(im − γ)t} for t ≥ 0 has the power spectrum 1/((ω − m)² + γ²), the same Lorentzian.
- **The Cauchy process.** It is Lévy's stable process of index 1: X(t) ~ C(0, vt), with stationary independent increments.
  It is self-similar: X(ct) has the law of c·X(t).
- **Spitzer (1958).** A planar Brownian motion started at height h lands on the line at C(0, h). Watched at its first
  passage to each lower level, its place is the Cauchy process in the depth descended.
- **The hidden clock's law.**
  - Per coordinate, the motion's variance is 2D·t. The first-passage time from height h is h²/(2D·Z²), with Z standard
    normal: Lévy's law, index ½, with no mean.
  - The sum of M such times has the law of M² times one of them, so the mean of M has the law of M times one.
  - The landing place is h·N/|Z|, with N standard normal independent of Z, whatever D is.
- **Weisskopf and Wigner (1930).** A decaying state's natural line is a Lorentzian whose angular half-width at half
  maximum Γ/2 and lifetime τ satisfy Γ·τ = 1.

**In the corpus and in draw.**
- **SUM run 2:** heights add along a relay.
- **ADR run 1:**
  - from height γ, mode k is kept as e^{−kγ} (A4);
  - along a relay the error grows as n, and averaging gains nothing (A5).
- **MOT:** the time to contact x/ẋ is a ratio read free; the clock is the only amount.
- **R327:** a sweep is counted from its zero by the share passed. Stopping makes the next zero.
- **draw's REC lab** (`labs.html`, rerun at draw `ea07709`). A serial record keeps order only, with no timestamps. It is
  unchanged character for character when the whole history is rescaled. Two readers of different grain recover the ratio
  of their grains by counting each other's ticks between marks they both kept, with no unit exchanged.

  So the claim that order is free and survives any rescaling is known for records. What is new here is that claim for the
  Cauchy's own time parameter, and the bridge as a speed.

## The reading, before the run

The Cauchy's time parameter is the standpoint's height: what turns z, and what raises it. A reading taken in that parameter
is a direction, kept by its order. A duration on a clock is an amount. They are joined only through a speed v = γ/t, the
height gained per unit of clock. So:
- Rescaling the clock, or the world, moves no reading of order and no ratio of two durations.
- Rescaling the clock moves every duration by its factor.
- A product of a rate and a duration is unitless and free.
- The hidden clock under Spitzer's construction can be sped up or slowed down without moving a single landing.

### Predictions

- **T1 (time turns z).** For z = 0.7 + 0.3i, at 100 digits:
  - (a) the Fourier transform of C(0.7, 0.3) is e^{0.7it − 0.3|t|} at t ∈ {0.1, 1, 5, −2};
  - (b) the damped phasor e^{izt} on t ≥ 0 has the power spectrum 1/((ω − m)² + γ²), which is (π/γ)·C(m, γ)(ω), at
    ω ∈ {−1, 0, 0.7, 2}, by direct quadrature of its transform.
  - Both are oscillatory integrals, (a) with a slow tail (HZT run 1's trouble), so the tolerance is set at 10⁻⁴⁰.
  - *Killed* if either differs by more than 10⁻⁴⁰.
- **T2 (time raises the standpoint).** A Cauchy process of unit rate, built from independent C(0, Δt) increments (seeded,
  10⁵ paths).
  - (a) At t = 1, 4, 16, its quartiles are within 3 standard errors of ±t.
  - (b) Self-similarity: X(16)/4 and X(4) pass a two-sample KS test, distance below 1.63·√(2/N).
  - (c) Independent increments: the rank correlation of X(4) − X(1) with X(1) is within 3/√N of 0.
  - *Killed* if any fails.
- **T3 (order and ratios are free; durations are amounts).** On the paths of T2, rescale the clock by c ∈ {10⁻³, 7, 10³}
  (time t → ct, rate v → v/c, so X at clock time ct is unchanged) and the world by k ∈ {10⁻³, 7, 10³} (X → kX).
  - (a) The order of every path's values at its sample points is unchanged in every case, exactly.
  - (b) The read of the spread's growth, the ratio half-IQR(X(16))/half-IQR(X(4)), is unchanged to rounding, 10⁻¹².
  - (c) The read of the rate v̂ = half-IQR(X(t))/t moves by exactly k/c, to 10⁻¹².
  - (d) The product v̂·T, for a clock duration T, moves by k alone: the clock cancels, to 10⁻¹².
  - *Killed* if any fails. These are near-identities; a kill would be my code.
- **T4 (the hidden clock).** Spitzer's landing from height h = 1, by the exact construction (time h²/(2D·Z²), place
  h·N/|Z|). D ∈ {0.1, 1, 10}, 10⁵ draws each, independent seeds for each D.
  - (a) The landing's quartiles are within 3 standard errors of ±1 at every D.
  - (b) The landings at D = 0.1 and D = 10 pass a two-sample KS test, distance below 1.63·√(2/N).
  - (c) The median passage time is h²/(2D·q), with q = 0.45494 the median of Z², within 3 standard errors from the exact
    density, at every D. So the clock's durations move by 1/D and no landing moves.
  - (d) No mean: for batches of M = 10, 100, 1000 times at D = 1 (1000 batches each), the median of the batch mean is
    M·h²/(2q) within 3 standard errors. It grows in proportion to M, where a quantity with a mean would settle.
  - *Killed* if any fails.
- **T5 (a rate times a duration is free: real data).** Natural lines: the lifetime τ measured in time and the natural
  width Γ measured in frequency, independently, for the same transition.
  - Prediction: Γ·τ = 1 (angular width at full width at half maximum) within 3 combined standard errors, for every pair
    found.
  - The run will search the literature for such pairs, after this plan is committed. It records each source, how each
    number was measured, and the sha256 of any file read.
  - A width computed from the lifetime, as data compilations often give, is not independent and does not count.
  - *Untested*, and I say so, if no independent pair can be read here.
  - *Killed* if a pair falls outside 3 standard errors.
  - The test is classical (Weisskopf–Wigner). The bridge is the clock, which cancels from the product. What the reading
    adds is that the product is one height read in two units, so it is free, while each factor alone is an amount.
- **T6 (the verdict).** A judgment. In every case above:
  - the order and the ratios are free;
  - the durations move with the clock;
  - the only constant joining place to time is a speed.

  *Killed* if T2–T4 show an order reading moved by the clock, or a duration that did not move.

T1–T4 are classical, so a kill there would be my set-up. T5 is real data on a classical law. T6 is the reading.

## What would and would not be shown

**Shown:** that in the Cauchy the order is the address's and the duration is an amount, joined by a speed, as ranging was
joined by the signal's speed (CFH, WRD).

**Not shown:**
- whether readers keep time this way;
- anything about relativity or the arrow of time;
- that every clock is a Cauchy's.

## Runs

(Nothing above this line is edited after a run.)
