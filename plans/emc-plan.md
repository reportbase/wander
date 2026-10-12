# EMC: E² = (pc)² + (mc²)² through the corner

*11 October 2026. Tom: "so lets talk about how the corner helps understand the known equation", then "yes" to writing it
up with predictions first. Exact arithmetic (rationals where the numbers are rational) and the complex step. Predictions
written before the script (`emc/emc.py`) exists. It follows MOT run 3 (`plans/mot-plan.md`), whose P17 already has the
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
