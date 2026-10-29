# One length turned

*The second of a series of essays on what can be known from where one stands. Draft, 28 October 2026.*

The first essay ended on a claim: a reader with no second length still has a circle, because its own single length,
turned, traces one. This essay takes that claim slowly. It asks what a turned length gives you, why it gives a circle and
not some other curve, and why there is one special direction on it, at 45°. It also shows how two different ways of
pivoting the same length read the same point twice, once as a ratio and once as a square.

All of it is classical geometry, most of it in Euclid. What is new is the order in which it is read. Usually the circle
comes first, as an object held whole, and turning is something done to it afterwards. Here the turning comes first,
and the circle is what it leaves behind.

---

## 1. An arm held out

Hold your arm out straight in front of you, level with the ground, and raise it slowly until it points straight up.
Your arm does not change length. Your hand traces a quarter of a circle.

That is all a circle is, from where you stand: one length, turning. You did not need to know how far away anything was.
You did not need a second length, a radius chosen to match something else, or a centre measured out. You needed your
arm and the ability to turn it.

At each moment of the turn your arm points somewhere. Its reach has two parts: how far it reaches forward, and how far
it reaches up. Call the forward part **h** and the upward part **v**. Both are shares of the same arm, so each lies
between 0 and 1. Straight ahead, h is all of it and v is nothing. Straight up, v is all of it and h is nothing. Halfway,
pointing up at 45°, the two are equal.

The ratio v/h is what the direction *reads*: how steeply it points. It starts at 0 straight ahead, passes 1 at 45°, and
grows without bound as the arm nears the vertical. It is a slope, and it has no unit, because both of its parts are
shares of one arm. If your arm were twice as long, every reading would be the same.

The first essay called a reader's own length **H**. Your arm is a good H: always with you, never measured, and enough
to start a geometry.

---

## 2. Why a circle, and not some other curve

The claim that a turned length traces a circle sounds too obvious to need defending. It is worth defending, because the
reasons show exactly what is being assumed.

"A length that does not change" depends on how length is measured. Measure it the usual way, straight across as the crow
flies, and points at a fixed length from your shoulder lie on a circle. Measure it instead by the larger of the two
parts, forward or up, and points at a fixed "length" lie on a square: forward one, or up one, whichever is bigger. Measure
it by the sum of the parts, and points at a fixed "length" lie on a straight line from straight ahead to straight up. The
circle, the square and the line are all curves of constant length. They use different rulers.

So something must pick the circle. It turns out that turning picks it, if turning means what it naturally means.

Think of the turn as a motion made of tiny identical steps. Each step does the same thing to every direction, nudging it
round by the same small amount, and the steps repeat. After enough of them the arm is back where it started, a full turn.
A quarter of the way round, all of the forward reach has become all of the upward reach. Those are the only conditions:
the same step repeated, coming back after a full turn, forward becoming up after a quarter.

From those conditions alone, there is exactly one way of measuring length that the turn leaves unchanged, up to a single
overall factor. In that measure every direction of the arm has the same length, forward and up are at right angles, and
the arm's tip moves along the circle. The square and the line fail: no single repeated step carries the square's corners
round its sides at an even pace and comes back. The turn's own ruler is the round one.

The single overall factor left free is the arm's own length, H. The turn fixes everything about the geometry except how
big it is drawn, and that it leaves to the reader.

This matters for what follows. The circle is not assumed and then turned. The turn is assumed, a plain repeated motion
that comes back, and the circle is what it must trace. The only thing still taken on trust is that the motion is linear:
each step mixes forward and upward reach the same way, however far round the arm has gone. That is what "one motion,
repeated" means.

*Demo: one sweep, three paths: the circle, the line and the square, each swept along its own length.*

---

## 3. The corner

On a quarter turn there is one direction that is different from all the others: 45°, where forward and up are equal and
the reading v/h is exactly 1. The essays call it **the corner**.

It is special for a reason so simple it is easy to miss. Swap the roles of forward and up, so that you read h against v
instead of v against h. Every reading s becomes 1/s. A reading of 2 becomes a half; a reading of 10 becomes a tenth.
Every direction moves, except one. At 1, s and 1/s are the same number. The corner is the one reading the swap leaves
where it was.

From that one fact, several others follow.

