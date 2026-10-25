# FOV: fidelity at the focus, only enough in the fields

*25 October 2026. Tom: "why would readers care that much about the far or near field anyways? we are concerned about
what we are focused on. its highly likely that the corner is constanly adjusted to follow our point of gaze."; "the far
and near fields, are useful as a signal about what to focus on next."; "what we are focused on, we want maximum
possible fidelity. only enough fidelity in the near and far fields to discriminate about where to focus next."; then
"yes, 1,2,3". Exact arithmetic; no data; no page. SPN R495.*

## The question

A reader holds K addresses. It wants the most fidelity it can get on what it is focused on, an extent F about the
gaze, and only enough everywhere else to say where to look next. Which allocation of the K addresses does that, and
where is its corner?

Laid on x, the angle away from the gaze (an eccentricity, a direction: it ends at a fixed angle X, so its extent is known
without any amount). Fidelity at the focus: every cell inside [0, F] at most δ wide, δ as small as possible. Enough to
discriminate: every cell outside the focus, [a, b] with a ≥ F, has b ≤ ρ·a, so a target is located within a factor ρ
(ρ = 2: within a factor of two, which the next look refines).

## Known beforehand

- `plans/neighbours.md` §2: Schwartz's log-polar map, w = log(z + a); Horton and Hoyt 1991, cortical magnification
  17.3/(E + 0.75) mm per degree, so ln(1 + E/0.75): proportional below about 0.75°, logarithmic above. Recorded there with
  Tom's ruling of 8 October: "the human eye is engineering more than fundemental geometry." A neighbour, not evidence.
- DPR, SKT: floats, HdrHistogram and A-law are absolute near zero and relative far (on amounts).
- OFS §8: the turn's cell at s = x/F is (π/2K)(1 + s²)·F wide, relative (π/2K)(s + 1/s).
- Interval covering with a reach b_max(a) nondecreasing in a: the greedy cover from the left is optimal (standard).

## Predictions, before any run

- **F1, the cover.** The fewest cells meeting both conditions on [0, X] is N = ⌈F/δ⌉ + ⌈log_ρ(X/F)⌉ (for
  δ ≤ (ρ − 1)F): uniform cells of δ across the focus, then cells of ratio ρ from F. The greedy cover attains it, and a
  dynamic program on a grid finds no fewer. *Killed* if the DP beats the greedy count on any case tried
  (F = 1, X = 16 and 90, δ = 1/8 and 1/16, ρ = 2 and 3/2).
- **F2, the allocation.** With K fixed the best δ is F/(K − ⌈log_ρ(X/F)⌉): the field costs only the levels, and every
  other address goes to the focus. The corner (the switch from absolute to relative) is the focus's edge F. At ρ = 2,
  X/F = 64: the field takes 6 addresses; at X/F = 90 (a 2° focus on 180°), 7. *Killed* if the optimum puts the switch
  anywhere but F, or the field's count differs.
- **F3, matched grain is the reader's lay.** If the field's first cell must match the focus's grain (ρ = 1 + δ/F, no
  jump at the corner), the field costs ⌈ln(X/F)/ln(1 + δ/F)⌉ cells, within ln(X/F)/2 + 1 of n·ln(X/F), n = F/δ: the
  reader's lay, n in proportion then n per neper, 1 + ln s. *Killed* if outside that bound for n = 8, 32, 128 and
  X/F = 16, 64, 90.
- **F4, against the turn.** The turn with its corner at F and the same K: its widest focus cell (the last before s = 1)
  is between 2.7 and 3.0 times the optimum's δ at K = 64, X/F = 64, ρ = 2 (π(K − 6)/K ≈ 2.85); and it breaks the
  factor-2 condition beyond about s = 2K/π (≈ 41 at K = 64), so inside X/F = 64. *Killed* if the ratio is outside
  [2.7, 3.0], or the turn meets the factor-2 condition all the way to 64.

## What would follow

If F1–F4 stand: the allocation Tom described is exact and simple. Proportional on the focus, levels of ratio ρ past
its edge, the corner at the focus's edge, the field costing log_ρ(X/F) addresses whatever K is. The reader's lay
(1 + ln s) is its matched-grain case. Laid on angle from the gaze the extent X is free, which distance never gave
(SKT). A note (`plans/gaze-note.md`) drafts the OFS paragraph; OFS waits for Tom.

## Runs

*(none yet)*
