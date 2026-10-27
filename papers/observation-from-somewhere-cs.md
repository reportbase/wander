# Addresses Given, Payloads Met

**The geometry of a situated reader, for computer science**

*Tom Brinkman, with Claude. A companion to "Observation from Somewhere", 27 October 2026.*

*This paper restates "Observation from Somewhere" for readers whose background is computing. It is drawn from that
paper and claims nothing it does not; where the two differ, that paper stands and this one is to be fixed.*

## Abstract

Every programmer keeps two things apart without thinking about it: where a value can be put, its index or key, and the
value stored there. An array's indices exist before anything is written into it, and writing a value moves no index.
This paper is about a geometry with the same split. A reader that stands somewhere has *addresses*, the directions from
its standpoint, and meets *payloads*, whatever arrives along them. The addresses are given by the standpoint alone,
complete, before anything arrives; the payload is what the world puts on them, and it moves no address.

The ideas were first met in computing: in arrays indexed by turn, in floating-point numbers, in depth buffers, in
level of detail for viewers of very large data. The paper states the geometry under them exactly, and finds that one
well-known distribution belongs entirely to the index side. Stated plainly: directions taken uniformly by turn from
where a reader stands, each read as a ratio v/h, follow the Cauchy distribution, and that law is the turn's own,
whatever is stored at the directions. Whatever arrives along a direction cancels from its reading. The Cauchy's median
exists and sits at v/h = 1, because a median depends only on order, which belongs to the addresses; its mean does not
exist, which costs nothing, since a mean is a sum of sizes, a question about the payload. The three are kept apart:
any sweep that treats the two parties alike puts its median at v = h; if its weight also stays above zero near the
horizon, it has no mean; and only the uniform turn of the reader's one length gives the standard Cauchy's exact
shape. In the vocabulary of
computing, order statistics are index statistics and sums are value statistics, and this is a theorem rather than a
convention.

Around that result the geometry gives, from one chosen value H and nothing else: a split of every reading into a near
register and a far register at one point, v = h, which needs no division to find; a layout that is proportional inside
that point and, if no scale is preferred, logarithmic past it, the layout floating-point numbers already use; a fixed
count of addresses, K, that covers a world of any size N with no table built for N; and H as a zoom, which decides
where the finest of the K addresses fall and changes no reading. The uniform turn is a measure, not a procedure: no
loop runs to produce the addresses. And the fraction that `Math.floor` throws away turns out to be address, not data: its digits are
the finer levels, a second coordinate of the address, and the cells they pick out tile the hyperbolic plane in which the
Cauchy's own parameters live. The measure is standard mathematics; reading it as a reader's addresses is the
paper's interpretation, and every result is stated so that it can be checked apart from that reading.

In one sentence: the address scheme and the magnitude met at an address are distinct mathematical roles, and a geometry
can specify the former without determining the latter. So ratios suffice for everything a reader does from where it
stands; a blueprint, a statement in amounts, adds capabilities an intricate system of many parts may need and a reader
does not.

## 1. Introduction

### 1.1 Index and value

A blueprint states a thing in amounts: every line at its true length, to one scale, facing no one. To draw it you need
the true sizes, and you get them by measuring the whole object or by being handed a measurement someone made before.
Call whoever states things this way a *writer*. (The word means stating amounts; it has nothing to do with a memory
write.) A *reader* stands somewhere. It has one scale of its own, a value it chooses to start from rather than a size it
measured, and it does not know the size of what it reads.

The question is what geometry such a reader needs. Our answer, put as a thesis:

> A situated observer does not possess a coordinate system for the world; it constructs an addressing scheme from
> relations available at its standpoint, and uses those addresses to encounter the world's magnitudes.

The analogy to storage is direct, and it is where the ideas came from. Three things are kept apart:
- the *object*, whatever exists independently of any reading of it;
- the *address*, the place in the reader's scheme at which something can be met (the index);
- the *payload*, the magnitude met there (the value).

A change of coordinates moves addresses and payloads together, as re-indexing an array moves its values with it. The
separation here lets either change without the other. Changing what arrives leaves every address in place (Theorem 6),
and changing the standpoint changes the addresses without touching the object.

### 1.2 A measure, not an algorithm

Classical pictures of this geometry are processes: a ray stepped across a quadrant, a lamp turning on a shore, a
needle dropped again and again. A programmer reads them as loops. The mathematics under them is not a loop. The uniform
turn is a measure on directions, the one every rotation leaves unchanged, and a measure is given whole: the share of
the quarter turn below a direction, (2/π)·arctan(v/h), is a fact about that direction, not a counter that a loop has
advanced to. So throughout, "in equal steps of turn", "swept uniformly" and "counted" are said of the measure and of the
order it puts on directions, never of an act. Nothing in this paper is an algorithm a reader runs.

A real reader may count against something else: a clock, the equal pixels of a flat screen, or whatever happens to
arrive. Each of those is another weight, with its own consequences (§12, §13).

### 1.3 A picture

Hold your hand up to a stained-glass window, fingers spread between flat and upright. Each finger is a direction you can
look in, an address, and each is lit by the pane it lines up with. The fingers are there before any light reaches them,
and they are the same wherever you hold the hand. The coloured light is what arrives along each direction, the payload.
Put another window in its place and the fingers stay; only the colours change. The colour says nothing about how far
off its pane is: two panes on one line show only the nearer, and to learn the distance you have to walk, so that the
panes slide across one another. Much of what follows is the mathematics of the fingers alone, and the main result is
that the Cauchy distribution is entirely fingers.

Your thumb is your own breadth, H: the one measure you hold up, chosen because it is to hand, and the only length you
have. The mountain you look at has a true breadth of its own, V*, which you may not know. Not knowing it, you set
nothing, having no second length: the mountain arrives as directions on the circle your thumb traces, read in thumbs. A
writer looking at your drawing would say you had drawn the mountain at your thumb, V = H.

### 1.4 What is new, and what is not

That coordinates depend on the observer is old, and so is keeping a location apart from its value: an array's index and
its contents, a function's domain and its values, a sampling grid and its samples. The pieces used here are classical: the reciprocal x ↦ 1/x, the Cauchy
as the projection of a uniform angle and its invariance under Möbius maps, Cauchy's functional equation, Jaynes's
transformation groups. What is new is where the reader's scheme comes from (the relations available at its standpoint,
before any payload arrives) and the reading of these pieces as one structure, in which the Cauchy is the index and not
the data. Whether this is a better way to compute anything is a question this paper does not take up; §12 says what it
offers instead, a baseline against which existing designs can be read.

### 1.5 Results

- **The separation.** Directions taken uniformly from where the reader stands follow the Cauchy, whatever is met along
  them. Order statistics survive every change of payload; sums do not. So the Cauchy has a median, at the corner, and
  no mean (§5).
- **The corner.** Every relation between two parties turns over at one point, v = h, the only point the exchange of
  the two parties leaves fixed. Two registers, v/h below it and h/v above it, both stay within [0, 1] only if the
  switch is there. Sameness, order and the corner need no division (§3).
- **One length.** The reader holds one length, H, and turns it; the orbit is a circle because the length is fixed, and
  the uniform turn's readings are the half-Cauchy on one quadrant, its median at the corner (the standard Cauchy
  signed over two). No breadth is given to the other party: V belongs to a writer,
  and V = H is the writer's name for the reader's circle. Working back from the Cauchy, on one quadrant its median at the
  corner, arrives at a turn of one length (§4); a drawing with two axes at V = cH gives a Cauchy of scale 1/c.
- **Arrays.** For an even-length array indexed at equal steps of turn, the slopes of its places are exactly the evenly
  spaced quantiles of the Cauchy. The index is the address and the stored values are the payload; the floor function
  is where an array is not a reader (§6).
- **Two address spaces.** Inside the corner the addresses are proportional; past it, if no scale is preferred, only a
  logarithmic layout is consistent. Floating-point numbers are an instance (§8).
- **What Math.floor throws away.** The fraction the floor drops is not data but address: its binary digits are the
  finer levels, and they are the address's second coordinate. The dyadic cells tile the hyperbolic plane, the space of
  the Cauchy's own parameters, every level alike and every cell of one room; a tree keeps the levels but not the plane,
  and the floor's loss of detail is a wall where a reader's is a soft cut (§7).
- **A fixed count.** A reader's K addresses cover a world of any size N, with no table and no knowledge of N; H is a
  zoom that places them and changes no reading (§9).
- **Ratios suffice; a blueprint adds.** Everything a reader does from where it stands runs on ratios; a blueprint, the
  writer's statement in amounts, adds the size, parts that meet out of view, sums, the join, a statement made in
  advance and a far field in proportion common to every reader. No reading fixes scale; one amount supplied from outside fixes it everywhere it is linked (§10).
- **A dial.** A held push adds to the hyperbolic angle; the place is its sinh and the screen its turn. The whole list
  stays on a bounded screen, its end the horizon, and any place up to N is reached in about ln(2N)/rate, with no
  table and no count in the control (§11).
- **What comes free.** A depth buffer is the in-place lay with H at the near plane; equal pixels on a flat screen
  over-weight directions off the axis; tables fixed in advance need what the uniform turn does not (§12).

## 2. The model

### 2.1 Unit relations

Everything is built from the *unit relation*: a number from 0 to 1 relating a part to its whole, like the fraction of a
day gone or the share of a road behind. A relation needs two of them, one for each party. Draw one horizontally and one
vertically and call them h and v. They have no units, and neither knows the other's whole.

The wholes are the *breadths* H and V, written in uppercase. H is the reader's own, the one value it chooses to start
from; V is the length at which the reader draws the other party; V* is the other party's true size, an amount the
reader does not have. The amounts are h·H and v·V*, so

  (v·V*)/(h·H) = (v/h)·(V*/H).

The ratio of unit relations, v/h, is not the ratio of amounts, V*/H. The only way from one to the other is to multiply
by a breadth, which must be known. In programming terms these are two types, a unitless ratio and an amount in some
unit, and the paper keeps them apart as a type system would: lowercase for unit relations, uppercase for breadths and
amounts. Most confusion in this area is a silent cast from one type to the other.

### 2.2 A reading is a direction

A reading is a pair (h, v) with h, v ≥ 0, not both zero, taken up to a common factor: a direction [h : v], a point of
the projective line, in the homogeneous coordinates graphics programmers use for the same reason (to keep a point at
infinity as an ordinary value). The pair's size, its position along its own ray, is exactly what dividing one unit
relation by the other removes.

The usual pictures of a relation are normalizations of that ray, each a different cut:

