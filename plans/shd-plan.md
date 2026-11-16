# SHD: one shared denominator, against orthogonal axes

16 Nov 2026. SPN R1045. Tom: "Cauchy works on 3d. Does it work on 4d or greater? If so, could be used in AI.";
"But AI dimensions are orthogonal. In observation, they share a denominator."; "Yes, write the plan and run the test".

## The question

In observation every reading is in terms of one thumb: s₁ = v₁/h, s₂ = v₂/h, …, one h under all of them. In an AI
embedding each coordinate is an amount on its own orthogonal axis. Does the shared denominator change what can be read,
and does reading an embedding in terms of the query's own axis keep its near neighbours better than cosine similarity?

## Worked out before any data (exact, recorded here before the run)

Read a candidate x from a query q: h = x·q̂ (along the look), v₁ … v_n the components in any orthonormal basis of the
complement. Then |s| = |v|/h = tan α, α the angle between x and q, for h > 0 (h ≤ 0: behind the look, past the horizon).
So **any reading about the query that treats the n readings alike (a function of |s|) ranks candidates exactly as cosine
does**; the Cauchy heat about the look, (1 + |s|²)^(−(n+1)/2) = cos^(n+1) α, is a monotone function of cosine. A reading
that does not treat them alike (each |sᵢ| ≤ 1, a cube) depends on the basis chosen for the complement, which the query
does not supply. So the proposal "reading in terms of the query's axis keeps more neighbours than cosine" is settled
by arithmetic, not data: it ranks the same. What the framing can do is say why cosine works (it reads a direction,
unmoved by scaling) and test the rest below.

## Predictions (committed before the data are fetched)

Exact or seeded (`runs/shd/shd.py`, part 1):
- **E1.** For parties vᵢ, h independent and identically distributed with finite variance of ln|·|, the log readings
  ln|vᵢ/h| correlate at exactly ½ for i ≠ j (they share −ln|h|); with their own denominators, at 0. Seeded check
  (normal, uniform, exponential; 400,000 draws) within 3 standard errors.
- **E2.** The share with every reading inside the corner (|sᵢ| ≤ 1 for all i) is exactly 1/(n + 1) with one shared h
  (h the largest of n + 1 exchangeable parties) and ½ⁿ with own denominators. Seeded, n = 1 … 8, three laws, within 3 SE.
- **E3.** On the data: ranking by |s| in the query's frame equals ranking by cosine for every candidate with h > 0
  (Spearman 1 to 10⁻¹²).

On real data (part 2): GloVe 50d (Wikipedia + Gigaword, 400,000 words; gensim-data release, PDDL), two human
similarity lists (SimLex-999, WordSim-353, from the eval-word-vectors repository's copies). Measures for a pair (a, b):
M1 cosine; M2 Euclidean distance (an amount, no denominator); M3 |s| in a's frame (shared denominator, E3);
M4 own denominators: the median over coordinates of |ln|bᵢ/aᵢ|| (each axis its own h).
- **D1.** M1's Spearman with the human ratings exceeds M2's on both lists.
- **D2.** Scale every word vector by its own random factor e^U, U uniform on (−2, 2) (scaling each thing, seeded):
  M1 and M3 unchanged to 10⁻¹²; M2's Spearman falls by at least 0.05 on both lists.
- **D3.** M4 (own denominators) scores at least 0.05 below M1 on both lists.
- **D4.** Embedding directions are not the uniform hemisphere: over 1,000 seeded query words, the mean share of the
  vocabulary within 45° of a query is at least 10 times the uniform hemisphere's share in 50 dimensions (the regularised
  incomplete beta I(½; 49/2, ½)). Kill if under 10 times.
- **D5.** Removing the mean vector (centring) at least halves D4's share.

Kill conditions are the predictions' own thresholds. A failed prediction stays failed; a fix is a new run with its own
prediction.

## Runs

(none yet)
