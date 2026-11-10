# Near and far

*The fourth of a series of essays on what can be known from where one stands. Draft, 28 October 2026.*

The first three essays built a reader with one length, its thumb pointed at the mountain and turned (the circle a writer
draws of it, the reader holding none), and a law, the Cauchy, for the directions that pointing gives. This essay asks a
practical question. A reader has only so many places to put things. How should it lay them out, near and far?

The answer has two parts, split at the corner. Near, in proportion. Far, by thumbs: two, then four, then eight. Between
them there is one point and no seam. The essay also asks where the corner should go, and answers that a reader should put
it on whatever it is looking at. That is what H, the reader's one length, is for (its thumb, held out at arm's length): not
a measurement, but a zoom.

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

The reader has one length, H: its thumb, held out at arm's length. Anything within that length can be laid out at its true
scale against it: a thing half a thumb away goes halfway out; a thing a quarter of a thumb away goes a quarter of the way.
This is the **near field**, one thumb laid evenly, in proportion. Inside it, the thumb is a ruler.

Proportion is exactly what the near field needs. Differences there are what matter: whether a cup is a hand's width or
two hand's widths away decides whether you can reach it. A ruler with equal marks is the right tool.

The trouble comes past H, past one thumb. A ruler with equal marks never ends. A reader that kept laying things out in
proportion beyond its own length would need room without limit.

---

## 3. Past the corner: what the far field has to be

So how should a reader lay out the things beyond H? Suppose it places a far thing, x times H away (x thumbs), at some
position on its layout, and that the position grows with x. What rule should the growth follow?

There is one natural condition. The reader's choice of H is free; nothing in its readings fixes it. A reader that chose H
twice as large, a thumb twice the size, would see every far amount as half as many thumbs away. If the layout gave a
stretch of distances more or less room depending on where that stretch happened to fall, then the room would depend on the
arbitrary choice of H. So the layout should give a stretch from x to λx the same room wherever it falls: room that depends
on the ratio λ alone, not on x.

That one condition decides the layout. Only one rule gives every stretch of the same ratio the same room: the logarithm.
One thumb to two gets the same number of places as four to eight, and every tenfold the same number again. The proof is a
classical functional equation, the one Cauchy solved in 1821: a function that turns products into sums, and grows, must be
a logarithm. And if the far layout is to join the near one without a kink at the corner, the logarithm has to start there
with the same slope: one plus the natural logarithm of x.

It is worth seeing why the obvious alternatives fail.

- **Proportion all the way out** gives the stretch from x to λx room proportional to x. Far stretches get more and more
  room, which is a preference for the far.
- **A power** of x does the same in a milder way.
- **A logarithm with a correction** gives room that depends on where you are, which smuggles a scale back in.

Only the plain logarithm treats one thumb to two, and four to eight, alike.

There is a second route to the same answer that never mentions distances. Ratios chain by multiplying: v over h equals v
over m times m over h, through any middle term m. A measure of ratios under which chained ratios *add* must be a logarithm,
by the same equation. The steady turn is not such a measure. That is why a bounded sweep gives the stretches from a count
of thumbs to twice it unequal room, as section 7 will show.

This condition is a premise, and the essays say so. It is the requirement that no scale be preferred, motivated by the
fact that nothing in the readings fixes H. It is not derived.

---

## 4. In proportion, then in ratios: one corner

So the reader reads distance in two ways, and they meet at the corner.

- **Inside the corner, distance is read in proportion.** Each step out is the same distance.
- **Past the corner, it is read in ratios.** Each stretch over which the reading halves, one in two to one in four, one
  in four to one in eight, holds the same share of the heat. A writer, laying the heat out as places, puts the same
  number in each, and counts these stretches in thumbs: one to two, two to four, four to eight.

They join without a kink. There is only one such corner built into the relation: the one point the swap of the two parties
leaves fixed, where v equals h. Past it the far field is plain stretches laid side by side, the reading halving across
each. They have no corners of their own and nothing nested inside them.

