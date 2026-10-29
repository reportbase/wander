# EUL: the Cauchy and Euler's exponential, and what stops at the plane

29 Oct 2026. Tom: "anny connection between cauchy and eulers/", then "yes. Its likely that classical math missed
something. they did not have the computational power you do. Take a look around, see what you find."

## Known beforehand

- The Cauchy's characteristic function is e^(imt − γ|t|); with z = m + iγ it is e^(izt) for t > 0 (classical).
- The Cayley map W = (X − i)/(X + i) takes the line to the circle; a Cauchy with parameter z goes to the wrapped Cauchy,
  whose moments are E[Wⁿ] = wⁿ, w = (z − i)/(z + i) (McCullagh 1996, classical). So the circle chart's mean is the
  Cayley image of the standpoint z.
- On the circle the wrapped Cauchy is the Poisson kernel, harmonic measure from w (classical).
- Kato and McCullagh (2020): the spherical Cauchy on S^(d−1), density ∝ ((1 − ρ²)/(1 + ρ² − 2ρ·t))^(d−1), is the Möbius
  image of the uniform law and is closed under Möbius maps; a boosted uniform sky (OFS §11, SRA) is this law with
  ρ = tanh(η/2).
- The Poisson kernel of the ball in d dimensions is (1 − r²)/|x − u|^d. In d = 2 the two exponents agree (1); in d = 3
  they do not (3/2 against 2). Laplace's equation is unchanged by conformal maps only in the plane; Liouville's theorem
  leaves only Möbius maps as the conformal maps of space (classical).
- CIW (`plans/ciw-plan.md`): in the plane the landing density of a uniform turn from an interior point, doubled, less
  the uniform, is the Poisson kernel (2·dθ/dφ − 1)/2π.
- Draw's labs: the projective reader's cross ratios (two Möbius charts of one line); nothing on characteristic
  functions, the wrapped Cauchy's mean or three dimensions. Wander's runs: no 3D Poisson kernel.

## The question

In the plane several of the reader's facts coincide: the standpoint z, the Euler exponential e^(izt), the circle's mean
w, harmonic measure, the Möbius family, and the two sweeps' rates. Which survive in three dimensions, and which split?

## Predictions (written before any run)

**E1.** For X ~ Cauchy(m, γ), z = m + iγ: E[e^(itX)] = e^(izt) for t > 0 and e^(iz̄t) for t < 0. Checked by quadrature
at three z and four t. *Killed* if any differs by more than 10⁻²⁵.

**E2.** With W = (X − i)/(X + i), E[Wⁿ] = wⁿ, w = (z − i)/(z + i), n = 1 … 6, at three z. *Killed* if any differs by more
than 10⁻²⁵.

**E3.** The reader's quarter turn, θ uniform on [0, π/2]: E[e^(2iθ)] = 2i/π, its length 2/π and its direction i (the
corner). *Killed* if not exact.

**E4 (the plane: one law).** On the circle, the Poisson kernel from w = ρ (harmonic measure) and the Möbius image of the
uniform (the wrapped Cauchy with ρ) are the same density at every angle. *Killed* if they differ anywhere by more than
10⁻³⁰ (ρ = 0.1, 0.5, 0.9).

**E5 (space: two laws).** On S², with t the cosine to the axis:
- harmonic measure from x = r·axis, P_H = (1 − r²)/(4π(1 + r² − 2rt)^(3/2));
- the spherical Cauchy, P_M = (1 − ρ²)²/(4π(1 + ρ² − 2ρt)²).
  - (a) E_H[t] = r, and E_H[P_l(t)] = r^l for l = 1 … 6 (moments powers of one number). *Killed* if not, to 10⁻²⁵.
  - (b) E_M[t] = f(ρ) with f(ρ) > ρ for ρ = 0.1 … 0.9, and E_M[P_2] ≠ E_M[P_1]² (moments not powers). *Killed* if
    f(ρ) ≤ ρ anywhere or the moments are powers.
  - (c) For ρ = 0.1 … 0.9 no r makes P_H equal P_M: the least sup-norm gap over r stays above 10⁻³ of P_M's peak.
    *Killed* if any falls below.
  - (d) Möbius closure: a boost of rapidity η₂ carries P_M(tanh(η₁/2)) to P_M(tanh((η₁ + η₂)/2)) (to 10⁻²⁵), and carries
    P_H(r = 0.3) to no P_H (least sup-norm gap above 10⁻³). *Killed* if either fails.

