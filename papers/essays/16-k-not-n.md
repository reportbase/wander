# K, not N: reading and writing for computer science

*The sixteenth of a series of essays on what can be known from where one stands. Draft, 2 November 2026. It brings forward
the archived computer-science companion, "Addresses Given, Payloads Met … for computer science" (27 October), in the
vocabulary of* Reads and Writes*.*

```c
x = mem[a];      /* read  */
mem[a] = y;      /* write */
```

These two lines are the oldest interface in computing. A read takes an address and returns what is stored there, and
changes nothing. A write puts a value at an address, and the next read sees it. Everything else, files, databases,
caches, the network, is built on top of them.

The essays have been using the same two words for something older. A *read* is what an observer has from where it
stands: directions, ratios, the light arriving along each, nothing that changes when the world is scaled. A *write*
states amounts: lengths in a unit, extents, totals, the whole. The two pairs of words were not chosen to match, and yet
they do match, closely enough that it is worth asking how far. The answer is that computing already keeps the split this
series is about, the address apart from what is found there, and that it keeps it in a world a writer has already laid
out. This essay asks what changes when nobody has laid the world out yet.

Computer science has two letters for the difference, and they carry the essay. N is how many items there are. K is how
many are held. A writer knows N. A reader never does, and holds only K. The Cauchy is what goes between them.

The order: the two words (§1), the two letters (§2), two types that must never be silently cast into each other (§3), a
direction kept as a pair (§4), the corner as a register (§5), index statistics and value statistics (§6), the array
(§7), what the floor throws away (§8), two layouts of addresses (§9), the cull (§10), what a blueprint adds (§11), what
comes free (§12), and what a machine can and cannot hold (§13).

*Demos: `array-sweeps.html` (K places on the quarter turn, an array of known length beside them); `star-field.html` and
`star-field-3d.html` (N doubled, the reader's view unmoved); `star-dial.html` and `wedge-browse.html` (2⁵³ − 1 items held
at a fixed count); `depth.html` (the floor's remainder as the half-plane); `zoom.html` (H as a zoom); `fpv.html` (depth laid
by the turn, against log depth and the standard buffer).*

---

## 1. Read and write, twice

Start with the likeness, because it is real.

A computer's read takes an address and returns the value stored at it. The address is fixed before anything is stored;
storing a value moves no address. That is the split between address and payload that the third essay drew from a hand
held up to a stained-glass window: the fingers are there before any light reaches them, and changing the window changes
the colours and moves no finger. Hardware has had the split since the first stored-program machine.

A computer's write stores at an address a value that came from somewhere else: from input, from a computation over
other values, from a constant in the source. A write in this series likewise needs an amount carried in from outside.
No collection of readings, from any number of standpoints, fixes a size; one amount brought in fixes every size the
readings link to it (§11).

Then the two pairs part, in five places.

- **Who lays out the addresses.** A computer's address space exists before the first read: a known size, addresses
  counted from 0 to N − 1, an end, and an error past it. Someone laid that out, and laying out a space of known size is
  a writer's act. An array whose `sizeof` is known is held by a writer (essay 12). A reader has no addresses at all: it
  has directions and their heat, given by its turn, uniform by the turn's own measure, from home toward a horizon it never
  reaches. There is no N among them, no last place, and no end to fall off.
- **What a read returns.** A computer's read returns an amount: a byte, an integer, a float, in whatever unit the
  program agreed. A read here returns a direction and the paint arriving along it, with every amount along that
  direction already gone. Nothing in it would change if the world were k times as large.
- **What a write changes.** A computer's write changes the memory. A write here states amounts ("the room is 15 metres
  wide"); it changes the world only when it is acted on, as moving the furniture is.
- **What stays the same.** A computer's read is repeatable: read one address twice with no write between and the value
  is the same. A read here has a stronger sameness, across worlds: scale the world and no reading moves.
- **Where caching falls.** In a computer, keeping a value read, in a cache or a variable, is a write into another place.
  Here too: to keep a reading as a number, a length in a unit, an entry in a table of known size, is to write it.

So the computing words are the writer's frame applied to both acts. Memory is a written world, and a computer's read is
an address looked up in it. The read of this series comes before any such layout. It is what a reader has when no one
has written the memory, and when no one could, because the world it reads has no size anyone holds.

### Why reads never race

The first thing a programmer thinks of, seeing *read* and *write* together, is a race. Bernstein's conditions (1966)
say when two operations may run together: neither writes what the other reads, and they do not write the same place.
Reads with reads are always safe (the concurrent-read side of CREW); a race needs a write meeting a read or another
write on one location. Most of the machinery of concurrency, locks, versions, copy-on-write, persistent structures, MVCC
(multiversion concurrency control), exists to keep that meeting from happening, or to make it harmless.

The split this series turns on is that condition, given rather than built. A read adds nothing, so reads of one geometry
agree in whatever order they are taken, or all at once. A write states the payload, and the second test of the third
essay says a change of payload moves no address. So a write never moves what a read stands on, and never runs into one.

The failures in computing are exactly where that breaks: places whose addresses move with their contents. A vector
that reallocates invalidates every pointer into it; a hash table that rehashes moves every entry; a compacting
collector moves objects under their references. Each is repaired by rebuilding the separation by hand: stable handles,
indirection tables, copies kept for the readers, versions that leave the old addresses standing. The reader's directions
need none of it. They and their heat are the turn's, given before anything arrives, and nothing written can move them.

### The projection is the dereference