**The crosshairs.** Picture H as a thumb held out at arm's length; in space, two thumbs crossed at a right angle across the
line of sight, one reading up and one across, both the same H (the fifth essay). Where they cross is the corner: the thing
there reads one thumb up for one thumb along, v equal to h, and it is drawn one thumb wide. That crossing, with H, lays
the near field and the far field over the read; the Cauchy of directions has neither (the fifth essay, section 10). The near field is a single thumb, laid evenly: everything nearer than the crossing is read
in proportion. The far field is read in ratios: a thing one thumb wide reads one in two, then one in four, then one in
eight, each stretch with as much of the heat as the one before, out toward the horizon. Counted across, as places, the same stretches
are two thumbs, four, eight.

For the crosshair to be the corner of every pair at once, the look has to run down the diagonal of three thumbs,
horizontal, vertical and depth, the thing pointed at one thumb along each and √3 thumbs along the line of sight; round it a
circle one thumb wide in space, 35° on the screen, runs from the corner out to home, the readings squeezing toward home as
they go (the fifth essay, "Three thumbs at the crosshair").

Laid by distance address (K places along distance, a writer's layout of the reader's heat), a view shows the far field
as the reader holds it: a point on the ground ρ away goes on the row
(2/π)·atan(D/ρ), D the thumb's own ground distance, so that the thumb sits at ½ and the bands one in 2, 4 and 8 pack ever
thinner under the horizon. The world is never counted for it: drawn only where the view reaches and culled to what spans one
of those places, it needs K and no N (the fifth essay, "Laid by the heat").

### Reality in 2H

There is a second way to lay out the same far field, by length instead of by count. Place a far reading at a distance
of 2 minus h/v from home, in units of H, in thumbs. Then the stretch past the corner from one thumb to two (H to 2H) takes
up half of the next thumb; from two to four takes a quarter; from four to eight an eighth. The whole far field, out to
infinity, fits between one thumb and two, H and 2H.

The reader holds the same heat either way, the same share over each stretch where the reading halves. Laid by count it
runs on forever; laid by length it crowds toward a wall at 2H. A reader of finite fineness K runs out of what it can tell
apart at the end of its own range in either case.

| drawing of the same heat | measured by | bounded? | corner at |
|---|---|---|---|
| the fisheye, the turn itself | steps of turning | yes, a quarter turn | half the turn |
| the in-place lay | length | yes, out to 2H | H, halfway |
| the logarithmic lay | number of places | no | at one thumb, where the equal stretches start |

### The near-field sphere, the writer's account

A writer watching the reader choose its thumb can say what was set in one more way. Every facing joined with every other
party at the one length, V = V₂ = H, fills a ball one thumb in radius about the eye: setting H sets that ball, the
near-field sphere. One facing of it is the wedge with its cap at H; the far field is everything outside it, and near and
far together are the writer's whole. Inversion in that sphere, d ↦ H²/d, carries the far field point for point onto the
near field, infinity onto the eye: the swap of d/H for H/d, which leaves one thumb where it is, drawn in space, and
why each field holds half of every direction's heat. The sphere is not filled evenly. Along each ray its filling is the reader's heat in distance, the
half-Cauchy 2H/(π(H² + d²)), hottest at the eye and half of it passed at one thumb; across directions it cools as cos³ of
the angle off the look. So the near-field sphere is the writer's outline round the reader's Cauchy. The reader itself holds
no sphere: it has a split on every direction it reads, one thumb out, and nothing round.

*Demos: levels (the reader's lay, and the in-place lay at* `?lay=inplace`*); H is a zoom; crosshairs in a field (by distance address).*

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

If a stretch, from one thumb to two say, has nothing but its two ends, their order and the swap between them, how can it be
divided?

Only one interior point is special: the corner, the swap's fixed point. Any other point inside one half can be slid
anywhere else in that half by a change that keeps the order and commutes with the swap, so no other point is marked.
Divide at the corner, and apply the same argument to each half, and you get halvings, then quarters, then eighths. Three
parts, or any other number, need something added to the stretch, a measure it does not have. This is Felix Klein's
principle that a geometry supplies what its symmetries keep, applied to the points of a stretch.

Two halvings should be kept apart. Halving a length or a count, a thumb to half a thumb (H to H/2), the counts 2ᵏ of
thumbs, is rational, and a reader with one length makes it. Placing the cut inside a stretch at its geometric middle, √2
thumbs inside the one from one thumb to two, takes a square root, two lengths combined, and that is the writer's (the
fourteenth essay, "One variable, two, and the whole turn"). The argument above says which point a stretch's symmetries
mark; it does not make the reader the one who places it.

