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

**Run 3** (`runs/orb/orb3.py`, output `runs/orb/orb-run3.txt`). P1′ not killed: in t = tan(ν/2), with k = s/(1 − e)
and s² = 1 − e², the numerator of (1/2π)·dE/dν − stage is 0. (P1′'s text as committed has a stray fragment,
"· ½·... taken by sympy from that form"; the check is the one its last sentence describes.)

**What runs 2 and 3 show.** A two-body orbit is a stage and a payload. Taking the eccentric anomaly evenly, the
direction from the focus has the wrapped Cauchy of width β = (1 − √(1−e²))/e, centred on the far point: the stage, set by
e alone, with no amount. The time spent per direction is that stage times r/a, the distance in the orbit's own size,
exactly: the payload, unique once the stage is fixed (the clock divided by it). Its mean over the stage is 1, over the
clock 1 + e²/2. Added up over the stage it is Kepler's equation, M = E − e sin E; so the one step that takes an
iteration, the position at a given time, is the payload's sum inverted. The period needs a and GM carried in
(2π√(a³/GM), no e); scaling a moves neither stage nor payload. The clock's own law over ν is on no wrapped Cauchy (5% to
129% off). Classical in every part (the half-angle relation, Laplace's β, the areal law, the time-averaged distance
a(1 + e²/2)); the reading as a stage and a payload ours. Tom: "We would have to create a payload that gives the same
results".

## Run 4: where the stage's standpoint sits (predictions committed before the run)

Tom (25 Nov 2026): "Proceed", to Claude's offer (the stage's wrapped Cauchy of width β is the harmonic measure seen
from a point a·β from the auxiliary circle's centre; which point, what it is, how it moves with e). Claude's reading
before the run, not checked: tan(ν/2) = k·tan(E/2) has the form of the relativistic aberration formula
tan(θ′/2) = √((1+v)/(1−v))·tan(θ/2), with e in the place of the speed v; whether that is in print was not searched.
Exact: sympy for identities, mpmath at 50 digits; e in {0.01, 0.1, 0.3, 0.6, 0.9, 0.99}.

- **Q1 (β a half-slope).** With e = sin φ (φ the angular eccentricity), β = tan(φ/2) and k = (1 + β)/(1 − β), so k
  is the corner composed with β by tangent addition, 1 ⊕ β; identities in sympy.
- **Q2 (e a speed).** With η = artanh e: e = tanh η, k = e^η, β = tanh(η/2). The map from E to ν is a hyperbolic
  translation of the disc by η along the major axis, so the stage's standpoint sits at hyperbolic distance η from the
  centre (Euclidean β, since 2·artanh β = η); identities in sympy, and the push-forward of uniform E equal to the
  harmonic measure (Poisson kernel) from −β to 10⁻⁴⁵ at 200 values of ν for every e.
- **Q3 (composing).** Applying the map for e₁ then for e₂ is the map for e₃ = (e₁ + e₂)/(1 + e₁e₂), velocity
  addition, and β₃ = (β₁ + β₂)/(1 + β₁β₂): the boost's rule (PYK's κ = −1) twice; 30 seeded pairs to 10⁻⁴⁵.
- **Q4 (between centre and focus).** e/2 < β < e for every 0 < e < 1, β = e/2 + e³/8 + O(e⁵); so the standpoint lies
  nearer the centre than the focus, past the half-way point; symbolic series and the six values.
