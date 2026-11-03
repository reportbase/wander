# Reads and Writes

**What can be known from a standpoint, and what it costs to know more**

*Tom Brinkman. Draft, 30 October 2026; retitled 2 November 2026 (it was* Readers and Writers*). Written with AI assistance (Claude).*

The propositions and proofs this paper draws on are in *Observation from Somewhere*, now archived and kept for
reference; where its wording differs from this paper, this paper stands.

## Abstract

Observation comes in two acts. A *read* is taken from a standpoint, turning there. It needs one length, H (a thumb held out
at arm's length), and what reaches the standpoint along each direction; every reading is a ratio, a direction [h : v], and
no amount survives into it. A *write* holds the whole: both sides of every axis, the extents in amounts, the completed
turn, the unit. The two are told apart by one test, *scale the world*: a reading is unchanged when every length is
multiplied by the same factor, a writing changes with it. And they are told apart by one quantity, V, the other party's
breadth: no reading carries it, and every writing needs it.

This paper brings together what each vantage holds, gives the geometry the reader has for free, and says exactly what is
added in becoming a writer. The reader's directions are laid by the uniform turn, whose law in the reading v/h is the
Cauchy, with its median at the corner v = h, its horizon never reached and no mean: an *address* given before anything
arrives. What arrives along an address is the *payload*, met. A rate is of a payload per an address. The writer has the
angle, the rate 1, and measures the reader's two sweeps from horizontal to vertical as π/2 (central) and 2/π (inscribed),
whose product is its own 1. The reader's own numbers are the rationals, which one length makes in finite steps; the square
roots need two lengths combined, and the transcendental numbers a limit no finite algebraic step reaches: π completes the
turn, e completes the scale, and both are the writer's. The reader meets such a direction whole; the writer needs the limit
to state it as a number. The passage from reading to writing is parallax: a second standpoint, the step between them,
places from crossings. An observer making that passage is writing: read and write are acts, not kinds of observer. And the
passage has degrees: V is learned in some unit, to some precision, for some things, never all at once.

None of the mathematics is new. What is offered is a division of it: which parts a standpoint has, which parts need the
whole, and what carries an observer from one to the other.

## 1. Two acts

Map a room without a ruler. Stand in a corner, look at each thing, and note where it is: so far round, so far up. You now
have every thing's direction and nothing's distance. A room twice as large, seen from the same corner, gives the same
notes; so does a room half as large. What you have is a picture, exact and complete in its own terms, with no size in it.

Now take one step, a stride along the wall, and look again. Each thing's two directions cross, and where they cross is
its place, in strides. The room has a shape and a size now, in your stride. Count the stride in metres, and the room is
in metres.

The first part is reading. The second and third are writing. The rest of this paper is about the line between them.

**Words.** The paper names acts, a *read* and a *write*, not two kinds of observer: one observer reads while it stands and
turns, and writes while it walks, counts, ranges or agrees a unit. *Read*, *reading* and *reader* are used as each sentence
needs (a reader is whatever is reading, for as long as it reads), and likewise *write*, *writing* and *writer*.

**Read and write in computing.** Computer science has used these words for longer, and the likeness is real. A computer's
read takes an address and returns what is stored there, changing nothing; that is this paper's split of address and
payload, met in hardware. A computer's write stores at an address a value that came from somewhere else; a write here
likewise needs an amount carried in from outside. But the two pairs part in five places.

- *Who lays out the addresses.* A computer's address space is laid out before anything is read: a known size, indices
  counted from 0 to N − 1, an end. That layout is a writer's work (an array whose `sizeof` is known is held by a writer).
  A reader's addresses are given by the turn, uniform by the turn's own measure, from home toward a horizon that is never
  reached; there is no N, no last address, and no end to fall off. What it holds is K, its own count (§6, "K and N").
- *What a read returns.* A computer's read returns an amount in a unit: bytes, a float, a count. A read here returns a
  direction and the paint arriving along it, with every amount along that direction already gone. Nothing in it would
  change if the world were k times as large.
- *What a write changes.* A computer's write changes the memory, and the next read sees it. A write here states amounts
  (the room is 15 metres wide); it changes the world only when it is acted on, as moving the furniture is.
- *What stays the same.* A computer's read is repeatable: read the same address twice, with no write between, and the
  value is the same. A read here has a stronger sameness, across worlds: scale the world, and no reading moves.
- *Where caching falls.* In a computer, keeping a value read (a cache, a variable) is a write into another place. Here too:
  to keep a reading as a number, a length in a unit, a value in a table of known size, is to write it.

So the computing words are the writer's frame applied to both acts: memory is a written world, and a computer's read is
an address looked up in it. The read of this paper comes before any such layout; it is what a reader has when no one has
written the memory yet.

**The read.** A read is taken from one point, *home*, by turning there. The reader holds one length, H, which it chooses,
as you hold up your thumb: any value, since every reading is a ratio and H only sets the zoom, where its finest detail
falls. It does not hold the other party's breadth, V. Every reading is a direction, written [h : v] in homogeneous
coordinates, or v/h, the reading in its usual chart: h is how much of the thumb lies along the first axis, v how much of it
along the second, each between 0 and 1. A reading needs no division by the reader; the projection from home divides.

**The write.** A write holds what no standpoint gives: both hemispheres, so both signs of every axis; the extent of each
axis as an amount; the unit those amounts are in; the completed turn. Its frame is a box, a number line on each axis, every
point three amounts. Nothing in it is round, and nothing in it has a corner of a read's kind: the number line is
proportional everywhere, with no place where one unit gives way to another.

**The test.** Multiply every length in the world by k. A reading is unchanged; a writing is multiplied by k (or by a
power of k). This sorts every quantity, and it is the old line of dimensional analysis between the scale-invariant and the
scale-variant (Bridgman 1922; Buckingham 1914). The names *reading* and *writing* say more than the sorting: they name the
act that crosses the line (a function of invariants is invariant, so a writing needs an amount carried in from outside)
and the vantage that holds each.

**The second test.** Change what arrives, keeping the standpoint and the turn: repaint the world, move the light, replace
a wall by a row of trees. The *addresses*, the directions the turn lays down, are unchanged; the *payload*, what is found
along each, changes. The first test separates reading from writing; the second separates address from payload.

**V.** One quantity sits on the line between the two acts: V, the breadth of the other party, the mountain in the distance
that the thumb is held up against. Every reading is a ratio in which V cancels, so no reading ever carries it. To have V is
to have written: walked a baseline, counted a step, timed a pulse, or agreed a unit. A reader that comes to know V has not
read better; it has written. This is not a shortcoming of the reader. Its geometry needs V unknown: the horizon, the corner
as a median, the missing mean are all the traces of a breadth no reading holds.

## 2. What the reader has for free

**The thumbs pointed.** The reader has no circle. It points its crossed thumbs at the mountain, and that pointing
generates its own geometry: the corner where the thumbs cross, the fingers spread from it, near and far counted in thumbs.
What the reader holds is H, its thumb; never V, the mountain. A writer watching would say that a length held fixed and
turned about one end traces a circle, and would call that circle V = H, the writer's way of saying that the two axes of its
drawing are drawn at one length: the thumb equal to the mountain. We call it the *one-length circle*. It is the writer's,
held whole, with a circumference and an area. The reader does not draw it, set it or choose it; it points, and has the
turn.

**The uniform turn.** The reader's directions are laid by turning, and a turn measured by itself is uniform: equal turns,
equal shares. Nothing the reader does produces the directions; they are given by the geometry before anything arrives,
which is why we call them addresses. In the reading s = v/h the uniform turn over a quarter turn has the law

  (2/π) · 1/(1 + s²),  s ≥ 0,

the half-Cauchy. Its median is s = 1, the *corner*, where v = h. Its quartiles are √2 − 1 and √2 + 1. Its far end, s = ∞,
the direction [0 : 1], is the *horizon*, reached by no finite reading. It has no mean: averages of readings climb without
settling, by (2/π)·ln 10 for every tenfold further the readings run. Given the uniform turn, these facts hold whatever is looked at: a straight
wall, a row of trees, a curved hill, an empty sky. The wall's shape only decides where each direction meets it.

The constant 2/π and the quartiles' values are the writer's arithmetic for this law; what the reader has of it is the
order of its readings, the corner, and the directions themselves.

**Address and payload.** An address is a direction from home; a payload is what arrives along it. They share one thing, the
point where a direction meets the world. The world decides what meets each address, which thing is nearest and what it
sends back; nothing it does moves an address. Scale the world and no address moves. Change the world and no address moves.
Change the turn's standpoint and the addresses move, as a family: the Cauchy is carried into another Cauchy, its centre and
width the new standpoint's foot and height (m + iγ). This closure, under every operation on directions alone, is the law's
own; only an amount entering, an edge, a square, a sum of amounts, breaks it.

So the Cauchy is not a law of what is measured. It is the law of the uniform turn, the measure on the reader's addresses.
Practice already treats it so, taking its median and never its mean; this is the reason.

**The Cauchy, derived from H and from V.** The Cauchy is usually met as a family with two parameters, a location m and a
scale γ. Derived from what an observer holds, it comes in three forms, and the parameters arrive with V.

- *From one length.* Turn one length H, the thumb, uniformly. Its tip is at (H cos θ, H sin θ), and the reading v/h = tan θ
  divides H out. The share of a quarter turn passed before the reading reaches s is (2/π)·arctan s: the standard
  half-Cauchy, scale 1, median at the corner. No V appears anywhere, and H appears only in the tip's place, never in the law.
  The scale is 1 not because anything was set equal to anything, but because the reading is a ratio, and a ratio carries no
  scale.
- *From two axes.* Draw the second axis at a length V of its own. The drawn point is (H cos θ, V sin θ), its reading
  (V/H)·tan θ, and the law a Cauchy of scale c = V/H, its median at c, off the corner unless c = 1. Scaling the world
  leaves c unchanged, so c is not an amount; but it needs two lengths held against each other, as √2 needs the square's two
  sides, and holding both is the writer's.
- *From a line in the world.* A lamp turning uniformly lights a shore at distance d; its landings x = m + d·tan θ follow
  C(m, d), its quartiles at m ± d. Both parameters are amounts, moved by scaling the world. The angles follow the uniform
  turn whatever d is: nothing in the directions carries d. The scale appears only when the landings are measured on a ruler
  laid along the shore, which needs the shore found and walked.

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

The writer's circle holds amounts. A point is x = H cos θ, y = V sin θ; the curve is (x/H)² + (y/V)² = 1, round only when
V = H, the thumb equal to the mountain, and then x² + y² = r² with r an amount. It states the area πHV, the circumference and
every point's place, and all of them move when the world is scaled.

Divide the round circle by x²:

  1 + s² = (r/x)² = sec²θ,  s = y/x.

The ratio r/x of two amounts is not an amount, and no length is left. Two things follow. The density is the share squared:
1/(1 + s²) = (x/r)² = h², the reader's own share of its thumb, squared. And the even turn becomes the Cauchy: ds =
sec²θ·dθ, so dθ = ds/(1 + s²), and the uniform turn, read as s, is (2/π)·1/(1 + s²). The Cauchy is the circle's equation
used to carry an even turn into readings. It has scale 1 because every amount has been divided out, not because V was set
equal to H.

Divide the two-axis curve the same way and something survives: s = (V/H)·tan θ, with the law (2/π)·c/(c² + s²), c = V/H.
The amounts go and their ratio stays, and that ratio is the Cauchy's scale. With V unknown there is no c to leave behind,
and the law is the reader's.

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

**The missing mean, because the Cauchy is an address.** The Cauchy has a median and no mean. Over a quarter turn the readings
s = v/h up to S average (1/π)·ln(1 + S²) divided by the share they cover, and that climbs without limit, by (2/π)·ln 10 ≈ 1.47
for every tenfold further the readings run. This is usually told as a defect of the law. Read as an address, it is what an
address should do.

A mean is a sum of amounts divided by their count. An address is a direction, and directions have no sum: there is no
length along a direction to add. To average the readings v/h is to treat each direction as an amount laid along a line,
the chart in which the horizon sits at s = ∞, and the sum picks up that chart's far end. The missing mean belongs to the
chart that takes a direction for an amount, not to the directions. Other charts of the same directions do have means (the
bounded chart s/(1 + s) averages ½), and the order statistics do not depend on the chart at all: the median and the
quartiles are the same directions however the readings are written, because they commute with every increasing map of the
reading, and a mean does not. So the median is a property of the addresses and the mean is not; asking for the mean of a
Cauchy is asking an address for something only an amount has.

A mean of directions can be had, by a writer. Take each direction as a unit vector and add: over the uniform quarter turn
the average of (cos θ, sin θ) is (2/π)(1, 1), pointing at the corner, of length 2√2/π ≈ 0.900. The direction it gives is the
corner, the median again; its length is the writer's measure, π and all. And a writer holding a finite world, capped at an
extent M, has a Cauchy with a mean, (1/π)·ln(1 + M²) over the share below M, about 8.8 at M = 10⁶: finite, and set by the
extent, an amount that moves when the world is scaled. The mean appears only once an extent is written in, and its value is set by that extent, not equal to it.
A machine's Cauchy, capped by its largest number, has one for the same reason.

The payload has means where it is an amount: the light along each address, its colour, its brightness, all add. The
lighthouse's landings on the shore lack a mean although they are written in a unit, because they are still the turn's
addresses, carried onto the shore's ruler; the light that lands there is the payload, and it averages. What arrives can be
averaged; where it arrives cannot. Practice already takes the median of a Cauchy and never its mean: this is the reason.

**The payload is not lost.** The separation spends nothing of the payload: no part of it goes into making the addresses, so
all of it arrives, on addresses known before it came. The Cauchy then gives it back in four ways.

- *By its ratios.* Two payloads read against each other make a ratio, and a ratio is a reading. The light along one
  address over the light along another, one colour channel over another, the radius in one direction over the radius in
  another: each is a direction [p₁ : p₂] in the payload's own space, read exactly as an address is read, unchanged when the
  world is scaled. A shape about a centre, ln r = a₀ + f(θ), comes back this way whole: every mode of f from ratios of radii,
  exactly. Two detectors' signals read against each other are a direction too, and where the signals are like noise that
  direction follows a Cauchy: the payload read as a ratio is an address again. What the ratios leave out is one number,
  the payload's overall scale a₀, and that number is V again.
- *By dividing the address law out.* What is counted along the addresses is the address law times the payload's own
  weight, ρ(θ)·2/(π(1 + s²)). The address law is known before anything arrives, so dividing by it leaves the payload's
  distribution exactly, up to its total: the astronomer's flat field, importance sampling's 1/p. The median direction of
  what arrives is then the payload's median, at the corner only when the payload weighs alike on both sides.
- *By undoing the blur.* Seen from a height γ, the payload arrives smoothed by the Cauchy kernel, whose Fourier
  transform e^(−γ|k|) is never zero. Every mode survives, damped and not destroyed, and comes back multiplied by
  e^(γ|k|), noise with it. A box blur, the floor's, has a transform with zeros, and the modes there are gone for good.
  How fine a mode comes back is set by the resolution and the noise, which is how finely the reader draws, not loss:
  unique in principle is not the same as stable.
- *By averaging it.* The payload is amounts, and amounts have means: weighted by the known address measure, the light
  across the turn totals exactly wherever that total is finite, which is the payload's to say. The mean was never
  missing from the payload, only from the addresses.

What the payload carries along its address all comes back; its scale and its distance are V, and come back only by
writing. A known measure can be divided out and an invertible blur undone; a floor that discards cannot.

**The picture.** Hold a hand up to a stained-glass window, fingers spread between flat and upright. Each finger lines up
with a pane and is lit by its colour. The fingers are the addresses: wherever the hand is, the same fingers, spread the same
way. The colours are the payload: they change with the window. No colour carries a distance; to learn how far the window
is, you must walk.

**The reader never sees a shape.** A thing is, to the reader, the addresses it paints and the paint. Its shape is a radius
along each direction from its own centre, an amount, and amounts are removed before reading. Every way to a shape is a
writing: ranging, a counted step, a blueprint. This is not a shortfall to be made up by inference. The reader's side is
whole; the shape was never the reader's to lack.

**Passive.** The reader sends nothing. It is not a radar. A ranging instrument carries in the signal's speed and a clock,
two amounts, and so it writes.

## 3. Four pictures

Four pictures carry most of what the earlier sections say. Each shows what the reader has, what the writer adds, and where
V enters.

**The hand.** Hold up a hand, thumb out. The thumb is H: the one length the reader holds, its size chosen, setting only the
zoom. The fingers, spread from flat to upright, are the addresses. The reader does nothing to lay them; wherever the hand
is held, the geometry gives the same fingers spread the same way, evenly by turn, and read as v/h they follow the Cauchy,
half below the corner. The light that falls along each finger is the payload: it paints the fingers and changes with what is
in front of them, and no finger carries how far that light came. The hand moves two ways, raised from the ground toward
the vertical and turned round the horizontal, and the two are the altitude and the azimuth of §7. Hold
the thumb up against a mountain range, and the range spans so many fingers; with no V the reader draws the mountain at the
thumb's own size, and every amount it then reads is off by the one number it lacks, V/H. To learn that number it must walk
(§10).

**Two hands.** In space the window is held with both hands. One hand spreads its fingers from flat to upright, the
altitude; the other spreads its fingers round the horizontal, the azimuth. The two thumbs cross at a right angle (§7), and
where they cross is the corner, the triple corner of the wedge, where both read 1. Each pane of the window now lines up with
a crossing, one finger of each hand: the address is the pair of fingers, a direction of the wedge, (v/h, v₂/h). Each hand
alone gives its own sweep, the one-dimensional Cauchy with its own corner; the crossings together give the two-dimensional
Cauchy. For every crossing to hold the same share of the window, the round hand spreads its fingers evenly by turn and the
upright hand evenly in height, not in angle (Archimedes' hat-box, Lambert's map); spread both evenly by angle and the pair
neither hand reads leaves its corner. The coloured light at each crossing is the payload, as before, and still no colour
carries a distance. Two hands add no second length: both thumbs are the one H, the same size, and the right angle between
them is a quarter turn, no amount.

No one holds a window this way; the picture is not about hands. What it shows is that the reader's space in three
dimensions is not Cartesian. There are no three axes of amounts, no X, Y and Z counted out from an origin: there is one
thumb, crossed with itself, and two sweeps of fingers from where it is held. Everything else, the corner, the near and far
fields, the Cauchy over the crossings, follows from the thumb. The writer's cube (below) is the Cartesian frame, and it is
the writer's.

**The lighthouse.** A lamp turns evenly and throws a flash along each direction. Where a flash lands on a straight shore, the
landing x obeys (x − α)/β = tan θ, with α the foot of the lamp on the shore and β its distance from it. The angles are the
lamp's addresses, laid evenly by its turn, whatever shore there is; the landings follow a Cauchy because the shore is
straight. Within each flash the path to the shore cancels: the angle carries no distance. The lamp's own corner is the flash
halfway through the quarter turn, and it lands at the foot plus one distance, the shore's corner, only if the shore is
measured at the sea's own scale; drawn on a ruler c times the sea's, the halfway flash lands at arctan c, and the corner
slides off. To read β from the landings, take half the spread between the quartiles; never the mean, which the landings do
not have. That reading is a writer's: it needs the shore found and a ruler laid along it. The lamp is the reader, its turn
the addresses; the shore is the writer's line, where V comes in as the scale.

**Mercator's map.** A navigator wants a straight line on the chart to be a constant compass bearing. On a chart whose
parallels are spaced so that a degree of latitude is drawn c times a degree of longitude at that latitude, a bearing ψ is
drawn at tan ψ′ = tan ψ/c. Bearings are true everywhere only at c = 1: both directions drawn at one length at every place,
which is Mercator's chart (1569). It keeps every direction and pays in area, stretched by sec² of the latitude, so Greenland is
drawn about as large as Africa, which is some fourteen times its area. The chart that keeps areas instead draws c = cos² of
the latitude and gives up the bearings. Neither is wrong; each keeps what it was made to keep, and only the globe, the
writer's whole, keeps both. Mercator's map is also not the reader's picture. It is a chart of the whole field, every stretch
from a count of thumbs to twice it alike, with no focus; the reader's picture is the turn, proportional in direction
and finest where it looks.
Bearings are the reader's; areas are amounts, and the writer's.

**A moving sky.** An observer moving through a field of stars at a fraction β of the speed of light sees each star change
in two ways, and special relativity already writes them as two formulas. Where the star is seen moves: aberration, cos θ′ =
(cos θ + β)/(1 + β cos θ), the same at every frequency. On the stereographic chart of the sky it is z ↦ z/k, with k = e^η
and η the rapidity, a Möbius map of the directions; it moves addresses and carries the Cauchy's family onto itself. A sky
uniform in the stars' own frame is seen as the spherical Cauchy, its density D²/4π. What arrives at each place changes: the
Doppler factor D = √(1 − β²)/(1 − β cos θ′) scales each photon's energy and its rate of arrival, a weighting of the payload
that moves no address. For a sky uniform in its own frame, counting total power, the familiar D⁴ brightening ahead is D² of
addresses crowding and D² of payload. Laid on ξ = −ln tan(θ/2) (the pseudorapidity), aberration is a slide by η, so a
reader holding directions alone reads its own rapidity, with no clock, no frequency and no speed of light carried in,
provided every source is counted whatever its brightness and the sources are uniform in their own frame. That is a reading.
To state the speed in metres a second needs the speed of light carried in, and to read D as the shift of a spectral line
needs the line's rest frequency, a known kind of atom: both are writings. The theory makes the split in its formulas
without naming it; the reader's part is the directions, the writer's the amounts.

## 4. Rates, not angles

A carpenter calls a roof "six in twelve". A road sign says "10%". A ramp is built "one in twelve". None of them says an
angle. The pitch is a ratio, had at once with a level and a tape; the degrees are a share of the whole turn, and to state
one you must hold the whole turn first.

**A rate is of something per something.** The *per* is the sweep's: an address. The *of* is the payload: what arrives
there. A reader reads payload per address. The Cauchy is the law of the per against itself: a speed of the turn through
the readings, with no payload in it.

**The writer's rate is 1.** The angle is arc per radius, measured against the completed turn; the chord between home and
the far end of a quarter turn is held as a straight line of length 1. That is the writer's rate.

**The reader's sweeps, as the writer measures them.** A hand swept from horizontal to vertical can pivot two ways. From the
centre of the circle on the chord (the *central* sweep), the hand turns twice as far as its direction does; arc over chord
θ/sin θ runs from 1 to π/2 as the sweep reaches the far end. From home on the circle (the *inscribed* sweep), the ratio
chord over arc sin θ/θ runs from 1 to 2/π, approached at the horizon and never reached. Their product is 1 at every θ.
These are the only two standpoints from which equal turns cut equal arcs (Euclid III.20: the inscribed angle is half the
central). So the sweep from horizontal to vertical comes at π/2 or 2/π, never at 1; 1 is had only by joining both, which is
the writer's join. Euclid's theorem, the two reciprocal ratios and the writer's rate of 1 in radians are three things that
correspond here, not one theorem. And π/2 and 2/π are the writer's measure of the reader's sweeps, not numbers the reader
holds: π is the total of a completed turn.

**The corner, where three meet.** At v = h three things coincide: v fills as fast as h empties; the reading v/h is 1, the
writer's 1; and 1 is the geometric mean of π/2 and 2/π, the fixed point of the reciprocal that exchanges the two sweeps.
The running rates there are 1.1107 and 0.9003, not 1. The corner is a meeting, not a rate.

**Tangent and arctangent are the writer's tools.** They convert between a direction and an angle, a share of the whole turn.
The reader never needs them. It composes directions by tangent addition,

  (a ⊕ b) = (a + b)/(1 − ab),

which takes ratios to ratios; it turns a reading over, s to 1/s; it orders readings. That is enough for everything a reader
does. The algebra of the tangent is the reader's; evaluating tan or arctan at an angle is the writer's.

**Two 1's.** On the axes, the three ways to measure a direction of the square agree: the largest component (the cube's), the
sum h + v (the diamond's) and the length √(h² + v²) (the circle's) all give 1. At the corner they part: 1, 2 and √2. A 1 needs
a measure. The writer cannot choose the measure by fiat; the turn picks the round one, and √2 is the geometric mean of the
other two (Hölder: ‖x‖₂² ≤ ‖x‖₁‖x‖∞, with equality on the axes and the corner's diagonals).

## 5. Which numbers belong to whom

**One length makes the rationals.** From H alone, counting thumbs, taking twice a thumb or half a thumb and taking ratios
of thumbs to thumbs give rational multiples of H and nothing else. The reader's operations on readings, the reciprocal,
tangent addition, the order, keep rationals rational. The corner is 1. This is the reader's arithmetic, and it is enough.

**Two lengths make square roots.** √2 first appears as the diagonal of a square, the length of [1 : 1]: Pythagoras combines
two independent lengths through their squares, which needs two axes held at once. This is where the Greeks met
incommensurability. On one line, from one unit, it never happens. Bisecting a direction is of this kind: the reading
halfway to s is (√(1 + s²) − 1)/s, a square root of two lengths combined. Halving a length is the reader's; halving a turn
is the writer's. Square roots, nested as deep as one likes, are what two lengths and a straight edge and compass give: not
every algebraic number (the cube root of 2, which doubles a cube, is beyond them; Wantzel 1837).

**A limit makes the transcendental numbers.** The algebraic numbers are closed under every finite operation: add, subtract,
multiply, divide or take roots of them, any finite number of times, and the result is algebraic. So a number that is not
algebraic is reached by no finite algebraic step, and as a number it is had only through a limit, by one for whom that
infinity is finished. It may still have a short name (tan 1, or π = 4·arctan 1); the reader meets the direction tan 1
whole, and only stating it as a number needs the limit.

- *π completes the turn.* The reader meets the corner as s = 1, exactly. Its angle is π/4 = 1 − 1/3 + 1/5 − …
  (Madhava, Gregory, Leibniz), every partial sum a fraction, none of them π/4. Machin's identity shows the split with no
  rounding: the direction 1/5 composed with itself four times, by tangent addition, is 120/119, and 120/119 less 1/239 is
  exactly 1, the corner. That much is finite, rational and the reader's. The number π comes next, from the arctangent's
  series. Viète's product shows it from the other side: 2/π is a product of nested square roots, each algebraic, the whole
  only in the limit.
- *e completes the scale.* The reader counts sizes in thumbs: a thing 8 thumbs away is past two, four and eight, exactly.
  That count as a continuous quantity is the logarithm, and to give it a value is to choose a unit and finish a series:
  from one count of thumbs to twice it is ln 2 = 1 − 1/2 + 1/3 − … nats. e itself is Bernoulli's limit, a coin lent at a
  hundred per cent compounded ever more often, (1 + 1/n)ⁿ, or 1 + 1 + 1/2! + 1/3! + …: every term a fraction, the number
  only at the end.

The reader's two ignorances, after Jaynes (1968), are which way it faces and how large things are: turns and rescalings.
Each is a one-parameter group with an exponential map. Turns close, so their map has a period, 2π. Rescalings never close,
so their map has no period, only a base, e. π is what is needed to say that the turn comes back; e, to say how the scale
goes on. The complex logarithm puts them in one line, ln z = ln r + iθ: the scale on the real part, measured in e's unit,
the turn on the imaginary part, measured against π's total. They meet at e^(iπ) = −1, the writer's notation for the far end
of the reader's sweep, which the reader holds as the finite pair [0 : 1]. It was through that meeting that Lindemann proved
π transcendental (1882): a power of e with a nonzero algebraic exponent is never algebraic, and e^(iπ) is −1.

**π with the address, e with the payload.** The two parts of ln z = ln r + iθ are the two sides of this paper. The
imaginary part is the address: turns act on it alone. The real part is the payload's size: scaling the world acts on it
alone, sliding ln r and leaving θ where it was. So π belongs with the address and e with the payload, and they are not
alike. The address coordinate closes, so it has a total, and π is that total in the unit the exponential sets; nothing can
choose it away. The payload coordinate is an open line with no total and no natural size, so nothing on it marks a place;
its base is a convention (counting in thumbs, doublings serve as well), and e is the base that lets one unit serve both
coordinates, so that e^(iθ) is a turn of θ and e^t growth at a rate of one. That open line is why the reader never reads
a₀, the overall size: there is no mark on it to read against. One coordinate closed and its constant forced, one open and
its constant chosen: the asymmetry of address and payload, in two numbers. Both numbers are still the writer's; the reader
meets the closing and the openness, and states neither.

**Met, not made.** None of this keeps irrational or transcendental numbers out of the reader's world. A direction whose
reading is tan 1 is a direction like any other, painted, passed, ordered. The reader holds it as a pair and by its order; the
decimal 1.5574… is the writer's account of where it is. The reader meets these numbers and does not make them.

**A machine is a reader here.** Every floating-point number is rational, an integer times a power of two. The machine's π
is 884279719003555/2⁴⁸, within 1.2·10⁻¹⁶ of π and not π. Every operation a machine does on numbers is monotone and finite, so
order statistics come out as the true ones rounded, and sums of amounts do not. Where the infinity is a horizon, kept as a
pair [h : v] or as a turn, and the computation keeps to order, the machine is faithful. Where it sits in a sum of amounts,
the machine's Cauchy, truncated, has a mean that the true one lacks.

## 6. Near and far

**The crosshairs.** Cross the two thumbs (§7) over whatever is looked at. Where they cross is the corner: the thing there
reads one thumb up for one thumb along and one thumb across, v/h = v₂/h = 1, and it is drawn one thumb wide. That crossing
sets the near field and the far field. The near field is a single thumb, laid evenly: everything nearer than the crossing
gets its addresses in proportion, the first half of the thumb as much room as the second. The far field is laid in thumbs:
two thumbs, then four, then eight, each stretch the same number of addresses as the one before, out toward the horizon.
Move the crosshairs onto something else and the corner, and with it the split between near and far, goes with them.

**Counted in thumbs.** The reader's distances, as ratios d/H, in thumbs, are in proportion inside the corner and counted in
thumbs past it: one stretch from one thumb to two, the next from two thumbs to four, then four to eight, each holding the
same number of addresses. This is the logarithm as the reader holds it: a count, not a value. The writer's formula for it
is 1 + ln(d/H), or 2 − H/d on a lay that keeps all of reality within two thumbs. There is one corner, the split between the
near field and the first stretch, one thumb to two; past it the stretches are plain, with no corner of their own.

**H is a zoom.** The reader's addresses are finite: some count K, which comes before H. H, the thumb it holds up, decides
how K is split. Half the addresses lie inside H at every H; a small H makes the near ones fine and puts more of the world
past the held edge; a large H does the reverse. No H holds everything. The best H for a thing is the one that puts it at
the corner, where the reader's relative grain is finest. That is why the corner follows the focus: what is looked at is
drawn one thumb wide.

**K and N.** Computer science has two letters for this, and they sort the acts as well as anything. N is how many items
there are; K is how many are held. To know N is to know the whole: its extent, V, and how much is in it. That is writing,
and only a writer has it. A reader never knows V, so it never knows N; what it knows is K, its own count of addresses,
fixed before H is chosen. The Cauchy is what goes between them. It lays the reader's K addresses over a world of any size,
the near field in proportion, the far field in two thumbs, four, eight, and everything past the last address on the one
address at the horizon. Double N and the reader's view does not change; make N unbounded and it still does not change (an
infinite star field browsed at N and 2N shows the same view, apart by less than 10⁻⁷ at N = 2⁴⁰). So the Cauchy is a cull:
whatever N is, the reader's work is K, O(K), and for a fixed K it does not grow with N. What the cull gives up is sameness.
A writer who knows N can hold every item as 1/N of the whole, all alike, on a number line with no corner, and no item has
an advantage over another, because no standpoint is favoured: there is none. A reader's K is spent unevenly, finest at the
corner and coarser each stretch of thumbs away, and that unevenness is the vantage: what is looked at gets the most.
Knowing N buys equality; holding only K buys a standpoint, at a cost that does not grow with the world.