- **Every turn passes through it.** Starting from 0, a reading has to reach 1 before it can pass it. However the arm is
  raised, it goes through the corner on the way.
- **It splits the turn into two halves that mirror each other.** The swap carries every reading below 1 onto one above
  1, point for point, and back. Whatever is true of the near side, readings less than 1, is true of the far side, read
  the other way up. The essays call the two sides the *near field* and the *far field*.
- **It is where a reader has to change hands.** Suppose you want to keep every reading between 0 and 1, so it fits a
  fixed scale. Below the corner, v/h does that. Above it, v/h runs off to infinity, but h/v comes back between 0 and 1.
  So a reader that keeps its readings bounded must switch from one to the other, and the only place the switch works on
  both sides is exactly at 1.
- **Approximations break there.** A great many formulas are written as series in powers of the reading: 1, s, s², s³ and
  so on. Such a series behaves well for readings below 1 and blows up for readings above it. The corner is the edge of
  where they work, and past it one rewrites them in 1/s. The corner is where expansions stop.

None of this depends on how long the arm is or how far away anything is. The corner is a fact about comparing two shares
of one length. It would be the same for a thumb, a telescope or a lighthouse beam.

---

## 4. Why 45°, and what the chord does not have

There is a second way to see why the corner sits at 45°, and it shows what a turned length has that a straight line does
not.

Draw a straight line from a point A to a point B. Walk along it from A to B, and at every step you can say how far along
you are: a share h of the way still to go to B, a share v already come from A, with h + v = 1. Every ratio of v to h
appears once on the walk. In that sense the line, the *chord*, already holds every reading. It holds them in the way a
writer holds them, both ends at once, with a length of 1 between.

The arc holds the same readings in a different way. Turn a length from pointing along the chord to pointing square to it,
and its tip sweeps a quarter circle that bows out from the chord. The arc passes through every ratio too, but it has
something the chord lacks: a direction it *faces* as it goes. At the start the arc runs square to the chord; at the end
it runs along it. In between it turns.

Picture your arm's quarter arc against the straight line joining its two ends, from straight ahead to straight up. At
the start the arc leaves that line leaning one way; at the end it meets it leaning the other. Halfway, at 45°, it runs
parallel to the line, leaning toward neither end, and the arm itself points square to the line. That halfway point is
the corner. There the arc stands farthest from the line, by 1 − 1/√2 of the arm's length, about 0.29.

So the corner is 45° because that is where the facing is square to the line between the two parties. A straight line has
no facing, so on it nothing marks the middle except arithmetic. On the arc the middle is the place where the turning
favours neither side.

This marks a difference of vantage that runs through the whole series.

- **The writer holds the chord.** It has both ends at once, the length 1 between them, and it faces nothing. It does not
  turn.
- **The reader faces the arc.** It does not walk along the chord. It stays where it stands and turns, and the point it
  reads crosses from one end to the other.

The circle is what the reader's facing traces. The chord is what the writer holds.

*Demo: the facing: one sweep from A to B, the facing turning through square to the line at the corner.*

---

## 5. The arc from the chord: two rays meeting

There is a way to get the arc without turning anything, and it is one of the oldest results in geometry.

Stand at A and look toward the far side with a slope s: up s for every one along. Stand at B and look back with the
reciprocal slope, 1/s, the swap of the first. Where the two lines of sight cross, mark a point. Do this for every s, from
0 to infinity, and the marks trace a semicircle with AB as its diameter.

The reason is Thales' theorem, which Euclid gives in Book III of the *Elements*: an angle standing on a diameter is a right
angle, and conversely, every right angle on a diameter has its corner on the circle. The two lines of sight, slope s and
slope 1/s turned the other way, always meet at a right angle. So their crossing is always on the circle.

The crossing has a tidy address. Put A at 0 and B at 1. The crossing for slope s lands at

> the point (1, s) divided by (1 + s²).

Its distance from A is h and its distance from B is v, the same two shares as before. The chord, of length 1, is the
hypotenuse of a right triangle with sides h and v, so h² + v² = 1: Pythagoras, standing on the chord.

