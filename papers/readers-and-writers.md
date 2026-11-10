# Reads and Writes

**What one standpoint holds, what two standpoints place, and what a unit writes**

*Tom Brinkman. Rewritten 10 November 2026 (SPN R788) from version 17, which is kept unchanged as
`papers/archive/rw/reads-and-writes-record.md`; section numbers cited before 10 November are the record's. Written with AI
assistance (Claude).*

**How this paper is kept.** It is a working paper, the source of truth that AI sessions iterate on, not a text for
publication. So it is written as a specification. The definitions come first and are numbered (D1–D7); every later
section is checked against them. Claims are marked: **classical** (standard mathematics or physics), **checked** (exact
arithmetic or a measurement made here, listed under Code and data), or **reading** (ours: a way of dividing what is
known, not a result). "Checked" means the calculation is right under its stated assumptions and the code reproduces
it; whether those assumptions fit a physical system is a further claim, made case by case (§11). Each idea has one home; other sections point to it. Open questions are in §12. The propositions and
proofs this paper draws on are in *Observation from Somewhere*, archived (`papers/archive/ofs/`); where its wording differs
from this paper, this paper stands.

## Abstract

A point seen from a standpoint can be written ln(z/H) = ln(d/H) + iθ, with H the thumb held out at arm's length. Up is
the direction; across is the distance, counted in thumbs. Scaling the world, every length multiplied by one factor (the
reader's own thumb and stride with it), slides every point across by the same amount and moves nothing up. That one
motion sorts everything an observer can hold into three kinds. A **read** is the direction, [h : v]: one standpoint has
it, and scaling moves it not at all. A **place** is a gap across, a distance in thumbs or one distance against another:
scaling leaves it unchanged too, but no single read holds it; it needs a second standpoint and the step between
(parallax). A **write** is an amount, the across axis's zero tied to a unit carried in from outside, a metre or a second:
it is exactly what scaling the world moves. The write is the scale-variant companion of the read.

The read's directions are laid by the uniform turn, whose law in the reading v/h is the Cauchy: its median at the corner
v = h, its horizon never reached, no mean. It is best read as a *heat*, a continuous weight over the readings, hottest
along the look and given before anything arrives. What arrives along a direction is the *payload*, the paint. *The heat
is given; the paint is met.* A second test sorts them: change what arrives, and the directions and their heat stay
while the paint changes. Because the read adds nothing and a change to the paint moves no direction, reads never race.

None of the mathematics is new. What is offered is a division of it: which parts one standpoint has, which need two, and
which need a unit, with the plane as the frame that holds the division in one line.

## 1. Definitions

**The room, without a ruler.** Stand in a corner of a room, look at each thing, and note where it is: so far round, so
far up. You have every thing's direction and nothing's distance; a room twice as large, seen from the same corner, gives
the same notes. That is a read. Take one stride along the wall and look again. Each thing's two directions cross, and
where they cross is its place, in strides: the room now has a shape and a size in your stride, and a room twice as large,
walked with a stride twice as long, gives the same places. That is a place. Count the stride in metres, and the room is
in metres; a room twice as large now gives numbers twice as large. That is a write.

- **D1. One point, two parts.** A point seen from a standpoint is, in the writer's notation, ln(z/H) = ln(d/H) + iθ, H
  the thumb held out at arm's length: up the direction θ, across the distance in thumbs. In space the point is d·u, u a
  direction, and the across part ln(d/H) is unchanged (§2).
- **D2. A read** is the direction: [h : v] in the plane, [h : v : v₂] in space, up on the plane. It is every sweep of the
  thumb at once, from one standpoint, *home*, at one moment, given whole (§3). It comes with its heat, given, and the
  paint met along it (§4). One read holds no distance.
- **D3. A place** is a gap across: a distance in thumbs, d/H, or one distance against another, d₁/d₂. Scaling the world
  leaves it unchanged, as it leaves a read; but no single read holds it. It needs a second standpoint and the step
  between them: parallax (§6). V\*/H, a party's true breadth in thumbs, is a place; so is a time to contact counted in
  the reader's own ticks.
- **D4. A write** is an amount: the across axis's zero tied to a unit carried in from outside the world, a metre, a
  second, an agreed notch. Scaling the world moves it. One amount serves every place hung from the same thumb (§7).
  A change of units is a different operation from scaling the world: it moves every write's number and no place, no read.
- **D5. The first test.** Multiply every length in the world by k, the reader's thumb and stride included; the units
  stay outside the world. What moves is a write. What stays is a read or a place. This is the old line of dimensional
  analysis between the scale-variant and the scale-invariant (Bridgman 1922; Buckingham 1914), a sorting by invariance
  under the scaling group, as Klein (1872) sorts geometries by their groups. **Classical**; the names are ours.
- **D6. The second test.** Change what arrives, keeping the standpoint and the turn: repaint the world, move the light,
  replace a wall by a row of trees. The directions and their heat stay; the paint changes. The first test does not do
  this work: a probability, or a ratio of two amounts, is unmoved by scaling and is still not a direction. The second
  test tells a direction from a ratio of payloads.
- **D7. Joining and recording.** Joining reads, two standpoints or two moments, gives places and orders, not writes. A
  count, or a mark kept, is how a write is recorded; being an amount in a unit is what makes it a write. A count of
  strides is a whole-number record of a ratio d/stride, a place; the same count with the stride in metres is a write.
  A quantity's kind is what it is, not how it was had: a place is a scale-invariant gap across, usually had by parallax,
  and a distance in thumbs handed over by another observer is still a place.

Two independent questions sort the geometric quantities, those about directions and distances from standpoints: does
scaling the world move it (D5), and does one standpoint hold it (Proposition 8 of the archived paper: no read holds a
distance). The table is for those. A ratio of two payloads at one standpoint, one colour channel over another, is unmoved
by scaling and needs no second standpoint, yet it is not a direction of the geometry: it is a direction in the payload's
own space (§4), and D6, not this table, sorts it.

| | moved by scaling? | held by one standpoint? | kind |
|---|---|---|---|
| a direction [h : v] (up) | no | yes | read |
| a gap across: d/H, d₁/d₂, V\*/H | no | no: two standpoints and the step | place |
| the across zero tied to a unit | yes | no | write |

**The writer, as a vantage.** *The writer* names the vantage that holds everything at once: both signs of every axis,
the turn completed, the extents in amounts, the unit. Much of what it holds is places and completed joins (the circle
held whole, the facings joined, π); what only it holds is the amount, the write. So "the writer's" for π, for the
one-length circle or for trigonometry means held from that vantage, joined and completed, not that it is a write. An
observer reads while it stands and turns, places while it walks and counts, and writes when it agrees a unit; the words
name acts, not kinds of observer.

**V.** V is the other party's breadth, the mountain in the distance that the thumb is held up against. A reading is a
ratio of the thumb's own shares; V was never in it, and it does not "cancel" from it. V\*/H is a place, had by walking;
V in metres is a write, had by walking and a unit. Neither is a shortcoming of the read: the horizon, the corner as a
median and the absence of any mean are what a read with no breadth in it is.

**Reads do not conflict.** A read adds nothing, so reads of one geometry can be taken in any order, or all at once, and
they agree; a conflict needs something written where something else reads. In computing this is the condition for
running operations together without a race (Bernstein 1966). Here it holds by construction: nothing writes to the
geometry, and a change to the paint moves no direction and no heat (D6). A system whose addresses move with their
contents (an array that reallocates, a table that rehashes) has to rebuild that separation by hand. **Classical**
(Bernstein's conditions); the application is a design argument, not a proof.

**Words used throughout.** These carry over from the rulings and hold in every section.
- When H comes up, name the thumb.
- A reader's far field is said in ratios: a thing one thumb wide reads one in two, one in four, one in eight. Counted in
  thumbs, two, four, eight thumbs out, it is a place. Never "doubling" or "level".
- A reader has a vantage, never a shape: no circle, no sphere, no body.
- *Heat* and *paint* for what the read has and what it meets; *address* only as a computing metaphor or for a count of K
  places at the heat's quantiles (§5).
- π/2, 2/π, π and the one-length circle are the writer's measures of the reader's sweep (§9).
- The Cauchy has no near and no far; H lays them over the read as an overlay (§5).

**Continuous and discrete.** A read is continuous: a turn passes through every direction between two, and nothing in it
is counted. A count, of strides, of units on a ruler, of digits, is discrete, with a next and, if finite, a last. Counts
are how places and writes are kept. The writer's continuous things, the real line, the circle held whole, π and e, are
counts carried to their limit and held as finished, so there are two continuities: the reader's, never counted, and the
writer's, a count completed. These are the acts idealized: a sensor that samples has already counted, and no real
instrument is a pure read; what the paper offers real instruments is the two tests, quantity by quantity (§6, "Turns,
counts and corners").

## 2. The plane

**The equation.** Divide a point by the thumb and take the logarithm: ln(z/H) = ln(d/H) + iθ. Drawn with the direction
up and the distance across, it is Euler's plane. A turn of the world slides every point up or down; scaling the world
slides every point across by ln k; the two slides commute, and nothing else moves. So:

- **Up is the read.** θ, the direction, and every difference of directions.
- **Gaps across are places.** ln(d₁/H) − ln(d₂/H) = ln(d₁/d₂), and ln(d/H) itself, a distance against the thumb, since
  the thumb scales with the world. A slide across keeps every gap.
- **The across axis's zero, tied to an outside unit, is the write.** ln(H/metre) is the one number scaling moves.

Anyone who has pinched and twisted a map on a phone has done both slides: the phone takes the line between the fingers
after over the same line before, k·e^(iα); the real part of its logarithm is the pinch, the imaginary part the twist.
**Classical**; the reading of the parts is ours.

**Each axis has a zero, and the two are not alike.** Up, the zero is home, θ = 0, where the direction lies along h.
Across, the zero is the thumb, d = H. Both are the reader's: home is where it faces, the thumb what it holds out. The
axes differ in how they end. Up closes: within one read it runs from home to a horizon a quarter turn off, never reached,
and it wraps (θ and θ + 2π one place) only when turns are joined. Across is open both ways: no total, no natural size,
nothing on it marking a place but the thumb. That is why no read and no place gives the overall size: there is no mark on
the open axis to read it against, until a unit is carried in.

**The two corners are the plane's two mirrors.** The horizontal line θ = 45° is fixed by the reading's reciprocal,
s ↦ 1/s; the upright line d = H by the distance's, d ↦ H²/d. Turning moves the first, choosing the thumb moves the
second, along different axes. On the writer's plane every straight line of the world is one curve moved,
u = ln(p/H) − ln cos(θ − φ₀), half a turn wide, and a logarithmic spiral is a straight line. **Classical.**

**The thumb's lay is itself a turn.** The overlay's lay of distance (§5), g = (2/π)·arctan(d/H), is on the plane
½ + gd(ln(d/H))/π, gd the Gudermannian, Mercator's function. A writer can draw why. Put the plane on a sphere
stereographically, scaled so that one thumb lands on its equator: the eye is one pole and the horizon the other, the near
field the eye's half and the far field the other; g is the angle from the eye's pole over π. Euler's plane is that
sphere's Mercator chart; d ↦ H²/d is the reflection in the equator, and sech(ln(d/H)) the cosine of the latitude.
Turning the world turns the sphere about its axis; taking the thumb k times larger slides every latitude toward the
eye's pole, tan(χ′/2) = tan(χ/2)/k, the boost of rapidity ln k that a moving sky applies to directions (§4), here applied
to distance. The two motions commute, which is why both are slides on the plane, and Jaynes's dθ·dκ/κ, the measure that
suits the reader's two ignorances, is the plane's area. The sphere is the writer's drawing: its own even measure, area,
is not the read's, which per unit of the sphere's area runs as 1/sin χ, χ the angle from the eye's pole. **Checked** (to
thirty digits; `euler.html`).

**π with the direction, e with the distance.** The reader's two ignorances, after Jaynes (1968), are which way it faces
and how large things are: turns and rescalings, each a one-parameter group with an exponential map. Turns close, so
their map has a period: 2π for an oriented turn, π for the direction of a line (the projective line the readings live
on). Rescalings never close, so their map has no period, only a base. π is what is needed to say that the turn comes
back, a period forced; e is the base that lets one unit serve both axes, so that e^(iθ) is a turn of θ and e^t growth
at a rate of one, a convention (counting in thumbs serves as well). Both numbers are the writer's; the reader meets the
closing and the openness and states neither. They meet at e^(iπ) = −1, where the square (h + iv)² = e^(2iθ) sends the
far end of the sweep, the horizon the reader holds as the finite pair [0 : 1]. Through that meeting Lindemann proved π
transcendental (1882). **Classical**; the assignment to direction and distance is a reading.

**The paper in one equation.** Write the sphere's equation, three lengths about a centre: x² + y² + z² = r². Kept as
written it is the writer's: lengths held, a radius, a closed surface, every sign; scale the world and every term moves
against a fixed unit. Divide it by the thumb's own share, x²:

  1 + s² + s₂² = (r/x)²,  s = y/x, s₂ = z/x.

What is left is two ratios, unmoved by scaling, and nothing closes: where the sphere would have met itself, s runs to
infinity, the horizon. The left side is the denominator of the two-dimensional Cauchy, 1/(2π(1 + s² + s₂²)^(3/2)), the
even turn's heat on a screen square to the look (§3): its corner s = 1, its horizon s = ∞, a median and no mean. The
sphere has a shape, a size and a boundary that closes; dividing by the thumb takes the size away and opens the surface
along the rim, 90° off the look, and what is left is heat thinning outward with a tail that never completes. In the plane
Euler's formula says the same: the writer's point x + iy = r·e^(iθ), divided by the thumb, is the reading
1 + is = sec θ·e^(iθ); divided once more by its mirror, (1 + is)/(1 − is) = e^(2iθ), every length is gone and the horizon
lands at −1. What the equation leaves out is the paint (D6). **Classical**; the reading is the paper's.

**In space the plane parts.** The across part survives: space laid out by ln(d/H) beside the direction is a line times
the sphere of directions, and scaling moves only the line's coordinate and commutes with every turn. The read's heat can
still be laid flat, on Lambert's equal-area map about the look, and every turn of the look keeps it flat. What no flat
chart does is keep the turns rigid: turned by φ, Lambert's chart is stretched by 1/cos(φ/2) at the old look and by up to
2 at a quarter turn, while the stereographic chart keeps the angles and loses the heat, a quarter as hot at its rim. No
chart of a sphere keeps both (Gauss 1828; Euler 1777); the plane's one chart does both because a line times a circle is
flat. Turns of space stop being slides (§8). **Checked** (FLC).

**Two geometries, and where physics enters.** *Reader geometry* has no length in it: directions from one standpoint,
shares of one thumb, the corner, the horizon, the Cauchy, order. Classically it is close to the geometry of the lines
through one point, projective geometry seen from a standpoint (incidence, order, cross ratio, no length), with a home and
a corner of its own (Klein 1872). It can be reached two ways: as lines through the origin of a plane with the scale
divided out, the writer's route; or from incidence and order alone, with no length to set aside (von Staudt 1847), the
reader's. Places add gaps across, still with no unit: the shape and size of a room in strides. *Physical geometry* has
the unit: lengths and extents in amounts, the writer's cube with a number line on each axis, x² + y² = r² with r in
metres. Physics enters there, with the unit: a unit injects physics into a relation. Picture reality as a sheet of paper
every physical thing writes on, a stone's mass, a planet's path, a cell dividing, each in amounts. A read adds nothing to
the paper; its directions and their heat are laid over it, blank or full, and the light that arrives along them is the
paper's writing met there. This says where physics sits in this frame and tells physics nothing it does not know.
**Reading.**

## 3. Up: the read

**What a read is.** A read is every sweep of the thumb at once, from one standpoint, at one moment. A sweep is the one
length the reader holds, H, turned from all of it lying along h to all of it standing along v; the read is every such
sweep given whole, not performed one after another. H can be any value; it sets only the zoom (§5). A reading is one
direction met in the sweep, [h : v], charted as v/h, h and v each a share of the thumb between 0 and 1; the projection
from home divides, not the reader. Each sweep is centred on the crosshairs, where the thumbs cross (§5). A read holds no
time: time, like distance, is a gap between reads, and a single read carries nothing from the one before. Geometry is
free in this sense: nothing in it is computed, no procedure runs; tan, arctan and every formula for the turn are the
writer's way of stating what is already there (§9). A companion paper, *The Tangent Bridge* (reportbase/draw), proves the
split in the angle chart and runs it in the slope chart with no trigonometric call.

**The thumbs pointed; a vantage, not a shape.** The reader points its crossed thumbs at the mountain, and that pointing
gives its geometry: the corner where the thumbs cross, the fingers spread from it, near and far read as ratios of the
thumb. A writer watching would say that a length held and turned about one end traces a circle, and would call it
V = H, the thumb equal to the mountain: the *one-length circle*, held whole, with a circumference and an area. The reader
does not draw it. Circles and spheres are a line's whole turn held at once, the writer's. A reader has a standpoint and
the turn from it; walking round a shape, it gets places, and with a unit it writes (§6, §7).

**The uniform turn.** A turn measured by itself is uniform: equal turns, equal shares. In the reading s = v/h the
uniform turn over a quarter turn has the law

  (2/π) · 1/(1 + s²),  s ≥ 0,

the half-Cauchy. Its median is s = 1, the *corner*, where v = h; its quartiles √2 − 1 and √2 + 1; its far end, s = ∞,
the direction [0 : 1], the *horizon*, reached by no finite reading. It has no mean: averages of readings climb without
settling, by (2/π)·ln 10 for every tenfold further the readings run. Given the uniform turn this holds whatever is looked
at, a straight wall, a row of trees, a curved hill, an empty sky; the wall's shape only decides where each direction
meets it. The constant 2/π and the quartiles' values are the writer's arithmetic; the reader has the order of its
readings, the corner and the directions. **Classical.**

**Why there is no mean.** A mean is a sum of amounts over their count. The Cauchy weighs directions, and a direction has
no length to add; its number is a chart, and the question is what survives a change of chart. To average v/h is to take
each direction as an amount on a line, the chart in which the horizon sits at s = ∞, and the sum picks up that chart's
far end. Other charts of the same directions have means (the bounded chart s/(1 + s) averages ½), and the order
statistics do not depend on the chart: the median and quartiles commute with every increasing map of the reading, a mean
does not. So the median is the directions' and the mean the chart's. A mean of directions is well defined once an embedding is
chosen, and choosing one is the writer's step: unit vectors
over the uniform quarter turn average (2/π)(1, 1), pointing at the corner, of length 2√2/π ≈ 0.900. And a world capped at
an extent M has a Cauchy with a mean, (1/π)·ln(1 + M²) over the share below M, about 8.8 at M = 10⁶: set by the extent, an
amount written in. The payload, where it is an amount, averages (§4). Practice already takes the median of a Cauchy and
never its mean; this is the reason. **Classical**; the reason is a reading.

**The Cauchy from one length, from two axes, from a line in the world.** The family has a location m and a scale γ.
Derived from what is held, it comes in three forms.

- *One length turned.* The tip of H turned uniformly is at (H cos θ, H sin θ); the reading v/h = tan θ has no H in it.
  The share passed before the reading reaches s is, in the writer's account, (2/π)·arctan s: the standard half-Cauchy,
  scale 1, median at the corner. The scale is 1 because a reading is a ratio, and a ratio carries no scale.
- *Two axes drawn.* Draw the second axis at a length V of its own: the point (H cos θ, V sin θ), the reading
  (V/H)·tan θ, a Cauchy of scale c = V/H, its median at c. Scaling leaves c unchanged, so c is a place, not a write; but
  it needs two lengths held against each other, as √2 needs the square's two sides.
- *A line in the world.* A lamp turning uniformly lights a shore at distance d; its landings x = m + d·tan θ follow
  C(m, d), quartiles m ± d. In metres both parameters are writes. The angles follow the uniform turn whatever d is; the
  scale appears only when the landings are laid on a ruler along the shore.

The ratio of two normal amounts gives the same three: equal spreads (the first), spreads σ₁ and σ₂ (scale σ₁/σ₂), means
away from zero (a location).

| form | what is held | scale | location | kind |
|---|---|---|---|---|
| one length turned | H | 1 | 0 (the corner) | read |
| two axes drawn | H and V | V/H | 0 | a place (two lengths held) |
| a line in the world | the line's place | d | m | writes, in a unit |

So V enters the Cauchy as its scale, and only there. The point m + iγ that indexes the family is the standpoint's place
with respect to the line; the reader's ignorance is turns and rescalings, never translations, so in its own chart it
stands at i, foot 0 and height 1, and holds the standard Cauchy. Moving the standpoint is walking (§6). **Classical**;
the sorting is a reading.

**The circle's equation, divided by its own length.** The writer's circle holds amounts: x = H cos θ, y = V sin θ,
(x/H)² + (y/V)² = 1, round only when V = H, then x² + y² = r². Divide the round circle by x²:

  1 + s² = (r/x)² = sec²θ,  s = y/x.

The density is the share squared, 1/(1 + s²) = (x/r)² = h², and ds = sec²θ·dθ, so dθ = ds/(1 + s²): the uniform turn,
read as s, is (2/π)·1/(1 + s²). The Cauchy is the circle's equation used to carry an even turn into readings. (The
division is the writer's account, not something the read does.)

| | the writer's circle (with V) | the reader's Cauchy (without V) |
|---|---|---|
| a point, a reading | (H cos θ, V sin θ), amounts | s = tan θ, a ratio |
| the equation | (x/H)² + (y/V)² = 1 | 1 + s² = sec²θ |
| the law | none needed: every point stated | (2/π)/(1 + s²) = (2/π)·h² |
| what it states | the area πHV, the circumference, points | the median 1, quartiles √2 ∓ 1, the horizon, no mean |
| if V ≠ H | an ellipse | a Cauchy of scale V/H |
| the world scaled, against a fixed unit | everything moves | nothing moves |

**The standpoint and its closure.** Change the turn's standpoint and the directions move as a family: the Cauchy is
carried into another Cauchy, its centre and width the new standpoint's foot and height, m + iγ. This closure, under the
real Möbius maps of the reading (changes of standpoint and of chart), is the law's own. Not every operation on directions
keeps it: an amount entering, an edge, a square, a sum of amounts, breaks it. So the Cauchy here is not a law of what is
measured; it is the law of the uniform turn, the heat over the reader's directions. A Cauchy met elsewhere, a resonance's
line, a ratio of two normal amounts, a stable sum, may have another origin; whether a turn lies behind it is a question
to ask of each case (§11). **Classical**; the reading is ours.

**The Cauchy's routes.** Every Cauchy is one measure: the Poisson kernel of the upper half-plane seen from a point
z = m + iγ, p(x) = (1/π)·Im 1/(x − z), the harmonic measure of a line seen from a point off it. The circle and the point
off the line are one construction in two coordinates: centre the line at the foot and scale it by the height,
u = (x − m)/γ; the Cayley map w = (1 + iu)/(1 − iu) = e^(2iθ), θ = arctan u, takes the line to the circle, and the
circle's even angle, returned to the line, is dθ/dx = γ/((x − m)² + γ²); divided by π, that is p. Many mechanisms put a
point at z and reach the line from it:
- **a uniform turn read on the line**: the lighthouse, the ratio of any rotation-invariant pair, a circle seen from a
  point of it;
- **a random walk** leaving the half-plane from z (Kakutani 1944), and its twin, a normal mixed over the walk's hitting
  time;
- **a pole** a height γ off the line, p(x) = (γ/π)·|1/(x − z)|², whose Fourier pair is e^(imt − γ|t|) (§9);
- **a sum** of Cauchys, whose points add;
- **a real Möbius map**, carrying one point to another.

In the plane these are one measure, since a turn about z preserves harmonic measure; on a flat boundary they agree in
every dimension; on a curved one they part (inside a ball the straight turn and the walk land differently). One sample
never tells the routes apart; only what γ tracks can (a distance for the turn and the walk, a rate for a pole, a sum for
a sum), and the boundary's shape. So the turn does not own the Cauchy; it is the reader's route to it. "Find the turn" is,
more generally, "find the z". A fat tail with no z is not harmonic measure by any route. **Checked** (CRT); classical.

**How far apart two standpoints are: a place.** The standpoints z = m + iγ form the hyperbolic plane, and the family
carries it as its measure of distinguishability: the Fisher metric of C(m, γ) is (dm² + dγ²)/(2γ²), half the Poincaré
metric, and the divergence between two members is 2·ln cosh(d/2), d their Poincaré distance in the upper half-plane, the one with
ds² = (dm² + dγ²)/γ² (Chyzak and Nielsen give
the closed form). Every real Möbius map leaves it as it was, scaling among them; it joins two standpoints. So it is a
place (D3): unmoved by scaling, held by no single read. At one foot the distance is |ln r| for heights in the ratio r,
the gap across of §2; standing higher on both sides only makes them harder to tell apart. **Checked** (FRG); classical.

**Where the heat comes from.** The read is a heat map: a continuous weight over its readings, with nothing counted in it.
The measure is uniform by solid angle, every direction of the hemisphere alike, so by angle there is no heat; the heat is
that measure read in a coordinate. In the plane, with one thumb, a direction θ reads s = tan θ and dθ = ds/(1 + s²) =
cos²θ·ds: the heat per unit of reading is the half-Cauchy, falling as cos²θ. In space, a small patch dA of a screen one
thumb out, square to the look, at r = tan α thumbs, subtends dΩ = cos³α·dA (one cosine for the patch's tilt, two for its
distance squared), so the heat per unit of screen is (1/2π)·cos³α = 1/(2π(1 + r²)^(3/2)), the two-dimensional Cauchy:
0.35 of the peak at 45°, 0.125 at 60°, none at the rim. With n thumbs square to the look it falls as cos^(n+1). Half the
peak heat is at 37.5° off the look, with a fifth of the directions inside (the share within α is 1 − cos α); half the
directions lie within 60°, √3 thumbs out on the screen. A camera shows it: a wide lens's natural vignetting, the cos⁴α by
which a photograph's corners darken, is this cos³α and one cosine more for the aperture seen at a slant, so three of its
four cosines are the heat, there before any light arrives (0.35 of the middle at 45°, against the photograph's 0.25).
**Classical.**

**The heat depends on what it is counted per.** Per unit of turn the direction has no heat; per unit of s it falls as
cos²θ, per unit of a flat screen in space as cos³α. The heat is not a grid seen from home: marks laid evenly on a wall one
distance d away, the writer's grid, are flat in the reading and crowd toward the horizon per unit of angle, as sec²θ in
the plane and sec³α in space. The Cauchy is the other way round: the turn, even in angle, laid on that flat grid. It is
the turn per unit of the writer's grid, the *per* of §9, the rate at which a turn consumes the world. In measure theory it
is a Radon–Nikodym derivative: the turn's even measure carried onto the wall by the projection from home, against the
wall's own measure, dν/dλ = (1/π)·d/(d² + y²) for a wall d away, the half-plane's Poisson kernel. On a flat wall the two
agree in every dimension: the half-space's kernel, Γ(n/2)/π^(n/2)·d/|x|^n, is the even hemisphere carried onto the wall,
(2/|S^(n−1)|)·d/|x|^n, the same constant; in space (1/2π)·d/(d² + r²)^(3/2), the cos³α above. Stepping back composes the
kernels, e^(−d|k|), the Poisson semigroup in the standpoint's height. This is Laplace's equation, a steady state; it is
not the heat equation, whose kernel is the Gaussian, e^(−tk²). The Gaussian too keeps every frequency, damping the fine
ones by k² where the Cauchy damps by |k|; the kernel that loses frequencies outright is the floor's box blur, whose
transform has zeros. The "heat" here is a weight over readings, never diffusion in time. **Classical.**

**Heat maps combine without reconciling.** Two shapes combine only by working out their boundaries. A heat map has no
boundary, so the heat adds. Two senses of combining stay apart: readings added give one Cauchy again, the standpoints
added, z₁ + z₂ (a relay of standpoints); heat maps laid over each other add too, but their sum is a heat map, not one
Cauchy: two peaks stay two. Averaging n readings gives back the same Cauchy, no narrower; the median gains, the mean
nothing. **Classical.**

**The reader never sees a shape.** This is about what one read determines, not about what a visual system infers. A
thing is, to one read, the directions it paints. Its shape is a radius along each direction from its own centre, and no
radius is in a read: a single read determines no distance along any direction, and so no shape. A shape comes back only
from more than the bare read: from structure in the paint (ratios of radii carried by what arrives, §4), or from further
standpoints as places, in the stride; with a unit, in metres. The
reader's side is whole; the shape was never the read's to lack.

**Passive.** The reader sends nothing. It is not a radar. A ranging instrument carries in the signal's speed and a
clock, two amounts, so its ranges are writes.

## 4. The paint

**Heat and paint.** A direction from home, with its heat, is the read's; a payload, the paint, is what arrives along it.
They share one thing, the point where a direction meets the world.

**The hand.** Hold up a hand, thumb out, to a stained-glass window. The thumb is H: the one length held, its size
chosen, setting only the zoom. The fingers, spread from flat to upright, are the directions; the reader does nothing to
lay them, and wherever the hand is held the geometry gives the same fingers spread the same way, evenly by turn, half
below the corner. Each finger is lit by the pane it lines up with: the coloured light is the paint, the world's, met on
the fingers, and it changes with what is in front of them. No colour carries how far the light came; walking is the way
to distance (§6). Hold the thumb against a mountain range and the range spans so many fingers; drawn at the thumb's own
size, every amount read from it would be off by V\*/H, a place had only by walking (§10). The fingers are coloured,
never colour: painting on them would be writing. In space the window is held with both hands (§8). **Reading**; after
Gibson's ambient optic array (1979). The world decides what meets each direction, which
thing is nearest and what it sends back; nothing it does moves a direction or its heat. Scale the world and nothing moves;
change the world and nothing moves. A rate is a payload per direction: the *of* is the paint, the *per* the read (§9).

**The payload is not lost.** No part of the payload goes into making the directions or their heat, so all of it
arrives, along directions given before it came. Four ways give it back, each exact in the ideal model, with the heat
known and the payload given whole; from finite, noisy samples each is an estimate, and undoing the blur is the least
stable.

- *By its ratios.* Two payloads read against each other make a direction [p₁ : p₂] in the payload's own space, unmoved
  by scaling: the light along one direction over the light along another, one colour channel over another, the radius in
  one direction over the radius in another. A shape about a centre, ln r = a₀ + f(θ) (the real part of ln z as a function
  of the turn), comes back this way: every mode of f from ratios of radii, exactly. The modes are places (gaps across,
  D3); a₀, the overall size, is the across value against a unit, a write, and no ratio gives it. Radio astronomy reads
  polarization this way: a source's intrinsic polarization angle, from the ratio of its Stokes U to Q, is unmoved by
  scale, while the Faraday rotation that turns it, RM·λ², carries the rotation measure in radians per square metre, a
  write (Burn 1966).
- *By dividing the heat out.* What is counted along the directions is the heat times the payload's weight,
  ρ(θ)·2/(π(1 + s²)). The heat is known before anything arrives, so dividing by it leaves the payload's distribution
  exactly, up to its total: the astronomer's flat field, importance sampling's 1/p. The median direction of what arrives
  is the payload's median, at the corner only when the payload weighs alike on both sides.
- *By undoing the blur.* Seen from a height γ, the payload arrives smoothed by the Cauchy kernel, whose transform
  e^(−γ|k|) is never zero: every mode survives, damped, and comes back multiplied by e^(γ|k|), noise with it. A box
  blur's transform has zeros, and those modes are gone. Unique in principle is not the same as stable.
- *By averaging it.* The payload is amounts, and amounts have means: weighted by the known heat, the light across the
  turn totals exactly wherever that total is finite. The mean was never missing from the payload, only from the
  directions.

A known measure can be divided out and an invertible blur undone; a floor that discards cannot. **Classical**; the
sorting is a reading.

**The lighthouse.** A lamp turns evenly and throws a flash along each direction. On a straight shore the landing x
obeys (x − α)/β = tan θ, α the lamp's foot on the shore and β its distance. The angles are the lamp's directions, laid
evenly whatever shore there is; the landings follow a Cauchy because the shore is straight; within each flash the path
to the shore cancels. The lamp's own corner, the flash halfway through the quarter turn, lands at the foot plus one
distance only if the shore is measured at the sea's own scale; drawn on a ruler c times the sea's, the halfway flash lands
at arctan c. To read β from the landings, take half the spread between the quartiles, never the mean. In metres β is a
write: it needs the shore found and a ruler laid along it. The lamp is the read, the shore the line where V comes in as
the scale. **Classical.**

**Mercator's map.** A navigator wants a straight line on the chart to be a constant compass bearing. On a chart whose
parallels are spaced so that a degree of latitude is drawn c times a degree of longitude there, a bearing ψ is drawn at
tan ψ′ = tan ψ/c; bearings are true everywhere only at c = 1, both directions drawn at one length at every place,
Mercator's chart (1569). It keeps every direction and pays in area, stretched by sec² of the latitude, so Greenland is
drawn about as large as Africa, which is some fourteen times its area. The equal-area chart draws c = cos² of the
latitude and gives up the bearings. Each keeps what it was made to keep; only the globe keeps both. Mercator's map is
also not the read: it is a chart of the whole field, every stretch where the reading halves alike, with no focus; the
read is the turn, finest where it looks. Bearings are reads; areas in a unit are writes. **Classical.**

**A moving sky.** An observer moving through a field of stars at a fraction β of the speed of light sees each star change
in two ways, and special relativity writes them as two formulas. Where the star is seen moves: aberration,
cos θ′ = (cos θ + β)/(1 + β cos θ), the same at every frequency. On the stereographic chart of the sky it is z ↦ z/k,
k = e^η, η the rapidity, a Möbius map of the directions, carrying the Cauchy's family onto itself; a sky uniform in the
stars' frame is seen as the spherical Cauchy, density D²/4π. (The sky's own uniform heat on the stereographic chart is
(1/π)·dA/(1 + |z|²)², not the plane's two-dimensional Cauchy, which is half the sky on a flat screen. No law on the sky
is unchanged by boosts; the uniform one is unchanged by turns, and boosts carry it within its family.) What arrives
changes: the Doppler factor D = √(1 − β²)/(1 − β cos θ′) scales each photon's energy and rate, a weighting of the
payload that moves no direction. For a sky uniform in its frame, counting total power, the D⁴ brightening ahead is D² of
directions crowding (the heat) and D² of payload. On ξ = −ln tan(θ/2), the pseudorapidity, aberration is a slide by η,
so directions alone give the rapidity, with no clock, no frequency and no speed of light, provided every source is counted
whatever its brightness and the sources are uniform in their frame. Taken so, from one look, the rapidity is a read: the
slide of one read's median against where the premise puts it, unmoved by scaling, with no second standpoint. Taken as
the sky's median before a boost against after, it joins two looks: a place. The speed in metres a second needs c carried in, and D read as a line's shift needs the
line's rest frequency: both writes. **Classical**; the sorting is a reading.

## 5. Near and far

**The crosshairs.** Cross the thumbs (§8) over whatever is looked at, the look running down their diagonal. Where they
cross is the corner: the thing there reads one thumb along each thumb, every pair alike, v/h = v₂/h = 1, and it is drawn
one thumb wide. Along the line of sight it lies √2 thumbs off in the plane and √3 in space, the diagonal of a square or a
cube one thumb on a side. That crossing, with H, lays the near field and the far field over the read, as an overlay: the
Cauchy itself has neither. Along every direction one thumb splits the heat in distance in half, whatever H is.

**Near and far.** The near field is a single thumb, laid evenly: everything nearer than the crossing gets its heat in
proportion, the first half of the thumb as much as the second. The far field is read in ratios: a thing one thumb wide
reads one in two, one in four, one in eight, and two far things are related by the ratio of their readings ("one in eight
is half of one in four"), the same at every scale. Each stretch over which the reading halves holds the same heat as the
one before, out toward the horizon. Counted, "8 thumbs out, three stretches past the corner", it is a place; given a
value, 1 + ln(d/H) with a base chosen (§2), or 2 − H/d on a lay that keeps all of reality within two thumbs, it is the
writer's number for what the read holds as a ratio. There is one corner, the split between the near field and the first
stretch; past it the stretches are plain. Move the crosshairs and the split goes with them.

**The overlay's heat in distance.** Along every direction the share of distance below x = d/H is (2/π)·arctan x. Per
unit of plain distance it is greatest at the eye, 2/(π(1 + x²)); per unit of ln(d/H), by ratio, it is
(2/π)·x/(1 + x²) = (1/π)·sech(ln(d/H)), hottest at one thumb and cooling alike both ways: 0.8 of the peak at one in 2 and
at two thumbs, 0.47 at one in 4 and four, 0.25 at one in 8 and eight, never zero. A writer counting it as K places puts
them at d/H = tan(kπ/2K), the first K/2 inside one thumb. Past it the share left beyond x thumbs is (2/π)·arctan(1/x),
0.295 past two thumbs, 0.156 past four, 0.079 past eight: a heavy tail, so no mean of distances. The split is a mark at
one thumb on every direction, each one's median, not a body. Take the overlay away and the Cauchy is unchanged.
**Classical.**

**The hot spot.** Put the two heats together and the read has two centres. The eye is where every direction starts, a
point with no size. The hot spot is one thumb out along the look, where the thumbs cross: the corner twice over, in
direction the triple corner [1 : 1 : 1], in distance d/H = 1, the point fixed when every distance ratio is turned over,
and the median as well as the peak. The two corners meet there only because the reader points its thumbs at a thing and
takes that thing as its thumb; pointed elsewhere, the heat moves and no direction does. From the hot spot the heat thins
every way: across the look as cos³α, along it as sech(ln(d/H)). The near field runs from the eye to the hot spot,
distance in proportion; the far field from the hot spot to the horizon, in ratios; each holds half the heat. A writer
joining the cuts on every direction draws the near-field sphere of radius H (§8). The reader holds only the mark one
thumb out on each direction it reads.

**The one-thumb circle, and the three corners.** Everything within one thumb of the crosshair's point is a ball (a disc
in the plane) touching each face of the wedge, at the cube's corners one thumb back along each thumb. From the eye its
outline is a circle 35.26° about the look, the largest about the crosshair inside the wedge, holding 73% of its
directions; in the plane the same construction runs ±45°, home to horizon. Whatever is pointed at becomes the corner, so
the circle goes with the look. Home is on it, at the three points it touches. Each pair of thumbs has its own corner, a
line through the crosshair, the three crossing there 120° apart; along each, the third thumb runs a quarter turn from
home on the circle (35.26° off the look) through the corner to the horizon at that thumb's direction (54.74° off). Inside
the circle there is no distortion at the corner, every pair's ln(v/h) zero there; moving out each direction's
grain holds more, in proportion, as one over twice the reading toward home: compression, not blur, hexagonal near the
corner and unbounded only at the three homes. It is a precision, not a size: laid by turns off the look a thing's place
parts from a flat screen's only far out (tan α/α, 1.10 at 30°, 1.27 at 45°). **Checked** (THM).

**Laid by the heat.** A flat screen does not give each direction the same room; the screen that does is Lambert's
equal-area map about the look, a direction α off it at radius 2·sin(α/2): true at the crosshair, off by 0.9% at 15°, 3.4%
at 30°, 7.6% at 45°. Laid that way the rings of the distance overlay come where the readings fall: one thumb off the look
at 0.765, then one in two, one in four, one in eight at 1.05, 1.23 and 1.32, packing toward the rim at √2, because each
stretch holds fewer of the look's directions than the one before (0.26, 0.20, 0.12 of what is in front, and 0.12 past one
in eight). The ground has its own reading: a point ρ along it, with the thumb's ground point D away, reads
(2/π)·atan(D/ρ), one at the feet, a half at the thumb, zero at the horizon, so the far ground gathers in rows just under
the horizon. A world made only where the view reaches, from cells at every scale kept only where a thing spans π/(8K) or
more, gives the same read. **Checked** (`crosshairs.html`).

**H is a zoom; K comes first.** The reader's fineness is finite, its resolution K, which comes before H. H, the thumb it
holds up, decides how K is split: half of it lies inside H at every H; a small H makes the near ones fine and puts more of
the world past the held edge, a large H the reverse. No H holds everything. The best H for a thing is the one that puts
it at the corner, where the relative grain is finest; so the corner follows the focus, and what is looked at is drawn one
thumb wide.

**Where the split falls: looking around.** Pointed at a thing, the crossed thumbs take its distance as H, so the thing
sits at the corner, half of every direction's distance heat nearer and half farther. The reason to do this is that it is
optimal: the corner is where a reading's cells are finest relative to their place, and a thing at the corner is at
parallax's corner, where a step of two thumbs places it with the least error (§6). Putting the thing looked at on the
corner is what a reader should do; whether readers do is open (§12).

**K and N.** N is how many items there are; K how many are held. To know N is to know the whole, its extent in amounts
and how much is in it: a write. A reader never knows N; it knows K, read continuously as the turn is, a fineness with no
last place. Laid out as K places at the heat's quantiles, K *addresses*, it is a count, and addresses here are always
that; as a metaphor they serve where they connect the Cauchy to computing (a direction looked along is like an address
looked up, with the heat under it). The Cauchy spreads the reader's K over a world of any size, the near field in
proportion, the far in ratios, and, counted as K addresses, everything past the last on the one at the horizon. Double
N and the view does not change; make N unbounded and it still does not (an infinite star field browsed at N and 2N shows
the same view, apart by less than 10⁻⁷ at N = 2⁴⁰). So the Cauchy is a cull: an implementation holding K samples does
O(K) work, whatever N. What the cull gives up is sameness: a writer who knows N holds every item as 1/N of the whole, all
alike, with no standpoint favoured; a reader's K is spent finest at the corner and coarser each stretch away, and that
unevenness is the vantage. **Checked** (`star-field.html`).

**The read as a control.** The same split can be held in the hand as a dial. A held push adds to the hyperbolic angle
ζ at a steady rate; the place it reaches is one thumb times sinh ζ from home, and the needle is drawn at the turn gd ζ,
so it never leaves the quarter turn. Near home the place moves in proportion; one thumb out it reaches the corner
(ζ = 0.881, the needle at 45°); far out a steady push reads a steady ratio, one in two each ln 2 of ζ (2.31 from the corner
itself, 2.0037 ten thumbs out, 2 within 4·10⁻⁵ at a hundred). The needle turns per unit of place as cos²θ, half at the
corner. With one more degree of freedom the control is a dome looking down on a floor without end: home straight down,
the rim the horizon, the heat per unit of floor cos³α; each place painted by what its one direction meets, so a far place
is a sample of the floor, read at the detail its footprint earns, a few dozen tiles for the whole world. Laid as sound,
one in two is an octave, and a tone of octaves that rises without arriving (Shepard 1964) is the horizon heard. None of it
needs a count of what is out there. **Checked** (reportbase/calendar's dials).

**Drawing a shape: circles, a height, a step toward the detail.** A closed outline about a centre can be written as
circles on circles, its Fourier series: the turns of one standpoint at the centre, evenly. Seen from a height γ, the
outline is smoothed by the circle's own Cauchy, the wrapped Cauchy, shrinking circle k by e^(−γ|k|) and moving none: the
broad form stays, the fine circles fade first, the height as level of detail. Or each term can be the circle seen from a
standpoint stepped toward where the detail is: the Takenaka–Malmquist terms, chosen one at a time to take the most of what
is left (adaptive Fourier decomposition; Qian and Wang 2011). On an outline with one dent, the best 85 circles draw it to
a part in a thousand; eleven such terms do, every one standing at the dent. On a broad outline the even circles win, ten
against nineteen. The radii drawn are places about the centre; the overall size a₀ is in none of the terms. **Checked**
(EPI).

## 6. Across: places

**Parallax is the passage from a read to a place.** One standpoint gives directions and a frame, and no size: every
ghost of the room, twice as far and twice as large, gives the same readings. A second standpoint adds the step between
the two. Each point, matched in both looks, is two rays crossing, and its place comes out of the crossing, in the step's
length. More standpoints give every place seen. This is how an observer reconstructs the shape of the writer's cube,
in its own stride; the cube in metres needs the stride counted in metres, a write (§7).

**Parallax is a sum of reads.** Put two standpoints a step B apart and let each read a point in its h/v chart along the
step, cot a from one end and cot b from the other. Then cot a + cot b is the step over the point's distance from the
step's line: the depth is the reciprocal of a sum of two reads. Those are the two operations the Cauchy is closed under,
the sum (a relay, points m + iγ adding) and the reciprocal (the exchange), so parallax never takes a read out of the
family. If each read is uncertain as a read from a height γ is, and the two errors are independent, each is a Cauchy
point w = (c + iγ)/(1 − iγc) in that chart, c its true value (a law written as one complex number, location plus i times
scale, as McCullagh 1992 does), and the depth is exactly a Cauchy whose point is the same triangulation done on the two
points: D = B/conj(w_a + w_b), at every γ, not only for small errors; rays that do not meet ahead are part of the law, as
negative depths. At the pair's corner, the circle on the step, the depth's point stays at the true distance d, turned by
twice the read's error angle: D = d·e^(2i·atan γ). Two things leave the family. The place across the line of sight,
−1 + 2·cot a/(cot a + cot b) in half-steps, has a density over each standpoint that is infinite, where a Cauchy's never
is. And when each standpoint reads only a quarter turn, the sum of two half-Cauchys has density (4/π²)·s near zero, so
the depth's tail falls as 1/d³, not 1/d², and that depth has a mean. Repeating the reads, the mean of the reciprocal
depths gains nothing, while their median narrows. The step is the one length in it, and in thumbs or strides the depth
is a place. **Checked** (PXS).

**Turning teaches the directions; walking teaches the world.** A standpoint has two motions, a turn about itself and a
step along a line. A turn moves every direction by the same angle, near and far alike: it gives the frame, the corner and
the Cauchy of the fingers, the same in every world. A step is the first motion whose effect depends on the world: near
things cross the fingers faster than far ones. Any motion of a standpoint is a turn and a step together (a turn about any
point but the standpoint carries it along a chord), and only the step's part places anything.

**Motion, from reads.** A thing coming toward the reader is read at its edge: x, the thing's breadth against its
distance, the reading v/h of the line to its edge. One read holds one x; that x grows joins two reads. The reading over
its rate of growth, x/ẋ, is the time until the thing arrives if it keeps coming as it comes: the breadth, the distance
and the speed all drop out. Lee (1976) proposed that a driver braking uses exactly this: brake so that the time to
contact shrinks no faster than half a tick a tick, τ̇ ≥ −½, and the car stops at the thing, since at τ̇ = −½ the distance
it needs to stop is the distance it has. Sorted: τ counted in the reader's own ticks, and τ̇, ticks per tick, are places,
unmoved by scaling or by any change of clock, and held by no single read; τ in seconds is a write. One stream cannot tell
a thing coming nearer from a thing growing where it stands; a neighbour at the same depth, read at once, tells them apart,
approach moving both readings and growth one. A speed in metres a second is a write twice over. **Classical** (Lee);
the sorting is ours.

**Walking to the mountain.** Hold the thumb out at arm's length, H against the arm L, and walk toward a mountain whose
breadth V\* and distance d are unknown. The thumb never changes; each read is the finger the mountain's edge touches,
[h : v]. The writer's account of which finger, v/h = (V\*/d)/(H/L), uses amounts no read holds. A read is one place, now:
"one in eight of the thumb". Nearer compares two reads, so "getting nearer" is a place, not a read. Laid in order: far off
the mountain is one in eight of the thumb, then one in four, one in two; per halving of the distance the turn taken in is
greatest where the mountain fills the thumb and fades on either side. One read has the mountain exactly covering the
thumb: the corner, which needs nothing walked: "now the mountain is my thumb", while V\*, d and the corner's distance
d_c = V\*·L/H stay unknown. Past it the two sides mirror each other: d and d_c²/d read as reciprocals. Laid in order the
reads climb toward the horizon, [0 : 1], and no read meets it; the walk arrives because the walk is a count of strides and
ends, and at the foot the reader has one more read, its feet. A steady pace makes τ̇ = −1, past Lee's −½, arriving at
speed; easing so that it holds at −½ stops at the foot. The strides from the corner to the foot are d_c, so counting them
gives V\* = (strides from the corner) × H/L: a place, in the walker's stride; in metres once the stride is carried in, a
write. Scale the world, the walker's stride with it, and nothing along the walk moves: no read, no count of strides; only
the metre carried in.

**The mountain's own corner.** The walk has a second corner, with no thumb in it. Stand on the mountain's centreline and
read each edge against the line to its middle: half the breadth over the distance, s = (V\*/2)/d. Squared and divided by
its own length it is Z = (1 + is)/(1 − is), rational in the read: no angle, no π and no e are needed to have it. Far off
s ≈ 0 and Z ≈ 1: that end of the walk is home. Where the half-breadth equals the distance, s = 1 and Z = i: the edges a
quarter turn apart, the mountain's own corner. At the foot s grows without end and Z goes to −1: the horizon. So walking to
a mountain is walking from home toward the horizon, and the two corners are far apart: the thumb's at d_c = V\*·L/H
(thirty breadths off for a thumb of 2 cm at 60 cm), the mountain's own at half a breadth, sixty times nearer.

Laid in order, the reads take in the turn at two paces. Counted in ratios, every halving of the distance, the span grows
most about the mountain's corner and alike either side: from eight half-breadths off to an eighth of one, 14°, 28°, 53°,
90°, 127°, 152°, 166°, the gains 14°, 25°, 37°, 37°, 25°, 14°. Per unit of x = ln(V\*/2d) the turn taken in is sech x, the
distance heat of §5 with the half-breadth as the thumb. Counted in distance walked, ℓ, with dℓ = −dd, it is
dα/dℓ = V\*/((V\*/2)² + d²), the Cauchy in distance, least far off and most at the foot. One turn, two measures: from the
corner to the foot either gathers π/2, from home to the foot π. Neither is the breadth. Strides from the mountain's corner
to the foot are V\*/2 in the walker's stride, since the read there is 1. They agree only at a corner, where a read is 1 and
a length walked and a ratio held say the same. Joined, the reads telescope: the product of Z_(j+1)/Z_j along the walk is
Z_N/Z_0, the first and last reads alone; every finite walk ends at its last read, and only the writer's limiting completion
tends to −1. The writer names each point Z = e^(iα), α the span, and the end e^(iπ) = −1 (§9): the formula describes the
end and drives nothing. **Checked** (the breath note's §5, at 30 digits; `approach.html`).

**Places come by degrees.** The crossing from reads to places, and from places to writes, is not a switch thrown.
- *In what.* Two standpoints a step apart give every place in that step. If the step was one thumb, places are in thumbs
  and V is placed as V\*/H. Only a step counted in an agreed unit gives an amount, a write, the one rung scaling the world
  moves.
- *How well.* The place's error per unit of angular error is least when the thing sits at the pair's corner, half the
  baseline equal to the distance. With k = d/(B/2) and ε the smallest step in direction the reader tells apart, the
  fractional error in the distance, and so in V\*/H, is ε·cosh(ln k) = ε·(k + 1/k)/2: ε at the corner, about ε·d/B far
  off, the same at k and 1/k. It reaches 1, and the thing is a direction alone, near d = B/ε. In the worked example (§10)
  one thumb walked toward a range ten thumbs off puts it at k = 20, an error 10.025 times ε.
- *Of which things.* One observer, from the same two standpoints, places near things and not far ones. Placing belongs to
  a thing at its distance, not to the observer.

More standpoints and longer baselines narrow the band; nothing closes it. The writer who holds every amount exactly is the
limit of the passage, not a stage of it, as π is the limit of its approximants. **Classical.**

**The thing itself as H.** The thumb can be set to the very thing whose size is wanted. *As the unit*: the thing is drawn
at one length, its V is 1 by choice, and everything else is placed in its units; its two ends become the baseline and the
reader is the point placed, at 1/(2·tan(α/2)) of its breadth from its middle, α the turn between its ends, from one look.
*As the focus*: the reader keeps its thumb and chooses a baseline that puts the thing at parallax's corner, half the
baseline equal to the distance, where the error is least; that needs the distance roughly first, so it is done in passes.

**A tower of places.** Ratios suffice for a great deal. A tower of places, each storey placed against the next, holds a
building, its rooms and their things, with one amount at the top if metres are wanted. Along a chain the gaps add, so the
middle lengths drop out and the ends survive; a loop's gaps sum to zero, and what does not is the error, which a loop shows
and cannot place. Laid across the plane, places are gaps, and composing them is adding gaps: N places hold all
N(N − 1)/2 ratios between them, a slide rule, straight across and circular up, with nothing computed. **Reading**;
`slide-rule.html` shows it.

**Turns, counts and corners.** A read's turns are continuous: between two directions it passes through every one between,
so a read never turns sharply. A corner, a change of direction at one place, is met only by walking a line and stopping
there, a count.
- *A count made to hold a turn rings.* A finite count of even waves, asked to hold a sharp change, overshoots on both
  sides by about 9% of a jump however many waves are used, the ripples only crowding nearer (Wilbraham 1848, Gibbs 1899).
  The overshoot belongs to the representation, not to the edge; physical ringing is a dynamics.
- *Written down, the two cost differently.* An outline can be written as numbers at even places of one turn (Fourier
  coefficients, radii at even angles, points at even shares of its length) or as a walk along it (Bézier pieces, a list of
  points, a turtle's steps). On 73 outlines from a shape library, each written to within half a percent of its size, every
  even-turn form was shorter as text than every walk on the smooth outlines, and every walk shorter on the outlines with
  corners. Rounding the corners of a square, a triangle, a star and an arrow took the even samples from two to three times
  a Bézier path's length to between a half and three quarters of it. Across the library the even samples' length followed
  how fast the outline turns (Spearman ρ 0.85) more than how many corners it has (0.55); the Bézier path's followed its
  corners (0.59) and not its turning at all (0.00). **Checked** (TXT, with the predictions that failed recorded).
- *π and e are where a count tries to hold a turn* (§9).

## 7. The zero: writes

**The unit carried in.** A write ties the across axis's zero to something outside the world: a metre bar, a second, an
agreed notch. Every place hung from the same thumb is then an amount, all at once, by one number: the thumb in metres.
Scaling the world moves that number and every amount with it, and moves no place. The foot, the cubit and at last the
metre were each one observer's body or object made into a public notch. Two observers that see one thing in common need
no unit between them: the ratio of their thumbs is a place, read off what they share. A unit is needed between observers
who share nothing in view. **Reading.**

**A survey.** Snellius (1617) and Roy (1784–85) wrote whole countries this way: thousands of directions read, each
written down in degrees by the instrument, one base walked and counted. The directions are reads; with the base as the
thumb, every side of every triangle is a place; the base counted in a unit is the one write, and every side is then in
the base's unit. A second base checks the first and adds no scale. **Classical.**

**What a blueprint adds.** A reader builds with reads and places and never needs a unit, until one of these is wanted:
1. the size, an amount;
2. meeting out of view, with another observer with nothing in view in common;
3. sums of amounts, which no ratio supplies;
4. the join, the facings put together into a closed circle or sphere;
5. the thing before the thing, a plan for what is not yet there;
6. completeness, stated rather than hoped for;
7. a far field kept in proportion, common to readers whose corners differ (the number line has no corner, so readers
   whose thumbs differ can share it).

Each is a capability, not a condition. A blueprint adds them. Nothing here is against the writer or the number line: they
hold what no standpoint holds.

**Write once, then read again.** A write is over once made: the stride counted, the number put down, the blueprint
drawn. To be used it must be read: someone stands somewhere and looks at it, at marks on a page in their directions and
ratios, as at anything else that arrives. A blueprint in a drawer does nothing until it is looked at; a survey's base,
once counted, is read against by every angle that follows; a drawing of a known room, rendered from a standpoint, is a
write turned back into a read. So the passage runs both ways: reads become places through standpoints, places become
writes through a unit, and every write, once made, joins what is read.

**Recovered, by placing.** An observer can recover a thing exactly, its shape, its places, even its size in its stride,
and still partially. A loop that closes shows that the routes taken agree; it cannot show that no route remains untaken.
Completeness is never a read. What recovers the thing is not reading harder but the passage through standpoints.

## 8. In space

**Three parties.** With a third party, V₂, the reader turns two ways: up from the horizontal (altitude) and round it
(azimuth), the horizon coordinates of astronomy. Its directions fill one octant, the *wedge*: [h : v : v₂], two numbers
a direction. The uniform measure over the octant's area is uniform in azimuth and in height (Archimedes' hat-box;
Lambert's equal-area map), and its law in the readings (v/h, v₂/h), the two tangent readings on a screen square to h, is
the two-dimensional Cauchy, 2/(π(1 + a² + b²)^(3/2)). Every pair of parties is at its own corner, half its readings on
each side; the near field in both readings is a third. The triple corner, h = v = v₂, sits at azimuth 45° and altitude
35.26°, not at either sweep's 45°. **Classical.**

**Two hands.** In space the window is held with both hands. One spreads its fingers from flat to upright, the altitude;
the other round the horizontal, the azimuth. The thumbs cross at a right angle, and where they cross is the triple
corner. Each pane lines up with a crossing, one finger of each hand: the reading is the pair, a direction of the wedge.
Each hand alone gives the one-dimensional Cauchy with its own corner; the crossings together give the two-dimensional
Cauchy. For every crossing to hold the same share, the round hand spreads its fingers evenly by turn and the upright hand
evenly in height, not in angle; spread both evenly by angle and the pair neither hand reads leaves its corner. Two hands
add no second length. The picture is not about hands: it shows that the reader's three dimensions are not Cartesian, no
three axes of amounts, but one thumb crossed with itself and two sweeps from where it is held. The Cartesian frame is
the writer's cube.

**One thumb, two thumbs, three.** In the plane the reader holds one thumb square to the line of sight, one reading, v
against h. In space it holds two thumbs crossed at a right angle, both square to the line of sight: one reads up, v
against h, the other across, v₂ against h. Both are the one H, so what a writer would write as V = V₂ = H is the two thumbs
being the same size, and the right angle between them is a quarter turn, unmoved by scaling. Counted from a standpoint,
the dimension is the number of thumbs square to the look. Held with the look along h, the middle of the cross reads
(0, 0), home for both pairs, as the middle of a camera's screen is, and the triple corner lies 54.74° off the look. To put
the corner under the crosshairs the look turns onto the diagonal, and then every party is a thumb at the same angle to
it: two at 45° in the plane, three at 54.74° in space. The three pairs' corners are three planes through the eye that
meet in one line only, so that look is the only one that puts the crosshair at the corner of all three. **Checked**
(THM).

**The wedge is the writer's; the reader has the horizon's heat map.** The wedge, an octant of directions with faces,
edges and a triple corner, is the writer's description of the read, drawn whole from outside. What the reader has is the
heat over every direction in front, out to the horizon. The heat is the look's, not the thumbs': hottest wherever the look
points; looked down the thumbs' diagonal, where they cross, [1 : 1 : 1], every pair at its corner. Laid on a screen square
to one thumb instead, as the wedge's law is in v/h and v₂/h, the same directions are hottest along that thumb, at home;
nothing moved but the screen. As the reader turns, the heat map turns with the look, without a seam: perfect wherever it
looks, because it is wherever it looks.

**The read's heat covers the hemisphere.** One read's heat covers the hemisphere in front, nothing smaller. Projected
from the eye onto a screen square to the look, directions spread evenly over the hemisphere land as the two-dimensional
Cauchy, 1/(2π(1 + r²)^(3/2)) per unit of screen at r thumbs off the look: the look its peak, rings of equal area its rings
of equal share, and the rim, 90° off, its long tail, never landing. Each pair of thumbs' quarter turn, from its home to its
horizon, is a part of it, the wedge's triangle, 35.26° off at a home and 54.74° at a thumb. The sphere, behind as well as
in front, is the head turned all the way round, other facings joined, the writer's.

**The sphere without V, and the cone of one read.** H, V and V₂ held as amounts combine into the writer's sphere (an
ellipsoid unless written equal); H, H and H, one thumb crossed with itself, into the reader's Cauchy. With V unknown only
the ratios (v/h, v₂/h) are kept, and two things go: the sign (a point and its opposite give the same ratios, so the sphere
folds onto the projective plane) and the closing (the great circle square to the look lands at infinity, the horizon).
The sphere's even measure lands on the screen as the two-dimensional Cauchy, each reading twice. Likewise a single read
with V known is the wedge with its cap, an octant of the ball; with V unknown the cap goes and what is left is the cone,
three flat faces meeting at the eye, open. A cone is the one kind of shape that scaling about its apex carries onto
itself, which is why the read is unmoved by scaling; the cap was where the scale lived. Cut by a screen one thumb out, the
cone shows the quadrant with 2/(π(1 + s² + s₂²)^(3/2)) square to h, or the triangle with the corner at its middle down
the diagonal; cut elsewhere, the same law at another size, which is why H only zooms. In the plane: a quarter disc with
its arc when V is known, a right angle with no arc when it is not.

| shape | what is kept | kind |
|---|---|---|
| the sphere | H and V, every sign: all relations, closed | the writer's, with amounts |
| the Cauchy plane (the full round of the look) | V dropped: opposite points one, the horizon at infinity | the relations without V |
| the cone of one read (the quarter turn) | V dropped and no relation negative: every pair from home (0) to its horizon (∞) | the read |

The cone is the writer's name for what one read holds; the reader has only a vantage.

**Setting H sets the near-field sphere, the writer's.** Choosing the thumb is, in the writer's account, choosing the near
field as a ball of radius H about the standpoint, every facing joined. The reader has the same choice as a mark on every
direction it reads, nearer than one thumb or past it: no surface, no facings joined. Inversion in the sphere at H carries
the far field point for point onto the near field, infinity to the eye, which is why each holds half of every direction's
distance heat. Its filling is the read's heat: along each ray the half-Cauchy in distance, 2H/(π(H² + d²)); across
directions cos³α off the look.

**A cube of dots, read from one of them.** Lay a writer's box of dots one unit apart, 12 a side, stand at one dot and
look at another, and colour every dot by the read's heat, cos³α × sech(ln(d/H)), the thumb set on the dot looked at
(`heat-cube.html`). The cube never changes, only its colours, and only when the look does. Choosing what to look at is
choosing the thumb. The two fields are equal in room, not in count: from a corner of the box looking at its middle, 436
dots are nearer than one thumb and 1,291 farther, but laid as the read lays distance, (2/π)·arctan(d/H), each field has
half the room. The hot core is small: inside 37.5° lies about a fifth of the directions in front. The box has a last dot,
so along the look the dots stop short of the horizon: the box closes, the heat runs on.

**The shape is swept, not each thumb.** Within the quarter turn the even read does not come from sweeping each thumb
through its own angle. Sweep them that way, evenly and one after the other, and the directions pile toward the thumb the
first sweep turns about: v falls below h for 0.343 of the readings, not a half, and the near field is 0.233, not a third;
in the other order the pile goes to another thumb. Swept together, the three thumbs fill the wedge evenly by area: every
pair at its corner, the near field a third, no order. A writer holding every turn of space finds the same law on the
octant as the one measure left alone by turns (Haar), any turns composing to one about one axis (Euler). In the plane the
two ways are the same. Any linear map of the thumbs' space, a projective map of the screen, carries the even read to an
elliptical Cauchy, its standpoint five numbers in space against the plane's m + iγ; only turns keep it round. **Checked**
(SWP).

**The writer's cube, and the sphere as the writer's picture.** The writer's frame with three parties is Descartes's: X,
Y, Z, three number lines, every point three amounts. It reaches the reader's directions only with H and the angles:
X = H·cos a·cos ψ, and so on. Every direction about a point at radius H is a sphere, drawn by the writer. Placed together,
the corner of the reader's wedge points at the vertex of the writer's cube. With the cube outside the sphere, touching it
at the ends of the axes, the picture is the inscribed sweep's; with the cube inside, its far corner on the sphere, the
central sweep's (Thales' circle through home, the ends and the far corner). The hemisphere's 2 and ½, like π/2 and 2/π,
are the writer's measure.

**What survives in space, and what does not.** In the plane one law plays four parts: the image of the uniform turn under
a Möbius map, harmonic measure, the powers of the standpoint, and the two sweeps' rates. On the sphere they part into
three laws: harmonic measure keeps the powers of the standpoint and its mean; the spherical Cauchy, the uniform turn pushed
through a boost, keeps the Möbius maps; neither is the other's image. A quarter turn about one axis and then another ends
120° away from the same two in the other order. What survives is the split between direction and payload, heat and paint,
the corners and the wedge seen from home: both tests still sort every quantity, and every pair of thumbs still has its
corner at the median, since those need only the exchange of two shares, not commuting turns. **Checked** (EUL).

**Three loops.** Undo each of two motions in turn and see what is left. These are compositions, joinings, so each loop
is the writer's account of motions, not a read.
- *A turn and a scaling.* Up by a turn, across by a scaling, down, back. On the plane the loop closes, the two slides
  commuting; in space it closes too, since a scaling by one factor commutes with every turn. A scaling anywhere in a loop
  changes only the loop's overall size.
- *Two turns about different axes.* A turn α about one axis, β about another at angle φ, each undone: the loop comes home
  turned by Ω with cos(Ω/2) = 1 − 2·sin²(α/2)·sin²(β/2)·sin²φ, about αβ·sin φ when small (1.741° at 10° and 10°, against
  α·β = 1.745°), about the axis square to both; bounded however often repeated. This is the sphere of directions' own
  leftover, holonomy; in the plane the same loop leaves nothing.
- *A turn and an unequal stretch.* A turn α with a stretch that scales one axis by c and leaves the other (two axes drawn
  at V = cH): the loop's net map has eigenvalues e^(±ζ), cosh ζ = 1 + 2·sin²α·sinh²(½ ln c), about |α·ln c| when small,
  the same at c and 1/c. It is a squeeze of rapidity ζ up to a turn (its largest stretch is somewhat more: at α = 0.3,
  c = 2, 0.220 against ζ = 0.209), and repeated n times it is nζ. It closes only at c = 1.

So a loop of a turn and a scaling comes home unchanged exactly when the scaling is in one length; the one-length circle is
what a closed loop looks like to the writer. **Checked** (BRL; the trace reading of ζ checked 10 Nov).

**Two boosts joined.** Along one axis two boosts share their fixed points, the stars straight ahead and behind, and each
is a slide of the same pseudorapidity ξ, so their rapidities add and the velocity law, (β₁ + β₂)/(1 + β₁β₂), is the
writer's tanh of the sum. Along two axes no single coordinate carries both slides, and the join leaves a turn: the
Thomas–Wigner rotation, tan(Ω/2) = ab·sin φ/(1 + ab·cos φ), a and b the tangents of the half rapidities and φ the angle
between them, the area of the velocity triangle in hyperbolic space. It is read from directions alone: three stars before
and after fix the map of the sky, and its turn is the rotation, from any three stars, with no frequency and no distance.
No single boost has any; the turn belongs to the join, a place. For a small loop it is ε²·sin φ, the size of the two-turn
loop's leftover, about the opposite axis: curvature −1 against +1. At the next order they part: the turn loop's
correction is −ε²/12 at every angle, the boost loop's (1/3 + cos φ/4)·ε². The split does not derive the Lorentz group:
it enters with the premise that a change of standpoint by motion keeps the angles between nearby stars, so that every such
map of the sky is a Möbius map (Liouville). **Checked** (TWG, to 10⁻⁵⁸); classical (Thomas 1926, Wigner 1939).

## 9. Which numbers belong to whom

**Rates, not angles.** A carpenter calls a roof "six in twelve", a road sign says "10%", a ramp is built "one in
twelve". None says an angle. The pitch is a ratio, had at once; the degrees are a share of the whole turn, and to state
one you must hold the whole turn first. A rate is of something per something: the *per* is the sweep's, a direction,
read; the *of* is the payload. The Cauchy is the law of the per against itself, the turn's speed through the readings with
no payload in it.

**The writer's measures of the sweep.** The angle is arc per radius, measured against the completed turn: the writer's
rate is 1. A hand swept from horizontal to vertical can pivot two ways. From the centre of the circle on the chord (the
*central* sweep), it turns twice as far as its direction does, arc over chord θ/sin θ running from 1 to π/2 at the far
end. From home on the circle (the *inscribed* sweep), chord over arc sin θ/θ runs from 1 to 2/π, approached at the
horizon. Their product is 1 at every θ. These are the only two standpoints from which equal turns cut equal arcs (Euclid
III.20). So a writer measures the sweep at π/2 or 2/π, never at 1; 1 is had only by joining both. π/2 and 2/π are the
writer's measure of the reader's sweeps, not numbers the reader holds. At the corner three things coincide: v fills as
fast as h empties; v/h = 1; and 1 is the geometric mean of π/2 and 2/π, the fixed point of the reciprocal that exchanges
the sweeps. The running rates there are 1.1107 and 0.9003, not 1. **Classical**; the assignment is a reading.

**Tangent addition is the reader's; tan and arctan the writer's.** Evaluating tan or arctan converts between a direction
and an angle, a share of the whole turn. The reader composes directions by tangent addition, (a ⊕ b) = (a + b)/(1 − ab),
ratios to ratios; turns a reading over, s to 1/s; and orders readings. That is enough. Trigonometry as a whole is the
writer's tool: it counts the places read and closes the turn, both of its signs held at once.

**Two 1's.** On the axes the three ways to measure a direction of the square agree: the largest component (the cube's),
the sum h + v (the diamond's) and the length √(h² + v²) (the circle's) all give 1. At the corner they part: 1, 2 and √2.
A 1 needs a measure; the turn picks the round one, and √2 is the geometric mean of the other two (Hölder:
‖x‖₂² ≤ ‖x‖₁‖x‖∞, with equality on the axes and the corner's diagonals). **Classical.**

**One length, counted, makes the rationals.** From H alone, counting thumbs, taking twice a thumb or half a thumb and
ratios of thumbs to thumbs give rational multiples of H: places. A pure read holds directions and their order; its
operations (the reciprocal, tangent addition, the order) take directions to directions and keep a rational direction
rational. The corner is 1, met whole.

**Two lengths make square roots.** √2 first appears as the diagonal of a square, the length of [1 : 1]: Pythagoras
combines two independent lengths through their squares, which needs two axes held at once. Bisecting a direction is of
this kind: the reading halfway to s is (√(1 + s²) − 1)/s. Halving a length is the reader's; halving a turn is the
writer's. Square roots, nested as deep as one likes, are what two lengths and a straight edge and compass give, not every
algebraic number (the cube root of 2 is beyond them; Wantzel 1837). **Classical.**

**A limit makes the transcendental numbers.** The algebraic numbers are closed under every finite operation, so a number
that is not algebraic is reached as a value only through a limit, by one for whom that infinity is finished; as a
definition it can be finite and exact, and it may have a short name (tan 1, or π = 4·arctan 1). The reader meets the
direction tan 1 whole; only stating it as a number needs the limit.
- *π completes the turn.* The reader meets the corner as s = 1, exactly. Its angle is π/4 = 1 − 1/3 + 1/5 − … (Madhava,
  Gregory, Leibniz), every partial sum a fraction. Machin's identity shows the split with no rounding: the direction 1/5
  composed with itself four times by tangent addition is 120/119, and 120/119 taken back by 1/239 by tangent subtraction
  ((a − b)/(1 + ab)) is exactly 1, the corner: finite, rational and the reader's. π comes next, from the arctangent's
  series. Viète's product shows it from the other side: 2/π a product of nested square roots, the whole only in the limit.
- *e completes the scale.* The reader reads a far thing as a ratio, one in eight; counted in thumbs, 8 thumbs out, past
  two, four and eight, it is a place. That count as a continuous quantity is the logarithm, and to give it a value is to
  choose a unit and finish a series: one stretch where the reading halves is ln 2 = 1 − 1/2 + 1/3 − … nats. e itself is
  Bernoulli's limit, (1 + 1/n)ⁿ, or 1 + 1 + 1/2! + 1/3! + …, every term a fraction.

**Euler's formula as a count of reads.** The two limits are one construction on two axes. Cut a turn into n equal reads,
each [1 : θ/n], and compose them by tangent addition: in complex numbers, (1 + iθ/n)ⁿ, exact at every n and rational
whenever θ/n is. As n grows it becomes e^(iθ), by the same limit that takes (1 + 1/n)ⁿ to e: one compounds along the
thumb, the other square to it, both missing their limit by the leading term −w²/(2n), w = 1 or iθ. At every finite n the
count falls short of the angle, exactly by θ − n·arctan(θ/n), θ³/(3n²) to leading order, and stretches the length by
(1 + θ²/n²)^(n/2), θ²/(2n) to leading order, which no reading sees. A thousand reads of π/1000 land at −1.005, on their way
to e^(iπ) = −1. In space, alternating small steps about two thumbs leaves a turn of order 1/n,
(θ₁θ₂/2)·sin(φ/2)/(φ/2) for a whole turn φ; in the plane none. **Classical** (Euler 1748; Trotter 1959); **checked**
(ELM); the reading (each finite count a read, the limit the writer's) is ours.

**The Cauchy's constant, from the same turn.** The quotient that took the length away, w = (1 + is)/(1 − is), does more,
in three exact steps. For every real s, |w| = 1: w = (1 − s² + 2is)/(1 + s²), both parts rational for rational s. With
s = tan θ, w = e^(2iθ). Following the logarithm continuously as s runs on from 0, (1/2i)·d(ln w)/ds = 1/(1 + s²): the
kernel is the rate at which the arc turns per unit of reading. From home to the horizon ln w gathers iπ, so
∫₀^∞ ds/(1 + s²) = π/2, and the half-Cauchy's 2/π is one over that gathered arc; over the whole line w goes once round
and the total is π, the standard Cauchy's 1/π. The constant comes from the identity, the logarithm and the change of
variable together, and enters in no single read, only in the completed total. Composing reads multiplies their w's,
(1 + ia)(1 + ib) = (1 − ab) + i(a + b), tangent addition, closed among complex numbers with rational parts. **Classical**
(Cayley 1846; the residue theorem); where the constant enters is the reading.

**One pole, the constant and the phasor.** Put the standpoint anywhere, z = m + iγ, γ > 0; its kernel
(1/π)·γ/((s − m)² + γ²) has one pole above the line, at z. Weight it by e^(its), t ≥ 0, close the line through the upper
half-plane, and the residue at z is all that is left: e^(izt) = e^(imt − γt). For t < 0 the line closes below, round the
mirror pole at z̄, and together e^(imt − γ|t|). At t = 0 the phasor is 1, the normalized total (π for the unnormalized
kernel). This unity is the Cauchy's alone among familiar kernels: a double pole (Student's t with three degrees of
freedom) gives (1 + t)·e^(−t), not a phasor; two simple poles beat; the hyperbolic secant's endless poles give a series
that does not total term by term; the Gaussian and Laplace kernels have no point off the line at all. Here t is the
transform's variable, dual to position on the line, not time. **Checked** (OPL, to 25 digits at z = 0.7 + 0.4i,
t = 1.3); classical by uniqueness of the transform; that the one pole is the standpoint is our reading.

**What the one pole already carried.** The reader at i holds the standard Cauchy (§3). Readings added give one Cauchy
with the standpoints added, z₁ + z₂, the phasors multiplying. Parallax is a sum of reads whose depth is exactly Cauchy,
its point the triangulation of the two reads' points (§6). A cell of the floor's discarded fraction sits at its own
m + iγ, half its Cauchy in the cell (DYH). Each was reached from its own question; the residue is why each could carry z
and nothing else. A demonstrated unity for the Cauchy and its Poisson kernel, not a principle for kernels in general.

**Met, not made.** None of this keeps irrational or transcendental numbers out of the reader's world. A direction whose
reading is tan 1 is a direction like any other, painted, passed, ordered; the decimal 1.5574… is the writer's account of
where it is. The reader meets these numbers and does not make them.

## 10. A worked example: the mountain and the thumb

Hold up a thumb, one mile wide in the writer's units, and look at a mountain range twenty miles wide, ten miles off.

**From the standpoint.** The range's ends sit at ±45°: the pair (half-width, distance) is at its corner. Of thirty-six
fingers spread evenly over the half turn, eighteen land on the range. Scale the world by a thousand and nothing in the
view moves: still 45°, still eighteen fingers.

**Mountain equals thumb.** With no V, drawing the range at its own H reads it one thumb wide at half a thumb away: the
writer's circle, V = H. Every amount is then off by V\*/H = 20, the same on both sides of the corner.

**The two sweeps, measured.** On the circle drawn about the thumb, the writer measures the central sweep at π/2 and the
inscribed at 2/π; to the range's ends, 1.1107 and 0.9003. Their product is 1, the starting length returned, H in H. The
mountain never enters.

**Walk one thumb.** Step one thumb toward the range and read again. The half-angle's reading goes from s = 1 to
s′ = 10/9. The distance is d = H·s′/(s′ − s) = 10 thumbs and the range V = 2·s·d = 20 thumbs: places, exactly. Count the
thumb in miles and they are 10 miles and 20 miles: writes.

**The mountain as H** (§6, "The thing itself as H"). As the unit, its ends 90° across put the reader half a range-width
from its middle, from one look; as the focus, a baseline of twenty miles puts it at parallax's corner, where one thumb
walked has about ten times the least error.

**In three dimensions: a tower and two thumbs.** Hold both thumbs crossed, one reading up (v/h), one across (v₂/h), the
look along h, so the middle of the cross reads (0, 0) as a camera's screen does, and look at a tower off to one side. Its
top reads (¼, ⅓), its foot (0, ⅓). From one place that is all: two directions, no distance, and a tower twice as large
twice as far off reads the same. Step one thumb across and read again: the top reads (¼, ¼), the foot (0, ¼). Only the
across thumb moved, by 1/12, so the distance along the look is 12 thumbs; the top is 12·⅓ = 4 thumbs across and 12·¼ = 3
up; the tower is 3 thumbs tall, 12 off and 4 to the side: places, exactly. The up thumb did not move, and that is the gain
of the second thumb: in space each step gives two changes for one unknown, so one is spare and must agree (the epipolar
condition of stereo vision). Take the step for diagonal when it was across, and the up thumb says the step had no up in
it: the misreading is caught. Step one thumb forward instead and both readings grow by the same factor, the top to
(3/11, 4/11), either thumb giving 12. Scale the world, the step with it, and no place changes. Count the thumb as 5 metres
and the tower is 15 metres tall and 60 away: the one write. **Checked** (`runs/two/two_thumbs.py`).

## 11. Cases in data, and what this changes

**What it changes.** No mathematics. It sorts.
- **Every reading is a read, every gap across a place, every amount a write.** A result unmoved by scaling and held by
  one standpoint is a read; unmoved and needing two, a place; moved, a write, which needs an amount carried in.
- **A Cauchy-type quantity is a direction where a turn that lays it can be named, apart from the law's shape.** A fat
  tail alone is no evidence of a turn: a mixture of amounts makes one too.
- **The constants have owners.** π, e, π/2, 2/π, the hemisphere's 2 and ½, the Cauchy's normalizing constant, the
  logarithm's nats and the angle's degrees are the writer's measures of the reader's things; the reader's own versions are
  finite: an order, a ratio, a corner, a composition by tangent addition.
- **The acts move.** An observer reads while it stands and turns, places while it walks and counts, writes when it agrees
  a unit.

**LIGO.** In open data from the two LIGO detectors (Abbott et al. 2023; 512 s, about two million whitened samples each),
each detector's signal taken alone is an amount, and its heavy tail is one loud transient on a law of finite spread: block
means shrink as n^(−½), which nothing Cauchy can do. The Cauchy is in the direction [H1 : L1] of the two read at one
instant: its median at 1, its spread unmoved by averaging, its angle near uniform, and the small departure from uniform
reproduced from each channel alone, by pairing samples 8 s apart, to 0.0001; a prediction written before the data were
fetched, which could have failed. **Checked** (LGO).

**The quasar dipole.** A reader moving through a sky of sources counts more ahead. With no limit on brightness the census
is a count of directions, and its dipole is 2β, Ellis and Baldwin's 2, from the directions alone (1984). A real census is
cut at a brightness, and the cut adds a term set by what arrives. On Secrest et al.'s quasars (2021), per slice the
expected dipole is [2 + x(1 + α)]·β, α the spectral index, the 2 the directions' and x(1 + α) the payload's: 5.3 to 6.6
times β, so the payload carries 60–70% of it. Taken as directions alone, the measured 0.018–0.023 would give a speed nearly
three times too large; with the payload's part divided out, four slices by brightness give one β,
3.3·10⁻³ ± 0.3·10⁻³, 2.7 times the speed from the microwave background, as one motion should. Slices by colour give 2.3,
2.8 and 4.6 times it, which no motion can do, so part of the dipole belongs to what arrives. The sort says which part could
be the reader's, not where the dipole comes from. **Checked** (EBD), and provisional: the residual of 2.7 times the
microwave background's speed rests on the catalogue's selection, the flux cut and the spectral indices, and has not been
reproduced independently; it is a decomposition, not yet an explanation of the discrepancy.

**One photon at a time.** In a double slit the fringes' visibility is at most 2hv, h and v the two paths' shares, and the
which-path predictability |h² − v²| (Greenberger and Yasin 1988; Englert 1996): full visibility only at the corner. On
Aspden, Padgett and Spalding's frames (2016) the slits' counts, 9,026 : 10,465 and 11,993 : 11,891, give 2hv 0.997 and
1.000, and the measured contrast, 0.69 and 0.56, lies under that bound, short by the source. The bound is the shares',
the geometry's; how far below it a pattern falls is what arrives. **Checked** (WVP).

**Berry's phase.** A spin carried slowly round a closed loop of field directions comes back with two phases (Berry
1984). The geometric one is half the solid angle the loop of directions encloses: the same taken twice as slowly, in a
field twice as strong, in an apparatus twice the size. The dynamical one is energy times time and moves with all three.
Experiments have separated them by keeping the loop and changing the rest (Tomita and Chiao 1986; Bitter and Dubbers
1987). Both tests sort it. The half is the central sweep's twice the angle: a spin state at angle θ has its point on the sphere
of states at 2θ. **Classical**; not run here.