**The far field in proportion.** The number line keeps the far field proportional everywhere. That is one of the writer's
capabilities, useful wherever readers with different H (different thumbs) must agree about far things, since the number
line has no corner to disagree about.

## 7. Three parties, the reader's sphere and the writer's cube

With a third party, V₂, the reader turns two ways: up from the horizontal (altitude) and round it (azimuth). These are the
horizon coordinates of astronomy. Its directions fill one octant, the *wedge*: [h : v : v₂], two numbers a direction. The
uniform measure over the octant's area is uniform in azimuth and in height (Archimedes' hat-box; Lambert's equal-area map),
and its law in the readings (v/h, v₂/h) is the two-dimensional Cauchy, 2/(π(1 + a² + b²)^(3/2)). Every pair of parties is at
its own corner, half its readings on each side; the near field in both readings is a third. The triple corner,
h = v = v₂, sits at azimuth 45° and altitude 35.26°, not at either sweep's 45°.

**The wedge is the writer's; the reader has a tunnel.** The wedge, an octant of directions with its faces, its edges and
its triple corner, is the writer's description of the reader's geometry: drawn whole, from outside, at once. The reader
never holds it. What the reader has is what its crossed thumbs give where it looks: a tunnel of addresses about the line of
sight. Laid out as readings, as on a screen held square to the look, the directions crowd toward the line of sight and thin
out on every side by the Cauchy, 1/(2π(1 + r²)^(3/2)) per unit of the screen at r thumbs off the line of sight (the whole
hemisphere in front; over the wedge alone, a quarter of the screen, the same law reads 2/(π(1 + a² + b²)^(3/2))), toward a
horizon they never reach. All of it is generated from the thumb; none of it is stored. As the reader sweeps, the tunnel
turns with the look, continuously and without a seam, so whatever it looks at is at the tunnel's centre with the finest
addresses, and each address is exact, given by the geometry, not computed. That is the reader's fidelity: perfect wherever
it looks, because it is wherever it looks. The wedge, the octant and the sphere are what a writer draws to describe that
tunnel from outside.

