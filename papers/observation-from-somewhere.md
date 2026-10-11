# Observation from Somewhere

**Addresses, payloads and the geometry of a situated reader**

*Tom Brinkman, with Claude. Draft for external review, 11 October 2026.*

## Abstract

Classical geometry is drawn from nowhere: every length is held at once, to one scale, by no one in particular. A reader
that stands somewhere has less. It knows its own breadth but not the breadth of what it reads. This paper works out the
geometry that this one restriction leaves. Any relation between two parties can be written as a pair of fill levels, h
and v, each between 0 and 1, and the reader reads their ratio. Because neither fill level can pass 1, every such sweep
turns over at a single point, v = h, the *corner*, where reading v in terms of h gives way to reading h in terms of v.
To read at all, the reader must use its own breadth as the unit for the other party. With that choice the corner lies at
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

This paper asks what geometry such a reader has. The answer is not a new geometry of the world. It is a geometry of the
reader's own *addresses*: the places where readings can be put, which exist before anything is read and do not depend
on what is found there.

**A picture.** Hold your hand out flat, palm down, and turn it until it points straight up. The motion between is a
sweep. Spread your fingers between flat and upright: each finger is a direction in which you can look, an address. Now
put a ring on each finger. The rings are what you find in each direction, the *payload*. Turning the hand does not
change the rings, and swapping the rings for others does not change the fingers. Much of what follows is the
mathematics of the fingers alone, and the main result is that one well-known distribution, the Cauchy, is entirely
fingers.

**Three vantages.** A figure can be held in three ways. The *completed* vantage holds every breadth at once from no
standpoint; this is classical geometry, and its figure is the circle. A *situated* reader has a facing. Either it takes
in a hemisphere at once, from outside (a parallel reader), or it sweeps the hemisphere from home, one direction at a
time (a serial reader). The three read the same thing differently. Take a line of true breadth 1. Stand a half-turn on
it as its chord: the arc is π/2, and the hemisphere turned away from the reader reads π/2. Sweep a bar of length 1
through a quarter turn and average its shadow on the line: (2/π)∫₀^{π/2} cos θ dθ = 2/π, and the hemisphere turned
toward the reader reads 2/π. The product is 1. The true breadth is had only with both hemispheres in hand, which no
single observation provides. A situated reader can construct it from several observations, as a survey is built from
many exposures, but it cannot observe it. Many apparent paradoxes come from reading one vantage's geometry as if it were
another's, most often from treating the completed view as if a single observation held it.

**What the completed view costs.** In h² + v² = 1, h and v are not compared with each other. Each is compared with the
equation, which supplies the common scale, the constant and the equals sign: the equation is a third party. A completed
account holds the whole figure and so cannot state an order of arrival; a situated account states the order of arrival
and cannot hold the whole figure. And the point on which the situated reading turns, the corner, is an unremarkable
point of the completed drawing.

**Results.**
- Every sweep between two parties turns over at one point, the corner v = h, the only point left fixed when the two
  parties are exchanged. Near and far are one geometry, read from either side of it (§3).
- A reader that holds one breadth must use it as the unit for the other party. This puts the corner at distance 1
  whatever unit is chosen and, with Euclidean length, makes the relation a unit circle (§4).
- Inside the corner the reader can lay readings out in proportion; past it, if no scale is preferred, only a
  logarithmic layout is consistent. The reader has two address spaces joined at one corner (§5).
- **Main result.** Sweeping the circle evenly from home yields the Cauchy distribution, and the Cauchy is the reader's
  addresses, not its payload. Whatever is met in each direction cancels from the reading. Order survives every change of
  payload and sums do not, which is why the Cauchy has a median, at the corner, and no mean (§6).
- How finely a reader reads is a count the geometry leaves open, and the choice of unit is a zoom, not an escape (§7).
- The geometry does not supply amounts; a fact shared between two readers supplies exactly one ratio (§8).

Section 9 discusses a single principle that may underlie all of these, the assumptions they rest on, and related work.
The paper is geometry only. It makes no claim about physics, perception or the structure of spacetime.

## 2. Setting

**Shares.** Everything here is built from a share of something: all of it, none of it, or anything in between. Take two
such shares, each of its own whole: the fraction of a tank filled and the fraction of a day gone, or the part of a road
behind and the part ahead. Draw one horizontally and one vertically and call them h and v. They are *fill levels*,
numbers in [0, 1] with no units. The wholes they are shares of are the *breadths* H and V, which are amounts. The reader
is H, its own breadth; h is the reader's side of a relation.

