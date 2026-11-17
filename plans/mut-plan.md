# MUT: two readers reading and writing each other, in H, V, h, v

17 November 2026. SPN R1068. Tom: "each observer reads / writes. than reads / writes. etc. so every reader / writer is
reading and writing each other based on their geometric heat."; "this quickly creates infinite computation complexity.
but observers don't walk infinity, they are rational. geometric laws collapse infinite complexity into a inevitable
single conclusion."; "We should explore this somehow with H V and h v. that lets us build out from a solid foundation.";
"yes. proceed".

## The question

When two things each read the other and write their own state from that read, the back-and-forth has no last step.
Does a geometric law collapse the endless chain into one closed form, which each read and write only fills in? Where
does it fail to?

## The set-up (exact)

- Two things, A and B, a distance d apart. Their breadths H_A and H_B are amounts, the writer's. Each holds one thumb at
  arm's length, t_A and t_B, as a slope.
- A's reading of B: s_A = (H_B/d)/t_A, the slope v/h with h A's own thumb. B's reading of A: s_B = (H_A/d)/t_B. Scaling
  the world by k (every length) moves neither.
- Each has its own corner, where its reading is 1: d_A = H_B/t_A for A and d_B = H_A/t_B for B. A pair has
  s_A/s_B = (H_B/H_A)(t_B/t_A): each reads the other in its own thumb (the denominator paradox).
- Levels: x = ln d, a = ln d_A, b = ln d_B. Then s_A = e^(a − x) and s_B = e^(b − x).
- **A write**: each thing moves to bring the other toward its own corner by a fixed share of the gap in levels, A by α,
  B by β. **Simultaneous** (both read the same moment, then both write): x′ = x + α(a − x) + β(b − x).
  **Alternating** (A reads and writes, then B reads A's write and writes): x′ = x + α(a − x), then x″ = x′ + β(b − x′).
- N things on a line (M5): positions p_i (amounts), gaps g_i = p_(i+1) − p_i. Thing i wants its right gap at its corner
  for its right neighbour, R_i = H_(i+1)/t_i, and its left gap at L_i = H_(i−1)/t_i. Each moves simultaneously by
  ½α(g_i − R_i) − ½α(g_(i−1) − L_i) (an end has one term). This is in amounts, not levels, so that the law is one linear
  system; a stated choice.
- Arithmetic: Fractions wherever the levels, shares and targets are rational (they are chosen so), mpmath at 60 digits
  otherwise.

## Predictions (committed before any run)

- **M1.** Simultaneous, α = β, 0 < 2α < 2: from every start the walk tends to x* = (a + b)/2, d* = √(d_A·d_B), and
  |x_n − x*| = |1 − 2α|^n·|x_0 − x*| exactly, every round.
- **M2.** At x*, s_A = √(d_A/d_B), s_B = √(d_B/d_A), s_A·s_B = 1 exactly: the pair's corner, reached by neither alone.
- **M3.** Scaling the world by k (a, b, x_0 each plus ln k) moves x_n by ln k at every round and no reading s_A, s_B.
- **M4.** Simultaneous, unequal shares (0 < α + β < 2): x* = (αa + βb)/(α + β), a weighted geometric mean
  d_A^(α/(α+β))·d_B^(β/(α+β)), with factor |1 − α − β| a round; s_A·s_B = 1 only when α = β (or a = b).
- **M5.** N things (N = 5, 8, 12, rational H_i, t_i): the iterated walk, for α below 2/λ_max of its own update matrix,
  converges to the one solution of the linear system the fixed point satisfies, solved once in Fractions, to 10⁻⁵⁰; above
  2/λ_max it diverges. Scaling the world by k scales every gap of the solution by k.
- **M6.** Simultaneous with α + β = 2: a two-cycle forever (x′ − x* = −(x − x*)), no limit; α + β > 2: diverges as
  |1 − α − β|^n. No collapse there.
- **M7.** Alternating, α = β = ½: no single meeting; the walk ends on a two-cycle, after A's step at (2a + b)/3, after B's
  at (a + 2b)/3, its midpoint (a + b)/2 the geometric mean; general shares: after B's step
  x* = [(1 − β)αa + βb]/[1 − (1 − α)(1 − β)], after A's step its image under A's write. Factor (1 − α)(1 − β) a round.

## Kill conditions

Any equality stated exactly failing in Fractions; M5's iterate more than 10⁻⁵⁰ from the solve after convergence, or
converging above 2/λ_max; M6 converging; M7's cycle points off.

## Runs

**Run 1** (`runs/mut/mut.py`, output `runs/mut/mut-run1.txt`, 17 Nov). M1, M3–M7 not killed; M2 killed by my code
(`mp.e ** mp.mpf(n) ** 0 * …` raised e to the first power, so s_A came out e^(−1/2) for e^(−3/2)); its exact clause held
(a − x* = −3/2, b − x* = 3/2, sum 0).
- M1: |x_n − x*| = |1 − 2α|^n·|x_0 − x*| exactly at every round, α = 1/8, 1/4, 1/2, 3/4, four starts; α = ½ lands in one round.
- M3: the world scaled by e^−7, e^(5/3), e^40 moved x_n by ln k each round and no reading, exactly.
- M4: x* = (αa + βb)/(α + β) with factor |1 − α − β| exactly; ln(s_A·s_B) = 0 only at α = β (−9/7, −12/5, 3/2 otherwise).
- M5: N = 5, 8, 12: 2/λ_max 1.1056, 1.0396, 1.0173; at 0.9 of it the walk lands on the one Fraction solve to 5·10⁻⁶⁰,
  at 1.1 it diverges (10³⁰); the solution scales by k exactly; the eigenvalues real and negative.
- M6: α + β = 2 a two-cycle forever, α = β = 5/4 diverging as (3/2)^n, exactly.
- M7: alternating, α = β = ½: after A 1 = (2a + b)/3, after B 2 = (a + 2b)/3, midpoint 3/2 = (a + b)/2; the closed forms
  for 1/5, 1/2 and 3/4, 1/10 and the factor (1 − α)(1 − β) exact.

**Run 2** (`runs/mut/mut2.py`, output `mut-run2.txt`): the M2 line fixed, nothing else changed. M2b not killed:
s_A = e^(−3/2) = 0.223130160148 = √(d_A/d_B), s_A·s_B = 1 exactly at x*.

**Post hoc, not predicted.** In M5 the gaps settle but the line as a whole does not: at the gaps' fixed point every thing
moves by the same amount a round, −1.283α, 1.630α, 0.538α for the three chains, ½·Σ(L_(i+1) − R_i)/N, zero only when the
corners wanted from each side balance. The law fixes the shape (the gaps, in thumbs of each) and leaves the place free:
"steps, never positions" (R842) turning up unasked. The left/right drift is my set-up's (amounts, an end with one term).

**What is classical.** Everything here is a linear fixed-point iteration (a contraction, Jacobi's), its limit and rate in
closed form; the geometric mean of two corners is PXC's and the denominator paradox's. What is ours is the reading: two
readings' infinite back-and-forth is one expression in the two corners, the pair's corner s_A·s_B = 1 reached by neither
alone, only by equal shares; and where the share overshoots there is no collapse.