**One thumb, two thumbs.** In the plane the reader holds one thumb at arm's length: H, square to the line of sight, and one
reading, v against h. In space it holds two thumbs crossed at a right angle, both square to the line of sight: one reads
up, v against h, the other across, v₂ against h. The pair (v/h, v₂/h) is a direction of the wedge; each thumb alone reads
the one-dimensional Cauchy with its own corner, and the two together the two-dimensional Cauchy above. Two thumbs add no
second length: both are the reader's own H, so no breadth for either party enters, and what a writer would write as V = V₂
= H is the two thumbs being the same size. The triple corner is where both read 1. The right angle between them is no
amount either: it is the quarter turn that takes one thumb onto the other, unchanged when the world is scaled. So the
dimension, counted from a standpoint, is the number of transverse facings, a thumb for each direction square to the look:
one in the plane, two in space.

**The writer's cube.** The writer's frame with three parties is Descartes's: X, Y, Z, three number lines, every point three
amounts. It reaches the reader's directions only with H and the angles: X = H·cos a·cos ψ, and so on.

**The sphere is the writer's picture of the reader.** Every direction about a point at radius H, one thumb, is a sphere,
and it is the writer who draws it. The reader holds directions and reads them with the Cauchy; it never holds the sphere
whole. Placed together, the corner of the reader's wedge points at the vertex of the writer's cube. With the cube outside
the sphere, touching it at the ends of the axes, the picture is the inscribed sweep's; with the cube inside, its far corner
on the sphere, it is the central sweep's (Thales' circle through home, the ends and the far corner). The hemisphere's 2 and
½, like π/2 and 2/π, are the writer's measure.

