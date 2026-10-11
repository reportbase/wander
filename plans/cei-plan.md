# CEI: more points, less seen (exact arithmetic)

*Plan written 11 October 2026, before `cei/cei.py` was written or run (Claude; Tom: "proceed according to your
recommendation", to check the archived result before moving it into `papers/observation-from-somewhere.md`). The lab
rules hold: predictions and kills first; nothing above "Runs" edited after the run.*

## The claim, from the archive

*The Order of Limits* §3.1–§3.2 and *One Reader* (L896–909): a parallel reader of fixed step ε, looking side-on at N
points spaced evenly round a circle, resolves R(N) = (N/π)·arccos(εN/2π) of them; R peaks at about 1.1222/ε and then
falls; past N = 2π/ε it resolves none.

## The set-up, in current terms (keep the case)

- The circle has radius R (an amount); N points at angles 2πk/N. The reader is parallel (one hemisphere taken in at
  once, the outer vantage) and reads each point's position across its view, the projection R·sin θ, θ measured from the
  middle of the view.
- Its step is an amount, ε_len. The only quantity that enters is ε = ε_len/R, a ratio of two amounts: the bridge is
  the radius. Neither h nor v appears; this is physics of a named pair (step against radius), not the corner.
- A point is *resolved* when its projected gap to each neighbour on the visible half is at least ε.

## Derivation (written before the run)

Neighbouring points at θ and θ + 2π/N project a gap of about (2π/N)·cos θ. It is at least ε where cos θ ≥ εN/2π, that
is |θ| ≤ θ* = arccos(εN/2π). The resolved points span 2θ* of angle at spacing 2π/N, so R(N) ≈ 2θ*/(2π/N) =
(N/π)·arccos(εN/2π). Write x = εN/2π; then R = (2/ε)·x·arccos x, largest where arccos x = x/√(1 − x²), at
x* ≈ 0.6522, giving R_max = (2/ε)·x*·arccos x* ≈ 1.1222/ε, at N* = 2πx*/ε ≈ 4.098/ε. Past x = 1 nothing is resolved.

## Predictions

- **P1 (the formula).** A brute-force count (exact chord gaps, both neighbours, visible half) agrees with
  (N/π)·arccos(εN/2π) to within 2 points, for ε = 10⁻³ and 10⁻⁴ and N from 0.05/ε to 0.99·2π/ε. *Killed* if any
  disagreement exceeds 2 points plus 0.2% of the count.
- **P2 (the peak).** The brute-force maximum over N is within 0.5% of 1.1222/ε, at an N within 2% of 4.098/ε. *Killed*
  otherwise.
- **P3 (the ceiling).** At N ≥ 2π/ε (rounded up) the brute-force count is 0. *Killed* if any point is resolved.
- **P4 (depends on εN alone).** The resolved share R/N at the same εN agrees between ε = 10⁻³ and 10⁻⁴ within 0.002.
  *Killed* otherwise.

## Runs

**Run 1 (11 October 2026; `cei/cei.py`).**

| | ε = 10⁻³ | ε = 10⁻⁴ |
|---|---|---|
| worst |brute force − formula| over 400 values of N | 2.00 points | 2.00 points |
| peak count (against 1.1222/ε) | 1121 (−0.11%) | 11221 (−0.01%) |
| N at the peak (against 4.098/ε) | 3993 (−2.56%) | 40707 (−0.67%) |
| count at and past N = 2π/ε | 0 | 0 |

Share of all N resolved at the same εN, ε = 10⁻³ against 10⁻⁴: 0.4740/0.4746 (εN = 0.5), 0.4490/0.4491 (1),
0.3965/0.3968 (2), 0.2802/0.2803 (4), 0.0958/0.0959 (6). (The archive's table gives about twice these, counting the
visible half only.) The exact peak: x* = 0.652185, 2·x*·arccos x* = 1.122193.

- **P1 not killed**: the formula holds to within 2 points everywhere.
- **P2 killed** (narrowly): the peak's height is within 0.11%, but at ε = 10⁻³ its place is 2.56% below 4.098/ε, past
  the 2% written. The count is flat across the peak (it moves by about one point over hundreds of N), so whole-point
  steps decide where its first maximum falls; at ε = 10⁻⁴ the place is within 0.67%. A new run with a looser place
  tolerance would be a new prediction; this one stays killed.
- **P3 not killed**: nothing is resolved at or past N = 2π/ε.
- **P4 not killed**: the share depends on εN alone, within 0.0006.