A reader can still match any other ratio. A reader whose resolution grows by a factor of three from stretch to stretch
matches one thumb to three, three to nine, exactly, as one with a factor of two matches two thumbs, four, eight. But every
ratio other than the halving costs something carried in the reader. A layout with uneven stretches costs more. A calendar's
centuries, months, days, hours, minutes and seconds match no single factor, and reading them needs a table of their sizes,
which a reader given nothing does not have. Uniformity can be free; variation has to be stored somewhere.

The halvings show up in the turn too. Read the turn against the logarithm, and each stretch past the corner, one thumb to
two, two to four, gets less of the quarter turn than the one before: 18.4°, then 12.5°, 6.9°, 3.5°, 1.8°, the step
shrinking by a factor approaching two. The turn is the logarithm seen whole from one side, squeezed into ninety degrees.

---

## 8. Two familiar instances

### Floating-point numbers

The numbers inside every computer lay their places exactly this way. A floating-point number has an exponent, which counts
powers of two, and a significand, which is a plain share between one power of two and the next. Below the smallest normal
number, a short stretch called the subnormals is laid in proportion from zero. The count of powers of two plus the share
toward the next is the logarithm laid in straight pieces between powers of two. It is exact at every power of two and never
more than 0.086 of the way to the next from the smooth logarithm. A float differs from the reader in counting powers of two
on both sides of 1 and in having a floor at the bottom. The reader has proportion inside the corner and no floor.

### Mercator's map

Gerardus Mercator's map of 1569 is the oldest instance of the near field's proportion and the far field's ratios laid out
together. On the globe at latitude φ, the
height above the equator is v = sin φ and the radius of the circle of latitude is h = cos φ, so v/h is tan φ. Mercator
stretched each circle of latitude out to the same width, and stretched the map vertically by the same amount at each place,
to keep shapes true. Summed from the equator, the height on the map comes out as a function of v/h alone. Near the equator
it is nearly v/h, in proportion. Past 45°, the corner, each time v/h grows to twice what it was adds a height approaching
the natural logarithm of 2: 0.562, then 0.651, 0.682, 0.690, 0.692 from 1 to 2, 2 to 4, and so on to 32. The pole is the
horizon, which is why the map is cut off short of it.

But Mercator's map is not a picture of what a reader sees, and the difference is worth stating carefully. The map is a
chart of the whole globe, drawn once to be read from anywhere on it. Past the corner it gives every stretch from a value of
v/h to twice it the same room. It favours no place; it has no focus.

A reader looking out from a standpoint is laid the other way, on two counts.

- **Its picture is the turn.** Stand with your eye one height H above level ground. The ground at distance 2H appears 26.6°
  below the horizon, at 4H 14.0°, at 8H 7.1°. Each stretch past the corner, one thumb to two, two to four, takes half the
  room of the last. The far field is in proportion to the reciprocal of distance, not to its logarithm.
- **Its turn has a focus.** The turn's room over each stretch where the reading halves is greatest at the corner and falls off
  alike toward home and toward the horizon. Turning your head carries the corner, and the most room, to whatever you look
  at.

Mercator's equal stretches belong somewhere else in the reader's account: in distance laid by a count of places, where
every stretch where the reading halves is held alike because none is known beforehand to matter more. The map
represents the field. The reader observes from somewhere within it.

---

## 9. One figure, three rulers

The circle, the writer's number line and Mercator's height fit in one figure, and the figure shows what each does with
the corner.

