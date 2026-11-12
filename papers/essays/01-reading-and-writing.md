# Reading and writing

*The first of a series of essays on what can be known from where one stands. Draft, 28 October 2026.*

Some things you can know just by looking from where you stand. Others you can know only if someone hands you a
number. This essay is about the line between the two. It sounds like a small distinction. It turns out to sort almost
everything we measure, and it explains why a lone observer with no ruler can do far more than one would guess. It also
explains why one familiar curve, the circle, has a second life as a law of probability, the Cauchy distribution. In
that second life it needs no second length at all.

The ideas here are not new one by one. Pieces of them are scattered through surveying, perception, measurement theory
and the geometry of the circle, each seen from one side. The aim is to put the pieces in one place and show that they
fit.

One consequence belongs up front, because the words invite it. Put *read* and *write* side by side and anyone who has
programmed thinks of a race: a read and a write meeting on one thing, the answer depending on which came first. Here that
never arises. A read adds nothing, so reads taken in any order, or all at once, agree. What a read gives is a direction and
its heat; what a write states is the payload met along it, and writing the payload moves no direction, so no write runs
into a read. Computing has to engineer that separation; the geometry starts with it. In a programmer's words a direction is
an address and the payload the value stored there; the metaphor serves, so long as the heat under the address is
remembered.

A second consequence belongs up front too. The geometry has no memory, and its laws need none. A law says what any
two directions give together: join this slope to that one and get a third. It holds for every pair at once, and
nothing in it happened. That is how the geometry can hold a function like Euler's, which describes the composing of
any number of turns, without remembering a single turn. Memory is needed only for something else: which steps a
particular observer took, and so where it has come from. So there are three things, not two. The geometry, complete
with no memory and no unit. Keeping, which holds a history and still no unit. And the unit, where physics enters.
"Law" here means a geometric law, a relation among the directions of one read. Laws in general are many things, and
a physical law carries units; they are not a third kind beside reading and writing. That the geometry's laws are of
this kind may be why it needs no memory.

The plainest example is Euler's identity. The blueprint, which here means classical geometry with its view from no standpoint, brought in only for comparison, states it as e^(iπ) = −1, with an exponential, the number e and a
half turn measured by π. The same relation is there in a form that uses none of them: write a direction of slope s as
w(s) = (1 + is)/(1 − is), and w(s)·w(1/s) = −1 for every slope, a direction and its reciprocal; at the corner, i·i = −1.
The algebra is ordinary and the two forms are equivalent. The simpler one exists because it relates directions of one
read; a position, a total or a closing has no simpler read's form, because a read does not hold them at all. And the
blueprint's form holds something the read's does not, the join completed (the second essay, section 9).

---

## 1. Mapping a room with no ruler

Stand in a room you have never seen. You have no tape measure and no idea how big anything is. There is a table, a
cube on the floor, a ball on the table and a cabinet against the far wall. What can you find out?

Point at the corner of the table. You can say where it is: so far to your right, so far down. That is a direction, and
a direction is all a single look gives. Point at the top of the cabinet and you have another direction. Between the
two you have an angle. You do not have a distance. The table could be small and near or large and far. The same
direction comes back for a table twice the size at twice the distance, or half the size at half the distance. Seen
from one place, a room and every scaled copy of it give exactly the same view.

Now take one step to the right. You do not know how long the step is. Call it one step, and nothing more. From the new
place, point at the same corner of the table again. The two lines you have drawn, one from each place, cross at the
corner. Where they cross is the corner's place, measured in steps: so many steps ahead, so many to the side, so many
down. Do it for every corner you can see from both places, and the room comes out as a map. Every corner is placed,
every edge has a length, every object has a size, and all of it is in steps. The table is 1.71 steps long; the cabinet
stands 2.57 steps tall; the ball is 0.43 of a step across. Every one of those numbers is
right. Every ratio between any two things in the room is exactly the true ratio.

You have done all of this without a unit. The step was never measured. What you have is the room complete except for
one number: how long a step is. If someone tells you that your stride is seventy centimetres, the whole map turns into
metres at once, every length multiplied by the same 0.7. But the map was finished before anyone told you, and it would
still be finished if no one ever did.

This is the whole essay in miniature. There are two acts here, and they are very different, with a step between them.

The first act is **reading**. You read directions from where you stand. From two standpoints, joined across the step,
you have the room's shape and every ratio in it, in steps: what *Reads and Writes* calls an **extent**, unmoved when the
world is scaled, like a reading, but held by no single standpoint. Reading and placing needed no unit, and they gave you
everything except one number.

The second act is **writing**. To say how many metres the table is, you must be given an amount from outside your
readings: the stride measured once against a rule. Writing cost that one number, and nothing your eyes could do would
have supplied it. A write is exactly what scaling the world moves; the map in steps does not move, so it is not yet one.

The rest of the essay takes these two acts apart. They have a structure, and the structure has two sides.

*Demo: the room in ratios, steps 1–3: one place, one step to the right, the stride counted.*

---

## 2. Two questions, two acts

Every reading you could ever take can be sorted by asking two questions about it. Each question has two answers, and
each answer either ends the sorting or leads to the next question. So every reading lands in exactly one place, and the
places do not overlap. There are two of them: the blueprint's, which has no standpoint and is set here for comparison, and
the read's.

