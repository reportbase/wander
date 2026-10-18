# SUM: a sum of Cauchys, read as addresses

*18 October 2026 (Tom's local date). Tom: "what I'm not aware of is somone makng the clear and definitive statement that
cauchy is address, not payload. that is not a small distinction. that is everything."; then "It would be well known, if it
was know. we have done that search before."; then "yes" to two pieces: the rule stated plainly in OFS (done in §7.2: "a
Cauchy variable is a direction … never an amount"; "find the turn, and find the amount"), and the hard case worked
prediction-first. The hard case: a sum of independent Cauchy variables is again Cauchy (Lévy), which looks like adding
amounts. Exact mathematics and a seeded simulation; no physics.*

## The guess, withdrawn before any run

In conversation Claude guessed that the geometry reads a sum of Cauchys as composing directions, by tangent addition
(OFS §2, R327). Writing this plan, before any computation, that guess fails on its face. With X₁ = tan θ₁ and
X₂ = tan θ₂, θ uniform, the composed direction is tan(θ₁ + θ₂) = (X₁ + X₂)/(1 − X₁X₂). Its angle is uniform again, so
it is a standard Cauchy, scale 1. But X₁ + X₂ is a Cauchy of scale 2. So the sum is not the composition. The guess is
recorded here as withdrawn; P2 below checks the numbers.

## Known beforehand

These are classical, and are not tested as new:
- A Cauchy of centre m and scale γ is the landing point on a line of a uniform turn from the point (m, γ) above it. That
  is the lighthouse, and the Poisson kernel of the half-plane.
- Its characteristic function is e^{imt − γ|t|}, so independent Cauchys add their centres and their scales (Lévy). In
  complex form the point z = m + iγ adds (McCullagh 1996).
- A planar Brownian motion started at height γ lands on the line at a Cauchy of scale γ (harmonic measure). Watched at
  the times it first reaches each lower level, its horizontal place is the Cauchy process (Spitzer 1958).
- The mean of n standard Cauchys is a standard Cauchy.
- Normalized sums of symmetric variables whose tails fall as 1/x² tend to a Cauchy: the stable law of index 1.

## The reading, before the run

A sum of Cauchys is a relay of addresses: one turn's landing taken as the next standpoint's foot. Each summand is a
direction read in one chart: the landing of a uniform turn from a standpoint a height γᵢ above the line.

Relay two such readings. From a standpoint at height γ₁ + γ₂, turn uniformly and land on the line at height γ₂. From
that landing, now a standpoint γ₂ above the line, turn uniformly again and land on the line. Where it lands is X₁ + X₂.
- The reading's claim is that this is one uniform turn from height γ₁ + γ₂, not two.
- What adds is the standpoints' heights γᵢ (and feet mᵢ). These are amounts: the distance of a standpoint from the
  line, the payload's side.
- The sum itself stays a direction from the combined standpoint, read by its order. It still has no mean.

So the rule holds: in a sum of Cauchys, the turn is the combined standpoint's uniform turn; the amounts are the heights.

The stable limit is the case where no turn is visible in the summands. There the reading says the turn is in the limit
object: the Cauchy process is the horizontal place of a planar Brownian motion at the times it first reaches each level
(Spitzer). The summands themselves need not be directions; only the limit is.

### Predictions

- **P1 (the relay is one turn).** With γ₁ = 1 and γ₂ = 2:
  - exactly: the characteristic functions multiply to e^{−3|t|}, which is that of a uniform turn from height 3, at 200
    digits for t ∈ {0.1, 0.5, 1, 2, 5};
  - by simulation (seeded, 10⁶ draws each): the two-stage relay of uniform turns, from height 3 to height 2 to the line,
    and one uniform turn from height 3 have quartiles within 0.01 of ±3, and their Kolmogorov–Smirnov distance is under
    0.003.
  - *Killed* if either fails.
- **P2 (the sum is not tangent addition).** For γ₁ = γ₂ = 1 (seeded, 10⁶ draws):
  - the quartiles of X₁ + X₂ are within 0.01 of ±2;
  - those of (X₁ + X₂)/(1 − X₁X₂) are within 0.01 of ±1.
  - *Killed* if either fails.
- **P3 (averaging addresses gains nothing).** The mean of n standard Cauchys has quartiles within 0.01 of ±1, for
  n = 1, 10, 1000 (seeded, 10⁵ draws each). That is a relay from height n, rescaled by 1/n back to height 1.
  - Its spread does not fall as n grows.
  - *Killed* if any n's quartiles leave ±1 by more than 0.01.
- **P4 (the stable limit, the turn in the limit object).**
  - Normalized sums Sₙ/n of n symmetric variables with P(|Y| > y) = 1/y for y ≥ 1 (density 1/y², each sign alike; the
    centring is zero by symmetry) come close to the Cauchy of scale π/2.
  - The scale follows from tails c/y² on each side with c = ½: γ = πc. The Kolmogorov–Smirnov distance to Cauchy(0, π/2)
    falls with n: 0.02 or less at n = 1000 (10⁵ draws).
  - A planar Brownian motion started at height π/2, simulated in steps of 10⁻³ (10⁴ paths), lands with quartiles within
    0.05 of ±π/2.
  - *Killed* if the distance does not fall, or the landing quartiles miss.
- **P5 (the verdict).** A judgment, not a number: in every case above a turn and an amount can be named. The turn is
  the uniform turn from the combined standpoint (P1–P3) or the Brownian landing (P4). The amount is the heights. And no
  case has the Cauchy variable adding as an amount.
  - *Killed* if some case leaves no turn to name. Then the rule as written in OFS §7.2 needs narrowing, and I say so.

P1–P4 are classical, so a kill would be my set-up. P5 is the reading.

## Runs

(Nothing above this line is edited after a run.)
