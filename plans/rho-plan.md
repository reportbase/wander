# RHO: the two ρ joined

*17 October 2026 (Tom's local date). Tom, 14:28: "the cauchy density setting is interesting. what does the paper say
about that."; 14:31: "yes", to Claude's suggestion that OFS never ties its two uses of ρ together. Geometry, exact.
Predictions written before the script (`rho/rho.py`) exists.*

## The two uses, as OFS has them

1. **The density** (after Proposition 5(d)): ρ in [0, 1], the share of the sweep's addresses at which a payload is met.
   Constant, it normalises out; varying with direction, the arrivals per unit of turn are ρ(θ)·2/π, divided by their
   total no longer a Cauchy, their median the payload's median direction, at the corner when ρ(θ) = ρ(π/2 − θ).
2. **The perturbation** (§7.4): a shape seen from the reader, ln r = a₀ + ρ·f(θ), the unit circle at ρ = 0 and the
   full shape at ρ = 1. Laid by direction the readings are the Cauchy at every ρ; laid along the outline the law moves
   with ρ (SHG: for f₁, P(v/h ≤ 1) = 0.500, 0.529, 0.563, 0.632 at ρ = 0, ¼, ½, 1). This plan writes the
   perturbation's strength as ε, to keep the letters apart.

## The claim

Laying a shape along its outline *is* use 1 with a density that varies with direction: the payload met at the address
θ is the length of outline per unit of turn, so

  ρ(θ) = σ(θ)/max σ,  σ(θ) = √(r² + r′²) = e^{a₀ + εf}·√(1 + ε²f′²).

The perturbation's strength ε is how far that density is from constant. So:
- the outline read evenly gives the Cauchy exactly when ρ is constant, which is §7.4's "only a circle" (r² + r′² = q²);
- the arrivals' median leaves the corner only by the shape's part that the exchange θ ↦ π/2 − θ reverses: to first
  order the median direction moves by δ = (ε/2)·[∫_{π/4}^{π/2} f dθ − ∫₀^{π/4} f dθ];
- the unknown size a₀ cancels from ρ, so the arrivals never read V*;
- to first order ln ρ = ε·f + const, so the arrivals give back the shape's modes (all but the constant) to O(ε²).

## Known beforehand

- **draw's SMP lab** (read at `ea07709`; see `plans/hzt-plan.md`): walked at constant speed along the outline, the
  arrival density is the arc element √(r² + r′²), recovered up to one constant (where the reader stood). That is the
  identity at the heart of this claim, in controlled form. What is new here is reading it as OFS's density ρ(θ), and
  the median's shift by the exchange-reversed part of the shape.
- SHG (`plans/shg-plan.md`): the numbers along the outline, and only circles having constant √(r² + r′²).
- Classical: the polar arc element; first-order perturbation of a quantile.

## Set-up (exact, mpmath at 40 digits)

SHG's shapes: f₁ = 0.3 cos 2θ + 0.1 cos(3θ + 0.4) (lopsided under the exchange) and f₂ = 0.25 cos 4θ (unchanged by
it); also f₃, a seeded sum (seed 11) of four terms aₙ cos(nθ + φₙ), n ≤ 8, amplitudes up to 0.3, made
exchange-symmetric by f₃(θ) = g(θ) + g(π/2 − θ). The quarter turn θ ∈ [0, π/2]. Use 1's law:
P(v/h ≤ t) = ∫₀^{arctan t} ρ dθ / ∫₀^{π/2} ρ dθ.

## Predictions

- **P1 (the identity).** For f₁ and f₂ at ε = ¼, ½, 1 and t = ¼, 1, 4, use 1's law with ρ = σ/max σ equals the law laid
  evenly along the outline (arc length to arctan t over arc length to π/2), to 10⁻³⁰, and at t = 1 for f₁ gives SHG's
  0.529, 0.563, 0.632 (to the three figures printed). *Killed* if any value misses.
- **P2 (the exchange).** For f₂ and f₃, at ε = ¼, ½, 1, the arrivals' median is the corner (θ = 45°) to 10⁻³⁰, while
  P(v/h ≤ ¼) is off the Cauchy's by more than 10⁻³ (the shape kept in the ends). For f₁ the median is off 45° by more
  than 0.1° at every ε. *Killed* if any misses.
