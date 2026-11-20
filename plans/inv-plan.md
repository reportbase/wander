# INV: is the near/far exchange the facings' exchange?

*19 Nov 2026. SPN R1118. Tom: "Interesting about ehulers simplification with shv. The inverse"; "Both. Just noticing
all the inverses including Omega"; to Claude's question whether d/H ↔ H/d (along the look) is the same exchange as
s ↔ 1/s (across it), "Yes. I'm just hunting for deeper mesnings". Exact (sympy), predictions written before the run.*

## Setup

- The slope s = v/h of one direction, its law the half-Cauchy (2/π)·ds/(1 + s²), the uniform turn θ with s = tan θ.
- The distance reading x = d/H, its law the overlay's heat (1/π)·sech(ln x) per unit of ln x (R702, R703).
- Euler's plane: u = ln x across, θ up (R736).
- Heat on the plane (`euler.html`): cos²(θ − π/4)·sech(u).

Known beforehand: R580 (the two corners as mirror lines on the log plane), R728 (the hot spot one thumb out at the
corner), R801 (four identities, one exchange), `euler.html`'s lay g = (2/π)·atan(d/H) = ½ + gd(ln(d/H))/π. So X1 and X2
are expected; X3 and X4 say what is new or not.

## Predictions

- **X1.** The distance law, written in x, is exactly the slope's law: (1/π)·sech(ln x)·d(ln x) = (2/π)·dx/(1 + x²).
- **X2.** Both are unchanged by their exchange (s ↦ 1/s, x ↦ 1/x), both have median 1 and quartiles √2 ∓ 1, and
  w(x)·w(1/x) = −1 with w(x) = (1 + ix)/(1 − ix), landing 0, 1, ∞ at +1, i, −1. (X1 and X2 are the same arithmetic once
  X1 holds, so they cannot fail separately; said here, not hidden.)
- **X3.** On Euler's plane the two exchanges are reflections in perpendicular lines (θ = π/4 and u = 0). Done together
  they are one half turn about (u, θ) = (0, π/4), the heat's peak; the heat is unchanged by each and by both.
- **X4.** The two differ in their motion. A turn (θ ↦ θ + a, on the whole turn) leaves the uniform law in θ unchanged.
  Changing the thumb (u ↦ u + ln k) moves the sech law: the median of x goes to k. So the slope's law is unmoved by its
  motion, the distance's is moved by its own.
- **X5.** In the angle chart the two laws differ: θ is uniform, u is not (sech/π). They agree only in the ratio chart,
  through θ′ = atan x = π/4 + gd(u)/2 being uniform when u is sech-distributed.

Kill: any stated equality not exact (sympy simplifies the difference to 0), X3's composite not a half turn about
(0, π/4), or X4's median not k.

## Runs

**Run 1** (`runs/inv/inv.py`, output `inv-run1.txt`, 19 Nov). Nothing killed. X1: the distance overlay written in x is
exactly the half-Cauchy, the slope's own law. X2: both kept by their exchange, median 1, quartiles √2 ∓ 1, w(x)·w(1/x) = −1
(as predicted, these follow from X1 and could not fail apart). X3: on Euler's plane the two exchanges are reflections in
θ = π/4 and u = 0; together one half turn about (0, π/4), the heat's peak (value 1), the heat kept by each and both.
X4: changing the thumb carries the median of x to k exactly; the turn's clause is the uniform law shifted on the whole
turn, an identity, entered as true and not computed. X5: atan(eˣ) = π/4 + gd(u)/2 (checked to 55 digits at u = 7/5, the
symbolic simplifier not closing it), its derivative sech(u)/2, so θ′ = atan(d/H) is uniform exactly when u is
sech-distributed; in the angle and level charts the two laws differ (uniform against sech).

