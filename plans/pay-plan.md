# PAY: what arrives of the payload, serially and at once

*11 October 2026. Tom: "the payloads can't be recovered from serial situated observation, but can be in parallel situated
observation. basically, all we see is the motion of the center of gravity as situated observers of serial streams"; then
"yes" to a run and to naming the two centres (SPN R210). Exact arithmetic, rationals where the numbers are rational, the
complex step for rates. Predictions written before the script (`pay/pay.py`) exists.*

## Set-up, with the case kept

**Amounts:** a thing of half-size S at distance d; luminosities L, masses M, separations s, a source's radius R, a
step (the point-spread width σ).

**Readings:** x = S/d, read against the reader's own H. Ratios of readings taken at once share one denominator.

**Two centres, kept apart** (R210):
- the **median** of the addresses: an order statistic, at the corner, which exists where a mean does not;
- the **centroid** of an unresolved payload: a weighted mean, which is what arrives when the payload is below the
  step (the light-weighted photocentre; the total mass at the centre of mass).

Fingers order; rings add.

## Predictions

- **P1. One stream does not tell approach from growth.**
  - **The two worlds:** (a) a rigid thing approaching at speed u, x = S/(d₀ − ut); (b) a thing at rest growing as
    S(t) = S·d₀/(d₀ − ut).
  - **Predicted:** the streams are the same at every t, with the same time to contact x/ẋ. Neither S nor d can be read
    from the stream. Any S(t), d(t) with the same ratio give the same stream.
  - **Killed if:** the two streams differ by more than 1e-12 (relative) anywhere over 10³ random set-ups, or their x/ẋ do.
- **P2. A second reading taken at once separates them, if it shares the denominator.**
  - **The set-up:** a neighbour of half-size S₂ is read at the same moment.
  - **At the thing's distance:** the ratio of the two readings, x₁/x₂ = S₁/S₂, is a ratio of payloads. The shared
    distance cancels, so the observer's own motion cancels with it.
  - **Predicted:** under approach the ratio stays constant (to 1e-12), and under growth it follows S₁(t)/S₁(0) exactly.
  - **A neighbour at another distance** gives x₁/x₂ = (S₁/S₂)(d₂/d₁), and under approach that ratio drifts. Without a
    shared denominator, reading at once does not separate approach from growth.
  - **Killed if:** the same-depth ratio drifts under approach by more than 1e-12, or misses S₁(t)/S₁(0) under growth;
    or the other-depth ratio stays constant within 1e-6 under approach.
- **P3. Below the step, the payload arrives as its moments, the centroid first.**
  - **The set-up:** two point sources with lights L₁, L₂ (light fraction β = L₂/(L₁ + L₂)), a separation s, each
    blurred by a Gaussian step σ, and the blended image sampled finely.
  - **Predicted:**
    - (a) The image's first moment is the light-weighted mean of the two positions, the photocentre, at every
      separation, resolved or not, to 1e-12 of σ.
    - (b) Its second central moment is σ² + β(1 − β)s². The payload's internal structure arrives as a fraction
      β(1 − β)(s/σ)² of the step's own spread, two levels down per level the separation shrinks.
    - (c) With equal lights, the blend has a dip between the two (two maxima) exactly when s > 2σ, the Sparrow limit.
      That is the step, an amount: physics, not the corner.
    - (d) A binary orbiting its barycentre, unresolved, shows only the photocentre's orbit, of size a·|B − β| (B the
      mass fraction of the second star). Any (B, β) with the same B − β gives the same photocentre stream. Resolved
      against a shared background, the two components' orbits give B = a₂/a and the flux ratio gives β.
  - **Killed if:** (a) or (b) misses by more than 1e-9 (relative) over 10³ random set-ups; or (c)'s change from one
    maximum to two is not at s = 2σ within 1e-6 σ; or (d)'s photocentre streams differ by more than 1e-12 for equal
    B − β, or the resolved recovery misses B or β by more than 1e-12.
