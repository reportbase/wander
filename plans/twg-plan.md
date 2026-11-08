# TWG: the Thomas–Wigner rotation read from directions alone

8 Nov 2026. Tom pasted ChatGPT's next step after R758: "test whether the read/write framework can explain the composition
law itself, rather than just redescribe it … make non-collinear boost composition the next calculation … If it does not,
we will have learned exactly where the correspondence ends."

## Known beforehand (stated so the predictions are not mistaken for discoveries)

- Collinear boosts compose by adding rapidities (the hyperbolic addition identities); β = tanh ζ gives the velocity law.
- Boosts act on the celestial sphere as Möbius maps (PSL(2,ℂ) ≅ SO⁺(3,1); Penrose and Rindler 1984). Liouville: every
  conformal map of the sphere is Möbius, so a map of directions that keeps the angles between nearby stars is already a
  Lorentz transformation (the orientation-preserving conformal group of S² *is* the Lorentz group). That conformality is
  the premise, not something the read/write split supplies.
- Non-collinear boosts compose to a boost times a rotation (Thomas 1926, Wigner 1939); the angle is
  tan(Ω/2) = ab·sin φ/(1 + ab·cos φ), a = tanh(ζ₁/2), b = tanh(ζ₂/2), φ the angle between the boosts; for φ = 90°,
  cos Ω = (γ₁ + γ₂)/(1 + γ₁γ₂). Ω is the area of the velocity triangle in hyperbolic space (curvature −1), by Gauss–Bonnet.
- The archived *The Bounded Observer in Motion* (§6) already read Thomas–Wigner as holonomy, a property of a loop of acts,
  and checked the half-rapidity formula to 10⁻¹⁴ in its `tns` demo. The corpus has the matching fact for turns: in space a
  loop of turns about two axes comes home turned by its solid angle (essay 13; `euler.html`'s loop, about α·β; ELM's
  Lie–Trotter leftover).

## What is tested

Whether the rotation is a reading in the paper's sense: recovered from directions alone (no Doppler payload, no
distance), the same from any stars, absent from any single read, present only when two are joined; and how its small-loop
form compares with the turn loop's.

## Predictions (written before the run)

Data: seeded star directions; each observer's apparent directions from the photon four-momenta under the 4 × 4 boosts
(the writer's generator); the reader is given only the directions before and after, put on the stereographic chart.

- W1. Collinear. A boost along n by ζ, fitted as a Möbius map from three stars' directions, has trace 2·cosh(ζ/2) (ζ read
  from directions alone, to 10⁻⁴⁰); two along n compose to ζ₁ + ζ₂, and tanh of it is (β₁ + β₂)/(1 + β₁β₂). On the
  chart centred on n the map is z ↦ e^(±ζ)·z: a slide of ln z, the level of direction (pseudorapidity), by ζ. Kill: any
  mismatch above 10⁻³⁰.
- W2. Non-collinear. Two boosts at φ ∈ {30°, 60°, 90°, 135°} and (ζ₁, ζ₂) ∈ {(0.5, 0.8), (1.5, 2.0), (3, 0.2)}: the Möbius
  map fitted from three stars' directions predicts every other star's direction (20 more, to 10⁻³⁰); its polar
  decomposition's rotation angle equals the half-rapidity formula and, at 90°, the γ formula, to 10⁻³⁰. Kill: a mismatch.
- W3. No single read carries it. One boost's fitted map has rotation angle 0 (to 10⁻⁴⁰), whatever its direction and size.
  Kill: a nonzero angle.
- W4. Any stars. Fitting from five different seeded triples gives the same Ω to 10⁻³⁰. Kill: a spread above it.
- W5. The area. Ω equals π minus the angle sum of the velocity triangle with sides ζ₁, ζ₂ meeting at angle π − φ (third
  side from the hyperbolic law of cosines), to 10⁻³⁰. Kill: a mismatch.
- W6. Against the turn loop. For the small loop b₁b₂b₁⁻¹b₂⁻¹ of boosts by ε along n₁, n₂ (angle φ), and the same loop of
  turns by ε about n₁, n₂: both leave a rotation of ε²·sin φ to leading order (ratio → 1 as ε → 0: within 10⁻² at
  ε = 10⁻², 10⁻⁴ at 10⁻⁴), about axes pointing opposite ways (curvature −1 against +1). Kill: the magnitudes parting, or
  the axes the same way.

## The reading, kept apart