Before the questions, a little language. You, the observer, have a length of your own. It might be your stride, your thumb
held at arm's length, your eye height above the floor, or the length of a rod you happen to be carrying. Call it **H**; the
essays picture it as the thumb. You always have it, because it is yours. Anything else in the world, the mountain, the
table, the other end of a measurement, has a breadth of its own. Call that **V**; the essays picture it as the mountains in
the distance, the far thing the thumb is held up against. How far a thing reaches along your length is a share of H,
written **h**, a number between 0 and 1. How far it reaches along the other is **v**, also between 0 and 1. These small
letters are *relations*: how much of a length is filled, with no unit in them. The capital letters are amounts. Keeping the
two apart is most of the work.

Now the questions.

**First: is anything related to you at all?** If nothing is, if there is no h because nothing is set against your
length, then there is nothing to read. You have your own length and nothing to hold it against. Having a length is not
the same as having a reading. A ruler in a dark room measures nothing.

**Second: is the other's breadth V known?** If it is, the whole thing is in your hands: both lengths, both amounts, and
everything that follows from them. That is the **blueprint**. If V equals H in every direction, the whole is a circle, the
equation h² + v² = 1, held whole: the blueprint's circle is the thumb held to equal the mountain. If V is known but differs
from H, or differs from one direction to another, the whole is some other shape, an ellipse, a coastline, a floor plan, a
breadth given in every direction.

If V is not known, you have a standpoint, and what you have from it is a **read**. You are
somewhere, looking out, and what you have is what arrives at that place. It comes in two parts. One part is the directions themselves, the places on your view
where something can be: each one a ratio of v to h and nothing more. These are the *directions*, and the read weighs
them as a *heat*: hottest along the look, cooling toward the horizon, continuous, with nothing counted in it. The other
part is what arrives along each direction, its colour, brightness and texture, laid onto those directions: the *paint*.
The paint never comes without its direction, because whatever arrives arrives along some direction. The directions can
come without the paint: a direction along which nothing arrives is still a direction, with its heat. *The heat is given;
the paint is met.* Heat and paint are not two kinds of read.
They are two parts of the one read, and the geometry gives two ways of reading where the paint sits, which later essays call
the inscribed and the central sweeps.

| side | what you know | what you have | a picture of it |
|---|---|---|---|
| the blueprint | the other's breadth V, equal to H or not | the whole, as a circle or a shape | the equation h² + v² = 1; an architect's drawing |
| a read | your length H, and a standpoint; never V | the directions, and what arrives along each | a hand held up to a stained-glass window |

Each has a scene that fits it.

The blueprint's scene is the circle in a geometry book, centre, radius, the equation, every point at once; or an architect's
drawing, every wall drawn to scale, front and back, from no particular place, every length marked in one unit.

A read's scene is a stained-glass window seen from inside a church, with a hand held up against it, fingers spread.
Each finger points in one direction. The fingers are there whether the light is bright or dim, red or blue, or out
altogether. They are the places the colour can be put. They are not the colour. Each pane lights the finger it lines up
with, and the window tells you nothing about how far away the sun is. In space it takes both hands, thumbs crossed: not
three axes of amounts, as the blueprint has, but one thumb and two sweeps of fingers (the fifth essay).

### Things that look like a third act

People sometimes think of a case the two leave out. Each turns out to be one of the two.

- **You know V only roughly**, say "the mountain is somewhere between ten and thirty miles wide". This is a reading
  from a standpoint, with its one missing number known within bounds. The bounds narrow the guess; they do not change
  what was read.
- **Several observers.** Each has a standpoint of its own. What passes between them is a separate matter, which the essay
  comes to in section 6.
- **A system that changes over time.** At any one reading it is a read's or the blueprint's. An observer can pass from
  reading to writing, as the observer in the room did the moment the stride was measured; that is a write, made from a
  standpoint, and the blueprint has none.
- **Directions along which nothing arrives.** These are still directions, with their heat and nothing painted on them. That is a fact
  about what arrives, not about the vantage.
- **Your own length changes between readings.** This changes no reading. Every reading is a ratio, and your unit
  cancels from every ratio. Each reading is then a read of its own, and joining them is the business of several
  observers again.

The two are exhaustive. That is a strong claim, and it matters. It means that anything you could record about the
world can be asked: was this read or written? The answer settles what the record can and cannot contain.

*Demo: the blueprint's box, its three views: the blueprint's, a read's from home, and ranges.*

---

## 3. Reading and writing, sorted

Set beside the two acts of the first section, the two sides sort cleanly.

**The blueprint's shapes are amounts alone, the kind of thing a write states.** A blueprint states amounts: this wall is
four metres, that door is ninety centimetres. It holds every breadth, and holding every breadth means holding the whole, front and
back, from no standpoint at all. An architect's drawing is not a view from anywhere. It is what you would have if you
could stand nowhere and see everything. Its natural frame is a box, one number line along each axis, both signs, every
side an amount. Nothing in it is round, because roundness, as we will see, belongs to turning from a point, and the
blueprint has no point to turn from.

**The directions, their heat and their paint are reading alone.** They are what a standpoint has: directions, and what arrives along
them. No second breadth is known, and none is needed to read.

