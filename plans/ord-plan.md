# ORD: is a map between reads an order?

10 Nov 2026. SPN R825. A ruling pasted by Tom: "treat "a map between reads" as the clearer name for the existing kind
of orders, not as a fourth kind—provisionally"; "Before changing the definitions, test orders against three cases";
"The third case is decisive." D1–D7 are not changed by this pass.

## The question

*Reads and Writes* D7 says joining reads gives "places and orders", and §12 O4 says an order of reads is "a joining with
no gap in it, not a place". MBR (R824) found that a turn and a boost are functions on directions, the same in every
world. Does "order", as the paper already uses it, name that structure? Three cases: a turn, a boost, a general map on
directions.

What "order" means here, taken from the paper and fixed before the run: a relation of before and after among reads, or
of one side and the other among the directions of one read. As a relation it has no cycle: if a is before b and b
before c, then a is before c and c is not before a. Nothing else is assumed of it.

## Known beforehand

- MBR: turns and boosts are Möbius maps of the directions; the stretch is the map's; stretches compose only through
  the map.
- SRB: a change of standpoint acting on directions alone, with finitely many numbers, the turns among them and a
  motion, is a Möbius map (given Lie's classification). So "arises from a change of standpoint" and "Möbius" coincide
  under those premises.
- OFS Theorem 6(c): every increasing map of the reading keeps the order of readings. So keeping order cannot single
  out anything narrower than the increasing maps.
- Essay 13, TWG: turns of space do not commute (two quarter turns in the two orders land 120° apart).
- The cross ratio of four directions is kept by every Möbius map (classical).

## Set-up

Exact rational arithmetic (`runs/ord/ord.py`, reusing MBR's Gaussian rationals). Directions in the plane are slopes
s; a turn acts by tangent addition, a boost along the axis by s ↦ ks on the level's chart, the exchange by s ↦ 1/s.
In space, turns are 3 × 3 rational rotation matrices.

## Predictions (committed before the run)

- **N1. A turn is not an order.** A quarter turn applied four times is the identity: the relation "carried to by this
  turn" has a cycle, which an order cannot. Kill: no cycle found for a rational turn of finite period.
- **N2. A boost is not an order.** A boost k followed by 1/k is the identity: a cycle of two. Kill: the composite is
  not the identity.
- **N3. A map's coordinate may be ordered without the map being an order.** Boosts along one axis are totally ordered
  by k (and compose in either order alike); turns of the plane are ordered only cyclically; turns of space not at all
  in a way composition respects (N5). Kill: boosts on one axis fail to commute.
- **N4. Keeping order does not single out the maps between reads.** s ↦ s³ keeps the order of every set of slopes and
  is not a Möbius map: it moves the cross ratio of four slopes, which every turn and boost keeps exactly. The exchange
  s ↦ 1/s keeps the cross ratio and reverses the order. So "keeps order" and "is a map between reads" are
  independent: each holds without the other. Kill: s³ keeps the cross ratio of the test slopes, or a turn or boost
  moves it, or the exchange keeps the order.
- **N5. An order and a map are two variables.** The same two maps joined in the two orders give two composites in
  space (two quarter turns about two thumbs: the composites differ, and the turn between them is 120°), and one
  composite in the plane. So the order of reads is an argument a composition takes, not the composition. Kill: the
  two composites in space are equal, or their relative turn is not 120°.
- **N6. A general map does not count merely by being a function on directions.** Of the maps tried (a turn, a boost,
  their composite, the exchange, s ↦ s³, s ↦ s + 1 on the slope chart, a lens-like s ↦ s/(1 + s)·2), those that keep
  every cross ratio are exactly the Möbius ones; among those, the ones that can be a change of standpoint by SRB's
  premises are the turns, boosts and their composites. s ↦ s³ is a change of chart of one read (a representation,
  D7); it is no relation between two reads. Kill: a non-Möbius map on the list keeps the cross ratios tried.
  Note stated beforehand: s ↦ s + 1 and 2s/(1 + s) are Möbius on the slope chart, so they are expected to keep the
  cross ratio; whether they are changes of standpoint is SRB's premises' to say, not this run's.

A convention to state with the result, raised by the ruling: "a boost changes the heat" must say which measure is
held. Each read has its own heat, given with its directions, the same at every standpoint. What a map's stretch
measures is the first read's heat carried by the map against the second read's own. A turn carries heat onto heat
(stretch 1); a boost does not.

## Runs

**Run 1** (10 Nov, `python3 runs/ord/ord.py`, output `runs/ord/ord-run1.txt`; exact rationals). N1–N6 not killed.

- N1. A turn by slope 1 is the identity on slopes after four applications and not before: a cycle. (Reported, not
  predicted: a turn by slope 3/4 does not return in 199 steps. A turn need not cycle; that some do is enough to show a
  turn is not an order.)
- N2. A boost k followed by 1/k is the identity.
- N3. Boosts on one axis commute and are ordered by k; turns of the plane commute.
- N4. s ↦ s³ keeps the order of the six test slopes and moves a cross ratio; a boost and a turn keep every cross ratio
  of the six; the exchange keeps every cross ratio and reverses the order.
- N5. Quarter turns about two thumbs in the two orders give two composites, 120° apart; in the plane, one.
- N6. Of nine maps, the six Möbius ones keep all fifteen cross ratios of the six slopes and the three others (s³, s²,
  s/(1 + s²)) do not.

One line of the output says FAIL. It is a side check I added while writing the script, not in the plan: that a turn
by slope 1/10 would break the slope chart's order of the test slopes by carrying one past the horizon. It does not:
that needs a slope above 10 and the largest tried is 7. My choice of numbers; the output is left as it came. (A turn
by slope 1 does carry 3/2 past the horizon, to −5.) Nothing rests on it.

Limits. N1 and N2 are close to definitional once "order" is fixed as a relation with no cycle and a map has an
inverse; they are here because the ruling asked for them case by case. N6 tries nine maps on six slopes; that the
cross-ratio-keeping maps are exactly the Möbius ones is classical, not shown by nine cases. Which Möbius maps are
changes of standpoint is SRB's premises', assumed.

Answers to the three cases:

1. A turn is not an order. It is a map of one read onto itself, with an inverse and cycles. The directions of one
   read do have an order (cyclic round a turn), and a turn keeps it; keeping an order is not being one.
2. A boost is not an order. It is a map between two reads at one position, with an inverse. Along one axis its
   coordinate (k, or the rapidity) is ordered, which is a fact about the coordinate.
3. A general map does not qualify by being a function on directions. Three things a function on directions can be,
   and the tests that part them:
   - a change of chart of one read (s ↦ s³): one read, relabelled; it keeps order and not the cross ratio; a
     representation, which has its variable's kind (D7). No relation between two reads at all.
   - a change of what arrives (a lens or the air between, R820): which source paints a direction changes; D6 already
     puts it with the payload.
   - a map between reads: induced by a change of standpoint that is not a step (a turn of the look, a change of
     motion). By SRB's premises these are Möbius maps: they keep every cross ratio, have inverses and compose.
   So the further condition is "induced by a change of standpoint", and its checkable trace is the cross ratio.

Reading. "Order", as the paper has used it, does not name this structure. An order is a relation with no cycle; a map
is a function with an inverse. They are also separate variables: joining the same two maps in the two orders gives
two results in space, so the order is something a composition takes, not the composition (N5). And keeping order is
neither needed nor enough for being a map between reads (N4).

What they share is the phrase O4 already uses: "a joining with no gap in it". That phrase names a family, and the
pass finds two members: an order (which read is before which) and a map (how one read's directions go to
another's). So the ruling's lean holds in one form and not the other. No fourth kind beside read, place and write is
needed. But "maps between reads" is not a clearer name for orders; it is a second member of the family orders belong
to. The least change that would say so is in D7: "Joining reads gives places, orders and maps", with O4 widened from
"orders" to "joinings with no gap". Not made; D1–D7 stand as they are until Tom rules.

The convention on heat, as the ruling asked. Each read has its own heat, given with its directions and the same at
every standpoint; no map changes it. A map's stretch at a direction is the first read's heat carried by the map,
against the second read's own heat there. A turn carries heat onto heat (stretch 1 everywhere). A boost does not
(stretch k to 1/k). So MBR's "the heat is moved" should read: the boost does not carry one read's heat onto the
other's. Whether the paint's colour follows the stretch is premise (P), physics. In coordinates: the stretch is
stated on the sphere of directions with its uniform measure; on the slope chart the same fact appears with the
chart's own factor, and the number at a direction is the same.
