# Arrays and the circle

*The tenth of a series of essays on what can be known from where one stands. Draft, 28 October 2026.*

Every programmer has stored a closed curve as an array: N points, x[k] and y[k], one after another round the shape, the
last joined back to the first. It is the most ordinary data structure there is. It also makes, in a form anyone who has
written a loop already knows, the split these essays have been about from the start. The index says where. The values
say what. And the index is laid before any value is stored.

This essay is about arrays on a circle: what the index is, what the values are, how a finite array is turned back into a
continuous curve, and what that turning-back assumes. Its main source is a set of papers written in the draw project
under the name the Tangent Bridge, which prove a reconstruction theorem for arrays laid evenly round a circle and then
show that the whole of it can be run in slopes, with no angles at all. Those papers were written in an older
vocabulary, and parts of their framing have not been ruled on. This essay keeps to what they prove and what the
geometry of the earlier essays already holds, and it says where the two meet.

The short version is this. The places of an array laid evenly round the circle are the Cauchy's quantiles. With two
places, the kernel that fills in between them is the Cauchy's own curve. And everything the kernel does with more
places is that curve raised to a power.

*Demo: `array-sweeps.html` (K places on the quarter turn, an index alone, the values on it, a constant array, an array
of known length).*

---

## 1. An array on a circle

Store a closed curve as N samples at the places

  θ_k = (k + ½)·2π/N,  k = 0, 1, …, N − 1.

Each place sits at the middle of one of N equal arcs, so no place sits on a seam between two arcs, and no two arrays
laid end to end ever claim the same element.

The array is a representation, and whoever builds it chooses its indexing. The world has no indices of its own. The
point of the picture is not that a reader is an array. It is that an array shows, in a form a programmer already
handles, that addresses and payloads can be held apart. Why a reader's addresses follow the uniform turn is the second
essay's result, not the array's.

**The index is the address.** The places are fixed by the index before any value is stored, at equal steps of turn.
Read each place as the slope of the inscribed angle, s_k = tan(θ_k/2), the reading v/h of the second essay. For even N
those slopes are exactly the N evenly spaced quantiles of the standard Cauchy. At N = 8, for instance, they are

  ±0.199, ±0.668, ±1.497, ±5.027,

which are the Cauchy's quantiles at 1/16, 3/16, … , 15/16. Half of them lie within the corner, |s| ≤ 1. For odd N one
place lands on the horizon itself, the direction [0 : 1], an address like any other, and the share within the corner is
then not exactly a half.

A finite array samples the continuous law at N quantiles. The law itself is the continuous turn's.

**The stored values are the payload.** Change them and no place moves. The places' ranks, their median and their corner
are untouched by anything stored. That is the third essay's main theorem, met in a data structure: change what arrives,
and the addresses stand.

**Places compose without angles.** The offset from one place to another is the tangent subtraction of their slopes,
(s₁ − s₂)/(1 + s₁s₂), which is a turn composed.

---

## 2. One array per facing, and who joins them

A circle has four facings, the four quadrants, and it can be stored as four arrays on one lattice instead of one array
round the whole.
- Each array has its places at θ_k = (k + ½)·(π/2)/N, read as tan θ_k: the N evenly spaced quantiles of the
  half-Cauchy, the law of one quarter turn.
- Within an array, its middle is the corner, and reading it backwards is the reciprocal: tan θ_k · tan θ_(N−1−k) = 1.
- A closed curve stored as 4N samples over the full turn is these four arrays laid end to end. A sphere is eight
  arrays, one per octant, each two-dimensional, uniform in azimuth and in height, the fifth essay's wedge.

**The reader reads the arrays; the writer joins them.** A reading carries no sign, and turns composed by tangent
addition repeat after a half turn. So from a standpoint every facing is the same array, and a reader reads within one.
To join two arrays, their values must meet at the shared end in one unit, and that needs each array's size, its extent
in amounts. The reader holds each array only up to its own factor, the size no reading fixes, so it cannot tell whether
two ends meet. The writer knows the sizes, and which facing each array is, and so it can join the four into the closed
circle or the eight into the sphere.