In memory, an address and the value it reaches are the same kind of thing: a pattern of bits, an integer in a layout of
N slots. Untyped, nothing tells a pointer from a number, and the machine needs a separate step, the dereference
(`*p`, a load), to go from the one to the other. Typed languages, tagged machines and capability hardware such as CHERI
keep the two apart again, by type or in the hardware; the separation is built.

For the reader it is not built, because the two were never one kind. Where memory has an address, the reader has a
direction [h : v], a share of the thumb with no length in it; what reaches it is paint, an arrival with no direction to add to. There is nothing to do
arithmetic between them, and no step from one to the other: pointing is the dereference. Looking along a direction is
already to be met by whatever arrives along it, and which thing that is (the first met) is the world's, the payload's.
So there is no indirection to pay for, in cycles or misses; that cost belongs to a machine, which holds both acts in one
memory, not to the geometry, which is given before anything arrives.

### Heat, not addresses

The words in this essay are the programmer's, and a programmer's addresses are discrete: places counted in a layout, the
writer's. The reader has none. What it has is a heat over its directions, the Cauchy: continuous, hottest along the look
and cooling toward the horizon, with nothing counted in it (*Reads and Writes* §7, "Where the heat comes from"). Where this
essay says "the reader's addresses" or "K addresses", it uses the word as a metaphor, the one that connects the Cauchy to
computing: read it as K places a writer lays at the heat's quantiles, the heat under them. The heat is given; the paint is
met.

This is not a claim that geometry proves anything new about concurrency. It is the other way: a principle computing
already holds, applied to geometry, says why the reader's world has no races to manage. It does not make a computer
race-free, which does both acts in one memory (*Reads and Writes* sets the machine aside for that reason).

---

## 2. Two letters

The letters K and N are everywhere in computing: N for the size of the input, K for the size of what is kept (the
top K, a K-way merge, a sketch of K counters, a cache of K lines). Asymptotic analysis is mostly about how cost grows
with N, and the most valuable algorithms are the ones whose cost does not.

Read the two letters as vantages:

- **N is the writer's.** To know N is to know the whole: how many there are, which is to know the extent, V, and how much
  is in it. That is writing. The first essay's test sorts it at once: double the world and N doubles.
- **K is the reader's.** A reader never knows V, the mountain in the distance (it holds one length, its own H, the thumb it
  holds up, and V was never in a reading), so it never knows N. What it knows is K, its own fineness, read continuously (a writer counts it as K addresses), fixed before
  it chooses H and unchanged by anything it looks at.

The Cauchy is the map from a world of N to a holding of K. Its heat spreads the reader's K over a world of any size, and
counted as K addresses it puts them: in
proportion inside the corner, by thumbs past it, two, four, eight, and everything past the last address on the one address
at the horizon. Double N and the reader's view does not change. Make N unbounded and it still does not. An infinite star
field browsed at N and at 2N stars, counted exactly at K addresses, gives views that differ by less than 10⁻⁷ at N = 2⁴⁰
(`star-field.html`), and by less as N grows.

So the Cauchy is a *cull*. Whatever N is, the reader's work is K, O(K). For a fixed K it does not grow with N; there is no N in it to grow.

What the cull gives up is sameness. A writer who knows N can hold every item as 1/N of the whole, all alike, on a number
line with no corner, and no item has an advantage over another, because no standpoint is favoured: there is none. A
reader's K is spent unevenly: finest at the corner, coarser each time a thing is twice as far, and that unevenness is the
vantage. What is looked at gets the most. Knowing N buys equality; holding only K buys a standpoint, at a cost that does
not grow with the world.

---

## 3. Two types

Everything in the series is built from the *unit relation*: a number between 0 and 1 relating a part to its whole, like
the fraction of a day gone or the share of a road behind. A relation needs two, one for each party, and they are written
h and v, in lower case.

The wholes are written in upper case. The reader holds one, H, the thumb, a value it chooses to start from rather than a
size it measured; any H will do, and H only sets where the finest addresses fall. It holds no other. A writer, holding both
sides, also holds V, the other party's breadth, and V* is the other party's true size, an amount. The amounts are h·H and
v·V*, and so

  (v·V*)/(h·H) = (v/h)·(V*/H).

The ratio of unit relations, v/h, is not the ratio of amounts. The only way from one to the other is to multiply by a
breadth, and the breadth must be known.

In a program these are two types: a unitless ratio, and an amount in some unit. Most of the confusion this series has
had to untangle, in its own older papers as much as anywhere, is a silent cast from one to the other: a reading taken for
a measurement, v/h written where V*/H was meant. A type system would refuse the cast. A direction type with no length,
no unit and no addition; an amount type that carries its unit; and a conversion between them that takes a breadth as an
argument, so the breadth has to come from somewhere visible. Essay 12 asked for exactly this.

The first essay's test becomes a property test. Run the system on the world, and on the world with every length
multiplied by k. Whatever does not move is a reading. Whatever moves by k (or a power of k) is a writing, and an amount
had to be carried in to make it. A record the test would not move cannot contain the world's size, however carefully it
was made.

---

## 4. A direction is a pair

A reading is a pair (h, v), both at least 0 and not both 0, taken up to a common factor: a direction, written [h : v].
Graphics programmers know this form already as homogeneous coordinates, kept for the same reason: a point at infinity is
an ordinary value in it.

