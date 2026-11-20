# NAT: nature's read against the high-dimensional way

20 Nov 2026. SPN R1141. Tom: "The natural world figured this out long ago, let's follow its lead, see if it helps, it's a
result either way. Mostly, I think the natural world is organized for real time, cost free, simple geometry, not the
highly dimensional way ai is organized now. Regardless, we learn more about the claims of our read writes paper."
After RAT and SCT (R1138–R1140); no expensive training (R1139): one exact part and one small learner, minutes on a CPU.

## What "nature's lead" is taken to mean

A read as an eye has it: three dimensions (two slopes from the look), a standpoint (the look), one hemisphere (the
front), the geometry given (no parameter learned for it), a thumb H (R226). The high-dimensional way: many dimensions,
directions and sizes mixed in a learned embedding, weights by an exponential of a dot product (softmax, the DHV's form,
R1046). Two claims of *Reads and Writes* are put at risk:
- **the heat** (§3, §7; R728): from a standpoint the Cauchy keeps half its heat inside the corner. Claimed for the plane
  and space; what happens as the dimension grows is not said in the paper;
- **the read needs no N and no size** (R935, R1039): given, not learned, it should need no training and be unmoved by
  sizes and by how many things there are.

## Part A (exact, no training): the horizon in n dimensions

Directions uniform over the front hemisphere of n dimensions (n − 1 slopes from the look). α the angle off the look
(the writer's name), s = tan α the read's slope; density of α ∝ sin^(n−2) α on [0, π/2]; s² is (n − 1) times an
F(n − 1, 1) variable.

- **A1.** The share inside the corner (s ≤ 1): ½ at n = 2, 1 − 1/√2 at n = 3, strictly falling with n, under 1% by n = 16.
  Killed if any clause fails.
- **A2.** The median slope: 1 at n = 2, √3 at n = 3; the median over √(n − 1) tends to 1/Φ⁻¹(¾) = 1.4826 (the normal's
  median absolute deviation constant), within 2% at n = 64. Killed if any clause fails.
- **A3.** The corner as the median holds only at n = 2: at n ≥ 3 the median slope exceeds 1. (Follows from A2; stated
  so the reading can be checked.)
- **A4.** The √d. With q and k uniform directions in n dimensions, cos α has standard deviation 1/√n exactly; times √n,
  1. So softmax's 1/√d (Vaswani et al. 2017) is the high-dimensional way's correction for every key sitting near the
  horizon. Killed if the sd differs from 1/√n by more than 10⁻⁹ (exact moment).

## Part B (a small learner): the eye's task

A viewer at the origin; 32 things around it, directions uniform on the whole sphere (half behind the look), distances
log-uniform over [1, 100] (writes, sizes with no bearing on the answer); a look q uniform. Each thing carries a value (a
random 16-vector). The answer: the value of the thing nearest the look (largest cosine; it lies in front with
probability 1 − 2⁻³²). Output the weighted sum of values; trained by squared error; accuracy is the arg-max of the weights
on 20,000 test cases.

Arms:
- **nature**: the read, front, on the raw 3D position from the look, H = 1, **no parameters, no training**;
- **read-3**: the read, front, after learned 3 × 3 maps W_q, W_k and a learned H;
- **softmax-3**: softmax(β·(W_q q)·(W_k k)), 3 × 3 maps;
- **softmax-mlp**: the high-dimensional way: q and k each through a learned embedding 3 → 64 → 64 (ReLU, with biases),
  then 64 × 64 W_q, W_k and softmax;
- **read-mlp**: the same embedding, then the read, front, in 64 dimensions.
Adam, 3,000 steps, batch 256, learning rate 3·10⁻³, three seeds (0–2); accuracy also checked every 250 steps.
Tests: the training world; the world scaled by 10³ and by 10⁻³ (every distance); and 1,024 things in place of 32.

Known by construction (a check, not a prediction): nature's arg-max *is* the nearest direction in front, so its
accuracy is 100% on every test with no training. What the run adds is how far the learned and high-dimensional arms get.

- **B1 (check).** Nature 100% on all four tests.
- **B2 (uniform scale, exact).** softmax-3 and read-3 give the same predictions case by case when the world is scaled by
  10³ or 10⁻³ (softmax's logits all scale by k > 0, the arg-max cannot move; the read's slopes do not move). Killed if any
  case differs.
- **B3 (the embedding breaks the scale test).** softmax-mlp's accuracy in the world scaled by 10³ is at least 20 points
  below its accuracy in the training world (biases and ReLUs are not homogeneous). Killed if it falls by less.
- **B4 (spread of sizes).** In the training world softmax-3 is at least 20 points below nature (a dot product cannot undo
  sizes spread over a factor 100, as SCT found over 2.7). Killed if it is within 20.
- **B5 (more things than trained).** With 1,024 things, softmax-mlp is at least 20 points below nature. Killed if within 20.
- **B6 (learned geometry, cost).** At 3,000 steps the best learned arm in the training world is still at least 2 points
  below nature's 100%. Killed if any learned arm reaches 98%.

A killed prediction stays killed; a fix is a new run with its own prediction.

## Runs

### Run 1 (20 Nov 2026)

`python3 runs/nat/nat.py` (about 4 minutes on four threads); output `runs/nat/nat-results.json`.

**Part A, exact.** The front hemisphere's share inside the corner and the median slope, by dimension n:

| n | 2 | 3 | 4 | 8 | 16 | 32 | 64 |
|---|---|---|---|---|---|---|---|
| share inside the corner | 0.5 | 0.2929 | 0.1817 | 0.0332 | 0.0015 | 4.2·10⁻⁶ | 4.6·10⁻¹¹ |
| median slope | 1 | 1.732 | 2.264 | 3.720 | 5.603 | 8.158 | 11.70 |
| median / √(n − 1) | 1 | 1.225 | 1.307 | 1.406 | 1.447 | 1.465 | 1.474 |

- **A1 not killed**, **A2 not killed** (1.4740 against 1.4826 at n = 64, 0.6% off), **A3 not killed**, **A4 not killed**
  (sd of cos α times √n = 1 at every n).

**Part B.** Mean accuracy over three seeds (chance 1/32 = 3.1%):

| arm | parameters | training world | world × 10³ | world × 10⁻³ | 1,024 things |
|---|---|---|---|---|---|
| nature | 0 | 100% | 100% | 100% | 100% |
| read-3 | 19 | 96.6% | 96.6% | 96.6% | 81.1% |
| softmax-mlp | 17,025 | 66.7% | 58.7% | 17.4% | 17.5% |
| softmax-3 | 19 | 17.4% | 17.4% | 17.4% | 2.7% |
| read-mlp | 17,025 | 3.2% | 3.2% | 3.2% | 0.1% |

- **B1 not killed** (the check).
- **B2 not killed:** softmax-3 and read-3 the same case by case under ×10³ and ×10⁻³.
- **B3 killed:** softmax-mlp fell 8.0 points under ×10³ (bound 20). It fell 49.3 points under ×10⁻³: the embedding
  breaks the scale test, but on the side I did not predict.
- **B4 not killed:** softmax-3 82.6 points below nature.
- **B5 not killed:** softmax-mlp 82.5 points below nature with 1,024 things.
- **B6 not killed:** the best learned arm (read-3) 96.6%.
- **read-mlp failed to train** (constant from step 250, the same at every test, near 1/32). Post hoc, untested: the
  guard 10⁻³⁰⁰ is 0 in float32, so its weights may have collapsed to zero, every arg-max the first key. My code, not a
  result about the arm; a fix is a new run with its own prediction.

**Reading, after the run, not a test.** Part A is classical (the concentration of measure; Vaswani's 1/√d), the sorting
ours: the Cauchy's corner as the median of a read is the plane's alone; in space half lies within √3 (R700); as the
dimension grows nearly every direction sits at the horizon (inside the corner 0.15% at 16 dimensions, 5·10⁻¹¹ at 64),
which is what softmax's 1/√d rescales. The read's heat gives the front its structure only in few dimensions. In part B
the geometry given (no parameter, no training) answered every test; nineteen learned parameters in its form reached 97%
and were unmoved by scale; the high-dimensional embedding, with 900 times the parameters, reached 67%, lost most of it
when the world shrank and when the things grew in number. The task is the read's own, built so (as SCT's); it shows what
the given geometry does without cost, not a general advantage over learned attention.
