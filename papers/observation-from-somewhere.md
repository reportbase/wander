# Observation from Somewhere

**Addresses, payloads and the geometry of a situated reader**

*Tom Brinkman, with Claude. Draft for external review, 11 October 2026.*

## Abstract

Classical geometry is drawn from nowhere: every length is held at once, to one scale, by no one in particular. A reader
that stands somewhere has less. It knows its own breadth but not the breadth of what it reads. This paper works out the
geometry that this one restriction leaves. We begin with the readers themselves. What a reader knows of two breadths
sets one of five situations, and these give three vantages: the completed view from nowhere, whose figure is the circle,
and two situated readers, one taking in a hemisphere at once and one sweeping it from home, whose figures are the bell
and the fisheye. The three read a line of true breadth 1 as 1, π/2 and 2/π; the true breadth is held only from nowhere,
or constructed from several observations, never observed from one. Any relation between two parties can be written as a pair of unit relations, h
and v, each between 0 and 1, and the reader reads their ratio. Because neither unit relation can pass 1, every such sweep
turns over at a single point, v = h, the *corner*, where reading v in terms of h gives way to reading h in terms of v.
To read at all, the reader must use its own breadth as the unit for the other party: its thumb as the measure of
the mountain. With that choice the corner lies at
distance 1 whatever unit was chosen, and the relation, drawn as a bar of fixed length, traces a unit circle. Inside the
corner the reader can lay out its readings in proportion; past it, if no scale is preferred, the only consistent layout
is logarithmic. The reader therefore has two address spaces, proportional and logarithmic, joined at one corner.

Our main result concerns what a reader receives when it sweeps this circle evenly from where it stands. Its readings
follow the Cauchy distribution, and we show that the distribution belongs entirely to the reader's addresses and not to
anything that arrives at them: whatever is met in each direction cancels from the reading. This explains the Cauchy's
best-known peculiarity. Its median exists and sits at the corner, because a median depends only on order, which is a
property of addresses. Its mean does not exist, because a mean is a sum of sizes, a question about the payload, and
addresses carry no size.

## 1. Introduction

Geometry as usually written is drawn from nowhere. A blueprint shows every line at its true length, to one scale,
turned neither toward nor away from anyone, and the equation h² + v² = 1 holds all its points at once. Nagel (1986)
called this the view from nowhere. It is the right view for many purposes, but it is not the view of anyone who actually
observes. An eye, an instrument or a person counting stands somewhere. It knows its own scale, its own breadth, and it
does not know the breadth of what it reads.

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

**A picture.** Hold your hand out flat, palm down, and turn it until it points straight up. The motion between is a
sweep. Spread your fingers between flat and upright: each finger is a direction in which you can look, an address. Now
put a ring on each finger. The rings are what you find in each direction, the *payload*. Turning the hand does not
change the rings, and swapping the rings for others does not change the fingers. Much of what follows is the
mathematics of the fingers alone, and the main result is that one well-known distribution, the Cauchy, is entirely
fingers.

Your thumb is your own breadth, H: the one measure you hold up. The mountain you look at has a breadth of its own, V.
If you know the mountain's size, you hold the view from nowhere, and the corner is where your thumb equals the mountain,
a point you can compute. If you do not know it, your thumb is the only measure you have, so you set the mountain equal
to your thumb, V = H, and read the mountain in thumbs.

**Three vantages.** A figure can be held in three ways. The *completed* vantage holds every breadth at once from no
standpoint; this is classical geometry, and its figure is the circle. A *situated* reader has a facing. Either it takes
in a hemisphere at once, from outside (a parallel reader), or it sweeps the hemisphere from home, one direction at a
time (a serial reader). Their figures are the bell and the fisheye. The three read the same thing differently: a line
of true breadth 1 reads 1 to the completed view, π/2 to the hemisphere turned away from the reader and 2/π to the
hemisphere turned toward it. The true breadth is had only with both hemispheres in hand, which no single observation
provides. A situated reader can construct it from several observations, but it cannot observe it. Many apparent
paradoxes come from reading one vantage's geometry as if it were another's, most often from treating the completed view
as if a single observation held it. Section 3 sets out the readers in full.

**Results.**
- What a reader knows of the two breadths sets its situation, one of five, and the situations give three vantages,
  each with its own geometry and its own reading of a line of true breadth 1. A situated reader can divide only by its
  own breadth, and what it lacks is a single number (§3).
- Every sweep between two parties turns over at one point, the corner v = h, the only point left fixed when the two
  parties are exchanged. Near and far are one geometry, read from either side of it (§4).
- A reader that holds one breadth must use it as the unit for the other party. This puts the corner at distance 1
  whatever unit is chosen and, with Euclidean length, makes the relation a unit circle (§5).
- Inside the corner the reader can lay readings out in proportion; past it, if no scale is preferred, only a
  logarithmic layout is consistent. The reader has two address spaces joined at one corner (§6).
- **Main result.** Sweeping the circle evenly from home yields the Cauchy distribution, and the Cauchy is the reader's
  addresses, not its payload. Whatever is met in each direction cancels from the reading. Order survives every change of
  payload and sums do not, which is why the Cauchy has a median, at the corner, and no mean (§7).
- How finely a reader reads is a count the geometry leaves open, and the choice of unit is a zoom, not an escape (§8).
- The geometry does not supply amounts. A common rescaling leaves every reading unchanged, one amount supplied from
  outside fixes the scale, and a fact shared between two readers supplies exactly one ratio (§9).
- A worked example, a mountain range read from nowhere and from where the reader stands, puts the pieces together (§10).

Section 11 discusses a single principle that may underlie all of these, the assumptions they rest on, and related work.
The paper is geometry only. It makes no claim about physics, perception or the structure of spacetime.

## 2. Setting

**Unit relations.** Everything here is built from the *unit relation*: a number from 0 to 1 relating a part to its
whole, none of it, all of it, or anything in between, such as the fraction of a day gone or the part of a road
behind. A relation requires two unit relations, one for each party. Draw one horizontally and one
vertically and call them h and v. They have no units, and neither knows the other's whole. The wholes they relate to are
the *breadths* H and V, which are amounts. The reader's breadth H is its thumb, the one measure it holds; the other's
breadth V is the mountain it looks at. h is the reader's side of a relation. A
circle has two unit relations, h and v; a sphere has three, h, v and v₂.

