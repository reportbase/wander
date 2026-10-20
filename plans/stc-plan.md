# STC: why the construction from situated observations can succeed

*12 October 2026. Tom, in a passage he shared: "Physics already constructs the completed view from situated observations,
and the framework supplies a geometric reason the construction can succeed. … Several situated observations, plus one
external amount that fixes scale, are assembled into a representation that no individual observation held." Then "yes"
to Claude's five refinements and to this test. A simulation of our own, checked against a full referee (the true
figure, known to the script). Predictions written before the script (`runs/stc/stc.py`) exists.*

## The claim, refined

A single reading is situated: one facing, one breadth held, its addresses laid in the reader's own unit. It cannot hold
the true breadth (OFS Proposition 8(a)). Physics assembles several situated readings plus one amount from outside into
a figure no single reading held: parallax from a baseline, triangulation, multi-epoch astrometry, the distance ladder.
The geometric reason this can work is classical (similarity invariance, triangulation). What the framework adds is the
separation:
- **The addresses are exact while the scale is arbitrary.** Directions, order and shape up to scale do not depend on
  the scale (OFS Theorem 6, Proposition 8(a)).
- **One outside amount fixes every amount linked to it** (OFS Proposition 8(b)), and the correction is one common
  factor: a translation in levels for every amount, whatever the lay. The reader's logarithmic far-field lay keeps its
  room per doubling under it; the near field takes it as a plain rescaling; the drawing V = H is never redrawn (R215).
- **Stitching needs links.** Overlap (a shared landmark or denominator, OFS Propositions 7 and 10), the standpoints'
  placement known up to scale (Proposition 11(b)), and a chain of readings from each amount to the outside one
  (Proposition 8(b)). Unlinked amounts stay unfixed.
- **Not every practice constructs.** Co-adding exposures from one standpoint beats noise (resolving); it adds no
  standpoint and no scale (SPN R210, R211: holding and resolving are two axes).

**The consequence tested here.** More readings improve the figure: errors in direction, order and shape average down.
They never improve the scale: the scale is exactly as good as the one outside amount, and every linked amount shares its
error as one shift in levels. The separation of addresses from payload lines up with physics' split between statistical
error (averages down) and systematic calibration error (does not). Along a ladder each rung's calibration error carries
up, as one shift, to every rung above it.

## Set-up, with the case kept

Everything here is amounts (positions, lengths, luminosities, fluxes, in world units); no unit relation is used.
- **The figure.** M = 20 landmarks at fixed random places, x in [−50, 50], y in [100, 200] (seeded).
- **The readers.** N standpoints evenly spaced along the x-axis over a span S = 10 centred on the origin. Each reads
  the bearing of every landmark with independent angular noise of sd σ_θ = 10⁻³ rad. The readers know their own
  placement only up to scale: in their own unit the span is 1. *Bridge:* the baseline's shape (travel along a line,
  known up to scale).
- **The outside amount.** The span's true length, supplied as S₀ = S·e^ε, ε ~ N(0, σ_s²), σ_s = 0.01, one draw per
  trial: a calibration with its own error. *Bridge:* a shared fact (one known length).
- **The construction.** Each landmark placed by least squares from its N bearing lines, in the readers' unit, then
  scaled by S₀.
- **A second rung, a standard candle.** A kind whose members have ln L ~ N(μ, σ_k²), σ_k = 0.1. The 20 landmarks are
  its calibrators: their fluxes F = L/(4πd²) are read exactly, and the kind's ln L is estimated as the mean of
  ln(4π d̂² F) over them. Far members (n_far of them, at distances 10³ to 10⁴) are placed by d̂ = √(L̂/(4πF)).
  *Bridges:* a known kind (equal mean luminosity, scatter σ_k) and light's inverse square.
- **Measures**, per trial, with the referee's true figure:
  - each landmark's log-distance error e_m = ln(d̂_m/d_m) (d from the baseline's middle);
  - the **common shift** c = mean over landmarks of e_m (the pan);
  - the **shape error** r = rms over landmarks of (e_m − c), what is left after the pan;
  - the far rung's mean log-distance error f = mean over far members of ln(d̂/d).