The point also cuts the chord beneath it into two pieces, of lengths h² and v², and its height above the chord is
hv. That height is the *mean proportional* of the two pieces, the number whose square is their product, which Euclid
constructs in Book VI exactly this way. When the slope is a fraction, the point has fractional coordinates. A slope of a
half, for instance, lands at (4/5, 2/5); seen from the middle of the chord it has turned to an angle whose cosine is 3/5
and whose sine is 4/5, the 3–4–5 right triangle. Every Pythagorean triple comes out of this construction.

At the corner, s = 1, both lines of sight are at 45°, and the crossing stands directly above the middle of the chord, at
the top of the arc. The swap of s and 1/s is the mirror across the line through that top.

There is a modern name for this construction. In the nineteenth century Jakob Steiner showed that whenever the lines
through one point are paired with the lines through another by a correspondence of this kind, the crossings trace a
conic: an ellipse, a parabola or a hyperbola. A circle is the case where the pairing turns each line through a right
angle, and that needs forward and up measured at one length. If someone draws the picture on a page with the upward
direction stretched by a factor c, the same lines of sight cross on an ellipse instead. The circle belongs to the reader's
one length. A page with two different lengths on its two axes gets an ellipse.

One more classical fact comes out of the construction, and it is the point of the next section. As A's line of sight
turns through an angle θ, the crossing moves round the circle by twice that angle, seen from the middle of the chord.

*Demo: one turn and one read: the ray from A and the radius from the middle meeting on one point of the circle.*

---

## 6. Two sweeps, one standpoint

That factor of two is Euclid again, in Book III: an angle at the edge of a circle is half the angle at the centre that
stands on the same arc. It is called the inscribed angle theorem, and it organises everything the reader can read.

There are two natural ways to sweep the same arc.

- **From A, a point on the circle.** A ray from A turns through θ. This is the *inscribed* sweep.
- **From the middle of the chord, the circle's centre.** A radius turns through 2θ. This is the *central* sweep.

The ray at θ and the radius at 2θ end at the same point of the arc, for every θ. One point, reached two ways.

Why only these two? A sweep is useful for reading an arc when equal steps of turning reach equal stretches of arc,
wherever the sweep points. From the centre that is obviously so: each step of turn moves the radius's end by the same
step of arc. From a point on the circle it is so too, by the inscribed angle theorem: each step of turn moves the end by
twice the step of arc, always twice. From anywhere else it fails. Stand inside the circle but off centre, and a step of
turn sweeps more arc when you look toward the centre than when you look away from it. Stand outside, and the rate runs
wild as your gaze grazes the edge. So a circle has exactly two places to sweep it evenly from: its centre, and any point
on it. There is no third.

These are not two readers, and not two motions. They are one standpoint's directions, counted about the two pivots the
geometry allows. The reader stands at A, the circle's own point. The centre belongs to the pair, A and B, and is neither
party's place.

### What each sweep reads

The two sweeps name the same point in two different ways, and the two names are of different kinds.

**The inscribed sweep reads a ratio.** Follow A's ray out until it crosses the line that touches the circle at B. The
height where it crosses is s = v/h, the reading of section 1. As the ray turns toward the vertical, that height runs off
to infinity. The readings are unbounded. This is the sweep whose readings, taken at even steps of turning, follow the
Cauchy law: half below the corner and half above, the median at 1, and no mean.

**The central sweep reads a square.** The radius at 2θ ends at a point whose coordinates are half of (h² − v², 2hv). If
you write A's direction as a single complex number, h + iv, that point is half its square. The central sweep's point is
the inscribed sweep's direction, squared. Its coordinates never exceed the radius, so they are bounded, and every average
over an even turn exists: the across part averages to 0, and the height, measured against the radius, averages to
2/π.

The factor of two between the sweeps *is* that squaring. It is why the radius turns twice as fast as the ray. It is why
one sweep's readings are ratios, unbounded and held by their median, and the other's are squares, bounded and held by
their mean.

There is a pretty corollary. In complex form, the central sweep's point is half of e raised to 2iθ. At the start, zero
turn, it sits at B. At the corner, it sits at the top of the arc, in the direction i. At the end of the quarter turn, the horizon, the radius has made
a half turn and sits back at A, home. That half turn is e to the power iπ, which equals −1. Euler's identity is the
central sweep's half turn, seen from the middle of the chord, while the reader's own ray has made only a quarter. The e
and the π are only notation here: the same squaring, written with the reading s, is (1 + is)/(1 − is), and as s runs
off to infinity that runs to −1. What the identity records is projective: the reader's two ends, zero and the horizon,
land at the two ends of one diameter. Section 9 comes back to Euler's formula as the reader's notation.

