# Observation from Somewhere

**Addresses, payloads and the geometry of a situated reader**

*Tom Brinkman, with Claude. Draft for external review, 15 October 2026.*

## Abstract

Classical geometry is drawn from nowhere: every length is held at once, to one scale, by no one in particular. A reader
that stands somewhere has less. It has its own breadth, a value it chooses to start from, but not the breadth of what it
reads. This paper works out the geometry that this one restriction leaves. We build on Jaynes's principle of
transformation groups: what a reader cannot tell apart, it addresses alike. Taking its ignorance to be of its own
attitude, of the other's size and of which unit relation a reading was divided by, and the sweep to be the turning of a
rigid bar, the principle gives the even turn, the corner and the drawing at the reader's own breadth, and, through
amounts, motivates the logarithm past the corner; being situated, at home, removes the translations that Jaynes's chord
keeps. We begin with the readers themselves. What a reader knows of two breadths sets one of five situations (with more
parties, one entry per party), and these give three vantages: the completed view from nowhere, which holds the straight
chord between two points, and two situated readers, the central sweep and the inscribed sweep,
which hold only the arc they turn through and whose figures are the bell and the fisheye. The chord comes before the
circle: it needs no turn, and the circle is drawn on it by one. The three read a line of true breadth 1 as 1, π/2 and
2/π; the true breadth is held only from nowhere, or constructed from several observations, never observed from one. Any
relation between two parties can be written as a pair of unit relations, h and v, each between 0 and 1, and the reader
reads their ratio. Because neither unit relation can pass 1, every such sweep turns over at a single point, v = h, the
*corner*, where reading v in terms of h gives way to reading h in terms of v. For there to be a relation, the reader
must assign the other party a breadth, and its only measure is its own: it draws the mountain at the breadth of its
thumb, V = H. This is required for the sweep to be a turn. Only then is the sweep from one party to the other the turn
of one rigid bar, tracing a unit circle with the corner at distance 1 whatever unit was chosen, and only then is there a
single even turn; working back from the Cauchy distribution, which is known, arrives at V = H and nowhere else. The two
familiar pictures of a turn laid on a line require it too: a lighthouse's flashes put half their landings within the
lamp's distance of its foot only when shore and sea are drawn at one length, and Mercator's map draws every compass
course true only because it stretches north–south as much as east–west, giving up only size, a zoom. The drawing is not
a claim about the mountain. Its true size is a separate number, which one observation does not give; the reader's best
estimate of it is the median of what it knows, and correcting the estimate moves every amount by the same number of
levels and redraws nothing. Nor is the reader's own breadth a measurement: H is the value it chooses to start from,
every value gives the same circle, and its size sets only the zoom, fine near for a small H and fine far for a large
one. The geometry needs that value and a shape, and the shape is set by how many unit relations the system includes: two
give the circle, three the sphere. Inside the corner the reader can lay out its readings in proportion; past it, if no
scale is preferred (a premise we assume, not derive), the only consistent layout is logarithmic. The reader therefore
has two address spaces, proportional and logarithmic, joined at one corner.

Our main result concerns what a reader receives when it sweeps this circle evenly from where it stands. Its readings
follow the Cauchy distribution. When the evenness is the reader's own laying, we show that the distribution belongs
entirely to the reader's addresses and not to anything that arrives at them: whatever is met in each direction cancels
from every single reading. Where the evenness belongs to the sources instead, as when a lighthouse sends its flashes
at evenly spread angles, the same law is a property of the world's directions. This gives a reason for the Cauchy's
best-known peculiarity. Its median exists and sits at the corner, because a median depends only on order, which is a
property of addresses. Its mean does not exist, because a mean is a sum of sizes, a question about the payload, and
addresses carry no size. Neither property needs the circle or the even turn: any sweep that treats the two parties alike
puts its median at the corner and, if it reaches the horizon, has no mean; the even turn gives the Cauchy's exact
shape. The same split decides what reaches a reader of a payload. One stream of readings fixes the
course of a relation, not its parties. The median is had only by a reader that holds its readings at once. Payloads
closer together than the reader's step arrive as their centroid, a sum.

## 1. Introduction

Geometry as usually written is drawn from nowhere. A blueprint shows every line at its true length, to one scale, turned
neither toward nor away from anyone, and the equation h² + v² = 1 holds all its points at once. Nagel (1986) called this
the view from nowhere. It is not a view anyone takes but a representation that abstracts from every standpoint: the
right one for many purposes, but not what anyone who actually observes has. An eye, an instrument or a person counting
stands somewhere. It has its own scale, its own breadth, a value it chooses to start from rather than a size it has
measured, and it does not know the breadth of what it reads.

This paper asks what geometry such a reader has. Our thesis is this:

> A situated observer does not possess a coordinate system for the world; it constructs an addressing scheme from
> relations available at its standpoint, and uses those addresses to encounter the world's magnitudes.

Put another way, geometry is not shapes. It is the sweep of addresses that point to a magnitude, and it says nothing
about what the magnitudes are. The magnitudes are not irrelevant: they make the back sides and everything hidden. But
they are met at the addresses, not built into them. The geometry that follows is therefore not a new geometry of the
world. It is a geometry of the reader's own
*addresses*: the places where readings can be put, which exist before anything is read and do not depend on what is
found there.

**What is new, and what is not.** That coordinates depend on the observer is old: a coordinate system is a choice,
and a change of coordinates changes every coordinate. What is new here is where the scheme comes from. A coordinate
system is laid on a completed space. It presupposes the whole, with every length already in one scale, and a change of
coordinates carries every amount along with it. A situated reader has no completed space to lay coordinates on. It has
its own breadth and the relations it can form from where it stands, and from these alone it builds its places before
anything is read. Three things then have to be kept apart:
- the *object*, whatever exists independently of any reading of it;
- the *address*, the place in the reader's scheme at which something can be met;
- the *payload*, the magnitude met there.

A change of coordinates moves addresses and payloads together. The separation here lets either change without the
other. Changing what arrives leaves every address in place (Theorem 6), and changing the reader's sweep changes its
addresses without touching the object. The contribution is a construction of a bounded observer's representation that
does not presuppose the whole, together with an exact account of what that construction can recover and what it
cannot. Classical geometry is not wrong; it begins where this paper ends, with the whole already in hand.

**What we build on.** The method is not new either. Jaynes (1968, 1973) showed how to choose a measure from what an
observer does not know: state its ignorance as a group of transformations, and take the measure the group leaves
unchanged. His cases give the classical priors, even in a location and even in the logarithm of a scale, and one answer
to Bertrand's chord drawn at random in a circle, posed so that turning, resizing or moving the circle changes nothing.
We apply the method to a reader that stands somewhere, with a group we choose as its ignorance: turns of its bar,
rescalings of the other party's size, and the exchange of the two unit relations. Given that the sweep is the turning of
a rigid bar, the measures these leave unchanged give much of this paper's geometry: the even turn and its Cauchy, the
corner, and the drawing at the reader's own breadth; carried to amounts, the same indifference to scale motivates the
logarithm past the corner (§2). What is ours is the choice of group, the near field, and the reading of the measure as
the reader's addresses rather than its belief.

**A picture.** Hold your hand out flat, palm down, and turn it until it points straight up. The motion between is a
sweep. Spread your fingers between flat and upright: each finger is a direction in which you can look, an address. Now
put a ring on each finger. The rings are what you find in each direction, the *payload*. Turning the hand does not
change the rings, and swapping the rings for others does not change the fingers. Much of what follows is the
mathematics of the fingers alone, and the main result is that one well-known distribution, the Cauchy, is entirely
fingers.

Your thumb is your own breadth, H: the one measure you hold up, chosen because it is to hand, not because it measures
anything. The mountain you look at has a breadth of its own, V*, which you may not know.
If you know the mountain's size, you hold the view from nowhere, and the corner is where your thumb equals the mountain,
a point you can compute. If you do not know it, your thumb is the only measure you have, so you set the mountain equal
to your thumb, V = H, and read the mountain in thumbs.

**Three vantages.** A figure can be held in three ways. The *completed* vantage holds every breadth at once from no
standpoint; this is classical geometry. Between two points it holds the straight chord, which needs no turn; the circle
comes after the chord, drawn on it by turning. A *situated* reader has a facing, and holds only the arc it turns
through, by one of two sweeps that get two different things. The central sweep, turning about the centre of the circle
on the chord, gets the payloads, what arrives, read by their mean; the inscribed sweep, from home, gets the addresses to
the payloads, the Cauchy, read by its median at the corner. How either sweep is made is not pinned down; this paper
follows one proposal, the central taken at once and the inscribed one direction at a time. These two are not the only
situated views: every drawing other than the sum of the unit relations is built from a standpoint (§2). The sum is where
the truth would lie: a system's true breadths, as shares of their whole, would be one point of it, found only with the
breadths themselves, amounts the reader does not read. A reader's drawing, every party at its own H, is the sum's
centre, where every pair is at its corner; the geometry follows from there, and the truth lies off the centre by the
ratios the reader lacks. The three read the same thing differently: a line of true breadth 1 reads 1 to the completed
view, π/2 to the hemisphere turned away from the reader and 2/π to the hemisphere turned toward it. The true breadth is
had only with both hemispheres in hand, which no single observation provides. A situated reader can construct it from
several observations, but it cannot observe it. Many apparent paradoxes come from reading one vantage's geometry as if
it were another's, most often from treating the completed view as if a single observation held it. Section 3 sets out
the readers in full.

**Results.**
- A situated reader's ignorance, as we choose it, is a group: turns of its bar, rescalings of the other party's size,
  and the exchange of the two unit relations. The measure the first two leave unchanged, even in attitude and even in
  levels of size, is analogous to Jaynes's location and scale with the location on a circle. Given that the sweep is the
  turning of a rigid bar, it gives the even turn; the exchange gives the corner and, with the rigid turn, the drawing V
  = H; through amounts, the rescalings motivate the logarithm past the corner. Standing at home removes the
  translations: from home the even measure is even in direction and in levels of distance, not in area, and Bertrand's
  chord has an answer that depends on where the circle lies, ⅓ from on it, rising to Jaynes's ½ from far off (§2).
- What a reader knows of the two breadths sets its situation, one of five, and the situations give three vantages,
  each with its own geometry and its own reading of a line of true breadth 1. A situated reader can divide only by its
  own breadth, and what it lacks is a single number (§3).
- Every sweep between two parties turns over at one point, the corner v = h, the only point left fixed when the two
  parties are exchanged. Near and far are one geometry, read from either side of it (§4).
- A reader that holds one breadth must assign the other party a breadth in its own unit. For the sweep to be a turn,
  that breadth must be its own, V = H: only then does the sweep trace a unit circle with the corner at distance 1
  whatever unit is chosen, and only then is there one even turn. Sweeps that are not turns (along a line, say) keep the
  corner and the missing mean but not the Cauchy's shape (Theorem 6(e), §11.2). Working back from the Cauchy, which is
  known, arrives at V = H (§5, §7.1). So do the two familiar pictures of a turn laid on a line: a lighthouse's flashes
  on a shore, and Mercator's chart, which draws every compass course true only because it stretches north–south as much
  as east–west. Both leave the size free (§7.1). What the paper shows is that a reader should draw V = H, since only
  that drawing gives it these; whether readers do is an empirical question it leaves open (§11.2). The other party's
  true size is a separate estimate (§9). H itself is not a measured size but the value the reader starts from; any value
  gives the same geometry, and its size sets only the zoom (§8).
- How many unit relations the system includes sets its shape: two the circle, three the sphere, n + 1 the sphere in
  n + 1 dimensions (§5). With two other parties the same holds once per party. Drawn at V = V₂ = H, the relation lies on one sphere, and the
  reader sweeps one octant of it, a wedge. Swept evenly, its readings are the two-dimensional Cauchy: every pair keeps
  its corner, and the reader is near in both readings for a third of them, not a half (§5, §7.1). With n other
  parties it is near in all its readings for 1/(n + 1) of them. The drawing is the geometry's whole work; no party's
  true size enters it.
- Inside the corner the reader can lay readings out in proportion; past it, if no scale is preferred, only a
  logarithmic layout is consistent. The reader has two address spaces joined at one corner (§6).
- **Main result.** Sweeping the circle evenly from home yields the Cauchy distribution, and the Cauchy is the reader's
  addresses, not its payload. Whatever is met in each direction cancels from the reading. Order survives every change of
  payload and sums do not, which is why the Cauchy has a median, at the corner, and no mean (§7). The median at the
  corner needs only that the sweep treat the two parties alike, and the missing mean only that, besides, its weight not
  vanish at the horizon; the circle and the even turn give the Cauchy's exact shape (§7.2).
- How finely a reader reads is a count the geometry leaves open, and the choice of unit is a zoom, not an escape (§8).
  A larger H gives the near less detail and reaches the far; the best H is the corner of what is read. An H of 0 or
  of ∞ leaves the reader one of the rulers that favour no amount, and no corner (§9).
- The geometry does not supply amounts. A common rescaling leaves every reading unchanged, one amount supplied from
  outside fixes the scale, and a fact shared between two readers supplies exactly one ratio. The best estimate of the
  other party's true size is the median of what the reader knows of it (§9).
- A unit is a relation measured beforehand, such as one foot, or five ounces to a foot, and it brings in the one
  ratio no reading supplies. A reader needs one for two reasons. Its addresses are finitely many, so the value of its
  own unit decides which sizes it reads finely, and choosing that value well is where the scale of the world first
  reaches it; and, agreed between readers, a unit lets amounts pass between them. The number line is such a unit:
  a ruler that favours no reader's unit must be a power or a logarithm, with no corner, and the number line is the
  power that keeps proportion on both sides of 1 (§9).
- What reaches a reader of a payload depends on what it holds and what it resolves (§7.6, §9).
  - One stream fixes the course of a relation, not its parties: motion comes before the object.
  - Readings taken at once against one denominator give payloads relative to each other.
  - Further standpoints bring back a figure up to its scale.
  - Payloads closer than a step arrive as their centroid.
  - The addresses' centre, the median, is had only by a reader holding its readings at once.
- A worked example, a mountain range read from nowhere and from where the reader stands, puts the pieces together (§10).

Section 2 states the principle these rest on, Jaynes's, and Section 11 returns to it. The geometry is claimed as
necessary relative to a stated ignorance, not absolutely, and each relaxation of that ignorance gives a named
alternative; Section 11 also lists the assumptions and related work.
The paper is geometry only. It makes no claim about physics, perception or the structure of spacetime.

## 2. Setting

**Unit relations.** Everything here is built from the *unit relation*: a number from 0 to 1 relating a part to its
whole, none of it, all of it, or anything in between, such as the fraction of a day gone or the part of a road
behind. A relation requires two unit relations, one for each party. Draw one horizontally and one
vertically and call them h and v. They have no units, and neither knows the other's whole. The wholes they relate to are
the *breadths* H and V, written in uppercase with the amounts. Neither is a measured size. The reader's breadth H is
the one value it chooses to start the system, its thumb in the picture of §1: any value will do, and which one it chooses sets
only the zoom (§8). The other's breadth V is the length at which the reader draws the other party's whole, the
mountain it looks at; the other party's true size, an amount the reader does not have, is written V*. h is the
reader's side of a relation. A circle has two unit relations, h and v; a sphere has three, h, v and v₂. How many a
system includes sets its shape (§5).

**Unit relations are not amounts.** The amounts are h·H and v·V*, so their ratio is (v·V*)/(h·H) = (v/h)·(V*/H). The
ratio of the unit relations, v/h, is not the ratio of amounts, V*/H. The only way from one to the other is to multiply
by a breadth, which must be known. We keep lowercase letters for unit relations and uppercase for breadths and amounts
throughout, with V* for a party's true breadth.

**The sweep.** Within one observation neither breadth changes. The *sweep* is every way h and v can relate, from all of
H (v = 0) to all of V (h = 0). Leaving *home* (v = 0), v rises against h held at 1. It can rise only until it too
reaches 1, at v = h. After that the relation can continue only by h falling against v held at 1. The reader reads v/h on the first
half and h/v on the second, each in [0, 1]. Exchanging the two parties, the *flip*, sends v/h to h/v. The limit
v/h → ∞, where h empties, is the *horizon*; it is never reached.

**The wedge, and its drawings.** Every pair of unit relations is a ray from the origin into the quarter-plane between
the two axes; with a third unit relation v₂, read against the same h, it is a ray into the solid wedge between three
axes. The ray is the relation. Position along the ray is the pair's size, and that is what dividing one unit relation by
another removes. The wedge itself favours neither unit relation: a facing, in the sense below, is the choice of which
one to divide by, and v/h is the wedge read facing h. The wedge is the primitive. It is made afresh at each observation, from the relations at one
standpoint, and the sphere is not assembled from wedges: it is the picture, from nowhere, of all the wedges that could
be made.

The usual drawings are cuts of the wedge, each a different normalization:

| cut the wedge where | two unit relations | three unit relations | normalized by |
|---|---|---|---|
| length = 1 | the quarter circle h² + v² = 1, length π/2 | the sphere's octant, area π/2 | the whole length |
| largest = 1 | the unit square's two arms, length 2 | the unit cube's three faces, area 3 | the largest unit relation |
| sum = 1 | the line h + v = 1, length √2 | a flat triangle, area √3/2 | the sum |
| one unit relation = 1 | the reading v/h on [0, ∞) | the plane of v/h and v₂/h | one unit relation: a facing |

Every cut passes once through every ratio and meets the corner at v/h = 1. The numbers belong to the cut, not to the
relations: the quarter arc and the octant both measure π/2 because they are cut by length. Statements about ratios hold
in every drawing; statements about lengths, angles or areas belong to one, and we say which. We call the first three
cuts the *arc*, the *square* and the *line*.

**The sum, and the drawings built from a standpoint.** One cut needs no standpoint. The sum h + v + v₂ + … = 1 treats
every unit relation alike and needs nothing but addition: each is a share of a whole, and only a view that holds the
whole has shares. It is the completed view's own drawing, the line (the chord) for two unit relations and the flat
triangle for three. Every other drawing is built from a standpoint. Dividing by one unit relation chooses a facing;
dividing by the largest chooses a register, reading v/h up to the corner and h/v past it; dividing by length needs a
turn. The two hemispheres of §3.4 are two such drawings, not the only ones.

The sum also shows where a reader stands. The triangle holds every way the breadths can share a whole. A system's true
breadths, taken as shares of their whole, would be one point of it, and no common unit moves that point; but finding it
needs the true breadths, which are amounts, and normalizing the unit relations by their sum does not supply them. A
situated reader does not have that point. It chooses H, which sets only
its zoom (§8), and draws every other party at it, V = V₂ = H: equal shares, the triangle's centre (⅓, ⅓, ⅓), which is
the triple corner, where every pair is at its corner. The rest of the geometry follows from that drawing. The true point
lies off the centre by the two ratios the reader lacks, V*/H and V₂*/H (§3.8); amounts brought from outside move the
reader's amounts toward it and redraw nothing (§9).

**Two sweeps: altitude and azimuth.** A reader reaches the wedge of three unit relations by two sweeps, the coordinates
an observer uses for its own sky (Smart 1977). Take v as the vertical and h and v₂ as the horizontal plane, h the
forward direction, toward the first other party. The *altitude* a sweeps from the horizontal up to the vertical: the
sweep from H to V. The *azimuth* z sweeps round the horizontal plane, from h to v₂ square to it: the sweep that brings
in V₂. The direction is (h, v, v₂) = (cos a cos z, sin a, cos a sin z). Each sweep reads its own pair and has its own
corner at 45°: the azimuth reads v₂/h = tan z, whatever the altitude, and the altitude reads v against the horizontal
reach, v/√(h² + v₂²) = tan a, whatever the azimuth. These are horizon coordinates: the horizon and the vertical are set
by where the reader stands, as an observer's are, unlike coordinates fixed to the sky, and a surveyor's theodolite reads
the same two angles. The sweeps choose an order, a forward direction and a vertical; the wedge itself does not. With
n + 1 unit relations there are n sweeps. What sweeping them evenly means is taken up with the even wedge (§7.1).

**Addresses and payload.** An *address* is a place in the reader's layout where a reading can be put. The range of
addresses is fixed by the geometry before anything arrives, and an address is taken from it when something does. The
*payload* is what arrives: a wave of some kind, sent out or shaped by the things read, not the things themselves.
A reader reads what arrives and reaches the things only through it. In the picture of §1 the fingers are addresses and the rings are payload. The addresses a
reader lays do not depend on what arrives at them; every "if" belongs to the payload, including which side of the
corner a given reading falls on. A *lay* is a rule
that places each reading at a position in a drawing; the *room* a stretch of readings receives is measured either by
length or by number of addresses. A *facing* is one side of the corner in one freedom; a sweep from all h to all v
covers one facing. A *level* is a stretch of the reading: the first runs from home to the corner, and past the corner
each level is one doubling of v/h.

**What we build on: the reader's ignorance as a group.** The method is Jaynes's (1968, 1973). An observer that cannot
tell two problems apart must treat them alike, and when the problems it cannot tell apart are related by a group of
transformations, the measure it should use is the one the group leaves unchanged: indifference between problems, not
between events. His cases are these (Jaynes 1968, §VII). Ignorance of a location and a scale gives a measure even in the
location and even in the logarithm of the scale, dμ·dσ/σ, Jeffreys's rule for a scale (Jeffreys 1939); ignorance of a
rate's time scale gives dλ/λ. Ignorance of a share t, read as a population of opinions that learns nothing from a new
piece of evidence, which multiplies every opinion's odds by one factor, gives 1/(t(1 − t)), even in the logarithm of the
odds, the prior Haldane (1932) had proposed. When the group has as many parameters as the problem, the measure is fixed
up to a constant (Jaynes 1968). And Bertrand's "chord drawn at random" in a circle (Bertrand 1889) has one answer once
it is posed so that the answer must not change when the circle is turned, resized or moved: ½, the chord's distance from
the centre even, the answer Crofton's measure on lines gives (Crofton 1868; Jaynes 1973). Resizing alone already rules
out Bertrand's chord between two random ends, which can hold "for, at most, only one size of circle", and moving the
circle alone already fixes the answer.

We apply the method to a situated reader. It does not know two quantities, its *attitude* θ, which way its bar points,
and the other party's true size relative to its own, κ = V*/H (written b in §3.8); nor, from a reading alone, which of
the two unit relations the reading was divided by. We take its ignorance of these to be this group:
1. a *turn* of the bar, θ ↦ θ + α: nothing the reader holds prefers one attitude to another;
2. a *rescaling* of the other party's size, κ ↦ λκ: the other party's amounts all change by one factor, and no unit
   relation and no reading changes;
