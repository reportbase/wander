# OFS review 30: a fresh referee review of version 42 (ChatGPT, 26 October 2026)

*Pasted by Tom: a referee review of version 42, dated 23 October, like review 29's. Its points kept in substance, then
Claude's response and what was made (SPN R526).*

## The review's points

- 7.8/10; mathematical core 8.5, conceptual contribution 8.2, argument and assumptions 7.5, technical precision 7.0,
  readability 6.5. "Revise targeted claims, then seek external mathematical review"; not a relabeling of the Cauchy.
- Established: the reciprocal corner; the half-Cauchy from a uniform turn and its octant extension; Theorem 6(e)'s split
  of median, missing mean and exact shape; Proposition 4 conditional on (S), assumed and said so; Propositions 8, 11 and
  the mountain example.
- Scope: within the construction the Cauchy is the measure the uniform turn induces on the addresses; not a
  reclassification of every Cauchy-distributed quantity (§7.2, §7.8 say so; some phrasings outrun it).
- Issue 1 (correction): Proposition 12's "exactly, however close they are" overstates; total, centroid and spread are
  exact, but the higher moments carry the arrangement, and a blend of shifted kernels is not one kernel at the centroid.
- Issue 2: §6 defines x = v/h, then says a change of H multiplies the far readings; v/h does not change with H, d/H does.
- Issue 3: Proposition 3(g)'s scope wherever summarized (given the linear periodic sweep).
- Issue 4: "payload" shifts between the landing point on the Thales circle and the value there: use address, landing
  point, payload.
- Issue 5: a fixed K is a model of capacity, not supplied by the geometry.
- "A Cauchy variable is never an amount" contextual; "given before anything arrives" a premise of the model; reading and
  writing the paper's categories. Lighthouse excellent, the octant strong, Mercator and spectral lines with boundaries.
- Readability: less repetition; the theorem/interpretation boundary visible in abstract, introduction and conclusion.

## Response (Claude)

Made (Tom: "yes"):
- Issue 1. Proposition 12's paragraph now says the total and the centroid are exact; the arrangement enters the spread
  at (Δ/σ)² (w(1 − w)Δ²) and the third and higher moments at higher powers (the pair adds w(1 − w)(1 − 2w)Δ³ to the third
  central moment, checked); one payload at the centroid is an approximation, good to second order in Δ/σ. "The two
  centres" now says the arrangement arrives through the spread and the higher moments.
- Issue 2. §6 names the variable of (S): x = d/H, the far amount in units of H, which the lay places; v/h does not change
  with H. Proposition 4 unchanged.
- Issue 4. §4 "The address points at the payload" names three terms, address, landing point P, payload; the point
  ½(h² − v², 2hv) is "the landing point", its height a coordinate of it, not an amount of the payload.
- Issue 5. "A fixed count, aimed by H" says the turn's addresses are continuous and a fixed K a model of finite capacity
  added to them; what follows holds for any K.
- §7.2's rule: "In this construction it is never an amount."

Already met: issue 3 (review 29's uniqueness sentence and §5's scoping; §12.2 question 1, Appendix A conditional); the
abstract marks its interpretations (R462); §12.2's "What depends on what"; Mercator presented as a chart keeping
bearings, not descended from the model; spectral lines bounded in §7.2 and §7.8.

Declined: removing repeated statements of the main result (the tightening pass made; R203).