**Division by zero.** A program that keeps a direction as one number, a slope v/h, has chosen a chart, and that chart
sends the horizon, [0 : 1], to infinity. Dividing by zero is the chart reaching its own end, not anything in the
direction. As a pair the horizon is as ordinary as home, [1 : 0]; the other chart, h/v, sends home to infinity instead.
The reader divides nothing: the projection from home divides, and the reading is the ratio itself. Computing has met this
one remedy at a time, and every remedy keeps the pair:

- *Homogeneous coordinates.* A graphics pipeline carries [x : y : z : w] and divides by w last, after clipping. A point
  with w = 0 is a direction, held like any other.
- *`atan2(v, h)`.* It takes the pair, so the horizon is the end of the quarter turn and not a fault.
- *Floating point's infinities.* IEEE 754 gives 1/0 = +∞ and −1/0 = −∞, closing the line at two ends, and 0/0 = NaN,
  the one pair, [0 : 0], that names no direction. The 8087 also had a projective mode with one unsigned infinity, which
  closes the line as a circle of directions does; the 1985 standard kept only the two ends. Posits close it again with a
  single point at infinity (Gustafson and Yonemoto 2017).
- *Integers* have no infinity and trap: they are amounts and nothing else.

The rule is a representation's, not a numerical trick. Where a value is a direction, keep the pair and divide last, if
at all. Where it is an amount over an amount, a zero denominator is a real absence (a rate over no elapsed time, a mean of
no items), and no closure of the line repairs it. That zero belongs to the writer's sums (§11). The readings have only the
chart's.

**Comparing without dividing.** Of two directions [h₁ : v₁] and [h₂ : v₂], the first is farther from home exactly when

  D = v₁·h₂ − v₂·h₁

