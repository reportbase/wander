# MOT: motion and tracking from inside

*11 October 2026. Tom: "maybe h helps in object tracking and motion", then "yes, explore in physics.md", after the
reading that a situated reader can know when without knowing how far. Exact arithmetic and exact kinematics, no data.
Predictions written before the script (`mot/mot.py`) exists.*

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

### Run 1 (11 October, `mot/mot.py`)

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
