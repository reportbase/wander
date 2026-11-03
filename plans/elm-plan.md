# ELM: Euler's formula as a count of reads

3 Nov 2026. Tom: "i'm just wondering if a tighter connection to euler's is possible. where should we look?", then
Claude's lead (one limit, two axes), then a Gemini reply pasted by Tom, offering four predictions, read here as "write
that plan". Exact arithmetic (Python fractions and mpmath at 50 digits); no data.

## The claim

A reader holds a direction as [1 : s] and composes two by tangent addition, s₁ ⊕ s₂ = (s₁ + s₂)/(1 − s₁s₂), which is the
projective form of the product (1 + is₁)(1 + is₂). Cut a turn θ into n equal reads s = θ/n and compose them: (1 + iθ/n)ⁿ.
Every finite n is a count of reads, exact and, for rational θ, inside ℚ[i]. As n grows the count goes to e^(iθ): Euler's
formula, reached as Bernoulli reached e by (1 + 1/n)ⁿ. One limit, two axes: along the scale (the real axis) it gives e,
along the turn (the imaginary axis) e^(iθ). The paper's "π and e are where a count tries to hold a read" (*Reads and
Writes* §8; R646's "the writer's continuum is a count completed") then has a literal construction.

Known beforehand, cited as such:
- The identity lim (1 + w/n)ⁿ = e^w for every complex w is classical (Euler 1748, *Introductio*, ch. VII–VIII), and so is
  its error, e^w·(1 − w²/(2n) + O(n⁻²)).
- Tangent addition as the product of 1 + is: the archived *Algebra of Discrete Observation* (composition in the Gaussian
  integers, R472); draw's TB algebraic presentation (the rational half-angle, no trigonometric call).
- The Cauchy's characteristic function e^(izt), z = m + iγ the standpoint: EUL run 1 (`plans/eul-plan.md`).
- Alternating small rotations about two axes converge to the turn about their sum with error O(1/n) (the Lie–Trotter
  product formula); the symmetric splitting with O(1/n²) (Strang 1968).
- draw's labs: `avd` (averaging directions) composes reads; none takes the n-step limit. Nothing found that reads the limit
  as reads counted.

So nothing here is new mathematics. What is tested is that the reading holds in exact numbers: which part of the
construction is the reader's at every n, what the count misses, and what the limit (the writer's) repairs.

## Gemini's predictions, checked before the run

Gemini's P3 gives the modulus error as (γ² − m²)t²/(2n). Expanding e^w(1 − w²/(2n)) with w = izt = −γt + imt gives
−w²/2 = (m² − γ² + 2imγ)t²/2, so the modulus factor is 1 + (m² − γ²)t²/(2n): the sign is the other way. The phase
term mγt²/n agrees. L5 below uses the corrected sign. Its P4 is the Lie–Trotter formula, kept as L6 with its name.
A note on P3's reading: the step 1 + izt/n = (1 − γt/n) + i·mt/n is a read times a scale, not a pure read [1 : s];
the height enters as an amount on the real axis (a damping), the foot as the turn. That is the classical split of
iz into its real and imaginary parts; whether it says more is a reading, not tested here.

## Predictions (written before the script)

- **L1 (closure).** For θ = 1 and θ = 1/2, n = 1 … 64, the composed reading s_n = tan(n·atan(θ/n)), built by tangent
  addition in fractions, is a rational number at every n, and equals Im/Re of (1 + iθ/n)ⁿ computed in ℚ[i] exactly.
  Killed if any n gives a mismatch or leaves ℚ.
- **L2 (the angle falls short).** θ − n·atan(θ/n), times n², tends to θ³/3: within 1% of θ³/3 at n = 100 for
  θ = 1, π/2, π. Killed if any is off by 1% or more there.
- **L3 (the length grows, and the read does not see it).** R_n = |(1 + iθ/n)ⁿ| = (1 + θ²/n²)^(n/2); n(R_n − 1) within 1%
  of θ²/2 at n = 1000 for θ = 1, π/2, π (the next term predicts a relative θ²/(4n), 0.25% at θ = π). The reading Im/Re is
  the same with and without each step normalized, at every n to 40 digits. Killed if either fails.
- **L4 (one limit, two axes).** With E_n(w) = (1 + w/n)ⁿ/e^w, n·(E_n(w) − 1) within 1% (in modulus) of −w²/2 at n = 1000
  for w = 1 (Bernoulli), w = iπ/2 and w = iπ (Euler; at w = iπ the count lands near e^(iπ) = −1). Killed if any is not.
