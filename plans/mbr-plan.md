# MBR: maps between reads

10 Nov 2026. After BCL (`plans/bcl-plan.md`) and a ruling pasted by Tom: "keep the time-to-contact number out of D3 for
now, and proceed with the counterexample pass on maps between reads"; "run the map-between-reads counterexample pass
before changing D1–D7 again. The objective is to discover whether the framework needs a fourth kind". Nothing in
*Reads and Writes* D1–D7 is changed by this plan.

## The question

A turn, a boost, the rapidity and the Doppler factor each relate two reads. Is "a map between two reads" a kind of its
own, beside read, place and write, and does it keep the Doppler factor apart as a relation between payloads?

## Known beforehand

SRB (`plans/srb-plan.md`): a boost acts on the sky as a Möbius map; the Doppler factor is that map's stretch; the
frequency identification is a further premise (P); the rapidity is the Poincaré distance between the skies'
standpoints. TWG (`plans/twg-plan.md`): two boosts in different directions compose to a boost and a turn. *Reads and
Writes* §1: turns compose by tangent addition; §6: a step places, a turn does not. None of this is new here; the pass
asks only how the definitions class it. Draw's labs were not consulted (no reader, shape or recovery is built).

## Set-up (exact, rational arithmetic)

The sky on the stereographic chart, the writer's coordinate z on a direction (z = 0 the direction of the boost). A
boost of rapidity η is z ↦ k·z, k = e^η, taken rational. A turn is z ↦ (a·z + b)/(−b̄·z + ā) with |a|² + |b|² = 1,
taken with rational a, b. The stretch of a map g at a direction is D_g(z) = |g′(z)|·(1 + |z|²)/(1 + |g(z)|²). Under
premise (P), the frequency received along a direction changes by that factor, f′ = D·f. A step is a change of the
standpoint's position in the plane, the world's points given as positions. Classical special relativity is assumed for
the boost's action, not derived.

## The five counterexamples asked for, and predictions (Claude's, before the run)

- M1, same direction, different motion. On the boost's axis (z = 0) the direction is unmoved by every boost, and the
  stretch there is k, not 1. So the relation between the two reads is not the displacement of that direction.
- M2, same boost, different payload. The map z ↦ k·z and its stretch do not depend on the emitted frequency. With a
  source factor σ of its own (its own motion), the observed ratio to the rest frequency is σ·D; changing σ changes the
  ratio and not the map. (Partly true by construction; stated so.)
- M3, same payload ratio, different maps. D = 2 at z = 0 under k = 2, and at |z|² = 1/15 under k = 3, and under the
  identity map with σ = 2. One ratio, three maps: the ratio does not fix the map.
- M4, turn against boost, and both against a step. A turn's stretch is 1 at every direction; a boost's runs from k to
  1/k. Both are maps on directions that hold whatever the world is. A step is not: two points on one direction at
  different distances are on two directions after it, so no map on directions describes it.
- M5, composition. Maps compose to maps (the kind is kept). Stretches compose as D_{g∘h}(z) = D_g(h(z))·D_h(z), which
  needs the map h to say where z went; D_g(z)·D_h(z) is wrong off the axis. A turn and a boost in the two orders are
  different maps with different stretches at one direction.
- M6, the rapidity. For boosts along one axis k multiplies, η adds, and β = (k² − 1)/(k² + 1) composes by
  (β₁ + β₂)/(1 + β₁β₂): the same three coordinates a turn has (w = e^(2iθ) multiplies, θ adds, s composes by tangent
  addition). So η is the writer's additive coordinate on a boost, as an angle is on a turn.

Killed: any identity above failing in exact arithmetic. The framing is killed if a step turns out to be a map on
directions, or if a turn's stretch is not 1, since then "a map on directions, the same in every world" would not
separate turns and boosts from steps or from each other.

## Runs

### Run 1 (10 Nov 2026)

`python3 runs/mbr/mbr.py`, output in `runs/mbr/mbr-run1.txt`. Every identity holds in exact rational arithmetic;
nothing killed.

Weak checks, said plainly: M2's first three lines are true by construction (the stretch is a function of the map and
the direction, so it cannot depend on the emitted frequency once premise (P) is granted), and one line of M4 ("a map
sends one direction to one direction") asserts a definition and tests nothing. The checks that could have failed are
M1, M3, M4's stretches and its step, M5 and M6.

What the five counterexamples show:

1. Same direction, different motion (M1). On the axis no direction moves and the stretch is k. So the relation between
   two reads is not carried by any one direction's displacement: it is the map as a whole.
2. Same boost, different payload (M2). The map and its stretch are fixed by the two standpoints. The observed ratio to
   a rest frequency is the stretch times the source's own factor; only the second is the world's.
3. Same ratio, different maps (M3). A ratio of 2 comes from k = 2 on the axis, from k = 3 at |z|² = 1/15, or from no
   boost and a source factor of 2. The ratio does not fix the map; the map and a direction fix the stretch.
4. Turn against boost against step (M4). A turn and a boost are both maps on directions, the same whatever the world
   holds. A turn's stretch is 1 everywhere; a boost's runs from k to 1/k. A step is no map on directions: one
   direction before it is two after it, according to distance. That is exactly why a step places and the others do
   not.
5. Composition (M5). Maps compose to maps. Stretches compose only through the map, D_{g∘h}(z) = D_g(h z)·D_h(z); the
   product taken at one direction is wrong off the axis. So the stretch is carried by the map, not the reverse.
6. The rapidity (M6). k multiplies, η adds, β composes by (β₁ + β₂)/(1 + β₁β₂), as for a turn w multiplies, θ adds and
   s composes by tangent addition. η is to a boost what an angle is to a turn: the writer's additive coordinate on the
   map, a representation of it and not a further thing.

Answers to the four candidates:

- A turn. A map of a read onto itself: every direction relabelled, the heat kept (stretch 1), the paint carried along
  unchanged. The separation of two directions within one read is the turn that carries one to the other, so it is of
  the read, as D2 now says.
- A boost. A map between two different reads at one position: the heat is moved (stretch not 1) and, under (P), the
  colour of what arrives with it.
- The rapidity. Neither the map nor a distance in space: the writer's coordinate on the boost in which boosts along
  one axis add. By D7's sentence on representations it has the map's kind, whatever that is called.
- The Doppler factor. Two variables with one value. The stretch of the map at a direction is the map's own, fixed by
  the two standpoints and the direction, unmoved by what arrives. The ratio of two received frequencies is a relation
  between payloads. Premise (P) makes them equal; it is physics and is not read. An observed ratio to a rest frequency
  is the stretch times the source's factor, and is the payload's.

Reading. The test the ruling set is met: one criterion, stated without the answer in view, separates the cases. A
relation between two reads is a map between reads when it is a function on directions that is the same in every world.
Turns and boosts are; a step is not, and what a step gives instead is places. The criterion keeps the Doppler ratio
apart from the stretch, and keeps the rapidity as a coordinate.

Whether that makes a fourth kind is for Tom. For: it is unmoved by scaling, unmoved by what arrives, needs two reads,
holds no gap across, and composes as a group, which none of read, place or write does. Against: D7 already has
"orders", a joining with no gap in it (§12 O4), and a map between reads may be that kind under a better name; and for
turns the map is already inside the read. What the pass does not settle: whether a boost's action on directions must
be a map at all is premise (C) of SRB, assumed here from special relativity and not derived.

Not done: no change to D1–D7; the time to contact stays out of D3 (its number d₁/B is a ratio of two distances, and
its reading as a time is not classed).
