# Reading a record: what attention reads, and where it learns

*The thirty-second of a series of essays on what can be known from where one stands. Draft, 21 November 2026. It writes
up five tests: RAT (`plans/rat-plan.md`, `runs/rat/`), SCT (`plans/sct-plan.md`, `runs/sct/`), NAT (`plans/nat-plan.md`,
`runs/nat/`), LNK (`plans/lnk-plan.md`, `runs/lnk/`) and GPA (`plans/gpa-plan.md`, `runs/gpa/`). Each had its predictions
committed before it ran, and each killed some of them; the kills are gathered in §8. Every number below is from those
runs. Since 20 November no test here trains a model at any size worth the name (R1139): the geometry is pointed at AI,
and others can test it at scale. The mathematics is classical and is named where it is used; the sorting is the
series' own, and is marked as a reading.*

A phone's keyboard offers the next word. Type "see you" and it offers "tomorrow", "soon", "later". Nothing in the phone
has been to tomorrow. It has read a great deal of what people wrote, and it offers what usually came next.

The model behind that offer, and behind the larger ones that write whole pages, has one step at its centre, called
attention. For each place in the text it asks which earlier places matter, gives each a weight, and blends what those
places carry by their weights. The weighting is a read: it looks from one place over the others. What the places carry,
and the rules that turn words into the vectors it compares, are writes: they were made, they are kept, and they are what
training changed.

The series has two acts for this. A read is continuous and unmoved by scaling; a write is discrete and has a size
(R896, R1039). The question here is what happens when the read the series has studied, the single hemispherical vantage
(SHV, one standpoint facing one way), is put where attention's read is, and what a trained model's own read looks like
when it is measured without training anything.

The short answer, from five tests: the read given by the geometry needs no training and is unmoved by sizes; in many
dimensions almost every key lies at its horizon; on language, the given read lost; a language model reads a record of
human writes, which nothing in nature does; and a trained model, measured, builds a facing of its own from each query's
own zero.

The order: the read just reads (§1), a read that needs no training (§2), many dimensions (§3), when the read met
language (§4), a record, not a world (§5), close links count for more (§6), what a trained model builds (§7), the kills
gathered (§8), what is classical and what is ours (§9), and what it changes (§10).

---

## 1. The read just reads

Tom's line, after the first of these tests: "The read just reads, the intelligence is in the write." (R1142.) And then:
"The last read reads the last write, the read is continuous, the write is discreet." (R1143.)

In attention the parts sort cleanly. A query and a key are vectors; the weight one puts on the other is computed from
them by a fixed rule; the output is the blend of the values by those weights. The rule is the read. The vectors are
writes: each was made by a learned map from a word and its place, and each stays in the model's cache once made. Each
new token's read reads the writes made so far, never one still to come. What training learns is the maps, so it learns
how to write the keys and values so that a fixed read finds them.

"Intelligence" is the everyday word, not a term of the series, as "reads" is never awareness (R1065). The claim it
carries is narrower and testable: if the read is given, then nothing about the read needs learning.

## 2. A read that needs no training

The series' read, put in attention's place, weighs a key k by its slope from the query's look. With h the key's reach
along the look and v its reach across, the slope is s = v/h, and the read's heat is the Cauchy's, 1/(1 + s²), counted in
the thumb H: a key straight down the look gets the most, a key square to it none, a key behind gets none if one facing
is read (R700, R728). Only directions enter. Scale a key by any factor and its slope does not move.

RAT checked that exactly first: the read's weights moved by at most 4.5·10⁻¹³ when each key was scaled by its own
factor, and softmax's (the usual rule, an exponential of q·k) moved by 0.78. Its least weight on a key behind the query
was 0.0014, not 0.