**And one where it failed.** Seeds falling from a plant also spread with a fat tail, and the turn can be named
beforehand: a seed leaving its release point straight, every downward direction alike, lands as the hemisphere's Cauchy,
Clark's 2Dt with shape p = ½ and a tail falling as r⁻³. On Bullock et al.'s compiled kernels (2017), the 35 that could be
fitted of 38 picked as wind-dispersed say otherwise: median p 0.10, a tail falling about as r⁻², and no nearer the turn's
than kernels carried by animals. The fat tail there is a mixture over wind speeds: amounts, not a turn. So the reading is
not a rule that every Cauchy-like law is a turn's heat; it holds where the turn is there to be named, and a test written
before the data can show where it is not. **Checked** (TCF; killed).

## 12. Open questions

- **O1. The name "place".** *Closed (R792):* "place" stays, its scope fixed by D3 (a gap across, unmoved by scaling,
  needing two standpoints).
- **O2. The thumb.** *Closed (R792):* the thumb is the across axis's chosen zero, as home is the up axis's, as D5
  already requires; the record's "the read's own length" describes how it is chosen, not a different kind.
- **O3. "The writer's" for joins.** The writer as a vantage holds completed joins (π, the one-length circle, the facings
  joined) as well as amounts. A completed join is unmoved by scaling, so it is not a write; "the writer's" here names a
  vantage. Until a word is chosen, say "a completed join". Whether it deserves its own kind is open.
