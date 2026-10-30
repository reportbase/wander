# Addresses Given, Payloads Met

**The Cauchy distribution as the geometry of a situated reader**

*Tom Brinkman. Draft for submission, 27 October 2026.*

## Abstract

A reader that stands somewhere, holds one length of its own and does not know the size of what it reads holds two
different things: where a reading can be put, its *address*, and what is met there, its *payload*. We construct the
addresses from that restriction and the uniform measure on the reader's turn. Any relation between two parties is a pair of unit relations h and v in [0, 1],
and every relation turns over at one point, v = h, the corner. The reader's one length, turned uniformly, traces a
circle; a continuous linear sweep that composes, carries h into v in a quarter turn and returns after a full turn
preserves an inner product of its own, unique up to that length. Read as v/h, the uniform turn's directions are the half-Cauchy on a quadrant, its median at the corner and
its quartiles a reciprocal pair. Following Jaynes's principle of transformation groups, with a group we state as the
reader's ignorance, this law is the group's invariant measure, Jaynes's m(x), rather than a
belief about what arrives. Whatever arrives along a direction cancels from its reading, by construction; order survives
every change of what arrives, and sums do not. Hence the median at the corner for any sweep that treats the two
parties alike, the missing mean wherever the sweep's weight stays above zero near the horizon, and the Cauchy's exact
shape only for the uniform turn. No reading fixes the size of what is read; one amount carried in does. In one
sentence: an address scheme and the magnitude met at an address are distinct mathematical roles, and a geometry can
specify the former without determining the latter. Three cases in published data (detector noise from LIGO, the quasar
number-count dipole and single-photon interference) show where the address law lies in each.

## 1. Introduction

A reader that stands somewhere has its own scale, a value it chooses to start from rather than a size it has measured,
and it does not know the size of what it reads. This paper asks what geometry such a reader needs. Its thesis is that a
situated observer does not possess a coordinate system for the world; it constructs an addressing scheme from the
relations available at its standpoint, and uses those addresses to meet the world's magnitudes.

Three things have to be kept apart: the *object*, whatever exists independently of any reading; the *address*, the
place in the reader's scheme at which something can be met; and the *payload*, the magnitude met there. A change of
coordinates moves addresses and payloads together. The separation constructed here lets either change without the
other: changing what arrives leaves every address in place (Theorem 5), and changing the standpoint changes the
addresses without touching the object.

The separation itself is familiar. Coordinates, sampling grids and a function's domain already keep a location apart
from the value found there. What is proposed is a construction of it for a reader at a standpoint, and what follows from
that construction. The addresses are built from bounded relations available at the standpoint, which fix a corner and a
horizon with no amount; a measure on them, the turn's, gives their law; and the construction says which magnitude it
loses in the building, the one size no reading carries, and what restores it, one amount carried in (Proposition 6).

The addresses are given, not performed. Classical results describe them as a sweep: a lamp turning on a shore, a needle
dropped at random angles. The pictures are processes; the mathematics under them is a measure on directions, the one
every turn leaves unchanged, and a measure is given whole. Once the reader's one length and the uniform measure on
directions are granted, the addresses are there at every standpoint before anything arrives. The measure is standard;
reading it as the reader's addresses is this paper's interpretation, and the results are stated so that each can be
checked apart from it.

**The method.** It is Jaynes's (1968, 1973): state an observer's ignorance as a group of transformations, and take the
measure the group leaves unchanged. We apply it to a reader that stands somewhere, with a group we choose as its
ignorance: turns of its attitude, rescalings of the other party's size, and the exchange of the two unit relations
(§2). What is ours is the choice of group, the near field and the corner, and the reading of the measure as addresses
rather than belief.

**Background: how the Cauchy is usually read.** The Cauchy law has been read in five main ways, each correct on its
own terms. This paper adds another, and it helps to have the five in view first.

- *A counterexample.* The law entered probability as an exception. Poisson met it in 1824 (as Stigler 1974 recounts) as a case where the average
  of many observations is no better than one: the mean of n independent Cauchy variables has the law of a single one,
  so the law of large numbers fails. Cauchy returned to it in 1853, in his exchange with Bienaymé over least squares
  (Stigler 1974). Textbooks keep it in that role, as the standard example of a law with no mean and no variance, to
  which the central limit theorem does not apply and whose sample mean never settles (Feller 1971). "Pathological" is
  the word often used.
- *A stable law, and a ratio.* It is the stable law of index 1 (Lévy 1925): sums of independent copies keep its shape,
  and only the scale grows. It is the law of the ratio of two independent centred normal variables, and Student's t with
  one degree of freedom. In these readings it is a law of amounts, values that add, divide and are averaged and that
  happen to have heavy tails.
- *A tail to guard against.* In statistics it is the standard stress test for estimators. The sample mean fails on it;
  the median, and the estimators that bound the influence of any one observation, do not (Huber 1964). The heavy tail is
  read as a fact about the data, outliers that come with them, and the remedy is to read the data by their order.
- *A line shape.* In physics it is the Lorentzian, the profile of a resonance or of a decaying state's spectral line,
  at half its height one half-width from the centre (Weisskopf and Wigner 1930; Breit and Wigner 1936). There it is read
  as a property of the system: the line is broad because the state decays.
- *The tangent of a uniform angle.* Geometrically it is the tangent of an angle turned uniformly, a lamp turning on a
  shore and flashing onto a straight beach, the lighthouse problem of Bayesian textbooks (Gull 1988; Sivia and Skilling
  2006). As the image of the uniform law on the circle under the projective map it is carried into itself by every
  Möbius map of the line (Knight 1976; McCullagh 1996), and as harmonic measure it is where a Brownian path from a point
  above a line first meets the line (Kakutani 1944). This reading is the nearest to ours. It makes the law a fact about
  directions, but about the directions of a lamp or a path, not about the places at which a reader meets what it reads.

**Background: indifference and Bertrand.** The second strand is the principle of indifference. Bertrand (1889) drew a
chord "at random" in a circle in three ways, got three answers for the chance that it is longer than the side of the
inscribed triangle (⅓, ½ and ¼), and concluded that "at random" means nothing until a procedure is named. Jaynes (1973)
answered that if the problem is posed so that its answer must not change when the circle is turned, resized or moved,
one measure survives and the answer is ½, and straws he tossed onto a circle agreed. The answer has not settled the
question. Van Fraassen (1989) argues that symmetry cannot fix a unique answer in general, Marinoff (1994) that each
answer belongs to a differently specified problem, Shackel (2007) that the attempts to save indifference fail, and Drory
(2015) that Jaynes's symmetries, imposed in different ways, give different measures; Seidenfeld (1979) presses the wider
objection against objective priors, and Kass and Wasserman (1996) review the formal rules for choosing them. Each treats the measure as a probability over outcomes: a belief about the chord, or
the frequency of chords.

**What the readings share, and what this paper adds.** In every reading above the Cauchy is a law of what is measured:
values that lack a mean, data with outliers, a system's response, a lamp's flashes, or a belief about chords. Its missing
mean is then an anomaly in what is measured, to be managed by robust methods or explained by the system. Jaynes points to
a different status. The measure his groups fix, his invariant measure m(x) (Jaynes 1968), is a reference, prior to any
data, against which distributions are measured. This paper puts the Cauchy in that place: as the invariant measure of the
directions from a standpoint, the law of the reader's addresses, fixed by the standpoint and the turn before anything
arrives. On that reading the missing mean is not an anomaly of anything measured. Read in the unbounded chart v/h, a
law of directions has a median and no mean; on a bounded chart, the angle, it has both. The missing mean belongs to the
chart that sends the horizon to infinity, not to anything measured (§6). What arrives at the addresses is a
separate thing, with a law of its own. The earlier readings stay correct; the reading here says which of their facts
belong to the addresses and which to what is met at them (§6).

**What the paper is for.** Practice already reads Cauchy-type quantities correctly. No one reports the mean of a Cauchy
sample: the median and the quartiles, or the centre and half-width of a line, are what statisticians, spectroscopists
and astronomers report, and robust methods were built to do the same where the tails are heavy. This paper does not
correct that practice. It gives a reason for it. The usual reasons, that the mean does not exist and that the median is
robust, say that the median works. The reading says what makes it the right summary: the quantity is a direction read
from a standpoint, its law has a median and no mean on the chart in which it is reported, and the median is the corner,
where the two parties' readings meet. It also says when the median stops being the right summary: when what arrives
weighs the two sides of the corner unequally the median moves off the corner by that weighting, and when an amount
enters, the law stops being a Cauchy from its centre outward (§6).

**Results.**
- Every relation between two parties turns over at one point, the corner v = h, the only point fixed by exchanging them
  (Proposition 1).
- A reader holding one length traces a circle when that length is turned; a continuous linear sweep that composes,
  carries h into v in a quarter turn and returns after a full turn preserves an inner product of its own, unique up to
  that length (Proposition 3).
- The uniform turn's readings v/h are the half-Cauchy on a quadrant, its median at the corner (Proposition 4); on a
  drawing with two axes, a page or an instrument that draws v at c times h, they are a Cauchy of scale 1/c, with the
  corner at the median only for c = 1.
- The main result: whatever arrives along a direction cancels from its reading; order statistics survive every change
  of payload and sums do not. The median at the corner needs only that the sweep treat the two parties alike, the
  missing mean that its density of h stay above zero near the horizon; the Cauchy's exact shape needs the uniform turn
  (Theorem 5).
- The inscribed sweep from the standpoint and the central sweep from the centre of the circle on the chord meet at one
  point for every direction (Euclid III.20); the central point is the inscribed direction squared (§7).
