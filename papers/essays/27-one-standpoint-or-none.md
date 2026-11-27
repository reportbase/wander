# One standpoint or none: how alike, in AI and in a read

*The twenty-seventh of a series of essays on what can be known from where one stands. Draft, 16 November 2026. It
starts from three sentences of Tom's: "But AI dimensions are orthogonal. In observation, they share a denominator.",
and, after the test, "Cosine is dhv, so is Ai." The test is SHD (`plans/shd-plan.md`, `runs/shd/`), its predictions
written before the data. The numbers are from those runs or plain arithmetic; the classical results are named where
they are used, and what is a reading is marked so.*

Press "more like this" on a song, a film or a book, and a machine answers from a list. Behind the list, each item is a
point with a few hundred coordinates, and "alike" is a number worked out between two points. The commonest number is the
cosine of the angle between them: 1 for the same direction, 0 for square, −1 for opposite.

Ask the same question standing somewhere ("what here looks like the thing in front of me?") and the answer is made
differently. There is a look, a front and a behind, and everything is seen in terms of the one thing looked at.

This essay sets the two side by side. In the series' words, cosine similarity is the dual hemispherical vantage (DHV),
from no standpoint; a read about a query is the single hemispherical vantage (SHV), from one standpoint.
They agree wherever both apply, and the places they part show what each one is.

The order: the two questions (§1), cosine from no standpoint (§2), a read from the query (§3), one shared denominator
(§4), where the two agree and where they part (§5), what the words showed (§6), what the lengths carry (§7), not a
uniform sky (§8), many dimensions (§9), what is classical and what is ours (§10), and what it changes (§11).

---

## 1. Two questions

"How alike are these two?" can be asked two ways.

From no standpoint: take both items, set them in one frame, and compare them on equal terms. Neither is the one being
looked from. The answer is the same whichever is named first.

From one standpoint: take one item as the look, and say how the other appears from it. The first item is not in the
answer as a point; it is the direction everything else is read against. There is a front, the half of the directions the
look faces, and a behind, which a single look does not reach.

The first is how embeddings are built and searched. The second is how a read is made.

## 2. Cosine, from no standpoint

Cosine similarity is x·y divided by |x| times |y|. Three things make it the dual hemispherical vantage's (DHV's).

- **No standpoint.** Swap x and y and nothing changes. Neither vector is the look; both sit in one frame, side by side.
- **Both hemispheres.** It runs from +1 through 0 to −1. A thing directly behind gets a value, −1, as readily as a thing
  directly in front. Nothing is past a horizon.
- **An angle's function.** It is the cosine of the angle between the two, the completed turn's chart, which is
  trigonometry, and so the DHV's (*Reads and Writes* §1, R793).

The embedding it works on is the DHV's too. Every vector is held at once, all N of them, in one global frame, each
coordinate an amount on its own axis. That is what Tom's first sentence says: the dimensions are orthogonal, each its own
quantity, read on its own.

None of this is a fault. It is a description of where the number is taken from: from no standpoint, with the whole held.

## 3. A read from the query

Now stand at the query q and look along it. Any other item x is read in terms of that look:

- h, the part of x along the look;
- v₁, v₂, …, v_n, the parts square to it, in any square frame about the look;
- the readings s₁ = v₁/h, s₂ = v₂/h, …, every one over the same h.

Taken together, the readings give one number about the look, s = |v|/h: how far off the look x stands, in terms of its
own reach along the look. At s = 0 it is straight ahead; at s = 1 it is at the corner, as far off the look as along it.
For h ≤ 0 it is not in front at all; it is past the horizon, and the read has nothing to say about it.

No angle is taken and no trigonometric function is used. The readings are ratios of parts. The dual hemispherical vantage's name for s is
tan α, α the angle between x and q, but the read does not need the name.

## 4. One shared denominator

Tom's second sentence is the whole difference: in observation the readings share a denominator.