3. the *exchange* of the two unit relations, v ↔ h, which sends a reading to its flip and θ to 90° − θ (Proposition 1):
   nothing in a reading says which of the two it was divided by. It acts on readings and on drawings, not on κ: the
   reader holds H and not V*, and the two breadths cannot be swapped without changing what it knows. That the other is
   as likely to be larger as smaller, κ and 1/κ alike, is a separate premise, used only for the estimate of the size
   (Proposition 13(c)).

The turns and the rescalings act on separate unknowns and commute. This is analogous to Jaynes's problem of a location
and a scale, with the location on a circle, though here the scale acts on no reading: two problems side by side rather
than one. The measure they leave unchanged is dθ·dκ/κ, their Haar measure (Haar 1933), unique up to a constant factor,
since f(θ + α, λκ)·λ = f(θ, κ) for all α and λ leaves only k/κ. Jaynes's own group, μ′ = μ + b with σ′ = aσ (1968, eq.
49), also commutes. The location-and-scale family's group, x ↦ p + qx, does not, and has two invariant measures:
dμ·dσ/σ, the right-invariant one, which coincides with Jaynes's, and dμ·dσ/σ², the left-invariant one, Jeffreys's
general rule. Later work has favoured the right-invariant one where the location or the scale is of interest and the
other a nuisance: it is then Bernardo's reference prior (Bernardo 1979) and gives frequentist coverage exactly (as
reviewed by Ghosh 2011); with other quantities of interest the left one can be the better (§11.2, question 7). The
reader's group has one: its turns and rescalings commute, and its exchange is a reflection, so the group is unimodular
and the measures unchanged by composing on the left and on the right coincide. What the measure gives:
- *Even in θ*: once the sweep is taken to be the turning of the bar, an even turn (§7.1); which variable the evenness is
  in is the choice Drory presses (§11.2, question 2). Read as v/h on one facing, with the parties drawn at one length,
  it is the half-Cauchy with its median at the corner (Proposition 5); signed over both facings, the standard Cauchy.
  Write a Cauchy law with median m and scale γ as the point m + iγ of the upper half-plane. A turn acts on the signed
  reading as a Möbius map and carries each Cauchy law to the one at the image point (McCullagh 1996); the standard
  Cauchy, at i, is the only one every turn leaves where it is. Drawn at V = cH the even turn's readings are the Cauchy
  law at i/c (Proposition 5(d)); turns in that drawing's plane act on its readings by conjugate maps, which fix i/c, and
  do not carry all of h into all of v; the exchange carries i/c to ic. So the drawing V = H is selected twice: by the
  rigid turn, which with c ≠ 1 has no turn from all of h to all of v (Proposition 3(e)), and by the exchange acting on
  the law of the readings, V = H being the only drawing whose readings favour neither unit relation (Proposition 5(d)).
- *Even in log κ*: every level of the other's size alike. As an estimate of the size, with nothing to make the other
  larger rather than smaller (the separate premise above), it gives the median of what is known: the corner √(V₋·V₊) of
  any bounds, and H itself when what is known is symmetric in levels about H (Proposition 13). It does not lay the
  readings, which κ never touches. Carried to amounts, a far reading taken as an amount at V = H, the same indifference
  to scale motivates premise (S) of §6, which gives the logarithmic lay past the corner (Proposition 4): the bridge is
  the amount, and (S) stays a premise (§11.2, question 1). The lay and the even turn are different measures on the same
  reading: the even turn is how a sweep steps through attitudes, the lay how the reader places far readings, taken as
  amounts at V = H, past its own breadth.
- *The exchange's fixed point*: v = h, θ = 45°, the corner (Proposition 1).

The method is not ours. Three things in its use here are. The first is the group. Which transformations a situated
reader cannot detect is a statement about its situation, and we choose it as a statement of ignorance rather than derive
it from anything prior (§11.1). Jaynes phrases his rotation as the observer's: his problem "does not specify whether the
observer is facing north or east" (1973, §2); here the turn is the bar's attitude. The reader's group differs from his
in one respect: this reader stands somewhere. His straws are thrown at a circle that may lie anywhere, so his group
includes the translations, and the measure it gives on lines is Crofton's; on points of the plane, the measure that
translations and turns keep is area. A situated reader's lines all pass through home, and the transformations that keep
home where it is are the turns and dilations about it, multiplication of the plane's points by a complex number. The
measure they leave unchanged on the plane is dx·dy/(x² + y²) = dθ·dr/r: even in direction and even in levels of
distance, not even in area. Read from home, Bertrand's question has no single answer. For a circle of radius R whose
centre is at distance D ≥ R, the share of the chords cut by evenly turned rays that are longer than the side of the
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

Everything in this paper is read by someone, and what kind of reader it is decides what it can read. A reader's kind is
set by what it knows of the two breadths: not by where it is in the world, not by how many things there are, and not by
what arrives.

### 3.1 The situations

**The relations first.** A system is a set of unit relations, h, v, v₂ and so on, each between 0 and 1, each with its
breadth, H, V, V₂. A breadth may be known, which is the unsituated view, or not, which is the situated view. A situated
reader starts the geometry by choosing H and drawing every other party at it, V = V₂ = H. That gives the set of every
[h, v, v₂]: every way the relations can stand to one another, the unit cube of relations, whose directions are the wedge
and whose sum h + v + v₂ = 1 holds every point the truth could be (§2). The reader stands where the parties' rays meet
square: with the parties at the triangle's corners, (1, 0, 0), (0, 1, 0) and (0, 0, 1), the only points from which every
pair is seen at a right angle are the cube's corner, the reader's home, and its mirror across the triangle, (⅔, ⅔, ⅔).
With two parties those points make a whole circle through home, the circle on the chord of §4; with three they pin the
reader down. A reader's situation is how it holds the set, and it is given party by party: first for one other party,
the five below, then for two.

| situation | H | V | standpoint | how it reads | example |
|---|---|---|---|---|---|
| 0 | known | not known | none | nothing: H but no h, so no relation | — |
| 1 | known | known, equal to H | none | the whole at once | an equation: the circle h² + v² = 1 |
| 2 | known | known, unequal or varying with direction | none | the whole at once | an array: a shape's breadth in every direction |
| 3 | known | not known | the centre of the circle on the chord: a central angle | not pinned down; proposed: one hemisphere at once | the central sweep: it gets the payloads, what arrives |
| 4 | known | not known | home, a point of that circle: an inscribed angle | not pinned down; proposed: one direction at a time | the inscribed sweep: it gets the addresses to the payloads |

