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

### Run 1 (`runs/lns/lns.py`, output `runs/lns/lns-run1.txt`)

Nothing killed.
- **N1 not killed**: a point mass at z = −5b, 0, 7b deflects by 4GM/(c²b) at each, and split as ⅓ at −3b and ⅔ at 4b
  by the same: the lens reads only the column. Said plainly: over the whole path this is the integral's shift
  invariance, so it could not have failed; it holds only because the path is taken whole (a source or observer at a
  finite distance brings the lens equation's distance ratios back in).
- **N2 not killed**: α = 4GM/(c²b) exactly.
- **N3 not killed**: a ring of column on the sky deflects from outside at 2a by exactly its mass at its centre (to 10⁻⁴⁰)
  and inside by 1.7·10⁻⁴²: the thin-lens kernel is the pull in two dimensions, 1/r^(D−1) at D = 2, CLM's column premise
  one dimension down.
- **N4 not killed**: a uniform disc of column and Σ ∝ 1/(1 + ξ²) deflect by 4G·M(<ξ)/(c²ξ) exactly (4πGξ/c² and
  4πG·ln(1 + ξ²)/(c²ξ)). Said plainly: the sympy step sums rings with N3's ring law, so it is exact given N3 (checked
  numerically), not independent of it. An extra direct 2D quadrature, not among the predictions, divided by zero at the
  lens point itself and was taken out.
- **N5 not killed**: lengths and masses × k leave every angle unmoved; masses alone × k move the angles × k.

Reading: a lens reads the column, the pull's own take, and lays it on the sky's plane, where its law is the pull's one
dimension down: the deflection is the plane's pull of the projected column, so only the column inside the impact radius
bends the light, the plane's shell theorem. Light here carries gravity's take to the observer as directions: what the
look sees bent is a column's pull. Classical in every part (the thin-lens formula, Einstein 1936, the enclosed-mass
law); the joining (CLM's premise in D = 3 for the pull and D = 2 for the lens) is the stage's, support by the same
results (R1229).
