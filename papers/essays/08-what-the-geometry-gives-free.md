# What the geometry gives free

*The eighth of a series of essays on what can be known from where one stands. Draft, 28 October 2026.*

Every scrolling interface meets the same wall. A scrollbar maps the list's length onto the screen's height, so a list of a
billion rows leaves each pixel of the bar a million rows wide. A flick scrolls at a speed, so the far end of a long list
takes as long to reach as the list is long. And somewhere in the code a scroll offset grows with the list. These are
three faces of one fact. The interface was built on the writer's number line, which has no corner and no horizon, and a
list without end laid on that line has no end that fits on a screen.

This essay is about what changes when such things are built on the reader's geometry instead. Once a reader holds one
length H and turns it, some structures follow with no further choice: a zoom, a split between near and far, readings no
change of size can move, and addresses for any number of things with no table and no count. Engineers have arrived at
most of them already, by design, under other names: depth buffers, log depth, floating point, level of detail, hashing on
a circle, a filter's steady state. The geometry does not do any of these jobs better. What it offers is a baseline. It
says where each structure comes from, so that what a design adds, and what that costs, can be named.

The essay opens on the dial, the cleanest case, and then goes through the others one at a time.

---

## 1. A dial: scrolling without end

The fourth essay laid one reading x three ways in one figure:
- as itself, on the writer's number line;
- as the turn θ = arctan x, which never leaves the quarter turn;
- as the hyperbolic angle ζ = asinh x, which grows without end but by about ln 2 a doubling far out.

They are tied by x = tan θ = sinh ζ, and θ = gd ζ, the Gudermannian. A dial runs all three as one control.
- **The push is ζ.** A held thumb adds to ζ at a steady rate r. Pushes add in ζ, as rapidities do in special relativity,
  which is where ζ got its other name.
- **The place is x.** The hand stands at record x = sinh ζ of the list, counted in units of a window.
- **The screen is θ.** The hand is drawn at the turn θ = gd ζ, which stays inside the quarter turn however far it has gone.
  The corner, one window from home, is drawn at 45°. The rungs at x = 2, 4, 8 … windows fall past it in levels, crowding
  toward the edge.

In code, one frame of a held push is three lines:

```
zeta += rate * dt;                    // the push adds, unbounded
const x = Math.sinh(zeta);            // the place: records from home, in window units
const theta = Math.atan(x);           // the screen: always inside the quarter turn
```

**Any place, in time logarithmic in its distance.** Held at a steady rate, the hand reaches x after

  t(x) = asinh(x)/r.

Near home it moves in proportion, x ≈ rt, one record after another. Far off each doubling costs the same time, ln 2/r.
Any place up to N is reached in about ln(2N)/r. A list of 2⁵³ records, the largest count a double holds exactly, is
crossed in 37.4/r: at a rate of 2 a second, under twenty seconds of holding. The same push crosses a thousand records in
7.6/r and a googol in 231/r. Nothing about the list's length was set in advance.

**The whole list on the screen.** The screen shows θ, a quarter turn, whatever the list's length. Within one window of
the hand the records are laid in proportion, each its own row. Past it they are laid in levels. The far end of the list
is the horizon, θ = 90°, at the edge of the screen and never drawn, as a road's end is its vanishing point. So the
scrollbar's question, how long is the list, is never asked. The list's length is N. The control works with the screen's
own fixed count of places, K.

**Letting go: a new zero.** When the thumb lets go, the place reached becomes home: ζ returns to 0 and the rungs are drawn
again about the new place. The second essay called this a new zero; the third showed it costs nothing, because a new zero
on a Cauchy is another Cauchy. Pushes compose by adding in ζ, and a release folds the sum into the place, so the control
holds no growing number. The only number that grows is the record's own index, which the list needs anyway.

**The window is a zoom.** How many records one rung holds is the window, and the window plays H. It changes how much of
the list the corner holds in proportion and moves no record's place in the list.