- **Q5 (the ratios at the ends).** The stage's density at the far point over the near point is k² = (1 + e)/(1 − e),
  equal to r_max/r_min; the payload's near over far is 1/k²; the clock's far over near is (1 + e)²/(1 − e)², the
  stage's k² times the payload's... wait: the clock is stage × payload, so its far/near is k² × k² = k⁴ = r_max²/r_min²
  (the areal law's r²); all exact in sympy.

What could fail: every item is an identity, so only by my algebra (Q5's statement as written above names the payload's
ratio twice: its far/near is k², near/far 1/k²; the claim checked is clock far/near = k⁴) or by Q3's direction of
composition; Q2's reading as a speed is a reading, and a hit there says the forms agree, not that an orbit is a boost.

**Run 4** (`runs/orb/orb4.py`, output `runs/orb/orb-run4.txt`). Q1 killed by my code; Q2–Q5 not killed. Before the
run, the Q5 check was corrected in code to the predicted direction (clock far/near = k⁴; the script had first tested
near/far), and Q4's check reduced to the predicted terms; neither touched a prediction.

- Q1 killed in its first clause: sympy left β − tan(φ/2) as −tan(φ/2) − cot φ + csc φ, which it did not reduce to 0
  (it is 0: csc φ − cot φ = tan(φ/2)). Its second clause, ((1 + t)/(1 − t))² = k² with t = tan(φ/2), is 0.
- Q2: e^(2η) = (1 + e)/(1 − e) and 2β/(1 + β²) = e with e = tanh η, β = tanh(η/2), both 0; the push-forward of
  uniform E is the Poisson kernel from −β to 2·10⁻⁴⁹; 2·artanh β = artanh e at all six.
- Q3: the map for e₁ then e₂ is the map for (e₁ + e₂)/(1 + e₁e₂), and the β's add by the same rule, to 10⁻⁵⁰ on 30
  pairs.
- Q4: β = e/2 + e³/8 + e⁵/16 + …; e/2 < β < e at all six.
- Q5: the stage's far over near k², the payload's near over far 1/k², the clock's far over near k⁴, all 0 in sympy.

## Run 5 (prediction committed before the run)

- **Q1′.** With t = tan(φ/2), sin φ = 2t/(1 + t²) and cos φ = (1 − t²)/(1 + t²) (so √(1 − e²) = cos φ for
  0 < φ < π/2), β = (1 − cos φ)/sin φ reduces to t in sympy as a rational function. Fails only by my algebra or code.

**Run 5** (`runs/orb/orb5.py`, output `runs/orb/orb-run5.txt`). Q1′ not killed: β − t is 0 as a rational function.

**What runs 4 and 5 show.** The stage's standpoint is the point −β of the anomaly's disc (the far side), β the
half-slope of the angular eccentricity (e = sin φ, β = tan(φ/2)) and k the corner composed with it, (1 + β)/(1 − β).
In the speed's chart e = tanh η: the map from E to ν is a hyperbolic translation of the disc by η = artanh e along the
major axis, the same form as relativistic aberration with the speed e, and two such maps compose by velocity addition,
(e₁ + e₂)/(1 + e₁e₂), the β's by the same rule (PYK's boost kind). The standpoint lies between the centre and the
focus, past half way (e/2 < β < e). At the ends: the stage's far over near is k² = r_max/r_min, the payload's near over
far its reciprocal, the clock's far over near k⁴, the areal law's r². A form shared with aberration, not a claim that
an orbit is a boost; whether the likeness is in print was not searched. Classical in each part.

## Run 6: the orbit at e ≥ 1 (predictions committed before the run)

25 November 2026, Tom: "1 2 3", the third being the orbit pushed to the parabola and the hyperbola. Worked by hand
beforehand from the standard relations (Barker's equation; tan(ν/2) = √((e + 1)/(e − 1))·tanh(F/2) for the hyperbolic
anomaly F); the run checks them exactly. Claude's guess when offering it, "the stage becomes the plain Cauchy on a line
of directions between the asymptotes", is restated as R1 and R4.