**What survives in space, and what does not.** In the plane, one law plays four parts: the image of the uniform turn under
a Möbius map, harmonic measure, the powers of the standpoint, and the two sweeps' rates. On the sphere they part, and turns
of space do not commute. What survives is the split between address and payload, the corners, and the wedge seen from home.

## 8. From reading to writing

**Parallax is the passage.** One standpoint gives directions and a frame, and no size: every ghost of the room, twice as
far and twice as large, gives the same readings. A second standpoint adds a second variable, the step between the two. Each
point, matched in both looks, is then two rays crossing, and its place comes out of the crossing, in the step's length; the
step's length in any other unit is what a writer carries in. More standpoints give every place seen. This is how a reader
reconstructs the writer's cube, and while it does, it is writing: it has moved, joined its standpoints and holds what no
one standpoint holds. When it stops and looks again, it reads. A read and a write are not two kinds of observer; they are
what one observer is doing.

**Parallax is a sum of reads.** Put the two standpoints a step apart and let each read a point in its h/v chart along
the step, cot a from one end and cot b from the other. Then cot a + cot b is the step over the point's distance from the
step's line: the depth is the reciprocal of a sum of two reads. Those are the two operations the Cauchy is closed under,
the sum (a relay of standpoints, their points m + iγ adding) and the reciprocal (the exchange). So parallax never takes
a read out of the family. If each read is uncertain as a read from a height γ is (the uniform turn's law about the true
direction), and the two reads' errors are independent, each is a Cauchy point w = (c + iγ)/(1 − iγc) in that chart, c
its true value, and the depth is exactly a Cauchy whose point is the same triangulation done on the two points:
D = B/conj(w_a + w_b), B the step. That holds at every γ, not only for small errors; rays that do not meet ahead are
part of the same law, as negative depths. At the pair's corner, the circle on the step, the depth's point stays at the
true distance d, turned by twice the read's error angle: D = d·e^(2i·atan γ). Two things leave the family, and each can
be seen in a line. The place across the line of sight is a ratio of two sums, −1 + 2·cot a/(cot a + cot b) in
half-steps; its density over each standpoint is a read's density at zero times the sum's missing mean, so it is infinite
there, where a Cauchy's never is. And when each standpoint reads only a quarter turn, the sum of two half-Cauchys has
density (4/π²)·s near zero, where every half-Cauchy's is positive; so the depth's tail falls as 1/d³, not 1/d², and that
depth has a mean. And repeating the reads, the mean of the reciprocal depths gains nothing, while their median narrows.
Parallax is the Cauchy's own composition, carried across two standpoints; the step is the one amount in it. (Checked in
PXS, `plans/pxs-plan.md`.)

