# PRX: which sources pair near with far

17 November 2026. Tom: "This seems simple enough, does not require expensive measurement, just pure theory. Seems like the
read write has something new to say here.", then "Yes, write the plan and run the test".

## The claim, from the read

A flat source of uniform radiance L in a plane parallel to a receiving element, a height d above the element's foot.
The light caught, counted with the receiver's cosine, is L times the source's projected solid angle. When the source
contains the foot and each azimuth φ meets its edge once, at radius ρ(φ):

  E(d)/(πL) = (1/2π) ∫ ρ²/(d² + ρ²) dφ.

So the read sees the source only through its edge slopes ρ(φ)/d, one per direction of the uniform turn about the axis.
ISX found that a centred disc pairs near with far, E(d) + E(a²/d) = πL, and a square does not. The read says why, and
says which other shapes pair:

- **The rule (R).** Since ρ²/(d² + ρ²) at height c²/d equals 1 minus d²/(d² + (c²/ρ)²)... more simply: the share at c²/d
  equals the complement of the share at d with every radius ρ replaced by c²/ρ. So E(d) + E(c²/d) = πL for every d
  exactly when the radii, as the uniform turn reads them, have the same law as c²/ρ: the law of ln ρ over the turn is
  symmetric about ln c. Then c is the geometric mean of the radii, exp(mean ln ρ), and it is the corner: half the light
  at d = c. (The transform ∫ dμ(u)/(d² + u²) over all d fixes the law of u², so "exactly when" is both ways.)
- **A ring** (the source between ρ₁(φ) and ρ₂(φ), the foot not in it): E(d)/(πL) = (1/2π) ∫ [f(ρ₂) − f(ρ₁)] dφ with
  f(u) = u²/(d² + u²). If ρ₁ρ₂ = c² along every direction, the same identity gives E(c²/d) = E(d): not complements but
  mirrors, the light greatest at d = c. A near-and-far pair either completes (the foot inside) or mirrors (the foot
  outside), the two charts RWX found in other physics (a crossover; a best point).

Known beforehand, so not discovery: the projected-solid-angle formula and the off-axis disc's view factor are
textbook radiometry; the power of a point (ρ(φ)ρ(φ + π) = |a² − b²| for a circle seen from a point b from its centre,
Euclid III.35–36) is classical; ISX's disc and square. Not checked against the literature: whether the pairing rule (R)
or the mirror for a source off the foot is stated anywhere.

## Predictions (committed before any run)

mpmath at 40 digits. "Pairs" means max over d ∈ {10⁻², …, 10²} (41 points, even in ln d) of |E(d) + E(c²/d) − πL|/πL
below 10⁻²⁵ at the stated c; "mirrors" the same for |E(d) − E(c²/d)|/πL. "Fails" means the least such deviation over
c (a scan about the geometric mean of the radii, refined) is above 10⁻³. E computed by the azimuth integral, and for
the discs and the annulus cross-checked by a direct area integral in double precision (to 10⁻⁸).

- **P1 (the rule on its own family).** ln ρ = ln c + ε·cos(nφ), ε = ½, n = 1, 2, 3, 5: each pairs at c, though none is
  round. Kill: any one fails to pair.
- **P2 (odd modes).** ln ρ = ln c + 0.4 cos φ + 0.3 cos 3φ + 0.2 sin 5φ pairs (a sum of odd modes changes sign under
  φ → φ + π, so its law is symmetric). Kill: it does not pair.
- **P3 (mixed modes fail).** ln ρ = ln c + 0.5 cos φ + 0.25 cos 2φ and ln ρ = ln c + 0.4 cos 2φ + 0.3 cos 4φ each fail
  (their third central moments are not zero). Kill: either pairs, or deviates by less than 10⁻³ at its best c.
- **P4 (a disc off its axis, the foot inside).** A disc of radius a with the foot b from its centre, b/a = 0.3, 0.7,
  0.95: pairs at c = √(a² − b²) (the power of the point), half the light at d = c. Kill: any fails, or the best c is not
  √(a² − b²) to 10⁻²⁰.
- **P5 (a disc with the foot outside).** b/a = 1.5, 3: mirrors at c = √(b² − a²) (the tangent length), the light
  greatest at d = c. Kill: either fails to mirror, or the maximum is elsewhere by more than 10⁻¹⁰ relative.
- **P6 (an annulus, centred).** Radii 1 to 4 and 1 to 10: mirrors at c = √(ρ₁ρ₂), the light greatest there. Kill:
  either fails.
- **P7 (the ellipse).** Semi-axes 1 and 2, centred: fails. Kill: deviates by less than 10⁻³ at its best c.
- **P8 (polygons).** Regular n-gons about their centre, n = 3, 4, 6, 8: all fail, the least deviation falling as n
  grows. The square reproduces ISX's sums (1.0045 πL far off and 1.108 πL at d equal to the half-side) when c is the
  half-side. Kill: any polygon pairs, the deviation is not decreasing in n, or the square's numbers differ from ISX's in
  the third digit.

## Runs