**Content made from the address.** Because the addresses do not depend on N, what is shown at a place can be made from
the place itself, a function of the index, and nothing need be stored. The `wedge-browse.html` demo browses 2⁵³ − 1 items
in two dimensions this way, each made from its own address by a binomial cascade and never stored, with cells opened
largest-on-screen first and every drawn total adding exactly to the whole at every zoom. The `star-dial.html` demo does the
same with a star field without end, eight times as many stars each level out, where the stars drawn and the totals of the
cells not opened add exactly to the stars held at every H. The payload, in the third essay's sense, is a function on the
addresses, and here the function is the program.

**In two dimensions.** The same control works over two sweeps. The thumb points in a direction from the centre and adds
to a two-dimensional push at a rate set by how far it is tilted. The hand sits at sinh of the push inside the triangle of
the fifth essay, nearing its edge and never reaching it. The two coordinates there are log-ratios, which add, so pushes in
two directions commute. A dial built from true two-dimensional boosts would not. Pushed round a loop and brought back to
rest, its frame would come home turned by the area the loop enclosed, as special relativity's frames do (Thomas 1926). For
a list in two dimensions that turn is a design choice, to show or to cancel.

**What is the design's and what is the geometry's.** The place, the corner, the levels past it and the horizon are the
geometry's: the three rulers and their one figure. The design adds two numbers, the rate and the window. Zooming
interfaces have arrived at relatives of this. Igarashi and Hinckley coupled scrolling speed to zoom, so that scrolling fast
zooms out (Igarashi and Hinckley 2000). Furnas and Bederson drew views as points of position and scale (Furnas and
Bederson 1995). Van Wijk and Nuij found that the smoothest zoom-and-pan paths are written in the hyperbolic functions (van
Wijk and Nuij 2003). What the geometry adds is where those choices come from: a control whose reach is the logarithm of
the list because its push is the hyperbolic angle.

---

## 2. What comes free, and what needs one premise more

The dial used most of what the geometry gives. It is worth listing it plainly, because "free" is a strong word and has to
be earned.

Once the reader chooses H, its one length, these follow with no further choice:
- **a zoom**, the value of H. Small H is fine near and coarse far; large H the reverse. Nothing else changes.
- **a split between near and far**, the corner v = h, at 45° on the reader's circle.
- **readings that no change of the world's size can move**, since every reading is a ratio. That is the first essay's test,
  scale the world.
- **addresses for any number of things, with no table and no count**, given that the sweep is uniform: the turn's Cauchy.
  This is the one the dial leans on hardest.

Two more need one stated premise each, and are free once it is granted:
- **precision far off**, the lay past the corner, 1 + ln s on the reader's lay or 2 − 1/s on the in-place lay. The
  premise is the fourth essay's (S): that no level past the corner is preferred to another.
- **a level of detail**, given a fixed count K of addresses. H then divides the K between the near field and the far, half
  inside H at every H.

And one thing is not on the list. What hides what, which surface is in front, is the payload's. It is set by which
surfaces are opaque, and the geometry says nothing about it.

The rest of this essay reads engineered systems against that list. In each case the question is the same: which of these
structures is the system using, and what did it add?

---

## 3. The depth buffer

A three-dimensional renderer has to decide, at every pixel, which surface is in front. The usual tool is a depth buffer:
each pixel stores a number for the distance of the nearest surface drawn there so far, and a new surface is drawn only if
it is nearer. The number stored is not the distance. For a point at distance d between a near plane n and a far plane f,
a perspective depth buffer stores

  (f/(f − n))·(1 − n/d).

Every graphics programmer meets the consequence. Precision is lavish near the camera and runs out far away, so that two
distant surfaces close together flicker through each other, which is called z-fighting.

Read against the geometry, the stored number is a familiar one. With H = n, the near plane, the fourth essay's in-place lay
is 2 − n/d. The depth buffer stores that, less its constant 1, rescaled to fit between 0 and 1. So:
- **Setting the near plane is choosing H.** It is the zoom, with the corner placed at the near plane.
- **The near field inside it is thrown away.** Everything nearer than n is clipped. The renderer has chosen H at the very
  front of what it draws.
- **Precision runs out far off because every address there has already been spent toward the horizon.** The in-place lay
  gives each level past the corner half the room of the last. By the time d is many times n, the remaining addresses are
  squeezed into the last sliver before the horizon at 2.