- **P4. From far off a body is its total mass at its centre of mass; its detail comes in level by level; the
  expansion's two forms meet at the corner and are each other's flip.**
  - **The set-up:** random point masses inside a sphere of radius R.
  - **Predicted:**
    - (a) About the centre of mass the first-order (dipole) term vanishes, so the monopole's relative error falls two
      levels per level of distance. About any other centre it falls one. Measured as slopes in levels between 100 R and
      1,000 R: −2 and −1, within 0.02.
    - (b) For one mass at radius ρ, the exterior series Σ ρ^l/r^{l+1} P_l(cos γ) converges for r > ρ and fails for
      r < ρ. Its terms along γ = 0 are all equal, 1/r, at r = ρ: the corner of the pair (ρ, r), where no order may be
      dropped.
    - (c) Kelvin's inversion, f ↦ (ρ/r)·f(ρ²/r), sends the interior series Σ r^l/ρ^{l+1} P_l onto the exterior one,
      term by term. It is exact in rationals for rational cos γ, l ≤ 30. A source on the sphere r = ρ is its own image
      (to 1e-12): the flip about the corner.
    - (d) The number of orders needed to read the body to a relative precision ε at distance r never exceeds
      ln(ε(1 − R/r))/ln(R/r) − 1. It grows without bound as r falls to R: level of detail by distance, with the corner
      the place where none can be dropped.
  - **Killed if:** (a)'s slopes miss; (b) converges inside or fails outside, over 10³ random cases at r/ρ = 0.9 and
    1.1 with 200 terms; (c) is inexact; or (d)'s bound is broken in any of 10³ cases.

Known already: the Sparrow criterion; photocentre and barycentre orbits of astrometric binaries (the photocentre's orbit
a(B − β), van de Kamp's form); the multipole expansion and its convergence outside the source's sphere; Kelvin's
inversion (1847); the centre of mass as the origin that removes the dipole; that a single image sequence cannot tell
approach from expansion (the size–distance ambiguity of looming). What PAY adds is the reading: the addresses' centre is a
median, the unresolved payload's a centroid. The payload arrives as its moments, each finer one further down by the
reading, and the expansion's two forms are the flip about the corner.

## Runs

### Run 1 (11 October, `pay/pay.py`)

Seed 17, four seconds. P4 (c) is in rationals; the rest are in floats, with rates by the complex step.

| | prediction | result | |
|---|---|---|---|
| P1 | approach and growth give one stream, and one x/ẋ | streams apart by at most 4.4e-16, x/ẋ by 6.7e-16, over 10³ set-ups | not killed |
| P2 | a same-depth neighbour read at once: the ratio is constant under approach and follows S₁(t)/S₁(0) under growth; another depth drifts | 4.4e-16 and 6.7e-16; another depth drifted at least 0.651 | not killed |
| P3 | (a) centroid = photocentre; (b) second moment σ² + β(1 − β)s²; (c) two maxima from s = 2σ; (d) photocentre orbit a·\|B − β\|, degenerate in B − β, resolved recovery | 5.3e-15 σ; 1.1e-15; 2.0000002 σ; 3.3e-16 and 3.3e-16; recovery to 1.1e-16 | not killed (see the note) |
| P4 | (a) slopes −2 and −1; (b) converges outside, fails inside, terms equal at the corner; (c) Kelvin exact, a source on the sphere its own image; (d) orders needed within the bound | −1.9995 and −1.0000; 1,000/1,000 and 1,000/1,000, yes; 0 of 9,300 inexact, 1.3e-15; 0 of 1,000 above the bound | not killed |

**A slip in the plan, recorded and not edited.** P3 (d) says the resolved orbits give "B = a₂/a". With B = M₂/(M₁ + M₂),
it is the first star's orbit about the barycentre that has size B·a, so B = a₁/a; the script recovers B that way. The
prediction's content holds; the index in it was wrong.

**Also from the run:**
- **The payload's share of the second moment** at β = ½ is β(1 − β)(s/σ)²: 0.0025, 0.0625, 0.25, 1 and 4 at
  s = 0.1, 0.5, 1, 2 and 4 σ. It falls two levels per level the separation shrinks.
- **The orders needed to read a body to 1e-6 of its monopole** (at most, over the random bodies), against the bound:
  - 157 against 345 at 1.05 R;
  - 54 against 85 at 1.2 R;
  - 24 against 36 at 1.5 R;
  - 16 against 20 at 2 R;
  - 8 against 9.2 at 4 R;
  - 5 against 5.05 at 10 R.

  Approaching the corner the count runs away; far off it is a handful.
- **Bug fixed before the recorded run:** the first launch failed on a mis-written random depth in P2, 10**(−1) on
  integers. The orders-needed loop now counts a body that never reaches 1e-6 as broken instead of zero; none did.

**Reading.**
- **A serial stream gives motion before it gives an object.** One stream carries the ratio's trajectory, and approach
  and growth are the same stream.
- **Two readings taken at once separate them when they share a denominator.** The common distance cancels from their
  ratio, which is a ratio of payloads: what one reader at once recovers is payloads relative to each other, never their
  scale.
- **Below the step, what arrives is the payload's moments.**
  - The first is its centroid, exact at any separation.
  - Each finer moment is further down by the separation over the step.
  - The binary's photocentre orbit holds only B − β; resolved against a shared background, B and β separate.
- **From far off a body is its total mass at its centre of mass.** Its detail comes in one order per power of the reading
  R/r. The two forms of the expansion meet at the corner, where no order may be dropped, and Kelvin's inversion is the
  flip about it.
- **The two centres of R210.** The addresses' centre is a median, an order statistic. The unresolved payload's is a
  centroid, a sum. Fingers order; rings add.

### Prior work in the drawing tool (found after run 1)

Tom, 11 October: "we have explore this in the draw.html repository in the labs". Four of draw's labs had already run
this ground on the shapes library. They were run again here at draw `ea07709` (9 October), headless, and their reports
read back.
- **`rcc`, the recovered circle.** One reader, one arrival at a time: dividing cancels the size, so the readings carry
  the turn and nothing else. They are Cauchy for every figure, the quartiles at ±1 to 0.000, though the figures' radii
  swing 5.7×. The census returns the same unit circle from all 4 of 4: "the radius that told them apart was never in the
  readings."
- **`udv`, undoing the division.**
  - One reader with the census gets the unit circle, missing the figures by up to 140% of their radius.
  - Three readers who know only the shape of their triangle get each figure exactly, up to its size (6 of 6, 2e-15).
  - One agreed length between two of them gives the figure itself (6 of 6, 2e-15).
  - "Another standpoint brings back the shape, one length the size."
- **`ref`, reference tests: where a serial reader gets the equality it marks against.** Three references were tried:
  - the median of the readings, which "requires every arrival to be held at once, and is therefore a parallel reference
    smuggled into a serial account": scale 100%, grain 100%, 12.0 marks;
  - the first arrival held and never updated (one slot): scale 88%, grain 100%, 10.9 marks;
  - the reader's own held value (nothing extra): scale 76%, grain 3%, 38.4 marks.

  "So the grain-free mark costs exactly one extra slot." The scale failures are 15 shapes that touch their reference
  without crossing it.
- **`rec`, record tests.** A serial reader's record (a tick per level crossed and a mark at each crossing of its
  reference) behaves as follows:
  - it is unchanged by rescaling (58 of 58);
  - it marks the same arrivals at every grain (58 of 58);
  - it reconstructs each address within half a level (58 of 58);
  - two grains recover their ratio from tick counts only asymptotically, 2.7% fine and 37% coarse;
  - a lost tick drifts the count until the next mark ends the drift: "the count leans on its history and the mark does
    not."

