# Reads and Writes

**What one standpoint holds, what two standpoints place, and what a unit writes**

*Tom Brinkman. Rewritten 10 November 2026 (SPN R788) from version 17, which is kept unchanged as
`papers/archive/rw/reads-and-writes-record.md`; section numbers cited before 10 November are the record's. Written with AI
assistance (Claude).*

**How this paper is kept.** It is a working paper, the source of truth that AI sessions iterate on, not a text for
publication. So it is written as a specification. The definitions come first and are numbered (D1–D7); every later
section is checked against them. Claims are marked: **classical** (standard mathematics or physics), **checked** (exact
arithmetic or a measurement made here, listed under Code and data), or **reading** (ours: a way of dividing what is
known, not a result). "Checked" means the calculation is right under its stated assumptions and the code reproduces
it; whether those assumptions fit a physical system is a further claim, made case by case (§11). Each idea has one home; other sections point to it. Open questions are in §12. The propositions and
proofs this paper draws on are in *Observation from Somewhere*, archived (`papers/archive/ofs/`); where its wording differs
from this paper, this paper stands.

**One letter, Ω = π/2.** A read is one sweep, from home to the horizon, and the total of one sweep is π/2: the
weight ds/(1 + s²), the one weight that composing slopes leaves unchanged, summed over every slope from 0 up. π is two
sweeps' worth. Since the paper's subject is the single sweep, its constants are mostly π/2 and 2/π, and it is simpler to
give that total its own letter than to keep halving π: Ω = π/2, so 2/π is 1/Ω, the turn is 4Ω and the sphere 8Ω, the
Cauchy's coefficient is 1/Ω, and the corner has Ω/2 on each side. Ω and its inverse are to reads and writes what π is to the blueprint: 1/Ω is the
number for what turning sees, Ω the number for what walking counts (§9, "Reading is 1/Ω; walking is Ω"), and π, two
sweeps joined, is the blueprint's own. Both are limits, and they are the limits a read and a write actually encounter: 1/Ω is
what the thumb's share tends to as a sweep runs on toward the horizon, and Ω is what a count of the walk tends to,
stride by stride. No finite sweep and no finite count has either value, but each is headed for its own. π is a limit
neither encounters, since it takes both hemispheres at once. From here on the paper writes Ω where it helps and π where it does
not. One sweep is written in Ω: the half-Cauchy, the thumb's share, the arc in thumbs, the corner, e^(iΩ) = i. A whole
turn, a whole line and the classical statements keep π: the circle's 2π and π, the standard Cauchy's 1/π, the
Gaussian's 2π, Euler's e^(iπ) = −1, the parsec, Basel's sum, Lindemann's theorem. π is written too where the
blueprint's own number is meant, both hemispheres at once.

## Abstract

A point seen from a standpoint can be written, in the blueprint's notation, ln(z/H) = ln(d/H) + iθ, with H the thumb held out
at arm's length. Up is the direction; across is the distance, counted in thumbs. Against a unit outside the world the
across part has one more term, ln(d/metre) = ln(d/H) + ln(H/metre). Scaling the world, every length multiplied by one
factor (the observer's own thumb and stride with it), leaves the direction and the distance in thumbs where they were
and moves only that last term, the thumb in metres, by the same amount for every point. Two properties sort
what an observer has: whether it is continuous or discrete, and whether that scaling moves it. A **read** is continuous
and unmoved by scaling: the direction, [h : v], from one standpoint, its slopes spread by one density. Two looks held
together are still a read: the distance they give in thumbs, a **parallax extent**, an *extent* for short, is a
continuous ratio of their slopes (parallax). A **write** is discrete and moved by scaling: a bounded thing with a size, a
stone, a stride, a mark, a metre bar, and an amount put down in a unit carried in from outside, a metre or a second. The
write is the discrete, scale-variant companion of the read. The two mixed cases are tools of description: a count,
discrete and unmoved by scaling, and the number line in a unit, continuous and moved by it. Read and write are acts,
the verbs for the continuous and the discrete: there is no reader and no writer here. Every read is a *single hemispherical vantage*, one standpoint and one hemisphere; the *blueprint*, the drawn shape,
is the *dual hemispherical vantage*, both hemispheres at once, which no standpoint holds and which exists only as drawn, so it is neither a read nor a write. It is classical geometry, the view
from no standpoint, and it is in this paper only as a point of comparison: the paper is about reads and writes.

The read's directions are laid by the uniform turn, whose law in the reading v/h is the Cauchy: its median at the corner
v = h, its horizon never reached, no mean. It is best read as a *heat*, a continuous weight over the readings, hottest
along the look and given before anything arrives. What arrives along a direction is the *payload*, the paint. *The heat
is given; the paint is met.* A second test sorts them: change what arrives, and the directions and their heat stay
while the paint changes. Because the read adds nothing and a change to the paint moves no direction, reads never race.

The geometry has no memory, and its laws need none. A law, tangent addition or the exchange behind Euler's identity,
says what any two directions give together; it holds for every pair at once, and nothing in it happened. Memory is
needed only for which steps were taken, never for what steps do. So two things stand apart: the geometry, complete
with no memory and no unit; and writes, things with a size, where physics enters. A count kept of the steps taken is a
description laid over those writes. The blueprint's completed equations each have a read's form that is rational in
the slope and needs no limit: for e^(iπ) = −1 it is w(s)·w(1/s) = −1 with w(s) = (1 + is)/(1 − is), a direction and its
reciprocal, and at the corner i·i = −1 (§1, "The same relation, held two ways").

None of the mathematics is new. What is offered is a division of it: which parts one standpoint has, which need two, and
which need a unit, with the plane as the frame that holds the division in one line.

## 1. Definitions

**The room, without a ruler.** Stand in a corner of a room, look at each thing, and note where it is: so far round, so
far up. You have every thing's direction and nothing's distance; a room twice as large, seen from the same corner, gives
the same notes. That is a read. Take one stride along the wall and look again. Each thing's two directions cross, and
where they cross gives how far off it is, in strides: the room now has a shape and a size in your stride, and a room twice as large,
walked with a stride twice as long, gives the same extents. That is still reading, two looks held together, and nothing
in it has a size in any unit; the stride itself is a write, a thing with a size, and the number of strides a count laid
over it. Put the stride against a metre bar, and the room is
in metres; a room twice as large now gives numbers twice as large. That is a write.

**A read and a write.** Two properties sort everything this paper discusses. One is whether a thing is continuous or
discrete. The other is whether scaling the world, the thumb included, moves it.

*A read is continuous and unmoved by scaling.* From one standpoint, with the thumb held out as H, every direction has a
slope s = v/h, and the slopes are spread by one density, ds/(1 + s²) up to its total: the Cauchy density. Nothing in it
is bounded, nothing in it is counted, and it is the same over a world of any size. Two looks held together are still a
read: the distance they give, in the step between them, is a continuous ratio of their slopes,
1/(d/B) = 1/s₁ + 1/s₂ (§6), with no count in it.

*A write is discrete and moved by scaling.* It is a bounded thing with a size: a stone, a stride, a mark on a wall, a
metre bar. An amount put down in a unit, so many metres, is a write too: a mark, and a number of units that scaling the
world changes. A write is over once it is made, and it is used only by being read (§7). Reading is continuous, and what
is read is discrete.

| | unmoved by scaling | moved by scaling |
|---|---|---|
| **continuous** | reading: a read, and what reads held together give, an extent or a map | the number line in a unit |
| **discrete** | a count or an order, descriptions kept in writes | a write |

The top-left box is reading, not only a read: an extent (D3) and a map (D7) are had from reads held together, continuous and unmoved by scaling, and neither is a read (§4). The bottom-left box holds two different descriptions: an order, which read came first, is discrete and unmoved like a count, but is kept with no step repeated, so it is not a count (D7; O4). The other two boxes mix the properties, and both are tools of description. A count is discrete and unmoved by scaling:
the strides to the mountain are writes, and "514" is an account laid over them; what is kept of it is kept as things,
marks or pebbles, each a write. The number line in a unit is continuous and moved by scaling: a length as an exact real
number, the circle held whole at a size. That box is the blueprint, classical geometry, which this paper sets beside a read's
form for comparison; it is nowhere in the physical world. The blueprint is not one box: its amounts in a unit sit
here, and its completed ratios, π, e and the one-length circle, which scaling does not move, sit outside the table
(below, "Two verbs, two nouns"). The same holds of this paper's own terms: the slope, the
density's formula and this table are descriptions, and a read is described by them. When something will not sit on the
diagonal, the first thing to ask is whether it is a description. Heat and paint, used below, are pictures of the density
and of what is met along a direction, and the definition does not rest on them. **A reading**, offered as a way to sort;
it claims nothing about what the world is made of. The two tests (D5, D6) keep their work.

*Two verbs, two nouns.* Among acts the two properties are one. A discrete thing has a boundary, so it has a size, so
scaling moves it; a direction has no boundary and no size, and scaling has nothing of it to move. So reading is the verb
for the continuous and writing the verb for the discrete, and the scale test follows from that; it is not a second
definition. The two mixed boxes hold no act. A count and the number line are nouns, descriptions laid over what was
read or written. The friction between continuous and discrete shows wherever one is made to hold the other: a count
holding a read (a slope no fraction lands on, the ringing at a sharp edge, §6), a read holding a count (K, §5), and
parallax, where a walk is cut into strides before the reads at its two ends give a size. π and e belong to neither box
of the table's right column. Each is a pure ratio that scaling does not move, and a count reaches neither. They are how
the blueprint's three concepts are synthesized: both hemispheres at once, completeness, and no standpoint. π is the turn
completed, e the scale completed (§9, "What is free, and what Ω costs"). **A reading.**

- **D1. One point, two parts.** A point seen from a standpoint is, in the blueprint's notation, ln(z/H) = ln(d/H) + iθ, H
  the thumb held out at arm's length: up the direction θ, across the distance in thumbs. In space the point is d·u, u a
  direction, and the across part ln(d/H) is unchanged (§2). θ is the blueprint's coordinate on the direction, the one in
  which turns add; a read holds the direction itself, [h : v], or its slope s = v/h, and uses no trigonometry (§1,
  "A read uses no trigonometry").
- **D2. A read** is the direction: [h : v] in the plane, [h : v : v₂] in space, up on the plane. It is every sweep of the
  thumb at once, from one standpoint, *home*, at one moment, given whole (§3). A relation among the directions
  of one read, the separation of two of them, is of the read. The heat is the read's own measure on its directions,
  given with them and part of the read, not a further kind (§3). The paint met along a direction accompanies the read
  and is no part of it (§4). One read holds no distance. Its sweep runs from h to v on the thumb H alone, with no V in
  it, and stops at its horizon: a read closes nothing. Each read is orthogonal to every other, in the plain sense of
  independent: it stands by itself and shares nothing with them. No inner product is meant, and two reads can still
  be related from outside, by an extent, an order or a map (D7). Three words are kept apart. A *reading* is one direction's slope. A *read* is the whole of them from one
  standpoint at one moment. *Reading*, the act, is anything continuous and unmoved by scaling had with nothing kept.
  Two looks held together at once, with nothing kept
  between them, are still reading (D3), though they are two reads and not one; closing a circle, with its π and 2π, is a join of several (D7), and a join is not a read.
- **D3. A parallax extent**, an **extent** for short, is a gap across: a distance in thumbs, d/H, or one distance
  against another, d₁/d₂. Scaling the world
  leaves it unchanged, as it leaves a read; but no single look holds it. Two looks held together give it, as a
  continuous ratio of their slopes: parallax (§6), which is why it carries that name. So had, it is reading (two reads held together, not one read), not a third
  kind: two eyes have it with nothing kept and nothing counted. Counted out, so many thumbs or strides, it is a count,
  a description (above). Where one standpoint moves, the earlier look has to be kept to be there for the later one, and
  what keeps it is a write. It has two named cases: a *parallax distance*, d/H,
  along the line of sight, and a *parallax breadth*, V\*/H, across it. The word says how far or how large, not where: a
  read has no position (below, "Steps, never positions"), and an extent is not one either. In this paper "extent"
  without more is always in thumbs or steps; a size in a unit is a write (D4). The verb stays "to place": a step places
  a thing, and what it gives is an extent. V\*/H, a party's true breadth in thumbs, is an extent. An extent is a relation
  between standpoints and named things in space; not every number had from two reads is one (§12, O9).
- **D4. A write** is discrete and moved by scaling: a bounded thing with a size. A stone, a stride, a mark on a wall
  and a metre bar are writes. So is an amount put down in a unit carried in from outside the world: a metre, a second,
  a hertz, an agreed notch. The exact amount, a real number with no last digit, is the number line's, the blueprint's
  (§6, "Extents come by degrees"). For the geometry it is the across axis's zero tied to a unit, a distance in metres, and one such amount serves
  every extent hung from the same thumb (§7). A payload has writes too: a frequency in hertz, a brightness in watts.
  Scaling the world in a write's own dimension moves it (D5). A change of units is a different operation from scaling
  the world: it moves every write's number and no extent, no read as a read holds it (an angle in degrees is the
  blueprint's coordinate on a read, and its number follows the blueprint's choice of degree or radian).
- **D5. The first test.** Multiply every length in the world by k, the observer's thumb and stride included; the units
  stay outside the world. What moves is a write. Among the geometry's quantities, what stays is a read, an extent
  among them; a count of the observer's own strides stays too, and is a count.
  This is the geometric test, and it
  sorts the geometry. In general the test is a named scaling, one dimension at a time: multiply every amount of that
  dimension in the world by k, the world's constants of that dimension included, the unit staying outside. A quantity
  in another unit is tested by that unit's scaling: a frequency in hertz moves when every time is scaled, and its ratio
  to a rest frequency does not. Nothing here makes times follow lengths; a test that scales both says so. This is the old line of dimensional
  analysis between the scale-variant and the scale-invariant (Bridgman 1922; Buckingham 1914), a sorting by invariance
  under the scaling group, as Klein (1872) sorts geometries by their groups. **Classical**; the names are ours.
- **D6. The second test.** Change what arrives, keeping the standpoint and the turn: repaint the world, move the light,
  replace a wall by a row of trees. The directions and their heat stay; the paint changes. The first test does not do
  this work: a probability, or a ratio of two amounts, is unmoved by scaling and is still not a direction. The second
  test tells a direction from a ratio of payloads. It tests a candidate once its standpoint and its turn have been
  named, as D2 names them before anything arrives; it does not find a read in a bare number, and where no standpoint
  and turn can be named it cannot be run and nothing is concluded (§11). The direction it keeps is the direction of
  arrival at the standpoint: light bent on the way, by a lens or by refraction, changes which source paints a
  direction and moves no direction, and where that source lies is a further inference, the blueprint's. And the test
  sorts quantities, not causes: one cause can move both, as a boost moves where a star appears and the colour of what
  arrives from it (§4, "A moving sky"). The standpoint includes its state of motion where motion bears on what is
  read: a boost is a change of standpoint, so it is not among the changes of what arrives, and it moves the read. A
  relation between two standpoints that is not a distance is, where it carries one read's directions to the other's,
  a map (D7), and a number such as the rapidity is that map's coordinate, not a read (§4). Whether every such relation
  is an extent, an order or a map is not claimed and stays open (§12, O4, O9). A worked case, with
  everything named. The standpoint is a floor corner, the look along one wall; a red wall stands 3 m off, and one
  point of it lies at slope ½. Three candidates: that point's slope; its share h² = 4/5; and the brightness arriving
  from it over the brightness arriving from a second point at slope 2. Held fixed: the standpoint and the look.
  Changed: the wall is repainted blue, then taken away for a row of trees 10 m off. The slope is ½ and the share 4/5
  before and after; they are of the read. The ratio of brightnesses changes at each step; it is a ratio of payloads,
  though scaling the world never moved it.
- **D7. Joining and recording.** Joining reads, two standpoints or two moments, can give extents, orders or maps, not
  writes. These are distinct relations, told apart by what each is. An extent involves a gap in space (D3). An order is a
  relation with no cycle: which read is before which. A map carries one read's directions to another's, as a turn of
  the look or a change of motion does; it has an inverse, and maps compose. An order and a map hold no gap. A map's
  coordinate, a turn's angle or a boost's rapidity, is a representation of the map, not a further relation. This names
  the relation being formed; it does not say every relation between reads is one of the three (§12, O4, O9). A count of
  strides is a whole-number description of a ratio d/stride, an extent; the same count with the stride in metres is a write.
  A quantity's kind is what it is, not how it was had: an extent is a scale-invariant gap across, usually had by parallax,
  and a distance in thumbs handed over by another observer is still an extent. The kind attaches to the variable, not to
  its law: a Cauchy law on a direction's slope and a Cauchy law on the quotient of two amounts are two variables with
  one law, and the law alone does not say which is which. And a read is a direction, not a pairing of a direction with
  a source: which thing paints a direction is part of what arrives. Likewise an extent is a gap to a named thing, not to
  whatever is met along a direction. What is classified, throughout, is a variable: a quantity said of something named,
  this direction, that gap, this light's frequency. A relation between two variables is another variable and is put to
  the same tests; it does not inherit the kind of what it relates. A representation of a variable, its number in a
  coordinate, a count, a mark kept, has the variable's kind: an angle in degrees and a pixel's index are reads in the
  blueprint's coordinate and count. A count is neither a read nor a write. It is discrete, and no scaling of the world
  moves it: a count of steps taken, an extent put on paper in thumbs. The steps are writes, things with a size; the
  count is a description laid over them, and what is kept of it is kept as things, marks or pebbles, each a write. So
  keeping is done in writes, and physics enters with the first write, a thing with a size, not only with the unit. The
  geometry itself keeps nothing ("A law needs no memory", below).

**A law needs no memory.** The geometry keeps nothing, and yet it holds functions that describe the composing of any
number of steps: tangent addition, w(s) × w(1/s) = −1, Euler's formula. There is no conflict, because two things that
sound alike are different. *What steps do* is a law: any slope joined to any other gives a definite third, any slope
times its exchange gives −1. It holds for every pair at once. It is the whole table, given and not performed, and
nothing in it happened. *Which steps were taken* is a history: a tenth of a sweep, then a fifth, then three tenths. Only
the history needs keeping. Euler's formula looks as though it accumulates because the classical reading tells it as a
journey round a circle; the function holds no journey, only the rule, available everywhere at once. So the geometry can
say what a thousand steps would do without remembering one of them, and memory enters only when someone asks where a
particular sequence has got to. The laws are **classical**; that keeping is a separate act, done in writes, is a
**reading**. "Law" here means a geometric law only, a relation among the directions of one read. Laws in general
are many things (a physical law carries units and constants) and are not a third kind beside the read and the write;
the sorting stays the read and the write. That the geometry's laws are of this kind may be why the geometry needs
no memory: offered as a likely reason, not shown.

**A law in place of memory.** A geometric law is what the geometry has where an observer would need memory. An
observer who wants to know what a set of steps gives together must keep the steps and total them. The law holds the
answer for every such set at once, with none of them taken: it collapses the set into one relation. In that it does for
the geometry what a limit does for the blueprint, with one difference. The blueprint's limit is approached step by step and
its value (π, e) is had only at the end of a count without end (§9, "What is free, and what Ω costs"); the law is not
approached, it is given whole. So a geometric law is free in the same sense the geometry is: not an algorithm, not
computed, with no time in it. It can still be taken apart into intermediate steps, a slope joined to a slope, then to
another, or (1 + iθ/n)ⁿ step by step (§9), and that is how a law is understood and checked. The steps are the blueprint's
account of the law, a journey told afterwards; they are not the law, and the law does not wait on them. That the law
stands in for memory is a **reading**; what is free is the relation, never the value of Ω or e.

One expression does this for sequences without number. "n strides are one slide of n rungs" holds for every n;
w(s)·w(1/s) = −1 holds for every slope. What is collapsed is every sequence, of any length, at once, by an expression
that is finite and rational: not one endless sequence carried to its end, which is the blueprint's limit. Steps taken one at
a time are exact members of what the law describes, not approximations to it: strides compose exactly, ratios compose
exactly, turns compose exactly by tangent addition. And the expression leaves a place empty, the n or the s. The geometry
gives the expression and never fills that place; a read fills it (which slope, now) or a count (how many,
so far).

**What is kept is a count laid over writes.** In every case this paper works, what is kept comes to one thing: a count of a
repeated step, from a kept mark. A count of strides is that plainly: the strides are writes, each a bounded thing with a
size, and the count of them is a description, discrete, unmoved by scaling and not itself a write. A mark left at a start
is a write, and the count's zero. An extent
put down in thumbs is a count of thumbs. So the n in the law's empty place is a count, and it is what
turns a read into a size: on the walk the read times the count is the mountain in strides (§6, "Read times count"),
which neither has alone. Three limits keep this honest. The count is whole only in part: the house's corner is 514 and
two sevenths strides from its door, and the two sevenths is not counted but read, as the last part's ratio to a stride;
what is kept is a whole count and one more read. A count takes its step to be the same step each time, and
the geometry does not supply that: the law's rungs are exactly alike, a walker's strides only roughly. And a
count is held only in things, marks or pebbles, each a write; a number with nothing holding it is nowhere in the world. Nor is it claimed that every keeping is a count: an
order kept, which of two reads came first, is kept without a step being repeated (D7's orders; O4). **A reading**, resting
on WLK and ONE.

**A law shortens the chain of writes to its least, and the least is not zero.** A result can be built: read, keep, read,
keep, to the end. Or the law can be used, and most of the keeping is then not needed. On the walk the strides from the
corner to the foot, 514 of them for the house, need not be walked or counted: two reads one counted stride apart give
the strides left and the size (§6). The chain of reads between collapses to its two ends. What the law cannot do is
remove the last write. One standpoint holds no distance and no size (no read holds a distance, D3); a pace that counts nothing, the
fixed share, has the read at every moment and never the size (§6, "Read times count"). The least is one counted step.
So writing is not what establishes a relation, the relation holds unkept; and writing is not made unnecessary by the
law either. The law gives the expression; one write fills its empty place. This is said of finite chains. A law is not a
limit and reaches none: it covers every finite chain at once, and a limiting value such as π is the blueprint's at the
limit, never had by shortening. **A reading**, resting on WLK and ONE.

**A denominator is scaffolding.** Every reading is one thing in terms of another, and the other, the denominator, is
half of it: a reading with nothing under it is no reading. For a read the denominator is the thumb's share. Two things
are true of it together. Any size will do: 3 and 4 read against 1, 7, 1000 or 0.004 give 3/4 every time, which is the
first test seen from underneath. And it is never zero: where the thumb's share is empty there is no reading, only the
horizon. Within one read nothing comes down; the thumb's size was never in it. What comes down is the middle of a chain
of readings joined, a/b · b/c = a/c, where b was needed for both links and is in neither end (§6, "A tower of extents").
That is said by whoever keeps the chain, so scaffolding is a word for writes, and a scaffold put up and kept, a step
taken and counted, is a write with a count laid over it. The last "in terms of" never comes down: a/c is still in terms of c. Where a tower
ends is its kind: on the thumb, a read; on a kept step, an extent; on an agreed unit, a size. A unit is scaffolding
left up by agreement. A denominator leaves no mark on a number written down, so two readings on different denominators
can be joined by mistake: each of two people sees the other smaller, in terms of its own hand. Dividing one such reading
by the other takes down the distance they share and leaves their sizes against each other; multiplying takes down the
sizes and leaves the distance (*Each Sees the Other Smaller*, Code and data). **A reading**; the arithmetic is exact. The older statement is the archive's centring (*Degrees of
Freedom* §3.1), taken here without its Roman arch.