The common remedies are the other lays.
- **Logarithmic depth** in its plain form, ln(d/n)/ln(f/n), is the reader's lay past the corner, 1 + ln s, with its corner at
  the near plane. Each level of distance gets equal room.
- The form ln(Cd + 1)/ln(Cf + 1), proportional below d ≈ 1/C and logarithmic above, is a smooth form of the whole lay, near
  field and far, turning at d ≈ 1/C. It is the hyperbolic angle of section 1 smoothing the reader's lay, with its corner
  moved from the near plane out to 1/C.
- **Reversed-Z**, the remedy most engines now use, stores the in-place lay turned round, in a floating-point number. The
  fourth essay showed that a float is itself a reader's lay in base 2: an exponent for the level and a mantissa laid in
  proportion within it, the subnormal numbers below the smallest level its proportional near field. Turning the in-place
  lay round and storing it in a float puts the float's levels where the in-place lay ran out, and the result is close to
  constant relative precision over the whole range.

None of this was designed from the geometry. Each scheme was found by people solving the flicker. What the geometry adds
is the name of what each one is doing: the depth buffer is a lay with its corner at the near plane, log depth is the
reader's lay, reversed-Z the in-place lay turned round inside a float. And it adds the question a designer can then ask:
where should the corner be? The geometry's answer, from the fourth essay, is on what matters most, which in a game is
usually what the player is looking at, not the near plane.

---

## 4. The flat screen

A camera's sensor and a display are flat grids of equal pixels. Equal pixels on a plane are not equal turns.

The fifth essay worked out how the uniform turn's directions fall on a flat screen. Per unit of screen area, at angle α
off the camera's axis, their density is (2/π)·cos³α. Along a single line of the screen it is (2/π)·cos²α, one cosine
fewer. Equal pixels therefore over-weight the directions off the axis by sec³α: a pixel at the edge of a wide
view covers a smaller piece of the sky than a pixel at the centre, and there are more of them per degree. Along one line
of a screen of finite edge, the median of the directions put through its pixels falls at half the edge, not at the corner.
The weighting is the design's, added to the geometry, and it is usually unnamed. It is the geometric part of the familiar
cos⁴ fall-off of brightness toward a photograph's corners.

There is an alternative already in use. A cube map, which stores everything visible in all directions as six square
images on the faces of a cube, can lay each face by turn instead of by length, an arctangent on each coordinate. That is
the equi-angular cube map. Its cells' solid angles vary by a factor of √2 across a face, against 3√3, about 5.2, for
equal pixels. Laying by turn does not make every cell equal, since a cube's face is still flat. It takes most of the
flat screen's weighting out.

However the faces are laid, there is a bound the geometry gives directly. A direction in d + 1 dimensions is never more
than arccos(1/√(d + 1)) from the axis of the face it falls on, since its largest component is at least 1/√(d + 1). That is
45° for one other party, 54.74° for two and 60° for three. Every direction's capped reading lies within √d of its face's
centre.

---

## 5. What Math.floor throws away

Every programmer has written it:

```
const i = Math.floor(x / w);   // which cell
const f = x / w - i;           // where in the cell, in [0, 1)
```

and then kept `i` and dropped `f`. The cell's value is read from `a[i]`, and `f` is gone. It looks like rounding, a small
leftover, the part of x that did not fit the grid. This section is about why it is not, and it is the longest in the
essay, because the act of dropping it turns out to be one of the most consequential in the whole construction.

**The remainder is address, not data.** Start with what is not lost. The value stored in the cell is untouched: `a[i]` is
exactly what it was. Nothing of the payload goes. What goes is where in the cell the place was, and that is address. So
the floor is not a lossy operation on data. It is a lossy operation on the index. Where only the cell's value is wanted,
dropping the place within the cell is exactly right. Where the place matters, what was dropped was address.

Write the remainder in binary, f = 0.b₁b₂b₃… Each digit answers one question. b₁ says which half of the cell; b₂ which half
of that half; b₃ which half of that, without end. So the digits of f are the finer levels of the address, one level a
digit. `Math.floor(2 * x / w)` is the key one level finer, and its low bit is b₁. Every level of detail is a floor taken at
a different depth.