- **O4. Orders.** *Closed (R792):* an order of reads is its own kind, a joining with no gap in it, not a place; D7 lists
  places and orders side by side.
- **O5. Do readers put the thing looked at on the corner?** A "should" (§5), not a claim about eyes or instruments.
- **O6. A second test that can fail.** "Find the z" has passed once in data (LIGO) and failed once (the seeds). A second
  domain, where the turn can be named before the data, would show whether the rule sorts.
- **O7. The essays, the demos and *Reads and Writes in Physics*.** *Closed (R792):* all three brought to R788's kinds;
  the last place still calling a place a write, the demos page's card for `write.html`, now says the move places.
- **O8. Why the sky is conformal.** The moving sky's Möbius map rests on motion keeping angles on the sky. SRB (runs 1–2)
  replaces that premise by four: a change of standpoint acts on directions alone, chains included; it is fixed by finitely
  many numbers; the turns are among the changes; a motion carries directions from the back toward the front. With Lie's
  classification of the finite groups on a surface, these leave the Möbius maps alone; Newton's aberration fails the
  first, since two of its steps are no single step once the speed is dropped. Two of the four carry the physics: that what
  no read can hold makes no difference to what is read (the light postulate stated for reads), and that a place is a
  finite list of numbers. Neither is shown to follow from reading. A reconstruction, not an explanation.