**Turning teaches the addresses; walking teaches the world.** A standpoint has two motions, a turn about itself and a
step along a straight line. A turn moves every direction by the same angle, near and far alike, so nothing shifts against
anything else: it gives the frame, the corner where the thumbs cross and the Cauchy of the fingers, and these are the same
in every world. A reader that only turns learns its own addresses and nothing about what is out there; what meets its
fingers changes, and a colour carries no place. A step is the first motion whose effect depends on the world: near things
cross the fingers faster than far ones, and that difference is parallax. Any motion of a standpoint is a turn and a step
together (a turn about any point but the standpoint carries the standpoint along a chord, and the chord is a step), and only
the step's part places anything. The straight line walked is the writer's own: count it in a unit and every place found
from it is written.

**Motion, read.** A thing coming toward the reader is read at its edge: x, the thing's breadth against its distance, the
reading v/h of the line to its edge, and that reading grows. The reading over its own rate of growth, x/ẋ, is the time
until the thing arrives, if it keeps coming as it comes: the breadth cancels, and so do the distance and the speed. Lee
(1976) proposed that a driver braking reads exactly this, and the rule he found is a reading too: brake so that the time
to contact shrinks no faster than half a tick a tick, τ̇ ≥ −½, and the car stops at the thing, since at τ̇ = −½ the
distance it needs to stop is the distance it has. Two limits keep this honest. The time comes out in the reader's own
ticks, as places come out in its own thumbs; seconds are a writer's unit, carried in. And one stream cannot tell a thing
coming nearer from a thing growing where it stands, since both raise x alike; a neighbour at the same depth, read at
once, tells them apart, approach moving both readings and growth one. The rate at which the reader turns cancels from
every reading. A speed in metres a second is a writing twice over: a metre and a second, both carried in.