- 2,000 trials at each N in 16, 64, 256, 1,024, 4,096 (seed 12).

## Predictions

- **P1. The figure improves with readings.** The trial-averaged shape error r falls as N^(−½): the slope of ln r on ln N
  over the five N lies in [−0.55, −0.45].
  - **Killed if** the slope is outside that range.
- **P2. The scale does not.** The sd of the common shift c over trials stays at the outside amount's error.
  - For N ≥ 256 the sd lies within 10% of σ_s = 0.01.
  - From N = 64 to N = 4,096 the sd falls by less than 10%, while r falls by about a factor of 8.
  - **Killed if** either fails.
- **P3. The error becomes one shift.** As N grows, the landmarks' log-distance errors move together: their mean pairwise
  correlation across trials rises with N and is at least 0.95 at N = 4,096.
  - **Killed if** it is below 0.95 there, or does not rise.
- **P4. A ladder carries its calibration up.** At N = 4,096:
  - the far rung's mean error f has sd within 10% of √(σ_s² + σ_k²/(4·20)) = 0.0150, both for n_far = 100 and for
    n_far = 10,000. A hundred times more far members shrink it by less than 10%; if errors averaged down they would
    shrink it tenfold;
  - its correlation with the rung below's shift c is within 0.1 of σ_s/0.0150 = 0.667.
  - **Killed if** either fails.

Known already: triangulation, similarity invariance, the propagation of calibration (systematic) error up the distance
ladder, and that systematic error does not average down. What STC adds is the reading: the addresses improve with
readings, the scale is the outside amount's, and the split is the split between address and payload.

