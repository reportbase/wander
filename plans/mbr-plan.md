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