- **L5 (from a standpoint).** For m = 0.5, γ = 0.3, t = 2, n·(E_n(izt) − 1) within 1% of (m² − γ² + 2imγ)t²/2 at
  n = 1000 (real part 0.32, imaginary part 0.6). Killed if not; Gemini's sign (real part −0.32) killed if it fits better.
- **L6 (where it stops).** Turns of space: θ₁ = 0.7 about x and θ₂ = 0.4 about y. Alternating n steps of each,
  (R_x(θ₁/n)R_y(θ₂/n))ⁿ, against the one turn about (θ₁, θ₂, 0): the leftover turn's angle times n within 2% of
  (θ₁θ₂/2)·sin(φ/2)/(φ/2) = 0.1362 at n = 1000, φ = √(θ₁² + θ₂²) the whole turn (the bracket's θ₁θ₂/2 = 0.14, carried
  through the turn's own exponential, which scales a part square to the axis by sin(φ/2)/(φ/2); found while writing
  this, before any run); the symmetric step R_x(θ₁/2n)R_y(θ₂/n)R_x(θ₁/2n) leaves an angle that times n² stays within
  a factor 2 between n = 250 and n = 1000. In the plane the same alternation leaves exactly no angle at every n. Killed if
  any part fails.

## Runs

**Run 1** (3 Nov, `runs/elm/elm.py`, output `runs/elm/elm-run1.txt`). L1–L5 not killed; L6 killed.
- L1: tangent addition in fractions equals Im/Re of (1 + is)ⁿ in ℚ[i] at every n to 64, θ = 1 and ½.
- L2: n²·shortfall/(θ³/3) = 0.99994, 0.99985, 0.99941 at n = 100 for θ = 1, π/2, π.
- L3: n(R − 1)/(θ²/2) = 1.00025, 1.00062, 1.00247 at n = 1000 (the predicted θ²/(4n)); the reading the same with each
  step normalized, to 40 digits.
- L4: n(E_n − 1) against −w²/2 off 0.09%, 0.12%, 0.32% for w = 1, iπ/2, iπ; (1 + iπ/1000)¹⁰⁰⁰ = −1.00495 + 1.04·10⁻⁵ i.
- L5: n(E_n − 1) = 0.3204 + 0.6002i against 0.32 + 0.6i (off 0.07%); Gemini's sign off 94%.
- L6: alternating n·leftover 0.1362390 against 0.1362390 (off 9·10⁻⁹); symmetric n²·leftover 0.0121047 at all three n;
  the plane's leftover 1.6·10⁻²⁴ against my 10⁻⁴⁰. Killed by my set-up: the angle was read by acos of a trace near 1,
  which keeps only half of 50 digits (√(10⁻⁴⁸) ≈ 10⁻²⁴).

**L6′ (written after run 1, before run 2).** The plane's leftover measured as the largest entry of the difference of the
two matrices, below 10⁻⁴⁰ at n = 1, 7, 64, 1000; the rest of L6 unchanged. Killed if not.

**Run 2** (3 Nov, `python3 runs/elm/elm.py --run2`, output `runs/elm/elm-run2.txt`). L6′ not killed: the plane's
leftover 1.1·10⁻⁴⁸ (the working precision); the rest as run 1. Nothing else changed.

**What it says (a reading).** Every finite count of reads is exact and the reader's: composed by tangent addition, it
stays in ℚ[i] for rational steps, and the length each step adds (1 + θ²/(2n) over the whole turn) is never in the
reading. What the count misses is the angle, θ³/(3n²), the tangent running ahead of the arc at every step; the limit,
the writer's, repairs both the angle and the length and lands on e^(iθ). Bernoulli's e and Euler's e^(iθ) are the same
limit with the step along the scale or square to it, and the error has the same form, −w²/(2n), on both axes. From a
standpoint z = m + iγ the same limit gives the Cauchy's characteristic function, the foot as the turn and the height as
a damping on the real axis (an amount, not a read). In space the order of the steps matters at 1/n, the leftover the
bracket carried through the turn, (θ₁θ₂/2)·sin(φ/2)/(φ/2), to nine digits; the plane has none. So the count of reads
gives Euler's formula exactly where the turns commute, and no further.