| | memory | unit |
|---|---|---|
| the geometry: reads, and the laws relating them | none | none |
| a count: which steps were taken, a description kept in writes | yes | none |
| a write: a thing with a size, an amount in a unit; physics | yes | yes |

**The same relation, held two ways.** The central example of this paper is Euler's identity. The blueprint states it as
e^(iπ) = −1: an exponential, the number e, and a half turn measured as π, each of them a limit (marked the blueprint's, §9).
The relation it states is already present in a form that uses none of the three. Write a direction of slope s = v/h as
w(s) = (1 + is)/(1 − is). Then for every slope

  w(s)·w(1/s) = −1,

by ordinary algebra: a direction and its reciprocal compose to the half turn. At the corner the direction is its own
reciprocal, w(1) = i, and the relation is i·i = −1, two corner steps, exact. Every member with 0 < s < ∞ is a pair of
directions of one read. The one member that is not is the pair home and horizon, s = 0 and 1/s = ∞: no read holds the
horizon, so that member is the blueprint's, and it is the one the classical equation names, which is why it is the one
that carries Ω. The circle, the quarter turn's two numbers and the Cauchy's total go the same way, each with a form
rational in s about the exchange s ↔ 1/s and the corner (§9, "Four identities, one exchange"; parallax and the Gaussian
beside them in "What is free, and what Ω costs"). Three limits on what is claimed. The algebra is **classical** and the
two forms are equivalent; saying which form a read holds is a **reading**. The simpler form exists for relations among
the directions of one read; positions, closures and totals are not done more simply by a read, they are not done
("Steps, never positions", next). And nothing here says the classical statement carries anything it should not: the
blueprint's form holds the join completed, which the read's form does not have.

**Steps, never positions.** A sweep goes one way, from home toward the horizon, and where it stops is the next
sweep's home: every sweep resets. A tenth of a sweep, then a fifth of a fresh one, then three tenths of another, is
three steps, each from its own start. Nothing in any of them says how far the three have come together. A position,
"three fifths of the way round", is a total of steps from a starting mark that was kept, and a read keeps no mark.
Going back is open: the observer faces the other way and sweeps, and that too is a forward sweep, in the
opposite facing. What it cannot do by reading alone is go back exactly to where it was. For that the steps must
have been kept and totalled, or a mark left at the start: a write, with a count laid over it (D7). Without it the observer goes back
some way and has no means of telling when it has arrived. This is why an angle, the turn's whole measure and
the arctangent sit together on the blueprint's side: each is a position, a total from a kept mark, where a read
has only the step it is in and the heat along it. There is no circle anywhere in this. A circle is one fixed dial on
which every sweep has its place and going back is going the other way round; a read has no such dial, only a
sweep forward, a reset, and another sweep forward. The circle appears when someone keeps the steps and lays them end
to end. That keeping is a write. The circle held whole, with no standpoint in it, is the blueprint's.

**A read uses no trigonometry.** A read is in v/h; angles are the blueprint's. The claim is about named operations, not every construction: composing slopes, the exchange, the corner and the equal halves are rational in s; the shares h and v and the halving of a turn take a square root; a total or an angle takes a limit (§9's three grades). Sin, cos, tan and arctan are the blueprint's: they are defined on the completed turn,
whose period is π (§2), and evaluating one is a pass over that whole turn. A read holds the turn open, and works in the
slope s = v/h: a direction is [h : v]; two turns compose by tangent addition, (s₁ + s₂)/(1 − s₁s₂); the reciprocal is
s ↦ 1/s and the corner s = 1; the heat is 1/(1 + s²) per unit of reading, 1/(2π(1 + r²)^(3/2)) per unit of a screen
square to the look; a turn of twice the angle is (1 + is)/(1 − is). In the plane all of it is rational in s. The one step
that is not, √(1 + s²) = 1/h, is the circle entering, its measure h² + v² = 1: with it a turn can be halved,
t = s/(1 + √(1 + s²)) = v/(1 + h); without it it cannot (from the corner, rational steps reach only the quarter turns, and
the next place, √2 − 1, needs the root). So doubling a turn is the read's and halving one the blueprint's, as halving a
ratio, s ↦ s/2, is the read's (SLP). In space the root comes in even for the heat: per unit of a screen it is
h³ = (1 + s² + s₂²)^(−3/2), the circle's measure in the heat itself. Where this paper writes θ, an angle, or a trigonometric function, it speaks
of the blueprint: the angle is the chart in which turns add and theorems about the whole turn are already proved, the slope
the chart in which the read's operations run. The two are one projective line in two coordinates, joined by the
half-angle, s = tan(φ/2) for the blueprint's angle φ of total 2π (or s = tan θ for θ of total π); putting s = tan φ in its place
moves every result. This is draw's *Tangent Bridge* (its classical presentation, `tb_classical.md`, and its algebraic one,
`tb_algebra.md`): the reconstruction proved in the angle chart and run in the slope chart, with no trigonometric call.

Two independent questions sort the geometric quantities, those about directions and distances from standpoints: does
scaling the world move it (D5), and does one standpoint hold it (Proposition 8 of the archived paper: no read holds a
distance). The table is for those. A ratio of two payloads at one standpoint, one colour channel over another, is unmoved
by scaling and needs no second standpoint, yet it is not a direction of the geometry: it is a direction in the payload's
own space (§4), and D6, not this table, sorts it.

| | moved by scaling? | held by one standpoint? | kind |
|---|---|---|---|
| a direction [h : v] (up) | no | yes | read |
| a gap across: d/H, d₁/d₂, V\*/H | no | no: two looks held together | a read (an extent) |
| the across zero tied to a unit | yes | no | write |

Read and write are so the named outcomes of two tests that cross, and the crossing has a fourth box, the
payload's:

| | the geometry: stays when what arrives changes (D6) | the payload: changes with what arrives (D6) |
|---|---|---|
| unmoved by scaling (D5) | a read (one standpoint), with its heat; an extent (two, a gap); an order or a map (two, no gap) | a ratio of payloads: one colour channel over another, a probability of what arrives, a frequency over a rest frequency |
| an amount in a unit (D4), moved by its own dimension's scaling | a write: a distance in metres | a write: a frequency in hertz, a brightness in watts |

A write is found in both columns; a read and an extent are the geometry's alone; a ratio of payloads is the payload's
counterpart of a read, unmoved by scaling and not a direction of the geometry. Being unmoved by scaling therefore never
shows that a quantity is a read. One thing can supply several variables of different kinds: a pixel's value in the
sensor's unit is a payload's write, its ratio to its neighbour a ratio of payloads, the pixel's position in the grid a
count of directions, a description.

**Reads, writes and the blueprint.** There are reads and writes; there is no reader and no writer. Both are acts, and
one observer does both: it reads while it stands and turns, and writes while it strides, leaves a mark or agrees a unit. A
read is a single hemispherical vantage, one standpoint and one hemisphere, and there are two of them, the two sweeps: the inscribed, from home to a horizon
(1/Ω, the limit it approaches), and the central, across a bounded thing to its rim (Ω, the limit a count of its arc tends to, the end itself reached at a point). Both
are reads. A write is a bounded thing with a size, a stride taken, a mark made, a unit carried in (D4); it is how a read is carried to a later
read. Two looks held together are joined with no write. Neither a read
nor a write holds both hemispheres. What holds both at once is the **blueprint**: the drawn shape, with both signs of every axis, the turn completed, the
facings joined. It is the dual hemispherical vantage, and it exists only as the blueprint: no standpoint holds both hemispheres, so the blueprint is drawn, never stood at. Reads and writes are what is done from a standpoint, so the blueprint has nothing to do
with reads and writes: it is not a third act beside them, not a read of a larger kind, and not what they add up to.
It is classical geometry, with its eye above the figure seeing every side at once. This paper is about reads and
writes; the blueprint is brought in as the point of comparison, the familiar statement a read's or a write's form is
set beside (e^(iπ) = −1 beside w(s)·w(1/s) = −1), and no result here is a result about it. "Dual hemispherical vantage" and "from no standpoint" say the same thing: a standpoint faces
one way, so both hemispheres at once can only be drawn. The circle held whole, the sphere and the cube, the angle and trigonometry, π and e
are the blueprint's. Whole, with π at its exact value, it is a limit. So this paper says "a read", "a write" and "the blueprint", and "the observer" where someone has to stand,
walk or count.

**V.** V is the other party's breadth, the mountain in the distance that the thumb is held up against. A reading is a
ratio of the thumb's own shares; V was never in it, and it does not "cancel" from it. V\*/H is an extent, had by walking;
V in metres is a write, had by walking and a unit. Neither is a shortcoming of the read: the horizon, the corner as a
median and the absence of any mean are what a read with no breadth in it is.

**Four things: the universe, an apple, a human and a sheet of paper.** Two reads, a thing held and turned and, for comparison, the blueprint, and where V stands in each.
- *The apple and the human read the universe by the inscribed sweep.* From home to a horizon: directions only, a turn
  that never ends, 1/Ω the limit it tends to, never reached. The universe has no far side to face, so its V
  is **unknowable**: no size could be had, and with none there is no inside or outside, only home and the horizon.
- *The apple and the human face each other as bounded things.* From a distance each one's paint stops at a finite slope
  in the other's look: its rim, one direction inside the read like any other, not the horizon. That is what the universe
  lacks, an end that can be walked to. The sweep that has that end is the central one, a read across one hemisphere from
  the bounded thing's own centre (the pivot of Euclid III.20): its end is reached at a point, e^(iπ) = −1, and Ω is the
  limit a count of its arc tends to. The observer at a distance is not at that centre. It meets the same −1 in its own
  read only by walking to the rim, where at contact the slope runs out to the horizon (§6, "Two ways to arrive"). So the
  other's V is **knowable**: the end exists and can be met. It is not known, since the far hemisphere stays turned away;
  each holds the other's front only.
- *The human holds the apple and turns it.* The turn makes the Cauchy: a uniform turn, read as the slope v/h against the
  line of sight, is the Cauchy whatever the apple's shape, the shape only the paint. The hand holds the back as the eye
  holds the front, so both hemispheres are in reach and the turn is known; the apple is a thing with a size, held, and in the hand
  the apple's V is **known**: held whole. Its amount in a unit needs a unit carried in, and its exact amount is the limit of §6.
- *The human draws a circle on paper.* This fourth is the comparison, classical geometry's circle. The drawing is the blueprint, the dual hemispherical vantage: both hemispheres at once, held from no standpoint and so with no facing, neither read nor write, whole
  only at its limit (§9, "What is free, and what Ω costs"), made, not seen, a mark holding both halves together, V = H at one length, π held whole. It has neither sweep's
  number. Ω and 1/Ω belong to the two facings, the central reached at a point and the inscribed approached; the blueprint
  has the number 1, the thumb in thumbs. The product of the two reads' numbers is also 1; that is arithmetic, not a way of making the blueprint from reads.

| | hemispheres | vantage | V | the blueprint's number for it | what it is |
|---|---|---|---|---|---|
| inscribed, toward the universe | one | home, facing a horizon | unknowable | 1/Ω, approached | a read: what turning sees |
| central, toward the apple | one | the apple's centre, across to its rim | knowable | Ω, the limit a count of its arc tends to; the end reached at a point | a read about a bounded thing; from afar its rim is one direction, met at −1 by walking; its arc, counted in thumbs, is an extent |
| the apple held and turned | both, in reach | one, the turn known | known, held | the turn's Cauchy | looks joined by a known turn, of a thing held in the hand |
| the blueprint | both at once | dual, drawn; no standpoint | known | 1 | neither read nor write: the dual hemispherical vantage |

The human is all of these at the same time, not by turns: it reads the universe, faces the apple and is faced by it, and
what it holds in the hand or draws it holds as a blueprint. The apple has the facings and never the blueprint. So Ω · 1/Ω = 1 is
not two parties meeting but one observer's two reads held at once, and the 1 is its own thumb given back.

Faced, V is knowable, not known. The inscribed sweep approaches its horizon without end; a bounded thing puts its rim
inside the look, one direction that the central sweep, about the thing's centre, reaches at a point and that a walk
carries to −1 at contact. Only a write holds V whole; parallax narrows the band toward it and never closes it (§6). Euler's identity is the hinge: the
turn's end, endless in the read's chart (s → ∞), is one named point, −1, in the central one, and a named point is what
can be carried onto the blueprint.

