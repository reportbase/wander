# ISX: the inverse square as a read and its exchange

14 November 2026. Tom: "maybe inverse square law has a read/write pair.", then "yes, run the test".

## The claim

The light a flat, evenly bright disc (radius a, radiance L) gives a point on its axis at distance d, counted with the
receiver's cosine, is exactly its share of the receiver's front hemisphere, E/(πL) = 1/(1 + s²) with s = d/a: the
Cauchy's heat. The inverse square is that share's far chart (s → ∞), the flat near field its near chart (s → 0). The
exchange s ↔ 1/s makes them complements, E(s) + E(1/s) = πL, half each at the corner s = 1. The share is a read
(unmoved by scaling the world); the inverse square in d needs a held fixed, an amount carried in (a write). Between two
ends, each reads the other (étendue): the ratio of the two reads leaves the sizes, their product the distance.

Known beforehand, stated so the run is not mistaken for discovery: the disc's on-axis irradiance πL·a²/(a² + d²) is
textbook (radiometry; Lambert); NRF (`plans/nrf-plan.md`) already has the slope form σ(s) + σ(1/s) = −2 for the disc;
view-factor reciprocity A₁F₁₂ = A₂F₂₁ is classical (radiative transfer). What is tested here: that the exact share is
the Cauchy heat, that the exchange pairs near with far, what scaling moves, and whether the pairing is the disc's alone.

## Predictions (committed before any run)

All in exact arithmetic (fractions) or mpmath at 50 digits; "to 10⁻⁴⁰" means agreement past 40 digits.

- **X1** The on-axis irradiance by direct quadrature of L·cosθ·cosθ′·dA/r² over the disc equals πL·a²/(a² + d²), at
  s = 1/10, 1/3, 1, 3, 10 (to 10⁻⁴⁰). Kill: any miss past 10⁻³⁰.
- **X2** E(s)/(πL) = 1/(1 + s²) is the Cauchy heat h² of the direction with v/h = s; and E(s) + E(1/s) = πL exactly for
  s = p/q over 30 rationals (exact fractions). Kill: any rational where the sum is not exactly πL.
- **X3** At the corner s = 1 the share is ½; the slope σ(s) = d ln E/d ln s = −2s²/(1 + s²), σ(1) = −1,
  σ(s) + σ(1/s) = −2 (exact). Kill: any failure.
- **X4** Far chart: s²·E/(πL) → 1, off by 1/(1 + s²) (exactly 1/(1 + s²) relative), so within 10⁻⁶ at s = 10³; near
  chart: E/(πL) → 1, off by s²/(1 + s²). Kill: either limit off its stated form.
- **X5** Scale test: (a, d) → (ka, kd) with L fixed leaves E unchanged for k = 10⁻³, 7, 10⁶ (exact). Holding a fixed
  and moving d → kd, the far-off E falls as 1/k² only to leading order, the exact factor (1 + s²)/(1 + k²s²). Kill: any.
- **X6** Two coaxial parallel discs (radii r₁, r₂, gap d): the closed-form view factors obey A₁F₁₂ = A₂F₂₁ to 10⁻⁴⁰ at
  five geometries (reciprocity: each end's read of the other, its ratio F₁₂/F₂₁ = A₂/A₁ exactly, the distance gone);
  their product F₁₂·F₂₁·(πd²)²/(A₁A₂) → 1 as d → ∞ (the distance in the sizes' geometric mean), within 10⁻⁵ at
  d/max(r) = 10³. Kill: reciprocity off past 10⁻³⁰, or the far product not tending to 1.
- **X7** The pairing is the disc's: for a square plate of half-side b on axis (s = d/b), E(s) + E(1/s) is **not**
  constant (varies by more than 10⁻³ over s in [1/10, 10]). Kill: constant to 10⁻⁶. (Claude's guess, not derived.)
- **X8** A sphere of radius a seen from its centre's distance d ≥ a gives E/(πL) = (a/d)² exactly at every d ≥ a, the
  inverse square with no near-field flattening outside it: no exchange partner, since s < 1 is inside the body. Kill:
  quadrature off past 10⁻³⁰.

## Runs

(appended below as they come out; nothing above this line edited afterwards)