**Reading.** The near/far exchange is the facings' exchange: one law (the half-Cauchy), one exchange, one fixed point
(the reading 1), in the ratio chart. Along the look the reading is d/H, across it v/h; both are a slope of a pair. On
Euler's plane they are two perpendicular mirrors, and their meeting point is the heat's peak, the one place fixed by
both, so the hot spot (R728) is the two corners as one point. What tells them apart is the motion: a turn leaves the
slope's law where it is, a new thumb moves the distance's median to the thumb. So turning reads, changing the thumb
re-sizes: the same exchange, held by different motions. Classical pieces (the half-Cauchy, the Gudermannian, two
reflections composing to a half turn); the sorting a reading. Ω and 1/Ω are not in this: they have no fixed point to
meet at.

**Run 2, predictions** (19 Nov, written before `runs/inv/inv2.py`; Tom: "yes", to checking the SHV equivalent of Euler's
plane). The SHV holds the pair (s, x), the slope across the look and the bar share d/H along it, and can read each as its
share, p = 1/(1 + s²) and q = 1/(1 + x²), a point of the unit square.

- **Y1.** Each exchange is the reflection p ↦ 1 − p (and q ↦ 1 − q) exactly; the corner and the bar's tip sit at
  (½, ½), the one point fixed by both; both at once is the half turn about (½, ½), as on Euler's plane, with no π or e.
- **Y2.** Changing the thumb, x ↦ kx, is rational in the share: q ↦ q/(q + k²(1 − q)), a Möbius map of [0, 1] fixing
  0 and 1 (home and the horizon), and composing over k by multiplying.
- **Y3.** Turning, s ↦ s ⊕ a, is not rational in p: p ↦ (√p − a√(1 − p))²/(1 + a²) (from PYT's identity
  1 + (s ⊕ a)² = (1 + s²)(1 + a²)/(1 − sa)²), rational only in the shares' roots h = √p, v = √(1 − p). So in the share
  square the exchanges are simple and the thumb rational, the turn needs a root; neither motion is a translation.
- **Y4.** The uniform turn's law, carried to p, is the arcsine law 1/(π√(p(1 − p))), symmetric about ½; the sech law
  of distance carried to q is the same arcsine law. The share chart's density carries π (the law's total), though
  every map above is π-free.
- **Y5.** After x ↦ kx the median of q moves from ½ to 1/(1 + k²).

Kill: any stated equality not exact (sympy to 0, or 50 digits where it does not close), Y3's map rational in p, or
Y2's map not fixing 0 and 1.

**Run 2** (`runs/inv/inv2.py`, output `inv-run2.txt`, 19 Nov). Nothing killed. Y1: each exchange is p ↦ 1 − p exactly,
the one fixed point ½ (the corner, the bar's tip), both at once the half turn about (½, ½). Y2: x ↦ kx is
q ↦ q/(q + k²(1 − q)), fixing 0 and 1, M_k′ ∘ M_k = M_(kk′). Y3: the turn is (√p − a√(1 − p))²/(1 + a²), not rational
in p, rational in (h, v) as (h − a·v)²/(1 + a²); its shift depends on p (at a = ⅓: −3/10 at p = ½, (1 − 3√3)/20 at
p = ¼), so not a translation. Y4: the slope's law in p and the distance's in q are both the arcsine law
1/(π√(p(1 − p))), total exactly 1; sympy left an Abs(√(1 − p)) open (p not declared below 1), closed at 50 digits as the
kill allows. Y5: after x ↦ kx the median of q is 1/(1 + k²) at k = 2, 7/3, 10.

**Reading.** The SHV's counterpart of Euler's plane is the pair (s, x), and in shares the unit square: the two corners one
point (½, ½), the two exchanges two reflections, both at once a half turn, with no π, e or angle in any map. What the
square gives up is Euler's one trick: neither motion slides. The thumb is a Möbius map of the share, rational; the turn
needs the shares' roots, h and v, so the turn is the slope's (tangent addition) or the roots' ((h − a·v)), never the
share's alone. And the law on the square carries π (the arcsine's 1/π), though no map does: π is the law's total, the
DHV's, not any motion's. So Euler's plane trades π and e for addition; the share square keeps fractions and pays in
motions that do not add.

