# Reads and Writes

**What can be known from a standpoint, and what it costs to know more**

*Tom Brinkman. Draft, 30 October 2026; retitled 2 November 2026 (it was* Readers and Writers*). Written with AI
assistance (Claude).*

The propositions and proofs this paper draws on are in *Observation from Somewhere*, now archived and kept for
reference; where its wording differs from this paper, this paper stands.

## Abstract

Observation comes in two acts. A *read* is taken from a standpoint, turning there. It needs one length, H (a thumb held
out at arm's length), and what reaches the standpoint along each direction; every reading is a ratio, a direction [h :
v], and no amount survives into it. A *write* holds the whole: both sides of every axis, the extents in amounts, the
completed turn, the unit. Two tests tell them apart. Scale the world, every length multiplied by one factor: a reading
is unchanged, a writing changes. Change what arrives, keeping the standpoint and the turn: the directions stay, the
payload changes. And one quantity tells them apart, V, the other party's breadth: no reading carries it, and every
writing needs it.

The reader's directions are laid by the uniform turn, whose law in the reading v/h is the Cauchy: its median at the
corner v = h, its horizon never reached, no mean. It is best read as a *heat*, a continuous weight over the readings,
hottest along the look and given before anything arrives. What arrives along a direction is the *payload*, the paint,
the world's writing met there. *The heat is given; the paint is met.* So the two acts never race: a read adds nothing,
and a write to the paint moves no direction, so reads agree in whatever order they are taken. Computing has to engineer
that separation with addresses, which are counted and the writer's; here it is given.

The passage from reading to writing is parallax: a second standpoint, the step between them counted, places from the
crossings. An observer making that passage is writing; read and write are acts, not kinds of observer, and the passage
comes by degrees. Underneath is an older line: a read is continuous and a write is a count, and where a count is made to
hold a turn, π and e appear.

None of the mathematics is new. What is offered is a division of it: which parts a standpoint has, which parts need the
whole, and what carries an observer from one to the other.

## 1. Two acts

**Words.** The paper names acts, a *read* and a *write*, not two kinds of observer: one observer reads while it stands
and turns, and writes while it walks, counts, ranges or agrees a unit. *Read*, *reading* and *reader* are used as each
sentence needs (a reader is whatever is reading, for as long as it reads), and likewise *write*, *writing* and *writer*.

Map a room without a ruler. Stand in a corner, look at each thing, and note where it is: so far round, so far up. You now
have every thing's direction and nothing's distance. A room twice as large, seen from the same corner, gives the same
notes; so does a room half as large. What you have is a picture, exact and complete in its own terms, with no size in it.

Now take one step, a stride along the wall, and look again. Each thing's two directions cross, and where they cross is
its place, in strides. The room has a shape and a size now, in your stride. Count the stride in metres, and the room is
in metres.

The first part is reading. The second and third are writing. The rest of this paper is about the line between them.

Put read and write side by side and anyone who has programmed thinks first of a race. In this geometry none arises, and
the reason is the split the paper turns on ("Reads do not conflict", below).

**What a read is.** A read is the set of all sweeps of the thumb in one moment, from one standpoint, *home*. A sweep is
the one length the reader holds, H, turned from all of it lying along h to all of it standing along v; the read is every
such sweep at once, given whole, not performed one after another. H can be any value, since every reading is a ratio and
H only sets the zoom; V, the other party's breadth, is not in it. A reading is one direction met in the sweep, [h : v],
charted as v/h, h and v each a share of the thumb between 0 and 1; it needs no division by the reader, since the
projection from home divides. Each sweep is centred on the crosshairs, the corner where the thumbs cross (§6, §7). The
read is a heat over directions, the Cauchy: hottest along the look, cooling toward the horizon, continuous, with nothing
counted in it (§7). Geometry is free in this sense: nothing in it is computed, no procedure runs, and there is no
tangent or arctangent in it; tan, arctan and every formula for the turn are the writer's way of stating what is already
there. How finely a reader tells directions apart, and the near and far fields the thumb lays over the read, are §6's.

