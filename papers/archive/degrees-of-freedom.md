# Degrees of Freedom
## What they are, and how they compose

*A research record in the calibration-free series.* ***Freedom* here is short for *degree of
freedom*, in the ordinary sense this series already uses — not a new object and not a new name
for one.** *A degree of freedom is **v in terms of h, at expression g**: an address on **[0, ∞)**,
scale-invariant, and an address to a magnitude rather than the magnitude itself; the expression is how
fully the signal is expressed, runs 0 to 1, and takes no part in any address. **g was called the unit
radius until Sep 18 2026; the letter changed because* radius *was carrying three jobs at once (Tom:
"radius is already overused"), and r now means only a figure's radius in a direction — a magnitude, the
thing a hold is.** Nothing is assumed about what any degree of freedom addresses;
the question is only how they compose into larger structure, and which ones to plug in comes
afterwards; a composite of freedoms is itself a freedom, since it meets the same definition, so
nothing here is sorted into types. §5.1 works three examples in full, but **the construction has
no preferred size**: the composition law holds identically at two freedoms, at ten and at five
hundred (§5.9). **Sep 20 2026: §5.18 adds the serial/parallel pair as two SIGNALS — 1d is motion, 2d
is magnitude lists, 3d is both together and still separate — and with it the ruling that* **we
project serial and count parallel, because N is unknown in one and known in the other***. That
reclassified one existing passage: §5.16's quantile account of hangers is a count, and so a parallel
reading performed on a serial stream. §5.18a then rules 2d as CLOSURE — a closed list holds every relation in both facings, and the condition is a symmetry about the corner rather than a count — and §5.19 rules DEPTH: it is z, the serial signal, and it is
the log radius — so 3d is a cylinder, direction round the plane and depth up the axis, and the grain
of §5.7 is the measure along it.* A research record for this series, not for publication;
unreviewed; the title is provisional.*

*Revised 1 October 2026: the text is left as it was, and notes marked* **(1 Oct)** *say where the rulings of 30 September – 1 October (R124–R152 of* Reader Geometry as Addressing*) change how it reads. The composition arithmetic (§2–§4.1, §4.4–§5.14, §6) and §5.17's proofs stand as the record; what the paper says about readers and situations is re-situated below.*