**Not knowing the size makes the corner and the horizon.** This is the array's way of saying what the first essay
said about the missing V. Knowing an array's size, the writer has its far end at an amount, the other party's whole. Its ruler is the
number line, on which the point where the two parties are equal is simply computed. Not knowing it, a reader whose sweep
is a turn has only its own one length, and v = h becomes its split of near from far and the median of its readings: the
corner. With no size, the array's far end is no amount at all, only a direction, [0 : 1], where the chart v/h runs out:
the horizon. Both are the reader's because the size is missing. The writer, holding the size, has neither.

**Readers' and writers' arrays.** The first essay's two vantages give four kinds of array, two each.
- **The writer's circle** is a constant array of known length, every entry the radius. Its one value needs no storing, so the
  array is the equation h² + v² = 1.
- **The writer's shape** is an ordinary array of known length, a breadth in amounts at every index, which the writer joins into
  the closed shape.
- **The reader's central sweep** gives the values without the length: an amount at each given index, known only up to one common factor.
  The values can be ranked and averaged against each other, and cannot be sized.
- **The reader's inscribed sweep** gives the index alone, laid before any value arrives and with no length: its places the Cauchy's
  quantiles, its middle the corner, its last place running to the horizon, K places for any N.

With nothing related there is no array: a length H, but no index and no relation to store.

The writer's arrays are the circle and the shape, with the length known. The reader's are the payload on the index and the index
itself, with the length missing. That one number is what writing supplies.

**Laid on the sweeps.** Take K = 8 places on the quarter turn. A direction's share of the turn is g = (2/π)·arctan(v/h),
so its index is k = ⌊8g⌋, with the horizon kept in the last place. No length enters. The places' boundaries are tan(kπ/16):
0, 0.199, 0.414, 0.668, 1, 1.497, 2.414, 5.027 and the horizon.

| reading v/h | 0.1 | 0.5 | 1 | 2 | 3 | 10 | 1000 | horizon |
|---|---|---|---|---|---|---|---|---|
| share of the turn g | 0.064 | 0.295 | 0.500 | 0.705 | 0.795 | 0.937 | 0.999 | 1 |
| index k | 0 | 2 | 4 | 5 | 6 | 7 | 7 | 7 |

