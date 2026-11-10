# SRB: the bridge from observer geometry to special relativity

*10 November 2026, SPN R790. Tom, pasting a recommendation: "The next step is to test the bridge from observer geometry
to special relativity—not to revise Reads and Writes again." Three steps: (1) derive the Lorentz boost and the Doppler
law from the observer side, not restate them; (2) find exactly what survives between standpoints, keeping the Cauchy's
height apart from the Lorentz factor; (3) demand a discriminating prediction, one not already guaranteed by special
relativity, with what would support it and what would count against it stated first. "I would keep this as a separate SR
investigation rather than reopening the synthesis paper." Nothing here goes into Reads and Writes until it has survived.*

*Exact arithmetic (sympy) and 50-digit numerics (mpmath). Scripts in `runs/srb/`. Predictions written and committed
before any script.*

## Known beforehand

- **SRA** (`plans/sra-plan.md`, runs 1–3): aberration is the Möbius map tan(θ′/2) = tan(θ/2)/k, k = e^η, on the
  stereographic chart; a uniform sky boosted is the spherical Cauchy (Kato and McCullagh 2020) with ρ = tanh(η/2), the
  wrapped Cauchy in 2 + 1; the address density is D²; beaming's D⁴ = D² of address × D² of payload. **[classical, checked]**
- **TWG** (`plans/twg-plan.md`): the Thomas–Wigner rotation read from three stars' directions alone; collinear rapidities
  add as slides of the pseudorapidity; the Lorentz group "enters with the premise that a change of standpoint by motion
  keeps the angles between nearby stars" (conformality on the sky; every conformal automorphism of S² is Möbius). The
  correspondence was never a derivation of the group. **[classical, checked]**
- **MOT run 3, EMC:** β = sin θ = tanh ζ, celerity tan θ = sinh ζ, γ = cosh ζ; the three rulers. **[classical]**
- **FRG** (`plans/frg-plan.md`): the Cauchy family's Fisher metric (dm² + dγ²)/(2γ²), KL 2·ln cosh(d/2), d the Poincaré
  distance. **[classical, checked]**
