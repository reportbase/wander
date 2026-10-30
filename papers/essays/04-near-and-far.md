# Near and far

*The fourth of a series of essays on what can be known from where one stands. Draft, 28 October 2026.*

The first three essays built a reader with one length, a circle traced by turning it, and a law, the Cauchy, for the
directions that turn gives. This essay asks a practical question. A reader has only so many places to put things. How
should it lay them out, near and far?

The answer has two parts, split at the corner. Near, in proportion. Far, in doublings. Between them there is one point
and no seam. The essay also asks where the corner should go, and answers that a reader should put it on whatever it is
looking at. That is what H, the reader's one length, is for: not a measurement, but a zoom.

---

## 1. Fence posts on a plain

Stand on a flat plain beside a line of fence posts, evenly spaced, running straight away from you. Count them as they
recede.

The first few are easy. One post, two posts, three, each a clear step further than the last. You can see the gaps
between them in proportion: the second is twice as far as the first, the third three times.

Further out, something changes. The posts crowd together. You can still tell that the hundredth is further than the
fiftieth, but you cannot see fifty separate gaps between them. What you can see is that it is about twice as far.
Further still, you can tell that the thousandth is about ten times as far as the hundredth, and not much more.

Near things are read by their differences. Far things are read by their ratios. Somewhere between, the reading changes
from one kind to the other. The essays call that place the corner, and this essay is about the two kinds of reading on
either side of it.

---

## 2. Inside the corner: proportion

The reader has one length, H. Anything within that length can be laid out at its true scale against it: a thing half
of H away goes halfway out; a thing a quarter of H away goes a quarter of the way. This is the **near field**, and it is
laid in proportion. Inside it, H is a ruler.

Proportion is exactly what the near field needs. Differences there are what matter: whether a cup is a hand's width or
two hand's widths away decides whether you can reach it. A ruler with equal marks is the right tool.

The trouble comes past H. A ruler with equal marks never ends. A reader that kept laying things out in proportion beyond
its own length would need room without limit.

---

## 3. Past the corner: what the far field has to be

So how should a reader lay out the things beyond H? Suppose it places a far thing, x times H away, at some position on
its layout, and that the position grows with x. What rule should the growth follow?

There is one natural condition. The reader's choice of H is free; nothing in its readings fixes it. A reader that chose
H twice as large would see every far amount as half as many H's away. If the layout gave a stretch of distances more or
less room depending on where that stretch happened to fall, then the room would depend on the arbitrary choice of H. So
the layout should give a stretch from x to λx the same room wherever it falls: room that depends on the ratio λ alone,
not on x.

That one condition decides the layout. Only one rule gives every stretch of the same ratio the same room: the
logarithm. Every doubling gets the same number of places, every tenfold the same number again. The proof is a classical
functional equation, the one Cauchy solved in 1821: a function that turns products into sums, and grows, must be a
logarithm. And if the far layout is to join the near one without a kink at the corner, the logarithm has to start there
with the same slope: one plus the natural logarithm of x.

It is worth seeing why the obvious alternatives fail.

- **Proportion all the way out** gives the stretch from x to λx room proportional to x. Far stretches get more and more
  room, which is a preference for the far.
- **A power** of x does the same in a milder way.
- **A logarithm with a correction** gives room that depends on where you are, which smuggles a scale back in.

Only the plain logarithm treats every doubling alike.

There is a second route to the same answer that never mentions distances. Ratios chain by multiplying: v over h equals
v over m times m over h, through any middle term m. A measure of ratios under which chained ratios *add* must be a
logarithm, by the same equation. The steady turn is not such a measure. That is why a bounded sweep gives its levels
unequal room, as section 7 will show.

This condition is a premise, and the essays say so. It is the requirement that no scale be preferred, motivated by the
fact that nothing in the readings fixes H. It is not derived.

---

## 4. Two address spaces, one corner

So the reader has two ways of laying out its places, and they meet at the corner.