**The circle is the blueprint's, and the read's geometry looks just like it, which is why the whole distinction is so easy
to miss.** The circle is the most familiar object in mathematics. The blueprint holds it as an equation, h² + v² = 1, with V
known to equal H: the thumb held to equal the mountain. A read has no circle. The observer points its crossed thumbs (in the
plane, one thumb) at the mountain, and that pointing generates a geometry of its own, which section 4 will explain: a
corner where the thumbs cross, directions laid by turning, near and far read as ratios of the thumb. That geometry has every feature
of the circle except the circle. Because of that, the line between reading and writing runs straight through the middle of
the thing everyone starts from, and it is very hard to see. Classical geometry works almost entirely on the blueprint's side.
It never needs to say so, because the circle it begins with looks, from a standpoint, like what the pointing gives.

So the map is simple:

| what | whose |
|---|---|
| nothing related | no one's: nothing to read |
| the circle | the blueprint's: V = H, the thumb equal to the mountain; the thumbs' pointing gives its features, not the circle |
| any other shape, in amounts | the blueprint's alone |
| the directions, their heat and their paint | the read's alone |

### What writing needs

If writing is stating amounts, where do the amounts come from? Not from any reading, as section 5 will make exact. They
come from outside, and there are only a few ways they come.

- **A step whose length you count.** The stride in the room, measured once.
- **A size you already know.** A door is usually about two metres high; if you know that, every reading against the
  door becomes an amount.
- **A base you walk.** Surveyors lay a measured line on the ground and carry it through a network of angles.
- **A clock and the speed of a signal.** Radar and sonar time an echo and multiply by a speed someone measured before.
  Ranging is writing: the speed is the amount carried in.
- **A standard agreed beforehand.** The metre itself, the kilogram, the second: amounts kept somewhere and copied.

The philosopher Niels Martens, writing about mass, puts the point sharply. A magnitude like mass "can only be reported
or expressed, non-dynamically, in terms of how this magnitude relates to the magnitude of another particle having the
same determinable property." And of the unit we use to report it: "A unit is thus merely a relation—to a standard
reference body … in disguise." That is writing seen from the inside. Every amount is a reading against some
standard, and the standard has to be carried in.

### Two rulers

There is one more difference between the two sides, and it shows in the rulers each one uses.

A write's ruler is the number line. Its marks are evenly spaced, 1, 2, 3, as far as you like in both directions,
and every unit of length is like every other. That is exactly what you want for stating amounts: an amount is a count
of units, and counting needs equal units. The number line has no special place on it. The mark at 1 is just a mark.

A read's ruler, as later essays will show in detail, has a special place: the point where the thing you are reading
equals your own length, one thumb, where v equals h. Near you, inside that point, the read's ruler is proportional, like
the number line: one thumb laid evenly. Past it the ruler goes by ratios: a thing one thumb wide reads one in two, then
one in four, then one in eight, each stretch over which the reading halves holding as many places as the last. So far
things are laid by how many times farther they are, read as a ratio, not counted in units. A write, counting the same
stretches, says two thumbs, four, eight. Neither ruler is better. They are made for different acts. A write counts; a read
sees.

*Demo: one blueprint, and a read beside it, in two dimensions and three; reads and the counted walk.*

---

## 4. The circle without the V

Here is the part of the story that seems to me the most surprising.

Look again at the circle, the place where a read and the blueprint meet. The blueprint's circle is an equation in
two breadths. To write h² + v² = 1, and to mean it as a statement about lengths, you must know V and know that it
equals H. Two amounts, and a claim about how they compare.

A read has no V. More than that, it never comes to hold one. Every reading is a ratio of the thumb's own shares, and V was
never in it: not missing, never there. So no reading, however many, carries it. V against the thumb, V\*/H, is placed by
walking a baseline or counting a step; V as an amount is known only by writing: a step counted in an agreed unit, a
signal of known speed timed, or an agreed unit handed over, each an amount carried in from outside. An observer that comes
to know V has not read better. It has placed it by walking, or, with a unit, written it, and passed from reading to writing. Yet a read has the circle's geometry,
without the circle. Where does it come from?

It comes from pointing. Hold your one length, H, your thumb, up at the mountain, and turn it about one end, steadily, like
the beam of a lighthouse sweeping the sea, or your gaze sweeping along a row of trees. Drawn whole, the free end
traces a circle, for one simple reason: the length does not change as it turns. A read does not hold that circle.
Circles and spheres are the blueprint's; a read has a vantage, not a shape. It holds where the thumb points, and each pointing is a reading. Its geometry is what the pointing generates.

Now ask what is read as the thumb turns. At each moment the length points in some direction. The direction has an
across part and an up part, two shares of the same length: h across and v up. What is read is how they compare,
v against h. That is a slope, a direction, a ratio. Both of its parts are shares of the observer's own length. Nothing
about anyone else's size enters.

So far this is ordinary trigonometry. If the turn has reached an angle θ, then v/h is the tangent of θ. Here is the
step that matters. If the turn is steady, so that every angle is passed through at the same rate, then the readings v/h
are not spread evenly. They have a definite law, and that law is the **Cauchy distribution**.

The Cauchy is one of the most famous distributions in probability. It is also one of the most notorious, because it has
no mean. It turns up in physics as the shape of a spectral line. It turns up in statistics as the ratio of two
independent normal measurements. In the classic puzzle, a lighthouse flashes at random angles and you see the flashes
land along a straight shore; the landing points are Cauchy. It is usually presented as a law about something out
there: the line's shape, the measurements' ratio, the flashes on the beach.

Read from the standpoint, it is something else. It is the law of the directions themselves: the turn's own measure,
there before anything arrives to be measured. And it needs no V at all.

