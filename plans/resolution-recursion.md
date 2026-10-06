# Does finite resolution force the recursion?

*6 October 2026, by Claude, at Tom's "yes" to working it out. The question: "does this adequately explain the recursion
of the sweep of the situated readers?" (the fisheye and the bell, SPN §2.1). The short answer was "partly": the fisheye
shows where recursion is needed and why every level looks alike. It does not show why the reader re-centres; that rests
on (R), no rung preferred. This note tests one way to close the gap: a reader that resolves only finitely fine angles.
A reading, not a ruling. Checks: `python3 plans/spiral/resolution.py`.*

## The setting

The serial reader's view is the fisheye, r = θ = atan(v/h) (SPN §2.1). Give it a finite resolution δ: two rays closer
than δ are one ray to it. Nothing else is assumed: in particular not (R).

## 1. A finite reader resolves finitely many octaves

Octave rings narrow by half each octave out, so a reader of resolution δ tells apart about log₂(1/δ) octaves on each
side of the corner. The rest fall into the last δ at the rim (and, by the flip, the first δ at the centre):

| δ | octaves resolved, each side | log₂(1/δ), δ in radians |
|---|---|---|
| 10° | 2 | 2.5 |
| 1° | 5 | 5.8 |
| 0.1° | 9 | 9.2 |
| 1′ | 11 | 11.7 |

So the reader resolves a **window** of relations, from tan δ to cot δ, with the corner at its middle. Beyond it lie
infinitely many octaves, all in one unresolved sliver at the rim. That is the horizon, as the reader meets it. Ten times
finer resolution buys only about three more octaves.

## 2. The rim, magnified, is the view one octave on

To read past the window, the reader must look closer at the rim. Near the rim the gap from the horizon is
atan(h/v) ≈ h/v, so magnifying the rim twofold shows the relations half as large: the view one octave on.

| v/h | rim gap magnified ×2 | the view one octave on | relative difference |
|---|---|---|---|
| 2 | 53.13° | 45.00° | 1.8 × 10⁻¹ |
| 4 | 28.07° | 26.57° | 5.7 × 10⁻² |
| 16 | 7.153° | 7.125° | 3.9 × 10⁻³ |
| 64 | 1.7903° | 1.7899° | 2.4 × 10⁻⁴ |
| 256 | 0.4476° | 0.4476° | 1.5 × 10⁻⁵ |

The difference falls as (h/v)², so a sixteenth for every two octaves. Far out, the magnified rim cannot be told from the
view one octave on. A reader that zooms cannot tell how many times it has zoomed. **There, no rung is preferred: (R)
comes out of the fisheye's own tail instead of being assumed.** Near the corner it does not: one octave out, the two
differ by 18%.

## 3. So the recursion is forced, and endless

Any finite δ leaves infinitely many octaves in the sliver at the rim, because the horizon is never reached. Every zoom
resolves finitely many more and leaves the rest in a new sliver. So a finite reader facing a horizon must zoom again
and again, without end. In situations 1 and 2 nothing lies past the rim, since the whole is held, so there is nothing to
zoom into.

The chain is: **a horizon and a finite resolution ⇒ endless zooms; far from the corner, every zoom alike.**

## 4. What it does not give, and what it suggests

- **The full quarter turn per level is still a choice.** Zooming the rim magnifies a tail; it does not give each level
  its own corner. To get that, the reader must take its window as a whole sweep and stretch it onto 0 to π/2: the
  re-centring of SPN's premise (P). Stretched that way, the window is close to the projective octave of Proposition 3.12
  and moves away from the logarithmic reading as δ shrinks:

  | δ | window ratio r = cot δ | stretched window − projective octave | stretched window − logarithmic |
  |---|---|---|---|
  | 26.57° | 2 | at most 3.5° | at most 1.3° |
  | 10° | 5.67 | at most 1.8° | at most 6.1° |
  | 1° | 57.3 | at most 0.2° | at most 16.6° |

  For fine resolution this closeness is unsurprising: both tend to the fisheye itself as r grows. It is no evidence for
  the projective octave over the logarithmic one.
- **A suggestion for the ratio between rungs.** If the reader re-centres by its whole window, the windows abut at
  cot δ, and the ratio between rungs is r = cot δ: set by the reader's resolution. SPN's octave, r = 2, would be a reader
  resolving 26.6°, the angle of the ring at v/h = ½. This would answer the open question of what fixes the ratio between
  rungs (SPN §14; the spiral's pitch, Proposition 3.13), but only if re-centring by the whole window is right. A reader
  could as well zoom by 2 each time. Unruled.

## Where this leaves the question

| | explained by |
|---|---|
| where recursion is needed: the far octaves, crushed into the rim | the fisheye (SPN §2.1) |
| that it is needed at all, and without end | finite resolution and the horizon (§3 here) |
| every level alike, far from the corner | the fisheye's tail, magnified (§2 here) |
| each level a full quarter turn, with its own corner | still a premise: re-centring, (P) |
| the ratio between rungs | open; resolution suggests r = cot δ (§4 here) |
