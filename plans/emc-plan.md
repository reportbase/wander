# EMC: E² = (pc)² + (mc²)² through the corner

*11 October 2026. Tom: "so lets talk about how the corner helps understand the known equation", then "yes" to writing it
up with predictions first. Exact arithmetic (rationals where the numbers are rational) and the complex step. Predictions
written before the script (`runs/emc/emc.py`) exists. It follows MOT run 3 (`plans/mot-plan.md`), whose P17 already has the
energy's level-slope, β², halfway at the corner.*

## Set-up, with the case kept

**Amounts:** an energy E, a momentum p, a mass m and the constant c. c is the bridge: it makes the momentum and the mass
into energies, pc and mc².

**Unit relations:** dividing by E gives v = pc/E and h = mc²/E, two unit relations read against one unit, so
v² + h² = 1. The reading v/h = pc/mc² = x is the celerity. The pair (pc, mc²) has its corner at x = 1.

**A second pair,** the light-cone energies (E + pc, E − pc). Their reading (E + pc)/(E − pc) is the square of the
particle's Doppler factor, and a boost acts on it.

## Predictions

- **P1. The energy relation is the unit circle of (pc, mc²), and its unit relations are β and the clock's rate.**
  - The particle's speed is u = dE/dp, taken by complex step from E(p) alone, never from a formula for speed. Its
    β = u/c equals v = pc/E.
  - Over 10⁴ states built from Pythagorean triples (pc, mc², E all rational), v² + h² = 1 exactly, and
    √(1 − β²) = h = mc²/E exactly. That makes h = 1/γ = dτ/dt: a moving clock runs at the rest share of its energy.
  - **Killed if:** u/c misses pc/E by more than 1e-12 over 0.001 ≤ x ≤ 1000; or any rational identity fails.
- **P2. The sweep's three landmarks are three named cases.**
  - Home (v = 0, h = 1) is E = mc²; the horizon (h = 0, v = 1) is E = pc.
  - At the corner, pc = mc², β = 1/√2, E = √2·mc², and the kinetic energy is T = (√2 − 1)·mc². With CODATA 2018's
    rest energies (electron 0.51099895000 MeV, proton 938.27208816 MeV), that is 0.2116605 MeV for an electron and
    388.6430 MeV for a proton.
  - **Killed if:** any of these misses its closed form by more than 1e-12 (relative).
- **P3. Newton and the ultra-relativistic limit are flips of each other, handing over at the corner.**
  - Newton's form is E_N = mc² + p²/(2m). The ultra-relativistic form is E_U = pc + (mc²)²/(2pc). Swapping pc and mc²
    turns each into the other.
  - With relative errors e_N(x) = E_N/E − 1 and e_U(x) = E_U/E − 1, predicted: e_N(x) = e_U(1/x) at every x. Newton's
    form is the better exactly when x < 1, and they are equal at the corner, each √(9/8) − 1 = 0.0606602 high.
  - **Killed if:** e_N(x) and e_U(1/x) differ by more than 1e-12 over 0.001 ≤ x ≤ 1000; or the better form is ever the
    other one off the corner; or the corner's error misses √(9/8) − 1 by more than 1e-12.
- **P4. Mass is the corner of the light-cone pair; that is why it is the same for every observer.**
  - The pair's level-midpoint is ½[ln(E + pc) + ln(E − pc)] = ln mc². A boost with Doppler factor k_b sends E + pc to
    (E + pc)/k_b and E − pc to k_b·(E − pc): a pan in levels, both ends the same number of levels in opposite
    directions, with the midpoint fixed. Pans compose by multiplying their Doppler factors: rapidities add.
  - Within one frame, by contrast, the circle's shares v and h change under a boost; only the light-cone pair's
    midpoint does not.
  - The boost with k_b = (E + pc)/mc² brings E to its least, mc²: rest, the light-cone pair at its corner, where
    E + pc = E − pc.
  - **Predicted over 10⁴ random rational states and rational boosts** (k_b rational, so β_b and γ_b are rational), with
    the boost taken from the Lorentz transformation of (E, pc), not from the pan:
    - every identity above holds exactly;
    - two boosts in a row equal one with k₁k₂;
    - E′ ≥ mc², equal only at k_b = (E + pc)/mc².
  - **Killed on any inexact identity, or E′ < mc² anywhere.**

