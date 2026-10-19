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
