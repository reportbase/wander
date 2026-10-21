# OFS review 23: ChatGPT's mathematical stress test (of version 38)

*21 October 2026, 08:35 MDT, from Tom, pasted without comment. ChatGPT pushed on six places where a valid result might
read as a stronger claim, and asked for a line-by-line audit of the higher-dimensional extension.*

Its verdict: the strongest core is the reciprocal corner, the uniform-turn-to-Cauchy derivation and the separation of
the address map from the payload; the risks are scope and inference (a conditional result read as a necessity, an
interpretation read as a theorem's cause). Its points, checked against the text, and what was done with each:

| Point | Checked | Made |
|---|---|---|
| 1. Does the Cauchy require V = H? Print the unequal-breadth calculation in the proof. | Already printed: 5(d)'s proof takes θ′ uniform in the drawing's directions, tan θ′ = c·(v/h), P(v/h ≤ r) = (2/π)·arctan(cr), median 1/c. ChatGPT's own calculation is the other parameterisation (uniform in the sweep's parameter, the drawn ratio c·tan t, median c). | One sentence added to the proof: read on the page as the drawn ratio, with the sweep uniform in its own parameter, the median is c, again the law of (b) only at c = 1. Both readings now in the proof. |
| 2. The uniform turn is selected by the stated ignorance, not by ignorance alone; separate invariance, model choice and behaviour. | The abstract and §2 already state the premises (the chosen ignorance, the sweep a rigid bar's turn) and §11.2 question 6 keeps behaviour open; but "the principle gives the uniform turn" could read as unconditional. | Abstract and §2: "selects the uniform turn for that stated ignorance"; §2 adds "other observers may count other measures; §11.1". |
| 3. Reciprocal symmetry gives the median; the missing mean needs a tail condition; the uniform turn gives the exact Cauchy. Keep the three apart everywhere. | Theorem 6(e) states the condition (h's density bounded away from 0 near the horizon); the introduction said "if it reaches the horizon, has no mean", which is weaker than the theorem. | The introduction now names the three results separately, "if its weight also stays above zero at the horizon"; 6(e)'s title and §11.2's three-path paragraph say the same. |
| 4. State address invariance formally; keep amount non-invariance (V*/H) beside it; the Cauchy lacks a mean because its tail diverges, the address reading interprets that, it does not cause it. | The introduction, §7.2 "The rule, and a test" and the hand's list said "has no mean because …" with the interpretive reason. | Each now gives the divergence first and the interpretation after ("Read in this paper's terms, that is no loss …"). Theorem 6(a) adds the formal statement (the law of the addresses is independent of the payload assigned to them) and the ratio of amounts (V*/H)·(v/h), which keeps V*/H. |
| 5. The logarithm is conditional on (S); the join at the corner is not fixed by reciprocity. | Already so: (S) is stated as a premise, "assumed, not derived", and the paragraph after Proposition 4 says a fixed corner and a matched slope are not enough. | No change. |
| 6. Parallax: recoverability, not a guarantee; occlusion, correspondence, baseline, scale. | The introduction's "places the whole at V*/H" was unqualified; Proposition 11 and §9's visual hull carry the limits. | The introduction now places "what both standpoints see and can match, while its parallax stays above the reader's resolution; hidden faces and unmatched points stay unplaced". |
| Audit the higher-dimensional extension (indexing, normalisation, marginals, the event "near in all", 1/(n + 1)). | Done by a fresh agent, `runs/ofs/wedge_audit.py` (+ `.out`), mpmath at 30 digits, n = 1 … 5: 115 checks pass (normalisation two ways, the gnomonic area element by a Gram determinant, every single and pair marginal, the near field 1/(n + 1) from the density, the number past the corner uniform on 0 … n, 0.3426 and 0.2326 for the sweep uniform in both angles). Found: (i) n means unit relations in 3(d) and other parties in "More parties", so 2ⁿ orthants read across is off by 2; (ii) "More parties" uses the sphere of n + 1 unit relations without citing 3(e)–(f) per pair; (iii) 1/(n + 1) needs the exchange to keep the measure, not only the orthant (pair corners alone do not give it: half the weight on the chamber v₂ > h > v and half on v > h > v₂ keeps every pair's corner and never has h the largest). | (i) 3(d), its proof and "What the geometry needs" now use m for unit relations; (ii) "More parties" cites 3(d) with m = n + 1 and 3(e) per pair, the sphere in n + 1 dimensions, 2^(n+1) orthants; (iii) the exchange is an isometry keeping the orthant and its area, with the counterexample in one sentence; 5(e)'s proof "keeps the octant and its area". |

Its closing recommendation (mark each claim derived, conditional, interpretive or empirical) is the paper's practice in
words rather than marks; OFS keeps no standing marks (SPN R202).

## Follow-up (21 October, 10:06 MDT)

ChatGPT then read the audit (`runs/ofs/wedge_audit.py`, `.out`) and asked one question: is the uniform area on the orthant
derived from the observer's stated principles, or does it enter as an axiom? It noted it had read the audit's text and
outputs, not run the script; the script was run here (all 115 checks pass) and was written against the paper's current
propositions.

Checked: 5(e) stated the uniform area as its hypothesis and contrasted the sweep uniform in both angles, but did not say
where the measure comes from. It comes from the same premise as the circle's uniform turn: the reader's attitudes are the
turns of one rigid bar, treated alike. With three unit relations those turns are the rotations of the sphere, whose only
invariant probability is uniform area (the invariant measure of a compact group acting transitively is unique; Haar 1933);
its restriction to the octant is (e)'s law, and likewise in n + 1 dimensions. The parties' exchanges alone do not fix it
(a finite group; the audit's counterexample shows pair corners do not either), and the two angles uniform is a chart, not
the group's measure.

Made: OFS "Why uniformly by area", after 5(e)'s proof: the measure selected by the stated ignorance, as the uniform turn
is; not forced by bounded observation alone.

ChatGPT's reply (10:13 MDT): agreed; asked that "treated alike" be stated as invariance under the full rotation group, not
only the parties' exchanges or chosen angles, and that the premise be visible as a choice about ignorance (uniqueness of
the invariant measure does the rest, but does not prove a reader must adopt it); an observer weighting attitudes
otherwise implements another law, not a wrong one. It withdrew its "not run" caveat. Made: both, in the same paragraph.
