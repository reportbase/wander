# Reads and Writes in Physics

**Known physics, sorted by what a standpoint can read**

*Tom Brinkman. Draft, begun 8 November 2026. Written with AI assistance (Claude).*

*A first full draft (8 November 2026), from the outline in `plans/phy-outline.md`. Its geometry is* Reads and Writes*'s
(`papers/readers-and-writers.md`), and where the two differ that paper stands. Since 10 November 2026 it follows that
paper as rewritten on SPN R788: what scaling leaves unmoved is a read if one standpoint holds it and a place if it needs
two, and only an amount in a unit carried in is a write. Its physics comes from the working
record, `papers/physics.md`, and from the plans and runs it names; a new physics result goes into the record first and
is carried out to this paper.*

## Abstract

Physics is written. Its laws are stated in amounts, a mass in kilograms, a distance in metres, a time in seconds, and
every amount needs a unit carried in from outside. But a great deal of what physics knows was read before it was
written: taken from one standpoint as directions, ratios and orders, with no amount in it, and only afterwards given a
size by something carried in. A *read* is taken from a standpoint, turning there, with one length H (a thumb held out at
arm's length); every reading is a direction [h : v], a ratio, and no amount survives into it. A *place* joins reads,
two standpoints or two moments, into a ratio of distances or durations, still with no unit in it. A *write* is an
amount, the place given a size by a unit carried in. This paper sorts known physics into the three.

Two tests do the sorting, and both are tests physics already uses. Scale the world, every length multiplied by one
factor: a read or a place is unchanged and a write moves (the test of dimensional analysis, Bridgman's and Buckingham's).
Change what arrives, keeping the standpoint and the turn: the directions stay, and what changes is the *payload*, the
paint met along them. A law's form often comes from the first half and its values from the second, joined by a
*bridge*: the speed of light, a rest frequency, the astronomical unit, a kind of star, a clock.

Sorted this way, several familiar results come apart cleanly. A moving observer's sky is a Möbius map of directions
(aberration, a read) carrying a payload weighting (Doppler, read from what arrives, its frequency a write); the
rotation left by two boosts joined, Thomas and Wigner's, is had from three stars' directions alone and belongs to the
joining, never to one boost: a place. A line's Lorentzian is the heat of a phase's turn, and its width and the decay time it
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
reached, and the Cauchy, the heat the uniform turn lays over the readings before anything arrives. A place joins reads
across a step, two standpoints or two moments, and gives distances and durations as ratios, with no unit. A write is an
amount: a place tied to a unit carried in. Reads and places are geometry; physics enters with the unit.

This paper takes the line at its word and turns to physics. If physics is the writing, two questions follow. Which
parts of a known physical result could have been read, from a standpoint, or placed, from several, before any amount
was carried in? And for the
rest, what exactly was carried in, and where does it enter? The answers sort known physics; they add nothing to it.
That is the claim and its limit: physics is already a mix of reading, placing and writing, often within one formula, and the
boundary between the two is not marked. The two tests mark it, quantity by quantity.

The point of marking it is practical. A quantity read as a direction and handled as an amount is misplaced, and a
known difficulty sometimes follows. Inverting a noisy parallax as if it were a distance gives Lutz and Kelker's bias;
averaging a Cauchy-distributed reading gives a mean that never settles, where its median does. Whether a misplaced
boundary is what causes other known difficulties is a question this paper raises and does not settle.

### 1.2 Two tests, as physics uses them

**Scale the world.** Multiply every length in a situation by one factor k, the observer's included, and keep every
standpoint where it stands relative to the rest; the units stay outside. A quantity unchanged by k is a read if one
standpoint holds it, a place if it joins standpoints or moments. A quantity that changes with k is a write, and
somewhere an amount was carried in to give it its size. (Until 10 November this paper, with *Reads and Writes*, called
every joining a write; R788 keeps "write" for what scaling moves.) Physics has used this test for a century as
dimensional analysis: Bridgman (1922) and Buckingham (1914) sort quantities into dimensionless groups and the scale
that sets them. The groups are reads or places (with one base unit they are exactly the directions of a read; Buckingham's
π groups, checked in `plans/bpi-plan.md`); the scale is the write. The test is necessary for a reading and not
sufficient: a number unmoved by scaling can still have been made by joining, as π is made by closing the turn.

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
- **a baseline**, the step between two standpoints, turning crossed directions into places in the step's length
  (parallax), and into amounts once the step is in a unit (for the stars, the astronomical unit, now fixed by agreement);
- **a kind**, a thing of known size or brightness, turning an angle or a flux into a distance (a standard candle or
  ruler);
- **a clock**, turning an order of reads into durations.

Each carries in an amount, and so makes a write; a baseline left in its own length makes only places. None is found by
reading harder.

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

## 2. The geometry, in brief

What follows is *Reads and Writes*'s, stated only as far as this paper needs it.

**The read.** A read is taken from one standpoint, *home*. The reader holds one length, H, a thumb held out at arm's
length, and nothing else to measure with. A reading is a direction met from home, [h : v], h and v each a share of the
thumb between 0 and 1, charted as the ratio v/h. Neither share can pass 1, so every relation turns over at one point,
v = h, the *corner*, the one reading the reciprocal x ↦ 1/x leaves where it is. At one end is *home*, v/h = 0; at the
other the *horizon*, [0 : 1], reached by no reading. V, the other party's breadth, never enters a read: every reading is
a ratio of the thumb's own shares.

**The heat.** Turned uniformly, the thumb's readings follow the Cauchy law: on the quarter turn the density in v/h is
(2/π)/(1 + (v/h)²), its median at the corner, its quartiles √2 − 1 and √2 + 1, and no mean, since the horizon carries a
tail no average can settle. With a second thumb crossed with the first, square to the look, the readings (v/h, v₂/h) on a
screen square to the look follow the two-dimensional Cauchy, 1/(2π(1 + r²)^(3/2)), which is cos³α per unit of screen,
α the angle off the look. The Cauchy is best read as a *heat*: a continuous weight over the directions, hottest along the
look, given whole before anything arrives.

**The paint.** What arrives along each direction is the *payload*, the paint met there: a colour, a flux, a spectrum, a
count. Changing it moves no direction and no heat. That is the second test of §1.2, and the reason reads never conflict:
a read adds nothing, and a change to the paint moves nothing a read holds.

**The standpoint z = m + iγ.** A reader at height γ above a line, over the point m, turning uniformly, lands on the line
as the Cauchy law of location m and scale γ, density (γ/π)·|1/(x − z)|², z = m + iγ. The whole law has one pole, at the
standpoint. One residue there gives its total (at t = 0) and its characteristic function e^(izt) (for t > 0), and below
the line the conjugate pole gives the rest: e^(imt − γ|t|), a phasor turning at the rate m and fading at the rate γ. Of the
kernels one meets in physics, only the Cauchy's response is a pure phasor: the Gaussian, sech, Laplace, Student's t₃
and a two-pole mixture each miss it, and a pole of higher order, several poles, endless poles or none each fail to give
it [exact, to 10⁻³¹].

**Relays and the exchange.** Two independent reads in sequence, the second taken from where the first landed, compose as
one read whose points add: z₁ + z₂. A real Möbius map of the chart (a turn, a change of thumb, the reciprocal) carries
the Cauchy family into itself and moves only its point. So sums of reads and reciprocals of reads stay reads.

**Joining reads.** A read holds no time, and two reads are joined only across a step that is counted: in space, the
baseline between two standpoints (parallax); in time, the ticks between two moments. Each such join is a place, unmoved
by scaling and held by no single read: an order, a rate in one's own ticks, a distance in the step, a duration in ticks.
It becomes a write only when the step or the tick is given in a unit carried in.

**Two geometries.** *Reader geometry* has no V: directions from one standpoint, shares of one thumb, the corner, the
horizon, the heat, order; joined, it gives places, still unitless. Scaling the world moves nothing in it. *Physical
geometry* has V in a unit: lengths and extents, the
box with a number line on each axis, the circle stated as x² + y² = r². Every figure in it has a size, and scaling the
world moves it. Physics is written in the second. The bridge between them is a share of the thumb times a breadth
carried in.

## 3. The dictionary

Each row pairs a piece of the reader's geometry with what it meets in physics, says which test sorts it, and names what
must be carried in to state it in amounts. "None" means one standpoint reads it.

| the reader's piece | in physics | sorted by | carried in |
|---|---|---|---|
| a reading over its own rate, x/ẋ, x = S/d | time to contact, d/u (Lee's τ) | unmoved by scaling; counted in the reader's own ticks | a clock, for seconds |
| ωτ, a bearing's rate times τ | how close a thing will pass, as a share of its distance | unmoved by scaling and by the clock | none |
| two shares of one circle in the unit E | E² = (pc)² + (mc²)²: β = pc/E, 1/γ = mc²/E | unmoved by scaling | c |
| a pair's geometric mean, fixed when the pair is multiplied by k and 1/k | rest mass, from E + pc and E − pc | unmoved by a boost | c |
| the logarithm of a direction's stereographic coordinate | pseudorapidity; a boost along the axis adds the rapidity | none | none |
| a Möbius map of directions | aberration | unmoved by what arrives | none |
| a weighting of the paint per direction | Doppler shift and beaming | moves with what arrives | a rest frequency, to state a speed |
| the turn left by joining two reads' maps | the Thomas–Wigner rotation | none: read from directions | none |
| the heat of a phase's uniform turn | a Lorentzian line; its width and the decay it answers to | read in frequency or in time | a frequency standard or a clock |
| the paint per direction constant; the count of directions a source covers | the radiance theorem; irradiance | scaling moves neither | the source's size, to state 1/d² |
| the uniform turn aimed outward, laid on a flat receiver | a point source on a plane, the cos³ law | none | the source's power |
| a census of directions with no cut on the paint | Ellis and Baldwin's 2 in the count dipole | unmoved by what arrives | none |
| the reciprocal of a sum of two reads | a triangulated depth | its law unmoved by scaling | the baseline |
| the central sweep's point: height 2hv, foot h² | the Bloch point; Born's weight; the visibility bound | none | Born's rule |
| the sum cut of two standpoints' readings, h + v = 1 | hard-ball contact | unmoved by scaling | none |
| a direction of two channels read at one instant | LIGO's [H1 : L1] | unmoved by averaging | none |
| dimensionless groups | Buckingham's π groups | unmoved by scaling | the base units |

## 4. Motion and time

### 4.1 Motion, from reads [exact]

A thing of half-size S at distance d closes at speed u. The reader reads x = S/d, the pair's v/h; it holds its own
clock, in ticks.

- **Time to contact is the reading over its rate**, x/ẋ = d/u, at every distance, before and past the corner, with none
  of S, d or u known (Lee 1976). Read from the angle arctan x instead, the same ratio gives d/u times
  arctan(x)(1 + x²)/x: right far off, too long by π/2 at the corner, and worse past it. So the exact carrier is the ratio.
- **A rate joins reads, so τ is a place**, in the reader's own ticks. Two looks a tick apart give it exactly:
  x₁/(x₂ − x₁) is the time to contact at the second look, x₂/(x₂ − x₁) one tick earlier. Seconds are carried in with a
  clock, a write. Scale-free too is τ̇, the rate at which τ itself changes: under steady braking τ̇ + 1 = d/(2s), s the
  stopping distance, so Lee's critical τ̇ = −½ is stopping distance equal to distance, the pair (s, d) at its corner.
- **How close it will pass.** With ω the bearing's rate, the closest approach as a share of the present distance is
  ωτ/√(1 + (ωτ)²). The clock enters ω and τ oppositely and leaves ωτ, so this needs nothing carried in; a bearing that
  holds still is a collision, as navigators know.
- **One stream is one relation.** A thing coming nearer and one growing at the matching rate give the same stream of
  readings. A neighbour at the same depth, read in the same moment, separates them.

The corners of motion come in two kinds. A quantity unchanged when its pair swaps, f(k) = f(1/k), is stationary at the
corner: a launch's range at a fixed speed, (2U²/g)·k/(1 + k²), longest at 45° with complementary launches equal; the
energy a head-on elastic collision passes to a ball at rest, 4k/(1 + k)², all of it at equal masses; a baseline's
conditioning, 2k/(1 + k²). A quantity whose sign flips when its pair swaps changes regime there: braking, above. All of
this is known kinematics. The sort settles which reading carries each result exactly, and what is carried in.

### 4.2 Special relativity as one circle [exact]

Divide E² = (pc)² + (mc²)² by E². It is the unit circle of the pair (pc, mc²), both read in the one unit E, with c the
bridge. Its two shares are v = pc/E = β and h = mc²/E = 1/γ, the moving clock's rate: a clock runs at the rest share of
its energy, and the reading v/h is the celerity γβ.

- **Home** (v = 0) is E = mc²; the **horizon** (h = 0) is E = pc, light, reached by nothing with mass. The **corner** is
  pc = mc²: β = 1/√2, E = √2·mc², kinetic energy (√2 − 1)·mc², 0.2117 MeV for an electron and 388.6 MeV for a proton.
- **Newton's form and the massless form are each other's reciprocal.** mc² + p²/2m and pc + (mc²)²/2pc swap when pc and
  mc² swap, and their relative errors satisfy e_N(x) = e_U(1/x) exactly. Newton's is the better approximation exactly
  inside the corner; at the corner both are √(9/8) − 1 = 6.07% high. This is the precise form of "where relativity
  starts to matter".
- **Mass is the geometric mean of the light-cone pair.** (E + pc)(E − pc) = (mc²)². A boost with Doppler factor k sends
  E + pc to (E + pc)/k and E − pc to k(E − pc); the geometric mean does not move, which is why mass is the same for every
  observer, and boosts compose by multiplying k, which is why rapidities add. Mass is the least value of E over boosts.
- **γ and γβ are the two parts of k under its reciprocal:** γ = (k + 1/k)/2 is unchanged by k ↦ 1/k and γβ = (k − 1/k)/2
  reverses, so k = γ + γβ and 1/γ = 2k/(1 + k²), the form of a launch's range. Rapidity is asinh of the celerity:
  proportional near rest, logarithmic far out, never more than 1 − ln 2 nats from the reader's own lay of the celerity.
  Under uniform acceleration a the Doppler factor grows as e^(aτ) in proper time.

All of it is standard (Bondi's k-calculus, light-cone coordinates, the two limits). What the sort adds is organisation:
one circle in one unit, home and horizon, the two limits one approximation under the reciprocal, the invariant mass a
geometric mean. What it does not give: c's value, or why a change of frame is a hyperbolic turn rather than a circular
one. That sign is the world's.

### 4.3 Time and the standpoint's phasor [exact, data]

The characteristic function of the Cauchy from z = m + iγ is e^(imt − γ|t|): a phasor turning at m and fading at γ. Read
the other way round, a phase turning at a steady rate and fading, as a two-level atom's dipole does after it is excited,
has as its spectrum the Cauchy law in frequency, the Lorentzian, its centre the turning rate and its half-width the
fading rate. So the Lorentzian is the heat of the phase's turn, and the line's width Γ and the decay time τ are one
quantity, the height of one standpoint, read two ways: in frequency, by sweeping a probe across the line, and in time, by
watching the excited state empty. Their product is 1 (Weisskopf and Wigner 1930). Checked [exact]: the transform of the
Cauchy is the phasor to 10⁻⁴⁶, the damped phasor's power spectrum the Lorentzian to 10⁻⁶⁰.

On one transition the two reads were made independently. For the sodium D2 line, Oates, Vogel and Hall (1996) measured
the natural width by spectroscopy on cold atoms, Γ/2π = 9.802 MHz, equivalent to 16.237(35) ns; Volz and colleagues
(1996) measured the decay in flight, 16.254(22) ns. Then Γτ = 1.0010 ± 0.0025 [data]. The line's shape is the turn's; its
width and the lifetime are amounts, each needing its own standard, a frequency or a clock. Neither is read from a
standpoint; that they agree is the one standpoint seen twice.

The same was then tested on four more transitions, with the prediction fixed before the search [data]. Each pair is a
width measured in frequency or energy against a lifetime measured in time, and the lifetimes run from 10⁻¹⁷ s to 10⁻⁸ s:
- **The neutral pion.** Its two-photon width from the Primakoff effect (Larin et al. 2020), over its branching ratio,
  against its decay length (Atherton et al. 1985): Γτ = 1.076 ± 0.037.
- **Cadmium's ¹P₁ level.** Its line shape (Hofsäss et al. 2023) against beam-foil (Andersen and Sørensen 1973):
  1.19 ± 0.10.
- **Krypton's 3d core hole.** Its width, 88 ± 4 meV, against an attosecond pump–probe measurement (Drescher et al.
  2002): 1.06 ± 0.14.
- **Dysprosium's 421 nm level.** Its line shape (Lu, Youn and Lev 2011) against time-resolved fluorescence (Curry,
  Den Hartog and Lawler 1997): 0.964 ± 0.055.

With sodium, χ² is 8.43 on five degrees of freedom (p = 0.13). The pion's 2σ is a tension known in the particle data. The
width and the lifetime agree across nine orders of magnitude of time, and only the standard each needs differs.

The clock itself is hidden in the same way [exact]. A Brownian walker from height h lands on a line as the Cauchy of
scale h whatever its diffusion constant D; speed the walk up a hundredfold and every passage time shrinks a hundredfold
while not one landing moves, and the passage times have no mean to settle on (the median of a batch's mean grows in
proportion to the batch). Order and ratios are free; durations are amounts, and the only constant joining place to time
is a speed.

## 5. The moving sky

### 5.1 Aberration and Doppler [exact]

A moving observer's sky is the clearest place in physics where a read and a write sit inside one formula.

- **Aberration is a map of directions.** In the stereographic chart about the line of motion it is z ↦ z/k, k the
  Doppler factor: a Möbius map of the celestial sphere (Penrose 1959; Terrell 1959). Directions go to directions, angles
  between nearby stars are kept, and nothing arriving is consulted.
- **A uniform sky, seen moving, is the spherical Cauchy**, density D²/4π with D the Doppler factor of each direction
  (Kato and McCullagh 2020): the Möbius family carries the uniform law within itself. No law on the sky is
  boost-invariant; boosts carry the uniform one within its family. On the logarithm of the stereographic coordinate,
  −ln tan(θ/2) (the pseudorapidity), a uniform sky lies as ½·sech² and a boost slides it by the rapidity η. So the
  rapidity is had from directions alone: from one look, with the sources taken as uniform in their own frame, the slide
  of one read's median (a read); against a look before the boost, the two medians joined (a place). No clock, no
  frequency, no c.
- **Doppler shift and beaming weight the paint**, moving no direction. Of the D⁴ by which an isotropic sky brightens
  ahead, D² is the crowding of directions and D² the paint. To state the shift as a speed needs a rest frequency, a write.
- **Two more readings of one sky.** A thermal sky, each direction a blackbody at T₀·D: the hottest over the coldest is
  exactly (1 + β)/(1 − β) = k² at every speed, a ratio; a linear dipole fit reads β = 0.6 as 0.67 (Peebles and Wilkinson
  1968). Radar: two echo times give the Doppler factor as their ratio, t₂/t₁ = k², and the interval as their product,
  t₁t₂ = τ² (Bondi 1964). A common rescale of both stamps leaves the ratio and moves the product: one pair of stamps, a
  place and a write.

### 5.2 The quasar dipole [data]

The boost is read from directions alone only for a census taken whatever the brightness, and every real census is cut at
a flux. With no cut a moving reader's census is D²/4π, and its dipole is 2β plus terms in β³: Ellis and Baldwin's 2
(1984) is the directions'. Cut at a flux limit, it is D^(2 + x(1 + α)), with x the counts' slope at the limit and α the
sources' spectral index, both read from the same catalogue: still ratios, with no rest frequency and no distance in them,
but no longer directions alone. The payload has entered.

On Secrest et al.'s CatWISE quasars (2021) the sort sets the number. Per slice the expected dipole is [2 + x(1 + α)]·β,
5.3 to 6.6 times β, so the paint carries 60–70% of it. Taken as directions alone, the measured 0.018–0.023 would give a
speed nearly three times too large. With the payload's part divided out, four slices by brightness give one β,
(3.31 ± 0.27) × 10⁻³, 2.7 times the speed read from the microwave background, as one motion of the reader should: the
first test passed in a form that could have failed. Slices by colour give 2.3, 2.8 and 4.6 times it, which no motion of
the reader can do (p = 2.6 × 10⁻⁴), and the direction lies 21–28° from the background's. So part of the dipole belongs
to what arrives, or to a selection that depends on colour: the second test failed, and says where. The sort does not
settle where the dipole comes from. It says which part could be the reader's.

### 5.3 Two boosts joined [exact]

Collinear boosts add their rapidities. Read on the sky the reason is plain: a boost along one axis is, in the
stereographic chart centred on that axis, a multiplication z ↦ k·z, a slide of ln z by the rapidity, and slides along one
line add. A Möbius map fitted to three stars' apparent directions before and after a boost along n by ζ has trace
2·cosh(ζ/2): the rapidity is read from three directions, with no frequency and no distance. Two boosts along n read
ζ₁ + ζ₂, and tanh of it is (β₁ + β₂)/(1 + β₁β₂), the velocity law, which is the writer's tanh of the reader's sum.

Boosts along two axes cannot be one slide. Joined, they leave a turn, the Thomas–Wigner rotation (Thomas 1926; Wigner
1939). Its angle Ω satisfies tan(Ω/2) = ab·sin φ/(1 + ab·cos φ), a = tanh(ζ₁/2), b = tanh(ζ₂/2), φ the angle between the
boosts, and it equals the area of the velocity triangle in hyperbolic space. The test here was whether this rotation is
a reading in the paper's sense, and it is:

- **From directions alone.** Twelve pairs of boosts (φ from 30° to 135°, rapidities 0.2 to 3), each applied to seeded
  stars as photon four-momenta; the reader given only three stars' directions before and after, on the stereographic
  chart. The fitted Möbius map predicts every other star's direction to 10⁻⁵⁸, and its polar decomposition's rotation
  equals the half-rapidity formula to 10⁻⁵⁹, the triangle's area to 10⁻⁵⁸.
- **The same from any stars.** Five different seeded triples agree to 4 × 10⁻⁵⁸.
- **Absent from any single read.** One boost's fitted map has no rotation (below 2 × 10⁻⁵⁹ for nine boosts of three sizes
  and directions), nor has a collinear pair. The rotation belongs to the joining, a place.
