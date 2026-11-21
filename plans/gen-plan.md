# GEN: the reader geometry generated from the rules

21 Nov 2026. Tom: "have established the rules, can we now generate the complete reader geomety/". The rules are
`plans/bar-steps.md` steps 17–19 (SPN R1157–R1159), with the turn of steps 13–14 (R1153, R1154). This note derives the
read geometry from them in order, each step from those before. Every claim is committed here before `runs/gen/gen.py`
is written; the script checks them exactly (sympy) or to 40 digits (mpmath). A claim that fails is recorded as killed.

Words: a single vantage in its own terms (trace and pivot, slopes, shares), no angle and no trigonometric function given
to a read (R793, R1110). Where a result is the dual hemispherical vantage's (DHV: both hemispheres, a total, π), it is
marked so.

## The rules

- **A.** Take any point P.
- **B.** From P pick another point Q.
- **C.** The distance PQ is the thumb, 1. It is the hypotenuse.
- **D.** The legs v1, v2, v3 of PQ are derived from it, given that they have the same extent (one thumb each, not one
  thumb between them).
- **E.** Q is turned about P with PQ kept (steps 13–14).

Nothing else is given: no unit, no second length, no angle, no π.

## What is generated, as claims

**G1. Readings are slopes of legs.** By C and D, any Q is v1² + v2² + v3² = 1 (Pythagoras with the thumb the
hypotenuse). A reading is a ratio of legs, s = v2/v1, s₂ = v3/v1, and 1 + s² + s₂² = 1/v1². Scaling every length by k
moves no reading.

**G2. One pair: the shares.** In one pair (v3 = 0), writing h = v1, v = v2: h² + v² = 1, h = 1/√(1 + s²),
v = s/√(1 + s²), home at s = 0, the horizon as s grows without end. √(1 + s²) is the one root.

**G3. Rational points from one half-slope.** For rational t, h = (1 − t²)/(1 + t²), v = 2t/(1 + t²) satisfy h² + v² = 1
exactly and give the slope s = 2t/(1 − t²): every rational slope with a rational root comes from one half-slope.

**G4. Composition keeps the thumb.** Turning Q by slope a from slope s gives s ⊕ a = (s + a)/(1 − sa), and
1 + (s ⊕ a)² = (1 + s²)(1 + a²)/(1 − sa)²: the composed shares again square to 1 (E is kept).

**G5. One weight is unchanged by composition.** ds/(1 + s²) pulled back through s ↦ s ⊕ a is ds/(1 + s²) for every a.
The trace's walk per unit of the pivot's pointing is that weight, h².

**G6. The exchange and the corner.** s ↦ 1/s keeps the weight too (up to orientation), so its fixed point s = 1, where
h = v = 1/√2, splits the weight in equal halves: the median of the readings is 1, with no π needed for "half".

**G7. No mean.** ∫ s·ds/(1 + s²) from 0 to M grows as ½·ln(1 + M²) without bound.

**G8. The total is a completion.** ∫₀^∞ ds/(1 + s²) is Ω = π/2 (the DHV's number; reached by no rational step:
rational half-slopes return home only for t ∈ {0, 1}, checked to n = 50 compositions).

**G9. Three legs: the screen's law.** On a screen square to leg v1, readings (s, s₂) uniform over the directions have
density (1/2π)·(1 + s² + s₂²)^(−3/2) over the whole screen (all four facings of the pair), and in one octant every pair is
at its corner (each pair's shares below 1 a half), the near field in both readings (s ≤ 1 and s₂ ≤ 1) a third, and the
six orders of v1, v2, v3 a sixth each.

**G10. The equal extent is what puts the corner at 1.** If the legs are drawn with unequal extents (v2 at c times v1),
the read weight's median moves to s = 1/c; only c = 1 has the median at the corner. At the triple corner with equal
extents each leg is 1/√3.

**G11. Near and far.** Along any direction a point at distance d (in thumbs, Q at 1) reads d inside the thumb and 1/d
past it; the exchange d ↦ 1/d fixes d = 1. The overlay's heat (1/π)·sech(ln d) per unit of ln d is the half-Cauchy in d
(G5's weight with s = d), half below d = 1 and half above.

**G12. Euler's −1 as an exchange.** The landing point w(s) = (1 + is)/(1 − is) has |w| = 1, w(s)·w(a) = w(s ⊕ a),
w(1) = i (the corner) and w(s)·w(1/s) = −1 for every s > 0, all in rational arithmetic. e^(iπ) = −1 is the member at
s = 0 paired with the horizon (DHV).

**G13. Nothing has a size.** Every quantity G1–G12 is unchanged when P, Q and every other point are scaled by k about P.

## Runs

*(nothing above this line is edited after the run)*
