# A tower of ratios: building without writing

27 Oct 2026. Tom: "When I think situated geometry, I think a tower of ratios, and as i move around, new ratios are added
and old ones are removed." Then: "yes, plan the test and lets build on other classical ideas. create a note that we can
iterate over. its not a new idea, but I don't think that it fully understood. for example, we would it be possible for
a reader to build with ratios only, and not care about writing."

A working note, to iterate on. A reading, not a ruling. Its test is TWR (`plans/twr-plan.md`). Citations below are from
memory unless marked read; each is to be checked before it goes anywhere else.

## 1. The picture

A situated reader holds two towers at once.

- **A tower in scale.** OFS's tower of holds: a building, its rooms, the things in them. Each link is a ratio read one
  level up (a thing in room units, a room in building units), not an amount. Any number of levels are held in ratios
  alone; writing the whole costs one amount, at the top.
- **A tower in time.** OFS's "Sweeping from zero": every stop is a new zero, readings compose by tangent addition, and a
  walk is a chain of legs, each read against the one before it (leg i over leg i − 1, from a thing seen at three stops).

Moving runs both. What it does to them is not the same:

- **The ground floor churns.** The addresses (directions from here, [h : v : v₂]) belong to this standpoint. Every step
  changes them all, and changes which things are held: some merge into home, some pass the held edge, some go behind a
  nearer thing, new ones come in. No act of the reader's; the geometry adds and removes them.
- **The upper floors stand.** The links (a size over a size, a distance over a distance) come out the same from any
  standpoint that sees what they relate. Once read they stay read, whether or not the reader ever stands there again.
- **Steps add floors.** Two standpoints turn address ratios into a place (parallax), so each step trades old addresses
  for a new link: a distance in legs. The first leg is the reader's H.
- **Loops check floors.** A misread link moves everything above it. A second route back to an old ratio shows the error
  (OFS's "Closing a loop"), and draw's cycle sheet (`cyc`) shows how: ratios on a graph with no common unit split into the
  part one ground explains and the obstruction round each cycle, from the readings alone.

## 2. Can a reader build with ratios only, and never write?

The claim to test: **yes, for everything it does alone.** A lone reader's whole map, its routes, its comparisons of size,
its way home and its time to contact are ratios in its own H (its first leg, its stride, its eye height). None of it
changes when the world is scaled, so none of it needs a unit. Writing is needed only where an amount comes from outside
the reader's own view:

- a quantity in another unit that no thing in view relates to (a speed in m/s, a clock's seconds, a stock of energy);
- another reader with whom it shares nothing in view (then the ratio of their H's is an agreement, a unit).

And one case that looks like writing and is not: **two readers that see one thing in common** align their maps by that
thing alone. The ratio of their H's is read off the shared link, with no amount passed (TGT already found the exact
form: closure between two readers' counted edges gives the ratio of their holds and nothing more). So "a unit between
readers is an agreement" holds only where they share no view.

If this holds, writing is not something a reader needs for its own geometry; it is how a reader meets the amounts of
others: other readers it cannot see, and instruments that state amounts.

## 3. Classical ideas to build on

Each with what it gives, what the tower adds, and its standing. "Check" marks a citation from memory.

1. **Eudoxus and Euclid, Book V: magnitudes in ratio, no unit.** Euclid's geometry of lengths, areas and volumes is
   built on ratios and proportions between magnitudes of one kind, with no unit length and no number attached to a
   segment; Book V (Eudoxus's theory) makes ratio rigorous without one. Classical geometry was, for two thousand years,
   built with ratios only. What the tower adds: the standpoint (Euclid's ratios belong to no one standing anywhere).
2. **Descartes, *La Géométrie* (1637): the unit segment.** To make the product of two lengths a length (not an area),
   Descartes chose one segment as unity; from then on lengths are numbers. The unit enters to do arithmetic on lengths
   as numbers, not to do geometry. A reading to examine: the unit is where geometry is turned into writing. (Kept
   neutral: OFS says nothing against the number line.)
3. **Thales and the pyramid's height, by its shadow.** The height read as the ratio of the shadows, against a staff:
   the oldest worked case of a tower link (the pyramid in staff units) with no unit at all. (Check: the story is
   Plutarch's and Diogenes Laërtius's; details vary.)
4. **Klein's Erlangen programme (1872): similarity geometry.** The geometry of the similarity group is exactly what is
   unchanged by scaling the world: OFS's test ("scale the world") is membership in it. Kendall's shape space (1984,
   check) is configurations modulo similarity, so a reader's map from ratios alone is a point of Kendall's space; draw's
   `owt` sorted which quantities survive similarity, affine and projective accounts.
5. **Bearing rigidity.** A framework of points is fixed up to translation and scale by the bearings between them when it
   is bearing-rigid (Eren et al. 2003; Zhao and Zelazo 2016, check). The tower's claim (a map from directions alone, one
   scale left) is this theorem; what is ours is the reading of that one scale as the one amount writing costs.
6. **Structure from motion and monocular SLAM: scale ambiguity and scale drift.** A single moving camera recovers the
   scene up to one scale; over a long walk the scale drifts as a random walk in its logarithm, and a loop closure corrects
   it as a similarity, not a rigid motion (Strasdat, Montiel and Davison 2010, check; Hartley and Zisserman 2003, the
   stratification projective, affine, metric). The tower in time is exactly this chain, and its drift is the chain's.
7. **Cycle consistency and synchronization; Hodge decomposition of ratios.** Pairwise ratios on a graph are consistent
   with one ground exactly when every cycle closes; least squares on log ratios projects onto the gradient part and the
   cycle part is the inconsistency (Jiang, Lim, Yao and Ye 2011, check; Singer 2011, check). Draw's `cyc` is this.
8. **Cognitive maps: topological before metric.** Tolman (1948) and Kuipers's spatial semantic hierarchy (2000, check):
   places and routes first, metric later and optional. A reading to examine: the topological and similarity levels are
   ratios; Kuipers's metric level is writing.
9. **Animals that navigate in their own units.** Bees' odometer reads optic flow, and bees flown down a narrow textured
   tunnel overstate distance (Srinivasan et al. 2000, check): a distance in the surroundings' units, a reading. Desert
   ants count strides, and ants on stilts overshoot (Wittlinger, Wehner and Wolf 2006, check): a distance in the ant's own
   H. Bees home by matching a snapshot of directions (Cartwright and Collett 1983, check): no distance at all. Each is a
   reader building with ratios only. (Perception is out of OFS's scope; this stays here.)

## 4. What seems not fully understood

- Which ratios a moving reader may **drop**. Candidate: any it can get back by closing a loop; a ratio is lost only if no
  route returns to it. (TWR T4.)
- How the **drift** of the tower in time is shared out by a loop: the Brownian bridge, error at the loop's middle half of
  the open chain's. (TWR T5.)
- Whether **two readers sharing a view** ever need writing between them. (TWR T6(f).)
- The two towers as **one structure**: the links in scale are the gradient part of a ratio graph whose nodes are things,
  the links in time the gradient part of one whose nodes are standpoints; a loop is a cycle of either. To be written out.
- Where exactly **writing** first becomes unavoidable, case by case: an outside amount, another reader out of view, or
  nothing else? (TWR T6(e).)

## 5. Log

- 27 Oct: note started; TWR planned (`plans/twr-plan.md`), predictions written, not run.