- **The small loop.** A loop of boosts by ε along n₁, n₂, back and back leaves a rotation of ε²·sin φ to leading order;
  so does the same loop of turns, about the opposite axis: the same leftover of joining, with curvature −1 against +1.
  At the next order they part. The turn loop's leftover is exactly 4·arcsin(sin²(ε/2)·|sin φ|), so ε²·sin φ·(1 − ε²/12),
  the correction the same at every angle; the boost loop's is ε²·sin φ·(1 + (1/3 + cos φ/4)·ε²), the correction
  depending on the angle. Both were predicted before the run and held to 10⁻⁹ at fresh angles.

What this does not do is derive the Lorentz group from reading and writing. The group enters through one premise: that a
change of standpoint by motion is conformal on the sky, keeping the angles between nearby stars. By Liouville (1850)
every conformal map of the sphere is Möbius, and the Möbius group of the sphere is the Lorentz group (Penrose and Rindler
1984). Given that premise, the rest is classical. That is where the correspondence ends, and it is said here so that it
is not mistaken for more.

### 5.4 Loops that come home turned [exact]

§5.3's leftover is one case of a wider fact. A read is one standpoint at one moment; reads joined end to end round a loop
are a place, and what the joining leaves over when the loop closes depends on where it happens.

- **In the plane, nothing.** Turns of the plane commute, so carrying a direction round any closed loop brings it home
  unturned. Fifty loops laid flat turned by 0, which was guaranteed: flat transport does not change a direction at all.
