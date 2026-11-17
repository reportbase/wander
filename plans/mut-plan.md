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
