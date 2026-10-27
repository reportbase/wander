# OFS review 35: Gemini, a skeptical referee's read (27 October 2026)

Pasted by Tom. Four points on OFS as of review 34, recorded in brief, then the response and what was made.

## The points, in brief

1. Appendix A's Cayley entry: −e^(2iθ) checked at zero, the corner and the horizon (−1, −i, +1); against §4's
   ½e^(2iθ) (+1, +i, −1) a half turn. Gemini's own conclusion: no error.
2. Two missing citations: the 1853 Cauchy–Bienaymé exchange (Stigler 1974 is in the references but not cited there),
   and Euler's formula (Euler 1748 not listed).
3. §6's opening: x is introduced as a far reading v/h, then as x = d/H, the far amount in H; a referee would ask where
   d came from before §9. Clarify which x the lay places.
4. Proposition 3(g) derives the inner product for two unit relations; does it hold for three (the sphere)? Gemini: yes,
   any compact subgroup acting transitively preserves a quadratic form unique up to a factor (Weyl's averaging); one
   clause after 3(g).

## Response

1. Nothing to fix; the entry already says "turned a half turn".
2. The 1853 claim needs its source; Stigler (1974) is already listed. "Euler's formula" is a standard name and needs no
   citation.
3. Real. Review 30 put (S) on x = d/H but left the opening sentence on v/h.
4. Worth a clause, with a condition Gemini's version leaves out: the group the sweeps generate must be compact
   (bounded). Each sweep returning on its own is not enough. Two sweeps that each return, each in its own inner product,
   can compose to an unbounded map: a turn from h to v and a turn from h to v₂ in a sheared measure give, composed once
   each, a step with an eigenvalue of 39.67, its tenth power of norm 10¹⁶ (`runs/ofs/compact.py`). With a shared inner
   product the composition stays a rotation.

Proposed G1–G3; Tom: "yes".

## Made (R548)

- **G1** Appendix A, "Cauchy's functional equation, twice": "his exchange with Bienaymé in 1853 (Stigler 1974)".
- **G2** §6's opening: the lay places a far amount x = d/H ≥ 1, a distance in units of H, which a reader has only from a
  second standpoint or an amount carried in (§9); the reading v/h does not change with H. The second paragraph's
  restatement removed.
- **G3** After Proposition 3(g): with more unit relations the same holds if the sweeps together stay bounded (a compact
  group); an inner product averaged over its Haar measure (Haar 1933) is preserved, unique up to a factor when the group
  carries every direction to every other, as the sphere's turns do; sweeps each returning in their own inner product can
  compose to a map that grows without bound. Also in the CS companion.

No result changed.