In an embedding each coordinate stands alone. In a read every reading is over the same h, so the readings are tied
together by it. Two consequences, each worked out before the data and checked on seeded draws (SHD run 2, 400,000 draws a
check, three laws for the parts):

**They are coupled.** The log of a reading is ln v_i − ln h. Two readings share the −ln h term, so their logs correlate,
even when every part is independent of every other. When the parts have one law, the correlation is exactly ½:
0.49982, 0.49974 and 0.50006 for normal, uniform and exponential parts, over 200 repeats each. Give each reading its own
denominator and the correlation is 0.

**They stay near together.** Ask what share of things have every reading inside the corner at once, every |s_i| ≤ 1:

| readings n | one shared h | each its own h |
|---|---|---|
| 1 | ½ | ½ |
| 2 | ⅓ | ¼ |
| 3 | ¼ | ⅛ |
| 8 | 1/9 | 1/256 |
| 768 | 1/769 | 2⁻⁷⁶⁸ |

With one shared h the share is 1/(n + 1): every reading is inside the corner exactly when h is the largest of the n + 1
parts, and with parts alike each is largest equally often. With orthogonal axes it is ½ⁿ, since each reading is inside
its own corner half the time, independently. At the size of a modern embedding the first is a share of one in 769; the
second is nothing at all.

So the shared denominator is what holds many readings together. Orthogonal axes fall apart into independent halves.

## 5. Where the two agree, and where they part

Here is the part worked out before any data was fetched. A read about the query that treats all its readings alike is a
function of s = |v|/h alone. In front of the look, s grows exactly as cosine falls. So every such read ranks the things in
front in exactly the order cosine does. The Cauchy's own heat about the look, 1/(1 + s²)^((n+1)/2), is one of these, and
ranks the same.

This was checked on the data (SHD run 2): rounded to twelve figures, the two rankings agree exactly, on both word lists.
(Run 1 missed by the last digit: each list holds a pair twice, the two copies' cosines equal to the last bit and their s,
read from each word in turn, not. Run 2 rounded first and the ranks met.)

So the read cannot beat cosine on the things in front. It is not meant to. Two accounts of one geometry agree wherever both
apply (R950). What separates them is what each needs and what each covers:

- **The standpoint.** Cosine needs none. The read needs one: the query, which is not compared but looked from.
- **The behind.** Cosine ranks what is behind the query. The read has a horizon there. In one of the word lists, five
  pairs of 353 (1.4%) were behind; cosine gave them values, the read gave them none.
- **The trigonometry.** Cosine is the cosine of an angle. The read is a ratio of parts.

The same thing happens in a menu bar, which shows why the two are so easily taken for each other. The games page's bottom
bar holds a game's tools on a ring: with more tools than the screen fits, it shows about as many as fit, whatever the
number of tools, the rest past the bar's ends, brought round by turning it. That is K, not N, on a screen (essay 16). But
the code that does it is the dual hemispherical vantage's: each tool at an equal turn, `angle + i·π/N`, put on the screen by
`tan`, the ones drawn found by `atan`, the ring closing on itself after a half turn. A single vantage would hold a slope for
the focus, place the others by composing slopes, (s + a)/(1 − sa), cull by comparing slopes, and have a fan running to a
horizon, never a loop; the wrap would be a count of the tools, not a turn. Both give the same chips in the same places. So
the bar works, and it is still not a read. Nothing in what it shows says which form made it; only what the code holds does:
an angle, π and a closing, or a slope, a composition and a horizon. They part only where the dual vantage has what a read
cannot (a closing, a total, turns in space that do not commute), and until a problem reaches one of those nothing forces
anyone to tell them apart. That is how the conflation survives: because it can. (R1264.)

## 6. What the words showed

