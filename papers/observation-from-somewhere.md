# Observation from Somewhere

**Addresses given, payloads met: the geometry of a situated reader**

*Tom Brinkman, with Claude. Draft for external review, 27 October 2026.*

## Abstract

What geometry does a reader need when it does not know the complete object? A writer, who states a thing in amounts,
needs its true breadth, and gets it by walking the whole object or by carrying in an amount measured beforehand. A
reader that stands somewhere needs neither: it has its own breadth, a value it chooses to start from, H, but not the
breadth of what it reads. This paper works out the geometry that this one restriction leaves, building on Jaynes's
principle of transformation groups: what a reader cannot tell apart, it addresses alike. Any relation between two
parties is a pair of unit relations, h and v, each between 0 and 1, and since neither can pass 1 every relation turns
over at one point, v = h, the *corner*. The reader holds one length, H, and nothing else to measure with. Turned
uniformly, that one length traces a circle, since its length is fixed, with the corner at distance 1; no second breadth
is needed, and the reader has none. The readings of that turn follow the Cauchy distribution: on the quarter turn the
half-Cauchy, its median at the corner and its quartiles a reciprocal pair (signed over two quadrants, the standard
Cauchy), so the Cauchy is not a law laid on a circle but the measure of the addresses
the one-length turn makes. The other party's breadth, V, is held only by a writer, who holds both hemispheres; looking at
the reader's circle the writer can draw a second axis and find V = H, and in a drawing that does have two axes (a page, a
shore, a chart, an instrument) V = cH with c ≠ 1 is no turn, and a uniform turn of direction there gives a Cauchy of scale 1/c, which is why a lighthouse's
flashes on a shore and Mercator's map need c = 1. None of this is a claim about the mountain, whose true size is a
separate number that no reading carries. The geometry has two sweeps, and neither is something the reader does: the *inscribed sweep* lays the addresses, the
directions from the standpoint each read as a ratio v/h; the *central sweep* is the same quarter seen from the centre
of the circle they land on, where the light arriving along each direction paints its address. The two meet at one
point for every direction (Euclid III.20); reading that point as where the payload lands is our interpretation.

A reader that stands somewhere holds two different things: where a reading can be put, its *address*, and what is met
there, its *payload*. The paper is about keeping them apart. The addresses are given by the geometry of the standpoint
alone, complete before anything arrives: the uniform turn is a measure on directions, given whole, and the reader
computes, sends and turns through nothing to have it. The measure is standard mathematics; reading it as the reader's
addresses is this paper's interpretation, and the results are stated so that each can be checked apart from it. The
main result is the separation in its sharpest form. Given uniformly by turn from where the reader stands, the readings
follow the Cauchy distribution, and that law is the turn's own, whatever is painted on it: whatever arrives along a
direction cancels from its reading. Three results are kept apart: any sweep that treats the two parties alike puts its
median at the corner, since a median depends only on order, which belongs to the addresses; if its weight also stays
above zero near the horizon it has no mean, which is no loss, since a mean is a sum of sizes, a question about the
payload; and the uniform turn gives the Cauchy's exact shape.

What one standpoint cannot give is the size. A writer holds a line of true breadth 1 as 1; the central sweep measures
it as π/2, the inscribed as 2/π, and their product gives the 1 back, but that 1 is the line drawn at the reader's own
breadth, H measured in H, not the true breadth of anything read. Every reading is a ratio, unmoved when the world is
scaled; an amount needs one amount carried in, and more standpoints bring back the figure but not its size. Inside the
corner the reader's addresses are proportional; past it, if no scale is preferred (a premise we assume, not derive:
every doubling given the same room, the layout increasing), the only consistent layout is logarithmic. H is not a
measurement but the value the reader starts from: every value gives the same geometry, its size sets only the zoom, and
a fixed count of addresses holds any number of things, though things sharing an address arrive there as one. The geometry needs that value and a shape, set by how
many unit relations the system includes: two give the circle, three the sphere. In one
sentence: the address scheme and the magnitude met at an address are distinct mathematical roles, and a geometry can
specify the former without determining the latter. So ratios suffice for everything a reader does from where it stands;
a blueprint, the writer's statement in amounts, adds capabilities the ratios cannot give (the size, parts that meet out
of view, sums, the whole joined and stated before it exists, a far field in proportion common to every reader), which an intricate system may need and a reader does not.

## 1. Introduction

A writer states a thing in amounts. A blueprint shows every line at its true length, to one scale, turned neither toward
nor away from anyone, and the equation h² + v² = 1 holds all its points at once. To make either, the writer needs the
true breadths, and gets them by walking the complete object, or by carrying in an amount someone measured beforehand. A
reader needs neither. It stands somewhere. It has its own scale, its own breadth, a value it chooses to start from
rather than a size it has measured, and it does not know the breadth of what it reads.

This paper asks what geometry such a reader needs when it does not know the complete object. Our thesis is this:

> A situated observer does not possess a coordinate system for the world; it constructs an addressing scheme from
> relations available at its standpoint, and uses those addresses to encounter the world's magnitudes.

Put another way, the geometry built here is not shapes. It is the addresses, given whole, that point to a magnitude, and it says
nothing about what the magnitudes are. The magnitudes are not irrelevant: they make the back sides and everything hidden. But
they are met at the addresses, not built into them. The geometry that follows is therefore not a new geometry of the
world. It is a geometry of the reader's own *addresses*: the places where readings can be put, which exist before
anything is read and do not depend on what is found there.

The paper's argument runs on one line. Ratios suffice: a reader that builds, places, compares, orders and checks from
where it stands does all of it in ratios to its own breadth, and no amount is needed. A blueprint adds: the writer's
statement in amounts gives the size, lets parts made apart meet, lets amounts be added, keeps the far field in proportion
for readers whose near fields differ, and states the whole before it exists, which intricate systems of many parts may need. It is a capability added to the ratios, not a condition of them.
Section 9 sets the two side by side.

**What is new, and what is not.** That coordinates depend on the observer is old: a coordinate system is a choice, and a
change of coordinates changes every coordinate. What is new here is where this reader's scheme comes from: it is built
from the relations available at its standpoint, its own breadth and what it can relate to it, before any payload
arrives. Three things then have to be kept apart:
- the *object*, whatever exists independently of any reading of it;
- the *address*, the place in the reader's scheme at which something can be met;
- the *payload*, the magnitude met there.

A change of coordinates moves addresses and payloads together. The separation here lets either change without the other.
Changing what arrives leaves every address in place (Theorem 6), and changing the standpoint changes the addresses
without touching the object. That separation is the subject of this paper; the rest is what it takes to state it
exactly.

**The addresses are given, not performed.** Nothing the reader does produces them. Classical results describe them
as a sweep: a ray turned uniformly through a quadrant, a lamp turning on a shore, a needle dropped at random angles, and
the pictures are processes. The mathematics under the pictures is not. The uniform turn is a measure on directions, the
one every turn leaves unchanged, and a measure is given whole, all of its directions at once: the share of the quarter
turn below a direction is a fact about that direction, not the count of a procedure that has reached it. So, once the one
length and the uniform measure on directions are granted, the sweep is given to every standpoint for free (§12.4 says
what each part of that rests on), complete before anything arrives, and the reader runs no algorithm to have it.
The measure is standard and needs no reader; that it is a reader's own addresses is the reading this paper proposes. A
real reader may count against something else, a clock, a flat screen or what arrives (§2), and
each such count is another weight, with the consequences set out in §12.2.
What arrives then paints the addresses that are already there.

**The separation, in brief.** An address is a point, a direction from the standpoint; a payload is what is found at that
point, an amount. The law of the addresses, the Cauchy, is fixed by the standpoint and the turn alone, and any payload
can be swapped for any other at any address without moving one address (Theorem 6(a)). The two have no connection;
they share only a place, and the distinction has to be stated, since a number that does not mark it holds them as one
(§7.2). The separation itself is familiar:
coordinates, sampling grids and a function's domain already keep a location apart from the value found there. What is
proposed here is a construction of it for a reader at a standpoint, and what follows from that construction. That is
more than a domain and its values: the addresses are built from bounded relations available at the standpoint (unit
relations in [0, 1]), which fix a corner and a horizon with no amount; a measure on them, the turn's, gives their law;
and the construction says which magnitude it loses in the building, the one size no reading carries, and what restores
it, one amount carried in (Proposition 8). Its rule,
this paper's and offered as a reading, is that a Cauchy variable is a direction, read by its order, and never an amount; where one appears beside an amount, as a spectral line's profile
beside its strength, the two are separate factors, and the test is to find the turn and find the amount. Every operation
on directions (a new zero, the reciprocal, a zoom, a relay through a standpoint between) keeps the law a Cauchy, moving
only where the standpoint is; only an amount entering breaks it, and then from its centre outward, the tails last
(§7.2). The contribution is a construction of a bounded observer's representation that does not
presuppose the whole, together with an exact account of what that construction can recover and what it cannot. The
writer's geometry, with the whole already in hand, is not in question here; this paper concerns what a reader needs
without it.

**What we build on.** The method is not new either. Jaynes (1968, 1973) showed how to choose a measure from what an
observer does not know: state its ignorance as a group of transformations, and take the measure the group leaves
unchanged. His cases give the classical priors, uniform in a location and uniform in the logarithm of a scale, and one
answer to Bertrand's chord drawn at random in a circle, posed so that turning, resizing or moving the circle changes
nothing. We apply the method to a reader that stands somewhere, with a group we choose as its ignorance: turns of its
bar, rescalings of the other party's size, and the exchange of the two unit relations. Given that the sweep is the
turning of a rigid bar, the measures these leave unchanged give much of this paper's geometry: the uniform turn and its
Cauchy, and the corner; carried to amounts, the same indifference to scale
motivates the logarithm past the corner (§2). What is ours is the choice of group, the near field, and the reading of
the measure as the reader's addresses rather than its belief.

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
chart that sends the horizon to infinity, not to anything measured (§4, §7.2). What arrives at the addresses is a
separate thing, with a law of its own. The earlier readings stay correct; the reading here says which of their facts
belong to the addresses and which to what is met at them (§7.2, "The rule, and a test").

**What the paper is for.** Practice already reads Cauchy-type quantities correctly. No one reports the mean of a Cauchy
sample: the median and the quartiles, or the centre and half-width of a line, are what statisticians, spectroscopists
and astronomers report, and robust methods were built to do the same where the tails are heavy. This paper does not
correct that practice. It gives a reason for it. The usual reasons, that the mean does not exist and that the median is
robust, say that the median works. The reading says what makes it the right summary: the quantity is a direction read
from a standpoint, its law has a median and no mean on the chart in which it is reported, and the median is the corner,
where the two parties' readings meet. It also says when the median stops being the right summary: when what arrives
weighs the two sides of the corner unequally the median moves off the corner by that weighting, and when an amount
enters, the law stops being a Cauchy from its centre outward (§7.2).

**A picture.** Hold your hand up to a stained-glass window, with the fingers spread between flat and upright. Each
finger is a direction in which you can look, an address, and each is lit by the pane it lines up with, in that pane's
colour. The fingers are there before any light reaches them, and they are the same wherever you hold the hand: nothing
has to move to lay them, and nothing has to be worked out. The coloured light is what arrives along each direction, the
*payload*. Put another window in its place and the fingers stay as they were; only the colours change. Hold the hand
somewhere else and the same is true. The colour says nothing about how far off its pane is, or how big: two panes on
one line show only the nearer. To learn that, you have to walk, so that the panes slide across one another. Much of
what follows is the mathematics of the fingers alone, and the main result is that one well-known distribution, the
Cauchy, is entirely fingers.

Your thumb is your own breadth, H: the one measure you hold up, chosen because it is to hand, not because it measures
anything, and the only length you have. The mountain you look at has a breadth of its own, V*, which you may not know.
If you know the mountain's size, you hold the writer's vantage, and the corner is where your thumb equals the mountain,
a point you can compute. If you do not know it, you set nothing, since you have no second length to set: the mountain
arrives as directions on the circle your thumb traces as you turn it. A writer looking at your drawing would say you had
drawn the mountain at the breadth of your thumb, V = H, mountain equals thumb, because the drawing holds no other length.
You read the mountain in thumbs.

**Two vantages, and two sweeps.** There are writers and readers, told apart by their vantage. The writer's vantage holds
both hemispheres, every breadth at once. The writer needs the true breadth, and to have it must walk the complete
object, or carry in an amount measured beforehand. Because it writes, its ruler is the number line: what it writes are
amounts, counted out and added, laid alike on both sides of 1, in proportion and with no corner (§9). Between two points
it holds the straight chord, which needs no turn. The reader's vantage is hemispherical: it stands at one point, faces
one way, and holds the directions from there. The corner, where a lay turns from proportion to levels, is the reader's:
it sits where the reader's own unit falls.

The reader's geometry has two sweeps, and neither is something the reader does or a kind of reader it could be. Both are
what the geometry gives a standpoint for free, given the one length and the uniform measure on directions. The *inscribed sweep* is the addresses: the directions from the
standpoint, a quarter turn from all of h to all of v, each a ratio, uniform by turn. The *central sweep* is
where those addresses land: on the circle drawn on the chord between the two parties, each direction from the
standpoint meets one point, which the circle's centre sees at twice the angle (Euclid III.20). There what arrives along
the direction, the payload, paints the address. A direction and its paint are one read, broken down two ways.

The two sweeps measure a line of true breadth 1 differently: the central sweep, a half turn about the circle's centre,
as π/2; the inscribed sweep, a quarter turn from the standpoint, as 2/π; the writer, with no turn at all, as 1. Their
product, π/2 · 2/π = 1, not their difference, gives the line back, and what it gives back is the reader's own H measured
in H (§10, step 3), not the other party's true breadth. From one standpoint the reader has the frame, every direction at
no particular size. Its true size needs a second standpoint, the walk between the two a baseline in the reader's own H,
which places at V*/H what both standpoints can match while its parallax stays above the reader's resolution
(Proposition 11; §10, step 6). One amount carried in writes it in a shared unit. Each step adds what the one before
could not: the frame from one standpoint, the size in H from two, the unit from one amount more.

The sum of the unit relations is where the truth would lie: a system's true breadths, as shares of their whole, would be
one point of it, found only with the breadths themselves. The reader's drawing, which holds only H and so puts every party at it,
is the sum's centre, where every pair is at its corner; the geometry follows from there, and the truth lies off the centre by the
ratios a blueprint would add. Many apparent paradoxes come from reading one vantage's geometry as if it were another's, most
often from treating the writer's vantage as if a single observation held it. Section 3 sets out the reader in full.

**Results.**
- **Main result: the separation.** The addresses are given by the geometry before anything arrives, and no payload moves them. Given uniformly from home, the addresses are the Cauchy distribution. The Cauchy is the law of the
  uniform turn itself, whatever turns and whether it receives or sends: the addresses, not the payload. Whatever is
  met in each direction cancels from the reading. Order survives every change of payload and sums do not, which is why
  the Cauchy has a median, at the corner, and no mean (§7). The median at the corner needs only that the sweep treat the
  two parties alike, and the missing mean only that, besides, its density of h stay above zero near the horizon; the
  circle and the uniform turn give the Cauchy's exact shape (§7.2). As this paper's rule, offered as a reading: a Cauchy variable is a direction, read by
  its order, never an amount, and where one appears beside an amount, as a spectral line's profile beside its strength,
  the two are separate factors (§7.2).
- A situated reader's ignorance, as we choose it, is a group: turns of its bar, rescalings of the other party's size,
  and the exchange of the two unit relations. The measure the first two leave unchanged, uniform in attitude and uniform
  in levels of size, is analogous to Jaynes's location and scale with the location on a circle. Given that the sweep is
  the turning of a rigid bar, it selects the uniform turn for that stated ignorance (§12.1); the exchange gives the
  corner; through amounts, the rescalings motivate the logarithm past the
  corner. Standing at home removes the translations: from home the uniform measure is uniform in direction and in
  levels of distance, not in area, and Bertrand's chord has an answer that depends on where the circle lies, ⅓ from on
  it, rising to Jaynes's ½ from far off (§2).
- What is known of the breadths sets the situation, one of five: nothing related, the circle or another shape held
  whole by a writer, or a reading from somewhere, which has its two sweeps, the addresses and their paint. A situated
  reader can divide only by its own breadth, and what a blueprint would add is a single number (§3).
- Every relation between two parties turns over at one point, the corner v = h, the only point left fixed when the two
  parties are exchanged. Near and far are one geometry, read from either side of it (§4).
- A reader holds one length, H, and no other. Turned uniformly, it traces a circle, because the length is fixed, with
  the corner at distance 1 whatever H is, and the readings of that turn are the half-Cauchy on one quadrant, its median
  at the corner, and the standard Cauchy signed over two (§5, §7.1). No breadth is given to the other party: its breadth, V, is held only by a writer, who holds both
  hemispheres, and V = H is the writer's name for the circle the reader makes. Where a drawing does have two axes (a
  page, a shore, a chart, an instrument), V = cH with c ≠ 1 is not a turn and moves the median log₂ c levels off the
  corner (Proposition 5(d)); the lighthouse's flashes on a shore and Mercator's chart, which draws every compass course
  true only because it stretches north–south as much as east–west, need c = 1. Sweeps that are not turns keep the
  corner and the missing mean but not the Cauchy's shape (Theorem 6(e), §12.2). Whether a reader's sweep is a turn, and
  whether its instrument imposes a c, are empirical questions the paper leaves open (§12.2). The other party's true size
  is a separate estimate (§9). H itself is not a measured size but the value the reader starts from;
  any value gives the same geometry, and its size sets only the zoom (§8).
- How many unit relations the system includes sets its shape: two the circle, three the sphere, n + 1 the sphere in
  n + 1 dimensions (§5). With three, the one length H turned in two angles traces one sphere, and the addresses fill
  one octant of it, a wedge. Laid uniformly, they are the two-dimensional Cauchy: every pair keeps its corner, and the near field in both
  readings is a third, not a half (§7.1). With n other parties it is 1/(n + 1). The turn of H is the geometry's whole
  work; no party's true size enters it.
- Inside the corner the addresses are proportional; past it, if no scale is preferred (every doubling the same room,
  the layout increasing), only a logarithmic layout is consistent (Cauchy's functional equation, Proposition 4). The reader has two address spaces joined at one corner (§6).
- How finely a reader reads is a count the geometry leaves open, and the choice of unit is a zoom, not an escape (§8).
  A larger H gives the near less detail and reaches the far; the best H is the corner of what is read. The fraction an
  array's floor discards is the address's second coordinate, its depth: the dyadic cells tile the hyperbolic plane, the
  space of the Cauchy's own parameters, every level alike and every cell of one room (§8). An H of 0 or
  of ∞ leaves one of the rulers that favour no amount, and no corner (§9).
- The geometry does not supply amounts. A common rescaling leaves every reading unchanged, one amount supplied from
  outside fixes the scale, and a fact shared between two readers supplies exactly one ratio. The best estimate of the
  other party's true size is the median of what the reader knows of it (§9).
- A unit is a relation measured beforehand, such as one foot, or five ounces to a foot, and it brings in the one ratio
  no reading supplies. Within one reader its value is a zoom, needed because addresses are finitely many; agreed
  between readers, it lets amounts pass between them. The number line is such a unit: a ruler that favours no reader's
  unit must be a power or a logarithm, with no corner, and the number line is the power that keeps proportion on both
  sides of 1 (§9).
- What one standpoint's readings fix, and what more standpoints add (§9): one stream fixes the course of a relation, not
  its parties; readings against one denominator give payloads relative to each other; further standpoints bring back a
  figure up to its scale; payloads closer than the resolution arrive as their centroid.
- Ratios suffice, and a blueprint adds (§9): everything a reader builds, places, compares, orders and checks from where it
  stands is done in ratios to its own H; a blueprint, the writer's statement in amounts, adds seven things no reading
  supplies (the size, meeting out of view, sums of amounts, the join, a statement before the thing, completeness stated,
  and a far field kept in proportion, common to readers whose corners differ), which intricate systems of many parts may need and a reader does not.
- A worked example, a mountain range written by the writer and read from where the reader stands, puts the pieces
  together (§10); applications follow (§11).

Section 2 states the principle these rest on, Jaynes's, and Section 12 returns to it. The geometry is claimed as
necessary relative to a stated ignorance, not absolutely, and each relaxation of that ignorance gives a named
alternative; Section 12 also lists the assumptions and related work. Section 11 applies the propositions to familiar
cases (a survey, one's own height, towers of units, a room, parallax far off, the outline from one place, special
relativity's sky), and two appendices gather the classical results that confirm steps of the main line and the
engineered systems read against it. The paper's results are geometry: what the geometry gives a reader, not how
readers or instruments make use of it. It draws on physics and perception to show what the reading does, restating
special relativity's sky (§11) in its terms and sorting three cases in data, LIGO's noise, the quasar dipole and single photons (§7.2), and it claims no new
physics, perception or structure of spacetime.

## 2. Setting

**Unit relations.** Everything here is built from the *unit relation*: a number from 0 to 1 relating a part to its
whole, none of it, all of it, or anything in between, such as the fraction of a day gone or the part of a road
behind. A relation requires two unit relations, one for each party. Draw one horizontally and one vertically and call
them h and v. They have no units, and neither knows the other's whole. Breadths are written in uppercase with the
amounts. The reader holds one, H, and no other: the one value it chooses to start the system, its thumb in the picture
of §1, not a measured size. Any value will do, and which one it chooses sets only the zoom (§8). For the reader, h and v
are both shares of that one length: its bar, of length H, turned from all of h to all of v (§5). A writer, who holds
both hemispheres, also holds a breadth for the other party, V, and writes v against it; the reader has no V. The other
party's true size, an amount the reader does not have, is written V*. h is the reader's side of a relation. A circle has two unit relations, h and v; a sphere has three, h, v and v₂. How many a system includes sets its
shape (§5).

**Unit relations are not amounts.** The amounts are h·H and v·V*, so their ratio is (v·V*)/(h·H) = (v/h)·(V*/H). The
ratio of the unit relations, v/h, is not the ratio of amounts, V*/H. The only way from one to the other is to multiply
by a breadth, which must be known. We keep lowercase letters for unit relations and uppercase for breadths and amounts
throughout, with V* for a party's true breadth.

**The sweep.** Within one observation neither breadth changes. The *sweep* is every way h and v can relate, from all of
h (v = 0) to all of v (h = 0). Leaving *zero* (v = 0), v rises against h held at 1. It can rise only until it too
reaches 1, at v = h. After that the relation can continue only by h falling against v held at 1. The reading is v/h on
the first half and h/v on the second, each in [0, 1]. Exchanging the two parties, the *reciprocal*, sends v/h to h/v.
The limit v/h → ∞, where h empties, is the *horizon*; it is never reached.

**Given, not performed.** The sweep is a name for what the geometry gives, not for anything done. Every relation from
all of h to all of v is there at once, from the standpoint alone, before anything arrives; nothing moves to lay them,
no beam goes out and no head need turn. "Uniform" names the measure on these directions that every turn leaves
unchanged, and a measure is given whole. The share of the quarter turn below a direction, (2/π)·arctan(v/h), is a fact
about that direction, not the count of a process that has reached it. The classical results used here are of the same
kind: ∫₀^{π/2} dθ = π/2 and ∫₀^{π/2} cos θ dθ = 1 are sums over a set of directions taken together, Buffon's 2/π is a
measure on a needle's angles, and the invariant measure on turns is fixed before any turn is made. Their pictures are
processes (a lamp turning, a needle dropped again and again, a ray stepped across a quadrant), and the word "sweep"
carries the picture with it; the mathematics does not need it. So throughout, "in equal steps of turn", "swept
uniformly", "counted" and "from zero to the horizon" are said of the measure and of the order it puts on the
directions, never of an act, and nothing in this paper is an algorithm a reader runs. A lamp does turn, and its flashes
are made in time; the law they leave on a shore is the same measure, which the lamp's turning realizes and does not
create.

**The wedge, and its drawings.** Every pair of unit relations is a ray from the origin into the quarter-plane between
the two axes; with a third unit relation v₂, read against the same h, it is a ray into the solid wedge between three
axes. The ray is the relation. Position along the ray is the pair's size, and that is what dividing one unit relation by
another removes. The wedge itself favours neither unit relation: reading it chooses a denominator, the one unit relation
it divides by, and v/h is the wedge read against h. The wedge is the primitive. It is given afresh at each standpoint,
from the relations there, and the sphere is not assembled from wedges: it is the writer's picture of all the wedges that
could be given.

The usual drawings are cuts of the wedge, each a different normalization:

| cut the wedge where | two unit relations | three unit relations | normalized by |
|---|---|---|---|
| length = 1 | the quarter circle h² + v² = 1, length π/2 | the sphere's octant, area π/2 | the whole length (ℓ₂) |
| largest = 1 | the unit square's two arms, length 2 | the unit cube's three faces, area 3 | the largest unit relation (ℓ∞) |
| sum = 1 | the line h + v = 1, length √2 | a flat triangle, area √3/2 | the sum (ℓ₁) |
| one unit relation = 1 | the reading v/h on [0, ∞) | the plane of v/h and v₂/h | one unit relation: a denominator |

Every cut passes once through every ratio and meets the corner at v/h = 1. The numbers belong to the cut, not to the
relations: the quarter arc and the octant both measure π/2 because they are cut by length. Statements about ratios hold
in every drawing; statements about lengths, angles or areas belong to one, and we say which. These are the ℓ₂, ℓ∞ and ℓ₁
normalizations; for short we call the first three cuts the *arc*, the *square* and the *line*, and the third is the
standard simplex.

**The sum, and the drawings built from a standpoint.** One cut needs no standpoint. The sum h + v + v₂ + … = 1 treats
every unit relation alike and needs nothing but addition: each is a share of a whole, and only a view that holds the
whole has shares. It is the writer's own drawing, the line (the chord) for two unit relations and the flat triangle for
three. Every other drawing is built from a standpoint. Dividing by one unit relation chooses a denominator; dividing by
the largest chooses a register, reading v/h up to the corner and h/v past it; dividing by length needs a turn.

The sum also shows where a reader stands. The triangle holds every way the breadths can share a whole. A system's true
breadths, taken as shares of their whole, would be one point of it, and no common unit moves that point; but finding it
needs the true breadths, which are amounts, and normalizing the unit relations by their sum does not supply them. A
situated reader does not have that point. It has H, which sets only its zoom (§8), and no other length, so its drawing
gives every party that one length; a writer would write it V = V₂ = H. That is equal shares, the triangle's centre
(⅓, ⅓, ⅓), which is the triple corner, where every pair is at its corner. The rest of the geometry follows from it. The true point lies off the centre by two ratios no
reading carries, V*/H and V₂*/H (§3.8); amounts brought from outside move the reader's amounts toward it and redraw nothing
(§9).

**Altitude and azimuth.** With three unit relations the wedge's directions are given by two angles, the coordinates an
observer uses for its own sky (Smart 1977). Take v as the vertical and h and v₂ as the horizontal plane, h the forward
direction, toward the first other party. The *altitude* a runs from the horizontal up to the vertical: the sweep from
all of h to all of v. The *azimuth* ψ runs round the horizontal plane, from h to v₂ square to it: the sweep that brings in V₂. The
direction is (h, v, v₂) = (cos a cos ψ, sin a, cos a sin ψ). Each angle reads its own pair and has its own corner at 45°:
the azimuth reads v₂/h = tan ψ, whatever the altitude, and the altitude reads v against the horizontal reach,
v/√(h² + v₂²) = tan a, whatever the azimuth. These are horizon coordinates: the horizon and the vertical are set by where
the reader stands, as an observer's are, unlike coordinates fixed to the sky. They choose an order, a forward direction
and a vertical; the wedge itself does not. With n + 1 unit relations there are n such angles. What a uniform wedge means
is taken up in §7.1.

**Addresses and payload.** An *address* is a place in the reader's layout where a reading can be put. The range of
addresses is fixed by the geometry before anything arrives, and an address is taken from it when something does. The
*payload* is what arrives: a wave of some kind, sent out or shaped by the things read, not the things themselves; it
paints the address it arrives along. A reader reads what arrives and reaches the things only through it. In the picture
of §1 the fingers are addresses and the coloured light on them is payload. The addresses do not depend on what arrives at them; every
"if" belongs to the payload, including which side of the corner a given reading falls on. Nothing in the paint is a
distance: of two things on one line the nearer paints the address, and how far it lies does not arrive with it. A *lay*
is a rule that places each reading at a position in a drawing; the *room* a stretch of readings receives is measured
either by length or by number of addresses. A *quadrant* is one way of facing the wedge: a sign for each freedom of a
drawing, and since no unit relation is negative the other three are the wedge faced another way (Proposition 3(d)); the
directions from all h to all v fill one (an *orthant* for more unit relations, an *octant* for three). A *facing* is the
direction faced along the way from h to v, which turns as the direction does (§3.4, §4). A *level* is a stretch of the
reading: the first runs from zero to the corner, and past the corner each level is one doubling of v/h.

**The two sweeps.** The geometry gives two sweeps over the same quadrant, and they are two ways of counting one set of
directions, not two motions and not two readers. The *inscribed sweep* is the directions from the standpoint, home, a
point of the circle drawn on the chord between the two parties (the Thales circle, §4): each is a ray from home, a
quarter turn takes them from all of h to all of v, and each is read as a ratio, v/h. These are the addresses. The
*central sweep* is the same directions counted from that circle's centre: the ray from home at θ meets the circle at the
point the centre sees at 2θ (Euclid III.20), so the quarter turn from home is a half turn about the centre. That point
is where what arrives along the direction is met: the paint on the address. One direction, read two ways: its address
by the inscribed sweep, the point its paint lands on by the central one (§4, "The address points at the payload").
These are the only two standpoints on a circle from which equal turns cut equal arcs (§4).

**Our words and the standard ones.** A few short words here are ours, and each names something standard. *Home* is where
the reader stands, the point its rays leave from: the apex of the wedge, the centre of its unit circle (§5), a point of
the Thales circle (§4). *Zero*, v/h = 0, is a reading, not a place: the direction of all h, pointing at the other party.
The lays of §6 put it at home, which is why the two are easily run together; on the Thales circle they are the two ends
of the chord. The *wedge* is the closed positive orthant, the cone of directions with no unit relation below 0. A
direction in it is a point of the projective line or plane, [h : v] or [h : v : v₂] (§9); the *triple corner* is the
direction [1 : 1 : 1], the centre (⅓, ⅓, ⅓) of the simplex. The *bar* is the reader's one length H, turned, its
length taken as 1: the unit vector (h, v) = (cos θ, sin θ); its *attitude* θ is its polar angle. The *corner* is the fixed point of the reciprocal x ↦ 1/x,
x = 1. A *level* past the corner is a dyadic interval of the reading, from 2^(j−1) to 2^j, an octave in the sense of
music and of signal processing. A *lay* is a scale in the sense of measurement theory (Stevens 1946), a monotone map L
from readings to positions, as Luce's ruler is (Luce 1959). The sweep's progress g is the share of the quarter turn from
zero to a direction; written as a formula, g = (2/π)·arctan(v/h), the distribution function of the uniform turn's
readings (§7.1). The formula is the writer's account of it; the reader evaluates nothing. The *capped reading*, v/h up to
the corner and h/v past it, is the reading normalized by the larger unit relation, the ℓ∞ cut.

**An address, its reading and its law.** Three objects share the word *address* in what follows, and they are kept
apart. The *address* is a direction, [h : v], a point of the closed half-arc of the projective line (§4): a geometric
object. Its *reading* is a coordinate on that object, the chart s = v/h (or h/v past the corner); the same direction has
other coordinates, its angle θ or its share g, and none of them is the direction itself. The *law* of the addresses, the
Cauchy, is a measure on the readings, the image of the uniform turn under the chart. When we say the Cauchy is the
addresses, we mean that it is the law of these readings, set by the standpoint and the turn, and not a law of anything
that arrives.

**What we build on: the reader's ignorance as a group.** The method is Jaynes's (1968, 1973). An observer that cannot
tell two problems apart must treat them alike, and when the problems it cannot tell apart are related by a group of
transformations, the measure it should use is the one the group leaves unchanged: indifference between problems, not
between events. His cases are these (Jaynes 1968, §VII). Ignorance of a location and a scale gives a measure uniform in
the location and uniform in the logarithm of the scale, dμ·dσ/σ, Jeffreys's rule for a scale (Jeffreys 1939); ignorance
of a rate's time scale gives dλ/λ. Ignorance of a share t, read as a population of opinions that learns nothing from a
new piece of evidence, which multiplies every opinion's odds by one factor, gives 1/(t(1 − t)), uniform in the logarithm
of the odds, the prior Haldane (1932) had proposed. When the group has as many parameters as the problem, the measure is
fixed up to a constant (Jaynes 1968). And Bertrand's "chord drawn at random" in a circle (Bertrand 1889) has one answer
once it is posed so that the answer must not change when the circle is turned, resized or moved: ½, the chord's distance
from the centre uniform, the answer Crofton's measure on lines gives (Crofton 1868; Jaynes 1973). Resizing alone already
rules out Bertrand's chord between two random ends, which can hold "for, at most, only one size of circle", and moving
the circle alone already fixes the answer.

We apply the method to a situated reader. It does not know two quantities, its *attitude* θ, which way its bar points,
and the other party's true size relative to its own, κ = V*/H; nor, from a reading alone, which of the two unit
relations the reading was divided by. We take its ignorance of these to be this group:
1. a *turn* of the bar, θ ↦ θ + α: nothing the reader holds prefers one attitude to another;
2. a *rescaling* of the other party's size, κ ↦ λκ: the other party's amounts all change by one factor, and no unit
   relation and no reading changes;
3. the *exchange* of the two unit relations, v ↔ h, which sends a reading to its reciprocal and θ to 90° − θ
   (Proposition 1): nothing in a reading says which of the two it was divided by. It acts on readings and on drawings,
   not on κ: the reader holds H and not V*, and the two breadths cannot be swapped without changing what it knows. That
   the other is as likely to be larger as smaller, κ and 1/κ alike, is a separate premise, used only for the estimate of
   the size (Proposition 13(c)).

The turns and the rescalings act on separate unknowns and commute. This is analogous to Jaynes's problem of a location
and a scale, with the location on a circle, though here the scale acts on no reading: two problems side by side rather
than one. The measure they leave unchanged is dθ·dκ/κ, their Haar measure (Haar 1933), unique up to a constant factor,
since f(θ + α, λκ)·λ = f(θ, κ) for all α and λ leaves only a constant multiple of 1/κ. Jaynes's own group, μ′ = μ + b
with σ′ = aσ (1968, eq. 49), also commutes. The location-and-scale family's group, x ↦ b + ax, does not, and has two
invariant measures: dμ·dσ/σ, the right-invariant one, which coincides with Jaynes's, and dμ·dσ/σ², the left-invariant
one, Jeffreys's general rule. Later work has favoured the right-invariant one where the location or the scale is of
interest and the other a nuisance: it is then Bernardo's reference prior (Bernardo 1979) and gives frequentist coverage
exactly (as reviewed by Ghosh 2011); with other quantities of interest the left one can be the better (§12.2, question
7). The reader's group has one: its turns and exchange form the compact group O(2) and its rescalings an abelian group, so the
group is unimodular and the measures unchanged by composing on the left and on the right coincide. The turns act on the whole
circle of directions; the reader's quarter is that measure restricted, which the exchange carries onto itself. What the
measure gives:
- *Uniform in θ*: once the sweep is taken to be the turning of the bar, a uniform turn (§7.1). That is not a rate
  anyone keeps. Measured by itself a turn is uniform: with no clock, no flat ruler and no count of arrivals there is no
  measure on the directions but the amount of turning, and the measure every turn leaves unchanged is unique up to a
  factor. A sweep is uneven only against something carried in: a clock (the time spent at each direction), a flat
  screen or wall (equal steps along it are equal in tan θ, not in θ, as a camera's pixels are) or what arrives (a
  density over directions, the payload). Which of these the readings are counted against is the choice Drory presses
  (§12.2, question 2). Read as v/h on one quadrant, all of h and all of v being the one length of the bar, the uniform
  turn is the half-Cauchy with its median at the corner (Proposition 5); signed over both quadrants, the standard Cauchy. Write a
  Cauchy law with median m and scale γ as the point m + iγ of the upper half-plane. A turn acts on the signed reading as
  a Möbius map and carries each Cauchy law to the one at the image point (McCullagh 1996); the standard Cauchy, at i, is
  the only one every turn leaves where it is. The reader's bar has one length, so nothing here is chosen. A drawing that
  has two axes, a writer's page or an instrument, can give all of v c times the length of all of h, V = cH; there the
  uniform turn's readings are the Cauchy law at i/c (Proposition 5(d)), turns in that drawing's plane act on its
  readings by conjugate maps, which fix i/c and do not carry all of h into all of v, and the exchange carries i/c to ic.
  So in a drawing with two axes c = 1 is selected twice: by the rigid turn, which with c ≠ 1 has no turn from all of h
  to all of v (Proposition 3(e)), and by the exchange acting on the law of the readings, c = 1 being the only drawing
  whose readings favour neither unit relation (Proposition 5(d)). It is the drawing that has the reader's circle.
- *Uniform in log κ*: every level of the other's size alike. As an estimate of the size, with nothing to make the other
  larger rather than smaller (the separate premise above), it gives the median of what is known: the corner √(V₋·V₊) of
  any bounds, and H itself when what is known is symmetric in levels about H (Proposition 13). It does not lay the
  readings, which κ never touches. Carried to amounts, a far reading taken as an amount in H, the same indifference
  to scale motivates premise (S) of §6, which gives the logarithmic lay past the corner (Proposition 4): the bridge is
  the amount, and (S) stays a premise (§12.2, question 1). The lay and the uniform turn are different measures on the
  same reading: the uniform turn is the measure on attitudes, the lay how far readings are placed, taken as amounts in
  H, past the reader's own breadth.
- *The exchange's fixed point*: v = h, θ = 45°, the corner (Proposition 1).

**What kind of measure this is.** The address law is neither a belief about what arrives nor a frequency of
arrivals. It is what Jaynes (1968) calls the invariant measure m(x): the measure fixed by the transformation group
alone, which enters his continuous entropy −∫ p·ln(p/m) dx as the reference against which any distribution is
measured, before any data. The Cauchy here is that m for the reader's group, the invariant measure of its directions.
What a reader observes, the readings of whatever arrives, has a law of its own, which depends on what arrives; the
invariant measure does not. Medians, means and samples are applied to it as to any measure, and what they say is said
of the reference, not of the world.

**Zero, and a new zero.** Zero is the direction the reader faces, the start of the quarter turn; every direction is
counted from it. Facing another way gives a new zero and changes nothing in the law: every turn leaves the standard
Cauchy where it is, so the readings from the new zero have the same law, and no zero is preferred. The old zero
survives only as one reading from the new one. Readings from two zeros compose as turns compose, by tangent addition,
s ⊕ t = (s + t)/(1 − st); a full round composes to no turn, a check like the closed loop of §9. Tangent addition counts
turns only modulo a half turn, so readings composed round a loop close in the same way after one round as after two:
the count of rounds, the loop's winding number, is in no reading, and only a count of passes through the horizon keeps
it. Which repeated steps ever close, and how a new zero composes with two other parties, are classical (Appendix A). A frame that seems fixed,
a wall or a far point, is one that keeps its reading from each new zero. The corner is not computed: it is the
direction at which the two unit relations read alike, and that it halves the quarter turn is the geometry's. It is a
crossing, not a turning point: v − h = √2·sin(θ − 45°) changes sign there at its steepest, while the arc's height off
the chord, sin 2θ, is flat there at its greatest. A small error ε in what is read moves a crossing by about ε, and a
peak by about √ε, so the corner is held at first order (at ε = 10⁻³, a fifteenth of the peak's error).

The method is not ours. Three things in its use here are. The first is the group. Which transformations a situated
reader cannot detect is a statement about its situation, and we choose it as a statement of ignorance rather than derive
it from anything prior (§12.1). Jaynes phrases his rotation as the observer's: his problem "does not specify whether the
observer is facing north or east" (1973, §2); here the turn is the bar's attitude. The reader's group differs from his
in one respect: this reader stands somewhere. His straws are thrown at a circle that may lie anywhere, so his group
includes the translations, and the measure it gives on lines is Crofton's; on points of the plane, the measure that
translations and turns keep is area. A situated reader's lines all pass through home, and the transformations that keep
home where it is are the turns and dilations about it, multiplication of the plane's points by a complex number. The
measure they leave unchanged on the plane is dx·dy/(x² + y²) = dθ·dr/r: uniform in direction and uniform in levels of
distance, not uniform in area. Read from home, Bertrand's question has no single answer. For a circle of radius R whose
centre is at distance D ≥ R, the share of the chords cut by uniformly turned rays that are longer than the side of the
inscribed equilateral triangle is arcsin(R/2D)/arcsin(R/D). From a home on the circle it is ⅓: the rays from a point of
the circle are the chords from one end, and this is Bertrand's chord between two random ends, holding, as Jaynes found,
for one size of circle only: here for one ratio of R to D. As the circle recedes, the rays turn parallel and the share
rises toward Jaynes's ½, which, he argued, is what a tosser whose "region of uncertainty" is large compared with the
circle will see. Straws tossed since show a similar dependence on a ratio of two lengths: the answer turns on the
circle's diameter against the straw's length, and reaches ½ only for straws much longer than the circle (Liu and Adams
2019). The second is what the measure is taken to be. For Jaynes the group's measure is a "pre-prior": not itself a
realistic state of knowledge, but the invariant measure of the parameter space, on which a prior is then built from what
is known (1968). Norton (2008) goes further: complete ignorance is not a probability distribution at all, and
indifference and the invariance of ignorance look paradoxical only when it is taken to be one. Here the measure is not
built on: it is the reader's addresses, laid before anything arrives, and its main consequence is that the Cauchy
belongs to the addresses and not to the payload (§7). The third is the near field: within its own breadth the reader
holds a length, and no position within it is preferred, so equal differences within H get equal room, which is
proportion (an indifference within the near field, not a translation of home, which stays where it is); the proportional
and logarithmic lays meet at the exchange's fixed point, where their spacings agree once the logarithm's constant is
chosen to make the join smooth (§6). A prior for a scale alone has no such corner.

## 3. The reader

Everything in this paper is read from somewhere, and what is known of the breadths decides what can be read. That is
set by what is known of the two breadths: not by where the reader is in the world, not by how many things there are,
and not by what arrives.

### 3.1 The situations

**The relations first.** A system is a set of unit relations, h, v, v₂ and so on, each between 0 and 1. Each other
party has a breadth, V, V₂, which a writer may hold; that is the writer's view. A situated reader holds only H. It
starts the geometry with that one length, turned (§5), which a writer would write V = V₂ = H. That gives the set of every
[h, v, v₂]: every way the relations can stand to one another, the unit cube of relations, whose directions are the wedge
and whose sum h + v + v₂ = 1 holds every point the truth could be (§2). The reader stands where the parties' rays meet
square: with the parties at the triangle's corners, (1, 0, 0), (0, 1, 0) and (0, 0, 1), the only points from which every
pair is seen at a right angle are the cube's corner, the reader's home, and its mirror across the triangle, (⅔, ⅔, ⅔).
With two parties those points make a whole circle through home, the Thales circle of §4; with three they pin the
reader down. A situation is what is known, given party by party: first for one other party, the five below, then for
two.

| situation | H | V | standpoint | what is had | example |
|---|---|---|---|---|---|
| 0 | known | not known | none | nothing: H but no h, so no relation | — |
| 1 | known | known, equal to H | none | the whole at once | an equation: the circle h² + v² = 1 |
| 2 | known | known, unequal or varying with direction | none | the whole at once | an array: a shape's breadth in every direction |
| 3 | known | not known | home, seen from the Thales circle's centre: a central angle | the paint: what arrives along each direction | the central sweep |
| 4 | known | not known | home, a point of that circle: an inscribed angle | the addresses: directions, ratios, no amount | the inscribed sweep |

**One read, two results.** Situations 3 and 4 are the two sweeps of one situated reading: one standpoint, one quadrant
of directions, each direction read two ways. The inscribed sweep gives the addresses: the places a reading can be put,
laid before anything arrives, whose law is the Cauchy, with its median at the corner and no mean (Theorem 6). The central
sweep gives where each address's paint lands, the point of the Thales circle the direction meets (§4, "The address
points at the payload"). Neither is a reader standing outside or inside a thing, and neither is something a reader does
or could choose to be; both are the geometry of one standpoint. The addresses can be had without the paint: a count of
directions alone, whatever painted them, is situation 4 by itself. The paint is never had without its address, so 3
always comes with 4. What the paint is, its colour, its strength, its departure from a uniform sky, is the payload's
and the world's; if the strengths are taken to vary independently and to be unchanged by turns, they are normal (§7.1,
"Why the payload is Gaussian"), a model under two premises, not a consequence of the sweep.

**The rule.** Three questions place any reading in exactly one situation.
1. Is anything related to the reader, so that it has an h? If not, it is in situation 0.
2. Is V known? If it is, the whole is held: situation 1 if V equals H in every direction, situation 2 otherwise.
3. If it is not, the reading is from somewhere, and has the addresses (4) and, where something arrives, their paint
   (3).

Each question has two answers, and each answer either ends the questioning or leads to the next question, so every
reading lands in one situation and none in two: the five are exhaustive and do not overlap. Cases that look like a
sixth reduce to these.
- *V known only within bounds, or as a distribution,* is a situated reading with its one missing number known that way
  (§3.8). Its best estimate is then the corner of the bounds, or the median (Proposition 13).
- *H unknown* leaves no reading at all: H is the reader's own breadth and is always held. Situation 0 is H with no h.
- *A system that changes kind* moves from one situation to another over time; at any one reading it is in one.
- *Several readers* each have a situation of their own; what passes between them is the subject of §9.
- *More than two breadths* put the questions to each further breadth in turn: "Two other parties", below.
- *Directions along which nothing arrives* are addresses still laid, with nothing painted on them. That is a matter of
  payload, not of situation (Theorem 6(a)).
- *A thumb that changes between readings* changes no reading, since every reading is a ratio of amounts in one unit and
  the unit cancels (Proposition 8). Each reading is then a reader of its own, joined to the others as several readers
  are (§9).
- *A reading of an area, or of any other power of the relation,* (v/h)^p with p > 0, keeps the order, the corner, the
  reciprocal and the median, and only rescales the levels by p.

**Thumb and mountain.** Call the reader's breadth H its thumb and the other party the mountain, whose breadth a writer
would call V. If the mountain's size is known, the view is the writer's: thumb and mountain are both in hand, and the
corner, where the thumb equals the mountain (v·V = h·H), is computed. If it is not known, the reading is situated, and
the reader has no second length at all: it turns its thumb, and the mountain arrives as directions on the thumb's circle,
read in thumbs. A writer looking at that drawing finds the mountain drawn at one thumb, V = H, mountain equals thumb
(§5); the reader set nothing, having no V to set. That one length is what makes the sweep a turn and its readings the
Cauchy (§5, §7.1); a page or an instrument that drew the mountain at another length would have neither. How many thumbs
the mountain really is,
is a separate estimate. It changes no reading, only the amounts, and one thumb is the best estimate when nothing says
bigger or smaller (Proposition 13, §9). The corner v = h is still found exactly, but the amounts there are the
estimate's. The mountain's true size, V*/H thumbs, is the one number a blueprint adds to the situated reading (§3.8).

- **0, nothing.** The reader has its breadth H, as it always does, but no h: nothing is related to it, so there is
  nothing to read and no home to lay from.
- **1, the circle.** Both breadths known and equal, held whole as an equation, h² + v² = 1, by the writer. The corner is
  computed, at 45°, and there is no horizon.
- **2, every other shape.** Both breadths known but unequal, or varying with direction, held whole as an array: the
  breadth in every direction, known together. The corner is computed in each direction, and there is no horizon.
- **3, the central sweep.** Each direction from home meets the Thales circle at the point its centre sees at twice the
  direction's angle; over the quarter turn those points run a half turn about the centre, from one end of the chord to
  the other. There the paint lands: what arrives along each direction.
- **4, the inscribed sweep.** The rays from home, a quarter turn from along the chord to square to it: the addresses,
  the Cauchy laid by direction, with their median at the corner. Their shares make the hyperbolic secant density, and
  their running total is the fisheye (§7.1).

Situations 1 and 2 are the writer's. They are written views, an equation or an array, and they name a state of
knowledge, the whole walked or carried in, not a place anyone stands. Situations 3 and 4 are from somewhere. Both find
the corner exactly, since v = h needs neither breadth (§4); what is missing is the amounts there. Both meet a horizon
that 1 and 2 do not have, and neither knows how many things there are.

| situation | the corner | horizon | its geometry | measures a line of true breadth 1 as |
|---|---|---|---|---|
| 1 | computed, at 45° | none | the circle | 1 |
| 2 | computed in each direction | none | the shape | 1 |
| 3 | found: v = h | the horizon | the Thales circle, a half turn about its centre | π/2 |
| 4 | found: v = h | the horizon | the fisheye and the hyperbolic secant density; counted, the Cauchy | 2/π |

**Two other parties.** With V₂ the rule is put to each party in turn, and a situation is one entry per party: 1 or 2 if
that party's breadth is known, a situated reading if it is not. Situation 0 stays a single case, nothing related and no
h, and the five above are the one-party case. The two angles are the altitude, from all of h to all of v, and the azimuth, which
brings in V₂ (§2).
- **Both known.** The writer's view in three dimensions: the solid held whole, its corners computed, no horizon. The
  truth is one point of the triangle h + v + v₂ = 1.
- **One known.** One pair held as a writer holds it, the other read from somewhere. With V known the corner of h and v
  is computed and V's amounts are exact; V₂ is read on the reader's own length, H, the corner of h and v₂ found, and V₂'s amounts are had up to
  the one ratio missing, V₂*/H. Written in one freedom and situated in the other.
- **Both read.** Every direction of the octant an address [h : v : v₂], two numbers, laid uniformly by area (§7.1), each
  painted by what arrives along it. Over a whole hemisphere the central measure is its area over its projection on the
  base, 2, its surface being twice its base; the inscribed measure is its mean height over the hemisphere, ½; and
  2 · ½ = 1, as π/2 · 2/π = 1 for two (§3.4). These are not the two-party measures squared, (π/2)² and (2/π)², but those
  times 8/π² and π²/8.

With n other parties a situation is n entries, one per party, and the rule is the same.

### 3.2 Which division a reader can make

A breadth pair becomes a reading by dividing, and there are two ways to divide: by the reader's own breadth, or by the
whole, taken as a sum or as a length. Which one can be made is the situation.

| divide both by | (H, V*) lands at | which lies on | needs |
|---|---|---|---|
| H | (1, V*/H) | the number line held upright at 1: unbounded | H only |
| the sum, H + V* | (H, V*)/(H + V*) | the chord h + v = 1: bounded | H and V* |
| the whole, √(H² + V*²) | (cos θ, sin θ) | the quarter circle: bounded | H and V*, and Euclidean length |

A situated reader has H, which it chose, and not V*, so it cannot form the whole; it can only divide by H, measuring
everything in thumbs. Every system it reads lands on one unbounded line, at its ratio, with the scale gone and a horizon
at the far end. A writer holds both breadths and can divide by the whole. Divided by their sum, every system lands on the
chord h + v = 1, which needs nothing beyond the two breadths and their addition; divided by their length, it lands on
the bounded quarter circle, which needs the Euclidean length as well (§5, "The Euclidean choice"). Either way the corner
is computed, at the chord's middle or at 45°, and there is no horizon. The chord comes first: the arc is the chord with a
facing turned through (§4), and the circle is that arc over every quadrant. The number line and the quarter circle are
one projection apart: projecting (1, x) toward the centre gives the circle's point.

### 3.3 The number line laid twice

The clearest single picture of the situations is the number line itself. Hold the number line upright at h = 1, so that
the number x is the point (1, x), and lay it down in two ways. Projected toward the centre onto the quarter circle of
radius 1, x lands at (1, x)/√(1 + x²), at height sin θ with θ = arctan x: the whole unbounded line fits on a quarter of
the circle. Laid on the same quarter arc unrolled straight, the *unit line* of length π/2, x lands at θ itself, with
nothing curved.

| number x | on the unit line, θ | on the circle, sin θ | unit line ÷ circle | circle ÷ unit line |
|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 |
| ½ | 0.464 | 0.447 | 1.037 | 0.965 |
| 1 | 0.785, the middle | 0.707, at 45° | 1.111 | 0.900 |
| 2 | 1.107 | 0.894 | 1.238 | 0.808 |
| 4 | 1.326 | 0.970 | 1.367 | 0.732 |
| 10 | 1.471 | 0.995 | 1.478 | 0.676 |
| → ∞ | → π/2 | → 1 | → π/2 | → 2/π |

- **1** is the quarter circle itself: a closed, known curve, both breadths held, the corner computed at 45°, no
  horizon.
- **2** puts a shape in place of the circle: each number lands at the shape's radius in its direction.
- **3**, the central sweep, sets the unit line against the circle, θ/sin θ: rising from 1 toward π/2, approaching the
  line from above.
- **4**, the inscribed sweep, sets the circle against the unit line, sin θ/θ: falling from 1 toward 2/π, approaching
  from below. Its view is the unit line laid out as the fisheye.
- **0** has no unit, and nothing to lay.

Past 1, every number lands closer to the circle's top and the line's end, and the numbers out to infinity crowd into the
last stretch of both without arriving: the horizon, the same on both layouts. One construction gives all five. 1 and 2
are the quarter circle, held whole; 3 and 4 live on the unit line, and the two sweeps are the two ways of comparing the
layouts, line over circle and circle over line, with 1 between them. The unit line is the address space, and the number
line is what is addressed. Why the number line itself, unlike any reader's lay, has no corner is taken up in §9; the
line, the turn and the lay are drawn on one figure in §6 ("One figure, three rulers").

### 3.4 Two vantages, and the true breadth

The five situations give two vantages: the writer's, which holds both hemispheres, and the reader's, which holds one,
with its two sweeps. Situation 1, the circle, is the baseline of both: the writer's equation, with V = H, and the
circle the reader's one length traces (§9); the table gives what each adds to it. The writer's own drawing is the sum, h + v + … = 1 (§2).

| | situations | geometry | the turn | measure of a turn θ | measures a line of true breadth 1 as |
|---|---|---|---|---|---|
| the writer: the whole, walked or carried in | 2, on 1 | the chord, and the circle drawn on it; every breadth held; no facing; its ruler the number line, with no corner | none | none | 1 |
| the reader, central sweep: the radius of the Thales circle | 3, on 1 | one quadrant: where each direction's paint lands | a half turn about the centre, from one end of the line to the other | θ/sin θ | π/2 |
| the reader, inscribed sweep: a ray from home | 4, on 1 | one quadrant: directions from home | a quarter turn, from zero to the horizon | sin θ/θ | 2/π |

**Where the numbers come from.** The reader stays where it stands, and nothing it does draws the arc: the arc is the
geometry's, the points the directions from home meet as they run from all of h to all of v. The two sweeps relate those
points by different turns, and the writer by none. The inscribed sweep's directions are a bar of length 1 from home: at
angle θ the bar's end has drawn an arc θ, and the line it covers, its projection, is sin θ. The central sweep's facing
turns twice as far, 2θ (§4, "Why the corner sits at 45°"): it faces the far end of the line at the start, is square to
the line at the corner, and faces the first end at the finish, a half turn in all. Drawn on the line as its diameter, of
radius ½, a turn of 2θ draws an arc of θ over a chord of sin θ. So both draw an arc θ over a line sin θ. The central
sweep measures arc over line, θ/sin θ; the inscribed, line over arc, sin θ/θ. The two are reciprocal at every turn (the
table's θ is the bar's; the central facing has turned 2θ):

| turned through | central, θ/sin θ | inscribed, sin θ/θ | product |
|---|---|---|---|
| almost 0° | 1.0000 | 1.0000 | 1 |
| 15° | 1.0115 | 0.9886 | 1 |
| 45° | 1.1107 | 0.9003 | 1 |
| 75° | 1.3552 | 0.7379 | 1 |
| 90° | π/2 = 1.5708 | 2/π = 0.6366 | 1 |

Both tend to 1 as the turn shrinks, and neither reaches it while there is any turn. At the limb, the central facing has
made its half turn, an arc of π/2 stood on the line of 1 as its chord, and measures π/2; the inscribed bar has made its
quarter turn, and its average projection over the turn is (2/π)∫₀^{π/2} cos θ dθ = 2/π. The central facing turns farther
and the inscribed less, but as ratios the two lie equally far either side of 1, π/2 above it by the factor that 2/π is
below it, and it is their product, not their difference, that returns the line: the arc's excess over the line,
π/2 − 1, and the projection's shortfall, 1 − 2/π, add to 0.934, not to 1.

The 2/π is the uniform turn's, not the circle's. Over a uniform turn of directions, the width of any convex figure,
its projection on the line of sight, averages to its perimeter over π (Cauchy 1841; Barbier 1860 for figures of
constant width): the width is half the outline's length weighed by |cos| of each piece against the direction, and the
turn's mean of |cos| is 2/π, whatever the figure. The circle of diameter 1, perimeter π, gives width 1.

The average projection is Buffon's needle (Buffon 1777): a needle as long as the gap between parallel lines, dropped at
random, crosses one with probability 2/π. Crofton's formula, which measures a curve by the random lines that cross it,
grew from the same problem (Crofton 1868). Buffon's number, like the inscribed measure, holds only when every angle of
the turn is equally likely; weight the turn otherwise and it changes.

Both numbers come from the same two integrals over the quarter turn: the arc the turn draws, ∫₀^{π/2} dθ = π/2 (the
central facing's half turn, on radius ½, draws the same arc), and the projection it casts on the line,
∫₀^{π/2} cos θ dθ = 1. The central measure is the turn over the projection, π/2; the inscribed is the projection over the
turn, 2/π. Each is a ratio of two sums over the turn, so each is taken only by something that adds the projections up,
as the writer does. The reader holds its directions, their shares and their median, the corner at ½, and no mean: 2/π is
the mean projection of its directions under the uniform turn, a mean its directions make possible and it does not
hold. Other weightings of the turn keep the median at the corner (Theorem 6(e)) and in general move this mean, so the
2/π, unlike the corner, is the uniform turn's. Taken to any turn θ, the same two give the table's θ/sin θ and sin θ/θ.
The projection is the line itself: the steps of the turn, each casting cos θ dθ, cover the breadth exactly once. Each
measure sets it against the turn, one way up or the other, so their product is 1. Without angles the turn is
∫₀^∞ ds/(1 + s²) over every relation s = v/h, and the corner halves it, π/4 on each side. The true breadth, 1, is had
only with no turn at all. To the writer, then, a relation is the chord between its ends; from somewhere it is the arc.
The chord comes first: it needs no turn, and the arc is drawn on it by one, where the rays from its two ends cross (§4,
"The arc from the chord").

**With three unit relations.** Taken over a hemisphere instead of a half-turn, the same two measures are its area over
its projection on the base, 2, since a hemisphere's surface is twice its base (Archimedes, *On the Sphere and
Cylinder*), and its projection over its area, ½, the mean height over the hemisphere, since the height is uniform over a
sphere (the hat-box theorem). Their product is again 1. In n dimensions they are √π·Γ((n + 1)/2)/Γ(n/2) and its
reciprocal: π/2 and 2/π for the circle, 2 and ½ for the sphere, 3π/4 and 4/(3π) next.

Archimedes measured the circle from both sides, and the inscribed measure equals his inscribed polygon in number; its
halvings give Viète's product for 2/π (Appendix A).

**From the reader's vantage to the writer's.** The argument runs in seven steps, each resting on the one before.
1. A line has a true breadth, 1. That is what the writer holds.
2. From a standpoint the line is had through a facing: the central sweep measures it as π/2, the inscribed sweep as
   2/π, and π/2 · 2/π = 1.
3. Reading 1 assumes no facing, nothing turned toward or away from the standpoint. Every standpoint has a facing, so no
   situated observation reads 1.
4. Only the writer reads with no facing, so only it holds the true breadth, and it holds it because it has walked the
   complete object or carried in an amount measured beforehand, not because it stands nowhere. A blueprint is the
   example: drawn by a writer who has the whole, every line at its true length to one scale, nothing turned toward or
   away from anyone.
5. To hold 1 is to hold both hemispheres in hand at once, which no single observation can do. That is what the writer's
   vantage is: the true breadth belongs to the whole, walked, not to any one standpoint.
6. So the true breadth can be had from somewhere only by construction from several observations: readings from more
   than one standpoint, joined. The construction represents the true breadth; it does not observe it. A telescope survey
   is the working example. One exposure is one facing from one standpoint, and the survey is the construction. Not every
   combination builds: exposing the same field again lowers the noise and adds nothing; pointings joined at their
   overlaps give the shape up to a scale; only a second standpoint at a known baseline gives a distance (§10 works one
   through).
7. There are therefore two ways to the true breadth, and only two: held, as the writer holds it in a blueprint; or
   constructed, from several situated observations, which is how the writer came to hold it.

The arithmetic of steps 1 and 2 is exact. Steps 3 to 6 are a reading of that arithmetic, not a theorem. The "only two"
of step 7 is exact, as the next paragraph shows.

**Why only two.** The limit in steps 3 to 6 is exact, not an intuition about perspective. Every reading from somewhere
is a ratio of two amounts, so multiplying every amount in the scene by one factor leaves every reading unchanged. No
collection of readings, from however many standpoints, can therefore fix the scale, and one amount supplied from outside
the readings fixes it (Proposition 8, §9). "Only two" means this: the true breadth is either held, or an amount is
brought in from beyond the single reading and the rest is constructed from it. Calibration against a standard, a
baseline of known length and prior knowledge of a size are all ways of bringing that amount in. They belong to the
second route; they are not a third.

Each vantage is right from where it stands. Many apparent paradoxes come from reading one vantage's geometry as if it
were the other's, most often from treating the writer's vantage as if one observation held it.

**What the writer's vantage costs.** In h² + v² = 1, h and v are not compared with each other. Each is compared with the
equation, which supplies the common scale, the constant and the equals sign: the equation is a third party. A written
account holds the whole figure and so cannot state an order of arrival; a situated account states the order of arrival
and cannot hold the whole figure. And the point on which the situated reading turns, the corner, is an unremarkable
point of the writer's drawing.

### 3.5 What the geometry leaves to the reader

This paper is about the geometry, not about how readers or instruments use it. The geometry gives a standpoint its
addresses, laid uniformly by turn, and the paint arrives along them; how a particular reader takes them in, all at once
or a direction at a time, through receptors at equal angles or the equal pixels of a flat screen, and whether it moves,
are its own and are not taken up here. Where a result does depend on such a thing, it says so. Two do. The median of the
addresses, the corner, is had only where the readings are held together, since a median needs every reading compared
with every other (§7.6). And a count of directions on a flat screen of equal pixels follows the screen, not the turn:
equal steps on the screen are equal in v/h, not in θ, and put the median at half the screen's edge instead of at the
corner. With no motion at all, the addresses are still laid and the paint still arrives, but nothing gives parallax, so
no V*/H (§9), and nothing changes, so a second look tells nothing new.

### 3.6 What a situated reader holds, and where it stands

The writer has coordinates x, y and z, any of which a rotation turns into another. Situated observation is not built
that way, and it is not a number of dimensions. It consists of five things, each reached through the one before:
- *relations*: v over h, from horizontal to vertical;
- *addresses*: a relation laid from home, in a quadrant;
- *the sweep's progress*, g = (2/π)·arctan(v/h): 0 at pure horizontal, where nothing of v is expressed, and 1 at pure
  vertical, where all of v is, with the corner at ½ and g(h/v) = 1 − g(v/h);
- *the capped reading*: v/h before the corner, h/v past it, so never more than 1;
- *magnitudes*: the world's, one value at each address, met, not laid.

A reading *divides* (v by h, leaving a relation with no scale; the division is made by the projection through the
standpoint, not by the reader, §9), the geometry *lays* the relation from home, and each address *points* (it reaches a
magnitude, an amount v·V*, which needs V*). Dividing and laying are addressing, there before anything arrives; the
magnitude is the world.

**The reader is the pivot.** Draw the relation as a bar about one fixed end, from pure horizontal to pure vertical. The
free end traces the sweep, and the reader is the fixed end. It sits off the sweep and points along the bar to it.

| on the sweep | the bar | v/h | the capped reading |
|---|---|---|---|
| zero, the start of the sweep | pure horizontal: all h, no v | 0 | 0 |
| the corner | at 45°: v = h | 1 | 1, on both sides |
| the horizon, the end of the sweep | pure vertical: all v, no h | → ∞ | 0 |

Facing the corner, the reader has the near side's [0, 1] before it and the far side's [0, 1] behind it. At the pivot v
and h are both 0, and v/h is 0/0: the reader is the one point with no reading and no address of its own. It lives in
the circle its own H creates (§5), at the centre, and is not the circle. It points and is not pointed to, except as the
payload of another standpoint's address (§7.7).

**h as the focus.** An intuition, not a result: h is not one of the things a reading sweeps but what the sweep is
relative to, the reader's focus. The reading v/h asks where v lies against the focus, which is why scale drops out. The
corner is the thing read sitting at the focus, and the reciprocal is the thing read crossing the focus while the focus
stays put. Changing the focus rescales every reading, and nothing in the world changes.

### 3.7 The hand

Hold your hand out flat: that is h, zero. Point it straight up: that is v, toward the horizon. Every direction between
is a relation of the two, and the hand treats them alike because they share one denominator, the hand itself: the
hand has one length, its own (§5), and nothing else to measure with. Spread the fingers between flat and upright: each finger is an address, one ray of
the relation. Hold the hand up to a stained-glass window: each finger is lit by the pane it lines up with, and that
coloured light is what the address holds, the payload. Put another window there, and the fingers are the same fingers,
each the same address; only the colours change.
- *The thumb is H.* The hand's own measure is its thumb, the reader's breadth, the value it starts from. The mountain it
  looks at is the other party, whose breadth a writer would call V; the hand has no V. A writer looking at the hand
  would say it had set V = H, mountain equals thumb; the hand only read the mountain in thumbs.
- *The geometry is the hand, not the glass.* Dividing v by h keeps the finger and drops the colour.
- *The fingers are free; the light colours them.* The fingers are the geometry of the uniform turn, the Cauchy, and
  they are there wherever the reader looks: they are given, and the reader computes nothing, sends nothing and turns
  through nothing. The colour on each finger is the light the world sends along it, from the first pane on its line. To
  read the payload is to read the colours on the fingers, from the same standpoint.
- *The colour carries no distance.* A finger lit red does not say whether its pane is near or far, small or large.
  Moving the hand changes the colours, never the fingers: that is reading. Walking to another place makes the panes slide
  across one another, so a pane lit along two fingers from two places can be placed, in steps: that is the way to
  writing (§9).
- *The glass hides; the hand does not.* Two panes on one finger's line show only the nearer: the pane behind is the back
  side. The hand hid nothing; the glass did.
- *The far field's doublings are fingers.* Past the corner the levels are doublings (§6), addresses laid before
  anything arrives; what lands on them is coloured light. The fingers sit side by side on one hand, not one inside another.
- *The situations in the hand.* 0: no hand, nothing to point with and nothing pointed at. 1 and 2: the window held
  whole, every pane at once, as its maker holds its drawing, with no hand needed to reach it; in 1 every pane is alike, in
  2 they differ. 3: the colours, the light on the fingers, the payloads. 4: the inscribed sweep, the fingers themselves,
  the addresses the colours land on.
- *The hand has two angles.* Raised, it runs from flat to upright, from all of h to all of v: the altitude. Turned, it runs round
  from pointing at the other party to pointing square to it, which brings in a second other party, v₂: the azimuth.
  Every way the hand can point, within the positive octant, is one altitude and one azimuth, as every point of an
  observer's sky is (§2).
- *The unit circle is the hand's own arc.* In one quadrant it is a quarter, flat to upright. Upright is the arc's end,
  the horizon [0 : 1], a direction the hand can point; in the chart v/h it is open at the top, since no finite reading
  is the horizon (§4). Facing the four quadrants, the hand has four arcs alike, since no reading carries a sign. Joining
  them into the closed circle is the writer's work: it knows each one's size, so their ends can be made to meet. The
  sphere is every way a hand could face, its eight octants joined by the writer; no hand holds it.

The same picture without the hand. Every direction from the point where the reader stands makes a sphere round that
point: the directions themselves, drawn at H (its radius is H, a value chosen, not an amount), the same in every world.
What arrives along each direction paints that point. The paint is the payload; no distance is on these directions, and
of two things on one line the nearer paints the point. The reader need send nothing. It receives what the world puts
there, and it never holds the sphere whole: joining patches into one painted sphere in a common frame is the writer's
work, as above. A reader that carries in the signal's speed to turn a delay into a distance is no longer only reading:
the speed is an amount, and stating the range in it is writing (§9). The picture is Gibson's ambient optic array, the
light at a point of observation (Gibson 1979, ch. 5). In an earlier essay he sets it apart from "the radiant light,
emitted from a point-source", and describes it as "visual solid angles all having a common apex at the point of
observation", one for each face that is not hidden from it (Gibson 1972). What the geometry adds is a measure on these
directions before any paint. Laid uniformly over an octant, they are the two-dimensional Cauchy, with every pair at its
corner and the near field a third, whatever paints them (Proposition 5(e), Theorem 6). The writer's frame is not a
sphere. Holding both hemispheres means holding both signs of every axis, the front and back, left and right, above and
below of everything, and an axis held on both signs is the writer's number line (§9), proportional on both sides of
zero, with no corner and no horizon. Each dimension is one copy of it, independent of the others, so the writer's frame
is their product, a box: Descartes' frame, its extent along each axis an amount, the size of what it holds (§9). Drawn
in unit relations, each axis divided by its own extent, the box is the unit cube. Nothing in it is round, since
roundness is the equal turn from a centre, and the writer has no centre to turn from; drawn, its faces are orthographic
views, parallel rays from no standpoint, the front and the back of everything at once (the glass box of technical
drawing; a blueprint is one face). A point is D amounts to the writer, one on each line, and D − 1 to the reader, a
direction [h : v : v₂] whose parts are ratios of one another; the number between them is the size along the ray, the
one number of §3.8. The two share the axes' squareness, an angle and so a reading; only the amounts along them are the
writer's. The writer joins the reader's eight octants into the box, and every standpoint is a place in it, with its H
given a size there, both writings. From the standpoint the box is never seen, since its extent arrives along no
direction. The reader's wedge opens from its standpoint and reaches the box's faces in the far field: its horizon is the
box seen from within, reached along every direction and never measured, so the box's size, an amount to the writer, is
unknowable to the reader. What reaches it is the wedge's directions; along each, the nearer thing on the line paints the
point first. A second standpoint gives the box's extent in H; an amount carried in gives it in a unit shared with
others.

### 3.8 The one number a blueprint adds

The situations can be written in terms of one another. A situated reading, 3 and 4, is a shape of situation 2, read
through situation 1's drawing, with situation 0's unknown on one side only. The world is a shape like any other, with
some breadth ratio; lacking it, the readings are laid as if the shape were the circle.

Assume a value for V*, and the situated reading becomes situation 2. With directions spread uniformly (§7.1), the
readings in amounts are (v·V*)/(h·H) = κ·(v/h), where κ = V*/H. Counted in doublings of the amount ratio, the readings
for κ = 2 are those for κ = 1 slid up exactly one doubling, every doubling's share unchanged:

| doubling of the amount ratio | ¼ to ½ | ½ to 1 | 1 to 2 | 2 to 4 | 4 to 8 |
|---|---|---|---|---|---|
| κ = 1 | 0.139 | 0.205 | 0.205 | 0.139 | 0.077 |
| κ = 2 | 0.077 | 0.139 | 0.205 | 0.205 | 0.139 |

So what a blueprint adds to a situated reading is one number, how many thumbs the mountain is, V*/H; on the count of
doublings it is an offset, log₂(V*/H), not a change of pattern. The number matters only where the reader must meet an
amount from outside; everything it reads, places and orders from where it stands is done without it (§9). Situation 2 knows the number; a situated reading does not; known within
bounds, it is known within bounds. Assuming it clarifies the reading; it does not simplify it.

The reader does not merely do without V; it never knows V. Every reading is a ratio, and a ratio cancels the amount V
would be, so no reading, however many, carries it (Proposition 8). V is known only by writing: by walking a baseline,
counting a step, ranging with a signal's speed, or being handed an agreed unit, each an amount carried in from outside,
and each moved when the world is scaled (§9). A reader that comes to know V has written; it has not read better but
taken the writer's vantage. And the reader's geometry needs V unknown: the horizon is there because the far end is
never an amount, the corner is the median because nothing sizes either side, and the missing mean is the absent V's
trace (§4, Theorem 6(d)). A writer, knowing V, has a closed circle, its corner only a point, and no horizon.

The same holds for what arrives. The geometry removes the scale before anything is read: the projection divides, not the
reader (§9), so a direction arrives with every amount along it already gone, and the paint on a direction arrives as
paint, never as a number of units (Theorem 6(a)). The reader manages no magnitudes, neither the other party's breadth nor
the size of what arrives. It holds no unit to manage them in: its one length H is its own unit, H in H is 1, and the
value of H in anything else is a writing. So the geometry creates the reader, and the reader has no scale whatsoever.
Every magnitude, with its unit, is a writer's.

## 4. The corner

**Proposition 1.** Let x = v/h ∈ [0, ∞). Then x = 1 is the only point fixed by the reciprocal x ↦ 1/x. The reciprocal
carries (0, 1) onto (1, ∞) point for point, and every sweep from home passes through x = 1. This point depends on
neither H nor V.

*Proof.* The reciprocal is its own inverse and reverses order, so x < 1 exactly when 1/x > 1, and for x > 0, x = 1/x
gives x = 1. A sweep from home grows continuously from 0, so it reaches 1 before it can pass it. Finally, x = 1 means
v = h, a comparison of two unit relations, unchanged when both are scaled together. ∎

We call this point the *corner*. It is ordinary arithmetic, and nothing about it is special beyond what follows from
that. Its importance is that it separates two ways of reading: before it, v is read in terms of h; past it, h in terms
of v. Near and far are one geometry, read from either side.

**Proposition 2.** (a) Let a reader hold x in two registers: x itself where x ≤ a, and 1/x where x > a. Both registers
stay within [0, 1] if and only if a = 1. (b) Let f : (0, ∞) → [0, 1] be strictly increasing and treat the two sides
alike, f(1/x) = 1 − f(x). Then f(1) = ½, and f maps the near side below ½ and the far side above it.

*Proof.* (a) The registers take values in [0, a] and (0, 1/a); both lie in [0, 1] exactly when a ≤ 1 and 1/a ≤ 1.
(b) At x = 1 the condition reads f(1) = 1 − f(1); the rest follows from monotonicity. ∎

Part (b) assumes the reading is *reciprocal-symmetric* (log-symmetric, as Jones 2008b has it): it treats the two sides
alike, although the reader's knowledge does not, since it knows H and not V. Without that symmetry a bounded reading
such as x/(2 + x) has its middle at x = 2. Reciprocal-symmetric readings include the line's share v/(v + h) = x/(1 + x)
and the arc's v²/(h² + v²) = x²/(1 + x²).

**The reader's line, closed.** A reading is a direction [h : v] with h, v ≥ 0, not both zero: a point of the projective
line (§2). These points form the closed arc of that line on which h and v share a sign, half of it. The arc has two
ends, home [1 : 0] and the horizon [0 : 1], and two charts:
- x = v/h, defined everywhere but the horizon;
- y = h/v, defined everywhere but home;
- where both are defined, y = 1/x.

The reciprocal of Proposition 1 is the exchange [h : v] ↦ [v : h]. On the arc it swaps the two ends and the two charts,
and it fixes one point, the corner [1 : 1]. The results so far, and those to come, divide by what they use.
- *The exchange alone, on the open arc between the ends:*
  - the corner and its uniqueness, and the reversed order (Proposition 1);
  - the registers and their cap (Proposition 2(a));
  - the median of any reciprocal-symmetric law (Proposition 2(b); Theorem 6(e)).
- *The closed arc, its ends as points:*
  - a quarter turn from home ends at a point, the horizon, where the chart y is 0 and the chart x has no value;
  - the exchange carries the arc onto itself, ends included.
- *A chart that sends an end to infinity: the missing mean* (Theorem 6(d), (e)). The readings' law has no mean in x,
  which runs to infinity at the horizon, nor in y, which does so at home. On a bounded chart of the same arc, the angle
  θ or the capped share x/(1 + x), the same law has one: π/4 and ½ for the uniform turn. So the missing mean is a fact
  about the chart in which directions are counted as numbers, not about the arc. Being unbounded is not enough to lose
  it: on the level chart ξ = ln(v/h), which runs to infinity at both ends, the same law is (1/π)·sech ξ and has every
  moment, its mean 0 at the corner and its variance π²/4 (Talacko 1956). What loses the mean is how the chart stretches
  the end, the tail falling as 1/x² on x against e^(−|ξ|) on the levels. A mean asks for the readings to be
  amounts on some chart; the arc holds them as directions.

**The corner, fixed by the exchange.** On the whole projective line the exchange has a second fixed point, −1,
off the reader's arc. For every pair it swaps, the cross ratio (1, −1; x, 1/x) is −1: the two fixed points are harmonic
conjugates with respect to every swapped pair, home and the horizon (0, ∞) among them, as the fixed points of any
involution of the line are (Coxeter 1987). So once the exchange is given, the corner is fixed by the line's projective
structure alone, with no measure. Home and the horizon do not fix it by themselves: the maps x ↦ λx keep both and move
1. The exchange does, and swapping h with v asks only that both be shares of one length, the reader's H. The uniform
turn adds only that the corner is the median. Order on the arc is projective too ("Comparing without dividing", below), and so is the levels' distance
(Appendix A).

**Series stop at the corner.** The expansion 1/(1 + x²) = 1 − x² + x⁴ − … converges for x < 1 and diverges for x > 1;
past the corner the expansion in 1/x converges instead. The singularities at x = ±i lie at distance one from zero, so no
expansion about zero reaches past the corner. This is a property of expansions, not a break in the function, but it is
one reason near and far seem to obey different mathematics.

**Comparing without dividing.** For two readings (h₁, v₁) and (h₂, v₂), let D = v₁·h₂ − v₂·h₁. With h₁
and h₂ positive, D = 0 exactly when the two ratios agree, and D > 0 exactly when v₁/h₁ > v₂/h₂. Comparing a reading
with its own reciprocal gives D = v² − h², which is zero exactly at the corner. Sameness, order and the corner need no
division; only the size of D depends on scale.

**Why the corner sits at 45°.** A straight segment from A to B passes once through every ratio of the two, as the
quarter arc does. The arc has a second degree of freedom that the segment lacks: the direction it faces along the way.
The arc is drawn by that turning, not walked: the standpoint stays where it is, and the point read crosses the segment
once while the facing turns (§3.4). If the bar pivots at a point of the circle, as in Thales' configuration, a turn of θ moves its far end through a central
angle of 2θ (the inscribed-angle theorem), so the facing turns twice as fast as the sweep, from facing B at A to facing A
at B. At the corner, θ = 45° and the facing is 90°: square to AB, leaning toward neither party. There the arc stands
farthest from the segment, by 1 − 1/√2. The chord and the arc belong to different vantages. The writer holds the chord
and faces nothing: holding both its directions at once, it holds the chord's length as 1 and no facing. From a
standpoint the chord is had only through the arc. A facing has two senses, toward the half of the circle above the
chord or the half below; each is the other turned through the chord's middle, so the two are always opposite and the
arcs they face are congruent but never the same, meeting at the middle, the corner, square to the chord. Neither sense
is defined except against the other, and both at once, the closed circle, is the writer's join. From an end the ray
turns through a quarter turn, from the middle the radius through a half, both ending at the same point of the arc.
These are the two sweeps of one standpoint, not two readers: the central sweep, the radius about the circle's centre
through a half turn, and the inscribed sweep, the ray from a point of the circle through a quarter, the only two pivots
at which equal turns carve equal arcs (below). The arc faced, not the chord held, is where π/2 and 2/π come from: the
writer's 1 is had through the half turn as the arc, π/2, and through the quarter turn as 2/π, and only their product
gives back the 1.

**The arc from the chord.** The arc can be had from the chord AB without turning a bar. Stand the two parties at its
ends, and from each end sweep a ray: from A a ray reading v/h, from horizontal along AB up to vertical, and from B a ray
reading the reciprocal, h/v, from vertical down to horizontal. Where the two rays cross traces the semicircle on AB.
With A = (0, 0), B = (1, 0) and A's ray of slope s = v/h, the crossing is P = (1, s)/(1 + s²); the rays meet at a right
angle, so P lies on the circle with AB as diameter (Thales' theorem, Euclid's *Elements* III.31, with its converse). Its
distances from A and from B are h and v, the chord is the hypotenuse, and h² + v² = 1 is Pythagoras on it; the foot of P
cuts AB into h² and v², and its height is hv, their mean proportional (*Elements* VI.8). Seen from the middle of AB, P
has turned through 2α when A's ray has turned through α (the inscribed angle theorem, *Elements* III.20): the facing
turning twice as fast as the sweep. The reading is the tangent of half the facing 2α, so cos 2α = (1 − s²)/(1 + s²) and
sin 2α = 2s/(1 + s²), and a rational reading gives a rational point (Euclid's formula for Pythagorean triples). At the
corner, s = 1, both rays stand at 45° and P is over the middle of AB; the reciprocal s ↦ 1/s mirrors P across the
perpendicular bisector. In classical terms this is Steiner's construction of a conic (Steiner 1832): the lines through A
and the lines through B are paired by a projective correspondence, slope s with slope −1/s, that does not pair AB with
itself, so corresponding lines meet along a conic through A and B. It is a circle because the pairing turns each line
through a right angle, and that needs h and v at one length, as they are for the reader, whose one length is H: a page
that draws v at c times h has the same readings cross on
the ellipse x² − x + y²/c² = 0. Paired at equal angles instead of by the reciprocal, the rays meet on the perpendicular
bisector, a line. Equal angles of A's ray give equal arcs of P, so the uniform measure on one ray's directions is the
uniform turn of §7, and its readings are the Cauchy's. Over two amounts x₁ and x₂ laid end to end, the crossing
above the join stands at √(x₁x₂), Euclid's mean proportional (*Elements* VI.13), which is the H that sets the two
furthest apart (§8). The chord comes first; the arc is where the two parties' rays cross. With three parties at the
corners of the triangle h + v + v₂ = 1, rays meeting with every pair square meet only at the cube's corner, the reader's
home, and its mirror across the triangle: the arc of two parties becomes, for three, a single standpoint (§3.1).

**The address points at the payload.** The two sweeps of §3.1 meet on this arc, one point at a time. The inscribed
sweep is A's ray: from home, a point of the Thales circle, it turns through the inscribed angle θ from along the
chord, and at each angle it is an address, the reading s = v/h = tan θ, there before anything arrives. The central sweep
is the circle's radius: it turns about the middle M of the chord through the central angle, from pointing at B. The
payload is what is found where that radius ends. The ray at θ and the radius at 2θ end at the same point P of the arc,
for every θ. That is the inscribed angle theorem (*Elements* III.20): an angle at the circle is half the angle at the
centre on the same arc, and P is its one shared point. Three things are kept apart here: the *address*, the direction
of the ray from home; the *landing point* P, where the radius ends; and the *payload*, what arrives at P. The theorem
gives the shared point; that the payload is met there is our reading of
it, and a physical application must justify that reading on its own. Within it, the address computed by the inscribed
sweep points directly at the payload reached by the central sweep, and it does so in five ways.
- *Exactly, and once.* Each address meets one point of the arc, and each point of the arc has one address. The map
  keeps the order: the address along the chord, θ = 0, points at B itself, the other party, where the radius starts;
  the corner, θ = 45°, points at the top of the arc, where the radius stands square to the chord; the horizon, θ → 90°,
  points at A's own end of the chord, where the radius has made its half turn.
- *At the other party's projection on the address.* The angle APB is right (*Elements* III.31), so P is the foot of the
  perpendicular from B onto the ray: what the address finds is the other party projected onto it. It lies at distance
  h from home and v from B, its foot on the chord at h² and its height hv (*Elements* VI.8).
- *Without the payload in the address.* The address is the ray and its reading; the payload is what is at P. What
  arrives there changes nothing in the address, since the reach of what arrives along a ray cancels from its reading
  (Theorem 6(a)). Every address is laid before anything arrives, and each still points at where its payload will
  land.
- *In the two readings.* Read along the ray, line over arc, the inscribed sweep gives sin θ/θ, 2/π over the whole
  turn; read along the arc, arc over line, the central sweep gives θ/sin θ, π/2 (§3.4). One point, named twice: by its
  direction from home, its address, and by the facing of the radius that reaches it, the landing point.
- *On the circle of one length.* A page that draws v at c times h has the same rays cross on the ellipse
  x² − x + y²/c² = 0 (above). Each address still meets one point, but the radius no longer turns twice the address's
  angle, and the corner no longer points at the top. The direct pointing is a property of the circle, which the
  reader's one length gives and a two-axis drawing has only at c = 1 (Proposition 3(e)).

The inscribed sweep lays the addresses; the central sweep reaches, at each, the payload that address points to. The
reader's addresses and the world's payloads are joined point for point by one classical theorem, and the join needs
nothing the reader lacks: no amount and no second length, only its own H turned.

**Why there are two sweeps, and only two.** The two sweeps are not two motions and not two readers. They are the
directions of one standpoint counted about the two possible pivots, and they meet at one point of the circle (above,
“The address points at the payload”). Structurally the difference is only where the pivot stands. A sweep is a ray
turning about a pivot, counted in steps of turn. For those steps to stand for steps along the arc, equal turns must
reach equal stretches of arc wherever the ray points. Only two kinds of pivot do this.

- *The centre.* A ray from the middle M of the chord is a radius. Each step of turn moves its end by the same step of
  arc, at rate 1.
- *A point of the circle.* From a point A on the circle, a ray turned through θ reaches the point whose central angle
  from B is 2θ, wherever it points (the inscribed angle theorem, *Elements* III.20). Each step of turn moves its end by
  twice that step of arc, at rate 2.
- *Anywhere else.* Take the radius as 1 and a pivot P inside the circle at distance p from the centre. A ray from P
  meets the arc ahead at distance t and behind at distance t′, and a step of turn dθ moves the point ahead by 2t/(t +
  t′)·dθ of arc. That is 1 − p looking straight away from the centre and 1 + p looking straight toward it. Equal turns
  reach unequal arcs, unless p = 0, or unless the point behind is the pivot itself, t′ = 0, which happens just when P
  lies on the circle. From a pivot outside the circle the rate grows without bound toward the two rays that graze it. In
  classical terms, the angle at a point inside a circle is half the sum of the two arcs it cuts off, and at a point
  outside half their difference; only at the centre and on the circle does one arc alone fix it.

So a uniform sweep of a circle has two places to stand, and no third. The points of the circle that matter are the two
parties, home A and the other end B of the chord. The centre is the chord's middle, which belongs to the pair and is
neither party's standpoint. The inscribed sweep is the sweep about a party; the central sweep is the sweep about the
pair's middle. Neither is made by anyone: each is what the geometry of the one standpoint gives.

**What each sweep reads.** The two pivots name the same point of the arc in two ways.

- *From a party.* Read A's ray at θ where it crosses the line touching the circle at B: its height there is s = tan
  θ = v/h. This is projection from a point of the circle onto a line (stereographic projection; in the half-angle form
  s = tan θ, with 2θ the central angle). It carries the whole circle but A itself onto a whole line, so its readings are
  unbounded: as the ray turns toward the tangent at A, square to the chord, s runs to the horizon. A uniform turn laid
  on that line is the Cauchy law (§7.1): its median is at the corner, and it has no mean.
- *From the pair's middle.* The radius at 2θ ends at ½(cos 2θ, sin 2θ) = ½(h² − v², 2hv). With h + iv for A's direction,
  that end is ½(h + iv)²: the central sweep's point is the inscribed sweep's direction squared, ½e^(2iθ) in complex
  form, so the half turn from zero's landing point, B, to the horizon's, which is home, is e^(iπ) = −1. Its coordinates are bounded by
  the radius, so every average over a uniform turn exists: cos 2θ averages 0 and sin 2θ averages 2/π.

The factor of two between the sweeps is that square. It is why the radius turns twice as fast as the ray, why the
address at θ points at the payload at 2θ (above), and why one sweep's readings are ratios and the other's are squares.
Read at one address, the two are easily confused. The inscribed sweep's addresses crowd on the line with density
2/(π(1 + s²)) = (2/π)·h²: at every address, the inscribed reading 2/π times the foot of the point that address points
to. The two have one shape, but they are different things. The density must be summed over a stretch of addresses to
give a share, and summed it is the arctangent, not h². The foot is already a share of the chord. At the corner the
density is 1/π and the foot ½. On the level axis ξ = ln(v/h) the same pairing returns. There the addresses' density is
½·sech ξ = hv, its total π/2 and its running area the fisheye (§7.1), while the landing point ½(h² − v², 2hv) has
height 2hv = sin 2θ = sech ξ and foot h² = ½(1 − tanh ξ). The density is half the height of the point its address points
to: one function, a density of addresses on the one side and a coordinate of the landing point on the other, ½ and 1 at the
corner. The sweep about a party gives ratios, of the first degree, unbounded, held by the median. The sweep about the
pair's middle gives squares, of the second degree, bounded, with means. Both rates are exact only on the circle. Drawn on the
ellipse of a stretched drawing, the inscribed angle theorem fails and neither pivot turns a uniform sweep into a uniform
arc. So the two sweeps, like the pointing, need the circle, which the reader's one length gives (Proposition 3(e)). The two sweeps are also one classical map, the Cayley transform,
under which the Cauchy is the harmonic measure from the standpoint (Appendix A).

**What the reciprocal gives, and what it does not.** The reciprocal proves that the corner is the one point it leaves
fixed, that every sweep passes through it, that a reading kept within [0, 1] on both sides must change register there
(Proposition 2(a)), that a reciprocal-symmetric reading puts it at the middle (Proposition 2(b)), and that expansions
about zero stop there. It does not prove that the drawing is a circle: paired by the reciprocal, the rays from the two
ends cross on a conic, and only Euclidean measure, the right angle with h and v at one length, makes it round (above, and §5);
how readings past the corner are laid out, which needs the premise that no scale is preferred (§6); or the weight with
which the sweep is counted, which needs uniform steps of turn (§7). Each of these rests on its own premise, and we name
it where it enters.

**Every pair has its own corner.** Any two parties have a sweep and a corner, and the corner of one pair is not the
corner of another. A corner means nothing until its pair is named. In the wedge the corner is the central ray. With
three unit relations the three pairwise corners, v = h, h = v₂ and v = v₂, are planes through the central ray v = h = v₂, and
they cut the wedge into six chambers, one for each ordering of the three unit relations.

## 5. The reader's circle

We assume three things.
- **(P0)** A relation requires two unit relations, one for each party, h and v, each in [0, 1]. For a writer, who holds
  both hemispheres, each relates its party to that party's breadth: h to H, v to V. A situated reader has no V: for it
  both are shares of its own one length, the bar of (P1), turned from all of h to all of v.
- **(P1)** A situated reader holds exactly one length, H, the value it starts from, and holds no whole of the system.
  H is not a measured size, and any H will do.
- **(P2)** A level carries no measure: nothing on it but its two ends, their order and the reciprocal between them.

**Proposition 3 (the reader's circle).** Under (P0) and (P1):

(a) the reader holds no breadth for the other party, so there is no second length to give it and no number c relating
one to the other; a writer, holding the other's breadth, can write the reader's drawing on a page with two axes as
V = cH, and no unit relation and no single reading depends on c;

(b) the corner lies at distance 1 from home, measured in H, whatever H was chosen;

(c) if the attitudes of the relation are turns of one rigid bar, of the reader's one length, the relation traces the
unit circle h² + v² = 1;

(d) with m freedoms (unit relations), all shares of the one length H, there are 2^m orthants: 4 quadrants for the
circle, and 8 octants for the sphere h² + v² + v₂² = 1, where v₂ is a second v read against the same h;

(e) on a page with two axes, all of v drawn at c times all of h, V = cH, the attitudes are turns of one rigid bar only
if c = 1: with c ≠ 1 nothing turns all of h into all of v, and there is no circle. So the reader's circle, written by a
writer with two axes, is V = H;

(f) with two other parties, written on three axes V = cH and V₂ = c₂H, the attitudes are the directions of one rigid
bar, the sphere h² + v² + v₂² = 1, only if V = V₂ = H;

(g) the bar can be derived rather than assumed. Take a sweep that is continuous and uniform (every step the same linear map of the
plane of all-h and all-v), that returns to its start after one full turn, and that carries all of h into all of v in a
quarter of it. Such a sweep preserves an inner product, unique up to a positive factor.
- In that inner product, all of h, all of v and every attitude between them have one length, and all of v is square to
  all of h.
- At the sweep's own parameter t, the unit relations are (h, v) = (cos ωt, sin ωt): the unit circle of (c).

So the sweep is the turning of a rigid bar in its own measure, every attitude of one length. The one factor left free is
that length, and it is H. Written on a page with two axes, it is V = H. With more unit relations the same holds on one
condition: the sweeps together must stay bounded (generate a compact group of linear maps). Then an inner product is
preserved, any one averaged over the group's Haar measure (Haar 1933), and it is unique up to a factor when the group
carries every direction to every other, as the turns of the sphere do. Each sweep returning on its own is not enough:
two sweeps that each return, but each in its own inner product, can compose to a map that grows without bound.

*Proof.* (a) By (P1) the reader's only length is H, and by (P0) its v is a share of it, not of any breadth of the other
party's; a reading v/h is a ratio of two shares of one length. A writer who holds the other's breadth V can set it
against H, V = cH, but a unit relation v lies in [0, 1] however large V is, so no reading involves c; c multiplies only
the amounts v·V. (b) The corner is one H from home measured in H: H/H = 1. A reader with unit λH reading a world scaled
by λ receives exactly the same readings, so nothing in the readings fixes H. (c) With one length, the relation is a bar
of length 1 in H whose attitudes are mixes of all-h and all-v, so h² + v² = 1 when length is Euclidean, and the
Euclidean norm is, up to scale, the only norm preserved by every turn. A page with two axes would show the same bar as
an ellipse stretched by V/H. (d) With one length nothing prefers one side of a freedom, so each freedom has two signs. A
closed walk through the orthants must flip each freedom an even number of times, so the orthants are the 2^m vertices
of an m-cube, walked as a Gray code. (e) A turn keeps the bar's length. On the page all of h is the bar at length H and
all of v the bar at length cH, so a turn carries one to the other only if c = 1. With c ≠ 1 the tip must stretch on its
way, along the ellipse of (c) or some other path. (f) By (e) applied to each pair: all of v and all of v₂ must each be
the bar at length H.

(g) Continuous and uniform, the sweep is a continuous one-parameter group of linear maps, so Φ(t) = exp(tA), with A ≠ 0
and T the least time with Φ(T) = I.
1. A real 2 × 2 matrix with exp(TA) = I has eigenvalues ±iω, with ω = 2π/T. A pair of zeros would make A nilpotent,
   and then exp(TA) = I + TA ≠ I.
2. So A = U(ωJ)U⁻¹, with J the generator of turns, and Φ(t) = U·R(ωt)·U⁻¹. This preserves Q(x) = |U⁻¹x|².
3. Suppose a symmetric form G is preserved by every Φ(t). Then UᵀGU is preserved by every turn, so it commutes with J;
   being symmetric, it is a multiple of the identity. So G is a multiple of Q.
4. Let u = U⁻¹(all of h). Since all of v = Φ(T/4)(all of h), U⁻¹(all of v) = R(π/2)u. The two are square to each
   other and of one length in Q.
5. Then Φ(t)(all of h) = cos ωt·(all of h) + sin ωt·(all of v), so (h, v) = (cos ωt, sin ωt), and every point of the
   orbit has the same Q.

A page drawn at V = cH with c ≠ 1 shows the same sweep in coordinates other than its own. Its unit relations at the
sweep's parameter are unchanged; only the page's angles differ, which is the c of Proposition 5(d). ∎

**The order of the chain.** Read in the order the reader has them, the parts run: one length, H (P1); turned uniformly
and returning, it is a rigid bar in its own measure, every attitude of that one length (g); a fixed length turned traces
a circle (c), with the corner at distance 1 (b); and the uniform turn's readings are the Cauchy, the half-Cauchy on one quadrant
with its median at the corner (Proposition 5(a)–(c)). No second length enters anywhere, and none is needed: the orbit is a circle because the length
is fixed. The Cauchy is not a law laid on a circle that already held a V; it is the measure of the addresses the
one-length turn makes. Each ingredient is named: H supplies the one length, the turn supplies the circle, the chart
s = v/h supplies the reading, and the uniform measure on the turn supplies the law. That the reader holds H alone means only
that no second length enters, not that H by itself gives the distribution. Parts (a), (e) and (f), and Proposition 5(d), (f) and (g), belong to drawings with two axes, a
writer's page, a shore, a chart or an instrument: there c is real, and c = 1 is the drawing that has the reader's circle. The family V = cH describes other external
drawings; none of it is a choice the reader makes to set up its own geometry.

**What the geometry needs: a shape and one H.** Neither is a measured size. The shape is set by how many unit
relations the system includes: by (d), m of them give the sphere in m dimensions, with 2^m orthants, so two give the
circle and three the sphere, all of them shares of the one length, and their attitudes turns of one bar, (c). The H
starts it: some H is needed, but by (b) every H gives the same shape and the same corner, and its value sets only the
zoom, which things fall in the near field and are read finely (§8). No party's true size enters the geometry, and no
breadth of the other party's at all.

**What V = H names.** V = H is the writer's name for the reader's circle. A writer, holding both hemispheres, has a
breadth for the other party and can draw it on a second axis; looking at the circle the reader's one length traces, it
finds that axis drawn at H, the mountain at one thumb. The reader did not set this. It has no V to set: its thumb is the
only length it holds, and the mountain arrives as directions on the circle the thumb traces. Nor is it a claim that the
mountain is the size of a thumb. Where it is not, every amount taken from the reader's drawing is off by V*/H, the number
of thumbs the mountain really is (§9). The circle constructs relations in one length and discovers nothing about the
world. Step (a) is close to a definition; we claim only that a situated reader has one length.
- *What c would change, where there is a c.* On a page or an instrument with two axes, no unit relation, no corner
  v = h and no single reading depends on c. But with c ≠ 1 all of h and all of v are drawn at different lengths, so the
  sweep between them is not a turn (part (e)). The tip stretches along an ellipse of axis ratio c, the point of equal
  amounts, v·V = h·H, slides log₂ c levels off the corner, and "sweeping uniformly" no longer names one sweep: uniform
  steps of direction, of the curve and of its parameter give three different laws, and only one of them is the Cauchy
  with its median at the corner (Proposition 5(d)).
- *Why the circle.* With one length the sweep is one rigid bar turning, it traces the unit circle, and the uniform turn
  is unique; its readings are the Cauchy with nothing more chosen. Working back from the Cauchy, which is known, on one
  quadrant the half-Cauchy with its median at the corner, arrives at a turn of one length and, on a page with two axes, at c = 1 and nowhere else
  (Proposition 5(d); V = cH gives the Cauchy of scale 1/c). Both statements are made within the construction (a relation
  as two unit relations, the sweep a rigid bar's linear periodic turn); that every reader must use this construction is
  not claimed (§12.2, "What depends on what"). Unit relations drawn on equal axes, each running from 0 to 1, are this
  circle written with two axes.
- *What the circle does not do.* It does not say how large the mountain is. The mountain's true breadth, V*, is a
  separate number, unknown within one observation. An estimate of it is an amount, the best being the median of what is
  known (Proposition 13, §9); it enters only the amounts, as a shift of every one of them by the same number of levels,
  and never redraws the circle.

**Circular mathematics without V.** The circle's usual equation seems to need V: on a page, (x/H)² + (y/V)² = 1 is a
circle only when V = H. But that is the equation of a drawing with two axes, each with its extent, a writer's. The
classical definition needs one length: everything at the distance H from a centre, |r| = H. The reader's circle is that
length turned (Proposition 3(g) derives it from the turn alone). Its parts h = cos θ and v = sin θ are the across and up
shares of the same H, and h² + v² = 1 is a fact about the shares of one length; the v in it is the turned length's own
up share, not a share of a second party's breadth. Circular mathematics was always ratio mathematics in this sense: sine,
cosine and tangent are sides over the hypotenuse, the radian is arc over radius, π is circumference over diameter,
e^(iθ) is any circle over its own radius, and the corner, π/2 and 2/π and the Cauchy are ratios too; none moves when the
world is scaled (§9), so all of it is reading. What the reader cannot do without an amount carried in is place a point at
(x, y) in a unit, state the circumference or the area as so many units, or set its circle beside another party's: those
are writings. The reader does every part of circular mathematics except the parts that state a size.

**One choice, and two numbers that are not the reader's.**
- *H, the reference.* The reader's one choice, and free. Every H gives the same circle and the same corner (part (b)),
  and its value sets only the zoom (§8).
- *c, a page's or an instrument's, V = cH.* Not the reader's: it holds no V for c to relate to H. It is real wherever
  something written or built has two axes, and there c = 1 is the only value for which:
  - the sweep is one rigid bar turning (part (e));
  - the uniform turn's readings are the Cauchy, with the median at the corner and unchanged by the reciprocal
    (Proposition 5(d));
  - a lighthouse's 45° flash is the corner of its landings (Proposition 5(f));
  - a chart draws every compass bearing true (Proposition 5(g)).

  Any other c is a consistent drawing, but it gives up all four. By part (g), it is the same sweep described in
  coordinates other than its own: a uniform sweep that returns after a full turn has its own measure, unique up to a
  factor, every attitude of one length. The factor is H.
- *V*/H, the true size.* Not a choice. The readings never give it (Proposition 8). An amount, it is the writer's; it
  can be estimated at the median of what is known (Proposition 13), and corrected by a shift in levels when an amount
  arrives.

Changing H rescales the circle in both directions alike, which is a zoom. Changing c, on a page, stretches it in one
direction, which changes its angles and moves its corner off 45°. These are the two effects Proposition 5(f) and (g)
keep apart. With a third party a page has two such numbers, c and c₂ (V = cH, V₂ = c₂H), and the reader's sphere is
c = c₂ = 1 (Proposition 3(f)); H is still the one free choice.

The value of H sets only the zoom, so it may be taken as the circle's own unit: H = 1, the unit circle itself, which a
writer would write V = H = 1. In it the amounts equal the unit relations in number, h·H = h, and the corner v = h is the
point where both are 1 on the square of the capped unit relations. The agreement is in number only: the unit relations
are still ratios and the amounts are still amounts in H, which is why the two are so easily run together. Taking H = 1
does not use up the zoom; it moves it from the circle to the laying: the zoom is which amount in the world is taken as
the 1, and with it the number s = d/H at which each thing lands (§8). With three unit relations it is the unit sphere,
and on the capped cube the triple corner is h = v = v₂ = 1, the point (⅓, ⅓, ⅓) of the simplex written another way.

H cannot be declined. Without a length there is no bar and no relation. An H that favours no value is one taken to its
ends, 0 or ∞. There the reader's lay becomes one of the rulers of Proposition 14 that favour no amount. It has no
corner, and a reader with finitely many addresses loses what it reads: all of it falls into the first address, or past
the levels held (§9). So some H must be chosen; which one sets only the zoom.

**Already drawn, under other names.** The drawing c = 1 is not new. Wherever directions or ratios are read from
something with two axes and the answer must not depend on units, it has been made: statistics standardizes and whitens
its variables, charts keep bearings true, graphs are drawn with equal axes, cameras with square pixels. Each field found
it for its own reason. The geometry gives the common one: it is the only two-axis drawing that has the reader's circle,
so the only one in which the sweep is a turn and the median of every pair's readings sits on the corner. Where it is
skipped on purpose, amounts are being read, not directions. Appendix A lists the cases.

**Where c ≠ 1 comes from.** "V = H is still a choice" is a writer's objection: it supposes someone who holds both axes,
sees c as a free number and decides to set it to 1. A reader whose sweep is a turn never stands there. It holds one
length, and there is no c for it to know, set or decline; a uniform sweep that returns after a full turn has one length
in its own measure (part (g)), and writing it with c ≠ 1 describes the same sweep in coordinates not its own, hiding the
turn's symmetry without removing it. A c ≠ 1 can still appear in what a reader's readings are taken through, imposed
rather than chosen, and then it has a signature. One of four things is the case:
- *It is writing, not reading.* Amounts are wanted in a shared unit, so c is the ratio of real units, measured. An
  equal-area map or a weighting of features keeps amounts on purpose (§9).
- *It is uncalibrated.* Unequal gains, pixels that are not square, variables left in their own units: c is imposed by
  the instrument. The median of its readings sits at c instead of on the corner, and standardizing restores it.
- *An estimate has been taken for the circle.* What is known or guessed of the other's true size, κ = V*/H, belongs to
  the amounts, a shift in levels (Proposition 13); redrawing the circle with it runs κ together with c.
- *It does not turn.* If its measure is not a turn (a boost, or another group), there is no circle to stretch: it has
  another geometry, with no corner at its median and other tails (§7.1, "Why a turn and not a boost").

**The Euclidean choice.** Part (c) is where an assumption enters. One length makes all of h and all of v commensurable, but "a bar
of fixed length" also needs a norm: under the largest-component norm the bar traces the square, under the sum norm the
line. The circle follows if the sweep is the turning of a rigid bar. The facing of §4 motivates that; it does not prove
it. Part (g) narrows the assumption. A sweep that is uniform and returns after a full turn is the turning of a rigid bar
in its own measure, which is Euclidean and unique up to the factor H. What remains assumed is that the sweep acts
linearly on the mixes of all-h and all-v, one motion repeated. That it is uniform is not a further premise: the reader
measures its turn by nothing but that motion (§2, “Uniform in θ”). The same circle comes without a bar, from the chord
and the two parties' rays (§4, "The arc from the chord"); there the Euclidean measure enters as the right angle at which
the reciprocal pairs the rays, drawn with h and v at one length, and without it the crossings are still a conic, an
ellipse. Less rests on the Euclidean choice than it seems. The readings are directions only (Theorem 6(a)), so the norm
reaches them only through the measure on directions that "sweeping uniformly" uses; laid by direction, every path gives
the same readings (§7.4). Swept uniformly along their own paths, the square and the line give other laws, with the same
median at the corner and no mean (Theorem 6(e)). What the circle and the uniform turn add is the Cauchy's exact shape.
Among the p-norms the circle is also the extreme case (Appendix A).

**What the count of orthants borrows.** The count 2^m needs no angle. That the orthants tile the circle or the sphere in
equal shares, a quarter turn each or π/2 of the sphere's area each, is the Euclidean measure of (c), not part of the
count.

**Diameter 2.** The corner has two sides and only two. The reader's own level runs from zero to the corner in every
quadrant: radius 1, diameter 2, the near field. Measured in the reading v/h, the next level runs from 1 to 2, and level
j ends at 2ʲ. We read the 2 across the reader's own level and the 2 between levels as the same 2, the corner's two
sides; this is a reading, not a proof.

**Where the reader lives.** The reader stands at home, the centre of the circle its own choice creates. It is not the
circle. Two circles meet at home and should not be confused: this one, the reader's unit circle, is centred there, the
bar's own; the Thales circle of §4 passes through home. Read from home they give the same directions, and they are the
two circles that read uniformly along their own outline (§7.4). Held whole, as the writer holds it (§3.2), either circle
has no home and no horizon; read from home it is the fisheye of §7.

## 6. Two address spaces

Inside the corner the reader holds its unit and can lay its readings out in proportion: the near field at true scale.
Past the corner the reciprocal makes the reading h/v ∈ [0, 1], but it does not say how far things should be laid out.
Let a lay place a far amount x = d/H ≥ 1 at position L(x), counting addresses from home, with L increasing and
L(1) = 1. Here x is a distance in units of H, which a reader has only from a second standpoint or an amount carried in
(§9); the reading v/h itself does not change with H.

Choosing a different H multiplies every such x by one common factor. A lay whose room depended
on where a reading sits, and not only on ratios, would then depend on the arbitrary choice of H. Premise (P2) points the
same way: no measure is carried past the corner, so nothing supplies a scale for the room to depend on. We therefore
require that no scale be preferred:

> **(S)** L(λx) − L(x) depends on λ alone, for all x, λ ≥ 1.

**Proposition 4.** If L is increasing and satisfies (S), then L(x) = 1 + k·ln x for some k > 0: every doubling receives
the same number of addresses, k·ln 2. If the far lay also joins the near lay L(x) = x without a kink at the corner, then
k = 1.

*Proof.* Let f(λ) = L(λ) − 1. Comparing (S) at x = μ with (S) at x = 1 gives L(λμ) − L(μ) = f(λ), so
f(λμ) = f(λ) + f(μ) for all λ, μ ≥ 1. This is Cauchy's functional equation in multiplicative form (Cauchy 1821),
and its only increasing solutions are f(λ) = k·ln λ. At x = 1 the near lay has slope 1 and the far lay slope k. ∎

Room here is the number of addresses a doubling receives, not its length.

The premise (S) does the work. Monotonicity, a fixed corner and a matched slope are not enough by themselves:
L(x) = 1 + ln x + α(ln x)² with α > 0 satisfies all three and gives successive doublings different room.

**Why (S) is the rule for a reader with no preferred scale.** Suppose a lay breaks (S): for some factor λ, the stretch
from x to λx gets more room than the stretch from y to λy. Choosing the reader's unit differently would turn the
readings x into y, since a change of H multiplies every far reading by one factor. The two stretches therefore differ
only by a choice that, by Proposition 3(b), nothing in the readings can make: a reader with unit λH in a world scaled
by λ receives exactly the same readings. A lay that breaks (S) builds into the addresses a scale the reader cannot
have. Each natural alternative breaks it in just this way:
- *proportion past the corner*, L(x) = x, gives the stretch from x to λx room (λ − 1)·x, which grows with x;
- *a power*, L(x) = x^α, gives it room (λ^α − 1)·x^α, which also depends on x;
- *a logarithm with a correction*, as above, gives room that depends on ln x.

The logarithm alone gives room that depends on λ and not on x, and Proposition 4 shows it is the only increasing lay
that does. (S) does not follow from "any H will do", which only places the corner. It is scale invariance of the lay's
increments, motivated by Proposition 3(b) and assumed, not derived (§12.2, question 1). Note also that the argument for (S) passes
through amounts, far readings taken as amounts in H, and that the smooth join (k = 1) is a further condition rather than a consequence of
the reciprocal.

**A second route, through ratios alone.** Relations chain by multiplying: through any middle unit relation m,
v/h = (v/m)·(m/h). A measure of relations under which chained relations add, f(ab) = f(a) + f(b), and which grows with
the relation, can only be f = k·ln, by the same functional equation. Every doubling then adds the same amount. The turn
is not such a measure, since arctan(ab) is not arctan a + arctan b, and so a bounded sweep gives the levels unequal
shares. This route never leaves the unit relations, so it does not pass through amounts; what it assumes instead is that
the measure of a chain is the sum of its links.

Two ways of holding a relation make the contrast concrete. Measure a relation by twice the area its ray sweeps from the
corner. Hold the whole, h² + v² = 1, and the swept area is the turn: bounded, π/2 in all (Archimedes). Hold only the
corner, on the hyperbola xy = 1 drawn in coordinates that run without bound (with y/x = v/h; unit relations on [0, 1]
meet this hyperbola only at the corner), and the swept area is ln(v/h): unbounded on both sides, every doubling the same
area ln 2 (Saint-Vincent 1647). The rescaling (x, y) ↦ (x/√λ, √λ·y) slides along the hyperbola and keeps areas, so no
scale is preferred. The two are one sweep, squeezed: read against ln(v/h), the turn is
arctan(v/h) = π/4 + ½·gd(ln(v/h)), where gd(x) = arctan(sinh x) is the Gudermannian. It carries the whole unbounded
logarithm into a quarter turn, nearly uniform at the corner and squeezed without end toward the edges, so that the turn
per doubling past the corner falls 18.4°, 12.5°, 6.9°, 3.5°, 1.8°, …, by a ratio tending to 2. The bounded sweep is the
logarithm seen whole from one side.

**Two address spaces.** Inside the corner the addresses are proportional; past it they are logarithmic, each doubling
receiving the same number. The corner is where one gives way to the other, without a kink. There is only one such
corner intrinsic to the relation, the one fixed point of the reciprocal; a particular reader's layout may have other
thresholds of its own. Past it the levels are plain doublings laid side by side, with no corners of their own and nothing nested inside
them. They are doublings of scale, v/h ↦ 2·v/h. (Doubling the angle of the sweep instead sends v/h to
2(v/h)/(1 − (v/h)²); the two agree near zero and part at the corner, which the angle doubling sends to the horizon. Appendix A has what the angle doubling keeps.)

**Reality in 2H.** Measured by length rather than by count, the far field fits in one more H. The *in-place lay* puts a
far reading at length 2 − h/v from home. Level j past the corner, where v/h runs from 2^(j−1) to 2^j, then has length
2^(−j), so the whole far field, out to the horizon, lies between radius 1 and radius 2. The room per unit of v/h is
(h/v)², the Jacobian of the reciprocal. The in-place lay holds the same addresses as the logarithmic lay, the same
number per doubling, crowded toward radius 2; a reader with finitely many addresses runs out of them at the end of its
own range.

| drawing of the same addresses | measured by | bounded | corner at |
|---|---|---|---|
| fisheye (§7) | steps of turn | yes, a quarter turn | half the turn |
| in-place lay | length | yes, radius 2 | radius 1 of 2 |
| logarithmic lay | number of addresses | no | 1, where the equal doublings start |

**Why not proportion all the way out.** A reader that kept v/h itself, in proportion, past the corner would suffer in
five ways. It could not lay its range, since its readings would run to infinity and no range fixed in advance would hold
them. It would divide by the smaller part: past the corner h is the smaller unit relation, and a small wobble in it swings the
reading without bound. Inverting divides by the larger part instead, the rule numerical computing also follows when it
pivots. Its averages would never settle, being dominated by the long tail of its nearest things (§7.6). It would have
to crop: a picture kept in proportion out to the horizon would be infinitely large, and rectilinear cameras, which are
such readers, crop at about the corner, while a fisheye lens holds the whole hemisphere by giving up proportion near
its edge. And its expansions about zero would fail past the corner (§4).

**The corner, the end of the range, and the horizon.** A situated reader meets three boundaries. The corner, v = h,
lies between the two sides of its reading; every reader finds it. The *end of its range* is where the reader's count of
addresses runs out, well short of h = 0; a reader can reach it, as a floating-point
number overflows when its exponent runs out. The *horizon* is the reading's own infinity, h = 0 and v/h
without end, at the reader's sides: the boundary between the side it faces and the side behind it, which no reader
reaches. It is not the vanishing point. A thing infinitely far ahead reads 0, at zero; the reading's infinity lies at
the sides, in what is nearest.

**Why halving.** If a level has nothing but its two ends, their order and the reciprocal (P2), the only subdivision its
symmetries preserve is the cut at the corner into two halves: any other interior point can be moved anywhere within its
half by an order-preserving map that commutes with the reciprocal. Applied again to each half, this gives repeated
halvings. Three parts, or any other number, need an added measure. This is Klein's criterion, that a geometry supplies
what its symmetries keep, applied to the points of a level. Halving is a branching into two; it is not by itself a ratio
of 2 between level edges, since where the edges fall depends on how the readings are laid out. On the lays of this
section they fall at the doublings of v/h. The constructions agree: square roots reach every halving of the turn, and not every other
division (Appendix A). The halvings, factor by factor, are also what give 2/π (Viète's product,
Appendix A).

*What another ratio costs.* A reader whose own resolution multiplies by r from level to level matches levels that are
powers of r exactly, one level per factor: a reader with r = 3 matches levels of three as one with r = 2 matches
doublings. Any ratio can be matched, then, but by the argument above every ratio other than the halving costs a measure
added to the level, carried in the reader's resolution. A layout whose levels are uneven, as a calendar's are (100
years, 12 months, about 30 days, 24 hours, 60 minutes, 60 seconds), matches no single factor and costs a table of its
levels, which a reader given nothing does not have. Uniformity can be free; variation has to be represented somewhere,
in the reader's resolution or in information handed to it. Levels given by a ratio must be one ratio repeated (Appendix A).

**A familiar instance.** Floating-point numbers lay their addresses this way. The exponent counts levels and the
significand is a plain share within the level; below the smallest normal number, the subnormals lay one stretch in
proportion from zero. The count of levels plus the share within the current one is the logarithm laid straight between
level edges, exact at every edge and never more than 0.086 of a level from the smooth logarithm. A float differs in
having levels on both sides of 1 and a floor; the situated reader has proportion inside the corner and no floor.

**An older instance: Mercator's map.** On a globe at latitude φ let v = sin φ, the height above the equator, and
h = cos φ, the radius of the circle of latitude, so that v/h = tan φ and the globe's meridian is the quarter circle.
Mercator's map (Mercator 1569) stretches each circle of latitude by 1/h so that all are drawn the same width, and stretches the
vertical equally to keep shapes; the equal stretch, c = 1 at every place, is what keeps them (Proposition 5(g)). Summed from the equator, the height on the map is y = asinh(v/h), the textbook
ln tan(π/4 + φ/2) written as one relation. Near the equator y ≈ v/h, in proportion; past 45°, the corner, y approaches
ln(2·v/h), and each doubling of v/h adds a height approaching ln 2 (0.562, 0.651, 0.682, 0.690, 0.692 for the doublings
from 1 to 32). The pole is the horizon, h = 0, which is why the map is cut off short of it. The central cylindrical
projection, whose height is v/h itself, is the plain division, proportional throughout and unbounded; Mercator's map
keeps the division's local scale 1/h but accumulates it, and so lays the same relation in proportion before the corner
and logarithmically past it. Latitude is the Gudermannian of the map's height, φ = gd(y). It is the oldest instance we
know of the two address spaces laid out.

**What Mercator's map is, and what it is not.** The map is a chart of the whole globe, drawn once to be read from
anywhere on it. Past the corner it lays every level alike, each doubling of v/h the same height, about ln 2, and so it
favours no place: it has no focus. Where a navigator's attention falls on it is the navigator's, not the projection's.
A reader looking out from a standpoint is laid the other way on both counts.
- *Its picture is the turn.* Level ground seen from an eye one height H above it appears at arctan(H/d) below the
  horizon at distance d: 26.6°, 14.0° and 7.1° at 2H, 4H and 8H. Each doubling past the corner takes half the room of
  the last, the far field in proportion in h/v (θ ≈ π/2 − h/v), not in levels.
- *Its turn has a focus.* The turn's room per level is greatest at the corner and falls alike toward home and toward
  the horizon (the table below). Turning the head carries the corner, and the most room with it, to whatever is looked
  at; the near and the far field are held alike about it, each with enough to choose where to look next.
- *Mercator's levels belong elsewhere in its account.* They are distance laid by a count of addresses (Proposition 4),
  where every level is held alike because none is known beforehand to matter more, and direction laid about a point of
  gaze. How many levels off a thing lies, a day's walk or a month's, is not in the picture at all: it is the thing's
  size against H, which no reading fixes (Proposition 8) and which is carried in.

The map represents the field; the reader observes from somewhere within it.

**One figure, three rulers.** The circle, the number line and Mercator's height fit in one figure, and the figure shows
what each of them does with the corner. Draw the unit circle, the tangent line at A = (1, 0), and the unit
hyperbola u² − w² = 1, which touches the same line at A (u along the axis, w sideways). A reading x = v/h sits on the
tangent at T = (1, x). The circle's point P = (cos θ, sin θ), whose ray from the centre passes through T, and the
hyperbola's point (cosh ζ, sinh ζ) level with T, give

  x = tan θ = sinh ζ,  so θ = gd(ζ),

and each angle is twice the area of its sector from A: the circle's (Archimedes) and the hyperbola's (Saint-Vincent 1647; de Sarasa 1649). So one reading is
laid three ways, each an exact function of the others:

| ruler | room for the near field, x ≤ 1 | room for the far field, x ≥ 1 | room per level, per unit of ln x | the corner x = 1 | the reciprocal x ↦ 1/x |
|---|---|---|---|---|---|
| x itself, the writer's number line (§9) | 1, in proportion | unbounded, in proportion | x, more each level than the last | a point | not a reflection of the ruler |
| θ = arctan x, the turn | 45° | 45° | ½·sech(ln x), most at the corner, falling alike on both sides | the middle | θ ↦ π/2 − θ, a reflection |
| ζ = asinh x, the hyperbolic angle, Mercator's height | asinh 1 ≈ 0.881, nearly in proportion | unbounded, about ln 2 a doubling | x/√(1 + x²), rising to 1, every far level alike | a point; proportion gives way to levels around it, gradually | no reflection of the ruler |

So the one figure draws the near field and the far field three ways. On the turn they are halves, mirrored by the
reciprocal. On the hyperbolic angle they are the two address spaces above, proportion giving way to levels. On the
writer's line there is no split, only the point. Only the turn has a focus: its room per level is greatest at the
corner, ½ a radian per unit of ln x, and adds up over all the levels to the quarter turn; the hyperbolic angle gives
every far level the same room and has no greatest, and the writer's line gives each level more than the last. The
table "drawing of the same addresses" above compares the fisheye and the two lays in the same terms.

The third is the reader's lay of Proposition 4 made smooth. ζ ≈ x inside the corner and ζ ≈ ln 2x past it, and the
lay (x, then 1 + ln x) never exceeds it by more than 1 − ln 2 ≈ 0.307, approached far out (0.119 at the corner).

The three curves are the unit sets of the complex, split-complex and dual numbers (Appendix A).

All three carry the corner, since it is the reciprocal's fixed point (Proposition 1) and so a point of the reading
itself. Only the turn gives it a role.
- A measure uniform in θ puts its median at x = 1 with nothing else given (Proposition 5(b), (d)), because the turn's range,
  the quarter turn from home to the horizon, is fixed by the geometry and carried onto itself by θ ↦ π/2 − θ.
- The two unbounded rulers have no uniform probability until a range is given beforehand. A measure uniform in ζ over
  [0, Z] puts its median at x = sinh(Z/2), at the corner only when Z = 2 asinh 1 ≈ 1.763. A measure uniform in x over
  [0, X] puts it at X/2, at the corner only when X = 2. Either way the range, an amount, decides where the middle falls.

So the corner's point is shared, and its role as the median belongs to the turn. This is the division of §9 drawn on
one figure: the writer's ruler and the reader's lay hold the corner as a point, and only the reader's sweep makes it
the median. The rulers' rates against one another are dθ/dx = 1/(1 + x²), the Cauchy's density shape, and
dθ/dζ = cos θ.

**The proportion is in the addresses.** Within a doubling past the corner the lay's addresses are uniform; how uniformly
things arrive at them is up to the world. If what arrives is spread uniformly in direction, as a lighthouse's flashes
are (§7.1, §7.8), the far share h/v has density proportional to 1/(1 + (h/v)²), so the arrivals thin toward the corner
by 1.6 to 1 across the first doubling past it, 1.18 across the second and 1.05 across the third. That unevenness belongs
to the payload, not to the addresses. The two measures are different things on the same reading: the lay places far
readings, taken as amounts in H, past the reader's own breadth, and a uniform turn counts directions. When the
uniform turn is the inscribed sweep from the reader's standpoint, its law is the law of the addresses, §7; when it is the
sources' spread, it is the world's.

## 7. The Cauchy distribution is the address, not the payload

### 7.1 The circle, uniform by turn

The reader's one length, H, taken as 1, is a bar of length 1 about home. Its directions from flat (all h) to upright (all v), under
the uniform measure on turn, are the inscribed sweep, and each direction is one reading, v/h. The "steps" below are
pieces of that measure, not a motion: the directions are there together, and nothing turns through them (§2, "Given,
not performed").

**Proposition 5.** (a) Equal steps of turn give unequal readings. Near zero a step barely changes v/h; the corner is
halfway through the turn; near upright each step changes v/h by more and more, without bound.

(b) Counted per unit of v/h, the steps have density 2/(π(1 + (v/h)²)) on [0, ∞): the half-Cauchy distribution. Its
median is the corner, and the reciprocal leaves it unchanged. Over both quadrants, with v/h signed, it is the standard
Cauchy 1/(π(1 + (v/h)²)), with its median at zero and its quartiles at the corners ±1.

(c) Placing each reading at its angle of turn, rather than at its value, gives the *fisheye*: true scale near home,
compressed gently toward the corner and increasingly past it, with the horizon at the edge of the turn, never reached.

(d) *Conversely, the Cauchy requires one length.* Let a page or an instrument with two axes draw all of v at c times
the length of all of h, V = cH, and sweep in equal steps of direction from home. Its readings v/h follow the law of (b), with its median at the corner and
unchanged by the reciprocal, if and only if c = 1.

*Proof.* When the bar turns by a small angle, v/h changes by that angle times 1/h², and on the circle
1/h² = (h² + v²)/h² = 1 + (v/h)². So the steps per unit of v/h go as 1/(1 + (v/h)²), and normalising over a quarter turn
gives the factor 2/π. Half the turn lies on each side of 45°, and the substitution v/h ↦ h/v carries the density to
itself. (d) A direction θ′ from home in the drawing has tan θ′ = c·(v/h). With θ′ uniform on [0, π/2],
P(v/h ≤ r) = P(θ′ ≤ arctan(cr)) = (2/π)·arctan(cr): a half-Cauchy of scale 1/c, with median 1/c. The reciprocal
v/h ↦ h/v carries it to scale c. It is the law of (b), and unchanged by the reciprocal, exactly when c = 1. Read instead
on the page, as the drawn ratio c·(v/h), with the sweep uniform in its own parameter t (h = cos t, v = sin t), the law is
P(c·tan t ≤ r) = (2/π)·arctan(r/c), with median c: again the law of (b) only at c = 1. ∎

**A second route to the same law.** A payload taken to be unchanged by turns, with independent components, is the
isotropic normal, and its ratio is the Cauchy the addresses already were: a model consistent with the addresses, not
their cause (Appendix A).

**Why a turn and not a boost.** The Möbius maps of the reader's line come in three kinds of one-parameter flow: the
elliptic, a turn, with no fixed point on the line; the hyperbolic, a boost, which fixes two points; the parabolic, a
translation, which fixes one. Only the turn leaves unchanged a probability spread over the whole line, and that
probability is the Cauchy, the only one it keeps (the turns are the compact subgroup, and the measure they keep is its
Haar measure). Under a boost or a translation every point off the fixed points moves monotonically toward one of them, so
any probability they keep sits on the fixed points alone. So a measure on directions that treats every place alike and
is unchanged by its own motion can only come from a turn, and is the Cauchy; a sweep by boosts has no such measure to
give.

**Proposition 5, continued: two other parties.** (e) Let the reader read two other parties on its one length, so
that the relation lies on the sphere of Proposition 3(f) (written with three axes, V = V₂ = H), and sweep the positive octant h, v, v₂ ≥ 0,
uniformly by area. Write s = v/h and s₂ = v₂/h. Then:
- the readings (s, s₂) have density 2/(π(1 + s² + s₂²)^(3/2)) on [0, ∞)², the two-dimensional half-Cauchy;
- each of v/h, v₂/h and v/v₂ alone has the law of (b), with its median at its own corner and no mean;
- the six orderings of h, v and v₂ are equally likely, so the reader is near in both readings (h the largest) for a
  third of the octant, past in one for a third and past in both for a third;
- drawn on three axes at V = c₁H and V₂ = c₂H and swept uniformly by direction in the drawing, the medians of v/h, v₂/h and v/v₂ are
  1/c₁, 1/c₂ and c₂/c₁. Every pair keeps its corner only if c₁ = c₂ = 1, the reader's one length, and a pair keeps its
  own only if its two parties are drawn at one length.

*Proof.* The point of the octant in direction (1, s, s₂) is (1, s, s₂)/r with r² = 1 + s² + s₂². Projected from the
centre onto the plane h = 1, an element ds·ds₂ of the plane at distance r from the centre subtends dA = ds·ds₂·cos α/r²
of the sphere, where α is the angle between the ray and the plane's normal, cos α = 1/r; so dA = ds·ds₂/r³. In polar
coordinates on that plane, s = q cos χ and s₂ = q sin χ, ∫₀^∞ q·dq/(1 + q²)^(3/2) = 1, so the octant's area is π/2 and χ
is spread uniformly over [0, π/2]; hence s₂/s = tan χ, which is v₂/v, has the law of (b). Integrating s₂ out, ∫₀^∞
ds₂/(1 + s² + s₂²)^(3/2) = 1/(1 + s²), which gives the law of (b) for s, and likewise for s₂. Exchanging any two of h, v
and v₂ is a symmetry of the sphere that keeps the octant and its area, so the six orderings have equal areas; h is the largest in two
of them. In the drawing a uniform direction is (1, c₁s, c₂s₂) normalised, so (c₁s, c₂s₂) has the law above and each
median is divided by its c. ∎

**Why uniformly by area.** (e) takes the uniform area as its hypothesis. It enters where the uniform turn enters
for the circle, from the same premise: the reader's attitudes are the turns of one rigid bar, and it treats them alike
(§2). "Alike" means that the law of its attitude is unchanged by every turn, the whole group, not only by exchanging the
named parties or by shifting chosen angles; that is a premise about its ignorance, a choice (§12.1), and nothing in the
geometry compels it. Given it, the rest follows. With three unit relations those turns are all the rotations of the
sphere, and the only probability on the sphere that every rotation leaves unchanged is uniform area (the invariant measure of a compact group acting
transitively is unique; Haar 1933). Its part on the octant is (e)'s law, and with n + 1 unit relations the same holds on
the sphere in n + 1 dimensions. The exchanges of the parties alone do not fix it: they are a finite group, and many
laws on the octant are unchanged by them. Nor is it the law of the two sweeps taken uniformly in both angles: that is a
chart of the sphere, which a rotation changes, and it moves the near field to 0.233 (below). So the uniform area is
selected by the stated ignorance, as the uniform turn is; it is not forced by bounded observation alone. An observer
that weights its attitudes another way is not wrong: it implements another law of observation, with other shares.

The law of (e) is the Cauchy wedge, the sweep in three dimensions. Where two unit relations are swept by one uniform
turn, three are swept uniformly over the octant's area, and every pair it holds is swept as the circle is; uniform over
the area is not uniform in both angles, which keeps only the pairs each angle reads ("Swept by altitude and azimuth",
below). The wedge is made at each observation, not taken from a sphere the reader holds: the whole sphere, every octant
drawn together, is the writer's. A sphere that placed every place by its direction and its distance would need every
distance, which no situated reader has. The wedge needs no size: the readings are ratios, laid by the two-dimensional
Cauchy. What a blueprint would add is what it adds to the circle, once per party: V*/H and V₂*/H. On the circle near and far were halves;
with three parties the reader is near in both readings for a third of its addresses.

**Swept by altitude and azimuth.** Reached by the two sweeps of §2, the uniform octant is uniform in azimuth and uniform
in height v, not in altitude. By Archimedes' hat-box theorem (*On the Sphere and Cylinder*), a zone of a sphere has area
in proportion to its height, so the octant's area between azimuths ψ₁, ψ₂ and heights v₁, v₂ is (ψ₂ − ψ₁)(v₂ − v₁):
Lambert's equal-area map (Lambert 1772), with the altitude's density cos a. Swept that way, every pair keeps its corner
and the near field is a third, as (e) states. Swept uniformly in both angles instead, each sweep keeps its own corner (a
uniform azimuth keeps v₂ = h at the median however the altitude is weighted), but the pair that neither sweep reads
leaves its corner: v ≤ h for 0.343 of the readings, and the near field shrinks to 0.233, because the rings of azimuth
narrow toward the vertical. The raise uniform in height belongs to three unit relations only: with two, the uniform
sweep is the turn itself; with four, the height's density on the uniform orthant is (4/π)√(1 − t²).

**More parties.** The same holds for any number n of other parties, each read on the one length H. There are then n + 1 unit
relations, so by Proposition 3(d) with m = n + 1, and 3(e) applied to each pair as in 3(f), the relation lies on the unit
sphere in n + 1 dimensions. The wedge is its positive orthant, one of 2^(n+1), and the point in direction (1, s) is (1, s)/r
with r² = 1 + |s|², s = (v₁/h, …, v_n/h). The projection argument of the proof gives the element of area ds/r^(n+1), so
the uniform orthant's readings have density Z_n·(1 + |s|²)^(−(n+1)/2), the n-dimensional half-Cauchy, with
Z_n = 2ⁿ·Γ((n + 1)/2)/π^((n+1)/2). Integrating out all readings but one leaves the law of (b); all but two, the law of
(e). So every reading and every pair keeps its corner, and adding a party changes nothing about the pairs already held.
Exchanging any two of the n + 1 unit relations is an isometry of the sphere that keeps the orthant, so it preserves the
uniform area on it; every ordering of them is then equally likely and h's rank among them is spread uniformly. The pairs'
corners alone would not give this: a weight on two of the six chambers of the octant can keep every pair's median at its
corner and never have h the largest. The reader is near in all its readings (h the largest) for 1/(n + 1) of its
addresses, a half, a third, a quarter, and so on, and the number of readings past their corner is spread uniformly over
0, 1, …, n. Drawn on a page at unequal lengths, these shares move, as in (e). None of this involves any party's true breadth, or
any breadth of another party at all. The turn of H is the geometry's whole work; each true breadth is one number of the amounts, a shift in levels of that party's
amounts alone.

In classical terms the readings are the tangent of a uniformly distributed angle: the gnomonic projection of a uniform
direction. It is also the one chart that keeps lines straight (Appendix A). For two other parties the gnomonic projection of a uniform direction on the sphere is the multivariate Cauchy
(the multivariate t with one degree of freedom), whose marginals are Cauchy (Cacoullos 2014). The gnomonic projection is
the image plane of a pinhole: a direction (1, s, s₂) lands at (s, s₂) on a flat screen one unit along h, so the Cauchy
wedge is what such a screen records of directions arriving uniformly over the octant, with no reader dividing anything
(§9). With α the angle off the axis, 1 + s² + s₂² = 1/cos²α, and the density is (2/π)·cos³α, the solid angle a flat
screen receives per unit of its area: the geometric part of the classical cos⁴ falloff across a camera's image. The
sweep's own density is (2/π)·cos²θ (§4), and with n other parties it is Z_n·cos^(n+1)α: one more power of the cosine for
each party added.

**Working back from the Cauchy.** The Cauchy is known: it is the tangent of an angle turned uniformly. Read backward,
from the known law to what it needs, each step is forced by the one before.
1. The readings follow the law of (b): distribution function (2/π)·arctan(v/h), median at the corner.
2. Then the angle θ = arctan(v/h) is turned uniformly, since P(θ ≤ t) = P(v/h ≤ tan t) = 2t/π.
3. That angle is the direction from the standpoint only if all of h and all of v are one length, by (d). For the reader
   they are, being shares of its one length H. On a page drawn at V = cH, a uniform turn of direction puts the median
   log₂ c levels off the corner. No other uniform choice
   rescues it. Uniform steps along the stretched curve give no Cauchy at all: for c = 2 the quartiles of v/h are 0.316,
   0.739 and 1.673, not a reciprocal pair. Uniform steps of the ellipse's parameter do give the law of (b), but that
   parameter is the turn of the circle of one length, stretched afterwards.
4. With one length the sweep is one rigid bar turning, and it traces the unit circle (Proposition 3(c), (e)).

So the one length is not a convenience laid under the Cauchy. It is what the Cauchy, on one quadrant the half-Cauchy with its median at
the corner, requires, and, forward through Proposition 3 and parts (a) to (c), it is also enough. Every link of the chain, from the
reader's one length to the Cauchy and back, passes through a turn of that length, and nowhere through a second one.
Stated as uniqueness, and no more: among the two-axis drawings V = cH whose sweep is a rigid turn and whose readings are
reciprocal-symmetric, the equal-length drawing c = 1, the reader's circle, is the only one, and it gives the half-Cauchy
with its median at the corner (the standard Cauchy signed over two quadrants). That a reader sweeps by a turn at all is not this result; it is the premise of
Proposition 3(g).

**Uniform in what.** Bertrand's lesson is that "uniform" needs a parameter, and different parameters give different
laws. On a page drawn at c = 2, uniform in the angle drawn on the page puts the quartiles of v/h at 0.207, 0.5 and
1.207, and uniform along the stretched curve at 0.316, 0.739 and 1.673. For the reader the parameter is fixed by
Proposition 3(g): its sweep is a flow Φ(t), one motion repeated, and in that flow's own inner product
(h, v) = (cos ωt, sin ωt). Uniform means uniform in t, the one parameter the flow carries, and then the readings are
the half-Cauchy, whatever page a writer later draws them on. The competing laws belong to the page, each uniform in a
parameter a writer's drawing adds: an angle measured on the stretched page, a length along its curve. So the exact law
is forced given the premises of Proposition 3(g) (a sweep that is continuous, linear and returning); whether a reader's
sweep is such a flow is the open question it leaves (§12.2, question 2).

**Proposition 5, continued: two familiar pictures.** The best-known pictures of a turn laid out on a straight line
are a lighthouse's flashes on a shore and Mercator's chart of the globe. Each is a drawing with two axes, so each has a
c; each requires c = 1, and each separates it from the size, which stays free.

(f) *The lighthouse.* A lamp stands at distance β from a straight shore, opposite the shore's point α. It sends flashes
at angles θ from the perpendicular, spread uniformly over the half turn toward the shore.
- A flash at θ lands at x = α + β·tan θ. Its offset from the foot over the lamp's distance is the reading:
  (x − α)/β = tan θ.
  - **Zero** is the foot.
  - **The corners** are the flashes at ±45°, which land at α ± β.
  - **The horizons** are the shore's two ends.

  The landings follow the law of (b) over both quadrants, and half of them lie within β of the foot.
- The flash's path, β/cos θ, differs from flash to flash and cancels from the ratio of its two legs: β out to sea and
  x − α along the shore. One length remains, β. It is the same for every flash because the shore is straight.
- Draw the shore at c times the length of the sea: V = cH, with H drawn at the lamp's distance.
  - The half-way flash then lands c drawn lamp-distances from the foot and is drawn at arctan c.
  - The share of landings within one drawn lamp-distance is (2/π)·arctan(1/c).
  - The drawn readings follow the law of (b), with the median at the corner and unchanged by the reciprocal, if and only
    if c = 1.
- Drawn at c = 1, but with any H in place of β, each landing is laid H·tan θ from the foot. Every angle is kept and the
  45° flash is still the corner; every length is off by β/H, in both directions alike.

(g) *Mercator's map.* On a globe of radius 1, take a chart that draws the parallels as horizontal lines of one length
(x the longitude λ) and puts the latitude φ at height y = f(φ). It draws a step east at sec φ times its length on the
globe and a step north at f′(φ) times. Write c = f′(φ)·cos φ for the ratio of the two: V = cH at that place, with H the
step east.
- A course of constant compass bearing ψ is drawn, where it crosses the latitude φ, at bearing ψ′, with
  tan ψ′ = tan ψ/c.
  - Every bearing is drawn true, and the course northeast (the corner between north and east) is drawn at 45°, at
    every latitude, if and only if c = 1 everywhere.
  - That is, f′(φ) = sec φ and y = ln tan(π/4 + φ/2) = asinh(tan φ): Mercator's map. There every such course is a
    straight line at its true bearing.
- A small circle on the globe is drawn as an ellipse whose axes stand in the ratio c. This is the bar of Proposition 3(c)
  traced in two units, and it is Tissot's indicatrix (Tissot 1881). It is a circle only on Mercator's map.
- Mercator's map draws lengths at sec φ in both directions at latitude φ, so its areas are sec²φ times true. That is a
  zoom which changes from place to place and keeps every angle.
- A chart that keeps areas instead must have c = cos²φ, which is 1 only on the equator. No chart of the globe keeps both
  angles and areas (Euler 1777; Gauss 1828).

In v and h (§6), with v = sin φ and h = cos φ:

| chart | height y | in v and h | c at latitude φ | the course northeast, drawn at latitude 60° |
|---|---|---|---|---|
| plate carrée | φ | arctan(v/h), the turn | cos φ | 63.4° |
| Lambert's equal-area | sin φ | v | cos²φ | 76.0° |
| central cylindrical | tan φ | v/h, the division | sec φ | 26.6° |
| Mercator's | asinh(tan φ) | asinh(v/h) | 1 | 45° |

**Two charts.** Mercator's chart keeps local angles, so a course of constant compass bearing is a straight line on it.
That keeps the addresses, for which the relation that matters is a direction: the ratio of a step east to a step north.
It does so by an area scale of sec²φ, a zoom that grows with latitude, and areas are amounts, the payload's. On the
chart Greenland looks comparable to Africa, about two-thirds its
size, when Africa is in fact about fourteen times larger. An equal-area chart such as Lambert's keeps the relative
areas instead, at the cost of the bearings. The two charts keep different properties of the same globe. No flat chart
keeps both (Euler 1777; Gauss 1828), and nothing obliges a reader to use either: each chart follows from the property
it keeps. Only the globe itself, the complete object, keeps every direction and every area at
once; it is the common reference from which both charts are drawn.

*Proof.* (f) The flash at θ meets the shore where its leg out to sea, of length β, and its leg along the shore, x − α,
stand at angle θ. So (x − α)/β = tan θ, and the path, β/cos θ, divides out of the ratio. With θ uniform on (−π/2, π/2),
the law of (b) over both quadrants follows as in the proof of (b), and P(|x − α| ≤ β) = P(|θ| ≤ π/4) = ½. Drawn with the
shore at c times, the drawn reading is c·tan θ, so P(|c·tan θ| ≤ r) = (2/π)·arctan(r/c). That is a Cauchy of scale c,
with median c. The reciprocal carries it to scale 1/c, so it is the law of (b), and unchanged by the reciprocal, exactly
when c = 1, as in (d). (In (d) the uniformity is in the drawing's directions, so the median there is 1/c; here it is in
the lamp's turn, so it is c. Either way only c = 1 keeps the corner.) The flash at 45° is drawn at c·β from the foot, at
angle arctan c. Laying each landing H·tan θ from the foot multiplies every length of the true figure by H/β, which is a
similarity.

(g) A step dφ north has length dφ on the globe and f′(φ)·dφ on the chart. A step dλ east has length cos φ·dλ on the
globe and dλ on the chart. So the chart's scales are f′(φ) north and sec φ east, and their ratio is c. A course at
bearing ψ moves east and north in the ratio tan ψ, so cos φ·dλ = tan ψ·dφ, and on the chart
dx/dy = dλ/(f′(φ)·dφ) = tan ψ/c. That is tan ψ for every ψ only if c = 1. Where c = 1 at every latitude, dx/dy is
constant along the course, so the course is drawn straight. Integrating f′ = sec φ from the equator gives
ln tan(π/4 + φ/2) = asinh(tan φ).

A circle of small radius δ, its points δ·(cos t, sin t) north and east, is drawn as δ·(f′(φ) cos t, sec φ sin t): an
ellipse with axes in the ratio c. With f′ = sec φ both scales are sec φ, and areas are multiplied by sec²φ. Keeping
areas means f′(φ)·sec φ = 1, so f′ = cos φ and c = cos²φ. On any chart, keeping angles makes the two scales equal at
each place, and keeping areas makes their product 1. Both together make every scale 1, a drawing of the sphere on the
plane without stretch, which its curvature forbids (Gauss's theorema egregium). ∎

**What the two pictures show.** Each lays a uniform turn on a straight line: the lamp's flashes on the shore, and a
navigator's bearings on the chart. Each keeps the turn true only when its two directions are drawn at one length.
- **The lighthouse** shows it on one picture. Drawn with the shore stretched, the half-way flash leaves 45°, half the
  landings no longer fall within one drawn lamp-distance of the foot, and the near half no longer mirrors the far half.
- **Mercator's map** shows it at every place. It is the one chart of its kind on which the corner between north and
  east is drawn at 45° everywhere.

What each leaves free is the size: the lamp's distance, which the picture can be drawn at any value of, and the local
scale sec φ, which Mercator lets grow toward the poles. Both are zooms, which change every length and no angle. That is
the distinction this paper draws throughout: in a drawing with two axes, c = 1 is required for the turn and its
readings, which is the circle the reader's one length already is, and the true size is one number the readings do not
fix.

Mercator's choice (keep the angles, give up the areas) is what the reader's one length gives: its circle is c = 1 written
with two axes, and the size is left to be estimated. It is not the reader's view. The chart lays the far field in levels, all
alike, with no focus; the reader's turn is centred on what it looks at, its far field in proportion (§6, "What
Mercator's map is, and what it is not"). The familiar complaint about his map, that it draws Greenland as large as Africa, is a
complaint about the zoom, not about the drawing.

The two pictures meet on a chart. A lighthouse charted on Mercator's map is drawn true at every latitude. On a plate
carrée chart at 60°, with the shore running east–west, its half-way flash is drawn at 63.4°.

In the lighthouse the uniformity is the lamp's, a fact about the world (§7.8). A reader standing at the lamp and reading
each landing by its direction holds tan θ itself, with no β at all and no second length: its one length gives the turn,
so the requirement of (d) is met before it can arise.

**The addresses' hyperbolic secant.** The inscribed sweep's addresses, taken together, each with its share of the turn,
form a bell; the central sweep's payloads are a different thing, read by their mean (§3.1). On the logarithmic axis
ξ = ln(v/h) the shares form the hyperbolic secant density, a bell centred on the corner,

  ½·sech ξ = 1/(v/h + h/v),  with total area π/2, a quarter turn.

On the plain axis the same shares are 1/(1 + (v/h)²), Cauchy's curve. The sech density and the fisheye are one function:
the area under the sech density up to ξ is arctan(v/h) = π/4 + ½·gd(ξ), the fisheye's radius there, because the
Gudermannian is the running area under sech. Taken direction by direction the addresses give the running total, which is
the fisheye; taken together, every share, which is the sech density. It is not the normal curve, which belongs to the
payload's mean. With the same peak and area the two look alike near the corner, but one level out from it the sech
density stands at 0.400, then 0.235, 0.123, 0.062, halving with every further level and keeping a share in every level
without end, while the normal curve falls ever faster and its far levels vanish (0.043 at the fourth level against the
sech density's 0.062, and 0.002 against 0.016 at the sixth). The sech density has a horizon; the normal curve has none.

### 7.2 The main result

> **The Cauchy is not the payload; it is the address to the payload.**

**An address is not a payload.** The two are different kinds of thing, and this paper keeps them apart throughout. An
address is a point: a direction, a reading [h : v], a place on the reader's line. A payload is what is found at that
point: an amount, a function on the addresses. The law of the addresses, the Cauchy, is a measure on the points, the
uniform turn carried onto them; it is fixed by the standpoint and the turn alone, and no payload enters it. Whatever
arrives can be swapped for anything else, at any address, and the addresses and their law do not move (Theorem 6(a)).
So nothing the Cauchy says (its median, its scale, its missing mean) is a statement about the payload, and nothing in
the payload can be read from it. The two have no connection. They share one place, the landing point where the ray from
home meets the radius (§4), and nothing passes between them there: the address carries none of the payload, and the
payload none of the address or its law.

**Why the distinction has to be stated.** A number on the real line carries no mark of which it is, an address or a
payload. A representation that does not mark the difference holds the two as one object; there is no third case, in
which the distinction is present but unstated. Mathematics separates direction from magnitude in many places: polar
coordinates, a unit vector and its norm, the projective line. A Cauchy variable written as a value x = tan θ on the real
line is not among them. There one number is both where a reading is made and what is read, so the law of the turn is
read as a law of amounts, and a mean is asked of it. This is a statement about that representation, not about anyone's
intentions or results. Unmarked, the two cannot be told apart; marked, they separate exactly: the address is a point of
the projective line, where its law has a median and its missing mean belongs to the chart (§4), and Theorem 6(a) shows
that no payload moves it.

**The rule, and a test.** The rule is this paper's, offered as a reading, not a law of nature: a Cauchy variable is a direction, a point of the projective line, a ratio [x : y] read in one
chart, laid by a turn. It is never an amount. Its median and its quartiles are places on that line and mean what they
say; it has no mean, since its tail makes the first moment diverge, and in this paper's terms none is wanted, since the coordinates of directions do not add. Two directions have no sum, only a composition, a
turn followed by a turn, which in the chart is tangent addition (§2). Where a Cauchy appears beside an amount, the two
are separate factors: the amount is the payload, and the Cauchy is where it lands. So for any Cauchy met in practice
there is a test: find the turn, and find the amount. In the lighthouse the lamp turns and the flash is the amount. For a
ratio of two components of a spherically symmetric vector the turn is the vector's direction, uniform, and the amount
its length, which cancels (part (a) below).

A sum of independent Cauchy variables, which is again Cauchy, looks like amounts added, and is not: it is a relay of
standpoints. Land a uniform turn made from a height γ₁ + γ₂ on the line at height γ₂, take that landing as the next
standpoint, and turn again down to the line: where it lands is the sum of two Cauchys of scales γ₁ and γ₂, and it lands
exactly as one uniform turn from height γ₁ + γ₂ would. What adds is the standpoints' heights and feet, the parameters m
+ iγ (McCullagh 1996), which are amounts; the sum itself is still a direction from the combined standpoint, read by its
order, with no mean. It is not the composition of the two directions: that, tan(θ₁ + θ₂), is a turn of uniform angle
again and keeps the scale 1 where the sum of two standard Cauchys has scale 2.

**Once a Cauchy, always a Cauchy.** Every operation a reader can make on a direction keeps the law in the family, and
moves only its one point m + iγ, the standpoint's foot and height above the line:

| What the reader does | What the law does |
|---|---|
| starts again from a new zero (a turn) | a Möbius map: Cauchy to Cauchy |
| divides by the other unit relation (the reciprocal) | Cauchy to Cauchy |
| rescales its drawing, or zooms | Cauchy of another scale |
| relays through a standpoint between | the sum: Cauchy |
| averages n readings | the same Cauchy: nothing gained, nothing lost |

The table is about the signed reading over two quadrants, the law on the whole line. The reader's own readings over one
quadrant are the half-Cauchy, which a turn carries off its arc and whose average grows like (2/π)·ln n.

The closure under Möbius maps and under sums is classical (Knight 1976; McCullagh 1996; Lévy 1925); the reading is that
the family is closed because it is the reader's addresses, and that its one parameter is where the reader stands. The
normal law is its counterpart among amounts: closed under sums and rescalings, the operations on amounts, and not under
ratios, reciprocals or turns, where a ratio of two independent centred normals becomes a Cauchy (§7.1). Taking a ratio
carries the one fixed law into the other.

**What breaks it.** Only operations that are not operations on directions. Folding a reading to its size, |X|, is not
one of them: it keeps the half-Cauchy, the quadrant's law, which the reciprocal keeps too. The breaks are these.
Squaring, X², which is not a reading of any turn. Cutting the line at an edge, as a flat screen of finite width does, so
that the addresses past it are lost (§3.5). Multiplying each reading by an amount that varies, A·X with A random and
positive, which gives a mixture of scales and no single standpoint; the characteristic function E[e^{−A|t|}] is
e^{−γ|t|} only when A is constant. Adding an amount to each reading, X + N, as the thermal velocities of emitters add a
Doppler shift to every address of a line: the profile becomes Voigt's, normal at its core and Lorentzian in its wings.
Pooling readings taken from different standpoints without relaying them, which gives a mixture of Cauchys with different
centres. And counting the turn against something other than itself (a lopsided clock, the payload's density), which
changes the law; if that weight treats the two parties alike the median stays at the corner (Theorem 6(e)), if not it
moves. In each, an amount has entered: a writer's move, not a reader's. Even then the far field holds: an added amount
of finite spread leaves the tails ~ γ/(πx²), so the Cauchy is lost first near its centre and last at the horizon, which
is why the wings of a Voigt line's normalized profile still read its half-width.

**Three properties of one law.** Read together, the closure above, Theorem 6(a) and the far field are what make the
Cauchy usable as addresses. A reader can sweep with it and stay in the family, moving only m + iγ. The payload can be
changed at every address and no address moves. And where an amount enters, the law is broken from its centre outward,
its tails ~ γ/(πx²) kept to the last; only cutting the line at an edge, or taking a power of the reading, takes the
tails.

The plainest instance in practice is a spectral line. Spectroscopy writes a line as a strength times a profile, I(ν) =
S·φ(ν − ν₀) with ∫φ = 1. The strength S is an amount, in physical units, and the strengths of separate lines add. The
profile of a resonance is the Lorentzian, φ(ν) = (1/π)·dδ/dν, where δ is the phase of the response, tan δ = γ/(ν₀ − ν),
which turns through half a turn as the line is crossed: the profile is the frequency line laid by a uniform turn of that
phase, the address. Spectroscopy reads the profile by its centre and its half-width at half maximum, γ, which for a
Cauchy is half the interquartile range, and reads the strength by its integral: the address by its order and the amount
by its sum, as Theorem 6 says each must be read. The line's cross-section has the same shape, γ²/((ν − ν₀)² + γ²) =
sin²δ, since at every address the density is 2/π times the foot of the point it points to (§4); but it is bounded by 1,
a share of what arrives, the payload's, not the address.

Call a statistic of a set of readings an *address statistic* if it depends only on their order, so that for every
strictly increasing f it picks out of f(X) the image of what it picks out of X (the ranks, the median, the quartiles),
and a *payload statistic* if it depends on their sizes (the mean, any sum). Which side of the corner a reading lies on
is kept only by the increasing maps that fix 1, those that commute with the reciprocal; it belongs to the exchange, not
to order alone.

**Theorem 6 (the separation of address and payload).** Parts (a) and (d) concern the readings of Proposition 5: the circle of the reader's one length,
swept uniformly by direction. Parts (b) and (c) hold for any finite set of readings. Part (e) drops both the circle and
the uniform turn. The readings are the addresses: directions, ratios with no amount in them, so what (a) and (d) find
is a property of the uniform turn that lays them, and what (e) finds a property of any reciprocal-symmetric sweep, and
neither is a property of what is read; the amounts that arrive along them, the payload, are what (c) concerns.

(a) *Nothing that arrives changes the Cauchy.* Suppose that whatever arrives along each direction lies at some
reach ℓ > 0, an amount that may differ from direction to direction and is unknown to the reader. In the reader's unit
its components are ℓ·h and ℓ·v, and the reading is (ℓ·v)/(ℓ·h) = v/h. The readings of Proposition 5, their Cauchy count
and the fisheye are therefore the same whatever arrives, and are fixed before anything does: the law of the addresses is
independent of the payload assigned to them. What does not cancel is the ratio of amounts, (v·V*)/(h·H) = (V*/H)·(v/h),
which keeps the factor V*/H; that is why one standpoint cannot give the true size (§9). The cancellation is an identity
about this representation of what arrives, an amount along a given direction; that the directions are the reader's
addresses is this paper's reading of it, and whether a particular instrument's arrivals have this form is a question
about that instrument (§12.2).

(b) *Address statistics ignore the payload.* For a finite set X of readings and any strictly increasing map f, the set
f(X) has the same ranks as X, so every address statistic picks out the same element; for an odd count,
median f(X) = f(median X). Conversely, two sets with the same ranks are carried onto one another by some strictly
increasing f, so the ranks keep exactly what survives every such change, and nothing more.

(c) *Payload statistics do not, the mean among them.* Among the strictly increasing maps of (b), only an affine f commutes with the mean on
every set of readings: for any such f that is not affine there is a set X with mean f(X) ≠ f(mean X). For convex f, mean
f(X) ≥ f(mean X) on every X, with equality only if f is affine on the smallest interval containing X.

(d) *The Cauchy is an address law.* Over one quadrant its median is v/h = 1, the corner, and its quartiles are √2 − 1
and √2 + 1, a reciprocal pair. Its mean does not exist: ∫₀^s x·2/(π(1 + x²)) dx = (1/π)·ln(1 + s²), which grows without
bound.

(e) *The median needs only reciprocal symmetry, and the missing mean a density of h bounded away from zero near the horizon.* Let the sweep
follow any continuous path from all of h to all of v that comes near h = 0 only at its end, with any weight, both
unchanged by exchanging the two parties. Then the readings' law is unchanged by the reciprocal and the corner is a
median of it, the only one where the law increases strictly through 1. If moreover the law of h has a density at
least f₀ > 0 on some interval (0, δ), the mean does not exist. The uniform turn on the circle is the case that gives the
Cauchy of (d).

*Proof.* (a) holds by construction, a reading being a direction; it is stated so that (b)–(e) can be read against
it. (b) Strictly increasing maps preserve ranks; the converse follows by monotone
interpolation between matched points. (c) A strictly increasing f that satisfies f((a + b)/2) = (f(a) + f(b))/2 for all
a, b is affine, so a non-affine f fails it for some pair, and X = {a, b} is the set required. Monotonicity, or some
other regularity such as measurability, is needed: an additive function built on a Hamel basis, plus a constant,
satisfies the midpoint equation and commutes with the mean of every finite set without being affine. The inequality and
its equality case are Jensen's. (d) Over one quadrant the distribution function is (2/π)·arctan(v/h), which is ½ at
v/h = 1 and ¼ and ¾ at tan(π/8) = √2 − 1 and tan(3π/8) = √2 + 1; the integral is elementary. (e) The exchange carries
v/h to h/v and leaves path and weight unchanged, so v/h and 1/(v/h) have one law. Then P(v/h < 1) = P(v/h > 1), each at
most ½, so 1 is a median, and the only one where the law increases strictly through 1; for a continuous law this is
F(1/x) = 1 − F(x) and Proposition 2(b). The path ends at all of v and comes near h = 0 only there, so there are δ > 0
and v₀ > 0 with v ≥ v₀ wherever h < δ: on the path itself, not only with some probability. Then P(v/h > r) ≥ P(h < v₀/r) ≥ f₀·v₀/r once v₀/r < δ, where f₀ > 0 bounds the density
of h below δ from below; then ∫ P(v/h > r) dr diverges, and so does the mean. ∎

The theorem is elementary; its content is the reading. The addresses are given before anything arrives, and nothing that
arrives moves them: (a) for every single reading, (b) for every statistic of their order, and (c) says why no statistic
of size can be read from them. The Cauchy distribution is not a law of anything the reader meets. It is the reader's own layout of directions, counted. What arrives in each direction cancels from every single
reading, not merely on average, so the readings tell rays apart, not points. The Cauchy is where the reader can put what
arrives, never what arrives.

**What the result establishes, and what it does not.** The argument has three steps.
1. The addresses are given without any reference to what arrives: the uniform measure on directions from home.
2. Changing what arrives, while keeping the sweep, leaves the readings and their distribution exactly as they were
   (Theorem 6(a)).
3. So the Cauchy is a property of the sweep, the uniform turn itself, and finding it is no
   evidence by itself that anything in the world is distributed that way.

Two things are not claimed. The theorem does not show that every real observer counts by the sweep rather than by a
clock, a flat sensor or what arrives (§2); it shows what the sweep's count gives, and why the turn,
measured by itself, is the count that prefers no attitude (§2, §7.5). Nor does it show that every Cauchy distribution
met in data has this origin; a Cauchy met as data may have others, and the next paragraph says what sets its scale when
it is formed from a reading.

Third, a sweep is uniform by definition, a turn measured by itself (§2), so the uniformity is never in question; what
can differ is what is counted. Counted along the sweep, the law is the standpoint's addresses, as step 1 defines
them. Counted as arrivals from sources that happen to be spread uniformly in direction, the same shape is the payload's
density over directions, a property of the world, and "addresses" would be the wrong name for it. What does not depend
on what is counted:
- the reach cancels from every single reading, not on average (Theorem 6(a));
- order survives every change of payload (Theorem 6(b));
- only an affine map commutes with the mean on every set (Theorem 6(c));
- the median at the corner for any weight that treats the two parties alike, and the missing mean for any whose density
  of h also stays above zero near the horizon (Theorem 6(e)). Only the Cauchy's exact shape needs the uniform turn.

These give a reader a reason to prefer order whatever the uniformity is: order is what survives a payload it does not
know.

**Where the usual confusion comes from.** Laid uniformly by direction, the sweep is uniform and bounded, g from 0 to 1,
with its middle at the corner: geometry, with nothing wild in it. Read on the axis v/h, the same lay is a Cauchy of
scale 1. That needs no knowledge of the true V*, since h and v each run from 0 to 1; it needs only the reader's one
length, which the Cauchy requires (Proposition 5(d)) and the reader always has. Read in amounts against the true breadth it is another Cauchy, of
(v·V*)/(h·H) = (v/h)·(V*/H), with scale V*/H. Writing that one as the standard Cauchy, of scale 1, silently takes the
mountain's true breadth to be the drawn one: it turns a situated reader into situation 1, the circle, without knowing
V*. A situated reader has one length, and a writer writes its circle V = H (§5); the confusion is taking that circle
for a measurement of the mountain. Taking the mean of the readings then applies an operation on amounts to addresses, and the missing mean is
what that costs: it comes from the unbounded axis of the reading, not from the world. Where a Cauchy is met as data
rather than laid as addresses, an amount has been formed from the reading by a known length, and the distribution's
scale is that length, not 1 by assumption.

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
  levels, and the answer is ln 6/ln 9 ≈ 0.8155 (§12.2, question 2).
- *The marginalization paradox.* Under an improper prior on a scale nuisance, integrating it out of the data and
  reasoning from statistics free of it can disagree (Stone and Dawid 1972; Dawid, Stone and Zidek 1973). Read with the
  reader's own measure on the other's size, dη/η, they cannot. For amounts y = η·w, n of them, the first reasoner's
  likelihood ∫ η^(−n−1) f(y/η | ζ) dη and the second's, from the direction u = y/|y| alone, ∫ r^(n−1) f(r·u | ζ) dr,
  differ by the factor |y|^n, which carries no ζ: the same conclusion from the same prior, whatever the law f. Reading
  the data's direction is reading its address, and the scale's invariant measure is what makes the two agree (§12.2, question 7).
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
  belongs to amounts, the median to addresses (Theorem 6(b), (c)).

**What is observed, and what the reading predicts.** The address law is not the law of anything observed, and the two
are easily run together: every Cauchy met in practice, a ratio of two normal amounts, a heavy-tailed sample, a line's
profile, is the law of something observed. The reading relates them. Counted against what arrives, the readings' law is
the turn's law weighted by how what arrives is spread over the directions (§2). It is the Cauchy exactly when what
arrives is spread evenly over the reader's addresses, as a pair of independent centred normal amounts of equal spread
is, its direction uniform by turn. So the reading makes a claim the usual readings do not: an observed law of Cauchy
type has a uniform turn behind it (a rotation, a phase advancing steadily, or the direction of a pair of
independent amounts of one spread), and its departure from the Cauchy is the
spread of what arrives over directions, which can be measured on its own. Its median stays at the corner exactly when
that spread weighs the two sides of the corner alike (Theorem 6(e)), and moves only by the part that does not. That is the test,
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
Cauchy (§11), and the count's dipole is 2β to first order, Ellis and Baldwin's "2", from the addresses alone (Ellis and
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
central sweep's height and foot (§4), full visibility only at the corner. On Aspden, Padgett and Spalding's frames (2016)
the two slits' shares give 2hv = 0.997 and 1.000, the pair at its corner; the measured contrast, 0.69 and 0.56, lies
under that bound, short by the source's coherence; the photons are independent draws from one pattern that does not
drift, and the fringe period is fλ/d to 0.3% and 1.7%. The bound is set by the two shares alone, the geometry's; how far
below it a pattern falls is the source's, what arrives. All of this is classical; the reading is the sort.

### 7.3 In the picture of the hand

Spread the fingers uniformly by turn and read each one as v over h: the readings are the Cauchy, and nothing of the
colours is in them.
- *The median is a finger.* Of five fingers spread uniformly from flat to upright, the middle one, at 45°, is the
  corner. Order, ranks, quartiles and the corner are address statistics, and they ignore the colours.
- *The corners are the quartiles.* With the fingers spread over both quadrants, the corners at ±45° are the quartiles of
  the standard Cauchy. So anything whose two ends sit at the reader's corners takes exactly the middle half of its
  fingers, whatever its size and however far away: the mountain range of §10 is one.
- *The missing mean asks the fingers about the colours.* The readings' tail makes their mean diverge. In the hand's terms
  that is no loss: a mean is a sum of sizes, a question about the payload, and the readings carry no size. The median, a
  question about addresses, always has one.
- *More fingers, not brighter glass.* A finer count of the sweep lays more addresses. It buys precision about where, never
  about what. What is at the addresses comes only from payload held beside them.
- *The glass hides; the hand does not.* Two panes on one finger's line show only the nearer. Every back side is made
  by the payload; the addresses hide nothing.
- *Three breadths.* In space the fingers spread through a solid wedge and, spread uniformly, give the two-variable
  Cauchy, with density proportional to (1 + |s|²)^(−3/2). Each pair of readings keeps its median at its own corner
  (Proposition 5(e)), but the radius |s| does not: only 1 − 1/√2 ≈ 0.29 of the addresses have |s| ≤ 1, and the median of
  |s| is √3. That median is still an address, though not a corner.

**In the picture of an array.** A closed curve stored as N samples x[k], y[k], at the places θ_k = (k + ½)·2π/N, makes
the same split in a form any programmer knows. An array is a representation: whoever builds it chooses its indexing, and
the world has no indices of its own. The picture shows that addresses and payloads can be held apart; why a reader's
addresses follow the uniform turn is Proposition 5's, not the array's.
- *The index is the address.* The places are fixed by the index before any value is stored, at equal steps of turn.
  - Read as slopes of the inscribed angle (§4), s_k = tan(θ_k/2), they are, for even N, exactly the N evenly spaced
    quantiles of the standard Cauchy. A finite array samples the continuous law at N quantile locations; the law
    itself is the continuous turn's (Proposition 5).
  - For even N, half of them lie within the corner, |s_k| ≤ 1.
  - For odd N one place falls on the horizon itself, [0 : 1], an address like any other, and the share within the
    corner is not exactly a half.
- *The stored values are the payload.* Changing them moves no place, so the places' ranks, their median and their
  corner are untouched by anything stored (Theorem 6(a)).
- *Places compose without angles.* The offset from one place to another is the tangent subtraction of their slopes:
  turns composed (§2).
- *Where the array is not the reader.* An array index is ⌊x⌋. The floor keeps the cell and discards the fractional
  part, which locates the place within that cell. In binary, the fraction is a sequence of halvings, each digit one
  finer level below the indexed cell (exact for dyadic subdivisions). By indexing alone, the array keeps the levels
  across its indices but not this hierarchy within a cell. A reader has no floor. It uses the continuous address and
  keeps as much of the finer structure as its resolution supports, rather than discarding every finer level at once;
  how many levels it keeps is set by its resolution, not by the fraction (§8). One method an array can use for
  something like it is band-limited reconstruction, which spreads a value over every sample by weights that sum to
  one, with N setting the band. That method assumes a model of the signal; it is an analogy to the reader's coarser
  level, not the same mechanism.
- *One array per facing.* A circle has four facings, the quadrants, and can be stored as four arrays on one lattice.
  - Each array has its places at θ_k = (k + ½)·(π/2)/N, read as tan θ_k: the N evenly spaced quantiles of the
    half-Cauchy.
  - The circle stores one value everywhere, its radius. A shape stores others (§7.4).
  - The size is the one value no reading fixes (Proposition 8).
  - Within an array, its middle is the corner, and reading it backwards is the reciprocal:
    tan θ_k · tan θ_(N−1−k) = 1.
  - A closed curve stored as 4N samples over the full turn is these four arrays laid end to end.
  - A sphere is eight arrays, one per octant, each two-dimensional, uniform in azimuth and in height.
- *The reader reads the arrays; the writer joins them.*
  - A reading carries no sign, and composed turns repeat after a half turn (tangent addition). So from a standpoint, every
    facing is the same array, and a reader reads within one.
  - To join two arrays, their values must meet at the shared end in one unit. That needs each array's size, its extent
    in amounts.
  - The reader holds each array only up to its own factor, the size no reading fixes (Proposition 8), so it cannot tell
    whether two ends meet. The point in amounts needs the extent, as for the sphere in a cube (§9).
  - The writer knows the sizes, and which facing each array is, so it can join the four into the closed circle, or the
    eight into the sphere.
  - Since the places sit at midpoints, no array holds an end, and joined arrays never claim the same element.
- *Not knowing the size makes the corner and the horizon.*
  - Knowing an array's size, the writer has its end at an amount, the other party's whole V*. Its ruler is the number
    line, on which the point where the two parties are equal is computed (§10, the writer's map; §9).
  - Not knowing it, a reader whose sweep is a turn must draw the other party at its own H, and v = h becomes its split of near from far and
    the median of its readings, the corner (Propositions 3(e), 5(d)).
  - With no size, the array's far end is no amount, only a direction, [0 : 1], where the chart v/h runs out: the horizon
    (§4).
  - Both are the reader's because the size is missing; the writer, holding it, has neither.
- *The situations as arrays* (§3.1).
  - Situation 1 is a constant array of known length: every entry the radius, of length H. Its one value needs no
    storing, so the array is the equation h² + v² = 1.
  - Situation 2 is an ordinary array of known length, a breadth in amounts at every index, which the writer joins into
    the closed shape.
  - Situation 3 is the values without the length: an amount at each given index, known only up to the one common
    factor a₀, so the values are relative to one another, can be ranked and averaged, and cannot be sized.
  - Situation 4 is the index alone, laid before any value arrives and with no length: its places the Cauchy's
    quantiles, its middle the corner, its last place running to the horizon, K places for any N.
  - Situation 0 has no array: H, but no index and no relation to store.
  So the writer's arrays are 1 and 2, with the length known; the reader's are 3 and 4, the payload on the index and the
  index itself, with the length missing. That one number is what writing supplies.

**Laid on the sweeps: a worked example.** Take K = 8 places on the quarter turn. The inscribed sweep's reading of a
direction is s = v/h, and its share of the turn is g = (2/π)·arctan s, so the index is

  k = ⌊K·g⌋ = ⌊8·(2/π)·arctan(v/h)⌋,

with the horizon, v/h unbounded, kept in the last place. No length enters: the places' boundaries are tan(kπ/16),
0, 0.199, 0.414, 0.668, 1, 1.497, 2.414, 5.027 and the horizon, and their middles tan((k + ½)π/16), 0.099, 0.303, 0.535,
0.821, 1.219, 1.871, 3.297, 10.15, are the eight evenly spaced quantiles of the half-Cauchy.

| reading v/h | 0.1 | 0.5 | 1 | 2 | 3 | 10 | 1000 | horizon |
|---|---|---|---|---|---|---|---|---|
| share of the turn g | 0.064 | 0.295 | 0.500 | 0.705 | 0.795 | 0.937 | 0.999 | 1 |
| index k | 0 | 2 | 4 | 5 | 6 | 7 | 7 | 7 |

The four arrays lay on these places as follows.
- *The index alone* (situation 4). The table is the whole array: eight places and nothing stored. The corner is the
  boundary between places 3 and 4, found with no length, since K is even (for odd K one place is centred on it). The
  reciprocal reverses the order, a reading s and its reciprocal 1/s going to places k and 7 − k (at s = 2 and ½, places
  5 and 2). Scaling the world moves nothing: v and h scaled together by 10⁻³, 7 or 10⁶ leave s = 3 in place 6.
- *The values on the index* (situation 3). The central sweep meets the same point at the central angle φ = 2θ (Euclid
  III.20), and indexes it by ⌊K·φ/π⌋ over its half turn; that is the same k, place for place (2, 5 and 7 at s = ½, 2
  and 10). So one index serves both sweeps: the inscribed sweep's ratio and the central sweep's amount found there are
  stored at one place. The amounts are known up to one factor, so what is kept is ln of each amount less their mean.
- *A constant array* (situation 1). Every place holds the radius, of length H, 1, so nothing is stored: the value at place
  k is a function of k alone.
- *An array of known length* (situation 2). The writer places an amount x on [0, X] at ⌊N·x/X⌋, which needs X. With
  N = 8 and X = 100, the amounts 10, 50 and 99 go to places 0, 4 and 7. Read from home at a distance laid by H,
  ⌊8·(2/π)·arctan(x/H)⌋, they go to places 4, 6 and 7 with H = 10, and to 1, 4 and 5 with H = 50: H moves them, as a
  zoom, and X never enters. The count index needs the extent; the turn index needs only the zoom.

### 7.4 The shape is payload

The sweep opens a closed shape out, with zero in the middle of the opening and the two ends running toward the horizon
in each quadrant. Opening divides out size, so each place on the opened line is an address pointing back to a point of
the closed shape, which keeps its size. Laid uniformly by direction, every shape opens into the same fisheye and the
same Cauchy; the shape survives only in what arrives at each address, one breadth per direction, as Theorem 6(a)
requires. The addresses are the same for every shape laid uniformly by direction, and the shape is payload.

**The lay, not the shape.** Laying the same shapes another way shows where the Cauchy comes from. Read each shape from
its centre as v/h, and describe its opening by four numbers: the share of readings before the corner, their median, how
they cross zero (the share below s, divided by s, at s = 0.025) and how they cross toward the horizon (s times the share
above s, at s = 40). Laid by direction, every shape gives the circle's four numbers, since the reading is the direction
alone. Laid in equal steps along its own outline instead, a lay taken from the shape itself, each shape opens its own
way:

| shape | laid | before the corner | median | crossing zero | crossing toward the horizon |
|---|---|---|---|---|---|
| any shape | by direction | 0.500 | 1.000 | 0.637 | 0.637 |
| circle | along its outline | 0.500 | 1.000 | 0.637 | 0.637 |
| square | along its outline | 0.500 | 1.000 | 0.500 | 0.500 |
| diamond, h + v = 1 | along its outline | 0.500 | 1.000 | 0.976 | 0.976 |
| astroid | along its outline | 0.500 | 1.000 | 3.15 | 3.15 |
| ellipse, twice as tall as wide | along its outline | 0.373 | 1.479 | 0.413 | 0.826 |

Shapes unchanged when h and v are exchanged keep the corner at the middle, as the reciprocal requires, and none of them
has a mean, since each keeps a share of order 1/s or more beyond s (Theorem 6(e)). They differ only at the ends; the
astroid's cusps make its ends heavy, the square's flat sides make them light. The ellipse, which the exchange alters,
moves its corner as well. Over 73 single-outline shapes from a drawing library the pattern is the same, with ends from
0.27 for a gear to about 3.1 for the astroid. The test would have failed had any shape laid by direction departed from
the circle's numbers, or had a shape unchanged by the exchange moved its corner off the middle. The table and the 73 are illustrations of
results proved elsewhere, not their proof: that every shape laid by direction reads alike is Theorem 6(a), the shape
being payload, and that a lay unchanged by the exchange keeps its median at the corner is Theorem 6(e). The Cauchy is what a
uniform lay by direction gives, whatever the shape; a lay taken from the outline brings the shape into the distribution.
The Cauchy belongs to how the addresses are laid.

**Why the circle and the Cauchy go together.** The circle is the one shape whose two lays coincide: on a circle, equal
steps along the outline are equal steps of turn. So for the circle alone, a lay taken from the shape and a lay that
knows nothing of any shape are the same lay, and both give the Cauchy. Every other shape tells them apart. This is why
the Cauchy is usually met through the circle, as the tangent of an angle spread uniformly round it: it belongs to the
uniform turn, and the circle is the one shape in which the uniform turn and the shape cannot be told apart.

**A shape is a perturbation of the circle, and only a circle can be the base.** Write a shape seen from the reader as
r(θ) = exp(f(θ)), the unit circle at f = 0. Every such map moves each point along its own ray and never across it, so
the maps r ↦ λ(θ)·r, λ(θ) > 0, form a group that fixes every direction; laid by direction, the readings are the same
Cauchy for every shape. Laid along the outline, the law moves with the shape: for f = 0.3 cos 2θ + 0.1 cos(3θ + 0.4) the
share before the corner is 0.632, against the circle's 0.500, and for f = 0.25 cos 4θ, unchanged by the exchange, it
stays 0.500 while the ends move. Among outlines read from one pivot, only a circle is a base that carries nothing: an
outline reads uniformly by direction exactly when its length per unit of turn, √(r² + r′²), is constant, and r² + r′² =
q² has two kinds of solution, r = q, the circle centred on the one who sweeps, and r = q·sin(θ + θ₀), the circle through
it. These are the two pivots of §4, the centre and a point of the circle, and no other shape gives either. Which circle
depends on the sweep: the circle centred on the pivot for the central sweep, the circle through it for the inscribed;
with the pivot at home, these are the reader's unit circle and the Thales circle. The uniqueness is relative to the
construction, a uniform lay by direction from one pivot, not a claim that no other geometry can be drawn. Nor do two smooth outlines read alike along their length: if
r₁, r₂ > 0 have the same √(r² + r′²) at every direction, then where |r₁ − r₂| is greatest its derivative is zero, and
(r₁ − r₂)(r₁ + r₂) + (r₁′ − r₂′)(r₁′ + r₂′) = 0 leaves (r₁ − r₂)(r₁ + r₂) = 0 there, so r₁ = r₂ everywhere. The law laid
along a smooth outline fixes the outline, its size included once the length per turn is an amount; as a share, the
size a₀ stays unread. Smoothness is needed: three arcs of circles through the pivot, joined at corners, have length 1
per unit of turn throughout, as the unit circle has. We have not found this argument in print; it is elementary, and we give it as ours. Read as the
reader's ignorance (§2), a reader who does not know the shape needs a law that every radial map leaves unchanged, and
only a law on directions alone is one; the rescalings of κ are the radial maps with λ constant. So a reader can begin at
the unit circle and read the shape without knowing V*: in ln r = a₀ + f(θ), the unknown size is the constant term alone,
a₀ = ln κ, the one term no ratio of radii reads, and the uniform measure dκ/κ is the flat da₀. Every term of f is the
shape, read exactly from ratios of radii wherever the payload or another standpoint supplies them (from directions alone
none is read), and taking the terms in order of n is a level of detail, each truncation leaving every address where it
was.

The addresses with their payloads give the shape back, up to scale, exactly when the shape is star-shaped from the
standpoint, so that each direction meets the outline once. Otherwise some direction meets it more than once and the
parts behind are hidden: panes behind panes on one finger's line.

Two examples show the reach and the limit. An ellipse with semi-axes 2 and 1, read from its centre, meets each
direction θ once, at r(θ) = 2/√(cos²θ + 4·sin²θ). One value per address holds it completely, and doubling the ellipse
doubles every value and moves no address. A ring between radii 1 and 2, read from its centre, is not star-shaped from
there: every direction meets its inner edge and then its outer edge. One value per address keeps the inner edge, the
first thing met, and loses the outer one, which lies behind it on the same address. What the representation keeps is
the first meeting along each address; what it loses is everything behind that. Occlusion and contact need more than a value at each address
(that sight runs straight and stops at the first thing it meets), and nothing here is claimed for them.

### 7.5 Situated and unsituated

Held whole, as the writer holds it, the bar's uniform turn traces the circle h² + v² = 1, every point like every other:
no home, no horizon and no corner of any consequence. Swept from home and read as v/h, the same uniform turn gives the
Cauchy when counted and the fisheye when drawn. Home, the corner and the horizon appear because the reading is taken
from somewhere. Situated geometry is the arc, read as the Cauchy; unsituated geometry is the chord, with the circle
drawn on it whole. The chord needs no turn, and the circle is what a turn traces.

Proposition 5 assumes the measure on the turn is uniform, which is a choice of weight on the sweep. It is not a weight chosen
to produce the Cauchy: stepping the turn uniformly is what makes the circle uniform in the first place, so one
assumption, uniformity, lies behind both. The two are still distinct: the circle's symmetry under turns is one thing,
and counting a standpoint's directions in equal turns is another. Other weights symmetric under the reciprocal exist, such as
the line's share v/(v + h). By Proposition 2(b) each puts the corner at its middle, but none of them gives the Cauchy.

### 7.6 What being situated costs

Two things are missing from a situated reading, and they are easily confused. The breadths are missing from every
single reading: v/h cancels them, as it cancels the reach of whatever arrives. The total of the whole is missing because
the reader's readings have no end: the horizon is never reached, so no census can be taken. The Cauchy's missing mean
belongs to the first absence, not the second. It is not a census that more readings would complete: over both quadrants
the mean of n Cauchy readings is distributed exactly as a single reading, whatever n is, so averaging never settles.
The readings are addresses, and a mean asks them for sizes they do not carry. A situated reader keeps order and loses
sums, and the Cauchy is the extreme case: an order law with no sum.

**Order needs the readings together.** The median of the addresses, the corner, is laid with them, before anything
arrives (§3.1). The median of what arrives survives every change of it (Theorem 6), but it is had only where the
arrivals are held together, since a median compares every reading with every other: finding the exact median of n
arrivals taken one at a time needs storage that grows in proportion to n (Munro and Paterson 1980). To a stated accuracy two registers
suffice (Appendix A). It uses order only, as Theorem 6 says a median does. How a reader holds them is its own (§3.5).

### 7.7 Other addresses and payloads

The same split appears in familiar places.
- *The unit circle is an addressing scheme.* A system of any size can be laid onto it, and nothing is read out of it.
  It has no size of its own and no count of things.
- *The number line is laid on the sweep.* The sweep from zero to the horizon is the address space; the number line is
  what is addressed, with its 0 at the sweep's zero, 1 at the corner and its unbounded end toward the horizon, the two
  sides of 1 exchanged by the reciprocal.
- *Division makes addresses.* Dividing by H removes the scale. What is left, v/h, is a place on the sweep, the same at
  every scale, and the world returns what is there. Division loses nothing but the scale, which no address holds.
- *Relays.* An address that meets a mirror goes on: a live relay, holding nothing of its own. An address that meets a
  painting of exactly what the mirror showed stops there: a stored relay. From the painter's standpoint the two agree
  address for address, and they part as soon as the reader moves.
- *Payloads on demand.* Because the range of addresses exists before anything arrives, a payload need not exist until
  its address is read. It can be a function of the address, evaluated on demand, as in a procedurally generated
  landscape. It can also be another reader, which is the centre of its own addresses and a payload in someone else's.
  Reader and world are roles in a relation, not kinds of thing.
- *The end of the track has an address.* Stand between straight rails and read each tie as half the gauge over its
  distance. With ties 0.6 apart and half the gauge 0.7, every tie past the first reads below 1, so infinitely many ties
  fit between that pair's corner and zero, and the end of the track, however far, has an address, zero, that no tie
  reaches.

### 7.8 What is known

The Cauchy as the image of a uniform angle (the gnomonic projection of uniform measure on a hemisphere), its invariance
under Möbius maps and its missing mean are classical (Knight 1976; McCullagh 1996; Pitman and Williams 1967; Cuadras
2002; Stigler 1974), as are the facts that the mean of n Cauchy variates is again Cauchy and that order statistics
follow every increasing map; those facts underlie parts (b) and (d). The other parts of Theorem 6 are in print too.
- *Part (a).* The ratio of two components of any spherically symmetric vector is Cauchy, whatever its radial law, since
  its direction is uniform and independent of its length (Jones 1999). In more dimensions the tangents of the polar
  angle are multivariate Cauchy (Cacoullos 2014), the law of Proposition 5(e). Under elliptical symmetry the ratio is a
  Cauchy of another scale (Jones 2008a), the forward half of Proposition 5(d). This is the reach cancelling.
- *Parts (b) and (c).* That the median keeps its place under every order-preserving transformation, and the mean only
  under linear ones, is Stevens's classification of scales of measurement (1946).
- *Part (e).* Positive variables with the same law as their reciprocal were characterized by Seshadri (1965) and are
  called log-symmetric (Jones 2008b); a ratio X/Y has that property exactly when X and Y are, or can be chosen to be,
  exchangeable (Cacoullos and Papadatos 2013).
- *The textbook case* is the lighthouse (Gull 1988; Sivia and Skilling 2006): flashes sent at uniformly spread angles
  land along the shore as a Cauchy, and the lamp's position is found from the median or the likelihood, never the mean.
  There the lamp turns, in time, and the shore records its addresses laid on a line; our claim is that this law
  belongs to the uniform turn, the lamp's or a standpoint's, and not to what the turn meets. That half the landings fall within
  the lamp's distance of its foot only when shore and sea are drawn at one length is Proposition 5(f), which is
  elementary.
- *The same law where no standpoint's turn lays it.* A spectral line or a resonance is a Lorentzian because of a pole a half-width
  off the real line, |1/(x − x₀ + iγ)|², from an exponential decay or a damped response (Weisskopf and Wigner 1930;
  Breit and Wigner 1936). Crossed uniformly in frequency or energy, the pole's phase turns through half a turn, not
  uniformly, standing 45° from its middle at the half-width; read the other way, the Lorentzian is the line laid by a
  uniform turn of that phase, the profile of §7.2, with the line's strength the amount. The turn there is the
  response's, not a standpoint's. A sum of terms whose densities fall off like 1/x² reaches the same law as a stable limit
  of index 1, with no angle in the terms (Lévy 1925); the turn is in the limit, which is where a planar Brownian motion
  started above the line first lands on it, a uniform turn from its start (Spitzer 1958). Our claim is only that where a standpoint's directions are counted
  uniformly by turn, their law is its addresses, whatever else may give the same shape.
- *Special relativity's sky*, the one physics example, is set out in §11.
- *Proposition 5(g)* is classical cartography. A chart's two scales at a place are the axes of Tissot's indicatrix
  (Tissot 1881), which is a circle exactly where the chart keeps angles; Mercator's map is the cylindrical chart that
  does so everywhere; and no chart keeps both angles and areas (Euler 1777; Gauss 1828). What is ours is the reading: the
  ratio of the two scales is the drawing V = cH, and the corner between north and east is the corner of §4.
- *The nearest prior reading* is Frank and Smith's (2010; Frank 2014): the scale on which an observer measures defines
  the most likely distribution of what it observes, and a scale linear for small magnitudes and logarithmic for large
  ones, as the reader's two address spaces are (§6), gives Student's t, of which the Cauchy is the case of one degree of
  freedom. Their route is maximum entropy under a constraint set by the scale; ours is the cancellation of the reach,
  which also separates what order keeps from what sums lose.

What is new here is the reading: from what standpoint, knowing what, the Cauchy is had, and that what it receives is its own
addresses rather than anything in the world. The split itself is carried, unnamed, in the equations of several fields.
In potential theory the value at a point is the boundary's values averaged by where a Brownian path started there first
meets the boundary, u(x) = ∫ f dμ_x, the harmonic measure μ_x fixed by the point and the region alone, the half-plane's
Cauchy from i, and the boundary data f free (Kakutani 1944; Doyle and Snell 1984). In spectroscopy a line is its
strength times a profile of unit area. In the lighthouse only where each flash lands is recorded. Each separates a
measure on points from what is found at them; none states that the Cauchy is always the first and never the second. We
did not find that statement, that an address is not a payload, made in print.

## 8. Level of detail and the choice of H

**The count is the level of detail.** The forms of the two address spaces are fixed; their counts are not. Laying the
near field in proportion means dividing H into some number of parts, and the geometry neither knows nor uses that
number. Past the corner, what is fixed is that each doubling gets the same count, not what the count is. In both spaces
the count is the *level of detail*: the geometry gives the forms, and the level of detail gives the count.

**Size sets the level.** A thing that spans n of the reader's addresses is resolved to about log₂ n levels, one fewer
each time the number of addresses it spans halves; when it spans a single address it is a point. Nothing is requested:
the span sets the level. How many addresses a thing spans depends on amounts, which the geometry does not supply.

**A resolution, not cells.** The count is a resolution; it does not make cells.
- A thing between two addresses is not rounded to either. It is held at the coarser level.
- The level is a continuous number, and its fractional part says how far the finest detail held has faded.
- The Cauchy carries such a level in its own height. Seen from height γ, a pattern's mode of frequency k is kept as
  e^{−kγ} (the Poisson kernel), and each mode fades, faster the finer it is, with none cut off.
- The address itself is continuous; the reader's level of detail decides how much of its finer structure remains
  distinguishable.
- Rounding to cells is a device of storage, not of reading.

**What the floor discards.** An array finds a cell by the floor: x = ⌊x⌋ + {x}, a key and a remainder, and it keeps the
key. The remainder looks like a leftover, the part that did not fit, and it is usually thrown away as such. It is not a
leftover, and it is not payload. Nothing stored at the cell is lost: the cell keeps its value. What is lost is where in
the cell the place is, and that is address. Written in binary, the remainder is 0.b₁b₂b₃…, and each digit says which half
of the cell before it the place lies in: b₁ the half of the cell, b₂ the half of that half, and so on. The digits are the
finer levels of the address, one level a digit, without end. So the floor does not round one number. It takes an address
that runs through every level and keeps it at one, discarding all the finer ones in a single step. The floor is not
lossless, and flooring is not wrong: where only the cell's value is wanted, dropping where in the cell is exactly right;
where the place within the cell matters, what was dropped was address, not payload.

*The remainder is a second coordinate.* The levels it holds are not a list kept beside the address; they are the
address's other dimension. Give the dyadic cell [kw, (k + 1)w), w = 2^(−j), the point z = m + iγ of the upper half-plane,
with m its middle and γ = w/2 its half-width. A place is then two numbers: where it is along the line, m, and how far down
it is held, γ. The floor keeps m at one height and forgets that the height was a coordinate at all. The plane the two
numbers make has a geometry of its own, and it is a familiar one.
- *Every level is the next.* The map z ↦ 2z is an isometry of the half-plane (its metric is ds² = (dx² + dy²)/y²), and it
  carries each level of cells onto the next. Each binary digit is one step down, and every step is alike: a step of ln 2
  in height.
- *Every cell has the same room.* The tile [kw, (k + 1)w] × [w/2, w] has hyperbolic area ∫∫ dx·dy/y² = w·(2/w − 1/w) = 1,
  at every level. A cell a million levels down has exactly the room of the first. The tiles are Böröczky's binary tiling
  (Böröczky 1974).
- *Distances are fixed by the levels.* With cosh d = 1 + |z₁ − z₂|²/(2γ₁γ₂), a parent and either child are arcosh(3/2)
  apart, two siblings arcosh 3, and two cells n apart on one level arcosh(1 + 2n²), at every level and every place.
- *A point of this plane is a Cauchy law.* Each z = m + iγ is the Cauchy C(m, γ), and from its cell's point the Cauchy
  puts exactly half its weight in the cell: (1/π)(arctan 1 − arctan(−1)) = ½. The cell is its interquartile range. So the
  plane the floor's remainder lives in is the space of the address law's own parameters, the standpoint's foot and height
  of §7.2, and a dyadic cell is one Cauchy, read from its own point.

*A tree keeps the levels and loses the plane.* The usual way to keep the finer levels is a tree: a quadtree, an image
pyramid, mipmaps, each cell joined to its parent and its children. A tree keeps the depth but measures it wrongly. The two
cells either side of the middle of level j, k = 2^(j−1) − 1 and 2^(j−1), touch, and in the plane they are arcosh 3 apart
at every level; in the tree their nearest common ancestor is the root, so they are 2j steps apart, 60 at level 30. Add
the sideways neighbours, each cell joined to the cells beside it on its level, and the graph measures the plane: its step
count g between any two cells is within a bounded amount of the hyperbolic distance d over ln 2 (for all 523,776 pairs at
level 10, |d − g·ln 2| ≤ 2.19), the shortest way between two cells is always up, across and down, and d/g tends to ln 2.
An array indexed by (level, index), with links across as well as up and down, is a discrete copy of the half-plane; a
tree is not.

*Two ways to lose depth.* Every reader with a finite resolution loses the finer levels; the floor and a reader at a height
lose them differently.
- *The floor.* A cell average multiplies a wave e^{ikx} by |sin(kw/2)/(kw/2)|. It keeps every level coarser than the cell
  whole and none finer: a cut at one level, with zeros and side lobes past it, so finer detail, once each cell is kept
  as one value, can come back as coarser (aliasing).
- *A reader at height γ.* The Cauchy from z multiplies the same wave by e^{−kγ}: smooth, never zero, and composing as
  heights add (from γ₁ then γ₂ is from γ₁ + γ₂). No γ brings the two within 0.22 of each other, so keeping binary digits
  is not reading from a height. For a step detail, a reader at its own cell's point keeps the shares below, by the level
  read against its own (negative is coarser):

  | level read, against the reader's own | −7 | −6 | −5 | −4 | −3 | −2 | −1 | 0 | +1 | +2 |
  |---|---|---|---|---|---|---|---|---|---|---|
  | share of the step kept | 0.927 | 0.874 | 0.789 | 0.660 | 0.482 | 0.279 | 0.110 | 0.027 | 0.0044 | 0.0006 |

  It keeps half of the step 3.09 levels coarser than its own cell and takes 5.5 levels to go from 90% kept to 10%: one
  soft cut over the levels, the same at every depth, where the floor at the same level keeps every coarser level whole
  and none of its own.

*Who sets the depth.* The floor sets one depth for everything, the cell's, chosen by the store before anything is read.
The geometry sets each thing's level by its span, as above: a thing spanning n addresses is held to about log₂ n levels,
and a thing between two addresses at the coarser one. So the floor imposes a level of detail; the reader reads one off
what it meets. Where the floor is taken of an amount, ⌊x/w⌋, the cell width w is an amount too, and scaling the world by
k moves the key unless w is scaled with it: by the test of §9 the key is then a writing, its grain carried in. A floor
taken of a share of the turn carries no amount, and scaling moves no key.

*What it means.* Three things follow, each from the pieces above.
- The address is continuous and hierarchical at once. The levels of detail are not a structure kept beside the address,
  a pyramid built and stored; they are the address's second coordinate, the height, and they come with it. Pyramids,
  mipmaps and quadtrees can each be read as a way of keeping some of that coordinate after the floor has dropped it.
- The hierarchy is not a convenience of storage but a geometry, the hyperbolic plane: every level alike, every cell of
  one room, distances fixed by the levels. That plane is the one the Cauchy's parameters live in, so the reader's law and
  the store's hierarchy share it, and differ only as filters on it.
- The separation of address and payload reaches down into the depth. The floor discards address, not payload; and from a
  height the window 2γ is the address's, fixed before anything arrives, while what survives inside it is the payload's
  (below).

Not shown: that the world stores anything this way; that a reader's level of detail is a dyadic depth rather than a
continuous height; anything about physics. The mathematics is classical (Böröczky, the Poisson kernel, the sinc of a box);
the reading is ours.

**What the height fixes, and what it does not.** Seen from a cell's point m + iγ:
- The height fixes an address window, 2γ wide, the cell itself, before anything arrives, and no payload enters it. Only
  the line changes it. On a closed line of length 1 the window is (2/π)·arctan(tanh πγ), close to 2γ for a low reader and
  half the line for a high one.
- What is kept of a payload's variation depends on the payload. For a detail a cell of width w′ wide, the share kept
  depends only on u = γ/w′, by the isometries above. So the reader's loss of detail is one soft cut over the levels, the
  same at every depth. Its form is the detail's: near the reader a step loses (12/π)·u·ln(1/u), a smooth detail an amount
  in proportion to u, and far off the detail's vanishing moments set how fast it falls.
- Whether two payloads read as two depends on the kernel and on the payloads. Two equal Cauchy profiles of height γ
  show two maxima only when more than 2γ/√3 apart, and two equal Gaussians of width σ only when more than 2σ apart.
  Cusped profiles show two at any separation, and unequal amplitudes raise every threshold.

So the height alone fixes where the reader's window falls, and what survives inside it is the payload's: the division
of Theorem 6, at the level of detail.

**From far off, a thing is its total at its centroid.** Take payloads w_i at points r_i about a centre, each at
distance q_i from it, read from a standpoint at distance r with every q_i < r. The reciprocal of the distance to each
expands in the reading q_i/r: 1/|r − r_i| = Σ_l (q_i^l / r^(l+1)) P_l(cos γ_i), with P_l the Legendre polynomials and
γ_i the angle at the centre.
- Weighted by the w_i and taken about their centroid, the first-order terms cancel. From far off the payloads read as
  their total at their centroid, and each finer order of their arrangement arrives smaller by one more power of the
  reading.
- For a single payload the series converges outside the sphere of radius q and fails inside it. On that sphere, along
  the line to the payload, every term is the same and none may be dropped: the corner of the pair (q, r).
- Inversion in that sphere, r ↦ q²/r with the factor q/r, exchanges the outer series and the inner one term by term
  (Kelvin's inversion; Kellogg 1929). It is the reciprocal of §4, in space.

This is level of detail by distance, with the corner as its seam.

**H is a zoom, not an escape.** H is not a measured size: it is the value the reader chooses to start the system
(P1), and nothing in the geometry fixes it. Any H gives the same circle and corner, so a reader could choose a very large H and hold
everything it will ever look at in the near field, at true scale, with no logarithm. The cost is the level of detail.
With finitely many addresses spread uniformly over a very large H, everything at the reader's own scale falls within the
first address and becomes a point. A small H holds the small at true scale and the large logarithmically; a large H
holds the large and loses the small. There is always something smaller than any H's first address, as there is always
something larger past any corner, so no single H holds every scale at true scale. The best choice is to set H to the
scale of the thing being read, which places that thing at the corner; focusing an eye or zooming a lens does this.
(For a thing at x read from a standpoint at distance d, the kernel d/(x² + d²) is largest when d = x, that is, at
v = h.) The
same idea appears in the hyperbolic browser, which draws only nodes at least a pixel across (Lamping, Rao and Pirolli
1995), in mipmaps, which halve an image at each level (Williams 1983), and in web-map tiles, whose key gains one digit
per level of detail (Microsoft, Bing Maps Tile System).

**What a larger H gives and takes.** Count the room the reader gives one object, the stretch of amounts from d to
d + Δ, with n addresses across the near field: n times the stretch of lay the object covers. Inside the corner
(d + Δ ≤ H) it spans nΔ/H addresses. A larger H moves the corner away and gives the proportional field more room, but
the count is fixed, so every object inside the corner gets fewer addresses: one level of detail fewer for each
doubling of H. Past the corner (d ≥ H) the two lays of §6 part. On the logarithmic lay the object spans
n·ln(1 + Δ/d), whatever H is: its detail is set by where it is, and a larger H only moves the held levels outward,
bringing farther things in. On the in-place lay it spans n·H·(1/d − 1/(d + Δ)) = nΔH/(d(d + Δ)), which grows with H,
so there a larger H gives the far more detail as well. A small H reads the near finely; a large H reaches the far. On
the in-place lay an object gets the most room when H = √(d(d + Δ)), the corner of its own two ends, where it spans
2n·(1 − √(d/(d + Δ))), close to nΔ/d for a thin object; on the logarithmic lay it gets as much as it can have for
every H up to d. Placed on the quarter turn at arctan(x/H), two amounts are set furthest apart, at the angle
arcsin((r − 1)/(r + 1)) for a ratio r, when H is their geometric mean. The best H is the corner of what is read, as
the best estimate of a size is the corner of what is known (Proposition 13).

**A fixed count, aimed by H.** Call the reader's whole count of addresses K: its fixed capacity to observe, its own,
the same whatever it looks at. The turn's addresses are continuous; a fixed K is a model of a reader's finite
capacity added to them, not something the turn supplies, and what follows holds for whatever K a reader has. K comes before H. Choosing H does not change K; it splits it in two. Lay the K addresses
of a uniform turn of the reader's one length along distance. Their boundaries fall at d_k = H·tan(kπ/2K), k = 1, …, K − 1,
the quantiles of the Cauchy with its scale at H.
- Since tan(π/4) = 1, the middle boundary is d = H whatever H is. Half the addresses lie inside the corner and half past
  it, at every H (Proposition 5(d)). H moves the split; it never changes the count.
- A small H gives the near half a short stretch of amounts, each address a fine one, the first tan(π/2K)·H ≈ πH/2K wide.
  A large H gives the same half a long stretch, each address coarser, and carries the far half farther out.
- The world's own count enters nowhere. Doubling or thinning what arrives moves no address (Theorem 6(a)), so a world of
  N things, of 2N, or of infinitely many is held at the same K addresses, each holding its share.
- Holding is not telling apart. Things that share an address arrive there as one payload, their sum or the nearest's
  paint, and only a finer count or another standpoint separates them: a finite K is a level of detail, not a lossless
  store.

The same points, and their parity at the corner, are known in numerical analysis and in quantization (Appendix A).

So a reader's K addresses fall on any world, and its choice of H places the finest of them anywhere along distance;
it never has more than K at a time. The count is the level of detail, and H is the zoom. (Elsewhere in this
section n counts the addresses across the near field on a lay, a different measure; on the turn's own addresses it is
K/2.)

**One K, in direction and in distance.** The same count enters twice, and H enters the two differently.
- In direction, the K addresses are the turn's equal angles, split K/2 and K/2 at the corner by the reader's one length. The
  value of H appears in none of these readings, so no choice of H moves them (Theorem 6(a)): the split is fixed by the
  geometry.
- In distance, the same K quantiles fall at H·tan(kπ/2K), and there the value of H is the zoom: K/2 in proportion up
  to H, at an absolute grain, the first about πH/2K wide, and K/2 past it at a relative grain, out to the horizon.
  Distance is an amount, and the paint carries none (§2); this lay is had once distances are, from a second standpoint
  in H or from an amount carried in (§9).
- On the in-place lay the far boundaries are the near ones reflected about H, since 2 − cot θ_k = 2 − tan(π/2 − θ_k).
  So the K addresses fill a ruler 2H long, K/2 on each side of H, with the horizon at its end. On the logarithmic lay
  the far half has no end in length, only in count.
- A direction's K addresses and a distance's K together make a polar grid of K × K cells. Every thing falls in exactly one, whatever the world's count N. H moves only the radial split.

The reader interacts with K. The writer, which states every distance in amounts, interacts with N: it places each
thing at its amount on its number line. The Cauchy is what keeps the two apart. Its K quantiles are fixed by the turn alone, at
H·tan(kπ/2K), with no reference to how many things there are or how far they reach. Its last address runs to the
horizon, so a finite K covers an unbounded world, and whatever lies past every other address lands in that tail. N
then enters only as the share each address holds, which is payload (Theorem 6(a)).

**The corner follows the focus.** Nothing in the geometry fixes where the reader puts its corner; H is its own choice.
On the turn's addresses a cell's width relative to its distance is (π/2K)(s + 1/s), least at s = 1, so the finest
relative grain is at the corner, and a reader should put the corner on what it is looking at. Near and far then mean
nearer than and farther than that, and the two are held alike, since the next look may fall on either: the reader does
not know on which side of the corner the next thing will be, and the exchange (§2) favours neither (Corollary 6.1
below). The rest of the
field is not lost. Every direction is still held, coarser away from the corner, which is enough to show that something
is there and where to look next; moving the corner there is a new zero (§2). So the corner's roles are the ones a
focus wants: the median of the addresses, half on either side (Proposition 5(d)); their finest relative grain; and the
reciprocal's fixed point (Proposition 1), the one reading the exchange leaves where it is. In three dimensions the same
holds at the triple corner [1 : 1 : 1], down which the wedge is seen from home, every pair's corner a median through it
(Proposition 5(e)). This is what a reader should do with its corner, not a claim about what any eye does.
- *Two corners, both free.* Turning the head carries the corner in direction to what is looked at, which is then read
  at the finest grain, with no distance (a turn in place gives no parallax, §11). Designating it reads it on the one length H, which
  puts it at the corner of distance too: mountain equals thumb, as a writer would say of the drawing (§10).
- *How far it is lies outside every reading.* Whether a range of hills is a day's walk off or a month's is its size
  against H (Proposition 8), needed only roughly, in levels, and carried in: a baseline, a known kind, the horizon.
  No field holds it, near or far.
- *What the fields cost.* Ask for cells no wider than δ across an extent F about the focus, and past it for cells
  that each place a thing within a factor ρ. The fewest addresses that do it are ⌈F/δ⌉ cells of one width across F and
  ⌈log_ρ(X/F)⌉ of ratio ρ past it, X the field's extent: proportion on the focus, levels past its edge, the corner at
  the edge. The field then costs about log_ρ(X/F) addresses, six at X/F = 64 and ρ = 2, whatever K is, and every other
  address goes to the focus. The reader's lay of Proposition 4, proportion and then levels, is the case in which the
  field's first cell matches the focus's grain. The turn, which gives the fields half of K, gives them more than this
  least.
- *Where the levels lie.* Laid on the angle from the gaze, the field's extent X is fixed by the geometry and needs no
  amount. Laid on distance it needs the distances. The picture itself is the turn, its far field in proportion to the
  reciprocal of distance (§6, "What Mercator's map is, and what it is not"); levels in distance belong to distance
  laid by a count of addresses.

**Corollary 6.1 (the corner is the best focus).** Let the reader lay the turn's K addresses with its corner at s = 1.
(a) *Grain.* A cell's width relative to its place is (π/2K)(s + 1/s), least at s = 1 and only there; in K discrete cells
the two beside the corner are the finest. More generally, any cost f with f(s) = f(1/s) and convex in ln s is least at
the corner.
(b) *Symmetry.* A choice of focus that does not depend on which unit relation a reading was divided by, v/h or h/v, is
unchanged by the reciprocal, and the reciprocal's only fixed point is s = 1.
(c) *Travel to the next look.* Let the place X of the next thing to be looked at follow a law, and measure the travel
from a focus c on any increasing ruler g: the angle, the levels ln s, the in-place lay. Wherever the expected travel
E|g(X) − g(c)| is finite it is least at the median of X, the same c on every ruler. If the law is reciprocal-symmetric,
which is all the reader's not knowing on which side the next thing lies allows, that median is the corner.
(d) *A lopsided law moves it.* If the next look is more likely on one side, the best focus moves to that law's median,
off the corner and toward the likelier side, still the same on every ruler.

*Proof.* (a) At d = H·tan θ, d(ln d)/dθ = sec²θ/tan θ = s + 1/s, and the addresses are π/2K apart in θ; s + 1/s ≥ 2,
with equality only at 1. A function of ξ = ln s that is even and convex is least at ξ = 0; evenness alone is not enough
(an even cost such as (ξ² − 1)² is least at ξ = ±1). (b) is Proposition 1. (c) The expected distance E|Y − c| of a law
Y with a finite first moment is least at Y's median, a classical fact; with Y = g(X) for increasing g, the median of
g(X) is g(median X) (Theorem 6(b)). On a ruler where the expected travel is infinite, as on v/h itself under the turn's
law, the difference E(|X − c| − |X − 1|) is finite and is least at the same point. A reciprocal-symmetric law has its
median at the corner (Theorem 6(e)). (d) is (c) with the median of the lopsided law. ∎

Under the uniform turn with a weight 1 + a·cos 2θ (a > 0 favouring the near side), the best focus is tan θ_m, where
θ_m + (a/2)·sin 2θ_m = π/4: 0.821 at a = 0.2 and 0.627 at a = 0.5, a quarter of a level and two thirds of a level
nearer than the corner. The corollary says where a focus should go and why; it does not say that any reader puts it
there, and (c) rests on a premise, that the reader has no reason to expect the next look on one side rather than the
other.

**Other ways to squeeze the line.** The three paths of §12.2 (question 2) each squeeze the reader's line into K
addresses, each swept uniformly along its own length and read as the signed reading s = v/h:

| path, swept uniformly | law of s | where the last of K addresses begins | swept again from a new zero (a turn of 30°) | two readings added |
|---|---|---|---|---|
| the circle (a turn) | 1/(π(1 + s²)), the Cauchy | cot(π/2K)·H ≈ 0.64·K·H | the same law | a Cauchy, scale 2 |
| the line, \|h\| + \|v\| = 1 | ½·(1 + \|s\|)⁻² | (K − 1)·H | 0.044 from its own family | 0.022 from it |
| the square's edges | ¼ up to \|s\| = 1, then 1/(4s²) | (K/2)·H | 0.047 from it | 0.062 from it |

The distances are the least, over location and scale, of the largest gap between distribution functions (the fourth
column) and between characteristic functions (the fifth).
- All three are unchanged by the reciprocal, so H is their median and K/2 addresses lie on each side of it. Each has a
  tail c/s past s, with c = 2/π, 1 and ½, so the last address begins near c·K·H and the unbounded rest of the line goes
  to the horizon. All three keep K apart from N.
- They part when swept again. A turn about the standpoint carries the Cauchy onto itself, and every turn and zoom
  carries it onto a Cauchy (§7.2; McCullagh 1996). The others leave their own families: each has kinks where its path
  has corners (the line's law at s = 0, the square's at s = ±1), and a turn moves those kinks to places no member of
  the family has them.
- They part when recombined. Two independent Cauchy readings add to a Cauchy, the stable law of index 1 (Lévy 1925),
  and neither of the other sums stays in its family. Added many times, the line's and the square's readings, scaled by
  their count, tend to a Cauchy too, of scale π/2 and π/4: their tails put them in its domain of attraction.

So every fair squeeze with such a tail keeps K apart from N, and recombining them tends to the Cauchy. Only the turn's
squeeze can be swept again or recombined without changing its shape.

**More points, fewer told apart.** Seen side-on, N points spaced uniformly around a circle are read across the view to
a resolution ε, relative to the circle's radius. Neighbours at
angle θ from the middle of the view are about (2π/N)·cos θ apart, so the reader separates those with cos θ ≥ εN/2π,
which is R(N) = (N/π)·arccos(εN/2π) of them. This peaks at about 1.12/ε points, where εN/2π ≈ 0.65, and falls to
none at N = 2π/ε: past the peak, more points mean fewer told apart. The addresses never overflow; the resolution does.

## 9. What a blueprint adds

**Ratios suffice.** Everything a reader does from where it stands is done in ratios. Every reading is a ratio, and none
contains a unit (Proposition 8(a)); the addresses, their law and the corner are given before anything arrives (§2, §4,
Proposition 5, Theorem 6(a)); near and far are laid by their count (§6), and the level of detail with them (§8); order
and the median survive every change of payload (Theorem 6(b), (c), (e)); more standpoints bring back the figure up to
its size (Proposition 11), and one step taken places every thing in the reader's own H (§10, step 6); a hierarchy of
any depth is held in ratios read one level up ("Units within units", §11), an error is found by closing a loop, with no
amount ("Closing a loop", §11), and two readers that see one thing in common are aligned by it (Proposition 7). All of
it is in the reader's own unit, H, a value it chose; none of it needs a breadth from outside. A reader that builds, places,
compares, orders and checks from where it stands needs nothing more than its ratios.

**What a blueprint adds.** A blueprint is the writer's statement of a thing in amounts: every length at once, to one
scale, from no standpoint (§1, §3.4). It gives seven things the ratios do not, and for each a result here shows that no
reading can supply it.

1. *The size.* How many of the reader's H the other is, V*/H: one number, carried by no reading (Proposition 8; §3.8).
2. *Meeting out of view.* Two systems that never see each other fit only through an amount agreed beforehand, a unit
   ("What a unit is", below); seen together, one ratio read between them suffices (Proposition 7). Parts made apart and
   joined later are this case.
3. *Sums of amounts.* A total, a mean or a budget adds amounts. The readings can be ordered and not added: they have a
   median and no mean (Theorem 6(b), (c); §7.6).
4. *The join.* Both hemispheres, every facing, the back and the inside, held at once; a reader holds one facing at a
   time and no reading carries a sign (§3.7; §7.3).
5. *Before the thing.* A blueprint can state what does not yet exist, and be built to; a reader reads what arrives
   (Proposition 9). To put a thing at a stated place is to write ("To move the furniture is to write", §11).
6. *Completeness, stated.* A reader can recover a thing exactly and still not know that it has all of it ("Recovered,
   not written", §11); a blueprint states the whole by construction.
7. *A far field kept in proportion.* A reader lays amounts in proportion only up to its corner, at its own H, and in
   levels past it (§6). Two readers with different H therefore lay the amounts between their two corners differently,
   one in proportion and the other in levels, and nothing in either reading says where the other's near field ends. The
   number line has no corner (Proposition 14): every amount, however far past any reader's H, is laid in proportion,
   so nothing about the extent of a near field has to be agreed. It is the common far field none of the readers' own
   lays has ("The number line is a shared unit, and the writer's ruler", below), and it is what lets amounts pass
   between readers whose corners do not coincide.

None of the seven is needed to build, place, compare, order or check from a standpoint. Each becomes needed when parts
made apart must meet, when amounts must be added or compared across readers whose near fields differ, or when the whole
must be stated before it exists, and those are the
needs of an intricate system of many parts. So the blueprint is a capability added to the ratios, not a condition of
them: a reader is not a writer short of an amount, and a writer is a reader that has carried one in. This is a statement
about what the mathematics makes possible, not about how any builder works. The rest of this section sets out what the
amount is and what it costs.

**Geometry first, then values.** Once the geometry is defined, a shape and one H (§5), physics assigns the values of
its placeholders, and the geometry is agnostic to that step. The values enter as multipliers on the amounts: V*/H on
each party's, and one more on all of them together when H itself is given a value in an agreed unit. They never redraw
the circle, since the reader's one length is what makes the turn (Proposition 3(e)). So no value assigned changes
the shape, the corner, the levels or any address. What the values decide is where things land among the addresses:
which fall in the near field and which past the corner, the zoom of §8.

**The amounts' error.** With H taken as 1 the amounts equal the unit relations numerically, which is why the two are so easily
confused. Where the true V* differs from H, every amount is off by V*/H, by the same factor on both sides of the corner: the
reader has read the mountain as one thumb, and it is V*/H thumbs. The addresses are exact; the amounts are not. Within
one observation a reader cannot tell a mountain of a hundred thumbs from one of 10¹⁶. Amounts
can come only from outside the geometry, across observations, from something whose amount is already known. That is
physics, and this paper does not treat it.

**Proposition 7 (a shared fact buys one factor).** Two readers share one closed polygon. Reader A records its part as
edges, each an exact direction and a length counted in its own unit H_A; reader B records the rest in its own unit H_B.
Neither knows the other's unit. Let S_A and S_B be the vector sums of each reader's counted edges, and suppose neither
part closes by itself. Then H_B/H_A = |S_A|/|S_B|, and nothing more about the units can be recovered.

*Proof.* Closure gives H_A·S_A + H_B·S_B = 0, so S_A and S_B are antiparallel and H_B/H_A = |S_A|/|S_B|. Scaling both
units together leaves every count unchanged, so their common scale cannot be recovered. ∎

Between two private rulers, a shared fact buys exactly the one factor that crosses.

**Proposition 8 (scale cannot be read).** Let a reader's observations be any collection of readings, each a ratio of
two amounts in the scene: sizes, distances, the separation between two of its standpoints. Then:

(a) multiplying every amount in the scene by one factor λ > 0 leaves every observation unchanged, so no collection of
such observations, from any number of standpoints, fixes the scale;

(b) if one amount L₀ is supplied from outside the readings, every amount that the readings link to L₀ is fixed.

*Proof.* (a) Each reading is a ratio a/b of amounts, and (λa)/(λb) = a/b. (b) If a reading links an amount a to L₀,
directly as a/L₀ or through a chain of readings whose ratios multiply to a/L₀, then a = L₀ times that product; and λ = 1
is the only factor that leaves L₀ fixed. ∎

This is the exact form of §3.4's "only two". In physics it is the ground of dimensional analysis, in which only
dimensionless ratios of amounts enter a law (Buckingham 1914). The worked example of §10 is (b) in use: the baseline is
a walk of one known H, and it fixes the mountain's distance and width.

**A sphere in a cube.** Put a sphere, free to turn, at the centre of a cube of half-extent e. From the centre each
point u of the sphere goes along its ray to one point of the cube's surface, u·e/‖u‖_∞, on the face of u's largest
component; every point of the surface is reached once, at every e and after any turn of the sphere, since the ray from
the centre through a surface point meets the sphere once. Sphere and cube here are the drawings of every octant
together; one wedge of the sphere lands on the three faces that meet at one corner of the cube, the cut "largest = 1" of
§2, scaled by e. Every point inside the cube but its centre is t times its surface point for exactly one t in (0, 1], a
unit relation: the cube's interior is held in proportion. So the pair (u, t) addresses every point of the cube, and it
is the same pair at every extent. The point itself, in amounts, is e times it. A reader that holds the addresses and not
e has the cube up to scale, as Proposition 8(a) says it must; it draws the cube at its own one length, the circle
again (V = H, a writer would say), right as addresses and off as amounts by the true e/H. Each face is the plane of the readings against one
denominator, so a sphere swept uniformly lays the Cauchy of Proposition 5(e) on it: a face's middle quarter by area
takes 38% of the face's directions, and its centre is 3^(3/2) ≈ 5.2 times as dense as its corners.

**What reaches a standpoint.** Proposition 8 speaks of every reading at once. Read over time from one standpoint, or at
once from several, it has four sharper forms. Each is classical: ratio invariance, division, triangulation and the
moments of a blur. What is ours is their placement, as what the paint at a standpoint gives.

**Proposition 9 (one stream is one relation).** A reader at one standpoint receives readings x(t) = a(t)/b(t) of a pair
of amounts. For any positive function λ(t), the pair λ(t)·a(t), λ(t)·b(t) gives the same readings.

*Proof.* (λa)/(λb) = a/b at every t. ∎

A single stream fixes the course of the relation, not its parties. A thing coming nearer and a thing at rest growing at
the matching rate are the same stream, and so is every mixture of the two. What the stream does fix is the relation's
own pace, the reading over its rate, x/ẋ; for a thing coming nearer at a steady rate it is the time left until contact,
the quantity Lee (1976) proposed a driver reads directly when braking.
Over time, a standpoint is given motion before it is given an object.

**Proposition 10 (one denominator, at once).** Two readings taken at the same moment, x₁ = a₁/b₁ and x₂ = a₂/b₂, have
the ratio x₁/x₂ = (a₁/a₂)(b₂/b₁). When the two parties share the denominator, b₁ = b₂, the ratio is a₁/a₂, whatever the
denominator is and however it changes.

*Proof.* Division. ∎

Reading at once recovers payloads relative to each other, and only where they share a denominator; by Proposition 8,
never their scale. A neighbour at the same distance tells growth from approach: under approach the ratio of the two
readings holds still, and under growth it follows the growth.

**Proposition 11 (standpoints bring back the figure).** Each reader reads only directions: for each place on a figure,
the turn at which it stands. Then:

(a) one reader fixes, for each place, only a line through it;

(b) two readers whose placement relative to each other is known up to scale, reading directions in one frame, fix every
place both see that is not in line with them both, up to one common scale;

(c) one agreed length between them fixes the scale.

*Proof.* (a) A direction from a known point is a line. (b) Two lines from different points, if not parallel, meet in
exactly one point, and moving both readers by a common similarity moves every meeting point by the same similarity.
(c) By Proposition 8(b). ∎

So one reader's readings, however many, fix no place. Laid out with nothing else, they return the circle of §5, the same
from every figure. The figure comes back from a second standpoint, and its size from an agreed length. This is
triangulation, read as a ladder of what each further standpoint buys; that two views fix a scene up to its scale is the
basis of reconstruction from two images (Longuet-Higgins 1981).

**Proposition 12 (below the resolution, the centroid first).** Payloads w₁, …, w_n > 0 at places x₁, …, x_n along a line
are read at a resolution: a kernel τ of total 1, mean 0 and spread σ². The reading f(x) = Σ w_i·τ(x − x_i) has total W =
Σ w_i, centroid x̄ = Σ w_i·x_i / W, and spread σ² + Σ (w_i/W)(x_i − x̄)².

*Proof.* Integrate the sum of shifted kernels: ∫ f = W; ∫ x f = Σ w_i x_i, since τ has mean 0; and
∫ (x − x̄)² f = Σ w_i (σ² + (x_i − x̄)²). ∎

Payloads closer together than the resolution arrive with their total and their centroid exact, however close they are.
Their arrangement does not vanish: it enters the spread, where it is smaller than the kernel's own by the square of the
separation over the resolution (two payloads with shares w and 1 − w at separation Δ add w(1 − w)Δ² to σ²), and the
third and higher moments at higher powers of Δ, fainter still (the same pair adds w(1 − w)(1 − 2w)Δ³ to the third).
So reading them as one payload at the centroid is an approximation, good to the second order in Δ/σ; it is exact only
in the total and the centroid.

So there are two centres, and they must not be confused:
- **The addresses' centre is the median,** an order statistic that a mean cannot replace (§7.6), had only by a reader
  that holds its readings.
- **The unresolved payload's centre is its centroid,** a weighted mean. It arrives first and exactly; the payload's arrangement reaches the reader only through the spread and the higher moments, faintly, until its parts lie the resolution apart.

Fingers order; colours add.

**The best estimate of the true size.** The geometry needs only the reader's one length (Proposition 3, Proposition
5(d)), and that says nothing about the world. Amounts need more: an estimate of the other party's true breadth V*, some
ĉH, by which the amounts the circle gives are scaled. That is a question about an amount, a writer's question, though it
can be asked on the reader's behalf: the reading v/h becomes ĉ·(v/h) thumbs. In
levels that is a shift of log ĉ, the same for every reading, and it leaves the circle and the turn alone. Every amount
is then off by the factor V*/(ĉH). Which ĉ is best depends on what the reader knows of V*.

**Proposition 13 (the best estimate is the median).** Measure the error by |f(V*) − f(ĉH)| for an increasing f: in
levels, f = log; in amounts, f the identity.

(a) If the reader knows only that V₋ ≤ V* ≤ V₊, the estimate whose worst error in levels is least is
ĉH = √(V₋·V₊), the corner of the pair of bounds. Its worst error is half the range, ½·log(V₊/V₋).

(b) If the reader holds a distribution for V*, the estimate whose expected error is least is a median of that
distribution. It is the same median for every increasing f. The mean, best under squared error in amounts, changes with
f and need not exist.

(c) If nothing the reader knows makes the other larger rather than smaller, so that V*/H and H/V* are alike, as bounds
H/R ≤ V* ≤ H·R for some R ≥ 1 or as a proper law for log(V*/H) symmetric about 0, (a) and (b) both give ĉH = H, the
estimate equal to the reader's own length. The improper dκ/κ alone has no median and gives no estimate.

*Proof.* (a) The worst error is the larger of |log V₊ − log ĉH| and |log V₋ − log ĉH|, least when log ĉH is midway
between log V₋ and log V₊. (b) E|X − m| is least when m is a median of X. For X = f(V*) a median is f of a median of V*,
since medians commute with increasing maps, as order does (Theorem 6(b)). (c) The bounds H/R and H·R have
geometric mean H, and a proper law symmetric in log(V*/H) has median 0. ∎

So for a reader whose knowledge is symmetric in levels about its own breadth, the best estimate of the true size is its
own breadth; otherwise it is the median of what the reader knows. The circle is not chosen, being the one length turned;
the estimate is, and this is how to choose it. The result rests on measuring error by order or in
levels, the same premise of no preferred scale as (S). Levels are what the reader's ignorance of the size leaves: an
error unchanged when the size κ = V*/H and the estimate are rescaled together, and alike for larger and smaller, is a
function of |ln(κ/ĉ)|, the error in levels, and with absolute loss in levels the best estimate is the median (b)
(§12.1). As a distribution, dκ/κ restricted to the bounds has its median at √(V₋·V₊)/H, the same estimate (§2).

**Designating and sizing.** Two acts are easily run together, and only one of them is a guess.
- *Designating* the other party is turning to it: reading it on the reader's one length, which gives the reader its
  geometry, the unit relations, the corner, the circle, the sweep and the Cauchy of §7 (Proposition 3). No breadth is
  given to the other party, so nothing is asserted about the world: a unit relation lies in [0, 1] however large the
  other truly is. It costs nothing. A reader with nothing to turn to has no relation and nothing to read: situation 0
  (§3.1).
- *Sizing* the other party, an estimate ĉH of its true breadth, gives amounts: the mountain in thumbs. That is the
  arbitrary part, and it is writing, an amount stated. By Proposition 13 the reader's best size is the median of what it knows.

So the geometry is free, and the amounts cost one arbitrary number. Sense is then made in three ways.
1. *The addresses are exact while the scale is wrong.* Directions, the corner, order and every shape up to scale do not
   depend on ĉ (Theorem 6, Proposition 8(a)). In §10 the fingers and the corners are right while every mile is off by
   a factor of twenty.
2. *Several observations construct what one cannot hold.* A second standpoint at a known baseline, or a fact shared
   with another reader, supplies the missing factor, and nothing within the readings does (Propositions 7, 8 and 11).
3. *The size can be revised, and the unit can be moved; these are different acts.*
   - A new fact moves the median, so the reader re-sizes the other party (Proposition 13).
   - Changing H instead is a zoom (§8). It chooses what sits at the reader's corner, and corrects nothing about the
     other's size.

The correction is cheap, and in levels it is exact. When the true size arrives, every reading moves by the same
log₂(V*/ĉH) levels, and no address moves against another. A lay that keeps (S) gives every doubling the same room, so
the levels keep their widths. The structure was never wrong, only where it sat, and one amount from outside slides it
into place.

**What a unit is, and why a reader needs one.** Proposition 8(a) says more than that the scale is hidden. A reader
whose world and own breadth are scaled together receives the same readings, so no reading contains a unit and none
needs one. A reader alone has a unit anyway: its own breadth. It reads the mountain in thumbs, and since it compares
its readings only with each other, the thumb serves. Nothing it does would change if its thumb were twice as long and
the world with it.

Something does change if the thumb changes and the world does not: what the reader reads finely. Its addresses are
finitely many, so the value of its unit decides which sizes fall at its corner and are given the most room, and which
crowd into home or run past the levels it holds (§8). With unlimited addresses every value would serve and the unit's
value would be idle; with finitely many, the reader needs a value suited to what it reads, and the sizes of what it
reads are amounts. So even a reader alone needs its unit for something, and the unit's value is where the scale of the
world first reaches it: not in its readings, which no unit changes, but in how it lays them.

A unit is needed again when amounts pass between readers. Two readers, each counting in its own breadth, give one amount x as
x/H_A and x/H_B, and the factor between them, H_A/H_B, is read by neither alone. A shared fact supplies exactly that
factor and nothing more (Proposition 7), and one amount supplied from outside fixes every amount the readings link to it
(Proposition 8(b)). That is what a unit is: a relation measured beforehand, between something both readers can read
and a notch agreed to count as 1, or between two kinds of amount, as five ounces to a foot. It carries in the one ratio
no reading supplies. Any such thing
serves: a body, a stick, one reader's thumb made public. A reader then sends an amount as a count of the agreed unit,
x = r_A·H_A, and the other takes it back into its own breadth, r_B = x/H_B. The round trip is one factor,
r_B = r_A·(H_A/H_B), and where the two breadths are equal the reading passes unchanged. The foot, the cubit and the
metre each began as one body or one object made into a public notch.

**Two ways to represent a thing.** A thing can be given in terms of something else in view: a reading, the ratio of
two amounts read at once, or an amount in the reader's own H. Such a representation carries no unit, and it is
geometric: no change of unit touches it (Proposition 8(a)). Or it can be given in terms of a unit agreed beforehand, as
a count of a notch both readers can read. That is still a ratio, but its second term is not in the reading; it was
measured beforehand and carried in, and that is where physics enters. Of the unitless values, the geometry fixes some:
the corner at 1, π/2 and 2/π, the near field 1/(n + 1). Others are read from the world, such as a mountain's reading or
a dimensionless constant of physics: geometric in kind, but found, not derived. Dimensional analysis rests on the same
division, since only unitless groups of amounts enter a law (Buckingham 1914).

So three numbers are easily confused, and the geometry needs none of them:
- the reader's own breadth H, which it chooses for itself and which only moves what sits at its corner, and so what
  it reads finely (a zoom, §8);
- its estimate of the other party's true breadth, ĉH, the one arbitrary number in sizing (above), best set at the median
  of what it knows (Proposition 13); the circle itself is the one length turned and is not a number to choose, and the
  c of a two-axis drawing is a page's or an instrument's, never the reader's (§5);
- the shared unit, which is neither a reading nor a guess but a relation measured beforehand and agreed between
  readers, needed for talking.

**Reading and writing.** Reading needs only ratios: every reading is a ratio, none contains a unit (Proposition 8(a)),
and the shape is read from ratios alone, its size the one term no ratio of radii reads (§7.4). Writing needs breadths.
To write a thing is to state it in amounts, as an equation or an array of breadths, and that is situations 1 and 2, the
whole held with V known. Reading is situations 3 and 4, the two sweeps, with V unknown. Situation 1 is common to both,
the baseline of every vantage. The circle is the reader's one length turned, there before anything arrives, and the
writer's equation, with V known to equal H: one circle held two ways, made by the one from H alone and known by the
other, who holds V. Situation
2 is writing alone, a shape written on that circle as its perturbation (§7.4), and 3 and 4 are reading alone. Taking the
reader's circle for the writer's is the confusion of §7.1. Writers and readers are told apart by their vantage: the
writer's is dual-hemispherical, a reader's hemispherical. There is one kind of reader, and its standpoint has both
sweeps: the inscribed, whose directions are the addresses, and the central, which places where each address's paint
lands (§4). A writer needs more than both: the addresses, an amount along each, which no paint carries, and the one unit
that fixes the size of the amounts (below). It loses its situation in the process: holding all of it at once is holding
the whole, situations 1 and 2, which the writer has by walking the complete object. So reading is the situated
operation, and writing produces the written, unsituated representation, stating a thing in amounts. A situated observer
can write, but only with information its ratios do not contain. To know a breadth is to hold the whole, both hemispheres
at once, which is situations 1 and 2 and which no standpoint supplies: no reading gives V*/H
(Proposition 8). An observer writes by carrying in what it did not read, a shared unit or an amount from outside, and
the writer's vantage is where that writing is done: the whole walked or carried in, not one place anyone stands. Reading
is free: the geometry supplies every ratio. Writing must discover the breadths, and every breadth it finds is an amount
from outside the readings (Proposition 8(b)), found by movement or by interaction. Movement takes the reader's own H as
a baseline: walked once, it gives the other's true size in the reader's own breadth, V*/H (§10, step 6). Interaction
takes in what another has measured: a shared unit, a known kind, a constant measured beforehand, and writes in a breadth
both can read. Counted, the steps are one each: from one standpoint nothing is written, each thing's size and distance
free together; one displacement of known length writes every breadth in the reader's own H, and a second adds nothing to
the scale; one number exchanged writes them for another reader; one notch agreed writes them in a public unit. An
observer is both a reader and a writer: as a reader it needs the unit relations h and v and its one length H, as a
writer the breadths H and V, and the value of its own H matters only where its readings meet amounts (the zoom, §8). The one bridge between them
is a unit relation times its breadth, and two such products must be kept apart: v·H, the amount in the reader's circle, which
writes nothing new, and v·V*, the amount at the other's true breadth, which is the act of writing and
needs V*. A reader that also writes needs actual breadths: to state the other's size in amounts is to write it, and
without V* it can write only its estimate ĉH (Proposition 13); to write an amount for another reader needs the shared
unit; a world drawn in amounts is written with its breadths known, and a common factor on all of them would change no
reading. Taking the reader's circle, V = H as a writer writes it, for a measurement (§7.1) is reading mistaken for
writing. What is written can change
without any reading changing, which is why no reading recovers it. With more parties writing still costs one amount, not
one per party: every party is read on the reader's one length, so one known move writes every breadth, V*/H and V₂*/H
alike.

**The inscribed reading is the ratio itself.** The reader never touches a breadth and never divides one by another. What reaches it through its standpoint is a direction, and a direction already is a ratio: v/h = tan θ, a point
of the projective line, [h : v] in homogeneous coordinates (Möbius 1827), before anything is divided. The dividing is
done by the projection through the standpoint, not by the reader: the reach cancels between the two legs of each reading
before it arrives (Theorem 6(a)), as a pinhole's image point is formed by the light and never computed from its two
distances. Breadths, and the division that turns them into ratios, appear only in a writer's account of the reading, the
writer writing it as V*/d. So the breadths may be as large as they like, even infinite, at no cost to the reader: a
breadth without bound arrives as one more direction, [0 : 1], the horizon, and the reading stays between 0 and 1. A
breadth that can never be written can still be read. Only where two breadths both grow without bound does their reading
need the limit of their ratio, which is again a ratio and must arrive as one. A reader that measures two amounts and
then divides them, two intensities compared, does touch breadths: it writes first and reads afterwards, and its
quotient is not a direction in this sense. With a third party the direction is [h : v : v₂], a point of the projective plane
carrying two ratios, v/h and v₂/h; a breadth without bound still arrives as a point at the edge, [0 : 1 : 0] for an
unbounded V*, and the reading stays bounded.

**The central sweep places the paint; the amount is written.** From the centre every ray is a radius, and equal turns
reach equal arcs (§4), so the central sweep's directions are laid out uniformly before anything arrives. For each
address it gives the point of the Thales circle where that address's paint lands, ½(h² − v², 2hv): a pair of lengths
along its axes, bounded by the radius, not a ratio of two unit relations, and lengths add, so every average over a
uniform turn exists (§4). That is why the central sweep has means and the inscribed only the median (Theorem 6(b), (c)):
a mean is an amount, and ranks are what survive when there are none. The point is the geometry's, laid at H; it is not
a distance to anything, and no paint carries one (§2). A shape about a centre, its radius r(θ) along each direction from
that centre, ln r = a₀ + f(θ), is an amount per direction. It is had only by writing, a range per direction with the
signal's speed carried in (§11, "From one place"), or from a second standpoint, which gives it in H (Proposition 11).
Even then the amounts are in one unit no reading fixes: the size a₀ = ln κ is the term common to every ray, and
changing it multiplies every amount by one factor (§7.4; Proposition 8). So the shape is had in amounts without its
size. Neither sweep gives the unit, the one term a₀. A writer needs all three: the addresses, an amount along each, and
the unit carried in from outside by a move or an exchange (above). Holding them at once is holding the whole, situations
1 and 2, the writer's. With a third party the directions are two angles, the altitude and the azimuth (§2), and an
amount along each is still in the one unit no reading fixes.

**The test: scale the world.** Whether a record is read or written can be checked without asking how it was made.
Multiply every breadth and distance in the world by one factor k. A reading does not change: a direction, each angle of
the survey, a photograph, the reader's [h : v], the central sweep's point on the circle, a shape held over its own mean.
A writing changes by k: a dimension on a floor plan, the length the map's scale bar states, the length of the base. A
shape's radii from its centre also move by k, but in a unit no reading received (above), so they state no size, and the
shape over their geometric mean does not move. This is Proposition 8 used as a test: what scaling leaves unchanged is geometry, and
what it moves, in a named unit, is an amount that had to be carried in. A record that scaling would not change cannot
contain the world's size, however carefully it was made.

Sorted by the test, reading and writing are the scale-invariant and the scale-variant: what does not move under k, and
what does. That is the old distinction of dimensional analysis, the absolute significance of relative magnitude
(Bridgman 1922) and the dimensionless groups of Buckingham's theorem (Appendix A), and the readings are such groups. We
keep the names reading and writing because they say more than the distinction does. They name the act: a writing is
made by carrying an amount in, since any function of scale-invariant quantities is scale-invariant, so no reading, however
many, yields a scale-variant number without at least one taken from outside. They name the vantage: the reader is handed
its invariants by the geometry, which removes the scale before anything is read (§3.8), while the writer holds the
variant quantities and can form invariants from them. And they name who can do what: a ratio of two lengths on a
blueprint is scale-invariant, a reading by the test, yet a writer formed it; the test sorts quantities, the names sort
vantages. Beside it the second test is a second invariance, under a change of what arrives.

**Two tests.** The paper's two distinctions can be applied without accepting its reading, by two tests anyone can run
on any quantity.
- *Scale the world.* Multiply every breadth and distance by one factor k. A quantity that does not change is a reading:
  a direction, an angle, a ratio of two breadths, a shape held over its own mean. A quantity that changes by k is a
  writing, an amount in a named unit, and somewhere an amount was carried in to state it (Proposition 8). In the worked example
  (§10) every reading of the mountain range is the same at k = 1/10, 1 and 100 (a range 2, 20 or 2,000 miles wide); its width and distance in miles move by
  k, and are had only once one thumb is walked.
- *Change what arrives.* Replace what arrives along each direction by something else, keeping the directions. A quantity
  that does not change belongs to the addresses; one that changes belongs to the payload (Theorem 6(a)). On data the replacement
  can be made by pairing each reading of one detector with another instant's reading of the other, which keeps each
  channel's own law and changes what arrives together: in LIGO's noise the direction's law did not change, so its
  departure from the uniform turn belongs to each channel's own spread, not to anything the two share (§7.2, "A case in data").

Together the tests sort a fact four ways: readings of the addresses (the corner, the quartiles of directions), readings
of what arrives (a colour, a ratio of intensities), and writings of either (a range in metres, a flux in a unit). Neither
test needs the paper's vocabulary to be run.

**Proposition 14 (a ruler that favours no unit).** Let a ruler lay each amount x > 0 at a place L(x), with L continuous
and not constant. Say the ruler favours no unit if changing the unit by any factor λ > 0 changes the layout only by a
change of the ruler's own scale and origin: L(λx) = a(λ)·L(x) + b(λ) for all x and λ, with a(λ) > 0. Then, up to the
ruler's own scale and origin, L is a power x^p with p ≠ 0, or the logarithm ln x. If the room between places may not be
rescaled, a ≡ 1, only the logarithm remains.

*Proof.* Applying the condition twice, L(λμx) = a(λ)a(μ)·L(x) + a(λ)b(μ) + b(λ), and the same with λ and μ exchanged.
Since L is not constant, a(λμ) = a(λ)a(μ) and b(λ)·(a(μ) − 1) = b(μ)·(a(λ) − 1). If a ≡ 1, then L(λx) − L(x) = b(λ)
depends on λ alone, and as in Proposition 4, L = k·ln x + m. Otherwise choose λ₀ with a(λ₀) ≠ 1 and set
C = b(λ₀)/(a(λ₀) − 1). Then b(λ) = C·(a(λ) − 1) for every λ, so (L + C)(λx) = a(λ)·(L + C)(x). At x = 1 this reads
(L + C)(λ) = a(λ)·(L + C)(1), and (L + C)(1) ≠ 0 because L is not constant. So a is continuous and multiplicative,
a(λ) = λ^p with p ≠ 0, and L = c₀·x^p − C. ∎

This is classical: it is the form Luce (1959) found for any law that carries a ratio scale to a ratio or interval scale,
and the functional equations behind it were later treated in general by Aczél, Roberts and Rosenbaum (1986).
Neither kind of ruler has a corner, since no amount is laid differently from any other. The reader's own lay is
neither. Proportional up to its corner and logarithmic past it (§6), it favours one amount, the one at its joint, and
that amount is its own: its breadth H.

Taken to its ends, the reader's lay becomes the rulers that favour none. On any stretch [a, b] of amounts, once H lies
past b the lay there is x/H, the number line, and once H lies below a it is 1 + ln(x/H), the logarithm; the in-place
lay gives 2 − H/x there, the power −1. So an H of ∞ and an H of 0 are exactly the rulers of Proposition 14, and the
corner, the one amount the lay favours, exists only for an H among the amounts read. At either end a reader with
finitely many addresses loses what it reads: an endless H puts all of it in the first address, and a vanishing H sends
all of it past the levels held, or, on the in-place lay, into the horizon's last address.

**The number line is a shared unit, and the writer's ruler.** The ordinary number line is the clearest example of a unit
agreed between readers. It is one notch agreed to stand for 1, built out by counting and dividing, and its form is the
form a shared ruler must have.
- *It has no corner.* Every stretch is laid like every other: 0.5 to 1 looks exactly like 1 to 1.5, and nothing turns
  over at 1. A corner would sit at some reader's unit and favour that reader, and by Proposition 14 a ruler that
  favours none has none. The corner belongs to the reader, where its unit falls on the line, not to the line.
- *It is proportional on both sides of 1.* It is the power p = 1, the near field's plain proportion carried past the
  corner. A shared ruler can do this because its notches are lengths, and everyone who uses it can relabel them together
  when the unit changes. A reader's addresses are a count, which cannot be relabelled, and past its corner (S) leaves it
  only the logarithm (Proposition 4). Where the range is wide, people share the other ruler Proposition 14 allows, one
  whose notches are levels: decibels, stellar magnitudes, pH. Scientific notation, 3.2 × 10⁶, writes both at once, a
  count of levels with a plain ruler inside one.
- *It is not a reader; it is the writer's.* It has no standpoint, so it has no situation. A reading
  passes through it, from one reader's relations to another's. The writer writes on it, and
  needs it as it is: to write is to state amounts, counted out in a unit and added, a breadth walked as so many strides,
  and a sum of equal steps is laid in proportion, the power p = 1, with each step alike wherever it falls. A corner
  would lay the steps on one side of it differently from those on the other, so the amount written would depend on where
  the writer's unit fell; a ruler for amounts must have none.
- *Its two infinities are its readers'.* Outward without end (1, 2, 4, …) and inward without end (1, ½, ¼, …) are
  exchanged by the reciprocal. They are the far and near sides of whatever unit a reader holds against the line (§3.3,
  §4), not two separate properties of the line.

So the number line is the writer's ruler, and the interface readers agree on so that amounts can pass between them; its
uniformity, without a corner, is what lets it favour no one.

## 10. A worked example: a mountain range

A reader looks at a mountain range, face on, from opposite its middle. As writers we know three amounts: the reader's
thumb H = 1 mile (the thumb is whatever single measure the reader holds; here it is a mile), the mountain's width V* =
20 miles, and its distance d = 10 miles. The reader knows only its thumb.

**The pairs.** Each pair has its own corner, so we name them first.

| pair | ratio | where it sits |
|---|---|---|
| half-width to distance, (V*/2, d) = (10, 10) | 1 | at that pair's corner: each end of the range lies 45° off straight ahead |
| width to distance, (V*, d) = (20, 10) | 2 | one doubling past that pair's corner: the range is wider than it is far |
| distance to the thumb, (d, H) = (10, 1) | 10 | log₂ 10 ≈ 3.32 doublings past the reader's corner |
| mountain to thumb, (V*, H) = (20, 1) | 20 | log₂ 20 ≈ 4.32 doublings: the mountain is 20 thumbs |

The first two can be read from the view itself, as directions. The last two set H against amounts the reader does not
have.

**The writer's map.** The writer holds 1, 20 and 10 in one unit, miles: the blueprint, with the range drawn 20 miles
wide and 10 miles out and its ends at ±45°. Every number in the table is available to it, and the 45° is simply where
the ends are; nothing marks it. Thumb and mountain are both in hand: the mountain is 20 thumbs, and the point where
thumb equals mountain is computed, not found. There is no home, no order of arrival and no horizon. It holds the true
width, and no one stands anywhere in it.

**From where the reader stands.**
1. *The addresses come first.* The reader's circle has radius 1 mile, with the corner at 1 mile: proportional addresses
   inside, and past it the same number of addresses for each doubling, 2, 4, 8, 16 miles and on. All of this is laid
   whether or not anything is there.
2. *What it reads exactly.* Among its directions, zero, v/h = 0, is straight ahead at the middle of the range, and the
   range's ends are at v/h = ±1: exactly at its corners. It knows that the ends sit at its corner, though not
   why. With fingers spread uniformly over the half-turn, the range takes exactly the middle half of them, between the
   Cauchy's quartiles, which are its corners (§7.3), and the median finger points at its middle. On each finger the
   ridge's elevation is a second direction, read by the altitude sweep (§3.7). Together they give the range's skyline, a
   curve of directions, up to scale. The far slopes are hidden, panes behind panes.
3. *The two sweeps, on the thumb.* The one breadth the reader holds is its thumb, the H it started from, and the two
   sweeps of §3.4 measure it by the turn from the reader's standpoint. Each side of the half-turn is a quarter turn,
   from home to the limb, where a finger runs parallel to the range and never meets it. On the thumb's circle that
   quarter turn is an arc of π/2 thumbs, and its projection on the line across the view is exactly 1 thumb. Read by the
   central sweep, limb to limb, the whole half-turn is an arc of π thumbs over a projection of 2, and the central
   reading, the turn over its projection, is π/2. Read by the inscribed sweep, from home, the inscribed reading, the
   projection over the turn, is 2/π: the fingers' mean projection (0.6368 with 36 fingers at the midpoints of 36 equal
   steps of the half turn; 0.6367 over a quarter). Their product is 1: H
   measured in H, the value the reader started from, which neither sweep reads alone. Out to the
   range's ends, at 45°, the same two readings are θ/sin θ = 1.1107 and sin θ/θ = 0.9003, the row of §3.4 at 45°, and
   their product is 1 again. None of this involves the mountain: a range 2 miles wide at 1 mile gives the same fingers
   and the same products. Joined, the two sweeps return only what the reader put in; the mountain's breadth must be
   constructed (step 6).

   The two sweeps can also be joined by their rates, and on this range they say the same thing.
      - The circle about the range's middle, of radius half the width, passes through both ends. Because the pair
     (V*/2, d) is at its corner, it passes through the reader's own place too.
   - So the reader's standpoint is on that circle, and the central sweep is the one about its centre. From the centre
     the ends lie 90° either side of the line to the reader; from the reader they lie 45° either side (step 2).
   - By the inscribed angle theorem, the reader's direction turns at exactly half the rate of the radius, at every
     point of that circle. These are the rates 2 and 1 of §4, seen from the other side.
   - Joined as twice the inscribed rate less the central rate, 2·dθ/dφ − 1, the two sweeps of any circle give the
     circle's own Cauchy. That is the wrapped Cauchy (the Poisson kernel, the harmonic measure seen from the reader's
     place), since 2·dθ/dφ − 1 = (1 − |z|²)/|e^{iφ} − z|² for a reader at z in units of the radius. Its centre and
     concentration are the reader's direction and distance, in the circle's own radius.
   - Here the reader is on the circle, |z| = 1. The combination is 2·½ − 1 = 0 everywhere but at the reader's own place,
     where all of it gathers.

      Joined by their product the two sweeps return H in H. Joined by their rates they return the reader's own place.
   Neither form reads the 20, and scaling the world moves neither.
4. *What it cannot read.* A range 20 miles wide at 10 miles, 2 miles wide at 1 or 2,000 miles wide at 1,000 gives the
   same fingers and the same colours. The reach cancels from every reading (Theorem 6).
5. *Mountain equals thumb.* Not knowing the mountain's size, the reader has only its thumb: the range arrives as
   directions on the thumb's circle, and a writer reading amounts off that circle takes the range to be one thumb, 1
   mile, wide (V = H, as the writer writes it); the width-to-distance reading of 2 then puts it half a mile away. Every amount is off by V*/H = 20,
   the number of thumbs the mountain really is, by the same factor on both sides of the
   corner. In levels, the reader places the range at 0.5 H, inside its near field, when it is truly at 10 H, 3.3
   doublings out in the far field: a rigid shift of log₂ 20 ≈ 4.32 levels, with the pattern of readings untouched. This
   is the one number of §3.8.
6. *Constructing the truth.* A second standpoint at a known baseline closes the gap. Walk one H, a mile, toward the
   range: its half-angle grows from 45° to 48.0°, the reading from s = 1 to s′ = 10/9. Then d = H·s′/(s′ − s) = 10 miles
   and V* = 2·s·d = 20 miles. The walk is where an amount enters: the reader's own starting value, walked once and used
   as a baseline. The true width, 20 thumbs, is constructed from two standpoints and observed from neither; it is 20
   miles for whoever has agreed that a thumb is a mile (§9). Once d is known, the range sits at 1 + ln 10 ≈ 3.30 on the
   logarithmic lay and at 2 − 1/10 = 1.9 H on the in-place lay, inside the reader's 2H.

What is the same for every reader, and exact: the fingers, the corner at the range's ends, the range's share of the
Cauchy, the skyline's shape, and the two sweeps' readings of the thumb, whose product is 1. What belongs to the
payload: the 10 and the 20. The writer has them, from having walked the whole; the situated reader has them only by
construction, and until then it is off by one factor, which is one shift in levels.

## 11. Applications

Each of the following applies the propositions above to a familiar case. None is needed for them, and each can be read
on its own: they show the separation of address and payload, and the one amount writing needs, where they are met in
practice.

**A survey: many readings, one amount.** Triangulation divides the labour exactly so. Snellius measured an arc of the
meridian, about 130 km from Alkmaar to Bergen op Zoom, as a chain of triangles whose angles he read from church towers,
and scaled the whole chain from one short base near Leiden (Snellius 1617). Roy's triangulation, which joined Greenwich
to Paris and began the Ordnance Survey, read its angles with a theodolite from hill to hill and took its scale from one
base on Hounslow Heath, about 8.4 km, measured with rods through the summer of 1784 (Roy 1785). Every angle is a
direction read at a standpoint, a reading in the sense above, and the network of angles fixes the figure up to its size
and no further, however many angles are read (Propositions 8 and 11). The base is the one amount carried in, found by
moving along the ground, and it writes every side of every triangle at once, in the base's own unit. A second base, as
Roy measured one on Romney Marsh, adds nothing to the scale: it checks the angles that carried the first base's length
to it. The costs fall where the geometry puts them: each angle needed only an instrument and a standpoint, while the
base needed the ground itself, crossed rod by rod, and one was enough to write the whole. The finished map is the
written thing, the writer's representation, and its scale bar is the base.

**The ground: one's own height as the base.** A reader standing on level ground carries a base with it. The horizon
of a ground plane lies at the eye's height, so it cuts every object standing on that plane at the same height above
the plane's surface: the part of the object below the horizon is one eye height tall. If the object's foot reads F
below the horizon and its top E above, its height over the eye height is (tan E + tan F)/tan F, a ratio of readings
(Sedgwick 2021, restating his horizon-ratio relation of 1973 and 1986; Sedgwick 1973, 1986). Without the eye height every object's size
relative to every other is still read; with it, each is written in that one length. As Sedgwick puts it, without the
eye height "the vertical extents of all those objects relative to each other are still visible even though their
vertical extents relative to the observer are not", and he names the separation of the two eyes and the step of a
moving eye as scale factors of the same kind: the baselines of "One standpoint gives no parallax" below and §10's walk. Three things are
added here, and none is read: a plane known to be level, the eye's height above it, and each object's contact with
it. Given those, the eye height is the survey's base, carried in the body instead of measured with rods. An object
exactly one eye height tall has its top on the horizon: it is at the corner of the pair (object, eye height), its
true breadth equal to the eye height.

**Growth, the test's other form.** The world can also grow without being scaled, and the same split shows. An address
made by dividing a thing's place in a list by the list's length is a ratio, a reading of the list's own contents: the
thing a third of the way through a level is placed a third of the way through, and it moves as soon as the level grows.
An address made of slots, a fixed number to each level whatever the level holds, does not move: the number of slots, the
radix, was agreed beforehand, and it is a written amount carried into every address, as the base is carried into every
side. A timestamp is the familiar case. Year, month, day, hour, minute and second are levels with fixed slots, and
2026·9·3·14·30·15 names the same second however many later seconds are recorded, because nothing in it was divided by a
count. Positional notation is stable for the same reason. Read against its own contents, a list re-addresses itself as
it grows; written against an agreed radix, it never does, and the price is the slots held empty.

**Units within units.** Ratios can carry much more than one relation. When lengths are read against units nested one
inside another, every unit cancels inside its own level, and what is left between two levels is again a ratio, read one
level up. An ISO metric screw thread is a standard case. Its profile is fixed by the pitch P (ISO 68-1): the fundamental
triangle stands (√3/2)·P high and the basic depth of engagement is five eighths of that, so the profile's ratios,
0.86603 and 0.54127 of the pitch, and their quotient 1.6, are the same from M6 to M36, readings against the pitch in
which the pitch cancels. The pitch is set against the nominal diameter D by a second standard (ISO 261), and what
relates a profile length to the diameter is P/D, a ratio read at the level above, not an amount. Two lengths read
against one unit are related directly; two whose common unit lies k levels up are related through k ratios, one for each
level between. However the n lengths are grouped, n − g ratios inside g groups and g − 1 between them make the same
n − 1, every independent ratio there is. So a reader can hold a whole hierarchy of units, each level read against the
one above, in ratios alone. What none of them gives is the top: writing still costs one amount, and one length anywhere
in the hierarchy, a single diameter in millimetres, writes every other.

**A worked example of the tower.** A building holds two rooms, A and B, and each room holds two things. Each length is
read only against the length that holds it, so every reading is a ratio, and none is an amount:

| reading | against | value |
|---|---|---|
| room A | the building | 1/2 |
| room B | the building | 1/3 |
| thing a₁, thing a₂ | room A | 3/4, 1/2 |
| thing b₁, thing b₂ | room B | 2/3, 1/3 |

Seven lengths give six readings, n − 1: four inside the rooms and two between them. Two things in one room are related
by one quotient, a₁/a₂ = (3/4)/(1/2) = 3/2. Two things in different rooms are related by two quotients, one for each
level up to the building that holds them both: a₁/b₁ = (3/4)/(2/3) · (1/2)/(1/3) = 9/8 · 3/2 = 27/16. Nothing has been
measured yet. One amount then writes every length, whichever it is: the building's 12 m gives a₁ = 4.5 m and b₂ = 4/3 m;
b₂ = 1 m measured instead gives the building 9 m and a₁ = 27/8 m. Scaling the world by k multiplies every one of those
amounts by k and leaves the six readings as they were. And if one link is misread, room B taken as 0.3 of the building
instead of 1/3, everything in room B moves by one factor, 9/10, its ratio b₁/b₂ = 2 does not move, room A is untouched,
and a₁/b₁ is off by that one factor, 10/9. A whole hierarchy is held in six ratios, and one amount anywhere in it writes
the rest; an error in a link is shared by everything the link holds.

**Closing a loop, and what is left to the reader.** A tree of readings, each thing read against only the one length that
holds it, cannot find its own error: room B misread moves everything in B together, and every reading inside B still
agrees. A second route finds it. Read a₁ directly against b₁ as well, from a standpoint where both are in view: the
reading is 27/16, where the chain through the misread link gives 15/8, and the two routes disagree by 10/9, the misread
factor exactly. That is a closure error, and it is why surveys are built of triangles and checked by a second base. The
reader computes none of this. The projection through its standpoint divides (above); that ratios compose by
multiplication is the geometry's; whether two routes close is the geometry's too. What the reader contributes is not computation but position: choosing H, its one length, which the geometry cannot
choose for it (§5), and taking standpoints, a second one for a loop to close or a known move for an
amount to be written. The heavy lifting is done by the geometry
and by being situated.

**Recovered, not written.** A reader is not powerless. By taking standpoints, closing loops and carrying in one amount
it can recover a thing exactly: its shape, its places, even its size (§10). What it recovers can be true and still
partial. A loop that closes shows that the routes taken agree; it cannot show that no route remains untaken, and only a
second route that disagrees reveals a gap (above). So completeness is never a reading: a reader can find its account
incomplete, never prove it complete, and the correctness of what it has recovered does not settle how much it has
recovered. Nor does recovering the truth make the reader the writer. The writer holds the whole by walking it or by
carrying in its measure, and states it in amounts from a vantage that holds both hemispheres. A reader that reaches the
same statement has reached it by cleverness, in where it stood, which routes it closed and what it carried in, and not
by holding the whole. Reading does not turn into writing; what the reader recovers is exact where it is exact, and its
completeness is not the reader's to know.

**Inside a room.** Each room is a hold, and the reader's one length gives it a unit circle on which both sweeps of §4 lie. From
home on that circle the things in the room are directions [h : v], addresses, and together they are the room's layout,
with no amount in it; each address is painted by the thing it meets, and the central sweep places where that paint lands
(§4). What a thing is beyond its outline, its shape about its own centre, is a radius along each direction from that
centre, an amount (above): had from further standpoints or written, its shape over the radii's mean (§7.4), its size the
one term no ratio reads. Moving a thing changes its address and not its shape; reshaping it changes its shape and not its
address. Its size in the room's units comes from neither sweep but from a shared denominator: the thing and the room's
wall, side by side at one distance, read against one denominator, give the one relative to the other, and the distance
cancels (Proposition 10). So a room is read whole, its layout, its things'
shapes and their sizes, in ratios, and the tower's links join the rooms. Each room has its own corner, one for each
hold, as two readers with different H have two; the levels of the tower are holds joined by ratios, not corners nested
inside one another.

**To move the furniture is to write.** A reader that wants to move a chair to a place, or hang a picture at a height,
wants a thing to be at an amount: a metre from the wall, at eye level. No reading holds that, so the reader must become
a writer, and writing needs what reading never does: the reader must move and engage with the room's geometry
physically. A known step, a hand laid flat against the wall, a tape measure: one amount carried in writes every length
of the room in its unit (§10, step 6), and only then can the place wanted be named. Then the writer acts, and the act
changes the payload, not the geometry: the chair moved has a new address and the same shape, the picture hung a new
place on the wall. Reading the room again afterwards is free. Reading is done from where the reader stands; writing, and
changing what is written, needs the reader to move.

**Far off, parallax in place of the shape.** A thing's shape about its centre needs the directions from that centre
across its turn, and from outside the thing they are had only from standpoints round it: each gives one direction from
the centre (Proposition 11). Seen from the thing's centre, the standpoints span its parallax angle, the widest angle
there between two of them; for a thing at distance d and standpoints spanning B square to the line of sight, that angle
is about B/d. The shape needs a good share of the whole turn; the place needs only two directions that differ. By
Proposition 11(b) any parallax angle larger than the resolution ε fixes the place, up to the common scale, to about ε
over that angle, as a share of its distance. So as a thing recedes the shape is lost first, while the place is still
fixed: parallax is what is left of the shape when the standpoints no longer go round, two points of the circle they
would have spanned. Past d ≈ B/ε every standpoint reads the thing in one direction, and only a line through it remains
(Proposition 11(a)). Its breadth across, held between its two edges, lasts while that breadth is more than ε of its
distance. Near, a thing gives shape and place; farther, place without shape; farthest, direction alone. Each loss is set
by a ratio, of the baseline or the thing to the distance, and not by any amount.
Robotics meets the same order from the other side. A single moving camera recovers a scene and its own path only up to
one common scale, which stays undetermined unless a known length is supplied; a feature that shows no parallax “cannot
be used for estimating camera translation but is a perfect bearing reference for estimating rotation”, so such features
are kept as a direction with an inverse depth that may be zero until the motion gives them a place (Civera, Davison and
Montiel 2008). Joining every direction from every standpoint into one figure is bundle adjustment (Triggs et al. 2000).

**One standpoint gives no parallax.** A turn about the point seen from, home, carries every direction through the same
angle, near and far alike, so nothing shifts against anything else: it gives the directions, the frame and the corner,
and no distance. Both sweeps belong to that one standpoint, the inscribed pivoting at home and the central at the middle
of the chord, and the standpoint does not move; that is why one standpoint gives the frame and not the size. Parallax
needs the point seen from to move, or a second point seen from at once: a baseline B, which by Proposition 11(b) places
things out to about B/ε, in the baseline's own length, and in a shared unit once the baseline is an amount carried in.

**From one place: the outline is free, the face is carried in.** A standpoint that does not move still sees a thing
from many sides when the thing crosses its view. Each look gives the directions that meet the
thing, and the two at the edges of that set are lines that touch it. Over the crossing these lines close in on it from
every side the line of sight turned through, and what lies within them at every look is the thing's visual hull
(Laurentini 1994). The hull contains the thing, meets it wherever some edge touched it, and elsewhere only spans it: a
hollow that no edge reached is bridged over. Where an edge grazes a smooth surface, the map from the surface to
directions folds (Whitney 1955): points just either side of the rim meet the same directions, so the outline's
directions do not say which side is which. What the outline gives beyond the hull is its curvature, whose sign is the
sign of the surface's Gaussian curvature at the rim, convex where it bends out, saddle-shaped where it bends in
(Koenderink 1984). It is built of directions alone, so it is the outline up to the common
scale, and nothing in it moves when the world is scaled; the thing's track across the view, which the hull needs, is
itself known from the looks only up to that scale. The face needs more: along each direction, how far the surface lies, an
amount, in a unit. A range gives both: the time for a signal to go out and return, times the signal's speed, which is an
amount measured beforehand and carried in. That speed supplies the unit, the one term a₀ that no reading gives, so
ranging is writing. With the ranges, every point met is held in that unit, and with them the face, and the thing's distance and speed as well.
From one standpoint, then, the addresses, their paint and the outline come free; the face needs an amount along each
direction, written, or further standpoints (above).

**Special relativity's sky.** A moving observer sees each source change in two ways, which the theory writes as two
formulas.
- **Where the source is seen moves.** This is aberration: cos θ′ = (cos θ + β)/(1 + β cos θ), the same at every
  frequency. In the stereographic chart it is z ↦ z/k, with k = √((1 + β)/(1 − β)), a Möbius map of the celestial
  sphere (Penrose 1959; Terrell 1959).
- **What arrives at each place seen changes.** This is the Doppler factor D = √(1 − β²)/(1 − β cos θ′), which scales
  each photon's energy and its arrival rate.

The first is a map of addresses, and it carries the Cauchy's family onto itself.
- A sky uniform in the sources' own frame is seen as the spherical Cauchy, density (1 − β²)/(4π(1 − β cos θ′)²)
  (Kato and McCullagh 2020).
- Its parameter is ρ = tanh(η/2), where η is the rapidity. With one dimension fewer it is the wrapped Cauchy with the
  same ρ.
- That density is D²/4π: the crowding of addresses toward the motion.
- It keeps the cross ratio of any four sources' places, read as complex numbers in that chart, and three sources seen
  in both frames fix the whole boost and turn: the Möbius maps of the sphere are the Lorentz group, and a Möbius map
  is fixed by three points (Penrose and Rindler 1984).

The second is a weighting of the payload at each address, and it moves no address.
- Of the D⁴ by which an isotropic sky's intensity brightens ahead (Rybicki and Lightman 1979), D² is read here as the
  addresses' crowding and D² as the payload, energy and arrival rate, D each; the D⁴ is standard, the split this
  paper's reading.

So the motion can be read from the addresses alone. On the levels ξ = −ln tan(θ/2), the pseudorapidity, aberration is
a shift by η exactly, and a sky uniform in the sources' frame lies as ½·sech²ξ, its median the transverse plane; seen
from the moving frame it lies as ½·sech²(ξ′ − η), its median moved to η. A reader holding directions alone reads its
own rapidity, a reading, with no clock, no frequency and no c carried in, provided every source is counted whatever
its brightness and the sources are uniform in their own frame. A census cut by brightness adds a weighting of the
addresses, D raised to a power read from the census's own ratios (the slope of its counts and a ratio of two bands):
still a reading, needing no rest frequency, but no longer of directions alone. To read the Doppler factor as a
frequency needs a rest frequency carried in, a known kind: a writing.

The split is in the formulas, aberration apart from Doppler shift and beaming. It is not named there as a
transformation of addresses and a weighting of payload. The identities are exact.
The same theory runs on §6's three rulers. A velocity's celerity γβ is x, its rapidity η is ζ, and with χ the turn
ruler's angle (not the aberration angles above), its speed β = tanh η = sin χ and γ = sec χ (γ here the Lorentz factor, not a Cauchy half-width). Rapidities add along a
line, and uniform acceleration is uniform in η, not in χ, so its corner γβ = 1 (β = 1/√2) is where its two regimes
hand over, not a median.

## 12. Discussion

### 12.1 The principle, after Jaynes

With the method of §2, the results above rest on one principle rather than several:

> A situated reader gives equal addresses to whatever its readings cannot tell apart.

This is Jaynes's principle of transformation groups (1968, 1973), read as a rule for addresses rather than for belief,
and Klein's criterion applied to measures. It is applied to a group chosen as the situated reader's ignorance (§2), and
what it gives rests on that choice and on two further premises, which we name. Given that the sweep is the turning of a
rigid bar, the turns give the uniform turn, and so the Cauchy and the fisheye (Proposition 5); the bar has the reader's
one length, so its attitudes trace the circle (Proposition 3(c)), and the circle and the Cauchy rest on one premise, the
rigid turn. The exchange of the unit relations gives the corner, and, acting on the law of the readings, says that a
drawing with two axes has the reader's circle only at c = 1 (Proposition 5(d)), as the rigid turn also does
(Proposition 3(e)); reciprocal symmetry (Proposition 2(b)) is its
invariance stated as a rule. The rescalings of the other's size give dκ/κ, and, carried to amounts, motivate premise (S)
and so the logarithm past the corner (Proposition 4); (S) is still assumed (§12.2, question 1).

Inside the corner the reader holds H as a length, and one more indifference applies: no position within H is preferred,
so equal differences within H get equal room, which is proportion. It is an indifference within the near field, not a
translation of home, which stays where it is. The two address spaces are then the same principle applied on either side
of what the reader knows, to different transformations. Their spacings, 1 and k/x, agree at x = 1 only for k = 1, the
smooth join, which is chosen (below). The halving of §6 is the same criterion applied to points.

On the reading itself a different group acts, and it should not be confused with the reader's ignorance. On the signed
reading x = v/h, over both quadrants, a turn acts as the Möbius map x ↦ (x·cos α + sin α)/(cos α − x·sin α), and a
change of a two-axis drawing, V = cH, as x ↦ x/c. Together these generate PSL(2,ℝ), every element of which factors as turn,
change of drawing, turn; adding the reciprocal x ↦ 1/x gives PGL(2,ℝ), the group that preserves cross ratios. The Cauchy
family is the orbit of the standard Cauchy under this group, which acts on it transitively (Knight 1976; McCullagh 1996), and as points
m + iγ of the upper half-plane it is the hyperbolic plane on which the group acts. The drawings V = cH are the points
i/c, one line of that plane, at distance |ln(c′/c)| from one another, the number of levels between them times ln 2. This
group is not the reader's ignorance: its change of drawing is not something the reader leaves open, since the reader
holds one length and has no c, and acting on the readings alone it is too large in Jaynes's sense, with no probability on
readings unchanged by all of it (the case he calls overdetermined, 1973, §8). It is a fact about the family of drawings,
and its one use here is to measure distances.

The estimate of the size is measured by the reader's own ignorance, not by this group. If the loss of an estimate ĉH is
to be unchanged when the other's size and the estimate are rescaled together, it is a function of κ/ĉ; if larger and
smaller count alike, of |ln(κ/ĉ)|, the error in levels; and with absolute loss in levels the best estimate is
Proposition 13's median. The Möbius picture gives the same quantity as a distance: the uniform turn of the drawn bar,
read in amounts at the true breadth, is the Cauchy law at iκ, and read at the estimate it is at iĉ; their distance is
|ln(κ/ĉ)|, the one distance along curves, up to a constant factor, that the action keeps (Beardon 1983).

The nearest use of these three transformations together is in fitting a line when both coordinates carry error: Leonard
(2011) puts the Cauchy, the slope's law invariant under turns, on the slope, and the inference that results is unchanged
by exchanging and by rescaling the two coordinates. The claim is therefore not the principle, which is Jaynes's, but
that a situated reader's state of knowledge selects these transformations, from which, with the premises named above,
the structure follows. Two things remain outside it. Invariant measures are fixed only up to a constant, so the smooth
join at the corner (k = 1) is still an added condition. And "no attitude preferred" still treats the sweep as the
turning of a rigid bar.

Which transformations a reader is ignorant of is chosen here, not derived. A reader ignorant of more or of fewer would
be given other measures. Because ignorance of attitude presupposes turns, the principle cannot choose the circle over
the square (§12.2, question 2).

**What is claimed, then.** The geometry is necessary relative to a stated ignorance, not absolutely: a reader that does
not know which unit relation a reading was divided by, which attitude the bar is in, or how large the other party is.
From that premise and the reader's one length, with the sweep taken as the turning of a rigid bar, come the circle (one
length turned, Proposition 3(c), (g)), the corner and the median (the exchange), the uniform turn and the Cauchy (the turns), and, through amounts and premise (S), the logarithm past the corner (the
rescalings). Each relaxation gives a named alternative rather than no geometry:
- a second length, held on a page or imposed by an instrument with a preferred axis, gives c ≠ 1; the bar is then no
  longer rigid, and a uniform turn puts the Cauchy's median off the corner (Proposition 5(d));
- a preferred direction gives the square's or the line's law, with the median at the corner and the missing mean
  intact (Theorem 6(e));
- a preferred scale gives a lay that stops there (§8, §12.2 question 1).

The main result's core, order surviving and sums failing, with the median at the corner, needs only the first of the
three; the missing mean needs besides a density of h bounded away from zero near the horizon (Theorem 6(e)).

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

The reading predicts no new number, but it makes a claim that can fail (§7.2, "What is observed, and what the reading predicts").

### 12.2 Assumptions and open questions

**What depends on what.** The results of the earlier sections do not all rest on the same premise. Each row gives a
result and the condition that makes it hold, whatever else the reader's weighting of its attitudes does; the proofs
stay where they are.

| result | the condition it needs | where |
|---|---|---|
| Each reading is a direction, with no unit; scaling the world moves none | the addresses fixed before anything arrives; any weighting | Proposition 8(a) |
| The address law is independent of the payload; ranks and medians commute with every increasing map; the reader's K addresses hold any number N of things, those sharing an address arriving as one | the addresses fixed before anything arrives; any weighting | Theorem 6(a), (b); §8, "A fixed count, aimed by H" |
| The median at the corner, K/2 addresses on each side of H | the weight unchanged by the reciprocal; no condition at the horizon (sin² 2θ has its median at the corner and a mean, 4/π) | Theorem 6(e); question 2 below |
| No mean; a tail c/s, so the last of K addresses begins near c·K·H | a density of h bounded away from zero near the horizon, at least f₀ > 0 there; since the path ends at all of v, v ≥ v₀ > 0 wherever h is small, so P(v/h > r) ≥ f₀·v₀/r far out; no symmetry (a weight leaning toward the horizon has no mean and its median off the corner) | Theorem 6(e); §8, "Other ways to squeeze the line" |
| Every pair's median at its own corner | each pair's weight unchanged by its own reciprocal | Proposition 5(e); "More parties" |
| Near in all readings for 1/(n + 1); the number of readings past their corner uniform over 0, 1, …, n | the weight unchanged by every permutation of the n + 1 unit relations; the pairs' symmetry is not enough (half the weight on each of two chambers can keep every pair's median at its corner and never have h the largest) | "More parties"; "Why uniformly by area" |
| The exact Cauchy, its 2/π and quartiles √2 ∓ 1; on the octant the two-dimensional Cauchy and the near field exactly ⅓ | the uniform turn, or on the sphere uniform area: the reader treats every turn alike | Proposition 5(b), (d), (e); "Why uniformly by area" |
| Staying a Cauchy under re-aiming and under sums. Re-aiming: a new zero or a change of H acts on the signed reading over both quadrants (the projective line) as a real Möbius map g(x) = (ax + b)/(cx + d), and X distributed as C(z) gives g(X) as C(g(z)) for every such map with ad − bc > 0 (as C of the conjugate of g(z) when ad − bc < 0; the pole is one reading, of probability zero, sent to the horizon). Within one quadrant a turn does not keep the half-Cauchy. Sums: of independent readings, each Cauchy, the points m + iγ adding. The stretch 2KH/π before the horizon | the readings Cauchy to begin with, which the uniform turn gives; for sums, independence as well | §7.2 (McCullagh 1996); §8, "Other ways to squeeze the line" |

The first two rows are the paper's main result in its widest form: the split of address from payload, and K from N,
holds for any reader whose addresses are laid before anything arrives. The Cauchy is that split under the uniform turn.

1. *The link in Proposition 4.* (S) does not follow from "any H will do", which only places the corner. It is scale
   invariance of the lay's increments, motivated by Proposition 3(b), since a lay that breaks it builds in a scale no
   reading can fix, but assumed rather than derived. The second route of §6, an additive measure on chains of
   relations, is equivalent to it, not weaker. Is there a premise about situated readers, thinner than scale
   invariance, from which it follows? Real readers do have preferred scales, their own resolution among them. Here a
   preferred scale sets where the lay stops, the count of levels a reader resolves (§8), and (S) is claimed only for the
   lay's form within that range.
2. *Why Euclidean, and why the uniform turn?* The readings are directions only, so the norm enters only through the
   measure on directions, and the two questions are one: is there a reason, from the reader's premises, that its weight
   on directions is the one every turn leaves unchanged, rather than the square's or the line's? The median at the
   corner and the missing mean do not depend on the answer (Theorem 6(e)); the Cauchy's exact shape does. Part of the
   answer is Proposition 3(g): a continuous linear sweep that returns after a full turn, carrying h into v a quarter of
   the way, preserves an inner product of its own,
   unique up to the factor H, so the norm follows from a linear sweep, one motion repeated, and that is what remains
   chosen; uniformity is not chosen, since a turn measured by itself is uniform (§2). The sharpest form of the objection
   is Drory's (2015), against Jaynes's treatment of Bertrand's chord (1973): the same symmetries, turns, rescaling and
   shifts, can be imposed in different ways, and give different measures, depending on how the random selection is made.
   We grant it. Which selection is made is a choice of what the turn is counted against (§2): the turn itself gives the
   uniform turn, while a clock, a flat ruler or a count of arrivals gives another law (§12.1), and symmetry alone does
   not say which is wanted. What the framework adds is that the core of the main result survives the choice: any
   selection that treats the two parties alike puts the median at the corner, and leaves no mean if its weight does not
   vanish at the horizon (Theorem 6(e)).

   Three paths from all of h to all of v show what that leaves free. Sweep each uniformly along its own length, and
   write g for the share of the sweep done when the direction θ is reached:

   | path, swept uniformly along its length | g | at 22.5° | at the corner, 45° | at 67.5° | the mean below s, per tenfold of s |
   |---|---|---|---|---|---|
   | the circle, h² + v² = 1 | 2θ/π | 1/4 | 1/2 | 3/4 | (2/π)·ln 10 ≈ 1.47 |
   | the line, h + v = 1 | tan θ/(1 + tan θ) | 1 − 1/√2 ≈ 0.293 | 1/2 | 1/√2 ≈ 0.707 | ln 10 ≈ 2.30 |
   | the square's edges, the larger of h and v at 1 | tan θ/2, then 1 − cot θ/2 | (√2 − 1)/2 ≈ 0.207 | 1/2 | (3 − √2)/2 ≈ 0.793 | (ln 10)/2 ≈ 1.15 |

   Each has g(θ) + g(90° − θ) = 1. They agree at zero, at the corner (½) and at the horizon (1), and part in
   between. So the two ends, the reciprocal and its symmetry fix the corner and the median, and leave the scale between
   them free. Only the circle is uniform in the turn, and the uniform turn is what gives g = 2θ/π, the Cauchy's exact
   shape and the factor 2/π: the premise selects the geometry, and the circle supplies the factor. None of the
   three has a mean. The mean of the readings below s grows, far out, by a fixed amount each time s grows tenfold (the
   last column), because each gives h a density bounded away from zero near the horizon. The horizon condition does real work: the circle weighted by
   sin² 2θ also treats the two parties alike and keeps its median at the corner, but it vanishes at zero and at the
   horizon, and its readings have a mean, 4/π.

   The three classical priors for a share come from this paper's drawings: two of the paths above swept uniformly, and
   the levels. The line's is Bayes and Laplace's uniform share. The circle's, read at the foot of each of its points on
   the chord, which cuts the chord h² : v² (Euclid VI.8), is Jeffreys's prior for a share, the arcsine law
   1/(π√(t(1 − t))) (Jeffreys 1946). The levels give Haldane's, 1/(t(1 − t)), uniform in the logarithm of the odds
   (Haldane 1932), Jaynes's for complete ignorance of a share (1968). Each is unchanged by the exchange and has its
   median at the corner, ½ (Haldane's on any range of levels symmetric about it); below t = ¼ they hold ¼, ⅓ and, over
   three decades of odds either side, 0.42. Jaynes's own answer to Bertrand, ½, is from this paper's side a situated
   reader's answer from far off (§2).

   Von Mises's water and wine, the case Jaynes left open as overdetermined (Jaynes 1973, §8), shows the same structure,
   and his method gives an answer once one premise is added. In the form Mikkelson (2004) states it: a liquid is wine
   and water, the ratio x of wine to water between 1/3 and 3; what is the chance that x ≤ 2 (von Mises 1928)?
   Indifference over x gives 5/8 and over 1/x gives 15/16, each favouring one liquid, and any answer between ½ and 1 can
   be had (Deakin 2006, as Parker and Jeynes 2023 report it). Answers that treat the two liquids alike, 5/6 (uniform in
   the share of wine; Mikkelson 2004), about 0.764 (uniform along the hyperbola xy = 1; Burock 2005, as stated by
   Gerville-Réache 2016), the mean of 5/8 and 15/16, 25/32 (which Mikkelson considers and rejects), and the levels and
   the uniform turn of this paper, 0.815 and 0.847, all put the chance of x ≤ 1 at ½, the corner, and part past it.
   Parker and Jeynes (2023) reach 0.816 from scale invariance through Benford's law (Benford 1938) and maximum entropy,
   by a law that does not treat the liquids alike. Nothing in the statement fixes the unit in which either liquid is
   measured, and a change of one liquid's unit multiplies x by a constant. If, as Jaynes required of the chord, one law
   is to hold on every range of x (its restriction to a smaller range is the law there), a premise the problem does not
   state, then a law unchanged by such a change is a power of x, and the exchange of the liquids leaves dx/x alone, the
   levels, and the answer ln 6/ln 9 ≈ 0.815. The mean of 5/8 and 15/16 is also unchanged by the unit, but it is no
single law: it weighs its two parts afresh on each range. In Jaynes's own form (at least half wine; what is the chance
   of at least three-quarters?) the range of x is unbounded, and no proper law on it is unchanged by a change of unit:
   his overdetermination. Bounded at 2^L, the levels give 1 − (log₂ 3)/L, so an answer needs the range held. With volume
   agreed beforehand as the common unit, the writer's uniform share, 5/6, is available instead; the problem's statement
   does not say which reading von Mises meant.
3. *No measure on a level.* Is there a principled reason a level could not carry a measure before anything arrives?
4. *Reciprocal symmetry.* Proposition 2(b) needs the reading to treat both sides alike although the reader's knowledge
   does not. Is that more than a choice?
5. *Uniformity as the weight.* Now part of question 2: the argument of §7.5 moves the burden of the uniform turn to "why
   the circle", and the two are one question about the measure on directions.
6. *V = H.* Dissolved for readers; open where something else is. A reader holds one length and has no V, so whether it
   draws V = H is not a question that arises for it: its circle is its one length turned (Proposition 3(c), (g)), and
   V = H is the writer's name for that circle. Where a drawing does have two axes, a page, a chart, a shore or an
   instrument, c = 1 is required for the turn (Proposition 3(e)) and for the Cauchy, forward and working back from it
   (Proposition 5(d)). That the construction works is shown where it is used: triangulation from two standpoints
   (Proposition 11) reads every direction on one length, and it is how surveying and astronomy measure distance;
   Mercator's chart, on which navigators have laid compass courses since 1569, has c = 1 at every place (Proposition
   5(g)). What stays open is empirical, and this paper does not take it up: whether a particular reader's sweep, an
   eye's, a brain's or an instrument's, is a turn, and whether what its readings are taken through imposes a c (unequal
   gains, pixels that are not square). That a reader should sweep by a turn of its one length, with nothing imposing a
   c, is what the propositions show, in the sense of Jaynes's principle, which says what a reader should assign given
   what it does not know, not what any reader does. Only that makes the directions from the standpoint a turn, with one
   uniform sweep (Proposition 3(e)). Only it lays the readings out before anything arrives with the corner at their
   median and the near field exactly a half (Proposition 5(d)), keeps every pair's corner however many parties are held
   (Proposition 5(e)), and keeps the angles from the standpoint (Proposition 5(f), (g)). Readings taken through a
   stretched drawing hold a consistent picture without these. The estimate of the true size is Proposition 13's: the
   median of what the reader knows, and H when what it knows is symmetric in levels about H. If the error of that
   estimate is to be unchanged when the size and the estimate are rescaled together, and alike for larger and smaller,
   it is a function of the error in levels (§12.1), and with absolute loss the best estimate is the median. What remains
   open is the group itself.
7. *Measures that cannot be normalized.* The reader's measure for the other's size, dκ/κ, has no total over all sizes,
   and such measures on a nuisance can produce the marginalization paradoxes of Stone and Dawid (1972) and Dawid, Stone
   and Zidek (1973). One reasoner integrates the nuisance out of the full data; another reasons from statistics whose
   law does not involve it; no prior lets the second reproduce the first. The paradox does not reach the reader's size,
   for a reason that is short to state. Let the data be amounts y = η·w, a vector of n, with w drawn from a joint law
   f(w | ζ) whose parameter ζ no rescaling touches, and η a scale. Under the nuisance measure dη/η the first reasoner's
   likelihood for ζ is ∫ η^(−n−1) f(y/η | ζ) dη, which the substitution η = 1/λ makes ∫ λ^(n−1) f(λy | ζ) dλ. The second
   reasoner uses the data's direction u = y/|y|, which no η touches; its law is found by setting η = 1 and integrating
   the length r = |y| out with its Jacobian, ∫ r^(n−1) f(r·u | ζ) dr, and putting r = λ|y| shows this is |y|^n times the
   first. So under dη/η the two reasoners reach the same conclusion about ζ with the same prior, whatever the law f and
   whatever the signs of the data. In their own examples the paradox comes from other powers of η (in Stone and Dawid's
   exponentials, a uniform prior on the rate); in some laws, a gamma for one, another power produces no paradox but
   moves the prior on ζ instead. This is their group condition as Jaynes (1980) reports it: the paradox is avoided by
   the nuisance's own invariant measure. The reader's size is such a nuisance, and dκ/κ is the one invariant measure its
   rescalings have; with it a reader that integrates the size out of amounts concludes what a reader of the data's
   direction alone concludes, the ratios with their overall sign: the address reading of Theorem 6, met from the side of
   inference. Two cautions. Which of the location-and-scale family's two measures avoids the paradox depends on what is
   of interest: with μ/σ of interest the nuisance σ at fixed μ/σ carries dσ/σ, which is dμ·dσ/σ² in (μ, σ), Jeffreys's
   rule, while dμ·dσ/σ, Jaynes's, produces the paradox there; §2's note that later work favours the right-invariant
   measure holds where the location or the scale is of interest. And whether the paradox shows improper measures
   inconsistent at all is disputed (Jaynes 1980; Wallstrom 2003); the reader's lay is in any case finite, its levels
   counted.

8. *Systems within systems: a speculation.* The two sweeps are the geometry of a standpoint and of the circle through
   it, the one laid from a point of that circle and the other about its centre, and a thing read is itself a centre with
   circles of its own. A room holds things as a house holds rooms (§11, "A worked example of the tower"). That suggests
   systems nested in systems, each with its own writer, a box of its own extents, and its own standpoints within it: the
   readings alike at every level, since no reading carries a scale, and the writers not, each written from the one
   outside it by a ratio read one level up, with one amount at the top. It suggests too that every standpoint is within
   the box that holds it, with everything else that box holds, and outside each of the others, reading their outlines and
   never their interiors, and read the same way in return. None of this is shown here. The levels of a reader's lay do
   not recurse: each lay keeps one corner and plain doublings (§6). Whether observation is recursive in any stronger
   sense, and whether the world is so arranged, the geometry does not prove and no reading could confirm; we note it as
   speculation.

If the principle of §12.1 stands, questions 1 and 2 become one: whether a situated reader's ignorance is exactly these
three transformations.

**Where the conclusions do not follow.**
- An observer that holds two independent lengths, one for each party, reads with two axes and has a c; unless c = 1 it
  has no circle and no turn (Proposition 3(e)). It is a writer's page or an instrument, and lies outside the reader's
  framework rather than against it.
- A level with more structure than its two ends, their order and the reciprocal, such as a measure, allows other
  subdivisions than the halving, since (P2) fails.
- Plain proportion past the corner keeps true scale but cannot fit the far field on bounded addresses (§6).
- A reading that disturbs what it reads. Theorem 6(a) assumes that what arrives is the same whichever address meets it.
  Where meeting a thing changes it, as a quantum measurement does, the addresses are still laid, but nothing here says
  what then arrives at them.

### 12.3 Related work

The pieces are classical: the reciprocal x ↦ 1/x, the Cauchy as the projection of a uniform angle and its Möbius
invariance, Cauchy's functional equation, Klein's Erlangen programme (1872), and Jaynes's and Jeffreys's invariant
priors, the first of which this paper builds on (§2). Our use of Jaynes is conditional in the sense of the critics named in §1: the group is chosen, and with it the measure. What is ours is the group, and the reading of its invariant measure as the reader's addresses rather than as a belief. Directional statistics reads directions on bounded charts, where mean directions exist (Mardia and Jupp 2000); structural inference builds inference on the group that generates the data (Fraser 1968). Near neighbours in measured perception include Gilinsky's
perceived distance with a finite horizon (1951), Schwartz's log-polar map of visual cortex, proportional near the fovea
and logarithmic beyond (1977), and the number-line literature, from logarithmic-to-linear shifts (Siegler and Opfer
2003; Dehaene et al. 2008) to proportion judgment on bounded lines (Barth and Paladino 2011). Scales that are linear
near a unit and logarithmic far from it are common in practice, astronomy's asinh magnitudes among them (Lupton, Gunn
and Szalay 1999); what §6 adds is the join placed at the reciprocal's fixed point, where the two spacings agree. The
pair and its corner appear in two-path interference: with the paths' amplitudes in the relation of h to v, the fringe
visibility is at most 2hv and the which-path predictability is |h² − v²|, the sine and cosine of the facing, so that
their squares sum to at most 1 (Greenberger and Yasin 1988; Englert 1996). In the logarithm of the amplitudes' ratio
they are its sech and tanh (Bramon, Garbarino and Hiesmayr 2004), and the visibility is whole only where the two
amplitudes are equal, at the corner. Van Fraassen (2008) argues that the measurer's own position enters measurement
irreducibly, as the reader's does here. In terms of limits, a writer's account lets the resolution go to zero first and
then lets the count of things grow without bound; a situated reader has a fixed resolution and an unknown count.

What we claim is not the pieces but their reading as one structure, set by what a reader knows of two breadths, and in
particular that the Cauchy distribution is a situated reader's addresses, not its payload. Whether this is a better way
to compute anything is an engineering question we do not take up. The aim is to explain things that are known but not
well understood: why near and far seem to obey different mathematics, why logarithmic scales appear wherever a range is
too wide to hold in proportion, and why the Cauchy has a median but no mean.

### 12.4 What the geometry gives free

The last section left aside whether this is a better way to compute anything. What the geometry does offer engineering
is narrower and, we think, more useful: a baseline. Once the reader chooses H, its one length, some structures follow
with no further choice:
- a zoom, the value of H (§8);
- a split between near and far, the corner v = h, at 45° on the reader's circle, and on a page only at c = 1 (§4);
- readings no change of the world's size can move, since every reading is a ratio (Theorem 6(a), §9);
- given that the sweep is uniform, addresses for any number of things with no table and no count, the uniform turn's
  Cauchy (§7).

Others need one stated premise more, and are free once it is granted:
- precision far off, the lay past the corner, 1 + ln s or 2 − 1/s, given (S) (§6);
- a level of detail, given a fixed count K of addresses, which H then divides between the near field and the far (§8).

What hides what is not among them: it is the payload's, set by which surfaces are opaque (§3.7). Some systems built to
read or draw a world arrive at these structures by design, and the geometry lets each design be read against them: what
it adds, and what that costs. Appendix B reads a set of them against it: the depth buffer, the flat screen, a filter's
steady state, exact composition, hashing, tables fixed in advance, the centre of directions, and a dial over a list
without end.

This is a claim about where these structures come from, not about how well any system performs: a design that departs
from the geometry may be right to, for reasons the geometry does not see. Two limits apply. What comes free is the
readings, not the amounts: metres still cost one amount carried in (§9), and the geometry says only which amount and
why one is enough. And whether a given departure is worth its cost is the designer's question; the geometry only makes
it one that can be asked.

## Appendix A. Where the geometry already appears

The classical results below confirm steps of the main line without carrying any of them. Each is listed with the section
where it bears.

**Steps that close, and a new zero with two other parties** (§2). Repeating one step t from zero comes back to zero
after finitely many steps only if arctan t is a rational multiple of π, and for a rational t that holds only at home,
the corner and the horizon, t = 0, 1 and ∞ (Niven 1956); every other rational step never closes, and its multiples
spread uniformly round the turn (Weyl 1916). With two other parties the composition is of another kind. The directions
[h : v : v₂] form a projective plane, and no continuous group law lives on it, since a compact Lie group of positive
dimension has Euler characteristic 0 and the projective plane has 1; so a new zero there is a turn of space, composed in
the rotation group and acting on the directions, not a sum of directions.

**Archimedes' proof, the writer's and the reader's** (§3.4). Archimedes measured the circle from both sides
(*Measurement of a
Circle*). A polygon inscribed in the circle falls short of it and one circumscribed about it exceeds it; doubling their
sides from 6 to 96 squeezed π between 223/71 and 22/7. Both polygons need the circle in hand: the inscribed one's
corners lie on it and the circumscribed one's sides touch it. His proof is the writer's, both sides held at once.

The inscribed measure equals his inscribed polygon in number. An inscribed polygon of n sides has perimeter
n·sin(π/n) against the circle's π (both for a diameter of 1), and with θ = π/n that ratio is sin θ/θ. So the measure at
the quarter turn, 90°, is the polygon of 2 sides, 2/π; at 45° it is the square, 0.9003; and halving the turn matches his
doubling of the sides, each step bringing the measure about four times closer to 1:

| sides | turn θ | inscribed, sin θ/θ | short of 1 by |
|---|---|---|---|
| 2 | 90° | 0.6366 = 2/π | 0.3634 |
| 4 | 45° | 0.9003 | 0.0997 |
| 8 | 22.5° | 0.9745 | 0.0255 |
| 16 | 11.25° | 0.9936 | 0.0064 |

A situated reader draws neither polygon. Both need the circle in hand, and it does not hold the circle: the inscribed
polygon's corners lie on the circle just as the outer polygon's sides touch it. What it has is the turn from home. Its
measure sin θ/θ is a measure of that turn, not a polygon laid on a circle; it equals the inscribed polygon's share in
number, but no polygon is held. The central measure comes the same way, as a number, through the reciprocal,
θ/sin θ = 1/(sin θ/θ): π/2 at the limb from the turn alone, and π/2 · 2/π = 1 stands in for the circle that is not held.
(Archimedes' outer polygon goes as tan θ/θ rather than θ/sin θ; both lie above 1 and close on it at the same rate.)
Archimedes squeezed π between two polygons because he held the whole; a situated reader holds neither polygon and has
the same numbers from the turn and the reciprocal. The convergence is ordinary geometry; what the vantages add is what
each holds.

The turn gives the halvings without a polygon. Halving a turn takes out one cosine, sin 2θ/2θ = cos θ · sin θ/θ, so the
inscribed measure at the quarter turn is a product with one factor per halving, the first at the corner:

  2/π = cos 45° · cos 22.5° · cos 11.25° · … = (√2/2) · (√(2 + √2)/2) · (√(2 + √(2 + √2))/2) · …

This is Viète's formula (Viète 1593). After n factors the product is 2/π divided by the share of the inscribed polygon
of 2ⁿ⁺¹ sides, so it closes on 2/π at Archimedes' rate, about four times closer with each halving: 0.7071, 0.6533,
0.6407, 0.6376, ….

**Order and distance on the arc** (§4). Order on the arc is projective too. Of two readings [h₁ : v₁] and [h₂ : v₂], the
second lies farther from home exactly when the bracket D = v₂h₁ − v₁h₂ is positive. D is zero when the two are one
direction, and a linear change of the drawing multiplies it by its determinant, so the order survives every drawing that
keeps the sign. With the dot product it accounts for the pair: D² + (h₁h₂ + v₁v₂)² = (h₁² + v₁²)(h₂² + v₂²), Lagrange's
identity in two dimensions, and only D's sign tells which way round the two lie. The order chains without a quotient:
for three readings A, B, C, D(A, C)·h_B = D(A, B)·h_C + D(B, C)·h_A (the three-term Plücker relation among 2 × 2 minors;
Plücker 1865), so with every h above zero, B past A and C past B put C past A. Home and the horizon fix a distance as
well as the corner: the logarithm of the cross ratio of two readings x and y against home and the horizon is ln(x/y),
Hilbert's projective metric on the open arc (Cayley 1859; Klein 1871; Hilbert 1895). It gives the levels' distance its
form, a count by ratio, and fixes it only up to a factor: no projective fact supplies the base.

**The Cayley transform, and the square that takes a centre to a focus** (§4). The two sweeps are also one classical map.
The Cayley transform w = (z − i)/(z + i) carries the upper half-plane onto the disc and the line onto the circle (Cayley
1846). It sends the reading s = tan θ to w = −e^(2iθ), the point of the circle 2θ round from the image of zero, and the
standpoint i to the centre (zero, s = 0, lands at −1 and the horizon at +1: the landmarks of the Thales circle turned a
half turn). So the inscribed reading at θ and the central angle 2θ are one point under the map, and the
uniform turn about the centre is carried onto the Cauchy law on the line: the Cauchy is the harmonic measure from i, the
circle's uniform measure seen from its centre, written in the line's coordinate. The square that carries θ to 2θ also
carries one figure to another. Under w = z² an ellipse centred at the origin, z = a cos t + i b sin t, becomes a conic
with a focus at the origin, |w| = ℓ + e·Re w with ℓ = 2a²b²/(a² + b²) and e = (a² − b²)/(a² + b²), w going round once
while z goes round twice (Bohlin 1911; Levi-Civita 1920). The doubling of the angle that separates the two sweeps is the
same square that takes a figure's centre to its focus.

**Cauchy's functional equation, twice** (§5, §6). Two steps of the main line are Cauchy's functional equations
(Cauchy 1821). The uniform sweep of Proposition 3(g) is a one-parameter group, Φ(t₁ + t₂) = Φ(t₁)Φ(t₂), the equation in
its exponential form for matrices, whose continuous solutions are Φ(t) = exp(tA). Because the sweep returns after a full
turn, exp(TA) = I, the rate is imaginary, ±iω, and in the sweep's own inner product the bar's attitude is
h + iv = e^(iωt), Euler's formula. It is the return that makes the rate imaginary; the one length fixes only the factor
left free in that inner product. The scale invariance (S) of Proposition 4 gives f(λμ) = f(λ) + f(μ), the equation in
its logarithmic form, whose increasing solutions are k·ln λ. Each needs its regularity condition, continuity of the
sweep in the one and monotonicity of the lay in the other; without it the equation has other solutions, as the
Hamel-basis example in Theorem 6's proof shows for the additive form. In the exponential form three layers are kept
apart. Assumed: the sweep is continuous, composes (every step the same linear map) and returns. Derived from these: the
imaginary rate, an inner product the sweep preserves, unique up to its factor (it is not assumed, Proposition 3(g),
step 3), and Euler's form. This paper's reading: the return is what the reader's turn supplies, so i enters as the
generator of a returning turn, not as an added ingredient. That a returning one-parameter group has an imaginary
generator is classical; Euler's formula and identity are used, not derived. The Cauchy distribution's name has another
origin, his exchange with Bienaymé in 1853 (Stigler 1974).

**π_p** (§5). Among the p-norms the circle is also the extreme case. Measured in its own norm, the unit circle of ℓ_p
has half-perimeter π_p, which is 4 at p = 1 and as p → ∞ (the line's norm and the square's) and least, π, at p = 2
(Adler and Tanton 2000); and π_p = π_q whenever 1/p + 1/q = 1 (Keller and Vakil 2009). The sum norm and the
largest-component norm are such a pair, dual to each other, and both give 4; the Euclidean norm is the one that is its
own dual. This is classical and nothing here rests on it; it says that the norm the rigid bar needs is the one fixed
point of that pairing.

**What square roots reach** (§5). The constructions agree. Halving a turn needs one square root, tan(θ/2) = (√(1 + t²) −
1)/t, so square roots reach tan(π/2ᵏ) from the corner at every level; other divisions are not all in reach, since
tan(π/7) and tan(π/9) have degree 6 over the rationals and no ruler and compass divide a half turn into seven or nine
(Wantzel 1837, completing Gauss).

**One ratio repeated** (§5). Levels given by a ratio must be one ratio repeated: every discrete set of rescalings closed
under composing is the powers of one factor g, since under the logarithm it is a discrete subgroup of the line, the
multiples of one step. Two factors whose logarithms are incommensurable, 2 and 3, generate rescalings dense in every
range, and no levels at all. The levels' form is forced; which g is not.

**The Cauchy from one length** (§5, §7.1). Every piece of the mathematics here is classical. A circle needs one length:
it is everything at a fixed distance from a centre, and one length turned about its end traces it. The tangent of an
angle turned uniformly is Cauchy; that is the lighthouse problem of the Bayesian textbooks (Gull 1988; Sivia and
Skilling 2006). Projecting the circle from one of its own points onto a line, the stereographic projection, carries its
uniform measure to the Cauchy (§4), and the family is closed under the Möbius maps of the line (Knight 1976; McCullagh
1996); its median, its symmetry under the reciprocal and its missing mean are textbook facts. None of these mentions a
second breadth, and none needs one: the slope v/h is already a ratio of two shares of one radius, so its absence is
never remarked. What this paper adds is the reading of who holds what. The reader holds one length, H, and never knows V (§3.8): V
and c belong to a writer or to a drawing with two axes, and V = H is the writer's name for the reader's circle (§5).
Each feature of the Cauchy is then a feature of the circle that survives without V: the corner is the median, the
near and far halves are mirrored by the reciprocal, and the missing mean is what the absent V leaves, the far end being
the horizon, a direction and not a place, with nothing to average toward. A writer, holding V, has its far end as an
amount: no horizon, and the corner only a point. We did not find this assembly in print; the pieces are classical.

**V = H under other names** (§5). Every field that reads directions through something with two axes draws its parties
at one length, the reader's circle written with two axes, under its own name:
- *Standardizing.* The correlation coefficient (Pearson 1896) divides each variable by its own spread before the two
  are compared, and the z-score does the same for one. For two normal variables of spreads σ_i and σ_j, at any
  correlation, the ratio X_j/X_i is a Cauchy whose absolute value has its median at σ_j/σ_i: the drawing V = cH with
  c = σ_j/σ_i, the corner moved to c. Standardized, the median is 1 at every correlation, since the standardized pair is
  unchanged by exchanging the two variables, and Theorem 6(e) does the rest.
- *Whitening.* Mahalanobis's distance (1936), and the map x ↦ Σ^(−1/2)x, draw every axis at one length and at right
  angles, the inner product of Proposition 3(g). Whitening is unique only up to a turn, which is the part of the
  reader's ignorance the drawing leaves free.
- *Principal components and canonical correlations.* Components are taken from the correlation matrix, the standardized
  variables, when units differ (Hotelling 1933); from the covariance matrix the axis drawn longest takes the first
  component. Canonical correlations (Hotelling 1936) whiten each set before reading the angles between them, and so are
  unchanged by every change of units within a set.
- *Charts and lamps.* Mercator's chart is the one that keeps every bearing true, and a lighthouse's 45° flash marks the
  corner of its landings, both only at c = 1 (Proposition 5(g), (f)).
- *Graphs.* A line at 45° means "equal" only on equal axes. Cleveland, McGill and McGill (1988) chose a graph's aspect
  ratio so that the orientations of its segments centre on 45°, "banking to 45°", for the eye's accuracy in judging
  slopes: choosing the drawing so that the middle direction is the corner.
- *Instruments.* Square pixels, and the two cameras of a stereo pair calibrated alike, draw the two directions, or the
  two standpoints, at one length.

Where the drawing is skipped on purpose, amounts are being read. Variables already in one shared unit need no
standardizing, since the unit has made c = 1. An equal-area map keeps areas, not bearings. A weighting of features
chosen for a task sets c on purpose. Each field found c = 1 for its own purpose; the common reason is the one of §5.

**Three numbers, three rulers** (§6). The three curves are the unit sets of the only three real number systems of two
dimensions with a unit: the complex numbers (j² = −1), whose units e^(jθ) = cos θ + j sin θ run round the circle; the
split-complex numbers (j² = +1), e^(jζ) = cosh ζ + j sinh ζ on the hyperbola; and the dual numbers (j² = 0), e^(jx) = 1
+ jx on the tangent line. In each, multiplying units adds the ruler's own coordinate, θ, ζ or x (Yaglom 1968). So each
ruler is the one along which its own numbers multiply by adding: the writer's line is the flat case, the turn and the
hyperbolic angle the two curved ones.

**The angle doubling** (§6). The angle doubling carries the uniform turn's law onto itself, since it doubles a uniform
angle, yet it is two to one and moves cross ratios: it keeps the Cauchy without being a Möbius map (Pitman and Williams
1967), while the doubling of scale is one of them.

**Why the payload is Gaussian** (§7.1). Let the payload at the reader have two components, X on h's side and Y on v's, as
amounts; its reading is their ratio, s = |Y|/|X|, which keeps the direction and drops the size. Two premises are needed,
and the paper's own do not supply them. The first is that the payload's law is unchanged by every turn. That the reader
cannot detect its own turns (Proposition 3(e)) is a fact about what the reader knows, not about the payload; it makes
the turn-invariant law the representation an ignorant reader should choose, in Jaynes's sense (§2), and that is all it
does. The second is that the two components vary independently. Given both, the payload's law is the isotropic normal,
the only law of two independent components that every turn leaves unchanged (Herschel 1850; Maxwell 1860). Three things
follow, each classical.
- Its direction is uniform over the turn, so its reading is the half-Cauchy of (b), P(s ≤ r) = (2/π)·arctan r, with its
  median at the corner. The normal payload's ratio has the addresses' law.
- Its size, √(X² + Y²), is independent of its direction. What arrives and where it is addressed separate exactly:
  Theorem 6(a), seen from the payload's side.
- With unequal spreads, σ_v ≠ σ_h, the reading is still a half-Cauchy, of scale σ_v/σ_h, its median there: (d) with
  c = σ_v/σ_h. Equal spreads are the drawing c = 1, the reader's circle. With the payload's centre off the origin the reading is no longer a
  Cauchy at all, and its median leaves the corner (with the centre at (0, σ), to 1.515).

The central sweep reads the payload, which has a mean (each component's size averages √(2/π)·σ); its ratio, which has the
addresses' law, has none (its mean up to s is (1/π)·ln(1 + s²), growing without limit). The two routes to the
Cauchy are kept apart. The address law of (b) is the sweep's own: it needs only the uniform turn and holds whatever the
payload is, Gaussian or not (Theorem 6(a)). The normal payload is a second route that arrives at the same law, a model
consistent with the addresses, not their cause. The paper does not claim that payloads are Gaussian, only that if a
payload's law is taken to be unchanged by turns, with independent components, it is the normal, and its ratio is then
the Cauchy the addresses already were. The central limit theorem is a third matter: it makes a sum of many independent
contributions normal, and says nothing about a single payload averaged over the quadrant.

**The one chart that keeps lines straight** (§7.1). The gnomonic projection is the one chart that keeps lines straight:
a map from part of the sphere to the plane that sends every great circle to a straight line is the gnomonic projection
followed by a projective map (Beltrami 1865), so asking that things in one line read as one line forces the reading v/h,
up to a projective change of the drawing.

**Planes of directions** (§7.1, §7.2). A reading of one direction is a point of projective space, the Grassmannian of
lines through home; a frame of k directions held at once is a plane through home, a point of the Grassmannian of
k-planes. Its rotation-invariant measure, in the chart where a k-plane is the column space of [I ; X], has density
proportional to det(I + XᵀX)^(−n/2), the matrix-variate Cauchy (Dickey 1967); for k = 1 it is the law of
Proposition 5(e) and "More parties". One rank up the two halves of the main result come apart. Every entry of X is a
standard Cauchy for every k and n (it is a normal divided by the length of an independent normal), so every coordinate
keeps the turn's law. The plane's own readings are the tangents of its principal angles θ_i to a reference plane (Jordan
1875), and they keep the corner only through the exchange: where the plane is half the space (n = 2k), swapping the
reference plane with its complement sends each θ_i to π/2 − θ_i, so the product of the tangents has its median at 1;
that product is not a Cauchy (for k = 2 its law is ½(1 + |r|)⁻²), and without the exchange the corner is not its median.
The corner as median is Theorem 6(e)'s, from a reciprocal symmetry; the exact Cauchy belongs to single directions. The
principal angles have density proportional to ∏_{i<j}|cos²θ_i − cos²θ_j| (from the singular-value Jacobian), and the
chance that all k lie inside the corner is a ratio of two Pfaffians of elementary integrals (de Bruijn 1955): ½,
½ − π/8, ¼ − 3/(4π), 19/256 − 3π/128 for k = 1 to 4, falling as 2^(−k²/2) to leading order, the rate of a repelling gas
confined to half its range, by the Coulomb-gas method of Dean and Majumdar (2006). A frame keeps its near field whole less often the more it holds at
once, faster than geometrically.

**A shape as a function on the circle** (§7.4). Holding a star-shaped outline as one radius per direction, r(θ) on the
unit circle, is classical: it is the outline's radial function, its polar coordinates. So is describing it by the
Fourier series of that function, or of its tangent angle along the outline, made blind to size, position and turn by
normalising (Fourier descriptors; Zahn and Roskies 1972), and so is taking a shape as what is left when position, scale
and rotation are removed (Kendall 1984). For a convex body the support function on the circle or sphere plays the same
part, and the areas carried by its outward normals fix it up to translation (the Minkowski problem, Minkowski 1903; in
vision, the extended Gaussian image, Horn 1984). In three dimensions, series of spherical harmonics in the radius
describe planets and asteroids. What §7.4 adds is where each part of the function comes from. The directions are the
addresses, the same for every shape. The radius along each is an amount, the payload, had only by ranging (a writing) or
from further standpoints. In ln r = a₀ + f(θ) the constant a₀ is the one term no ratio of radii reads, so the
normalisation the descriptors make by choice is here what reading leaves. The terms of f, taken in order of n, are a
level of detail. The classical treatments begin with r(θ) in hand.

**A median in two registers** (§7.6). To a stated accuracy less is needed: a running estimate moved by the sign of each
comparison alone, m ← m + a_k·sign(x_k − m) with steps a_k falling more slowly than 1/k, and averaged as it goes,
reaches the sample median's own accuracy with two registers (Robbins and Monro 1951; Polyak and Juditsky 1992; for the
Cauchy √n times its spread tends to π/2 in the scale's unit).

**The doubling map** (§8). Read on the line alone, the step is the doubling map x ↦ 2x mod 1: each step moves the first
digit of the remainder into the key, and the rate at which the map forgets where it started, its Lyapunov exponent, is
ln 2, one level a step (the Bernoulli shift).

**Odd and even K** (§8). For even K the corner is a boundary between two addresses; for odd K one address is centred on
it, its ends reciprocal (K = 9: from 0.8391 to 1.1918 H). The two are the mid-rise and mid-tread quantizers (Gersho and
Gray 1992), and both are unchanged by the exchange.

**Boyd's points and Chebyshev's nodes** (§8). The same points are known in numerical analysis. Boyd's collocation points
for a function on the whole line, L·cot((2j − 1)π/2N), j = 1, …, N, are the midpoints of N equal shares of the Cauchy of
scale L, and their positive half are the K addresses' midpoints along distance, H·tan((2k − 1)π/4K), with L = H and N =
2K; doubling L lays the grid again at twice the length. His rule for L, set it at the scale of the feature to be
resolved (Boyd 1982), is the rule above that the best H puts the thing read at the corner. His basis is Chebyshev's on
the turn, T_n(y/√(y² + L²)) (Boyd 1987): the same equal angles read by their cosine are Chebyshev's nodes, crowded at
the ends of the chord (the last gap about π²/N², the middle ones π/N; Rivlin 1974), and read by their tangent are the
Cauchy's, spread out to the horizon. The law is the turn's; the chart decides where the addresses crowd.

**Euclid's Book V: a geometry of ratios** (§9). Euclid's *Elements* never assigns a number to a length. A ratio is
"a sort of relation in respect of size between two magnitudes of the same kind" (Book V, definition 3), and the theory
of proportion that Book V owes to Eudoxus (definition 5) compares ratios without measuring either term; the plane and
solid geometry of the *Elements* is built on it. So a whole classical geometry was carried in ratios, with no unit
length, which is the regime §9 calls sufficient: magnitudes of one kind compared with each other, nothing compared with
an amount from outside.

**Descartes's unit segment** (§9). In *La Géométrie* (1637), Book I, Descartes chooses one line as unity so that the
product of two lines is again a line rather than an area, and the quotient a line rather than a ratio; with it, lengths
are handled as numbers, added and multiplied. The unit enters to do arithmetic on lengths: sums of amounts and products
read as lengths, the third of the capabilities §9 lists, bought with one chosen length.

**Paper sizes, ISO 216** (§9). One constraint states the system: a sheet cut in half across its long side keeps its
shape. Halving sends a sheet's aspect r to 2/r, so in units of √2 it is the reciprocal, and the only shape it keeps is
its fixed point, r = √2, the corner of that exchange; a sheet off it alternates between two shapes whose geometric mean
is √2. Every breadth of the series is then a ratio to the sheet, and the series is written by one amount, A0's area of
1 m²; the B series is the same system written with a second amount (B0's short side 1 m) and the C series with their
geometric mean. All 33 listed sizes of each series come from those amounts and one rule, the long side halved and
rounded down to the millimetre (ISO 216; ISO 269). Ratios state the system; the amounts let sheets, envelopes and
machines made apart meet, the second capability of §9.

**Buckingham's π theorem** (§9). A law among n quantities whose units come from base units of rank r in the
dimension matrix is a law among n − r dimensionless groups, the invariants of the unit changes (Buckingham 1914;
Bridgman 1922; Barenblatt 1996). With one base unit, length, the change is x ↦ λx, and its invariants are exactly the
directions [x₁ : … : xₙ]: the positive orthant's projective space, the wedge of §2. So in one dimension the π groups
are the addresses, and Proposition 8 is the theorem read from a standpoint. The rank counts the amounts to carry in:
r of them, independent in the dimension matrix, write every quantity; with fewer a family of worlds is left with the
same groups. In this paper's geometry r = 1, the one amount of §9. The theorem says nothing about the law on the groups:
unit changes act trivially there, so every law on the directions is equally scale-invariant, and the uniform turn's
Cauchy, with its median at the corner, comes from the turns and the exchange (§2), not from dimensional analysis. With
several base units the groups split into one wedge per unit only when each quantity carries a single base unit; in
general they mix units.

**An unnormalized density** (§7.3). A weight vector known only up to its normalizing constant is an array of the
third kind, its values without their common factor. The sampling algorithms built for it use only ratios of entries:
Metropolis's acceptance test compares p(x′)/p(x), so the constant cancels and rescaling every weight changes no step of
the chain (Metropolis et al. 1953; Hastings 1970). Computing the constant, an evidence or a partition function, is the
writing step. Ranks and ratios survive the unknown factor and sums need it, as Theorem 6 says.

**Geometric growth** (§5, §7.3). A dynamic array that grows its capacity by a factor g at each reallocation copies in
all fewer than gN/(g − 1) elements over N appends, whatever g > 1 is: its reallocations fall at the levels g, g², …,
and their costs form a geometric series. Growth by a fixed step copies in proportion to N per element. So the levels
must be one ratio repeated for the cost per element to stay constant, and which ratio is a choice: implementations use
2 or 1.5.

## Appendix B. Engineering read against the geometry

The structures of §12.4 met in systems built to read or draw a world, each with what it adds:
- *The depth buffer.* A perspective depth buffer stores (f/(f − n))·(1 − n/d) for a point at distance d between the
  near and far planes n and f. With H = n this is the in-place lay, 2 − n/d, less its constant 1, rescaled: setting the
  near plane is choosing H, the near field inside it is discarded, and precision runs out far off because every
  address there has already been spent toward the horizon. Logarithmic depth in its plain form, ln(d/n)/ln(f/n), is the
  reader's lay past the corner with its corner at the near plane; the form ln(Cd + 1)/ln(Cf + 1), proportional below
  d ≈ 1/C and logarithmic above, is a smooth form of the whole lay, near field and far, turning at d ≈ 1/C, as §6's
  hyperbolic angle smooths the reader's lay.
- *The flat screen.* Equal pixels on a plane are not equal turns. Per unit of screen area the uniform turn's directions
  have density (2/π)·cos³α (Proposition 5(e)), so equal pixels over-weight the directions off the axis by sec³α, and
  along one line of a screen of finite edge they put the median at half the edge instead of at the corner (§3.5). The
  weighting is the design's, added to the geometry. Laid by turn instead, an arctangent on each coordinate of a cube's
  face (the equi-angular cubemap), the cells' solid angles vary by a factor of √2 across a face, against 3√3 ≈ 5.2 for
  equal pixels. However the faces are laid, a direction in d + 1 dimensions is never more than arccos(1/√(d + 1)) from
  the axis of the face it falls on (45°, 54.74° and 60° for one, two and three other parties), since its largest
  component is at least 1/√(d + 1); every capped reading lies within √d of its face's centre.
- *A filter's steady state.* A Kalman filter tracking a random walk, with process noise q and measurement noise r,
  settles with its predicted and updated variances at √(qr)·μ and √(qr)/μ, μ = (n + √(n² + 4))/2 with n = √(q/r)
  (Kalman 1960): a reciprocal pair about √(qr), the corner of the two noises, their product qr whatever n. For matrices
  the same holds as P⁻ # P = Q # R, with # the matrix geometric mean. The design supplies the noises; that its two
  variances sit at reciprocal readings about their geometric mean is the geometry's.
- *Exact composition.* Readings composed by tangent addition can be held exactly as Gaussian integers, the step v/h as
  h + iv, reduced after each product. The register then grows by ½·log₂ of the odd part of h² + v² bits a step, and not
  at all only at home, the corner and the horizon: every other step costs storage without end, the arithmetic face of
  the steps that never close (§2, "Zero, and a new zero").
- *A step that never closes.* Hashing by an irrational fraction of a turn, the golden one in Fibonacci hashing
  (⌊2³²/φ⌋ = 2,654,435,769; Knuth 1998, §6.4), uses just such steps: their multiples spread round the turn, leaving at
  most three sizes of gap at every count (the three-distance theorem; Sós 1958).
- *Addresses on a turn, not by a count.* Consistent hashing puts keys and machines on a circle by angle, each key served
  by the next machine round (Karger et al. 1997); adding a machine moves about one key in n + 1, where placing keys by
  their remainder on division by n moves nearly all of them. Labels drawn from a fixed count M are the other side: kept
  in order with new items put between, one gap can take about log₂ M before labels must be given out again (Itai,
  Konheim and Rodeh 1981; Dietz 1982). A count of addresses fixed beforehand runs out where the world's count grows; the
  turn's addresses do not, and pay with a horizon (§8).
- *Tables fixed in advance.* A sampling table or a grid of cells fixed in advance must know beforehand the extent it
  covers and the resolution it needs, and is rebuilt when either changes. The uniform turn's addresses need neither (§8,
  "A fixed count, aimed by H"); what needs them is the payload or the writer.
- *The centre of directions.* Where the readings themselves fall as the uniform turn's law, as the addresses of a sweep
  do, their tangent chart has no mean and the median is the law's own centre (Theorem 6); a fit that averages them on
  that chart has nothing to settle on. Measurement errors are another law, which the geometry does not fix.
- *A dial over a list without end.* The three rulers of §6 can be run as a control. Let a held push add to the
  hyperbolic angle ζ at a steady rate r, and place the hand at the reading x = sinh ζ = tan θ, drawn at the turn θ = gd ζ.
  The screen holds the turn, a quarter turn whatever the list's length; the hand is at x after asinh(x)/r, so each
  doubling far out costs the same ln 2/r of holding, and any place up to N is reached in about ln(2N)/r (a list of 2⁵³,
  37.4/r). The far end is the horizon, at the edge of the turn and never drawn. Letting go makes the place reached the
  new zero, and pushes compose by adding in ζ, so no count accumulates in the control. The window, how many places one
  rung holds, is a zoom, as H is (§8). What the list holds at each place can be made from the place itself, since the
  addresses do not depend on N. In two dimensions, pushes that are true boosts do not commute: a loop of them brought
  back to rest leaves the frame turned by the area it enclosed (Thomas 1926), a turn the design must show or cancel;
  pushes in log-ratios, which add, commute. The design adds the rate and the window; the place, the corner and the
  horizon are the
  geometry's. Zooming interfaces arrive at relatives of this: speed coupled to zoom (Igarashi and Hinckley 2000),
  views as points of position and scale (Furnas and Bederson 1995), and smooth zoom-and-pan paths written in the
  hyperbolic functions (van Wijk and Nuij 2003).

## Appendix C. Notation

| symbol | kind | meaning |
|---|---|---|
| h, v, v₂ | unit relations, from 0 to 1 | for the reader, shares of its one length H; for a writer, h relates to H, v to V, v₂ to V₂; a relation requires two, a circle has two, a sphere three; how many a system includes sets its shape |
| K | the reader's capacity | its whole count of addresses, fixed and prior to H; H splits it, half inside the corner and half past it; in direction its split is the corner, in distance H is the zoom; the reader interacts with K, the writer with N (§8) |
| H | the starting value | the reader's breadth, its thumb, and its only length: the one value it chooses to start the system, not a measured size; its value sets the zoom (§8) |
| V, V₂ | a writer's | the other parties' breadths, held only by a writer, who holds both hemispheres; the reader has none. V = H is the writer's name for the reader's circle (§5) |
| V* | an amount | a party's true breadth: never read; estimated (§9) or supplied from outside |
| v/h, h/v | geometry | the reading before and past the corner |
| θ, κ | what the reader does not know | its attitude, which way its bar points; the other's size relative to its own, κ = V*/H. Turns of θ and rescalings of κ leave dθ·dκ/κ unchanged; the exchange acts on readings and drawings, not on κ (§2) |
| m + iγ | geometry | a Cauchy law of the signed reading with median m and scale γ, as a point of the upper half-plane; the uniform turn on a two-axis drawing V = cH is i/c (§2, §12.1) |
| c, ĉ | a page's or an instrument's; an estimate | c: a two-axis drawing V = cH, never the reader's; c = 1 is the reader's circle (Propositions 3(e), 5(d)); ĉ: the estimate ĉH of the true breadth V*, an amount (Proposition 13) |
| a, ψ | geometry | altitude, from the horizontal up to the vertical (the sweep from all of h to all of v), and azimuth, round the horizontal from h to v₂ (the sweep that brings in v₂); v₂/h = tan ψ, v/√(h² + v₂²) = tan a (§2) |
| the corner | geometry | v = h |
| home | geometry | where the reader stands, the point its rays leave from; the lays of §6 put zero there |
| zero, the horizon | geometry | v/h = 0, all h, pointing at the other party; v/h → ∞, never reached |
| g | geometry | the sweep's progress, (2/π)·arctan(v/h), the uniform turn's distribution function: 0 at zero, ½ at the corner, 1 at the horizon |
| reading, writing | what an observer does | reading: in the unit relations h and v, with V unknown (situations 3, 4); writing: in amounts, with the breadths H and V known (situations 1, 2); situation 1 is common to both, the baseline of every vantage (§9); the writer's vantage dual-hemispherical, a reader's hemispherical, one reader with two sweeps, the inscribed (the addresses) and the central (where the paint lands) |
| address, payload | geometry; what arrives | a place laid before anything arrives; what arrives there: the finger and the coloured light on it |
| situations 0 to 4 | what a reader knows | §3.1: nothing; the circle; a shape; the central sweep, where the paint lands; the inscribed sweep, the addresses; with more parties, one entry per party |
| ℓ | an amount | the reach of what arrives along a ray (Theorem 6); it cancels from every reading |
| ε | a resolution | the reader's resolution, the least difference it tells apart, relative to what it reads (§8) |
| the shared unit | an agreement | something two readers can both read, agreed to count as 1 (§9); not a reading, and no part of the geometry |
| level | geometry | zero to the corner (the first); one doubling of v/h past it: a dyadic interval |
| quadrant, orthant | geometry | one way of facing the wedge, a sign for each freedom of a drawing; the wedge itself is the positive one |
| facing | geometry | the direction a reader faces as it sweeps; its turning draws the arc |
| denominator | geometry | the unit relation a reading divides by; v/h is read against h |
| in-place lay | geometry | position by length: v/h inside the corner, 2 − h/v past it |
| logarithmic lay | geometry | position by number of addresses: v/h inside the corner, 1 + ln(v/h) past it |

## References

Abbott, R. et al. (LIGO Scientific Collaboration, Virgo Collaboration and KAGRA Collaboration) (2023). Open data from
the third observing run of LIGO, Virgo, KAGRA and GEO. *Astrophysical Journal Supplement Series* 267, 29.

Aczél, J., Roberts, F. S. and Rosenbaum, Z. (1986). On scientific laws without dimensional constants. *Journal of
Mathematical Analysis and Applications* 119, 389–416.

Adler, C. L. and Tanton, J. (2000). π is the minimum value for pi. *The College Mathematics Journal* 31(2),
102–106.

Archimedes (c. 250 BC). *Measurement of a Circle*.

Archimedes (c. 225 BC). *On the Sphere and Cylinder*.

Aspden, R. S., Padgett, M. J. and Spalding, G. C. (2016). Video recording true single-photon double-slit interference.
*American Journal of Physics* 84, 671. Data: University of Glasgow Enlighten repository, doi:10.5525/gla.researchdata.281.

Barbier, E. (1860). Note sur le problème de l'aiguille et le jeu du joint couvert. *Journal de Mathématiques
Pures et Appliquées* (2) 5, 273–286.

Barenblatt, G. I. (1996). *Scaling, Self-Similarity, and Intermediate Asymptotics*. Cambridge University Press.

Barth, H. C. and Paladino, A. M. (2011). The development of numerical estimation: evidence against a representational
shift. *Developmental Science* 14(1), 125–135.

Beardon, A. F. (1983). *The Geometry of Discrete Groups*. Graduate Texts in Mathematics 91. Springer, New York.

Beltrami, E. (1865). Risoluzione del problema: riportare i punti di una superficie sopra un piano in modo che le
linee geodetiche vengano rappresentate da linee rette. *Annali di Matematica Pura ed Applicata* 7, 185–204.

Benford, F. (1938). The law of anomalous numbers. *Proceedings of the American Philosophical Society* 78(4), 551–572.

Bernardo, J. M. (1979). Reference posterior distributions for Bayesian inference. *Journal of the Royal Statistical
Society B* 41(2), 113–128.

Bertrand, J. (1889). *Calcul des probabilités*. Gauthier-Villars, Paris.

Bohlin, K. (1911). Note sur le problème des deux corps et sur une intégration nouvelle dans le problème des trois
corps. *Bulletin Astronomique* 28, 113–119.

Böröczky, K. (1974). Gömbkitöltések állandó görbületű terekben I [Sphere packings in spaces of constant curvature I].
*Matematikai Lapok* 25, 265–306.

Boyd, J. P. (1982). The optimization of convergence for Chebyshev polynomial methods in an unbounded domain.
*Journal of Computational Physics* 45, 43–79.

Boyd, J. P. (1987). Spectral methods using rational basis functions on an infinite interval. *Journal of
Computational Physics* 69, 112–142.

Bramon, A., Garbarino, G. and Hiesmayr, B. C. (2004). Quantitative complementarity in two-path interferometry.
*Physical Review A* 69, 022112.

Breit, G. and Wigner, E. (1936). Capture of slow neutrons. *Physical Review* 49(7), 519–531.

Bridgman, P. W. (1922). *Dimensional Analysis*. Yale University Press, New Haven.

Buckingham, E. (1914). On physically similar systems; illustrations of the use of dimensional equations. *Physical
Review* 4(4), 345–376.

Buffon, G.-L. Leclerc, comte de (1777). Essai d'arithmétique morale. In *Histoire naturelle, générale et particulière*,
Supplément, tome 4. Imprimerie royale, Paris.

Burock, M. (2005). Indifference, sample space, and the wine/water paradox. Preprint, PhilSci Archive 2487.

Cacoullos, T. (2014). Polar angle tangent vectors follow Cauchy distributions under spherical symmetry. *Journal of
Multivariate Analysis* 128, 147–153.

Cacoullos, T. and Papadatos, N. (2013). Self-inverse and exchangeable random variables. *Statistics & Probability
Letters* 83(1), 9–12.

Cauchy, A.-L. (1821). *Cours d'analyse de l'École royale polytechnique. Première partie: Analyse algébrique*.
Paris: Debure, ch. 5.

Cauchy, A.-L. (1841). Note sur divers théorèmes relatifs à la rectification des courbes et à la quadrature des
surfaces. *Comptes Rendus de l'Académie des Sciences* 13, 1060–1065.

Cayley, A. (1846). Sur quelques propriétés des déterminants gauches. *Journal für die reine und angewandte Mathematik*
32, 119–123.

Cayley, A. (1859). A sixth memoir upon quantics. *Philosophical Transactions of the Royal Society of London* 149,
61–90.

Civera, J., Davison, A. J. and Montiel, J. M. M. (2008). Inverse depth parametrization for monocular SLAM. *IEEE
Transactions on Robotics* 24(5), 932–945.

Cleveland, W. S., McGill, M. E. and McGill, R. (1988). The shape parameter of a two-variable graph. *Journal of the
American Statistical Association* 83(402), 289–300.

Coxeter, H. S. M. (1987). *Projective Geometry*, 2nd ed. Springer, New York.

Crofton, M. W. (1868). On the theory of local probability, applied to straight lines drawn at random in a plane.
*Philosophical Transactions of the Royal Society of London* 158, 181–199.

Cuadras, C. M. (2002). Geometrical understanding of the Cauchy distribution. *Qüestiió* 26(1–2), 283–287.

Dawid, A. P., Stone, M. and Zidek, J. V. (1973). Marginalization paradoxes in Bayesian and structural inference.
*Journal of the Royal Statistical Society B* 35(2), 189–233.

de Bruijn, N. G. (1955). On some multiple integrals involving determinants. *Journal of the Indian Mathematical
Society* 19, 133–151.

de Sarasa, A. A. (1649). *Solutio problematis a R. P. Marino Mersenne Minimo propositi*. Antwerp.

Deakin, M. A. B. (2006). The wine/water paradox: background, provenance and proposed resolutions. *Gazette of the
Australian Mathematical Society* 33(3), 200.

Dean, D. S. and Majumdar, S. N. (2006). Large deviations of extreme eigenvalues of random matrices. *Physical Review
Letters* 97(16), 160201.

Dehaene, S., Izard, V., Spelke, E. and Pica, P. (2008). Log or linear? Distinct intuitions of the number scale in Western
and Amazonian indigene cultures. *Science* 320, 1217–1220.

Descartes, R. (1637). *La Géométrie*. Appendix to *Discours de la méthode*. Leiden. Translated by D. E. Smith and
M. L. Latham (1925), *The Geometry of René Descartes*. Open Court, Chicago.

Dickey, J. M. (1967). Matricvariate generalizations of the multivariate t distribution and the inverted multivariate
t distribution. *The Annals of Mathematical Statistics* 38(2), 511–518.

Dietz, P. F. (1982). Maintaining order in a linked list. *Proceedings of the 14th ACM Symposium on Theory of
Computing*, 122–127.

Doyle, P. G. and Snell, J. L. (1984). *Random Walks and Electric Networks*. Carus Mathematical Monographs 22.
Mathematical Association of America, Washington.

Drory, A. (2015). Failure and uses of Jaynes' principle of transformation groups. *Foundations of Physics* 45(4),
439–460.

Ellis, G. F. R. and Baldwin, J. E. (1984). On the expected anisotropy of radio source counts. *Monthly Notices of the
Royal Astronomical Society* 206, 377.

Englert, B.-G. (1996). Fringe visibility and which-way information: an inequality. *Physical Review Letters* 77,
2154–2157.

Euclid (c. 300 BC). *Elements*. Translated by T. L. Heath (1908), *The Thirteen Books of Euclid's Elements*. Cambridge
University Press.

Euler, L. (1777). De repraesentatione superficiei sphaericae super plano. *Acta Academiae Scientiarum Imperialis
Petropolitanae* 1777(1), 107–132.

Feller, W. (1971). *An Introduction to Probability Theory and Its Applications*, vol. II, 2nd ed. Wiley, New York.

van Fraassen, B. C. (1989). *Laws and Symmetry*. Oxford University Press.

van Fraassen, B. C. (2008). *Scientific Representation: Paradoxes of Perspective*. Oxford University Press.

Frank, S. A. (2014). How to read probability distributions as statements about process. *Entropy* 16(11), 6059–6098.

Frank, S. A. and Smith, D. E. (2010). Measurement invariance, entropy, and probability. *Entropy* 12(3), 289–303.

Fraser, D. A. S. (1968). *The Structure of Inference*. Wiley, New York.

Furnas, G. W. and Bederson, B. B. (1995). Space-scale diagrams: understanding multiscale interfaces. *Proceedings of
CHI '95*, 234–241.

Gauss, C. F. (1828). *Disquisitiones generales circa superficies curvas*. Göttingen.

Gersho, A. and Gray, R. M. (1992). *Vector Quantization and Signal Compression*. Kluwer, Boston.

Gerville-Réache, L. (2016). Mettre de l'eau dans du vin, un paradoxe de l'indifférence ? *Implications
philosophiques*, 12 December 2016.

Ghosh, M. (2011). Objective priors: an introduction for frequentists. *Statistical Science* 26(2), 187–202.

Gibson, J. J. (1972). On the concept of the "visual angle" in an optic array and its history. Unpublished manuscript
(the "Purple Perils"), Cornell University.

Gibson, J. J. (1979). *The Ecological Approach to Visual Perception*. Houghton Mifflin, Boston.

Gilinsky, A. S. (1951). Perceived size and distance in visual space. *Psychological Review* 58, 460–482.

Greenberger, D. M. and Yasin, A. (1988). Simultaneous wave and particle knowledge in a neutron interferometer.
*Physics Letters A* 128, 391–394.

Gull, S. F. (1988). Bayesian inductive inference and maximum entropy. In G. J. Erickson and C. R. Smith (eds),
*Maximum-Entropy and Bayesian Methods in Science and Engineering*, vol. 1, 53–74. Kluwer, Dordrecht.

Haar, A. (1933). Der Massbegriff in der Theorie der kontinuierlichen Gruppen. *Annals of Mathematics* 34(1), 147–169.

Haldane, J. B. S. (1932). A note on inverse probability. *Proceedings of the Cambridge Philosophical Society* 28(1),
55–61.

Hastings, W. K. (1970). Monte Carlo sampling methods using Markov chains and their applications. *Biometrika* 57(1),
97–109.

Herschel, J. F. W. (1850). Quetelet on probabilities. *Edinburgh Review* 92, 1–57.

Hilbert, D. (1895). Über die gerade Linie als kürzeste Verbindung zweier Punkte. *Mathematische Annalen* 46,
91–96.

Horn, B. K. P. (1984). Extended Gaussian images. *Proceedings of the IEEE* 72(12), 1671–1686.

Hotelling, H. (1933). Analysis of a complex of statistical variables into principal components. *Journal of
Educational Psychology* 24, 417–441, 498–520.

Hotelling, H. (1936). Relations between two sets of variates. *Biometrika* 28(3–4), 321–377.

Huber, P. J. (1964). Robust estimation of a location parameter. *Annals of Mathematical Statistics* 35(1), 73–101.

Igarashi, T. and Hinckley, K. (2000). Speed-dependent automatic zooming for browsing large documents. *Proceedings
of UIST 2000*, 139–148.

ISO 269 (1985). *Correspondence envelopes — Designation and sizes*. International Organization for Standardization,
Geneva.

ISO 68-1 (1998). *ISO general purpose screw threads — Basic profile — Part 1: Metric screw threads*. International
Organization for Standardization, Geneva.

ISO 216 (2007). *Writing paper and certain classes of printed matter — Trimmed sizes — A and B series, and indication
of machine direction*. International Organization for Standardization, Geneva.

ISO 261 (1998). *ISO general purpose metric screw threads — General plan*. International Organization for
Standardization, Geneva.

Itai, A., Konheim, A. G. and Rodeh, M. (1981). A sparse table implementation of priority queues. *Automata,
Languages and Programming (ICALP 1981)*, Lecture Notes in Computer Science 115, 417–431.

Jaynes, E. T. (1968). Prior probabilities. *IEEE Transactions on Systems Science and Cybernetics* 4(3), 227–241.

Jaynes, E. T. (1973). The well-posed problem. *Foundations of Physics* 3(4), 477–493.

Jaynes, E. T. (1980). Marginalization and prior probabilities. In A. Zellner (ed.), *Bayesian Analysis in
Econometrics and Statistics: Essays in Honor of Harold Jeffreys*. North-Holland, Amsterdam. Reprinted in R. D.
Rosenkrantz (ed.) (1989), *E. T. Jaynes: Papers on Probability, Statistics and Statistical Physics*, Reidel, 337–375.

Jeffreys, H. (1939). *Theory of Probability*. Oxford University Press.

Jeffreys, H. (1946). An invariant form for the prior probability in estimation problems. *Proceedings of the Royal
Society of London A* 186(1007), 453–461.

Jones, M. C. (1999). Distributional relationships arising from simple trigonometric formulas. *The American
Statistician* 53(2), 99–102.

Jones, M. C. (2008a). The distribution of the ratio X/Y for all centred elliptically symmetric distributions.
*Journal of Multivariate Analysis* 99(3), 572–573.

Jones, M. C. (2008b). On reciprocal symmetry. *Journal of Statistical Planning and Inference* 138(10), 3039–3043.

Jordan, C. (1875). Essai sur la géométrie à n dimensions. *Bulletin de la Société Mathématique de France* 3,
103–174.

Kakutani, S. (1944). Two-dimensional Brownian motion and harmonic functions. *Proceedings of the Imperial Academy
Tokyo* 20(10), 706–714.

Kalman, R. E. (1960). A new approach to linear filtering and prediction problems. *Journal of Basic Engineering*
82(1), 35–45.

Karger, D., Lehman, E., Leighton, T., Panigrahy, R., Levine, M. and Lewin, D. (1997). Consistent hashing and random
trees. *Proceedings of the 29th ACM Symposium on Theory of Computing*, 654–663.

Kass, R. E. and Wasserman, L. (1996). The selection of prior distributions by formal rules. *Journal of the American
Statistical Association* 91, 1343–1370.

Kato, S. and McCullagh, P. (2020). Some properties of a Cauchy family on the sphere derived from the Möbius
transformations. *Bernoulli* 26(4), 3224–3248.

Keller, J. B. and Vakil, R. (2009). π_p, the value of π in ℓ_p. *The American Mathematical Monthly* 116(10),
931–935.

Kellogg, O. D. (1929). *Foundations of Potential Theory*. Springer, Berlin.

Kendall, D. G. (1984). Shape manifolds, Procrustean metrics, and complex projective spaces. *Bulletin of the London
Mathematical Society* 16(2), 81–121.

Klein, F. (1871). Über die sogenannte Nicht-Euklidische Geometrie. *Mathematische Annalen* 4, 573–625.

Klein, F. (1872). *Vergleichende Betrachtungen über neuere geometrische Forschungen* (the Erlangen programme).

Knight, F. B. (1976). A characterization of the Cauchy type. *Proceedings of the American Mathematical Society* 55,
130–135.

Knuth, D. E. (1998). *The Art of Computer Programming*, Vol. 3: *Sorting and Searching*, 2nd ed. Addison-Wesley,
Reading, MA.

Koenderink, J. J. (1984). What does the occluding contour tell us about solid shape? *Perception* 13(3), 321–330.

Lambert, J. H. (1772). *Anmerkungen und Zusätze zur Entwerfung der Land- und Himmelscharten*. Berlin.

Lamping, J., Rao, R. and Pirolli, P. (1995). A focus+context technique based on hyperbolic geometry for visualizing
large hierarchies. *Proceedings of CHI '95*, 401–408.

Laurentini, A. (1994). The visual hull concept for silhouette-based image understanding. *IEEE Transactions on
Pattern Analysis and Machine Intelligence* 16(2), 150–162.

Lee, D. N. (1976). A theory of visual control of braking based on information about time-to-collision. *Perception*
5(4), 437–459.

Leonard, D. (2011). Estimating a bivariate linear relationship. *Bayesian Analysis* 6(4), 727–754.

Levi-Civita, T. (1920). Sur la régularisation du problème des trois corps. *Acta Mathematica* 42, 99–144.

Lévy, P. (1925). *Calcul des probabilités*. Gauthier-Villars, Paris.

Liu, Z. and Adams, C. S. (2019). Experimental tests of Bertrand's question and the Duhem–Quine problem. *European
Journal of Physics* 40(6), 065801.

Longuet-Higgins, H. C. (1981). A computer algorithm for reconstructing a scene from two projections. *Nature* 293,
133–135.

Luce, R. D. (1959). On the possible psychophysical laws. *Psychological Review* 66(2), 81–95.

Lupton, R. H., Gunn, J. E. and Szalay, A. S. (1999). A modified magnitude system that produces well-behaved
magnitudes, colors, and errors even for low signal-to-noise ratio measurements. *The Astronomical Journal* 118(3),
1406–1410.

Mahalanobis, P. C. (1936). On the generalised distance in statistics. *Proceedings of the National Institute of
Sciences of India* 2(1), 49–55.

Mardia, K. V. and Jupp, P. E. (2000). *Directional Statistics*. Wiley, Chichester.

Marinoff, L. (1994). A resolution of Bertrand's paradox. *Philosophy of Science* 61, 1–24.

Maxwell, J. C. (1860). Illustrations of the dynamical theory of gases. *Philosophical Magazine* 19, 19–32.

McCullagh, P. (1996). Möbius transformation and Cauchy parameter estimation. *The Annals of Statistics* 24, 787–808.

Mercator, G. (1569). *Nova et aucta orbis terrae descriptio ad usum navigantium emendate accommodata*. Duisburg.

Metropolis, N., Rosenbluth, A. W., Rosenbluth, M. N., Teller, A. H. and Teller, E. (1953). Equation of state
calculations by fast computing machines. *The Journal of Chemical Physics* 21(6), 1087–1092.

Microsoft. Bing Maps Tile System (documentation).

Mikkelson, J. M. (2004). Dissolving the wine/water paradox. *British Journal for the Philosophy of Science* 55(1),
137–145.

Minkowski, H. (1903). Volumen und Oberfläche. *Mathematische Annalen* 57, 447–495.

Secrest, N. J. et al. (2021). A test of the cosmological principle with quasars. *Astrophysical Journal Letters* 908,
L51.

von Mises, R. (1928). *Wahrscheinlichkeit, Statistik und Wahrheit*. Springer, Vienna.

Möbius, A. F. (1827). *Der barycentrische Calcul*. Barth, Leipzig.

Munro, J. I. and Paterson, M. S. (1980). Selection and sorting with limited storage. *Theoretical Computer Science*
12(3), 315–323.

Niven, I. (1956). *Irrational Numbers*. Carus Mathematical Monographs 11, Mathematical Association of America.

Norton, J. D. (2008). Ignorance and indifference. *Philosophy of Science* 75(1), 45–68.

Parker, M. C. and Jeynes, C. (2023). A maximum entropy resolution to the wine/water paradox. *Entropy* 25(8), 1242.

Pearson, K. (1896). Mathematical contributions to the theory of evolution. III. Regression, heredity, and panmixia.
*Philosophical Transactions of the Royal Society of London, Series A* 187, 253–318.

Penrose, R. (1959). The apparent shape of a relativistically moving sphere. *Proceedings of the Cambridge
Philosophical Society* 55, 137–139.

Penrose, R. and Rindler, W. (1984). *Spinors and Space-Time*, Vol. 1. Cambridge University Press.

Pitman, E. J. G. and Williams, E. J. (1967). Cauchy-distributed functions of Cauchy variates. *Annals of Mathematical
Statistics* 38(3), 916–918.

Plücker, J. (1865). On a new geometry of space. *Philosophical Transactions of the Royal Society of London* 155,
725–791.

Polyak, B. T. and Juditsky, A. B. (1992). Acceleration of stochastic approximation by averaging. *SIAM Journal on
Control and Optimization* 30(4), 838–855.

Rivlin, T. J. (1974). *The Chebyshev Polynomials*. Wiley, New York.

Robbins, H. and Monro, S. (1951). A stochastic approximation method. *The Annals of Mathematical Statistics* 22(3),
400–407.

Roy, W. (1785). An account of the measurement of a base on Hounslow-Heath. *Philosophical Transactions of the Royal
Society of London* 75.

Rybicki, G. B. and Lightman, A. P. (1979). *Radiative Processes in Astrophysics*. Wiley, New York.

Saint-Vincent, G. de (1647). *Opus geometricum quadraturae circuli et sectionum coni*. Antwerp.

Schwartz, E. L. (1977). Spatial mapping in the primate sensory projection: analytic structure and relevance to
perception. *Biological Cybernetics* 25, 181–194.

Sedgwick, H. A. (1973). *The Visible Horizon: A Potential Source of Visual Information for the Perception of Size
and Distance*. Doctoral dissertation, Cornell University.

Sedgwick, H. A. (1986). Space perception. In K. R. Boff, L. Kaufman and J. P. Thomas (eds.), *Handbook of Perception
and Human Performance*, vol. 1, 21.1–21.57. Wiley, New York.

Sedgwick, H. A. (2021). J. J. Gibson's "Ground Theory of Space Perception". *i-Perception* 12(3), 20416695211021111.

Seidenfeld, T. (1979). Why I am not an objective Bayesian; some reflections prompted by Rosenkrantz. *Theory and
Decision* 11, 413–440.

Shackel, N. (2007). Bertrand's paradox and the principle of indifference. *Philosophy of Science* 74, 150–175.

Seshadri, V. (1965). On random variables which have the same distribution as their reciprocal. *Canadian
Mathematical Bulletin* 8, 819–824.

Siegler, R. S. and Opfer, J. E. (2003). The development of numerical estimation: evidence for multiple representations of
numerical quantity. *Psychological Science* 14(3), 237–243.

Sivia, D. S. and Skilling, J. (2006). *Data Analysis: A Bayesian Tutorial*, 2nd ed. Oxford University Press.

Smart, W. M. (1977). *Textbook on Spherical Astronomy*, 6th ed., revised by R. M. Green. Cambridge University Press.

Snellius, W. (1617). *Eratosthenes Batavus, de terrae ambitus vera quantitate*. Leiden.

Sós, V. T. (1958). On the distribution mod 1 of the sequence nα. *Annales Universitatis Scientiarum Budapestinensis
de Rolando Eötvös Nominatae, Sectio Mathematica* 1, 127–134.

Spitzer, F. (1958). Some theorems concerning 2-dimensional Brownian motion. *Transactions of the American
Mathematical Society* 87, 187–197.

Steiner, J. (1832). *Systematische Entwickelung der Abhängigkeit geometrischer Gestalten von einander*. Fincke,
Berlin.

Stevens, S. S. (1946). On the theory of scales of measurement. *Science* 103(2684), 677–680.

Stigler, S. M. (1974). Cauchy and the witch of Agnesi: an historical note on the Cauchy distribution. *Biometrika*
61(2), 375–380.

Stone, M. and Dawid, A. P. (1972). Un-Bayesian implications of improper Bayes inference in routine statistical
problems. *Biometrika* 59(2), 369–375.

Talacko, J. (1956). Perks' distributions and their role in the theory of Wiener's stochastic variables.
*Trabajos de Estadística* 7, 159–174.

Terrell, J. (1959). Invisibility of the Lorentz contraction. *Physical Review* 116(4), 1041–1045.

Thomas, L. H. (1926). The motion of the spinning electron. *Nature* 117, 514.

Tissot, N. A. (1881). *Mémoire sur la représentation des surfaces et les projections des cartes géographiques*.
Gauthier-Villars, Paris.

Triggs, B., McLauchlan, P. F., Hartley, R. I. and Fitzgibbon, A. W. (2000). Bundle adjustment — a modern synthesis.
In *Vision Algorithms: Theory and Practice*, Lecture Notes in Computer Science 1883, 298–372. Springer, Berlin.

Viète, F. (1593). *Variorum de rebus mathematicis responsorum liber VIII*. Tours.

Wallstrom, T. C. (2003). The marginalization paradox does not imply inconsistency for improper priors. arXiv
math/0310006.

Wantzel, P. L. (1837). Recherches sur les moyens de reconnaître si un problème de géométrie peut se résoudre avec
la règle et le compas. *Journal de Mathématiques Pures et Appliquées* 2, 366–372.

Weisskopf, V. and Wigner, E. (1930). Berechnung der natürlichen Linienbreite auf Grund der Diracschen Lichttheorie.
*Zeitschrift für Physik* 63, 54–73.

van Wijk, J. J. and Nuij, W. A. A. (2003). Smooth and efficient zooming and panning. *Proceedings of IEEE InfoVis
2003*, 15–23.

Weyl, H. (1916). Über die Gleichverteilung von Zahlen mod. Eins. *Mathematische Annalen* 77, 313–352.

Whitney, H. (1955). On singularities of mappings of Euclidean spaces. I. Mappings of the plane into the plane.
*Annals of Mathematics* 62(3), 374–410.

Williams, L. (1983). Pyramidal parametrics. *Computer Graphics* (Proceedings of SIGGRAPH '83) 17(3), 1–11.

Yaglom, I. M. (1968). *Complex Numbers in Geometry*. Academic Press, New York.

Zahn, C. T. and Roskies, R. Z. (1972). Fourier descriptors for plane closed curves. *IEEE Transactions on Computers*
C-21(3), 269–281.
