# Reading each other: where the back-and-forth closes, and where it does not

*The thirtieth of a series of essays on what can be known from where one stands. Draft, 17 November 2026. It works
through MUT (`plans/mut-plan.md`, `runs/mut/`): seven predictions committed before any run, six not killed in run 1, the
seventh killed by my code and not killed in run 2. It adds three checks I made while writing (`runs/mut/mut3-checks.py`),
worked by hand first and then checked by a seeded simulation. They are checks, not committed tests, and are marked as
such. All the mathematics is classical. The essay is an iteration, not a result: it asks how easily the idea is
handled, and finds that it is not handled easily.*

Two people walk toward each other down a narrow corridor. Each steps aside to let the other pass, both to the same
side. Each sees this, and steps back. They mirror each other again, and for a few seconds they dance, until one of them
stops, or laughs, or says "you go".

Everyone has done this. It is two readers reading each other. Each reads where the other is, and each writes its own
next step from that read. Then each reads the other's write and writes again. Nothing in the rule says when to stop.

The series has said that everything reads and writes. Each thing reads from its own standpoint, writes its own state,
and what it reads is the writes of others (R1065). Tom took the next step: "every reader / writer is reading and
writing each other based on their geometric heat". Then he named the worry: "this quickly creates infinite computation
complexity. but observers don't walk infinity, they are rational. geometric laws collapse infinite complexity into a
inevitable single conclusion." And then the doubt that this essay follows: "i doubt it is so easily handled."

The order: two readings and two corners (§1), the endless exchange (§2), where it closes (§3), what closed it (§4),
strides, not shares (§5), together or in turn (§6), the heat (§7), many things (§8), where there is no law (§9), laws
between systems (§10), what it leaves (§11), what is classical and what is ours (§12), and what is still open (§13).

---

## 1. Two readings, two corners

Keep it as small as it can be. There are two things, A and B, a distance d apart. Each has a breadth, H_A and H_B,
which are amounts and so the writer's. Each holds out a thumb of its own, t_A and t_B, as a slope.

A reads B as a slope against its own thumb,

  s_A = (H_B/d)/t_A,

which is v over h, with h being A's thumb. B reads A the same way, s_B = (H_A/d)/t_B. Scale the whole world by any
factor, every length together, and neither reading moves. These are reads.

Two things follow at once.

**Each reads the other in its own thumb.** The ratio s_A/s_B = (H_B/H_A)·(t_B/t_A). This is the denominator paradox
(*Each Sees the Other Smaller*): there is one line between them, the same line seen from its two ends, and two readings
on it, each in a private unit.

**Each has its own corner.** A reads 1 at d_A = H_B/t_A, and B reads 1 at d_B = H_A/t_B. These are where each would
like the other to be: at its crosshair, its finest grain, its hottest point. Unless d_A = d_B, the two corners are in
different places, and the two things cannot both have what they want.

## 2. The endless exchange

Give each thing a write. It moves to bring the other toward its own corner, by a fixed share of the gap. A moves; that
changes d; B reads the new d and moves; that changes d again; A reads it. The corridor dance.

Followed one step at a time, this never ends. Each read is of the other's last write, and each write makes a new read
necessary. With N things all reading each other it is worse: every write changes every other thing's read. A record
of the whole exchange grows without bound, which is essay 16's and §6 of *Reads and Writes*'s "a record the size of
what it records" (R1050).

Tom's claim is that this is the blueprint's problem, not the things'. Each thing does one read and one write a step.
None of them walks the infinity. And where there is a law, the infinity is not walked at all: one expression covers
every length of the exchange at once (R864, R871).

## 3. Where it closes

MUT put that to the test in the smallest case, in exact fractions. Work in levels: x = ln d, a = ln d_A, b = ln d_B.
Then A's reading is s_A = e^(a − x). A's write moves x by a share α of A's gap, α(a − x), and B's by β(b − x).

When both read at the same moment and then both write, the whole endless exchange is one line:

  x′ = x + α(a − x) + β(b − x).

That is a contraction toward one point, and its limit is in closed form.

- **With equal shares** the walk ends at x* = (a + b)/2, that is d* = √(d_A·d_B), the geometric mean of the two
  corners. It does so from every start, and the distance from it shrinks by exactly |1 − 2α| every round. That was
  checked in fractions for four shares over forty rounds, with not one round off (M1). At a share of ½ it lands in one
  round.
- **At d*, s_A·s_B = 1.** A reads √(d_A/d_B), B reads its reciprocal, and their product is 1 exactly (M2b). Neither
  thing reaches its own corner. Together they reach the pair's, which is the corner of s × (1/s) = 1.
- **Scaling the world** by e^−7, e^(5/3) or e^40 moved every x by the same amount at every round and no reading at any
  round (M3).