## Where the ideas come from

Jaynes's principle of transformation groups (1968, 1973) gives the method: the measure an observer's ignorance leaves
unchanged. Poincaré's universe made a thousand times larger overnight (1908), undetectable from inside, is the first test;
his representative and geometric space are close to the reader's and the writer's. Leibniz's space as an order of
coexistences (1715–16) is the reader's picture; Klein's programme (1872), geometry as the study of a group, is the form of
the sort. Gibson's ambient optic array (1979) is the stained-glass window. Bridgman and Buckingham sorted quantities by
scale long before. What is offered here is the three kinds on one plane, the heat of directions and the payload inside a
read, and what carries an observer from one kind to the next.

## Code and data

The checks and measurements cited are in this repository (reportbase/wander), each with its plan written before it was
run; plan codes in the text name them. The one pole, the constant and the phasor: `plans/opl-plan.md`, `runs/opl/`. Two
boosts joined: `plans/twg-plan.md`, `runs/twg/`. Why the sky is conformal: `plans/srb-plan.md`, `runs/srb/`. Time and the Cauchy's point: `plans/tim-plan.md`, `runs/tim/`. The floor's
cells: `plans/dyh-plan.md`, `runs/dyh/`. The Cauchy's routes: `plans/cauchy-routes.md`, `runs/crt/`. Parallax as a sum of
reads: `plans/pxs-plan.md`, `runs/pxs/`. Formats as text: `plans/txt-plan.md`, `runs/txt/`. The tower and two thumbs:
`runs/two/two_thumbs.py`. Three thumbs at the crosshair: `plans/thm-plan.md`, `runs/thm/`. The shape swept:
`plans/swp-plan.md`, `runs/swp/`. Three laws on the sphere: `plans/eul-plan.md`, `runs/eul/`. Euler's formula as a count of
reads: `plans/elm-plan.md`, `runs/elm/`. The three loops: `plans/brl-plan.md`, `runs/brl/`. The distance between
standpoints: `plans/frg-plan.md`, `runs/frg/frg.py`. A flat chart in space: `plans/flc-plan.md`, `runs/flc/`. Epicycles and
aimed terms: `plans/epi-plan.md`, `runs/epi/`. The seed kernels: `plans/tcf-plan.md`, `runs/tcf/`. The data cases:
`plans/lgo-plan.md`, `plans/ebd-plan.md`, `plans/wvp-plan.md`, with `runs/lgo/`, `runs/ebd/`, `runs/wvp/`; each records its
runs as they came out, the killed ones too, and none alone establishes the sort. Pages: `read.html`, `pinhole.html`,
`crosshairs.html`, `heat-cube.html`, `euler.html`, `approach.html`, `slide-rule.html`, `star-field.html`. The read as a
control: reportbase/calendar (`dial.js`, `dome.js`, `horizon.html`, `dome.html`, `dome-map.html`, `dome-instrument.html`).
The mountain walk's two corners and paces: `plans/breath-note.md` §5. The rewrite's map from the record and its checklist:
`plans/rw-rewrite-outline.md`. The known physics sorted by the two tests is the companion *Reads and Writes in Physics*
(`papers/reads-and-writes-physics.md`), drawn from the record and not yet brought to R788.