**The Cauchy is the blueprint's circle with the second breadth taken away.**

Consider what the blueprint's circle gives. On a quarter turn, from straight ahead to straight up, there is a special place in
the middle: 45°, where the across and the up are equal and v equals h. The quarter turn is symmetric about it. Swap across
for up and the near half lands on the far half, point for point. Half of the turn lies on each side.

Every one of those features survives in the Cauchy, and none of them needs V.

- **The middle is the median.** Half of the readings v/h lie below 1 and half above. The line between them is the place
  where v equals h, the 45° direction. We will call it *the corner*.
- **The halves are near and far.** Readings below 1, where v is less than h, are the near field. Readings above 1 are
  the far field. Each holds exactly half.
- **The swap is the reciprocal.** Exchanging across and up turns a reading s into 1/s, and it carries the near half onto
  the far half, point for point. The law looks the same from both sides.
- **The spread is even in turning, uneven in slope.** About 41% of all the readings lie within a factor of two of the
  corner, between a half and two. The rest thin out toward each end. Every equal step of turning holds equal weight;
  only the slope, read as a number, crowds and thins.

The blueprint's circle has every one of these properties, with V known. The pointed thumb has every one of them with V
unknown, and no circle. That is the sense in which the Cauchy is the circle without the V. It is the circle's geometry, the
corner, the halves and the swap, generated by one thumb pointed, with no circle held.

### What the missing V does

The second breadth is gone, but it leaves its mark, and the mark is the most famous thing about the Cauchy.

The blueprint's circle closes. Go far enough round it and you come back to where you started, at a place you could name in
amounts. A read's quarter turn ends somewhere else entirely: at straight up, where h has dropped to nothing and the
reading v/h has run off to infinity. That end is the **horizon**. It is a direction you can always point at, and it is
never a place. Nothing has a distance there, because a distance would need the very breadth that is missing.

Because the readings run off toward the horizon with nothing to cap them, the average reading never settles. Take more
and more readings and their mean keeps drifting upward. Each tenfold reach outward adds about the same amount again,
two over π times the natural logarithm of ten. This is the Cauchy's missing mean. It is not a defect of the law. It is
the trace of the missing V: the far end is a direction, not a place, and you cannot average your way to a place that is
not there. The median, sitting at the corner, is perfectly well defined. It is where v equals h, and it does not depend
on the size of anything.

There is a neat way to say all this. Not knowing the size of the far end is exactly what gives the corner its job and
creates the horizon. The read's geometry needs V unknown. The blueprint, holding V, has neither. Its corner is just a point
on the circle, and its circle has no horizon, because it closes.

### What it means

Three consequences follow, and each is a reason the distinction is worth having.

**First, the Cauchy is not a law of what is out there.** It is the measure of the directions a read has before
anything arrives, and before the size of anything is known. A spectral line, a lighthouse, a ratio of two measurements:
each of these has a Cauchy in it because each has a turn in it somewhere, and the law is the turn's. What arrives, the
brightness of the line, the strength of the flash, is painted on top.

**Second, it is reading through and through.** Section 5 gives a test: scale the whole world by any factor and see
what changes. Under that test nothing in the Cauchy moves. No V ever entered it, so there is nothing for the scaling to
grab.

**Third, it explains a habit that practice already has.** People who work with Cauchy-type quantities, spectroscopists,
astronomers and engineers, report the median and the half-width. They do not report the mean, and they are right. The
usual explanation is that the mean does not exist, which is true but not a reason. The reason is that the quantity is a
direction read from a standpoint. Its median is the corner, a feature of the geometry. Its mean would be an amount, and
there is no amount to be had.

One more point, about a phrase that appears often in the writings this essay draws on: "V = H". When the observer
points its thumb, one length is turned; the blueprint draws the circle its tip would trace, and describes it in its own
terms: two breadths, both equal to H, the thumb equal to the mountain. The phrase is the blueprint's name for that circle. A
read never sets V equal to H. It has no V to set, and no circle.

### What is old and what is new