**Unit relations are not amounts.** The amounts are h·H and v·V, so their ratio is (v·V)/(h·H) = (v/h)·(V/H). The ratio
of the unit relations, v/h, is not the ratio of amounts, V/H. The only way from one to the other is to multiply by a
breadth, which must be known. We keep lowercase letters for unit relations and uppercase for breadths throughout.

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

**Addresses and payload.** An *address* is a place in the reader's layout where a reading can be put. The range of
addresses is fixed by the geometry before anything arrives, and an address is taken from it when something does. The
*payload* is what arrives. In the picture of §1 the fingers are addresses and the rings are payload. The addresses a
reader lays do not depend on what arrives at them; every "if" belongs to the payload, including which side of the
corner a given reading falls on. A *lay* is a rule
that places each reading at a position in a drawing; the *room* a stretch of readings receives is measured either by
length or by number of addresses. A *facing* is one side of the corner in one freedom; a sweep from all h to all v
covers one facing. A *level* is a stretch of the reading: the first runs from home to the corner, and past the corner
each level is one doubling of v/h.

## 3. The reader

Everything in this paper is read by someone, and what kind of reader it is decides what it can read. A reader's kind is
set by what it knows of the two breadths: not by where it is in the world, not by how many things there are, and not by
what arrives.

### 3.1 Five situations

| situation | H | V | standpoint | how it reads | example |
|---|---|---|---|---|---|
| 0 | known | not known | none | nothing: H but no h, so no relation | — |
| 1 | known | known, equal to H | none | the whole at once | an equation: the circle h² + v² = 1 |
| 2 | known | known, unequal or varying with direction | none | the whole at once | an array: a shape's breadth in every direction |
| 3 | known | not known | outside | parallel: one hemisphere at once | an apple held in the hand, its facing side seen at once |
| 4 | known | not known | inside | serial: one direction at a time | a molecule inside an endless apple, the others arriving one at a time, nearest first |

**The rule.** Three questions place any reader in exactly one situation.
1. Is anything related to the reader, so that it has an h? If not, it is in situation 0.
2. Does the reader know V? If it does, it holds the whole: situation 1 if V equals H in every direction, situation 2
   otherwise.
3. If it does not, does the thing hold still for the reader's look, so that its facing side can be taken at once from
   outside? If so, situation 3. If it changes or arrives during the look, so that it must be taken one direction at a
   time from inside, situation 4.

Each question has two answers, and each answer either ends the questioning or leads to the next question, so every
reader lands in one situation and no reader lands in two: the five are exhaustive and do not overlap. Cases that look
like a sixth reduce to these.
- *V known only within bounds* is situation 3 or 4 with its one missing number known within bounds (§3.8).
- *H unknown* leaves no reader at all: H is the reader's own breadth and is always held. Situation 0 is H with no h.
- *A reader that reads in patches* is serial across the patches and parallel within each; every single look is 3 or 4.
- *A system that changes kind* moves its reader from one situation to another over time (§3.5); at any one look the
  reader is in one.
- *Several readers* each have a situation of their own; what passes between them is the subject of §9.
- *More than two breadths* put the questions to each further breadth in turn; with V and V₂ both unknown and both set
  to H, the circle becomes the sphere (§5).

**Thumb and mountain.** Call the reader's breadth H its thumb and the other's breadth V the mountain. If the reader
knows the mountain's size, it holds the unsituated view: thumb and mountain are both in hand, and the corner, where the
thumb equals the mountain (v·V = h·H), is computed. If it does not know the mountain's size, it is situated, and the
only measure it has to give the mountain is its thumb: it sets V = H, mountain equals thumb (§5), and reads the mountain
in thumbs. The corner v = h is still found exactly, but the amounts there are the assignment's. The mountain's true
size, V/H thumbs, is the one number the situated reader lacks (§3.8).

- **0, nothing.** The reader has its breadth H, as it always does, but no h: nothing is related to it, so there is
  nothing to read and no home to lay from.
- **1, the circle.** Both breadths known and equal, held whole as an equation, h² + v² = 1, from no standpoint. The
  corner is computed, at 45°, and there is no horizon.
- **2, every other shape.** Both breadths known but unequal, or varying with direction, held whole as an array: the
  breadth in every direction, known together. The corner is computed in each direction, and there is no horizon.
- **3, parallel, outside.** A reader outside a thing, facing it, takes in the facing side at once; the far side is
  turned away. Its sweep covers one hemisphere, from the point that faces it (0) to the limb (π/2); the half past the
  limb is never swept. It counts every relation at once, and their shares make a bell (§7.1).
- **4, serial, inside.** A reader inside, one part among others, takes the rest one direction at a time, from home.
  Its view is the fisheye, the running total of the same bell (§7.1).

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

### 3.2 Which division a reader can make

A reader turns a pair of breadths into a reading by dividing, and there are two ways to divide. Which one a reader can
make is its situation.

| divide both by | (H, V) lands at | which lies on | needs |
|---|---|---|---|
| H | (1, V/H) | the number line held upright at 1: unbounded | H only |
| the whole, √(H² + V²) | (cos θ, sin θ) | the quarter circle: bounded | H and V |

A situated reader knows H and not V, so it cannot form the whole; it can only divide by H, measuring everything in
thumbs. Every system it reads lands
on one unbounded line, at its ratio, with the scale gone and a horizon at the far end. An unsituated view holds both
breadths and can divide by the whole: every system lands on the bounded quarter circle, with the corner computed at 45°
and no horizon. The two are one projection apart: projecting (1, x) toward the centre gives the circle's point.

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
- **3**, parallel, holds the laid numbers at once and reads the unit line against the circle, θ/sin θ: rising from 1
  toward π/2, approaching the line from above.
- **4**, serial, takes one number at a time, projected onto the circle, and reads the circle against the unit line,
  sin θ/θ: falling from 1 toward 2/π, approaching from below. Its view is the unit line laid out as the fisheye.