So `Math.floor` does not round one number. It takes an address that runs through every level at once and keeps it at
exactly one, discarding every finer level in a single step. A double holds 53 significant bits, and every one of them
below the cell's own is one of these levels.

**The remainder is a second dimension.** The levels in the remainder are not a list to be stored beside the index. They are
the index's other coordinate. Give the cell of level j and index k, the interval from kw to (k + 1)w with w = 2^(−j), the
point

  z = m + iγ,  with m = (k + ½)·w its middle and γ = w/2 its half-width,

in the upper half of the plane. A place is then two numbers: where it is along the line, m, and how far down it is held,
γ. The floor keeps m at one fixed height and forgets that the height was a coordinate at all.

The plane those two numbers make has a geometry of its own, and it is a classical one, the hyperbolic plane, in which
lengths are measured with ds² = (dx² + dy²)/y².
- **Every level is the next.** Doubling, z ↦ 2z, is a rigid motion of that plane, and it carries each level of cells onto
  the next. Each binary digit is one step down, and every step is the same, ln 2 in height. No level is privileged: level
  50 is as good a place to stand as level 0. On the line alone the step is the doubling map x ↦ 2x mod 1, which moves the
  first digit of the remainder into the index. Its rate of forgetting where it started is ln 2, one level a step.
- **Every cell has the same room.** The tile from kw to (k + 1)w across and from w/2 to w in height has hyperbolic area
  exactly 1, at every level. A cell fifty levels down, 2⁻⁵⁰ wide on the line, has exactly the room of the first. The tiles
  are Böröczky's binary tiling of the hyperbolic plane (Böröczky 1974).
- **Distances are fixed by the levels.** A parent and either child are arcosh(3/2), about 0.962, apart. Two siblings are
  arcosh 3, about 1.763. Two cells n apart on one level are arcosh(1 + 2n²). The same at every level and every place.
- **A point of the plane is a Cauchy law.** Each z = m + iγ is the Cauchy with foot m and height γ, the third essay's
  standpoint. From its cell's own point that law puts exactly half its weight in the cell. The cell is that law's
  interquartile range.

So the plane the floor's remainder lives in is the space of the address law's own parameters. A dyadic cell is not merely
like a Cauchy. It is one, read from its own point. The array's grid and the reader's law live in the same plane.

**A tree keeps the levels and loses the plane.** The usual way to keep the finer levels is a tree: a quadtree, an image
pyramid, a chain of mipmaps, each cell linked to its parent and its children. A tree keeps the depth and measures it
wrongly. Take the two cells either side of the middle of level j. They touch. In the plane they are arcosh 3 apart at
every level. In the tree their nearest common ancestor is the root, so they are 2j steps apart: 60 at level 30, for two
cells side by side. A neighbour search in a quadtree that has to climb to the root is meeting this.

Add sideways links, each cell joined to the cells beside it on its own level, and the graph measures the plane. Over all
523,776 pairs of cells at level 10, counting g steps up, down or across, the hyperbolic distance d never differs from
g·ln 2 by more than 2.19. The shortest way between two cells is always up, across and down, and d/g tends to ln 2. An
array indexed by level and index, `cells[level][index]`, with links across as well as up and down, is a sampled copy of
the half-plane. A tree is not.

**Two ways to lose depth.** Every reader with finite resolution loses the finer levels somewhere. The floor and a reader
at a height lose them differently.
- **The floor**, averaging over a cell, multiplies each wave of the signal by the familiar sinc. It keeps every level
  coarser than the cell whole and none finer: a wall, with zeros and side lobes past it, so that finer detail can come back
  as coarser, which is aliasing.
- **A reader at height γ**, looking through the Cauchy from z, multiplies the same wave by a smooth exponential: never zero,
  and composing as heights add.

No height brings the two within 0.22 of each other. For a step detail, a reader at its own cell's point keeps these shares
of each level, the level read against its own:

| level read, against the reader's own | −7 | −6 | −5 | −4 | −3 | −2 | −1 | 0 | +1 | +2 |
|---|---|---|---|---|---|---|---|---|---|---|
| reader at a height: share of the step kept | 0.927 | 0.874 | 0.789 | 0.660 | 0.482 | 0.279 | 0.110 | 0.027 | 0.0044 | 0.0006 |
| the floor at the same level | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |

