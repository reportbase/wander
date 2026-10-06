# Which near/far laws are fair to the facings?

*6 October 2026, by Claude; the open question SPN §14 lists after the audit of Part I ("a classification of classical
near/far laws … would replace 'physics has the same structure' with a count"). Mathematics, not a lab: no prediction to
register. Checks: `python3 plans/audit/near_far.py`. A reading, not a ruling.*

## The criterion, and what it means

A near/far law, written as a reading f(s) on [0, 1] increasing from 0 far away (s the thing's own size over the
distance, or whatever ratio the law turns on), is **fair to the facings** when f(s) + f(1/s) = 1: Proposition 3.2(b)'s
condition. Then its middle is at the corner, f(1) = ½.

Three equivalent forms, each a line to prove:

1. **In the logarithm.** f is fair if and only if f(eˣ) − ½ is odd in x. (Put s = eˣ; the condition is
   f(e⁻ˣ) − ½ = −(f(eˣ) − ½).) So the fair laws are exactly ½ plus an odd function of ln s: the Hill family is
   ½ + ½ tanh(n·x/2), the subtended angle ½ + (1/π)·gd(x), gd the Gudermannian.
2. **As a split.** f is fair if and only if f(s) = A(s) / (A(s) + A(1/s)) for some positive A: the share of a whole
   made of two parts that the flip exchanges. (If: swap s and 1/s. Only if: take A = f, since then A(1/s) = 1 − f(s).)
   The disc is the split between s and 1/s; Michaelis–Menten between √s and 1/√s; a dipole's magnetic intensity
   between its far term s² and its near term s⁴.
3. **In the angle.** With θ = atan s (the turn of §3.5), f is fair if and only if F(θ) + F(90° − θ) = 1, F(θ) = f(tan θ).
   The disc is F = sin²θ, and its fairness is Pythagoras, sin²θ + cos²θ = 1. No other power of the sine is fair: at
   45°, 2·(1/√2)ⁿ = 1 forces n = 2. That is why, of the powers of s/√(1 + s²) = sin θ, only the square passed (§3.2,
   corrected).

## The count

Twelve classical laws of this kind, checked to 10⁻¹⁵ (the list is Claude's; it is not exhaustive, and a different list
would give a different count):

| law | s | fair? | f at the corner | f = ½ at |
|---|---|---|---|---|
| glowing disc, light on its axis | radius / distance | **fair** | 0.5000 | s = 1 |
| dipole, near term's share of the magnetic intensity | (λ/2π) / distance | **fair** | 0.5000 | 1 |
| first-order filter, power passed | frequency / corner frequency | **fair** | 0.5000 | 1 |
| Michaelis–Menten, v / Vmax | concentration / K | **fair** | 0.5000 | 1 |
| two-state occupancy (Boltzmann) | ratio of the two weights | **fair** | 0.5000 | 1 |
| voltage divider, share across one resistor | R₁ / R₂ | **fair** | 0.5000 | 1 |
| Hill equation, n = 4 | concentration / K | **fair** | 0.5000 | 1 |
| angle a segment subtends, share of the half turn | half-length / distance | **fair** | 0.5000 | 1 |
| circular coil, field on its axis | radius / distance | favours the far facing | 0.3536 | 1.30 |
| first-order filter, amplitude passed | frequency / corner frequency | favours the near facing | 0.7071 | 0.577 (30°) |
| ring, or a Plummer-softened point, potential on axis | radius / distance | favours the near facing | 0.7071 | 0.577 (30°) |
| uniform disc, field on its axis (= its solid angle / 2π) | radius / distance | favours the far facing | 0.2929 | 1.73 (60°) |

**Eight fair, four not.** The line between them is plain once the split form is in hand:

- **Fair: shares of a two-way split.** Powers, rates, probabilities and fractions of a whole: each is "this part over
  this part plus its counterpart", and the flip exchanges the parts. Their middle is at the corner because that is where
  the two parts are equal.
- **Not fair: single components.** A field, an amplitude, a potential, a solid angle: one projection of the turn
  (sin θ, 1 − cos θ, sin³θ), not a share of a split. Their middle falls where the *angle* makes them ½: 30° for sin θ,
  60° for 1 − cos θ, about 52.5° for sin³θ.

**The same system can be both.** A first-order filter's *power* passed is fair, with its middle at the corner
frequency, where engineers already put the "corner" (the half-power point, −3 dB). Its *amplitude* passed is 0.707
there and favours a facing. Fairness is a property of which quantity is read, not of the system alone.

## Not of the form at all

- **Gravity inside and outside a uniform ball**, g / g_surface with s = r/R: s inside, s⁻² outside. It peaks exactly at
  the corner (the surface), like the share, but is not symmetric under the flip (exponents 1 and −2).
- **A dipole's electric intensity**, s²(s⁴ − s² + 1): its bracket is palindromic (s⁴P(1/s) = P(s)), symmetric about the
  corner, but it is not a share.
- **A ball's share of the view**, (1 − √(1 − s²))/2: ends at contact, s = 1; there is no far side (BAL).
- **The round opening**, 4 sin²(πs²/2): oscillates; its last maximum is at the corner (§3.2).

## What it does to "physics has the same structure"

It sharpens it to something checkable: **a near/far law has its middle at the corner, with near and far one geometry
under the flip, exactly when it is the share of a two-way split whose parts the flip exchanges.** Among the twelve,
every share of a split is fair and no single component is. So the correspondence is not a claim about where physical
near/far boundaries fall in general (the coil, the ring, the disc's field and the filter's amplitude all fall
elsewhere, at angles of 30°, 52.5° and 60°); it is a claim about which quantities a reader reads. A reader that reads
shares, as SPN's does (§3.5), meets the corner as the middle; a reader that reads components would not.

One caution of the audit's applies again: s carries a choice of unit (h = λ/2π, not λ, for the dipole; K for
Michaelis–Menten). A fair law is fair under any choice, but its middle is at s = 1 only in the unit that makes the two
parts of the split equal there.