## References

- Abbott, R. et al. (LIGO, Virgo and KAGRA Collaborations) (2023). Open data from the third observing run of LIGO, Virgo,
  KAGRA and GEO. *Astrophysical Journal Supplement Series* 267, 29.
- Archimedes. *On the Sphere and Cylinder*, Book I.
- Aspden, R. S., Padgett, M. J. and Spalding, G. C. (2016). Video recording true single-photon double-slit interference.
  *American Journal of Physics* 84, 671.
- Bernoulli, J. (1690). *Quæstiones nonnullæ de usuris.* Acta Eruditorum.
- Bernstein, A. J. (1966). Analysis of programs for parallel processing. *IEEE Transactions on Electronic Computers*
  EC-15(5), 757–763.
- Berry, M. V. (1984). Quantal phase factors accompanying adiabatic changes. *Proceedings of the Royal Society of London
  A* 392, 45–57.
- Bitter, T. and Dubbers, D. (1987). Manifestation of Berry's topological phase in neutron spin rotation. *Physical Review
  Letters* 59, 251–254.
- Bridgman, P. W. (1922). *Dimensional Analysis.* Yale University Press.
- Brinkman, T. (2026). *Observation from Somewhere: addresses given, payloads met.* Working paper, archived.
- Bullock, J. M., Mallada González, L., Tamme, R., Götzenberger, L., White, S. M., Pärtel, M. and Hooftman, D. A. P.
  (2017). A synthesis of empirical plant dispersal kernels. *Journal of Ecology* 105(1), 6–19.
