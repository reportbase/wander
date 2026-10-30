# Rates, not angles

*The fourteenth of a series of essays on what can be known from where one stands. Draft, 30 October 2026.*

A carpenter calls a roof "six in twelve": it rises six for every twelve it runs. A road sign says "10%": the road climbs
ten for every hundred it goes. A wheelchair ramp is built to "one in twelve". None of them says an angle. Nobody on the
site needs to know that six in twelve is 26.57°, and if someone asks, the number has to be looked up, or computed by a
function that sums an infinite series. The pitch itself is had at once, with a level and a tape.

The pitch is the reading the earlier essays have called v/h, a direction held as a ratio. The degrees are something
else, a share of the whole turn, and to give one you have to hold the whole turn first. This essay is about the
difference, and its claim fits in one line:

> Writers have angles; readers have sweeps.

Three things follow. A rate is always a rate *of* something *per* something: the per is the sweep's, an address, and the
of is what arrives there, the payload. A hand swept from horizontal to vertical goes at one of two rates, π/2 or 2/π,
depending on where it pivots, and never at 1: the 1 is the writer's rate, the angle. And the tangent and arctangent,
which convert between a direction and an angle, are the writer's tools: they need the completed turn. The reader runs the
sweep and never needs them.

Put together, this is the Cauchy's framing: it is the sweep over the something. The sweep lays the per, and the Cauchy is
the law of that per, the reader's sweep rate counted in readings; the payload is what lies over it. The writer's rate is
1, the reader's π/2 or 2/π, and the corner is where the three come together.

None of this corrects trigonometry. It says where trigonometry sits.

*Demos: `facing.html` (the facing turns twice as fast as the sweep); `one-read.html` (arc over chord and chord over arc,
their product 1 at every θ); `paths.html` (the turn and its projection, π/2 and 2/π at the horizon); `mountain.html`
("the two vantages" on the thumb's circle); `sweep-zero.html` (a turn counted by itself, and a new zero composed by
tangent addition); `slide-rule.html` (the circular rule: a turn from a new zero against tangent subtraction).*

---

## 1. The of and the per

A rate has two places. Light per square metre, cars per hour, rise per run: there is the thing counted, and the thing it
is counted against. The first is what the rate is *of*; the second is what it is *per*.

For a reader the two places are filled from opposite sides. The per is the sweep's. Turning from where it stands, one
length lays out the reader's addresses in order, one after the next, before anything arrives (the third essay). The of is
the payload: the light, the colour, whatever arrives along each address. So what a reader reads is always payload per
address, and the third essay's split between the two is a fraction, the address underneath and the payload on top.

The two places behave differently when the world is scaled. Scale everything by k and every address stays where it was,
since a direction has no size. So the per never moves. The of may or may not: a payload compared with another payload
arriving at a neighbouring address is a ratio and stays put; a payload stated in an agreed unit moves with k, and is a
writing (the first essay). The geometry fixes the per, completely and in advance. What fills the of is the world's.

---

## 2. The hand's two rates

Hold out a hand at arm's length, level, and raise it until it points straight up: a sweep from horizontal to vertical.
How fast does it go?

The writer has a ready answer. Holding the whole quarter circle at once, it measures the turn by its angle: so much arc
for so much radius, step for step. In the writer's measure the sweep goes at rate 1, and the straight line from the
hand's first place to its last, the chord, is a length it holds whole. That 1 is the writer's rate. It is what an angle
is: arc per radius, read against the completed turn.

The reader has no such measure. It has the sweep, from where it stands, and only two places to stand where a sweep is
even (the second essay): the middle of the chord, where the radius turns, and a point of the circle, where the ray turns.
From each, the same sweep from horizontal to vertical comes at its own rate against the straight line the writer holds:

- **π/2, the central sweep.** From the middle, the sweep runs π/2 of arc for the chord's 1. Along the way the running
  value is arc over chord, θ/sin θ, from 1 at the start through 1.1107 at the corner, and it is attained when the radius,
  its half turn done, lands back on home, a point.
- **2/π, the inscribed sweep.** From a point of the circle, the chord comes at 2/π per unit of sweep. Along the way it is
  chord over arc, sin θ/θ, through 0.9003 at the corner, and it reaches 2/π only as the ray goes to the horizon,
  approached and never arrived at.

