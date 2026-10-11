# Reader Geometry as Addressing

### A bounded reader, a payload, and the continuous sweep between them

*Working paper, 25 September 2026. Tom Brinkman. This gathers in one place the rigorous draft of 24–25 September and
the rulings, proofs and measurements made on 25 September. Rulings are cited as [R1]–[R151] and quoted in full, with
times, in Appendix A. Measurements and kill logs are in Appendix B. Material about the writer that no proof here uses
is kept in the companion note `writer-notes.md`. Title provisional.*

---

## Abstract

A reader receives two magnitudes together, a vertical part v and a horizontal part h, and keeps only their relation,
the reading v/h. This paper argues that the geometry such a reader has is **an addressing scheme and nothing else**: it
says where on a sweep the reader is, and never how big anything there is. The sizes arrive in every v and h, but they
come without a unit, and dividing, the only way a reader without a unit can make sense of them, removes them. The
paper derives, from the reader's side: the reading and its three landmarks; the fact that a continuous sweep with a
starting point admits no jump to a chosen place, only a sweep or a calculation costing one step per binary digit of the
reader's pixel; the sharp line between a drawing known complete (discrete, pointable, both ends closed) and one not
known complete (a continuous sweep, no count, a horizon); the reader's moves and the projective group they generate;
the Cauchy law as the only thing dividing leaves; the circle as the view from nowhere and each Cauchy as a view from
somewhere; and that every plane shape is a list of v/h, short only of its size, one mirror bit and its lap count. It
then measures, on a library of 73 shapes, that a reader circling a stationary shape recovers it: the reader that keeps
magnitudes recovers the whole outline wherever the path faces it (70 of 73 shapes entirely), the reader that divides
recovers the convex hull, and the difference between them is the concavities. The main claims are proved or measured with predictions registered first; what rests on citation or on one remaining
premise is marked.

---

## 0. Thesis, scope and foundations

### 0.0 Start here: [0, 1]

Take anything that can be all there, none there, or anywhere between: a glass from empty to full, eyes from closed to
open, a push from nothing to all of it. Call none 0 and all 1. The number between is not an amount. It is a share of the
thing's own all, a ratio already, so it needs no unit, and it means the same for a glass as for a lake [R38].

Now take two such things. Each knows its own all; neither knows the other's. Nothing outside them measures both. From
that alone, the rest of this paper follows.

In geometry the two are usually drawn as **H and V: a horizontal extent and a vertical extent, each on [0, 1]** [R38].
Together they are a point in the unit square. The drawing is a convention, not a requirement: H and V can be anything
that has its own none and its own all, so that where it stands is a ratio [R38]. For example:

| domain | 0, none | 1, all | between |
|---|---|---|---|
| everyday | an empty glass, tank or page | full, or read to the end | how full, how far through |
| perception | eyes closed, sound off | eyes open, volume at maximum | how open, how loud |
| physics | at rest; a pendulum at the bottom | the speed of light; the top of its swing | β = v/c; the share of the amplitude |
| engineering | a battery flat, a valve shut | fully charged, fully open | state of charge, opening |
| computing | a progress bar at the start, a disk empty | done, full | progress, fill, place i of N |
| biology and medicine | no oxygen bound, a heart chamber empty | saturated, filled | oxygen saturation, fill of a beat |
| chemistry | no reaction yet, nothing dissolved | complete, saturated | completion, concentration against saturation |
| probability | impossible | certain | a probability, a frequency |
| economics | nothing spent, no share of a market | the budget gone, the whole market | share spent, market share |
| time | the start of a day, a year, a lap | its end | the time of day, the season, the phase |

A relation is any two of these, each against its own all: what is written against what a reader can read, what a battery
holds against what a device draws, the demand on a server against its capacity, a runner's progress against another's,
β against 1/γ. Nothing requires the two to be the same kind of thing.

Everything below is written in the drawing's letters, h and v, and each stays a magnitude on [0, 1] [R37]. That
restriction is what **bounded** means here [R53]: the relation is bounded because each side is held to [0, 1].
**Unbounded** is [0, ∞) [R54]: the reading v/h, which runs from 0 at home through 1 at the corner and without end toward
the horizon at h = 0. Bounded is two numbers on [0, 1]; unbounded is one number on [0, ∞). Going from one to the other is
the division that strips a dimension [R46], so the parallel reader, which keeps the magnitudes, stays bounded, and the
serial reader, which divides, is unbounded. What grows without bound, or changes sign, is only ever how the pair is
read, never the relation.

**Every way two ratios can be related is a sweep from one to the other** [R39]. A point (h, v) in the unit square is a
pair; many pairs are the same relation ((0.2, 0.1) and (0.8, 0.4) both say v is half of h), and they lie on one ray from
the origin. A sweep from (1, 0) to (0, 1) crosses every ray once, in order: every way the two can be related, each once.

*The visual* [R39]: hold your hand out flat. That is H. Turn it until it points straight up. That is V. The motion
between is the sweep. It is symmetric, because H and V share a denominator: your hand. Now put rings on your fingers [R51]. The rings
are the payload. Each finger is an address; the ring on it is what that address holds. Turning the hand does not change the
rings. Now replace those rings with other rings [R52]. The sweep from flat to upright is the same sweep, and each finger
is the same address; only what the addresses hold has changed.

The path the sweep takes is a choice; any path from (1, 0) to (0, 1) meeting each ray once holds every relation.
Three natural ones are charts the series already uses:

| path | where v = h lands | what it is |
|---|---|---|
| the arc, h² + v² = 1 | (0.707, 0.707) | the turn: the hand's own path, this paper's sweep |
| the line, h + v = 1 | (½, ½) | the share v/(v + h): *The Relation Space*'s Part One chart |
| the square's edges: up h = 1, then across v = 1 | (1, 1) | the reading itself: on the first edge v/h is v, a proportion; past the vertex it is 1/h, a count |

The third path draws *The Relation Space* §9, the unit changing hands at the corner, with no arithmetic. And it settles a
collision of names: "each accounts for half" at the fulcrum (*The Relation Space* §5) is the line's picture of the
corner, and "on the arc, never at a vertex of the box" (*The Six Things* §14) is the arc's. The corner is one ray; where
it lands depends on the path.

**The system is the shape; h and v are only ratios to it** [R40]. The shape can be any shape: a circle, a star, an
array, a field, a physical system. Its magnitudes are the system itself. The relation space holds none of them. It holds
the complete set of ways h can be related to v, the same set for every shape, and it sweeps whichever shape is there. The
two are orthogonal in the plain sense: the relation runs across rays (which way the reader faces), the magnitude runs
along a ray (how far out the system is in that direction). A particular figure is the magnitude as a function of the
relation, r against the facing; the sweep supplies the facing, the system supplies the r, and neither carries the
other (Propositions 3, 12, 13). One condition: where a direction meets the shape more than once, the magnitudes cannot
be indexed by the relation alone and need the order of arrival as well (§10.2).

**Serial keeps the ratio; parallel keeps the magnitude** [R41]. The serial reader divides, and keeps the relation: an
address, one number, 1d. The parallel reader does not divide, and keeps the magnitudes, each at its place: the system,
2d. **The serial reader's address is to the parallel reader's magnitude.** The figure is the address followed to its magnitude; neither
reader holds it alone (§7). In the visual, the serial reader is the hand and fingers, and the parallel reader is the
rings [R78].

### 0.1 The thesis

> **The geometry is the sweep, not the system. Shapes, arrays and physics are plugged into it.** [R36]

> **The geometry is not the payload; it is the addressing scheme. Geometry provides the continuous sweep over the
> payload; discrete consumption is possible with indexing.** [R14, R15]

In h and v: a place on the sweep is a reading v/h, and every reading is an address. The payload is what was drawn at
that place, a magnitude. Dividing separates the two: it keeps the place and discards the size (Proposition 7a).
Discrete consumption is a floor at the reader's own pixel ε, lossy, dropping the part of each place inside one pixel
[R16]. Two readers can floor the same sweep at different grains; the addresses and the payload do not change, only how
finely they are consumed.

Three results say this from different sides:
1. the reading stream is **the same for every shape** (§3.4): the geometry does not come from the shapes;
2. the Cauchy is **what dividing leaves, whatever the sizes** (Proposition 7a): it belongs to the addressing;
3. the turn, the shift and the stretch are **the three ways to lay addresses down evenly** (§3.3), and their horizons,
   and closure for the turn, belong to the scheme.

The payload reaches the reader only as motion, how the drawing changes from one address to the next (Proposition 3).
That is why anything plugs in (§10): the addressing never looks at what it addresses.

### 0.2 Scope: reader geometry

The claim is about **reader geometry**, the geometry that survives dividing [R21]. The test: multiply v and h by one
common factor. What is unchanged is address: direction, order, the landmarks, cross ratios, and the scale-free metric
built from them [corpus: *The Boundary* B21–B25]. What changes is payload: length, area, radius, anything that needs a
unit [corpus: *The Relation Space* §19, §23].

**The scale is in the signal, without a unit.** A shape's v and h, as drawn, carry its size; dividing removes it
[R23]. Dividing by h gives the reading; dividing by the pair's own size gives the hold v² + h² = 1. Both remove the
scale, which is why the unit circle has none [R22]. But the size in an undivided v or h has no unit: it is a number, not
a size, and nothing says what it is a number *of*. **Some kind of unit is needed; without an external unit, an internal
one** [R23]. Dividing is taking the internal one.

*Why a unit is needed.* A bare value says how many, but not how many of what. The push (v, h) and the push (λv, λh) are
the same arrangement (A1), so the same arrival could carry any size λ, and nothing in the value says which: scale a
whole drawing by 137 and a raw value moves from 9.1 to 1246.7, while every divided quantity stays exactly where it was
[corpus: *The Boundary* B185]. A number that changes with an arbitrary choice, and carries no mark of the choice, cannot
be compared with anything. To mean something it must be counted in something: "three more than me" needs a unit,
"three times me" does not [corpus: *The Relation Space* §19]. Counting in the reader's own terms is dividing; counting
in anything else is bringing in an external unit. There is no third way. (This is also why, in one register, a size and
a step look the same: Proposition 3.)

**Two additions, not one.** *Completeness* closes the far end (the page, the unit circle, a drawing known complete)
and stays address: its 1 is each part's own whole, not a unit of measure [corpus: *The Relation Space* §16, rule 1;
*The Centring* §4; *The Boundary* B236]. *An anchor with a unit* supplies scale: one v or h kept undivided gives a number
(the "one number short" of a figure [corpus: *The Centring* §5c]), and it becomes a size only with a unit, external or
internal. The rest of geometry is addressing plus such an anchor; Euclidean length is the case with the anchor in.

*Priority.* Fisheye and hyperbolic browsers already use geometry as an addressing scheme [cited: Lamping, Rao &
Pirolli 1995]. What may be new is that here the geometry is forced by dividing, is only addressing, and passes the
payload to the reader only as motion. A database search comes before any such claim (§13, item 7).

### 0.3 Two layers, and how claims are marked

- **The reader/drawing decomposition** (§§1–3, §9–10): the reader supplies the geometry, the drawing the payload, and
  the sweep is the only contact. This is the main claim.
- **The group-theoretic identification** (§§4, 6): the reader's moves generate PGL(2,ℝ), and the Cauchy is the law they
  cannot leave. The projective line is forced by dividing, the group by one premise (§4.0); the rest rests on cited
  theorems.

The first does not depend on the second.

Claims are marked **[proved]** (here, or a short standard argument given here), **[cited]**, **[corpus]** (an earlier
paper of the series, by an executed check), **[measured]** (for this paper, script named, predictions registered
first), **[ruled]** (a definition or choice fixed by ruling, Appendix A) or **[reading]** (an interpretation).

### 0.4 Foundations

*Axioms: assumed, not proved.*
- **A1. The pair.** A push arrives as two non-negative magnitudes together, v going up and h going across; neither is
  privileged. Double the push and it does not move: (v, h) and (λv, λh) are the same arrangement.
- **A2. The sweep.** A bar of 1 sweeps continuously from a horizontal of 1 to a vertical of 1. It has a starting point,
  home. [R17, R19]
- **A3. Complete or not.** A reader either knows the drawing is complete, or it does not. [R20]
- **A4. Readers divide.** A reader keeps the relation of v to h and drops their common size. The scale arrives in every
  v and h; it has no unit, some unit is needed to make sense of it, and dividing is taking the internal one. [R2, R23]
- **A5. The arrangement is free.** How the drawing is arranged along the sweep is not forced. [R13]
- **A6. The reader's limits are chosen**, its pixel ε among them. [R7, R16]
- **A7. One register.** The serial reader holds one number at a time.

*Definitions: names, not claims.*
- **D1. The reading** is s = v/h, with h underneath. [R1]
- **D2. The freedom** is the half-line [0, ∞) the reading lives on: home at 0, the corner at 1, the horizon where h runs
  out.
- **D3. The facing.** A facing is a direction of looking, one per freedom; a freedom's facing is its choice of what goes
  underneath. [R5, R29]
- **D4. Depth** is z. [R6]
- **D5. Address and payload.** A place on the sweep is an address; what is drawn there is the payload. [R14]
- **D6. The payload may be anything**: a magnitude, a state, another address. [R8]
- **D7. The floor.** On the sweep, an index is a place divided by the pixel ε with the decimal dropped: lossy. For the
  sweep the array is only a metaphor. A drawing known complete is discrete from the start and needs no floor. [R11,
  R12, R20]
