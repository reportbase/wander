# The system on one page, and what wavelets already know of it

*6 October 2026, by Claude, at Tom's word: "yes, do a wavelet comparison. i'm sure we will find that it captures some
of these ideas. whats new here is trying to bring it all together from the situated and not-situated perspective."
A reading, not a ruling. Checks: `python3 plans/wavelets/checks.py`.*

## The system on one page

| in SPN | what it is | its name in isolation |
|---|---|---|
| the sweep, 0 to π/2 | a relation v/h addressed by its turn | slope as angle; the gnomonic projection; an even spread of directions read as tan is the Cauchy distribution |
| the flip, s ↔ 1/s | the same relation from the other facing | the reciprocal; the complementary angle, θ ↔ 90° − θ |
| the corner, 45° | where the known side equals the unknown; the flip's one fixed point | the Cauchy's median; the corner frequency, the half-power point |
| proportion, then a count | proportional within an octave, logarithmic across octaves | linear then log scales; a float's subnormals then normals; Weber–Fechner |
| the octave | one quarter turn of the sweep (Proposition 3.12) | the octave; the decade; a radix digit; a dyadic wavelet band |
| recursion | every octave the same sweep again, without end (3.11) | self-similarity; multiresolution |
| the spiral | the reading drawn: k > 0 in situation 3, k = 0 (the circle) in situations 1–2 (3.13) | Bernoulli's equiangular spiral |
| the pitch k | the ratio between rungs | the dilation factor of a wavelet frame |

One object (the quarter turn), one mark (the corner), one parameter (k). **Uniform sweep, k = 0**: both breadths known,
no horizon, no recursion forced (situations 1 and 2, not situated; they can still recurse on a known shape's residual,
SPN §2.1, revised 6 October). **Non-uniform sweep, k > 0**: one breadth known, a horizon,
recursion (situation 3, situated).

## What filters and wavelets already have (each checked)

**1. A single first-order filter is the one bounded sweep.** H = 1/(1 + iω/ωc) lags by atan(ω/ωc): a quarter turn from
0 to ∞, 45° at the corner frequency, where exactly half the power passes. The octaves out from the corner get 36.9°,
19.4°, 5.3°, 1.3°, 0.34°, 0.08° of it: the same numbers as Proposition 3.11's counterexample. Engineers already call
the 45° point *the corner*.

