# TWS: why there are exactly two sweeps

*16 October 2026 (Tom's local date). Tom, about 04:48: "the inside and outside are just two different type of sweeps,
but why,structurally." Then, about 04:53, after Claude's answer (two pivots): "yes, a detailed explanation without
physics is needed. people have been very confused about this."*

## The claim

A sweep is a ray turning about a pivot. On the circle drawn on the chord AB (the drawing V = H), the arc is reached
evenly by an even turn from only two kinds of pivot:
- the centre, where the arc moves as fast as the ray turns: the central sweep;
- a point of the circle, where the arc moves twice as fast as the ray turns: the inscribed sweep.

From any other pivot, equal turns reach unequal stretches of arc. The two points of the circle that matter are the pair's
own ends, home A and B. The centre is the pair's middle, M, which is neither party's standpoint.

The two sweeps read one point in two charts:
- From A, the ray's reading s = v/h = tan θ is where the ray meets the tangent line at B. That is the stereographic
  projection of the circle from A onto that line: the line is unbounded, so even steps give the Cauchy law.
- From M, the radius ends at ½(cos 2θ, sin 2θ) = ½(h² − v², 2hv), the inscribed reading squared, (h + iv)². Everything
  there is bounded.

All of this is classical: the inscribed angle theorem (Euclid III.20, and the angles at points inside and outside a
circle, III.20 and its standard extensions), stereographic projection, the Weierstrass half-angle substitution, and z ↦ z²
on the unit circle. What is ours is the reading: the two pivots are a party and the pair's middle, and they are the only
two. Geometry only, exact (mpmath, 40 digits), no amounts, no bridge.

## Predictions (written 16 Oct about 05:00, before any run)

The unit circle is centred at O. A pivot P stands at distance p from O, at (p, 0). A ray from P at direction ψ meets the
circle at Q(ψ), the hit ahead of P, or the far hit when P is on the circle. φ(ψ) is Q's angle about O, and the arc's
rate is r(ψ) = dφ/dψ.

- **T1. The centre.** At p = 0, r ≡ 1 for every ψ, to 10⁻³⁰.
- **T2. A point of the circle.** At p = 1, r ≡ 2 for every ray into the circle, to 10⁻³⁰.
- **T3. Any other point inside.** For 0 < p < 1, r(ψ) = 2t/(t + t′), with t and t′ the distances from P to the circle
  ahead and behind (to 10⁻³⁰ at 50 directions for each of p = 0.1, 0.5, 0.9). Its extremes are 1 − p and 1 + p
  (outward and inward along OP), so r is not constant.
- **T4. Outside.** For p > 1, over the rays that meet the circle, r at the near hit is not constant. Its least and
  greatest differ by more than 10⁻³ at p = 1.5, 2 and 5, and it grows without bound toward the tangent rays.
- **T5. Only two.** Scanning p over 0, 0.01, 0.02, …, 3 (301 values), the spread max r − min r over 200 directions is at
  most 10⁻³⁰ only at p = 0 and p = 1, and more than 10⁻⁴ everywhere else. (The proof is below; this is its check.)
- **T6. The two charts, on the chord.** With A = (0, 0), B = (1, 0), M = (½, 0), h = cos θ and v = sin θ, A's ray at θ
  ends at P = (h², hv). For 40 values of θ in (0, π/2), each to 10⁻³⁰:
  - 2(P − M) = (h² − v², 2hv) = (h + iv)²;
  - the angle of P − M is 2θ;
  - the ray meets the tangent at B, x = 1, at height s = v/h = tan θ = tan(φ/2), with φ = 2θ the central angle.
- **T7. Even steps of turn.**
  - Inscribed: θ even on (0, π/2) makes the law of s exactly 2/(π(1 + s²)), with median 1. Its mean truncated at S
    climbs (2/π)·ln 10 per decade of S: 1.4658711978 from 10⁶ to 10⁷, to 10⁻⁹.
  - Central: φ = 2θ even on (0, π) makes the means of the radius's ends, cos φ and sin φ, equal 0 and 2/π, to 10⁻³⁰,
    and both are bounded by 1.

*Proof of T5 (written before the run).* Put P = (p, 0) and the ray direction u = (cos ψ, sin ψ). The ray meets the
unit circle where |P + λu|² = 1, so λ = −p cos ψ ± √(1 − p² sin² ψ). Write t and −t′ for the two roots, with
t + t′ = 2√(1 − p² sin² ψ), the chord's length. Moving the ray by dψ moves the hit by t·dψ across the ray, and the arc
meets the ray at an angle whose cosine is (half the chord)/1. So the arc moves by r = t/√(1 − p² sin² ψ)
= 2t/(t + t′) per unit of turn. That is 1 + (−p cos ψ)/√(1 − p² sin² ψ) for the hit ahead. It is constant in ψ only if
p cos ψ/√(1 − p² sin² ψ) is constant. At ψ = π/2 this quotient is 0. So it must vanish for every ψ, which needs p = 0 (r ≡ 1),
unless the square root vanishes with it, which happens at p = 1 for the rays into the circle, where the far hit gives
r ≡ 2. For p > 1 only the rays with |sin ψ| ≤ 1/p meet the circle. At the two tangent rays the square root vanishes
while p cos ψ does not, so r is unbounded there and not constant. ∎

What a kill would mean:
- T1, T2 or T6: my computation, since the theorems are classical.
- T3 to T5: my claim that only two pivots exist, the point of this plan.
- T7: the readings' laws, already in OFS §7.

## Runs

### Run 1 (16 Oct about 05:05, `tws/tws.py`, output in `tws/run1.txt`; 6 s)

- **T1 not killed.** At the centre the arc's rate is 1 for every direction.
- **T2 not killed.** From a point of the circle it is 2 for every ray into it.
- **T3 killed, by my set-up.** For p = 0.1, 0.5 and 0.9, the rate matches 2t/(t + t′) to 2·10⁻⁴¹ at all 50
  directions, and the outward extreme is 1 − p exactly. But the inward extreme, at ψ = π, printed −2.8·10⁴⁴. The hit's
  angle there sits on atan2's cut at ±π, so the numerical derivative straddled a jump of 2π.
- **T4 not killed.** Outside, the rate at the near hit runs over [−4.70, −0.50] at p = 1.5, [−7.33, −1.00] at p = 2 and
  [−21.5, −4.00] at p = 5, and reaches about −10⁴ beside a tangent ray. It is negative because the near hit moves
  against the turn.
- **T5 not killed.** Of 301 pivots from p = 0 to 3, only p = 0 and p = 1 give a constant rate.
- **T6 not killed.** On the chord, 2(P − M) = (h + iv)², its angle is 2θ, and s = tan θ = tan(φ/2) is where the ray
  meets the tangent at B, all within 10⁻³⁰.
- **T7 not killed.** The inscribed readings are exactly Cauchy, with median at s = 1 and a mean that climbs
  1.46587119776 a decade. The central sweep's means are 0 and 2/π.

### Run 2, T3′ (prediction written 16 Oct about 05:08, before running)

The same claim as T3, with the hit's angle measured from the direction opposite the pivot, so it never crosses ±π. Its
derivative then needs no unwrapping. *Killed if*, for p = 0.1, 0.5 or 0.9, the rate at ψ = π is off 1 + p by more than
10⁻³⁰, or the rate at ψ = 0 is off 1 − p by more than 10⁻³⁰.
