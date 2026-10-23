# CAH: Cauchy attention's horizon, read through the address and the payload

*23 October 2026, SPN R469. Tom, of LGO's script: "Wrong script. this is the one." The test is
`cauchy_horizon_sweep_2.py` (Tom Brinkman and Claude, February 2026, sha256
`a75f629d7eb2883d9f46e49cb701e15a9d110f909a0fb729185f904949de88f1`; not committed, Tom's file). Its pre-registered
hypothesis: "The Cauchy kernel 1/(1+d²) with bounded horizon K = ⌊(2/π) × N⌋ minimizes perplexity among all tested K
values, and matches or beats softmax attention on the same architecture." Earlier, Tom: "lets complete those tests,
through the lense of our mathmatical framework … I would prefer to revisit the ideas from scratch." The old session logs
were not read, and the old run's results are not known to me. LGO (`plans/lgo-plan.md`) ran on the script given first;
its results stand as a real-data check of its own, but it was not this test.*

*No real data is at stake here: a language model trained on text, judged by its own held-out loss. The run is ours, on a
CPU, at a reduced scale, stated below before the run. A result at this scale is evidence about this scale.*

## The script, as it stands

- A GPT-style model (4 layers, 8 heads, 384 wide, block N = 256, GPT-2's tokenizer, weight tying), trained one epoch on
  WikiText-103's first 15,000 lines, AdamW 3·10⁻⁴, 100 warm-up steps, then linear decay to 0.1; three seeds (42, 137,
  2024).
- **The Cauchy attention:** weight(q, k) = 1/(1 + ‖q − k‖²/γ²), a learnable γ² per head, zero outside the last K positions
  (a hard causal window), divided by the row's sum. **The baseline:** softmax(q·k/√d) over every earlier position.
- **The sweep:** K ∈ {96, 128, 148, 163, 180, 210, 256}; 163 = round((2/π)·256) is the prediction.
- **The probes:** a needle (" The secret code is BANANA") at depths 0.1–0.9; loss by quartile of position; copying a
  pattern from 10 to 240 back; and "Circle attention", a 6 × 768 projection of two tokens' embeddings to six angles in
  [0, π] (`(π/2)(1 + tanh(W·x))`), cut into cells of π/4, trained 20 epochs by InfoNCE, its "purity" (each cell's share of
  its commonest next token, averaged over occupied cells) predicted to approach 2/π and "the product" purity × π/2 to
  approach 1.

## Known beforehand

- **Classical, the kernel:** 1/(1 + d²/γ²) is the Cauchy (Student t with one degree of freedom) profile used as a
  similarity of two amounts, as t-SNE uses it for low-dimensional affinities (van der Maaten and Hinton 2008), and
  attention built on a distance instead of a dot product is known (the L2 attention of Kim, Papamakarios and Mnih 2021,
  made for its Lipschitz bound). A heavy-tailed kernel keeps far keys a share of the weight a Gaussian kernel or a sharp
  softmax would not.
- **Classical, the window:** a sliding causal window of K (Longformer and its kin) limits a layer's reach, not the
  network's: L layers reach L·(K − 1) back. With N = 256 and K ≥ 96, every position of a block can still reach its
  start through four layers. A window only differs from full attention at positions t ≥ K; for t < K the mask is the
  causal mask.
- **OFS:** a Cauchy variable is a direction, never an amount; find the turn, find the amount (§7.2). 2/π is a ratio of
  two sums over the uniform turn, the mean projection, taken by whoever adds the projections; the corner, the turn's
  median, is at v/h = 1, half the quarter turn (§3.4, §4). π/2 · 2/π = 1 is one turn read from its two pivots, central and
  inscribed, the product returning H in H (§4, §10). An edge takes the Cauchy's tails ("What breaks it"). H is the
  reader's zoom, the amount at which s = d/H = 1.
- **draw's labs:** nothing on attention. Checked before planning, per CLAUDE.md, by the lab list's names; none touches
  learned kernels.

## The reading, before the run

**The kernel is over an amount.** ‖q − k‖ is a length in the head's space, an amount. 1/(1 + s²) with s = ‖q − k‖/γ is
the Cauchy's *shape*, used as a weight on that amount; there is no turn behind it, and none of OFS's address results (the
median at the corner, the missing mean, Theorem 6's order surviving every payload) is about it. What the framework does
name in it is γ: the head's H, the amount at which the weight falls to ½ (s = 1, the kernel's corner). A learnable γ per
head is each head choosing its zoom. This is a reading; it predicts nothing about perplexity.

**2/π is not a fraction of a count.** In OFS 2/π is the mean of the projection over a uniform turn. A context of N tokens
is not a turn and a horizon K is not a projection: nothing in the geometry makes the fraction K/N = 2/π special, and the
framework's own scale test says so: a fraction that belonged to the geometry would be the same fraction of any N, and
would have to come with a turn that sets it. If anything in the framework were borrowed, the corner (½, the median) would
be the natural candidate, not the mean, and the framework does not ask for that either.

**The window is an edge.** A hard mask at K cuts the kernel's tail, the part that makes a Cauchy kernel differ from a
Gaussian one; so the window works against the very property the kernel was chosen for.

**The Circle probe's 2/π borrows the identity.** Its purity is a share of a cell's commonest token, averaged over the
cells that are occupied. Its value is set by how many triples fall in each cell (a cell holding one triple has purity 1),
so by D, the cell's width and the data; nothing in it is a turn's mean projection. "The product → 1" is purity → 2/π
restated, not π/2 · 2/π = 1, which is two readings of one turn, never a share times π/2.

Where would the framework put a Cauchy in attention? On a direction: the angle between q and k (attention that reads
cos(q, k) and divides out ‖q‖‖k‖ is reading a direction), or a position laid on the turn (a reader's lay of the distance
back, the corner at H). Neither is in the script, and neither is tested here.

## The scale of the run

The script's own scale (≈ 1 million tokens of training text, read at every offset, about 60,000 steps a run, 24 runs) is
weeks on this sandbox's four CPU cores. Run 1 keeps everything but the size, fixed now:

- 4 layers, 4 heads, 128 wide (head width 32, as the script's 384/8 is 48: near), block N = 256, GPT-2's tokenizer;
  dropout 0.1, AdamW 3·10⁻³ (a small model, so ten times the script's), weight decay 0.1, 100 warm-up steps, then the
  script's linear decay to 0.1, batch 16, clip 1.0.
- WikiText-2 (`Salesforce/wikitext`, `wikitext-2-v1`, its whole train split; the script's own last fallback), blocks drawn
  at random offsets, S = 1,500 steps a run (24,000 blocks, about 6 million token positions, about 3 passes over its 2
  million tokens). If a step takes so long that 24 runs exceed about 8 hours, S is cut before the first run and recorded
  here; nothing is cut after.
- Evaluation: the validation split cut into non-overlapping blocks of 256 (the script reads every offset, which counts
  most tokens 256 times), the mean cross-entropy over all of them, perplexity its exponential; and the same by position
  within the block.
- Configs as the script's: softmax, and Cauchy at K ∈ {96, 128, 148, 163, 180, 210, 256}; seeds 42, 137, 2024. The
  attention modules are the script's, copied unchanged.

## Predictions

**C1, no fraction is special.** Over K, the mean validation loss is non-increasing in K within noise: for every pair
K₁ < K₂, loss(K₂) ≤ loss(K₁) + 2·se (se the standard error of the difference of the two means over seeds). Killed if
K = 163 beats each of 148, 180 and 256 by more than 2·se.

**C2, the window acts only past itself.** The loss gap between K = 96 and K = 256, measured on positions t < 96, is under
a third of the gap on positions t ≥ 163 (both as K = 96 minus K = 256, means over seeds). Killed if not (if the gap is
spread evenly over positions, the window acts through training, not through what each position can see).

**C3, the kernel, classical.** Cauchy at K = 256 and softmax within 10% in perplexity; no claim for which is lower. A
classical expectation, not the framework's; recorded so a surprise is seen.

**C4, each head's zoom.** The learned γ² differ across heads and layers by more than a factor of 2 within at least one
layer, in every seed. A reading of γ as H; killed if every head lands within a factor of 2 of every other in its layer.

**C5, purity is a cell count.** The Circle probe's purity, computed by the script's own code without the retrofit, on
(i) the Cauchy K = 163 model's embeddings, (ii) the softmax model's, (iii) Gaussian random embeddings of the same size,
at D = 4, 6 and 8: it moves by more than 0.2 across D in each case, and random embeddings land in the same range as
trained ones. Killed if the trained Cauchy model's purity is within 0.02 of 2/π at all three D while the softmax and
random ones are not.

**C6, after the retrofit.** Running the script's InfoNCE retrofit at D = 6 (5 epochs, not 20, on 20,000 training triples,
since it is pure Python) on the Cauchy K = 163 model's embeddings, the purity is not within 0.02 of 2/π. Killed if it is.
(A purity can land near 0.64 for many reasons; one landing would not show the geometry, but it would kill this.)

**C7, the verdict.** The script's hypothesis, that K = ⌊(2/π)N⌋ minimizes perplexity, is not supported at this scale:
not killed unless C1 is.

## Runs