**Fill levels are not amounts.** The amounts are h·H and v·V, so their ratio is (v·V)/(h·H) = (v/h)·(V/H). The ratio of
fill levels, v/h, is not the ratio of amounts, V/H. The only way from one to the other is to multiply by a breadth,
which must be known. We keep lowercase letters for fill levels and uppercase for breadths throughout.

**The sweep.** Within one observation neither breadth changes. The *sweep* is every way h and v can relate, from all of
H (v = 0) to all of V (h = 0). Leaving *home* (v = 0), v fills against a full h. It can fill only until it too is full,
at v = h. After that the relation can continue only by h emptying against a full v. The reader reads v/h on the first
half and h/v on the second, each in [0, 1]. Exchanging the two parties, the *flip*, sends v/h to h/v. The limit
v/h → ∞, where h empties, is the *horizon*; it is never reached.

**Drawings.** The sweep fixes only the ratio v/h, so each pair (h, v) stands for a ray of pairs with that ratio. Three
drawings of the rays are useful: the *square* (each share capped at 1, the larger one full), the *line* h + v = 1 and
the *arc* h² + v² = 1. All three pass once through every ratio and meet the corner at v/h = 1. Statements about ratios
hold in every drawing. Statements about lengths, angles or areas belong to one drawing, and we say which.

**Readers.** What a reader knows of the two breadths sets its situation.

| reader | H | V | |
|---|---|---|---|
| completed | known | known | no standpoint: the circle if V = H, other shapes if not |
| parallel | known | unknown | takes in one hemisphere at once, from outside |
| serial | known | unknown | reads one direction at a time, from home |

The completed reader is the view from nowhere: a state of knowledge, not a place anyone stands. The parallel and serial
readers are situated. Neither knows how many things there are, and both meet horizons.

**Addresses and payload.** An *address* is a place in the reader's layout where a reading can be put. The range of
addresses is fixed by the geometry before anything arrives, and an address is taken from it when something does. The
*payload* is what arrives. In the picture of §1 the fingers are addresses and the rings are payload. A *lay* is a rule
that places each reading at a position in a drawing; the *room* a stretch of readings receives is measured either by
length or by number of addresses. A *facing* is one side of the corner in one freedom; a sweep from all h to all v
covers one facing. A *level* is a stretch of the reading: the first runs from home to the corner, and past the corner
each level is one doubling of v/h.

## 3. The corner

**Proposition 1.** Let x = v/h ∈ [0, ∞). Then x = 1 is the only point fixed by the flip x ↦ 1/x. The flip carries
[0, 1) onto (1, ∞) point for point, and every sweep from home passes through x = 1. This point depends on neither H nor V.

*Proof.* The flip is its own inverse and reverses order, so x < 1 exactly when 1/x > 1, and for x > 0, x = 1/x gives
x = 1. A sweep from home grows continuously from 0, so it reaches 1 before it can pass it. Finally, x = 1 means v = h, a
comparison of two fill levels, unchanged when both are scaled together. ∎

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

**Every pair has its own corner.** Any two parties have a sweep and a corner, and the corner of one pair is not the
corner of another. A corner means nothing until its pair is named.

## 4. The reader's circle

We assume three things.
- **(P0)** A relation has two parties, each a share of an assigned breadth: h of H, v of V. Assigned is not known: v
  lies in [0, 1] however large V is, but it must be a share of something.
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
other party. It is not a claim that the other's breadth equals H. Where it does not, every amount the reader reads is
off by the true V/H (§8). The rule constructs a relation calibrated in one unit and discovers nothing about the world.
Step (a) is close to a definition; we claim only that a relation needs two assigned breadths and a situated reader has
one. Under V = H the point where the two parties' amounts are equal, v·V = h·H, coincides with the geometric corner
v = h, the edge of the unit circle.

**The Euclidean choice.** Part (c) is where an assumption enters. One unit makes the axes commensurable, but "a bar of
fixed length" also needs a norm: under the largest-component norm the bar traces the square, under the sum norm the
line. The circle follows if the sweep is the turning of a rigid bar. The facing of §3 motivates that; it does not prove
it.

