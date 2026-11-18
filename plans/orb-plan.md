# ORB: an oscillator and an orbit from one standpoint

18 Nov 2026. SPN R1103. Tom: "Merge  1 2", to: test physics' own equations as RIC tested the slope's (the oscillator's
direction exact, its size a write; Kepler's orbit's shape rational, its clock the completion), then carry CLC and RIC
into *Reads and Writes* §1.

## The question

RIC found the slope's own equation stepped exactly in fractions, the clock time the completion. Do two classical
equations of physics split the same way?

1. **The oscillator** x″ + 2γx′ + ω²x = 0, γ and ω² rational, underdamped (γ² < ω²). Its direction s = x′/x obeys the
   Riccati equation s′ = −ω² − 2γs − s², constant coefficients, so by RIC it steps exactly by rational Möbius maps. The
   whole state (x, x′) flows by exp(tA), A = [[0, 1], [−ω², −2γ]], and exp(τA) = λ·P_u with P_u = I + u(A + γI), rational
   for rational u, and the scalar λ = e^(−γτ)/√(1 + u²Ω²), Ω² = ω² − γ², τ = arctan(uΩ)/Ω. The direction is P_u's alone;
   the size carries λ. Undamped, λ² = 1/(1 + u²ω²) is rational (energy kept, a square root at most); damped, λ carries
   e^(−γτ), a completion.
2. **The orbit.** Against the angle φ, u = 1/r obeys u″ + u = 1/ℓ, linear with constant coefficients, and
   r = ℓ/(1 + e·cos φ). In the half-slope t = tan(φ/2) the point is rational in t: x = r(1 − t²)/(1 + t²),
   y = r·2t/(1 + t²), r = ℓ(1 + t²)/((1 + e) + (1 − e)t²). The time to reach it is the mean anomaly
   M = E − e·sin E, tan(E/2) = √((1 − e)/(1 + e))·t: Kepler's equation, transcendental, inverted only by iteration.

## Set-up

`fractions` for the exact parts, mpmath at 50 digits, seeded (`random.seed(1103)`).

## Predictions (committed before any run)

- **O1.** For 50 seeded oscillators (γ in {0, 1/10, …, 1/2}, ω² rational with ω² > γ² + 1/10, u = 1/(k + 4), k in 0–6,
  start (x₀, x₀′) rational), the direction x′/x after n = 6 steps of P_u, in fractions, equals the flow exp(6τA)'s to
  10⁻⁴⁰ in 50 of 50 (cases crossing x = 0 included: the direction is kept as the pair).
- **O2.** The state after six steps of P_u times λ⁶ equals exp(6τA)·(x₀, x₀′) to 10⁻⁴⁰ in 50 of 50.
- **O3.** Undamped (γ = 0), λ² = 1/(1 + u²ω²) exactly (as a fraction, checked against e.g. the energy ratio of one step),
  in every undamped case. Damped (γ > 0), PSLQ finds no integer relation among [λ², 1] of height ≤ 10⁴ in every damped case.
- **K1.** For 500 seeded orbits and points (ℓ rational in [1, 5], e rational in (0, 1), t rational), the point (x, y)
  is a pair of fractions and satisfies x² + y² = (ℓ − e·x)² exactly: 500 of 500.
- **K2.** n = 20 steps of a fixed rational half-slope a composed by tangent addition land on the point at
  φ = 20·2·arctan(a) to 10⁻⁴⁰ in 50 of 50 (the angle a completion, the composed half-slope a fraction).
- **K3.** For 50 seeded (e, t) with t ≠ 0, PSLQ finds no integer relation among [M, 1, π] of height ≤ 10⁴ in 50 of 50:
  the time to a rational point is not a simple number.
- **K4.** Newton's method on Kepler's equation for M = 1/2 from E₀ = M (e < 0.8) or E₀ = π (e ≥ 0.8) reaches 10⁻⁴⁰ in
  4 to 12 iterations for e in {0.1, 0.5, 0.9}: the clock's inverse takes a count, the shape none.

## What could fail, and what could not

O1, O2, K1, K2 are identities and fail only by my code. O3's undamped clause is an identity; its damped clause and K3
can fail by a small integer relation turning up (a pass only says none of small height). K4 can fail by the count.

## Runs

**Run 1** (`runs/orb/orb.py`, output `runs/orb/orb-run1.txt`). Nothing killed.

- O1: the direction after six rational steps equals the flow's, kept as a pair (their cross product under 10⁻⁴⁰), 50 of 50.
- O2: λ⁶ times the rational state equals the flow's state to 10⁻⁴⁰, 50 of 50.
- O3: undamped, λ² = 1/(1 + u²ω²) exactly, the one-step energy ratio, 5 of 5; damped, no relation [λ², 1] of height
  ≤ 10⁴, 45 of 45.
- K1: rational points on the orbit's conic exactly, 500 of 500. K2: twenty composed half-slopes land on the angle
  40·arctan(a) to 10⁻⁴⁰, 50 of 50. K3: no relation [M, 1, π] of height ≤ 10⁴ for the time to a rational point, 50 of 50.
- K4: Newton on Kepler's equation at M = ½ reaches 10⁻⁴⁰ in 4, 6 and 7 iterations at e = 0.1, 0.5, 0.9.

**What it shows.** The oscillator's direction steps exactly by rational maps; its size carries λ, a square root when
undamped (energy kept) and e^(−γτ) when damped, a completion. The orbit's shape is rational in the half-slope of the
angle; the time to reach a point is Kepler's, with no small relation, and its inverse takes an iteration count. In both,
as in RIC, the steps are the read's, the clock and the decay the completion. Classical (the oscillator's matrix
exponential, the conic in the half-angle, Kepler 1609, Newton's method); the sorting ours.
