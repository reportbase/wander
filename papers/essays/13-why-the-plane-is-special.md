# Why the plane is special

*The thirteenth of a series of essays on what can be known from where one stands. Draft, 29 October 2026.*

In October 1843 William Rowan Hamilton was walking along the Royal Canal in Dublin. For years he had tried to do with
triples of numbers what complex numbers do with pairs: add them, multiply them, divide them, and have multiplication
stand for turning, as multiplying by e^(iθ) turns the plane. Every morning, so the story goes, his sons asked whether he
could multiply triples yet, and every morning he said he could only add and subtract them. On the walk he saw how to do
it with four numbers, not three, at the price of the order: in his new numbers ij is not ji. He cut the rule into the
stone of Broome Bridge.

Hamilton's quaternions are how computers turn things in three dimensions today. But the price he paid is the subject of
this essay. Turning in the plane is a kind of multiplication that does not care about order, and that one fact holds
together a great deal of what the earlier essays found. In space it fails, and when it fails several things that were
one thing in the plane come apart.

The reader of these essays lives mostly in the plane: one other party, across and up, a quarter turn from one to the
other. The fifth essay added a second party and found that most of what mattered survived. This essay asks the sharper
question. Of everything the reader has in the plane, what is a fact about readers, and what is a fact about the plane?

*Demos: `central-reader.html` (step 5, a reader off the centre of a circle: its uniform turn lands unevenly, and the
landing, doubled less the uniform, is harmonic measure); `one-read.html` (the landing point ½e^(2iθ) and the Cayley
disc); `boost-sky.html` (a sky seen under a boost: the spherical Cauchy); `wedge.html` (step 7, position, then sweep);
`sphere-cube.html` (step 7, the two sweeps).*

---

## 1. One law, four parts

Start with what the plane gives. A reader stands somewhere off a line, at a foot m along it and a height γ above it.
Write that standpoint as one complex number, z = m + iγ. Turn uniformly and read where each direction meets the line,
and the readings are a Cauchy law with foot m and height γ (the third essay, section 6). In the plane this one law is
four different things at once.

**It is the uniform turn carried by a Möbius map.** A Möbius map of the line, x ↦ (ax + b)/(cx + d), moves the
standpoint z to (az + b)/(cz + d) and carries a Cauchy law to the Cauchy law of the new standpoint. Nothing else
changes. Every change of chart the reader can make, a new zero, a new H, the reciprocal, is such a map, and so the
family of Cauchy laws is closed under all of them. The third essay called this "once a Cauchy, always a Cauchy".

**It is harmonic measure.** Release a random walker at the standpoint and let it wander until it first touches the line.
Where it lands is a Cauchy law with the same foot and height. Mathematicians call this the harmonic measure of the line
from z, because it solves the problem of heat or voltage on the half-plane: hold the line at a temperature that varies
along it, and the temperature at z is the average of the line's temperatures over this law. So the law a reader's turn
lays down is also the law of where a blind random path would end up. Nothing about the turn mentions walkers; it is a
coincidence, and the plane is where it happens.

**Its averages are the powers of one point.** Carry the line onto a circle, the central sweep's chart, with the Cayley
map W = (X − i)/(X + i). The standpoint z goes to a point w = (z − i)/(z + i) inside the circle, and the averages of the
law become the powers of w: the average of W is w, of W² is w², and so on. A law with no mean on the line has one on the
circle, and the mean is the standpoint itself, carried across. The second essay's Euler section said this in Euler's
notation: the Fourier transform of the Cauchy is e^(izt), the exponential of the standpoint.

**It is the two sweeps' rates, combined.** Put a reader inside a circle, off its centre, and let it turn uniformly. Its
directions land on the circle unevenly: bunched on the near side, spread on the far side. Call the landing density L.
Then 2L less the uniform density is exactly the circle's harmonic measure from the reader's place. Twice the inscribed
rate less the central rate, the second essay's two sweeps, gives the law of where a walker from the same place lands.
This is the demo `central-reader.html`, step 5.