**Two sweeps, two results.** Situations 3 and 4 are two sweeps over the same facing, and they get two different things.
The central sweep, a radius turning about the centre of the circle on the chord, gets the payloads: what arrives, its
departure from the unit circle, read by its mean. If its law is taken to be unchanged by turns and its two components to
vary independently, it is normal (§7.1, "Why the payload is Gaussian"); that is a model under two premises, not a
consequence of the sweep. What the central sweep reads is centred on the payload's centre of gravity. The inscribed
sweep, a ray from home, a point of that circle, gets the addresses to the payloads: the places a reading can be put,
laid before anything arrives, whose law is the Cauchy, with its median at the corner and no mean (Theorem 6). What the
inscribed sweep reads is centred on that median, the address of the payload's centre. Neither is a reader standing
outside or inside a thing; each is a sweep, set by where it turns: the central sweep about the centre of the circle on
the chord, the inscribed sweep at home, a point of that circle; and each address points at its payload (§4, "The address
points at the payload"). How a reader makes either sweep, its mechanism, is not pinned down for either. The paper calls
them the central reader and the inscribed reader, and follows one proposal throughout: the central sweep taken in at
once, the inscribed swept one direction at a time from home, with static and dynamic saying why (§3.5). What it shows
that rests on the proposal (the bell and the fisheye, §7.1; which centre a reader can hold, §7.6) is shown of a reader
working that way, and attaches to situation 3 or 4 as far as the proposal holds (§11.2, question 8). Taking in a
hemisphere at once is not holding the whole: the whole at once is situations 1 and 2.

**The rule.** Three questions place any reader in exactly one situation.
1. Is anything related to the reader, so that it has an h? If not, it is in situation 0.
2. Does the reader know V? If it does, it holds the whole: situation 1 if V equals H in every direction, situation 2
   otherwise.
3. If it does not, which sweep does it make? The central sweep, turning about the centre of the circle on the chord,
   getting the payloads: situation 3. The inscribed sweep, from home, getting the addresses: situation 4. (On the
   proposal followed here, the first is taken at once, as when the thing holds still for the reader's look, and the
   second one direction at a time, as when the thing changes or arrives during the look; §3.5.)

Each question has two answers, and each answer either ends the questioning or leads to the next question, so every
reader lands in one situation and no reader lands in two: the five are exhaustive and do not overlap. Cases that look
like a sixth reduce to these.
- *V known only within bounds, or as a distribution,* is situation 3 or 4 with its one missing number known that way
  (§3.8). Its best estimate is then the corner of the bounds, or the median (Proposition 13).
- *H unknown* leaves no reader at all: H is the reader's own breadth and is always held. Situation 0 is H with no h.
- *A reader that reads in patches* is, on the proposal of §3.1, one at a time across the patches and at once within
  each; every single look is 3 or 4.
- *A system that changes kind* moves its reader from one situation to another over time (§3.5); at any one look the
  reader is in one.
- *Several readers* each have a situation of their own; what passes between them is the subject of §9.
- *More than two breadths* put the questions to each further breadth in turn: "Two other parties", below.
- *Directions along which nothing can arrive* are addresses still laid, with nothing met at them. That is a matter of
  payload, not of situation (Theorem 6(a)).
- *A thumb that changes between looks* changes no reading, since every reading is a ratio of amounts in one unit and
  the unit cancels (Proposition 8). Each look is then a reader of its own, joined to the others as several readers are
  (§9). Within one look, a wavering thumb blurs the reader's step (§8).
- *A reading of an area, or of any other power of the relation,* (v/h)^p with p > 0, keeps the order, the corner, the
  flip and the median, and only rescales the levels by p.

**Thumb and mountain.** Call the reader's breadth H its thumb and the other's breadth V the mountain. If the reader
knows the mountain's size, it holds the unsituated view: thumb and mountain are both in hand, and the corner, where the
thumb equals the mountain (v·V = h·H), is computed. If it does not know the mountain's size, it is situated, and the
only measure it has to give the mountain is its thumb: it sets V = H, mountain equals thumb (§5), and reads the mountain
in thumbs. Drawing the mountain at one thumb is required: only then is the sweep a turn and its readings the Cauchy
(§5, §7.1). How many thumbs the mountain really is, is a separate estimate. It changes no reading, only the amounts, and
one thumb is the best estimate when nothing says bigger or smaller (Proposition 13, §9). The corner v = h is still found
exactly, but the amounts there are the estimate's. The mountain's true size, V*/H thumbs, is the one number the situated
reader lacks (§3.8).

- **0, nothing.** The reader has its breadth H, as it always does, but no h: nothing is related to it, so there is
  nothing to read and no home to lay from.
- **1, the circle.** Both breadths known and equal, held whole as an equation, h² + v² = 1, from no standpoint. The
  corner is computed, at 45°, and there is no horizon.
- **2, every other shape.** Both breadths known but unequal, or varying with direction, held whole as an array: the
  breadth in every direction, known together. The corner is computed in each direction, and there is no horizon.
- **3, the central sweep.** A radius of the circle on the chord, it turns a half turn about that circle's centre, from
  one end of the chord to the other, twice the angle of the address it meets. It gets the payloads, what arrives over
  the facing, and reads them by their mean, the average departure from the unit circle.
- **4, the inscribed sweep.** A ray from home, it turns a quarter turn, from along the chord to square to it. It gets
  the addresses to the payloads, the Cauchy laid by direction, and reads them by their median, the corner. Its
  addresses' shares make a bell, and their running total is the fisheye (§7.1).

Situations 1 and 2 are the view from nowhere. They are mathematical views, an equation or an array, and they name a
state of knowledge, not a place anyone stands. Situations 3 and 4 are the view from somewhere. Both find the corner
exactly, since v = h needs neither breadth (§4); what they lack is the amounts there. Both meet a horizon that 1 and 2
do not have, and neither knows how many things there are.

| situation | the corner | horizon | its geometry | reads a line of true breadth 1 as |
|---|---|---|---|---|
| 1 | computed, at 45° | none | the circle | 1 |
| 2 | computed in each direction | none | the shape | 1 |
| 3 | found: v = h | the mathematical horizon | the bell | π/2 |
| 4 | found: v = h | the mathematical horizon | the fisheye; counted, the Cauchy | 2/π |

**Two other parties.** With V₂ the rule is put to each party in turn, and a reader's situation is one entry per party: 1
or 2 if that party's breadth is known, 3 if its sweep is central, 4 if inscribed. Situation 0 stays a single case,
nothing related and no h, and the five above are the one-party case. The two sweeps are the altitude, from H to V, and
the azimuth, which brings in V₂ (§2). The table and its examples follow the proposal above, the central sweep taken at
once and the inscribed one direction at a time; the readings, 2 and ½, are the vantages' own and do not depend on it.

| V, V₂ | what the reader has | example |
|---|---|---|
| both known (1 or 2 each) | the sphere, or another solid, held whole from no standpoint | a solid's equation; a three-dimensional array |
| one known, the other 3 or 4 | half-situated: one pair held, its corner computed; the other swept from home, its corner found | a sailor who knows a lighthouse's height but not how far the coast runs |
| 3, 3 | both sweeps at once: a hemisphere of directions in one look | a camera's frame |
| 4, 4 | both sweeps one direction at a time | a single-pixel scanner stepped through both angles |
| 3, 4 | the altitude at once, the azimuth one direction at a time | a rotating fan-beam radar; a slit panoramic camera |
| 4, 3 | the azimuth at once, the altitude one direction at a time | a horizontal line scanner tipped up step by step |

- **Both known.** The unsituated view in three dimensions: the solid held whole, its corners computed, no horizon. The
  truth is one point of the triangle h + v + v₂ = 1.
- **Half-situated.** Each party is asked separately, so one reader can hold one pair from nowhere and the other from
  somewhere. With V known it computes the corner of h and v and reads V's amounts exactly; V₂ it draws at H and sweeps,
  finding the corner of h and v₂ and reading V₂'s amounts up to the one ratio it lacks, V₂*/H. It is unsituated in one
  freedom and situated in the other.
- **Both central (3, 3).** On the proposal, a hemisphere of directions taken in one look, as a camera takes its frame.
  Read against its shadow on the base, the hemisphere reads 2, its surface being twice its base: the central reading of
  §3.4 for three unit relations.
- **Both inscribed (4, 4).** On the proposal, the reader steps through both angles. Its mean height over the hemisphere
  is ½, the inscribed reading for three unit relations, and 2 · ½ = 1, as π/2 · 2/π = 1 for two (§3.4). These are not
  the two-party readings squared, (π/2)² and (2/π)², but those times 8/π² and π²/8: the two sweeps of a three-party
  reader do not read as two independent two-party readers.
- **Mixed (3, 4) and (4, 3).** One sweep at once and the other step by step, as scanning instruments work: a radar's fan
  holds every altitude at once and turns through the azimuth; a line scanner holds a row of azimuths and tips through the
  altitude. What such a reader reads of a whole hemisphere depends on how its two sweeps are weighted (§7.1, "Swept by
  altitude and azimuth"), and is not taken up here.

With n other parties a situation is n entries, one per party, and the rule is the same.

### 3.2 Which division a reader can make

A reader turns a pair of breadths into a reading by dividing, and there are two ways to divide: by its own breadth, or
by the whole, taken as a sum or as a length. Which one a reader can make is its situation.

| divide both by | (H, V*) lands at | which lies on | needs |
|---|---|---|---|
| H | (1, V*/H) | the number line held upright at 1: unbounded | H only |
| the sum, H + V* | (H, V*)/(H + V*) | the chord h + v = 1: bounded | H and V* |
| the whole, √(H² + V*²) | (cos θ, sin θ) | the quarter circle: bounded | H and V*, and Euclidean length |

A situated reader has H, which it chose, and not V*, so it cannot form the whole; it can only divide by H, measuring everything in
thumbs. Every system it reads lands
on one unbounded line, at its ratio, with the scale gone and a horizon at the far end. An unsituated view holds both
breadths and can divide by the whole. Divided by their sum, every system lands on the chord h + v = 1, which needs
nothing beyond the two breadths and their addition; divided by their length, it lands on the bounded quarter circle,
which needs the Euclidean length as well (§5, "The Euclidean choice"). Either way the corner is computed, at the chord's
middle or at 45°, and there is no horizon. The chord comes first: the arc is the chord with a facing turned through
(§4), and the circle is that arc over every facing. The number line and the quarter circle are one projection apart:
projecting (1, x) toward the centre gives the circle's point.

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
- **3**, the central reader, holds the laid numbers at once (on the proposal of §3.1) and reads the unit line against
  the circle, θ/sin θ: rising from 1 toward π/2, approaching the line from above.
- **4**, the inscribed reader, takes one number at a time (on that proposal), projected onto the circle, and reads the
  circle against the unit line, sin θ/θ: falling from 1 toward 2/π, approaching from below. Its view is the unit line
  laid out as the fisheye.
- **0** has no unit, and nothing to lay.

Past 1, every number lands closer to the circle's top and the line's end, and the numbers out to infinity crowd into the
last stretch of both without arriving: the horizon, the same on both layouts. One construction gives all five. 1 and 2
are the quarter circle, held whole; 3 and 4 live on the unit line, and the two situated readers are the two ways of
comparing the layouts, line over circle and circle over line, with 1 between them. The unit line is the address space,
and the number line is what is addressed. Why the number line itself, unlike any reader's lay, has no corner is taken
up in §9.

### 3.4 Three vantages, and the true breadth

The five situations give three vantages, each with its own geometry. The completed view's own drawing is the sum,
h + v + … = 1 (§2); the two situated vantages are two of the drawings a standpoint builds from its sweeps, the two this
paper follows through, and not the only ones.

| vantage | situations | geometry | the turn | measure of a turn θ | reads a line of true breadth 1 as |
|---|---|---|---|---|---|
| completed: the view from nowhere | 1, 2 | the chord, and the circle drawn on it; every breadth held; no facing | none | none | 1 |
| central: a radius of the circle on the chord | 3 | one facing; the hemisphere turns away from the reader (proposed: taken in at once) | a half turn: the facing, from one end of the line to the other | θ/sin θ | π/2 |
| inscribed: a ray from home | 4 | one facing; the hemisphere turns toward the reader (proposed: swept from home) | a quarter turn: a bar, from home to the horizon | sin θ/θ | 2/π |

**Where the numbers come from.** A situated reader measures by turning. Its position crosses the line once, and its
facing turns; the arc is drawn by that turning, not walked. The two situated vantages turn by different amounts, and the
unsituated one not at all. The inscribed reader turns a bar of length 1 from home: at angle θ the bar's end has drawn an
arc θ, and the line it covers, its shadow, is sin θ. The central reader's facing turns twice as far, 2θ (§4, "Why the
corner sits at 45°"): it faces the far end of the line at the start, is square to the line at the corner, and faces the
first end at the finish, a half turn in all. Drawn on the line as its diameter, of radius ½, a turn of 2θ draws an arc
of θ over a chord of sin θ. So both draw an arc θ over a line sin θ. The central sweep reads arc over line, θ/sin θ; the
inscribed, line over arc, sin θ/θ. The two are reciprocal at every turn (the table's θ is the bar's; the central
reader's facing has turned 2θ):

| turned through | central, θ/sin θ | inscribed, sin θ/θ | product |
|---|---|---|---|
| almost 0° | 1.0000 | 1.0000 | 1 |
| 15° | 1.0115 | 0.9886 | 1 |
| 45° | 1.1107 | 0.9003 | 1 |
| 75° | 1.3552 | 0.7379 | 1 |
| 90° | π/2 = 1.5708 | 2/π = 0.6366 | 1 |

Both tend to 1 as the turn shrinks, and neither reaches it while there is any turn. At the limb, the central
reader's facing has made its half turn, an arc of π/2 stood on the line of 1 as its chord, and reads π/2; the
inscribed reader's bar has made its quarter turn, and its average shadow over the turn is (2/π)∫₀^{π/2} cos θ dθ = 2/π.
The central reader turns farther and the inscribed less, but as ratios the two lie equally far either side of 1, π/2
above it by the factor that 2/π is below it, and it is their product, not their difference, that returns the line: the
arc's excess over the line, π/2 − 1, and the shadow's shortfall, 1 − 2/π, add to 0.934, not to 1.

The average shadow is Buffon's needle (Buffon 1777): a needle as long as the gap between parallel lines, dropped at
random, crosses one with probability 2/π. Crofton's formula, which measures a curve by the random lines that cross it,
grew from the same problem (Crofton 1868). Buffon's number, like the inscribed reading, holds only when every angle of
the turn is equally likely; weight the turn otherwise and it changes.

Both readings come from the same two integrals over the quarter turn: the arc the turn draws, ∫₀^{π/2} dθ = π/2 (the
central reader's half turn, on radius ½, draws the same arc), and the shadow it casts on the line,
∫₀^{π/2} cos θ dθ = 1. The central reading is the turn over the shadow, π/2; the inscribed is the shadow over the turn,
2/π. Taken to any turn θ, the same two give the table's θ/sin θ and sin θ/θ. The shadow is the line itself: the steps of the turn, each casting
cos θ dθ, cover the breadth exactly once. Each reading sets it against the turn, one way up or the other, so their
product is 1. Without angles the turn is ∫₀^∞ ds/(1 + s²) over every relation s = v/h, and the corner halves it, π/4 on
each side. The true breadth, 1, is read only with no turn at all. From nowhere, then, a relation is the chord between its ends;
from somewhere it is the arc the reader turns through. The chord comes first: it needs no turn, and the arc is drawn on
it by one, where the rays the two facings sweep from its ends cross (§4, "The arc from the chord").

**With three unit relations.** Taken over a hemisphere instead of a half-turn, the same two readings are its area over
its shadow on the base, 2, since a hemisphere's surface is twice its base (Archimedes, *On the Sphere and Cylinder*),
and its shadow over its area, ½, the mean height over the hemisphere, since the height is even over a sphere (the
hat-box theorem). Their product is again 1. In n dimensions they are √π·Γ((n + 1)/2)/Γ(n/2) and its reciprocal: π/2 and
2/π for the circle, 2 and ½ for the sphere, 3π/4 and 4/(3π) next.

**Archimedes' proof, from nowhere and from somewhere.** Archimedes measured the circle from both sides (*Measurement
of a Circle*). A polygon inscribed in the circle falls short of it and one circumscribed about it exceeds it; doubling
their sides from 6 to 96 squeezed π between 223/71 and 22/7. Both polygons need the circle in hand: the inscribed one's
corners lie on it and the circumscribed one's sides touch it. His proof is the completed view, both sides held at once.

The inscribed reader's measure equals his inscribed polygon in number. An inscribed polygon of n sides has perimeter
n·sin(π/n) against the circle's π (both for a diameter of 1), and with θ = π/n that ratio is sin θ/θ. So the reading at
the quarter turn, 90°, is the polygon of 2 sides, 2/π; at 45° it is the square, 0.9003; and halving the turn matches his
doubling of the sides, each step bringing the reading about four times closer to 1:

| sides | turn θ | inscribed, sin θ/θ | short of 1 by |
|---|---|---|---|
| 2 | 90° | 0.6366 = 2/π | 0.3634 |
| 4 | 45° | 0.9003 | 0.0997 |
| 8 | 22.5° | 0.9745 | 0.0255 |
| 16 | 11.25° | 0.9936 | 0.0064 |

A situated reader draws neither polygon. Both need the circle in hand, and it does not hold the circle: the inscribed
polygon's corners lie on the circle just as the outer polygon's sides touch it. What the reader has is its own turn,
swept step by step from home. Its reading sin θ/θ is a reading of that turn, not a polygon laid on a circle; it equals
the inscribed polygon's share in number, but the reader never holds the polygon. The central reader reaches it the same
way, as a number, through the flip, θ/sin θ = 1/(sin θ/θ): so it knows π/2 at the limb from its own turn, and
π/2 · 2/π = 1 stands in for the circle it does not hold. (Archimedes' outer polygon goes as tan θ/θ rather than
θ/sin θ; both lie above 1 and close on it at the same rate.) Archimedes squeezed π between two polygons because he held
the whole; a situated reader holds neither polygon and has the same numbers from its own turn and the flip. The
convergence is ordinary geometry; what the vantages add is what each reader holds.

The reader's own turn gives the halvings without a polygon. Halving a turn takes out one cosine,
sin 2θ/2θ = cos θ · sin θ/θ, so the inscribed reading at the quarter turn is a product with one factor per halving, the
first at the corner:

  2/π = cos 45° · cos 22.5° · cos 11.25° · … = (√2/2) · (√(2 + √2)/2) · (√(2 + √(2 + √2))/2) · …

This is Viète's formula (Viète 1593). After n factors the product is 2/π divided by the share of the inscribed polygon
of 2ⁿ⁺¹ sides, so it closes on 2/π at Archimedes' rate, about four times closer with each halving: 0.7071, 0.6533,
0.6407, 0.6376, ….

**From the vantages to the view from nowhere.** The argument runs in seven steps, each resting on the one before.
1. A line has a true breadth, 1. That is what the completed view reads.
2. Each situated vantage reads it through a facing: the hemisphere turned away reads π/2, the hemisphere turned toward
   reads 2/π, and π/2 · 2/π = 1.
3. Reading 1 assumes no facing, nothing turned toward or away from the reader. A situated reader always has a facing,
   so no situated observation reads 1.
4. Only an observer with no standpoint has no facing, so only it holds the true breadth. A blueprint is the example:
   drawn from no standpoint, every line at its true length to one scale, nothing turned toward or away from anyone.
5. To hold 1 is to hold both hemispheres in hand at once, which no single observation can do. That is what "the view
   from nowhere" means: the true breadth belongs to no standpoint.
6. So a situated reader that wants the true breadth can only construct it from several observations: the hemisphere turned away and the one
   turned toward, read in turn and joined. The construction represents the true breadth; it does not observe it. A
   telescope survey is the working example. One exposure is one facing from one standpoint, and the survey is the
   construction. Not every combination builds: exposing the same field again lowers the noise and adds nothing;
   pointings joined at their overlaps give the shape up to a scale; only a second standpoint at a known baseline gives
   a distance (§10 works one through).
7. There are therefore two ways to the true breadth, and only two: held, unsituated, as in a blueprint; or constructed,
   situated, from several observations.

The arithmetic of steps 1 and 2 is exact. Which vantage reads which measure, and steps 3 to 6, are a reading of that
arithmetic, not a theorem. The "only two" of step 7 is exact, as the next paragraph shows.

**Why only two.** The limit in steps 3 to 6 is exact, not an intuition about perspective. Every reading a situated
reader takes is a ratio of two amounts, so multiplying every amount in the scene by one factor leaves every reading
unchanged. No collection of readings, from however many standpoints, can therefore fix the scale, and one amount
supplied from outside the readings fixes it (Proposition 8, §9). "Only two" means this: the true breadth is either held,
or an amount is brought in from beyond the single reading and the rest is constructed from it. Calibration against a
standard, a baseline of known length and prior knowledge of a size are all ways of bringing that amount in. They belong
to the second route; they are not a third.

Each vantage's reading is right from where it stands. Many apparent paradoxes come from reading one vantage's geometry
as if it were another's, most often from treating the completed view as if one observation held it.

**What the completed view costs.** In h² + v² = 1, h and v are not compared with each other. Each is compared with the
equation, which supplies the common scale, the constant and the equals sign: the equation is a third party. A completed
account holds the whole figure and so cannot state an order of arrival; a situated account states the order of arrival
and cannot hold the whole figure. And the point on which the situated reading turns, the corner, is an unremarkable
point of the completed drawing.

### 3.5 At once or one at a time: static and dynamic

At once and one at a time say how a situated reader reads, on the proposal this paper follows for situations 3 and
4, which are set by the vantage, their mechanism not pinned down (§3.1); static and dynamic say why. A system is
*static* to a reader if it holds still for the whole look, so that the reader can take its facing side at once: on the
proposal, situation 3. It is *dynamic* if it changes or arrives during the look, so that the reader takes it one part
at a time: on the proposal, situation 4.
- *Both are situated.* Static and dynamic part 3 from 4, not situated from unsituated. The equation and the array of 1
  and 2 are held whole, with no reader standing anywhere.
- *It is measured against the reader's look, not the system alone.* A building that does not move is read one part at a
  time by someone walking through it, and a moving flock is read at once by a photograph.
- *Arrival makes a reading dynamic, as change does.* A system that holds still is still read one part at a time when
  news of it reaches the reader over time, nearest first.
- *It is not a matter of dimension.* Static is not "three dimensions" and dynamic is not "three dimensions plus time".
  Both read the same sweep, 0 to π/2, one laid across at once and one turned step by step.

A system can change kind, and the reader must follow. A dynamic system can settle (on the proposal, 4 becomes 3), and once its breadths
are in hand it is held whole (it becomes 2). When a system settles, the levels read one at a time can serve as the
addresses of a reading at once, and the reader need not start again. When a static system starts to change, a reader
that lays its sweep once keeps a stale picture; only reading again and comparing, one look after another, shows the
change. So a reader that may face either kind keeps some such check running. In both directions the reader
infers the change rather than seeing it: a system that changes more slowly than the look, or more finely than the
reader resolves, looks still.

### 3.6 What a situated reader holds, and where it stands

The unsituated view has coordinates x, y and z, any of which a rotation turns into another. Situated observation is not
built that way, and it is not a number of dimensions. It consists of five things, each reached through the one before:
- *relations*: v over h, the turn from horizontal to vertical;
- *addresses*: a relation laid from home, in a facing;
- *the sweep's progress*, g = (2/π)·arctan(v/h): 0 at pure horizontal, where nothing of V is expressed, and 1 at pure
  vertical, where V is fully expressed, with the corner at ½ and g(h/v) = 1 − g(v/h);
- *the share* of a reading: v as a share of h before the corner, h as a share of v past it;
- *magnitudes*: the world's, one value at each address, met, not swept.

A reader *divides* (v by h, leaving a relation with no scale), *sweeps* (lays the relation from home, step by step) and
*points* (each address reaches a magnitude, an amount v·V*, which needs V*). Dividing and sweeping are addressing, and can
be done before anything is there; the magnitude is the world.

**The reader is the pivot.** Draw the relation as a bar that turns, about one fixed end, from pure horizontal to pure
vertical. The free end traces the sweep, and the reader is the fixed end. It sits off the sweep and points along the bar
to it.

| on the sweep | the bar | v/h | the share |
|---|---|---|---|
| home, the start of the sweep | pure horizontal: all h, no v | 0 | 0 |
| the corner | at 45°: v = h | 1 | 1, on both sides |
| the horizon, the end of the sweep | pure vertical: all v, no h | → ∞ | 0 |

Facing the corner, the reader has the near side's [0, 1] before it and the far side's [0, 1] behind it. At the pivot v
and h are both 0, and v/h is 0/0: the reader is the one point with no reading and no address of its own. It lives in
the circle its own choice creates (§5), at the centre, and is not the circle. It points and is not pointed to, except as
the payload of another reader's address (§7.7).

**h as the focus.** An intuition, not a result: h is not one of the things a reading sweeps but what the sweep is
relative to, the reader's focus. The reading v/h asks where v lies against the focus, which is why scale drops out. The
corner is the thing read sitting at the focus, and the flip is the thing read crossing the focus while the focus stays
put. Changing the focus rescales every reading, and nothing in the world changes.

### 3.7 The hand

Hold your hand out flat: that is h, home. Turn it until it points straight up: that is v, toward the horizon. The
motion between is the sweep, and the hand treats the two alike because they share one denominator, the hand itself:
the situated reader's V = H (§5) is its own hand. Spread the fingers between flat and upright: each finger is an
address, one ray of the relation. Put a ring on each finger: the ring is what that address holds, the payload. Turning
the hand does not change the rings. Replace the rings with others, and the sweep from flat to upright is the same sweep,
each finger the same address.
- *The thumb is H.* The hand's own measure is its thumb, the reader's breadth, the value it starts from; the mountain it looks at is V. Setting
  V = H is reading the mountain in thumbs.
- *The geometry is the hand, not the rings.* Dividing v by h keeps the finger and drops the ring.
- *The inscribed reader is the hand and its fingers; the central reader holds the rings.* One steps through the addresses; the
  other keeps the magnitudes, all at once (on the proposal of §3.1).
- *The rings hide; the hand does not.* Two rings on one finger, seen along it, show only the nearer: the ring behind is
  the back side. The hand hid nothing; the rings did.
- *The far field's doublings are fingers.* Past the corner the levels are doublings (§6), addresses laid before
  anything arrives; what lands on them is rings. The fingers sit side by side on one hand, not one inside another.
- *The situations in the hand.* 0: no hand, nothing to point with and nothing pointed at. 1 and 2: the rings held
  whole, all at once, with no hand needed to reach them; in 1 every ring is alike, in 2 they differ. 3: the central
  sweep, which gets the rings, the payloads. 4: the inscribed sweep, which lays the fingers, the addresses to the rings.
- *The hand has two sweeps.* Raised, it sweeps from flat to upright, from H to V: the altitude. Turned, it sweeps
  round from pointing at the other party to pointing square to it, which brings in a second other party, V₂: the
  azimuth. Every way the hand can point, within one facing of each freedom, is one altitude and one azimuth, as every
  point of an observer's sky is (§2).
- *The unit circle is the hand's own arc.* In one facing it is a quarter, flat to upright, open at the top, since no
  finger is ever the horizon. The closed circle comes from turning the hand through its facings, or from nowhere,
  drawing every facing at once. The sphere is every way a hand could face, drawn from nowhere; no hand holds it.

### 3.8 What the reader lacks is one number

The situations can be written in terms of one another. A situated reader, 3 or 4, is a shape of situation 2, read
through situation 1's assumption, with situation 0's unknown on one side only. The world is a shape like any other,
with some breadth ratio; lacking it, the reader lays its readings as if the shape were the circle.

Assume a value for V*, and situation 3 or 4 becomes situation 2. With directions spread evenly (§7.1), the readings in
amounts are (v·V*)/(h·H) = b·(v/h), where b = V*/H. Counted in doublings of the amount ratio, the readings for b = 2 are
those for b = 1 slid up exactly one doubling, every doubling's share unchanged:

| doubling of the amount ratio | ¼ to ½ | ½ to 1 | 1 to 2 | 2 to 4 | 4 to 8 |
|---|---|---|---|---|---|
| b = 1 | 0.139 | 0.205 | 0.205 | 0.139 | 0.077 |
| b = 2 | 0.077 | 0.139 | 0.205 | 0.205 | 0.139 |

So what a situated reader lacks is one number, how many thumbs the mountain is, V*/H; on the count of doublings it is an
offset, log₂(V*/H), not a change of pattern. Situation 2 knows the number; 3 and 4 do not; known within bounds, they know it within bounds. Assuming it
clarifies the reading; it does not simplify it.

## 4. The corner

**Proposition 1.** Let x = v/h ∈ [0, ∞). Then x = 1 is the only point fixed by the flip x ↦ 1/x. The flip carries
[0, 1) onto (1, ∞) point for point, and every sweep from home passes through x = 1. This point depends on neither H nor V.

*Proof.* The flip is its own inverse and reverses order, so x < 1 exactly when 1/x > 1, and for x > 0, x = 1/x gives
x = 1. A sweep from home grows continuously from 0, so it reaches 1 before it can pass it. Finally, x = 1 means v = h, a
comparison of two unit relations, unchanged when both are scaled together. ∎

We call this point the *corner*. It is ordinary arithmetic, and nothing about it is special beyond what follows from
that. Its importance is that it separates two ways of reading: before it, v is read in terms of h; past it, h in terms
of v. Near and far are one geometry, read from either side.

**Proposition 2.** (a) Let a reader hold x in two registers: x itself where x ≤ a, and 1/x where x > a. Both registers
stay within [0, 1] if and only if a = 1. (b) Let f : [0, ∞) → [0, 1] be strictly increasing and treat the two sides
alike, f(1/x) = 1 − f(x). Then f(1) = ½, and f maps the near side below ½ and the far side above it.

*Proof.* (a) The registers take values in [0, a] and (0, 1/a); both lie in [0, 1] exactly when a ≤ 1 and 1/a ≤ 1.
(b) At x = 1 the condition reads f(1) = 1 − f(1); the rest follows from monotonicity. ∎

Part (b) assumes the reading is *fair*: it treats the two sides alike, although the reader's knowledge does not, since
it knows H and not V. Without fairness a bounded reading such as x/(2 + x) has its middle at x = 2. Fair readings include
the line's share v/(v + h) = x/(1 + x) and the arc's v²/(h² + v²) = x²/(1 + x²).

**Series stop at the corner.** The expansion 1/(1 + x²) = 1 − x² + x⁴ − … converges for x < 1 and diverges for x > 1;
past the corner the expansion in 1/x converges instead. The singularities at x = ±i lie at distance one from home, so no
expansion about home reaches past the corner. This is a property of expansions, not a break in the function, but it is
one reason near and far seem to obey different mathematics.

**Comparing without dividing.** For two readings A = (h_A, v_A) and B = (h_B, v_B), let D = v_A·h_B − v_B·h_A. With h_A
and h_B positive, D = 0 exactly when the two ratios agree, and D > 0 exactly when v_A/h_A > v_B/h_B. Comparing a reading
with its own flip gives D = v² − h², which is zero exactly at the corner. Sameness, order and the corner need no
division; only the size of D depends on scale.

**Why the corner sits at 45°.** A straight segment from A to B passes once through every ratio of the two, as the
quarter arc does. The arc has a second degree of freedom that the segment lacks: the direction it faces along the way.
The arc is drawn by that turning, not walked: the reader's position crosses the segment once while its facing turns
(§3.4). If the bar pivots at a point of the circle, as in Thales' configuration, a turn of θ moves its far end through a central
angle of 2θ (the inscribed-angle theorem), so the facing turns twice as fast as the sweep, from facing B at A to facing A
at B. At the corner, θ = 45° and the facing is 90°: square to AB, leaning toward neither party. There the arc stands
farthest from the segment, by 1 − 1/√2.

**The arc from the chord.** The arc can be had from the chord AB without turning a bar. Stand the two parties at
its ends, and from each end sweep a ray: from A a ray reading v/h, from horizontal along AB up to vertical, and from B
a ray reading the flip, h/v, from vertical down to horizontal. Where the two rays cross traces the semicircle on AB.
With A = (0, 0), B = (1, 0) and A's ray of slope s = v/h, the crossing is P = (1, s)/(1 + s²); the rays meet at a right
angle, so P lies on the circle with AB as diameter (Thales' theorem, Euclid's *Elements* III.31, with its converse).
Its distances from A and from B are h and v, the chord is the hypotenuse, and h² + v² = 1 is Pythagoras on it; the
foot of P cuts AB into h² and v², and its height is hv, their mean proportional (*Elements* VI.8). Seen from the middle
of AB, P has turned through 2α when A's ray has turned through α (the inscribed angle theorem, *Elements* III.20): the
facing turning twice as fast as the sweep. The reading is the tangent of half the facing φ, so
cos φ = (1 − s²)/(1 + s²) and sin φ = 2s/(1 + s²), and a rational reading gives a rational point (Euclid's formula for
Pythagorean triples). At the corner, s = 1, both rays stand at 45° and P is over the middle of AB; the flip s ↦ 1/s
mirrors P across the perpendicular bisector. In classical terms this is Steiner's construction of a conic (Steiner
1832): the lines through A and the lines through B are paired by a projective correspondence, slope s with slope −1/s,
that does not pair AB with itself, so corresponding lines meet along a conic through A and B. It is a circle because
the pairing turns each line through a right angle, and that needs h and v drawn at one length: drawn with v at c times
h, the same readings cross on the ellipse x² − x + y²/c² = 0. Paired at equal angles instead of by the flip, the rays
meet on the perpendicular bisector, a line. Sweeping A's ray in equal steps moves P in equal steps along the arc, so
the even sweep of one ray is the even turn of §7, and its readings are the Cauchy's. Over two amounts x₁ and x₂ laid
end to end, the crossing above the join stands at √(x₁x₂), Euclid's mean proportional (*Elements* VI.13), which is
the H that sets the two furthest apart (§8). The chord comes first; the arc is where the two facings' rays cross. With
three parties at the corners of the triangle h + v + v₂ = 1, rays meeting with every pair square meet only at the
cube's corner, the reader's home, and its mirror across the triangle: the arc of two parties becomes, for three, a
single standpoint (§3.1).

**The address points at the payload.** The two sweeps of §3.1 meet on this arc, one point at a time. The inscribed
sweep is A's ray: from home, a point of the circle on the chord, it turns through the inscribed angle θ from along the
chord, and at each step it is an address, the reading s = v/h = tan θ, laid before anything arrives. The central sweep
is the circle's radius: it turns about the middle M of the chord through the central angle, from pointing at B. The
payload is what is found where that radius ends. The ray at θ and the radius at 2θ end at the same point P of the arc,
for every θ. That is the inscribed angle theorem (*Elements* III.20): an angle at the circle is half the angle at the
centre on the same arc, and P is its one shared point. So the address computed by the inscribed sweep points directly
at the payload reached by the central sweep. It does so in five ways.
- *Exactly, and once.* Each address meets one point of the arc, and each point of the arc has one address. The map
  keeps the order: the address along the chord, θ = 0, points at B itself, the other party, where the radius starts;
  the corner, θ = 45°, points at the top of the arc, where the radius stands square to the chord; the horizon, θ → 90°,
  points at A's own end of the chord, where the radius has made its half turn.
- *At the other party's shadow on the address.* The angle APB is right (*Elements* III.31), so P is the foot of the
  perpendicular from B onto the ray: what the address finds is the other party projected onto it. It lies at distance
  h from home and v from B, its foot on the chord at h² and its height hv (*Elements* VI.8).
- *Without the payload in the address.* The address is the ray and its reading; the payload is what is at P. What
  arrives there changes nothing in the address, since the reach of what arrives along a ray cancels from its reading
  (Theorem 6(a)). The inscribed sweep can lay every address before anything arrives, and each still points at where its
  payload will be.
- *In the two readings.* Read along the ray, line over arc, the inscribed sweep gives sin θ/θ, 2/π over the whole
  turn; read along the arc, arc over line, the central sweep gives θ/sin θ, π/2 (§3.4). One point, named twice: by its
  direction from home, its address, and by the facing of the radius that reaches it, the payload's place.
- *Only with V = H.* Drawn with v at c times h, the same rays cross on the ellipse x² − x + y²/c² = 0 (above). Each
  address still meets one point, but the radius no longer turns twice the address's angle, and the corner no longer
  points at the top. The direct pointing is a property of the circle, so of the drawing V = H (Proposition 3(e)).

The inscribed sweep lays the addresses; the central sweep reaches, at each, the payload that address points to. The
reader's addresses and the world's payloads are joined point for point by one classical theorem, and the join needs
nothing the reader lacks: no amount, only the drawing.

**Why there are two sweeps, and only two.** The two sweeps are often pictured as reading the arc from outside and from
inside. Structurally the difference is only where the pivot stands. A sweep is a ray turning about a pivot, and a reader
counts its steps of turn. For those steps to stand for steps along the arc, equal turns must reach equal stretches of
arc wherever the ray points. Only two kinds of pivot do this.

- *The centre.* A ray from the middle M of the chord is a radius. Each step of turn moves its end by the same step of
  arc, at rate 1.
- *A point of the circle.* From a point A on the circle, a ray turned through θ reaches the point whose central angle
  from B is 2θ, wherever it points (the inscribed angle theorem, *Elements* III.20). Each step of turn moves its end by
  twice that step of arc, at rate 2.
- *Anywhere else.* Take the radius as 1 and a pivot P inside the circle at distance p from the centre. A ray from P
  meets the arc ahead at distance t and behind at distance t′, and a step of turn dψ moves the point ahead by 2t/(t +
  t′)·dψ of arc. That is 1 − p looking straight away from the centre and 1 + p looking straight toward it. Equal turns
  reach unequal arcs, unless p = 0, or unless the point behind is the pivot itself, t′ = 0, which happens just when P
  lies on the circle. From a pivot outside the circle the rate grows without bound toward the two rays that graze it. In
  classical terms, the angle at a point inside a circle is half the sum of the two arcs it cuts off, and at a point
  outside half their difference; only at the centre and on the circle does one arc alone fix it.

So an even sweep of a circle has two places to stand, and no third. The points of the circle that matter are the two
parties, home A and the other end B of the chord. The centre is the chord's middle, which belongs to the pair and is
neither party's standpoint. The inscribed sweep is the sweep a party makes; the central sweep is the sweep the pair's
middle makes.

**What each sweep reads.** The two pivots name the same point of the arc in two ways.

- *From a party.* Read A's ray at θ where it crosses the line touching the circle at B: its height there is s = tan θ =
  v/h. This is projection from a point of the circle onto a line (stereographic projection; in the half-angle form s =
  tan(φ/2), with φ the central angle). It carries the whole circle but A itself onto a whole line, so its readings are
  unbounded: as the ray turns toward the tangent at A, square to the chord, s runs to the horizon. An even turn laid on
  that line is the Cauchy law (§7.1): its median is at the corner, and it has no mean.
- *From the pair's middle.* The radius at 2θ ends at ½(cos 2θ, sin 2θ) = ½(h² − v², 2hv). With h + iv for A's direction,
  that end is ½(h + iv)²: the central sweep's point is the inscribed sweep's direction squared. Its coordinates are
  bounded by the radius, so every average over an even turn exists: cos 2θ averages 0 and sin 2θ averages 2/π.

The factor of two between the sweeps is that square. It is why the radius turns twice as fast as the ray, why the
address at θ points at the payload at 2θ (above), and why one sweep's readings are ratios and the other's are squares.
Read at one address, the two are easily confused. The inscribed sweep's addresses crowd on the line with density
2/(π(1 + s²)) = (2/π)·h²: at every address, the inscribed reading 2/π times the foot of the point that address points
to. The two have one shape, but they are different things. The density must be summed over a stretch of addresses to
give a share, and summed it is the arctangent, not h². The foot is already a share of the chord. At the corner the
density is 1/π and the foot ½. A party's sweep reads ratios, of the first degree, unbounded, and is read by the median.
The pair's middle reads squares, of the second degree, bounded, and is read by the mean. Both rates are exact only on
the circle. Drawn on the ellipse of a stretched drawing, the inscribed angle theorem fails and neither pivot turns an
even sweep into an even arc. So the two sweeps, like the pointing, need the drawing V = H (Proposition 3(e)).

**What the flip gives, and what it does not.** The flip proves that the corner is the one point it leaves fixed, that
every sweep passes through it, that a reading kept within [0, 1] on both sides must change register there (Proposition
2(a)), that a fair reading puts it at the middle (Proposition 2(b)), and that expansions about home stop there. It does
not prove that the drawing is a circle: paired by the flip, the rays from the two ends cross on a conic, and only
Euclidean measure, the right angle drawn at one length, makes it round (above, and §5); how readings past the corner are laid out,
which needs the premise that no scale is preferred (§6); or the weight with which the sweep is counted, which needs
even steps of turn (§7). Each of these rests on its own premise, and we name it where it enters.

**Every pair has its own corner.** Any two parties have a sweep and a corner, and the corner of one pair is not the
corner of another. A corner means nothing until its pair is named. In the wedge the corner is the central ray. With
three unit relations the three pairwise corners, v = h, h = v₂ and v = v₂, are planes through the central ray v = h = v₂, and
they cut the wedge into six chambers, one for each ordering of the three unit relations.

## 5. The reader's circle

We assume three things.
- **(P0)** A relation requires two unit relations, one for each party, each relating it to an assigned breadth: h to
  H, v to V. Assigned is not known: v lies in [0, 1] however large the party truly is, but it must relate to
  something.
- **(P1)** A situated reader chooses exactly one breadth, H, the value it starts from, and holds no whole of the system.
  H is not a measured size, and any H will do.
- **(P2)** A level carries no measure: nothing on it but its two ends, their order and the flip between them.

**Proposition 3 (the reader's circle).** Under (P0) and (P1):

(a) the reader must assign V in its own unit, V = cH for some c > 0, and no unit relation and no single reading
depends on c;

(b) with V = H, the corner lies at distance 1 from home, whatever H was chosen;

(c) if the attitudes of the relation are turns of one rigid bar, the relation traces the unit circle h² + v² = 1;

(d) with n freedoms each set to H there are 2ⁿ facings: 4 for the circle, and 8 octants for the sphere
h² + v² + v₂² = 1, where v₂ is a second v read against the same h;

(e) the attitudes are turns of one rigid bar only if V = H: with c ≠ 1 nothing turns all of h into all of v, and there
is no circle;

(f) with two other parties, assigned V and V₂, the attitudes are the directions of one rigid bar, the sphere
h² + v² + v₂² = 1, only if V = V₂ = H;

(g) the bar can be derived rather than assumed. Take a sweep that is uniform (every step the same linear map of the
plane of all-h and all-v), that returns to its start after one full turn, and that carries all of h into all of v in a
quarter of it. Such a sweep preserves an inner product, unique up to a positive factor.
- In that inner product, all of h, all of v and every attitude between them have one length, and all of v is square to
  all of h.
- At the sweep's own parameter t, the unit relations are (h, v) = (cos ωt, sin ωt): the unit circle of (c).

So the sweep is the turning of a rigid bar in its own measure, and it draws V = H there. The one factor left free is H.

*Proof.* (a) By (P0) the other party must be assigned a breadth for there to be a relation, and by (P1) the reader's
only breadth is H, so the assignment is H times a number c. A unit relation v lies in [0, 1] however large V is, so no
reading involves c; c multiplies only the amounts v·V. (b) The corner is one H from home measured in H: H/H = 1. A reader with unit λH reading a world scaled
by λ receives exactly the same readings, so nothing in the readings fixes H. (c) With one unit, the relation is a bar of
length 1 whose attitudes are mixes of all-h and all-v, so h² + v² = 1 when length is Euclidean, and the Euclidean norm
is, up to scale, the only norm preserved by every turn. With two units the same bar would trace an ellipse stretched by
V/H. (d) Once both parties share a unit nothing prefers one side of a freedom, so each freedom has two facings. A closed
walk through the facings must flip each freedom an even number of times, so the facings are the 2ⁿ vertices of an
n-cube, walked as a Gray code. (e) A turn keeps the bar's length. All of h is the bar at length H and all of v the bar
at length cH, so a turn carries one to the other only if c = 1. With c ≠ 1 the tip must stretch on its way, along the
ellipse of (c) or some other path. (f) By (e) applied to each pair: all of v and all of v₂ must each be the bar at
length H.

(g) Write the sweep as g(t) = exp(tA), with A ≠ 0 and T the least time with g(T) = I.
1. A real 2 × 2 matrix with exp(TA) = I has eigenvalues ±iω, with ω = 2π/T. A pair of zeros would make A nilpotent,
   and then exp(TA) = I + TA ≠ I.
2. So A = P(ωJ)P⁻¹, with J the generator of turns, and g(t) = P·R(ωt)·P⁻¹. This preserves Q(x) = |P⁻¹x|².
3. Suppose a symmetric form B is preserved by every g(t). Then PᵀBP is preserved by every turn, so it commutes with J;
   being symmetric, it is a multiple of the identity. So B is a multiple of Q.
4. Let u = P⁻¹(all of h). Since all of v = g(T/4)(all of h), P⁻¹(all of v) = R(π/2)u. The two are square to each
   other and of one length in Q.
5. Then g(t)(all of h) = cos ωt·(all of h) + sin ωt·(all of v), so (h, v) = (cos ωt, sin ωt), and every point of the
   orbit has the same Q.

A page drawn at V = cH with c ≠ 1 shows the same sweep in coordinates other than its own. Its unit relations at the
sweep's parameter are unchanged; only the page's angles differ, which is the c of Proposition 5(d). ∎

**What the geometry needs: a shape and one H.** Neither is a measured size. The shape is set by how many unit
relations the system includes: by (d), n of them give the sphere in n dimensions, with 2ⁿ facings, so two give the
circle and three the sphere, once their wholes are drawn at one length, (e) and (f), and their attitudes are turns of
one bar, (c). The H starts it: some H is needed, but by (b) every H gives the same shape and the same corner, and its
value sets only the zoom, which things fall in the near field and are read finely (§8). No party's true size enters
the geometry.

**What V = H means.** Setting V = H is a rule of representation: the reader uses its own breadth as the unit for the
other party. It sets the mountain equal to its thumb because its thumb is the only measure it has. It is not a claim
that the mountain is the size of a thumb. Where it is not, every amount the reader reads is off by V*/H, the
number of thumbs the mountain really is (§9). The rule constructs a relation calibrated in one unit and discovers nothing about the world.
Step (a) is close to a definition; we claim only that a relation needs two assigned breadths and a situated reader has
one. Which breadth it assigns is not free:
- *What c would change.* No unit relation, no corner v = h and no single reading depends on c. But with c ≠ 1 all of h
  and all of v are drawn at different lengths, so the sweep between them is not a turn (part (e)). The tip stretches
  along an ellipse of axis ratio c, the point of equal amounts, v·V = h·H, slides log₂ c levels off the corner, and
  "sweeping evenly" no longer names one sweep: even steps of direction, of the curve and of its parameter give three
  different laws, and only one of them is the Cauchy with its median at the corner (Proposition 5(d)).
- *Why c = 1.* With V = H the sweep is one rigid bar turning, it traces the unit circle, and the even turn is unique;
  its readings are the Cauchy with nothing more chosen. Working back from the Cauchy, which is known, arrives at V = H
  and nowhere else (Proposition 5(d)). So V = H is required for a situated geometry built on a turn: it gives the
  reader a circle to turn. Unit relations drawn on equal axes, each running from 0 to 1, are this drawing.
- *What c = 1 does not do.* It does not say how large the mountain is. The mountain's true breadth, V*, is a separate number,
  unknown within one observation. The reader may estimate it, and the best estimate is the median of what it knows
  (Proposition 13, §9), but the estimate enters only the amounts, as a shift of every one of them by the same number of
  levels. It never redraws the circle.

**Two choices, and a number that is not one.** The reader makes two choices in turn, and they differ in kind.
- *H, the reference.* It is free. Every H gives the same circle and the same corner (part (b)), and its value sets only
  the zoom (§8).
- *c, the representation, V = cH.* It is not free. c = 1 is the only value for which:
  - the sweep is one rigid bar turning (part (e));
  - the even turn's readings are the Cauchy, with the median at the corner and unchanged by the flip (Proposition 5(d));
  - a lighthouse's 45° flash is the corner of its landings (Proposition 5(f));
  - a chart draws every compass bearing true (Proposition 5(g)).

  Any other c is a consistent drawing, but it gives up all four. By part (g), it is the same sweep described in
  coordinates other than its own. A uniform sweep that returns after a full turn has its own measure, unique up to a
  factor, and in that measure V = H. The factor is H.
- *V*/H, the true size.* It is not a choice. The readings never give it (Proposition 8). It is estimated at the median
  of what the reader knows (Proposition 13), and corrected by a shift in levels when an amount arrives.

Changing H rescales the drawing in both directions alike, which is a zoom. Changing c stretches it in one direction,
which changes its angles and moves its corner off 45°. These are the two effects Proposition 5(f) and (g) keep apart.

Neither choice can be declined. Without a breadth for the other party there is no relation (part (a)). An H that
favours no value is one taken to its ends, 0 or ∞. There the reader's lay becomes one of the rulers of Proposition 14
that favour no amount. It has no corner, and a reader with finitely many addresses loses what it reads: all of it
falls into the first address, or past the levels held (§9). So some H must be chosen; which one sets only the zoom.
The estimate of the true size is not left open either: with nothing known either way, it is H itself (Proposition
13(c)).

**The Euclidean choice.** Part (c) is where an assumption enters. One unit makes the axes commensurable, but "a bar of
fixed length" also needs a norm: under the largest-component norm the bar traces the square, under the sum norm the
line. The circle follows if the sweep is the turning of a rigid bar. The facing of §4 motivates that; it does not prove
it. Part (g) narrows the assumption. A sweep that is uniform and returns after a full turn is the turning of a rigid bar
in its own measure, which is Euclidean and unique up to the factor H. What remains assumed is that the sweep is uniform
and acts linearly on the mixes of all-h and all-v. The same circle comes without a bar, from the chord and the two
facings' rays (§4, "The arc from the chord"); there the Euclidean measure enters as the right angle at which the flip
pairs the rays, drawn with h and v at one length, and without it the crossings are still a conic, an ellipse. Less rests
on the Euclidean choice than it seems. The readings are directions only (Theorem 6(a)), so the norm reaches them only
through the measure on directions that "sweeping evenly" uses; laid by direction, every path gives the same readings
(§7.4). Swept evenly along their own paths, the square and the line give other laws, with the same median at the corner
and no mean (Theorem 6(e)). What the circle and the even turn add is the Cauchy's exact shape.

**What the count of facings borrows.** The count 2ⁿ needs no angle. That the facings tile the circle or the sphere in
equal shares, a quarter turn each or π/2 of the sphere's area each, is the Euclidean measure of (c), not part of the
count.

**Diameter 2.** The corner has two sides and only two. The reader's own level runs from home to the corner in every
facing: radius 1, diameter 2, the near field. Measured in the reading v/h, the next level runs from 1 to 2, and level k
ends at 2ᵏ. We read the 2 across the reader's own level and the 2 between levels as the same 2, the corner's two sides;
this is a reading, not a proof.

**Where the reader lives.** The reader stands at home, the centre of the circle its own choice creates. It is not the
circle. Two circles meet at home and should not be confused: this one, the reader's unit circle, is centred there, the
bar's own; the circle on the chord of §4 passes through home. Read from home they give the same directions, and they are
the two circles that read evenly along their own outline (§7.4). Held whole from no standpoint, as the completed
view holds it (§3.2), either circle has no home and no horizon; read from home it is the fisheye of §7.

## 6. Two address spaces

Inside the corner the reader holds its unit and can lay its readings out in proportion: the near field at true scale.
Past the corner the flip makes the reading h/v ∈ [0, 1], but it does not say how that reading should be laid out. Let a
lay place a far reading x = v/h ≥ 1 at position r(x), counting addresses from home, with r increasing and r(1) = 1.

Choosing a different H multiplies every far reading, taken as an amount, by one common factor. A lay whose room depended
on where a reading sits, and not only on ratios, would then depend on the arbitrary choice of H. Premise (P2) points the
same way: no measure is carried past the corner, so nothing supplies a scale for the room to depend on. We therefore
require that no scale be preferred:

> **(S)** r(λx) − r(x) depends on λ alone, for all x, λ ≥ 1.

**Proposition 4.** If r is increasing and satisfies (S), then r(x) = 1 + k·ln x for some k > 0: every doubling receives
the same number of addresses, k·ln 2. If the far lay also joins the near lay r(x) = x without a kink at the corner, then
k = 1.

*Proof.* Let g(λ) = r(λ) − 1. Comparing (S) at x = μ with (S) at x = 1 gives r(λμ) − r(μ) = g(λ), so
g(λμ) = g(λ) + g(μ) for all λ, μ ≥ 1. This is Cauchy's functional equation in multiplicative form, and its only
increasing solutions are g(λ) = k·ln λ. At x = 1 the near lay has slope 1 and the far lay slope k. ∎

Room here is the number of addresses a doubling receives, not its length.

The premise (S) does the work. Monotonicity, a fixed corner and a matched slope are not enough by themselves:
r(x) = 1 + ln x + α(ln x)² with α > 0 satisfies all three and gives successive doublings different room.

**Why (S) is the rule for a reader with no preferred scale.** Suppose a lay breaks (S): for some factor λ, the stretch
from x to λx gets more room than the stretch from y to λy. Choosing the reader's unit differently would turn the
readings x into y, since a change of H multiplies every far reading by one factor. The two stretches therefore differ
only by a choice that, by Proposition 3(b), nothing in the readings can make: a reader with unit λH in a world scaled
by λ receives exactly the same readings. A lay that breaks (S) builds into the addresses a scale the reader cannot
have. Each natural alternative breaks it in just this way:
- *proportion past the corner*, r(x) = x, gives the stretch from x to λx room (λ − 1)·x, which grows with x;
- *a power*, r(x) = x^α, gives it room (λ^α − 1)·x^α, which also depends on x;
- *a logarithm with a correction*, as above, gives room that depends on ln x.

The logarithm alone gives room that depends on λ and not on x, and Proposition 4 shows it is the only increasing lay
that does. (S) does not follow from "any H will do", which only places the corner. It is scale invariance of the lay's
increments, motivated by Proposition 3(b) and assumed, not derived (§11.2, question 1). Note also that the argument for (S) passes
through amounts, by way of V = H, and that the smooth join (k = 1) is a further condition rather than a consequence of
the flip.

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
area ln 2 (Saint-Vincent 1647). The rescaling (x, y) ↦ (x/√c, √c·y) slides along the hyperbola and keeps areas, so no
rung is preferred. The two are one sweep, squeezed: read against ln(v/h), the turn is
arctan(v/h) = π/4 + ½·gd(ln(v/h)), where gd(x) = arctan(sinh x) is the Gudermannian. It carries the whole unbounded
logarithm into a quarter turn, nearly even at the corner and squeezed without end toward the edges, so that the turn
per doubling past the corner falls 18.4°, 12.5°, 6.9°, 3.6°, 1.8°, …, by a ratio tending to 2. The bounded sweep is the
logarithm seen whole from one side.

**Two address spaces.** Inside the corner the addresses are proportional; past it they are logarithmic, each doubling
receiving the same number. The corner is where one gives way to the other, without a kink. There is only one such
corner intrinsic to the relation, the one fixed point of the flip; a particular reader's layout may have other
thresholds of its own. Past it the levels are plain doublings laid side by side, with no corners of their own and nothing nested inside
them. They are doublings of scale, v/h ↦ 2·v/h. (Doubling the angle of the sweep instead sends v/h to
2(v/h)/(1 − (v/h)²); the two agree near home and part at the corner, which the angle doubling sends to the horizon.)

**Reality in 2H.** Measured by length rather than by count, the far field fits in one more H. The *in-place lay* puts a
far reading at length 2 − h/v from home. Level k past the corner, where v/h runs from 2^(k−1) to 2^k, then has length
2^(−k), so the whole far field, out to the horizon, lies between radius 1 and radius 2. The room per unit of v/h is
(h/v)², the Jacobian of the flip. The in-place lay holds the same addresses as the logarithmic lay, the same number per
doubling, crowded toward radius 2; a reader with finitely many addresses runs out of them at a far horizon of its own.

| drawing of the same addresses | measured by | bounded | corner at |
|---|---|---|---|
| fisheye (§7) | steps of turn | yes, a quarter turn | half the turn |
| in-place lay | length | yes, radius 2 | radius 1 of 2 |
| logarithmic lay | number of addresses | no | 1, where the even doublings start |

**Why not proportion all the way out.** A reader that kept v/h itself, in proportion, past the corner would suffer in
five ways. It could not lay its range, since its readings would run to infinity and no range fixed in advance would hold
them. It would divide by the smaller part: past the corner h is the smaller unit relation, and a small wobble in it swings the
reading without bound. Inverting divides by the larger part instead, the rule numerical computing also follows when it
pivots. Its averages would never settle, being dominated by the long tail of its nearest things (§7.6). It would have
to crop: a picture kept in proportion out to the horizon would be infinitely large, and rectilinear cameras, which are
such readers, crop at about the corner, while a fisheye lens holds the whole hemisphere by giving up proportion near
its edge. And its expansions about home would fail past the corner (§4).

**Three horizons.** A horizon is a boundary between a front side and a back side, and a situated reader meets three.
The *near horizon* is the corner, v = h, between the two sides of its reading; every reader finds it. The *far horizon*
is where the reader's count of addresses runs out, well short of h = 0; a reader can reach it, as a floating-point
number overflows when its exponent runs out. The *mathematical horizon* is the reading's own infinity, h = 0 and v/h
without end, at the reader's sides: the boundary between the side it faces and the side behind it, which no reader
reaches. It is not the vanishing point. A thing infinitely far ahead reads 0, at home; the reading's infinity lies at
the sides, in what is nearest.

**Why halving.** If a level has nothing but its two ends, their order and the flip (P2), the only subdivision its
symmetries preserve is the cut at the corner into two halves: any other interior point can be moved anywhere within its
half by an order-preserving map that commutes with the flip. Applied again to each half, this gives repeated halvings.
Three parts, or any other number, need an added measure. This is Klein's criterion, that a geometry supplies what its
symmetries keep, applied to the points of a level. Halving is a branching into two; it is not by itself a ratio of 2
between level edges, since where the edges fall depends on how the readings are laid out. On the lays of this section
they fall at the doublings of v/h.

*What another ratio costs.* A reader whose own step multiplies by r matches levels that are powers of r exactly, one
level per step: a reader with r = 3 matches levels of three as one with r = 2 matches doublings. Any ratio can be
matched, then, but by the argument above every ratio other than the halving costs a measure added to the level, carried
in the reader's step. A layout whose levels are uneven, as a calendar's are (100 years, 12 months, about 30 days, 24
hours, 60 minutes, 60 seconds), matches no single step and costs a table of its levels, which a reader given nothing
does not have. Uniformity can be free; variation has to be represented somewhere, in the reader's step or in
information handed to it.

**A familiar instance.** Floating-point numbers lay their addresses this way. The exponent counts levels and the
significand is a plain share within the level; below the smallest normal number, the subnormals lay one stretch in
proportion from zero. The count of levels plus the share within the current one is the logarithm laid straight between
level edges, exact at every edge and never more than 0.086 of a level from the smooth logarithm. A float differs in
having levels on both sides of 1 and a floor; the situated reader has proportion inside the corner and no floor.

**An older instance: Mercator's map.** On a globe at latitude φ let v = sin φ, the height above the equator, and
h = cos φ, the radius of the circle of latitude, so that v/h = tan φ and the globe's meridian is the quarter circle.
Mercator's map (Mercator 1569) stretches each circle of latitude by 1/h so that all are drawn the same width, and stretches the
vertical equally to keep shapes; the equal stretch, V = H at every place, is what keeps them (Proposition 5(g)). Summed from the equator, the height on the map is y = asinh(v/h), the textbook
ln tan(π/4 + φ/2) written as one relation. Near the equator y ≈ v/h, in proportion; past 45°, the corner, y approaches
ln(2·v/h), and each doubling of v/h adds a height approaching ln 2 (0.562, 0.651, 0.682, 0.690, 0.692 for the doublings
from 1 to 32). The pole is the horizon, h = 0, which is why the map is cut off short of it. The central cylindrical
projection, whose height is v/h itself, is the plain division, proportional throughout and unbounded; Mercator's map
keeps the division's local scale 1/h but accumulates it, and so lays the same relation in proportion before the corner
and logarithmically past it. Latitude is the Gudermannian of the map's height, φ = gd(y). It is the oldest instance we
know of the two address spaces laid out.

**The proportion is in the addresses.** Within a doubling past the corner the lay's addresses are even; how evenly
things arrive at them is up to the world. If what arrives is spread evenly in direction, as a lighthouse's flashes are
(§7.1, §7.8), the far share h/v has density proportional to 1/(1 + (h/v)²), so the arrivals thin toward the corner by 1.6 to 1
across the first doubling past it, 1.18 across the second and 1.05 across the third. That unevenness belongs to the
payload, not to the addresses. The two measures are different things on the same reading: the lay places far readings,
taken as amounts at V = H, past the reader's own breadth, and an even turn is how a sweep steps through attitudes. When
the even turn is the reader's own sweeping, its law is the law of the reader's sweep, the addresses of §7; when it is
the sources' spread, it is the world's.

## 7. The Cauchy distribution is the address, not the payload

### 7.1 Sweeping the circle evenly
With V = H the relation is a bar of length 1. A reader at home sweeps it from flat (all h) to upright (all v) in equal
steps of turn, and at each step holds one reading, v/h. On the proposal of §3.1, one direction at a time describes this
look, not the system being read (§3.5).

**Proposition 5.** (a) Equal steps of turn give unequal readings. Near home a step barely changes v/h; the corner is
halfway through the turn; near upright each step changes v/h by more and more, without bound.

(b) Counted per unit of v/h, the steps have density 2/(π(1 + (v/h)²)) on [0, ∞): the half-Cauchy distribution. Its
median is the corner, and the flip leaves it unchanged. Over both facings, with v/h signed, it is the standard Cauchy
1/(π(1 + (v/h)²)), with its median at home and its quartiles at the corners ±1.

(c) Placing each reading at its step of turn, rather than at its value, gives the *fisheye*: true scale near home,
compressed gently toward the corner and increasingly past it, with the horizon at the edge of the turn, never reached.

(d) *Conversely, the Cauchy requires V = H.* Let the reader draw all of v at c times the length of all of h, V = cH, and
sweep in equal steps of direction from home. Its readings v/h follow the law of (b), with its median at the corner and
unchanged by the flip, if and only if c = 1.

*Proof.* When the bar turns by a small angle, v/h changes by that angle times 1/h², and on the circle
1/h² = (h² + v²)/h² = 1 + (v/h)². So the steps per unit of v/h go as 1/(1 + (v/h)²), and normalising over a quarter
turn gives the factor 2/π. Half the turn lies on each side of 45°, and the substitution v/h ↦ h/v carries the density to
itself. (d) A direction φ from home in the drawing has tan φ = c·(v/h). With φ even on [0, π/2],
P(v/h ≤ r) = P(φ ≤ arctan(cr)) = (2/π)·arctan(cr): a half-Cauchy of scale 1/c, with median 1/c. The flip v/h ↦ h/v
carries it to scale c. It is the law of (b), and unchanged by the flip, exactly when c = 1. ∎

**The density in full.** Written out in full, (b) carries one more parameter, ρ in [0, 1]: the share of the sweep's
addresses at which a payload is met. The arrivals per unit of v/h are ρ·2/(π(1 + (v/h)²)), and per unit of turn ρ·2/π,
so the density times the extent of the quarter turn is ρ·(2/π)·(π/2) = ρ, the share that arrived. With every address
met, ρ = 1, the default, and the parameter is simplified away: that is the form of (b) and of the rest of the paper. The
simplification loses nothing the addresses hold. ρ counts payload, not addresses: dividing the arrivals by their total
ρ returns the law of (b), so a constant ρ leaves the median at the corner, the quartiles and the flip where they were
(Theorem 6(a)).

**When the density varies with direction.** Where ρ depends on the direction θ = arctan(v/h), it is no longer a
constant to drop: it carries the payload's shape (§7.4), and the arrivals per unit of v/h are

  ρ(θ)·2/(π(1 + (v/h)²)),  in total ρ̄ = (2/π)∫₀^{π/2} ρ(θ) dθ,

which, divided by ρ̄, is no longer a Cauchy. The addresses are the same at every ρ; only what they find differs. This is
the join of §4 ("The address points at the payload") read as a law: the inscribed sweep lays the Cauchy, the central
sweep finds ρ(θ) at each address, and the arrivals are their product. The total ρ̄, the payload's average over the
facing, is what the central sweep reads by its mean (§3.1). Since the addresses are even in θ, the arrivals' median is
the direction θ_m at which ∫₀^{θ_m} ρ dθ is half of ∫₀^{π/2} ρ dθ: the median direction of the payload. It stays at the
corner when the payload weighs as much on one side of it as on the other, and in particular when ρ(θ) = ρ(π/2 − θ),
unchanged by the flip; otherwise it moves toward the heavier side. With ρ = (2 + cos 2θ)/3, heavier toward home, the
arrivals' median falls at θ = 32.1°, v/h = 0.627, and 0.659 of them lie below the corner; with ρ = (2 + cos 4θ)/3,
unchanged by the flip, it stays at 45°. The distance of the arrivals' median from the corner measures the payload's
lopsidedness, in the payload's own terms, against addresses that did not move.

**Why the payload is Gaussian.** Let the payload at the reader have two components, X on h's side and Y on v's, as
amounts; its reading is their ratio, s = |Y|/|X|, which keeps the direction and drops the size. Two premises are needed,
and the paper's own do not supply them. The first is that the payload's law is unchanged by every turn. That the reader
cannot detect its own turns (Proposition 3(e)) is a fact about what the reader knows, not about the payload; it makes
the turn-invariant law the representation an ignorant reader should choose, in Jaynes's sense (§2), and that is all it
does. The second is that the two components vary independently. Given both, the payload's law is the isotropic normal,
the only law of two independent components that every turn leaves unchanged (Herschel 1850; Maxwell 1860). Three things
follow, each classical.
- Its direction is even over the turn, so its reading is the half-Cauchy of (b), P(s ≤ r) = (2/π)·arctan r, with its
  median at the corner. The normal payload's ratio has the addresses' law.
- Its size, √(X² + Y²), is independent of its direction. What arrives and where it is addressed separate exactly:
  Theorem 6(a), seen from the payload's side.
- With unequal spreads, σ_v ≠ σ_h, the reading is still a half-Cauchy, of scale σ_v/σ_h, its median there: (d) with
  c = σ_v/σ_h. Equal spreads are the drawing V = H. With the payload's centre off the origin the reading is no longer a
  Cauchy at all, and its median leaves the corner (with the centre at (0, σ), to 1.515): the density varying with
  direction, above.

The central sweep reads the payload, which has a mean (each component's size averages √(2/π)·σ); its ratio, which has the
addresses' law, has none (its mean up to M is (1/π)·ln(1 + M²), growing without limit). The two routes to the
Cauchy are kept apart. The address law of (b) is the sweep's own: it needs only the even turn and holds whatever the
payload is, Gaussian or not (Theorem 6(a)). The normal payload is a second route that arrives at the same law, a model
consistent with the addresses, not their cause. The paper does not claim that payloads are Gaussian, only that if a
payload's law is taken to be unchanged by turns, with independent components, it is the normal, and its ratio is then
the Cauchy the addresses already were. The central limit theorem is a third matter: it makes a sum of many independent
contributions normal, and says nothing about a single payload averaged over the facing.

**Proposition 5, continued: two other parties.** (e) Let the reader assign two other parties V = V₂ = H, so that the
relation lies on the sphere of Proposition 3(f), and sweep one facing of every freedom, the octant h, v, v₂ ≥ 0, evenly
by area. Write a = v/h and b = v₂/h. Then:
- the readings (a, b) have density 2/(π(1 + a² + b²)^(3/2)) on [0, ∞)², the two-dimensional half-Cauchy;
- each of v/h, v₂/h and v/v₂ alone has the law of (b), with its median at its own corner and no mean;
- the six orderings of h, v and v₂ are equally likely, so the reader is near in both readings (h the largest) for a
  third of the octant, past in one for a third and past in both for a third;
- drawn at V = c₁H and V₂ = c₂H and swept evenly by direction in the drawing, the medians of v/h, v₂/h and v/v₂ are 1/c₁,
  1/c₂ and c₂/c₁. Every pair keeps its corner only if c₁ = c₂ = 1, and a pair keeps its own only if its two parties are
  drawn at one length.

*Proof.* The point of the octant in direction (1, a, b) is (1, a, b)/r with r² = 1 + a² + b². Projected from the centre
onto the plane h = 1, an element da·db of the plane at distance r from the centre subtends dA = da·db·cos α/r² of the
sphere, where α is the angle between the ray and the plane's normal, cos α = 1/r; so dA = da·db/r³. In polar
coordinates on that plane, a = q cos ψ and b = q sin ψ, ∫₀^∞ q·dq/(1 + q²)^(3/2) = 1, so the octant's area is π/2 and ψ
is spread evenly over [0, π/2]; hence b/a = tan ψ, which is v₂/v, has the law of (b). Integrating b out, ∫₀^∞ db/(1 + a² + b²)^(3/2) = 1/(1 + a²), which gives the law of (b) for
a, and likewise for b. Exchanging any two of h, v and v₂ is a symmetry of the sphere that keeps the octant, so the six
orderings have equal areas; h is the largest in two of them. In the drawing an even direction is (1, c₁a, c₂b)
normalised, so (c₁a, c₂b) has the law above and each median is divided by its c. ∎

The wedge is made at each observation, not taken from a sphere the reader holds: the whole sphere, every facing drawn
together, is the completed view. A sphere that placed every place by its direction and its distance would need every
distance, which no situated reader has. The wedge needs no size: the readings are ratios, laid by the two-dimensional
Cauchy. What it lacks is what the circle lacks, once per party: V*/H and V₂*/H. On the circle near and far were halves;
with three parties the reader is near in both readings for a third of its addresses.

**Swept by altitude and azimuth.** Reached by the two sweeps of §2, the even octant is even in azimuth and even in
height v, not in altitude. By Archimedes' hat-box theorem (*On the Sphere and Cylinder*), a zone of a sphere has area
in proportion to its height, so the octant's area between azimuths z₁, z₂ and heights v₁, v₂ is (z₂ − z₁)(v₂ − v₁):
Lambert's equal-area map (Lambert 1772), with the altitude's density cos a. Swept that way, every pair keeps its corner
and the near field is a third, as (e) states. Swept evenly in both angles instead, each sweep keeps its own corner (an
even azimuth keeps v₂ = h at the median however the altitude is weighted), but the pair that neither sweep reads leaves
its corner: v ≤ h for 0.343 of the readings, and the near field shrinks to 0.233, because the rings of azimuth narrow
toward the vertical. The raise even in height belongs to three unit relations only: with two, the even sweep is the
turn itself; with four, the height's density on the even orthant is (4/π)√(1 − t²).

**More parties.** The same holds for any number n of other parties, each drawn at H. The relation lies on the sphere
of n + 1 unit relations, one facing of every freedom is its positive orthant, and the point in direction (1, a) is
(1, a)/r with r² = 1 + |a|², a = (v₁/h, …, v_n/h). The projection argument of the proof gives the element of area
da/r^(n+1), so the even orthant's readings have density c_n·(1 + |a|²)^(−(n+1)/2), the n-dimensional half-Cauchy, with
c_n = 2ⁿ·Γ((n + 1)/2)/π^((n+1)/2). Integrating out all readings but one leaves the law of (b); all but two, the law of
(e). So every reading and every pair keeps its corner, and adding a party changes nothing about the pairs already held.
Exchanging any two of the n + 1 unit relations keeps the orthant, so every ordering of them is equally likely and h's
rank among them is spread evenly. The reader is near in all its readings (h the largest) for 1/(n + 1) of its
addresses, a half, a third, a quarter, and so on, and the number of readings past their corner is spread evenly over
0, 1, …, n. Drawn at unequal lengths, these shares move, as in (e).
None of this involves any party's true breadth. The drawing is the geometry's whole work; each true breadth is one
number of the amounts, a shift in levels of that party's amounts alone.

In classical terms the readings are the tangent of a uniformly distributed angle: the gnomonic projection of a uniform
direction. For two other parties the gnomonic projection of a uniform direction on the sphere is the multivariate
Cauchy (the multivariate t with one degree of freedom), whose marginals are Cauchy (Cacoullos 2014).

**Working back from the Cauchy.** The Cauchy is known: it is the tangent of an angle turned evenly. Read backward, from
the known law to what it needs, each step is forced by the one before.
1. The readings follow the law of (b): distribution function (2/π)·arctan(v/h), median at the corner.
2. Then the angle θ = arctan(v/h) is turned evenly, since P(θ ≤ t) = P(v/h ≤ tan t) = 2t/π.
3. That angle is the direction the reader turns through only if both breadths are drawn at one length, V = H, by (d);
   drawn at V = cH, an even turn of direction puts the median log₂ c levels off the corner. No other even rescues it.
   Even steps along the stretched curve give no Cauchy at all: for c = 2 the quartiles of v/h are 0.316, 0.739 and
   1.673, not a flip pair. Even steps of the ellipse's parameter do give the law of (b), but that parameter is the turn
   of the circle drawn with V = H, stretched afterwards.
4. With V = H the sweep is one rigid bar turning, and it traces the unit circle (Proposition 3(c), (e)).

So V = H is not a convenience laid over the Cauchy. It is what the Cauchy requires, and, forward through Proposition 3
and parts (a) to (c), it is also enough. Every link of the chain, from the reader's one breadth to the Cauchy and back,
passes through V = H.

**Proposition 5, continued: two familiar pictures.** The best-known pictures of a turn laid out on a straight line
are a lighthouse's flashes on a shore and Mercator's chart of the globe. Each requires V = H, and each separates it
from the size, which stays free.

(f) *The lighthouse.* A lamp stands at distance β from a straight shore, opposite the shore's point α. It sends flashes
at angles θ from the perpendicular, spread evenly over the half turn toward the shore.
- A flash at θ lands at x = α + β·tan θ. Its offset from the foot over the lamp's distance is the reading:
  (x − α)/β = tan θ.
  - **Home** is the foot.
  - **The corners** are the flashes at ±45°, which land at α ± β.
  - **The horizons** are the shore's two ends.

  The landings follow the law of (b) over both facings, and half of them lie within β of the foot.
- The flash's path, β/cos θ, differs from flash to flash and cancels from the ratio of its two legs: β out to sea and
  x − α along the shore. One length remains, β. It is the same for every flash because the shore is straight.
- Draw the shore at c times the length of the sea: V = cH, with H drawn at the lamp's distance.
  - The half-way flash then lands c drawn lamp-distances from the foot and is drawn at arctan c.
  - The share of landings within one drawn lamp-distance is (2/π)·arctan(1/c).
  - The drawn readings follow the law of (b), with the median at the corner and unchanged by the flip, if and only
    if c = 1.
- Drawn at V = H, but with any H in place of β, each landing is laid H·tan θ from the foot. Every angle is kept and the
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

*Proof.* (f) The flash at θ meets the shore where its leg out to sea, of length β, and its leg along the shore, x − α,
stand at angle θ. So (x − α)/β = tan θ, and the path, β/cos θ, divides out of the ratio. With θ even on
(−π/2, π/2), the law of (b) over both facings follows as in the proof of (b), and P(|x − α| ≤ β) = P(|θ| ≤ π/4) = ½.
Drawn with the shore at c times, the drawn reading is c·tan θ, so P(|c·tan θ| ≤ r) = (2/π)·arctan(r/c). That is a
Cauchy of scale c, with median c. The flip carries it to scale 1/c, so it is the law of (b), and unchanged by the flip,
exactly when c = 1, as in (d). (In (d) the evenness is in the drawing's directions, so the median there is 1/c; here
it is in the lamp's turn, so it is c. Either way only c = 1 keeps the corner.) The flash at 45° is drawn at c·β from
the foot, at angle arctan c. Laying each landing H·tan θ from the foot multiplies every length of the true figure by
H/β, which is a similarity.

(g) A step dφ north has length dφ on the globe and f′(φ)·dφ on the chart. A step dλ east has length cos φ·dλ on the
globe and dλ on the chart. So the chart's scales are f′(φ) north and sec φ east, and their ratio is c. A course at
bearing ψ moves east and north in the ratio tan ψ, so cos φ·dλ = tan ψ·dφ, and on the chart
dx/dy = dλ/(f′(φ)·dφ) = tan ψ/c. That is tan ψ for every ψ only if c = 1. Where c = 1 at every latitude, dx/dy is
constant along the course, so the course is drawn straight. Integrating f′ = sec φ from the equator gives
ln tan(π/4 + φ/2) = asinh(tan φ).

A circle of small radius ε, its points ε·(cos t, sin t) north and east, is drawn as ε·(f′(φ) cos t, sec φ sin t): an
ellipse with axes in the ratio c. With f′ = sec φ both scales are sec φ, and areas are multiplied by sec²φ. Keeping
areas means f′(φ)·sec φ = 1, so f′ = cos φ and c = cos²φ. On any chart, keeping angles makes the two scales equal at
each place, and keeping areas makes their product 1. Both together make every scale 1, a drawing of the sphere on the
plane without stretch, which its curvature forbids (Gauss's theorema egregium). ∎

**What the two pictures show.** Each lays an even turn on a straight line: the lamp's flashes on the shore, and a
navigator's bearings on the chart. Each keeps the turn true only when its two directions are drawn at one length.
- **The lighthouse** shows it on one picture. Drawn with the shore stretched, the half-way flash leaves 45°, half the
  landings no longer fall within one drawn lamp-distance of the foot, and the near half no longer mirrors the far half.
- **Mercator's map** shows it at every place. It is the one chart of its kind on which the corner between north and
  east is drawn at 45° everywhere.

What each leaves free is the size: the lamp's distance, which the picture can be drawn at any value of, and the local
scale sec φ, which Mercator lets grow toward the poles. Both are zooms, which change every length and no angle. That
is the distinction this paper draws throughout: the drawing V = H is required, and the true size is one number the
readings do not fix.

Mercator's choice (keep the angles, give up the areas) is the one this paper's reader makes: it keeps the drawing and
leaves the size to be estimated. The familiar complaint about his map, that it draws Greenland as large as Africa, is a
complaint about the zoom, not about the drawing.

The two pictures meet on a chart. A lighthouse charted on Mercator's map is drawn true at every latitude. On a plate
carrée chart at 60°, with the shore running east–west, its half-way flash is drawn at 63.4°.

In the lighthouse the evenness is the lamp's, a fact about the world (§7.8). A reader standing at the lamp and reading
each landing by its direction holds tan θ itself, with no β at all. The same requirement holds for it, by (d).

**The addresses' bell.** The inscribed sweep's addresses, taken together, each with its share of the turn, form a bell;
the central sweep's payloads are a different thing, read by their mean (§3.1). On the logarithmic axis x = ln(v/h) the
shares form a bell centred on the corner,

  ½·sech x = 1/(v/h + h/v),  with total area π/2, a quarter turn.

On the plain axis the same shares are 1/(1 + (v/h)²), Cauchy's curve. The bell and the fisheye are one function: the
area under the bell up to x is arctan(v/h) = π/4 + ½·gd(x), the fisheye's radius there, because the Gudermannian is the
running area under sech. Taken direction by direction the addresses give the running total, which is the fisheye; taken
together, every share, which is the bell. It is not the normal curve, which belongs to the payload's mean. With the same
peak and area the two look alike near the corner, but one level out from it the bell stands at 0.400, then 0.235, 0.123,
0.062, halving with every further level and keeping a share in every level without end, while the normal curve falls
ever faster and its far levels vanish (0.043 at the fourth level against the bell's 0.062, and 0.002 against 0.016 at
the sixth). The bell has a horizon; the normal curve has none.

### 7.2 The main result

> **The Cauchy is not the payload; it is the address to the payload.**

Call a statistic of a set of readings an *address statistic* if it depends only on their order (the ranks, the median,
the quartiles, which side of the corner each lies on), and a *payload statistic* if it depends on their sizes (the mean,
any sum).

**Theorem 6.** Parts (a) and (d) concern the readings of Proposition 5: the other party drawn at V = H and the circle
swept evenly by direction. Parts (b) and (c) hold for any finite set of readings. Part (e) drops both the circle and
the even turn.

(a) *Nothing that arrives changes the Cauchy.* Suppose that whatever arrives in the direction of each step lies at some
reach ℓ > 0, an amount that may differ from direction to direction and is unknown to the reader. In the reader's unit
its components are ℓ·h and ℓ·v, and the reading is (ℓ·v)/(ℓ·h) = v/h. The readings of Proposition 5, their Cauchy count
and the fisheye are therefore the same whatever arrives, and are fixed before anything does.

(b) *Address statistics ignore the payload.* For a finite set X of readings and any strictly increasing map f, the set
f(X) has the same ranks as X, so every address statistic picks out the same element; for an odd count,
median f(X) = f(median X). Conversely, two sets with the same ranks are carried onto one another by some strictly
increasing f, so the ranks keep exactly what survives every such change, and nothing more.

(c) *Payload statistics do not.* Among the strictly increasing maps of (b), only an affine f commutes with the mean on
every set of readings: for any such f that is not affine there is a set X with mean f(X) ≠ f(mean X). For convex f, mean
f(X) ≥ f(mean X) on every X, with equality only if f is affine on the smallest interval containing X.

(d) *The Cauchy is an address law.* Over one facing its median is v/h = 1, the corner, and its quartiles are √2 − 1 and
√2 + 1, a flip pair. Its mean does not exist: ∫₀^M x·2/(π(1 + x²)) dx = (1/π)·ln(1 + M²), which grows without bound.

(e) *The median needs only fairness, and the missing mean a weight that reaches the horizon.* Let the sweep follow any path from all of h to all of v, with
any weight, both unchanged by exchanging the two parties. Then the readings' law is unchanged by the flip and its
median is the corner. If moreover the weight gives h a density bounded away from 0 near the horizon, the mean does not
exist. The even turn on the circle is the case that gives the Cauchy of (d).

*Proof.* (a) is the cancellation shown. (b) Strictly increasing maps preserve ranks; the converse follows by monotone
interpolation between matched points. (c) A strictly increasing f that satisfies f((a + b)/2) = (f(a) + f(b))/2 for all a, b is affine,
so a non-affine f fails it for some pair, and X = {a, b} is the set required. Monotonicity, or some other regularity
such as measurability, is needed: an additive function built on a Hamel basis, plus a constant, satisfies the midpoint
equation and commutes with the mean of every finite set without being affine. The inequality and its equality case are
Jensen's. (d) Over one facing the distribution function is
(2/π)·arctan(v/h), which is ½ at v/h = 1 and ¼ and ¾ at tan(π/8) = √2 − 1 and tan(3π/8) = √2 + 1; the integral is
elementary. (e) The exchange carries v/h to h/v and leaves path and weight unchanged, so v/h and 1/(v/h) have one law,
F(1/x) = 1 − F(x), and by Proposition 2(b) F(1) = ½. Near the horizon v stays above some v₀ > 0, so
P(v/h > r) ≥ P(h < v₀/r) ≥ q₀·v₀/r for large r, where q₀ > 0 bounds the density of h there from below; then ∫ P(v/h > r) dr diverges, and
so does the mean. ∎

The theorem is elementary; its content is the reading. The Cauchy distribution is not a law of anything the reader
meets. It is the reader's own layout of directions, counted. What arrives in each direction cancels from every single
reading, not merely on average, so the readings tell rays apart, not points. The Cauchy is where the reader can put what
arrives, never what arrives.

**What the result establishes, and what it does not.** The argument has three steps.
1. The sweep is defined without any reference to what arrives: equal steps of turn, from home.
2. Changing what arrives, while keeping the sweep, leaves the readings and their distribution exactly as they were
   (Theorem 6(a)).
3. So the Cauchy is a property of the sweep, the reader's addressing, and finding it is no evidence by itself that
   anything in the world is distributed that way.

Two things are not claimed. The theorem does not show that every real observer samples in equal turns; it shows what a
reader that does so receives, and why equal turns is the sampling that prefers no attitude (§2, §7.5). Nor does it show that
every Cauchy distribution met in data has this origin; a Cauchy met as data may have others, and the next paragraph
says what sets its scale when it is formed from a reading.

Third, where the evenness comes from is a choice. If it comes from the world, as when sources are spread evenly in
direction, the same Cauchy is a property of the world's directions, and "addresses" would be the wrong name for it.
The address reading holds where the even sweep is the reader's own laying, as step 1 defines it. What does not depend
on that choice:
- the reach cancels from every single reading, not on average (Theorem 6(a));
- order survives every change of payload (Theorem 6(b));
- only an affine map commutes with the mean on every set (Theorem 6(c));
- the median at the corner and the missing mean, for any weight that treats the two parties alike and does not vanish
  at the horizon (Theorem 6(e)). Only the Cauchy's exact shape needs the even turn.

These give a reader a reason to prefer order whatever the evenness is: order is what survives a payload it does not
know.

**Where the usual confusion comes from.** Laid evenly by direction, the sweep is uniform and bounded, g from 0 to 1,
with its middle at the corner: geometry, with nothing wild in it. Read on the axis v/h, the same lay is a Cauchy of
scale 1. That needs no knowledge of the true V*, since h and v each run from 0 to 1; it needs only the drawing V = H,
which the Cauchy requires (Proposition 5(d)). Read in amounts against the true breadth it is another Cauchy, of
(v·V*)/(h·H) = (v/h)·(V*/H), with scale V*/H. Writing that one as the standard Cauchy, of scale 1, silently takes the
mountain's true breadth to be the drawn one: it turns a situated reader into situation 1, the circle, without knowing
V*. A situated reader must draw V = H (§5); the confusion is taking the drawing for a measurement. Taking the mean of
the readings then applies an operation on amounts to addresses, and the missing mean is what that costs: it comes from
the unbounded axis of the reading, not from the world. Where a Cauchy is met as data rather than laid as addresses, an
amount has been formed from the reading by a known length, and the distribution's scale is that length, not 1 by
assumption.

### 7.3 In the picture of the hand

Spread the fingers evenly by turn and read each one as v over h: the readings are the Cauchy, and nothing of the rings
is in them.
- *The median is a finger.* Of five fingers spread evenly from flat to upright, the middle one, at 45°, is the corner.
  Order, ranks, quartiles and the corner are address statistics, and they ignore the rings.
- *The corners are the quartiles.* With the fingers spread over both facings, the corners at ±45° are the quartiles of
  the standard Cauchy. So anything whose two ends sit at the reader's corners takes exactly the middle half of its
  fingers, whatever its size and however far away: the mountain range of §10 is one.
- *The missing mean asks the fingers about the rings.* A mean is a sum of sizes, a question about the payload. The
  readings carry no size, so the question has no answer. The median, a question about addresses, always has one.
- *More fingers, not bigger rings.* Sweeping more finely lays more addresses. It buys precision about where, never
  about what. What is at the addresses comes only from payload held beside them.
- *The rings hide; the hand does not.* Two rings on one finger, seen along it, show only the nearer. Every back side is
  made by the payload; the addresses hide nothing.
- *Three breadths.* In space the fingers spread through a solid wedge and, spread evenly, give the two-variable Cauchy, with
  density proportional to (1 + |x|²)^(−3/2). Each pair of readings keeps its median at its own corner (Proposition
  5(e)), but the radius |x| does not: only 1 − 1/√2 ≈ 0.29 of the addresses have |x| ≤ 1, and the median of |x| is
  √3. That median is still an address, though not a corner.

### 7.4 The shape is payload

The sweep opens a closed shape out, with home in the middle of the opening and the two ends running toward the horizon
in each facing. Opening divides out size, so each place on the opened line is an address pointing back to a point of the
closed shape, which keeps its size. Laid evenly by direction, every shape opens into the same fisheye and the same
Cauchy; the shape survives only in what arrives at each address, one breadth per direction, as Theorem 6(a)
requires. The addresses are the same for every shape laid evenly by direction, and the shape is payload.

**The lay, not the shape.** Laying the same shapes another way shows where the Cauchy comes from. Read each shape from
its centre as v/h, and describe its opening by four numbers: the share of readings before the corner, their median, how
they cross home (the share below e, divided by e, at e = 0.025) and how they cross toward the horizon (s times the share
above s, at s = 40). Laid by direction, every shape gives the circle's four numbers, since the reading is the direction
alone. Laid in equal steps along its own outline instead, a lay taken from the shape itself, each shape opens its own
way:

| shape | laid | before the corner | median | crossing home | crossing toward the horizon |
|---|---|---|---|---|---|
| any shape | by direction | 0.500 | 1.000 | 0.637 | 0.637 |
| circle | along its outline | 0.500 | 1.000 | 0.637 | 0.637 |
| square | along its outline | 0.500 | 1.000 | 0.500 | 0.500 |
| diamond, h + v = 1 | along its outline | 0.500 | 1.000 | 0.976 | 0.976 |
| astroid | along its outline | 0.500 | 1.000 | 3.15 | 3.15 |
| ellipse, twice as tall as wide | along its outline | 0.373 | 1.479 | 0.413 | 0.826 |

Shapes unchanged when h and v are exchanged keep the corner at the middle, as the flip requires, and none of them has a
mean, since each keeps a share of order 1/s or more beyond s (Theorem 6(e)). They differ only at the ends; the
astroid's cusps make its ends heavy, the square's flat sides make them light. The ellipse, which the exchange alters,
moves its corner as well. Over 73 single-outline shapes from a drawing library the pattern is the same, with ends from
0.27 for a gear to about 3.1 for the astroid. The test would have failed had any shape laid by direction departed from
the circle's numbers, or had a shape unchanged by the exchange moved its corner off the middle. The Cauchy is what an
even lay by direction gives, whatever the shape; a lay taken from the outline brings the shape into the distribution.
The Cauchy belongs to how the addresses are laid.

**Why the circle and the Cauchy go together.** The circle is the one shape whose two lays coincide: on a circle, equal
steps along the outline are equal steps of turn. So for the circle alone, a lay taken from the shape and a lay that
knows nothing of any shape are the same lay, and both give the Cauchy. Every other shape tells them apart. This is why
the Cauchy is usually met through the circle, as the tangent of an angle spread evenly round it: it belongs to the even
turn, and the circle is the one shape in which the even turn and the shape cannot be told apart.

**A shape is a perturbation of the circle, and only the circle can be the base.** Write a shape seen from the reader as
r(θ) = exp(ρ·f(θ)), the unit circle at ρ = 0 and the full shape at ρ = 1. Every such map moves each point along its own
ray and never across it, so the maps r ↦ r·e^{g(θ)} form a group that fixes every direction; laid by direction, the
readings are the same Cauchy at every ρ, not only at the two ends. Laid along the outline, the law moves with ρ: for
f = 0.3 cos 2θ + 0.1 cos(3θ + 0.4) the share before the corner runs 0.500, 0.529, 0.563, 0.632 at ρ = 0, ¼, ½, 1, and
for f = 0.25 cos 4θ, unchanged by the exchange, it stays 0.500 while the ends move. The circle is the only base that
carries nothing: an outline reads evenly by direction exactly when its length per unit of turn, √(r² + r′²), is
constant, and r² + r′² = c² has two kinds of solution, r = c, the circle centred on the one who sweeps, and
r = c·sin(θ + φ), the circle through it. These are the two pivots of §4, the centre and a point of the circle, and no
other shape gives either. Read as the reader's ignorance (§2), a reader who does not know the shape needs a law that
every radial map leaves unchanged, and only a law on directions alone is one; the rescalings of κ are the radial maps
with g constant. So a reader can begin at the unit circle and sweep the perturbation without knowing V*: in
ln r = a₀ + ρ·f(θ), the unknown size is the constant term alone, a₀ = ln κ, the one term no ratio of radii reads, and
the even measure dκ/κ is the flat da₀. Every term of f is the shape, read exactly from ratios of radii wherever the
payload or another standpoint supplies them (from directions alone none is read), and taking the terms in order of n is
a level of detail, each truncation leaving every address where it was.

The addresses with their payloads give the shape back, up to scale, exactly when the shape is star-shaped from the
standpoint, so that each direction meets the outline once. Otherwise some direction meets it more than once and the
parts behind are hidden: rings behind rings on one finger.

Two examples show the reach and the limit. An ellipse with semi-axes 2 and 1, read from its centre, meets each
direction θ once, at r(θ) = 2/√(cos²θ + 4·sin²θ). One value per address holds it completely, and doubling the ellipse
doubles every value and moves no address. A ring between radii 1 and 2, read from its centre, is not star-shaped from
there: every direction meets its inner edge and then its outer edge. One value per address keeps the inner edge, the
first thing met, and loses the outer one, which lies behind it on the same address. What the representation keeps is
the first meeting along each address; what it loses is everything behind that. Occlusion and contact need more than a value at each address
(that sight runs straight and stops at the first thing it meets), and nothing here is claimed for them.

### 7.5 Situated and unsituated

Held whole, from no standpoint, the bar's even turn traces the circle h² + v² = 1, every point like every other: no
home, no horizon and no corner of any consequence. Swept from home and read as v/h, the same even turn gives the Cauchy
when counted and the fisheye when drawn. Home, the corner and the horizon appear because the reading is taken from
somewhere. Situated geometry is the arc, read as the Cauchy; unsituated geometry is the chord, with the circle drawn
on it whole. The chord needs no turn, and the circle is what a turn traces.

Proposition 5 assumes the turn is stepped evenly, which is a choice of weight on the sweep. It is not a weight chosen to
produce the Cauchy: stepping the turn evenly is what makes the circle uniform in the first place, so one assumption,
uniformity, lies behind both. The two are still distinct: the circle's symmetry under turns is one thing, and a reader's
choice to sample in equal turns is another. Other weights fair to both facings exist, such as the line's share
v/(v + h). By Proposition 2(b) each puts the corner at its middle, but none of them gives the Cauchy.

### 7.6 What being situated costs

Two things are missing from a situated reading, and they are easily confused. The breadths are missing from every
single reading: v/h cancels them, as it cancels the reach of whatever arrives. The total of the whole is missing because
the reader's readings have no end: the horizon is never reached, so no census can be taken. The Cauchy's missing mean
belongs to the first absence, not the second. It is not a census that more readings would complete: over both facings
the mean of n Cauchy readings is distributed exactly as a single reading, whatever n is, so averaging never settles.
The readings are addresses, and a mean asks them for sizes they do not carry. A situated reader keeps order and loses
sums, and the Cauchy is the extreme case: an order law with no sum.

**Order needs holding.** The median survives every change of what arrives (Theorem 6), but a reader has it only if it
holds its readings. Finding the exact median of n arrivals taken one at a time needs storage that grows in proportion to
n (Munro and Paterson 1980).
- A reader that holds its hemisphere at once has the median of what arrived. (The median of the addresses, the
  corner, needs no holding: the inscribed sweep lays it before anything arrives, §3.1.)
- A reader that holds one arrival at a time does not. What it can keep, at the cost of one more slot, is one
  arrival, held and left alone, against which every later arrival is higher or lower.
  - That comparison is unchanged by any common rescaling.
  - It needs no step, since it asks only which of two is larger, so readers who count in different steps mark the same
    arrivals.

  It does for the one what the median does for the other. A reference that moves with the reader's
  own counts loses this: readers counting in different steps then mark different arrivals.

### 7.7 Other addresses and payloads

The same split appears in familiar places.
- *The unit circle is an addressing scheme.* A system of any size can be laid onto it, and nothing is read out of it.
  It has no size of its own and no count of things.
- *The number line is laid on the sweep.* The sweep from home to the horizon is the address space; the number line is
  what is addressed, with 0 at home, 1 at the corner and its unbounded end toward the horizon, the two sides of 1
  exchanged by the flip.
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
  fit between that pair's corner and home, and the end of the track, however far, has an address, home, that no tie
  reaches.

### 7.8 What is known

The Cauchy as the image of a uniform angle (the gnomonic projection of uniform measure on a hemisphere), its invariance
under Möbius maps and its missing mean are classical (Knight 1976; McCullagh 1996; Pitman and Williams 1967; Cuadras
2002; Stigler 1974), as are the facts that the mean of n Cauchy variates is again Cauchy and that order statistics
follow every increasing map; those facts are part (d). The other parts of Theorem 6 are in print too.
- *Part (a).* The ratio of two components of any spherically symmetric vector is Cauchy, whatever its radial law, since
  its direction is uniform and independent of its length (Jones 1999). In more dimensions the tangents of the polar
  angle are multivariate Cauchy (Cacoullos 2014), the law of Proposition 5(e). Under elliptical symmetry the ratio is a
  Cauchy of another scale (Jones 2008a), the forward half of Proposition 5(d). This is the reach cancelling.
- *Parts (b) and (c).* That the median keeps its place under every order-preserving transformation, and the mean only
  under linear ones, is Stevens's classification of scales of measurement (1946).
- *Part (e).* Positive variables with the same law as their reciprocal were characterized by Seshadri (1965) and are
  called log-symmetric (Jones 2008b); a ratio X/Y has that property exactly when X and Y are, or can be chosen to be,
  exchangeable (Cacoullos and Papadatos 2013).
- *The textbook case* is the lighthouse (Gull 1988; Sivia and Skilling 2006): flashes sent at evenly spread angles land
  along the shore as a Cauchy, and the lamp's position is found from the median or the likelihood, never the mean. There
  the evenness belongs to the lamp, a fact about the world. Our claim concerns the case where it belongs to the reader.
  That half the landings fall within the lamp's distance of its foot only when shore and sea are drawn at one length
  is Proposition 5(f), which is elementary.
- *Proposition 5(g)* is classical cartography. A chart's two scales at a place are the axes of Tissot's indicatrix
  (Tissot 1881), which is a circle exactly where the chart keeps angles; Mercator's map is the cylindrical chart that
  does so everywhere; and no chart keeps both angles and areas (Euler 1777; Gauss 1828). What is ours is the reading: the
  ratio of the two scales is the drawing V = cH, and the corner between north and east is the corner of §4.
- *The nearest prior reading* is Frank and Smith's (2010; Frank 2014): the scale on which an observer measures defines
  the most likely distribution of what it observes, and a scale linear for small magnitudes and logarithmic for large
  ones, as the reader's two address spaces are (§6), gives Student's t, of which the Cauchy is the case of one degree of
  freedom. Their route is maximum entropy under a constraint set by the scale; ours is the cancellation of the reach,
  which also separates what order keeps from what sums lose.

What is new here is the reading: which reader, knowing what, receives the Cauchy, and that what it receives is its own
addresses rather than anything in the world. We did not find that reading, or a split between addresses and payload, in
print.

## 8. Level of detail and the choice of H

**The count is the level of detail.** The forms of the two address spaces are fixed; their counts are not. Laying the
near field in proportion means dividing H into some number of parts, and the geometry neither knows nor uses that
number. Past the corner, what is fixed is that each doubling gets the same count, not what the count is. In both spaces
the count is the *level of detail*: the geometry gives the forms, and the level of detail gives the count.

**Size sets the level.** A thing that spans n of the reader's addresses is resolved to about log₂ n levels, one fewer
each time the number of addresses it spans halves; when it spans a single address it is a point. Nothing is requested:
the span sets the level. How many addresses a thing spans depends on amounts, which the geometry does not supply.

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
  (Kelvin's inversion; Kellogg 1929). It is the flip of §4, in space.

This is level of detail by distance, with the corner as its seam.

**H is a zoom, not an escape.** H is not a measured size: it is the value the reader chooses to start the system
(P1), and nothing in the geometry fixes it. Any H gives the same circle and corner, so a reader could choose a very large H and hold
everything it will ever look at in the near field, at true scale, with no logarithm. The cost is the level of detail.
With finitely many addresses spread evenly over a very large H, everything at the reader's own scale falls within the
first address and becomes a point. A small H holds the small at true scale and the large logarithmically; a large H
holds the large and loses the small. There is always something smaller than any H's first address, as there is always
something larger past any corner, so no single H holds every scale at true scale. The best choice is to set H to the
scale of the thing being read, which places that thing at the corner; focusing an eye or zooming a lens does this.
(For a thing at x read from a standpoint at distance d, the kernel d/(x² + d²) is largest when d = x, that is, at
v = h.) The
same idea appears in the hyperbolic browser, which draws only nodes at least a pixel across (Lamping, Rao and Pirolli
1995), in mipmaps, which halve an image at each level (Williams 1983), and in web-map tiles, whose key gains one digit
per level of detail (Microsoft, Bing Maps Tile System).

**What a larger H gives and takes.** Count the room the reader gives one object, the stretch of amounts from x to
x + Δ, with n addresses across the near field: n times the stretch of lay the object covers. Inside the corner
(x + Δ ≤ H) it spans nΔ/H addresses. A larger H moves the corner away and gives the proportional field more room, but
the count is fixed, so every object inside the corner gets fewer addresses: one level of detail fewer for each
doubling of H. Past the corner (x ≥ H) the two lays of §6 part. On the logarithmic lay the object spans
n·ln(1 + Δ/x), whatever H is: its detail is set by where it is, and a larger H only moves the held levels outward,
bringing farther things in. On the in-place lay it spans n·H·(1/x − 1/(x + Δ)) = nΔH/(x(x + Δ)), which grows with H,
so there a larger H gives the far more detail as well. A small H reads the near finely; a large H reaches the far. On
the in-place lay an object gets the most room when H = √(x(x + Δ)), the corner of its own two ends, where it spans
2n·(1 − √(x/(x + Δ))), close to nΔ/x for a thin object; on the logarithmic lay it gets as much as it can have for
every H up to x. Placed on the quarter turn at arctan(x/H), two amounts are set furthest apart, at the angle
arcsin((r − 1)/(r + 1)) for a ratio r, when H is their geometric mean. The best H is the corner of what is read, as
the best estimate of a size is the corner of what is known (Proposition 13).

**More points, fewer told apart.** A reader taking its view at once looks side-on at N points spaced evenly around a
circle and reads each one's position across its view to a step ε, relative to the circle's radius. Neighbours at
angle θ from the middle of the view are about (2π/N)·cos θ apart, so the reader separates those with cos θ ≥ εN/2π,
which is R(N) = (N/π)·arccos(εN/2π) of them. This peaks at about 1.12/ε points, where εN/2π ≈ 0.65, and falls to
none at N = 2π/ε: past the peak, more points mean fewer told apart. The addresses never overflow; the resolution does.

## 9. What the geometry does not give: amounts

**Geometry first, then values.** Once the geometry is defined, a shape and one H (§5), physics assigns the values of
its placeholders, and the geometry is agnostic to that step. The values enter as multipliers on the amounts: V*/H on
each party's, and one more on all of them together when H itself is given a value in an agreed unit. They never redraw
a whole, since a whole drawn at any length but H would undo the turn (Proposition 3(e)). So no value assigned changes
the shape, the corner, the levels or any address. What the values decide is where things land among the addresses:
which fall in the near field and which past the corner, the zoom of §8.

**The amounts' error.** Under V = H the amounts equal the unit relations numerically, which is why the two are so easily
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
the centre through a surface point meets the sphere once. Sphere and cube here are the drawings of every facing together;
one wedge of the sphere lands on the three faces that meet at one corner of the cube, the cut "largest = 1" of §2,
scaled by e. Every point inside the cube but its centre is t times its surface point for exactly one t in (0, 1], a
unit relation: the cube's interior is held in proportion. So the pair
(u, t) addresses every point of the cube, and it is the same pair at every extent. The point itself, in amounts, is e
times it. A reader that holds the addresses and not e has the cube up to scale, as Proposition 8(a) says it must; it
draws the cube at its own breadth, which is V = H again, right as addresses and off as amounts by the true e/H. Each
face is the plane of one facing, so a sphere swept evenly lays the Cauchy of Proposition 5(e) on it: a face's middle
quarter by area takes 38% of the face's directions, and its centre is 3^(3/2) ≈ 5.2 times as dense as its corners.

**What reaches a reader of a payload.** Proposition 8 speaks of every reading at once. Read over time from one
standpoint, or at once from several, it has four sharper forms. Each is classical: ratio invariance, division,
triangulation and the moments of a blur. What is ours is their placement, as what a reader of a payload is given.

**Proposition 9 (one stream is one relation).** A reader at one standpoint receives readings x(t) = a(t)/b(t) of a pair
of amounts. For any positive function λ(t), the pair λ(t)·a(t), λ(t)·b(t) gives the same readings.

*Proof.* (λa)/(λb) = a/b at every t. ∎

A single stream fixes the course of the relation, not its parties. A thing coming nearer and a thing at rest growing at
the matching rate are the same stream, and so is every mixture of the two. What the stream does fix is the relation's
own pace, the reading over its rate, x/ẋ; for a thing coming nearer at a steady rate it is the time left until contact,
the quantity Lee (1976) proposed a driver reads directly when braking.
A reader taking one look after another is given motion before it is given an object.

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

(b) two readers whose placement relative to each other is known up to scale fix every place both see, up to one common
scale;

(c) one agreed length between them fixes the scale.

*Proof.* (a) A direction from a known point is a line. (b) Two lines from different points, if not parallel, meet in
exactly one point, and moving both readers by a common similarity moves every meeting point by the same similarity.
(c) By Proposition 8(b). ∎

So one reader's readings, however many, fix no place. Laid out with nothing else, they return the circle of §5, the same
from every figure. The figure comes back from a second standpoint, and its size from an agreed length. This is
triangulation, read as a ladder of what each further standpoint buys; that two views fix a scene up to its scale is the
basis of reconstruction from two images (Longuet-Higgins 1981).

**Proposition 12 (below a step, the centroid first).** Payloads w₁, …, w_n > 0 at places x₁, …, x_n along a line are
read through a step: a kernel K of total 1, mean 0 and spread σ². The reading f(x) = Σ w_i·K(x − x_i) has total
W = Σ w_i, centroid c = Σ w_i·x_i / W, and spread σ² + Σ (w_i/W)(x_i − c)².

*Proof.* Integrate the sum of shifted kernels: ∫ f = W; ∫ x f = Σ w_i x_i, since K has mean 0; and
∫ (x − c)² f = Σ w_i (σ² + (x_i − c)²). ∎

Payloads closer together than a step arrive as their total and their centroid, exactly, however close they are. Their
arrangement enters only the spread, where it is smaller than the step's own by the square of the separation over the
step: two payloads with shares β and 1 − β at separation s add β(1 − β)s² to σ².

So there are two centres, and they must not be confused:
- **The addresses' centre is the median,** an order statistic that a mean cannot replace (§7.6), had only by a reader
  that holds its readings.
- **The unresolved payload's centre is its centroid,** a weighted mean. It arrives first and exactly; the payload's
  arrangement reaches the reader only through the spread, faintly, until its parts lie a step apart.

Fingers order; rings add.

**The best estimate of the true size.** The geometry requires the drawing V = H (Proposition 3(e), Proposition 5(d)),
and the drawing says nothing about the world. To read amounts, the reader also needs an estimate of the other party's
true breadth V*, some ĉH, by which it scales the amounts the drawing gives: the reading v/h becomes ĉ·(v/h) thumbs. In
levels that is a shift of log ĉ, the same for every reading, and it leaves the circle and the turn alone. Every amount
is then off by the factor V*/(ĉH). Which ĉ is best depends on what the reader knows of V*.

**Proposition 13 (the best estimate is the median).** Measure the error by |f(V*) − f(ĉH)| for an increasing f: in
levels, f = log; in amounts, f the identity.

(a) If the reader knows only that V₋ ≤ V* ≤ V₊, the estimate whose worst error in levels is least is
ĉH = √(V₋·V₊), the corner of the pair of bounds. Its worst error is half the range, ½·log(V₊/V₋).

(b) If the reader holds a distribution for V*, the estimate whose expected error is least is a median of that
distribution. It is the same median for every increasing f. The mean, best under squared error in amounts, changes with
f and need not exist.

(c) If nothing the reader knows makes the other larger rather than smaller, so that V*/H and H/V* are alike, (a) and (b)
both give ĉH = H, the estimate equal to the drawing.

*Proof.* (a) The worst error is the larger of |log V₊ − log ĉH| and |log V₋ − log ĉH|, least when log ĉH is midway
between log V₋ and log V₊. (b) E|X − m| is least when m is a median of X. For X = f(V*) a median is f of a median of V*,
since medians commute with increasing maps, as order does (Theorem 6(b)). (c) The bounds are then H/R and H·R, whose
geometric mean is H, and log(V*/H) has median 0. ∎

So for a reader whose knowledge is symmetric in levels about its own breadth, the best estimate of the true size is its
own breadth, the same as the drawing; otherwise it is the median of what the reader knows. The drawing V = H is
required; the estimate is chosen, and this is how to choose it. The result rests on measuring error by order or in
levels, the same premise of no preferred scale as (S). Levels are what the reader's ignorance of the size leaves: an
error unchanged when the size κ = V*/H and the estimate are rescaled together, and alike for larger and smaller, is a
function of |ln(κ/ĉ)|, the error in levels, and with absolute loss in levels the best estimate is the median (b)
(§11.1). As a distribution, dκ/κ restricted to the bounds has its median at √(V₋·V₊)/H, the same estimate (§2).

**The price of a geometry.** Two acts are easily run together, and only one of them is a guess.
- *Designating* the other party, as (P0) requires, and drawing it at the reader's own breadth, V = H, as the turn
  requires (Proposition 3(e)), gives the reader its geometry: the unit relations, the corner, the circle, the sweep, and
  the Cauchy of §7. It asserts nothing about the world, since a unit relation lies in [0, 1] however large the other
  breadth is, and it costs nothing. A reader that will not designate a second party has no relation and nothing to
  read: situation 0 (§3.1).
- *Sizing* the other party, an estimate ĉH of its true breadth, gives the reader amounts: the mountain in thumbs. That
  is the arbitrary part. By Proposition 13 the reader's best size is the median of what it knows.

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
- its estimate of the other party's true breadth, ĉH, the one arbitrary number in the price of a geometry, best set at
  the median of what it knows (Proposition 13); the drawing itself, V = H, is required and is not a number to choose;
- the shared unit, which is neither a reading nor a guess but a relation measured beforehand and agreed between
  readers, needed for talking.

**Reading and writing.** Reading needs only ratios: every reading is a ratio, none contains a unit (Proposition 8(a)),
and the shape is read from ratios alone, its size the one term no ratio of radii reads (§7.4). Writing needs breadths.
To write a thing is to state it in amounts, as an equation or an array of breadths, and that is situations 1 and 2, the
whole held with V known. Reading is situations 3 and 4, the two sweeps, with V unknown. Situation 1 is common to both.
The circle, V = H, is the reader's drawing, chosen before anything arrives, and the writer's equation, with V known to
equal H: one circle held two ways, drawn by the one and known by the other. Situation 2 is writing alone, a shape
written on that circle as its perturbation (§7.4), and 3 and 4 are reading alone. Taking the reader's circle for the
writer's is the confusion of §7.1. So writers are unsituated and readers situated. To know a breadth is to hold the
whole, both hemispheres at once, which is situations 1 and 2 and which no standpoint supplies: no reading gives V*/H
(Proposition 8). An observer writes by carrying in what it did not read, a shared unit or an amount from outside, and
the view from nowhere is where that writing is done, not a place anyone stands. Reading is free: the geometry supplies
every ratio. Writing must discover the breadths, and every breadth it finds is an amount from outside the readings
(Proposition 8(b)), found by movement or by interaction. Movement takes the reader's own H as a baseline: walked once,
it gives the other's true size in the reader's own breadth, V*/H (§10, step 6). Interaction takes in what another has
measured: a shared unit, a known kind, a constant measured beforehand, and writes in a breadth both can read. Counted,
the steps are one each: from one standpoint nothing is written, each thing's size and distance free together; one
displacement of known length writes every breadth in the reader's own H, and a second adds nothing to the scale; one
number exchanged writes them for another reader; one notch agreed writes them in a public unit. An observer is both a
reader and a writer: as a reader it needs the unit relations h and v, as a writer the breadths H and V, and the value of
its own H matters only where its readings meet amounts (the zoom, §8). The one bridge between them, a unit relation
times its breadth, v·V, is the act of writing. A reader that also writes needs actual breadths: to state the other's
size in amounts is to write it, and without V* it can write only its estimate ĉH (Proposition 13); to write an amount
for another reader needs the shared unit; a world drawn in amounts is written with its breadths known, and a common
factor on all of them would change no reading. Taking the drawing V = H for a measurement (§7.1) is reading mistaken for
writing. What is written can change without any reading changing, which is why no reading recovers it.

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
a(λ) = λ^p with p ≠ 0, and L = K·x^p − C. ∎

This is classical: it is the form Luce (1959) found for any law that carries a ratio scale to a ratio or interval scale,
and the functional equations behind it were later treated in general by Aczél, Roberts and Rosenbaum (1986).
Neither kind of ruler has a corner, since no amount is laid differently from any other. The reader's own lay is
neither. Proportional up to its corner and logarithmic past it (§6), it favours one amount, the one at its joint, and
that amount is its own: its breadth H, under V = H.

Taken to its ends, the reader's lay becomes the rulers that favour none. On any stretch [a, b] of amounts, once H lies
past b the lay there is x/H, the number line, and once H lies below a it is 1 + ln(x/H), the logarithm; the in-place
lay gives 2 − H/x there, the power −1. So an H of ∞ and an H of 0 are exactly the rulers of Proposition 14, and the
corner, the one amount the lay favours, exists only for an H among the amounts read. At either end a reader with
finitely many addresses loses what it reads: an endless H puts all of it in the first address, and a vanishing H sends
all of it past the levels held, or, on the in-place lay, into the horizon's last address.

**The number line is a shared unit.** The ordinary number line is the clearest example of a unit agreed between readers.
It is one notch agreed to stand for 1, built out by counting and dividing, and its form is the form a shared ruler
must have.
- *It has no corner.* Every stretch is laid like every other: 0.5 to 1 looks exactly like 1 to 1.5, and nothing turns
  over at 1. A corner would sit at some reader's unit and favour that reader, and by Proposition 14 a ruler that
  favours none has none. The corner belongs to the reader, where its unit falls on the line, not to the line.
- *It is proportional on both sides of 1.* It is the power p = 1, the near field's plain proportion carried past the
  corner. A shared ruler can do this because its notches are lengths, and everyone who uses it can relabel them together
  when the unit changes. A reader's addresses are a count, which cannot be relabelled, and past its corner (S) leaves it
  only the logarithm (Proposition 4). Where the range is wide, people share the other ruler Proposition 14 allows, one
  whose notches are levels: decibels, stellar magnitudes, pH. Scientific notation, 3.2 × 10⁶, writes both at once, a
  count of levels with a plain ruler inside one.
- *It has the same grain everywhere.* It cannot know who will read it or how finely, so it is notched alike throughout,
  whether or not a given reader needs the detail there.
- *It is not a reader.* It reads nothing and has no standpoint, so it has no situation. A reading passes through it,
  from one reader's relations to another's, and nobody reads on it.
- *Its two infinities are its readers'.* Outward without end (1, 2, 4, …) and inward without end (1, ½, ¼, …) are
  exchanged by the flip. They are the far and near sides of whatever unit a reader holds against the line (§3.3, §4),
  not two separate properties of the line.

So the number line is not the structure of observation, and it need not be. It is the interface readers agree on so
that amounts can pass between them, made after the geometry and the readings, and its plainness, uniform and without a
corner, is what lets it favour no one. In order: the world, a reading, a relation, an address and then, between
readers, the number line.

## 10. A worked example: a mountain range

A reader looks at a mountain range, face on, from opposite its middle. From nowhere we know three amounts: the reader's
thumb H = 1 mile (the thumb is whatever single measure the reader holds; here it is a mile), the mountain's width
V* = 20 miles, and its distance d = 10 miles. The reader knows only its thumb.

**The pairs.** Each pair has its own corner, so we name them first.

| pair | ratio | where it sits |
|---|---|---|
| half-width to distance, (V*/2, d) = (10, 10) | 1 | at that pair's corner: each end of the range lies 45° off straight ahead |
| width to distance, (V*, d) = (20, 10) | 2 | one doubling past that pair's corner: the range is wider than it is far |
| distance to the thumb, (d, H) = (10, 1) | 10 | log₂ 10 ≈ 3.32 doublings past the reader's corner |
| mountain to thumb, (V*, H) = (20, 1) | 20 | log₂ 20 ≈ 4.32 doublings: the mountain is 20 thumbs |

The first two can be read from the view itself, as directions. The last two set H against amounts the reader does not
have.

**From nowhere.** The completed view holds 1, 20 and 10 in one unit, miles: the blueprint, with the range drawn 20
miles wide and 10 miles out and its ends at ±45°. Every number in the table is available to it, and the 45° is simply
where the ends are; nothing marks it. Thumb and mountain are both in hand: the mountain is 20 thumbs, and the point
where thumb equals mountain is computed, not found. There is no home, no order of arrival and no horizon. It holds the
true width, and no one stands anywhere in it.

**From where the reader stands.**
1. *The addresses come first.* The reader's circle has radius 1 mile, with the corner at 1 mile: proportional addresses
   inside, and past it the same number of addresses for each doubling, 2, 4, 8, 16 miles and on. All of this is laid
   whether or not anything is there.
2. *What it reads exactly.* Sweeping its directions, the reader finds home, v/h = 0, straight ahead at the middle of the
   range, and the range's ends at v/h = ±1: exactly at its corners. It knows that the ends sit at its corner, though
   not why. With fingers spread evenly over the half-turn, the range takes exactly the middle half of them, between the
   Cauchy's quartiles, which are its corners (§7.3), and the median finger points at its middle. On each finger the ring is the ridge's elevation
   reading, and together they give the range's skyline, up to scale. The far slopes are hidden, rings behind rings.
3. *The two vantages, on the thumb.* The one breadth the reader holds is its thumb, the H it started from, and the two
   situated vantages of §3.4 read it from the reader's own turn. Each facing side of the half-turn is a quarter turn,
   from home to the limb, where a finger runs parallel to the range and never meets it. On the thumb's circle that
   quarter turn is an arc of π/2 thumbs, and its shadow on the line across the view is exactly 1 thumb. Read by the
   central sweep, limb to limb, the whole half-turn is an arc of π thumbs over a shadow of 2, and the central reading,
   the turn over its shadow, is π/2. Read by the inscribed sweep, one finger at a time from home, the inscribed reading,
   the shadow over the turn, is 2/π: the fingers' mean shadow (0.6368 with 36 fingers). Their product is 1: H measured
   in H, the value the reader started from, which neither vantage reads alone. Out to the range's ends, at 45°, the same
   two readings are θ/sin θ = 1.1107 and sin θ/θ = 0.9003, the row of §3.4 at 45°, and their product is 1 again. None of
   this involves the mountain: a range 2 miles wide at 1 mile gives the same fingers and the same products. Joined, the
   two vantages return only what the reader put in; the mountain's breadth must be constructed (step 6).
4. *What it cannot read.* A range 20 miles wide at 10 miles, 2 miles wide at 1 or 2,000 miles wide at 1,000 gives the
   same fingers and the same rings. The reach cancels from every reading (Theorem 6).
5. *Mountain equals thumb.* Not knowing the mountain's size, the reader sets V = H: it takes the range to be one thumb,
   1 mile, wide, and the width-to-distance reading of 2 then puts it half a mile away. Every amount is off by V*/H = 20,
   the number of thumbs the mountain really is, by the same factor on both sides of the
   corner. In levels, the reader places the range at 0.5 H, inside its near field, when it is truly at 10 H, 3.3
   doublings out in the far field: a rigid shift of log₂ 20 ≈ 4.32 levels, with the pattern of readings untouched. This
   is the one number of §3.8.
6. *Constructing the truth.* A second standpoint at a known baseline closes the gap. Walk one H, a mile, toward the
   range: its half-angle grows from 45° to 48.0°, the reading s from 1 to 10/9. Then d = H·s₂/(s₂ − s₁) = 10 miles and
   V* = 2·s₁·d = 20 miles. The walk is where an amount enters: the reader's own starting value, walked once and used as
   a baseline. The true width, 20 thumbs, is constructed from two standpoints and observed from neither; it is 20 miles
   for whoever has agreed that a thumb is a mile (§9). Once d is known, the range sits at
   1 + ln 10 ≈ 3.30 on the logarithmic lay and at 2 − 1/10 = 1.9 H on the in-place lay, inside the reader's 2H.

What is the same for every reader, and exact: the fingers, the corner at the range's ends, the range's share of the
Cauchy, the skyline's shape, and the two vantages' readings of the thumb, whose product is 1. What belongs to the payload: the 10 and the 20. The view from nowhere has them and no
standpoint; the situated reader has them only by construction, and until then it is off by one factor, which is one
shift in levels.

## 11. Discussion

### 11.1 The principle, after Jaynes

With the method of §2, the results above rest on one principle rather than several:

> A situated reader gives equal addresses to whatever its readings cannot tell apart.

This is Jaynes's principle of transformation groups (1968, 1973), read as a rule for addresses rather than for belief,
and Klein's criterion applied to measures. It is applied to a group chosen as the situated reader's ignorance (§2), and
what it gives rests on that choice and on two further premises, which we name. Given that the sweep is the turning of a
rigid bar, the turns give the even turn, and so the Cauchy and the fisheye (Proposition 5); with the bar drawn at V = H
the attitudes trace the circle (Proposition 3(c)), so the circle and the Cauchy rest on one premise, the rigid turn. The
exchange of the unit relations gives the corner, and, acting on the law of the readings, the drawing V = H (Proposition
5(d)), which the rigid turn also requires (Proposition 3(e)); fairness (Proposition 2(b)) is its invariance stated as a
rule. The rescalings of the other's size give dκ/κ, and, carried to amounts, motivate premise (S) and so the logarithm
past the corner (Proposition 4); (S) is still assumed (§11.2, question 1).

Inside the corner the reader holds H as a length, and one more indifference applies: no position within H is preferred,
so equal differences within H get equal room, which is proportion. It is an indifference within the near field, not a
translation of home, which stays where it is. The two address spaces are then the same principle applied on either side
of what the reader knows, to different transformations. Their spacings, 1 and k/x, agree at x = 1 only for k = 1, the
smooth join, which is chosen (below). The halving of §6 is the same criterion applied to points.

On the reading itself a different group acts, and it should not be confused with the reader's ignorance. On the signed
reading x = v/h, over both facings, a turn acts as the Möbius map x ↦ (x·cos α + sin α)/(cos α − x·sin α), and a change
of the drawing, V = cH, as x ↦ x/c. Together these generate PSL(2,ℝ), every element of which factors as turn, change of
drawing, turn; adding the flip x ↦ 1/x gives PGL(2,ℝ), the group that preserves cross ratios. The Cauchy family is the
one family of distributions this group carries into itself (Knight 1976; McCullagh 1996), and as points m + iγ of the
upper half-plane it is the hyperbolic plane on which the group acts. The drawings V = cH are the points i/c, one line of
that plane, at distance |ln(c′/c)| from one another, the number of levels between them times ln 2. This group is not the
reader's ignorance: its change of drawing is not something the reader leaves open, since the drawing is required to be V
= H, and acting on the readings alone it is too large in Jaynes's sense, with no probability on readings unchanged by
all of it (the case he calls overdetermined, 1973, §8). It is a fact about the family of drawings, and its one use here
is to measure distances.

The estimate of the size is measured by the reader's own ignorance, not by this group. If the error e(κ, ĉ) of an
estimate ĉH is to be unchanged when the other's size and the estimate are rescaled together, it is a function of κ/ĉ; if
larger and smaller count alike, of |ln(κ/ĉ)|, the error in levels; and with absolute loss in levels the best estimate is
Proposition 13's median. The Möbius picture gives the same quantity as a distance: the even turn of the drawn bar, read
in amounts at the true breadth, is the Cauchy law at iκ, and read at the estimate it is at iĉ; their distance is
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
the square (§11.2, question 2).

**What is claimed, then.** The geometry is necessary relative to a stated ignorance, not absolutely: a reader that does
not know which unit relation a reading was divided by, which attitude the bar is in, or how large the other party is.
From that premise, with the sweep taken as the turning of a rigid bar, come the corner and the median (the exchange),
the drawing V = H (the rigid turn, Proposition 3(e), and the exchange acting on the law of readings, Proposition 5(d)),
the even turn and the Cauchy (the turns), and, through amounts and premise (S), the logarithm past the corner (the
rescalings). Each relaxation gives a named alternative rather than no geometry:
- a preferred party, with the bar no longer rigid, gives c ≠ 1, and an even turn then puts the Cauchy's median off the
  corner (Proposition 5(d));
- a preferred direction gives the square's or the line's law, with the median at the corner and the missing mean
  intact (Theorem 6(e));
- a preferred scale gives a lay that stops there (§8, §11.2 question 1).

The main result's core, order surviving and sums failing, with the median at the corner, needs only the first of the
three; the missing mean needs besides that the weight not vanish at the horizon (Theorem 6(e)).

### 11.2 Assumptions and open questions

1. *The link in Proposition 4.* (S) does not follow from "any H will do", which only places the corner. It is scale
   invariance of the lay's increments, motivated by Proposition 3(b), since a lay that breaks it builds in a scale no
   reading can fix, but assumed rather than derived. The second route of §6, an additive measure on chains of
   relations, is equivalent to it, not weaker. Is there a premise about situated readers, thinner than scale
   invariance, from which it follows? Real readers do have preferred scales, their own step among them. Here a preferred
   scale sets where the lay stops, the count of levels a reader resolves (§8), and (S) is claimed only for the lay's
   form within that range.
2. *Why Euclidean, and why the even turn?* The readings are directions only, so the norm enters only through the measure
   on directions, and the two questions are one: is there a reason, from the reader's premises, that its weight on
   directions is the one every turn leaves unchanged, rather than the square's or the line's? The median at the corner
   and the missing mean do not depend on the answer (Theorem 6(e)); the Cauchy's exact shape does. Part of the answer is
   Proposition 3(g): a sweep that is uniform and returns after a full turn has its own Euclidean measure, unique up to
   the factor H, so the norm follows from a uniform, linear sweep, and that is what remains chosen. The sharpest form of
   the objection is Drory's (2015), against Jaynes's treatment of Bertrand's chord (1973): the same symmetries, turns,
   rescaling and shifts, can be imposed in different ways, and give different measures, depending on how the random
   selection is made. We grant it. Which selection the reader makes, the even turn, is a choice (§11.1), and symmetry
   alone does not make it. What the framework adds is that the core of the main result survives the choice: any
   selection that treats the two parties alike puts the median at the corner, and leaves no mean if its weight does not
   vanish at the horizon (Theorem 6(e)).

   Three paths from all of h to all of v show what that leaves free. Sweep each evenly along its own length, and write
   b for the share of the sweep done when the direction θ is reached:

   | path, swept evenly along its length | b | at 22.5° | at the corner, 45° | at 67.5° | the mean below s, per tenfold of s |
   |---|---|---|---|---|---|
   | the circle, h² + v² = 1 | 2θ/π | 1/4 | 1/2 | 3/4 | (2/π)·ln 10 ≈ 1.47 |
   | the line, h + v = 1 | tan θ/(1 + tan θ) | 1 − 1/√2 ≈ 0.293 | 1/2 | 1/√2 ≈ 0.707 | ln 10 ≈ 2.30 |
   | the square's edges, the larger of h and v at 1 | tan θ/2, then 1 − cot θ/2 | (√2 − 1)/2 ≈ 0.207 | 1/2 | (3 − √2)/2 ≈ 0.793 | (ln 10)/2 ≈ 1.15 |

   Each has b(θ) + b(90° − θ) = 1. They agree at home (0), at the corner (½) and at the horizon (1), and part in
   between. So the two ends, the flip and fairness fix the corner and the median, and leave the scale between them
   free. Only the circle is even in the turn, and the even turn is what gives b = 2θ/π, the Cauchy's exact shape and
   the factor 2/π: the premise selects the geometry, and classical geometry supplies the factor. None of the three has
   a mean. The mean of the readings below s grows, far out, by a fixed amount each time s grows tenfold (the last
   column), because each weight reaches the horizon. The horizon condition does real work: the circle weighted by
   sin² 2θ also treats the two parties alike and keeps its median at the corner, but it vanishes at home and at the
   horizon, and its readings have a mean, 4/π.

   The three classical priors for a share come from this paper's drawings: two of the paths above swept evenly, and
   the levels. The line's is Bayes and Laplace's even share. The circle's, read at the foot of each of its points on
   the chord, which cuts the chord h² : v² (Euclid VI.8), is Jeffreys's prior for a share, the arcsine law 1/(π√(t(1
   − t))) (Jeffreys 1946). The levels give Haldane's, 1/(t(1 − t)), even in the logarithm of the odds (Haldane 1932),
   Jaynes's for complete ignorance of a share (1968). Each is unchanged by the exchange and has its median at the
   corner, ½ (Haldane's on any range of levels even about it); below t = ¼ they hold ¼, ⅓ and, over three decades of
   odds either side, 0.42. Jaynes's own answer to Bertrand, ½, is from this paper's side a situated reader's answer
   from far off (§2).

   Von Mises's water and wine, the case Jaynes left open as overdetermined (Jaynes 1973, §8), shows the same
   structure, and his method gives an answer once one premise is added. In the form Mikkelson (2004) states it: a
   liquid is wine and water, the ratio x of wine to water between 1/3 and 3; what is the chance that x ≤ 2 (von Mises
   1928)? Indifference over x gives 5/8 and over 1/x gives 15/16, each favouring one liquid, and any answer between ½
   and 1 can be had (Deakin 2006, as Parker and Jeynes 2023 report it). Answers that treat the two liquids alike, 5/6
   (even in the share of wine; Mikkelson 2004), about 0.764 (even along the hyperbola xy = 1; Burock 2005, as stated
   by Gerville-Réache 2016), the mean of 5/8 and 15/16, 25/32 (which Mikkelson considers and rejects), and the levels
   and the even turn of this paper, 0.815 and 0.847, all put the chance of x ≤ 1 at ½, the corner, and part past it.
   Parker and Jeynes (2023) reach 0.816 from scale invariance through Benford's law (Benford 1938) and maximum
   entropy, by a law that does not treat the liquids alike. Nothing in the statement fixes the unit in which either
   liquid is measured, and a change of one liquid's unit multiplies x by a constant. If, as Jaynes required of the
   chord, one law is to hold on every range of x (its restriction to a smaller range is the law there), a premise the
   problem does not state, then a law unchanged by such a change is a power of x, and the exchange of the liquids
   leaves dx/x alone, the levels, and the answer ln 6/ln 9 ≈ 0.815. The mean of 5/8 and 15/16 is also unchanged by
   the unit, but it is no single law: it weighs its two parts afresh on each range. In Jaynes's own form (at least
   half wine; what is the chance of at least three-quarters?) the range of x is unbounded, and no proper law on it is
   unchanged by a change of unit: his overdetermination. Bounded at 2^L, the levels give 1 − (log₂ 3)/L, so an answer
   needs the range held. With volume agreed beforehand as the common unit, the completed view's even share, 5/6, is
   available instead; the problem's statement does not say which reading von Mises meant.
3. *No measure on a level.* Is there a principled reason a level could not carry a measure before anything arrives?
4. *Fairness.* Proposition 2(b) needs the reading to treat both sides alike although the reader's knowledge does not.
   Is that more than a choice?
5. *Uniformity as the weight.* Now part of question 2: the argument of §7.5 moves the burden of the even turn to "why
   the circle", and the two are one question about the measure on directions.
6. *V = H.* Answered for the construction and for what a reader should do; open for what readers do. The drawing V = H
   is required for the turn (Proposition 3(e)) and for the Cauchy, forward and working back from it (Proposition 5(d)).
   That the construction works is shown where it is used. Triangulation from two standpoints (Proposition 11) draws
   every direction in one unit, which is V = H, and it is how surveying and astronomy measure distance; Mercator's
   chart, on which navigators have laid compass courses since 1569, draws V = H at every place (Proposition 5(g)). That
   shows the mathematics holds. It does not show that any particular reader, an eye, a brain or an instrument, draws
   V = H. Whether readers do is an empirical question, and this paper does not take it up. That a reader should draw
   V = H is what the propositions show, in the sense of Jaynes's principle, which says what a reader should assign given
   what it does not know, not what any reader does. Only the drawing V = H makes the reader's own turning a turn, with
   one even sweep (Proposition 3(e)). Only it lays the readings out before anything arrives with the corner at their
   median and the near field exactly a half (Proposition 5(d)), keeps every pair's corner however many parties are held
   (Proposition 5(e)), and keeps in the drawing the angles the reader turned through (Proposition 5(f), (g)). A reader
   that draws otherwise holds a consistent picture without these. The estimate of the true size is Proposition 13's: the
   median of what the reader knows, and H when what it knows is symmetric in levels about H. If the error of that
   estimate is to be unchanged when the size and the estimate are rescaled together, and alike for larger and smaller,
   it is a function of the error in levels (§11.1), and with absolute loss the best estimate is the median. What remains
   open is the group itself.
7. *Measures that cannot be normalized.* The reader's measure for the other's size, dκ/κ, has no total over all sizes,
   and such measures on a nuisance can produce the marginalization paradoxes of Stone and Dawid (1972) and Dawid, Stone
   and Zidek (1973). One reasoner integrates the nuisance out of the full data; another reasons from statistics whose
   law does not involve it; no prior lets the second reproduce the first. The paradox does not reach the reader's size,
   for a reason that is short to state. Let the data be amounts ℓ = η·w, a vector of n, with w drawn from a joint law
   g(w | ζ) whose parameter ζ no rescaling touches, and η a scale. Under the nuisance measure dη/η the first reasoner's
   likelihood for ζ is ∫ η^(−n−1) g(ℓ/η | ζ) dη, which the substitution η = 1/λ makes ∫ λ^(n−1) g(λℓ | ζ) dλ. The second
   reasoner uses the data's direction u = ℓ/|ℓ|, which no η touches; its law is found by setting η = 1 and integrating
   the length r = |ℓ| out with its Jacobian, ∫ r^(n−1) g(r·u | ζ) dr, and putting r = λ|ℓ| shows this is |ℓ|^n times the
   first. So under dη/η the two reasoners reach the same conclusion about ζ with the same prior, whatever the law g and
   whatever the signs of the data. In their own examples the paradox comes from other powers of η (in Stone and Dawid's
   exponentials, an even prior on the rate); in some laws, a gamma for one, another power produces no paradox but moves
   the prior on ζ instead. This is their group condition as Jaynes (1980) reports it: the paradox is avoided by the
   nuisance's own invariant measure. The reader's size is such a nuisance, and dκ/κ is the one invariant measure its
   rescalings have; with it a reader that integrates the size out of amounts concludes what a reader of the data's
   direction alone concludes, the ratios with their overall sign: the address reading of Theorem 6, met from the side of
   inference. Two cautions. Which of the location-and-scale family's two measures avoids the paradox depends on what is
   of interest: with μ/σ of interest the nuisance σ at fixed μ/σ carries dσ/σ, which is dμ·dσ/σ² in (μ, σ), Jeffreys's
   rule, while dμ·dσ/σ, Jaynes's, produces the paradox there; §2's note that later work favours the right-invariant
   measure holds where the location or the scale is of interest. And whether the paradox shows improper measures
   inconsistent at all is disputed (Jaynes 1980; Wallstrom 2003); the reader's lay is in any case finite, its levels
   counted.

8. *How situations 3 and 4 are read.* The two are set by the vantage, the central sweep and the inscribed (§3.1). The
   mechanism is not pinned down for either. This paper follows one proposal, the central sweep taken in at once and the
   inscribed swept one direction at a time, and what it shows of readers working that way (the bell and the fisheye,
   §7.1; the median held and the reference kept, §7.6) is shown of those mechanisms. The vantages' own readings, π/2 and
   2/π (§3.4), and every result that needs only the readings and their weight, do not depend on it. Whether a reader of
   the central sweep does take it in at once, or a reader of the inscribed sweep one direction at a time, is open.

If the principle of §11.1 stands, questions 1 and 2 become one: whether a situated reader's ignorance is exactly these
three transformations.

**Where the conclusions do not follow.**
- A reader that keeps two independent breadths and chooses neither has no relation, since (P0) fails. It lies outside
  the framework rather than against it.
- A level with more structure than its two ends, their order and the flip, such as a measure, allows other subdivisions
  than the halving, since (P2) fails.
- Plain proportion past the corner keeps true scale but cannot fit the far field on bounded addresses (§6).
- A reading that disturbs what it reads. Theorem 6(a) assumes that what arrives is the same whichever address meets it.
  Where meeting a thing changes it, as a quantum measurement does, the addresses are still laid, but nothing here says
  what then arrives at them.

### 11.3 Related work

The pieces are classical: the flip x ↦ 1/x, the Cauchy as the projection of a uniform angle and its Möbius invariance,
Cauchy's functional equation, Klein's Erlangen programme (1872), and Jaynes's and Jeffreys's invariant priors, the
first of which this paper builds on (§2). Near
neighbours in measured perception include Gilinsky's perceived distance with a finite horizon (1951), Schwartz's
log-polar map of visual cortex, proportional near the fovea and logarithmic beyond (1977), and the number-line
literature, from logarithmic-to-linear shifts (Siegler and Opfer 2003; Dehaene et al. 2008) to proportion judgment on
bounded lines (Barth and Paladino 2011). Scales that are linear near a unit and logarithmic far from it are common in
practice, astronomy's asinh magnitudes among them (Lupton, Gunn and Szalay 1999); what §6 adds is the join placed at the
flip's fixed point, where the two spacings agree. The pair and its corner appear in two-path interference: with the
paths' amplitudes in the relation of h to v, the fringe visibility is at most 2hv and the which-path predictability is
|h² − v²|, the sine and cosine of the facing, so that their squares sum to at most 1 (Greenberger and Yasin 1988;
Englert 1996). In the logarithm of the amplitudes' ratio they are its sech and tanh (Bramon, Garbarino and Hiesmayr
2004), and the visibility is whole only where the two amplitudes are equal, at the corner. The view from nowhere is Nagel's phrase (1986); Haraway (1988) called
the ideal of seeing everything from nowhere "the god trick", and van Fraassen (2008) argues that the measurer's own
position enters measurement irreducibly, as the reader's does here. In terms of limits, classical work lets the reader's
step go to zero first and then lets the count of things grow without bound; a situated reader has a fixed step and an
unknown count.

What we claim is not the pieces but their reading as one structure, set by what a reader knows of two breadths, and in
particular that the Cauchy distribution is a situated reader's addresses, not its payload. Whether this is a better way
to compute anything is an engineering question we do not take up. The aim is to explain things that are known but not
well understood: why near and far seem to obey different mathematics, why logarithmic scales appear wherever a range is
too wide to hold in proportion, and why the Cauchy has a median but no mean.

## Appendix: notation

| symbol | kind | meaning |
|---|---|---|
| h, v, v₂ | unit relations, from 0 to 1 | h relates to H, v to V, v₂ to V₂; a relation requires two, a circle has two, a sphere three; how many a system includes sets its shape |
| H | the starting value | the reader's breadth, its thumb: the one value it chooses to start the system, not a measured size; its value sets the zoom (§8) |
| V, V₂ | drawn | the other parties' wholes as the reader draws them, at H (§5) |
| V* | an amount | a party's true breadth: never read; estimated (§9) or supplied from outside |
| v/h, h/v | geometry | the reading before and past the corner |
| θ, κ | what the reader does not know | its attitude, which way its bar points; the other's size relative to its own, κ = V*/H (b in §3.8). Turns of θ and rescalings of κ leave dθ·dκ/κ unchanged; the exchange acts on readings and drawings, not on κ (§2) |
| m + iγ | geometry | a Cauchy law of the signed reading with median m and scale γ, as a point of the upper half-plane; the even turn drawn at V = cH is i/c (§2, §11.1) |
| c, ĉ | drawn; an estimate | c: the drawing V = cH, required to be 1 (Propositions 3(e), 5(d)); ĉ: the estimate ĉH of the true breadth V* (Proposition 13) |
| a, z | geometry | altitude, from the horizontal up to the vertical (the sweep from H to V), and azimuth, round the horizontal from h to v₂ (the sweep that brings in V₂); v₂/h = tan z, v/√(h² + v₂²) = tan a (§2) |
| the corner | geometry | v = h |
| home, the horizon | geometry | v/h = 0; v/h → ∞, never reached |
| g | geometry | the sweep's progress, (2/π)·arctan(v/h): 0 at home, ½ at the corner, 1 at the horizon |
| ρ | geometry | the share of the addresses at which a payload is met, in [0, 1] (after Proposition 5(d)); in §7.4, the strength of a shape's perturbation of the circle, r = exp(ρ·f(θ)); in both uses a constant ρ changes no reading |
| reading, writing | what an observer does | reading: in the unit relations h and v, with V unknown (situations 3, 4); writing: in amounts, with the breadths H and V known (situations 1, 2); situation 1 is common to both (§9) |
| address, payload | geometry; what arrives | a place laid before anything arrives; what arrives there: the finger and the ring |
| situations 0 to 4 | what a reader knows | §3.1: nothing; the circle; a shape; the central sweep, the payloads; the inscribed sweep, the addresses; with more parties, one entry per party |
| ℓ | an amount | the reach of what arrives along a ray (Theorem 6); it cancels from every reading |
| ε | a step | the reader's step, relative to what it reads (§8) |
| the shared unit | an agreement | something two readers can both read, agreed to count as 1 (§9); not a reading, and no part of the geometry |
| level | geometry | home to the corner (the first); one doubling of v/h past it |
| in-place lay | geometry | position by length: v/h inside the corner, 2 − h/v past it |
| logarithmic lay | geometry | position by number of addresses: v/h inside the corner, 1 + ln(v/h) past it |

## References

Aczél, J., Roberts, F. S. and Rosenbaum, Z. (1986). On scientific laws without dimensional constants. *Journal of
Mathematical Analysis and Applications* 119, 389–416.

Archimedes (c. 250 BC). *Measurement of a Circle*.

Archimedes (c. 225 BC). *On the Sphere and Cylinder*.

Barth, H. C. and Paladino, A. M. (2011). The development of numerical estimation: evidence against a representational
shift. *Developmental Science* 14(1), 125–135.

Beardon, A. F. (1983). *The Geometry of Discrete Groups*. Graduate Texts in Mathematics 91. Springer, New York.

Benford, F. (1938). The law of anomalous numbers. *Proceedings of the American Philosophical Society* 78(4), 551–572.

Bernardo, J. M. (1979). Reference posterior distributions for Bayesian inference. *Journal of the Royal Statistical
Society B* 41(2), 113–128.

Bertrand, J. (1889). *Calcul des probabilités*. Gauthier-Villars, Paris.

Bramon, A., Garbarino, G. and Hiesmayr, B. C. (2004). Quantitative complementarity in two-path interferometry.
*Physical Review A* 69, 022112.

Buckingham, E. (1914). On physically similar systems; illustrations of the use of dimensional equations. *Physical
Review* 4(4), 345–376.

Buffon, G.-L. Leclerc, comte de (1777). Essai d'arithmétique morale. In *Histoire naturelle, générale et particulière*,
Supplément, tome 4. Imprimerie royale, Paris.

Burock, M. (2005). Indifference, sample space, and the wine/water paradox. Preprint, PhilSci Archive 2487.

Cacoullos, T. (2014). Polar angle tangent vectors follow Cauchy distributions under spherical symmetry. *Journal of
Multivariate Analysis* 128, 147–153.

Cacoullos, T. and Papadatos, N. (2013). Self-inverse and exchangeable random variables. *Statistics & Probability
Letters* 83(1), 9–12.

Crofton, M. W. (1868). On the theory of local probability, applied to straight lines drawn at random in a plane.
*Philosophical Transactions of the Royal Society of London* 158, 181–199.

Cuadras, C. M. (2002). Geometrical understanding of the Cauchy distribution. *Qüestiió* 26(1–2), 283–287.

Dawid, A. P., Stone, M. and Zidek, J. V. (1973). Marginalization paradoxes in Bayesian and structural inference.
*Journal of the Royal Statistical Society B* 35(2), 189–233.

Deakin, M. A. B. (2006). The wine/water paradox: background, provenance and proposed resolutions. *Gazette of the
Australian Mathematical Society* 33(3), 200.

Dehaene, S., Izard, V., Spelke, E. and Pica, P. (2008). Log or linear? Distinct intuitions of the number scale in Western
and Amazonian indigene cultures. *Science* 320, 1217–1220.

Drory, A. (2015). Failure and uses of Jaynes' principle of transformation groups. *Foundations of Physics* 45(4),
439–460.

Englert, B.-G. (1996). Fringe visibility and which-way information: an inequality. *Physical Review Letters* 77,
2154–2157.

Euclid (c. 300 BC). *Elements*. Translated by T. L. Heath (1908), *The Thirteen Books of Euclid's Elements*. Cambridge
University Press.

Euler, L. (1777). De repraesentatione superficiei sphaericae super plano. *Acta Academiae Scientiarum Imperialis
Petropolitanae* 1777(1), 107–132.

van Fraassen, B. C. (2008). *Scientific Representation: Paradoxes of Perspective*. Oxford University Press.

Frank, S. A. (2014). How to read probability distributions as statements about process. *Entropy* 16(11), 6059–6098.

Frank, S. A. and Smith, D. E. (2010). Measurement invariance, entropy, and probability. *Entropy* 12(3), 289–303.

Gauss, C. F. (1828). *Disquisitiones generales circa superficies curvas*. Göttingen.

Gerville-Réache, L. (2016). Mettre de l'eau dans du vin, un paradoxe de l'indifférence ? *Implications
philosophiques*, 12 December 2016.

Ghosh, M. (2011). Objective priors: an introduction for frequentists. *Statistical Science* 26(2), 187–202.

Gilinsky, A. S. (1951). Perceived size and distance in visual space. *Psychological Review* 58, 460–482.

Greenberger, D. M. and Yasin, A. (1988). Simultaneous wave and particle knowledge in a neutron interferometer.
*Physics Letters A* 128, 391–394.

Gull, S. F. (1988). Bayesian inductive inference and maximum entropy. In G. J. Erickson and C. R. Smith (eds),
*Maximum-Entropy and Bayesian Methods in Science and Engineering*, vol. 1, 53–74. Kluwer, Dordrecht.

Haar, A. (1933). Der Massbegriff in der Theorie der kontinuierlichen Gruppen. *Annals of Mathematics* 34(1), 147–169.

Haldane, J. B. S. (1932). A note on inverse probability. *Proceedings of the Cambridge Philosophical Society* 28(1),
55–61.

Haraway, D. (1988). Situated knowledges: the science question in feminism and the privilege of partial perspective.
*Feminist Studies* 14(3), 575–599.

Herschel, J. F. W. (1850). Quetelet on probabilities. *Edinburgh Review* 92, 1–57.

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

Kellogg, O. D. (1929). *Foundations of Potential Theory*. Springer, Berlin.

Klein, F. (1872). *Vergleichende Betrachtungen über neuere geometrische Forschungen* (the Erlangen programme).

Knight, F. B. (1976). A characterization of the Cauchy type. *Proceedings of the American Mathematical Society* 55,
130–135.

Lambert, J. H. (1772). *Anmerkungen und Zusätze zur Entwerfung der Land- und Himmelscharten*. Berlin.

Lamping, J., Rao, R. and Pirolli, P. (1995). A focus+context technique based on hyperbolic geometry for visualizing
large hierarchies. *Proceedings of CHI '95*, 401–408.

Lee, D. N. (1976). A theory of visual control of braking based on information about time-to-collision. *Perception*
5(4), 437–459.

Leonard, D. (2011). Estimating a bivariate linear relationship. *Bayesian Analysis* 6(4), 727–754.

Liu, Z. and Adams, C. S. (2019). Experimental tests of Bertrand's question and the Duhem–Quine problem. *European
Journal of Physics* 40(6), 065801.

Longuet-Higgins, H. C. (1981). A computer algorithm for reconstructing a scene from two projections. *Nature* 293,
133–135.

Luce, R. D. (1959). On the possible psychophysical laws. *Psychological Review* 66(2), 81–95.

Lupton, R. H., Gunn, J. E. and Szalay, A. S. (1999). A modified magnitude system that produces well-behaved
magnitudes, colors, and errors even for low signal-to-noise ratio measurements. *The Astronomical Journal* 118(3),
1406–1410.

Maxwell, J. C. (1860). Illustrations of the dynamical theory of gases. *Philosophical Magazine* 19, 19–32.

McCullagh, P. (1996). Möbius transformation and Cauchy parameter estimation. *The Annals of Statistics* 24, 787–808.

Mercator, G. (1569). *Nova et aucta orbis terrae descriptio ad usum navigantium emendate accommodata*. Duisburg.

Microsoft. Bing Maps Tile System (documentation).

Mikkelson, J. M. (2004). Dissolving the wine/water paradox. *British Journal for the Philosophy of Science* 55(1),
137–145.

von Mises, R. (1928). *Wahrscheinlichkeit, Statistik und Wahrheit*. Springer, Vienna.

Munro, J. I. and Paterson, M. S. (1980). Selection and sorting with limited storage. *Theoretical Computer Science*
12(3), 315–323.

Nagel, T. (1986). *The View from Nowhere*. Oxford University Press.

Norton, J. D. (2008). Ignorance and indifference. *Philosophy of Science* 75(1), 45–68.

Parker, M. C. and Jeynes, C. (2023). A maximum entropy resolution to the wine/water paradox. *Entropy* 25(8), 1242.

Pitman, E. J. G. and Williams, E. J. (1967). Cauchy-distributed functions of Cauchy variates. *Annals of Mathematical
Statistics* 38(3), 916–918.

Saint-Vincent, G. de (1647). *Opus geometricum quadraturae circuli et sectionum coni*. Antwerp.

Schwartz, E. L. (1977). Spatial mapping in the primate sensory projection: analytic structure and relevance to
perception. *Biological Cybernetics* 25, 181–194.

Seshadri, V. (1965). On random variables which have the same distribution as their reciprocal. *Canadian
Mathematical Bulletin* 8, 819–824.

Siegler, R. S. and Opfer, J. E. (2003). The development of numerical estimation: evidence for multiple representations of
numerical quantity. *Psychological Science* 14(3), 237–243.

Sivia, D. S. and Skilling, J. (2006). *Data Analysis: A Bayesian Tutorial*, 2nd ed. Oxford University Press.

Smart, W. M. (1977). *Textbook on Spherical Astronomy*, 6th ed., revised by R. M. Green. Cambridge University Press.

Steiner, J. (1832). *Systematische Entwickelung der Abhängigkeit geometrischer Gestalten von einander*. Fincke,
Berlin.

Stevens, S. S. (1946). On the theory of scales of measurement. *Science* 103(2684), 677–680.

Stigler, S. M. (1974). Cauchy and the witch of Agnesi: an historical note on the Cauchy distribution. *Biometrika*
61(2), 375–380.

Stone, M. and Dawid, A. P. (1972). Un-Bayesian implications of improper Bayes inference in routine statistical
problems. *Biometrika* 59(2), 369–375.

Tissot, N. A. (1881). *Mémoire sur la représentation des surfaces et les projections des cartes géographiques*.
Gauthier-Villars, Paris.

Viète, F. (1593). *Variorum de rebus mathematicis responsorum liber VIII*. Tours.

Wallstrom, T. C. (2003). The marginalization paradox does not imply inconsistency for improper priors. arXiv
math/0310006.

Williams, L. (1983). Pyramidal parametrics. *Computer Graphics* (Proceedings of SIGGRAPH '83) 17(3), 1–11.
