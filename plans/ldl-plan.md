# LDL: light's delay past a lens

25 Nov 2026; Tom: "1 then 5". *Reads and Writes* §7, open item (4), its second half: light's own delay past a lens.
Two images of one source arrive at different times; the delay has two parts, the extra path (geometric) and the slowing
near the mass (Shapiro). Exact arithmetic (sympy), no data. Classical (Refsdal 1964; Schneider, Ehlers and Falco 1992,
from memory). What is sorted: which part of the delay the images' directions give, and what needs an amount.

## Set-up

Thin lens, angles in units of the Einstein radius θ_E, source at β on a line through the lens. The arrival time of an
image at θ, up to a constant, is t(θ) = T·[½(θ − β)² − ψ(θ)], T = θ_E²·D_Δt/c, ψ the lens potential in θ_E² units. For a
point mass ψ = ln|θ| and T = 4GM(1 + z_L)/c³; for the singular isothermal sphere (SIS) ψ = |θ|. Images where
dt/dθ = 0. q = θ₊/|θ₋|, the ratio of the images' distances from the lens, a ratio of directions.

## Predictions (committed before any code)

- **T1 (point mass).** Δt/T = ½(q − 1/q) + ln q exactly, the geometric part ½(q − 1/q) and the Shapiro part ln q, each a
  function of q alone; both odd under q ↔ 1/q, both zero at q = 1 (the ring).
- **T2.** The geometric part is at least the Shapiro part for every q > 1, equal only in the limit q → 1; their ratio
  (q − 1/q)/(2 ln q) grows without bound.
- **T3 (SIS).** The geometric parts of the two images are equal, so the whole delay is the potential's:
  Δt = T·2β (θ_E units), the extra paths cancelling exactly.
- **T4 (scale).** Scaling every length and every time together by k (GM/c² a length, so with them) moves no image
  direction and no q, and multiplies Δt by k: the delay is an amount. For the point mass, a counted delay and q give
  M(1 + z_L) = c³·Δt/(4G·f(q)) with no distance; for the SIS a counted delay needs D_Δt, a distance.
- **T5.** For the point mass, the brightness ratio r = q² gives the delay's form from brightness alone,
  Δt/T = ½(√r − 1/√r) + ½·ln r.

Kill conditions: an identity failing past an exact zero (or 10⁻⁴⁰ numerically at rational inputs); T2's inequality
failing at any q > 1 tried.

## Runs
