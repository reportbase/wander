# ONL: online decisions read as the reader's geometry

*25 October 2026. Tom: "its interesing to frame a dynamic array as a situated observer."; "a dynamic array is grows and
shrinks, but you you know its size at any point in time. however, it could grow or shrink unknowably."; "I wonder if our
framing would offer a geometric insight into those patterns and why they work."; "i'm interested if it helps Ofs and the
geometry."; "does it say anything about the near and far fields"; then "yes" to this plan. Exact arithmetic (fractions)
and one literature search; no physics, no page.*

## The reading, before any run

An online decision is made now, with the future unknown. The *offline* optimum knows the whole sequence: the writer. The
online algorithm does not: a reader situated in time, its standpoint "now", the unknown future the other party whose
breadth it never reads. A dynamic array is a writer of its past (its size now is an amount, exactly held) and situated
about its future (it may grow or shrink without bound, and cannot know which).

Three claims, each to be checked:
1. **The corner.** Where the decision trades an amount already sunk against an amount about to be committed, and the
   future charges for whichever turns out larger, the worst case depends only on their ratio r and is reciprocal-symmetric,
   f(r) = f(1/r). So the best place to stand is the corner, r = 1 (OFS Proposition 13's median of the bounds, in time).
2. **The levels.** Where the unknown is a scale (a distance, a final size), a strategy with the same guarantee at every
   scale steps by a fixed ratio, so its turn points are a geometric sequence: the reader's levels from dκ/κ (OFS §2, §8).
   The ratio is free unless a cost is added; where a cost is added and it is of the sunk-against-committed kind, the corner
   fixes the ratio (SPN Proposition D.1: other bases need an added measure).
3. **Near and far.** Each such algorithm needs one chosen scale, its H (the first leg, the start capacity, the price), and
   without it the guarantee fails near home (OFS: H of 0 loses what is read). Inside the corner its guarantee is absolute (a
   fixed amount, set by H); past it, relative (a fixed ratio). This is OFS §8's "detail absolute inside the corner,
   relative past it" as a cost bound. H is a zoom: it moves where the levels fall, not the far-field constant.

## Known beforehand

These are classical and are not tested as new:
- Competitive analysis (Sleator and Tarjan 1985; Karlin, Manasse, Rudolph and Sleator 1988; Borodin and El-Yaniv 1998).
  An algorithm is c-competitive if ALG ≤ c·OPT + α for every input; the additive constant α is in the definition.
  *So claim 3's split is already the definition's two terms; what would be ours is only that α is set by a chosen H and
  that the split falls at the corner.*
- Ski rental: rent until the rent paid equals the price, then buy, 2-competitive (2 − 1/B in whole days); randomized,
  e/(e − 1) (Karlin, Manasse, McGeoch and Owicki 1994).
- The cow path (linear search on two rays): doubling turn points give 9, optimal among deterministic strategies (Beck and
  Newman 1970; Baeza-Yates, Culberson and Rawlins 1993), assuming the target is at least a unit away.
- Table expansion and contraction (Cormen et al., §17.4): double at load 1, halve at load ¼, amortized O(1); halving at ½
  thrashes. Geometric growth by g copies under gN/(g − 1) in all.
- "Each doubling step costs as much as all before it" is folklore of the doubling trick.
- MOT run 2 (`plans/mot-plan.md`): a quantity unchanged by swapping its pair has f′(1) = 0 at the corner.
- Claude's checks in conversation (25 Oct, exact fractions): the cow path's 1 + 2b²/(b − 1) equals 5 + 2(r + 1/r) with
  r = 1/(b − 1) at b = 3/2, 2, 3, 4 (10, 9, 10, 35/3); ski rental's worst ratio is 1 + max(s, 1/s) at s = ½, 1, 2 (3, 2,
  3); the dynamic array's past copying over the new copy tends to 1/(g − 1). These are stated here, so they are not
  predictions.

## Predictions

*Each with its kill condition. Written before `runs/onl/onl.py` exists.*

- **O1, ski rental at the corner.** Continuous: buying after paying sB in rent has worst ratio exactly 1 + max(s, 1/s),
  least at s = 1 and the same at s and 1/s for every rational s tried. Whole days, price B: buying on day B gives
  2 − 1/B, the least over every day of buying, for B = 1 … 50. *Killed* if any tried s breaks the symmetry or any B has a
  better day than B.
