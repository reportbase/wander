# Online decisions and sketches: a writer's things (ONL, SKT)

*25 October 2026. Tom, after SKT run 1 and its search: "the connection to ofs seems unimpressive", "also it seems like a
writer thing not a reader thing", then "remove them from the papers and into a note." SPN R494.*

## Why they are out of the papers

**SKT** (`plans/skt-plan.md`): every sketch tested (DDSketch, HdrHistogram, the lay, the turn) bins a value x, an amount
already stated in a unit, against a chosen H. That is laying amounts: a writer's act, or the payload's, even with the
extent X unknown. A writer missing one amount is still a writer. A reader's reading is a direction, a ratio between
parties [x₁ : x₂], never one value against a unit; a reader's data structure is indexed by direction, as
`wedge-browse.html` and `array-sweeps.html` already are. So SKT put a writer's structure in the reader's column, which is
why the turn did badly there (its horizon cell, applied to amounts, is a cap on a ruler: K4, K6, K7). The family
⌊K·F(x/H)⌋ is in print as a binning theory (circllhist, Hartmann and Schlossnagle 2020); the known-or-unknown universe is
already an axis of quantile surveys. It never entered OFS or the companion.

**ONL** (`plans/onl-plan.md`): the online player knows its prices and counts its costs, all amounts; the dynamic array
is a writer of its past. Each is a writer with one unknown amount, the future. The competitive ratio is unitless, and
in ski rental and the cow path it has the corner's reciprocal form, but that does not make the player a reader. The
levels from an unknown scale are Gal's theorem. The entries below were in OFS Appendix A and the CS companion §6
(SPN R490) and are removed. The demos `online-corner.html` and `dynamic-array.html` stay on the site and in
`demos.html`; nothing in the papers links them now.

What stands: the runs and their verdicts (ONL run 1, SKT run 1 and its search), as recorded in the plans.

## The text removed from OFS, Appendix A

**Online decisions** (§8, §9). An online algorithm decides now without the input still to come; the offline optimum,
which has the whole input, is in the writer's place. Two of the field's patterns are this paper's layout in time. Where
a decision trades an amount already spent against one about to be committed, and the future charges for whichever turns
out larger, the worst case is one function of their ratio r, the same at r and 1/r, and so least at the corner. Renting
skis until the rent paid equals the price of buying is 2-competitive (Karlin et al. 1988): buying once the rent paid is
s times the price has worst ratio 1 + max(s, 1/s). Searching two rays for a point at an unknown distance, each leg b
times the last, has worst ratio 1 + 2b²/(b − 1) = 5 + 2(r + 1/r), with r = 1/(b − 1) the distance walked before a leg
over that leg; it is least at r = 1, b = 2, ratio 9 (Beck and Newman 1970), and online bidding's lower bound carries the
same 2 + r + 1/r (Chrobak et al. 2008). Doubling is break-even taken again at every leg. Where only one side is priced,
as in a dynamic array's copying alone (the entry above), the cost is monotone in r and the factor stays free: the 2 is
fixed only once both sides are. And that a cost unchanged by rescaling makes the optimal search geometric is Gal's
theorem (Gal 1980), the levels of §8 from not knowing the scale. Each such algorithm needs one scale supplied, a least
distance to the target or a first capacity, without which nothing near the start is bounded; within it the guarantee
is an amount, past it a ratio, the additive and multiplicative terms of a competitive bound, as §8's grain is absolute
inside the corner and relative past it. The estimate at the corner of the bounds (Proposition 13) is the same choice
made in size rather than in time.

References removed with it (cited nowhere else in OFS):

Beck, A. and Newman, D. J. (1970). Yet more on the linear search problem. *Israel Journal of Mathematics* 8,
419–429.

Chrobak, M., Kenyon, C., Noga, J. and Young, N. E. (2008). Incremental medians via online bidding. *Algorithmica*
50(4), 455–478.

Gal, S. (1980). *Search Games*. Academic Press, New York.