SCT then gave a small learner a task built so that only direction decides: thirty-two keys, the answer the one most
nearly on the query's look, every key given a random length that has no bearing on the answer. The front read scored
92.1% at the trained range of lengths and 92.1% when the lengths spread 403 times wider. Softmax scored 52.6% and fell to
20.4%; the Cauchy laid on an amount (CAH's kernel, on the distance ‖q − k‖) fell from 49.5% to 28.9%.

NAT took nature's lead (Tom: "The natural world figured this out long ago, let's follow its lead", R1141) and made the
task an eye's: a viewer at the origin, thirty-two things all round, half behind the look, distances spread a hundredfold,
the answer the thing nearest the look. The read on the raw positions, with no parameter and no training, scored 100% in
the trained world, the world a thousand times larger, the world a thousand times smaller, and with 1,024 things in place
of 32. Nineteen parameters in the read's form, trained, reached 96.6% and were unmoved by scale. A learned embedding into
64 dimensions with softmax, 17,025 parameters, reached 66.7%, fell to 17.4% when the world shrank a thousandfold, and to
17.5% with 1,024 things.

The tasks are the read's own, built so. They show what the given geometry does at no cost, not an advantage over
learned attention in general.

## 3. Many dimensions: every key at the horizon

The series' Cauchy keeps half its heat inside the corner, where the slope is 1. That is the plane's fact. NAT counted it
exactly in more dimensions: directions spread evenly over the front hemisphere of n dimensions, the share with slope at
most 1.

| n | 2 | 3 | 4 | 8 | 16 | 32 | 64 |
|---|---|---|---|---|---|---|---|
| share inside the corner | 0.5 | 0.2929 | 0.1817 | 0.0332 | 0.0015 | 4.2·10⁻⁶ | 4.6·10⁻¹¹ |
| median slope | 1 | 1.732 | 2.264 | 3.720 | 5.603 | 8.158 | 11.70 |

In three dimensions the share is 1 − 1/√2 and the median slope √3, as the paper has it (R700). By sixty-four, the size
of one of GPT-2's heads, the share inside the corner is five parts in a hundred billion. The median slope grows as
√(n − 1) times 1.4826, the normal law's constant for its median absolute deviation. Almost every key sits near the
horizon, nearly square to the look.

That is what the transformer's designers corrected for. The cosine between two random directions in n dimensions has
spread exactly 1/√n; softmax's logits are divided by √d (Vaswani et al. 2017) so that they do not shrink toward zero as
the dimension grows. Read in the series' terms, the 1/√d is the high-dimensional way's correction for every key lying at
its horizon. This part is classical, the concentration of measure; the sorting is ours: the corner at the median of a
read is the plane's alone, and the read's heat gives the front a structure only in few dimensions.

## 4. When the read met language

RAT put the read into a small language model, four arms over three seeds each, trained the way CAH had trained for
softmax, 400 steps on a CPU. Perplexity, lower better:

| arm | perplexity |
|---|---|
| the Cauchy on an amount | 154.79 |
| softmax | 156.03 |
| the read, both hemispheres | 158.06 |
| the read, front only | 166.42 |

The front read lost by 6.7% against softmax. Joining the back side brought it within 1.3%. Trained softmax put 24% of
its weight on keys behind the query. The read's loss did not move when the keys were scaled (by 10⁻¹⁰), and it was as
well calibrated as softmax. Softmax's loss moved only 0.4% under the same scaling: a learned model is not as bound to
key size as the prediction assumed.

Tom read it at once: "I think the results would be dependent on how the writes are written." And then: "discreetness
organizes the writes. Discreteness writes the full Apple, not half the apple in front and half in back. Discreteness
does not have a hemisphere." (R1138.) A key is a write, and a write is whole. One read faces one hemisphere of it; the
whole needs two facings, or the join the dual hemispherical vantage (DHV) holds. On the language task the join helped;
on SCT's task, where the answer lies in front by construction, the same join halved the score (47.2%), since a key and
its opposite read alike.

The writes in RAT were CAH's, chosen for softmax, and a row with no key in front gave the front read nothing to blend.
Neither was tested. RAT was closed at its first run (R1139).

## 5. A record, not a world

Tom, after NAT: "George Washington apple tree is a story about honest, apples and trees. The natural world would not care
about there connection, AI would." (R1145.) And: "Ai is doing something new, no natural world comparison." (R1146.)

A story's connections are writes people made. Nature joins a fruit to its tree, since it grew there; it does not join
honesty to either. (The story is Weems's cherry tree, from the 1806 edition of his life of Washington, told as a lesson
and not attested as fact.) A model trained on text learns which writes went together in what people wrote. Its geometry
is the record's, not a standpoint's read of the world.

That bears on how far nature's lead reaches. NAT's eye task is a read of a world, and there the given read answered
everything. A language model reads a record of writes. In the series a record held whole is the DHV's (R1049, R1050),
and softmax, which depends on no facing, is the DHV's form (R1046). That may be why softmax suits language where the
single vantage's read did not. A reading, not a test.

Tom added two lines on writes in nature, which belong here as the contrast: "A rock is stable, not much or any writes
going on. Water is not stable, it flows, lots of writes going on." (R1144.) The last read of a rock meets a write made
long ago; the last read of water meets one just made. A record of human writing is neither: a great deal written, kept
whole, read at once.

## 6. Close links count for more

Tom: "Not all links the same, maybe close links are better" (R1147). LNK counted it on a text with no training: how much
a word tells about the word d places on, in WikiText-2 (2,051,910 words, the 2,000 commonest kept), the bias of counting
taken off by a shuffled copy.

| d | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 |
|---|---|---|---|---|---|---|---|---|---|---|
| bits | 1.246 | 0.484 | 0.139 | 0.056 | 0.033 | 0.024 | 0.019 | 0.015 | 0.014 | 0.011 |

The next word tells 1.25 bits, the fourth 0.14, the sixteenth 0.03. The prediction that the fall would be the Cauchy in
distance, flat inside a thumb and falling as 1/d² past it, was killed: off by 81% at its best thumb. The fall is two
regimes instead, about d^(−1.5) over the first eight words or so and about d^(−0.3) past them, with a knee near ten
words, roughly a sentence's reach. Read in the paper's terms, the knee is a corner of the record's own: near links fall
fast, far links hold by slow ratios, about 0.8 a doubling. That reading came after the run, on one text.

## 7. What a trained model builds

Then the measurement with nothing trained at all. GPA ran GPT-2 small (OpenAI 2019; twelve layers of twelve heads, 64
dimensions a head) forward only on forty blocks of 256 tokens of WikiText-2, and read off every head's queries, keys and
weights.

**The first token.** GPT-2 pours much of its weight onto the first token of a block, known as an attention sink (Xiao et
al. 2023, from memory). The median head put 48% of its weight there, 1% in the first layer rising to 64% by the eighth.
No direction asks for it. The other measures leave it out.

**No knee.** With the first token left out, a head's weight on the key d places back falls at one rate, about
d^(−0.85), from d = 1 to 128: slope −0.88 over the first eight, −0.82 past sixteen. The text's own links had a knee;
the model's attention does not.

**The sign of q·k is not a facing.** The prediction that a head puts under 10% of its weight on keys with q·k ≤ 0 was
killed: the median head put 64% there. But 98% of keys had q·k ≤ 0 by count. In GPT-2 the raw sign is set mostly by a
shared offset between queries and keys, and softmax depends on a query's logits only up to a constant: add the same
number to all of them and nothing changes. So softmax has no standpoint of its own, and the sign of q·k is not something
it reads. That was my set-up, and it fits R1046: softmax is the DHV's form, with no facing.

**A facing of its own.** Measured instead from each query's own zero, the mean of its logits over its keys (a choice
made after seeing the first run), about half the keys lie below (median 53%), and they get 5.2% of the weight, by layer
2% to 14%. So a trained head does build a facing: nearly all its weight on one half of what it could read, the half
counted from its own zero, not from the origin. It is a facing in the read's sense, one side kept and the other let go,
made by the writes rather than given.