- **With unequal shares** the end is a weighted geometric mean, d_A^(α/(α+β))·d_B^(β/(α+β)), again in closed form. The
  product of the readings is 1 there only when the shares are equal (M4): the one who moves less gets nearer its own
  corner.
- **Five, eight and twelve things on a line**, each wanting each neighbour at its own corner, ended on the one solution
  of a single linear system, solved once in fractions, to 10⁻⁵⁰. That held for shares below a bound read off the
  system itself; above it they diverged (M5).

So far Tom's claim stands as he made it. Infinitely many rounds, one expression, one conclusion, and the conclusion has
the series' own shape: the corner.

The next sections are where I doubt it.

## 4. What closed it

The collapse was not the geometry's alone. It was the geometry's readings plus a write rule that I chose: step a fixed
share of the gap in levels.

The geometry gave the readings, the corners and the scale test. It did not give the rule. Change the rule and the
conclusion changes:
- step a share of the gap in amounts instead of levels, and the same pair ends at the arithmetic mean of the corners,
  not the geometric;
- step by turns instead of together, and it does not end at a point at all (§6).

Each rule is a law, and each law collapses its own infinity. But they collapse it to different places.

By R1065 the rule is each thing's own write. A thing's write belongs to the thing. So the "single conclusion" is the
geometry's only once the things' writing is fixed, and what fixes it is not in any read. That is the first place the
idea is harder than it looked.

## 5. Strides, not shares

There is a worse problem with the rule I chose. A share of the gap in levels means multiplying the distance by a
factor: d becomes d·s^α. To do that a walker would need to know d. It does not. It has its reading s and nothing in
amounts (R654: there is no V in a read).

What a walker actually has is a stride, an amount of its own: a write, and its own write. So try the nearest honest
rule. Each steps S·ln s: a stride's worth, scaled by how far its reading is from 1 in levels. Then

  d′ = d + S·ln s_A + S·ln s_B,

which needs no knowledge of d. It rests where ln s_A + ln s_B = 0, at s_A·s_B = 1 again, at the same geometric mean.
So far, good.

But the rest point is now stable only when the stride is short against the distance where they meet. Near it, each
round multiplies the error by 1 − 2S/d*, so the walk settles only while S < d*. I worked that by hand and checked it
(`runs/mut/mut3-checks.py`, d* = 4.4817):
- strides of 0.5, 2, 4 and 4.4 all settle on 4.4817;
- at 4.6, just past d*, the pair never settles and swings between 3.01 and 6.66;
- at 5 it swings between 1.98 and 10.17;
- at 15 the first step carries them through each other to a negative distance, which is nonsense: the rule has walked
  off the edge of its own meaning.

This is the corridor dance exactly: steps too large for the room they are taken in.

So whether there is a single conclusion depends on a stride measured against a distance. That is a comparison of two
amounts, which no read holds and which neither walker can make. A thing that takes small steps settles without knowing
why; one that takes large steps never does, and cannot tell from its reads which it is.

## 6. Together or in turn

Run 1 had a second warning, and I had predicted it, not hoped it away. If the two take turns, A reading and writing,
then B reading A's write and writing, they never meet. They end on a two-cycle. With shares of ½ it runs between
(2a + b)/3, just after A's step, and (a + 2b)/3, just after B's, and stays there for ever. Its midpoint is the
geometric mean, but no write is ever made there (M7). Taking turns is a law too, and it collapses to a pair of places,
not a place.

"At the same moment" is itself the next difficulty. Two things apart cannot read each other at the same moment. Each
reads what arrives, and what arrives left the other a while ago. Simultaneity far off is a convention (R1049). So try
the plainest version: both read the distance as it was one round earlier. I worked out that the walk then settles only
while the share is below ½, against 1 when nothing is late. The check agrees (`mut3-checks.py`):
- at shares of 0.25 and 0.45 it settles on 1.5;
- at exactly 0.5 it cycles for ever;
- at 0.55 it reaches 10⁴² in 2,000 rounds.

Being late by one round halves the room for a write.

POL met this already. Pool balls reading each other late at the speed c came right only when they carried the late
image forward, and the error followed the lateness in ticks. Reading each other is where timing enters, and timing is
not in a read.

## 7. The heat

Tom's sentence had "based on their geometric heat" in it, and run 1 left the heat out. Every reading was exact. A real
read is not a point. It is the Cauchy's heat about the look, spread with some half-width, here written g in levels.

So spread each read. I worked out where the walk goes. Because sums of Cauchy variables are Cauchy and their widths add,
the walk does not settle at all. It wanders for ever about the geometric mean, as a Cauchy of half-width
g·(α + β)/(1 − |1 − α − β|). For any shares adding to 1 or less, that half-width is exactly g: the read's own, no matter
how many rounds. The check (`mut3-checks.py`, g = 0.05, 200,000 pairs over 400 rounds) found:
- a median of 1.500 every time;
- a half-width of 0.0501, 0.0500 and 0.0500 for shares of 0.1, 0.25 and 0.5 each;
- 0.1167 at 0.7 each, against the worked 0.11667.