Four parts, one law. EUL, the run behind this essay, checked each of them in the plane to forty digits: the Fourier
transform to 6·10⁻⁴², the powers to 10⁻⁴¹, harmonic measure against the Möbius image of the uniform to 2·10⁻³⁹.

---

## 2. Why the plane can do this

The reason is old, and it is the reason Hamilton could not multiply triples.

In the plane, the maps that keep angles (the conformal maps) are exactly the complex functions with a derivative, and
there are endlessly many of them. Any such map carries harmonic functions to harmonic functions: the heat problem on one
region is solved by mapping it onto another whose answer is known. Riemann's mapping theorem says almost any region can
be mapped onto a disc this way. So in the plane, harmonic measure and conformal maps are tied together, and every
conformal map that sends a disc to itself is a Möbius map. The Möbius maps carry the turn's law; they also carry the
walker's law; so the two are carried together, and if they agree at one standpoint (the centre, where both are uniform)
they agree at every standpoint.

That is the whole argument, and every step of it uses a fact of the plane: that angle-keeping maps are plentiful, that
they keep harmonic functions harmonic, and that turning is multiplication by a complex number of size one.

In space all three fail. Liouville proved in 1850 that in three or more dimensions the only maps that keep angles are
the Möbius maps (turns, scalings, translations and inversions in spheres). There is no stock of other conformal maps.
And the heat equation is no longer kept by them: an inversion in a sphere carries a harmonic function to a harmonic
function only after it is multiplied by a power of the distance. So harmonic measure and the Möbius maps are no longer
tied. Each has its own law, and the two laws differ.

---

## 3. What the run found in space

On the sphere, put the axis through the standpoint and let t be the cosine of a direction's angle to it. Two laws now
stand where one stood in the plane.

**Harmonic measure** from a point at distance r from the centre, inside the unit ball, is

> P_H = (1 − r²) / (4π (1 + r² − 2rt)^(3/2)).

**The spherical Cauchy** at concentration ρ, the Möbius image of the uniform law (Kato and McCullagh, 2020), is

> P_M = (1 − ρ²)² / (4π (1 + ρ² − 2ρt)²).

In the plane the two powers are the same, 1 and 1; on the sphere they are 3/2 and 2. EUL measured what that costs.

**Harmonic measure keeps the powers.** Its averages of the Legendre polynomials are r, r², r³, … to 2·10⁻⁴⁴: one
number, raised. So its mean direction (the average of t) is r, the standpoint's own distance from the centre. The
standpoint is still the mean.

**The spherical Cauchy keeps the Möbius maps.** A boost of rapidity 0.7 carried the law at ρ = tanh(0.2) onto the law at
tanh(0.55) to 7·10⁻⁴¹: rapidities add, as the plane's would. But its averages are not powers of one number, and its mean
is not ρ. In closed form, with ρ = tanh(η/2),

> mean of t = coth η − η / sinh² η,

0.1331 at ρ = 0.1, 0.6320 at 0.5, 0.9727 at 0.9, every one above ρ. In the plane the mean would be ρ, algebraic in ρ. On
the sphere the rapidity η itself, a logarithm, appears.

**No harmonic measure is a spherical Cauchy.** For each ρ from 0.1 to 0.9, the run looked for the r whose harmonic
measure comes nearest. The least gap never fell below half a percent of the peak (0.0055 at ρ = 0.1, 0.067 at 0.8). And
a boost carries harmonic measure onto no harmonic measure at all: from r = 0.3, a boost of 0.5 lands at least 2% of the
peak from the nearest one.

**The two sweeps' rates have no counterpart.** Inside a ball, a reader off the centre turning uniformly lands on the
sphere with density L = (1 − rt)/(4π(1 + r² − 2rt)^(3/2)). In the plane, 2L less the uniform was harmonic measure
exactly. In space no a·L + b/(4π), for any constants a and b, comes within 2.6% (at r = 0.3) or 5.8% (at r = 0.7) of it.
The best a is 1.52 or 1.66, not 2.

