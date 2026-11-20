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