**2. A ladder of them, one corner per octave, is the spiral.** Corners geometrically spaced at qⁿ give a phase
Φ(ω) = Σ atan(ω/qⁿ) that adds exactly 90° per octave (to 10⁻¹² of a degree, q = 2 and 4): (R) of Proposition 3.11,
realised as a circuit. Against ln ω it is a straight line with a periodic ripple, Proposition 3.13's form exactly, and
a close one: ±0.05° for q = 4 (one octave of SPN's, ×4), under 10⁻⁴° for q = 2. SPN's projective octave
(Proposition 3.12) ripples ±4.74° on the same measure. Geometrically spaced corners are the construction of Oustaloup's
recursive approximation of fractional-order systems (Oustaloup et al. 2000).

**3. Wavelet and constant-Q analysis is (R).** Twelve bins an octave in every octave (Brown 1991), a wavelet dilated by
the same factor from band to band (Mallat 1989; Daubechies 1992): no rung preferred. The two alternatives fail it in
opposite directions:

| tiling | bins in successive octaves | which rung it prefers |
|---|---|---|
| uniform (short-time Fourier) | 1, 2, 4, 8, 16, 32, … | the far ones (k = 0: the circle's even sweep) |
| one bounded sweep (even in atan s) | 19.7, 13.4, 7.4, 3.8, 1.9, 1.0, … of 96 | the one at the corner |
| octaves (wavelet, constant-Q) | 12, 12, 12, 12, … | none |

That is Proposition 3.11 seen from signal processing: only the octave tiling treats every rung alike.

**4. The dilation factor is a choice there too.** Dyadic wavelets (factor 2) are standard because Mallat's fast
algorithm halves at each step, but wavelet frames work for any dilation a₀ > 1 (Daubechies 1992). The same as the audit
of Part I found for SPN: the 2 is convenient, not forced.

**5. Multiresolution is R176's lay.** A multiresolution analysis holds everything below its coarsest band in one
lowpass piece (the scaling function) and lays octave bands above it (Mallat 1989): one plain piece toward home, then
octaves past it, as a float holds subnormals and then normals, and as SPN §14's R176 lays proportion to the corner and
octaves past it.

**6. Hearing is built that way, by measurement.** Two standard scales of pitch fitted to listeners' data are both
log(1 + f/fc): proportional below a corner and logarithmic above it, the slope halved at the corner.

| scale | corner fc | proportion holds at fc/10 to | the logarithm holds at 10·fc to |
|---|---|---|---|
| mel, 2595·log₁₀(1 + f/700) (O'Shaughnessy 1987, from Stevens, Volkmann and Newman 1937) | 700 Hz | 4.7% | 4.0% |
| ERB-number, 21.4·log₁₀(1 + 0.00437 f) (Glasberg and Moore 1990) | 229 Hz | 4.7% | 4.0% |

This is the shape the number-line test looked for in children and did not find (NLE): here it is, in a sense that has
been measured for decades. Two cautions. The formulas were chosen to fit, and their corners are fitted values, not
predicted. And log(1 + s) is not fair to the facings: it runs on without bound past the corner, so it is R176's lay
(proportion, then a count), not Proposition 3.2(b)'s bounded reading.

## What they do not have: what the situated view adds

- **Why octaves, not only that they work.** Wavelets are chosen; their analyst holds the whole signal, both breadths,
  a view from nowhere, and picks the tiling for convenience or for a trade-off. SPN derives the octave tiling as
  forced for a reader that knows one side and faces a horizon, once no rung is preferred (Proposition 3.11). The
  short-time Fourier tiling, usually the other side of a trade-off, is then the reading of a reader that knows both
  breadths: the circle, k = 0. So the choice between the two tilings becomes a fact about the reader, what it knows,
  not a design choice.
- **The two facings and the flip.** Frequency analysis treats its two ends unalike: one lowpass piece at DC, bands up
  to ∞. SPN treats them alike, with the corner as the flip's fixed point. A counterpart may be time–frequency duality,
  where scale and frequency are reciprocal and the Gaussian is its own Fourier transform; unexplored, flagged as a
  question only.
- **The standpoint as the source of the structure.** In filters and wavelets the corner, the octave and the spiral are
  separate tools. In SPN they are one consequence of one situation: a known side, an unknown side, a horizon.

So Tom's expectation holds: the pieces are known, the corner frequency and the dyadic ladder by name, and a circuit
already builds the spiral. What is new is the claim that they are one structure, and that what decides between the
uniform and the octave tiling is what the reader knows. That claim is now precise enough to be tested: it predicts that
wherever a reader is situated in the SPN sense (one known side, a horizon), it tiles by octaves, and wherever both sides
are known, it tiles evenly.

## References

- Brown, J. C. (1991). Calculation of a constant Q spectral transform. *Journal of the Acoustical Society of America*
  89, 425–434.
- Daubechies, I. (1992). *Ten Lectures on Wavelets*. SIAM.
- Glasberg, B. R. and Moore, B. C. J. (1990). Derivation of auditory filter shapes from notched-noise data. *Hearing
  Research* 47, 103–138.
- Mallat, S. G. (1989). A theory for multiresolution signal decomposition: the wavelet representation. *IEEE
  Transactions on Pattern Analysis and Machine Intelligence* 11, 674–693.
- O'Shaughnessy, D. (1987). *Speech Communication: Human and Machine*. Addison-Wesley.
- Oustaloup, A., Levron, F., Mathieu, B. and Nanot, F. M. (2000). Frequency-band complex noninteger differentiator:
  characterization and synthesis. *IEEE Transactions on Circuits and Systems I* 47, 25–39.
- Stevens, S. S., Volkmann, J. and Newman, E. B. (1937). A scale for the measurement of the psychological magnitude
  pitch. *Journal of the Acoustical Society of America* 8, 185–190.