- Burn, B. J. (1966). On the depolarization of discrete radio sources by Faraday dispersion. *Monthly Notices of the Royal
  Astronomical Society* 133, 67–83.
- Buckingham, E. (1914). On physically similar systems; illustrations of the use of dimensional equations. *Physical
  Review* 4, 345–376.
- Chyzak, F. and Nielsen, F. (2019). A closed-form formula for the Kullback–Leibler divergence between Cauchy
  distributions. arXiv:1905.10965.
- Clark, J. S., Silman, M., Kern, R., Macklin, E. and HilleRisLambers, J. (1999). Seed dispersal near and far:
  patterns across temperate and tropical forests. *Ecology* 80(5), 1475–1494.
- Cayley, A. (1846). Sur quelques propriétés des déterminants gauches. *Journal für die reine und angewandte
  Mathematik* 32, 119–123.
- Ellis, G. F. R. and Baldwin, J. E. (1984). On the expected anisotropy of radio source counts. *Monthly Notices of the
  Royal Astronomical Society* 206, 377.
- Englert, B.-G. (1996). Fringe visibility and which-way information: an inequality. *Physical Review Letters* 77,
  2154–2157.
- Euclid. *Elements*, Book III, Proposition 20.
- Euler, L. (1748). *Introductio in analysin infinitorum.* Lausanne.
- Euler, L. (1776). Formulae generales pro translatione quacunque corporum rigidorum. *Novi Commentarii Academiae
  Scientiarum Petropolitanae* 20, 189–207.