**Real data, queued.** A published parallax zero-point (a calibration of the instrument's own scale) appearing as one
common shift in levels across a catalogue's distances. The archives that hold it (ESA, VizieR) are blocked from here.

## Runs

### Run 1 (12 October, `runs/stc/stc.py`)

Seed 12, 2,000 trials at each N, fourteen seconds.

| N | shape error r | sd of the common shift c | mean correlation of the landmarks' errors |
|---|---|---|---|
| 16 | 0.01317 | 0.01052 | 0.370 |
| 64 | 0.00692 | 0.00997 | 0.666 |
| 256 | 0.00367 | 0.01022 | 0.891 |
| 1,024 | 0.00215 | 0.00990 | 0.967 |
| 4,096 | 0.00154 | 0.00986 | 0.992 |

| | prediction | result | |
|---|---|---|---|
| P1 | r falls as N^(−½): slope in [−0.55, −0.45] | slope −0.394: r halves per fourfold N up to 256, then flattens (0.00367, 0.00215, 0.00154) | **killed** |
| P2 | sd of c within 10% of 0.01 at N ≥ 256; falls < 10% from N = 64 to 4,096 | 0.01022, 0.00990, 0.00986; ratio 0.989 while r falls 4.5× | not killed |
| P3 | correlation rises, ≥ 0.95 at N = 4,096 | 0.370, 0.666, 0.891, 0.967, 0.992 | not killed |
| P4 | far rung's mean error sd within 10% of 0.0150 at n_far 100 and 10,000; correlation with c within 0.1 of 0.667 | 0.01598 and 0.01478; a hundred times more far members shrink it 7.5%; correlation 0.666 | not killed |

**Reading, before any fix.** The scale behaved as predicted: whatever the number of readers, the common shift stays at
the outside length's error, and a hundred times more far members leave the far rung's error where the calibration put
it. P1's kill is in the shape. The likely cause is my estimator: least squares on the bearing lines puts the noise
into the lines themselves (errors in the variables), which biases each landmark's depth by an amount that does not
shrink with N, a floor of about 0.0012 if the rest of r at N = 4,096 is the expected 0.0009. If so, the floor is a
systematic error of the construction, not of the scale: an inconsistent construction has a systematic of its own,
which more readings do not remove. Run 2 tests that.

### Run 2: predictions (12 October, written before `runs/stc/stc2.py` exists)

Same figure, readers, outside length and rung as run 1 (seed 12 again, so the figure is the same).
- **P5. Run 1's floor is the line estimator's own bias.** With run 1's estimator:
  - at N = 4,096 the per-landmark bias, the mean over trials of e_m − c, has rms across landmarks of at least 0.0008,
    and at N = 1,024 it is the same within 20% (it does not shrink with N);
  - halving the bearing noise to σ_θ = 5 × 10⁻⁴ cuts that rms by a factor between 3 and 5 (errors in the variables
    bias as σ_θ²).
  - **Killed if** any of these fails.
- **P6. A consistent construction removes it.** Placing each landmark by maximum likelihood on its bearings (five
  Gauss–Newton steps on the angular residuals, from run 1's estimate):
  - the trial-averaged shape error r falls as N^(−½): slope over the five N in [−0.55, −0.45];
  - the per-landmark bias at N = 4,096 has rms at most 0.0003.
  - **Killed if** either fails.
- **P7. The scale is untouched by the fix.** With the maximum-likelihood construction, P2 and P4 hold as stated for
  run 1 (sd of c within 10% of 0.01 for N ≥ 256 and falling < 10% from 64 to 4,096; the far rung within 10% of 0.0150
  at both n_far, correlation within 0.1 of 0.667).
  - **Killed if** any of these fails.

### Run 2 (12 October, `runs/stc/stc2.py`)

Seed 12, 2,000 trials at each setting, seventy-three seconds.

**The maximum-likelihood construction:**

| N | shape error r | sd of the common shift c | per-landmark bias rms |
|---|---|---|---|
| 16 | 0.01316 | 0.01050 | 0.00032 |
| 64 | 0.00681 | 0.01009 | 0.00019 |
| 256 | 0.00347 | 0.01009 | 0.00006 |
| 1,024 | 0.00174 | 0.00986 | 0.00004 |
| 4,096 | 0.00087 | 0.01009 | 0.00001 |

| | prediction | result | |
|---|---|---|---|
| P5 | the line estimator's per-landmark bias ≥ 0.0008 at N = 4,096, the same within 20% at 1,024; a factor 3 to 5 smaller at half the noise | 0.00127 and 0.00125 (ratio 0.987); 0.00032 at half the noise, a factor 4.01 | not killed |
| P6 | maximum likelihood: slope in [−0.55, −0.45]; bias ≤ 0.0003 at N = 4,096 | slope −0.491; bias 0.00001 | not killed |
| P7 | the scale untouched: P2 and P4 as in run 1 | sd of c 0.01009, 0.00986, 0.01009 for N ≥ 256, ratio 0.999 from 64 to 4,096; far rung 0.01575 and 0.01509 against 0.01500; correlation 0.677 | not killed |

**Reading.**
- **The figure improves with readings, if the construction is consistent.** Run 1's floor was the line estimator's own
  bias: flat in N (0.00125, 0.00127) and four times smaller at half the noise, as errors in the variables predict. With
  maximum likelihood the shape error halves with every fourfold N, from 0.013 at 16 readers to 0.0009 at 4,096.
- **The scale does not improve with readings.** In both runs, from 16 readers to 4,096, the common shift stays at the
  outside length's 1%, while the shape error falls fifteenfold.
- **The error becomes one shift.** At 4,096 readers the landmarks' errors are 99% correlated: what is left of the error is
  the outside amount's, shared by every landmark as one shift in levels.
- **A ladder carries its calibration up.** The far rung's error is the rung below's shift plus its own calibration,
  √(0.01² + 0.0112²) = 0.0150, whether a hundred far members are measured or ten thousand; it correlates 0.67 to 0.68
  with the shift below, as predicted.
- **Two kinds of systematic error.** The scale's, which no number of readings removes and only a better outside amount
  improves; and the construction's own (run 1), which a consistent estimator removes. The second is not the
  framework's; it is a warning that "the addresses average down" holds for a consistent construction only.
- **All of this is known** in metrology and astronomy: calibration error does not average down and propagates up the
  ladder; least squares on noisy lines is biased. What STC adds is the reading: the figure is the addresses' and improves
  with readings, the scale is the payload's and is exactly as good as the one amount from outside.