The reader keeps half of a step 3.09 levels coarser than its own cell and takes 5.5 levels to go from 90% kept to 10%.
The share depends only on the reader's height measured in the detail's own width, so it is one soft cut over the levels,
the same at every depth. The floor's row is a wall. The `depth.html` demo draws both.

**Who sets the depth.** The floor sets one depth for everything, the cell's, chosen by the store before anything is read,
the same for a mountain and a grain of sand. The geometry sets each thing's level by its span: a thing that spans n
addresses is held to about log₂ n levels, and a thing between two addresses is held at the coarser one, not rounded to
either. The floor imposes a level of detail; the reader reads one off what it meets.

The first essay's test finds a second difference at once. Where the floor is taken of an amount, `Math.floor(x / w)`, the
cell width w is an amount too, and scaling every amount in the world by k moves the key unless w is scaled with it. The key
is then a writing: its grain had to be carried in. A floor taken of a share of the turn, `Math.floor(theta / dTheta)` with
`dTheta` a fraction of the quarter turn, carries no amount, and no scaling moves its key.

**Why it matters.** Three things follow.
- **The address is continuous and hierarchical at once.** Level of detail is not a structure kept beside the address, a
  pyramid built, stored and kept in step. It is the address's second coordinate, the height, and it comes with the address.
  Pyramids, mipmaps, quadtrees and tile keys that gain a digit a level can each be read as ways of keeping some of that
  coordinate after the floor has dropped it.
- **The hierarchy is a geometry, not a convenience.** It is the hyperbolic plane: every level alike, every cell of one room,
  distances fixed by the levels. That is why "zoom in one level" is the same operation everywhere, and why a structure that
  links only up and down gets its distances wrong.
- **The separation of address and payload reaches into the depth.** The floor discards address, never payload. From a
  height, the window 2γ is the address's, fixed before anything arrives; what survives inside it, and whether two things in
  it read as two, is the payload's.

What is not shown: that the world stores anything this way, or that any reader's level of detail is a dyadic depth rather
than a continuous height. The mathematics is classical, Böröczky's tiling, the Poisson kernel, the sinc of a box. The
reading is ours.

---

## 6. Addresses on a turn, not by a count

A count of addresses fixed beforehand runs out where the world's count grows. The turn's addresses do not, and they pay
with a horizon instead. Computer science has met both sides.

**Consistent hashing.** A distributed cache has to say which of n machines holds each key. The obvious answer,
`hash(key) % n`, divides the keys by a count. Add one machine and the count changes, and nearly every key moves. Karger and
his colleagues put keys and machines on a circle instead, each at an angle given by its hash, and each key served by the
next machine round (Karger et al. 1997). Adding a machine then moves only about one key in n + 1, those between the new
machine and the one before it. The addresses are angles, which no count enters; the machines are the payload painted on
them.

**Labels from a fixed count.** The other side is an order kept with labels drawn from a fixed range of M numbers, new items
put between old ones by giving them a label in the gap. One gap can take only about log₂ M insertions before the labels
run out and have to be given out again (Itai, Konheim and Rodeh 1981; Dietz 1982). The labels are a writer's ruler with a
fixed number of notches, and a list that grows in one place exhausts them there.

**A step that never closes.** Fibonacci hashing multiplies a key by ⌊2³²/φ⌋ = 2,654,435,769, a golden fraction of the turn
(Knuth 1998, §6.4). The second essay met steps that never close: a step that is not a rational fraction of the turn never
returns to zero. Its multiples spread round the turn, and at every count they leave at most three sizes of gap, which is the
three-distance theorem (Sós 1958). The golden fraction is the step whose gaps stay most even.

**Exact composition.** The second essay composed readings by tangent addition, and the third used a new zero as the
everyday act. Readings composed that way can be held exactly as Gaussian integers: the step v/h as the complex integer
h + iv, multiplied, and reduced after each product. The register then grows by ½·log₂ of the odd part of h² + v² bits a
step. It does not grow at all only at home, the corner and the horizon. Every other step costs storage without end. That
is the arithmetic face of the steps that never close.

---

## 7. Tables fixed in advance, and addresses that need none

