# The Cauchy, Inside and Out

### The order of limits: fixed fidelity, unknown N, and the horizon two readers share

*Research paper and session record. Unreviewed. Title provisional. Sep 22 2026.*

*Revised 1 October 2026: the text is left as it was, and notes marked* **(1 Oct)** *say where the rulings of 30 September – 1 October (R124–R152 of* Reader Geometry as Addressing*) bear on it. The measurements and the array and stitch mathematics stand; the frame (three scenarios, inside/outside, "everywhere", density, the old g, arctan as the sweep, the reader as the unit circle) is superseded; the section "The dynamic array is a freedom" closely anticipates situation 3.*

> **(1 Oct) How to read this paper now.**
> - **The situations** (R137, R146, R151, R152). (1) The circle: both breadths known and equal; the view from nowhere. (2) Every other shape: breadths known, varying with direction; also a view from nowhere. (3) The fisheye: h's breadth known (h is the known side by definition), v's not, so v is had only as a count of h's; the only view from somewhere, and the only situation with a reader in it, serial or parallel. (4) Neither known: impossible. (5) v's breadth known approximately. Not exhaustive.
> - **Home, the corner and the horizon belong to situation 3 only**; the circle and other known shapes have none (R131, R139). A known list or shape read through the fisheye is situation 1 or 2 read as if v's breadth were unknown: a simulation of situation 3 (R143).
> - **The corner and the two sides** (R149–R150, R152). The corner is known in situation 3, where v reaches one h. The front side, home to the corner, is swept from home in plain proportion and is the **working horizon**; the corner is its edge. The back side, past the corner, is counted by doublings. The parallel reader keeps v on the front side only.
> - **Arctan** is an index into the turn, a shortcut, not the sweep (R148). **The reader is not the unit circle** (R127).
> - **Names now in use.** "Fulcrum" → **the corner**; "the view from everywhere" → **the view from nowhere**; "inside/outside" → **serial/parallel**; "density" is dropped as a framework word (the Cauchy's probability density keeps its name). Quotes keep their wording.

*Scripts:* `outside.mjs`, `join.mjs`, `sameh.mjs`, `bothsides.mjs`, `repair.mjs`, `ceiling.mjs`,
`rotate.mjs`, `godseye.mjs`, `serialpos.mjs`, `towercheck.mjs`, `gceiling.mjs`, `dynarray.mjs`, `landmark.mjs`, `freedom.mjs`, `finished.mjs`, `window.mjs`, `dialphysics.mjs`; carried forward from the companion, `serial.mjs` and
`serial2.mjs`.
*Draws on the day's notes:* `the-outside-hemisphere.md`, `inside-plus-outside.md`, `both-sides.md`,
`serial-inside-outside.md`.
*Companion to* `the-fisheye-as-a-lens.md`. Its lens, grain, local count, unwithdrawn verdicts, order-keeping
and signed-move results are carried into §0.1, §0.1a, §0.2, §0.4, §2.2 and §7. From *The Centring* (Sep
17–18), the following are carried into §0.1b, §0.3, §0.4, §4, §5.1 and §7:
- the residue field and the circle as the figure whose field is trivial;
- the circle as the fixed point of the own-size reading;
- the lap product as a check on the reader;
- form without size;
- the enclosed and outside images;
- the arch's feet.

From *Browsing the Fisheye*, the following are carried into §0, §0.1a, §0.1b, §0.2, §2.1, §3.2 and §4.3:
- the position reader against the motion reader;
- the two ways to form a pair;
- whose "both" is whose;
- the two absences;
- carried against laid marks;
- the uniform address space;
- the two routes to the corner;
- "denser, never larger" against the ceiling;
- the confound.

From *The Unit Rule* (Aug 21, an older paper), the following are carried into §0.1, §0.1a, §0.1b, §0.2,
§0.4, §4.1, §5.1 and §7:
- the capability stack;
- the corner crossing as a route to the corner;
- continuity as the reader's own;
- the silent circle;
- the founding of the hold;
- the guard on "absolute";
- the two checksums;
- the record as a projection that does not drift.

From *Degrees of Freedom* §3.1, §5.10 and §5.12a (the centring; how freedoms scale, formerly the tower of
holds), §4.4 tests the stitch as a two-group tower.

*The Unit Rule*'s vocabulary is updated as it comes in:

| *The Unit Rule* says | this paper says | why |
|---|---|---|
| the screen, the broadcast | the reader, the writer | the corpus's current terms |
| its "fulcrum" | **the corner** (v = h) | this paper's term for the relation's equality |
| its "corner", the frame where the arrival equals the hold | **a corner crossing** | an event the reader notices, as distinct from the corner itself |
| its step *g* | **the step** | *g* is now the grain (*Degrees of Freedom* ruling 11) |
| its symbols | the record's moves | the corpus's current terms |
| the rail, the clip | the horizon | the corpus's current terms |

---

**This paper takes a fresh look at classical ideas related to the Cauchy, and breaks them down using inside
and outside vocabulary.**

The ideas are all old:
- the Cauchy's missing mean;
- its average being the same law at every N;
- the arcsine and Gaussian laws of a projection;
- the rim, and the fold at the rim;
- depth from foreshortening;
- the intrinsic equation;
- the turning tangents.

What is new is the sorting. Each idea is assigned to one of three views:
- **the view from everywhere** (the classical view, which holds N);
- **the outside reader** (parallel, holding one side);
- **the inside reader** (serial, receiving the other side).

Neither real reader knows N, and neither needs it. Sorted this way, the classical results turn out to be
what the two real readers see, stitched at the horizon they share.

**The paper at a glance.** The readers here are in their default pairing: outside and parallel, inside and
serial. §2.0 and `serial-inside-outside.md` separate position from verb.

| | outside | inside | the view from everywhere |
|---|---|---|---|
| stands to the shape | in front of it | surrounded by it | holds the whole |
| verb | walks: parallel, iterative | points: serial, projective | resolved |
| primitive | position and gap, **v** | direction and move, **v/h** | the complete list |
| count it holds (§0.1a) | V, or V_ε at its fidelity | M, local to one eighth of a closure | N |
| lens (§2.2) | dv = h: **crowds** at the horizon | dz = 1/(vh): **spreads** at the horizon, slowest at the corner | none |
| runs out of, at the horizon (§2.0) | distance | direction | nothing |
| blind first, at fixed fidelity (§3.3) | the horizon; the band grows with N | the corner (grain) and the far reach (fixed share) | nowhere |
| law found in its list (§0.2) | arcsine (2D), flat (3D) | Cauchy, **but finding the law is everywhere's act**; the reader has the lens | the classical law, with the order discarded |
| needs N? | no | no | yes |
| holds closure? (§0.4) | no: two of the four sweeps | no: two sweeps; keeps the facing by its signed move, not the tally | yes |
| breadth and density (§1.1) | half the closure; fixed fidelity | half the closure; fixed grain and reach | **both infinite**: no horizon, every hanger resolved |

**Glossary.** One line per term, grouped by what it names.

| term | means | where |
|---|---|---|
| *the relation* | | |
| **h, v** | the two components of one relation, arriving together; neither privileged | throughout |
| **the hold** | v² + h² = 1: the pair against its own size | §2 |
| **the reading** | s = v/h; its log register z = ln(v/h) | §2.2 |
| **home, the corner, the horizon** | h = 1 (facing); v = h; h = 0 (edge-on) | §2 |
| **the sweep** | a bar of 1 turning from horizontal to vertical: 0 to π/2, every relation of h and v | §0.3 |
| **closure** | four sweeps: H → V → H → V → H | §0.4 |
| **the quarter turn** | [0, π/2]: angular, N known, no infinity | What an array is |
| **the freedom** | [0, ∞): the readings; N unknown; has a horizon | What an array is |
| *the readers* | | |
| **the view from everywhere** | the classical view: holds N and the whole list; infinite breadth and density | §1.1 |
| **outside reader** | in front of the shape; parallel; **walks**; holds positions v and their gaps | §2.0 |
| **inside reader** | surrounded by the shape; serial; **points**; holds directions and moves | §2.0 |
| **serial, parallel** | the verb: one at a time, or all at once. Default pairing inside/serial, outside/parallel; position and verb can be separated | §2.1 |
| **the lens** | how a reader's spacing runs: outside dv = h (crowds at the horizon); inside dz = 1/(vh) (slowest at the corner) | §2.2 |
| *the counts* | | |
| **N, V, V_ε, M** | the whole closure's; the outside hemisphere's; what the outside tells apart at ε; the serial reader's, between two landmarks | §0.1a |
| **ε** | a reader's fidelity: the smallest difference it tells apart | §3 |
| **the grain** | the serial reader's step size | §3.3 |
| **g** | the density dial: the share of hangers placed (or evaluated) | §1.1 |
| **tally, mean, law** | whole-list statistics; everywhere's acts, since they need N | §0.2 |
| *the construction* | | |
| **hangers, the scaffolding, the frame** | the evenly placed positions; in an array, the indexes | What an array is |
| **stones** | what hangs on the hangers; in an array, the values a reader fetches; in a shape, the magnitudes the outside reader reads | What an array is |
| **array** | a list on **one quarter turn**: not a shape; no closure, no facing, no sides | What an array is |
| **the stitch** | joining the two readers' sides at the horizon to rebuild the shape without N | §4 |
| **the repair** | taking the outside's hidden near-horizon steps from the inside side, by the fidelity rule | §5 |
| **the two checksums** | the order-blind sum (closure) and the order-bearing landmark sequence; neither catches a balanced loss | §0.4, §5.1 |
| **landmarks** | horizons, homes and corners along a closure: eight on a convex one | §5.1 |

## What an array is

> **(1 Oct)** Arctan is not the sweep (R148). It is a shortcut that makes a sweep act like an index, and its 2/π divides by the whole turn out to a horizon that is never seen. Read every arctan here as that shortcut; sweeps are swept from home.

> *"An array has no horizon, its length is known."* (Tom, Sep 22)

> *"An array is not a shape, it does not close, it has no facing, it is just one quarter turn."* (Tom, Sep 23)

The most concrete way into everything that follows is an ordinary array of data. **It is not a shape.**
- **It does not close.** A closure is four sweeps (§0.4). An array is one.
- **It has no facing.** Nothing in it turns towards or away from a reader. So there is no outside hemisphere
  and no inside hemisphere, no limb, and no second side to stitch.
- **It is just one quarter turn.** Everything below that is true of arrays is true of one sweep, from home to
  the far end.

**An array is a quarter turn with its N established.** Lay N entries uniformly on [0, π/2], so that entry i sits
at angle θᵢ = (π/2)·(i/N).
- **The indexes are the scaffolding:** the hangers, evenly placed, with g = 1. That is the frame.
- **The values are the stones:** what hangs on each hanger. They are what a reader fetches at an address.
- **Its length is known, so it has no horizon.** The last entry sits just short of π/2, at a finite place.
  This is the horizon ruling read backwards: *any time there is a horizon, N is unknown* (Tom, Sep 22), so
  where N is known there is no horizon.

**The two conversions are the everywhere equation, run as a round trip.**
- **Index to angle:** θ = (π/2)·(i/N). The share of the array becomes turn.
- **Reading to index:** θ = arctan(s), then i/N = (2/π)·θ. The turn becomes a share of the array.
- **Round and back is π/2 · 2/π = 1** (§0.3). π/2 takes a share to a turn, a breadth. 2/π takes a turn back to
  a share, a density (§1.1).

**What each reader gets from the array.**
- **The inside reader** gets a reading s. arctan and 2/π turn it into i/N: how far along, as a share. That is an
  address, and it is N-free. It never gets the index, because i/N becomes i only with N, and **only the array
  has N.**
- **The reading says where; the array says which; the value there is the stone.** This is *Browsing the
  Fisheye*'s "given the direction, which magnitude was it?", with the conversion written out.
- **What survives of the two readers is the verb, not the side.** Pointing is fetching by a reading: random
  access. Walking is stepping through the indexes in order: iteration. Both work on one quarter turn. What
  does not carry over is the pair of sides: with no facing, there is no half the outside reader holds and no
  half the inside reader receives.

**Where the horizon goes.** The array has none. It appears only in the reading: as i approaches N, θ approaches
π/2 and s = tan θ runs off without bound.
- **The array is the resolved account**, bounded at both ends. (Bounded, not closed: it does not come back
  round.)
- **The reading is the unresolved one**, open at the far end.
- arctan carries the open reading onto the bounded array, and tan carries it back.

**Two objects, kept apart** (Tom, Sep 21):
- **The quarter turn** is angular, symmetric, has N known and has no infinity. **The array is laid on it.**
- **The freedom**, [0, ∞), has N unknown and a horizon. **The readings live on it.**
- arctan and tan are the bridge between them. They carry points across without making the two objects one.

**By the Sep 22 ruling, the static array is everywhere's object.** It holds N and the whole list at once. A
real reader gets a share, with no N, and whatever stone stands at the share. It does not get "half the
stones": with no facing there are no halves.

### Static and dynamic arrays

> *"I wonder if the dynamic array would be the N is not known situation, the freedom."* (Tom, Sep 22)

The array above is **static**: its length is fixed before it is laid down. A **dynamic** array, one that grows
at its end, has no length to lay against. It cannot go on the quarter turn by share, because the share i/N has
no N. **It goes on the freedom instead**, one entry per step of a unit c: sᵢ = i/c, θᵢ = arctan(i/c).

| | static array | dynamic array |
|---|---|---|
| N | known | unknown |
| laid on | the quarter turn, θᵢ = (π/2)(i/N) | the freedom, sᵢ = i/c, θᵢ = arctan(i/c) |
| hangers | uniform | Cauchy-spaced, crowding toward π/2 |
| horizon | none | yes: the end not yet arrived |
| address | a share i/N, which moves when N changes | an absolute place, fixed for good |
| spends | N | a unit c |

**The dynamic array is the corpus's own situation.** It is the reader's side of the two objects above, the
freedom, with N unknown and a horizon. The static array is everywhere's. The two layouts are the two objects,
each holding a list.

**The addresses correspond to *Browsing*'s two kinds of angle.** The static address is **relative**: a share
of whatever the length is, so the same entry moves when the array grows. The dynamic address is **absolute**:
arctan(i/c) involves no N, so an entry keeps its angle however long the array becomes. Measured
(`dynarray.mjs` D3, c = 100, entry 250): the dynamic angle stays at 1.1903 as the array goes from 500 to 2000
entries, while the static angle halves each time, 0.785 → 0.393 → 0.196.

**The trade: the dynamic array spends a unit where the static one spends N.** Something has to fix the
spacing. The static array takes it from its length. The dynamic array cannot, so it takes a unit c, the number
of entries that fill the run from home to the corner (i = c is where θ = π/4). This is the Unit Rule's point,
moved to arrays: a reader with no N still needs a unit.

**The newest entries sit at the horizon, and they are where a fixed-fidelity reader loses them.** The spacing
between neighbours is θᵢ₊₁ − θᵢ ≈ c/(c² + i²), which is c/i² once i is well past c. It shrinks as the array
grows, so at fidelity ε the entries stay distinct only while c/(c² + i²) > ε:

- **Distinct up to i ≈ √(c/ε − c²).** Measured (`dynarray.mjs` D1–D2, ε = 10⁻³): the first merge is at
  i = 99 for c = 10 (predicted 99.5) and at i = 300 for c = 100 (predicted 300).
- **The widest gap is at home, 1/c.** If c > 1/ε, even the first entries merge (c = 1000 merges from i = 1).
- **The largest distinct run is about 1/(2ε)**, at c = 1/(2ε): 500 entries at ε = 10⁻³. This is derived from the
  formula above, not run separately.
- **So in a growing array the fisheye puts the newest data at the limb**, and past a point a fixed reader sees
  it only as a crowd at the edge. That is the §3 ceiling, arrived at from the list's side: more entries, the
  same number seen.

**What this does to the practical application below.** The claim that growth changes no address holds **only
on the freedom layout**. On the quarter turn every address is a share, and growth moves every entry. The two
layouts pay differently: the static one re-addresses when N changes and has no horizon; the dynamic one never
re-addresses and has a horizon, where its newest entries crowd.

### The dynamic array is a freedom

> **(1 Oct)** This is close to R146 and R149, nearly word for word. v is a count of h's (here, entries counted in the unit c). The corner is where v reaches one h; home to the corner is plain proportion (the front side, the working horizon), and past it the doublings are counted (the back side). The static/dynamic split, N known or not, is R143: situation 3 is situation 2 with v's breadth unknown.

> *"The dynamic array is a freedom is an interesting mapping. Let's explore."* (Tom, Sep 22)

Read sᵢ = i/c in the corpus's own terms and the mapping is exact, not an analogy: **v is the count, h is the
unit.** Each entry is the relation of how many have arrived to the unit they are counted in. Everything the
freedom has, the growing array has. (`freedom.mjs`; F1–F3 below are identities checked numerically, not
experiments.)

| the freedom | the dynamic array |
|---|---|
| v | the count so far, i |
| h | the unit, c |
| the reading s = v/h | the entry's address, i/c |
| home, s = 0 | the first entry |
| the corner, v = h | entry c: the count has reached its unit |
| the horizon, h → 0 against v | the end that has not arrived |
| the sweep, a bar turning from horizontal to vertical | **the array growing**: its frontier at θ = arctan(n/c) |

**Growth is the sweep, and it never finishes.** With n entries in, the frontier sits at arctan(n/c). Each
arrival turns the bar a little further towards vertical, by less each time, and it never gets there. A static
array is a sweep already completed: its N is known, and it fills the quarter turn. A dynamic array is a sweep
in progress. This is Tom's sweep visual (§0.3) with the list as the thing that turns.

**Arrived and unarrived are a ratio and its swap.** The part of the quarter turn behind the frontier is
arctan(n/c). The part ahead of it is arctan(c/n): the swapped reading. They always add up to π/2 (F1, to
2×10⁻¹⁶). So at every moment the array divides the quarter turn into its past and its future, and **the
future's reading is the past's reading swapped.** The corner is the moment they are equal: n = c, half the
turn behind and half ahead. This is the same shape as the everywhere equation (§0.3), a ratio times its swap,
met here as time: what has arrived against what has not.

**At fixed fidelity, a growing array comes to look finished.** A reader of fidelity ε passes through three
regimes (F2, c = 100, ε = 10⁻³):

| entries n | what the reader sees |
|---|---|
| n < √(c/ε − c²), here 300 | every entry distinct |
| 300 < n < c/ε, here 100 000 | the newest entries merge into a crowd, but the frontier still stands visibly short of the horizon |
| n > c/ε | **the unarrived part, arctan(c/n) ≈ c/n, is below ε. The frontier cannot be told from the horizon, and the array looks complete** (narrowed in the next subsection: the reader loses n, not the kind of list) |

The count of distinct entries stops at 300 while n goes on to a million. That is the §3 ceiling again. The
third regime adds something new: **a fixed-fidelity reader sees a growing list turn into a finished one.**
The static array (everywhere's object, N known, no horizon) shows up as what a real reader sees of a dynamic
array long enough to hide its own frontier. That is the order of limits met in a list. In the classical order,
ε → 0 first, the frontier stays visible for ever, and the array is never mistaken for finished. At fixed ε, the
horizon closes over it at n = c/ε.

**The unit c matters in one register only** (F3).
- **Log register**, z = ln(i/c) = ln i − ln c: changing c slides every address by the same amount. Distances
  between entries are c-free (3.218876 at c = 100 and at c = 7). This is the ratio move: entries i and 2i
  are always the same distance apart, the octave.
- **Angle register**, θ = arctan(i/c): changing c moves the corner, and distances change (1.1760 against
  0.3227).
- So the unit is invisible to a reader using ratios, and only fixes *where the corner is*. The Unit Rule's
  point again: the unit is needed for the corner, not for the form.

**Absolute addresses force the crowding onto the new end.** The quarter turn is bounded and the list is not.
Any layout that gives every entry a fixed angle for good must fit unboundedly many entries into a finite
turn, so the spacing must shrink towards the unarrived end. Arctan is one such layout. Every layout with fixed
addresses pays this way.
- **The consequence:** with fixed addresses, the *oldest* entries get the resolution and the *newest* crowd.
- To resolve the newest instead, address entries by age, n − i, counted back from the frontier. But age
  changes with every arrival, so those addresses are relative and move. That is the static layout's price
  again.
- **So a reader of a growing list chooses between fixed addresses and a resolved present.** Arctan does not
  impose that choice. It comes from laying an unbounded list on a bounded turn.

### When a growing array looks finished

"Looks finished" (above) needs narrowing first. **What a fixed-fidelity reader loses is the present count n,
not the kind of list.** The spacing still gives the layout away at any length. Sampled across the array, the
dynamic layout's gaps shrink by a factor of 10⁵ from home to the frontier, while the static layout's are
equal (P2). So the reader can always tell a growing layout from a finished one. It cannot tell how long the
growing one is, or whether it has stopped. (`finished.mjs`; predictions registered before the run; P5 was
added after P3 and registered before its own run.)

| test | result |
|---|---|
| **P1** the reader estimates n from the frontier's angle, n = c·tan θ, with θ known to ε; the relative error should be about εn/c | **confirmed**: mean relative error 2.5×10⁻³, 2.6×10⁻², 0.117 and 0.260 at n = 10³, 10⁴, 5×10⁴ and 10⁵, against εn/(4c) = 2.5×10⁻³, 2.5×10⁻², 0.125 and 0.25 (c = 100, ε = 10⁻³; a quarter of the step because rounding to the nearest ε averages ε/4) |
| **P2** the spacing tells the layouts apart at any n | **confirmed**: first/last gap ratio 1.5×10⁵ dynamic, 1.000 static, at n = 2×10⁵ |
| **P3** re-uniting: double c whenever n passes 4c | **confirmed**: 16 rescales up to n = 2×10⁶. Each moves every address in the log register by the **same single number**, ln 2 (equal to 10⁻¹²). Between rescales no address moves. The frontier stays between arctan 2 and arctan 4 |
| **P3′** re-uniting keeps n, not the newest entries | **confirmed**: the newest entry stops being distinct once c > 1/(5ε) (first lost at c = 320) |
| **P4** c = n, re-uniting on every arrival, is a relative layout | **confirmed**: entry 250 moves 0.245 → 0.124 → 0.062 as n doubles: the static array's behaviour, with arctan in place of the linear share |
| **P5** the re-united array holds n to a fixed relative error for ever, at most (1 + s²)/s · ε/2 ≈ 2.1×10⁻³ for s in [2, 4] | **confirmed**: worst 2.12×10⁻³ up to n = 5×10⁶ (predicted 2.13×10⁻³). With c fixed at 100, the worst is 1.0: n is lost |

**The largest count a reader can name is about c/ε.** With c fixed, the estimate stops at 125 577 (c = 100,
ε = 10⁻³): the last angle short of π/2 that the reader can tell apart. Every longer array gets the same
estimate. It has the same form as the shape's parallel ceiling (§3.2, εN = 2π), with the unit in place of
the turn: **εn/c = 1.** Same form, different cause: the shape's ceiling comes from its facing (the limb
crowds in projection), and an array has no facing. Here it comes from the one quarter turn itself filling up
towards π/2.

**Re-uniting holds the count as floating point.** After k doublings the reader holds n as
n = c₀ · 2ᵏ · tan θ:
- the **exponent** is k, the number of rescales;
- the **mantissa** is the frontier's reading, kept between 2 and 4.

The precision is relative and constant: 2.1×10⁻³ at n = 10³ and at n = 5×10⁶. Each rescale is **one
number carried across the whole array**, a shift of ln 2 in the log register. It is the same kind of object
as the tower's cross-group residue (§4.4): one ratio of units. But it is not the stitch's scale (§4.2). The
stitch carries a scale between two sides of a shape, and an array has one side. The unit is
re-chosen so that the frontier never reaches the horizon, and the cost is one number per octave.

**Whatever the layout, a fixed-fidelity reader holds about 1/ε distinct things. The layout only decides
which.**

| layout | what stays resolved | what is lost |
|---|---|---|
| fixed c (absolute addresses) | the oldest entries, up to √(c/ε − c²); at most about 1/(2ε) | the newest entries, and past c/ε the count |
| re-united c (addresses shift one number per octave) | the count, to constant relative precision | the newest entries, once c > 1/(5ε) |
| by age, n − i (relative addresses) | the newest entries | fixed addresses: everything moves on every arrival |

The ~1/ε budget is the same as §1.1's cap (1122 distinct points at ε = 10⁻³, whatever N). No layout raises
the budget; a layout only spends it. **A growing list never loses its addresses. What runs out is the
reader's resolution** (§3.2's "the address never overflows; the resolution does", now in a list).