- **P3 (first order).** For f₁ the exact median shift δ(ε), in radians, against the first-order δ₁(ε) above: at
  ε = 0.1, 0.05, 0.025, 0.0125 the relative error |δ − δ₁|/|δ₁| falls by at least a factor 1.8 per halving of ε (first
  order: it is O(ε)), and is below 2% at ε = 0.0125. Sign: δ₁ < 0 for f₁ (heavier toward zero; OFS's
  (2 + cos 2θ)/3 example moves the same way). *Killed* if either fails.
- **P4 (no size).** With a₀ = −5, 0, 5, every value of P1 and P2 is the same to 10⁻³⁰. *Killed* if any moves.
- **P5 (other payloads).** Weighting by r^k instead of the arc element (k = 1 the radius, an amount along the ray; k = 2
  twice the area of the shape's sector per unit of turn), the first-order median shift is k·δ₁: for f₁ the relative
  error against k·δ₁ below 2% at ε = 0.0125 for k = 1, 2; and the arc element's median differs from the radius's
  (k = 1) by an amount falling by at least a factor 3 per halving of ε (it is O(ε²)). *Killed* if either fails.
- **P6 (the shape read back).** From ρ alone, ln ρ(θ) minus its mean over the quarter turn equals ε·(f − f̄) to O(ε²):
  for f₁ and f₃ the largest error over 200 directions, divided by ε², stays within a factor 1.5 between ε = 0.1 and
  ε = 0.0125. The constant term of f and a₀ are not read (P4). *Killed* if the ratio drifts by more.

## What would and would not be shown

P1–P6 join OFS's two ρ: the strength of a shape's perturbation is the departure of the payload's density from
constant, and the density varying with direction is, for an outline, its arc element per unit of turn. A circle is the
one shape whose density is constant, so it reads as the Cauchy along its outline as well as by direction; a shape
moves the median only by its exchange-reversed part, and gives back its modes, not its size. Nothing here is physics:
which payload a real reader meets (arc length, radius, area, light) is the payload's business, and P5 shows only that
the first-order picture holds for each, scaled.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (17 Oct, `python3 -I rho/rho.py`; output `rho/rho-run1.txt`, 2 min)

- P1 not killed: the density σ/max σ on the inscribed sweep's addresses and arc length along the outline (computed from
  the polar points themselves) agree to 1·10⁻⁴¹; f₁ at t = 1 gives 0.5295, 0.5625, 0.6323 (SHG's 0.529, 0.563, 0.632).
- P2 not killed: f₂ and f₃ keep the median at 45° to 7·10⁻⁴⁰ degrees at every ε, their P(v/h ≤ ¼) off the Cauchy's by
  0.007 to 0.070; f₁ moves it by −2.67°, −5.58°, −10.95° at ε = ¼, ½, 1, toward zero.
- P3 not killed: δ₁ = −0.17139·ε; the relative error 3.9%, 2.0%, 1.0%, 0.51% at ε = 0.1 … 0.0125, falling by 1.95,
  1.98, 1.99 per halving.
- P4 not killed: a₀ = −5, 0, 5 change nothing, to 2·10⁻³⁸.
- P5 not killed: weighting by r and r² the shift is δ₁ and 2δ₁ to 0.11% and 0.21% at ε = 0.0125; the arc element's
  median differs from the radius's by 5.3·10⁻⁴ … 8.6·10⁻⁶, falling by 3.89, 3.95, 3.98 per halving.
- P6 not killed: ln ρ less its mean is ε(f − f̄) to an error of 0.181ε² (f₁) and 1.88–1.94ε² (f₃), steady from ε = 0.1
  to 0.0125.

**Reading.** OFS's two ρ are one thing seen twice. A shape's outline, laid by its length, is the density
ρ(θ) = √(r² + r′²)/max on the inscribed sweep's unmoved addresses; the strength ε of the perturbation is how far that
density is from constant, and the circle (the only outline with r² + r′² constant) is the one shape whose density is
constant, which is why it alone reads as the Cauchy both ways. The arrivals' median moves from the corner only by the
part of the shape the exchange reverses, by (ε/2)·[∫_{π/4}^{π/2} f − ∫₀^{π/4} f] to first order, and a radius or an
area as the payload moves it by the same picture, once or twice over. The size a₀ never enters; the shape's modes come
back from ln ρ to O(ε²). The identity at the centre was draw's SMP lab (the walk's arrival density is the arc element);
what is added is reading it as OFS's density and the median's first-order shift.