A sampling table or a grid of cells fixed in advance has to know beforehand the extent it covers and the resolution it
needs, and it is rebuilt when either changes. The uniform turn's addresses need neither. A direction is given whatever
the count of things and whatever their size, and the fourth essay's K addresses at H·tan(kπ/2K) hold half inside H at
every H and every N.

Rendering meets this in importance sampling. To light a scene by a sky, a renderer draws directions in proportion to how
much light comes from each, using a table built from the sky. When the view changes in a way that moves every direction,
as a fast-moving camera's sky is boosted, the table has to be rebuilt. The seventh essay showed that a boost is a Möbius
map of the addresses and carries the Cauchy onto itself. So the directions can be drawn by pushing uniform ones through the
boost, with no table at all, and only the payload, the sky's own light in its own frame, needs tabling, once. The
`boost-sky.html` demo compares the samplers. What needs a table is the payload or the writer, never the addresses.

That is also the third essay's point that the Cauchy does not need to know N. Whatever is tied to a count, a table's size,
a grid's resolution, a far plane, is the payload's or the writer's. A method that ties with a classical one has shown it is
correct; where the classical one needed N and the turn's addresses did not, the tie comes free.

---

## 8. A filter's steady state

A Kalman filter tracking something that wanders at random keeps two variances: before each measurement, the predicted
variance, and after it, the updated one. With process noise q and measurement noise r, the filter settles with them at

  √(qr)·μ and √(qr)/μ,  μ = (n + √(n² + 4))/2,  n = √(q/r)

(Kalman 1960). They are a reciprocal pair about √(qr), the geometric mean of the two noises: the corner of the pair (q, r).
Their product is qr whatever n. For matrices the same holds with the matrix geometric mean in place of the square root.

The design supplies the noises, which are amounts. That its two variances sit at reciprocal readings about their
geometric mean is the geometry's: the fourth essay's corner, met by a recursion that knows nothing of corners.

---

## 9. The centre of directions

Where the readings themselves fall as the uniform turn's law, as the addresses of a sweep do, their tangent chart has no
mean, and the median is the law's own centre. A fit that averages them on that chart has nothing to settle on. That is
the third essay's theorem applied to engineering: least squares is a mean, and a mean of a law that has none stalls.

The working notes tested this on bearings, the directions in which features are seen from known standpoints. With bearing
errors of the Cauchy's kind, as the number of standpoints grew from 4 to 16, least squares improved by a factor of only
1.39, where the median of pairwise crossings improved by 3.95. Real bearing errors, measured on a standard image benchmark,
turned out not to be Cauchy: a narrow core plus a share of wrong matches. So in practice the cost shows where wrong matches
do. The geometry does not fix the law of measurement errors, which is another matter. It fixes the law of the addresses.

The same addresses are known in numerical analysis. Boyd's rational Chebyshev collocation points for problems on the whole
line, L·cot((2j − 1)π/2N), are the midpoints of N equal shares of the Cauchy of scale L: the reader's K addresses with L in
the place of H (Boyd 1982, 1987). Boyd's rule for choosing L, the scale of the feature to be resolved, is the fourth
essay's best H, at the corner of what is read. The same equal angles read by their cosine are Chebyshev's nodes, crowded
at the ends of a chord; by their tangent, the Cauchy's, spread out to the horizon.

---

## 10. Origin, not performance

The list of correspondences is long, and it would be easy to read it as a claim that the geometry does better. It is not.
The tests in the working notes came out as ties or trade-offs. The reader's lay with its corner at the geometric mean of the
near and far planes beat log depth past the corner by a factor of 1.78, and inside the corner kept an absolute rather than
a relative precision: a trade, not a win. A Cauchy sampler beats a rebuilt table in one regime and not in another. A median of
crossings is robust and is one robust estimator among several that were already known. The verdict of the depth-precision
test stands for all of them: the geometry names these schemes and adds none.

What it adds is the name, and with the name a baseline. Without the geometry a scheme can be seen to work. With it, what
the scheme is doing can be said, and what it gave up: the depth buffer put its corner at the near plane; the flat screen
weighted its pixels by sec³α; `Math.floor` dropped the height; `hash % n` divided by a count. Each of these may be right
for its purpose. A design that departs from the geometry may be right to, for reasons the geometry does not see.