Draw the unit circle, the straight line touching it at one point A, and the hyperbola that touches the same line at A. A
reading x sits on the straight line. The ray from the centre through it meets the circle at an angle θ, and the point of
the hyperbola level with it sits at a hyperbolic angle ζ. Then x is the tangent of θ and the hyperbolic sine of ζ.
Each angle is twice the area of its own sector, the circle's as Archimedes knew and the hyperbola's as Grégoire de
Saint-Vincent found in 1647. One reading, laid three ways:

| ruler | near field, x up to 1 | far field, x past 1 | room from x to 2x | the corner |
|---|---|---|---|---|
| x itself, the writer's number line | 1, in proportion | without end, in proportion | more each stretch than the last | a point |
| θ, the turn | 45° | 45° | most at the corner, falling alike on both sides | the middle |
| ζ, the hyperbolic angle, Mercator's height | about 0.881, nearly in proportion | without end, about ln 2 from any x to 2x | rising to the same for every far stretch | a point where proportion gives way to the logarithm |

All three carry the corner, because it is a point of the reading itself. Only the turn gives it a role. On the turn the
near and far fields are halves, mirror images under the swap, and a steady turn puts its median at the corner with nothing
else given. The two unbounded rulers have no even spread until someone fixes a range in advance, and then the range, an
amount, decides where the middle falls.

The hyperbolic angle is the writer's smooth formula for the reader's lay of ratios. It is nearly x inside the corner and nearly the
logarithm of 2x past it. The lay of section 3, x then 1 plus the logarithm of x, never differs from it by more than
1 − ln 2, about 0.31.

**The same figure in distance.** The thumb's own lay of distance, (2/π)·arctan(d/H), is the turn ruler applied to d/H,
and written against the ratio x = ln(d/H) it is ½ + gd(x)/π, gd the function Mercator's chart is built on. So distance
laid by the thumb is a turn, bounded, with its corner at one thumb. A writer can draw the reason. Wrap the plane onto a
sphere so that one thumb lands on its equator: the eye is one pole and the horizon the other, the near field is the half
on the eye's side and the far field the half on the horizon's, and the swap of d for H²/d is the reflection in the
equator. The thumb's lay is then the sphere's latitude drawn evenly; the reader's ratios of thumbs, the logarithm, are
the same sphere's Mercator chart, where each stretch of the far field takes the same room. The K places a writer counts
along distance, H·tan(kπ/2K), are the meridian cut into equal steps, half of them in each half of the sphere. Making the
thumb larger slides every latitude toward the eye: a boost along the sphere's axis, the moving sky of the seventh essay
done to distance. The sphere is the writer's drawing; the reader has the lay.

*Demo: one sweep, three paths; what is H; Euler's plane.*

---

## 10. The count is the detail

The forms of the near and far fields are fixed by the geometry: proportion, then ratios, one in two, one in four, one in
eight (as places, two thumbs, four, eight). Their *counts* are not. How many places the near field is divided into, and how
many each stretch where the reading halves gets, is the **detail**, how finely things are drawn. The geometry gives the forms. The detail gives the count. The reader reads that
fineness, K, continuously; laid out as K places it is a writer's count, K addresses.

A thing that spans n of the reader's places can be halved about log₂ n times before its halves are single places, one fewer
each time it halves. When it spans a single place it is a point. Nothing is requested: the span sets how finely it is
drawn.

Two clarifications keep this honest.

- **The count is a resolution, not a set of boxes.** A thing between two places is not rounded to either. It is held at the
  coarser grain, and the grain is a continuous number whose fractional part says how far the finest detail has faded.
  Rounding to cells is a device of storage, not of reading. (The Cauchy carries such a grain in its own height: seen from
  height γ, a pattern's ripple of frequency k is kept as e to the power −kγ, each finer ripple fading faster, none cut
  off.)
- **Holding is not telling apart.** Things that share a place arrive there as one payload. Only a finer count or another
  standpoint separates them.

The same idea appears in computer graphics. The hyperbolic browser of 1995 drew only nodes at least a pixel across. Mipmaps
halve an image again and again. Web map tiles add one digit to their key each time a tile is halved.

---

## 11. H is a zoom, not an escape