- **R1 (the parabola's lighthouse).** On a parabola r = p/(1 + cos ν), the coordinate across the axis through the focus
  is y = p·tan(ν/2) = p·D, D Barker's parabolic anomaly. So directions ν taken evenly from the focus over (−π, π) give y
  exactly the Cauchy of scale p (the semi-latus rectum) centred on the axis: a lighthouse turning at half the rate. The
  eccentric-anomaly stage of runs 2–5 does not carry over: uniform D pushed to ν has density (1 + D²)/2 per unit ν,
  which has no finite total.
- **R2 (the parabola's clock).** Time per unit D is proportional to 1 + D² (so M ∝ D + D³/3, Barker), the reciprocal of
  R1's Cauchy density in y, times a constant: the clock over y is the stage's density inverted.
- **R3 (the exchange e ↔ 1/e).** With e = coth η for the hyperbola (and tanh η for the ellipse), the hyperbolic map is
  tan(ν/2) = e^η·tanh(F/2): the ellipse of eccentricity e and the hyperbola of eccentricity 1/e have the same k, and
  their maps differ only by tan ↔ tanh. The parabola, e = 1, is the exchange's fixed point, where k is infinite.
- **R4 (the hyperbola's stage).** Directions ν taken evenly over the hyperbola's open range (−ν∞, ν∞), cos ν∞ = −1/e,
  give t = tan(ν/2) the Cauchy cut to |t| < K = √((e + 1)/(e − 1)), the asymptote's half-slope; as e → 1⁺ the cut
  goes to infinity and R1's Cauchy returns.
- **R5 (the payload survives).** For the hyperbola dM = (r/a)·dF exactly, M = e·sinh F − F, r = a(e·cosh F − 1): time
  is the even measure in F times r/a, Kepler's hyperbolic equation the sum, the measure now with no finite total (the
  orbit is open), so no stage as a probability.
- **R6 (the ellipse's stage at e → 1⁻).** The elliptic stage's width β → 1 and its weight piles onto the far point:
  for any fixed arc about ν = 0 not containing π, its share of the stage goes to 0.

Kill conditions: any identity off by more than 10⁻⁴⁰ at 50 digits, or failing in sympy where exact; R4 on a 200-point
grid against the cut Cauchy; R6 as a limit at e = 1 − 10⁻ⁿ, n = 2, 4, 8.

**Run 6** (`runs/orb/orb6.py`, output `runs/orb/orb-run6.txt`). R1 and R3 killed by my code; R2, R4, R5, R6 not killed.

- R1 killed in its first clause: sympy left y − p·tan(ν/2) as p·(sin ν − (1 + cos ν)·tan(ν/2))/(1 + cos ν), which is
  0 (sin ν = (1 + cos ν)·tan(ν/2)) but was not reduced. Its other clauses hold exactly: the density of y = p·tan(ν/2)
  under uniform ν is the Cauchy p/(π(p² + y²)), and uniform D pushed to ν has density (1 + D²)/2, its weight on
  (0, π − 10⁻⁶) already 2·10⁶.
- R2: dt/dD = (p²/2)(1 + D²), times the Cauchy density in y a constant, p/(2π); its integral D + D³/3 (Barker).
- R3 killed in its first clause: sympy left √(e^(2η) − 1)·√(1/(e^(2η) − 1)) − 1 unreduced (it is 0 for η > 0). The
  second clause, k(1/e)² = k(e)², is 0; the hyperbolic map tan(ν/2) = K·tanh(F/2) holds to 3·10⁻⁴⁹ at e = 1.01, 1.5,
  3, 20.
- R4: uniform ν over the open range is the Cauchy in tan(ν/2) cut at |t| < K to 10⁻⁵¹; tan(ν∞/2) = K at all four.
- R5: dM/dF − r/a = 0.
- R6: the elliptic stage's share on |ν| < 1 is 0.0246, 0.00246, 2.5·10⁻⁵ at e = 1 − 10⁻², 10⁻⁴, 10⁻⁸ (as √(1 − e²)).

## Run 7 (predictions committed before the run)

- **R1′.** With t = tan(ν/2), sin ν = 2t/(1 + t²), cos ν = (1 − t²)/(1 + t²), y − p·t reduces to 0 as a rational
  function in sympy.
- **R3′.** With x = e^(2η) − 1 declared positive, √x·√(1/x) − 1 reduces to 0 in sympy, and K(coth η) − e^η is under
  10⁻⁴⁵ at 50 digits for η = 0.01, 0.5, 2, 10.

Fail only by my algebra or code.

**Run 7** (`runs/orb/orb7.py`, output `runs/orb/orb-run7.txt`). R1′ not killed (y − p·t = 0 as a rational function).
R3′ killed by my set-up: its sympy clause is 0, but at η = 10, coth η − 1 ≈ 4·10⁻⁹ loses nine of the fifty digits and
e^η ≈ 22,026 multiplies what is left, so the absolute gap is 7·10⁻⁴⁰, over my 10⁻⁴⁵; a bound on the absolute gap was
the wrong measure.

## Run 8 (prediction committed before the run)

- **R3″.** The relative gap |K(coth η) − e^η|/e^η is under 10⁻⁴⁰ at 50 digits for η = 0.01, 0.5, 2, 10.
