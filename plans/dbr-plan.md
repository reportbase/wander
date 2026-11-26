# DBR: a Tangent Bridge behind the dial, over a list without end

*26 November 2026. Tom: "In calandar repos, we created dials to browse infinitely large data sets", then, to Claude's
proposal (a bridge behind a dial over an endless list, holding only the K leaves round the needle): "Yes, attach it and
write the plan". The calendar repository was read first (`reportbase/calendar` at 2ea78a2: `README.md`, `dial.js`,
`horizon.html`). Predictions written before any script (`runs/dbr/dbr.py`) exists; not yet run.*

## The dial, as the calendar has it

`dial.js` holds a list of `count` records, or, given a thumb H instead (`horizon.html`), a list with no end: the needle
turns from home toward a horizon it never reaches and the record is H·tan θ = H·sinh ζ, θ = gd ζ. The gold needle is a
rate (ζ grows at tan(gold) × thrust while held), the blue a place; letting go rests the window on the record reached. In
the count's mode the window is span = count^reach records round the needle, a unit the 45° corner, half the window 2^K
units. The turn's heat per record is cos²θ: all of it at home, half at the corner. Within one thumb the records read in
proportion, past it as ratios ("one in 2, 4, 8 …"), and a steady push walks out by a steady ratio. `horizon.html` cuts
the quarter turn into 256 cells, each painted by the first post it meets: "K, not N".

## The question

What can a Tangent Bridge hold behind that dial, over a list with no end, with work that does not grow with how far out
the needle is and nothing that asks for N? Three ways to lay it:

- **L1, the whole list on the turn.** One bridge on x = H·tan t, t in [0, π/2), N leaves at the Cauchy's quantiles
  H·tan((k + ½)π/2N) (`horizon.html`'s cells, R408's addresses). Fixed N, the whole endless list in one hold. This is
  Boyd's rational Chebyshev map of a half-line, known.
- **L2, a window in ratios round the needle.** The window x in [c/ρ, c·ρ] round the needle's record c, mapped by the
  ratio coordinate y = (x − c)/(x + c), which depends only on x/c and is rational (the slope's tangent subtraction,
  turned to the line). On it K leaves at the chord's Chebyshev nodes (the bridge's leaves under the cosine, TB §9,
  generated with no angle: cos from the half-angle slope, (1 − t²)/(1 + t²)), rebuilt by the barycentric formula,
  rational. The window is the dial's far-field window: past the corner ζ ± w is c·e^(∓w).
- **L3, a window in records round the needle.** x in [c − w, c + w] with w fixed in records (the writer's units), the
  same K Chebyshev leaves.

**Content**, made from the address and never stored (the paint, so any arithmetic may make it):
- *ratio content*, its features the same size in ratio wherever it is: f(x) = cos(2π·log₂(x/H)) + ½·sin(2π·1.7·log₂(x/H))
  (one and 1.7 cycles a doubling);
- *size content*, its features a fixed number of records: g(x) = cos(x/H).

## Predictions

- **D1 (exact at its own leaves, everywhere).** L2 at K = 16, ρ = 4, window centres c = 10, 10³, 10⁶, 10⁹, 10¹² thumbs:
  the rebuilt curve equals f at its K leaves to ≤ 10⁻¹².
- **D2 (ratio content at a fixed cost, anywhere).** L2's sup error on f over its window, at K = 24 and ρ = 4, is ≤ 10⁻⁶
  at every centre from 10 to 10¹² thumbs, and the largest and smallest of those errors are within a factor 2.
- **D3 (nothing asks for N or for distance).** In L2 every read does exactly K kernel terms and K leaf values, at every
  centre; the count of operations per read is the same at 10 and at 10¹² thumbs; no length of the list enters (there
  is none).
- **D4 (no angle).** L2's leaves, map and rebuild make zero trigonometric calls (every entry point replaced by a counter);
  only the paint f uses logarithms and sines, and it is evaluated outside the count.
- **D5 (the whole list on the turn holds ratio content only near the thumb).** L1 at N = 256: sup error on f below
  10⁻³ over [H/4, 4H], above 0.3 over [10³H, 10⁴H]; and the N L1 needs for error ≤ 10⁻³ on [H/4, X] grows at least
  ×5 from X = 16H to X = 256H (in t the far field is laid as the reciprocal, H²/x, so a ratio's feature narrows as 1/x).
- **D6 (size content costs with distance in ratios, nothing in records).** On g: L2 at K = 24, ρ = 4 has sup error
  ≤ 10⁻⁶ at c = 10 thumbs and ≥ 0.3 at c = 10³ thumbs (the window holds c·(ρ − 1/ρ)/H radians of g, growing with c);
  L3 at K = 24, w = 4H holds g to ≤ 10⁻⁶ at every centre from 10 to 10¹² thumbs (where the double still separates the
  records; the run states where it stops).
- **D7 (the window, not a cut of a larger bridge).** L2 at K leaves is an exact interpolant of its own window, its
  Lebesgue constant (2/π)·ln K + O(1) (within 10% of the Chebyshev value at K = 16, 32, 64) at every centre; no
  error floor of the kind TB §16 measured for a K-cut of the N-kernel appears (D2's errors fall at least ×100 from
  K = 12 to K = 24).

Each is killed by its own number. Known beforehand, so checks and not discoveries: Chebyshev interpolation on an interval
and its Lebesgue constant; the barycentric formula (Berrut and Trefethen 2004); rational maps of the half-line (Boyd
1987); TB §16's floor for a cut kernel. D2 and D6 are the test of the sorting.

## What would follow, if nothing is killed (a reading, to rule on)

Behind the dial, a bridge laid in ratios round the needle holds content made in ratios to the same accuracy anywhere on
a list without end, at a cost of K and with no N and no angle: the read's own form. Content made with a size (a fixed
number of records) costs more the farther out a ratio window reads it, and is held at fixed cost only in the writer's
units, records counted, which is the write's form. The whole list on one turn (L1) is the in-place lay: fine within a
thumb, the far field folded to the horizon, as the dial's heat says. And the dial's window is a whole bridge of its own,
the K-circle, not a window cut from an N one.

## Runs