is positive: a cross product, exact in integers, zero when the two are one direction. The comparison is transitive with
no quotient (D(A, C)·h_B = D(A, B)·h_C + D(B, C)·h_A, Plücker's three-term relation), so a sort by D alone is a sort.
Comparing a reading with its own reciprocal gives D = v² − h², zero exactly at the corner. Sameness, order and the corner
need no division; only the size of D depends on scale.

**Composing.** Readings from two zeros compose as turns compose, by tangent addition,

  s ⊕ t = (s + t)/(1 − st),

and a full round composes to no turn, which is a check a program can run. Directions have no sum, only this composition.
Kept as complex numbers the composition loses its pole: (h₁ + iv₁)(h₂ + iv₂) is the composed direction, exact in Gaussian
integers. That works in the plane and only there; turns of space do not commute, and quaternions compose them in order
(essay 13).

Repeating one rational step t comes back to zero after finitely many steps only for t = 0, 1 and ∞ (Niven 1956). Every
other rational step never closes, and held exactly its register grows without end (§12). The reader can compose a step
forever; it cannot always say, in a fixed number of bits, where it has got to.

---

## 5. The corner is a register switch

Let x = v/h. The reciprocal x ↦ 1/x swaps (0, 1) with (1, ∞) point for point and fixes one point, x = 1, the *corner*.
Every sweep from home passes through it, and it depends on neither H nor V. That much is arithmetic.

Its use in computing is a fact about fixed-width storage. Suppose a reader keeps x in two registers: x itself where
x ≤ a, and 1/x where x > a. Both registers stay within [0, 1] if and only if a = 1. A reader that keeps a bounded register
must switch at the corner and nowhere else. Numerical code already does this when it pivots: past the corner h is the
smaller part, and dividing by the smaller part lets a small wobble swing the answer without bound, so a routine inverts
and divides by the larger.

A second reason routines switch there: the expansion 1/(1 + x²) = 1 − x² + x⁴ − … converges for x < 1 and diverges for
x > 1, and past the corner the expansion in 1/x converges instead. The function has no break at the corner; its series
do. This is one reason near and far seem to obey different mathematics, and why a library evaluates them by different
formulas.

---

## 6. Index statistics and value statistics

> **The Cauchy is not the payload; it is the heat of the directions the payload arrives along.**

Directions taken uniformly by turn from where a reader stands, each read as v/h, follow the half-Cauchy on one quadrant,
density 2/(π(1 + x²)), its median at the corner. Whatever arrives along a direction, at whatever reach ℓ, its components
are ℓh and ℓv and its reading is v/h. So the law is the turn's, fixed before anything arrives, and the same whatever
arrives.

Now split statistics by what they need. An *index statistic* depends only on order: the ranks, the median, the quartiles.
It can be computed from a sort. A *value statistic* depends on sizes: the mean, any sum. It needs the values.

- **Index statistics ignore the payload.** For any strictly increasing map f, f(X) has the ranks of X, so every index
  statistic picks out the same element: median f(X) = f(median X). Conversely, ranks keep exactly what survives every
  such map, and nothing more.
- **Value statistics do not.** Among increasing maps, only an affine one commutes with the mean on every set. For any
  other there is a set where the mean of the images is not the image of the mean. (The word "increasing" matters: an
  additive function built on a Hamel basis commutes with every finite mean without being affine.)
- **So the Cauchy has a median and no mean**, and the missing mean costs nothing: a mean is a sum of sizes, a question
  about the payload, and the Cauchy is not the payload. Its quartiles are √2 − 1 and √2 + 1, a reciprocal pair.

In computing terms: order statistics are index statistics and sums are value statistics, and that is a theorem, not a
convention. Finding a Cauchy in data is, by itself, no evidence that anything in the world is spread that way. The test
for any Cauchy met in practice is to find the turn and find the amount: a spectral line is a strength, an amount whose
values add, times a profile laid by the uniform turn of a phase.

The median needs less than the uniform turn. Any sweep from all of h to all of v that treats the two parties alike puts
its median at the corner; if its weight also stays above zero near the horizon, it has no mean. Only the uniform turn
gives the Cauchy's exact shape.

**A median in two registers.** An exact running median of n readings needs storage that grows with n (Munro and Paterson
1980). To a stated accuracy it needs two registers: move an estimate by the sign of each comparison,
`m += a_k * sign(x_k - m)`, with steps a_k falling more slowly than 1/k, and keep a running average of m (Robbins and Monro
1951; Polyak and Juditsky 1992). It reads only a comparison's sign. A running mean, against that, needs the count n,
which is an amount. Even online, the median is the read's and the mean the write's.

**A closed type.** Every operation a reader makes on a direction keeps the law in the Cauchy family and moves only its
one point m + iγ, the standpoint's foot and height:

| what the reader does | what the law does |
|---|---|
| starts again from a new zero (a turn) | a Möbius map: Cauchy to Cauchy |
| takes the reciprocal | Cauchy to Cauchy |
| zooms | Cauchy of another scale |
| relays through a standpoint between | a sum: Cauchy |
| averages n readings | the same Cauchy: nothing gained, nothing lost |

For a programmer the family is a closed type: every change of standpoint or chart (a real Möbius map) returns the same type, and the whole state of
a law is two numbers. Averaging gains nothing, as it should not, since it is an operation on amounts. (The table is about
the signed reading over two quadrants; the reader's half-Cauchy on one quadrant is carried off its arc by a turn.)

**What breaks it.** Only operations that bring an amount in: squaring; cutting the line at an edge, as a flat screen of
finite width does; multiplying by an amount that varies; adding an amount, as thermal speeds add to a spectral line;
pooling standpoints without relaying them; counting the turn against a lopsided clock. Even then the tails go last: the
law is lost first near its centre and last at the horizon.

---

## 7. The array

Essay 12 took `int a[10]` apart. Here is the part of it a programmer can type.

**K places on the quarter turn.** The index of a direction (h, v), among K places, is its share of the turn times K:

```js
const turnIndex = (v, h, K) => Math.min(K - 1, Math.floor(K * (2 / Math.PI) * Math.atan2(v, h)));
```

`atan2` takes the horizon without dividing, and the clamp keeps it in the last place. No length enters. At K = 8 the
readings 0.1, 0.5, 1, 2, 3, 10, 1000 and the horizon go to places 0, 2, 4, 5, 6, 7, 7, 7. The boundaries are tan(kπ/16);
the places' middles are the half-Cauchy's eight evenly spaced quantiles, 0.099 to 10.15. The corner is the boundary
between places 3 and 4, found with no length; a reading and its reciprocal go to places k and K − 1 − k; scaling v and h
together moves no index.

That code is a writer's code, and it should be said so. It evaluates an arctangent, which takes π, and it floors, which
takes K; both are the writer's tools for describing where the reader's addresses fall. The reader evaluates nothing: its
turn passes the places in order, and the share passed is met, not computed. A program recreates the reader's situation
by a boundary: the world a generator with no length across, the reader K slots of its own, and the writer's arithmetic
between them (essay 12, §6).

Against it, an array of known length: `Math.floor(N * x / X)` needs the extent X. With N = 8 and X = 100 the amounts 10,
50 and 99 go to places 0, 4 and 7. `turnIndex(x, H, 8)` needs only H, the zoom: places 4, 6 and 7 at H = 10, and 1, 4 and 5
at H = 50.

**The length sorts the operations.** Normalizing an index as i/N, indexing from the end, a percentile index p·N, a mean,
concatenation and a bounds check all use `length`. Comparing two elements, ranking, the median of what is present, the
ratio of two entries and the step to the next index do not. Whether an operation touches `length` is the scale test
applied to code: the first list is writing, the second reading.

**Four kinds of array.** What is known of the two breadths gives four kinds.
- *A constant array of known length*: every entry the radius. It needs no storing; it is the equation of the one-length
  circle.
- *An array of known length*: an amount at every index, which a writer can join into a closed shape.
- *Values without the length*: amounts known only up to one common factor, like samples from a sensor of unknown gain.
  They can be ranked and their ratios taken, not sized.
- *The index alone*: allocated before any value arrives, with no length; its slots the Cauchy's quantiles, its middle the
  corner, its last slot running to the horizon. K slots for any N, as a hash ring's are.

The writer's arrays have the length; the reader's are the index, and the values on it without the length. That one
number is what writing supplies.

**The unknown factor.** A weight vector known only up to its normalizing constant Z is the third kind, and the
algorithms built for it use only ratios of entries. Metropolis's test compares p(x′)/p(x), so Z cancels and rescaling
every weight changes no step of the chain (Metropolis et al. 1953; Hastings 1970). Computing Z itself, a partition
function or an evidence, is the writing step, and it is the hard one. In logarithms the unknown factor is an added
constant: the payload without its size is the log-values less their mean, unchanged by the factor, while the mean moves
by exactly its logarithm.

**One array per facing.** A circle has four facings, the quadrants, and can be stored as four arrays on one lattice,
places at (k + ½)·(π/2)/K. Reading one backwards is the reciprocal. A sphere is eight, one per octant. A reading carries no
sign, so from a standpoint every facing is the same array, and a reader reads within one. Joining two needs their values
to meet at the shared end in one unit, which needs each array's size, which no reading fixes. The writer knows the sizes
and joins the four into a closed circle; the reader cannot tell whether two ends meet. Not knowing the size is also what
makes the corner and the horizon: the writer's array ends at an amount; the reader's ends at a direction, [0 : 1], where
its chart runs out.

**Growth.** A dynamic array is still a writer, but every growth rewrites the one number, and what moves when it does is
exactly what divided by it. An index counted from the start survives an append. An index from the end moves, and so does
any position stated as i/N: a percentile, a scroll fraction, a progress bar. An index laid by turn never moves, because it
never used N. Growing capacity by a factor g puts the reallocations at capacities g, g², g³, …, and the copying over N
appends stays under gN/(g − 1): 2N at g = 2, 3N at g = 1.5. Any g above 1 gives a constant cost per element. The powers are
forced; their base is not.

A timestamp is the other side. An address made of slots, a fixed number to each digit whatever the digit holds, does not
move as the world grows: the radix was agreed beforehand, and it is a written amount carried into every address. The price
is the slots held empty.

---

## 8. What the floor throws away

```js
const i = Math.floor(x / w);   // which cell
const f = x / w - i;           // where in the cell, in [0, 1)
```

Every programmer has kept `i` and dropped `f`. Essay 8 (§5) follows this all the way; here is the part that bears on K
and N.

The value stored in the cell is untouched by the floor. Nothing of the payload goes. What goes is where in the cell the
place was, and that is address. Written in binary, f = 0.b₁b₂b₃…, each digit answers one question, which half, then which
half of that half: the digits of f are the address carried finer, one halving a digit. `Math.floor(2 * x / w)` is the key
one halving finer. So the floor does not round one number. It takes an address that runs through every depth at once and
keeps one, discarding every finer depth in a single step.

Those digits are not a list to store beside the index; they are its other coordinate. Give the cell of depth j and index k
the point z = m + iγ, its middle m and its half-width γ, in the upper half-plane. Then:

- z ↦ 2z carries each depth onto the next, every step alike;
- every cell has hyperbolic area exactly 1, at every depth (Böröczky's binary tiling, 1974);
- each z is a Cauchy law C(m, γ), and from its own point it puts exactly half its weight in the cell: the cell is that
  law's interquartile range.

So the plane the floor's remainder lives in is the space of the address law's own parameters. A tree (a quadtree, a mipmap
chain) keeps the depths and loses the plane: two cells side by side across the middle of depth j are 2j steps apart in the
tree and a fixed hyperbolic distance apart in the plane. Add the sideways links, each cell joined to its neighbours at its
own depth, and the graph measures the plane: an array `cells[depth][index]` read with its neighbours is the address plane,
sampled.

And the floor imposes a depth where a reader reads one off what it meets. The floor sets one depth for everything, chosen
by the store before anything is read. A reader at height γ keeps each depth softly, multiplying a wave by e^(−kγ), never
zero and never a wall; the floor keeps every halving coarser than the cell whole and none finer. Where the floor is taken
of an amount, `Math.floor(x / w)`, the width w is an amount, and the scale test moves the key unless w moves with it: the
key is a writing. A floor taken of a share of the turn carries no amount and nothing moves it.

---

## 9. Two layouts of addresses

Inside the corner the reader can lay its readings in proportion. Past it the reciprocal gives h/v within [0, 1], but says
nothing about layout. Ask only that a lay not build in a scale the reader cannot have: that the room between x and λx
depend on λ alone. Then the far lay is the logarithm, as many addresses over each stretch where the reading halves
(Cauchy's functional equation, Cauchy 1821). The ratio is what the reader holds; counting the stretches, and the smooth
1 + ln x, are the writer's. The premise is assumed, not derived, and it is the only premise the logarithm needs.

**Floating point lays its numbers this way.** The exponent counts powers of two and the significand is a plain share
between one and the next; the subnormals lay one stretch in proportion from zero. Count of powers plus the share toward the
next is the logarithm laid straight between powers of two, never more than 0.086 of the way to the next from the smooth
curve. A float differs from the reader in counting powers of two on both sides of 1 and in having a floor; the reader has
proportion inside the corner and no floor.

**Why not proportion all the way out.** A reader that kept v/h in proportion past the corner would overflow (its range
runs to infinity), divide by the smaller part, have averages that never settle, have to crop as a flat camera does near
the corner, and find its expansions failing. Each of these is familiar from numerical work.

**Why halving.** If a stretch, from one thumb to two say, has only its two ends, their order and the reciprocal between
them, the only subdivision its symmetries preserve is the cut at the corner into two halves; applied again, binary
subdivision. Any other number of parts needs a measure carried in. Halving a count or a length is rational and the
reader's. Halving a turn, or a stretch's ratio at its geometric middle, takes a square root, two lengths combined, and is
the writer's. A calendar's uneven units (months, hours, minutes) match no single factor and cost a table: uniformity can be
free; variation has to be stored.

**Three boundaries.** The *corner*, v = h, between the two sides of a reading, which every reader finds. The *end of its
range*, where its count of addresses runs out, as a float overflows when its exponent runs out; a reader can reach it.
The *horizon*, h = 0, the reading's own infinity, which no reader reaches.

---

## 10. The cull

Now the K addresses can be laid along distance. The writer's account of where they fall, with its tangent and its π, is

  d_k = H·tan(kπ/2K),  k = 1, …, K − 1,

the Cauchy's quantiles with its scale at H. The heat they sample is the reader's; the places, and the formula placing
them, are the writer's.

- Since tan(π/4) = 1, the middle boundary is d = H, one thumb away, whatever H is: half the addresses inside the corner and
  half past it, at every H. H moves the split; it never changes the count.
- The first address is about πH/2K wide: a small H, a small thumb, makes the near half fine, a large H carries the far half
  farther.
- The world's count enters nowhere. A world of N things, of 2N, or of infinitely many is held at the same K addresses,
  each holding its share. N enters only as that share, which is payload.

For a programmer this is the useful part. The addresses are a closed form in k, H and K: no table is built, nothing is
precomputed for N, and nothing is rebuilt when N changes. The last address runs to the horizon, so a finite K covers an
unbounded world. Tables fixed in advance (a sampling grid, a histogram's bins, a lookup of known range) must know the
extent they cover and the resolution they need, and are rebuilt when either changes. The turn's addresses need neither;
what needs them is the payload or the writer.

**A world made where the view reaches.** A program that recreates the reader's view need not store a world at all. Make
each thing from its cell, at every scale, only when the view reaches that cell, and keep only what spans a quarter of one
address, π/8K; give each thing a key so that it is the same thing when made again. The view's work is then K whatever the
world holds, and there is no N anywhere to know. `crosshairs.html` draws its field that way, and lays its far field by
distance address, the bands one in 2, 4, 8 packing ever thinner under the horizon.

**H is a zoom, not an escape.** A reader could choose a very large H, a big thumb, and hold everything in proportion, with
no logarithm. The cost is detail: with K addresses spread over a very large H, everything at the reader's own scale falls
inside the first. With n addresses across the near field, a thing covering d to d + Δ spans nΔ/H of them inside the corner,
one halving of detail fewer each time H, the thumb, is made twice as big; past the corner, on the logarithmic lay, n·ln(1 +
Δ/d), whatever H is. The best H puts the thing read at the corner. The hyperbolic browser (Lamping, Rao and Pirolli 1995),
mipmaps (Williams 1983) and map tiles whose key gains a digit a halving all make this choice by design.

**The corner follows the focus.** On the turn's addresses a cell's width relative to its distance is (π/2K)(s + 1/s), least
at s = 1. The corner is the addresses' median, their finest relative grain and the reciprocal's fixed point, the roles a
focus wants; it is also where the expected travel to the next look is least, whenever the next look is as likely on either
side. So what is looked at is drawn at H, one thumb wide. Near and far are then nearer and farther than the focus, held
alike; their job is to show where to look next. The fewest addresses for a focus of extent F at grain δ, with a field to X
whose cells stay within a factor ρ of each other, are ⌈F/δ⌉ + ⌈log_ρ(X/F)⌉: proportion on the focus, the logarithm past its
edge. At X/F = 64 and ρ = 2 the field costs six addresses, whatever K is. `fpv.html` lays a first-person view's depth this
way.

**Only the turn's cull composes.** Other paths from all of h to all of v, each swept uniformly along its own length, also
squeeze the line into K addresses with H at their median and a tail that sends the rest to the horizon: the line
|h| + |v| = 1 and the square's edges among them. They part when used again. Started from a new zero, or with two readings
added, only the turn's squeeze stays in its own family; the line's and the square's drift off it. Of the three ways to
cull, only one can be re-aimed and recombined.

**More points, fewer told apart.** Seen side-on, N points round a circle, read across the view to a resolution ε, are
told apart R(N) = (N/π)·arccos(εN/2π) of them. That peaks at about 1.12/ε points and falls to none at N = 2π/ε. Past the
peak, more points mean fewer told apart. The addresses never overflow; the resolution does.

**From far off, a thing is its total at its centroid.** A cluster read from far off arrives as its total at its centroid,
each finer order smaller by one more power of the reading, the corner of the pair (cluster radius, distance) the seam. This
is detail chosen by distance, and it is the cull's far field: a whole subtree held as one address.

**The dial.** Put the cull under a thumb. A held push adds to the hyperbolic angle ζ; the place is sinh ζ; the screen is
the turn gd ζ, which never leaves the quarter turn. Any place up to N is reached in about ln(2N)/rate: a list of 2⁵³
records in under twenty seconds at a rate of 2, a googol in about two minutes. The far end is the horizon, at the screen's
edge and never drawn, so the screen holds K whether the list has a thousand records or none at the end. Letting go makes
the place reached home again, so the control holds no growing number. Essay 8 (§1) sets it out; `star-dial.html` and
`wedge-browse.html` run it over 2⁵³ − 1 items made from their own addresses, never stored, every drawn total adding
exactly to the whole. Content made from the address is the payload as a function on the addresses, and here the function
is the program.

---

## 11. What a blueprint adds

**Ratios suffice.** Everything a reader does from where it stands is done in ratios. Every reading is a ratio with no
unit in it; the index and its law are given before any value; near and far are laid by count; order statistics survive
every change of value; more standpoints bring back the figure up to its size; one step taken places everything in the
reader's own H. A system that builds, places, compares, orders and checks from where it stands needs nothing more.

**Scale cannot be read.** Multiply every amount in a scene by λ and every ratio is unchanged, so no collection of
readings, from any number of standpoints, fixes the scale. Supply one amount L₀ from outside and every amount the
readings link to it is fixed. And two readers who share one closed loop, each counting in its own unit, recover from the
closure the ratio of their units, H_B/H_A = |S_A|/|S_B|, and nothing more: a shared fact buys one factor.

**What a blueprint adds.** A blueprint is the writer's statement in amounts. It gives seven things the ratios do not:
the size; parts made apart that must meet out of view; sums, totals, means and budgets; the join of every facing; a
statement before the thing exists, to be built to; completeness stated; and a far field in proportion, common to readers
whose corners differ. In a program's terms: an index and its order statistics run on ratios; a schema with units, a sum,
or an interface between components built apart needs the amount. None is needed to work from a standpoint. Each becomes
needed when parts made apart must meet, amounts must add, or the whole must be stated in advance: the needs of an
intricate system of many parts. A blueprint is a capability, not a condition.

**Distance in the payload.** What arrives can carry cues to distance: an echo's delay, how faint a thing of a known kind
looks. Each becomes a distance only with an amount carried in, the signal's speed and a clock, or the thing's true
brightness. Ranging is writing. Scale the world and the distance so stated moves.

**The best guess is the median.** A reader that must guess the other's size, the mountain's, knowing only V₋ ≤ V* ≤ V₊,
does best, on the logarithm, at √(V₋V₊), the corner of its bounds; holding a distribution, at its median, for every
increasing measure of error; knowing nothing either way, at H itself.

---

## 12. What comes free, and what was built

Once a reader chooses H, the size of its thumb, some structures follow with no further choice: a zoom; a split between near
and far; readings no change of size can move; and, given uniform directions, addresses for any number of things with no
table and no count. Two more need one premise: the logarithm past the corner (the premise of §9), and detail (a fixed K).
What hides what is not among them; that is the payload's, set by which surfaces are opaque.

Engineers have arrived at many of these by design. The geometry does not do their jobs better; it says where each comes
from, so that what a design adds can be named. Essay 8 goes through them; in brief:

- **The depth buffer** stores (f/(f − n))·(1 − n/d), the in-place lay with H at the near plane: setting the near plane is
  choosing H, and precision runs out far off because every address there was spent toward the horizon. Log depth is the
  logarithmic lay with its corner at the near plane.
- **The flat screen.** Equal pixels on a plane are not equal turns: they over-weight directions off the axis by sec³α,
  and along one line they put the median at half the edge, not at the corner. Laid by turn instead (the equi-angular
  cubemap), cell sizes vary by √2 across a face against about 5.2 for equal pixels.
- **Consistent hashing** puts keys and machines on a circle by angle (Karger et al. 1997): adding a machine moves about
  one key in n + 1, where `hash(key) % n` moves nearly all. That is the difference between K and N in one line:
  `% n` is a writer's address, divided by the count, and moves when the count does; a place on the turn never used it.
  Order-maintenance labels from a fixed count M are the other side: one gap takes about log₂ M insertions before labels
  must be reassigned.
- **Fibonacci hashing** multiplies by ⌊2³²/φ⌋ = 2,654,435,769, a golden fraction of the turn (Knuth 1998): a step that never
  closes, whose multiples leave at most three sizes of gap at every count (Sós 1958).
- **Exact composition.** Readings composed by tangent addition can be held as Gaussian integers, the step v/h as h + iv.
  The register grows by ½·log₂ of the odd part of h² + v² bits a step, and not at all only at home, the corner and the
  horizon: the arithmetic face of steps that never close.
- **Boyd's rational Chebyshev points**, L·cot((2j − 1)π/2N), are the midpoints of N equal shares of the Cauchy of scale L:
  the reader's addresses with L = H, and Boyd's rule for L, the scale of the feature to resolve, is the best H at the
  corner of what is read (Boyd 1982, 1987).
- **A Kalman filter** tracking a random walk settles with predicted and updated variances √(qr)·μ and √(qr)/μ, a
  reciprocal pair about √(qr) (Kalman 1960). The noises are the design's; the corner they meet about is the geometric
  mean's.

This is a claim about where the structures come from, not about how well any system performs. A design that departs from
the geometry may be right to, for reasons the geometry does not see. What comes free is the readings, never the amounts:
metres still cost one amount carried in.

---

## 13. What a machine can and cannot hold

Essays 12 and 15 asked this from two sides; here is the answer in this essay's terms.

A computer is a writer. Every number it holds is a fraction: a float is an integer times a power of two, `Math.PI` is
884279719003555/281474976710656. Doubles end near 1.8 × 10³⁰⁸. So a program cannot hold the Cauchy itself, which has its
infinity in the chart v/h. Drawn as tan((π/2)·U) from a uniform double U, the largest value is about 3.5 × 10¹⁵, so a
machine's Cauchy is truncated and has a mean, (1/π)·ln(1 + M²) ≈ 22.8 for that largest draw M. The true one has none.

What makes a program faithful anyway is that every machine operation on numbers is monotone: rounding, overflow and
truncation never swap the order of two values. By §6, order statistics then come out as the true ones rounded, and sums do
not. Over 11, 1,001, 100,001 and ten million draws the median of v/h is 1.21, 0.97, 1.002 and 1.0003, settling; the mean is
1.78, 3.68, 14.3 and 13.0, never settling. Capping 100,001 draws at 10, 10³ or 65,504, as a smaller machine would saturate,
moves their mean from 8.08 to 2.10, 5.07 or 7.74 and does not move their median (`runs/arr/infinity.mjs`).

So a program holds a reader faithfully where it keeps the infinity as a horizon, a pair [0 : 1] or an angle, and keeps
its operations to order; it is unfaithful where the infinity sits inside a sum of amounts. The pieces are all in
computing already: homogeneous coordinates and `atan2` for the pair; sorts, selections and two-register medians for the
order; generators for a world with no length across; types to keep the writer's N on the writer's side; the dial for a
list without end. What the geometry adds is the reason they fit together.

---

## 14. What it changes

Computing already reads and writes, and its read and write already keep the address apart from what is found there. That
is why the Cauchy maps onto computing so well: the split it lives on is the one memory is built on. What computing does
not usually mark is that its address space was laid out by a writer, with an N, before the first read. The read of this
series comes before that layout.

Put in computing's own letters: the writer holds N, every item 1/N of a whole, all alike, no vantage; the reader holds K,
spent unevenly, finest where it looks. The Cauchy is the cull between them, K addresses over any N at a cost constant in N,
and the only cull among its kind that can be re-aimed and recombined without leaving its family. From it come the corner
as the one place a bounded register can switch, order statistics as the statistics that survive, the logarithm as the
only far layout without a built-in scale, the floor's remainder as address and not data, and H as a zoom that never
changes the count.

Three habits follow for a program:
- **Keep the pair.** Where a value is a direction, store [h : v] and divide last; division by zero is then the chart's
  edge, not a fault.
- **Ask whether an operation touches N.** If it does, it is a writing, and it will move when the world grows. If it
  does not, it is a reading, and nothing in the world can move it.
- **Run the scale test.** Multiply the world by k and see which outputs move. Those needed an amount carried in; the
  others never contained the world's size, and could not.

The writer's tools are not lesser for any of this. A blueprint, a schema, a sum, a known N: these are what let parts made
apart meet. But a program that reads a world it does not hold, a sky, a stream, a list with no end, is a reader, and the
geometry of a reader is K, not N.

---

## Sources

- Bernstein, A. J. (1966). Analysis of programs for parallel processing. *IEEE Transactions on Electronic Computers*
  EC-15(5), 757–763.
- Böröczky, K. (1974). Gömbkitöltések állandó görbületű terekben I. *Matematikai Lapok* 25, 265–306. (The binary tiling.)
- Boyd, J. P. (1982). The optimization of convergence for Chebyshev polynomial methods in an unbounded domain. *Journal of
  Computational Physics* 45, 43–79; (1987). Spectral methods using rational basis functions on an infinite interval.
  *Journal of Computational Physics* 69, 112–142.
- Cauchy, A.-L. (1821). *Cours d'analyse*. Paris, ch. 5. (The functional equation.)
- Gustafson, J. L. and Yonemoto, I. T. (2017). Beating floating point at its own game: posit arithmetic. *Supercomputing
  Frontiers and Innovations* 4(2), 71–86.
- Hastings, W. K. (1970). Monte Carlo sampling methods using Markov chains and their applications. *Biometrika* 57(1),
  97–109.
- IEEE (1985). *IEEE Standard for Binary Floating-Point Arithmetic*, ANSI/IEEE Std 754-1985.
- Kalman, R. E. (1960). A new approach to linear filtering and prediction problems. *Journal of Basic Engineering* 82(1),
  35–45.
- Karger, D. et al. (1997). Consistent hashing and random trees. *Proceedings of the 29th ACM Symposium on Theory of
  Computing*, 654–663.
- Knuth, D. E. (1998). *The Art of Computer Programming*, vol. 3, 2nd ed., §6.4. Addison-Wesley.
- Lamping, J., Rao, R. and Pirolli, P. (1995). A focus+context technique based on hyperbolic geometry for visualizing
  large hierarchies. *Proceedings of CHI '95*, 401–408.
- Metropolis, N. et al. (1953). Equation of state calculations by fast computing machines. *Journal of Chemical Physics*
  21(6), 1087–1092.
- Munro, J. I. and Paterson, M. S. (1980). Selection and sorting with limited storage. *Theoretical Computer Science*
  12(3), 315–323.
- Niven, I. (1956). *Irrational Numbers*. Mathematical Association of America.
- Polyak, B. T. and Juditsky, A. B. (1992). Acceleration of stochastic approximation by averaging. *SIAM Journal on
  Control and Optimization* 30(4), 838–855.
- Robbins, H. and Monro, S. (1951). A stochastic approximation method. *Annals of Mathematical Statistics* 22(3), 400–407.
- Sós, V. T. (1958). On the distribution mod 1 of the sequence nα. *Ann. Univ. Sci. Budapest. Eötvös Sect. Math.* 1,
  127–134.
- Williams, L. (1983). Pyramidal parametrics. *Computer Graphics (SIGGRAPH '83)* 17(3), 1–11.

The references are carried over from the archived companion, where they were checked when it was written.

The account this essay follows is *Reads and Writes* (`../readers-and-writers.md`): §6 ("K and N"); its passages on
computing are now a note, `plans/rw-computing-note.md` (a machine is built to do both acts, R641). The proofs are in the archived *Observation from Somewhere* and its computer-science companion
(`../archive/ofs/observation-from-somewhere-cs.md`), kept for reference: the corner and the registers in §3, the
separation in §5, the array in §6, the floor in §7, the two layouts in §8, detail and the fixed count in §9, the
blueprint in §10, the dial in §11, what comes free in §12. Where the companion's wording differs from the later rulings
(it speaks of "the reader's circle", of π/2 and 2/π as the reader's own, and says the word *writer* has nothing to do with a
memory write, which R613 qualifies), the rulings stand. The essays before this one: 3 (address and payload), 4 (thumbs past the corner, H as a zoom, K), 8 (the dial, the
depth buffer, the floor), 12 (what an array is, what a machine holds), 13 (where the plane's conveniences stop), 15 (what
only a writer holds).