- No collection of readings fixes the scale; one amount supplied from outside fixes it wherever readings link to it;
  two standpoints bring back the figure up to scale; the best estimate of the unknown size is the median of what is
  known (§8).
- Past the corner, if no scale is preferred (a premise), only a logarithmic layout is consistent (Proposition 9).

The paper's results are geometry. It makes no claim about how real observers or instruments read; it draws on physics
and data to show what the reading does (three cases in data, §6), and claims no new physics. A
longer version, with the full account of the reader, further applications and classical connections, is Brinkman
(2026).

## 2. Setting

**Unit relations.** A *unit relation* is a number from 0 to 1 relating a part to its whole, such as the fraction of a
day gone. A relation between two parties requires two, one for each; draw one horizontally and one vertically and call
them h and v. Breadths are written in uppercase. The reader holds one, H, the value it chooses to start from, its own
length; it is not a measured size, and which value it chooses sets only the scale at which things are laid (§9). For the
reader, h and v are both shares of that one length. A *writer*, who holds the whole object, also holds a breadth V for
the other party and writes v against it; the reader has no V. The other party's true size, an amount the reader does
not have, is written V*.

Unit relations are not amounts. The amounts are h·H and v·V*, so (v·V*)/(h·H) = (v/h)·(V*/H): the ratio of unit
relations is not the ratio of amounts, and the only way from one to the other is to multiply by a breadth, which must be
known.

**Readings, the sweep and the horizon.** The *sweep* is every way h and v can relate, from all of h (v = 0, *zero*) to
all of v (h = 0). Leaving zero, v rises against h held at 1 until it too reaches 1, at v = h; after that h falls against
v held at 1. The reading is v/h on the first half and h/v on the second. Exchanging the two parties, the *reciprocal*,
sends v/h to h/v. The limit v/h → ∞ is the *horizon*.

This describes h and v on the *capped chart*, the edges of the unit square, the larger always held at 1. The paper's
main picture is the one-length circle (§4), on which the same direction is (h, v) = (cos θ, sin θ), with h² + v² = 1. A
reading, being a ratio, is the same on both; where an amount of h or v enters (a distance, a foot, a height) we work on
the circle unless the capped chart is named.

A reading is a direction, [h : v] with h, v ≥ 0, not both zero: a point of the closed half-arc of the projective line,
with two ends, *home* [1 : 0] and the horizon [0 : 1], and two charts, x = v/h (defined except at the horizon) and y = h/v
(defined except at home). The *address* is the direction; its *reading* is a coordinate on it (v/h, its angle θ, or its
share g of the quarter turn); the *law* of the addresses is a measure on the readings. With a third unit relation v₂,
read against the same h, the directions fill the positive octant, the *wedge*.

**Near field, levels, lay and zoom.** The *near field* is the readings up to the corner, v/h ≤ 1; with three unit
relations, those in which h is the largest. A *level* is a doubling, from 2^(j−1) to 2^j in a reading or a distance;
levels are counted in log₂. A *lay* places amounts along a line of addresses (§9); a *zoom* is a change of the reader's
H, which moves where every amount lies on the lay and changes no reading.

**Addresses and payload.** An address is a place where a reading can be put; the range of addresses is fixed by the
geometry before anything arrives. The *payload* is what arrives along an address: a wave of some kind, sent out or
shaped by the things read, not the things themselves. Nothing in it is a distance: of two things on one line the nearer
is the one met, and how far it lies does not arrive with it.

**The reader's ignorance as a group.** Jaynes's principle says that an observer which cannot tell two problems apart
must treat them alike; when the problems are related by a group, the measure to use is the one the group leaves
unchanged (Jaynes 1968, 1973). The situated reader does not know its *attitude* θ, which way its bar points, nor the
other party's size relative to its own, κ = V*/H, nor, from a reading alone, which unit relation the reading was divided
by. We take its ignorance to be this group:
1. a *turn*, θ ↦ θ + α;
2. a *rescaling* of the other party's size, κ ↦ λκ, which changes every amount of that party by one factor and no unit
   relation or reading;
3. the *exchange* v ↔ h, which sends a reading to its reciprocal and θ to 90° − θ. It acts on readings and drawings, not
   on κ.

The turns and rescalings act on separate unknowns and commute; the measure they leave unchanged is dθ·dκ/κ, their Haar
measure (Haar 1933), unique up to a constant factor. The exchange does not commute with the turns, but with them it forms the compact group O(2),
and with the abelian rescalings the whole group is unimodular and its left and right invariant measures coincide. The location-and-scale family's
affine group, x ↦ b + ax, is not, and has two invariant measures (Ghosh 2011); the reader's group has one. The turns act
on the whole circle of directions; the reader's quarter is that measure restricted, which the exchange carries onto
itself. What it gives: uniform in θ, once the
sweep is taken to be the turning of a bar (§4, §5); uniform in log κ, every level of the other's size alike, which governs
the estimate of the size (Proposition 8) and touches no reading; and the exchange's fixed point, the corner.

**What kind of measure this is.** The address law is neither a belief about what arrives nor a frequency of
arrivals. It is what Jaynes (1968) calls the invariant measure m(x): the measure fixed by the transformation group
alone, which enters his continuous entropy −∫ p·ln(p/m) dx as the reference against which any distribution is
measured, before any data. The Cauchy here is that m for the reader's group, the invariant measure of its directions.
What a reader observes, the readings of whatever arrives, has a law of its own, which depends on what arrives; the
invariant measure does not. Medians, means and samples are applied to it as to any measure, and what they say is said
of the reference, not of the world.

Being situated removes the translations Jaynes's straw-thrower keeps. A situated reader's lines all pass through home,
and the transformations that keep home are the turns and dilations about it; the measure they leave on the plane is
dx·dy/(x² + y²) = dθ·dr/r, uniform in direction and in levels of distance, not in area. Read from home, Bertrand's chord
has no single answer: for a circle of radius R whose centre is at distance D ≥ R, the share of uniformly turned rays
cutting a chord longer than the inscribed triangle's side is arcsin(R/2D)/arcsin(R/D), ⅓ from a home on the circle and
rising to Jaynes's ½ as the circle recedes; straws tossed since show a similar dependence on a ratio of two lengths
(Liu and Adams 2019).

The group is chosen, not derived. Jaynes's measure is a "pre-prior" on which a prior is built (1968), and Norton (2008)
argues that complete ignorance is not a probability at all. Here the measure is not built on: it is read as the reader's
addresses, and its main consequence is that the Cauchy belongs to them and not to what arrives (§5, §6).

## 3. The corner

**Proposition 1.** Let x = v/h ∈ [0, ∞). Then x = 1 is the only point fixed by the reciprocal x ↦ 1/x. The reciprocal
carries (0, 1) onto (1, ∞) point for point, and every sweep from home passes through x = 1. This point depends on
neither H nor V.

*Proof.* The reciprocal is its own inverse and reverses order, so x < 1 exactly when 1/x > 1, and for x > 0, x = 1/x
gives x = 1. A sweep from home grows continuously from 0, so it reaches 1 before it can pass it. And x = 1 means v = h, a
comparison of two unit relations, unchanged when both are scaled together. ∎

We call this point the *corner*. It separates two ways of reading: before it, v in terms of h; past it, h in terms of
v. On the whole projective line the exchange has a second fixed point, −1, off the reader's arc, and the two fixed
points are harmonic conjugates with respect to every pair the exchange swaps, home and the horizon among them (Coxeter
1987): once the exchange is given, the corner is fixed by projective structure alone, with no measure. Home and the
horizon do not fix it by themselves, since the maps x ↦ λx keep both and move 1; the exchange does, and swapping h with
v asks only that both be shares of one length, the reader's H.

**Proposition 2.** (a) Let a reader hold x in two registers: x itself where x ≤ a, and 1/x where x > a. Both registers
stay within [0, 1] if and only if a = 1. (b) Let f : (0, ∞) → [0, 1] be strictly increasing with f(1/x) = 1 − f(x).
Then f(1) = ½, and f maps the near side below ½ and the far side above it.

*Proof.* (a) The registers take values in [0, a] and (0, 1/a); both lie in [0, 1] exactly when a ≤ 1 and 1/a ≤ 1.
(b) At x = 1 the condition reads f(1) = 1 − f(1); the rest follows from monotonicity. ∎