**One turn, two charts.** The even turn belongs to neither sweep. Written as the inscribed sweep's ratio, it is the
Cauchy: the long tails and the missing mean come from the ratio running off to infinity. Written as the central sweep's
point, the very same turn is spread evenly along the half circle, and it has a mean because the half circle is bounded.
Neither is a bell curve. The bell, the Gaussian, belongs to what arrives, and only as a model: if the light's strengths
along two axes vary independently and look the same however the axes are turned, together they make a round bell, and
the direction of that bell's samples is an even turn, which is why its ratio is a Cauchy. That is a fact about one kind
of paint, not about either sweep.

### Address, landing, payload

Three things meet at that one point of the arc, and the series keeps them apart.

- **The address** is the direction of A's ray, the reading s. It is there before anything arrives.
- **The landing point** is where the radius ends, the point the address points at.
- **The payload** is whatever is found there: the colour, the light, the thing.

The inscribed angle theorem guarantees the address and the landing point meet. It says nothing about what is found.
That is the world's business. The address is laid whatever arrives, and each address points exactly at where its payload
will land. The third essay is about what that separation means. Here the point is only that it is built into the circle:
the reader's addresses and the world's landing points are joined, one to one, by a theorem that needs no second length,
only the reader's own length turned.

*Demos: one turn and one read; the central reader, step 6 (one read).*

---

## 7. π/2 and 2/π: the writer's 1, read twice

There is a number on each side of the chord and the arc, and the two numbers are reciprocals.

Raise the arm through its quarter turn. Its tip travels π/2 of the arm's length along the arc, while its straight reach
upward goes from nothing to all of the arm, 1. Read the turn as arc over straight reach and it comes to π/2 over the whole
quarter; read it as straight reach over arc and it comes to 2/π. The first is the central sweep's reading; the second is
the inscribed sweep's.

Neither is the straight length itself. The writer, holding it whole, has it as 1, no curve involved. Each sweep gets at
that 1 through the arc, and each gets it distorted: one too long by π/2, one too short by 2/π. Only their product
gives back the 1:

> π/2 × 2/π = 1.

This is not a coincidence of numbers. It says that the reader, facing the arc from where it stands, never has the chord's
length directly. It has it twice over, once from each pivot, and the two readings together return exactly what the
writer holds in one. What they return is the reader's own length measured in itself, H in H. They do not return the
size of anything else.

*Demo: the mountain and the thumb, "the two vantages": π/2 and 2/π on the thumb's circle, their product 1.*

---

## 8. Other paths, and what only the circle gives

Section 2 said that the square and the line are curves of constant length under other rulers. What happens if you
sweep them instead?

Take three paths from straight ahead to straight up: the quarter circle; the straight line h + v = 1; and the two sides of
the unit square, along the bottom and up the side. Sweep each one evenly along its own length, and ask, at each moment,
what share of the sweep has been done and what direction it points in.

At three places all three paths agree.
- **At the start,** straight ahead, nothing is done.
- **At the corner,** 45°, exactly half is done, on all three.
- **At the end,** straight up, all of it is done.

In between they differ. When the direction reaches 22.5°, halfway to the corner, the circle has done exactly a quarter of
its sweep, the line about 0.293 of its, and the square about 0.207 of its. And all three share two features: half the
sweep lies on each side of the corner, and the readings v/h have no mean. Those two features need only that the path is
the same on both sides of the corner and reaches all the way to the vertical.

What only the circle gives is the exact shape of the law: the Cauchy itself, with no other choice made. The square and
the line give other laws with the same median and the same missing mean. The circle gives the one law that a further
turn carries onto itself unchanged. That is the law of the reader's own turning, the circle with no V.

*Demo: one sweep, three paths.*

---

## 9. The circle, written by a writer

Everything so far has been from the reader's side. The writer has a circle too, and it is worth seeing how the writer
describes the reader's.

A writer holds both lengths, the reader's H and the other party's V, and can draw them on a page with two axes. Looking at
the circle the reader's one length traces, the writer sees two axes drawn at the same length and writes that down as
**V = H**. It is the writer's name for the reader's circle. The reader never set it. It has no V to set.