- Euler, L. (1778). De repraesentatione superficiei sphaericae super plano. *Acta Academiae Scientiarum Imperialis
  Petropolitanae* 1777, I, 107–132.
- Gauss, C. F. (1828). Disquisitiones generales circa superficies curvas. *Commentationes Societatis Regiae Scientiarum
  Gottingensis Recentiores* 6, 99–146.
- Gibbs, J. W. (1899). Fourier's series. *Nature* 59, 606.
- Gibson, J. J. (1979). *The Ecological Approach to Visual Perception.* Houghton Mifflin.
- Greenberger, D. M. and Yasin, A. (1988). Simultaneous wave and particle knowledge in a neutron interferometer.
  *Physics Letters A* 128, 391–394.
- Haar, A. (1933). Der Massbegriff in der Theorie der kontinuierlichen Gruppen. *Annals of Mathematics* 34, 147–169.
- Hölder, O. (1889). Ueber einen Mittelwerthssatz. *Göttinger Nachrichten*, 38–47.
- Jaynes, E. T. (1968). Prior probabilities. *IEEE Transactions on Systems Science and Cybernetics* 4(3), 227–241.
- Jaynes, E. T. (1973). The well-posed problem. *Foundations of Physics* 3, 477–492.
- Kakutani, S. (1944). Two-dimensional Brownian motion and harmonic functions. *Proceedings of the Imperial Academy
  (Tokyo)* 20(10), 706–714.
