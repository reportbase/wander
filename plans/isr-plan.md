# ISR: the inverse square revisited, as addresses and payload

*22 October 2026. Tom: "we've put physics aside writing the ofs paper. we have learned alot, lets revisit our physics
results such as the inverse square law." `papers/inverse-square.md` was written on 10–11 October, before the address and
payload split (OFS §7.2, Theorem 6), reading and writing (OFS §9), the reader's and the writer's spheres (OFS §3.7), the
emitter as the turn aimed outward, and K. This plan re-reads it with those, and checks every new claim in exact
arithmetic (mpmath, 50 digits). Predictions first; nothing above "Runs" is edited after the run.*

## Known beforehand
- A point source over a plane lights it as E = P·cos θ/(4π r²) = P·d/(4π(d² + ρ²)^(3/2)): the "cos³ law" of
  illumination (textbook photometry). That this is the two-dimensional Cauchy (Proposition 5(e)'s density, scaled) is a
  change of variable, not new; it is classical in statistics that the gnomonic projection of a uniform hemisphere is the
  bivariate Cauchy (OFS §7.8, Knight 1976). The lighthouse is the one-dimensional case.
- The radiance theorem; irradiance as radiance × projected solid angle; view factors (inverse-square.md §0).
- log N–log S: in Euclidean space a homogeneous population of sources gives N(>S) ∝ S^(−3/2) whatever its luminosity
  function (radio astronomy's source counts, 1950s; inverse-square.md §2 has the same as 1.5 levels per level).
- NRF (10 Oct): the isotropic line, (1/d)·arctan(b/d), killed P3 by its slope in levels (σ(1) = −1.637, not −1.5; the
  flip identity missed by 0.224). The Lambertian disc's s²/(1 + s²) passed. Draw's SMP lab: a uniform turn gives the
  Cauchy whatever the figure (CLAUDE.md, "check draw's labs").

## The reading to test
An arrival is an address (a direction, laid by the turn) times a payload (what comes along it). The inverse square is
entirely the payload's bookkeeping: per address the paint is unchanged (radiance), and distance changes only how many
addresses a source paints. The emitter's own uniform turn, aimed outward and laid on a flat receiver, is the
(D − 1)-dimensional Cauchy whose scale is the distance; the inverse square on the axis is that Cauchy's height. The
corner of the pair (extent, distance) belongs to the address count; where the payload's own fall-off is mixed in (a
slope in levels of light), it can move.

## Predictions
- **P1 (the law is the Cauchy's height).** An isotropic point source of power P in D dimensions, a flat receiver
  (dimension D − 1) at distance d: the power per unit area is (P/2)·C_{D−1}(x; d), C_n the n-dimensional Cauchy density
  of scale d, Γ((n + 1)/2)·d/(π^((n+1)/2)·(d² + |x|²)^((n+1)/2)). Its height on the axis is P/(|S^{D−1}|·d^(D−1)), the
  inverse (D − 1)-th power law, for D = 2, 3, 4, 5. *Killed* if either identity misses by more than 10⁻⁴⁰ at five test
  points each.
- **P2 (the corner is in the address count, the fall-off in the payload).**
  (a) An isotropic line of half-length b and linear power λ at distance d from its middle, received from every
  direction: E = (λ/(4πd))·2·arctan(b/d); the received power per unit angle is λ/(4πd), the same at every address the
  line paints. The address factor (2/π)·arctan(b/d) has f(s) + f(1/s) = 1 (s = b/d) and its median, f = ½, at s = 1
  exactly.
  (b) A Lambertian disc of radius a, radiance L, on its axis at d, received by a flat patch: E = πL·sin²θ with
  sin²θ = a²/(a² + d²); L per address is the same at every d; the projected address count sin²θ has f(s) + f(1/s) = 1,
  f(1) = ½.
  (c) NRF's slope criterion mixes the two: for the line, the slope of E in levels is σ = −1 + (slope of the address
  factor), and σ(1) = −1 − 2/π = −1.6366 (NRF's −1.637); the address factor's own slope there is exactly −2/π, the
  half-Cauchy's density at the corner, 1/π, over its share there, ½.
  *Killed* if any identity misses by more than 10⁻⁴⁰.
- **P3 (every pair at its corner on the receiver).** Isotropic emission landing on a plane at distance d (D = 3): the
  medians of |x|/d, |y|/d and |y/x| are each 1 exactly (each pair at its own corner, as OFS Proposition 5(e)); the radial
  r/d, not a pair of unit relations, has median √3 (a polar angle of 60°). Lambertian (cos-weighted) emission puts the
  radial median at r/d = 1 (45°) and the per-axis median at |x|/d = √(2/3). *Killed* if any value misses by more than
  10⁻³⁰.
- **P4 (the weighting and the dimension).** Cos-weighted emission's share within s = a/d on the axis is sin^(D−1)θ; it
  is reciprocal-symmetric (f(1) = ½) only for D = 3 among D = 2 … 6. Uniform emission's marginal along any one axis of
  the receiver is the one-dimensional Cauchy of scale d, median at the corner, in every D = 2 … 6. *Killed* if the
  first is reciprocal-symmetric for another D, or the second misses its corner by more than 10⁻³⁰.
- **P5 (counts by flux are a reading).** A homogeneous Euclidean population with a luminosity function of two kinds
  (L₁ = 1 with weight 0.7, L₂ = 30 with weight 0.3): log N(>S)/log S has slope −3/2 exactly at every S; multiplying every
  length by k (sources' sizes and distances, radiance fixed, so L ∝ k²) leaves N(>S) unchanged; a slab of thickness T
  gives a slope that runs monotonically from −3/2 (S large) to −1 (S small).
  *Killed* if the slope misses −3/2 by more than 10⁻³⁰, if scaling moves N by more than 10⁻³⁰ relatively, or if the slab's
  slope leaves (−3/2, −1).

## Runs
