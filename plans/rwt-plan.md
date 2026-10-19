# RWT: reading is free, writing needs movement and interaction (counting the steps)

*16 October 2026 (Tom's local date). Tom, about 09:33: "Writing requires much more than reading, writing must
discovering the breadths. Reading ratios is free provided by geometry. Writing requires movement and interaction."
(SPN R297); about 09:36, "Yes test it", to Claude's offer to count the steps. Geometry, exact; OFS §9's "Reading and
writing" states it.*

## The claim

- A reader that only reads needs no movement: every reading is a ratio, unchanged by any common rescaling.
- To write one breadth in its own H takes exactly one displacement of known length (in H): no fewer, and a second adds
  nothing to the scale.
- To write in a breadth another reader shares takes one interaction more: one written number exchanged.
- To write in a public unit (metres) takes one more: one notch agreed.

**The bridge.** None inside the readings. The known displacement is the reader's own H walked (an amount in its own
breadth); the exchanged number and the notch are amounts carried in. This is OFS Proposition 8 counted.

## Predictions (written 16 Oct about 09:40, before any run)

Exact (mpmath, 40 digits). A scene of K = 4 targets, each a breadth V*ₖ (half-breadth aₖ) at a place (xₖ, yₖ) in the
plane, amounts in metres, seeded (seed 13). A reader reads, from a standpoint, each target's bearing and its half-angle
reading sₖ = aₖ/dₖ (dₖ the distance). The unknowns are the logarithms of every amount; the count of what is not fixed
is the nullity of the Jacobian of the log-readings (and any known values) with respect to them, singular values below
10⁻²⁵ counted as zero.

- **T1. Zero moves: reading is free, writing nothing.** From one standpoint, every reading is unchanged when all
  amounts are multiplied by λ ∈ {10⁻³, 7, 10⁶} (to 10⁻³⁰). The nullity is K = 4: each target's size and distance trade
  freely (its reading fixes only their ratio).
- **T2. One known move writes in the reader's own H.** The reader moves by a displacement of length H, known to it in
  H (the length is 1 in its own breadth), either toward a target or sideways (a baseline):
  - from the two standpoints' readings, every dₖ/H and V*ₖ/H is recovered to 10⁻³⁰, for 10 scenes, by
    d = H·s₂/(s₂ − s₁) along the line of sight (OFS §10 step 6) and by triangulation across a baseline;
  - the nullity, in the reader's own breadth (log H fixed), is 0.
- **T3. A move of unknown length writes nothing.** With the displacement's length not known, the nullity is 1, a
  common scale: the scenes multiplied by λ give identical readings at both standpoints (to 10⁻³⁰), so V*/H takes every
  value.
- **T4. A second move adds nothing to the scale.** Two known moves (toward, then sideways) give the same V*ₖ/H as one
  (to 10⁻³⁰); the nullity stays 0.
- **T5. Interaction: one exchanged number.** Two readers A, B with strides H_A = 0.7 m and H_B = 1.9 m each make one
  known move and write every V*ₖ in their own breadth: A's V*ₖ/H_A and B's V*ₖ/H_B differ by exactly H_B/H_A for every
  k. Neither alone fixes H_B/H_A (the joint nullity, in A's breadth, is 1). When B sends A one number, its written
  V*₁/H_B, A reads H_B/H_A = (V*₁/H_A)/(V*₁/H_B), and then all K of B's written breadths agree with A's to 10⁻³⁰ (joint
  nullity 0).
- **T6. A public unit: one notch.** Everything in T5 is still in A's breadth; in metres the joint nullity is 1 until one
  amount in metres is supplied (H_A = 0.7 m, a notch agreed), after which every breadth is written in metres to 10⁻³⁰
  (nullity 0).

The counts: reading 0; writing in one's own breadth 1 move; writing for another reader 1 exchange more; writing in a
public unit 1 notch more.

*Killed if* any check misses its tolerance or any nullity differs from its prediction. The identities are classical
(Proposition 8); a kill would be my computation or my count.

## Runs

### Run 1 (16 Oct about 09:45, `runs/rwt/rwt.py`, output in `runs/rwt/run1.txt`; 2 s)

**T1–T6 not killed.** (An unused function was removed from the script after the run; the rerun printed the same.)
- **T1.** From one standpoint the readings are unchanged by λ (to 2·10⁻⁴⁰). The nullity is 4: each target's size and
  distance trade freely.
- **T2.** One move of known length H, toward a target or sideways, recovers every V*/H and d/H (to 10⁻³⁵) in 10 scenes.
  The nullity is 0 in all six systems checked.
- **T3.** With the move's length unknown, the nullity is 1, and scenes multiplied by λ read the same.
- **T4.** A second known move gives the same V*/H (to 2·10⁻³⁵); the nullity stays 0.
- **T5.** Two readers' written breadths differ by H_B/H_A = 1.9/0.7 at every target. One number sent by B makes all four
  agree (to 2·10⁻³⁸). A's nullity is 1 without that number and 0 with it.
- **T6.** In metres the nullity is 1 until one notch (H_A = 0.7 m) is agreed, and then 0.

## What it shows

Counted exactly: reading takes no move, and from one standpoint each target's size and distance stay free together.
Writing one breadth in the reader's own H takes exactly one displacement of known length, and a second adds nothing to
the scale. Writing for another reader takes one number exchanged. Writing in a public unit takes one agreed notch more.
Each step is one amount carried in from outside the readings, as Proposition 8(b) says; this plan counts them.
