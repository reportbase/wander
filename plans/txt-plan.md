# TXT: TVF text against SVG paths as text a model reads and writes

*Plan written 3 November 2026, before any code for it was written or run. Tom, after AMX: "the advantage is the text
format. it is speculated that it would be easier to train AI with text.", then "yes" to two quick tests (token counts,
robustness to the kind of slips a model makes). The third test, training two small models, is not part of this plan.
Nothing above the "Runs" line is edited after the first run.*

## The question

AMX found TVF no smaller than FLAC or Opus for audio, and a shape's `.tvf` larger than its SVG. The claim to test now is
different: that TVF's text (rows of leaf values, no grammar) is easier for a language model to read and write than SVG's
path data. Two things a model meets can be measured without training one:

1. **Length in tokens.** The same outline, to the same accuracy, as TVF text and as an SVG path, counted by a standard
   tokenizer. A longer form costs a model more context and more steps to write.
2. **Robustness to slips.** A model's mistakes are a wrong number, a dropped token, imprecise numbers. Put each into both
   forms and measure how far the drawn outline moves.

## Known beforehand

- AMX run 3 (wander) and draw `papers/tvf.md` §7: TVF text is larger in bytes than the binary or path forms it was
  compared with. Bytes are not tokens: a tokenizer splits digits and spaces its own way.
- draw `?lab=aim` (`papers/labs.md` §58): even leaves need many more numbers where an outline has corners (Gibbs ringing
  at a corner falls slowly), and few where it is smooth.
- draw's SVG export (`_fitCubics`, Schneider 1990) fits cubics to a reconstruction; a polygon's straight edges are one
  cubic each.
- Text tokenizers split long numbers into several tokens, and language models are known to handle numbers in text
  poorly. Nothing here is new about tokenizers; this measures two formats with them.
- The SVG path grammar (SVG 1.1, F.2 "Error processing"): a path is drawn up to the first error and the rest ignored.

## Data and set-up

- **Figures:** every figure in draw's shape library with a point generator (`PRIMITIVES` with `pts`, about 80), read
  from draw at the branch's head by a headless browser, walked by arc length to 2,048 points and scaled so the longer side
  of its box is 1,000 units (the box 0–1000).
- **Tolerance τ:** 5 units (0.5% of the figure) and 1 unit (0.1%). A form passes when the symmetric Hausdorff distance
  between the figure's 2,048 points and the form's drawn outline (sampled densely) is at most τ, after its numbers are
  rounded as written.
- **Numbers:** integers at τ = 5, one decimal at τ = 1, the same for both formats.
- **TVF:** the fewest even N (4 to 1,024) whose leaves (the figure walked at (k + ½)/N of its length, as `?lab=aim`
  does) pass, reconstructed by draw's `tvf-core.js`. Written as the spec writes it: `TVF N 1 2`, a row of x, a row of y.
- **SVG:** draw's own `_fitCubics` on the 2,048 points, its tolerance lowered until the rounded path passes. Written as the
  path data alone, no XML around it (which favours SVG), in two variants: absolute (`M x y C … Z`) and relative
  (`m … c … z`, shorter numbers). Each comparison is against the shorter of the two.
- **Tokenizers:** o200k_base and cl100k_base (tiktoken). Claude's own tokenizer is not public; these stand in for a
  standard byte-pair tokenizer. Characters are reported too.
- **Corners:** a figure has a corner if its outline turns by more than 30° within 1% of its length (from the 2,048 points);
  the rest are smooth.
- **Slips** (at τ = 5, seeded, 20 a figure a kind a form):
  - (a) *wrong number:* one number replaced by another number from the same text;
  - (b) *dropped token:* one token (o200k_base) taken out of the text, the rest put back together;
  - (c) *imprecise numbers:* every number moved by a uniform amount in ±10 (1% of the figure).