- **Inside the corner, the addresses are proportional.** Each step out is the same distance.
- **Past the corner, they are logarithmic.** Each doubling gets the same number of places.

They join without a kink. There is only one such corner built into the relation: the one point the swap of the two
parties leaves fixed, where v equals h. Past it the levels are plain doublings laid side by side. They have no corners of
their own and nothing nested inside them.

### Reality in 2H

There is a second way to lay out the same far addresses, by length instead of by count. Place a far reading at a distance
of 2 minus h/v from home, in units of H. Then the first doubling past the corner, from H to 2H, takes up half of the next
H; the second doubling takes a quarter; the third an eighth. The whole far field, out to infinity, fits between H and
2H.

The reader holds the same addresses either way, the same number per doubling. Laid by count they run on forever; laid by
length they crowd toward a wall at 2H. A reader with finitely many places runs out of them at the end of its own range
in either case.

| drawing of the same addresses | measured by | bounded? | corner at |
|---|---|---|---|
| the fisheye, the turn itself | steps of turning | yes, a quarter turn | half the turn |
| the in-place lay | length | yes, out to 2H | H, halfway |
| the logarithmic lay | number of places | no | where the equal doublings start |

*Demos: levels (the reader's lay, and the in-place lay at* `?lay=inplace`*); H is a zoom.*

---

## 5. Why not proportion all the way out

A reader that kept the plain ratio v/h, in proportion, past the corner would pay five ways.

- **It could not lay out its range.** Its readings run to infinity, and no range fixed in advance would hold them.
- **It would divide by the smaller part.** Past the corner h is the smaller share, and a small wobble in it swings the
  reading without bound. Swapping to h/v divides by the larger part instead. Numerical computing follows the same rule:
  when solving equations it divides by the largest entry available, not the smallest.
- **Its averages would never settle.** That is the missing mean of the third essay.
- **It would have to crop.** A picture kept in proportion out to the horizon would be infinitely large. Ordinary
  rectilinear cameras are such readers, and they crop at about the corner. A fisheye lens holds the whole hemisphere by
  giving up proportion near its edge.
- **Its approximations would fail.** Series in powers of the reading break down past 1, as the second essay showed.

---

## 6. Three boundaries

A reader meets three different edges, and they are easily confused.

- **The corner,** where v equals h, lies between the two sides of the reading. Every reader finds it, whatever its
  length or its count of places.
- **The end of its range** is where its count of places runs out, well short of the horizon. A reader can reach it, as a
  floating-point number overflows when its exponent runs out.
- **The horizon** is the reading's own infinity, where h is zero and v/h has no end. No reader reaches it.

The horizon is not the vanishing point. A thing infinitely far straight ahead reads 0: it sits at zero, dead centre. The
reading's infinity lies at the sides, in what is nearest, at right angles to where you face.

---

## 7. Why halving

If a level has nothing but its two ends, their order and the swap between them, how can it be divided?

Only one interior point is special: the corner, the swap's fixed point. Any other point inside one half can be slid
anywhere else in that half by a change that keeps the order and commutes with the swap, so no other point is marked.
Divide at the corner, and apply the same argument to each half, and you get halvings, then quarters, then eighths. Three
parts, or any other number, need something added to the level, a measure it does not have. This is Felix Klein's
principle that a geometry supplies what its symmetries keep, applied to the points of a level.

Two halvings should be kept apart. Halving a length or a count, H to H/2, the doublings 2ᵏ, is rational, and a reader
with one length makes it. Placing the cut inside a doubling at its geometric middle, √2 inside the first, takes a square
root, two lengths combined, and that is the writer's (the fourteenth essay, "One variable, two, and the whole turn"). The argument above says which point a level's
symmetries mark; it does not make the reader the one who places it.

A reader can still match any other ratio. A reader whose resolution grows by a factor of three from level to level
matches levels of three exactly, as one with a factor of two matches doublings. But every ratio other than the halving
costs something carried in the reader. A layout with uneven levels costs more. A calendar's centuries, months, days,
hours, minutes and seconds match no single factor, and reading them needs a table of their sizes, which a reader given
nothing does not have. Uniformity can be free; variation has to be stored somewhere.

The halvings show up in the turn too. Read the turn against the logarithm, and each doubling past the corner gets less of
the quarter turn than the one before: 18.4°, then 12.5°, 6.9°, 3.5°, 1.8°, the step shrinking by a factor approaching
two. The turn is the logarithm seen whole from one side, squeezed into ninety degrees.

---

## 8. Two familiar instances

### Floating-point numbers

The numbers inside every computer lay their places exactly this way. A floating-point number has an exponent, which
counts levels, and a significand, which is a plain share within the level. Below the smallest normal number, a short
stretch called the subnormals is laid in proportion from zero. The count of levels plus the share within the current one
is the logarithm laid in straight pieces between level edges. It is exact at every edge and never more than 0.086 of a
level from the smooth logarithm. A float differs from the reader in having levels on both sides of 1 and a floor at the
bottom. The reader has proportion inside the corner and no floor.

### Mercator's map

Gerardus Mercator's map of 1569 is the oldest instance of the two address spaces laid out. On the globe at latitude φ,
the height above the equator is v = sin φ and the radius of the circle of latitude is h = cos φ, so v/h is tan φ.
Mercator stretched each circle of latitude out to the same width, and stretched the map vertically by the same amount
at each place, to keep shapes true. Summed from the equator, the height on the map comes out as a function of v/h alone.
Near the equator it is nearly v/h, in proportion. Past 45°, the corner, each doubling of v/h adds a height approaching
the natural logarithm of 2: 0.562, then 0.651, 0.682, 0.690, 0.692 for the doublings from 1 to 32. The pole is the
horizon, which is why the map is cut off short of it.

But Mercator's map is not a picture of what a reader sees, and the difference is worth stating carefully. The map is a
chart of the whole globe, drawn once to be read from anywhere on it. Past the corner it gives every level the same room.
It favours no place; it has no focus.

A reader looking out from a standpoint is laid the other way, on two counts.

- **Its picture is the turn.** Stand with your eye one height H above level ground. The ground at distance 2H appears
  26.6° below the horizon, at 4H 14.0°, at 8H 7.1°. Each doubling past the corner takes half the room of the last. The far
  field is in proportion to the reciprocal of distance, not in levels.
- **Its turn has a focus.** The turn's room per level is greatest at the corner and falls off alike toward home and
  toward the horizon. Turning your head carries the corner, and the most room, to whatever you look at.

Mercator's equal levels belong somewhere else in the reader's account: in distance laid by a count of places, where every
level is held alike because none is known beforehand to matter more. The map represents the field. The reader observes
from somewhere within it.

---

## 9. One figure, three rulers

The circle, the writer's number line and Mercator's height fit in one figure, and the figure shows what each does with
the corner.

Draw the unit circle, the straight line touching it at one point A, and the hyperbola that touches the same line at A. A
reading x sits on the straight line. The ray from the centre through it meets the circle at an angle θ, and the point of
the hyperbola level with it sits at a hyperbolic angle ζ. Then x is the tangent of θ and the hyperbolic sine of ζ.
Each angle is twice the area of its own sector, the circle's as Archimedes knew and the hyperbola's as Grégoire de
Saint-Vincent found in 1647. One reading, laid three ways:

| ruler | near field, x up to 1 | far field, x past 1 | room per level | the corner |
|---|---|---|---|---|
| x itself, the writer's number line | 1, in proportion | without end, in proportion | more each level than the last | a point |
| θ, the turn | 45° | 45° | most at the corner, falling alike on both sides | the middle |
| ζ, the hyperbolic angle, Mercator's height | about 0.881, nearly in proportion | without end, about ln 2 a doubling | rising to the same for every far level | a point where proportion gives way to levels |

All three carry the corner, because it is a point of the reading itself. Only the turn gives it a role. On the turn the
near and far fields are halves, mirror images under the swap, and a steady turn puts its median at the corner with nothing
else given. The two unbounded rulers have no even spread until someone fixes a range in advance, and then the range, an
amount, decides where the middle falls.

The hyperbolic angle is the reader's logarithmic lay made smooth. It is nearly x inside the corner and nearly the
logarithm of 2x past it. The lay of section 3, x then 1 plus the logarithm of x, never differs from it by more than
1 − ln 2, about 0.31.

*Demo: one sweep, three paths; what is H.*

---

## 10. The count is the level of detail

The forms of the two address spaces are fixed by the geometry: proportion, then doublings. Their *counts* are not. How
many places the near field is divided into, and how many each doubling gets, is the **level of detail**. The geometry
gives the forms. The level of detail gives the count.

A thing that spans n of the reader's places is resolved to about log₂ n levels of detail, one fewer each time it halves.
When it spans a single place it is a point. Nothing is requested: the span sets the level.

Two clarifications keep this honest.

- **The count is a resolution, not a set of boxes.** A thing between two places is not rounded to either. It is held at
  the coarser level, and the level is a continuous number whose fractional part says how far the finest detail has
  faded. Rounding to cells is a device of storage, not of reading. (The Cauchy carries such a level in its own height: seen
  from height γ, a pattern's ripple of frequency k is kept as e to the power −kγ, each finer ripple fading faster, none
  cut off.)
- **Holding is not telling apart.** Things that share a place arrive there as one payload. Only a finer count or another
  standpoint separates them.

The same idea appears in computer graphics. The hyperbolic browser of 1995 drew only nodes at least a pixel across.
Mipmaps halve an image at each level. Web map tiles add one digit to their key for every level of detail.

---

## 11. H is a zoom, not an escape

H is not a measured size. It is the value the reader starts from, and nothing in the geometry fixes it. Every H gives
the same circle and the same corner. So a reader could choose an enormous H and hold everything it will ever look at
inside the near field, in proportion, with no logarithm at all.

The cost is the level of detail. With a fixed number of places spread across an enormous H, everything at the reader's
own scale falls inside the first place and becomes a point. A small H holds the small at true scale and the large in
levels. A large H holds the large and loses the small. There is always something smaller than any H's first place, as
there is always something larger past any corner. No single H holds every scale at true scale.

So the best choice is to set H to the scale of the thing being read, which puts that thing at the corner. That is what
focusing an eye or zooming a lens does.

### What a larger H gives and takes

Count the room one object gets, the stretch from distance d to d + Δ.

- **Inside the corner,** it spans a number of places proportional to Δ/H. A larger H moves the corner further out and
  gives the proportional field more reach, but the count is fixed, so every object inside gets fewer places: one level
  of detail fewer for each doubling of H.
- **Past the corner, on the logarithmic lay,** its room depends only on where it is, not on H. A larger H only moves the
  held levels outward.
- **On the in-place lay,** a larger H gives the far more detail as well. The object gets the most room when H is the
  geometric mean of its two ends, the corner of the object itself.

The best H is the corner of what is read, as the best estimate of a size, when nothing says bigger or smaller, is the
corner of what is known.

*Demos: H is a zoom; what is H.*

---

## 12. A fixed count, aimed by H

Call the reader's whole count of places **K**: its fixed capacity to observe, the same whatever it looks at. K comes
before H. Choosing H does not change K; it splits it.

Lay the K places of a steady turn along distance. Their boundaries fall at H times the tangent of kπ/2K, for k from 1 to
K − 1. These are the Cauchy's quantiles with its scale at H.

- **The middle boundary is at H, whatever H is.** Half the places lie inside the corner and half past it, at every H. H
  moves the split; it never changes the count.
- **A small H gives the near half a short stretch,** each place fine, the first about πH/2K wide. A large H gives the
  same half a long stretch, each place coarser, and carries the far half further out.
- **The world's own count enters nowhere.** A world of N things, of 2N, or of infinitely many, is held at the same K
  places, each holding its share. That is the third essay's separation again: how many things there are is payload.

The reader works with K. The writer, who states every distance in amounts, works with N, placing each thing at its
amount on its number line. The Cauchy is what keeps the two apart. Its K quantiles are fixed by the turn alone, and its
last place runs out to the horizon, so a finite K covers an unbounded world.

*Demos: an infinite star field (N doubles and the reader's view does not change); browsing the stars.*

---

## 13. The corner follows the focus

Nothing in the geometry fixes where the reader puts its corner. Where should it?

On the turn's places, a cell's width relative to its distance is smallest at the corner and grows on both sides. So the
finest relative grain is at the corner, and a reader should put the corner on what it is looking at. "Near" and "far"
then mean nearer and farther than that thing.

Three reasons agree.

- **Grain.** The corner is where the cells are finest relative to their place.
- **Symmetry.** A choice of focus that does not care which party was divided by which must sit at the swap's one fixed
  point, the corner.
- **The next look.** Suppose the reader does not know where it will look next, only that it is as likely to be nearer
  as farther. The expected travel to the next look, measured on any increasing scale (angle, levels, length), is least at
  the median of where the next look falls. Not knowing which side is the same as a symmetric law, and its median is the
  corner.

If the next look is more likely on one side, the best focus moves toward that side, to the median of the lopsided law.
Under a turn weighted toward the near side by a factor 1 + a·cos 2θ, the best focus is 0.821 at a = 0.2 and 0.627 at
a = 0.5, a quarter of a level and two thirds of a level nearer than the corner.

The rest of the field is not lost. Every direction is still held, coarser away from the corner, which is enough to show
that something is there and where to look next. Moving the corner there is a new zero.

This says where a focus *should* go, and why. It is not a claim about what any eye does.

*Demos: the focus is the corner; the crosshair is the corner; friend or foe.*

---

## 14. What it comes to

The two unifying ideas of the series meet here in a practical form.

**Reading and writing.** The writer's ruler is the number line: proportion everywhere, no corner, every unit like every
other, which is what adding amounts needs. The reader's layout has a corner, set by its own length: proportion inside,
doublings past it, so that a finite count of places covers everything from the cup in its hand to the horizon. Neither
is better. They are made for different acts.

**The Cauchy.** The reader's K places, laid by a steady turn, fall at the Cauchy's quantiles with H as their scale. Half
inside the corner, half past it, whatever H is and however many things the world holds. The corner, where the law's
median sits, is also the finest grain and the best focus. A reader that points its corner at what it looks at uses its
fixed count where it matters, and still holds the rest of the field coarsely enough to know where to look next.

Go back to the fence posts. Near, you count the gaps. Far, you count the doublings. The corner sits at whatever post you
are looking at, and you can move it.

---

## Sources

- Cauchy, A.-L. (1821). *Cours d'analyse*. Paris. (The functional equation.)
- Saint-Vincent, G. de (1647). *Opus geometricum quadraturae circuli et sectionum coni*. Antwerp. (The hyperbola's area.)
- Mercator, G. (1569). *Nova et aucta orbis terrae descriptio*. Duisburg.
- Klein, F. (1872). *Vergleichende Betrachtungen über neuere geometrische Forschungen* (the Erlangen programme).
- Lamping, J., Rao, R. and Pirolli, P. (1995). A focus+context technique based on hyperbolic geometry for visualizing
  large hierarchies. *Proceedings of CHI '95*, 401–408.
- Williams, L. (1983). Pyramidal parametrics. *Computer Graphics (SIGGRAPH '83)* 17(3), 1–11.

The geometry is set out with proofs in *Observation from Somewhere*: the two address spaces in §6 (Proposition 4, the
in-place lay, why halving, floating point, Mercator's map, one figure and three rulers) and level of detail and the
choice of H in §8 (H is a zoom, a fixed count aimed by H, the corner follows the focus, Corollary 6.1).