This is the series' oldest Cauchy fact turning up again: averaging Cauchy readings gains nothing (ADR). The exchange
does not sharpen what the two things know of where they stand. It keeps them exactly as uncertain as one read.

So is this still "one conclusion"? In one sense yes. The whole endless exchange is again one expression: a Cauchy about
√(d_A·d_B) with the read's own width. In another sense no. It is a law of where the pair wanders, not a place where it
stops. The law collapses the infinity into a distribution, and the distribution has no mean. The conclusion is
inevitable as a heat, never as a point.

## 8. Many things

With many things on a line, M5 settled, but in a way I had not predicted. The gaps between neighbours settle: each
thing's neighbours end where the one linear solve puts them. But the line as a whole does not settle. At the gaps'
fixed point every thing still moves by the same amount every round: −1.283α, 1.630α and 0.538α for the three chains.
It stands still only if the corners wanted from each side happen to balance. The law fixed the shape and left the place
free: "steps, never positions" (R842), arriving without being asked. That drift is partly my set-up's: things at the
ends have one neighbour, and the steps were in amounts.

On a plane or in space there is a further reason to doubt the easy collapse, and I have not tested it. There, readings
carried round a loop come back turned. Two turns about two axes do not commute and leave a leftover (HOL, BRL, TWG). Three
things reading each other round a triangle are such a loop. Whether their exchange settles, cycles or turns for ever is
open.

## 9. Where there is no law

Everything above had a law, linear near its rest point, and that is what let one expression cover every round. Not
every exchange has one. Balls of unequal mass colliding on a ring (TWK runs 17 and 19b) leave every free path by the
first unequal contact. After that the state to keep spreads, and no expression in T gives it. Generic chaos (CXB)
spends the start's digits at the rule's own rate. In those cases nothing collapses. The exchange is reached one step at
a time.

Even there no thing walks an infinity. Each does one read and one write a step, locally, and carries its own state.
Only a blueprint trying to hold every thing at once has the growing record (R1050). So the infinity was never the
things' problem. But "inevitable" belongs only to the cases with a law.

## 10. Laws between systems

Tom then put it as systems: "each system reads and writes. systems interact with each other with reads and writes";
"the combinitorial complexity is massive, but there are laws that collapse that complexity." He guessed a law "somethihng
like Oelher's identity", Euler's. MRL (`plans/mrl-plan.md`) looked for laws that hold among the readings exactly, whatever the
rule, with predictions written first and checked in exact fractions.

Three held as predicted:

- **The product is shared.** For any two systems i and j, s_ij·s_ji = H_i·H_j/(t_i·t_j·d_ij²). Neither's breadth or thumb
  appears alone. This is the denominator paradox's product, now between any pair of N.
- **The ratio is owned.** s_ij/s_ji = q_j/q_i, with q = H·t, each system's own write (it moves by k when the world is
  scaled). Round every loop of 3, 4 or 5 systems, in the plane and in space, the ratios multiply to exactly 1. There is no
  arbitrage: the ratios come from one number per system, a potential.
- **Euler's −1 is where a fair exchange rests.** With w(s) = (1 + is)/(1 − is), w(s_A)·w(s_B) = −1 exactly when
  s_A·s_B = 1, and nowhere else. Every exchange rule that is odd and strictly increasing (x/2, tanh, x³/3, arctan) has one
  rest point, there. A fixed stride rests on the whole stretch between the two corners, so it has no single conclusion.

So Tom's guess is right in this sense: the pair's corner of §3 is the reader's form of Euler's identity held between two
systems. It says where a rest can be. Whether the exchange gets there is still §5–§7's question.

The fourth law was the count, and my prediction was wrong. N systems make N(N − 1) readings. I predicted they carry
4N − 5 numbers in the plane and 5N − 8 in space: every breadth, thumb and position, less the scalings, translations and
turns. The exact rank was 4N − 7 and 5N − 11, two and three fewer. I had left out the inversions. An inversion multiplies
each squared distance by one factor per point, and each system's breadth and thumb can absorb its own factor, so no
reading changes. Mutual readings therefore fix the systems' places only up to the conformal (Möbius) maps, whose
invariants are the cross ratios of distances. A second run confirmed the count, and a slip in my factor for the
inversion's null direction (2 where it is 1) was recorded as killed by my arithmetic.

This is a collapse of the kind Tom meant. N(N − 1) readings, quadratic, are carried by a number of quantities that grows
linearly, and the laws that do it are exact. The group that is left over, the Möbius maps, is the same one that keeps the
Cauchy family (R359) and that SRB found behind the boost. All of it is classical (a cocycle, inversive geometry, rigidity
counts); the sorting into a shared product, an owned ratio and the Möbius freedom is ours.