**Where the reader lives.** The reader stands at home, the centre of the circle its own choice creates. It is not the
circle. The circle read evenly from no standpoint is the completed view; read from home it is the fisheye of §6.

## 5. Two address spaces

Inside the corner the reader holds its unit and can lay its readings out in proportion: the near field at true scale.
Past the corner the flip makes the reading h/v ∈ [0, 1], but it does not say how that reading should be laid out. Let a
lay place a far reading x = v/h ≥ 1 at position r(x), counting addresses from home, with r increasing and r(1) = 1.

Choosing a different H multiplies every far reading, taken as an amount, by one common factor. A lay whose room depended
on where a reading sits, and not only on ratios, would then depend on the arbitrary choice of H. We therefore require
that no scale be preferred:

> **(S)** r(λx) − r(x) depends on λ alone, for all x, λ ≥ 1.

**Proposition 4.** If r is increasing and satisfies (S), then r(x) = 1 + c·ln x for some c > 0: every doubling receives
the same number of addresses, c·ln 2. If the far lay also joins the near lay r(x) = x without a kink at the corner, then
c = 1.

*Proof.* Let g(λ) = r(λ) − 1. Comparing (S) at x = μ with (S) at x = 1 gives r(λμ) − r(μ) = g(λ), so
g(λμ) = g(λ) + g(μ) for all λ, μ ≥ 1. This is Cauchy's functional equation in multiplicative form, and its only
increasing solutions are g(λ) = c·ln λ. At x = 1 the near lay has slope 1 and the far lay slope c. ∎

The premise (S) does the work. Monotonicity, a fixed corner and a matched slope are not enough by themselves:
r(x) = 1 + ln x + α(ln x)² with α > 0 satisfies all three and gives successive doublings different room. Whether (S)
follows from (P1) and (P2), or must be added, is the first question of §9. Note also that the argument for (S) passes
through amounts, by way of V = H, and that the smooth join (c = 1) is a further condition rather than a consequence of
the flip.

**Two address spaces.** Inside the corner the addresses are proportional; past it they are logarithmic, each doubling
receiving the same number. The corner is where one gives way to the other, without a kink. There is only one such
corner. Past it the levels are plain doublings laid side by side, with no corners of their own and nothing nested inside
them. They are doublings of scale, v/h ↦ 2·v/h. (Doubling the angle of the sweep instead sends v/h to
2(v/h)/(1 − (v/h)²); the two agree near home and part at the corner, which the angle doubling sends to the horizon.)

**Reality in 2H.** Measured by length rather than by count, the far field fits in one more H. The *in-place lay* puts a
far reading at length 2 − h/v from home. Level k past the corner, where v/h runs from 2^(k−1) to 2^k, then has length
2^(−k), so the whole far field, out to the horizon, lies between radius 1 and radius 2. The room per unit of v/h is
(h/v)², the Jacobian of the flip. The in-place lay holds the same addresses as the logarithmic lay, the same number per
doubling, crowded toward radius 2; a reader with finitely many addresses runs out of them at a far horizon of its own.

| drawing of the same addresses | measured by | bounded | corner at |
|---|---|---|---|
| fisheye (§6) | steps of turn | yes, a quarter turn | half the turn |
| in-place lay | length | yes, radius 2 | radius 1 of 2 |
| logarithmic lay | number of addresses | no | 1, where the even doublings start |

**Why halving.** If a level has nothing but its two ends, their order and the flip (P2), the only subdivision its
symmetries preserve is the cut at the corner into two halves: any other interior point can be moved anywhere within its
half by an order-preserving map that commutes with the flip. Applied again to each half, this gives repeated halvings.
Three parts, or any other number, need an added measure. This is Klein's criterion, that a geometry supplies what its
symmetries keep, applied to the points of a level.

**A familiar instance.** Floating-point numbers lay their addresses this way. The exponent counts levels and the
significand is a plain share within the level; below the smallest normal number, the subnormals lay one stretch in
proportion from zero. The count of levels plus the share within the current one is the logarithm laid straight between
level edges, exact at every edge and never more than 0.086 of a level from the smooth logarithm. A float differs in
having levels on both sides of 1 and a floor; the situated reader has proportion inside the corner and no floor.

