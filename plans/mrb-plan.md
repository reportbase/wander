# MRB: five hundred marbles, contact counted from inside

*Plan, predictions and kills written 12 October 2026, before any script existed (Claude; Tom: "what about something a
little different, a huge collection of marbles, say 500? would this be helpful?", then "both", to a physics test and a
game). A simulation of our own checked against exact kinetic theory: evidence about the engine and about how a reader may
count, not about the physical world (`papers/physics.md` §2.4, the standing POL runs 11–18 and CUE have). The lab rules
hold: nothing above the "Runs" line is edited after the run; later runs write their predictions in the Runs section
before they run, as POL's did.*

## Why marbles, after pool

POL played up to sixteen balls on a table and a gas of 13,581 discs in two dimensions, every contact elastic or nearly so.
Five hundred marbles in three dimensions add what pool never needed:

1. **Contacts that lose energy, many times over.** Each marble meets the others hundreds of times. With restitution e < 1
   the gas cools, and how it cools is known exactly (Haff's law, below). This is part 1.
2. **Contacts that last.** A heap of marbles at rest has every marble touching its neighbours all the time. In the pair's
   readings that is h + v = 1 held, not crossed. An engine that finds contacts one at a time, as POL's does, can only
   reach rest through infinitely many contacts in a finite time (inelastic collapse: a ball bouncing to rest on a floor
   makes infinitely many bounces in a time 2v₀/(g(1 − e))). Part 2, with its own predictions written later, holds contact
   as a state: the heap, its weight carried along chains of contacts, and whether a reader can hold the far part of a
   heap as totals (POL runs 11–18's question, for a static load).
3. **The game**, on part 2's engine: shooting into a heap of 500, played from the same frames, with sound.

## What was derived before writing this (disclosed)

From kinetic theory, worked out here before the plan; none of it is new.

- **Haff's law.** For N smooth inelastic spheres of diameter σ and mass m, with no gravity, a two-body contact with
  closing speed g_n (the relative velocity along the line of centres) removes (1 − e²)·m·g_n²/4 of kinetic energy. With
  the granular temperature T = m⟨|v|²⟩/3, molecular chaos and a Maxwellian, the colliding pairs have ⟨g_n²⟩ = 4T/m, so
  **each contact removes (1 − e²)·T on average**, and with nω/2 contacts per unit volume and time (ω the contacts per
  marble per unit time) the energy (3/2)nT falls as dT/dt = −(1 − e²)ωT/3. With Enskog's ω = 4√π·n·χ·σ²·√(T/m) this
  integrates to Haff's law, T(t) = T₀/(1 + t/τ)², 1/τ = (1 − e²)ω₀/6.
- **The same law counted in contacts.** Write C for the contacts per marble so far (twice the number of contacts over N).
  Then dC/dt = ω, and the law becomes **ln T(C) = ln T(0) − (1 − e²)·C/3**: T falls by the factor e^(−(1−e²)/3) per contact
  per marble. Counted so, the density n, the diameter σ, the pair correlation at contact χ and the clock all cancel; only
  e is left. In the referee's clock they do not: T^(−1/2) rises linearly in t at the rate (2/3)√π·n·χ·σ²·(1 − e²)/√m.
- **The second-order correction, known.** The cooling gas is not quite Maxwellian. Its fourth cumulant a₂ is
  16(1 − e)(1 − 2e²)/(9 + 24d − e(41 − 8d) + 30(1 − e)e²) in d = 3 (van Noije and Ernst, 1998, from memory), and
  multiplies the cooling rate by (1 + 3a₂/16) and the contact rate by (1 − a₂/16) (Brilliantov and Pöschel's book, from
  memory). Per contact the slope is then (1 − e²)/3 × (1 + 3a₂/16)/(1 − a₂/16), less than 0.4% from the plain one at the
  e used here. The predictions include it.
- **Where the homogeneous state ends** (the clustering instability, Goldhirsch and Zanetti 1993; McNamara and Young; the
  shear-mode threshold of Brey and others, all from memory). In the cooling frame a shear flow of wavenumber k grows if
  ζ/2 > νk², ζ the cooling rate and ν the kinematic viscosity. With the dilute viscosity (5/16σ²)√(mT/π) and Enskog's
  density factors for the viscosity and for ζ, the smallest box mode, k = 2π/L, grows when L exceeds
  L_c ≈ 10.8·ℓ₀/√(1 − e²) × √(ν_E/ν₀ · 1/χ) (ℓ₀ = 1/(√2·π·n·σ²)). Per contact the growth rate is
  λ = (1 − e²)/6 × (1 − (L_c/L)²). My estimate, worth ±20% (the dilute viscosity, elastic transport coefficients):
  at φ = 0.3, L/L_c ≈ 0.55 for e = 0.95 and ≈ 1.5 for e = 0.5; at φ ≤ 0.15 and e ≥ 0.7, L/L_c ≤ 0.8.

What is known to be uncertain and is not predicted: whether, when and where five hundred marbles in three dimensions
undergo inelastic collapse at e = 0.5. I cannot derive it, so P5 below claims only the safe side.

## Keep the case

- σ, m, the box's side L, positions, the clock t and the temperature T are **amounts**, in the gas's own units (σ = 1,
  m = 1). They enter only the clock's prediction (P2), with the referee's density.
- e is a pure number. C is a count. **The per-contact law involves no amount and needs no bridge**: a marble that counts
  its contacts and reads speeds in its own size needs nothing else to know how fast its world cools.
- Each marble reads another as v = r_b/d and is told the other's reading h = r_a/d. Contact is h + v = 1, found as an
  exact moment in each marble's own units, as in POL run 9. Equal marbles touch at the corner h = v = ½. The event
  queue's clock is the one unsituated thing, named here as in POL.
- T as used here is a **total** (an average over all 500 marbles), not any one marble's reading.

## The model

- **The gas.** N = 500 marbles, σ = 1, m = 1, in a periodic cube of side L set by the packing fraction
  φ = Nπσ³/(6L³). No gravity, no rotation, no friction: smooth spheres, so a contact changes only the velocity along the
  line of centres: Δv_a = −(1 + e)/2·(g·n̂)n̂.
- **Event-driven**, exactly as POL's contacts: each pair's next moment of h + v = 1 from a quadratic, a queue of
  contacts and cell crossings, a marble's events discarded once it has moved on. No tick.
- **Start.** 500 of the 512 sites of a simple cubic lattice, chosen at random; Gaussian velocities, total momentum zero,
  T = 1; then elastic (e = 1) for 20 contacts per marble to melt the lattice and reach the equilibrium structure. Then
  e is set, and C and t are counted from that moment.
- **Read**, every 0.25 contacts per marble: C, t, T, and the box-scale flow:
  R = (1/6)·Σ_k |Σ_i v_i e^(−ik·r_i)|² / Σ_i |v_i|² over the six smallest wavevectors k = ±2π/L along each axis. With
  the velocities uncorrelated from place to place R is 1 on average (each mode carries its share); a flow on the scale of
  the box makes it grow, up to N/6 if every marble moved with one wave.
- **Fits.** Over C from 5 to 5 + 3·ln(100)/(1 − e²) (two decades of T past the first five contacts, which let the gas
  settle into its cooling state): the least-squares slope of −ln T against C (P1), and of T^(−1/2) against t (P2), each
  per seed; four seeds per condition, the mean reported with the spread.
- **Collapse guard.** A marble meeting the same partner 100 times in a row is inelastic collapse; the run stops and
  records the C, the t and the marbles.

## Predictions

The conditions: φ = 0.1 with e = 0.95, 0.9, 0.8, 0.7, and e = 0.9 with φ = 0.05 and 0.15. That makes six; P4 adds two
at φ = 0.3. Computed from the formulas above before any run:

| φ | e | per contact: −d ln T/dC | contacts per halving of T | clock: d(T^−½)/dt |
|---|---|---|---|---|
| 0.05 | 0.9 | 0.06310 | 10.98 | 0.02431 |
| 0.1 | 0.95 | 0.03242 | 21.38 | 0.02862 |
| 0.1 | 0.9 | 0.06310 | 10.98 | 0.05572 |
| 0.1 | 0.8 | 0.11962 | 5.79 | 0.10562 |
| 0.1 | 0.7 | 0.17006 | 4.08 | 0.15002 |
| 0.15 | 0.9 | 0.06310 | 10.98 | 0.09661 |

(χ from Carnahan and Starling's (1 − φ/2)/(1 − φ)³: 1.1372, 1.3032, 1.5062 at φ = 0.05, 0.1, 0.15.)

- **P0 (the engine, against equilibrium).** During the elastic melt, past its first 5 contacts per marble, the contacts
  per marble per unit time are within 2% of Enskog's 4√π·n·χ·σ²·√(T/m) at every φ (an exact relation given the pair
  correlation at contact, here Carnahan–Starling's). *Killed* if any φ is 2% or more off.
- **P1 (Haff's law per contact: only e).** At each of the six conditions the mean per-contact slope is within 3% of the
  table's. *Killed* if any is 3% or more off.
- **P2 (Haff's law in the clock: the density enters).** At each of the six conditions the mean clock slope is within 3% of
  the table's, and Haff's form holds: the clock slope over the last third of the fit's range is within 5% of that over the
  first third. *Killed* if either fails anywhere.
- **P3 (the count does not see density, the clock does).** At e = 0.9, from φ = 0.05 to 0.15, the per-contact slopes agree
  within 3% (largest over smallest), while the clock slopes rise by Enskog's factor n·χ, 3.974, the measured ratio within
  5% of it. *Killed* if either fails.
- **P4 (where a total stops being enough).** At φ = 0.3 (L/ℓ₀ = 24.3), with e = 0.95 R stays below 4 up to C = 60; with
  e = 0.5, R exceeds 20 before C = 60 (about a quarter of the energy in the six box-scale modes). *Killed* if either fails.
  If the e = 0.5 run collapses before C = 60 with R still below 20, P4's second half is recorded as not tested, not as
  passed or killed.
- **P5 (the engine survives where the gas stays even).** None of the six conditions' 24 runs, nor the e = 0.95 runs at
  φ = 0.3, trips the collapse guard before its fit's range ends. *Killed* if any does. The e = 0.5 runs are recorded as
  they come out (not predicted).

## What would follow

- P1–P3 not killed: in this gas a reader counting its own contacts reads the cooling from e alone, while the clock needs
  the density and the pair correlation (the reach), the per-contact form of "the reach cancels" (SPN §4.3) on a known
  law. A reading, unruled.
- P4 not killed: the homogeneous state, held as one total (T for the whole box), stops being enough past a size set by
  ℓ₀/√(1 − e²); the box's largest level then carries structure of its own. That is level of detail failing from the
  coarse side, as POL run 18 found it failing for a signal on its way.
- Collapse at e = 0.5 (if seen): the one-contact-at-a-time engine meeting a held contact. Part 2's subject.

## Runs
