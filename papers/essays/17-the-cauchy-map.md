# The Cauchy map: heat given, paint met

*The seventeenth of a series of essays on what can be known from where one stands. Draft, 5 November 2026. It gathers the
rulings of 5 November (R700–R707) on the read as a hemisphere, the Cauchy as a heat map, near and far as an overlay, and
addresses as the writer's word, and follows* Reads and Writes *§7, "A heat map: the Cauchy's and the overlay's" and "Where
the heat comes from".*

Take any photograph with a wide lens and look at its corners. They are darker than the middle, even of a white wall evenly
lit. Photographers call it natural vignetting and give it a law: the light falls off as the fourth power of the cosine of
the angle off the lens's axis. At 30° off the axis the corner gets 0.56 of the middle's light; at 45°, a quarter, two stops.
No lens maker put it there and none can take it out entirely. It is geometry.

Three of those four cosines are the subject of this essay. They are not about light at all. They are about how the
directions from one point spread over a flat surface held in front of it, and they are there before a single photon
arrives. A camera's sensor is a flat screen; the directions it collects are spread evenly over the half of the sky in
front of it; and directions spread evenly by angle land on a flat screen crowded at the middle and thinning toward the
edge, as cos³ of the angle off the middle. The fourth cosine is the light's own: the aperture seen at a slant. Take the
light away and the three remain, a map of where the looking is.

That map is the Cauchy. This essay is about reading it as a map.

The order: the map (§1), where it comes from (§2), what it is not (§3), the same map as a random walk (§4), stepping back
(§5), moving the map (§6), the second map, in distance (§7), a middle and no centre of mass (§8), addresses as the
writer's word (§9), who saw which piece (§10), and what it changes (§11).

## 1. A map of where the looking is

Stand anywhere and look. Everything in front of you, out to the edge of what you can see, is a hemisphere of directions:
straight ahead in its middle, the horizon of the look its rim, 90° off on every side. Nothing about that hemisphere favours
one direction over another. The turn that carries the look from one direction to the next treats them all alike; measured
by itself it is uniform (essay 2).

Now hold a sheet of glass one thumb in front of you, square to the look, and mark where each direction crosses it. A
direction α off the look crosses at r = tan α thumbs from the middle. The directions that were even on the hemisphere are
not even on the glass. Near the middle they crowd; out toward the edge of the glass they thin, and the rim of the
hemisphere never lands on the glass at all, however large it is.

Count them in a small patch of the glass and you have a number per patch: how much of the looking passes through there.
Lay those numbers over the glass and you have a heat map. It is hottest where the look points, cools steadily off it, and
reaches nothing at the rim: 0.35 of the peak one thumb off the middle (45°), 0.125 at 60°, half the hemisphere inside
that 60°. That heat map is the two-dimensional Cauchy,

  1/(2π(1 + r²)^(3/2)) per unit of glass, falling as cos³α.

In the plane, with one thumb instead of two crossed, the same construction gives the familiar Cauchy, (2/π)/(1 + s²) per
unit of the reading s = v/h, falling as cos²θ.

Three things are worth saying about this map at once.

It is continuous. There is no grain in it, no smallest cell, nothing counted. It is a weight over the readings, defined
at every reading.