**The proportion is in the addresses.** Within a doubling past the corner the addresses are even; how evenly they are
filled is up to the world. If directions are spread evenly (§6), the far share h/v has density proportional to
1/(1 + (h/v)²), so the fill falls toward the corner by 1.6 to 1 across the first doubling past it, 1.18 across the
second and 1.05 across the third. That unevenness belongs to the payload, not to the addresses.

## 6. The Cauchy distribution is the address, not the payload

### 6.1 Sweeping the circle evenly

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

### 6.2 The main result

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
(c) *Payload statistics do not.* The mean commutes with f only where f is affine on the data; for convex f,
mean f(X) ≥ f(mean X), with equality only if f is affine there or X is constant.
(d) *The Cauchy is an address law.* Over one facing its median is v/h = 1, the corner, and its quartiles are √2 − 1 and
√2 + 1, a flip pair. Its mean does not exist: ∫₀^M x·2/(π(1 + x²)) dx = (1/π)·ln(1 + M²), which grows without bound.

*Proof.* (a) is the cancellation shown. (b) Strictly increasing maps preserve ranks; the converse follows by monotone
interpolation between matched points. (c) is Jensen's inequality. (d) Over one facing the distribution function is
(2/π)·arctan(v/h), which is ½ at v/h = 1 and ¼ and ¾ at tan(π/8) = √2 − 1 and tan(3π/8) = √2 + 1; the integral is
elementary. ∎

The theorem is elementary; its content is the reading. The Cauchy distribution is not a law of anything the reader
meets. It is the reader's own layout of directions, counted. What arrives in each direction cancels from every single
reading, not merely on average, so the readings tell rays apart, not points. The Cauchy is where the reader can put what
arrives, never what arrives.

### 6.3 In the picture of the hand

Spread the fingers evenly by turn and read each one as v over h: the readings are the Cauchy, and nothing of the rings
is in them.
- *The median is a finger.* Of five fingers spread evenly from flat to upright, the middle one, at 45°, is the corner.
  Order, ranks, quartiles and the corner are address statistics, and they ignore the rings.
- *The missing mean asks the fingers about the rings.* A mean is a sum of sizes, a question about the payload. The
  readings carry no size, so the question has no answer. The median, a question about addresses, always has one.
- *More fingers, not bigger rings.* Sweeping more finely lays more addresses. It buys precision about where, never
  about what. What is at the addresses comes only from payload held beside them.
- *The rings hide; the hand does not.* Two rings on one finger, seen along it, show only the nearer. Every back side is
  made by the payload; the addresses hide nothing.
- *Three breadths.* In space the fingers fill a solid wedge and, spread evenly, give the two-variable Cauchy, with
  density proportional to (1 + |x|²)^(−3/2). Here the corner is no longer the median: only 1 − 1/√2 ≈ 0.29 of the
  addresses lie within it, and the median of |x| is √3. The median is still an address, though not the corner.

### 6.4 The shape is payload

The sweep opens a closed shape out, with home in the middle of the opening and the two ends running toward the horizon
in each facing. Opening divides out size, so each place on the opened line is an address pointing back to a point of the
closed shape, which keeps its size. Laid evenly by direction, every shape opens into the same fisheye and the same
Cauchy; the shape survives only in what arrives at each address, one breadth per direction. (We checked this on 73
outlines.) The addresses are universal, and the shape is payload.

The addresses with their payloads give the shape back, up to scale, exactly when the shape is star-shaped from the
standpoint, so that each direction meets the outline once. Otherwise some direction meets it more than once and the
parts behind are hidden: rings behind rings on one finger. Occlusion and contact need more than a value at each address
(that sight runs straight and stops at the first thing it meets), and nothing here is claimed for them.

### 6.5 Situated and unsituated

Held whole, from no standpoint, the bar's even turn traces the circle h² + v² = 1, every point like every other: no
home, no horizon and no corner of any consequence. Swept from home and read as v/h, the same even turn gives the Cauchy
when counted and the fisheye when drawn. Home, the corner and the horizon appear because the reading is taken from
somewhere. Situated geometry is the Cauchy; unsituated geometry is the circle.

Proposition 5 assumes the turn is stepped evenly, which is a choice of weight on the sweep. It is not a weight chosen to
produce the Cauchy: stepping the turn evenly is what makes the circle uniform in the first place, so one assumption,
uniformity, lies behind both. The two are still distinct: the circle's symmetry under turns is one thing, and a reader's
choice to sample in equal turns is another. Other weights fair to both facings exist, such as the line's share
v/(v + h). By Proposition 2(b) each puts the corner at its middle, but none of them gives the Cauchy.

