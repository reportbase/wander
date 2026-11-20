# SCT: the scale test, run on a small learner

20 Nov 2026. SPN R1140. Tom: "We should be able to train small models to make a geometric point. Our is that not
possible?", then "Yes" to the first of three toys. After RAT (`plans/rat-plan.md`) and R1139 (no expensive training;
explore by the geometry): a task built so that one geometric point is the only thing that matters, trained in seconds.

## The point

A read is a direction with no size (R1039); a write has a size (R1138: whole, no hemisphere). The scale test (R568):
scale the world and a read does not move, a write does. Here the keys' sizes are writes with no bearing on the answer,
and at test time their range is widened: the world scaled, key by key.

## The task

A query and 32 keys in 16 dimensions. Directions uniform on the sphere (seeded). Each key's length e^U, U uniform on
(−a, a); the query's length likewise. Each key carries a value, a random vector in 16 dimensions. The answer is the value
of the key whose direction is nearest the query's (largest cosine). Train at a = 0.5 (lengths within a factor 2.7);
test at a = 0.5, 1.5 and 3 (factors 2.7, 20, 403).

The learner: learned linear maps W_q, W_k (16 × 16) and one learned scale, then weights over the 32 keys, the output the
weighted sum of the values, trained by squared error to the answer's value. Four arms, as RAT's:
- **softmax**: softmax(β·(W_q q)·(W_k k));
- **Cauchy on an amount**: 1/(1 + ‖W_q q − W_k k‖²/γ²), normalized;
- **read, front**: the Cauchy heat on the slope of W_k k read from W_q q, h²/(h² + v²/H²), keys with h ≤ 0 weighed 0;
- **read, both**: the same with h of either sign.
Adam, 4,000 steps, batch 256, learning rate 3·10⁻³; five seeds (0–4). Accuracy: the key given most weight is the answer;
over 20,000 test cases per range.

Known beforehand: RAT's A1 (the read's weights unmoved by any key's or the query's length, exact); with W_k linear,
scaling a key scales W_k k, so the read's weights, and its accuracy, are the same at every a for a trained model. That
part is arithmetic. What the learner adds is whether softmax and the amount-Cauchy learn to ignore length when length
varies in training, and how they fail when it varies more.

## Predictions (committed before the script is written)

- **S1 (exact).** For each read arm, the accuracy at a = 1.5 and at a = 3 equals that at a = 0.5 (the same test
  directions; lengths redrawn), the test predictions identical case by case. Killed if any case's prediction differs.
- **S2.** Softmax's mean accuracy over five seeds falls by at least 10 percentage points from a = 0.5 to a = 3. Killed if
  it falls by less.
- **S3.** The amount-Cauchy's mean accuracy falls by at least 10 points from a = 0.5 to a = 3. Killed if less.
- **S4 (competes at the training range).** At a = 0.5, read, front's mean accuracy is within 5 points of softmax's,
  either side. Killed if more than 5 points below.

A killed prediction stays killed; a fix is a new run with its own prediction.

## Runs

### Run 1 (20 Nov 2026)

`python3 runs/sct/sct.py` (3 min 42 s on four threads); output `runs/sct/sct-results.json`. Mean accuracy over five
seeds, 20,000 test cases a range (chance 1/32 = 3.1%):

| arm | a = 0.5 (trained) | a = 1.5 | a = 3 |
|---|---|---|---|
| read, front | 92.1% | 92.1% | 92.1% |
| softmax | 52.6% | 28.9% | 20.4% |
| Cauchy on an amount | 49.5% | 38.6% | 28.9% |
| read, both | 47.2% | 47.2% | 47.2% |

- **S1 not killed:** both reads gave the same prediction case by case at every range, every seed.
- **S2 not killed:** softmax fell 32.1 points from a = 0.5 to a = 3.
- **S3 not killed:** the amount-Cauchy fell 20.5 points.
- **S4 not killed:** read, front 39.6 points *above* softmax at the training range (the prediction allowed it to be up to
  5 below).

**Reading, after the run, not a test.** The task is built so that direction alone decides the answer and size is a
write with no bearing on it; it shows the scale test on a learner, not a general advantage. Even within the training
range (lengths within a factor 2.7), softmax and the amount-Cauchy learned the task only about half as well as the
front read in 4,000 steps, and widening the range cut them further; the reads did not move. Read, both sits near half
(47%) for a geometric reason: joining the back side makes a key and its opposite read alike, and of 32 random keys in 16
dimensions the most opposed is about as often more extreme than the most aligned (R1138: a key is whole; one facing reads
the half that answers here, the join confuses the two). In RAT's language model the join helped; here, where the answer
lies in front by construction, it halves the score.