H, the thumb, is not a measured size. It is the value the reader starts from, a thumb of any size, and nothing in the
geometry fixes it. Every H gives the same geometry and the same corner. So a reader could choose an enormous H and hold
everything it will ever look at inside the near field, in proportion, with no logarithm at all.

The cost is detail. With a fixed number of places spread across an enormous H, everything at the reader's own scale falls
inside the first place and becomes a point. A small H, a small thumb, holds the small at true scale and the large by thumbs
counted two, four, eight. A large H, a big thumb, holds the large and loses the small. There is always something smaller
than any H's first place, as there is always something larger past any corner. No single H holds every scale at true scale.

So the best choice is to set H to the scale of the thing being read, which puts that thing at the corner, one thumb wide.
That is what focusing an eye or zooming a lens does.

### What a larger H gives and takes

Count the room one object gets, the stretch from distance d to d + Δ.

- **Inside the corner,** it spans a number of places proportional to Δ/H. A larger H, a bigger thumb, moves the corner
  further out and gives the proportional field more reach, but the count is fixed, so every object inside gets fewer
  places: one halving of detail fewer each time H, the thumb, is made twice as big.
- **Past the corner, on the logarithmic lay,** its room depends only on where it is, not on H. A larger H only moves the
  held range outward: as many places from one thumb to two, wherever the thumb is.
- **On the in-place lay,** a larger H gives the far more detail as well. The object gets the most room when H is the
  geometric mean of its two ends, the corner of the object itself.

The best H is the corner of what is read, as the best estimate of a size, when nothing says bigger or smaller, is the
corner of what is known.

### Dragging the thumb

What moves when H moves? Not the read. The directions never held H: a reading is a ratio of the thumb's own shares, and the
Cauchy over them is the same at every H. What H moves is distance, and with it the overlay's heat in distance, (1/π)·sech(ln(d/H)), half nearer than the thumb and
half past it at every H. Counted by a writer as K places, K addresses, it sits at H·tan(kπ/2K); laid as the reader lays
it, each share the same room and the corner in the middle, it does not move at all. Drag the thumb out and the things in
the world slide through that fixed heat, more of them into the near field, each with less room; drag it in and they slide
out past the corner, the near ones held finer. The heat stays; the world slides through it, its paint met wherever it
lands. *The heat is given; the paint is met.* Nothing is written: no amount is carried in, only which things land
where changes. Near and far, then, are an overlay the thumb lays over the read, a split on every direction one thumb out,
not part of the read's Cauchy, and not a shape.

A cube of dots makes the split concrete. Twelve dots a side, seen from a corner and looking at the middle, put 436 dots
nearer than one thumb and 1,291 farther; the writer's even spacing puts more of the box far off. Laid as the read lays
distance, the dot looked at sits in the middle, and each field has half the room. The count belongs to the writer; the
room to the read. Look at another dot and the split goes with it; scale the box and nothing changes colour.

*Demos: H is a zoom; what is H; the read (drag the thumb); a cube of heat.*

---

## 12. A fixed count, aimed by H

Call the reader's whole count of places **K**: its fixed capacity to observe, the same whatever it looks at. K comes before
H. Choosing H, the size of the thumb, does not change K; it splits it.

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
- **The next look.** Suppose the reader does not know where it will look next, only that it is as likely to be nearer as
  farther. The expected travel to the next look, measured on any increasing scale (angle, the logarithm, length), is least
  at the median of where the next look falls. Not knowing which side is the same as a symmetric law, and its median is the
  corner.

If the next look is more likely on one side, the best focus moves toward that side, to the median of the lopsided law.
Under a turn weighted toward the near side by a factor 1 + a·cos 2θ, with the corner at one thumb, the best focus is 0.821
of a thumb away at a = 0.2 and 0.627 at a = 0.5.

The rest of the field is not lost. Every direction is still held, coarser away from the corner, which is enough to show
that something is there and where to look next. Moving the corner there is a new zero.

This says where a focus *should* go, and why. It is not a claim about what any eye does.

