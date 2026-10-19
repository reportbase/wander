# MOT: motion and tracking from inside

*11 October 2026. Tom: "maybe h helps in object tracking and motion", then "yes, explore in physics.md", after the
reading that a situated reader can know when without knowing how far. Exact arithmetic and exact kinematics, no data.
Predictions written before the script (`runs/mot/mot.py`) exists.*

## Set-up, with the case kept

A thing of half-size S at distance d closes on the reader at speed u: S, d and u are amounts. The reader reads only the
ratio x = S/d, its v/h for the pair (half-size, distance), and the turn θ = arctan x. Past the pair's corner (x > 1) the
thing is wider than it is far. The reader holds one amount in time, its own clock: the tick Δt between looks. Every
time below is in ticks of that clock.

**Bridges.** Time: the reader's clock, its own, as H is its own breadth. Length: none in P1 to P5. P6 uses the reader's
own breadth B as a baseline, the one length it holds.

## Predictions

- **P1. Time to contact from the ratio is exact.** τ = x/ẋ equals d/u at every distance, before and past the corner,
  with no S, d or u known. Killed if |τ/(d/u) − 1| exceeds 1e-12 anywhere on 0.001 ≤ x ≤ 1000.
- **P2. Read from the turn, it is not.** θ/θ̇ = (d/u)·arctan(x)·(1 + x²)/x: 1 far off, π/2 at the corner, growing
  without bound past it. Killed if the factor at x = 1 differs from π/2 by more than 1e-12, or is not increasing in x.
- **P3. Two looks a tick apart give τ exactly, if divided by the older reading.** At constant closing speed, with x₁
  then x₂ one tick later: x₁/(x₂ − x₁) ticks is exactly τ at the second look; x₂/(x₂ − x₁) is τ one tick earlier, one
  tick late. Killed if either differs from its prediction by more than 1e-9 of τ over 10⁴ random approaches.
- **P4. Holding the corner tracks the approach, and the levels bunch toward contact.** A reader that re-sets its unit to
  keep the thing at its corner changes it at the rate d ln H/dt = 1/τ. At constant closing speed each doubling of the
  reading (one level of approach) takes half the time of the one before, and all of them, from distance d₀, sum to
  d₀/u: infinitely many levels before contact. Killed if the times per level do not halve to 1e-12 or their sum misses
  d₀/u by more than 1e-12 of it.
- **P5. Bearing rate and τ read how close a thing will pass.** For a thing on a straight course, ω the rate its
  direction turns and τ = x/ẋ from its reading: the closest approach, as a share of its present distance, is
  m/d = ωτ/√(1 + (ωτ)²), from readings alone. ωτ is itself a reading, tangential over radial speed, so its corner,
  ωτ = 1, is a pass at 1/√2 of the present distance; a bearing that holds still, ω = 0, is a collision. Killed if the
  formula misses the true closest approach by more than 1e-9 of d over 10⁴ random courses, or ω = 0 fails to give a
  collision.
- **P6. The reader's own breadth is a baseline, good only near.** Two looks at once from the ends of a breadth B (two
  eyes) read the convergence γ = 2·arctan(B/2d), and d = (B/2)/tan(γ/2) exactly. With γ rounded to a step ε, the worst
  relative error is ε·d/(2B) while that is small: amounts in the reader's own unit near home, lost past about B/ε
  baselines. Killed if the worst error over a step differs from ε·d/(2B) by more than 10% of it for εd/B between 0.01
  and 0.2.

- **P7. The baseline reads best at its corner** (added 11 October, after P1 to P6 were committed and before the script
  was written). For the pair (B/2, d) the relative change in the distance read per unit of convergence is
  |d ln d/dγ| = 1/sin γ: least, 1, at γ = 90°, where d = B/2 (the pair's corner), and the same at d and at its flip
  (B/2)²/d. So a reader that can set its breadth reads a distance best with B = 2d, its baseline at the corner with the
  thing: the claim that the best H puts the thing read at the corner (SPN Proposition 1.2), with the baseline as H.
  Killed if, with ε = 10⁻⁴ radian, the distance whose worst rounded error is least is not within 1% of B/2; or if
  |d ln d/dγ|·sin γ differs from 1 by more than 1e-12; or if the first-order errors at d and (B/2)²/d differ by more than
  1e-12 of either.

Known already, and not predictions: τ = θ/θ̇ is Lee's tau (Lee 1976), read from the turn of a small thing; its rate
τ̇ = −1 at constant speed, and a braking that holds τ̇ at −½ stops at contact. Constant bearing, decreasing range is the
navigators' collision rule. Stereo depth's error growing with distance squared over baseline is textbook. What is
tested here is the reading: which of the reader's quantities (the ratio, the turn, the older or newer look, the corner
held) give these exactly.

