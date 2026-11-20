# RAT: attention as a read

20 Nov 2026. SPN R1138. Tom: "Ai uses trig to read, which means it is looking at the back side."; "We've tested this
before, and the results were in favor of cauchy. Let's revisit this idea again, using what we have learned about read and
write as the foundation."

## What was tested before

CAH (`plans/cah-plan.md`, 23 Oct; SPN R469) reran the February sweep at a reduced scale. A Cauchy kernel
1/(1 + ‖q − k‖²/γ²) came out level with softmax: perplexity 155.6 against 156.2, one seed each, 400 steps. CAH's reading
was that this kernel puts the Cauchy's shape on an amount, the length ‖q − k‖, with no turn behind it. It closed:
"A test of the framework in attention would put the Cauchy on a direction … not taken up." This plan takes that up.

## The three forms, sorted by read and write

- **Softmax**, exp(q·k/√d) normalized. q·k = |q|·|k|·cos α is two amounts times a direction; e is the DHV's completion
  (R915, R1062). It weighs every earlier key, including those behind the query (q·k < 0). It has no standpoint and
  covers both hemispheres: the DHV's form (R1046). Scaling one key by a factor changes its weight.
- **Cauchy on an amount** (CAH's kernel, here with no window), 1/(1 + ‖q − k‖²/γ²). The Cauchy's shape on a length.
  Scaling one key changes its weight.
- **The read** (new). Stand at the query. For each key, h = k·q̂ (its reach along the look) and v = |k − h·q̂| (its
  reach square to the look); the reading is the slope s = v/h. The weight is the plane's Cauchy heat on that slope, with
  the head's own thumb H (learnable, one per head, R226: the zoom):
  w = 1/(1 + (s/H)²) = h²/(h² + v²/H²).
  It has a standpoint (the query) and a facing. Scaling a key, or the query, by any factor leaves every s unchanged
  (R1039: no scale). Two variants:
  - **read, front**: w = 0 for h ≤ 0. Only the hemisphere in front of the query is read: one standpoint, one hemisphere
    (the SHV).
  - **read, both**: the same formula with h of either sign (s² is the same for h and −h), so keys behind the query are
    weighed as their mirror in front: the back hemisphere joined to the front (the DHV's join, R1105).

  The two read variants differ only in the back side, which is what Tom's line is about.

Classical: attention built on a cosine or on a normalized distance is known (cosine attention, Luo et al. 2018; Swin v2,
2021; L2 attention, Kim et al. 2021), and SHD (R1045) showed a function of |s| alone ranks the front exactly as cosine
does. What is new here is only the sorting: weighing the front hemisphere alone, from the query as a standpoint, by the
Cauchy heat with a thumb, against the same with the back side joined.

## Set-up

CAH's script and scale, unchanged except the attention module (`runs/rat/rat.py`): 4 layers, 4 heads, 128 wide, block
256, GPT-2's tokenizer, WikiText-2, 400 steps, AdamW 3·10⁻³, batch 16. Four arms: softmax; Cauchy on an amount (no
window, γ² per head); read, front; read, both (H per head, starting at 1). Three seeds each (42, 137, 2024). Validation
loss over non-overlapping blocks; perplexity its exponential. Rows with no key in front (read, front) give zero output;
the residual carries the token on. CPU, four threads.

## Predictions (committed before the script is run)

- **A1 (exact, before training).** On seeded random q and k (float64): every read weight (front and both) is unchanged to
  10⁻¹² when each key is scaled by its own factor e^U, U uniform on (−2, 2), and when the query is scaled; softmax's and
  the amount-Cauchy's normalized weights change by more than 10⁻³ somewhere. Read, front gives zero weight to every key
  with h ≤ 0; softmax gives each such key a positive weight. Killed if any clause fails.
- **A2 (competes).** Read, front's mean perplexity over three seeds is within 5% of softmax's, either side. Killed if it is
  more than 5% worse. (R1104: "competes", never "better".)
- **A3 (the back side, Tom's line).** Read, front's mean perplexity is no more than 1% above read, both's. Killed if
  read, both is better by more than 1% and by more than twice the standard error of the difference between the means.
- **A4 (how much the DHV form weighs the back).** In the trained softmax models, the share of attention weight on keys
  behind the query (q·k ≤ 0), averaged over validation positions, layers and heads, is under 20%. Killed if 20% or more.
- **A5 (the Cauchy on a direction against on an amount).** Read, front's mean perplexity is no more than 2% above the
  amount-Cauchy's. Killed if the amount-Cauchy is better by more than 2% and by more than twice the standard error.

One scale (CPU, 400 steps): a result here is evidence about this scale. A killed prediction stays killed; a fix is a new
run with its own prediction.

## Runs

**A1, run** (20 Nov, `python3 runs/rat/rat.py exact`, float64, 12 queries and 12 keys of 16 dimensions, seed 7):
**not killed.** Read weights moved by at most 4.5·10⁻¹³ (front) and 2.4·10⁻¹³ (both) when each key was scaled by its own
factor, 6.6·10⁻¹⁴ when the query was; read, front's weight on keys with h ≤ 0 exactly 0. Softmax moved by 0.78 and the
amount-Cauchy by 0.16 under the same key scaling; softmax's least weight on a key behind the query 0.0014, not 0.