| cut where | two unit relations | three unit relations | normalized by |
|---|---|---|---|
| length = 1 | quarter circle h² + v² = 1 | the sphere's octant | ℓ₂ |
| largest = 1 | the unit square's two arms | the unit cube's three faces | ℓ∞ |
| sum = 1 | the line h + v = 1 | a flat triangle (the simplex) | ℓ₁ |
| one unit relation = 1 | the reading v/h on [0, ∞) | the plane of v/h and v₂/h | a denominator |

Every cut passes once through every ratio and meets v/h = 1 once. Statements about ratios hold in every cut; statements
about lengths, angles and areas belong to one. The sum cut needs no standpoint, only addition: it is the writer's
drawing. Every other cut is built from a standpoint.

### 2.3 Addresses and payload

An *address* is a place in the reader's layout where a reading can be put. The range of addresses is fixed by the
geometry before anything arrives. The *payload* is what arrives: a wave of some kind, sent out or shaped by the things
read, not the things themselves; it paints the address it arrives along. The addresses do not depend on what arrives at
them. Every "if" belongs to the payload, including which side of the corner a given reading falls on.

An address is a point; a payload is a function on the points. The law of the addresses is a measure on the points,
fixed by the standpoint and the turn alone. Any payload can be swapped for any other, at any address, and no address
moves.

### 2.4 Zero, and composition

Zero is the direction the reader faces, the start of the quarter turn. Facing another way gives a new zero and changes
nothing in the law. Readings from two zeros compose as turns compose, by tangent addition,

  s ⊕ t = (s + t)/(1 − st),

and a full round composes to no turn, a closure check. Directions have no sum, only this composition. Repeating one
step t comes back to zero after finitely many steps only for t = 0, 1 and ∞ among the rationals (Niven 1956); every other
rational step never closes, and its multiples spread uniformly round the turn (Weyl 1916).

Comparing two directions needs no division either. Of [h₁ : v₁] and [h₂ : v₂], the second is farther from home exactly
when the bracket `D = v2*h1 - v1*h2` is positive: a cross product, exact in integers, zero when the two are one direction.
Its square and the dot product's add to the product of the norms, D² + (h₁h₂ + v₁v₂)² = (h₁² + v₁²)(h₂² + v₂²) (Lagrange's
identity in two dimensions), and only D's sign says which way round the two lie. The comparison is transitive with no
quotient: D(A, C)·h_B = D(A, B)·h_C + D(B, C)·h_A (the three-term Plücker relation; Plücker 1865), so a sort by the
bracket alone is a sort. Tangent addition, though, counts turns only modulo a half turn: readings composed round a loop
close alike after one round and after two, and a program that needs the winding number must count passes through the
horizon itself.

## 3. The corner

**Proposition 1.** Let x = v/h ∈ [0, ∞). Then x = 1 is the only point fixed by the reciprocal x ↦ 1/x. The reciprocal
carries [0, 1) onto (1, ∞) point for point, and every sweep from v = 0 passes through x = 1. This point depends on
neither H nor V.

*Proof.* The reciprocal is its own inverse and reverses order, so x < 1 exactly when 1/x > 1, and x = 1/x gives x = 1
for x > 0. A sweep from 0 grows continuously and reaches 1 before it can pass it. x = 1 means v = h, a comparison of two
unit relations, unchanged when both are scaled together. ∎

This point is the *corner*. It is ordinary arithmetic. Its importance is that it separates two ways of reading: before
it, v is read in terms of h; past it, h in terms of v.

**Proposition 2.** (a) Let a reader hold x in two registers: x itself where x ≤ a, and 1/x where x > a. Both registers
stay within [0, 1] if and only if a = 1. (b) Let f : [0, ∞) → [0, 1] be strictly increasing and *reciprocal-symmetric*,
f(1/x) = 1 − f(x). Then f(1) = ½, and f maps the near side below ½ and the far side above it.

*Proof.* (a) The registers take values in [0, a] and (0, 1/a); both lie in [0, 1] exactly when a ≤ 1 and 1/a ≤ 1.
(b) At x = 1 the condition reads f(1) = 1 − f(1); the rest is monotonicity. ∎

Part (a) is a fact about fixed-width storage: a reader that keeps a bounded register must switch at the corner and
nowhere else. Reciprocal-symmetric readings include the line's share x/(1 + x) and the arc's x²/(1 + x²).

**The closed line.** The readings form a closed arc of the projective line with two ends, home [1 : 0] and the horizon
[0 : 1], and two charts: x = v/h, defined everywhere but the horizon, and y = h/v, defined everywhere but home. The
exchange [h : v] ↦ [v : h] swaps the ends and the charts and fixes one point, the corner [1 : 1]. A chart that sends an
end to infinity has no mean for the uniform law; a bounded chart of the same arc, the angle θ or the share x/(1 + x),
has one (π/4 and ½). So the missing mean of §5 is a fact about the chart in which directions are written as numbers,
not about the directions.

**Division by zero.** The same holds for the oldest singularity in computing. A program that keeps a direction as one
number, a slope v/h, has chosen the chart x, and x sends the horizon to infinity. Dividing by zero is that chart reaching
its own end, not anything in the direction: as a pair, [0 : 1] is as ordinary as home, [1 : 0], and the chart y sends
home to infinity instead. The reader holds the pair and divides nothing; the reading is the ratio itself, and a quotient
appears only when a direction is written as one amount over another, as a writer writes it. Computing has met this
piecemeal, and each remedy keeps the pair:

- *Homogeneous coordinates.* A graphics pipeline carries [x : y : z : w] and divides by w last, after clipping; w = 0 is a
  point at infinity, a direction, held like any other point.
- *`atan2(v, h)`.* It takes the pair, so the horizon is the end of the quarter turn and not a fault (§6's `turnIndex`
  relies on it). The bracket D of the next paragraph compares two directions with no quotient at all.
- *Floating point's infinities.* IEEE 754 gives 1/0 = +∞ and −1/0 = −∞, closing the line at two ends, its affine
  closure, and 0/0 = NaN, which is [0 : 0], the one pair that names no direction (§2.2 leaves it out). The 8087 also
  offered a projective mode, one unsigned infinity, which closes the line as a circle of directions does; the 1985
  standard kept only the affine one (IEEE 1985). Posits close it again with a single point at infinity (Gustafson and
  Yonemoto 2017).
- *Integers* have no infinity and trap: they are amounts alone.

The rule that follows is a representation's, not a numerical trick: where a value is a direction, keep the pair and
divide last, if at all; where it is an amount over an amount, a zero denominator is a real absence (a rate over no
elapsed time, a mean of no items), not a horizon, and no closure of the line repairs it. That zero belongs to
the sums of amounts a blueprint adds (§10, capability 3); the readings, which run on ratios, have only the chart's.

**Comparing without dividing.** For readings (h₁, v₁) and (h₂, v₂) let

  D = v₁·h₂ − v₂·h₁,

the 2 × 2 determinant of the two pairs. With h₁, h₂ > 0, D = 0 exactly when the ratios agree, and D > 0 exactly when
v₁/h₁ > v₂/h₂. Comparing a reading with its own reciprocal gives D = v² − h², zero exactly at the corner. Sameness,
order and the corner need no division; only the size of D depends on scale.

**Series stop at the corner.** The expansion 1/(1 + x²) = 1 − x² + x⁴ − … converges for x < 1 and diverges for x > 1;
past the corner the expansion in 1/x converges instead, since the singularities at ±i lie at distance one from zero.
This is a property of expansions, not a break in the function, but it is one reason near and far seem to obey different
mathematics, and one reason a numerical routine evaluates them by different formulas.

## 4. One length: the reader's circle

We assume three things.
- **(P0)** A relation needs two unit relations, one for each party. For a writer, who holds both hemispheres, each
  relates its party to that party's breadth; a situated reader has no V, and for it both are shares of its one length.
- **(P1)** A situated reader holds exactly one length, H, and no whole of the system. H is not a measured size, and any
  H will do.
- **(P2)** A level carries no measure: nothing on it but its two ends, their order and the reciprocal between them.