If nothing is killed: collinear rapidity adds because, read on the sky, a boost along one axis is a slide of the level of
direction about that axis, and slides add (the reader's rescaling group, after Jaynes); the velocity law is the writer's
tanh of that sum. Non-collinear boosts slide along different axes; no single chart makes both slides, and joining them
leaves a turn. The turn is read from directions alone, so it is an address quantity, unmoved by any payload; no single
read carries it, so it belongs to the joining (a write, as every join of reads is here). It is the hyperbolic twin of the
turn loop's leftover. What this does not do: derive the Lorentz group from the read/write split. The group enters through
the premise that a change of standpoint by motion is conformal on the sky; given that, the rest is classical. That is
where the correspondence ends.

## Runs

### Run 1 (8 Nov 2026), `runs/twg/twg.py`, output `runs/twg/twg-run1.txt`; W3 killed by my measure

- W1 held: ζ read from three stars' directions to 6·10⁻⁶⁰, collinear boosts summing to 3·10⁻⁶⁰, the velocity law to
  8·10⁻⁶², every other star predicted to 4·10⁻⁵⁹; on the chart centred on the boost the map is z ↦ k·z with ln k = ζ.
- W2 held: twelve cases (φ 30°–135°), the rotation read from directions alone equal to the half-rapidity formula to
  1.2·10⁻⁵⁸ and at 90° to the γ formula to 2·10⁻⁵⁹; 20 more stars predicted to 1.4·10⁻⁵⁸.
- W3 killed in its letter: one read's rotation 6.7·10⁻³⁰ against my 10⁻⁴⁰. My measure: the angle taken as 2·acos of a
  number within 10⁻⁶⁰ of 1 keeps only half the digits (the collinear composition's 4.5·10⁻³⁰ is the same artefact).
- W4 held: five triples agree to 3.7·10⁻⁵⁸. W5 held: Ω is the velocity triangle's defect to 1.2·10⁻⁵⁸.
- W6 held: both loops leave ε²·sin φ (ratios within 5·10⁻⁵ at ε = 10⁻², 5·10⁻⁹ at 10⁻⁴), axes antiparallel (dot product
  −0.99996 and −0.999999998, the departures of order ε²).

W3′ (written before run 2): the rotation of one read, measured as 2·asin of the norm of U's part along the Pauli matrices
(|tr(σₖU)|/2), is below 10⁻⁵⁰ for every boost of W3, and so is a collinear pair's. Kill: either above it.

### Run 2 (8 Nov 2026), the same script with the angle from U's Pauli part, output `runs/twg/twg-run2.txt`; nothing killed

- W3′ held: one read's rotation at most 1.5·10⁻⁵⁹ (nine boosts, three sizes, three directions); a collinear pair's
  9·10⁻⁶⁰. Every other check as in run 1, now to 10⁻⁵⁸ or better (the half-rapidity formula to 5·10⁻⁶⁰).

Reading: the Thomas–Wigner rotation is recovered from three stars' directions before and after, with no frequency and no
distance, the same from any three, and equal to the velocity triangle's hyperbolic area. One read (one boost) carries
none; collinear boosts share their fixed points and slide one level of direction, so their rapidities add and no turn is
left; boosts along two axes cannot be one slide, and the joining leaves a turn. For a small loop it is ε²·sin φ, the turn
loop's size about the opposite axis: the same leftover of joining in space, with curvature −1 against +1. All classical
(Thomas 1926; Wigner 1939; Penrose and Rindler 1984; the archived *Bounded Observer in Motion* §6). What is ours: the
rotation is an address quantity, read from directions, and belongs to the joining of reads, never to one. The Lorentz
group itself is not derived from the read/write split; it enters as the premise that a change of standpoint by motion is
conformal on the sky (Liouville), which is where the correspondence ends.

## Run 3 predictions (8 Nov 2026, written before the run; the next order of the small loops)

ChatGPT, pasted ("TWG run 3, analytic prediction"), from W6's conventions (turn exp(−iθ n·σ/2), boost exp(ζ n·σ/2), loop
g₁g₂g₁⁻¹g₂⁻¹, the residual the polar decomposition's turn). Known beforehand and not counted as tests: run 2's ratios at
φ = 60° and 90° (c_B ≈ 0.458 and 0.333, c_T ≈ −0.083), from which these coefficients could have been fitted.

- W7. Turn loop, exact: cos(Ω_T/2) = 1 − 2·sin⁴(ε/2)·sin²φ, so Ω_T = 4·arcsin(sin²(ε/2)·|sin φ|), to 10⁻⁵⁰ at every φ
  and ε tried. Hence Ω_T = ε²·sin φ·(1 − ε²/12 + O(ε⁴)): c_T = −1/12 whatever φ.
- W8. Boost loop: Ω_B = ε²·sin φ·(1 + c_B·ε² + O(ε⁴)) with c_B(φ) = 1/3 + cos φ/4. Tested at angles not seen before,
  φ = 30°, 45°, 120°, 150° (and 60°, 90° as checks): (Ω_B/(ε² sin φ) − 1)/ε² within 10⁻⁶ of c_B at ε = 10⁻⁴, and its
  departure from c_B shrinking as ε² (ratio of departures at ε = 10⁻³ and 10⁻⁴ near 100). Kill: either fails.
- W9. The difference c_B − c_T = 5/12 + cos φ/4, angle-dependent for boosts, constant for turns. Follows from W7, W8.

Reading if nothing is killed: the two loops share their leading term and part at the next, the turn loop's correction the
same at every angle, the boost loop's depending on it. The boost construction assumes the Lorentz group, so this compares
two geometries; it derives nothing.

### Run 3 (8 Nov 2026), `runs/twg/twg3.py` (90 digits), output `runs/twg/twg-run3.txt`; nothing killed

- W7 held: the turn loop's residual equals 4·arcsin(sin²(ε/2)·|sin φ|) to 4·10⁻⁹⁵ at six angles and three ε; c_T = −1/12
  to 1.3·10⁻¹⁰ at ε = 10⁻⁴, the same at every angle.
- W8 held: c_B within 10⁻⁹ of 1/3 + cos φ/4 at ε = 10⁻⁴ at the four fresh angles (30°: 0.5498397, 45°: 0.5101100,
  120°: 0.2083333, 150°: 0.1168270) and at 60° and 90°; the departure falls by 100.0 from ε = 10⁻³ to 10⁻⁴, as ε².
- W9 follows: the boost loop's correction depends on the angle, the turn loop's does not.

The coefficients were derived by ChatGPT and checked here, not derived here. The loops share ε²·sin φ (opposite axes) and
part at the next order; a comparison of two geometries, the Lorentz group assumed in the boost one.
