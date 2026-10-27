# OFS review 33 (ChatGPT, 27 Oct 2026: a fresh referee review of the "reader holds only H" OFS)

Tom pasted ChatGPT's fresh review of OFS as of 27 October (after review 32's edits). Kept below in substance, each point
with where OFS already stands and what is proposed. SPN R546.

## The review, in brief

- **Verdict.** 8.6/10 overall, 8.8 for the central construction; "suitable for serious external review after a focused
  technical audit"; no further wholesale rewrite.
- **Established.** Address and magnitude are different roles (v/h against (v/h)(V*/H)); the horizon is defined from the
  reader's side (h → 0, no V* needed), a property of the chart, not of a breadth; the half-Cauchy and its median,
  quartiles and missing mean exact; the logarithm conditional on (S), stated as such; uniform area in 3D selected by full
  rotational invariance, the exchange alone not selecting it.
- **The main issue.** Theorem 6(a)'s cancellation holds for the stipulated representation of what arrives (an amount ℓ
  along each direction). Keep three layers apart in its presentation: (1) the mathematical invariance, proved; (2) the
  representational thesis, the paper's interpretation, supported by the construction; (3) whether an actual observer
  instantiates it, empirical and left open.
- **Audit points.** (1) Theorem 6(e): state the density condition in a precise measure-theoretic form; (2) Proposition
  5(d): keep it distinct from a claim that every instrument must have equal axes; (3) Proposition 4: the logarithm
  unique given (S), not from bounded observation alone; (4) the two sweeps: Euclid gives the angles, not that a payload
  sits at the point; (5) "for free" is relative to the chosen structure (the one length, the measure on directions, the
  symmetries), and the abstract and opening sometimes sound more inevitable than the later qualifications allow.
- **Recommendation.** Three changes only: keep the address–payload distinction explicit wherever a proved identity
  meets its interpretation; audit the technical lemmas (the horizon-tail condition, the higher-dimensional measures);
  do not strengthen the empirical claim.

## Response

### Already in OFS

- Layer (3), the empirical question: §12.2's assumptions list ("a reading that disturbs what it reads": Theorem 6(a)
  assumes what arrives is the same whichever address meets it); the introduction's "a real reader may count against
  something else"; "What the result establishes, and what it does not" after Theorem 6.
- Audit (2): Proposition 5(d) is stated for "a page or an instrument with two axes"; Theorem 6(e) and §2 name the other
  weights (a clock, a flat screen, what arrives), each with its own law.
- Audit (3): the abstract, §1 and §6 call (S) "a premise we assume, not derive".
- Audit (4): the abstract ("reading that point as where the payload lands is our interpretation") and §4 ("the theorem
  gives the shared point; that the payload is met there is our reading of it, and a physical application must justify
  that reading on its own").
- The 3D measures: "Why uniformly by area" after Proposition 5(e) says the exchange alone does not select the measure;
  checked in `runs/ofs/wedge_audit.py` (115 checks) and `runs/ofs/depends.py`.

### Proposed (not yet made)

- **R1. Theorem 6(a)'s scope, one sentence after it.** "The cancellation is an identity about this representation of
  what arrives, an amount along a given direction; that the addresses are the reader's is this paper's reading of it,
  and whether a particular instrument's arrivals have this form is a question about that instrument (§12.2)." The
  three layers in one place, where the identity is proved.
- **R2. "For free", made conditional where it first appears.** §1 ("so the sweep is given to every standpoint for free")
  and §2 ("what the geometry gives a standpoint for free"): add "once the one length and the uniform measure on
  directions are granted" at the first, and a pointer to §12.4 ("What the geometry gives free" already separates what is
  free outright from what is free given a premise). No change elsewhere.
- **R3. Theorem 6(e)'s condition, stated precisely.** "If moreover the weight gives h a density bounded away from 0 near
  the horizon" becomes "if moreover the law of h has a density at least f₀ > 0 on some interval (0, δ)", which is the form
  the proof uses (P(h < x) ≥ f₀·x for x < δ), with the path continuous so that v ≥ v₀ > 0 there. The title line and
  §12.2's table already say the same in words.

Not proposed: a technical audit beyond these (the propositions carry their checks in `runs/ofs/`), any new empirical
claim, a rewrite. The CS companion carries R1 and R3 where it states Theorem 6 (its §5).

### Made (27 Oct, SPN R546; Tom: "if you agree, make the small proposed changes.")

- R1: OFS Theorem 6(a), the sentence after it; the CS companion's §5 likewise.
- R2: OFS §1 ("The addresses are given, not performed") and §2's two-sweeps paragraph, conditional on the one length and
  the uniform measure, with the pointer to §12.4.
- R3: Theorem 6(e)'s condition, "the law of h has a density at least f₀ > 0 on some interval (0, δ)", in OFS and the CS
  companion.