- **O2, the cow path's 2 is the corner.** With first leg d₀ = 1 and turn points bᵏ alternating sides, the supremum of
  (distance walked)/(distance to target) over targets x ≥ 1 equals 1 + 2b²/(b − 1) = 5 + 2(r + 1/r), approached just past
  a turn point and not attained, for b = 3/2, 2, 3, 4 (computed by the walk, not the formula). Least at r = 1 (b = 2),
  9. *Killed* if the walk's supremum differs from the formula at any b.
- **O3, near and far on the cow path.** For targets 0 < x < 1 behind the start, the ratio is unbounded as x → 0, and the
  excess walking (distance walked − x) is exactly 2d₀ behind the start and 0 ahead of it (a fixed amount). For x ≥ d₀ the excess is at most
  (c − 1)·x with c the O2 constant (a fixed ratio). Doubling d₀ leaves the far-field constant unchanged and doubles the
  near-field bound. *Killed* if the near-field excess grows with x → 0 or the far constant moves with d₀.
- **O4, the dynamic array's band.** Grow by g at load 1, shrink by g at load 1/g²: both resizes land at load 1/g, the
  geometric middle of [1/g², 1], for g = 3/2, 2, 3, 4. Shrinking at 1/g instead: alternating push and pop at the boundary
  costs at least N element copies per pair of operations, for N up to 2¹⁶. Over 10⁵ seeded random pushes and pops (several
  mixes, and runs of pushes then pops), at g = 2 the copies per operation never exceed 2 (Cormen et al.'s amortized cost
  3 per operation, less the operation's own 1); at the other g, the copies per operation are bounded by one constant for
  every N from 2⁸ to 2¹⁶. *Killed* if either resize lands elsewhere,
  shrinking at 1/g does not thrash, or any sequence breaks the bound.
- **O5, the array's near and far.** With start capacity C₀ and never shrinking below it: for N ≤ C₀ no copying at all
  and the waste (capacity − size) at most C₀ slots (absolute); past C₀, reallocations number ⌈log_g(N/C₀)⌉, one a level,
  and the waste at most a factor g² of the size (relative, g without shrinking). Doubling C₀ shifts the reallocations by
  one level and changes no far-field constant. *Killed* if any count or bound fails.
- **O6, which problems reduce.** Written as a worst case over the unknown future in one ratio r of two amounts:
  ski rental, the cow path and the dynamic array's past/new copying reduce to a reciprocal-symmetric f(r). Predicted
  *not* to reduce: randomized ski rental (e/(e − 1), not at a corner), paging (LRU's k, no sunk-against-committed ratio),
  online bin packing (First Fit's 1.7), and exponential (galloping) search, whose leading cost 1 + 1/log₂ b falls as b
  grows and has no interior corner. *Killed* if one predicted to reduce does not, or one predicted not to does.
- **O7, the time-times-space reason for 2.** For geometric growth without shrinking, copying per element (1 + r) times
  worst waste factor (1 + 1/r), r = 1/(g − 1), is 2 + r + 1/r, least at g = 2. This objective is Claude's choice, not
  the problem's; the test is only of the algebra. *Killed* if the product computed from the simulated array differs.

## The search

A fresh agent, given the three claims (not the predictions), searches for prior statements:
- S1: competitive ratios written as a reciprocal-symmetric function of a sunk-to-committed ratio, or break-even read as
  a fixed point of an exchange.
- S2: the cow path's 9 written in r = (walked before)/(next leg), or b = 2 derived as "each leg equals all before it".
- S3: the additive constant α tied to a chosen unit or scale (a minimum distance, an initial capacity), with the
  additive/multiplicative split read as near/far.
- S4: online algorithms framed as situated observers, or offline/online as writer/reader, in any field.

Predicted before the search: S1 and S2 found in part (break-even and the doubling folklore are common, the symmetric
form in r rarer); S3 found as the definition's α and as "assume distance ≥ 1", not read as near/far; S4 not found.
Each source to be seen in full or marked as seen only as a search result.

## What would follow

If the runs stand and the search does not find the reading: one paragraph in OFS Appendix A, "Online decisions: the
corner and the near field in time" (the corner as the best place to stand, the 2 fixed only by a cost, absolute inside
and relative past, pointing to Proposition 13 and §8), and a section in the CS companion (the dynamic array as a writer
of its past and situated about its future). Not OFS's body: an online algorithm is a reader's decision, and OFS keeps
the reader's acts out of its body (R455). Tom rules.

## Runs

### Run 1 (25 Oct): `runs/onl/onl.py`, output `runs/onl/onl.txt`, 14 s

- **O1 not killed.** Ski rental's worst ratio, scanned over the adversary's stop on a grid of 1/200 that contains the buy
  time, is exactly 1 + max(s, 1/s) at all nine s (1/5 … 5) and the same at s and 1/s; least at s = 1, 2. In whole days,
  buying on day B gives 2 − 1/B and no day does better, for every B from 1 to 50.
- **O2 not killed.** The cow path walked (turn points bᵏ alternating sides, a target just past each turn point): the
  supremum is 10, 9, 10 and 35/3 at b = 3/2, 2, 3, 4, below the formula by 10⁻¹⁰ to 10⁻¹⁴ and never above it; each equals
  5 + 2(r + 1/r), r = 1/(b − 1) = 2, 1, ½, ⅓. Least at b = 2.
- **O3 not killed.** Behind the start the excess walking is exactly 2d₀ for every target nearer than d₀ (2, or 4 at
  d₀ = 2), ahead of it 0; the ratio at x = 10⁻⁹·d₀ is 2·10⁹, unbounded as x → 0. Past d₀ the excess over x stays under
  c − 1 (at most 7.90 against 8 at b = 2, 8.92 against 9 at b = 3). Doubling d₀ doubles the near excess and leaves the
  far supremum exactly as it was.
- **O4 not killed.** Grow at 1 and shrink at 1/g² both land at 1/g, √(1/g²·1), at g = 3/2, 2, 3, 4; in a real run at g = 2
  (4,096 pushes, 4,000 pops) every resize landed at ½. Shrinking at 1/g thrashes: one push–pop pair at the boundary costs
  2N copies, N = 16 … 65,536. At g = 2 the worst copies per operation over every prefix of five mixes of 10⁵ operations is
  at most 1.9993 (start capacity 1) and 1.9956 (16), under 2; the runs of pushes then pops come nearest. At g = 3/2, 3, 4
  the worst per operation settles to 3, 1.5, 1.333 (that is, 1 + r) from N = 2⁸ to 2¹⁶.
- **O5 not killed.** With start capacity C₀ = 8 or 16 and pushes only: up to C₀ no copying and the waste at most C₀; past
  it the reallocations are ⌈log_g(N/C₀)⌉ exactly at every N to 20,000, and the waste factor C/N under g (1.5000, 1.9999,
  2.9998). With shrinking the least load past C₀ stays above 1/g² (0.4445, 0.2505, 0.1116). Doubling C₀ at g = 2 takes
  exactly one reallocation off at N = 17, 100, 1,000, 5,000.
- **O6 killed, by my clause on the array.** Ski rental and the cow path reduce as predicted. The dynamic array's copying
  alone does not: its worst copies per element is 1 + r (3, 2, 1.5 at r = 2, 1, ½), monotone, not the same at r and 1/r,
  so it has no corner and favours a large g. Its corner appears only once the waste factor 1 + 1/r is multiplied in (O7).
  So my prediction folded O7's objective into O6; the array's base is free under copying alone, as OFS says of the levels.
  The rest of O6 stands: randomized ski rental's optimal mixture (buy time with density ∝ eˢ on [0, 1]) has ratio
  e/(e − 1) at every stop T from 0.1 to 10 (to 40 digits), all its buy times inside the corner, so it is not at the
  corner; galloping search's worst comparisons over log₂ i (i to 2⁴⁰) fall as b grows, 2.10, 1.77, 1.70, 1.57, 1.55, 1.54
  at b = 2, 3, 4, 8, 16, 256, with no interior corner. Paging and bin packing were classified by their definitions, not
  computed.
- **O7 not killed.** From the simulated array (pushes only, N to 2·10⁵): copies per element times waste factor is 4.50,
  4.00, 4.50, 5.33 at g = 3/2, 2, 3, 4, against 2 + r + 1/r to 10⁻⁴; least at g = 2. The objective is mine.

**Reading.** The corner holds where a decision trades a sunk amount against a committed one and the future charges for
the larger (ski rental, the cow path): the worst case is one reciprocal-symmetric function of their ratio, least at 1.
Where only one cost is counted (the array's copying, galloping's comparisons) there is no corner and the base is free or
runs to an end; a corner at 2 needs both sides of the exchange priced. The near and far fields hold as predicted in every
case computed: a chosen scale, the guarantee absolute inside it and relative past it, the far constant unmoved by the
scale. All of this is classical arithmetic; what is read is the arrangement.

### The search (25 Oct), by a fresh agent given the three claims, not the predictions

Access: arXiv PDFs read in full through the proxy; the rest seen only as search results. Not reached: Beck and Newman
1970, Karlin et al. 1988 and 1994, Baeza-Yates, Culberson and Rawlins 1993, Gal 1980, Gal and Chazan 1976, Alpern and
Gal 2003, Kao, Reif and Tate 1996, the 2006 SIGACT column.

- **Read.** Chrobak, Kenyon, Noga and Young, "Incremental medians via online bidding", *Algorithmica* 2008 (arXiv
  cs/0504103). Online bidding (bid until a bid reaches an unknown threshold, paying the sum of the bids): deterministic 4
  by doubling, randomized e by a uniform offset on the log scale. Its lower bound uses y = (sum after a bid)/(sum before)
  and needs y²/(y − 1). With y = 1 + 1/r, r = (sum before)/(next bid), that is exactly 2 + r + 1/r (checked here in
  fractions at r = 1/3, 1/2, 1, 2, 3). So the sunk-over-next ratio is in print, but not in the reciprocal form and not
  called a symmetry. Bids are positive integers, s_j ≥ j: the unit enters as an assumption.
- **Read.** Demaine, Fekete and Gal, "Online searching with turn cost", *TCS* 2006 (arXiv cs/0406045). "Under certain
  assumptions, any unbounded optimal search trajectory has to be a geometric sequence" (Gal 1972; Gal and Chazan 1976).
  Geometric trajectories "start with an infinite sequence of infinitesimal steps"; quoting López-Ortiz and Schuierer
  2001, "we assume that a lower bound of one for the distance to the target t is known". With a turn cost d, 9·OPT + 2d,
  the additive term tied to the scale d. "9 for large OPT".
- **Read.** Angelopoulos, Dürr and Jin, "Best-of-two-worlds analysis of online search", STACS 2019 (arXiv 1810.08109):
  "the standard assumption that the target must be at distance at least 1 from O, since no strategy can have bounded
  competitive ratio if this distance can be arbitrarily small"; its Theorem 3 (Gal 1980, Schuierer 2001) is the general
  theorem, with scale invariance F(λX) = F(X) an explicit hypothesis, the optimum then a geometric sequence; infinitely
  many strategies achieve 9.
- **Search results only.** Ski rental's ratio (TR + B)/min{(T + 1)R, B} in lecture notes, break-even best, nowhere called
  reciprocal-symmetric; a multi-shop ski rental case max{b/x, x/b}, the symmetry unnamed; online bounded analysis (Boyar
  et al. 2016) restricting the offline adversary, no standpoint language.

Against the predictions: **S1 found in part** (predicted in part): the ratios standard, the reciprocal form and break-even
as the fixed point of an exchange not found. **S2 found in part** (predicted in part): the cumulative-over-next ratio and
its 2 + r + 1/r in online bidding's proof; the cow path's 5 + 2(r + 1/r) and "each leg equals all before it" as the
reason for b = 2 not found (the cow path's own sources not reached). **S3 found in part, strongly** (predicted: as α and
"distance ≥ 1", not as near/far): the unit's necessity, an additive term tied to a scale, a large-OPT regime are explicit;
a named absolute-inside, relative-outside split not found. **S4 not found** (predicted not found; the search brief).

Missing from my "Known beforehand": **Gal's theorem** (Gal 1972, 1980; Gal and Chazan 1976; Schuierer 2001): with a
scale-invariant cost, the optimal unbounded search is geometric. It is claim 2's first half, in print with its
hypothesis; the claim is classical, ours only as the reading (the reader's dκ/κ is that invariance).

**What is left to us, after run 1 and the search.** Not the corner's numbers, not the levels (Gal), not the unit's
necessity or the additive term. What is not found: (a) the worst case written as one reciprocal-symmetric function of
the sunk-to-committed ratio across problems (ski rental, the cow path, online bidding), with the corner as the exchange's
fixed point and the 2 fixed only when both sides are priced (run 1's O6 kill: one side alone gives no corner); (b) the
additive and multiplicative terms read as the near and far fields of one chosen scale, the same split as a reader's
lay. Both are readings of known results; nothing new is proved. Tom rules on OFS Appendix A and the companion.