- **0** has no unit, and nothing to lay.

Past 1, every number lands closer to the circle's top and the line's end, and the numbers out to infinity crowd into the
last stretch of both without arriving: the horizon, the same on both layouts. One construction gives all five. 1 and 2
are the quarter circle, held whole; 3 and 4 live on the unit line, and the two situated readers are the two ways of
comparing the layouts, line over circle and circle over line, with 1 between them. The unit line is the address space,
and the number line is what is addressed.

### 3.4 Three vantages, and the true breadth

The five situations give three vantages, each with its own geometry.

| vantage | situations | geometry | measure of a turn θ | reads a line of true breadth 1 as |
|---|---|---|---|---|
| completed: the view from nowhere | 1, 2 | the circle; every breadth held; no facing | none | 1 |
| outer hemisphere: parallel | 3 | one facing, taken in at once; the hemisphere turns away from the reader | θ/sin θ | π/2 |
| inner hemisphere: serial | 4 | one facing, swept from home; the hemisphere turns toward the reader | sin θ/θ | 2/π |

**Where the numbers come from.** A situated reader measures by turning. Measured from the point that faces it, the arc
to angle θ is θ, while what the reader sees of it is its projection, sin θ. Outside, the reader reads arc over
projection, θ/sin θ; inside, projection over arc, sin θ/θ. The two are reciprocal at every turn:

| turned through | outside, θ/sin θ | inside, sin θ/θ | product |
|---|---|---|---|
| almost 0° | 1.0000 | 1.0000 | 1 |
| 15° | 1.0115 | 0.9886 | 1 |
| 45° | 1.1107 | 0.9003 | 1 |
| 75° | 1.3552 | 0.7379 | 1 |
| 90° | π/2 = 1.5708 | 2/π = 0.6366 | 1 |

Both tend to 1 as the turn shrinks, and neither reaches it while there is any turn. At the limb, a quarter turn, the
outer hemisphere reads π/2 and the inner 2/π. (Equivalently: a half-turn stood on a line of breadth 1 as its chord has
arc π/2, and a bar of length 1 swept evenly through a quarter turn casts an average shadow of
(2/π)∫₀^{π/2} cos θ dθ = 2/π.) The true breadth, 1, is read only with no turn at all.

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
6. So a situated reader must construct the truth from several observations: the hemisphere turned away and the one
   turned toward, read in turn and joined. The construction represents the true breadth; it does not observe it. A
   telescope survey is the working example. One exposure is one facing from one standpoint, and the survey is the
   construction. Not every combination builds: exposing the same field again lowers the noise and adds nothing;
   pointings joined at their overlaps give the shape up to a scale; only a second standpoint at a known baseline gives
   a distance (§10 works one through).
7. There are therefore two ways to the true breadth, and only two: held, unsituated, as in a blueprint; or constructed,
   situated, from several observations.

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

### 3.5 Parallel and serial: static and dynamic

Parallel and serial say how a situated reader reads; static and dynamic say why. A system is *static* to a reader if it
holds still for the whole look, so that the reader can take its facing side at once: situation 3. It is *dynamic* if it
changes or arrives during the look, so that the reader takes it one part at a time from inside: situation 4.
- *Both are situated.* Static and dynamic part 3 from 4, not situated from unsituated. The equation and the array of 1
  and 2 are held whole, with no reader standing anywhere.
- *It is measured against the reader's look, not the system alone.* A building that does not move is read serially by
  someone walking through it, and a moving flock is read in parallel by a photograph.
- *Arrival makes a reading dynamic, as change does.* A system that holds still is still read serially when news of it
  reaches the reader over time, nearest first.
- *It is not a matter of dimension.* Static is not "three dimensions" and dynamic is not "three dimensions plus time".
  Both read the same sweep, 0 to π/2, one laid across at once and one walked.

A system can change kind, and the reader must follow. A dynamic system can settle (4 becomes 3), and once its breadths
are in hand it is held whole (it becomes 2). When a system settles, the serial reader's levels can serve as the
parallel reader's addresses, and the reader need not start again. When a static system starts to change, a parallel
reader that lays its sweep once keeps a stale picture; only reading again and comparing, which is serial reading, shows
the change. So a reader that may face either kind keeps some serial check running. In both directions the reader
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
*points* (each address reaches a magnitude, an amount v·V, which needs V). Dividing and sweeping are addressing, and can
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
- *The thumb is H.* The hand's own measure is its thumb, the reader's breadth; the mountain it looks at is V. Setting
  V = H is reading the mountain in thumbs.
- *The geometry is the hand, not the rings.* Dividing v by h keeps the finger and drops the ring.
- *The serial reader is the hand and its fingers; the parallel reader holds the rings.* One walks the addresses; the
  other keeps the magnitudes, all at once.
- *The rings hide; the hand does not.* Two rings on one finger, seen along it, show only the nearer: the ring behind is
  the back side. The hand hid nothing; the rings did.
- *The far field's doublings are fingers.* Past the corner the levels are doublings (§6), addresses laid before
  anything arrives; what lands on them is rings. The fingers sit side by side on one hand, not one inside another.
- *The situations in the hand.* 0: no hand, nothing to point with and nothing pointed at. 1 and 2: the rings held
  whole, all at once, with no hand needed to reach them; in 1 every ring is alike, in 2 they differ. 3: one hand
  facing a thing from outside, all its fingers at once, each reaching the ring on the facing side. 4: inside, one
  finger at a time, each ring arriving in turn.
- *The unit circle is the hand's own arc.* In one facing it is a quarter, flat to upright, open at the top, since no
  finger is ever the horizon. The closed circle comes from turning the hand through its facings, or from nowhere,
  drawing every facing at once. The sphere is every way a hand could face, drawn from nowhere; no hand holds it.

### 3.8 What the reader lacks is one number

The situations can be written in terms of one another. A situated reader, 3 or 4, is a shape of situation 2, read
through situation 1's assumption, with situation 0's unknown on one side only. The world is a shape like any other,
with some breadth ratio; lacking it, the reader lays its readings as if the shape were the circle.