Neither is 1. Both start at 1, at zero, before any sweeping has happened, and part from it at once. Once the hand is
moving, the reader has π/2 or 2/π, never the writer's 1. The two together, multiplied, give back 1, at every point of the
sweep and not only at its ends; but no one sweep has it. The second essay put this as the two sweeps each reaching the
writer's 1 through the arc, one too long and one too short. In rates it is plainer: the writer has the angle, the reader
has the sweep, and the angle is what the two sweeps make when they are joined.

None of these rates changes when the world is scaled, and none of them is a rate of anything that arrives. They are the
per, measured against the writer's straight line: the spacing the sweep gives its addresses. They are the frame's own
rates, empty until a payload fills them.

---

## 3. The corner, where the three meet

Where is the corner? The second essay found it three ways: the one ratio the reciprocal leaves alone, the halfway point
of the turn, the place where the facing stands square to the chord.

In rates it is where three things come together: the horizontal, the vertical and the writer's 1.

**The horizontal and the vertical meet.** As the hand rises, v fills and h empties. Early on v fills fast and h hardly moves; late, h
empties fast and v hardly moves. There is one place where v fills exactly as fast as h empties. That place is the corner.
It is where the two rates trade places, which is why v − h changes sign there at its steepest: the corner is a crossing,
not a turning point.

**Their ratio is the writer's 1.** At the corner the reading is v/h = 1. Everywhere else along the sweep the reader's
reading differs from 1; here, and only here, it agrees with the writer's rate.

**The writer's 1 is the corner of the reader's two rates.** π/2 and 2/π are reciprocals, and 1 is their geometric mean,
√(π/2 · 2/π). On the levels they sit either side of it, ln(π/2) = 0.4516 above and ln(2/π) = −0.4516 below. So the
writer's rate is the fixed point of the reciprocal that pairs the two sweeps: the corner between them.

One thing does not happen there. The sweeps' running rates are not 1 at the corner: arc over chord is 1.1107 and chord
over arc 0.9003. They are 1 only at zero, before any sweeping. The corner is not where the reader's sweep runs at the
writer's rate. It is where the horizontal and vertical balance, their ratio is the writer's 1, and the writer's 1 sits
between the reader's two rates.

No 45° was used. "45°" is the writer's name for the corner, the corner written as an eighth of the whole turn. The reader
finds it by the sweep alone.

---

## 4. Two sweeps, two rates

The second essay showed two pivots for one standpoint. Measured in the writer's angle, a radius turned about the
circle's centre moves its end one step of arc for each step of turn, and a ray turned about a point of the circle moves
its end two steps of arc for each step of turn (Euclid III.20: the angle at the centre is double the angle at the circumference). Those are the only two places
where the rate is the same wherever the ray points. Anywhere else a step of turn carries the end by 2t/(t + t′) steps of
arc, t and t′ the distances ahead and behind, which changes as the ray turns.

So the inscribed angle theorem, read this way, is a statement about rates: the facing turns twice as fast as the sweep.
Read from the reader's side, without the angle, the two pivots are the two rates of the last section, π/2 and 2/π.
The square of the second essay, the central point ½(h + iv)², is that doubling written as a point.

A reader off the centre and off the circle has no uniform rate, and this is where the circle's own law comes from. Turned
uniformly, its end lands unevenly; twice its rate less the central rate, (2·dθ/dφ − 1)/2π, is the circle's harmonic
measure from where the reader stands, the wrapped Cauchy (the thirteenth essay, "One law, four parts"). It is a
combination of two rates, and needs nothing else.

---

## 5. The Cauchy is a speed

The third essay read the Cauchy as the law of the reader's addresses: turn uniformly, read each direction as v/h, and the
readings are spread as 2/(π(1 + s²)). Read in rates, that density is a speed.

Per step of turn, the reading s = v/h moves on by 1 + s². Near home, where s is small, it moves about one for one. At the
corner it moves two for one. Past the corner it moves faster and faster, without bound, as the ray goes to the horizon.
The density is the other way round, how much turn there is per unit of reading, 1/(1 + s²), scaled by 2/π so the whole
quarter is one. Where readings go by slowly the turn lingers on them; where they rush, the turn leaves few of them.

Both of the Cauchy's famous features come from this one speed:

- **The median is at the corner.** Half the turn's steps are taken before the corner and half after, since the corner is
  the turn's halfway point. The reading at that halfway point is 1.
- **There is no mean.** To average the readings is to weight each step of turn by the reading it reaches, and past the
  corner the readings outrun the steps without bound. Take the mean of the turn instead, or of the shares, and it exists.