So a reader separates the near field from the far field by looking around at things: whatever the crossed thumbs point at
is taken as H, half of every direction's heat in distance nearer than it and half farther, and looking at something else moves
the split there. Parallax gives one more reason to think it should. A thing at the corner is a thing at parallax's corner:
a step of two thumbs, half the baseline equal to the distance, places it with the least error, ε·cosh(ln k) at its least,
just ε (the sixth essay). The finest grain and the best baseline fall on the same thing, the one looked at. Counted per
stretch, the split is a heat map in distance, (1/π)·sech(ln(d/H)), hottest at the thing looked at and cooling alike nearer
and farther (the fifth essay, section 10).

Lay the whole read out along the look and it runs: the eye; the near field, distance in proportion, half the heat; the
thing looked at, one thumb out, the corner, where the heat is greatest; the far field, distance in ratios, the other half
of the heat, without end; the horizon. The near field is not hotter than the far. They are equal halves of one heat,
split at the thing the reader chose to look at.

The same holds when the thing read is a shape. Epicycles draw an outline from one standpoint at the centre; terms read from
standpoints stepped toward a dent draw it in about an eighth as many, and every one of them stands at the dent (the tenth essay,
§3).

*Demos: the focus is the corner; the crosshair is the corner; friend or foe; circles and standpoints.*

**In physics.** The inverse square is near and far in physics. Along each direction a source covers its paint is the
same at every distance; distance changes how many directions it covers, so the law lives in the count, never in the
paint. A disc's light turns from the near field's flat to the far field's inverse square exactly where the distance
equals the radius, symmetrically about it, σ(s) + σ(1/s) = −2, but only when the light counted is a share of directions;
counted as an angle, the switch moves off the corner. On real stars one kind falls in light as d^(−2.02), while counts
by light, needing no distance, grow as S^(−1.23) (*Reads and Writes in Physics* (`../reads-and-writes-physics.md`), §6).

---

## 14. What it comes to

The two unifying ideas of the series meet here in a practical form.

**Reading and writing.** The writer's ruler is the number line: proportion everywhere, no corner, every unit like every
other, which is what adding amounts needs. The reader's layout has a corner, set by its own length, its thumb: proportion
inside, one thumb laid evenly, and past it ratios, one in two, one in four, one in eight, so that a finite count of places covers
everything from the cup in its hand to the horizon. Neither is better. They are made for different acts.

**The Cauchy.** The reader's K places, laid by a steady turn, fall at the Cauchy's quantiles with H as their scale. Half
inside the corner, half past it, whatever H is and however many things the world holds. The corner, where the law's
median sits, is also the finest grain and the best focus. A reader that points its corner at what it looks at uses its
fixed count where it matters, and still holds the rest of the field coarsely enough to know where to look next.

Go back to the fence posts. Near, you count the gaps. Far, you count thumbs: two, four, eight. The corner sits at whatever
post you are looking at, and you can move it.

---

## Sources

- Cauchy, A.-L. (1821). *Cours d'analyse*. Paris. (The functional equation.)
- Saint-Vincent, G. de (1647). *Opus geometricum quadraturae circuli et sectionum coni*. Antwerp. (The hyperbola's area.)
- Mercator, G. (1569). *Nova et aucta orbis terrae descriptio*. Duisburg.
- Klein, F. (1872). *Vergleichende Betrachtungen über neuere geometrische Forschungen* (the Erlangen programme).
- Lamping, J., Rao, R. and Pirolli, P. (1995). A focus+context technique based on hyperbolic geometry for visualizing
  large hierarchies. *Proceedings of CHI '95*, 401–408.
- Williams, L. (1983). Pyramidal parametrics. *Computer Graphics (SIGGRAPH '83)* 17(3), 1–11.

The geometry is set out with proofs in *Observation from Somewhere* (archived since 30 October and kept for its proofs; the current account is *Reads and Writes*, rewritten on 10 November (R788) with read, place and write): the proportional and logarithmic lays in §6 (Proposition 4, the
in-place lay, why halving, floating point, Mercator's map, one figure and three rulers) and detail and the
choice of H in §8 (H is a zoom, a fixed count aimed by H, the corner follows the focus, Corollary 6.1).