### 6.6 What being situated costs

Two things are missing from a situated reading, and they are easily confused. The breadths are missing from every
single reading: v/h cancels them, as it cancels the reach of whatever arrives. The total of the whole is missing because
the reader's readings have no end: the horizon is never reached, so no census can be taken. The Cauchy's missing mean
belongs to the first absence, not the second. It is not a census that more readings would complete: over both facings
the mean of n Cauchy readings is distributed exactly as a single reading, whatever n is, so averaging never settles.
The readings are addresses, and a mean asks them for sizes they do not carry. A situated reader keeps order and loses
sums, and the Cauchy is the extreme case: an order law with no sum.

### 6.7 Other addresses and payloads

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

### 6.8 What is known

The Cauchy as the image of a uniform angle (the gnomonic projection of uniform measure on a hemisphere), its invariance
under Möbius maps and its missing mean are classical (Knight 1976; McCullagh 1996; Pitman and Williams 1967; Cuadras
2002; Stigler 1974), as are the facts that the mean of n Cauchy variates is again Cauchy and that order statistics
follow every increasing map. What is new here is the reading: which reader, knowing what, receives the Cauchy, and that
what it receives is its own addresses rather than anything in the world.

## 7. Level of detail and the choice of H

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
scale of the thing being read, which places that thing at the corner; focusing an eye or zooming a lens does this. The
same idea appears in the hyperbolic browser, which draws only nodes at least a pixel across (Lamping, Rao and Pirolli
1995), in mipmaps, which halve an image at each level (Williams 1983), and in web-map tiles, whose key gains one digit
per level of detail (Microsoft, Bing Maps Tile System).

**More points, fewer told apart.** A parallel reader looks side-on at N points spaced evenly around a circle and reads
each one's position across its view to a step ε, relative to the circle's radius. Neighbours at angle θ from the middle
of the view are about (2π/N)·cos θ apart, so the reader separates those with cos θ ≥ εN/2π, which is
R(N) = (N/π)·arccos(εN/2π) of them. This peaks at about 1.12/ε points, where εN/2π ≈ 0.65, and falls to none at
N = 2π/ε: past the peak, more points mean fewer told apart. Brute-force checks at ε = 10⁻³ and 10⁻⁴ agree with the
formula to within two points. The addresses never overflow; the resolution does.

## 8. What the geometry does not give: amounts

**The calibration error.** Under V = H the amounts equal the fill levels numerically, which is why the two are so easily
confused. Where the true V differs from H, every amount is off by V/H, by the same factor on both sides of the corner.
The addresses are exact; the amounts are not. Within one observation a reader cannot tell V = 10² from V = 10¹⁶. Amounts
can come only from outside the geometry, across observations, from something whose amount is already known. That is
physics, and this paper does not treat it.

**Proposition 7 (a shared fact buys one factor).** Two readers share one closed polygon. Reader A records its part as
edges, each an exact direction and a length counted in its own unit H_A; reader B records the rest in its own unit H_B.
Neither knows the other's unit. Let S_A and S_B be the vector sums of each reader's counted edges, and suppose neither
part closes by itself. Then H_B/H_A = |S_A|/|S_B|, and nothing more about the units can be recovered.

*Proof.* Closure gives H_A·S_A + H_B·S_B = 0, so S_A and S_B are antiparallel and H_B/H_A = |S_A|/|S_B|. Scaling both
units together leaves every count unchanged, so their common scale cannot be recovered. ∎

On 2000 random polygons the ratio is recovered to 5 × 10⁻¹⁵. Between two private rulers, a shared fact buys exactly the
one factor that crosses.

## 9. Discussion

### 9.1 A candidate single principle

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
two spaces coincide. The halving of §5 is the same criterion applied to points.

The three transformations form one group. On the ratio x = v/h a turn acts as the Möbius map
x ↦ (x·cos α + sin α)/(cos α − x·sin α) and a rescaling as x ↦ λx. Together they generate PSL(2,ℝ), every element of
which factors as turn, rescaling, turn; adding the flip x ↦ 1/x gives PGL(2,ℝ), the group that preserves cross ratios.
The Cauchy family is the one family of distributions this group carries into itself (Knight 1976; McCullagh 1996).