Two limits apply. What comes free is the readings, not the amounts: metres still cost one amount carried in, and the
geometry says only which amount and why one is enough. And whether a given departure is worth its cost is the designer's
question. The geometry only makes it one that can be asked.

---

## 11. What it comes to

**Reading and writing.** Every structure in this essay sorts by the first essay's test. The dial's place, the depth
buffer's lay, the flat screen's weighting, a key floored from a share of the turn, a hash on a circle: none of them moves
when every amount in the world is scaled, so all are readings, and all came free once H was chosen. What moves is what was
carried in: the near plane's distance, the cell width of a floor taken of an amount, the noises of a filter, a far plane.
Engineering keeps rediscovering which numbers it must carry in, often one at a time and by trouble. The geometry says in
advance: one length H for the zoom, a count K if one is wanted, and an amount for each thing to be written.

**The Cauchy.** Its superpower, in the third essay's word, is that its addresses need no count. That is what the dial
uses to cross a list of any length, what consistent hashing uses to add a machine and move almost nothing, what a sampler
uses to drop its table, and what `Math.floor` throws away when it keeps one level of the address and drops the rest. The
horizon is the price: a turn's addresses never run out, and they never reach the end.

Back to the scrollbar. Its bar shrinks as the list grows because it is laid on the writer's line, which has no corner and
no horizon. A dial laid on the reader's turn keeps the whole list on one quarter turn, reaches any place in time
logarithmic in its distance, and never asks how long the list is.

---

## Sources

- Igarashi, T. and Hinckley, K. (2000). Speed-dependent automatic zooming for browsing large documents. *Proceedings of
  UIST 2000*, 139–148.
- Furnas, G. W. and Bederson, B. B. (1995). Space-scale diagrams: understanding multiscale interfaces. *Proceedings of
  CHI '95*, 234–241.
- van Wijk, J. J. and Nuij, W. A. A. (2003). Smooth and efficient zooming and panning. *Proceedings of IEEE InfoVis
  2003*, 15–23.
- Thomas, L. H. (1926). The motion of the spinning electron. *Nature* 117, 514.
- Böröczky, K. (1974). Gömbkitöltések állandó görbületű terekben I. *Matematikai Lapok* 25, 265–306.
- Karger, D., Lehman, E., Leighton, T., Panigrahy, R., Levine, M. and Lewin, D. (1997). Consistent hashing and random
  trees. *Proceedings of the 29th ACM Symposium on Theory of Computing*, 654–663.
- Itai, A., Konheim, A. G. and Rodeh, M. (1981). A sparse table implementation of priority queues. *Automata, Languages
  and Programming (ICALP 1981)*, Lecture Notes in Computer Science 115, 417–431.
- Dietz, P. F. (1982). Maintaining order in a linked list. *Proceedings of the 14th ACM Symposium on Theory of
  Computing*, 122–127.
- Knuth, D. E. (1998). *The Art of Computer Programming*, Vol. 3: *Sorting and Searching*, 2nd ed. Addison-Wesley.
- Sós, V. T. (1958). On the distribution mod 1 of the sequence nα. *Annales Universitatis Scientiarum Budapestinensis de
  Rolando Eötvös Nominatae, Sectio Mathematica* 1, 127–134.
- Kalman, R. E. (1960). A new approach to linear filtering and prediction problems. *Journal of Basic Engineering* 82(1),
  35–45.
- Boyd, J. P. (1982). The optimization of convergence for Chebyshev polynomial methods in an unbounded domain. *Journal
  of Computational Physics* 45, 43–79.
- Boyd, J. P. (1987). Spectral methods using rational basis functions on an infinite interval. *Journal of Computational
  Physics* 69, 112–142.

The geometry is set out with proofs in *Observation from Somewhere*, §8 ("What the floor discards", "What the height
fixes"), §12.4 and Appendix B, and for programmers in the computer-science companion, §7 ("What Math.floor throws away"),
§11 ("A dial: scrolling without end") and §12. The tests behind section 9 and section 10's verdicts are in the working
paper `mapping.md`, §9½.
