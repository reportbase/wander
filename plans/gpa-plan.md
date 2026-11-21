# GPA: reading a trained model's attention, no training

21 Nov 2026. SPN R1149. Tom: "Is there any promising ideas about Ai that we should explore", then "1" (read a real trained
model with no training: the weight behind the query, the keys' effective dimension, attention against distance). Under
R1139 (no training runs; point the geometry at AI) and after RAT, SCT, NAT and LNK (R1138–R1148).

## What is measured

GPT-2 small (OpenAI 2019; Hugging Face `gpt2`, `model.safetensors` sha256
248dfc3911869ec493c76e65bf2fcf7f615828b0254c12b473182f0f81d3a707; MIT licence; not committed), 12 layers × 12 heads,
64 dimensions a head, run forward only (no gradient) on WikiText-2's validation split (cached since CAH), 40
non-overlapping blocks of 256 tokens. For every head, the query and key vectors after their projections (biases
included, as the model uses them), and the model's own attention weights.

**The first key.** GPT-2 is known to pour much of its weight onto the block's first token (an "attention sink", Xiao et
al. 2023, from memory). That weight carries no direction from the query, so the measures below leave key 0 out and
renormalise over the rest; the sink's own share is reported beside them. Queries with fewer than 8 earlier keys are left
out.

- **Back share.** For a query, the share of its (renormalised) weight on keys with q·k ≤ 0: keys behind the query's
  standpoint, what one facing does not read (R1138, RAT A4: 24% in our own small model).
- **Effective dimension.** Per head, the participation ratio (Σλ)²/Σλ² of the keys' second-moment matrix (uncentred:
  directions are read from the origin), out of 64; and the same for the queries.
- **Weight against distance.** The weight a query puts on the key d positions back, averaged over queries, heads and
  blocks (key 0 left out), for d = 1 … 128.

## Predictions (committed before the script is written)

- **G0 (a check, arithmetic).** In every head, the front keys' share of the weight is at least their share of the count
  (softmax is increasing in q·k, and every front key has a larger q·k than every back key). Killed if any head fails
  (beyond 10⁻⁶).
- **G1 (one facing, mostly).** The median head's back share is under 10%. Killed if 10% or more.
- **G2 (few dimensions; nature's lead, R1141).** The median head's key participation ratio is 8 or less (of 64). Killed if
  more.
- **G3 (the knee; LNK, R1148).** In the head-averaged weight against distance, the log–log slope over d = 1 … 8 is steeper
  than over d = 16 … 128 by at least 0.5. Killed if by less.
- **G4 (the sink is no read).** The median head puts at least 30% of its weight on key 0. Killed if less. (Known
  beforehand in kind, from memory; the number is a guess.)

One model, one text, inference only: evidence about GPT-2 small on this text. A killed prediction stays killed; a fix is a
new run with its own prediction.

## Runs