**Knowing V comes by degrees.** The crossing is not a switch thrown. It has three counts.

- *In what.* Two standpoints a step apart give every place in that step. If the step was H, one thumb, places are in thumbs
  and V is written as V*/H. Only a step counted in an agreed unit gives an amount, and that is the one rung scaling the
  world moves.
- *How well.* The place's error per unit of angular error is least when the thing sits at the pair's corner, the circle on
  the baseline, half the baseline equal to the distance. Elsewhere the error stretches as d/(B/2). Past about B/ε, with ε
  the smallest angle the reader can tell apart, the thing is a direction alone.
- *Of which things.* So one observer, from the same two standpoints, knows V for near things and does not for far ones.
  Knowing V belongs to a thing at its distance, not to the observer.

More standpoints and longer baselines narrow the band; nothing closes it. The writer who holds V exactly, the vantage this
paper calls the writer, is the limit of the passage, not a stage of it, just as π is the limit of its approximants and not one
of them.

**The thing itself as H.** The thumb can be set to the very thing whose size is wanted, in two senses. *As the unit*: the
thing is drawn at one length, its V is 1 by choice, and nothing about it is found; what is found is everything else in its
units. Its own two ends become the baseline and the reader is the point placed: an angle α across it, centred, puts the
reader 1/(2·tan(α/2)) of its breadth away, from one look. *As the focus*: the reader keeps its thumb and chooses a baseline
that puts the thing at parallax's corner, half the baseline equal to the distance, where the error is least. That needs the
distance roughly first, so it is done in passes, each baseline set from the last rough reading.

