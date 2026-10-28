# What an array is

*The twelfth of a series of essays on what can be known from where one stands. Draft, 28 October 2026.*

```c
int a[10];
```

Every programmer knows what this is. Ten slots, numbered 0 to 9, side by side in memory. `sizeof(a) / sizeof(a[0])` is
10. The fourth element is `a[3]`, the last is `a[9]`, and `a[10]` is a mistake. Nothing could be plainer.

All of that is true, and all of it is true from one vantage: the writer's. The writer holds the array whole. It knows
how many slots there are before it stores anything, and every index it uses is an amount counted against that total.
That is how computer science meets an array, and it is the right way to meet it when you are the one who made it.

But an array can be met two other ways, and the earlier essays have been about those two ways all along. A reader that
does not hold the array, and could never be told its size, does not see ten slots. It sees a sweep. Where the sweep
runs out of anything to size it, there is a horizon. And from where the reader stands, what programmers write as one
expression, `a[i]`, comes apart into two things that share only a place.

This essay takes the array apart in that order: the writer's array, an apple held in the hand, the reader's sweep, the
horizon, the two numbers at the end of the sweep, and then the array again, read twice.

*Demos: `array-sweeps.html` (K places on the quarter turn, the index alone, the values on it, an array of known length);
`star-field.html` (N doubled, the reader's view unmoved).*

---

## 1. Ten slots, from the writer's vantage

Look at what the declaration already contains. There is a count, 10. There is an index, i, running from 0 to 9, an
amount: three slots past the first. There is a share, i/10, the fraction of the way through. And every slot is as wide
as every other, so the array has the same density everywhere: one element per step of the index.

Every one of these is the writer's. Apply the test of the first essay: scale the world, and see what moves. Grow the
array to twenty slots. The count changes. The share of the way through changes for every element: the old last
element, i/10 = 0.9 of the way, is now 9/20 = 0.45. A loop bound written as 10 is now wrong. Everything in the
programmer's array is scale-variant, because all of it is stated against a total that is held.

That is not a fault. It is what holding the array means. The writer's vantage is the one from which `sizeof` exists,
and programs are written there. The point of this essay is only that it is one vantage of three, and that the other
two do not have `sizeof` at all.

---

## 2. An apple in the hand

Before the reader, one more picture from the writer's side, because it is the easiest place to feel what holding gives.

Pick up an apple. From where you stand you see part of its skin. Its rim, where your line of sight grazes it, is an
edge: past it is the back. Turn the apple in your hand and the back comes round. Turn it all the way and you have seen
every side.

That is writing, in the sense of these essays. Two things make it so. The hand holds the back: touch reaches what no
line of sight does, and holding a thing is holding both of its sides at once. And the turn is known: your hand did the
turning, and it knows the turn was whole. A known motion is an amount carried in, like a counted step. Together they
give the apple whole, its N, every side of it, and its size in hand-widths.

So everything we say about the apple is a writer's sentence. "I see half of it." Half of what? Of the whole apple,
which the hand can get. "This is the outside, that is the inside." Of a boundary the apple has. "The rim, and the back
behind it." An edge, with something known to be past it. Even from far off, where you see exactly half of the apple's
surface directions (the half whose normals face you, for any convex shape), the half is a share of a whole that holding
can supply.

A reader that does not hold the apple can watch it turn on its own. It sees every side go by. It does not know the turn
was whole. When the same face comes round again, that is a loop closing, evidence and not proof: a twin face would look
the same. Completeness is never a reading. The hand knows because the hand did the turning.

Keep the apple in mind as the writer's world made tangible: a thing with an N you can get, with edges, halves, an
inside and an outside.

---

## 3. The reader's sweep

Now take the array away from the writer. The reader is not given `sizeof`. It cannot iterate the array from 0 to N − 1,
because it does not know there is an N − 1.

It cannot read the array from inside its own index either. To read it at all, the reader has to stand somewhere, off
the line of slots: at some place m along the array, and some distance γ out from it. That is one point,

  z = m + iγ,

a point of the upper half-plane. This is the degree of freedom the reader adds: the writer's array is one-dimensional,
and the reader is not on it.

From there the reader turns, steadily. Each step of the turn is a direction, and each direction meets the array at some
slot. The turn's angle θ, counted from the foot, lands at

  i = m + γ·tan θ.

Two things come with the standpoint, and only two.

**A density.** Equal steps of turn do not land on equal numbers of slots. They are thick near the foot and thin out
farther along: the share of the turn that lands on slots near i is

  γ / (π(γ² + (i − m)²)),

the Cauchy. Half the quarter turn lands within γ of the foot; that is the corner. The other half covers everything
past it, thinning as 1/i².

**A breadth.** γ, the reader's own length, its H. It sets where the corner falls on the array.

`sizeof` is not among them. The reader's breadth is its own, never the array's.

So the reader reads a sweep of the array, not the array. It holds the part of the turn it has passed, the addresses
from the foot up to where it is now, each with whatever it found there. With the foot at slot 0 and γ = 1, half of its
turn is spent on the first slot, and the other half on everything from there on. With γ = 10, half its turn lands on the
first ten slots.

---

## 4. The horizon

What happens at the far end of the sweep depends on whether there is an N to reach.

If there is one, and the reader simply does not hold it, the paint stops. Past the last slot the directions meet
nothing. With the foot at 0 and γ = 1, an array of 10 slots fills the turn up to the share

  g = (2/π)·arctan(10/1) ≈ 0.937,

and the last 6% of the turn runs past the end. The reader can see where the paint stops, and that is a reading:

  tan(πg/2) = N/γ.

It reads N/γ, never N. Double the array to 20 slots and the paint stops at 0.968 instead. Nothing else in the reader's
view moves. The reader knows the array's length only as a ratio to its own breadth, as it knows a mountain only in
thumbs.

Now take away even that. Suppose the size is not merely unheld but unknowable: there is no last slot to be found, and
no amount could ever be carried in to say how far the array goes. Then the sweep does not stop at an edge. It runs on
toward the end of the turn, where the reading v/h has no bound, and never arrives. That is a **horizon**.

A horizon is not an edge. The apple's rim is an edge: the reading of its slant also runs without bound there, but past
it is the back, and the back can be got by turning the apple. A horizon has no back. It is not the far side of a thing.
It is what the reader's geometry has where a size would be, and no size ever will be.

And so, at a horizon, there is no inside and no outside. Those words presuppose a boundary, and a boundary presupposes
N. There are no halves of anything: "half" would be half of a whole the reader cannot have. There is no "toward" or
"away", because those put a side on the reader. What remains is only the reading's own structure, and the mathematics
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
The reciprocal maps one to the other, and the Cauchy is unchanged under it, so from its readings alone a reader cannot
tell an array of unknown length from an array of unknown depth. The writer, holding `sizeof` and the size of one
element, has neither end. Its array has a first slot and a last.

---

## 5. The two numbers at the end of the sweep

The second essay showed that one turn is read two ways, from two pivots. From the middle of a chord, the centre of the
circle on it, a radius turns through a half turn. From one end of the chord, home, a ray turns through a quarter turn.
Both sweep the same arc, and both end at the same point.

They measure it differently. The central sweep reads arc over chord, θ/sin θ: 1 at the start, 1.1107 at the corner,
π/2 at the end. The inscribed sweep reads chord over arc, sin θ/θ: 1 at the start, 0.9003 at the corner, 2/π at the
end. At every θ their product is 1, the chord, which is the writer's: only the writer walks the chord; the readers face
the arc.

The horizon tells the two ends apart. The radius, its half turn done, lands back on home: a point, a place with a
bounded chart around it. π/2 is attained there. The ray, as v/h runs without bound, goes tangent to the circle: the
horizon. 2/π is approached and never reached. It is the horizon's number.

So the three vantages have three numbers for the one chord:

| vantage | how it has the chord | its number | at the end |
|---|---|---|---|
| the writer | walks it | 1 | an amount, held |
| the central sweep | faces the arc from the centre | π/2 | attained, at a point |
| the inscribed sweep | faces the arc from home | 2/π | approached, at the horizon |

---

## 6. The array, read twice

Back to `int a[10]`. Read from a standpoint, it splits along the same two sweeps.

**Inscribed: the index as addresses.** Give the reader K addresses, equal steps of turn over its quarter turn. They land
at

  i = m + γ·tan((k + ½)·π/2K),  k = 0, 1, …, K − 1.

For K = 10, in units of γ from the foot, that is 0.079, 0.240, 0.414, 0.613, 0.854, 1.171, 1.632, 2.414, 4.165 and
12.71. Five of the ten fall inside the corner, whatever the array holds and however long it is. These are the half-Cauchy's
quantiles. They are where the reader can look, laid before anything is stored, and the same for every array. Far slots
share addresses; near slots each get several. That is not a fault of the reader's resolution. It is what a sweep is.

**Central: the values as payload.** Lay the slots round a circle instead, one per equal step of turn, and stand at its
centre. Now the directions are given, one per slot, and what each slot holds arrives along its direction as an amount:
a radius. The reader gets the shape those radii make, but in a unit no reading fixes. Multiply every value by the same
factor and the shape, divided by the radii's geometric mean, does not change. The overall size is the one term no reading
reaches.

**`a[i]` holds both as one.** In code, `a[i]` is one expression, the place and what is at the place. From a standpoint
they are two things that meet. Euclid's III.20 says where: the ray from home at θ and the radius from the centre at 2θ
end at the same point of the circle. The address is the ray; the payload is what the radius finds; they share that
point and nothing else. Change what is stored and no address moves. That is the third essay's theorem, met in the most
ordinary data structure there is. The papers' first intuition for the Cauchy came from arrays, and this is why.

**The floor is the writer's index.** `Math.floor(N·x)` turns a share into a slot, and it needs N. The reader's address
is continuous. What the floor throws away, the fraction below the slot, is not noise: its binary digits are the finer
levels, the end at 0 of section 4. The eighth essay gives it its full room.

---

## 7. Scale the world

Put the array through the test once more, now with all three vantages in view.

| change | the writer | the inscribed reader | the central reader |
|---|---|---|---|
| double every slot's width and the reader's distance together | every length doubles | nothing moves | the radii move, the shape does not |
| double every stored value | every value doubles | nothing moves | the shape does not move |
| double N, the reader where it was | the count doubles, every share i/N halves | the paint stops later, at N/γ doubled | twice the slots round the circle, each its own direction |
| take N away entirely | the array has no size; nothing can be written | the sweep runs to the horizon | the shape is unchanged |

The first two rows are the scale test proper: they scale the world, and only the writer's numbers move. The third row
changes the world, so the reader's reading changes too, but only as a ratio, N/γ. The last row is the one the writer
cannot follow. With no N there is no array to write. The reader loses nothing: it never had N.

---

## 8. What it comes to

An array, as programmers know it, is a writer's object. Its size is held, its index is an amount, its shares are shares
of a known total, and every one of those moves when the world is scaled. That is exactly right for whoever made it.

Read from where one stands, the same array is something else. The reader adds one degree of freedom, its standpoint off
the line, and gets exactly two things: a density, the Cauchy laid over the slots by its turn, and a breadth, its own H.
It reads a sweep, not the array. Where an N exists it reads N only as N/H. Where none does, or none could, the sweep runs
to a horizon, and at a horizon there is no inside, no outside and no half of anything, only the two ends 0 and ∞ of the
projective line, the reciprocal that swaps them, and the corner it fixes. The central sweep's π/2 is reached at a
point; the inscribed sweep's 2/π only at the horizon; and their product is the writer's 1.

Holding is how a reader becomes the writer of a thing: the hand holds the back and knows the turn. What cannot be held
(a street, the sky, a list too long to iterate) can only be swept. And `a[i]`, the most ordinary expression in
programming, is the place where an address meets a payload, two things that share a point and nothing else. The writer
writes them as one. The reader, standing somewhere, never could.

---

## Sources

- Euclid (c. 300 BC). *Elements*, Book III, Proposition 20. Translated by T. L. Heath (1908), *The Thirteen Books of
  Euclid's Elements*. Cambridge University Press.
- Gauss, C. F. (1828). *Disquisitiones generales circa superficies curvas*. Göttingen. (The map from a surface's points
  to its normal directions.)
- Koenderink, J. J. (1984). What does the occluding contour tell us about solid shape? *Perception* 13(3), 321–330. (The
  rim as the edge of what is seen.)

The geometry is set out with proofs in *Observation from Somewhere*: the reading and the scale test in §9, the one number
a blueprint adds and the reader that never knows V in §3.8, the corner and the two sweeps in §4 ("Why the corner sits at
45°", with π/2 attained at a point and 2/π a limit at the horizon), the readings as the projective line in §4, the array
picture in §7.3, and what the floor discards in §8. For programmers, the computer-science companion's §6 ("The array")
and §7 ("What Math.floor throws away").
