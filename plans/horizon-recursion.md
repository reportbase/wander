# The horizon forces recursion, and the reading is a spiral

*6 October 2026, by Claude, from Tom's remark the same day: "the most exciting potentially impactful idea here … is that
each octave is equivalent to the 0 to π/2, so each octave is a 90 degree turn. Situation 1 and 2 is uniform, no horizon,
no recursion. Situation 3 has a horizon and has recursion"; and, on the spiral, "logarithmic spiral maps onto this
framing very nicely". Propositions and proofs for review before anything goes into SPN; Claude's, unruled.
Checks and figure: `python3 plans/spiral/spiral.py --svg plans/spiral/spiral.svg`.*

![The reading as a spiral](spiral/spiral.svg)

## The setting

Situation 3: a reading s = v/h on (0, ∞), home at 0 and the horizon at ∞, neither reached. The reader holds it as a
**turn** Θ(s), increasing, counted in quarter turns: Θ = (π/2)·(n + g), with n the whole quarter turns (which
**piece** the reading is in) and g ∈ [0, 1) the share of a quarter turn within it.

Four premises, each from SPN, and named so that each result says which it uses:

- **(H) The horizon.** Θ is defined on all of (0, ∞): the reading runs on without end both ways (situation 3; R174).
- **(B) Bounded pieces.** Within a piece the reading turns through at most one quarter turn (a relation is bounded; Tom,
  26 September; g on [0, 1]).