**A survey.** Snellius (1617) and Roy (1784–85) wrote whole countries this way: thousands of angles read, one base walked
and counted. The angles are readings; the base is the one writing; every side of every triangle is then in the base's unit.
A second base checks the first and adds no scale.

**Recovered, by writing.** A reader can recover a thing exactly, its shape, its places, even its size, and still partially. A
loop that closes shows that the routes taken agree; it cannot show that no route remains untaken. Completeness is never a
reading. What recovers the thing is not reading harder but the passage through standpoints, and in that passage the observer
is writing.

## 9. What a blueprint adds

Ratios suffice for a great deal. A tower of ratios, each storey read against the next, holds a building, its rooms and their
things with one amount at the top. A loop of ratios checks itself. A reader builds with ratios alone and never needs a unit,
until one of these is wanted:

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

**From the standpoint.** The range's ends sit at ±45°: the pair (half-width, distance) is at its corner. Of thirty-six fingers
spread evenly over the half turn, eighteen land on the range. Scale the world by a thousand and nothing in the view moves:
still 45°, still eighteen fingers.

**Mountain equals thumb.** With no V, the reader drawing the range at its own H reads it one thumb wide at half a thumb
away. This is the writer's circle, V = H: the thumb taken to equal the mountain. Every amount is then off by V*/H = 20, the
range twenty thumbs wide and not one, the same on both sides of the corner.

**The two sweeps, measured.** On the circle it draws about the thumb, the writer measures the central sweep at π/2 and the inscribed at
2/π; to the range's ends, 1.1107 and 0.9003. Their product is 1, the starting length returned, H in H. The mountain never
enters.

**Walk one thumb.** Step one thumb toward the range and read again. The half-angle's reading goes from s = 1 to s′ = 10/9. The
distance is d = H·s′/(s′ − s) = 10 thumbs, the range V = 2·s·d = 20 thumbs. In thumbs, exactly. Count the thumb in miles and
it is in miles.

**The mountain as H.** Make the range the unit: its ends at 90° across, the reader on the writer's circle drawn on it, half a range-width
from its middle, from one look. Or make the range the focus: a baseline of twenty miles puts it at parallax's corner, where
its error per step is least; one thumb walked has about ten times that error.

**In three dimensions: a tower and two thumbs.** Hold both thumbs crossed (§7), one reading up (v/h), one across (v₂/h),
and look at a tower off to one side. Its top reads (¼, ⅓): a quarter of a thumb up and a third across for every thumb
along the look. Its foot reads (0, ⅓). From one place that is all: two directions, no distance, and a tower twice as large
twice as far off reads the same.

Step one thumb across and read again. The top now reads (¼, ¼), the foot (0, ¼). Only the across thumb moved, by 1/12, so
the distance along the look is 1/(1/12) = 12 thumbs. Then the top is 12·⅓ = 4 thumbs across and 12·¼ = 3 up, and the foot
4 across and 0 up: the tower is 3 thumbs tall, 12 off and 4 to the side, in thumbs, exactly.