**Few dimensions.** The keys' participation ratio, how many of the 64 dimensions they spread over, was 3.1 in the median
head as first measured, but that was mostly the shared offset. With the keys centred it is 12.1, from 2.5 to 27 by layer.
Few dimensions, but not three.

One model, one text, inference only. The centred numbers were found after the run, so they are readings until a second
run predicts them first.

## 8. The kills, gathered

Each test committed its predictions first. Those killed:

- RAT A2, A3, A4, A5, A7: the front read lost to softmax by 6.7% (bound 5%); the back side helped; trained softmax put
  24% behind the query (bound 20%); the front read lost to the amount-Cauchy; softmax moved only 0.4% under key scaling
  (bound 1%).
- NAT B3: the learned embedding was predicted to break the scale test when the world grew a thousandfold; it fell 8
  points there and 49 when the world shrank. The embedding does break the test, on the side I did not predict.
- NAT's read in 64 dimensions after a learned embedding did not train at all, near chance from the start. The likely
  cause is my code (a guard of 10⁻³⁰⁰, which is 0 in float32), untested.
- LNK L2: the Cauchy in distance, off by 81%. LNK's counted range was also cut short by my rule for what counted.
- GPA G1, by my set-up (the sign of q·k), and G3: no knee in the model's attention.

Not killed: every exact check (the read unmoved by sizes, NAT's dimensions and 1/√n, SCT's reads alike at every range),
the read's calibration, NAT's spread-of-sizes and many-things predictions, LNK's steady fall, and GPA's few dimensions
and attention sink.

