# GDI: what directions give, for a ball, a lens and a pair in orbit

25 Nov 2026; Tom: "Merge and proceed with gravity." *Reads and Writes* §7, "Gravity on the stage", open item (2) asks
whether what FCL run 9 found for two masses at rest (places and the masses' ratio from the pull's directions alone,
no mass, no G) holds for a ball, a lens and the pair in orbit. Exact arithmetic (sympy, mpmath at 50 digits) and a
seeded least squares; no data. A pull is not a read (R1183); this sorts what each needs, in the corpus's terms: a
direction or a ratio of strengths needs no amount; a mass needs one carried in.

## Set-up

- **Ball.** A uniform ball of radius R at c. Its pull at x: GM(x − c)/|x − c|³ outside, GM(x − c)/R³ inside. Places
  given in counted steps; directions are unit vectors; "strength ratios" are |g(x₁)|/|g(x₂)|, scale-free in GM.
- **Point lens.** A point mass on the sky at the origin, Einstein radius θ_E; a source at β on the line through it.
  Images θ± = (β ± √(β² + 4θ_E²))/2, magnifications μ± = 1/(1 − (θ_E/θ±)⁴). Directions on the sky are angles; the
  Einstein radius is an angle; the mass is θ_E²·c²·D_L·D_S/(4G·D_LS), which needs the distances (amounts).
- **Singular isothermal sphere (SIS).** Deflection θ_E·sign(θ) whatever |θ|: images θ± = β ± θ_E for β < θ_E,
  magnifications |θ|/(|θ| − θ_E).
- **Pair in orbit.** Masses μ/(1 + μ) and 1/(1 + μ) at distance D on the x axis about their centre of mass, turning
  at the Kepler rate Ω² = G(M₁ + M₂)/D³; the effective pull in the turning frame (gravity plus the centrifugal term) at
  a place in the orbit plane.

## Predictions (committed before any code)

- **D1 (ball, directions).** Outside the ball the pull's directions are a point mass's at c: two places not on one
  line through c give c exactly, and no set of outside directions gives R. Inside, the directions also point at c, so
  directions alone cannot tell inside from outside.
- **D2 (ball, ratios).** Along a counted line through c, the strength ratios g(x)·|x − c|² / g(x′)·|x′ − c|² are 1
  outside and (|x − c|/R)³ inside: the ratios give R in steps exactly, with no mass. Scaling every length and the step
  together moves no ratio.
- **D3 (point lens).** With the lens's own direction seen, the two images' directions give θ_E = √(θ₊·|θ₋|) (the
  geometric mean, the exchange's fixed point θ ↔ −θ_E²/θ) and β = θ₊ + θ₋ exactly; their magnification ratio is
  |μ₊/μ₋| = (θ₊/|θ₋|)⁴... checked exactly, whatever the formula's power turns out to be stated here as: a function of
  θ₊/|θ₋| alone, no mass and no distance. The mass needs D_L·D_S/D_LS carried in.
- **D4 (lens unseen).** The two images' directions alone leave a one-parameter family of lens places; adding the
  magnification ratio fixes it exactly.
- **D5 (SIS against point).** For the SIS the Einstein radius is the arithmetic mean (θ₊ + |θ₋|)/2, not the geometric
  one; the two agree only when β = 0. So the corner's mean is the deflection law's, not a property of lenses in general.
- **D6 (pair in orbit, scaling).** The effective pull's directions are unmoved when every length is scaled and the rate
  follows Kepler (Ω ∝ k^(−3/2)); they depend on μ and the masses' places in units of D only.
- **D7 (pair in orbit, recovery).** From the effective pull's directions at six seeded places in the plane (positions
  in counted steps, the masses' places, D and μ unknown), a least squares from many starts recovers μ and the masses'
  places to 10⁻⁸ in steps on noise-free directions, for μ = 1, 0.3 and 0.01. No mass and no G enter.

Kill conditions: any exact identity failing past 10⁻⁴⁰; D7's recovery off by more than 10⁻⁶ in μ or in a place, or a
second solution found as good.

## Runs
