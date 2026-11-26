# CRC: a Cauchy reading a Cauchy

26 Nov 2026; Tom: "This is worth understanding in more detail.  A cauchy reading another cauchy.", then "Yes". After
R1235 (*Reads and Writes* §7, "Two Cauchies"): the read's Cauchy (SHV) laid over gravity's take (DHV). Exact arithmetic
and 25-digit quadrature (mpmath); no data. Under R1229: known results by the stage's route, no new physics. A pull is not
a read (R1183).

## Set-up

Matter lies at z ≤ 0. A survey plane at height z = h > 0 is painted, point by point, with the pull found there,
g = G·Σ m·(q − p)/|q − p|³ (G = 1). A reader stands at height a above the plane, at (X, Y, h + a), looking down. Its heat
per unit of the plane is the flat screen's cos³, P_a(ρ) = a/(2π(a² + ρ²)^(3/2)), the 3D Poisson kernel (the SHV Cauchy of
scale a). The heat-weighted reading of the paint is R = ∫ P_a·g dA over the plane. In the plane (2D gravity, pull
2G·m·(q − p)/|q − p|²) the kernel is P_a(x) = a/(π(a² + x²)).

## What I know beforehand

The Poisson representation of a bounded harmonic function in a half-space, the semigroup P_a ∗ P_h = P_(a+h) and
gravity's upward continuation are textbook. The corpus has the relay of standpoints (SUM: heights and feet m + iγ add)
and GRV (a sheet's pull is the Poisson kernel of its density). What the run adds, if it holds, is the reading: the
read's heat laid over gravity's take returns gravity's take at the reader's own place, and where it stops.

## Predictions (committed before any code)

- **C1 (one Cauchy from two).** On the line and on the plane, P_a ∗ P_h = P_(a+h) for (a, h) = (1, 1), (0.3, 2.5),
  (4, 0.25): to 10⁻²⁰ at sample points.
- **C2 (the reader gets the pull at its place).** In 3D, for a point mass on the reader's axis, a point mass off axis and
  a pair of masses at different depths, R equals the pull at (X, Y, h + a), all three components, to 10⁻¹².
- **C3 (standpoints add).** On the line, a unit line mass at foot m₂ and depth c read through the plane at h by a reader
  at X, height a above the plane: R = the pull of the mass at height a + h + c, i.e. the Cauchy at the complex point
  (X − m₂) + i(a + h + c), for four off-axis cases, to 10⁻²⁰.
- **C4 (where it stops).** Each off by more than 1% (relative, in |R − g|/|g|):
  (a) the heat-weighted median of g_z over the plane in place of the mean, for an off-axis point mass;
  (b) a point mass between the plane and the reader (at height h + a/2, off axis), with the mass below kept;
  (c) a point mass above the reader (height h + 2a, off axis), with the mass below kept.
- **C5 (scale).** Lengths × k (masses fixed): R and g both × 1/k², their ratio 1, at k = 3 and 1/7, to 10⁻¹².

Kill: an identity past its tolerance; a C4 case within 1%.

## Runs
