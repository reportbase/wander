# One Reader

### The Cauchy, the fisheye, rapidity and the array, as one object seen by a bounded reader

*Research paper. Sep 23 2026, with Sep 24 additions. Title provisional. Draft for Tom; unreviewed.*

*Revised 1 October 2026: the paper's text is left as it was, and notes marked* **(1 Oct)** *say where the rulings of 30 September – 1 October (R124–R152 of* Reader Geometry as Addressing*) change how it reads. Its results stand; its organising axis (a reader that divides, with N unknown, and "the reader's density") is replaced by the situations, set by what is known of the two breadths.*

> **(1 Oct) How to read this paper now.**
> - **The situations** (R137, R146, R151, R152). (1) The circle: both breadths known and equal; the view from nowhere. (2) Every other shape: breadths known, varying with direction; also a view from nowhere. (3) The fisheye: h's breadth known (h is the known side by definition), v's not, so v is had only as a count of h's; the only view from somewhere, and the only situation with a reader in it, serial or parallel. (4) Neither known: impossible. (5) v's breadth known approximately. The list is not exhaustive.
> - **The reader of this paper** (a bounded reader that holds h and v and divides) is the serial reader of situation 3. Home, the corner and the horizon belong to situation 3 only; situations 1 and 2 have none of them, and no division (R131, R139).
> - **The corner and the two sides** (R149–R150). The corner is known in situation 3, where v reaches one h. The front side, home to the corner, is swept from home in plain proportion (two known ends) and is the **working horizon**; the corner is its edge. The back side, past the corner, is counted by doublings. The parallel reader keeps v on the front side only (R152).
> - **Arctan** is an index into the turn, a shortcut, not the sweep (R148). Where this paper uses θ = arctan s, (2/π)·arctan or tan(arctan s + arctan t), read them as the shortcut for where a sweep would land.
> - **The reader is not the unit circle**; the uniform unit circle is the view from nowhere (R127).
> - **Names now in use.** "The view from everywhere" → **the view from nowhere**; "inside" and "outside" readers → **serial** and **parallel**; "the fulcrum" → **the corner**; "density" is dropped as a framework word (the Cauchy's probability density keeps its name). Quotes keep their wording.

---

## What this paper does

The ideas collected here are old, and most of them are well known in their own fields:
- the Cauchy distribution, and the fact that no other family is closed under the real Möbius maps;
- fisheye views, and the hyperbolic browser;
- rapidity, hyperbolic velocity space, the Thomas–Wigner rotation, and the way a boost acts on the sky;
- hyperbolic motion, and the horizon of a uniformly accelerated observer;
- consistent hashing, list labeling and floating point;
- the occluding contour, the intrinsic equation of a curve and the turning tangent.

At the level of pure mathematics most of them already share a home. One group, **PSL(2,ℝ)**, the orientation-preserving
real Möbius maps of the projective line, is at once the group whose action preserves the Cauchy family, the group of
motions of the hyperbolic plane, and the proper orthochronous Lorentz group of 2+1 dimensions. A mathematician would say "it is all PSL(2,ℝ)", and would be right.

What this paper adds is the **reader**. Every account below starts from the group, or from a sample in hand, or from the
whole object seen at once. None of them starts from a bounded reader:
- one that holds two magnitudes, **h** and **v**, and divides;
- that has a **fixed fidelity ε**;
- that does not know, and does not need, **N**, the size of what it reads.

Starting from that reader, the dots connect in a particular way, and some consequences appear that the group-first
accounts do not state: what fixed fidelity does, how an array, a ring and a shape differ, and why one small instrument, the
dial, can read all of them.

**How claims are marked.** Every claim carries one of four marks.
- **[cited]**: established elsewhere; the reference is given.
- **[corpus]**: established in an earlier paper of this series, by an executed check; the paper and script are named.
- **[new]**: checked on Sep 22–24 for the sessions behind this paper or for this paper itself, by a script in the
  outputs folder; predictions were registered before each run.
- **[reading]**: an interpretation, not a check.

The corpus papers are listed at the end with the external references. Several of them (*Browsing the Fisheye*, *SR
through the Fisheye*, *The Two Settings*, `velocity-space.mjs`, `field.html`) are not in this outputs folder; their
figures are quoted from the corpus's own records and can be checked only against those papers.

**A note on c.** In this paper c is the speed of light. The unit of a growing array, written c in the session record, is
written **u** here.

**Added Sep 24** (a consolidation session; the record is `refresh-sep22-23.md`, "3D: clues, not conclusions"): §1.6
(world, projection, reader: breadth is the world's, density the reader's, and the view from everywhere is just
breadth); notes in §1.2 and §2.2 (the circle demoted; the even turn made by the projection); §3.1 (the inside view is
the two-dimensional Cauchy, and a naming snag); §5.2 (the view from everywhere redefined); §5.4 (readers need
horizons); §5.5 (3D, clues only); density in §6.1 and §6.3; new open items and appendix entries. Later on Sep 24:
**§1.7, v and h and the names they go by**; **§6.4, the reader's density is the Cauchy** (the density accounting collapsed to one law, its parameters, a count and
the reader's limits; ε as the pixel; the Cauchy computed with N unknown, by the corner rule).

**Rulings, Sep 24 afternoon** (Tom): **the order is v/h** (h underneath, so the horizon is at h = 0); **readers don't
build arches; building is the view from everywhere**; **depth is z**; the reader's limits are **chosen**; **one facing
per freedom**. Later: **breadth means extent, not quantity**. Also agreed: dividing is what removes the scale, and choosing what goes underneath is what gives a reader
its horizon, so readers divide.

---

## 0. The map

> **(1 Oct)** The map joins known ideas through a reader that divides with N unknown. Read that reader as situation 3's serial reader: what the joining needs is v's breadth unknown, not N unknown (R146). The rows stand as written.

| the idea | where it is known | what the reader makes of it | § |
|---|---|---|---|
| a uniform turn read through tan is Cauchy | probability, standard [cited] | the reader's reading of an evenly met turn | 2 |
| the Cauchy is the only family the real Möbius maps cannot leave | Knight 1976; Letac 1977; McCullagh 1996 [cited] | the reader's swap and compose are Möbius maps (its doubling is not, but still keeps Cauchy laws Cauchy), so the Cauchy is the only non-degenerate family its moves cannot leave | 2 |
| the Cauchy has no mean | Poisson 1824, via Stigler 1974 [cited] | an address is not supposed to have an average | 2 |
| fisheye views: magnify the focus, compress the edges | Furnas 1986; Sarkar & Brown 1992 [cited] | the reader's lens, tan from the focus | 3 |
| the hyperbolic browser: a tree on the hyperbolic plane, drawn in the Poincaré disk; refocus by translation | Lamping, Rao & Pirolli 1995 [cited] | the space of readers is the hyperbolic plane | 3 |
| SR velocity space is hyperbolic; rapidity adds | Varićak 1910; Robb 1911; Borel 1913 [cited] | the space of readers is velocity space | 4 |
| boosts act conformally on the sky | Penrose 1959; Terrell 1959 [cited] | in the sky's reading, a boost is a change of the reader's radius | 4 |
| the Thomas–Wigner rotation is a velocity-space triangle's area | Thomas 1926; Wigner 1939; Aravind 1997 [cited] | a pan between zoom levels costs radius and turns the rim | 4 |
| β² + 1/γ² = 1 | SR, elementary | the hold, v² + h² = 1, with v = β and h = 1/γ | 4 |
| hyperbolic motion; the accelerated observer's horizon | Born 1909; Rindler 1966 [cited] | an array growing at a steady rate | 4 |
| the Breit–Wigner (Lorentzian) line | Breit & Wigner 1936 [cited] | the energy as an address into a uniformly swept phase | 4 |
| RP¹ is a circle and S¹ double-covers it | topology, standard [cited] | a ring (two sweeps) against a shape (four sweeps) | 5 |
| the tangent of a simple closed curve turns through 2π | Hopf 1935 [cited] | closure as four sweeps of the bar | 5 |
| the occluding contour; foreshortening gives orientation | Koenderink 1984; Gårding 1993 [cited] | the outside reader's horizon and its depth | 5 |
| a fixed label space forces relabeling | Itai, Konheim & Rodeh 1981; Dietz 1982 [cited] | the reader's budget of about 1/ε distinct addresses | 6 |
| floating point: exponent and significand | Goldberg 1991; IEEE 754 [cited] | re-uniting a growing array | 6 |
| consistent hashing: growth moves few keys | Karger et al. 1997 [cited] | absolute addresses on the freedom | 7 |
| lazy evaluation | Henderson & Morris 1976 [cited] | a stone made on arrival | 7 |

The rest of the paper walks this table from the top, from the continuous observer outwards.

---

## 1. The continuous observer

### 1.1 Two magnitudes that arrive together

Start with one push, felt as two parts: **v**, the part going up, and **h**, the part going across. They arrive
together and neither is privileged. Double the push and nothing about its direction changes. That scale-freedom is the
whole starting point: the reader keeps the **relation** of v to h and discards their common size.

Held against its own size, the pair lies on the **hold**:

> **v² + h² = 1.**

From here on v and h are plain magnitudes; the push was only a way in.

### 1.2 The reading, and its three landmarks

> **(1 Oct)** The three landmarks belong to situation 3 only (R137, R146); the circle and every other known shape have none. R88 ruled the count: three, of two kinds (the corner; home and the horizon, a pair the facing exchanges). And R149: the corner is reached, as the edge of the front side, the working horizon; "the horizon" alone stays the far end, never reached (R77). The arctan bridge is the shortcut (R148).

The reader's one number is the **reading**, s = v/h. Three places on it have names [corpus: *The Relation Space*;
*Browsing the Fisheye*]:
- **home**, h = 1, v = 0: s = 0;
- **the corner**, v = h: s = 1 (*The Relation Space*'s **fulcrum**; §1.7);
- **the horizon**, h → 0: s runs off without bound, and is never reached.

⚠ *The Boundary* (§9.3 B52, kill log; §13): "Home, the corner and the horizon are three landmarks on the line" →
"**two.** Home and the horizon are one place exchanged by the facing; the same two magnitudes read as either." It notes
"the corpus says 'home, the corner and the horizon' everywhere", this paper included. Unrevised here.

The reading lives on **the freedom**, the half-line [0, ∞). The angle θ = arctan s lives on **the quarter turn**,
[0, π/2]. arctan and tan are the bridge. The quarter turn is bounded and symmetric; the freedom is unbounded and has
a horizon [corpus: *The Cauchy, Inside and Out*, "What an array is"].

**Which of these a reader holds (Sep 24)** [reading]. A reader holds only the reading on the freedom, with its three
landmarks and its horizon. The quarter turn and the circle are **the builder's drawing** of that space, or **the view
from everywhere's inference** from many readings (§1.6, §3.3): *"semi-circles are for builders, horizons are for
readers"* (Tom, Sep 24). The quarter turn is used below because it is the clearest drawing, not because a reader has
it. The rigorous paper should define in the other order (appendix, item 1).

### 1.3 The sweep, and closure

> **(1 Oct)** The four sweeps of closure are the circle's, situation 1, which has no home and no horizon; the alternation "home, horizon, home, horizon" belongs to the reading of situation 3 laid over it.

The quarter turn has a picture (Tom, Sep 22): **a horizontal bar of 1 sweeping to a vertical bar of 1.** The angle 0
to π/2 is the full set of relations between a horizontal of 1 and a vertical of 1.

**Closure is four sweeps**: a horizontal of 1, to a vertical of 1, to a horizontal of 1, to a vertical of 1, back to a
horizontal of 1. The facing is built into the picture: each vertical is met from the other side of the one before
[corpus: *The Cauchy, Inside and Out* §0.4]. For a plane curve this is the turning-tangent theorem: the tangent of a
simple closed curve turns through exactly 2π [cited: Hopf 1935].

**Facings are rotations between v and h** (Tom, Sep 24: *"facings are rotations between V and H. horizontal to vertical
to horizontal to vertical and back to horizontal for closure"*) [reading]. A facing is one quarter rotation of the bar;
each swaps which of v and h the bar moves away from:

⚠ **Checked against *The Boundary* (Sep 19–22 working log): most of what follows was already tested there, and two of
the five consequences were killed.** *The Boundary* §9.4 B57 found that "the corpus has one of each under one word":
**the quarters** (a quarter turn applied repeatedly) form the cyclic group of order four, while **the facings** (which
term is underneath, a flip) form the Klein group, because "a facing cannot have order 4; it is a choice between two".
The cyclic four "is about **signs** … an **outside** object"; the Klein four has "no plane, no signs, no page". So Tom's
statement here, four quarter turns to closure, describes **the quarters**, and the table below is the quarters' table.
The kill log (B57, B58) then settles two of the consequences listed under it:
- "the facing does the work a sign would do": **killed as worded.** The four quarters need signs; the two facings do
  not, and "rerun … with every magnitude positive … all four [facing configurations] stay distinct" (B57). The sign
  ruling itself is still unmade: "the corpus currently holds both, in different files" (B324–B325);
- "a rotation count tells facing 1 from facing 3": **killed.** Recovering the facing from order "imports a walker, and
  nobody is walking a path" (B33 withdrawn, B58); "u and u + π give identical addresses", and a lap "costs an unbroken
  watch — a completed quantifier a serial reader cannot supply" (B75).

What survives: every other quarter reads as the swap, "measuring the turn from the other end **is** the swap" (B69), and
the facing is "a selection among freedoms", not a count (B55).

| facing | the bar | v and h | the reading v/h |
|---|---|---|---|
| 1 | horizontal → vertical | h falls to 0, v rises to 1 | 0 → ∞ |
| 2 | vertical → horizontal | v falls to 0, h rises to 1 | ∞ → 0 (h/v runs 0 → ∞) |
| 3 | horizontal → vertical | as facing 1 | 0 → ∞ |
| 4 | vertical → horizontal | as facing 2 | ∞ → 0 |

- **As magnitudes, facings 1 and 3 are identical, and so are 2 and 4.** What tells them apart is the count of rotations.
  So the facing does the work a sign would do: signed v and h mark the four quarters with ±; magnitudes with facings mark
  the same four with a rotation count. This bears on the open **sign** ruling: a third answer is magnitudes, with the
  facing carrying what the sign would have carried. Unruled.
- **Every other facing is the swap.** Facing 2 is facing 1 read from the other seat, the reading running as h/v. v/h and
  h/v are consecutive facings, not rival readings. This bears on the open **order** ruling. Unruled.
- **It fits the sorting by sweeps** (§5.1): an array is one facing; a ring two, meeting itself at the seam; a shape four,
  closed.
- **It fits the two readers** (§6.4): one rotation swaps, for the outside reader, what it sees across its view and what
  lies in its depth; for the inside reader, v/h and h/v. Both meet a facing as a swap of the two parts' roles.
- **Ruled, Sep 24: one facing per freedom.** A freedom is one relation read one way, v over h; its facing is that
  choice of what goes underneath, and it does not change along the freedom. The four quarters are the view from
  everywhere's drawing of four freedoms joined, not four facings of one.
- **No walker is needed.** A rotation is the bar turning a quarter; this answers Tom's Sep 19 concern that "the facing is
  confusing because no one is actually walking a path."
- **The Relation Space already has it** [corpus: *The Relation Space* §14, §18, §21, §22]: two choices, whose terms are
  used and which way the passage runs, give four passages that exhaust the ways two things can be related; on a page,
  and only there, they are the four quadrants of one turn; each hands its far end to the next, the meetings alternating
  home, horizon, home, horizon; and "V/H is never negative. Fullnesses have no sign." So the magnitudes-with-facings
  answer to the sign ruling is that paper's own position; what remains is whether the corpus keeps it.
- **Where *The Six Things* differs** [corpus: *The Six Things* §4, §13, §15]. It agrees that two traversals "identical in
  every reading" are told apart only by the facing, whose accumulated turn "differs by a full turn" (§4), and that
  "nothing underfoot distinguishes the second traversal from the first; only the facing does" (§13). But there the
  parties exchange seats on the **second out-and-back**, "the other party supplying the terms" (§13), "on the doubled run
  the seats exchange" (§15), not on every other quarter. And it keeps the sign as a declared extension: the anti-fulcrum
  "is equality met in the reversed facing. It requires the signed reading" (§15). So "every other facing is the swap"
  and "the facing replaces the sign" are both in tension with that paper. Unruled.
- **And *Degrees of Freedom* differs again** [corpus: *Degrees of Freedom* §5.2 and its numbers table]. It keeps signs for
  closure ("allow each of the two terms a sign", §5.1) and has the semicircle as "two freedoms joined at their
  horizons", the facing being "a choice between V/H and H/V" (§5.2), which agrees with "every other facing is the swap".
  But its scripts record "the four facings are Klein and the four signed copies cyclic — not the same four"
  (`four.mjs`) and "order does not recover which term is underneath; the claim imported a walker" (`no-walker.mjs`).
  The second cuts against "a rotation count tells facing 1 from facing 3" above. Unruled.
- **And *The Centring*** [corpus: *The Centring* §6]: the ratio v/h covers a half turn; both components against the
  arrival's own size keep the side and cover the whole circle; but "what neither holds is a tally of how many horizons
  it has crossed. So neither knows when it has closed." That too cuts against the rotation count. Unruled.

### 1.4 Two registers

> **(1 Oct)** The angle register, θ = arctan s, is the shortcut, an index into the turn (R148). The log register is the back side's count of doublings (R149).

The reader can hold its reading in two ways [corpus: *The Cauchy, Inside and Out* §2.2; *The Two Settings* §4]:
- **the angle register**, θ = arctan s. Its move is the **compose move**, (s₂ − s₁)/(1 + s₁s₂): the tangent of a
  difference of angles.
- **the log register**, z = ln s. Its move is the **ratio move**, ln(s₂/s₁), which acts on a reading as a dilation, s → ks. The corners one doubling apart (s = 1, 2,
  4, …) are equally spaced here: the **rungs**.

### 1.5 The round trip

> **(1 Oct)** Reading back with arctan and 2/π divides by the whole turn, out to a horizon a situated reader never reaches (R148). The swept form: steps over the steps to the corner on the front side (R149).

Laying an array of N entries evenly on the quarter turn, θ = (π/2)(i/N), and reading back with arctan and then 2/π, is a
round trip whose factors are π/2 and 2/π:

> **π/2 · 2/π = 1.**

π/2 takes a share of the array to a turn; 2/π takes a turn back to a share [corpus: *The Cauchy, Inside and Out* §0.3,
"the everywhere equation"]. 2/π is also the mean of |sin| over a quarter or a half turn, the mean facing of §5
[corpus: same §0.3].

### 1.6 World, projection, reader (Sep 24)

> **(1 Oct)** "Density" is dropped (R124): what makes a situated reader is that v's breadth is unknown (R146), not a density. "The view from everywhere" is now the view from nowhere.

*Tom's framing across the Sep 24 session, stated as rulings; [reading] throughout unless marked.*

> *"Think of reality as just a bunch of arrays. The everywhere knows their N, they have an N. Each array has a length,
> that is its breadth. The density is from the reading … the reader creates the density from their limitations to read
> it."* … *"It would now seem that the everywhere view is just breadth."* … *"It's the projection that removes the scale
> and creates the uniform arrays of address, the world is not uniform."* (Tom, Sep 24)

Three layers, kept apart:

1. **The world** is not uniform. It has magnitudes, the stones, which differ from place to place. What it has as an
   array is its **breadth**: its **extent**, how far its magnitudes reach, and not its quantity (Tom, Sep 24:
   *"breadth means extent, not quantity"*). The quantity is **N**, the count of entries. An index has no unit to change
   (§7); its only unit is one entry.
2. **The projection** removes the scale. Dividing, v/h, cancels every magnitude and leaves an **array of addresses**,
   one per entry, each exactly like the next. It is uniform because the projection took out the only thing that varied.
   This is §7's relation → address → payload, and *Browsing*'s "the circle contains no data, it contains addresses"
   [corpus: *Browsing the Fisheye* §7].
3. **The reader** reads that uniform array through its lens and at its fidelity ε, and so reads it unevenly. That
   unevenness is **density**: how many entries fall in each unit of the reader's frame, the reciprocal of their
   spacing. It is mathematical density (how closely entries pack), not physical density and not topological denseness,
   and it is finite because ε is. More exactly (§6.4): the **shape** of the density is the lens's, and is there even for
   the continuous observer; the **count** comes with the discrete step; ε decides where the reader stops telling
   entries apart.

**Prior statement, and "breadth" settled.** Tom said it first on Sep 21: *"The breadth is the world, the density is
the reader"* [corpus: *Degrees of Freedom* §5.15g, with both invariances measured, and a control reader]. ⚠ There,
**breadth is the world's range of magnitudes** (its extremes), and **N belongs to neither**: "N is not a third kind of
thing beside them — it is the place they meet"; N moves when the reader thins to g = ½. Here, on Sep 24, breadth is
**N itself**, "each array has a length, that is its breadth". **Ruled later on Sep 24: breadth means extent, not
quantity**, which is the Sep 21 sense: breadth is the world's range, and N is the count, "the place they meet". That paper also has "the world has infinite breadth AND infinite density" (§5.15h), which Sep 24's "just breadth"
overrides.

**Density is the reader's, not the world's.** The test: **the world's breadth does not change with the reader (a reader
may see less of it, never more: "the reader understates it", *Degrees of Freedom* §5.15g); density differs from reader
to reader.** One array gives a different profile to each reader (§6.3 lists four): the outside reader crowds toward
the horizon, the inside reader's reading packs at home, its log register peaks at the corner. Anything that changes when
the reader changes is the reader's. No reader's packing is uniform; the one uniform thing a reader can hold is the silent
record of an even traverse, which reports nothing [corpus: *The Unit Rule* §7; *The Cauchy, Inside and Out* §0.4].

**The view from everywhere is just breadth.** It holds every array's full extent and reads with no limitation, so nothing
packs: it has no density at all. (This replaces "infinite breadth and infinite density", §5.2.) What makes a reader a
reader is its density.

**This explains the even turn.** The evenly met turn behind the Cauchy (§2.2) is not the world's. The projection makes
it: the addresses it leaves are uniform, and laid on the turn they are even. **The Cauchy is the projection's uniformity
read through the reader's lens.** The world's non-uniformity never reaches the reader through the address; it stays in
the payload, which only the outside reader, holding the stones, has (§5.4).

**The order of limits, reread** (§6.1). "ε → 0 first, then N → ∞" does not reach an infinite density; it **removes the
reader's density** and leaves everywhere's breadth. Classical: density removed first, then the count grown. The corpus's
readers: density kept while the count grows.

**The density is the Cauchy** (§6.4). The lens is the density: its slope, h² for the inside reader, is the Cauchy, and
the reader's focus and unit are the Cauchy's location and scale. ε is the pixel the reader sees it through.

### 1.7 v and h, and the names they go by (Sep 24)

> **(1 Oct)** Names now in use are listed in the header note. g is now the ratio between the reader and the world on [0, 1] (Sep 30): in situation 2 the ratio of circle to shape; in situation 3 a position between known ends on the front side and a count toward an unknown end past the corner (R150).

*Tom: "a lot of the confusion is the various names we give the items in this list." The full list, with sources, is
`v-and-h.md`. This is its condensed form. The names are the corpus's own, gathered from its papers and records; which
to keep is Tom's to rule.*

| the item | in v and h | names in use across the corpus |
|---|---|---|
| the source | one push, two parts | v and h; V and H (older papers); writer and reader (*The Relation Space* since Sep 1: H reads, V is written); relatee and relator (its earlier drafts) |
| the pair held without its size | v² + h² = 1 | the hold; the census; the unit circle (demoted, §1.2) |
| the passage from home to horizon | the bar of 1 turning | the sweep; the passage; the asymmetric relation space, [0, ∞) or the share chart [0, 1); the quarter turn (its drawing, the symmetric space); the atom (retired) |
| the reader's number | s = v/h | the reading; the address; the ratio; r (*The Unit Rule*); celerity (SR). ⚠ *The Relation Space* uses s for the share v/(v + h) |
| the same, from the other seat | h/v | the swap; the other facing |
| the angle | θ = arctan(v/h) | the turn; the angle register; the blue (the dial); times 2/π, the share |
| the log of the reading | z = ln(v/h) | the log register; the rungs; the ladder; octaves |
| the relation before division | v_A·h_B − v_B·h_A | the disagreement; the relation raw |
| home | h = 1, v = 0 | home, (0, 1), where nothing is written (*The Relation Space*); the keystone (Boyd's arch, §6.1b) |
| the corner | v = h = 1/√2 | the corner (*One Reader*); **the fulcrum** (*The Relation Space* and *The Unit Rule* since Sep 1); the agreement point; the one mark; s = ½ in the share chart; 45° (on the page only) |
| the horizon | h → 0 | the horizon, (1, 0), where nothing is read; the rim and the limb (outside); the leg (*The Serial Cauchy*); the far end |
| the reader that divides | holds v/h | inside; serial; Cauchy; fisheye; the unit rule; the flashlight; pointing |
| the reader that does not | holds v | outside; parallel; arcsine; Chebyshev; reverse fisheye (provisional); the kept frame; counting |
| the reader with no limits | holds v and h with size | the view from everywhere (formerly god's eye); classical; the builder |

**Collisions: one name, two things.**
1. **"Corner."** v = h in *One Reader*. *The Relation Space* and *The Unit Rule* (both since Sep 1) call v = h the
   **fulcrum**, and in *The Unit Rule* "corner" is the register's crossing (arrival = hold).
2. **"Grain."** d = ln(b/a), the register's step (*Degrees of Freedom*; §6.4); and g, the share of hangers placed, which
   Tom proposed calling the grain on Sep 19 (rename outstanding).
3. **"Freedom."** The half-line [0, ∞) the reading lives on (§1.2); "a freedom", the complete set of ways v and h can
   relate (*The Serial Cauchy* §2); "the facing is your freedom" (Sep 19); a degree of freedom (*Degrees of Freedom*).
4. **"Turn."** The quarter turn (the angle's range); and *the turn* as a landmark, a reversal of the magnitudes' direction
   (*The Unit Rule* §7).
5. **"v" and "h" in the dictionaries.** v is β, the speed as a share of c, while Varićak's "v = c·tanh u" (§4.1) is a
   physical velocity; on the freedom, h is the unit (§6.2).
6. **"Pair."** The relational pair (the bar's attitude) and the register pair (the held and arriving slots) are two
   objects, not two readings of one. Conflating them is the corpus's most frequent error (*The Unit Observer*, record).
7. **"Hold."** v² + h² = 1 here; in *The Unit Rule* §4, the held level, the register's stand-in for the reader ("Call
   the level in hand **the hold**, and the sample being read **the arrival**"); in *Degrees of Freedom* §1, **h** itself,
   the denominator. *The Six Things* uses none of these for the census.
8. **"g" and "grain," three ways.** *The Unit Rule* §5: g is the register's step ratio, "the grain is the generator";
   *The Six Things* §16: the grain is "the smallest ratio a reader tells apart", the base of its logarithm; and g, the
   share of hangers placed (Sep 19), which *Degrees of Freedom* calls the **expression** (renamed from the unit radius
   Sep 18).
12. **"Breadth."** ~~The world's range of magnitudes or the array's length N~~ **Ruled (Tom, Sep 24): breadth means
   extent, not quantity.** N is the count.
9. **"Corner," a third sense.** *The Six Things* §14 uses it for the unit square's vertex: "the fulcrum sits on the arc,
   never at a vertex of the box". *The Unit Rule* also stretches it to every rung (§5) and every rule's hold match (§14a).
10. **"Facing."** *The Six Things* §4: the facing is a constituent, the turn as against the extent, accumulated over a
   traversal; §15, "the reversed facing". *One Reader* §1.3 numbers facings 1–4 as quarter rotations. Close, but the
   paper counts passages, not facings. (§6.4's outside table now says "the foreshortening" for h, to avoid a fourth
   sense.)
11. **"r."** *The Unit Rule* uses r for arrival/hold (a ratio, §7 lens) and for x − y in rungs (a log difference, §7
   proof).

**Collisions: one thing, many names.** The reader that divides has seven names and the corner six (the corner, the fulcrum, the agreement point, the one mark, the ratio at one, 45°). Each came from a
different paper, and each is right in its register (Cauchy formal, fisheye visual, semicircle mathematical, Sep 2). What
confuses is using two in one passage without saying they are one thing.

---

## 2. The reader's moves, and the law they force

### 2.1 Three moves: two Möbius maps and a doubling

A reader that holds one reading and divides can do three things to it [corpus: *Why the Cauchy is forced*, demo and
note]:
- **swap the hold**, s → 1/s: read h against v instead of v against h;
- **compose two readings**, s → tan(arctan s + arctan t);
- **read the turn twice over**, s → tan(2 arctan s).

A fourth, the **ratio move** of the log register (§1.4), turns out to matter most; §2.1a shows why.

The first two are real linear-fractional (Möbius) maps of the projective line, s → (as + b)/(cs + d): the swap has
determinant −1 and composing with t is a rotation. Together they sit in PGL(2,ℝ), whose orientation-preserving part
is PSL(2,ℝ).

**The third is not a Möbius map.** tan(2 arctan s) = 2s/(1 − s²) has degree two: it is the double cover of §5.1 run as
a map. The corpus note had filed it with the other two, and that was wrong. It still carries Cauchy laws to Cauchy
laws, with the parameter point m + ig of the upper half-plane moved by the same function: Cauchy(0.3, 2) goes to
Cauchy(−0.073, 0.797), measured −0.074 and 0.796, and two other laws agree to about two decimals [new: `doubling.mjs`,
400 000 samples]. The fact is classical: such maps of Cauchy variates are Cauchy [cited: Pitman & Williams 1967], and
2s/(1 − s²) = −1/(s − 1) − 1/(s + 1) has the form of the maps Letac characterised [cited: Letac 1977]. It is one of
those, not one of the Möbius maps.

### 2.1a Which group the moves generate (Sep 23)

The corpus had set two things to prove: that the reader's moves generate exactly the Möbius group (closure), and that
a richer reader steps outside it (maximality) [corpus: the Cauchy-rigidity note]. Working them out changed the first
and replaced the second [new: `closure.mjs`, C1–C5; predictions registered before the run].

**1. Swap and compose alone are not the Möbius group.** (Compose alone gives the rotations, PSO(2); the swap adds the
reflections, making PO(2).) Every product of swaps and composes maps an evenly met turn to
an evenly met turn: pushed through twenty random words of six moves each, the standard Cauchy came out with its
quartiles within 0.033 of ±1 (C1). They are the circle's own rotations and reflections, PO(2), a compact group: the
rotation setting's. A dilation is not among them: s → 2s moves the quartiles to −1.97 and 2.04.

**2. The missing move is the ratio move, and with it the group is complete.** The log register's move, dividing one
reading by another, acts on a reading as a dilation, s → ks (§1.4). Then:
- the rotation generator and the dilation generator, with their bracket, span all three dimensions of the Lie algebra
  sl(2,ℝ) (C2);
- **every element of SL(2,ℝ) is a compose, a ratio and a compose**: g = R_a · D_k · R_b, the singular value
  decomposition of a 2 × 2 matrix, also called the Cartan or KAK decomposition. Rebuilt over 10 000 random g, the
  worst angular mismatch was 3.5×10⁻¹⁴ (C3);
- every generator is linear-fractional, so nothing outside PGL(2,ℝ) is reached.

So **compose and ratio generate exactly PSL(2,ℝ), and with the swap, exactly PGL(2,ℝ).** That is the closure, proved,
with one amendment: the reader needs *both* its registers.

**3. Maximality, restated: the moves are exactly the maps that keep the cross ratio.** The original question ("a
reader keeping a second value steps outside") was not well posed: a sum with a held reading, s → s + t, is a parabolic
Möbius map and stays inside. The sharp form is classical and elementary:
- every generated move keeps the cross ratio of four readings (worst relative change 1.7×10⁻¹⁴ over 1000 random
  words) (C4);
- conversely, a bijection of the projective line that keeps every cross ratio is a Möbius map: its images of 0, 1
  and ∞ fix a Möbius map g, and g⁻¹ ∘ f keeps cross ratios while fixing 0, 1 and ∞, so it fixes everything, since
  CR(x, 0, 1, ∞) determines x. Rebuilt from three images by the cross ratio alone, random Möbius maps agree everywhere
  else to 7.7×10⁻¹⁴ (C5).

So **a move is one of the reader's if and only if it keeps the cross ratio.** The doubling of §2.1 multiplies a cross
ratio by −0.44, squaring by 2.6 and the logarithm by 3.3, so all three lie outside (C4). This is the corpus's own test,
stated in the embedded VCP library: "a transform that changes it is not one of the reader's moves".

**What it means** [reading]:
- **Each register alone gives only part of the group.** The angle register (compose) gives the rotations, the compact
  circle of the rotation setting. The log register (ratio) gives the dilations, the line of boosts (§4.3). Only the two
  together give the Möbius group. This is *The Two Settings*' fork seen from inside one reader: each setting is one
  register, and the reader holds both.
- **The space of readers is the same split.** A reader is a focus, moved by the angle register, and a zoom, moved by
  the log register: PSL(2,ℝ) modulo its rotations, the hyperbolic plane of §3.3.
- **The pan cost is the decomposition at work.** A pan between two zoom levels costs radius and turns the rim (§3.2),
  because a rotation sandwiched between two dilations is again rotation · dilation · rotation, with a different
  dilation and an extra turn: the Thomas–Wigner rotation of §4.1.
- **Knight's theorem, in its sharp form, uses a piece of each register.** Its hypotheses are an atomless law, a
  location–scale type, and invariance under the inversion s → −1/s [cited: Knight 1976; Phillips 1989 for the
  statement]. The inversion is the quarter-turn compose, from the angle register; the location–scale type is the log
  register's dilations with translations. The whole group is more than the theorem needs. The full fractional-linear
  version is Knight & Meyer's and Dunau & Senateur's [cited]. **Correction (Sep 23):** an earlier line here said the
  two registers' "only invariant family is the whole Cauchy family". That is false as stated: point masses are
  invariant, and the Möbius orbit of any atomless law is a Möbius-closed three-parameter family. The uniqueness holds
  only under Knight's hypotheses, or for a family indexed by the upper half-plane, PSL(2,ℝ) modulo its rotations.

**What remains open.** That a reader "holding h and v and dividing" has exactly these three moves, swap, compose and
ratio, is a modelling statement about the reader, not a theorem. Given those moves, the group they generate is now
proved.

### 2.1b Two octaves (Sep 23)

The doubling of §2.1 and the ratio move by 2 are both called an "octave", and they are different moves on different
registers [new: `twooct.mjs` F1–F6, predictions registered before the run; all held]:

| | **the frequency octave**: angle doubling | **the scale octave**: dilation |
|---|---|---|
| on the reading | s → 2s/(1 − s²) | s → 2s |
| register | angle (the turn read twice over) | log (one rung of the radius) |
| where it lives | Chebyshev's T₂ on the chord; TB's FFT butterfly; the half-angle step | the dial's radius; a Doppler octave (§4.3a) |
| count | 2-to-1: 0.7 has the two preimages 0.3152 and −3.1724 (F1) | 1-to-1 (F1) |
| an evenly met turn | stays evenly met: standard Cauchy quartiles stay at ±1 (F2) | rescaled: quartiles move to ±2 (F2) |
| cross ratio | changed (×−0.4386 on a test quadruple, F3) | kept (×1.0000, F3) |
| a move of §2.1a? | no | yes |

- **On the chord it is Chebyshev's T₂** [cited: the TB corpus; checked, F4]: T₂(x) = 2x² − 1 maps the order-16
  Chebyshev nodes onto the order-8 ones, each hit exactly twice (worst distance 3×10⁻¹⁶). The frequency octave halves
  the sample count; the scale octave keeps it.
- **They agree near home and part at the corner** (F5): D(s)/(2s) = 1/(1 − s²) is 1.0001 at s = 0.01, 1.33 at 0.5 and
  50 at 0.99. The doubling sends the corner to the horizon; the dilation sends it to s = 2. So the frequency octave
  stretches the half-sweep (home to corner) over the whole quarter turn, while the scale octave slides the corner
  outward along the freedom.
- **They do not commute** (F6): D(2s) = 1.875 against 2D(s) = 1.319 at s = 0.3.

[reading] Near home the two octaves are the same small step, which is why one word serves for both; the corner is
where the reader must say which it means. The dial's radius is the scale octave. The spectral methods of §6.1a–c run
on the frequency octave.

### 2.2 The Cauchy, forced

> **(1 Oct)** Two Cauchys should be told apart. In situation 2 a known shape laid on the circle's even turn reads as a Cauchy of scale b, its breadth ratio (R144, R147); in situation 3 the Cauchy is forced, with the scale unknown (R138, R146). The compose move tan(arctan s + arctan t) is written with the shortcut (R148).

Two facts from the literature finish the argument:
- **A uniform turn read through tan is Cauchy.** If Θ is uniform on (−π/2, π/2), tan Θ is standard Cauchy [cited:
  Johnson, Kotz & Balakrishnan 1994, ch. 16]. Geometrically, it is where a uniformly turned needle through the origin
  meets the line x = 1: a pinhole projecting evenly spread directions onto an image line [cited: Cuadras 2002]. The reading of §1.2 lives on one side, [0, ∞), where the same fact gives
  the half-Cauchy; the full Cauchy is the reading with its sign, both sides of the focus, as the lens of §3 has it.
- **The Cauchy family is the only one closed under the real Möbius maps**: its orbit under that group equals its orbit
  under the affine maps, and no other family's does [cited: Knight 1976; Knight & Meyer 1976]. Letac characterises every
  map that carries Cauchy laws to Cauchy laws [cited: Letac 1977]. McCullagh gives the family's parameter as a point of
  the upper half-plane, moved by the same Möbius map as the data, and joins the ordinary and the wrapped Cauchy
  [cited: McCullagh 1996].

So, under Knight's hypotheses (an atomless location–scale type), **the Cauchy is the only type a reader's Möbius moves
cannot leave**, and a turn met evenly lands in it [reading, resting on the two cited facts]. Mendonça and Lundell put
the same uniqueness in measurement terms, for cameras: "Cauchy distributions are characterized as the unique class of
continuous distributions invariant to projective transformations" [cited: Mendonça & Lundell 2025]. The doubling does not break this: it keeps Cauchy laws Cauchy too, by
Pitman and Williams's and Letac's route rather than Knight's. The literature states the rigidity as a fact about a
family under a group. Read here, it is a fact about which law a bounded reader's own moves keep.

**Where the even turn comes from (Sep 24)** [reading]. "A turn met evenly" is not an assumption about the world. The
projection supplies it: dividing removes every magnitude and leaves a uniform array of addresses, which laid on the turn
is even (§1.6). So the Cauchy is the projection's uniformity read through the reader's lens. What remains open is which
sources project to an evenly met array; that is the applicability question, decided stream by stream [corpus: *Degrees
of Freedom*, the traverse; the magnitude-list gates].

### 2.3 The Cauchy as an address

The distribution entered mathematics as a pathology. Poisson noticed in 1824 that its averages do not settle; Cauchy's
name comes from his 1853 papers in a dispute with Bienaymé about fitting methods [cited: Stigler 1974].

Read from the reader's side, the reading s is an **address**: where along the freedom the reader is pointing. It is not
a magnitude [corpus: *Browsing the Fisheye* §12]. Then:
- **"An address is not supposed to have an average."** The mean of 10, 100 and 10 000 Main Street is not an address,
  and nobody calls that a pathology of the street.
- **The infinity belongs to the chart, not to the thing addressed.** The tangent diverges at the horizon; the entries
  near it are ordinary entries at ordinary places.

The missing mean is not explained here by the reader's missing N; it is the distribution's own fact. The two absences
fit together; one does not cause the other [corpus: *The Cauchy, Inside and Out* §0.2].

---

## 3. The lens, and the space of readers

### 3.1 Fisheye views

A fisheye view magnifies near a focus and compresses towards the edges. Furnas defined the degree of interest as
a priori importance minus distance from the focus [cited: Furnas 1986]; Sarkar and Brown gave a distortion function
steep near the focus and flat near the edges [cited: Sarkar & Brown 1992, 1994].

The reader's own lens is the tangent from the focus: an entry at angle θ from the focus is drawn at R·tan θ. In the
camera literature this is the **perspective** model r = f tan θ, one of the standard five alongside stereographic
(r = 2f tan(θ/2)), equidistant, equisolid and orthographic [cited: Kannala & Brandt 2006]. Of those, the stereographic
is the conformal one, the one on which a Möbius map acts as a Möbius map of the image [cited: Schleimer & Segerman
2016]. Two
conversions are kept apart [corpus: *Browsing the Fisheye* §7]:
- **the layout**, index to angle, fixed by the array alone: θ = π(i + ½)/N;
- **the lens**, angle to position, chosen by the reader: p = s·tan(θ − f).

"A lens is orthogonal to the data it observes" [corpus: *Browsing the Fisheye* §7]: it takes an angle and returns a
position, with no opinion about what is there.

**The inside view is the two-dimensional Cauchy** (Sep 24) [new: a check of 200 000 evenly spread directions]. A reader
at the centre of a sphere of evenly spread directions, drawing each at tan θ from its focus, gets the isotropic
two-dimensional Cauchy: the share within tan θ ≤ r is 1 − 1/√(1 + r²), matched to 3×10⁻³. The corner circle, tan θ = 1,
holds **1 − 1/√2** of what is in front of it. From the centre every direction is alike; the bunching at the focus is made
by the reading (§1.6). (That the central projection of a uniform sphere is the isotropic bivariate Cauchy is standard; no reference checked here.)

**A naming snag** [reading]. The corpus's fisheye is the tan lens: evenly met directions bunch at the focus and spread
toward the edge. A camera "fisheye" is the opposite, squeezing the edges to fit a wide view; r = f tan θ is the ordinary
pinhole [cited: Kannala & Brandt 2006]. Furnas's "magnify the focus" is also the reverse picture: it is what content laid
on a line looks like viewed by angle, as on the dial. This paper pairs the tan lens with Furnas above; the rigorous paper
should say which way the word points. (Resolved in §6.4: the camera fisheye is the outside reader's lens, the corpus's is the
inside reader's.)

### 3.2 A reader is a circle

> **(1 Oct)** Here the circle is the lens with its zoom k, ψ = arctan(k·tan(θ − f)), which is svg.html's fisheye. It is not the uniform unit circle: the reader is not the unit circle (R127). The zoom k as one number anticipates situation 5's one unknown scale (R151).

Wrapped back onto a circle, the reader's angle is ψ = arctan(k·tan(θ − f)), with k the **zoom**, the ratio of the
array's radius to the reader's [corpus: the reader-geometry note, Sep 3]. Then [corpus, all measured]:
- **k = 1 is the array itself**; k > 1 spreads the focus (the fisheye); k < 1 spreads the edges (an anti-fisheye).
- **Composition multiplies radii**: ×4 then ×3 is exactly ×12. A fisheye of a fisheye is a fisheye.
- **A pan between zoom levels costs radius**: ×4 then ×3 with a pan of 0.35 rad between them gives ×10.815, not ×12,
  and turns the rim.
- **The cross ratio of four entries is untouched by any of it** (to 10⁻¹⁵).

### 3.3 The space of readers is the hyperbolic plane

A reader is a focus and a zoom: a point of the upper half-plane, moved by PSL(2,ℝ). That is the hyperbolic plane, and
PSL(2,ℝ) is its group of orientation-preserving motions; the swap of §2.1, with determinant −1, acts as a reflection
[cited: Ratcliffe 2019]. The corpus measured it directly:
hyperbolic distance between two readers equals the relative rapidity of §4 to ten decimals [corpus: *SR through the
Fisheye* §13, `velocity-space.mjs` V0–V5].

The hyperbolic browser is this same space used for display. Lamping, Rao and Pirolli lay a tree out on the hyperbolic
plane and draw it in the Poincaré disk; "very remote parts of the hyperbolic plane get miniscule amounts of space near
the edge of the disk", and a change of focus is a translation of the plane [cited: Lamping, Rao & Pirolli 1995]. A
change of the reader's zoom is also a motion of that plane (§4.3).

**Read in full (Sep 23), the hyperbolic browser already has three of this paper's array results**, found by display
engineering rather than from a reader [cited: Lamping, Rao & Pirolli 1995]:
- **the resolution budget**: "the transformation only needs to be computed for nodes whose display size will be at
  least a screen pixel. This yields a constant bound on redisplay computation, no matter how many nodes are in the
  tree." That is §6.3's budget and §7's lazy payload together. In a 600 × 600 window: 1000 nodes drawn, about 50 near
  the focus legible;
- **a layout that never needs N**: the layout is recursive and local, "moving some distance or turning through some
  angle", and "can handle arbitrarily large hierarchies". That is §6.2's freedom layout, for trees;
- **the loop rotation**: "a series of translations forming a closed loop, each preserving the orientation along the
  line of translation, will, in general, cause a rotation", which they cancel so the root keeps its orientation. That
  is the Thomas–Wigner rotation of §4.1 and the pan cost of §3.2, met on a screen and named neither.

The paper names no Möbius map, cross ratio or Cauchy; that link to it is this paper's.

---

## 4. The same group, in special relativity

### 4.1 What is known

- **Velocity space is hyperbolic.** Varićak wrote v = c·tanh u and treated composition of velocities in Lobachevsky's
  geometry [cited: Varićak 1910]. Robb named the parameter **rapidity** [cited: Robb 1911]. Borel worked in hyperbolic
  velocity space and found the rotation left by composing non-collinear boosts [cited: Borel 1913].
- **That rotation is a triangle's area.** It is the Thomas precession of a spinning electron [cited: Thomas 1926], the
  rotation implicit in Wigner's little group [cited: Wigner 1939]; its angle is (minus) the area of the rapidity-space
  triangle formed by two boosts and their resultant [cited: Aravind 1997; also Rhodes & Semon 2004].
- **Boosts act conformally on the sky.** A moving sphere still looks circular, because aberration is a circle-preserving
  map of the celestial sphere [cited: Penrose 1959]; the Lorentz contraction is not seen, and appearance is a rotation
  for small subtended angles [cited: Terrell 1959]. Put in camera terms, "the pixel mapping is given by a fractional
linear transformation" between a boosted and an unboosted snapshot [cited: Weiss, *Physics FAQ*, not peer reviewed]. In 3+1 dimensions the proper orthochronous Lorentz group is PSL(2,ℂ) acting on the
  celestial sphere by Möbius maps [cited: Oblak 2015]; in 2+1 it is SO⁺(2,1) ≅ PSL(2,ℝ) acting on the celestial circle
  [cited: Ratcliffe 2019, for the isometries of the hyperbolic plane and the hyperboloid model].
- **The Doppler factor, celerity and pseudorapidity.** Bondi's k-calculus builds SR on the Doppler factor k [cited:
  Bondi 1964]; the identification k = e^ζ, with ζ the rapidity, is standard. Celerity βγ is discussed alongside rapidity
  as one of several speed measures [cited: Lévy-Leblond 1980]. Pseudorapidity η = −ln tan(θ/2); for massless particles
  it equals the rapidity, which a longitudinal boost shifts by a constant [cited: Navas et al. (PDG) 2024, §49].

### 4.2 The reader's vocabulary is SR's kinematics

The corpus's navigation dial reads its blue needle as the **gudermannian of the rapidity**: tan(blue) = sinh ζ
[corpus: `fisheye-ladder-shape.html`]. In h and v [new: `dialphysics.mjs` D1–D6]:

| the reader | special relativity | check |
|---|---|---|
| v = sin(blue) | β, the speed | D1: equal to 2×10⁻¹⁴ at five rapidities |
| h = cos(blue) | 1/γ, the moving clock's rate | D1 |
| the reading s = v/h | βγ, celerity | D1 |
| **the hold, v² + h² = 1** | **β² + 1/γ² = 1, the definition of γ** | D1 |
| home | rest | |
| the corner, v = h | β = 1/√2, γ = √2, celerity 1 | D2; *sr.md* §1 [corpus] |
| the horizon | light, never reached | *The Two Settings* §3 [corpus] |
| the rungs, s = 1, 2, 4 … (celerity doublings) | β = 0.707, 0.894, 0.970, 0.992 … Far out a celerity doubling is a doubling of the Doppler factor k = √(1 + s²) + s ≈ 2s; the exact Doppler octaves k = 2ⁿ sit at β = 3/5, 15/17, 63/65, 255/257, which the celerity rungs approach | D4; *SR through the Fisheye* C3 [corpus]; the dial's build log: the two coordinates part company at the corner (0.5623 against ln 2) |

**The hold is the Lorentz factor's identity.** That is elementary once written down. The other rows need one more
thing, the parametrisation of the blue by the rapidity (the gudermannian); the hold alone does not give them.

### 4.3 A change of unit is a boost, in the sky's dictionary, not the speed's

Two dictionaries are in play, and they must be kept apart.
- **The speed's** (§4.2): the reading s is the observer's own celerity βγ. A boost does *not* rescale it:
  sinh(ζ − ln k) is not sinh(ζ)/k.
- **The sky's**: the reading s is the observer's view of a direction in the sky. A direction at polar angle θ_sky is
  read as s = cot(θ_sky/2), its half-angle stereographic coordinate, whose logarithm is the pseudorapidity η. A boost of
  Doppler factor k along the axis multiplies that s by k for every direction at once, so η moves by the same ln k
  everywhere [cited: Navas et al. 2024, §49, for massless directions; corpus: *SR through the Fisheye* C1, C4, "a boost
  is a pan in rungs"]. The reader's angle is half the sky's angle.

On the dial, the radius sets the reader's unit, and a change of radius keeps the record and restates only the angle.
Doubling the unit halves every reading, so in the log register **every address moves by the same ln 2** [new: D3]. That
is the same kind of move as a boost **in the sky's dictionary**: a dilation of the projective line, which is a motion of
the hyperbolic plane along one line. D3 checks the two shifts separately (both 0.693147180560 at four places); that
they are one move rests on the group identification, not on D3 [reading].

So re-uniting an array (§6.3), zooming a reader (§3.2) and boosting a sky are one move, read in the sky's dictionary.
Boosting an observer's own speed is not that move.

### 4.3a The dial is an octave browser, and SR is written in octaves

The dial's radius moves through octaves (one rung, one doubling, one bit), and its arch shows five octaves down each
side. SR's additive quantity, rapidity, is an octave count: collinear boosts add rapidities, the Doppler factor
k = e^ζ multiplies, its octaves add [cited: Bondi 1964 for the k-calculus; new: `octave.mjs` O1]. So [new: O2–O10,
predictions registered before the run]:
- **the radius is the sky's octave control**: one rung multiplies every direction's stereographic reading by exactly
  2 (O2);
- **the blue is the speed's, and a hybrid**: celerity doublings are 0.014 of an octave near rest, 0.811 at the
  corner and 1.000 far out; small celerities add like Galilean speeds, large ones add octaves (O3). Galilean
  mechanics is the linear part of the octave browser, and the corner is where it hands over [reading];
- **the arch is one-dimensional velocity space**: gd maps every rapidity onto the arch, keystone rest, corners
  β = ±1/√2, feet light (O8);
- **holding the gold is constant proper acceleration**: the blue's worldline lies on a hyperbola to 4×10⁻¹⁰ (O4);
- **a zoom, a pan and a zoom are two non-collinear boosts**: ×4, pan 0.35 rad, ×3 gives ×10.8151, an octave deficit
  of 0.150 and the Wigner angle 17.867° (O5);
- **no octave is preferred**: a boosted isotropic sky is still a Cauchy, only its scale changed (O6);
- **far out, each octave halves the moving clock's rate** (O9);
- **a reader of fidelity ε runs out of octaves at about log₂(2/ε)**, the same count reading the sky (O7) or its own
  speed (O10). Light is infinitely many octaves away; a fixed-fidelity reader's last readable octave is finite
  [reading: a statement about reading, not about physics].

### 4.4 One sign

The compose move, (s₂ − s₁)/(1 + s₁s₂), is the tangent of a difference: the rotation's composition. Velocity addition,
(β₁ + β₂)/(1 + β₁β₂), is the hyperbolic tangent of a sum. They differ by one sign: "a rotation and a boost differ by one
sign bit" [corpus: *The Two Settings* §2]. The same split is the classical one between the two geometries a line can
carry, with an absolute off the line or on it [cited: Klein 1871; corpus: *The Two Settings* §4].

### 4.5 A growing array is a uniformly accelerated observer

Hyperbolic motion, constant proper acceleration a, has celerity growing linearly in coordinate time: βγ = a·t (in units
with c = 1) [cited: Born 1909, who named it]. The uniformly accelerated observer approaches the speed of light without
reaching it, and has an event horizon: a null surface its worldline approaches asymptotically, beyond which lie events
it can never receive signals from [cited: Rindler 1966].

Now lay an array growing at r entries per unit time on the freedom with unit u: entry i at reading i/u (§6.2). Its
frontier sits at reading n/u = (r/u)·t. **Read as celerity, that is hyperbolic motion, with proper acceleration
a = r/u** [new: `dialphysics.mjs` D7, equal to 3×10⁻¹² in celerity and rapidity against the integrated equation of
motion].
- The frontier's rapidity, asinh(n/u), is a times its own proper time. So **far out (n ≫ u), each doubling of the
  array costs the same ln 2/a of the frontier's clock**: 1.382562, 1.386257, 1.386294, 1.386294 at a = ½ from
  n/u = 10, 100, 1000, 10⁴, against ln 2/a = 1.386294 [new: D7]. Near the corner it costs less (0.562/a from n/u = 1
  to 2). Far out, the array's rungs are equal steps of proper time.
- **The end the array never reaches corresponds to the speed of light the observer never reaches** [reading]. It is
  not the observer's event horizon, which is a different object.

The identity itself is textbook; what is new is reading a growing array as the observer.

### 4.6 The Breit–Wigner line as an address

A resonance's line shape is Lorentzian, that is Cauchy [cited: Breit & Wigner 1936]. With tan δ = (Γ/2)/(E_R − E), a
uniformly swept phase δ puts the energies on a Cauchy of scale Γ/2: the energy is the address into the phase, E_R its
focus and Γ/2 its scale [corpus: *SR through the Fisheye* §12, C9, quartiles to six places]. The tempting next step,
that the width composes as the reader's radius does, failed: convolved lines add their half-widths, as Cauchy sums do,
where radii would multiply [corpus: C10, killed].

### 4.7 What physics supplies that the reader does not

The reader's kinematics is SR's; three things are not the reader's [corpus: *SR through the Fisheye* §11]:
- **which setting**: the sign of §4.4, rotation or boost;
- **where the horizon sits in world units**: c. The dial's reader chooses its unit; an observer in the world is given
  one;
- **the magnitudes**: mass, energy, interval. They are exactly what a ratio reading cancels, and physics supplies them
  from behind the lens.

Nothing here claims that the world is a dial. The shared object is the geometry of a bounded reading.

---

## 5. Array, ring and shape

### 5.1 Three objects, told apart by sweeps

> **(1 Oct)** The landmark sequences given to rings and shapes put situation 3's landmarks on known objects; known objects are situations 1 and 2, which have none (R137). A shape "read" for its landmarks is a known shape read as if v's breadth were unknown: a simulation of situation 3 (R143).

An array, a ring and a shape can all be read by the same reader. They differ in how many sweeps they take and where the
sweeps join. This table is a reading from the code and the vocabulary, not a measurement [reading; first set out in
*The Cauchy, Inside and Out*, "The dial, read whole"]:

| | sweeps | joined | closes? | facing? | example |
|---|---|---|---|---|---|
| **array** | one, as laid: H → V, from the first entry to the last. A reader standing at a focus inside it looks both ways, two quarter turns joined at home | at home only; each far end is a bound | no | no | the dial, which clamps its record between 0 and N − 1 |
| **ring** | two: H → V → H, a half turn | at home and at the horizon, which is one point: the seam | yes | no | the board browser in `field.html`, which lays item i at −iπ/N and folds every focus mod π |
| **shape** | four: H → V → H → V → H, a whole turn | all the way round | yes | yes | any closed figure |

**A shape is an array, completed** (Tom, Sep 24): *"a shape is just an array with four facings and the complete [set]
of h relative to v."* Nothing new is added to make a shape: it is the same indexed magnitude list, laid over four
facings, which by the Sep 24 ruling (one facing per freedom, §1.3) is four freedoms joined, until it holds every
relation of h to v. That is Tom's Sep 20 ruling on closure said of the object: "when a magnitude list closes, it
represents all possible ways v and h can be represented relative to one another in all possible facings" [corpus:
*Degrees of Freedom* §5.18a]. So the table's three rows are one object at three extents: one facing (the array), two
(the ring), four (the shape).

The board browser's library states the ring's rule in one line: **"The address repeats every half turn, so a direction
and its opposite are one address."** [corpus: `field.html`, embedded VCP]

This is the topology of the projective line. RP¹ is a circle, and the oriented circle S¹ double-covers it: a direction
and its opposite are one point of RP¹ and two of S¹ [cited: Hatcher 2002]. Directional statistics has the same split
as **axial** against **directional** data: "an axis represents an undirected unit vector", handled by doubling the
angle [cited: Mardia & Jupp 2000; the quote from Fernández-Durán & Gregorio-Domínguez 2025]. So [reading]:
- **a ring is RP¹**: it closes in a half turn and has no facing, because it cannot tell a direction from its opposite;
- **a shape needs S¹**: it takes the whole turn, and **facing is exactly telling a direction from its opposite**. A
  shape's two sides are those two.

Tom's rulings fix the array's place (Sep 23): "an array is not a shape, it does not close, it has no facing, it is just
one quarter turn." Read from a focus in its middle, an array and a ring both show two quarter turns; what separates
them is the far ends: bounds for the array, one shared seam for the ring.

**Checked (Sep 23, `ring.mjs`, predictions registered before the run):**

| | ring (laid as the board browser lays it) | shape (an egg) |
|---|---|---|
| one lap turns through | **π** (1.000000 π) | **2π** (2.000000 π) |
| landmarks in one lap | **H C o C**: four, each point met once | **H C o C H C o C**: eight, each point met twice |

- **The shape's lap is the ring's lap run twice.** Read each of the shape's step directions as a point of the
  projective line, forgetting which way it faces, and its landmark sequence becomes exactly H C o C H C o C, the
  ring's twice over. Turning a direction round to its opposite moves no reading on the ring (6.7×10⁻¹⁶).
- **So facing is which of the two passes the reader is on.** The ring cannot tell; the shape can, and that is its two
  sides.
- **Correction:** the prediction written earlier, that the landmark sequence "belongs to shapes only", was too strong.
  A ring has a landmark sequence too, half the shape's; what belongs to shapes is the *repetition*, each landmark met
  twice, which is the facing. The order-blind checksum closes on both, at π and at 2π.

### 5.2 The shape, from the three scenarios

> **(1 Oct)** Both readers are in situation 3, the only situation with a situated reader (R152); the parallel reader keeps v on the front side only, before the corner (R152). The classical account is the view from nowhere, "from no standpoint".

A reader meets a shape in three different scenarios (Tom, Sep 22) [corpus: *The Cauchy, Inside and Out* §1]:
- **the view from everywhere**: the classical view, **just breadth** (Tom, Sep 24): it holds every array's full extent and
  reads with no limitation, so nothing packs and it has no density (§1.6). (Formerly "god's eye", renamed Sep 23 as "the
  view from everywhere, with infinite breadth and infinite density"; the density half was dropped on Sep 24. It is the
  inverse of Nagel's *view from nowhere* [cited: Nagel 1986], the ideal Haraway called "the god trick of seeing
  everything from nowhere" [cited: Haraway 1988]: not from no standpoint, but from every standpoint at once. A reader at
  every position with a fixed fidelity would still meet a horizon: breadth everywhere plus a limitation is still a
  reader.)
- **outside, in parallel**: it holds the outside hemisphere;
- **inside, serially**: it receives the inside hemisphere.

Parallel is not the view from everywhere. Neither real reader knows N, and both meet a horizon: **the same horizon, from its two
sides.** Their verbs differ: "an inside reader points, an outside reader walks" (Tom, Sep 22).

The outside reader's horizon is the **occluding contour**, the rim, where the surface turns edge-on. The contour's
curvature gives the sign of the surface's Gaussian curvature [cited: Koenderink 1984]; contours end only in particular
ways [cited: Koenderink & van Doorn 1982]. Foreshortening gives surface orientation [cited: Gårding 1993;
Aloimonos 1988]. The inside reader's record of the turning is the curve's intrinsic equation, curvature against arc
length [cited: Whewell 1849].

### 5.3 Classical as both sides together

The corpus's central construction is **the stitch** [corpus: *The Cauchy, Inside and Out* §4, `bothsides.mjs`]:
- the outside reader holds positions and gaps, and so depth;
- the inside reader holds directions;
- joined at the horizon they share, with one scale carried across it and fixed by closure, **they rebuild the shape
  without ever using N**: worst error 2.5×10⁻⁷ on a circle and an egg, 6.1×10⁻⁷ on a trefoil, at N = 4000, falling as
  1/N².
- **Its scope is narrow, and the controls show it.** It holds for convex closures with evenly spaced hangers and two
  horizons. With uneven hangers (±30 %) the worst error is 0.54 at every N; on a dented shape, with six horizons, 2.2;
  at fixed ε without the repair of §6.1, the limb loss spoils it [corpus: §4.3 of the same paper, `bothsides.mjs`
  K1–K3]. "The counting premise carries the depth; convexity carries the two."

The nearest prior work rebuilds a convex set from support lines, known directions with measured offsets, and
notes that measured lines "may not be consistent with any set in the plane" [cited: Prince & Willsky 1990]; polygons
are rebuilt from mixed partial features in recent work [cited: Baumann et al. 2026]. The split between a silhouette
reader and a direction-only serial reader, joined at the contour without N, was not found.

That result is measured. "Classical is both sides together" is the corpus's **thesis**, its reading of that result; the
tests show the two sides are enough to give back the classical object, not that the classical account *is* a stitch
[corpus: §0 of the same paper].

The stitch is also a two-group tower: the one scale that crosses the horizon is the ratio of the two readers' holds,
recovered by closure (L ÷ unit = 0.5000, 2.0000, 3.7003 for hold ratios 0.5, 2, 3.7) [corpus: §4.4, `towercheck.mjs`].

### 5.4 Readers need horizons: the arch, the address and the thing (Sep 24)

*Found by trying to draw the stitch; the demos are in the corpus list. [reading], with one measured identity.*

- **Readers require actual horizons** (Tom, Sep 24). An attempt to show both readers on one hemisphere, pairing each
  outside shadow with its inside reading stick by stick, produced the Roman arch: the stick's length is shadow ×
  √(1 + s²), the hold applied once per stick [new: `samehemi.mjs`, an identity], and nothing was left unknown. Tom:
  *"the roman arch does not have inside and outside readers, it is a static situation with pure math."* The pairing was
  **identity**, which is everywhere's; so a picture with no horizon has no readers in it. The claim first drawn from it,
  that the pair "turns the freedom back into the quarter turn", is withdrawn.
- **Two frames, two parties.** *"The scaffolding is needed before the magnitudes can be placed, and the magnitudes can be
  anything … but the roman arch is not a unit circle, so it's not an address to another thing, it's the thing itself."*
  And: *"readers don't build roman arches, they read them."*
  - **The builder's centring** is part of making the thing and is struck once it stands [corpus: *The Centring*]. The
    reader never sees it.
  - **The reader's frame, its address**, is brought to a finished thing and never struck, because it was never part of
    the thing. It is the reading with its horizon, carried with the reader [corpus: *Browsing the Fisheye* §2: "a mark
    the reader carries never moves; a mark laid in the world does"].
- **Outside is the shape; inside is a flashlight** (Tom, Sep 24: *"the outside is just the shape itself, and all of its
  perturbations. The inside points to a spot on it. Like a flashlight."*). The flashlight supplies the address, which
  spot; the shape supplies the payload, where it sits and how far. A round and a lumpy shape look identical through the
  flashlight's fisheye (§3.1) and different to the outside reader. This is the position reader; the **motion reader**,
  reading how the lit surface turns between pointings, would recover the form without the size (§2.1 of *The Cauchy,
  Inside and Out*).
- **A flat page cannot hold two readers apart.** The page is itself the view from everywhere: whatever is drawn on it
  sits side by side and can be paired. Every 2D attempt either stitched the readers by hand or collapsed into the arch.
  The readers came apart only as **two-dimensional images of a three-dimensional object**: the parallel signal as the
  image, the serial signal as a beam through the shape, along which depth lies (Tom's Sep 20 rulings: "the 1d signal is
  where depth comes from"; "3d is consumed as 2d images of 1d slices"). Tom: *"interesting that 3d is needed to show the
  situation cleanly, that is evidence in itself that 3d is just serial + parallel."* That is evidence of fit, partly by
  construction; the independent part is that every 2D version failed.

### 5.5 Three dimensions: clues, not conclusions (Sep 24)

*Tom: "the 3d question is not going to be resolved here, we are just looking for clues and ways to frame it."*

- **Under parallel sight lines, 3D splits exactly into a fan of 2D slices** sharing the sight axis: visibility and
  occlusion stay inside each plane containing it. When the inside reader's focus is on that axis, its slices are the same
  planes. So the 3D stitch is one 2D stitch per slice, and the only per-slice question is coverage [reading; an exact
  statement about orthographic projection].
- **Coverage** [new: `rig3d.mjs`; 36 slices, 800 hangers each; held steps given their true directions, so this tests
  coverage only; one script bug fixed before judging]:

  | shape | inside receives | slices with steps held by neither |
  |---|---|---|
  | tilted ellipsoid, egg | its hemisphere | 0 (rebuild exact to 10⁻¹⁵) |
  | deep, tilted dent | its hemisphere | **7 of 36**: the dent floor hidden behind the rim, recovered only as a chord (sagitta 0.022) |
  | deep, tilted dent | whatever it can see from the centre | 0 |

- **The framing question** this leaves: is "the inside reader receives the inside hemisphere" fundamental, or an artefact
  of convex shapes, where it agrees with "whatever it can see"? Under the second, the claim can fail only on a surface
  hidden from both readers, a pocket behind the rim from outside and behind an overhang from the centre. Untested.

---

## 6. Fixed fidelity, N unknown

### 6.1 The order of limits

> **(1 Oct)** Where this section reads "in terms of density", read "in terms of the spacing of addresses" (R124). The outside reader is the parallel reader.

The classical accounts work, in effect, after the resolution limit has been taken: **fidelity ε → 0 first, then N → ∞**.
That is not a claim about how each result was derived; it is how a continuum treatment looks from a regime where the
order matters [corpus: *The Cauchy, Inside and Out* §0]. The corpus's readers cannot take the limits in that order:
**ε is fixed, and N grows, unknown.** Taken in that order, several things appear that the classical order hides
[corpus, all measured]:
- **The outside reader's rim hides a share that grows with N**, about εN²/(2π²) points. The crowding itself is the
  familiar clustering of Chebyshev points, equispaced points on a circle projected onto a line, with spacing of order
  N⁻² at the ends [cited: Trefethen 2019, ch. 2; its cost in spectral methods: Kosloff & Tal-Ezer 1993]. What the
  searches did not find is the count at fixed ε.
- **The count has a closed form** [new: `rigor.mjs`]. The gap in v between neighbours is about (2π/N)|cos φ|, so a
  point is resolved when |cos φ| ≥ x, with x = εN/(2π). Of the N/2 points on the visible half,

  > **R(N) = (N/π) · arccos(εN/2π)** for εN ≤ 2π, and 0 beyond.

  It matches every measured count to within two points (1120 against 1121.3 at N = 4000, ε = 10⁻³; 11 212 against
  11 213.3 at N = 40 000, ε = 10⁻⁴). It peaks where arccos x = x/√(1 − x²), at x* = 0.6522, that is εN = 4.098, with
  **R_max = 1.1222/ε**. That is the measured cap of 1122 at ε = 10⁻³, and the measured best g·N ≈ 4100, both now
  derived. For small x the loss N/2 − R is εN²/(2π²), the earlier approximation (20.27 against 20.26 at N = 2000,
  ε = 10⁻⁴). **More points eventually
  means less seen**: the count told apart peaks near εN ≈ 4 to 5 (1120 at N = 4000, ε = 10⁻³), falls (1034 at 5000,
  574 at 6000), and is zero by the ceiling εN = 2π (`ceiling.mjs`). Placing only a share g of the hangers helps, but
  not without limit: at the best g the outside reader never told more than 1122 points apart at ε = 10⁻³, at N from
  20 000 to a million (`gceiling.mjs`).
- **Each reader is blind where its lens is slowest**: the outside reader at the horizon; the inside reader, in the log
  register, around the corner (§3.3 of that paper).
- **The pair repairs what each loses alone**: the inside reader counts the outside reader's hidden near-horizon steps
  by the fidelity rule, restoring the count to N exactly and the error to the scoring floor (22 hidden at N = 2000;
  worst error 1.9×10⁻² alone, 2.5×10⁻³ for the pair) (`repair.mjs`).
- **Where the pair runs out** (Sep 23) [new: `fixfid.mjs`–`fixfid3.mjs`; *The Cauchy, Inside and Out* §5.2]. The
  outside reader is blind where h·ds < ε, a band at the horizon. The inside reader is blind where Δ/(vh) < d, a band at
  the corner. The pair loses a hanger only where the two bands overlap:
  - On the circle the overlap first opens at (ε/Δ)√(1 − (ε/Δ)²) = Δ/d. That is about N = 2π/√(εd), at h ≈ √(ε/d),
    between the corner and the horizon. When ε > d/2 it opens at the corner instead, at N = 4π/d.
  - Measured thresholds fall within 1 % of the exact form. Band edges match to three or four decimals.
  - On a general shape the local form holds, with the turn written as κ·ds: the pair's first blind hanger is where
    **h²v/κ = ε/d**, with no N. On the egg this predicts 15 105 against a measured 15 100.
  - Past the outside reader's ceiling, the pair holds **8/d** hangers, at home and at the horizon, whatever N and ε are.
- **Neither checksum finds a balanced loss.** Closure, the order-blind sum, cancels a loss that is equal at both
  horizons; the order-bearing landmark sequence also passes it, even with 81 % of a half lost. The loss is not
  detected; it is inferred, locally (`landmark.mjs`).

**Read in terms of density (Sep 24)** [reading]. Every result in this section is a statement about a reader's density,
not about the world: the world supplies breadth and the count N, and the rim loss, the ceiling, where the pair runs out and the 1/ε budget
are what a reader of fidelity ε makes of it (§1.6). "ε → 0 first" removes that density; the corpus's order keeps it.

### 6.1a The limb crowding is the Chebyshev nodes

The outside reader's samples are evenly spaced hangers seen orthographically, so they are the Chebyshev nodes of the
first kind; the inside reader's are the same hangers read through tan, the Cauchy [corpus: *The Tangent Bridge
Theorem*, Chord Projection Corollary §9]. The two readers are the two classical projections of one evenly spaced set.
The limb count R(N) = (N/π) arccos(εN/2π) counts the Chebyshev nodes still resolvable at ε. Chebyshev nodes meet the
optimal interpolation growth (2/π) ln n [cited: Erdős 1961 for the floor; Trefethen 2019], the same 2/π as the
everywhere equation.

**Fixed fidelity breaks that optimality completely** [new: `chebfix.mjs`, predictions registered before the run]. With
all nodes, the Lebesgue constant is (2/π) ln n + 0.96 (C1). Keep only the resolvable ones and interpolation over the
visible extent fails the moment any end nodes merge: 14 of 250 lost at N = 500, ε = 10⁻³, and the Lebesgue constant is
1.3×10¹⁶ (C2); even within the kept span it stays above 10¹⁴, beyond double precision (C5). Restoring the end nodes
from the other reader returns it to Chebyshev's 4.5 to 5.4 (C4). The crowding that makes Chebyshev nodes near-optimal
at ε → 0 is the first thing a fixed-fidelity reader loses, and without it no global reconstruction of the hemisphere
survives. The pair's repair is necessary, not just helpful.

### 6.1b The inside reader as a spectral method (Sep 23)

*Condensed. The runs, tables and every miss are in the session record (the sections from "Two octaves, the inside
reader's nodes, and a local repair" to "One rule over the whole plane"). Scripts: `inside.mjs`.*

- **The inside reader's nodes are Boyd's rational Chebyshev points** [cited: Boyd 1987; Boyd 2001]. Boyd maps the line
  onto a half turn, y = L cot t, and expands in TB_n(y) = cos(n arccot(y/L)). Checked [new]: his points are exactly
  the Cauchy's midpoint quantiles at scale L, and TB_n(y) = T_n(y/√(y² + L²)), both to 10⁻¹⁴. **The two readers are
  one set of evenly spaced angles, projected two ways**: the chord (x = cos t, v) gives the outside reader's
  Chebyshev nodes; the central projection (y = cot t, the reading s = v/h) gives the inside reader's.
- **Boyd's domain is the Roman arch.** Home is the keystone, the corners are at ±L, the feet are the two horizons.
  They stay distinct (TB_n(±∞) = (±1)ⁿ): an array, not a ring (§5.1).
- **What the nodes are for**: functions on the whole freedom that are smooth through the horizon. One that tends to
  different limits at ±∞ is read to 3×10⁻¹⁵ with 20 nodes; exp(−y²), singular at the horizon, converges far slower.
- **A local repair for the outside reader** [new]. Global interpolation on the resolvable nodes fails at fixed ε
  (§6.1a). Cubic interpolation on the four nearest kept nodes does not: its Lebesgue constant stays below 1.63 at
  every N, against 10¹⁴ to 10¹⁶ globally. All the error is in the lost band and grows smoothly with εN. **Global
  methods lose everything once the limb merges; local methods lose exactly the limb.**

### 6.1c The dial's radius, chosen by the reader (Sep 23)

*Condensed, as above. Scripts: `selfl.mjs`, `poles.mjs`, `parity.mjs`, `decay.mjs`, `sweep.mjs`, `regime.mjs`,
`regimeN.mjs`, `coarse.mjs`, `place.mjs`, `centre.mjs`, `hplace.mjs`, `composite.mjs`, `composite2.mjs`. Predictions were registered before each run;
about a third of them failed, all logged.*

Boyd's L is the dial's radius, the scale octave of §2.1b. Can a reader set it from what it reads?

1. **For an array's values, exactly: put the corners at the quartiles.** For Cauchy data this recovers the scale to
   0.6%, and the entries' angles are then evenly met. Data spread over many decades is evened by no single radius;
   that is the digits' job.
2. **For a function, two things set the best radius** [cited: Boyd 1982 for the formulas; checked here].
   - **The poles.** The best (m, L) pushes the nearest pole furthest from the arch. The predicted convergence rate
     matched to two figures. For two scales the best radius is their geometric mean.
   - **The horizon's parity.** A function that meets the horizon with a slope in the angle (a 1/y tail) defeats the
     cosines, which are all flat at the arch's feet. It needs the sines [cited: arXiv:1703.07441].
3. **One radius cannot find its own best setting.** A feature beyond its outermost node, or between its central ones,
   is invisible to it. A reader that sees nothing (flat samples) thinks it is done.
4. **The sweep can.** Checking each radius against the readings the dial takes at every other octave finds the true
   best in all five test functions. **The dial's octave sweep, which it already does to browse, is also how a
   reader calibrates itself.**
   - **The sweep reads each value against its double for free**, because a node at the next octave sits at exactly
     twice its position. The ratio of 2y(f(y) − f(2y)) from octave to octave names the tail's order: 1 for 1/y,
     ½ for 1/y².
   - **Stop when each side reaches its regime**, where one octave is the last scaled by a power of 2. The cost is
     the features' span in octaves plus about 12. The window slides as N grows; its width does not.
   - **A coarse reader (N = 8) sweeps as well as a fine one** and chooses as well when the data has one octave. It
     costs a third of the readings. With two octaves it drifts by a few-fold.
5. **When no single radius serves, the sweep places several readers.** One reader per peak of the change profile,
   split at valleys, reads widths 1 and 10⁴ to 4×10⁻¹² where the best single radius gave 0.92. Placing by octave
   finds features nested at one centre; placing greedily at the residual's peak finds features side by side. These
   are **the two directions of the plane of readers** (§3.3), centre and radius. One rule over the whole plane failed
   twice. **The composite works** (`composite.mjs`): greedy centres, then two-sided octave clusters at each. It reads
   widths 1 and 100 with two readers at one centre to 3.6×10⁻¹², five orders better than any single-direction rule,
   and finds side-by-side centres to 0.02. A borrowed acceptance test (the Bayesian information criterion, with a
   precision floor) gives side-by-side features exactly two readers, error 2.2×10⁻⁹ (`composite2.mjs`). Left: the
   centre, which a reader with an even number of nodes never samples, so peak-picking locates it only to the nearest
   node; fitting the peak between samples is the standard fix. The session record has the runs.

**Prior art** (checked Sep 23; abstracts only for Boyd 1982 and Tee & Trefethen 2006):

| result | already known |
|---|---|
| the nodes and the map | Boyd 1987; Boyd 2001 |
| the best L from the poles | Boyd 1982 ("simple analytic formulas for choosing the optimum … mapping parameter L") |
| singularities located from samples, the map adapted to them | Tee & Trefethen 2006 (Chebyshev–Padé); Cueto-Felgueroso & Juanes 2009; AAA (Nakatsukasa, Sète & Trefethen 2018) |
| map parameters chosen by minimising error over the samples | Alexandrescu et al. |
| parity at the horizon, hybrid bases | arXiv:1703.07441 |
| the order of a tail from successive ratios | Richardson, Aitken; classical |
| local stability, aliasing, under-resolution; resolution placed adaptively | textbook; multi-domain and adaptive methods |

**Verdict: the methods are known; what is ours is the joining.** Specifically:
- the inside reader is Boyd's method, and Boyd's domain is the arch;
- Boyd's L is the dial's radius;
- the dial's octave sweep is the reader's calibration, with each node read against its double;
- placing readers along the radius and along the centre are the two directions of the plane of readers.

The rigorous paper should cite Boyd 1982, Boyd 1987 and Tee & Trefethen 2006 for items 2–4 and claim only the
reading.

### 6.2 Arrays on the freedom

> **(1 Oct)** "v is the count and h is the unit" is the earliest form of R146: v had only as a count of h's. The axis here, whether N is known, is now whether v's breadth is known. The layout arctan(i/u) is the shortcut (R148).

*Terminology.* What is laid on the quarter turn or the freedom is an **array**: entries with **indexes**. The index is
the address, and the reader's reading is converted to an index (arctan, then 2/π for a known length, or the unit u for
an unknown one). Nothing about the entries themselves enters: any array, whatever it holds, plugs in the same way
(§7). An earlier draft called it a list; the index is the point, so the word is array.

An array of known length goes on the quarter turn by share, θ = (π/2)(i/N): relative addresses, no horizon. An array whose
length is unknown cannot be laid by share. It goes on the freedom instead, one entry per step of a unit u: reading i/u,
angle arctan(i/u) [corpus: *The Cauchy, Inside and Out*, "Static and dynamic arrays"]. Read in h and v, **v is the
count and h is the unit**, and every landmark carries over: home is the first entry, the corner is entry u, the horizon
is the end not yet arrived. Its addresses are absolute: entry 250 keeps its angle as the array grows from 500 to 2000,
while the share layout's angle for it halves each time (`dynarray.mjs`).

With n entries in, the part of the quarter turn behind the frontier is arctan(n/u) and the part ahead is arctan(u/n):
**arrived and unarrived are a ratio and its swap**, adding to π/2 (`freedom.mjs`, to 2×10⁻¹⁶).

**The rule** (Tom, Sep 24): **if the magnitude list has a known length, the semicircle is appropriate; if it has an
unknown length, the freedom is appropriate.** In h and v:
- **known length: the semicircle.** Each entry takes a share of the turn, θ = (π/2)(i/N); both ends are contained,
  nothing runs off, no horizon; addresses are relative.
- **unknown length: the freedom.** Each entry takes one step of a unit, v/h = i/u; home is contained, the far end never
  arrives, so there is a horizon; addresses are absolute.

"Length" here is the count N, not the breadth (breadth is extent, §1.6). The rule is Tom's Sep 21 line said as a
choice: *"A freedom is mathematical, it has an infinity, it is asymmetric, it is projective, N is unknown. Quarter turns
are symmetric, have no infinity, are angular, can be counted, N is known."* It fits three Sep 24 rulings: a reader never
knows N (Sep 22), so a reader is on the freedom, and knowing the length is the builder's or the view from everywhere's
("semicircles are for builders, horizons are for readers"); readers divide, and dividing with h underneath is what
makes the freedom's horizon; and the magnitude list plugs into the geometry, **its length deciding which geometry it
plugs into**. Two cases sit between: the corner rule (§6.4), by which a reader on the freedom forecasts a length and
closure confirms it; and the heartbeat's [0, ~N), "N kind of known", where the semicircle is approximately right and the
corner can be seen coming.

### 6.3 The resolution budget

> **(1 Oct)** Re-uniting by doubling u, every address moving by the same ln 2, anticipates R147: assuming v's breadth slides the whole reading by whole rungs, and situation 5 knows that offset within bounds.

At fixed ε a reader tells apart only a bounded number of things, whatever the array's length [corpus, all measured,
`finished.mjs`, `window.mjs`]:
- **The count is lost first.** Reading n from the frontier's angle carries a relative error of about εn/u; the reader
  cannot name any count beyond about u/ε, and a growing array then looks finished.
- **Re-uniting keeps the count.** Doubling u whenever n passes 4u moves every address in the log register by the same
  ln 2 and holds the frontier between arctan 2 and arctan 4. The count is then held as **u₀ · 2ᵏ · tan θ**: an exponent
  k and a mantissa, to a fixed relative error for ever (worst 2.12×10⁻³ at ε = 10⁻³ out to 5×10⁶, against a predicted
  2.13×10⁻³). That is floating point: sign, exponent, significand, with roughly constant relative precision [cited:
  Goldberg 1991; IEEE 754-2019].
- **About 1/ε distinct things, whatever the layout; the layout only chooses which.** Fixed addresses keep the oldest
  entries; re-uniting keeps the count; addressing by age keeps the newest, at the price of addresses that move on every
  arrival. The fixed budget is the list-labeling problem's: a label space of fixed size holds a bounded number of items
  before relabeling is forced [cited: Itai, Konheim & Rodeh 1981; Dietz 1982].
- **A fisheye window goes blind at its focus first.** In a 1000-pixel window at 1-pixel fidelity, an array laid by share
  merges first where the lens is slowest on screen, the focus, from n ≈ πR/ε (942 at R = 300), and shows nothing
  distinct past about 3600. The peak never exceeds the window's own W/ε, and the stronger the fisheye the lower it is
  (254 at R = 50, 973 at R = 2000). With a fixed angle per entry, the window never sees the array's length (393 resolved
  at n = 600, 6000 and 600 000).

"The address never overflows; the resolution does" [corpus: *The Cauchy, Inside and Out* §3.2].

**One array, four densities** (Sep 24) [reading, from the lenses of *The Cauchy, Inside and Out* §2.2]. Tom: *"density
varies, it's not dense at home, and very dense at the horizon."* That holds for the outside reader, and not for every
reader:

| the reader, in its frame | at home | at the corner | at the horizon |
|---|---|---|---|
| outside, positions across its view (gap = h per step) | sparse | | **dense**: crowds to nothing |
| an array on the freedom seen by angle (the dial) | sparse | | **dense**: spacing ≈ u/i² |
| inside, its reading s = v/h | **dense** | | sparse: spreads without bound |
| inside, its log register z = ln(v/h) | sparse | **densest** | sparse |

The array has not changed; only the reader has. If density were the world's, the readers would agree. Each goes blind
where it is densest (§3.3 of *The Cauchy, Inside and Out*). The four rows are one law and its twin: the two inside rows
are the Cauchy in two coordinates, the dial's is the Cauchy read backwards, and the outside row is the same turn seen
side-on (§6.4).

### 6.4 The reader's density is the Cauchy (Sep 24)

> **(1 Oct)** Read the title as "the serial reader's spacing is the Cauchy" (R124, R45). The corner rule below places the front side with arctan and goes past the corner by the swap. R149 places the front side in plain proportion, n/C, from home to the corner, and counts the back side by doublings. The two agree if the back side's g is read from the swapped seat, h/v, halving at each doubling (v-and-h item 365, proposed, unruled).

*Built from the working document `reader-densities.md` (ten sources in eight kinds) and the session's discussion,
which collapsed it. Tom: "is density a complicated situation, or can we mostly capture that concept with Cauchy, and the
other densities are of secondary importance?" Then: "so Cauchy is universal, any bounded reader is subject to its math;
epsilon is specific to the reader." This section records the answer, with one refinement to the second remark.*

**From the continuous observer.** The continuous observer meets every relation of h and v once and in order, with no
gaps, so it has nothing to count. It still has a lens, and the lens has a shape. What the discrete observer adds is the
count: N addresses, a step Δ of turn apart. Its fidelity ε then decides where it can no longer tell neighbours apart.
Three things, kept apart below: **shape** (the lens), **count** (the step), **limit** (ε).

**The lens is the density** [reading; the slopes checked in `densities.mjs` D1–D3]. A lens lays the evenly met turn out
in the reader's frame. The density asks how much turn lands in each unit of that frame, which is the lens's slope. The
density is the lens differentiated; the lens is the density added up:

| the lens (how the frame is laid) | its slope, the density | where it packs |
|---|---|---|
| outside, holding v | 1/h | crowds at the horizon |
| inside, the reading s = v/h | h² | packs at home |
| inside, the log register z = ln(v/h) | vh (= ½ sech z) | peaks at the corner |

Nothing is added to get the middle column. And backwards: h² added up from home gives the turn, arctan s, which scaled by
2/π is the Cauchy's cumulative. **The lens tan, the address arctan s (§2.3) and the Cauchy are one object.** The Cauchy
curve is how steep the lens is at each point.

**What the Cauchy absorbs** [reading, from sources already cited]. Of the ten sources in the working document, the ones
that change *where* the packing is heavy all turn out to be the Cauchy or its parameters:
- **the inside lens**, h², is the Cauchy;
- **the log register**, vh, is the same law with ln(v/h) as the coordinate (the hyperbolic secant form); its peak at the
  corner is the Cauchy seen on a log scale;
- **focus and unit** are the Cauchy's location and scale. The reader's compose and ratio moves are Möbius maps (§2.1a),
  and the Cauchy is the family those maps cannot leave [cited: Knight 1976; McCullagh 1996]: focusing and zooming move a
  reader to another Cauchy, never out of the family. They are where the reader stands in the space of readers (§3.3);
- **dimension**: in an image the central lens packs as h³ (the two-dimensional Cauchy, §3.1), in a 3D view as h⁴; in n
  dimensions h^(n+1) (`densities.mjs` D5, `densities2.mjs`). It is still the Cauchy, in more directions at once.

**The one companion.** The outside lens, 1/h, is the same evenly met turn projected side-on instead of centrally: the
Chebyshev (arcsine) crowding of §6.1a. It is the Cauchy's twin, not a Cauchy. Unlike the central lens it does not change
with dimension: seen side-on an even circle, sphere or 3-sphere packs as 1/h per unit length, area or volume
(`densities2.mjs`, flat to sampling noise), because a patch of surface is foreshortened by its facing h in one direction
only.

**Secondary: count and limits.** The other sources are not density shapes.
- **Count**: the step Δ, the share g of entries evaluated, and a steady clock multiply the packing by a number. They say
  how much, not where. A steady clock is exactly g: a whole-number stride gave the evenly thinned count (1121 = 1121 at
  every N); a fractional stride was within 3 % of 1/stride, always slightly below [new: `clockg.mjs`].
- **Limits**: fidelity ε, the grain d, reach S, noise, and an unsteady clock do not change the packing. They decide
  where the reader stops telling entries apart. They are §6.1 and §6.3's budget.
- **Layout** is the condition for either lens to appear at all: an even turn gives the Cauchy; an even reading (one entry
  per unit, §6.2) gives the dial's u/h² per radian, the Cauchy read backwards.

So: **a reader's density is the Cauchy, with its focus as location and its unit as scale, in however many dimensions it
takes in at once, read from an evenly met turn. The outside reader's rim crowding is the same turn seen side-on.** The ten
sources were three kinds of thing listed together: the Cauchy's own parameters, a scale factor, and the reader's limits.

**Universal, in a stated scope** [reading]. Any reader that holds v and h and divides has Möbius maps for moves, and the
Cauchy is the only law those moves cannot break. So every such reader that meets an even turn is subject to the Cauchy,
whatever its fidelity, focus or unit. Two limits on "every":
- it must **divide**: a reader holding v alone gets the side-on twin;
- the turn must be **evenly met**: by a steady clock, or by counting on the turn (*The Serial Cauchy* §6a). Laid by a
  unit, the same reader gets the dial.

*The Serial Cauchy* keeps two Cauchys apart, and this section is about the second: the **world's** (the arriving pairs
have no preferred direction, a premise the reader can confirm as a law but not check as a symmetry, §4 and §8.1 there),
and the **observer's** (a counter with a constant grain produces it whatever the world does: "the fisheye is the
observer's signature, not the world's property", §6a there). That is §1.6's "density is the reader's", reached from the
other side on Sep 20. ⚠ **Killed in *The Boundary*** (kill log, B300): "The Cauchy is the observer's
signature" → "it is there before the reader chooses anything. Fixed by a breadth and one number saying where the facing
is; g then decides how many places to put on a lens already shaped." The same verdict as *Degrees of Freedom* §5.15n
(above): the kernel is the setup's, fixed by where the reader faces from.

**ε is the pixel, not a shift** [reading; the losses measured in §6.1]. Tom's second remark was that ε, specific to the
reader, moves the density slightly from the Cauchy. Refined: ε does not change the shape. The arrivals still pack as the
Cauchy. ε is the size of the reader's pixel: where the Cauchy packs entries closer than ε, they merge. The reader sees
the Cauchy drawn coarse, and at the pixel edges the counts are still exactly Cauchy. How coarse is set by **εN**, fidelity
against the count, not by ε alone:
- **εN small**: slight. The outside reader loses about εN/π² of its visible half, all at the rim (§6.1);
- **εN near 1 or more**: large. The count told apart peaks and falls, and past εN = 2π the outside reader resolves
  nothing (§6.1).

**Noise is what bends it** [new: `noise.mjs`, ε = 10⁻³, predictions registered]. Each received position jittered by a
Gaussian of size σ:
- **false resolution**: in the rim band, where every true gap is below ε and the noise-free reader is blind, noise
  produces apparent gaps of at least ε, 24 to 266 of them depending on N and σ. **A threshold can only remove resolution;
  noise also invents it**;
- **real resolution lost**: 1121 falls to 809 at N = 4000, σ = ε;
- **no single threshold reproduces it**: the noise-free ε' matching the noisy count is 1.51ε, 1.26ε and 1.11ε at
  N = 2000, 4000 and 5000.

An **unsteady clock** does the same in milder form [new: `clockg.mjs`]: jittered ±30 % about the same mean, the reader
received the same number (4305 against 4301 at N = 40 000) and resolved 6.5 % fewer, entirely from uneven spacing.

**The Cauchy when N is unknown** [new: `cornerrule.mjs`, predictions registered in `cornerrule-predictions.md`]. The
classical calculation divides by N, but N enters only as NΔ = π/2, the whole quarter turn; what it assumes is that the
entries fill the turn evenly, horizon included. A serial reader never reaches the horizon. It does reach the corner,
v = h, which holds half the quarter turn. So:

> **The corner rule.** Count the arrivals from home to the corner; call it c. Below any reading s ≤ 1 the count is
> c · (4/π) arctan s. Past the corner, the arrivals between the corner and s mirror those between 1/s and the corner,
> by the swap (arctan s + arctan 1/s = π/2).

A steady turn of 400, 4000 and 40 000 steps, the reader stopping at 60 %, 80 % or 95 % of the turn, knowing neither N nor
its step:

| prediction | result |
|---|---|
| near half: within 1 entry | worst 0.995 to 1. Held |
| far half by the swap: within 2 | worst 1 to 2. Held |
| normalised curve against (2/π) arctan s: worst gap below 1/c | 0.5/c to 0.95/c. Held |
| control, laid by a unit: the swap is off by a factor of s | exactly 4.000 at s = 4. Held |
| unsteady clock (±30 %): worst gap below 0.02 at N ≥ 4000 | 0.0005 to 0.0053; 0.0216 at N = 400. Held |

The rule never uses N or Δ, only the steadiness of the step. Its count c is exact whatever ε is: counting arrivals is not
limited by fidelity, placing them is.

**What the rule implies.** The swap puts as many arrivals after the corner as before it, so the rule forecasts a lap of
2c. That is the number of arrivals the reader receives per quarter turn, **gN, not the world's N** (*serial-watch*, "Grain
over N": a crossing "recovers gN … NOT the world's N"). It rests on the turn running on to the horizon. The Sep 20 record
reaches the same lap by **confirmation**: the running product passes back through 1, and the move repeats one arrival
later, "and then N = the count there" (*serial-watch*, observers O1 and O3). So:

| | what it gives the reader | when |
|---|---|---|
| **the corner rule** | the lap, **forecast** | at the corner, half a lap in |
| **closure** (O1, O3) | the lap, **confirmed** | one arrival after the product returns to 1 |

The corner is where a serial reader can first forecast its lap; closure is where it knows it.

**Already in *Degrees of Freedom*, with a caveat this test did not reach** [corpus: *Degrees of Freedom* §5.19a,
§5.15k–m, §5.18a]. "The corner is crossed at arrival N/2, so N = 2m **exactly** — *half the cost of closure*." But
"only where the corner is unique": a wandering signal crossing 1 twenty-five times in 64 arrivals gives "25 answers
between 4 and 122", and "the prior is not corrected; it is confirmed". `cornerrule.mjs` tested only steady, monotone
turns, so its result holds only there. Two further cautions from the same paper: the swap-mirror assumes a sampling
symmetric about the corner, and "still not shown: whether a sampling can be symmetric about the corner *without being
chosen to be*" (§5.18a); and "a frame cannot lift itself by its own readings" (§5.15l). The steady step the corner rule
assumes is exactly such a frame, taken as a premise the reader cannot check.

**Inside and outside, in h and v** (Tom, Sep 24: *"inside = serial = cauchy = fisheye"*; the outside line drawn to
match, its visual name provisional). One push, two parts arriving together; the bar of 1 sweeping from home (h = 1) to
the horizon (h = 0). Two readers meet that one sweep:

> **The inside reader holds both parts and keeps only their relation, v/h.** Its reference moves with every arrival
> (the unit rule). It packs as h²: dense at home, thinning toward a horizon it never reaches. **Inside = serial =
> Cauchy = fisheye = the unit rule.**
>
> **The outside reader holds one part, v, against a frame it keeps.** It keeps the size. It packs as 1/h: sparse at
> home, piling up at a rim it can see, v = 1, where it saturates. **Outside = parallel = arcsine (Chebyshev) = the
> reverse fisheye = the kept frame.**

**v and h are different things to the two readers** (Tom, Sep 24: *"V and H are different when read from the inside
versus the outside"*) [reading]. One point, a quarter turn θ from home:

| | **inside** (at the centre) | **outside** (far away, looking side-on) |
|---|---|---|
| **v** | one part of the arrival: how far across from the focus | a position across its view, which it sees |
| **h** | the other part of the arrival: how far toward the focus | the foreshortening: the depth along its line of sight, which it cannot see |
| their size | dropped; only the relation is kept | kept, against its frame |
| what it can hold | v/h | v directly; h only indirectly |
| as h → 0 | the reading runs off to infinity | the surface turns edge-on: the rim |

To the inside reader, v and h are two parts of one arrival, received together and even-handed. To the outside reader
they are not even-handed: v lies across its view, h along its line of sight, and a side-on view discards exactly that
direction. It recovers h only as foreshortening: neighbours seen side-on are hΔ apart, so h appears as the spacing, the
1/h crowding [cited: "foreshortening gives orientation", Gårding 1993, §0]. **So the outside reader has nothing to divide
by, and the inside reader has no size to keep.** The difference between the two readers is a difference in what v and h
are to each.

~~*A clue for the 3D thread, not a claim* (§5.5): to the outside reader, h is depth.~~ **Withdrawn by ruling (Tom, Sep
24): depth is z**, the log radius, as *Degrees of Freedom* §5.19 has it. What the outside reader recovers from h is how
squarely the surface faces it, its tilt, not its depth. The struck passage is kept for the record: Tom, Sep 20: *"the 1d signal is where
depth comes from, it is the z. The 2d signal would then be the x and y."* If the parallel reader lacks exactly the depth,
and the serial reader is where depth comes from, each supplies what the other cannot see, which fits "3d is just serial
+ parallel". ⚠ **But *Degrees of Freedom* rules depth differently**: depth is z, "the log of the magnitude", the log
radius, and "x and y carry the direction and nothing else" (§5.19). h, being readable from the address
(h = 1/√(1 + s²)), is on the direction side. The foreshortening meant here is a line-of-sight depth, a third sense
beside that paper's two ("indirection depth" and "coordinate depth", §5.19). The clue stands only as a clue. *The Centring*
§1a supports it: the outside reader's gaps, if the stones are evenly hung, "give how squarely the surface faces it, and
that gives depth" [corpus: *The Centring* §1a]. *The Boundary* goes the other way: from a facing point
"h = |x| and v = 1", so v is the facing distance (B276), and in triangulation "a point sits at height **v** with offset
**h**" (B319); while B69 finds the labels "one choice wearing three names". Which of v and h is depth is a labelling,
and the corpus has used both.

**Two inside readings** [corpus: *The Centring* §6, "half or whole"]. The inside reader here holds one ratio, v/h, which
repeats every half turn. *The Centring*'s enclosed reader holds both components against the arrival's own size,
(v, h)/size = (cos u, sin u), which keeps the side and covers the whole circle; the circle is that reading's fixed
point. The fisheye is the ratio reading. Neither reading holds "a tally of how many horizons it has crossed".

One sweep; one reader divides and the other does not. Why each is which:
- **a serial reader must divide**: it has no unit, the size being absent rather than degraded (*The Serial Cauchy* §1),
  so the relation is all an arrival leaves it; and its clock is what meets the turn evenly. It holds both terms only from
  observer O4 of `serial-watch.xlsx` up; below that it has closure and a count, but no Cauchy;
- **a parallel reader keeps the magnitudes**: it sees the whole shape at once against one frame, so it need not divide.
  *Keeping the Horizon*: "saturation is what the horizon looks like in a system that kept a frame."

Where each stands: the inside reader at the centre, its sight lines all through one point; the outside reader far away,
its sight lines parallel, which is why it is called parallel. Run the fisheye backwards and the result is neither: it is
the dial, 1/h², the exact inverse. The outside reader's 1/h is opposite in direction, not the inverse.

**Registers and names.** The camera world's "fisheye" (the orthographic model r = f sin θ among them) squeezes the edges,
so it is the *outside* reader's lens; this series' fisheye is the inside reader's (§3.1's naming snag, resolved). The
outside reader's formal name is the arcsine law, Chebyshev in approximation theory; its visual name is not yet ruled
("reverse fisheye" here; Tom also offered "negative Cauchy", apt as a picture but misleading as a formal term, since the
negative of a Cauchy variable is Cauchy and h⁻² belongs to the dial). The pure-mathematics names are the semicircle
(central projection) and the chord (orthographic projection onto the diameter), both builder's drawings. **Caution:**
*The Unit Rule* uses "corner" for the register's crossing (arrival = hold) and "fulcrum" for v = h; this paper's corner
is v = h.

**Against *The Cauchy*** (Aug 22, checked Sep 24). It already has the lens as the density: the measure is "a constant
over one-plus-the-ratio-squared", and "a band of ratios weighs exactly the arc it subtends" (§4); the rung density
peaks at the fulcrum (§7); "the Cauchy's own scale parameter *is* the fulcrum" (§11a). Three points bear on this
section:
- **Whose measure.** "Both steps belong to the resolved object rather than to the reader"; "the reader does not choose
  this measure and could not check it. It inherits it" (§4); "the arrivals are the pair's. Their distribution is an
  account's" (§5). With *Degrees of Freedom* §5.15n and *The Boundary* B300, that is three papers against calling the
  Cauchy the reader's own: the lens is where the reader stands, the measure is inherited.
- **Half, or a quartile?** The corner rule uses "the corner holds half the quarter turn". *The Cauchy* §11a says "home
  is the median of the arrivals; the fulcrum is their upper quartile". Both are right, in different readings: on the
  unsigned quarter turn the reading is below 1 half the time, as §4 there says ("the weight below the fulcrum is one
  half because the fulcrum halves the arc"); on a signed half turn the tangent is below 1 three-quarters of the time.
  The corner rule is the unsigned case; §11a is the signed one, which waits on the sign ruling.
- **A reader holds no collection.** "Forming any of these statistics needs a collection, and a reader holding one arrival
  at a time holds no collection" (§6, §12). The corner rule needs one number, the count c, so it needs a counter (O2 of
  `serial-watch.xlsx`) and no more; its forecast and its checks against arctan are an account's, not the reader's.

**Against *Perfect Fidelity at Zero*** (archived by Tom on Sep 5; recorded, not current doctrine). It has the observer's own
coordinate as the rapidity, asinh(v/h), and the fidelity h = cos θ as the rate dθ/dζ; so "the Cauchy, 1/(1 + r²), is
not the observer's law. It is the shadow an observer uniform in its own coordinate casts when its arrivals are laid on
the drawn arc" (§6). On that account the reader's own packing in the reading is h, not h². And its close: "the
observer does not act on it, does not apply a lens to it … *fisheye* is the adjective for what that looks like. From the
centre a circle looks like a circle." Both cut against this section's "the lens is the reader's density".

**Against *The Observation Atom* and *The Balance*** (checked Sep 24). Both refuse the act this section gives the inside
reader. *The Observation Atom*: "v/h names an executed quotient — a value the observer does not compute … held as the
pair (v, h)"; dividing is "a division and a conditional, and the observer has neither" (§1.5). *The Balance*: "executing
v/h is what is forbidden; *holding* (v, h) and reading their standing is the primitive act itself" (§20.2); the
evaluated quotient belongs to "the outside describer, and nobody else". Both put the fisheye on the describer's side:
"The fisheye is not something the observer applies. It is what an even layout looks like when described in the slope
chart", and the Cauchy is "the chart's — and only for the angle device" (*The Observation Atom* §1.6a–b); "the divergence
at the horizon lives entirely in the chart, and the chart is precisely the object the observer declines to compute"
(*The Balance* §27.6). And *The Observation Atom* forbids the corner rule's count: "No running total can be kept: it needs
a register, and the register is the observer" (§2.1); the serial-watch ladder adds that register on purpose (O2). The
reconciliation already in the corpus is *The Relation Space* §25: the reader holds the pair and its disagreement, and
"only the final report divides". Read that way, "the inside reader holds v/h" means holds the pair whose name is v/h.

**Two readers** [reading, from §6.1]. Densities do not add. Each reader keeps its own lens and its own pixel; what the
pair combines is **coverage**, an entry held if either resolves it. The pair is blind only where both are, first at
h²v/κ = ε/d between the corner and the horizon; past the outside ceiling it holds the inside reader's 8/d (§6.1). Whether
noise's false resolution passes into the pair's join is open (§9, item 12).

**Against *Degrees of Freedom*** (checked Sep 24 against the uploaded copy, §5.15–§5.19). Much of this section is
already there, and some of it is contradicted there:
- **Already there.** "The lens is what the word 'density' means once the breadth has been fixed", with du/dx =
  d/(x² + d²), 1/(1 + x²) at d = 1: "It **is** the fisheye, written out" (§5.15i). Serial hangers "unequal, and arranged
  by the Cauchy", (2N/π)/(1 + s²) per unit of address, "the Cauchy's own density" (§5.16). An even frame on the arc is
  "a Cauchy-spread sampling … Neither is neutral" (§5.15h). And the Cauchy is not made by g: "It is there before the
  reader chooses anything … g then decides how many places to put on a lens that was already shaped" (§5.15n). This
  section's "the lens is the density" and "count is secondary" restate these.
- **Whose the Cauchy is.** *Degrees of Freedom* §5.15n assigns the kernel to **the setup**, "fixed by a breadth and one
  number saying where the facing is", and g alone to the reader. This section calls the Cauchy the reader's density.
  They agree only if where the reader faces from counts as the reader's, as §5.15h's "a third reader quantity" allows.
- **What g is.** Defined there: "the share of the freedom's hangers that are placed" (§1, Tom Sep 18: "it is a
  DENSITY"), purely the reader's: "there is no g error anywhere, because there could not be" (§5.15g). That largely
  settles §9's "evaluated or placed" ruling: placed, and placed by the reader, never a gap the world left. But g is not
  a free scalar: "closure quantises g to multiples of 2/N", and "gN is a subset, not a count" (§5.15b); in serial "g does
  not punch holes in the signal, it multiplies it" and "nothing in a product says how many factors it has" (§5.18). So
  the steady clock as g, and ρ → g·ρ above, hold as counts but carry no closure guarantee, and a serial reader cannot see
  its g.
- **ε as a pure pixel** is too clean: a frame can "beat against a feature of the world" and the reader cannot tell
  (§5.15d); error "belongs to the pair (reader, world)" (§5.15k).
- **Two conventions.** *Degrees of Freedom* §5.15e counts addresses per unit of turn (1 + s²); this section counts turn
  per unit of frame (h²). Reciprocal conventions: the log-register entries of the two are not the same quantity.
- **The outside reader is not in *Degrees of Freedom*.** Its parallel hangers are "equal and uniform" in the turn, the
  same hangers read another way, and the parallel account has "no home, no fulcrum and no horizon" (§5.15, §5.16). The
  arcsine outside reader with a rim is this session's; it conflicts with that line as §5.2's "the view from everywhere"
  does with the Sep 22 rulings.

**Corrections made on the way** (from `reader-densities.md`):
- "Dimension adds one power of h per dimension": wrong for the side-on lens, which is 1/h in every dimension. Caught
  against the document's own numbers and checked in `densities2.mjs` before correcting.
- `clockg.mjs` K3 ("a jittered clock resolves more than 3 % fewer"): failed at the two smaller N (−1.1 %, −2.2 %), held at
  the two larger (−6.5 %, −4.9 %). The size depends on how near the reader is to its ceiling.
- `noise.mjs` Z1 ("false resolution grows with σ"): mostly held, but levels off above σ = ε/2 and dips at N = 2000 (37 to
  31). Z2 held only just at σ = ε/2 (a 10.1 % spread against the registered 10 %).
- "The reader has inferred N" (said in the session after `cornerrule.mjs`): corrected to gN, above.

---

## 7. Relation, address, payload

> **(1 Oct)** Breadth means extent, not quantity (Sep 24); the "breadth" and "density" of digits in this section are a different use of both words.

Separating addressing from what is addressed is old in computing. Consistent hashing maps keys and caches into the unit
interval, later drawn as a ring, so that adding a cache moves only the keys nearest it [cited: Karger et al. 1997].
Lazy evaluation computes a value only when it is demanded [cited: Henderson & Morris 1976].

From the reader's side the separation reads [corpus: *The Cauchy, Inside and Out*, "The stones can be anything"]:
- **the relation** supplies an address; **the address** picks a position; **the payload** is whatever stands there.
  "The geometry supplies the addresses; the data supplies the objects."
- **For a shape, the payload is the address.** The inside reader's reading is made from the magnitudes it receives, so
  address and content coincide. They come apart only when the reading comes from outside the content: a hand on a dial,
  a query, a key.
- **The one condition the content must meet is that entries differ**: an array of identical glyphs has perfect
  addresses and cannot tell a reader where it is [corpus: *Browsing the Fisheye* §12].

**An index has no unit to change** [corpus: *The Cauchy, Inside and Out*, "An index has no unit to change"]. A
magnitude can be rescaled, because a unit can be changed: centimetres become kilometres and nothing is lost. An index
counts things, its only unit is one entry, and an entry cannot be divided or merged: no "kilo-record" keeps what
the number names. What things get instead of a larger unit is a **level of the address**: a crate is not a larger
egg. Units compose by multiplying and discarding; levels compose by nesting and keep everything. The dial's N is
2⁵³ − 1 because that is where a double stops holding integers exactly: where magnitudes stop caring and indexes run
out.

**The logarithm is a unit of a different kind** [corpus: same paper, "The logarithm: a unit of a different
kind"]. An ordinary unit divides the thing; a logarithmic unit counts its doublings. log₂ of an index says how many
levels deep its address runs without dividing any entry, which is why the log register, not a larger unit, is what an
index can be navigated by. But it gives the level, not the entry: neighbouring records share a log. The log navigates;
the digits address.

**Breadth and density are the two sides of the point** [corpus: same paper, "Breadth and density as the two
sides of the point"]. Breadth is how many whole digits a number may have; density is how many fraction digits can be
held. An index is all breadth (no fractional part: larger, never denser); the quarter turn is all density (a fixed
whole: denser, never larger); the dial joins them. In the log register, the whole part of log₂ is the level and the
fraction the position within it, which is floating point's exponent and mantissa.

**The dial is one implementation of a known idea** (Tom, Sep 23: "our dial is just another implementation of this
idea with our vocabulary"). Scale-free domains keep finding the log register: the musical octave, Fechner's law that
sensation goes with the logarithm of the stimulus, decibels, f-stops, bits, floating point's exponent, rapidity. The
logarithm is the only continuous map that turns multiplying into adding, so any domain without a preferred size
ends up there [cited: Lang 1997, §IV.2; Fechner 1860]. The fuller instrument, levels, browsing within a level and an
exact address, has been built too:
- **zoomable interfaces**: Pad, an infinitely zoomable information surface, and Pad++ [cited: Perlin & Fox 1993;
  Bederson & Hollan 1994]. Space-scale diagrams make scale an explicit dimension, so that "moving a viewing window
  around via pans and zooms corresponds to taking it on a trajectory through scale-space" [cited: Furnas & Bederson
  1995];
- **optimal pan and zoom**: smooth and efficient paths through that space [cited: van Wijk & Nuij 2003, 2004], whose
  metric is the hyperbolic plane's; Reach and North give the explicit Poincaré half-plane model [cited: Reach &
  North 2018]. That is this paper's "the space of readers is the hyperbolic plane", found from the interface side;
- **web map tiles**: each level doubles the scale, and a tile's quadkey has one base-4 digit per level, "the length
  of a quadkey (the number of digits) equals the level of detail" [cited: Microsoft, Bing Maps Tile System]: the
  dial's tower of bits;
- **pyramids and multiresolution**: mipmaps, a prefiltered image halved per level [cited: Williams 1983], and the
  dyadic wavelet decomposition [cited: Mallat 1989];
- **the hyperbolic browser**, with focus, level and a pixel budget (§3.3).

So the dial is not a new instrument. What is new is what it is attached to: the reader and its two registers, the
Cauchy as the law its moves keep, fixed fidelity with N unknown, and the SR identity (§4.3a).

**The instrument.** The corpus's dial, with its tower of bits [corpus: `example-tower.html`, Sep 8–13], carries most of
this paper at once:
- it browses 2⁵³ − 1 records laid by share, and reads the blue needle as unit · tan(blue);
- its corners are the rungs; its radius is the unit; a change of radius is the move a boost makes on the sky (§4.3);
- its tower shows the steered bit as log₂ of the unit, so "one rung of the dial is exactly one bit of the address":
  the count as floating point (§6.3), found on the instrument before it was measured;
- "nothing is stored": each cell's content is a hash of its own prefix, made on arrival, a lazy payload.

The dial does not go blind at its focus, where a share-laid strip does, because it measures in the reader's unit, not
at π/N a record: its window always holds about 2·2⁵ units, whatever N.

---

## 8. What is known, what is new, what is not proved

**Known, and cited.** The group and its three faces (Cauchy rigidity; hyperbolic plane; 2+1 Lorentz); fisheye views
and the hyperbolic browser; rapidity, velocity space, the Thomas–Wigner rotation as an area; the conformal action of
boosts on the sky; hyperbolic motion and its horizon; the Breit–Wigner line; RP¹ and its double cover; the turning
tangent; the occluding contour; rational Chebyshev functions on the whole line (Boyd); consistent hashing, list labeling, floating point, lazy evaluation.

**Not found stated elsewhere, in first-pass searches** (the corpus's contribution):
1. **The reader as the starting point.** The published accounts take the group as given. Here it is the repertoire of
   a reader holding h and v and dividing: its compose and ratio moves, one from each register, generate exactly
   PSL(2,ℝ), and its moves are exactly the cross-ratio-keeping maps (§2.1a). Neither register alone gives the group.
   The group-theoretic steps are classical (the KAK decomposition; the cross ratio fixing a projectivity); what is new
   is the reading of them as a reader's two registers.
2. **Fixed fidelity with N unknown**, and what it does: the growing rim loss and the ceiling; each reader blind where
   its lens is slowest; the pair's repair; checksums blind to a balanced loss; which entries a layout spends its budget
   on; a growing array that comes to look finished. (The budget itself, and a layout that needs no N, are already in the
   hyperbolic browser, §3.3.)
3. **The sorting by sweeps**: array, ring and shape as one, two and four sweeps of the bar; facing as the difference
   between a direction and its opposite.
4. **The stitch**: two real readers, neither holding N, rebuilding the classical shape at the horizon they share.
5. **The corner rule** (§6.4): a serial reader with no N and no step recovers the Cauchy by normalising at the corner and
   mirroring by the swap, and so forecasts its lap (gN) half a lap before closure confirms it. ⚠ **Not new inside the
   corpus**: *Degrees of Freedom* §5.19a already has "the corner is crossed at arrival N/2, so N = 2m exactly — half the
   cost of closure", with a caveat §6.4 did not test (it holds only where the corner is unique). What §6.4 adds is the
   Cauchy's shape recovered from the corner count, and the far half by the swap.
6. **Small identities read in a new place**: the hold as β² + 1/γ² = 1; a change of unit as the move a boost makes on the sky; a steadily growing
   array as hyperbolic motion; the count held on a dial as floating point.

**The novelty searches (Sep 23).** Three searches covered the reader-derived group, the fixed-fidelity results and the
mathematics of perspective. Their verdicts, claim by claim:

| claim | what is already known | what was not found |
|---|---|---|
| the reader's moves generate PGL(2,ℝ); each register one half of KAK (§2.1a) | the group, KAK, the cross-ratio characterisation (textbook); Cauchy uniqueness under projective maps (Knight 1976; Knight & Meyer 1976; Dunau & Senateur 1987; McCullagh 1992, 1996; Mendonça & Lundell 2025); the Cauchy as a ratio or an angle (Jones 1999; Cuadras 2002) | the group derived as a ratio-holding reader's whole repertoire, with angle and ratio as its two halves. **The novelty is the framing, not a theorem** |
| more points, less seen: the count at fixed ε peaks and falls to zero (§6.1) | the crowding (Chebyshev points; Trefethen 2019; Kosloff & Tal-Ezer 1993) | the fixed-ε count and its peak-then-fall. **Looks new as a stated result** |
| the stitch (§5.3) | support-line reconstruction (Prince & Willsky 1990); closure (Minkowski); the turning function (Arkin et al. 1991) | the two-reader split without N, joined at the contour. **New as a combination** |
| closure blind to a balanced loss (§6.1) | sum checks miss cancelling errors (surveying folklore) | the specific instance; **little novelty** |
| array, ring, shape (§5.1) | RP¹ against S¹; axial against directional data (Mardia & Jupp 2000); nematic directors (Mermin 1979) | only the array/ring/shape framing; **the mathematics is standard** |
| a growing array as hyperbolic motion (§4.5) | the identity (Born 1909; textbook) | its reading for arrays and counters; **interpretation only** |
| the fisheye, perspective, the Cauchy and aberration as one group action | each pairwise link: cross ratio and perspective; pinhole and Cauchy (Cuadras 2002); Cauchy and Möbius (McCullagh); stereographic and conformal (Schleimer & Segerman 2016); boost and camera image (Penrose 1959; Weiss FAQ) | **no source puts them together**, with or without a reader |

The honest summary: **the theorems are known; the joining is not.** The searches were web searches, not database
searches, and several full texts could not be opened.

**Not proved.**
- **That the reader has exactly the moves swap, compose and ratio** (§2.1a). Given them, the group is proved; that
  they are the reader's whole repertoire is a modelling statement.
- **Novelty.** The searches were first passes. Directional statistics and the mathematics of perspective have not been
  searched properly. The hyperbolic browser, now read in full, already has the resolution budget, the N-free layout and
  the loop rotation (§3.3).
- **That the Cauchy is every reader's density** (§6.4). Shown for a reader that divides and meets an evenly met turn;
  that these are the only readers worth the name is a modelling statement.
- **The 3D case.** Everything above §5.4 is on a line or a plane curve. In three dimensions the horizon is a curve. §5.5
  records one coverage test and a framing question; none of the claims above is extended there.

---

## 9. Open

> **(1 Oct)** Item 8's sign is ruled: magnitudes, each on [0, 1] (R37, Sep 25). The g items predate the Sep 30 definition of g. New open items are kept in v-and-h §9.

1. ~~Prove or refute closure and maximality~~ Done (§2.1a): closure holds once the ratio move is included; maximality
   is replaced by the cross-ratio characterisation. Left: whether any published account derives PSL(2,ℝ) from a
   ratio-holding observer (search).
2. ~~Run the ring prediction~~ Done (§5.1, `ring.mjs`): the prediction was too strong; a ring has its own landmark
   sequence, half the shape's.
3. ~~Read the hyperbolic browser in full~~ Done (§3.3): it already has the budget, the N-free layout and the loop
   rotation.
4. ~~Search directional statistics and the mathematics of perspective~~ Done (§8, the novelty table). Left: a
   database search (MathSciNet, Web of Science) before any claim of priority.
5. ~~The two octaves, the inside reader's nodes, a local repair, the reader choosing its radius~~ Done (§2.1b,
   §6.1b, §6.1c). The composite placement works for nested and separated features, with a borrowed acceptance test.
   Left: locating a centre between samples; re-running the
   function quartile rule with sines; a database search before any claim beyond the reading.
6. ~~Where between corner and horizon each reader runs out at fixed fidelity~~ Done (§6.1, `fixfid.mjs`): the pair
   runs out between them, at h ≈ √(ε/d). Left: the sweep's overhead against its stop tolerance (needs
   `regime.mjs`); whether the 8/d hangers the pair keeps past the ceiling carry any shape.
7. Say where, if anywhere, fixed fidelity enters physics: "a fixed-fidelity observer cannot tell celerity 1/ε from
   light" is only a reading of §6.3 (§4.5).
8. **Rulings** (Sep 22–24). **The order is ruled: v/h** (Tom, Sep 24). **The facing: one per freedom** (Tom, Sep 24),
   which is Sep 19's "each freedom IS a facing". Still owed: the sign (are v and h magnitudes or signed? *The Boundary* B324–B325: "an unmade
   ruling … the corpus currently holds both, in different files"; §1.3's "facing carries the sign" was killed by B57);
   the order (v/h or h/v? consecutive quarters read as the swap, B69; *The Boundary* B328 finds `freedom.js` using v/h
   while the receipts use h/v); and **g, "the
   density dial"**, which mixes hangers *evaluated* (the reader's count, §6.4) with hangers never *placed* (which would
   change the array's count). *Degrees of Freedom* largely settles this: g is "the share of the freedom's hangers that
   are placed", placed by the reader, and purely the reader's (§1, §5.15g; see §6.4).
9. **3D framing** (§5.5): hemisphere, or whatever the inside reader can see? The pocket hidden from both is the test that
   can fail. Each reader's own rules for turning its data into directions; the motion reader in the flashlight picture.
10. **Which sources project to an evenly met address array** (§1.6, §2.2): the traverse question, restated.
10a. ~~Readers build, or only read?~~ **Ruled** (Tom, Sep 24): readers don't build arches; **building is the view from
    everywhere**. *The Centring*'s "the reader builds against the circle" and "the inside reader erects the frame"
    (§0, §1a), and *The Boundary*'s "the builder puts it up" (B87), are to be read as the view from everywhere's.
11. **The turn, demoted and needed** (§6.4). The Cauchy needs counting laid on the turn, not on the reading, and the
    turn is what Sep 24 demoted to the builder's drawing. A candidate answer: the turn has a lap and the reading only a
    horizon, and a counter needs closure to re-grain (*The Serial Cauchy* §6a), so it must count in the frame that
    closes. If that holds, the turn returns as the counter's own frame. Unruled.
12. **A guard against false resolution** (§6.4). A noisy reader resolves spurious gaps at the rim, so any rule that
    counts resolved entries (the pair's repair, R(N)) over-counts under noise. How large a σ the repair tolerates is
    untested.
13. **Is the density list complete?** The working document found ten sources in eight kinds, now read as the Cauchy's
    parameters, a count, and limits (§6.4). A further source would have to change the packing in a way none of those
    does. None is known.
14. ~~Chosen or suffered~~ **Ruled: chosen** (Tom, Sep 24). The reader's limits are counted as the reader's choices,
    in line with *Degrees of Freedom*'s "gN is CHOSEN, and a choice cannot be wrong" (§5.15b).

---

## Appendix: for the rigorous paper

> **(1 Oct)** The order this outline proposes (the reading first, the circle after) is reversed by R143: the circle and other shapes (situations 1 and 2) come first, and situation 3 is situation 2 with v's breadth unknown. "Whether its length is known" is now "whether v's breadth is known".

*Tom, Sep 23: this paper is the session record, and the basis for a complete rigorous paper in a future session.*

**Structure** (Tom, Sep 24). The rigorous paper builds on one object: **the magnitude list, which is anything that can
be indexed** (an index in, a magnitude out); the reader turns the same index into an address, and the two meet only at
i. The one property of the list the geometry depends on is **whether its length is known**: known, the semicircle;
unknown, the freedom (§6.2). *"These are all the same things at their core, just a collection of things that can be
indexed."* The examples (arrays, shapes, physics, systems, lazy lists, addresses to another list) **go at the end**, each
plugged in to show that it works universally, not threaded through the argument.
What that paper should contain, drawn from the material above:

1. **Definitions**: the reading s = v/h as a point of the projective line; the quarter turn and the freedom; home,
   corner, horizon; the two registers; the three moves swap J, compose R_t, ratio D_k.
   **Order of definitions (Tom, Sep 24: the unit circle is demoted, "just something the everywhere view can infer"):**
   start from the reading and the freedom, [0, ∞) with home, corner and horizon, which is all a reader holds. Bring in
   the circle and the quarter turn afterwards, as the view from everywhere's inference (the rim of the space of
   readers; the circle whose rotations the compose move is) or as the builder's drawing ("semi-circles are for
   builders, horizons are for readers"). §1.2 of this paper currently introduces arctan and the quarter turn early;
   the rigorous paper should reverse that.
2. **Proposition (closure)**: ⟨R_t⟩ = PSO(2); ⟨J, R_t⟩ = PO(2); ⟨R_t, D_k⟩ = PSL(2,ℝ); ⟨J, R_t, D_k⟩ = PGL(2,ℝ).
   Proof by KAK. Checks: `closure.mjs` C1–C3.
3. **Proposition (characterisation)**: the moves are exactly the cross-ratio-preserving bijections of RP¹. Elementary
   proof. Checks: C4–C5.
4. **The law**: uniform turn to Cauchy (Cuadras; Johnson, Kotz & Balakrishnan); Knight's theorem with its exact
   hypotheses (atomless location–scale type, invariant under s → −1/s); McCullagh's equivariance; the doubling keeps
   Cauchy laws Cauchy (Pitman & Williams) but is not a move (it changes cross ratios).
5. **The space of readers** is PSL(2,ℝ)/PSO(2), the hyperbolic plane; composition, the pan cost and the loop
   rotation (Lamping et al.; Aravind) as KAK.
6. **Proposition (the speed dictionary)**: with the blue at gd(ζ), v = β, h = 1/γ, s = βγ, and the hold is
   β² + 1/γ² = 1. **The sky dictionary**: a boost dilates the half-angle stereographic coordinate (PDG). Keep the two
   apart.
7. **Proposition (steady growth)**: an array growing at rate r on unit u has celerity n/u = (r/u)t, hyperbolic motion;
   the proper time per doubling is (asinh(2n/u) − asinh(n/u))/a → ln 2/a.
8. **Proposition (array, ring, shape)**: laps of π and 2π; landmark sequences H C o C and its double; the double
   cover S¹ → RP¹; axial against directional data (Mardia & Jupp).
9. **Fixed fidelity, with closed forms where they exist**:
   - the limb count R(N) = (N/π) arccos(εN/2π), its peak and R_max = 1.1222/ε (`rigor.mjs`);
   - the array's distinct run √(u/ε − u²), maximal at u = 1/(2ε);
   - the count error ε(1 + s²)/(2s) per reading, about εn/(2u) far out; re-uniting bounded by (17/8)ε for s in
     [2, 4];
   - the window: the focus merges at n = πR/ε, and everything by πR(1 + (W/2R)²)/ε.
    - the two octaves: angle doubling (2-to-1, keeps the uniform turn, changes cross ratios) against dilation (a
     move); agreement near home, parting at the corner (`twooct.mjs`);
   - the inside reader's nodes are Boyd's rational Chebyshev points, the Cauchy's quantiles; TB_n(y) = T_n(y/√(y² + L²))
     (`inside.mjs` B1–B2);
   - local interpolation on the resolvable nodes: Lebesgue constant bounded, error confined to the lost band
     (`inside.mjs` L1–L4);
   - the radius from the data: corners at the quartiles; exact for Cauchy entries; for functions, scale-equivariant
     with a shape-dependent offset (`selfl.mjs`);
   - the pole rule for the best (m, L), the geometric mean for two scales, and the parity condition at the horizon
     (`poles.mjs`, `parity.mjs`);
   - the decay rule and the cross-check rule; a feature between the central nodes is invisible at that radius
     (`decay.mjs`);
   - the sweep's cost and its stopping rule; the tail's order read from the octave ratio (`sweep.mjs`);
   - the regime stop and its cost, span + about 12 octaves at every N; the window slides with N, its width does
     not (`regime.mjs`, `regimeN.mjs`);
   - coarse sweep, fine reading: exact for one octave (`coarse.mjs`);
   - where the pair runs out: the shared blind band opens at (ε/Δ)√(1 − (ε/Δ)²) = Δ/d on the circle, and at
     h²v/κ = ε/d locally; past the ceiling the pair holds 8/d (`fixfid.mjs`–`fixfid3.mjs`);
   - several readers from the sweep's change profile (`place.mjs`); centres by greedy placement, and the two
     directions of the plane of readers (`centre.mjs`); the plane search failed (`hplace.mjs`);
   - **cite, do not claim**: Boyd 1982, Boyd 1987 and Tee & Trefethen 2006 for §6.1c items 2–4.
10. **Measured results without closed forms**, with scope stated: the stitch (convex, even hangers, two horizons);
    the repair; the checksums' blindness (with the exact argument for a perfectly balanced loss).
11. **Relation to the literature**: the novelty table of §8, after a database search.
12. **Left out as exploratory**: the dial as instrument, the Breit–Wigner reading, physics as the outside reader, the
    array-as-observer reading beyond the identity, and "classical is both sides together" except as a one-line
    interpretation.

13. **From the Sep 24 session** (§1.6, §5.4):
    - **definitions**: the world's breadth (its extent, Tom, Sep 24) and its count N, kept apart; the projection's uniform address array; the reader's density as entries per
      unit of its frame, finite by ε; the view from everywhere as **just breadth**;
    - **the order of limits** stated as removing the reader's density, not reaching an infinite one;
    - **the test**: breadth does not change with the reader, density differs; with the four-row density table;
    - **the density is the lens's slope** (§6.4): the Cauchy for the dividing reader, with location = focus,
      scale = unit, h^(n+1) in n dimensions; its side-on twin 1/h in every dimension; count as a scale factor; ε as the
      pixel, with coarseness set by εN; noise as the one limit that bends the curve (`densities.mjs`, `densities2.mjs`,
      `clockg.mjs`, `noise.mjs`);
    - **the corner rule** (§6.4, `cornerrule.mjs`): the Cauchy with N unknown, the lap forecast as gN, and its relation
      to closure (O1, O3 of `serial-watch.xlsx`);
    - **the inside view as the two-dimensional Cauchy**, with the corner circle's share 1 − 1/√2;
    - **scope**: readers require horizons; the arch (the thing) is not a reader picture; say which way "fisheye" points.

## References

### The corpus (outputs folder)

- *The Cauchy, Inside and Out* (`the-cauchy-inside-and-out.md`, Sep 22–23 2026), the session record behind §§1, 5, 6
  and 7; scripts `bothsides.mjs`, `repair.mjs`, `ceiling.mjs`, `gceiling.mjs`, `towercheck.mjs`, `landmark.mjs`,
  `dynarray.mjs`, `freedom.mjs`, `finished.mjs`, `window.mjs`, `dialphysics.mjs`, `doubling.mjs`, `closure.mjs`, `ring.mjs`, `rigor.mjs`, `octave.mjs`, `chebfix.mjs`, `twooct.mjs`, `inside.mjs`, `selfl.mjs`, `poles.mjs`, `parity.mjs`, `decay.mjs`, `sweep.mjs`, `regime.mjs`, `regimeN.mjs`, `coarse.mjs`, `place.mjs`, `centre.mjs`, `hplace.mjs`, `composite.mjs`, `composite2.mjs`.
- *Browsing the Fisheye* (`browsing-the-fisheye.md`, Sep 3–22 2026): the two conversions; the lens orthogonal to the data;
  the Cauchy as an address; relative and absolute angles.
- *SR through the Fisheye* (`sr-through-the-fisheye.md`, Sep 4 2026), scripts `sr-fisheye-checks.mjs` (C0–C10),
  `velocity-space.mjs` (V0–V5), `fourth-star.mjs`.
- *The Two Settings* (`the-two-settings.md`, Aug 22 2026): one sign; rapidity as the rung count; the Cayley–Klein fork.
- *sr.md* ("The Bounded Observer in Motion", v10, Sep 11 2026).
- The reader-geometry note (Sep 3 2026) and its scripts in `frame-scripts/`.
- *The Relation Space*; *The Centring* (Sep 17–18 2026); *The Unit Rule*; *Degrees of Freedom*.
- The navigation dial `fisheye-ladder-shape.html` and `example-tower.html` (Sep 8–13 2026); `field.html` and its
  embedded VCP library.
- `refresh-sep22-23.md` (Sep 23–24 2026): the consolidation record, with "3D: clues, not conclusions"; scripts
  `fixfid.mjs`–`fixfid3.mjs` (where the pair runs out), `samehemi.mjs`, `rig3d.mjs`; demos `stitch-sticks.html`,
  `two-readers-3d.html`, `shape-and-flashlight.html`.
- `reader-densities.md` (Sep 24 2026): the working accounting of the reader's densities, collapsed in §6.4; scripts
  `densities.mjs` (D1–D6), `densities2.mjs` (dimension), `clockg.mjs` (K1–K3), `noise.mjs` (Z1–Z2); and
  `cornerrule.mjs` with `cornerrule-predictions.md` (R1–R6).
- *The Serial Cauchy* (`the-serial-cauchy.md`, Sep 20 2026): the world's Cauchy and the observer's, kept apart; and
  `serial-watch.xlsx`, the serial observers O1–O5, grain over N, and counting.

### External

- Alexandrescu, A., Bueno-Orovio, A., Salgueiro, J. R. & Pérez-García, V. M. Mapped Chebyshev pseudospectral method
  to study multiple scale phenomena. arXiv:0706.3108; *Computer Physics Communications* (2009).
- Aloimonos, J. (1988). Shape from texture. *Biological Cybernetics* 58(5), 345–360. doi:10.1007/BF00363944
- Aravind, P. K. (1997). The Wigner angle as an anholonomy in rapidity space. *American Journal of Physics* 65(7),
  634–636. doi:10.1119/1.18620
- Arkin, E. M., Chew, L. P., Huttenlocher, D. P., Kedem, K. & Mitchell, J. S. B. (1991). An efficiently computable
  metric for comparing polygonal shapes. *IEEE TPAMI* 13(3), 209–216. doi:10.1109/34.75509
- Baumann, Biedl, Elashmawi, Fink, Saumell & Schulz (2026). On reconstructing a convex polygon from partial
  information. arXiv:2607.01423.
- Bederson, B. B. & Hollan, J. D. (1994). Pad++: a zooming graphical interface for exploring alternate interface
  physics. *Proc. UIST '94*, 17–26. doi:10.1145/192426.192435
- Bondi, H. (1964). *Relativity and Common Sense: A New Approach to Einstein.* Garden City, NY: Doubleday (Anchor).
- Borel, É. (1913). Notes in *Comptes rendus de l'Académie des sciences* 156, 215 and 157(17), 703. (Titles and end
  pages not confirmed; see the citation-status note.)
- Born, M. (1909). Die Theorie des starren Elektrons in der Kinematik des Relativitätsprinzips. *Annalen der Physik*
  335(11) [4th ser. 30], 1–56. doi:10.1002/andp.19093351102
- Boyd, J. P. (1982). The optimization of convergence for Chebyshev polynomial methods in an unbounded domain.
  *Journal of Computational Physics* 45(1), 43–79.
- Boyd, J. P. (1987). Spectral methods using rational basis functions on an infinite interval. *Journal of
  Computational Physics* 69(1), 112–142.
- Boyd, J. P. (2001). *Chebyshev and Fourier Spectral Methods*, 2nd rev. ed. Mineola, NY: Dover.
- Breit, G. & Wigner, E. (1936). Capture of slow neutrons. *Physical Review* 49(7), 519–531.
  doi:10.1103/PhysRev.49.519
- Cuadras, C. M. (2002). Geometrical understanding of the Cauchy distribution. *Qüestiió* 26(1–2), 283–287.
- Cueto-Felgueroso, L. & Juanes, R. (2009). Adaptive rational spectral methods for the linear stability analysis of
  nonlinear fourth-order problems. *Journal of Computational Physics*.
- Dietz, P. F. (1982). Maintaining order in a linked list. *Proc. 14th ACM STOC*, 122–127. doi:10.1145/800070.802184
- Dunau, J.-L. & Senateur, H. (1987). *Journal of Multivariate Analysis* 22(1), 74–78.
  doi:10.1016/0047-259X(87)90076-5 (short proof of Knight & Meyer's characterisation).
- Erdős, P. (1961). Problems and results on the theory of interpolation, II. *Acta Mathematica Academiae
  Scientiarum Hungaricae* 12, 235–244. (Via MathWorld's citation; the text was not read.)
- Fechner, G. T. (1860). *Elemente der Psychophysik.* Leipzig: Breitkopf und Härtel. (English, vol. I: *Elements of
  Psychophysics*, trans. H. E. Adler, 1966.)
- Fernández-Durán, J. J. & Gregorio-Domínguez, M. M. (2025). arXiv:2504.04681 (axial data).
- Furnas, G. W. & Bederson, B. B. (1995). Space-scale diagrams: understanding multiscale interfaces. *Proc. CHI '95*,
  234–241. doi:10.1145/223904.223934
- Furnas, G. W. (1986). Generalized fisheye views. *Proc. CHI '86*, 16–23. doi:10.1145/22627.22342
- Goldberg, D. (1991). What every computer scientist should know about floating-point arithmetic. *ACM Computing
  Surveys* 23(1), 5–48. doi:10.1145/103162.103163
- Gårding, J. (1993). Shape from texture and contour by weak isotropy. *Artificial Intelligence* 64(2), 243–297.
  doi:10.1016/0004-3702(93)90106-L
- Haraway, D. (1988). Situated knowledges: the science question in feminism and the privilege of partial
  perspective. *Feminist Studies* 14(3), 575–599.
- Hatcher, A. (2002). *Algebraic Topology.* Cambridge University Press. (RPⁿ as Sⁿ modulo the antipodal map.)
- Henderson, P. & Morris, J. H., Jr. (1976). A lazy evaluator. *Proc. POPL '76*, 95–103. doi:10.1145/800168.811543
- Hopf, H. (1935). Über die Drehung der Tangenten und Sehnen ebener Kurven. *Compositio Mathematica* 2, 50–62.
- IEEE (2019). *IEEE Standard for Floating-Point Arithmetic*, IEEE Std 754-2019. doi:10.1109/IEEESTD.2019.8766229
- Itai, A., Konheim, A. G. & Rodeh, M. (1981). A sparse table implementation of priority queues. *ICALP 1981*, LNCS 115,
  417–431. doi:10.1007/3-540-10843-2_34
- Johnson, N. L., Kotz, S. & Balakrishnan, N. (1994). *Continuous Univariate Distributions*, Vol. 1, 2nd ed., ch. 16
  (Cauchy distribution). Wiley.
- Jones, M. C. (1999). Distributional relationships arising from simple trigonometric formulas. *The American
  Statistician* 53(2), 99–102. doi:10.1080/00031305.1999.10474439
- Kannala, J. & Brandt, S. S. (2006). A generic camera model and calibration method for conventional, wide-angle, and
  fish-eye lenses. *IEEE TPAMI* 28(8), 1335–1340. doi:10.1109/TPAMI.2006.153
- Karger, D., Lehman, E., Leighton, T., Panigrahy, R., Levine, M. & Lewin, D. (1997). Consistent hashing and random
  trees: distributed caching protocols for relieving hot spots on the World Wide Web. *Proc. 29th ACM STOC*, 654–663.
  doi:10.1145/258533.258660
- Klein, F. (1871). Ueber die sogenannte Nicht-Euklidische Geometrie. *Mathematische Annalen* 4(4), 573–625.
  doi:10.1007/BF02100583
- Knight, F. B. & Meyer, P.-A. (1976). Une caractérisation de la loi de Cauchy. *Zeitschrift für
  Wahrscheinlichkeitstheorie und verwandte Gebiete* 34, 129–134.
- Knight, F. B. (1976). A characterization of the Cauchy type. *Proceedings of the American Mathematical Society* 55(1),
  130–135. doi:10.2307/2041858
- Koenderink, J. J. & van Doorn, A. J. (1982). The shape of smooth objects and the way contours end. *Perception* 11(2),
  129–137. doi:10.1068/p110129
- Koenderink, J. J. (1984). What does the occluding contour tell us about solid shape? *Perception* 13(3), 321–330.
  doi:10.1068/p130321
- Kosloff, D. & Tal-Ezer, H. (1993). A modified Chebyshev pseudospectral method with an O(N⁻¹) time step restriction.
  *Journal of Computational Physics* 104, 457–469. doi:10.1006/jcph.1993.1044
- Lamping, J., Rao, R. & Pirolli, P. (1995). A focus+context technique based on hyperbolic geometry for visualizing large
  hierarchies. *Proc. CHI '95*, 401–408. doi:10.1145/223904.223956
- Lang, S. (1997). *Undergraduate Analysis*, 2nd ed., §IV.2. Springer. doi:10.1007/978-1-4757-2698-5
- Letac, G. (1977). Which functions preserve Cauchy laws? *Proceedings of the American Mathematical Society* 67(2),
  277–286. doi:10.1090/S0002-9939-1977-0584393-8
- Lévy-Leblond, J.-M. (1980). Speed(s). *American Journal of Physics* 48(5), 345–347. doi:10.1119/1.12093
- Mallat, S. G. (1989). A theory for multiresolution signal decomposition: the wavelet representation. *IEEE TPAMI*
  11(7), 674–693. doi:10.1109/34.192463
- Mardia, K. V. & Jupp, P. E. (2000). *Directional Statistics.* Wiley.
- McCullagh, P. (1992). Conditional inference and Cauchy models. *Biometrika* 79(2), 247–259.
- McCullagh, P. (1996). Möbius transformation and Cauchy parameter estimation. *Annals of Statistics* 24(2), 787–808.
  doi:10.1214/aos/1032894465
- Mendonça, P. R. S. & Lundell, B. (2025). Explicit formulae for projectively transformed Cauchy distributions with
  applications. *Statistics & Probability Letters* 222, 110393. doi:10.1016/j.spl.2025.110393
- Mermin, N. D. (1979). The topological theory of defects in ordered media. *Reviews of Modern Physics* 51, 591.
  doi:10.1103/RevModPhys.51.591
- Microsoft. Bing Maps Tile System. https://learn.microsoft.com/en-us/bingmaps/articles/bing-maps-tile-system
- Nagel, T. (1986). *The View from Nowhere.* Oxford University Press.
- Nakatsukasa, Y., Sète, O. & Trefethen, L. N. (2018). The AAA algorithm for rational approximation. *SIAM
  Journal on Scientific Computing* 40(3), A1494–A1522. doi:10.1137/16M1106122
- Navas, S. et al. (Particle Data Group) (2024). Review of Particle Physics, §49 Kinematics. *Physical Review D* 110,
  030001. (A 2026 edition exists: Takahashi, F. et al., *Int. J. Mod. Phys. A* 41, 2630011.)
- Oblak, B. (2015). From the Lorentz group to the celestial sphere. arXiv:1508.00920.
- Penrose, R. (1959). The apparent shape of a relativistically moving sphere. *Proceedings of the Cambridge
  Philosophical Society* 55(1), 137–139. doi:10.1017/S0305004100033776
- Perlin, K. & Fox, D. (1993). Pad: an alternative approach to the computer interface. *Proc. SIGGRAPH '93*, 57–64.
  doi:10.1145/166117.166125
- Phillips, P. C. B. (1989). A new proof of Knight's theorem on the Cauchy distribution. Cowles Foundation Discussion
  Paper 887.
- Pitman, E. J. G. & Williams, E. J. (1967). Cauchy-distributed functions of Cauchy variates. *Annals of Mathematical
  Statistics* 38(3), 916–918. doi:10.1214/aoms/1177698885
- Prince, J. L. & Willsky, A. S. (1990). Reconstructing convex sets from support line measurements. *IEEE TPAMI* 12(4),
  377–389. doi:10.1109/34.50623
- Ratcliffe, J. G. (2019). *Foundations of Hyperbolic Manifolds*, 3rd ed., Graduate Texts in Mathematics 149. Springer.
  doi:10.1007/978-3-030-31597-9
- Reach, A. M. & North, C. (2018). Smooth, efficient, and interruptible zooming and panning. *IEEE TVCG*.
  doi:10.1109/TVCG.2018.2800013; arXiv:1801.09358
- Rhodes, J. A. & Semon, M. D. (2004). Relativistic velocity space, Wigner rotation, and Thomas precession. *American
  Journal of Physics* 72(7), 943–960. arXiv:gr-qc/0501070
- Rindler, W. (1966). Kruskal space and the uniformly accelerated frame. *American Journal of Physics* 34(12),
  1174–1178.
- Robb, A. A. (1911). *Optical Geometry of Motion: A New View of the Theory of Relativity.* Cambridge: W. Heffer & Sons.
- Sarkar, M. & Brown, M. H. (1992). Graphical fisheye views of graphs. *Proc. CHI '92*, 83–91.
  doi:10.1145/142750.142763. Journal version: Graphical fisheye views. *Communications of the ACM* 37(12) (1994),
  73–83. doi:10.1145/198366.198384
- Schleimer, S. & Segerman, H. (2016). Squares that look round: transforming spherical images. *Bridges 2016*.
  arXiv:1605.01396
- Stigler, S. M. (1974). Studies in the history of probability and statistics. XXXIII. Cauchy and the witch of Agnesi:
  an historical note on the Cauchy distribution. *Biometrika* 61(2), 375–380. doi:10.1093/biomet/61.2.375
- Tee, T. W. & Trefethen, L. N. (2006). A rational spectral collocation method with adaptively transformed
  Chebyshev grid points. *SIAM Journal on Scientific Computing*. doi:10.1137/050641296
- Terrell, J. (1959). Invisibility of the Lorentz contraction. *Physical Review* 116(4), 1041–1045.
  doi:10.1103/PhysRev.116.1041
- Thomas, L. H. (1926). The motion of the spinning electron. *Nature* 117(2945), 514. doi:10.1038/117514a0
- Trefethen, L. N. (2019). *Approximation Theory and Approximation Practice*, extended ed., ch. 2. SIAM.
- van Wijk, J. J. & Nuij, W. A. A. (2003). Smooth and efficient zooming and panning. *Proc. IEEE InfoVis 2003*,
  15–22. doi:10.1109/INFVIS.2003.1249004. Extended: A model for smooth viewing and navigation of large 2D
  information spaces. *IEEE TVCG* 10(4) (2004) (pages and DOI to confirm).
- Varićak, V. (1910). Anwendung der Lobatschefskijschen Geometrie in der Relativtheorie. *Physikalische Zeitschrift*
  11, 93–96.
- Weiss, M. Can you see the Lorentz–Fitzgerald contraction? Or: Penrose–Terrell rotation. *Usenet Physics FAQ*.
  https://math.ucr.edu/home/baez/physics/Relativity/SR/penrose.html (not peer reviewed)

Added with the prior art on octave browsers (Sep 23):
- Whewell, W. (1849). On the intrinsic equation of a curve, and its application. *Transactions of the Cambridge
  Philosophical Society* 8, 659–671.
- Wigner, E. (1939). On unitary representations of the inhomogeneous Lorentz group. *Annals of Mathematics* 40(1),
  149–204. doi:10.2307/1968551

Added after the novelty searches (Sep 23; details from publisher or index pages where reachable, otherwise from
search listings):
- Williams, L. (1983). Pyramidal parametrics. *Computer Graphics* (Proc. SIGGRAPH '83) 17(3), 1–11.
  doi:10.1145/800059.801126

### Citation status

Checked by search on Sep 23 2026 against publisher pages, Crossref, dblp and secondary bibliographies. Not fully
confirmed:
- **Borel 1913**: which of the two notes carries which result, their titles, and their end pages.
- **Ratcliffe**: the book covers the isometries of the hyperbolic plane and the hyperboloid model; no theorem number
  for SO⁺(2,1) ≅ PSL(2,ℝ) was checked.
- **Hatcher**: the RP¹ statement is standard; no page was checked.
- **Johnson, Kotz & Balakrishnan**: chapter confirmed, page not.
- **Lévy-Leblond 1980**: citation confirmed; its text was not read.
- **McCullagh 1996**: confirmed through secondary sources; the paper itself did not load.
- **Whewell 1849**: "On" or "Of" in the printed title is not confirmed.
- **Stigler 1974**: Cauchy's name comes from his 1853 papers in the dispute; the naming itself came later.
- **Octave-browser prior art**: van Wijk & Nuij 2004's pages and DOI; which earlier model Reach & North credit as
  hyperbolic (probably van Wijk & Nuij 2004, not confirmed); Perlin & Fox and Williams quoted only through secondary
  sources.
- **Boyd**: the 1987 abstract was read (the map y = L cot t onto [0, π]); the formula TB_n(y) = cos(n arccot(y/L))
  was read in a later paper (arXiv:1703.07441, J. Comput. Phys. 2017), not in Boyd's text. The book's Dover year is
  from memory; the ebook listing shows 2013.
- **§6.1c prior art**: Boyd 1982's volume and pages are from the ADS code (1982JCoPh..45...43B), the end page
  from memory; its formulas were not read. Tee & Trefethen 2006's volume and pages were not checked. Cueto-Felgueroso
  & Juanes 2009's volume was not recorded. Alexandrescu et al.: the journal year is from the ScienceDirect listing,
  not checked.
- **Added Sep 23**: McCullagh 1992 (DOI not checked); Phillips 1989 (content via its abstract); Dunau & Senateur 1987
  (title not confirmed); Fernández-Durán & Gregorio-Domínguez 2025 (title not recorded); Trefethen (edition year to
  confirm). Several full texts could not be opened.
