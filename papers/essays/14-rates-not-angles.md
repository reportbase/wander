# Rates, not angles

*The fourteenth of a series of essays on what can be known from where one stands. Draft, 30 October 2026.*

A carpenter calls a roof "six in twelve": it rises six for every twelve it runs. A road sign says "10%": the road climbs
ten for every hundred it goes. A wheelchair ramp is built to "one in twelve". None of them says an angle. Nobody on the
site needs to know that six in twelve is 26.57°, and if someone asks, the number has to be looked up, or computed by a
function that sums an infinite series. The pitch itself is had at once, with a level and a tape.

The pitch is a rate: so much rise for so much run. It is the reading the earlier essays have called v/h, a direction held
as a ratio. The degrees are something else, a share of the whole turn, and to give one you have to hold the whole turn
first. This essay is about the difference. Its claim is short. The sweep, one length turning from where it stands, gives
**rates**: one increment of the sweep against another. The three numbers that keep coming back, 1, π/2 and 2/π, are
three of those rates, and none of them changes when the world is scaled. Angles, and the tangent and arctangent that
convert between an angle and a rate, are the writer's tools: they need the completed turn. The reader runs the sweep and
never needs them.

None of this corrects trigonometry. It says where trigonometry sits.

*Demos: `facing.html` (the facing turns twice as fast as the sweep); `one-read.html` (arc over chord and chord over arc,
their product 1 at every θ); `paths.html` (the turn and its projection, π/2 and 2/π at the horizon); `mountain.html`
("the two vantages" on the thumb's circle); `sweep-zero.html` (a turn counted by itself, and a new zero composed by
tangent addition); `slide-rule.html` (the circular rule: a turn from a new zero against tangent subtraction).*

---

## 1. What one length turned gives

Hold out an arm of length H and raise it. The second essay drew what it traces, a quarter of a circle, and named the two
shares of the arm's length: h along the ground, v straight up, h = v at the corner. Here look at the turning itself.

Take one small step of the sweep. The tip moves along the arc by that step (measured in H, the arm's own length). In the
same step v rises, by h times the step, and h falls, by v times the step. Near the ground v rises almost one for one and
h barely moves; near the top it is the other way round. Nothing in this needs an angle to be named. It needs a step, and
what each share does during it.

So everything the sweep gives comes as one increment against another:

- the arc against the step of turn (the sweep against itself);
- each share against the arc (how fast v fills, how fast h empties);
- the reading v/h against the arc (how fast the readings go by);
- one pivot's arc against another's (the two sweeps of the second essay).

Each is a **rate**, and each is a ratio of two increments of the same sweep. Scale the world by k: the arm, the arc and
both shares are all k times as long, and every one of these rates is what it was. By the first essay's test they are
readings. The reader has them free, from where it stands, by turning.

What the reader does not have is the turn's position as a number on a scale fixed in advance. It has the arc by turning
through it, met, not computed (the second section of *Observation from Somewhere*, "Zero, and a new zero"). The
arctangent is the writer's formula for how much of the turn a reading has passed.

---

## 2. The corner, as a meeting of rates

Where is the corner? The second essay found it three ways: the one ratio the reciprocal leaves alone, the halfway point
of the turn, the place where the facing stands square to the chord.

Here is a fourth, in rates. As the sweep goes, v fills and h empties. Early on v fills fast and h hardly moves; late, h
empties fast and v hardly moves. There is one place where v fills exactly as fast as h empties. That place is the
corner. It is where the rate of v and the rate of h trade places, which is why v − h changes sign there at its steepest:
the corner is a crossing, not a turning point.

No 45° was used. "45°" is the writer's name for the corner, the corner written as an eighth of the whole turn. The reader
finds it by the rates alone.

---

## 3. The three numbers

**1.** The sweep against itself: a step of arc per step of turn, measured in the arm's own length. This is the reader's
own rate, H in H. It is what the first essay called the reader's one length, read against itself: the only amount the
reader holds, and it holds it as 1.

**2/π.** Over the whole quarter sweep, v rises from nothing to the whole arm, 1, while the arc runs π/2. On average, then,
the share fills at 2/π per unit of arc. That is the mean rate of the projection, how fast the straight reach grows
against the curve, and it is the inscribed sweep's number: chord over arc. Along the way the running value is
sin θ/θ, from 1 at the start through 0.9003 at the corner, and it reaches 2/π only as the ray goes to the horizon,
approached and never arrived at.

**π/2.** The same rate the other way: arc per unit of straight reach, how much sweep it takes to fill a share. It is the
central sweep's number, arc over chord, running as θ/sin θ from 1 through 1.1107 at the corner, and attained when the
radius lands back on home, a point.

Their product is 1 at every point of the sweep, not only at its ends. That is not a coincidence of two constants. They are
one rate read from its two sides, and turned over and multiplied it gives back the sweep against itself, the reader's
own 1. The second essay said the two sweeps each get at the writer's 1 through the arc, one too long and one too short.
In rates the same thing is plainer: the writer holds the chord as an amount; the reader has only how fast the chord
grows against the arc, and that rate turned over.

None of the three changes when the world is scaled. They are not lengths of anything. They are the sweep's own rates.

---

## 4. Two sweeps, two rates

The second essay showed two pivots for one standpoint. A radius turned about the circle's centre moves its end one step
of arc for each step of turn. A ray turned about a point of the circle moves its end two steps of arc for each step of
turn (Euclid III.20: the angle at the centre is double the angle at the circumference). Those are the only two places
where the rate is the same wherever the ray points. Anywhere else a step of turn carries the end by 2t/(t + t′) steps of
arc, t and t′ the distances ahead and behind, which changes as the ray turns.

So the inscribed angle theorem, read this way, is a statement about rates: the facing turns twice as fast as the sweep.
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

---

## 6. Tangent and arctangent are the writer's tools

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
rate, is one the reader meets only at the horizon.

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
carefully, it is a claim about what a turning thing has to hand.

A wheel of diameter 1 rolls π along the road for each turn it makes. That is π as a rate: road per turn. The wheel does
not compute it. A planet sweeps out equal areas in equal times; the law is a rate, area against time. A pendulum, a gear
train, a sunflower following the light, a hand raised to point: each has its turning and how much of something else
comes with each bit of it. Where a quantity in physics is an angle, it is usually an angle per something, a frequency,
an angular speed, a phase advance per metre.

The earlier essays' rule applies: this is a reading of known physics, not new physics, and nothing here says how nature
computes, or that it computes. What it says is that the quantities a turning thing has are rates of its own turn against
other things, and that the angle as a share of a whole turn, with π in it, is the record a writer makes of those rates
afterwards, once the whole turn is in hand.

One caution keeps the claim exact. A rate must say what it is measured against. Measured against the sweep's own
advance, the rates are pure ratios and scale-free. Measured against a clock, they carry the clock's unit (radians per
second), and moving between them needs the clock carried in. That is a writing. The rates in this essay are all of the
first kind.