> **(1 Oct) How to read this paper now.**
> - **The situations** (R137, R146, R151, R152). (1) The circle: both breadths known and equal; the view from nowhere. (2) Every other shape: breadths known, varying with direction; also a view from nowhere. (3) The fisheye: h's breadth known (h is the known side by definition), v's not, so v is had only as a count of h's; the only view from somewhere, and the only situation with a reader in it, serial or parallel. (4) Neither known: impossible. (5) v's breadth known approximately. The list is not exhaustive.
> - **A freedom as defined here**, v in terms of h with home, corner and horizon, is a situation-3 object. Division, home, the corner and the horizon belong to situation 3 only; the circle and other known shapes have none (R131, R139). Where the paper gives them to circles, shapes or the parallel account, read situation 3.
> - **Two g's.** This paper's g, the expression, runs from the circle (0) to the full shape (1): that is situation 2's ratio of circle to shape (R140). The corpus's g since 30 September is the ratio between the reader and the world, 0 = reader, 1 = world. They share a letter and a range; they are not the same quantity, and the reader is not the circle (R127).
> - **The corner and the two sides** (R149–R150, R152). The corner is known in situation 3, where v reaches one h. The front side, home to the corner, is swept from home in plain proportion (two known ends) and is the **working horizon**; the corner is its edge. The back side, past the corner, is counted by doublings. The parallel reader keeps v on the front side only.
> - **Arctan** is an index into the turn, a shortcut, not the sweep (R148). **Depth** is the forward sweep, the parallel reader's (R79). Observation is not called dimensional (R125).
> - **Names now in use.** "The view from everywhere" → **the view from nowhere**; "inside/outside" → **serial/parallel**; "the fulcrum" → **the corner**; "density" is dropped as a framework word (the Cauchy's probability density keeps its name). Quotes keep their wording.

---

## 0. What this paper is about

**One shared denominator, and what can be built on it.**

A reader with one register holds one value and reads everything against it. Three such readings
share that value, and the question is what they can be: what they address, how they compose,
what the composition leaves behind, and where it stops.

**The word for such a reading here is *degree of freedom*, shortened to *freedom*** — one
independent way a reader's situation can vary. It is used because it asks *whose*, which is this
series' first question about anything, and because it says nothing about directions or axes,
which the construction never needs.

**And what it carries is worth having.** A degree of freedom is not freedom in the loose
sense. It is
**constrained** — it belongs to a reader with one register and one hold — and the constraint is what
makes it an address rather than a measurement. Dividing v by h is what discards the scale; a
reader rich enough not to have to divide would never get an address at all. **The scale-freedom
is a consequence of the poverty, not a triumph over it.**

**And the mathematics here is imported.** Tan of an even turn is Cauchy, quantiles are quantiles, a
trigonometric polynomial of degree m needs 2m + 1 samples, and a shared denominator cancels — all
classical, and cited where used (§7). **What the constraint supplies is the division, and the order in
which things become available to a reader that can perform nothing else.** Where this paper claims
something of its own, it says so in the same breath.

**The order is deliberate.** Sections 1 to 4 build the structure from one reading, then several
sharing a hold, then how they compose. The composition law falls out, the denominator cancels
from its own result, the corner turns up as the identity, and the horizon turns up as the place
where composing stops. **Whether any of that is afterwards recognisable as something a reader
already has a name for is a question better answered having seen it first**, and this paper does
not answer it. **Where the two words of the definition come from — *address* and *magnitude* — is
§5.15**, and it is the reason the definition reads as it does.

## 0.1 Everything here is counted by listing

**The four cases are two by two.** Who supplies the terms, which direction the passage runs — the
count is reached by enumeration, and *The Six Things* §10 had it long before this paper. So does
the rest: all rearrangements of four things, listed, are twenty-four; those a reader can perform
without mirroring, twelve; movements of three marked extents, twenty-four, of which three keep
every extent non-negative while eight regions are reached, giving 8 × 3 by counting
(`without_groups.mjs`).

**No group theory is used anywhere in this paper, and that is deliberate.** An earlier version
reached for group theory and got four further results from it — three axes as one family,
isotropy as a consequence, no intermediate accounting, and an identification with a cube. Each
was real. None was needed for the count, and all required machinery the rest of this series
never uses, so they have been removed rather than kept as an import. **That version is kept
beside this one as `the-inventory-with-algebra.md` for anyone who wants what it bought.**

**What is *not* meant by that.** Ordinary arithmetic stays: the paper divides and multiplies, and
uses associativity, an identity and inverses on every page. What was removed is machinery the
rest of this series never uses — named groups, conjugacy, automorphisms — **not the arithmetic
itself.**

## 1. A degree of freedom

> **(1 Oct)** The definition carries home, the corner and the horizon into every freedom: in the current terms that makes a freedom a situation-3 object (R146). Its g is the circle-to-shape ratio of situation 2 (R140), not the Sep 30 g, and "it is a DENSITY" falls under R124. Ruling 3 here (parallel with N known, spaced uniformly) describes the view from nowhere: both readers are in situation 3 (R152). Ruling 10, "the turn and the circle belong to whoever is describing the reader", is what R127 settled.

**A note on the word before anything else.** *Freedom* below is an abbreviation of *degree of
freedom*, used because the phrase appears on nearly every line and the full form makes the
composition rules unreadable. It denotes exactly what this series has always meant by a degree
of freedom — one independent way a reader's situation can vary — and nothing is claimed by the
shortening. Where a sentence would be ambiguous, the full phrase is written out.

### Definition

Let **h ≥ 0** and **v ≥ 0**, not both zero, be two magnitudes arriving together — h the hold, v
the one read against it — and let **g ∈ [0, 1]** be the expression, 1 at the limit.

> **A degree of freedom is v in terms of h, at expression g.**

It has two parts, and each is ruled on separately.

**The address.** s = v / h, on **[0, ∞]**, with s = ∞ exactly when h = 0. Two pairs have the same
address exactly when one is the other scaled by some λ > 0: (3, 4), (21, 28) and (0.03, 0.04) all
give 0.75. **The address is that equivalence class, and it has no size.** Its angular form, u =
arctan s on [0, π/2], is a parametrisation of the address and not a second address (§4.3).

**The expression — and it is a DENSITY (Tom, Sep 18).** g is the share of the freedom's hangers that are
placed: **at g = 1 all N of them, at g = 0 none, and gN in between.** It does not enter any address.

Everything else this paper says about g follows from that one reading, and follows rather than being
asserted beside it. **Detail is downstream of density**: a perturbation needs hangers to sit on, so how
much of the list can be expressed is a count of places and not a level of anything (ruling 9). The cost
of a value is the count of its hangers. The horizon is where the hangers run out. And at g = 0 there are
no hangers at all — **which is why the unit circle there is an abstraction and cannot be drawn: a drawn
thing has places where values sit, and no N means no places.** What a picture of it shows is the page
lending it hangers it does not have.

⚠ **And the hangers are EMPTY.** Placing them is all g does; what hangs on them is the magnitudes, and
**the scale comes with what hangs, never from g** (§3.1). A freedom with all N hangers placed and
nothing hung is a complete frame and no figure.

⚠ **And "share" is a COUNT, which makes g a parallel-side word (Tom, Sep 20).** *We project serial
and count parallel, because N is unknown in one and known in the other.* To place a share of the
hangers you have to know how many there are, so gN is something the construction has and a serial
reading does not — not because the reader is inside anything, but because a count needs a total and
it has none. **g = 1 is the exception and it sits in neither column:** it enumerates nothing, so it
is not a count, and it maps no arrival, so it is not a projection. It is the claim *that there was
no count to make*, which is why it is the one value of g a reader with no total can confirm (§5.18).

⚠ This supersedes the earlier phrasing, which called g a level of detail and had the hangers as a
consequence of it. The order was backwards. Sections written before Sep 18 still say *level of detail*
for what is now the density; the reading is the same in every case and the words are a sweep still owed
(§8, item 12(b) carries the other half of that sweep).

**AND THE ADDRESS'S LAW IS NOT A CHOICE EITHER (Sep 18).** A reader that holds one value and divides has
exactly four moves on its own addresses — swap the hold, rescale it, compose two readings, shift by held
multiples — each linear on the pair and so each a map of one kind, and together all of them: every such
map is compose · rescale · compose. That repertoire is closed and maximal, and the Cauchy is the only
family of laws closed under it, which is a rigidity result of Knight's and not this series'. **So an
evenly met turn is not the only route to the Cauchy: the second route is that the reader could report no
other law**, and it needs no assumption about what arrives. See *The Repertoire*; the moves and the
cross-ratio test that polices them are executable in `freedom.js` and `vcp-core.js`.

**And g is the reader's, not the signal's.** Nothing in a signal names one. A reader arrives, names a g,
and only then are there values to speak of — which is why a reading is two choices and not one: where to
point, and how much of the freedom to open (ruling 11). **h and v take the scale out of a pair; g is what
put it in** — and the two are not inverse, since what g supplies is the reader's scale, chosen, and not the
world's, recovered (ruling 12).

**In serial, g is how much of the signal has arrived.** Arrivals spread over the turn express the shape
coarse first: a few arrivals give only the unit circle; the broadest perturbation appears next, then finer
ones; the finest appears only with the last arrivals (ruling 9). **At g = 1 the reader is sweeping the
full shape and all of its perturbations. At g = 0 the shape is gone, there is nothing to sweep, and the
reader is browsing the unit circle.** This paper assumes the pristine synthetic situation throughout:
arrivals spread evenly over the turn, as the Cauchy's hidden unit circle already assumes (ruling 8).

### Rulings

**1. An address is not a magnitude.** The magnitude is spent forming the address and is recovered
only by bringing the hold back: v = s · h. A freedom addresses a magnitude and is not one.

**2. An address is not a reading.** The address is fixed by h and v alone. A reading is its
representation at a level of detail, and it depends on g. So h = 1, v = 0 has the address 0 at every
expression, while what is *read* there changes with g.

**3. What the reader holds fixes the spacing; nothing else does.** The cut is not between early and late
but between **holding the list and holding one value**. A reader that holds the list has n, its number of
magnitudes, and can divide the turn by it; a reader with one register holds a single value, so n never
becomes available to it however long it reads. Parallel and serial are those two cases, and the spacing —
and so how many addresses are told apart — follows from which one obtains:

| situation | n | spacing | what r changes |
|---|---|---|---|
| **parallel** | known | **uniform over n** — n hangers, each (π/2)/n of the turn (§5.16) | the level of detail at which the n hangers are expressed; never how many |
| **serial** | unknown | **the fisheye** — there is no n to divide the turn by, so what arrives is placed by the tangent, and the hangers are the Cauchy's quantiles (§5.16) | whatever the fisheye expresses at that level of detail (*Browsing the Fisheye* §7–8) |

There is no third case, and no choice of grain to make beside this one. A count of addresses that
does not say which of the two obtains is incomplete. **And the cut is not about time:** a reader that
kept its arrivals would have the list and the parallel picture with it, which is why the serial case is
stated as one register rather than as reading over time.

**4. At g = 0 no hanger is placed.** There is nowhere for a value to sit, so the signal has no
expression and only the unit circle remains — as an idea, not as a drawing. The address is still defined, but nothing of the signal is expressed to read it from:
h = 1, v = 0, g = 0 does not read 0, because at g = 0 nothing is read but the circle — the reader is
browsing the circle, not sweeping a shape.

**5. The expression is not an arrival's size, and no longer shares its letter.** §4.3 Case B reads
arrivals at "radii" 1, 2, 0.5 and 10 against a laid-down unit. That quantity is a recovered magnitude —
it exceeds 1 — and was never the dial of this definition. **Since Sep 18 the two have different names: g
is the expression, bounded 0 to 1, unitless, the reader's; r is a figure's radius in a direction, a
magnitude, the world's, and what a hold is made of.** That closes §8's flag 12(b). A third use, *The
Radix* and *Browsing the Fisheye* §8's reach, remains its own dial (12(a)).

**6. The horizon is an address no arrival reaches.** s = ∞ belongs to the address set, but no finite
v over a hold above zero produces it (§5.17). Composition is undefined where one address is 0 and
the other ∞ (§6).

**7. Membership is three tests.** A quantity is a freedom exactly when it is formed as one thing
against another, is unchanged when both are scaled, and addresses rather than values (§5). A count
fails the second. A composite of freedoms passes all three and is a freedom (§5.11).

**8. The Cauchy's result is the fisheye; the unit circle is a hidden assumption inside it.** The
circle is an intermediate step in the Cauchy's derivation — the angle taken as spread evenly over the
turn, then carried through the tangent — and the result is the fisheye. The circle is in there, and it
is a useful visualization of that step; it is not what the Cauchy presents. **The intermediate step is the
parallel situation:** laying the turn out evenly needs N known in advance (ruling 3). The fisheye appears
only when the reader reads that circle serially. **And the even turn is the world's assumption, not the
reader's:** it says the arrivals are spread over the turn — something turning at a constant rate, met at a
constant rate — while what the reader contributes is its grain (§8, item 12(d)). **The fisheye is what an
even traverse looks like read through a reader's addresses.**

**9. The shape is the unit circle, expressed.** A shape is not a second object beside the circle: it is the
circle with its perturbations expressed, and serial arrival expresses them in order of coarseness. Each
level arrives whole — a perturbation of n lobes is absent until about 2n + 1 arrivals and then present at
its full amplitude — so detail is added level by level and never faded in (`serial_expression.mjs`). A
shape with a circle and perturbations of 2, 5 and 13 lobes, at amplitudes 0.30, 0.15 and 0.05, over 256
arrivals:

| arrived | g | expressed |
|---|---|---|
| 1–3 | 0.004–0.012 | the unit circle |
| 7 | 0.027 | + the 2-lobe perturbation at 0.300 |
| 15 | 0.059 | + the 5-lobe at 0.150 |
| 31 | 0.121 | + the 13-lobe at 0.050 |
| 255 | 0.996 | the full shape |

**And that gives g a formula — as a count of hangers, which is what g is.** A trigonometric polynomial of
degree m is determined by 2m + 1 samples (§7.9a), so k = gN hangers spread over the turn carry
perturbations up to

> **lobes ≈ (gN − 1) / 2**, and an n-lobe perturbation needs **g ≥ (2n + 1) / N**.

On the run above, N = 256: the 2-lobe needs r ≥ 0.020 and appeared at 0.027; the 5-lobe needs 0.043 and
appeared at 0.059; the 13-lobe needs 0.105 and appeared at 0.121.

**And below its threshold a perturbation is not missing: it folds onto a hanger already there**
(`hangers_fold.mjs`). At k arrivals the n-lobe and the (k − n)-lobe give the same value at every arrival,
since cos(nθ) at θ = 2πi/k depends only on n mod k — **aliasing, on the turn.** Three consequences, and the
third is a proof:

- **A shape with nothing coarse in it reads as coarse.** A pure 13-lobe of 0.300 reads as a 1-lobe of 0.300
  at 7 arrivals and a 2-lobe of 0.300 at 15, at full amplitude, and only at 27 as itself.
- **Where the hanger is occupied, the readings add.** A true 2-lobe of 0.300 with a 13-lobe of 0.200 reads
  0.500 or 0.100 at 15 arrivals, by the phase of a perturbation the reader cannot resolve; at 21 it reads
  0.300 again, though the 13-lobe is still not carried. **Nothing is ignored and nothing is lost from the
  reading; what is lost is attribution.**
- **And the earlier lobe is then unrecoverable, provably.** At 15 arrivals a 2-lobe of 0.500, a 2-lobe of
  0.300 with a 13-lobe of 0.200, and a 13-lobe of 0.500 with no 2-lobe at all agree at every arrival to
  1e−15, and all three read a 2-lobe of 0.500000. The map from shapes to readings is many-to-one, so no
  reading separates them.

**So the order of landing is fixed from outside, and the reader has its own test for it** (`settling.mjs`).
From outside: **a lobe lands at k ≥ 2n + 1**, so the order is the order of lobe count and amplitude plays no
part — a 13-lobe of 0.05 and one of 0.90 both land at 27. From inside the reader cannot see thresholds, but
**a landed reading stops moving while an aliased one jumps.** On a shape with lobes at 2, 5 and 13 (0.30,
0.15, 0.05), the 2-lobe's hanger reads 0.4500, 0.3000, 0.3500, 0.3000, 0.3500 at 7 to 15 arrivals as first
the 5-lobe and then the 13-lobe fold onto it, then holds at 0.3000 from 17 on; the 13-lobe appears at 27,
its threshold, and never moves again.

⚠ **But that test does not survive real arrival, and it was tested** (`settling_incremental.mjs`). The table
above re-spreads its arrivals at every count. A serial reader cannot: it adds one at a time and refits on
the set it has, and then **a landed reading can un-land** — in spread order the 2-lobe reads its true 0.3000
at 13 arrivals, drifts to 0.2676 at 17 and 0.1752 at 21, and returns to 0.3000 only at 27. **Quiet is not
evidence either:** the same run moves 0.0000 at 13 and 0.1045 eight arrivals later. And the readings do not
land lobe by lobe: declaring a landing after five quiet arrivals gives k = 32, 32, 32 in one regime and 26,
26, 57 in another, against thresholds of 5, 11 and 27 — the declarations mark where the whole fit became
exact, not where each lobe crossed its own threshold. Every regime ends correct to 1e−13 or better, so what
fails is not the reconstruction but the reader's reading of its own progress.

> **So the landing order stands and the reader's test for it does not.** 2n + 1 is a theorem and holds
> whatever the arrival; what a reader can tell from its own readings is only that the shape **as a whole**
> has stopped moving, never which part of it has landed.

> **The threshold is where this stops.** Past g ≥ (2n + 1)/N the n-lobe has a hanger of its own and cannot
> be confused with a coarser one. Below it, what the reader holds is not the coarse part of the shape but
> **the coarsest shape consistent with what has arrived.**

**And what perturbs a freedom is a magnitude list.** A bare freedom has nothing to express: it is an address
space, and its perturbations are the magnitudes hung on it (§5.16). So the circle at g = 0 is not an empty
shape but a freedom with none of its list expressed yet, and **locking g locks the freedom at the level of
perturbation that list defines** — the lobes up to (gN − 1)/2 of that particular list, and no others. ⚠ And by
the fold above, **a figure locked at g does not name its list:** many lists express to the same figure at
that level, and nothing in the figure says which was hung on it.

**So g's purpose is to fix a figure.** A freedom with a list hung on it is not yet a shape: it is something
that could be expressed at any level. **Choosing g is the act that makes a figure of it**, resolved at that
level of detail and no other — which is why a figure cannot dial afterwards and why every reading taken
against it inherits the level. The two ends are not special cases: g = 0 is the lock at nothing expressed,
which is the circle, and g = 1 the lock at everything.

**And a shape is a freedom that has fixed its expression.** A freedom still has the dial: r runs from the bare
circle to the full expression, and the reader moves along it. A figure has already turned that dial and
locked it — its horizons are resolved at the level it was expressed at, every reading against it inherits
that level, and the figure does not say which level it was (*The Centring* §5b). **In serial the dial turns
one way only:** an arrival can raise the level already expressed and cannot lower it or choose a different
one after the fact.

**The confusion this rules on:** looking for the shape as a thing apart from the circle. The circle is
always there first; the shape is what arrives on it.

**What is classical here and what is not** (§7.9a): the circle-plus-harmonics form is standard — in radial
frequency patterns, in Fourier descriptors where a circle is the shapeless zero, and in the sphere-plus-
corrections of nuclear and geodetic shapes — and so is the 2n + 1 threshold, which is the sampling theorem
for a periodic signal. **What is this paper's:** that the circle is what a reader has before anything
arrives rather than an origin chosen for convenience, and that the coarse-to-fine order is forced by
serial arrival rather than chosen as it is in progressive image coding.

**10. The reader produces the address; the turn is the outside view's.** A reader with one register forms
s = v/h and holds nothing else. Reading that address back as a turn, u = arctan s, needs an arctangent it
does not have and a corner it can only estimate, so **the turn and the circle belong to whoever is
describing the reader, not to the reader** (ruling 8; *the path, formally*, Step 3). What this does not
weaken: every address stream corresponds to exactly one turn, so the circle is always available as a
representation. **The ratio selects the coordinate; the measure on it is additional information** — which is
where flag 12(d) sits.

**11. A magnitude list is not given; it is what a generator returns at a named g** — and since g is a
density, what it returns is what the hangers g placed can hold. This reverses the
paper's own earlier usage, on Tom's ruling of Sep 17 2026 (*"you need to specify its radius to know what
the values are"*). A freedom holds no values. Name a g and values come back — actual magnitudes, with
scale, in the world's own terms — and a different g returns different ones, none of them wrong. **Asking
what a signal's values are without naming a g is not a hard question but an unfinished one.** Two
consequences the paper already half-stated: the circle at g = 0 is not an empty shape (ruling 4), and the
values at an intermediate g are not degraded copies of the values at 1 — they are that generator's honest
values at that expression.

**12. What generates a list can be anything that returns magnitudes** — an equation, a shape or outline,
an algorithm, a table, a physical object met by an instrument. **The corpus's figures are one species and
not the definition** (§2.2). What matters is not what kind of thing it is but whether it answers two
arguments at once: which direction, and at what expression. A generator that answers only the first has
already spent its g, which makes it a figure rather than a freedom. ⚠ **And answering is not the same as
being walkable**: whether a reader can move through a generator's levels one at a time is a further
condition, and it is *The Radix*'s — the generator's orders must sit in the reader's own ratio, or their
schedule must be handed to it (§2.2).

**13. The expression is spent at both ends, and for opposite reasons.** At g = 0 no hanger is placed, so
the signal is unexpressed and the circle is all there is. **And a reader too far in does not hold the whole thing either** (Tom,
Sep 17): the window carries a patch, the rest of the turn is outside it, and a small enough patch is flat
— the circle again. So g trades the whole against the detail rather than climbing toward completeness, and
**no single station holds a signal entire.** ⚠ The attempt to derive g's shape from the vanishing-point
freedom — a folding peaked at the corner, 2vh — was measured and **did not survive**: with the generator's
own amplitude law divided out, the reader's response is not peaked but a **plateau**, running from its
grain up to its view and falling as 1/r² above it, of width log₂(view ÷ grain) octaves at every glass size
tried (`example-shape.html`, Sep 17). The peak belonged to the list: amplitude ∝ period^α gives arms α and
α − 2, measured across α = 0 … 2. **What survives is that g is the share of the rungs between two ends that
are both the reader's — the pose at the top, the grain at the bottom** — which is what a browsing dial
computes, span = N^g. The rest is open (§8, item 14).

### The marks

The address has two ends and one interior mark, and this is the whole of its structure:

| address | what it is |
|---|---|
| **0** | the numerator has gone absent |
| **1** | the two stand equal — the corner |
| **∞** | the denominator has gone absent |

The expression has two:

| expression | what it is |
|---|---|
| **1** | the limit: the full shape, every perturbation expressed — sweeping the shape |
| **0** | no expression: the unit circle alone — browsing the circle (rulings 4, 9) |

**And a freedom is finite in extent and infinite in density.** Its whole run is a quarter turn; what has no end is how many addresses that turn carries, crowding toward the horizon.
Nothing is added to a freedom — magnitudes are hung on it, and the horizon is where no further
hanger can be hung (§5.16).

---

## 2. Freedoms sharing a denominator

Freedoms are comparable when they are read against the same held value: s₁ = v₁/h, s₂ = v₂/h, s₃
= v₃/h. That is what one register means, and it is the only way a reader with one register can
have more than one freedom at once.

**Each can be read on its own; none can be moved on its own.** Hold 1, 2, 5 in turn and the
readings run 3, 4, 12 → 1.5, 2, 6 → 0.6, 0.8, 2.4 while the proportion 3 : 4 : 12 never moves.
One denominator is the only handle, and it moves all of them together.

---

## 2.1 A freedom and its magnitude list

**The list is produced, not given** (ruling 11): what follows is the list a generator returns once a g is
named, and §2.2 says what may do the generating. Everything below holds at every g.

**A freedom points at a list of magnitudes, and every magnitude in the list is a point on the
freedom.** The two are not the same kind of object, and they behave oppositely as the list grows
(`density.mjs`).

**The list grows in size.** Ten items, a thousand, a thousand million — each addition makes it
longer and its span wider, and nothing bounds it.

**The freedom does not grow at all.** Address each item against the list's own hold and the
addresses run from 1/n to 1 for every n. The two ends do not move. **A freedom has the same
extent for ten items as for a thousand million.**

**What changes is the spacing:**

| items | gap between neighbours | addresses per unit |
|---|---|---|
| 10 | 0.1 | 10 |
| 1,000 | 0.001 | 1,000 |
| 1,000,000 | 0.000001 | 1,000,000 |

> **The list grows in size; the freedom grows in density.** Same items, two behaviours: one
unbounded
> in extent, the other unbounded in fineness.

**And the boundedness comes from where the hold is drawn.** Address the same list against a
*fixed* hold instead and the readings run 1 … n and away with it — magnitudes wearing a ratio's
clothes. **A freedom is bounded exactly when its denominator is drawn from the same thing its
numerators are.**

**And the freedom has a unit while the list does not** (*The Boundary* §11.3, B50). The two sides
here are a base and a fibre — the freedom is the base, the magnitude list the fibre, and the division
is the projection between them. A unit can be named on one side and not the other, and the asymmetry
is total: four pairs eight orders apart — (3, 3), (0.7, 0.7), (418.2, 418.2), (10⁻⁶, 10⁻⁶) — give
**the same reading every time**, so no magnitude in the list is nameable as *one*; but that reading
is 1, and 1 is **the corner**, which the reader places with no total and no reference (*The Boundary*
§7.2). So a freedom carries exactly one number of its own.

> **A freedom has a unit; its magnitude list has none.** The corner is that unit, and it is why the
> series has always measured from there rather than from either end.

⚠ This corrects a flat reading of "the reader has no unit" that this series has used. The right
statement is *no unit for the magnitudes it divided away* — those are the ones a bulk has.

**And a magnitude past the ceiling is not dropped — it folds.** A perturbation finer than the hangers can
carry lands on the hanger at its folded position and adds to whatever is there, so too few hangers are paid
for by the ones that exist (§1, ruling 9).

**⚠ And the grain is a step in TURN, not in address** (Tom, Sep 19; *The Boundary* §9.5, B59). The
ruling: **at g = 0 no hangers are placed, at g = 1 all N are, and at g = 1 the grain perfectly
coincides with N hangers.** That last clause sorts the grain, which this paper had left unsorted. The
hangers are the same width in turn — π/2N at every one — and wildly different in address: at N = 6
they run 0.268, 0.309, 0.423, 0.732, 2.000, ∞. So an address-even grain cannot coincide with them at
any step size (a grain of 0.3 lands 1, 1, 2, 2, **7**, 1), and a turn-even grain of π/2N lands exactly
one per hanger. **The grain belongs with the aperture on the pointing side.**

**And it makes g = 1 detectable from inside, though g is not** (B60). At g = 1 every resolvable step
holds exactly one hanger — no step empty, none doubled — and both sides of that test are counts. The
ratio filled/total *is* g, but reading it needs the total, and §5 is explicit that the observer never
has N. **At g = 1 no division is needed:** every step it has is filled, checkable without knowing how
many there are.

> **g = 1 is the one value of g a reader with no total can detect.** It cannot say how much is
> expressed; it can say whether all of it is.

**⚠ Built and tried to break, and it comes back narrower** (B93–B96). The reader's whole method uses
nothing it does not have: take the arrival turns, take the **smallest gap between neighbours** — the
finest step it has evidence for, since nobody told it the spacing either — and ask whether every gap
is that step. At N = 64 the verdict is right at every g tried, including **0.98**: one hanger missing
out of sixty-four makes one gap exactly twice the step, so the test is **exact rather than
statistical**, and over 400 random thinnings at each of seven values of g the false-complete rate is
zero. It also reports **how many steps are missing and where the first gap is**, still without a
total.

**And the count on its own is worth nothing.** Thirty-two hangers is *32 of 32 at g = 1*, or *32 of
64 at g = 0.5*, or *32 of 256 at g = 0.125*; the reader sees the same count in all three, and what
separates them is the finest step — precisely what the test reads. The one recoverable thing is the
one thing returned.

**⚠ But the test does not detect g = 1.** A regularly thinned set has no gaps: every second of 64
slots is a perfect lattice at twice the step, every fourth at four times, and both pass. What it
detects is *no gaps at the finest step I have evidence for* — **completeness relative to the reader's
own inferred grain.** That is not a defect to patch but this section's own position arriving
uninvited: fullness is fullness *against a grain*, a reader with a coarser grain **is** full because
evidence is all it has, and to call that wrong is to smuggle N back in.

**And this is what g means from inside** (Tom, Sep 19): *at a grain of 0.5, only 50% of the hangers
have been hung — the reader must **step over** 50% of them.* A partial expression is not a faint
signal or a blurred one; it is a **full-strength signal with holes in it** — `|.|.|.|.` at g = 0.5,
`|||.|||.` at 0.75. **g is how often the reader finds something when it looks**, which is a better
account than "how fully the signal is expressed" and says what is actually met.

⚠ **The name, though, is taken.** "Grain" is this paper's word for the reader's step, and the two are
separable: half hung at a fine step (8 sites, 4 hung) and all hung at a coarse step (4 sites, 4 hung)
both leave a reader holding four magnitudes, but the first has **four gaps** and the second none, and
their bands differ. **The step sets how many bands there are; g sets how many hold anything** — two
parameters, four situations. The reading is adopted here; the rename is left open.

**Density has a ceiling, and it is the reader's.** Two addresses closer together than a reader's
own step are one address to it, so a grain of 0.1 distinguishes ten, 0.01 a hundred, 0.0001 ten
thousand. The list may grow without limit and the freedom may grow dense without limit; **what a
reader has of either is set by its grain** — the quantity *The Radix* measures, arriving here as
the ceiling on density.

**And the packing is not even.** Where the far items crowd toward the end, the last gap closes
faster than the addresses accumulate: at ten items the final gap is 0.0091, at a hundred
0.000099, at ten thousand 0.00000001. The end is approached and never arrived at, which is
**what a horizon looks like when the list is long — not a wall, but an accumulation.**

## 2.2 What generates a list

**A generator is anything that returns magnitudes when given a direction and an expression.** Write it
r(u, g), with r(u, 0) = 1 for every u. That is the whole requirement, and it is deliberately indifferent to
what the thing is:

| species | what it is | where the corpus has one |
|---|---|---|
| **an equation** | a formula in u and g | the octave and harmonic toys of *the path, formally* §0 |
| **a shape or outline** | a figure met by rays from a centre | `svg.html`'s PRIMITIVES; the reading button of `svg-inline.html` draws exactly this — each direction one address, meeting the shape where it first crosses |
| **an algorithm** | a procedure computing a magnitude on demand | the self-affine ladder the shape page browses at 2⁵³ directions; `vcp-core.js`, which places 2⁵³ of them and is in working applications |
| **a table** | stored magnitudes, with an interpolation | any recorded outline; the list is the table read at the expression its sampling affords |
| **a physical object** | met by an instrument at a standoff | every real reading the series has taken; here g is the station |

**The species does not enter any result in this paper.** What enters is two properties.

⚠ **And these definitions now have an executable form**, which is worth saying because it changes what a
disagreement costs: `freedom.js` implements a freedom, a generator, the expression and the two readings,
and its checks hold rulings 9 and 11–13 to the digit — at g = 0 every generator is the circle to 0.0, a
lobe is absent below its own g and at full amplitude at it to 1.1e−16, the two-component reading is tan u
at every g to 2.8e−16 while the hold-following reading moves. **A ruling that cannot be made to run is a
ruling that has not been stated precisely enough**, and three of these were not until they were.

**First, whether it is algorithmic.** A generator is *algorithmic* if r(u, g) can be had in work bounded by
its rung count, from u and g alone — without computing another direction, and without computing a smaller
g. It is *pathological* otherwise: when the value at g is reachable only by passing through the values
below it. Measured on four toys (`path_checks_g.mjs`): one value costs **1, 3, 7, 13, 19, 25** terms at
g = 0, 0.1, 0.25, 0.5, 0.75, 1 — the rung count and nothing else, the same for every direction tried. A
generator written to be pathological costs **129 steps at g = 0.5 and 257 at g = 1**: its price is the g
below it, not the g asked for. **For a pathological generator g is not a dial but a stopping rule**, and a
reader cannot say which g it is at.

**Second, its amplitude law, which is its own and not the reader's.** What a reader gets is the generator's
law seen through the reader's band, and mistaking one for the other is easy: measured, amplitude ∝ period^α
gives a response with arms α and α − 2 (ruling 13). A self-affine list, α = 1, gives the symmetric halving
per octave that looks like a property of reading and is a property of the list.

**Third, whether its orders sit in the reader's own ratio.** *The Radix* settles this and the result
transfers without change: a scale-free reader's ladder is a ladder of ratios, its pitch is its own grain,
and one rung selects one level only where the list's pitch matches. Applied to expression — a rung being a
doubling of the arrivals, the dial's grain being ln 2 — levels gained per rung, measured by walking:

| the list's orders | rung 4→5 | 8→9 | 12→13 | 16→17 | |
|---|---|---|---|---|---|
| harmonic, n = 1, 2, 3, … | 8 | 128 | 2,048 | 32,768 | slides |
| **octave, n = 1, 2, 4, 8, …** | **1** | **1** | **1** | **1** | **matched** |
| every third, n = 3, 6, 9, … | 3 | 43 | 683 | 10,923 | slides |

**The octave list is the matched radix of the expression dial.** A harmonic list is not unbrowsable, but a
reader walking it crosses thirty-two thousand of its orders in one rung, so moving through it level by
level needs the schedule supplied from outside — and ruling 9's own threshold, g ≥ (2n+1)/N, *is* that
table: arithmetic in n, against a reader that is geometric. **That is The Radix's bill, arriving in the
expression machinery: uniformity can be free, variation is paid for by the reader's grain or by
information handed to it.**

**And expression arrives in whole rungs, though g is continuous** — because a hanger is a whole thing:
the count gN slides smoothly and what the count can carry does not. A generator carrying one rung of
twenty-four is *exactly* the circle until g = 7/24 = 0.2917 and has its full swing above it — nothing
fades in (ruling 9's levels, checked as L0f).

### Injecting scale into the unit circle

A generator can be built rather than met, and there is exactly one way to build one.

**Proposition.** Let r(u) > 0 be star-shaped about the reader, continuous and of bounded variation. Then
r(u) = a₀·(1 + Σ_{n≥1} c_n cos(nu + φ_n)) with a₀ > 0 and the list (c_n, φ_n) determined uniquely by r,
the series converging uniformly. **So every such figure is the unit circle with two things injected: one
number that is the scale, and one magnitude list that is the shape** — the circle being the case where the
list is empty. Scale and form separate cleanly: a₀ carries the size and nothing else, the list is unitless.
⚠ The list is unique **at full expression only**; below it just the truncation is fixed and many lists
share it, which is ruling 9's fold with its reason — uniqueness lives in the whole series, not in a partial
sum.

⚠ **And the path through g can leave the class of figures.** Hung on the radius, a partial sum of a figure
that comes close to the reader goes through zero: measured, the grazing figure 1/(1.15 + cos u) reaches
min/mean **−0.1642** and is not a figure from g = 0.0117, and a knife of least extent 0.06 reaches −0.0514
at the same g. **At those expressions the radius is negative somewhere and the expressed thing is an
outline turned inside out** — so "every intermediate g gives that generator's honest values" (ruling 11) is
false as stated for figures near the reader, and this paper's own escape hatch (§8, item 12(a); the
uniqueness theorem's) shows up here in a second guise.

Hung on the **log radius** instead — ln r = ln a₀ + Σ… — positivity is automatic at every g and the same
figure returns at g = 1 (agreement 2.7e−15 ellipse, 5.4e−15 star, 1.3e−6 knife); the grazing figure's worst
point moves from −0.1642 to 0.2281 and the knife's from −0.0514 to 0.1166. The cost is at hinges, where a
corner in r is a corner in ln r too: the square, exact in the radius form, is 5.0e−3 out in the log form at
127 lobes. **A trade, not an improvement, and not yet ruled** (§8, item 14(d)). What is not optional is
that a list must say which coordinate it was hung in, since the same coefficients are different figures in
the two.

**What none of this changes: the address.** For any generator and any g, the two-component reading gives
v/h = tan u, because the magnitude stands in both terms and cancels. Measured across four generators and
six expressions, the largest departure is **4.3 × 10⁻¹⁶** — the address streams at g = 0 and g = 1 are the
same stream. **So g decides which values the reader met and none of what it says about them.** Where g does
show is any reading that keeps a magnitude rather than a ratio, and the hold-following reading, which keeps
consecutive proportions: there the same measurement moves by **1.3 × 10⁻²**, thirteen orders of magnitude
away from the ratio's noise floor.

---

## 3. How they compose, and what happens to the denominator

**Two freedoms compose by division, and the composite is another freedom** (`compose.mjs`):

> **c₁₂ = s₁ / s₂**

And the thing worth noticing is what drops out. s₁/s₂ = (v₁/h)/(v₂/h) = v₁/v₂ — **the shared
denominator cancels.** Composed against H = 1, 7 or 1000, c₁₂ reads 0.75 every time and c₂₃
reads 0.333333 every time.

> **The denominator is what makes two freedoms comparable, and it is absent from the result of
> comparing them.**

So a reader that holds one value to make its freedoms comparable finds that the comparison it
then performs does not depend on which value it held. The register is spent on making the
composition possible and takes no part in it.

**And that gives the denominator a better status than *a nuisance that cancels*.** It is required to
form the reading and absent from the result — **constitutive but non-retentive.** Said the other
way round:

> **A freedom is made possible by scale and made scale-free by division.**

You cannot form s without v and h; both are magnitudes, and the address cannot be had without
them. Then λv/λh = v/h, and the scale that made it possible is gone from it. **The interesting
part is not that something disappears. It is that the thing which disappears had to be there
first** — a reading with no magnitudes behind it is not a scale-free reading, it is no reading.

### 3.1 The centring

The Romans built an arch on a wooden frame. Every stone rested on the centring while the ring
was being closed, and the frame carried the whole weight until the last stone went in. Then it
was struck, and taken away, and the arch stood — on nothing but the stones, which had never
touched the ground.

**The denominator is the centring.** It is what lets two readings bear on each other while the
comparison is being made, and it is not in the result. The test is the one a centring has to
pass: *the finished thing must not depend on which frame was used.* Compose the same two
freedoms against four different holds —

| the hold | s₁ | s₂ | s₁ / s₂ |
|---|---|---|---|
| 1 | 3 | 4 | **0.75** |
| 7 | 0.428571 | 0.571429 | **0.75** |
| 1000 | 0.003 | 0.004 | **0.75** |
| 0.004 | 750 | 1000 | **0.75** |

— four different scaffolds, four different pairs of readings, and one arch every time.

**AND SINCE SEP 18 THIS IS NOT AN IMAGE** (Tom's ruling, taken up in *The Centring*). The circle is
not *like* a falsework; it **is** one, and the three parts of a building are three parts of a
reading with nothing left over:

| building | reading |
|---|---|
| erecting the frame — the places where stones will rest | naming **g**, which places the hangers: a count of places, and they are empty |
| laying the stones on it | the **magnitudes**, hung on those places — **this is where scale enters, and it never comes from g** |
| striking it: the arch stands, the frame is gone | **dividing**: the hold bears the weight while the reading forms and is absent from what it composes to |

⚠ So g and scale are two separate acts and neither does the other's work. **g places empty
hangers.** Place all N of them and hang nothing and there is still nothing to read: a complete
frame and no figure. Whatever hangs brings the size with it. (An earlier draft of this paper said
the first hanger is where a magnitude can first *exist*; that was wrong — it is where one can first
be **hung**.)

**And the arch is the semicircle.** The image is not borrowed from masonry and laid over geometry:
a Roman arch is a half turn, and so is the address space, since the tangent repeats every π — the
mason's falsework and the reader's are one figure. **A span shorter than a half does not close and a
full circle has nothing to stand on**, so a half is the smallest thing that closes and carries, which
is a structural reason for the half turn sitting beside the trigonometric one. **And the keystone is
the corner**: two freedoms meet in the middle, and that stone's place is fixed by both at once — the
only one that can be set without measuring from either springing, which is why a reader with no unit
can find it and why after it goes in the two spans are one structure. ⚠ An arch also needs its feet on
something, and what the reader's span rests on — the next freedom along, or nothing — is not settled.

**And this falsework differs from a mason's in two ways**, which are now properties of it rather
than places an image breaks down. A centring is struck once and the arch stands for good; a hold is
not, and has to be re-erected for every comparison, because two freedoms never held against a common
denominator cannot be composed at all — so **the arch never stands on its own**, and every magnitude
a reader holds rests on a frame that has to go up again to hold it. And a frame can stand with
nothing on it, which a mason would call a wasted afternoon and which here is a real state: the
circle, complete as a frame and empty as a figure.

*The test is offered to the series rather than to this paper alone: wherever something is required
to build a structure and absent from the structure — vary it, and see whether what was built moves.*

---

## 4. What a set of freedoms generates

Three freedoms have three pairwise composites: c₁₂ = 0.75, c₂₃ = 0.333333, c₁₃ = 0.25. And **c₁₂
× c₂₃ = c₁₃** exactly, so only two of the three are independent.

> **n freedoms sharing a denominator generate n − 1 independent composites.**

The composition is multiplication of addresses, and it brings its own structure with it:

| | |
|---|---|
| **composition** | c₁₂ · c₂₃ = c₁₃ — associative |
| **identity** | c = 1: **the corner**, where two freedoms stand equal |
| **inverse** | 1/c: the same relation with the parties swapped |

**The unit of the structure is the corner.** That is not put in; it is what an address has to be
for composing with it to change nothing. Nothing about what any freedom addresses was used to
reach it.

---

## 4.1 The other cancellation, and why one seat cannot have it

§4 found that dividing two freedoms cancels their shared denominator. That is half the law, and
the other half is easiest to reach through a case where the missing half is felt as a
contradiction.

**Two friends at opposite ends of a field.** Each looks at the other and sees someone small —
much smaller than their own hand at arm's length. Both are being perfectly accurate. Written
down, A says *B is smaller than me* and B says *A is smaller than me*, and those two sentences
cannot both be true.

**Nothing went wrong in the field.** What went wrong is that each read is a fraction — the
other's apparent size over one's own — and the two fractions have **different denominators**,
each private to its seat. Writing them on one number line deletes both and silently supplies a
replacement, because every number on a line shares that line's unit. *Smaller than my ruler*
becomes *smaller, period*, and the contradiction is manufactured in the notation — by a tool
with no slot for the thing that was lost. The companion piece, `denominator_paradox.md`, follows
the same shape through relativity's reciprocal clocks, Simpson's paradox and the prosecutor's
fallacy; this section takes only what it needs.

**The numbers.** A reads 0.088889, B reads 0.1125, and each read is made of the same two parts
differently arranged: the **shared** part sits the same way up in both, and the **private** part
sits one way up in A and the other way up in B (`exchange.mjs`).

| | what cancels | what comes out |
|---|---|---|
| **divide** the reads | the shared part | √(rA/rB) = 0.888889 — the true size ratio, exactly |
| **multiply** them | the private parts | √(rA·rB) = 0.1 — the true distance factor, exactly |

> **Dividing cancels what the two seats share; multiplying cancels what is private to each.**

**And the product carries a condition the quotient does not.** Two freedoms against *one*
denominator multiply to v₁v₂/h² — 0.244898 in the running example — and the denominator has not
gone anywhere. The product recovers a shared part only when the two reads are **reciprocal in
the private part**, which is what happens when they are the same relation read from two seats:
the party swap of §1.

**Which has a consequence worth stating plainly.** The quotient is available to one reader: it
needs two freedoms it already holds. The product is not, because it needs **both reads** — one
from each seat — and therefore an exchange between them.

> **One seat can divide its own freedoms; the reciprocal cancellation takes two seats.**

(The slogan invites a cheap objection in its shorter form: of course one seat can multiply two
numbers. What one seat cannot do is perform *this* cancellation, which needs two reads whose
private parts are inverted with respect to each other.)

The second cancellation is exactly what this series prices as a second reader, arriving here as
arithmetic rather than as a purchase argued for.

**And the paradox and the price are the same fact.** The contradiction in the field was not a
discovery about the world; it was two private denominators put on one line. The repair is not an
argument either — it is a phone call. *Who is really bigger* has a definite answer, and the
answer costs an exchange, which is why no seat could have had it alone. **A denominator paradox
is the shape a missing purchase takes when it is mistaken for a fact.**

## 4.2 The unit circle and the unit sphere are freedoms sharing a hold

> **(1 Oct)** The circle is situation 1. Its normalisation by the pair's own size stands; the corner and home placed on it do not, since situation 1 has neither (R139).

Everything above has been written without borrowing anything. It is worth showing what it looks
like in the notation everybody already has, because the answer is not a new object — it is a
familiar one, read differently (`unit.mjs`).

**Two freedoms, and the hold they share.** Take two extents, 3 and 4, and let the hold be the
pair's own size, 5. The two readings are **0.6 and 0.8** — which every reader of trigonometry
has met as **cos θ and sin θ**. They are not new. What is worth saying is what they *are*: two
freedoms sharing one denominator, and the denominator is the pair's own size.

**And the identity everyone knows is the receipt.** cos²θ + sin²θ = 1 is usually read as a fact
about lengths on a circle. As addresses it says something plainer:

> (v₁/h)² + (v₂/h)² = (v₁² + v₂²) / h² = 1 — **exactly when h is the shared hold.**

**The Pythagorean identity is not a law about sizes. It is the statement that the two readings
were taken against the same denominator**, and that the denominator was their own combined size.
It is the receipt of §0, written as an equation.

**The scale is gone, which is what makes them addresses.** Multiply the extents by 1, 7, 0.01 or
1000 — (3, 4), (21, 28), (0.03, 0.04), (3000, 4000) — and the point reads (0.6, 0.8) every time.
**cos and sin do not carry a magnitude; they address one.** The *unit* in *unit circle* is not a
size: it is the denominator having been divided out, and the 1 is what is left of it.

**And the composite of the two is the tangent.** s₂/s₁ = 1.333333, and v₂/v₁ = 1.333333 — the
same, with h nowhere in it. **tan θ = sin θ / cos θ is §3's composition law in the usual
letters**: divide two freedoms and the shared denominator cancels. Which is why the tangent is
the reading this series keeps — it is the one that needs no hold at all.

**Three freedoms, and the same sentence one step up.** Extents 3, 4, 12 against a hold of 13
give 0.230769, 0.307692, 0.923077, and their squares sum to 1. Those are the **direction
cosines**, and the sum is 1 for exactly the same reason: one hold, three readings.

> **The unit circle and the unit sphere are not shapes a reader measures. They are what two or three
> freedoms look like once they share a hold** — and every point on them is an address to a magnitude
> that was spent putting it there.

### 4.3 Where the unit is — and why it is a quarter turn, not a circle

The section above used the pair's **own size** as the hold, and that choice does more than it
looks (`where.mjs`). Two cases have to be told apart.

**Case A — no unit brought.** The denominator is the arrival's own size. Then (3, 4), (6, 8), (1.5,
2) and (30, 40) all read (0.6, 0.8) at radius 1: **everything lands on the circle by construction**,
the circle carries direction only, and the size was spent putting it there. Four arrivals, one
point. That is §4.2 as written.

**Case B — a unit laid down at home.** The denominator is the hold — the stick the reader
carried and put down. Then the same four arrivals read (0.6, 0.8), (1.2, 1.6), (0.3, 0.4) and
(6, 8), at radii 1, 2, 0.5 and 10. **They no longer all land on the circle**, and the radius
they land at says something: under 1 is smaller than what I laid down, over 1 is larger, and
exactly 1 is the same.

> **The unit circle is the locus of arrivals that read the same as the hold.** It is not an
> abstraction drawn at a convenient distance. **It sits at the laid-down unit** — it passes through
> the end of the stick, and the reader can point to it.

**And *circle* is the wrong word for what one freedom spans — but so, strictly, is *quarter turn*,
and the difference matters.** Three things are in play here and they are not the same object:

| | |
|---|---|
| the **freedom** | the ratio space [0, ∞). This is primary, and §§1–4 use nothing else |
| its **angular parametrisation** | s = tan u, which spans a quarter of a turn. A *realisation* of the freedom, not the freedom |
| the **signed copies** | four of them, which is what closure needs (§5.1) |

**The ratio space is [0, ∞); its tangent parametrisation spans a quarter turn.** That is the careful
form, and it is weaker than *a freedom is a quarter turn* in exactly the way it should be —
because the angle is **borrowed**. A reader with one register, one arrival and a ratio has no
arctangent; an angular reading is a purchase, like a unit or a second register. So π/4 and π/2
below are descriptions from outside, not readings anyone takes.

With that said, the parametrisation shows the shape of the freedom clearly:

| | |
|---|---|
| s = 0, V absent | u = 0 — one end |
| s = 1, V equals H | u = π/4 — **the middle** |
| s = ∞, H absent | u = π/2 — the other end |

**So the laid-down unit sits at the middle of the quarter, not at an edge of it.**
Everything smaller than the hold is in the first half — 0.5 of the hold reads at 29.5% of the
quarter — and everything larger is in the second, with 2 at 70.5%. The two ends are the two
absences.

**And a smaller hold is a smaller radius, not a smaller freedom.** The quarter is always a quarter —
π/2 of turn, whatever was laid down — and what the hold sets is the *radius*, which sets the arc
that quarter occupies:

| radius | span | arc | distinguishable addresses | per unit arc |
|---|---|---|---|---|
| 10 | π/2 | 15.708 | 157 | 10 |
| 1 | π/2 | 1.5708 | 157 | 100 |
| 0.1 | π/2 | 0.1571 | 157 | 1,000 |
| 0.01 | π/2 | 0.0157 | 157 | 10,000 |

**The span never changes and the count never changes.** A grain of σ gives the same 157
distinguishable addresses at every radius, because the grain is a step of *angle* and the angle
is always a quarter. What changes is how tightly they sit: **density goes as 1/r.** Shrink the
hold tenfold and the same addresses pack ten times closer.

> **A freedom never grows in size.** Whatever is done to it — a longer list, a smaller hold, a sweep
> further out — **it answers in density.** That is what it is to be an address space rather than an
> extent, and §2.1 said the same thing from the list's side.


**A circle takes four of these**, which is the closure count of §5.1 exactly: four signed
cases, four quarters, 2π. So the picture to keep is not a circle with the reader at its centre.
**It is a quarter turn with the laid-down unit at its middle and a horizon at each end** — and
four of those, back to back, are what a closed shape is.

The corner, where V and H stand equal, is a point of *that* circle and of no other.

**And the difference between the two cases is a purchase.** A reader that brought nothing has
direction and no size: the denominator came from the arrival, so the radius is 1 by force. A
reader that carried a unit from home has direction **and** size, because **a laid-down unit buys
back the radius** — and the price was the journey that brought it, which is what this series
charges for a unit everywhere else.

### 4.4 A moving hold, and a new circle at every reading

If the circle sits at the laid-down unit, then **a reader that changes what it holds moves its
circle**. And a reader with one register changes it constantly: walking a list, the only thing
it can keep is the last thing it saw, so each arrival becomes the next hold (`moving.mjs`).

**Then the circle is re-laid at every step.** Reading the list 2, 3, 12, 6, 30 that way
gives holds of 2, then 3, then 12, then 6 — four readings, four circles, each erected for one
reading and struck for the next. **It is the centring of §3.1, put up and taken down once per
arrival**, rather than a frame the reader keeps.

**And the composition law turns over.** With a fixed hold, dividing two readings cancels what they
share. With a moving hold, every intermediate value appears once above the line and once below:

| | |
|---|---|
| the readings | 1.5, 4, 0.5, 5 |
| their **product** | **15** |
| and v_last / v_first | **15** — the same |

> **With a fixed hold the quotient composes; with a moving hold the product does.** Divide to cancel
> what the readings *share*; multiply to cancel what they *pass through*.

Which is §4.1's pair of cancellations arriving from the other direction — and it says why a
serial reader multiplies where a seated one divides.

**What the moving reader keeps, and what it loses.** It keeps the whole chain in one number.
It loses every intermediate, and the loss is total: walking 2 → 3 → 12 → 6 → 30 and walking 2 →
60 → 30 both give 15. **The product is blind to the path.** That is what makes it a relation
between the ends rather than a record of the journey — and why a reader that wants the journey
has to count as well as divide, which is the other instrument again (§5.5).

### 4.5 The two are one structure

§4.1 found that dividing cancels what two readings share while multiplying cancels what is
private to each, and §4.4 found that a fixed hold composes by division while a moving hold
composes by multiplication. Two structures that resemble each other, or one seen twice? **One**
(`onestructure.mjs`).

**A moving reading is a composite of fixed ones.** With readings 0.4, 0.6, 2.4, 1.2, 6
against a hold of 5, the moving readings are 1.5, 4, 0.5, 5 — and each of those is exactly a
quotient of two fixed ones: 1.5 = s₁/s₀, 4 = s₂/s₁, and so on. **The moving structure is not a
second structure. It is the fixed structure's own composites, relabelled as readings.**

**Which is why its composition is multiplication.** If rᵢ = sᵢ/sᵢ₋₁ then a product of consecutive
readings telescopes: 1.5 × 4 × 0.5 × 5 = 15, and s₄/s₀ = 15. **Multiplying the moving readings
is dividing the fixed ones at the two ends** — one operation, seen through the relabelling as
the other.

**And the landmarks agree because they are the same landmarks.** The fixed identity is c = 1, two
freedoms standing equal; the moving identity is r = 1, an arrival equal to the last, which is no
change. Both inverses are reciprocals: parties swapped, or a step taken backwards.

**The only difference is what is kept, and that is not structural.** A fixed reader holds every
reading against one hold and can form any composite at will. A moving reader holds the
composites and has thrown the readings away, which is why its product gives the two ends and
nothing between (§4.4).

> **One structure. Dividing readings gives composites; multiplying composites gives composites
> further apart. Whether a reader divides or multiplies says which of the two it is holding.**

## 5. Examples, and the one that uses this arithmetic exactly

The definition is abstract on purpose, but it is not empty, and most of what this corpus reads
turns out to satisfy it (`examples.mjs`). The test is three questions: is it formed as one thing
against another, is it unchanged when both are scaled, and does it address rather than value?

**The Cauchy is a freedom, and it uses this arithmetic exactly.** *The Cauchy* states it in its
own words before this vocabulary existed: a reader with no outside unit states **ratios** — the
arrival against the hold, one number per reading — and the ratio is unbounded with **one horizon
at each end of every passage**. That is [0, ∞) with its two ends, reached independently.

**And it supplies §4's inverse without being asked for it.** That paper notes that exchanging
the two parties turns the ratio into its **reciprocal**, an involution the reader must apply.
That is 1/c — the inverse of the composition law — named there for other reasons entirely.

**The correspondence goes further than the shape.** If the facing behind a ratio is flat, the
ratio is not: it is Cauchy. Sample it and read the quartiles of its magnitude — **0.4142,
1.0000, 2.4142**.

- the median is **exactly 1**: the corner, which is §4's identity;
- the quarter-points are **an inverse pair**: 0.4142 and 1/0.4142 = 2.4143.

**The distribution's own median is the composition law's identity, and its quartiles are an
inverse pair.** Two facts about a density and two facts about the structure freedoms compose
into, and they are the same two facts.

**Others in the corpus, by the same test:**

| | formed as | |
|---|---|---|
| a reader's **radius** | how much of a list is in reach, against the whole | a proportion of a list |
| the dial's **record** | a position against the list's length | and the length cancels |
| an **arrival against a hold** | the Unit Rule's one operation | the definition itself |
| a **grain** σ | a step against the value it steps on | which is why it sets a ratio, e^σ |
| a **height** in the city | standoffs, against the standoff | the standoff is the shared denominator |

**And one thing that is not a freedom**, which fixes the boundary. A **count** of arrivals is an
integer, and seven arrivals is not seventy scaled down — scaling changes it, so it does not
address. Counting is this corpus's other instrument and it is not of this kind, which is why a
winding number sat so oddly in earlier work: **it counts, it does not address.**

**And the non-freedoms have now been censused** (*The Boundary* §9.2, B36). This paper has named one
count; there are at least four, each real information about the reader that Definition 4.1 rules out
of being a freedom:

| the count | what it tells the reader | what it costs beyond the integer |
|---|---|---|
| **parity** | whether it stands in material or a hole | nothing |
| **the size** of the reading, beyond its parity | whether the single-valued case is in force | nothing |
| **which magnitude is underneath** | which way round its own hold is | a monotone turn |
| **the lap** | how many times round it has watched | an unbroken watch |

The winding number is the third row's neighbour — it is the **lap**, and the census says why it sat
oddly and what it costs. tan has period π, so a turn and that turn plus a half-turn are *the same
address, exactly*: the address line is the circle modulo a half-turn, and the lap is simply not on
it. A reader recovers it by counting passages through the horizon, and only if it never looked away.

**⚠ And the cost column is the result, not the membership.** Two of the four cost nothing beyond the
integer and two cost something the reader cannot supply from inside: a *completed* condition — "the
turn is monotone", "I never looked away" — each a statement over a totality it does not hold. So a
count is free the way arithmetic is free, and what it actually needs is an uninterrupted relation to
the world, which is the thing a serial reader is least able to guarantee.

**One more, and it is in neither instrument.** Four distinct arrivals and one arrival met four times
give the *identical* addresses and the *identical* count — so neither addressing nor counting
separates them. That fact has no location: there is no arrival, no pair, and no subset where the
missing information would sit. **Addressing is per-reading and counting is per-element; both are
local, and a fact with no location defeats both at once.**

## 5.1 Three worked examples, in the order they are met

The examples above pass the definition; these three are set out in full, because a later paper
will propose that they are the degrees of freedom of the space a person actually moves in.
Nothing here argues that proposal. It only says what each freedom is, what its two ends mean,
and what it costs.

### The first: the Cauchy, also called the fisheye — an address to a centre of gravity

**What it is.** One thing read against another, with no outside unit: the arrival over the hold.
*The Cauchy* states it in those words — a reader with no outside unit states **ratios**, one
number per reading, and the ratio is unbounded with one horizon at each end of every passage.

**What it addresses.** Not the size of the thing read, which was spent making the reading
scale-free, but **where the thing sits relative to the reader's own hold** — its centre of
gravity in the reader's own terms. Everything about the thing's magnitude is gone; what survives
is a position in [0, ∞).

**Its two ends and its middle.** Nought where the numerator goes absent, infinity where the
denominator does, and **one** where the two stand equal — the corner, which §4 finds again as
the identity of composition. The Cauchy's own median sits exactly there, and its quartiles,
0.4142 and 2.4142, are an inverse pair.

**What it costs.** One register: the held value. It is the cheapest freedom there is, and the
only one a reader has without buying anything.

**It is also called the fisheye, and the two names are one thing.** *Cauchy* is the formal term —
the distribution's, used for statistics and citations. *Fisheye* is the visual one: it names
what the same freedom looks like rather than what it measures as.

**Deriving it from V and H, with nothing else** (`fisheye.mjs`). A reader holds H and takes V, so
its address is s = V/H. Now lay the readings out at equal steps of **the reader's own movement**
— which is the facing, not the address. With H held, a facing of u puts the arrival at V = H·tan
u:

> **s = V/H = tan u** — the address, as a function of the reader's own step.

Take equal steps in u and see where they land:

| step u, as a fraction of a quarter turn | address s | gap from the last |
|---|---|---|
| 0.1 | 0.1584 | 0.1584 |
| 0.5 | 1.0000 | 0.2735 |
| 0.8 | 3.0777 | 1.1151 |
| 0.95 | 12.7062 | 6.3925 |
| 0.99 | 63.6567 | 50.9505 |

**Equal steps of the reader land unevenly on the address** — close together near the middle, flying
apart toward the end and never arriving. **That uneven landing is the fisheye:** fine near the
hold, coarse far from it. Backwards it says the same thing: addresses 1, 10, 1000 and a million
sit at 0.5, 0.9365, 0.9994 and 0.999999 of the reader's range, so **the whole infinite far end
is squeezed into the last sliver. A bounded reader holds an unbounded list by crowding it.**

**And that is why the fisheye is the Cauchy.** Let the reader's own step be uniform — every facing
as good as every other, which is what *no facing preferred* means — and push it through s = tan
u. The density on the address is 1 / (π(1 + s²)): the Cauchy, with its median at the corner and
its quartiles an inverse pair. **The fisheye is what the uneven landing looks like; the Cauchy
is what it measures as.** Both are V/H with the reader stepping evenly in its own facing.

**The name earns itself.** A fisheye lens does this to a scene — the middle spacious, the edges
compressed, the rim never reached — and the address space has that shape for the same reason:
the hold sits at the middle, and everything far from the hold is far in the *reading* before it
is far in the world.

**And it has relatives.** The fisheye is the two-pole logarithmic map with its poles at ±i — one
member of a family that also holds the map from visual field to cortex. §7.4 sets the family
out, and §7.5 says for which world the fisheye is the efficient code. **§5.15 says what it
does in each of the two situations a reading can be in** — a stream met one value at a time, and
data held whole.

**And the crowding buys something at the other end: perfect fidelity where the reader stands.** A
step du of the reader lands as sec²u · du on the address, so the stretch is:

| u, as a fraction of a quarter turn | address | stretch |
|---|---|---|
| **0** | 0 | **1.0000** |
| 0.01 | 0.0157 | 1.0002 |
| 0.25 | 0.4142 | 1.1716 |
| 0.5 | 1.0000 | 2.0000 |
| 0.9 | 6.3138 | 40.8635 |
| 0.99 | 63.6567 | 4053.18 |

**At the hold the stretch is exactly 1** — not nearly, since sec²0 = 1 — so a step of the reader
lands as a step of the same size on the address. **The fisheye is undistorted at the hold and
nowhere else.** The reader lays its unit down at home, and what it keeps for that is fidelity:
near itself, what it reads is what is there. Everything it pays for that is paid far away, where
a step of the reader covers forty addresses and then four thousand.

**And its unit is the unit circle's radius.** Whatever the reader laid down — 1, 5, 1000 — the
arrival reads the same address, and **the hold reads as 1 to itself** every time. That 1 is not
a length chosen for convenience. It is the reader's own unit seen from inside its own readings,
and it is the radius §4.2 finds left over when the denominator is divided out.

### The second: closure — and why a shape needs four

**What it is.** The freedom to come back. One freedom does not have it: [0, ∞) is an open ray,
and walking it upward never returns — the far end is a horizon, not a way home.

**How many it takes** (`closure.mjs`). Allow each of the two terms a sign and there are four
ways the pair can stand: (+,+), (+,−), (−,+), (−,−). **Each quadrant is a whole copy of [0, ∞)**
— within it the ratio runs from nought to infinity — and the four laid end to end join up, the
far end of one being the near end of the next. Four quarter turns, 4 × π/2 = 2π, and the turn is
closed.

> **A shape closes on four.** Not by choice: it is two signs by two signs, and there is no fifth
sign
> pair to add.

**And a third signed term gives eight regions, by the same count.** The sign pairs become sign
triples — +++, ++−, +−+, +−−, −++, −+−, −−+, −−− — eight of them, and **each carries two
freedoms rather than one**: two independent ratios among three terms, which is the whole
difference between closing a line and closing a surface.

**And the count is forced without any turn at all** (`noangle.mjs`). A copy is fixed by its two
signs, and joining a far end to the next near end flips exactly one of them: V+H+ → V−H+ → V−H−
→ V+H− → V+H+. Each sign must be flipped an even number of times to return and there are two
signs, so
**the shortest return flips each twice: four steps and no fewer.** That derivation is counting, not
geometry, and the joining rule needs none either — **the far end of a copy is where its
denominator vanished, the near end of the next is where its numerator vanished, and those are
the same event with the roles swapped.**

So the closure count survives the removal of the angle. What does *not* survive is the
**measure** — that each copy is π/2 of something, that eight regions sum to 4π. Those are
statements about size, and a freedom has none (§5.5). **The turn can be dropped from the
derivation and kept only where it is measuring**, which is where it was already marked as
imported.

**And the closed walk is 2ⁿ steps, of which four was only the first case** (`sixteen.mjs`). Closure
joins regions that differ in one sign, and the shortest walk visiting every region and returning
is a Gray code on the sign vector. At four terms it runs ++++, +++−, ++−−, ++−+, +−−+ … −+++ and
back:
**sixteen steps, every one flipping exactly one sign.**

| signed terms | regions | closed walk | freedoms per region |
|---|---|---|---|
| 2 | 4 | **4** | 1 |
| 3 | 8 | **8** | 2 |
| 4 | 16 | **16** | 3 |
| 5 | 32 | **32** | 4 |

**The rule was never *four*.** Four was 2², the case §5.1 works. And the atlas keeps pace: at four
terms, one chart leaves twenty-six directions unaddressed, two leave eight, three leave
**exactly two**, and four cover everything — the same shape as the sphere's three, one step up.

**Three claims have to be told apart here, because they are not equally earned:**

| | |
|---|---|
| three signed terms give **eight regions**, each with two freedoms | **derived** — it is 2 × 2 × 2, and the ratio count |
| those eight regions **tile a sphere**, each of solid angle π/2, summing to 4π | **consequential** — true, and it imports conventional spherical measure |
| therefore a sphere **is** eight copies of this relation space | **not established**, and this paper does not claim it |

The first is the result. The second is a fact about the usual geometry that the first is
consistent with. The third would need an argument nobody here has made.

**The rule underneath both.** n + 1 signed terms close on 2ⁿ⁺¹ regions, each carrying n
freedoms: a circle is 4 regions of 1 freedom, and three terms give 8 regions of 2. **The count
of regions is the closure; the freedoms inside are what is read.**

**What it costs.** Nothing extra to *have* — the four and the eight are not new freedoms but
copies of the same one laid end to end. What they cost is the horizon: a closed structure has no
far end to be lost at, and §6 shows what goes with it.

### An aside: the walk and the facing are one kind and two readings

Worth settling here, because the two are easy to run together (`walkfacing.mjs`).

**By form they are the same kind.** Both take two things in and give one magnitude out,
which is this paper's own criterion for a kind (§5.5). **By pair they are two readings.** The
walk is an arrival against the held standoff — V/S = 0.6. The facing is an arrival's extent
against its own other extent — V/H = 0.75. Same form, different pair, which is exactly what §5.1
says distinguishes a rate from a plain reading: the first kind applied to a pair a poorer reader
could not make.

**And holding one standoff gives all of it.** V/S = 0.6, H/S = 0.8 — two readings against one hold —
and then (V/S)/(H/S) = 0.75 is the facing, with the standoff cancelling. **One hold, two
readings, one composite.** The facing is not a third thing held; it is what the two held
readings make.

Which is why the list below is *three worked examples* rather than *the three freedoms*: they
are examples of the definition, not a claim that a reader has exactly these and no others.

### The third: depth — the vanishing point

**What it is.** The freedom that says how far along a line of sight a thing sits, read as an
address rather than a distance. The demonstration built for it (`vanishing-point.html`) is the
plainest statement: posts at every unit along a road, the eye standing among them, and each
post's reading formed against the standoff the eye holds.

**What it addresses.** The place where the extents run away — the vanishing point. Every post
has a reading; the point itself has none. It is the address that can be pointed at and never
opened, which is what a horizon is when it is written as an address rather than met as a
failure.

**Its two ends.** Nought underfoot, where the thing is at the eye, and the vanishing point at
the far end — and *between* them the whole road, compressed as the reading grows. That
compression is the freedom's own shape and not an artefact of drawing: it is what reading
against a held standoff does.

**What it costs.** The same one register as the first — but only one of the two can be held at a
time, which is why a reader with one register has a depth or a centre of gravity and not both at
once.

## 5.2 The semicircle: two freedoms, one join

> **(1 Oct)** Built from signed copies, which the Sep 25 ruling replaced by magnitudes (R37). Its "facing forwards/backwards" is which term is underneath, not R149's front side and back side. "Semicircle" is now also the pure-mathematics name for the fisheye.

The smallest structure with two freedoms joined, and worth looking at first because it has the
joining without the wrap-around (`semicircle.mjs`).

**What a semicircle is, in freedoms.** A turn is four signed copies of [0, ∞). A semicircle
is two of them — **one binary choice exercised, one not**: take V non-negative and let H be
either sign. That is this series' own reading of the bilateral semicircle, the atom times an
orientation bit.

⚠ **That bit was called a count here, and it is not one** (Tom, Sep 19; *The Boundary* §9.4). The
ruling: **the facing is your freedom — you are free to face forwards or backwards at the seam between
two freedoms.** The discriminating mark is not scale-invariance, since a count of arrivals survives a
common scaling too; it is whether the thing *addresses*. A count of arrivals is a property of **the
list** — seven arrivals is a fact about how many came, with no pair and no denominator. The
orientation bit is a choice between **V/H and H/V, and both are freedoms by §1's definition**: each
is one magnitude in terms of another, scale-invariant, on [0, ∞).

> **It is not a count because it is not a property of a list. It is a selection among freedoms** —
> which is why *free* is the right word for it. A count says how many; the facing says which freedom
> is being exercised.

**And the table below already shows where it is exercised.** The two special places are opposite in
kind: at the quarter both readings say **1** — the freedoms agree; at the middle one says ∞ and the
other **0** — they are maximally apart. **The seam is the middle**, because it is the only place the
two disagree about *which end the reader is at* rather than about a value.

| at the seam, V = 1 and H = 0 | hold underneath | reading | what the reader calls it |
|---|---|---|---|
| facing forwards | H = 0 | 1/0 = ∞ | **the horizon** |
| facing backwards | V = 1 | 0/1 = 0 | **home** |

**The same two magnitudes, the same instant.** Which end of its own line a reader believes it stands
at is decided entirely by the orientation — and nothing in the reading fixes that orientation, so it
is genuinely free.

**⚠ And there are two freedoms here, not one with a bit attached.** A first pass read this as *one
freedom with two orientations* and was corrected: **each freedom IS a facing, and a reader's freedom
is restricted to that facing** (Tom, Sep 19). There is no freedom-plus-orientation, because the
orientation is the whole of what distinguishes V/H from H/V. A reader has one because it is
**restricted** to one — and this section's own words were already right: "two freedoms **joined** at
their horizons."

**The restriction is what makes §4.2 true, and it makes it a consequence rather than a ruling.**

> A reader faces one way; a facing is a freedom; therefore a reader has one freedom — and the only
> way to have the other is to be a reader facing the other way.

"A second freedom requires a second reader" was never a budget rule about seats. It is this.

**And it sorts the four moves, which were never alike** (*The Boundary* §9.4, B56). Three act *within*
a freedom and one *leaves* it: rescale, shift and compose all have positive determinant and keep the
facing; **swap has determinant −1 and crosses to the other one.** The determinant is multiplicative,
so a product of positives is positive — **a reader zooming, shifting and scrolling forever never
arrives at the other facing.** It is not far away and not hard to reach; it is not reachable by doing.
One swap suffices and two undo.

> **The moves fall into exactly two components, and the components are the facings.** Which is why the
> repertoire closes on *four* moves and not three: three to move within a freedom, and one to be the
> other freedom.

**Where the two join, and where its ends are.** Walk it, watching both readings:

| position | V | H | s = V/H | H/V |
|---|---|---|---|---|
| the start | 0 | 1 | **0** | ∞ |
| a quarter along | 0.707 | 0.707 | 1 | 1 |
| **the middle** | 1 | 0 | **∞** | **0** |
| three quarters | 0.707 | −0.707 | −1 | −1 |
| the end | 0 | −1 | **0** | ∞ |

**The two outer ends are V = 0, where s reads nought** — ordinary addresses, read without
difficulty.
**The middle is H = 0**, where the first reading diverges and the second reads nought.

> **A semicircle is two freedoms joined at their horizons**, with their origins left at the
two outer
> ends. The join is exactly the place one reading cannot reach.

**And the two legs are two paths to that one place, which neither of them can cross.** Approaching
the middle in the first reading:

| position | H | s = V/H | H/V |
|---|---|---|---|
| 0.40 of the half | 0.309 | 3.08 | 0.3249 |
| 0.48 | 0.0628 | 15.89 | 0.0629 |
| 0.499 | 0.0031 | 318.31 | 0.0031 |
| **0.5** | **0** | **+∞** | **0** |
| 0.501 | −0.0031 | **−318.31** | −0.0031 |
| 0.52 | −0.0628 | −15.89 | −0.0629 |

From the near leg the reading runs to **+∞**; from the far leg it returns from **−∞**.

> **One place in the structure, two horizons in the reading** — and they sit at opposite ends of the
> ray, so no continuous path in the reading joins them.

So a reader holding this freedom approaches the middle from either leg and **never crosses it**
— not because the place is missing, but because its two approaches leave the reading in opposite
directions. **And the other reading crosses without noticing**: 0.3249 → 0.0629 → 0.0031 → 0 →
−0.0031, with nothing special at the middle at all. **Crossing is not forbidden; it is forbidden
to that reading** — and a one-register reader holds one reading at a time, so crossing costs a
swap, which is an act rather than a continuation.

**Which is an earlier result seen in a mirror.** There, nought and infinity were one boundary with
two addresses. Here, the middle is one place with two horizons. **A single place in the
structure, doubled in the reading — and the doubling is what makes it uncrossable from inside.**

**And that is the whole closure mechanism, visible and not yet closed.** Crossing the middle is
impossible in the first reading and ordinary in the second, which reads nought and keeps going.
Nothing is cancelled: **the horizon has been made interior by a second freedom whose own horizon
is somewhere else** — at the two outer ends, where the first reading is perfectly comfortable.
Each covers the other's blind place and no place is blind in both.

**What it still lacks is the wrap.** Its outer ends join nothing, so walking off one does not bring
you to the other. Closing takes two more copies, the V < 0 half, which is §5.1's four. **So the
semicircle is the right object to learn on: it has the joining and not the wrap-around, and the
two can be understood separately.**

## 5.3 Freedoms that close instead of exploding

Each freedom, read alone, runs to a horizon it never reaches. Read *together*, they need not —
and what happens instead is worth stating carefully, because it is where the infinities go
(`charts2.mjs`).

**Two freedoms address a direction, with nothing borrowed.** Three extents sharing a hold, and two
composites of them: a = v₁/v₃, b = v₂/v₃. Both are freedoms by §3, both are addresses, and
together they fix the direction — extents 3, 4, 12 give (0.25, 0.3333), recovered as (a, b, 1)
normalised. No angle anywhere. **Two freedoms do the work of two coordinates.**

**But one pair is blind on a whole circle**, wherever its denominator vanishes. And here is the part
that matters: **another pair reads that same place as an ordinary number.**

| direction | pair A: v₁/v₃, v₂/v₃ | pair B: v₂/v₁, v₃/v₁ | pair C: v₃/v₂, v₁/v₂ |
|---|---|---|---|
| (3, 4, 12) | (0.25, 0.3333) | (1.3333, 4) | (3, 0.75) |
| (1, 0, 0) | *no address* | (0, 0) | *no address* |
| (0, 1, 0) | *no address* | *no address* | (0, 0) |
| (0, 0, 1) | (0, 0) | *no address* | *no address* |

Of twenty-six directions tested, **none is blind in all three pairs.**

> **A sphere is freedoms whose horizons cover each other.** The far end of one pair is the middle of
> the next, and there is nowhere left for an infinity to be. **The infinity does not live on the
> sphere; it lives in a chart, and another chart does not have it.**

**Which is §5.1's closure one step up.** Four copies close a turn because the far end of one is the
near end of the next. Three pairs close a sphere because the blind circle of one is interior to
the others. Same mechanism, one more freedom.

**And the trade against angular coordinates is exact.** Latitude and longitude are blind at two
points where a ratio pair is blind on a circle, so the angular system covers more with one chart
— and it pays for that with an angle. Three ratio pairs cover everything; two leave exactly two
directions, which are precisely lat/long's two poles. **One more chart, and nothing in it is an
angle.** The coupling goes too: a degree of longitude shrinks with the cosine of latitude, while
a and b are formed separately and composed only when asked.

## 5.4 One more paradox, because it names the horizon

The companion piece has a case that belongs to §6 rather than here. **A stock falls 50%, then
rises 50%** — and ends at 75, not 100. The second percentage was taken against a *different*
denominator, the shrunken price, and chaining the two as though the *of what* had stayed fixed
is a denominator error committed with a calculator.

That is the composition law being used where it does not apply. Two reads compose only when
their denominators are the same or are known to each other; here the second read's denominator
is the first read's *result*, and nothing was kept that would let the two be related.

**It also says where composing stops, in a case with no infinities in it.** §6 finds that
composition fails when one freedom is at 0 and another at ∞. The percentage case fails less
dramatically and for the same reason: **composition needs the denominators to be accounted for,
and a chain that discards each one as it goes has nothing left to compose with.**

## 5.5 Where scale invariance comes from

A stronger claim than anything above, and worth testing rather than asserting: **scale
invariance always comes from a freedom.** Take invariant quantities from wherever they are found
and ask what makes each one invariant (`invariance.mjs`):

| the quantity | invariant under ×1, ×7, ×1000 | what it is |
|---|---|---|
| a ratio v/h | 0.75, 0.75, 0.75 | a freedom, by definition |
| an angle atan(v/h) | 0.927295 throughout | a freedom in another notation — the argument is still v/h |
| a correlation | 0.9897 → 1 | a covariance over two spreads: all three carry the scale, and it cancels |
| a power-law exponent | 1.5, 1.5, 1.5 | a ratio **of** ratios — a composite, by §3's law. Fractal dimension has the same form |
| a shape | invariant | a set of freedoms and nothing else |

**The claim holds for all of them, and there is exactly one exception.** Rescale every magnitude
in a list and there are still five items in it. **A count is scale-invariant and is not a
ratio** — which §5 already puts outside the definition, since seven arrivals is not seventy
scaled down.

> **Scale invariance has two sources, and they are this series' two instruments. DIVIDING, where the
> scale is discarded — a freedom, or a composite of freedoms. COUNTING, where the scale was never
> referenced at all.**

**And the two instruments act on two different objects, which is the deeper reason they do not
mix.** A magnitude list *has* items: 2, 3, 12, 6, 30 is five things, with a next one after each.
**A freedom has none.** Between 0.75 and 0.76 lies 0.755, and between those 0.7525, and it never
stops —
**there is nothing on a freedom to count.** A freedom is not counted; it is **swept**. The reader
moves along it continuously, with no first step and no next address to tally, and sweeping is
the freedom's own operation the way counting is the list's.

**And when a freedom does get counted, the count belongs to the reader.** A grain of 0.1 gives 16
steps across the quarter, 0.01 gives 157, 0.0001 gives 15,708 — and every one of those is the
*same freedom*. The numbers describe the grain. **A count on a freedom is a count of the
reader's own steps**, and the discreteness came in with the reader rather than being found
there.

Which is the cleanest statement of why a winding number was never a freedom: **laps are items of
a journey, not points of an address.**

**And underneath that is the reason the two instruments cannot meet at all: counting implies a
changing size, and a freedom has no size to change.**

| items | the tally's extent | the freedom's span | its spacing |
|---|---|---|---|
| 5 | 5 | 1 | 2.0 × 10⁻¹ |
| 50 | 50 | 1 | 2.0 × 10⁻² |
| 500 | 500 | 1 | 2.0 × 10⁻³ |
| 5,000 | 5,000 | 1 | 2.0 × 10⁻⁴ |

**A tally is its own size.** The count and the extent are the same number, so counting is not
something done *to* a size — it is a size being made, one item at a time. **A freedom has a span
it cannot exceed**: add to it and the span is unchanged while the spacing halves and halves.

> Counting needs somewhere to put the next one, and the only place is further out. **A
freedom has no
> further out** — its far end is a horizon, not an edge to extend past. **So a freedom cannot be
> counted, because counting would require it to grow, and it answers everything in density
instead.**

Not a rule about what is permitted. There is simply nowhere for a tally to go.

**And the difference is worth keeping.** A freedom is invariant because it *paid*: the magnitude
was spent buying the address. A count is invariant because it never engaged with magnitude in
the first place. Which is also why a count cannot be composed with a freedom — §3's law divides,
and there is nothing in a tally to divide out — and why a winding number resisted every attempt
at reduction in earlier work.

**So the corrected form of the claim, and it is a conjecture rather than a result:** every
scale-invariant quantity either divided or counted. The table above is five cases and a
counterexample, which is support and not proof — a universal claim about all scale-invariant
quantities is not something a handful of examples settles. **Held as a working conjecture** it
earns its place: it has survived every case tried, it names its own exception, and it says where
to look for a refutation — something invariant under scaling that neither formed a ratio nor
kept a tally.

## 5.6 The horizon is where addresses become indistinguishable

> **(1 Oct)** R77 keeps the two ends apart: the horizon is v/h → ∞, never reached; what sits at home is the vanishing point. Where a reader's grain gives out is not the horizon; with R149, the reached span is the working horizon, the front side. R88 settles the count as three landmarks of two kinds, close to this section's "one value and one pair".

Two results above meet here. The freedom thins as it sweeps (§5.1), and a freedom answers every
pressure in density rather than in size (§4.3). Put together they say what a horizon is
(`fisheye.mjs`):

| sweep, as a fraction of the quarter | address | addresses per unit of sweep |
|---|---|---|
| 0 | 0 | 1 |
| 0.5 | 1 | 2 |
| 0.9 | 6.3 | 40.9 |
| 0.99 | 63.7 | 4,053 |
| 0.999 | 636.6 | 405,285 |
| **at the quarter exactly** | **∞** | **∞** |

> **The horizon is where the addresses become indistinguishable.** The diverging density is the
> mechanism; the indistinguishability is what a reader actually meets.

**And that is a better account of why nobody arrives than the arithmetic one.** Saying the
denominator vanishes is true and sounds like an accident of notation. Saying the density
diverges needs no notation: **to arrive you would have to tell apart infinitely many addresses
in no room.** Any grain stops short, and its own size says where — a grain of 0.1 can still
separate addresses out to ten, 0.01 out to a hundred, 0.0001 out to ten thousand. A coarse
reader stops early and a fine one stops late, and neither arrives.

**Which makes the horizon the reader's and not the space's.** A reader of step σ separates two
addresses only if their sweeps differ by σ or more, and past tan(π/2 − σ) nothing ever differs
by that much again:

| grain | last separable address | what lies past it |
|---|---|---|
| 0.2 | 4.93 | everything to ∞ |
| 0.1 | 9.97 | everything to ∞ |
| 0.01 | 100 | everything to ∞ |
| 0.0001 | 10,000 | everything to ∞ |

> **Past its own horizon a reader holds one address containing everything.** Not a blur and not a
> boundary: a single reading, into which the whole remaining ray has collapsed.

**⚠ And there is a second reason nobody arrives, found later and stronger than this one** (*The
Boundary* §9.3, B52). Everything above says the horizon is unreachable. It is also **not a separate
place.** Swapping which magnitude goes underneath sends 0 to ∞ and ∞ to 0, so home and the horizon
are exchanged by that one choice — and the exchange is not bookkeeping but a statement about one
situation:

| magnitudes present | which is held underneath | reading | what the reader calls it |
|---|---|---|---|
| 1 and 0 | the 0 | 1/0 = ∞ | **the horizon** |
| 1 and 0 | the 1 | 0/1 = 0 | **home** |

**The same two magnitudes, the same instant, the same world.** Which end of its own line the reader
believes it stands at is decided entirely by which magnitude it happened to put underneath.

> **Home and the horizon are one place with two names.** Not two ends of a line — one end, read from
> either side of the hold.

That also settles the landmark count. The candidates are forced: every landmark is a fixed point of
one of the four moves, so on the line there are only 0, +1, −1 and ∞. −1 needs a negative magnitude
and is outside a reader's world; 0 and ∞ are the pair above; **+1, the corner, is the only one the
swap leaves alone.** The honest inventory is **one value and one pair**, not three landmarks — and it
is why §2.1's unit is the corner and could not have been either end.

The space has one horizon, at infinity, where composition stops. **A reader meets its own
wherever its grain gives out** — and two readers of the same space have different ones, with a
finer reader pushing it further without ever removing it.

**So the far end is not empty and not distant. It is occupied and unresolved:** everything is still
there, and none of it is separately addressable. The reader has the whole of it and can say
nothing about any part.

**And notice what is absent from every line of this.** No size. Not in the density, not in the
divergence, not in where a reader stops, not in what collapses. **The size was spent when the
address was formed**, and the horizon is a fact about an address space — which has no sizes in
it to be far away.

## 5.7 A freedom's own measure, and how it disagrees with the borrowed one

§8 asked whether there is a measure on the ratio side at all. There is, it is essentially
unique, and it disagrees with the angle about the thing that matters (`measure.mjs`).

**What a measure has to satisfy.** Additive over pieces joined end to end — m[a,b] + m[b,c] = m[a,c]
— and invariant under the one operation the structure supplies, which is composing with a
constant.

| candidate | additive? | under composing with 3 |
|---|---|---|
| plain length, b − a | yes | m[1,2] = 1 becomes m[3,6] = **3** — fails |
| log length, ln(b/a) | yes | m[1,2] = 0.693147 stays **0.693147** — survives |

Plain length fails because it is a magnitude and a freedom has none. Log length survives because
the constant cancels inside the ratio, which is the freedom's own move. **And it is the only
kind that can:** invariance forces dependence on b/a alone, additivity then forces m =
c·ln(b/a). **The logarithm of the ratio, up to a choice of unit.**

**And in that measure the count toward either end is infinite.** From 1 to 2 is 0.6931; 1 to a
million is 13.8155; a millionth to 1 is also 13.8155; and **0 to 1, or 1 to ∞, is infinite.** What
this measure counts is addresses — how many lie between two places — and toward either horizon there
is no end to them. **The extent they are hung on is still the quarter turn** (§5.16).

> **The angle measures a freedom's extent: a quarter turn, finite, with ends at a finite distance. Its
> own measure counts its addresses: infinitely many toward either end, which is why the horizon cannot
> be arrived at.** The two do not disagree about the freedom. One is its extent and the other its
> density (§5.16).

**So the π/2 was never a debt.** It is a different measure, imported with the angle, and the paper
should say so rather than promise to repay it.

**And the freedom's own measure is not new either: it is the grain.** m[a,b] = ln(b/a) says
a step is a *ratio* rather than a difference, which is exactly what a grain σ is in this series
— a step in the log, with e^σ its ratio: σ = 0.6931 multiplies the address by 2, σ = 1 by
2.7183, σ = 2.3026 by 10.
**The measure was never missing. It has been here since *The Radix*, under another name and doing
another job.**

It also counts without any angle. Between two addresses the steps are ln(b/a)/σ: 1 to a thousand
at a grain of ln 2 is ten steps, 1 to a million is twenty, a thousandth to a thousand at σ =
0.01 is 1,382.
**The earlier counts — 16, 157, 15,708 "across the quarter" — were counts in the borrowed measure.**
In the freedom's own, the count between any two addresses is finite and the count across the
whole is infinite, which is the honest statement of a reader that can always look further and
never arrive — not because the freedom is long, but because it is infinitely dense.

## 5.8 Why freedoms compose picturably, and what the ease costs

An asymmetry worth stating structurally rather than as a fact about anyone's imagination
(`picturing.mjs`).

**What each costs to add.** An extra direction must be perpendicular to *every* existing one — a
joint condition, and the n-th must satisfy n − 1 constraints at once. An extra freedom must be
another pair read against the same hold — a local condition, and it need only be a ratio.

| | constraints on the n-th direction | constraints on the n-th freedom |
|---|---|---|
| 3 | 2 | 0 |
| 4 | 3 | 0 |
| 10 | 9 | 0 |

> **The cost of a direction grows with how many there already are. The cost of a freedom does not
> grow at all.**

**Which is why four of one can be drawn and four of the other cannot.** Four directions must be held
mutually perpendicular at once, and there is nowhere to put the fourth. Four freedoms are four
copies of [0, ∞) laid end to end, each joined where the last ran out — nothing perpendicular to
anything, and the picture is §5.1's closed turn. **Composing freedoms needs a join; composing
directions needs a direction. Joins are always available; directions run out.**

**And the count of freedoms is not bounded by the count of directions.** Three extents give six
ordered pairs, ten give ninety, and the number available is set by **how many things there are
to relate** rather than by how many directions a space has. A colour has three extents and three
freedoms; a sound has as many as its spectrum has bands. So *many freedoms* and *three
dimensions* are not rival claims — **they count different things, and only one of them is
bounded by perpendicularity.**

**⚠ And the ease is also the hazard, which has to be said in the same breath.** Freedoms are easy to
add precisely because adding one costs nothing structural. **A framework in which nothing
constrains the next addition can accommodate anything, and a framework that can accommodate
anything predicts nothing.** What keeps this one honest is already here: n freedoms give only
**n − 1 independent** composites, so most of what can be added is dependent on what is present
already. **The easy part is adding freedoms. The work is showing which are independent.**

## 5.9 Nothing in this singles out three

The three worked examples of §5.1 are examples. It is worth checking that the construction has
no preferred size, because if it had one, that would be the paper's most important result and it
does not (`arbitrary.mjs`).

| freedoms | hold cancels | associative | telescopes | independent composites | ordered pairs |
|---|---|---|---|---|---|
| 2 | yes | — | yes | 1 | 2 |
| 3 | yes | yes | yes | 2 | 6 |
| 4 | yes | yes | yes | 3 | 12 |
| 10 | yes | yes | yes | 9 | 90 |
| 50 | yes | yes | yes | 49 | 2,450 |
| 500 | yes | yes | yes | 499 | 249,500 |

**Nothing changes at three.** The hold cancels, composition stays associative, the chain telescopes,
and the independent count stays n − 1, at every size tried. **And the closure count has no step
in it either**: two terms give four regions of one freedom, three give eight of two, eight give
256 of seven — one rule throughout.

**What is actually special about three is two things, and neither is about freedoms.** It is the
number of extents a person's own situation happens to offer — a fact about people. And it is one
of the two sizes at which the *borrowed* spherical measure agrees with a quarter circle, two and
three both giving π/2 while four gives π²/8 (§5.7) — a fact about the imported measure, which a
freedom's own measure does not share.

> **Three is where a reader of this series arrives. It is not where the arithmetic stops.**

**And the complexity available grows as fast as anyone could want.** Ten freedoms give
ninety ordered pairs and 720 chains of three; twenty give 380 and 6,840. **Every one of those is
still an address in [0, ∞) with the same two ends** — arbitrary complexity, and no new kind of
object anywhere in it. Which is the better thing to show than a match to any particular count:
**not that there are three, but that there is no last one.**

## 5.10 How freedoms scale

> **(1 Oct)** The real-world numbers in this section count as tests, which since 26 September are planned first (source, predictions, kill conditions), not improvised.

§5.9 shows the construction runs to any size. What keeps a large set of freedoms workable is not
more arithmetic but an arrangement: **freedoms grouped, a hold for each group, and a hold above the
group holds.** Relating two freedoms then stays cheap and local however many there are. This section
says how, first on a worked example, then in general. It is arithmetic about arrangements; it does
not claim that anything in the world is arranged this way.

### The worked example: the human body

Take published adult anthropometric means and hold each part against the part it belongs to — the
digits against the hand, the hand and forearm against the arm, the arm against stature
(`realtower.mjs`). Numbers nobody chose for the purpose.

| | |
|---|---|
| digits against the hand | index 0.3947, middle 0.4368, ring 0.4053, little 0.3158 |
| index / middle | **0.9036**, and 7.5/8.3 = 0.9036 — the hand is gone |
| and with the hand at 17.2 or 21.4 | 0.9036 either way |

**Inside a group, the group's hold cancels.** The proportions of the fingers do not depend on how big
the hand is.

**Between groups, exactly one factor is left.** A digit against the hand reads 0.3947; the forearm
against the arm reads 0.3462; their composite is 1.1404, where the bare items give 0.2778. **The
residue is 4.1053 — and arm/hand is 4.1053.** One factor, and one only.

**And the level above removes it.** Hand against stature is 0.1083, arm against stature 0.4444, and
their composite is **4.1053** with stature cancelled.

> **Freedoms scale by grouping: each group's hold cancels inside the group, a crossing leaves exactly
> one factor, and that factor is removed one level up.**

**⚠ What the example shows and what it does not.** It shows the arithmetic on measured numbers. It does
not show that a body *is* organised this way: the grouping was chosen here, and another grouping
would give another arrangement over the same measurements.

### The smallest case, and the count

Four freedoms in two groups of two (`four.mjs`): group A holds 6 and 4 against 2; group B holds 9 and 3
against 6; both holds are read against 12.

| | the readings |
|---|---|
| group A | 6/2 = **3**, 4/2 = **2** |
| group B | 9/6 = **1.5**, 3/6 = **0.5** |
| one level up | 2/12 = **0.1667**, 6/12 = **0.5** |

Inside A, 3/2 = **1.5** = 6/4, with the hold of 2 gone. Across, 3/1.5 = **2** where the bare items give
6/9 = 0.6667; the residue **3** is 6/2, the ratio of the two group holds. One level up, 0.5/0.1667 =
**3**, with the 12 cancelled. At a hundred items in ten groups it behaves identically (`tower.mjs`):
the residue across groups is h₇/h₂ = 2.052632, and one level up removes it.

**Grouping sorts independence and makes none:**

| items | groups | within groups | between groups | total | flat n − 1 |
|---|---|---|---|---|---|
| 4 | 2 | 2 | 1 | **3** | 3 |
| 100 | 10 | 90 | 9 | **99** | 99 |
| 100 | 50 | 50 | 49 | **99** | 99 |
| 500 | 20 | 480 | 19 | **499** | 499 |

> **(n − g) + (g − 1) = n − 1, always.** Composites are sorted into those that stay inside a group and
> those that relate the groups.

**Two things are not grouping, and it helps to say so.** A sphere's three pairs are peers covering each
other's blind circles (§5.3) — an atlas, with no hold above another. And a hierarchy of addresses is
not grouping either: a prefix names, it does not hold. Grouping needs each level to supply the unit
for the level below.

### 5.10a A grouping fixed from outside: the metric thread

The body's grouping was chosen here. In an **ISO metric screw thread** it is fixed by the standard: the
nominal diameter by ISO 261, the pitch for each diameter by the same standard, and the profile
dimensions defined by the pitch in ISO 68-1 (`given.mjs`).

| bolt | H/P | h₃/P | r/P | H/h₃ |
|---|---|---|---|---|
| M6 | 0.86603 | 0.61343 | 0.14434 | **1.41178** |
| M10 | 0.86603 | 0.61343 | 0.14434 | **1.41178** |
| M20 | 0.86603 | 0.61343 | 0.14434 | **1.41178** |
| M36 | 0.86603 | 0.61343 | 0.14434 | **1.41178** |

The pitch cancels inside its group, so an M6 and an M36 have the same profile composites. Crossing to
the diameter leaves one factor, which varies because the standard makes it vary: (H/P) / (P/D) reads
5.1962, 5.7735, 6.9282, 7.7942. Twelve items in four groups give eight composites within and three
between, eleven in all.

**⚠** This shows the thread behaves as grouped freedoms because the pitch really is the unit of the
profile. That is engineering; the arithmetic only reports it correctly.

### 5.10b Relating costs a distance, not a size

Grouping nests to any depth (`deeptower.mjs`). **A composite cancels every hold its two freedoms share
and leaves one factor for each they do not**, so its bill is the number of levels up to their common
hold. At depth four and branching three, eighty-one freedoms:

| the two freedoms | levels to the common hold | factors left |
|---|---|---|
| neighbours under one hold | 1 | 1 |
| cousins | 2 | 2 |
| opposite sides | 4 | 4 |

> **Neighbours cost nothing; strangers cost the depth.**

**And the independent count does not move:**

| branching | depth | freedoms | holds | independent | flat n − 1 |
|---|---|---|---|---|---|
| 2 | 3 | 8 | 7 | 7 | 7 |
| 3 | 4 | 81 | 40 | 80 | 80 |
| 10 | 2 | 100 | 11 | 99 | 99 |
| 2 | 10 | 1,024 | 1,023 | 1,023 | 1,023 |

**Depth sets cost, never the answer.** Four readings composed by any route — ((A₁/A₂)·(A₂/B₁))·(B₁/B₂),
bracketed the other way, A₁/B₂ directly, or through B₁ — all give **6**. Composition is associative and
commutative, so the order in which levels are crossed cannot change the result.

> Complexity grows with the number of freedoms. **The cost of using them grows with the distance
> between the ones wanted** — which an arrangement can keep small.

### 5.10c At size

A thousand freedoms carry 999 independent composites and 998,001 dependent ones; a million carry a
million and **a trillion** (`scene.mjs`). Nobody holds the pairs. **The independent set is the object.**

| | flat: every freedom against one hold | grouped: a hold per group |
|---|---|---|
| cost to relate any two | **0 factors** — the hold cancels outright | **at most the depth**: 3 at a thousand, 6 at a million, 9 at a billion |
| what must have been compared | **every freedom against the same thing** | **each freedom against its own group's hold only** |

> **Grouping is not cheaper. It is buildable.** Flat composition costs nothing and needs one global
> reference; grouping needs only that neighbours were compared, and pays log N factors for the rest.

**And what a one-register reader has of such a scene is one reading** — the hold, the arrival, their
ratio. Every other composite is reachable by walking to it; none is held. **A scene of thousands of
freedoms is not something a reader holds. It is something it can address.**

### 5.10d The reader scales the same way

One arrangement was not chosen here, and it is the reader itself (`indirections.mjs`). Two
indirections, each a ratio against a hold:

| | items | hold | an address |
|---|---|---|---|
| **level 0** | magnitudes | **h**, the held value | s = v/h — 3 and 12 against 4 read 0.75 and 3 |
| **level 1** | addresses | **σ**, the grain | position in grains, ln(s)/σ |

Level 0 is an ordinary freedom: composing two addresses gives 0.25 = v₁/v₂, and the hold is gone.
Level 1 is one too: §5.7 found the reader's own measure to be ln(b/a), so its position counted in its
own steps is ln(s)/σ, and composing two positions gives **−0.26186** whether the grain is 0.6931, 1 or
2.3026. **The grain cancels inside its own level.**

> **The two indirections are two levels, and they were not arranged. They are what a reader is.**

**Which says what the fisheye is.** Equal reader steps land at addresses 1, 2, 4, 8, 32, 1024 because the
two levels measure differently — ratios of magnitudes below, ratios of logs above. **The fisheye is
the residue of the crossing between them.**

**A single reader has exactly two levels, because it holds exactly two things** — a value and a step
(`morelevels.mjs`). A facing, a record or a composite is a reading, not a thing held. **A third level
costs a second reader:** two grains of 0.6931 and 2.3026 give **0.30103**, unmoved when both are scaled.

| | levels |
|---|---|
| one reader | **2** — a value and a step |
| two readers | **3** — the third is their grains compared |
| n readers | **untested** |

**⚠** Every level here is a level of the reader. That a scene supplies matching levels is not shown.
## 5.11 An address of addresses, and why depth is free

Scaling needs one more thing to be affordable, and it is already available: **an address whose
two terms are themselves addresses** (`indirection.mjs`).

Four magnitudes against a hold read 3, 2, 4.5, 1.5. Compose them in pairs: c₁ = 1.5, c₂ = 3. Now
compose *those*: d = c₁/c₂ = **0.5** — and d is in [0, ∞), with the same two ends and the same
corner as everything below it.

> **The space is closed under addressing.** A ratio of two addresses is an address. **No new kind of
> object appears at the second order, or at any order.**

Carried further it keeps not happening: order 1 gives 1.5 and 3, order 2 gives 0.5, order 3
gives 0.25, order 5 gives 0.0039 — every one formed the same way, landing in the same space,
scale-free by the same argument. **Indirection is free, and that is why grouping can nest as deep
as anyone likes (§5.10b): depth adds levels, not kinds.**

**⚠ And "free" is a parallel statement, which this section did not say** (`depths.mjs`, B167). A
reader that may compose *any* address against *any* other has no top. A reader taking each arrival
against the last runs out of terms: on n arrivals the sequential tower dies at **order n − 1**,
measured at n = 2, 4, 8 and 16. That is the same n − 1 that prices what a bounded reader can check of
the band (§9.7n), reached from the other side. **The depth a serial reader can stand on is its own
memory.**

**And the reason depth is free is sharper than "no new kind appears", and it is the same fact as z
being bounded** (§5.19, §8 item 0). Every term at order ≥ 1 is a product of the magnitudes with
integer exponents **summing to zero** — that is exactly what scale-freedom is — while a single
coordinate has exponent sum one. Stacking every tower row at orders 1–5 on eight magnitudes spans
**rank 7 of 8**: one short, always the same one short, and the missing direction is the hold.

> **Depth is free precisely because it never produces a coordinate.** Free and coordinate-less are
> one property stated twice, and getting z back needs the one direction the tower cannot make.

**And the landmarks survive it.** An address divided by its own partner gives 1 at every order —
s₁/s₁ = 1, c₁/c₁ = 1. Swapping the two terms gives the reciprocal at every order: c₂/c₁ = 2 and
1/(c₁/c₂) = 2.

> **An address that addresses itself is the corner.** Self-reference is not a paradox here;
it is the
> identity of the composition law, and it is the same 1 at every order.

**And it settles the standing of a composite along with it.** A composite is formed as one thing
against another, is unchanged when both are scaled, and addresses rather than values — it meets
the definition of §1, which is the whole of the test. **Freedoms are not sorted into types here,
and nothing so far gives a reason to start.** Since composing composites produces nothing of a
new kind, that ruling covers every order at once.

## 5.12 What the framework actually predicts, and what is only an identity

§5.8 warns that a framework which accommodates anything predicts nothing. Open item 6 asks where
the dependent pairs go — and answering it says which half of this construction has content
(`forced_pairs.mjs`).

**The dependent pairs are forced.** Measure the n − 1 consecutive composites and every other pair is
their product: c₁₄ = c₁₂·c₂₃·c₃₄. So n = 10 gives ninety ordered pairs of which nine are
measured and
**eighty-one are predicted**; n = 50 predicts 2,401 of 2,450.

**And that sounds like a great deal more than it is.** Put to an ISO thread, the worst
relative error across all pairs is 1.6 × 10⁻¹⁶. Put to anthropometric means, 2.5 × 10⁻¹⁶. **Both
exact — and the second is the important one**, because those measurements were not chosen to
satisfy anything.

> A chain of ratios among fixed numbers is **always** consistent, whatever the numbers are.
> v₁/v₄ = (v₁/v₂)(v₂/v₃)(v₃/v₄) is an identity. **The forcing is a tautology within one reading and
> says nothing about the world.**

**What has content is the grouping, and only across instances.** The framework says composites *inside*
a hold must repeat as instances change, and composites *crossing* one need not:

| across four bolt sizes | | | | |
|---|---|---|---|---|
| H/h₃ — inside the pitch | 1.41178 | 1.41178 | 1.41178 | 1.41178 |
| H/D — crossing to the diameter | 0.14434 | 0.12990 | 0.10825 | 0.09623 |

**The first is constant and the second is not, and the arrangement said in advance which would be
which.** That is a prediction, it is checkable on any set of instances, and it can fail: a
composite inside a hold that varies across instances refutes the grouping.

> **Open item 6, answered.** The dependent pairs are forced, and the forcing predicts nothing on its
> own. **What predicts is the grouping — which composites stay fixed as instances change — and that is
> falsifiable.**

## 5.12a Change stays local

§5.10 says local structure is independent of global. That is worth measuring rather than
asserting, so a hundred freedoms in ten groups were built and then mutated
(`mutate.mjs`). Nine thousand nine hundred ordered pairs; count how many move.

| the change | composites that moved |
|---|---|
| **one item** | 198 of 9,900 — exactly 2(N − 1), which is 2% |
| **a group's hold**, set to 999 | **0** |
| **the top hold**, set to 0.004 | **0** |

**A hold can be replaced and nothing built on it shifts.** The group hold cancels inside its group
and its residue is repaired from above; the top hold appears once above the line and once below
in every repair, so it never survives to be changed. **The centring test of §3.1, at the scale
of a whole arrangement.**

**And the reach of a real change shrinks as the set grows:**

| freedoms | pairs | moved by one freedom | fraction |
|---|---|---|---|
| 20 | 380 | 38 | 10% |
| 100 | 9,900 | 198 | 2% |
| 1,000 | 999,000 | 1,998 | 0.2% |
| 10,000 | 99,990,000 | 19,998 | 0.02% |

> **The more freedoms, the smaller the reach of a change.** One item touches 2/N of the
> composites, and a change to any *hold* touches none of them at any size.

**Which is what makes arbitrary scale affordable, and it is not the obvious reason.** Not that a
grouping is cheap to build — it is cheap to **change**. And the reason is the one that has been
running through the whole paper: **a denominator that appears once above the line and once below
has nowhere to propagate from.**

**And the robustness is bounded, at exactly the place this paper has always put the boundary.** Set
a hold to **zero** and it is not a change of value at all:

| | |
|---|---|
| a group hold set to 0 | 1,890 of 9,900 composites undefined |
| one item set to 0 | 99 undefined, and its other pairs read nought |
| the top hold set to 0 | 9,000 undefined |

**A hold of zero is the horizon.** The reading it was supporting has no denominator, and §6 says
composition stops there. Nothing is broken by the arithmetic — the arithmetic is reporting that
the scaffold is *gone* rather than moved.

> **Any hold may be replaced by any other non-zero value and nothing moves. A hold replaced by zero
> takes its group with it.** Robust in the interior, undefined at the ends — which is where
> composition has stopped since §6.

## 5.12b Overlap, and what grouping can audit

Every grouping so far put each freedom in exactly one group. Let one belong to two and the
arrangement stops being a tree (`overlap.mjs`).

**Write the grouping as a graph.** Items, group holds and the top hold are the nodes; each reading —
the log of an item against its hold — is an edge. A tree has no loops, and every membership
beyond an item's first adds exactly one:

> **loops = memberships − items.**

**Routes still agree.** §5.10b found that every route between two freedoms gives the same
composite, and overlap does not disturb that: across 1,000 groupings with random holds the worst
departure of any route was 3 × 10⁻¹⁶. **And the shared item is a route of its own.** With x₀, x₁,
x₂ in one group and x₂, x₃ in another, x₀ → x₂ → x₃ relates two strangers without passing
through either group hold or the top.

**A loop sums its readings to nothing, and that makes it a check.**

| the change | the loop's closure |
|---|---|
| a hold scaled wherever it appears | **0** |
| an item scaled in both its groups | **0** |
| one reading on the loop off by ε | **ε** |
| one reading on no loop off by ε | **0** |

> **A loop audits readings, never holds or items.** What a party brings cancels around it; what a
> reading owns does not — *The Closure Phase*, found inside a grouping.

**Which readings can be audited is fixed by where the loops run.** With three shared items — x₂
in groups A and B, x₃ in B and C, x₁ in A and C — nine memberships over six items give three
loops, and:

| a reading of | what the loops can do |
|---|---|
| an item in one group | **nothing** — it is on no loop, and an error in it is invisible |
| an item in two groups | **detect** an error, not say which of its two readings holds it — both sit on the same loops, opposite in sign, and an error's sign is not known |
| a group hold against the top | **detect and name** — each sits on a pair of loops no other reading shares |

**Under a grain, a loop's closure is a count.** Keep each reading to the nearest step of σ. A
clean loop of L readings then closes on a whole number of steps k, with **|k| ≤ ⌈L/2⌉ − 1** and
an rms of √(L/12) steps. For four readings:

| step σ | closures at −1 · 0 · +1 | at ±2 | rms, in steps |
|---|---|---|---|
| 0.05 | 0.166 · 0.678 · 0.156 | **none** | 0.571 |
| 0.2 | 0.164 · 0.668 · 0.168 | **none** | 0.578 |
| 0.693 | 0.163 · 0.676 · 0.162 | **none** | 0.580 |

Shares from 2,000 clean loops each, against an rms of √(4/12) = 0.577 predicted.

> **On a loop of four readings, a closure of two steps is not grain.** For a reader that
> quantises, the threshold for refuting a reading is a count rather than a statistic.

**⚠ What no loop can see is an item in the wrong group.** Moving it changes which hold cancels and
nothing else, so every loop still closes. Grouping is still decided only by §5.12's test across
instances.

## 5.12c Under a grain

Everything above is exact. For a reader that keeps its readings at a grain, two things change, and only
one of them survives a change of how readings are stored (`overlap.mjs`, `depth.mjs`,
`storage_compare.mjs`).

**Holds must sit within the storage's range of their members.** A hold moved a thousand times away from
its members still cancels exactly in value, but its readings leave any finite store's range and the
answer is lost: the error equals the whole span. So §5.12a's "a hold can be replaced and nothing moves"
holds for value, and under a grain only for replacements that keep the readings in range. This holds
for every storage tried.

**How deep a chain should be depends on the storage, and nothing else.** Kept as fisheye angles, u = atan
s, a reading d from its corner has error proportional to 2 cosh d, which gives a best reading span of
d* = 0.7717 (d · tanh d = ½). Kept as ln s on a uniform grid, every reading has the same error, and the
best chain is the shortest that fits the range. At 256 levels a span of 10 needs 13 angle readings for
an rms of 0.017 and 2 log readings for 0.016. **So d\* is a property of rounding in angle, not of
scaling**, and which storage a serial reader has is flagged in §8, item 12(c).

## 5.13 Structures, not shapes

Enough shapes have turned up here — a turn, a quarter, a spherical triangle, a grouping — to raise
the question of whether freedoms *make* shapes. The answer splits, and the split is the useful
part (`shapes.mjs`).

**What is forced needs no measure at all.** A freedom has two ends; signs give four copies and no
fifth; the copies join, because the far end of one *is* the near end of the next with the roles
swapped; four steps return, since each sign must flip twice; three pairs cover a sphere, since
no direction is blind in all of them; grouping sorts independence, (n − g) + (g − 1) = n − 1.
**Every one of those is counting.** Not a line of it mentions a length, an angle or an area.

**What a shape needs is a measure — and in its own measure, a freedom has no shape.** m[a, b] =
ln(b/a) gives 0.6931 from 1 to 2, 6.9078 from 1 to a thousand, and **infinity to either
horizon**. So each copy holds infinitely many addresses, the joins lie beyond ever denser crowds of
them, and counting addresses alone never comes round to anything — though the extent they are hung
on is a quarter turn apiece (§5.16).

> **The turn closes by counting — four flips and you are back — and never closes by distance.**

| | freedoms form |
|---|---|
| **structures** | natively and by force: joins, returns, coverings, groupings |
| **shapes** | only once a measure is imported — the circle, the quarter, the spherical triangle, π/2 |

**The shapes are real and they are not native**, which is not a complaint. The borrowed measure is
what makes them drawable, and drawing is how anyone sees a structure at all (§5.8). But a
freedom left to itself has a shape only in the sense that a list has one: an order, a set of
joins, and no size.

**And the two measures disagree exactly where it matters.** Borrowed, the horizon is a finite
distance off and the turn is closed. Native, the horizon is infinitely far and nothing closes at
any finite distance. **They agree about what joins what and disagree about how far.**

**The clearest case of that is what happens at four signed terms** (`sixteen.mjs`). The structure
continues without a hitch: sixteen regions, three freedoms apiece, a closed walk of sixteen
steps, four charts to cover it — all counting. The *shape* does not: in the borrowed measure two
and three terms both give π/2 per region, and four gives **π²/8 = 1.2337**. **The tidy number
stops at three, and nothing structural stops with it.** That is the strongest evidence here that
the shapes are the imported half.

> **A shape is a structure plus a choice, and the choice is the thing to declare.**

## 5.14 The n-cube prediction

The join rule is forced (§5.1), so the adjacency is forced with it — and that is the sharpest
prediction in this paper, because it is about **structure** rather than arithmetic and can be
checked against a system nobody here arranged (`ncube.mjs`).

**If a system is n signed terms against a shared hold**, its states are the sign patterns and two
states are adjacent exactly when one term crosses its hold. So:

| | |
|---|---|
| states | **2ⁿ** |
| neighbours of each state | **n** — no more, no fewer |
| joins in all | **n · 2ⁿ⁻¹** |
| shortest closed tour of all states | **2ⁿ**, and it exists |
| states at distance d | **C(n, d)** |

**And each way it can fail names what is wrong**, not merely that something is: a state with n + 1
neighbours means two terms crossed at once, so they are not independent signed terms; fewer than
n means some term cannot cross, so it is not free; no closed tour means the parity argument
fails; distances that are not binomial mean the terms are coupled.

**⚠ And this is where it stops today.** Put to four on/off terms every number comes out — 16 states,
4 neighbours apiece, 32 joins, a closed tour of 16, distances 1, 4, 6, 4, 1 — **but that system
was built from four binary terms, so of course it does.** A constructed n-cube is an n-cube by
assumption, and every system available here is one I would construct.

**What would make it a test** is a state graph given from outside: a machine with n independent
faults, n binary clinical indicators, n switches on real equipment. In each the prediction says
**every state has exactly n neighbours and every transition flips exactly one term** — and a single
observed transition that flips two, or a state from which some term cannot be flipped, refutes
the arrangement.

> **Recorded as unfalsified, not as confirmed.** It is sharp, it is cheap to check, and it
needs data
> from a system nobody here arranged.

## 5.15 Address and magnitude: one lens, two situations

> **(1 Oct)** "Two situations" here are serial and parallel; both are now situation 3 (R152), and "no home, no fulcrum and no horizon" in the parallel account describes the view from nowhere instead. In §5.15e–i, "density" is dropped (R124); "any breadth can be normalized to 1" holds for situation 1, not the fisheye, which cannot be normalised (R135); the half-Cauchy reached through arctan and 2/π uses the shortcut (R148). §5.15g, "the breadth is the world, the density is the reader", is the forerunner of the Sep 30 g; §5.15h–i, the Cauchy fixed by a breadth and one number, anticipates R147 and situation 5; and §5.15h's reader that never fails to see the corner and never sees the horizon is R149.

§1 defines a freedom as **an address to a magnitude, not the magnitude itself.** This section says
where the two words come from, and it draws on four earlier papers in this series rather than
repeating them: *The Relation Space*, *The Six Things*, *The Unit Rule* and *The Cauchy*.

**Start from a reader holding both terms at once.** It has the magnitudes, and it can point at any
of them directly, so it needs no address. A reader holding one term and receiving the other has
lost that: the division cancels what arrives into a ratio against what is held. What it has
instead is **where each arrival sits relative to its hold**. The address is what the reader gets
in place of the data.

### The two situations

**Parallel: everything held at once.** A list of magnitudes, a recorded waveform, a drawn shape.
Nothing is expressed in terms of anything else, so no term is the denominator, and there is no
home, no fulcrum and no horizon — *The Relation Space* §6: every landmark is a consequence of
reading in order, and the parallel account has none. It holds the figure and cannot state a rate.
Four things belong to it alone (*The Six Things* §8): **totals, closure, the far end named, and the
figure.**

**Serial: one value at a time against a hold.** The held term is the denominator not by choice
but because it is the one standing there when the other arrives (*The Cauchy* §3). Here the
landmarks appear, the horizons with them, and a rate can be stated.

> **Serial arrival trades data for address.** The parallel account holds the magnitudes and has
> no addresses; the serial reader holds addresses and has lost the magnitudes.

### What each reading cancels

The trade is not one price but three, according to what is divided by what (*The Six Things* §8):

| the reading | what cancels | what remains |
|---|---|---|
| two components of one reach, divided — **the Cauchy** | the figure and the scale | the address: a direction, a rate, a bearing |
| a single list, each value against the last held — **the Unit Rule** | the gain only, one number | the figure, as a record of addresses |
| the list held whole — **the parallel account** | nothing | the figure, and no rate |

**The Cauchy end.** Up and across are one reach measured two ways, so their ratio is the tangent
of the turn and the reach cancels **in every reading, not on average**: five figures read in the
same 100,000 directions agree arrival by arrival to 7 × 10⁻¹² (*The Cauchy* §11). The figure is
not flattened; it was never sent. What arrives is where a body's centre of gravity lies and how it
moves: four bodies with identically orbiting centres — a disk, a ring, a bar, a lopsided disk —
return periods of 194.4, 193.3, 196.8 and 195.8 against 200 (*The Cauchy* §14c).

**The Unit Rule between.** *Hold the value that filled you, until the next observation.* Each
arrival is read against the hold and the record keeps a symbol — how many steps away it fell. Seen
through the lens, that symbol is a fisheye address: the step for a ratio r sits at atan r, and a
signal at 6 millivolts and at 6 volts lands in the same place, **because the lens strips the gain
in the act of pointing** (*The Unit Rule* §7). The record is the nearest-step projection of the
signal and does not drift — error in the last tenth of a run against the first, 1.03× over
fifty-six scenes (§15). Summed from the first sample it gives the magnitudes back within a step,
**r = r₀ · exp(σ · Σℓ)**: the figure, short of one number.

**And the circle is the identity of the addresses.** Read from its centre, a circle is all corner:
every look lands on *nothing changed*, and the record is empty. A figure is what departs from it.

### The serial situation, made from parallel data

Nothing stops a reader holding data in parallel from walking it through the lens. Then the
addresses the walk produces **point into data already possessed**, and nothing needs recovering,
because nothing was lost.

- **The Unit Rule's form.** The record lacks exactly one number, the value at home. A reader
  holding the list has it, so **the record plus one held value points to every magnitude.**
- **The Cauchy's form.** An address on the lens names an element of an array held behind it, and a
  view reads only the elements its addresses name — a fixed cost per view, whatever the array's
  size (*Browsing the Fisheye*). Not a recovery: the list was in hand throughout.
- **The editor's reading view draws it.** The circle is the address space, the shape is the held
  data, each ray is an address pointing at the magnitude it stands for, and as the shape is
  rescaled the addresses on the circle do not move.

> **A freedom is this indirection.** The serial reading makes the address, the parallel account
> holds the magnitude, and the freedom is the pointer between them. An address with nothing behind
> it is only a name (*The Cauchy* §14d); where something holds the data it points into, it is worth
> everything.

### Completion

**The whole figure is the complete set of composites, which is the parallel account — and it is
available only once the signal has fully arrived and the horizons are resolved.** Completion is
what clips the run: a drawn figure has had its approach to the horizon clipped by being drawn,
where a serial run never is (*The Cauchy* §11).

**And completion is inferred, never observed.** A serial reader cannot tell *not yet* from
*never*. Its record carries two checks — the symbols sum to zero if the scene returned, which is
blind to order, and the landmark sequence returns, which is not — and their strength is one-sided:
**an open record proves the scene did not return; a closed record does not prove it did** (*The
Unit Rule* §17). For a Cauchy stream, what one completed lap certifies is the **frame**, not the
figure: the reader counts arrivals between its home event and its horizon event, both in its own
alphabet, and holds at half the count (*The Lap Rule*).

**Where the data are held in parallel, the horizon problem is gone.** Every address, however near
the horizon, has something behind it. The held data resolve the horizons that no amount of serial
arrival can.

### Why the Cauchy turns up everywhere

The Cauchy is what a direction met evenly looks like when read as a ratio against a line, and
that situation is common. The ratio of two independent standard normals is a standard Cauchy; light
leaving a point evenly in angle strikes a straight wall with a Cauchy distribution; a Brownian path
started above a line first meets it at a Cauchy-distributed place; and the Lorentzian line of a
resonance is the same curve. **It turns up wherever something reads a direction without a
scale.**

**⚠ And that makes it weak evidence about the world.** It says the reading was of a direction, not
what was turning: a clover and a circle give one stream. Its structure is easily found — the
cross ratio comes out exact on white noise as readily as on a tone, and what separates them is
order, not the distribution. And a departure from it names no cause: a circle read on an uneven
clock departs four times as far as a clover read correctly (*The Cauchy* §13).

## 5.15a ⚠ Three levels, and which results belong to which

**Tom, Sep 21** (§9.7ac, B238–B241). *"There are three things here: the quarter turn, the quarter
turn with the hangers constructed, and the quarter turn with magnitudes hanging on the hangers."*

| | | where it comes from |
|---|---|---|
| **1 the turn** | the address space, [0, ∞), there whether or not anything is placed on it | **forced** — it is what a freedom is (§1) |
| **2 the hangers** | gN placements across it. A frame, nothing hung yet | ⚠ **N identified, gN chosen** — see §5.15b |
| **3 the magnitudes** | what hangs | **given** — they arrive |

**The addresses belong to the FRAME and the residues to the FIGURE** — change the frame and the
addresses move by 113.3558 while the residues move by 0.1691; change the figure and only the residues
move. *Level 3 cannot be read until level 2 has chosen where to sample.*

**⚠ Which reattributes three of this paper's results.** *Closure and the facing* (§5.18a), and *the
Cauchy from counting* (§5.18), are **level 2** — decided by where the hangers went, blind to what
hangs there. They have been written as though they were about a figure or a world.

**And level 2 is the chosen one.** `arch.js` lists the four choices in its own header: that the array
goes on the turn at all, that hangers are **evenly** spaced, that index order runs with arc order, one
value per hanger. **The grain is the sharpest case** — two frames with the same N share the same
(π/2)/N of 0.196350 and have gap ratios of **1.0000 and 4.8363**.

> ***(π/2)/N describes an even frame, not frames.*** It is an average gap, and this paper quotes it as
> a spacing. **Every result quoting a grain, a facing or an index inherits a choice that nothing above
> or below it forces.**

**⚠ That suspicion is now measured, and it was right — see §5.15k.** *Closure admits an infinite
family of frames; the even one is merely the one a reader holding N alone can build.*

**⚠ And the levels name the two readers.** The **serial reader is level 3 without level 2** —
magnitudes with no frame — which is why N is unknown to it, why it has no facing, and why everything
it computes is scale-free. *Those are not three properties of a serial reader; they are one missing
level.* The mirror case, **a frame with no figure**, this paper has never named: `centring` is exactly
that object and is called scaffolding without being called a level.

**⚠ Not shown:** that level 1 is free of the other two. The turn is [0, ∞) *under the tangent*, and
§5.11's note found the tangent carries no structure across — so whether *the turn* is a level or a
**picture** of the ray is unresolved.

## 5.15b ⚠ Inside the frame: N is identified, gN is chosen — and g is not free

**Tom, Sep 21** (§9.7ad, B242–B245). The middle level has two steps and they carry different risk.

**N is IDENTIFIED** — by counting a list in hand, by closure (§5.18a), by a past lap. Each is correct
when it fires. ⚠ **A prior is not an identification**, and the two worst failures this paper records
are both this step: a window centred on 80 returning a confident **76** for a true 64, and a fidelity
of 3e−2 declaring closure at **7** for a true 48. **gN is CHOSEN**, and a choice cannot be wrong.

> **N is where a frame-building reader can be *wrong*. g is where it can only be *costly*.**

**⚠ And g is not the free dial §5.16 treats it as.** Thinning to gN preserves closure **only when the
kept places are whole facing pairs**:

| keep, from 12 | places | closes? |
|---|---|---|
| every other — 0,2,4,6,8,10 | 6 | **no**, 5.45e+0 |
| three whole pairs | 6 | **yes**, 3.11e−15 |

Enumerating all 4,095 subsets at N = 12: **every odd gN has zero closing subsets, and every even one
has exactly C(N/2, gN/2)** — the closing subsets *are* the pair-choices, on every row.

> **Closure quantises g to multiples of 2/N.** At N = 12: 0.1667, 0.3333, 0.5000, 0.6667, 0.8333,
> 1.0000 — and nothing between. *The dial has half the detents this paper assumes.*

**⚠ And gN is a subset, not a count.** The same g taken two ways gives a closed inventory (3.11e−15)
or an open one (5.450084). *§5.16 writes ⌊gN⌋ as though the number decided it; it does not.*

**And for a reader that does *not* need closure, g is free of validity and never of capability**
(§9.7ae, B246–B249). Every one of the 4,083 thinnings gives a consistent residue reading — *which is
telescoping, not a property of thinning, and worth nothing.* What it costs is measured:

- **every summary moves.** Five valid readings of one figure give interquartile ratios of 7.2734,
  1.7460, 3.0159 and 3.1385. *The invariance belongs to the quantities, never to what is computed over
  them.*
- ⚠ **and the band becomes a function of g.** A planted coincidence survives **1.5%** of thinnings at
  gN = 2 and **100%** at gN = 12. **§5.18's band is not a fixed hazard of a bounded reader —
  coarsening manufactures it.**

> **The two channels constrain g in opposite ways.** The address channel says *which* thinnings are
> allowed at all — 63 of 4,083. The residue channel allows every one and charges for each. *A reader
> with a facing has few choices and clean ones; a reader without has every choice and no free ones.*

**⚠ And it cannot detect that its g has hidden one** (§9.7af, B250–B253) — for a reason stronger than
*no statistic works*. Drop the partner place and the reading is **bit-identical** to the reading of a
world with no coincidence in it. *There are not two readings to separate.*

**What it can do is price the blindness exactly, because g is its own dial.** A reader keeping m of N
has seen **C(m,2)/C(N,2)** of the pairs — matching the enumerated share on every row. And with memory
k as well the two limits **compose as a conjunction, not a product**: **km − k(k+1)/2** over C(N,2),
where multiplying the separate shares gives 0.1928 for a true 0.2727.

> **The report it can always file:** *"I kept m of N and held k, so I checked km − k(k+1)/2 of the
> C(N,2) pairs and nothing about the rest."* Every term is its own — m and k are its dials, N is
> identified at §5.15b — and the fraction needs nothing from the world.

**And thinning is the worse blindness.** Full memory over 6 kept places sees 15 of 66 pairs; all 12
kept with memory 4 sees 38. *Thinning deletes pairs outright; memory only defers them, for a reader
that could go back — which the serial reader cannot.*

### ⚠ 5.15c And g is a discreteness dial, read inversely

**Tom, Sep 21** (§9.7ag, B254–B257). Everything above reads g as *how many places*. It is better read
as **how coarse the step is**, and inversely: **D = (π/2)/gN**. *That says what g **is** rather than
what it counts* — and both of its limits turn out to be **baseline** statements.

| | the ruling | what a finite reader gets |
|---|---|---|
| **g → 0** | D → ∞ | unbounded from **g < 1/N**, not from 0 — *this paper's dead band, restated as a fact about the step* |
| **g → 1** | D → 0 | **D = (π/2)/N and no smaller.** "Infinitely small" is the N → ∞ column, which is the continuous observer |

**⚠ And the dead band is a property of the pair (g, N), not of g.** The same g = 0.04 places nothing
at N = 12 and gives 400 places at N = 10,000. *It empties as N grows.*

**⚠ A closing reader cannot reach the coarse end at all, and §5.15b's parity is re-derived from the
dial.** Laying each gN as an even frame and testing intrinsic closure: **every odd gN fails outright**
— at odd gN the middle place sits at turn π/4, **address exactly 1, its own reciprocal**, so it has no
*distinct* partner and the list cannot pair off at any tolerance. *The obstruction is a place, not a
count.* The coarsest closed reading is therefore **two places, D = π/4 = 0.785398** — the corner pair.

> **The dial does not run to zero. It stops at the corner, and it stops there for the reason the
> corner exists.**

**⚠ And "discreteness" has three answers.** D is a step **in the turn**, and the reader holds
addresses while this paper measures in ln(b/a) (§5.7). At gN = 64: the turn is **uniform**, the raw
address spans **×2212.3**, and the log address spans **×22.4**. *Neither extreme is the corpus's own
channel.* The log steps do not converge either — the largest stays near 1.10 at every gN while the
smallest halves. **Turning the dial up refines the middle and leaves the outermost step where it was:
the horizon is not brought closer, only approached with more places.**

### ⚠ 5.15d The same dial named the other way — continuity, and why it is not 1/D

**Tom, Sep 21** (§9.7ah, B258–B261). *"Or continuity is infinitely small at 0 and infinitely large at
1."* If continuity were **1/D** this would be one notion with two names. It is not, and the way to
see it is to define continuity **operationally** — how well a reader reconstructs a magnitude
arriving *between* its places — and measure it rather than derive it.

| reader, same dial and same places | error per doubling of gN | so continuity goes as |
|---|---|---|
| **snaps** to the nearest place | ÷2.02 | 1/D |
| **interpolates** between two places | ÷4.06 | **1/D²** |

> **Discreteness is a property of the frame. Continuity is a property of the frame AND of what the
> reader does between the places.** *So the ruling fixes both ends and does not fix the dial between
> them: the rate belongs to the reader, not to g.*

**⚠ And continuity does not rise monotonically.** Eight places against a world carrying a cos(7u)
term gain **÷2.52** for a doubling where every other step gains ÷4 — and the stall is absent on two
other worlds. *A frame can beat against a feature of the world, and the reader, which does not hold
the world, cannot tell that is what happened.*

**The low end is sharper in this naming.** Below g = 1/N nothing is placed, so continuity is **exactly
0** — not a limit. *The discreteness naming needed an ∞ there; this one gets a plain zero, and
§5.15c's dead band is the same fact in both.*

**⚠ And the two words disagree about channels, which is the sharpest separation of the pair.**
Discreteness differs by **×2212** between the turn and the raw address at gN = 64; continuity differs
by **under 1%** on the same frame. *Not because nearest-place is channel-free — it flips 10.11% of
the time at gN = 4 — but because a flip happens only near the midpoint, where the two candidate
places hold nearly equal values.* **Spacing is violently chart-dependent; nearness is barely so.**

**And a closing reader has a continuity floor**: it stops at the corner pair (§5.15c), so its
continuity never reaches zero. *Holding a closed shape means holding some continuity.*

### ⚠ 5.15e Why a density must be picked at all — and where that belongs

**Tom, Sep 21** (§9.7ai, B262–B266). *"[0, π/2] represents the complete relation set between v and h.
Two endpoints. Infinitely dense, not infinitely broad — two types of infinity, and this is the
former. The generator must create the complete relation space, but infinite density can't be
represented. You have to pick a density."*

**The quarter turn IS the relation set, not a chart of part of it** — 199,999 distinct turns give
199,999 distinct relations with no collisions, and the round trip from (v, h) and back is exact at
the corner. *⚠ It degrades to 7.81e−8 by v/h = 1e9, which is the density claim arriving as
arithmetic: the completeness is exact in the mathematics and approximate in any representation, and
it fails first exactly where the crowding is worst.*

**⚠ And "dense, not broad" is a fact about the PRESENTATION.** The turn is bounded (π/2) with density
1 + s²; the address has density 1 and infinite extent; the log address has unbounded extent and
density s. **No channel bounds both**, because a finite extent holding infinitely many relations must
crowd.

**⚠ And the two infinities are not a symmetric trade — §5.15f.** *Density is a **child** of breadth.*

> *And the log address is exactly the geometric middle: turn density 1 + s² against log density s.
> That is why §5.15c found ×2212 in the raw address and ×22.4 in the log on one frame — the log
> channel sits at the square root of the distortion, by construction.*

**⚠ "You have to pick a density" is forced for an EMITTER and false for a RULE.** atan(v/h) carries
the complete set to 3.71e−13 over 100,000 arbitrary queries and has no density at all — but a rule
must be **queried**, at a relation of the asker's choosing, and that is parallel access. *A serial
reader receives what arrives and cannot ask, so for this paper's reader the escape is closed.*

**⚠ Which adds a level §5.15a did not have:**

| level | | |
|---|---|---|
| 1 | the turn, complete and dense | forced |
| **1½** | ⚠ **that a density must be picked** | **forced** |
| 2 | *which* density: N identified, gN chosen | chosen |
| 3 | the magnitudes | given |

*§5.15b's "gN is chosen" stands. The **necessity** of choosing is not the choice, and it is forced by
the density of the set against the finiteness of the emitter.* **The dial is not realism added to an
ideal picture — it is the only way a finite emitter stands in for a dense set.**

**And no picked density delivers the complete set, in a sharper way than measure zero.** An offset
frame reaches neither endpoint; an inclusive one reaches both and **cannot address one of them**
(turn 0 has address Infinity). *The set is complete because of its endpoints, so every reading holds
the open interior and leaves the two relations that close it outside.*

### ⚠ 5.15f Density is a child of breadth — establish the breadth first

**Tom, Sep 21** (§9.7aj, B267–B270), correcting §5.15e. *"Infinite density is different than infinite
breadth. Infinite density is a child of infinite breadth. First establish the breadth, then the
density within that breadth."*

§5.15e read the two infinities as a **symmetric trade** — pick your channel. **That is the wrong
shape, and the parent/child reading forbids something the trade does not**, so it can be put at risk:

| | |
|---|---|
| **the density integrates to the breadth** | 1.91e−12 mismatch at worst, on every stretch tested |
| infinite breadth **without** infinite density? | **yes** — the address channel, density 1 everywhere |
| infinite density **without** infinite breadth? | **no** — a bounded set [0, M] is capped at 1 + M², in every presentation |

> **There are not two infinities. There is one — the breadth — and the density is what it looks like
> folded into a finite extent.** *Nothing is paid: the breadth is **conserved**, and ∫density du
> returns it exactly. The turn is not crowded as a property of its own; it is crowded because of
> what it carries.*

**"No channel bounds both" survives with a better reason** — it is now a consequence rather than a
coincidence. *The breadth is infinite, any presentation of finite extent must absorb it, and the only
place left to put it is the density.*

**⚠ And the ordering is not a preference — the reverse has no referent.** "A density of 8" is a step
of **0.098175**, **0.195100** or **0.196350** depending on a breadth that has not been named, and the
number 8 chooses none of them. *A density is a ratio against an extent, so it cannot be picked before
the extent exists.* **Which puts the three in sequence rather than in layers:**

| | | |
|---|---|---|
| **1 the breadth** | [0, ∞), the complete relation set | forced — **the parent** |
| **2 the extent** | present it as [0, π/2] (§4.3) | the fold; **density appears here** |
| **3 the density** | gN places within that extent | chosen, and only now defined |

*§5.15e's level 1½ stands but moves: "that a density must be picked" is **downstream** of the
breadth, not beside it. The necessity is inherited from the parent — which is what a child is.*

### ⚠ 5.15g The breadth is the world, the density is the reader

**Tom, Sep 21** (§9.7ak, B271–B274): *"I think the concept of breadth and density is central to this
entire corpus. The breadth is the world, the density is the reader."*

A **factorisation** claim, and it predicts two invariances. **Both hold:**

| | |
|---|---|
| reader operations → the world's **breadth** | no effect — and the reader **understates** it, monotonically, with **not one overshoot in 20,000 draws** at any density |
| world operations → the reader's **density** | no effect, bit-identical across five worlds — *while an **adaptive** control reader, setting its step from the observed spread, moves on two of them* |

**The asymmetry is the content:** *the reader cannot change the breadth and cannot fully see it; the
world cannot change the density and does not need to.* And **the shortfall has a sign** — a subset's
extremes lie inside the full set's — which makes it a limitation of **access** rather than a
distortion. **A reader can be sure the world is at least as broad as it reads, without holding N.**

> *The control is what makes this a result and not a restatement. "The density is the reader" is a
> claim about **this** reader: §9.7ab's "g is its own dial" is the assumption the factorisation rests
> on, and the adaptive column shows what the corpus would look like without it.*

#### ⚠ And N belongs to neither — which is why §5.15b is true

| | breadth | density | **N** |
|---|---|---|---|
| the reader thins to g = 1/2 | no | no | **moves** |
| the world gains magnitudes **inside** its range | **no** | no | **moves** |
| the world gains magnitudes **outside** its range | moves | no | **moves** |

**The density never moves; the breadth moves on one row of three; N moves on all three.** *N is not
a third kind of thing beside them — it is **the place they meet**.*

> **Which gives §5.15b its reason.** "N is where a reader can be **wrong**; g is where it can only be
> **costly**" was an observation. Now: **g is purely the reader's, so there is nothing outside it to
> disagree with. N is a world fact the reader must supply, so it is the only place disagreement is
> possible at all.** *Both of the worst failures in this paper are N errors — 76 for a true 64, 7 for
> a true 48 — and there is no g error anywhere, because there could not be.*

**⚠ And anything defined *through* N inherits N's position.** The grain (π/2)/N is reader-side while
the reader **holds** its N, and belongs to neither the moment N tracks the world. *The clean two-way
split is the split of a reader that has already fixed its N.*

### ⚠ 5.15h Four cells, not two — and where the quarter turn comes from

**Tom, Sep 21** (§9.7am, B275–B279), correcting §5.15g and then adding a construction.

**The world has infinite breadth AND infinite density; the reader has a finite amount of each.**

| | the world | the reader |
|---|---|---|
| **breadth** | ∞ *(a premise)* | 4.969813 — finite |
| **density** | 100,000 distinct relations in a window of 1e−9 | 8 places, step 0.196350 |

*§5.15g binned these as two quantities on two sides. Each side has both, and what differs is
finiteness.* **What §5.15g actually established survives as the sharper claim: the reader cannot
move the world's breadth, and the world cannot move the reader's density — ownership, not
possession.** *And the world's column is a premise rather than a result: no finite computation shows
a window holds infinitely many relations.*

#### The quarter turn, constructed

**A breadth carries no v and no h on its own. Add a facing point C that every position faces, and
each position acquires a direction — which has both.** With C at height d above position 0, the
facing from position x is (−x, d), so h = |x| and v = d:

- the half-breadth [0, ∞) maps onto the quarter turn **(0, π/2] exactly once**, round-tripping at
  2.30e−16
- **the corner falls where the position's offset equals the facing distance** — v = h
- the *other* half does it again: positions −3 and +3 both address 3.0000

> **"The sweep of the horizontal line into the vertical line" is literal — and the fold is not a
> convention this paper adopted. It is what a breadth does once it has a facing in it.**

#### ⚠ And what the finite reader gets

**A finite breadth gives a partial arc, missing always the same end.** |x| ≤ 100 covers **99.36%** of
the quarter turn — and **0%** of the address line, at every finite reach. *Same reader, same reading:
nearly all of it or none of it, depending on the channel.* What it misses is [0, arccot L], **the
relations nearest the horizon**. *§5.15g's one-sided shortfall, as geometry: a finite breadth never
fails to see the corner and never succeeds in seeing the horizon.*

**⚠ And the facing distance is a third reader quantity, previously unnamed.** Only the ratio
breadth/d matters: |x| ≤ 10 covers 99.36% at d = 0.1 and **6.35%** at d = 100. *A wide reader
standing far off sees what a narrow one standing close sees.* **This paper has been carrying "the
breadth" without its denominator, and the denominator is where the reader stands.**

#### ⚠ And the fisheye arrives here too, from geometry alone

Positions spread **uniformly** along the breadth land **95.82%** in the sixth of the arc nearest the
horizon. Inversely, nine **even turns** read off as positions 11.43, 3.73, 2.14, 1.43, 1.00, 0.70,
0.47, 0.27, 0.09 — median exactly 1.0000, a Cauchy spread.

> **An even frame on the arc is a Cauchy-spread sampling of the breadth; an even sampling of the
> breadth is a crowded reading of the arc. Neither is neutral.** *The same lens §9.7m reached by
> counting, reached again by a route with no observer in it at all — only a facing.*

### ⚠ 5.15i Breadth to 1, then density as the arc over that line — which is the kernel itself

**Tom, Sep 21** (§9.7an, B280–B283): *"Any breadth can be normalized to 1. Any density can then be
normalized as the arc over that line. So, breadth first, density second."*

**The normalisation is free and it is not empty — it moves everything into the facing distance.**
Breadths of 10 and 50 at facings of 1 and 5 normalise to **the same reader** (d = 0.100000, arc
1.471128); equal breadths at different facings stay apart. *You can always set the breadth to 1. You
can never set both to 1.* **What survives is one number** — §5.15h's breadth/d with the breadth
divided out, and *"breadth first" is what makes that number well-defined.*

#### ⚠ And "the arc over that line" is the Cauchy kernel

Taken at a point rather than in bulk, arc-over-line is **du/dx**. Measured against a closed form with
no assumption about what that form should be — twelve points, **worst difference 4.21e−10**:

$$\frac{du}{dx} \;=\; \frac{d}{x^{2}+d^{2}} \qquad\text{and at } d=1, \quad \frac{1}{1+x^{2}}$$

> ***"Any density can be normalised as the arc over that line" is not a description of the fisheye
> and does not lead to it by an argument. It **is** the fisheye, written out.*** **The lens is what
> the word "density" means once the breadth has been fixed.**

**A third route to one lens, and the shortest.** §9.7m reached it by counting; §5.15h by the geometry
of a facing; this by taking *density* literally and differentiating — *with no observer, no counting
and no sampling in it.* And the integral is the arc: ∫d/(x²+d²) = arctan(x/d), reaching **99.9999%**
of π/2 by L = 10⁶. **Dividing by that total gives the half-Cauchy, (2/π)·1/(1 + x²)** — this paper's
own distribution, from normalising twice.

**⚠ And the one point where it breaks is the fold.** At x = 0 the measured density is 0.000000
against a closed form of 1.000000, because that is the point facing straight up and |x| has no
two-sided derivative there. *The Cauchy density is the **one-sided** density, and the corner of the
relation space is a corner of this function too.*

#### The third naming of the dial

**Density = gN/(π/2): exactly 0 at g = 0, and 7.639437 at g = 1 with N = 12 — not infinity.**

| naming | at g = 0 | at g = 1 | exact at |
|---|---|---|---|
| discreteness (§5.15c) | ∞ *(limit)* | 0 *(limit)* | **neither end** |
| continuity (§5.15d) | **0 exactly** | ∞ *(limit)* | the low end |
| **density** | **0 exactly** | ∞ *(limit)* | the low end |

*Three words for one dial. Continuity and density share a direction and a sharp low end; the high end
is the continuous observer in all three.*

**⚠ Not shown:** whether "breadth first" survives a reader that cannot see its own breadth.
Everything here normalises by L, which the reader must hold — and §5.15g found a finite reader only
ever **understates** it. *The normalisation a reader can actually perform is by the breadth it has
**seen**.*

### ⚠ 5.15j At d = 0 the density is 0 — and the facing must be off the breadth

**Tom, Sep 21** (§9.7ao, B284–B287). The kernel is d/(x² + d²) and its numerator *is* the facing
distance, so at d = 0 every position has density zero. **Exactly right, and exactly pointwise.**

**The geometry says more than the algebra does.** d = 0 puts the facing point **on** the breadth;
every position then faces *along* the line — all h, no v — and four positions spanning a factor of
2,000 give **one turn between them**.

> **Which names a condition this paper has been assuming silently: the facing point must be OFF the
> breadth.** *A relation space exists exactly when the thing being read and the place it is read
> from are not the same place. d > 0 is not a technical convenience — it is what makes there be
> anything to read.*

**⚠ But the total does not follow the pointwise limit down.** ∫₀^L d/(x²+d²) = arctan(L/d) gives the
whole quarter turn for **every** d > 0 — at d = 1e−6 the density at x = 1 is a millionth of what it
was and the arc is still π/2 — and 0 at d = 0. *A jump, not a decay: the kernel **concentrates**
into a spike of width d rather than fading, so everything survives to the bottom and is annihilated
there.*

#### ⚠ There is a best place to stand, and it is the corner

Differentiating the kernel in **d** gives (x² − d²)/(x² + d²)², zero at **d = x** — which is v = h.
The best density available at position x is exactly **1/(2x)**, matching at 0.00e+0 across five
positions.

> *Even standing ideally, a position ten times further off is resolved ten times worse.* **The
> horizon is hard to reach from anywhere, not merely from where the reader happens to be — and
> moving closer to one part of the breadth moves away from the rest. A reader cannot stand well for
> all of it at once.**

**⚠ And the two ends of d are not symmetric for a finite reader.** With an infinite breadth the arc
is π/2 at every d > 0. With a breadth of 100 it is **1.570796** at d = 1e−6 and **0.000100** at
d = 1e6. *Standing very close gives a finite reader the whole quarter turn; standing very far gives
it almost none.* **d = 0 is a discontinuity, large d a smooth fade — the reader is better off too
close than too far.**

*So what the facing distance sets depends on the breadth it is set against: for an infinite breadth
only **where** the resolution is spent, for a finite one **how much there is as well** — and the
finite case is the reader's.*

### ⚠ 5.15k The even frame is not forced — it is what poverty can build

**§5.15a suspected this** — *"every result quoting a grain, a facing or an index inherits a choice
that nothing above or below it forces"* — and §9.7ap (B288–B291) measured it. Two things could have
forced the even frame: **closure** or **accuracy**. Neither does.

**Closure is testing corner symmetry.** Two different spacings close — even-in-turn at **1.78e−15**
and even-in-**log-address** at **2.22e−16** — while the same log frame **offset from the corner by
0.3** fails at 7.17e+0. *The log frame closes not because it is logarithmic but because it is centred
on the corner — which is §5.18a's own condition, now separating two frames that differ in nothing
else.*

**And corner symmetry admits an infinite family.** Every frame built by mirroring turns about the
corner closes, including one with a **gap ratio of 20.66 built from random numbers**.

> **Evenness is not forced by closure.** *§5.15b's even **count** — gN even — is forced by the
> pairing and stands. The equal **gaps** are a separate claim, and closure does not make it.* **An
> uneven frame is a fully legitimate reader, not a degraded one.**

**Accuracy picks a match, not a frame.** Across four worlds the even frame wins two and loses two —
the corner-clustered world goes to the log frame at 0.015000 against 0.041092. *What wins each world
is the frame shaped like it, which is §5.15d arriving at the frame: the error belongs to the pair
(reader, world).*

**⚠ But the even frame is the minimax choice.** Its scores span a factor of **1.3**; the log frame's
span **28**. *Never best by much, never worst by much.*

#### What it actually has

| frame | what it needs to be laid down |
|---|---|
| **even in the turn** | **N, and nothing else** |
| even in the log address | N, and a **scale** — nothing in N fixes it |
| crowded anywhere | N, and a **shape** |

**The even frame is the only one a reader can build from N alone.** Every other closing frame needs a
second number that N does not supply and only the world could.

> **Forced by poverty, not by correctness** — and the two findings agree rather than competing: *the
> even frame is the only one a count can build, **and** the one whose worst case is bounded. The same
> ignorance that makes it the only option makes it the right one.*

### ⚠ 5.15l A frame cannot lift itself by its own readings

§5.15k left the obvious follow-up: if a world-shaped frame reads better, could a reader **learn**
one? §9.7aq (B292–B295) settles it, and the structure that decides it is **oracle versus real**.

**An oracle handed 200,000 unquantised draws gains ×4.41, ×4.42 and ×6.71 on three worlds and still
closes** — so adapting violates nothing the address channel requires. **A real reader, holding only
which of its 8 places each arrival snapped to, gains ×1.00 on three worlds and ×0.95 on the fourth.**

> ***A frame cannot lift itself by its own readings.*** *To place hangers where the world is, the
> reader must first see where the world is; to see that, it must already have hangers there. Every
> quantile it can compute is a quantile of its own frame.*

**⚠ And neither escape works.** Ten million arrivals leave **2 distinct values** in the record — on a
narrow world only two of the eight places are ever nearest, so *the record does not contain even the
reader's own frame, let alone the world.* Iterating is a **fixed point from round zero**, scoring
identically every round: the world is never in the loop.

#### The price, if a reader *were* handed the shape

| | even frame | adapted frame |
|---|---|---|
| closure | holds | **holds** |
| buildable from N alone | yes | no |
| §5.15g's factorisation | holds | **broken** |
| **two readers share a frame** | **0.000000** | **0.635771** |

**Closure is the one thing an adapted frame keeps.** What it loses — beyond N-buildability and the
bounded worst case — is **comparability**: two adapted readers' places differ by 0.635771, and their
index k means different things. *An index is communicable only because the frame is not a private
fact.*

> **So the even frame is what a count can build, what two counts can share, and what a reader cannot
> improve on from the inside.** *Three reasons, none of them accuracy.*

### ⚠ 5.15m A second reader — and what two readers actually share

§5.15l proposed the escape: two readers with **offset** frames. §9.7ar (B296–B299) refutes it and
finds something else.

**An offset frame does not close.** A shift of 0.01 — one twentieth of a gap — takes the residual
from **1.78e−15 to 1.86e−1**, because sliding an even frame moves every place off its own reciprocal.

> **Two closing readers at the same N and the same spacing rule have the *same* frame.** *Closure
> admits an infinite family of spacings (§5.15k) and, within a spacing, no freedom of placement at
> all — which is far more restrictive than it looked.*

**So a second reader must differ in spacing rather than in phase**, and that works: two
differently-spaced mirrored frames both close.

#### ⚠ And what they exchange repairs §5.15l

| what A sends | what B can use |
|---|---|
| "place k = 3" | **nothing** — A's is 0.687223, B's 0.775000, apart by 0.087777 |
| "turn 0.6872" | **everything** |

**An index is not communicable between them; a turn is.** *What two closing readers share is not a
frame — it is the **arc** and the **corner**: both run [0, π/2], both symmetric about π/4, because
that is what closing means.*

> **A shared reading rests on a shared arc with a shared landmark in it. The corner is not merely
> where v = h — it is the one place two readers can point at without agreeing on anything else.**

#### But the joint record does not break the bootstrap

**The pooled record scores 0.058445 — exactly what reader A alone scores.** And the records hold
**3, 2 and 5** distinct values against frames of 8, 8 and 16: *this world touches only a few places
of either frame.* **Pooling two readers pools what they saw, not what they could have seen.**

*The deadlock is not about how many places there are, or how many readers — it is about the record
holding **places** at all, and only those the world happens to touch.* **And a second reader can hurt:
reader B scores ×0.26, four times worse than not adapting, and nothing in the pooling knows which
one to trust.**

**⚠ Not shown:** readers that **ask each other questions** rather than pool records after the fact.
*That is a different machine, and it is the one `the-common-hour` is about.*

### ⚠ 5.15n Which density the Cauchy comes from — and it is not g

**Tom, Sep 21** (§9.7as, B300–B303): *"So the Cauchy comes merely from picking a density from 0 to 1
after you have normalized a breadth to 1."* **Exact — for one of the three things this paper now
calls a density, and two of them run [0, 1].**

| | what it is | range | whose | Cauchy? |
|---|---|---|---|---|
| **g**, the dial | places per quarter turn | [0, 1] | the **reader** | **no** |
| d/(x² + d²) | arc per unit line | a function | the **setup** | **it is** |
| **arc/(π/2)** | the total arc, normalised | [0, 1] | the **setup** | **fixes it** |

**Picking g gives nothing Cauchy.** ⌊gN⌋ positions on a line of length 1 — no arc, no turn, no v and
no h. *A breadth carries none of those on its own (§5.15j); until a facing maps position to
direction there is nothing for a distribution over directions to be about.*

**Picking c = arc/(π/2) gives the whole kernel.** c fixes d = 1/tan(cπ/2), and c = 0.5 gives
d = 1.000000 and **1/(1 + x²)** — the standard Cauchy. *The breadth is 1, so c fixes the only
remaining freedom, which §5.15i showed is d. Round trip 5.55e−17.*

> **The Cauchy is not something a reader produces by choosing how finely to read. It is there before
> the reader chooses anything — fixed by a breadth and one number saying where the facing is. g then
> decides how many places to put on a lens that was already shaped.**

**⚠ And c and 1 − c are reciprocal standpoints.** They give facings of 6.313752 and 0.158384 and
agree **exactly at the corner** (0.154508), differing everywhere else. *The facing swap is in the
standpoint too — the corner doing the same job it does in the address channel.*

**Both endpoints are degenerate, differently:** at c = 0 the facing is infinitely far and the kernel
is flat at zero; at c = 1 it sits **on** the breadth and §5.15j's collapse happens. *"A number from
0 to 1" is right on the **open** interval.*

## 5.16 Hangers: a freedom is infinitely dense, not infinitely long

> **(1 Oct)** Read "dense" as the spacing of addresses (R124). The equal hangers called parallel here are the uniform unit circle, the view from nowhere (R127).

**A freedom is finite in extent.** Presented in parallel and faced inward it is a quarter turn of π/2
(§4.3); faced forward, a line of length 1. Both ends are a finite distance away. **What is infinite
is how much it carries:** every address from 0 to ∞ is on it, on that finite arc. So the addresses
must crowd, and they crowd toward the horizon — per unit of turn there are 1 + s² of them: 1 at home,
2 at the corner, 101 at address 10, ten thousand at 100, without limit (`hangers.mjs`). **The horizon is
not far away. It is where the density has no limit.**

**Nothing is added to a freedom; things are hung on it.** Lay N magnitudes on a freedom and it is
divided into N **hangers**, one to each magnitude, each (π/2)/N of the turn. The freedom is unchanged —
hanging does not lengthen it and taking a hanger away does not shorten it. A hanger holds a magnitude;
it is not one.

### Parallel: equal and uniform

All N magnitudes present at once are laid in equal turns, **every hanger the same size, evenly
spaced.** In address they are not: hanger k covers tan(kπ/2N) to tan((k+1)π/2N). With N = 100:

| hanger | addresses | width in address |
|---|---|---|
| 0, home | 0 – 0.0157 | 0.0157 |
| 25 | 0.4142 – 0.4327 | 0.0185 |
| 49 | 0.9691 – 1.0000, ending at the corner | 0.0309 |
| 75 | 2.4142 – 2.5257 | 0.1115 |
| 98 | 31.82 – 63.66 | 31.84 |
| 99 | 63.66 – ∞ | ∞ |

### Serial: unequal, and arranged by the Cauchy

**A serial reader has no turn to lay anything in** — it receives addresses, one at a time. Measured in
address the hangers are neither the same size nor evenly spaced; there are (2N/π)/(1 + s²) of them per
unit of address, which is the Cauchy's own density. **What makes them hangers is that each holds an
equal share:** hanger k encloses exactly k/N of the Cauchy (to 2 × 10⁻¹⁶ at N = 100 and 10⁶). The
hangers are the Cauchy's quantiles — the edge of hanger 50 is the median at the corner, 1; the edges of
25 and 75 are the quartiles, 0.4142 and 2.4142, an inverse pair.

**Sort a million Cauchy arrivals into equal shares and the boundaries land on the hanger edges.** With
a sound generator, at ten million arrivals: 0.158415 against 0.158384 at the tenth, 1.000363 against 1
at the median, 6.323070 against 6.313752 at the ninetieth. **One set of hangers, two accounts:** in
turn, equal and uniform; in address, unequal and Cauchy-arranged; in both, one share each. This holds
only where the turn is met evenly (§5.15; *The Cauchy* §13).

> ⚠ **This paragraph used to begin "so a serial reader finds them by counting, with no angle," and
> that is now ruled wrong (Tom, Sep 20).** *We project serial and count parallel.* Sorting arrivals
> into equal shares is a **count** — it divides by a total, and it revisits arrivals a serial reader
> has already let go. **The quantile account of hangers is a parallel reading performed on a serial
> stream**, not something the stream itself supports.

**And the measurements say so plainly, because a count is provisional until the total is.** The same
edges recomputed as the stream lengthens:

| arrivals so far | 10th | median | 90th |
|---|---|---|---|
| 10³ | 0.148375 | 1.087290 | 7.179838 |
| 10⁴ | 0.160262 | 1.023802 | 6.329418 |
| 10⁵ | 0.160198 | 1.005754 | 6.395069 |
| 10⁶ | 0.158491 | 1.001213 | 6.340488 |
| 10⁷ | 0.158415 | 1.000363 | 6.323070 |
| **from the turn** | **0.158384** | **1.000000** | **6.313752** |

**Every edge moves with every extension, and none of them has arrived even at ten million.** Set
against that, the *projection* — one arrival read against the hold — is the same number after a
thousand arrivals and after ten million: **1.363081673437**, unrevised, because nothing later was in
it. **A projection is complete when its arrival is; a count is provisional until the total is.** That
is the operational content of the two verbs, and it is why the turn column above is not a better
estimate of the quantiles but a different kind of thing: it needs N and no arrivals, where the
quantiles need arrivals and are never finished.

### The home hanger, and why a hanger's size does not matter

**At home the two accounts meet.** The stretch from turn to address is exactly 1 there (§5.1), so the
home hanger's size in address is its size in turn, to second order — 0.0157080 against 0.0157093 at
N = 100, and equal to seven figures from N = 10⁶ on. Every other hanger is wider in address by sec² of
its turn: twice at the corner, 3,283 times at 89°. **Taken as the reference for the rest, the home
hanger reads 1** — the corner ½, the horizon 0 — **and the magnitude hung at home sets what that 1 means
in the world.**

> **And because a hanger is not a value, its size does not matter.** It carries no size into any
> comparison: every comparison is made against what is hung on it. So the reading has the same form at
> any N.

| N | each hanger | the last hanger begins at |
|---|---|---|
| 6 | 15° of the turn | 3.73 |
| 100 | 0.9° | 63.66 |
| 10⁶ | 9 × 10⁻⁵ ° | 6.37 × 10⁵ |
| 10¹⁴ | 9 × 10⁻¹³ ° | 6.37 × 10¹³ |

Six hangers take up a great deal of the circle — at N = 6 the addresses run 0–0.268, 0.268–0.577,
0.577–1, 1–1.732, 1.732–3.732, 3.732–∞ — and the home hanger still reads 1, the corner still falls on a
hanger's edge, each hanger still holds a sixth. A hundred trillion take up almost none, and each still
has room for a value. **N sets resolution, not meaning.**

### The horizon is where no further hanger can be hung

**For every N the last hanger runs from its lower edge to infinity** — 3.73 at N = 6, 63.66 at 100,
6.37 × 10¹³ at 10¹⁴, about 2N/π in general — and everything past that edge shares the one hanger. That
is §5.6's horizon stated as hangers: a reader of grain σ = π/(2N) has its last separable address at
cot σ ≈ 2N/π, the same number. **More hangers move the horizon out; no finite number reaches it.** It is
where the addresses are too dense for another hanger to be hung.

### What this restates

**§5.7's "infinite line" is the count, not the extent.** ln(b/a) is additive, invariant under composing,
and essentially unique, and it is the grain; what it measures between two addresses is **how many
addresses lie between them**, and that count is infinite toward either end. The freedom those addresses
are hung on is the quarter turn. The two measures of §5.7 do not disagree about the freedom; they
measure two different things on it — its extent, and its density.

## 5.17 In serial, one freedom is enough — and a second could not be reached

> **(1 Oct)** The proofs stand. The search below for what breaks the tie between v and h is answered by R146: h is the known side by definition.

§5.16 found a freedom infinitely dense. That raises the question of whether a serial reader ever needs
a second one — and, if it had one, how it would move between them. **It does not, and it could not.**

⚠ **The reader below is described as holding a value and dividing, and §5.18 rules that it receives
neither** — in serial what arrives is the *move*, and the values it is a move between are never sent.
That does not disturb this section's proof, which turns on one register and unsigned magnitudes and
not on where the ratio comes from; but the description is the parallel one, and §5.18 is the
correction.

**The reader.** One register. It holds a value h > 0; each arrival v ≥ 0 is read as a single address,
s = v / h; after reading, the arrival becomes the hold. **Two conditions are assumed and named:** one
register, and unsigned magnitudes — what is held and what arrives are fullnesses, which have no sign
(*The Relation Space* §18). Everything the reader has of an arrival is its address and its place in the
sequence.

### 1. One freedom always has room

For a fixed hold, v ↦ v / h sends every possible arrival to an address in [0, ∞), and sends distinct
arrivals to distinct addresses. **No arrival is ever left without an address, and no two are forced
onto one.** In hangers: any finite set of arrivals fits on one freedom given enough hangers, and whatever
lies past the last hanger's edge still lands on the horizon hanger (§5.16). A second freedom cannot be
needed for room, because the first is infinitely dense.

### 2. A second freedom adds nothing the reader can tell apart

To use two freedoms, the reader needs a rule for which one an arrival goes on, and the rule can use only
what the reader has: the address, and the addresses before it. **Whatever the rule, it sorts addresses
of [0, ∞) into two labelled groups — and any such sorting can be relabelled back into one [0, ∞) without
merging anything.** No operation on s creates a distinction s did not already carry. Two freedoms hold
exactly the distinctions one holds, laid out differently.

### 3. There is no way to move between freedoms

A move from one freedom to another has to cross a join, and a freedom's only joins are its two ends:

| the join | what reaching it would take | what a serial stream does there |
|---|---|---|
| the horizon, s = ∞ | v / h = ∞ | no finite arrival over a hold above zero gives it: never reached |
| home, s = 0 | v = 0 | that arrival becomes the hold, and the next reading divides by zero: the reader has stopped, not moved on |
| — displacing the hold | — | not a move: the freedom is laid out again from the new hold, whose hook is always the first |

**So no event in a serial stream carries the reader across a join.** Every arrival is read on the one
freedom of the hold it arrives against.

> **In serial, a one-register reader of unsigned magnitudes uses exactly one freedom.** One is enough
> (1); more add no distinction (2); a second could never be reached (3).

### The two ways a second freedom might be smuggled in, and why neither works

**Order.** An arrival's place in the sequence is a count, and a count is not a freedom — scaling changes
it, so it does not address (§5). Order is carried alongside the freedom, never as a second one.

**⚠ And one thing it does NOT buy, recorded because it was claimed here and withdrawn** (*The
Boundary* §9.1, B33). The claim was that order recovers **which magnitude is underneath** — compare
the address order against the arrival order, and on a monotone turn they agree one way round and
disagree the other. That is true of a *sweep* and it is not about the hold. Tom's correction: **no one
is actually walking a path.** A reader making one reading has two magnitudes and a chosen
denominator; it has no arrival order, because one arrival has no order, and no monotone turn, because
nothing turned.

> **There is nothing to recover.** Which term is underneath is not a hidden fact about the world but a
> **choice already made**, constitutive of the reading. V/H and H/V are both *correct* readings of the
> same pair — not one right and one wrong-way-round.

So order stands as this section already had it: carried alongside the freedom, never a second one,
and it does not secretly buy the hold back.

**Sign.** Signed terms give copies of a freedom — four of them, joined end to end (§5.13). But a serial
reader's terms are fullnesses; a sign is a place on a page, and only the parallel account has a page.

**⚠ And "fullness" is the kind, not a turn of phrase** (Tom, Sep 19; *The Boundary* §9.6). **h is the
same kind of thing as g: at 1 fully present, at 0 fully absent.** Under this paper's own v² + h² = 1,
h = 1 at home and h = 0 at the horizon, and **v, h and g all run 0 to 1 and all mean how much is
there.** The list is now complete, and two things follow.

**The reading is one fullness against another** — how present the read is against how present the
hold is — which gives the three marks of §1 a single account instead of two-by-absence and the corner
as an exception: the corner is **both equally present**, home is **the read absent and the hold
full**, the horizon is **the read full and the hold absent**.

**And the kept measure is h².** §2.4 already calls cos²θ "the quadratic kept measure"; cos is h, so
h = 1/√(1 + s²) gives h² = 1/(1 + s²) — the fisheye exactly, to 1.1 × 10⁻¹⁶. **The lens is the hold's
presence squared**, and its falloff toward the horizon is the hold going absent.

⚠ True **under the normalisation** and not without it: a reader meeting 418.2 and 418.2 has no 1 to
compare to. What the reader supplies is not a unit but **the circle**, and having supplied it, both
terms are readable from the address — h = 1/√(1 + s²) to 1.1 × 10⁻¹⁶.

**And v is the same thing, which licenses the swap** (B66–B68). v and h are exact mirrors — v absent
where h is full, and at the corner **neither**, both 0.707107, since two fullnesses on one circle
cannot both be 1. Their lenses are complementary: **h² + v² = 1** to 0.00e+0, and v² is exactly the
lens of the swapped address. **The two readings partition the measure with no residue**, so neither
is partial and neither is privileged.

> **So the Repertoire is three moves and one interchange, not four moves.** Rescale, shift and
> compose act on the address; the swap exchanges the *terms*, and two things can only be exchanged if
> they are the same kind. The swap is not a fourth axiom — it is what having two interchangeable
> fullnesses makes possible.

**And nothing distinguishes v from h but which is underneath.** Not size (at the corner neither is
larger), not boundedness, not readability, not side. **That is the whole of the difference**, and it
makes §4.2 nearly trivial: a reader has one freedom because it puts one of two interchangeable
fullnesses underneath, and there is nothing else to have.

**⚠ So it is not always v/h, and this paper says so in three places without defending it once**
(*The Boundary* §9.6, B69). A search for a tie-breaker found none: both orderings land on [0, ∞); the
lens is the hold squared *whichever* is the hold; the hanger set maps onto itself under the swap
(1.8 × 10⁻¹⁵); the figure cancels from both orderings by Lemma 1.2a, so an asymmetric figure cannot
prefer one. And "home is where v vanishes" is circular — it *defines* v as the one that vanishes at
home.

> **Choosing which term is the hold, choosing where the turn starts and choosing which end is home
> are one choice wearing three names.**

**And the relation is a fullness too, with a partner** (Tom, Sep 19; *The Boundary* §9.6, B70–B72).
*In a relation, full is the corner, and absence can be either h's absence or v's absence.* That shape
— 1 at the corner, 0 at both ends — is **R = 2vh**, and the "either" is its partner **D = v² − h²**:
R is how full the relation is, D says which way it is empty, and **R² + D² = 1** exactly, the same
constraint as the terms one level up. At home R = 0 and D = −1 (v is gone); at the horizon R = 0 and
D = +1 (h is gone); at the corner R = 1 and D = 0.

> **R = sin 2u and D = −cos 2u, so the relation's circle is the terms' circle at DOUBLE the turn.**

**⚠ And that recurses, which is §5.3's cascade** (B73–B74). If R is a fullness then R and D are a
fullness pair like v and h, and **a fullness pair makes a relation** — so the step repeats, doubling
the turn each time, and **level k sits at 2ᵏ·u** to 1.3 × 10⁻¹⁵. The doubling map of §5.3 and the
resolution pyramid of §8 are this recursion, and the leaves at odd multiples of π/2^(d+1) are exactly
the points the doubling has not yet folded to home.

> **The resolution pyramid is not a construction laid on the reader.** It is what happens when the
> reader does the only thing it can do — relate two fullnesses — and then does it again to what it
> got.

**⚠ And §2.2's binary path is a record of laps** (*The Boundary* §9.6, B75). That section says the
leaf positions are "forced by the rung structure's binary path" and never says what the path is. It
is this: a lap ambiguity of π at level k is an ambiguity of **π/2ᵏ** at level 0, so the levels carry
nested laps — π, π/2, π/4, π/8 — and **that family is the leaf lattice.** Each bit of the path is one
level's lap, and the bits are the leaf index in binary (0.9 → 010 → leaf 2; 1.4 → 011 → leaf 3).

> **Descending the tree is asking, at each rung, which half-turn you are on.** The leaf is the answer
> to all of them at once.

**⚠ And the fullness account changes nothing — it changes the picture** (Tom, Sep 19; *The Boundary*
§9.6, B76–B77). (R, D) and the address determine each other on the quarter, round trip to
5.3 × 10⁻¹⁵, so it is the same content in other coordinates. What it offers is a **change of
perspective: the corner becomes the top point, and the two empties fall away from it.**

**That is worth having because a peak is findable from inside and a midpoint is not.** This paper's
§1 marks describe the corner positionally — between the two ends, where the two stand equal — and a
midpoint needs both ends, one of which §5.6 says is never arrived at. A peak needs neither: climbing
by the reader's own **rescale** move, comparing R one rescale either way, reaches the corner from
starts of 0.02, 3 and 1000 in under 200 rescales, to 10⁻⁹.

> **The line is drawn from outside, with both ends on the page. The hill is what those ends feel like
> to something standing on it.**

**⚠ And the term underneath may be better called the scaffold** (Tom, Sep 19; *The Boundary* §9.6,
B87) — with two riders. It adds what "the hold" does not: the reader **puts it up** rather than
finding it (the climb is the reader adjusting its own), and **its magnitude is dismantled** — three
holds five orders apart, (3,4), (300,400) and (0.003,0.004), all read 0.750000, so Lemma 1.2a stops
being a cancellation in an algebra and becomes something that happens to a structure.

⚠ **The riders.** It names the **role**, not the letter: nothing distinguishes v from h but which is
underneath, so the scaffold is whichever one is. And **the scaffold is never struck** — remove it and
the reading diverges rather than standing. Only its *magnitude* comes down; its *presence* stays in
the reading and is recoverable from it.

> Which gives §5.6 a better sentence for the horizon than it has: **not a place too far away, but the
> scaffold gone.**

**And the climb needs nothing this paper says a reader lacks** (B82–B84). R written for raw
magnitudes is **2VH/(V² + H²)** — degree two over degree two, so the scale cancels — and as a
function of the address it is simply 2s/(1 + s²). So the climb needs the address, arithmetic, one
rescale and an order test: **no list, no N, no second reader.**

**That makes it the only placement of the corner a serial reader can run.** The median needs n
arrivals held and sorted; balance needs two states; the swap's fixed point needs both readings; equal
arms needs a ladder already laid. The climb needs one address at a time.

**And "fully represented" is exact** (*The Boundary* §9.6, B85–B86). Since v² and h² are measures and
partition, the pair is a two-way split, and the corner is that split's **maximum-entropy point** —
entropy ln 2, R = 1, both maximal at s = 1 and nowhere else, and they are different functions
(differing by up to 0.149), so the coincidence of argmax is a fact rather than a restatement.

⚠ Entropy needs a **logarithm**, which a reader has no more than it has an arctangent; R needs
2s/(1 + s²). **So "most evenly represented" is the outside's way of saying it and R is the inside's**
— same maximum, same meaning, computable from the address.

> **The corner is where neither term is drowned out**, which is a reason to measure from there — one
> this paper has always done without stating. At home only the hold is represented, at the horizon
> only the read, and at the corner both equally.

⚠ **And it is not a claim about precision.** A reading far from the corner is not degraded but
*exact*: at s = 0.001, R = 0.002 and |v/h − tan u| is 0.00e+0. R measures how much of the **pair** a
reading is about, not how good the reading is.

⚠ **But it is a calibration, not a measurement.** The climb moves the reader's *own hold* until
V/H = 1 — it has chosen a hold equal to what it is reading, which always succeeds whatever the world
is doing. **It tells the reader nothing about the world, only that it has finished adjusting
itself.** The median, by contrast, finds the corner of an arriving stream, which is a fact about the
world. Two jobs, not two methods for one.

**⚠ And auditing the whole geometry for fullness settings exposes a split this paper does not draw**
(*The Boundary* §9.6, B78–B80). Everything has one — v, h, g, R, the kept measure, an aperture's
share — or is built from ones that do (D = v² − h² is a *difference* of two). But they do not all
satisfy the same constraint:

| pair | constraint | kind |
|---|---|---|
| v and h | v² + h² = 1 | a **circle** |
| v² and h² | v² + h² = 1 | a **partition** |
| g and 1 − g | g + (1 − g) = 1 | a partition |

**The same equation is doing two jobs**, so the fullnesses come in two grades and squaring carries one
to the other: **amplitudes** (v, h, R — squares partition, on a circle) and **measures** (v², h², g,
an aperture's share — sum to 1 directly). g partitions *directly*, so **g is a measure and should be
compared to h², not to h.**

**⚠ Which says why §1's constraint is v² + h² = 1 and not v + h = 1** — a question this paper has
never asked. The linear partition has a corner and two absences too; what it lacks is a **turn**,
since its absences sit at v = 0 and v = 1, both finite, leaving nowhere for a rotation.

> **The square is what makes the terms a direction rather than a split**, and a direction is what can
> be rotated — which is the whole repertoire. The measures are where the split lives, so one equation
> gives both. That is what a unit vector is.

**⚠ And "four ways for a relation to be full" is an outside count** (*The Boundary* §9.6, B81).
R = sin 2u reaches its extreme at π/4, 3π/4, 5π/4 and 7π/4 — **the four corners of the turn**, one
per signed copy of §5.13, with R = +1 at two and −1 at the other two. But corners are four only
because there are quadrants, and quadrants need signs, and this paper's own §6 says a serial reader
has none: *"a sign is a place on a page, and only the parallel account has a page."*

**Stripped of sign, all four corners are the same fullness pair** — 0.7071, 0.7071 — so the reader
has **one**. On its own quarter R reaches 1 exactly once.

> **Four from outside, one from inside.** The signed four and the corner-four are the same four; the
> inside's four is the facings, which is four ways two relations can be *held*, not four ways one can
> be *full*.

⚠ And it adds nothing to the inventory: the summit *is* the corner, R(s) = R(1/s) so the peak does
not distinguish the two slopes (that remains the choice of hold), and evaluating R still needs the
normalisation.

**Which prices it.** A lap costs an unbroken watch, so locating yourself in a depth-d leaf costs
**d+1 unbroken watches**, one per level — and §8's measured result is the same fact: *"sub-leaf
position is absent from one observation… what one observation retains is the host leaf-window, not
the position inside it."* One observation buys no lap bits, so it gets the window and never the place
within it.

**The corner does not survive the step, and that is §5.3's fold.** Home is the fixed point; **the
corner goes to the horizon**, because where the two terms are equally present their relation is full,
and a full relation with no imbalance is all-read-and-no-hold. §5.3 states the fold; this says why the
corner is the thing it moves.

**⚠ And §2.4's radix is forced twice.** That section forces g = 2 by asking which dilation tiles the
conserved measure. This route never mentions tiling: **the radix is 2 because a relation has two
terms.** They agree, which is a check — not a proof that either implies the other, and whether they
are one argument is now an open question rather than an assumption.

⚠ **Which is what §2's factor of two is.** The inside arc of total π carries the **terms**; the
outside arc of total 2π carries the **relation**, and the doubling is the passage between them — not
a convention this paper adopts for compatibility, but the step from a pair to what the pair makes.

What is invariant is not "the address is v/h" but: **a reading is one fullness over the other, and
which is underneath is the reader's freedom.** Every result here survives that restatement, because
each is about the pair and not the labels — the label appears in the statements and never in the
content.

⚠ **Where it bites is the company program, not the mathematics.** Two readers each choosing their own
hold read the pair (0.6, 0.8) as 0.750000 and 1.333333 — reciprocals, both correct, neither able to
name its own choice. Their cross ratios agree exactly, so the disagreement never appears in anything
they exchange; it appears only when one says "the address is 0.75" and the other believes it.

**⚠ And there is a second four, which is the inside one** (Tom, Sep 19; *The Boundary* §9.4, B57).
**Each freedom is one relation between two things — v relative to h; another freedom is just another
relation of v relative to h; and there are four ways two relations can face each other.** Two
relations, each read one way or the other, is 2 × 2, and all four give distinct addresses.

**Counting to four twice is not an identification.** Four things can be arranged two ways, and these
are the two:

| | generated by | element orders | |
|---|---|---|---|
| the four **facings** | two facing flips | 1, **2, 2, 2** | **Klein** |
| the four **signed copies** | a quarter turn | 1, **4**, 2, **4** | **cyclic** |

A facing flip has order 2 — flipping twice puts the same term back underneath — while a quarter turn
has order 4, since applied twice it lands on the opposite quarter, not the start. These are the only
two groups of order four and this paper now has one of each.

**And the difference is exactly the sentence above.** The signed four needs a page; the facing four
does not. Run the four configurations with every magnitude positive, which is all a serial reader
ever has, and the four stay distinct — **the inside four is available to a reader that has never seen
a negative number.**

> **The signed four is the parallel account's; the facing four is the serial reader's own.** This
> paper had only the first.

### What it looks like, and the one place a stream reached its horizon

The serial lab (`one-freedom-serial-lab.html`) reads the 73 single-loop shapes of svg-inline.html's
library this way: the outline walked once, each point arriving as its distance from a counterpart, each
held value hung on one freedom of 32 hangers by its proportion to its successor. With the counterpart at
the centroid, the largest proportion on the circle, star, heart, cardioid, crescent and gear ran 1.00 to
1.11 and **nothing reached the horizon hanger.** On the rose — whose outline passes through the centroid,
so that one arrival is zero — the proportion ran to 4.1 × 10¹⁵ and **4 of 199 values landed on the horizon
hanger.** A counterpart moved to within 0.001 of a circle's outline gave only 2.03: with a hold that
follows the arrivals, neighbouring distances stay within a small factor of each other, and the stream
reaches its horizon only where an arrival vanishes. **The horizon is where the denominator runs out, and
nowhere else.**

### What this does not cover

- **Parallel accounts.** A held list may be laid on any number of freedoms; that is the reader's
  bookkeeping over data already present, with no stream to move through (§5.15).
- **More than one register.** A second reader, holding its own value, has its own freedom. Many freedoms
  come from many readers, never from one reader's stream.
- **Signed quantities.** A serial reader given signed values breaks the second condition, and the proof
  does not apply to it.

## 5.18 Serial and parallel are two signals, and 1d + 2d is what 3d is made of

> **(1 Oct)** Both readers are in situation 3 (R152); "N is unknown in one and known in the other" is now "v's breadth is unknown" for both. 1d, 2d and 3d as names for observation fall under R125.

§5.17 settled what a serial reader can reach with one freedom. Tom's Sep 20 rulings settle what a
serial reader is *given*, and the answer changes the account of both sides.

> **1d is the serial signal, 2d is the parallel signal, 3d is both combined, but still separated
> signals. Motion of 1d and the magnitude lists of 2d are separated and consumed with a 3d
> standpoint.**

**So the ladder is about what arrives, not about how many numbers a point carries.**

### The values never arrive — the motion does

§5.17's reader holds h, receives v, and divides. ⚠ **It receives neither.** In serial the array
arrives one value at a time and **what each arrival carries is the move from the last one**, so the
residue is not computed from the signal; **it is the signal**.

That costs less than it sounds and more than it sounds, in two different places.

**Less, for the figure.** Rebuilt from moves alone, anchored at 1, a hanging comes back to
**2.776 × 10⁻¹⁶** relative — every proportion exact. What is missing is **one number**: multiply
everything hung by 1, 7 or 10⁻⁶ and the received stream is *bit-identical*. The scale is not degraded,
it is absent, which is §5.5's scale invariance arriving as a property of the channel rather than of
the arithmetic.

**More, for g.** In parallel a withheld value leaves an **empty hanger** — a place with nothing on it,
which is how it can be counted. In serial there is no hanger to leave empty, so **g does not punch
holes in the signal, it multiplies it**: the move simply spans further and what arrives is the product
of the moves not sent. Two moves of 0.400000 and 3.666667 arrive, thinned, as the single move
**1.466667**, and a skipped slot holding 0.01 versus 500 gives the same stream to the last bit.

> **What g costs a serial signal is the factorisation, not the values** — and nothing in a product
> says how many factors it has.

### Neither signal contains the other, and they fail differently

| | the signal | carries | does not carry |
|---|---|---|---|
| **1d** | the **serial** signal — **motion** | the order, and the figure up to scale | N, the places, the anchor |
| **2d** | the **parallel** signal — **magnitude lists** | N, g as a real count, the magnitudes, the anchor | an order |

A magnitude list walked three ways disagrees from the first move, and one list yields **(N−1)! =
5,040 motion streams** at N = 8: *"the one before it" is not a fact about a set of places seen at
once.* Conversely motion plus **one anchor** rebuilds the list at **0.000e+0**, exactly, at any N.

> **The parallel signal is missing a sequence. The serial signal is missing a size.**

**⚠ And neither one ever turns into the other** (Tom, Sep 21; §9.7p, B183–B188). *"When does a serial
signal become a parallel signal? Never. You have just gained access to its magnitude list."* The gap
is exactly **an anchor and an N** — put those beside the move stream and the list comes back at
0.000e+0 — and **the anchor is not hard to hear, it is inaudible**: every quantity a serial reader can
form has had the scale divided out before it was formed, so no memory recovers it. A reader with
**unbounded** memory holds bit-identical values on a world and on that world scaled.

**Which sorts the sentence above into its two cases.** A magnitude **list** is ordered, so it strictly
contains the move stream — being handed it costs nothing and gains the anchor, N and the order. A heap
of **places seen at once** is what this paragraph means by the parallel signal, and being handed *that*
is a trade: the sizes arrive and the sequence goes, 362,880 streams at N = 10.

> **A reader does not become parallel. It is handed a list, or it is not.**

**⚠ AND A SCOPE STATEMENT THIS PAPER OWES, which it has never made** (Tom, Sep 21; §9.7q,
B189–B192). *"The serial signal comes from a magnitude list. The serial signal measures the motion of
the magnitude list **in some way**. For example, a heart beat is a serial signal that comes from a
heart, which is a magnitude list."*

**Everywhere this paper writes "the serial signal" it means one particular measurement — the
consecutive ratio.** That is a choice meeting two separate requirements which the paper has never
distinguished:

- **it measures motion** — two resting lists at different levels give it the same output, where the
  raw value reads 5.0 against 9.0 and so is measuring where the list *is*;
- **it is scale-free** — and this is a *second* condition, not a consequence. The consecutive
  **difference** measures motion, is **not** scale-free, and gives the list back **exactly**.

**So retention and scale-freedom do not travel together, and a beat is not a degraded ratio.** A beat
is scale-free, reports 4 numbers about a list of 24, and what it keeps is the **period** — which is
closure, which is the one thing §5.18a says is serially free. *A pulse is a closure detector.*

> **Read every result of §5.16–§5.19 as a result about the consecutive ratio.** The address, the
> residue, the lap product, z and the band are all that one measurement. **Closure is the only one
> that crosses to the others.**

**⚠ AND A SECOND SCOPE, WHICH SORTS THE LIMITS THIS PAPER PRICES** (Tom, Sep 21; §9.7r,
B193–B197). *"The heart beats, it generates a signal. It can be observed beating. So both its motion
and shape are known."* A source that can be **watched** as well as heard has two channels, and they
are coarse in different places: the watcher is exact in value and coarse in time, the listener exact
in time and coarse in value. Neither dominates.

**Which reclassifies, without withdrawing, most of what §5.16–§5.19 establishes:**

| the limit | what removes it |
|---|---|
| the anchor is inaudible; N waits for closure; the band is undetectable | **a second channel.** Watching hands over the value, the count and every coincidence at once |
| a single pass cannot see inside its own grain | **time.** The peak is short by 1.899786 on one pass and by 0.000000 over sixty, because a step coprime with the period walks through every offset |
| v and h are magnitudes, so three quarters never arrive | **nothing** |

> **Three kinds of limit, and this paper has been writing them as one: what one channel cannot tell
> you, what one pass cannot tell you, and what a magnitude cannot tell you.** *The serial-only
> results are exact, and they are a worst case.*

**⚠ AND A FOURTH, WHICH COMES BEFORE ALL THREE** (Tom, Sep 21; §9.7s, B198–B201). *"A human has a
heart that beats and eyes that blink and runs creating motion, all are signal and have nothing to do
with his magnitude list."*

**A body is not a magnitude list. It has one, and several others, and the signals it emits belong to
those others.** Three signals from one body move each with its own list and with no other; the body's
own list can be scaled by a thousand, reversed, replaced or **deleted** with every signal unchanged at
**0.00e+0**. That is not a weak dependence — it is no channel at all, and no number of arrivals and no
second channel closes it. *You are not short of the body. You are not pointed at it.*

> **So "two channels on one source" holds only when both are pointed at the SAME list** — the
> paragraph above describes watching the heart and hearing the heart. Watch the person and hear his
> heart and there is no join to make.

**⚠ AND N HAS A FOURTH POSITION THIS PAPER HAS NEVER NAMED** (Tom, Sep 21; §9.7u, B206–B209).
*"A heart rate is well known, we know exactly how it works. So N is kind of known, but not
precisely."* The paper has N **known** (parallel), N **unknown** (serial) and N **from closure**
(§5.18a). **A reader holding N to within a fraction is a fourth, and it splits the machinery:**

| | |
|---|---|
| N used as a **size** — the grain, the aperture, the corner's place | **degrades in proportion.** 5% error in N, about 5% in the quantity |
| N used as an **index** — the facing, k → N−1−k | **inverts on an off-by-one.** All 64 places mis-paired, closure 0.000000 → 2.832519 |

> **Approximately right is fine for a size and meaningless for an index.** Half of §5.16–§5.19 works
> on an approximate N; the other half is not approximately wrong on one, it is wrong.

**And the prior buys search, not accuracy** — 399 candidates down to 3, with every window containing
the truth returning the same N. ⚠ A window centred wrongly returns its best candidate with no mark
that the truth was outside.

**⚠ WHICH GIVES THE FOURTH POSITION AN ADDRESS SPACE OF ITS OWN** (§9.7v, B210–B213). *"The quarter
turn is [0, N], the freedom is [0, ∞), the heartbeat is [0, ~N)."* A top that is there but not
sharp — and its own property is **anticipation**:

| | top | corner at | can the reader say *when*, in advance? |
|---|---|---|---|
| **[0, N]** | exact | place N/2 | yes, exactly |
| **[0, ∞)** | none | address 1 | **no** — §7.2's corner is findable, not predictable |
| **[0, ~N)** | ~N | place ~N/2 | **yes, approximately** |

**And on a list traversed once through its corner the exchange is excellent.** The corner is crossed
at arrival N/2, so N = 2m **exactly** — *half the cost of closure*, and it overrules a wrong prior: a
reader believing N = 88 is corrected to 64 by looking.

> ⚠ **But only where the corner is unique.** A wandering signal crosses 1 repeatedly — 25 times in
> 64 arrivals — every crossing a genuine v = h, and N = 2m then returns 25 answers between 4 and 122.
> **Move the prior's centre and the answer follows it.** The prior is not corrected; it is confirmed.

**So [0, ~N) earns its keep on the arch's kind of list — traversed once, monotonically, through its
corner.** *A pulse is [0, ~N) in extent and [0, ∞) in structure.*

**⚠ AND THE SCOPE STATEMENT THIS PAPER MOST OWES ITS READER** (Tom, Sep 21; §9.7w, B214–B217).
*"If N is truly unknown — a signal arriving over a very long time, or with poor fidelity — that is a
true freedom. Most signals, we know a great deal about their history."*

**§5.16–§5.19 is about a reader with no history at all, and that reader is rare.** History is
stronger than the count prior above: **a past lap that closed gives N exactly**, before the current
lap begins, where a prior gives only a window. And **a varying N costs nothing** — laps of 11, 13, 9,
14, 12 give q25 0.4142, q50 1.0000, q75 2.4142, the half-Cauchy exactly, because §5.18a's re-graining
is free at closure and every lap closes. *A rate that wanders is the ordinary case, not an exotic
one.*

**⚠ But only one of the two routes to a true freedom is one.** A long arrival **withholds** N — at 47
of 48 the reader knows exactly as little as at 6, and there is no partial credit until the lap shuts.
**Poor fidelity delivers an N that is wrong**: 7 instead of 48 at a fidelity of 3e−2, a cliff rather
than a slope, with the corner at 3.5 instead of 24 and the grain out by a factor of seven.

> **An absence and a corruption are opposite conditions, and only the absence is a freedom.**

**And the corruption is catchable.** Its facing spreads by 2.058883 where a true closure reads
0.000000 — vast beside the fidelity that caused it. *The closure test and the facing test disagree,
and an error that passes its own checks is only dangerous while there is one check.*

**⚠ AND WHEN MAY A FREEDOM BE WORKED AS A QUARTER TURN?** (Tom, Sep 21; §9.7x, B218–B221.) *"If N is
known approximately, or has low variability, you can treat the freedom as symmetric and like a
quarter turn."* §5.11's separation stands, and the treatment is legitimate — but **the condition
attaches to the wrong half:**

| treating a freedom as a quarter turn… | safe? | needs |
|---|---|---|
| …as **symmetric**, and as **bounded** | **always** | **nothing.** u ↦ π/2 − u is an isometry and neither it nor arctan mentions N |
| …with **places**, a **grain**, an **aperture** | mostly | ~N, degrading in proportion |
| …with a **facing** | ⚠ **no** | N exactly |
| …**composing**, by adding turns | ⚠ **no** | wrong at any N |

> **The symmetry is free.** A reader holding addresses can move to the turn coordinate and have it
> immediately, at any N or none. What ~N buys is the **places**.

**⚠ And the treatment carries a cost no N ever pays.** Composing multiplies addresses; adding turns
is not that, and there is **no region where it nearly is** — the two laws' identity elements sit at
opposite ends of the arc, composition doing nothing at the **corner** and addition doing nothing at
the **horizon**. Operations whose neutral elements differ cannot agree anywhere.

> **Treat a freedom as a quarter turn to look at, and never to compose in.**

**And of the two conditions, low variability is the stronger** — measured from the signal's own past
closures, so it can be *spread* but not *mis-centred*, where a prior can be confidently wrong.
Neither rescues the facing.

### ⚠ 5.19b What knowledge of N is an axis OF

An external review proposed organising the whole signal taxonomy by what the observer knows of N.
Tested (§9.7z, B226–B229), **the axis is real and it is one of three**:

| axis | positions | where it was measured |
|---|---|---|
| **what is known of N** | exact · from closure · approximate · unknown | §5.18a, §5.19a |
| **which measurement of motion** | consecutive ratio · difference · crossing · … | §5.18, the scope note above |
| **how many standpoints** | one · two · more | §5.11's note, and the arc's forcing |

The knobs are independent — hold N fixed and change the rule and the signal changes; hold the rule
fixed and change what is known of N and the output is identical — *so a classification that names
only the first reads as a list of cells.*

**⚠ And the N axis is a dial for sizes and a switch for indices**, which is the §5.19a split stated
as a taxonomy rather than as a caution. *"Operations become unavailable as uncertainty increases" is
true of the size half; the index half was never available at anything but exact.*

**What "N unknown" actually is.** The review's closing proposal — *that it is not a deficiency but a
different mathematics* — is **false as a capability claim**: every quantity the N-unknown reader can
form, the N-known reader can form too, by construction. It is **true as an invariance claim**:

> A reader that computed at n = 8 and then receives two more arrivals finds **every move and every
> z-difference still correct, bit for bit**, and its grain, its facing, its corner and its claim that
> the lap closed all **replaced**. *A reader that never committed to N has nothing to withdraw.*

**So: not more mathematics — mathematics that is invariant to N being revised.** ⚠ And the invariance
belongs to the *quantities*, not to summaries built on them: a median move survives two extensions at
1.5455 and moves to 1.0111 on a third.

**⚠ And §5.18's join cannot tell the difference, in a strip.** Fed one list's places and another's
motion it **refuses** outright at a fine grain — an unclaimed cross-source guarantee — and goes
degenerate at a coarse one, which is the band doing its job. **Between them is a narrow strip where it
returns exactly one confident join and that join is false**, carrying no mark to distinguish it from
the true one. *A perfect reading of the wrong list is still nothing, and the reader is not told.*

Which is why §5.16's hanger table has two accounts that do not reduce to one another, and why the
quantile account there had to be reclassified: **that account was the parallel signal reading a
serial stream.**

### The join, and whether 3d is simply 1d + 2d

The motion is indexed by **arrival**, the list by **place**, and *no arrival announces where it came
from*. So a standpoint holding both must **match** them, and the match is an act it performs. Matched,
it holds **a path through the places** — an object neither signal had.

**And the match is generically forced, which is the case for Tom's simpler reading.** An exhaustive
search over every cyclic order returns exactly one, in **1,200 of 1,200 random hangings** at N = 6, 8
and 10, and it is scale-free: the list scaled by 10³⁰ or 10⁻³⁰ gives the same single order. *If the
join is derivable from the two signals, 3d adds no third ingredient and really is 1d + 2d.*

**⚠ Except in a band, and the band's width is the reader's grain.** Degeneracy needs exact
coincidences — measure zero, which sounds like a curiosity. It is not one, because a reader compares
with a grain. Perturbing the circle by ε:

| ε | orders that match, grain 10⁻⁶ | orders that match, grain 10⁻¹² |
|---|---|---|
| 0 | **40,320** = 8! | — |
| 10⁻⁹ | **40,320** | **1** |
| 10⁻⁷ | **40,320** | **1** |
| 10⁻⁶ | 453 | **1** |
| 10⁻⁵ and up | **1** | **1** |

**Refining the grain narrows the band and never closes it.** And degeneracy does not arrive
gradually: coincident pairs added one at a time give **1, 2, 4, 8, 16** — exactly **2^r**, since the
two places in each coincidence swap independently.

> ⚠ **And the band is centred on the circle** — this paper's own centring, the figure with no
> residue, the one everything else is read against (§4.2, §5.13). **The place where 3d stops being
> the sum of its two signals is not an exotic corner of the space. It is the middle of it**, and a
> reader working near its own centring is working where its two signals have least to say to each
> other.

**And consistency does not rescue it.** The lap product is **1.000000000000000 for every hanging, in
every order, at every g** — a quantity taking one value on everything identifies nothing, so it is a
**checksum**, not a measurement. Corrupt one move by 1.1 and it reports exactly 1.100000000 while
saying nothing about which move. *A standpoint can have both signals verify, the lap close, and still
hold a correspondence it invented* — on the circle it would take one of 40,320 with equal warrant.

**The extract is `three-dimensions.md`** — fourteen statements with their receipts and seven open
questions, kept strictly apart. Receipts: `serial.mjs`, `dimensions.mjs`, `standpoint.mjs`.

## 5.18a 2d is closure, and closure is a symmetry about the corner

> **(1 Oct)** The symmetry about the corner holds where both breadths are known (situations 1 and 2). Situation 3 is not symmetric about the corner: proportional on the front side, doublings past it (R150), and the parallel reader keeps v on the front side only (R152).

> **2d is closure. When a magnitude list closes, it represents all possible ways V and H can be
> represented relative to one another in all possible facings. 3d is the depth of that
> representation.** — Tom, Sep 20

The testable core is *all possible facings*. A facing is which of the two terms is held, and swapping
it sends the address s to **1/s**. So the ruling says a closed list's address set is **closed under
reciprocal** — a property a set either has or has not (`closure.mjs`).

**It has it.** On a full list at N = 12, every address's reciprocal is in the set to **3.220 × 10⁻¹⁵**,
and the pairing is hanger k with hanger **N − 1 − k**, reflected about the corner:

| | | |
|---|---|---|
| k = 0: 0.065543 | × k = 11: 15.257052 | = 1.000000000000 |
| k = 3: 0.493145 | × k = 8: 2.027799 | = 1.000000000000 |
| k = 5: 0.876976 | × k = 6: 1.140281 | = 1.000000000000 |

> ⚠ **Two repairs to this sentence, both from Sep 21** (§9.7aa, B230–B233). **First, "every relation"
> means every relation THE LIST HOLDS, not every relation that could exist** — the corner pair closes
> exactly on two relations and leaves uncountably many unvisited. **closure = the inventory held ×
> all facings.** **Second, this paper uses "closure" for two independent conditions in two channels:**
> this one, the inventory pairing off under the swap (address), and §5.18a's serially-detectable
> event, the magnitudes coming home (residue). All four combinations of the two exist. *The event a
> serial reader detects with no total and no unit is the second, and it says nothing about the first.*
>
> **And that gives the open/closed distinction its real content.** N unknown is not a missing number —
> it is **an inventory with no known boundary**. A reader can always establish *everything encountered
> is accounted for* and never *everything that could exist is*: an inventory closes, opens and closes
> again as arrivals continue, and every reading was correct when it was made. **A shape is a completed
> relational inventory.**
>
> **And the levels below it separate** (§9.7ab, B234–B237). The **relation space** is every v/h that
> could be — [0, ∞), uncountable. The **inventory** is what is held: six addresses carry thirty
> ordered ratios. An **arrangement** is one order of it, 1 of 720, and the permutations give 720
> streams read straight or 120 read as laps (B131's (N−1)!, which identifies them *up to rotation* —
> simply wrapping still gives 720). **Closure survives all 720 arrangements at 1.11e−15 where
> k → N−1−k accepts 48**, so *closure is closure of the relation space and not of the data
> arrangement.*
>
> ⚠ **And a permutation does not create a relation — it EXHIBITS one.** x₄/x₂ existed before anything
> was placed beside anything, but **one arrangement exhibits 5 of the 30 ratios among six magnitudes
> and the arrangements between them exhibit all 30.** *Say it that way round; it is the version with
> a number in it.*
>
> ⚠ **Which also says what "unit" names, and it is not the radius.** *Unit circle* bundles three
> independent properties: the **radius** (entirely incidental — the address has none in it, B146, so
> a radius-7 circle is as unit as a radius-1 one), **circle-ness** (residues all equal — a *residue*
> channel fact, *The Centring*'s figure with no residue), and **completeness** (the inventory pairs
> off — an *address* channel fact, set by which turns were sampled). *"The complete relation space"
> names only the third.*

> **So a closed list holds every relation in both facings**, and holding v against h is the same as
> holding h against v. That is what closure buys, and it is a property of the **set**, not of any
> reading taken from it.

### ⚠ And spanning is not enough, which is not what I expected

| hanger set | symmetric under k → N−1−k | worst reciprocal miss |
|---|---|---|
| all 12, g = 1 | yes | **3.220e−15** |
| every other, still spanning | no | **0.6705** |
| every third, still spanning | no | 0.8069 |
| the first half | no | 0.9425 |
| symmetric thinning, 6 | yes | **3.220e−15** |
| symmetric, just 4 | yes | **3.220e−15** |
| symmetric, the corner pair | yes | **0.000e+0** |

The "every other" row reaches every part of the address space, end to end, and **misses by 0.67**.
*Coverage is not closure.* The reciprocal of hanger 0 is hanger 11, and keeping the even hangers
throws away every odd partner they need.

> **The condition is a symmetry, not a count: the set must be invariant under k → N−1−k, which is
> reflection about the corner.** Necessary and sufficient on every row.

Two consequences worth separating:

- **g = 1 is sufficient for closure and not necessary.** A symmetric thinning of six, or of four, is
  as facing-complete as the full twelve. What g = 1 buys is **closure for free, without having to
  arrange anything** — a reason for its standing that §1's census did not have.
- **The smallest closed list is the pair straddling the corner**, and it closes exactly:
  0.876976 × 1.140281 = 1.000000000000. **Two hangers are a complete 2d.**

### and the facing leaves z alone

Give each hanger a magnitude and z = its log. The swap k → N−1−k reflects the addresses about the
corner and **the z values as a set come back identical** — no depth changed, created or lost.

> **The facing is an x,y operation and nothing else** — which is §5.19's angular row arriving as a
> symmetry rather than as a motion.

### closure in 2d and closure in z are one condition in two channels

A list that closes returns to its own first value, so its moves **multiply to 1.000000000000000** and
its z-steps **sum to −1.1 × 10⁻¹⁶**. *"2d is closure" and "3d is the depth of that representation" do
not name two requirements: the second is what the first looks like along the third axis.*

### ⚠ Closure is intrinsic, and this section had only shown it on even layouts

An external review pressed on exactly the caveat printed above — *checked on lists laid evenly on the
turn* — and asked whether k → N−1−k is **the symmetry of the relations or of an evenly sampled
representation**. Tested (§9.7y, B222–B225):

| layout | even? | symmetric about the corner? | does it close? |
|---|---|---|---|
| even, symmetric | yes | yes | **4.46e−14** |
| **crowded**, symmetric | **no** | yes | **4.46e−14** |
| **random**, symmetric | **no** | yes | **6.66e−16** |
| **even, off-centre** | **yes** | **no** | ⚠ **3.78e+0** |

> **Evenness was never doing the work.** A crowded layout and a random one close to machine
> precision; a perfectly even one sitting off the corner does not close at all. **Symmetry about the
> corner is the condition**, exactly as this section claims — and now on layouts that are nothing
> like even.

**And the two readings must be stated in the right order.** *Intrinsic closure* — every address pairs
off against a **distinct** partner, one-to-one, self-partnering only at the corner — is blind to order
and to spacing. **k → N−1−k is how a sorted list displays it**: shuffle the same twelve relations and
the index reading misses by **1.29e+1** while the intrinsic one does not move.

> ⚠ **State the intrinsic form and derive the index form for sorted lists.** The checks behind this
> section measured the index form, which additionally needs sortedness — a fact about the list as
> written down, not about the relations it holds.

**⚠ Still not shown:** whether a sampling can be symmetric about the corner *without being chosen to
be*. Every symmetric layout tested was built symmetric. **That is the even-turn hypothesis wearing
another hat**, and it is untouched.

⚠ **Scope.** This is checked on lists laid **evenly** on the turn, where k → N−1−k *is* the
reflection. On a crowded layout the reflection is a different permutation and the condition is
untested — `arch.js` already found the corner results to be consequences of the even layout, and this
may be another.

## 5.19 Depth is z, and 3d is the motion of 2d

> **(1 Oct)** R79 (27 Sep) makes depth the forward sweep, the parallel reader's, not the serial signal. The rungs as doublings anticipate R149's back side; §5.19a's corner at arrival N/2 anticipates the front side's plain proportion.

> **Notice that the 1d signal is where depth comes from, it is the z. The 2d signal would then be
> the x and y.** — Tom, Sep 20

This rules the slot §5.18 left open, and it is not a free ruling: **coordinates have to be
independent.** If z were a function of x and y then 1d and 2d would not be two signals and §5.18's
whole account would collapse. So it is worth checking rather than adopting (`depth.mjs`).

### z is the log radius

The serial signal is motion, so the obvious z is motion accumulated as it arrives. Three traversals
of the same hanging give three completely different profiles — and **the same range, 2.0149, all
three times.** That is not a coincidence: accumulating log-moves telescopes, so z at arrival i is
log(value there) − log(value started from). The traversal sets the offset and the ordering; it cannot
touch the range, because the range is the hanging's own spread in log — **log(max) − log(min) =
2.0149**, the same number.

> **z is the log of the magnitude.** Depth is not a property of the path through the figure; the
> path only decides where the reader's own zero sits.

### which forces x and y to carry no radius at all — and they do not

Three different figures met at the same 64 turns, each read at **its own boundary point**:

| turn | circle | star | cloud |
|---|---|---|---|
| 0.0245 | 40.735483872 | 40.735483872 | 40.735483872 |
| 0.8099 | 0.952079147 | 0.952079147 | 0.952079147 |
| 1.5953 | −0.024548622 | −0.024548622 | −0.024548622 |

Largest disagreement across all 64 turns and all three figures: **7.105 × 10⁻¹⁵**. The radius cancels
in v/h, so **x and y carry the direction and nothing else** — the two-channel result stated as
coordinates.

### and that is the independence test, which the ruling passes

Identical x and y; and z of range **0.000000** (circle), **0.969061** (star), **0.995038** (cloud).

> ⚠ **z is not a function of x and y, so 1d and 2d are genuinely two signals.** Had the depth been
> recoverable from the direction, the separation §5.18 rests on would have been an illusion. It is
> not.

**And it names the shape of 3d: direction round the x,y plane, log radius up the z axis — a
cylinder.** Which is the log-polar coordinate this series has used since *The Radix*, arriving as
geometry rather than as a change of variable.

### what the lap meant all along

§5.18 called the lap product a **checksum** and refused to treat it as content, since a quantity
taking one value on everything identifies nothing. That refusal stands. But read in z the product
becomes a sum, and the sum of z-steps round a lap is **0.000e+0, 8.3 × 10⁻¹⁷, −4.2 × 10⁻¹⁷** for the
three figures:

> **A closed lap returns to the depth it started at.** The lap identifies no figure, and it is not
> nothing either: it is the closure condition in z.

### and the grain was a depth measure all along

§5.7 found a freedom's own measure — ln(b/a), additive, invariant under composing, essentially
unique — and identified it with the grain. **z is that measure accumulated.** ln(7.5/3) + ln(3/2) =
ln(7.5/2) = 1.321755840, unchanged at ×1000.

> **"How many addresses lie between these two" and "how far apart in z" are one quantity under two
> descriptions** — which is why the grain is additive. Depth adds. **A rung is a step in z.**

### 3d is just the motion of 2d

> **3d is just the motion of 2d.** — Tom, Sep 20

Which sharpens the above rather than contradicting it. §5.19's independence test was taken **at one
instant**, and that is what motion means: *a velocity is not recoverable from one position.* What it
left open is whether a **sequence** of 2d frames determines z, and it does — exactly.

| frame | z accumulated from the moves | log(rₜ / r₀) |
|---|---|---|
| 1 | 0.314810740 | 0.314810740 |
| 2 | 0.629621480 | 0.629621480 |
| 4 | 1.259242959 | 1.259242959 |

> **So 3d is not a third signal sitting beside 2d. It is what 2d does.** One frame gives no z; two
> give a z step; the sequence gives z outright. And **the serial reader is the one that has the moves
> without ever having held a frame** (§5.18).

**And it resolves a tension this account had been carrying.** §5.18 calls the 2d signal *magnitude
lists*, which carry radii; §5.19 finds x and y carry the direction and **no radius at all**. Both
hold, at different levels: **the frame carries magnitudes; the address channel inside it does not** —
and z is the motion of the magnitudes, which is why it takes two frames to see.

**⚠ And motion decomposes without remainder, along those two channels exactly.**

| the motion | change in the address list | change in z |
|---|---|---|
| **radial**, ×1.1 to ×10, **non-uniform** | **1.78 × 10⁻¹⁵** | spread 0.5996 |
| **angular**, +0.001 to +0.1 | 0.105 to **558** | **exactly 0** |

*The radial motion above multiplies each place by a different amount and the address list still does
not move*, because the address is cot(u) and has no radius in it. **Radial motion is z and nothing
else; angular motion is x,y and nothing else.** Neither channel is a partial view of the other:
they are the two halves of what moving is.

### 3d is consumed as 2d images of 1d slices

> **3d is consumed as 2d images of 1d slices.** — Tom, Sep 20

So a standpoint never receives 3d whole: it takes **slices**, each slice is 1d — a serial stream —
and each is rendered as a 2d **image**. Since §5.18a makes 2d closure, this puts closure forward as
the **event** that turns a slice into an image, which can be watched rather than asserted
(`slices.mjs`).

**⚠ And the two conditions do not arrive together, which is the result.** Filling twelve places one
arrival at a time:

| | |
|---|---|
| the **image** completes at arrival 12 | the last place is filled and the set becomes facing-complete — what the reader **has** |
| the **lap** closes one move later | on the return to where it began — what the reader can **confirm** |

*A slice becomes an image when its places are all there; it becomes a closed image only once the
reader comes back round.* **The confirmation costs one arrival more than the thing it confirms** —
the series' own *one lap of counting* in another setting. And **z = 0 alone is not sufficient**:
arrival 1 has z = 0 and is not an image at all, because nothing has moved yet. *The lap condition
detects a return, not a completion.*

**And the image does not fade in.** The reciprocal miss over the fill runs 0.996, 0.987, … 0.807,
0.670 — visibly improving and meaningless the whole way, since none of those sets holds its own
reciprocals — and then **3 × 10⁻¹⁵** at the last arrival. *Closure is a symmetry, and a symmetry is
not something a set can have a little of.*

### the stack

Four slices of one 3d thing, each a full lap:

| slice | the 2d image | z of the image |
|---|---|---|
| 0 | identical at every slice | −0.131344 |
| 1 | identical | 0.218656 |
| 2 | identical | 0.568656 |
| 3 | identical | 0.918656 |

Spacing **0.350000** between consecutive slices — exactly the rate the object was built with. **Every
slice gives the same 2d image and a different depth**, because the address set is the direction
channel and the slices differ only in radius.

> **So "consumed as 2d images of 1d slices" is the cylinder read off one ring at a time.** Each
> slice arrives serially, closes into an image, and takes its place at a depth. The standpoint never
> holds the solid — it holds a stack, and **the stack is the depth**.

⚠ **And it puts the join problem one level up.** Within a slice the reader matches motion to places
(§5.18). **Across slices it has no such handle**: the images are indistinguishable in x and y, so
their order in the stack is carried by z alone. *Lose the depths and the stack is a set of identical
pictures with no way back to the solid.*

⚠ **Scope.** The slices here are full laps at a fixed depth — flat rings. Whether a slice can cut the
cylinder any other way, and what a reader would have if it did, is not measured.

⚠ **And this opens a question in the place of the one it closes.** §5.11 says an address of addresses
is free — *depth adds levels, not kinds*. That depth is **indirection** depth, a count of
compositions; this one is a **coordinate** measured in grains. They are not obviously the same thing
and nothing here shows that they are. **§8 item 0 is rewritten accordingly.**

## 6. Where composition stops

Composition needs both addresses to exist. A freedom at 0 or ∞ is at its horizon, and there:

| | |
|---|---|
| one freedom at 0, the other ordinary | c = 0 |
| one at ∞, the other ordinary | c = ∞ |
| **one at 0 and the other at ∞** | **undefined — no address at all** |

> **The composites are defined everywhere except at the horizons.** The structure lives on the
> interior, and the ends are where composing stops.

Which is the same fact as a reader losing its chart, arriving here as an algebraic gap rather
than as an instrument failure — the two descriptions of a horizon meeting.

---

## 7. What other frameworks hold, and what this paper takes from them

Ratios are old and heavily studied. This section says where the structures of §3–§5 already
exist, what is taken from each, and what is left as this paper's own.

### 7.1 Ratios as fundamental, elsewhere

Several traditions already treat ratios as more than elementary. Buckingham's π theorem rewrites
any physical law as a relation among ratios of like quantities (Buckingham 1914). Measurement
theory makes the ratio scale a formal type, meaningful under rescaling and nothing else (Stevens
1946; Krantz et al. 1971) — the property §1 uses to define a freedom. Projective geometry takes
the cross-ratio as its invariant, and relational physics argues that absolute scale is not
physical.

**Each reaches ratios by stipulation or by symmetry. This paper reaches them from a lack.** A
reader holding the whole pair needs no ratio. Take away the other party's size, and a ratio
against what is held is the only reading left; the corner, the fisheye, the grain, the levels
and the audits of §5.12b follow from that one poverty (§0).

> **The object of this paper is the bounded reader, and the ratio is its first consequence.**

### 7.2 Compositional data analysis: grouping, already built

Compositional data analysis is statistics on quantities of which only ratios are informative
(Aitchison 1986). A freedom is a compositional part there, and several structures of §5 are
established:

- **n parts carry n − 1 log-ratio coordinates** — the count of §4.
- **Grouping freedoms under holds (§5.10) is the sequential binary partition.** Its coordinates, *balances*, are
  log-ratios of the geometric means of two groups of parts (Egozcue et al. 2003; Egozcue &
  Pawlowsky-Glahn 2005). The group holds are geometric means, chosen for orthonormality, and
  (n − g) + (g − 1) = n − 1 is the partition's count.
- **Finding a grouping in data is solved, two ways.** Ward clustering on the *variation matrix* — the
  variance of each log-ratio across samples — merges the most nearly proportional parts first, and
  the distance between two clusters is proportional to the variance of a balance, so the
  dendrogram is a partition (*Insights in hierarchical clustering of variables for compositional
  data*, 2023). *Principal balances* choose the partition whose balances successively carry the
  most variance (Pawlowsky-Glahn, Egozcue & Tolosana-Delgado 2011; Martín-Fernández et al. 2018).
  **§5.12's "which composites stay fixed across instances" is the variation matrix.**
- **That stability as a statistic** is *proportionality*, built on log-ratio variance and zero when
  two parts move exactly in proportion (Lovell et al. 2015).
- **The denominator paradox of §4.1 is Pearson's spurious correlation:** independent quantities
  divided by a common divisor become correlated (Pearson 1897).

**Taken:** these citations wherever §5.10–§5.12 use the structures, and Ward clustering on the
variation matrix as the method for any test of grouping on real data. **Not claimed here:** the
n − 1 count, the partition, or grouping from data.

**Left as this paper's own:** reading the partition as how freedoms scale — why relating stays cheap
and local, and why the reader itself already has two levels (§5.10d) — and what a grain does to one
(§5.12b–c). The statistics takes its data matrix as given and never
quantises.

### 7.3 Loops: avoided in one literature, used in another

Compositional practice picks n − 1 pairwise log-ratios forming an acyclic connected graph and
treats a cycle as redundancy to remove (Greenacre 2018). Ranking theory uses cycles as §5.12b
does: HodgeRank splits pairwise comparisons on a graph into a gradient part, the consistent
ranking, and a cyclic part measuring how far the data depart from any ranking, locally and
globally (Jiang, Lim, Yao & Ye 2011). Consistency of pairwise ratio judgements around a loop is
also the concern of the analytic hierarchy process (Saaty 1980), and the closure phase of radio
interferometry is a third instance (*The Closure Phase*).

**Taken:** the Hodge vocabulary for §5.12b — a tree's readings are the gradient, and a loop's
closure is the cyclic remainder. **Left as this paper's own:** the junction. A grouping with shared
freedoms is a balance partition and a cycle audit at once, and the whole-step bound of §5.12b is
what the audit looks like under a grain.

### 7.4 Lenses: the fisheye as one of a family

> **(1 Oct)** Where the fisheye "should be expected to lose" is the better/worse framing set aside on 27 September; the lens facts stand.

The map from visual field to primate primary visual cortex has a magnification falling as
k/(r + a) with eccentricity (Van Essen, Newsome & Maunsell 1984). Schwartz modelled it as
w = log(z + a), the offset a setting the size of the foveal representation (Schwartz 1977,
1980): flat inside a, logarithmic beyond — proportional before a corner and logarithmic after it.
The far periphery needs a second pole of opposite sign, w = log((z + a)/(z + b)) (Balasubramanian,
Polimeni & Schwartz 2002).

**The fisheye is exactly this two-pole map with its poles on the imaginary axis** (`lens_family.mjs`,
to 2 × 10⁻¹⁶):

> **atan s = (1/2i) · ln((1 + is) / (1 − is)).**

Read by the local slope of the magnification — 0 flat, −1 logarithmic, −2 saturating — the three
differ in one thing, the width of the logarithmic band:

| lens | s = 0.01 | 1 | 10 | 100 | 10⁴ | [0, ∞) maps to |
|---|---|---|---|---|---|---|
| fisheye, poles at ±i | 0.00 | **−1.00** | −1.98 | −2.00 | −2.00 | π/2 |
| one pole, a = 1 | −0.01 | −0.50 | −0.91 | −0.99 | −1.00 | ∞ |
| two poles, a = 1, b = 100 | −0.01 | −0.51 | −1.00 | −1.49 | −1.99 | ln(b/a) = 4.61 |

**The fisheye passes through the logarithmic regime at one point only, and that point is the
corner.** Two real poles pass through −1 at √(ab) and stay within half a unit of it across the whole band from a to b.

> **Taken: the fisheye is the conjugate-pole member of the two-pole logarithmic family — the one
> whose logarithmic band has zero width and sits on the corner.**

**And the lens of vision is not a fisheye.** It is the two-pole map with real poles far apart. §5.1
names the fisheye after what a lens does to a scene, and that stands; it does not propose the
fisheye as the eye's.

### 7.5 Efficient coding: a lens is matched to a world

> **(1 Oct)** As §7.4: the comparison is an engineering question, outside the paper's scope since 27 September.

A neuron with a limited output range carries most information when its response is the cumulative
distribution of its inputs, so that every output level is used equally often. The fly's
contrast response follows the distribution of natural contrasts (Laughlin 1981). For a
population, the optimal density of cells is proportional to the prior, and a prior falling as
1/s gives discrimination thresholds proportional to s — Weber's law (Ganguli & Simoncelli 2014).

**So every lens has a world for which it is the efficient code.** The fisheye, atan s, is the
cumulative distribution of the Cauchy; the logarithm is the efficient code for a world with no
scale; a two-pole map is the efficient code for a world between two scales.

> **Taken: beside every statement that the fisheye is forced on a reader, the statement of when
> it is efficient.** The two agree where the reader steps evenly in its own facing (§5.1), which is
> where the fisheye is the Cauchy. **Where the world has a scale, efficient coding predicts a
> different lens** — and that is where the fisheye should be expected to lose.

### 7.6 Quantisation: the depth law in general form

The error of a quantiser with level density λ on inputs of density p is Bennett's integral,
D ≈ (1/12) ∫ p/λ² dx (Bennett 1948). Panter and Dite (1951) found the density that minimises it,
and Lloyd (1982) and Max (1960) gave the conditions for a fixed number of levels to be optimal;
Gray and Neuhoff (1998) survey the field.

**Taken: §5.12c's depth law is a Bennett-type calculation for one lens and one error measure.** The
measure is a choice. d\* = 0.772 minimises rms error in ln s; a worst-case bound or an information
criterion gives a different optimum. **So d\* is a property of the fisheye storage and that measure
together, not of scaling** — and under a uniform log grid there is no d\* at all (§5.12c).

### 7.7 Examined and set aside

Rate-distortion theory supplies the vocabulary of rate spent and distortion kept, but its results
concern long codes and add nothing specific here. Relational quantum mechanics shares the stance
that facts are relative to an observer (Rovelli 1996) and carries no lens and no grain. Rational
inattention models capacity-limited agents (Sims 2003); it is an economics of choosing rather
than of reading, and is cited without being built on.

### 7.8 Arrival and partial information

§5.15's two situations each have a literature, and in both the literature supplies the structure
by requirement where this paper derives it.

**Serial arrival, extended but never revised.** Domain theory, from Scott, formalises partial
information: a computation that has not finished is a partially defined object, later results only
extend it, and admissible functions must be monotone and continuous — continuity being taken as a
necessary condition of computability (Scott 1970; Abramsky & Jung 1994). Brouwer's choice
sequences make the same point about the continuum: only a finite initial segment is ever known, and
the continuity principle says a total function depends on that segment alone (Troelstra 1977).
**Here the monotonicity is not required but derived:** a composite is final the moment its two
freedoms have arrived, because the hold cancels from it (§3, §5.12a).

**Parallel arrival, glued.** Sheaf-theoretic sensor integration asks whether local readings form a
global section, a consistent whole, and measures their failure to by a consistency radius
(Robinson 2017). That is §5.12b's loop audit in general form. A sheaf takes its cover as given; this
paper says why one standpoint cannot supply one — its horizon.

**Replicated state, and the freeze.** Conflict-free replicated data types and LVars keep state that
only grows, and a merge that forgets the order in which it grew (Shapiro et al. 2011; Kuper &
Newton 2013); the CALM result ties coordination-free computation to exactly that monotonicity
(Hellerstein & Alvaro 2020). That matches the Unit Rule's sum check, which is blind to order. What
such systems cannot do without coordination is **know that nothing more will arrive** — the
negative information a *freeze* asserts. §5.15 meets the same wall from inside: completion is
inferred, never observed, and the landmark check, which is not blind to order, is the reader's own
contribution.

**Taken:** these citations for §5.15, and the one-sided statement of completion. **Left as this
paper's own:** that the two accounts are one reading traded for another at a priced exchange, and
that a serial reading built over parallel data yields both address and magnitude.

### 7.9 The indirections

**A reader holding the whole pair has no indirection.** The bounded reader of §5.10d has two:
magnitudes against a hold give addresses, and addresses against a grain give positions.

| framework | indirections it has | what it takes them to be |
|---|---|---|
| classical geometry and mechanics | none | the configuration is given whole |
| measurement theory, Buckingham's π theorem | one: quantity to ratio | a definition, or a symmetry |
| compositional data analysis | one, iterated: parts to log-ratios to balances | a coordinate choice |
| cortical maps, efficient coding | one: stimulus to cortical position or response | anatomy, or an optimum matched to a prior |
| companding and floating point | **two**: a lens, then a uniform grain | an engineering design (ITU-T G.711; IEEE 754) |

**The indirections belong entirely to the register; how well they fit belongs to the world.** The
seam, where one address meets several magnitudes, is the world failing the indirection (§5.15);
whether the fisheye is the efficient lens is the world's distribution (§7.5); whether a grouping's
inside composites stay fixed is the world's answer to §5.12.

**And this is why so much can be done without either.** Wherever the denominators cancel, the
reader drops out: routes agree, holds can be replaced, the identity holds. **The observer-free
account is correct as far as that — and the detail beyond it lives in the residuals**, which need
both indirections: the whole-step closure of §5.12b, the placement and depth law of §5.12c, the
horizon, the seam, and completion. Companding has both indirections and never derived them; the
depth optimum exists only when both are present.

### 7.9a The circle as baseline, and coarse-to-fine arrival

> **(1 Oct)** "The circle is where the reader starts" does not stand: the reader is not the unit circle (R127). The circle is the view from nowhere; situation 3 is situation 2 with v's breadth unknown (R143).

§1's ruling 9 has anchors in four literatures, and each holds a part of it.

**The circle as the baseline a shape departs from.** *Radial-frequency patterns* in vision science are
closed contours built by sinusoidal modulation of a circle's radius, ρ(θ) = r₀(1 + A sin(ωθ + φ)), so a
shape is a circle with n lobes expressed on it and A = 0 is the circle (Wilkinson, Wilson & Habak 1998).
**Fourier descriptors** normalise the cumulative angular function so that a circle maps to zero, calling it
the most shapeless closed form (Zahn & Roskies 1972); the zeroth harmonic of a radial series is a circle
and every later harmonic is a departure from it. In physics the same architecture is a sphere plus
corrections: a nuclear surface as R(θ) = R₀(1 + Σ βλ Yλ0(θ)), the geoid as a reference ellipsoid plus
harmonics, and the multipole expansion as a sum of terms with progressively finer angular features.
**And the Fourier-descriptor case is the parallel situation.** Its signature is the accumulated change in
direction along the boundary, computed as a difference between neighbouring pieces of a polygon given
whole and in order; a circle is normalised to zero there because a circle accords with the intuition of
being shapeless. That reading needs two arrivals held at once, adjacent and in sequence, which a
one-register reader cannot form.

**And that signature is a composite of two freedoms sharing a hold** (`curvature_composite.mjs`). Per step
the reader has two magnitudes, the turning dθ and the arc ds. Read each against the curve's own totals —
dθ against 2π/n, ds against L/n — and both are freedoms by §1; their composite is the curvature, and
**both holds cancel from it**, which is §3's law. Over 720 steps a circle reads **1.0000 at every step**, at
radius 1 and at radius 37 alike: turning and arc take the same share, so **the circle is the corner**. An
ellipse of 2:1 runs 0.3855 to 3.0838. So the zero those descriptors normalise to is this paper's corner —
the same landmark, subtracted there and divided here. **And the normalisation they justify by intuition is
forced here:** a reader with no outside unit has nothing to divide by except the curve's own totals, and
reading a thing against itself gives the corner. It also says why the signature needs the whole curve: its
hold is 2π and L, which a serial reader does not have until the end. (Deep modulation turns the composite
negative — the signed case, which §5.17 puts outside a one-register reader.)

**Taken:** these as precedent for the form. **Left as this paper's own:** the circle as what a reader *has*
before anything arrives, rather than an origin chosen for convenience. **They are in parallel, with n known
and the whole curve in hand, and the circle is their normalisation; this paper is in serial, and the circle
is where the reader starts** (ruling 3).

**The threshold.** A trigonometric polynomial of degree m is determined by 2m + 1 distinct samples, so k
arrivals spread over the turn support perturbations up to about (k − 1)/2 lobes. **Not claimed here:** the
theorem, which is classical.

**Coarse to fine.** Progressive image transmission sends the low frequencies first and refines later
(JPEG's spectral selection; Shapiro 1993), and progressive coders state plainly that ordering the
bitstream coarse-to-fine is a design choice. **Left as this paper's own:** that for a serial reader the
order is not chosen. Nothing decides it; the arrivals cannot carry the finer perturbations until there
are enough of them.

**The circle inside the Cauchy.** That the tangent of an evenly spread angle is Cauchy-distributed is
classical and is stated geometrically on the circle (Cuadras 2002; Larson & Odoni 1981), and the circular
Cauchy is the uniform distribution on the circle carried by Möbius maps (McCullagh 1996). **And the reader
owns only part of that closure** (`mobius_reader.mjs`): of the maps the family is closed under, a
one-register reader can change the hold and swap the two parties — §4's identity and inverse — and both
leave a stream half-Cauchy and move only its corner (KS 0.0041 against a 5% band of 0.0056, corner 0.998 →
6.989 under a sevenfold hold, 1.002 under the swap). The rest need **addition**: a shift scores 0.3745 and a
general map 0.2079, both far outside the band. **So the gap between what the Cauchy is closed under and what
a reader can do is exactly addition, which this series charges for everywhere else.** **Left as this
paper's own:** that the even turn assumed there is the same assumption that makes serial arrival
coarse-to-fine (ruling 8, ruling 9). ⚠ *Fisheye* is this series' own name for the tangent's spacing; no
source uses it for the Cauchy.

### 7.10 What this paper claims, after this section

Ratios, their n − 1 count, the balance partition, grouping from data, loop audits, logarithmic
lenses and partial information are established elsewhere and are cited as such. **What is added is a reason, and the
predictions that follow from the reason rather than from ratios:**

1. **A bounded reader must hold ratios, and has exactly two levels of its own**; grouping is how freedoms scale past them (§0, §5.10, §5.10d).
2. **Under a grain, a loop's closure is a whole number of steps**, with a counting threshold for refutation (§5.12b).
3. **Under a grain, holds must keep their readings within the storage's range**; the best span d\* holds only for storage in angle (§5.12c).
4. **The fisheye is the zero-width member of the two-pole family** — forced on a reader, and efficient only for a Cauchy world (§7.4–§7.5).
5. **Serial arrival trades data for address**, at one of three prices — the figure and the scale, the gain alone, or nothing and no rate (§5.15).
6. **A serial reading built over parallel data yields both**: the Unit Rule's record plus one held value, or the Cauchy's address into a held array (§5.15).
7. **Completion is inferred, never observed** — an open record refutes a return, and a closed one does not prove it (§5.15, §7.8).
8. **The indirections are the register's, and their fit is the world's** (§7.9).
9. **A freedom is infinitely dense, not infinitely long.** N magnitudes hang on N hangers of π/(2N) —
   equal and uniform in turn, unequal and Cauchy-arranged in address, one share each — and the
   horizon is where no further hanger can be hung, near 2N/π (§5.16).
10. **In serial, one freedom is enough.** A one-register reader of unsigned magnitudes uses exactly one:
    it always has room, a second adds no distinction, and no event in a stream crosses a join (§5.17).
11. **The n-cube prediction** of §5.14, still unfalsified.
12. **The shape is the unit circle, expressed, and serial arrival expresses it coarse first** — where the
    order is forced rather than chosen (§1 ruling 9, §7.9a).
13. **The reader produces the address; the turn and the circle are the outside view's** (§1 ruling 10).
14. **A shape is a freedom that has spent its radius** — every figure is a centring, the circle the one with
    no residue, and a figure held fixes the level of expression of everything read against it (*The
    Centring*).

### References for §7

The series' own papers are cited by name in the text — *The Relation Space*, *The Six Things*, *The Unit Rule*, *The Cauchy*, *The Lap Rule*, *Browsing the Fisheye*, *The Closure Phase*, *The Centring* — and are not repeated here.


- Abramsky, S. & Jung, A. (1994). Domain theory. In *Handbook of Logic in Computer Science*, vol. 3. Oxford University Press.
- Aitchison, J. (1986). *The Statistical Analysis of Compositional Data*. Chapman & Hall.
- Balasubramanian, M., Polimeni, J. & Schwartz, E. L. (2002). The V1–V2–V3 complex: quasiconformal dipole maps in primate striate and extra-striate cortex. *Neural Networks* 15, 1157–1163.
- Bennett, W. R. (1948). Spectra of quantized signals. *Bell System Technical Journal* 27, 446–472.
- Buckingham, E. (1914). On physically similar systems. *Physical Review* 4, 345–376.
- Cuadras, C. M. (2002). Geometrical understanding of the Cauchy distribution. *QÜESTIIÓ* 26, 283–287.
- Egozcue, J. J. & Pawlowsky-Glahn, V. (2005). Groups of parts and their balances in compositional data analysis. *Mathematical Geology* 37, 795–828.
- Egozcue, J. J., Pawlowsky-Glahn, V., Mateu-Figueras, G. & Barceló-Vidal, C. (2003). Isometric logratio transformations for compositional data analysis. *Mathematical Geology* 35, 279–300.
- Ganguli, D. & Simoncelli, E. P. (2014). Efficient sensory encoding and Bayesian inference with heterogeneous neural populations. *Neural Computation* 26, 2103–2134.
- Gray, R. M. & Neuhoff, D. L. (1998). Quantization. *IEEE Transactions on Information Theory* 44, 2325–2383.
- Greenacre, M. (2018). *Compositional Data Analysis in Practice*. CRC Press.
- Hellerstein, J. M. & Alvaro, P. (2020). Keeping CALM: when distributed consistency is easy. *Communications of the ACM* 63(9), 72–81.
- IEEE 754-2019. *IEEE Standard for Floating-Point Arithmetic*.
- ITU-T Recommendation G.711 (1972). *Pulse code modulation of voice frequencies*.
- *Insights in hierarchical clustering of variables for compositional data* (2023). *Mathematical Geosciences*. doi:10.1007/s11004-023-10115-4.
- Jiang, X., Lim, L.-H., Yao, Y. & Ye, Y. (2011). Statistical ranking and combinatorial Hodge theory. *Mathematical Programming* 127, 203–244.
- Krantz, D. H., Luce, R. D., Suppes, P. & Tversky, A. (1971). *Foundations of Measurement*, vol. I. Academic Press.
- Kuper, L. & Newton, R. R. (2013). LVars: lattice-based data structures for deterministic parallelism. *Proceedings of the 2nd ACM SIGPLAN Workshop on Functional High-Performance Computing*, 71–84.
- Larson, R. C. & Odoni, A. R. (1981). *Urban Operations Research*. Prentice-Hall. (§3.3.3, the Cauchy from a uniform angle.)
- Laughlin, S. (1981). A simple coding procedure enhances a neuron's information capacity. *Zeitschrift für Naturforschung C* 36, 910–912.
- Lloyd, S. P. (1982). Least squares quantization in PCM. *IEEE Transactions on Information Theory* 28, 129–137.
- Lovell, D., Pawlowsky-Glahn, V., Egozcue, J. J., Marguerat, S. & Bähler, J. (2015). Proportionality: a valid alternative to correlation for relative data. *PLoS Computational Biology* 11, e1004075.
- Martín-Fernández, J. A., Pawlowsky-Glahn, V., Egozcue, J. J. & Tolosana-Delgado, R. (2018). Advances in principal balances for compositional data. *Mathematical Geosciences* 50, 273–298.
- Max, J. (1960). Quantizing for minimum distortion. *IRE Transactions on Information Theory* 6, 7–12.
- McCullagh, P. (1996). Möbius transformation and Cauchy parameter estimation. *Annals of Statistics* 24, 787–808.
- Panter, P. F. & Dite, W. (1951). Quantization distortion in pulse-count modulation with nonuniform spacing of levels. *Proceedings of the IRE* 39, 44–48.
- Pawlowsky-Glahn, V., Egozcue, J. J. & Tolosana-Delgado, R. (2011). Principal balances. *Proceedings of the 4th International Workshop on Compositional Data Analysis*, Girona.
- Pearson, K. (1897). On a form of spurious correlation which may arise when indices are used in the measurement of organs. *Proceedings of the Royal Society of London* 60, 489–498.
- Robinson, M. (2017). Sheaves are the canonical data structure for sensor integration. *Information Fusion* 36, 208–224.
- Rovelli, C. (1996). Relational quantum mechanics. *International Journal of Theoretical Physics* 35, 1637–1678.
- Saaty, T. L. (1980). *The Analytic Hierarchy Process*. McGraw-Hill.
- Schwartz, E. L. (1977). Spatial mapping in the primate sensory projection: analytic structure and relevance to perception. *Biological Cybernetics* 25, 181–194.
- Schwartz, E. L. (1980). Computational anatomy and functional architecture of striate cortex: a spatial mapping approach to perceptual coding. *Vision Research* 20, 645–669.
- Scott, D. (1970). Outline of a mathematical theory of computation. *Technical Monograph PRG-2*, Oxford University Computing Laboratory.
- Shapiro, J. M. (1993). Embedded image coding using zerotrees of wavelet coefficients. *IEEE Transactions on Signal Processing* 41, 3445–3462.
- Shapiro, M., Preguiça, N., Baquero, C. & Zawirski, M. (2011). Conflict-free replicated data types. *Stabilization, Safety, and Security of Distributed Systems*, LNCS 6976, 386–400.
- Sims, C. A. (2003). Implications of rational inattention. *Journal of Monetary Economics* 50, 665–690.
- Stevens, S. S. (1946). On the theory of scales of measurement. *Science* 103, 677–680.
- Troelstra, A. S. (1977). *Choice Sequences: A Chapter of Intuitionistic Mathematics*. Oxford University Press.
- Van Essen, D. C., Newsome, W. T. & Maunsell, J. H. R. (1984). The visual field representation in striate cortex of the macaque monkey. *Vision Research* 24, 429–448.
- Wilkinson, F., Wilson, H. R. & Habak, C. (1998). Detection and recognition of radial frequency patterns. *Vision Research* 38, 3555–3568.
- Zahn, C. T. & Roskies, R. Z. (1972). Fourier descriptors for plane closed curves. *IEEE Transactions on Computers* C-21, 269–281.

---

## 8. What is open

> **(1 Oct)** Calls here for outside data are planned tests now (26 Sep). New open items are kept in v-and-h §9.

Ordered by what would move the paper rather than by how interesting it sounds.

**0. ~~Depth is unruled.~~ ⚠ RULED, §5.19: depth is z, the serial signal, and it is the log radius.**
Tom listed four consequential differences in the serial case — *depth, a g less than 1, an asymmetry
between v and h, and N unknown* — and all four are now grounded (§5.16, §5.18, §5.19). The ruling
passed the test it had to pass: **z is not a function of x and y**, so 1d and 2d are genuinely two
signals, and 3d is a cylinder — direction round the plane, log radius up the axis.

**~~What it opens in its place.~~ ⚠ ANSWERED, §5.11 and `depths.mjs` B164–B167: they are one
notion.** The question was whether §5.11's indirection depth — a count of compositions — and §5.19's
z — a coordinate in grains — are the same thing. **They are, and the relation is differencing.**

The answer that suggests itself is wrong and was killed first: *they differ because indirection lives
in the address channel and z in the residue channel.* **The residue channel is closed under addressing
exactly as the address channel is**, so the indirection tower stands **on** z. They are not in two
places.

> **Order 0 of the tower is z. Order 1 is the grain between arrivals. Order n is the nth difference
> of z** — exact at every order, to 3.6e−15 at order 5, with the binomial signs falling out of the
> construction rather than being put in.

**And the two behaviours this item called different are one property.** Indirection being free and z
being bounded is not a tension to resolve: every tower term is a zero-sum combination of the
magnitudes and a coordinate is not, so **depth is free exactly because it never reaches a coordinate**
(§5.11). What remains, and is smaller than what was asked: the **combinatorial** tower spans the same
subspace, but whether every composite a parallel reader can form is a difference of z *in the same
sense* is not measured.

**0a. And the 3d questions the join opens** (`three-dimensions.md` §5, seven of them). The two that
bear hardest on this paper: everything in §5.18 assumes the two signals are **about one hanging**, so
if 3d admits signals of genuinely different things the join is a different operation; and **nothing
plays the corner's role for a correspondence** — in a freedom the corner is findable without a unit,
and whether a join has such a landmark is unknown. Added to those, **the band's shape**: §5.18 gives
its width but not how it scales with N. ~~nor whether a reader can detect that it is inside one~~ —
**⚠ that last is answered, and negatively (§9.7n, B161–B163): it cannot, within its means.** The
ambiguity is 2× at every separation while only an adjacent coincidence shows in the moves; memory
buys detection at exactly k/(n−1); and no affordable summary catches the rest.

**0b. ⚠ Three further items are now settled, and two of them cost this paper something** (§9.7o).

**Reading a count as a turn is not forced — for a lone reader** (`forced.mjs`, B168–B170). Four rival
maps from a count into [0, ∞) pass **every constraint this paper states** — the ray, the corner, the
swap, closure, scale-freedom. The nearest is the **odds map**, (M−n+½)/(n−½), which is the standard
log-logistic and reads 3.0 at q75 where the Cauchy reads 2.4142. What separates them is the one
condition that cannot be stated from a single standpoint: **that the reading survive a change of
standpoint**, where the arc holds to 0.0024 and the rivals drift by 1.69, 11.2 and 39.6. *So the arc
is forced by a second reader, and `arch.js`'s choice is the one that costs nothing if company arrives
and everything if it does not.*

**The necessity is cited, and the citation was wrong** (`rigidity.mjs`, B171–B174). "The Cauchy is
the unique family **invariant** under the real Möbius group" is false as written — the orbit of any
law is setwise invariant. Knight (1976) proves something stronger: the Möbius orbit **is** the affine
orbit. ⚠ **And a reader never holds the object the theorems characterise**: they need a measure
charging no point, and a finite reading is atomic at every n.

**The world's symmetry splits by reader grade** (`world.mjs`, B175–B178). A **counting** reader learns
nothing of the world; a **pair** reader, holding v and h, separates symmetric worlds from lopsided
ones on a median and reaches 90% power against the log-logistic at n = 512, with no unit and no N. ⚠
**But it has checked the conclusion, not the hypothesis** — B155 gave sufficiency only — and because
v and h are magnitudes it sees one quarter, which is where the remaining gap now sits: *a property
defined on the full circle, read from magnitudes that only ever land in one quarter.*

**1. ~~The angle is borrowed for the measure.~~ Answered in §5.7, and not as expected.** A freedom
has its own measure — ln(b/a), additive and invariant under composing, and essentially the only
one — and **it is the grain the series has used since *The Radix***. In that measure a freedom
holds infinitely many addresses toward either end, where the angle gives its extent as a finite
quarter; the one is its density and the other its extent (§5.16).
**The two disagree, so the π/2 was never a debt to repay: it is a different measure, imported with
the angle.** What remains is a smaller question — whether anything in the series still *needs*
the borrowed measure, or whether every π/2 in it can be restated in grains.

**2. The n-cube prediction needs outside data.** §5.14 states it — 2ⁿ states, n neighbours each, a
closed tour, binomial distances — and every system available here was one this paper would have
built, so it is recorded unfalsified rather than confirmed. **It is the cheapest outstanding
test and the only one that can fail on first contact.**

**3. Whether a sphere is eight copies of this relation space.** §5.1 separates three claims: eight
regions of two freedoms each is derived, the eight tiling a sphere is consequential and imports
conventional spherical measure, and the identification itself is **not established**. Nobody
here has made that argument, and making or refuting it is the obvious next piece.

**4. ~~Whether the composites are freedoms in the full sense.~~ Ruled: they are.** A composite is
formed as one thing against another, is unchanged when both are scaled, and addresses rather
than values — it meets the definition, and that is the whole of the test (§1). **There is no
reason at this stage to sort freedoms into types.** §5.11 makes the ruling cover every order at
once, since composing composites produces nothing of a new kind. What would reopen it is a
composite that fails one of the three tests, and none has been found.

**5. ~~Whether the fixed-hold and moving-hold structures are one structure.~~ Answered in §4.5:
they are one.** The moving readings are the fixed structure's own composites relabelled,
multiplying them is dividing the fixed readings at the two ends, and the landmarks coincide
because they are the same landmarks. What remains is smaller: **whether a reader can tell from
its readings alone which of the two it is holding.**


**6. ~~Where the extra pairs go.~~ Answered in §5.12, and the answer cuts against the framework.**
They are forced — n − 1 measurements fix every other pair — but the forcing is an **identity**,
true of any numbers whatever, so on its own it predicts nothing. **What predicts is the grouping**:
which composites stay fixed as instances change, and which are free to vary. That is
falsifiable, and a composite inside a hold that varies across instances would refute the
grouping. **How large a deviation should count as a refutation is answered in §5.12b for a reader
that quantises**: a loop's closure is a whole number of steps, and past ⌈L/2⌉ − 1 of them it is
not grain. **Grouping here is the reader's bookkeeping for how freedoms scale (§5.10), not a claim about how the
world is arranged,** so a varying composite refutes the grouping for that set of instances and says
nothing further. The continuous, noisy case is set aside for later consideration.

**7. The scale-invariance conjecture.** *Every scale-invariant quantity either divided or counted*
survived five cases and named its own exception (§5.5), which is support and not proof. **The
refutation to look for: something invariant under scaling that neither formed a ratio nor kept a
tally.**

**8. Symmetry.** If two freedoms are interchangeable then c and 1/c are one address, the composites
fold at the corner, and what a set of freedoms can distinguish halves. The fold is easy to state
and its consequences are not worked out.

**9. The two-pole family and the levels.** A two-pole map is the difference of two logarithms —
a reading against two holds — and its logarithmic band runs between them (§7.4). A single reader
gets the zero-width band of the fisheye. **Whether a reader with two holds acquires a band
between them**, tying the lens family to the levels of §5.10d, is suggested by the form and not
shown. It is a derivation to attempt before any claim.

**10. Completion, certified from inside.** A serial record's two checks refute a return and do not
certify one, and a Cauchy lap certifies the frame rather than the figure (§5.15). **Whether any
bounded rule can certify that a serial arrival is complete** — not merely unrefuted — is not
shown, and the replicated-state literature (§7.8) suggests it needs something outside the reader.

**11. And last, which freedoms to plug in — with the count no longer the point.** §5.1 sets out three
worked examples, and §5.9 shows the construction has no preferred size: the law holds
identically at two, ten and five hundred. **So the later paper's job is not to find three
freedoms to match three directions.** It is to show that freedoms compose with arbitrary
complexity and that the composites stay addresses — which §5.9 begins and §5.8 says why. Three
cautions belong with any attempt on the ontological version, all decided by work already here:

- **The walk and the facing are one kind and two readings**, not one reading under two names (the
aside in §5.1). A reader holding one standoff has both, and the facing is the composite of them.
- **Closure is not a reading at all.** It is a property of how signed copies join. Counting
it beside two readings gives *two kinds of thing*, not three freedoms of equal standing — the
error that retired an earlier paper in this line.
- **And the scarce resource is the arrival, not the register.** Holding one standoff, both
extents of an arrival read against it and the facing falls out as a composite, so the two do not
compete for the hold. What they need is an arrival carrying two extents (`compete.mjs`) — a
claim about instruments, testable where the register version is not.

**The safe form of the later claim** is therefore narrower than *these three and no others*: a
one-register reader has **one hold, as many readings as the arrival carries, and the composites
those make** — with closure as what lets the whole thing return.

**13. ~~Does the settling test hold on an incremental stream?~~ Answered, and it does not**
(`settling_incremental.mjs`, §1 ruling 9). On a growing set a landed reading can un-land (the 2-lobe reads
0.3000 at 13 arrivals, 0.1752 at 21, 0.3000 again at 27), a still reading can move later (0.0000 at 13,
0.1045 at 21), and declared landings cluster where the whole fit became exact rather than at each lobe's
own threshold. **What survives is a global test only:** when every reading stops moving, the shape as a
whole has landed. ⇒ **The one positive capability this paper gave the constrained reader is withdrawn.**
What replaces it, if anything — an internal criterion that marks a single landing under real arrival — is
open.

**12. Flagged contradictions, held for later consideration.** Each is a place where two statements in
this series disagree. Neither side is withdrawn until it is ruled on. **(d2) is the priority.**

- **(a) ~~What r = 0 is: no expression, or arrival.~~ Resolved (Sep 17):** they are two different dials,
  both called a radius. The definition's r is **expression** — at r = 0 the shape is gone and the unit circle
  remains (rulings 4, 9). *Browsing the Fisheye* §8's radius is **reach** — at 0 the window holds one record,
  and the reader has arrived at what it pointed at. Each is right about its own dial.
- **(b) ~~Two uses of *radius*.~~ Resolved (Sep 18) by renaming, not by widening.** The definition's dial
  is now **g**, the expression, on [0, 1], unitless, the reader's (rulings 5, 11). **r** keeps the other
  job: a figure's radius in a direction — the hold's or an arrival's size against a laid-down unit, as
  §4.3 tabulates at 10, 1, 0.1 and 0.01. Two dials, two letters. ⚠ Sections written before the rename may
  still say *radius* for the expression; the definition, the rulings, the marks table and §2.1–2.2 are
  converted, and the rest is a sweep still owed.
- **(c) Premise S of *The tower of holds, formally* (archived Sep 17) stores readings in turn.** Its T7–T10 — the route
  error, the depth law d · tanh d = ½, the golden-ratio split and the best hold h* — assume each reading is
  kept as the angle u = atan(eʳ) rounded on an even grid. An even grid in turn is the parallel picture
  (ruling 3, ruling 8); a serial reader meets the fisheye, not a turn grid. And the results do not survive a
  change of storage (`storage_compare.mjs`, 256 levels per reading): a log grid of about the same range
  (±5 against the angle grid's implicit ±ln(2K/π) ≈ ±5.1) carries a span of 10 in **2 readings at rms
  0.016**, where the angle grid needs **13 readings for 0.017**, and it has no interior optimum — it splits
  only to fit its range. So the depth law and the split threshold are properties of rounding in turn, not
  of scaling. **And (d1) now rules the storage:** the register's grain is ln(b/a), so a serial reader stores
  in log, premise S describes a parallel observer's store, and T7–T10 do not apply to the reader.
- **(d) ~~Two native measures for the same reader.~~ Split (Sep 17): one half is settled, the other is the
  open question.** The two candidates were never rivals — they govern different things (`traverse_grain.mjs`).
  - **The TRAVERSE** is how the arrivals are spaced: the reader's movement, or the world's schedule. §5.1's
    equal steps of facing are this.
  - **The GRAIN** is how finely the register tells two addresses apart. §5.7's ln(b/a) and *The Radix* are
    this.
  - **They coexist, measured.** An even traverse stored on a log ladder stays half-Cauchy — KS 0.0043 exact,
    0.0121 at grain 0.05, 0.0353 at 0.2, 0.1126 at 0.6931, against a 5% band of 0.0068 — while its stored
    values sit at 31.99, 63.98, 128.0, 255.9, 511.8, 1024, a ladder of exact doublings. **A traverse that is
    itself even in ln s is not Cauchy at all: 0.4876.**

  **(d1) The grain — settled.** The reader's own measure is ln(b/a) and its register steps in that (§5.7).
  Nothing in the Cauchy chain is threatened, because storage is not traverse. The circularity charge is
  answered here: the grain is fixed by the reader's own operation, not by what it recovers.

  **(d2) The traverse — open, and this is the question.** Why are the arrivals spread evenly over the turn?
  No argument from the register forces it: evenness is a property of the source, something turning at a
  constant rate and met at a constant rate, which is the continuous-observer baseline. **So the even turn is
  an assumption about the world, and the grain is the reader's** (ruling 8).

  ⭐ **And the series already has evidence about it, and an instrument that decides it per stream.** The
  applicability screen tests exactly this — whether a stream's arrivals are Cauchy, which is the even
  traverse — and the record reads:
  - **Evenness is not generic.** Every real signal put to the screen was refused, each with a nameable
    physical cause: four handheld video clips, a chirp, a cymbal, a fire alarm, a voice, room hum. Meanwhile
    45 of 45 library figures met evenly passed, and figures walked at their own pace were caught 35 times in
    44, with the misses a named class rather than a mystery.
  - **How far off is measurable, not just pass or fail.** The lens grades how nearly a list behaves as one
    thing turning at one rate: a tone 0.048, a tone with 5% noise 0.220, with 20% noise 0.446, white noise
    1.587, with no overlap across seeds.
  - **And the class that is even has a name:** one centre of gravity in steady periodic motion — a pendulum,
    a metronome, a wheel, a fan blade. Four bodies with identical orbits returned periods agreeing to 1.8%,
    and every refusal above was the instrument pointed at something that is not that.

  ⇒ **So evenness is an applicability condition on the source, rare rather than generic, and decidable per
  stream before the chain is applied.** What that does not give is a reason the world should contain such
  sources at all — a question about physics, not about readers, and the part of (d2) that stays open.

**14. What fixes g, and whether the corpus's own figures have one.** Opened Sep 18 with rulings 11–13.

- **(a) ~~g is named here, not derived.~~ CLOSED (Tom, Sep 18): no derivation is owed, because g is a
  dial the reader sets.** It says how many times to divide the circle, and a dial has no correct value any
  more than a standoff does. ⚠ Which also puts the failed attempt in its place: deriving g from the
  vanishing-point freedom was looking for a fact where there is a choice. The measurement that killed it
  still earns its keep as method — a folding fitted on one generator reproduces that generator's amplitude
  law and says nothing about the reading, and the way to catch that is to divide the generator's own
  amplitude out and look at what is left, which was a plateau and not a peak.
- **(f) THE REMAINDER, and it may be a hole rather than a detail.** A circle cannot be cut a fractional
  number of times, so the count is **⌊gN⌋** and the dial is continuous over an outcome that is not. Two
  consequences are plain and may be more than bookkeeping. **At the bottom there is a dead band**: every g
  below 1/N floors to zero cuts, so the circle is not only at the point g = 0 but across a whole interval
  whose width is the reader's own grain — which is a different statement from the one this paper makes
  elsewhere, and a truer one. **And everywhere else the dial carries a remainder it cannot spend** — the
  fraction of a cut between where g sits and where the last cut fell. Nothing yet says whether that
  remainder is inert or accumulates into a bias, and until something does, **any result stated in g rather
  than in ⌊gN⌋ is carrying an unexamined rounding.** Held open deliberately: it is the most likely place
  for this account of g to fail.
- **(b) The library's figures have no second argument, and are not the witness here anyway.** The standing
  ruling is that `svg.html`'s PRIMITIVES is the evidence base, but those are outlines: each is a generator
  whose g is already spent, at whatever expression its sampling fixed. **Every number checked for rulings
  11–13 comes from generators this series wrote.** ⚠ Tom, Sep 18: *the library is full of really weird
  shapes that are highly improbable* — so it stays the evidence base for falsification, where an adversarial
  figure is a feature, and is **not** automatically the witness for what a real generator does. The witness
  this line of work needs is a generator the world supplies — a brightness round a ring, a rod's extent, one
  number a frame — with an amplitude law nobody chose. Until then the claims stand on formulas.
- **(c) Whether the list is hung on the radius or on the log radius.** Both give the same figure at g = 1.
  The radius form is exact at hinges and can leave the class of figures near the reader; the log form never
  leaves the class and pays at hinges (§2.2). The corpus's own machinery is multiplicative throughout —
  holds divide, residues are ratios, rungs are logs of them, the register's grain is in ln-radius — which
  argues for the log form, and *The Radix* supplies the reason: a scale-free reader steps in ratios, so a
  perturbation it can step by must be a ratio. **Not ruled.** Whichever is chosen, the coordinate must be
  recorded with the list.
- **(d) Whether a real generator is algorithmic.** Definition aside (§2.2), nothing yet says whether a
  measured object answers (direction, expression) at a bounded price, or only by traversal. This is the
  applicability question for everything in this paper that treats g as a dial.
- **(e) And whether it is walkable, which is a different question.** Answering at a price makes a generator
  algorithmic; having its orders in the reader's ratio makes it walkable level by level (§2.2). The
  corpus's own shapes are harmonic in construction, so a reader walking one crosses thousands of orders in
  a rung — **the shape page's octave ladder, chosen by instinct, is the only class this dial can browse a
  level at a time**, and that was luck rather than design.

---

## Where the numbers came from

| the claim | where it came from |
|---|---|
| the image complete at arrival 12 with the lap closing one move later; the miss 0.670 → 3e−15; four slices, one image, z spaced 0.350000 | `slices.mjs` L1–L4 |
| reciprocal closure to 3.220e−15 on a full list; spanning thinnings missing 0.67–0.94; symmetry under k → N−1−k necessary and sufficient; the corner pair closing at 0.000e+0; the z multiset fixed by the facing | `closure.mjs` C1–C4 |
| z accumulating to the same range 2.0149 under three traversals and equalling log(max) − log(min); three figures at one turn giving one address to 7.105e−15; z ranges 0.000000 / 0.969061 / 0.995038 on that one direction list; the z-lap closing at 0 | `depth.mjs` Z1–Z5 |
| the quantile hanger edges moving at every stream length — median 1.087290 at 10³ to 1.000363 at 10⁷ against the turn's 1 — while one arrival's address stays 1.363081673437 throughout | §5.16, run against a mulberry32 stream |
| the figure rebuilt from motion alone at 2.776e−16 with the anchor absent; thinning composing moves, 0.400000 × 3.666667 → 1.466667; the lap product 1.000000000000000 at every g | `serial.mjs` S5–S7 |
| one list yielding 5,040 motion streams; motion + one anchor → the list at 0.000e+0; the verb partition identical to the needs-N partition on all eleven rows | `dimensions.mjs` D1–D6 |
| the join unique in 1,200 of 1,200 random hangings and scale-free to 10^±30; the circle matching 40,320 = 8!; degeneracy exactly 2^r; the grain band, 40,320 orders at 10⁻⁷ from the circle at a grain of 10⁻⁶ and 1 at 10⁻¹² | `standpoint.mjs` T1–T6 |
| a freedom is an equivalence class: (3,4), (21,28), (0.03,0.04) all read 0.75 | `compose.mjs` |
| the shared denominator cancels: c₁₂ = 0.75 and c₂₃ = 0.333333 against H = 1, 7 and 1000 alike | `compose.mjs` |
| c₁₂ × c₂₃ = c₁₃, so three freedoms give two independent composites | `compose.mjs` |
| the same two freedoms composed against holds of 1, 7, 1000 and 0.004 all give 0.75 — the centring test | `compose.mjs` |
| the identity is the corner and the inverse is the party swapped | `compose.mjs` |
| two seats' reads: dividing gives 0.888889 (the size ratio) and multiplying gives 0.1 (the distance factor), while two freedoms on one denominator multiply to 0.244898 with nothing cancelled | `exchange.mjs` |
| the field paradox, the number line's deletion of the receipt, and the 50%-down-50%-up chain | `denominator_paradox.md`, the companion piece |
| ratios, angles, correlations, exponents and shapes are all freedoms or composites; a count is scale-invariant and is not | `invariance.mjs` |
| a list has items and a freedom has none, so counting is the list's operation and sweeping the freedom's; a grain of 0.1, 0.01, 0.0001 gives 16, 157, 15,708 steps across the same quarter | `invariance.mjs` |
| four copies close because each join flips one of two signs and each must flip twice — counting, with no turn in it | `noangle.mjs` |
| the moving readings 1.5, 4, 0.5, 5 are exactly s₁/s₀ … s₄/s₃, and their product 15 equals s₄/s₀ — one structure, not two | `onestructure.mjs` |
| a freedom's own measure is ln(b/a) — additive, invariant under composing, essentially unique — and it makes the freedom infinite at both ends, where the angle makes it a finite quarter | `measure.mjs` |
| the walk and the facing have the same form and different pairs; one hold gives V/S = 0.6, H/S = 0.8 and the facing 0.75 as their composite | `walkfacing.mjs` |
| one value from a generator costs 1, 3, 7, 13, 19, 25 terms at g = 0, 0.1, 0.25, 0.5, 0.75, 1, the same for every direction, while a pathological one costs 129 steps at g = 0.5 and 257 at g = 1 | `path_checks_g.mjs` |
| the two-component reading is blind to g: largest departure from tan u across four generators and six expressions, 4.3e−16, against 1.3e−2 for the hold-following reading | `path_checks_g.mjs` |
| a generator carrying one rung of twenty-four is exactly the circle until g = 7/24 = 0.2917, then at full swing | `path_checks_g.mjs` |
| one rung of the reader gains the octave list exactly one order at rungs 4, 8, 12 and 16, against 8 / 128 / 2,048 / 32,768 for a harmonic list | `radix_expr.mjs` |
| a partial sum on the radius goes negative — grazing −0.1642 and knife −0.0514, both from g = 0.0117 — while the log form stays positive (0.2281, 0.1166) and returns the figure at g = 1 to 2.7e−15 / 1.3e−6, the square costing 5.0e−3 | `inject.mjs` |
| the reader's response is a plateau of width log2(view ÷ grain) octaves — 5, 6, 7, 8, 9 at five glass sizes — and the peak belongs to the list, whose amplitude law ∝ period^α gives arms α and α − 2 across α = 0 … 2 | `example-shape.html`, the Sep 17 bench |
| facing and depth do not compete for the register — both extents read against one standoff, with the facing as composite; the scarce thing is the arrival | `compete.mjs` |
| the semicircle is two signed copies joined at H = 0: its outer ends read 0 and its middle is one reading's ∞ and the other's 0 | `semicircle.mjs` |
| approaching the middle gives +318.31 from one leg and −318.31 from the other, so one place shows two horizons and no path in that reading joins them | `semicircle.mjs` |
| two freedoms address a direction with no angle; one pair is blind on a circle, and of 26 directions none is blind in all three pairs; two pairs leave exactly lat/long's two poles | `charts2.mjs` |
| the n-th direction carries n−1 perpendicularity constraints and the n-th freedom carries none; three extents give six ordered pairs, ten give ninety | `picturing.mjs` |
| grouped freedoms on an ISO metric thread, levels fixed by the standard: H/h₃ = 1.41178 for M6 through M36 alike, while the cross-level residue D/P runs 6, 6.67, 8, 9 | `given.mjs` |
| grouped freedoms on published anthropometric means: index/middle = 0.9036 with the hand gone at any hand size; the cross-level residue 4.1053 is arm/hand exactly; and the level above gives 4.1053 with stature cancelled | `realtower.mjs` |
| four freedoms in two regions: 3/2 = 1.5 inside A with the hold gone; 3/1.5 = 2 across, leaving 3 = 6/2; and the level above gives 3 with the 12 cancelled | `four.mjs` |
| grouped freedoms: a group's hold cancels inside its group, leaves exactly h₇/h₂ = 2.052632 across groups, and that residue is a composite one level up; and (n − g) + (g − 1) = n − 1 always | `tower.mjs` |
| mutating 100 grouped freedoms: one item moves 198 of 9,900 composites, a group hold moves 0, the top hold moves 0; and the fraction moved by one item is 2/N at every size | `mutate.mjs` |
| and a hold set to zero is not a change of value but the horizon: 1,890 composites undefined for a group hold, 9,000 for the top one | `mutate.mjs` |
| the n-cube prediction: 2ⁿ states, n neighbours each, n·2ⁿ⁻¹ joins, a closed tour of 2ⁿ, distances C(n,d) — all four confirmed on a constructed case, which is why it is recorded unfalsified rather than confirmed | `ncube.mjs` |
| four signed terms: 16 regions of 3 freedoms, a Gray-code walk of 16 steps, 4 charts to cover with 3 leaving exactly two directions — and the borrowed measure gives π²/8, breaking the π/2 run | `sixteen.mjs` |
| what is forced needs no measure — joins, returns, coverings, groupings are all counting; and in the native measure every copy is infinitely long, so the turn closes by counting and never by distance | `shapes.mjs` |
| n − 1 composites force all n(n−1) pairs — 81 of 90 at n = 10 — but the forcing is an identity, exact to 1.6e−16 on a thread and 2.5e−16 on body means alike; what predicts is which composites repeat across instances | `forced_pairs.mjs` |
| the space is closed under addressing: a ratio of two addresses is an address, at order 1, 2, 3 and 5 alike, and an address over itself is 1 at every order | `indirection.mjs` |
| a single reader has exactly two levels because it has two holds; a third needs a second grain, and two grains of 0.6931 and 2.3026 give 0.30103, unmoved under scaling | `morelevels.mjs` |
| of the maps the Cauchy family is closed under, a one-register reader owns the hold change and the swap (KS 0.0041 against a band of 0.0056, corner 0.998 → 6.989 and 1.002); a shift scores 0.3745 and a general Möbius map 0.2079 | `mobius_reader.mjs` |
| under incremental arrival the settling test fails: a landed 2-lobe un-lands (0.3000 at 13 arrivals, 0.1752 at 21, 0.3000 at 27), a 0.0000 move is followed by 0.1045 eight arrivals later, and declared landings cluster at 32/32/32 and 26/26/57 against thresholds 5/11/27 | `settling_incremental.mjs` |
| settling: with lobes at 2, 5 and 13, the 2-lobe's hanger reads 0.4500, 0.3000, 0.3500, 0.3000, 0.3500 over 7–15 arrivals and holds at 0.3000 from 17; the 13-lobe appears at 27, its threshold, and does not move again | `settling.mjs` |
| traverse and grain are independent: an even traverse stored on a log ladder reads half-Cauchy at KS 0.0043 exact and 0.0121, 0.0353, 0.1126 at grains 0.05, 0.2, 0.6931 (band 0.0068), its stored values doubling exactly, while a traverse even in ln s scores 0.4876 | `traverse_grain.mjs` |
| the fold: a pure 13-lobe reads as a 1-lobe at 7 arrivals and a 2-lobe at 15, at full amplitude; where the hanger is occupied the readings add (0.500 or 0.100 by phase); and three shapes agree to 1e−15 at 15 arrivals, all reading a 2-lobe of 0.500000 | `hangers_fold.mjs` |
| curvature is a composite of the turning and arc freedoms against the curve's own totals: a circle reads 1.0000 at every step at radius 1 and 37 alike (the corner), an ellipse 2:1 runs 0.3855–3.0838 | `curvature_composite.mjs` |
| the reader itself has two levels: level 0 holds h and reads v/h, level 1 holds the grain and reads ln(s)/σ, and the grain cancels within its level at 0.6931, 1 and 2.3026 alike | `indirections.mjs` |
| at scale: a million freedoms give a trillion dependent pairs and a million independent; relating any two costs at most the depth — 3 at a thousand, 9 at a billion — and flat composition costs nothing but demands one global reference | `scene.mjs` |
| grouping nests: relating two freedoms leaves one residue per level to their common hold, and the independent count stays n − 1 at depth 3, 4 and 10 | `deeptower.mjs` |
| the law holds identically at 2, 3, 4, 5, 10, 50 and 500 freedoms — hold cancels, associative, telescopes, n − 1 independent — and the closure count runs 4, 8, 16, 32, 256 with no step | `arbitrary.mjs` |
| that measure IS the grain: σ = 0.6931, 1, 2.3026 multiply the address by 2, 2.7183, 10; and steps between addresses are ln(b/a)/σ | `measure.mjs` |
| a tally's extent is its count — 5, 50, 500, 5,000 — while the freedom's span stays 1 and its spacing runs 2×10⁻¹ to 2×10⁻⁴: counting needs somewhere further out, and a freedom has none | `invariance.mjs` |
| s = tan u derived from V and H; equal reader steps landing at 0.1584, 1.0000, 3.0777, 12.7062, 63.6567; addresses 1 … a million filling 0.5 … 0.999999 of the reader's range | `fisheye.mjs` |
| the stretch is exactly 1 at the hold and 2, 40.86, 4053 further out; and the hold reads as 1 to itself whatever was laid down | `fisheye.mjs` |
| the quarter is half spent when the arrival equals the hold, 93.65% spent at ten times it; and the smallest visible difference grows as (1 + s²)σ | `fisheye.mjs` |
| the last ε of angle holds everything beyond cot ε — beyond 10, 100, 10,000, 10⁸ — so the horizon is where density diverges; and a grain of σ puts a real reader's horizon near 1/σ | `fisheye.mjs` |
| density per unit sweep runs 1, 2, 40.9, 4,053, 405,285 and diverges at the quarter; a grain of 0.1, 0.01, 0.0001 separates addresses out to 10, 100, 10,000 | `fisheye.mjs` |
| a reader of grain 0.2, 0.1, 0.01, 0.0001 has its last separable address at 4.93, 9.97, 100, 10,000, and holds everything beyond as one | `fisheye.mjs` |
| with the hold as denominator, four arrivals of the same direction read at radii 1, 2, 0.5 and 10 — so the circle is the locus of arrivals matching the hold, and a laid-down unit buys back the radius | `where.mjs` |
| one freedom spans a quarter turn: 0 at one end, π/4 where the arrival equals the hold, π/2 at the other — so the unit sits at the middle and four quarters close | `where.mjs` |
| at radii 10, 1, 0.1 and 0.01 the span stays π/2 and the count stays 157, while density per unit arc runs 10, 100, 1,000, 10,000 | `where.mjs` |
| a moving hold re-lays the circle every reading; the readings 1.5, 4, 0.5, 5 multiply to 15 = v_last/v_first; and 2 → 60 → 30 gives the same 15 as the longer route | `moving.mjs` |
| one freedom does not close; four quadrants close a turn at 4 × π/2 = 2π; eight octants close a sphere at 8 × π/2 = 4π; and n + 1 signed terms give 2ⁿ⁺¹ regions of n freedoms each | `closure.mjs` |
| the list grows in size and the freedom in density: addresses span 1 at every n while the gap goes 0.1, 0.001, 0.000001; a grain of σ distinguishes 1/σ of them; and the last gap closes faster than the list fills | `density.mjs` |
| extents 3 and 4 against their own size read 0.6 and 0.8 — cos and sin; their squares sum to 1; the point is unmoved at ×1, ×7, ×0.01, ×1000; and their quotient is 1.333333 with the hold gone | `unit.mjs` |
| composition is defined except where one freedom is at 0 and another at ∞ | `compose.mjs` |
| each freedom readable alone, none movable alone | `compose.mjs`, and the earlier work |
| the Cauchy's quartiles are 0.4142, 1.0000, 2.4142 — median at the corner, quarter-points an inverse pair | `examples.mjs` |
| radius, record, arrival-against-hold, grain and height all pass the three tests; a count does not | `examples.mjs` |
| the fisheye is the two-pole log map with poles at ±i, to 2e−16; local slopes of magnification show its logarithmic regime at the corner only, where a two-pole map with a = 1, b = 100 reads −0.51 at a, −1.00 at √(ab) = 10 and −1.49 at b; [0, ∞) maps to π/2, ∞ and ln(b/a) for the fisheye, one pole and two | `lens_family.mjs` |
| a grouping with shared freedoms: loops = memberships − items; routes agree to 3e−16 over 1,000 random groupings; a hold or item change leaves closure 0, a reading off by 0.1 on the loop gives 0.100 and off the loop 0 | `overlap.mjs` |
| three shared items over six give three loops: single-group readings undetected, two-group readings detected but twinned, hold-to-top readings named | `overlap.mjs` |
| a four-reading loop at steps 0.05, 0.2, 0.693 closes on −1, 0 or +1 steps only, rms 0.571, 0.578, 0.580 against 0.577 | `overlap.mjs` |
| strangers read through the fisheye at π/64: direct best at 1 apart (0.038), one level at 6 (0.123), two levels at 10 and 14 (0.728, 1.95); holds 1,000× away lose the whole span | `overlap.mjs` |
| the depth law: d·tanh d = ½, d* = 0.7717; rms at the optimum within 3.1% of 0.863·δ·√S across four steps and five spans, and m* inside the 5% band every time | `depth.mjs` |
| computed by integration over the grid phase, d* = 0.771 at fine grain, shortening to 0.651 at π/16 over S = 96 as a per-reading bias accumulates | `depth_exact.mjs` |
| serial arrival trades data for address: dividing two components cancels the figure (spread 0.0000%), keeping magnitudes keeps it and loses the rate (87.6%), a single list against its last value cancels the gain only | *The Six Things* §8 |
| the reach cancels per arrival, 7e−12 across five figures in the same 100,000 directions; four bodies with identical orbiting centres return periods 194.4, 193.3, 196.8, 195.8 against 200 | *The Cauchy* §11, §14c |
| the Unit Rule's symbol is a fisheye address at atan r, and the gain is stripped in pointing; its record is the nearest-step projection and drifts 1.03× over 56 scenes; r = r₀·exp(σΣℓ) | *The Unit Rule* §7, §15 |
| an open record proves no return and a closed one does not prove return; the sum check is blind to order and the landmark check is not | *The Unit Rule* §17 |
| a Cauchy lap is certified by counting between the home and horizon events and holding at half the count | *The Lap Rule* |
| a circle on an uneven clock departs 4.78 against a correctly walked clover's 0.43 departure — a departure names no cause | *The Cauchy* §13 |
| a freedom carries 1 + s² addresses per unit of turn — 1, 2, 101, 10,001 at addresses 0, 1, 10, 100 — on an extent of π/2 | `hangers.mjs` §G |
| N hangers of π/(2N): at N = 100, hanger 0 covers addresses 0–0.0157, hanger 49 ends at the corner, hanger 99 runs from 63.66 to ∞ | `hangers.mjs` §B |
| hanger k encloses k/N of the Cauchy, to 2e−16 at N = 100 and 10⁶; counting a million arrivals finds the edges — 0.1583, 0.9964, 6.3085 against 0.1584, 1, 6.3138 | `hangers.mjs` §C, §D |
| the home hanger in address matches its turn to second order — 0.0157093 against 0.0157080 at N = 100, equal to seven figures from 10⁶ | `hangers.mjs` §E |
| N = 6 gives hangers 0–0.268, 0.268–0.577, 0.577–1, 1–1.732, 1.732–3.732, 3.732–∞ | `hangers.mjs` §A |
| the last hanger begins at 3.73, 63.66, 6.37e5 and 6.37e13 for N = 6, 100, 10⁶, 10¹⁴ — about 2N/π | `hangers.mjs` §F |
| in serial one freedom suffices and a second cannot be reached: every arrival has a distinct address in [0, ∞); a partition of [0, ∞) relabels into one; the horizon needs v/h = ∞ and home needs v = 0, after which the next reading divides by zero | §5.17, argued |
| the serial lab over 73 library shapes, counterpart at the centroid: largest proportion 1.00–1.11 and nothing on the horizon hanger for circle, star, heart, cardioid, crescent, gear; the rose, whose outline passes through the centroid, 4.1e15 and 4 of 199 on the horizon hanger; a counterpart 0.001 from a circle's outline, 2.03 | `one-freedom-serial-lab.html` |
| the base has a unit and the fibre none — four pairs eight orders apart read identically | `b42.mjs` A–D |
| the landmark candidates are forced to four; home and the horizon are exchanged by the swap | `base-values.mjs` A–E |
| the census of non-freedoms: four counts, two with a completed condition | `census.mjs` 1–7 |
| the swap is invisible to every formed quantity; order is what recovers it | `facing.mjs` A, B |
| the seam is the middle, not the corner; the orientation bit is a freedom, not a count | `seam.mjs` A–D |
| three moves keep the facing and swap crosses; the restriction is absolute | `restricted.mjs` B, C |
| the four facings are Klein and the four signed copies cyclic — not the same four | `four.mjs` A–D |
| order does not recover which term is underneath; the claim imported a walker | `no-walker.mjs` B, C |
| the grain is even in turn, not address; g = 1 is countable without N | `grain-g.mjs` A–D |
| library figures given a second argument (*the path, formally*, flagged (d)): L0a exact at 0.0, L0d 2.8e−14 on the corpus's own outlines rather than on T1–T3; the sixteen-order truncation costs 0.01% on an egg and 8.09% on a star | `library-shapes.mjs` B–E |
| *The Centring* §5c's star-shaped hypothesis excludes 17 of 73 primitives, `ell`, `wedge` and `spiro` at 100% of directions | `library-shapes.mjs` A |
| the completeness test is exact at g = 0.98 and zero-false over 2,800 thinnings; the count carries no g; a regularly thinned set passes, so what is detected is completeness against the reader's own inferred grain | `completeness.mjs` A–F |
| g is the fill rate; g and the step are independent — four situations from two | `g-is-grain.mjs` C, D |
| v, h and g are all fullnesses; h is recoverable from the address; the lens is h² | `fullness.mjs` A–E |
| h² + v² = 1; v² is the swapped reading's lens; the swap needs sameness of kind | `both-fullnesses.mjs` A–E |
| six candidate tie-breakers for v-on-top, none of them forcing | `always.mjs` A–D |
| the relation's own fullness pair R = 2vh, D = v²−h², R²+D²=1, at double the turn | `relation-fullness.mjs` A–E |
| the recursion: level k at 2ᵏu, the corner folding to the horizon, the radix without tiling | `recursion.mjs` A–E |
| the binary path is one lap bit per level; the leaf index is the lap record | `lap-depth.mjs` A–E |
| the corner as a peak, climbable by rescale from any start in under 200 steps | `the-peak.mjs` A–E |
| the fullness audit; amplitudes vs measures; why the constraint is squared | `fullness-audit.mjs` A–E |
| the four corners of the turn collapse to one fullness pair | `four-fulls.mjs` C, D |
| R is scale-free from raw magnitudes; the climb is serial but is a calibration | `peak-use.mjs` A–E |
| the corner is the measure split's entropy maximum; R is the reader's version | `represented.mjs` A–E |
| the scaffold audit: the magnitude is dismantled, the presence is not | `scaffold.mjs` A–D |