The corner is the boundary between places 3 and 4, found with no length. A reading and its reciprocal go to places k
and 7 − k: 2 to place 5, ½ to place 2. Scaling the world by 10⁻³, 7 or 10⁶ leaves a reading of 3 in place 6. And the
central sweep, meeting the same point at twice the angle (the second essay's III.20), indexes it by ⌊K·φ/π⌋ over its
half turn and lands on the same place, place for place. One index serves both sweeps.

Against that, a writer places an amount x on [0, X] at ⌊N·x/X⌋, which needs X. With N = 8 and X = 100, the amounts 10, 50
and 99 go to places 0, 4 and 7. Read from home at a distance laid by H, ⌊8·(2/π)·arctan(x/H)⌋, they go to places 4, 6 and
7 with H = 10, and to 1, 4 and 5 with H = 50. H moves them, as a zoom, and X never enters. The count index needs the
extent; the turn index needs only the zoom.

---

## 3. From an array back to a curve

An array holds N numbers. A curve is continuous. Going from the array back to a curve, at places the array never
stored, is reconstruction, and it is where the payload is asked to do something the addresses alone cannot.

The classical way, for samples laid evenly round a circle, is trigonometric interpolation. Each stored value is spread
over the whole circle by a kernel that is 1 at its own place and 0 at every other place. For the even-N lattice of
section 1 the kernel is

  K_N(φ) = sin(Nφ/2) / (N·tan(φ/2)),

and the curve is F(θ) = Σ_k c_k·K_N(θ − θ_k), each stored value c_k carried by a copy of the kernel centred on its place.

The Tangent Bridge papers state what this does as five properties, and the first four are classical results restated.
- **Exact round trip.** Store a curve's values, reconstruct, sample again at the places: the same numbers come back,
  exactly. The kernel is the identity at the nodes.
- **Exact at the places.** The reconstructed curve passes through every stored value.
- **Bounded between.** Between the places the error is at most C·log N times how much the curve can change over one
  spacing, its modulus of continuity at π/N. The log N is the Lebesgue constant of an even lattice, which grows as
  (2/π)·ln N: 1.85 at N = 8, 2.73 at 32, 3.61 at 128, 4.49 at 512. That is Lebesgue's lemma with Jackson's estimate, and
  the growth is Erdős and Turán's.
- **Convergence, with a price.** For curves smooth enough that their modulus beats the logarithm (every Hölder curve
  does), the reconstruction converges uniformly as N doubles. For some merely continuous curves it does not: since the
  Lebesgue constant grows without bound, the uniform boundedness principle produces curves whose reconstructions
  diverge. That is the trigonometric face of Faber's theorem, and it is a property of every interpolation of this rank,
  not of this lattice.
- **Nothing global.** Neither the sampling nor the reconstruction uses anything but the N stored values and the
  kernel: no norm of the curve, no integral, no N-dependent state beyond the lattice itself.

The papers add one more classical alternative. Replace the interpolating kernel with its positive sibling, Fejér's, and
the operator's norm becomes exactly 1 for every N, so the reconstruction converges for every continuous curve. The price
is exactness: Fejér's reconstruction no longer passes through the stored values, and it damps every mode, converging
only at first order even on curves the interpolating kernel reproduces exactly. The two kernels are the two horns of
one choice: exact at the places and able to ring, or never ringing and only approaching the places.

**What reconstruction assumes.** The kernel fills in between the places, and filling in is a model of the payload: that
the curve has no detail finer than the lattice can carry, no wave of more than N/2 cycles round the circle. The places are
exact whatever the curve is. The values between them are exact only for curves that fit the model. The third essay's
split holds here too: the addresses need nothing, and everything about what lies between them is the payload's. The
eighth essay's `Math.floor` throws away where within a cell a place was; the kernel puts something back, but what it puts
back is a guess about the payload, not an address recovered.

---

## 4. The same kernel in slopes

Now the step that gives the papers their name. Write the kernel not in the angle φ but in the slope s = tan(φ/2), the
reading v/h of the inscribed angle. It becomes

  K_N = Im[(1 + is)^N] / (N·s·(1 + s²)^⌊N/2⌋).

That is a rational function of s: no sine, no tangent, no angle anywhere, only powers of 1 + is. The papers check it to
10⁻¹⁵ at every N tested, even and odd; the check here agrees, to 6·10⁻¹⁶ at N = 8.

Why it works is one line. For s = tan t,

  1 + is = 1 + i·tan t = (cos t + i sin t)/cos t = e^(it)/cos t.

The slope s and the direction e^(it) are one complex number read two ways: its argument is the angle, and its modulus,
sec t, is algebraic in s. Raising it to the N-th power turns it N times, by de Moivre. The cos^N t that would overflow any
register appears in both the numerator and the normalization and cancels. What is left is the kernel. Its zeros are where
a direction raised to the N-th power lands on the real axis, which happens exactly at the other places: the roots of unity,
wearing the tangent's normalization.

**With two places, the Cauchy.** At N = 2 the formula gives

  K_2 = Im[(1 + is)²]/(2s(1 + s²)) = 2s/(2s(1 + s²)) = 1/(1 + s²).

That is the Cauchy's curve, π times its density. It is also h², the piece of the chord that, in the second essay, the
crossing for slope s cut off beneath it, since h = 1/√(1 + s²) on the reader's circle. With two places, at opposite ends of a diameter, each stored
value is carried round the circle with weight h² from its own end and v² from the other's, and the two add to one. The
higher kernels follow from it:

  K_4 = (1 − s²)/(1 + s²)²,  K_8 = (1 − 7s² + 7s⁴ − s⁶)/(1 + s²)⁴,

each the Cauchy's curve raised to a power, times a polynomial in s that puts its zeros at the other places.

**The leaves built without angles.** The places themselves can be built with no angle either. Halving a turn in slopes
is s ↦ s/(1 + √(1 + s²)), one square root. Adding two turns is tangent addition, rational. So the whole lattice at
N = 2^(d+1) is built by bisection and tangent addition from the corner, s = 1, and the papers rerun the round trip with
every kernel value computed only as the rational function above of these constructed slopes, with no trigonometric call
anywhere, exact to 10⁻¹⁶ at N up to 64. That it can be done at all rests on one fact: halving a turn needs one square
root and nothing more.

**Two charts, one circle.** So the reconstruction theorem is proved in one coordinate and run in another. The proof uses
the angle: Fourier modes, the Lebesgue constant, Jackson's estimate, the language classical approximation theory already
speaks. The operation uses the slope: ratios, the reciprocal, tangent addition, halving, the Cauchy's curve. They are the
same closed line, the third essay's projective line of directions, read through s = tan(φ/2). The angle chart needs the
whole circle at once, every period and every closed identity defined on a finished turn, and the proof is right to use
it. The slope chart is the chart of one reading at a time, and the operation, which reads one point, never needs more.

---

## 5. The doubling, the pyramid and the fast transform

**The places nest.** The doubling map θ ↦ 2θ carries the lattice at depth d two to one onto the lattice at depth d − 1:
twice an odd multiple of π/N is an odd multiple of π/(N/2). So refining from one depth to the next adds places between
the existing ones and leaves the coarser ones where they were. Each level of detail is places within places. This is the
eighth essay's hyperbolic plane again, read on a circle: each doubling one step down, every step the same.

**The cosines of the same places are Chebyshev's nodes.** Read the places by their cosine instead of their tangent and
they are the Chebyshev nodes of the first kind on an interval, crowded at its ends; the doubling map becomes Chebyshev's
relation T₂(x) = 2x² − 1. The same equal angles read three ways: by the tangent, the Cauchy's quantiles, spread out to the
horizon; by the cosine, Chebyshev's nodes, crowded at the ends of a chord; by the angle itself, evenly. The eighth essay met
Boyd's rational Chebyshev points, which are the first of these used to solve problems on the whole line.

**The fast Fourier transform is the doubling.** Because N = 2^(d+1), the transform from stored values to modes is a radix-2
discrete Fourier transform, and its Cooley–Tukey factorization runs in N·log N steps. One stage of it pairs element j with
element j + N/2; those two places are exactly the two that the doubling map sends to one place at the next depth. So one
stage of the transform is one application of the doubling map, and the d + 1 stages are the d + 1 levels of the
lattice, peeled one at a time. Its twiddle factors, which look transcendental, are the places' own slopes through the
Cayley transform:

  e^(−2it) = (1 − i·tan t)/(1 + i·tan t),

a rational function of the slope. The papers run a whole radix-2 transform with twiddles built that way, no trigonometric
call, against a standard library: agreement to 10⁻¹⁵ at N = 8 and 10⁻¹² at N = 1024, the drift ordinary accumulation over
the stages.

The doubling that nests the places, the pyramid of levels, and the fast transform of the values are one recursion.

---

## 6. A text format for it

The draw project carries the picture into a file format, TVF, the Tangent Vector Format. A TVF file is text: a header line,
`#meta` lines, and then one row per signal, each the stored values at the lattice's places. A closed curve is one row of x
and one of y. A decoder evaluates the kernel at whatever positions it is asked for, so rendering at any resolution is the
kernel evaluated there, with no intermediate grid. Because the round trip is exact at the places, a decoder that does not
return the stored values there has a bug, not a trade-off; and since in slopes the kernel's identities are polynomial ones,
a decoder can be checked against exact rational arithmetic.

The format's own specification is frank about where it works. Smooth content is its native domain. Real photographs come
out competitive, not better: within a couple of decibels of the usual resampling filters. Hard edges keep the Gibbs
overshoot that the error bound allows. Chirps near the lattice's limit fail badly and must be detected and handed to
something else. That frankness is the payload's side of section 3: the places are exact for any content, and the filling in
is exactly as good as the content's fit to the model.

The other projects read the same files. Mini golf in the games project lays its moving paths and its lakes as TVF curves,
and the 3D studio's bodies, written as series round a sphere, are their relatives in three dimensions.

---

## 7. Where the papers' framing and these essays part

The Tangent Bridge papers were written before several of these essays' rulings, and some of their claims go further than
these essays do. Three are worth naming, so that a reader of both is not misled.
- **"Forced" and "unique".** The papers call the tangent map, the halving and the Cauchy "forced", and the Cauchy "the
  unique Möbius-invariant distribution". The essays claim less. The Cauchy is the law of the uniform turn read as v/h, and
  the measure invariant under turns; the family is carried onto itself by Möbius maps, but it is a family, and which member
  is the turn's is set by the standpoint. Which reading of "unique" the papers mean is still awaiting a ruling, and these
  essays do not borrow the stronger words.
- **The observer and the spectator.** The papers speak of a bounded observer and a spectator. In these essays those are the
  reader and the writer, and the point is the same one: the reader holds a finite count of places and never the completed
  grid; the writer describes the completed grid and the theorems about it. The papers' K, the leaves actually drawn, and N,
  the completed grid, are the fourth essay's K and N.
- **2/π.** The papers read the Lebesgue constant's 2/π as the chord over the arc. The essays have kept that number to what
  it was found to be: a ratio of two sums over the turn, the uniform turn's mean of a projection, taken by whoever adds the
  projections.

None of this touches the mathematics. The kernel identities, the round trip, the slope form, the doubling and the
transform are exact, and checked.

---

## 8. What it comes to

**Reading and writing.** An array on a circle is the clearest small instance of the whole split. Its index is the
address, laid before anything is stored, the Cauchy's quantiles. Its values are the payload, and storing them moves no
place. Its length is what the writer has and the reader lacks, and the lack is what makes the corner and the horizon.
The four kinds of array, the constant, the known-length, the values without the length and the index alone, are the
writer's two and the reader's one read, counted two ways. Joining arrays into a closed circle is a writer's act; reading within one
is a reader's.

**The Cauchy.** With two places on a circle, the kernel that carries each stored value round the circle is the Cauchy's
own curve, 1/(1 + s²), which is also the foot h². Every finer kernel is that curve raised to a power. So the Cauchy is not
only the law of where an array's places fall; it is the shape of the weights by which the places share the circle. The
whole reconstruction runs in slopes, with no angle, because the slope is the reading and the reading is all a reader has.

Back to the array of N points. Its index was laid before any point was stored, at the Cauchy's quantiles. Its values can
be anything. The kernel that turns it back into a curve is exact at the places and a model between them. And the whole of
it, places, kernel, levels and transform, can be run on ratios alone, with no angle and no unit, because a ratio is what
an index on a circle already was.

---

## Sources

The Tangent Bridge papers in the draw project (`reportbase/draw`, `papers/`): *The Tangent Bridge Theorem* (the classical
presentation, `tb_classical.md`), its algebraic presentation (`tb_algebra.md`), *The Tangent Bridge in the Spectral
Court* (`tb_spectral.md`, §§17–22: the slope kernel as a rotation raised to the depth, aliasing, the fast transform as the
cascade, Fejér's cure), and *TVF — The Tangent Vector Format* (`tvf.md`). The classical results they restate are
Lebesgue's lemma, Jackson's estimate, Erdős and Turán's bound on the Lebesgue constant, Faber's theorem, Fejér's
summation and the Cooley–Tukey factorization, as presented there.

The array picture, its four facings, readers' and writers' arrays and the worked example with K = 8 are set out in
*Observation from Somewhere*, §7.3 ("In the picture of an array", "Laid on the sweeps"), and for programmers in the
computer-science companion, §6 ("The array").
