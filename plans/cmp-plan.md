# CMP: the conformal map, CIW beyond the circle

*19 October 2026 (Tom's local date), SPN R390.*

*Tom (19:22 MDT): "we also have demos that shows the address points to shape, so we can recover the shape. I'm wondering
if there is more here, ideas that we missed."*

*Claude proposed three leads; first the conformal map, the general form of CIW, which the archived* Reader Geometry as
Addressing *noted (item 5) and the corpus never followed up. Tom (19:24): "yes".*

*Exact (mpmath) where a closed form exists, seeded samples elsewhere, thresholds in standard errors. Scripts in
`runs/cmp/`.*

## Known beforehand

- **The Riemann mapping theorem.**
  - A simply connected region Ω is the conformal image F(D) of the unit disc, with F(0) a chosen interior point.
  - For a Jordan boundary, F extends one-to-one from the circle onto ∂Ω (Riemann; Carathéodory 1913).
  - **[classical]**
- **Harmonic measure is conformally invariant.** The harmonic measure of ∂Ω from F(z) is the Poisson kernel P_z on the
  circle carried by F. From F(0) it is the uniform measure dφ/2π carried by F (Garnett and Marshall 2005).
  **[classical]**
- **Theodorsen's equation** for a star-shaped near-circle (Theodorsen 1931; Gaier 1964; Henrici 1986, vol. 3).
  - Write F(e^{iφ}) = ρ(θ(φ))·e^{iθ(φ)}, with F(0) = 0 and F′(0) > 0.
  - The boundary correspondence then satisfies θ(φ) = φ + K[ln ρ(θ(·))](φ), where K is the conjugate-function operator
    on the circle: the periodic Hilbert transform, which sends cos nφ to sin nφ and kills constants.
  - It is solved by iteration.
  - **[classical]**
- **The archive.** *Reader Geometry as Addressing* item 5: "the even circle pushed through it lands as the shape's harmonic
  measure from the image of the centre … with the line's Cauchy as the simplest case." Not followed up in
  `plans/archive-gems.md`.
- **CIW.**
  - On a circle the wrapped Cauchy (the Poisson kernel) is ±(2·dθ/dφ − 1)/2π, twice the straight-ray inscribed rate less
    the central rate.
  - For an ellipse with φ its geometric central angle, the combination is no wrapped Cauchy.
- **draw's SMP:** a uniform turn's census is the unit circle for every shape. RCC: the readings carry the turn, not the
  size.
- **ADR:** the Cauchy family is carried onto itself by Möbius maps, its parameters moving with them (McCullagh 1996).

## The set-up

- **The shapes.** Ω = F(D) with three kinds of map:
  - **Möbius maps** F(z) = z/(1 − bz), b real in (0, 1): the control, whose images are discs;
  - **polynomial maps** F(z) = z + a·zⁿ, n ∈ {2, 3, 5}, a real in (0, 1/n), so F is univalent: smooth lobed shapes;
  - **the near-circles** among the polynomial maps (a small), for Theodorsen.
- **The reader** stands at w = F(z) for an interior z.
- **The inscribed reading** of the boundary point F(e^{iφ}) is its straight-ray direction from w,
  θ_w(φ) = arg(F(e^{iφ}) − w).
- **The central angle** is φ, the conformal angle: the disc's own uniform turn carried to the shape. It is not the
  geometric angle from F(0), except on a circle.
- **The radii.** The central reader at F(0) = 0 reads ρ along the geometric direction θ: amounts, in a unit no reading
  fixes.

## Predictions

**C1 (the shape's own Cauchy is the disc's Poisson kernel carried by F).**
- For each map and three interior points z, Brownian motion from w = F(z), run by walk-on-spheres to within 10⁻⁶ of ∂Ω,
  lands at conformal angles φ whose law is the wrapped Cauchy P_z: the boundary point is pulled back through F⁻¹ by
  Newton's method on F(e^{iφ}).
- KS distance below 1.63/√N (the 1% level), N = 10⁵ per case, nine cases (three maps × three points).
- **[classical]**; the run checks our arithmetic.
- *Killed* if any case fails.

**C2 (the straight-ray combination is the circle's alone).**
- 2·dθ_w/dφ − 1 = 2π·P_z(φ) holds at every φ and every interior z for the Möbius maps, to 10⁻³⁰ at 50 digits over
  10³ seeded (z, φ).
- For each polynomial map with a ≥ 0.05, there is a sampled (z, φ) where it fails by more than 10⁻³.
- So straight rays carry the turn's law to the shape's own Cauchy only when the shape is a circle; elsewhere F bends the
  rays.
- *Killed* if the Möbius case fails or any polynomial case holds.

**C3 (the failure is first order in the shape's departure).**
- For F(z) = z + a·z³ and z = 0.3, the largest |2·dθ_w/dφ − 1 − 2π·P_z(φ)| over φ, divided by a, at a = 10⁻², 10⁻³ and
  10⁻⁴, agrees between the three within 2%.
- *Killed* if not.

**C4 (Theodorsen recovers the boundary correspondence).**
- For F(z) = z + a·zⁿ with n ∈ {2, 3, 5} and a ∈ {0.02, 0.1}: start from the true radii ρ(θ) of ∂Ω (computed from F)
  on N = 1,024 points.
- Iterating θ ← φ + K[ln ρ(θ)] (K by the FFT) converges to arg F(e^{iφ}), to 10⁻¹⁰ in the maximum, within 60
  iterations.
- *Killed* if any case fails.

**C5 (the radii's unit cancels).**
- K kills constants, so replacing ρ by k·ρ (k ∈ {10⁻³, 7, 10³}) leaves the recovered θ(φ) unchanged to 10⁻¹².
- So the boundary correspondence, and with it the shape's own Cauchy from F(0), is recovered from:
  - the address reader's directions θ;
  - the central reader's radii up to an unknown unit;
  - and no amount carried in.
- *Killed* if any case moves by more than 10⁻¹².

**C6 (the verdict).** A judgment. *Killed* if C1, C2 or C4 is killed.
- The shape's own Cauchy (its harmonic measure from a reader inside it) is the disc's Poisson kernel carried by the
  conformal map. The turn's law (the unit circle, SMP) is the disc; the shape is the map.
- Straight rays carry it onto the shape only for a circle, which is why CIW's identity is the circle's alone.
- For other shapes, the turn needs the map:
  - the address reader's directions;
  - the central reader's radii in no unit;
  - Theodorsen's step.
- With them, a reader recovers the boundary correspondence, and with it the shape's harmonic measure from F(0).

## What would and would not be shown

**Shown:**
- that CIW's result generalises through the conformal map;
- what each reader contributes to recovering it: directions, radii up to a unit, and no amount.

**Not shown:**
- that any reader computes a conformal map;
- shapes that are not star-shaped about F(0), where Theodorsen's equation does not apply in this form;
- three dimensions, where conformal maps are only Möbius (Liouville's theorem) and the theorem has no analogue.

## Runs

(Nothing above this line is edited after a run.)