---

## 9. What it comes to

**The sweep gives rates.** Every quantity one length turned produces is one increment of the sweep against another,
and every one is unchanged when the world is scaled. They are readings.

**1, 2/π and π/2 are three of those rates.** The sweep against itself, the mean rate at which a share fills against the
arc, and the arc it takes per share filled. The last two are one rate read from its two sides; their product is the
first.

**The corner is where two rates meet**, v filling as fast as h empties, and **the Cauchy is a speed**, the rate at which
the turn passes readings. Its median and its missing mean both come from that speed.

**Tangent and arctangent are the writer's tools.** Evaluating either crosses between a rate and a share of the whole
turn, and the whole turn, with its π, is the writer's. The reader runs the tangent's addition law and the halving, and
never evaluates. Trigonometry is the completion of the sweep, not its equipment, and where the completion is available,
as it is in nearly all of practice, it is a superb tool. It is the writer's record of what the reader does by turning.

The degree on a protractor and the pitch on a roof name the same direction. The carpenter's is the one the reader has.

---

## Sources

- Euclid, *Elements*: Book III, proposition 20 (the angle at the centre is double the angle at the circumference).
- Viète, F. (1593). *Variorum de rebus mathematicis responsorum liber VIII*. Tours. (The product for 2/π.)
- Lindemann, F. (1882). Über die Zahl π. *Mathematische Annalen* 20, 213–225. (π is transcendental.)

From this series' own record: *The Algebra of Discrete Observation* (`../archive/algebra-of-discrete-observation.md`;
its sections "Trigonometry is the completion, not the equipment", "Trigonometry is an abstraction layer; the observer
sits beneath it", and the fisheye without the tangent); in the draw repository, *The Tangent Bridge Theorem* in its
algebraic form (`papers/tb_algebra.md`: the two charts and their exchange rate, and §7.5, "The coefficient is algebraic;
its π is the normalization") and the format's specification (`papers/tvf.md`, "The kernel is rational, and the decoder
can be trig-free").

The geometry is in *Observation from Somewhere*: §2, "Zero, and a new zero" (the turn met, not computed; tangent
addition); §4, "Why the corner sits at 45°", "Why there are two sweeps, and only two" and "Rates, not angles" (the three
numbers as rates); §7.1 (the uniform turn and the Cauchy).