- **(R) No rung preferred, in the address.** There is a ratio q > 1 such that Θ(q·s) = Θ(s) + π/2 for every s: scaling
  the reading by q moves the address one quarter turn and changes nothing else. This is R172/R175 ("every octave is a
  sweep") stated as an equation, and the address-level form of Proposition 3.7 (every rung has the same structure).
  With q = r², r is the ratio between rungs (the octave runs from c/r to rc round its corner c).
- **(F) Fair to the facings.** The flip s ↦ 1/s mirrors the turn about the corner: Θ(1/s) = π/2 − Θ(s) on the reader's
  own piece (R162; Proposition 3.2(b)).
- **(P) Each piece read as a relation.** Within a piece the reading is a projective map of the piece onto [0, ∞],
  then the turn: the piece is read as the whole was (SPN §3.3, "Each octave is a sweep").

## Proposition A. The horizon, with no rung preferred, forces endless pieces, all alike

*Under (H), (B) and (R): the pieces are infinitely many toward home and toward the horizon, and each is the reader's own
piece scaled by a power of q and read the same way.*

*Proof.* Iterating (R), Θ(qⁿs) = Θ(s) + n·π/2 for every whole n. Take the reader's own piece, [s₀, q s₀). As n runs
over the integers, qⁿ·[s₀, q s₀) covers (0, ∞) without overlap, and by (H) Θ is defined on all of it; on the n-th
image Θ is the reader's own Θ moved by n quarter turns. So piece n is piece 0 scaled by qⁿ, there is one for every
integer n, and Θ runs to −∞ toward home and +∞ toward the horizon. By (B), none of them holds more than a quarter turn. ∎

**What the proposition needs, and what it does not.** The horizon alone does not force pieces. One bounded sweep, the
turn of s itself, Θ = atan s, holds the whole unbounded reading in a single quarter turn, and satisfies (H) and (B).
It fails (R): the octaves out from the corner get 36.9°, 19.4°, 5.3°, 1.3°, 0.34°, 0.08° of turn, so the rung at the
corner is preferred and the far ones are crushed. So the chain is **the horizon *and* no preferred rung ⇒ recursion**.
Situations 1 and 2 fail the first premise: with both breadths known nothing is divided, the reading is the closed turn,
and there is no horizon to run on to (R131).

## Proposition B. Each piece is exactly one quarter turn, the same for every ratio

*Add (F) and (P). Then the reader's own piece runs from 1/r to r round the corner 1, and on it*

  ρ = (r s − 1)/(r − s),    Θ = atan ρ,

*uniquely: the edges at 0° and 90°, the corner at 45°, for every ratio r > 1.*

*Proof.* (F) makes the corner, the flip's fixed point s = 1, the middle of the reader's piece, and the flip carries the
piece onto itself; with (R) its edges are 1/r and r (q = r²). (P) asks for a projective map sending the lower edge, the
corner and the upper edge to 0, 1 and ∞, and three points fix a projective map: ρ = (rs − 1)/(r − s). Then
ρ(1/s) = (r − s)/(rs − 1) = 1/ρ(s), so Θ(1/s) = atan(1/ρ) = π/2 − Θ(s): (F) holds without being imposed. ∎

Checked: one octave out turns exactly 90° (to 10⁻¹⁵) for r = 2, 3 and φ; the flip mirrors the turn about 45° (to 10⁻¹⁶).
This is SPN §3.3's map, now for every ratio; the audit of Part I found that the ratio is not fixed by it. **Each octave
is a quarter turn whatever the ratio between rungs.**

## Corollary. Recursion without end

ρ is itself a reading on [0, ∞), home at 0 and its own horizon at ∞, so (H) holds for it. Applying Propositions A and B
to ρ gives pieces within the piece, each a quarter turn again, and so on without end: the address (n; j₁, j₂, …) of
SPN §3.3 ("Nesting"), 1.37h = (0; 1, −1, 0, 1). **Every level of the recursion exists because the level above has a
horizon.** Situations 1 and 2, with no horizon at the top, have none to recurse on.

## Proposition C. The reading is a logarithmic spiral, up to a wobble that repeats each octave

Draw the reading as a curve: the turn Θ as the angle, the reading s as the radius.

*Under (R), and only then, the curve is carried onto itself by the spiral similarity "turn a quarter, scale by q". Every
such curve is*

  ln s = k·Θ + c + W(Θ),    k = ln q / (π/2),

*with W periodic, of period one quarter turn. It is an exact logarithmic spiral if and only if W is constant.*

*Proof.* Θ increases, so s is a function of Θ; write u(Θ) = ln s. (R) says u(Θ + π/2) = u(Θ) + ln q, which holds if and
only if u(Θ) − kΘ is periodic with period π/2. ∎

What it gives:

- **Situation 3 is a spiral; situations 1 and 2 are the circle, the spiral with k = 0.** No growth per turn, no
  horizon, nothing to recurse on: the circle is the one curve of the family that a rotation alone carries onto itself.
  For r = 2 the reading grows ×4 each quarter turn and ×256 each full turn (k = 0.8825); for r = 3, ×9 and ×6561.
- **The pitch is the ratio between rungs.** k = 2 ln r/(π/2). So the open question the audit left, *what fixes a
  reader's ratio between rungs*, is the same question as *what fixes the spiral's pitch*. The geometry fixes the turn per
  octave (a quarter); it does not fix how much the reading grows in that quarter.
- **Two readings make "a quarter turn per octave", and they differ by under 5°.** The projective reading of
  Proposition B (each octave read as a relation) leaves the exact spiral by a wobble W that repeats each octave and
  vanishes at every corner and edge: at most 4.74° for r = 2 (0.053 of an octave, SPN §3.3's figure), 5.69° for r = 3,
  4.40° for φ (periodic to 10⁻¹⁰). The exact spiral is the logarithmic reading g = log_q s + ½ within the octave, also
  fair to the facings, but not projective. Which one a reader holds is the choice between reading each octave as a
  relation (a turn of a ray) and reading it as a count.
- **Equiangular.** A logarithmic spiral crosses every ray from its centre at the same angle, arccot k: 48.6° for r = 2,
  35.6° for r = 3. That constancy is the curve's form of "no rung preferred": the reading meets every direction alike,
  at every scale (Bernoulli's *spira mirabilis*: *eadem mutata resurgo*, "changed, I rise again the same").

## What is proved, and what is not

- Proved, on the premises named: A, B, the corollary and C. Each is short, and the numbers are checked.
- **(R) is the load-bearing premise**, and it is a ruling (R172/R175), not a theorem: Proposition 3.6 shows a reader
  cannot read its rung, which motivates (R), but does not by itself require the address to be the same at every rung.
  Proposition A shows exactly what (R) buys: drop it and one bounded sweep, with no recursion, holds the whole horizon.
- Not settled: the pitch (the ratio between rungs), and whether a reader holds the projective octave or the exact
  spiral. The second is a small, sharp question: they differ by at most 4.74°, a wobble with a known shape.

## For SPN (done, 6 October, at Tom's "Yes, proceed")

Added to §3.3 after "Every octave is a sweep" as Propositions 3.11 (A), 3.12 (B) and 3.13 (C), with the figure; the spiral's pitch added to §14's open question on the ratio between rungs; and in §2's
situations table, "the circle" for situations 1–2 read as the spiral with k = 0.