Choosing a measure by the transformations one is ignorant of is Jaynes's method of transformation groups (1968), and
dx/x for an unknown scale is Jeffreys's prior (1939). The claim would therefore not be the principle itself, but that a
situated reader's state of knowledge selects these three transformations, from which the structure follows. Two things
remain outside it. Invariant measures are fixed only up to a constant, so the smooth join at the corner (c = 1) is still
an added condition. And "no attitude preferred" still treats the sweep as the turning of a rigid bar.

### 9.2 Assumptions and open questions

1. *The link in Proposition 4.* Does (S) follow from "any H will do", or is it scale invariance assumed under another
   name?
2. *Why Euclidean?* Is there a reason, from the reader's premises, that the sweep must be a turn rather than the
   square's or the line's path through the same ratios?
3. *No measure on a level.* Is there a principled reason a level could not carry a measure before anything arrives?
4. *Fairness.* Proposition 2(b) needs the reading to treat both sides alike although the reader's knowledge does not.
   Is that more than a choice?
5. *Uniformity as the weight.* Does the argument of §6.5 remove the burden of the even turn, or only move it to "why the
   circle"?
6. *V = H.* Is Proposition 3(a) more than a restatement of having one breadth?
7. *A measured reader.* Grid cells in the entorhinal cortex map space in modules whose spacing ratios no physical law
   sets. Without an added measure, §5 allows only halving: a ratio of 2 along a line, or √2 if a level doubles an area.
   Published means lie near 1.42 (Stensola et al. 2012) and, in other studies, near 1.7. A test on per-animal data not
   yet examined is planned, and suggestions for data are welcome.

If the principle of §9.1 stands, questions 1, 2 and 5 become one: whether a situated reader's ignorance is exactly these
three transformations.

### 9.3 Related work

The pieces are classical: the flip x ↦ 1/x, the Cauchy as the projection of a uniform angle and its Möbius invariance,
Cauchy's functional equation, Klein's Erlangen programme (1872), and Jaynes's and Jeffreys's invariant priors. Near
neighbours in measured perception include Gilinsky's perceived distance with a finite horizon (1951), Schwartz's
log-polar map of visual cortex, proportional near the fovea and logarithmic beyond (1977), and the number-line
literature, from logarithmic-to-linear shifts (Siegler and Opfer 2003; Dehaene et al. 2008) to proportion judgment on
bounded lines (Barth and Paladino 2011). One test of our own against children's number-line placements did not favour a
proportional-then-logarithmic model over proportion judgment. The view from nowhere is Nagel's phrase (1986); Haraway
(1988) called the ideal of seeing everything from nowhere "the god trick". In terms of limits, classical work lets the
reader's step go to zero first and then lets the count of things grow without bound; a situated reader has a fixed step
and an unknown count.

What we claim is not the pieces but their reading as one structure, set by what a reader knows of two breadths, and in
particular that the Cauchy distribution is a situated reader's addresses, not its payload. Whether this is a better way
to compute anything is an engineering question we do not take up. The aim is to explain things that are known but not
well understood: why near and far seem to obey different mathematics, why logarithmic scales appear wherever a range is
too wide to hold in proportion, and why the Cauchy has a median but no mean.

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

Microsoft. Bing Maps Tile System (documentation).

Nagel, T. (1986). *The View from Nowhere*. Oxford University Press.

Pitman, E. J. G. and Williams, E. J. (1967). Cauchy-distributed functions of Cauchy variates. *Annals of Mathematical
Statistics* 38(3), 916–918.

Schwartz, E. L. (1977). Spatial mapping in the primate sensory projection: analytic structure and relevance to
perception. *Biological Cybernetics* 25, 181–194.

Siegler, R. S. and Opfer, J. E. (2003). The development of numerical estimation: evidence for multiple representations of
numerical quantity. *Psychological Science* 14(3), 237–243.

Stensola, H., Stensola, T., Solstad, T., Frøland, K., Moser, M.-B. and Moser, E. I. (2012). The entorhinal grid map is
discretized. *Nature* 492, 72–78.

Stigler, S. M. (1974). Cauchy and the witch of Agnesi: an historical note on the Cauchy distribution. *Biometrika*
61(2), 375–380.

Williams, L. (1983). Pyramidal parametrics. *Computer Graphics* (Proceedings of SIGGRAPH '83) 17(3), 1–11.
