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
exponential, the conic in the half-angle, Kepler 1609, Newton's method; Newton's *Principia* Book I, Lemma XXVIII, no oval's cut-off area given by a finite
equation, the classical statement of the orbit's split, read in Bruce's translation after the run); the sorting ours.

## Run 2: the orbit as a stage and a payload (predictions committed before the run)

Tom (25 Nov 2026): "We know cauchy very well now. Could we use it to calculate planetary orbits", then, of the timing
the Cauchy does not give, "We would have to create a payload that gives the same results", then "Yes". Claude's check
before this plan (a 2 million draw sample at e = 0.6 and a float identity, not counted as the run): taking the eccentric
anomaly E evenly gives the true anomaly ν a wrapped Cauchy; the time spent per direction over that stage is r/a. The
run states and checks it exactly, at 50 digits (mpmath) and in sympy where it is an identity.

Set-up: a two-body orbit of eccentricity e (0 < e < 1), semi-major axis a, GM; ν the direction from the focus, E the
eccentric anomaly, tan(ν/2) = k·tan(E/2), k = √((1+e)/(1−e)); r = a(1−e²)/(1 + e cos ν); β = (1 − √(1−e²))/e.
Eccentricities e in {0.01, 0.1, 0.3, 0.6, 0.9, 0.99}.

- **P1 (the stage).** E uniform on the turn carries ν to the wrapped Cauchy with ρ = β centred at ν = π (the far
  point): density (1 − β²)/(2π(1 + β² + 2β cos ν)), equal to √(1−e²)/(2π(1 + e cos ν)) as an identity in sympy, and
  the two agree to 10⁻⁴⁵ at 200 values of ν for every e.
- **P2 (the payload).** The clock, time per direction from the areal law dt/dν = r²/h with h = √(GM·a(1−e²)), divided
  by the stage and by the period, is r/a exactly: an identity in sympy, and to 10⁻⁴⁵ at 200 values of ν, every e.
- **P3 (its mean).** The payload's mean over the stage is 1 (⟨r⟩ over E is a), to 10⁻⁴⁵, every e; its mean over the
  clock is 1 + e²/2 (the time-averaged distance a(1 + e²/2)), to 10⁻⁴⁵, every e. The two differ, so the payload is not
  "the time" but what the stage is weighted by.
- **P4 (Kepler's third law).** The period, the clock integrated over the whole turn, is 2π√(a³/GM) to 10⁻⁴⁵ for every e
  and for a in {1, 7, 10³}, GM in {1, 3}: no e enters.
- **P5 (scale).** Scaling a by k = 10³ at fixed GM leaves the stage and the payload r/a unchanged at every ν (to
  10⁻⁴⁵) and multiplies the period by k^(3/2) exactly; the stage needs no amount, the period needs GM and a.
- **P6 (the clock is not on the stage's family).** No wrapped Cauchy equals the clock's law over ν: for e = 0.3, 0.6,
  0.9 the best wrapped Cauchy (ρ and centre chosen to minimise the largest relative difference over 2,000 values of ν)
  still misses by at least 1% somewhere.
- **P7 (Kepler's equation is the payload added up).** Integrating the payload over the stage from the near point,
  ∫₀^E (r/a) dE′ = E − e sin E = M, as an identity in sympy; inverting it needs an iteration (ORB run 1's K4), not
  restated here.

What could fail: P1, P2, P4, P5, P7 are identities and fail only by my code or my algebra (a sign of the centre, a
factor of the period); P3's second clause is a known result recalled from memory and can fail by my recollection; P6
can fail by its 1% (a fitted wrapped Cauchy may come closer than I expect at e = 0.3).

**Run 2** (`runs/orb/orb2.py`, output `runs/orb/orb-run2.txt`). P1 killed by my code; the rest not killed.

- P1 killed in its symbolic clause: sympy proved the wrapped Cauchy with ρ = β centred at π equal to the stage (0),
  but left the push-forward of uniform E, (1/2π)·dE/dν − stage, unsimplified (a sum of square roots it did not combine),
  where the prediction asked for 0. Numerically the three agree at every e to 3·10⁻⁴⁹ or better (10⁻⁵¹ but at
  e = 0.99), under the 10⁻⁴⁵ asked.
- P2: clock/stage − r/a is 0 in sympy, and under 6·10⁻⁵¹ at 200 ν for every e.
- P3: the payload's mean over the stage is 1, its mean over the clock 1 + e²/2 (1.00005, 1.005, 1.045, 1.18, 1.405,
  1.49005), each to 10⁻⁵⁰.
- P4: the period is 2π√(a³/GM) to 10⁻⁵⁰ at every e, a and GM. P5: a scaled by 10³ leaves r/a unchanged to 3·10⁻⁵¹ and
  multiplies the period by 10^4.5 exactly to rounding.
- P6: the best wrapped Cauchy misses the clock's law by 4.8%, 25% and 129% at e = 0.3, 0.6, 0.9 (each fit ρ = ±e
  centred on the near point: post hoc, the clock's 1/(1 + e cos ν)² is nearest the Cauchy shape 1/(1 + e cos ν)
  squared away from it).
- P7: r/a in E is 1 − e cos E and its integral from the near point E − e sin E, both 0 in sympy.

## Run 3 (prediction committed before the run)

- **P1′.** With t = tan(ν/2) and the push-forward written rationally (E = 2·atan(t/k), so dE/dν = k(1 + t²)/(k² + t²)
  · ½·... taken by sympy from that form, with cos ν = (1 − t²)/(1 + t²) and k² = (1 + e)/(1 − e) substituted as a
  symbol K with K² = (1 + e)/(1 − e)), (1/2π)·dE/dν − √(1−e²)/(2π(1 + e cos ν)) reduces to 0 in sympy after
  eliminating K and √(1−e²) by their squares (`sp.simplify` on the expression with K = √((1+e)/(1−e)) written as
  s/(1−e), s = √(1−e²)). Fails only by my algebra or code.