It is given. Nothing has arrived yet. The map is the same in a desert and a cathedral, in fog and in sunlight, near a wall
or under the open sky. It belongs to the standpoint and the turn, not to the world (*Reads and Writes* §2, "Heat and
paint").

It moves with the look. Turn and the map turns with you: whatever you look at sits at its hottest point. A reader's
fidelity is greatest wherever it looks, because the map is centred wherever it looks (R624).

What arrives along each direction is something else: the colour, the light, the paint. The world decides it, and it
changes when the world changes. The paint lands on the map; it does not move it. In a line: *the heat is given; the paint
is met.*

## 2. Where the heat comes from

The derivation is short and classical, and it is worth having in front of you, because everything else rests on it.

Start with the measure that treats every direction alike: uniform by angle in the plane, uniform by solid angle in space.
That is the turn's own measure, the one the hand sweeps with no clock and no ruler (essays 2 and 14). It has no heat: on
the hemisphere, by angle, every direction weighs the same.

The heat appears when the directions are read in a coordinate. In the plane, a direction θ off home reads s = v/h = tan θ,
and

  dθ = ds/(1 + s²) = cos²θ · ds.

So an even spread of θ, read in s, has weight proportional to 1/(1 + s²): over a quarter turn, (2/π)/(1 + s²), the
half-Cauchy, its median at the corner s = 1, its quartiles at √2 − 1 and √2 + 1.

In space, a small patch dA of the glass at r = tan α subtends a solid angle

  dΩ = cos³α · dA,

one cosine because the patch is tilted to the ray, two because it is sec α away and solid angle falls with distance
squared. So an even spread over the hemisphere, (1/2π) per unit of solid angle, read on the glass, has weight
(1/2π)·cos³α = 1/(2π(1 + r²)^(3/2)). With n thumbs square to the look, the same count gives cos^(n+1): one cosine more for
each thumb.

The photographer's cos⁴ is this cos³ and one more for the aperture, which a ray reaching the corner of the frame sees
foreshortened. The three geometric cosines would be there for a pinhole with no light at all; they are where the looking
is.

## 3. What it is not

There is an easy way to get this backward, and it is worth getting it wrong once on purpose.

Suppose the world in front of you is a wall of tiles, evenly spaced: a Cartesian grid, a writer's grid, so many tiles a
metre. Is the Cauchy the way that grid looks from where you stand?

No. Tiles on a wall d away sit at y = d·s, so in the reading s they are spaced evenly; on the glass they are flat. Per unit
of angle they are not flat: they crowd toward the horizon, as sec²θ in the plane and sec³α on a wall in space, because a
small turn near the horizon sweeps across many tiles. Nothing about the tiles is hottest along the look.

The Cauchy is the other way round: the even turn laid on that flat grid,

  dθ/ds = 1/(1 + s²),  dΩ/dA = cos³α,

the turn per unit of the writer's grid. It is a rate, the *per* of essay 14: how much of the looking per tile. The tiles
are the writer's; the turn is the reader's; the Cauchy is how one sits on the other. It is not the layout of the world.

## 4. The same map, from a walker

Here is a second way to the same map, from somewhere that seems to have nothing to do with looking.

Stand at your point, d from a straight wall, and let a random walker start from where you stand: a step in a random
direction, then another, then another, in the plane. Sooner or later it hits the wall. Where? The landings pile up near the
foot of the perpendicular and thin out along the wall, and their law is

  (1/π) · d/(d² + y²),

the Cauchy again, with its scale the distance d. This is harmonic measure: the law of where a walker from a point first
meets a boundary (Kakutani 1944; Doyle and Snell 1984). It is also the Poisson kernel of the half-plane, the weight with
which a steady temperature on the wall is felt at your point.

That the walker and the look give the same map is not a coincidence, and it is not special to the plane. On a flat wall in
any number of dimensions, the half-space's Poisson kernel is

  Γ(n/2)/π^(n/2) · d/|x|^n,

and the even hemisphere carried onto the wall is (2/|S^(n−1)|) · d/|x|^n. The two constants are equal for every n; checked
for n = 2 to 5. In space it is (1/2π) · d/(d² + r²)^(3/2): the cos³α of §2. In the language of measure theory, the Cauchy
is the Radon–Nikodym derivative of the turn's measure, carried onto the wall by the projection from home, against the
wall's own measure.

Two cautions keep this honest.

The walker's map is Laplace's: a steady state, with no time in it. It is not the heat equation, whose kernel is the
Gaussian, e^(−tk²) in frequency; mixing them up would bring the Gaussian back where it does not belong. The "heat" of the
heat map is a weight over the readings, not diffusion in time.

And on a sphere the two part. Seen from inside a ball, the walker's landings and the turn's directions carried through a
boost are different laws; in the run behind essay 13 the boosted sky never came within half a percent of the peak of any harmonic measure, and
at ρ = ½ the nearest was 3.84% off. The plane is special, and a
flat wall is the plane's gift in every dimension: there the look and the walk agree.

## 5. Stepping back

What happens to the map as you step back from the wall?

Its scale grows with your distance: at d the Cauchy has half-width d. And stepping back composes. If the wall is seen
from d₁ and that view is seen again from d₂ further back, the result is the view from d₁ + d₂. In frequency each view
multiplies by e^(−d|k|), and the exponents add:

  e^(−d₁|k|) · e^(−d₂|k|) = e^(−(d₁ + d₂)|k|).

This is the Poisson semigroup, and it is the cleanest level of detail there is. Every pattern on the wall survives the
step back, damped and never destroyed: the fine ones fade first, the broad ones last, and none is ever zero (*Reads and
Writes* §2, "The payload is not lost"). A floor, a box blur, cuts some patterns to zero and they are gone; the Cauchy only
dims them.

It is also why a sum of Cauchys is a Cauchy: a relay of standpoints, each one height above the last, lands as one turn from
the total height (the SUM run). The heights add, and the map stays a map of directions.

And it is how the epicycles of essay 4 and the demo `epicycles.html` blur: seen from a height γ, circle k of an outline
shrinks by e^(−γ|k|), and no circle moves.

## 6. Moving the map

Move the standpoint and the map moves with it, as a family. A change of standpoint, or of the chart a reading is written
in, is a real Möbius map of the reading, and the Cauchy is carried into another Cauchy: its centre the foot of the new
standpoint, its width the new height, together the point m + iγ (McCullagh 1996). The map does not break; it slides and
stretches, and the new map is again a map of where some standpoint is looking.

Special relativity does this to the sky. An observer moving at speed sees every star's direction crowd forward,
aberration, a Möbius map of the directions; a sky even in its own frame becomes the spherical Cauchy, its heat
proportional to D², D the Doppler factor (Kato and McCullagh 2020). The familiar D⁴ brightening ahead is that D² of heat,
the directions crowding, times D² of payload, each photon's energy and rate. The heat moves; the paint is reweighted;
they multiply.

What breaks the family is an amount entering: an edge (the map cut off at a finite wall), a square, a sum of amounts. The
map's tails go last: they are the horizon, and only an edge or a power takes them.

## 7. The second map, in distance

The Cauchy map has a middle, the look, and no near or far. No length enters it. Near and far are a second map laid over
the first, and it takes one length, H, the thumb held out (*Reads and Writes* §6, §7).

Along every direction, the thumb marks one distance: the thing it is pointed at, one thumb's worth out. Nearer than that
is the near field, held in proportion; past it is the far field, read in ratios, a thing one in two, one in four, one in
eight. Read by ratio, per unit of ln(d/H), the weight of the distances is

  (1/π) · sech(ln(d/H)),

hottest at one thumb and cooling alike both ways: 0.8 of the peak at one in two and at two thumbs, 0.47 at one in four
and four, 0.25 at one in eight and eight. It never reaches zero, and it is the same law as the first map, the half-Cauchy,
read along distance instead of across directions.

Multiply the two maps and the result is hottest at one point: on the look, one thumb out, the thing looked at. They meet
there only because the look points at it. Look at something else and both go with it.

That is why a reader should put what it looks at on the corner (R701). The corner is where its reading is finest relative
to its place, and the thing there is at parallax's corner too: a step of two thumbs places it with the least error,
ε·cosh(ln k) at its least, ε (essay 6). Whether readers do this is a question about readers. That they should is a
question about the map.

## 8. A middle and no centre of mass

A heat map has a hottest point. The Cauchy map has a middle, too: half its weight inside 60° of the look on the
hemisphere, half inside the corner s = 1 in the plane. These are medians, and they are the same however the readings are
written down, because a median commutes with every increasing change of chart.

What the map does not have is a centre of mass along the reading. Average the readings v/h over a quarter turn and the
average climbs without end, (2/π)·ln 10 for every tenfold further the readings run. This is usually told as a defect of
the Cauchy. Read as a map of directions it is what such a map should do: a direction has no length to add (essay 3). The
average belongs to the chart that took a direction for an amount; the map never had one.

The paint does. Light adds; colours average; the payload has every mean it ought to have. *What arrives can be averaged;
where it arrives cannot.*

## 9. Addresses, the writer's word

The essays used to call the reader's directions its *addresses*. That word is discrete: an address is a place in a
layout, counted, one of so many, the thing a computer looks up in memory. A writer can lay out such places on the map: K
of them at its quantiles, each holding an equal share of the heat; along distance, at H·tan(kπ/2K), half inside the thumb
and half past it at every H. Those are good tools, and essays 8, 12 and 16 use them. But they are the writer's sampling of
the map, not the map. The reader counts nothing. Its fineness, K, is read continuously; laid out as K places, it is a
writer's count (R706).

As a metaphor, the word still serves where it connects the Cauchy to computing (R707). A direction looked along is like an
address looked up: fixed before anything is stored there, unmoved by what is written there, reached in one step. The
difference is that memory's addresses and values are the same kind of thing, bits in a layout of N slots, while the
reader's direction and its paint never were: pointing is already being met (essay 16, "The projection is the
dereference"). Keep the metaphor and remember the heat under the address.

## 10. Who saw which piece

None of the mathematics is new.

The density itself is Poisson's and Cauchy's (Stigler 1974). The cos³ and cos⁴ of a flat screen are the optics of every
camera. Harmonic measure as the walker's landing is Kakutani's (1944), told for networks by Doyle and Snell (1984). The
Möbius closure of the family is McCullagh's (1996), and its spherical form under a boost Kato and McCullagh's (2020). The
choice of the even turn as the measure that treats every direction alike is Jaynes's method of transformation groups
(1968). The Takenaka–Malmquist terms that stand off the centre toward the detail are Qian and Wang's adaptive Fourier
decomposition (2011).

What the essays add is a division of it. The density is a map of where a standpoint is looking: given before anything
arrives, centred wherever it looks, continuous, and not the law of anything measured. What lands on it is the world's
writing, met there. The map has a middle and no mean; near and far are a second map laid on it by a length; and the
places a computer counts on it are a writer's sampling, useful and not the thing itself.

## 11. What it changes

It changes where to look for the Cauchy. If the Cauchy is a map of looking, then wherever it turns up there should be a
standpoint and a turn behind it: a lamp turning over a shore, a phase turning over a resonance, a walker leaving a point.
Find the turn, and the amounts are the paint. Where no turn can be found, the reading does not apply, and that is the test
that could fail.

It changes what to expect of an average. The map's middle is a median, and the median is the statistic that survives
every change of chart. Practice already takes the median of a Cauchy and never its mean; the map says why.

It changes what a camera's corners mean. The darkening at the edge of a photograph is not mostly a fault of the glass;
three of its four cosines are the map showing through.

And it changes the word. A reader has no addresses. It has a map, given whole wherever it looks, and the world's paint
landing on it. *The heat is given; the paint is met.*

**Demos.** `read.html` (the read with no world: the hemisphere in front, the 3D Cauchy as a hill, painted by both maps),
`crosshairs.html` (the map in a field of things: the tunnel, equal area, the overlay's rings), `pinhole.html` with
`?sky=1` (a uniform sky on a flat screen, cos³α), `central-reader.html` (harmonic measure from a point inside a circle),
`plane-sphere.html` (the plane's one law and the sphere's three), `epicycles.html` (stepping back as the Poisson blur),
`boost-sky.html` (the map moved by a boost).

## Sources

- Doyle, P. G. and Snell, J. L. (1984). *Random Walks and Electric Networks*. Carus Mathematical Monographs 22.
- Jaynes, E. T. (1968). Prior probabilities. *IEEE Transactions on Systems Science and Cybernetics* 4(3), 227–241.
- Kakutani, S. (1944). Two-dimensional Brownian motion and harmonic functions. *Proceedings of the Imperial Academy
  Tokyo* 20(10), 706–714. (Where a walker lands is harmonic measure.)
- Kato, S. and McCullagh, P. (2020). Some properties of a Cauchy family on the sphere derived from the Möbius
  transformations. *Bernoulli* 26(4), 3224–3248. (The spherical Cauchy.)
- McCullagh, P. (1996). Möbius transformation and Cauchy parameter estimation. *The Annals of Statistics* 24, 787–808.
- Qian, T. and Wang, Y.-B. (2011). Adaptive Fourier series, a variation of greedy algorithm. *Advances in Computational
  Mathematics* 34(3), 279–293.
- Stigler, S. M. (1974). Cauchy and the witch of Agnesi: an historical note on the Cauchy distribution. *Biometrika*
  61(2), 375–380.

The references are carried over from the essays before this one and *Reads and Writes*, where they were checked.

The account this essay follows is *Reads and Writes* (`../readers-and-writers.md`): §2 ("Heat and paint", "Why there is
no mean"), §6 ("The crosshairs", "H is a zoom") and §7 ("The hemisphere is the shape; near and far are an overlay",
"Where the split falls", "A heat map: the Cauchy's and the overlay's", "Where the heat comes from"). The rulings are SPN
R700–R707. The comparison of harmonic measure and the boosted sky on the sphere is EUL (`../../plans/eul-plan.md`), the
relay of standpoints SUM (`../../plans/sum-plan.md`), the aimed terms EPI (`../../plans/epi-plan.md`). The essays before
this one: 2 (the turn), 3 (heat and paint, no mean), 4 (near and far), 5 (the wedge and the tunnel), 6 (parallax's
corner), 13 (where the plane's one law parts), 14 (rates, the per), 16 (addresses in computing).