**Proposition 3 (the reader's circle), in part.** Under (P0) and (P1):
(a) the reader holds no breadth for the other party, so it has no c; a writer can write the reader's drawing with two
axes as V = cH, and no unit relation and no single reading depends on c;
(b) the corner lies at distance 1 from home, in H, whatever H was chosen, and a reader with unit λH in a world
scaled by λ receives exactly the same readings;
(e) on a page with two axes, V = cH, the attitudes are turns of one rigid bar only if c = 1: with c ≠ 1 nothing turns
all of h into all of v, and there is no circle. So the reader's circle, written with two axes, is V = H.
(g) The bar can be derived rather than assumed: a sweep that is uniform (every step the same linear map of the plane),
returns to its start after one full turn, and carries all of h into all of v in a quarter of it, preserves an inner
product unique up to a positive factor. In that inner product every attitude has one length and
(h, v) = (cos ωt, sin ωt). The one factor left free is that length, H.

(The proofs are in the parent paper. Part (g) is linear algebra: exp(TA) = I forces A to be conjugate to a rotation
generator, and any symmetric form it preserves is a multiple of one.)

**Proposition 5, in part.** Take the reader's one length turned, and directions uniformly by turn on the quarter
circle. Then:
(a) equal steps of turn give unequal readings: near zero a step barely changes v/h, and near upright each step changes
it without bound;
(b) per unit of v/h the directions have density 2/(π(1 + (v/h)²)) on [0, ∞), the half-Cauchy, with its median at the
corner and unchanged by the reciprocal; signed over two quadrants it is the standard Cauchy, quartiles at ±1;
(d) conversely, on a page or an instrument drawn at V = cH and taken uniformly by direction in the drawing, the readings follow the law of (b)
if and only if c = 1.

*Proof of (b) and (d).* When the bar turns by dθ, v/h changes by dθ/h², and on the circle 1/h² = 1 + (v/h)². Drawn at
V = cH, a uniform direction θ′ has tan θ′ = c·(v/h), so P(v/h ≤ r) = (2/π)·arctan(cr): a half-Cauchy of scale 1/c,
the law of (b) exactly when c = 1. ∎

So the order is: hold H, turn it, obtain the circle, and with the uniform measure obtain the Cauchy. The Cauchy is not a
law laid on a circle that already held a V; it is the measure of the addresses the one-length turn makes. Within this
construction (two unit relations, a rigid bar's linear periodic turn) working back from the Cauchy (the half-Cauchy on one quadrant) arrives at
a turn of one length, and on a page with two axes at c = 1 and nowhere else. "V = H is still a choice" is a writer's
objection: only one who holds both axes sees c as a number to set, and the reader holds one. It is not a claim about
the world either: where the true V* differs from H, every amount taken from the reader's circle is off by V*/H (§10).
The addresses are exact; the amounts are not.

The parent paper shows c = 1 required in two familiar drawings with two axes: a lighthouse whose flashes land on a straight
shore, and Mercator's chart, which draws every compass bearing true only because it stretches north–south exactly as
much as east–west.

**Three parties.** With a third unit relation v₂, read against the same h, the directions fill one octant of the sphere,
a *wedge*. Read on the one length H (a writer would write V = V₂ = H) and taken uniformly by area (Proposition 5(e)), the readings (s, s₂) = (v/h, v₂/h) have
density 2/(π(1 + s² + s₂²)^(3/2)), the two-dimensional Cauchy. Each of v/h, v₂/h and v/v₂ alone has the law of (b) with
its median at its own corner; the six orderings of h, v and v₂ are equally likely, so h is the largest for a third of
the octant. With n other parties it is 1/(n + 1). Uniform area is the only probability on the sphere every rotation
leaves unchanged (Haar's uniqueness); it is selected by treating every turn alike, a premise, not forced by bounded
observation alone.

## 5. The main result: index statistics and value statistics

> **The Cauchy is not the payload; it is the address to the payload.**

Call a statistic of a set of readings an *address statistic* if it depends only on their order (the ranks, the median,
the quartiles, which side of the corner each lies on), and a *payload statistic* if it depends on their sizes (the mean,
any sum). In computing terms, the first kind can be computed from a sort, and the second needs the values.

**Theorem 6 (the separation of address and payload).** Parts (a) and (d) concern the readings of Proposition 5 (the
reader's one length, directions uniform by turn). Parts (b) and (c) hold for any finite set of readings. Part (e) drops both the circle and
the uniform turn.

(a) *Nothing that arrives changes the Cauchy.* Suppose whatever arrives along each direction lies at some reach ℓ > 0,
an amount that may differ from direction to direction and is unknown to the reader. Its components are ℓ·h and ℓ·v, and
the reading is (ℓ·v)/(ℓ·h) = v/h. The readings and their law are therefore the same whatever arrives, and are fixed
before anything does. What does not cancel is the ratio of amounts, (v·V*)/(h·H), which keeps the factor V*/H.

(b) *Address statistics ignore the payload.* For a finite set X of readings and any strictly increasing map f, f(X) has
the same ranks as X, so every address statistic picks out the same element; for an odd count,
median f(X) = f(median X). Conversely, two sets with the same ranks are carried onto one another by some strictly
increasing f, so ranks keep exactly what survives every such change, and nothing more.

(c) *Payload statistics do not.* Among strictly increasing maps, only an affine f commutes with the mean on every set:
for any f that is not affine there is a set X with mean f(X) ≠ f(mean X). For convex f, mean f(X) ≥ f(mean X), with
equality only if f is affine on the range of X.

(d) *The Cauchy is an address law.* Over one quadrant its median is v/h = 1, the corner, and its quartiles are √2 − 1
and √2 + 1, a reciprocal pair. Its mean does not exist: ∫₀^s x·2/(π(1 + x²)) dx = (1/π)·ln(1 + s²), which grows without
bound.

(e) *The median needs only reciprocal symmetry, and the missing mean a density of h bounded away from zero near the
horizon.* Let the directions follow any path from all of h to all of v, with any weight, both unchanged by exchanging
the two parties. Then the median is the corner. If moreover the weight gives h a density bounded away from 0 near the
horizon, the mean does not exist. The uniform turn on the circle is the case that gives the Cauchy of (d).

*Proof.* (a) is the cancellation shown. (b) Strictly increasing maps preserve ranks; the converse is monotone
interpolation between matched points. (c) A strictly increasing f satisfying f((a + b)/2) = (f(a) + f(b))/2 for all
a, b is affine, so a non-affine f fails for some pair, and X = {a, b} is the set required. (Monotonicity is needed: an
additive function built on a Hamel basis commutes with every finite mean without being affine.) The inequality is
Jensen's. (d) The distribution function is (2/π)·arctan(v/h); the integral is elementary. (e) The exchange gives
F(1/x) = 1 − F(x), so F(1) = ½ by Proposition 2(b). The path ends at all of v, so v ≥ v₀ > 0 wherever h < δ; then
P(v/h > r) ≥ f₀·v₀/r for large r, and ∫ P(v/h > r) dr diverges. ∎

The theorem is elementary; its content is the reading. The addresses are given before anything arrives, and nothing
that arrives moves them: (a) for every single reading, not on average, (b) for every statistic of their order, and (c)
says why no statistic of size can be read from them. So nothing the Cauchy says (its median, its scale, its missing
mean) is a statement about the payload, and nothing in the payload can be read from it. Finding a Cauchy is, by itself,
no evidence that anything in the world is distributed that way.

**A median in two registers.** An exact median of n readings taken one at a time needs storage that grows with n
(Munro and Paterson 1980). To a stated accuracy it needs two registers: move an estimate by the sign of each comparison
alone, `m += a_k * sign(x_k - m)` with steps a_k falling more slowly than 1/k (k^(−0.6), say), and keep a running average
of m. The average reaches the sample median's own accuracy (Robbins and Monro 1951; Polyak and Juditsky 1992); for a
Cauchy, √n times its spread tends to π/2 in the scale's unit. It reads order only, a comparison's sign, which is all
Theorem 6 says a median needs.

**What it does not claim.** It does not show that every real observer counts by the turn rather than by a clock, a flat
sensor or what arrives; it shows what the turn's count gives. Nor does it show that every Cauchy met in data has this
origin: a resonance's profile and a stable sum of index 1 are Cauchy laws that are facts about a system. The claim is
only that a reader's uniform turn lays its own addresses this way.

**The rule, and a test.** This paper's rule, offered as a test: a Cauchy variable is a direction, a ratio read in one chart, laid by a turn; never an amount.
Its median and quartiles are places on the line and mean what they say. Where a Cauchy appears beside an amount, the two
are separate factors: the amount is the payload, the Cauchy is where it lands. So for any Cauchy met in practice there is
a test: find the turn, and find the amount. A spectral line is the plainest case: spectroscopy writes it as a strength,
an amount whose values add, times a profile, the Lorentzian, which is the frequency line laid by a uniform turn of the
response's phase. The profile is read by its centre and half-width, an order statistic; the strength by its integral, a
sum.

**Once a Cauchy, always a Cauchy.** Every operation a reader can make on a direction keeps the law in the family and
moves only its one point m + iγ, the standpoint's foot and height above the line:

| what the reader does | what the law does |
|---|---|
| starts again from a new zero (a turn) | a Möbius map: Cauchy to Cauchy |
| takes the reciprocal | Cauchy to Cauchy |
| rescales its drawing, or zooms | Cauchy of another scale |
| relays through a standpoint between | the sum: Cauchy |
| averages n readings | the same Cauchy: nothing gained, nothing lost |

The closures are classical (Knight 1976; McCullagh 1996; Lévy 1925). For a programmer they say that the family is a
closed type: every operation on directions returns a value of the same type, and the whole state of a law is two
numbers. Averaging is the exception that proves the point: the mean of n independent standard Cauchy readings is a
standard Cauchy reading, so averaging buys nothing, as it should not, since it is an operation on amounts.

**What breaks it.** Only operations that are not operations on directions, each of which brings an amount in:
- squaring, X², which is not a reading of any turn;
- cutting the line at an edge, as a flat screen of finite width does;
- multiplying each reading by an amount that varies, which gives a mixture of scales;
- adding an amount to each reading, as thermal velocities add to a spectral line and give Voigt's profile;
- pooling readings from different standpoints without relaying them;
- counting the turn against something other than itself, a lopsided clock or the payload's density.

Even then the far field holds: an added amount of finite spread leaves the tails ~ γ/(πx²), so the Cauchy is lost
first near its centre and last at the horizon. Only an edge or a power takes the tails.

## 6. The array

A closed curve stored as N samples x[k], y[k], at the places θ_k = (k + ½)·2π/N, makes the same split in the form any
programmer knows. An array is a representation: whoever builds it chooses its indexing, and the world has no indices of
its own. The picture shows that addresses and payloads can be held apart; why a reader's addresses follow the uniform
turn is Proposition 5's, not the array's.

**The index is the address.** The places are fixed by the index before any value is stored, at equal steps of turn.
- Read as slopes of the inscribed angle, s_k = tan(θ_k/2), they are, for even N, exactly the N evenly spaced quantiles
  of the standard Cauchy. A finite array samples the continuous law at N quantile locations.
- For even N, half of them lie within the corner, |s_k| ≤ 1. For odd N one place falls on the horizon itself, [0 : 1],
  an address like any other, and the share within the corner is not exactly a half.

**The stored values are the payload.** Changing them moves no place, so the places' ranks, median and corner are
untouched by anything stored (Theorem 6(a)). The offset from one place to another is the tangent subtraction of their
slopes: places compose without angles.

**Where the array is not the reader.** An array index is ⌊x⌋. The floor keeps the cell and discards the fractional
part, which locates the place within the cell; its binary digits are the finer levels of the address. A reader has no
floor: it uses the continuous address and keeps as much of the finer structure as its resolution supports, rather than
discarding every finer level at once. What the floor discards, and why it matters, is the subject of §7. One thing an array can do that resembles
this is band-limited reconstruction, which spreads a value over every sample by weights that sum to one; that assumes a
model of the signal, and is an analogy, not the same mechanism.

**One array per facing.** A circle has four facings, the quadrants, and can be stored as four arrays on one lattice,
places at θ_k = (k + ½)·(π/2)/N, read as tan θ_k: the N evenly spaced quantiles of the half-Cauchy. Within an array its
middle is the corner, and reading it backwards is the reciprocal: tan θ_k · tan θ_(N−1−k) = 1. A sphere is eight
arrays, one per octant, each two-dimensional, uniform in azimuth and in height. Since the places sit at midpoints, no
array holds an end, and joined arrays never claim the same element.

**The reader reads the arrays; the writer joins them.** A reading carries no sign, so from a standpoint every facing is
the same array, and a reader reads within one. To join two arrays their values must meet at the shared end in one unit,
and that needs each array's size, its extent in amounts, which no reading fixes (§10). The writer knows the sizes, and
which facing each array is, so it can join the four into the closed circle. The reader cannot tell whether two ends
meet.

**Not knowing the size makes the corner and the horizon.** Knowing an array's size, the writer has its end at an
amount, V*; its ruler is the number line, on which the point where the two parties are equal is computed.
Not knowing it, the reader must draw the other party at its own H, and v = h becomes its split of near from far and the
median of its readings. With no size, the array's far end is no amount, only a direction, [0 : 1], where the chart v/h
runs out: the horizon. Both are the reader's because the size is missing.

**Four kinds of array.** What is known of the two breadths gives four kinds of array. A circle, both breadths known
and equal, is a constant array of known length, every entry the radius, of length H, so it needs no storing: it is the
equation h² + v² = 1. A shape with its breadths known is an ordinary array of known length, an amount at every index,
which the writer can join into a closed shape. Without the length there are two more. The values without the length
are an amount at each given index known only up to one common factor, like samples from a sensor of unknown gain: they
can be ranked and averaged, not sized. The index alone is allocated before any value arrives and has no length, its
slots the Cauchy's quantiles, its middle the corner, its last slot running to the horizon, K slots for any N, as a hash
ring's are. The writer's arrays have the length; the reader's are the index and the payload on it, without the length,
and that one number is what writing supplies.

**What the length decides.** The length is the line between the writer's arrays and the reader's, so it sorts the
operations on an array.
- *Writing needs the length.* Normalizing an index as i/N, indexing from the end, a percentile index p·N, a mean over
  the array, concatenation and a bounds check all use `length`. Comparing two elements, ranking, the median of what is
  present, the ratio of two entries and the step to the next index do not. Whether an operation touches `length` is the
  scale-the-world test of §10 applied to code.
- *An unnormalized density is the payload without its factor.* A weight vector known only up to its normalizing
  constant Z is the third kind of array, and the algorithms built for it use only ratios of entries: Metropolis's
  acceptance test compares p(x′)/p(x), so Z cancels and rescaling every weight changes no step of the chain (Metropolis
  et al. 1953; Hastings 1970). Computing Z itself, an evidence or a partition function, is the writing step, and it is
  the hard one. Ranks, ratios and medians survive the unknown factor; sums need it (§5).
- *In logarithms the unknown factor is the DC term.* A common factor k becomes an added constant ln k, so the payload
  without its size is the log-values less their mean, unchanged by k, while the mean moves by exactly ln k. The size is
  the zeroth Fourier coefficient of ln r, the shape the modes n ≥ 1, and a shape is stored most cheaply as the circle's
  one constant plus the residual.

**Static and dynamic arrays.** A static array writes its length once. A dynamic array is still a writer, but every
growth rewrites the one number, and what moves when it does is exactly what divided by it.
- *Growth moves what divides by the length.* An index counted from the start survives an append: it is a count of
  slots, one slot agreed beforehand. An index from the end moves, and so does any position normalized as i/N, a
  percentile, a scroll fraction or a progress bar; an insertion in the middle moves everything after it, the
  order-maintenance problem of §12. An index laid by turn never moves, since it never used N: K slots for any N, the far
  end at the horizon.
- *Amortized growth is the levels, its base free.* A dynamic array grows its capacity by a factor g at each
  reallocation, so the reallocations fall at levels g, g², g³, … and the total copying over N appends stays under
  gN/(g − 1): 2N at g = 2, 3N at g = 1.5, 5N at g = 1.25. Any g > 1 gives a constant cost per element, and
  implementations choose 2 or 1.5; growth by a fixed step instead copies in proportion to N per element. The logarithm
  is forced and the base is not, as for the reader's levels (§8).
- *Static is held at once, dynamic in order.* A static array has every value present, and its exact median is one
  selection away. Read as it grows, the exact median needs storage in proportion to n (§5), and to a stated accuracy
  two registers. A running mean needs the count n, an amount; a running median needs only order. So even online the
  median is the reading's and the mean the writing's.

**Laid on the sweeps, in code.** With K places on the quarter turn, the index of a direction (h, v) is its share of the
turn times K:

```js
const turnIndex = (v, h, K) => Math.min(K - 1, Math.floor(K * (2 / Math.PI) * Math.atan2(v, h)));
```

`atan2` takes the horizon, h = 0, without dividing, and the clamp keeps it in the last place. No length enters. At
K = 8 the readings 0.1, 0.5, 1, 2, 3, 10, 1000 and the horizon go to places 0, 2, 4, 5, 6, 7, 7, 7; the boundaries are
tan(kπ/16) and the places' middles the half-Cauchy's eight evenly spaced quantiles, 0.099 … 10.15. The four arrays lay
on these places.
- *The index alone.* The places are the whole array. The corner is the boundary between places 3 and 4, found with no
  length; a reading and its reciprocal go to places k and K − 1 − k; scaling v and h together moves no index.
- *The values on the index.* The central sweep meets the same point at twice the angle and indexes it by
  `Math.floor(K * phi / Math.PI)` over its half turn, the same place: one index serves both sweeps, the ratio and the
  amount found there stored together. The amounts are known up to one factor, so keep their logs less their mean.
- *A constant array.* Every place holds the radius, of length H, so the value is a function of the index and nothing is
  stored.
- *An array of known length.* `Math.floor(N * x / X)` needs the extent X: with N = 8 and X = 100 the amounts 10, 50, 99
  go to 0, 4, 7. `turnIndex(x, H, 8)` needs only H, the zoom: 4, 6, 7 at H = 10 and 1, 4, 5 at H = 50.

An interactive version of this example is at https://reportbase.github.io/wander/array-sweeps.html. It draws the K
places from home and from the centre of the circle on the chord, lights the place a chosen direction falls in by both
sweeps, and lays the four kinds of array on those places; K, the direction, the scale of the world and H can be changed,
and the page's functions (`turnIndex`, `centralIndex`, `countIndex`) are the ones above.

**Growth.** The same split shows when a world grows rather than scales. An address made by dividing a thing's place in
a list by the list's length is a ratio, a reading of the list's own contents, and it moves as soon as the list grows.
An address made of slots, a fixed number to each level whatever the level holds, does not move: the radix was agreed
beforehand, and it is a written amount carried into every address. A timestamp is the familiar case; positional
notation is stable for the same reason. Read against its own contents, a list re-addresses itself as it grows; written
against an agreed radix, it never does, and the price is the slots held empty.

## 7. What Math.floor throws away

Every programmer has written it:

```
const i = Math.floor(x / w);   // which cell
const f = x / w - i;           // where in the cell, in [0, 1)
```

and then kept `i` and dropped `f`. The cell's value is read from `a[i]`, and `f` is gone. It looks like rounding: a
small leftover, the part of x that did not fit the grid. This section is about why it is not, and why the act of
dropping it is one of the most consequential things in the whole construction.

### 7.1 The remainder is address, not data

Start with what is not lost. The value stored in the cell is untouched: `a[i]` is exactly what it was. Nothing of the
payload goes. What goes is where in the cell the place was, and that is address. So the floor is not a lossy operation
on data at all. It is a lossy operation on the index. So the claim is not that the floor is lossless, nor that flooring
is wrong: where only the cell's value is wanted, dropping where in the cell is exactly right; where the place within
the cell matters, what was dropped was address, not data.

Write the remainder in binary, f = 0.b₁b₂b₃… Each digit answers one question: b₁ which half of the cell, b₂ which half
of that half, b₃ which half of that, without end. So the digits of f are the finer levels of the address, one level a
digit. Appending a digit to the key and dropping it from the remainder is moving one level down:
`Math.floor(2 * x / w)` is the key one level finer, and its low bit is b₁. Every level of detail is a floor taken at a
different depth.

So `Math.floor` does not round one number. It takes an address that runs through every level at once and keeps it at
exactly one, discarding every finer level in a single step. A double holds 53 significant bits; every one of them below
the cell's own is one of these levels, and the floor keeps none.

### 7.2 The remainder is a second dimension

The levels in the remainder are not a list to be stored beside the index; they are the index's other coordinate. Give
the cell of level j and index k, [kw, (k + 1)w) with w = 2^(−j), the point

  z = m + iγ,  m = (k + ½)·w its middle,  γ = w/2 its half-width,

in the upper half-plane. A place is then two numbers: where it is along the line, m, and how far down it is held, γ. In
these terms the floor keeps m at one fixed height and forgets that the height was a coordinate at all. The plane the two
numbers make has a geometry of its own, and it is a classical one, the hyperbolic plane, with metric
ds² = (dx² + dy²)/y².
- **Every level is the next.** z ↦ 2z is an isometry of that plane, and it carries each level of cells onto the next.
  Each binary digit is one step down, and every step is the same: ln 2 in height. There is no privileged level; level
  50 is as good a place to stand as level 0. On the line alone the step is the doubling map x ↦ 2x mod 1, which moves
  the first digit of the remainder into the index: `floor(2*x)` is that digit and `2*x - floor(2*x)` the rest. Its
  Lyapunov exponent, the rate at which it forgets where it started, is ln 2: one level a step (the Bernoulli shift).
- **Every cell has the same room.** The tile [kw, (k + 1)w] × [w/2, w] has hyperbolic area
  ∫∫ dx·dy/y² = w·(2/w − 1/w) = 1, at every level. A cell fifty levels down, 2⁻⁵⁰ wide on the line, has exactly the room
  of the first. The tiles are Böröczky's binary tiling (Böröczky 1974).
- **Distances are fixed by the levels.** With cosh d = 1 + |z₁ − z₂|²/(2γ₁γ₂): a parent and either child are
  arcosh(3/2) ≈ 0.962 apart, two siblings arcosh 3 ≈ 1.763, two cells n apart on one level arcosh(1 + 2n²), the same at
  every level and every place.
- **A point of the plane is a Cauchy law.** Each z = m + iγ is the Cauchy C(m, γ), the law of §5 with its foot and
  height, and from its cell's point the Cauchy puts exactly half its weight in the cell:
  (1/π)(arctan 1 − arctan(−1)) = ½. The cell is that law's interquartile range.

So the plane the floor's remainder lives in is the space of the address law's own parameters. A dyadic cell is not just
like a Cauchy: it is one, read from its own point. The array's grid and the reader's law live in the same plane.

### 7.3 A tree keeps the levels and loses the plane

The usual way to keep the finer levels is a tree: a quadtree, an image pyramid, a mipmap chain, each cell linked to its
parent and its children. A tree keeps the depth. It measures it wrongly.

Take the two cells either side of the middle of level j, k = 2^(j−1) − 1 and k = 2^(j−1). They touch. In the plane they
are arcosh 3 apart, at every level. In the tree their nearest common ancestor is the root, so they are 2j steps apart:
60 at level 30, for two cells side by side. A neighbour search in a quadtree that climbs to the root is meeting this.

Add the sideways links, each cell joined to the cells beside it on its own level, and the graph measures the plane.
Counting g steps (up, down or across), over all 523,776 pairs of cells at level 10, |d − g·ln 2| never exceeds 2.19; the
shortest way between two cells is always up, across and down, in closed form min over s of 2s + |⌊k₂/2^s⌋ − ⌊k₁/2^s⌋|;
and d/g tends to ln 2. An array indexed by (level, index), with links across as well as up and down, is a discrete copy
of the half-plane. A tree is not.

This is the precise sense of "another dimension". A two-dimensional array `cells[level][index]`, read with its
neighbours, is not a stack of separate resolutions; it is the address plane itself, sampled.

### 7.4 Two ways to lose depth

Every reader with finite resolution loses the finer levels somewhere. The floor and a reader at a height lose them in
different ways, and the difference is exact.
- **The floor.** Averaging over a cell of width w multiplies a wave e^{ikx} by |sin(kw/2)/(kw/2)|. It keeps every level
  coarser than the cell whole and none finer: a cut at one level, with zeros and side lobes past it, so that finer
  detail, once each cell is kept as one value, can come back as coarser (aliasing).
- **A reader at height γ.** The Cauchy from z multiplies the same wave by e^{−kγ}: smooth, never zero, and composing as
  heights add (reading from γ₁ and then from γ₂ is reading from γ₁ + γ₂, a semigroup).

No γ brings the two within 0.22 of each other, so keeping binary digits is not the same as reading from a height. For a
step detail (the Haar wavelet), a reader standing at its own cell's point keeps these shares of each level, by the level
read against its own (negative is coarser):

| level read, against the reader's own | −7 | −6 | −5 | −4 | −3 | −2 | −1 | 0 | +1 | +2 |
|---|---|---|---|---|---|---|---|---|---|---|
| reader at a height: share of the step kept | 0.927 | 0.874 | 0.789 | 0.660 | 0.482 | 0.279 | 0.110 | 0.027 | 0.0044 | 0.0006 |
| the floor at the same level | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |

The reader keeps half of the step 3.09 levels coarser than its own cell and takes 5.5 levels to go from 90% kept to 10%.
The share depends only on u = γ/w′, the reader's height in the detail's own width, so it is one soft cut over the
levels, the same at every depth. The floor's row is a wall.

What the reader keeps also depends on the detail, which is the payload's: near the reader a step loses
(12/π)·u·ln(1/u) and a smooth detail an amount in proportion to u, and far off the detail's vanishing moments set how
fast it falls (u⁻³ for one, u⁻⁵ for two). The window itself does not: from height γ the address window is 2γ wide, the
cell, before anything arrives.

### 7.5 Who sets the depth

The floor sets one depth for everything: the cell's, chosen by the store, before anything is read, the same for a
mountain and a grain of sand. The geometry sets each thing's level by its span (§9): a thing that spans n addresses is
held to about log₂ n levels, and a thing between two addresses is held at the coarser one, not rounded to either. So
the floor imposes a level of detail; the reader reads one off what it meets.

There is a second difference, which the scale-the-world test of §10 finds at once. Where the floor is taken of an
amount, `Math.floor(x / w)`, the cell width w is an amount too, and multiplying every amount in the world by k moves the
key unless w is multiplied with it. By the test, the key is then a writing: its grain had to be carried in. A floor
taken of a share of the turn, `Math.floor(θ / Δθ)` with Δθ a fraction of the quarter turn, carries no amount, and no
scaling moves its key.

### 7.6 Why this matters

Three things follow, each from the pieces above.
- **The address is continuous and hierarchical at once.** Level of detail is not a structure kept beside the address,
  a pyramid built, stored and kept in sync; it is the address's second coordinate, the height, and it comes with the
  address for free. The engineered hierarchies (pyramids, mipmaps, quadtrees, tile keys that gain a digit a level) can
  each be read as a way of keeping some of that coordinate after the floor has dropped it.
- **The hierarchy is a geometry, not a convenience.** It is the hyperbolic plane: every level alike, every cell of one
  room, distances fixed by the levels. That is why "zoom in one level" is the same operation everywhere, and why a
  structure that links only up and down gets its distances wrong. And that plane is the one the Cauchy's parameters live
  in, so the reader's law and the store's hierarchy share a plane and differ only as filters on it.
- **The separation of address and payload reaches into the depth.** The floor discards address, never payload. From a
  height, the window 2γ is the address's, fixed before anything arrives; what survives inside it, and whether two things
  in it read as two, is the payload's. The split of §5 holds at every level.

**What is not shown.** That the world stores anything this way; that a reader's level of detail is a dyadic depth rather
than a continuous height; anything about physics. The mathematics is classical (Böröczky's tiling, the Poisson kernel,
the sinc of a box); the reading is the paper's.

## 8. Two address spaces

Inside the corner the reader holds its unit and can lay readings in proportion. Past it the reciprocal makes the
reading h/v ∈ [0, 1], but does not say how it should be laid out. Let a lay place a far reading x = v/h ≥ 1 at
position L(x), counting addresses from home, with L increasing and L(1) = 1.

A different H multiplies every far reading, taken as an amount, by one common factor, and a reader with unit λH in a
world scaled by λ receives the same readings (Proposition 3(b)). A lay whose room depended on where a reading sits would
build in a scale the reader cannot have. So we require:

> **(S)** L(λx) − L(x) depends on λ alone, for all x, λ ≥ 1.

**Proposition 4.** If L is increasing and satisfies (S), then L(x) = 1 + k·ln x for some k > 0: every doubling receives
the same number of addresses, k·ln 2. If the far lay also joins the near lay L(x) = x without a kink at the corner,
k = 1.

*Proof.* With f(λ) = L(λ) − 1, (S) gives f(λμ) = f(λ) + f(μ) for λ, μ ≥ 1: Cauchy's functional equation in
multiplicative form, whose only increasing solutions are k·ln λ. At x = 1 the near lay has slope 1 and the far lay
slope k. ∎

(S) does the work, and it is assumed, not derived: scale invariance of the lay's increments, motivated by the fact that
no reading can fix a scale. Monotonicity, a fixed corner and a matched slope are not enough by themselves:
1 + ln x + α(ln x)² satisfies all three. Proportion past the corner, L(x) = x, gives the stretch from x to λx room
(λ − 1)·x, which grows with x; a power does the same; only the logarithm gives room that depends on λ alone.

**Floating point.** Floating-point numbers lay their addresses this way. The exponent counts levels and the significand
is a plain share within the level; below the smallest normal number the subnormals lay one stretch in proportion from
zero. The count of levels plus the share within the current one is the logarithm laid straight between level edges,
exact at every edge and never more than 0.086 of a level from the smooth logarithm. A float differs in having levels on
both sides of 1 and a floor; the situated reader has proportion inside the corner and no floor.

**Reality in 2H.** Measured by length rather than count, the far field fits in one more H. The *in-place lay* puts a
far reading at 2 − h/v from home. Level j past the corner, where v/h runs from 2^(j−1) to 2^j, has length 2^(−j), so
the whole far field out to the horizon lies between radius 1 and radius 2. Its room per unit of v/h is (h/v)², the
Jacobian of the reciprocal. It holds the same addresses as the logarithmic lay, the same number per doubling, crowded
toward radius 2; a reader with finitely many addresses runs out of them at the end of its own range.

| drawing of the same addresses | measured by | bounded | corner at |
|---|---|---|---|
| fisheye | steps of turn | yes, a quarter turn | half the turn |
| in-place lay | length | yes, radius 2 | radius 1 of 2 |
| logarithmic lay | number of addresses | no | 1, where the equal doublings start |

**Why not proportion all the way out.** A reader that kept v/h in proportion past the corner would suffer five ways,
each familiar in numerical work:
- it could not lay its range, since its readings run to infinity and no range fixed in advance holds them (overflow);
- it would divide by the smaller part: past the corner h is the smaller unit relation, and a small wobble in it swings
  the reading without bound; inverting divides by the larger, the rule numerical computing follows when it pivots;
- its averages would never settle, dominated by the tail;
- it would have to crop, as rectilinear cameras do at about the corner, while a fisheye lens keeps the whole hemisphere
  by giving up proportion near its edge;
- its expansions about zero would fail past the corner.

**The corner, the end of the range, the horizon.** A situated reader meets three boundaries. The corner, v = h, lies
between the two sides of its reading; every reader finds it. The *end of its range* is where its count of addresses runs
out, well short of h = 0; a reader can reach it, as a floating-point number overflows when its exponent runs out. The
*horizon* is the reading's own infinity, h = 0, which no reader reaches.

**Why halving.** If a level has nothing but its two ends, their order and the reciprocal (P2), the only subdivision its
symmetries preserve is the cut at the corner into two halves: any other interior point can be moved anywhere within its
half by an order-preserving map that commutes with the reciprocal. Applied again to each half, this gives repeated
halvings: binary subdivision. Three parts, or any other number, need an added measure. A reader whose resolution steps
by r matches levels that are powers of r, but every ratio other than the halving costs a measure carried in the reader.
A layout whose levels are uneven, as a calendar's are (years, months of about 30 days, hours, minutes, seconds), matches
no single factor and costs a table of its levels. Uniformity can be free; variation has to be stored somewhere.

**One figure, three rulers.** The circle, the number line and Mercator's height lay one reading x three ways:
x = tan θ = sinh ζ, θ = gd ζ. The writer's number line x has no corner, only a point. The turn θ = arctan x gives 45°
to each side and makes the corner its median. The hyperbolic angle ζ = asinh x, Mercator's height, is nearly in
proportion inside the corner and about ln 2 a doubling past it: the logarithmic lay made smooth, never more than
1 − ln 2 ≈ 0.307 from (x, then 1 + ln x). All three carry the corner as a point; only the turn makes it the median,
because only its range is fixed by the geometry. A measure uniform in x or in ζ needs a range given beforehand, an
amount, and that range decides where the middle falls.

Only the turn has a focus. Its room per unit of ln x is ½·sech(ln x), most at the corner and falling alike on both
sides; ζ gives every far level the same room, about ln 2 a doubling, and favours none; x gives each level more than the
last. So Mercator's map, a chart of the whole globe, lays the far field in levels all alike and has no focus: where its
reader looks is the reader's. A picture seen from a standpoint is the turn instead, its far field in proportion in h/v
(each doubling half the room of the last), centred on whatever the corner is turned to. The levels belong to distance
counted by a fixed number of addresses, where no level is known beforehand to matter more. The map represents the field;
the reader observes from somewhere within it.

## 9. Level of detail, and H as a zoom

**The count is the level of detail.** The forms of the two address spaces are fixed; their counts are not. Laying the
near field in proportion means dividing H into some number of parts, and the geometry neither knows nor uses that
number; past the corner, what is fixed is that each doubling gets the same count, not what it is. A thing that spans n
of the reader's addresses is resolved to about log₂ n levels, one fewer each time its span halves, and a point when it
spans one. Nothing is requested: the span sets the level.

**A resolution, not cells.** The count is a resolution; it does not make cells. A thing between two addresses is not
rounded to either; it is held at the coarser level. The level is a continuous number, and its fraction says how far the
finest detail held has faded. Seen from height γ, a pattern's mode of frequency k is kept as e^{−kγ} (the Poisson
kernel), each mode fading, faster the finer it is, none cut off. Rounding to cells is a device of storage, not of
reading.

**What the height fixes.** From a cell's point m + iγ (§7.2) the height fixes an address window, 2γ wide, before
anything arrives, and no payload enters it; only the line changes it (on a closed line of length 1 the window is
(2/π)·arctan(tanh πγ)). What survives inside the window is the payload's: how much of a detail is kept (§7.4), and
whether two payloads read as two, which depends on the kernel and the payloads (two equal Cauchy profiles of height γ
part only when more than 2γ/√3 apart, two equal Gaussians of width σ only when more than 2σ; cusped profiles part at
any separation).

**H is a zoom, not an escape.** H is the value the reader chooses to start from, and nothing in the geometry fixes it.
Any H gives the same circle and corner, so a reader could choose a very large H and hold everything in the near field,
in proportion, with no logarithm. The cost is the level of detail: with finitely many addresses spread over a very large
H, everything at the reader's own scale falls within the first address. A small H holds the small in proportion and the
large logarithmically; a large H holds the large and loses the small. The best choice puts H at the scale of the thing
read, at the corner. The same idea appears in the hyperbolic browser, which draws only nodes at least a pixel across
(Lamping, Rao and Pirolli 1995), in mipmaps, which halve an image at each level (Williams 1983), and in web-map tiles,
whose key gains one digit per level of detail.

**What a larger H gives and takes.** With n addresses across the near field, an object covering the amounts d to d + Δ
spans nΔ/H addresses inside the corner: one level fewer for each doubling of H. Past the corner the two lays part. On
the logarithmic lay it spans n·ln(1 + Δ/d), whatever H is. On the in-place lay it spans nΔH/(d(d + Δ)), which grows
with H, and is largest when H = √(d(d + Δ)), the corner of the object's own two ends. Two amounts in a ratio r, placed
at arctan(x/H), are furthest apart, at arcsin((r − 1)/(r + 1)), when H is their geometric mean.

**A fixed count, aimed by H.** Call the reader's whole count of addresses K: its fixed capacity, the same whatever it
looks at. K comes before H; choosing H does not change K, it splits it. Lay the K addresses of the uniform turn of the
reader's one length along distance. Their boundaries fall at

  d_k = H·tan(kπ/2K),  k = 1, …, K − 1,

the quantiles of the Cauchy with its scale at H.
- Since tan(π/4) = 1, the middle boundary is d = H whatever H is: half the addresses inside the corner and half past it,
  at every H. H moves the split; it never changes the count.
- A small H gives the near half a short stretch, each address fine, the first about πH/2K wide; a large H gives the same
  half a long stretch and carries the far half farther out.
- The world's own count enters nowhere. Doubling or thinning what arrives moves no address (Theorem 6(a)), so a world of
  N things, of 2N, or of infinitely many is held at the same K addresses, each holding its share.

For a programmer this is the useful part. The addresses are a closed-form function of k, H and K: no table is built,
nothing is precomputed for N, and nothing is rebuilt when N changes. The last address runs to the horizon, so a finite K
covers an unbounded world, and whatever lies past every other address lands in that tail. N enters only as the share
each address holds, which is payload. The reader interacts with K; the writer, which states every distance in amounts,
interacts with N, placing each thing at its amount on its number line.

**One K in direction and in distance.** In direction, the K addresses are the turn's equal angles, split K/2 and K/2 at
the corner, and the value of H appears in none of them. In distance the same K quantiles fall at H·tan(kπ/2K), and
there H is the zoom (distance itself has to be had from a second standpoint or an amount carried in, §10). On the
in-place lay the far boundaries are the near ones reflected about H, so the K addresses fill a ruler 2H long. A
direction's K addresses and a distance's K together make a polar grid of K × K cells; every thing falls in exactly one,
whatever N.

**The corner follows the focus.** H is the reader's choice, and on the turn's addresses a cell's width relative to its
distance is (π/2K)(s + 1/s), least at s = 1: the finest relative grain is at the corner, so the corner goes on what is
looked at: the corner is the addresses' median, their finest relative grain and the reciprocal's fixed point, the
roles a focus wants. It is also where the expected travel to the next look is least, on any ruler, whenever the
next look is as likely on either side (the median minimizes E|X − c|; a lopsided expectation moves the best focus to its
own median). Near and far are then nearer and farther than the focus, held alike, since the next look may fall on either
side; their job is to show where to look next. Turning carries the corner in direction, designating the focus puts it
at the corner of distance, and how far the focus really is (a day's walk or a month's) is its size against H, carried
in. The fields are cheap: with cells no wider than δ across a focus of extent F and cells within a factor ρ past it,
the fewest addresses are ⌈F/δ⌉ + ⌈log_ρ(X/F)⌉, proportion on the focus and levels past its edge (six for the field at
X/F = 64, ρ = 2, whatever K is); the reader's lay is the case where the field's first cell matches the focus's grain.

**Other ways to squeeze the line.** Other paths from all of h to all of v, each swept uniformly along its own length,
also squeeze the line into K addresses:

| path, swept uniformly | law of s = v/h | where the last of K addresses begins | swept again from a new zero (30°) | two readings added |
|---|---|---|---|---|
| the circle (a turn) | 1/(π(1 + s²)), the Cauchy | cot(π/2K)·H ≈ 0.64·K·H | the same law | a Cauchy, scale 2 |
| the line, \|h\| + \|v\| = 1 | ½·(1 + \|s\|)⁻² | (K − 1)·H | 0.044 from its own family | 0.022 from it |
| the square's edges | ¼ up to \|s\| = 1, then 1/(4s²) | (K/2)·H | 0.047 from it | 0.062 from it |

All three are reciprocal-symmetric, so H is their median, and all three have a tail c/s that sends the unbounded rest of
the line to the horizon, so all three keep K apart from N. They part when used again: only the turn's squeeze can be
re-aimed or recombined without leaving its family. (The distances are the least, over location and scale, of the
largest gap between distribution functions and between characteristic functions.)

**More points, fewer told apart.** Seen side-on, N points spaced uniformly round a circle are read across the view to a
resolution ε. Neighbours at angle θ from the middle of the view are about (2π/N)·cos θ apart, so the reader separates
R(N) = (N/π)·arccos(εN/2π) of them. This peaks at about 1.12/ε points and falls to none at N = 2π/ε: past the peak,
more points mean fewer told apart. The addresses never overflow; the resolution does.

**From far off, a thing is its total at its centroid.** Payloads w_i at distances q_i from a centre, read from distance
r with every q_i < r, expand in the reading q_i/r through the Legendre series. About their centroid the first-order
terms cancel: from far off the payloads read as their total at their centroid, each finer order arriving smaller by one
more power of the reading. On the sphere r = q every term is the same size and none may be dropped, the corner of the
pair (q, r); inversion in that sphere exchanges the outer and inner series term by term. This is level of detail by
distance, with the corner as its seam.

## 10. What a blueprint adds

**Ratios suffice.** Everything a reader does from where it stands is done in ratios: every reading is a ratio with no
unit in it (Proposition 8 below), the index and its law are given before any value arrives (§5), near and far are laid
by count (§8), order statistics survive every change of value (§5), more standpoints bring back the figure up to its
size, one step taken places everything in the reader's own H, and two readers that see one thing in common are aligned
by it (Proposition 7 below). A system that builds, places, compares, orders and checks from where it stands needs
nothing more.

**What a blueprint adds.** A blueprint is the writer's statement in amounts: every length at once, to one scale, from no
standpoint. It gives seven things the ratios do not: (1) the size, V*/H, which no reading carries; (2) meeting out of view,
parts made apart that fit only through a unit agreed beforehand, where parts seen together need only a ratio read between
them; (3) sums of amounts, totals, means and budgets, where the readings have a median and no mean (§5); (4) the join,
every facing and both signs held at once; (5) a statement before the thing exists, to be built to, where a reader reads
what arrives; (6) completeness stated, where a reader can recover a thing exactly and not know that it has all of it; (7) a far field
kept in proportion, the number line's, with no corner, so two readers whose corners (their H) differ need not agree where
either near field ends.
None is needed to build, place, compare, order or check from a standpoint; each becomes needed when parts made apart must
meet, when amounts must be added, or when the whole must be stated in advance, the needs of an intricate system of many
parts. In a program's terms: an index and its order statistics run on ratios; a schema with units, a sum or an interface
between separately built components needs the amount.

**Proposition 8 (scale cannot be read).** Let a reader's observations be any collection of readings, each a ratio of
two amounts in the scene. Then (a) multiplying every amount by one factor λ > 0 leaves every observation unchanged, so no
collection of observations, from any number of standpoints, fixes the scale; (b) if one amount L₀ is supplied from
outside, every amount the readings link to L₀ is fixed.

*Proof.* (a) (λa)/(λb) = a/b. (b) A chain of readings linking a to L₀ multiplies to a/L₀, and λ = 1 is the only factor
leaving L₀ fixed. ∎

**Proposition 7 (a shared fact buys one factor).** Two readers share one closed polygon, each recording its part as
exact directions and lengths counted in its own unit, H_A and H_B, neither knowing the other's. If S_A and S_B are the
vector sums of each part and neither part closes alone, then H_B/H_A = |S_A|/|S_B|, and nothing more about the units can
be recovered. (Closure gives H_A·S_A + H_B·S_B = 0; scaling both units together changes no count.)

**The test: scale the world.** Whether a record is read or written can be checked without asking how it was made.
Multiply every size and distance in the world by one factor k. A reading does not change: a direction, an angle, a
photograph, [h : v]. A writing changes by k: a dimension on a floor plan, the length a map's scale bar states. What
scaling leaves unchanged is geometry; what it moves, in a named unit, is an amount that had to be carried in. A record
that scaling would not change cannot contain the world's size, however carefully it was made. For a programmer this is a
property test: run the system on the world and on the world scaled by k, and see which outputs move.

**What standpoints add.** From one standpoint a reader has the frame, every direction at no particular size. A second
standpoint, the step between the two a baseline in the reader's own H, brings back the figure in H wherever the parallax
stays above the reader's resolution; past that distance a point is only a ray. One amount carried in, the length of the
step in an agreed unit, writes it all in that unit. Each step adds what the one before could not: the frame from one
standpoint, the size in H from two, the unit from one amount more.

**Distance cues in the payload.** What arrives can carry cues to distance: an echo's delay, or how faint a thing of a
known kind looks. Each turns into a distance only with an amount carried in, the signal's speed and a clock, or how
bright or large such a thing truly is. Scaling the world by k moves the distance so stated, so by the test above it is a
writing, not a reading. The picture of §1.3, where a colour says nothing of how far off its pane is, is the reading
alone: an address, and a payload with no amount carried in beside it.

**The best estimate is the median.** If the reader must guess the other's true size, and knows only V₋ ≤ V* ≤ V₊, the
guess whose worst error in levels is least is √(V₋V₊), the corner of the bounds; holding a distribution, the guess of
least expected error is its median, the same for every increasing measure of error; knowing nothing either way, it is
H itself. The mean, best under squared error in amounts, changes with the measure and need not exist.

## 11. A dial: scrolling without end

Every scrolling interface meets the same wall. A scrollbar maps the list's length onto the screen's height, so a list
of a billion rows leaves each pixel of the bar a million rows wide. A flick scrolls at a speed, so the far end of a long
list takes as long to reach as the list is long. And the code keeps a scroll offset that grows with the list. The
geometry of §8 and §9 gives a control with none of these: the whole list on a bounded screen, any place reached in
time that grows with the logarithm of its distance, and no count kept anywhere in the control.

### 11.1 Three rulers, run as a control

§8's figure lays one reading x three ways: as itself (the number line), as the turn θ = arctan x, and as the hyperbolic
angle ζ = asinh x, with

  x = tan θ = sinh ζ,  θ = gd(ζ).

A dial runs the three as one control:
- **The push is ζ.** A held thumb adds to ζ at a steady rate r. Pushes add in ζ, as rapidities do in special
  relativity, where ζ has that name.
- **The place is x.** The hand is at record x = sinh ζ, in units of the window.
- **The screen is θ.** The hand is drawn at the turn θ = gd(ζ), which never leaves the quarter turn however far it has
  gone. The corner, one unit from home, is at 45°; the rungs at x = 2^k fall in levels past it (§8's two address
  spaces).

```
// one frame of a held push
zeta += rate * dt;                    // the push adds, unbounded
const x = Math.sinh(zeta);            // the place: records from home, in window units
const theta = Math.atan(x);           // the screen: always inside the quarter turn
```

### 11.2 Any place, in time logarithmic in its distance

Held at a steady rate, the hand is at x after

  t(x) = asinh(x)/r,

so near home it moves in proportion (x ≈ rt) and far off each doubling costs the same time, ln 2/r. Any place up to N
is reached in about ln(2N)/r. A list of 2⁵³ records, the largest a double counts exactly, is crossed in 37.4/r: at a
rate of 2 a second, under twenty seconds of holding, against 2⁵³ rows at any fixed scrolling speed. Nothing about the
list's length was set in advance; the same push crosses a thousand records in 7.6/r and a googol in 231/r.

### 11.3 The whole list on the screen

The screen shows θ, a quarter turn, whatever the list's length. Inside the corner, within one window of the hand,
records are laid in proportion, each its own row; past it, they are laid in levels, the rungs at 2, 4, 8 … windows
crowding toward the edge. The far end of the list is the horizon, θ = 90°, at the edge of the screen and never drawn,
as a road's end is its vanishing point. So the screen holds K addresses (§9) whether the list has a thousand records or
no end, and a scrollbar's question, how long is the list, is never asked. The list's length is N; the control
interacts with K.

### 11.4 Letting go: a new zero

When the thumb lets go, the place reached becomes home: ζ returns to 0, and the rungs are drawn again about the new
place (§2.4's new zero). Pushes compose by adding in ζ, and a release folds the sum into the place, so the control
holds no growing number: the only number that grows is the record's own index, which the list needs anyway. The
window, how many records one rung holds, is a zoom, as H is (§9): it changes how much of the list the corner holds in
proportion and moves no record's place in the list.

### 11.5 Content made from the address

Because the addresses do not depend on N, what is shown at a place can be made from the place itself, a function of
the index, and nothing need be stored. A dial can walk a road of quadrillions of records whose country is made from each
record's index, or browse 2⁵³ − 1 items in two dimensions made the same way, with cells opened largest-on-screen first
and every drawn total adding exactly to the whole. The payload is
a function on the addresses (§2.3), and here the function is the program.

### 11.6 In two dimensions

The same control works over two sweeps. The thumb points in a direction from the centre, adds to
a two-dimensional push at a rate set by how far it is tilted, and the hand sits at sinh of the push inside the
triangle of §2.2's sum cut, nearing its edge and never reaching it. The two coordinates there are log-ratios, which add,
so pushes in two directions commute. A dial built from true two-dimensional boosts does not: pushed round a loop and
brought back to rest, its frame comes home turned by the area the loop enclosed, as special relativity's frames do
(Thomas precession; Thomas 1926). For a list in two dimensions that turn is a design choice, to show as the record of the path or to
cancel.

### 11.7 What is the design's and what is the geometry's

The place, the corner, the levels past it and the horizon are the geometry's: the three rulers and their one figure.
The design adds two numbers, the rate and the window. Zooming interfaces have arrived at relatives of this: speed
coupled to zoom, so that scrolling fast zooms out (Igarashi and Hinckley 2000); views as points of position and scale
(Furnas and Bederson 1995); and smooth zoom-and-pan paths written in the hyperbolic functions (van Wijk and Nuij 2003).
What the geometry adds is where those choices come from, and a control whose reach is the logarithm of the list
because its push is the hyperbolic angle.

## 12. What the geometry gives free

Once the reader chooses H, its one length, some structures follow with no further choice:
- a zoom, the value of H (§9);
- a split between near and far, the corner v = h (§3);
- readings no change of the world's size can move (Theorem 6(a), §10);
- given that the directions are uniform, addresses for any number of things with no table and no count (§9).

Others need one stated premise more:
- precision far off, the lay past the corner, 1 + ln s or 2 − 1/s, given (S) (§8);
- a level of detail, given a fixed count K of addresses, which H then divides between the near field and the far (§9).

What hides what is not among them; it is the payload's, set by which surfaces are opaque. Some systems built to read
or draw a world arrive at these structures by design, and the geometry lets each design be read against them.

- **The depth buffer.** A perspective depth buffer stores (f/(f − n))·(1 − n/d) for a point at distance d between the
  near and far planes n and f. With H = n this is the in-place lay, 2 − n/d, less its constant 1, rescaled: setting the
  near plane is choosing H, the near field inside it is discarded, and precision runs out far off because every address
  there has already been spent toward the horizon. Logarithmic depth in its plain form, ln(d/n)/ln(f/n), is the
  reader's lay past the corner with its corner at the near plane; the form ln(Cd + 1)/ln(Cf + 1), proportional below
  d ≈ 1/C and logarithmic above, is a smooth form of the whole lay, turning at d ≈ 1/C.
- **The flat screen.** Equal pixels on a plane are not equal turns. Per unit of screen area the uniform turn's
  directions have density (2/π)·cos³α, so equal pixels over-weight the directions off the axis by sec³α, and along one
  line of a screen of finite edge they put the median at half the edge instead of at the corner. The weighting is the
  design's, added to the geometry. Laid by turn instead, an arctangent on each coordinate of a cube's face (the
  equi-angular cubemap), the cells' solid angles vary by a factor of √2 across a face, against 3√3 ≈ 5.2 for equal pixels.
- **A filter's steady state.** A Kalman filter tracking a random walk (process noise q, measurement noise r) settles
  with predicted and updated variances √(qr)·μ and √(qr)/μ, μ = (n + √(n² + 4))/2, n = √(q/r) (Kalman 1960): a
  reciprocal pair about √(qr), their product qr at every n; for matrices P⁻ # P = Q # R, # the matrix geometric mean.
  The noises are the design's; the corner the two variances meet about is the geometric mean's.
- **Exact composition.** Readings composed by tangent addition can be held exactly as Gaussian integers, the step v/h
  as h + iv, reduced after each product by the gcd of its parts. The register grows by ½·log₂ of the odd part of
  h² + v² bits a step, and not at all only at home, the corner and the horizon: every other step costs storage without
  end, the arithmetic face of the steps that never close (§2.4).
- **A step that never closes.** Fibonacci hashing multiplies by ⌊2³²/φ⌋ = 2,654,435,769, a golden fraction of the turn
  (Knuth 1998, §6.4): a step that never closes, whose multiples spread round the turn leaving at most three sizes of gap
  at every count (the three-distance theorem; Sós 1958).
- **Addresses on a turn, not by a count.** Consistent hashing puts keys and machines on a circle by angle, each key
  served by the next machine round (Karger et al. 1997): adding a machine moves about one key in n + 1, where
  `hash(key) % n` moves nearly all of them. Order-maintenance labels drawn from a fixed count M are the other side: one
  gap takes about log₂ M insertions before labels must be reassigned (Itai, Konheim and Rodeh 1981; Dietz 1982). A count
  of addresses fixed beforehand runs out where the world's count grows; the turn's addresses do not, and pay with a
  horizon (§9).
- **One stream is not an address.** A direction is two numbers, [h : v]. A single stream of amounts can be given a
  partner by the Hilbert transform (Gabor's analytic signal; Gabor 1946), but the partner is the stream's own quadrature
  only when its envelope's spectrum lies below the carrier (Bedrosian 1963): a premise about the payload, added.
- **Relative steps on a lattice.** If every reading is rounded to whole levels and each step is coded against the last
  rounded value, the held value is round(x) at every step, since round(x − n) + n = round(x) for whole n: the steps
  telescope, and no error builds up whatever the route (DPCM with its predictor in the rounded domain). A k-tap
  extrapolating predictor codes the k-th backward difference instead, and one isolated step then costs 2^(k−1) units.
- **A spectral grid on the whole line.** Boyd's rational Chebyshev collocation points, L·cot((2j − 1)π/2N), are the
  midpoints of N equal shares of the Cauchy of scale L: the reader's addresses with L = H, and Boyd's rule for L, the
  scale of the feature to be resolved, is the best H at the corner of what is read (Boyd 1982, 1987). The same equal
  angles read by their cosine are Chebyshev's nodes, crowded at the ends of the chord; by their tangent, spread to the
  horizon.
- **Tables fixed in advance.** A sampling table or grid of cells fixed in advance must know the extent it covers and the
  resolution it needs, and is rebuilt when either changes. The uniform turn's addresses need neither (§9); what needs
  them is the payload or the writer.
- **The centre of directions.** Where readings fall as the uniform turn's law, their tangent chart has no mean and the
  median is the law's own centre (Theorem 6); a fit that averages them on that chart has nothing to settle on.
  Measurement errors are another law, which the geometry does not fix.
- **A dial over a list without end.** The place, the corner and the horizon are the geometry's; the rate and the window
  are the design's (§11).

This is a claim about where these structures come from, not about how well any system performs: a design that departs
from the geometry may be right to, for reasons the geometry does not see. What comes free is the readings, not the
amounts: metres still cost one amount carried in (§10). Whether a given departure is worth its cost is the designer's
question; the geometry only makes it one that can be asked.

## 13. Assumptions and related work

**What depends on what.** The results do not all rest on the same premise.

| result | the condition it needs |
|---|---|
| each reading a direction, unmoved by scaling the world; the address law independent of the payload; ranks and medians commute with every increasing map; K addresses hold any N | the addresses fixed before anything arrives; any weighting |
| the median at the corner, K/2 addresses on each side of H | the weight unchanged by the reciprocal |
| no mean; a tail c/s, so the last of K addresses begins near c·K·H | a density of h bounded away from zero near the horizon |
| every pair's median at its own corner (three or more parties) | each pair's weight unchanged by its own reciprocal |
| the exact Cauchy, its 2/π and quartiles √2 ∓ 1; on the octant the near field exactly ⅓ | the uniform turn, or uniform area on the sphere |
| staying a Cauchy under re-aiming and under sums | the readings Cauchy to begin with; for sums, independence |

The first row is the main result in its widest form: the split of address from payload, and of K from N, holds for any
reader whose addresses are laid before anything arrives. The Cauchy is that split under the uniform turn.

**Premises named.** The logarithm past the corner rests on (S), assumed, not derived; real readers have preferred
scales, their own resolution among them, and here a preferred scale sets where the lay stops, not its form. The
Cauchy's exact shape rests on the uniform turn, which is selected by treating every attitude alike, a stated ignorance
(below), not forced. The reader's circle is its one length turned, a rigid bar's linear periodic turn; that every reader
uses this construction is not claimed, and whether real eyes, brains or instruments sweep by such a turn, with nothing
imposing a c, is an empirical question left open. The paper's claim is normative: a reader should, since only that gives
it a turn, the Cauchy with its median at the corner, and true angles.

**What we build on.** The method is Jaynes's (1968, 1973): state an observer's ignorance as a group of transformations,
and take the measure the group leaves unchanged. We choose the group: turns of the reader's bar, rescalings of the
other party's size, and the exchange of the two unit relations. Given that the sweep is the turning of a rigid bar,
these select the uniform turn and its Cauchy, and the corner; through amounts, the same indifference
to scale motivates the logarithm past the corner. The geometry is claimed as necessary relative to that stated
ignorance, not absolutely. What is ours is the choice of group, the near field, and reading the measure as a reader's
addresses rather than its belief.

**Related work.** The pieces are classical: the Cauchy as the projection of a uniform angle (Jones 1999; Cacoullos
2014), its Möbius invariance (Knight 1976; McCullagh 1996), its stability (Lévy 1925), reciprocal symmetry (Jones
2008b; Cacoullos and Papadatos 2013), Klein's Erlangen programme, Haar's uniqueness. In computing, the same structures
appear by design in the hyperbolic browser (Lamping, Rao and Pirolli 1995), mipmaps (Williams 1983), web-map tile keys,
floating-point numbers and depth buffers; in perception, Schwartz's log-polar map of visual cortex, proportional near
the fovea and logarithmic beyond (1977). Scales that are linear near a unit and logarithmic far from it are common, as
in astronomy's asinh magnitudes (Lupton, Gunn and Szalay 1999); what is added here is the join placed at the
reciprocal's fixed point, where the two spacings agree. In terms of limits, a writer's account lets the resolution go to
zero first and then lets the count of things grow without bound; a situated reader has a fixed resolution and an
unknown count, the order a program with finite memory lives in.

## References

Bedrosian, E. (1963). A product theorem for Hilbert transforms. *Proceedings of the IEEE* 51(5), 868–869.

Boyd, J. P. (1982). The optimization of convergence for Chebyshev polynomial methods in an unbounded domain.
*Journal of Computational Physics* 45, 43–79.

Boyd, J. P. (1987). Spectral methods using rational basis functions on an infinite interval. *Journal of
Computational Physics* 69, 112–142.

Böröczky, K. (1974). Gömbkitöltések állandó görbületű terekben I. *Matematikai Lapok* 25, 265–306.

Cacoullos, T. (2014). Polar angle tangent vectors follow Cauchy distributions under spherical symmetry. *Journal of
Multivariate Analysis* 128, 147–153.

Cacoullos, T. and Papadatos, N. (2013). Self-inverse and exchangeable random variables. *Statistics & Probability
Letters* 83(1), 9–12.

Dietz, P. F. (1982). Maintaining order in a linked list. *Proceedings of the 14th ACM Symposium on Theory of
Computing*, 122–127.

Furnas, G. W. and Bederson, B. B. (1995). Space-scale diagrams: understanding multiscale interfaces. *Proceedings of
CHI '95*, 234–241.

Gabor, D. (1946). Theory of communication. *Journal of the Institution of Electrical Engineers* 93(26), Part III,
429–457.

Gustafson, J. L. and Yonemoto, I. T. (2017). Beating floating point at its own game: posit arithmetic.
*Supercomputing Frontiers and Innovations* 4(2), 71–86.

Haar, A. (1933). Der Massbegriff in der Theorie der kontinuierlichen Gruppen. *Annals of Mathematics* 34(1), 147–169.

Hastings, W. K. (1970). Monte Carlo sampling methods using Markov chains and their applications. *Biometrika* 57(1),
97–109.

IEEE (1985). *IEEE Standard for Binary Floating-Point Arithmetic*, ANSI/IEEE Std 754-1985. Institute of Electrical
and Electronics Engineers, New York.

Igarashi, T. and Hinckley, K. (2000). Speed-dependent automatic zooming for browsing large documents. *Proceedings
of UIST 2000*, 139–148.

Itai, A., Konheim, A. G. and Rodeh, M. (1981). A sparse table implementation of priority queues. *Automata,
Languages and Programming (ICALP 1981)*, Lecture Notes in Computer Science 115, 417–431.

Jaynes, E. T. (1968). Prior probabilities. *IEEE Transactions on Systems Science and Cybernetics* 4(3), 227–241.

Jaynes, E. T. (1973). The well-posed problem. *Foundations of Physics* 3(4), 477–493.

Jones, M. C. (1999). Distributional relationships arising from simple trigonometric formulas. *The American
Statistician* 53(2), 99–102.

Jones, M. C. (2008b). On reciprocal symmetry. *Journal of Statistical Planning and Inference* 138(10), 3039–3043.

Kalman, R. E. (1960). A new approach to linear filtering and prediction problems. *Journal of Basic Engineering*
82(1), 35–45.

Karger, D., Lehman, E., Leighton, T., Panigrahy, R., Levine, M. and Lewin, D. (1997). Consistent hashing and random
trees. *Proceedings of the 29th ACM Symposium on Theory of Computing*, 654–663.

Klein, F. (1872). *Vergleichende Betrachtungen über neuere geometrische Forschungen*.

Knight, F. B. (1976). A characterization of the Cauchy type. *Proceedings of the American Mathematical Society* 55,
130–135.

Knuth, D. E. (1998). *The Art of Computer Programming*, Vol. 3: *Sorting and Searching*, 2nd ed. Addison-Wesley,
Reading, MA.

Lamping, J., Rao, R. and Pirolli, P. (1995). A focus+context technique based on hyperbolic geometry for visualizing
large hierarchies. *Proceedings of CHI '95*, 401–408.

Lévy, P. (1925). *Calcul des probabilités*. Gauthier-Villars, Paris.

Lupton, R. H., Gunn, J. E. and Szalay, A. S. (1999). A modified magnitude system that produces well-behaved
magnitudes, colors, and errors even for low signal-to-noise ratio measurements. *The Astronomical Journal* 118(3),
1406–1410.

McCullagh, P. (1996). Möbius transformation and Cauchy parameter estimation. *The Annals of Statistics* 24, 787–808.

Mercator, G. (1569). *Nova et aucta orbis terrae descriptio ad usum navigantium emendate accommodata*. Duisburg.

Metropolis, N., Rosenbluth, A. W., Rosenbluth, M. N., Teller, A. H. and Teller, E. (1953). Equation of state
calculations by fast computing machines. *The Journal of Chemical Physics* 21(6), 1087–1092.

Microsoft. Bing Maps Tile System (documentation).

Munro, J. I. and Paterson, M. S. (1980). Selection and sorting with limited storage. *Theoretical Computer Science*
12(3), 315–323.

Niven, I. (1956). *Irrational Numbers*. Carus Mathematical Monographs 11, Mathematical Association of America.

Plücker, J. (1865). On a new geometry of space. *Philosophical Transactions of the Royal Society of London* 155,
725–791.

Polyak, B. T. and Juditsky, A. B. (1992). Acceleration of stochastic approximation by averaging. *SIAM Journal on
Control and Optimization* 30(4), 838–855.

Robbins, H. and Monro, S. (1951). A stochastic approximation method. *The Annals of Mathematical Statistics* 22(3),
400–407.

Schwartz, E. L. (1977). Spatial mapping in the primate sensory projection: analytic structure and relevance to
perception. *Biological Cybernetics* 25, 181–194.

Sós, V. T. (1958). On the distribution mod 1 of the sequence nα. *Annales Universitatis Scientiarum Budapestinensis
de Rolando Eötvös Nominatae, Sectio Mathematica* 1, 127–134.

Thomas, L. H. (1926). The motion of the spinning electron. *Nature* 117, 514.

van Wijk, J. J. and Nuij, W. A. A. (2003). Smooth and efficient zooming and panning. *Proceedings of IEEE InfoVis
2003*, 15–23.

Weyl, H. (1916). Über die Gleichverteilung von Zahlen mod. Eins. *Mathematische Annalen* 77, 313–352.

Williams, L. (1983). Pyramidal parametrics. *Computer Graphics* (Proceedings of SIGGRAPH '83) 17(3), 1–11.