## Runs

### Run 1 (11 October, `runs/mot/mot.py`)

Rationals where the arithmetic is rational (P3, P4's levels); elsewhere floats, with every rate of a reading taken by the
complex step (exact to rounding, and never from the reading's formula). Seed 12. Three seconds.

| | prediction | result | |
|---|---|---|---|
| P1 | x/ẋ = d/u, 0.001 ≤ x ≤ 1000 | worst 4.4e-16 | not killed |
| P2 | θ/θ̇ ÷ (d/u) = arctan(x)(1 + x²)/x, π/2 at x = 1, increasing | worst 6.7e-16; π/2 to the last digit; increasing | not killed |
| P3 | x₁/(x₂ − x₁) = τ at the second look; x₂/(x₂ − x₁) = τ + 1 tick | both exact in rationals, 10⁴ approaches, τ from 1.5 to 10⁴ ticks | not killed |
| P4 | d ln H/dt = 1/τ; levels halve; their sum d₀/u | 4.4e-16; every one of 60 levels halves exactly in 1,000 approaches; 60 levels short of d₀/u by 2⁻⁶⁰ | not killed |
| P5 | m/d = ωτ/√(1 + (ωτ)²); ω = 0 a collision | worst 4.4e-16 of d in 10⁴ courses; aimed courses ωτ and miss ≤ 3.9e-16 | not killed |
| P6 | worst error per step ε·d/(2B), within 10% for εd/B in [0.01, 0.2] | 0.8% off at 0.01, 3.8% at 0.074, 11.1% at 0.2; past 10% from 0.183 | **killed** |
| P7 | least error at d = B/2 (ε = 10⁻⁴); 1/sin γ; d and (B/2)²/d alike | at d = 0.49999 B (2.3e-5 off); 5.6e-16; 2.1e-14 | not killed |

Values from the run:
- P2: the turn's factor is 1 (to 7 digits) at x = 0.001, 1.00665 at 0.1, π/2 at the corner, 14.86 at 10, 1,570 at 1,000.
  Far off, the turn gives τ; at the corner it overstates it by π/2; past the corner it grows as (π/2)·x.
- P4: each level of approach takes exactly half the τ read at its start.
- P5: at ωτ = 1 the pass is 0.707106781186547 of the present distance.
- P6: the exact recovery d = (B/2)/tan(γ/2) holds to 3.8e-15 from 0.01 B to 10⁴ B. Rounding to the step, the far side
  (γ read low, d read long) and the near side part:
  - the far side is x/(1 − x) and the near side x/(1 + x), with x = εd/(2B), each to 0.25% (the tangent's departure
    from the angle at d = 10 B);
  - a fixed grid of steps, with d swept over two whole steps of γ, finds the same worst (1.008, 1.014, 1.038 and 1.125 of
    ε·d/(2B), the last over a window reaching x = 0.11).
- P7, the worst rounded error in half-steps, for d = 0.05, 0.5, 5 and 50 B: 5.05, 1.000, 5.05, 50.1. A thing at a tenth
  of the corner's distance and one ten times past it read alike.

**Reading.**
- P1 to P5 are identities of kinematics, and the run confirms them to rounding. What it settles is which of the reader's
  readings carries each one exactly:
  - the ratio x carries τ at every distance;
  - the turn carries τ only far off;
  - the older look carries τ now, and the newer one carries τ one tick ago;
  - the product ωτ is a ratio with no clock left in it.
- POL run 10's kick read 8% low from two looks a tick apart (its P25, killed; post hoc: "divided by the newer reading,
  and the tick is a tenth of a fast pair's τ"). P3 makes that exact: the newer look gives τ + 1 tick, and at τ = 10
  ticks a kick in 1/τ reads 1/1.1 of itself, 9% low. The cloth's slowing is not in P3.
- P6 was killed by my prediction, which kept only the first order. The error is one-sided past the first order: the far
  side's x/(1 − x) has no bound at x = 1, that is at d = 2B/ε, where the convergence can round to nothing. That is the
  baseline's horizon, an amount (the step), so physics, not the corner.
- P7 is the corner of the pair (half-baseline, distance), in levels, with its flip. Surveying knows that a right angle of
  intersection is the best-conditioned fix; read here, that is the corner. A reader that can choose its baseline (how far
  it moves between two looks) reads a distance best with its half-breadth equal to the distance, and as badly at d as at
  (B/2)²/d.

### Run 2: predictions (11 October, written before `runs/mot/mot2.py` exists)

Tom: "connecting known kinematics to the corner may reveal a deeper geometric truth, but if all we can do is explain
motion through our vocabulary, that might be useful, particularly using ratios instead of angles may simplify the
math"; then "yes, even if we could just provide a fuller geometric explanation of motion using our corner insights, that
would be a win."

**Set-up.** b = B/2 is the half-baseline, d the distance, both amounts. Their pair's reading is k = b/d, and the unit
relation, capped at 1, is u = min(k, 1/k) with one bit for the side. Other pairs are named where they are used. Each
pair's corner is its own and needs no bridge; the amounts a result needs are named with it.

**Two kinds of corner** (a derivation, which the predictions instance). Take a quantity f of a pair through its ratio k.
- If swapping the pair leaves f unchanged, f(k) = f(1/k). Differentiating gives f′(k) = −f′(1/k)/k², so f′(1) = −f′(1),
  and f′(1) = 0. **A swap-symmetric quantity is stationary at the corner.** In levels (ln k) it is even, and the corner
  is its centre.
- If swapping the pair flips f's sign, f is zero at the corner (by continuity). **A sign-odd quantity changes regime at
  the corner.**

**Predictions.**
- **P8. Ranging by three readers of k, each reading to a step ε = 10⁻⁴.**
  - **The readers:** (a) the angle φ = arctan k, even in φ; (b) the unit relation u, even in u on each side of the
    corner; (c) the plain ratio k, even in k and uncapped.
  - **To first order, the relative error in d per step** is (a) 2/sin 2φ, (b) 1/u, (c) 1/k = d/b.
  - **Predicted:** (a) and (b) are least at the corner, and alike at d and b²/d. (c) has no interior least; its error
    only grows with d.
  - **Killed if:** for (a) or (b), the worst rounded error over 0.01 b ≤ d ≤ 100 b is least more than 1% from d = b, or
    the first-order errors at d and b²/d differ by more than 1e-12 of either; or (c)'s worst rounded error ever falls as
    d grows.
- **P9. Equal budgets: the Cauchy's lay against the in-place lay.** N addresses cover every distance.
  - **The two lays:** the even turn spreads N over φ in [0, 90°] (the lay that gives the Cauchy). The in-place lay puts
    N/2 evenly in u on each side of the corner: proportion inside, 2 − 1/s past it. The plain ratio cannot cover every
    distance with finite N.
  - **Per address, the relative error** is π/(N sin 2φ) for the even turn and 2/(N u) for the in-place lay. Their
    ratio, in-place over even turn, is 4cos²φ/π (for d ≥ b, the same at the flip).
  - **Predicted:** at the corner the ratio is 2/π, so the in-place lay reads π/2 better. Far off and near home it
    rises toward 4/π, where the even turn reads better. They are equal where cos²φ = π/4: u = √(4/π − 1) = 0.52272,
    that is d = 1.91306 b and 0.52272 b.
  - **Killed if:** the ratio from complex-step sensitivities misses 4cos²φ/π by more than 1e-12 anywhere on 10⁻³ b to
    10³ b, or either crossing misses by more than 1e-4 of itself.
- **P10. The ratio forms are trig-free and exact; the angle forms are not; turning is the exception.** Each problem has
  a referee (world positions), a ratio reader and an angle reader.
  - **The ratio reader** is given what a ratio reading gives: the size reading x = S/d, the bearing as a slope q
    against its own axis, two looks or their rates.
  - **The angle reader** is given the angular half-size θ = arctan x, the bearing angle β and their rates.
  - **The problems:** (A) time to contact head-on, from two looks; (B) stereo with parallel axes: the place (X, Z)
    from the two slopes, Z = 2b/(q_L − q_R); (C) closest approach, m/d = |r|/√(1 + r²), r = ωτ, with ω = q̇/(1 + q²)
    and τ = x/ẋ; (D) the collision test, the bearing still.
  - **Predicted for A–D:** each ratio form agrees with its referee to 1e-12 (relative) over 10³ random cases and calls
    no transcendental function (√ is allowed; calls are counted). The angle forms of A, B and C agree only by calling at
    least one (tan or sin). D needs no call in either form.
  - **(F) Steady turning:**
    - the angle advances by addition, with no call a step, but each place read costs cos and sin;
    - the capped pair (the larger component set to 1, the other the unit relation) advances by a fixed rotation (two
      constants computed once) and a division by its larger component, with no call a step. Each place read costs one √;
    - **predicted:** both track the referee to 1e-9 over 10⁴ steps. The plain ratio's largest magnitude over a whole
      turn is at least cot(ωΔt/2), unbounded as the step shrinks, while the capped pair never exceeds 1.
  - **Killed on any failure.**
  - Since I write the readers, the call counts show only that a trig-free exact form exists; the test is the agreement
    with the referee.
- **P11. Braking reads its corner.**
  - **Derivation:** with closing speed u, deceleration a and stopping distance s = u²/(2a) (amounts), τ = d/u gives
    τ̇ = −1 + d·a/u², so **τ̇ + 1 = d/(2s)**. Lee's critical τ̇ = −½ is therefore s = d: the pair (stopping distance,
    distance) at its corner. τ̇ + ½ = (d − s)/(2s) is sign-odd: a thing stops short when s < d and overshoots when
    s > d.
  - **Predicted:** the ratio reader computes τ̇ = 1 − x·ẍ/ẋ² from its readings with no call.
  - **Killed if:** over 10⁴ random states that τ̇ misses −1 + d/(2s) by more than 1e-12; or classifying by τ̇ ≷ −½
    disagrees with the exact rational referee (s against d) in any state; or 10³ states built with s = d exactly read
    τ̇ off −½ by more than 1e-12.
- **P12. Swap-symmetric quantities in motion are stationary at the corner; the others are not.**
  - **Three swap-symmetric quantities:**
    - the range of a launch at fixed speed, against k = V_y/V_x: (2U²/g)·k/(1 + k²), since 2V_x·V_y/g is unchanged
      when the speeds swap. Its corner is 45°; complementary launches go equally far. U and g are the amounts;
    - the share of energy a head-on elastic collision passes to a ball at rest, against the mass ratio k: 4k/(1 + k)².
      All of it passes at equal masses;
    - the baseline's conditioning, sin γ = 2k/(1 + k²) with k = b/d (P7).
  - **Two from the same launch that are not swap-symmetric:** the time of flight ∝ k/√(1 + k²) and the greatest
    height ∝ k²/(1 + k²).
  - **Predicted:** each symmetric one has f(k) = f(1/k) to 1e-12 on 10⁻³ ≤ k ≤ 10³, f′(1) = 0 to 1e-12 (complex
    step), and its grid maximum at k = 1 (within the grid step), computed from k with no call. The two others are
    strictly increasing, with f′(1) > 0.
  - **Killed on any failure.**

Known already: complementary launch angles give equal range; equal masses pass all the energy (the same form, 4k/(1+k)²,
as the maximum power transfer theorem); Lee's τ̇ = −½; rectified stereo's Z = fB/disparity; Wildberger's rational
trigonometry, which replaces angles by spreads (sin², bounded in [0, 1]) to make trigonometry algebraic; arctan
computed by folding at 1, arctan x = π/2 − arctan(1/x). What run 2 adds is the reading: which corner each is, of which
pair, of which kind, and that the capped unit relation keeps both the ratio's algebra and the angle's best-conditioned
middle.

### Run 2 (11 October, `runs/mot/mot2.py`)

Seed 13, two seconds. P11 is in exact rationals; the rest are in floats, with rates by the complex step. Each reader is
handed a counting math namespace (√ free, every trig call counted).

| | prediction | result | |
|---|---|---|---|
| P8 | angle and unit relation least at the corner, alike at d and b²/d; plain ratio has no interior least | both least at d = 0.99995 b (the grid point beside b; the far side's rounding is the larger); alike to 1.0e-14 and 4.4e-16; plain ratio rises throughout (and is 10⁴ off alike) | not killed |
| P9 | in-place over even turn = 4/(π(1 + u²)): 2/π at the corner, toward 4/π, equal at 0.52272 b and 1.91306 b | worst 1.4e-13; 0.636620 at the corner; 1.273238 at 10³ b; equal at 0.522723 b and 1.913058 b | not killed |
| P10 | ratio forms of A–C exact (1e-12) with no call; angle forms agree by calling; D none in either; F as stated | ratio forms 2.2e-13, 2.9e-13, 4.4e-16 with no call; D 0 wrong both ways with no call; F as predicted; **but the angle forms, with their calls, miss 1e-12: A 1.9e-10, B 1.2e-12** (C 4.4e-16) | **killed** (the angle clause) |
| P11 | τ̇ + 1 = d/(2s); τ̇ ≷ −½ classifies; s = d reads −½ | 0 of 10⁴ off, 0 misclassified, 0 of 1,000 off −½, all exact | not killed |
| P12 | the three swap-symmetric quantities: f(k) = f(1/k), f′(1) = 0, greatest at 1; the two others increasing; no call | 6.7e-16 at most; f′(1) = 0.0 each; greatest at k = 1.0000 each; flight and height increasing (f′(1) = 0.354, 0.500); 0 calls | not killed |

Values from the run:
- **P8, the worst error in half-steps at d = 0.01, 0.1, 0.5, 1, 2, 10, 100 b:**
  - angle: 100.0, 10.1, 2.5, **2.0**, 2.5, 10.1, 100.5;
  - unit relation: 100.0, 10.0, 2.0, **1.0**, 2.0, 10.0, 100.5;
  - plain ratio: 0.01, 0.1, 0.5, 1.0, 2.0, 10.0, 100.5.

  At one step, the unit relation is twice as good as the angle at the corner and as good or better everywhere. Past the
  corner it is the plain ratio. Inside the corner the plain ratio is far better per step, but only by an unbounded range
  of addresses: reading d = 0.01 b needs k = 100, a hundred times the unit relation's whole range. P9 makes that
  budget explicit.
- **P10 F, turning over 10⁴ steps of 0.1, 0.01 and 0.001:**
  - the angle reader is within 1.6e-10, 1.4e-11 and 9.9e-13, making 208 calls for 104 place reads;
  - the capped pair is within 7.2e-14, 7.0e-14 and 8.9e-14, making two calls in all (the constants). Its unit relation
    peaked at 0.99928, 0.999985 and 0.999982;
  - the plain ratio peaked at 80.7, 1,256 and 4,910, against cot(δ/2) = 20.0, 200 and 2,000.
- **P10 A:** the angle reader with no call (θ₁/(θ₂ − θ₁), Lee's from two looks) was off by up to 9 × 10⁵ of τ.

**What killed P10's angle clause** (post hoc). A double spaces the angle evenly near 90°, about 2.2e-16 apart. So the
ratio read back through tan is held to ulp·(1 + x²)/x relative: 2.2e-16 at x = 1, 2.2e-15 at 10, 2.2e-13 at 1,000,
2.2e-11 at 10⁵. That is P8's angle reader with its step one ulp: past the corner an angle holds a ratio worse in
proportion to its size. The capped unit relation min(x, 1/x) is held to about 1.5e-16 at every x. Folding sends both ends
of the range toward 0, where doubles are finest; the angle sends one end to 90°, where they are not. My prediction
assumed that a call makes the angle forms exact. It does in arithmetic; in a reader with a step it does not, past the
corner. The turning results agree: the angle reader, whose angle grows without bound, drifted 1.6e-10, while the capped
pair stayed within 1e-13 (reducing the angle by whole turns would help it; the pair needs no reduction).

**Not predictions:**
- **Braking judged from θ/θ̇ with no call**, wrong in 1 of 2,000 states with S/d in [0.01, 0.1), 182 in [0.1, 1) and
  996 in [1, 10) (s/d log-even in [0.1, 10]). Far off the angle's τ̇ is good. Toward the corner it starts to fail, and
  past it it is a coin toss. The ratio's τ̇ is exact everywhere (P11).

**Reading.**
- **Corners in motion come in two kinds, as the derivation says.**
  - *Stationary*: the range of a launch (45°), the energy one ball passes to another (equal masses), the baseline's
    conditioning (half-baseline equal to the distance). Each is unchanged when its pair swaps.
  - *Change of regime*: braking (stopping distance equal to the distance, Lee's τ̇ = −½). It changes sign when its
    pair swaps.
  - Quantities with no swap symmetry, such as a launch's time of flight and greatest height, have no corner.
- **The range and the baseline's conditioning are one form, 2k/(1 + k²)**, the sine of the facing 2θ written in the
  ratio (the tangent half-angle form). The range of a launch is (U²/g) times the sine of its facing.
- **The ratio reader needs no trig for time to contact, stereo, closest approach, collision or braking.** The angle
  reader needs a call to be exact, and even then holds big ratios poorly. Angles are simpler only for advancing a
  steady turn. There the capped pair does as well with no call a step, and stays bounded.
- **Of the three readers of one pair**, only the bounded ones (angle, unit relation) have a best place, the corner, and
  the unit relation's is twice the angle's at one step. At one budget of addresses, the in-place lay reads best between
  0.52 b and 1.91 b (by π/2 at the corner); the even turn, the Cauchy's lay, reads best outside that (by 4/π far off
  and near home).

### Run 3: predictions (11 October, written before `runs/mot/mot3.py` exists)

Tom: "yes", to special relativity in unit relations. The run follows the archived *Special Relativity, Through the
Fisheye* (`papers/archive/sr-through-the-fisheye.md`) and its survey (`plans/archive-gems.md`).

**Set-up, with the case kept.**
- **Amounts:** the relative speed u, the constant c, a mass m, a momentum p, a proper acceleration a and the reader's
  proper time τ.
- **The bridge from u to a reading is c**, a known constant. β = u/c and 1/γ = √(1 − β²) are the unit relations v and
  h, one unit for both, so v² + h² = 1 (`v-and-h.md` item 48). The reading v/h = γβ is the celerity w.
- **The Doppler factor is k = √((1 + β)/(1 − β)).** It is a ratio of two of the reader's own intervals (sent and
  received), so it needs no bridge. Its levels are ζ = ln k, the rapidity.

**Predictions.**
- **P13. Three pairs, three corners.** Each pair's swap is an involution on its reading with one fixed point.
  - **(a) The Doppler pair (sent, received):** k ↔ 1/k is β ↔ −β (approach against recession). Its corner is k = 1,
    rest.
  - **(b) The pair (β, 1/γ), equivalently (pc, mc²):** the swap is w ↔ 1/w. Its corner is w = 1: β = 1/√2, momentum
    energy equal to rest energy, k = 1 + √2, ζ = ln(1 + √2) = 0.881374.
  - **(c) The sky's pair (fore, aft):** for a direction at θ from the motion, the reading is t = tan(θ/2), and the swap
    is t ↔ 1/t (θ ↔ π − θ). Its corner is θ = 90°, the transverse plane.
  - **Predicted:** the three corners are three different places, and a boost moves only (c)'s. The moving observer's
    transverse plane is the rest frame's direction with tan(θ/2) = k exactly. At (b)'s corner, that is θ = 135°, and
    the forward hemisphere is seen within 45°.
  - **Killed if:** β → −β fails to give k → 1/k to 1e-12; or β = 1/√2 fails to give w = 1, k = 1 + √2 and those two
    directions to 1e-12.
- **P14. γ and γβ are the two kinds of corner of the Doppler pair.** Over 10⁴ random rational k in [1/1000, 1000],
  exactly in rationals:
  - γ = (k + 1/k)/2 is unchanged by the swap, so it is stationary at rest;
  - γβ = (k − 1/k)/2 flips its sign under the swap, so it is zero at rest;
  - k = γ + γβ and 1/k = γ − γβ: the Doppler factor's even and odd parts in levels;
  - β = (k² − 1)/(k² + 1) and 1/γ = 2k/(1 + k²), the facing's sine, P12's form;
  - β² + (1/γ)² = 1.

  By complex step: dγ/dζ = 0 and d(γβ)/dζ = 1 at rest, to 1e-12.
  **Killed on any inexact identity or either derivative missing.**
- **P15. Rapidity is the reader's lay of celerity, smoothed.**
  - **The reader's lay** of w is w inside the corner and 1 + ln w past it. Rapidity is ζ = asinh w.
  - **Predicted:** both have slope 1 at home and slope 1/w far off. The gap (lay − rapidity) rises throughout, from 0
    at home through 1 − ln(1 + √2) = 0.118626 at the corner, toward 1 − ln 2 = 0.306853 (nats) and never past it.
  - **Killed if:** the gap is not increasing on 10⁻⁶ ≤ w ≤ 10⁶; or its value at the corner, or at w = 10⁶ against the
    limit, misses by more than 1e-9.
- **P16. Pseudorapidity is a direction's level, and a boost along the axis pans every level by ln k.**
  - **Predicted:** η = −ln tan(θ/2) is the sky pair's reading in nats. Over 10⁴ random θ and β in (−0.99, 0.99), a
    boost along the axis gives η′ − η = ln k. The swap fore ↔ aft is η ↔ −η. For a massless particle,
    ½ ln((E + p_z)/(E − p_z)) = η.
  - **Killed if:** any of these misses by more than 1e-12.
- **P17. The relativistic regime switches at (b)'s corner, symmetrically for the energy and not for the kinetic
  energy.**
  - **For E** = √((pc)² + (mc²)²), with x = pc/mc² (the celerity): the level-slope d ln E/d ln x = x²/(1 + x²) = β².
    This is a share of the circle: ½ at the corner, with s(x) + s(1/x) = 1.
  - **For T** = E − mc²: its level-slope is x²/(√(1 + x²)(√(1 + x²) − 1)), which runs from 2 at home to 1 far off. At
    the corner it is 1 + 1/√2, not 1.5, and s_T(x) + s_T(1/x) is not constant. This repeats NRF: the corner switch is
    symmetric where the quantity is a share.
  - **Killed if:** E's slope misses β², or its swap sum misses 1, by more than 1e-12; or T's corner slope misses
    1 + 1/√2 by more than 1e-12; or T's swap sum is within 1e-6 of a constant over 10⁻³ ≤ x ≤ 10³.
- **P18. Levels of motion, three ways.** A level is one doubling of the Doppler factor, k = 2ⁿ.
  - **Predicted:** under uniform proper acceleration a from rest (ζ = aτ), each level takes exactly ln 2/a of the
    traveller's proper time. In the launch frame's time t = sinh(aτ)/a, level n is reached at t_n = (2ⁿ − 2⁻ⁿ)/(2a),
    and each level takes Δ_n = (2ⁿ + 2⁻ⁿ⁻¹)/(2a), its ratio to the last tending to 2. Set beside P4, where the levels
    of an approach at constant speed each take half the last, the traveller's levels come evenly and the launch frame's
    double.
  - **Killed if:** the rationals for t_n and Δ_n (a = 1, n ≤ 40) differ from sinh(n ln 2) and its differences by more
    than 1e-12 relative; or the ratio at n = 20 differs from 2 by more than 1e-9.

Known already: Bondi's k-calculus (k, β = (k² − 1)/(k² + 1)); rapidity adds (Varićak 1910, Robb 1911); pseudorapidity
equals rapidity for a massless particle; d ln E/d ln p = β² follows from dE/dp = u; the non-relativistic and
ultra-relativistic regimes either side of pc ~ mc²; hyperbolic motion, t = sinh(aτ)/a; the headlight effect. What run 3
adds is the reading: three named pairs, their corners and their kinds, and the regime switch symmetric only where the
quantity is a share.

### Run 3 (11 October, `runs/mot/mot3.py`)

Seed 15, two seconds. P14 and P18 are in exact rationals; the rest are in floats, with rates by the complex step.

| | prediction | result | |
|---|---|---|---|
| P13 | three pairs, three corners; a boost moves only the sky's; tan(θ/2) = k seen at 90°; at (b)'s corner 135°, the forward hemisphere within 45° | k(β)k(−β) = 1 to 2.2e-16; w = 1, k = 1 + √2, ζ = asinh 1 = 0.881374 to 2.2e-16; seen at 90° to 1.1e-15 rad; 135.000000000000° and 45.000000000000° | not killed |
| P14 | γ even, γβ odd, k = γ + γβ, 1/k = γ − γβ, β and 1/γ = 2k/(1 + k²), β² + (1/γ)² = 1; dγ/dζ = 0, d(γβ)/dζ = 1 at rest | every identity exact for 10⁴ of 10⁴ rational k; 1e-60 and 1.000000000000000 | not killed |
| P15 | the gap lay − asinh rises throughout, 0.118626 at the corner, toward 1 − ln 2 | slope positive everywhere on 10⁻⁶ to 10⁶; 0.118626; 0.306852819 at 10⁶ | not killed |
| P16 | η′ − η = ln k; fore ↔ aft is η ↔ −η; a massless particle's rapidity is η | 1.8e-15, 5.8e-15, 2.2e-14 over 10⁴ draws, θ in 0.05 to π − 0.05 (my range: nearer the ends, 1 − cos θ loses digits in floats) | not killed |
| P17 | E's level-slope β², ½ at the corner, s(x) + s(1/x) = 1; T's 1 + 1/√2 at the corner, its swap sum not constant | 3.3e-16; 0.500000000000000; 2.2e-16. T: 2.000000 at 10⁻³, 1.707106781186547 at the corner, 1.001000 at 10³; its swap sum runs from 3.000999 at the ends to 3.414214 (2 + √2) at the corner | not killed |
| P18 | hyperbolic motion; level n at k = 2ⁿ; t_n and Δ_n exact; ratio → 2 | all exact for n ≤ 40 ((x + 1)² − t² = 1; k² = 4ⁿ); t_n against sinh 2.4e-15; launch-frame ratios 1.5000, 1.8333, 1.997076 at n = 1, 2, 5, and 1.999999999997 at 20; proper time per level ln 2 | not killed |

**Reading.**
- **Special relativity has three corners, one for each pair it holds:**
  - rest, for the Doppler pair (sent, received);
  - β = 1/√2, for (β, 1/γ), where momentum energy equals rest energy;
  - the transverse plane, for the sky's (fore, aft).

  Saying "the corner" in SR without naming the pair is ambiguous three ways (the archived paper's "three exchanges,
  three fixed points").
- **The pairs meet in two exact places:**
  - the moving observer's transverse plane is the rest frame's direction with tan(θ/2) = k, so the sky's corner reads
    off the Doppler pair's reading;
  - at the (β, 1/γ) corner, that direction is 135°, and the whole forward hemisphere is seen within 45°.
- **In the Doppler pair's levels, γ is the even part of k and γβ the odd part:** k = γ + γβ. These are run 2's two kinds
  of corner:
  - time dilation is stationary at rest, unchanged when sender and receiver swap;
  - celerity changes sign there.

  1/γ = 2k/(1 + k²) is the facing's sine of the Doppler pair, the same form as a launch's range and a baseline's
  conditioning. β = −cos F and 1/γ = sin F, with k = tan(F/2).
- **Rapidity is the reader's lay of celerity, smoothed.** It is proportional at home and logarithmic far off, with the
  same slopes, and never more than 1 − ln 2 nats (0.44 doublings) from the lay. The gap is 0.119 nats at the corner.
  Physics' additive speed is the reader's two address spaces joined smoothly.
- **A direction's level is its pseudorapidity.** A boost along the axis pans every level by the same ln k, and fore and
  aft are the flip.
- **The regime switch is at the corner of (pc, mc²).**
  - E's level-slope is β², a share of the circle: halfway at the corner and flip-symmetric, as NRF found for light where
    the count is a share.
  - T is not a share, and its switch is lopsided: 1 + 1/√2 at the corner, its swap sum running from 3 to 2 + √2.
- **Levels of motion, three ways:**
  - approaching at constant speed, each level takes half the time of the last (P4);
  - under uniform proper acceleration the traveller's levels come evenly, one per ln 2/a;
  - in the launch frame each takes twice the time of the last.

All the physics here is standard (Bondi, Varićak and Robb, hyperbolic motion, the regimes either side of pc ~ mc²).
What the run adds is the account: which pair, which corner, which kind, and where the switch is symmetric.
