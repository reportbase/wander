# RWX: reads, writes and exchanges in physical situations

14 November 2026. Tom: "read/write might be a nice reframe for other physical situations.", then "yes, write the plan
and run the test."

## The question

ISX found the inverse square to be the far chart of one share, 1/(1 + s²), whose exchange s ↔ 1/s pairs near with far.
Do other classical situations sort the same way: a read (a ratio, unmoved by scaling), an exchange with a corner, and a
write that appears only when an amount is carried in? Every formula below is textbook; what is tested is the sorting.

Known beforehand: MOT run 2 (`plans/mot-plan.md`) found two kinds of corner in motion, stationary (swapping the pair
leaves a quantity unchanged) and a change of regime; it had the elastic collision's equal-mass corner. The RC
crossover, impedance matching, Fresnel's normal incidence, the series RLC power factor, the pendulum and Kepler's third
law are classical. Each quantity is computed from its physics (impedances, conservation laws, boundary conditions,
integration), not from the share's formula, so the identities below can fail.

## Cases

- **C1** An RC divider: |H|² of the low-pass (across C) and of the high-pass (across R), from complex impedances.
- **C2** A series RLC driven at ω: the power absorbed over its peak, from the impedance.
- **C3** A 1D elastic collision, m₁ onto m₂ at rest: the share of energy passed, from momentum and energy.
- **C4** A source of resistance R_s into a load R_L: power over the matched power, from the circuit.
- **C5** Light at normal incidence from n₁ into n₂: T and R from the boundary conditions (field continuity).
- **C6** A pendulum of length ℓ, amplitude θ₀, under g: the period, by integrating the equation of motion.
- **C7** A Kepler orbit, semi-major axis a, eccentricity e, under GM: the period, by integrating the orbit.

## Predictions (committed before any run)

Exact (fractions or mpmath at 50 digits) unless stated; C6, C7 by numerical integration at rtol 10⁻¹².

- **R1 (the turn's family)** C1: |H_low|² = 1/(1 + s²), |H_high|² = s²/(1 + s²), s = ωRC; their sum 1; s ↔ 1/s swaps
  them (a complement); they cross at s = 1, ½ each (a crossover corner); the low-pass share is cos²φ with φ the phase,
  tan φ = s (the turn named, R719). Kill: any.
- **R2 (the level's family)** C3, C4, C5 each give the share 4k/(1 + k)² = sech²(½ ln k), k the ratio of the pair (m₁/m₂,
  R_L/R_s, n₂/n₁), unchanged by k ↔ 1/k, 1 at k = 1 with zero slope in ln k (a stationary corner); C5's R = tanh²(½ ln k),
  R + T = 1. Kill: any case off this function past 10⁻⁴⁰.
- **R3 (one share, two charts)** The level's share is the turn's share on another chart: sech²(½ ln k) = 1/(1 + s²) with
  s = sinh(½ ln k) = (√k − 1/√k)/2, on which k ↔ 1/k is s ↔ −s (unchanged), while on C1's chart it is s ↔ 1/s
  (complement). C2 is also on a sinh chart: P/P_max = 1/(1 + s²), s = Q·(ω/ω₀ − ω₀/ω) = 2Q·sinh(ln(ω/ω₀)), unchanged by
  ω ↔ ω₀²/ω, half power at s = ±1, tan φ = s. So the crossover and the stationary corner are one share read on two
  charts (the ratio and the sinh of the level). Kill: any identity off past 10⁻⁴⁰.
- **R4 (reads unmoved)** Scaling every amount of a kind by k (R and C → kR, C/k; both masses; both resistances; both
  indices; L, C, R with ω₀ and Q kept) leaves every share. Kill: any.
- **R5 (the bounce's move)** C6: T·√(g/ℓ) depends on θ₀ alone (the read), the same at ℓ = 1, 7, 100 to 10⁻⁹; with g
  carried in a counted period writes ℓ = g·(T/T̂(θ₀))². C7: T·√(GM/a³) = 2π at e = 0, 0.5, 0.9 and a = 1, 10, 1000 to
  10⁻⁸; e and every angle unmoved by a → ka; with GM carried in a counted period writes a. Kill: any departure.
- **R6 (the sorting)** Every case falls in one of three types: a turn's share with a crossover (C1), a level's share with
  a stationary corner (C2–C5), a count that writes a size with one amount carried in (C6, C7); and the first two are one
  share (R3). Kill: a case that needs a fourth type.

## Runs

(appended below as they come out; nothing above this line edited afterwards)

### Run 1 (14 Nov 2026; `runs/rwx/rwx.py`, output `runs/rwx/rwx-run1.txt`): nothing killed

- R1 not killed: the RC divider from its impedances gives 1/(1 + s²) and s²/(1 + s²), sum 1, swapped by s ↔ 1/s,
  ½ each at s = 1; the low-pass share cos²φ with tan φ = s (worst 9·10⁻⁴⁷).
- R2 not killed: the collision (momentum and energy checked), the matched load and Fresnel at normal incidence (from
  field continuity) each give exactly 4k/(1 + k)² in fractions at eight ratios, the same at k and 1/k (for Fresnel, light
  going in and coming out), = sech²(½ ln k), R = tanh²(½ ln k), R + T = 1, 1 at k = 1 with zero slope.
- R3 not killed: sech²(½ ln k) = 1/(1 + s²) on s = (√k − 1/√k)/2; the series RLC's P/P_max = 1/(1 + s²) on
  s = 2Q·sinh(ln(ω/ω₀)), unchanged by ω ↔ ω₀²/ω, tan φ = s, half power at s = ±1 (worst 2·10⁻⁴⁵).
- R4 not killed: every share unmoved when the pair is scaled together.
- R5 not killed: T·√(g/ℓ) the same at ℓ = 1, 7, 100 (6.2871145493, 6.6999756644, 10.3231628659 at θ₀ = 0.1, 1, 2.5,
  Legendre's 2π/AGM(1, cos(θ₀/2)) each); with g carried in a counted period writes ℓ = 7 to 10⁻⁸. Kepler:
  T·√(GM/a³) = 2π to 5·10⁻¹² at e = 0, 0.5, 0.9 and a = 1, 10, 1000; e read back from the orbit to 2·10⁻¹³.
- R6 not killed: every case fell in one of the three types, the first two one share.

Said plainly: R3's identity sech² = 1/(1 + sinh²) is algebra and could not fail; what could was that each physical case,
computed from its own physics, lands on it, which all did. R6 is a sorting I made, not a blind one; a case chosen by
someone else could need a fourth type. Post hoc, what the two charts say: the same share 1/(1 + s²) is a crossover
(near against far, low against high) when its chart is the ratio itself, where the exchange is s ↔ 1/s and turns one
share into its complement; it is a stationary best point (matching, equal masses, the same index, resonance) when its
chart is the sinh of the level, where the exchange is s ↔ −s and leaves the share unchanged. Which chart a situation
uses is set by whether its pair is read directly (ωRC, d/a) or through the ratio's level (½ ln k, ln(ω/ω₀)).
