# What an array is

*The twelfth of a series of essays on what can be known from where one stands. Draft, 28 October 2026.*

```c
int a[10];
```

Every programmer knows what this is. Ten slots, numbered 0 to 9, side by side in memory. `sizeof(a) / sizeof(a[0])` is
10. The fourth element is `a[3]`, the last is `a[9]`, and `a[10]` is a mistake. Nothing could be plainer.

All of that is true, and all of it is true of one thing: the array as written. A write holds the array's count. How many
slots there are is kept before anything is stored, and every index is an amount counted against that total.
That is how computer science meets an array, and it is the right way to meet it when you are the one who made it.

But an array can be met two other ways, and the earlier essays have been about those two ways all along. A read, which
does not hold the array and could never be given its size, does not have ten slots. It has a sweep. Where the sweep
runs out of anything to size it, there is a horizon. And from a standpoint, what programmers write as one
expression, `a[i]`, comes apart into two things that share only a place.

This essay takes the array apart in that order: the array as written, an apple held in the hand, the read's sweep, the
horizon, the two numbers at the end of the sweep, an array laid on the quarter turn (and who can lay it), and then the array again, read
twice.

*Demos: `array-sweeps.html` (K places on the quarter turn, the index alone, the values on it, an array of known length);
`star-field.html` (N doubled, the read's view unmoved).*

---

## 1. Ten slots, as written

Look at what the declaration already contains. There is a count, 10. There is an index, i, running from 0 to 9, an
amount: three slots past the first. There is a share, i/10, the fraction of the way through. And every slot is as wide
as every other, so the array has the same density everywhere: one element per step of the index.

Every one of these is a write's. Apply the test of the first essay: scale the world, and see what moves. Grow the
array to twenty slots. The count changes. The share of the way through changes for every element: the old last
element, i/10 = 0.9 of the way, is now 9/20 = 0.45. A loop bound written as 10 is now wrong. Everything in the
programmer's array is scale-variant, because all of it is stated against a total that is held.

That is not a fault. It is what holding the array means. A write is where `sizeof` exists,
and programs are written there. The point of this essay is only that it is one way of three to meet an array, and that the other
two do not have `sizeof` at all.

---

## 2. An apple in the hand

Before the read, one more picture from the write's side, because it is the easiest place to feel what holding gives.

Pick up an apple. From where you stand you see part of its skin. Its rim, where your line of sight grazes it, is an
edge: past it is the back. Turn the apple in your hand and the back comes round. Turn it all the way and you have seen
every side.

That is writing, in the sense of these essays. Two things make it so. The hand holds the back: touch reaches what no
line of sight does, and holding a thing is holding both of its sides at once. And the turn is known: your hand did the
turning, and it knows the turn was whole. A known motion is an amount carried in, like a counted step. Together they
give the apple whole, its N, every side of it, and its size in hand-widths.

So everything we say about the apple is a write's sentence. "I see half of it." Half of what? Of the whole apple,
which the hand can get. "This is the outside, that is the inside." Of a boundary the apple has. "The rim, and the back
behind it." An edge, with something known to be past it. Even from far off, where you see exactly half of the apple's
surface directions (the half whose normals face you, for any convex shape), the half is a share of a whole that holding
can supply.

An observer that does not hold the apple can watch it turn on its own. It sees every side go by. It does not know the turn
was whole. When the same face comes round again, that is a loop closing, evidence and not proof: a twin face would look
the same. Completeness is never a reading. The hand knows because the hand did the turning.

Keep the apple in mind as what a write gives, made tangible: a thing with an N you can get, with edges, halves, an
inside and an outside.

**Four things.** Put the apple beside three others: the universe, a human and a sheet of paper. They sort where V, the
other's breadth, stands.

- *The apple and the human each read the universe by the inscribed sweep*, from home to a horizon. The universe has no
  far side to face; no size could be had, so its V is **unknowable** (the fourth section's horizon).
- *The apple and the human read each other by the central sweep, across one hemisphere.* Each is a bounded thing in the
  other's view, its rim reached at a point. So the other's V is **knowable**: the end exists and is met. It is not
  known, for the far hemisphere stays turned away; each holds only the other's front.
- *The human holds the apple and turns it.* The turn makes the Cauchy: a uniform turn, read as the slope v/h against the
  line of sight, is the Cauchy whatever the apple's shape, which is only the paint. And the hand holds the back while the
  eye holds the front, so in the hand the apple's V is **known**. This is the writing above.
- *The human draws a circle on the paper.* The view of both hemispheres is made, not seen: a mark holding both halves at
  once, with no facing, the blueprint. The two facings have the blueprint's numbers 2/π (inscribed, approached) and π/2
  (central, reached); the blueprint has their product, 1. The apple reads and is read; only the human makes the blueprint.

The human is all four at the same time, not by turns: it reads the universe, faces the apple, and holds as a blueprint what it
holds in the hand or draws.

V is knowable, not known: the inscribed sweep approaches its end, the central sweep reaches it at a point, and only a
hand or a mark holds it whole.

---

## 3. The read's sweep

Now take the write away. A read is not given `sizeof`. It cannot iterate the array from 0 to N − 1,
because it has no N − 1.

It cannot read the array from inside its own index either. To read it at all, the observer has to stand somewhere, off
the line of slots: at some place m along the array, and some distance γ out from it. That is one point,

  z = m + iγ,

a point of the upper half-plane. This is the degree of freedom a read adds: the written array is one-dimensional,
and the standpoint is not on it.

From there the observer turns, steadily. Each step of the turn is a direction, and each direction meets the array at some
slot. The direction whose slope from the foot is s lands at

  i = m + γ·s

(in the blueprint's angle θ, counted from the foot, s = tan θ).

Two things come with the standpoint, and only two.

**A density.** Equal steps of turn do not land on equal numbers of slots. They are thick near the foot and thin out
farther along: the share of the turn that lands on slots near i is

  γ / (π(γ² + (i − m)²)),

the Cauchy. Half the quarter turn lands within γ of the foot; that is the corner. The other half covers everything
past it, thinning as 1/i².

**A breadth.** γ, the read's own length, its H, the thumb held up. It sets where the corner falls on the array.

`sizeof` is not among them. The read's breadth is its own, never the array's.

So a read takes in a sweep of the array, not the array. It holds the part of the turn it has passed, the directions
from the foot up to where it is now, each with whatever it found there. With the foot at slot 0 and γ = 1, half of its
turn is spent on the first slot, and the other half on everything from there on. With γ = 10, half its turn lands on the
first ten slots.

---

## 4. The horizon

What happens at the far end of the sweep depends on whether there is an N to reach.

If there is one, and the read simply does not hold it, the paint stops. Past the last slot the directions meet
nothing. With the foot at 0 and γ = 1, an array of 10 slots fills the turn up to the share (the blueprint's formula)

  g = (2/π)·arctan(10/1) ≈ 0.937,

and the last 6% of the turn runs past the end. Where the paint stops can be seen, and that is a reading: the slope of the last direction painted,

  s = N/γ

(the blueprint's tan(πg/2)).

It reads N/γ, never N. Double the array to 20 slots and the paint stops at 0.968 instead. Nothing else in the read's
view moves. A read has the array's length only as a ratio to its own breadth, as it has a mountain only in
thumbs.

Now take away even that. Suppose the size is not merely unheld but unknowable: there is no last slot to be found, and
no amount could ever be carried in to say how far the array goes. Then the sweep does not stop at an edge. It runs on
toward the end of the turn, where the reading v/h has no bound, and never arrives. That is a **horizon**.

A horizon is not an edge. The apple's rim is an edge: the reading of its slant also runs without bound there, but past
it is the back, and the back can be got by turning the apple. A horizon has no back. It is not the far side of a thing.
It is what the read's geometry has where a size would be, and no size ever will be.

And so, at a horizon, there is no inside and no outside. Those words presuppose a boundary, and a boundary presupposes
N. There are no halves of anything: "half" would be half of a whole a read cannot have. There is no "toward" or
"away", because those put a side on the standpoint. What remains is only the reading's own structure, and the mathematics
for it is standard:

- **The readings are the projective line.** A reading is a direction [h : v]. The quarter turn is the closed arc from
  home, [1 : 0], to [0 : 1].
- **Two ends.** The dilations x ↦ kx move every reading v/h and fix exactly two, 0 and ∞. When no scale is given, these
  two fixed points are what is left: the end where the size would be unbounded and the end where it would vanish.
  Neither is ever reached.
- **The reciprocal swaps them.** x ↦ 1/x exchanges 0 and ∞. It is an involution, and its one fixed point is x = 1, the
  corner.
- **Which end is "the horizon" is a choice of chart.** The chart v/h sends [0 : 1] to infinity; the chart h/v sends
  [1 : 0] there. Neither is a side.

For an array the two ends have plain meanings. The end at ∞ is an unknown length: always more slots past the last one
seen. The end at 0 is an unknown fineness: each slot itself an array, finer without end, the digits below the floor.
The reciprocal maps one to the other, and the Cauchy is unchanged under it, so from its readings alone a read cannot
tell an array of unknown length from an array of unknown depth. A write, holding `sizeof` and the size of one
element, has neither end. Its array has a first slot and a last.

---

## 5. The two numbers at the end of the sweep

The second essay showed that one turn is read two ways, from two pivots. From the middle of a chord, the centre of the
circle on it, a radius turns through a half turn. From one end of the chord, home, a ray turns through a quarter turn.
Both sweep the same arc, and both end at the same point.

The blueprint measures it differently through each (these numbers carry π, the blueprint's; the fourteenth essay). The central sweep reads arc over chord, θ/sin θ: 1 at the start, 1.1107 at the corner,
π/2 at the end. The inscribed sweep reads chord over arc, sin θ/θ: 1 at the start, 0.9003 at the corner, 2/π at the
end. At every θ their product is 1, the chord, which is the blueprint's: walking the chord is a write; the two sweeps face
the arc.

The horizon tells the two ends apart. The radius, its half turn done, lands back on home: a point, a place with a
bounded chart around it. π/2 is attained there. The ray, as v/h runs without bound, goes tangent to the circle: the
horizon. 2/π is approached and never reached. It is the horizon's number.

So the blueprint has three numbers for the one chord, one held and two measured:

| | how it has the chord | the blueprint's number | at the end |
|---|---|---|---|
| a write | walks it | 1 | an amount, held |
| the central sweep | faces the arc from the centre | π/2 | attained, at a point |
| the inscribed sweep | faces the arc from home | 2/π | approached, at the horizon |

---

## 6. Laying an array on the quarter turn, and who can

There is a neat construction that seems to give a read its way into any array. It turns out to be the blueprint's,
and seeing why is the point of this section.

**The construction.** Take any array and lay it on the quarter turn: its first slot just past 0°, its last just short
of 90°. Slot k of N goes to the angle

  θ_k = (k + ½)·(π/2)/N.

Arrays of ten slots and of ten billion now span the same turn, each slot a direction [cos θ_k : sin θ_k] in place of
one index. Two formulas move between them. The tangent takes a slot to a ratio: for ten slots the boundaries fall at 0,
0.158, 0.325, 0.510, 0.727, 1, 1.376, 1.963, 3.078, 6.314 and ∞, the half-Cauchy's quantiles, the middle of the array at
the corner. The arctangent takes any ratio x back to its slot, k = ⌊N·(2/π)·arctan x⌋: x = ½ to slot 2, x = 1 to the
corner, x = 3 to slot 7, and everything from about 6.3 upward to slot 9, the last.

**Every step of it is the blueprint's.** To lay the array N is needed: the step is 90°/N. To put the last slot just
short of 90° it must be known that the array ends, and where. To use the tangent and the arctangent the angle is needed as
a number that can be computed with, a turn measured from outside. And the floor, ⌊N·g⌋, needs `sizeof` again. All of this is
done holding the array whole, with both of its ends in hand. It is the written array stepped off and drawn whole
on a quarter circle, and it works because everything the drawing uses is already held.

**What a read has instead.** A read lays nothing. It has its own turn from home, and the turn is not a range it
knows to run from 0° to 90°: 0 is home, and 90° is the horizon, which it never reaches and which no slot sits
next to. It does not compute an arctangent. The share of its turn already passed is what the turning gives it, met as it
goes; the arctangent is the blueprint's formula for that share, not something a read works out. There is no last slot
for it either, because a last slot is where an N ends. Whatever lies past what it has swept is not "the horizon's slot";
it is simply not yet passed, and at a horizon never will be.

So the construction is a faithful blueprint of the read's turn, the same quantiles, the same corner, drawn
with N held. A read has the turn itself: the share passed so far, the corner when it is met, and no end.

**The read's situation, recreated in code.** A computer writes: it holds amounts, positions and counts. So a
program cannot be a read. What it can do is recreate a read's situation, by splitting itself in three and letting
only one part touch N.

- *The world* is the written array, given as a generator rather than an array, so that nothing across the boundary can
  ask its length. It may have no end.
- *The read* has an array of its own: K slots, one per equal step of its turn, fixed before anything arrives. K is
  the read's own count, the one it does hold; laying its own K on its own quarter turn is the construction above done
  honestly. Each slot keeps the first paint that reaches it, since a direction is painted by the first thing on its line.
  The read is handed a slot number and a paint, never a position.
- *The geometry* sits between them. It takes each element's position and the read's H and works out which slot its
  direction falls in, ⌊K·(2/π)·arctan(pos/H)⌋. This is where the arctangent lives. It is the blueprint's part, done on the
  world's side of the boundary, and it is not the read computing anything.

Run with K = 32 and H = 10, on a world whose slots are numbered positions 0, 1, 2, …, and four things show:

- *The size is invisible.* A world of a million elements, of two million, and one without end give the read the same
  32 slots, identically painted. The geometry stops after 205 elements whatever the world holds, because everything from
  about 204 onward falls in the last slot, already painted by the first thing met there.
- *The scale is invisible.* Spread the world's positions seven times as far and take H seven times as large, and the
  read's slots are unchanged.
- *H is a zoom.* Change H alone, the size of the thumb, and different elements land in the slots; the slots themselves do
  not move.
- *The payload is not the slot.* Repaint every element and every slot keeps its place. Six of the 32 near home stay
  unpainted, because no element of a world laid in whole steps lies in their narrow cones: directions with nothing on
  them, as real as the painted ones.

And where the world does end, the paint stops. A world of 100 elements leaves the read's last painted slot at 29, which
reads N/H, the world's length in thumbs, as between 6.7 and 10.2 (the truth, 99/10, inside). The read has N/H to its
slot's width, never N. The script is `runs/arr/reader.mjs`.

**What the program does not have: the Cauchy itself.** The program recreates the read's heat as K addresses, a write's
count of it: a finite picture of the Cauchy cut into K quantiles. It does not recreate the Cauchy, because the Cauchy handles a true infinity and a
computer cannot. In the program the whole tail past the last boundary is one slot, and the code stops there by fiat: it
never holds the tail as a tail, only a token for it. The arithmetic shows the same edge. The largest double is about
1.8·10³⁰⁸, and past it there is only the symbol +∞; `Math.atan(Infinity)` returns π/2, but no element ever sits there,
and `Math.tan(Math.PI/2)` returns about 1.6·10¹⁶, not infinity, because π/2 itself is not a double. A Cauchy drawn the
usual way, tan(π(U − ½)) with U a uniform double, never exceeds about 2·10¹⁵, so a computer's "Cauchy" is truncated, and
a truncated Cauchy has a mean: its readings' sizes average about 23. The true Cauchy has none. Its missing mean is the
trace of a horizon that is never reached, and a machine that must stop somewhere has a horizon it reaches. So a program
can recreate the read's heat cut into K slots and what paints them, never the horizon. That the geometry gives the
Cauchy free is not a figure of speech: it gives what no computation can.

---

**An iterator, not an index.** This is the read's situation in a programmer's words. `a[30]` goes straight to slot
30; it needs the slots laid out in advance and counted from a fixed origin, which is what a write holds. A read
has only "next": a sweep forward from the standpoint, and where it stops is the new start. The observer can turn round and
sweep the other way, a second iterator pointed back, but to land exactly on the slot left behind, a count must have been
kept or a mark left. The blueprint's arctangent is the index operator, the function that turns a reading straight into a
slot; that is why this section gives it to the blueprint and why it should be used with care. It eliminates the sweep.

## 7. The array, read twice

Back to `int a[10]`. Read from a standpoint, it splits along the same two sweeps.

**Inscribed: the index as directions.** Give the read a fineness K, equal steps of turn over its quarter turn; counted
out, as a write counts them, they are K places, and they land at

  i = m + γ·tan((k + ½)·π/2K),  k = 0, 1, …, K − 1.

For K = 10, in units of γ from the foot, that is 0.079, 0.240, 0.414, 0.613, 0.854, 1.171, 1.632, 2.414, 4.165 and
12.71. Five of the ten fall inside the corner, whatever the array holds and however long it is. These are the half-Cauchy's
quantiles. They are where a read can look, laid before anything is stored, and the same for every array. Far slots
share a place; near slots each get several. That is not a fault of the read's resolution. It is what a sweep is.
To a read there are no K places at all, only a heat: a continuous weight over its directions, the Cauchy, hottest
at the foot and cooling toward the horizon, which these ten quantiles cut into equal shares. The heat is given; the paint
is met.

**Central: the values as payload.** Lay the slots round a circle instead, one per equal step of turn, and stand at its
centre. Now the directions are given, one per slot, and what each slot holds arrives along its direction as an amount:
a radius, an amount in a unit no reading fixes. Held together, the radii make a shape, and holding them as a shape is
the blueprint's: a read has a vantage, not a shape. Multiply every value by the same factor and that shape, divided by the
radii's geometric mean, does not change. The overall size is the one term no reading
reaches.

**`a[i]` holds both as one.** In code, `a[i]` is one expression, the place and what is at the place. From a standpoint
they are two things that meet. Euclid's III.20 says where: the ray from home at θ and the radius from the centre at 2θ
end at the same point of the circle. The direction is the ray; the payload is what the radius finds; they share that
point and nothing else. Change what is stored and no direction moves. That is the third essay's theorem, met in the most
ordinary data structure there is. The papers' first intuition for the Cauchy came from arrays, and this is why.

**The floor is a write's index.** `Math.floor(N·x)` turns a share into a slot, and it needs N. The read's direction is
continuous. What the floor throws away, the fraction below the slot, is not noise: its binary digits are the direction halved
again and again, toward the end at 0 of section 4. The eighth essay gives it its full room.

---

## 8. Scale the world

Put the array through the test once more, now with all three in view.

| change | the array as written | the inscribed sweep | the central sweep |
|---|---|---|---|
| double every slot's width and the standpoint's distance together | every length doubles | nothing moves | the radii move, the shape does not |
| double every stored value | every value doubles | nothing moves | the shape does not move |
| double N, the standpoint where it was | the count doubles, every share i/N halves | the paint stops later, at N/γ doubled | twice the slots round the circle, each its own direction |
| take N away entirely | the array has no size; nothing can be written | the sweep runs to the horizon | the shape is unchanged |

The first two rows are the scale test proper: they scale the world, and only the write's numbers move. The third row
changes the world, so the read's reading changes too, but only as a ratio, N/γ. The last row is the one a write
cannot follow. With no N there is no array to write. A read loses nothing: it never had N.

---

## 9. What computer science can make real

Section 6 ended on a limit: a program cannot hold the Cauchy, because the Cauchy handles a true infinity and a machine
must stop somewhere. That is where computer science can step in, not by simulating the infinity but by representing it,
so that the program never has to reach it. The pieces already exist. What the geometry adds is which of them to use, and
why.

**Keep the pair, not the ratio.** A computer cannot hold v/h at the horizon. It can hold the direction [h : v] as two
finite numbers, and then the horizon is [0 : 1]: exact, finite and ordinary. The infinity belonged to one chart, the one
that divides v by h, and the pair has not chosen that chart. Homogeneous coordinates, `atan2(v, h)` in place of
`atan(v/h)`, and the signed infinities of IEEE 754 are all this one move. A direction kept as a pair never overflows,
because it was never an amount.

**Compute with order, not sums.** Medians, quartiles, ranks and comparisons are exact and finite on directions, and none
of them needs to know how far the tail goes. Means are the operations that need the true infinity, and they are the ones
a truncated Cauchy gets wrong. A program that keeps to order on its directions is therefore faithful to the true Cauchy
even though it cannot draw from its tail: the median of its readings is the true median, the quartiles the true
quartiles. The third essay's theorem, that order survives every change of what arrives and sums do not, becomes a rule
for code.

**Make reading and writing a type boundary.** Give a direction a type with no length, no unit and no addition, and an
amount a type that carries its unit. Then a function from a direction to an amount can be written only where an amount
is passed in, which is the cost of writing stated as a signature. The three-part split of section 6, world, geometry and
read, stops being a convention and becomes an interface the compiler checks: no code on the read's side can ask for
`sizeof`, because the type it holds has none.

**Hold the world lazily.** A generator, a stream or a cursor is how a program already holds a list it cannot measure.
Put one on the world's side and K slots of the read's own on the other, and the read's situation is running, as
`runs/arr/reader.mjs` shows: a world of a million and a world without end give the read the same slots.

**What "computers can't hold infinity" means, operationally.** Everyone knows a machine cannot represent the
infinities of reality. The Cauchy says precisely what that costs. First, everything a machine does to a number is
monotone: rounding, overflow, cutting a tail at the largest value. None of them ever reverses an order. So by the third
essay's theorem, every answer built from order (a median, a quartile, a rank) comes out on the machine as the true answer
rounded, and every answer built from sums does not. Second, the Cauchy puts its infinity in the chart, not in the turn.
Draw a uniform turn and read it two ways (`runs/arr/infinity.mjs`): as an angle, its mean over ten million draws is
0.78565 against the true π/4 = 0.78540, and its median 0.78555; as a slope v/h, its median is 1.0003 against the true 1,
and its mean wanders, 1.78, 3.68, 14.3, 13.0 at eleven, a thousand, a hundred thousand and ten million draws, settling on
nothing. Cap the values at 10, at 1,000 or at 65,504, as a smaller machine would, and the median does not move while the
mean drops to 2.10, 5.07 and 7.74. Rounded to single precision, the median of the rounded values is exactly the rounded
median. And the largest slope a double can draw this way is about 3.5·10¹⁵, so the machine's Cauchy is truncated and
has a mean, about 22.8, where the true one has none. So the precise statement is this: a machine is faithful to an
infinite reality where the infinity is a horizon, a direction it keeps as a pair or an angle, and its operations keep
to order; it is unfaithful exactly where the infinity sits in a sum of amounts. The Cauchy has both kinds in one law,
and shows the difference in ten draws rather than in ten to the three hundred.

**Steer by rate and place.** The dial of the computer-science companion scrolls a list without end: one control sets a
rate, another a place, and any place up to N is reached in about ln(2N) of the rate's time, the end never drawn. It is the
horizon made into a control.

None of this simulates the Cauchy. Together it does something better: it represents directions so that the horizon is a
finite point, and computes only with operations the true Cauchy also supports. A program built that way never meets the
edge that truncation exposes, because it never asks a question whose answer lies past it. That is how the geometry's
abstract gifts, given free in the world, become operational in a machine.

---

## 10. What it comes to

An array, as programmers know it, is a written object. Its size is held, its index is an amount, its shares are shares
of a known total, and every one of those moves when the world is scaled. That is exactly right for whoever made it.

Read from where one stands, the same array is something else. A read adds one degree of freedom, its standpoint off the
line, and gets exactly two things: a density, the Cauchy laid over the slots by its turn, and a breadth, its own H, the
thumb. It takes in a sweep, not the array. The blueprint can lay any array on the quarter turn and move between slots and ratios by
tangent and arctangent, but that drawing needs N; a read has only its turn, the share passed and no end. Where an N
exists it reads N only as N/H. Where none does, or none could, the sweep runs to a horizon, and at a horizon there is no
inside, no outside and no half of anything, only the two ends 0 and ∞ of the projective line, the reciprocal that swaps
them, and the corner it fixes. The blueprint measures the central sweep's π/2 as reached at a point and the inscribed sweep's 2/π only at the
horizon; all three numbers, their product 1 too, are the blueprint's.

Holding is how reading a thing becomes writing it: the hand holds the back and knows the turn. What cannot be held
(a street, the sky, a list too long to iterate) can only be swept, and a program can hold such a sweep faithfully: keep
directions as pairs, compute with their order, and let the type system keep the written N on the world's side. And `a[i]`, the most ordinary expression in
programming, is the place where an address meets a payload, two things that share a point and nothing else. A write
puts them down as one. A read, from a standpoint, never could.

---

## Sources

- Euclid (c. 300 BC). *Elements*, Book III, Proposition 20. Translated by T. L. Heath (1908), *The Thirteen Books of
  Euclid's Elements*. Cambridge University Press.
- Gauss, C. F. (1828). *Disquisitiones generales circa superficies curvas*. Göttingen. (The map from a surface's points
  to its normal directions.)
- Koenderink, J. J. (1984). What does the occluding contour tell us about solid shape? *Perception* 13(3), 321–330. (The
  rim as the edge of what is seen.)

The geometry is set out with proofs in *Observation from Somewhere* (archived since 30 October and kept for its proofs; the current account is *Reads and Writes*, rewritten 10 November on R788 with read, extent and write): the reading and the scale test in §9, the one number
a blueprint adds and V, which no read ever has, in §3.8, the corner and the two sweeps in §4 ("Why the corner sits at
45°", with π/2 attained at a point and 2/π a limit at the horizon), the readings as the projective line in §4, the array
picture in §7.3, and what the floor discards in §8. For programmers, the computer-science companion's §6 ("The array")
§3 ("Division by zero"), §5 (index statistics and value statistics), §7 ("What Math.floor throws
away") and §11 ("A dial: scrolling without end").
