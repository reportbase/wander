# LGS: light and gravity on one stage

25 Nov 2026; Tom: "the connection between observation and gravity is potentially very interesting.", then "yes, 1 then
2" (this is 1; LNS is 2). Exact arithmetic (sympy) and 40-digit quadrature (mpmath); no data. Under R1229 the aim is the
same known results by one route, no new physics. A pull is not a read (R1183); a look and a pull share the stage.

## The stage, and the two takes

From a place, the directions u, each with dΩ. A scene of bodies, each with a surface radiance B (vacuum, no absorption
unless said) and a density ρ.
- **The look's take:** along u, the radiance of the first surface met, B(u). Its flux vector at the place is
  F = ∫ B(u)·u dΩ (Lambert's net flux).
- **The pull's take:** along u, the column, the matter met all along it, ∫ρ dr. The pull is g = G·∫ (∫ρ dr)·u dΩ (CLM).
- **One premise for both:** what a direction carries does not depend on how far along it its source lies. For light this
  is the brightness theorem (radiance unchanged along a ray in vacuum); for gravity it is CLM's column premise.

## What I know beforehand

The brightness theorem and the inverse square of light are textbook; a Lambertian sphere's flux πB(R/d)² is textbook;
CLM showed the column premise is the inverse square for gravity; COS gave D = π(R/d)² for a ball and a pull
G·ρ·(4R/3)·D. Mass-to-light ratios are standard in astronomy. What I have not seen stated: the two inverse squares as one
premise on one stage, and the ratio of the two takes as a distance-free reading. From memory; to check.

## Predictions (committed before any code)

- **L1 (one inverse square, two amounts).** For a ball of radius R with uniform radiance B and density ρ, at every d > R:
  F = B·D and g = G·ρ·(4R/3)·D, D = π(R/d)²·n̂, exactly (sympy). Light and gravity are the same stage weight D, each
  times one amount fixed by the body (B; Gρ·4R/3).
- **L2 (the premise is the inverse square, for light).** For a small patch whose flux at the place falls as d^(−p), the
  radiance it presents (flux over the solid angle it covers, A·cos θ/d²) is the same at every distance exactly when p = 2
  (in D dimensions p = D − 1, the solid angle ∝ d^(−(D−1))) (sympy).
- **L3 (with absorption, an amount enters).** In a medium of absorption κ the radiance along a direction falls as
  e^(−κ·r), so the look's take depends on where along the direction the surface lies; the ball's F is no longer B·D
  (off by more than 1% at κR = 0.1, d = 5R) and the ratio moves with d. The premise fails exactly where the medium adds
  an amount per length.
- **L4 (the ratio of the takes).** For one uniform ball, g/F = G·ρ·(4R/3)/B at every d > R exactly: a mass-to-light
  reading with no distance in it. For a uniform cube approached face-on (radiance B on its faces, density ρ), g/F changes
  with distance by more than 10% between 0.5 and 20 sides from its near face.
- **L5 (occlusion parts them).** A small ball hidden wholly behind a larger one leaves F unchanged and raises g by its
  whole share: the look takes the first surface, the pull the whole column (as COS's K6, now with light).
- **L6 (scale).** Lengths × k at fixed B and ρ: F unmoved exactly (D a ratio of lengths, B per direction), g × k; the
  direction of each unmoved.

Kill: an identity (L1, L2, L4's ball, L5, L6) not exact in sympy or past 10⁻²⁵ in quadrature (quadratures done in
variables measured from the edge, to avoid CLM's cancellation); a threshold in L3 or L4's cube not met.

## Runs

### Run 1 (`runs/lgs/lgs.py`, output `runs/lgs/lgs-run1.txt`)

Nothing killed.
- **L1 not killed**: for a ball, F = πB·R²/d² = B·D and g = (4π/3)Gρ·R³/d² = Gρ·(4R/3)·D exactly: one stage weight D,
  times the radiance for light and times the mean column for gravity.
- **L2 not killed**: radiance unchanged with distance exactly when the flux falls as d^(−(D−1)), in D = 2, 3, 4: the
  brightness theorem is light's inverse square, as CLM's column premise is gravity's.
- **L3 not killed**: with absorption κR = 0.1, F/(B·D) is 0.887, 0.652, 0.145 at d = 2, 5, 20 R, and g/F 1.50, 2.05,
  9.20 against 4/3 without absorption: the medium adds an amount per length and the look's take then depends on where.
- **L4 not killed**: one ball's g/F = 4GρR/(3B), no d; a cube face-on 0.542, 0.692, 0.953 (× Gρ/B) at 0.5, 2, 20 sides,
  76% apart (COS's ⟨L⟩, since only its near face is seen and its radiance is uniform).
- **L5 not killed**, but by construction: F takes the first surface and g sums every column, so the hidden ball leaves F
  at πB/25 and adds Gρπ/6000 = G·(4/3)πr³ρ/8² to g. The check is that the sums were set up as the takes say, not a test.
- **L6 not killed**: lengths × k at fixed B and ρ, F unmoved and g × k exactly.

Reading: light's inverse square and gravity's are one premise on one stage: what a direction carries does not depend on
how far along it its source lies (the brightness theorem; the column). A look and a pull then both read the stage weight
D, a ratio of lengths, times an amount per direction: radiance, the first surface's; the column, everything along it. So
one ball's pull over its light is a mass-to-light reading with no distance in it; a body without spherical symmetry
(the cube) loses that, and a medium (absorption) breaks the light's half of the premise while gravity's stands. Classical
in every part (Lambert, the brightness theorem, Newton, mass-to-light ratios); the joining is the stage's, and under
R1229 it is support by the same results with one route for two laws.