On a page, though, two different lengths are possible. Draw the upward axis at c times the forward axis, so V = cH with c
not equal to 1. Then nothing turns all of the forward reach into all of the upward reach without stretching on the way.
The tip moves along an ellipse, not a circle. "Sweeping evenly" no longer names one sweep: even in direction, even along
the curve and even in its parameter now give three different laws, and only one of them is the Cauchy with its median
at the corner. The corner itself, where the two amounts are equal, slides off 45°.

So where does a c other than 1 come from, if the reader never chooses it? Four places, each with a signature.

- **It is writing.** Amounts are wanted in a shared unit, and c is a real ratio of units, measured on purpose. An
  equal-area map does this deliberately.
- **It is uncalibrated.** An instrument with unequal gains, pixels that are not square, or variables left in their own
  units imposes a c. The median of the readings sits at c instead of on the corner. Standardizing puts it back.
- **An estimate has been taken for the circle.** A guess at the other party's true size belongs to the amounts. Redrawing
  the circle with it confuses a size with a stretch.
- **It does not turn at all.** A motion that is not a turn has no circle to stretch. It has a different geometry, with no
  corner at its median.

Practice has found c = 1 again and again, under other names, each field for its own reason. Statistics standardizes its
variables before comparing directions. Charts that must keep compass bearings true draw them at c = 1; that is what
Mercator's projection does. Graphs of slopes are drawn with equal axes, and cameras have square pixels. The geometry gives
the one reason underneath: c = 1 is the only two-axis drawing that has the reader's circle on it.

### Circular mathematics without V

That raises a fair question. The circle's equation seems to need V. On a page it reads (x/H)² + (y/V)² = 1, and it is a
circle only when V equals H. If the reader never knows V, how can it do circular mathematics at all?

The answer is that the equation on the page is the writer's. It describes a drawing with two axes, each with its own
extent, and that drawing does need two lengths. The circle itself needs only one. Its classical definition is everything
at one distance from a centre, and that is one length. Turn the length and its tip traces the circle, as section 2 showed.
The turn's two parts are h = cos θ and v = sin θ, the across and up shares of the same length. So h² + v² = 1 is a fact
about the shares of one length. The v in it is the turned length's own up share, not a share of some second party's
breadth. Reading it as the second is where the confusion comes from.

And circular mathematics was always ratio mathematics. Sine, cosine and tangent are sides over the hypotenuse. A radian
is arc over radius. π is circumference over diameter, a ratio, so π itself is a reading. e^(iθ) is the unit circle, any
circle divided by its own radius. The corner, π/2 and 2/π, and the Cauchy are ratios too. None of them moves when the
world is scaled, which is the test for a reading. Trigonometry is the reader's mathematics.

What the reader cannot do without an amount carried in is place a point at (x, y) in metres, state the circumference as
2π times so many metres or the area as so many square metres, or say how large another party's circle is beside its own.
Those are amounts, and amounts are writing. The reader does every part of circular mathematics except the parts that
state a size.

### Euler's formula, the reader's notation

One piece of classical notation holds all of this at once: Euler's formula, written in polar form,

> z = r·e^(iθ).

**The two factors are the address and the payload.** The factor e^(iθ) has size exactly 1. It is a direction and
nothing else: the address, held in the reader's own length, H measured in H. The factor r is an amount, how far, how
bright, how big, and it means something only in a unit, which only a writer can supply. Polar form has been splitting a
number into its direction and its amount since the eighteenth century. Read from a standpoint, that split is the
reader's and the writer's.

**The logarithm makes the scale test a question of which part moved.** Take the logarithm:

> ln z = ln r + iθ.

Scale the world by k and only the real part moves, by ln k. Turn, and only the imaginary part moves. So the first test
of the series, scale the world, comes down to which part of the logarithm changed: the imaginary part is a reading, the
real part a writing. The real part's starting point, the one amount that sets every size, is exactly what no reading
fixes. And the reader's ignorance, which turn it faces and how large anything is, is nothing more than sliding this
plane up and down and left and right. Sliding keeps area, so the measure that suits that ignorance is plain area on the
logarithm's plane: uniform in direction, and uniform in levels of distance.

