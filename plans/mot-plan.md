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
