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
