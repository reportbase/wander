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

## Run 3: readers' formats and writers' formats (predictions written 3 November, before any code for run 3)

Tom, after run 2: "Readers have a facing, they rotate. Writers walk the line, they interact with the world. TVF is a
readers format.", then "I actually think this is our best proof of readers and writers being different situations.",
then "Proceed" to a test that could fail: more than one format on each side, a crossover predicted per figure, and a
hybrid. Run 2's reading was made after its numbers were seen; this run states its predictions first.

**The claim under test.** A *reader's* format lays its numbers at addresses fixed in advance by an even turn (the same
addresses for every shape); the shape is the payload painted on them. A *writer's* format walks the line, each number a
step or a place met along the way. If the two are different situations, then, whatever the particular format:
a reader's format is short where the outline is smooth and long at corners; a writer's the other way; a reader's
format with *place* addresses (neighbouring addresses hold similar values) is barely moved when one number is lost and
spreads one wrong number over its neighbours; a writer's absolute format keeps a wrong number local, and a writer's
relative format (steps) carries every error on to the end of the walk. A format that gives the smooth runs to a reader
and the corners to a writer should be shortest.

**Formats** (box 0–1000, τ = 5 by the plan's Hausdorff test, numbers integers, or one decimal where integers cannot
pass; the fewest numbers that pass, by doubling then bisection; o200k_base tokens):
- Readers: **TVF** (run 2's texts, unchanged); **FD**, Fourier descriptors: the complex coefficients c₋K … c_K of the
  outline walked by arc length, a row of real parts and a row of imaginary parts (frequency addresses, not places);
  **RAD**, the radial function from the area centroid, the radius at N even angles (k + ½)·2π/N, rebuilt by draw's
  kernel (place addresses by angle; defined only on figures every ray from the centroid meets once; elsewhere it does
  not apply and is left out).
- Writers: **SVG** (run 2's texts, absolute and relative, the shorter for length); **POLY**, the outline's vertices by
  Douglas–Peucker, absolute x y pairs; **STEP**, the same vertices as a start and steps dx dy; **TURTLE**, a start and a
  heading, then forward d, turn a (degrees).
- Hybrid: **HYB**, the corners (the plan's rule) as absolute places, and for each run between two corners its
  departure from the straight chord at n even places, rebuilt by sine interpolation (a reader's leaves on each run);
  on a figure with no corners it is TVF's text.

Slips as in run 2, every format, 20 a figure a kind. Jitter moves a number by ±1% of its own range (±10 units; a
turtle's turn ±3.6°). A second measure joins the Hausdorff: the share of the rebuilt outline (by length) more than 10
units (1%) from the figure, "share disturbed".

**Predictions** (figures: smooth = no corner, 12 in run 2; cornered = 2 or more corners):
- **Q1** Smooth figures: every reader format's median tokens is below every writer format's. Killed if not.
- **Q2** Cornered figures: every writer format's median tokens is below every reader format's. Killed if not.
- **Q3** Per figure, the best reader format is shorter than the best writer format on at least 75% of smooth figures,
  and longer on at least 90% of cornered figures. Killed if either share falls short.
- **Q4** HYB is the shortest format (ties count) on at least 70% of figures, and its median over the best writer
  format on cornered figures is at most 1.0. Killed if either fails.
- **Q5** Dropped token, broken share: TVF and RAD (place addresses) break less often than every writer format. FD
  (frequency addresses: a lost number shifts every later coefficient to another frequency) breaks at least as often as
  the median writer format. Killed if any part fails.
- **Q6** Wrong number, median share disturbed: the absolute writers (SVG absolute, POLY) are below TVF and RAD; the
  relative writers (SVG relative, STEP, TURTLE) are above both absolute writers. Killed if any ordering fails.
- **Q7** Imprecise numbers: each relative writer (SVG relative, STEP, TURTLE) breaks more often than every absolute
  writer and every reader format. Killed if not.

**Run 3 (3 November)** (`runs/txt/txt-run3.txt`; the fitting scripts were tried first on five figures, whose token
counts were seen before the full run). 73 figures: 12 smooth, 4 with one corner, 57 cornered; every text checked
within τ as read back. Median tokens, o200k_base:

| | TVF | FD | RAD | SVG | POLY | STEP | TURTLE | HYB |
|---|---|---|---|---|---|---|---|---|
| smooth (12) | 90 | 63 | 35 (10) | 127 | 135 | 134 | 199 | 90 |
| cornered (57) | 656 | 569 | 409 (44) | 150 | 74 | 72 | 110 | 56 |

- **Q1 not killed.** On smooth figures all three readers' formats are shorter than all four writers'.
- **Q2 not killed.** On cornered figures all four writers' formats are shorter than all three readers'.
- **Q3 killed narrowly.** The best reader beats the best writer on 100% of smooth figures; the best writer beats the
  best reader on 89% of cornered figures, against 90%. The six exceptions: four `graze` figures, which my corner rule
  calls cornered but which FD and RAD hold in 19 tokens (a sharp but smooth turn, not a corner); the polar `flower`,
  whose radius from its centre is its own formula (RAD 31 tokens against 267); and `hinge7` (179 against 195).
- **Q4 killed.** HYB has the lowest median on cornered figures (56), but per figure it is 1.03 times the best writer, and
  it is the shortest format on only 25% of figures: on smooth figures it is TVF, which FD and RAD beat.
- **Q5 killed by FD.** Dropped token, broken: TVF 51%, RAD 58%, FD 42%, every writer 75–94%. The readers all break
  less than every writer; my reason for FD breaking was wrong (most of its coefficients are small, so the ones a drop
  shifts are near nothing; its median distance 0.9%).
- **Q6 killed.** Wrong number, share disturbed: RAD 1.9%, FD 0.0%, TVF 17%; SVG absolute 10%, POLY 16%; STEP 40%,
  TURTLE 42%, SVG relative 8%. Post hoc, a fault of my slip: a wrong number is drawn from the same text, so a format
  whose numbers are alike (RAD's radii, FD's small coefficients, SVG relative's small steps) is barely moved by it.
  The slip measures how alike a format's numbers are as much as where an error goes.
- **Q7 killed by FD.** Imprecise numbers, broken: TURTLE 84%, STEP 29%, SVG relative 10%; SVG absolute, POLY, TVF and
  RAD 0%; but FD 92% (±10 on every coefficient adds up over the whole outline).

**Reading, after the run.** The length profile held cleanly on three formats of each kind (Q1, Q2) and figure by figure
in 89% of cornered and all smooth figures: where a shape is smooth a reader's format is shorter, where it has corners a
writer's. The robustness profile did not sort by reader and writer. It sorts by how a format addresses its numbers:
*places* (TVF, RAD, POLY, SVG absolute) keep imprecise numbers local; *steps* (STEP, TURTLE, SVG relative) carry them to
the end of the walk; *frequencies* (FD) spread them over the whole outline. Losing a token is the one slip where the
readers as a group did better than every writer. The hybrid did not beat the best single format on its own figures.

**On the hybrid (3 November, after run 3).** Tom: "Readers rotate, writers walk. I don't know what a hybrid system even
is." The hybrid was my construction, not the framework's: in *Reads and Writes* a read and a write are two acts, and an
observer who reads and then writes is writing (R594), not doing a third thing. Q4 tested an engineering mixture, not a
consequence of the distinction, and its kill says nothing about the distinction either way.

**An observation, not a ruling (3 November).** Tom: "Gibbs corner i think demonstrates the problem. We're shocked when
we see the ringing, because nature does not ring like that.", then "This is just an observation at this point. Readers
don't take sharp turns, there turns are rotational." A reader's turn passes through every direction between two
directions, so a reader has no sharp turn of its own; a corner, a jump in direction at one place, is met only by walking
the line. Asked to hold one, a reader's even addresses ring (Gibbs: on both sides, not shrinking with more addresses;
on an outline's corner, ringing in direction that shrinks only as 1/N, which is the cost run 2 and run 3 measured).
Nature's ringing comes after its event (a struck bell) or on one side of an edge (diffraction). Not tested here.

**Observations continued (3 November, not rulings).** Tom: "A write is a count, it is discrete. A read is continuous.
The weird numbers of pi and e arise when a write tries to convert a read into a write." Then, asked whether the
reader's K addresses (R408) are a count: "K is continuous, not discrete. K is read continuously." Read here: π is where
Archimedes' count of sides would end if it held the whole turn, e where Bernoulli's count of compoundings would end if
it became continuous (essay 15, R597); a `.tvf` is a count (N numbers), its leaves at (k + ½)·π/N, and Gibbs's overshoot,
the residue of a finite count holding a corner, is a number defined through π (about 0.0895 of the jump). K continuous
agrees with OFS's "A resolution, not cells" (R367: the level continuous, the array rounds and the reader does not) and
with R373 (the floor is what discards); the count of addresses is the writer's floor of it.
