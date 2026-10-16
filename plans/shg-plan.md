# SHG: the shape as a perturbation of the unit circle, and why only the circle

*16 October 2026 (Tom's local date). Tom, about 08:37: "The cauchy density paramater shows cauchy at full expression
and no expression. That seems to prove the necessity of the situation"; about 08:42, after Claude's partial reply: "I'm
not persuaded. It shows a profound symmetry, density is the pertibation of a unit circle."; about 08:45, "Yes. How could
you do that with any other shape?" Geometry, exact; for OFS §7.4 if it holds.*

## The claim

Write a shape seen from the reader as a perturbed unit circle, r(θ) = exp(ρ·f(θ)) with f(θ) = Σ aₙ cos(nθ + φₙ):
- ρ = 0 is the circle (the addresses with nothing on them);
- ρ = 1 is the full shape (the archived *Reader Geometry*'s density, "at density = 0 unit circle … at density = 1
  full shape"; OFS keeps ρ for the share met, R274, and this plan writes the perturbation's strength as ρ only here).

1. **The symmetry.** A perturbation moves each point along its own ray, never across, so every direction (address) is
   fixed. The radial maps r ↦ r·e^{g(θ)} form a group, and laid by direction the readings are the same Cauchy at every
   ρ, not only at the two ends. Laid along the shape's own outline, the law moves with ρ.
2. **Why only the circle.** The zero-perturbation shape carries no payload only if its own outline reads evenly in
   direction: equal steps of length along it are equal steps of turn from the reader. The length per unit of turn is
   √(r² + r′²), constant exactly when r² + r′² = c². The solutions are r = c (the circle centred on the reader, the
   central sweep) and r = c·sin(θ + φ) (the circle through the reader, the inscribed sweep). No other shape. So the base
   of the perturbation can only be the circle, and its two solutions are the two sweeps (TWS).
3. **The group as ignorance.** A reader who does not know the shape needs a law of readings unchanged by every radial
   map: only measures on directions alone. With the turns, the even turn; on the drawing V = H, the Cauchy (OFS
   Proposition 5(d)). The perturbations are a third member of the reader's ignorance (Jaynes's method), beside turns and
   rescalings: rescalings are the radial maps with g constant.

Classical pieces: radial (star-shaped) deformations fix directions; the arc length in polar form √(r² + r′²); the ODE
r′² = c² − r² (its singular solution r = c and its general solution c·sin(θ + φ)). What is ours is the reading.

## Predictions (written 16 Oct about 08:50, before any run)

Exact (mpmath, 40 digits). f₁ = 0.3 cos 2θ + 0.1 cos(3θ + 0.4) (lopsided under the flip θ ↦ π/2 − θ), f₂ = 0.25 cos 4θ
(unchanged by the flip), each at ρ = 0, ¼, ½, 1. The reader at the origin; readings v/h = tan θ on the quarter turn
θ ∈ [0, π/2].

- **S1. By direction, the same at every ρ.** Laid evenly in θ, the reading of the point r(θ)·(cos θ, sin θ) is
  y/x = tan θ whatever r, so P(v/h ≤ t) = (2/π)·arctan t at every ρ (checked at t = ¼, 1, 4), to 10⁻³⁰.
- **S2. Along the outline, the law moves.** Laid evenly in arc length on the quarter turn:
  - at ρ = 0 it is the Cauchy (P(v/h ≤ 1) = ½ and P(v/h ≤ ¼) = (2/π) arctan ¼), to 10⁻³⁰;
  - for f₁ at ρ > 0, P(v/h ≤ 1) is off ½ by more than 10⁻³;
  - for f₂ (unchanged by the flip), P(v/h ≤ 1) = ½ to 10⁻³⁰ at every ρ, but P(v/h ≤ ¼) is off the Cauchy's by more
    than 10⁻³ at ρ > 0 (the corner kept, the shape in the ends, as OFS §7.4's table).
- **S3. Only the circles.** The length per unit of turn √(r² + r′²) is constant (spread over 400 directions at most
  10⁻³⁰):
  - for r = c (c = 0.7, 1, 3);
  - for r = c·sin(θ + φ) on its arc (c = 1, 2; φ = 0, 0.3), where it equals c;
  - and for no perturbation: f₁ and f₂ at ρ = ¼, ½, 1 and 20 seeded random f (seed 7, three terms, n ≤ 6, amplitudes up
    to 0.3) give a spread above 10⁻⁶;
  - and r² + r′² = c² is satisfied by these two families to 10⁻³⁰ (the ODE checked).
- **S4. The group.** Radial maps compose by adding g and commute (r·e^{g₁}·e^{g₂} = r·e^{g₂}·e^{g₁}), to 10⁻³⁰. The
  even measure on directions is unchanged by each (the pushed measure of any arc of directions the same, to 10⁻³⁰). A
  measure with a radial part, uniform on the unit disc, is moved: under g = f₁ the share of the disc's mass within
  radius ½ changes by more than 10⁻³.

*Killed if* any check misses its tolerance. S1 and S4 are near identities (a kill is my computation); S2 is OFS §7.4's
table in a new form; S3 is the claim that only the circle works.

## Runs

### Run 1 (16 Oct about 08:55, `shg/shg.py`, output in `shg/run1.txt`; 4 s)

**S1–S4 not killed.**
- **S1.** By direction the reading is tan θ at every ρ and the law is (2/π)·arctan t (to 7·10⁻⁴⁰).
- **S2.** Along the outline the law moves with ρ. For f₁, P(v/h ≤ 1) runs 0.5, 0.529, 0.563, 0.632 at ρ = 0, ¼, ½, 1.
  For f₂, unchanged by the flip, it stays ½ while P(v/h ≤ ¼) runs 0.156, 0.163, 0.168, 0.175. At ρ = 0 both are the
  Cauchy's.
- **S3.** Circles centred on the reader or through it read evenly along their outline (spread 9·10⁻⁴¹; r² + r′² = c²
  holds); the 26 perturbations do not (the least spread 0.124).
- **S4.** Radial maps commute and keep every direction (to 2·10⁻⁴¹); the uniform disc, a measure with a radial part, is
  moved (its share within ½ goes from ¼ to 0.2757).

## What it shows

A shape is a perturbation of the unit circle along the rays, and the perturbations form a group that fixes every
direction. Laid by direction, the readings are the same Cauchy at every strength of the perturbation, not only at
none and full; laid along the shape's outline, the shape enters the law. Only circles read evenly along their own
outline: r² + r′² = c² has two kinds of solution, the circle centred on the reader and the circle through it, the
central and the inscribed sweeps. So the circle is the only base a perturbation can start from with nothing on it,
and it comes with exactly the two sweeps. A reader who does not know the shape needs a law that every radial map
leaves alone, a law on directions only (the rescalings are the radial maps with a constant g). Classical pieces; the
reading is ours.