**E6 (the two sweeps' rates).** In space, the landing density of uniform directions from x = r·axis inside the unit
sphere is L = (1 − rt)/(4π(1 + r² − 2rt)^(3/2)). No constants a, b make a·L + b/(4π) equal P_H for r ≠ 0 (the plane's
2L − U = P has no counterpart). *Killed* if a least-squares fit at r = 0.3 and 0.7 leaves a residual under 10⁻⁶ of the
peak.

## Runs

**Run 1** (29 Oct, `runs/eul/eul.py`, mpmath at 40 digits, 83 s; output `runs/eul/eul-run1.txt`). Nothing killed.
- E1: E[e^(itX)] = e^(izt) to 6·10⁻⁴² at three z and four t (the negative t with z̄).
- E2: E[Wⁿ] = wⁿ to 1.4·10⁻⁴¹, n = 1 … 6.
- E3: E[e^(2iθ)] = 0.63662i, exactly 2i/π: the quarter turn's mean in the central chart points at the corner, its length
  2/π.
- E4: on the circle the Poisson kernel and the Möbius image of the uniform agree to 2·10⁻³⁹.
- E5a: in space harmonic measure keeps the powers: E_H[P_l] = r^l to 2·10⁻⁴⁴, l = 0 … 6, so its mean is the standpoint.
- E5b: the spherical Cauchy does not: E_M[t] above ρ at every ρ (0.1331 at 0.1, 0.6320 at 0.5, 0.9727 at 0.9), and
  E_M[P₂] below E_M[P₁]² (0.3701 against 0.3995 at 0.5). Post hoc, in closed form (sympy, checked at three ρ to 10⁻¹⁴):
  with ρ = tanh(η/2), **E_M[t] = coth η − η/sinh² η**, equivalently 1/β − ln((1 + β)/(1 − β))/(2β²γ²) with β = tanh η.
  In the plane the mean is ρ = tanh(η/2), algebraic in ρ; in space the rapidity η itself, a logarithm, enters.
- E5c: no harmonic measure equals a spherical Cauchy: the least sup gap over r runs from 0.0055 (ρ 0.1) to 0.067
  (ρ 0.8) of the peak; the nearest r is above ρ (0.588 at 0.5).
- E5d: a boost of rapidity 0.7 carries the spherical Cauchy at tanh(0.2) onto tanh(0.55) to 7·10⁻⁴¹ (rapidities add); a
  boost of 0.5 carries harmonic measure from r = 0.3 onto no harmonic measure (least gap 0.022, nearest r 0.543).
- E6: no a·L + b/(4π) is the 3D Poisson kernel (residual 0.026 at r = 0.3, 0.058 at r = 0.7 of the peak; best a 1.52 and
  1.66, against the plane's exact 2 and −1).

**Reading.** In the plane one law holds four roles at once: the Möbius image of the uniform turn (closed under the
reader's turns and boosts), harmonic measure (where a random path from the standpoint lands), the law whose moments are
the powers of one point w (Euler's structure, so the standpoint is the mean in the circle chart), and the two sweeps'
rates combined (CIW). In space they part: harmonic measure keeps the powers and the mean, the spherical Cauchy keeps
the Möbius maps (the boosted sky), and the rates' combination has no counterpart. The classical reason is the one the
plan named: Laplace's equation is conformally invariant only in the plane, and in space the conformal maps are only the
Möbius maps (Liouville). Every piece is classical (the 3D Poisson kernel's Legendre series is the generating function
of the P_l; Kato and McCullagh's family; Liouville). The mean of an isotropic sky seen under a boost is likely in the
radiation literature; not searched for. Nothing here suggests a gap in classical mathematics. What it gives the corpus:
the reader's coincidences between standpoint, mean, Möbius closure and the two sweeps are a fact of the plane, and a
three-dimensional statement has to say which of the two laws it means.
