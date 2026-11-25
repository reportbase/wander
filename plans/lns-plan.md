# LNS: a lens sees columns

25 Nov 2026; Tom: "yes, 1 then 2" (this is 2, after LGS). Exact arithmetic (sympy) and 40-digit quadrature (mpmath); no
data. Under R1229: known results by the stage's route, no new physics. A pull is not a read (R1183).

## Set-up

Light passing a mass distribution, weak field, the Born approximation (a straight path, impact vector ξ in the lens
plane, along z): the deflection α(ξ) = (2/c²)·∫ ∇⊥Φ dz over the whole path, Φ the Newtonian potential. The column
along the line of sight is Σ(ξ) = ∫ ρ dz.

## What I know beforehand

The thin-lens formula α(ξ) = (4G/c²)·∫ Σ(ξ′)·(ξ − ξ′)/|ξ − ξ′|² d²ξ′ and the point mass's 4GM/(c²b) are textbook; that a
circularly symmetric lens deflects by its mass inside ξ is textbook. What the stage adds, if it holds, is the reading:
the lens is gravity on the sky's plane with the column as its mass, and the plane's law is CLM's p = D − 1 at D = 2.

## Predictions (committed before any code)

- **N1 (only the column).** For any matter along the line of sight, the deflection depends only on Σ: a point mass moved
  along z (z = −5, 0, 7 in units of b) gives the same α, exactly, and a mass split into two along the same line gives the
  sum's α (sympy, the integral over the whole path).
- **N2 (the point mass).** α = 4GM/(c²·b) exactly from the integral.
- **N3 (the plane's law).** The kernel of the thin-lens formula, (ξ − ξ′)/|ξ − ξ′|², is the pull of a point in two
  dimensions, 1/r = 1/r^(D−1) at D = 2: CLM's column premise one dimension down. A uniform ring of column on the sky
  deflects from outside as its mass at its centre and not at all inside (40-digit quadrature, to 10⁻²⁵ in a variable free
  of cancellation).
- **N4 (enclosed mass).** For a circularly symmetric lens, α(ξ) = 4G·M(<ξ)/(c²ξ), the column outside ξ adding nothing,
  for two profiles (a uniform disc of column, and Σ ∝ 1/(1 + ξ²)) (sympy).
- **N5 (scale).** Lengths × k and masses × k (M/b fixed): every deflection angle unmoved exactly; masses × k alone:
  angles × k (an amount).

Kill: an identity not exact in sympy or past 10⁻²⁵ in quadrature.

## Runs