The up thumb did not move, and that is the gain of the second thumb. In the plane one step gives one change for one
unknown, the distance, and nothing is left over. In space each step gives two changes for the same one unknown, so one is
spare, and it must agree: a reading can move only along the line through where the step itself points (the epipolar
condition of stereo vision). A step across points straight across, so readings move straight across. Step one thumb
across and up together and both thumbs move by 1/12, and both give 12. Take the step for diagonal when it was across, and the up thumb, which did not move, says the step had no up in it: the misreading is caught.
Step one thumb forward instead and both readings grow by the same factor, the top to (3/11, 4/11): the tower slides
straight out from the middle of the cross, its up over its across still ¾, and either thumb gives 12.

Scale the world, the step with it, and no reading changes, so every place in thumbs stands. Count the thumb as 5 metres and
the tower is 15 metres tall and 60 away. The writer's one amount is still one amount; the second thumb adds no length, only
a check (`runs/two/two_thumbs.py`, exact).

## 11. What this changes

It changes no mathematics. It sorts.

- **Every reading is the reader's, every amount the writer's.** A result stated as a ratio, unchanged by scaling the world, is
  a reading; a result that moves with the world's scale is a writing, and needs an amount carried in. A Cauchy-type quantity
  is a direction; find the turn that lays it, and the amount that the payload carries is found separately.
- **The constants have owners.** π, e, π/2, 2/π, the hemisphere's 2 and ½, the Cauchy's normalizing constant, the logarithm's
  nats and the angle's degrees are the writer's measures of the reader's things. The reader's own versions are finite: an
  order, a count of thumbs, a corner, a composition by tangent addition.
- **The roles move.** No observer is a reader or a writer once and for all. It reads while it stands and turns; it writes while
  it walks, counts, ranges or agrees a unit. The passage between is parallax, and it comes by degrees.
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
directions, and its dipole is 2β, Ellis and Baldwin's 2, from the addresses alone (1984). A real census is cut at a
brightness, and the cut adds a term set by what arrives: the counts' slope and the sources' spectra, read from the same
catalogue. On Secrest et al.'s quasars (2021) four slices by brightness give one β, as one motion of the reader should;
slices by colour disagree, which no motion of the reader can do, so part of the dipole belongs to what arrives. The sort
does not settle where the dipole comes from; it says which part could be the reader's.

In a double slit lit one photon at a time, the fringes' visibility is at most 2hv, h and v the two paths' shares, and
the which-path predictability |h² − v²| (Greenberger and Yasin 1988; Englert 1996): full visibility only at the corner.
On Aspden, Padgett and Spalding's frames (2016) the shares give 2hv = 0.997 and 1.000, the pair at its corner, and the
measured contrast, 0.69 and 0.56, lies under that bound, short by the source. The bound is the shares', the geometry's;
how far below it a pattern falls is what arrives. None of the three is new physics. What the reading adds is where each
part lives.

**Where the ideas come from.** Jaynes's principle of transformation groups (1968, 1973) gives the method: the measure that an
observer's ignorance leaves unchanged. Poincaré's universe made a thousand times larger overnight (1908), undetectable from
inside, is the scale test; his distinction between representative and geometric space is the reader's and the writer's.
Leibniz's space as an order of coexistences (1715–16) is the reader's picture; Klein's programme (1872), geometry as the study
of a group, is the method's form. Gibson's ambient optic array (1979) is the stained-glass window. Bridgman and Buckingham
sorted quantities by scale long before. What is offered here is the division into two acts, the address and payload
inside a read, and what carries an observer from one to the other.

## References

- Abbott, R. et al. (LIGO, Virgo and KAGRA Collaborations) (2023). Open data from the third observing run of LIGO, Virgo,
  KAGRA and GEO. *Astrophysical Journal Supplement Series* 267, 29.
- Archimedes. *On the Sphere and Cylinder*, Book I.
- Aspden, R. S., Padgett, M. J. and Spalding, G. C. (2016). Video recording true single-photon double-slit interference.
  *American Journal of Physics* 84, 671.
- Bernoulli, J. (1690). *Quæstiones nonnullæ de usuris.* Acta Eruditorum.
- Bridgman, P. W. (1922). *Dimensional Analysis.* Yale University Press.
- Brinkman, T. (2026). *Observation from Somewhere: addresses given, payloads met.* Working paper, archived.
- Buckingham, E. (1914). On physically similar systems. *Physical Review* 4, 345–376.
- Ellis, G. F. R. and Baldwin, J. E. (1984). On the expected anisotropy of radio source counts. *Monthly Notices of the
  Royal Astronomical Society* 206, 377.
- Englert, B.-G. (1996). Fringe visibility and which-way information: an inequality. *Physical Review Letters* 77,
  2154–2157.
- Euclid. *Elements*, Book III, Proposition 20.
- Gibson, J. J. (1979). *The Ecological Approach to Visual Perception.* Houghton Mifflin.
- Greenberger, D. M. and Yasin, A. (1988). Simultaneous wave and particle knowledge in a neutron interferometer.
  *Physics Letters A* 128, 391–394.
- Hölder, O. (1889). Ueber einen Mittelwerthssatz. *Göttinger Nachrichten*, 38–47.
- Jaynes, E. T. (1968). Prior probabilities. *IEEE Transactions on Systems Science and Cybernetics* 4(3), 227–241.
- Jaynes, E. T. (1973). The well-posed problem. *Foundations of Physics* 3, 477–492.
- Klein, F. (1872). *Vergleichende Betrachtungen über neuere geometrische Forschungen.* Erlangen.
- Lambert, J. H. (1772). *Anmerkungen und Zusätze zur Entwerfung der Land- und Himmelscharten.* Berlin.
- Lee, D. N. (1976). A theory of visual control of braking based on information about time-to-collision. *Perception*
  5, 437–459.
- Leibniz, G. W., and Clarke, S. (1717). *A Collection of Papers … Relating to the Principles of Natural Philosophy and
  Religion.* London.
- Lindemann, F. (1882). Über die Zahl π. *Mathematische Annalen* 20, 213–225.
- Machin, J. (1706), in W. Jones, *Synopsis palmariorum matheseos.* London.
- Poincaré, H. (1902). *La Science et l'hypothèse.* Paris. (1908). *Science et méthode.* Paris.
- Roy, W. (1785). An account of the measurement of a base on Hounslow-Heath. *Philosophical Transactions* 75, 385–480.
- Secrest, N. J. et al. (2021). A test of the cosmological principle with quasars. *Astrophysical Journal Letters* 908,
  L51.
- Snellius, W. (1617). *Eratosthenes Batavus.* Leiden.
- Viète, F. (1593). *Variorum de rebus mathematicis responsorum liber VIII.* Tours.

Some details of the classical works above are given from memory and are to be checked against the texts.
