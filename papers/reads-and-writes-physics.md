# Reads and Writes in Physics

**Known physics, sorted by what a standpoint can read**

*Tom Brinkman. Draft, begun 8 November 2026. Written with AI assistance (Claude).*

*A draft. The abstract and §1 are written; §2–§12 follow the outline in `plans/phy-outline.md` and are filled in
section by section, each checked against its plan's runs. Its geometry is* Reads and Writes*'s
(`papers/readers-and-writers.md`), and where the two differ that paper stands. Its physics comes from the working
record, `papers/physics.md`, and from the plans and runs it names; a new physics result goes into the record first and
is carried out to this paper.*

## Abstract

Physics is written. Its laws are stated in amounts, a mass in kilograms, a distance in metres, a time in seconds, and
every amount needs a unit carried in from outside. But a great deal of what physics knows was read before it was
written: taken from one standpoint as directions, ratios and orders, with no amount in it, and only afterwards given a
size by something carried in. A *read* is taken from a standpoint, turning there, with one length H (a thumb held out at
arm's length); every reading is a direction [h : v], a ratio, and no amount survives into it. A *write* holds the
whole, the extents, the unit, the completed turn. This paper sorts known physics into the two.

Two tests do the sorting, and both are tests physics already uses. Scale the world, every length multiplied by one
factor: a reading is unchanged and a writing moves (the test of dimensional analysis, Bridgman's and Buckingham's).
Change what arrives, keeping the standpoint and the turn: the directions stay, and what changes is the *payload*, the
paint met along them. A law's form often comes from the first half and its values from the second, joined by a
*bridge*: the speed of light, a rest frequency, the astronomical unit, a kind of star, a clock.

Sorted this way, several familiar results come apart cleanly. A moving observer's sky is a Möbius map of directions
(aberration, a read) carrying a payload weighting (Doppler, read from what arrives, its frequency a write); the
rotation left by two boosts joined, Thomas and Wigner's, is read from three stars' directions alone and belongs to the
joining, never to one boost. A line's Lorentzian is the heat of a phase's turn, and its width and the decay time it
answers to are one quantity read two ways. The quasar dipole's expected size is 2β from directions plus a payload term
read from the catalogue, the payload carrying 60–70% of it. Interference's visibility is bounded by 2hv, the two paths'
shares, at most 1 at their corner. Each case is checked on published data or in exact arithmetic, with its prediction
written before its run, and the cases where the sort failed are kept.

Nothing here is new physics. Reading and writing describe the observer, not the world. What is offered is where each
part of a known result lives: which parts a standpoint has, which parts need an amount carried in, and what crosses
between.

## 1. Introduction

### 1.1 What this paper is

Reading and writing are a division of the observer's acts, worked out in *Reads and Writes* as geometry. A read is the
geometry of one standpoint: directions, the shares of one thumb, the corner where they are equal, the horizon never
reached, and the Cauchy, the heat the uniform turn lays over the readings before anything arrives. A write is the
recording of a read, a mark that lasts and can be counted, and it is where amounts live. That paper says it in one
line: a read is geometry, a write is physics.

This paper takes the line at its word and turns to physics. If physics is the writing, two questions follow. Which
parts of a known physical result could have been read, from a standpoint, before any amount was carried in? And for the
rest, what exactly was carried in, and where does it enter? The answers sort known physics; they add nothing to it.
That is the claim and its limit: physics is already a mix of reading and writing, often within one formula, and the
boundary between the two is not marked. The two tests mark it, quantity by quantity.

The point of marking it is practical. A quantity read as a direction and handled as an amount is misplaced, and a
known difficulty sometimes follows. Inverting a noisy parallax as if it were a distance gives Lutz and Kelker's bias;
averaging a Cauchy-distributed reading gives a mean that never settles, where its median does. Whether a misplaced
boundary is what causes other known difficulties is a question this paper raises and does not settle.

### 1.2 Two tests, as physics uses them

**Scale the world.** Multiply every length in a situation by one factor k, the observer's included, and keep every
standpoint where it stands relative to the rest. A quantity unchanged by k is a reading. A quantity that changes with k
is a writing, and somewhere an amount was carried in to give it its size. Physics has used this test for a century as
dimensional analysis: Bridgman (1922) and Buckingham (1914) sort quantities into dimensionless groups and the scale
that sets them. The groups are the reader's (with one base unit they are exactly the directions of a read; Buckingham's
π groups, checked in `plans/bpi-plan.md`); the scale is the writer's. The test is necessary for a reading and not
sufficient: a number unmoved by scaling can still have been made by writing, as π is made by closing the turn.

**Change what arrives.** Keep the standpoint and the turn, and change the world that paints the directions: another
source, another spectrum, another brightness, another medium. What stays is the read's own: the directions and their
heat. What changes is the payload. This test is the one that discriminates. A dipole that keeps its direction and size
whatever is counted belongs to the observer's motion; a dipole that changes with the slice counted belongs, in part, to
what arrives.

### 1.3 What crosses: the bridges

A reading crosses into an amount only by a bridge, something carried in that the read did not give. The bridges of the
cases in this paper are few and named each time:

- **a speed**, of light or sound, turning a direction's change into a time, or a delay into a range (a ranging reader
  is writing: it carries in the signal's speed and a clock);
- **a rest frequency**, turning a received frequency into a speed;
- **a baseline**, the step between two standpoints counted, turning crossed directions into places (parallax; for the
  stars, the astronomical unit, now fixed by agreement);
- **a kind**, a thing of known size or brightness, turning an angle or a flux into a distance (a standard candle or
  ruler);
- **a clock**, turning an order of reads into durations.

Each is a write. None is in the geometry, and none is found by reading harder.

### 1.4 Standings

Every result is marked by how it is known. **[exact]**: arithmetic checked to its last digit, often with many digits
to spare. **[data]**: published measurements, the source, licence and checksum recorded in the result's plan, the
prediction written before the data were opened. **[simulation]**: a simulation of our own, checked against a full
referee that computes the known physics directly. **[classical]**: a known result restated, not rerun. Results from
Wander's world, the flying page and its bodies, are illustrations and are not used here. A prediction that failed is
reported as failed, and a fix is a new prediction with its own run.

### 1.5 What follows

§2 gives the geometry in brief. §3 is the dictionary: quantity by quantity, read or written, and the bridge. Then the
cases: motion and time (§4), the moving sky and two boosts joined (§5), light and the inverse square (§6), distance and
parallax (§7), waves and the qubit (§8), two detectors read together (§9), and many bodies (§10). §11 reports where the
sort failed and what each failure taught. §12 says what the sort changes and what is open.