Assume a value for V, and situation 3 or 4 becomes situation 2. With directions spread evenly (§7.1), the readings in
amounts are (v·V)/(h·H) = b·(v/h), where b = V/H. Counted in doublings of the amount ratio, the readings for b = 2 are
those for b = 1 slid up exactly one doubling, every doubling's share unchanged:

| doubling of the amount ratio | ¼ to ½ | ½ to 1 | 1 to 2 | 2 to 4 | 4 to 8 |
|---|---|---|---|---|---|
| b = 1 | 0.139 | 0.205 | 0.205 | 0.139 | 0.077 |
| b = 2 | 0.077 | 0.139 | 0.205 | 0.205 | 0.139 |

So what a situated reader lacks is one number, how many thumbs the mountain is, V/H; on the count of doublings it is an
offset, log₂(V/H), not a change of pattern. Situation 2 knows the number; 3 and 4 do not; known within bounds, they know it within bounds. Assuming it
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
If the bar pivots at a point of the circle, as in Thales' configuration, a turn of θ moves its far end through a central
angle of 2θ (the inscribed-angle theorem), so the facing turns twice as fast as the sweep, from facing B at A to facing A
at B. At the corner, θ = 45° and the facing is 90°: square to AB, leaning toward neither party. There the arc stands
farthest from the segment, by 1 − 1/√2.

**What the flip gives, and what it does not.** The flip proves that the corner is the one point it leaves fixed, that
every sweep passes through it, that a reading kept within [0, 1] on both sides must change register there (Proposition
2(a)), that a fair reading puts it at the middle (Proposition 2(b)), and that expansions about home stop there. It does
not prove that the drawing is a circle, which needs Euclidean length (§5); how readings past the corner are laid out,
which needs the premise that no scale is preferred (§6); or the weight with which the sweep is counted, which needs
even steps of turn (§7). Each of these rests on its own premise, and we name it where it enters.

**Every pair has its own corner.** Any two parties have a sweep and a corner, and the corner of one pair is not the
corner of another. A corner means nothing until its pair is named. In the wedge the corner is the central ray. With
three unit relations the three pairwise corners, v = h, h = v₂ and v = v₂, are planes through the central ray v = h = v₂, and
they cut the wedge into six chambers, one for each ordering of the three unit relations.

## 5. The reader's circle

We assume three things.
- **(P0)** A relation requires two unit relations, one for each party, each relating it to an assigned breadth: h to
  H, v to V. Assigned is not known: v lies in [0, 1] however large V is, but it must relate to something.
- **(P1)** A situated reader chooses exactly one breadth, H, and holds no whole of the system. Any H will do.
- **(P2)** A level carries no measure: nothing on it but its two ends, their order and the flip between them.