- **D8. Count and breadth.** N is how many; breadth is extent, not quantity. [R4]
- **D9. Complete and not complete: discrete and continuous** (A3). It is reading in both cases.
  - *Not known complete: the sweep (asymmetric).* Continuous. Only v in terms of h; home contained, the horizon
    approached; no N; no pointing, only algorithmic pointing; discrete places only by the floor, at a loss; a rate can
    be stated.
  - *Known complete: the array (symmetric).* Discrete, e.g. [0, 1, 2, 3]. v and h expressible in each other's terms;
    both ends contained, no horizon; N known; pointing in one step; no floor; no rate.

  The semicircle is the drawing of the complete case, the freedom the other [corpus: *The Six Things* §7: "A relation
  space is resolved when its range contains both of its ends"; *The Relation Space* §6]. Nothing converts one into the
  other: a complete array is not a floored sweep. [R20]
- **D10. Geometry and calculation.** The sweep's own operations are adding bars, order (the sign of the disagreement)
  and the landmarks. Arctan (a place → a number of turn; the common route, not the only one), the square root (a
  reading → the bar's size) and the floor are calculations: engineering, not geometry. [R18, R24]
- **D11. Pointing** is reaching a chosen place in one step, O(1). The sweep has none; a drawing known complete has it.
  [R19, R20]

*Claims, proved or measured below.*
- **C1.** Dividing makes the horizon (Proposition 1).
- **C2.** The sweep is the only contact: the payload reaches a reader only as motion (Proposition 3).
- **C3.** Dividing leaves only the Cauchy; the readings are the Cauchy plus the arrangement's residue (Proposition 7a).
- **C4.** There are exactly three even sweeps: the turn, the shift, the stretch (§3.3).
- **C5.** No reader of the sweep can point; algorithmic pointing costs log2(1/ε) + 0 to 2 steps (§2.4).
- **C6.** The sweep needs no arctan and no root: halving is adding two bars (§2.7).
- **C7.** Where the bar is is state; how many times round is history (§2.6).
- **C8.** Every plane shape is a list of v/h, short of its size, one mirror bit and its lap (Proposition 12).

---

## 1. The continuous observer

### 1.1 The pair and the reading

**Definition 1 (the pair).** A push arrives as two parts together: v, going up, and h, going across. Both are
non-negative, not both zero, neither privileged. The pair (v, h) and the pair (λv, λh), λ > 0, are the same arrangement;
what survives is the **ray**, the pair up to a common size.

**Definition 2 (the hold).** Held against its own size, the pair lies on v² + h² = 1: one representative per ray.

**Definition 3 (the reading)** [R1]. The reader divides: s = v/h. It is the one number of the ray unchanged by doubling
the push, defined whenever h > 0.

**Definition 4 (the freedom)**. The reading lives on [0, ∞). Three named places [corpus: *The Relation Space*]:
- **home**, v = 0: s = 0. Contained.
- **the corner**, v = h: s = 1. The one reading equal to its own reciprocal.
- **the horizon**, h → 0: s grows past every value and is never reached; not a value of s, but where the reading stops
  being formable.

**Proposition 1 (dividing makes the horizon)** [proved]. The ray has no distinguished far end: as the push turns from
horizontal to vertical, it passes through h = 0 like any other arrangement. The reading is unbounded exactly as h → 0.

*Proof.* On the hold, (v, h) = (sin θ, cos θ) is continuous through θ = π/2, and s = tan θ → ∞ as θ → π/2⁻. ∎

So the horizon is not in the pair; it is in the division [corpus: *Keeping the Horizon* §5]. A holder of the pair that
never divides has no horizon.

### 1.2 The facing and the corner

**Definition 5 (the facing)** [R5]. A freedom's facing is its choice of what goes underneath, fixed along the freedom.
Reading h/v = 1/s is another freedom, with the other facing [corpus: *The Six Things* §18].

**Proposition 2 (the corner is the swap's fixed point)** [proved]. The swap s → 1/s fixes exactly one reading, s = 1, and
exchanges home with the horizon.

*Proof.* s = 1/s with s ≥ 0 gives s = 1; on the projective line the swap sends 0 to ∞ and ∞ to 0. ∎

The corner is the one mark a reader certifies without a unit: "you are as much as me" needs no scale [corpus: *The
Relation Space* §9, §20]. Below it the reading is a share of the reader, in [0, 1]; above it the reader cannot hand over
its unit, keeps itself as the unit and counts, the tally and then its logarithm [corpus: *The Relation Space* §9, §19].

*Ruled (R88).* Three landmarks, of two kinds: the corner, which the facing leaves where it is, and home with the horizon, a pair the facing exchanges [corpus: *The Boundary* B52].

---

## 2. The sweep, and why there is no pointing

### 2.1 What the geometry gives

The bar's state is the pair (v, h). From it, with no angle and no calculation, a reader has three things:
- **where the bar is**: the pair, or its reading;
- **order**: of two places, which comes first from home is the sign of the disagreement v_A·h_B − v_B·h_A [corpus: *The
  Relation Space* §25]; no division, no angle;
- **the landmarks**: home, the corner (fixed by the swap) and the horizon.

It does **not** give distance along the sweep. "How far the bar has swept" as a number is arctan(v/h), and that is
calculated, not drawn [R18]. An address is **where the sweep has got to**, not how far it has gone.

### 2.2 Arctan is the point of contact, and it is engineering

To name a discrete point on the continuous sweep, a floor needs a number of turn to divide by ε. Arctan supplies it: it
is where the sweep meets a discrete point, and it must be computed [R18].

### 2.3 No pointing

Pointing means reaching a chosen place in one step, without passing the places before it. The sweep is continuous and
starts at home, so there is no such step, and no coordinate to aim with except a calculated one [R19]. *The Boundary*
§2's "inside is pointing" is withdrawn as worded [R19]: dividing gives where the bar is, not a jump to a chosen place.
Only a drawing known complete can be pointed into (D9).

### 2.4 Algorithmic pointing costs one step per binary digit

[R19; measured: `pointing.mjs`–`pointing3.mjs`, Appendix B.7.] A reader can calculate its way to a place, and the
calculation is itself a sweep. CORDIC [cited: Volder 1959] turns the bar toward home through turns whose readings are 1,
½, ¼, …; each step is a sign test (order) and an addition of bars scaled by a halving; the number of turn comes from a
precomputed table.
- **Cost: log2(1/ε) + 0 to 2 steps** to hold a place within ε, in all twenty cases tested (four places, ε = 2^-10 to
  2^-50). Where the place is does not matter; N enters only through ε (log2 N + 0 to 1 steps to one of N places, at
  N = 10⁶, 10⁹).
- **The corner is the first turn of the sequence**, so the sweep passes it in one step. But holding it costs the full
  count: the loop cannot tell it has arrived. Arriving is not knowing you have arrived.

So algorithmic pointing is a fast sweep, O(log(1/ε)), never O(1) in precision. It is O(1) in N: a working library's
"two operations regardless of dataset size" is the same fact in the other variable.

### 2.5 Arctan in practice, and without it

**Where arctan is used** [corpus: `boma.js`, `angleQuery`, `realDimension`; checked]. Only at **the two edges of a
window**. The reader holds a continuous focus, moved only by panning, and an aperture measured flat. `angleQuery` turns
the aperture into a span of turn with atan(−aperture) and atan(+aperture); every extent and offset in the code cancels
(to 1.2e-16), and the focus never enters the arctan. An aperture of 1, the corner, gives a half-window of a quarter of the
quarter turn. Places inside the window are set forward by tan, which is lossless; arctan runs backward and is the lossy
direction. So arctan is paid twice per window, not once per place. With N unknown the library returns a window and
nothing else; with N known a place's turn is one step, (1 − i/N)·π: D9 in code.

**Arctan is the common route, not the only one** [R24; measured: `contact.mjs`, all held]. Window membership: read the
place from the focus with the compose move backward, r = (s − f)/(1 + s·f), and compare |r| with the aperture; rational,
order only; it agrees with the arctan test in 1,000,000 of 1,000,000 cases. The floored place, N known: bisect on the
places' own readings; the same index every time, in exactly log2 N comparisons. So the choice is a trade: arctan, O(1)
in N and log2(1/ε) in precision; order, log2 N comparisons and no transcendental step.

**Keep the address until contact with the payload** [R25; measured: `defer.mjs`]. Keep the place continuous through k
moves and floor once, at contact: worst error half a pixel, whatever k (0.500 px at k = 1 to 1000). Floor after every
move: the loss accumulates, rms 0.29, 0.90, 2.82, 9.13 px at k = 1, 10, 100, 1000, √k times half a pixel's spread. This
is the corpus's rule one level down: *The Relation Space* §25 keeps the pair undivided until the report.

### 2.6 State and history

*The Boundary* withdrew the rotation count because it "imports a walker, and nobody is walking a path" [B33, B58]. The
sweep does not, within one freedom: where the bar is is **state**, carried whole by v and h, with no tally. Beyond one
freedom it does: u and u + π give the same address [B75], so how many times round is **history**, and needs an unbroken
watch that a one-register reader cannot keep. (A first run of `defer.mjs` scored a sweep past the horizon as a 512 px
error, exactly a half turn: the place was right and only the lap was lost.)

### 2.7 Halving is adding two bars; the square root is the reading's cost

[Measured: `halving.mjs`, all held.] In the sweep, the place halfway between home and the bar at (h, v) is found by
putting the two bars end to end, (1, 0) + (h, v) = (1 + h, v): two equal bars make a rhombus, whose diagonal halves the
turn. It reads **v/(1 + h)**: one addition of pushes, no division, no root, no arctan.
- Equal length is what matters: equal bars of 1e-6, 3 or 1e6 halve to 4.4e-16; bars of 1 and R miss by 0.0024 at
  R = 1.01, 0.17 at R = 2, 0.46 at R = 10.
- Halving the corner gives √2 − 1 = 0.4142 and its swap 2.4142: the Cauchy's quartiles, by adding bars.
- **From the reading alone** the bar's length is gone and must be computed back: s/(1 + √(1 + s²)). At the corner the
  answer is irrational, so no rational expression in s reaches it. The root is the size dividing removed.
- Past the first halving a construction from sums needs the root too, to bring (1 + h, v) back to length 1. The sweep
  never pays this: it has a bar of 1 at every place.

| the reader's calculation | recovers | kind |
|---|---|---|
| **arctan** | a number of turn: where, as a count | transcendental |
| **square root** | the bar's size | algebraic, degree 2: the hold |

The one premise left in the projective theory (§4.0, Step 3: moves respect adding pushes) is the operation that halves
the sweep.

[Cited.] v/(1 + h) is tan(θ/2), the classical rational parametrisation of the circle (stereographic projection from
(−1, 0)); see §5.4 item 2.

---

## 3. The drawing, floored

### 3.1 The drawing and the floor

**Definition 6 (the drawing).** What is read is a **drawing along the sweep**: at every place the bar passes there is a
payload. The sweep is continuous; nothing on it is counted [R11]. An **array** is the metaphor for the drawing cut into
entries; getting from the sweep to an index takes a **floor**, the place divided by ε with the decimal dropped [R12].
What the floor drops is what the resolution horizon is made of (§8.2); N is what the floor makes of the sweep.

*Terms.* **The drawing** is what is read; **a place** is a place on the sweep; **a floored place** i is a place after the
floor; **the count** N is how many floored places there are. "Index", "entry", "array" and "list" appear only as
metaphors or in quotations.

**Definition 7 (count and breadth)** [R4]. The count N is how many floored places; the breadth is the drawing's extent.
They are independent: floored places added inside the range move N and leave the breadth [corpus: *Degrees of Freedom*
§5.15g].

### 3.2 Two layouts: complete and not

The reader has only the place, the address. Known length is the complete case, unknown length the other (D9):
- **Known complete: the semicircle.** Place i takes a share of the turn, θᵢ = (π/2)(i/N). Both ends contained; no
  horizon; addresses **relative** (place i depends on N).
- **Not known complete: the freedom.** Place i takes one step of a unit u, sᵢ = i/u. Home contained; the far end never
  arrives; addresses **absolute**.

They are one sweep divided two ways, evenly in the turn or evenly in the reading, and the arrangement is free (A5)
[R13]. A reader not knowing the drawing complete has no N and is on the freedom.

### 3.3 Three even sweeps

[Cited: the classification of real Möbius moves, e.g. Beardon 1983 §4.3, Katok 1992 §2.1; measured: `sweeps.mjs`,
`stretch.mjs`, Appendix B.1, B.8.] An even sweep is one of the reader's own moves run continuously, and there are exactly
three kinds, told apart by how many places on the reading line they leave fixed:

| even sweep | the move run continuously | fixed places | in h and v |
|---|---|---|---|
| **the turn** (the share, the semicircle) | compose | none | the bar comes back where it started: closure; no horizon |
| **the shift** (the fixed step, s = i/u) | s → s + t | one: the horizon | from home toward the horizon, forever |
| **the stretch** (the ladder gⁱ) | s → ks | two: home and the horizon | reaching neither |

Only the turn gives the Cauchy when divided; what the other two give is the arrangement's residue (Proposition 7a). The
corpus's apparent disagreement between the fixed step and the geometric ladder [*The Unit Rule* §5; *The Observation
Atom* §1.6c] is two of the three kinds.

**The stretch starts at the corner** [measured: `stretch.mjs`]. The turn and the shift carry home to t; the stretch
leaves it at 0, so no stretch leaves home. From the corner, home and the horizon are equally far by stretching,
log_g(1/δ) steps each, unbounded as δ → 0. A ladder s₀·gⁱ is carried onto itself by the swap exactly when s₀² is a whole
power of g (2,000 of 2,000 cases), and among starting readings the swap fixes only s₀ = 1. **A ladder's one unit-free
origin is the corner** [corpus: *The Six Things* §12].

**Two horizons, kept apart** [reading]. On the turn the *bar* reaches h = 0 after a finite sweep; only the *reading*
never arrives. On the shift and the stretch the sweep itself never arrives.

### 3.4 The sweep is the only contact

**Proposition 3** [proved from A7; tested, `interleave.mjs`, Appendix B.3]. A one-register reader, which has divided
out the scale, cannot receive the drawing's magnitudes. Its only contact with the drawing is the sweep: where the bar
is, never how large the drawing is there. Floored, the address of place i is a function of i (and N or u) alone.

*Proof, by contradiction.* Suppose the magnitudes were returned. What already arrives on the one register is motion,
each step scale-free, so the magnitudes would be interleaved with it [R31]; one number per arrival, a size and a
step look the same.
1. *If the reader can tell them apart*, it holds something that sorts sizes from steps: a unit, the scale. But dividing
   removed the scale. Contradiction.
2. *If it cannot*, the magnitudes enter its signal, which then stops being uniform (the addresses are even, the
   magnitudes are not), depends on the writer's scale, and no longer closes. Contradiction. ∎

The scale does arrive, in every v and h (A4); what the proof rules out is keeping it after dividing, on the same
register as the steps. Motion can be computed from magnitudes, not the reverse, without "an anchor and an N" [*The
Boundary* B183–B188]. *The premise:* a reader with a second slot, even one bit tagging "size", escapes the
contradiction; that tag is a second freedom.

*The test.* Seven shapes at three scales: the pure reading and motion streams are unchanged by scale (≤ 7e-16), uniform
through the lens, balanced at the corner and closed; interleaved, every shape fails all four. And laid by share, **the
reading stream is the same for every shape**; the shape reaches the reader only as motion rᵢ₊₁/rᵢ.

**Proposition 4 (arrived and unarrived)** [proved]. On the freedom, with n floored places arrived, the frontier reads
n/u and what lies ahead reads u/n, a reading and its swap, meeting at the corner when n = u. (As turn, arctan(n/u) +
arctan(u/n) = π/2; that sum is the calculation.)

### 3.5 Where the evenness comes from

Laid down in either layout, floored places are uniform in that layout's coordinate. Dividing removed every magnitude,
so nothing is left to make one address differ from the next; the world's unevenness stays in the payload [R32].

### 3.6 A worked example: one drawing, two grains

[Measured: `worked.mjs`, `worked2.mjs`, Appendix B.4.] An ellipse (axes 2 and 1) is drawn along one sweep to the vertical,
and both readers know it is complete (A3). They floor the same sweep at 64 and at 512 places.
- **The addresses belong to the sweep.** At each reader's places, the ellipse, the circle, the ellipse enlarged a
  millionfold and a five-lobed blob give the same readings to one rounding (3.3e-16 relative).
- **The payload arrives only as motion**, unchanged by the drawing's scale × 1e-6 or × 1e6 (≤ 5.6e-16). A coarse motion
  is the product of the eight fine motions across its cell (by construction).
- **One number short.** With the magnitude at home the ellipse is rebuilt exactly at both grains; without it, the shape
  returns (≤ 1.4e-15) and the size does not.
- **Only the grain changes.** The count is 64 or 512, set by the floor, given completeness. The floors nest as cells
  (no disagreement in 200,000 places), not as centres.

---

## 4. The reader's moves

### 4.0 How the projective theory is forced

**Step 1. The projective line is forced by dividing** [proved]. (v, h) and (λv, λh) are the same; the set of pushes up
to size is the projective line, and v/h its coordinate.

**Step 2. Linear moves of the pair are Möbius moves of the reading** [proved]. (h, v) ↦ A(h, v) sends s to
(c + d·s)/(a + b·s); A and λA give the same map, so the moves are PGL(2,ℝ). Every linear move factors as a turn, a
stretch and a turn, with a swap when it flips the facing (Proposition 5).

**Step 3. The premise: a move acts on the reading as a linear move of the pair does.** Respecting doubling is forced;
respecting adding pushes is what makes a move linear. Without it a move may warp the sweep as it likes.

**The Cauchy can tell** [measured: `moves.mjs`, `moves2.mjs`, Appendix B.5]. Linear moves keep the Cauchy on the
predicted member (D ≤ 0.0023); warps outside the Möbius motions miss at first order (up to D = 0.048); warps along them
miss only at second order.

*Letac.* It is false that only Möbius maps keep the Cauchy: Boole's ½(x − 1/x), two-to-one, keeps it [cited: Letac 1977,
via Chin, Jung & Markowsky 2019]. Letac characterises the measurable maps keeping the whole family; the citation is
confirmed, the statement not yet read. A route is visible but **unverified**: the Cauchy laws are harmonic measure on
the line seen from the upper half-plane, and analytic self-maps of the half-plane keeping the line keep the family. *If*
these are the only such maps, a one-to-one one is degree one, a Möbius map, and the premise of Step 3 goes.

*Read, 27 Sep.* Letac's theorem characterises every measurable f keeping the whole Cauchy family: ε·f(x) = kx + a minus
the boundary value of a Poisson-type integral against a bounded singular positive measure μ. With finitely many point
masses, a generic value has (1 if k > 0) + (number of point masses) preimages, so the one-to-one maps are exactly the
affine maps and the real projectivities, with ε = ±1: PGL(2, ℝ). The premise of Step 3 goes in that case, and
Aaronson (1978, Theorem 1.1) extends it to every singular μ. Maximality from the group's side follows from Giblin & Markovic (2006),
Theorem 1.3: PSL(2, ℝ) is a maximal closed subgroup of the circle's orientation-preserving homeomorphisms. Both are
worked out in the working paper *The Reader's Moves Are All There Is*.

### 4.1 Three moves

Given Step 3, a reader holding one reading has three moves [corpus: *One Reader* §2.1]:
- **swap**, J: s → 1/s, the other facing;
- **compose** with t, R_t: s → (s + t)/(1 − s·t), rational in the readings [corpus: *The Boundary* B16]; written as
  tan(arctan s + arctan t) it is the angle register, a calculation;
- **ratio** by k > 0, D_k: s → ks, the log register.

Each acts on the projective line ℝ ∪ {∞}; the freedom is its non-negative chart.

### 4.2 The group

**Proposition 5 (closure)** [proved by the KAK decomposition; corpus: `closure.mjs`]. ⟨R_t⟩ = PSO(2); ⟨J, R_t⟩ =
PO(2); ⟨R_t, D_k⟩ = PSL(2,ℝ); ⟨J, R_t, D_k⟩ = PGL(2,ℝ).

*Proof sketch.* Every g ∈ SL(2,ℝ) is R_a·D_k·R_b; every generator is linear-fractional; J has determinant −1. Checked on
10,000 random g to 3.5e-14. ∎

**Proposition 6 (characterisation)** [proved]. A bijection of the projective line is one of the reader's moves if and
only if it keeps every cross ratio.

*Proof.* Möbius maps keep cross ratios. Conversely, the images of 0, 1, ∞ fix a Möbius g; g⁻¹∘f keeps cross ratios and
fixes 0, 1, ∞, hence every x, since CR(x, 0, 1, ∞) determines x. ∎

The moves are geometric, rational in the readings; the registers as numbers, θ = arctan(v/h) and z = ln(v/h), are
calculations.

### 4.3 The space of readers

A reader's standpoint is a focus (moved by compose) and a zoom (moved by ratio). The standpoints form PSL(2,ℝ)/PSO(2),
the hyperbolic plane [corpus: *One Reader* §3.3; cited: Lamping, Rao & Pirolli 1995].

---

## 5. The circle and the Cauchy: nowhere and somewhere

### 5.1 Unitless, scale-free, and holding no values

The circle enters as the orbit of the compose move. Its 1 is each part's own whole, not a unit of measure, so it carries
no size and can stand for a shape of any size [R22, R27]. Each point is a direction; from a standpoint a direction meets
a shape once, wherever the shape is and however far it runs. So an even sweep on the circle is an even sweep over any
shape, messy or unbounded, and what the shape does to that evenness is its own [corpus: *The Centring* §5a:
the circle is the one figure with no residue]. **Neither the circle nor the Cauchy holds values; both sweep things that
do** [R29].

What the mapping keeps from the drawing:
- even on the circle is not even on the shape: on a straight line it lands as the Cauchy, packed near the foot [corpus:
  *The Boundary* B279]; that unevenness, the fisheye, is the shape's;
- for an unbounded shape the far end is a limit: the direction along it meets it nowhere finite, the horizon;
- the shape must meet each direction once from the standpoint (star-shaped); 17 of the library's 73 figures do not
  [corpus: *The Boundary* B109].

### 5.2 The view from nowhere and the view from somewhere

**The circle is the view from nowhere; a reader's view is from somewhere, and that is the Cauchy** [R28]. The circle has
no standpoint: every direction is alike on it. A reader stands somewhere, at a focus and a zoom (§4.3), and the even
circle seen from there is the Cauchy, located at the focus and spread by the zoom (Proposition 7a). The series already
has this as the lighthouse: a point at distance d from a line, sweeping evenly, lands Cauchy on it [corpus: *The
Boundary* B276–B281].

### 5.3 Facings: one, two, four

A facing is a direction of looking, one per freedom [R29]:

| who holds it | facings | what it is |
|---|---|---|
| an array | one | one freedom, [0, ∞) |
| a reader from somewhere | two: left and right | the ring; the standard Cauchy is an even half turn, (−π/2, π/2) |
| the view from nowhere | four: left, right, forwards, backwards | the shape, closed |

From a standpoint a reading repeats every half turn: a direction and its opposite give one reading [corpus: *The
Centring* §6; *The Boundary* B75]. So a reader from somewhere holds two facings joined at the seam. The second facing is
not a sign put on a magnitude; it is a second freedom facing the other way [corpus: *The Boundary* B55; *Degrees of
Freedom* §5.2]. All four are held only by the view from nowhere. The sphere is left open [R30]; this paper stays in the
plane.

**Each facing has a breadth** [R121]. A breadth is an extent, continuous, like N but not an index (D8), one per facing,
known or unknown; when known it is the same B for every facing. Then one facing is the quarter circle, two the semicircle,
four the circle, and eight the sphere. g ∈ [0, 1] is the radius in the breadth's own lengths, r = 1 + g(B − 1): at g = 0 the
radius is 1, and that is the unit circle (with eight facings, the unit sphere); at g = 1 it is B, the breadth fully
expressed. The turn points to one place within it, x = r · turn/(π/2). Worked out in *Serial, Parallel and Nowhere* §2.4,
with the demo `breadth-sweep.html`. Along the radius an address keeps its magnitude: the turn is the same from r = 1 to r = B,
and g is only the ratio between the two. So the unit circle, which can hold addresses without limit, addresses a breadth
without limit: the address connects the unit circle and the breadth at any B [R122]. The world is breadth, always fully
expressed; g is the ratio between the reader and the world, 0 the reader and 1 the world, r = (1 − g) · 1 + g · B
[R124]. The unit circle is not the reader: read uniformly with no situated observer, it is the view from nowhere [R127].

### 5.4 What the literature says

[Cited, not claimed.] Four standard results sit under §5.1–5.2. None uses the words nowhere or somewhere; each is the
same fact in its own field.

1. **Harmonic measure: the Cauchy is the circle seen from a point.** The Poisson kernel of the unit disc,
   P(r, θ) = (1 − r²) / (1 − 2r cos θ + r²), is the harmonic measure of the circle seen from a point at distance r from
   the centre (Axler, Bourdon & Ramey 2001, ch. 1). At r = 0 it is 1: the even circle. At r > 0 it is the wrapped Cauchy
   with ρ = r (Mardia & Jupp 2000, §3.5). Carried to the line by the Cayley map, the circle seen from the point μ + iσ is
   the Cauchy located at μ and spread by σ, and Möbius maps move the standpoint while keeping the family (McCullagh
   1996). This is §5.2 in the literature's terms: a standpoint turns the even circle into a Cauchy, its focus and zoom
   are the point's two coordinates.

   **⚠ Correction (Sep 25, `toy.mjs` T7).** "Seen" here means harmonic measure, or the Möbius move of the standpoint;
   it does not mean rays. Even rays from a point at distance r inside the circle land on it with density
   (1 − r cos φ)/(1 − 2r cos φ + r²)/2π, which is **half uniform and half wrapped Cauchy**: ½·(1/2π) + ½·P(r, φ)/2π
   (measured to 5e-6; the Poisson prediction missed by 0.083). On a straight line the two coincide, which is why the
   lighthouse gives the Cauchy either way [corpus: *The Boundary* B276–B281]. So a reader's rays from somewhere on the
   circle see half the view from nowhere and half the view from somewhere.

   **The refinement it forces.** In the literature the even circle is not standpoint-free: it is the view from the
   *centre*. And every point of the disc is carried to the centre by a Möbius map, so the centre is not a special place
   but whichever place is taken as origin. So R28 is read here as: *the view from nowhere is the view from the centre
   before any centre is chosen;* once a reader stands at a point off it, that same circle is a Cauchy. The claim
   "a reader's view is the Cauchy" is then the classical one, and the only thing this paper adds is the reading of it as
   addressing.

2. **The rational parametrisation.** The halving reading of §2.7, t = v/(1 + h), is t = tan(θ/2), the stereographic
   projection of the circle from (−1, 0) onto the line, with inverse h = (1 − t²)/(1 + t²), v = 2t/(1 + t²). It is the
   classical rational parametrisation of the circle (the Weierstrass substitution in calculus; the source of all
   Pythagorean triples in number theory). §2.7 is therefore not new; what it adds is the reading that this is the one
   step of the sweep that needs no root.

3. **Directional statistics: normalising removes the scale.** A direction is recorded by dividing a vector by its own
   length, which puts it on the circle; its size is discarded (Mardia & Jupp 2000, ch. 1). The circle is the rotation
   group, and its even measure is the only one every rotation leaves alone (Haar measure). This is §5.1: the circle holds
   no values because dividing removed them, and it is even because no direction is preferred.

4. **The phrase.** "The view from nowhere" is Nagel's (1986): the standpoint-free conception of the world, set against
   each subject's view from a particular place. It is cited as an echo, not an argument: this paper uses it only for the
   circle before a standpoint is chosen (item 1), and makes no philosophical claim with it.

5. **The circle reaches every point of a shape**, in four standard forms, differing in what they ask of the shape.
   *Radial function*: from a standpoint, each direction meets a star-shaped boundary once, at r(θ) (Gardner 1995);
   this is §5.1's, with its limit (17 of 73 figures are not star-shaped) and, where r(θ) is infinite, the horizon.
   *Gauss map*: on a convex shape each direction is the outward normal at one point (Schneider 2014); the circle's point
   is then the facing, not the look. *Conformal map*: the disc maps onto any simply connected region, and for a Jordan
   boundary the circle goes one-to-one onto the boundary (Riemann; Carathéodory 1913); the even circle pushed through
   it lands as the shape's harmonic measure from the image of the centre (Garnett & Marshall 2005), which names
   "what the shape does to that evenness is its own", with the line's Cauchy as the simplest case. *Parametrisation*:
   a closed curve is by definition a continuous image of the circle, and the line is the circle less one point (the
   horizon). The mathematics is classical; reading it as addressing is this paper's.

---

## 6. The law the moves cannot leave

### 6.1 An evenly met turn

**Proposition 7** [cited: Johnson, Kotz & Balakrishnan 1994, ch. 16]. If Θ is uniform on (−π/2, π/2), tan Θ is standard
Cauchy. On [0, π/2) the reading is half-Cauchy, density (2/π)/(1 + s²) = (2/π)h². The corner holds half the weight.

### 6.2 Dividing leaves only the Cauchy

**Proposition 7a** [proved; measured: `divide.mjs`, Appendix B.6] [R33]. Write h = R cos θ, v = R sin θ. Then:
1. v/h = tan θ contains nothing of R, whatever the sizes and scale;
2. swept evenly in the turn, the reading is Cauchy (evenness in the turn is itself a calculated measure; geometrically
   only the dyadic places are laid evenly, §2.7);
3. under a linear move of the pair, A, it is still Cauchy, with focus x₀ = Σ_hv/Σ_hh and spread γ = √(det Σ)/Σ_hh,
   Σ = AAᵀ.

*Proof.* (1) R cancels. (2) Proposition 7. (3) The ratio of the two parts of a pair with covariance Σ is Cauchy(x₀, γ)
[cited: Johnson, Kotz & Balakrishnan 1994]. ∎

**The one way to get something else** is the arrangement. Points spread evenly along a square's edge by length are not
Cauchy (D = 0.024); on a circle, where length and turn agree, they are (D = 0.0011).

> **The readings are the Cauchy, plus the arrangement's residue.** The circle, which leaves no residue, leaves only the
> Cauchy.

### 6.3 The family is forced

**Proposition 8 (Knight)** [cited: Knight 1976, read 27 Sep]. X is of Cauchy type if and only if (aX + b)/(cX + d) has
the same location–scale type as X for every a, b, c, d with ad − bc ≠ 0. In Knight's own geometric reading: the Cauchy
type is the only type kept by projecting one line onto another from any point off both. **⚠ Corrected 27 Sep.** This
proposition earlier read "if −1/X has a law of the same type, that type is the Cauchy type." That is false: with Θ of
density ∝ 1 + ½ cos 4θ on (−π/2, π/2), X = tan Θ and −1/X have the same law (two-sample KS 0.0017 over 4 × 10⁵), and X
is not Cauchy (KS 0.040 against its best-fitting Cauchy, baseline 0.0011). A single swap is a quarter turn, a rational
rotation; it takes the whole group, or a rotation by an irrational angle (Williams 1969), to force the Cauchy. Kept separate: the n-dimensional projective version [cited: Knight & Meyer 1976, read 27 Sep: a law on ℝⁿ whose type
every projective transformation keeps is of Cauchy type; the proof shows the law's stabiliser is a compact group acting
transitively, a rotation group of a sphere, whose even measure the law is; Dunau &
Sénateur 1987 (see its reference entry); in n dimensions the projective and conformal versions part, §7.9]; the parameter m + iγ moved by the same Möbius map as the data [cited: McCullagh 1996]; and, **not** true
as stated, "the Cauchy family is the only family closed under the real Möbius maps" (point masses are invariant, and any
atomless law's Möbius orbit is closed). Hypotheses still to be checked against the papers themselves.

**Consequence** [reading]. The moves cannot carry a Cauchy law outside the family. Its **shape** is nobody's choice; its
**location and scale** are where the reader stands, its focus and zoom. The circle is the view from nowhere; each Cauchy
is a view from somewhere.

### 6.4 The layout decides whether it appears

**Proposition 9** [proved]. Laid by share, the readings are half-Cauchy. Laid by unit they are uniform in s, and in the
turn their spacing is u/(u² + i²), crowding toward the horizon. So the Cauchy needs an evenly met turn, not a known N.

### 6.5 The density is the slope of the layout

**Definition 8 (density)** [R34]. Floored places per unit of frame: ρ(x) = (dθ/dx)/Δ. For an evenly met
turn (θ is the calculated turn, so this is the describer's account) [corpus: *One Reader* §6.4]:

| frame x | dθ/dx | packs at |
|---|---|---|
| the reading, s = v/h | h² | home |
| the log register, z = ln(v/h) | vh | the corner |
| side-on, holding v | 1/h | the horizon |

The first row is the Cauchy's shape. In n dimensions the central row becomes h^(n+1); the side-on row stays 1/h
[measured: `densities2.mjs`].

### 6.6 The Cauchy with N unknown

**Proposition 10 (the corner count)** [measured: `cornerrule.mjs`]. On a steadily met turn, with c arrivals from home to
the corner, the arrivals past the corner mirror those before it (the swap); below the corner the count is
c·(4/π) arctan s (the calculation). Checked at 400, 4000 and 40,000 steps; laid by unit instead, the mirror is off by a
factor of s. The rule uses neither N nor the step size, only steadiness; it forecasts a lap of 2c. Limits [corpus:
*Degrees of Freedom* §5.19a; *The Boundary* B210–B213]: only where the corner is unique; the mirror assumes a sampling
symmetric about the corner; the count needs a register. The corner is where a serial reader can first forecast its lap;
closure is where it knows it.

---

## 7. The readers

### 7.0 Serial and parallel [R41, R45]

> **Parallel keeps the magnitude; serial keeps the ratio. Parallel is 2d; serial is 1d. Serial divides; parallel does not.
> The serial reader's address is to the parallel reader's magnitude.**

The two readers are **serial and parallel: motion and magnitudes** [R44, R45]; serial
receives motion and reads it as ratios, parallel holds magnitudes and counts them. Dividing is the one operation that
separates them, and each difference follows from it.

**v and h are two dimensions by definition, and dividing them strips one** [R46]. It strips it in both senses of the
word at once: two coordinates become one (the plane goes to a line, n → n − 1), and metres over metres is no unit at all
(a dimensionless quantity, in physics' word). The coordinate dividing removes is the one that carried the scale. So
"serial is 1d" and "serial needs no unit" are one statement, and parallel, keeping both coordinates, keeps the units and
needs a ruler.


| | serial (divides) | parallel (does not) |
|---|---|---|
| keeps | the ratio: an address | the magnitude: the system (R40) |
| dimension | 1d | 2d: magnitudes at their places |
| scale | cancelled; needs no unit | kept; comparing sizes needs a unit |
| home (v = 0) | yes | yes |
| the corner (v = h) | yes | yes: comparing v with h needs no division |
| order | yes, the disagreement's sign | yes, the same: the disagreement does not divide |
| the horizon (h = 0) | **yes**: the reading grows without limit | **no**: h = 0 is an ordinary zero |
| its distribution | **Cauchy**: the ratio | **Gaussian**: the magnitudes (R44) |

Home, the corner and order belong to both, because none of them needs division. **The horizon belongs to the serial
reader alone**: it is what dividing by a vanishing h costs. Dividing buys freedom from a unit and pays for it with the
magnitude, one dimension and a horizon.

**Parallel is Gaussian, serial is Cauchy, and one is the other divided** [R44; measured: `gauss.mjs`, all held; cited:
the ratio of two centred normals is Cauchy, Johnson, Kotz & Balakrishnan 1994 ch. 16]. Magnitudes that are sums of many
small independent parts spread as a Gaussian; divide two such, centred on home, and the ratio is exactly Cauchy (KS
0.0027 over 10⁵ pairs; as magnitudes, |v|/|h| is the half-Cauchy with its median at the corner, 0.994). Both are stable
laws, and they average differently: the average of 100 Gaussian magnitudes is ten times tighter than one (9.81); the
average of 100 Cauchy readings is no tighter at all (0.98), so a serial reader cannot average its way to a number. The
condition is isotropy: a Gaussian centred on home spreads its directions evenly, and dividing turns an evenly met turn
into the Cauchy (Proposition 7a); centred elsewhere, at the corner, the ratio stays near-Gaussian (KS vs Cauchy 0.688; vs a Gaussian 0.029, post hoc).
So "parallel is Gaussian" has the status of "the turn is met evenly": a condition on the system, true when the magnitudes
are many small independent contributions.

Three consequences. The serial reader cannot follow an address to its magnitude by itself; it meets the parallel reader's magnitudes
only as motion (Proposition 3), and following the address is the final contact with the payload (§2.5). The parallel
reader cannot address without a unit: its places are positions in its own frame, shares i/N, and need N or a ruler; the serial reader's
address needs neither, so it is how the parallel reader's magnitude is reached when N is unknown. And, as an inference not yet
ruled: the parallel reader is the table, laid out whole (the static, symmetric side); the serial reader is the addressing that moves
through it (the dynamic, asymmetric side).

*Precedence.* An earlier ruling (Sep 22) held that serial and parallel readers both meet horizons. Where it conflicts
with R41, R41 stands: the more recent ruling is the more reliable [R42]. The parallel reader's side-on crowding, where
magnitudes pile at the edge of what it sees, is then a feature of its density, not a horizon: nothing there stops being
readable, and h = 0 is an ordinary zero.

A third reader is kept apart: the **side-on** reader, holding v alone, is also 1d, a projection rather than a ratio
[corpus: *One Reader* §6.4]; it is not the parallel reader of this section, which keeps the magnitudes at their places.

### 7.1 The serial reader

The reader of this paper is the serial reader: one arrival at a time, dividing, keeping v/h (A4, A7). What it holds of a
figure is the figure one number short: across directions a figure leaves its own proportion, the residue r(t₂)/r(t₁)
[corpus: *The Centring* §5c]; the circle is the one figure whose residue is 1 everywhere. It has no N while it reads the
sweep; where a count would use N it uses the corner (§6.6).

### 7.2 The side-on reader, untested

*Nothing in the rest of the paper depends on this.*

| | serial | side-on |
|---|---|---|
| holds | v/h | v, against a frame it keeps |
| size | dropped | kept |
| density | h²: the Cauchy | 1/h: the arcsine |
| horizon | never reached | a rim, v = 1, where it saturates |

The side-on column's arcsine, 1/h and rim appear in none of the earlier papers; *Degrees of Freedom* has the parallel
hangers even in the turn and no horizon for them. Untested. Depth is z [R6]; what the side-on reader recovers from h is
its tilt. (Until Sep 25 this reader was called the outside reader; R41–R45 give that role to the parallel reader, which
keeps the magnitudes at their places, §7.0.)

### 7.3 Two readers

*Depends on §7.2.* Densities do not add; coverage does [corpus: *One Reader* §6.1]. The side-on reader is blind where
h·ds < ε, the serial reader where Δ/(vh) < d; they first overlap where h²v/κ = ε/d, with no N (the egg: 15,105 predicted, 15,100
measured).

---

### 7.4 3d: the two readings combined [R43, R79]

> **A 3d object is the combined serial and parallel readings: the addresses across, and the magnitude forward along
> each.**

*Rewritten Sep 27 under R79. As first written, this section gave depth to the serial reader and the image to the
parallel reader; that version is kept at the end of the section.*

**Three sweeps from a standpoint** [R79]. **Left** runs from home to the horizon on one side, **right** to the horizon on
the other: the front half, the serial reader's two facings, each with its own corner. **Forward** runs out along each
address to the first border: the parallel reader's magnitude, heading toward the vanishing point [R77]. The parallel
reader does not sweep across; it rides the serial sweeps and sweeps **along** each address.

**The count** [R41, R46]. In the plane, a standpoint reads a place as one reading v/h (which line, 1d) and one magnitude
along it (how far, 1d): 1 + 1 = 2. In 3d the address needs two readings against home, x/z and y/z, the image; the
magnitude along it is one: 2 + 1 = 3. *[Reading, to be ruled: in 3d the across sweeps run in two directions, left–right
and up–down, each from home to a horizon; R79 was stated for the plane.]*

**The forward magnitude is what dividing removed.** Dividing strips the dimension that carried the size [R46]; the
forward sweep keeps exactly that size. So 3d is not two separate pairs but one relation read twice: **divided across**
(the serial reader's addresses) and **kept forward** (the parallel reader's magnitude). The address points to the
magnitude [R41].

[Checked: `corner/toy3d-r79.mjs`, Sep 27, after R79. Arithmetic on a tilted torus of 400 points, not a finding.]

| the two readings | what comes back | |
|---|---|---|
| addresses alone | nothing of distance: slide each point along its own line (moving the object 91% of its size) and every address is unchanged (6 × 10⁻¹⁷) | the image is blind to the forward sweep |
| addresses + forward magnitudes, each address followed to its own magnitude | **the object, in the parallel reader's own unit** (3.4 × 10⁻¹⁶) | registration only, no landmark |
| addresses + forward magnitude read against the reader's own size R (divided too) | the object **up to one scale**, and that scale is R (1.3 × 10⁻¹⁵) | the unit is the corner |
| addresses + magnitudes, 5% mispaired | 60% error | registration is the whole cost |

So the combination costs **registration** (each address followed to its own magnitude, R41), and a unit only when the
forward magnitude is itself divided. **Then the unit is the corner**: the reader's own size, where the forward
magnitude reads 1 against it (*The Corner Between the Readers* §2.2; whether a standpoint has such a place from its
front half is B.41). That is *The Unit Rule*'s one scale, and the "balloon" of the series: ratios defined, one scale
injected.

**The lighthouse** is the divided case. A direction below the reader names a line; the ground, a surface at the
reader's own height, turns that line into a distance, in units of the height. The known surface is the landmark, and
the horizon falls where the line never meets it.

**A camera is the serial reader** [measured: `toy3d.mjs` part two, held; unchanged by R79]. A perspective image holds
x/z and y/z, ratios, so by R41 it is a serial reading, and alone it loses depth point by point (sliding each point along
its line of sight moved the object 177% of its size and changed no image point). Combined with depth read against its
own size, it gave the object up to one scale with no shared landmark (5.9 × 10⁻¹⁵): the divided row of the table.

**What the first version measured, read again** [reading]. `toy3d.mjs` part one paired an image kept as magnitudes
across (x and y in the parallel reader's units) with depth as a ratio, and needed one shared landmark to join them:
without it the torus came back only up to a stretch along the line of sight (one-scale residual 324% of size); with it,
up to one scale (2.4 × 10⁻¹⁵). An image kept as magnitudes across has parallel lines of sight and no standpoint: it is
**the view from nowhere's image**. So that configuration joined a view from nowhere to a reading from somewhere, and the
landmark was the price of joining them. From one standpoint under R79 it does not arise.

[Cited.] The classical counterpart: images from uncalibrated cameras give a scene that "may differ from the true
geometry by an unknown 3D projective transformation", upgraded to metric by calibration (Hartley 2014; the
stratification is Faugeras 1995); and structure from motion "can only be determined up to the unknown scale factor",
resolved by an extra measurement such as inertial data (Mustaniemi et al. 2016). What §7.4 adds, from somewhere: the
image is the divided reading and depth the kept one; the unit is needed only when depth too is divided, and then it is
the corner.

*As first written (superseded by R79, kept for the record):* by R41 the parallel reader keeps magnitudes at their places
(2d: x and y, in its own units) and the serial reader keeps a ratio (1d: depth z, read against its own size, in
corners); 2 + 1 = 3 [after *Degrees of Freedom* §5.19, "the 1d signal is where depth comes from, it is the z"]. The
third dimension was said to come from a second pair, one kept whole (2d) and one divided (1d), and the landmark to be
"the serial reader's corner laid on the parallel reader's image".

### 7.5 The address and the payload are orthogonal [R47]

> **The payload is orthogonal to the addresses: the median and the mean are not the same, and the corner shifts as new
> values arrive. The Cauchy is not the payload; it is the address to the payload.**

**Definitions.** An *address statistic* is computed from the order of the arrivals only: which comes before which, the
sign of the disagreement. The ranks, the median, the quartiles and the corner are address statistics. A *payload
statistic* uses the magnitudes: the mean and every sum. *Orthogonal* means each side can be changed completely while the
other side's statistics stay exactly fixed.

**Proposition 14** [proved]. Let X be a finite stream of readings.
- (a) *Address statistics ignore the payload.* For every strictly increasing f, the ranks of f(X) equal the ranks of X,
  and every order statistic picks the same arrival: median(f(X)) = f(median X) for an odd count.
- (b) *Maximality.* If X and Y have the same ranks, some strictly increasing f carries X onto Y. So the ranks keep exactly
  what survives every change of payload, and nothing more.
- (c) *Why median and mean part.* The mean commutes with f only when f is affine on the data; for convex f, Jensen's
  inequality gives mean(f(X)) ≥ f(mean X), with equality only when f is affine there or X is constant. The gap between
  the two is set by the payload's spacing alone.
- (d) *The corner shifts by sign.* After a new arrival, which arrival is the median (odd count) depends only on how many
  arrivals lie on each side of it, never on how far any lies.
- (e) *The Cauchy is an address law.* The reading of an evenly met turn has a median, the corner, and no mean
  (E|v/h| = ∞). It supports order, not sums.

*Proof.* (a) f keeps every comparison, so the sorting order and every rank are unchanged. (b) Sort both; join the sorted
pairs (xᵢ, yᵢ) by straight pieces; the pieces rise because both lists are strictly increasing, and the map sends each
xᵢ to yᵢ. (c) Jensen's inequality. (d) The median of 2k + 1 arrivals is the one with k on each side; a new arrival
changes those counts by one on one side, and which side is the sign of its disagreement with the median. (e) The density
1/(π(1 + s²)) has ∫|s| ds divergent and median 0; on the freedom, |v/h| has median 1, the corner. ∎

[Cited: rank statistics are invariant under continuous strictly increasing transformations (Encyclopedia of Mathematics,
"Rank test"); the treatment of rank tests by invariance is Lehmann & Romano 2005 §6.8 (section located; its
maximal-invariance statement not retrieved, and (b) above does not rely on it). The Cauchy's missing mean: Johnson, Kotz
& Balakrishnan 1994 ch. 16.]

[Measured: `orthogonal.mjs`, registered first; `median.mjs`.] On 2001 readings of an evenly met turn: under five
increasing maps of the payload (x³, sinh, arctan, a random piecewise map, and a steep one), the ranks and the corner's
whole path, which arrival it is after each of 1001 odd counts, are identical, and the corner's value is the map of the
original's bit for bit, while the mean goes from 8.9 to anything from 0.04 to 4.8·10⁹. Under five shuffles of the arrival
order with the payload fixed, the final mean agrees to 3·10⁻¹⁵ and the final median exactly, while the corner's path
differs at 968–985 of 1001 steps. Each side is blind to the other. One registered outcome was not met: under sinh two
readings overflowed to ±∞, order survived but the mean became undefined rather than different (logged in
`orthogonal-predictions.md`).

**The measure, not the statistic** [R47; measured: `measure.mjs`, all held]. Two different changes can reach a statistic,
and they are kept apart by different things. *Rescaling the payload* (any increasing map of the values) is kept out by
using order only: Proposition 14. *Re-timing the arrivals* (the same outline met at a different pace, the clock of F2) is
kept out by taking the statistic **over the addresses**, evenly spaced directions, instead of **over the arrivals**. On a
five-lobed star met at an even clock and at a drifted one: the mean over arrivals (the leaf centroid) moves 27% of the
radius, and so does the *median* over arrivals, 2.8%; the mean over addresses (the census centre) moves 0.005%, and the
median over addresses 0.017%, which is the polyline's discretisation. So median against mean is one case of the split,
not its definition: what the payload cannot reach is **order, taken over the addresses**.

**Proposition 15 (the address measure, on the first border)** [proved; measured: `measure2.mjs`, `shapes/library-test.mjs`;
R50]. Let a closed curve be met at any timing t ↦ φ(t), increasing and onto, and from a standpoint c let r(φ) be the
distance to the **first border**, the first crossing along direction φ. A statistic of r taken over the address measure
(φ spread evenly over the turn, each direction weighted alike) is the same for every timing; a statistic taken over the
arrival measure (t spread evenly, each arrival weighted alike) is the same for all timings only when φ(t) is linear. Any
statistic of r that uses order only is also unchanged by any increasing map of r (Proposition 14). *No shape condition is
needed:* the first border is a property of the curve on any closed shape. Being star-shaped from c decides only
*coverage*, whether the first border is the whole outline; where it is not, the rest is the backside (§7.6), reached only
from another standpoint (§10.0, F1). *Caveat:* the first border is found here with the outline in hand. A serial reader
also receives the backside's arrivals; their directions repeat directions already received, and without magnitudes it
cannot tell a first crossing from a second. It detects the backside as the stream turning back (the evenness check's
"not met once", §10.0), not as a place.

*Proof.* The first crossing along φ is fixed by the curve's point set, and the address measure is defined from φ alone; t
enters neither. The arrival measure is dt carried to φ by
φ(t); its density in φ is 1/φ′(t), which is constant exactly when φ is linear in t. ∎

*Measured.* The residues left by the address statistics above vanish as the leaves grow, while the re-timing does not:
from 512 to 4096 leaves the census-centre shift falls 4.06, 4.13 and 4.32 times per doubling to 6·10⁻⁷ of the radius,
and the address median falls 70 times over the three doublings to 2·10⁻⁶ (its step-by-step rate was registered as
between 3 and 5 and was not: 7.1, 2.5, 4.0, one order statistic's chord error jumping), while the leaf-centroid shift
holds at 0.2727 and the arrival-median shift at 0.026.

*On the shape library* [measured: `shapes/library-test.mjs`, registered first; the 73 single-loop shapes of svg.html's
PRIMITIVES, extracted verbatim]. Each outline met at an even and a drifted clock: the leaf centroid moved on all 73 (by 8–29%
of size) and the arrival median on 66; **the median distance along even directions moved at most 1.2·10⁻⁴ of size on all
73**, the 16 that are not star-shaped included. Two registered lines failed. (i) The census centre held on 66 of 73, not
the 95% registered: on seven shapes its fixed point is not unique, and my implementation seeded it from the leaf
centroid, an arrival statistic, so the pace chose the basin (0.02–0.72 of size). An address statistic seeded by an
arrival statistic inherits the pace; the page seeds from one leaf the reader chooses, a standpoint rather than an
average over arrivals. (ii) "Which direction holds the median"
under an increasing radial map held on 50 of 73: symmetric shapes tie many directions, and the map moved vertices, not the
curve. Post hoc, the median *value* follows the map to within 10⁻⁴ of size. Logged in `shapes/library-predictions.md`.

**Which even sweep lays the addresses** [R59; measured: `shapes/measure3.mjs`, registered first; B.14]. "Spread evenly"
above needs a name. The addresses can be laid by any of the three even sweeps (§3.3): the **turn** (even in angle), the
**shift** (even in the reading, a pinhole's pixels) or the **stretch** (even in the log of the reading). Changing from one
to another is a monotone re-spacing of the same addresses along the same sweep: **a change of pace on the reader's side.**
On the 73 library shapes, four facings, 4096 addresses per sweep:
- *statistics of order and value do not depend on the sweep*: the number of times the payload crosses a fixed level was
  the same under all three on 72 of 73 (73 of 73 at four times the addresses); the largest and smallest payloads agree
  in the continuum, and at a fixed count differ only by resolution (misses fell from 9 to 2 when the addresses were
  quadrupled, the two left being cusps);
- *statistics of density do*: the median moved by more than 0.5% of size on only 26% (shift against turn) and 36%
  (stretch against turn) of shapes, far fewer than the 80% registered, but where it moved it moved a lot (xmark 33%,
  astroid 31%, star8 22%, hinge4 19%): shapes whose payloads fall in clusters, where the median sits in a gap;
- *within any one sweep, the median is still pace-free*: re-timing the outline moved it by at most 2.1·10⁻³ of size, on
  all 73.

Why most medians did not move (post hoc, labelled): the three sweeps share their landmarks. Each keeps every facing's
share, the corners (reading ±1) and the mirror a ↔ −a. When a shape's symmetry lines up with the facings its median
falls on a landmark and is pinned: on the ellipse every address of the long-axis facings holds more than the payload at
the corner and every address of the short-axis facings holds less, so the median *is* the payload at the corner v = h,
whichever sweep lays the addresses. **A median on a landmark is pinned; a median between clusters is not.**

So Proposition 15 is to be read with its sweep named: a statistic over addresses *laid by a given even sweep* is the
same for every timing of the arrivals. Changing the sweep changes the reader's own pace, and only statistics of order
and value, or a density statistic that falls on a shared landmark, survive that.

This was first drawn and measured in the reading view of `svg-inline.html` [corpus: the edit view's reading button,
`drawCauchyAddresses` and `censusOf`]: the circle holds the addresses, "a DIRECTION and nothing more … the leaves have
nothing to do with it"; from each address a ray goes to the magnitude it names; where a direction meets the shape again
behind its first crossing, "nothing on the circle changes — the address is one address". Its census centre is "the point
that is the mean of what it sees" along uniform directions, and its own test (`test-centre.js`, not re-run here) found the
leaf centroid moving 37.380 under a drifted clock while that point moved 0.000; reproduced above on another star. One
honest note on that view: its circle is placed at the payload's means (centre and mean radius, taken over the addresses),
so the drawn circle is the addresses *set at* two payload summaries, not the addresses alone (compare R29).

**What is proved and what is claimed.** Proposition 14 is about the definitions and cannot fail. The claim it supports,
that the reader's addresses *are* order statistics, rests on the corner being the median of an evenly met turn
(Proposition 7a, §6.6); that is where a reviewer would press.

### 7.6 What the failures show

The registered lines that failed in §7.5's shape-library test were not noise. Each is logical once seen, and each marks
a place where one side of the split reached the other. They are kept here because they say where the claim's edges are.

**1. An address statistic started from an arrival inherits the pace.** The census centre is a mean over directions, so it
should be timing-free (Proposition 15), and on 66 of 73 shapes it was. On seven (the grazing family, the rose, the
infinity sign, the chevron) it moved by 2–72% of size. These shapes have more than one resting place for "the point that
is the mean of what it sees", and the iteration was started from the leaf centroid, a mean over arrivals. When the
arrivals were re-timed, the start moved, and the iteration settled in a different basin. The statistic was on the address
side; its starting point was not. Where a shape offers more than one resting place, **which one the reader reads from is
a choice of standpoint**, not a fact about the shape: the view from somewhere (§5.2) has to be supplied, and if it is
supplied by an arrival statistic, the pace chooses it. svg-inline.html supplies it from the leaf the reader chooses
(Sep 7: "the reader's geometry builds outwards from him").

**2. Order names values, not always places.** "Which direction holds the median distance" survived an increasing map of
the payload on only 50 of 73 shapes. The failures are symmetric shapes, where many directions share one distance, so no
single direction holds the median; any of the tied ones may be reported. The median *value* followed the map to within
10⁻⁴ of size on every shape. Proposition 14 is about values in order, and it holds; what fails is asking an order
statistic for a unique address where the shape makes several addresses equivalent. The circle is the extreme: every
direction ties, no direction is singled out, which is the view from nowhere (R28) seen from inside a test.

**3. Between samples the reader has nothing.** The payload map was applied to the sampled points, not to the curve, so
along a direction that falls between two samples the new distance is only approximately the map of the old one (chord
error, up to 10⁻⁴ of size). A change to the payload acts on what arrived; between arrivals there is no payload to change.
This is the floor (§3.1) appearing inside a payload test.

**4. Where a direction meets the shape twice, the addresses stop covering it.** On the 16 shapes that are not
star-shaped, the median over directions was still timing-free (the first crossing is a property of the curve), but
between 8.5% (the bulb) and 99.6% (the rose) of the outline was never a first crossing. The shape condition bites on *coverage*, not on *invariance*
(Proposition 15 now states it so): what the addresses reach is still unaffected by the pace; they just do not reach everything (the seam,
§10.2).

**5. The rose: a reader standing on the crossing.** Seen from its census centre, 99.6% of the rose is hidden and its mean
distance did not change under the payload map. Checked afterwards: the rose passes through its own centre, where all its
petals cross, and the census settles exactly there. Every direction's first crossing is at distance ~10⁻¹⁶, the reader
standing on the curve itself, so the map r ↦ r + 2r³ changes nothing it can see (10⁻⁴⁴ of size). Everything else is
behind that first crossing.

**The backside** [R49]. Items 1, 4 and 5 are one thing: what a reader from somewhere does not face. A standpoint faces
its front; the hidden stretches of a non-star shape, the other resting place of a multi-basin shape, and nearly all of the
rose are behind it. The claim holds on what is faced, and what fails is only ever the backside: the part that a second
standpoint, not a better statistic, would reach. Item 2 is the opposite limit, the circle, where nothing is behind and
nothing is in front: every direction alike.

The same pattern runs through the day's other misses: the clock's rounding near the horizon (a root, the reading's cost,
§2.7), closure recognised one place late (a landmark is passed, not arrived at, cpp S10), and even rays from a point
inside a ring landing half evenly and half as a wrapped Cauchy (rays are not harmonic measure, §5.4). **Each failure sits
at a seam between the two sides: where the reading pays, where a landmark is crossed, where a standpoint must be chosen,
where symmetry makes addresses equal.**

### 7.7 Motion: the parallel reader holds the frame, the serial reader reads the swap [R55]

A shape that moves is the hand visual (§0.0) run frame after frame: the fingers stay where they are, and the rings are
replaced with other rings [R52]. The two readers split the work.

**The parallel reader holds the frame.** From a standpoint it sweeps the addresses (even directions) and keeps, at each,
the distance to the first border: a magnitude, bounded [R53]. One frame is one set of rings.

**The serial reader reads the swap.** At each address it divides the payload now by the payload in the frame before. That
is a reading on [0, ∞), unbounded [R54], with the usual landmarks: **the corner (1) is stillness**, above or below it the
border came nearer or went farther, home (0) is the border collapsing onto the standpoint, and toward the horizon is
something appearing where there was almost nothing.

**What each motion looks like.**
- *Scale* about the standpoint: every address reads the same ratio. Scale is the reading's level, and by Proposition 14
  the median over addresses gives it whatever the magnitudes.
- *Translation*: seen from a fixed standpoint, addresses on one side read above the corner and on the other below, in one
  swing around the sweep: the reading's first wave. A standpoint that follows the shape (the census centre, an address
  statistic, each frame seeded from the last) moves with it.
- *Rotation*: not a change at any one address but a slide along the sweep, each address taking its neighbour's ring. It
  is visible only where neighbouring rings differ; a shape with n-fold symmetry is read up to 2π/n, and a circle turning
  about its centre is invisible to both readers.
- *Deformation*: what is left.

All of this is taken over addresses, so by Proposition 15 a change of pace between frames does not reach it; the same
frames read by arrivals (leaf k against leaf k) are fooled by it.

**Measured on the 73 library shapes** (B.11; a known similarity, scale 1.08, rotation 5.73°, translation 5% of size, with
the outline re-timed between frames). On the 63 shapes whose first border does not jump, translation, rotation (up to the
shape's own symmetry) and scale came back to around 10⁻⁵ of size and 5·10⁻⁴°. Read by arrivals, translation and scale
were wrong on all 73 (median 26% and 9.5%). The first wave pointed within 20° of the translation on 81% of star-shaped
shapes. Six of the eight registered lines were killed, wholly or in part; B.11 has each.

**The frame and the signal** [R66; B.21]. Tom, 27 Sep, 03:14: "serial signal is dynamic and the parallel signal is static.
the parallel signal is much larger, but than it gets updated real time with the serial signal, but the serial signal does
not give details, just that somthing is moving." Held as a frame, the parallel reading is large and carries the content;
the serial reading is small and mostly the corner. Frame × serial reading = the current frame, at every address where
the reading stays off home and the horizon. At those two landmarks (a ray starting or stopping to meet a border) the
frame needs a fresh parallel look.

**Where it fails is the backside again** (§7.6; sharpened by the rerun in B.15: none of the failures was the grid; three
are a census centre balanced on a saddle between two resting places, three a jumping first border). All ten shapes on which tracking failed have first crossings that jump:
six are not star-shaped and four graze. The census centre is equivariant under a similarity in the continuum, but read
along finitely many fixed directions it is not, because moving the shape changes which rays graze, and on three grazing
shapes the census leaves the moved standpoint by half the size even when started there. A standpoint cannot be tracked
across a jump in what it faces. From a fixed standpoint the same thing shows as jumps in the serial reading: a move can
expose a backside (five star-shaped shapes stopped being star-shaped once moved) or swing a grazing hit a long way
(six more). The corner is stillness to the chord error: with no motion, the median address reads exactly 1, but single
addresses near sharp corners do not.

**What is classical.** The payload over addresses read from a centre is the *centroid distance function* of shape
description [Zhang & Lu 2004], there taken from the centroid rather than from an address statistic. Turning rotation
into a slide along the angle and scale into a slide along the log of the distance is log-polar (Fourier–Mellin)
registration [Reddy & Chatterji 1996]. What this section adds is the attribution: the frame is the parallel reader's,
the motion is the serial reader's reading with stillness at the corner, and it is timing-free because it is taken over
addresses, not arrivals.

### 7.8 Recovery: a reader circling a stationary shape [R56]

Turn §7.7 around: the shape stays still, and the reader moves around it on a circle, always facing it. From each stop the
reader has a view from somewhere (§5.2): it faces the shape's front, and the rest is its backside (§7.6). The front seen
from one stop is part of the backside seen from another. The question is what the stops add up to, and the two readers
give different answers.

**The parallel reader recovers what the orbit faces.** At each stop it keeps, along each direction in its view, the
distance to the first border: the front, as magnitudes. Placed in one frame by the known stops, the fronts add up to the
outline, except for any stretch that is never a first crossing from anywhere on the orbit: a pocket no stop faces.

**The serial reader recovers the convex hull, in the plane.** It divides, so it keeps directions and not distances [R46]. Facing the
shape, what it has at each stop is where the shape begins and ends in its view: two directions, a wedge. The shape is
inside every wedge, and in the plane, with the stops outside the shape, the wedges close down onto the convex hull. (In
three dimensions the same intersection is the visual hull, which can be tighter than the convex hull: a hole seen
through along its axis is carved out.) A concavity cannot show: the depth that would reveal
it is what the division strips.

So the split is: **parallel gives the faced set, serial gives the hull, and the difference between them is the
concavities.** What neither reaches is a pocket that no position on the orbit faces.

**Measured on the 73 library shapes** (B.12; 64 stops on a circle of three times the shape's size, 1024 directions across
each view, the orbit known). **The parallel reader recovered the whole outline of 70 of the 73 shapes**: all 25 convex
shapes and 45 of the 48 non-convex ones. On every non-convex shape it found points well inside the hull (the shallowest,
the crescent, 2% of size), so it sees concavity. What it missed is on three shapes that cross themselves or fold back on
themselves: spiro 30.5% of the outline, fork 3.3% and rose 3.1%, all of it pocket inside the hull, none of it on the hull.
**The backside is reached by other standpoints, as §7.6 said:** the census centre, standing still, had missed 8.5–99.8%
of the 16 shapes that are not star-shaped from it; from the orbit, 13 of those were seen entirely, and the rose went from
99.8% hidden to 3.1%.

The serial reader's wedges came out 1–4.9% larger than the hull on 26 shapes at 64 stops, against a registered 1%: a kill.
All 26 have a hull with long straight sides, either the shape's own or the bridges the hull lays across a concavity. A
straight side is pinned only by a stop on its own line; between such stops the wedge edges pass through its two end
vertices and leave a thin sliver outside it. More stops close the sliver, in steps: at 256 stops all eleven shapes
rechecked were within 0.6% of the hull. So the serial reader does converge to the hull; straight sides need more stops.

**What this shows.** A reader from somewhere never sees its own backside, but a reader that moves does: the shape is
recovered in full wherever some position on the path faces it. What is lost is not lost to the reading. It is lost to the
path, and a different path (a stop inside the pocket's mouth) would reach it.

**What is classical.** The serial half is the visual hull, shape from silhouettes [Laurentini 1994]; in the plane with
the stops outside, recovering a convex set from support lines [Prince & Willsky 1990]. The parallel half is the
integration of range scans [Curless & Levoy 1996]. What this section adds is the attribution: the two classical methods
are the two readers of this paper, the concavities are exactly the difference between dividing and not dividing, and the
backside of §7.6 is what a single standpoint misses and a moving one recovers.

**Not yet tested:** the orbit unknown to the reader, which must then recover its own step between stops by §7.7's
machinery (open item 13).

### 7.9 A first look at the sphere [R58]

*A session record: the first probe of the unit sphere, run to see what falls out, with predictions registered first.
It is not yet a treatment of 3D. Exact, noise-free, on analytic shapes.*

In three dimensions a relation is three magnitudes, h, v and a depth d, each on [0, 1]. The parallel reader keeps all
three: 3d, bounded. The serial reader divides by the facing axis and keeps two readings, v/h and d/h: dividing still
strips one dimension [R46], and the address is now two numbers on [0, ∞) × [0, ∞). The expectation was that the sphere
would work like the circle. Where it was probed, it did.

**The Cauchy comes along, one dimension up.** Directions spread evenly over the facing hemisphere, read serially, give
the two-dimensional Cauchy (the radius r of the reading has P(R ≤ r) = 1 − 1/√(1 + r²), its angle is uniform); so does
Gaussian ÷ Gaussian, as in the plane (§7.0). After any linear move of the three magnitudes (a move of the standpoint),
the reading is still a two-dimensional Cauchy, stretched into an ellipse whose centre and shape the move predicts: the
sphere's form of the circle's rigidity (§6.3). The literature has both halves (searched Sep 26). The central
projection of an even hemisphere is the *projective Cauchy*, density ∝ (1 + |x|²)^−(n+1)/2 in n dimensions [Dupuy,
Belcour & Heitz, arXiv:1909.07605]; that the Cauchy is the one continuous family invariant under projective maps, in
any dimension, goes back to Knight & Meyer (1976) and is given explicit parameter formulas, with a computer vision use,
by Mendonça & Lundell (2025).

**On the sphere the two Cauchys part.** There is a second one. Stereographic projection of an even sphere gives the
*conformal Cauchy*, density ∝ (1 + |x|²)^−n, whose type is kept by inversions [Dunau & Sénateur 1988]. On the line both
are (1 + x²)^−1: one law, kept by the Möbius maps, which on the line are the projective maps. In the plane and above they
are two laws and two groups: **dividing (the serial reader, central projection) gives the projective one**, which is the
one measured here; the conformal one belongs to inversions. The circle hid a choice the sphere makes visible.

**Every sweep of the sphere must stand still somewhere.** On the circle a sweep can run forever without stopping; on
the sphere it cannot. A smooth sweep of the whole sphere has still points whose indices add to 2, the sphere's Euler
characteristic [cited: the Poincaré–Hopf theorem; the hairy ball theorem is its best-known case]. What falls out is
*where* the reader's own sweeps stand still:
- the three planar sweeps, h→v, h→d and v→d (the last the wrist's twist about the facing), each stand still at the two
  directions they do not involve: ±d, ±v and ±h. **The six directions of looking are exactly where the three sweeps
  stand still**;
- the sweep that cycles all three, h→v→d→h (the turn about the diagonal), stands still at **the corner v = h = d** and
  its opposite. In §7.7 the corner was stillness in motion; here it is stillness of the sweep itself.
The total, 2, is the sphere's counterpart of the circle's closure (§9; four sweeps of the bar and home). Whether it is
the right counterpart is open (item 15).

**Recovery works as the plane said** (§7.8, now in 3D; B.13). 128 stops on a sphere around the shape, each facing it:
- *parallel*: every point of ball, ellipsoid, cube, capsule, torus and bowl was faced (100%). A sealed hollow is never
  faced from anywhere (74.0% seen, 73.5% predicted from its share of the area). A blind hole was 99.5% seen; everything
  missed lies deep in the hole. One ring of stops is not enough: from the equator alone, 94.4% of a ball is seen
  (94.3% predicted), the caps never.
- *serial*: in 3D the silhouettes' intersection is the visual hull, tighter than the convex hull where a view passes
  through the shape: the torus's hole is carved (71% of its convex hull). A cavity, a hollow and a blind hole do not show
  in silhouettes (bowl, shell and drilled cube stay at their convex hull). The parallel reader sees into the bowl, the
  torus and the hole (28–71% of size inside the hull).

**What has not been looked at.** Three things change on the sphere and none has been probed:
1. *Order.* On the circle the sign of v_A h_B − v_B h_A puts two places in order along one sweep. On the sphere the sign
   of a 3×3 determinant gives the handedness of three directions, not a line-up: there is no one sweep that meets every
   address once in order, so a serial reader must choose a path (latitudes, a spiral, a raster). On the circle the
   sweep is given; on the sphere it is a choice.
2. *Motion.* A turn in 3D has three parameters and they do not commute, so §7.7's single slide along the sweep does not
   carry over as it stands.
3. *Closure.* Whether index 2 is to the sphere what four sweeps and home are to the circle.

That the first probe went this easily says the pieces carry over: the reading, the Cauchy, the moves of the standpoint,
and the two readers with the backside between them. It does not say 3D is done. Order, motion and closure are where the
sphere will cost something, and the probe was exact and noise-free.

### 7.10 Two readers of one solid: each errs at its own blind spot [R61]

The rung editor (`3d.html`, Tom's tool for making 3D pieces) reads a solid from an **axis**: at each height a circle of
horizontal rays. Its point reader (§7.9's six facings, added to it) reads the same solid from **one point**. On the corner
box the two drew different caps: pinched under the axis reader, flat under the point reader. Registered first and run
on eight exact solids, with the same budget of about 8,200 addresses each (B.16):
- **Flat caps favour the point reader**: on box and cylinder its error is 0.04% of the volume, against 1.3–1.4% for
  the axis reader. 82–93% of the axis reader's error lies at horizontal surfaces, and **none of its addresses lands on a
  cap**: to the axis reader a flat cap is not a place but a jump between the last height inside and the first outside.
  Its rays run parallel to the cap, which lies on the horizon of every one of its circles.
- **Overhangs favour the axis reader**: on a pawn and a mushroom it is 9–13 times better (4% against 37% and 55%). From
  the centre, the ball above the pawn's thin neck and the mushroom's cap above its stalk lie behind what the point
  reader faces first: its backside.
- **Round solids favour neither much** (both under 1% on sphere and ellipsoid); on a box tilted 35°, the point reader is
  better by about two.

So **each reader's error sits at its own blind spot: the axis reader's at surfaces parallel to its rays (its horizon), the
point reader's behind what it faces first (its backside).** No reader is best for every shape; a reader does best on the
shapes that are star-shaped from its standpoint. Two registered lines were killed, neither by a reader: one by a bug of
mine (the ellipsoid's distance function is 0 at its centre, so the point reader's standpoint read as outside; fixed, it
is 0.08%), and one by a classification built for errors that are thin skins, which does not apply to a hidden volume.

**Two readers together** [R62; B.17]. A reader standing inside a solid *certifies* what it faces: along each address, the
stretch up to the first border is solid. What lies beyond is not certified empty; it may be the backside. So two readers
combine by the **union** of what each certifies, never the intersection, which would let one reader's backside delete
what the other sees. Registered first, on the same eight solids: the union was never more than 0.2% of the volume worse
than the better reader; better than both on pawn and mushroom (narrowly: 4.1% against 4.2% and 4.3%, because both
readers are, by inference, blind at the pawn's base top and the mushroom's flat underside); and 3–10 times better than the axis reader
on box, cylinder and cone, though not as good as the point reader alone there, since a union keeps the axis reader's
over-fill above the caps.

**Does a reader know its blind spot?** A reader can look at its own payloads for **jumps** (neighbours differing by more
than a factor 1.3, or one of them 0). 97–100% of the axis reader's error sits within two addresses of its own jumps:
it knows where its caps are. The point reader's does on the pawn (92%) but not on the mushroom (9%): it sees where its
backside *begins*, and a backside narrower than that reach is found, a wide one is not (post hoc, two solids only). This
is §7.5's caveat met in 3D: the backside shows as an event, the stream turning back, not as a place.

**A second look where the first reader's payloads jump** [R63; B.18]. If a reader sees where its backside begins, it can
send a second reader there: at each jump take the longer side, mark the point halfway along it, and stand the second
reader at the mean of those points; no jumps, no second reader. Registered first: no jumps were found, and none were
needed, on sphere, ellipsoid, box, cylinder, cone and tilted box; on the mushroom one guided second reader took the error
from 55% to 2.2% (a random second reader averaged 12.7%; the axis reader 4.3%). On the pawn it failed (35%): its jumps
come in two groups, one for the ball above the neck and one for the base below it, and their single mean falls back into
the neck. Post hoc, one reader per group still left 30%, because halfway down the longer side of a downward jump falls
short of the base. The rule needs **one reader per backside, placed past the edge its jump marks**.

With both repairs, registered first and run [R64; B.19]: the jumps' edge points are grouped by nearness (a ring of jumps
around one hidden part is one group), and each group's reader stands a quarter of the way past the edge along the longer
addresses. The pawn showed two groups and the mushroom one; the pawn went from 37% to **1.6%** and the mushroom from 55%
to **2.4%**, each better than as many random readers (12.0%, 7.3%) and than the axis reader (4.2%, 4.3%); on the six solids
with no backside nothing was sent. **A reader that looks at its own jumps can say how many backsides it has and where to
stand to see each one.** The positions are its own: taken from its payloads along its addresses, with no view from
nowhere.

## 8. Fixed fidelity, N unknown

### 8.1 The order of limits

Classical accounts take ε → 0 and then N → ∞, which removes the reader's density. The series' readers keep ε fixed
while N grows, unknown [corpus: *The Cauchy, Inside and Out* §0].

### 8.2 ε is the pixel

The **structural horizon**, h = 0, belongs to the division; the **resolution horizon**, where neighbouring addresses
differ by less than ε, belongs to the reader. ε does not change the density's shape; coarseness is set by εN. Noise is
the one limit that bends the curve [measured: `noise.mjs`].

### 8.2a Resolution

**The breadth is the world's; the resolution is the reader's** [R34, R35]. **Resolution** is how many places the reader
tells apart: about 1/ε, whatever N is (§8.4). Density (§6.5) is how those places pack; resolution is how many there are.
- *Complete (N known):* resolution is also a share, the fraction of the N places told apart, about 1/(εN). This is the
  quantity the series called g, "the expression", and before that the unit radius: 1 when all N are told apart, 0 when
  none are, and quantised by closure to multiples of 2/N [corpus: *Degrees of Freedom* §1, §5.15b].
- *Not complete (N unknown):* there is no share, since there is no N to divide by. Resolution is a count, fixed by ε
  alone. Holding ε fixed while N grows (§8.1), the share falls toward 0: the reader who never learns N tells apart the
  same number of places over an ever larger world.
- *Resolution 0:* nothing is told apart, and no reading exists. What remains is the circle, which holds no values
  (§5.1). This corrects a withdrawn claim, "at g = 0 every shape is the unit circle" [corpus: *The Boundary* B110]: the
  code's refusal at g = 0 was right, since at resolution 0 there is nothing to read, not a circle read.

From the limb count (§8.3), the most places told apart come at εN ≈ 4.1, a share of about 0.27.

(The letter g in §3.3 and Appendix B.8 is the ladder's ratio, *The Unit Rule*'s sense, and is unrelated.)

### 8.3 The count told apart

**Proposition 11 (the limb count)** [derived; corpus: `rigor.mjs`]. N points evenly on a circle, read side-on at
fidelity ε: of the N/2 visible, the number told apart is **R(N) = (N/π)·arccos(εN/2π)** for εN ≤ 2π, and 0 beyond.

*Derivation.* Neighbours at angle φ are about (2π/N)|cos φ| apart in v; resolved when that is at least ε; the share with
|cos φ| ≥ εN/2π is (2/π) arccos(εN/2π). ∎

It matches every measured count to within two (1120 against 1121.3 at N = 4000, ε = 10⁻³), peaks at εN = 4.098 with
**R_max = 1.1222/ε**, and falls to zero by εN = 2π.

### 8.4 The budget

At fixed ε the number of things told apart is O(1/ε), independent of N [cited: Itai, Konheim & Rodeh 1981; Dietz
1982]. Re-uniting the unit whenever the count passes 4u holds the count as exponent and mantissa: floating point
[cited: Goldberg 1991].

---

## 9. Closure

### 9.1 Array, ring, shape

**Definition 9 (array, ring, shape)** [R9]. An array: one facing, one freedom. A ring: two, joined at the seam. A shape:
four facings joined, holding every relation of h to v. Nothing is added to make a shape; it is the same drawing carried
until complete. The ring is RP¹ and the shape its double cover S¹ [cited: Hatcher 2002; Mardia & Jupp 2000]; a closed
plane curve's tangent turns through 2π [cited: Hopf 1935].

*Why four, from the reader's side:* it is not four. A reader from somewhere holds two facings; four, the shape closed, is
the view from nowhere (§5.3) [R28, R29]. A reader can check that the drawing came back round, not hold all four.

### 9.2 How closure is known

A reader cannot count its way round: recovering the facing from order imports a walker [corpus: *The Boundary* B33,
B58]. It checks the return with two checksums [corpus: *The Unit Rule* §17]: the reading returns (order-blind: the
record's moves sum to zero), and the landmarks return in order (order-bearing). An open record proves the shape open; a
closed record does not prove it closed.

---

## 10. Examples, plugged in

### 10.0 What the system still decides

The sweep is the same whatever is plugged in [R36]; four things are the system's:
1. **Whether it meets each direction once.** Indexing by direction needs it; 17 of 73 library figures fail, and for
   them the sweep is carried by arrival order (§10.2).
2. **How the evenness lands.** The sweep is even; what it lands on is spread by the system's own measure, the Cauchy on
   a line and harmonic measure on a shape (§5.4). The unevenness is the system's and reaches the reader as motion
   (Proposition 3).
3. **Complete or not.** Whether N is known belongs to the system: the same sweep gives an array or a freedom (§3.2).
4. **Whether it is met evenly.** Any system plugs in structurally; whether a real one is met evenly is the traverse
   question (§13 item 5), decided system by system. The series' screens refused six of six real signals [corpus:
   *Degrees of Freedom* §12(d2)]. For physics the claim is: can be plugged in, if met evenly.

**Definition 13 (a system).** A map from places on the sweep to payloads, positive magnitudes R, with three facts:
(F1) each place is met once, with R > 0 there; (F2) the places are laid by the sweep, not by the system's own pace;
(F3) N is known (complete) or not. The reader receives (v, h) = R·(place) and divides.

**Proposition 13 (the plug-in)** [measured: `plugin.mjs`, Appendix B.10]. If F1 and F2 hold, the reader's side (the
reading stream, the landmarks, the floored cells) depends on F3 only, never on the payload; the payload reaches the reader
only as motion, R_{i+1}/R_i. Where F1 or F2 fails, the system's shape enters the addresses themselves.

*Proof.* v/h = (R·sin)/(R·cos): R cancels, exactly in the reals and to rounding in floating point (Proposition 3 is the
same fact seen from the reader). F3 decides the layout (§3.2). ∎

*Measured:* ten systems (circle; eight numbers; a five-lobed star; random payloads over six decades; heart volume;
nested lists; a lazy payload; the circle at ×10⁻⁶ and ×10⁶; a clock at speed), complete and not: streams within
3e-16 of the circle's, landmarks and cells identical. The clock, which computes h = R√(1 − β²) itself, reaches 6.5e-15
near the horizon, where 1 − β² cancels: rounding, and §2.7's root, not payload. Breaking the facts shows at once: two
ellipses walked at their own pace (F2) leak into the addresses by 0.50 and 0.67 and differ from each other; a looped
limaçon (F1) reverses four times; a payload of 0 reads NaN; complete meets the horizon once, open never.

Every object below is a drawing along the sweep: a place in, a payload out. The reader's side is unchanged in each.

**10.1 Eight numbers.** 3, 1, 4, 1, 5, 9, 2, 6 on eight places, known complete: the semicircle, place i at share i/8.
The reader holds addresses; the numbers are the payload.

**10.2 A shape.**

**Proposition 12 (every shape is a list of v/h)** [R26; corpus: *The Centring* §5a, §5c; *The Boundary* B104, B107,
B109–B115, B75; §3.6]. A plane figure is given, up to its size, one mirror bit and its lap count, by readings v/h on the
right pairs:
1. **the address**, v/h of one arrival: *where* the boundary is met. Alone it carries no shape: a circle, a star and a
   cloud met at the same directions give one address list [B104];
2. **the residue**, one magnitude against the next: *what* the figure is; the same division on a different pair [B107];
   with the addresses it rebuilds the figure exactly, one number short;
3. equivalently, **the boundary's own direction**, v/h of each small step, spaced by the share of perimeter walked: the
   turning function [cited: Arkin et al. 1991].

*Proof sketch.* The residues compose, so one magnitude and the residues give all of them [*The Centring* §5c]; the
addresses place them. Nothing in either list carries a size, because each is a ratio. ∎

What the list leaves out, each measured: **the size** (it was in v and h without a unit; dividing removed it); **one
mirror bit** [B113–B115]; **the lap** [B75]. *Condition:* indexing residues by direction needs each direction to meet the
figure once; 17 of 73 library figures fail [B109]; indexed by arrival order the residues still compose and close [B111]
but become a figure only once the directions are added back.

**10.3 Physics.** A clock moving at speed: v = β, h = 1/γ, the reading is the celerity βγ, and β² + 1/γ² = 1 is the
definition of γ [corpus: *One Reader* §4.2]. The speed of light is the horizon [cited: Varićak 1910].

**10.4 A system.** A heart's volume through each beat: N "kind of known"; the semicircle is approximately right and the
corner can be seen coming [corpus: *The Boundary* §9.7u–v].

**10.5 A lazy drawing.** Each payload is computed only when its address is asked for [cited: Henderson & Morris 1976]:
the freedom, and a direct case of keeping the address until contact (§2.5).

**10.6 Addresses to another drawing.** Each payload is itself an address: chapters, pages, lines; a semicircle whose
places hold semicircles [corpus: *Degrees of Freedom* §5.11].

In every case the reader did the same thing and got the same geometry.

---

## 11. How classical mathematics reads this

Classical mathematics works from the view from nowhere. "Let θ be a point of the circle" gives the point: pointing is
free, resolution is infinite, N (if any) is known, and ε → 0 is taken first (§8.1). That is its method, not an
oversight, and it is why the reader's costs do not appear there. The maps are all present; no one is using them.

**What it would say of the interpretation.**
1. *The circle as an address space is a chart.* Coordinates are addresses by definition, so this is a re-description,
   not a theorem. Granted.
2. *Scale-free is standard.* Dividing by size sends the plane less the origin onto its rays, the circle; v/h without
   the sign is the projective line RP¹. §5.1 is these, named.
3. *The circle reaches every point of a shape* in four standard forms (§5.4 item 5), of which only the conformal one
   covers every simply connected shape.
4. *The Cauchy is elementary.* The tangent of an evenly spread angle is Cauchy. What Proposition 7a adds is not its
   mathematics but the claim that this is all a dividing reader gets.
5. *The Cauchy is on the reading, not the shape.* An even sweep lands Cauchy on a straight line; on any other shape its
   hits are spread by the shape's own measure (§5.1).
6. *Nowhere and somewhere are metaphors.* Their content is the Poisson kernel and the Möbius maps that move the
   standpoint (§5.4 item 1).

**Where it would have to engage.** The claims about cost: pointing takes about one step per binary digit (§2.4); the
floor can be deferred to contact with the payload; resolution is about 1/ε whatever N is (§8.2a, §8.4); complete and
not complete are different layouts (§3.2). Classical geometry has no way to state these. Computable analysis does, and
agrees in outline: a real number arrives as a stream of approximations, and equality of reals cannot be decided
[cited: Weihrauch 2000], which is §2.3's no pointing and B.7's loop that cannot recognise arrival. Numerical analysis
and CORDIC keep the cost of arctan and the root (§2.5, §2.7); computer graphics keeps the split between addresses and
values (a texture's (u, v) holds places, its texels hold values). The pieces sit in separate fields; this paper's
contribution, pending §13 item 7, is joining them, and its most original claims are also the ones most in need of
checking against computable analysis.

### 11.1 How the framework differs from the classical methods it meets [R57]

§7.7 and §7.8 met five classical methods head on. This section summarises how the reader framework differs from them
and what that might mean. It is a start, not the full treatment: a separate paper is to take it up thoroughly (§13 item
14). Everything under *What it might mean* is inference, not result.

**The methods, side by side.** The basic operation is shared: a pinhole camera records x = f·X/Z, a ratio of two
magnitudes, which is the serial reader's v/h scaled by the focal length; log-polar registration takes the log of a
ratio of radii, which is the log of §7.7's serial reading.

| their method | what they measure | the same thing here | how they differ |
|---|---|---|---|
| visual hull [Laurentini 1994] | silhouettes from calibrated cameras; cones cast back and intersected | the serial reader's wedges (§7.8) | they need pose and focal length; in 3D their hull can be tighter than the convex hull |
| support lines [Prince & Willsky 1990] | a parallel projection's extent at known, evenly spaced angles, with noise; consistency hᵀC ≤ 0 (C circulant); quadratic or linear programming | the wedge edges, seen from a finite orbit; at infinite orbit they become theirs | a support value is a distance, so theirs is a parallel reading at even addresses (normals); ours is serial at uneven ones; they handle noise |
| range fusion [Curless & Levoy 1996] | range along lines of sight, pre-aligned; D(x) = Σwᵢdᵢ / Σwᵢ per voxel, weights falling at grazing; unseen, empty, near-surface | the parallel reader (§7.8) | their "empty" is the stretch to the first border, "unseen" is the backside; they down-weight grazing, where our tests failed |
| centroid distance function [Zhang & Lu 2004] | distance to a centre, indexed along the boundary | the payload over addresses | theirs covers the whole curve but depends on how it is sampled; ours is pace-free (Proposition 15) but misses the backside |
| log-polar registration [Reddy & Chatterji 1996] | phase correlation for translation; Fourier magnitude resampled log-polar for rotation and scale; a 180° ambiguity | the tracked census centre, the slide along the sweep, the median serial reading (§7.7) | they remove translation with the Fourier magnitude, we by moving the standpoint; they take a correlation peak, we a median |

**The frameworks, side by side.** The larger differences are in what each side takes as given.

| | the reader framework | the classical methods |
|---|---|---|
| starting point | two magnitudes on [0, 1], each a share of its own all: unitless and bounded [R53] | coordinates with units: pixel pitch, focal length, metric range |
| the unit | none; dividing is forced, being the only comparison without one | assumed and calibrated; dividing is a sensor model |
| where the reader stands | always a view from somewhere; the view from nowhere, a world frame, is not available to a reader | the output is a world frame; every view is registered into it first |
| registration | bought: registration plus one relative unit (§7.4) | assumed (known poses, pre-aligned scans) |
| the count | complete or open; with N unknown the serial reader has a horizon (§3.2) | complete: so many images, so many pixels |
| pace | the serial reader receives one reading at a time at an unknown pace; the measure (arrivals or addresses) decides what the pace reaches | a frame is taken at once, or timestamps are known |
| kinds of reader | two, derived: serial divides (1d, Cauchy, unbounded), parallel keeps magnitudes (2d, Gaussian, bounded) (§7.0) | sensor types by engineering: camera, range scanner, tomograph |
| distributions | consequences of the reading | error models laid over the data, usually Gaussian |
| addresses | the sweep: an even turn, unitless | a grid of pixels, voxels or angles, in units |
| failure | one thing, the backside (§7.6): occlusion, second resting places, grazing, pockets | handled piecemeal: visibility, occlusion, grazing weights, hole filling |

In one line: **the classical methods start from a calibrated world frame and put readers into it; the framework starts
from a reader with no unit, no count and no frame, and asks what each of those costs to buy.**

**Where the framework is closer than it looks.** Home, the corner and the horizon (0, 1, ∞) are the standard projective
frame on a line, the one the cross-ratio is anchored to; the framework gives them meaning (stillness, the end of the
count) but not existence. Projective first, metric bought later, is Faugeras's stratification [Faugeras 1995], which
§7.4 already follows. The backside is occlusion, and Curless & Levoy's unseen voxels are it; what is new is making it the
one cause behind several different failures, not the idea. And the Cauchy is already at work in vision: it appears in
the distribution of the cross-ratio under Gaussian errors [Mardia, Goodall & Walder 1996], and its projective
transformation formulas are used for triangulation [Mendonça & Lundell 2025]. Item 2 below meets that literature, and
the novelty search (§13 item 7) must start there.

**Where the classical methods are ahead.** Noise and the estimators built for it; three dimensions; efficient
algorithms; consistency conditions (Prince & Willsky's hᵀC ≤ 0 says whether any convex set could have produced the
data); and decades on real sensors. The tests here are exact, noise-free and planar.

**What it might mean** (inference).
1. *Calibration becomes an account.* Each classical assumption (the unit, the frame, the count, the pace) is something
   a reader can be without, and the framework asks what is left without it and what each purchase adds: without a unit
   either reader recovers the shape up to scale; the unit and the registration buy the rest (§7.4). §7.8's test bought
   both (a known orbit, metric distances), so it sits in the classical setting; the unbought version is §13 item 13.
2. *The statistic follows from the reader, not from a noise model.* Averaging parallel readings is sound; averaging
   serial readings is not, because the Cauchy has no mean, and the median is the safe statistic (Proposition 14).
   Curless & Levoy average distances, which the framework allows. Anything obtained by dividing two noisy magnitudes
   is a serial reading and should not be averaged. Depth from stereo disparity, Z = fB/d, would be one such case;
   whether its heavy tails are treated this way in that literature is to be checked, not assumed.
3. *Which statistics the pace cannot reach is a rule, not a habit.* Classical practice gets pace-freedom implicitly, by
   resampling at even arc length or by capturing whole frames. The framework states it: take the statistic over
   addresses (Proposition 15). §7.7's arrival baseline, fooled by a change of pace, is what breaking the rule costs.
4. *Failures can be predicted before a run.* If the backside is one cause, a method's failures should be findable by
   asking where a standpoint cannot see: grazing directions, second resting places, pockets. In §7.7 and §7.8 the kills
   fell there.
5. *Open streams.* Methods that assume the count is known have nothing to say when it is not. The framework says what
   survives with N unknown (address statistics, order, the corner) and what is lost (the horizon is never reached).
6. *Choosing a lens is choosing an address measure.* A rectilinear (pinhole) camera samples evenly in the reading v/h; an
   equidistant fisheye samples evenly in the turn. From an evenly turning standpoint the first gives the Cauchy's
   density across the image, the second a uniform one. This is standard optics; the framework says which reader each
   lens is.

**What the full paper would need.** The novelty search first (§13 item 7). Then each classical method re-derived from
the reader side, stating which assumptions it buys; the averaging rule (item 2) tested on shapes with a planned noise
model; §7.8 repeated with the orbit unknown and without a unit; and any real-sensor test planned in detail before it is
run [R48].

---

## 12. What is proved, cited and measured

**Proved here:** Propositions 1–6, 7a, 9, 13, 14, 15; 11's derivation; 12's sketch; §4.0 Steps 1–2.

**Cited, not claimed:** the Cauchy from a uniform turn; Knight's rigidity and McCullagh's parameter; the real Möbius
classification; CORDIC; the hyperbolic browser; the list-labeling bound; floating point; RP¹ and its double cover; the
turning function; the Poisson kernel and wrapped Cauchy as harmonic measure; the rational parametrisation; Haar measure
on the circle; Nagel's phrase; the radial function, Gauss map and conformal boundary correspondence (§5.4);
computable analysis on deciding equality of reals (§11); the centroid distance function and log-polar registration (§7.7); the visual hull, support-line reconstruction and range-scan integration (§7.8); the projective and conformal Cauchys (Knight & Meyer; Dunau & Sénateur) and the Poincaré–Hopf theorem (§7.9).

**Measured** (Appendix B): Proposition 3 on seven shapes; which moves keep the Cauchy; Proposition 7a; the three even
sweeps and the stretch; the worked example; the corner count; the densities by dimension; the limb count; algorithmic
pointing's cost; arctan-free window and floor; deferring the floor; halving by adding bars; the plug-in
(Proposition 13); 3d as the two readings combined (§7.4); a first look at the sphere (§7.9); two readers of one solid (§7.10, B.16); which even sweep lays the addresses (§7.5, B.14); motion from the two readers on the shape library (§7.7); recovery of a stationary shape by a circling reader (§7.8).

---

## 13. Open

1. ~~**The sign.** Magnitudes or signed?~~ **Ruled (R37): magnitudes.** v and h each range over [0, 1], each against
   its own full; direction is carried by which freedom is read and which facing the reader stands in, never by a
   negative v or h [corpus: *The Boundary* B324–B325; *The Relation Space* §16, §18 remark 1]. The sign that remains is
   the disagreement's, which orders two places; it is not a value's. Still to do: re-read B276, B317/B331 and B115,
   which rest on the question, and the toy and interface code, which use a signed v for the second facing.
2. **Whose the Cauchy is.** Largely answered by Proposition 7a (the shape is the dividing's, the member the
   standpoint's); still to check against the six papers that place it off the reader.
3. ~~**Two landmarks or three** (§1.2).~~ **Ruled (R88): three, of two kinds.**
4. **The side-on reader** (§7.2): untested; its visual name unruled. What the parallel reader keeps is ruled (R41, R44, §7.0).
5. **The traverse question:** which sources, projected, give an evenly met set of addresses.
6. ~~**The last premise of §4.0**~~ **Settled, 27 Sep** (*The Reader's Moves Are All There Is*): by Letac (1977) and
   Aaronson (1978, Theorem 1.1), the one-to-one maps keeping the whole Cauchy family are exactly PGL(2, ℝ), for every
   singular measure; by Giblin & Markovic (2006, Theorem 1.3) and Navas (§1.4), nothing lies between the reader's moves
   and every homeomorphism of its line. The premise goes.
7. **Priority:** a database search before any claim of novelty.
8. **The sphere** [R30]. In the plane three counts coincide at four; on a sphere they part:

   | what is counted | plane | sphere | n dimensions |
   |---|---|---|---|
   | directions of looking | 4 | 6 | 2n |
   | sweeps between neighbouring directions | 4 | 12 | 2n(n − 1) |
   | corners by sign | 4 | 8 | 2ⁿ |

   First look taken in §7.9 [R58]: the six directions are where the three planar sweeps stand still, and the twelve
   sweeps are those three turns in quarters.

9. **Who reads a finished array**, and the word "continuously" in *The Relation Space* §1: moved to `writer-notes.md`;
   no proof here uses them.
10. **The floor rule** of *The Unit Rule*: whether it is the same operation as the floor here.
11. **A real-world test of Propositions 14 and 15** [R48], to be planned in detail before anything is recorded: a source
    whose pace varies a lot while its shape does not, with the predictions, apparatus and kill conditions fixed first.
12. ~~**Motion (§7.7), three repairs before a re-run.**~~ **Rerun with the repairs, B.15** [R60]: the symmetry and
    re-timing faults were the test's; the grazing failures were not the grid but a census centre balanced on a saddle
    between two resting places. Original item: A symmetry detector that finds 6- and 12-fold shapes (the
    registered one did not); a re-timing that is not odd about leaf 0, so the arrival baseline's rotation is tested
    fairly; and a census that stays equivariant where rays graze (directions tied to the standpoint's own frame, or
    many more of them), which would show whether the ten tracking failures are the backside or the grid.
13. **Recovery with the orbit unknown (§7.8).** *First run Sep 27 (B.20): from corners in its own readings the reader
    recovers 12 of 73 orbits exactly and flags every wrong step; point-to-line ICP (post hoc) reaches 44. Open: noise,
    bridging unfound steps, landmarks on smooth borders.* Original item: The reader circling a stationary shape without knowing where it is must
    recover its own step between stops from the overlap of successive views (§7.7), then add up the fronts. To be
    registered separately; expected to fail where §7.7 failed (grazing, jumping first crossings) and to leave symmetric
    shapes recovered only up to their symmetry.
14. **The framework against the classical methods** [R57]: a separate, thorough paper. §11.1 is its summary and lists
    what it needs.
15. **The sphere, next** (§7.9): which path a serial reader should take when the addresses cannot be lined up (order);
    motion in 3D, where turns have three parameters and do not commute; whether index 2 is the sphere's closure; and the
    recovery tests with noise and with the stops unknown.
16. **Which sweep the reader's addresses are** (§7.5, R59): the reader framework says a reader addresses by its readings,
    which is the shift (a pinhole); the view from nowhere is even in the turn. Whether the paper's address measure is to
    be the turn's, the shift's, or named case by case, and whether a density statistic can be chosen to sit on a
    landmark by construction (the corner as the median of an evenly met turn, Proposition 7a).

---

## Appendix A. Rulings (provenance)

As recorded, with dates and quotes. The paper cites them as [R1]–[R144]; where a ruling was refined, the later
wording is the working one.

1. The reading is **v/h**: h goes underneath.
2. **Readers divide.** Dividing is what removes the scale, and choosing what goes underneath is what gives a reader its
   horizon. Readers require actual horizons.
3. **One writer, two readers.** The builder is **the writer**: the writer builds the system, and holds it from
   everywhere. Readers don't build; they read. There is one writer and two types of reader, inside and outside (Tom,
   Sep 24). "Semi-circles are for builders, horizons are for readers."
4. **The view from everywhere is just breadth**, and **breadth means extent, not quantity**. The count N is a different
   thing.
5. **One facing per freedom.**
6. **Depth is z.**
7. The reader's limits are **chosen**.
8. **The magnitude list is anything that can be indexed.** Known length: the semicircle. Unknown length: the freedom.
   *Refined by 11–13*: both are the same sweep.
9. **A shape is an array with four facings and the complete set of h relative to v.**
10. Neither the inside nor the outside reader knows N, and both meet a horizon (Sep 22).
11. **No indexes; the freedom is a sweep** (Tom, Sep 24: "Indexes are a computer science concept, they are not needed.
    The freedom is a sweep, not an index.").
12. **The array is a metaphor only.** Indexing needs a floor operation, which is lossy: it removes the decimal (Tom,
    Sep 24: "Arrays are fine, but it requires a floor operation, it is lossy, removing the decimal. Its a metaphor
    only.").
13. **One sweep; the writer does the math, and nothing is forced.** The semicircle and the freedom are the same sweep;
    the writer "is free to arrange the signal however he chooses, nothing forced" (Tom, Sep 24).
14. **The geometry is not the payload; it is the addressing scheme** (Tom, Sep 25).
15. **Geometry provides the continuous sweep over the payload; discrete consumption is possible with indexing** (Tom,
    Sep 25).
16. **The indexing can be done at the reader's ε** (Tom, Sep 25: "the indexing can be done at the users epsilon"). The
    floor is the reader's, at its own pixel; with ruling 7 (limits are chosen), each reader picks its own grain on the
    same sweep.
17. **Geometry is a sweep: you start at home and sweep to where you want to go; you can't just point at it** (Tom,
    Sep 25: "the interesting thing is geometry is a sweep, you start at home and sweep to where you want to go. you
    can't actually just point at where you want to go."; 04:30: "there is no way to just point at something on the
    sweep."). Worked out Sep 25 (§1.5):
    - **the state of the bar is (v, h)**, not an angle. Geometry gives a place, an order (the sign of the
      disagreement v_A·h_B − v_B·h_A) and the landmarks; it does not give how far the bar has swept;
    - **an address is where the sweep has got to**, not how far it has gone;
    - **the square root belongs to the reading, not the sweep** (Tom, Sep 25: "is it needed for the sweep or just
      the reading of the sweep?"; §1.5): halving the sweep is adding two bars;
    - **the walker test** (*The Boundary* B33, B57, B58): where the bar is is **state**, carried by v and h with no
      tally, so no walker is imported inside one freedom; how many times round is **history** (u and u + π give
      one address, B75), and there the walker returns. The ruling holds up to the lap and no further;
    - **pointing** (random access) needs the whole sweep laid out at once, which is the writer's, the view from
      everywhere. The floor names a place already swept to; it does not give pointing.
18. **Arctan is engineering, not geometry** (Tom, Sep 25, 04:26: "arctan is not geometric it is algoritmic."; 04:30:
    "arctan is the point of contact between the continuous sweep and a discrete point on that sweep. but it is
    engineering and must be calculated, its not geometric."). Arctan turns a place on the sweep into a number of turn,
    which is what a floor needs before it can name a discrete point. It must be calculated (a series, a table); the
    drawing does not hand it over. Every use of it in this draft is marked as the calculation, not the geometry
    (§1.5).
19. **You can't point; *The Boundary* is wrong on this** (Tom, Sep 25, 04:47: "No, you can't point, the boundary is
    wrong. the sweep is continuous and has starting point. you can't just point to somewhere on the sweep. you can
    algorithimically point, but that is not an O(1) operation."). Pointing means reaching a place on the sweep in one
    step, O(1). No reader can. A place can be reached by calculation (algorithmic pointing), but that costs steps.
    *The Boundary* §2's "inside is pointing" (dividing to get a direction) is withdrawn as worded: dividing gives
    *where the bar is*, not a jump to a chosen place.

20. **Complete or not** (Sep 25). 05:03: "the writer example, the writer does not stop drawing though, the moment she
    stops, N is defined." 05:06: "maybe the writer does stop at some point, its more that the reader has no access to
    that. the moment the reader has access to the stoping point, its a semi-circle not a freedom." 05:10: "its not so
    much as the writer stopping puts you on a semi-circle, its that V and H are now symetric, where they were previously
    asymetric." 05:15: "a reader can know a finished array [0,1,2,3]. they can know its finished. its still a type of
    reading. maybe, when you know the complete array its no longer a continuous sweep, but a discrete array." 05:17:
    "confirmed." Operational content: A3, D9. The writer-side material is in `writer-notes.md`.
21. **Reader geometry** (Sep 25, 07:35–07:40). "Is all of geometry addresses or just reader geometry"; the scope agreed:
    "Yes".
22. **The unit circle has no scale** (Sep 25, 07:42). "The unit circle by definition has no scale."
23. **The scale is in the signal, without a unit** (Sep 25). 07:54: "The v and the h of shapes have the scale, but
    dividing removes that scale." 08:24: "So the scale is in the signal, you just remove it when you divide them." 08:41:
    "However these values have no unit. As a result, no way to makes sense of them without the readers hold." 08:46:
    "Just say some kind of a unit is needed. Without an external unit, an internal unit would be needed."
24. **Arctan is the common route** (Sep 25, 06:39). "arctan is the most common way to do it. there are probably other
    ways."
25. **Keep the address** (Sep 25, 06:41). "the common wisdom in computer science is to keep the address until final
    contact with the payload."
26. **All shapes are v/h** (Sep 25, 07:49). "All shapes can be represent as v/h."
27. **The unit circle's use** (Sep 25, 08:53). "The unit circle is unit less and scale free, which may seem to be a
    contradiction. But that is why this mathematical abstraction is so useful. It can be used for even uniform sweeping
    of a messy reality. Every point on a unit circle can be mapped to any point on a infinitely large shape."
28. **Nowhere and somewhere** (Sep 25). 08:55: "Yes, the unit circle is a view from everywhere. Readers have a view from
    somewhere, and that is cauchy." 09:10: "Nowhere seem better."
29. **No values; facings** (Sep 25). 09:03: "Both unit circles and cauchy are unitless and scale free, they contain no
    values, they sweep systems with values. If you can see all four facings, you have a view from nowhere. If you have a
    view from somewhere, you have two facings." 09:10: "An array has only one facing". 09:17: "the second facing is the
    second degree of freedom, you can left or right. The fourth freedom, is just four degrees of freedom, you can look
    left right forwards and backwards. A shere just adds up an down."
30. **The sphere, open** (Sep 25, 09:22). "Someone just needs to map all this out. Leave the sphere open."
31. **Proposition 3 by contradiction** (Sep 24). "If the magnitude list was returned to the reader, its signal would be
    interleaved with the motion signal"; "if magnitudes were included, the signal would not be uniform and we know that
    it is. Also we can prove it empirically with shapes."
32. **The projection makes the addresses even** (Sep 24). "it's the projection that removes the scale and creates the
    uniform arrays of address, the world is not uniform."
33. **Only the Cauchy emerges** (Sep 24). "The cauchy emerges when you divide away the scale. Its the only thing that
    emerges. We can show that easily."
34. **Density is the reader's** (Sep 21, Sep 24). "the breadth is the world, the density is the reader."
35. **g is named resolution** (Sep 25, 14:15–14:16). "g was just a place holder until a better name came along." Offered
    *resolution*; "ok".
36. **The geometry is the sweep** (Sep 25, 14:26–14:27). "what about the idea the geometry is just the sweep, not the
    system itself. that we can plug different systems, shapes, arrays, even physics into the sweep." Offered as the head
    of §0.1 with §10.0; "yes".
37. **v and h are magnitudes on [0, 1]** (Sep 25, 15:55–15:57). "what we have is two things that can range from [0,1].
    From that simple constraint, all this complexity emerges." Asked whether that rules the sign (open item 1):
    "i so rule."
38. **Start from [0, 1]** (Sep 25, 16:08–16:10). "any discussion of this should start with simply explaining [0,1]. it is
    the ratio of all or none of something and everything in between." Then: "State that the typical way this is
    described in geometry is with H and V, horizontal and vertical extents of [0,1]." Then: "but it is not required,
    H and V could be anything that can be represented in such a way. anytying that can be reprsented as a ratio. give
    examples from a variety of domains." 
39. **The sweep holds every relation; the hand** (Sep 25, 16:14–16:18). "Every possible way that two ratios can be
    related is represented by a sweep between them. [0,1] related to [1,0]." Then: "hold your hand horizontally, that is
    H, move your hand vertically, that is V. the distance traveled beween those two motions is the sweep. it is symetric
    and both V and H share a denonimnator, your hand." 
40. **The system is the shape** (Sep 25, 16:25–16:26). "A shape is just the complete set of ways h can be related to v.
    The magnitudes that they point to are orothogonal to the shape. the magnitues are the complete system itself, that
    can be swept with the geometry of the relation space. the h and v are not the system, they are just ratios to the
    system." Asked which thing "shape" names: "my point about shape is that it could be any shape, they system is the
    shape." 
41. **Inside and outside** (Sep 25, 18:03–18:12). "outside keeps the magnitude, inside keeps the ratio." "outside is 2d,
    inside is 1d?" "inside divides, outside does not?" "the inside's address is to the outsides magnitude?" Offered as
    one ruling with the table in §7.0 (home, corner and order shared; the horizon and the Cauchy the inside's alone):
    "yes." 
42. **Precedence** (Sep 25, 18:18). Asked about R41's horizon row against the Sep 22 ruling that serial and parallel
    both meet horizons: "my more recent rulings are more reliable." (The same rule as Sep 22's "Todays results take
    precedent when there is conflict.") 
43. **3d** (Sep 25, 18:21–18:58). "this nice part about this framing is it gives a clean runway to 3d. a 3d object is
    then the the combined inside and outside readings." Then, on recording it and building the test: "proceed". 
44. **Parallel Gaussian, serial Cauchy** (Sep 25, 19:05–19:06). "the outside is gaussian and the inside cauchy, but not
    literally inside and outside, it is serial + parallel = motion + magnitudes." Offered with the ratio-of-Gaussians link
    and a check: "yes". Supersedes the Sep 24 ruling "gaussian is not correct here. The outside is just the shape itself,
    and all of its perturbations" by R42; the two can stand together if the shape is the centre and its perturbations
    the Gaussian spread. 
45. **Drop inside and outside** (Sep 25, 19:09). "i'm thinking we should drop inside and outside, inside what, outside
    what/. it has heavy visual imagery that is more of obsfiscating than claryfing." The paper says serial and parallel
    (motion and magnitudes, R44) throughout; quotes and paper titles keep their words; the reader that holds v alone,
    formerly also called outside, is the side-on reader (§7.2). 
46. **Dividing strips a dimension** (Sep 25, 19:12). "v and h are literally two dimensions by definition. dividing them
    is literally striping the dimensinoality." Offered with the two senses (coordinates and units) and the second-pair
    point for §7.4: "yes". 
47. **The address and the payload are orthogonal** (Sep 26, 05:53–06:23). "the proof that payload is orthogonal from the
    addressess is that the median and the mean are not the same and that the corner shifts as new values arrives.
    cauchy is not the payload it is address to the playload." Then: "how should we proof this? to make it undeniable."
    Offered as definitions, Proposition 14 and a two-way demonstration: "yes". Pointed to the reading view of
    svg-inline.html (06:27); refinement to arrival measure against address measure, with a reproduction: "ye". 
48. **Real-world tests are planned, not improvised** (Sep 26, 06:49). "remove the real world test. that needs to be done
    carefuly and planned with great detail." A quick test on a real ECG was run and removed from the paper on this
    ruling. 
49. **The failures are the backside** (Sep 26, 06:57–06:59). "the failures are interesting but logical. lets discuss the
    failures in the paper." Then, on §7.6: "it makes sense, its the backside." 
50. **The first border** (Sep 26, 07:01–07:02). "so it works for the first border encountered." Offered as the restated
    Proposition 15 (no star-shaped condition; star-shaped decides coverage; the serial reader's caveat): "ok". 
51. **Rings on the fingers** (Sep 26, 10:06). "The first visual metaphor of the hand sweeping from horizontal to vertical
    should add rings to the fingers. The rings are the payload."  
52. **Other rings** (Sep 26, 10:11). "Replace those rings with other rings" — the hand visual's demonstration of
    orthogonality: the payload is swapped, the sweep and the addresses are not.  
53. **Bounded** (Sep 26, 10:15). "Bounded means the relations being restricted to [0,1]."  
54. **Unbounded** (Sep 26, 10:18). "Unbounded is the [0,inf)"  
55. **Motion** (Sep 26, 10:34–10:52). "I wonder if we can capture motion of a shape. Using the serial and parallel
    readers." The test was proposed with its predictions: "Yes". After the run: "Yes add this section and the test
    results."  
56. **Recovery** (Sep 26, 10:55–11:01). "Shapes are stationary and the reader rotates around them, facing them, can the
    shape be recovered." The test was proposed with its predictions: "Yes". After the run: "Yes add this to the paper.
    It's very important, shows the shape can be recovered fully."  
57. **How the framework differs** (Sep 26, 11:03–11:16). "Do a comparison of our reader math to theirs." "What about the
    differences with our reader framework?" Then: "Yes, excellent. Add this different comparison and your comments to
    the paper. Im more interested in how our framework is different, and what that might mean. We can do a full
    thorough paper on this in another paper. But lets get that started here with a summary of the situation."  
58. **The sphere** (Sep 26, 13:55–14:13). "Let's take a peak ahead to unit spheres. It should work the same as unit
    circles. Not for paper just a peek to what is coming." Then: "Let's get started, see what falls out." After the run:
    "Great result. Exciting. Add this out session record paper of reader geometry. I knew it would work, but not so
    easily. 3d is notoriously hard. Good work." (The peek was first kept out of the paper; this ruling puts the session
    record in, §7.9.)  
59. **Which sweep lays the addresses** (Sep 26, 19:04–19:44). After the sphere demo raised it (addresses even in the
    reading or in the turn), "Proceed" to the registered test; after the results, "yes" to adding them as a note on
    Proposition 15 with the test logged in Appendix B.  
60. **The motion rerun** (Sep 26, 20:00). "proceed": taken as open item 12, the motion test rerun with its three
    repairs, registered first (B.15).  
61. **Two readers of one solid** (Sep 26, 20:25 – Sep 27, 01:22). Tom uploaded the rung editor ("here is our 3d
    application from an earlier session which was created before the insights of this paper"); "proceed" to the point
    reader in it; "what does this demo have to say about our framework?"; "proceed" to the registered test; "proceed" to
    adding it here (§7.10, B.16).  
62. **Two readers together** (Sep 27, 01:21–01:22). "whats next" → the list; "proceed" to adding §7.10 and then
    registering and running the combined-readers test (B.17).  
63. **A guided second look** (Sep 27, 01:27). "proceed" to the suggested test: a second reader sent where the first
    reader's payloads jump (B.18).  
64. **The guided look, repaired** (Sep 27, 01:36). "proceed" to the two repairs B.18 named, registered first (B.19).  
65. **The orbit unknown** (Sep 27, 02:50). "proceed" to open question 1 of the working paper *From Somewhere to
    Nowhere* (set up at 02:43 on Tom's "yes"): correspondence from the reader's own landmarks, run as item 13, registered
    first (B.20).  
66. **The frame and the signal** (Sep 27, 03:14–03:19). "serial signal is dynamic and the parallel signal is static. the
    parallel signal is much larger, but than it gets updated real time with the serial signal, but the serial signal does
    not give details, just that somthing is moving"; "ok" to adding it to §7.7 and the literature paper and registering
    the test (B.21).  
67. **The inventory; addresses only** (Sep 27, 03:51–03:56). "there is a v/h signal and a v&h signal. the v&h signal is
    orthogonal to the v/h address to it. we know there is cauchy and an a sweep from 0 to inf. i'm wondering if this a
    fairly complete inventory. if so, we should be able to build observation from only these primatives"; "yes, but i
    would only add that the reader only has addresses to the world, he does not store the world in his head" (restating
    R29 for observation). Audit in the working paper *The Inventory*.  
68. **The serial reading addresses the parallel** (Sep 27, 04:09–04:11). "I'm wondering if serial signal provides the
    address to each pixel in the parallel signal"; "proceed" to recording it as: the serial reading (v/h, and d/h in 3d)
    gives each pixel its address, and the parallel reading gives what is at it; the same division across time says which
    addresses changed; "before" lives at the address, in the instrument, not in the reader. Test under addresses only:
    B.22.  
69. **The moving reader, addresses only** (Sep 27, 04:18). "proceed" to the next piece of the observer: a moving reader
    relating its standpoints only through shared landmarks, carrying addresses (bearings) and signatures, not positions
    (B.23). Open for Tom's ruling: whether a corner's signature (its turning angle, a unitless reading) counts as part of
    its address.  
70. **Noise** (Sep 27, 04:27–04:53). "proceeed" to recording the two models (*From Somewhere to Nowhere* §6) and testing
    both observers with noise; "proceed" (04:45) to repair 3, steadying at the address; "proceed" (04:53) to finishing the
    run (B.24). Pilots and calibration unregistered, in `shapes/noise-pilot.md`.  
71. **How noise enters** (Sep 27, 05:04–05:05). "LOL. a static image does not jump around. it is static by definition.";
    "yes, they will be different in this test by definition of what the are." The parallel image of a still scene is
    static: its errors are fixed, not flickering. Jitter is change, so it belongs to the serial signal, and the instrument at
    each address filters it (it fires only past ε, R68). The two signals therefore take noise differently by definition.
    A standpoint's image carries a fixed error; the image changes only when the world or the reader moves. Applied to
    B.24 post hoc.  
72. **Solve or geometry?** (Sep 27, 05:10). "proceed" to repair 1; found already applied in B.24 (least squares over all
    shared corners), so the test registered instead asked whether distance (the conditioning of bearings-only resection)
    explains the gap (B.25).  
73. **The diagnostic** (Sep 27, 06:55). "proceed" to the rerun that records every step and corner, to find the cause of
    the steady gap (B.26).  
74. **The weak triple** (Sep 27, 07:45). "Proceed" to testing whether a reader can judge a weak three-corner step from
    its own addresses (B.27).  
75. **The reader in 3D** (Sep 27, 08:26). "1" (to carrying the addresses-only reader into 3D, testing one address more than
    exactly determined) (B.28).  
76. **Consolidation, then smooth borders** (Sep 27, 08:54). "1 then 2": the write-up *Observing with Addresses Only*,
    then curvature landmarks on smooth borders (B.29).  
77. **The two infinities** (Sep 27, 09:19). The **horizon** keeps its corpus meaning: the reading's infinity, v/h → ∞
    as h → 0, which a forward-facing reader finds at its sides. The payload's infinity, the far ahead that collapses to
    v/h → 0, is **the vanishing point**, and it sits at **home**. The two are not the same place, and neither word is
    used for the other. (Chosen from three options: keep the horizon at the sides; move it ahead; qualify both.)
    Then: "5 then 1", which leads to the assembled observer (B.30).  
78. **The hand and the rings** (Sep 27, 15:02–15:06). "I'm most interested in persuing the serial and paralell
    obserervers, one divides one doesn,t and they are connected by the corner." 15:04: "yes. the idea is that the
    serial reader is the hand and fingers, and the parallel reader is the rings." 15:06: "proceed." The serial reader
    is the hand and its fingers (the sweep and its addresses); the parallel reader is the rings (the magnitudes kept).
    Worked out in the working paper *The Hand and the Rings*.  
79. **Three sweeps: left, right and forward** (Sep 27, 18:11–18:21). "What if parallel reader is just a sweep itself."
    Then: "So three sweep, left right and forward." Read back and agreed: from a standpoint, **left** runs from home to
    the horizon on one side and **right** to the horizon on the other (the front half, two facings, two freedoms; each
    carries its own corner), and **forward** runs out along each address to the first border, which is the parallel
    reader's sweep. The parallel reader rides the serial sweeps: it sweeps **along** an address, not across. Each sweep
    ends at a named place: left and right at the horizon (R77's sides), forward at the vanishing point. On depth: "I
    don't think that old ruling is correct. This one is cleaner." **Depth is the forward sweep, the magnitude along the
    address, and belongs to the parallel reader.** Supersedes the Sep 20 ruling "the 1d signal is where depth comes from,
    it is the z" (*Degrees of Freedom* §5.19) and the assignment of depth in §7.4 as first written.
80. **g, the hangers placed** (Sep 27, 20:31–20:46). "at density = 0 unit circle, N = 0. at density = 1 full shape, N =
    1000"; "h = [0,1], v = [0,1]. relation = [0,inf) if you divide, [0,1] if you don't. [unit circle=0, shape=1]"; "i
    think g is the depth, it is the third dimesion"; then, asked whether g counts hangers or measures how far each has
    come: "yes, g =1 means all the hangers are placed. g=0 no hangers placed." **g ∈ [0, 1] is the share of the N
    hangers placed**: at 0 none, and the reader has the unit circle, addresses only; at 1 all N, the shape. Between,
    gN hangers carry their magnitudes and the rest stay on the unit circle. Confirms *Degrees of Freedom* §1 (Sep 18).
    Proposed as the depth, the third dimension; how that depth relates to R79's forward magnitude is open.
    21:34: "a corner is only for things with a horizon. g is just [0,1]. no horizon." g is kept, never divided, so it has
    no horizon and no corner (the symmetric space has no fulcrum). Withdrawn: "depth starts at the corner", and the
    ladder from the corner as a rule for g (B.42's CORNER arm measures a placement, not g's own structure).
81. **g is the reader's** (Sep 28, 04:47). Asked whether the g in the address law is the reader's (addresses laid) or the
    shape's (hangers placed): "the g is the readers, nohting to do with the world, the sahpes move through the g." g is
    a property of the reader, laid out from it (1 near, falling as 1/distance to 0 at the vanishing point, B.43); the
    world's shapes pass through it and are seen at the g where they are. So the address law with g kept in,
    gN · h²/π, is the reader's alone and nothing in the world changes it: the payload stays orthogonal to it (R47).
82. **Missiles are the reverse g** (Sep 28, 05:16, on the game *Horizon Defender*): "this is more accurate because the
    missles are the reverse g. so they wont make contact until the g of the missle and the g of the object are equal."
    A missile leaves the reader at g = 1 and runs down its address toward the vanishing point, g → 0; a piece comes the
    other way. Being on the same address (the serial reader's, left and right) is not contact; contact is the moment
    their g's are equal (the forward sweep, the parallel reader's, R79). So a hit is two conditions, one per reader:
    the same address, and the same g.
83. **The game loop is the world; reality has no game loop** (Sep 28, 11:07, ruling the open question of whose frame
    the world moves in, raised by *Two Standpoints*): "Computers have a game loop, that is the world. Each reader does
    not get their own loop. So we should be flexible the here, but realize reality does not have game loops." The
    simulation's single update of the world is the view from nowhere's machinery, not the geometry: readers only read
    it. So in demos the frame the motion is laid out in (a reader, a point no reader stands at, or no point) is a free
    choice, and no finding rests on it. What does not carry over to reality is anything the loop supplies: one global
    update, one "now" in which every reader reads the same frame, an event happening at a single tick for all.
84. **In 3d the across sweeps are one even sweep over the front half** (Sep 28, 14:27, "ok, proceed", accepting the
    proposal of v-and-h items 187–188, from *The Even Sky*). A reader in 3d space has two readings and one magnitude; its
    addresses are laid evenly over the whole front half (the 2d Cauchy, h³/2π on the bar), not as a left–right turn
    with an up–down turn laid at each. "Left–right" and "up–down" name directions in the one sweep; they are not two
    sweeps. Laid as crossed turns, the front half gets two poles and a preferred up, and the share within the corner
    (20% against 29%) and the median (v/h 2.69 against √3) belong to the layout; laid evenly, tilting the head about
    home changes nothing. Refines R79 for 3d; items 153–156 (both readings needed, crossed at each address) stand.
85. **Two roles, two lays** (Sep 29, 05:04, "3", choosing the third of three options put after v-and-h item 207). The
    even sky of R84 stays the lay a reader **reads and measures** with. The circle of circles with its pole at home
    (every great circle through home a line reader laid evenly in turn) is the lay its readings are **presented** on,
    where the Tangent Bridge's kernel presents the atoms continuously, exact at the atoms and bounded between. Stated as
    two roles, not a rival to R84.
86. **Where each rung comes from** (Sep 29, 06:54, "proceed as written", accepting §10 of *The View from Somewhere in
    3d*, gathered from v-and-h items 187–215). The world up to a projective map comes from relations between two
    readers (or one reader and a return in time); the shape up to a scale from the reader's own even sky (its turns)
    or its own g; the rotation from a reading of something far; the count of turns from a carry; the place from
    closing a loop or marks left in the world; the unit from an agreement, a thing all read called 1. Beside the
    reading, three kinds of thing: a carry, a relay (live or stored) and an agreement.
87. **The forward reading is laid in turn; the three readings are one even lay** (Sep 29, 07:03, "proceed as written",
    accepting the proposal of v-and-h items 216–217). Along each address the forward reading is laid evenly in turn,
    d = D1·tan ψ, so its corner falls at the reader's own D1; g = min(1, cot ψ) is that reading from its far end,
    clipped at the corner (R80's "no corner" holds of g itself). With the two across readings it is one even lay of
    the reader's space, the 3d Cauchy, which has no pole at the reader's own point (crossed, it has one). Refines R79–R80
    and extends R84 one reading up.
88. **Three landmarks, of two kinds** (Sep 29, ~09:06, choosing "Three, of two kinds" when put the question of
    *The Boundary* B52 with the 3d forward reading). Each reading has three marks: home (v/h = 0), the corner (v = h)
    and the horizon (v/h → ∞). Under the facing (v/h read as h/v) they are two kinds: the corner, which the facing
    leaves where it is, and home with the horizon, a pair the facing exchanges. Along the forward reading (R87) the pair
    is the reader's own point and the vanishing point, and g is the reading taken from the vanishing point's end.
89. **The unit is not geometric** (Sep 29, 09:25: "the unit is persuasive. that only comes from aggreement. it is not
    geometric."). No reading gives a unit (v-and-h items 214–215); readers have one only by agreeing to call a thing
    all of them read 1. So the unit is not a rung of the ladder: the geometry from somewhere tops out at the shape up to
    a scale (similarity), and "+ one length" is an agreement laid over it. Refines R86's last row.
    Refined 09:27: "a solo reader would have no need for a unit, because that is how you communicate with other
    readers. if you only need to communicate with yourself, a unit can just be you." A unit is for passing a length
    between readers; alone, the reader is its own unit (its D1, its body, its step), as *The Relation Space* §9 has it
    above the corner: the reader "keeps itself as the unit".
90. **The view from nowhere is the backside** (Sep 29, 09:30–09:32: "the god's eye view is needed if you need to consider
    the backside"; "yes, that is clean definition of the view from nowhere, it it is the hidden view, the blocked view,
    the backside."). A reader holds two facings; it reaches the other two by turning (later: v-and-h items 173–174) or
    through a company of readers (from elsewhere, joined by relations and a shared beat: 159–170, 213); only the view
    from nowhere holds all four at once. So the view from nowhere is defined by what no one standpoint holds: **the
    hidden view, the blocked view, the backside**. The readers' residuals (what no standpoint read; change faster than
    any reading) are exactly what it would supply.
91. **Geometry is the sweep of addresses; the magnitudes make the backside** (Sep 29, 10:42–10:43: "the big, potentially
    paradigm changing idea here is that geometry is not shapes, it is the sweep of addresses that point to a magnitude.
    says nothing about what the magnitudes are."; "yes, the magnitudes are what create the backsides and the hidden
    geometry. so they are not not irrelevent."). The addressing (the lay, its corner, its grain, the facing) is geometry
    and holds whatever the payload. The magnitudes met along the sweep are payload; they make the first border, and so
    the hidden, the blocked and the backside (R90). Shape is recovered from payloads through the addresses, as far as the
    ladder allows (R86, R89).
92. **The span is π/2 at every g; g counts hangers** (Sep 29, 13:24–13:25: "it is always PI/2 at every g."; "at g = 1,
    it simplifies away."). The relations between h and v span ∫₀^∞ ds/(1 + s²) = π/2 whatever g is. g sets how many
    hangers express the span (gN of N, spaced π/(2gN)), never the span: expressed density gN · (2/π) · ds/(1 + s²). At
    g = 1 the factor simplifies away and the classical equation remains; along the forward sweep that holds from the
    reader out to the corner (R87), and beyond it g < 1 thins the count while the span stays π/2. Breadth is extent;
    g is the share of the quantity expressed.
93. **The sweep of g is the radius of the addressing scheme** (Sep 29, 13:46–13:48: "right, but as you reduce g from 1 to 0, you create the unit sphere or unit circle. At 1, all N is included to create the addressing scheme. g is simply how much of N is being used. but its addresses, not data. And its not a specific g, its the sweep of g. you don't pick a g of 0.5 or example, it is all g between 0 and 1."; "Yes. than what ever system you are observing is overlayed onto this addressing scheme. g is never chosen, it is the sweep over the full expression of N to empty expression of N."). g is the share of N
    addresses in use: addresses, not data. It is never chosen: it is the sweep from full expression of N (g = 1) to empty
    expression (g = 0). With the turn as angle and g as radius, at radius g the span π/2 carries gN addresses (arc
    g · π/2); the sweep of g fills the unit disc (the unit ball, with two across readings), whose g = 1 rim is the unit
    circle (the unit sphere). Whatever system is observed is overlaid onto this addressing scheme.
94. **g is the Cauchy's own factor, not its scale** (Sep 29, 14:06: "its what ever the math says. yes, in the past we have characterized g as just the zoom or the level of detail. I think that is partially correct, but its actually as we discoved above, just the cauchy formula including the g."). The Cauchy with g,
    f_g(s) = g · (2/π)/(1 + s²), keeps the reading s as its coordinate and multiplies only the density. So across the
    sweep an address keeps its reading (its turn) and a lower g thins addresses in place; relations among readings, the
    cross ratio among them, hold at every g. g is the level of detail (step span/(gN)). The zoom is the Cauchy's other
    parameter, the scale γ in (2/π) · γ/(γ² + s²), which moves the median to s = γ and keeps all N: the reader radius
    of Sep 3. Two independent dials: g · (2/π) · γ/(γ² + s²).
95. **The scheme addresses any linear system, of any N** (Sep 29, 14:13: "right, this is the addressing scheme to any linear system of data, irregardless of its peridocity, or facings. the linear data could close into a circle, but that is not necessary. the system itself, can be of any size N. the addressing scheme perefectly accomodates any system N because it is from 0 to PI/2 is fixed and the number of addresses that creates of N can be infiniately densy packed."). The span, 0 to π/2, is fixed; N sets only
    the density, span/N between neighbouring addresses, and may grow without limit, the addresses packing toward the
    continuum. Periodicity and facings do not enter: the data may close into a circle or not. (Corpus, Sep 3: the lens is
    indifferent to completion except at the horizon; for data that closes, the horizon is a seam, where the data comes
    back round.)
96. **With N unknown, the addresses are laid differently** (Sep 29, 14:18: "If N is not know, things get interesting.
    seems like changes the situation, the addresses get arranged differently."; 14:20, on the write-up: "update the paper
    with this."). Without N the span cannot be divided. Addresses laid on arrival, never moved and kept in order, crowd
    toward a limit and cannot be even; the lay that keeps order and place is a fixed step in reading from home, turn
    arctan(k · step), crowding toward the horizon, which holds what has not arrived. g then stops multiplying the Cauchy
    and becomes its running total, g = (2/π) · arctan(n · step) [the shortcut, not the sweep: swept from home, g is the count of steps taken (R148)]: ½ at the corner (n · step = 1), 1 only at the horizon,
    never reached; the tail left there is ≈ (2/π)/(n · step).
97. **The unit circle and the unit sphere are addressing schemes** (Sep 29, 14:34: "seems like this captures the unit
    sphere and circle perfectly. they are just an addressing schemes that you can lay any system of any size onto
    them."). Each is the g = 1 rim of a sweep of addresses; a system is laid onto it. Notes carried from the record: the
    sphere's lay is even only nearly (S² has no group structure; Fibonacci lays for any N are near-even; crossed lays
    have poles); with N unknown the whole is never laid (R96); adjacency belongs to the system, so the system must come
    ordered (R95).
98. **The circle and the sphere are needed when the system has periodicity and facings** (Sep 29, 14:36: "they are needed
    when your system has periodicty and facings."). A linear system needs only the span 0 to π/2 (R95). A system that
    comes back round, periodic or with facings, needs the whole circle, which closes where the data does and so has no
    seam at the horizon; the sphere is the same need for facings all round. Note: periodic in two independent directions
    is the torus (circle by circle), not the sphere.
99. **The turn is another address for an array: by density, for sweeping** (Sep 29, 14:40: "0 to PI/2 is just another
    way to address values in an array. instead of breadth, it uses density and the cauchy and g. so its a bit more
    complicated to reference linear data in terms of its complexity, but it useful when you want to sweep the data, not
    just index it."). The index addresses by breadth (N cells, extent N · unit); the turn by density (span fixed, N
    sharing it, the Cauchy lay, g in use). They convert exactly and write nothing to the array. A view by turn is the
    same span at every N and g, so a sweep is one gesture at any size.
100. **The sweep is of breadth and density at once** (Sep 29, 14:41: "but your not sweeping just the breadth, but your
    sweeping its density as well."). Density enters along the sweep (the Cauchy lay: crowded at home, thin toward the
    horizon in reading) and across it (g: every address in use to none). The disc is the two together: turn for where
    along the breadth, radius g for how densely. An index sweeps breadth at one density.
101. **The Cauchy sets up the sweep of breadth and density** (Sep 29, 14:44: "thats key, the cauchy sets up the ability to
    sweep the systems breadth and density."). Foregrounded in the paper's abstract and §12 beside g's connection to the
    Cauchy.
102. **In the hand metaphor, g is how open the hand is** (Sep 29, 14:49: "the hand metaphore could benifit from how g is
    manifested. I propose g=0 is the closed hand into a fist. g=1 is the fingers fully extended."). A curled finger is
    out of use, not pointed elsewhere (R94: turns fixed); the span is the same at every opening. Still just a metaphor
    (R78, 15:10).
103. **Two degrees of freedom: the number of fingers and how far they extend** (Sep 29, 14:51: "notice that gives two
    degrees of freedom, the number of fingers and how much they extend."). N sets the division of the span and where each
    address points; g sets how much of N is expressed. The Cauchy's count carries them only as the product gN; they
    separate by which addresses are in use (N = 1,000 at g = ½ and N = 500 at g = 1 hold the same count, a quarter of the
    coarser step apart).
104. **With four or eight facings the backside is in the shape** *(withdrawn by 139)* (Sep 29, 15:14, answering whether the addressing's
    backside and the payload's are one thing: "yes, the circle and sphere are where the backside is a real thing. its
    in the actual shape, not just the backside."). With one or two facings (a reader's front) the backside is made only
    by payloads stopping the sweep. The circle and the sphere have a back half of their own: each reading v/h occurs in
    front and back, and only the facing, carried by the pair (v, h), separates them. It would remain in a transparent
    world. Refines R90–R91: the magnitudes make the blocked and hidden views, and the backside too for a reader's front.
105. **The quarter turn and the semicircle are not shapes** (Sep 29, 15:15: "the quarter turn and semi-circle are not
    closed, they are not shapes, like the circle and sphere are."). Open spans of addresses, with ends at the horizons;
    the circle and the sphere close, and closing makes a shape (corpus, Sep 3: open = still arriving or never
    completing, closed = returns to where it began). Why R104 holds: only a shape has a back half.
106. **Breadth was mislabelled: the two dimensions are relation and density** (Sep 29, 17:37: "wait, not breadth the
    relation. we've mislabled breadth. division removes the breadth or scale. so it is relation and density are our two
    dimensions, the third is just magnitude that each combinatino of breadth and density points to."). Breadth is extent
    (Sep 24), which v/h divides out. The turn addresses by relation and density; breadth returns only through the unit
    (EXTENT, R89). R100–R101's "breadth" is the relation.
107. **The headline result: three dimensions, relation, density and magnitude, not x, y, z** *(withdrawn by 125)* (Sep 29, 17:37: "yes, this
    is 3d space, its not x,y,z. it is relation,density and magnitude. that is the headline result of this paper.").
    Relation and density are addressing; magnitude is what each pair points to. Notes: "dimension" counts kinds, not
    coordinates (the relation may take two readings, a modelling choice for a finite set, Tom 17:22); density has no
    counterpart in x, y, z, the view from nowhere's coordinates, since it holds every g at once.
108. **Density is the reader's dimension, not the world's** (Sep 29, 17:44: "interesting that g is a reader dimension,
    not the worlds."). With Sep 24 ("density is created by a reader's limitation"). Magnitude is the world's; the
    relation sits between (the pair's, laid as a turn from a home).
109. **Magnitude is [0, ∞)** (Sep 29, 17:55: "Magnitude is 0 to inf"). The amount an address points to has no upper end;
    the [0, 1] of R37 is v and h as shares of their own all. Held on [0, 1] by the forward lay in turn, arctan(d/D1),
    against a unit (R87, R89).
110. **Density is [0, ∞) as well** (Sep 29, 17:56: "0 - 1 density is infinite as well"). g is a share, but the count it
    is a share of can grow without limit (R95). All three dimensions are native [0, ∞); the Cauchy's turn bounds each
    (relation: nothing needed; density: N or a step; magnitude: a unit).
111. **Not dimensional: divide, sweep, point** (Sep 29, 19:06: "x,y,z are ortogonal dimensions. relation is divided than
    sweeped of all densities, magnitude is what they point to. its not dimensional."). Corrects the word "dimensions" in
    R106–R107: x, y, z are the world's orthogonal dimensions (the view from nowhere's coordinates); observation from
    somewhere divides (v/h, scale removed), sweeps (the relation as a turn from home, across all densities) and points
    (to magnitude). Relation and density are not orthogonal axes and magnitude is not a coordinate. The ranges of
    R108–R110 stand.
112. **Three dimensions, nested rather than orthogonal** *(withdrawn by 125)* (Sep 29, 19:15: "its kind of dimensional, just not x, y, z
    orthgonally. all relations point to all densities which point to all magnitudes."; 19:18: "yes, by say the complete
    set of relations, complete set of densities and complete set possible magitudes."). Refines R111. The three are
    independent freedoms, but ordered: each is reached through the one before, and none rotates into another, where x,
    y, z are interchangeable. A chain, not a frame.
113. **The parallel reading defines the range of addresses; it takes no snapshot** (Sep 29, 19:24–19:39: "we don't
    actually take a snap shot, we just point to the magnitude"; "parallel because it already exists"; "the serial reader
    points to the full range of addresses, not the system itself. the parallel is the actaul address that point the
    full system. so to layers of inderection"; "so its still a parallel reading, but all thats needed is just define the
    range of addresses that this observation consists of"). Magnitudes stay in the system; nothing is copied. Two layers
    of indirection: serial → the range of addresses → the system. The snapshot of the simulations is a record (§9), and
    the latency weakness (ledger P2) is the record's.
114. **A formal definition of the unit circle and sphere** (Sep 29, 19:46: "our framing allows us to create a formal
    definition of the unit circle an unit sphere, not just an abstract concept."; 19:48 "yes"). Address = pair (h, v)
    in a facing, identified by relation; unit circle = all addresses over four facings (the sign patterns) at g = 1;
    disc = × density; sphere = triples, two relations, eight facings. "Unit" = scale divided out and full expression,
    not a length. Paper §2.4 (Definitions 2.1–2.4, Proposition 2.1).
115. **The three, in plain words** (Sep 29, 19:52, replacing R112's "complete set of … points to …" as awkward):
    "relations is the sweep of horizontal to vertical, densities is full shape to the unit circle, and the magnitues
    are the worlds." Paper abstract, §2.3 list and §12 reworded.
116. **Magnitudes are not swept** (Sep 29, 19:57: "the magnitues are not a sweep of possible things, they are a
    specific thing which is defined by the system."). Relations and densities are swept by the reader; the magnitude at
    each address is one value, fixed by the system, met and never chosen. R109's [0, ∞) is the range such a value may
    fall in, not a set the reader sweeps. Qualifies R112's "complete set of possible magnitudes".
117. **The Cauchy does not need to know the magnitude; the system is orthogonal to the sweep** (Sep 29, 20:00: "cauchy
    does not need to know what that thing is."; 20:01: "yes, it is clarifying. the system is orothogonal, you can lay
    any system onto the sweep geometry."). With R91 and the Sep 3 "a lens is orthogonal to the data it observes".
118. **g is the sweep, from magnitude to address; "density" is not its name** (Sep 30, 06:38: "i dont think g 'density' is the correct word, its just the sweep from pure magnitude to pure address."; 06:41,
    "yes" to the vocabulary that follows). g runs from the magnitude fully expressed (g = 1: the full shape, every
    address with its r) to pure address (g → 0: the unit circle, one representative per address, the magnitude divided
    out). "Density" now names only the factor g multiplies in the Cauchy, g · (2/π)/(1 + s²), which is how the sweep
    is laid, not what it is. To keep "sweep" for g alone, the relation is described as **the turn** from horizontal to
    vertical. The three nested dimensions read **relations, sweep, magnitudes**, walked as divide, sweep, point;
    earlier rulings' quotes keep "density" as said. Refines R93, R107, R111–R112, R115.
    *Refined the same morning* (06:45: "or more specifically, at g=1 all N is used as the divisor. g = 0, N is unused as the divisor, so its the unit circle. notice this is a divide by zero situation. I'm not sure what that means."; 06:48: "but N is not necissarily known anyways."; 06:49 "yes"). With N unknown, the general
    case, the sweep never divides by N: it is a turn of the count from home, g = (2/π) · arctan(n · step) [the shortcut, not the sweep: swept from home, g is the count of steps taken (R148)] (R96), so
    g = 0 is an ordinary point, **home: the unit circle as a scheme** (the rule for addresses, nothing laid, pure
    address), and g → 1 is **the horizon: the completed set**, every address laid and carrying its magnitude, never
    reached. The divide by zero belongs only to the known-N case, where the sweep is written as a share of N (the
    magnitude over gN) and blows up at the empty end. As for v/h, which end is home and which the horizon depends on
    what goes underneath (R2).
119. **3d is the sphere of addresses plus one relation, the magnitude over the reader's own travel** (Sep 30, 09:11:
    "it also gives you an address back to the original magnitudes. can we prove that with our framework? seems to me, that is what 3d is."; 09:12 "yes" to the proposition and this wording). Two relations, across and up, over eight facings,
    give direction, and one standpoint has all of it at once (R114, the unit sphere). Depth is not a third turn of that
    sphere: it is the relation of what an address points to, the magnitude, to the reader's own travel between two
    readings, d/|b| = sin α₁ / sin(α₁ − α₀), read from two addresses alone. It needs a second standpoint, and so
    motion: serial supplies it. The magnitude is not held, only addressed, through a v/h whose h is the reader's own
    step (with R89: the only unit is the reader's). Laid in turn it is the forward lay d = D1 · tan ψ with D1 = |b|
    (R87). The triangulation itself is classical.

120. **Three coincidences: overlap, meeting, contact** (Sep 30, 14:49: "proceed with your suggestions", on the proposal
    to name them so). Two bodies may coincide for a reader in three ways. An **overlap**: on the same address (the
    parallel reader's coincidence; it depends on where the reader stands). A **meeting**: arriving at the same moment
    (the serial reader's; it also depends on where the reader stands, since signals from different distances left at
    different times). **Contact**: the same place, which shows as both at once and holds as the reader moves: the one
    coincidence every standpoint agrees on. The reader tells contact from overlap without positions: two bodies of one
    system shown at one moment carry ticks that differ by their depth difference over the signals' speed; or their
    parallax under the reader's own travel; or their distances through the address. Collisions in *Wander* are kept
    within one system (no shared now between systems), and bounce (momentum kept), so a touch also weighs: each body's
    change of speed, over the other's, is their mass ratio (Mach).

121. **The unit circle and unit sphere are the known breadth at g = 0** (Sep 30, 21:29, on the breadth sweep: "this demo
    answers what the unit circle and unit spheres actually are. this is for known breadth. and g is [0,1] or the radius
    from 1 to the breadth."). Built on 21:03–21:20: "breadth is just like N, except that it continuous, not an index";
    one breadth per facing, known or unknown ("when known, it is the quarter circle"); "g is actaully just the radius.
    when radiius=0, than breadth = 1. when the radius = breadth, the breadth is fully expressed"; two facings the
    semicircle, four the circle, eight the sphere; "when known, the breath is the same for each facing." So with the
    breadth B known, r = 1 + g(B − 1): g = 0, radius 1, is the unit circle (eight facings, the unit sphere); g = 1,
    radius B, is the breadth fully expressed. The turn points to the place, x = r · turn/(π/2). Written up in *Serial,
    Parallel and Nowhere* §2.4.

122. **Infinite breadth and infinite density are connected through the address** (Sep 30, 21:37: "notice that at each
    address, from radius = 1 to radius = breadth, it stays connected to the same magnitude, but between the unit circle
    and the full expression of magitude, it is the ratio of between 0 and 1. but the key point is that the addres is
    always the same for each magnitude. and because circles can be infinitely dense, this supports. infinite breadth.
    this how infinite breadth and infinite density are connected."). The turn at an address does not change with g, so
    each magnitude keeps one address whatever B is; the unit circle's addresses can be without limit, so a breadth
    without limit is still addressed. Against ruling 4's dropping of "infinite density" the demo stands (21:39: "that is incorrect,
    this demo is correct.").

123. **Density is the bridge; the reader is the unit circle** (Sep 30, 21:42: "the view from somewhere is discreteness, the
    view from nowhere is continuity, and the bridge between them is density."; 21:47: "the bridge is density. somewhere is discrete, nowhere is continuous. no density means the unit circle, full density is the world. reader than is the unit circle.").
    No density is the unit circle (g = 0, radius 1, addresses only); full density is the world (g = 1, every magnitude
    fully expressed). The word "density" returns to the sweep (cf. 118). Superseded in wording by 124.

124. **Drop "density": g is the ratio between the reader and the world** (Sep 30, 21:56: "yes, density is the culprit
    here. the world is always fully expressed, regardless of who is observing it. the world is breadth. the reader than
    must be the unit circle. between the unit circle and the world is how much of the world and how much of the reader.
    0=reader. 1=world. between them is just parts of both."; 21:57: "yes, lets try to drop density if that possible. its
    just ratio between the reader and the world and its reflected by the ratio 0 to 1."). The word had named three
    things: the spacing of addresses, g, and the continuum's having no gaps. They are now the spacing, the ratio, and
    continuity. In this paper's body and earlier rulings, "density" as g is to be read as this ratio; where it is the
    spacing or the Cauchy's probability density, it is that. Refines 34 and 108 ("density is the reader's"): g is the
    share between the reader and the world, not the reader's alone.

125. **Observation is not dimensional, and not three things** (Sep 30, 22:02: "lets not call observation dimensional,
    that is another confusing word. its something different, it needs a new word so not to confuse the situation.";
    22:05: "lets not even say observation is three things, we have been trying to make observation three dimensional to
    fit in the 3d box. Its just what it is, consisting of the various things."). Withdraws the "three dimensions" of 107
    and 112 and any count: observation consists of relations, addresses, g (the ratio between the reader and the world)
    and magnitudes, each reached through the one before; x, y and z stay the view from nowhere's dimensions.

126. **The uniform unit circle is for known breadth, resolved geometry; in a sense the view from nowhere** (Oct 1, 03:52:
    "the uniform unit circle is for situations where the breadth is known and can be divided evenly across the address space. it is for static resolved geometry where every address points to a known magnitude. in a sense, it is the view from nowhere."). The even lay needs the breadth known and divided evenly; every address points to a known magnitude. A reader
    from somewhere lays its addresses from its own home by the Cauchy (§5.2). How this sits with 123–124 ("the reader is
    the unit circle") is open.

127. **The reader is not the unit circle** (Oct 1, 04:05: "the reader is not the unit circle, the uniform unit circle is read evenly across the entire address space, no point of view, it is the view from nowhwere. the unit circle is where v and h can be represented in terms of each other symetrically. it is read uniformly with no situated observer."). The unit circle is where v and h are represented in
    terms of each other symmetrically, read uniformly with no situated observer: the view from nowhere (as in 28).
    Withdraws "the reader is the unit circle" in 123 and 124.

128. **The situated reader is the same geometry, the breadth unknown** (Oct 1, 04:10: "the situated reader is the same geomeitry, with one difference, the breadth is unknown."). Breadth known: divided
    evenly, the uniform unit circle, the view from nowhere. Breadth unknown: laid from a home by a step, the Cauchy, a
    horizon (R96): the view from somewhere.

129. **The situated reader is the fisheye, not the unit circle** (Oct 1, 04:17: "the view from somewhere or the situated reader is the fish eye, not the unit circle.").

130. **The fisheye's two sides** (Oct 1, 04:25: "seems to me the front side is lesss then he corner and the back side is
    greater then the corner."; 04:37: "the back side is logrithmic").

131. **The view from nowhere has no home, no horizon, no corner, and no division** (Oct 1, 04:51–04:56: "there is no home or horizon in the breadth sweep," "no corner either." "no need to divide v from h in the view from no where, it just h relative to v and v relaive to h.").
    v and h are each read relative to the other, symmetrically; v/h, home, the horizon and the corner are the situated
    reader's.

132. **In the fisheye, h is known and v is unknown** (Oct 1, 05:06: "the fisheye, h is known, and v is unkown, expresed in terms of h."). v is expressed in terms of h, v = (v/h) · h:
    the reason the situated reader divides, where the view from nowhere (131) does not.

133. **The fisheye needs no v** (Oct 1, 05:08: "so we do't even need a v in the fisheye situation."; 05:09 "yes"). The situated reader holds h and a count of h's: home
    none, the corner one, the front less than one, the back more (logarithmic), the horizon beyond any count.

134. **The unit circle: the breadths of h and v known and equal, normalized to 1** (Oct 1, 05:23: "in the unit circle the breadth of v and h are known and equal, so we can nomralize them to 1."). Against 132–133:
    in the unit circle both are known; in the fisheye only h.

135. **The fisheye cannot be normalized** (Oct 1, 05:25: "you cant noramlize the fisheye, it is asymetric. h breadth known, v breadth unknown."). Normalizing needs both breadths known and equal (134).

136. **Both h and v inform; v has no baseline** (Oct 1, 05:27: "but we are still getting information about both h and v, just that we have no baseline about v."). Refines 133: the fisheye needs no v baseline, not no
    v.

137. **Four situations: circle, all other shapes, fisheye, impossible** (Oct 1, 05:33–05:43: "I think there are three situations to consider, v=h. v!=h and h known, v not known." "1 is symetric, 2 is asymetric, 3 is fisheye, 4 is impossible." "right, fisheye is neither symetric nor asymentric, one side of the relation is unknown."
    "1. circle, 2. all other shapes, 3. fisheye. 4. impossible." "in the fisheye, v exists, its just not known."). By what is known of the breadths: 1, known and the same every way (symmetric, the circle); 2, known
    but varying (asymmetric, all other shapes); 3, h's known and v's not (the fisheye: neither, one side unknown; v exists,
    its breadth is not known); 4, neither known (impossible, the pathological case). Supersedes 135's word "asymetric".

138. **The Cauchy is what happens in situation 3** (Oct 1, 05:45–05:47: "so we could give v a place holder value, but it would be of type 2 with a place holderfor unknown v." "so cauchy is what happens in situation 3."). With a placeholder for v's
    breadth, situation 3 is situation 2 with a placeholder: the Cauchy's scale γ.

139. **Shapes are views from nowhere; only the fisheye is a view from somewhere** (Oct 1, 05:50–05:53: "there is no frontside or backside in situation 1 or 2 because there is no situated place to observe them."
    "it goes. shapes are views from nowhere. only fisheye is view from somewhere."). No front or back in situations 1 and 2. Withdraws 104.

140. **g in situations 1 and 2** (Oct 1, 05:57: "notice that situation 1 does not have a g, because its symetric. situation 2 has a g, the ratio of situation 1 relative to situation 2."). r(θ) = (1 − g) · 1 + g · B(θ): 0 the circle, 1 the shape.
    Refines 124 ("0=reader. 1=world") after 127.

141. **g in situation 3** (Oct 1, 05:59: "yes, situation 3 has g, but its more complicated becuase v is unknown but exists."). A real g toward an unseen end, read only as a count in the reader's own
    step (R96); where it crosses ½ moves with the placeholder (138).

142. **The Cauchy creates situation 1; the corner measures the breadth ratio** (Oct 1, 06:06–06:37: "the cauchy creates an even turn, so even if the the breadh of v and h are different, you will get a unit circle as result of the eveness of the turn. its interesting that cauchy creates situation 1. so you could do the cauchy on sistuation 2 to simulate the situation of situation 3." "this gives a new perspective on the corner. if its an elipse, there will be 2x times values after the corner than before it." "yes. lets test this to get an exact statement about the corner.").
    Tested on ellipses (`corner.py`): laid evenly in share, a shape with v's breadth b times h's has its middle at v/h = b
    and (2/π)·arctan(1/b) before the corner; the corner is the middle only when b = 1. Holds for that lay, not for an even
    lay in length or in direction. Written up in *Serial, Parallel and Nowhere* §2.4.

143. **Situation 3 in terms of 1, 2 and 4** (Oct 1, 06:39–06:40: "so we know can now explain situation 3 in terms of situations 1,2 and 4."). The world is a shape of situation 2; v's breadth
    is unknown as in situation 4, on one side only; the reader assumes situation 1 (γ = 1, the corner as the middle); the
    gap between the corner and the middle of its arrivals is the breadth ratio (142).

144. **How shapes open into the fisheye** (Oct 1, 06:57: "so the fisheye just un-closes the shape, with the situated reader at the midpoint of that unclosure. however, shapes wll unclose differently, the unclosed circle will have a different corner position and long tail than the unclosed ellipse for example."). Tested on the library (`unclose.py`): laid in direction
    every shape opens as the circle; laid along its outline each opens its own way, by corner share, middle, head and
    tail; shapes the same with h and v swapped keep the corner at the middle and differ only at the ends.
145. **What the opened line holds** (Oct 1, 08:31: "So the cauchy is just the unrolled scale free version of the shape with the  addresses pointing back to the rolled up scaled version of the shape."; 08:33 "yes"). Dividing v by h cancels a size
    common to both, so the opened line holds ratios only; each place on it is an address back to a point on the closed,
    sized shape. Refinements: the Cauchy is the circle's opening (other shapes laid along the outline open their own way,
    144); only a common size cancels, not a stretch of one side; one value of v/h has up to four addresses, one per
    facing, unless the facing is kept.
146. **What a view from somewhere is** (Oct 1, 11:56: "the fisheye is view from somewhere. i want to be precise what
    that means exactly."; 12:05: "1) yes there could be other situations for V.    the four situations are not exhaustive.   2) h is the known side by definition."). A reading in which h's breadth is known and v's is not; h is the known side
    by definition, and v arrives only as a count of h's. Division, home, corner and horizon, the two sides, the forced
    Cauchy, no normalising and g toward an unseen end all follow from that. The four situations are not exhaustive:
    there could be other situations for v.
147. **Assuming v's breadth clarifies, it does not simplify** (Oct 1, 12:18–12:23: "situation 2 and situation 3 are the same, just that v is not known. i wonder if it would be helpful to just assume v is known in situation 3, say 2x h. how do you use cauchy in situation 2?" / "its claryifing, not simplyfing."). In
    situation 2 the readings on the circle's even turn are a Cauchy with scale b; for b = 2 the reading is the b = 1
    reading slid up one binary rung, every share unchanged. Assuming v = 2h in situation 3 shows the unknown is one
    number, a rung offset; the pattern is the same for every b, and b = 1 puts its middle at the corner.
148. **Arctan is not the sweep** (Oct 1, 12:25: "g is applicable in both situation 2 and 3."; 12:28: "arctan is not the sweep, it is engineering solution to bypass the sweep.    sweeps must be swept, starting from home.    arctan subverts that, and is just an engineeer convience."). Sweeps are swept, step by
    step from home; arctan gives where a step would land without sweeping, and its 2/π divides by the whole turn out to
    the horizon, which a situated reader never reaches. So g in situation 3 is the count of steps swept from home toward
    an unknown end; (2/π)·arctan(n·step) (96, 141) is the shortcut, marked wherever it appears. g applies in situations 2
    and 3: between two known ends in 2, swept out from home in 3. Extends 18 and 24. Refined (12:32): "arctan can be useful, it makes sweeps act more like indexes.   but it obfiscates the actual geomtery, and should be avoided if possible because of that." Arctan makes a
    sweep act like an index; it hides the geometry, so it is avoided where the sweep can be swept.
149. **The working horizon** (Oct 1, 12:35: "although the breadth of V is not known, you do know the corner.   so you could sweep to the corner."; 12:38: "thats clean if true, and i think it is.    it is a  working horizon, the one we see as situated readers, the sweep to the corner is the one we experience."; 12:39: "yes.     the backside then must be past the corner."). In situation 3
    the corner is known (v reaches one h) though v's breadth is not. The sweep from home to the corner is the one a
    situated reader experiences: two known ends, so proportional, n/C, no arctan. The front side is the working horizon, the corner its
    edge (corrected 12:43: "the working horizon is the frontside."); the
    back side is past it, counted by doublings (logarithmic), and maps onto the front by the swap. "The horizon" alone
    keeps its meaning (77): v/h → ∞, never reached. Refined (12:40): "the corner then must define the frontside." Home starts
    the sweep; the corner bounds it, giving the front side its extent and its proportions; the back side is what lies past.
150. **Situation 3 is a hybrid** (Oct 1, 12:41: "so situation 3 is a hybrid,   its like sitatuation 2 before the corner but adds a backside after the corner."). Up to the corner it behaves like situation 2: a span
    with two known ends, home and the corner, read in plain proportion. Past the corner it adds a back side with no end,
    counted by doublings. g splits there: a position between known ends on the front, a count toward an unseen end on
    the back. Situation 2 itself still has no home, corner or sides (139).
151. **A fifth situation: v approximately known** (Oct 1, 12:54: "things started to click for me when i realized that there actually was four distinct situations or even a fifth one where V is approximately known."; 12:55: "yes, add the fifth situation, for completeness."). h's breadth
    known, v's known approximately. v's breadth enters as one number, the Cauchy's scale, a whole-rung offset (147):
    situation 2 knows it, situation 3 does not, situation 5 knows it within bounds. Otherwise as situation 3: the corner
    known, the front side the working horizon, the back side past it. The bounds form is Claude's reading.
*Renamed on Sep 25:* "the view from everywhere" in rulings 3–4 above is now **the view from nowhere** (R28). *Rulings
3's writer and 10's inside/outside wording* are kept as recorded; the paper uses only their operational content.

## Appendix B. Measurements and kill logs

Moved here from the body (Sep 25, step 4 of the plan) so the body reads as definitions, propositions and
proofs. Each section below says where it came from; the body keeps a one-line pointer.

### B.1 Three even sweeps: the measurements (§3.3)

Measured: swept evenly, the turn gives the Cauchy (D = 0.0025), the shift a uniform reading (0.0025), the stretch a
uniform log reading (0.0024). Moved to 1,000 other standpoints (another focus and zoom), each keeps its kind and its
number of fixed places every time; the places themselves move, so they are home and the horizon only from the
reader's own standpoint. Of 10,000 moves picked at random, 6,550 are turns and 3,450 stretches; none is a shift, which
is the boundary between the two and has to be chosen on purpose.

### B.2 The review's objection, kept for the record (§3.2)

⚠ *Kept for the record (the review's objection, now answered on the writer's side).* **These two layouts are model
choices, not yet derived.** There are infinitely many maps from a floored place to an address:
i ↦ f(i, N) for a known count, i ↦ g(i) for an unknown one (log(1 + i), i², a doubling ladder…). What forces the two
chosen here is the open question the next draft must answer. The series has partial answers, and they do not yet agree:
- for a known count, the even share is "the only one a reader can build from N alone" [corpus: *Degrees of Freedom*
  §5.15k]; that is a forcing argument from poverty, not from symmetry;
- for an unknown count, *The Unit Rule* §5 proves that any discrete company of rescalings is the powers of one
  generator, so a scale-free ladder is forced to be geometric, gⁱ; and *The Observation Atom* §1.6c finds that
  aperture-invariance forces log spacing "uniquely", while calling the choice between criteria "a fork". The fixed-step
  freedom, sᵢ = i/u, is a count layout (absolute addresses, a drawing that keeps growing), not a rescaling ladder. Which of the two a
  reader with unknown N is forced to, if either, is not settled here.

### B.3 Proposition 3: the interleave test (§3.4)

*The test* [`interleave.mjs`, predictions registered first in `interleave-predictions.md`; all held]. Seven shapes
(circle, ellipse, square, triangle, star, limaçon, blob), each drawn at N = 360 directions and at scales 10⁻³, 1 and 10³.
The pure reading and motion streams are unchanged by the scale (≤ 7e-16), uniform through the lens (KS D = 2/N for
every shape), balanced at the corner (0.5000) and closed (lap product 1). With the magnitudes interleaved, every shape's
stream changes with the scale, loses uniformity (D = 0.50 at 10∓³), leaves the corner (0.75 / 0.25) and fails to close.
One case shows why leg 2 leans on uniformity: the unit circle at scale 1 interleaves 1s into 1s, so it still closes and
the reader cannot tell a size from a step, but its magnitudes pile onto the corner and D rises from 0.0056 to 0.25.

### B.4 The worked example: kills (§3.6)

*Kills recorded*: "bit-identical addresses" was the wrong bound (they agree to rounding); "the coarse places are every
eighth fine place" is false for cell centres and true for cells.

### B.5 Which moves keep the Cauchy: kills (§4.0)

*Kills recorded* (`moves-predictions.md`). The first run predicted that every warp would visibly break the Cauchy. It
failed for the sin 2θ warps (they are first-order Möbius, which the prediction missed) and for a sin θ warp (not a
move of the reading at all: p and −p have the same reading, and sin θ moves them oppositely). The corrected predictions
were registered before the second run.

### B.6 Proposition 7a: the test (§6.2)

*The test* (200,000 pushes per case). Five size laws (constant, uniform, exponential, log-normal σ = 3, and Pareto ½,
which has no mean), each at scales 10⁻⁶, 1, 10⁶: all standard Cauchy (KS D = 0.0024, the noise floor), and the readings
identical across all fifteen cases to 4e-16. Three moves (stretch 2:1, shear, stretch-and-turn): each lands on its
predicted member with no fitting (D ≤ 0.003).

### B.7 Algorithmic pointing: kills (§2.4)

- *Kills logged*: the first run measured the corner and found one step (the design, not the cost); "least step below
  ε" rewarded lucky crossings; a bound on where two nearby places' sign sequences part does not hold.

### B.8 The stretch: a rounding tie (§3.3)

At g = 10, δ = 1e-6 and 1e-12, the steps toward home came out one more than the steps toward the horizon, because 1/10
applied six times is 1.0000000000000004e-6, a hair above δ, while 10 applied six times is exactly 1e6. With exact
arithmetic the two sides agree (6 and 12). Logged as a kill of the run, not of the claim.

### B.10 The plug-in: one registered bound missed (§10.0)

`plugin.mjs`, `plugin-predictions.md` (registered before the run). P2–P5 and V1–V4 held or showed. **P1 missed for the
clock**: registered ≤ 1e-15, measured 6.46e-15, peaking at places 60–63 where 1 − β² cancels under the root. Landmarks
and cells unchanged. Corrected bound: to rounding when the system hands over (v, h); to rounding amplified by
cancellation when it computes h from v. Also loose: P4 said every other system's motion differs from the circle's, but
×10⁻⁶ and ×10⁶ are the circle, and theirs is flat, as it should be.

### B.11 Motion: the test and its kills (§7.7)

Registered before the run in `shapes/motion-predictions.md`; script `shapes/motion.mjs`; diagnostics
`shapes/motion-posthoc.mjs` (post hoc, labelled). Frame A: each of the 73 single-loop library shapes at 512 leaves on
the even clock. Frame B: the same polygon moved about frame A's census centre (scale 1.08, rotation 0.1 rad, translation
5% of size at 30°) and resampled on the drifted clock u + 0.6 sin u. 1024 addresses. Recovery from addresses:
translation from the census centre of B seeded from A's; rotation from the slide that best aligns the two log-payload
profiles; scale from the median serial reading. Baseline from arrivals: Procrustes on leaf k against leaf k.

| | registered | measured | verdict |
|---|---|---|---|
| M0 | arrivals exact with no re-timing (sanity) | 4·10⁻¹⁴ | held |
| M1 | translation < 10⁻³ of size on ≥ 95% | 63/73 = 86% (median 2.9·10⁻⁵) | **killed** |
| M2 | scale < 10⁻³ on ≥ 95% of non-degenerate | 66/72 = 92% (median 8.1·10⁻⁶) | **killed** (same shapes as M1) |
| M3 | rotation < 0.5° mod 2π/n on ≥ 95% of readable | 67/71 = 94.4% (median 5·10⁻⁴°) | **killed** |
| M4 | arrivals wrong under re-timing: translation ≥ 90%, scale ≥ 80%, rotation ≥ 80% | 73/73, 73/73, 18/73 | translation, scale held; **rotation killed** |
| M5 | no motion: 99% of addresses within 10⁻³ of the corner on ≥ 95% | 49/72 = 68% | **killed** |
| M6 | fixed standpoint, translation: first wave within 20° on ≥ 80% of star shapes | 46/57 = 80.7% (median 2.0°) | held, at the bar |
| M7 | fixed standpoint, translation: jumps on ≥ 80% of non-star, ≤ 10% of star | 12/15 = 80%; 11/57 = 19% | non-star held at the bar; **star killed** |

Degenerate: the rose (its census sits on its own crossing, as known from §7.6 item 5). Flat: the circle.

*Kills, explained afterwards.*
- **M1, M2.** All ten failures have jumping first crossings: ell, arrow2, chevron, bolt, bottle, rose (not star-shaped)
  and graze8, graze21, graze68, graze200 (grazing). On graze21/68/200 the census leaves the moved standpoint by about half
  the size even when seeded exactly there, with or without re-timing: 256 fixed directions are not rotation-equivariant
  where rays graze. On ell, chevron, bolt and bottle frame A's census is itself a fixed point only to 1.5·10⁻³–9·10⁻³
  when recast at 1024 directions. arrow2 fails only under re-timing (chord cuts). The rose is recovered (2.4·10⁻⁴) when
  seeded at its true moved centre: its failure was the seed's basin (§7.6 item 1).
- **M3.** The rotation reading was right; the registered symmetry detector was wrong. The four misses (dodecagon, burst,
  gear, snowflake) are off by exactly 30.00° or 60.00°, consistent with a 12- or 6-fold alias, but the detector returned
  4 or 2: 512 leaves do not cut a 12-fold outline 12-fold, and for a nearly round profile a tolerance of 5·10⁻³ of its
  spread is too tight. Taken modulo 30° or 60° for those four, all 71 readable shapes are within 0.5°.
- **M4 rotation.** The re-timing chosen is odd about leaf 0, so on shapes mirror-symmetric about leaf 0 its effect on
  Procrustes' rotation cancels: 0/48 of those exceeded 0.5°, against 18/25 of the rest. A test design fault, not a
  finding.
- **M5.** Median departure from the corner is exactly 0; the 99th percentile is 2.6·10⁻⁴ (median over shapes) but reaches
  1.1 on the worst, where re-timing cuts a sharp corner differently. The corner is stillness to the chord error.
- **M7 star.** Of the 11 star-shaped shapes that jumped, five were no longer star-shaped from the fixed standpoint once
  translated (graze21/68/200, clover, snowflake); six stayed star-shaped but have edges nearly along the rays (pie,
  astroid, gear, tree, spoon, knife), so a 5% move swings the grazing hit by more than 20% of size.

### B.12 Recovery by a circling reader: the test (§7.8)

Registered before the run in `shapes/orbit-predictions.md`; script `shapes/orbit.mjs`; diagnostics
`shapes/orbit-posthoc.mjs` (post hoc, labelled). Each of the 73 shapes at 512 leaves; 64 stops on a circle of radius
3·size about the census centre, each facing it, 1024 directions across ±1.05·asin(1/3). Parallel: first-border distance
per direction, placed by the known stop; coverage is the arc length of segments some ray hit first. Serial: the two
outermost directions that meet the shape at each stop; the recovered set is the intersection of the wedges. 25 shapes
convex, 48 not; 16 not star-shaped from the census centre.

| | registered | measured | verdict |
|---|---|---|---|
| P1 | parallel coverage ≥ 99.5% on every convex shape | 25/25, all 100% | held |
| P2 | sanity: recovered points on the outline to 10⁻⁹ of size | 1.5·10⁻¹⁵ | held (sanity only; the reader reads the polygon it is scored on) |
| P3 | serial wedge area within 1% of the hull on every shape | 47/73; −0.3% to +4.9% | **killed** |
| P4 | a parallel point > 1% of size inside the hull on every non-convex shape | 48/48 (crescent 2.0%, the shallowest) | held |
| P5 | the orbit hides less than the census centre on all 16 non-star shapes | 16/16 | held |
| P6 | hidden stretches on the hull < 1% of the outline, every shape | 73/73, all 0.00% | held |

Hidden from the orbit: spiro 30.5%, fork 3.3%, rose 3.1%; every other shape 0%. P4's operational form (a point deep
inside the hull, rather than an enclosed area) was fixed before the run, because a point set's area is not defined on the
self-crossing shapes.

*P3, explained afterwards.* All 26 failures over-estimate and have hulls with long straight sides (the shape's own, or
bridges across concavities: astroid, cloud, snowflake, spiro, rose). A straight side is a support line only from a stop on
its own line. Wedge excess against stops, rechecked on eleven shapes:

| shape | 64 | 128 | 256 | 512 |
|---|---|---|---|---|
| square | 4.49% | 0.17% | 0.17% | 0.17% |
| diamond | 3.44% | 1.06% | 0.52% | 0.06% |
| triangle | 1.72% | 1.70% | 0.45% | −0.41% |
| banner | 4.94% | 2.34% | 0.11% | 0.11% |
| check | 3.05% | 1.30% | 0.09% | −0.27% |
| star5 | 1.19% | 0.69% | 0.21% | −0.01% |
| circle | −0.16% | −0.21% | −0.22% | −0.23% |

The negative floor is the direction grid: the outermost direction that meets the shape lies just inside the true edge,
so each wedge is slightly narrow.

### B.13 The sphere: a first probe (§7.9)

Registered before the run in `sphere/sphere-predictions.md`; script `sphere/sphere.py` (output `sphere-run.txt`); post
hoc `sphere/sphere-posthoc.py`. The first run crashed on a 33 GB array in the convex-hull test; the fix (chunking)
changed nothing else and the rerun used the same seed. Shapes are distance functions read by sphere tracing (a hit below
1e-5). Stops at 3·size facing the origin. Coverage: a reference point (about 6000, area-even) counts if some stop's ray
toward it first meets the surface there. Visual hull: 128 × 128 silhouettes sampled evenly in the reading (a pinhole
image), voxels on a 72³ grid; compared with the convex hull and the solid on the same grid.

| | registered | measured | verdict |
|---|---|---|---|
| Q1 | hemisphere read serially, and Gaussian ÷ Gaussian, are the 2d Cauchy | KS 0.0026/0.0027 (crit 0.0036); 0.0021/0.0008 (crit 0.0026) | held |
| Q2 | 5 linear moves give the predicted elliptical 2d Cauchy | KS at most 0.0023 (crit 0.0026) | held |
| S1 | the three planar sweeps: index 2, still at ±d, ±v, ±h | exactly | held |
| S2 | the diagonal sweep: index 2, still at the corner and its opposite | 3, miscounted at the opposite corner | **killed** (apparatus) |
| S3 | 20 random smooth sweeps: index 2 | 20/20 | held |
| R1 | sphere of stops: ≥ 99% on six shapes; shell 73.5 ± 2%; drilled < 99% | 100% on all six; 74.0%; 99.5% | held except **drilled** |
| R2 | equatorial ring on the ball: 94.3 ± 0.7% | 94.42% | held |
| R3 | visual hull within 3% of convex hull on seven shapes; torus < 90% | ellipsoid 0.972, capsule 0.976, the rest within; torus 0.710 | **killed on two**; torus held |
| R4 | parallel sees > 5% inside the hull on bowl, torus, drilled; < 1% on convex | 0.71, 0.28, 0.50; 0.000 | held |

*Kills, explained afterwards.* **S2:** the cube-sphere grid has a node exactly at (1,1,1)/√3, so the still point sat on
three cells' corners. On a grid rotated off it: index 2, still at (0.569, 0.583, 0.580) and its opposite, the corner to
the grid's resolution. **R1 drilled:** 22 of 6000 points never faced, all in the hole, 0.52–0.80 below the top face; the
hole is a small share of the area, so the loss stayed under 1%. I mispredicted the share, not the effect. **R3:** the
visual hull should contain the solid but came out 2–3% smaller on curved shapes: partly covered silhouette pixels read as
outside carve true voxels. At 256 pixels the shave roughly halves (ball 0.980 → 0.990, ellipsoid 0.970 → 0.987, capsule
0.975 → 0.986). The pixel floor again, as in the plane's small negative floor (B.12).

### B.14 Which even sweep lays the addresses (§7.5)

Registered before the run in `shapes/measure3-predictions.md`; script `shapes/measure3.mjs` (output `measure3-run.txt`);
post hoc `shapes/measure3-posthoc.mjs` (the same code at 16384 addresses, and the largest moves). The 73 library shapes
at 512 leaves; standpoint the census centre; four facings, the reading a on [−1, 1]; 4096 addresses per sweep: turn
a = tan α (α even on [−π/4, π/4]), shift a even, stretch |a| = e^s (s even on [ln 10⁻³, 0], both signs).

| | registered | measured (4096) | verdict | post hoc (16384) |
|---|---|---|---|---|
| Q1 | median moves > 0.5% of size on ≥ 80%, shift and stretch vs turn | 19/73; 26/73 | **killed** | 18/73; 26/73 |
| Q2 | largest and smallest payload agree within 2·10⁻³ on ≥ 95% | 64/73 | **killed** | 67/73 |
| Q3 | crossings of a fixed level equal under all three on ≥ 95% | 72/73 | held | 73/73 |
| Q4 | each sweep's median pace-free (< 5·10⁻³) on ≥ 90% | 73/73 (largest 2.1·10⁻³) | held | 73/73 |

*Kills, explained afterwards.* **Q1**: typical move 5·10⁻⁵ of size, but xmark 16% (shift) and 33% (stretch), astroid
31%, star8 22%, hinge4 19%, gear 15%, cross 13%, burst 13%, heart 11%; the medians that did not move sit on landmarks
the sweeps share (§7.5). **Q2**: sharp extremes (vertices, cusps, the chevron's jump) sampled at different densities;
the largest miss fell from 4.0·10⁻² to 1.1·10⁻² of size and the failures from 9 to 2 (heart, astroid) at four times the
addresses. Resolution, not the measure.

### B.15 Motion rerun with its three repairs (§7.7, open item 12)

Registered before the run in `shapes/motion2-predictions.md`; script `shapes/motion2.mjs` (output `motion2-run.txt`);
post hoc `shapes/motion2-posthoc.mjs`. Repairs: a symmetry order found by recasting the profile turned by 2π/n (to
2·10⁻³ of size, absolute); a re-timing u + 0.45 sin(u + 1) + 0.2 sin(2u + 0.3), odd about no leaf; a census along 1024
directions, not 256.

| | registered | measured | verdict |
|---|---|---|---|
| R1 | translation < 10⁻³ on ≥ 90%; ≥ 3 of 4 grazing pass; ≤ 3 of 5 non-star jumpers pass | 64/73; 0/4; 2/5 | **killed** (total, grazing); jumpers held |
| R2 | scale passes on the same shapes as R1, ± 1 | 66/72; two differ | **killed** by one |
| R3 | rotation < 0.5° mod 2π/n on ≥ 97%; dodecagon 12, hexagon ≥ 6 | 70/71; 12; 6 | held |
| R4 | arrivals wrong: rotation > 0.5° ≥ 80%; translation, scale > 1% ≥ 90% | 73/73 each | held |

*Explained afterwards.* The rotation and re-timing kills of B.11 were the test's faults. The grazing kills were not the
grid: on graze21, graze68 and graze200 the census centre is a fixed point but a saddle, nudged 10⁻³ of size along x it
settles 0.44–0.51 of size away, nudged along y it returns; a translation with a component along x tips the tracker into
one of two resting places either side (§7.6 item 1). graze8's centre is stable and its miss is probably chord error (not checked); on ell the census has no
exact fixed point (one step moves 3.4·10⁻⁴), a jumping first border. Tally of the ten B.11 tracking failures: two pass under the
new re-timing (arrow2, bottle), three a saddle (graze21/68/200), three a jumping first border (ell, chevron, bolt), one probably chord
error (graze8), one the rose's seed basin; none the grid. One new near miss with the new re-timing: fork, 1.5·10⁻³.

### B.16 Two readers of one solid (§7.10)

Registered before the run in `app3d/readers-predictions.md`; script `app3d/readers.py` (output `readers-run.txt`); post hoc
`app3d/readers-posthoc.py`. Axis reader: 64 heights × 128 angles, horizontal rays from the axis (payload 0 where the axis
point is outside). Point reader: six facings of 37 × 37 addresses laid evenly in the readings, from the solid's centre.
Reconstruction: nearer than the interpolated payload along one's own address (linear in height and angle; bilinear in
the readings). Compared with the true solid on 128³ voxels over [−0.75, 0.75]³; an error voxel is *horizontal* where the
true surface's normal has |n_y| > 0.9.

| solid | axis error | horizontal share | axis addresses on caps | point error | horizontal share | point addresses on caps |
|---|---|---|---|---|---|---|
| box | 1.37% | 85.5% | 0.0% | 0.04% | 0.0% | 12.9% |
| cylinder | 1.31% | 86.3% | 0.0% | 0.04% | 0.0% | 10.6% |
| cone | 1.94% | 88.6% | 0.0% | 0.22% | 0.0% | 7.4% |
| sphere | 0.08% | 76.5% | 9.5% | 0.01% | 33.3% | 5.9% |
| ellipsoid | 0.33% | 48.7% | 15.1% | 100% (bug); 0.08% fixed | — | 5.9% |
| pawn | 4.18% | 82.4% | 2.5% | 36.6% | 73.8% | 1.6% |
| mushroom | 4.29% | 92.6% | 5.6% | 55.2% | 49.6% | 7.8% |
| tilted box | 0.78% | 0% | 0% | 0.42% | 0% | 0% |

| | registered | verdict |
|---|---|---|
| P1 | axis error > 50% horizontal on box, cylinder, cone, pawn, mushroom | held (82–93%) |
| P2 | point error < 30% horizontal on the same five | **killed** (0% on the first three; 74%, 50% on pawn, mushroom) |
| P3 | point < axis on box, cylinder | held |
| P4 | axis < point on pawn, mushroom | held |
| P5 | both < 1% on sphere, ellipsoid | **killed** (apparatus) |
| P6 | axis < 2%, point > 10% of addresses on caps, box and cylinder | held |

*Kills, explained afterwards.* **P5**: the ellipsoid's approximate distance function is exactly 0 at its centre, so the
standpoint read as outside and every address stopped at once; with that point fixed the point reader's error is 0.08%
(axis 0.33%). **P2**: on pawn and mushroom the point reader's error is whole hidden volumes, not a skin (inferred from its
size and shape, not checked voxel by voxel); classing a voxel deep inside them by the gradient there means nothing.

### B.17 Two readers together; does a reader know its blind spot? (§7.10)

Registered before the run in `app3d/readers2-predictions.md`; script `app3d/readers2.py` (output `readers2-run.txt`).
Same solids, readers and voxels as B.16, with the ellipsoid's centre fixed. Union of the two reconstructions; a voxel's
error is *flagged* by a reader if the addresses its value came from, or their neighbours out to two either side,
contain a jump (factor above 1.3, or 0 against non-zero).

| solid | axis | point | union | axis error flagged | point error flagged |
|---|---|---|---|---|---|
| box | 1.37% | 0.04% | 0.14% | 100% | 0% |
| cylinder | 1.31% | 0.04% | 0.20% | 100% | 0% |
| cone | 1.94% | 0.22% | 0.40% | 100% | 76% |
| sphere | 0.08% | 0.01% | 0.00% | 82% | 0% |
| ellipsoid | 0.33% | 0.08% | 0.12% | 68% | 0% |
| pawn | 4.18% | 36.57% | 4.08% | 97% | 92% |
| mushroom | 4.29% | 55.16% | 4.06% | 97% | 9% |
| tilted box | 0.78% | 0.42% | 0.42% | 70% | 0% |

| | registered | verdict |
|---|---|---|
| C1 | union ≤ better reader + 0.5%, all eight | held (worst +0.18%) |
| C2 | union below both on pawn, mushroom | held, narrowly |
| C3 | box, cylinder, cone: union < axis / 1.5 and > point | held |
| C4a | ≥ 70% of axis error flagged on the five cap shapes | held (97–100%) |
| C4b | < 30% of point error flagged on pawn, mushroom | **killed** on the pawn (92%); held on the mushroom (9%) |

*Explained afterwards.* The pawn's hidden ball lies in a thin band of directions right beside the jump where its neck
gives way; the mushroom's hidden cap spans a wide band, mostly far from any jump. The flag's reach (two addresses) is
what decides.

### B.18 A second reader sent where the first one's payloads jump (§7.10)

Registered before the run in `app3d/guided-predictions.md`; script `app3d/guided.py` (output `guided-run.txt`); post hoc
`app3d/guided-posthoc.py`. Reader A at the centre; its jumps (neighbours on a facing differing by more than 1.3, or 0
against non-zero); at each, the point halfway along the longer side; reader B at their mean; union. Baseline: ten random
second readers inside the solid.

| solid | A alone | jumps | A ∪ guided B | random second reader: mean, best |
|---|---|---|---|---|
| box, cylinder, cone, sphere, ellipsoid, tilted box | 0.01–0.42% | 0 | (none sent) | 0.02–0.41%, 0.01–0.35% |
| pawn | 36.57% | 160 | 35.36% (B at y = 0.028) | 18.40%, 1.90% |
| mushroom | 55.16% | 156 | 2.18% (B at y = 0.157) | 12.67%, 0.92% |

| | registered | verdict |
|---|---|---|
| G1 | no jumps on sphere, ellipsoid, box, cylinder, tilted box | held |
| G2 | guided standpoint inside, pawn and mushroom | held |
| G3 | mushroom: guided < 10% and < random mean | held |
| G4 | pawn: guided < 5% and < random mean | **killed** |
| G5 | guided < axis reader, pawn and mushroom | held on the mushroom; **killed** on the pawn |

*Explained afterwards.* The pawn's jumps form two groups (above and below the neck) whose mean lands in the neck. One
reader per group (2-means on the jump points): pawn 30.0%, mushroom 3.6%; the lower reader still sits in the neck, since
halfway along the longer side of a downward jump falls short of the base.

### B.19 The guided second look, repaired (§7.10)

Registered before the run in `app3d/guided2-predictions.md`; script `app3d/guided2.py` (output `guided2-run.txt`). Jumps as in
B.18; edge points (where the shorter address stopped) grouped by single linkage at 0.06; per jump, the point a quarter of
the way past the edge along the longer address; one reader per group at the mean (or, if outside, the nearest member);
union. Baseline: A plus the same number of random interior readers, ten trials.

| solid | A alone | groups | readers | union | same-count random |
|---|---|---|---|---|---|
| six with no backside | 0.01–0.42% | 0 | none | — | — |
| pawn | 36.57% | 2 | y = 0.153 (116 jumps), y = −0.340 (44), both inside | 1.56% | 11.98% |
| mushroom | 55.16% | 1 | y = 0.152 (156 jumps), inside | 2.41% | 7.31% |

H1 (pawn: two groups, inside, < 5%, < random, < axis), H2 (mushroom < 5%, < random), H3 (no groups on the six): all held.

### B.20 The orbit unknown: steps from the reader's own landmarks (item 13) [R65]

Registered before the run in `shapes/orbit-unknown-predictions.md`; script `shapes/orbit-unknown.mjs` (output
`orbit-unknown-run.txt`, verdicts `orbit-unknown-verdicts.txt`); apparatus census `shapes/landmark-census.mjs`; post hoc
`shapes/orbit-unknown-posthoc.mjs` (output `orbit-unknown-posthoc-p2l.txt`).

**Apparatus.** As §7.8, with the orbit unknown. Each stop's reading is kept in the reader's own frame.
- *Landmarks:* corners, found as the meeting of two adjacent straight runs along the sweep with a turn above 10°. A
  corner is a jump in the serial reading along the sweep, where a backside edge is a jump in the payload. Each corner's
  signature is its unitless turning angle.
- *Steps:* order-preserving pairs of landmarks, then inliers and least squares. Equal-best candidates with different
  steps are flagged ambiguous. No prior on the size of the step is used.
- *Baseline, registered:* point-to-point ICP, 50 iterations, started at no motion.

| | registered | verdict |
|---|---|---|
| U1 | asymmetric steps with two shared landmarks exact | held: 1,098/1,098 |
| U2 | orbit < 10⁻³·size on asymmetric shapes with all steps found | held: 3/3 (to 10⁻¹³), but only 3 of 36 had all steps |
| U3 | wrong steps only by symmetry, and flagged | held: 8 wrong, all the octagon's 45°, all flagged |
| U4 | closure flags every wrong orbit | **killed**: octagon's ±45° errors cancel, closure 2·10⁻¹⁵ |
| U5 | landmarks beat ICP where they work | held (3/3) |
| U6 | ICP recovers ≥ half the smooth shapes | **killed**: 2/11 |

Steps found: 1,922 of 4,672 (smooth 0, symmetric 54%, asymmetric 48%). Orbits recovered: 12 of 73, to 10⁻¹³·size or
better. No wrong step went unflagged.

*Post hoc (labelled).* The registered baseline was weak in form. Point-to-line ICP (200 iterations, started at no
motion) recovers 44 of 73 orbits to 10⁻⁵–10⁻⁴·size, including 8 of 11 smooth shapes. On 11 of the 12 shapes the
landmarks recovered, it is 10⁸–10¹⁰ times less precise; on the twelfth, xmark, it fails (2·10⁻²). Both methods fail on
flat sides seen face-on.

**Reading.**
- *Classical ICP reaches further*: 44 orbits against 12, given its small-step start.
- *Landmarks are exact where they work, and never silently wrong.* The precision advantage is a noise-free one and will
  shrink with noise.
- *Correspondence is recoverable from a reader's own readings where the shape offers corners.* Where it offers only
  curvature, or a flat side face-on, it is not, by this method.

### B.21 The frame and the signal (§7.7) [R66]

Registered before the run in `shapes/frame-signal-predictions.md`; script `shapes/frame-signal.mjs` (output
`frame-signal-run.txt`); post hoc `shapes/frame-signal-posthoc.mjs`.

**Setup.** One reader, standing still outside each of the 73 shapes, reads a parallel frame of 1024 addresses once.
The shape then turns 0.25° and shifts 0.001·size per frame, for 200 frames.
- *Serial events:* an address sends its ratio when the reading now against its last sent value leaves the corner by more
  than ε, and the held frame is multiplied by it.
- *Refreshes:* where a ray goes from hitting a border to missing, or back (home or the horizon), the address gets a fresh
  parallel look.

| | registered | verdict |
|---|---|---|
| K0, K1 | still control silent; held frame within ε (sanity) | held |
| K2 | the signal < 25% of full re-reads at ε = 0.02, < 60% at ε = 0.005 | held: median 3.2%, max 8.2%; median 12.3%, max 29.5% |
| K3 | refreshes only at a hit/miss boundary | held: 99.99% |
| K4 | large per-frame ratios only at payload jumps | **killed**: 45 of 4,098 elsewhere |
| K5 | refreshes < 5% of the signal | held: 3.5% |

*K4, post hoc (labelled).* 44 of the 45 are steep but continuous borders turning toward grazing (neighbouring payloads
differing by 1.001–1.298), which slide about six addresses in one frame. A large ratio in time marks a jump or a
grazing border.

**Reading.** A frame of magnitudes, read once, was kept current to within 2% for 200 frames by a serial signal costing a
median of 3% of re-reading. The update broke only at home and the horizon, and there the frame was refreshed.

### B.22 Addresses only: the reader tracks where it cannot see (§7.7) [R67, R68]

Registered before the run in `shapes/addresses-only-predictions.md`; script `shapes/addresses-only.mjs` (output
`addresses-only-run.txt`). The scene is B.21's.
- *The instrument:* each address keeps its own last sent value and fires its address when the payload leaves the
  corner by more than ε = 0.02, or goes from hit to miss or back.
- *The reader:* holds only addresses. These are the fired addresses and a list of landmark pairs (jumps above 1.3, and
  silhouette edges).
- *The rule:* it looks at the world only at both ends of each pair a fired address touches, and keeps no payload.

| | registered | verdict |
|---|---|---|
| L1 | the landmark list stays right (≥ 99%) | held: 99.996% recall and precision; 2 wrong of 26,049 |
| L2 | looks < 10% per frame on every shape | **killed**: 57/73; median 6.7%, max 16.8% (each fired address costs itself and its neighbours) |
| L3 | the list stays small (≤ 40 pairs) | held: never more than 4 |
| L4 | errors only near the threshold | held: 2/2 |

**Reading.** With no payload held anywhere but at the addresses themselves, a reader kept an exact account of where it
cannot see, through 200 frames of motion, looking at a median 6.7% of its addresses per frame.

### B.23 The moving reader, addresses only (item 13) [R69]

Registered before the run in `shapes/moving-reader-predictions.md`; script `shapes/moving-reader.mjs` (output
`moving-reader-run.txt`). B.20's orbit, with nothing given.
- *What crosses a move:* only each corner's bearing (its address along the sweep) and its signature (turning angle).
  No position or distance crosses.
- *Relating the standpoints:* at the new stop the reader looks again and relates the two by **resection**, finding where
  the old standpoint must have stood for its three held bearings to point at three corners it sees now. So three shared
  corners are needed, not two.

| | registered | verdict |
|---|---|---|
| A1 | ≥ 99% of asymmetric found steps exact | held: 711/713 (the other 2 flagged) |
| A2 | no wrong step unflagged | held: 0 of 12 |
| A3 | found steps between 800 and B.20's 1,922 | held: 1,321 |
| A4 | ≥ 6 orbits < 10⁻⁶·size | held: 6 (burst, flower, spiro, gear, snowflake, fork; 6·10⁻¹² to 2·10⁻⁹) |

*Post hoc (labelled).*
- Ambiguity under addresses only comes from the triple as well as the shape: two of the wrong steps are on asymmetric
  shapes (hinge7, clover).
- On the dodecagon, closure caught four flagged wrong steps (off 4.3), unlike B.20's octagon.
- Carrying addresses instead of positions lost six orbits (nonagon, decagon, dodecagon, star6, star8, xmark).

**Reading.** Holding no payloads costs one more shared corner per step. Where three are shared, a reader relates its
standpoints exactly from where things were and what they looked like, and says when it cannot.

### B.24 The two observers with noise (item 13) [R70]

Registered before the run in `shapes/noise-predictions.md`, after four unregistered pilots on four shapes
(`shapes/noise-pilot.md`), which are excluded from the run. Script `shapes/noisy-reader.mjs` (outputs
`noise-run-*.json`). 69 shapes, B.20's orbit.
- *Noise:* relative range noise σ = 10⁻⁵, 10⁻⁴, 10⁻³ on every look.
- *Steadying:* each address averages F = 1 or 16 of its own looks.
- *Corners:* split-and-merge.
- *Tolerances:* calibrated in pilot 4.
- *The two models:* addresses only (bearings and signatures, resection) and positions carried (Procrustes).

| | registered | verdict |
|---|---|---|
| V1 | 16 looks cut the median error to 0.1–0.5× | **killed** for addresses only (0.087: better than predicted); held for positions (0.19) |
| V2 | addresses only > 3× positions' median error | held in all six conditions (4.8–15×) |
| V3 | unflagged wrong ≤ 2% at small noise | **killed**: addresses 6.2% and 10.3%, positions 0.4% and 2.4% |
| V4 | no orbit < 10⁻²·size at σ = 10⁻³ | held (neither model) |
| V5 | ≥ 3 orbits < 10⁻³·size at σ = 10⁻⁵ | **killed**: addresses 0, positions 1 |

*Reinterpreted under R71 (post hoc, labelled).* B.24 gave every look fresh jitter, bypassing the instrument, so a
still image flickered, which by R71 it cannot.
- *The F = 1 conditions stand.* One look per stop made each stop's image static with a fixed error, and the image
  changed only when the reader moved.
- *The F = 16 conditions assumed flicker.* Averaging 16 independent jitters is the instrument settling before it holds,
  not a repair, so V1 and the F = 16 cells say little about the framework.
- *Repair 3 is dropped.*

**Reading.**
- With noise, addresses only is the more fragile model: 5–15 times the error, and silently wrong on a few per cent of
  steps where carried positions almost never are.
- Averaging at the address helps it more than √F.
- At real-sensor noise (10⁻³), corner-based observation fails in both models.

### B.25 Is addresses only fragile because of the solve or the geometry? [R72]

Registered before the run in `shapes/distance-predictions.md`. Repair 1 (solving over every shared corner) was already in
B.24, so this test varies the standpoint distance instead: D = 1.5, 3, 6 sizes, with the view framing the shape,
σ = 10⁻⁵ and 10⁻⁴, F = 1 (static images, R71), B.24's code and seed. ρ = the median step error of addresses only over
that of positions carried.

| | registered | verdict |
|---|---|---|
| W1 | closer narrows the gap | held at 10⁻⁴ (12.9 against 15.2); **killed** at 10⁻⁵ (8.3 against 6.6) |
| W2 | farther widens it | held at 10⁻⁴ (21.3 against 15.2); **killed** at 10⁻⁵ (6.0 against 6.6) |
| W3 | the gap stays (ρ > 1) | held: 6.0–21.3 |

**Reading.**
- At small noise the gap is about 6–8× whatever the distance, so conditioning along the line of sight is not its main
  cause. At larger noise, distance does widen it.
- The steady ~6× gap is unexplained. The candidates are three-corner steps (with no refinement), bearings taken from
  where noisy lines meet, and signature mismatches. Per-step records are needed.
- The D = 3 rows reproduce B.24.

### B.26 What causes the gap: a diagnostic [R73]

Registered before the run in `shapes/diag-predictions.md`. B.25's apparatus at D = 3, σ = 10⁻⁵ and 10⁻⁴, with every step
and corner recorded. The scorer labels each corner by its true world corner. The step counts reproduce B.24.

| | registered | verdict |
|---|---|---|
| D1 | 3-corner steps ≥ 2× worse than 4+ | held: 23× and 14× |
| D2 | a corner's bearing carries no extra error | held: its sideways error is 0.64–0.66 of the position error |
| D3 | wrong correspondences rare (≤ 2%) and behind half the wrong steps | first half held (1.2%); **killed** second half (30%) |
| D4 | a gap remains with 4+ corners | held: 3.1× and 5.7× |

**Reading.**
- The gap is mostly the three-corner resection, which has no redundancy: 113 of the 149 wrong steps at σ = 10⁻⁵ had
  exactly three corners.
- Bearings are not the problem, and wrong correspondences are minor.
- Requiring four shared corners leaves a gap of about 3×: the price of solving for distance instead of carrying it.

### B.27 Can a reader tell a weak three-corner step from its own addresses? [R74]

Registered before the run in `shapes/triple-predictions.md`. B.26's apparatus, with two reader-side measures per step:
the bearing spread, and the strength (the smallest eigenvalue of JᵀJ at the solution). A three-corner step is flagged
*weak* below the lower quartile of strength.

| | registered | verdict |
|---|---|---|
| Q1 | wide-spread triples far better at the median | held: 0.13× |
| Q2, Q4 | the flag catches ≥ 60% of wrong three-corner steps | **killed**: 27% and 31%, about chance |
| Q3 | dropping weak steps leaves ≤ 2% unflagged wrong | **killed**: 4.4% (while keeping 91%) |

**Reading.**
- Geometry explains the typical three-corner error, but not the gross failures. Those are mostly mismatches (59 of
  113), which three bearings fit exactly.
- A three-corner solve cannot check itself, however its geometry is judged. The fourth corner's value is the bearing left
  over to reveal a misfit (post hoc, labelled).

### B.28 The addresses-only reader in 3D (§7.9, open item 15) [R75]

Registered before the run in `threed/pose3d-predictions.md`. A shakeout amendment, recorded before the run, solved each
step both ways, because every step shared 7 or more landmarks.
- *Scenes:* 20, each of three random convex polyhedra, with the vertices as landmarks.
- *Path:* 64 stops on a rising and falling circle; every second step used (640).
- *What crosses a move:* bearings only (unit directions).
- *Solving:* the pose from a random three of the shared landmarks, and from all of them, by least squares from 32 broad
  starts, keeping the distinct solutions.

| | registered | verdict |
|---|---|---|
| T1 | three landmarks ambiguous without noise; all landmarks not | held: 639/640 have 2–4 exact solutions; 0/640 with all |
| T2 | all landmarks exact without noise | held: 640/640 to 10⁻¹⁴ |
| T3 | three landmarks less precise at σ = 10⁻⁴ | held but uninformative: only 2 single-solution three-landmark steps |
| T4 | all landmarks reliable at σ = 10⁻⁴ | held: 0/640 wrong by > 2° |

**Reading.** In 3D, three shared landmarks fix a step exactly but ambiguously (the classical perspective-three-point
problem), so a reader needs a fourth before it can trust a step, even before noise. With four or more, every step was
single, exact without noise, and never more than 2° off at σ = 10⁻⁴. Post hoc: a reader that picks a root anyway is wrong
on 23% of three-landmark steps at σ = 10⁻⁴; one that reports its ambiguity is never silently wrong here.

### B.29 Curvature landmarks on smooth borders (item 13) [R76]

Registered before the run in `shapes/curvature-predictions.md`, amended before the run after a shakeout showed resampling
ripple and fingerprinting.
- *Landmarks:* significant peaks of vertex turn (the strict maximum over 15 vertices each side, 1% above their mean).
- *The reader:* B.23's addresses-only reader, with a signature tolerance of 0.5°.

| | registered | verdict |
|---|---|---|
| S1 | the circle has none | **killed**: all 64 stops (its 160-point source polygon peaks) |
| S2 | the 12 others have landmarks at ≥ 50% of stops | **killed**: 10 of 12 |
| S3 | ≥ 30% of smooth-shape steps found | **killed**: 2 of 768 |
| S4 | found steps exact or flagged | held, on 2 steps |
| S5 | no unflagged wrong step | **killed**: 4, all on the circle, all three-landmark steps |

**Reading.**
- Curvature peaks exist, but only 1–3 are in view, too few for resection, so smooth borders stay out of reach for the
  addresses-only reader.
- The circle's silent errors repeat B.27: three landmarks fit a wrong triple exactly.

### B.30 The assembled observer (*The Inventory* §5) [R77]

Registered before the run in `shapes/assembled-predictions.md`, after seven unregistered pilot changes on the four pilot
shapes, all listed there. Script `shapes/assembled.mjs`, frozen as `assembled.registered.mjs`; outputs
`assembled-run-*.txt`.

**The reader.** It is given only a starting spot and holds:
- home's corners (bearings and signatures);
- the current held corners;
- its own chain of relations.

It chooses every act from its own look:
- centre the hits, keep its range, step left by a stride;
- the actuator errs, unseen by the reader.

It relates standpoints by resection, under either rule:
- rule 4: at least four shared corners;
- rule 3: at least three.

When it loses its landmarks, it backs up or backs away. It tries home after 300° of turning, and its own chain vetoes any
closure it disagrees with. Ties are broken either not at all (strict) or by its own command (act). Eight conditions:
σ ∈ {0, 10⁻⁵} × rule × mode, on 69 shapes.

| | registered | verdict |
|---|---|---|
| G1 | no wrong step at σ = 0 (rule 3: ≤ 0.5%) | held for rule 4 (0 of 286); **killed** for rule 3 (0.93%) |
| G2 | σ = 10⁻⁵: rule 4 ≤ 1% wrong | **killed**: 4.3%; rule 3 11.4% |
| G3 | the corner supply decides closure | held: 4 of 4 with supply 1, 0 of 60 below 0.5 |
| G4 | smooth shapes fail honestly | held: no step, no closure |
| G5 | no silent false closure | held: 0 of 25 |
| G6 | the act adds ≥ 3 symmetric closures | **killed**: no tie arose |
| G7 | ≥ 95% of unseen arcs marked by a jump | **killed**: 8 of 18, one shape |
| G8 | sees what a fixed orbit sees | held |
| G9 | its closure measures its drift | held (ρ = 1.00), nearly by construction |

**Reading.**
- **The answer is no, not with corners alone.** Assembled with nothing given, the observer closed its loop on 4 of 69
  shapes. Those were the four that show four corners from everywhere (burst, flower, gear, snowflake), exact to 10⁻¹²
  at σ = 0. Most shapes never show four corners at once (median supply 0), and 56 runs could not take a single related
  step.
- **Where it went round, it was right.** No wrong step at σ = 0 under rule 4, and no false closure in any condition.
- **Symmetry was handled by the loop, not the act** (post hoc). The chain vetoed 2 false closures, and symmetric shapes
  closed. B.23 had closed none.
- **Four corners do not check a step under noise** (post hoc). At 10⁻⁵ the 12 wrong steps were weak solves on two
  shapes (nonagon, cloud) whose loops never closed. A spare corner catches a wrong match. A weak solve needs the loop.
- **Supply is the binding constraint.** The six primitives and addresses only are enough to observe a shape exactly when
  the world offers the reader enough landmarks. Corners are not enough landmarks.

### B.31 The landmark supply census [R77]

Registered before the run in `shapes/supply-predictions.md`, piloted on the four pilot shapes only. Script
`shapes/supply.mjs`, frozen as `supply.registered.mjs`.
- *The looks:* B.24's orbit and B.30's field, σ = 0 and 10⁻⁵.
- *Four kinds of landmark, from the reader's own look:* corners (C), silhouette ends (S, the near side of a jump or miss),
  far ends (F), curvature peaks (K).
- *Supply:* the fraction of stops with at least 4 landmarks shared, as fixed points (within 0.01 size), with the next stop.

| | registered | verdict |
|---|---|---|
| P1 | corners alone scarce | held: median 0.00, 4 shapes ≥ 0.9 |
| P2 | S fixed where there are corners | **killed**: 55% (shapes mixing curves and corners); smooth half held |
| P3 | far ends slide | held: 0% persist |
| P4 | S lifts the supply (median ≥ 0.3, ≥ 20 shapes ≥ 0.9) | **killed**: median 0.00, 7 shapes |
| P5–P7 | smooth stay dry; noise changes little; F and K add little | held |

**Reading.**
- Silhouette ends are fixed points only where the border has a corner there. They lift the regular polygons of six or
  more sides and the spiky shapes, and nothing else.
- The typical view shares **two** fixed points with the next (post hoc: median shared per stop ≤ 3 on 55 of 69 shapes).
  A single plane shape seen from one side rarely offers the four that B.30's rule needs, whatever the point detector.
- Step 2 (the observer rerun) was conditioned on P4 and does not run.
- The candidates left: edges as landmarks, scenes of several shapes, a second reader.

### B.32 Edges as landmarks [R77]

Registered before the run in `shapes/edges-predictions.md`, piloted on the four pilot shapes only. Script
`shapes/edges.mjs`, frozen as `edges.registered.mjs`.

**The claim tested.** Under addresses only, an edge is worth one address: its direction is a reading (the slope v/h in
the reader's frame), and its offset is payload, not held. So a shared edge fixes the turn between standpoints and never
the position. B.31's apparatus, plus edges (straight pieces of the look, at least 8 addresses long) shared as world
lines.

| | registered | verdict |
|---|---|---|
| E1 | edges fixed where the border is straight | held: 92.8% |
| E2 | curves do not pass as edges | **killed**: the library's "smooth" shapes are 98–240-gons with facets of 6–14 addresses |
| E3 | ≥ 12 shapes with checked supply ≥ 0.9 | **killed**: 11 |
| E4 | the median shape still short of checked steps | held: 0.13 |
| E5 | exact steps become common | held: median 0.69 |
| E6 | smooth shapes stay dry | held: 0.00 on all, despite 6–34 shared edges per stop |
| E7 | noise changes little | **killed**: 0.13 → 0.39, partly curve chords at the looser tolerance |

**Reading.**
- *Edges without points place nothing.* On the smooth shapes, dozens of shared edges gave no checked step, as the claim
  says.
- *The cost of addresses only, counted* (post hoc). With positions carried, the same looks give a median supply of 1.00
  (59 shapes, an upper count: parallel lines do not fix a position). With addresses only, 0.13 (11 shapes). The
  difference is exactly the offsets the reader may not keep.
- *What edges buy.* Exact steps on most shapes (median 0.69), checked steps on few.
- *The counting rule* (post hoc, labelled, 27 Sep; *The Price of Not Storing* §2). Under R67 a shared feature fixes only
  what its held reading carries: a corner's bearing, one of a plane step's three unknowns (two with its range
  carried); an edge's direction, one, and it is the turn (two with its offset carried). The refusal costs one unknown
  per shared feature, which is why edges without points place nothing and why the checked supply falls from up to
  1.00 to 0.13.

### B.33 Scenes of several shapes [R77]

Registered before the run in `shapes/scenes-predictions.md`, piloted on scenes of the four pilot shapes only. Script
`shapes/scenes.mjs`, frozen as `scenes.registered.mjs`.
- *The scenes:* K shapes at once (K = 1, 2, 3, 5, 8, 40 scenes each, drawn from the 69), plus a smooth arm (five smooth
  shapes).
- *The reader:* circles each scene 2 sizes beyond its edge, with B.31's instrument and B.32's landmarks (points and
  edges), σ = 0.

| K | 1 | 2 | 3 | 5 | 8 | smooth, 5 |
|---|---|---|---|---|---|---|
| median checked supply | 0.04 | 0.60 | 0.77 | 0.81 | 0.78 | 0.00 |
| median exact supply | 0.49 | 0.84 | 0.91 | 0.91 | 0.92 | 0.03 |

| | registered | verdict |
|---|---|---|
| S1 | K = 1 reproduces B.32 | held |
| S2 | checked ≥ 0.5 at K = 3 and ≥ 0.9 at K = 8 | **killed**: levels off at about 0.8 |
| S3 | never falls with K | **killed**: 0.81 → 0.78 |
| S4 | points alone ≥ 0.5 at K = 5 | held: 0.61 |
| S5 | smooth scenes stay dry | held: 0.00 |
| S6 | exact ≥ 0.9 at every K ≥ 2 | **killed** at K = 2 (0.84) |

**Reading.**
- A world supplies what one shape cannot. Going from one shape to two lifts the checked supply fifteenfold, and from
  three shapes on, exact steps are available at 91–92% of stops and checked steps at about 80%.
- Only corners count. Smooth scenes stay at 0.00. Post hoc, the share of cornered shapes predicts a scene's supply
  (Spearman 0.45–0.67), which sets the level-off near 0.8.
- The growing orbit radius is not separated from this.
- *A caution raised and withdrawn (the B.34 pilot, `shapes/assembled-scenes-pilot.md` §4–5).* I suspected that
  counting shared points by world position, across kinds, overstated what an addresses-only reader can match. The pilot
  measured cross-kind matches at 0–3%, and B.34 measures it on the 69.

### B.34 The usable supply in scenes [R77]

Registered before the run in `shapes/usable-predictions.md`, after an observer pilot in scenes that got lost
(`shapes/assembled-scenes-pilot.md`, never registered). Script `shapes/usable.mjs`. Three layers per consecutive pair
of B.33's orbit stops, on B.33's scenes:
- **position:** B.33's count;
- **signature:** the same kind and a matching signature;
- **solver:** the observer's own step solver relates the stops and is right.

| K | pos4 | sig4 | solve4 | solve3 | scenes solved at all 64 stops |
|---|---|---|---|---|---|
| 1 | 0.00 | 0.00 | 0.02 | 0.38 | 4/40 |
| 3 | 0.52 | 0.48 | 0.69 | 0.77 | 0/40 |
| 5 | 0.60 | 0.61 | 0.73 | 0.75 | 0/40 |

| | registered | verdict |
|---|---|---|
| U1 | cross-kind matches rare | held: 1.6–2.6% |
| U2 | signature ≈ position | held |
| U3 | solver ≥ 0.8 at K = 5, wrong ≤ 1% | **killed**: 0.75; wrong 1.1% (rule 4), 2.4% (rule 3) |
| U4 | some scenes solved at every stop | **killed**: none of 40 |
| U5 | one shape stays dry | held |

**Reading.**
- Counting by world position did not mislead: the reader can match what the census counted.
- What stops an observer in scenes is that its own solver relates only about three steps in four, and a loop needs
  every one.
- Post hoc: the solver also "finds" more than the fixed supply, and is wrong on 1–2% of steps at σ = 0. That points at
  sliding silhouette ends passing within the looser tolerance.
- The observer run in scenes (planned as B.34) was not built.

### B.35 A tighter silhouette tolerance [R77]

Registered before the run in `shapes/tols-predictions.md`. B.34's census at K = 3 and 5, with the silhouette-end bearing
tolerance at 1.5 (B.34), 0.5 and 0.2 address spacings, and a corners-only arm.

| tolerance | 1.5 | 0.5 | 0.2 | corners only |
|---|---|---|---|---|
| K = 5 median solve4 | 0.73 | 0.61 | 0.49 | 0.17 |
| wrong four-point steps | 1.25% | 1.17% | 1.34% | 0.32% |

| | registered | verdict |
|---|---|---|
| T1 | tightening removes the wrong steps | **killed** |
| T2 | corners alone never wrong at four | **killed**: 0.32% |
| T3–T6 | tightening costs supply; corners alone are scarce; no loop closes | held |

**Reading.**
- Sliding silhouette ends are not the cause of the solver's wrong steps. Tightening only costs supply.
- Post hoc: the corners-only wrong steps have turn errors of −87°, +84°, −120° and +24°. Three are near the symmetry
  angles of shapes in view. The likely mechanism is that the view's edge cuts off the true match's fourth pair while a
  rotated copy keeps four.
- The reader's own act, a commanded step of a few degrees, would reject such solutions: a veto rather than B.30's
  tie-break.

### B.36 The reader's own move as a check [R77]

Registered before the run in `shapes/act-predictions.md`. B.34's census at K = 3 and 5, with the reader's efference
copy (the true step with B.30's actuator error) used either as a **veto** on the solver's answer or as a **filter** on
its candidates, never to set the pose.

| arm | none (B.34) | veto | filter | corners only | corners only + veto |
|---|---|---|---|---|---|
| K = 5 solve4 | 0.73 | 0.73 | 0.74 | 0.17 | 0.17 |
| wrong, rule 4 | 1.25% | 0.42% | 0.44% | 0.32% | **0.00%** |
| wrong, rule 3 | 2.57% | 0.67% | 1.15% | 3.48% | **0.00%** |

| | registered | verdict |
|---|---|---|
| A1 | veto, rule 4 ≤ 0.1% | **killed**: 0.42% |
| A2 | at no cost | held |
| A3 | filter as good, ≤ 0.1% wrong | **killed**: 0.44% |
| A4–A6 | three-point improves; corners + veto never wrong; still no loop | held |

**Reading.**
- The act refuses the gross mismatches (the rotated copies of B.35) and costs no supply.
- With corners alone it leaves nothing wrong: 0 of 2,844 steps.
- What remains with silhouette ends lies inside the act's bound (2–5°), and is plausibly their half-address location.
- Post hoc, three checks now stand, each catching what the others miss:
  - the spare address catches a wrong match;
  - the loop catches drift and false closure;
  - the act catches a mismatch the landmarks cannot tell apart.

### B.37 Step size [R77]

Registered before the run in `shapes/steps-predictions.md`. B.36's veto arm at 64, 128 and 256 stops per loop, at K = 3
and 5.

| stops | 64 | 128 | 256 |
|---|---|---|---|
| K = 5 median solve4 | 0.73 | 0.91 | 0.96 |
| K = 5 median longest gap | 22.5° | 5.6° | 2.8° |
| wrong, rule 4 | 0.42% | 0.01% | 0.01% |
| K = 5 scenes related at every stop | 0/40 | 0/40 | 1/40 |

| | registered | verdict |
|---|---|---|
| Z0, Z1, Z3 | reproduction; smaller steps help; gaps shrink | held |
| Z2 | ≥ 10 of 40 closable at 256 | **killed**: 1 |
| Z4 | wrong ≤ 0.5% everywhere | **killed** at 64 stops, rule 3, by a registration error (the threshold sat below B.36's known 0.67%); held at 128 and 256 |

**Reading.**
- The solver's shortfall in scenes is step size, not blind stretches. Smaller steps lift per-step success to 0.96, cut
  the longest gap eightfold, and cut wrong steps fortyfold.
- What still breaks a loop is a gap of one to three steps: post hoc, 35 of 40 scenes at 256 stops.
- Bridging such a gap is a 2.8° step, which the solver relates 91% of the time at that size. An observer taking fine
  steps with bridging is the next test.

### B.38 The observer in scenes: fine steps with bridging [R77]

Registered before the run in `shapes/loops-predictions.md`, after a pilot that added a closure bound growing as
√(steps/64) and split the scoring of false matches from drift. B.34's fixed-path observer, carried round B.33's scenes
in 256 stops, with the act's veto (B.36), bridging up to 4 stops, and its chain's veto on closure. K = 3 and 5, rules 4
and 3.

| | K = 3 r4 | K = 3 r3 | K = 5 r4 | K = 5 r3 |
|---|---|---|---|---|
| closed | 3/40 | 4/40 | 2/40 | 6/40 |
| wrong steps | 0 | 1 | 0 | 0 |
| false match at closure | 0 | 1 | 1 | 1 |
| right closures vetoed | 0 | 23 | 30 | 15 |

| | registered | verdict |
|---|---|---|
| L1 | ≥ 50% / 40% of loops close | **killed**: 6 and 4 of 40 |
| L2 | no false match | **killed**: 3 |
| L3 | steps stay right | held: 1 wrong in 14,729 |
| L4 | drift ≤ 2° | held: 1.16° |
| L5 | ≤ 5 right closures vetoed | **killed**: 68 |

**Reading.**
- *The steps are right; continuity fails.* The reader's individual steps are now trustworthy.
- *Bridging does not carry it across the dips.* Lost runs die about a quarter of the way round. Post hoc: B.37's argument that the gaps were
  bridgeable was wrong. The likely reason, not yet measured, is that B.37 counted consecutive steps, while bridging
  relates a staler view across the dip.
- *At this length the loop's check fails both ways.* Honest drift (median 0.15 size) is as large as a wrong match's
  error, so a single chain-versus-direct comparison vetoed 68 right closures and passed 3 wrong ones.

### B.39 How relating success falls with the span of a bridge [R77]

Registered before the run in `shapes/bridge-predictions.md`. B.37's census at 256 stops (the act's veto, rule 3),
relating each stop s to s + k for k = 1 … 5, on B.33's scenes at K = 3 and 5.

| | registered | verdict |
|---|---|---|
| B1 | span k behaves like 256/k stops | held: 0.96, 0.92, 0.75 against 0.96, 0.93, 0.75 |
| B2 | bridges carry at most half the failed steps | held: 41% |
| B3 | failures cluster | held: 6.5× more likely after a failure |
| B4 | long bridges rarely wrong | held: 0.43% |

**Reading.**
- B.38's explanation now stands measured. Failures come in dips, and a bridge across a dip is only as good as a coarser
  step, so bridges carry only 41% of the failures.
- Post hoc: many scenes (25 of 40 at K = 3, 17 of 40 at K = 5) have five or more failures no bridge carries, and
  those were among B.38's lost runs.
- At 256 stops what remains is short stretches of low supply, crossed from behind only 41% of the time. Crossing them
  reliably needs a bridge from the far side, more
  landmarks per stop, or a reader free to stop and look around.

### B.41 The corner set from the front half [R78]

*Numbered B.41 because B.40 (the wide field) is being logged in the other workspace.* Registered before the run in
`corner/frontcorner-predictions.md`; script `corner/frontcorner.mjs`, frozen as `frontcorner.registered.mjs`. The
reading view places a reader's centre on the inward normal at its leaf, at the distance R where a statistic of what it
sees equals R. By construction the ray home then has magnitude R, so the leaf sits at the corner whenever a centre
exists; the question is whether one exists. Four arms: facing (front half, the reader's two facings; or the whole turn,
the code's) × statistic (median; or mean, the code's). 73 library shapes × 16 leaves = 1168 positions.

| | registered | verdict |
|---|---|---|
| F1 | front half, median: a centre exists at ≥ 95% of positions | **killed**: 62.3% |
| F2 | exactly one at ≥ 80% | **killed**: 61.2% |
| F3 | the circle: R is its radius | held (2 × 10⁻⁴ of size) |
| F4 | home ray = R at every centre (construction check) | held (10⁻¹⁵) |
| F5 | facing moves R more than the statistic | held: 69% |
| F6 | the backside's weight: median change in R ≥ 0.05 of size | held: 0.096 |

A centre exists at 62% (front, median), 72% (front, mean), 86% (whole, median) and 88.5% (whole, mean).

**Reading.**
- From what a reader faces, the corner between its serial and parallel readings sits at its own leaf on about three
  standpoints in five. The whole turn, which includes the backside, reaches 88%.
- Post hoc: where it fails, it is mostly (371 of 440) because the median of what the reader faces stays above the
  distance home at every R: the leaf is always nearer than half of what the reader faces. With a flat wall ahead the
  median is √2·R. Leaves on straight stretches failed 54% of the time, leaves at bends or on curves 28%.
- The facing matters more than the choice of median or mean (F5): the backside is what the code's construction was
  leaning on.

### B.42 Which hangers does g place? [R80]

*Registered Sep 27 (`gsweep/predictions.md`, script frozen). Tom, 20:56: "it is a sweep, so probably follows the same
rules as any sweep… Probably not evenly spread, lets investigate."* Three rules for placing gN of the N hangers on the
front half, from the view's own standpoint: **EVEN** (every (1/g)-th; needs the whole facing in hand, so not a sweep),
**HOME** (the turn sweep, outward from home on both sides), **CORNER** (the stretch sweep, a ladder outward from the
corner toward home and the horizon). Measured D(g), the share of the shape's departure from the circle, Σ|ln m|, that
the placed hangers carry; 1034 pairs.

| g | 0.1 | 0.25 | 0.5 | 0.75 | 0.9 |
|---|---|---|---|---|---|
| EVEN | 0.100 | 0.250 | 0.500 | 0.750 | 0.900 |
| HOME | 0.002 | 0.028 | 0.223 | 0.586 | 0.832 |
| CORNER | 0.107 | 0.266 | 0.529 | 0.780 | 0.915 |

G1, G2, G4 held; G3 killed (CORNER sits just above EVEN, not between); G5 killed (the chosen statistic, the slice's
front median, is pinned at 1 by the unplaced hangers and cannot tell the rules apart). Post hoc: HOME places almost
nothing of the shape until it nears the corner, partly by construction (the reader's circle touches the outline at
home); CORNER is a sweep that delivers the shape in step with g. Which rule g follows is Tom's to rule; the measurement
says what each gives. *Later the same evening (R80, 21:34): g has no horizon and no corner, so the CORNER arm is a
placement rule borrowed from the reading, not g's own.*

### B.43 g as the vanishing point [R77, R79, R80]

*Registered Sep 27 (`vanish/predictions.md`, script frozen). Tom, 21:04: "maybe g is the vanishing point."* Each library
shape (N = 1024 hangers, size 1) recedes along the forward sweep, z from 2 to 4000; the reader's grain is fixed (the
front half in 4096 directions). g(z) = hangers the reader can still tell apart ÷ hangers visible at that distance. All
four predictions held: **g falls as 1/distance** (log–log slope −1.012), so g is inverse depth and the vanishing point
is g = 0, reached where the whole thing fits in one direction (z ≈ 1300 here); at g ≈ ½ the hangers facing the reader
survive 3.85× as often as those near edge-on (0.73 against 0.19), and the survivors span the whole visible thing
(0.997). Post hoc: receding thins a thing by facing, everywhere at once, edge-on parts first; this is none of B.42's
three rules. The setting differs from B.42 (a thing ahead, not the outline the reader stands on).

### B.9 Index of scripts and registered predictions (Sep 24–25)

| script | predictions file | what it checks | result |
|---|---|---|---|
| `interleave.mjs` | `interleave-predictions.md` | Proposition 3 on seven shapes | all held |
| `divide.mjs` | `divide-predictions.md` | Proposition 7a | all held |
| `moves.mjs`, `moves2.mjs` | `moves-predictions.md` | which moves keep the Cauchy | three kills, then held |
| `sweeps.mjs` | `sweeps-predictions.md` | three even sweeps | all held |
| `halving.mjs` | `halving-predictions.md` | halving by adding bars; the root | all held; one finding logged |
| `pointing.mjs`–`pointing3.mjs` | `pointing-predictions.md` | cost of algorithmic pointing | design kills, then held (B.7) |
| `worked.mjs`, `worked2.mjs` | `worked-predictions.md` | one drawing, two grains | two kills (B.4) |
| `stretch.mjs` | `stretch-predictions.md` | the stretch starts at the corner | one rounding tie (B.8) |
| `contact.mjs` | `contact-predictions.md` | arctan-free window and floor | all held |
| `defer.mjs` | `defer-predictions.md` | floor once vs every move | one scoring kill (the lap), then held |
| `plugin.mjs` | `plugin-predictions.md` | Proposition 13, the plug-in | one bound missed for the clock (B.10); rest held |
| `median.mjs`, `orthogonal.mjs` | `median-predictions.md`, `orthogonal-predictions.md` | Proposition 14: address and payload orthogonal (§7.5) | held; sinh made the mean undefined, logged |
| `shapes/extract.py`, `shapes/library-test.mjs` | `shapes/library-predictions.md` | address against arrival on the 73 library shapes (§7.5) | L1 held; L2, L4 and part of L3 killed (census seeding; ties) |
| `measure.mjs`, `measure2.mjs` | `measure-predictions.md` | arrival measure against address measure; Proposition 15 (§7.5) | held; the address median's per-doubling rate missed its band, logged |
| `gauss.mjs` | `gauss-predictions.md` | parallel Gaussian, serial Cauchy (§7.0) | all held |
| `toy3d.mjs` | `toy3d-predictions.md` | 3d as serial + parallel; a camera that divides (§7.4) | all held; largely arithmetic |
| `corner/toy3d-r79.mjs` | none (arithmetic check, after R79) | §7.4 rewritten: addresses across + forward magnitudes; the divided case; addresses alone; mispairing | checked, Sep 27: 3.4e-16; one scale = R to 1.3e-15; 6e-17 unchanged under 91% slides; 60% at 5% mispaired |
| `shapes/motion2.mjs`, `shapes/motion2-posthoc.mjs` | `shapes/motion2-predictions.md` | motion rerun with its three repairs (§7.7) | R3, R4 held; R1 (grazing: a saddle, not the grid) and R2 (by one) killed (B.15) |
| `shapes/measure3.mjs`, `shapes/measure3-posthoc.mjs` | `shapes/measure3-predictions.md` | which even sweep lays the addresses (§7.5) | Q3, Q4 held; Q1 (the median moves on fewer shapes, but far) and Q2 (resolution) killed (B.14) |
| `shapes/curvature-reader.mjs` | `shapes/curvature-predictions.md` | curvature landmarks on smooth borders, addresses only | S4 held (on 2 steps); S1–S3, S5 killed: too few peaks in view (B.29) |
| `threed/pose3d.py` | `threed/pose3d-predictions.md` | the addresses-only reader in 3D: three landmarks against four or more | T1, T2, T4 held; T3 held but uninformative (B.28) |
| `shapes/assembled.mjs` | `shapes/assembled-predictions.md` | the assembled observer: nothing given, own moves, rule 4, loop closure with the chain's veto | G3–G5, G8, G9 held; G1 (rule 3), G2, G6, G7 killed: closes on 4 of 69, all with rich corner supply (B.30) |
| `shapes/supply.mjs` | `shapes/supply-predictions.md` | the landmark supply census: corners, silhouette ends, far ends, curvature peaks | P1, P3, P5–P7 held; P2, P4 killed: the typical view shares two fixed points (B.31) |
| `shapes/edges.mjs` | `shapes/edges-predictions.md` | edges as landmarks: an edge is worth one address (the turn) under addresses only | E1, E4–E6 held; E2, E3, E7 killed: exact steps common (0.69), checked rare (0.13); carried 1.00 (B.32) |
| `shapes/scenes.mjs` | `shapes/scenes-predictions.md` | scenes of several shapes: does the supply grow with the world? | S1, S4, S5 held; S2, S3, S6 killed: 0.04 → about 0.8 by K = 3, then level; smooth scenes 0.00 (B.33) |
| `shapes/usable.mjs` | `shapes/usable-predictions.md` | the usable supply in scenes: position, signature, and the observer's own solver | U1, U2, U5 held; U3, U4 killed: the solver relates about 3 steps in 4; no scene solved at every stop (B.34) |
| `shapes/usable.mjs` (TOLS, USES) | `shapes/tols-predictions.md` | a tighter silhouette tolerance | T3–T6 held; T1, T2 killed: wrong steps stay; post hoc, symmetric copies (B.35) |
| `shapes/usable.mjs` (ACT) | `shapes/act-predictions.md` | the reader's own move as a veto or a filter | A2, A4–A6 held; A1, A3 killed: wrong steps cut by two thirds at no cost; corners + veto never wrong (B.36) |
| `shapes/usable.mjs` (STOPS) | `shapes/steps-predictions.md` | step size: 64, 128, 256 stops per loop | Z0, Z1, Z3 held; Z2 killed, Z4 killed by a registration error: 0.73 → 0.96 per step, gaps 22.5° → 2.8° (B.37) |
| `shapes/assembled-scenes.mjs` (PATH, 256) | `shapes/loops-predictions.md` | the observer in scenes: fine steps, bridging, the act, the chain's closure veto | L3, L4 held; L1, L2, L5 killed: 2–6 of 40 loops close; steps right, continuity and the loop check fail (B.38) |
| `shapes/bridge.mjs` | `shapes/bridge-predictions.md` | success against the span of a bridge; clustering of failures | all held: bridges carry 41% of failures, failures cluster 6.5× (B.39) |
| `shapes/noisy-reader.mjs` (diag, OUT=triple) | `shapes/triple-predictions.md` | can a reader judge a weak three-corner step from its own addresses | Q1 held; Q2–Q4 killed: failures are mismatches, not geometry (B.27) |
| `shapes/noisy-reader.mjs` (diag) | `shapes/diag-predictions.md` | what causes the addresses-only gap: per-step and per-corner records | D1, D2, D4 held; D3 half killed (B.26) |
| `shapes/noisy-reader.mjs` (DIST) | `shapes/distance-predictions.md` | solve or geometry: standpoint distance against the addresses-only gap | W3 held; W1, W2 held at 10⁻⁴, killed at 10⁻⁵ (B.25) |
| `shapes/noisy-reader.mjs` | `shapes/noise-predictions.md` (pilots in `noise-pilot.md`) | the two observers with noise; steadying at the address (item 13) | V2, V4 held; V1 (addresses beat √F), V3 (silent errors), V5 (orbits) killed (B.24) |
| `shapes/moving-reader.mjs` | `shapes/moving-reader-predictions.md` | the moving reader, addresses only: resection from held bearings (item 13) | A1–A4 held (B.23) |
| `shapes/addresses-only.mjs` | `shapes/addresses-only-predictions.md` | a reader holding only addresses tracks its landmarks (§7.7) | L1, L3, L4 held; L2 killed (looks 2–3× the firing rate) (B.22) |
| `shapes/frame-signal.mjs`, `shapes/frame-signal-posthoc.mjs` | `shapes/frame-signal-predictions.md` | one parallel frame kept current by serial events (§7.7) | K0–K3, K5 held; K4 killed (grazing borders, not only jumps) (B.21) |
| `shapes/orbit-unknown.mjs`, `shapes/orbit-unknown-posthoc.mjs` | `shapes/orbit-unknown-predictions.md` | the orbit unknown: steps from the reader's own landmarks (item 13) | U1–U3, U5 held; U4 (closure fooled by cancelling symmetric errors) and U6 (the registered ICP) killed; post hoc, point-to-line ICP reaches 44/73 (B.20) |
| `app3d/guided2.py` | `app3d/guided2-predictions.md` | the guided look repaired: one reader per backside, past the edge (§7.10) | all held (B.19) |
| `app3d/guided.py`, `app3d/guided-posthoc.py` | `app3d/guided-predictions.md` | a second reader sent to the first one's jumps (§7.10) | G1–G3 held; G4 and G5 killed on the pawn (two backsides) (B.18) |
| `app3d/readers2.py` | `app3d/readers2-predictions.md` | two readers together; knowing one's blind spot (§7.10) | C1–C4a held; C4b killed on the pawn (B.17) |
| `app3d/readers.py`, `app3d/readers-posthoc.py` | `app3d/readers-predictions.md` | the axis reader against the point reader (§7.10) | P1, P3, P4, P6 held; P5 (a bug) and P2 (a skin classification) killed (B.16) |
| `sphere/sphere.py`, `sphere/sphere-posthoc.py` | `sphere/sphere-predictions.md` | a first probe of the sphere (§7.9) | Q1–Q2, S1, S3, R2, R4 held; S2 (grid), R1 drilled, R3 on two shapes killed (B.13) |
| `shapes/orbit.mjs`, `shapes/orbit-posthoc.mjs` | `shapes/orbit-predictions.md` | recovery by a circling reader (§7.8) | P1, P4–P6 held; P3 killed (straight sides need more stops, B.12) |
| `shapes/motion.mjs`, `shapes/motion-posthoc.mjs` | `shapes/motion-predictions.md` | motion from the two readers on the 73 library shapes (§7.7) | M0, M6, M7 non-star held; M1–M5 and M7 star killed (B.11) |
| `corner/frontcorner.mjs`, `corner/posthoc.mjs` | `corner/frontcorner-predictions.md` | the corner set from the front half: does a centre exist that puts the reader's leaf at the median of what it faces | F3–F6 held; F1, F2 killed: 62% of positions; fails mostly where the leaf is always nearer than half of what the reader faces (B.41) |


## References

### External

- Arkin, E. M., Chew, L. P., Huttenlocher, D. P., Kedem, K. & Mitchell, J. S. B. (1991). An efficiently computable
  metric for comparing polygonal shapes. *IEEE Trans. Pattern Analysis and Machine Intelligence* 13(3), 209–216. doi:10.1109/34.75509. (The
  turning function. Confirmed Sep 25; volume, issue and pages checked 27 Sep.)
- Axler, S., Bourdon, P. & Ramey, W. (2001). *Harmonic Function Theory*, 2nd ed. Springer, GTM 137. (§5.4: the Poisson
  kernel as harmonic measure: Ch. 1, "The Poisson Kernel for the Ball", with n = 2. Checked 27 Sep.)
- Carathéodory, C. (1913). Über die gegenseitige Beziehung der Ränder bei der konformen Abbildung des Inneren einer
  Jordanschen Kurve auf einen Kreis. *Mathematische Annalen* 73(2), 305–320. doi:10.1007/BF01456720. (§5.4 item 5.
  Checked 27 Sep.)
- Beardon, A. F. (1983). *The Geometry of Discrete Groups*. Springer, GTM 91. (§4.3: elliptic, parabolic, hyperbolic.)
- Katok, S. (1992). *Fuchsian Groups*. University of Chicago Press. (§2.1.)
- Laurentini, A. (1994). The visual hull concept for silhouette-based image understanding. *IEEE Trans. Pattern
  Analysis and Machine Intelligence* 16(2), 150–162. doi:10.1109/34.273735. (§7.8. Confirmed Sep 26.)
- Letac, G. (1977). Which functions preserve Cauchy laws? *Proc. Amer. Math. Soc.* 67(2), 277–286. (Title, journal,
  volume, issue, pages and year confirmed Sep 25 against two independent citations: Chin, Jung & Markowsky,
  arXiv:1908.04006, and arXiv:1602.08181. The theorem's exact statement has **not** been retrieved; the paper itself
  still needs reading.)
- Chin, Jung & Markowsky (2019). A note on invariance of the Cauchy and related distributions. arXiv:1908.04006.
  (Initials and journal version not retrieved.)
- Cuadras, C. M. (2002). Geometrical understanding of the Cauchy distribution. *Qüestiió* 26(1–2), 283–287.
- Curless, B. & Levoy, M. (1996). A volumetric method for building complex models from range images. *Proc. SIGGRAPH
  '96*, 303–312. doi:10.1145/237170.237269. (§7.8. Confirmed Sep 26; pages checked 27 Sep.)
- Dietz, P. F. (1982). Maintaining order in a linked list. *Proc. 14th ACM STOC*, 122–127.
- Dunau, J.-L. & Senateur, H. (1987). *Journal of Multivariate Analysis* 22(1), 74–78. (Not found in a search on
  Sep 26; title unknown. What could be found is the 1988 paper below, on the conformal Cauchy. Check before relying on
  this entry.)
- Dunau, J.-L. & Sénateur, H. (1988). Une caractérisation du type de la loi de Cauchy-conforme sur ℝⁿ. *Probability
  Theory and Related Fields* 77, 129–135. doi:10.1007/BF01848135. (§7.9: the conformal Cauchy, density ∝
  (1 + |x|²)^−n; a non-atomic law's type is kept by inversions exactly when it is of this type. Abstract read Sep 26.)
- Dupuy, J., Belcour, L. & Heitz, E. Integration and simulation of bivariate projective-Cauchy distributions within
  arbitrary polygonal domains. arXiv:1909.07605. (§7.9: the projective Cauchy as the central projection of an even
  hemisphere, density ∝ (1 + |x|²)^−(d+1)/2. Read Sep 26; year from the arXiv number, 2019.)
- Gardner, R. J. (1995). *Geometric Tomography.* Cambridge University Press, Encyclopedia of Mathematics and its
  Applications 58 (1st ed.; a 2nd ed. appeared in 2006). (§5.4 item 5: the radial function. Checked 27 Sep.)
- Garnett, J. B. & Marshall, D. E. (2005). *Harmonic Measure.* Cambridge University Press, New Mathematical
  Monographs 2. (§5.4 item 5. Checked 27 Sep.)
- Goldberg, D. (1991). What every computer scientist should know about floating-point arithmetic. *ACM Computing
  Surveys* 23(1), 5–48.
- Faugeras, O. (1995). Stratification of three-dimensional vision: projective, affine, and metric representations.
  *Journal of the Optical Society of America A* 12(3), 465–484. (§7.4. Title confirmed Sep 25; volume, issue and first
  page checked 27 Sep, end page not.)
- Hartley, R. (2014). Projective reconstruction. In K. Ikeuchi (ed.), *Computer Vision: A Reference Guide*. Springer.
  (§7.4; definition quoted, retrieved Sep 25.) See also Hartley, R. & Zisserman, A. (2004). *Multiple View Geometry in
  Computer Vision*, 2nd ed. Cambridge University Press.
- Hatcher, A. (2002). *Algebraic Topology.* Cambridge University Press.
- Henderson, P. & Morris, J. H., Jr. (1976). A lazy evaluator. *Proc. POPL '76*, 95–103.
- Hopf, H. (1935). Über die Drehung der Tangenten und Sehnen ebener Kurven. *Compositio Mathematica* 2, 50–62.
- Itai, A., Konheim, A. G. & Rodeh, M. (1981). A sparse table implementation of priority queues. *ICALP 1981*, LNCS 115,
  417–431.
- Johnson, N. L., Kotz, S. & Balakrishnan, N. (1994). *Continuous Univariate Distributions*, Vol. 1, 2nd ed., ch. 16.
  Wiley.
- Knight, F. B. (1976). A characterization of the Cauchy type. *Proceedings of the American Mathematical Society*
  55(1), 130–135.
- Knight, F. B. & Meyer, P.-A. (1976). Une caractérisation de la loi de Cauchy. *Zeitschrift für
  Wahrscheinlichkeitstheorie und verwandte Gebiete* 34, 129–134. (Credited with the ℝⁿ projective characterisation by
  Mendonça & Lundell 2025; the paper's own page could not be read on Sep 26, rate-limited.)
- Lehmann, E. L. & Romano, J. P. (2005). *Testing Statistical Hypotheses*, 3rd ed. Springer. §6.8, Rank tests. (§7.5;
  section located Sep 26; the maximal-invariance statement itself not retrieved.)
- Encyclopedia of Mathematics, "Rank test". (§7.5: "Rank tests are invariant with respect to groups of transformations
  defined by continuous strictly-increasing functions"; retrieved Sep 26.)
- Lamping, J., Rao, R. & Pirolli, P. (1995). A focus+context technique based on hyperbolic geometry for visualizing
  large hierarchies. *Proc. CHI '95*, 401–408.
- Milnor, J. W. (1965). *Topology from the Differentiable Viewpoint.* The University Press of Virginia,
  Charlottesville. (§7.9: the Poincaré–Hopf theorem. Publisher and year confirmed Sep 26.)
- Mardia, K. V., Goodall, C. & Walder, A. (1996). Distributions of projective invariants and model-based machine
  vision. *Advances in Applied Probability* 28(3), 641–661. (§11.1: Cauchy laws in the cross-ratio under Gaussian
  errors. Abstract read Sep 26.)
- Mendonça, P. R. S. & Lundell, B. (2025). Explicit formulae for projectively transformed Cauchy distributions with
  applications. *Statistics & Probability Letters* 222. (§7.9, §11.1: Cauchy laws as the continuous family invariant
  under projective maps, univariate to vector and matrix valued, crediting Knight 1976 and Knight & Meyer 1976 for
  ℝⁿ; a triangulation algorithm. Abstract read Sep 26.)
- Mustaniemi, J., Kannala, J., Särkkä, S., Matas, J. & Heikkilä, J. (2016). Inertial-based scale estimation for
  structure from motion on mobile devices. arXiv:1611.09498. (§7.4; quoted, retrieved Sep 25.)
- Mardia, K. V. & Jupp, P. E. (2000). *Directional Statistics.* Wiley. (§5.4: normalising to the circle; the wrapped
  Cauchy, pp. 50–52, in the wrapped distributions, §3.5.7. Pages as cited in arXiv:2409.03292; the section number not
  seen in the book.)
- Nagel, T. (1986). *The View from Nowhere.* Oxford University Press. (§5.4: source of the phrase; cited as an echo.)
- McCullagh, P. (1996). Möbius transformation and Cauchy parameter estimation. *Annals of Statistics* 24(2), 787–808.
- Volder, J. E. (1959). The CORDIC trigonometric computing technique. *IRE Transactions on Electronic Computers*
  EC-8(3), 330–334.
- Prince, J. L. & Willsky, A. S. (1990). Reconstructing convex sets from support line measurements. *IEEE Trans.
  Pattern Analysis and Machine Intelligence* 12(4), 377–389. (§7.8. Confirmed Sep 26 from the paper.)
- Reddy, B. S. & Chatterji, B. N. (1996). An FFT-based technique for translation, rotation, and scale-invariant image
  registration. *IEEE Trans. Image Processing* 5(8), 1266–1271. doi:10.1109/83.506761. (§7.7: log-polar registration.
  Confirmed Sep 26.)
- Zhang, D. & Lu, G. (2004). Review of shape representation and description techniques. *Pattern Recognition* 37(1),
  1–19. (§7.7: the centroid distance function. Authors, title, journal, volume and pages confirmed Sep 26.)
- Schneider, R. (2014). *Convex Bodies: The Brunn–Minkowski Theory*, 2nd ed. Cambridge University Press. Encyclopedia of Mathematics and its Applications 151. (§5.4
  item 5: the support function, §1.7; the Gauss map, Ch. 2. Section level checked 27 Sep; subsections not.)
- Weihrauch, K. (2000). *Computable Analysis: An Introduction.* Springer, Texts in Theoretical Computer Science.
  doi:10.1007/978-3-642-56999-9. (§11. Checked 27 Sep.)
- Varićak, V. (1910). Anwendung der Lobatschefskijschen Geometrie in der Relativtheorie. *Physikalische Zeitschrift*
  11, 93–96.

### The series

`writer-notes.md` (companion, Sep 25); 
*One Reader* (Sep 23–24); *The Cauchy, Inside and Out*; *The Relation Space*; *The Unit Rule*; *The Six Things*;
*Degrees of Freedom*; *The Centring*; *The Boundary* (working log); *The Cauchy*; *Keeping the Horizon*; *The Serial
Cauchy*; `serial-watch.xlsx`; `v-and-h.md` (the list of ideas about v and h, with the checks against each paper).
Scripts: `closure.mjs`, `rigor.mjs`, `freedom.mjs`, `finished.mjs`, `fixfid.mjs`–`fixfid3.mjs`, `densities.mjs`,
`densities2.mjs`, `noise.mjs`, `cornerrule.mjs`, `dialphysics.mjs`, `landmark.mjs`.