The data: GloVe's 50-dimensional word vectors (Pennington, Socher and Manning 2014; 400,000 words from Wikipedia and
Gigaword), and two lists of word pairs rated by people for similarity, SimLex-999 (Hill, Reichart and Korhonen 2015) and
WordSim-353 (Finkelstein et al. 2002). Each measure was scored by how well its order matches the people's (Spearman's
correlation, higher matching better).

| measure | SimLex | WordSim |
|---|---|---|
| cosine (the dual hemispherical vantage, from no standpoint) | 0.265 | 0.503 |
| the read from the query, s (one standpoint, shared h) | 0.265 | 0.503 |
| Euclidean distance (an amount) | 0.276 | 0.464 |
| each coordinate over its own denominator | 0.192 | 0.238 |

Then the scale test, done to each word separately: every word's vector multiplied by its own random factor, between about
a seventh and seven times. Cosine and the read did not move at all; both read a direction, and a direction is unmoved
when the thing is scaled. Euclidean distance, an amount, fell to 0.04 and less (SimLex) and to below 0.15 (WordSim).

The orthogonal reading, each coordinate over its own denominator (the median over coordinates of how far apart the two
words' coordinates stand in log), did worst on both lists, before any scaling. That is the arithmetic of §4 in data:
readings that do not share a denominator do not hold together.

## 7. What the lengths carry

One prediction failed. I had written that cosine would beat Euclidean distance on both lists. On SimLex it did not:
Euclidean distance, 0.276, edged cosine, 0.265. On WordSim cosine led.

Euclidean distance uses the vectors' lengths, which cosine and the read set aside. So in these vectors the lengths carry
something SimLex's ratings follow. In the series' terms the length is an amount, written into the embedding by its
training, not a direction. What an embedding holds is not all direction: some of it is a write, and a measure that reads
only directions does not have that part.

The kill stays recorded. It is a fact about these vectors and this list, not a rescue of either measure.

## 8. Not a uniform sky

The Cauchy is the law of directions spread evenly from a standpoint: a uniform sky. Are a vocabulary's directions like
that, seen from any one word?

Far from it. Within 45° of a word, the corner in every direction at once, a uniform sky in 50 dimensions would put about
seven in a billion of all directions. The vocabulary puts four in ten thousand there: about 67,000 times as many. Taking
away the mean vector, which is known to lean all the vectors one way (Mu and Viswanath 2018; Ethayarajh 2019, cited from
memory, not opened), roughly halves it, and leaves it still about 29,000 times the uniform share.

So the Cauchy about a query is not the law of a vocabulary. The vectors bunch in a narrow cone. That is a fact about what
the training wrote, not about the read.

## 9. Many dimensions

Tom's first question was whether the Cauchy works past three dimensions. It does, in any number: directions spread evenly
over the front of a look in D dimensions, read on a flat screen square to the look, give the (D − 1)-dimensional Cauchy,
and every pair of readings keeps its own corner, half its readings each side.

But one thing changes, and it is the classical concentration of measure on a sphere (Lévy; Milman). The share of
directions within 45° of the look falls fast: half in the plane, 0.29 in space, 0.022 in nine dimensions, 0.001 in
seventeen, and nothing to speak of in hundreds; half the directions lie within 88.6° of the look in 769 dimensions. A
round cone about the look holds almost nothing. What survives is the shared denominator's own near field, every reading
within one thumb, falling only as 1/(n + 1). In many dimensions, near means near on every reading, in terms of the one
thing looked at, or it means nothing.

## 10. What is classical and what is ours

Classical: cosine similarity and its use in retrieval; the multivariate Cauchy as a ratio of normals and the gnomonic
image of a uniform hemisphere; t-SNE's use of the one-degree Student t (the Cauchy) for its low-dimensional map (van der
Maaten and Hinton 2008); concentration of measure; the anisotropy of embeddings; GloVe, SimLex and WordSim themselves.
That a correlation of logs over a shared denominator is ½, and that the share with one party largest is 1/(n + 1), are
exercises.

