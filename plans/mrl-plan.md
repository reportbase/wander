# MRL: laws of systems reading each other

17 November 2026. SPN R1070. Tom: "there is probably a new law here somethihng like Oelher's identity. how about this,
each system reads and writes. systems interact with each other with reads and writes."; "the combinitorial complexity
is massive, but there are laws that collapse that complexity."; "ys" (to writing the plan and running it).

## The question

When N systems read each other, there are N(N − 1) readings. Which laws hold among them exactly, and how many numbers do
they actually carry?

## The set-up (exact)

- System i has a breadth H_i (an amount, its own write) and a thumb t_i (a slope). For two systems at distance d_ij,
  i reads j as s_ij = (H_j/d_ij)/t_i. Scaling the world by k (every H and every d) moves no reading.
- i's corner for reading j is d_ij* = H_j/t_i, the distance at which s_ij = 1.
- The landing point is w(s) = (1 + is)/(1 − is), and composition is s ⊕ a = (s + a)/(1 − sa).
- Positions are rational points, with squared distances D_ij = d_ij² rational, so that products and ratios of readings
  are rational and can be checked in Fractions.
- An exchange rule: both read at once, then each moves the shared distance by f(ln s) in levels, with f the same on both
  sides. Rest is where f(ln s_A) + f(ln s_B) = 0.

## Predictions (committed before any run)

- **L1. The product is shared.** For every pair, s_ij·s_ji = d_ij*·d_ji*/d_ij² = H_i·H_j/(t_i·t_j·D_ij), exactly, for 200
  random rational systems and positions. Neither system's own breadth and thumb appear separately: a pair of private
  amounts enters only as the product H_i·H_j/(t_i·t_j).
- **L2. Euler's −1 between two systems.** For rational readings, w(s_A)·w(s_B) = w(s_A ⊕ s_B) exactly in Gaussian
  rationals, and it equals −1 exactly when s_A·s_B = 1 (checked on 200 pairs with s_B = 1/s_A, and on 200 with
  s_A·s_B ≠ 1, none giving −1).
- **L2b. Where a fair rule rests.** For f odd and strictly increasing (f(x) = x/2, tanh x, x³/3, arctan x), the exchange
  has exactly one rest point, at s_A·s_B = 1, so w(s_A)·w(s_B) = −1 there (to 10⁻⁵⁰). For f = sign (a fixed stride
  toward the corner) every distance between the two corners is a rest point: no single conclusion.
- **L3. The ratio is owned, and closes on loops.** s_ij/s_ji = (H_j·t_j)/(H_i·t_i) exactly, whatever the distance; around
  every closed loop of 3, 4 and 5 systems the product of these ratios is exactly 1, in the plane and in space.
- **L4. The count.** In log coordinates (ln H_i, ln t_i and the positions), the Jacobian of the N(N − 1) log readings has
  rank exactly 4N − 5 in the plane and 5N − 8 in space, at random rational points, for N = 5, 10 and 20, computed in
  exact rational arithmetic. Its null space is: the world scaled; every H and every t scaled together; the translations;
  the rotations.
- **L5. Scaling.** Scaling the world by k leaves every reading, every product in L1 and every loop in L3 unchanged
  exactly. Each system's q_i = H_i·t_i moves by k.

## Kill conditions

- Any exact equality failing in Fractions.
- A rank other than 4N − 5 or 5N − 8.
- In L2b, a strictly increasing odd f resting anywhere but s_A·s_B = 1, or f = sign having a single rest point.

## What this does not test

- **Whether an exchange reaches its rest.** That is essay 30: strides, lateness and the heat.
- **Whether loops of directions come back turned in space.** The readings here are scalar slopes, so L3's closure is
  about owned amounts, not turns.
- **Novelty.** The arithmetic is classical: the denominator paradox's product, Möbius composition, a cocycle, and the
  rigidity count. The sorting into shared product and owned ratio is the series' own.

## Runs

**Run 1** (`runs/mrl/mrl.py`, output `runs/mrl/mrl-run1.txt`, 17 Nov).
- **Not killed: L1, L2, L2b, L3, L5.**
  - The product is shared exactly, on 200 pairs.
  - w(s)·w(1/s) = −1 exactly, and w(s)·w(a) = w(s ⊕ a) with no −1 off the corner.
  - Each of the four odd increasing rules has one rest point, at the geometric mean, where w_A·w_B = −1.
  - f = sign rests at all 299 points tested between the corners.
  - Every loop of 3, 4 and 5 systems closes to 1 exactly, in the plane and in space.
  - Scaling the world moves no reading, and moves q_i = H_i·t_i by k.
- **L4 killed, by my count.** The rank is 13, 33, 73 in the plane and 14, 39, 89 in space, against 15, 35, 75 and 17, 42,
  92 predicted. That is 4N − 7 and 5N − 11: two and three fewer.
- **Post hoc reading of the kill.** I left out the special conformal maps. An inversion multiplies each squared distance
  by a factor c_i·c_j, one factor per point. Each system's ln H and ln t can absorb its own factor, so no reading changes.
  - The readings then fix the positions only up to the conformal (Möbius) group of the plane or of space, which has
    dimension 6 and 10, plus the one joint scaling of H and t: 7 and 11.

**Run 2 predictions** (committed before run 2):
- **L4′.** The rank is 4N − 7 in the plane and 5N − 11 in space, at new random rational points, for N = 5, 10 and 20.
- **L4″.** For each b, the infinitesimal special conformal map δx_i = 2(b·x_i)x_i − |x_i|²·b, together with
  δ ln H_i = σ·2(b·x_i) and δ ln t_i = −σ·2(b·x_i) for one sign σ, is in the Jacobian's null space exactly: J·v = 0 in
  Fractions, for every b on a coordinate axis, in the plane and in space. With the other sign it is not.
- **Kill conditions.** Either rank off; or no sign giving J·v = 0 exactly.
