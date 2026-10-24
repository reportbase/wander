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

**Before run 1 (the cut the plan allowed).** Five timed steps took 3.4 s (softmax) and 2.4 s (Cauchy, K = 163) a step,
and an evaluation 52 s; 1,500 steps a run would be about 30 hours for 24 runs. S is cut to **400 steps** a run (6,400
blocks, 1.6 million token positions, two thirds of one pass over WikiText-2's 2.43 million training tokens; validation
257,233 tokens, 1,004 blocks), about 20 minutes a run, 8 hours in all; the warm-up stays at 100 and the decay runs to
step 400. These models are far from trained (the script's ran one pass over about 60,000 steps); a difference between
horizons that only appears with training would not be seen here, and C1's "within noise" is then weak evidence.
Nothing else changes.

**What is run, and what is not** (Tom, after the plan: "is this test still worth running. what will it prove?", then
"yes, proceed" to my answer). The sweep (C1–C4, C7) is not run: the framework makes no prediction about a horizon over
token positions, so neither outcome would bear on it (the reading above), and the February result is not in hand to
check. Only the Circle probe's purity (C5, C6) is run, since it is the one place the script claims one of the framework's
numbers. Its models: softmax and Cauchy K = 163, seed 42, the scale above (400 steps). The probe is the script's
`probe_circle_attention` copied, changed only to take a cap on the training triples (20,000, as C6 says; the script reads
every offset of 200 batches, about 1.6 million overlapping triples) and to return the purity before the retrofit (the
script returns the product under the name `purity_before`). Random embeddings: Gaussian, the trained embeddings' own
standard deviation, put in the Cauchy model's place.

**The paper behind the script** (Tom, before the probe's run: "here is an old session paper that describes the
script"; *2/π: The Universal Semantic Horizon in Representation Learning*, Tom Brinkman, tangent.fit, December 2025,
not committed). It does not describe the horizon sweep or the Circle probe (they came in February); it is where their
2/π comes from: ψ₁ = 2/π, "the S¹ access bound", read as a threshold on cosine similarity ("Above ψ₁, concepts share
semantic direction"), with ψ₂ = (2/π)·ln 2 an admission threshold. Read through the framework, before the probe runs:

- Its derivation, E|cos θ| = (2/π)∫₀^{π/2} cos θ dθ = 2/π for θ uniform on the quarter turn, is OFS's 2/π: the mean
  projection over a uniform turn, the circle's. It is a **mean**, not a boundary. The uniform turn's boundary, the place
  that splits it in half, is the corner: θ = 45°, cos θ = 1/√2 = 0.7071 (OFS §4). A threshold read off a law's mean is
  not where the law divides.
- Its Lemma ("the expected absolute projection of a random uniform direction onto any fixed axis equals 2/π", "a
  geometric necessity of high-dimensional projection") holds only in two dimensions. For a direction uniform on the
  sphere in d dimensions E|cos θ| = Γ(d/2)/(√π·Γ((d + 1)/2)), checked here to 20 digits: d = 2 gives 0.63662 (2/π),
  d = 3 gives ½ (Archimedes), d = 8 0.2910, d = 384 0.04074, d = 768 0.02880, falling as √(2/(πd)). In the embedding
  dimensions it cites (100–768) random directions sit near 0.03–0.08, not 2/π; this is the hemisphere's √π·Γ((n + 1)/2)/Γ(n/2)
  of SIT run 1, read the other way. So 2/π is the circle's number, and in a space of many directions it is not the
  number a uniform direction gives.
- Its synthetic check (noise raised "until mean cosine similarity matches 2/π") would match any target; its measured
  means range from 0.76 to 1.08 of 2/π across word models, 0.34 within topic for sentences, and CLIP's best threshold is
  0.74, which it reports itself ("the constant depends on training objective").
- What carries forward is not the constant but two of its "prizes", which OFS now states with their conditions: a reader's
  count of addresses K is apart from the world's N ("When N changes, you don't notice"; OFS §8, "A fixed count, aimed by
  H", and the Cauchy keeping K apart from N), and readings are scale-free (Theorem 6(a)). Its S¹ and S² (the line called
  S²) are not the standard spheres.

This changes no prediction: the plan's reading of the script's 2/π already stood on the first two points.

### Run 1 (23 October 2026)

`python3 runs/cah/cah.py` (the two models only, as above), then `python3 runs/cah/probe.py`; outputs
`runs/cah/cah-results.json`, `runs/cah/cah-probe.json`. Checkpoints kept outside the repo.

**The models.** Cauchy K = 163: validation loss 5.0472, perplexity 155.6 (12.0 min). Softmax: 5.0510, 156.2 (11.0 min).
One seed each, 400 steps; the two are level at this scale, which the sweep would not have resolved (C3 is not tested by
one seed; recorded only).

**C5, purity before the retrofit** (the script's projection, cells π/4, D = 4, 6, 8; 20,000 training triples):

| D | Cauchy K = 163 | softmax | random | occupied cells (of 5^D) |
|---|---|---|---|---|
| 4 | 0.1249 | 0.1198 | 0.1287 | 16, 16, 16 |
| 6 | 0.1727 | 0.1708 | 0.1566 | 64, 64, 64 |
| 8 | 0.3688 | 0.3715 | 0.2325 | 236, 237, 256 |

C5 is **not killed** by its kill condition: the Cauchy model's purity is nowhere near 2/π (0.12–0.37) at any D. Its
body was wrong in one clause, recorded as such: the trained purities move 0.24 across D, but the random one only 0.10,
and at D = 8 the random lands below the trained (0.23 against 0.37); its "same range" holds at D = 4 and 6 only. Post
hoc, the occupied cells explain the numbers: the projection starts with rows of norm 1.5 against embeddings of sd 0.069,
so W·x stays within ±0.33, θ = (π/2)(1 + tanh(W·x)) within [1.08, 2.02], and every angle lands in one of the two cells
either side of π/2: exactly 2^D cells are used, and the purity is the share of each of 2^D cells' commonest next token,
rising as D splits the triples finer (at D = 8 random embeddings fill all 256, trained ones 236, so the trained cells
hold more alike triples). The Cauchy kernel and softmax give the same purity to 0.005 at every D: nothing of the kernel
shows in it.

**C6, after the retrofit** (D = 6, five epochs): purity 0.5450 after one epoch, 0.5757 after five, "product" 0.9044;
**not killed** (0.061 from 2/π, and still rising with the epochs: a fitted statistic, which the InfoNCE moves toward
whatever the training reaches, not a value the geometry fixes). The script's own verdict line printed "CIRCLE
MATCHES/BEATS CAUCHY" (Circle 0.539 against the Cauchy model's 0.461 on the 141 of 500 held-out triples it committed to).
Post hoc, that comparison is not one: the script's triples come from the validation text read at every offset, so 200
batches of 32 give 1,632,000 triples of only 5,039 distinct ones (6,655 tokens of text); after the shuffle, 97% of the
500 held-out triples are among the 20,000 the cells were filled from (98.2% of their two-token contexts). The Circle's
cells are a lookup of answers it was shown; the Cauchy model is a 256-token language model given two tokens. The same
holds in the script at its own scale: its triples too are read at every offset of the first 200 batches.

**C7** is not tested (the sweep was not run).

### Where CAH stands

The script's 2/π has no footing in the framework, and where it can be measured here it is not found. In the horizon,
2/π is a fraction of a token count, with no turn to be the mean of. In the paper behind it, it is a mean read as a
boundary, and the circle's value used in hundreds of dimensions, where a uniform direction gives √(2/(πd)). In the Circle
probe, the purity is a count over 2^D cells, 0.12–0.37 before the retrofit, trained and random alike, and after it a
fitted value still climbing (0.58 at five epochs). The probe's "Circle beats Cauchy" reads held-out triples that were
97% in its own table. Tom's comment, on the paper: "so we fell into the same trap that we have now identified": 2/π is
the turn's (an address-side number, the uniform sweep's mean projection, there whatever is looked at) and was read as a
property of the payload, a constant of meaning, as linewidths were read as a system's own (`plans/rea/linewidth-note.md`).
The Cauchy kernel is that trap the other way: the address law's shape used as a weight on an amount, ‖q − k‖.

What carried forward from that work is not the constant but two of its prizes, now stated with their conditions in OFS:
K kept apart from N, and scale-free readings. A test of the framework in attention would put the Cauchy on a direction
(the angle between q and k, or the distance back laid on a reader's lay with its corner at H); not taken up.

**The February results** (Tom, after run 1, without comment: `attention_results.md`, 7 February 2026, "Projected
Attention: Complete Results & Next Steps"; not committed). Seven C++ programs: a viewport over per-dimension sorted key
indices (K nearest a dimension, the union weighted by the kernel), Cauchy and Gaussian kernels, keys "direct" or through a
random W_k. Its open question: "Does a trained Cauchy model produce attention patterns where effective keys stay bounded
as context grows? Or does Cauchy's nature mean effective keys always grow with N?"

*Prediction before a check* (from the kernel alone, no run yet): for keys spread with fixed density over a set of
dimension D′ about the query, the kernel's far weight is ∫ r^(D′−1)/(1 + r²/γ²) dr, which converges only for D′ < 2. So
with N keys the weight beyond any fixed radius grows as N^((D′−2)/D′) for D′ > 2 (as ln N at D′ = 2), the share held by
the nearest keys falls as its inverse, and the effective number of keys (Σw)²/Σw² grows without bound: at D′ = 32 nearly
in proportion to N. A Gaussian kernel's far weight converges in every dimension, so its effective keys stay bounded. So
the answer to the open question is the second, unless trained keys lie on a set of dimension below 2 about each query.
**CH1:** in a seeded check (keys Gaussian about the query at fixed density, N = 500 … 8,000, γ the median nearest-key
distance), the effective-key count's slope against N on log axes is within 0.1 of (D′ − 2)/D′ for D′ = 4 and 8, and
under 0.1 at D′ = 1 (bounded). Killed if not.

*CH1, the check* (`runs/cah/effkeys.py`, `effkeys.txt`; 20 repeats a point, γ = 1 at unit density). Slopes of the
effective-key count against N: Cauchy +0.012 at D′ = 1 (−0.012, bounded), +0.236 at 2, +0.904 at 4, +0.993 at 8;
Gaussian −0.015 at 4 and +0.726 at 8. **Killed**, by my arithmetic: I predicted the slope of the far *weight*, not of the
effective count (Σw)²/Σw², whose denominator also grows: Σw² = ∫ r^(D′−1)/(1 + r²)² dr converges only for D′ < 4. So the
count grows as N^(2(D′−2)/D′) for 2 < D′ < 4, as N/ln N at 4, in proportion to N past 4, and as (ln N)² at 2. The
Gaussian at D′ = 8 killed it by my set-up too: at unit density the ball's radius N^(1/8) (2.2 to 3.1) had not passed the
Gaussian's reach in eight dimensions (its mass peaks near √7 = 2.6), so it had not settled.

**CH1′** (written after the check, from the corrected count): Cauchy slope at D′ = 3 within 0.1 of 2/3; at 4 within 0.1
of 1 − 1/ln N̄ (0.88 at the run's middle N); at 8 within 0.05 of 1. Gaussian at D′ = 8 with N from 65,536 to 524,288 (ball
radius 4 to 5.2): slope under 0.1. Killed if any is not.

*CH1′, the run* (`runs/cah/effkeys2.py`, `effkeys2.txt`): Cauchy slopes 0.731 at D′ = 3 (predicted 0.667), 0.895 at 4
(0.868), 0.993 at 8 (1); the Gaussian at D′ = 8 settled at about 6,000 effective keys, slope 0.039. **Not killed.**

**The February results, read** (the document's own numbers):
- The answer to its open question is the second: with keys spread over a set of dimension above 2 about the query, the
  Cauchy kernel's effective keys grow without bound, in proportion to N past 4 dimensions. Its own table (121, 308, 623,
  2,037 effective keys at N = 500 … 5,000, slope 1.21 on log axes, a little steeper than N) is the D′ > 4 case. A trained W_k could only hold the count by putting
  each query's keys on a set of dimension below 2; the Gaussian holds it at any dimension once N outreaches the kernel.
- "Candidates plateau … O(K·D) confirmed": the union of K nearest in each of D sorted lists holds at most K·D keys by
  construction, so its plateau is the index's bound, not a finding about the kernel ("the viewport mechanism is
  kernel-independent", as it says). What a viewport costs is the weight left outside it, which for the Cauchy grows with N
  as above (its 62% captured at N = 5,000 and the falling top-1 down the scale table).
- "Cauchy is stable under linear projection": a sum of independent Cauchys is a Cauchy (Lévy's stable laws), classical.
  The kurtoses quoted (39–503) are of samples from a law with no variance, so they measure the sample, not the law.
- The framework's reading: here the Cauchy is a law on amounts twice over, on the keys' coordinates and as a weight on a
  distance, and its tail, which on a turn ends at the horizon of a closed arc, becomes unbounded far weight in D′
  dimensions. 2/π appears nowhere in these tests ("Cauchy (2/π) is not invalidated" tests nothing about 2/π).