Known already: the energy–momentum relation; u = dE/dp; the Newtonian and ultra-relativistic limits; light-cone
coordinates, whose product p⁺p⁻ is the mass squared; rapidity's additivity. What EMC adds is the reading: one circle
read in one unit, home and horizon as E = mc² and E = pc, the two limits as flips of each other handing over at the
corner, and mass as the corner of the light-cone pair.

**Real data, queued.** Bertozzi's measurements of electron speed against calorimetric kinetic energy (*Am. J. Phys.* 32,
551, 1964; 0.5 to 15 MeV) sit wholly past the electron's corner (x from about 1.7 to 30). They would test the far-field
side: each doubling of momentum adds about ln 2 of rapidity. That tests special relativity itself, which is settled,
not the corner. The paper is not reachable from here (AIP and its copies are blocked), and teaching reproductions of its
table will not be used. Tom to supply the table if wanted.

## Runs

### Run 1 (11 October, `runs/emc/emc.py`)

Seed 16, two seconds. P1's identities and P4 are in exact rationals, from Pythagorean triples and rational Doppler
factors. The rest is in floats, with the speed taken by complex step from E(p).

| | prediction | result | |
|---|---|---|---|
| P1 | u/c = pc/E from dE/dp; v² + h² = 1 and √(1 − β²) = h exactly | 4.4e-16 over 0.001 ≤ x ≤ 1000 (electron mass, c in m/s); 0 of 10⁴ rational states failing | not killed |
| P2 | home E = mc², horizon E = pc; at the corner β = 1/√2, E = √2·mc², T = (√2 − 1)·mc² | all hold; worst 1.1e-16 against the closed forms. The electron's corner is at T = 0.2116627 MeV, the proton's at 388.6450241 MeV | not killed (see the note) |
| P3 | e_N(x) = e_U(1/x); Newton better exactly when x < 1; both √(9/8) − 1 at the corner | 8.3e-16; 0 of 6,000 points wrong; both 0.0606602 | not killed |
| P4 | a boost pans the light-cone pair by ∓ln k_b, midpoint mc² fixed; composition by k₁k₂; E′ ≥ mc², least at k_b = (E + pc)/mc² | 0 of 10⁴ failing; none below mc²; the circle's share v moved in every boost but the identity (10⁴ of 10⁴ as predicted); all 1,000 boosts by (E + pc)/mc² land at rest | not killed |

**A slip in the plan, recorded and not edited.** P2's two worked decimals were my mental arithmetic, and both are off in
the sixth digit: 0.2116605 should be 0.2116627 MeV, and 388.6430 should be 388.6450 MeV. The kill condition was
against the closed form, which holds, so P2 is not killed. The decimals are wrong as written.

**P3's table, the two errors side by side** (e_N, e_U):
- x = 0.1: +0.000012, +4.074690;
- x = 0.5: +0.006231, +0.341641;
- x = 1: +0.060660 for both;
- x = 2: +0.341641, +0.006231;
- x = 10: +4.074690, +0.000012.

Newton at x is the ultra-relativistic form at 1/x, digit for digit.

**Reading.**
- **The relation is the unit circle of (pc, mc²), read in the one unit E.** Its two unit relations are β (the speed,
  from dE/dp) and the moving clock's rate (the rest share).
- **E = mc² is the statement of home and E = pc that of the horizon.** Massive things never reach the horizon, because
  v is capped at 1. The corner, pc = mc², is where Newton's form and the ultra-relativistic form are equally wrong, each
  6.07% high. Each is exactly as good on its own side as the other is at the flipped point: Newtonian mechanics is the
  near field, the massless limit the far field, and they are one approximation under the flip.
- **Mass is the corner of the other pair.** A boost pans the light-cone energies' levels by equal and opposite amounts,
  so their midpoint, mc², stays where it is. The circle's shares move with every boost; the midpoint never does. That
  is the reading of why mass is the same for every observer, and why rapidities add.
- **All four are standard physics.** The run settles them exactly and in the corner's terms.