## 11. What it leaves

The doubt was right. Taken together:

- **The readings and the corners are the geometry's.** So is the shape of the answer when there is one: the pair's
  corner, s_A·s_B = 1, at the geometric mean. Every rule above that came to rest at all came to rest there or at a
  weighted version of it.
- **Whether there is an answer is not the geometry's.** It depends on how each thing writes (shares or strides, in
  levels or amounts), on timing (together, in turn, late), and on the size of a step against a distance. None of those
  is in a read, and by R1065 each belongs to the thing that writes.
- **When there is an answer, the heat keeps it a heat.** With Cauchy reads the exchange collapses to a law of where the
  pair wanders, as wide as one read, never narrower.
- **When there is no law, there is no collapse,** only steps, each finite.

So I would restate Tom's sentence. Geometric laws collapse the infinite exchange into a single conclusion where the
writes are small, timely and in proportion. The conclusion is then the corner, held as a heat. Otherwise the exchange
cycles, drifts or wanders, and no read can tell a thing which case it is in.

## 12. What is classical and what is ours

All of the mathematics is classical:
- a linear fixed-point iteration, its rate and its stability bound;
- a delayed iteration's characteristic roots;
- the stability of a nonlinear map at its rest point;
- the Cauchy's widths adding under linear combination;
- the geometric mean of two corners, which is the denominator paradox's and parallax's;
- a cocycle with a potential, Möbius composition, and the conformal group's cross ratios.

None of it is a new result. But, as Tom put it, "Classical gives the tools, not the full explanation of what they mean,
or how they combine." Each tool above is proved and used in its own field. What is ours is what they mean here and how
they combine: the sorting.
- the readings and the corner as the geometry's;
- the rule, the stride and the timing as each thing's own writes;
- the heat as what keeps the conclusion a distribution;
- the infinity as the blueprint's;
- the shared product, the owned ratio and the Möbius freedom as one account of many systems reading each other, with
  Euler's −1 as the place a fair exchange rests.

## 13. What is still open

- **Loops.** Three things reading each other round a triangle on a plane. MRL's loops close, but they are loops of
  owned amounts, scalar slopes. With directions carried round the loop, does the exchange settle, cycle, or come back
  turned?
- **Which rule.** Is there a reason, from the geometry, for one write rule over another? Or is the rule always the
  things' own?
- **Steps from reads alone.** Can a thing keep its steps short against a distance it cannot read, for example by
  stepping in proportion to how fast its reading changes, which is τ, the time to contact (essay 6 §2)? Lee's τ̇ ≥ −½
  says something like that already for one thing approaching another.
- **The heat in the many.** With N things and Cauchy reads, do the gaps keep the read's own width, as the pair does?

Each of these should be a plan with its predictions first, before anything here is carried into *Reads and Writes*.

---

## Sources

- Tom, 17 November 2026: "each observer reads / writes. than reads / writes. etc. so every reader / writer is reading
  and writing each other based on their geometric heat."; "this quickly creates infinite computation complexity. but
  observers don't walk infinity, they are rational. geometric laws collapse infinite complexity into a inevitable single
  conclusion."; "We should explore this somehow with H V and h v."; "each system reads and writes. systems interact with
  each other with reads and writes."; "the combinitorial complexity is massive, but there are laws that collapse that
  complexity."; "Classical gives the tools, not the full explanation of what they mean, or how they combine."; "All of this is classical, it just iteration over the
  same core ideas to organize them."; "lets iterate this in an essay first. i doubt it is so easily handled."
- `plans/mut-plan.md`; `runs/mut/mut.py`, `mut2.py` (outputs `mut-run1.txt`, `mut-run2.txt`); `runs/mut/mut3-checks.py`
  (output `mut3-checks.txt`), checks made while writing, not committed predictions. `plans/mrl-plan.md`;
  `runs/mrl/mrl.py`, `mrl2.py` (outputs `mrl-run1.txt`, `mrl-run2.txt`).
- *Each Sees the Other Smaller* (`papers/denominator-paradox.md`); *Reads and Writes* §1 "Whose writes", §6 "A record the
  size of what it records". Essay 6 §2 (motion from reads), essay 16 (K, not N), essay 22 §10–§11 (TWK runs 15–19),
  essay 21 §9 (chaos).
- POL (`plans/pol-plan.md`, runs 3–4: reading late), ADR (`plans/adr-plan.md`: averaging gains nothing), HOL, BRL, TWG
  (loops that come back turned), TWK runs 17 and 19b, CXB.
- SPN rulings cited: R654, R842, R864, R871, R1049, R1050, R1065, R1068, R1070, R1071.