That is the third essay's advice, "to average, average the angle", said in rates: average the sweep's own advance, never
the quantity that runs away from it.

Notice what this speed is a rate of. It is turn per reading: address against address, the per against itself, with no
payload anywhere in it. That is the main result of the third essay said in rates. The Cauchy is the spacing of the per,
and so it belongs to the addresses, never to what arrives.

---

## 6. Writers have angles, readers have sweeps

The tangent turns an angle into a rate: tan θ = v/h. The arctangent turns a rate into an angle. Both cross between two
sides.

On one side is the slope, v/h: a ratio, the thing the reader holds, with no circle in it and no π. On the other side is
the angle, a share of the whole turn, and a share of the whole needs the whole: π, the total of a completed turn.
Angles need π by definition. To evaluate the tangent or the arctangent is to cross from one side to the other, and that
crossing is where π lives.

The reader never makes the crossing, and never needs to. What it does do is all on the slope side:

- **It composes.** A new zero composes with the old by tangent addition, s ⊕ t = (s + t)/(1 − st). That is the tangent's
  *addition law*, and the reader runs it on readings, never on angles. It needs no π.
- **It halves.** The reading halfway to s is (√(1 + s²) − 1)/s: one square root, no angle.
- **It orders and flips.** It tells which of two readings is nearer the horizon, and it reads 1/s for s.

*The Algebra of Discrete Observation*, a paper of this series' archive, put the pairing in four words: algebra kept,
evaluation declined. The reader runs the tangent's algebra; it never evaluates the tangent. π is not missing from the
reader's world. It is located, on the angle side, and the reader does not go there.

The writer does go there, and is right to. It holds the whole turn, so it can name any direction as a share of it, put a
degree on a protractor, lay an array of N slots evenly over the quarter turn and find a reading's slot by its arctangent
(the twelfth essay). That is construction from the completed turn, and it is the writer's.

The reader does reach π's neighbourhood, but only as a limit of its own steps. Halve the quarter turn, then halve again,
and multiply the cosines of the halves:

> 2/π = √½ · √(½ + ½√½) · √(½ + ½√(½ + ½√½)) · …

This is Viète's product of 1593, and each factor is a halving, the reader's own operation. The reader approaches 2/π by
halvings and never arrives. π is transcendental (Lindemann, 1882), so no finite chain of the reader's operations, which
are field operations and the halving square root, can reach it. Even the inscribed sweep's number, the reader's own
rate, is one the reader meets only at the horizon. And the writer's 1, the angle, the reader has only by joining both
sweeps.

---

## 7. It has been done

This is not only a way of talking. The draw project's Tangent Bridge, the theorem behind its curve format, was proved in
the angle chart, where classical approximation theory already sits, and is executed in the slope chart with the count of
calls to sin, tan and arctan held at zero. Its reconstruction kernel is a rational function of the held slope; the round
trip, exactness at the leaves and the partition of unity were checked that way to machine precision for up to 1,024
leaves. Its fisheye, which the editor's layout computes with tan, was rebuilt from the corner, the halving and tangent
addition alone, value for value. The format's decoder evaluates no trigonometric function.

The one place a π showed up in its numbers was the worst-case growth of reconstruction error, (2/π)·ln N. Read in the
slope chart, its 2 is the reader's, an algebraic integral, and its π is the normalization: "what share of the whole
turn", the whole turn being the thing the reader declines. The π was the writer's count of the arc, not anything the
reader computed.

Computer science learned the same lesson by accident. `atan2(v, h)` keeps the pair, so it returns the horizon and the quadrant
without dividing; `atan(v / h)` divides first, loses which way the pair pointed, and has nothing left when both are zero. The safe call is the one that does not
cross to the angle before it has to.

---

## 8. The natural world

The claim that started this essay was that the sweep is how things work in the world, and trigonometry is not. Read
carefully, it is a claim about what a turning thing has to hand: a sweep, and what comes along it.

The second claim of this essay sorts the examples. A rate is of something, and the something decides whether it is a
reading. A wheel of diameter 1 rolls π along the road for each turn: road per turn. But road is an amount, so stated that
way it is a writing, the writer's angle carried onto the ground. A planet sweeps equal areas in equal times: area per
time, and a time is a clock carried in, so that too is a writing. The rates a reader has are of what arrives per address:
how much brighter one direction is than its neighbour, which addresses are painted and which are dark, where along the
sweep the paint changes. Those are payload per address, compared between addresses, and they are unchanged when the world
is scaled. A sunflower following the light, an eye tracking an edge, a hand raised to point: each has its sweep and what
arrives along it.