- **Classical:** PSL(2, ℂ) ≅ SO⁺(3, 1) through X = [[t + z, x − iy], [x + iy, t − z]] ↦ M X M† (Penrose and Rindler 1984);
  the Galilean aberration tan θ′ = sin θ/(cos θ + β) (a moving observer, light at speed c in the sources' frame); cross
  ratios of four points are Möbius-invariant.

So steps 1 and 2 are mostly settled already as mathematics. What this plan adds is to say exactly which premise does the
deriving, what the observer-side data determine without any unit, and where γ and the Cauchy height part. Step 3 is the
new question.

## Premises named

- **(C) Conformal sky.** A change of standpoint by motion maps the sky (directions) to the sky by an orientation-preserving
  bijection that keeps the angle between any two nearby directions.
- **(N) Null directions.** Each direction read is the direction of a null ray, a line through the origin of a 4-dimensional
  real vector space with a quadratic form of signature (+, −, −, −), and a change of motion is a linear map of that space.
- **(P) Phase.** A payload's frequency ratio between standpoints is the ratio of the counts of wavecrests per tick, with
  the wave's phase the same number at every event.

(C) is about reads joined; (N) and (P) are not readings at all. Naming them is the point: where the derivation needs (N)
or (P), it has left the observer's geometry.

## Predictions

### Step 1: the boost and the Doppler law

**B1 (aberration from (C) alone).**
- (a) A Möbius map of the sphere (the conformal orientation-preserving maps, by (C)) that fixes the forward and backward
  directions and commutes with every turn about the axis is, in the stereographic chart from the forward pole, z ↦ λz
  with λ real and positive. Shown symbolically.
- (b) Written in angles, λ = 1/k gives exactly cos θ′ = (cos θ + β)/(1 + β cos θ) with β = (k² − 1)/(k² + 1) = tanh(ln k).
  Symbolic identity.
- (c) These maps form a one-parameter group, k₁ then k₂ giving k₁k₂, so ln k adds and β composes as
  (β₁ + β₂)/(1 + β₁β₂). Symbolic.
- (d) The Galilean aberration is not conformal: at β = 0.6 the ratio of its stretch along the meridian to its stretch
  across, over a grid of θ in (0, π), departs from 1 by more than 0.1 somewhere; the Lorentz aberration's ratio is 1 to
  10⁻⁴⁰ everywhere.
- *Killed* if (a)–(c) fail as identities, or (d) finds the Galilean map conformal or the Lorentz one not.

**B2 (the Doppler factor is the sky map's own stretch).**
- The linear stretch of the sky map at the image direction θ′, the factor by which a small angle between two nearby
  directions is multiplied, equals 1/D(θ′), D = √(1 − β²)/(1 − β cos θ′), the same in every direction at that point. To
  10⁻⁴⁰ at 10³ seeded (θ, φ) and β ∈ {0.1, 0.6, 0.99}. (Its square is SRA A3's D².)
- So D is fixed by the directions alone, as the stretch of the map that joins two reads: a place, with no unit.
- That the frequency ratio equals this D is (P), not a reading: directions alone fix D as a stretch and say nothing about
  what the payload does under it. Stated, not tested.
- *Killed* if the stretch is not isotropic or not 1/D.

**B3 (the boost matrix from the sky map, given (N)).**
- Given the sky map as an element M of SL(2, ℂ) (determined up to sign by three stars, TWG), the linear map
  X ↦ M X M† on Hermitian matrices is a Lorentz transformation Λ (det X kept), and for M = diag(k^{1/2}, k^{−1/2}) it is
  exactly the boost along z with cosh η = (k + 1/k)/2, sinh η = (k − 1/k)/2. Symbolic.
- Λ is dimensionless: it acts on (t, x, y, z) only once t is written in the units of x, which needs c carried in: a write.
  So from three stars' directions joined, the full Lorentz transformation is determined as a place; its action on events
  in metres and seconds is a write.
- (N) is used here and not before: B1 and B2 need only (C).
- *Killed* if the symbolic identity fails.

### Step 2: what survives

**B4 (what is unmoved between standpoints).**
- (a) The cross ratio of four stars is unchanged by any sky map, to 10⁻⁴⁰ at 100 seeded maps and quadruples.
- (b) The rapidity η is the Poincaré distance between the two skies' standpoints: the uniform sky's standpoint at the
  ball's centre, the boosted one at ρ = tanh(η/2) (SRA A2), distance 2·artanh ρ = η, to 10⁻⁴⁰.
- (c) γ is not a height. In 2 + 1, with the motion's two directions at 0 and ∞ of the half-plane chart t = tan(θ/2), the
  rest sky's standpoint is at i and the boosted one at i/k: its Cauchy height is e^(−η), the reciprocal of the forward
  Doppler factor, and γ = cosh η = cosh(d_P), the cosine of the hyperbolic distance. Height = γ only at η = 0. Exact.
- (d) KL between the rest circle sky and the boosted one is 2·ln cosh(η/2), to 10⁻³⁰ by quadrature at η ∈ {0.3, 1, 3};
  per small η it is η²/4, the Fisher metric dη²/2 along the boost.
- *Killed* if (a)–(d) fail, or if the boosted standpoint's height equals γ at any η > 0.

**B5 (the sphere, exploratory).** KL between the uniform sphere and the spherical Cauchy at ρ = tanh(η/2), at
η ∈ {0.1, 0.3, 1, 3}. Predicted only that it depends on η alone (not on the axis) and grows as cη² for small η, c
reported. No closed form predicted, so nothing here can be killed but the axis-independence.

### Step 3: a discriminating prediction

**B6 (the criterion, and what is expected).**
- A discriminating prediction must (i) follow from the read/place/write framing and its premises, (ii) give a number or a
  sign special relativity does not already fix, and (iii) be checkable against a calculation or data where a stated
  outcome would count against it.
- **Expected outcome, stated before the search: none on special relativity's own ground.** Under (C) the sky maps are
  exactly the Lorentz group (B1, B3), so every statement about directions, their joins and their stretches is a theorem of
  special relativity; the framing can only sort those statements (read, place, write), not add one. A result that differs
  from special relativity in a tested regime would count against the framing, not against relativity.
- Candidates to be examined, each sorted as (A) a consequence of special relativity, (B) a premise rather than a
  prediction, (C) statistics rather than physics, or (D) discriminating:
  1. the Doppler factor fixed by directions alone (B2);
  2. the full Lorentz transformation from three stars with no clock (B3, TWG);
  3. a census's dipole 2β from directions alone (Ellis and Baldwin 1984; EBD);
  4. the rapidity estimated from N directions of a sky taken as uniform in its own frame: the median of the
     pseudorapidity, its efficiency against maximum likelihood (the logistic's ¾ is predicted);
  5. what an observer can determine with no unit: rapidity, axis, the Thomas–Wigner turn, every ratio of proper times
     exchanged by signals; never a speed in metres a second.
- *The expectation is killed* if any candidate lands in (D). Then that candidate gets its own plan with its prediction.
- If none does, the verdict is that the bridge is an interpretation of known structure, sharp about which premise carries
  the Lorentz group ((C)) and where units enter ((N) with c, (P)), and not a source of new relativistic predictions.

## Runs

