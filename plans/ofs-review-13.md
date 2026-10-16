# OFS review 13: Grok, on the head rotation and the wave/particle reading

*Shared by Tom without comment, 16 October 2026, about 05:14 MDT, after PR #108 (SPN R287). Kept as received.*

> groc: The new draft (15 October) already incorporates a sharper distinction between the two situated sweeps:
>
> - central sweep (taken at once): gets the payloads, read by their mean
> - inscribed sweep (from home, one direction at a time): gets the addresses, the Cauchy, read by its median at the corner
>
> and it now grounds the even turn, the corner, and \(V=H\) explicitly in Jaynes's transformation groups applied to the
> reader's ignorance.
>
> The head-rotation account and the wave/particle reading fit this structure directly.
>
> - The arc is still drawn by concurrent head rotation while the body walks the straight chord.
> - Maximal head rotation (outside/parallel) corresponds to the central sweep received all at once: the payload is read
>   under the measure \(\pi/2\), as a wave.
> - Minimal head rotation (inside/serial) corresponds to the inscribed sweep accumulated point by point: the payload is
>   read under the measure \(2/\pi\), as a particle.
> - Zero head rotation remains the completed/unsituated chord, reading 1.
>
> The reading maps
> \[ R_{S_\parallel}(P)=\pi/2,\qquad R_{S_\perp}(P)=2/\pi,\qquad R_{S_0}(P)=1 \]
> are independent of the payload \(P\) and are fixed solely by the situation (how far the head turns). This is
> consistent with the paper's claim that the Cauchy (and the Born density under the measurement identification) belongs
> to the addresses, not the payload, and with the open question in §11.2 about whether the central sweep is in fact taken
> all at once and the inscribed sweep one direction at a time.
>
> The complementarity that recovers the unit remains a relation among situations:
> \[ \frac{\pi}{2}-\frac{2}{\pi}=1. \]
>
> The additions therefore supply an operational mechanism for the "how either sweep is made" that the draft currently
> leaves unpinned, without altering the transformation-group derivation, the address/payload split, or the main Cauchy
> result. They can be inserted as a short clarification in §3 (or §3.4) and cross-referenced from the open question in
> §11.2.

## Response

Nothing is taken into OFS. Point by point:

1. **"π/2 − 2/π = 1" is false.** π/2 − 2/π = 0.934. The relation that returns the unit is the product,
   (π/2)·(2/π) = 1. OFS §3.4 says so in so many words ("it is their product, not their difference, that returns the
   line … add to 0.934, not to 1"). The same slip was made and corrected once before (R233, `plans/facings-note.md`).
2. **The head rotation is already in OFS** (R233; §3.4's column for the turn, §4, §10 step 3). Since this morning there
   is also a sharper account of it (R284; §4, "Why there are two sweeps, and only two"). What distinguishes the sweeps
   is where the pivot stands: the centre or a point of the circle, the only two pivots at which an even turn reaches an
   even arc. The head's half turn and quarter turn are those two rates.
3. **It is not a mechanism.** Saying how far the head turns restates the two sweeps; it does not say how either is taken
   (at once, or one direction at a time). R266 leaves that open, and §11.2 question 8 says so. The suggestion would put
   a reading in the place of an open question.
4. **Wave and particle stay out of OFS.** R270 is a reading kept in SPN; OFS is a geometry paper (R201). The words
   "parallel" and "serial" are out of OFS too (R268).
5. **"The Born density under the measurement identification" is not in OFS.** OFS says the Cauchy is the addresses'
   law; it says nothing about Born's rule. The qubit correspondence (QBT, R286) is in `physics.md`, not OFS.
6. **What is right:** the readings π/2, 2/π and 1 are fixed by the situation and not by the payload. That is Theorem
   6's point, and OFS has it.

The draft Grok read appears to be of 15 October; it predates §4's two-pivots account (R284).
