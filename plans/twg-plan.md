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
