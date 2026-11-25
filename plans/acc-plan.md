# ACC: an accelerated mass, a look and a pull

25 Nov 2026; Tom: "Merge. Proceed on gravity thread". *Reads and Writes* §7, "Gravity on the stage", open item (4):
MVM did a mass in uniform motion and LDL light's delay past a lens; what is left is accelerated masses. Exact
arithmetic and 40-digit numerics, no data. A pull is not a read (R1183); what is sorted is what each points at.

## Set-up

A point source at rest at the origin at the moment t = 0 and accelerating there: z(t) = ½·a·t²·ŷ (its velocity zero at
t = 0, so MVM's order-β² departure is absent and only the acceleration speaks). A place x₀ = (X, Y, 0) at rest, read at
t = 0; r = |x₀|, n = x₀/r, c = 1, the light-time T = r. The dimensionless size is ε = a·r/c².
- **The look**: the light arriving at x₀ at t = 0 left the source at t_r with r(t_r) = |x₀ − z(t_r)| = −t_r; the look
  points at z(t_r).
- **A charge's pull** (an opposite test charge at rest at x₀): the exact Liénard–Wiechert field of the prescribed motion,
  force −E.
- **The pull** (a test body at rest at x₀): linearized general relativity with the source's own Liénard–Wiechert-form
  potential, h̄^μν = 4GM·u^μu^ν/ρ at the retarded point (ρ = γ(R − v·R), u = γ(1, v)), h_μν = h̄_μν − ½η_μν·h̄,
  acceleration −Γⁱ₀₀ = ½∂ᵢh₀₀ − ∂₀hᵢ₀, first order in G. **Premise, stated:** an accelerated point mass alone does not
  conserve its stress-energy; what accelerates it (a rope, a rocket's exhaust, a second body) is left out, and its own
  field would add to the pull. So this is the field of the mass's own motion, prescribed, not a whole solution.

## What I worked out by hand before writing this (said, so the predictions are not blind)

Expanding the retarded potentials to order 1/c² for a source momentarily at rest (the standard harmonic-gauge 1PN
metric, g₀₀ = −1 + 2V, g₀ᵢ = −4Vᵢ, V and Vᵢ expanded with the superpotential Gm·r): a body at rest is accelerated by
−GM·n/r² + (GM/c²r)·(7/2·a + ½(a·n)·n). For the charge, the same expansion of Liénard–Wiechert gives the force on an
opposite charge toward the source plus (qQ/c²r)·½(a + (a·n)·n) (textbook, Jackson's problem on the Darwin terms, from
memory). The coefficients are mine from the expansion; the runs check them against the exact retarded fields.

## Predictions (committed before any code)

- **A1 (the look).** The look points at the retarded place z(−T) = ½·a·T²·ŷ (to first order in ε, T = r): its angle
  from the present place is ½·ε·sin ψ to first order, ψ the angle between a and n.
- **A2 (a charge's pull).** The exact force on an opposite charge departs from the present place by ½·ε·sin ψ to first
  order, toward the acceleration: the look and the charge's pull point at the same place, to first order in ε.
- **A3 (the pull).** The exact linearized pull departs from the present place by (7/2)·ε·sin ψ to first order, toward the
  acceleration: seven times the look's. With an acceleration along n (ψ = 0) no direction departs, only the strength.
- **A4 (scale).** Scaling every length and time by k (accelerations by 1/k) leaves ε, and so every direction of A1–A3,
  unmoved; the strengths move by 1/k² (amounts).
- **A5 (what a direction gives).** At rest all three directions are one; for a source at rest but accelerating, the look
  and a charge's pull still agree (to first order), and the pull of gravity parts from them by 3ε·sin ψ: it points at a
  place (7/2)·a·T² along a, the look and the charge's pull at ½·a·T², where the source will be one light-time later.

Checks: each first-order coefficient read as the departure over ε at ε = 10⁻³, 10⁻⁴ and 10⁻⁵, at ψ = 30°, 60°, 90°;
kill if it differs from ½, ½ or 7/2 by more than 10·ε (the next order) at the smallest ε, or if A4 moves a direction past
10⁻²⁰.

## Runs

### Run 1 (`runs/acc/acc.py`, output `runs/acc/acc-run1.txt`)

Nothing killed. The departure from the present place over ε·sin ψ, at ε = 10⁻³, 10⁻⁴, 10⁻⁵ and ψ = 30°, 60°, 90°:
- **A1 not killed**: the look 0.49979, 0.49998, 0.499998 at ψ = 30° (0.5000000 at 90°), toward the acceleration.
- **A2 not killed**: a charge's pull the same to within 10⁻⁶ at ε = 10⁻³ and 10⁻¹⁰ at 10⁻⁵ (0.4999978351 against the
  look's 0.499997835 at ψ = 30°, ε = 10⁻⁵).
- **A3 not killed**: gravity's pull 3.5076, 3.50076, 3.500076 at ψ = 30°, 3.5000026, 3.5000000 at 90°: the coefficient
  7/2, its next order inside 10·ε. With a along n (ψ = 0) no direction departs.
- **A4 not killed**: lengths and times by k = 5 and 100 move no direction past 1.4·10⁻⁴¹; both strengths move by
  exactly 1/k².
- **A5 not killed**: so a source at rest and accelerating is looked at and pulled by an opposite charge toward one place,
  ½·a·T² along a (where it will be a light-time later, and where the light left, to this order), and pulled by its
  gravity toward a place seven times as far along a, (7/2)·a·T². The look and the charge's pull agree to second order
  too (they part by about ε², 10⁻⁶ at ε = 10⁻³), not predicted.

Reading: as with uniform motion (MVM), a look and a pull, one direction at rest, part; here the look and an
electric pull stay together and gravity's parts from both, by an amount of the acceleration times the distance over c²,
unmoved by scaling. The premise stands as stated: an accelerated mass needs something to accelerate it, whose own field
is left out, so the 7/2 is the moving mass's part of a pull, not a whole solution. Classical (the 1PN, Einstein–Infeld–
Hoffmann terms; the 7/2 from memory and my expansion, confirmed here against the exact retarded field), the sorting ours.

### Run 2, predictions (committed before its code; Tom: "1 then 3")

Run 1 left out what accelerates the mass. Here the whole first post-Newtonian field of a pair, each mass accelerated by
the other's pull, so the "rope" is gravity itself and nothing is left out at this order. The metric is the
harmonic-gauge 1PN metric (Blanchet and Damour's form, from memory: g₀₀ = −1 + 2V − 2V², g₀ᵢ = −4Vᵢ, gᵢⱼ = δᵢⱼ(1 + 2V),
c = 1), V and Vᵢ the retarded potentials of the conserved source σ = Σ m_A(1 + (3/2)v_A² − U_A)·δ, σᵢ = Σ m_A v_A·δ,
U_A the Newtonian potential of the other masses at A; V's retardation expanded to the order needed (the superpotential
½∂ₜ²Σ G m_A r_A). A test body at rest at the place: d²xⁱ/dt² = −Γⁱ₀₀.

- **B1 (the 7/2 survives).** The source accelerations enter the test body's acceleration only as
  Σ_A (G m_A/r_A)(7/2·a_A + ½(a_A·n_A)·n_A), ACC's term for each mass, whatever a_A is; the partner's own field adds
  terms in G² (the −2V² and the −U_A in σ) and in the velocities, none with an acceleration (exact, sympy: the
  coefficient of every component of a_A).
- **B2 (against the textbook).** The whole expression equals the Einstein–Infeld–Hoffmann equation's limit for a test
  body at rest (v = 0, its mass to zero), term by term (exact, sympy; the EIH form as I remember Wikipedia's, so a
  failure may be my memory, to be said if it happens).
- **B3 (scale).** For a circular pair, lengths × k and masses × k (velocities unchanged, the orbit the same shape in
  light-times) leave the direction of the test body's 1PN acceleration unchanged to 10⁻²⁵ and its size moved by 1/k.

Kill: B1 or B2 not an identity in sympy; B3 a direction moved past 10⁻²⁵.