- Klein, F. (1872). *Vergleichende Betrachtungen über neuere geometrische Forschungen.* Erlangen.
- Lambert, J. H. (1772). *Anmerkungen und Zusätze zur Entwerfung der Land- und Himmelscharten.* In *Beyträge zum
  Gebrauche der Mathematik*, Theil III. Berlin.
- Lee, D. N. (1976). A theory of visual control of braking based on information about time-to-collision. *Perception*
  5, 437–459.
- Leibniz, G. W., and Clarke, S. (1717). *A Collection of Papers … Relating to the Principles of Natural Philosophy and
  Religion.* London.
- Lindemann, F. (1882). Ueber die Zahl π. *Mathematische Annalen* 20, 213–225.
- Liouville, J. (1850). Extension au cas des trois dimensions de la question du tracé géographique. Note VI in
  G. Monge, *Application de l'analyse à la géométrie*, 5th ed., Paris, 609–616.
- Machin, J. (1706), in W. Jones, *Synopsis palmariorum matheseos.* London.
- Malmquist, F. (1926). Sur la détermination d'une classe de fonctions analytiques par leurs valeurs dans un ensemble
  donné de points. *Comptes Rendus du Sixième Congrès des Mathématiciens Scandinaves* (Copenhagen, 1925), 253–259.
- McCullagh, P. (1992). Conditional inference and Cauchy models. *Biometrika* 79, 247–259.
- Mercator, G. (1569). *Nova et aucta orbis terrae descriptio ad usum navigantium emendate accommodata.* Duisburg.
- Poincaré, H. (1902). *La Science et l'hypothèse.* Paris. (1908). *Science et méthode.* Paris.
- Qian, T. and Wang, Y.-B. (2011). Adaptive Fourier series, a variation of greedy algorithm. *Advances in
  Computational Mathematics* 34, 279–293.
- Roy, W. (1785). An account of the measurement of a base on Hounslow-Heath. *Philosophical Transactions* 75, 385–480.
- Secrest, N. J. et al. (2021). A test of the cosmological principle with quasars. *Astrophysical Journal Letters* 908,
  L51.
- Shepard, R. N. (1964). Circularity in judgments of relative pitch. *Journal of the Acoustical Society of America*
  36(12), 2346–2353.
- Snellius, W. (1617). *Eratosthenes Batavus.* Leiden.
- Staudt, K. G. C. von (1847). *Geometrie der Lage.* Nürnberg: Bauer und Raspe.
- Takenaka, S. (1925). On the orthogonal functions and a new formula of interpolation. *Japanese Journal of
  Mathematics* 2, 129–145.
- Thomas, L. H. (1926). The motion of the spinning electron. *Nature* 117, 514.
- Tomita, A. and Chiao, R. Y. (1986). Observation of Berry's topological phase by use of an optical fiber. *Physical
  Review Letters* 57, 937–940.
- Trotter, H. F. (1959). On the product of semi-groups of operators. *Proceedings of the American Mathematical Society*
  10, 545–551.
- Viète, F. (1593). *Variorum de rebus mathematicis responsorum liber VIII.* Tours.
- Wantzel, P. L. (1837). Recherches sur les moyens de reconnaître si un problème de géométrie peut se résoudre avec la
  règle et le compas. *Journal de Mathématiques Pures et Appliquées* 2, 366–372.
- Wigner, E. (1939). On unitary representations of the inhomogeneous Lorentz group. *Annals of Mathematics* 40(1),
  149–204.
- Wilbraham, H. (1848). On a certain periodic function. *Cambridge and Dublin Mathematical Journal* 3, 198–201.

The entries were checked against Crossref and library catalogues on 3 November 2026; Malmquist (1926) is given as it is
usually cited.
