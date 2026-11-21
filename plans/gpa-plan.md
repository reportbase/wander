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

### Run 1 (21 Nov 2026)

`python3 runs/gpa/gpa.py` (about 3 minutes); output `runs/gpa/gpa-results.json`. 40 blocks, 9,920 queries a head.

- **G0 not killed** (the check): in every head the front keys' weight share is at least their count share.
- **G1 killed:** the median head's back share is 64% (mean 63%), by layer 42–78%. But 98% of keys have q·k ≤ 0 by count,
  so the measure says little: in GPT-2 the raw sign of q·k is set mostly by a shared offset between queries and keys,
  and softmax is unchanged by adding one constant to all of a query's logits. My set-up: the sign of q·k is not a facing
  softmax sees.
- **G2 not killed:** the median head's key participation ratio is 3.1 of 64 (queries 4.7; by layer 2.0–7.3). See the
  post hoc note: much of this is the shared offset.
- **G3 killed:** no knee. The log–log slope is −0.88 over d = 1 … 8 and −0.82 over 16 … 128: attention (key 0 left out)
  falls with distance at one rate, about d^(−0.85), unlike the text's own links in LNK (about −1.5, then −0.3).
- **G4 not killed:** the median head puts 48% of its weight on key 0 (by layer 1% in layer 0 rising to 64% in layer 7).

**Post hoc, not predictions** (`runs/gpa/gpa_posthoc.py`, 20 blocks; `runs/gpa/gpa-posthoc.json`; both choices made
after seeing run 1):
- With each query's logits centred on their mean over its keys, about half the keys lie below (median 53%), and they
  get 5.2% of the weight (median head; by layer 2–14%, highest in layers 0–1). Read so, nearly all of a head's weight
  falls on one half of what it could read, measured from the head's own zero, not from the origin.
- With the keys centred, the median participation ratio is 12.1 of 64 (2.5 to 27 by layer, lowest in layers 2–4): the
  3.1 of run 1 was mostly one shared direction. Few dimensions, but not three.

**Reading, after the run, not a test.** Softmax has no standpoint of its own: the sign of q·k is not something it reads,
since it depends on logits only up to a constant per query (consistent with R1046: softmax the DHV's form, no facing).
What a trained model does build is a facing of its own, relative to each query's mean: almost all weight on the keys
above it. Its keys use about a fifth of their 64 dimensions once the shared offset is removed, and almost half its weight
goes to the first token, which no direction asks for. Its weight falls with distance at one rate, not with the text's
knee. One model, one text.