**From the second review of the arrays (Sep 22): two things taken, three corrected.**

*Taken:*
- **"N unknown" stated plainly: every completion agrees with the prefix.** A reader that has met entries 0 to
  n holds the same record whether the array stops at n, at 80 000, or never. So N is not in the data seen.
  It belongs to the completed account, which is everywhere's (§0.1). The dynamic reader is not holding a
  defective copy of the static array. It has a different kind of access to the same entries.
- **There is no out-of-range.** A static array has a last index, and an address past it is an error. On the
  freedom every reading s in [0, ∞) is a valid address, entry c·s. An address past the frontier is not an
  error but **not yet**: the entry has not arrived. So the horizon is not "nothing beyond here" but "the
  extent beyond here cannot be established".

*Corrected:*
- **The dynamic address is not "local".** The review has it built from the reader's local relation to the
  next entries. It is not: arctan(i/c) is the count against a **unit**, and the unit is one global number the
  whole layout shares. The static address spends N; the dynamic one spends c. Neither is free. The review
  also calls i/N the absolute address; in this paper i/N is the **relative** one (a share, which moves with N)
  and arctan(i/c) is the absolute one (§ Static and dynamic arrays).
- **The horizon is the layout's; the loss is the reader's.** The review puts the horizon with the observer.
  But the dynamic layout has a horizon at ε = 0 as well: π/2, the end that never arrives. What belongs to the
  reader is *where it stops resolving*: the newest entries past √(c/ε), and the count past c/ε. The freedom
  owns the horizon. The fidelity decides how much the horizon hides.
- **Supplying N gives everywhere's breadth, not its density.** The review says the view from everywhere "is what bounded
  observation becomes when the missing extent is supplied". Half right. With N supplied, the conversion to
  the classical address is one number, i/N = (c/N)·tan θ, and the data do not change. But a reader of fixed ε
  with N in hand is still blind past about π/(2ε) uniform entries. The view from everywhere is **infinite breadth and
  infinite density** (§1.1). Supplying N gives the first; only ε → 0 gives the second. And the view from everywhere remains
  one of the three scenarios by Tom's ruling, not a reader that the others become.

### An index has no unit to change

> *"This number is so big. If it were cm, or meters or miles, then it could be simplified to a new scale. But
> this is indivisible: it is indexes that have no scale."* … *"The first instinct is to create a larger unit.
> That's why we have mm, cm, meters, miles, so many types of units. This gets too large, just create a larger
> unit. You can't do that with actual things that exist."* (Tom, Sep 23)

**A magnitude has a unit, and a unit can be changed.** Nine quadrillion centimetres is ninety billion kilometres.
Changing the unit is the ratio move, a dilation of the reading: the number shrinks and nothing is lost, because
a magnitude only ever meant "so many units". That is why there are so many units, from millimetres to miles: when
a number gets too large, the first instinct is a larger unit. Floating point is that instinct built into the
machine: about sixteen significant digits and an exponent, with the exponent carrying the scale.

**An index has no unit to change.** Its only unit is one entry, and an entry cannot be divided or merged. Record
4,536,507,171,109,588 and its neighbour differ by exactly one, and that one matters as much as the top digit,
because it is a different thing. There is no "kilo-record" that shrinks the number and keeps what it names:
grouping a thousand records into one throws away which record was meant. **Every digit of an index is
load-bearing; the low digits of a magnitude are rounding.** In h and v: for an index v is the count and h is one
entry, and h is the one thing that may not be changed.

**What things get instead of a larger unit is a level.** A crate of twelve eggs is still twelve eggs; the crate is
not a larger egg, it is a new level of the address: crate, then egg. Shelves, aisles, buildings and streets do the
same. Units of magnitude compose by multiplying and discarding; levels of an address compose by nesting and keep
everything. That is the dial's tower: the bits are levels, and the radius chooses which level the hand steers,
without rescaling the address. A calendar is the same kind of thing for a count of moments: years, days and
seconds are levels of an address, not units of a magnitude ("milliseconds do not have leap days; calendars do",
the reader-geometry note).

**Why the dial's N is 2⁵³ − 1.** A double carries a 53-bit mantissa. For a magnitude that is sixteen digits of
relative precision, more than any measurement needs. For an index it is the last integer the double holds exactly;
past it, neighbouring records cannot be told apart. The dial's N sits exactly where magnitudes stop caring and
indexes run out.

**What this sharpens from the growing array.** Re-uniting holds the count as floating point, to about 0.2 %
relative error (§ When a growing array looks finished, P5). That is the magnitude's view of a count, "about how
many", and it is enough for that. It is useless for "which one". So the dial keeps both, and keeps them apart:
- **the radius is a scale**, the log register, for navigating: one gesture spans any size;
- **the digits are the address**, integers, where nothing may be rounded.

"You can't do that with actual things that exist": the things are the entries, and an entry is the one unit that
does not rescale.

### The logarithm: a unit of a different kind

> *"Right, indexes are unitless, indivisible. That's why we need logarithms, it's kind of a unit but of a
> different kind."* (Tom, Sep 23)

**An ordinary unit divides the thing; a logarithmic unit counts its doublings.** A metre says how many metres,
which an entry cannot take, since an entry cannot be divided. log₂ of an index says how many levels deep its
address runs, about how many bits it needs, and it never touches the entry. Doubling the count adds one rung,
whatever the count was. That is why it works where ordinary units fail: it measures the size of the address
without dividing anything the address names. Bits, octaves, decibels and orders of magnitude are all units of
this kind: each counts a ratio, and each is dimensionless.

**In the corpus it is the second register.**
- **The log register** measures depth: the rung, the octave, which level (§2.2).
- **The angle register** measures position: where along the turn.
- **The dial uses both.** Its radius is logarithmic: the window is N^reach, one rung per doubling. The tower's
  steered bit is log₂ of the unit. The radius is the log unit; the digits are the exact address.

**The log gives the level, not the entry.** log₂ of record 4,536,507,171,109,588 is about 52.0, and so is the log
of every one of its neighbours. So the logarithm navigates (it chooses which level the hand steers) and the digits
address. Floating point makes the same split: the exponent is the log, the mantissa a few of the digits. A
magnitude can live with that, because its low digits are rounding. An index keeps the log to move and all the
digits to name.

### Breadth and density as the two sides of the point

> **(1 Oct)** "Density" has been dropped as a framework word (Sep 30). Read this section as history. The world is breadth, and the reader:world ratio is g.

> *"Is density the fractional part of a number and breadth the whole part of a number?"* (Tom, Sep 23)

**Nearly, and exactly once it is said in digits.** Breadth is not the whole part itself but **how many digits it
may have**; density is not the fractional part itself but **how many digits of it can be held**.
- **Digits before the point are breadth**: how far out the numbers reach.
- **Digits after the point are density**: how finely the space between whole numbers is resolved.
- **The view from everywhere** is infinitely many digits on both sides (§1.1).
- **A real reader** holds finitely many on each side: a range it can reach and a fidelity ε.
- Fixed-point arithmetic is the plainest case: a set number of digits either side of the point.

**It sorts the session's objects.**
- **An index is all breadth.** A whole part and no fractional part: indivisible, density fixed at one entry. It
  grows only by adding whole digits: larger, never denser.
- **The quarter turn is all density.** Its whole part is fixed, one quarter turn and never more, and it can only be
  resolved more finely: *Browsing the Fisheye*'s "denser, never larger".
- **The dial joins them**: the digits (the index) are its breadth, and the angle on the turn is its density inside
  the window.

**It holds in the log register too.** The whole part of log₂ is the level, the exponent, the rung: breadth across
scales. The fractional part is the position within the octave: density within a level. Floating point stores the
log's whole part as its exponent and a number's leading digits as its mantissa: breadth and density in one word.

**The caution.** Density is how many fraction digits can be trusted, not what they are: two numbers can share a
fractional part and differ entirely in density.

### The stones can be anything

> *"The reader does not need to read magnitudes, he could read anything. The array could point to any kind of
> object, including a lazy function that is evaluated lazily, or it could point to glyphs or colors. Does not
> need to be a shape."* (Tom, Sep 22)

The scaffolding and the stones are separate, and **everything about addressing belongs to the scaffolding.** A
reading becomes a share through arctan and 2/π, and the share becomes an entry through the array's N. Neither
step looks at what hangs there. *Browsing the Fisheye* §7 already says it: "a lens is orthogonal to the data it
observes." An entry may be a number, a glyph, a colour, a record, or a function not yet run.

**So the paper's results split in two, and the split scopes them:**

| works for any list on one quarter turn | needs a shape: a closure, with facing |
|---|---|
| the address: reading → angle → share → entry | closure as four sweeps (§0.4); an array is one sweep and does not close |
| the fisheye spacing, the corner, the horizon in the reading (§2) | the facing, and the two sides it makes: outside and inside hemispheres |
| the two verbs: pointing (fetch by reading) and walking (step through the indexes) (§2.0) | the outside reader's depth: gaps give h, h gives depth (§4.1) |
| g: how many hangers are placed (§1.1) | the stitch, and the scale crossing the horizon between two sides (§4) |
| the resolution budget of about 1/ε distinct entries (§ When a growing array looks finished) | the limb loss, the ceiling, the repair: the projection's resolution in v (§3, §5) |
| the verdicts that are never withdrawn (§0.1) | the arcsine or Cauchy law of a shape's values (§0.2); the everywhere equation's mean facing (§0.3) |

The left column is general machinery: **a way to navigate any list by angle.** The right column is what happens
when the thing laid down is a shape: it closes, it faces, and so it has two sides. The magnitude list is one
species among many, as *Degrees of Freedom* ruling 12 already allows for generators.

**One condition carries over from the content, whatever it is** (*Browsing* §12): "what makes a list browsable
is not that its addresses are distinct but that what stands at them is." An array of identical glyphs has
perfect addresses, and a reader moving across it cannot tell where it is. The content need not be magnitudes,
but it must differ.