**Proposition 3 (the reader's circle).** Under (P0) and (P1):

(a) the reader must set V = H;

(b) the corner then lies at distance 1 from home, whatever H was chosen;

(c) if the attitudes of the relation are turns of one rigid bar, the relation traces the unit circle h² + v² = 1;

(d) with n freedoms each set to H there are 2ⁿ facings: 4 for the circle, and 8 octants for the sphere
h² + v² + v₂² = 1, where v₂ is a second v read against the same h.

*Proof.* (a) By (P0) the other party must be assigned a breadth for there to be a relation, and by (P1) the reader's
only breadth is H. (b) The corner is one H from home measured in H: H/H = 1. A reader with unit λH reading a world scaled
by λ receives exactly the same readings, so nothing in the readings fixes H. (c) With one unit, the relation is a bar of
length 1 whose attitudes are mixes of all-h and all-v, so h² + v² = 1 when length is Euclidean, and the Euclidean norm
is, up to scale, the only norm preserved by every turn. With two units the same bar would trace an ellipse stretched by
V/H. (d) Once both parties share a unit nothing prefers one side of a freedom, so each freedom has two facings. A closed
walk through the facings must flip each freedom an even number of times, so the facings are the 2ⁿ vertices of an
n-cube, walked as a Gray code. ∎

**What V = H means.** Setting V = H is a rule of representation: the reader uses its own breadth as the unit for the
other party. It sets the mountain equal to its thumb because its thumb is the only measure it has. It is not a claim
that the mountain is the size of a thumb. Where it is not, every amount the reader reads is off by the true V/H, the
number of thumbs the mountain really is (§9). The rule constructs a relation calibrated in one unit and discovers nothing about the world.
Step (a) is close to a definition; we claim only that a relation needs two assigned breadths and a situated reader has
one. Under V = H the point where the two parties' amounts are equal, v·V = h·H, coincides with the geometric corner
v = h, the edge of the unit circle.

**The Euclidean choice.** Part (c) is where an assumption enters. One unit makes the axes commensurable, but "a bar of
fixed length" also needs a norm: under the largest-component norm the bar traces the square, under the sum norm the
line. The circle follows if the sweep is the turning of a rigid bar. The facing of §4 motivates that; it does not prove
it.

**What the count of facings borrows.** The count 2ⁿ needs no angle. That the facings tile the circle or the sphere in
equal shares, a quarter turn each or π/2 of the sphere's area each, is the Euclidean measure of (c), not part of the
count.

**Diameter 2.** The corner has two sides and only two. The reader's own level runs from home to the corner in every
facing: radius 1, diameter 2, the near field. Measured in the reading v/h, the next level runs from 1 to 2, and level k
ends at 2ᵏ. We read the 2 across the reader's own level and the 2 between levels as the same 2, the corner's two sides;
this is a reading, not a proof.

**Where the reader lives.** The reader stands at home, the centre of the circle its own choice creates. It is not the
circle. The circle read evenly from no standpoint is the completed view; read from home it is the fisheye of §7.

## 6. Two address spaces

Inside the corner the reader holds its unit and can lay its readings out in proportion: the near field at true scale.
Past the corner the flip makes the reading h/v ∈ [0, 1], but it does not say how that reading should be laid out. Let a
lay place a far reading x = v/h ≥ 1 at position r(x), counting addresses from home, with r increasing and r(1) = 1.

Choosing a different H multiplies every far reading, taken as an amount, by one common factor. A lay whose room depended
on where a reading sits, and not only on ratios, would then depend on the arbitrary choice of H. Premise (P2) points the
same way: no measure is carried past the corner, so nothing supplies a scale for the room to depend on. We therefore
require that no scale be preferred:

> **(S)** r(λx) − r(x) depends on λ alone, for all x, λ ≥ 1.

**Proposition 4.** If r is increasing and satisfies (S), then r(x) = 1 + c·ln x for some c > 0: every doubling receives
the same number of addresses, c·ln 2. If the far lay also joins the near lay r(x) = x without a kink at the corner, then
c = 1.

*Proof.* Let g(λ) = r(λ) − 1. Comparing (S) at x = μ with (S) at x = 1 gives r(λμ) − r(μ) = g(λ), so
g(λμ) = g(λ) + g(μ) for all λ, μ ≥ 1. This is Cauchy's functional equation in multiplicative form, and its only
increasing solutions are g(λ) = c·ln λ. At x = 1 the near lay has slope 1 and the far lay slope c. ∎

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
that does. Whether (S)
follows from (P1) and (P2), or must be added, is the first question of §11. Note also that the argument for (S) passes
through amounts, by way of V = H, and that the smooth join (c = 1) is a further condition rather than a consequence of
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
without end, at the reader's sides: the boundary between the hemisphere it faces and the one behind it, which no reader
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
vertical equally to keep shapes. Summed from the equator, the height on the map is y = asinh(v/h), the textbook
ln tan(π/4 + φ/2) written as one relation. Near the equator y ≈ v/h, in proportion; past 45°, the corner, y approaches
ln(2·v/h), and each doubling of v/h adds a height approaching ln 2 (0.562, 0.651, 0.682, 0.690, 0.692 for the doublings
from 1 to 32). The pole is the horizon, h = 0, which is why the map is cut off short of it. The central cylindrical
projection, whose height is v/h itself, is the plain division, proportional throughout and unbounded; Mercator's map
keeps the division's local scale 1/h but accumulates it, and so lays the same relation in proportion before the corner
and logarithmically past it. Latitude is the Gudermannian of the map's height, φ = gd(y). It is the oldest instance we
know of the two address spaces laid out.

**The proportion is in the addresses.** Within a doubling past the corner the addresses are even; how evenly things
arrive at them is up to the world. If directions are spread evenly (§7), the far share h/v has density proportional to
1/(1 + (h/v)²), so the arrivals thin toward the corner by 1.6 to 1 across the first doubling past it, 1.18 across the
second and 1.05 across the third. That unevenness belongs to the payload, not to the addresses.

## 7. The Cauchy distribution is the address, not the payload

### 7.1 Sweeping the circle evenly

With V = H the relation is a bar of length 1. A serial reader at home sweeps it from flat (all h) to upright (all v) in
equal steps of turn, and at each step holds one reading, v/h.

**Proposition 5.** (a) Equal steps of turn give unequal readings. Near home a step barely changes v/h; the corner is
halfway through the turn; near upright each step changes v/h by more and more, without bound.

(b) Counted per unit of v/h, the steps have density 2/(π(1 + (v/h)²)) on [0, ∞): the half-Cauchy distribution. Its
median is the corner, and the flip leaves it unchanged. Over both facings, with v/h signed, it is the standard Cauchy
1/(π(1 + (v/h)²)), with its median at home and its quartiles at the corners ±1.

(c) Placing each reading at its step of turn, rather than at its value, gives the *fisheye*: true scale near home,
compressed gently toward the corner and increasingly past it, with the horizon at the edge of the turn, never reached.

*Proof.* When the bar turns by a small angle, v/h changes by that angle times 1/h², and on the circle
1/h² = (h² + v²)/h² = 1 + (v/h)². So the steps per unit of v/h go as 1/(1 + (v/h)²), and normalising over a quarter
turn gives the factor 2/π. Half the turn lies on each side of 45°, and the substitution v/h ↦ h/v carries the density to
itself. ∎

In classical terms the readings are the tangent of a uniformly distributed angle: the gnomonic projection of a uniform
direction.

**The parallel reader's bell.** A parallel reader takes in every relation at once, each with its share of the turn. On
the logarithmic axis x = ln(v/h) the shares form a bell centred on the corner,

  ½·sech x = 1/(v/h + h/v),  with total area π/2, a quarter turn.

On the plain axis the same shares are 1/(1 + (v/h)²), Cauchy's curve. The bell and the fisheye are one function: the
area under the bell up to x is arctan(v/h) = π/4 + ½·gd(x), the fisheye's radius there, because the Gudermannian is
the running area under sech. The serial reader, direction by direction, has the running total, which is the fisheye; the
parallel reader, all at once, has every share, which is the bell. It is not the normal curve. With the same peak and
area the two look alike near the corner, but one level out from it the bell stands at 0.400, then 0.235, 0.123, 0.062,
halving with every further level and keeping a share in every level without end, while the normal curve falls ever
faster and its far levels vanish (0.043 at the fourth level against the bell's 0.062, and 0.002 against 0.016 at the
sixth). The bell has a horizon; the normal curve has none.

### 7.2 The main result

> **The Cauchy is not the payload; it is the address to the payload.**

Call a statistic of a set of readings an *address statistic* if it depends only on their order (the ranks, the median,
the quartiles, which side of the corner each lies on), and a *payload statistic* if it depends on their sizes (the mean,
any sum).

**Theorem 6.**

(a) *Nothing that arrives changes the Cauchy.* Suppose that whatever arrives in the direction of each step lies at some
reach ℓ > 0, an amount that may differ from direction to direction and is unknown to the reader. In the reader's unit
its components are ℓ·h and ℓ·v, and the reading is (ℓ·v)/(ℓ·h) = v/h. The readings of Proposition 5, their Cauchy count
and the fisheye are therefore the same whatever arrives, and are fixed before anything does.

(b) *Address statistics ignore the payload.* For a finite set X of readings and any strictly increasing map f, the set
f(X) has the same ranks as X, so every address statistic picks out the same element; for an odd count,
median f(X) = f(median X). Conversely, two sets with the same ranks are carried onto one another by some strictly
increasing f, so the ranks keep exactly what survives every such change, and nothing more.

(c) *Payload statistics do not.* Only an affine f commutes with the mean on every set of readings: for any f that is not
affine there is a set X with mean f(X) ≠ f(mean X). For convex f, mean f(X) ≥ f(mean X) on every X, with equality only
if f is affine on the smallest interval containing X.

(d) *The Cauchy is an address law.* Over one facing its median is v/h = 1, the corner, and its quartiles are √2 − 1 and
√2 + 1, a flip pair. Its mean does not exist: ∫₀^M x·2/(π(1 + x²)) dx = (1/π)·ln(1 + M²), which grows without bound.

*Proof.* (a) is the cancellation shown. (b) Strictly increasing maps preserve ranks; the converse follows by monotone
interpolation between matched points. (c) A strictly increasing f that satisfies f((a + b)/2) = (f(a) + f(b))/2 for all a, b is affine,
so a non-affine f fails it for some pair, and X = {a, b} is the set required; the inequality and its equality case are
Jensen's. (d) Over one facing the distribution function is
(2/π)·arctan(v/h), which is ½ at v/h = 1 and ¼ and ¾ at tan(π/8) = √2 − 1 and tan(3π/8) = √2 + 1; the integral is
elementary. ∎

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
reader that does so receives, and why equal turns is the sampling that prefers no attitude (§7.5). Nor does it show that
every Cauchy distribution met in data has this origin; a Cauchy met as data may have others, and the next paragraph
says what sets its scale when it is formed from a reading.

**Where the usual confusion comes from.** Laid evenly by direction, the sweep is uniform and bounded, g from 0 to 1, with
its middle at the corner: geometry, with nothing wild in it. Read on the axis v/h, the same lay is a Cauchy of scale 1,
and that needs no V, since h and v each run from 0 to 1. Read in amounts it is another Cauchy, of
(v·V)/(h·H) = (v/h)·(V/H), with scale V/H. Writing it as the standard Cauchy, of scale 1, silently sets V = H: it turns a
situated reader into situation 1, the circle, without knowing V. A situated reader must make that assignment (§5); the
confusion is forgetting that it was made. Taking the mean of the readings then applies an operation on amounts to
addresses, and the missing mean is what that costs: it comes from the unbounded axis of the reading, not from the
world. Where a Cauchy is met as data rather than laid as addresses, an amount has been formed from the reading by a
known length, and the distribution's scale is that length, not 1 by assumption.

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
  density proportional to (1 + |x|²)^(−3/2). Here the corner is no longer the median: only 1 − 1/√2 ≈ 0.29 of the
  addresses lie within it, and the median of |x| is √3. The median is still an address, though not the corner.

### 7.4 The shape is payload

The sweep opens a closed shape out, with home in the middle of the opening and the two ends running toward the horizon
in each facing. Opening divides out size, so each place on the opened line is an address pointing back to a point of the
closed shape, which keeps its size. Laid evenly by direction, every shape opens into the same fisheye and the same
Cauchy; the shape survives only in what arrives at each address, one breadth per direction, as Theorem 6(a)
requires. The addresses are universal, and the shape is payload.

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
| astroid | along its outline | 0.500 | 1.000 | 3.15 | 3.15 |
| ellipse, twice as tall as wide | along its outline | 0.373 | 1.479 | 0.413 | 0.826 |

Shapes unchanged when h and v are exchanged keep the corner at the middle, as the flip requires, and differ only at the
ends; the astroid's cusps make its ends heavy, the square's flat sides make them light. The ellipse, which the exchange
alters, moves its corner as well. Over 73 single-outline shapes from a drawing library the pattern is the same, with
ends from 0.27 for a gear to about 3.1 for the astroid. The test would have failed had any shape laid by direction
departed from the circle's numbers, or had a shape unchanged by the exchange moved its corner off the middle. The
Cauchy is what an even lay by direction gives, whatever the shape; a lay taken from the outline brings the shape into
the distribution. The Cauchy belongs to how the addresses are laid.

**Why the circle and the Cauchy go together.** The circle is the one shape whose two lays coincide: on a circle, equal
steps along the outline are equal steps of turn. So for the circle alone, a lay taken from the shape and a lay that
knows nothing of any shape are the same lay, and both give the Cauchy. Every other shape tells them apart. This is why
the Cauchy is usually met through the circle, as the tangent of an angle spread evenly round it: it belongs to the even
turn, and the circle is the one shape in which the even turn and the shape cannot be told apart.

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
somewhere. Situated geometry is the Cauchy; unsituated geometry is the circle.

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
follow every increasing map. What is new here is the reading: which reader, knowing what, receives the Cauchy, and that
what it receives is its own addresses rather than anything in the world.

## 8. Level of detail and the choice of H

**The count is the level of detail.** The forms of the two address spaces are fixed; their counts are not. Laying the
near field in proportion means dividing H into some number of parts, and the geometry neither knows nor uses that
number. Past the corner, what is fixed is that each doubling gets the same count, not what the count is. In both spaces
the count is the *level of detail*: the geometry gives the forms, and the level of detail gives the count.

**Size sets the level.** A thing that spans n of the reader's addresses is resolved to about log₂ n levels, one fewer
each time the number of addresses it spans halves; when it spans a single address it is a point. Nothing is requested:
the span sets the level. How many addresses a thing spans depends on amounts, which the geometry does not supply.

**H is a zoom, not an escape.** Any H gives the same circle and corner, so a reader could choose a very large H and hold
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

**More points, fewer told apart.** A parallel reader looks side-on at N points spaced evenly around a circle and reads
each one's position across its view to a step ε, relative to the circle's radius. Neighbours at angle θ from the middle
of the view are about (2π/N)·cos θ apart, so the reader separates those with cos θ ≥ εN/2π, which is
R(N) = (N/π)·arccos(εN/2π) of them. This peaks at about 1.12/ε points, where εN/2π ≈ 0.65, and falls to none at
N = 2π/ε: past the peak, more points mean fewer told apart. The addresses never overflow; the resolution does.

## 9. What the geometry does not give: amounts

**The calibration error.** Under V = H the amounts equal the unit relations numerically, which is why the two are so easily
confused. Where the true V differs from H, every amount is off by V/H, by the same factor on both sides of the corner: the
reader has read the mountain as one thumb, and it is V/H thumbs. The addresses are exact; the amounts are not. Within
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

This is the exact form of §3.4's "only two". The worked example of §10 is (b) in use: the baseline is a walk of one
known H, and it fixes the mountain's distance and width.

## 10. A worked example: a mountain range

A reader looks at a mountain range, face on, from opposite its middle. From nowhere we know three amounts: the reader's
thumb H = 1 mile (the thumb is whatever single measure the reader holds; here it is a mile), the mountain's width
V = 20 miles, and its distance d = 10 miles. The reader knows only its thumb.

**The pairs.** Each pair has its own corner, so we name them first.

| pair | ratio | where it sits |
|---|---|---|
| half-width to distance, (V/2, d) = (10, 10) | 1 | at that pair's corner: each end of the range lies 45° off straight ahead |
| width to distance, (V, d) = (20, 10) | 2 | one doubling past that pair's corner: the range is wider than it is far |
| distance to the thumb, (d, H) = (10, 1) | 10 | log₂ 10 ≈ 3.32 doublings past the reader's corner |
| mountain to thumb, (V, H) = (20, 1) | 20 | log₂ 20 ≈ 4.32 doublings: the mountain is 20 thumbs |

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
3. *What it cannot read.* A range 20 miles wide at 10 miles, 2 miles wide at 1 or 2,000 miles wide at 1,000 gives the
   same fingers and the same rings. The reach cancels from every reading (Theorem 6).
4. *Mountain equals thumb.* Not knowing the mountain's size, the reader sets V = H: it takes the range to be one thumb,
   1 mile, wide, and the width-to-distance reading of 2 then puts it half a mile away. Every amount is off by V/H = 20,
   the number of thumbs the mountain really is, by the same factor on both sides of the
   corner. In levels, the reader places the range at 0.5 H, inside its near field, when it is truly at 10 H, 3.3
   doublings out in the far field: a rigid shift of log₂ 20 ≈ 4.32 levels, with the pattern of readings untouched. This
   is the one number of §3.8.
5. *Constructing the truth.* A second standpoint at a known baseline closes the gap. Walk one H, a mile, toward the
   range: its half-angle grows from 45° to 48.0°, the reading s from 1 to 10/9. Then d = H·s₂/(s₂ − s₁) = 10 miles and
   V = 2·s₁·d = 20 miles. The walk is where an amount enters: the reader's own breadth, used as a baseline. The true
   width is constructed from two standpoints and observed from neither. Once d is known, the range sits at
   1 + ln 10 ≈ 3.30 on the logarithmic lay and at 2 − 1/10 = 1.9 H on the in-place lay, inside the reader's 2H.

What is the same for every reader, and exact: the fingers, the corner at the range's ends, the range's share of the
Cauchy, and the skyline's shape. What belongs to the payload: the 10 and the 20. The view from nowhere has them and no
standpoint; the situated reader has them only by construction, and until then it is off by one factor, which is one
shift in levels.

## 11. Discussion

### 11.1 A candidate single principle

The results above rest on several premises. They may be one. We offer the following as a conjecture.

> A situated reader gives equal addresses to whatever its readings cannot tell apart.

That is, the reader's addresses are the measure left unchanged by the transformations it cannot detect: Klein's
criterion applied to measures. A situated reader's ignorance names three such transformations.
1. *Which party is which.* Exchanging v and h changes nothing the reader can check. The fixed point of the exchange is
   the corner (Proposition 1), and fairness (Proposition 2(b)) is this invariance stated as a rule.
2. *Which attitude the bar is in.* If no turn is preferred, the Euclidean norm is the only norm all turns preserve,
   giving the circle (Proposition 3(c)), and uniform measure on angle is the only probability measure they preserve,
   giving equal steps of turn and so the Cauchy and the fisheye (Proposition 5). The circle and the Cauchy then come
   from one premise.
3. *How large V is.* Multiplying every far reading by one factor changes nothing the reader can check. The measure
   invariant under rescaling is dx/x, which gives every doubling the same number of addresses: premise (S), and so the
   logarithm (Proposition 4).

Inside the corner the reader does hold H, and what remains is that no position within H is preferred: the measure
invariant under shifts gives proportion. The two address spaces are then one principle on either side of what the
reader knows. Their spacings, 1 and 1/x per unit, agree at x = 1, so the fixed point of the flip and the meeting of the
two spaces coincide. The halving of §6 is the same criterion applied to points.

The three transformations form one group. On the ratio x = v/h a turn acts as the Möbius map
x ↦ (x·cos α + sin α)/(cos α − x·sin α) and a rescaling as x ↦ λx. Together they generate PSL(2,ℝ), every element of
which factors as turn, rescaling, turn; adding the flip x ↦ 1/x gives PGL(2,ℝ), the group that preserves cross ratios.
The Cauchy family is the one family of distributions this group carries into itself (Knight 1976; McCullagh 1996).

Choosing a measure by the transformations one is ignorant of is Jaynes's method of transformation groups (1968), and
dx/x for an unknown scale is Jeffreys's prior (1939). The claim would therefore not be the principle itself, but that a
situated reader's state of knowledge selects these three transformations, from which the structure follows. Two things
remain outside it. Invariant measures are fixed only up to a constant, so the smooth join at the corner (c = 1) is still
an added condition. And "no attitude preferred" still treats the sweep as the turning of a rigid bar.

### 11.2 Assumptions and open questions

1. *The link in Proposition 4.* Does (S) follow from "any H will do", or is it scale invariance assumed under another
   name? The second route of §6 stays with ratios and assumes instead that the measure of a chain of relations is the
   sum of its links. Is either assumption weaker than scale invariance stated outright?
2. *Why Euclidean?* Is there a reason, from the reader's premises, that the sweep must be a turn rather than the
   square's or the line's path through the same ratios?
3. *No measure on a level.* Is there a principled reason a level could not carry a measure before anything arrives?
4. *Fairness.* Proposition 2(b) needs the reading to treat both sides alike although the reader's knowledge does not.
   Is that more than a choice?
5. *Uniformity as the weight.* Does the argument of §7.5 remove the burden of the even turn, or only move it to "why the
   circle"?
6. *V = H.* Is Proposition 3(a) more than a restatement of having one breadth?

If the principle of §11.1 stands, questions 1, 2 and 5 become one: whether a situated reader's ignorance is exactly these
three transformations.

**Where the conclusions do not follow.**
- A reader that keeps two independent breadths and chooses neither has no relation, since (P0) fails. It lies outside
  the framework rather than against it.
- A level with more structure than its two ends, their order and the flip, such as a measure, allows other subdivisions
  than the halving, since (P2) fails.
- Plain proportion past the corner keeps true scale but cannot fit the far field on bounded addresses (§6).

### 11.3 Related work

The pieces are classical: the flip x ↦ 1/x, the Cauchy as the projection of a uniform angle and its Möbius invariance,
Cauchy's functional equation, Klein's Erlangen programme (1872), and Jaynes's and Jeffreys's invariant priors. Near
neighbours in measured perception include Gilinsky's perceived distance with a finite horizon (1951), Schwartz's
log-polar map of visual cortex, proportional near the fovea and logarithmic beyond (1977), and the number-line
literature, from logarithmic-to-linear shifts (Siegler and Opfer 2003; Dehaene et al. 2008) to proportion judgment on
bounded lines (Barth and Paladino 2011). The view from nowhere is Nagel's phrase (1986); Haraway
(1988) called the ideal of seeing everything from nowhere "the god trick". In terms of limits, classical work lets the
reader's step go to zero first and then lets the count of things grow without bound; a situated reader has a fixed step
and an unknown count.

What we claim is not the pieces but their reading as one structure, set by what a reader knows of two breadths, and in
particular that the Cauchy distribution is a situated reader's addresses, not its payload. Whether this is a better way
to compute anything is an engineering question we do not take up. The aim is to explain things that are known but not
well understood: why near and far seem to obey different mathematics, why logarithmic scales appear wherever a range is
too wide to hold in proportion, and why the Cauchy has a median but no mean.

## Appendix: notation

| symbol | kind | meaning |
|---|---|---|
| h, v, v₂ | unit relations, from 0 to 1 | h relates to H, v to V, v₂ to V₂; a relation requires two, a circle has two, a sphere three |
| H, V, V₂ | amounts | breadths: the reader's (its thumb), the other's (the mountain), a second other's |
| v/h, h/v | geometry | the reading before and past the corner |
| the corner | geometry | v = h |
| home, the horizon | geometry | v/h = 0; v/h → ∞, never reached |
| g | geometry | the sweep's progress, (2/π)·arctan(v/h): 0 at home, ½ at the corner, 1 at the horizon |
| address, payload | geometry; what arrives | a place laid before anything arrives; what arrives there: the finger and the ring |
| situations 0 to 4 | what a reader knows | §3.1: nothing; the circle; a shape; parallel, outside; serial, inside |
| ℓ | an amount | the reach of what arrives along a ray (Theorem 6); it cancels from every reading |
| ε | a step | the reader's step, relative to what it reads (§8) |
| level | geometry | home to the corner (the first); one doubling of v/h past it |
| in-place lay | geometry | position by length: v/h inside the corner, 2 − h/v past it |
| logarithmic lay | geometry | position by number of addresses: v/h inside the corner, 1 + ln(v/h) past it |

## References

Barth, H. C. and Paladino, A. M. (2011). The development of numerical estimation: evidence against a representational
shift. *Developmental Science* 14(1), 125–135.

Cuadras, C. M. (2002). Geometrical understanding of the Cauchy distribution. *Qüestiió* 26(1–2), 283–287.

Dehaene, S., Izard, V., Spelke, E. and Pica, P. (2008). Log or linear? Distinct intuitions of the number scale in Western
and Amazonian indigene cultures. *Science* 320, 1217–1220.

Gilinsky, A. S. (1951). Perceived size and distance in visual space. *Psychological Review* 58, 460–482.

Haraway, D. (1988). Situated knowledges: the science question in feminism and the privilege of partial perspective.
*Feminist Studies* 14(3), 575–599.

Jaynes, E. T. (1968). Prior probabilities. *IEEE Transactions on Systems Science and Cybernetics* 4(3), 227–241.

Jeffreys, H. (1939). *Theory of Probability*. Oxford University Press.

Klein, F. (1872). *Vergleichende Betrachtungen über neuere geometrische Forschungen* (the Erlangen programme).

Knight, F. B. (1976). A characterization of the Cauchy type. *Proceedings of the American Mathematical Society* 55,
130–135.

Lamping, J., Rao, R. and Pirolli, P. (1995). A focus+context technique based on hyperbolic geometry for visualizing
large hierarchies. *Proceedings of CHI '95*, 401–408.

McCullagh, P. (1996). Möbius transformation and Cauchy parameter estimation. *The Annals of Statistics* 24, 787–808.

Mercator, G. (1569). *Nova et aucta orbis terrae descriptio ad usum navigantium emendate accommodata*. Duisburg.

Microsoft. Bing Maps Tile System (documentation).

Nagel, T. (1986). *The View from Nowhere*. Oxford University Press.

Pitman, E. J. G. and Williams, E. J. (1967). Cauchy-distributed functions of Cauchy variates. *Annals of Mathematical
Statistics* 38(3), 916–918.

Saint-Vincent, G. de (1647). *Opus geometricum quadraturae circuli et sectionum coni*. Antwerp.

Schwartz, E. L. (1977). Spatial mapping in the primate sensory projection: analytic structure and relevance to
perception. *Biological Cybernetics* 25, 181–194.

Siegler, R. S. and Opfer, J. E. (2003). The development of numerical estimation: evidence for multiple representations of
numerical quantity. *Psychological Science* 14(3), 237–243.

Stigler, S. M. (1974). Cauchy and the witch of Agnesi: an historical note on the Cauchy distribution. *Biometrika*
61(2), 375–380.

Williams, L. (1983). Pyramidal parametrics. *Computer Graphics* (Proceedings of SIGGRAPH '83) 17(3), 1–11.
