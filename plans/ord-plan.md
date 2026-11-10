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
