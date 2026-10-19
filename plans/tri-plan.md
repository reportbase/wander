# TRI: triangulation read from a height

*19 October 2026 (Tom's local date), SPN R382.*

*ChatGPT, via Tom (10:55 MDT), on triangulation as relational reconstruction:*
- *two bearings and a baseline constrain a target;*
- *bearings alone give only a family of similar triangles, and the baseline supplies the magnitude;*
- *where the Cauchy might enter: bearings read at finite resolution, "a range of possible addresses with a height-dependent reading profile".*

*Its question: "does the Cauchy address structure give a new reconstruction rule, or does it provide a different
representation of the same classical solution?" Its proposed test: "Hold the target and baseline fixed, vary the reader
height, and compare the reconstructed position and its uncertainty against ordinary triangulation."*

*Claude answered:*
- *the reconstruction is classical, and is already in the corpus (below);*
- *what is new is narrower: bearings read from a height γ, with a Cauchy profile;*
- *the run tests that.*

*Tom (10:57): "yes".*

*Exact (mpmath) where a closed form exists, seeded samples elsewhere, thresholds in standard errors. Scripts in
`runs/tri/`.*

## Known beforehand

- **Classical triangulation.**
  - Directions give a figure up to scale; one carried-in length fixes it. These are OFS Propositions 8 and 11, and §9's
    survey (Snellius, Roy).
  - The error of a triangulated point under small angular errors is the linear map of those errors (first-order
    propagation).
- **In the corpus.**
  - **PXC** (`plans/pxc-plan.md`): half-baseline b, target on the bisector at distance d, k = d/b.
    - The relative depth error per unit angular error, from one standpoint, is cosh(ln k), least at the pair's corner
      k = 1 (the Thales circle).
    - The band is acosh(1/ε)/ln 2 levels on each side.
    - Run 4, P14: a noisy parallax's inverse has no mean and keeps its median.
  - **STC:** more readings sharpen the shape, never the scale.
  - **HTP:** a turn in place gives no baseline.
  - **ADR run 1, A5:** along a relay of Cauchy readings the error grows linearly in the number of readings, and averaging
    gains nothing.
  - **DYH run 3:** from height γ the address window is 2γ. Two equal Cauchy profiles read as two only when more than
    2γ/√3 apart.
- **draw's labs.** UDV: three standpoints give a figure up to size, and one agreed length gives the size. RCC: one
  reader's readings carry the turn, not the size.
- **The Cauchy is stable with index 1.** A sum w₁C₁ + w₂C₂ of independent Cauchys is a Cauchy whose scale is
  |w₁|γ₁ + |w₂|γ₂: scales add linearly. Normal errors add in quadrature.

## The set-up

- **The geometry.** Standpoints A = (−b, 0) and B = (b, 0), with b = 1 (the half-baseline, carried in). The target is at
  (x, d).
- **The reading.** A reads the target's direction from height γ: the angular error δ has tan δ ~ Cauchy(0, γ). This is
  the uniform turn's law read from height γ, the address on a flat screen one unit along the true line of sight. B reads
  likewise, independently.
- **The reconstruction.** The classical one: cross the two read rays.
  - On the bisector, with interior angles α_A and α_B to the baseline: d = 2/(cot α_A + cot α_B).
  - When cot α_A + cot α_B ≤ 0, the rays do not meet in front: "no forward crossing".
- **The comparison.** The same with normal angular errors of equal median absolute size: δ ~ N(0, σ²), with
  σ = atan(γ)/0.6745.

## Predictions

**T1 (the depth error is Cauchy, its scale the corner's law, to first order).** On the bisector at k ∈ {1/8, 1/2, 1, 2, 8},
γ = 10⁻⁴, with 10⁶ seeded readings per k:
- the relative depth error (d̂ − d)/d passes a one-sample KS test against Cauchy(0, 2γ·cosh(ln k)), with distance below
  1.36/√N;
- its median is within 3 standard errors of 0.

From d = 2/(cot α_A + cot α_B), each angle's relative sensitivity is cosh(ln k). The two Cauchy errors add their scales,
hence 2γ·cosh(ln k).

*Killed* if either fails at any k.

**T2 (Cauchy bearings add, normal bearings add in quadrature).** At k = 1 and the same median absolute angular error
(γ = 10⁻⁴), the ratio of the half-interquartile ranges of the relative depth error, Cauchy over normal, is √2. Two
standpoints do not average their Cauchy errors down: the depth inherits the sum of their scales.

*Killed* if the ratio is outside 3 standard errors of √2 (bootstrap, 10⁶ readings each).

**T3 (no mean; the share of no forward crossing).**
- (a) The probability of no forward crossing, P(cot α̂_A + cot α̂_B ≤ 0), is positive for every γ > 0. Computed exactly
  (a one-dimensional integral over the difference of the two angular errors) at k ∈ {1, 8} and γ ∈ {10⁻³, 10⁻²}.
  - The seeded sample (10⁶) agrees with it within 3 standard errors.
  - *Killed* if not.
- (b) The mean of d̂ does not settle. Over 20 batches of 10⁵ readings at k = 8, γ = 10⁻², the interquartile range of the
  batch means exceeds that of the batch medians by more than 10 times.
  - The normal errors' means also have no expectation (PXC P14), so this is not the Cauchy's alone.
  - *Killed* if not.
- (c) What is the Cauchy's own: at matched median angular error (k = 8, γ = 10⁻²), the probability of no forward crossing
  is more than 10⁶ times larger for Cauchy bearings than for normal ones, both computed exactly.
  - *Killed* if not.

**T4 (telling two targets apart: the corner's law again).**
- Two equal targets on the bisector at d and d + Δ are read by A as two Cauchy profiles on A's screen.
- They are told apart (two maxima) when Δ exceeds Δ* with Δ*/d = (4/√3)·γ·cosh(ln k) to first order. A depth step Δ
  turns A's bearing by Δ·b/(b² + d²), and run 3's threshold is 2γ/√3 on the screen.
- Exact screen positions and exact bisection on the count of maxima, at γ = 10⁻³ and k ∈ {1/4, 1, 4}: within 1% of the
  first-order value.
- So the best place to tell two depths apart is the pair's corner too.
- *Killed* if outside 1% at any k.

**T5 (the verdict).** A judgment. Bearings read from a height γ leave the classical reconstruction as it is: the same
crossing and the same baseline. They change its error law in three ways:
1. the depth error is a Cauchy, scaled by 2γ·cosh(ln k);
2. two standpoints' errors add, never average down;
3. rays failing to meet ahead are a visible share, where a normal model makes them vanishingly rare.

The address window per bearing is 2γ, the corner law is the geometry's, and depth resolution follows the corner.

*Killed* if T1, T2 or T4 is killed.

## What would and would not be shown

**Shown:** that ChatGPT's "different representation of the same classical solution" is right about the reconstruction, and
what reading at a height changes, exactly, in the error.

**Not shown:**
- that any real instrument reads bearings from a height;
- any claim about surveying practice, which carries its own error models.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (19 Oct, `python3 runs/tri/tri.py`; output `runs/tri/tri-run1.txt`, 32 s)

Nothing was killed.

- **T1 not killed.** At γ = 10⁻⁴ the relative depth error is Cauchy(0, 2γ·cosh(ln k)) at every k: KS distance 0.0006–0.0010
  against a limit of 0.00136.
  - The medians are within 0.91 standard errors of 0.
  - The upper quartile over 2γ·cosh(ln k) is 0.995–1.003.
- **T2 not killed.** At k = 1, the ratio of half-interquartile ranges, Cauchy over normal, is 1.4118 against √2 = 1.4142
  (bootstrap standard error 0.0028). Cauchy bearings add their scales; normal ones add in quadrature.
- **T3 not killed.**
  - (a) The exact probability of no forward crossing: 0.000638 and 0.00646 at k = 1 (γ = 10⁻³, 10⁻²); 0.00259 and
    0.0258 at k = 8. The samples agree within 0.8 standard errors.
    - The plan called the integral "over the difference of the two angular errors". The script integrates over A's
      error, with B's in closed form. That is also one-dimensional, and exact.
  - (b) Over 20 batches at k = 8, γ = 10⁻², the batch means' interquartile range is 271 times the medians'.
    - The means are those of the readings that cross in front. The rest have no depth, a direction only, so they have no
      mean to include.
  - (c) At matched median angular error (k = 8, γ = 10⁻²), the probability of no forward crossing is 0.0258 for Cauchy
    bearings and 9.3·10⁻³³ for normal ones: a ratio of 2.8·10³⁰.
- **T4 not killed.** The depth step at which two equal targets read as two, over the depth, against the first-order
  (4/√3)·γ·cosh(ln k):
  - k = ¼: 1.0003;
  - k = 1: 1.0012;
  - k = 4: 1.0046.

  The bisection on the count of maxima equals the closed form d + Δ* = b·tan(arctan k + arctan(2γ/√3)) to all digits
  shown.

**T5, the verdict: not killed.** ChatGPT's alternatives come apart cleanly:
- **Reading at a height does not give a new reconstruction rule.** The crossing and the baseline are classical, so it is
  a different representation of the same solution.
- **It gives a different error law, exactly:**
  1. **The depth error is a Cauchy.** Its scale is 2γ·cosh(ln k), least at the pair's corner. This is PXC's bell, with
     the scale of the reading in place of ε.
  2. **Two standpoints' errors add their scales.** They do not average down: √2 more than a normal model's at the same
     median error. This is ADR A5's relay, once.
  3. **Rays that fail to meet in front are a visible share,** 2.6% at k = 8 and γ = 10⁻², where a normal model puts them
     at 10⁻³².
  4. **Depth resolution follows the corner too:** Δ*/d = (4/√3)·γ·cosh(ln k).

The address window per bearing (2γ) is the geometry's. What the triangle does to it (cosh(ln k)) is the pair's corner.

The mathematics is classical: error propagation, the stable index 1, and run 3's threshold. The reading is ours.

### Run 2 predictions: the payload reader beside the address reader (19 Oct, written before the run)

*Tom (11:07 MDT): "seems to me we can use the payload and address reader to retrieve more informattion abou the ojet."
Claude proposed a run: what an amount read at both standpoints adds to the bearings (a check, a rescue of the misses, the
breadth). Tom (11:09): "yes".*

**Known beforehand.**
- **Bipolar coordinates** (classical). The pair A = (−b, 0), B = (b, 0) has natural coordinates (σ, τ):
  - σ = the angle ATB at the target, the parallax angle;
  - τ = ln(r_A/r_B).
  - x = b·sinh τ/(cosh τ − cos σ), y = b·sin σ/(cosh τ − cos σ).
  - The curves of constant τ are Apollonius's circles; those of constant σ are the circles through A and B. The two
    families are orthogonal, and the map is conformal with one scale factor, h = b/(cosh τ − cos σ).
- **Reliability** (Baarda 1968). With one redundant reading, a gross error can be detected but not located.
  - Every reading's standardized residual (w-test) has the same magnitude.
  - Two redundancies are needed to locate it.
- **In the corpus.**
  - OFS §4, "The address points at the payload": two reads, one point.
  - R332: one read, two breakdowns.
  - CFH: a range per address is writing.
  - draw's UDV: a third standpoint.

**The bridge.** The payload is an amount F received at both standpoints, falling as a known power of distance,
F ∝ r^(−p). For light p = 2, the inverse square: a physics bridge, named. The unknown unit and the source's strength
cancel from F_A/F_B, so τ̂ = (1/p)·ln(F_B/F_A) is unitless. It is read with a normal error of sd s.
The angular size of a sphere of radius R (U6) gives τ with no physics bridge: sin β = R/r, so
sin β_B/sin β_A = r_A/r_B.

**What the two readers read.**
- The address reader's bearings give σ = π − α_A − α_B, so δσ = −(δ_A + δ_B).
- The bearings also give τ = ln(sin α_B/sin α_A), so δτ = cot α_B·δ_B − cot α_A·δ_A.
- The payload reader gives τ alone.
- So the two readers read the two orthogonal coordinates of the pair, each with its own corner:
  - σ = π/2 is the Thales circle, the address pair's corner;
  - τ = 0 is the perpendicular bisector, where the two amounts are equal: the payload pair's corner.

The set-up is run 1's otherwise: k = d/b on the bisector, with tan δ ~ Cauchy(0, γ) per bearing.

**U1 (the coordinates, exact).** At 10⁴ seeded targets anywhere in front:
- σ from the bearings and τ = ln(r_A/r_B) give back the target through the formulas above, to 10⁻¹²;
- ln(sin α_B/sin α_A) equals τ, to 10⁻¹²;
- the Jacobian ∂(x, y)/∂(σ, τ) is h times a rotation, to 10⁻⁹ relative (finite differences at 50 digits).

*Killed* if any fails.

**U2 (on the bisector, depth is the address reader's alone).**
- y is even in τ, so ∂y/∂τ = 0 at τ = 0. A ratio of any precision changes the depth's error on the bisector only at
  second order.
- At γ = 10⁻⁴ and k ∈ {1/8, 1, 8}, with 10⁶ readings each: the half-interquartile range of the relative depth error from
  (σ̂, the true τ) equals that from the bearings alone, within 3 bootstrap standard errors.

*Killed* if not.

**U3 (the ratio fixes the lateral coordinate, and helps near).**
- On the bisector x is odd in τ, so ∂x/∂σ = 0 there, and the lateral error is h·δτ, with h = ½(1 + k²) = k·cosh(ln k).
- From the bearings alone the lateral error is Cauchy(0, 2γb·cosh(ln k)).
- From σ̂ and the ratio it is normal, with half-interquartile range 0.6745·s·b·k·cosh(ln k).
- The ratio is better where k < k* = 2γ/(0.6745·s): near the baseline, where the bearings are nearly opposite.
- At γ = s = 10⁻⁴ (k* = 2.965) and k ∈ {1/8, 1/2, 1, 2, 8}, with 10⁶ readings each: both measured half-interquartile
  ranges are within 3 bootstrap standard errors of these values, and the better one changes between k = 2 and k = 8.

*Killed* if not.

**U4 (one bearing and the ratio close the triangle; the misses rescued).** With the ratio exact (s = 0):
- (a) A's bearing alone with the ratio gives the point: A's ray meets τ's Apollonius circle. On the bisector δ_B = δ_A,
  so δσ = −2δ_A. The relative depth error is Cauchy(0, 2γ·cosh(ln k)), the same law as two bearings, and no better.
  - KS distance below 1.36/√N at γ = 10⁻⁴, k ∈ {1/8, 1, 8}, N = 10⁶.
- (b) Of run 1's no-forward-crossing readings (k ∈ {1, 8}, γ = 10⁻²), a reading is rescued when one bearing's ray meets
  the bisector ahead (that bearing below π/2).
  - Neither ray meets it only when both bearings are at or past π/2, which implies no crossing.
  - So the share rescued is exactly 1 − p²/P_nc, with p = (1/π)·arctan(kγ) and P_nc run 1's exact probability of no
    forward crossing: about 0.975 at k = 8 and 0.998 at k = 1.
  - The seeded sample (10⁶) agrees within 3 standard errors.
- (c) The rescued depths' median absolute relative error is within 10% of that of the forward crossings of the same
  readings.

*Killed* if (a), (b) or (c) fails.

**U5 (the ratio checks the bearings: it detects a misread, and cannot say which).**
- With the ratio, a pair has three readings for two unknowns. The closure is c = ln(sin α̂_B/sin α̂_A) − τ̂.
- (a) In the linearized least-squares model (normal errors, sd σ_b per bearing, s on τ), the three w-tests have equal
  magnitude at every target, to 10⁻¹². So blaming A, B or the ratio fits equally well.
- (b) A misread Δ in A's bearing moves c by −cot α_A·Δ, which is −Δ/k on the bisector.
  - Set the threshold at the 99.9% quantile of |c| without a misread (γ = 10⁻⁴, s = 10⁻³).
  - The misread detected half the time is Δ₅₀ = k·c_thr to first order, within 5% at k ∈ {1/2, 2, 8}.
  - So a check of a given size catches misreads that grow in proportion to the distance.

*Killed* if (a) or (b) fails.

**U6 (the breadth, in b, and a ratio without a bridge).** A sphere of radius R at the target. Each standpoint reads its
two edges, each with Cauchy(0, γ) error. The bearing is the edges' mean, and the angular radius β is half their
difference.
- (a) R̂ = r̂_A·sin β̂_A, with r_A from the triangulation (b carried in, so R̂ is in b).
  - To first order δ ln r_A = sinh(ln k)·δ_A + cosh(ln k)·δ_B on the bisector.
  - So, for cot β ≥ |sinh(ln k)|, R̂/R − 1 is Cauchy(0, γ·(cot β + cosh(ln k))).
  - KS distance below 1.36/√N at γ = 10⁻⁵, R = 0.05 b, k ∈ {1/8, 1, 8}, N = 10⁶.
- (b) The angular sizes' ratio gives τ̂ = ln(sin β̂_B/sin β̂_A) with no bridge. Its error is Cauchy(0, 2γ·cot β) on the
  bisector, against the bearings' Cauchy(0, 2γ/k).
  - It is better only where cot β < 1/k, that is R > d: an object larger than its distance from the baseline.
  - At k = ½ and R ∈ {0.4 b, 0.6 b}, γ = 10⁻⁵, N = 10⁶: the ratio of half-interquartile ranges (size over bearings) is
    k·cot β (1.137, 0.825) within 3 bootstrap standard errors.

*Killed* if (a) or (b) fails.

**U7 (the verdict).** A judgment. *Killed* if U1, U2 or U4 is killed. The two readers read the pair's two bipolar
coordinates, orthogonal and with one scale:
- the address reader the parallax angle σ (its corner the Thales circle);
- the payload reader the log ratio τ (its corner the bisector, equal amounts).

What the payload adds:
1. On the bisector, nothing to the depth: depth is σ's alone.
2. The lateral place, where the bearings are weak (near the baseline).
3. A stand-in for a missing bearing, as good as the bearing and no better, which rescues most misses.
4. A check that detects a misread bearing but cannot locate it.
5. With angular size, the breadth in b, and a ratio needing no bridge but weaker than the bearings for any object clear
   of the baseline.