## 9. What is classical and what is ours

Classical: attention and softmax's 1/√d (Vaswani et al. 2017); the concentration of measure, almost every direction near
the equator of a high-dimensional sphere; the mutual information between words falling with their distance (Lin and
Tegmark 2017, from memory); attention biased toward near positions (sliding windows; ALiBi, Press et al. 2022); the
attention sink (Xiao et al. 2023). The Cauchy's heat and its corner are the series' earlier results (R700, R728).

Ours: the sorting. The weighting is the read and the embeddings, keys, values and weights the writes; the given read
needs no parameter and is unmoved by size; in many dimensions the read's front loses its structure, and the 1/√d is the
correction for keys at the horizon; softmax has no facing, as the DHV's form, and a trained model builds one from its
own zero; a language model reads a record of human writes, which nature's reads do not resemble. None of this is
claimed as new about AI. It is the series' account of what attention is doing, checked where it could fail.

## 10. What it changes

For the series: the read's claims held where the task was a read of a world, at no cost, whatever the sizes and however
many things there were. They did not carry to language, and the reason the tests point to is the one Tom gave: a record
of writes is held whole, and the DHV's form fits it. Nature's lead bears on reads of a world; it says nothing either way
about reading a record (R1146).

For AI, a reading offered to whoever tests it at scale: attention's read could be taken as given, and every learned
parameter put in the writes. NAT run 2 would test that on the eye's task, the read fixed and only the writes learned
(R1142). GPA run 2 would test whether a trained model's own facing, about half its keys getting 5% of the weight, and
its keys' twelve or so dimensions, are found again when predicted first, on another text and a larger model. Neither
needs a training run beyond seconds on a CPU.

---

## Sources

- Tom, 20 November 2026: "Ai uses trig to read, which means it is looking at the back side."; "I think the results would
  be dependent on how the writes are written."; "discreetness organizes the writes. Discreteness writes the full Apple,
  not half the apple in front and half in back. Discreteness does not have a hemisphere."; "These ideas can be explored
  without expensive ai training sessions. Others can test these ideas at scale."; "The natural world figured this out
  long ago, let's follow its lead, see if it helps, it's a result either way."; "The read just reads, the intelligence is
  in the write."; "The last read reads the last write, the read is continuous, the write is discreet."; "A rock is
  stable, not much or any writes going on. Water is not stable, it flows, lots of writes going on."; "George Washington
  apple tree is a story about honest, apples and trees. The natural world would not care about there connection, AI
  would."; "Ai is doing something new, no natural world comparison."; "Not all links the same, maybe close links are
  better". 21 November: "Is there any promising ideas about Ai that we should explore"; "1"; "proceed with 1 and 2".
- `plans/rat-plan.md`, `runs/rat/`; `plans/sct-plan.md`, `runs/sct/`; `plans/nat-plan.md`, `runs/nat/`;
  `plans/lnk-plan.md`, `runs/lnk/`; `plans/gpa-plan.md`, `runs/gpa/` (outputs `gpa-results.json`, `gpa-posthoc.json`).
- Essays 16 (`16-k-not-n.md`), 22 (`22-god-mode-and-a-vantage.md`) and 27 (`27-one-standpoint-or-none.md`).
- A. Vaswani et al., "Attention is all you need", 2017. A. Radford et al., "Language models are unsupervised multitask
  learners", OpenAI, 2019 (GPT-2). H. W. Lin and M. Tegmark, "Critical behavior in physics and probabilistic formal
  languages", 2017. O. Press, N. A. Smith and M. Lewis, "Train short, test long", 2022 (ALiBi). G. Xiao et al.,
  "Efficient streaming language models with attention sinks", 2023. All from memory, not opened.
- S. Merity et al., WikiText-2, 2016, as used in CAH.
- SPN rulings cited: R700, R728, R896, R1039, R1046, R1049, R1050, R1065, R1138, R1139, R1141–R1149.