Karlin, A. R., Manasse, M. S., Rudolph, L. and Sleator, D. D. (1988). Competitive snoopy caching. *Algorithmica* 3,
79–119.

## The text removed from the CS companion, §6

**A writer of its past, situated about its future.** A dynamic array always knows its size, an amount, so of its
past it is a writer; whether it will grow or shrink next, and how far, it cannot know, so of its future it is situated.
That is the online setting: the algorithm decides now, the offline optimum, which sees the whole sequence of operations,
is in the writer's place, and the competitive ratio is the price of standing at now. Three of the field's patterns have
the paper's shape.
- *The shrink band rests at the corner.* Doubling at load 1 and halving at load ¼ (Cormen et al. 2009, the table's
  expansion and contraction) leaves the load at ½ after either resize: the geometric middle of ¼ and 1, one level from
  each threshold. For a factor g, growing at 1 and shrinking at 1/g² both land at 1/g. Shrinking at ½ instead rests on a
  threshold, and a push and a pop alternating there copy 2N elements a pair. Not knowing which way the next run goes, the
  array rests where both are one level away. The symmetry is in levels, not counts: from ½, C/2 pushes reach the growth
  and C/4 pops the shrink.
- *Break-even is the corner.* Where a decision trades what it has spent against what it is about to commit, and the
  future charges for the larger, the worst case is a function of their ratio r alone, the same at r and 1/r, least at
  r = 1. Ski rental, renting until the rent equals the price of buying (Karlin et al. 1988): 1 + max(s, 1/s), 2 at the
  corner. Search on two rays with legs growing by b: 1 + 2b²/(b − 1) = 5 + 2(r + 1/r), r = 1/(b − 1), 9 at b = 2, each
  leg as long as all before it (Beck and Newman 1970); online bidding's lower bound is the same 2 + r + 1/r (Chrobak et
  al. 2008). Doubling is break-even at every step. A dynamic array's copying alone is 1 + r per element, monotone,
  favouring a large g; the 2 appears only when the waste factor 1 + 1/r is priced too, (1 + r)(1 + 1/r) = 2 + r + 1/r,
  least at g = 2. Price one side and the factor is free; price both and the corner fixes it.
- *One scale, near and far.* With the scale unknown, a strategy equally good at every scale steps by a fixed ratio: its
  turn points are levels (Gal 1980). Each needs one scale supplied, the first leg or a least distance to the target, the
  first capacity, and without it nothing near the start is bounded: a target at x just behind the start costs 2d₀ + x
  against x. Inside that scale the guarantee is an amount (2d₀ of extra walking; no copying and at most C₀ empty slots up
  to C₀), past it a ratio (8x; a waste factor g and log_g(N/C₀) reallocations): the additive α and the ratio c of
  ALG ≤ c·OPT + α, as §9's grain is absolute inside the corner and relative past it. The scale is a zoom: doubling C₀
  takes one reallocation off and changes no far constant.

Two pages run these on the public site: a dynamic array as it grows and shrinks under an unknown future
(https://reportbase.github.io/wander/dynamic-array.html), and ski rental and two-ray search at the corner
(https://reportbase.github.io/wander/online-corner.html).

References removed with it (cited nowhere else in the companion):

Beck, A. and Newman, D. J. (1970). Yet more on the linear search problem. *Israel Journal of Mathematics* 8,
419–429.

Chrobak, M., Kenyon, C., Noga, J. and Young, N. E. (2008). Incremental medians via online bidding. *Algorithmica*
50(4), 455–478.

Cormen, T. H., Leiserson, C. E., Rivest, R. L. and Stein, C. (2009). *Introduction to Algorithms*, 3rd ed.,
§17.4. MIT Press, Cambridge, MA.

Gal, S. (1980). *Search Games*. Academic Press, New York.

Karlin, A. R., Manasse, M. S., Rudolph, L. and Sleator, D. D. (1988). Competitive snoopy caching. *Algorithmica* 3,
79–119.