**What this changes in PAY's reading and R210.**
- **P1 and P2 are the motion case of what `rcc` and `udv` showed for shape.** `rcc` and `udv` are the stronger
  results: three standpoints give the whole figure up to its size, and one agreed length gives the size.
- **R210's "the median of the addresses" is a parallel quantity.** `ref` shows the median needs every arrival held at
  once. A strictly serial reader does not have it. What it can have is a held arrival, one extra slot, which does what
  the median does for grain (100%) though not always for scale (88%, where the shape touches its reference).
- **So the two axes in Tom's question are both real, and they are different.**
  - *Holding*, serial against parallel: whether the reader has the whole stream at once. It decides the address
    centre: the median (parallel) or a held arrival (serial, one slot).
  - *Resolving*, above or below the step: whether two payloads sit at least one step apart. It decides whether the
    payload arrives as components or only as its centroid.

**Moved (11 October, SPN R211).** Tom: "this is pure geometry not physics actually. lets move this into the main
papers." The geometry is now in:
- SPN §4.7, "Holding and resolving: what reaches a reader of a payload", with §2.1's "What 3 and 4 hold";
- `observation-from-somewhere.md`: §7.6, "Order needs holding"; Propositions 9–12 in §9; §8's "From far off".

`physics.md` §2.2 keeps the physical instances.