- **On the sphere of directions, the area.** Turns of space do not commute, and a direction carried round a closed loop
  on the sphere (parallel transport, each step as straight as the sphere allows) comes home turned by the solid angle the
  loop encloses (Gauss 1828; the Gauss–Bonnet theorem). The transport was integrated as a differential equation at 50
  digits, and the area worked out separately (by the triangle formula of Van Oosterom and Strackee 1983): twelve circles
  of latitude agreed to 3 × 10⁻⁵⁰, two hundred random geodesic triangles and quadrilaterals to 10⁻⁴⁹. Essay 13's quarter
  turns about h, then v, then back about each, coming home turned 90°, are the octant's loop: its area is π/2.
- **In velocity space, minus the area.** Boosts joined round a closed loop of velocities leave the Wigner rotation, and it
  equals minus the loop's hyperbolic area (rapidity space has curvature −1 where the sphere has +1). For two hundred
  loops with rapidities from 0.01 to 3 the two agreed to 1.5 × 10⁻⁴⁷, sign included. §5.3's small-loop coefficients are
  this at the leading order; it holds for large loops too.
- **No amount enters.** The turn is a direction. On spheres of radius 10⁻³, 7 and 10⁶ it is the same (to 10⁻⁴⁹): the
  radius cancels against the lengths of the loop, as the scale test asks of a reading. A loop out and back along one line
  encloses nothing and turns nothing (5 × 10⁻⁵¹ on the sphere, 2.5 × 10⁻⁴⁹ in velocity space).