So in space there are three laws where the plane had one: the landing of a uniform turn from an off-centre point, the
landing of a walker, and the Möbius image of the uniform. In the plane they are tied by an identity and a coincidence.
In space each goes its own way.

---

## 4. Turns that do not take turns

The other thing that stops at the plane is composition, and it is the thing Hamilton ran into.

In the plane, a reading taken from one zero and a reading taken from the next combine by tangent addition,
(s₁ + s₂)/(1 − s₁s₂), which looks awkward and blows up when the two turns reach the vertical. Written as e^(iα)·e^(iβ) =
e^(i(α + β)), it is plain addition of angles (the second essay's Euler section). That works because turns of the plane
commute: a turn by α and then by β ends where β and then α ends.

Turns of space do not. Hold a book flat, turn it a quarter about the vertical and then a quarter about the line pointing
at you; then start again and do the two turns in the other order. The book ends in two different positions. With no
fixed order there is no single angle to add, and no logarithm turns combining two turns of space into a sum. Frobenius
showed in 1878 that the only number systems with division in which multiplication does not care about order are the
real and the complex numbers. The quaternions keep division and give up the order; nothing keeps both past two
dimensions.

For the reader with two other parties this has a plain meaning. The fifth essay's two sweeps, altitude (from H up to V)
and azimuth (round from H to V₂), are each the turn of a plane. Each on its own still composes by adding angles, still
has its corner at 45°, still lays a half-Cauchy over its quarter turn. What fails is putting them together: a sweep in
altitude then a sweep in azimuth is not the same motion as the two in the other order, and the wedge's demo makes the
point by its own design. `wedge.html` step 7 places the wedge first and sweeps second ("position, then sweep"), because
the other order would give another wedge.

---

## 5. What survives in space

It would be wrong to read this as "the plane's reader does not extend". Most of what the earlier essays found is not a
plane coincidence at all. Sorting it is the point of this essay.

**The split survives.** A point of space is still an amount times a direction, r·u, with u a unit vector. Scaling the
world still moves the amount and not the direction. The first test of the series, scale the world, asks the same
question in any number of dimensions: which part moved. The logarithm ln r survives as the real part of the
logarithm's plane; only its imaginary part, which in the plane was one angle that added, becomes a direction on a
sphere that does not.

**The corners survive.** Each pair of parties has its corner, where the two shares are equal, and the reciprocal that
swaps them leaves it in place: a mirror plane in place of a mirror line. The corner in distance, d = H, is a mirror in
the logarithm of distance whatever the number of directions. The fifth essay's results, every pair at its corner and
the near field in all readings a third (1/(n + 1) with n other parties), are statements about uniform directions from
home. At home, at the centre of the directions, all three of space's laws are the same law: the uniform one. Nothing in
the fifth essay assumed a standpoint off the centre, so nothing there depends on the plane.

**The Cauchy wedge survives.** The two-dimensional Cauchy of the wedge's readings, (v/h, v₂/h), is the uniform law on
the octant seen through a flat screen. It is the image of the uniform directions, with no standpoint moved. It holds in
every dimension, and the fifth essay's numbers stand.

**What depends on the plane** is everything that moves the standpoint off the centre:
- that the mean, in the bounded chart, is the standpoint (in space it is for harmonic measure, not for the Möbius law);
- that the uniform turn's law and the walker's law agree (in space they do not);
- that the two sweeps' rates combine into either of them (in space into neither);
- that turns compose by adding (in space only within one sweep).

---

## 6. Which law a statement means

This gives the corpus a rule. A statement about the reader's standpoint in three dimensions has to say which law it
means.

The boosted sky is the clearest case. A uniform sky seen by an observer moving through it is the spherical Cauchy,
with ρ = tanh(η/2) (the seventh essay, section 7). In the plane the same law would also be harmonic measure and would
have mean ρ. On the sphere it is the Möbius law alone: its directions bunch toward the way of travel by a law that the
reader's boosts carry, but its mean cosine is coth η − η/sinh² η, not ρ, and no random walker from any point lands
that way. The sky is a Möbius fact, not a heat fact.

A reader standing off the centre of a room, turning evenly, is the other case. Its directions land on the walls by the
landing law L, the plain geometry of a turn from a point. That is neither the Möbius law nor harmonic measure. In the
plane it would have been half of each, plus the uniform; in space it is its own law.

And a walker, or heat, or anything that diffuses from a point, lands by harmonic measure, and keeps the property that
the plane's Cauchy had of having the standpoint for its mean.

None of these is new mathematics. The three-dimensional Poisson kernel is classical, its Legendre series is the
generating function of the polynomials, Kato and McCullagh set out the spherical Cauchy's family, and Liouville's
theorem is a hundred and seventy-five years old. What the corpus did not have, until the audit that went with this
essay, was a check that each of its own three-dimensional claims means the right one. Every claim about harmonic
measure in the corpus turned out to be in the plane; every three-dimensional claim about the Cauchy was either made
from the centre, where the laws agree, or about the boosted sky, where the Möbius law is the right one. None was wrong.

---

## 7. What it comes to

In the plane, the reader's Cauchy wears four hats: the uniform turn under every change of chart, where a walker
lands, the law whose averages are the powers of the standpoint, and the two sweeps' rates combined. It wears them
because the plane has endless angle-keeping maps, because those maps keep heat as heat, and because turning is
multiplication that does not care about order. Euler's formula, z = r·e^(iθ), is the notation of all three, which is
why the second essay could call it the reader's notation.

In space the hats come off. Liouville leaves only the Möbius maps; the heat problem stops being kept by them; turns
stop commuting. Harmonic measure keeps the powers and the mean. The spherical Cauchy keeps the Möbius maps and the
boosted sky. The two sweeps' rates combine into neither, and two sweeps compose only in order.

What does not come off is what the series has built on: the split of a point into a direction and an amount, the test
that asks which of them moved, each pair's corner, the corner in distance, and the uniform law from home, with the
fifth essay's thirds. Those are facts about a standpoint and its directions, and they hold in any number of
dimensions. The coincidences are facts about the plane.

So the plane is special, but not in the way that would undo anything. It is special because in it one law does four
jobs. A reader in space does the same reading; it only has to say which job it means.

---

## Sources

- Kakutani, S. (1944). Two-dimensional Brownian motion and harmonic functions. *Proceedings of the Imperial Academy
  Tokyo* 20(10), 706–714. (Where a walker lands is harmonic measure.)
- McCullagh, P. (1996). Möbius transformation and Cauchy parameter estimation. *The Annals of Statistics* 24, 787–808.
  (The Cauchy's standpoint carried by Möbius maps; on the circle, its moments the powers of one point.)
- Kato, S. and McCullagh, P. (2020). Some properties of a Cauchy family on the sphere derived from the Möbius
  transformations. *Bernoulli* 26(4), 3224–3248. (The spherical Cauchy.)
- Doyle, P. G. and Snell, J. L. (1984). *Random Walks and Electric Networks*. Carus Mathematical Monographs 22.
  Mathematical Association of America, Washington.

Named as history in the text and not cited in *Observation from Somewhere*: Hamilton's quaternions (1843), Liouville's
theorem on conformal maps in space (1850), Frobenius's theorem on division algebras (1878), Riemann's mapping theorem.

The computations are in `../../plans/eul-plan.md` and `../../runs/eul/eul.py` (run 1, forty digits). The geometry is in
*Observation from Somewhere*: Appendix A, "Polar form and the complex logarithm" (the notation, its limit in three
dimensions, the four parts and how they split) and "Cauchy's functional equation, twice"; Proposition 5(e) and "More
parties" for the wedge; §11 for the boosted sky.