The earlier essays' rule applies: this is a reading of known physics, not new physics, and nothing here says how nature
computes, or that it computes. What it says is that what a turning thing has is its sweep and what arrives along it, and
that the angle as a share of a whole turn, with π in it, is the record a writer makes afterwards, once the whole turn is
in hand.

One caution keeps the claim exact. A rate must say what it is per. Per address, against the sweep's own spacing, a rate
is a ratio of payloads and scale-free. Per second, it carries the clock's unit (radians per second, photons per second),
and moving between the two needs the clock carried in. That is a writing.

---

## 9. How the classical thinkers would describe it

Nothing here needs a new picture. Five old ones, each from a different century, already say most of it.

**The *Mechanica*** (Aristotle's school, around 300 BC) opens on the circle as "the origin of every marvel", and says why.
The radius that sweeps a circle has two motions at once, one along its way and one toward the centre, and the two are
never in a fixed ratio. If they were, the end would go straight. The changing ratio is what bends the path into a circle.
The same text holds that points farther out on the radius go faster, which led to the puzzle later called Aristotle's
wheel.

**Newton** (*Quadrature of Curves*, written 1691–92, printed 1704) treats quantities as made by motion, not built from
parts: "Lines are described, and thereby generated, not by the apposition of parts, but by the continued motion
of points … Angles by the Rotation of their Legs." His fluxions are the rates at which such quantities grow, and he
compares them one against another. A fluxion is never alone; it is always one flowing quantity against another.

**Archimedes** (*On the Sphere and Cylinder*, Book I) gives the sphere's numbers. A sphere's surface is four of its great
circles, so a hemisphere is exactly twice the flat disc under it. And slices of a sphere of equal height have equal
areas, the result that lets a globe be wrapped in its cylinder (the hat-box): a sweep up or down a sphere is even in
height.

**Ptolemy** and the astronomers after him kept two systems of coordinates on the sky. Altitude and azimuth are measured
from where the observer stands, against its own horizon and its own zenith. The equatorial coordinates are fixed to the
sky, the same for every observer, a frame that holds the whole sphere at once.

**The navigators** made it practical. Pedro Nunes (1537) showed that a ship holding one compass heading does not sail a
great circle: it sails a rhumb line, a spiral that runs into the pole. Edward Wright (1599) worked out the chart on which
such lines come out straight, the chart Mercator had drawn. So between two ports A and B there are three ways: straight
through the earth along the chord, which no ship can take; along the great circle, the shortest way on the surface, with
the heading changing all the time; and along the rhumb line, one heading held the whole way. And in plane sailing the
navigator never names an angle. It keeps two running counts, the difference of latitude (how far north or south) and the
departure (how far east or west), and reads its course as their ratio from a traverse table.

---

## 10. Our reading of them

Laid side by side, the five say what this essay says, each from one side.

**The writer goes straight; the reader has two motions.** From A to B the writer takes the chord, held whole as 1, the
way through the earth no navigator can sail. The reader stays on the surface and has what the *Mechanica*'s radius has:
two motions at once, across and up-down, the navigator's departure and difference of latitude, the reader's h and v.
That is the first line of this essay again. Writers have angles; readers have sweeps.

**How the two motions mix is the rate.** The *Mechanica* saw that a circle is two motions in a ratio that keeps
changing; the navigator's course is that ratio, read from a table, with no angle named. Newton's fluxions are what the
ratio is made of: one flowing quantity against another. In this essay's words, a rate is of something per something,
and the reader's sweep supplies the per. Along one great circle from horizontal to vertical, the mix runs at π/2 or 2/π
against the writer's chord, never at 1.

**Holding the mix fixed is a rhumb line; letting it change is a great circle.** A rhumb line is one reading held: the
same ratio of across to up-down the whole way, a single v/h. A great circle lets the ratio turn. The corner has a
navigator's name too: the course where departure equals the difference of latitude, northeast, the one heading on which
the two motions go equally fast. And Wright's chart, the one that straightens every rhumb line, is the chart OFS
Proposition 5(g) shows keeps every bearing true only when the two directions are drawn at one length.

**A sphere adds altitude, and changes the reader's numbers.** On a circle the reader compares arc with chord, and gets
π/2 and 2/π. On a sphere it compares the hemisphere with the flat disc under it, and Archimedes gives the answer: 2 at
once, ½ one direction at a time (the mean of a direction's projection onto the axis, over the hemisphere by area). The
product is still 1, and the writer's 1 is still their geometric mean, the corner between them. Archimedes' equal slices
are why the up-down sweep is the even one: a sweep uniform in height is uniform over the sphere, which is how the fifth
essay's wedge is laid.

**Altitude and azimuth were always the reader's.** Ptolemy's two systems are this series' two vantages. Altitude and
azimuth are measured from a standpoint, against one's own horizon: a reader's sweeps. The equatorial frame is fixed to
the sky and holds all of it: a writer's frame, from no standpoint.

**What is ours.** Every piece above is classical: the two motions, the fluxions, the hemisphere's 2, the observer's
coordinates, the rhumb line. What this essay adds is the sorting. The straight chord and the angle are the writer's; the
two motions and their mix are the reader's; the mix is a rate, of a payload per address; and the three numbers 1, π/2 and
2/π, or on a sphere 1, 2 and ½, are the writer's rate and the reader's two.

This is a picture still being settled. Which of the navigator's three ways the series should name as the reader's
three, the chord with the two motions, or the chord, the great circle and the rhumb line, is left open here.

---

## 11. What it comes to

**Writers have angles; readers have sweeps.** An angle is a share of the whole turn, measured at rate 1, arc per radius,
against a turn held complete. A sweep is what one length does from where it stands, and from either even pivot it comes at
its own rate: π/2 from the middle, 2/π from a point of the circle. Never 1. The 1 is the writer's, and the reader has it
only by joining the two sweeps.

**A rate is of something, per something.** The per is the sweep's: the addresses, given before anything arrives, their
spacing the frame's own rates. The of is the payload, met. What a reader reads is payload per address.

**The corner is where two rates meet**, v filling as fast as h empties, and **the Cauchy is a speed**, turn per reading,
the per against itself with no payload in it: which is why it is the addresses' law and not what arrives.

**Tangent and arctangent are the writer's tools.** Evaluating either crosses between a direction and a share of the whole
turn, and the whole turn, with its π, is the writer's. The reader runs the tangent's addition law and the halving, and
never evaluates. Trigonometry is the completion of the sweep, not its equipment, and where the completion is available,
as it is in nearly all of practice, it is a superb tool. It is the writer's record of what the reader does by turning.

The degree on a protractor and the pitch on a roof name the same direction. The carpenter's is the one the reader has.

---

## Sources

- Euclid, *Elements*: Book III, proposition 20 (the angle at the centre is double the angle at the circumference).
- Viète, F. (1593). *Variorum de rebus mathematicis responsorum liber VIII*. Tours. (The product for 2/π.)
- Lindemann, F. (1882). Über die Zahl π. *Mathematische Annalen* 20, 213–225. (π is transcendental.)
- *Mechanica* (*Mechanical Problems*), Peripatetic, late fourth or early third century BC; translated by W. S. Hett,
  Loeb Classical Library (Aristotle, *Minor Works*). (The radius's two motions.)
- Newton, I. (1704). *Tractatus de quadratura curvarum*, appended to *Opticks*; its introduction translated by J. Harris
  (1710). (Quantities generated by motion; fluxions.)
- Archimedes, *On the Sphere and Cylinder*, Book I. (The sphere four great circles; a segment's surface.)
- Ptolemy, *Almagest*. (The observer's horizon against the sky's frame.)
- Nunes, P. (1537). *Tratado da sphera*. Lisbon. (The rhumb line is not a great circle.)
- Wright, E. (1599). *Certaine Errors in Navigation*. London. (The chart that straightens the rhumb lines.)

From this series' own record: *The Algebra of Discrete Observation* (`../archive/algebra-of-discrete-observation.md`;
its sections "Trigonometry is the completion, not the equipment", "Trigonometry is an abstraction layer; the observer
sits beneath it", and the fisheye without the tangent); in the draw repository, *The Tangent Bridge Theorem* in its
algebraic form (`papers/tb_algebra.md`: the two charts and their exchange rate, and §7.5, "The coefficient is algebraic;
its π is the normalization") and the format's specification (`papers/tvf.md`, "The kernel is rational, and the decoder
can be trig-free").

The geometry is in *Observation from Somewhere*: §2, "Zero, and a new zero" (the turn met, not computed; tangent
addition); §4, "Why the corner sits at 45°", "Why there are two sweeps, and only two" and "Rates, not angles" (the two
sweeps' rates, the writer's 1, and payload per address); §7.1 (the uniform turn and the Cauchy).