**Reads do not conflict.** A read adds nothing, so reads of one geometry can be taken in any order, or all at once, and
they agree; a conflict needs something written where something else reads. In computing this is the condition for
running operations together without a race (Bernstein 1966). Here it holds by construction: nothing writes to the
geometry, and a change to the paint moves no direction and no heat (D6). A system whose addresses move with their
contents (an array that reallocates, a table that rehashes) has to rebuild that separation by hand. **Classical**
(Bernstein's conditions); the application is a design argument, not a proof.

**Words used throughout.** These carry over from the rulings and hold in every section.
- When H comes up, name the thumb.
- A read's far field is said in ratios: a thing one thumb wide reads one in two, one in four, one in eight. Counted in
  thumbs, two, four, eight thumbs out, it is an extent. Never "doubling" or "level".
- A read has a vantage, never a shape: no circle, no sphere, no body.
- There is no reader and no writer, only reads and writes; a read is the single hemispherical vantage, and what holds both hemispheres at once is the blueprint, the dual hemispherical vantage, which exists only as drawn. Where
  someone has to stand, walk or count, say "the observer".
- A read is continuous and unmoved by scaling; a write is discrete and moved by it; a count and the number line in a
  unit are descriptions. Definitions are stated on those two axes.
- *Heat* and *paint* are pictures, for the read's density and for what it meets, and are not leaned on; *address* only as a computing metaphor or for a count of K
  places at the heat's quantiles (§5).
- Ω and 1/Ω (defined before §1; Ω = π/2) are the limits the two reads encounter, each a single hemispherical vantage: 1/Ω the inscribed
  sweep's, Ω the central sweep's (its arc walked and counted is an extent; §9, "Reading is 1/Ω; walking is Ω"). Ω
  and the one-length circle are the blueprint's: the dual hemispherical vantage, from no standpoint, nothing to do with reads and writes.
- The Cauchy has no near and no far; H lays them over the read as an overlay (§5).

**Continuous and discrete.** A read is continuous: a turn passes through every direction between two, and nothing in it
is counted. A count, of strides, of units on a ruler, of digits, is discrete, with a next and, if finite, a last. A write is
discrete too, a bounded thing; a count is a description laid over writes, and unlike them is unmoved by scaling. The blueprint's continuous things, the real line, the circle held whole, Ω and e, are
counts carried to their limit and held as finished, so there are two continuities: the read's, never counted, and the
blueprint's, a count completed. These are the acts idealized: a sensor that samples has already counted, and no real
instrument is a pure read; what the paper offers real instruments is the two tests, quantity by quantity (§6, "Turns,
counts and corners").

## 2. The plane

**The equation.** Divide a point by the thumb and take the logarithm: ln(z/H) = ln(d/H) + iθ. Drawn with the direction
up and the distance across, it is Euler's plane. A turn of the world slides every point up or down. Changing the thumb
alone by k slides every point across by ln k; the two slides commute. Scaling the world, the thumb with it, moves no
point of this plane at all. What it moves is the plane's place against an outside unit: ln(d/metre) = ln(d/H) +
ln(H/metre), and scaling adds ln k to the last term only. So:

- **Up is the read.** The direction [h : v], and every difference of directions. The blueprint draws it at θ, where turns
  add; a read holds its slope s = v/h, and two turns compose as s₁ ⊕ s₂ = (s₁ + s₂)/(1 − s₁s₂), the angles'
  addition with no angle in it.
- **Gaps across are extents.** ln(d₁/H) − ln(d₂/H) = ln(d₁/d₂), and ln(d/H) itself, a distance against the thumb, since
  the thumb scales with the world. A slide across keeps every gap.
- **The across axis's zero, tied to an outside unit, is the write.** ln(H/metre) is the one number scaling the world
  moves.

Anyone who has pinched and twisted a map on a phone has done both slides: the phone takes the line between the fingers
after over the same line before, k·e^(iα); the real part of its logarithm is the pinch, the imaginary part the twist.
**Classical**; the reading of the parts is ours.

**Each axis has a zero, and the two are not alike.** Up, the zero is home, s = 0 (the blueprint's θ = 0), where the direction lies along h.
Across, the zero is the thumb, d = H. Both are the read's: home is where it faces, the thumb what it holds out. The
axes differ in how they end. Up closes: within one read it runs from home to a horizon a quarter turn off, never reached,
and it wraps (θ and θ + 2π one place) only when turns are joined. Across is open both ways: no total, no natural size,
nothing on it marking a place but the thumb. That is why no read and no extent gives the overall size: there is no mark on
the open axis to read it against, until a unit is carried in.

**The two corners are the plane's two mirrors.** The horizontal line s = 1 (the blueprint's θ = 45°) is fixed by the reading's reciprocal,
s ↦ 1/s; the upright line d = H by the distance's, d ↦ H²/d. Turning moves the first, choosing the thumb moves the
second, along different axes. On the blueprint's plane every straight line of the world is one curve moved,
u = ln(p/H) − ln cos(θ − φ₀), half a turn wide, and a logarithmic spiral is a straight line. **Classical.**

**The thumb's lay is itself a turn.** The overlay's lay of distance (§5), the share g of the heat 1/(1 + x²) lying below x = d/H (the blueprint's formula for it
is (1/Ω)·arctan(d/H)), is on the plane
½ + gd(ln(d/H))/π, gd the Gudermannian, Mercator's function. A blueprint shows why. Put the plane on a sphere
stereographically, scaled so that one thumb lands on its equator: the eye is one pole and the horizon the other, the near
field the eye's half and the far field the other; g is the angle from the eye's pole over π. Euler's plane is that
sphere's Mercator chart; d ↦ H²/d is the reflection in the equator, and sech(ln(d/H)) the cosine of the latitude.
Turning the world turns the sphere about its axis; taking the thumb k times larger slides every latitude toward the
eye's pole, tan(χ′/2) = tan(χ/2)/k, the boost of rapidity ln k that a moving sky applies to directions (§4), here applied
to distance. The two motions commute, which is why both are slides on the plane, and Jaynes's dθ·dκ/κ, the measure that
suits the read's two ignorances, is the plane's area. The sphere is the blueprint's drawing: its own even measure, area,
is not the read's, which per unit of the sphere's area runs as 1/sin χ, χ the angle from the eye's pole. **Checked** (to
thirty digits; `euler.html`).

**π with the direction, e with the distance.** The read's two ignorances, after Jaynes (1968), are which way it faces
and how large things are: turns and rescalings, each a one-parameter group with an exponential map. Turns close, so
their map has a period: 2π for an oriented turn, π for the direction of a line (the projective line the readings live
on). Rescalings never close, so their map has no period, only a base. π is what is needed to say that the turn comes
back, a period forced; e is the base that lets one unit serve both axes, so that e^(iθ) is a turn of θ and e^t growth
at a rate of one, a convention (counting in thumbs serves as well). Both numbers are the blueprint's; a read meets the
closing and the openness and states neither. They meet at e^(iπ) = −1, where the square (h + iv)² = e^(2iθ) sends the
far end of the sweep, the horizon a read holds as the finite pair [0 : 1]. Through that meeting Lindemann proved π (and so Ω)
transcendental (1882). **Classical**; the assignment to direction and distance is a reading.

**The paper in one equation.** Write the sphere's equation, three lengths about a centre: x² + y² + z² = r². Kept as
written it is the blueprint's: lengths held, a radius, a closed surface, every sign; scale the world and every term moves
against a fixed unit. Divide it by the thumb's own share, x²:

  1 + s² + s₂² = (r/x)²,  s = y/x, s₂ = z/x.

What is left is two ratios, unmoved by scaling, and nothing closes: where the sphere would have met itself, s runs to
infinity, the horizon. The left side is the denominator of the two-dimensional Cauchy, 1/(2π(1 + s² + s₂²)^(3/2)), the
even turn's heat on a screen square to the look (§3): its corner s = 1, its horizon s = ∞, a median and no mean. The
sphere has a shape, a size and a boundary that closes; dividing by the thumb takes the size away and opens the surface
along the rim, 90° off the look, and what is left is heat thinning outward with a tail that never completes. In the plane
Euler's formula says the same: the blueprint's point x + iy = r·e^(iθ), divided by the thumb, is the reading
1 + is = sec θ·e^(iθ); divided once more by its mirror, (1 + is)/(1 − is) = e^(2iθ), every length is gone and the horizon
lands at −1. What the equation leaves out is the paint (D6). **Classical**; the reading is the paper's.

The same equation shows what a denominator does. In the plane, x² + y² = r² can be taken in terms of three things. In
terms of a unit it is the circle as a size: 9 + 16 = 25. In terms of the pair's own size r it is the circle as shares,
h² + v² = 1: 0.36 + 0.64 = 1, and it closes exactly because both shares were read against one denominator; the equation
is the receipt of that. In terms of the thumb x it is 1 + s² = (r/x)², one slope, and its right side turned over is the
heat h² = 1/(1 + s²). So the circle and the Cauchy are one equation in terms of two different things from inside it. In
each the denominator's size is in no result: (3, 4), (21, 28) and (0.03, 0.04) give the same shares and the same slope.
They differ in cost: the slope needs only the two lengths against each other; the shares need r, a square root (§9).

**In space the plane parts.** The across part survives: space laid out by ln(d/H) beside the direction is a line times
the sphere of directions, and scaling moves only the line's coordinate and commutes with every turn. The read's heat can
still be laid flat, on Lambert's equal-area map about the look, and every turn of the look keeps it flat. What no flat
chart does is keep the turns rigid: turned by φ, Lambert's chart is stretched by 1/cos(φ/2) at the old look and by up to
2 at a quarter turn, while the stereographic chart keeps the angles and loses the heat, a quarter as hot at its rim. No
chart of a sphere keeps both (Gauss 1828; Euler 1777); the plane's one chart does both because a line times a circle is
flat. Turns of space stop being slides (§8). **Checked** (FLC).

**Two geometries, and where physics enters.** *The read's geometry* has no length in it: directions from one standpoint,
shares of one thumb, the corner, the horizon, the Cauchy, order. Classically it is close to the geometry of the lines
through one point, projective geometry seen from a standpoint (incidence, order, cross ratio, no length), with a home and
a corner of its own (Klein 1872). It can be reached two ways: as lines through the origin of a plane with the scale
divided out, the blueprint's route; or from incidence and order alone, with no length to set aside (von Staudt 1847), the
read's. Extents, had by two looks together, add gaps across, still with no unit: the shape and size of a room in the step between the looks. *Physical geometry* has
the unit: lengths and sizes in amounts, the blueprint's cube with a number line on each axis, x² + y² = r² with r in
metres. Physics enters with the write, a thing with a size, and a unit is a write carried in: it injects physics into a relation. The two are orthogonal. The
geometry is complete without physics: every read, and every relation among reads, stands with no unit anywhere; and
physics, when it enters, assigns amounts and moves none of them. Picture reality as a sheet of paper
every physical thing writes on, a stone's mass, a planet's path, a cell dividing, each in amounts. A read adds nothing to
the paper; its directions and their heat are laid over it, blank or full, and the light that arrives along them is the
paper's writing met there. This says where physics sits in this frame and tells physics nothing it does not know.
**Reading.**

## 3. Up: the read

**What a read is.** A read is every sweep of the thumb at once, from one standpoint, at one moment. A sweep is the one
length a read holds, H, turned from all of it lying along h to all of it standing along v; the read is every such
sweep given whole, not performed one after another. H can be any value; it sets only the zoom (§5). A reading is one
direction met in the sweep, [h : v], charted as v/h, h and v each a share of the thumb between 0 and 1; the projection
from home divides, not a read. Each sweep is centred on the crosshairs, where the thumbs cross (§5). A read holds no
time: time, like distance, is a gap between reads, and a single read carries nothing from the one before. Geometry is
free in this sense: nothing in it is computed, no procedure runs; tan, arctan and every formula for the turn are the
blueprint's way of stating what is already there (§9). A companion paper, *The Tangent Bridge* (reportbase/draw), proves the
split in the angle chart and runs it in the slope chart with no trigonometric call.

**The thumbs pointed; a vantage, not a shape.** The crossed thumbs are pointed at the mountain, and that pointing
gives its geometry: the corner where the thumbs cross, the fingers spread from it, near and far read as ratios of the
thumb. Drawn out whole, a length held and turned about one end traces a circle, and the blueprint calls it
V = H, the thumb equal to the mountain: the *one-length circle*, held whole, with a circumference and an area. A read
does not draw it. Circles and spheres are a line's whole turn held at once, the blueprint's. A read has a standpoint and
the turn from it; walking round a shape, it gets extents, and with a unit it writes (§6, §7).

**The uniform turn.** A turn measured by itself is uniform: equal turns, equal shares. In the reading s = v/h the
uniform turn over a quarter turn has the law

  (1/Ω) · 1/(1 + s²),  s ≥ 0,

the half-Cauchy. Its median is s = 1, the *corner*, where v = h; its quartiles √2 − 1 and √2 + 1; its far end, s = ∞,
the direction [0 : 1], the *horizon*, reached by no finite reading. It has no mean: averages of readings climb without
settling, by (1/Ω)·ln 10 for every tenfold further the readings run. Given the uniform turn this holds whatever is looked
at, a straight wall, a row of trees, a curved hill, an empty sky; the wall's shape only decides where each direction
meets it. The constant 1/Ω and the quartiles' values are the blueprint's arithmetic; a read has the order of its
readings, the corner and the directions. **Classical.**

**Why there is no mean.** A mean is a sum of amounts over their count. The Cauchy weighs directions, and a direction has
no length to add; its number is a chart, and the question is what survives a change of chart. To average v/h is to take
each direction as an amount on a line, the chart in which the horizon sits at s = ∞, and the sum picks up that chart's
far end. Other charts of the same directions have means (the bounded chart s/(1 + s) averages ½), and the order
statistics do not depend on the chart: the median and quartiles commute with every increasing map of the reading, a mean
does not. So the median is the directions' and the mean the chart's. A mean of directions is well defined once an embedding is
chosen, and choosing one is the blueprint's step: unit vectors
over the uniform quarter turn average (1/Ω)(1, 1), pointing at the corner, of length √2/Ω ≈ 0.900. And a world capped at
a bound M has a Cauchy with a mean, (1/π)·ln(1 + M²) over the share below M, about 8.8 at M = 10⁶: set by the bound, an
amount written in. The payload, where it is an amount, averages (§4). Practice already takes the median of a Cauchy and
never its mean; this is the reason. **Classical**; the reason is a reading.

**The Cauchy from one length, from two axes, from a line in the world.** The family has a location m and a scale γ.
Derived from what is held, it comes in three forms.

- *One length turned.* The tip of H turned uniformly is at (H cos θ, H sin θ); the reading v/h = tan θ has no H in it.
  The share passed before the reading reaches s is, in the blueprint's account, (1/Ω)·arctan s: the standard half-Cauchy,
  scale 1, median at the corner. The scale is 1 because a reading is a ratio, and a ratio carries no scale.
- *Two axes drawn.* Draw the second axis at a length V of its own: the point (H cos θ, V sin θ), the reading
  (V/H)·tan θ, a Cauchy of scale c = V/H, its median at c. Scaling leaves c unchanged, so c is an extent, not a write; but
  it needs two lengths held against each other, as √2 needs the square's two sides.
- *A line in the world.* A lamp turning uniformly lights a shore at distance d; its landings x = m + d·tan θ follow
  C(m, d), quartiles m ± d. In metres both parameters are writes. The angles follow the uniform turn whatever d is; the
  scale appears only when the landings are laid on a ruler along the shore.

The ratio of two zero-mean normal amounts gives the same three: equal spreads (the first), spreads σ₁ and σ₂ (scale
σ₁/σ₂), and the two correlated by ρ (a location, ρσ₁/σ₂, the scale then (σ₁/σ₂)·√(1 − ρ²)). With means away from zero
the ratio is no Cauchy at all.

| form | what is held | scale | location | kind |
|---|---|---|---|---|
| one length turned | H | 1 | 0 (the corner) | read |
| two axes drawn | H and V | V/H | 0 | an extent (two lengths held) |
| a line in the world | the line's place | d | m | writes, in a unit |

So V enters the Cauchy as its scale, and only there. The point m + iγ that indexes the family is the standpoint's place
with respect to the line; the read's ignorance is turns and rescalings, never translations, so in its own chart it
stands at i, foot 0 and height 1, and holds the standard Cauchy. Moving the standpoint is walking (§6). **Classical**;
the sorting is a reading.

**The circle's equation, divided by its own length.** The blueprint's circle holds amounts: x = H cos θ, y = V sin θ,
(x/H)² + (y/V)² = 1, round only when V = H, then x² + y² = r². Divide the round circle by x²:

  1 + s² = (r/x)² = sec²θ,  s = y/x.

The density is the share squared, 1/(1 + s²) = (x/r)² = h², and ds = sec²θ·dθ, so dθ = ds/(1 + s²): the uniform turn,
read as s, is (1/Ω)·1/(1 + s²). The Cauchy is the circle's equation used to carry an even turn into readings. (The
division is the blueprint's account, not something the read does.)

| | the blueprint's circle (with V) | the read's Cauchy (without V) |
|---|---|---|
| a point, a reading | (H cos θ, V sin θ), amounts | s = tan θ, a ratio |
| the equation | (x/H)² + (y/V)² = 1 | 1 + s² = sec²θ |
| the law | none needed: every point stated | (1/Ω)/(1 + s²) = (1/Ω)·h² |
| what it states | the area πHV, the circumference, points | the median 1, quartiles √2 ∓ 1, the horizon, no mean |
| if V ≠ H | an ellipse | a Cauchy of scale V/H |
| the world scaled, against a fixed unit | everything moves | nothing moves |

**The standpoint and its closure.** Change the turn's standpoint and the directions move as a family: the Cauchy is
carried into another Cauchy, its centre and width the new standpoint's foot and height, m + iγ. This closure, under the
real Möbius maps of the reading (changes of standpoint and of chart), is the law's own. Not every operation on directions
keeps it: an amount entering, an edge, a square, a sum of amounts, breaks it. So the Cauchy here is not a law of what is
measured; it is the law of the uniform turn, the heat over the read's directions. A Cauchy met elsewhere, a resonance's
line, a ratio of two normal amounts, a stable sum, may have another origin; whether a turn lies behind it is a question
to ask of each case (§11). **Classical**; the reading is ours.

**The Cauchy's routes.** Every Cauchy is one measure: the Poisson kernel of the upper half-plane seen from a point
z = m + iγ, p(x) = (1/π)·Im 1/(x − z), the harmonic measure of a line seen from a point off it. The circle and the point
off the line are one construction in two coordinates: centre the line at the foot and scale it by the height,
u = (x − m)/γ; the Cayley map w = (1 + iu)/(1 − iu) = e^(2iθ), θ = arctan u, takes the line to the circle, and the
circle's even angle, returned to the line, is dθ/dx = γ/((x − m)² + γ²); divided by π, that is p. Many mechanisms put a
point at z and reach the line from it:
- **a uniform turn read on the line**: the lighthouse, the ratio of any rotation-invariant pair, a circle seen from a
  point of it;
- **a random walk** leaving the half-plane from z (Kakutani 1944), and its twin, a normal mixed over the walk's hitting
  time;
- **a pole** a height γ off the line, p(x) = (γ/π)·|1/(x − z)|², whose Fourier pair is e^(imt − γ|t|) (§9);
- **a sum** of Cauchys, whose points add;
- **a real Möbius map**, carrying one point to another.

In the plane these are one measure, since a turn about z preserves harmonic measure; on a flat boundary they agree in
every dimension; on a curved one they part (inside a ball the straight turn and the walk land differently). One sample
never tells the routes apart; only what γ tracks can (a distance for the turn and the walk, a rate for a pole, a sum for
a sum), and the boundary's shape. So the turn does not own the Cauchy; it is the read's route to it. "Find the turn" is,
more generally, "find the z". A fat tail with no z is not harmonic measure by any route. **Checked** (CRT); classical.

**How far apart two standpoints are.** The standpoints z = m + iγ form the hyperbolic plane, and the family
carries it as its measure of distinguishability: the Fisher metric of C(m, γ) is (dm² + dγ²)/(2γ²), half the Poincaré
metric, and the divergence between two members is 2·ln cosh(d/2), d their Poincaré distance in the upper half-plane, the one with
ds² = (dm² + dγ²)/γ² (Chyzak and Nielsen give
the closed form). Every real Möbius map leaves it as it was, scaling among them; it joins two standpoints. Where the two
differ in position, a foot and a height over one line, it is an extent (D3): unmoved by scaling, held by no single read,
a gap in space. At one foot the distance is |ln r| for heights in the ratio r, the gap across of §2; standing higher on
both sides only makes them harder to tell apart. The same distance between two standpoints at one position that differ
by a boost is the rapidity (§4), and there it is no extent: no gap in space lies between them, and the number is the
coordinate of a map (D7). The formula is one; what it is said of decides the kind. **Checked** (FRG); classical.

**Where the heat comes from.** The read is a heat map: a continuous weight over its readings, with nothing counted in it.
The measure is uniform by solid angle, every direction of the hemisphere alike, so by angle there is no heat; the heat is
that measure read in a coordinate. In the plane, with one thumb, the heat per unit of reading s is 1/(1 + s²) = h², the
half-Cauchy (in the blueprint's angle, dθ = ds/(1 + s²) = cos²θ·ds). In space, a small patch dA of a screen one thumb out,
square to the look, r thumbs off it, subtends dA/(1 + r²)^(3/2) of the directions (the blueprint's cos³α·dA, r = tan α: one
cosine for the patch's tilt, two for its distance squared), so the heat per unit of screen is 1/(2π(1 + r²)^(3/2)), the
two-dimensional Cauchy:
0.35 of the peak at 45°, 0.125 at 60°, none at the rim. With n thumbs square to the look it falls as cos^(n+1). Half the
peak heat is at 37.5° off the look, with a fifth of the directions inside (the share within α is 1 − cos α); half the
directions lie within 60°, √3 thumbs out on the screen. A camera shows it: a wide lens's natural vignetting, the cos⁴α by
which a photograph's corners darken, is this cos³α and one cosine more for the aperture seen at a slant, so three of its
four cosines are the heat, there before any light arrives (0.35 of the middle at 45°, against the photograph's 0.25).
**Classical.**

**The heat depends on what it is counted per.** Per unit of turn the direction has no heat; per unit of s it falls as
cos²θ, per unit of a flat screen in space as cos³α. The heat is not a grid seen from home: marks laid evenly on a wall one
distance d away, the blueprint's grid, are flat in the reading and crowd toward the horizon per unit of angle, as sec²θ in
the plane and sec³α in space. The Cauchy is the other way round: the turn, even in angle, laid on that flat grid. It is
the turn per unit of the blueprint's grid, the *per* of §9, the rate at which a turn consumes the world. In measure theory it
is a Radon–Nikodym derivative: the turn's even measure carried onto the wall by the projection from home, against the
wall's own measure, dν/dλ = (1/π)·d/(d² + y²) for a wall d away, the half-plane's Poisson kernel. On a flat wall the two
agree in every dimension: the half-space's kernel, Γ(n/2)/π^(n/2)·d/|x|^n, is the even hemisphere carried onto the wall,
(2/|S^(n−1)|)·d/|x|^n, the same constant; in space (1/2π)·d/(d² + r²)^(3/2), the cos³α above. Stepping back composes the
kernels, e^(−d|k|), the Poisson semigroup in the standpoint's height. This is Laplace's equation, a steady state; it is
not the heat equation, whose kernel is the Gaussian, e^(−tk²). The Gaussian too keeps every frequency, damping the fine
ones by k² where the Cauchy damps by |k|; the kernel that loses frequencies outright is the floor's box blur, whose
transform has zeros. The "heat" here is a weight over readings, never diffusion in time. **Classical.**

**Heat maps combine without reconciling.** Two shapes combine only by working out their boundaries. A heat map has no
boundary, so the heat adds. Two senses of combining stay apart: readings added give one Cauchy again, the standpoints
added, z₁ + z₂ (a relay of standpoints); heat maps laid over each other add too, but their sum is a heat map, not one
Cauchy: two peaks stay two. Averaging n readings gives back the same Cauchy, no narrower; the median gains, the mean
nothing. **Classical.**

**A read never sees a shape.** This is about what one read determines, not about what a visual system infers. A
thing is, to one read, the directions it paints. Its shape is a radius along each direction from its own centre, and no
radius is in a read: a single read determines no distance along any direction, and so no shape. A shape comes back only
from more than the bare read: from structure in the paint (ratios of radii carried by what arrives, §4), or from further
standpoints as extents, in the stride; with a unit, in metres. The
read's side is whole; the shape was never the read's to lack.

**Passive.** A read sends nothing. It is not a radar. A ranging instrument carries in the signal's speed and a
clock, two amounts, so its ranges are writes.

## 4. The paint

**Heat and paint.** A direction from home, with its heat, is the read's; a payload, the paint, is what arrives along it.
They share one thing, the point where a direction meets the world.

**The hand.** Hold up a hand, thumb out, to a stained-glass window. The thumb is H: the one length held, its size
chosen, setting only the zoom. The fingers, spread from flat to upright, are the directions; a read does nothing to
lay them, and wherever the hand is held the geometry gives the same fingers spread the same way, evenly by turn, half
below the corner. Each finger is lit by the pane it lines up with: the coloured light is the paint, the world's, met on
the fingers, and it changes with what is in front of them. No colour carries how far the light came; walking is the way
to distance (§6). Hold the thumb against a mountain range and the range spans so many fingers; drawn at the thumb's own
size, every amount read from it would be off by V\*/H, an extent had only by walking (§10). The fingers are coloured,
never colour: painting on them would be writing. In space the window is held with both hands (§8). **Reading**; after
Gibson's ambient optic array (1979). The world decides what meets each direction, which
thing is nearest and what it sends back; nothing it does moves a direction or its heat. Scale the world and nothing moves;
change the world and nothing moves. A rate is a payload per direction: the *of* is the paint, the *per* the read (§9).

**The payload is not lost.** No part of the payload goes into making the directions or their heat, so all of it
arrives, along directions given before it came. Four ways give it back, each exact in the ideal model, with the heat
known and the payload given whole; from finite, noisy samples each is an estimate, and undoing the blur is the least
stable.

- *By its ratios.* Two payloads read against each other make a direction [p₁ : p₂] in the payload's own space, unmoved
  by scaling: the light along one direction over the light along another, one colour channel over another, the radius in
  one direction over the radius in another. A shape about a centre, ln r = a₀ + f(θ) (the real part of ln z as a function
  of the turn), comes back this way: every mode of f from ratios of radii, exactly. The modes are extents (gaps across,
  D3); a₀, the overall size, is the across value against a unit, a write, and no ratio gives it. Radio astronomy reads
  polarization this way: a source's intrinsic polarization angle, from the ratio of its Stokes U to Q, is unmoved by
  scale, while the Faraday rotation that turns it, RM·λ², carries the rotation measure in radians per square metre, a
  write (Burn 1966).
- *By dividing the heat out.* What is counted along the directions is the heat times the payload's weight,
  ρ(θ)·1/(Ω(1 + s²)). The heat is known before anything arrives, so dividing by it leaves the payload's distribution
  exactly, up to its total: the astronomer's flat field, importance sampling's 1/p. The median direction of what arrives
  is the payload's median, at the corner only when the payload weighs alike on both sides.
- *By undoing the blur.* Seen from a height γ, the payload arrives smoothed by the Cauchy kernel, whose transform
  e^(−γ|k|) is never zero: every mode survives, damped, and comes back multiplied by e^(γ|k|), noise with it. A box
  blur's transform has zeros, and those modes are gone. Unique in principle is not the same as stable.
- *By averaging it.* The payload is amounts, and amounts have means: weighted by the known heat, the light across the
  turn totals exactly wherever that total is finite. The mean was never missing from the payload, only from the
  directions.

A known measure can be divided out and an invertible blur undone; a floor that discards cannot. **Classical**; the
sorting is a reading.

**The lighthouse.** A lamp turns evenly and throws a flash along each direction. On a straight shore the landing x
obeys (x − α)/β = tan θ, α the lamp's foot on the shore and β its distance. The angles are the lamp's directions, laid
evenly whatever shore there is; the landings follow a Cauchy because the shore is straight; within each flash the path
to the shore cancels. The lamp's own corner, the flash halfway through the quarter turn, lands at the foot plus one
distance only if the shore is measured at the sea's own scale; read on a ruler whose unit is c times the lamp's distance, the landing
that reads 1 is the flash at the blueprint's arctan c, not the halfway one. To read β from the landings, take half the spread between the quartiles, never the mean. In metres β is a
write: it needs the shore found and a ruler laid along it. The lamp is the read, the shore the line where V comes in as
the scale. **Classical.**

**Mercator's map.** A navigator wants a straight line on the chart to be a constant compass bearing. On a chart whose
parallels are spaced so that a degree of latitude is drawn c times a degree of longitude there, a bearing ψ is drawn at
tan ψ′ = tan ψ/c; bearings are true everywhere only at c = 1, both directions drawn at one length at every place,
Mercator's chart (1569). It keeps every direction and pays in area, stretched by sec² of the latitude, so Greenland is
drawn about as large as Africa, which is some fourteen times its area. The equal-area chart draws c = cos² of the
latitude and gives up the bearings. Each keeps what it was made to keep; only the globe keeps both. Mercator's map is
also not the read: it is a chart of the whole field, every stretch where the reading halves alike, with no focus; the
read is the turn, finest where it looks. Bearings are reads; areas in a unit are writes. **Classical.**

**A moving sky.** An observer moving through a field of stars at a fraction β of the speed of light sees each star change
in two ways, and special relativity writes them as two formulas. Where the star is seen moves: aberration,
cos θ′ = (cos θ + β)/(1 + β cos θ), the same at every frequency. On the stereographic chart of the sky it is z ↦ z/k,
k = e^η, η the rapidity, a Möbius map of the directions, carrying the Cauchy's family onto itself; a sky uniform in the
stars' frame is seen as the spherical Cauchy, density D²/4π. (The sky's own uniform heat on the stereographic chart is
(1/π)·dA/(1 + |z|²)², not the plane's two-dimensional Cauchy, which is half the sky on a flat screen. No law on the sky
is unchanged by boosts; the uniform one is unchanged by turns, and boosts carry it within its family.) What arrives
changes: the Doppler factor D = √(1 − β²)/(1 − β cos θ′) scales each photon's energy and rate, a weighting of the
payload that moves no direction. For a sky uniform in its frame, counting total power, the D⁴ brightening ahead is D² of
directions crowding (the heat) and D² of payload. On ξ = −ln tan(θ/2), the pseudorapidity, aberration is a slide by η,
so one look can give evidence of the observer's boost, with no clock, no frequency and no speed of light, provided every
source is counted whatever its brightness and the sky is assumed uniform in its own frame. The rapidity inferred so is
not itself a read. The read is the sky's directions as they arrive; the premise is about where the sources lie, which
is part of what arrives; the inference compares the two, and what it yields is the coordinate of a map between the
observer's standpoint and the sky's assumed rest frame (D7; §12, O4). That it was had from one look does not change
the kind of thing it is, and the paint that served as evidence is not the map. This is a statement of classification,
not of measurability: the rapidity can be observed and measured as well as any quantity in physics; what is said is
only that a quantity does not become a read because a read lets it be inferred. Nor is the boost a fiction fitted
afterwards: it is a physical change of standpoint, and seeing a pattern and naming the change responsible for it are
two steps. The inference is conditional on the
premise: directions alone do not give the sky's rest frame, nor show that such a frame is the only one. Taken as the
sky's median before a boost against after, the same coordinate is had by joining two looks at one position, with no gap
in space: a map again, not an extent. The speed in metres a second needs c carried in, and D read as a line's shift needs the
line's rest frequency: both writes. **Classical**; the sorting is a reading.

## 5. Near and far

**The crosshairs.** Cross the thumbs (§8) over whatever is looked at, the look running down their diagonal. Where they
cross is the corner: the thing there reads one thumb along each thumb, every pair alike, v/h = v₂/h = 1, and it is drawn
one thumb wide. Along the line of sight it lies √2 of the crossed thumbs' lengths off in the plane and √3 in space, the diagonal of a
square or a cube one thumb on a side. The distance overlay counts along the look, and takes that whole distance as its one
thumb: d/H = 1 at the crossing, the crossed thumbs each that over √2 or √3. That crossing, with H, lays the near field and the far field over the read, as an overlay: the
Cauchy itself has neither. Along every direction one thumb splits the heat in distance in half, whatever H is.

**Near and far.** The near field is a single thumb, laid evenly: everything nearer than the crossing gets its heat in
proportion, the first half of the thumb as much as the second. The far field is read in ratios: a thing one thumb wide
reads one in two, one in four, one in eight, and two far things are related by the ratio of their readings ("one in eight
is half of one in four"), the same at every scale. Each stretch over which the reading halves holds the same heat as the
one before, out toward the horizon. Counted, "8 thumbs out, three stretches past the corner", it is an extent; given a
value, 1 + ln(d/H) with a base chosen (§2), or 2 − H/d on a lay that keeps all of reality within two thumbs, it is the
blueprint's number for what the read holds as a ratio. There is one corner, the split between the near field and the first
stretch; past it the stretches are plain. Move the crosshairs and the split goes with them.

**The overlay's heat in distance.** Along every direction the share of distance below x = d/H is the heat 1/(1 + x²) totalled from home to x, over its
whole total: a half at x = 1, whatever the thumb (the blueprint's formula for the share is (1/Ω)·arctan x). Per
unit of plain distance it is greatest at the eye, 1/(Ω(1 + x²)); per unit of ln(d/H), by ratio, it is
(1/Ω)·x/(1 + x²) = (1/π)·sech(ln(d/H)), hottest at one thumb and cooling alike both ways: 0.8 of the peak at one in 2 and
at two thumbs, 0.47 at one in 4 and four, 0.25 at one in 8 and eight, never zero. Counted as K places, they sit
them at d/H = tan(kΩ/K), the first K/2 inside one thumb. Past it the share left beyond x thumbs is, by the exchange, the share below 1/x (the blueprint's (1/Ω)·arctan(1/x)),
0.295 past two thumbs, 0.156 past four, 0.079 past eight: a heavy tail, so no mean of distances. The split is a mark at
one thumb on every direction, each one's median, not a body. Take the overlay away and the Cauchy is unchanged.
**Classical.**

**The hot spot.** Put the two heats together and the read has two centres. The eye is where every direction starts, a
point with no size. The hot spot is one thumb out along the look, where the thumbs cross: the corner twice over, in
direction the triple corner [1 : 1 : 1], in distance d/H = 1, the point fixed when every distance ratio is turned over,
and the median as well as the peak. The two corners meet there only because the thumbs are pointed at a thing and
takes that thing as its thumb; pointed elsewhere, the heat moves and no direction does. From the hot spot the heat thins
every way: across the look as cos³α, along it as sech(ln(d/H)). The near field runs from the eye to the hot spot,
distance in proportion; the far field from the hot spot to the horizon, in ratios; each holds half the heat. Joining the cuts on every direction, the blueprint
draws the near-field sphere of radius H (§8). A read holds only the mark one
thumb out on each direction it reads.

**The one-thumb circle, and the three corners.** Everything within one thumb of the crosshair's point is a ball (a disc
in the plane) touching each face of the wedge, at the cube's corners one thumb back along each thumb. From the eye its
outline is a circle 35.26° about the look, the largest about the crosshair inside the wedge, holding 73% of its
directions; in the plane the same construction runs ±45°, home to horizon. Whatever is pointed at becomes the corner, so
the circle goes with the look. Home is on it, at the three points it touches. Each pair of thumbs has its own corner, a
line through the crosshair, the three crossing there 120° apart; along each, the third thumb runs a quarter turn from
home on the circle (35.26° off the look) through the corner to the horizon at that thumb's direction (54.74° off). Inside
the circle there is no distortion at the corner, every pair's ln(v/h) zero there; moving out each direction's
grain holds more, in proportion, as one over twice the reading toward home: compression, not blur, hexagonal near the
corner and unbounded only at the three homes. It is a precision, not a size: laid by turns off the look a thing's place
parts from a flat screen's only far out (tan α/α, 1.10 at 30°, 1.27 at 45°). **Checked** (THM).

**Laid by the heat.** A flat screen does not give each direction the same room; the screen that does is Lambert's
equal-area map about the look, a direction α off it at radius 2·sin(α/2): true at the crosshair, off by 0.9% at 15°, 3.4%
at 30°, 7.6% at 45°. Laid that way the rings of the distance overlay come where the readings fall: one thumb off the look
at 0.765, then one in two, one in four, one in eight at 1.05, 1.23 and 1.32, packing toward the rim at √2, because each
stretch holds fewer of the look's directions than the one before (0.26, 0.20, 0.12 of what is in front, and 0.12 past one
in eight). The ground has its own reading: a point ρ along it, with the thumb's ground point D away, reads
the share below D/ρ (the blueprint's (1/Ω)·arctan(D/ρ)), one at the feet, a half at the thumb, zero at the horizon, so the far ground gathers in rows just under
the horizon. A world made only where the view reaches, from cells at every scale kept only where a thing spans Ω/(4K) or
more, gives the same read. **Checked** (`crosshairs.html`).

**H is a zoom; K comes first.** The read's fineness is finite, its resolution K, which comes before H. H, the thumb it
holds up, decides how K is split: half of it lies inside H at every H; a small H makes the near ones fine and puts more of
the world past the held edge, a large H the reverse. No H holds everything. The best H for a thing is the one that puts
it at the corner, where the relative grain is finest; so the corner follows the focus, and what is looked at is drawn one
thumb wide.

**Where the split falls: looking around.** Pointed at a thing, the crossed thumbs take its distance as H, so the thing
sits at the corner, half of every direction's distance heat nearer and half farther. The reason to do this is that it is
optimal: the corner is where a reading's cells are finest relative to their place, and a thing at the corner is at
parallax's corner, where a step of two thumbs places it with the least error (§6). Putting the thing looked at on the
corner is what an observer should do; whether observers do is open (§12).

**K and N.** N is how many items there are; K how many are held. To know N is to know the whole, its size in amounts
and how much is in it: a count. A read never knows N; it knows K, read continuously as the turn is, a fineness with no
last place. Laid out as K places at the heat's quantiles, K *addresses*, it is a count, and addresses here are always
that; as a metaphor they serve where they connect the Cauchy to computing (a direction looked along is like an address
looked up, with the heat under it). The Cauchy spreads the read's K over a world of any size, the near field in
proportion, the far in ratios, and, counted as K addresses, everything past the last on the one at the horizon. Double
N and the view does not change; make N unbounded and it still does not (an infinite star field browsed at N and 2N shows
the same view, apart by less than 10⁻⁷ at N = 2⁴⁰). So the Cauchy is a cull: an implementation holding K samples does
O(K) work, whatever N. What the cull gives up is sameness: a count that holds N holds every item as 1/N of the whole, all
alike, with no standpoint favoured; a read's K is spent finest at the corner and coarser each stretch away, and that
unevenness is the vantage. **Checked** (`star-field.html`).

**Something to read, and K of it.** A read says nothing about N except that there is something to read, and it only ever
holds K of it. It does not need the world to come counted: N is a count, and a count is a description laid over things
(§1), so whether the world has an N, finite or not, is the blueprint's question. The read is the same in every case, even
an empty world, where every direction reads to the horizon. A program that has to make the paint does need something in
N's place, and the honest form is a rule: each thing made from its cell when asked, a law covering every cell at once
rather than a list. That passes the count to the rule, and the read never asks the rule for a total.

The same holds across scales. Give each scale the Cauchy's share of the read, the heat per ratio (1/2Ω)·sech(ln s) taken
a scale at a time: sech(k·ln 2) at k scales from the focus, 1, 0.8, 0.47, 0.25, then about half each time. The total over
every scale is finite, so scales without end, up or down, are held at a fixed K, finest at the focus. With each scale
given the same share instead, the total is infinite. The view at any depth is the same view, and the readings take no more
digits at depth, since the depth's factor is in both terms of every slope and cancels. Only the observer's own position
takes more digits, about one decimal digit for every 3⅓ scales down: that is a write, and writes are moved by scaling.
**Checked** (`thumbs-walk.html`, TWK runs 4–5: about 4.5 times the focus scale's count in all, with 8 or 40 scales above
and down to 40 below, against π/ln 2 ≈ 4.53; the view 2⁻²⁰ deep within 4% of the start's; the slopes' digits the same).
Keeping things by their size on screen is classical (level of detail); the share law across scales, and no N anywhere,
are the reading here.

**The read as a control.** The same split can be held in the hand as a dial. A held push adds to the hyperbolic angle
ζ at a steady rate; the place it reaches is one thumb times sinh ζ from home, and the needle is drawn at the turn gd ζ,
so it never leaves the quarter turn. Near home the place moves in proportion; one thumb out it reaches the corner
(ζ = 0.881, the needle at 45°); far out a steady push reads a steady ratio, one in two each ln 2 of ζ (2.31 from the corner
itself, 2.0037 ten thumbs out, 2 within 4·10⁻⁵ at a hundred). The needle turns per unit of place as cos²θ, half at the
corner. With one more degree of freedom the control is a dome looking down on a floor without end: home straight down,
the rim the horizon, the heat per unit of floor cos³α; each place painted by what its one direction meets, so a far place
is a sample of the floor, read at the detail its footprint earns, a few dozen tiles for the whole world. Laid as sound,
one in two is an octave, and a tone of octaves that rises without arriving (Shepard 1964) is the horizon heard. None of it
needs a count of what is out there. **Checked** (reportbase/calendar's dials).

**Drawing a shape: circles, a height, a step toward the detail.** A closed outline about a centre can be written as
circles on circles, its Fourier series: the turns of one standpoint at the centre, evenly. Seen from a height γ, the
outline is smoothed by the circle's own Cauchy, the wrapped Cauchy, shrinking circle k by e^(−γ|k|) and moving none: the
broad form stays, the fine circles fade first, the height setting how much detail is kept. Or each term can be the circle seen from a
standpoint stepped toward where the detail is: the Takenaka–Malmquist terms, chosen one at a time to take the most of what
is left (adaptive Fourier decomposition; Qian and Wang 2011). On an outline with one dent, the best 85 circles draw it to
a part in a thousand; eleven such terms do, every one standing at the dent. On a broad outline the even circles win, ten
against nineteen. The radii drawn are extents about the centre; the overall size a₀ is in none of the terms. **Checked**
(EPI).

## 6. Across: extents

**Parallax is the passage from a read to an extent.** One standpoint gives directions and a frame, and no size: every
ghost of the room, twice as far and twice as large, gives the same readings. A second standpoint adds the step between
the two. Two standpoints held at once, as two eyes are, need nothing kept and nothing counted; one standpoint moved
needs the earlier look kept, in a write, and the step taken, a write. Each point, matched in both looks, is two rays crossing, and its distance comes out of the crossing, in the step's
length. More standpoints give every extent seen. This is how an observer reconstructs the shape of the blueprint's cube,
in its own stride; the cube in metres needs the stride counted in metres, a write (§7).

**Parallax is a sum of reads.** Put two standpoints a step B apart and let each read a point in its h/v chart along the
step, cot a from one end and cot b from the other (a and b the blueprint's names for the two directions; each read is
taken inward, toward the other standpoint, so both are positive for a point between the two feet, and they are §9's
1/s₁ and 1/s₂). Then cot a + cot b is the step over the point's distance from the
step's line: the depth is the reciprocal of a sum of two reads. Those are the two operations the Cauchy is closed under,
the sum (a relay, points m + iγ adding) and the reciprocal (the exchange), so parallax never takes a read out of the
family. If each read is uncertain as a read from a height γ is, and the two errors are independent, each is a Cauchy
point w = (c + iγ)/(1 − iγc) in that chart, c its true value (a law written as one complex number, location plus i times
scale, as McCullagh 1992 does), and the depth is exactly a Cauchy whose point is the same triangulation done on the two
points: D = B/conj(w_a + w_b), at every γ, not only for small errors; rays that do not meet ahead are part of the law, as
negative depths. At the pair's corner, the circle on the step, the depth's point stays at the true distance d, turned by
twice the read's error: D = d·(1 + iγ)/(1 − iγ) (the blueprint's d·e^(2i·atan γ)). Two things leave the family. The extent across the line of sight,
−1 + 2·cot a/(cot a + cot b) in half-steps, has a density over each standpoint that is infinite, where a Cauchy's never
is. And when each standpoint reads only a quarter turn, the sum of two half-Cauchys has density (1/Ω²)·s near zero, so
the depth's tail falls as 1/d³, not 1/d², and that depth has a mean. Repeating the reads, the mean of the reciprocal
depths gains nothing, while their median narrows. The step is the one length in it, and in thumbs or strides the depth
is an extent. **Checked** (PXS).

**Turning teaches the directions; walking teaches the world.** A standpoint has two motions, a turn about itself and a
step along a line. A turn moves every direction by the same angle, near and far alike: it gives the frame, the corner and
the Cauchy of the fingers, the same in every world. A step is the first motion whose effect depends on the world: near
things cross the fingers faster than far ones. Any motion of a standpoint is a turn and a step together (a turn about any
point but the standpoint carries it along a chord), and only the step's part places anything.

**Motion, from reads.** A thing coming toward the standpoint is read at its edge: x, the thing's breadth against its
distance, the reading v/h of the line to its edge. One read holds one x; that x grows joins two reads. The reading over
its rate of growth, x/ẋ, is the time until the thing arrives if it keeps coming as it comes: the breadth, the distance
and the speed all drop out. Lee (1976) proposed that a driver braking uses exactly this: brake so that the time to
contact shrinks no faster than half a tick a tick, τ̇ ≥ −½, and the car stops at the thing, since at τ̇ = −½ the distance
it needs to stop is the distance it has. Sorted: from two reads a tick apart the number is x₂/(x₂ − x₁) = d₁/B, the thing's distance over the step between
the two reads. That is a ratio of two distances, unmoved by scaling and held by no single read, and so far it is D3's
gap across with nothing temporal in it. Read as a time, the ticks still to come, it adds a premise no read holds: that
the steps go on alike. The ticks to come are not a count in this paper's sense, since a count describes writes made and none of them is made yet, though they rest on a count's premise; what kind they are is left open (§12, O9). τ in seconds
is a write. One stream cannot tell
a thing coming nearer from a thing growing where it stands; a neighbour at the same depth, read at once, tells them apart,
approach moving both readings and growth one. A speed in metres a second is a write twice over. **Classical** (Lee);
the sorting is ours.

**Walking to the mountain.** Hold the thumb out at arm's length, H against the arm L, and walk toward a mountain whose
breadth V\* and distance d are unknown. The thumb never changes; each read is the finger the mountain's edge touches,
[h : v]. The blueprint's account of which finger, v/h = (V\*/d)/(H/L), uses amounts no read holds. A read is one place, now:
"one in eight of the thumb". Nearer compares two reads, so "getting nearer" is an extent, not a read. Laid in order: far off
the mountain is one in eight of the thumb, then one in four, one in two; per halving of the distance the turn taken in is
greatest where the mountain fills the thumb and fades on either side. One read has the mountain exactly covering the
thumb: the corner, which needs nothing walked: "now the mountain is my thumb", while V\*, d and the corner's distance
d_c = V\*·L/H stay unknown. Past it the two sides mirror each other: d and d_c²/d read as reciprocals. Laid in order the
reads climb toward the horizon, [0 : 1], and no read meets it; the walk arrives because the walk is a count of strides and
ends, and at the foot a read has one more read, its feet. A steady pace makes τ̇ = −1, past Lee's −½, arriving at
speed; easing so that it holds at −½ stops at the foot. The strides from the corner to the foot are d_c, so counting them
gives V\* = (strides from the corner) × H/L: an extent, in the walker's stride; in metres once the stride is carried in, a
write. Scale the world, the walker's stride with it, and nothing along the walk moves: no read, no count of strides; only
the metre carried in.

**The mountain's own corner.** The walk has a second corner, with no thumb in it. Stand on the mountain's centreline and
read each edge against the line to its middle: half the breadth over the distance, s = (V\*/2)/d. Squared and divided by
its own length it is Z = (1 + is)/(1 − is), rational in the read: no angle, no Ω and no e are needed to have it. Far off
s ≈ 0 and Z ≈ 1: that end of the walk is home. Where the half-breadth equals the distance, s = 1 and Z = i: the edges a
quarter turn apart, the mountain's own corner. At the foot s grows without end and Z goes to −1: the horizon. So walking to
a mountain is walking from home toward the horizon, and the two corners are far apart: the thumb's at d_c = V\*·L/H
(thirty breadths off for a thumb of 2 cm at 60 cm), the mountain's own at half a breadth, sixty times nearer.

Laid in order, the reads take in the turn at two paces. Counted in ratios, every halving of the distance, the span grows
most about the mountain's corner and alike either side: from eight half-breadths off to an eighth of one, 14°, 28°, 53°,
90°, 127°, 152°, 166°, the gains 14°, 25°, 37°, 37°, 25°, 14°. Per unit of x = ln(V\*/2d) the turn taken in is sech x, the
distance heat of §5 with the half-breadth as the thumb. Counted in distance walked, ℓ, with dℓ = −dd, it is
dα/dℓ = V\*/((V\*/2)² + d²), the Cauchy in distance, least far off and most at the foot. One turn, two measures: from the
corner to the foot either gathers Ω, from home to the foot 2Ω. Neither is the breadth. Strides from the mountain's corner
to the foot are V\*/2 in the walker's stride, since the read there is 1. They agree only at a corner, where a read is 1 and
a length walked and a ratio held say the same. Joined, the reads telescope: the product of Z_(j+1)/Z_j along the walk is
Z_N/Z_0, the first and last reads alone; every finite walk ends at its last read, and only the blueprint's limiting completion
tends to −1. The blueprint names each point Z = e^(iα), α the span, and the end e^(iπ) = −1 (§9): the formula describes the
end and drives nothing. **Checked** (the breath note's §5, at 30 digits; `approach.html`).

**Two ways to arrive.** The thumb's corner has the same form. With s the mountain against the thumb, s = d_c/d,
Z = (1 + is)/(1 − is) is near 1 far off, i where the mountain covers the thumb, and −1 at the foot; a place and its mirror
d_c²/d have Z·Z′ = −1, §9's exchange. So the blueprint's e^(iπ) = −1 names the arrival, and i·i = −1 says the corner taken
twice is the arrival. Three motions act on these reads, and they are the three kinds of map a line of slopes has (the
classical elliptic, hyperbolic and parabolic maps of the projective line). A turn of the look leaves no read where it
was. A pace that covers a fixed share of the distance left multiplies 1/s by the same factor each step; it leaves two
reads where they were, home and the horizon, and carries every other from the first toward the second without reaching it.
The foot is its limit, and it needs no count and no size: one reading held steady. A steady stride takes the same amount
from 1/s each step, the stride over d_c; it leaves only home where it was, so nothing holds it off the horizon, and it
passes Z = −1 in a finite count. Along it 1/s falls evenly, before the corner and after it alike: 1/s is the number
line in units of d_c, and the corner is not marked on it; the corner belongs to the reads, the even steps to the count.
Even in 1/s and even in ratio are different paces: a pace that is both takes no step. So the one −1 is reached by a
count and approached by a ratio. Nor must the foot be walked to: two reads one counted stride apart, x₁ and x₂ in 1/s,
give the strides left, x₂/(x₁ − x₂), and the breadth in strides, (H/L)/(x₁ − x₂), at any distance: extents, in the
walker's stride. The fixed share has been observed: landing honeybees hold the image's rate of expansion steady, their
speed in proportion to the distance left and near zero at contact (Srinivasan et al. 2000; Baird et al. 2013); and the
corner found by looking with the size paced from it is the forester's stick method. Those findings are their authors';
what this section adds is the one circle on which the two paces are the maps with two fixed points and with one, which
is why the first never arrives and the second does in a finite count. Which pace a thing that approaches takes is not
this paper's question; both stand on the same reads, which are there for anything that looks.

Parallax is the link in this chain: two reads and one counted step. A chain of such links collapses to its ends, exactly:
the ratios Z_(j+1)/Z_j along the walk multiply to Z_N/Z_0 for any strides, equal or not. Nothing here needs the stride to
shrink. The strides left come exact from two reads at any stride size, and the arcs join by tangent addition: from a
start at x₀ = d/d_c to the foot the half-arc's slope is exactly x₀, so from the corner to the foot it is exactly 1, a
quarter of the blueprint's circle, in seven strides or a thousand. The half circle, from 1 to −1, belongs only to a walk
begun without end; from x₀ corners out it falls short by about 2/x₀ in the blueprint's measure. So the infinite in
e^(iπ) = −1 is the far start, the horizon behind the walker, not a small stride. The stride must shrink in one place only:
where slopes are added as though they were angles, the sum runs over by about the stride squared, and the blueprint's angle
is that sum's limit. Joining is the geometry's, exact at any stride; adding is the blueprint's. Each stride's Z_(j+1)/Z_j
lies on the circle exactly, where the factors of (1 + iθ/n)ⁿ (§9) do not: the walk is not that product, though both end
at −1. **Checked** (WLK, exact: house, tower and mountain 3600/7, 18000/7 and 900000/7
strides from the thumb's corner to the foot, each returning V\*).

**Read times count.** On this walk the read is s and what is kept is the count n of strides left, a description laid over the strides, which are the writes. Their
product is the same at every place: s·n = d_c/S, the corner's distance in strides, and that times the thumb over the arm
is the mountain in strides. Neither factor has it alone: a look gives s with no size in it, a count gives n with no
mountain in it. Counted in corners in place of strides the product is 1 everywhere, s × (1/s), and both factors are 1 at
the corner; what the walk adds to that identity is that 1/s is something counted, strides left times one stride's step.
Two reads and a count of one already give the product, by the formulas above. The fixed share never does: it holds a
ratio of reads and counts nothing, so it has s at every moment and no n, and its sum of steps falls short of the whole
by (1 − r)^m after m steps, at every m. The 1 is closed by a count and only approached by a ratio. How this 1 stands to
§9's 1/Ω × Ω is said there. **Checked** (ONE, exact).

**Extents come by degrees.** The crossing from reads to extents, and from extents to writes, is not a switch thrown.
- *In what.* Two standpoints a step apart give every extent in that step. If the step was one thumb, extents are in thumbs
  and V is placed as V\*/H. Only a step counted in an agreed unit gives an amount, a write, the one rung scaling the world
  moves.
- *How well.* The extent's error per unit of angular error is least when the thing sits at the pair's corner, half the
  baseline equal to the distance. With k = d/(B/2) and ε the smallest step in direction a read tells apart, the
  fractional error in the distance, and so in V\*/H, is ε·cosh(ln k) = ε·(k + 1/k)/2: ε at the corner, about ε·d/B far
  off, the same at k and 1/k. It reaches 1, and the thing is a direction alone, near d = B/ε. In the worked example (§10)
  one thumb walked toward a range ten thumbs off puts it at k = 20, an error 10.025 times ε.
- *Of which things.* One observer, from the same two standpoints, places near things and not far ones. Placing belongs to
  a thing at its distance, not to the observer.

More standpoints and longer baselines narrow the band; nothing closes it. The blueprint with every amount exact is the
limit of the passage, not a stage of it, as Ω is the limit of its approximants: V faced is knowable, and known as an exact amount
only at the limit (§1, "Four things"). **Classical.**

**The thing itself as H.** The thumb can be set to the very thing whose size is wanted. *As the unit*: the thing is drawn
at one length, its V is 1 by choice, and everything else is placed in its units; its two ends become the baseline and the
standpoint is the point placed, at 1/(2t) of its breadth from its middle, t the slope of half the turn between its ends (the blueprint's tan(α/2)), from
one look.
*As the focus*: the observer keeps the thumb and chooses a baseline that puts the thing at parallax's corner, half the
baseline equal to the distance, where the error is least; that needs the distance roughly first, so it is done in passes.

**A tower of extents.** Ratios suffice for a great deal. A tower of extents, each storey placed against the next, holds a
building, its rooms and their things, with one amount at the top if metres are wanted. Along a chain the gaps add, so the
middle lengths drop out and the ends survive; a loop's gaps sum to zero, and what does not is the error, which a loop shows
and cannot place. Laid across the plane, extents are gaps, and composing them is adding gaps: N extents hold all
N(N − 1)/2 ratios between them, a slide rule, straight across and circular up, with nothing computed. **Reading**;
`slide-rule.html` shows it.

The middle storeys are scaffolding (§1, "A denominator is scaffolding"). A table three quarters of a door and a door two
fifths of a wall give a table three tenths of the wall, and the door, needed for both readings, is in neither side of
the result; with a door half as tall the readings are 3/2 and 1/5 and the result the same. The bottom storey stays:
three tenths *of the wall*. So a tower gives the whole one number short, the size of what its last storey was read
against. A figure read from inside is the same tower closed into a loop: radii 2, 3 and 6 leave the ratios 3/2, 2 and
1/3, which are its shape and multiply to 1; the circle is the figure whose ratios are all 1 (§2, the payload by its
ratios).

**Turns, counts and corners.** A read's turns are continuous: between two directions it passes through every one between,
so a read never turns sharply. A corner, a change of direction at one place, is met only by walking a line and stopping
there, a count.
- *A count made to hold a turn rings.* A finite count of even waves, asked to hold a sharp change, overshoots on both
  sides by about 9% of a jump however many waves are used, the ripples only crowding nearer (Wilbraham 1848, Gibbs 1899).
  The overshoot belongs to the representation, not to the edge; physical ringing is a dynamics.
- *Written down, the two cost differently.* An outline can be written as numbers at even places of one turn (Fourier
  coefficients, radii at even angles, points at even shares of its length) or as a walk along it (Bézier pieces, a list of
  points, a turtle's steps). On 73 outlines from a shape library, each written to within half a percent of its size, every
  even-turn form was shorter as text than every walk on the smooth outlines, and every walk shorter on the outlines with
  corners. Rounding the corners of a square, a triangle, a star and an arrow took the even samples from two to three times
  a Bézier path's length to between a half and three quarters of it. Across the library the even samples' length followed
  how fast the outline turns (Spearman ρ 0.85) more than how many corners it has (0.55); the Bézier path's followed its
  corners (0.59) and not its turning at all (0.00). **Checked** (TXT, with the predictions that failed recorded).
- *Ω and e are where a count tries to hold a turn* (§9).

## 7. The zero: writes

**The unit carried in.** A write ties the across axis's zero to something outside the world: a metre bar, a second, an
agreed notch. Every extent hung from the same thumb is then an amount, all at once, by one number: the thumb in metres.
Scaling the world moves that number and every amount with it, and moves no extent. The foot, the cubit and at last the
metre were each one observer's body or object made into a public notch. Two observers that see one thing in common need
no unit between them: the ratio of their thumbs is an extent, read off what they share. A unit is needed between observers
who share nothing in view. **Reading.**

**A survey.** Snellius (1617) and Roy (1784–85) wrote whole countries this way: thousands of directions read, each
written down in degrees by the instrument, one base walked and counted. The directions are reads; with the base as the
thumb, every side of every triangle is an extent; the base counted in a unit is the one write, and every side is then in
the base's unit. A second base checks the first and adds no scale. **Classical.**

**What a blueprint adds.** A blueprint is the classical statement, the whole in amounts seen from no standpoint. An observer builds with reads and extents and never needs a unit, until one of these is wanted:
1. the size, an amount;
2. meeting out of view, with another observer with nothing in view in common;
3. sums of amounts, which no ratio supplies;
4. the join, the facings put together into a closed circle or sphere;
5. the thing before the thing, a plan for what is not yet there;
6. completeness, stated rather than hoped for;
7. a far field kept in proportion, common to standpoints whose corners differ (the number line has no corner, so standpoints
   whose thumbs differ can share it).

Each is a capability, not a condition. A blueprint has them; an observer comes to them only by a count and a unit carried in, and never by a read. Nothing here is against the write or the number line: they
hold what no standpoint holds.

**Write once, then read again.** A write is over once made: the stride counted, the number put down, the plan
drawn. To be used it must be read: someone stands somewhere and looks at it, at marks on a page in their directions and
ratios, as at anything else that arrives. A plan in a drawer does nothing until it is looked at; a survey's base,
once counted, is read against by every angle that follows; a drawing of a known room, rendered from a standpoint, is a
write turned back into a read. So the passage runs both ways: reads become extents through standpoints, extents become
writes through a unit, and every write, once made, joins what is read.

**Recovered, by placing.** An observer can recover a thing exactly, its shape, its extents, even its size in its stride,
and still partially. A loop that closes shows that the routes taken agree; it cannot show that no route remains untaken.
Completeness is never a read. What recovers the thing is not reading harder but the passage through standpoints.

**A bounce writes its size.** A ball bounces to a height A every P ticks under one pull, g = 8A/P². Scale the world and
the observer by k: the ball's directions at the top of the bounce and at its foot are the same fractions, and so is its
height in its own breadths, read from its foot and its breadth. Under the same pull the scaled ball takes √k times the
ticks, since P goes as √A. The pull is an amount in a unit, so the ticks of a bounce, counted, write the ball's size,
A = gP²/8: Galileo's square–cube law, where the unit gets in. **Classical**; **Checked** (`sky-city.html`, its balls
placed from the tick alone, the slopes unchanged and the ticks doubled at k = 4).

**A candle writes its distance the same way.** Scale the world with the paint fixed and no solid angle, flux or
irradiance moves: one standpoint does not read 1/d². Carry in a source's luminosity L, as the pull g is carried in, and
a flux counted writes its distance, d = √(L/4πF). The inverse square is the scale test with L held fixed, as the
square–cube law is the scale test with g held fixed. Its 4π is the source's whole sphere, held from no standpoint, the
dual hemispherical vantage's form; the single vantage at the receiver needs only its own front, the paint along each
direction unchanged with distance and the source's share set by the slope, (Δ/d)², with no π. The two forms agree, as
conservation says; what differs is where each stands. **Classical**, the sorting a reading (`inverse-square.md`, "From
one vantage").

**Near and far, one share and its exchange.** On its axis a flat, evenly bright disc of radius a gives exactly its share
of the front hemisphere, E/(πL) = 1/(1 + s²) with s = d/a: the heat of §2, met as light. Far off that share is the
inverse square, close in it is flat, and the exchange s ↔ 1/s makes the two complements, E(s) + E(1/s) = πL, half each at
the corner d = a: §9's 1/(1 + s²) + s²/(1 + s²) = 1, with near and far its two sides. Scaled with its distance the disc
moves no share; only with its size held fixed does the inverse square in d appear. Two discs facing each other read each
other reciprocally: the ratio of the two reads leaves the sizes, their product the distance in their geometric mean.
The pairing is the round source's (sin²α + cos²α = 1 for its rim's cone); a square plate's two shares overlap at the
corner. **Checked** (ISX, `plans/isx-plan.md`, exact at 50 digits, nothing killed); the formulas classical, the sorting a
reading.

**A single vantage and the blueprint, side by side.** A read is a single hemispherical vantage; the blueprint is the dual,
drawn from no standpoint. Where the blueprint is what is wanted, the list above says so: what acts out of view with no law
in time, whose state has to be stepped whether anyone looks; more than one standpoint, which must agree on something that
belongs to neither; a plan, a save, an edit. A program needs the world anyway: a machine is a counting thing, so the world
has to be held or made before any view of it exists, and the read decides only which part is looked at and how finely.
For a program the single vantage is an option, not a requirement; its interest is as the account of observing, since no
observer in nature has the view from no standpoint. A world can also be made as needed: each thing from its cell when a
read reaches it, by a rule. Without end there is no whole to hold, so the dual vantage cannot be formed at all, and
nothing compares with the read. The rule answers for any one place from no standpoint, a lookup and not a view; showing the
whole at once would mean making all of it. The work then falls three ways: a read from each standpoint, holding K things
whatever N is; the rule, for everything nobody has touched; and writes, only where something has been changed, the one
part that grows. **Checked** (`thumbs-walk.html`, `sky-city.html`: the read set beside a blueprint made about the eye, 0
missing and 0 extra; a stored blueprint's cells out to 10²⁶ units about 10⁵², against some 29,000 cells scanned at every
distance; cars on loops placed from the tick alone, cars in traffic held). **Reading.**

## 8. In space

**Three parties.** With a third party, V₂, the look turns two ways: up from the horizontal (altitude) and round it
(azimuth), the horizon coordinates of astronomy. Its directions fill one octant, the *wedge*: [h : v : v₂], two numbers
a direction. The uniform measure over the octant's area is uniform in azimuth and in height (Archimedes' hat-box;
Lambert's equal-area map), and its law in the readings (v/h, v₂/h), the two tangent readings on a screen square to h, is
the two-dimensional Cauchy, 1/(Ω(1 + a² + b²)^(3/2)). Every pair of parties is at its own corner, half its readings on
each side; the near field in both readings is a third. The triple corner, h = v = v₂, sits at azimuth 45° and altitude
35.26°, not at either sweep's 45°. **Classical.**

**Two hands.** In space the window is held with both hands. One spreads its fingers from flat to upright, the altitude;
the other round the horizontal, the azimuth. The thumbs cross at a right angle, and where they cross is the triple
corner. Each pane lines up with a crossing, one finger of each hand: the reading is the pair, a direction of the wedge.
Each hand alone gives the one-dimensional Cauchy with its own corner; the crossings together give the two-dimensional
Cauchy. For every crossing to hold the same share, the round hand spreads its fingers evenly by turn and the upright hand
evenly in height, not in angle (in the blueprint's terms, equal steps of the up share v, dv = h·da for altitude a, with h the level share: Archimedes' hat-box again); spread both evenly by angle and the pair neither hand reads leaves its corner. Two hands
add no second length. The picture is not about hands: it shows that the read's three dimensions are not Cartesian, no
three axes of amounts, but one thumb crossed with itself and two sweeps from where it is held. The Cartesian frame is
the blueprint's cube.

**One thumb, two thumbs, three.** In the plane a read holds one thumb square to the line of sight, one reading, v
against h. In space it holds two thumbs crossed at a right angle, both square to the line of sight: one reads up, v
against h, the other across, v₂ against h. Both are the one H, so what is written as V = V₂ = H is the two thumbs
being the same size, and the right angle between them is a quarter turn, unmoved by scaling. Counted from a standpoint,
the dimension is the number of thumbs square to the look. Held with the look along h, the middle of the cross reads
(0, 0), home for both pairs, as the middle of a camera's screen is, and the triple corner lies 54.74° off the look. To put
the corner under the crosshairs the look turns onto the diagonal, and then every party is a thumb at the same angle to
it: two at 45° in the plane, three at 54.74° in space. The three pairs' corners are three planes through the eye that
meet in one line only, so that look is the only one that puts the crosshair at the corner of all three. **Checked**
(THM).

**The wedge is the blueprint's; a read has the horizon's heat map.** The wedge, an octant of directions with faces,
edges and a triple corner, is the blueprint's description of the read, drawn whole from outside. What a read has is the
heat over every direction in front, out to the horizon. The heat is the look's, not the thumbs': hottest wherever the look
points; looked down the thumbs' diagonal, where they cross, [1 : 1 : 1], every pair at its corner. Laid on a screen square
to one thumb instead, as the wedge's law is in v/h and v₂/h, the same directions are hottest along that thumb, at home;
nothing moved but the screen. Let the crosshairs leave the middle of the look, as on a screen where they follow a pointer, and the heat
goes with them, hottest on the line through the crosshairs, while the thumbs stay the look's frame: off the middle, the
hottest direction and the thumbs' crossing are two points, one only down the thumbs' diagonal (`sky-city.html`). As the look turns, the heat map turns with it, without a seam: perfect wherever it
looks, because it is wherever it looks.

**The read's heat covers the hemisphere.** One read's heat covers the hemisphere in front, nothing smaller. Projected
from the eye onto a screen square to the look, directions spread evenly over the hemisphere land as the two-dimensional
Cauchy, 1/(2π(1 + r²)^(3/2)) per unit of screen at r thumbs off the look: the look its peak, rings of equal area its rings
of equal share, and the rim, 90° off, its long tail, never landing. Each pair of thumbs' quarter turn, from its home to its
horizon, is a part of it, the wedge's triangle, 35.26° off at a home and 54.74° at a thumb. The sphere, behind as well as
in front, is the head turned all the way round, other facings joined, the blueprint's. What a read holds is this whole
hemisphere; what a flat screen shows of it is the middle only. A screen whose half-width is a slope of 1.2, on a 16:9
window, takes about 1.78 of the 2π steradians in front, some 28% of the directions and the same share of the heat (on a
flat screen the heat per unit of screen is the solid angle's own measure); no flat screen reaches 90° off the look. The
one chart that fits the whole hemisphere on a disc, the equal-area map about the look, reads to the eye as a ball seen from
outside, its rim round and its squeeze toward the rim a ball's foreshortening, and so gives the read a shape it does not
have. **Checked** (`sky-city.html`: every direction with cos α > 0 kept by the rule, many held things off the screen).

**The sphere without V, and the cone of one read.** H, V and V₂ held as amounts combine into the blueprint's sphere (an
ellipsoid unless written equal); H, H and H, one thumb crossed with itself, into the read's Cauchy. With V unknown only
the ratios (v/h, v₂/h) are kept, and two things go: the sign (a point and its opposite give the same ratios, so the sphere
folds onto the projective plane) and the closing (the great circle square to the look lands at infinity, the horizon).
The sphere's even measure lands on the screen as the two-dimensional Cauchy, each reading twice. Likewise a single read
with V known is the wedge with its cap, an octant of the ball; with V unknown the cap goes and what is left is the cone,
three flat faces meeting at the eye, open. A cone is the one kind of shape that scaling about its apex carries onto
itself, which is why the read is unmoved by scaling; the cap was where the scale lived. Cut by a screen one thumb out, the
cone shows the quadrant with 1/(Ω(1 + s² + s₂²)^(3/2)) square to h, or the triangle with the corner at its middle down
the diagonal; cut elsewhere, the same law at another size, which is why H only zooms. In the plane: a quarter disc with
its arc when V is known, a right angle with no arc when it is not.

| shape | what is kept | kind |
|---|---|---|
| the sphere | H and V, every sign: all relations, closed | the blueprint's, with amounts |
| the Cauchy plane (the full round of the look) | V dropped: opposite points one, the horizon at infinity | the relations without V |
| the cone of one read (the quarter turn) | V dropped and no relation negative: every pair from home (0) to its horizon (∞) | the read |

The cone is the blueprint's name for what one read holds; a read has only a vantage.

**Setting H sets the near-field sphere, the blueprint's.** Choosing the thumb is, in the blueprint's account, choosing the near
field as a ball of radius H about the standpoint, every facing joined. A read has the same choice as a mark on every
direction it reads, nearer than one thumb or past it: no surface, no facings joined. Inversion in the sphere at H carries
the far field point for point onto the near field, infinity to the eye, which is why each holds half of every direction's
distance heat. Its filling is the read's heat: along each ray the half-Cauchy in distance, H/(Ω(H² + d²)); across
directions cos³α off the look.

**A cube of dots, read from one of them.** Lay a box of dots one unit apart, the blueprint's, 12 a side, stand at one dot and
look at another, and colour every dot by the read's heat, cos³α × sech(ln(d/H)), the thumb set on the dot looked at
(`heat-cube.html`). The cube never changes, only its colours, and only when the look does. Choosing what to look at is
choosing the thumb. The two fields are equal in room, not in count: from a corner of the box looking at its middle, 436
dots are nearer than one thumb and 1,291 farther, but laid as the read lays distance (the share passed, the blueprint's (1/Ω)·arctan(d/H)),
each field has half the room. The hot core is small: inside 37.5° lies about a fifth of the directions in front. The box has a last dot,
so along the look the dots stop short of the horizon: the box closes, the heat runs on.

**The shape is swept, not each thumb.** Within the quarter turn the even read does not come from sweeping each thumb
through its own angle. Sweep them that way, evenly and one after the other, and the directions pile toward the thumb the
first sweep turns about: v falls below h for 0.343 of the readings, not a half, and the near field is 0.233, not a third;
in the other order the pile goes to another thumb. Swept together, the three thumbs fill the wedge evenly by area: every
pair at its corner, the near field a third, no order. With every turn of space held, the blueprint has the same law on the
octant as the one measure left alone by turns (Haar), any turns composing to one about one axis (Euler). In the plane the
two ways are the same. Any linear map of the thumbs' space, a projective map of the screen, carries the even read to an
elliptical Cauchy, its standpoint five numbers in space against the plane's m + iγ; only turns keep it round. **Checked**
(SWP).

**The blueprint's cube, and the sphere as the blueprint's picture.** The blueprint's frame with three parties is Descartes's: X,
Y, Z, three number lines, every point three amounts. It reaches the read's directions only with H and the angles:
X = H·cos a·cos ψ, and so on. Every direction about a point at radius H is a sphere, drawn whole. Placed together,
the corner of the read's wedge points at the vertex of the blueprint's cube. With the cube outside the sphere, touching it
at the ends of the axes, the picture is the inscribed sweep's; with the cube inside, its far corner on the sphere, the
central sweep's (Thales' circle through home, the ends and the far corner). The hemisphere's 2 and ½, like Ω and 1/Ω,
are limits, their values held by no read.

**What survives in space, and what does not.** In the plane one law plays four parts: the image of the uniform turn under
a Möbius map, harmonic measure, the powers of the standpoint, and the two sweeps' rates. On the sphere they part into
three laws: harmonic measure keeps the powers of the standpoint and its mean; the spherical Cauchy, the uniform turn pushed
through a boost, keeps the Möbius maps; neither is the other's image. A quarter turn about one axis and then another ends
120° away from the same two in the other order. What survives is the split between direction and payload, heat and paint,
the corners and the wedge seen from home: both tests still sort every quantity, and every pair of thumbs still has its
corner at the median, since those need only the exchange of two shares, not commuting turns. **Checked** (EUL).

**Three loops.** Undo each of two motions in turn and see what is left. These are compositions, joinings, so each loop
is the blueprint's account of motions, not a read.
- *A turn and a scaling.* Up by a turn, across by a scaling, down, back. On the plane the loop closes, the two slides
  commuting; in space it closes too, since a scaling by one factor commutes with every turn. A scaling anywhere in a loop
  changes only the loop's overall size.
- *Two turns about different axes.* A turn α about one axis, β about another at angle φ, each undone: the loop comes home
  turned by Θ with cos(Θ/2) = 1 − 2·sin²(α/2)·sin²(β/2)·sin²φ, about αβ·sin φ when small (1.741° at 10° and 10°, against
  α·β = 1.745°), about the axis square to both; bounded however often repeated. This is the sphere of directions' own
  leftover, holonomy; in the plane the same loop leaves nothing.
- *A turn and an unequal stretch.* A turn α with a stretch that scales one axis by c and leaves the other (two axes drawn
  at V = cH): the loop's net map has eigenvalues e^(±ζ), cosh ζ = 1 + 2·sin²α·sinh²(½ ln c), about |α·ln c| when small,
  the same at c and 1/c. It is a squeeze of rapidity ζ up to a turn (its largest stretch is somewhat more: at α = 0.3,
  c = 2, 0.220 against ζ = 0.209), and repeated n times it is nζ. It closes only at c = 1.

So a loop of a turn and a scaling comes home unchanged exactly when the scaling is in one length; the one-length circle is
what a closed loop looks like on the blueprint. **Checked** (BRL; the trace reading of ζ checked 10 Nov).

**Two boosts joined.** Along one axis two boosts share their fixed points, the stars straight ahead and behind, and each
is a slide of the same pseudorapidity ξ, so their rapidities add and the velocity law, (β₁ + β₂)/(1 + β₁β₂), is the
blueprint's tanh of the sum. Along two axes no single coordinate carries both slides, and the join leaves a turn: the
Thomas–Wigner rotation, tan(Θ/2) = ab·sin φ/(1 + ab·cos φ), a and b the tangents of the half rapidities and φ the angle
between them, the area of the velocity triangle in hyperbolic space. It is inferred from directions alone: three stars before
and after are the evidence, they fix the map of the sky, and its turn is the rotation, from any three stars, with no frequency and no distance.
No single boost has any; the turn belongs to the join, a map between the two looks (D7), not an extent. For a small loop it is ε²·sin φ, the size of the two-turn
loop's leftover, about the opposite axis: curvature −1 against +1. At the next order they part: the turn loop's
correction is −ε²/12 at every angle, the boost loop's (1/3 + cos φ/4)·ε². The split does not derive the Lorentz group:
it enters with the premise that a change of standpoint by motion keeps the angles between nearby stars, so that every such
map of the sky is a Möbius map (Liouville). **Checked** (TWG, to 10⁻⁵⁸); classical (Thomas 1926, Wigner 1939).

## 9. Which numbers belong to whom

**Rates, not angles.** A carpenter calls a roof "six in twelve", a road sign says "10%", a ramp is built "one in
twelve". None says an angle. The pitch is a ratio, had at once; the degrees are a share of the whole turn, and to state
one you must hold the whole turn first. A rate is of something per something: the *per* is the sweep's, a direction,
read; the *of* is the payload. The Cauchy is the law of the per against itself, the turn's speed through the readings with
no payload in it.

**The blueprint's measures of the sweep.** The angle is arc per radius, measured against the completed turn: the blueprint's
rate is 1. A hand swept from horizontal to vertical can pivot two ways. From the centre of the circle on the chord (the
*central* sweep), it turns twice as far as its direction does, arc over chord θ/sin θ running from 1 to Ω at the far
end. From home on the circle (the *inscribed* sweep), chord over arc sin θ/θ runs from 1 to 1/Ω, approached at the
horizon. Their product is 1 at every θ. These are the only two standpoints from which equal turns cut equal arcs (Euclid
III.20). So the sweep is measured at Ω or 1/Ω, never at 1; 1 is had only by joining both. Ω and 1/Ω are the
blueprint's measure of the read's sweeps, not numbers a read holds. At the corner three things coincide: v fills as
fast as h empties; v/h = 1; and 1 is the geometric mean of Ω and 1/Ω, the fixed point of the reciprocal that exchanges
the sweeps. The running rates there are 1.1107 and 0.9003, not 1. **Classical**; the assignment is a reading.

**Tangent addition is the read's; tan and arctan the blueprint's.** Evaluating tan or arctan converts between a direction
and an angle, a share of the whole turn. A read composes directions by tangent addition, (a ⊕ b) = (a + b)/(1 − ab),
ratios to ratios; turns a reading over, s to 1/s; and orders readings. That is enough. Trigonometry as a whole is the
blueprint's tool: it counts the places read and closes the turn, both of its signs held at once. The arctangent does one
thing more, and worse: it eliminates the sweep. It names a single place on the turn, a third of the way to the horizon
say, as though that place could be gone to directly. It cannot. A direction is had only within its sweep, with every
direction between it and home had before it; the sweep starts at home and there is no other way in. So the arctangent
is kept for the blueprint's formulas and avoided elsewhere.

**Run as code.** A first-person view can be run this way. Turning, projecting, picking and walking call no trigonometric
function: a turn is a half-slope p/q, its rotation the rational pair ((q² − p²)/(q² + p²), 2pq/(q² + p²)); a heading is a
whole number of such steps. No π enters the loop: the rule that keeps a thing needs only ratios, the heat's 1/(2π)
cancelling and √cosh(ln ρ) being √((ρ + 1/ρ)/2). What stays is the one square root, √(1 + s²), in normalizing a direction
and in the heat's 3/2 power. What it buys is exactness: the three pair slopes multiply to exactly 1, scaling the world
moves none of them, a walk retraced comes back exactly, and places stay exact 10¹⁰⁰ units out. What it costs: fractions
grow digits, so the observer's place is put down on a grid at each change of heading (a write); turns come in steps; exact
fractions are slow beside floating point; and classical fixes (an integer heading with a sine table, a floating origin)
reach the same ends another way. For these key things the read is simpler, in the kinds of thing it needs (fractions and one
square root, no angle, no transcendental number), and that simplicity counts for its own sake. **Checked** (`thumbs-walk.html`, `sky-city.html`: 0 trigonometric calls in 300 steps;
100 of 100 walks retraced exactly; TWK, PWL).

**Two 1's.** On the axes the three ways to measure a direction of the square agree: the largest component (the cube's),
the sum h + v (the diamond's) and the length √(h² + v²) (the circle's) all give 1. At the corner they part: 1, 2 and √2.
A 1 needs a measure; the turn picks the round one, and √2 is the geometric mean of the other two (Hölder:
‖x‖₂² ≤ ‖x‖₁‖x‖∞, with equality on the axes and the corner's diagonals). **Classical.**

**One length, counted, makes the rationals.** From H alone, counting thumbs, taking twice a thumb or half a thumb and
ratios of thumbs to thumbs give rational multiples of H: extents. A pure read holds directions and their order; its
operations (the reciprocal, tangent addition, the order) take directions to directions and keep a rational direction
rational. The corner is 1, met whole.

**Two lengths make square roots.** √2 first appears as the diagonal of a square, the length of [1 : 1]: Pythagoras
combines two independent lengths through their squares, which needs two axes held at once. Bisecting a direction is of
this kind: the reading halfway to s is (√(1 + s²) − 1)/s. Halving a length is the read's; halving a turn is the
blueprint's. Square roots, nested as deep as one likes, are what two lengths and a straight edge and compass give, not every
algebraic number (the cube root of 2 is beyond them; Wantzel 1837). **Classical.**

**A limit makes the transcendental numbers.** The algebraic numbers are closed under every finite operation, so a number
that is not algebraic is reached as a value only through a limit, by one for whom that infinity is finished; as a
definition it can be finite and exact, and it may have a short name (tan 1, or Ω = 2·arctan 1). A read meets the
direction tan 1 whole; only stating it as a number needs the limit.
- *Ω completes the sweep.* A read meets the corner as s = 1, exactly. Its angle is Ω/2 = 1 − 1/3 + 1/5 − … (Madhava,
  Gregory, Leibniz), every partial sum a fraction. Machin's identity shows the split with no rounding: the direction 1/5
  composed with itself four times by tangent addition is 120/119, and 120/119 taken back by 1/239 by tangent subtraction
  ((a − b)/(1 + ab)) is exactly 1, the corner: finite, rational and the read's. Ω comes next, from the arctangent's
  series. Viète's product shows it from the other side: 1/Ω a product of nested square roots, the whole only in the limit.
- *e completes the scale.* A read reads a far thing as a ratio, one in eight; counted in thumbs, 8 thumbs out, past
  two, four and eight, it is an extent. That count as a continuous quantity is the logarithm, and to give it a value is to
  choose a unit and finish a series: one stretch where the reading halves is ln 2 = 1 − 1/2 + 1/3 − … nats. e itself is
  Bernoulli's limit, (1 + 1/n)ⁿ, or 1 + 1 + 1/2! + 1/3! + …, every term a fraction.

**Euler's formula as a count of reads.** The two limits are one construction on two axes. Cut a turn into n equal reads,
each [1 : θ/n], and compose them by tangent addition: in complex numbers, (1 + iθ/n)ⁿ, exact at every n and rational
whenever θ/n is. As n grows it becomes e^(iθ), by the same limit that takes (1 + 1/n)ⁿ to e: one compounds along the
thumb, the other square to it, both missing their limit by the leading term −w²/(2n), w = 1 or iθ. At every finite n the
count falls short of the angle, exactly by θ − n·arctan(θ/n), θ³/(3n²) to leading order, and stretches the length by
(1 + θ²/n²)^(n/2), θ²/(2n) to leading order, which no reading sees. A thousand reads of π/1000 land at −1.005, on their way
to e^(iπ) = −1. In space, alternating small steps about two thumbs leaves a turn of order 1/n,
(θ₁θ₂/2)·sin(φ/2)/(φ/2) for a whole turn φ; in the plane none. **Classical** (Euler 1748; Trotter 1959); **checked**
(ELM); the reading (each finite count a read, the limit the blueprint's) is ours.

**Read, write, read, write.** The product is also the two acts in turn. Each factor 1 + iθ/n is one read, a slope and
nothing else. To multiply the next factor on, the look so far has to be there to start from, kept in something, and what
is kept is a write (§1, D7); the next read is taken from it. So (1 + iπ/n)ⁿ is read, keep, read, keep, n times: what is
read is then written, and what is written is then read (§7, "Write once, then read again"). The n is a count laid
over the kept looks, not a write itself. Euler's identity is that alternation carried to its limit: π the turn
completed, e the scale completed, i the corner, where a step along the thumb becomes a step square to it, and −1 the
opposite facing; twice over, e^(2iπ) = 1, the cycle is home. No cycle anyone makes is the identity. At every finite n
the product is near −1 and off it, as above; the identity is what the cycle is a cycle toward, and it is the blueprint's.
The form with no limit in it is two corner steps, i × i = −1 (below). **A reading** of the classical product (ELM).

**The Cauchy's constant, from the same turn.** The quotient that took the length away, w = (1 + is)/(1 − is), does more,
in three exact steps. For every real s, |w| = 1: w = (1 − s² + 2is)/(1 + s²), both parts rational for rational s. With
s = tan θ, w = e^(2iθ). Following the logarithm continuously as s runs on from 0, (1/2i)·d(ln w)/ds = 1/(1 + s²): the
kernel is the rate at which the arc turns per unit of reading. From home to the horizon ln w gathers iπ, so
∫₀^∞ ds/(1 + s²) = Ω, and the half-Cauchy's 1/Ω is one over that gathered arc; over the whole line w goes once round
and the total is π, the standard Cauchy's 1/π. The constant comes from the identity, the logarithm and the change of
variable together, and enters in no single read, only in the completed total. Composing reads multiplies their w's,
(1 + ia)(1 + ib) = (1 − ab) + i(a + b), tangent addition, closed among complex numbers with rational parts. **Classical**
(Cayley 1846; the residue theorem); where the constant enters is the reading.

**One pole, the constant and the phasor.** Put the standpoint anywhere, z = m + iγ, γ > 0; its kernel
(1/π)·γ/((s − m)² + γ²) has one pole above the line, at z. Weight it by e^(its), t ≥ 0, close the line through the upper
half-plane, and the residue at z is all that is left: e^(izt) = e^(imt − γt). For t < 0 the line closes below, round the
mirror pole at z̄, and together e^(imt − γ|t|). At t = 0 the phasor is 1, the normalized total (π for the unnormalized
kernel). This unity is the Cauchy's alone among familiar kernels: a double pole (Student's t with three degrees of
freedom) gives (1 + t)·e^(−t), not a phasor; two simple poles beat; the hyperbolic secant's endless poles give a series
that does not total term by term; the Gaussian and Laplace kernels have no point off the line at all. Here t is the
transform's variable, dual to position on the line, not time. **Checked** (OPL, to 25 digits at z = 0.7 + 0.4i,
t = 1.3); classical by uniqueness of the transform; that the one pole is the standpoint is our reading.

**Four identities, one exchange.** Four equations state the completed joins: h² + v² = 1, e^(iπ) = −1, Ω · 1/Ω = 1
and (1/Ω)·∫₀^∞ ds/(1 + s²) = 1. Each is the blueprint's completion of something a read holds without Ω, rational in the
slope, and each of those is a fact about the exchange s ↔ 1/s, whose fixed point is the corner.

| | the blueprint's form | the read's form, rational in s | what it says of the exchange |
|---|---|---|---|
| the circle | h² + v² = 1 | 1/(1 + s²) + s²/(1 + s²) = 1 | the heat in the v/h chart and the heat in the h/v chart share one whole |
| the half turn | e^(iπ) = −1 | w(s)·w(1/s) = −1, w = (1 + is)/(1 − is) | a direction and its reciprocal compose to the half turn |
| the two facings | Ω · 1/Ω = 1 | s · (1/s) = 1 | the exchange undoes itself; the corner is its fixed point |
| the total | (1/Ω)·∫₀^∞ ds/(1 + s²) = 1 | ∫₀¹ ds/(1 + s²) = ∫₁^∞ ds/(1 + s²) | the corner splits the heat in equal halves |

*The circle.* The heat per unit of s is h² = 1/(1 + s²); in the turned-over chart t = 1/s it is 1/(1 + t²) = s²/(1 + s²)
= v². So Pythagoras, in squares, is the two charts' heats adding to one at every direction, with no root in it; the root
enters only for h itself. *The half turn.* w(1/s) = (s + i)/(s − i) = −1/w(s), so the product is −1 at every s; at the
corner it is i·i = −1, the corner composed with itself the horizon. *The total.* Putting s = 1/t carries the heat below
the corner onto the heat above it: a read has "half and half" without "Ω/2 and Ω/2". *The two facings* is the plain
one, as its blueprint's form is: its content is which facing each factor belongs to (above, "The blueprint's measures of the
sweep").

So a read holds one fact four ways, the exchange and its corner, and the blueprint's four equations are what that fact
becomes once the horizon is reached and the total stated: Ω is the price of turning "equal halves" into "how much". The
first holds at every direction, so one read has it, in squares; the other three need the horizon reached, which no read
does. They are also one chain: divide the blueprint's circle by the thumb, 1 + s² = 1/h²; its reciprocal is the heat; the
heat gathered to the horizon is (1/2i)·ln w with w reaching −1, the arc Ω; closed by 1/Ω it is 1. And squares are the
read's where roots are the blueprint's: w = (h + iv)² = (h² − v²) + 2i·hv is rational in s and h + iv is not, the doubling
and the halving of §1; h² − v² and 2hv are the double slit's predictability and visibility (§11), |w| = 1 their bound met.

The Gaussian shows the same split from the blueprint's side. In polar form (1/2π)·e^(−r²/2) dx dy =
(dθ/2π)·(e^(−r²/2) r dr): the uniform turn, whose slope is the Cauchy, times a law for the length, an amount, the payload.
Two independent zero-mean Gaussian amounts of one spread, divided, give the standard Cauchy; of spreads in a ratio c, a
Cauchy of scale c. Dividing by the thumb integrates the length away, taking e with it and leaving Ω. So the Cauchy is a
law of directions, a heat made a probability only when it is closed, on the blueprint, and the Gaussian a law of amounts.
**Classical**; the read's forms checked by hand; the assignment is a reading.

**Reading is 1/Ω; walking is Ω.** The two numbers sort by act. *1/Ω is what turning sees*: over the quarter turn the
thumb's share h averages 1/Ω, the mean of what is seen of one thumb from a standpoint that never moves; it is the constant
that closes the heat, and it is approached at the horizon, never reached. *Ω is what walking counts*: the quarter arc
from all of h to all of v is Ω thumbs long, the heat gathered to the horizon, ∫₀^∞ ds/(1 + s²), reached at a named
point, −1. An arc in thumbs is a length against the thumb, unmoved by scaling and held by no single read: of the kind D3
calls an extent, here counted out, so a count; with the thumb in a unit it is a write (D4). The sweep whose arc that is,
the central one, is itself a read: one hemisphere, from the bounded thing's centre, facing its rim. So both numbers belong to
single-hemisphere reads, 1/Ω to the inscribed and Ω to the central, and the walk is how the second one's arc is
counted. Their product is 1, which is also the blueprint's number, the thumb in thumbs; the blueprint itself, the dual hemispherical vantage, has no standpoint and
is neither of them. The exchange swaps the two, and they agree only at the corner, where a length walked and a
ratio held say the same (§6). Both numbers are limits, their values held by no read or count; what is sorted is
which read each one measures. In the table above the total's 1/Ω is the inscribed read's factor and its Ω the central
read's, and "the two facings" are those two reads. **Classical** (the mean share and the arc); the assignment is a reading.

**The thumb, short by reading, long by walking, and whole.** Said most simply: the true size is 1, the thumb in thumbs.
Reading gives the short side of it, 1/Ω; walking gives the long side, Ω; the two together give back the 1. The proof is
one line, in the blueprint's terms. Along the sweep, from all of h to all of v, each step dℓ of the arc gains v at the rate
dv/dℓ = h: what is read at a place, the thumb's share h, is the rate at which the thumb is gained per step walked there.
Summed over the walk the gain is all of v,

∫ h dℓ = 1,

and a sum is a mean times a length: (mean of what is read) × (length walked) = (1/Ω) × (Ω) = 1. The 1 owes nothing to the
circle. On any path from the one end to the other the gain per step, summed over the steps, is the whole of v, so the mean
rate times the length is 1 on every path; only the split between the two factors is the path's:

| the path | mean gain per step | length walked | product |
|---|---|---|---|
| the chord, straight across | 1/√2 | √2 | 1 |
| the quarter arc, the one length turned | 1/Ω | Ω | 1 |
| the square's two edges | ½ | 2 | 1 |

The arc is the one path on which the gain per step is the share itself, h, the same thumb turned and never stretched; so
Ω is what the split costs when the path is the turn. In space the split has no Ω in it: one thumb seen from every
direction of space averages ½, and the correction is 2 (the wedge's numbers, §8). So "Ω is the price", above, is the
plane's price. Three cautions keep the statement exact. The 1 is the thumb, H in H, not V*: nothing here gives the
mountain's size (D4). One read is one share h; 1/Ω is their average over the turn, a sum, so a limit the turning tends to and no read holds. And the walk
here is counted in thumbs, an extent as a count; it is an amount, a write, only once the thumb has a unit. The mathematics is old: the mean
projection of a segment over all directions is 1/Ω of its length (Cauchy 1841), a curve's length is Ω times its mean
projection (Cauchy 1841; Crofton 1868), and Buffon's needle (1777) is the same 1/Ω met as a chance. What is ours is the
assignment: the short factor to the read, the long one to the walk, their product to the two held together.
**Classical**; the assignment is a reading.

**The same 1 on the road.** §6's walk to the mountain has a 1 of this kind, and it is the square's row of the table, not
the arc's. Take the reading as shares with the larger one full. Far off the thumb's share is full and the mountain's
fills: from x₀ corners out to the corner it gains 1 − 1/x₀, all of it only for a walk begun without end. From the corner
to the foot the mountain's share is full and the thumb's empties, by the same amount at every stride: one stride's step
times the count of strides is exactly 1. Whole, that is ½ × 2. So the two 1's are one statement in form, a mean step
times a count of steps is the whole crossed, measured in itself (the thumb in thumbs here, the corner's distance in
corners there); and two in content, since the walker's steps are even in strides and the turn's are even in turn. The
walk never has the arc's split: weighed by strides, the thumb's mean share from the corner to the foot is √2 − 1, not
1/Ω. Ω comes with the turn's measure and with nothing else. The table has a twin as well: on every path the thumb's
share empties by exactly 1 as the other fills by 1. One caution: each of these sums is a sum of differences and equals
the difference of its ends whatever the steps, so the 1 itself cannot fail; what the check could have failed on is which
path the walk is, that its steps there are even, and that its split is not the turn's. **Checked** (ONE, exact).

**Ω of relations and four facings make a circle.** The quarter turn is every way the vertical and the horizontal can
relate, one slope s from all of h to all of v; weighed by the turn's heat and summed, those ways come to Ω. A relation
is never negative, so that is all of them. The circle is the same quarter turn four times, once for each choice of sign
for h and v, joined on the blueprint: four of them, 4Ω. The relation is continuous and the read's; the facing is a choice of
signs, discrete, the blueprint's join (one array per facing, essay 10 §2), a second kind of thing and not a second dimension. In
space the count is the same one step up: the wedge holds Ω of directions, the signs of h, v and v₂ give eight facings,
and eight of them, 8Ω, are the sphere. The Ω is the turn's weighing; summed along the chord the same ways come to √2, along the
square's edges to 2. **Classical**; the wording is a reading.

**What is free, and what Ω costs.** Two things have to be kept apart here. The geometry is prior to any physics and
free: the relation of the vertical to the horizontal, every slope from all of h to all of v; the exchange s ↔ 1/s and its
corner; the heat's equal halves either side of the corner; the four facings; and the 1, the thumb in thumbs, which the
short side and the long side give back whatever they are. None of these moves when the world is scaled or when what
arrives is changed, none was measured, no step is taken and no algorithm run to have them, and they take no time, since a
read holds none (§3, "What a read is"). They are the read's forms of "Four identities, one exchange", rational in s.

The numbers Ω and 1/Ω are not free. Ω is a limit, transcendental ("A limit makes the transcendental numbers", above): no finite count of steps gives its value, only
ever a fraction near it, each further digit at a further cost, the whole of it at an infinite one. It can be named
exactly, as the total of the turn, and the name used; what cannot be had in finite time is the value. So the sweep
only seems to hand over Ω at no cost. What it hands over free is that there is a whole, split in equal halves at the
corner, and that the read and the walk multiply to 1; how much the whole is, and so how short the short side and how long
the long side, is the blueprint's completed sum. That is the exact sense of "Ω is the price", above: the price is an
infinity, paid only at the limit, and a read never pays it because a read never needs the value.

So there are two acts, and the classical statement set beside them for comparison. A read has slopes, the corner and equal halves; it does not use Ω, and 1/Ω is the limit its share of the thumb tends to as the sweep runs on toward the horizon ("Reading is 1/Ω; walking is Ω", above). A count
is of a walk actually made, and any such walk is finite, so a count holds fractions: 11/7, 355/226, a series
stopped at some term, each nearer Ω and none of them Ω. A count uses Ω's name and its approximants, and never has its
value; Ω is the limit it tends to, stride by stride. So Ω and 1/Ω are limits the two acts actually encounter, each
headed for its own and neither reaching it. What neither encounters is π, two sweeps joined: the blueprint's, every
facing at once, the total of a sum no one finishes. The blueprint, whole, is therefore a limit, as the exact V is (§6,
"Extents come by degrees"), and never a thing anyone has made. What is exact is that Ω is defined as the total of one
sweep, and reached by no finite sweep or count.

The equation Ω × 1/Ω = 1 is then worth a second look, since it names the read and the walk and neither a read nor
a count has Ω's value. It does not need Ω. The two factors are reciprocals, and x × (1/x) = 1 for every x: Ω is in
both and leaves the product. The proof above says the same, since the 1 is the whole gain, fixed first, and the chord
and the square's edges split it with no Ω in them. A read, a count and, for comparison, the blueprint each hold the equation in their own form:

| who | what it holds of Ω × 1/Ω = 1 |
|---|---|
| a read | s × (1/s) = 1: the exchange undoing itself, no numbers |
| a count | (p/q) × (q/p) = 1: exact with any fraction held for Ω, 11/7 × 7/11 as well as a better one |
| the blueprint | Ω × 1/Ω = 1: the same fact with the turn's split named at its true value |

A better fraction changes both factors and leaves the 1 untouched, so the 1 is exact at every stage of approximation and
never waited on the limit. Ω's value is the one part of the equation no read or count reaches, and the one part the equation does
not depend on: it is the price of saying how the turn splits the 1, and no one pays it to have the 1.

Euler's identity goes the same way: the −1 never needed e or π. The corner is the quarter turn, exactly and with no root
in it: w(1) = (1 + i)/(1 − i) = i. Two corners composed are the half turn, i × i = −1, a finite and rational statement.
e^(iπ) = −1 is that fact with the arc given a length, π, and the composing written as an exponential, base e:

| who | what it holds of e^(iπ) = −1 |
|---|---|
| a read | w(s) × w(1/s) = −1; at the corner i × i = −1: the exchange, no numbers |
| a count | two corner steps land on −1 exactly; finer equal steps, (1 + iθ/n)ⁿ with fractions for θ, land near it and never on it |
| the blueprint | e^(iπ) = −1: the limit of the finer steps, the arc named π and the base named e |

Here a count is exact only at the corner, where with the product any fraction would do. The only turns whose
slope is rational and which are a rational part of the whole turn are the multiples of the corner's (Niven 1956), so
equal rational steps finer than the corner never land on −1; and (1 + iθ/n)ⁿ misses as "Euler's formula as a count of reads" says, above, the
turn short by about θ³/(3n²) and the length over by about θ²/(2n). The corner is the one finite door to −1, and
everything finer is an approach. So the values of e and Ω are the two parts of the identity no read or count reaches, and the two parts
the fact does not depend on: Ω the price of saying how long the arc to −1 is, e the price of saying it as one smooth
turn where a read has two corner steps. **Classical**; the assignment is a reading.

The read's form shows three things the classical statement does not. First, Euler's identity is one member of a
family, and the extreme one. w(s) × w(1/s) = −1 holds at every slope, pairing each direction with its exchange. Put
s = 0: home lands at +1 and its exchange, the horizon, at −1. So e^(iπ) = −1 says that home and the horizon are an
exchanged pair, and it is the only pair of the family that needs the horizon, which no read reaches; every pair
between is finite and exact, and the classical statement does not mention them. Every pair between has a standpoint: it
is two directions of one read. The identity is the one member with none, the family completed, and so the one member
that carries π and e, which are how completeness from no standpoint is put into numbers. Second, the corner's member is
i × i = −1. The corner is its own exchange and lands at i, so the equation that defines i is this identity taken at
the corner: i is the corner. Third, with the complex notation taken away almost nothing is left. Exchanging h and v
swaps the two shares, so their difference h² − v² changes sign while their product is kept. At home the difference is
+1, all h; at the horizon −1, all v. That is the whole content of the −1: the shares swapped. The classical statement
reads it as a position, half way round a dial; for a read there is no travel in it and no dial, only a pair of
directions of one read. And it is the exchange's one fact in a second chart: on the slope it reads s × (1/s) = 1, on
the landing point w × w′ = −1, the 1 and the −1 of "Four identities, one exchange".

The Cauchy's total is the cleanest of the three, since most of what the Cauchy is never touched Ω. The heat at each
slope, 1/(1 + s²) = h², is rational in s; so is the ratio of the heat at any two directions, (1 + s₂²)/(1 + s₁²); the
corner is the median because the heat below it equals the heat above it; there is no mean; and every statement of order
stands as it is. Ω comes in at one place only, the constant 1/Ω that makes the heat a probability per unit of slope:

| who | what it holds of (1/Ω)·∫₀^∞ ds/(1 + s²) = 1 |
|---|---|
| a read | the heat 1/(1 + s²), and equal halves either side of the corner; no total |
| a count | shares by count: of K equal turns, k below a slope, k/K; fractions near 1/Ω for the constant |
| the blueprint | the total closed to 1, the constant 1/Ω named |

A share is a turn over a turn: the share of the heat below a slope is the part of the quarter turn below it, and counted
in turns it needs no Ω to be defined. Ω enters when the turn is laid out as a length per unit of slope. The corner is
again the one exact door. The only rational slopes whose share is a rational number are 0, 1 and the horizon, with
shares 0, ½ and 1 (Niven 1956); the quartiles are exact as well, but at √2 − 1 and √2 + 1, by one square root, the
halving of a turn (above). And a count's sum is on the page: the heat below the corner is Gregory's and
Leibniz's series, 1 − 1/3 + 1/5 − 1/7 + … = Ω/2, each partial sum a fraction, only the limit Ω/2. The read's equal
halves say the whole is twice that sum without summing it. So across the three:

| the identity | the free fact | a limit, reached by no read or count |
|---|---|---|
| Ω × 1/Ω = 1 | s × (1/s) = 1 | Ω |
| e^(iπ) = −1 | i × i = −1 | e and π |
| the Cauchy's total | equal halves at the corner | 1/Ω |

The circle, the first of the four, comes out differently, and the difference completes the set. h² + v² = 1 has no Ω in
it. In the read's form, 1/(1 + s²) + s²/(1 + s²) = 1, it is rational in the slope and holds at every direction, so one
read has it and no horizon need be reached: for the identity itself there is nothing to pay. The cost comes elsewhere,
and in two grades. The shares themselves are roots, h = 1/√(1 + s²), usually irrational; and how much circle there is,
the length 2π and the area π, appears only when the four facings are joined and the whole measured.

| who | what it holds of h² + v² = 1 |
|---|---|
| a read | the squares, 1/(1 + s²) + s²/(1 + s²) = 1, at every direction |
| a count | exact points wherever 1 + s² is the square of a fraction: the Pythagorean triples, s = 3/4 giving h = 4/5, v = 3/5 |
| the blueprint | the circle whole: every point, its length 2π, its area π |

Here the corner flips. In the other three it was a count's one exact door; on the circle it is the landmark
a fraction cannot reach. Home and the horizon are exact points, and the triples give exact points as near together as
one likes, but at the corner h = v = 1/√2. A read has the corner exactly in squares, ½ and ½; the blueprint has it as a
construction, the diagonal of the square, and not as a count. So the four together show three grades of cost, the
sorting this section began with:

| the grade | what it buys | an example |
|---|---|---|
| free, rational in s | the four forms of a read | ½ + ½ = 1 at the corner |
| a square root, a finite construction | the shares themselves; halving a turn | 1/√2, √2 − 1 |
| a limit | how much the whole is | Ω, e |

A square root is not a limit as Ω is: it is exact as a length made in one step from two lengths, so it is the blueprint's
and not only the blueprint's.

The Gaussian, the law of amounts (above), shows where its π and its e each come from. In polar form it is a turn times a
length, (1/2π)·e^(−r²/2) dx dy = (dθ/2π) × (e^(−r²/2)·r dr). The turn's part carries all the π: the 2π is the circle
whole, Ω of relations in four facings, and an amount, having both signs, needs all four. The length's part carries
the e and totals a plain 1, ∫₀^∞ e^(−r²/2)·r dr = 1, with no π in it. So the Gaussian's π is the circle's and nothing
else; the same split is why the square of ∫ e^(−x²) dx is π, a full turn 2π times a half.

| who | what it holds of the Gaussian |
|---|---|
| a read | only the direction of a pair of equal-spread amounts: uniform by turn, the Cauchy, its median the corner; nothing of the length |
| a count | counts: the binomial, C(n, k)/2ⁿ, every value a fraction, its mean n/2 and its variance n/4 exact |
| the blueprint | the bell itself, e^(−x²/2)/√(2π): the limit of the binomial, with e and π both |

The count's tier is de Moivre's (1733): tossing and counting is what counting does, and the Gaussian is
what the counts tend to. Ω arrives in that limit through Wallis's product (1656),
Ω = (2·2)/(1·3) × (4·4)/(3·5) × (6·6)/(5·7) × …, every partial product a fraction: the walk's Ω, reached by
counting. And what is exact flips once more. For the Cauchy the exact facts were the median and the equal halves, and
there was no mean; for the Gaussian the exact facts a count holds are the mean and the variance, which are
sums. The Cauchy is kept by order and the Gaussian by sums, a law of directions and a law of amounts. This is no fifth
read's identity: a read holds nothing of one Gaussian amount, only the direction of a pair, which is the Cauchy it
already had.

Between the two laws lies a whole family, Student's t (Gosset 1908). One Gaussian amount z is divided by the root mean
square of ν others, t = z/√((w₁² + … + w_ν²)/ν). At ν = 1 it is the Cauchy; as ν grows it becomes the Gaussian. Three
things about it sort cleanly (exact checks in the STT plan, Code and data). First, t is unmoved by scaling at every ν:
t/√ν is one share against the length of the others, the slope of one direction among ν + 1 equal parties, and the
direction is uniform. So nothing is written anywhere along the family, and ν is not how well a divisor is known; it is
a count of parties. Second, no finite ν has an e. The density's shape is (1 + t²/ν)^(−(ν+1)/2), rational
in t or the square root of a rational, and e arrives only as Bernoulli's limit (1 + x/n)ⁿ, the gap from e^(−t²/2)
falling as 1/ν. The Gaussian is then the blueprint's in a second sense: one party's share among endlessly many, a
classical limit (Maxwell; Borel 1914). Third, the π comes and goes with the parity of ν: the height at t = 0 is 1/π,
2/(π√3), 8/(3π√5) for ν = 1, 3, 5 and 1/(2√2), 3/8 for ν = 2, 4, with no π at all. The turn's constant belongs to the
plane's pair; among more parties the constant is a ratio of two spheres' measures, and it holds π only when the
count of parties, ν + 1, is even.

So e reaches these equations in two ways, and they should be kept apart. It can be in the law: the Gaussian's length
(with u = r²/2 the length's part is the plain exponential e^(−u), the Gaussian's other half as the Cauchy is its
direction), where it is forced by squares that add and chances that multiply. Or it can be in the chart only: write the
slope as s = e^ξ, the blueprint's logarithm, and the Cauchy reads (1/π)·sech ξ and the share h² = 1/(1 + e^(2ξ)), a
logistic curve. Neither law gained anything; the chart supplied the e, and the read's forms, 1/(1 + s²) and the
equal halves, have none.

The same three charts hold the standard examples of chaos, as one map. Add a turn to itself. In the slope that is
tangent addition of s with itself, s ↦ 2s/(1 − s²), rational, with no Ω and no trigonometry: one step of it is the
read's own. In the reciprocal slope it is Boole's map, c ↦ ½(c − 1/c) (1857), which is also Newton's step for
c² + 1 = 0, a search for the standpoint i that no slope on the line reaches. In the share v² it is the logistic map,
y ↦ 4y(1 − y) (Ulam and von Neumann 1947). In the turn's own share it is the tent map. Each keeps the uniform turn's
law in its chart: the Cauchy, the Cauchy, the arcsine, the uniform. In the tent map every step spreads nearby starts
by exactly two, away from its one fold. In the other charts the stretch of a single step varies from place to place
(the logistic map's is 4·|1 − 2y|, nothing at y = ½), and what the charts share is the average of its logarithm over
the unchanged law, ln 2 a step, the Lyapunov rate, the same in every chart. All of this is classical; what the sorting into a read, a count and the classical statement adds is who
can follow the orbit (the CHS plan, Code and data, exact).

| who | what it holds of the orbit |
|---|---|
| a read | one step: a slope added to itself, exact and rational |
| a count, in fractions | every step exactly, at a cost that doubles each step (from 3/7 the twelfth slope's denominator has 9,950 binary digits); no cycle ever, since no rational slope but 0 and 1 belongs to one (Niven) |
| a count, in p digits | about p steps (24, 53, 113 and 200 digits part from the true orbit at step p − 1 to p + 6); at a fixed fineness K each step uses up one more binary digit of the start |
| the blueprint | the direction whole: every step, and the cycles, which sit at turns that are rational parts of Ω |

So the rule is fixed and free, and the orbit is determined; what gives out is the count. Unpredictability here is a
statement about what a count can hold, one binary digit a step, not about the rule or the law. And the
Cauchy is seen a second way: it is the heat of one sweep, and it is also the one law a turn added to itself, again
and again, leaves as it was.

The quarter turn also reaches counts that show no turn at all. The sum of 1/n² over the odd numbers is exactly half
the square of the quarter turn, 1 + 1/9 + 1/25 + … = ½·Ω², and the next ones are Ω⁴/6 and Ω⁶/15. The
reason is the slope. One read runs from home to its horizon, a quarter turn in the blueprint's measure, and stops. The
blueprint, joining facings, carries the slope on, and it meets a horizon at every odd multiple of the quarter turn. Euler's
expansion (1748) writes the slope as the sum of those horizons' pulls: at a turn x, the slope is the sum over the odd
numbers m of 2x/((m·Ω)² − x²). Close to home the slope is the turn itself, so the pulls must total 1 there, and that
is the sum above. The even numbers add nothing new, the same sum over again at a quarter of the size, so the sum over
all whole numbers is ⅔·Ω², Basel's π²/6. This is why the turn's constant appears in the share of whole
numbers with no repeated prime factor, (3/2)·(1/Ω)², and in the total of a thermal spectrum: each passes through that
sum. The sorting is as before. A read holds none of it, having one horizon and never passing it. A count
holds the partial sums, each a fraction. The value is the blueprint's, a count over all the odd numbers landing on the
quarter turn squared. It was found by looking back from the answers, not predicted from the constructions: a rule
that Ω appears exactly where a turn is taken whole failed a blind test on these very cases (the TWC plan, Code and
data), and what is said here is where their Ω comes from, not a way to foresee it.

Parallax (§6) is the case where two looks together are exact and the blueprint adds only its angles. Two standpoints a
step B apart each read the target's slope off the line between them, s₁ and s₂, measured inward. The target's depth d
off that line is then given by 1/(d/B) = 1/s₁ + 1/s₂, so d/B = s₁s₂/(s₁ + s₂): slopes 3 and 6 put it exactly 2 steps
off. No angle, no trigonometry and no Ω is in it.

| who | what it holds of parallax |
|---|---|
| one look | one slope, and nothing of parallax |
| two looks held together, still a read | the extent in the step between them, a rational function of the two slopes, exact, with no count |
| a write | the step itself, a thing with a size; the step in metres, the one amount carried in |
| the blueprint | the parallax angle γ in radians or arcseconds; γ(d) + γ(a²/d) = π about the half-step a; the error's γ/sin γ, Ω at the corner; the parsec, 648000/π astronomical units |

The corner is the exchange again. The corner circle, the circle on the step as diameter (Thales), is exactly
s₁·s₂ = 1, the two slopes reciprocal; a product above 1 is inside it and below 1 outside, and that needs no count of
the step. On the circle d/B = s/(1 + s²), the circle's hv: slopes 2 and ½ give the point (1/5, 2/5), the 3-4-5 triple
once more. The error is rational too: with k = d/a, a step in direction moves the depth in proportion to
(k + 1/k)/2, the same at k and 1/k and least at the corner; cosh(ln k) (§6) is the blueprint's smooth name for it. And the
three grades sort the rest: the depth is rational, the range along a ray is a square root, the angle is a limit. Ω
enters only where a slope is turned into an angle, which is why the parsec carries a π and the extent in steps carries
none. This is no fifth identity of one look: parallax holds two looks together, and what never needed Ω is the extent in
steps; the step in metres is still the one amount carried in.

**Classical**; the assignment is a reading. Physics enters
separately, with the first write: a stride taken, a mark made, a thumb given a unit. A walk's strides are writes; the
count of them is a description. **A reading**, resting on this
section's account of the transcendentals.

**What the one pole already carried.** A read at i holds the standard Cauchy (§3). Readings added give one Cauchy
with the standpoints added, z₁ + z₂, the phasors multiplying. Parallax is a sum of reads whose depth is exactly Cauchy,
its point the triangulation of the two reads' points (§6). A cell of the floor's discarded fraction sits at its own
m + iγ, half its Cauchy in the cell (DYH). Each was reached from its own question; the residue is why each could carry z
and nothing else. A demonstrated unity for the Cauchy and its Poisson kernel, not a principle for kernels in general.

**Met, not made.** None of this keeps irrational or transcendental numbers out of the read's world. A direction whose
reading is tan 1 is a direction like any other, painted, passed, ordered; the decimal 1.5574… is the blueprint's account of
where it is. A read meets these numbers and does not make them.

## 10. A worked example: the mountain and the thumb

Hold up a thumb, one mile wide in an agreed unit, and look at a mountain range twenty miles wide, ten miles off.

**From the standpoint.** The range's ends sit at ±45°: the pair (half-width, distance) is at its corner. Of thirty-six
fingers spread evenly over the half turn, eighteen land on the range. Scale the world by a thousand and nothing in the
view moves: still 45°, still eighteen fingers.

**Mountain equals thumb.** With no V, drawing the range at its own H reads it one thumb wide at half a thumb away: the
blueprint's circle, V = H. Every amount is then off by V\*/H = 20, the same on both sides of the corner.

**The two sweeps, measured.** On the circle drawn about the thumb, the central sweep is measured at Ω and the
inscribed at 1/Ω; to the range's ends, 1.1107 and 0.9003. Their product is 1, the starting length returned, H in H. The
mountain never enters.

**Walk one thumb.** Step one thumb toward the range and read again. The half-angle's reading goes from s = 1 to
s′ = 10/9. The distance is d = H·s′/(s′ − s) = 10 thumbs and the range V = 2·s·d = 20 thumbs: extents, exactly. Count the
thumb in miles and they are 10 miles and 20 miles: writes.

**The mountain as H** (§6, "The thing itself as H"). As the unit, its ends 90° across put the standpoint half a range-width
from its middle, from one look; as the focus, a baseline of twenty miles puts it at parallax's corner, where one thumb
walked has about ten times the least error.

**In three dimensions: a tower and two thumbs.** Hold both thumbs crossed, one reading up (v/h), one across (v₂/h), the
look along h, so the middle of the cross reads (0, 0) as a camera's screen does, and look at a tower off to one side. Its
top reads (¼, ⅓), its foot (0, ⅓). From one place that is all: two directions, no distance, and a tower twice as large
twice as far off reads the same. Step one thumb across and read again: the top reads (¼, ¼), the foot (0, ¼). Only the
across thumb moved, by 1/12, so the distance along the look is 12 thumbs; the top is 12·⅓ = 4 thumbs across and 12·¼ = 3
up; the tower is 3 thumbs tall, 12 off and 4 to the side: extents, exactly. The up thumb did not move, and that is the gain
of the second thumb: in space each step gives two changes for one unknown, so one is spare and must agree (the epipolar
condition of stereo vision). Take the step for diagonal when it was across, and the up thumb says the step had no up in
it: the misreading is caught. Step one thumb forward instead and both readings grow by the same factor, the top to
(3/11, 4/11), either thumb giving 12. Scale the world, the step with it, and no extent changes. Count the thumb as 5 metres
and the tower is 15 metres tall and 60 away: the one write. **Checked** (`runs/two/two_thumbs.py`).

## 11. Cases in data, and what this changes

**What it changes.** No mathematics. It sorts.
- **Every reading is a read, every gap across an extent, every amount a write.** A result unmoved by scaling and held by
  one standpoint is a read; unmoved and needing two, an extent; moved, a write, which needs an amount carried in.
- **A Cauchy-type quantity is a direction where a turn that lays it can be named, apart from the law's shape.** A fat
  tail alone is no evidence of a turn: a mixture of amounts makes one too.
- **The constants have owners.** π and e are the blueprint's; Ω, 1/Ω and the hemisphere's 2 and ½ are
  limits the acts encounter; the Cauchy's normalizing constant, the logarithm's nats and the angle's degrees are measures
  laid over the read's things; the read's own versions are
  finite: an order, a ratio, a corner, a composition by tangent addition.
- **The acts move.** An observer reads while it stands and turns, places while it walks and counts, and has an amount
  when it agrees a unit.

**LIGO.** In open data from the two LIGO detectors (Abbott et al. 2023; 512 s, about two million whitened samples each),
each detector's signal taken alone is an amount, and its heavy tail is one loud transient on a law of finite spread: block
means shrink as n^(−½), which nothing Cauchy can do. The Cauchy is in the direction [H1 : L1] of the two read at one
instant: its median at 1, its spread unmoved by averaging, its angle near uniform, and the small departure from uniform
reproduced from each channel alone, by pairing samples 8 s apart, to 0.0001; a prediction written before the data were
fetched, which could have failed. **Checked** (LGO).

**The quasar dipole.** An observer moving through a sky of sources counts more ahead. With no limit on brightness the census
is a count of directions, and its dipole is 2β, Ellis and Baldwin's 2, from the directions alone (1984). A real census is
cut at a brightness, and the cut adds a term set by what arrives. On Secrest et al.'s quasars (2021), per slice the
expected dipole is [2 + x(1 + α)]·β, α the spectral index, the 2 the directions' and x(1 + α) the payload's: 5.3 to 6.6
times β, so the payload carries 60–70% of it. Taken as directions alone, the measured 0.018–0.023 would give a speed nearly
three times too large; with the payload's part divided out, four slices by brightness give one β,
3.3·10⁻³ ± 0.3·10⁻³, 2.7 times the speed from the microwave background, as one motion should. Slices by colour give 2.3,
2.8 and 4.6 times it, which no motion can do, so part of the dipole belongs to what arrives. The sort says which part could
be the read's, not where the dipole comes from. **Checked** (EBD), and provisional: the residual of 2.7 times the
microwave background's speed rests on the catalogue's selection, the flux cut and the spectral indices, and has not been
reproduced independently; it is a decomposition, not yet an explanation of the discrepancy.

**One photon at a time.** In a double slit the fringes' visibility is at most 2hv, h and v the two paths' shares, and the
which-path predictability |h² − v²| (Greenberger and Yasin 1988; Englert 1996): full visibility only at the corner. On
Aspden, Padgett and Spalding's frames (2016) the slits' counts, 9,026 : 10,465 and 11,993 : 11,891, give 2hv 0.997 and
1.000, and the measured contrast, 0.69 and 0.56, lies under that bound, short by the source. The bound is the shares',
the geometry's; how far below it a pattern falls is what arrives. **Checked** (WVP).

**Berry's phase.** A spin carried slowly round a closed loop of field directions comes back with two phases (Berry
1984). The geometric one is half the solid angle the loop of directions encloses: the same taken twice as slowly, in a
field twice as strong, in an apparatus twice the size. The dynamical one is energy times time and moves with all three.
Experiments have separated them by keeping the loop and changing the rest (Tomita and Chiao 1986; Bitter and Dubbers
1987). Both tests sort it. The half is the central sweep's twice the angle: a spin state at angle θ has its point on the sphere
of states at 2θ. **Classical**; not run here.

**And one where it failed.** Seeds falling from a plant also spread with a fat tail, and the turn can be named
beforehand: a seed leaving its release point straight, every downward direction alike, lands as the hemisphere's Cauchy,
Clark's 2Dt with shape p = ½ and a tail falling as r⁻³. On Bullock et al.'s compiled kernels (2017), the 35 that could be
fitted of 38 picked as wind-dispersed say otherwise: median p 0.10, a tail falling about as r⁻², and no nearer the turn's
than kernels carried by animals. The fat tail there is a mixture over wind speeds: amounts, not a turn. So the reading is
not a rule that every Cauchy-like law is a turn's heat; it holds where the turn is there to be named, and a test written
before the data can show where it is not. **Checked** (TCF; killed).

## 12. Open questions

- **O1. The name of D3's kind.** *Closed:* it is a parallax extent, "extent" for short (it was "place" until
  11 November, a working name that said position where the paper says a read has none). Its scope is fixed by D3 (a gap
  across, unmoved by scaling, needing two standpoints).
- **O2. The thumb.** *Closed (R792):* the thumb is the across axis's chosen zero, as home is the up axis's, as D5
  already requires; the record's "the read's own length" describes how it is chosen, not a different kind.
- **O3. Completed joins, and their name.** *Closed (12 November):* a completed join (π, the one-length circle, the
  facings joined) is unmoved by scaling, so it is not a write; it was called "the blueprint's" until a word was chosen.
  The word is the **blueprint**, the dual hemispherical vantage: both hemispheres at once, from no standpoint, apart from reads and writes (§1, "Reads, writes and
  the blueprint"). *Settled (R890, R891; R922):* it is neither a kind beside D1–D7 nor their sum. It has no standpoint, so
  it has nothing to do with reads and writes, and no reads or writes, finite or carried to a limit, make it; it is
  classical geometry, set beside a read's form only for comparison. *Sharpened
  (R796):* what an angle needs comes in two stages. The ratio s = v/h needs nothing; it is the read. The shares h and v
  with h² + v² = 1 need the other party held at the one length (V = H, the one-length circle): with them come
  cos and sin as the shares themselves, √(1 + s²) = 1/h, and halving a turn, t = v/(1 + h). The angle θ needs the circle
  and the turn completed as well (π, a limit): an arc over the radius, counted against the whole. Neither stage needs a
  true breadth V* or a unit, so neither is a write; both are completed joins, the circle first and π second. *And (R797):* the exact V is a third, the limit of parallax:
  unknowable against the universe, knowable across one hemisphere, known only held or written (§1, "Four things").
  *And (R798–R801):* the completed joins are the blueprint's, both hemispheres at once with no facing; four identities
  state them, and each has a read's form about the exchange and the corner (§9, "Four identities, one exchange").
- **O4. Joinings with no gap.** *Orders (R792):* an order of reads is a joining with no gap in it, not an extent.
  *Widened, and open (R825, R826):* there are at least two such joinings, and they are different structures. An order is
  a relation with no cycle. A map carries one read's directions to another's; it has an inverse and can cycle (a turn
  by the corner's slope returns after four), so it is no order, and the order of reads is something a composition of
  maps takes, not the composition (two quarter turns of space joined in the two orders land 120° apart, §8). Keeping
  order neither makes a map nor is needed for one: s ↦ s³ keeps order and is only a change of chart of one read; the
  exchange s ↦ 1/s reverses it. Not every function on directions is a map between reads. A change of chart is a
  representation (D7); a lens or the air changes what arrives (D6); a map between reads is induced by a change of
  standpoint that is not a step. That such maps are the Möbius maps is conditional: it follows from the premises of O8
  (given Lie's classification), not from reading alone. Möbius maps keep every cross ratio, and classically a map
  keeping the cross ratio of every four distinct directions is Möbius; the cases checked (ORD: nine maps, six slopes)
  illustrate that and prove nothing. The heat under a map: each read has its own heat, the same at every standpoint,
  and no map changes it; a map's stretch at a direction is the first read's heat carried by the map against the second
  read's own there, 1 everywhere for a turn, not for a boost. Open: whether orders and maps exhaust the joinings with
  no gap, and whether extents, orders and maps exhaust the relations between reads. Neither is claimed.
- **O5. Do observers put the thing looked at on the corner?** A "should" (§5), not a claim about eyes or instruments.
- **O6. A second test that can fail.** "Find the z" has passed once in data (LIGO) and failed once (the seeds). A second
  domain, where the turn can be named before the data, would show whether the rule sorts.
- **O7. The essays, the demos and *Reads and Writes in Physics*.** *Closed (R792):* all three brought to R788's kinds;
  the last place still calling an extent a write, the demos page's card for `write.html`, now says the move places.
- **O8. Why the sky is conformal.** The moving sky's Möbius map rests on motion keeping angles on the sky. SRB (runs 1–2)
  replaces that premise by four: a change of standpoint acts on directions alone, chains included; it is fixed by finitely
  many numbers; the turns are among the changes; a motion carries directions from the back toward the front. With Lie's
  classification of the finite groups on a surface (Lie 1880), these leave the Möbius maps alone; Newton's aberration fails the
  first, since two of its steps are no single step once the speed is dropped. Two of the four carry the physics: that what
  no read can hold makes no difference to what is read (the light postulate stated for reads), and that an extent is a
  finite list of numbers. Neither is shown to follow from reading. A reconstruction, not an explanation.
- **O9. The Doppler factor, and relations between standpoints.** Three things are to be kept apart. The read is the
  direction of arrival from a standpoint, its state of motion included. The relation between two standpoints, their
  relative motion among it, is described by the rapidity (§4). The ratio of the frequencies received at the two is a
  relation between payloads, and it is what is measured. The Doppler factor is fixed by the second and the direction of
  arrival; the measured ratio equals it and is still a relation between payloads. So a quantity can be unmoved by
  scaling, unmoved by a change of what arrives, and neither a direction nor a distance: D3's extent is a gap across, and
  the factor is no distance, so it is not put there. Whether relations between standpoints need a name of their own,
  beside extents and orders (O4), is open; D3 stands as it is until that is settled. Found by a blind classification
  (BCL, run 2).
  *What makes a spatial gap an extent, and two cases tried against it (R823).* A candidate, not adopted: an extent is a
  ratio of two distances between points in space, standpoints and named things, at least one of them a step between
  standpoints. A time to contact had from two reads a tick apart is exactly d₁/B, the distance over the step, so the
  number meets the candidate as it stands; what does not is its reading as a time, which needs the further premise that
  the steps go on alike, a statement about reads not yet made. The rapidity does not meet it: it is had from two reads
  at one position, by the directions alone (§4), with no step in space, and what it relates the two reads by is a map
  on directions, as a turn does. To call it an extent would change what "a gap across" means. So the time to contact is
  taken out of D3's list until its temporal reading has a stated reason, and the rapidity and the Doppler factor stay
  unclassed.
  *Since (R824–R826).* The relation between two standpoints at one position is a map (D7, O4), and the rapidity is the
  blueprint's coordinate on it, as an angle is on a turn. The Doppler factor is two variables with one value: the map's
  stretch at a direction, which is the map's and unmoved by what arrives, and the ratio of the frequencies received,
  a ratio of payloads. That they are equal is a premise of physics, not read (MBR). *Closed (R827):* §4 had said
  that from one look, given a sky uniform in its own frame, the rapidity is a read. It is not: what can be inferred
  from a read is one thing, and what kind of thing the inferred quantity is, another. The look is a read, the
  uniformity a premise about what arrives, and the rapidity inferred the coordinate of a map; §4 now says so. Not
  settled by this: whether the rapidity is always recoverable from one sky, or the assumed rest frame unique. The time
  to contact stays out of D3. *Sharpened (R921):* as d₁/B it is an extent; read as ticks still to come it is not a
  count, since a count describes writes already made and no future tick is one, though it rests on the premise every
  count rests on, that the steps go on alike. What kind the ticks to come are is still open.

## Where the ideas come from

Jaynes's principle of transformation groups (1968, 1973) gives the method: the measure an observer's ignorance leaves
unchanged. Poincaré's universe made a thousand times larger overnight (1908), undetectable from inside, is the first test;
his representative and geometric space are close to the read's and the blueprint's. Leibniz's space as an order of
coexistences (1715–16) is the read's picture; Klein's programme (1872), geometry as the study of a group, is the form of
the sort. Gibson's ambient optic array (1979) is the stained-glass window. Bridgman and Buckingham sorted quantities by
scale long before. What is offered here is the read and the write on one plane, sorted by two properties, the heat of directions and the payload inside a
read, and what carries an observer from one kind to the next.

## Code and data

The checks and measurements cited are in this repository (reportbase/wander), each with its plan written before it was
run; plan codes in the text name them. The one pole, the constant and the phasor: `plans/opl-plan.md`, `runs/opl/`. Two
boosts joined: `plans/twg-plan.md`, `runs/twg/`. Why the sky is conformal: `plans/srb-plan.md`, `runs/srb/`. Time and the Cauchy's point: `plans/tim-plan.md`, `runs/tim/`. The floor's
cells: `plans/dyh-plan.md`, `runs/dyh/`. The Cauchy's routes: `plans/cauchy-routes.md`, `runs/crt/`. Parallax as a sum of
reads: `plans/pxs-plan.md`, `runs/pxs/`. Formats as text: `plans/txt-plan.md`, `runs/txt/`. The read's math in slopes: `plans/slp-plan.md`, `runs/slp/`. The tower and two thumbs:
`runs/two/two_thumbs.py`. Three thumbs at the crosshair: `plans/thm-plan.md`, `runs/thm/`. The shape swept:
`plans/swp-plan.md`, `runs/swp/`. Three laws on the sphere: `plans/eul-plan.md`, `runs/eul/`. Euler's formula as a count of
reads: `plans/elm-plan.md`, `runs/elm/`. The three loops: `plans/brl-plan.md`, `runs/brl/`. Student's t between the Cauchy and the Gaussian: `plans/stt-plan.md`, `runs/stt/`. Chaos as the turn added to itself: `plans/chs-plan.md`, `runs/chs/`. The two completions tested blind, and the odd sums: `plans/twc-plan.md`, `runs/twc/`. The distance between
standpoints: `plans/frg-plan.md`, `runs/frg/frg.py`. A flat chart in space: `plans/flc-plan.md`, `runs/flc/`. Epicycles and
aimed terms: `plans/epi-plan.md`, `runs/epi/`. The seed kernels: `plans/tcf-plan.md`, `runs/tcf/`. The data cases:
`plans/lgo-plan.md`, `plans/ebd-plan.md`, `plans/wvp-plan.md`, with `runs/lgo/`, `runs/ebd/`, `runs/wvp/`; each records its
runs as they came out, the killed ones too, and none alone establishes the sort. Pages: `read.html`, `pinhole.html`,
`crosshairs.html`, `heat-cube.html`, `euler.html`, `approach.html`, `slide-rule.html`, `star-field.html`. The read as a
control: reportbase/calendar (`dial.js`, `dome.js`, `horizon.html`, `dome.html`, `dome-map.html`, `dome-instrument.html`).
The mountain walk's two corners and paces: `plans/breath-note.md` §5. The stride and the fixed share: `plans/wlk-plan.md`, `plans/one-plan.md`, `runs/wlk/`. The denominator paradoxes and the exchange: `papers/denominator-paradox.md`. The rewrite's map from the record and its checklist:
`plans/rw-rewrite-outline.md`. The known physics sorted by the two tests is the companion *Reads and Writes in Physics*
(`papers/reads-and-writes-physics.md`), brought to R788's kinds (§12, O7).

## References

- Abbott, R. et al. (LIGO, Virgo and KAGRA Collaborations) (2023). Open data from the third observing run of LIGO, Virgo,
  KAGRA and GEO. *Astrophysical Journal Supplement Series* 267, 29.
- Archimedes. *On the Sphere and Cylinder*, Book I.
- Aspden, R. S., Padgett, M. J. and Spalding, G. C. (2016). Video recording true single-photon double-slit interference.
  *American Journal of Physics* 84, 671.
- Baird, E., Boeddeker, N., Ibbotson, M. R. and Srinivasan, M. V. (2013). A universal strategy for visually guided
  landing. *Proceedings of the National Academy of Sciences* 110(46), 18686–18691.
- Bernoulli, J. (1690). *Quæstiones nonnullæ de usuris.* Acta Eruditorum.
- Bernstein, A. J. (1966). Analysis of programs for parallel processing. *IEEE Transactions on Electronic Computers*
  EC-15(5), 757–763.
- Berry, M. V. (1984). Quantal phase factors accompanying adiabatic changes. *Proceedings of the Royal Society of London
  A* 392, 45–57.
- Bitter, T. and Dubbers, D. (1987). Manifestation of Berry's topological phase in neutron spin rotation. *Physical Review
  Letters* 59, 251–254.
- Boole, G. (1857). On the comparison of transcendents, with certain applications to the theory of definite
  integrals. *Philosophical Transactions of the Royal Society of London* 147, 745–803.
- Borel, É. (1914). *Introduction géométrique à quelques théories physiques.* Gauthier-Villars, Paris.
- Bridgman, P. W. (1922). *Dimensional Analysis.* Yale University Press.
- Brinkman, T. (2026). *Observation from Somewhere: addresses given, payloads met.* Working paper, archived.
- Bullock, J. M., Mallada González, L., Tamme, R., Götzenberger, L., White, S. M., Pärtel, M. and Hooftman, D. A. P.
  (2017). A synthesis of empirical plant dispersal kernels. *Journal of Ecology* 105(1), 6–19.
- Burn, B. J. (1966). On the depolarization of discrete radio sources by Faraday dispersion. *Monthly Notices of the Royal
  Astronomical Society* 133, 67–83.
- Buffon, G.-L. Leclerc, comte de (1777). Essai d'arithmétique morale. *Histoire naturelle, générale et particulière*,
  Supplément, tome 4. Imprimerie Royale, Paris.
- Buckingham, E. (1914). On physically similar systems; illustrations of the use of dimensional equations. *Physical
  Review* 4, 345–376.
- Chyzak, F. and Nielsen, F. (2019). A closed-form formula for the Kullback–Leibler divergence between Cauchy
  distributions. arXiv:1905.10965.
- Clark, J. S., Silman, M., Kern, R., Macklin, E. and HilleRisLambers, J. (1999). Seed dispersal near and far:
  patterns across temperate and tropical forests. *Ecology* 80(5), 1475–1494.
- Cauchy, A.-L. (1841). Note sur divers théorèmes relatifs à la rectification des courbes et à la quadrature des
  surfaces. *Comptes rendus de l'Académie des Sciences* 13, 1060–1063.
- Cayley, A. (1846). Sur quelques propriétés des déterminants gauches. *Journal für die reine und angewandte
  Mathematik* 32, 119–123.
- Crofton, M. W. (1868). On the theory of local probability. *Philosophical Transactions of the Royal Society* 158,
  181–199.
- de Moivre, A. (1733). *Approximatio ad summam terminorum binomii (a + b)ⁿ in seriem expansi.* London.
- Ellis, G. F. R. and Baldwin, J. E. (1984). On the expected anisotropy of radio source counts. *Monthly Notices of the
  Royal Astronomical Society* 206, 377.
- Englert, B.-G. (1996). Fringe visibility and which-way information: an inequality. *Physical Review Letters* 77,
  2154–2157.
- Euclid. *Elements*, Book III, Proposition 20.
- Euler, L. (1748). *Introductio in analysin infinitorum.* Lausanne.
- Euler, L. (1776). Formulae generales pro translatione quacunque corporum rigidorum. *Novi Commentarii Academiae
  Scientiarum Petropolitanae* 20, 189–207.
- Euler, L. (1778). De repraesentatione superficiei sphaericae super plano. *Acta Academiae Scientiarum Imperialis
  Petropolitanae* 1777, I, 107–132.
- Gauss, C. F. (1828). Disquisitiones generales circa superficies curvas. *Commentationes Societatis Regiae Scientiarum
  Gottingensis Recentiores* 6, 99–146.
- Gibbs, J. W. (1899). Fourier's series. *Nature* 59, 606.
- Gibson, J. J. (1979). *The Ecological Approach to Visual Perception.* Houghton Mifflin.
- Gosset, W. S. ("Student") (1908). The probable error of a mean. *Biometrika* 6(1), 1–25.
- Greenberger, D. M. and Yasin, A. (1988). Simultaneous wave and particle knowledge in a neutron interferometer.
  *Physics Letters A* 128, 391–394.
- Haar, A. (1933). Der Massbegriff in der Theorie der kontinuierlichen Gruppen. *Annals of Mathematics* 34, 147–169.
- Hölder, O. (1889). Ueber einen Mittelwerthssatz. *Göttinger Nachrichten*, 38–47.
- IAU (2015). Resolution B2, on recommended zero points for the absolute and apparent bolometric magnitude scales
  (the parsec as 648000/π au). XXIXth General Assembly, Honolulu.
- Jaynes, E. T. (1968). Prior probabilities. *IEEE Transactions on Systems Science and Cybernetics* 4(3), 227–241.
- Jaynes, E. T. (1973). The well-posed problem. *Foundations of Physics* 3, 477–492.
- Kakutani, S. (1944). Two-dimensional Brownian motion and harmonic functions. *Proceedings of the Imperial Academy
  (Tokyo)* 20(10), 706–714.
- Klein, F. (1872). *Vergleichende Betrachtungen über neuere geometrische Forschungen.* Erlangen.
- Lambert, J. H. (1772). *Anmerkungen und Zusätze zur Entwerfung der Land- und Himmelscharten.* In *Beyträge zum
  Gebrauche der Mathematik*, Theil III. Berlin.
- Lee, D. N. (1976). A theory of visual control of braking based on information about time-to-collision. *Perception*
  5, 437–459.
- Leibniz, G. W., and Clarke, S. (1717). *A Collection of Papers … Relating to the Principles of Natural Philosophy and
  Religion.* London.
- Lie, S. (1880). Theorie der Transformationsgruppen I. *Mathematische Annalen* 16, 441–528.
- Lindemann, F. (1882). Ueber die Zahl π. *Mathematische Annalen* 20, 213–225.
- Liouville, J. (1850). Extension au cas des trois dimensions de la question du tracé géographique. Note VI in
  G. Monge, *Application de l'analyse à la géométrie*, 5th ed., Paris, 609–616.
- Machin, J. (1706), in W. Jones, *Synopsis palmariorum matheseos.* London.
- Malmquist, F. (1926). Sur la détermination d'une classe de fonctions analytiques par leurs valeurs dans un ensemble
  donné de points. *Comptes Rendus du Sixième Congrès des Mathématiciens Scandinaves* (Copenhagen, 1925), 253–259.
- McCullagh, P. (1992). Conditional inference and Cauchy models. *Biometrika* 79, 247–259.
- Mercator, G. (1569). *Nova et aucta orbis terrae descriptio ad usum navigantium emendate accommodata.* Duisburg.
- Niven, I. (1956). *Irrational Numbers.* Carus Mathematical Monographs 11. Mathematical Association of America.
- Poincaré, H. (1902). *La Science et l'hypothèse.* Paris. (1908). *Science et méthode.* Paris.
- Qian, T. and Wang, Y.-B. (2011). Adaptive Fourier series, a variation of greedy algorithm. *Advances in
  Computational Mathematics* 34, 279–293.
- Roy, W. (1785). An account of the measurement of a base on Hounslow-Heath. *Philosophical Transactions* 75, 385–480.
- Secrest, N. J. et al. (2021). A test of the cosmological principle with quasars. *Astrophysical Journal Letters* 908,
  L51.
- Shepard, R. N. (1964). Circularity in judgments of relative pitch. *Journal of the Acoustical Society of America*
  36(12), 2346–2353.
- Snellius, W. (1617). *Eratosthenes Batavus.* Leiden.
- Srinivasan, M. V., Zhang, S. W., Chahl, J. S., Barth, E. and Venkatesh, S. (2000). How honeybees make grazing
  landings on flat surfaces. *Biological Cybernetics* 83(3), 171–183.
- Staudt, K. G. C. von (1847). *Geometrie der Lage.* Nürnberg: Bauer und Raspe.
- Takenaka, S. (1925). On the orthogonal functions and a new formula of interpolation. *Japanese Journal of
  Mathematics* 2, 129–145.
- Thomas, L. H. (1926). The motion of the spinning electron. *Nature* 117, 514.
- Tomita, A. and Chiao, R. Y. (1986). Observation of Berry's topological phase by use of an optical fiber. *Physical
  Review Letters* 57, 937–940.
- Trotter, H. F. (1959). On the product of semi-groups of operators. *Proceedings of the American Mathematical Society*
  10, 545–551.
- Ulam, S. M. and von Neumann, J. (1947). On combination of stochastic and deterministic processes (abstract).
  *Bulletin of the American Mathematical Society* 53(11), 1120.
- Viète, F. (1593). *Variorum de rebus mathematicis responsorum liber VIII.* Tours.
- Wallis, J. (1656). *Arithmetica infinitorum.* Oxford.
- Wantzel, P. L. (1837). Recherches sur les moyens de reconnaître si un problème de géométrie peut se résoudre avec la
  règle et le compas. *Journal de Mathématiques Pures et Appliquées* 2, 366–372.
- Wigner, E. (1939). On unitary representations of the inhomogeneous Lorentz group. *Annals of Mathematics* 40(1),
  149–204.
- Wilbraham, H. (1848). On a certain periodic function. *Cambridge and Dublin Mathematical Journal* 3, 198–201.

The entries were checked against Crossref and library catalogues on 3 November 2026; Malmquist (1926) is given as it is
usually cited, Lie (1880), added 10 November, as `plans/srb-plan.md` cites it, and Buffon (1777), Cauchy (1841) and Crofton (1868),
added 10 November: Crofton checked against the Royal Society's catalogue, Cauchy against a later reference list, and
Buffon to the volume only; Niven (1956), de Moivre (1733), Wallis (1656) and the IAU's resolution (2015) as they are usually cited.