Part (b) assumes the reading is *reciprocal-symmetric* (log-symmetric in Jones's terms, 2008). Without that, a bounded
reading such as x/(2 + x) has its middle at x = 2.

Order on the arc needs no division: for readings (h₁, v₁) and (h₂, v₂) the bracket D = v₁·h₂ − v₂·h₁ is zero exactly
when the two are one direction and, with h₁, h₂ > 0, positive exactly when v₁/h₁ > v₂/h₂; comparing a reading with its
own reciprocal gives D = v² − h², zero exactly at the corner.

## 4. The one-length circle

The circle here is the one an observer's single length traces when turned. From one place a reader has the open
quarter of it, its readings, whose law is the Cauchy; the closed circle, with its total turn and its π, is held by an
observer joining facings or standpoints, which is writing. Earlier versions called it "the reader's circle".

We assume:
- **(P0)** A relation requires two unit relations, h and v, each in [0, 1]. For a writer each relates its party to that
  party's breadth; a situated reader has no V, and for it both are shares of its own one length.
- **(P1)** A situated reader holds exactly one length, H, the value it starts from, and holds no whole of the system.

**Proposition 3 (the one-length circle).** Under (P0) and (P1):

(a) the reader holds no breadth for the other party, so there is no number c relating a second length to H; a writer,
holding the other's breadth, can write the reader's drawing on a page with two axes as V = cH, and no unit relation and
no single reading depends on c;

(b) the corner lies at distance 1 from home, measured in H, whatever H was chosen;

(c) if the attitudes of the relation are turns of one rigid bar of the reader's one length, the relation traces the
unit circle h² + v² = 1;

(d) on a page with two axes, all of v drawn at c times the length of all of h, the attitudes are turns of one rigid bar
only if c = 1;

(e) the bar can be derived rather than assumed. Take a sweep that is continuous and uniform (every step the same linear
map of the plane of all-h and all-v), that returns to its start after one full turn, and that carries all of h into all
of v in a quarter of it. Such a sweep preserves an inner product, unique up to a positive factor. In it all of h, all of
v and every attitude between have one length, all of v is square to all of h, and at the sweep's parameter t the unit
relations are (h, v) = (cos ωt, sin ωt). The one factor left free is that length, H.

*Proof.* (a) By (P1) the reader's only length is H, and by (P0) its v is a share of it; a reading v/h is a ratio of two
shares of one length. A unit relation lies in [0, 1] however large V is, so no reading involves c. (b) The corner is
one H from home measured in H. A reader with unit λH reading a world scaled by λ receives exactly the same readings, so
nothing in the readings fixes H. (c) With one length the relation is a bar of length 1 in H, so h² + v² = 1 when length
is Euclidean, and the Euclidean norm is, up to scale, the only norm preserved by every turn. (d) A turn keeps the bar's
length; on the page all of h is the bar at length H and all of v the bar at length cH, so a turn carries one to the
other only if c = 1.

(e) A continuous one-parameter group of linear maps has the form Φ(t) = exp(tA); let A ≠ 0 and T be the least time with
Φ(T) = I.
1. A real 2 × 2 matrix with exp(TA) = I has eigenvalues ±iω, ω = 2π/T. A pair of zero eigenvalues would make A
   nilpotent, and then exp(TA) = I + TA ≠ I.
2. So A = U(ωJ)U⁻¹, with J the generator of turns, and Φ(t) = U·R(ωt)·U⁻¹, which preserves Q(x) = |U⁻¹x|².
3. If a symmetric form G is preserved by every Φ(t), then UᵀGU is preserved by every turn, so it commutes with J; being
   symmetric, it is a multiple of the identity. So G is a multiple of Q.
4. Let u = U⁻¹(all of h). Since all of v = Φ(T/4)(all of h), U⁻¹(all of v) = R(π/2)u: the two are square and of one
   length in Q.
5. Then Φ(t)(all of h) = cos ωt·(all of h) + sin ωt·(all of v), so (h, v) = (cos ωt, sin ωt). ∎

With more unit relations the same holds on one condition: the sweeps together must stay bounded, generating a compact
group of linear maps. An inner product averaged over the group's Haar measure is then preserved, unique up to a factor
when the group carries every direction to every other, as the turns of the sphere do. Each sweep returning on its own
is not enough: two sweeps that each return, each in its own inner product, can compose to a map that grows without
bound.

Step 1 is Cauchy's exponential functional equation for matrices, Φ(t₁ + t₂) = Φ(t₁)Φ(t₂), whose continuous solutions are
exp(tA). Three layers are kept apart. *Assumed*: the sweep is continuous, composes, and returns. *Derived*: the
imaginary rate, an inner product the sweep preserves (not assumed: step 3), and Euler's form, h + iv = e^(iωt) in that
inner product. *Read*: that the return is what the reader's turn supplies, so that i enters as the generator of a
returning turn rather than as an added ingredient. That a returning one-parameter group has an imaginary generator is
classical; Euler's formula is used here, not derived.

**What V = H names.** V = H is a writer's name for the one-length circle. A writer, holding a breadth for the other party,
can draw it on a second axis; looking at the circle the reader's one length traces, it finds that axis drawn at H. The
reader set nothing: it has no V to set. Nor is V = H a claim that the other party has the reader's size. Where it does
not, every amount taken from the reader's drawing is off by V*/H, by the same factor on both sides of the corner.

Where a drawing does have two axes (a writer's page, a shore, a chart, an instrument), c is real, and c = 1 is the only
value for which the sweep is a rigid turn (part (d)) and the uniform turn's readings are reciprocal-symmetric with their
median at the corner (Proposition 4(c)). Part (e) narrows the Euclidean assumption: what remains assumed is that the
sweep acts linearly, one motion repeated, and returns.

## 5. The addresses are the Cauchy

The reader's one length, taken as 1, is a bar about home. Its directions from flat (all h) to upright (all v), under the
uniform measure on turn, are the *inscribed sweep*, and each is one reading v/h. "Steps" below are pieces of that
measure, not a motion.

**Proposition 4.** (a) Equal steps of turn give unequal readings: near zero a step barely changes v/h; the corner is
halfway through the turn; near upright each step changes v/h without bound.

(b) Counted per unit of v/h, the steps have density 2/(π(1 + (v/h)²)) on [0, ∞): the half-Cauchy distribution. Its
median is the corner, its quartiles √2 − 1 and √2 + 1, and the reciprocal leaves it unchanged. Over both quadrants,
with v/h signed, it is the standard Cauchy.

(c) *Conversely.* Let a page or an instrument with two axes draw all of v at c times the length of all of h, V = cH, and
sweep in equal steps of direction from home. Its readings v/h follow the law of (b), with the median at the corner and
unchanged by the reciprocal, if and only if c = 1.

(d) *Two other parties.* With a third unit relation v₂ read against the same h, sweep the positive octant uniformly by
area, and write s = v/h, s₂ = v₂/h. The readings (s, s₂) have density 2/(π(1 + s² + s₂²)^(3/2)) on [0, ∞)²; each of
v/h, v₂/h and v/v₂ alone has the law of (b), with its median at its own corner; and the six orderings of h, v and v₂ are
equally likely, so h is the largest, the reader near in both readings, for a third of the octant.

*Proof.* (b) When the bar turns by a small angle, v/h changes by that angle times 1/h², and on the circle
1/h² = 1 + (v/h)². Normalising over a quarter turn gives 2/π. The distribution function is (2/π)·arctan(v/h), ½ at
v/h = 1 and ¼ and ¾ at tan(π/8) and tan(3π/8); the substitution v/h ↦ h/v carries the density to itself. (c) A
direction θ′ in the drawing has tan θ′ = c·(v/h). With θ′ uniform on [0, π/2], P(v/h ≤ r) = (2/π)·arctan(cr): a
half-Cauchy of scale 1/c, median 1/c, which the reciprocal carries to scale c. It is the law of (b) exactly when c = 1.
(d) The point of the octant in direction (1, s, s₂) is (1, s, s₂)/r, r² = 1 + s² + s₂². Projected from the centre onto
the plane h = 1, an element ds·ds₂ subtends ds·ds₂/r³ of the sphere. Integrating s₂ out, ∫₀^∞ ds₂/(1 + s² + s₂²)^(3/2)
= 1/(1 + s²), the law of (b); in polar coordinates on the plane the angle is uniform, so v₂/v has it too. Exchanging any
two of h, v, v₂ keeps the octant and its area, so the six orderings have equal areas. ∎

**Why uniformly by area.** Part (d) takes the uniform area as its hypothesis, from the same premise as the uniform turn:
the reader treats its attitudes alike, under every turn, not only under exchanges of the named parties. With three unit
relations the turns are all the rotations of the sphere, and the only probability on the sphere every rotation leaves
unchanged is uniform area (Haar 1933). The exchanges alone do not fix it, and uniform in both of the two sweeping
angles, altitude and azimuth, is a chart, not this law: it moves the near field to 0.233. By Archimedes' hat-box
theorem, uniform area on the octant is uniform in azimuth and in height (Lambert's equal-area map, Lambert 1772). With n
other parties the readings have density Z_n·(1 + |s|²)^(−(n+1)/2), Z_n = 2ⁿ·Γ((n + 1)/2)/π^((n+1)/2), every pair keeps
its corner, and the reader is near in all readings for 1/(n + 1) of its addresses.

**Working back from the Cauchy.** Read backward from the known law, each step is forced by the one before. If the
readings follow (b), the angle arctan(v/h) is turned uniformly. That angle is the direction from the standpoint only if
all of h and all of v are one length, by (c); for the reader they are. With one length the sweep is a rigid bar turning,
and it traces the circle (Proposition 3). Stated as uniqueness and no more: among two-axis drawings V = cH whose sweep is
a rigid turn and whose readings are reciprocal-symmetric, the equal-length drawing c = 1 is the only one, and it gives
the half-Cauchy with its median at the corner. That a reader sweeps by a turn at all is the premise of Proposition 3(e),
not this result.

**Uniform in what.** Bertrand's lesson is that "uniform" needs a parameter, and different parameters give different
laws. On a page drawn at c = 2, uniform in the angle drawn on the page puts the quartiles of v/h at 0.207, 0.5 and
1.207, and uniform along the stretched curve at 0.316, 0.739 and 1.673. For the reader the parameter is fixed by
Proposition 3(e): its sweep is a flow Φ(t), one motion repeated, and in that flow's own inner product
(h, v) = (cos ωt, sin ωt). Uniform means uniform in t, the one parameter the flow carries, and then the readings are
the half-Cauchy, whatever page a writer later draws them on. The competing laws belong to the page, each uniform in a
parameter a writer's drawing adds: an angle measured on the stretched page, a length along its curve. So the exact law
is forced given the premises of Proposition 3(e) (a sweep that is continuous, linear and returning); whether a reader's
sweep is such a flow is the open question it leaves (§11, open question 2).

**Why a turn and not a boost.** The Möbius maps of the reader's line come in three kinds of one-parameter flow: the
elliptic (a turn), with no fixed point on the line; the hyperbolic (a boost), with two; the parabolic (a translation),
with one. Only the turn leaves unchanged a probability spread over the whole line, and that probability is the Cauchy;
under a boost or a translation every point off the fixed points moves monotonically toward one of them, so any
probability they keep sits on the fixed points. A measure on directions that treats every place alike and is unchanged
by its own motion comes only from a turn.

The readings are the tangent of a uniformly distributed angle, the gnomonic projection of a uniform direction; for two
other parties, the multivariate Cauchy, with Cauchy marginals (Cacoullos 2014). The gnomonic projection is a pinhole's
image plane, so the law of (d) is what a flat screen records of directions arriving uniformly over the octant, with
density (2/π)·cos³α at angle α off the axis.

## 6. The separation of address and payload

> **The Cauchy is not the payload; it is the address to the payload.**

Call a statistic of a set of readings an *address statistic* if it depends only on their order so that for every strictly
increasing f it picks out of f(X) the image of what it picks out of X (the ranks, the median, the quartiles), and a
*payload statistic* if it depends on their sizes (the mean, any sum). Which side of the corner a reading lies on is kept
only by the increasing maps that fix 1; it belongs to the exchange, not to order alone.

**Theorem 5 (the separation of address and payload).** Parts (a) and (d) concern the readings of Proposition 4; parts
(b) and (c) hold for any finite set of readings; part (e) drops both the circle and the uniform turn.

(a) *Nothing that arrives changes the Cauchy.* Suppose whatever arrives along each direction lies at some reach ℓ > 0,
which may differ from direction to direction and is unknown to the reader. In the reader's unit its components are ℓ·h
and ℓ·v, and the reading is (ℓ·v)/(ℓ·h) = v/h. The readings of Proposition 4 and their law are therefore the same
whatever arrives, and are fixed before anything does. What does not cancel is the ratio of amounts,
(v·V*)/(h·H) = (V*/H)·(v/h).

(b) *Address statistics ignore the payload.* For a finite set X of readings and any strictly increasing f, the set f(X)
has the same ranks as X, so every address statistic picks out the same element; for an odd count,
median f(X) = f(median X). Conversely, two sets with the same ranks are carried onto one another by some strictly
increasing f, so the ranks keep exactly what survives every such change, and nothing more.

(c) *Payload statistics do not, the mean among them.* Among the strictly increasing maps of (b), only an affine f commutes with the mean on
every set of readings. For convex f, mean f(X) ≥ f(mean X), with equality only if f is affine on the smallest interval
containing X.

(d) *The Cauchy is an address law.* Over one quadrant its median is v/h = 1, the corner, and its quartiles √2 ∓ 1 a
reciprocal pair. Its mean does not exist: ∫₀^s x·2/(π(1 + x²)) dx = (1/π)·ln(1 + s²) grows without bound.

(e) *The median needs only reciprocal symmetry, and the missing mean a density of h bounded away from zero near the
horizon.* Let the sweep follow any continuous path from all of h to all of v that comes near h = 0 only at its end,
with any weight, both unchanged by exchanging the two parties. Then the readings' law is unchanged by the reciprocal and
the corner is a median of it, the only one where the law increases strictly through 1. If moreover the law of h
has a density at least f₀ > 0 on some interval (0, δ), the mean does not exist.

*Proof.* (a) holds by construction, a reading being a direction; it is stated so that (b)–(e) can be read against it. (b) Strictly increasing maps preserve ranks; the converse follows by monotone
interpolation between matched points. (c) A strictly increasing f with f((a + b)/2) = (f(a) + f(b))/2 for all a, b is
affine, so a non-affine f fails it for some pair, and X = {a, b} is the set required. Monotonicity, or another
regularity, is needed: an additive function built on a Hamel basis commutes with the mean of every finite set without
being affine. The inequality is Jensen's. (d) The distribution function is (2/π)·arctan(v/h). (e) The exchange carries
v/h to h/v and leaves path and weight unchanged, so v/h and h/v have one law: P(v/h < 1) = P(v/h > 1), each at most ½,
and 1 is a median (for a continuous law, F(1/x) = 1 − F(x) and Proposition 2(b)). The path ends at all of v and comes
near h = 0 only there, so there are δ > 0 and v₀ > 0 with v ≥ v₀ wherever h < δ. Then P(v/h > r) ≥ P(h < v₀/r) ≥ f₀·v₀/r once
v₀/r < δ, so ∫ P(v/h > r) dr diverges, and so does the mean. ∎

The theorem is elementary; its content is the reading. The cancellation in (a) is an identity about this representation
of what arrives, an amount along a given direction; that the directions are the reader's addresses is this paper's
reading of it, and whether a particular instrument's arrivals have this form is a question about that instrument. The
addresses are given before anything arrives, and nothing that arrives moves them: (a) for every single reading, (b) for
every statistic of their order; (c) says why no statistic of size can be read from them. The Cauchy is not a law of
anything the reader meets. It is the reader's own layout of directions, counted.

**What depends on what.**

| result | the condition it needs |
|---|---|
| each reading a direction, unmoved by scaling the world | the addresses fixed before anything arrives; any weighting |
| the address law independent of the payload; ranks and medians commute with every increasing map | the addresses fixed before anything arrives; any weighting |
| the median at the corner | the weight unchanged by the reciprocal (the circle weighted by sin² 2θ keeps the median and has a mean, 4/π) |
| no mean | a density of h at least f₀ > 0 near the horizon; no symmetry needed |
| every pair's median at its own corner | each pair's weight unchanged by its own reciprocal |
| the exact Cauchy, its 2/π and quartiles √2 ∓ 1 | the uniform turn, or on the sphere uniform area |

Three paths from all of h to all of v, each swept uniformly along its own length, show what is left free. With g the
share of the sweep done when the direction θ is reached:

| path | g | at 22.5° | at 45° | at 67.5° |
|---|---|---|---|---|
| the circle, h² + v² = 1 | 2θ/π | 0.250 | ½ | 0.750 |
| the line, h + v = 1 | tan θ/(1 + tan θ) | 0.293 | ½ | 0.707 |
| the square's edges | tan θ/2, then 1 − cot θ/2 | 0.207 | ½ | 0.793 |

They agree at zero, the corner and the horizon and part between. None has a mean: the mean of the readings below s
grows by a fixed amount each time s grows tenfold, (2/π)·ln 10, ln 10 and (ln 10)/2. Only the circle is uniform in the
turn and gives the Cauchy's exact shape.

**An address is not a payload.** An address is a point: a direction, a place on the reader's line. A payload is what is
found at that point: an amount, a function on the addresses. The two share one place and nothing passes between them:
the address carries none of the payload, and the payload none of the address or its law. The distinction has to be
stated because a number on the real line carries no mark of which it is. Written as a value x = tan θ, one number is
both where a reading is made and what is read, so the law of the turn is read as a law of amounts, and a mean is asked
of it. This is a statement about that representation, not about anyone's results. Marked, the two separate exactly: the
address is a point of the projective line, where its law has a median and its missing mean belongs to the chart. On a
bounded chart of the same arc, the angle θ or the capped share x/(1 + x), the uniform turn has a mean, π/4 and ½; on
the level chart ξ = ln(v/h) its law is (1/π)·sech ξ, with every moment (Talacko 1956). The missing mean is a fact about
the chart x = v/h, not about the arc.

**Once a Cauchy, always a Cauchy.** Writing a Cauchy law with median m and scale γ as the point m + iγ of the upper
half-plane, a turn acts on the signed reading as a real Möbius map, and carries the law at z to the law at the image of
z (Knight 1976; McCullagh 1996). A new zero, the reciprocal and a zoom keep the family, moving only the point. A sum of
independent Cauchy variables is again Cauchy, the points m + iγ adding (Lévy 1925); read as addresses it is a relay of
standpoints: a uniform turn from height γ₁ + γ₂, landed on a line at height γ₂ and turned again from there down to the
base line, lands exactly as one turn from height γ₁ + γ₂ straight to the base line would. Averaging n signed readings gives the same Cauchy. All of this concerns the signed reading over two
quadrants; the reader's half-Cauchy on one quadrant is carried off its arc by a turn, and its average grows like
(2/π)·ln n. What breaks the family is an amount entering: squaring, a
cut at an edge, a random multiplier, an added amount (a Voigt profile), pooled standpoints, or a count against something
other than the turn. Even then an added amount of finite spread leaves the tails ~ γ/(πx²), so the Cauchy is lost first
near its centre and last at the horizon.

The plainest instance in practice is a spectral line, written as a strength times a profile, I(ν) = S·φ(ν − ν₀). The
strength is an amount; the strengths of separate lines add. The profile of a resonance is the Lorentzian,
φ(ν) = (1/π)·dδ/dν, with tan δ = γ/(ν₀ − ν): the frequency line laid by a uniform turn of the phase δ through half a
turn. Spectroscopy reads the profile by its centre and half-width and the strength by its integral: the address by its
order and the amount by its sum, as Theorem 5 says each must be read. We offer the rule as a reading, not a law of nature: a Cauchy variable is
a direction, read by its order, never an amount; where it appears beside an amount, find the turn and find the amount.

**What the reading changes.** The theorem is classical in its parts; what the reading adds shows in what it lets one
say. Four cases, each short and checkable. Their answers are known; what the reading adds is where each answer's facts
belong, to the addresses or to what arrives, and none says the usual treatment is wrong.

- *Water and wine.* Von Mises's problem: a liquid is wine and water, the ratio x of wine to water between 1/3 and 3;
  what is the chance that x ≤ 2 (von Mises 1928, in Mikkelson's 2004 form)? Indifference over x gives 5/8, over 1/x
  15/16, and the problem is the standard case of indifference contradicting itself; Jaynes left it open as
  overdetermined (1973, §8). Read as an address, x is a direction [water : wine]. The exchange of the two liquids
  carries it to its reciprocal, so every answer that treats them alike puts the chance of x ≤ 1 at ½, the corner,
  whatever else it assumes. A change of one liquid's unit multiplies x by a constant and moves no direction; if one law
  is to hold on every range of x, as Jaynes required of the chord, the only law left by both is dx/x, uniform in
  levels, and the answer is ln 6/ln 9 ≈ 0.8155 (the answers treating the liquids alike all agree at the corner and part past it: 5/6 uniform in the share of wine, 0.815 in levels).
- *The marginalization paradox.* Under an improper prior on a scale nuisance, integrating it out of the data and
  reasoning from statistics free of it can disagree (Stone and Dawid 1972; Dawid, Stone and Zidek 1973). Read with the
  reader's own measure on the other's size, dη/η, they cannot. For amounts y = η·w, n of them, the first reasoner's
  likelihood ∫ η^(−n−1) f(y/η | ζ) dη and the second's, from the direction u = y/|y| alone, ∫ r^(n−1) f(r·u | ζ) dr,
  differ by the factor |y|^n, which carries no ζ: the same conclusion from the same prior, whatever the law f. Reading
  the data's direction is reading its address, and the scale's invariant measure is what makes the two agree (§11, open question 4).
- *Bertrand from a standpoint.* Bertrand's chord has as many answers as procedures; Jaynes's ½ comes from a group that
  includes translations, a circle that may lie anywhere. A reader that stands somewhere has no translations: its lines
  all pass through home, and its measure is uniform in direction and in levels of distance. For a circle of radius R
  whose centre is D ≥ R away, the share of rays cutting a chord longer than the inscribed triangle's side is
  arcsin(R/2D)/arcsin(R/D): ⅓ from a point of the circle, rising to ½ as the circle recedes. Jaynes's answer is the far
  reader's, Bertrand's chord between two random ends the near reader's, and the answer depends on where the circle lies
  relative to the one who asks (§2).
- *Directions are read by their order.* Robust statistics treats a Cauchy tail as outliers in the data, to be resisted by
  medians and bounded-influence estimators (Huber 1964). Read as addresses the same readings need no defence: a ratio of
  two amounts (a slope, a ratio estimate, the tangent of a bearing) is a direction, and read in that chart its law
  has a median and no mean; the mean belongs to a bounded chart, the angle. Over a uniform turn the readings' median stays at 1 while the mean's
  integral up to s, (1/π)·ln(1 + s²), grows by (2/π)·ln 10 for every tenfold of s. To summarize directions, take the median or the
  quartiles; to combine two, compose them by tangent addition; to average, average the angle, which is bounded. The mean
  belongs to amounts, the median to addresses (Theorem 5(b), (c)).

**What is observed, and what the reading predicts.** The address law is not the law of anything observed, and the two
are easily run together: every Cauchy met in practice, a ratio of two normal amounts, a heavy-tailed sample, a line's
profile, is the law of something observed. The reading relates them. Counted against what arrives, the readings' law is
the turn's law weighted by how what arrives is spread over the directions (§2). It is the Cauchy exactly when what
arrives is spread evenly over the reader's addresses, as a pair of independent centred normal amounts of equal spread
is, its direction uniform by turn. So the reading makes a claim the usual readings do not: an observed law of Cauchy
type has a uniform turn behind it (a rotation, a phase advancing steadily, or the direction of a pair of
independent amounts of one spread), and its departure from the Cauchy is the
spread of what arrives over directions, which can be measured on its own. Its median stays at the corner exactly when
that spread weighs the two sides of the corner alike (Theorem 5(e)), and moves only by the part that does not. That is the test,
and it can fail: a Cauchy-type law met in practice with no uniform turn to be named behind it, or whose departure from
the Cauchy the independently measured spread of what arrives does not account for, counts against the reading. Writing a
law as the tangent of some uniform variable does not pass the test; the turn has to be there.

**A case in data.** Open data from the LIGO detectors show the sort (Abbott et al. 2023): 512 s from GPS 1257000000,
Hanford (H1) and Livingston (L1), each whitened, 2,080,768 samples each. Taken one detector at a time, the whitened strain
is an amount, and fitted sample by sample a Cauchy beats a Gaussian by a wide margin; read as the law of what is
measured, that suggests a Cauchy in the noise. Read the other way it is a tail of finite spread made by one loud
transient (a Student-t with about 16 degrees of freedom fits far better than either), and the block means of the amounts
shrink as n^(−1/2) through the whitened band, which nothing with a Cauchy law could do. The Cauchy is elsewhere: in the
direction [H1 : L1] of the two detectors read at one instant, a pair of nearly independent noises whose direction is
close to uniform: its angle is 0.009 from the uniform law in Kolmogorov distance, small but, at two million samples, more
than sampling explains, as the channels' unequal spreads and the transient lead one to expect. On two further
segments, with the predictions written down before the data were fetched, all of what follows held again, and the
reading's test, which could have failed, did not: pairing each sample of one detector with the other's 8 s away, which
keeps each channel's own law and loses their joint timing, reproduces the angle's departure from uniform (0.0076 and
0.0061, against a sampling scale of 0.0009) to within 0.0001. The departure is the spread of what arrives, measured from
each channel alone. Drawn at one length by each channel's own
interquartile range, the median of |L1/H1| is 0.999 and the quartiles of L1/H1 are −0.998 and +1.000; averaged over
blocks of up to 1,024 samples its spread does not shrink; scaling one channel by c moves the median to c exactly; and
removing the loudest 0.1% of samples, which takes the whole of the heavy tail, leaves the angle's law where it was.
Whitened instead by each channel's own spectrum, one of them inflated by the transient, the median sits at 0.93: that
offset is the drawing c, not anything in the detectors. Nothing here is new physics; ratios of independent centred
normals, the central limit theorem and transient detector noise are all known. What the reading supplies is where to
look, in the direction and not in the amount, and what a departure from the Cauchy is evidence of.

**A second case: the quasar dipole.** A reader moving at speed β through a sky of sources counts more of them ahead.
With no limit on brightness the census is a count of directions: the boost carries the uniform sky into a spherical
Cauchy (Kato and McCullagh 2020), and the count's dipole is 2β to first order, Ellis and Baldwin's "2", from the addresses alone (Ellis and
Baldwin 1984). Every real census is cut at a flux limit, and the cut adds x(1 + α)β, where x is the slope of the counts
and α the sources' spectral index, both read from the same catalogue: the payload's weighting, entering through what
arrives at each address. The separation says which part of the expected dipole is which. On Secrest et al.'s CatWISE
quasars (2021) the payload's term is about two thirds of the 0.0074 expected. Four disjoint brightness slices give one
β, (3.31 ± 0.27) × 10⁻³, as one boost should, though 2.7 times the cosmic microwave background's; three colour slices
disagree with one another, which no boost can do, so part of the dipole belongs to the sources themselves, what arrives,
and not to the reader's motion. The sort does not settle the dipole's origin. It says where to look: an excess that every
brightness slice shares behaves as one boost, and one that varies with colour belongs to what arrives.

**A third case: one photon at a time.** In a double slit lit one photon at a time, each photon arrives at one place on
the screen, and the fringes are built by many. With the two paths' amplitudes as h and v, the fringe visibility is at
most 2hv and the which-path predictability is |h² − v²|, so V² + P² ≤ 1 (Greenberger and Yasin 1988; Englert 1996): the
central sweep's height and foot (§7), full visibility only at the corner. On Aspden, Padgett and Spalding's frames (2016)
the two slits' shares give 2hv = 0.997 and 1.000, the pair at its corner; the measured contrast, 0.69 and 0.56, lies
under that bound, short by the source's coherence; the photons are independent draws from one pattern that does not
drift, and the fringe period is fλ/d to 0.3% and 1.7%. The bound is set by the two shares alone, the geometry's; how far
below it a pattern falls is the source's, what arrives. All of this is classical; the reading is the sort.

## 7. The two sweeps meet at one point

The addresses have a second reading. Stand the two parties at the ends of a chord AB of length 1, A at home. From A, a
ray reading s = v/h turns through the inscribed angle θ; from the middle M of the chord, the radius of the circle on AB
(the Thales circle) turns through the central angle. The ray at θ and the radius at 2θ end at the same point P of the
arc, for every θ: an angle at the circle is half the angle at the centre on the same arc (*Elements* III.20). P is the
foot of the perpendicular from B onto the ray (*Elements* III.31); its distances from A and B are h and v, its foot on
the chord at h², its height hv (*Elements* VI.8).

So one direction has two readings. The *inscribed sweep*, from a point of the circle through a quarter turn, gives the
address. The *central sweep*, from the centre through a half turn, reaches the landing point P. These are the only two
kinds of pivot from which equal turns cut equal arcs: taking the radius as 1, from a pivot inside the circle at distance p from the centre, a step of
turn moves the point ahead by 2t/(t + t′) of arc, t and t′ the distances ahead and behind, which is constant only at
p = 0 or with t′ = 0, the pivot on the circle; from a pivot outside the circle the rate grows without bound toward the
two rays that graze it. Three things are kept apart: the address, the direction of the ray; the
landing point P; and the payload, what arrives at P. The theorem gives the shared point; reading the payload as met
there is our interpretation.

**The central point is the inscribed direction squared.** The radius at 2θ ends at
½(cos 2θ, sin 2θ) = ½(h² − v², 2hv) = ½(h + iv)² = ½e^(2iθ). The sweep about a party gives ratios, of the first degree,
unbounded, held by the median; the sweep about the pair's middle gives squares, of the second degree, bounded, with
means (cos 2θ averages 0 and sin 2θ averages 2/π over a uniform turn). At zero, the corner and the horizon the landing
point is at +1, i and −1 (times ½): the half turn from zero's landing point, B, to the horizon's, which is home, is
e^(iπ) = −1. The
two are one classical map, the Cayley transform w = (s − i)/(s + i), which sends the reading s = tan θ to −e^(2iθ) and
the standpoint i to the centre of the disc (Cayley 1846); under it the Cauchy is the harmonic measure from i. That one
law is both the Möbius image of the uniform turn and harmonic measure is a fact of the plane: on the sphere the two
part (Kato and McCullagh 2020 give the first), so a statement about a standpoint off the centre in three dimensions has
to say which it means.

**What the two sweeps return.** A writer holds a line of true breadth 1 as 1. Measured by the writer through the
central sweep it is an arc, a half turn about the centre, π/2; through the inscribed sweep, its projection over the turn,
2/π. Both numbers have π in them and are the writer's; from one place the reader has its readings and their corner. Their product, not their
difference (π/2 − 2/π ≈ 0.934), gives the 1 back, and what it gives back is the reader's own H measured in H, not the
true breadth of anything read. Out to 45° the same two readings are θ/sin θ = 1.1107 and sin θ/θ = 0.9003, with product
1 again. Both rates are exact only on the circle; on the ellipse of a stretched drawing the inscribed angle theorem
fails, and the radius no longer turns twice the address's angle.

## 8. What no reading carries

**Proposition 6 (scale cannot be read).** Let a reader's observations be any collection of readings, each a ratio of
two amounts in the scene: sizes, distances, the separation between two of its standpoints. Then:

(a) multiplying every amount in the scene by one factor λ > 0 leaves every observation unchanged, so no collection of
such observations, from any number of standpoints, fixes the scale;

(b) if one amount L₀ is supplied from outside the readings, every amount that the readings link to L₀ is fixed.

*Proof.* (a) (λa)/(λb) = a/b. (b) If a reading links a to L₀, directly or through a chain whose ratios multiply to
a/L₀, then a = L₀ times that product, and λ = 1 is the only factor that leaves L₀ fixed. ∎

This is the ground of dimensional analysis, in which only dimensionless ratios of amounts enter a law (Buckingham 1914).
A survey is (b) in use: thousands of angles read, one base walked, every side written; a second base checks and adds no
scale (Snellius 1617; Roy 1785).

**Proposition 7 (standpoints bring back the figure).** Each reader reads only directions. Then: (a) one reader fixes,
for each place, only a line through it; (b) two readers whose placement relative to each other is known up to scale, reading
directions in one frame, fix every place both see that is not in line with them both, up to one common scale; (c) one agreed length between them fixes the scale.

*Proof.* (a) A direction from a known point is a line. (b) Two non-parallel lines from different points meet in one
point, and moving both readers by a common similarity moves every meeting point by the same similarity. (c) By
Proposition 6(b). ∎

One reader's readings, however many, fix no place: laid out with nothing else they return the circle of §4, the same
from every figure. The figure comes back from a second standpoint, and its size from an agreed length. This is
triangulation; that two views fix a scene up to its scale is the basis of reconstruction from two images
(Longuet-Higgins 1981).

**Proposition 8 (the best estimate is the median).** Measure the error of an estimate ĉH of the other party's size V*
by |f(V*) − f(ĉH)| for an increasing f.

(a) If the reader knows only V₋ ≤ V* ≤ V₊, the estimate whose worst error in levels (f = log₂) is least is
ĉH = √(V₋·V₊), the corner of the pair of bounds, with worst error ½·log(V₊/V₋).

(b) If the reader holds a distribution for V*, the estimate whose expected error is least is a median of it, the same
median for every increasing f. The mean, best under squared error in amounts, changes with f and need not exist.

(c) If nothing the reader knows makes the other larger rather than smaller, as bounds H/R ≤ V* ≤ H·R for some R ≥ 1 or
as a proper law for log(V*/H) symmetric about 0, both give ĉH = H. The improper dκ/κ alone has no median and gives no
estimate.

*Proof.* (a) The worst error is least when log ĉH is midway between log V₋ and log V₊. (b) E|X − m| is least at a median
of X, and medians commute with increasing maps (Theorem 5(b)). (c) The bounds H/R and H·R have geometric mean H,
and a proper law symmetric in log(V*/H) has median 0. ∎

So designating the other party, reading it on the reader's one length, is free and gives the geometry; sizing it is the
one guessed number, corrected by a shift in levels when an amount arrives. The estimate rests on measuring error by order
or in levels, the indifference to scale of §2: an error unchanged when κ and the estimate are rescaled together, and
alike for larger and smaller, is a function of |ln(κ/ĉ)|.

**Two tests.** The paper's two distinctions can be applied without accepting its reading, by two tests anyone can run
on any quantity.
- *Scale the world.* Multiply every breadth and distance by one factor k. A quantity that does not change is a reading:
  a direction, an angle, a ratio of two breadths, a shape held over its own mean. A quantity that changes by k is a
  writing, an amount in a named unit, and somewhere an amount was carried in to state it (Proposition 6). In the worked example
  (§10) every reading of the mountain range is the same at k = 1/10, 1 and 100 (a range 2, 20 or 2,000 miles wide); its width and distance in miles move by
  k, and are had only once one thumb is walked.
- *Change what arrives.* Replace what arrives along each direction by something else, keeping the directions. A quantity
  that does not change belongs to the addresses; one that changes belongs to the payload (Theorem 5(a)). On data the replacement
  can be made by pairing each reading of one detector with another instant's reading of the other, which keeps each
  channel's own law and changes what arrives together: in LIGO's noise the direction's law did not change, so its
  departure from the uniform turn belongs to each channel's own spread, not to anything the two share (§6, "A case in data").

Together the tests sort a fact four ways: readings of the addresses (the corner, the quartiles of directions), readings
of what arrives (a colour, a ratio of intensities), and writings of either (a range in metres, a flux in a unit). Neither
test needs the paper's vocabulary to be run.

**Ratios suffice.** Everything a reader does from where it stands is done in ratios to its own H: every reading is a
ratio with no unit (Proposition 6(a)); the addresses, their law and the corner are given before anything arrives
(Theorem 5); order and the median survive every change of payload; more standpoints bring back the figure up to its size
(Proposition 7). A blueprint, the writer's statement in amounts, adds what no reading supplies: the size, parts made
apart that must meet, sums of amounts, and a statement of the whole before it exists. It is a capability added to the
ratios, not a condition of them.

## 9. Past the corner, and the reader's one length as a zoom

Inside the corner the reader can lay its readings in proportion. Past it the reading h/v ∈ [0, 1] does not say how far
things should be laid out. Let a lay place a far amount x = d/H ≥ 1, a distance in units of H (which a reader has only
from a second standpoint or an amount carried in, §8), at position L(x), counting addresses from home, with L increasing
and L(1) = 1. Choosing a different H multiplies every such x by one factor, so a lay whose room depended on where a
reading sits would depend on the arbitrary H. We therefore require:

> **(S)** L(λx) − L(x) depends on λ alone, for all x, λ ≥ 1.

**Proposition 9.** If L is increasing and satisfies (S), then L(x) = 1 + k·ln x for some k > 0: every doubling receives
the same number of addresses, k·ln 2. If the far lay also joins the near lay L(x) = x without a kink at the corner, then
k = 1.

*Proof.* With f(λ) = L(λ) − 1, (S) gives f(λμ) = f(λ) + f(μ) for λ, μ ≥ 1: Cauchy's functional equation in
multiplicative form (Cauchy 1821), whose increasing solutions are k·ln λ. At x = 1 the near lay has slope 1 and the far
slope k. ∎

(S) does the work, and it is assumed, motivated by Proposition 3(b) and not derived: monotonicity, a fixed corner and a
matched slope are not enough, since 1 + ln x + α(ln x)² satisfies all three. (The reader holds the count of addresses
a doubling; the smooth logarithm is the writer's formula for it.) It passes through amounts. A second route
stays with ratios: relations chain by multiplying, v/h = (v/m)·(m/h), and a measure under which chained relations add
and which grows with the relation can only be k·ln. The turn is not such a measure, and read against ln(v/h) it is
arctan(v/h) = π/4 + ½·gd(ln(v/h)), the Gudermannian: the logarithm seen whole from one side, the turn per doubling past
the corner falling 18.4°, 12.5°, 6.9°, 3.5°, 1.8°, … by a ratio tending to 2. Measured by length instead of by count,
the far field fits in one more H: the in-place lay 2 − h/v gives level j past the corner length 2^(−j), the room per unit
of v/h being (h/v)², the Jacobian of the reciprocal.

**A fixed count, aimed by H.** Let the reader hold a fixed number K of addresses, laid at equal steps of the turn. Read a
distance d against H as a pair, the direction [H : d], as the reader reads any pair; once d/H is had (§8), the K
address boundaries lie along distance at H·tan(kπ/2K) (the writer's formula for where the reader's addresses fall), k = 1, …, K − 1, the last address running to the horizon, half of them inside H at every H; a larger H gives the near field less detail and
reaches farther, a smaller H the reverse. Every H gives the same geometry; its value sets only the zoom. The K
addresses hold any number of things, with no table and no count of them, though things sharing an address arrive there
as one. H cannot be declined: without a length there is no relation, and an H that favours no value is H at 0 or ∞,
where the lay loses its corner and a finite reader loses what it reads.

## 10. A worked example

A reader looks at a mountain range, face on, from opposite its middle. As writers we know three amounts: the reader's
thumb H = 1 mile (whatever single measure it holds), the range's width V* = 20 miles, its distance d = 10 miles. The
reader knows only its thumb.

1. *The addresses come first.* The one-length circle has radius 1 mile, its corner at 1 mile: proportional addresses
   inside, and past it the same number of addresses for each doubling. All of this is laid whether or not anything is
   there.
2. *What it reads exactly.* Zero, v/h = 0, is straight ahead at the middle of the range, and its ends are at v/h = ±1,
   exactly at the reader's corners, since the pair (V*/2, d) = (10, 10) is at its own corner. With directions spread
   uniformly over the half turn, the range takes exactly the middle half of them, between the Cauchy's quartiles, and
   the median points at its middle.
3. *The two sweeps, on the thumb.* On the thumb's circle each quarter turn is an arc of π/2 thumbs over a projection of
   1 thumb. Measured by a writer through the central sweep the half turn gives π/2, through the inscribed sweep 2/π (with 36 directions at the midpoints of 36 equal steps
   of the half turn the mean projection is 0.6368; 0.6367 over a quarter); their product is 1, the thumb measured in thumbs. A range 2 miles wide at 1 mile gives the
   same directions and the same products.
4. *What it cannot read.* A range 20 miles wide at 10 miles, 2 at 1 or 2,000 at 1,000 gives the same readings
   (Theorem 5(a)).
5. *The reader's drawing.* A writer reading amounts off the one-length circle takes the range to be one thumb wide, and
   the width-to-distance reading of 2 then puts it half a mile away. Every amount is off by V*/H = 20, by the same factor
   on both sides of the corner: a rigid shift of log₂ 20 ≈ 4.32 levels, the pattern of readings untouched.
6. *Constructing the truth.* Walk one H toward the range: its half-angle grows from 45° to 48.0°, the reading from s = 1
   to s′ = 10/9. Then d = H·s′/(s′ − s) = 10 miles and V* = 2·s·d = 20 miles. The walk is where an amount enters, the
   reader's own H walked once as a baseline (Proposition 7); the 20 is constructed from two standpoints and observed
   from neither.

The same for every reader, and exact: the directions, the corner at the range's ends, the range's share of the Cauchy,
and the two sweeps' readings of the thumb. The payload's: the 10 and the 20, which the reader has only by construction.

## 11. Discussion

**The principle, and what is claimed.** The results rest on one principle: a situated reader gives equal addresses to
whatever its readings cannot tell apart. This is Jaynes's principle of transformation groups, read as a rule for
addresses rather than for belief, applied to a group chosen as the reader's ignorance. The geometry is therefore
necessary relative to a stated ignorance, not absolutely. From that premise and the reader's one length, with the sweep
taken as a linear returning turn, come the circle, the corner and the median, the uniform turn and the Cauchy, and,
through amounts and premise (S), the logarithm past the corner. Each relaxation gives a named alternative rather than no
geometry: a second length gives c ≠ 1 and the Cauchy's median off the corner; a preferred direction gives the square's or
the line's law, the median at the corner and the missing mean intact; a preferred scale gives a lay that stops there.
The main result's core, order surviving and sums failing with the median at the corner, needs only reciprocal symmetry;
the missing mean needs besides a density bounded away from zero near the horizon.

On the reading itself a different group acts and should not be confused with the reader's ignorance: turns and changes
of a two-axis drawing generate PSL(2,ℝ) on the signed reading, the Cauchy family is the orbit of the standard Cauchy,
on which it acts transitively (Knight 1976; McCullagh 1996), and as points m + iγ that family is the hyperbolic plane on which it acts. The
drawings V = cH are the points i/c, at distance |ln(c′/c)| apart in the Cayley–Klein metric (Cayley 1859; Klein 1871). The reader holds no c, so this group is not part of
its ignorance; its one use here is to measure distances.

**What would follow.** If the reading is right, it changes less what is computed than what the results are taken to say. We state the
consequences as such, and as questions, not as claims about anyone's results.

- *What a missing mean is evidence of.* A law with no mean is usually taken as a fact about what was measured: heavy
  tails, outliers, an unruly system. On this reading it is first a question: is the variable a direction, a ratio of two
  amounts whose common scale the reading does not carry? If so, the missing mean need say nothing about the system; it is
  what any law of directions does, and the median and the quartiles are the summaries that mean something. Ratio
  estimates, slopes fitted with error in both coordinates, and bearings are the obvious places to ask.
- *Which part of a line shape belongs to the source.* Where a Cauchy appears as a profile beside a strength, the reading
  splits them: the strength is the amount, the profile a law of addresses fixed by a standpoint m + iγ. A change in the
  profile is then a change of where the turn is made from, and that is worth asking before it is read as a change in
  what is emitted.
- *What an invariant prior is.* Jaynes's invariant measure, read as a reference for directions rather than a belief, has
  a plain job: it lays the addresses before anything arrives, and the posterior lives on what arrives at them. Problems
  of the Bertrand kind then become questions of standpoint: the answer depends on where the one who asks stands, and an
  answer that ignores the standpoint is the far reader's.
- *What an address scheme costs.* A reader's addresses are given by its one length and the turn, with no table, no
  count of what will arrive and no knowledge of how far it reaches. Systems that index directions (cameras, depth
  buffers, samplers, maps) can be read against that baseline: what they add to it, and what they pay for it.

The reading predicts no new number, but it makes a claim that can fail (§6, "What is observed, and what the reading predicts").

**Open questions.**
1. *The premise (S).* It is scale invariance of the lay's increments, motivated and assumed. Is there a thinner premise
   about situated readers from which it follows? Real readers have preferred scales, their own resolution among them;
   here a preferred scale sets where the lay stops, and (S) is claimed only within that range.
2. *Why the uniform turn?* The readings are directions only, so the norm enters only through the measure on directions.
   Proposition 3(e) answers part of it: a sweep that is continuous, linear and returning preserves an inner product of its own.
   Drory (2015) objects to Jaynes's chord that the same symmetries imposed in different ways give different measures,
   depending on how the random selection is made. We grant it: which selection is made is a choice of what the turn is
   counted against (the turn itself, a clock, a flat screen, a count of arrivals). The core survives the choice: any
   selection that treats the two parties alike keeps the median at the corner (Theorem 5(e)).
3. *Whether real readers sweep by a turn.* That a reader should sweep by a turn of its one length, with nothing imposing
   a c, is what the propositions show given the stated group and premises, a conditional in the sense of Jaynes's principle. Whether a particular eye, brain or instrument does,
   and whether what its readings pass through imposes a c (unequal gains, pixels that are not square), is empirical, and
   not taken up here.
4. *Measures that cannot be normalized.* The reader's dκ/κ has no total, and such measures on a nuisance can produce
   the marginalization paradoxes of Stone and Dawid (1972) and Dawid, Stone and Zidek (1973). Under a scale nuisance's
   own measure dη/η, integrating it out of amounts agrees with reasoning from the data's direction alone, with the same
   prior, whatever the law: the substitution η = 1/λ turns one reasoner's likelihood into |y|^(−n) times the other's.
   This is the group condition Jaynes (1980) reports; the reader's size is such a nuisance.

**Where the conclusions do not follow.** An observer holding two independent lengths reads with two axes and has a c;
unless c = 1 it has no circle and no turn. A level with more structure than its two ends, their order and the
reciprocal admits other subdivisions. A reading that disturbs what it reads, as a quantum measurement does, falls
outside Theorem 5(a), which assumes that what arrives is the same whichever address meets it.

**Related work.** The pieces are classical: the reciprocal, the Cauchy as the projection of a uniform angle and its
Möbius invariance (Knight 1976; McCullagh 1996), the multivariate Cauchy's marginals (Cacoullos 2014), log-symmetric
laws (Jones 2008), Cauchy's functional equation, Klein's programme (1872) and the invariant priors of Jeffreys (1939)
and Jaynes, on which this paper builds. Our use of Jaynes is conditional in the sense of the critics named in §1: the group is chosen, and with it the measure. What is ours is the group, and the reading of its invariant measure as the reader's addresses rather than as a belief. Directional statistics reads directions on bounded charts, where mean directions exist (Mardia and Jupp 2000); structural inference builds inference on the group that generates the data (Fraser 1968). Leonard (2011) puts the Cauchy, the slope's law invariant under turns, on the
slope of a line fitted with error in both coordinates, with inference unchanged by exchanging and rescaling the
coordinates, the nearest use we know of these three transformations together. Scales linear near a unit and logarithmic
far from it are common, astronomy's asinh magnitudes among them (Lupton, Gunn and Szalay 1999); what §9 adds is the
join at the reciprocal's fixed point. Near neighbours in perception include Gilinsky's perceived distance with a finite
horizon (1951) and Schwartz's log-polar map of visual cortex (1977). In two-path interference, with the paths'
amplitudes as h and v, the fringe visibility is at most 2hv and the which-path predictability |h² − v²|, whole only at
the corner (Greenberger and Yasin 1988; Englert 1996). What we claim is not the pieces but their reading as one
structure, set by what a reader knows of two breadths, and in particular that the Cauchy distribution is a situated
reader's addresses, not its payload.

**What the geometry gives free.** Once the reader holds H, some structures follow with no further choice: a zoom, the
value of H; a split between near and far, the corner; readings no change of the world's size can move; and, given a
uniform sweep, addresses for any number of things with no table and no count. Others are free given one premise more:
precision far off (the logarithmic lay, given (S)), and a level of detail, given a fixed count of addresses. This is a
claim about where these structures come from, not about how well any system that uses them performs.

## Acknowledgements

Drafting, checking and editing were done with the assistance of an AI system (Claude, Anthropic), under the author's
direction; the numerical claims were checked by exact computation, and the author takes responsibility for the content.

## References

Abbott, R. et al. (LIGO Scientific Collaboration, Virgo Collaboration and KAGRA Collaboration) (2023). Open data from
the third observing run of LIGO, Virgo, KAGRA and GEO. *Astrophysical Journal Supplement Series* 267, 29.

Archimedes (c. 225 BC). *On the Sphere and Cylinder*.

Aspden, R. S., Padgett, M. J. and Spalding, G. C. (2016). Video recording true single-photon double-slit interference.
*American Journal of Physics* 84, 671. Data: University of Glasgow Enlighten repository, doi:10.5525/gla.researchdata.281.

Bertrand, J. (1889). *Calcul des probabilités*. Gauthier-Villars, Paris.

Breit, G. and Wigner, E. (1936). Capture of slow neutrons. *Physical Review* 49(7), 519–531.

Brinkman, T. (2026). *Observation from Somewhere: addresses given, payloads met* (long version). https://github.com/reportbase/wander/blob/main/papers/observation-from-somewhere.md

Buckingham, E. (1914). On physically similar systems; illustrations of the use of dimensional equations. *Physical
Review* 4(4), 345–376.

Cacoullos, T. (2014). Polar angle tangent vectors follow Cauchy distributions under spherical symmetry. *Journal of
Multivariate Analysis* 128, 147–153.

Cauchy, A.-L. (1821). *Cours d'analyse de l'École royale polytechnique. Première partie: Analyse algébrique*.
Paris: Debure, ch. 5.

Cayley, A. (1846). Sur quelques propriétés des déterminants gauches. *Journal für die reine und angewandte Mathematik*
32, 119–123.

Cayley, A. (1859). A sixth memoir upon quantics. *Philosophical Transactions of the Royal Society of London* 149,
61–90.

Coxeter, H. S. M. (1987). *Projective Geometry*, 2nd ed. Springer, New York.

Dawid, A. P., Stone, M. and Zidek, J. V. (1973). Marginalization paradoxes in Bayesian and structural inference.
*Journal of the Royal Statistical Society B* 35(2), 189–233.

Drory, A. (2015). Failure and uses of Jaynes' principle of transformation groups. *Foundations of Physics* 45(4),
439–460.

Ellis, G. F. R. and Baldwin, J. E. (1984). On the expected anisotropy of radio source counts. *Monthly Notices of the
Royal Astronomical Society* 206, 377.

Englert, B.-G. (1996). Fringe visibility and which-way information: an inequality. *Physical Review Letters* 77,
2154–2157.

Euclid (c. 300 BC). *Elements*. Translated by T. L. Heath (1908), *The Thirteen Books of Euclid's Elements*. Cambridge
University Press.

Feller, W. (1971). *An Introduction to Probability Theory and Its Applications*, vol. II, 2nd ed. Wiley, New York.

van Fraassen, B. C. (1989). *Laws and Symmetry*. Oxford University Press.

Fraser, D. A. S. (1968). *The Structure of Inference*. Wiley, New York.

Ghosh, M. (2011). Objective priors: an introduction for frequentists. *Statistical Science* 26(2), 187–202.

Gilinsky, A. S. (1951). Perceived size and distance in visual space. *Psychological Review* 58, 460–482.

Greenberger, D. M. and Yasin, A. (1988). Simultaneous wave and particle knowledge in a neutron interferometer.
*Physics Letters A* 128, 391–394.

Gull, S. F. (1988). Bayesian inductive inference and maximum entropy. In G. J. Erickson and C. R. Smith (eds),
*Maximum-Entropy and Bayesian Methods in Science and Engineering*, vol. 1, 53–74. Kluwer, Dordrecht.

Haar, A. (1933). Der Massbegriff in der Theorie der kontinuierlichen Gruppen. *Annals of Mathematics* 34(1), 147–169.

Huber, P. J. (1964). Robust estimation of a location parameter. *Annals of Mathematical Statistics* 35(1), 73–101.

Jaynes, E. T. (1968). Prior probabilities. *IEEE Transactions on Systems Science and Cybernetics* 4(3), 227–241.

Jaynes, E. T. (1973). The well-posed problem. *Foundations of Physics* 3(4), 477–493.

Jaynes, E. T. (1980). Marginalization and prior probabilities. In A. Zellner (ed.), *Bayesian Analysis in
Econometrics and Statistics: Essays in Honor of Harold Jeffreys*. North-Holland, Amsterdam. Reprinted in R. D.
Rosenkrantz (ed.) (1989), *E. T. Jaynes: Papers on Probability, Statistics and Statistical Physics*, Reidel, 337–375.

Jeffreys, H. (1939). *Theory of Probability*. Oxford University Press.

Jones, M. C. (2008). On reciprocal symmetry. *Journal of Statistical Planning and Inference* 138(10), 3039–3043.

Kakutani, S. (1944). Two-dimensional Brownian motion and harmonic functions. *Proceedings of the Imperial Academy
Tokyo* 20(10), 706–714.

Kass, R. E. and Wasserman, L. (1996). The selection of prior distributions by formal rules. *Journal of the American
Statistical Association* 91, 1343–1370.

Kato, S. and McCullagh, P. (2020). Some properties of a Cauchy family on the sphere derived from the Möbius
transformations. *Bernoulli* 26(4), 3224–3248.

Klein, F. (1871). Über die sogenannte Nicht-Euklidische Geometrie. *Mathematische Annalen* 4, 573–625.

Klein, F. (1872). *Vergleichende Betrachtungen über neuere geometrische Forschungen* (the Erlangen programme).

Knight, F. B. (1976). A characterization of the Cauchy type. *Proceedings of the American Mathematical Society* 55,
130–135.

Lambert, J. H. (1772). *Anmerkungen und Zusätze zur Entwerfung der Land- und Himmelscharten*. Berlin.

Leonard, D. (2011). Estimating a bivariate linear relationship. *Bayesian Analysis* 6(4), 727–754.

Liu, Z. and Adams, C. S. (2019). Experimental tests of Bertrand's question and the Duhem–Quine problem. *European
Journal of Physics* 40(6), 065801.

Longuet-Higgins, H. C. (1981). A computer algorithm for reconstructing a scene from two projections. *Nature* 293,
133–135.

Lupton, R. H., Gunn, J. E. and Szalay, A. S. (1999). A modified magnitude system that produces well-behaved
magnitudes, colors, and errors even for low signal-to-noise ratio measurements. *The Astronomical Journal* 118(3),
1406–1410.

Lévy, P. (1925). *Calcul des probabilités*. Gauthier-Villars, Paris.

Mardia, K. V. and Jupp, P. E. (2000). *Directional Statistics*. Wiley, Chichester.

Marinoff, L. (1994). A resolution of Bertrand's paradox. *Philosophy of Science* 61, 1–24.

McCullagh, P. (1996). Möbius transformation and Cauchy parameter estimation. *The Annals of Statistics* 24, 787–808.

Mikkelson, J. M. (2004). Dissolving the wine/water paradox. *British Journal for the Philosophy of Science* 55(1),
137–145.

Secrest, N. J. et al. (2021). A test of the cosmological principle with quasars. *Astrophysical Journal Letters* 908,
L51.

von Mises, R. (1928). *Wahrscheinlichkeit, Statistik und Wahrheit*. Springer, Vienna.

Norton, J. D. (2008). Ignorance and indifference. *Philosophy of Science* 75(1), 45–68.

Roy, W. (1785). An account of the measurement of a base on Hounslow-Heath. *Philosophical Transactions of the Royal
Society of London* 75.

Schwartz, E. L. (1977). Spatial mapping in the primate sensory projection: analytic structure and relevance to
perception. *Biological Cybernetics* 25, 181–194.

Seidenfeld, T. (1979). Why I am not an objective Bayesian; some reflections prompted by Rosenkrantz. *Theory and
Decision* 11, 413–440.

Shackel, N. (2007). Bertrand's paradox and the principle of indifference. *Philosophy of Science* 74, 150–175.

Sivia, D. S. and Skilling, J. (2006). *Data Analysis: A Bayesian Tutorial*, 2nd ed. Oxford University Press.

Snellius, W. (1617). *Eratosthenes Batavus, de terrae ambitus vera quantitate*. Leiden.

Stigler, S. M. (1974). Cauchy and the witch of Agnesi: an historical note on the Cauchy distribution. *Biometrika*
61(2), 375–380.

Stone, M. and Dawid, A. P. (1972). Un-Bayesian implications of improper Bayes inference in routine statistical
problems. *Biometrika* 59(2), 369–375.

Talacko, J. (1956). Perks' distributions and their role in the theory of Wiener's stochastic variables.
*Trabajos de Estadística* 7, 159–174.

Weisskopf, V. and Wigner, E. (1930). Berechnung der natürlichen Linienbreite auf Grund der Diracschen Lichttheorie.
*Zeitschrift für Physik* 63, 54–73.
