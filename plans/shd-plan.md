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

**Run 1** (16 Nov, `runs/shd/shd.py`, output `runs/shd/shd-run1.txt`; data sha256: glove50.gz
5c55f98957aa9fed8d2ac5fb1dcff57af3b23c5a3ee7af3f7945f8d49198eb24, simlex.txt
405394ffb7d25f6d0e3c041f87c9f27d29dc6b047506769953e85c4523b11685, ws353.txt
ce12919b240af45bdf46d243601eaca2b6212b159b5e7e9b435ee7ee40c5619c; not committed).
- E1 killed by my standard error: the exponential law's shared correlation 0.4961, outside my normal-theory 3 SE
  (0.0036). Post hoc, 200 seeded repeats give mean 0.49999 and spread 0.00135, wider than the 0.00119 I assumed
  (the log of an exponential is skewed). Normal 0.5015, uniform 0.4968; own denominators 0 within error for all three.
- E2 not killed: 1/(n + 1) shared and ½ⁿ own, every law, n = 1 … 8 (n = 8: 0.110 against 0.0038).
- E3 killed by my tolerance: Spearman(|s|, cos) 0.999999997 and 0.99999993. Post hoc both lists hold duplicate pairs
  (one in SimLex, two in WordSim); their cosines are equal to the last bit and their |s|, read in the two words' frames
  in turn, differ in the last bit, so two ranks split a tie. No other rank differs.
- D1 killed: on SimLex-999 Euclidean distance (0.2758) beats cosine (0.2646); on WordSim-353 cosine leads (0.5033
  against 0.4636). In GloVe 50d a vector's length carries something SimLex's ratings follow.
- D2 killed by my tolerance, in the |s| clause only (it moved by 5·10⁻⁸ on SimLex, the same duplicate ties). Cosine
  unchanged to 10⁻¹²; Euclidean fell 0.2758 → 0.0589 and 0.4636 → 0.1486 when each word was scaled by its own factor.
- D3 not killed: own denominators 0.1919 and 0.2375, against cosine 0.2646 and 0.5033.
- D4 not killed: 4.4·10⁻⁴ of the vocabulary within 45° of a query, 6.7·10⁴ times the uniform hemisphere's 6.6·10⁻⁹.
- D5 not killed: centring brings it to 1.9·10⁻⁴ (0.43 of raw), still 2.9·10⁴ times uniform.

**Run 2** (predictions written before it runs, same data and seeds as run 1):
- E1′: each law's shared correlation within 3 of its own spread over 200 seeded repeats of 400,000 draws, the mean of
  the 200 within 3·spread/√200 of ½; own within the same of 0.
- E3′, D2′: readings rounded to 12 significant figures before ranking (so last-bit ties are ties); then
  Spearman(|s|, cos) on pairs in front is 1 to 10⁻¹², and |s|'s and cosine's Spearman with the ratings move by under
  10⁻¹² when each word is scaled by its own factor, Euclidean's falls by at least 0.05. D1 is not rerun: it stays killed.