- **Readers, lenient:** SVG by its spec's error rule (drawn up to the first error, Z added if missing). TVF takes each row
  as it comes (a row of fewer than 3 numbers, or no row, fails; the header's N ignored where the rows disagree). Also
  reported: TVF read strictly (N must match both rows), which fails on a dropped number.
- **Measure:** the slipped form's Hausdorff distance from the figure, over 1,000. *Broken*: over 5%, or nothing drawn.

## Predictions

- **T1** At τ = 5, the median over all figures of TVF tokens over SVG tokens (o200k_base) is between 1.0 and 2.5: TVF
  longer, but not by more than 2.5×. Killed if outside.
- **T2** The median ratio at τ = 1 is larger than at τ = 5 (corners cost leaves faster than cubics as the tolerance
  tightens). Killed if not.
- **T3** On the smooth figures alone the median ratio at τ = 5 is under 1 (TVF shorter). Killed if not.
- **T4** Every slipped TVF read leniently draws a closed curve (100%); every slipped SVG draws something (at least 95%).
  Killed if either is lower.
- **T5** Dropped token: TVF's broken share is at most half SVG's. (A dropped number shifts the rest of a TVF row by one
  leaf, a small move when leaves are close; in SVG it swaps x and y for the rest of the path.) Killed if not.
- **T6** Wrong number: TVF's broken share is no higher than SVG's. Killed if higher.
- **T7** Imprecise numbers: both broken in under 5% of trials, and TVF's median distance within 3× of SVG's. Killed if
  not.

## Runs

**Set-up amended before any run (3 November).** draw's `_fitCubics` joins every split with a shared tangent, so on its
own it cannot make a corner and would spend many cubics rounding each one: unfair to SVG. Each outline is cut at its
corners (the plan's corner rule) and each run between corners fitted by `_fitCubics` on its own, so SVG keeps corners.
The fewest even N is found by doubling and then bisection, which assumes the error falls with N. An SVG cubic is drawn as
24 straight pieces, a TVF as 4,096 samples (1,024 in the slip trials); a Hausdorff distance is measured from points to
segments. Scripts: `runs/txt/txt_lib.cjs`, `txt_fit.cjs`, `txt_slip.py`, `txt_read.cjs`.

**Run 1 (3 November): killed by my set-up, no result.** The fit ran under a 15-minute limit of mine and was stopped
after 50 of the 73 figures, before writing anything; no number was read. Run 2 is the same set-up, the figures split
over four processes, and the distance's search confined to its grid (a speed change; the distances are the same).

**Run 2 (3 November)** (`runs/txt/txt-run2.txt`; the scripts were tried first on two figures, circle and square, whose
numbers were seen before the full run). 73 figures, 12 smooth and 61 with corners by the plan's rule.

- **T1 killed.** At τ = 5 the median TVF/SVG ratio in o200k_base tokens is 3.42 (cl100k_base the same): TVF 3.4 times
  longer. On figures with corners it is 4.28. A square takes 174 leaves (≈ 1,300 tokens) against 4 cubics.
- **T2 not killed.** At τ = 1 the median ratio is 11.77; 7 figures could not reach τ = 1 within 1,024 leaves.
- **T3 not killed.** On the 12 smooth figures TVF is shorter: median 0.63 (circle 24 tokens against 55, egg 0.36,
  blob 0.52; only the crescent, with two near-corners, is longer at 1.73).
- **T4 killed by my bound.** TVF read leniently drew a closed curve in 99.5% of slips, not 100%: a dropped newline
  merges the two rows. SVG drew something in 98.8%.
- **T5 killed.** Dropped token: TVF broken 51.2% against SVG 89.3%, not half. TVF's median distance was 5.4%, SVG's
  64%: TVF moves much less but still breaks half the time, because a dropped token is often part of a number (digits
  lost), not a whole number. Read strictly, only 1.6% of TVF slips pass.
- **T6 killed.** Wrong number: TVF broken 71.1% against SVG 49.2%. One wrong leaf moves the curve near it by the error,
  the kernel spreading it; one wrong SVG number moves a control point, which a cubic pulls on less.
- **T7 killed, by SVG.** Imprecise numbers: TVF broken 0.0%, median 1.52%; absolute SVG 0.0%, 1.06%; relative SVG 9.7%
  broken, 2.81%, since in relative form every error carries on to every later point. Against the shorter SVG (mostly
  relative) the 5% clause fails on SVG's side.

**Reading, after the run.** As text a model writes, TVF is shorter and steadier than SVG only on smooth outlines. On
outlines with corners, most of the library, it is 3–4 times longer at 0.5% and 12 times at 0.1%. It survives a dropped
token much better than SVG and imprecise numbers about as well as absolute SVG, and it is hurt more by one wrong
number. The case for TVF as a format for models is for smooth curves, or with corners carried separately (draw's
`#meta` structure, `papers/tvf.md` §2.9), which this run did not test.