Ours: the sorting. Cosine as the dual hemispherical vantage's form, from no standpoint and over both hemispheres; the
embedding held whole, from the DHV; the read about a query as the single hemispherical vantage's, with a shared
denominator, a front and a horizon; the observation that the two rank the front alike, so the difference lies in the
standpoint, the behind and the trigonometry, not in the order of what is in front; and the orthogonal axes' ½ⁿ against
the shared denominator's 1/(n + 1) as the reason many readings hold together only from a standpoint.

## 11. What it changes

Nothing in how AI works, and the essay does not ask it to. Cosine is right for what it does, which is to compare two
things held in one frame from no standpoint. Neither vantage is called better (R939).

What changes is what the number is. "Similarity" in an embedding is a statement of the dual hemispherical vantage: both things held, neither
looked from, everything behind counted. A read's "alike" is another kind of statement: one thing looked from, the other
read in its terms, the behind past a horizon. They give the same order to what is in front, which is why the difference
has been easy to miss.

And the shared denominator says what a single vantage would add if anyone built one: readings that hold together in any
number of dimensions, because every one of them is in terms of the same thing. Whether that is useful for a machine is not
tested here. The test that could say would need a task in which what lies behind the query should not count.

One more sorting, after Tom: "Writing is reaching out into the world to touch it. All sorts of temporary writes are
needed to manage that touch." A model has both kinds. Its trained weights, and the lengths its vectors carry, are lasting
writes, kept between inputs. The activations and the attention cache are temporary writes: kept only while the model
reaches through one input, and cleared after. (R1048; the sorting a reading.)

And one more, after Tom: "The problem with dhv and why the natural world does not use it is because it's not real time,
it's historical, it's a record of writes that have occurred." An embedding is that record. It is trained on writing that
has already happened and frozen at its cutoff, so "more like this" is history consulted: two entries of the record
compared, from no standpoint. A look is now. (R1049; the DHV whole, the limit, is still made by no writes, R890;
what is a record is every representation anyone has.) It is a compressed record, far smaller than its corpus, which is what
lets it be held at all; a complete record of what it was trained on would be as large as the writing itself (R1050).

---

## Sources

- Tom, 16 November 2026: "Cauchy works on 3d. Does it work on 4d or greater? If so, could be used in AI."; "But AI
  dimensions are orthogonal. In observation, they share a denominator."; "Yes, write the plan and run the test";
  "Cosine is dhv, so is Ai."; "This uses arctan, so it's not fully shv"; "No.  Arctan works fine,  it's just not shv"; "This is why people
  conflate shv and dhv, because you can." (27 November, of the games page's tool ring); "Write an essay on this and a section to the read wrote paper as a point of comparison
  between shv and DHV."
- `plans/shd-plan.md`, `runs/shd/shd.py`, `runs/shd/shd2.py` (runs 1 and 2; the data's sources and sha256s in the plan).
- *Reads and Writes* (`../readers-and-writers.md`) §7, "Similarity from one standpoint and from none"; §1 (the reader uses
  no trigonometry).
- Essay 22 (`22-god-mode-and-a-vantage.md`) §13, what a single vantage is for; essay 16 (`16-k-not-n.md`), K, not N.
- J. Pennington, R. Socher, C. D. Manning, "GloVe: Global Vectors for Word Representation", EMNLP 2014. F. Hill,
  R. Reichart, A. Korhonen, "SimLex-999", *Computational Linguistics* 41(4), 2015. L. Finkelstein et al., "Placing
  search in context: the concept revisited", *ACM TOIS* 20(1), 2002. L. van der Maaten, G. Hinton, "Visualizing data
  using t-SNE", *JMLR* 9, 2008. J. Mu, P. Viswanath, "All-but-the-top", ICLR 2018. K. Ethayarajh, "How contextual are
  contextualized word representations?", EMNLP 2019. Cited from memory, not opened.
- SPN rulings cited: R793, R939, R950, R1037, R1045, R1046, R1048, R1049, R1050.