Closed (19 Nov; Tom: "ok, proceed with your recommendation"): the share square's pieces are classical (the exchanges
h² ↔ v², the thumb an odds ratio, the arcsine law), and its half turn is Euler's under a chart (q = ½(1 − tanh u),
p = cos²θ). Not explored further.

**Run 3, predictions** (19 Nov, written before `runs/inv/inv3.py`; Tom: "proceed with the open thread", item 23's last
open point: Ω and 1/Ω, the one pair with no fixed point). Ω = ∫₀^∞ ds/(1 + s²), the trace's walk for a bar of one
thumb; 1/Ω the coefficient that makes it a law. Claude's reading, to be checked: Ω and 1/Ω are not a pair of the
exchange at all, but the length of the chart in which the exchange is a reflection and the factor that makes that
length 1.

- **Z1.** In the weight chart w(s) = ∫₀^s dt/(1 + t²) the exchange s ↦ 1/s is exactly w ↦ Ω − w: a reflection whose
  fixed point is Ω/2, at s = 1, the corner. Ω is the span of that reflection, not a value it moves.
- **Z2.** Multiplying by 1/Ω turns it into g ↦ 1 − g on [0, 1] (g the share of the sweep passed); the pair (Ω, 1/Ω)
  becomes (1, 1) and Ω leaves every statement. So the pairing of Ω with 1/Ω depends on the chart; the pairing of s
  with 1/s does not (in the weight chart and in g it is still the one reflection, fixed at the corner).
- **Z3.** The one family that carries Ω and 1/Ω as values, the walk over the chord r(s) = w(s)·√(1 + s²)/s and its
  reciprocal, has product 1 everywhere and meets (r = 1) only at home (s → 0), not at the corner (r(1) = Ω/√2·… =
  1.1107); it reaches Ω and 1/Ω only at the horizon.
- **Z4.** That family is not the exchange: r(1/s) ≠ 1/r(s) (at s → ∞, r(1/s) → 1 while 1/r(s) → 1/Ω).
- **Z5.** Ω/2 (the corner in the weight chart) is not 1/Ω, and no choice of thumb moves Ω (it has no unit to move).

Kill: any stated equality not exact (sympy to 0, or 50 digits where it does not close); Z3's family meeting anywhere but
home; Z4's two equal.

**Run 3** (`runs/inv/inv3.py`, output `inv-run3.txt`, 19 Nov). Nothing killed. Z1: in the weight chart the exchange is
w ↦ Ω − w, fixed at Ω/2 = w(1), the corner (sympy left arctan(1/s) + arctan s = Ω open for s > 0; closed by its derivative
0 and at 50 digits, as the kill allows). Z2: divided by Ω, g ↦ 1 − g on [0, 1], and (Ω, 1/Ω) becomes (1, 1). Z3: the walk
over the chord r(s) and its reciprocal multiply to 1, r rises from 1 at home through Ω/√2 = 1.1107 at the corner to Ω at
the horizon, meeting 1/r only at home. Z4: r(1/s) ≠ 1/r(s) at every s tried (at 10³⁰, 1 against 1/Ω). Z5: Ω/2 ≠ 1/Ω; the
total of ds/(1 + s²) is Ω whatever the thumb.

**Reading.** Ω and 1/Ω have no fixed point because they are not a pair of the exchange. Ω is the length of the chart in
which the exchange is a mirror, w ↦ Ω − w, and that mirror has a fixed point, Ω/2, the corner: the trace's walk folded at
its middle. 1/Ω is the factor that makes the length 1, the share g, where the mirror is g ↦ 1 − g (run 2's square) and Ω
is gone. So their product 1 says only that the unit interval has length one; no read moves Ω to 1/Ω. Where they do
appear as two values, in the walk over the chord and its reciprocal, the two meet at home, not at the corner, and that
family is not the exchange. So the pairs of item 23 sort in two: maps on directions (s ↔ 1/s, d/H ↔ H/d, w(s) ↔ w(1/s),
the heat's halves), each with a fixed point at the corner or the tip, and a change of chart (Ω ↔ 1/Ω), which has none.
A reading; classical parts (arctan s + arctan(1/s) = π/2).