**Relation → address → payload.** (Sep 22, from the review and Tom's agreement.) The usual presentation
runs *space → coordinate → value*, with a physical magnitude as the value, so the coordinate system looks as
if it were about magnitude. The construction here separates three things:
- **the relation** (the sweep, the reading) supplies an address;
- **the address** picks out a position;
- **the payload** is whatever occupies it.

> **The geometry supplies the addresses; the data supplies the objects. An address space does not care what
> occupies its addresses.**

On that reading the shape is one possible payload, not something the space requires. The Cauchy and shape
work is what made the addressing visible.

**Why the two were hard to tell apart: for a shape, the payload *is* the address.** The inside reader's
reading s = v/h is made from the magnitudes it receives. So in the geometric case the address is *read off*
the payload, and the two coincide. That is not a presentational habit. It is how a shape presents itself to
its reader. They come apart only when **the reading is supplied from outside the content**: a hand on a dial,
a query, a key. In the array, the navigator chooses s, and the entry is fetched. So the separation has a
precise cost: **a payload that is not magnitudes cannot tell the reader where it is; the navigator must bring
the reading.** This is the Browsing condition above seen from the other side. The content need not supply
the address, but it must differ, or the reader cannot confirm where the address took it.

**What is not new.** Separating address from payload is old in computing: pointers, memory addresses, hash
tables. A hash ring (consistent hashing) already places arbitrary payloads on a circle by angle, and already
buys the property that growth moves few addresses. The claim here is narrower:
- **which** address space: the quarter turn and the freedom, joined by arctan and 2/π;
- **what it does without N**: a static layout with relative addresses and no horizon, and a dynamic one with
  absolute addresses and a horizon where the newest entries crowd;
- **where resolution runs out**: at a fixed fidelity, set by the lens, not by the payload.

**The literature check (Sep 23): most of the array machinery is known, under other names.**

| this paper's array result | where it already exists |
|---|---|
| payloads of any kind placed on a circle by angle; growth moves few addresses | **consistent hashing** (Karger et al. 1997): keys and nodes hashed onto a ring; adding a node remaps only the keys between it and its neighbour |
| an unbounded structure laid on a bounded region, crowding at the rim, entries dropped below a resolution | **the hyperbolic browser** (Lamping & Rao 1995): a tree laid out on the hyperbolic plane and drawn in the Poincaré disk. "Very remote parts of the hyperbolic plane get minuscule amounts of space near the edge of the disk"; nodes below one pixel are not drawn |
| re-uniting: one number moves every address at once | the hyperbolic browser's **change of focus**, "a translation in the hyperbolic plane", a rigid move that recomputes nothing. Scaling the freedom, s → ks, is the same kind of move: a translation in the log register |
| the ~1/ε budget of distinct addresses; past it, addresses must change | **list labeling / order maintenance** (Itai, Konheim & Rodeh 1981; Dietz 1982): a fixed label space M holds at most M items before relabelling is forced; its cost bounds are known |
| the count held as exponent (doublings) and mantissa (the reading) | **floating point** |
| the fisheye as a spacing that falls away from a focus | **fisheye views** (Furnas 1986; Sarkar & Brown 1992) |

What the search did not find, as stated:
- the **pair of layouts**: a known-N list on the quarter turn, relative and with no horizon, and an unknown-N
  list on the freedom, absolute and with a horizon, joined by arctan and 2/π;
- **arrived and unarrived as a ratio and its swap**, adding to π/2. The identity is elementary
  (arctan x + arctan 1/x = π/2); the reading of it as past and future of a growing list is what is new, if
  anything is;
- **a growing list looking finished at n = c/ε**: the order of limits met in a list.

That is consistent with the paper's stated aim, a fresh look at old ideas through the inside/outside
vocabulary, rather than a new mechanism. The first search was a first pass; the hyperbolic browser is the
nearest neighbour and the one to read in full before any claim goes further.

**A lazy array is breadth without density.**
- It has its N, so it has full breadth and no horizon.
- None of its values exists until an address lands on one. So its density is produced only where the reader
  points, one evaluation per address.
- g then reads naturally as **how many hangers are evaluated.** This matches the Sep 18 ruling, where g places
  hangers and "the scale is what you hang on the hangers". A lazy entry is a hanger whose stone is made on
  arrival.
- It also matches *Browsing*'s cost claim: a view costs the entries in the window, however long the array is.

### The practical application

This is the point at which the whole construction becomes something usable (Tom, Sep 22: "how the array maps to
this is maybe the final actual practical application of all this").

**Put any list on a quarter turn or on the freedom, and navigate it by angle.**
- **Choose the layout by whether N is known.** A fixed list goes on the quarter turn: its address is a share,
  the same share of a thousand entries or a trillion, and it has no horizon. A growing list goes on the
  freedom: its address is absolute and never changes as the list grows, and it pays with a horizon where the
  newest entries crowd.
- **The cost of a view is the view.** Only the entries the reader's window lands on need to exist. With a lazy
  array they are made on demand, and the rest of the list stays unevaluated behind the scaffolding.
- **The content is free.** Numbers, glyphs, colours, records and functions all go through the same address
  machinery. Only depth, stitching and resolution in v need magnitudes.
- **The one condition is that entries differ.** A uniform list cannot report position.

**What today's measurements add to the application, marked by how well each is established:**
- **N is only ever the array's.** A reader navigating it holds a share, and N-free verdicts are never withdrawn
  when the array grows (§0.1). That is measured. It lets a growing array keep its addresses **only when it is
  laid on the freedom**; on the quarter turn, the share the reader holds points to a different entry once N
  changes.
- **A reader of fixed fidelity can tell apart only a fixed number of things, however long the array is.** In
  §1.1 the outside reader at ε = 10⁻³ never held more than 1122 distinguishable points, at N from 20 000 to a
  million.
  - If that carries over to a browser's view, then evaluating more than a fixed number of entries per view is
    waste, and the best g for a lazy array is set by the screen's fidelity, not by the array.
  - The array's own budget is now measured on one quarter turn with no facing (about 1/ε, § When a growing
    array looks finished). The 1122 figure came from a shape's projected, faced view, so it is a comparison,
    not the array's number.
  - **Measured in a fisheye window (Sep 23, `window.mjs`; predictions registered before the run).** n entries
    laid by share on the half turn and drawn at x = R·tan θ, as the strip draws them, in a window W = 1000 px
    wide, with entries told apart at ε = 1 px:

    | test | result |
    |---|---|
    | **W1** more entries, fewer seen | **confirmed**: resolved 617 at n = 942, then 500, 356, 274, 102, 10 and 0 at n = 1000, 1500, 2000, 3000, 3500, 3600 |
    | **W2** the merge starts at the **focus**, where the gap R(π/n)sec²θ is smallest, at n ≈ πR/ε = 942; the window is empty of distinct entries past πR(1 + (W/2R)²)/ε ≈ 3560 | **confirmed**: nothing merged at 942, merged out to 74 px at 1000; zero resolved at 3600 |
    | **W3** the peak is at most W/ε, whatever the lens | **confirmed**: peaks 254, 377, 611, 833 and 973 for R = 50, 150, 300, 600 and 2000, all under 1000 |
    | **W4** the collapse is set by εn alone | **confirmed**: resolved share 0.763, 0.764 and 0.765 at εn = 1000 from three different (n, ε) |
    | **W5** a fixed angle per entry (the dynamic layout) makes the window independent of the list's length | **confirmed**: 393 in the window and 393 resolved at n = 600, 6000 and 600 000 |

    - **The prediction holds**: a fixed-fidelity window resolves a bounded number of entries, at most W/ε,
      so evaluating more per view is waste.
    - **The window goes blind at its focus first.** The fisheye's slowest place on screen is the focus, and
      that is where too long a list merges. It is §3.3's rule, each reader blind where its lens is slowest,
      met in a browser.
    - **The stronger the fisheye, the fewer distinct entries.** A strong lens (R = 50) resolves 254 at best; a
      nearly flat one (R = 2000) resolves 973. The fisheye spends the screen's budget on reach, not count:
      it shows further along the list, at the price of fewer things told apart.
    - **The static strip fails for long lists, and the dynamic layout does not.** With the angle per entry
      set by the list's length, a long list crushes the focus. With the angle per entry fixed, the window
      never sees the list's length at all (W5). That is the static/dynamic split of "What an array is",
      measured on a screen.
- **g is the one dial the application needs.** It chooses how many hangers to place, or evaluate, so that the
  ones placed stay distinguishable.

### The dial already built on these ideas

> *"We created this dial with these ideas."* (Tom, Sep 23, of `example-tower.html`, which carries
> `fisheye-ladder-shape.html`'s dial unchanged, built Sep 8–13.)

The dial browses a list of 2⁵³ − 1 records, and nearly every array result above is already a working part
of it. Read in this paper's terms:

| the dial | this paper's array result |
|---|---|
| the list laid by share on the turn, θ = π(i + ½)/N, N fixed at 2⁵³ − 1 | the static layout: relative addresses, N known (§ Static and dynamic arrays) |
| the record read off the blue needle as the window's centre plus the unit times tan(blue) | the reading on the freedom: arctan carries it onto the list and tan carries it back |
| "ψ₁ = 2/π carries the reader's turn into that window's own count of records" | the round trip π/2 · 2/π = 1 (What an array is) |
| the corner at 45°, "one reader's unit"; the corners beyond at 2, 4 … 2⁵, one doubling apart | the unit c, and the log register's octave, where distances are c-free |
| the window's end at the fifth corner; "the horizon is further, where the corners never stop" | the budget: a window resolves a bounded number of units, whatever N |
| the radius sets the unit (unit = N^reach / 64 records); a change of radius keeps the record and restates only the angle | **re-uniting**: one number moves the reading, and no record moves |
| the tower: the steered bit is b = log₂(unit), and "one rung of the dial is exactly one bit of the address" | **the count held as floating point**: the radius is the exponent, the blue's reading the mantissa |
| "a bit does not move when the list grows"; "a calendar can name a moment without renaming it later" | absolute addresses, the dynamic layout's property |
| "nothing is stored": a cell's colour is a hash of its own prefix | relation → address → payload, and the **lazy array**: a stone made on arrival |
| ↑ and ↓ step one bit and return the address exactly; the carry marks the levels a step disturbed | a control, not just a correspondence; the carry is the address re-entering the level above |

**Why the dial does not go blind at its focus, where the strip does** (`window.mjs` W2). The strip spends a
fixed share of the turn per record, π/n, so a long enough list crushes its focus. The dial never lays records
at π/N on the screen. The blue's tan is measured in the **reader's unit**, which the radius sets, so the
window always holds about 2·2⁵ units, whatever the radius and whatever N. That is W5, the fixed angle per
entry, the window that never sees the list's length. At full radius a unit is 2⁴⁷ records and the hand
steers the 2⁴⁷ bit; it never tries to tell single records apart there. **The dial spends its resolution
budget the re-united way: it keeps the address, level by level, and lets the radius choose which level is
resolved.**

**What the dial knew first.** The floating-point reading (§ When a growing array looks finished, P5) was
found here on Sep 23 by measurement. The dial had it by Sep 13 as the tower, and the page's own head comment
records the prediction and the check ("the lit level stepped by +1 every time, without exception"). This
section is the paper catching up with the instrument.

### The dial, read whole

> *"I'm not sure, use the newer vocabulary to describe it. This has lots of physics ideas in it. Let's look
> for connections and how it all fits together. Lots of these ideas before, but not connected together."*
> (Tom, Sep 23)

Most of what follows was found before, in separate places: *SR through the Fisheye* (Sep 4), *The Two
Settings* (Aug 22), *sr.md* §9.2.1–9.2.2, the reader-geometry note, and the dial's own build log. What is
new here is putting them on one instrument in one vocabulary, plus three checks (`dialphysics.mjs`
D1, D3 and D7; predictions registered before each run). Each row says where it was established.

#### The dial in the paper's vocabulary

| the dial | in h and v |
|---|---|
| the apex, the blue at rest | **home**: h = 1, v = 0. The reading is zero |
| the blue needle's angle | a place on **one quarter turn**, from home towards the horizon |
| the blue's value, unit · tan(blue) | **the reading s = v/h**, on **the freedom**, in the reader's unit |
| the first tick, 45°, "one reader's unit" | **the corner**, v = h, s = 1 |
| the ticks at tan = 2, 4 … 32 | the **log register's** rungs, one doubling apart; ζ, the thrust's coordinate, reaches them only far out (0.5623 against ln 2 at the first gap) |
| "the horizon is further, where the corners never stop" | **the horizon**, h = 0, never reached |
| the half-disc | **two quarter turns**, back and forward from the record: two sweeps from one home |
| the radius | **the unit c**; a change of radius is **re-uniting** |
| the digits and the tower | the address, with **N known** (2⁵³ − 1): everywhere's object, the static array |
| the blue, pointing | the **inside reader's verb**: fetch by a reading |
| the gold thrust, a pan, ↑ and ↓ | the **outside reader's verb**: walk, a step at a time |
| the window's reach of about 2·2⁵ units | the **resolution budget** at the reader's fidelity |

So the dial holds all three scenarios on one screen, **as verbs and objects, not as sides.** Pointing is the
inside reader's, walking the outside reader's, and the address in hand is everywhere's. With no facing, none
of them has a hemisphere (What an array is).

#### The dial is the Roman arch, and a hybrid

> *"The dial is two quarter turns, it is the roman arch. The array is uniformly drawn on the arc. The arc [is]
> currently the freedom version."* … *"You can't actually browse 100 trillion items. So the dial has utility, but
> it's kind of a hybrid."* (Tom, Sep 23)

**The arch.** The keystone is home, at the apex: the record, reading zero, where the two sweeps meet. Each half is
one quarter turn, a bar of 1 sweeping from vertical at the keystone to horizontal at a foot; the corners sit 45°
down each side; the feet are the horizons, back and forward along the array. This settles *The Centring*'s arch
question (ruling recorded there): the span is the half turn, and its middle stone is home, not the corner.

**Two ways the arch carries an array.**

| | uniform | freedom (the dial as built) |
|---|---|---|
| layout | evenly by share across the whole arch, θ = π(i + ½)/N | the record at the keystone; each half read as unit · tan θ |
| the needle's angle is | a share of the array | a reading on the freedom, in the reader's unit |
| the feet are | the first and last records: ends | horizons, never reached; the window ends at the fifth corner |
| N | known, spread over the arch | not used by the reading; the radius sets the unit |
| whose view | the view from everywhere's layout | the reader's: focus at the keystone, fisheye to both feet |

The uniform layout survives on the dial only in the head comment's angle query, left when the line chart was
removed on Sep 12. The arc as drawn is the freedom version.

**Why the dial is a hybrid.** At fixed fidelity an arch holds only about a thousand distinguishable places (the
budget of § When a growing array looks finished; the window measured at most its width in pixels). So the uniform
version of 10¹⁴ records cannot be browsed at all. The dial joins three things instead:
- **addressing**: the digits are the exact index into a known N, the uniform layout's; this is not browsing;
- **browsing**: inside the window the blue reads unit · tan θ from the keystone, a fisheye over about 64 units,
  within the budget;
- **levels**: the radius chooses the level, one rung per doubling, one bit per rung, in the log register.

So the dial **searches by levels and browses within a level**: with the corner rule, every step is the same 45°
gesture, about six drags for one item in a trillion (the reader-geometry note, Sep 3). "An address is reached by
its digits; a place is found by looking": the digits reach, the fisheye looks, and the radius decides at which
level to look.

#### The dial is an octave browser, and what that says about SR

> *"So the dial is an octave browser."* … *"Ok, so this really is an octave browser. What does that say about the
> SR addons?"* … *"I want to fully explore this."* (Tom, Sep 23)

**Why the dial is an octave browser.** The radius moves through octaves: one rung is one doubling of the reader's
unit, one bit of the address (Tom, Sep 8: "zooming the radius is changing the active octave"; one octave per 0.019
of radius). The arch shows octaves too: its corners sit at 1, 2, 4 … 32 units from the keystone, five octaves down
each side. And the change is smooth because the dial stores the logarithm itself, reach, a real number: the whole
part of log₂(window) is the octave, the fraction is the position inside it. Only the corner ticks and the tower's
steered bit are whole numbers.

**What it says about SR.** `octave.mjs`, O1–O10, predictions registered before each run; all held.

| | result | check |
|---|---|---|
| **O1** rapidity is an octave count | collinear boosts add rapidities; the Doppler factor k = e^ζ multiplies; its octaves log₂ k add | exact to 10⁻¹² |
| **O2** the radius is the sky's octave control | a boost of k multiplies every direction's stereographic reading cot(θ/2) by exactly k, fore and aft: one rung of the radius is one Doppler octave | 1999 directions, worst 4×10⁻¹¹ |
| **O3** the blue is linear near rest and octaves near light | celerity doublings measured in Doppler octaves: 0.014 (0.01→0.02), 0.143 (0.1→0.2), **0.811 at the corner (1→2)**, 0.997 (10→20), 1.000 (1000→2000). Small celerities compose as a plain sum (0.01 and 0.02 give 0.030003); large ones compose so their octaves add (16.872715 both ways) | exact |
| **O4** the gold thrust is an accelerometer | the dial adds rapidity at a constant rate a = 0.4 tan(gold) per second of the hand's clock: that is constant proper acceleration; the blue's worldline lies on the hyperbola (x + 1/a)² − t² = 1/a²; after 10 s at gold 0.6 rad the blue is at 82.6° and never reaches 90° | hyperbola residual 4×10⁻¹⁰ |
| **O5** a zoom, a pan and a zoom are two non-collinear boosts | ×4, pan 0.35 rad, ×3 composes to ×10.8151, not ×12: an **octave deficit of 0.150**; the rotation left over is the **Wigner angle, 17.867°** (sky angle, sign by convention) | matches *SR through the Fisheye* C8 |
| **O6** no octave is preferred | an isotropic sky read stereographically is a Cauchy; after a boost of k it is still a Cauchy, its scale changed by k (quartiles ±1.00 → ±0.33 at k = 3). The view has the same shape at every octave: the octave is not in the view | 200 000 directions |
| **O7** a fixed-fidelity reader runs out of sky octaves | after a boost of k the forward hemisphere fits in 2 arccot k ≈ 2/k; past k ≈ 2/ε it is one resolution cell: **about log₂(2/ε) readable octaves**: 8, 11 and 15 at ε = 10⁻², 10⁻³ and 10⁻⁴ | exact |
| **O8** the arch is one-dimensional velocity space | gd maps every rapidity onto (−π/2, π/2): the keystone is rest, the corners are celerity ±1 (β = ±1/√2, ±45°), the feet are light, both ways | exact (±90° reached only in the limit) |
| **O9** far out, each octave halves the clock | h = 1/γ halves per Doppler octave (0.588, 0.501, 0.500 at k = 2, 16, 1024) while v = β saturates at 1 | exact |
| **O10** the blue runs out of octaves at the same count | a reader of the blue with angular fidelity ε loses it against the foot at ζ = asinh(cot ε): 7.64, 10.97, 14.29 octaves, **equal to O7's log₂(2/ε)** to two decimals | exact |

**What it adds up to** [reading, on the checks above]:
- **SR's kinematics sit on the dial because the dial browses octaves, and rapidity is an octave count.** Bondi's
  k-calculus is SR written in octaves.
- **The two dictionaries are the dial's two octave controls.** The radius is the sky's (exact octaves, O2); the blue
  is the speed's, a hybrid: linear near rest, octaves toward light, and the corner is the crossover (O3). **Galilean
  mechanics is the linear part of the octave browser**; the corner is where it hands over. That is the same hybrid
  the dial is as an instrument: fine near the record, octaves far out.
- **The arch is velocity space** (O8): keystone rest, feet light. The Roman arch, the dial and one-dimensional
  special relativity are one figure.
- **Holding the gold is uniform acceleration** (O4), and a steady octave rate is the same thing that D7 found for a
  steadily growing array: equal proper time per octave, far out.
- **No preferred octave is the relativity principle** in this language (O6): only differences in octaves mean
  anything. Physics supplies c, which pins where the octaves are counted from, the one thing the dial leaves free.
- **Light is infinitely many octaves away, but a real reader's last octave is finite** (O7, O10): about log₂(2/ε),
  the same count whether it reads the sky or its own speed. It is the order of limits once more: at ε → 0 first the
  octaves never run out; at fixed ε the reader cannot tell the last ones from light. That is a statement about
  reading at fixed fidelity, not a claim that physics has such a limit.

#### The dial is one implementation among many

> *"That's interesting that all these domains are just rediscovering browsing octaves in their language."* …
> *"Our dial is just another implementation of this idea with our vocabulary."* (Tom, Sep 23)

**The dial is one implementation of a known idea** . Scale-free domains keep finding the log register: the musical octave, Fechner's law that
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
- **the hyperbolic browser**, with focus, level and a pixel budget (*One Reader* §3.3).

So the dial is not a new instrument. What is new is what it is attached to: the reader and its two registers, the
Cauchy as the law its moves keep, fixed fidelity with N unknown, and the SR identity (the octave table above).

Full references are in *One Reader*.

#### The ring question, in the newer vocabulary

The dial's angle query returns the index mod N, "and the mod is what makes the list a RING". The Sep 23
ruling says an array does not close. The vocabulary now separates **three** things where there had been two:

| | closes? | facing? | what its far end is |
|---|---|---|---|
| **an array** | no | no | the end: with N known, a bound; with N unknown, the horizon, "the future" |
| **a ring** (a closed line) | yes | no | the other end of the list coming back, through a **seam**, not a horizon |
| **a shape** | yes | yes, so two sides | "its other side, coming back" (the reader-geometry note) |

The reader-geometry note already had the middle row: "closing a line gives a RING, not a surface", and the
calendar's hour ring is the example.
- What a ring does not have is what the shape results needed: facing, two hemispheres, a limb, a stitch.
- What it does have is closure. So closure's results (the four sweeps, the two checksums) could apply to a
  ring, and the shape results cannot.

**Both are in use (Tom, Sep 23: "both, we use the wrap around ring in the board browser").**
- **The dial is an array.** It clamps: `read()` and `recentre()` hold the record between 0 and N − 1, so a
  pan past the last record stops there. (The "mod N makes the list a RING" sentence belongs to the line
  chart's angle query, removed Sep 12, and survives only in the head comment.) One quarter turn each way
  from the record, two ends, N known.
- **The board browser in `field.html` is a ring.** It runs on the embedded VCP library, which lays item i
  at −i·π/N on a **half turn** and folds every focus back into it (`VCP.foldFocus`: focus mod π).
  `VCP.itemAt` returns the item mod N, and the library states the reason in one line: **"The address
  repeats every half turn, so a direction and its opposite are one address."**

**That line is the difference between a ring and a shape, in the corpus's own terms.**
- On the strip, the lens is tan, and tan repeats every half turn. The two horizons, at ±π/2 from the focus,
  are **one point**: the item opposite the focus. Items that run off one edge come back in at the other. So
  **the ring's seam is its horizon**, as the reader-geometry note put it: "Closed: no unreached end, so the
  horizon is a SEAM."
- **A ring has no facing because a direction and its opposite are one address.** Facing is exactly the
  ability to tell them apart: a shape's two sides are a direction and its opposite, *different*.

**So the three objects differ in how many sweeps they take and where the sweeps join:**

| | sweeps | joined | closes? | facing? |
|---|---|---|---|---|
| **array** (the dial) | one each way from the record: H → V | at home only; each far end is a bound | no | no |
| **ring** (the board browser) | two: H → V → H, a half turn | at home and at the horizon, which is one point, the seam | yes | no: a direction and its opposite are one address |
| **shape** | four: H → V → H → V → H, a whole turn (§0.4) | all the way round | yes | yes: a direction and its opposite differ, so two sides |

This matches the closure visual: **a ring closes in two sweeps, a shape in four.** The half turn is enough
for a ring because the ring never needs to tell a direction from its opposite. A shape needs the whole turn
because telling them apart is what its two sides are.

*This is a reading from the code and the vocabulary, not a measurement.* One consequence was then tested
(`ring.mjs`, Sep 23; see *One Reader* §5.1): a ring lap turns through π and a shape's through 2π; the ring has
its own landmark sequence, H C o C, and the shape's, H C o C H C o C, is the ring's run twice. The earlier
prediction that the landmark sequence "belongs to shapes only" was too strong: what belongs to shapes is the
repetition, each landmark met twice, which is the facing.

#### The physics on the dial

The dial's blue is the gudermannian of the rapidity: tan(blue) = sinh ζ. In h and v that is special
relativity's kinematics exactly:

| on the dial, in h and v | in special relativity | status |
|---|---|---|
| **v** = sin(blue) | **β**, the speed | **D1**, here: equal to 2×10⁻¹⁴ at five rapidities |
| **h** = cos(blue) | **1/γ**, the moving clock's rate | D1 |
| **the reading s = v/h** | **βγ**, celerity | D1; the build log's "speed" relation (Sep 12) |
| **the hold v² + h² = 1** | **β² + 1/γ² = 1**, the definition of γ | D1. *The Lorentz factor's identity is the hold.* |
| home | rest | |
| the corner, v = h | β = 1/√2, γ = √2, celerity 1 | *sr.md* §1, "the fulcrum's physical address"; D2 |
| the horizon, h → 0 | light: γ → ∞, never reached | *The Two Settings* §3, "the corner becomes the horizon" |
| the dial's cap, the fifth corner | β = 0.99951, γ = 32.0156 | build log, Sep 12; D6 |
| the gold held off the apex adds rapidity at a steady rate | **constant proper acceleration**: hyperbolic motion | *SR through the Fisheye* C5–C6, "uniform acceleration is the collapse on a schedule" |
| letting go rests the window on the record: the blue goes home | **taking the new rest frame**: every seat is home | *The Two Settings* §9, "no privileged seat = the swap"; a reading, not a check |
| **a change of radius shifts every record's ln s by the same ln 2** | **a boost shifts every direction's pseudorapidity by the same ln k**, but only in the **sky's** dictionary, where s is a direction's half-angle stereographic coordinate. In the speed's dictionary above (s = celerity) a boost does not rescale s | **D3**, here: both 0.693147180560 at four places, checked separately; that they are one move is a reading. *SR through the Fisheye* C4: "a boost is a pan in rungs". Corrected Sep 23, see the kill log |
| the rungs, celerity 1, 2, 4 … | β = 0.707, 0.894, 0.970 …; far out a celerity doubling is a Doppler doubling (k ≈ 2s). The exact Doppler octaves k = 2ⁿ sit at 3/5, 15/17, 63/65, 255/257, which the rungs approach | *SR through the Fisheye* C3; D4. Corrected Sep 23 |
| the compose move (s₂ − s₁)/(1 + s₁s₂) | velocity addition (β₁ + β₂)/(1 + β₁β₂), with tanh for tan | *The Two Settings* §2: "a rotation and a boost differ by one sign bit" |
| the reading is an address, not a magnitude | β read as a magnitude: "velocities don't add", "relativistic mass" | *SR through the Fisheye* §12, "did physics miss that it is an address?" |
| the space of readers (focus, radius) | velocity space; the Wigner angle is a triangle's area | *SR through the Fisheye* §13 (V0–V5) |

**The one new link: a steadily growing list is a uniformly accelerated observer** (D7). Lay a list growing
at r entries per unit time on the freedom with unit c. Its frontier sits at celerity n/c = (r/c)·t, and
celerity growing linearly in time is exactly **hyperbolic motion**, with proper acceleration a = r/c.
- Measured against the integrated equation of motion: equal to 3×10⁻¹² in celerity and in rapidity.
- The frontier's rapidity, asinh(n/c), is a × its own proper time. So **far out (n ≫ c), each doubling of the
  list costs the same ln 2/a of the frontier's clock** (1.386294 at a = ½, from n/c = 10⁴ on; 0.562/a from the
  corner to n/c = 2).
- So, far out, the growing array's rungs are **equal steps of proper time**. That is the collapse schedule of
  *SR through the Fisheye* C6, met from the list's side.
- And **the end the array never reaches corresponds to the speed of light the accelerated observer never
  reaches** (not to its event horizon, which is a different object).
  "A growing list looks finished at n = c/ε" becomes, in this reading, "a fixed-fidelity observer cannot
  tell celerity 1/ε from light". That is a structural reading, not a check.

**How it fits together.** Four threads were found separately:
- **the lens:** the fisheye, the Cauchy as an address;
- **the register:** rungs, doublings, re-uniting;
- **the hold:** v² + h² = 1;
- **the setting:** the one sign that separates a rotation from a boost.

On the dial they are one object:
- the blue is a place on a quarter turn (the lens);
- read in rungs, it is a rapidity (the register);
- its two components satisfy the hold, which in the saturating setting is γ's definition (the hold and the
  setting);
- the radius is the one number that re-units it all, which in physics is a boost (the register again).

What physics fixes and the dial leaves free is the unit: *SR through the Fisheye* §11 names it, "where the
horizon sits in world units (c)". **The dial's radius is the freedom physics does not have. A reader of
the dial chooses its c; an observer in the world is given one.**

**What is not claimed.** The dial was not built from physics, and nothing here says the world is a dial.
The shared object is the kinematics: the geometry of a bounded reading. The magnitudes (mass, energy,
interval) are what the fisheye cancels, and physics supplies them from behind the lens (*SR through the
Fisheye* §11).

## 0. The claim

The classical accounts of seeing a shape are unconcerned about N. That includes the rim, or occluding
contour; shape from texture; the intrinsic equation; and the theorem of turning tangents.

**This is not a claim about how each of those results was derived.** Most of them state a continuum object
from the outset and take no limit at all. The claim is narrower. A continuum treatment works **after** the
resolution limit has already been taken. Seen from a regime with finite fidelity, where the order of
refining and growing matters, that is as if the limits were taken in one order:

> **classical, in effect: the fidelity ε → 0 first, then N → ∞.** The rim hides nothing, and N never appears.

The corpus's readers cannot take the limits in that order. Their fidelity is what they are, and N is what
grows, unknown to them:

> **the corpus: ε fixed, N growing and unknown.** The horizon hides a share that grows with N. Past a
> ceiling, more points means less seen.

Taken in the corpus's order, the horizon is not only a loss. Two readers stand on opposite sides of it: one
outside and in parallel, one inside and serial. At the horizon, what one side loses the other side makes up.
Stitched there, the two sides give back the classical shape.

**Classical is both sides together. This paper is about what that sentence costs when ε is not allowed to go
to zero.**

**What kind of claim that sentence is.** The measured result is **the stitch** (§4): two readers, each
holding one side and neither holding N, rebuild the shape to the continuous observer's precision, and at
fixed ε the pair repairs what the horizon hides (§5). **"Classical is both sides together" is the paper's
thesis, its reading of that result.** The tests show that the two sides are enough to give back the
classical object; they do not show that the classical account *is*, in any historical or formal sense, a
stitch. Where the paper says "shown", it means the stitch; where it says "classical is both sides", it means
the thesis.

**Not the "both" of *Browsing the Fisheye*.** That paper's §5 also gets both the periodicity and the
magnitudes:
- the periodicity from the reading;
- the magnitudes from the list, "which was there all along", by address.

The list in hand is a completed system. By the Sep 22 ruling, holding it is **the view from everywhere**. So *Browsing*'s
both is **a serial reading plus everywhere's list**.

This paper's both is **two real readers and no list**. It rebuilds the shape without N (§4). The two results
do not compete:
- *Browsing* shows what a reading is worth once the whole is in hand;
- this paper shows what two partial readers can rebuild when it is not.

*Browsing* §12's "in parallel it is the layout of the array" is the view from everywhere under the same ruling, not the
outside reader.

### 0.1 Neither reader needs N

> *"The interesting thing is that neither parallel or serial know N. Have no concept of N, and most
> importantly, have no need for it."* (Tom, Sep 22)

Both the classical accounts and the corpus's readers are unconcerned about N, **for opposite reasons**:
- **The classical accounts** are unconcerned because they *hold* N.
- **The corpus's readers** are unconcerned because they never *use* it.

Every quantity either reader works with is its own:
- the outside reader's gaps, and its unit, which is its widest gap;
- the inside reader's step directions;
- the stitch, which is closure across the line of sight;
- the repair rule, which is the reader's own ε against its own spacing.

**None of them is N.** In the scripts, N appears in only two places: where the world is built (laying out
the hangers) and where the view from everywhere scores the result. **N is everywhere's count.**

**The same holds of a serial reader's whole kit** (*The Unit Rule* §4, §18). Its capabilities stack, and each
is priced:

| | capability | what it costs |
|---|---|---|
| 0 | receiving arrivals in order | nothing |
| 1 | relating an arrival to what it holds | a hold |
| 2 | recording the relation as a count of steps | a step |
| 3 | spanning the gaps between arrivals | a carry rule |
| 4 | recognising and counting corner crossings | a direction and two counters |

- "What rises across that list is **memory**. What never appears on it is a **unit**."
- **Nor does N appear on it.** The counters in row 4 count crossings locally: that is the M of §0.1a, never
  the whole's count.

So wherever this paper states a count against N, it is **the view from everywhere auditing the readers, not something the
readers needed.** That applies to "hidden εN²/(2π²)", to "N = V + R", and to "the count comes back to N".

**Why not needing N matters: the readers' verdicts are never withdrawn.** From *The Fisheye as a Lens* §3.4
(`serial2.mjs` S6′). One stream was run: an even lap, then one warped lap, then even laps.

| laps received | everywhere's whole-list verdict | serial flags formed |
|---|---|---|
| 1 | fisheye | 0 |
| 2 | **not a fisheye**: revised | 2044 |
| 80 | not a fisheye, *and still drifting back toward "fisheye"* | 2046 |

- Everywhere's verdict on the **same arrivals** is revised when the warp comes, then worn down by every even lap
  after it. Given enough laps it would say *fisheye* again about a stream that contains a warped lap.
- Each serial flag was formed on two moves and **stays correct for good.**
- A result that never used N never needs revising when the world turns out bigger. That is The Boundary's B229,
  and it is the practical meaning of "no need for N".

### 0.1a Three counts, not one

> *"The problem arises when you treat the outside parallel N, which is just the observable hemisphere's N,
> with the god's eyes' N, which is the true N."* (Tom, Sep 22)

The outside reader *does* hold a count: the count of what it holds. There are three counts, and conflating
them is the error. A fourth, the serial reader's, is added from *The Fisheye as a Lens* §2.3:

| count | whose | what it counts |
|---|---|---|
| **M** | the serial reader | arrivals between two landmarks it can see (corner to horizon, horizon to corner, …): one eighth of a closure |
| **V_ε** | the outside reader, at its fidelity | the points it can tell apart |
| **V** | the outside hemisphere | the points facing the outside reader, including those the limb merges |
| **N** | the view from everywhere | every point: both hemispheres, and the limb |

- **The serial reader's count is local.** It finds every segment the same: 125 at N = 1000, 512 at N = 4096
  (`serial.mjs` S4).
- A closure is four sweeps, each split by a corner, so eight segments. **N = 8M only for whoever holds the
  closure.** With no whole for M to be a fraction of, the serial reader cannot tell how many segments make a
  return.

- **V_ε ≤ V ≤ N**, and no rule inside the outside reader's list turns one into the next.
  - **V into N:** the far side. On the egg, V/N runs from 0.406 to 0.594 with the direction of view, so
    "N = 2V" fails (`outside.mjs` O2).
  - **V_ε into V:** the limb, which hides a share that grows with N (§3.1).
- **Any statistic the outside reader computes is a statistic of its hemisphere.** That includes its mean,
  its shares and its quantiles. It is well defined, and it is **not** the whole's. The error is quoting it as
  the whole's.
  - The Boundary's B209 row "N known: the list is in hand" is this error: the list in hand is V, or V_ε.
- The inside serial reader has the same issue with a moving hemisphere. Its count between horizons is the
  count of a half turn **centred on wherever it started** (`serial-inside-outside.md` P3).
  - This is *Browsing* §2's test: **"a mark the reader carries never moves; a mark laid in the world does."**
  - The inside serial reader's horizon is a **carried** mark. It sits a quarter turn from wherever the reader
    began, and it travels with the reader.
  - The outside serial reader's horizon is a **laid** mark. It sits at the limb, whatever the reader's start.
  - "A reader that has only the first can never say where it is, however long it walks."
  - **The mechanism is the founding of the hold** (*The Unit Rule* §4): "the first arrival is not a frame; it
    is the founding of the hold." The serial reader's home is wherever its hold was founded. Its horizon is a
    quarter turn from there, so it moves whenever the start moves.

So §0.1 needs sharpening. Neither reader holds **the true N**. The outside reader holds a hemisphere's count,
and it does not need even that for the stitch.

### 0.1b When reader and writer turn

> *"This would be fine if you the reader had a static position relative to the writer, but problematic if
> the reader and writer rotate relative to each other."* (Tom, Sep 22)

The outside reader watches the shape make one full turn, in 360 frames with N = 4000 (`rotate.mjs`; all
predictions registered before the run):

| | circle | egg |
|---|---|---|
| 2V/N across the turn | 1.000 in every frame | **0.812 to 1.188** |
| arcsine KS of the frame's v | 2.5×10⁻⁴ in every frame | **7.7×10⁻³ to 0.34** |
| can the reader see the rotation in its statistics? | **no** | yes |

- **On the circle, the hemisphere's statistics are the same from every angle.** So "the hemisphere is half
  the whole" is never caught out, and the rotation is invisible in them. Only the circle makes the
  conflation safe.
  - **The reason is *The Centring*'s Proposition 3.** Read a figure against its own size in each direction.
    The residue is the figure's ratio between two directions, r(t₂)/r(t₁). The circle is **the one figure
    whose residue field is trivial**: it is 1 for every pair of directions. So every direction looks the same,
    and a hemisphere from any angle is the same hemisphere. On every other figure the residues are the shape,
    and turning the figure turns them into view.
  - ***Browsing* §12 gives the same fact from the list's side:** "a uniform address space cannot report
    position at all". When every address holds the same thing, travelling changes nothing the reader can see.
    A turning circle is that, for a reader outside.
  - ***The Unit Rule* §7 gives it from the reader's side.** Read from its centre, a circle is a still scene:
    "every look lands on the corner … and the record says exactly what a circle deserves: nothing at all,
    ever". And "every rule is quiet on the shape it believes in".
  - So there are three accounts of one fact:
    - **the figure's:** its residue field is trivial;
    - **the list's:** its address space is uniform;
    - **the reader's:** its record is silent.

    The rotated circle's invisibility is all three at once.
- **On any other shape, rotation exposes it.** A hemisphere statistic quoted as the whole's is right only in
  the frames where it happens to be.
- **Accumulating without identity does not reach N:**
  - adding up the frames gives 180 N after one turn, and it keeps growing;
  - collecting distinct values saturates at the register's size: range ÷ ε = 2000 (circle) and 2700 (egg).
    That measures the reader's register, not the shape.
- **Accumulating with identity does reach N**, after half a turn. The union of labelled points seen comes
  to N at 0.500 of a turn on both shapes. Identity, meaning recognising a point when it comes round again,
  is everywhere's to give. It is the Sep 21 question of *which list a signal is a signal of*.
- **Every point enters and leaves the hemisphere through the limb, which is where the reader is blind.**
  The share of each point's visible passage spent below resolution:

  | N | ε | share of passage unresolved |
  |---|---|---|
  | 4000 | 10⁻⁴ | 4 % |
  | 16 000 | 10⁻⁴ | 16 % |
  | 4000 | 10⁻³ | 44 % |

  **The reader never sees a point arrive or leave.** Under rotation, the horizon becomes the gate every
  point passes through, and the gate is the blind band. That band grows with N.

### 0.2 The mean is everywhere's metric

> *"Mean is only meaningful when you know a N. Mean is the gods eye metric."* (Tom, Sep 22)

A mean is a total divided by N. **The mean of the whole needs the true N**, and only the view from everywhere has that. The
outside reader can divide by its own V, but that gives the mean of its hemisphere, not of the whole (§0.1a).
Three things follow, all classical in themselves:

- **The whole-list law is everywhere's too, not only the mean.**
  - The law meant here is the **empirical law of the whole list**: the tally over the resolved inventory. That
    tally needs the whole's count.
  - This is not a claim about laws in general. A density or a transition rule can be stated with no finite N
    known.
  - What the inside reader has is the **lens**, dz = 1/(vh) per unit of turn (§2.2), met one move at a time.
  - **"The lens is the thing; the law is its N-known shadow"** (*The Fisheye as a Lens* §1). The Cauchy law,
    1/(1 + s²), is what the view from everywhere gets by tallying the lens over a whole list.
  - So when `serial-inside-outside.md` P2 found the inside parallel reader's set to be Cauchy, the set was the
    reader's. Calling it Cauchy was the view from everywhere scoring it.
- **The Cauchy has no mean.** That is a fact about the distribution, true whoever observes it. **No new
  reason for it is proposed here.**
  - What is proposed is an **observational reading**: a Cauchy-like law arises naturally in an account that
    is serial, projective and N-free, and averaging such an account does not recover the whole object's mean.
  - The missing first moment and the reader's missing N are **consistent with each other**. Neither is offered
    as the cause of the other.
  - ***Browsing the Fisheye* §3 already keeps the two absences apart**, and this paper keeps them apart too:
    - **The magnitudes are gone because of the cancellation.** That is a fact about the ratio, true per
      arrival, and true of a finished set of a million readings too.
    - **The mean is gone because the run is never finished.** "The heavy tail is the horizon, and the run was
      never clipped." A drawn circle is closed, with both ends of every diameter present, and that closure is
      what makes its tail finite. The reader holds an open run instead.
  - This is the observational reading in the corpus's own terms. **A mean belongs to a closed, resolved
    account. The Cauchy's reader holds an open run.** It is the same division as §0.3's: the everywhere
    equation is the resolved space's statement, and the unresolved space cannot make it.
- **The Cauchy is also the law whose average does not depend on N.** The average of N Cauchy readings is
  distributed exactly like one reading, whatever N is. (The Cauchy is stable with index 1.) So even if the
  inside reader did average, N would have nothing to do.
  - Compare the Gaussian, whose average sharpens as 1/√N. There, N does work, which is why the Gaussian
    belongs to a view that holds N.
- **The reader's centre is the corner, not the mean.**
  - The corner is where v = h, so the reading there is 1.
  - The reader finds it from the reading alone, with no count.
  - It is the Cauchy's median, reached without counting to the middle.
  - **There are three routes to the corner. None needs N, and one needs neither a count nor a division.**
    - **By the reading:** the look whose reading is 1. Per arrival and with no count, but it needs the ratio
      formed.
    - **By the median of the reader's own arrivals** (*Browsing* §3). It "settles *on* it", sharpening as one
      over the root of the reader's own n: distance 0.0038 at a hundred arrivals, 0.00007 at a million. It
      uses the reader's own count, which is not everywhere's.
    - **By a corner crossing** (*The Unit Rule* §1, §4, §7). The reader is already comparing each arrival
      against its hold. The corner is where that comparison **changes sign**, an event it notices for free:
      "a by-product of the reading the reader was performing anyway", paid for in counters, not
      arithmetic. **No ratio is formed and no division is made.** It is the cheapest of the three, and the
      only one that is an event rather than a value.

**Today's means and medians are all on everywhere's side of the ledger:** error medians, fitted offsets, and
the arcsine and Gaussian checks. They score the readers; the readers never compute them.

**Holding everything is not keeping everything.** Forming a law throws the order away (*The Fisheye as a Lens*
§3.1, `serial2.mjs` S5):
- Everywhere's whole-list law was **blind** to whole families of uneven traverses. From the centre, that means
  anything whose antipodal sum is constant, including a square wave putting four times the arrivals on one
  side.
- A serial reader holding one slot, its last move, **flagged every one of them from the second arrival.** The
  square wave was flagged exactly at its jumps and nowhere else.
- So "classical is both sides together" needs a guard. The classical *law* is both sides together **with the
  order discarded**. The serial side's order is something everywhere's law does not keep.

### 0.3 The everywhere equation

> **(1 Oct)** In the view from nowhere there is no corner, no home and no division v/h (R137). The "corner" and "ratio and its swap" readings here belong to the situation-3 reader, not to the circle.

> *"The god's eye view is defined as π/2 · 2/π = 1."* … *"This equation is similar to the equation of the
> circle. Let's explore its meaning further."* (Tom, Sep 22)

**The continuous observer: the sweep.**

> *"0 to π/2 is the full set of relations between a horizontal of 1 and a vertical of 1. The visual is a
> horizontal bar of 1 sweeping to a vertical bar of 1."* (Tom, Sep 22)

This is the Unit Passage. A rigid bar of length 1 lies flat (h = 1, v = 0: home) and sweeps until it stands
(h = 0, v = 1). The bar never changes; only its two shadows do, h and v, and the hold v² + h² = 1 holds
throughout.

The everywhere equation is a statement about this one sweep.

- **π/2 is the sweep itself:** the full set of relations, measured as turn.
- **2/π is the average shadow over the sweep,** of h or of v.
- **Their product is the bar,** 1. The two sweep equations say how:
  - **The vertical bar is built out of the horizontal shadow.** The vertical grows at the rate of the
    horizontal shadow, dv = h per unit of turn. Summed over the sweep, the horizontal shadow comes to exactly
    the vertical of 1.
  - **Likewise the horizontal shadow is spent at the rate of the vertical one,** dh = −v. Summed, that is
    the horizontal of 1.
  - So **the sweep carries one bar into the other, and the average shadow is the rate of exchange.** The
    first equation, dv = h, is the outside reader's lens (§2.2).
- **It is the Passage's two accounts, exchanged.**
  - The facing account has turned π/2.
  - The bar's account has moved one bar's length.
  - **The radial exceeds the linear by π/2**, as the Passage already records. 2/π is the same exchange read
    the other way.
- **The corner, as an area.**
  - Averaged over the sweep, the squared shadows are ⟨h²⟩ = ⟨v²⟩ = ½. That is the corner square's area:
    the ½ that the Passage shows as an area rather than a length.
  - In first powers, the average shadow 2/π = 0.637 falls below the corner's side, 1/√2 = 0.707.
  - **The whole sweep averages to the corner in squares, and not in first powers.**
- **Why this is everywhere's equation and not a reader's.**
  - The sweep's turn is closed at both ends, [0, π/2]: the symmetric, resolved account.
  - The reading v/h is closed at home and open at the far end, [0, ∞).
  - The total from everywhere needs the far end *included*, and only the resolved account includes it.
  - The reader's account has no such total. Its sum grows without bound as it approaches the far end, which
    is the inside reader's G3 below.
  - **The everywhere equation is the resolved space's statement.** The unresolved space cannot make it.

**Two equations, side by side.** Now take one side of a shape, the side facing the outside reader, with
evenly spaced hangers.

| | the hold (the circle's equation) | the everywhere equation |
|---|---|---|
| holds for | **each step** of the surface | **the whole side** |
| its two parts | motion across the line of sight (h) and motion along it | **ARC**: the side's length, what the serial reader's moves cover along it (serial's total). **WIDTH**: the extent of its v's, what the outside view spans (parallel's total) |
| form | (across)² + (along)² = 1, per step: **a sum of squares** | (ARC ÷ WIDTH) × ⟨h⟩ = 1: **a ratio times its swap** |
| on the circle | v² + h² = 1 | π/2 × 2/π = 1 (per radius: a half turn's arc is π, its width 2) |

**The first equation gives the second.** The outside lens is dv = h per unit of surface. Summed over the side,
it gives **WIDTH = ARC × ⟨h⟩**, where ⟨h⟩ is the mean facing over the side. Divide through and you get the
everywhere equation.

**The meaning of the two factors:**
- **π/2 = ARC ÷ WIDTH** is how far the serial reader's moves carry it per unit of the parallel view: serial's total per
  parallel's total.
- **2/π = ⟨h⟩ = WIDTH ÷ ARC** is the same ratio swapped: parallel's total per serial's total.
- They are **one ratio and its swap** (s ↔ 1/s), and a ratio times its swap is 1. The view from everywhere holds both
  totals, so for the view from everywhere they cancel.
- **⟨h⟩ is a mean, so it is everywhere's** (§0.2). The mean is exactly the **exchange rate between the serial
  total and the parallel total**.
- The pair of real readers never computes that mean. They get the same exchange rate a different way: from
  closure at the horizon, where the inherited step length came out at L ÷ unit = 1.0000 (§4). **The view from everywhere
  gets the exchange rate from a mean; the pair gets it from the stitch.**

**Measured** (`godseye.mjs`, 200 000 hangers, predictions registered before the run):

| shape | looking from | ARC ÷ WIDTH | ⟨h⟩ | product | ⟨h²⟩ | ⟨along²⟩ |
|---|---|---|---|---|---|---|
| circle | any direction | **1.57080** (π/2) | **0.63662** (2/π) | **1.000000** | 0.50000 | 0.50000 |
| egg | 0° | 1.55162 | 0.64449 | 1.000000 | 0.50877 | 0.49123 |
| egg | 90° | 1.61928 | 0.61756 | 1.000000 | 0.48104 | 0.51896 |
| egg | 180° | 1.52053 | 0.65766 | 1.000000 | 0.52936 | 0.47064 |

What the table shows:
- **The equation holds on every convex shape, from every direction.** π/2 and 2/π are the circle's values.
  On the egg both factors move with the direction, and the product stays at 1. This is an identity (the
  outside lens, summed), so what it adds is **which quantity stands on which side**, not a new fact.
- **The hold, averaged over the side, is ⟨h²⟩ + ⟨along²⟩ = 1.**
  - **On the circle it splits ½ + ½ from every direction.** That is the corner's value in squares. The
    circle's side is, on average, at the corner.
  - **On the egg the split moves off the corner with the direction** (0.529 and 0.471 at 180°). **The split
    is where the shape shows.** The product never shows it.
  - In first powers the mean facing, 2/π = 0.637, sits below the corner's 1/√2 = 0.707.
- **Why only the circle keeps its two factors fixed from every direction.** *The Centring* (Theorems B and C)
  gives the footing:
  - A reader that brought no unit can read an arrival only against the arrival's own size.
  - Under that reading, the circle is **the one fixed point**: the one figure that is both the hold and the
    result. With a laid-down stick instead, every figure or none is a fixed point, and the circle is not
    distinguished.
  - So **the "1" of the everywhere equation is the own-size hold**, and π/2 and 2/π are the values that hold
    takes. On any other figure the same product is spread unevenly across directions, and that uneven spread
    is the shape, as the egg rows show. **The circle is the signature of no unit brought**, which is why the
    equation's factors sit still only there.
- **The inside reader has no such equation.**
  - Its lens is 1/h², not h, so its total reading over the side is 2S, from −S to +S, which grows without
    bound with its reach S.
  - Its would-be mean of 1/h² is its reach divided by π/2: 6.4×10⁴ at S = 10⁵.
  - The Cauchy has no mean, so **the everywhere equation exists from outside only.**

> **The hold says each step is two parts of one motion. The everywhere equation says each side is two totals
> of one surface: the serial arc and the parallel width. Their exchange rate is the mean facing. The view from everywhere
> holds that rate as a mean; the two real readers find it at the horizon.**

**A reading, unchecked** (§1.1). π/2 is a **breadth**: the turn of one sweep. 2/π is a mean, and a mean needs
every hanger counted, so it is a **density** quantity. On this reading the equation's product is 1 only for a
view that holds both limits at once, which is everywhere's definition. Nothing here tests that the two factors
must be read this way.

### 0.4 Closure

> **(1 Oct)** The two-component reading normalised to the unit circle is not the situation-3 reader, which cannot be normalised (R135) and is not the unit circle (R127). The two "sides" here are the signs of h, not R149's front and back sides.

> *"Closure is this: horizontal of 1 to a vertical of 1 to a horizontal of 1 to a vertical of 1 back to a
> horizontal of 1."* (Tom, Sep 22)

A closure is four sweeps: H → V → H → V → H. Each sweep is one quarter, π/2 of turn, carrying one bar into the
other. Four of them make 2π, and the bar is back where it started.

**What sums, and what cancels.**
- **Unsigned,** each sweep's shadows add up to one bar (§0.3), so a closure counts **four bars** in each
  shadow.
- **Signed,** the shadows cancel. The horizontal shadow runs + then − and the vertical runs + then −, so over
  a closure **both signed sums are 0.**
- **"Both signed sums are 0" is exactly the closure condition the stitch used (§4).**
  - Across the line of sight, closure fixed the serial side's missing length.
  - Along it, closure was the free check.
  - The stitch *was* this sequence, made to come back to its start.
- **What closure checks is the reader, not the figure** (*The Centring*, Proposition 4).
  - Walk a turn and multiply the residues. The product is 1, and in exact arithmetic it cannot be anything
    else, because it telescopes. So it is **no evidence about the shape**.
  - What it measures is the reader. A reader keeping each residue to 16, 12 or 8 bits misses closing by
    1.1×10⁻⁴, 7.5×10⁻⁴ and 3.3×10⁻³: the grain's amount, not the shape's.
  - The same holds here:
    - the stitch's free check caught the lopsided merge, an error in how one reader was recording;
    - it missed the balanced one (§5.1);
    - it can never supply the tally.
  - **Closure verifies the return and the readers' arithmetic. It does not verify the figure, and it does not
    count.**
- **Closure is one of two checksums, and the stitch ran only the first** (*The Unit Rule* §17):
  - **The reading returns.** The record's moves sum to zero. The sum telescopes, so it is exact, but it is
    **order-blind**: it passes with the moves in any order.
  - **The landmarks return.** The sequence of the record's corner crossings and horizons comes back round to
    where it began. This one is **order-bearing**: it is exactly the sequence the sum forgot.
  - Neither implies the other. "**An open record proves the scene did not return. A closed record does not
    prove it did**", and how much it can refute is priced by the step.
  - The stitch's closure (§4) is the first checksum, which is why it passes a balanced loss (§5.1).
  - **The second, landmark, checksum does not catch a balanced loss either** (§5.1, `landmark.mjs`). The loss
    removes steps between a corner and a horizon, and removes no landmark.

**Where the two readers sit in it.**
- The outside reader's side runs V → H → V: from its horizon, through home, to its other horizon. That is
  **two quarters**, a half closure.
- The inside side is the other two quarters, V → H → V the other way round.
- The seams between them are the two verticals: **the horizons.**
- So a closure is **the outside half and the inside half, joined at two horizons.** "Classical is both sides
  together" and "classical is closure" are the same statement. Measured (§4.2), each side turns π, and the two
  together make 2π.
- **A proposal, for Tom's ruling: this answers the centring's open question about the arch's feet.**
  - *The Centring* §0 reads the half turn as an arch, "the smallest thing that closes and carries".
  - It leaves open "what the reader's span rests on: the horizon at each side is either the next freedom
    along, or nothing at all".
  - The stitch suggests a third answer: **each reader's half rests on the other's, at the two horizons.**
    Neither half stands alone, and a closure is two arches meeting at their feet.
  - One part is *not* carried over: the centring's keystone-as-corner. In a reader's half, home sits in the
    middle, not the corner, so that mapping has to be checked against the four sweeps first.

**Why neither reader closes alone.**
- The reading v/h repeats every half closure. The run H → V → H reads 0 → ∞ → 0, and so does the next one.
  - This is the Passage's double cover. The second round trip is the same ground with the other party
    describing, and nothing in the reading tells the two apart.
- What does tell them apart is **the side**, the sign of h. That is precisely what is undefined at the
  horizon (§2.3), where h = 0.
- So **closure requires crossing both horizons while keeping the side, and the single ratio does not keep the
  side there.**
  - It is the ratio that loses it, not every reading. *The Centring*'s reader keeps **both** components
    against the pair's own size, (v, h)/r. That keeps the sign of h.
  - Its image is the whole unit circle when the reader is enclosed (Theorem A: every reading lands on it to
    2.2×10⁻¹⁶, 360° covered).
  - **Holding one ratio gives the half; holding both normalised components gives the whole.**
  - That second reader is still a single point with no tally of horizons crossed. It is the corpus's
    two-register reader, not a third view.
- **The move can keep it** (*The Fisheye as a Lens* §2.2, §2.4; `serial.mjs` S7):
  - Read as magnitudes |v|/|h|, the serial reader's compose move changes sign four times a lap, at home and
    at the horizon, twice each. The reader appears to **bounce**.
  - Read signed, the compose move stays constant and the reader **turns straight through** the horizon.
  - The ratio move cannot cross the horizon at all. Home and the horizon are its fixed points.
  - So **the facing is carried by the signed move, step by step, exactly as the bar's continuity carries it.**
    The single ratio does not carry it. The two-component own-size reading does (above).
  - **Whose continuity is it?** *The Unit Rule* §16: "continuity is not a property the world has and hands
    to the reader. It is the shape of the only door a one-value reader can come through."
    - What carries the facing through the horizon is the reader's own carry rule, whether that is the signed
      move or the bar's unbroken sweep.
    - So **the side kept across the horizon is kept by the reader, not handed over by the world.** At the
      horizon itself the world supplies no side at all (§2.3). What the reader supplies is the claim that
      nothing reversed while it was not able to see.
- **What the serial reader still lacks is the tally of horizons crossed.**
  - Its composed reading runs out of reach a quarter turn from wherever it started
    (`serial-inside-outside.md` P3).
  - So it keeps the facing across each step but cannot count how many horizons it has passed, and so cannot
    know it has closed.
  - The stitch in §4 used a reading (a ratio of motions), not signed compose moves. That is why it had to
    assign each half to its side by hand.
  - **The assignment is the join,** and a reader keeping signed moves would carry part of it itself: the
    facing, though not the tally.

**Closure and N.**
- Everywhere's N is the count of one closure.
- Each real reader counts at most its half, between its two horizons.
- Under rotation (§0.1b), labelled points reached N after half a turn, because the outside reader already
  holds one half and needs the other half to come round. With labels, one half-closure of motion completes
  the closure.
- Without labels, the count never completes. The reading repeats every half closure, so a reader cannot know
  it has come round.
- **N = the whole turn ÷ the grain** (*The Fisheye as a Lens* §2.1).
  - Under an even turn the serial reader's compose move is a constant: tan of one step, which is the grain.
    The reader holds it **exactly**. N = 97, 1000, 1001 and 65 537 all held it to within 10⁻¹⁰ over three
    laps (`serial.mjs` S2).
  - The whole turn is the closure: four sweeps, 2π.
  - So **the grain is serial's and the closure is everywhere's, and N is their quotient.** N is not a missing
    number for the serial reader. Its other factor does not exist for that reader.
  - The Boundary §2.1 says the same of 2/π: that it "exists only for a circle someone has completed". That is
    the everywhere equation of §0.3, stated earlier.

**The visual carries the facing** (Tom: *"this has the facing built in to the description. Other visuals
lack the facing visual."*).
- The bar has two ends. Across a closure, "a horizontal of 1" appears three times: at the start, halfway,
  and at the end.
  - As attitudes they are identical, and so is the reading.
  - As facings they differ. Halfway round, the bar has turned half around, and its ends have swapped.
- The sweep never reverses; it continues. So which end leads is carried through each vertical, **through
  each horizon**, by the sweep's own continuity.
- **That is the one thing the single ratio cannot carry,** and the thing the stitch had to assign by hand. What
  does carry it:
  - on the serial side, the signed move;
  - for a reader keeping both components against its own size, the reading itself (above).
- Other visuals leave it out:
  - A circle shows positions, and its first and second passes look the same.
  - The graph of the reading shows 0 → ∞ → 0 twice, with nothing to tell the two apart.
  - The square-and-circle shows the set.
- **The sweeping bar is the only one of these in which the second half of a closure looks different from the
  first.**

> **Closure is four sweeps, four bars unsigned, zero signed. Each reader holds two of the four sweeps,
> between two horizons. The whole is both halves, joined where the ratio loses the side. The signed move
> and the two-component reading keep the side; only the whole supplies the tally; and closure checks the
> readers, not the figure.**

## 1. Three scenarios

> **(1 Oct)** These three scenarios are superseded by the situations of R137, R146, R151 and R152. Both the serial and the parallel reader are in situation 3, the only view from somewhere. "Outside/inside" is now "parallel/serial" (Sep 25).

A reader meets a shape in one of three ways (Tom, Sep 22):

| scenario | what it has | N |
|---|---|---|
| **the view from everywhere**, the classical view | everything | known; never at issue |
| **outside, in parallel** | the outside hemisphere, all at once | **unknown** |
| **inside, serially** | the inside hemisphere, one arrival at a time | **unknown** |

- Parallel is **not** the view from everywhere. Only the view from everywhere has the whole.
- Neither real reader knows N, and both meet horizons.
- Any horizon means N is unknown (Tom, Sep 22).

### 1.1 The view from everywhere, defined: infinite breadth and infinite density

> **(1 Oct)** Since Sep 25 this view is called **the view from nowhere**, so the Nagel contrast below is reversed, and "infinite density" is withdrawn (Sep 24, Sep 30). The g here is the old g (share of hangers placed). Since Sep 30, g is the ratio of reader to world on [0, 1], and the circle has no g (R137).

> *"God's eye view is the view with infinite breadth and infinite density."* (Tom, Sep 22)

**Renamed (Tom, Sep 23): "the view from everywhere, with infinite breadth and infinite density."** The old name,
god's eye, suggested one very good eye: a single standpoint. What is meant is every standpoint at once: every
position read (infinite breadth) and every hanger resolved (infinite density). The new name also says what the
thesis says, that the classical view is the readers' views joined. Tom's own quotes keep the old name as he said
it. The short possessive is *everywhere's* ("N is everywhere's"), and the equation of §0.3 is **the everywhere
equation**.
- **Against the standard phrase.** Philosophy's name for the objective standpoint is Nagel's *The View from Nowhere*
  (1986), a view from no standpoint at all; Haraway (1988) called that ideal "the god trick of seeing everything
  from nowhere." This paper's classical view is the inverse: not from nowhere, but from everywhere at once.
- **Keep the definition attached.** "Everywhere" alone names the breadth. A reader at every position but at a fixed
  fidelity would still have a horizon; the density half is what removes it.
- **It stays unreachable.** Neither real reader has it, and neither does physics as practised.

These are the two limits of a freedom (Tom, Sep 16: "it has two limits, size and density").
- **Breadth** is how much of the closure a view covers.
  - The view from everywhere covers all four sweeps (§0.4), so it has no horizon.
  - Each real reader covers two sweeps, from horizon to horizon.
- **Density** is how finely the hangers are told apart.
  - The view from everywhere tells every hanger apart however many there are: ε → 0, all N drawn.
  - Each real reader has a fixed fidelity.

**The horizon is where the two limits meet.** The horizon is not infinitely far but infinitely dense: the
place where the hangers stop being distinguishable (Tom, Sep 16). So a real reader's breadth ends exactly
where its density runs out. The limb is both the edge of what the outside reader can see and the band in
which its hangers merge (§3.1).

The view from everywhere has no horizon because its density never runs out, so its breadth never has to end. The classical
order, in effect "ε → 0 first, then N → ∞" (§0), is **infinite density taken before infinite breadth**. The corpus's readers get neither:
fixed density, and a breadth cut at the horizon.

**Every limit in this paper is one of the two, or their meeting:**

| limit | § | kind |
|---|---|---|
| the far side; V against N; "N = 2V" failing on the egg | 0.1a | **breadth** |
| each reader holds two of the four sweeps | 0.4 | **breadth** |
| the inside serial reader's horizon is carried, a quarter turn from its start | 0.1a | **breadth** |
| a hemisphere statistic quoted as the whole's; rotation exposing it | 0.1a, 0.1b | **breadth** |
| the mean, and the whole-list law, need the whole count | 0.2 | **both**: every hanger (density) of the whole closure (breadth) |
| no tally of horizons crossed, so no knowledge of having closed | 0.4 | **breadth** |
| the limb hides εN²/(2π²) | 3.1 | **density** |
| the ceiling at N = 2π/ε | 3.2 | **density** |
| each reader goes blind where its lens is slowest; the corner band from N ≈ 4π/d | 3.3 | **density** |
| the inside reader's reach S at the horizon | 3.3 | **their meeting** |
| the hidden steps at the limb that the pair repairs | 5 | **their meeting** |
| the grain; the step of a record | 0.1a, 2.2 | **density** |
| the counting premise: even hangers, a known clock | 4.3 | **density**, supplied as an assumption |

- The breadth limits are what the **stitch** removes: two halves joined make the whole closure (§4).
- The density limits are what the **repair** partly removes: the pair counts across the horizon what each
  alone merges (§5).
- Neither removes both completely. The stitch cannot tally horizons, and the repair cannot go past the
  ceiling.
- **Only the view from everywhere has both at infinity.**

**Where g sits: on the density side, as the one density the reader chooses.**

g is the share of hangers placed: none at 0, which leaves only the unit circle, and all N at 1 (Sep 18 ruling).
So everywhere's infinite density is **g = 1 with every hanger resolved**. Two densities have to be kept apart:
- **g, how many hangers are placed**: the reader chooses it, and it is a dial;
- **ε, how finely the placed hangers are told apart**: this is imposed on the reader.

**The inside reader cannot see g; the outside reader holds it.**
- *The Centring*'s Theorem A: the own-size reading lands on the unit circle **at every g**. The
  two-component reading is blind to g. The inside reader holds the frame, and nothing in it says how many
  hangers the frame carries.
- The stones the outside reader holds are exactly what g changes: the list returned at that g.

**The stitch measures the ratio of the two readers' g, and nothing else about g.**
- §4.4's T3 hung the two sides at spacings in the ratios 0.5, 2 and 3.7. That is the two sides at different g.
- The stitch returned 0.5000, 2.0000 and 3.7003.
- Neither reader can know its own g, since a share of N needs N. **Their ratio is exactly the one factor that
  survives across the horizon**: g cancels inside each reader and leaves one residue between them.
- Reading the spacing ratio as a ratio of g's is an identification, not a separate measurement.

**g against the ceiling** (`gceiling.mjs`, ε = 10⁻³; predictions registered before the run; all passed):

- **G1: the resolved share depends on εgN alone.** gN = 1000, 4000 and 6000 give shares of 0.8960, 0.5600 and
  0.1913, identical at g = 1, 0.5, 0.1 and 0.02. This is an identity rather than a finding: a reader placing
  ⌊gN⌋ even hangers *is* a reader of ⌊gN⌋. What it establishes is that **the ceiling is on gN, not on N.**
- **G2: past the ceiling, turning g down restores resolution.** At N = 100 000, g = 1 resolves nothing.

  | g | placed | resolved | share |
  |---|---|---|---|
  | 1 | 100 000 | **0** | 0 |
  | 0.08 | 8000 | **0** | 0 |
  | 0.06 | 6000 | 574 | 0.19 |
  | 0.045 | 4500 | 1106 | 0.49 |
  | 0.02 | 2000 | 792 | 0.79 |

- **G3: there is a best g, and what it buys is fixed by ε alone.**

  | N | best g | g·N at best | resolved at best | resolved at g = 1 |
  |---|---|---|---|---|
  | 20 000 | 0.206 | 4116 | **1122** | 0 |
  | 100 000 | 0.041 | 4057 | **1122** | 0 |
  | 1 000 000 | 0.0041 | 4079 | **1122** | 0 |

  The best g·N sits near 4100, inside the registered 4000–5000; the small-angle estimate says 4935.
  - **The most a reader of fidelity ε can hold is set by ε alone**: 1122 points at ε = 10⁻³, however large N.
  - N and g decide only whether the reader reaches that number.
  - This is Tom's "g spent at both ends" (Sep 17), measured. Above the best g the limb swallows more than g
    adds; below it there are fewer hangers to hold.

**So g is the reader's answer to its own density limit.** It cannot raise ε, but it can choose how many hangers
to place so that the ones it places stay distinguishable. The view from everywhere has no such choice to make: its density is
infinite, so it takes g = 1 and loses nothing.

## 2. The continuous observer

### 2.0 In plain language: an inside reader points, an outside reader walks

> **(1 Oct)** "Inside/outside" is dropped (Sep 25): read serial/parallel. Depth from the gaps belongs to the parallel reader (R79), but R152 keeps the parallel reader's v on the front side only, not out to the limb.

> *"An inside reader points, an outside reader walks."* (Tom, Sep 22)

**Why inside is serial and projective, and outside is parallel and iterative.** Being inside something means
it surrounds you. Being outside something means it is in front of you.

- **Inside.**
  - When a shape surrounds you, you cannot face all of it at once. To take it in you turn, and turning brings
    it to you one direction at a time. That is why the inside reader is **serial**.
  - What each look gives is a direction: *there is something that way*. It carries no size and no distance.
    A small thing near and a large thing far, in the same direction, look alike.
  - So all the inside reader can do is **point**, and pointing is **projective**. In the corpus's terms,
    each look gives v against h: a ratio with no size in it.
- **Outside.**
  - When a shape is in front of you, its whole facing side is laid out across your view at once, side by side.
    That is why the outside reader is **parallel**.
  - Its sight lines run side by side, not out from a point, so sizes survive. A thing's place across the view
    is a real magnitude.
  - Holding them all together, the reader can go down the list, count them and compare them. That is what
    **iterative** means here: stepping through what it holds.
- **The pairing is a strong default, not a law.** Each half has its own source:
  - serial against parallel comes from whether the reader must **turn** to see it all;
  - projective against counting comes from whether its sight lines **spread from a point** or **run side by
    side**.

  The two can be split. A reader walking round an object is outside and serial. A camera inside a dome is
  inside and parallel (`serial-inside-outside.md`). The pairing holds in the ordinary case because being
  surrounded forces both at once: you must turn, and your sight lines spread from where you stand.

**The two readers are the two accounts of the sweep.**

- **The outside reader walks.**
  - Its v is a distance across the view, so going from one point to the next is a step, and **steps add**.
  - That is why it can total: its width is the sum of its steps, and its gaps are the steps' lengths.
  - Walking is the sweep's **linear** account, the one that covers a length of 1.
- **The inside reader points.**
  - Each look is a direction with no distance in it, and **pointing does not accumulate**. Two pointings do not
    add up to a length.
  - That is the plain reason the Cauchy has no mean (§0.2).
  - Pointing is the sweep's **facing** account, the one that turns through π/2.
- **The everywhere equation is the exchange between the two** (§0.3). Pointing sweeps π/2 while walking covers
  1, so 2/π is how far one walks per unit of pointing. Only a view holding both accounts multiplies them back
  to 1.
- **The two run out of different things at the one horizon.**
  - **The walker runs out of distance.** Walking along a surface that has turned edge-on gains no ground
    across the view: the crowding at the limb (§3.1).
  - **The pointer runs out of direction.** Pointing along the edge-on surface points at something it can
    never name: the reading running to infinity (§2.3).

**The inside reader holds the frame; the outside reader holds the stones** (Tom, Sep 22: *"so the outside
reader is the magnitude list"*). This is *The Centring*'s three parts of a reading, sorted by reader.

| *The Centring* | the reading | here |
|---|---|---|
| erecting the frame | naming the places, with nothing hung on them | **the inside reader.** Its own-size reading divides every magnitude out and lands on the unit circle (Theorem A). It holds directions, the centring, and no stones. |
| laying the stones | the magnitude list, hung on those places; this is where scale enters | **the outside reader.** Its v and its gaps are magnitudes. It is the one reader with access to the list: *"you have just gained access to its magnitude list"* (Sep 21). |
| striking the frame, so the arch stands | dividing: the hold is load-bearing while the reading forms | **the stitch.** The scale that crosses the horizon from outside to inside is the stones giving the frame its size. That is the one number *The Centring* says a reader with no unit is short of (Proposition 2). |

Two qualifications, both from this paper:
- **Half the stones.** The outside reader holds only the stones on its own hemisphere: V of them, not N
  (§0.1a). **The whole list, every stone at once, is everywhere's**, which is why *Browsing*'s "the list was
  there all along" is the view from everywhere (§0).
- **Stones as they project.** What arrives is v, each stone as it falls across the view, not its full
  magnitude. The outside reader turns projections back into magnitudes only through the counting premise:
  gaps give h, and h gives depth (§4.1). Without even hangers it holds the stones' shadows, not the stones.

> **The inside reader holds the frame, the outside reader holds half the stones, and classical is the arch.**

### 2.1 One h, one horizon

> **(1 Oct)** "The horizon" alone means v/h → ∞, never reached (R77). The working horizon is the front side, with the corner at its edge (R149), and g splits at the corner (R150). The stitch "at the horizon" should be reread with that in mind; this is a question to rule on, not a refutation.

Put the outside reader's line of sight along h.
- The outside reader holds **v**, the position across its line of sight, for every point that faces it.
- The inside reader receives **motion**, not values (Sep 20). It gets each step as a ratio: motion along
  the line against motion across it.

**Two kinds of serial reader, and this paper's is the second** (against *Browsing the Fisheye* §2):

| | what each look gives | what cancels | what survives |
|---|---|---|---|
| **the position reader** (*Browsing* §2) | the ratio of a point's two components, seen from a centre: reach·sin ÷ reach·cos | **the reach**, in every arrival: "there is no arrival on which a clover and a circle disagree" | the direction, and the rate at which directions arrive; **no shape** |
| **the motion reader** (this paper) | the ratio of one step's two motions: along the line of sight ÷ across it | only the step's length | the step's direction; given its clock (even hangers), **the form**, as the Whewell equation |

- The two statements are both true, of different readings:
  - *"the Cauchy discards the magnitudes"* is true of the position reader;
  - *"the serial side supplies the far side's form"* (§4) is true of the motion reader.
- The motion reader keeps the form **only through its clock**. That is *Browsing* §3's confound, and §4.3's
  uneven-hangers control is it (§4.3).

**Two ways to form a pair** (*Browsing* §2), for the outside side:
- The two-component ratio, above, cancels the reach and loses the shape.
- The **single-list quotient**, a value over its own increment, cancels only the *gain* and keeps the shape.
- The outside serial reader of `serial-inside-outside.md` records exactly that: how its gaps change,
  ln(gap₂ ÷ gap₁). That is why it came out as the outside parallel reader minus one anchor (P1), shape intact.

For the outside reader, h is how far the surface faces it. For the inside reader, h is the part of the
surface's motion across the line. **These are the same number at every point of every shape**, because the
facing is the motion turned a quarter turn (`sameh.mjs` H1; an identity, not a measurement). So:

> **There is one h and one horizon: h = 0, where the surface turns edge-on.**
> - The outside reader holds the side where h > 0.
> - The inside reader receives the side where h < 0.
> - They meet the same horizon from its two sides.

### 2.2 Two lenses at the one horizon

Per unit of surface:

| | lens | at home | at the corner | at the horizon (h → 0) |
|---|---|---|---|---|
| outside | dv = h | widest | 0.707 | **crowds to nothing** |
| inside, in the reading s = v/h | ds = 1/h² | 1 | 2 | **spreads without bound** |
| inside, in its log z = ln(v/h) | dz = 1/(vh) | **spreads without bound** | **2: its slowest** | **spreads without bound** |

- **The inside reader's lens has two registers.** Both are right; they are one lens written two ways.
  - In s it spreads at the horizon only.
  - In z, the log register the corpus uses, it is **the reading plus its swap**, h/v + v/h. It spreads toward
    **both** ends and is **slowest at the corner**, the same on both sides of it.
  - The z form is the fisheye as *The Fisheye as a Lens* §1 gives it: a lens focused at a central point.
  - It is also why the inside readers went blind **at the corner** at fixed grain
    (`serial-inside-outside.md` P4). A reader goes blind where its lens is slowest.
- In the z register, the step one grain of turn makes is exactly the lens integrated over that grain, to
  8×10⁻¹⁴ (`serial2.mjs` S3′). The lens is resolved only where the grain is small against v·h. Toward home
  and the horizon, a single grain becomes a step of order one.
- Both readers share home and share the horizon.
- They behave in opposite ways at the horizon.
- On an even surface, the outside reader's law depends on the dimension: arcsine on the circle, flat on the
  sphere (Archimedes), Gaussian only as the dimension grows.
- The inside reader's law is the Cauchy in every dimension (`outside.mjs` O4).

### 2.3 What neither can tell at the horizon

**The side is the sign of h, and at the horizon h = 0.**

- **Outside: the view folds.** Points either side of the limb give the same v. The difference is third
  order: 2.9×10⁻⁴, then 10⁻⁷, then 10⁻¹⁰ at δ = 10⁻¹, 10⁻², 10⁻³ turns from the limb (`sameh.mjs` H3).
- **Inside: the reading wraps.** It goes from −855 just before the limb to +855 just after, through the one
  point at infinity.
- **The side lives only in the curvature,** the second-order drop below the limb. Fidelity ε erases that
  drop within √(2ε/k) of the limb (H4).

With your face next to the earth, you cannot tell which side you are on. This is Koenderink's result (1984)
that the contour's curvature carries the surface's.

## 3. The two orders of limits

### 3.1 Outside: the limb hides a share that grows with N

Take the unit circle with N evenly spaced hangers, one step 2π/N apart.
- A distance δ from the limb, the gap between neighbouring v's is about δ · 2π/N.
- That gap is under ε within δ* = εN/(2π) of the limb.
- That band holds δ* ÷ (2π/N) = εN²/(4π²) hangers at each limb.

> **hidden ≈ εN²/(2π²)**, so the **share hidden ≈ εN/(2π²), which grows with N.**

Measured (`outside.mjs` O3):

| N | ε | hidden | εN²/(2π²) |
|---|---|---|---|
| 1000 | 10⁻⁴ | 4 | 5.1 |
| 2000 | 10⁻⁴ | 20 | 20.3 |
| 4000 | 10⁻⁴ | 80 | 81.1 |
| 2000 | 10⁻³ | 206 | 202.6 |

In the classical order, ε → 0 at fixed N, so the hidden count goes to 0 and the limb is harmless. In the
corpus's order, ε stays fixed and N grows, so the hidden share goes up.

**In the reader's own terms, the same statement needs no N.** The outside reader cannot resolve the band
where **h × (its unit) < ε**. Both h and the unit are its own. The count above is only everywhere's measure of
that band.

### 3.2 The ceiling: more points, less seen

Carry §3.1 to its end.
- The widest gap is at home, and it is 2π/N.
- Once that is under ε, **nothing** is resolved.
- So the outside reader has a ceiling at **N = 2π/ε**.
- Below the ceiling, its resolved count rises, peaks, and then falls (`ceiling.mjs`).

| εN | resolved share, ε = 10⁻³ | resolved share, ε = 10⁻⁴ |
|---|---|---|
| 0.5 | 0.944 | 0.949 |
| 1 | 0.896 | 0.898 |
| 2 | 0.792 | 0.794 |
| 4 | 0.560 | 0.561 |
| 6 | 0.191 | 0.192 |
| 6.4 (past 2π) | **0** | **0** |

- **The resolved share depends on εN alone.** The two columns agree to three decimals.
- The resolved count peaks between N = 4000 and 5000 at ε = 10⁻³ (the small-angle estimate puts it at
  π²/(2ε) ≈ 4935).
- After the peak, adding points to the surface **shrinks** what the outside reader holds.

This is invisible in the classical order and is the whole story in the corpus's order.

**In the reader's terms, the ceiling is simply "its unit is under ε":** its widest gap is below its own
fidelity. "More points, less seen" is everywhere's description. The reader holds what it holds and misses
nothing it could name.

**A tension with *Browsing the Fisheye*, stated rather than left for a reviewer to find.**
- *Browsing* §6: a circle "gets denser, never larger", so adding points never overflows the fisheye, because
  **the angle is orthogonal to the count**. That is true **of the angle**.
- At a fixed fidelity, denser eventually means **unresolvable**:
  - the outside reader loses everything past N = 2π/ε (this section);
  - the inside reader goes blind around the corner from about N = 4π/d (§3.3).
- **The address never overflows; the resolution does.** *Browsing* speaks in the classical order, where the
  address is free of fidelity. This paper speaks in the corpus's order, where the resolution is not.

### 3.3 Inside: a fixed share

The inside reader's horizon loss is different. It cannot reach past |s| = S. The points it loses lie within
about 1/S of each horizon, and there are **N/(πS)** of them: **a fixed share, whatever N is.**

For its own half, that is 2/(πS) = 0.0064 at S = 100. Measured: 0.0063–0.0067 from N = 2000 to 80 000.

> **The two readers fail differently at the one horizon:**
> - the outside reader's loss is a share that grows with N (resolution: its lens crowds);
> - the inside reader's loss is a fixed share (reach: its lens spreads).

**Correction, and a sharper statement** (`serial-inside-outside.md` P4). The fixed share above is the inside
reader's loss **at the horizon**. With a fixed grain on its record, the inside reader *also* goes blind
somewhere else: **around the corner**, where its lens in the log register, dz = 1/(vh), is slowest (§2.2).
That band grows with N once N passes about 4π/d (d is the grain; the band appeared between N = 8000 and
32 000 at d = 10⁻³).

The general rule is that **each reader goes blind where its lens is slowest, and that band grows with N**:

| reader | slowest at | blind first at |
|---|---|---|
| outside, parallel | the horizon | **the horizon** |
| outside, serial | home | **home** |
| inside, parallel or serial (ratio move) | the corner | **the corner** |
| inside, serial (compose move) | nowhere | nowhere |

So the difference **at the horizon** stands, and it is what the repair of §5 uses. Where the outside reader
is blindest, the inside reader's lens spreads and it resolves. What does not stand is "the inside reader's
loss is a fixed share" as a statement about the whole inside reader.

### The crowding at the horizon is the Chebyshev nodes

> *"The crowding at the horizon is the Chebyshev nodes."* … *"I'm wondering if there is more here to explore with
> our new insights."* (Tom, Sep 23)

**Already proved in the corpus.** *The Tangent Bridge Theorem*'s Chord Projection Corollary (§9): evenly spaced leaves
on the arc, projected onto the chord by cos, are exactly the Chebyshev nodes of the first kind; their density is the
arcsine law 1/(π√(1 − x²)); they cluster at the chord's edges with spacing ∝ 1/N², TB's *angular horizon*. The same
leaves projected by tan give the Cauchy.

**What it means for this paper.**
- **The outside reader is TB's chord projection.** Evenly spaced hangers seen orthographically, v = sin φ: its
  samples are Chebyshev nodes, its law is the arcsine (§0.2), its limb crowding is the Chebyshev clustering.
- **The inside reader is TB's tan projection**: the same leaves read centrally, the Cauchy.
- **So the two readers are the two classical projections of one evenly spaced set**, Chebyshev outside, Cauchy
  inside, and the horizon is where both crowd.
- **The limb count is a count of Chebyshev nodes.** R(N) = (N/π) arccos(εN/2π) counts those whose neighbour gap is
  still at least ε (*One Reader* §6.1, `rigor.mjs`); the 1122 cap is the most Chebyshev nodes a fidelity-ε reader
  can ever tell apart, 1.1222/ε.
- **The 2/π again.** No node set on an interval can hold the Lebesgue constant below (2/π) ln n − C (Erdős 1961), and
  Chebyshev nodes achieve (2/π) ln n + O(1). TB notes the coefficient is its ψ₁; it is also the everywhere
  equation's exchange rate (§0.3).
- **Two crowdings, not one.** The growing array's newest entries crowd too (§ Static and dynamic arrays), but that is
  the Cauchy kind, on the line: spacing ≈ u/i². Chebyshev is the chord's crowding, the outside reader's; Cauchy is the
  line's, the inside reader's and the dynamic array's. Both fall off as an inverse square toward their horizon.

**What fixed fidelity does to Chebyshev interpolation** (`chebfix.mjs`, predictions registered before each run):

| test | result |
|---|---|
| **C1** all visible nodes (ε → 0) | Lebesgue constant 3.17, 4.05, 4.93 at n = 32, 128, 512, against (2/π) ln n of 2.21, 3.09, 3.97: the Chebyshev growth, (2/π) ln n + 0.96. **Held** |
| **C2** the resolvable nodes only, interpolating over the visible extent [−1, 1] | predicted to worsen past the count's peak. **Failed, in a stronger way**: the moment *any* end nodes merge it is catastrophic. At N = 500, ε = 10⁻³, only 14 of 250 nodes are lost (the kept nodes reach ±0.9956), and the Lebesgue constant is already 1.3×10¹⁶ |
| **C3** Runge's function 1/(1 + 25x²) on the resolvable nodes | predicted to improve and then worsen, best near the peak. **Failed**: the error is 9 to 220 at every N tested, never small |
| **C4** the merged end nodes restored (their positions supplied by the other reader) | Lebesgue back to 4.5 to 5.4: Chebyshev's. **Held** |
| **C5** the resolvable nodes, evaluated only within their own span (no extrapolation) | still above 10¹⁴ at every N, past what double precision can represent: cut off from their end-clustering, the kept nodes behave like evenly spaced nodes near the cut, which is Runge's disaster |

**What this adds** [reading, on C1–C5]:
- **The Chebyshev crowding is load-bearing.** Classically (ε → 0 first) it is what makes the nodes near-optimal,
  meeting Erdős's floor. At fixed ε it is the first thing lost, and losing even a few per cent of the nodes at the
  ends destroys *global* interpolation over the whole visible extent, not just near the limb. Local, piecewise
  reconstruction is unaffected (tested below, `inside.mjs` L1–L4); the damage is to the spectral, whole-side methods.
- **So the order of limits bites harder than the count showed.** "More points, less seen" (§3.2) is about how many
  points; this is about what they can do: a fixed-fidelity outside reader cannot interpolate its own hemisphere
  globally at any N where the limb has merged.
- **The repair is necessary, not just helpful.** Restoring the end nodes from the other side (C4, the fold of §5)
  is exactly what returns the reader to Chebyshev's near-optimal conditioning. The pair recovers what each alone
  cannot even approximate.

### Two octaves, the inside reader's nodes, and a local repair

> *"yes. although, I'm wondering if there is more here to explore with our new insights."* … *"proceed"* (Tom, Sep 23)

Three follow-ups to the Chebyshev finding, each with predictions registered before the run (`twooct.mjs`,
`inside.mjs`). *One Reader* §2.1b and §6.1b carry the same results.

**1. There are two octaves, not one** (`twooct.mjs` F1–F6, all held).
- **The frequency octave** is the angle doubling, s → 2s/(1 − s²): the turn read twice over. On the chord it is
  Chebyshev's T₂(x) = 2x² − 1, which maps the order-16 Chebyshev nodes onto the order-8 ones, each hit twice (F4); it
  is TB's FFT butterfly. It is 2-to-1 (0.7 has the preimages 0.3152 and −3.1724, F1), it keeps an evenly met turn
  evenly met (standard Cauchy quartiles stay at ±1, F2), and it changes cross ratios (×−0.4386, F3), so it is not a
  move of the reader.
- **The scale octave** is the dilation, s → 2s: one rung of the dial's radius, one Doppler octave. It is 1-to-1,
  rescales the Cauchy (quartiles to ±2), and keeps cross ratios (×1.0000). It is a move.
- **They agree near home and part at the corner** (F5). D(s)/(2s) = 1/(1 − s²): 1.0001 at s = 0.01, 1.33 at 0.5,
  50 at 0.99, infinite at the corner. The doubling sends the corner to the horizon, stretching home-to-corner over
  the whole quarter turn; the dilation slides the corner out to s = 2.
- **They do not commute** (F6): D(2s) = 1.875, 2D(s) = 1.319 at s = 0.3.
- [reading] One word serves for both because near home they are the same small step. The corner is where the reader
  has to say which octave it means. The dial's radius is the scale octave; spectral methods run on the frequency
  octave.

**2. The inside reader's nodes are Boyd's rational Chebyshev points** (`inside.mjs` B1–B4, all held).
Boyd (1987) solves problems on the whole line by the map y = L cot t onto t in [0, π], and expands in
TB_n(y) = cos(n arccot(y/L)). Verified before use: the 1987 abstract states the map; the TB_n formula is from a later
paper citing it.
- **B1**: Boyd's points L cot((2j − 1)π/2N) are exactly the Cauchy's midpoint quantiles at scale L (to 9×10⁻¹⁵).
- **B2**: TB_n(y) = T_n(y/√(y² + L²)) (to 4×10⁻¹⁵). The same evenly spaced angles, projected by the chord (x = cos t,
  v, the outside reader, Chebyshev) and centrally (y = cot t, the reading s = v/h, the inside reader, Cauchy).
- **Boyd's domain is the Roman arch**: t over two quarter turns, keystone home, corners at y = ±L, feet the two
  horizons. TB_n(+∞) = 1, TB_n(−∞) = (−1)ⁿ, so the two horizons are distinct: an array, not a ring.
- **What the nodes are good for (B3)**: functions on the whole freedom that are smooth through the horizon.
  exp(y/√(1 + y²)) reaches 3×10⁻¹⁵ by N = 20; exp(−y²), with an essential singularity at the horizon, only
  1.0×10⁻⁵ at N = 40 and 1.9×10⁻⁸ at N = 80.
- **Boyd's L is the dial's radius (B4)**: a feature of width 20 is best caught with L = 20 (error 1.5×10⁻³ at
  N = 16), worse at L = 2 (0.09) or L = 200 (0.8). Choosing L is choosing the octave: put the corner at the
  feature's scale.
- [reading] The outside reader is the spectral method for the chord, the inside reader for the whole freedom. The
  inside reader's nodes spread out toward the horizon instead of crowding, so fixed fidelity costs it nothing
  there; what it cannot do is reach the horizon in finitely many rungs.

**3. A local repair degrades gracefully** (`inside.mjs` L1–L4; L1, L3, L4 held, L2 held from N = 1000). Cubic
interpolation on the four nearest kept nodes, ε = 10⁻³, Runge's function, the edge value held across the lost band:

| N | εN | kept | span | local Lebesgue | error in span | error in band |
|---|---|---|---|---|---|---|
| 500 | 0.5 | 236 | ±0.9956 | 1.49 | 8.7×10⁻⁶ | 3.3×10⁻⁴ |
| 1000 | 1 | 448 | ±0.9862 | 1.58 | 5.5×10⁻⁷ | 1.0×10⁻³ |
| 2000 | 2 | 792 | ±0.9466 | 1.62 | 3.4×10⁻⁸ | 4.3×10⁻³ |
| 4000 | 4 | 1120 | ±0.7700 | 1.62 | 2.1×10⁻⁹ | 2.5×10⁻² |
| 6000 | 6 | 574 | ±0.2955 | 1.63 | 4.2×10⁻¹⁰ | 2.8×10⁻¹ |

- The local Lebesgue constant stays under 1.63, against 10¹⁴ to 10¹⁶ globally on the same nodes.
- The error inside the span falls with N. All the error is in the lost band, where it is the function's own
  variation across the band, and it grows smoothly as the band widens.
- [reading] Global methods lose everything once the limb merges; local methods lose exactly the limb. So the
  pair's repair (§5) is needed only for the band, not for the whole side.

### The dial can set its own radius

> *"proceed."* (Tom, Sep 23, on the open question: can the dial choose its own L?)

The dial's radius is set by hand. Boyd's L is the same control (*One Reader* §6.1b), and Boyd's work shows the best L depends on
the data. Can the reader find it from what it reads? [new: `selfl.mjs`, predictions registered before the run; two
test-design errors fixed before the results below, logged.]

**For entries (an array's values on the freedom), yes, exactly: put the corners at the quartiles.** Set L to half the
interquartile range. For Cauchy data this recovers the scale within 0.6% at scales 0.003, 1 and 250 (B1, held), and
the entries' angles are then evenly met, KS distance 0.004 to 0.006 (B2, held). Half the entries always sit between
the corners, by construction. For data spread over six decades no single L evens the arch: KS 0.14 with the
quartile rule and 0.14 with the best L found by search (B3 predicted above 0.2; **failed** as stated, the point
survives). One radius serves one octave; spreading many octaves evenly is the log register's job, the dial's digits.

**For a function, the same rule works to within about an octave and a half.** The reader samples f at its own nodes,
finds where the samples change (the variation between neighbouring nodes), puts the corners at that variation's
quartiles, and repeats. Starting from L = 1:

| feature | best L (search, true error) | quartile rule L | octaves apart | error vs best |
|---|---|---|---|---|
| width 0.05 | 0.25 | 0.073 | 1.8 | ×2.95 |
| width 1 | 4.0 | 1.6 | 1.3 | ×2.52 |
| width 20 | 90.5 | 28.5 | 1.7 | ×3.34 |
| width 1000 | 4100 | 1570 | 1.4 | ×2.65 |
| Lorentzian, width 0.05 | 0.088 | 0.048 | 0.9 | ×110 |
| Lorentzian, width 20 | 32 | 18.9 | 0.8 | ×32 |

- **It never gets lost.** From L = 1 it reaches a feature three decades away in four steps (13.5, 105, 693, 1600),
  then hovers within ±7% of its value (the variation is located only to the node gaps).
- **It is scale-equivariant.** For one feature shape the ratio of best L to the rule's L is about 2.5 to 3.4 at every
  width from 0.05 to 1000: the rule tracks the octave, with an offset set by the feature's shape.
- **Registered A1 (within one octave) failed** for the mixed feature (1.3 to 1.8 octaves) and held for the
  Lorentzian (0.8, 0.9). **A2 (within ×3) held** for five of the six single features, failed at width 20 (×3.34), and
  failed badly for the Lorentzian, whose best error is 10⁻⁷ and falls off steeply away from the best L.
- **The obvious rule fails completely.** Choosing the L whose coefficients look most converged (least energy in
  their last quarter) picks L ≈ 3×10⁻⁵ every time: there the feature lies beyond the outermost node, the samples are
  flat, and a flat set of samples looks perfectly converged. **A reader that sees nothing thinks it is done.** Whatever
  rule sets the radius has to look for where the samples change, not for how quiet they are.
- **Two octaves defeat one radius** (A3, held): features of widths 0.1 and 100 together give a best error of 0.79 on
  the whole L ladder, 230 times worse than either alone. One reader, one octave; two features far apart need two
  readers or a local method (the local repair above).

[reading] So the dial can set its own radius: the rule is "corners at the quartiles", for entries or for change.
For entries it is exact; for a function it finds the octave and misses the best L by a shape-dependent factor.

*One Reader* §6.1c condenses these results.

### What sets the best radius: the poles and the horizon

> *"proceed"* (Tom, Sep 23, on the quartile rule's offset)

the section above left an offset between the quartile rule and the best radius. Boyd's convergence theory says what should set
the best radius [cited: Boyd 1987; Boyd 2001]. On y = m + L cot t, a pole of f at the complex point y_k sits at
t_k = arccot((y_k − m)/L), and the cosine series converges like exp(−Nρ), where ρ is the distance of the nearest such
point from the real t axis. **The pole rule**: choose the centre m and radius L that push the nearest pole furthest
from the arch. [new: `poles.mjs`, `parity.mjs`, predictions registered before each run.]

| test function | pole rule (m, L) | best found (m, L) | apart | predicted rate e^(−16ρ) | measured err₃₂/err₁₆ |
|---|---|---|---|---|---|
| R1 Lorentzian, width 1 | 0, 1 (exact) | 0, 1.19 (tie at 10⁻¹⁵) | 0.25 oct | exact | exact |
| R2 widths 1 and 4 | 0, 2 | 0, 2 | 0 | 1.5×10⁻⁴ | 1.5×10⁻⁴ |
| R3 width 1 centred at 3 | 3, 1 (exact) | 3, 1.19 (tie) | 0.25 oct | exact | exact |
| R4 double pole + 0.5y/(1 + (y − 1)²) | 0.5, 1.09 | −1, 4 | **1.88 oct** | 1×10⁻⁵ | **0.5** |
| R5 widths 1 and 100 | 0, 10.4 | −0.5, 11.3 | 0.13 oct | 0.21 | 0.22 |

- **The pole rule holds** where its premise holds (P1, P2): four of five cases, with the convergence rate predicted
  to two figures. **For two scales the best radius is their geometric mean** (2 for widths 1 and 4, 10 for 1 and
  100): the corner sits between the two octaves, and the rate falls as they separate (ρ = 0.55, then 0.10).
- **R4 failed, and the failure is at the horizon.** Its second term tends to 0.5/y at both horizons. Near a foot of
  the arch y ≈ L/t, so f meets the horizon **with a slope in the angle**, and every cos(nt) has zero slope there.
  Convergence becomes algebraic (err₃₂/err₁₆ = 0.5) whatever the radius. Registered after that failure and held
  (P4, P5): adding sines drops the error from 9.8×10⁻³ to 4.0×10⁻⁵ with the same 31 functions, and puts the best
  radius 0.12 octave from the pole rule; without the odd term the cosines alone are exact (9×10⁻¹⁶). This is the
  problem the later literature calls parity mixing and handles with hybrid bases [cited: arXiv:1703.07441].
- **The quartile rule is local; the pole rule is global.** Single pole: the quartile rule agrees within 0.1 octave
  (P3, held). Widths 1 and 4: it also agrees (P3 predicted a miss; **failed**). Widths 1 and 100: it settles at 1.1,
  11 or 101 depending on where it starts (from 0.01, 10 and 100): three resting places, one near each feature and one
  at the balance point. It finds *an* octave where things change, not necessarily the best one.

[reading] Two things set the radius. The poles set how far each feature reaches off the line, and the best corner
sits where the nearest reach is longest: the geometric mean for two scales. The horizon sets the parity: a function
that leaves the horizon with a slope needs the sines, the odd half of the arch's basis. The test feature of the section above
has such a tail (u/(1 + (u − 1)²) ~ 1/u) and a tanh term, which likely accounts for most of that section's offset;
this was not re-run.

*One Reader* §6.1c condenses these results.

### The reader finds its radius by sweeping

> *"proceed"* (Tom, Sep 23, on having the reader estimate its own poles)

The pole rule needs the poles, and the reader has only samples. Two ways for the reader to find its radius from what
it reads [new: `decay.mjs`, predictions registered before each run; one script bug fixed before judging, logged]:

**1. Measure your own convergence (the decay rule).** At each trial centre and radius, the reader takes the slope of
its own coefficients' envelope (the measured ρ) and keeps the steepest, sweeping every octave from 2⁻¹⁰ to 2¹⁴.

| test function | pole rule L | decay rule L | measured ρ | pole-rule ρ there | apart |
|---|---|---|---|---|---|
| R1 width 1 | 1 | 1 | 18 (exact) | exact | 0 |
| R2 widths 1 and 4 | 2 | 2 | 0.557 | 0.549 | 0 |
| R3 width 1 at 3 | 1 (m = 3) | 1 (m = 3) | 18 (exact) | exact | 0 |
| R4 odd tail | 1.09 | 2.38 | 0.319 | 0.364 | 1.13 oct |
| R5 widths 1 and 100 | 10.4 | **279** | 0.312 | **0.004** | **4.75 oct** |

- **Where every feature is seen, it works exactly** (E1, E2 held for R1–R3): the reader reads the pole rule's rate
  off its own coefficients, 0.557 against 0.549.
- **R5 fools it** (E1, E2 failed). At L = 279 the nodes nearest home are 13.7 apart, and the width-1 feature falls
  between them. The reader sees only the wide feature, which is smooth, and measures fast convergence. **A feature
  narrower than the node gap near home is invisible, and a reader at that radius cannot know it is there.** This is
  the dual of the flat-field trap of the radius section above: there the feature was beyond the outermost node, here it is between two
  central ones.
- **The flat field is nearly, not fully, unrewarded** (E3 failed narrowly): at L = 2⁻¹⁰ the measured rate is 0.070,
  over the 0.05 predicted.
- **The odd tail is not flagged** (E4 failed): over 28 coefficients the algebraic decay of R4 looks geometric,
  0.32. The reader cannot tell parity trouble from its coefficients at this N.

**2. Check each radius against the others (the cross-check rule).** As the dial sweeps its radius it has read 32
samples at every octave, 800 in all. Score each candidate radius by the worst misfit of its 32-term reading to all
the swept samples, and keep the least. Registered after the decay rule failed on R5, before this code ran:

| test function | pole rule (m, L) | cross-check (m, L) | misfit | apart |
|---|---|---|---|---|
| R1 | 0, 1 | 0, 1.19 (tie at 10⁻¹⁵) | 4×10⁻¹⁵ | 0.25 oct |
| R2 | 0, 2 | 0, 2 | 4.6×10⁻⁸ | 0 |
| R3 | 3, 1 | 3, 1.19 (tie) | 3×10⁻¹⁵ | 0.25 oct |
| R4 | 0.5, 1.09 | −1, 4 | 3.1×10⁻³ | 1.88 oct |
| R5 | 0, 10.4 | −0.5, 11.3 | 6.6×10⁻² | 0.13 oct |

- **The cross-check finds the true best in all five cases**: its choices are exactly the best found with the true
  error in the poles section above, R4 included. R1–R3 and R5 held.
- **R4 failed as registered** (1.88 octaves from the pole rule, predicted within 1), but the failure is the pole
  rule's: R4's true best is also at L = 4, because of its odd tail (the poles section above).

[reading] One radius cannot find its own best setting: it cannot see what lies beyond its outermost node or between
its central ones. **The sweep can**: the readings at other octaves see what this one misses. The dial's radius
sweep, which the dial already does to browse, is also what lets a reader calibrate itself. This is the order of
limits again (§3.2), in the reader's own terms: at a fixed radius, what lies beneath the grain is not just unseen
but unknowable; across radii, it is seen.

*One Reader* §6.1c condenses these results.

### What the sweep costs, and what it reveals at the horizon

> *"proceed"* (Tom, Sep 23)

What the sweep of the sweeping section above costs, and whether the reader can see the odd tail that defeated the pole rule [new:
`sweep.mjs`, predictions registered before each run; 32 readings per octave throughout].

**A few octaves are enough to choose; many are needed to know you can stop.**
- **Fixed sweep** (S1) for R5, widths 1 and 100, starting at radius 1. The sweep covers w octaves either side:
  - w = 0, 32 readings: radius 1, the narrow feature only;
  - w = 1, 96 readings: radius 5.66;
  - w = 2 to 4, 160 to 288 readings: radius 9.51, a quarter octave from the full sweep's 11.3 and closer to the pole
    rule's 10.4;
  - w = 6 or more: 11.3.

  **Held** for w = 0 and for success by w = 4 (it succeeded at w = 2); w = 1 fell between the predicted outcomes.
- **Adaptive sweep, stop when the best reading predicts the new octaves** (S2). R1–R3 stop after 5 or 6 octaves (160
  to 192 readings) with the full sweep's choice. **R4 and R5 never stop** (failed): a 32-term reading of a two-scale
  or odd-tailed function is never good to 10⁻³, so no new octave ever counts as predicted.
- **Adaptive sweep, stop when two new octaves in a row see a flat field** (S2', registered after S2 failed). Every
  case now stops with the full sweep's choice: 23 to 28 octaves, and 32 for R4 (predicted within 30; **failed**
  narrowly). The cost is set by the tolerance and how fast the tail flattens, not by the features: a 1/y² tail is
  flat to 10⁻³ about ten octaves out.

[reading] The flat field, which fooled a single radius twice (the radius and sweeping sections above), is the right signal for stopping the sweep:
seeing nothing new, twice, is when to stop looking.

**The odd tail is visible in the sweep, exactly.**
- **Fitting the three samples nearest each foot** (D1, D2) finds R4's odd coefficient (0.48 and 0.51 against 0.5,
  **held**). **But it also flags R2 and R5 (failed)**: at their chosen radii the outermost nodes are only a few
  widths out, not yet where the tail is simple.
- **Comparing the same node across octaves** (D3, registered after D2 failed, **held exactly**). Node j at octave
  k + 1 sits at exactly twice node j at octave k, so the sweep reads f at y and 2y for free. The quantity
  O = 2y(f(y) − f(2y)) is the odd coefficient for an odd tail and halves with each octave for an even one. At
  octaves 10 to 12, at both feet, the ratio from one octave to the next is 1.000 for R4 and 0.500 for R1, R2, R3
  and R5.

[reading] The sweep's octaves are doublings in y (the scale octave of the two-octaves section above), so a reader that sweeps compares each
reading with its own double, and the ratio names the tail's order: 1 for 1/y, ½ for 1/y², ¼ for 1/y³. The reader
learns from its own sweep whether it needs the sines.

*One Reader* §6.1c condenses these results.

### A cheaper stop: the regime

> *"proceed"* (Tom, Sep 23)

The flat-field stop of the sweep-cost section above costs 23 to 32 octaves. A cheaper stop: **stop each side once it has entered its
simple regime**, where one octave looks like the last one scaled by a power of 2 [new: `regime.mjs`, predictions
registered before each run].
- **High side**: the octave ratio of O = 2y(f(y) − f(2y)) at both feet (the sweep-cost section above).
- **Low side**: the spread of the octave's samples.

A side stops once its ratio has sat within 2% of 1, ½, ¼ or ⅛ for two octaves running.

| case | features' span | octaves (readings) | low / high ratio | choice = full sweep's? |
|---|---|---|---|---|
| R1 width 1 | 0 | 13 (416) | ¼ / ½ | yes |
| R2 widths 1, 4 | 2 | 14 (448) | ¼ / ½ | yes |
| R3 width 1 at 3 | about 2 | 16 (512) | ½ / ½ | yes |
| R4 odd tail | about 2 | 16 (512) | ½ / 1 | near tie: 3.55×10⁻³ against 3.13×10⁻³ |
| R5 widths 1, 100 | 6.6 | 19 (608) | ¼ / ½ | yes |
| R6 widths 1, 10⁴ | 13.3 | 25 | · | yes |

- **The ratios name the regimes** (T2, held once the fix below was in). At home, ¼ means the function is even there
  (f − f(0) ∝ y²) and ½ means it has a slope. At the horizon, ½ means a 1/y² tail and 1 means a 1/y tail.
- **The stop costs 30 to 40% fewer octaves than the flat-field stop.** The prediction was at most 14 octaves (T1);
  it held for R1, R2 and R4 on the first run and failed for R3 (16) and R5 (19).
- **One false settle** (run 1): on the low side R4's spread "settled" at ratio 1 while its outer nodes still saw the
  features. A spread that does not shrink is not a regime. With ratio 1 excluded on the low side (T3, registered
  after that run), R4's low ratio is ½ as predicted, but it took 16 octaves, and its choice (m 0.5) differs from the
  full sweep's (m −1). The two are near a tie in true error. **T3 failed** on both counts.
- **The cost has a form** (T4, registered from run 2's counts, **held**). The node nearest each foot sits
  cot(π/64) = 20.3 times the radius out, 4.3 octaves, and each side needs two confirming octaves. So the stop costs
  about (the features' span in octaves) + 2 × (4.3 + 2) ≈ span + 12.6 octaves. Predicted 24 to 28 for R6 (widths 1
  and 10⁴); it took 25, with the full sweep's choice.

[reading, **withdrawn in the next section**] ~~The fixed overhead, about 13 octaves, is the arch's own reach.~~ At N = 32 the
count is span + 12.6, but the overhead does not grow with N as the reach does; the next section gives the correct reading.
Features cost one octave per octave of span.

*One Reader* §6.1c condenses these results.

### The sweep's width does not depend on N

> *"proceed"* (Tom, Sep 23)

the regime section above's cost formula put the overhead in the arch's reach, log₂ cot(π/2N) octaves per side, which grows by one octave
each time N doubles. Tested at N = 8 to 128 [new: `regimeN.mjs`, predictions registered before the run]:

| N | R1: octaves swept | R1 readings | R5: octaves swept | R5 readings | formula (R1 / R5) |
|---|---|---|---|---|---|
| 8 | −7..4 = 12 | 96 | −7..11 = 19 | 152 | 8.7 / 15.3 |
| 16 | −8..3 = 12 | 192 | −8..10 = 19 | 304 | 10.7 / 17.3 |
| 32 | −9..3 = 13 | 416 | −9..9 = 19 | 608 | 12.7 / 19.3 |
| 64 | −10..3 = 14 | 896 | −10..8 = 19 | 1216 | 14.7 / 21.3 |
| 128 | −11..3 = 15 | 1920 | −11..7 = 19 | 2432 | 16.7 / 23.3 |

- **The formula is wrong** (U1 failed; off by up to 4.3 octaves). It matched at N = 32 only because it was fitted
  there, and T4's success in the regime section above was at N = 32 too.
- **What happens instead: the whole window slides, and its width does not change.** Each doubling of N moves both
  ends down one octave. The low end drops because the octave's spread includes the outermost node, which reaches
  further, so the radius must be smaller before every node is near home. The high end drops because the outermost
  node reaches the tail sooner. For R5 the width is 19 octaves at every N. R1's width grows by one octave per
  doubling only because its high end hits a floor: the sweep starts at octave 0 and cannot confirm a regime before
  octave 3.
- **The ratios do not depend on N** (U2, held): ¼ at home, ½ at the horizon, for both, at every N.
- **Fewer nodes, fewer readings** (U3, held): the sweep costs N × width, so N = 8 is cheapest (96 and 152 readings).
  Whether N = 8 also *chooses* well was not tested here.

[reading, correcting the regime section above] The sweep's overhead is not the arch's reach. It is the distance a side must go into its
regime before the ratio settles to 2%, plus two confirming octaves, and none of that depends on N. The node count
buys detail within each reading, not a shorter sweep. For finding the octave, a coarse reader sweeping is as good
as a fine one, and cheaper.

*One Reader* §6.1c condenses these results.

### A coarse reader to find the octave, a fine one to read it

> *"proceed"* (Tom, Sep 23)

the previous section left open whether a coarse reader also *chooses* the radius well. Two stages: an N = 8 sweep with the regime
stop, the cross-check on 8-term readings to choose (m, L), then one N = 32 reading at that choice. Compared with the
N = 32 sweep [new: `coarse.mjs`, predictions registered before the run]:

| case | coarse choice (readings) | fine choice (readings) | error, coarse then fine / fine alone | apart |
|---|---|---|---|---|
| R1 width 1 | 0, 1.00 (96 + 32) | 0, 1.19 (416) | 4×10⁻¹⁵ / 4×10⁻¹⁵ | 0.25 oct |
| R2 widths 1, 4 | 0, 2.00 (112 + 32) | 0, 2.00 (448) | 4.6×10⁻⁸ / 4.6×10⁻⁸ | 0 |
| R3 width 1 at 3 | 3, 1.00 (128 + 32) | 3, 1.19 (512) | 4×10⁻¹⁵ / 4×10⁻¹⁵ | 0.25 oct |
| R4 odd tail | 0.5, 1.00 (128 + 32) | 0.5, 4.00 (512) | 1.6×10⁻² / 3.5×10⁻³ (×4.4) | 2 oct |
| R5 widths 1, 100 | −3, 19.0 (152 + 32) | −0.5, 11.3 (608) | 0.24 / 0.066 (×3.7) | 0.75 oct |
| R6 widths 1, 10⁴ | 0, 4.00 (200 + 32) | 3, 128 (800) | 1.0 / 0.92 | 5 oct |

- **Where one octave dominates, the coarse reader chooses exactly as well** (R1–R3, and R2's two close scales), with
  under a third of the readings: V1 and V2 held. For the single features it even lands on the pole rule's exact
  radius, 1.00.
- **Where the best radius is a compromise, the coarse reader drifts.** It is off by ×4.4 for R4 (odd tail) and ×3.7
  for R5 (scales 6.6 octaves apart): V1 failed for both. V2 held for R5 (0.75 octave) and failed for R4 (2 octaves).
  An 8-term reading cannot represent the compromise it is choosing for, so its choice follows what it can represent.
- **R6 is beyond any one radius at N = 32**: both choices leave an error near 1 (the ratio passes V1, but neither
  reading holds the function). V2 failed (5 octaves). Two features 13 octaves apart need two readers or a local
  method (the local repair above), as the poles section found.
- **The readings held**: 29 to 32% of the fine sweep's in every case.

[reading] So the design is: **a coarse reader sweeps to find the octave, and a fine reader reads at it.** This is
exact when the data has one octave and loses a few-fold when it has two. When the octaves are far apart, no single
radius serves, and the sweep's job changes. It no longer finds the one radius; it finds where the readers should go.

*One Reader* §6.1c condenses these results.

### Several readers placed from one sweep

> *"proceed"* (Tom, Sep 23)

When no single radius serves (the previous section), the sweep should say where to put several readers. The rule: bin the change
seen by the coarse sweep (N = 8) by octave of |y|, find its clusters, and put one reader at each cluster's median
octave. The readers (32 cosines each) are then fitted jointly, by least squares, to their own samples and the sweep's
[new: `place.mjs`, predictions registered before each run].

| case | run 1: clusters split by 3 quiet octaves | run 2: split at valleys, readers centred | best single radius (the previous section) |
|---|---|---|---|
| R1 width 1 | 1 reader, 3.0×10⁻¹² | 1 reader, 1.6×10⁻⁷ | 4×10⁻¹⁵ |
| R2 widths 1, 4 | 1 reader, 1.4×10⁻⁵ | 1 reader, 2.9×10⁻⁷ | 4.6×10⁻⁸ |
| R3 width 1 at 3 | 1 reader, 8.4×10⁻³ | 1 reader, 4.3×10⁻⁵ | 4×10⁻¹⁵ |
| R5 widths 1, 100 | **1 reader**, 0.22 | **2 readers (L 1.03 and 98.8)**, 6.2×10⁻⁶ | 0.066 |
| R6 widths 1, 10⁴ | **2 readers (L 1.41 and 1.16×10⁴)**, 3.6×10⁻¹² | 2 readers, 8.2×10⁻⁷ | 0.92 |

Readings: the coarse sweep (96 to 200) plus 32 per reader.

- **Two readers do what no one radius can** (W2 held for R6). Widths 1 and 10⁴ go from 0.92 with the best single
  radius to 4×10⁻¹² with two readers, 264 readings in all. Each reader sits at its feature's octave: 1.41 and
  1.16×10⁴.
- **R5's gap is not quiet** (W1 and W2 failed for R5 in run 1). The width-1 feature's 1/y² tail fills the six octaves
  before the width-100 feature, so a quiet-gap rule sees one cluster. Splitting at **valleys**, the bins lower than
  half the smaller peak on either side, finds both (W4, registered after run 1, **held**): two readers at 1.03 and
  98.8, error 6.2×10⁻⁶, against 0.066 for the best single radius. The other counts were unchanged.
- **Centring from a coarse sweep is crude** (W5 failed). R3's centre came out at 2.8, not 3. Its radius (3.09 where 1
  is right) was measured from 0, not from the centre: a flaw in the rule. It also cost the exact cases: a centre
  0.002 off takes R1 from 10⁻¹² to 10⁻⁷.

[reading] The sweep does more than choose a radius. Its change profile, binned by octave, is a map of where the
data's octaves are, and one reader per peak reads what one radius cannot. This is the dial's hybrid (*One Reader* §7; the Roman-arch section above) run as a
method. The coarse sweep is the browse. The peaks are the addresses. Each fine reader is a lens set at one address.

*One Reader* §6.1c condenses these results.

### Readers at their own centres: two directions

> *"proceed"* (Tom, Sep 23)

the previous section placed readers by octave and centred them badly. The rule tried here is greedy and centres each reader first.
Put a reader where the unread part of the data (the residual) peaks. Take a local coarse sweep there. Measure its
radius from its own centre, as the half-width at half maximum. Refit all readers together and repeat, stopping at 4
readers [new: `centre.mjs`, predictions registered before the run; one script bug fixed before judging, logged].

| case | readers placed (centre, radius) | error | octave rule (previous section) |
|---|---|---|---|
| R1 width 1 | 1: (0, 1.26) | 7.6×10⁻¹⁴ | 1.6×10⁻⁷ |
| R3 width 1 at 3 | 2: (2.999, 1.25), (−18, 7.4) | 7.7×10⁻¹⁰ | 4.3×10⁻⁵ |
| R7 width 1 at −20 and at 30 | 4: (−20.01, 1.16), (30.02, 0.98), then two small ones | 2.4×10⁻⁷ | not tried |
| R5 widths 1, 100 | 4, the first at (0, 10.1) | 1.6×10⁻² | 6.2×10⁻⁶ |
| R6 widths 1, 10⁴ | 4, the second at (1.03×10⁴, 4380) | 1.9×10⁻⁴ | 8.2×10⁻⁷ |

- **Side by side, the greedy rule finds the centres** (Z1, Z2 centres held): 2.999 for R3, and −20.01 and 30.02 for
  R7. R1 held (Z4). The octave rule cannot do this, because it bins by distance from one centre.
- **But it over-places and under-reads** (Z1, Z2 failed on counts and errors). R3's radius came out at 1.25 against
  1 (0.32 octave, over the ¼ predicted), because the half-maximum is found only to the nearest sample. Once the main
  readers are in, the leftover residual draws extra readers. The errors were 7.7×10⁻¹⁰ and 2.4×10⁻⁷, against the
  10⁻¹⁰ and 10⁻⁸ predicted.
- **Nested, the greedy rule fails** (Z3 failed). For R5 the half-width of the combined peak is 10.1, between the two
  features' widths, so the first reader serves neither. The rest chase what is left: 1.6×10⁻², against 6.2×10⁻⁶ for
  the octave rule. For R6 the wide feature's reader lands off-centre, at 1.03×10⁴.

[reading] The two rules find the two directions of the space of readers. *One Reader* §3.3 says that space is the hyperbolic
plane, with a centre and a radius for each reader. **The octave rule finds features nested at one centre, along
the radius. The greedy rule finds features side by side, along the centre.** Each is blind in the other direction.
A rule that places readers over the whole data has to search the plane in both directions. One candidate: read
each gap between neighbouring swept samples as a point of the plane (its midpoint as the centre, half its length as
the radius), weight it by the change across it, and put one reader per cluster in hyperbolic distance. Not yet run.

*One Reader* §6.1c condenses these results.

### One rule over the whole plane: failed; and the prior art

> **(1 Oct)** The method comparisons in this run of sections ("best earlier rule", "100× better") are engineering framing, out of scope (Sep 27). They are not wrong. Keep the geometry (reader-plane directions, the order of limits) and set the rankings aside.

> *"yes"* (Tom, Sep 23, to running the plane search and then checking the literature)

the previous section ended by proposing one rule over the whole plane of readers [new: `hplace.mjs`, predictions H1–H4 registered
before each run]. **It failed twice**:
- **Run 1: each gap between neighbouring samples as a point of the plane.** A single width-1 feature came out as
  three readers, because a gap sits on *one flank* of a feature: the two flanks of R1 cluster separately, at ±0.8.
  A wide feature's gaps scattered into clusters too small to keep: R6 got no reader at the width-10⁴ feature (error
  0.98), and R7 got none at 30 (0.55). H1–H3 failed in every case except R2 and R5, whose errors improved
  (4.8×10⁻⁸ and 2.6×10⁻⁷) with the wrong reader counts.
- **Run 2: each reading's own quartile interval as the point.** Registered after run 1. It was worse (R7 7.3, R8
  0.49). An 8-node reading locates change only to its node gaps, so the points jitter by a gap. The extra readers
  overlap, and the joint fit degrades.

[reading] A reader is the geodesic spanning a feature's two flanks, not a point on one flank. A coarse reading is
too coarse to place that geodesic in both directions at once. **The two single-direction rules of the two previous sections each work
in their own direction.** The untried composite is simpler than the plane search: the greedy rule for the centres,
then the octave rule at each centre.

**Prior art.** Checked Sep 23 against the numerical-analysis literature, claim by claim:

| result (old *One Reader* §) | already known | what is left for us |
|---|---|---|
| inside nodes = rational Chebyshev points; TB_n = T_n under y/√(y² + L²) (§6.1b) | Boyd 1987; Boyd 2001 | the reading: the two readers as the two projections; Boyd's domain as the arch |
| the best L is set by the poles; formulas for L (§6.1e) | Boyd 1982 derives "simple analytic formulas for choosing the optimum … mapping parameter L" | none as mathematics |
| locating the singularities from samples and adapting the map to them (§6.1f) | Tee & Trefethen 2006 (Chebyshev–Padé locates the singularities, a conformal map adapts the grid); Cueto-Felgueroso & Juanes 2009; AAA finds poles from samples (Nakatsukasa, Sète & Trefethen 2018) | none as mathematics |
| choosing map parameters by minimising an error measure over the samples (§6.1f cross-check) | Alexandrescu et al. (mapped Chebyshev for multiple scales, parameters by minimising error functionals) | the sweep as the dial's own browse |
| parity at the horizon; sines needed (§6.1e) | hybrid TB/SB bases (arXiv:1703.07441) | the reading as a slope at the arch's feet |
| the tail's order from octave ratios (§6.1g–h) | estimating an order from successive ratios (Richardson, Aitken) is classical | the nested nodes of the sweep giving the ratio for free |
| local interpolation stable where global fails (§6.1c) | textbook | its reading as "local methods lose exactly the limb" |
| flat-field and between-node traps (§6.1d, §6.1f) | aliasing and under-resolution, textbook | tying both to the order of limits |
| placement along the radius and along the centre (§6.1k–l) | multi-domain and adaptive methods place resolution routinely | the two directions read as the plane of readers (*One Reader* §3.3) |

**Verdict**: the same as *One Reader* §8's. **The methods of this run of sections are known; what is ours is the joining**: the
inside reader as Boyd's method, the dial's radius as Boyd's L, the dial's sweep as the calibration. The rigorous
paper should cite Boyd 1982, Boyd 1987 and Tee & Trefethen 2006 for the pole rule and the sweep, and claim only the reading.
Boyd 1982's formulas were not read (abstract only), and neither was Tee & Trefethen's text.

*One Reader* §6.1c condenses these results. (The § numbers in the table above refer to *One Reader*'s pre-condensation layout: §6.1b–c are now §6.1b, and §6.1d–n are §6.1c.)

### The composite: greedy centres, then the octave rule at each

> *"proceed"* (Tom, Sep 23)

The composite rule was left untried: greedy centres, then the octave rule at each centre. At each centre it keeps
only **two-sided** octave clusters (at most 80% of the change on one side), because a reader spans both flanks and a
one-sided cluster belongs to another centre [new: `composite.mjs`, C1–C3 registered before run 1; run 2's and run 3's
acceptance tests registered before each; one script bug fixed before judging, logged]. Final run:

| case | readers | error | best earlier rule | C1 count | C2 ×10 | C3 place |
|---|---|---|---|---|---|---|
| R1 width 1 | (0, 1.08) | 8.9×10⁻¹⁴ | 7.6×10⁻¹⁴ | held | held | held |
| R2 widths 1, 4 | 3 | 8.2×10⁻⁸ | 4.8×10⁻⁸ | failed | held | · |
| R3 width 1 at 3 | (2.999, 1.08) | 3.3×10⁻⁸ | 7.7×10⁻¹⁰ | held | failed (×42) | held |
| R5 widths 1, 100 | (0, 1.08), (0, 111) | **3.6×10⁻¹²** | 2.6×10⁻⁷ | held | held, 10⁵ better | held |
| R6 widths 1, 10⁴ | (0, 1.08), (0, 6680) | 2.8×10⁻¹¹ | 3.6×10⁻¹² | held | held | failed (0.58 oct) |
| R7 width 1 at −20, 30 | (−20.01, 1.08), (30.02, 1.08), one extra | 3.6×10⁻⁷ | 2.4×10⁻⁷ | failed (3) | held | held |
| R8 R5 plus width 1 at 40 | (0, 1.08), (0, 104), two near 40 at 35.8 and 39.4 | 5.5×10⁻⁶ | · | failed (4) | failed (predicted < 10⁻⁶) | failed |

- **Nested features are now solved.** Two readers at one centre, each at its own octave, read widths 1 and 100 to
  3.6×10⁻¹². That is five orders better than any earlier rule, and it uses 664 readings.
- **Side by side, the centres are found** (R7), but the rule adds an extra reader.
- **The weak point is the acceptance test: when to stop adding readers.**
  - Run 1 stopped only below 10⁻⁹, tighter than a 31-term reading reaches, so leftover residual drew spurious
    readers (R3 got six).
  - Run 2 kept a centre only if it halved the *worst* residual. A reader at one of two side-by-side features cannot
    do that, since the other still holds the worst point, so R7 got none.
  - Run 3 used the root-mean-square residual instead: the table.
- **The centre is refined only to the nearest sample.** The feature at 40 in R8 was approached from 35.8 and never
  reached.

[reading] Placing readers in both directions of the plane now works where features are nested or well separated.
What is left is not geometry but **model selection**: when one more reader is worth its readings. That is a textbook
question (stepwise selection, information criteria), and the rule should borrow an answer, not invent one. Beyond
that, iterating the centre (re-sweep at each new residual peak until it stops moving) would fix R8's third feature.
This line stops here.

*One Reader* §6.1c, item 5, condenses this.

### The composite with a borrowed acceptance test

> *"proceed"* (Tom, Sep 23)

The two fixes the composite needed [new: `composite2.mjs`, predictions registered before the run]:
- **The acceptance test**, borrowed rather than invented: the Bayesian information criterion. The data have no noise,
  so the residual is floored at 10⁻¹⁰ of the range. A centre's readers are kept only if the criterion falls.
- **The centre**, iterated: re-sweep at each new residual peak until it stops moving.

| case | readers | error | composite (previous section) | K1 count | K2 ×10 of best |
|---|---|---|---|---|---|
| R1 width 1 | (−0.00005, 1.08) | 2.8×10⁻⁹ | 8.9×10⁻¹⁴ | held | **failed** |
| R2 widths 1, 4 | 3 | 9.1×10⁻⁸ | 8.2×10⁻⁸ | failed | held |
| R3 width 1 at 3 | (3.000, 1.08) | 1.8×10⁻⁹ | 3.3×10⁻⁸ | held | held |
| R5 widths 1, 100 | 2 at one centre | 1.5×10⁻¹⁰ | 3.6×10⁻¹² | held | held |
| R6 widths 1, 10⁴ | 2 at one centre | 2.5×10⁻⁹ | 2.8×10⁻¹¹ | held | **failed** (×680) |
| R7 width 1 at −20, 30 | **(−20.00, 1.08), (30.00, 1.08)** | **2.2×10⁻⁹** | 3.6×10⁻⁷ | **held** | held, 100× better |
| R8 R5 plus width 1 at 40 | 4, the last two at 35.4 and 39.4 | 5.7×10⁻⁶ | 5.5×10⁻⁶ | failed | failed |

- **The borrowed test fixes the side-by-side case.** R7 gets exactly two readers at the right centres, with an error
  of 2.2×10⁻⁹, a hundred times better than any earlier rule.
- **Iterating the centre costs the centred cases.** The centre settles 5×10⁻⁵ off true, taking R1 from 10⁻¹⁴ to
  10⁻⁹ and R6 from 10⁻¹¹ to 10⁻⁹. The reason is exact: **a reading with an even number of nodes never samples its own
  centre**, so picking the largest sample can place a centre only to the nearest node offset. Here that is the
  finest octave's, 2⁻¹² × cot(7π/16) ≈ 5×10⁻⁵.
- **R8's third feature is still missed** (K3 failed: 39.37, not 40). The iteration moves between nodes, and from
  35.4 the nodes near 40 are too far apart to land on it.

[reading] The acceptance question is settled by borrowing: an information criterion with a precision floor gives
the right reader count where the separation is clean. The centre question has an exact limit: **a reader locates a
peak only to its node spacing, and never at its own home.** Fitting the peak between samples (parabolic, or the
pole rule's own centre) would lift that limit. That is the obvious next step for anyone building this, and it is
standard.

*One Reader* §6.1c, item 5, condenses this.

## 4. Classical is both sides together

### 4.1 The stitch

Give each reader only its own side (`bothsides.mjs`).

- **Outside.** Its lens is dv = h, so each gap in v is h measured in hanger spacings. At home h = 1, so
  **the widest gap is the spacing**. With that unit, the hold gives each step's motion along the line of
  sight, √(1 − h²) spacings. That is the depth. Under the counting premise, the outside reader holds h in
  its gaps.
- **Inside.** It holds each step's direction, with no length.
- **At the horizon.**
  - The inside walk must come back to where the outside walk began, measured across the line of sight,
    where v is absolute. That fixes the inside reader's one missing length. **The scale crosses the horizon
    from the parallel side to the serial side.**
  - **"Absolute" means absolute in the outside reader's own view, not in an external unit.**
    - *The Unit Rule* §3 applies in full: a magnitude means nothing without a unit, and the gain between the
      surface and the reader is unknown.
    - The outside reader's unit is its own widest gap. So the scale that crosses the horizon is **that
      reader's own unit**, and the rebuilt shape carries its gain.
    - No external unit enters anywhere in the stitch.
  - Each of the two steps that straddle the horizon is the average of what the two sides last saw.
  - Closure along the line of sight is left unused, as a check.

### 4.2 Results

> **(1 Oct)** The one number carried across the stitch is the analogue of situation 5's single approximately known breadth of v, the Cauchy's scale (R146, R147).

N = 4000:

| shape | V + R | worst error | inherited length ÷ unit | closure along | each side turns |
|---|---|---|---|---|---|
| circle | 2000 + 2000 | 2.5×10⁻⁷ | 1.00000 | 3.1×10⁻⁷ | 0.999 π |
| egg | 2020 + 1980 | 2.5×10⁻⁷ | 1.00000 | 3.1×10⁻⁷ | 0.999 π |
| trefoil | 2218 + 1782 | 6.1×10⁻⁷ | 1.00000 | 5.0×10⁻⁷ | 0.999 π |
| squircle, tilted | 2000 + 2000 | 7.1×10⁻⁷ | 1.00000 | 9.9×10⁻⁸ | 0.999 π |

- **The stitch never uses N.** Counting the rebuilt hangers afterwards gives V + R = N, but that is the view from
  everywhere checking the result. The rebuild did not need the count.
- **The whole turn is π + π.** Each side turns a half turn, even when the counts differ.
- **Every point has both coordinates,** up to one slide along the line of sight that no reader fixes and
  classical does not need.
- **The error falls as 1/N²,** so for the continuous observer the rebuild is exact.
- **What the serial side lacked was exactly one number.** Two claims meet here, and they have different
  standing:
  - **Shown in this paper:** the stitch needs exactly one scale carried across the horizon, the inside step
    length L in the outside reader's unit, and closure fixes it (§4.1; §4.4 T3 identifies it as the ratio of
    the two holds).
  - **Imported, not shown here:** that a serial reader with no unit is *by its nature* one number short, all
    of the form and none of the size. That is *The Centring*'s proposition, and this paper leans on it rather
    than proving it. Taken apart from the corpus, "one number short" would need a formal statement (what a
    reader holds, up to which group) before it could stand as a result.

  *The Centring*'s Proposition 2:
  - A reader with no unit holds **all of the form, exactly, and one number short**: the size.
  - Its residues from one direction, plus one magnitude, rebuild the figure to 2.2×10⁻¹⁶. The same figure at
    scales 0.25, 1 and 40 gives residues identical to 4.4×10⁻¹⁶.
  - That is `serial-inside-outside.md` P1 (serial = parallel minus one anchor) from the other side.
  - **The one number is what the stitch carries across the horizon**, from the parallel side, where v is
    absolute, to the serial side, which has only form.

### 4.3 What carries it

| control | result | what it shows |
|---|---|---|
| uneven hangers (±30 %) | worst error 0.54 at every N | **the counting premise carries the depth** |
| a dented shape | 6 horizons, error 2.2 | **convexity carries the "two"** |

**The uneven-hangers control is *Browsing the Fisheye*'s confound.** *Browsing* §3: "a reader that does not
know its own clock cannot tell a shape it met from a rhythm it kept". There, a bent object swept evenly and a
plain extent swept unevenly gave identical arrivals.

The counting premise, even hangers, *is* the reader knowing its clock. Take it away, and the outside reader's
gaps and the serial reader's step count can no longer tell the surface's turning from the schedule's. The
rebuild then fails at 0.54 whatever N is. **What carries the depth is the clock, and the clock is not in the
reading.**

**This is the same boundary *The Centring* draws.** Its propositions and its reading map hold only where the
figure is star-shaped about the reader, where each direction meets the figure once. Where a direction meets
it twice there is no r(u), no residue, and no single horizon pair. The dent crosses that line, and both
results stop at it for the same reason.

### 4.4 The stitch is a two-group tower

*Degrees of Freedom* §5.10 ("how freedoms scale", formerly the tower of holds) and §5.12a make three claims:
- inside a group, the group's hold cancels;
- across groups, **exactly one factor is left**: the ratio of the two groups' holds;
- the level above removes that factor, and **replacing a hold moves nothing built on it**.

Read the stitch as such a tower:
- **group A** is the outside reader, whose hold is its unit, the widest gap;
- **group B** is the inside reader, whose hold is its step length, which it never holds;
- **the level above** is closure.

Registered before running (`towercheck.mjs`, N = 4000, circle and egg; all four passed on both):

| test | result |
|---|---|
| **T1** outside hold replaced: every v multiplied by a gain k = 0.001, 7, 1000 | the rebuild scales by exactly k; composites (ratios of distances within the rebuild) move by **≤ 1.7×10⁻¹²**; L ÷ unit stays **1.000000** |
| **T2** inside hold replaced: its steps scaled by 0.01, 3, 500 | composites move by **0**. It only ever uses the directions |
| **T3** the two groups hung at **different** spacings, the inside side at ρ times the outside's | **L ÷ unit = ρ**: 0.5000, 2.0000 and 3.7003 for ρ = 0.5, 2, 3.7. The shape is still rebuilt, worst error 2×10⁻⁴ to 9×10⁻⁴ |
| **T4** rebuilt in the inside reader's unit instead of the outside's | composites move by **4×10⁻¹⁶** |

**What this says:**
- **The scale that "crosses the horizon" is the tower's cross-group residue.** It is exactly one factor, the
  ratio of the two readers' holds. When both sides share the hangers it is 1; when they do not, it is their
  ratio, and closure recovers it.
- **Neither reader's hold is retained in what is built** (T1, T2). That is *Degrees of Freedom* §3.1's
  centring: the denominator is load-bearing while the rebuild forms and absent from it.
- **Which reader supplies the top hold does not matter** (T4). The rebuilt shape is the pair's, stated in
  whichever reader's unit one chooses.
- **The everywhere equation's exchange rate, 2/π (§0.3), is this residue written as a mean.** The view from everywhere holds it
  as the mean facing; the pair finds it by closure. This identification is by structure; the residue measured
  here is L ÷ unit, not the mean itself.

**One caveat on the numbers.** With two independent hanger sets the two steps at the seam belong to neither
group. They are given the mean of the two holds. That is why the base error here, 2.2×10⁻⁴, sits above
§4.2's 2.5×10⁻⁷, where both sides were cut from one set of hangers. The seam's length is the one place the
tower's arithmetic does not reach, which fits the seam being where the side is lost (§0.4).

## 5. At fixed ε: the pair repairs the horizon

With ε fixed, the outside reader loses a band at each limb. It knows neither the limb's v nor how many
points it lost (`repair.mjs`). The inside reader resolves its own near-horizon steps, because its lens
spreads.

The limb is a fold, so to second order the surface just past the horizon mirrors the surface just before
it. So:

> **The number of steps the outside reader cannot resolve equals the number of inside steps whose motion
> across the line of sight is under ε.**

The pair knows its own ε, so it can take the outside's hidden steps from the inside and fill them in. The
rule is the reader's ε against the reader's spacing. **No N is involved.** The count columns below are the audit
of the view from everywhere; the result is the shape.

| shape | N | ε | hidden | count, alone | count, the pair | worst error, alone → the pair |
|---|---|---|---|---|---|---|
| circle | 2000 | 10⁻⁴ | 22 | 1978 | **2000** | 1.9×10⁻² → 2.5×10⁻³ |
| circle | 4000 | 3×10⁻⁵ | 26 | 3974 | **4000** | 1.4×10⁻² → 1.2×10⁻³ |
| egg | 2000 | 10⁻⁴ | 20 | 1980 | **2000** | 1.7×10⁻² → 2.5×10⁻³ |
| trefoil | 2000 | 10⁻⁴ | 16 | 1984 | **2000** | 1.6×10⁻² → 2.5×10⁻³ |

- The repaired errors are at the scoring floor: the distance to the nearest true hanger, at most about half
  a spacing.
- **The fold works through the count, not the direction.** Copying the inside steps *without* mirroring
  them works almost as well (2.9×10⁻³). At the horizon every step runs nearly straight along the line of
  sight, so the part a mirror flips is below ε anyway.

> **The horizon is a loss for each reader alone, and not for the pair.**

### 5.1 What closure cannot see

> **(1 Oct)** The circle has no landmarks of its own (R137); these are the reader's, in situation 3. The count of eight per closure is to be checked against R88 (three landmarks of two kinds).

The steps a loss removes at the top horizon run one way along the line of sight; those at the bottom run
the other way.
- **A loss that is the same at both horizons cancels in the closure.** Closure stayed at 10⁻⁶ with 22 points
  missing.
- **Closure sees only the difference between the two horizons' losses, never their sum.**
- So the repair cannot come from closure. It has to come from the other side's count.
- This is *The Centring*'s Proposition 4 met from the other side. Closure is a check on the readers' own
  arithmetic, and a loss that the readers' arithmetic cannot tell apart from a return passes it (§0.4).
- It is also *The Unit Rule*'s asymmetry. The stitch's closure is the order-blind checksum, and a closed
  record does not prove a return. A balanced loss is one of the near-returns that checksum cannot refuse.

**The order-bearing checksum does not catch it either** (`landmark.mjs`; predictions registered before the
run). The landmarks are the horizons (the step runs along the line of sight), the homes (the step runs
straight across it) and the corners (the step at 45°). A convex closure has eight, in the order
H C home C H C home C, one eighth of a closure apart (§0.1a's M).

| test | result |
|---|---|
| **L1** the landmark sequence of the rebuilt closure, with the loss and with the repair | **unchanged** on the circle (N = 2000 and 4000), the egg and the trefoil. The sequence passes the balanced loss. Predicted |
| **L2** the sequence should break once the loss reaches the corner, near the ceiling | **failed.** On the circle at N = 2000 the sequence stayed H C home C H C home C with 81 % of the outside half lost (εN = 6). Predicted to break near εN ≈ 4.4 |
| **L3** the count between landmarks, compared across the horizon: the outside's steps from its corner to the horizon against the inside's from the horizon to its corner | **catches the loss on the circle**: −1 and +1 with no loss; −12 and −10 with 22 hidden, a shortfall of 11 at each horizon. Predicted |
| **L4** the same count comparison on shapes that are not mirror-symmetric across the horizon | **false alarms larger than the loss**: the egg is off by +15 and +16 with no loss at all, against a loss of 10 per horizon; the trefoil is off by about 200. Predicted |

**What this says:**
- **The sequence is blind because the landmarks live in each reader's own unit.** The outside reader finds
  its corner against its own widest gap, and the inside reader has all its corners whatever the outside
  lost. The seam steps join them. A loss thins the run between a corner and a horizon; it never takes a
  landmark out of the sequence. L2 failed because the sequence survives even a loss most of the way to home.
- **What catches the loss is a count, not an order.** L3 is *The Unit Rule*'s landmark checksum with its
  counts kept: M on each side of the horizon.
- **But comparing counts across the horizon assumes the two arcs are mirror images**, and only the circle's
  symmetry gives that (L4). The fold is local; the count from a corner to the horizon is not.
- **So neither checksum finds the loss on a general shape. The loss is not detected; it is inferred.** The
  repair (§5) does not check anything. It applies the fidelity rule: the pair's own ε against the inside
  reader's spacing in the band where the fold holds, right at the horizon. That is local, which is why it
  works on the egg and the trefoil, where every global check fails.

## 6. What the classical accounts take as given

Every piece of §2 and §4 is classical. It should be cited, not claimed.

| piece | where it is |
|---|---|
| the horizon: the shadow boundary, contour generator or rim | convex geometry (Blaschke); Koenderink |
| the fold at the limb | Whitney; Koenderink & van Doorn (1982) |
| the side lives in the curvature | Koenderink (1984) |
| depth from the gaps of an evenly spread surface | shape from texture (Gibson; Witkin 1981; Aloimonos 1988) |
| a shape from equal steps of known direction | the Whewell equation (1849); the turning function |
| π + π = 2π | Hopf's Umlaufsatz |
| the rim recovered from a moving silhouette | Giblin & Weiss (1987); Cipolla & Blake (1992). *Cited from memory; to be checked* |

**What those accounts assume is N in disguise.** Shape from texture's homogeneity assumption is a counting
assumption: the elements are spread at an even, known density. It is exactly this paper's counting premise,
and it fails the same way (§4.3).

**What they do not do is take the limits in the corpus's order.** Here is what that order adds:
- **a share hidden that grows with N**, and **a ceiling past which more points means less seen** (§3.1–3.2);
- **two different failures at one horizon**: one grows, one stays fixed. With the general rule behind it:
  each reader is blind where its lens is slowest (§3.3);
- **the whole classical shape rebuilt by two readers who never use N** (§0.1, §4.2). Classical holds N;
  the pair has no need of it;
- **the pair counting what each alone loses** (§5);
- **closure being blind to a balanced loss** (§5.1).

A first search found none of these five as stated. Not finding something is weaker evidence than finding
it, and the search was a first pass.

**The arrays have their own check** (What an array is, "The literature check"). There the finding runs the
other way: most of the machinery is already known, as consistent hashing, the hyperbolic browser, list
labeling, floating point and fisheye views. What remains is the sorting.

## 7. What is open

- **The landmark checksum on the stitch: run, and closed** (§5.1, `landmark.mjs`). The sequence passes the
  balanced loss; the count between landmarks catches it only on shapes mirror-symmetric across the horizon.
  Still open: whether a count check exists that is local enough to hold on a general shape and is not just
  the repair's fidelity rule restated.
- **Anchoring the depth on a lattice.** The stitch's depth is an unanchored sum of steps, so one step hidden
  at the limb moves everything after it (§4.3, `bothsides.mjs` K3).
  - *The Unit Rule*'s record does not drift, for a structural reason: every level it holds is a rung of the
    lattice anchored at its founding arrival. So its reconstruction is the nearest-rung projection of the
    signal, independent of the path (*The Unit Rule* §15).
  - Whether anchoring the outside reader's depth the same way would confine the limb damage to the seam is
    untested.
- **A vocabulary collision, for Tom's ruling.** *Browsing the Fisheye* §2's treadmill picture calls **the
  reader a walker** on the writer's belt. §2.0 here says **"an outside reader walks."** They are different
  uses: in *Browsing* the walker's pace is the held term, and here walking is the linear account. One of them
  needs a different word. (§0.3 had also called the *serial* reader a walker, against §2.0; that use is now
  removed, so inside this paper only the outside reader walks.)
- **The dented shape.** Several horizons means several sides of each kind. Is classical then "all the sides
  together", stitched at every horizon, with each pair counting across its own horizon?
- **The grain, g < 1.** Stepping over hangers is a different kind of unevenness from the ±30 % jitter
  tested here.
- **3D.** The horizon becomes a curve rather than two points, and the stitch and the repair run along the
  whole of it. "3d is just serial + parallel" (Sep 19). This paper is its 2D case.
- **Past the ceiling.** Beyond N = 2π/ε the outside reader holds nothing distinct. Does the pair still
  hold anything there, with the inside reader alone and a count with no scale?
- **Whose departure is it?** An even traverse seen from off-centre and a warped traverse seen from the centre
  give **the same stream, arrival by arrival**, for every prefix (*The Fisheye as a Lens* §3.2).
  - The serial reader sees all of a departure and cannot say whose it is.
  - Everywhere's law sees half of it and attributes nothing either.
  - Where a thing is, when it arrives, and where the reader stands remain **one freedom on both sides.**
    Whether the stitch, which fixes where each side is, breaks that freedom is untested.
- **Signed moves in the stitch.** §0.4 predicts that an inside reader keeping signed compose moves carries the
  facing through the horizon, so the stitch should need to assign only the tally, not the side. That is
  untested.
- **The modelling choice.** "In parallel" was taken as the far reader, with parallel sight lines. A reader
  at a finite distance forms a ratio against its distance. Which scenario that reader belongs to is Tom's to
  rule.
  - *Evidence toward the ruling, not the ruling* (*The Centring*, Theorem A). A reader standing **outside at
    a point**, reading against its own size, covers **only an arc** of the circle, not a hemisphere: 50.8° of
    the three-lobed figure, 64.8° of a crescent.
  - So a pointing reader outside is a case of its own. It is neither the far parallel reader nor the enclosed
    inside reader: **outside by position, pointing by verb.**

## Kill log

**Withdrawn during the day:**
- **"The inside and outside horizons are different places" (`inside-plus-outside.md` §3–§4).** It came
  from placing the inside reader at a point and giving it position ratios. By the Sep 20 ruling, the serial
  reader receives motion. Read that way, both readers share h and there is one horizon.
- **"Inside + outside gives depth or the whole, not both" (`inside-plus-outside.md` §5).** It came from the
  same error, plus leaving the outside reader's gaps unused.
- **"The outside reader does not hold h" (`the-outside-hemisphere.md` §0).** Under the counting premise it
  holds h in its gaps.
- **"The free closure check catches the limb loss" (`both-sides.md` §3).** It caught it only because that
  test's merge rule was lopsided. Closure is blind to a balanced loss (§5.1).

**Registered predictions that failed:**
- **The limb damage would stay at the seam** (`bothsides.mjs` K3). It does not, because depth is
  accumulated.
- **Mirroring the inside steps would be what does the repair** (`repair.mjs` R3). It is the count, not the
  mirror.
- **The landmark sequence would break once the loss reached the corner** (`landmark.mjs` L2). It never
  broke, even with 81 % of the outside half lost: the landmarks are found in each reader's own unit, and the
  inside reader keeps all of its own.
- **Global interpolation on the resolvable Chebyshev nodes would degrade gradually past the count's peak**
  (`chebfix.mjs` C2, C3). It fails outright the moment any end nodes merge.
- **Local interpolation would be accurate to 10⁻⁶ in the kept span at every N** (`inside.mjs` L2). It was
  8.7×10⁻⁶ at N = 500, where the nodes are still coarse; it held from N = 1000 on.
- **The radius from the data** (`selfl.mjs`). Two test-design errors first, fixed before any prediction was
  judged: run 1's test feature, exp(…)·cos(y/a), kept oscillating out to the horizon, so it had no width; run 2
  measured the error on a grid in the reader's own angle, which at a far-off L never visits the feature. Then, on
  run 3: A1 (within one octave) failed for the mixed feature, 1.3 to 1.8 octaves; A2 (within ×3) failed at width 20
  (×3.34) and for the Lorentzian (×32, ×110); B3 predicted KS above 0.2 and got 0.14. The tail search, the first
  rule tried, failed every time: flat samples look converged.
- **The pole rule for R4** (`poles.mjs` P1): 1.88 octaves off, with algebraic convergence. The pole rule assumes
  the function is even at the horizon; R4's 0.5/y tail is not. Fixed by adding sines (`parity.mjs` P4, held).
- **The quartile rule would miss for two scales** (`poles.mjs` P3): for widths 1 and 4 it agreed with the pole rule.
- **The decay rule** (`decay.mjs`). Script bug first, fixed before judging: run 1's envelope took the max over
  pairs of coefficients, and R2 at L = 2 keeps only every fourth, so two exact zeros read as convergence. Then:
  E1, E2 failed for R5 (a narrow feature between the central nodes); E3 failed narrowly (0.070 against 0.05); E4
  failed (R4's algebraic decay looks geometric over 28 coefficients). The cross-check rule X1 failed only for R4,
  where the pole rule itself fails.
- **The sweep** (`sweep.mjs`): S1 left w = 1 between the predicted outcomes; S2 (stop when predicted) never stopped for
  R4 and R5; S2' (the flat-field stop) took 32 octaves for R4 against 30 predicted; D2 (the three-sample slope at
  the feet) flagged R2 and R5, which have no odd tail.
- **The regime stop** (`regime.mjs`): T1 (at most 14 octaves) failed for R3 (16) and R5 (19); run 1's low side
  took ratio 1 as settled for R4; T3, with that excluded, still took 16 octaves for R4, and its choice was a near tie
  with the full sweep's rather than equal to it.
- **"The overhead is the arch's reach, log₂ cot(π/2N) per side"** (the regime section; `regimeN.mjs` U1 failed). The
  window slides with N; its width does not change. T4's success was at the N the formula was fitted at.
- **Coarse sweep, fine reading** (`coarse.mjs`): V1 (within ×3) failed for R4 (×4.4) and R5 (×3.7); V2 (within
  1 octave) failed for R4 (2) and R6 (5).
- **Placing readers** (`place.mjs`): W1 and W2 failed for R5 in run 1 (one cluster; the gap between its features is
  filled by the narrow one's tail); W5 failed (R3's centre at 2.8, radius measured from 0 rather than the centre).
- **Greedy centring** (`centre.mjs`). Script bug first, fixed before judging: the baseline's threshold (|y| > 10⁵) lay
  beyond every coarse sample, so the baseline was NaN. Then: Z1 failed on count (2), radius (0.32 octave) and error
  (7.7×10⁻¹⁰); Z2 failed on count (4) and error (2.4×10⁻⁷); Z3 failed for R5 (1.6×10⁻²) and R6 (1.9×10⁻⁴).
- **One rule over the plane of readers** (`hplace.mjs`): H1–H3 failed in run 1 (flanks cluster apart; wide
  features scatter); H4a–d failed in run 2 (coarse readings jitter by a gap).
- **The composite** (`composite.mjs`). Script bug first, fixed before judging run 2: the residual "before" a new
  centre was computed after its readers were added, when basis and coefficients no longer matched (NaN), so every
  centre was accepted. Then, final run: C1 failed for R2 (3), R7 (3) and R8 (4); C2 failed for R3 (×42) and R8
  (5.5×10⁻⁶); C3 failed for R6's radius (0.58 octave) and R8's third centre. Run 2's worst-residual test gave R7 no
  readers.
- **Composite with BIC and centre iteration** (`composite2.mjs`): K1 failed for R2 (3) and R8 (4); K2 failed for
  R1 (the centre 5×10⁻⁵ off: an even-node reading never samples its own centre), R6 (×680) and R8; K3 failed (R8's
  third centre at 39.37).
- **Novelty of the Sep 23 spectral sections**: the methods are known (Boyd 1982, 1987; Tee & Trefethen 2006; AAA 2018; Alexandrescu
  et al.). Only the joining is ours.

**Qualified after reading *The Centring* (Sep 22):**
- **"No reading keeps the side through the horizon"** (§0.4, written earlier the same day) was too broad. The
  **single ratio** v/h loses the side. A reading of both components against the pair's own size keeps it, and
  an enclosed reader of that kind covers the whole circle.

**Corrected after an independent audit of *One Reader* (Sep 23):**
- **"The tower's bit n ↔ Doppler factor 2ⁿ, at 3/5, 15/17 …"** conflated celerity rungs (s = 1, 2, 4) with
  Doppler octaves (rapidity steps of ln 2). They agree only far out (the dial's own 0.5623 against ln 2).
- **"A change of radius is a boost"** used celerity as s in one row and the sky's stereographic coordinate in the
  next. A boost rescales the second, not the first.
- **"Each doubling of the list costs the same proper time"** holds only for n ≫ c; rapidity is asinh, not ln.
- **"The horizon the array never reaches is the light …"**: the speed of light, not the observer's event horizon.

**Corrected on Tom's ruling that an array is not a shape (Sep 23):**
- **"The outside reader reads the stones on its facing half"; "the outside reader gets half the stones,
  projected"; "closure as four sweeps: going round the array".** Each treated the array as a shape. An array
  does not close, has no facing, and is one quarter turn. It has no halves, no limb and no second side. What
  carries over from the two readers is the verb (pointing and walking), not the side. The scope table was
  re-split: *any list on one quarter turn* against *needs a shape*.
- **The count ceiling and the re-uniting scale had been tied to the shape's parallel ceiling and the stitch.**
  They share the form, not the cause.

**Corrected when the dynamic array was added (Sep 22):**
- **"An array that grows at its end changes no address it has already given"** (The practical application)
  mixed the two layouts. It is true of the dynamic array on the freedom, whose addresses are absolute. It is
  false of the static array on the quarter turn, whose addresses are shares and move with N (`dynarray.mjs` D3).

**Narrowed after the external review (Sep 22):**
- **"The classical accounts take ε → 0 first"** became *in effect*. It is a statement about working after the
  resolution limit has been taken, not about how each result was derived (§0).
- **"A law is a tally, and a tally needs N"** became a statement about the **whole-list empirical law** only
  (§0.2).
- **"The Cauchy has no mean … it is the law of a reader that has no N"** became an observational reading.
  The missing moment is the distribution's own fact, and no new cause is proposed (§0.2).
- **"The inside reader's loss is a fixed share"** holds at the horizon only. At a fixed grain the inside
  reader is also blind around the corner, and that band grows with N (§3.3). The review had singled this
  contrast out as the paper's strongest result; the corrected form keeps the contrast *at the horizon*, which is
  what the repair uses.
- **Not taken from the review:** its "Level 6" ties the Cauchy to the serial account. Measured, it goes with
  the **inside position**, not the serial verb (`serial-inside-outside.md` P2).

**Bookkeeping slips, caught:**
- **`join.mjs`** first merged points against a cluster's first point, not against its neighbour.
- **`ceiling.mjs`** printed the inside reader's loss share against 1/(πS). The share of its own half is
  2/(πS), and that matches.

---

Sources:
- [Koenderink 1984, *What does the occluding contour tell us about solid shape?*](https://journals.sagepub.com/doi/10.1068/p130321)
- [Koenderink & van Doorn 1982, *The shape of smooth objects and the way contours end*](https://doi.org/10.1068/p110129)
- [Aloimonos, *Shape from texture: general principle*](https://www.sciencedirect.com/science/article/abs/pii/0004370289900660)
- [Gårding, *Shape from texture and contour by weak isotropy*](https://www.sciencedirect.com/science/article/abs/pii/000437029390106L)
- [Whewell equation](https://en.wikipedia.org/wiki/Whewell_equation)
- [Hopf Umlaufsatz (Harvard Math 136 notes)](https://abel.math.harvard.edu/~knill/teaching/math136/handouts/lecture06.pdf)
- [Shadow-boundaries of convex bodies](https://www.sciencedirect.com/science/article/pii/0012365X94003802)
- [Karger et al. 1997, *Consistent hashing and random trees*](https://dl.acm.org/doi/10.1145/258533.258660)
- [Lamping & Rao 1995, *A focus+context technique based on hyperbolic geometry for visualizing large hierarchies*](https://cgl.ethz.ch/teaching/scivis_common/Literature/Lamping95.pdf)
- [List-labeling problem](https://en.wikipedia.org/wiki/List-labeling_problem)
- [Furnas 1986, *Generalized fisheye views*](https://dl.acm.org/doi/10.1145/22627.22342)
- [Sarkar & Brown 1992, *Graphical fisheye views of graphs*](https://www.cs.montana.edu/courses/spring2005/430/pg/ft_gateway.cfm.pdf)
