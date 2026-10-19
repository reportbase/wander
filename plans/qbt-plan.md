# QBT: the qubit's state and its Bloch point as the two sweeps

*16 October 2026 (Tom's local date). Tom, about 05:02: "does this help quantum, they say quantum world is hard, is this
why?"; then, about 05:04, "yes" to Claude's offer of an exact check. Physics, so for `physics.md`, not OFS (R201).*

## The claim

The two sweeps of OFS §4 ("What each sweep reads") are the qubit's two descriptions:
- the state, a direction (a ray in the space of amplitudes), read at θ like the inscribed sweep;
- the Bloch point, where measured averages live, at 2θ like the central sweep, the state squared.

The match covers several facts that make quantum mechanics feel strange: the half angle, orthogonal states being
antipodal, 720° to return a spin-½, Born's rule as a square, and the duality relation. The complex version is the same
two charts on the Riemann sphere: the ratio of amplitudes is the stereographic chart of the Bloch sphere.

All of this is textbook quantum mechanics (the Bloch sphere, the double cover SU(2) → SO(3), Born's rule, the
Englert–Greenberger–Yasin relation). What is ours is only the reading.

**The bridge.** A state's amplitudes are unit relations: for the real slice, h = |⟨0|ψ⟩| and v = |⟨1|ψ⟩|. Born's rule
carries them to measured frequencies. No amounts.

**Not covered, and not claimed:**
- entanglement and Bell's theorem;
- non-commuting observables beyond one qubit's;
- the measurement problem.

## Predictions (written 16 Oct about 05:10, before any run)

Exact (mpmath, 40 digits), with |0⟩, |1⟩ the basis, the state ψ = (cos θ, e^{iα} sin θ), h = cos θ, v = sin θ, and n
the Bloch vector (⟨σx⟩, ⟨σy⟩, ⟨σz⟩).

- **Q1. The Bloch point is the central sweep.** n = (sin 2θ cos α, sin 2θ sin α, cos 2θ). For the real slice (α = 0),
  n = (2hv, 0, h² − v²), the central sweep's point (OFS §4) laid on a sphere. Checked at 30 (θ, α) pairs.
- **Q2. Born's rule is the foot.** P(0) = |⟨0|ψ⟩|² = h² = (1 + n_z)/2, the foot of the arc's point on the chord.
- **Q3. Ninety degrees in the state is antipodal on the sphere.** For θ₂ = θ₁ + π/2 (same α), ⟨ψ₁|ψ₂⟩ = 0 and
  n₂ = −n₁. More generally |⟨ψ₁|ψ₂⟩|² = (1 + n₁·n₂)/2 for any two states (30 random pairs, seed 3).
- **Q4. The double cover.** Turning the state through β (the real rotation of amplitudes, exp(−iσ_y β)) turns n
  through 2β about the y axis. A turn of β = π gives −ψ with the same n; β = 2π returns ψ. In the usual labelling,
  a Bloch rotation by angle φ is the state rotation exp(−iσ_y φ/2), so φ = 2π gives −ψ and φ = 4π gives ψ (the
  720°).
- **Q5. The complex version is the stereographic chart.** The ratio of amplitudes ζ = ψ₁/ψ₀ = e^{iα} tan θ equals
  the stereographic projection of n from the south pole, (n_x + i n_y)/(1 + n_z). On the real slice ζ = s = v/h, the
  inscribed sweep's reading.
- **Q6. Visibility and predictability, pure and mixed.** For ψ = (1, √a)/√(1 + a), with a ∈ (0, 1) a transmission:
  - the transverse length |n_⊥| = 2√a/(1 + a) is the visibility, |n_z| = (1 − a)/(1 + a) the predictability, and
    |n| = 1 (pure, on the sphere: DUO's foil);
  - for the mixture a chopper makes, ρ = [2a·|+⟩⟨+| + (1 − a)·|0⟩⟨0|]/(1 + a), with |+⟩ = (|0⟩ + |1⟩)/√2, the
    transverse length is 2a/(1 + a), n_z is the same (1 − a)/(1 + a), and |n| < 1 (inside the ball: DUO's chopper).

  Checked at a = 0.05, 0.24, 0.5, 0.9.

*Killed if* any identity is off by more than 10⁻³⁰, or in Q6 the mixture's |n| is not below 1 by more than 10⁻³. A kill
would be my computation or my statement of the textbook result, not quantum mechanics.

## Runs

### Run 1 (16 Oct about 05:15, `runs/qbt/qbt.py`, output in `runs/qbt/run1.txt`)

**Q1–Q6 not killed.** Every identity holds to 7·10⁻⁴¹, and Q5 to 3·10⁻³⁵.

| a | foil visibility | foil predictability | foil \|n\| | chopper visibility | chopper predictability | chopper \|n\| |
|---|---|---|---|---|---|---|
| 0.05 | 0.426 | 0.905 | 1 | 0.095 | 0.905 | 0.910 |
| 0.24 | 0.790 | 0.613 | 1 | 0.387 | 0.613 | 0.725 |
| 0.5 | 0.943 | 0.333 | 1 | 0.667 | 0.333 | 0.745 |
| 0.9 | 0.999 | 0.053 | 1 | 0.947 | 0.053 | 0.949 |

## What it shows

A qubit's state is the inscribed sweep's direction and its Bloch point is the central sweep's, the state squared at
twice the angle. Five things that make a qubit feel strange follow from that one doubling:
- the half angle;
- orthogonal states antipodal;
- −ψ after a 2π state turn (720° of Bloch rotation to return);
- Born's rule as the foot h²;
- the duality relation as the sphere itself.

The complex ratio of amplitudes is the stereographic chart of the Bloch sphere: the address, with a phase. A pure state
lies on the sphere, at its facing, like DUO's foil. A mixture lies inside the ball, at the same predictability, like
DUO's chopper.

All of this is textbook quantum mechanics: the double cover SU(2) → SO(3), the Riemann sphere, Born's rule, and
Englert–Greenberger–Yasin. The reading is ours. It does not touch entanglement, Bell's theorem, non-commuting
observables beyond one qubit, or the measurement problem, so it explains some of quantum mechanics' felt strangeness,
not its hard core.