**Composition becomes addition.** In the reader's own chart, readings taken from two zeros combine by tangent addition,
(s₁ + s₂)/(1 − s₁s₂). That is awkward, and it blows up when the two turns together reach the vertical. In Euler's form
the same combination is e^(iα)·e^(iβ) = e^(i(α + β)): the angles just add, and nothing is special at the vertical. The
reader's awkward arithmetic is the turn's plain arithmetic, seen through the tangent. A reading has no sign, so a turn
and the same turn plus a half turn give the same reading; the reader's line closes after half a turn of its ray, and the
squaring of section 6 turns that half turn into one whole turn of the central sweep.

All of this is classical: polar form, the complex logarithm, the area that multiplication keeps, the double cover. What is
the series' own is the reading: e^(iθ) as the address, r as the payload, the logarithm's two parts as reading and
writing. It is the right notation for a reader because it keeps the two apart. The reader holds the imaginary part; the
writer needs the real one.

**The two corners are two mirrors.** The plane of the logarithm also shows the corners plainly. Swap a reading for its
reciprocal, v/h for h/v, and the angle θ becomes 90° − θ: a reflection of the imaginary part, and the line it leaves
in place is θ = 45°, the corner in direction. Swap a distance for its reciprocal about the reader's length, d/H for
H/d, and ln d becomes 2 ln H − ln d: a reflection of the real part, and the line it leaves in place is d = H, the corner
in distance (the fourth essay's corner of near and far). So the reader has two corners, one on each axis of one plane,
each a mirror line. Each is moved by sliding the plane along its own axis: turning the head slides the first across
the world's directions, and choosing H slides the second along the levels of distance. That is why the two corners can
be set independently: they sit on different axes.

**Where it stops.** Euler's formula is a tool for the flat case, one other party and turns in a plane. With three
parties, the fifth essay's wedge, only half of it survives. The split survives: a point of space is still an amount
times a direction, scaling the world still moves only the amount, and the scale test still asks the same question. What
fails is composition as addition. Turns in a plane commute, so their angles add. Turns in space do not: a quarter turn
about one axis and then another ends somewhere different from the same two turns in the other order. With no fixed
order there is no single angle to add, and no logarithm turns combining them into a sum. Quaternions compose turns of
space, but they do not commute, and no number system of more than two dimensions does both. Each sweep on its own,
altitude or azimuth, is still a plane's turn and still adds; it is putting the two together that does not. It can look
strange that so tidy a tool stops at two dimensions, but the reason is that space has more than one way to turn, and
the ways do not take turns politely.

---

## 10. What it comes to

The two unifying ideas of the series, reading against writing and the Cauchy, meet in the circle, and this essay has
been about how.

**The circle is the reader's before it is the writer's.** A writer starts with the circle as an equation in two lengths
and turns it. A reader starts with one length and turns it, and the circle is what the turning traces. The writer's
equation describes, in two lengths, a thing the reader made with one.

**Everything special about the circle is available from one length.** That includes the corner at 45°, its two
mirrored halves, the right angle on the chord, and the inscribed sweep's ratios and the central sweep's squares. So are
π/2 and 2/π, whose product returns the reader's own length. None of it needs a second length or the size of anything.

**The Cauchy is the circle read from its edge.** The inscribed sweep, from the reader's own point on the circle, reads
directions as ratios, unbounded, with their median at the corner and no mean. That is the Cauchy, the circle's law
without the V. The central sweep, from the middle of the pair, reads the same points as squares, bounded, with means. They
are two names for one point, joined by a theorem in Euclid.

The third essay takes the inscribed sweep's law on its own terms: what it means that the reader's addresses are laid
before anything arrives, how they stay apart from what arrives, and why practice has always been right to read them by
their median.

---

## Sources

- Euclid, *Elements*: Book III, propositions 20 (the angle at the centre is double the angle at the circumference) and
  31 (the angle in a semicircle is right); Book VI, propositions 8 and 13 (the mean proportional).
- Steiner, J. (1832). *Systematische Entwickelung der Abhängigkeit geometrischer Gestalten von einander*. Berlin.

The geometry is set out with proofs in *Observation from Somewhere*: the corner in §4 (Propositions 1 and 2), the arc from
the chord, the two sweeps and what each reads in §4, the reader's circle in §5 (Proposition 3, with the derivation of the
circle from a uniform returning sweep as part (g)), and the three paths in §12.2.