**Reads are unconnected.** A read holds no time: time is the step between reads. Reads are continuous, one can be taken
at any place and any moment, but each has no connection to the one before; their order, and anything said across them,
is a write. Two reads, at two moments or two standpoints, are joined only across a step that is counted: parallax, and so
a write. (A *facing* is a writer's word, for several reads held together with their signs; no read is one.) A write can
plant a flag: a mark in the world that says "this is the starting point", from which strides and ticks are counted. Reads
plant no flags. A later read can read the flag, as paint in a direction, against the thumb ("the flag is one in four of a
thumb"), but the read has no notion of how close it is to the flag; how far, and how long since, are the count's.

**Reads do not conflict.** A read gives a direction and the heat over directions; what is written is the payload, the
paint, met along it. A read adds nothing, so reads of one geometry can be taken in any order, or all at once, and they
agree; a conflict needs a write, a mark made where something else reads or writes. In computing this is the condition for
running operations together without a race (Bernstein 1966), and much of the work there goes into keeping reads and
writes from meeting. Here it holds by construction: the geometry is given, nothing writes to it, and a write to the paint
moves no direction and no heat (the second test, below), so it never runs into a read. A system whose addresses move with
their contents (an array that reallocates, a table that rehashes) has to rebuild that separation by hand, with stable
handles or copies kept for the reads.

**A read is geometry, a write is physics.** A write is the recording of a read: a mark kept, discrete where the read was
continuous, which lasts and can be counted and set beside other marks; order, nearness, durations and amounts are all
said of marks. What a mark keeps is the direction the read gave and the paint met there: the heat is the read's, and the
paint recorded is the write. So the two distinctions this paper keeps are one. Picture reality as a sheet of paper.
Every physical thing writes on it, a stone's mass, a planet's path, a cell dividing; physics is that writing, and a life
is a writer that copies its own marks forward. A read adds nothing to the paper. Its directions and their heat are the
geometry laid over it, there whether the paper is blank or full, and the light that arrives along them is the paper's
writing met there. A reader's body is written too, its thumb a mark like any other; but the thumb held out as H is not a
mark, it is the read's own length, which is why no read carries a scale.

There are two geometries here, not one. *Physical geometry* has V: lengths and extents, the writer's cube with a number
line on each axis, the circle stated as x² + y² = r², the blueprint, the stride counted. Every figure in it has a size,
scaling the world moves it, and it is the geometry physics writes in, the marks on the paper with their sizes and
places. *Reader geometry* has no V: directions from one standpoint, shares of one thumb [h : v], the corner, the
horizon, the Cauchy and order. No figure in it has a size, and scaling the world moves nothing in it, not because V
cancels but because V was never there. Classically the line falls where Klein (1872) drew it: the reader's is close to
the geometry of the lines through one point, projective geometry seen from a standpoint (incidence, order, cross ratio,
no length), with a home and a corner of its own; metric geometry is had from it by fixing something more, and here what
is fixed is V, carried in by a write. The scale test sorts the two geometries, and the bridge v·V\*, a share of the
thumb times a breadth carried in, is where a reading crosses from one to the other. So a read is reader geometry, and a
write is physical geometry, where physics is written. This is how the account is held, not a claim about the world: it
says where physics sits in this frame and tells physics nothing it does not already know.

Projective geometry can be reached two ways. Taken as lines through the origin of a plane, with the scale divided out,
it is the writer's route: the box first, the lengths then set aside. Von Staudt's synthetic geometry (1847) reaches it
from incidence and order alone, with no length to set aside. The reader's route is the second kind: the thumb's shares
[h : v] first, V never there, and the box built later, by walking and counting.

Everything else in this paper is built on the read, and on its opposite, a count.

**The write.** A write holds what no standpoint gives: both hemispheres, so both signs of every axis; the extent of each
axis as an amount; the unit those amounts are in; the completed turn. Its frame is a box, a number line on each axis,
every point three amounts. Nothing in it is round, and nothing in it has a corner of a read's kind: the number line is
proportional everywhere, with no place where one unit gives way to another.

**The test.** Multiply every length in the world by k. A reading is unchanged; a writing is multiplied by k (or by a
power of k). This sorts every quantity, and it is the old line of dimensional analysis between the scale-invariant and the
scale-variant (Bridgman 1922; Buckingham 1914). The names *reading* and *writing* say more than the sorting: they name the
act that crosses the line (a function of invariants is invariant, so a writing needs an amount carried in from outside)
and the vantage that holds each.

**The second test.** Change what arrives, keeping the standpoint and the turn: repaint the world, move the light,
replace a wall by a row of trees. The *directions* the turn lays down, and their heat, are unchanged; the *payload*, the
paint found along each, changes. The first test separates reading from writing; the second separates the heat from the
paint. The first is necessary, not sufficient: a probability or a ratio of two amounts is unmoved by scaling and is
still not a direction; the second, with the standpoint and the turn held fixed, is the one that tells a direction from a
payload. They are one split seen two ways: the direction and its heat are what a read holds, and the payload is what is
written on the world where the direction falls. In the writer's notation both splits sit in one line, ln z = ln r + iθ:
scaling slides the real part, a turn the imaginary (§5).

**Continuous and discrete.** The two acts are, in the end, an old distinction under new names. A read is continuous: a
turn passes through every direction between two, none is next to another, and nothing in a turn is counted. A write is a
count: strides along a baseline, units on a ruler, items in a list, digits in a number, each with a next and, in a
finite count, a last. The writer's continuous things, the real line, the circle held whole, π and e, are counts carried
to their limit and held as finished: a ruler subdivided without end, a polygon given ever more sides, interest
compounded ever more often. So there are two continuities. The reader's is never counted; the writer's is a count
completed. Scaling the world leaves a turn as it was and multiplies every count of units; that is the first test seen
from this side. These are the two acts idealized, not their implementations: a sensor that samples, a register that
holds a reading, a machine that rounds it, has already written; the read is what is taken, before anything takes it. No
real instrument is a pure read; the pure read is the limit, and what the paper offers for real instruments is the two
tests, applied quantity by quantity. The rest of the paper keeps returning to this line, in the corner and the horizon,
in which numbers belong to whom, in K and N, and in the passage from one act to the other (§8, "Turns, counts and
corners").

**V.** One quantity sits on the line between the two acts: V, the breadth of the other party, the mountain in the
distance that the thumb is held up against. A reading is a ratio of the thumb's own shares, [h : v]; V was never in it,
so no reading carries it. It is not missing from a read; it was never there. To have V is to have written: walked a
baseline, counted a step, timed a pulse, or agreed a unit. A reader that comes to know V has not read better; it has
written. This is not a shortcoming of the reader. Its geometry is a read of directions with no breadth in it: the
horizon, the corner as a median and the absence of any mean are what such a read is.

## 2. What the reader has for free

**The thumbs pointed.** The reader has no circle. It points its crossed thumbs at the mountain, and that pointing
generates its own geometry: the corner where the thumbs cross, the fingers spread from it, near and far read as ratios
of the thumb. What the reader holds is H, its thumb; never V, the mountain. A writer watching would say that a length
held fixed and turned about one end traces a circle, and would call that circle V = H, the writer's way of saying that
the two axes of its drawing are drawn at one length: the thumb equal to the mountain. We call it the *one-length
circle*. It is the writer's, held whole, with a circumference and an area. The reader does not draw it, set it or choose
it; it points, and has the turn.

**A vantage, not a shape.** Circles and spheres are the writer's tools. Two points give the writer a line, the segment
between them walked and counted; a circle on them, or a sphere, is that line's whole turn held at once, which only a
writer holds. A reader has a vantage, not a shape: a standpoint and the turn from it, in the plane and in space alike.
It can walk the shape, round it or along it, and in walking it becomes a writer (§8).

**The uniform turn.** The reader's directions are laid by turning, and a turn measured by itself is uniform: equal
turns, equal shares. Nothing the reader does produces the directions; they are given by the geometry before anything
arrives, and how they crowd, read in the ratio, is their heat. In the reading s = v/h the uniform turn over a quarter
turn has the law

  (2/π) · 1/(1 + s²),  s ≥ 0,

the half-Cauchy. Its median is s = 1, the *corner*, where v = h. Its quartiles are √2 − 1 and √2 + 1. Its far end, s =
∞, the direction [0 : 1], is the *horizon*, reached by no finite reading. It has no mean: averages of readings climb
without settling, by (2/π)·ln 10 for every tenfold further the readings run. Given the uniform turn, these facts hold
whatever is looked at: a straight wall, a row of trees, a curved hill, an empty sky. The wall's shape only decides where
each direction meets it.

The constant 2/π and the quartiles' values are the writer's arithmetic for this law; what the reader has of it is the
order of its readings, the corner, and the directions themselves.

**Heat and paint.** A direction from home, with its heat, is the read's; a payload, the paint, is what arrives along it.
They share one thing, the point where a direction meets the world. The world decides what meets each direction, which
thing is nearest and what it sends back; nothing it does moves a direction or its heat. Scale the world and nothing
moves. Change the world and nothing moves. Change the turn's standpoint and the directions move, as a family: the Cauchy
is carried into another Cauchy, its centre and width the new standpoint's foot and height (m + iγ). This closure, under
the real Möbius maps of the reading (the changes of standpoint and of chart), is the law's own; not every operation on
directions keeps it, and an amount entering, an edge, a square, a sum of amounts, breaks it.

So the Cauchy here is not a law of what is measured. It is the law of the uniform turn, the heat over the reader's
directions. The reading is of the Cauchy this construction makes. A Cauchy met elsewhere, a resonance's line, a ratio of
two normal amounts, a stable sum, may have another origin; whether a turn lies behind it is a question to ask of each
case, not a consequence of this derivation.

**The Cauchy's routes.** Every Cauchy is one measure: the Poisson kernel of the upper half-plane seen from a point
z = m + iγ, p(x) = (1/π)·Im 1/(x − z). In other words, the harmonic measure of a line seen from a point off it. Many
mechanisms put a point at z and reach the line from it:
- **a uniform turn read on the line**: the lighthouse, the ratio of any rotation-invariant pair, a circle seen from a
  point of it;
- **a random walk** leaving the half-plane from z (Kakutani 1944), and its twin, a normal mixed over the walk's hitting
  time;
- **a pole** a height γ off the line, whose response squared is the kernel and whose Fourier pair is the damped
  oscillation e^(imt − γ|t|);
- **a sum** of Cauchys, whose points add;
- **a real Möbius map**, which carries one point to another.

In the plane these are one measure, because a turn about z preserves harmonic measure. On a flat boundary they agree in
every dimension. On a curved one they part: inside a ball, the straight turn and the walk land differently. One sample
never tells the routes apart. Only what γ tracks can (a distance for the turn and the walk, a rate for a pole, a sum for
a sum), and the boundary's shape. So the turn does not own the Cauchy. It is the reader's route to it, the one that makes
the heat over the reader's directions. "Find the turn" is, more generally, "find the z": what puts a point off the line,
and how the line is reached from it. A fat tail with no z, as in the seed kernels of §11, is not harmonic measure by any
route.

**The Cauchy, derived from H and from V.** The Cauchy is usually met as a family with two parameters, a location m and a
scale γ. Derived from what an observer holds, it comes in three forms, and the parameters arrive with V.

- *From one length.* Turn one length H, the thumb, uniformly. Its tip is at (H cos θ, H sin θ), and the reading v/h =
  tan θ divides H out. The share of a quarter turn passed before the reading reaches s is, in the writer's account,
  (2/π)·arctan s: the standard half-Cauchy, scale 1, median at the corner. No V appears anywhere, and H appears only in
  the tip's place, never in the law. The scale is 1 not because anything was set equal to anything, but because the
  reading is a ratio, and a ratio carries no scale.
- *From two axes.* Draw the second axis at a length V of its own. The drawn point is (H cos θ, V sin θ), its reading
  (V/H)·tan θ, and the law a Cauchy of scale c = V/H, its median at c, off the corner unless c = 1. Scaling the world
  leaves c unchanged, so c is not an amount; but it needs two lengths held against each other, as √2 needs the square's
  two sides, and holding both is the writer's.
- *From a line in the world.* A lamp turning uniformly lights a shore at distance d; its landings x = m + d·tan θ follow
  C(m, d), its quartiles at m ± d. Both parameters are amounts, moved by scaling the world. The angles follow the
  uniform turn whatever d is: nothing in the directions carries d. The scale appears only when the landings are measured
  on a ruler laid along the shore, which needs the shore found and walked.

The same three come from the ratio of two normal amounts: equal spreads, and the spread cancels (the first form); unequal
spreads σ₁ and σ₂, and the scale is σ₁/σ₂ (the second); means away from zero, and a location appears (the third).

| form | what is held | scale | location | whose |
|---|---|---|---|---|
| one length turned | H | 1 | 0 (the corner) | the reader's |
| two axes drawn | H and V | V/H | 0 | the writer's ratio |
| a line in the world | the line's place, in amounts | d | m | the writer's amounts |

So V enters the Cauchy as its scale, and only there; the location is where the line lies relative to the standpoint. The
point m + iγ that indexes the family is the standpoint's place with respect to the line. The reader's ignorance is turns
and rescalings, never translations, since a situated reader cannot step outside its own place: in its own chart it stands
at i, foot 0 and height 1, and holds the standard Cauchy. Moving the standpoint is walking; two standpoints differ by an
amount, and that difference is what parallax uses (§8). The reader has the law's shape; the writer adds its parameters.

**The circle's equation, divided by its own length.** Set the writer's circle beside the reader's Cauchy and the second is
the first with its lengths divided out.

The writer's circle holds amounts. A point is x = H cos θ, y = V sin θ; the curve is (x/H)² + (y/V)² = 1, round only
when V = H, the thumb equal to the mountain, and then x² + y² = r² with r an amount. It states the area πHV, the
circumference and every point's place, and all of them move when the world is scaled.

Divide the round circle by x²:

  1 + s² = (r/x)² = sec²θ,  s = y/x.

The ratio r/x of two amounts is not an amount, and no length is left. Two things follow. The density is the share
squared: 1/(1 + s²) = (x/r)² = h², the reader's own share of its thumb, squared. And the even turn becomes the Cauchy:
ds = sec²θ·dθ, so dθ = ds/(1 + s²), and the uniform turn, read as s, is (2/π)·1/(1 + s²). The Cauchy is the circle's
equation used to carry an even turn into readings. It has scale 1 because a reading holds only shares of one thumb: no
amount was ever in it, and no V was set equal to H. (The division above is the writer's account of the circle, not
something the read does.)

| | the writer's circle (with V) | the reader's Cauchy (without V) |
|---|---|---|
| a point, a reading | (x, y) = (H cos θ, V sin θ), amounts | s = tan θ, a ratio |
| the equation | (x/H)² + (y/V)² = 1 | 1 + s² = sec²θ |
| the law | none needed: every point is stated | (2/π)/(1 + s²) = (2/π)·h² |
| lengths in it | H and V | none |
| what it states | the area πHV, the circumference, places | the median 1, the quartiles √2 ∓ 1, the horizon, no mean |
| if V ≠ H | an ellipse | a Cauchy of scale V/H |
| the world scaled | everything moves | nothing moves |

The writer's circle states the lengths; the reader's Cauchy is that circle's equation with the lengths divided out, and V
comes back into it only as the scale, for whoever holds V.

**Why there is no mean: the Cauchy is the heat of directions.** The Cauchy has a median and no mean. Over a quarter turn
the readings s = v/h up to S average (1/π)·ln(1 + S²) divided by the share they cover, and that climbs without limit, by
(2/π)·ln 10 ≈ 1.47 for every tenfold further the readings run. This is usually told as a defect of the law. Read as the
heat of directions, it is what such a heat should do.

A mean is a sum of amounts divided by their count. The Cauchy weighs directions, and a direction, read as a direction,
has no length to add; its numerical representation is a chart, and the question is what survives a change of chart. To
average the readings v/h is to treat each direction as an amount laid along a line, the chart in which the horizon sits
at s = ∞, and the sum picks up that chart's far end. A mean belongs to the chart that takes a direction for an amount,
not to the directions; they never had one. Other charts of the same directions do have means (the bounded chart s/(1 +
s) averages ½), and the order statistics do not depend on the chart at all: the median and the quartiles are the same
directions however the readings are written, because they commute with every increasing map of the reading, and a mean
does not. So the median is a property of the directions and the mean is not; asking for the mean of a Cauchy is asking a
direction for something only an amount has.

A mean of directions can be had, by a writer. Take each direction as a unit vector and add: over the uniform quarter
turn the average of (cos θ, sin θ) is (2/π)(1, 1), pointing at the corner, of length 2√2/π ≈ 0.900. The direction it
gives is the corner, the median again; its length is the writer's measure, π and all. And a writer holding a finite
world, capped at an extent M, has a Cauchy with a mean, (1/π)·ln(1 + M²) over the share below M, about 8.8 at M = 10⁶:
finite, and set by the extent, an amount that moves when the world is scaled. The mean appears only once an extent is
written in, and its value is set by that extent, not equal to it.

The payload has means where it is an amount: the light along each direction, its colour, its brightness, all add. The
lighthouse's landings on the shore lack a mean although they are written in a unit, because they are still the turn's
directions, carried onto the shore's ruler; the light that lands there is the payload, and it averages. What arrives can
be averaged; where it arrives cannot. Practice already takes the median of a Cauchy and never its mean: this is the
reason.

**The payload is not lost.** The separation spends nothing of the payload: no part of it goes into making the directions
or their heat, so all of it arrives, along directions given before it came. The Cauchy then gives it back in four ways.
Each is exact in the ideal model, with the heat known and the payload given whole; from finite, noisy samples each is an
estimate, and undoing the blur is the least stable of the four.

- *By its ratios.* Two payloads read against each other make a ratio, and a ratio is a reading. The light along one
  direction over the light along another, one colour channel over another, the radius in one direction over the radius
  in another: each is a direction [p₁ : p₂] in the payload's own space, read exactly as a direction is read, unchanged
  when the world is scaled. A shape about a centre, ln r = a₀ + f(θ) (the real part of the writer's ln z = ln r + iθ
  taken as a function of the turn, §5), comes back this way whole: every mode of f from ratios of radii, exactly. Two
  detectors' signals read against each other are a direction too, and where the signals are like noise that direction
  follows a Cauchy: the payload read as a ratio is a direction again. The payload arrived written, as marks; read
  against itself it gives directions in its own space, so recovering it this way is a write read again. What the ratios
  leave out is one number, the payload's overall scale a₀, and that number is V again. Radio astronomy reads
  polarization this way: a source's intrinsic polarization angle, from the ratio of its Stokes U to Q, is a reading of
  the payload, unchanged by scale, while the Faraday rotation that turns it on the way, RM·λ², carries the rotation
  measure in radians per square metre and so is a writing (Burn 1966).
- *By dividing the heat out.* What is counted along the directions is the heat times the payload's own
  weight, ρ(θ)·2/(π(1 + s²)). The heat is known before anything arrives, so dividing by it leaves the payload's
  distribution exactly, up to its total: the astronomer's flat field, importance sampling's 1/p. The median direction of
  what arrives is then the payload's median, at the corner only when the payload weighs alike on both sides.
- *By undoing the blur.* Seen from a height γ, the payload arrives smoothed by the Cauchy kernel, whose Fourier
  transform e^(−γ|k|) is never zero. Every mode survives, damped and not destroyed, and comes back multiplied by
  e^(γ|k|), noise with it. A box blur, the floor's, has a transform with zeros, and the modes there are gone for good.
  How fine a mode comes back is set by the resolution and the noise, which is how finely the reader draws, not loss:
  unique in principle is not the same as stable.
- *By averaging it.* The payload is amounts, and amounts have means: weighted by the known heat, the light
  across the turn totals exactly wherever that total is finite, which is the payload's to say. The mean was never
  missing from the payload, only from the directions.

What the payload carries along its direction all comes back; its scale and its distance are V, and come back only by
writing. A known measure can be divided out and an invertible blur undone; a floor that discards cannot.

**The reader never sees a shape.** This is about what one read determines, from one standpoint with nothing written; not
about what a visual system infers. A thing is, to that read, the directions it paints; the paint is the world's writing,
met there. Its shape is a radius along each direction from its own centre, an amount, and amounts are removed before
reading: no shape in amounts. Every way to a shape is a writing: ranging, a counted step, a blueprint. This is not a
shortfall to be made up by inference. The reader's side is whole; the shape was never the reader's to lack.

**Passive.** The reader sends nothing. It is not a radar. A ranging instrument carries in the signal's speed and a clock,
two amounts, and so it writes.

## 3. Five pictures

Five pictures carry most of what the earlier sections say. Each shows what the reader has, what the writer adds, and where
V enters.

**The hand.** Hold up a hand, thumb out. The thumb is H: the one length the reader holds, its size chosen, setting only
the zoom. The fingers, spread from flat to upright, are the directions. The reader does nothing to lay them; wherever
the hand is held, the geometry gives the same fingers spread the same way, evenly by turn, and read as v/h they follow
the Cauchy, half below the corner. The light that falls along each finger is the payload, the world's writing met on the
fingers; the fingers stay geometry, there with or without it. The light paints the fingers and changes with what is in
front of them, and no finger carries how far that light came. The hand moves two ways, raised from the ground toward the
vertical and turned round the horizontal, and the two are the altitude and the azimuth of §7. Hold the thumb up against
a mountain range, and the range spans so many fingers; with no V the reader draws the mountain at the thumb's own size,
and every amount it then reads is off by the one number it lacks, V/H. To learn that number it must walk (§10).

**Two hands.** In space the window is held with both hands. One hand spreads its fingers from flat to upright, the
altitude; the other spreads its fingers round the horizontal, the azimuth. The two thumbs cross at a right angle (§7),
and where they cross is the corner, the triple corner of the wedge, where both read 1. Each pane of the window now lines
up with a crossing, one finger of each hand: the reading is the pair of fingers, a direction of the wedge, (v/h, v₂/h).
Each hand alone gives its own sweep, the one-dimensional Cauchy with its own corner; the crossings together give the
two-dimensional Cauchy. For every crossing to hold the same share of the window, the round hand spreads its fingers
evenly by turn and the upright hand evenly in height, not in angle (Archimedes' hat-box, Lambert's map); spread both
evenly by angle and the pair neither hand reads leaves its corner. The coloured light at each crossing is the payload,
as before, and still no colour carries a distance, and two hands add no second length (§7).

No one holds a window this way; the picture is not about hands. What it shows is that the reader's space in three
dimensions is not Cartesian. There are no three axes of amounts, no X, Y and Z counted out from an origin: there is one
thumb, crossed with itself, and two sweeps of fingers from where it is held. Everything else, the corner, the near and far
fields, the Cauchy over the crossings, follows from the thumb. The writer's cube (below) is the Cartesian frame, and it is
the writer's.

**The lighthouse.** A lamp turns evenly and throws a flash along each direction. Where a flash lands on a straight
shore, the landing x obeys (x − α)/β = tan θ, with α the foot of the lamp on the shore and β its distance from it. The
angles are the lamp's directions, laid evenly by its turn, whatever shore there is; the landings follow a Cauchy because
the shore is straight. Within each flash the path to the shore cancels: the angle carries no distance. The lamp's own
corner is the flash halfway through the quarter turn, and it lands at the foot plus one distance, the shore's corner,
only if the shore is measured at the sea's own scale; drawn on a ruler c times the sea's, the halfway flash lands at
arctan c, and the corner slides off. To read β from the landings, take half the spread between the quartiles; never the
mean, which the landings do not have. That reading is a writer's: it needs the shore found and a ruler laid along it.
The lamp is the reader, its turn the directions; the shore is the writer's line, where V comes in as the scale.

**Mercator's map.** A navigator wants a straight line on the chart to be a constant compass bearing. On a chart whose
parallels are spaced so that a degree of latitude is drawn c times a degree of longitude at that latitude, a bearing ψ
is drawn at tan ψ′ = tan ψ/c. Bearings are true everywhere only at c = 1: both directions drawn at one length at every
place, which is Mercator's chart (1569). It keeps every direction and pays in area, stretched by sec² of the latitude,
so Greenland is drawn about as large as Africa, which is some fourteen times its area. The chart that keeps areas
instead draws c = cos² of the latitude and gives up the bearings. Neither is wrong; each keeps what it was made to keep,
and only the globe, the writer's whole, keeps both. Mercator's map is also not the reader's picture. It is a chart of
the whole field, every stretch where the reading halves alike, with no focus; the reader's picture is the turn,
proportional in direction and finest where it looks. Bearings are the reader's; areas are amounts, and the writer's.

**A moving sky.** An observer moving through a field of stars at a fraction β of the speed of light sees each star
change in two ways, and special relativity already writes them as two formulas. Where the star is seen moves:
aberration, cos θ′ = (cos θ + β)/(1 + β cos θ), the same at every frequency. On the stereographic chart of the sky it is
z ↦ z/k, with k = e^η and η the rapidity, a Möbius map of the directions; it moves directions and carries the Cauchy's
family onto itself. A sky uniform in the stars' own frame is seen as the spherical Cauchy, its density D²/4π. (The sky's
own uniform heat, on the stereographic chart, is (1/π)·dA/(1 + |z|²)², which is not the plane's two-dimensional Cauchy:
that one, (1/2π)(1 + r²)^(−3/2), is half the sky on a flat screen square to the look, the cos³ of §7. Only the circle's
stereographic image is a Cauchy. No law on the sky is unchanged by boosts; the uniform one is unchanged by turns, and
boosts carry it within its family.) What arrives at each place changes: the Doppler factor D = √(1 − β²)/(1 − β cos θ′)
scales each photon's energy and its rate of arrival, a weighting of the payload that moves no direction. For a sky
uniform in its own frame, counting total power, the familiar D⁴ brightening ahead is D² of directions crowding, the
heat, and D² of payload. Laid on ξ = −ln tan(θ/2) (the pseudorapidity), aberration is a slide by η, so a reader holding
directions alone reads its own rapidity, with no clock, no frequency and no speed of light carried in, provided every
source is counted whatever its brightness and the sources are uniform in their own frame. That is a reading. To state
the speed in metres a second needs the speed of light carried in, and to read D as the shift of a spectral line needs
the line's rest frequency, a known kind of atom: both are writings. The theory makes the split in its formulas without
naming it; the reader's part is the directions, the writer's the amounts.

## 4. Rates, not angles

A carpenter calls a roof "six in twelve". A road sign says "10%". A ramp is built "one in twelve". None of them says an
angle. The pitch is a ratio, had at once with a level and a tape; the degrees are a share of the whole turn, and to state
one you must hold the whole turn first.

**A rate is of something per something.** The *per* is the sweep's: a direction, read. The *of* is the payload: what
arrives there. A rate lays a write over a read: the per is read, the of is written. The Cauchy is the law of the per
against itself: a speed of the turn through the readings, with no payload in it.

**The writer's rate is 1.** The angle is arc per radius, measured against the completed turn; the chord between home and
the far end of a quarter turn is held as a straight line of length 1. That is the writer's rate.

**The reader's sweeps, as the writer measures them.** A hand swept from horizontal to vertical can pivot two ways. From
the centre of the circle on the chord (the *central* sweep), the hand turns twice as far as its direction does; arc over
chord θ/sin θ runs from 1 to π/2 as the sweep reaches the far end. From home on the circle (the *inscribed* sweep), the
ratio chord over arc sin θ/θ runs from 1 to 2/π, approached at the horizon and never reached. Their product is 1 at
every θ. These are the only two standpoints from which equal turns cut equal arcs (Euclid III.20: the inscribed angle is
half the central). So a writer measures the sweep from horizontal to vertical at π/2 or 2/π, never at 1; 1 is had only by joining
both, which is the writer's join. Euclid's theorem, the two reciprocal ratios and the writer's rate of 1 in radians are
three things that correspond here, not one theorem. And π/2 and 2/π are the writer's measure of the reader's sweeps, not
numbers the reader holds: π is the total of a completed half turn, the period of a line's direction (2π that of an
oriented turn).

**The corner, where three meet.** At v = h three things coincide: v fills as fast as h empties; the reading v/h is 1, the
writer's 1; and 1 is the geometric mean of π/2 and 2/π, the fixed point of the reciprocal that exchanges the two sweeps.
The running rates there are 1.1107 and 0.9003, not 1. The corner is a meeting, not a rate.

**Tangent and arctangent are the writer's tools.** They convert between a direction and an angle, a share of the whole
turn. The reader never needs them. It composes directions by tangent addition,

  (a ⊕ b) = (a + b)/(1 − ab),

which takes ratios to ratios; it turns a reading over, s to 1/s; it orders readings. That is enough for everything a
reader does. The algebra of the tangent is the reader's; evaluating tan or arctan at an angle is the writer's.

**Two 1's.** On the axes, the three ways to measure a direction of the square agree: the largest component (the cube's),
the sum h + v (the diamond's) and the length √(h² + v²) (the circle's) all give 1. At the corner they part: 1, 2 and √2.
A 1 needs a measure. The writer cannot choose the measure by fiat; the turn picks the round one, and √2 is the geometric
mean of the other two (Hölder: ‖x‖₂² ≤ ‖x‖₁‖x‖∞, with equality on the axes and the corner's diagonals).

## 5. Which numbers belong to whom

**One length, counted, makes the rationals.** From H alone, counting thumbs, taking twice a thumb or half a thumb and
taking ratios of thumbs to thumbs give rational multiples of H and nothing else. Counting is not a pure read: it is done
in parallax, where a step is counted, and in writing. A pure read holds directions and their order; its operations on
them, the reciprocal, tangent addition and the order, take directions to directions, and keep a rational direction
rational once one has been counted. The corner is 1, met whole. This is the arithmetic of the first count, and it is
enough.

**Two lengths make square roots.** √2 first appears as the diagonal of a square, the length of [1 : 1]: Pythagoras
combines two independent lengths through their squares, which needs two axes held at once. This is where the Greeks met
incommensurability. On one line, from one unit, it never happens. Bisecting a direction is of this kind: the reading
halfway to s is (√(1 + s²) − 1)/s, a square root of two lengths combined. Halving a length is the reader's; halving a
turn is the writer's. Square roots, nested as deep as one likes, are what two lengths and a straight edge and compass
give: not every algebraic number (the cube root of 2, which doubles a cube, is beyond them; Wantzel 1837).

**A limit makes the transcendental numbers.** The algebraic numbers are closed under every finite operation: add,
subtract, multiply, divide or take roots of them, any finite number of times, and the result is algebraic. So a number
that is not algebraic is reached by no finite algebraic step, and its value as a decimal or a fraction is had only
through a limit, by one for whom that infinity is finished; as a definition it can be finite and exact. It may still
have a short name (tan 1, or π = 4·arctan 1); the reader meets the direction tan 1 whole, and only stating it as a
number needs the limit.

- *π completes the turn.* The reader meets the corner as s = 1, exactly. Its angle is π/4 = 1 − 1/3 + 1/5 − … (Madhava,
  Gregory, Leibniz), every partial sum a fraction, none of them π/4. Machin's identity shows the split with no rounding:
  the direction 1/5 composed with itself four times, by tangent addition, is 120/119, and 120/119 taken back by 1/239,
  by tangent subtraction ((a − b)/(1 + ab), not a − b), is exactly 1, the corner. That much is finite, rational and the
  reader's. The number π comes next, from the arctangent's series. Viète's product shows it from the other side: 2/π is
  a product of nested square roots, each algebraic, the whole only in the limit.
- *e completes the scale.* The reader reads a far thing as a ratio, one in eight. Counted in thumbs, by a writer, the
  same thing is 8 thumbs away, past two, four and eight, exactly.
  That count as a continuous quantity is the logarithm, and to give it a value is to choose a unit and finish a series:
  one stretch, where the reading halves, is ln 2 = 1 − 1/2 + 1/3 − … nats. e itself is Bernoulli's limit, a coin lent at a
  hundred per cent compounded ever more often, (1 + 1/n)ⁿ, or 1 + 1 + 1/2! + 1/3! + …: every term a fraction, the number
  only at the end.

**Euler's formula as a count of reads.** The two limits are one construction on two axes. Cut a turn into n equal reads,
each [1 : θ/n], and compose them by tangent addition: in complex numbers that is (1 + iθ/n)ⁿ, exact at every n and
rational whenever θ/n is. As n grows it becomes e^(iθ), Euler's formula, by the same limit that takes Bernoulli's (1 +
1/n)ⁿ to e: one compounds along the thumb, the other square to it, and both miss their limit by the same leading term,
−w²/(2n), with w = 1 or w = iθ. At every finite n the count falls short of the angle, each step's tangent running out
past its arc: exactly by θ − n·arctan(θ/n), which is θ³/(3n²) − θ⁵/(5n⁴) + …, so θ³/(3n²) to leading order; and it
stretches the length by (1 + θ²/n²)^(n/2), θ²/(2n) to leading order, which no reading sees, since [h : v] divides the
length out at every step. The limit, the writer's, repairs the angle and returns the length to 1; a thousand reads of
π/1000 land at −1.005, on their way to e^(iπ) = −1. From a standpoint z = m + iγ the same limit, (1 + izt/n)ⁿ, lands on
e^(izt) = e^(imt − γt) for t ≥ 0, the Cauchy's own characteristic function: the foot m turns, and the height γ damps
along the real axis, an amount rather than a read. And the construction is the plane's. In space, where turns do not
commute, alternating small steps about the two thumbs leaves a turn of order 1/n, (θ₁θ₂/2)·sin(φ/2)/(φ/2) for a whole
turn φ; in the plane it leaves none. All of this is classical (Euler 1748; the Lie–Trotter product formula, Trotter
1959); what is ours is the reading: each finite count a read, the limit a write, exact only where the turns commute. So
Euler's formula sorts like everything else here: the turn it describes is read, and the number it is written in is a
count completed.

The reader's two ignorances, after Jaynes (1968), are which way it faces and how large things are: turns and rescalings.
Each is a one-parameter group with an exponential map. Turns close, so their map has a period: 2π for an oriented turn,
π for the direction of a line, which comes back to itself after a half turn (the projective line the reader's readings
live on). Rescalings never close, so their map has no period, only a base, e. π is what is needed to say that the turn
comes back; e, to say how the scale goes on. The complex logarithm puts them in one line, ln z = ln r + iθ: the scale on
the real part, measured in e's unit, the turn on the imaginary part, measured against π, a line's period. They meet at
e^(iπ) = −1, which is where the doubling (h + iv)² = e^(2iθ) sends the far end of the reader's sweep, the horizon the
reader holds as the finite pair [0 : 1] (the horizon itself is a quarter turn, e^(iπ/2) = i). It was through that
meeting that Lindemann proved π transcendental (1882): a power of e with a nonzero algebraic exponent is never
algebraic, and e^(iπ) is −1.

**π with the direction, e with the payload.** The two parts of ln z = ln r + iθ are the two sides of this paper. The
imaginary part is the direction: turns act on it alone. The real part is the payload's size: scaling the world acts on
it alone, sliding ln r and leaving θ where it was. So, in this paper's reading of the period and the base, π belongs
with the direction and e with the payload, and they are not alike. The direction coordinate closes, so it has a period,
and π (a line's half turn; 2π an oriented turn) is that period in the unit the exponential sets; nothing can choose it
away. The payload coordinate is an open line with no total and no natural size, so nothing on it marks a place; its base
is a convention (counting in thumbs, doublings serve as well), and e is the base that lets one unit serve both
coordinates, so that e^(iθ) is a turn of θ and e^t growth at a rate of one. That open line is why the reader never reads
a₀, the overall size (the a₀ of a shape's ln r = a₀ + f(θ), §2): there is no mark on it to read against. One coordinate
closed and its constant forced, one open and its constant chosen: the asymmetry of direction and payload, in two
numbers. Both numbers are still the writer's; the reader meets the closing and the openness, and states neither.

**Met, not made.** None of this keeps irrational or transcendental numbers out of the reader's world. A direction whose
reading is tan 1 is a direction like any other, painted, passed, ordered. The reader holds it as a pair and by its
order; the decimal 1.5574… is the writer's account of where it is. The reader meets these numbers and does not make
them.

## 6. Near and far

**The crosshairs.** Cross the thumbs (§7) over whatever is looked at, the look running down their diagonal. Where they
cross is the corner: the thing there reads one thumb along each thumb, every pair alike, v/h = v₂/h = 1, and it is drawn
one thumb wide. Along the line of sight it lies √2 thumbs off in the plane and √3 in space, the diagonal of a square or a
cube one thumb on a side; no thumb lies along the line of sight. That crossing, with H, lays the near field and the far
field over the read, as an overlay: the Cauchy itself has neither (§7, "The hemisphere is the shape"). Along every
direction one thumb splits the heat in distance in half, whatever H is.

The near field is a single thumb, laid evenly: everything nearer than the crossing gets its heat in proportion, the first
half of the thumb as much as the second. The far field is read in ratios: a thing one thumb wide reads one in two, then
one in four, then one in eight, and two far things are related by the ratio of their readings ("one in eight is half of
one in four"), the same at every scale. Each stretch over which the reading halves holds the same heat as the one
before, out toward the horizon: the far field's self-similarity, read with nothing counted. To count the stretches,
"8 thumbs out, three stretches past the corner", is the writer's, and so is giving the count a value: 1 + ln(d/H), with a
base chosen (§5), or 2 − H/d on a lay that keeps all of reality within two thumbs. The logarithm is the writer's number
for what the reader reads as a ratio. There is one corner, the split between the near field and the first stretch; past
it the stretches are plain, with no corner of their own. Move the crosshairs onto something else and the corner, and
with it the split between near and far, goes with them.

**The one-thumb circle, and the three corners.** Everything within one thumb of the crosshair's point is a ball (a disc in
the plane) that touches each face of the wedge, at the cube's corners one thumb back from the crosshair along each thumb.
From the eye its outline is a circle 35.26° about the look, the largest about the crosshair inside the wedge, holding
73% of its directions; in the plane the same construction runs ±45°, home to horizon, the whole quarter turn. It never
changes size: whatever is pointed at becomes the corner, so the circle goes with the look. The corner is its centre; home
is on it, at the three points it touches, where one reading is zero. Each pair of thumbs has its own corner, where the two
read alike: a line through the crosshair, the three crossing there 120° apart. Along each, the third thumb runs a whole
quarter turn against the pair, from home on the circle (35.26° off the look) through the corner at the crosshair to the
horizon at that thumb's own direction (54.74° off, the other side). The view down the diagonal is three of the plane's
quarter turns crossed, each with its corner under the crosshair. Inside the circle the directions hold the world with no
distortion at the corner, the pair levels ln(v/h) all zero there and their squares the same in every direction to second
order; moving out each direction's grain holds more, in proportion, as one over twice the reading toward home. That is
compression, not blur: a fixed fineness squeezes more of the world into each grain, it does not make it fuzzy. The
squeeze is not round, hexagonal near the corner and unbounded only at the three homes. It is a precision, not a size:
seen, a thing spans the angle it spans, and laid by turns off the look its place parts from a flat screen's only far out
(tan α/α, 1.10 at 30°, 1.27 at 45°). (Checked exactly; see Code and data.)

**Laid by the heat.** A flat screen does not give each direction the same room: off the look it stretches the
directions as tan α and thins them as cos³α. The screen that does is the one where equal room holds equal shares of the
directions. For
directions taken uniformly, that is Lambert's equal-area map about the look, a direction α off it at radius 2·sin(α/2):
true at the crosshair, off by 0.9% at 15°, 3.4% at 30°, 7.6% at 45°. Laid that way, the tunnel's rings come where the
readings fall: one thumb off the look at 0.765, then one in two, one in four, one in eight at 1.05, 1.23 and 1.32, packing
toward the rim at √2, the horizon. They pack because each stretch holds fewer of the look's directions than the one before
(0.26, 0.20, 0.12 of what is in front, and 0.12 past one in eight); in the plane, with one thumb, they are as many. The
ground has its own reading: a point ρ along it, with the thumb's ground point D away, reads (2/π)·atan(D/ρ), one at the
feet, a half at the thumb, zero at the horizon, so the far ground gathers in rows just under the horizon. Nothing in this
needs to know how much world there is. A world made only where the view reaches, from cells at every scale and kept only
where a thing spans π/(8K) or more, gives the same read, and the reader's work is set by its K whatever the world's N.

**H is a zoom.** The reader's fineness is finite, its resolution K ("K and N", below), which comes before H. H, the
thumb it holds up, decides how K is split. Half of it lies inside H at every H; a small H makes the near ones fine and
puts more of the world past the held edge; a large H does the reverse. No H holds everything. The best H for a thing is
the one that puts it at the corner, where the reader's relative grain is finest. That is why the corner follows the
focus: what is looked at is drawn one thumb wide.

**Drawing a shape: the circles, a height, a step toward the detail.** A closed outline about a centre can be written as
circles on circles, epicycles: its Fourier series, each term a circle turning a whole number of times a lap. Those are
the turns of one standpoint at the centre, evenly. The Cauchy draws with the same circles two ways. Seen from a height
γ, the outline is smoothed by the circle's own Cauchy, the wrapped Cauchy, and that smoothing shrinks circle k by
e^(−γ|k|) and moves none: the broad form stays, the fine circles fade first, which is the height as level of detail. Or
each term can be the circle seen from a standpoint stepped off the centre toward where the detail is: the
Takenaka–Malmquist terms, whose kernel on the outline is the wrapped Cauchy about that place, chosen one at a time to
take the most of what is left (adaptive Fourier decomposition; Qian and Wang 2011). On an outline with one dent, the
best 85 circles draw it to a part in a thousand; eleven such terms do, and every one of them stands at the dent,
stepping nearer the outline as the detail gets finer. On a broad outline with nothing local the even circles win, ten
against nineteen: the centre is the right place to stand when there is nowhere to step toward. This is the corner
following the focus, applied to drawing a shape. The radii drawn are the outline's amounts, and its overall size a₀ is
in none of the terms.

**K and N.** Two letters sort the acts here. N is how many items there are; K is how many are held. To know N is to
know the whole: its extent, V, and how much is in it. That is writing, and only a writer has it. A reader never knows V,
so it never knows N; what it knows is K, its own resolution, fixed before H is chosen.

K has a foot in each act. It is read continuously, as the turn is, a fineness with no last place: the reader's way of
holding it. Laid out as K places at the heat's quantiles, K *addresses*, it is a count, the writer's way of saying how
much the reader holds, and addresses in this paper are always that, discrete, counted and the writer's. As a metaphor
they still serve where they connect the Cauchy to computer science: a direction looked along is like an address looked
up, with the heat under it. So K is the meeting place of the discrete and the continuous here: whatever is out there,
discrete or not, arrives as directions and is read continuously, and saying it comes in so many pieces, of the world or
of the reader's K, is the writer's statement.

The Cauchy is what goes between them. Its heat spreads the reader's K over a world of any size, the near field in
proportion, the far field in ratios (one in two, one in four, one in eight), and, counted as K addresses, everything past
the last on the one address at the horizon. Double N and the reader's view does not change; make N unbounded and it still
does not change (an infinite star field browsed at N and 2N shows the same view, apart by less than 10⁻⁷ at N = 2⁴⁰). So
the Cauchy is a cull: whatever N is, the reader's work is K: an implementation that holds K samples does O(K) work, and
for a fixed K it does not grow with N. What the cull gives up is sameness. A writer who knows N can hold every item as
1/N of the whole, all alike, on a number line with no corner, and no item has an advantage over another, because no
standpoint is favoured: there is none. A reader's K is spent unevenly, finest at the corner and coarser each stretch of
thumbs away, and that unevenness is the vantage: what is looked at gets the most. Knowing N buys equality; holding only K
buys a standpoint, at a cost that does not grow with the world.

## 7. Three parties, the reader's vantage and the writer's cube

With a third party, V₂, the reader turns two ways: up from the horizontal (altitude) and round it (azimuth). These are
the horizon coordinates of astronomy. Its directions fill one octant, the *wedge*: [h : v : v₂], two numbers a
direction. The uniform measure over the octant's area is uniform in azimuth and in height (Archimedes' hat-box;
Lambert's equal-area map), and its law in the readings (v/h, v₂/h), the two tangent readings on a screen square to the
look (not the altitude and the azimuth themselves), is the two-dimensional Cauchy, 2/(π(1 + a² + b²)^(3/2)). Every pair
of parties is at its own corner, half its readings on each side; the near field in both readings is a third. The triple
corner, h = v = v₂, sits at azimuth 45° and altitude 35.26°, not at either sweep's 45°.

**The wedge is the writer's; the reader has a tunnel.** The wedge, an octant of directions with its faces, its edges and
its triple corner, is the writer's description of the reader's geometry: drawn whole, from outside, at once. The reader
never holds it. What the reader has is what its crossed thumbs give where it looks: a tunnel of heat about the line of
sight. All of it is generated from the thumb; none of it is stored. As the reader sweeps, the tunnel turns with the look,
continuously and without a seam, so whatever it looks at is at the tunnel's centre, where the heat is greatest and the
reading finest, and each direction is exact, given by the geometry, not computed. That is the reader's fidelity: perfect
wherever it looks, because it is wherever it looks. The wedge, the octant and the sphere are what a writer draws to
describe that tunnel from outside.

**The hemisphere is the shape; near and far are an overlay.** One read's tunnel is the hemisphere in front, and that is
the Cauchy's whole shape, nothing smaller. Projected from the eye onto a screen square to the look, the directions spread
evenly over the hemisphere land as the two-dimensional Cauchy, 1/(2π(1 + r²)^(3/2)) per unit of the screen at r thumbs
off the look: one point for one direction, the look its peak, rings of equal area its rings of equal share (half within
60° of the look, √3 thumbs out on the screen), and the rim, 90° off, its long tail, never landing, which is why it has no
mean. Over the wedge alone, a quarter of the screen, the same law reads 2/(π(1 + a² + b²)^(3/2)): each pair of thumbs'
quarter turn, from its home to its horizon, is a part of the hemisphere, the wedge's triangle, 35.26° off at a home and
54.74° at a thumb; the sphere, behind as well as in front, is the head turned all the way round, other facings joined. The
hill, the triangle and the rings are ways of drawing the hemisphere, not shapes of their own. The Cauchy has no near and
no far: no length enters it, and its one marked place is the look. Near and far are a separate overlay, which H lays over
the read (§6): a split of distance. Along every direction the overlay's heat in distance is a half-Cauchy in the
distance's own reading; a writer counting it as K places puts them at d/H = tan(kπ/2K), the first K/2 inside one thumb
and the rest past it, whatever the direction and whatever the size of the thumb. Inside one thumb they are close to even,
in proportion: the near field. Past it the share left beyond x thumbs is (2/π)·arctan(1/x), 0.295 past two thumbs, 0.156
past four, 0.079 past eight, about half of what was left each time the reading halves, out toward a horizon never
reached: the far field, heavy, so no mean of distances. The split is a mark at one thumb on every direction, each one's
median, not a body: a first version drew it as a closed dome and gave the near field a shape, which it does not have. It
stands one thumb out, never at V. Take the overlay away and the Cauchy is unchanged.

**Where the reader stands.** Behind the screen, at one point. The look runs from it to the crosshair; a thumb lands √2
off the look on a screen one thumb away, home at 1/√2, one thumb off at 1, and the horizon runs parallel to the screen and
never lands on it. The point has no size and draws no shape: it is a vantage, the place the read is from, and the read is
there with no world at all. Turning and scaling the world change none of it; the buildings are what paints it.

**One thumb, two thumbs, three.** In the plane the reader holds one thumb at arm's length: H, square to the line of
sight, and one reading, v against h. In space it holds two thumbs crossed at a right angle, both square to the line of
sight: one reads up, v against h, the other across, v₂ against h. The pair (v/h, v₂/h) is a direction of the wedge; each
thumb alone reads the one-dimensional Cauchy with its own corner, and the two together the two-dimensional Cauchy above.
Two thumbs add no second length: both are the reader's own H, so no breadth for either party enters, and what a writer
would write as V = V₂ = H is the two thumbs being the same size. The right angle between them is no amount either: it is
the quarter turn that takes one thumb onto the other, unchanged when the world is scaled. So the dimension, counted from
a standpoint, is the number of transverse facings, a thumb for each direction square to the look: one in the plane, two
in space.

Held that way, with the look along h, the middle of the cross reads (0, 0): it is home for both pairs, as the middle of
a camera's screen is, and the triple corner, where both read 1, lies 54.74° off the look. To put the corner under the
crosshairs the look turns onto the diagonal, and then every party is a thumb at the same angle to it, h with the rest:
two thumbs at 45° in the plane, three at 54.74° in space, horizontal, vertical and depth, each reaching one thumb at the
corner. The three pairs' corners are three planes through the eye and meet in one line only, so that look is the only
one that puts the crosshair at the corner of all three (the Cauchy's thinning, centred on whatever is looked at, does
not choose it). They are the same one length either way: the thumbs counted across the look are the dimension, and the
thumbs counted at the corner are the parties, one more.

**The sphere without V, and the cone of one read.** Every way three crossed thumbs can stand to one another, with H and V
known, is a point of the sphere: three amounts at a known radius, every sign kept, closed and finite. That is the
writer's. The same relations with V unknown keep only their ratios (v/h, v₂/h), and two things go with the length: the
sign (a point and the point opposite it through the centre give the same ratios, so the sphere folds onto itself, the
projective plane, a screen its chart) and the closing (the great circle square to the look lands at infinity, the
horizon: where the sphere would have closed, the missing V's trace). The sphere's even measure lands on the screen as the
two-dimensional Cauchy, each reading twice. In the same way a single read with H and V known is the wedge, an octant of
the ball: three flat faces through the eye and a curved cap at a known radius, the cap the only part carrying an amount.
With V unknown the cap goes, and what is left is the cone: three flat faces meeting at the eye along the thumbs, open,
with no far side. A cone is the one kind of shape that scaling about its apex carries onto itself, so the read is
unmoved when the world is scaled; the cap was where the scale lived. Cut by a screen one thumb out, the cone shows its
law: the quadrant of readings with the half-Cauchy 2/(π(1 + s² + s₂²)^(3/2)) square to h, the triangle with the corner at
its middle down the thumbs' diagonal; cut elsewhere, the same law at another size, which is why H only zooms. In the
plane the same: a quarter of a disc with its arc when V is known, a right angle, two rays and no arc, when it is not. In
short:

| Shape | What is kept | Whose |
|---|---|---|
| The sphere | H and V, every sign: all relations, closed | the writer's |
| The Cauchy plane (the full round of the look) | V dropped: opposite points one, the horizon at infinity | the relations without V |
| The cone of one read (the quarter turn) | V dropped and no relation negative: every pair from home (0) to its horizon (∞) | the read |

The cone is the writer's name for what one read holds; the reader has no shape, only a vantage, and what it can say of
distance comes only through H, never V. The read's whole cone is the half-space in front, the hemisphere above; the
wedge's cone is the part of it where no pair of thumbs reads below zero.

**Setting H sets the near-field sphere, the writer's.** Every way H, V and V₂ can stand to one another, with all eight
facings, is the sphere; set H, and a writer who names the others at it (V = V₂ = H) has fixed that sphere's size. So
choosing the thumb is choosing the near field as a sphere: the ball of radius H about the standpoint, every facing joined,
nearer than one thumb inside it and farther past it. That is the writer's account. The reader has the same choice as a
split on every direction it reads, nearer than one thumb or past it, one read at a time: no surface, no V, no facings
joined. One choice of H; two accounts of what it set.

**Where the split falls: looking around.** The overlay is the reader's to move, and it moves it by looking. Pointed at a
thing, the crossed thumbs take its distance as H, so that thing sits at the corner, half of every direction's heat in
distance nearer than it and half farther; looking at another thing moves the split to it. We can only speculate that a
reader does this, and the reason to is that it is optimal: the corner is where a reading's cells are finest relative to
their place (§6, "H is a zoom"), and a thing at the corner is the thing at parallax's corner, since a step of two
thumbs, half the baseline equal to the distance, places it with the least error, ε·cosh(ln k) at its least, ε (§8, "The
thing itself as H"). Putting the thing looked at on the corner is what a reader should do; whether readers do is open.

**Where the heat comes from.** The read is a heat map: a continuous weight over its readings, with nothing counted in it
and no grain of its own. The measure is uniform by solid angle: every direction of the hemisphere alike, so on the
hemisphere itself, by angle, there is no heat. The heat is that measure read in a coordinate. Hold a screen one thumb
out, square to the look, and read a direction α off the look at r = tan α thumbs. In the plane, with one thumb, a
direction θ reads s = v/h = tan θ, and dθ = ds/(1 + s²) = cos²θ·ds: the heat per unit of reading is (2/π)/(1 + s²), the
half-Cauchy, falling as cos²θ. In space, with the thumbs crossed, a small patch dA of the screen at r subtends
dΩ = cos³α·dA (one cosine for the patch's tilt to the ray, two for its distance, sec α, squared), so the heat per unit of
screen is (1/2π)·cos³α = 1/(2π(1 + r²)^(3/2)), the two-dimensional Cauchy: hottest on the look, 0.35 of the peak one
thumb off (45°), 0.125 at 60°, none at the rim. With n thumbs square to the look it falls as cos^(n+1); the one cosine
more in space is the one thumb more. A camera shows it: the natural vignetting of a wide lens, the cos⁴α by which a
photograph's corners darken, is this cos³α and one more cosine for the aperture seen at a slant, so three of its four
cosines are the heat, there before any light arrives (0.35 of the middle at 45°, against the photograph's 0.25).

The overlay brings a second heat, in distance, there only once H is laid on: the share of a direction's distance below
x = d/H is (2/π)·arctan x. Per unit of plain distance it is greatest at the eye, 2/(π(1 + x²)); read as the reader reads
distance, by ratio, per unit of ln(d/H), it is (2/π)·x/(1 + x²) = (1/π)·sech(ln(d/H)), hottest at one thumb and cooling
alike both ways: 0.8 of the peak at one in 2 and at two thumbs, 0.47 at one in 4 and four, 0.25 at one in 8 and eight,
never zero. Multiplied, the two heats are hottest at one point, on the look one thumb out, the thing looked at; they meet
there only because the look points at it. Look at something else and both go with it. The heat is in the readings, not a
shape: the shape is still the hemisphere, and the heat is how its directions crowd as the reader reads it. (A writer can
sample it, K places at its quantiles, §6.) *The heat is given; the paint is met.*

The heat is not a grid seen from home. Marks laid evenly on a wall one distance d away, the writer's grid, are flat in
the reading (y = d·s, area d²·da·db) and, per unit of angle, crowd toward the horizon as sec²θ in the plane and sec³α in
space; nothing in them is hottest along the look. The Cauchy is the other way round: the turn, even in angle, laid on that
flat grid, dθ/ds = 1/(1 + s²), and in space dΩ/dA = cos³α. It is the turn per unit of the writer's grid, the *per* of §4,
not the layout of the world: it belongs neither to the wall alone nor to the eye alone, but is the rate at which a turn
consumes the world.

Said in measure theory, the Cauchy is a Radon–Nikodym derivative: the turn's even measure carried onto the wall by the
projection from home, against the wall's own measure, dν/dλ = (1/π)·d/(d² + y²) for a wall d away. That is the
half-plane's Poisson kernel, its harmonic measure seen from the standpoint: where a random walk started there first
meets the wall (Kakutani 1944). On a flat wall the two agree in every dimension: the half-space's kernel, Γ(n/2)/π^(n/2)
· d/|x|^n, is the even hemisphere carried onto the wall, (2/|S^(n−1)|) · d/|x|^n, the same constant; in space
(1/2π)·d/(d² + r²)^(3/2), the cos³α above. On a sphere they part (below, "What survives in space, and what does not").
Stepping back composes the kernels, e^(−d|k|), the Poisson semigroup in the standpoint's height d. This is Laplace's
equation, a steady state; it is not the heat equation, whose kernel is the Gaussian, e^(−tk²). The Gaussian too keeps
every frequency; it damps the fine ones by k² where the Cauchy damps by |k|, and it has a variance where the Cauchy has
only a scale. The kernel that loses frequencies outright is the floor's box blur, whose transform has zeros. The "heat"
here is a weight over the readings, never diffusion in time. The identity is classical; what is read into it is the
vantage.

**The shape is swept, not each thumb.** Each pair of thumbs reads a quarter turn: from its home, where it reads 0, to
its horizon, where it reads ∞. Down the thumbs' diagonal that is the wedge, a triangle on the screen whose corners are
the thumbs and whose edges are where a reading is 0 or ∞, inside the hemisphere the read holds; the sphere behind is
other facings, what the head would give turned all the way round, and joining facings is the writer's. Within the
quarter turn the even read does not come from sweeping each thumb through its own angle. Sweep them that way, evenly and
one after the other, round about the up thumb and then up toward it, and the directions pile toward the thumb the first
sweep turns about, where the second sweep shrinks to a point; the hill in the readings is not round; v falls below h for
0.343 of the readings, not a half, and the near field is 0.233, not a third. Taken in the other order, the pile goes to
another thumb and another pair leaves its corner. Swept together, the three thumbs fill the wedge evenly by area: every
pair at its corner, the near field a third, and no order, since no pair is taken past its horizon. Written in the
thumbs' own angles that sweep is even round the horizontal and even in height, not in angle (Archimedes' hat-box, as
above); the weight on the second angle comes from the thumbs moving as one, not from either thumb. The thumbs are marks
the shape carries, a thumb √2 off the look and a home 1/√2 however it is pointed. A writer, holding every turn of space,
finds the same law on the octant as the one measure left alone by turns (Haar), any turns composing to one turn about
one axis (Euler); that is the writer's account from the whole sphere, not the read. In the plane there is one thumb and
one quarter turn, and the two ways are the same. The shape can be swept further than turns: any linear map of the
thumbs' space, a projective map of the screen, carries the even read to an elliptical Cauchy, the same family, its
standpoint five numbers in space against the plane's m + iγ; only the turns keep it round, and a stretch is a drawing
with two lengths, a writer's.

**The writer's cube, and the sphere as the writer's picture.** The writer's frame with three parties is Descartes's: X,
Y, Z, three number lines, every point three amounts. It reaches the reader's directions only with H and the angles: X =
H·cos a·cos ψ, and so on. Every direction about a point at radius H, one thumb, is a sphere, and it is the writer who
draws it. The reader holds directions and reads them with the Cauchy; it never holds the sphere whole. Placed together,
the corner of the reader's wedge points at the vertex of the writer's cube. With the cube outside the sphere, touching
it at the ends of the axes, the picture is the inscribed sweep's; with the cube inside, its far corner on the sphere, it
is the central sweep's (Thales' circle through home, the ends and the far corner). The hemisphere's 2 and ½, like π/2
and 2/π, are the writer's measure.

**What survives in space, and what does not.** In the plane, one law plays four parts: the image of the uniform turn
under a Möbius map, harmonic measure, the powers of the standpoint, and the two sweeps' rates. On the sphere they part,
and turns of space do not commute. They come apart into three laws: harmonic measure keeps the powers of the standpoint
and its mean; the spherical Cauchy, the uniform turn pushed through a boost, keeps the Möbius maps; and neither is the
image of the other. A quarter turn about one axis and then another ends 120° away from the same two taken in the other
order, where in the plane any two turns commute. What survives is the split between direction and payload, heat and
paint, the corners, and the wedge seen from home: the second test still sorts every quantity, and every pair of thumbs
still has its corner at the median, since those need only the exchange of two shares, not commuting turns (the essays'
thirteenth works this through).

## 8. From reading to writing

**Parallax is the passage.** One standpoint gives directions and a frame, and no size: every ghost of the room, twice as
far and twice as large, gives the same readings. A second standpoint adds a second variable, the step between the two.
Each point, matched in both looks, is then two rays crossing, and its place comes out of the crossing, in the step's
length; the step's length in any other unit is what a writer carries in. More standpoints give every place seen. This is
how a reader reconstructs the writer's cube, and while it does, it is writing: it has moved, joined its standpoints and
holds what no one standpoint holds. When it stops and looks again, it reads. A read and a write are not two kinds of
observer; they are what one observer is doing.

**Parallax is a sum of reads.** Put the two standpoints a step apart and let each read a point in its h/v chart along
the step, cot a from one end and cot b from the other. Then cot a + cot b is the step over the point's distance from the
step's line: the depth is the reciprocal of a sum of two reads. Those are the two operations the Cauchy is closed under,
the sum (a relay of standpoints, their points m + iγ adding) and the reciprocal (the exchange). So parallax never takes
a read out of the family. If each read is uncertain as a read from a height γ is (the uniform turn's law about the true
direction), and the two reads' errors are independent, each is a Cauchy point w = (c + iγ)/(1 − iγc) in that chart, c
its true value (a Cauchy law written by one complex number, its location plus i times its scale, as McCullagh 1992 does;
the depth's point D below is written the same way), and the depth is exactly a Cauchy whose point is the same
triangulation done on the two points: D = B/conj(w_a + w_b), B the step. That holds at every γ, not only for small
errors; rays that do not meet ahead are part of the same law, as negative depths. At the pair's corner, the circle on
the step, the depth's point stays at the true distance d, turned by twice the read's error angle: D = d·e^(2i·atan γ).
Two things leave the family, and each can be seen in a line. The place across the line of sight is a ratio of two sums,
−1 + 2·cot a/(cot a + cot b) in half-steps; its density over each standpoint is a read's density at zero times a mean
the sum does not have, so it is infinite there, where a Cauchy's never is. And when each standpoint reads only a quarter
turn, the sum of two half-Cauchys has density (4/π²)·s near zero, where every half-Cauchy's is positive; so the depth's
tail falls as 1/d³, not 1/d², and that depth has a mean. And repeating the reads, the mean of the reciprocal depths
gains nothing, while their median narrows. Parallax is the Cauchy's own composition, carried across two standpoints; the
step is the one amount in it. (Checked exactly; see Code and data.)

**Turning teaches the directions; walking teaches the world.** A standpoint has two motions, a turn about itself and a
step along a straight line. A turn moves every direction by the same angle, near and far alike, so nothing shifts
against anything else: it gives the frame, the corner where the thumbs cross and the Cauchy of the fingers, and these
are the same in every world. A reader that only turns learns its own directions and their heat and nothing about what is
out there; what meets its fingers changes, and a colour carries no place. A step is the first motion whose effect
depends on the world: near things cross the fingers faster than far ones, and that difference is parallax. Any motion of
a standpoint is a turn and a step together (a turn about any point but the standpoint carries the standpoint along a
chord, and the chord is a step), and only the step's part places anything. The straight line walked is the writer's own:
count it in a unit and every place found from it is written.

**Turns, counts and corners.** A read's turns are rotational: between two directions it passes through every one between,
so a read never turns sharply. A corner, a change of direction at one place, is met only by walking the line and stopping
there, which is a count: at the third stop, turn this much. That is why a corner is the writer's. Three things follow.

- *A count made to hold a turn rings.* Lay a finite count of even waves, or of evenly spaced samples, along a turn and ask
  it to hold a sharp change. It overshoots on both sides of the change, by about 9% of a jump however many waves are used,
  the ripples only crowding nearer (Wilbraham 1848, Gibbs 1899). The overshoot belongs to the representation, a finite
  count of even waves, not to the edge it is asked to hold: physical ringing is a different thing, a dynamics (a struck
  bell rings after it is struck and never before; light past a straight edge makes fringes on the lit side, fading
  smoothly into the shadow). What the overshoot shows is the cost of writing a sharp change as an even count, which has
  no place to put the corner.
- *Written down, the two acts cost differently.* An outline can be written as numbers at even places of one turn (its
  Fourier coefficients, its radius from a centre at even angles, its points at even shares of its length rebuilt by a
  band-limited sum) or as a walk along it (Bézier pieces, a list of points, the same points as steps, a turtle's forward
  and turn). On 73 outlines from a shape library, each written to within half a percent of its size, every one of the
  first three was shorter as text than every walk on the smooth outlines, and every walk shorter than every one of the
  three on the outlines with corners. Rounding the corners of a square, a triangle, a star and an arrow by a growing
  radius took the even samples from two to three times a Bézier path's length to between a half and three quarters of
  it, on all four, while a list of points grew longer, a walk needing more stops to follow a gentle curve. Across the
  library the even samples' length followed how fast the outline turns (its length over its tightest radius of
  curvature; Spearman ρ 0.85) more than how many corners it has (0.55); the Bézier path's followed its corners (0.59)
  and not its turning at all (0.00). (Measured; see Code and data, where the predictions that failed are recorded too:
  the exact rate at which the count grows as a corner sharpens, and a walk's cost staying flat as a corner rounds.)
- *π and e are where a count tries to hold a read.* Archimedes' polygons give rational bounds on π, Bernoulli's coin
  rational steps toward e, and n reads of θ/n composed are both at once (§5, "Euler's formula as a count of reads"). The
  continuum a writer holds is that count completed, not the reader's uncounted turn.

**Motion, from reads.** A thing coming toward the reader is read at its edge: x, the thing's breadth against its distance,
the reading v/h of the line to its edge. One read holds one x; that x grows is two reads joined, and so a write. The
reading over its rate of growth, x/ẋ, is the time until the thing arrives, if it keeps coming as it comes: the breadth
cancels, and so do the distance and the speed. Lee (1976) proposed that a driver braking uses exactly this, and found a
rule on it: brake so that the time to contact shrinks no faster than half a tick a tick, τ̇ ≥ −½, and the car stops at
the thing, since at τ̇ = −½ the distance it needs to stop is the distance it has. Three limits keep this honest. A rate
of change needs two reads joined, so ẋ is a write, and so is everything made from it: τ, a count of the reader's own
ticks, as places after a counted step are written in its own thumbs, and τ̇, ticks per tick, which no change of clock
moves. Being unmoved by the clock makes τ̇ scale-free, not a read: no single read holds it. Seconds are a writer's unit,
carried in. One stream cannot tell a thing coming nearer from a thing growing where it stands, since both raise x alike;
a neighbour at the same depth, read at once, tells them apart, approach moving both readings and growth one. And a speed
in metres a second is a writing twice over: a metre and a second, both carried in. No reading holds the rate at which the
reader turns.

**Walking to the mountain.** Hold the thumb out at arm's length, H against the arm L, and walk toward a mountain whose
breadth V\* and distance d are unknown. The thumb never changes; each read is the finger of the thumb the mountain's
edge touches, [h : v]. The writer's account of which finger that is, v/h = (V\*/d)/(H/L), uses the amounts the read
never holds. A read is one place, now: "one in eight of the thumb", or "four thumbs". It does not hold that the mountain
is nearer than it was, or that it is getting nearer: nearer compares two reads, and joining reads is a write. What
follows is the writer's account, the reads laid in order along the walk. Far off the mountain is one in eight of the
thumb, then one in four, one in two: each time the distance halves the reading doubles, and each such stretch takes as
much of the heat as the last. One read has the mountain exactly covering the thumb. That is the corner, and that read
needs no amount: the reader can say "now the mountain is my thumb" while V\*, d and the corner's distance d_c = V\*·L/H
stay unknown. Past it the mountain is more than the thumb, and the two sides mirror each other: standing at d and at
d_c²/d read as reciprocals. Laid in order, the reads climb toward the horizon, [0 : 1], h falling to 0, and halvings
never reach it. That is a limit, and a limit is a sequence completed, the writer's (§5). No read meets it: each read,
wherever it is taken, has the whole sweep of the thumb, its corner and its horizon, and nothing in it says how near the
end is. The walk arrives because the walk is a count of strides and ends; arrival is contact, a write in one's own H,
and what the reader then has is one more read, the mountain's foot straight down. So the τ̇ of the walk is the writer's
too, from reads joined: a steady pace makes it −1, past Lee's −½, arriving at speed; easing so that it holds at −½ stops
at the foot. Counting from the corner plants a flag there: the corner is a read and free, the flag at it a write. The
strides from the corner to the foot are d_c, so counting them writes the mountain: V\* = (strides from the corner) ×
H/L, in the walker's own stride, and in metres once the stride is carried in. To know V at the foot is to have counted
one's own steps, and to be looking at one's feet. Scale the world and no read along the walk moves, only that count. We
do this whenever we walk toward something: the corner is free, the approach and the size are written.

**Knowing V comes by degrees.** The crossing is not a switch thrown. It has three counts.

- *In what.* Two standpoints a step apart give every place in that step. If the step was H, one thumb, places are in
  thumbs and V is written as V*/H. Only a step counted in an agreed unit gives an amount, and that is the one rung
  scaling the world moves.
- *How well.* The place's error per unit of angular error is least when the thing sits at the pair's corner, the circle on
  the baseline, half the baseline equal to the distance. With k = d/(B/2) and ε the smallest angle the reader can tell
  apart, the fractional error in the distance, and so in V, is ε·cosh(ln k) = ε·(k + 1/k)/2: ε at the corner, about
  ε·d/B far off, the same at k and 1/k. It reaches 1, and the thing is a direction alone, near d = B/ε. In the worked
  example (§10) one thumb walked toward a range ten thumbs off puts it at k = 20, an error 10.025 times the step's ε; a
  baseline of twenty thumbs would put it at the corner, with ε alone.
- *Of which things.* So one observer, from the same two standpoints, knows V for near things and does not for far ones.
  Knowing V belongs to a thing at its distance, not to the observer.

More standpoints and longer baselines narrow the band; nothing closes it. The writer who holds V exactly, the vantage
this paper calls the writer, is the limit of the passage, not a stage of it, just as π is the limit of its approximants
and not one of them.

**The thing itself as H.** The thumb can be set to the very thing whose size is wanted, in two senses. *As the unit*:
the thing is drawn at one length, its V is 1 by choice, and nothing about it is found; what is found is everything else
in its units. Its own two ends become the baseline and the reader is the point placed: an angle α across it, centred,
puts the reader 1/(2·tan(α/2)) of its breadth away, from one look. *As the focus*: the reader keeps its thumb and
chooses a baseline that puts the thing at parallax's corner, half the baseline equal to the distance, where the error is
least. That needs the distance roughly first, so it is done in passes, each baseline set from the last rough reading.

**A survey.** Snellius (1617) and Roy (1784–85) wrote whole countries this way: thousands of angles read, one base
walked and counted. The angles are readings; the base is the one writing; every side of every triangle is then in the
base's unit. A second base checks the first and adds no scale.

**Recovered, by writing.** A reader can recover a thing exactly, its shape, its places, even its size, and still
partially. A loop that closes shows that the routes taken agree; it cannot show that no route remains untaken.
Completeness is never a reading. What recovers the thing is not reading harder but the passage through standpoints, and
in that passage the observer is writing.

**And back: a write is over, and must be read.** A write is a count, and a count stops: the stride walked, the number
put down, the blueprint drawn. Once made, it is over; nothing more happens in it. To be used it must be read: someone
stands somewhere and looks at it, at marks on a page in their directions and their ratios, as at anything else that
arrives. A blueprint in a drawer does nothing until it is looked at; a survey's base, once walked, is read against by
every angle that follows; a drawing of a known room, rendered from a standpoint, is a write turned back into a read. So
the passage runs both ways: reading becomes writing through standpoints and a count, and every write, once made, joins
what is read. The write is the past tense; the read is the present.

## 9. What a blueprint adds

Ratios suffice for a great deal. A tower of ratios, each storey read against the next, holds a building, its rooms and
their things with one amount at the top. A loop of ratios checks itself. A reader builds with ratios alone and never
needs a unit, until one of these is wanted:

1. the size, an amount;
2. meeting out of view, with another reader with nothing in view in common;
3. sums of amounts, which no ratio supplies;
4. the join, the facings put together into a closed circle or sphere;
5. the thing before the thing, a plan for what is not yet there;
6. completeness, stated rather than hoped for;
7. a far field kept in proportion, common to readers whose corners differ.

Each is a capability, not a condition. A blueprint adds them, and to make or read a blueprint is to write. Nothing here is
against the writer or the number line: they are what holds what no standpoint holds.

## 10. A worked example: the mountain and the thumb

Hold up a thumb, one mile wide in the writer's units, and look at a mountain range twenty miles wide, ten miles off.

**From the standpoint.** The range's ends sit at ±45°: the pair (half-width, distance) is at its corner. Of thirty-six
fingers spread evenly over the half turn, eighteen land on the range. Scale the world by a thousand and nothing in the
view moves: still 45°, still eighteen fingers.

**Mountain equals thumb.** With no V, the reader drawing the range at its own H reads it one thumb wide at half a thumb
away. This is the writer's circle, V = H: the thumb taken to equal the mountain. Every amount is then off by V*/H = 20,
the range twenty thumbs wide and not one, the same on both sides of the corner.

**The two sweeps, measured.** On the circle it draws about the thumb, the writer measures the central sweep at π/2 and
the inscribed at 2/π; to the range's ends, 1.1107 and 0.9003. Their product is 1, the starting length returned, H in H.
The mountain never enters.

**Walk one thumb.** Step one thumb toward the range and read again. The half-angle's reading goes from s = 1 to s′ =
10/9. The distance is d = H·s′/(s′ − s) = 10 thumbs, the range V = 2·s·d = 20 thumbs. In thumbs, exactly. Count the
thumb in miles and it is in miles.

**The mountain as H** (§8, "The thing itself as H"). As the unit, its ends 90° across put the reader half a range-width
from its middle, from one look; as the focus, a baseline of twenty miles puts it at parallax's corner, where one thumb
walked has about ten times the least error.

**In three dimensions: a tower and two thumbs.** Hold both thumbs crossed (§7), one reading up (v/h), one across (v₂/h),
the look along h, so the middle of the cross reads (0, 0) as a camera's screen does (not §6's look down the diagonal), and
look at a tower off to one side. Its top reads (¼, ⅓): a quarter of a thumb up and a third across for every thumb
along the look. Its foot reads (0, ⅓). From one place that is all: two directions, no distance, and a tower twice as large
twice as far off reads the same.

Step one thumb across and read again. The top now reads (¼, ¼), the foot (0, ¼). Only the across thumb moved, by 1/12, so
the distance along the look is 1/(1/12) = 12 thumbs. Then the top is 12·⅓ = 4 thumbs across and 12·¼ = 3 up, and the foot
4 across and 0 up: the tower is 3 thumbs tall, 12 off and 4 to the side, in thumbs, exactly.

The up thumb did not move, and that is the gain of the second thumb. In the plane one step gives one change for one
unknown, the distance, and nothing is left over. In space each step gives two changes for the same one unknown, so one
is spare, and it must agree: a reading can move only along the line through where the step itself points (the epipolar
condition of stereo vision). A step across points straight across, so readings move straight across. Step one thumb
across and up together and both thumbs move by 1/12, and both give 12. Take the step for diagonal when it was across,
and the up thumb, which did not move, says the step had no up in it: the misreading is caught. Step one thumb forward
instead and both readings grow by the same factor, the top to (3/11, 4/11): the tower slides straight out from the
middle of the cross, its up over its across still ¾, and either thumb gives 12.

Scale the world, the step with it, and no reading changes, so every place in thumbs stands. Count the thumb as 5 metres
and the tower is 15 metres tall and 60 away. The writer's one amount is still one amount; the second thumb adds no
length, only a check (checked exactly; see Code and data).

## 11. What this changes

It changes no mathematics. It sorts.

- **Every reading is the reader's, every amount the writer's.** A result stated as a ratio, unchanged by scaling the
  world, is a reading; a result that moves with the world's scale is a writing, and needs an amount carried in. A
  Cauchy-type quantity is a direction where a turn that lays it can be named, apart from the law's shape; there the
  amount the payload carries is found separately. A fat tail alone is no evidence of a turn: a mixture of amounts makes
  one too.
- **The constants have owners.** π, e, π/2, 2/π, the hemisphere's 2 and ½, the Cauchy's normalizing constant, the
  logarithm's nats and the angle's degrees are the writer's measures of the reader's things. The reader's own versions
  are finite: an order, a ratio (one in two, one in four), a corner, a composition by tangent addition.
- **The roles move.** No observer is a reader or a writer once and for all. It reads while it stands and turns; it
  writes while it walks, counts, ranges or agrees a unit. The passage between is parallax, and it comes by degrees.
- **The line is where knowing V is.** On one side of it every reading holds, whatever the world's size; on the other every
  amount holds, in some unit. The passage across is always by an amount carried in.

**Three cases in data.** Practice already reads the median where it should; the sort says why, and where to look. In
open data from the two LIGO detectors (Abbott et al. 2023; 512 s, about two million whitened samples each), each
detector's signal taken alone is an amount, and its heavy tail is one loud transient on a law of finite spread: block
means shrink as n^(−½), which nothing Cauchy can do. The Cauchy is in the direction [H1 : L1] of the two read at one
instant: its median at 1, its spread unmoved by averaging, its angle near uniform, and the small departure from uniform
reproduced from each channel alone, by pairing samples 8 s apart, to 0.0001; a prediction written before the data were
fetched, which could have failed.

A reader moving through a sky of sources counts more ahead. With no limit on brightness the census is a count of
directions, and its dipole is 2β, Ellis and Baldwin's 2, from the directions alone (1984). A real census is cut at a
brightness, and the cut adds a term set by what arrives: the counts' slope and the sources' spectra, read from the same
catalogue. On Secrest et al.'s quasars (2021) the sort sets the number. Per slice the expected dipole is
[2 + x(1 + α)]·β, the 2 the directions' and x(1 + α) the payload's, read from the slice's own counts and colours: 5.3 to
6.6 times β, so the payload carries 60–70% of it. Taken as directions alone (2β), the measured 0.018–0.023 would give a
speed nearly three times too large; with the payload's part divided out, four slices by brightness give one β,
3.3·10⁻³ ± 0.3·10⁻³, 2.7 times the speed read from the microwave background, as one motion of the reader should. Slices
by colour give 2.3, 2.8 and 4.6 times it, which no motion of the reader can do, so part of the dipole belongs to what
arrives. The sort
does not settle where the dipole comes from; it says which part could be the reader's.

In a double slit lit one photon at a time, the fringes' visibility is at most 2hv, h and v the two paths' shares, and
the which-path predictability |h² − v²| (Greenberger and Yasin 1988; Englert 1996): full visibility only at the corner.
On Aspden, Padgett and Spalding's frames (2016) the slits' counts, 9,026 : 10,465 and 11,993 : 11,891, give
2hv = 2√(n₁n₂)/(n₁ + n₂) = 0.997 and 1.000, the pair at its corner, and the
measured contrast, 0.69 and 0.56, lies under that bound, short by the source. The bound is the shares', the geometry's;
how far below it a pattern falls is what arrives. None of the three is new physics. What the reading adds is where each
part lives.

**And one where it failed.** Seeds falling from a plant also spread with a fat tail, and the turn can be named beforehand:
a seed leaving its release point straight, every downward direction alike, lands as the hemisphere's Cauchy, Clark's 2Dt
with shape p = ½ and a tail falling as r⁻³. On Bullock et al.'s compiled kernels (2017), the 35 that could be fitted of
38 picked as wind-dispersed from their labels alone say otherwise: median p 0.10, a tail falling about as r⁻², shapes
spread widely, and no nearer the turn's than kernels carried by animals. The fat tail there is a mixture over wind
speeds, as the literature reads it: amounts, not a turn. So the reading is not a rule that every Cauchy-like law is a
turn's heat. It holds where the turn is there to be named, and a test written before the data can show where it is not.

One classical case, not run here, shows the sort as cleanly as any. A spin carried slowly round a closed loop of field
directions comes back with two phases (Berry 1984). The geometric one is half the solid angle the loop of directions
encloses: it depends on which directions were visited and nothing else, the same if the loop is taken twice as slowly,
in a field twice as strong, or in an apparatus twice the size. The dynamical one is energy times time, and moves with
all three. Experiments have separated them by keeping the loop and changing the rest: photons in a coiled fibre, whose
rotation followed the solid angle of the coil's turning alone (Tomita and Chiao 1986), and neutrons in a turning field,
where the field's strength and the time were varied and the geometric part stayed (Bitter and Dubbers 1987). Both tests
sort it: scaling moves only the dynamical phase, and changing what is carried along the loop moves only the dynamical
phase. Read here, the half is the central sweep's doubling: a spin state at angle θ has its point on the sphere of
states at 2θ, as the radius stands at twice the ray's angle (§4), so a loop counted on that sphere is counted twice.

**Where the ideas come from.** Jaynes's principle of transformation groups (1968, 1973) gives the method: the measure
that an observer's ignorance leaves unchanged. Poincaré's universe made a thousand times larger overnight (1908),
undetectable from inside, is the scale test; his distinction between representative and geometric space is the reader's
and the writer's. Leibniz's space as an order of coexistences (1715–16) is the reader's picture; Klein's programme
(1872), geometry as the study of a group, is the method's form. Gibson's ambient optic array (1979) is the stained-glass
window. Bridgman and Buckingham sorted quantities by scale long before. What is offered here is the division into two
acts, the heat of directions and the payload inside a read, and what carries an observer from one to the other.

## Code and data

The checks and measurements cited in the text are in the repository that holds this paper (reportbase/wander), each with
its plan written before it was run: the Cauchy's routes in `plans/cauchy-routes.md` and `runs/crt/`; parallax as a sum of reads in `plans/pxs-plan.md` and `runs/pxs/`; the formats
measured as text in `plans/txt-plan.md` and `runs/txt/`; the tower and two thumbs in `runs/two/two_thumbs.py`; the three
thumbs at the crosshair, the one-thumb circle and the three corners in `plans/thm-plan.md` and `runs/thm/`; the shape
swept whole against each thumb on its own in `plans/swp-plan.md` and `runs/swp/`; the read with no world, and where the
reader stands, in `read.html`; the heat on a flat screen and a lens's cos⁴ against it in `pinhole.html` (its uniform
sky); the tunnel laid by its heat, the distance reading and a world culled by K in `crosshairs.html`; Euler's formula as
a count of reads in `plans/elm-plan.md` and `runs/elm/`. The three cases in data of §11 (LIGO, the quasar dipole, single
photons) are `plans/lgo-plan.md`, `plans/ebd-plan.md` and `plans/wvp-plan.md`, with `runs/lgo/`, `runs/ebd/` and
`runs/wvp/`: each plan states its predictions and what would count against them before its run, and records the runs as
they came out, the killed ones too. They illustrate the sorting of direction from payload; none of them alone
establishes it.

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
- Burn, B. J. (1966). On the depolarization of discrete radio sources by Faraday dispersion. *Monthly Notices of the Royal
  Astronomical Society* 133, 67–83.
- Buckingham, E. (1914). On physically similar systems; illustrations of the use of dimensional equations. *Physical
  Review* 4, 345–376.
- Ellis, G. F. R. and Baldwin, J. E. (1984). On the expected anisotropy of radio source counts. *Monthly Notices of the
  Royal Astronomical Society* 206, 377.
- Englert, B.-G. (1996). Fringe visibility and which-way information: an inequality. *Physical Review Letters* 77,
  2154–2157.
- Euclid. *Elements*, Book III, Proposition 20.
- Euler, L. (1748). *Introductio in analysin infinitorum.* Lausanne.
- Euler, L. (1776). Formulae generales pro translatione quacunque corporum rigidorum. *Novi Commentarii Academiae
  Scientiarum Petropolitanae* 20, 189–207.
- Gibbs, J. W. (1899). Fourier's series. *Nature* 59, 606.
- Gibson, J. J. (1979). *The Ecological Approach to Visual Perception.* Houghton Mifflin.
- Greenberger, D. M. and Yasin, A. (1988). Simultaneous wave and particle knowledge in a neutron interferometer.
  *Physics Letters A* 128, 391–394.
- Haar, A. (1933). Der Massbegriff in der Theorie der kontinuierlichen Gruppen. *Annals of Mathematics* 34, 147–169.
- Hölder, O. (1889). Ueber einen Mittelwerthssatz. *Göttinger Nachrichten*, 38–47.
- Jaynes, E. T. (1968). Prior probabilities. *IEEE Transactions on Systems Science and Cybernetics* 4(3), 227–241.
- Jaynes, E. T. (1973). The well-posed problem. *Foundations of Physics* 3, 477–492.
- Klein, F. (1872). *Vergleichende Betrachtungen über neuere geometrische Forschungen.* Erlangen.
- Lambert, J. H. (1772). *Anmerkungen und Zusätze zur Entwerfung der Land- und Himmelscharten.* In *Beyträge zum
  Gebrauche der Mathematik*, Theil III. Berlin.
- Lee, D. N. (1976). A theory of visual control of braking based on information about time-to-collision. *Perception*
  5, 437–459.
- Leibniz, G. W., and Clarke, S. (1717). *A Collection of Papers … Relating to the Principles of Natural Philosophy and
  Religion.* London.
- Lindemann, F. (1882). Ueber die Zahl π. *Mathematische Annalen* 20, 213–225.
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
- Snellius, W. (1617). *Eratosthenes Batavus.* Leiden.
- Staudt, K. G. C. von (1847). *Geometrie der Lage.* Nürnberg: Bauer und Raspe.
- Takenaka, S. (1925). On the orthogonal functions and a new formula of interpolation. *Japanese Journal of
  Mathematics* 2, 129–145.
- Tomita, A. and Chiao, R. Y. (1986). Observation of Berry's topological phase by use of an optical fiber. *Physical
  Review Letters* 57, 937–940.
- Trotter, H. F. (1959). On the product of semi-groups of operators. *Proceedings of the American Mathematical Society*
  10, 545–551.
- Viète, F. (1593). *Variorum de rebus mathematicis responsorum liber VIII.* Tours.
- Wantzel, P. L. (1837). Recherches sur les moyens de reconnaître si un problème de géométrie peut se résoudre avec la
  règle et le compas. *Journal de Mathématiques Pures et Appliquées* 2, 366–372.
- Wilbraham, H. (1848). On a certain periodic function. *Cambridge and Dublin Mathematical Journal* 3, 198–201.

The entries were checked against Crossref and library catalogues on 3 November 2026; Malmquist (1926) is given as it is
usually cited.