Every piece of the mathematics here is classical. A circle needs one length: it is everything at a fixed distance from a
centre, and one length turned about its end traces it. The tangent of an angle turned uniformly is Cauchy; that is the
lighthouse problem of the Bayesian textbooks (Gull 1988; Sivia and Skilling 2006). Projecting the circle from one of its
own points onto a line, the stereographic projection, carries its uniform measure to the Cauchy, and the family is closed
under the Möbius maps of the line (Knight 1976; McCullagh 1996). (That is the circle's case. The sphere's even measure,
projected the same way, is not the plane's two-dimensional Cauchy; essay 13 says why.) Its median, its symmetry under the reciprocal and its
missing mean are textbook facts.

None of these mentions a second breadth, and none needs one. The slope v/h is already a ratio of two shares of one
radius, so the absence of a V is never remarked. What is new is the reading of what holds what: a read holds one
length and never has V, and each feature of the Cauchy is a feature of the circle that survives without V. The corner
is the median, the near and far halves are mirrored by the reciprocal, and the lack of a mean is what a read of directions
is, with no V in it to leave anything behind.
The blueprint, holding V, has its far end as an amount: no horizon, and the corner only a point. We did not find this
assembly in print; the pieces are classical.

The Cauchy's own story is long, and it has its own essay, the third: how its directions and their heat are kept apart from what arrives,
why it is the law a reasoner ignorant of scale must assign, and a second test to go with the one below. For now the point
is only this. The deepest piece of the read's side, the law of its directions, is the circle's geometry without the
circle: what one thumb, pointed, generates.

*Demos: one turn and one read (the ray and the radius meeting on one circle); sweeping from zero (the turn counted
against itself); the central reader, step 1 (the hand, its fingers laid by the turn, painted by the light).*

---

## 5. The test: scale the world

There is a simple test that tells reading from writing without asking how a record was made.

Imagine every length in the world multiplied by the same factor k, your own length included. The room is ten times
larger, and so are you, your stride, your rulers and the gap between your eyes. Then look at any quantity you recorded
before, and ask what happened to it.

- If it did not change, it is a **reading** or an **extent**. A direction, an angle, the place of the corner, held from
  one standpoint, are readings; the ratio of two lengths, a shape held up against its own average size, the map in
  steps, which need a second standpoint and the step between, are places. All of these come through untouched. (Reads
  joined can also give an order, as in essay 11, or a map carrying one look's directions to another's, as a turn or a
  boost does in essay 7; neither has a gap in space, and neither moves.)
- If it changed by the factor k, it is a **writing**. A length in metres, a distance on a map's scale bar, the size of
  the table in centimetres: all of these move, and each moved because somewhere an amount was carried in to state it.

Nothing length-like can do anything else. It is either fixed or it moves by k.

Try it on the room. The map in steps does not move: everything grew by k, your step grew by k, and every length in steps
is the same number as before. The map in metres moves: the stride was measured against a rule, the rule did not grow
with the world, and every length in metres is k times larger. One test, and it puts the map in steps with the readings,
unmoved (an extent, since it needed the step), and the map in metres on the writing side.

Three cautions keep the test honest. What it sorts is a variable, a quantity said of something named: this direction,
that gap, this light's frequency. A bare number is not yet sorted, and one thing can supply several variables of
different kinds. Second, the test crosses with a partner the third essay gives, change what arrives and keep the
directions, and the crossing has four boxes. On the geometry's side, unmoved is a reading or an extent and moved is a
writing, a distance in metres. On the payload's side, unmoved is a ratio of payloads, one colour channel over another,
and moved is again a writing, a frequency in hertz. So a writing is any amount in a unit carried in, whichever side it
is on, and being unmoved by scaling never shows by itself that a thing is a reading. Third, joining two reads does not
always give an extent. An extent has a gap in space in it. Which read came before which is an order, with no gap. And
turning the look, or changing one's motion, joins two reads by a map, one read's directions carried to the other's,
again with no gap; an angle of turn, or a rapidity, is a coordinate on such a map, inferred from the directions and
not itself a reading. Whether those three are all the ways reads can be joined is not claimed (*Reads and Writes* §1,
D4–D7; §12).

Try it on a mountain. A range of mountains twenty miles wide, ten miles away, seen against your thumb. Scale the world
by a tenth, so the range is two miles wide, one mile away, and your thumb is a tenth of its size. The view is the same.
Scale by a hundred, so the range is two thousand miles wide, a thousand miles away, and your thumb a hundred times as
large. The view is still the same. The mountain's width in miles changed every time. Its width against your thumb never
did.

Try it on the two sides. A read's directions, their heat and their paint never move: they are what a standpoint has, and a standpoint
has only directions. The blueprint moves by k in every number it states. The circle is the blueprint's, and it moves
with the amounts; the thumb's pointing, read as directions, does not.

In Euler's notation the test has a picture. Write a thing as a direction times an amount, r·e^(iθ), and take the
logarithm, ln r + iθ. With r in an outside unit, scaling the world by k slides the real part by ln k and leaves the imaginary part alone
(with r in thumbs, and the thumb scaled too, no point moves; only the thumb in metres does): the
imaginary part is the reading, differences of the real part are places, and the real part's zero, tied to a unit, is
the writing (the second essay, section 9; *Reads and Writes* §2).

This test is not new, and the essay claims no credit for it. Henri Poincaré imagined, more than a century ago, all the
dimensions of the universe becoming a thousand times larger overnight, and observed that "I shall not notice anything
at all". The physicist P. W. Bridgman, in his book on dimensional analysis of 1922, called the same fact "the absolute
significance of relative magnitude": the ratio of two lengths does not depend on the unit they are measured in.
The psychologist S. S. Stevens built his classification of measurement scales on which transformations leave a
statement unchanged. Louis Narens and others in the theory of measurement call a statement *meaningful* when it survives
the symmetries of what is being measured.

No real instrument reads purely: a sensor that samples, a register that holds a value, a machine that rounds it, has
already written something. The pure read is the limit. What the test offers a real instrument is a sorting, quantity by
quantity: scale the world, and see which of its numbers move.

What is new is a question these accounts do not ask: **who can apply the test, and from where?** Invariance under
rescaling has been treated as a property of statements, laws and scales. Here it is a property of standpoints. An observer
standing somewhere gets every invariant quantity for free and nothing else. Everything that moves under scaling is what
it would have to be handed.

*Demo: the mountain and the thumb, with "scale the world".*

---

## 6. What placing and writing cost: a count

If writing costs amounts carried in, it is natural to ask how many, and what placing costs on the way. The answer can be
counted exactly, and it is small.

Set up a simple scene: four objects, each with a size and a distance, and an observer who reads only directions, how wide
each object looks and which way it lies. Then ask, at each stage, how many numbers in the scene are still free: how many
could be changed without changing anything the observer has read.

- **One standpoint.** Each object's size and distance can trade freely: twice as big and twice as far reads exactly the
  same. With four objects there are four free numbers. From one place, nothing is written.
- **One step of known length,** known in the observer's own unit, say "one stride". Now every size and every distance is
  fixed, all of them, in strides. No free numbers are left. The step placed everything at once, in the observer's own
  length: places, unmoved by scaling, not yet writes.
- **One step of unknown length.** One free number remains: the length of the step. Everything is fixed relative to the
  step and nothing in strides, which is the room of section 1 before the stride was counted.
- **A second known step.** It adds nothing to the scale, which the first already fixed. It checks the first.
- **A second observer,** who has done the same in its own strides. Each map is complete in its own unit, but the two
  cannot be compared: one free number, the ratio of the two strides. **One number exchanged** between them, one observer
  telling the other the length of something both can see, removes it.
- **A public unit,** metres. One free number remains, the size of a stride in metres, until **one notch is agreed**:
  someone, once, measures a stride against the standard metre.

So placing costs one step for a lone observer, and one number exchanged for each further observer who must agree (a ratio
of two strides, itself unmoved by scaling); writing costs one amount more, the notch that ties them all to a public
standard. Each comes from moving or from exchanging; none comes from looking harder.

This kind of count has relatives. Buckingham's theorem in dimensional analysis counts how many dimensionless
combinations a physical law can depend on: the number of quantities less the number of independent units. Engineers
who reconstruct three-dimensional scenes from photographs know the result can be fixed only up to seven numbers, three
for where it sits, three for which way it faces, and one for how big it is; the last is the one a photograph cannot
supply. Physicists argue, sometimes heatedly, over how many fundamental units nature really needs. Each of these counts
the amounts for a theory, a law or a reconstruction. The count here is per observer. It says what each one must be
handed, and it says the answer is almost nothing.

*Demo: writing, step by step: the free numbers computed on the page as each step is taken: extents in the
observer's own H, then one agreed notch, the write.*

---

## 7. Many readings, one amount: the survey and the body

The division of labour between reading and writing is old, and it was worked out in practice long before anyone
described it.

When the Dutch mathematician Willebrord Snellius set out in 1615 to measure the size of the Earth, he did not measure
the hundred-odd kilometres from Alkmaar to Bergen op Zoom with a rod. He read the directions between church towers, which
his instrument wrote down in degrees, building a chain of triangles whose shape they fixed entirely, and then he measured one short base near Leiden. The base was
the one amount. It scaled the whole chain.

In the summer of 1784 the military engineer William Roy laid out a base on Hounslow Heath, west of London, about 8.4
kilometres long, and measured it with rods: first deal rods, which swelled in the damp, then glass tubes. It
took him most of the summer. From that one line, and thousands of directions read from hilltop to hilltop, each written down in degrees by a theodolite,
came the triangulation that joined Greenwich to Paris and began the Ordnance Survey. A second base, on Romney Marsh, was
measured later. It added nothing to the scale. It checked the angles that had carried the first base's length across
the country.

The costs fall exactly where the geometry puts them. Each angle needed an instrument and a place to stand. The base
needed the ground itself, crossed rod by rod, and one was enough to write everything. The finished map is a
plan in a unit, and its scale bar is the base.

### The body as the base

Every person walking about carries a base with them: the height of their own eyes above the ground.

The horizon of a flat floor lies at eye height. So on level ground, the horizon cuts every standing object at the same
height above the floor, one eye height up. A child shorter than you has their head below your horizon. A door taller
than you crosses it. An object exactly as tall as your eyes has its top resting on the horizon. The psychologist
H. A. Sedgwick worked out the relation in 1973: from the angle to an object's foot below the horizon and to its top
above it, its height over your eye height is fixed. It is a ratio of readings and needs no unit. As he put it later, without
the eye height "the vertical extents of all those objects relative to each other are still visible even though their
vertical extents relative to the observer are not." Take the eye height as the unit and every object is placed in eye
heights; supply it in metres and every object is written.

The body supplies such bases all the time. In a well-known experiment of 1984, William Warren asked short and tall
people to judge which stairs they could climb without using their hands. The boundary fell at the same proportion for
both: a riser about 0.88 of the climber's leg length. Short and tall people disagreed about the stair in centimetres
and agreed exactly about it as a ratio. Each was reading the stair against their own body, the one amount every person
carries.

So the carried-in amount does not have to be a metre rod. In perception it is the body: eye height, leg length, the gap
between the eyes, the length of a step. The observer reads everything against it and places everything in it; one amount
for it, in a public unit, writes everything.

*Demos: one's own height; walking the room.*

---

## 8. Towers of ratios, and closing a loop

Reading is not confined to simple maps. Ratios can carry whole hierarchies.

Picture a building with two rooms, A and B, and two things in each room. Read each length only against the length that
holds it: each room against the building, each thing against its room.

| what | read against | reading |
|---|---|---|
| room A | the building | 1/2 |
| room B | the building | 1/3 |
| the two things in A | room A | 3/4 and 1/2 |
| the two things in B | room B | 2/3 and 1/3 |

Seven lengths, six readings, and not a single amount. Yet any length can be compared with any other. The two things in
room A compare directly, 3/4 against 1/2, a ratio of 3/2. The first thing in A and the first thing in B compare through
the building that holds them both: 3/4 over 2/3 inside the rooms, times 1/2 over 1/3 between them, which is 27/16. Every
comparison is a chain of ratios through the tower.

Now carry in one amount, any one. If the building is twelve metres long, the first thing in A is four and a half metres
and the second thing in B is one and a third. If instead someone measures that second thing in B as one metre, the
building comes out at nine metres and everything else follows. One amount anywhere in the tower writes every length in
it. Scale the world, and every amount moves by k while the six readings stay put.

Real systems are built this way. A metric screw thread's profile is fixed as fractions of its pitch, the same from an
M6 bolt to an M36; the pitch is fixed against the diameter by a second standard; and one diameter in
millimetres writes all of it. Paper sizes work the same way. Every A sheet has its sides in the ratio of the square root
of two, so that halving it gives the next size down with the same shape, and one written amount, A0's area of one square
metre, fixes them all. A whole system of sizes is held in ratios, with one number at the top.

### Closing a loop

The tower has a weakness. Suppose room B's reading is wrong: it is really a third of the building, but it was read as
0.3. Then everything in room B is off by one factor, nine tenths. Everything inside B still agrees with everything else
inside B. Nothing in the tower complains. A tree of readings, each thing read against the one length that holds it,
cannot find its own mistakes.

A second route can. From a place where both are in view, read the first thing in A directly against the first thing in
B. The direct reading says 27/16. The chain through the misread room says 15/8. The two routes disagree, and the size
of the disagreement, 10/9, is exactly the misreading. That is a closure error, and it is why surveyors build networks of
triangles instead of chains, and why Roy measured a second base.

Two lessons follow, and both are about what an observer can and cannot know by reading.

**The observer does very little of the work.** The projection through its standpoint does the dividing; that ratios
compose by multiplying is the geometry's; whether two routes agree is the geometry's too. What the observer contributes is
position: the length it starts from, and the places it chooses to stand.

**Completeness is never a reading.** A loop that closes shows that the routes taken agree. It cannot show that no
route remains untaken. So an observer can find out that its account is incomplete, when two routes disagree, but it can
never prove that its account is complete. And even when an observer recovers something exactly, its shape, its places,
even its size in strides once a stride is counted, recovering it does not make its reads a blueprint. The blueprint holds the whole,
from no standpoint. An observer that arrives at the blueprint's answer got there by cleverness: where it
stood, which loops it closed, what it was handed. That is not a lesser achievement. It is a different one.

*Demo: a read is a slide rule: chains, loops and a misread link.*

**Two writes, and where physics enters.** "Write" has been doing two jobs in this essay, and they are worth telling
apart. One is the write of the scale: an amount in a unit carried in, the stride given in metres. Scale the world and
it moves. The other is the write of the relation: something kept, with no unit in it, a count of strides, a mark left
where one started, the room's shape put down in strides. Scale the world and it does not move. The first test of
section 5 tells the two apart; what tells a write of the relation from a read is only that it was kept, since a read
keeps nothing. Reading and the write of the relation are both prior to physics. Physics enters with the unit, and it
is orthogonal to the geometry: the geometry is complete without it, and physics, when it comes, assigns amounts and
moves no read and no relation.

**Steps, never positions.** One more thing separates the two acts, and it is the plainest. A sweep goes one way, from
home toward the horizon, and where it stops is the next sweep's home: every sweep resets. A tenth of a sweep, then a
fifth of a fresh one, then three tenths of another, is three steps, each from its own start, and nothing in any of them
says how far the three have come together. A position, "three fifths of the way round", is a total of steps from a
starting mark that was kept, and a read keeps no mark. The observer can go back: it faces the other way and sweeps, and
that too is a forward sweep. What it cannot do by reading alone is go back exactly to where it was; for that the steps
must have been kept, or a mark left at the start. So there is no circle anywhere in reading. A circle is one fixed dial
on which every sweep has its place; a read has a sweep, a reset and another sweep, and the dial appears only when
someone keeps the steps and lays them end to end.

**In physics.** Physics already runs both tests. Scaling the world is dimensional analysis (Bridgman's and
Buckingham's): a ratio unmoved by it is a read, and anything that moves had an amount carried in. Changing what arrives
splits one formula into its directions and its paint: aberration from Doppler, the quasar dipole's 2 from its x(1 + α).
What crosses between is a bridge, and there are few: a speed, a rest frequency, a baseline, a kind of star, a clock.
Sorted this way a parallax is an angle read and a distance written through the astronomical unit, and inverting noisy
parallaxes as if they were distances is Lutz and Kelker's bias, a read taken for a write. *Reads and Writes in Physics*
(`../reads-and-writes-physics.md`) goes through the known cases one by one, the failures with them. It claims no new
physics, only where each part of a known result lives.

---

## 9. Why the distinction is worth having

It would be easy to call all of this obvious. Of course angles do not depend on units; of course you need a ruler to
get metres. But the distinction does real work, and it is worth spelling out what.

**It finds mistakes.** The commonest is to take a reading for a writing. An observer with no outside amount does the only
sensible thing about the mountain's size: it takes its own length as the best guess, so that, in effect, mountain
equals thumb. That is a fine estimate, and it is the best available when nothing says bigger or smaller. It becomes a
mistake only when the estimate is read as a measurement, when "one thumb" is written down as "one mile". The same error
in a subtler form is well known in astronomy. A star's parallax is an angle, a reading. Its distance is that angle
turned into an amount using the size of Earth's orbit, a writing. The two have different statistics. An angle with
a small symmetric error becomes, once turned upside down into a distance, a distance with a lopsided error, and
catalogues that treat the distances as if they were the measurements come out biased (astronomers know the effect as
the Lutz–Kelker bias). Keeping the reading and the writing apart is most of the cure.

**It asks one question of any quantity.** Was it read or written? Was it a direction, something painted on a
direction, a shape held whole, or an amount stated in a unit? The answer says what the quantity can and cannot contain.
A record that scaling the world would leave unchanged cannot contain the world's size, however carefully it was made.
Measured data sorts the same way: the third essay's three cases (two gravitational-wave detectors, the quasar dipole,
photons arriving one at a time) each split into a part read as a direction and a part that is the payload's.

**It counts what must be brought in.** One step for a lone observer's places, one number exchanged for each observer
who must agree, one amount for a public standard. When a measurement fails, the count says where to look: at the amounts carried in, not at
the readings.

**It keeps reads from racing.** In computing, two operations can run together without a race when neither writes what
the other reads or writes (Bernstein's conditions, 1966): reads with reads are always safe, and the trouble is a read
and a write meeting on one place. The split here is that condition built in. Reads add nothing, so they never conflict
with one another; a write states the payload, and the payload is not where the directions are kept, so it moves none of
them. A system whose addresses move with their contents, an array that reallocates or a table that rehashes, has to
rebuild the separation by hand, with stable handles or copies kept for its readers. Geometry never had to: its directions and
their heat are given, and nothing writes to them. This is argued from a principle computing already holds, not proved anew.

**It explains how much a lone observer can do.** This is perhaps the most surprising lesson. With no unit at all, an observer
can map a room, size every object against every other, build a tower of units, check it by closing loops, and have the full
geometry of the circle, its corner, its halves and its symmetry, as the law of its own directions, with no circle held:
only its thumbs pointed. Almost everything comes free. What it cannot have is one number per agreement. The written world,
the map in metres, the number line, is a fine and useful thing: it lets sizes be stated before anything is
built, lets observers who never meet compare notes, and lets amounts be added up. But it rests on that handful of numbers,
carried in from outside, and the world as read was complete before they arrived.

Go back to the room. The map in steps was finished before anyone asked for metres. The metre was the one thing it had
to be handed.

---

## Sources

The essay draws on these; each is cited for something it uses.

- Bernstein, A. J. (1966). Analysis of programs for parallel processing. *IEEE Transactions on Electronic Computers*
  EC-15(5), 757–763. (When operations can run together without a race.)
- Bridgman, P. W. (1922). *Dimensional Analysis*. Yale University Press. "The absolute significance of relative
  magnitude", pp. 18–20 and 73.
- Buckingham, E. (1914). On physically similar systems. *Physical Review* 4, 345–376.
- Gull, S. F. (1988). Bayesian inductive inference and maximum entropy. In G. J. Erickson and C. R. Smith (eds),
  *Maximum-Entropy and Bayesian Methods in Science and Engineering*, vol. 1, 53–74. Kluwer, Dordrecht.
- Knight, F. B. (1976). A characterization of the Cauchy type. *Proceedings of the American Mathematical Society* 55,
  130–135.
- Martens, N. C. M. (2021). The (un)detectability of absolute Newtonian masses. *Synthese* 198(3), 2511–2550.
  "Kinematic comparativism", §4.
- McCullagh, P. (1996). Möbius transformation and Cauchy parameter estimation. *Annals of Statistics* 24(2), 787–808.
- Narens, L. (2002). *Theories of Meaningfulness*. Lawrence Erlbaum. Also Narens and Luce, "Meaningfulness and
  invariance".
- Poincaré, H. (1914). *Science and Method*, trans. F. Maitland. Thomas Nelson. Book II, ch. I, pp. 94–95.
- Roy, W. (1785). An account of the measurement of a base on Hounslow-Heath. *Philosophical Transactions of the Royal
  Society of London* 75.
- Sedgwick, H. A. (1973). *The Visible Horizon: A Potential Source of Visual Information for the Perception of Size and
  Distance*. Doctoral dissertation, Cornell University. And (2021), J. J. Gibson's "Ground Theory of Space Perception",
  *i-Perception* 12(3), the source of the quotation.
- Sivia, D. S. and Skilling, J. (2006). *Data Analysis: A Bayesian Tutorial*, 2nd ed. Oxford University Press.
- Snellius, W. (1617). *Eratosthenes Batavus, de terrae ambitus vera quantitate*. Leiden.
- Stevens, S. S. (1946). On the theory of scales of measurement. *Science* 103, 677–680.
- Triggs, B., McLauchlan, P., Hartley, R. and Fitzgibbon, A. (2000). Bundle adjustment: a modern synthesis. In *Vision
  Algorithms: Theory and Practice*, LNCS 1883, 298–372.
- Warren, W. H. (1984). Perceiving affordances: visual guidance of stair climbing. *Journal of Experimental
  Psychology: Human Perception and Performance* 10(5), 683–703.

The geometry is set out with proofs in *Observation from Somewhere* (archived since 30 October and kept for its proofs; the current account is *Reads and Writes*, rewritten on 10 November
(R788) with read, extent and write), in the same collection: readers and writers in
§3.1, the one-length circle in §5, the Cauchy as the law of the uniform turn in §7, reading and writing in §9, and the
classical pieces in Appendix A ("The Cauchy from one length").