So the leftover of joining is a place: the area the joined reads enclose, with no unit and no clock. A rate
of turning is another matter. Foucault's pendulum (1851) turns, against the ground, by 360°·sin φ a sidereal day at
latitude φ: the area the latitude's circle leaves out of the hemisphere, read per turn of the Earth. The degree a day
carries the sidereal day in, a clock, so it is a write. Measured rates were sought before any was read; one site met the
rules fixed beforehand (a pendulum free of the ellipse's precession, decided from its text): Schumacher and Tarbet (2009)
at Pittsburgh, −9.69 ± 0.09° an hour, which is 357.6 ± 3.3° a sidereal day over sin φ, 0.74 standard errors from 360°.
One site is too few to count; the test asked for three. Berry's phase in a coiled fibre (§8.4; Tomita and Chiao 1986),
the same leftover on the sphere of a light ray's directions, could not be reached as numbers. A qubit's could (Leek et
al. 2007): a superconducting two-level system whose field direction is taken round cones, the phase left after a spin
echo read against the cone's solid angle. Read from the paper's figure, 192 points over cones from 0.3 to 2.6 sr, both
directions and one or one and a half loops, follow twice the solid angle (the echo's two loops) with slope 1.013 ± 0.003;
the loop that undoes itself leaves no turn but an offset of 0.2 rad. The strength of the field and the length of the
sequence enter nowhere in the comparison.

In a spectrum the leftover shows as Thomas's half (Thomas 1926). An electron's frame, carried round its orbit, comes home
turned, and that precession halves the spin–orbit splitting a magnet alone would give. Hydrogen's 2P₃/₂–2P₁/₂ interval is
10,949.6 MHz on Dirac's value, which contains the half. The measured interval is 10,969.045 ± 0.015 MHz: the 2S₁/₂–2P₃/₂
interval, 9,911.200(12) MHz (Hagley and Pipkin 1994), plus the Lamb shift, 1,057.845(9) MHz (Lundeen and Pipkin 1981),
each read from its paper's abstract. Measured over
Dirac is 1.0018, the rest QED; measured over the interval without the half is 0.501. This is reported, not counted.

None of it is new physics: Gauss, Thomas, Wigner, Foucault and Berry hold every piece. What the sorting adds is where each
piece falls. The turn comes from the loop alone; the loop is joined, a place; a rate of turning in degrees a day needs a
clock, a write.

## 6. Light

### 6.1 The inverse square, as heat and paint [exact]

Physics derives the inverse square from conservation and three dimensions and tests its exponent to extraordinary
precision; it is not this paper's to test. What the sort says is where it lives.

- **The paint per direction does not carry the law.** Along each direction a source covers, the brightness is the same
  at every distance (the radiance theorem). Distance changes how many directions the source covers, never the paint on
  each.
- **The law is in the count of directions.** Irradiance is the paint times the solid angle the source covers, about
  π(Δ/d)² far off, a reading of the pair (size, distance).
- **An even emitter on a flat receiver is the Cauchy, and the law is its height.** A source sending alike in every
  direction is the uniform turn aimed outward. Laid on a flat receiver at distance d, its power per unit area is P/2 times
  the (D − 1)-dimensional Cauchy of scale d, and on the axis that is the inverse (D − 1)-th power: 1/d² in three
  dimensions. The receiver catches exactly half. This is the cos³ law of illumination, by a change of variable. A lens
  adds one cosine more, cos⁴, for the aperture seen obliquely: three cosines are the heat, the fourth the lens's.
- **The corner lives in the count.** An even line of half-length b at distance d gives (λ/4πd)·2·arctan(b/d): paint
  falling as 1/d on every direction it covers, and the share of directions (2/π)·arctan(b/d), whose median is exactly at
  b = d. Its slope on logarithmic axes at b = d is −1.637: −1 from the paint and −2/π from the directions.
- **The dimension.** The cosine-weighted share sin^(D−1)θ is symmetric under the reciprocal only in three dimensions:
  D = 3 is singled out by Lambert's cosine, not by the turn, whose one-axis marginal is the Cauchy in every dimension.
- **1/d² needs distance; counts by flux are a read.** Scale every length by k with the paint fixed, and every solid angle,
  irradiance and flux is unchanged. So 1/d² compares standpoints with the source's size held fixed, and needs d as an
  ratio at least, a place, from a baseline walked or a kind carried in (a standard candle), and as an amount a write. The count of sources brighter than a flux needs no
  distance at all: for any population spread evenly, N(> S) falls as S^(−3/2) at every S, unmoved by scaling.

All checked to 10⁻⁵⁰ in exact arithmetic; one prediction (the cosine-weighted per-axis median) was killed by my
arithmetic, recorded as such.

### 6.2 The near field turns at the corner [exact]

A Lambertian disc of radius a, seen on its axis at distance d, has a light whose logarithmic slope is −2s²/(1 + s²),
s = d/a: halfway between the near field's flat light and the far field's inverse square exactly at s = 1, and symmetric
about it, σ(s) + σ(1/s) = −2. A sphere counted from its surface does the same. Counted instead as an angle, or as an
unprojected solid angle, the switch moves off s = 1 and is not symmetric. The corner holds where the light counted is a
share of the directions.

### 6.3 Light and number on the stars [data]

- **Light falls as the inverse square of distance, for one kind.** On the Hipparcos stars (ESA 1997), with distance
  from parallax and kind from the spectrum, G0–G5 dwarfs within 23 pc fall in light as d^(−2.02) (83 stars), and K0
  giants where the catalogue is complete as d^(−1.93) (533). A kind is a bridge with a spread: about one in ten stars
  labelled K0 III is something fainter.
- **Number grows as the cube of distance, within 100 pc.** On the Gaia Catalogue of Nearby Stars (Gaia Collaboration,
  Smart et al. 2021), main-sequence stars by colour, counted within d, grow as d^2.93 to d^3.00 for each colour class,
  plane and poles alike, once no quality cut that depends on distance is used.
- **Counts by light are a read.** Hipparcos's stars brighter than V 7.3 grow in number as S^(−1.23) in flux, alike in
  the plane (1.229) and toward the poles (1.227), not the even spread's S^(−1.5). No distance enters a count by light;
  the 1.2 reads the world's shape, between a sphere's 1.5 and a slab's 1.0. Most of those stars lie past 100 pc in a
  thin layer of luminous kinds seen through dust; which of the layer and the dust does how much is open.

The distance-based results are places, through parallax and a kind, and writes once the parsec is in metres; the counts
by light are reads.

## 7. Distance

### 7.1 Parallax is a sum of reads [exact]

Two standpoints a step B apart each read a point: cot a from one end and cot b from the other. Then cot a + cot b is B
over the point's distance from the step's line, and the depth is the reciprocal of a sum of two reads. Those are the two
operations the Cauchy family is closed under (§2), so parallax never takes a read out of the family. If each read is
uncertain as a read from a height γ is, and the two are independent, each is a Cauchy point w = (c + iγ)/(1 − iγc), c
its true value, and the depth is exactly a Cauchy whose point is the triangulation done on the reads' points:
D = B/conj(w_a + w_b). That holds at every γ, not only for small errors: rays that do not meet ahead are part of the same
law, as negative depths. At the pair's corner, the circle on the step, the depth's point stays at the true distance,
turned by twice the read's error angle. Checked at three γ and seven targets to the sampling error; to first order the
depth's relative error is the Cauchy of scale 2γ·cosh(ln k), k = d/(B/2), least at the corner.

Two things leave the family, each visibly. The place across the line of sight is a ratio of two sums, and its density
over each standpoint is infinite; two standpoints each turning only a quarter turn give a depth whose tail falls as
1/d³, with a mean. And two standpoints' scales add, so a second standpoint never averages a read's spread down: more
standpoints improve the figure, never the scale.

### 7.2 The error's shape, and what parallax already knows [exact]

The pair is (B/2, d); its corner is the Thales circle on the baseline, where the parallax angle γ is 90°. The relative
distance error per unit angle is cosh(ln k), least at the corner and the same at k and 1/k, and sin γ = sech(ln k), the
height of the central sweep's point. With angles read to a step ε, the relative error stays under one over a band
reaching a factor of about 1/ε to either side of the corner; its far edge is about B/ε. Past it a point is a ray: parallax
needs a standpoint's read and returns to one.

Working back from practice: d = a/tan p, with the astronomical unit a measured outside the parallaxes and now fixed by
agreement: the parallax p is a read, d in astronomical units a place, d in metres a write. σ_d/d = σ_p/p is the far limit of the exact ratio γ/sin γ. Not inverting noisy parallaxes (Bailer-Jones 2015)
is the reciprocal's missing mean with the median kept: a parallax with a Gaussian error has an inverse with no mean, and
at the band's edge 16% of the readings are at or below zero. Inverting them as if they were distances is Lutz and
Kelker's bias (1973): a read taken for a place. Of the misplaced boundaries in this paper, it is the one shown to cause a
known difficulty.

### 7.3 The distance ladder as a tower [data, simulation]

A ladder's rungs are reads joined into places, with writes at the anchors: the angles and the flux ratios of one kind are
reads; the ratios between rungs, places; the astronomical unit, the anchors, every megaparsec and H₀, writes. A rung's error is one factor only if it is
flat against an independent distance. On Cosmicflows-4 (Tully et al. 2023), Hubble's rungs (Hubble 1929) are not
(slopes 0.79 and 0.16 against 1): his brightest-star rung was a stretch, a ruler of another kind, not a factor. An
apparent drift between the fundamental plane and type Ia supernovae belongs to the 58 galaxies the two share, not to the
rungs; away from that overlap neither drifts by more than 0.016 mag per mag. A network of loops whose routes cross
different objects locates a misread link; a single comparison cannot.

In a simulation of our own, a figure of 20 landmarks read by 16 to 4,096 standpoints with one outside length carried in
at 1% error: the shape improved as N^(−0.49), the scale never moved from the outside length's 1%, and by 4,096
standpoints the landmarks' errors were 99% correlated, one shift shared by all. Statistical error, which more reads
average down, against a calibration's error, which they do not: in the sort's terms, the reads and places against the
one write.

## 8. Waves and the qubit

### 8.1 The qubit is the two sweeps [exact, classical]

A qubit's state is a ray with real amplitudes h and v, a direction at θ: the inscribed read. Its Bloch point is at 2θ,
(2hv, 0, h² − v²): the central sweep's point, at twice the angle (Euclid III.20). Born's rule is the point's foot, h².
Orthogonal states are antipodal on the sphere; a turn of the state by 2π gives −ψ, so 720° returns it; the complex ratio
ψ₁/ψ₀ is the Bloch sphere's stereographic chart; a pure state lies on the sphere and a mixture inside. All textbook; the
reading is the sort's. Entanglement, Bell's theorem and measurement are not touched.

### 8.2 The duality relation [exact, data]

On the unit circle sin 2θ = 2hv and cos 2θ = h² − v². With h and v two paths' amplitudes, the fringe visibility is at
most 2hv and the which-path predictability is |h² − v²|, so V² + P² ≤ 1, with equality for a pure state (Greenberger and
Yasin 1988; Englert 1996). Full visibility comes only at the corner, and 2hv is sech of the logarithm of the amplitudes'
ratio, already in print as V = sech θ, P = tanh θ (Bramon, Garbarino and Hiesmayr 2004). The bridge is Born's rule: an
amplitude is the square root of a share of the counts.

- **Single photons.** On Aspden, Padgett and Spalding's frames (2016), a double slit lit one heralded photon at a time,
  the two slits' counts 9,026 : 10,465 and 11,993 : 11,891 give 2hv = 2√(n₁n₂)/(n₁ + n₂) = 0.997 and 1.000, the pair at
  its corner; the measured contrast, 0.69 and 0.56, lies below that bound, short by the source's coherence. The bound is
  the shares', the geometry's; how far below it a pattern falls is what arrives.
- **Neutrons.** Summhammer, Rauch and Tuppinger (1987), one path attenuated to transmission a, read from their figure:
  foils (each neutron passes with probability a, a pure pair with amplitudes 1 and √a) keep √a of the fringe amplitude,
  six points from a = 0.05 to 0.47 within 1.3σ; a chopper open a share a of the time (a mixture) keeps a, three points
  within 0.6σ. At a ≈ 0.24 the foil keeps 0.447 and the chopper 0.243. On the duality circle the foil is on it and the
  chopper inside. The thinnest gadolinium foils fall below √a, which the paper ascribes to uneven thickness.

### 8.3 Weak values and a missing frame [exact]

A state pre-selected at θ_i and post-selected at θ_f has the weak value of σz equal to ⟨σz⟩ − V·tan(θ_f − θ_i), with
⟨σz⟩ = h² − v² and V = 2hv (Aharonov, Albert and Vaidman 1988). Under a uniform turn of the post-selection it follows
the Cauchy at ⟨σz⟩ + iV: a read laid by the turn, its point the state's central point. A party without a shared phase
reference averages over what it cannot fix (Bartlett, Rudolph and Spekkens 2007): the twirl, an operation on the
payload. It lowers the ensemble's visibility and changes no member's overlap: amounts are lost, readings kept. Two
copies twirled together keep only their overlap, (1 + n₁·n₂)/2.

### 8.4 Berry's phase [classical]

A spin carried slowly round a closed loop of field directions comes back with two phases (Berry 1984). The geometric one
is half the solid angle the loop of directions encloses: it depends on which directions were visited and nothing else,
the same taken twice as slowly, in a field twice as strong, or in an apparatus twice the size. The dynamical one is
energy times time and moves with all three. Experiments have separated them by keeping the loop and changing the rest:
photons in a coiled fibre (Tomita and Chiao 1986) and neutrons in a turning field (Bitter and Dubbers 1987). Both tests
sort it: scaling, and changing what is carried, each move only the dynamical phase. The half is the central sweep's
twice the angle: the state at θ has its point at 2θ, so a loop counted on the sphere of states is counted twice.

## 9. Two detectors, one direction [data]

Open data from the two LIGO detectors (Abbott et al. 2023) give, in each detector, about two million whitened samples
over 512 s. Read with the sort, the predictions were written before the data were fetched.

- **Each channel is an amount.** Its heavy tail at a single sample is a finite-spread law (a Student t with ν = 15.9)
  with one loud transient, and the interquartile range of block means falls as n^(−½) through the whitened band, which
  nothing Cauchy can do. The old preference for a Cauchy over a Gaussian at one sample (by more than a million in
  log-likelihood) reproduces, and is the transient's.
- **The direction of the two is a read.** The ratio L1/H1 taken sample by sample, each channel drawn at its own spread,
  is a Cauchy at its corner: on two segments not seen when the predictions were written, the median |L1/H1| is 1.0010
  and 0.9996, the quartiles within 0.004 of ∓1. Its spread does not shrink under averaging (slope −0.002 and −0.008
  against 0).
- **The prediction that could have failed.** The angle atan2(L1, H1) is not quite uniform (0.0076 and 0.0061 in
  Kolmogorov distance, against a sampling scale of 0.00094). Pairing each H1 sample with the L1 sample 8 s away keeps
  each channel's own law and destroys their joint timing; it reproduces that departure to 0.0001. So the direction's law,
  its corner and its departure from the uniform turn are the two channels' own laws, measured separately. A disturbance
  shared at one instant would have broken this; none did.

A classical analysis would not predict otherwise. What the sort adds is where the Cauchy is (the direction, not either
amount) and why averaging helps one and not the other.

## 10. Many bodies [simulation]

Each simulation here is checked against a referee that computes the known physics directly.

- **Contact read from inside.** Each ball reads another as v = r_b/d and is told the other's reading h = r_a/d: radii
  over the distance between centres, one unit, so shares with no bridge. Contact is h + v = 1, the sum cut of two
  standpoints' reads; equal balls touch at the corner. A cushion is a ball meeting its own mirror image, always at the
  corner. Played from inside, each ball in its own size, a game of pool equals the referee's to rounding, and scaling the
  world moves no reading and no contact.
- **Cooling counted in contacts.** Five hundred smooth inelastic spheres, contact found where h + v = 1. Per contact per
  sphere the temperature falls by (1 − e²)/3 of itself to 0.8% wherever the gas stays even (Haff 1983). Density,
  diameter and pair correlation leave the count; the clock needs them all, and near the clustering instability goes
  wrong about twice as far as the count does. The count is a place (contacts joined, no unit), the clock a write.
- **Holding a world by distance.** A hard-disc gas held as a window of discs round the reader and, beyond it, totals in
  cells growing with distance, against a referee computing every disc (Enskog's contact rate to 0.1%, Henderson's
  equation of state, Henderson 1975): the view's density, warmth and contacts within 0.3%, for the work of the window,
  for a world 256 times larger. It needed what open systems need, the outside's pressure, a reservoir at fixed chemical
  potential and books kept where pushes balance; and it lost a pulse travelling toward the reader. Folding the paint
  into cells by distance is an irreversible mean: what travels toward a reader must be held at its own size until it
  arrives.
- **Ranging is writing.** A lumpy moon crossing a reader's view: with a range on each direction (the signal's round trip
  times its speed, an amount carried in) the face is recovered to 4%, and distance and speed to 0.25%. With directions
  alone the outline is free, the visual hull (Laurentini 1994), tight where an edge touched the moon, keeping none of the
  face elsewhere, and unmoved when the world is scaled.

## 11. Where the sort failed

Predictions are written before the runs, so some fail. The ones that teach most:

- **Seeds falling.** The test that could fail. Seeds falling from a plant spread with a fat tail, and the turn can be
  named beforehand: a seed leaving its release point straight, every downward direction alike, lands as the hemisphere's
  Cauchy, Clark's 2Dt with shape p = ½ and a tail falling as r⁻³ (Clark et al. 1999). On Bullock et al.'s compiled
  kernels (2017), the 35 that could be fitted of 38 picked as wind-dispersed from their labels alone say otherwise:
  median p 0.10, a tail falling about as r⁻², shapes spread widely, and no nearer the turn's than kernels carried by
  animals. The fat tail there is a mixture over wind speeds, as the literature reads it: amounts, not a turn. So a
  Cauchy-like law is a turn's heat only where the turn can be named apart from the law's shape, and a fat tail alone is
  no evidence of one.
- **The quasar dipole's colours** (§5.2). The colour slices disagree and the direction is 21–28° off: part of the dipole
  is not the reader's motion. One estimator of mine missed the published amplitude by 22%.
- **Star counts.** The disc was predicted to flatten counts toward the poles more than in the plane; both give 1.23. On
  Gaia within 100 pc all four predictions failed: a quality cut on the astrometry removes more near stars than far ones
  and steepened the counts, and a fifth of the G and K colours within 50 pc are white dwarfs. Colour alone is not a kind,
  and a kind is the bridge.
- **The ladder** (§7.3). Hubble's rungs are not one factor each.
- **Relief on real worlds.** On seven published shape models, relief per octave of spherical-harmonic degree was
  predicted to follow one power law, falling by half each octave, on every body. Earth, Mars and Venus hold near power
  laws (slopes −0.34 to −0.44); the airless bodies bend, their relief highest at a tenth to a fortieth of the radius. How
  relief is shared across scales is the world's, and no reading predicts it.
- **The near field, counted otherwise** (§6.2): an angle or an unprojected solid angle switches off s = 1, not
  symmetrically.
- **Constructions carry systematics.** Least squares on bearing lines left a floor on the shape error that more reads did
  not remove (errors in the variables); maximum likelihood removed it.

Other kills were mine: a tolerance under the sampling error, a derivation with a slip, a test that left out a term. Each
stays recorded beside the run that replaced it.

## 12. What this changes, and what is open

### 12.1 What the sort changes

It changes no physics. It sorts, and the sort gives four working rules.

- **A ratio unmoved by scaling is a read if one standpoint holds it, a place if it joins several; anything that moves
  is a write, and something was carried in.** Name the
  bridge each time: a speed, a rest frequency, a baseline, a kind, a clock.
- **Read the median where a turn is named; average only amounts.** A Cauchy-type quantity is a direction where a turn
  that lays it can be named apart from the law's shape. There the median and quartiles are its statistics, and averaging
  gains nothing (LIGO's direction; the inverted parallax). A fat tail alone is no evidence of a turn.
- **Separate what the observer brings from what arrives.** The second test splits a formula into the directions' part
  and the paint's (aberration from Doppler; the dipole's 2 from x(1 + α); Berry's geometric phase from the dynamical).
  The directions' part must be the same whatever is counted; where it is not, part of the effect belongs to what arrives.
- **Joining is a place.** What no single read carries and the joining of reads does, a rotation left by two boosts, a
  depth from two standpoints, a duration from two moments, belongs to the join; it is a write only once a unit is
  carried in.

### 12.2 Open

- **A registered prediction: Ω_m = 1/π.** An older draft (23 September 2026) predicted the matter fraction
  Ω_m = 1/π = 0.3183, with Ω_Λ = 1 − 1/π and w = −1, and through Friedmann's equations z_eq = (π − 1)^(1/3) − 1 = 0.2890
  and z_acc = (2(π − 1))^(1/3) − 1 = 0.6240. Its derivation is not accepted here: it multiplies 2/π and ½, the mean
  projection of a uniform direction in two dimensions and in three, as if they were filters in sequence, and the sort
  above would place both with the writer's vantage. But the numbers were written down before the next surveys report, so they
  are a fair test whatever their origin. Planck 2018 gives Ω_m = 0.3153 ± 0.0073 (Planck Collaboration 2020), 0.4σ from
  1/π; DESI's second data release's BAO alone gives 0.2975 ± 0.0086, 2.4σ below. Against DESI's five-year BAO with Euclid
  (2027) and Roman's and Rubin's supernovae and growth (2027–2028): if the best combination sits more than 3σ from 1/π,
  the number is killed.
- **The contrast against the slits' shares.** A double slit with one slit partly covered, recorded photon by photon with
  the shares measured, should lose contrast as sech of the logarithm of the amplitudes' ratio, the same at k and 1/k. The
  duality relation is long tested; what would be the sort's is reading it as a ratio.
- **Ratio or angle, in a measured reader.** x/ẋ gives time to contact at every distance; θ/θ̇ overstates it by π/2 at
  the corner. Responses to looming that run on to large visual angles would tell which an animal uses there.
- **A calibration as one shift.** A published parallax zero-point should appear as one common factor across a
  catalogue's distances, not shrinking with the number of stars (§7.3).
- **Why the counts give 1.2** (§6.3): a bright all-sky Gaia sample with extinctions, its slope by height above the plane.
- **A test for convention.** The scale test is one change applied to the whole world. Generalised, it says: a thing is a
  convention only if changing it leaves every reading of every arrival unchanged. In a world with a medium at rest the
  frame and the simultaneity of distant events would fail that test and be measured; in a world without one they pass.
  Stated before any run, it could be put to real data where a convention is in question (a parallax zero-point; the
  epoch of a clock).

## Code and data

The checks and measurements cited are in the repository that holds this paper (reportbase/wander), each with its plan
written before it was run and its runs recorded as they came out, the killed ones too. By section:

- §2: the one pole and the phasor against five other kernels, `plans/opl-plan.md`, `runs/opl/`; relays, `plans/sum-plan.md`.
- §4: motion from reads and special relativity in shares, `plans/mot-plan.md`, `runs/mot/`; E² = (pc)² + (mc²)²,
  `plans/emc-plan.md`, `runs/emc/`; time and the standpoint, `plans/tim-plan.md`, `runs/tim/`.
- §5: the moving sky, `plans/sra-plan.md`, `plans/srr-plan.md`, `runs/sra/`, `runs/srr/`; the quasar dipole,
  `plans/ebd-plan.md`, `runs/ebd/`; two boosts joined, `plans/twg-plan.md`, `runs/twg/`; loops that come home turned, `plans/hol-plan.md`,
  `runs/hol/`.
- §6: the inverse square, `plans/isr-plan.md`, `runs/isr/`; the near field, `plans/nrf-plan.md`; light and number on the
  stars, `plans/mag-plan.md`, `plans/cnt-plan.md`, `plans/gcn-plan.md`.
- §7: parallax as a sum of reads, `plans/pxs-plan.md`, `runs/pxs/`, after `plans/tri-plan.md`; parallax from the corner,
  `plans/pxc-plan.md`, `runs/pxc/`; the ladder, `plans/lth-plan.md`, `plans/ltr-plan.md`; many standpoints,
  `plans/stc-plan.md`, `runs/stc/`.
- §8: the qubit, `plans/qbt-plan.md`; the duality relation, `plans/wvp-plan.md`, `plans/duo-plan.md`; weak values and the
  twirl, `plans/qso-plan.md`, `plans/wvr-plan.md`.
- §9: LIGO, `plans/lgo-plan.md`, `runs/lgo/`.
- §10: pool from inside, `plans/pol-plan.md`, `plans/por-plan.md`; cooling, `plans/mrb-plan.md`; the face from home,
  `plans/cfh-plan.md`.
- §11: seeds, `plans/tcf-plan.md`, `runs/tcf/`; relief, `plans/ref-plan.md`.
- §12: D6, `papers/physics.md` §5.1 and `papers/archive/d6-dark-energy.md`.

Each dataset's source, licence and checksum are in its plan; large data are not committed. The working record of all of
it is `papers/physics.md`.

## References

Abbott, R. et al. (LIGO, Virgo and KAGRA Collaborations) (2023). Open data from the third observing run of LIGO, Virgo,
KAGRA and GEO. *Astrophysical Journal Supplement Series* 267, 29.

Aharonov, Y., Albert, D. Z. and Vaidman, L. (1988). How the result of a measurement of a component of the spin of a
spin-½ particle can turn out to be 100. *Physical Review Letters* 60, 1351.

Andersen, T. and Sørensen, G. (1973). *Journal of Quantitative Spectroscopy and Radiative Transfer* 13, 369.

Aspden, R. S., Padgett, M. J. and Spalding, G. C. (2016). Video recording true single-photon double-slit interference.
*American Journal of Physics* 84, 671. Data: University of Glasgow Enlighten, doi:10.5525/gla.researchdata.281.

Atherton, H. W. et al. (1985). Direct measurement of the lifetime of the neutral pion. *Physics Letters B* 158, 81–84.

Bailer-Jones, C. A. L. (2015). Estimating distances from parallaxes. *Publications of the Astronomical Society of the
Pacific* 127, 994.

Bartlett, S. D., Rudolph, T. and Spekkens, R. W. (2007). Reference frames, superselection rules, and quantum information.
*Reviews of Modern Physics* 79, 555.

Berry, M. V. (1984). Quantal phase factors accompanying adiabatic changes. *Proceedings of the Royal Society of London
A* 392, 45–57.

Bitter, T. and Dubbers, D. (1987). Manifestation of Berry's topological phase in neutron spin rotation. *Physical Review
Letters* 59, 251–254.

Bondi, H. (1964). *Relativity and Common Sense*. Doubleday.

Bramon, A., Garbarino, G. and Hiesmayr, B. C. (2004). Quantitative complementarity in two-path interferometry.
*Physical Review A* 69, 022112.

Bridgman, P. W. (1922). *Dimensional Analysis.* Yale University Press.

Buckingham, E. (1914). On physically similar systems; illustrations of the use of dimensional equations. *Physical
Review* 4, 345–376.

Bullock, J. M., Mallada González, L., Tamme, R., Götzenberger, L., White, S. M., Pärtel, M. and Hooftman, D. A. P.
(2017). A synthesis of empirical plant dispersal kernels. *Journal of Ecology* 105(1), 6–19.

Clark, J. S., Silman, M., Kern, R., Macklin, E. and HilleRisLambers, J. (1999). Seed dispersal near and far: patterns
across temperate and tropical forests. *Ecology* 80(5), 1475–1494.

Curry, J. J., Den Hartog, E. A. and Lawler, J. E. (1997). Radiative lifetimes of Dy I and Dy II. *Journal of the Optical Society of America B* 14, 2788.

Drescher, M. et al. (2002). Time-resolved atomic inner-shell spectroscopy. *Nature* 419, 803–807.

Ellis, G. F. R. and Baldwin, J. E. (1984). On the expected anisotropy of radio source counts. *Monthly Notices of the
Royal Astronomical Society* 206, 377.

Englert, B.-G. (1996). Fringe visibility and which-way information: an inequality. *Physical Review Letters* 77,
2154–2157.

ESA (1997). *The Hipparcos and Tycho Catalogues*. ESA SP-1200.

Foucault, L. (1851). Démonstration physique du mouvement de rotation de la Terre au moyen du pendule. *Comptes rendus
de l'Académie des sciences* 32, 135–138.

Gaia Collaboration, Smart, R. L. et al. (2021). Gaia Early Data Release 3: the Gaia Catalogue of Nearby Stars.
*Astronomy and Astrophysics* 649, A6.

Gauss, C. F. (1828). Disquisitiones generales circa superficies curvas. *Commentationes Societatis Regiae Scientiarum
Gottingensis Recentiores* 6, 99–146.

Greenberger, D. M. and Yasin, A. (1988). Simultaneous wave and particle knowledge in a neutron interferometer. *Physics
Letters A* 128, 391–394.

Haff, P. K. (1983). Grain flow as a fluid-mechanical phenomenon. *Journal of Fluid Mechanics* 134, 401.

Hagley, E. W. and Pipkin, F. M. (1994). Separated oscillatory field measurement of hydrogen 2S₁/₂–2P₃/₂ fine structure
interval. *Physical Review Letters* 72, 1172–1175.

Henderson, D. (1975). A simple equation of state for hard discs. *Molecular Physics* 30, 971.

Hofsäss, S., Padilla-Castillo, J. E., Wright, S. C., Kray, S., Thomas, R., Sartakov, B. G., Ohayon, B., Meijer, G. and Truppe, S. (2023). High-resolution isotope-shift spectroscopy of Cd I. arXiv:2210.11425.

Hubble, E. (1929). A relation between distance and radial velocity among extra-galactic nebulae. *Proceedings of the
National Academy of Sciences* 15, 168.

Kato, S. and McCullagh, P. (2020). Some properties of a Cauchy family on the sphere derived from the Möbius
transformations. *Bernoulli* 26(4), 3224–3248.

Larin, I. et al. (PrimEx-II Collaboration) (2020). Precision measurement of the neutral pion lifetime. *Science* 368, 506–509.

Laurentini, A. (1994). The visual hull concept for silhouette-based image understanding. *IEEE Transactions on Pattern
Analysis and Machine Intelligence* 16, 150.

Lee, D. N. (1976). A theory of visual control of braking based on information about time-to-collision. *Perception* 5,
437–459.

Leek, P. J., Fink, J. M., Blais, A., Bianchetti, R., Göppl, M., Gambetta, J. M., Schuster, D. I., Frunzio, L.,
Schoelkopf, R. J. and Wallraff, A. (2007). Observation of Berry's phase in a solid-state qubit. *Science* 318, 1889–1892.

Liouville, J. (1850). Extension au cas des trois dimensions de la question du tracé géographique. Note VI in G. Monge,
*Application de l'analyse à la géométrie*, 5th ed., Paris, 609–616.

Lu, M., Youn, S. H. and Lev, B. L. (2011). Spectroscopy of a narrow-line laser-cooling transition in atomic dysprosium. *Physical Review A* 83, 012510.

Lundeen, S. R. and Pipkin, F. M. (1981). Measurement of the Lamb shift in hydrogen, n = 2. *Physical Review Letters* 46,
232–235.

Lutz, T. E. and Kelker, D. H. (1973). On the use of trigonometric parallaxes for the calibration of luminosity systems.
*Publications of the Astronomical Society of the Pacific* 85, 573.

Oates, C. W., Vogel, K. R. and Hall, J. L. (1996). High precision linewidth measurement of laser-cooled atoms: resolution of the Na 3p ²P₃/₂
lifetime discrepancy.
*Physical Review Letters* 76, 2866.

Peebles, P. J. E. and Wilkinson, D. T. (1968). Comment on the anisotropy of the primeval fireball. *Physical Review* 174,
2168.

Penrose, R. (1959). The apparent shape of a relativistically moving sphere. *Proceedings of the Cambridge Philosophical
Society* 55, 137.

Penrose, R. and Rindler, W. (1984). *Spinors and Space-Time*, Volume 1. Cambridge University Press.

Planck Collaboration (2020). Planck 2018 results VI: cosmological parameters. *Astronomy and Astrophysics* 641, A6.

Schumacher, R. A. and Tarbet, B. (2009). A short Foucault pendulum free of ellipsoidal precession. arXiv:0902.1829.

Secrest, N. J. et al. (2021). A test of the cosmological principle with quasars. *Astrophysical Journal Letters* 908,
L51.

Summhammer, J., Rauch, H. and Tuppinger, D. (1987). Stochastic and deterministic absorption in neutron-interference
experiments. *Physical Review A* 36, 4447.

Terrell, J. (1959). Invisibility of the Lorentz contraction. *Physical Review* 116, 1041.

Thomas, L. H. (1926). The motion of the spinning electron. *Nature* 117, 514.

Tomita, A. and Chiao, R. Y. (1986). Observation of Berry's topological phase by use of an optical fiber. *Physical
Review Letters* 57, 937–940.

Tully, R. B. et al. (2023). Cosmicflows-4. *Astrophysical Journal* 944, 94.

Van Oosterom, A. and Strackee, J. (1983). The solid angle of a plane triangle. *IEEE Transactions on Biomedical
Engineering* BME-30, 125–126.

Volz, U., Majerus, M., Liebel, H., Schmitt, A. and Schmoranzer, H. (1996). Precision lifetime measurements on NaI
3p ²P₁/₂ and 3p ²P₃/₂ by beam-gas-laser spectroscopy. *Physical Review Letters* 76, 2862.

Weisskopf, V. and Wigner, E. (1930). Berechnung der natürlichen Linienbreite auf Grund der Diracschen Lichttheorie.
*Zeitschrift für Physik* 63, 54–73.

Wigner, E. (1939). On unitary representations of the inhomogeneous Lorentz group. *Annals of Mathematics* 40(1),
149–204.
