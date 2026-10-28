# Review 39: a second fresh referee read, for a foundations of probability journal (28 October 2026)

A new agent read the revised `papers/ofs-submission.md` alone, as a referee for a foundations of probability or
philosophy-of-probability journal, without the first report: major revision, 4/10, every number recomputed correct.
Review 38's main errors (the corner, address statistics, averaging, 8(c), the landing point) did not recur. Tom: "yes, go
with your recommendations". OFS first, then the submission and the CS companion (R421).

## Response

Made:
- *Uniform in what* (its finding 1, Bertrand): a paragraph after "Working back from the Cauchy" in OFS and the
  submission. For the reader the parameter is the flow's t (Proposition 3(g), the submission's 3(e)), in whose inner
  product (h, v) = (cos ωt, sin ωt); the c = 2 laws (0.207/0.5/1.207 by the page's angle, 0.316/0.739/1.673 along the
  curve) are uniform in parameters a writer's page adds. The exact law is forced given 3(g)'s premises; whether a
  reader's sweep is such a flow is the open question.
- *What kind of measure this is* (finding 2): the address law is Jaynes's (1968) invariant measure m(x), the reference
  measure of his continuous entropy, neither belief nor frequency; observed readings have a law that depends on what
  arrives, the reference does not. OFS §2, the submission §2, the CS companion's "What we build on".
- The submission's abstract: the law the group's invariant measure, a reference measure in Jaynes's sense; the
  cancellation "by construction" (finding 3).
- Related work (OFS §12.3, the submission's Related work): van Fraassen 1989, Marinoff 1994, Shackel 2007, Seidenfeld
  1979, Kass and Wasserman 1996, with Jaynes's use stated as conditional in their sense.
- The rule "a Cauchy variable is a direction" offered as a reading, not a test (OFS, submission, CS companion); "Jaynes's
  normative sense" narrowed to a conditional (submission, CS companion).
- Smaller: Proposition 2(b) on (0, ∞); the submission's K address boundaries k = 1 … K − 1, the last address to the
  horizon; the outside pivot in the submission; 0.6368 the half turn's (0.6367 over a quarter); the relay sentence
  spelled out; the straws as in OFS.

Not taken: the rescaling "idle" (it gives the estimate's median under a proper law); Bertrand from a point "reopening"
Jaynes (that is the result: from a standpoint the answer depends on D, tending to ½); 3(c)'s circularity and 3(e) step
1's diagonalisation, "home" as both reading and point, 5(b)'s converse, Proposition 7's orientation (the frame is now in
(b)), notation and typographic items: left for the typesetting pass. Review 38 already answered "the product returns the
1" and the rule's falsifiability is now marked as a reading.

## The report

# Referee report: "Addresses Given, Payloads Met: The Cauchy distribution as the geometry of a situated reader"

Venue: foundations / philosophy of probability. I read only the manuscript (`papers/ofs-submission.md`). I recomputed the numbers with mpmath and numpy; the script is `check.py` in the scratchpad directory.

---

## 1. Summary and recommendation

**Claimed contribution.** The paper models a "situated reader" that holds one length H and reads directions [h : v] in a quadrant. Its group of ignorance is taken to be turns, rescalings of the other party's size, and the exchange h ↔ v. In Jaynes's manner it takes the invariant measure: uniform in angle, so the readings v/h are half-Cauchy, with the median at the "corner" v = h. It then reads this measure as the reader's *addresses* (where readings can be put), not as a probability over *payloads* (what arrives). The "main result" (Theorem 5) says:

- the reach of an arrival cancels from a ratio;
- order statistics commute with increasing maps and means do not;
- the median sits at the corner under any exchange-symmetric weight;
- the missing mean needs a weight that does not vanish at the horizon.

Supporting results cover a derivation of the circle from a periodic linear flow, Thales/III.20, scale non-identifiability, and a logarithmic layout from a scale-invariance premise.

**Assessment.**
- Every proposition I checked is correct, or correct after small repairs. Every number I recomputed matches.
- The mathematics, however, is almost entirely classical and elementary, and the paper says so ("The theorem is elementary; its content is the reading").
- So the contribution stands or falls on the interpretive claim: that the Cauchy "is the address, not the payload", and that this follows from a Jaynesian group. For this venue that claim is not yet made precise enough to evaluate.
  - The status of the "law of the addresses" is never fixed. It is not a degree of belief and not a frequency, yet it is fed medians, means and finite samples.
  - The pivotal "cancellation" (Theorem 5(a)) is a tautology about ratios.
  - The paper never confronts the Bertrand-type question it raises itself: uniform *with respect to which parameter*? Section 3 below shows that three different "uniform" measures appear in the text at c = 2 and give three different laws.
  - The engagement with the critics of transformation-group priors is thin. Drory and Norton get a sentence each. Van Fraassen, Shackel, Marinoff, Seidenfeld and the reference-prior literature are absent.
- The idiolect (reader, writer, home, zero, corner, lay, payload, "all of h") raises the cost of reading considerably, and two terms clash outright (Section 4).

**Recommendation: major revision. Score 4/10** for this venue. The geometry is clean and the interpretive idea is interesting. As a philosophy-of-probability contribution it needs a precise statement of what an "address law" is, an honest treatment of parametrisation dependence, and serious engagement with the Bertrand and Jaynes-critique literature.

---

## 2. Mathematical errors and checks

No proposition is false as stated in a way that breaks the paper. The items below are ranked by severity. Recomputed values that agree are listed at the end.

**M1. Prop. 3(c), proof: circular norm argument.**
- Text: "h² + v² = 1 when length is Euclidean, and the Euclidean norm is, up to scale, the only norm preserved by every turn."
- Problem: "turn" (rotation) is defined *by* the Euclidean inner product, so the clause is circular. It is true only if "turn" is first defined abstractly, as an element of a compact one-parameter group carrying h to v.
- Fix: delete the clause and rest (c) on (e). Alternatively define turns abstractly before invoking uniqueness.

**M2. Prop. 3(e) makes c = 1 automatic, which undercuts 4(c) and "Working back".**
- Under (e), for *any* continuous linear flow with Φ(T/4)e_h = e_v that returns at T, the coordinates of Φ(t)e_h in the basis (e_h, e_v) are exactly (cos ωt, sin ωt). This holds whatever ellipse the flow traces on some "page".
- So a measure uniform in the flow parameter t gives v/h = tan ωt, the exact half-Cauchy, with no c anywhere.
- The c ≠ 1 cases of 4(c) and "Working back" use different measures:
  - 4(c): uniform in the drawn angle θ′. At c = 2 the quartiles are 0.207, 0.5, 1.207, a reciprocal pair about 1/c.
  - "Working back": uniform in arc length along the stretched curve. I confirm the stated quartiles 0.316, 0.739, 1.673.
- That is three measures and three laws for "one sweep". This is exactly Bertrand's/Drory's point.
- Fix: state explicitly which parameter carries the uniform measure in each of 3(e), 4(b), 4(c) and "Working back". Say plainly that the Cauchy follows from "uniform in the flow's own parameter", and that c only enters if uniformity is imposed in a different, external parameter. Then 4(c) is a statement about mixing measures, not about the reader.

**M3. Prop. 3(e), step 1: incomplete argument.**
- "A real 2 × 2 matrix with exp(TA) = I has eigenvalues ±iω … A pair of zero eigenvalues would make A nilpotent." The cases need to be closed properly:
  - exp(TA) = I forces A to be diagonalisable over ℂ, since a Jordan block gives e^{Tλ}(I + TN).
  - Every eigenvalue satisfies e^{Tλ} = 1, so a real eigenvalue must be 0.
  - For a real matrix this leaves A = 0 or a conjugate pair ±2πik/T.
  - "Least T" then gives k = 1 only after rescaling. If minimality is placed on T, the eigenvalues are ±2πi/T.
- Fix: replace the step with this argument (three lines).

**M4. §9, "A fixed count, aimed by H": the last address is at infinity.**
- Text: "the K addresses lie along distance at H·tan(kπ/2K), k = 1, …, K."
- At k = K this is tan(π/2) = ∞, so the last address is at infinity. The claim "half of them inside H" counts k ≤ K/2 and needs K even.
- Fix: use k = 0, …, K−1, or (k − ½)π/2K. State K even, or say "⌊K/2⌋".

**M5. §7: the pivot claim is proved only for interior pivots.**
- Text: "These are the only two kinds of pivot from which equal turns cut equal arcs".
- The 2t/(t + t′) computation (correct, and I verified it) covers pivots inside the circle and on it. Pivots outside the circle are not treated, so "only" is unproved for them.
- Fix: add the exterior case (each ray meets twice, so the near and far arcs must be distinguished), or restrict the claim to "pivots in the closed disc".

**M6. §6, "Once a Cauchy…": the relay sentence is garbled.**
- Text: "a uniform turn from height γ₁ + γ₂ landing at height γ₂ and turned again, which lands as one turn from height γ₁ + γ₂."
- As written, the start and the conclusion are the same, so the sentence asserts nothing. Presumably it means: a turn about a point at height γ₁ above a line at height −γ₂ lands at that line, and turning again from there lands as one turn from height γ₁ + γ₂.
- Fix: rewrite as a precise statement, e.g. via the harmonic-measure or Brownian-motion composition, or drop it.

**M7. Theorem 5(b), converse: vacuous for unlabelled sets.**
- Text: "two sets with the same ranks are carried onto one another by some strictly increasing f."
- Any two finite sets of distinct reals with the same cardinality are order-isomorphic, so "same ranks" adds nothing.
- The meaningful statement is for *labelled* samples or vectors (x₁, …, x_n): the maximal invariant of the group of increasing maps acting coordinatewise is the rank vector.
- Fix: state it for indexed samples, in maximal-invariant language.

**M8. Prop. 2(b): domain.**
- f is defined on [0, ∞), but the condition f(1/x) = 1 − f(x) needs x > 0.
- Fix: (0, ∞), with f(0) = 0 by continuity if wanted.

**M9. Prop. 8(a): unit not stated.**
- "Worst error ½·log(V₊/V₋)" should be ½·log₂(V₊/V₋), since f = log₂ was just fixed.

**M10. "Why a turn and not a boost": "the Cauchy" should be "a Cauchy".**
- An elliptic one-parameter subgroup of PSL(2,ℝ) fixes some z in the upper half-plane. Its invariant probability is the Cauchy with parameter z.
- Fix: "a Cauchy law, the one centred at the flow's fixed point".

**M11. §8 "Ratios suffice" / Prop. 7(b): an unstated condition.**
- Prop. 7(b) requires "placement relative to each other … known up to scale, … directions in one frame". This is a substantive, non-ratio input: the relative orientation of the two standpoints.
- The worked example (§10 step 6) assumes the walk is straight toward the range's middle.
- Fix: say that orientation is carried in alongside the one amount.

**Numbers recomputed (all agree):**

| Claim | Recomputed value |
|---|---|
| Quartiles √2 ∓ 1 | ✓ |
| ∫ x·2/(π(1+x²)) = (1/π)ln(1+s²) | ✓ |
| 4(d) marginal | ∫₀^∞ ds₂/(1+s²+s₂²)^{3/2} = 1/(1+s²) ✓ |
| Z_n normalises on the orthant | n = 1, 2, 3 ✓ |
| Six chambers, h largest | ⅓ by Monte Carlo ✓ |
| Uniform in altitude and azimuth | near field 0.2326 ✓; P(v ≤ h) = 0.3426 |
| sin²2θ weight | mean 4/π ✓ |
| Three-path table | 0.250/0.293/0.207 and 0.750/0.707/0.793 ✓ |
| Per-decade growth of the truncated mean | (2/π)ln 10, ln 10, (ln 10)/2 ✓ |
| Level chart | (1/π)sech ξ ✓ |
| Gudermannian identity | ✓ |
| Turn per doubling | 18.43°, 12.53°, 6.91°, 3.55°, 1.79° ✓ ("3.5" is rounding of 3.549) |
| In-place lay | 2^(−j) ✓ |
| Bertrand share arcsin(R/2D)/arcsin(R/D) | ⅓ at D = R, 0.483 at D = 2R, ½ in the limit ✓ |
| θ/sin θ at 45° | 1.1107 ✓; sin θ/θ = 0.9003 ✓ |
| §10 step 6 | arctan(10/9) = 48.01° ✓; d = 10, V* = 20 ✓; log₂ 20 = 4.32 ✓ |
| §10 step 3, 36 midpoints | 0.6368 over the **half** turn (0.6367 over the quarter turn). The text should say which. |
| Cayley transform | (tan θ − i)/(tan θ + i) = −e^{2iθ} ✓ |
| Central point | ½(h+iv)², foot h², height hv ✓ |
| Pivot rate | 2t/(t+t′) ✓ |

---

## 3. The argument

**A1. What is the "law of the addresses"? (most serious)**
- The paper reads Jaynes's invariant measure "as the reader's addresses, not belief" (§1, §2, §11). It then applies medians, means, quartiles, finite "sets of readings" and Jensen to it.
- A skeptical philosopher will ask: a law *of what random quantity*, under *what* interpretation of probability?
  - If addresses are "given whole, not performed", there is no sampling, and "the mean does not exist" is a statement about the integral ∫ x dμ of a measure, not about any reader's expectations.
  - If, instead, readings are drawn (Theorem 5(b), (c) speak of finite sets X), then the drawing mechanism is the payload's: where sources are and how often they arrive. The paper itself concedes this in "a count against something other than the turn" breaking the family.
- The paper needs to commit:
  - either (i) the address measure is a reference measure (a base or dominating measure, like Lebesgue measure on a chart), and Theorem 5 is about it;
  - or (ii) it is a probability, with an interpretation.
- Under (i), most of the thesis reduces to the standard decomposition "density = (payload density) × (reference measure)", which is well known in the Jaynes literature: the invariant measure as the m(x) of the continuous entropy H = −∫ p log(p/m), Jaynes 1968 §§6–7.
- The authors should engage that connection. It is the closest classical analogue of "address vs payload" in Jaynes's own work and is not mentioned.

**A2. Theorem 5(a) is a tautology presented as the main result.**
- "(ℓ·v)/(ℓ·h) = v/h" holds by construction. The authors say so: "(a) holds by construction".
- Yet the abstract builds on it: "Following Jaynes's principle … this law is the turn's own: whatever arrives along a direction cancels from its reading".
- The Jaynesian group does not imply the cancellation. The cancellation is a property of homogeneous coordinates.
- Also, the *distribution* of observed readings is not invariant to what arrives. It depends on which directions receive arrivals. Only the reference measure is invariant.
- Fix: separate (a) "a reading is a projective point and is invariant to the scale along the ray" from "the reference measure on readings is fixed before data". Do not present either as following from Jaynes's principle.

**A3. Parametrisation dependence is the Bertrand problem, and the paper doesn't face it.**
- As M2 shows, "uniform turn" is uniform in a chosen parameter.
- The paper's answer to Drory (§11 Q2) is that the median survives any exchange-symmetric choice. True (Theorem 5(e)), but this concedes that the *Cauchy* is not determined by the stated ignorance unless one adds full rotation invariance.
- Full rotation invariance is not part of a reader's ignorance on a *quadrant*. The quadrant is not invariant under turns; the paper restricts the circle's measure to it. Why should a reader confined to a quadrant be ignorant under rotations that leave it?
- The paper should argue this, or weaken the thesis to "the median at the corner is forced, and the exact Cauchy is one choice".

**A4. The choice of group is doing the work.**
- "The group is chosen, not derived" (§2) is honest. But then "the geometry is therefore necessary relative to a stated ignorance" (§11) is close to "assume the conclusion's symmetry, get the invariant measure".
- Critics anticipate this objection: van Fraassen (*Laws and Symmetry*, 1989) on the arbitrariness of choosing the group, Shackel (2007) and Marinoff (1994) on Bertrand, and Seidenfeld (1979) on objective Bayesianism.
- The paper should explain why turns + rescalings + exchange is the right ignorance for a "situated reader", and especially why the exchange is justified when h refers to the reader's own length and v to the other's. Those roles are asymmetric by the paper's own setup; (P0) asserts they are not.

**A5. The rescaling component is idle.**
- κ ↦ λκ "touches no reading". Its Haar measure dκ/κ "has no median and gives no estimate" (Prop. 8(c)). The estimate comes from bounds or from a proper symmetric law instead.
- So the scale part of the group plays no role in any proposition. Prop. 8 is plain decision theory under absolute or level loss.
- The paper should say this, or show where dκ/κ is actually used. The §11 Q4 marginalisation remark is the only place, and it is a citation of Jaynes 1980.

**A6. Bertrand, as treated in §2, undercuts Jaynes rather than extending him.**
- Removing translations re-opens Bertrand: the answer now depends on D.
- Citing an experiment (Liu & Adams) as "consistent" is a category error for a question about which measure is the right one. Empirical straw tosses test a physical mechanism, not a principle of indifference.
- Fix: present the D-dependence as showing that the "situated" group does *not* single out a unique answer to Bertrand. Drop the empirical support claim, or say exactly what it shows.

**A7. The "normative sense" claim (§11 Q3).**
- Text: "That a reader *should* sweep by a turn of its one length … is what the propositions show, in Jaynes's normative sense."
- The propositions are conditionals (if the sweep is linear, periodic and carries h to v in a quarter period, then …). They show no "should".
- Fix: state it as a conditional, or give the normative argument: why a rational reader adopts exactly that group.

**A8. "Address" vs "payload" vs domain/value.**
- §1 concedes the separation is familiar: coordinates, sampling grids, domain and value.
- What is new is claimed to be "a construction of it for a reader at a standpoint". It is unclear what a probabilist gains beyond "the Cauchy is the pushforward of the uniform angle under tan", which is textbook.
- The "rule" in §6 ("a Cauchy variable is a direction … never an amount") is either a definition or false. Counterexamples where a Cauchy-distributed quantity is naturally an amount:
  - Brownian motion's hitting position on a line;
  - a Lévy-flight displacement;
  - a resonance energy;
  - a ratio of independent normal *amounts*.
- The paper turns each into a "turn" post hoc. That makes the rule unfalsifiable as stated.
- Fix: present it as an interpretive heuristic, not a test.

**A9. §7, "What the two sweeps return": the product = 1 is trivial.**
- θ/sin θ and sin θ/θ are reciprocals at every θ, so their product is 1 by definition.
- At the horizon, the "inscribed 2/π" is chord/arc there. It is also, separately, the mean of cos θ over the quarter turn. That is a coincidence of two different quantities, and the text conflates them.
- Fix: delete the claim that something is "given back", or state it as the identity it is.

---

## 4. Self-containedness gaps

Ranked by severity.

**S1. "home" means two things (clash).**
- §2 (l.104): home is the *reading* [1 : 0] (v = 0, which l.94 also calls "zero").
- §4 and Prop. 3(b) ("the corner lies at distance 1 from home"), §5 ("a bar about home") and §7 ("A at home"): home is the *standpoint point*.
- §7 then says the horizon's landing point "is home", i.e. the point A, while zero's landing point is B. So "home" is the reading v/h = 0 in §2 and the landing point of the reading v/h = ∞ in §7.
- Fix: rename one of them, e.g. "the standpoint O" vs "the reading zero".

**S2. "zero" and "home" are both the reading [1 : 0].**
- Pick one.

**S3. Terms used before definition.**
- "inscribed sweep", "central sweep", "the chord", "c" all appear in the Results list (l.61–69) before their definitions in §5 and §7.
- "attitude", "bar" appear in §2 before §4.
- "lay", "zoom" are defined only by forward reference.
- "writer" is defined in one sentence ("who holds the whole object") and does a lot of work later.
- "all of h" / "all of v" are never defined. They appear to mean the basis vectors e_h, e_v.

**S4. What exactly is "the reading" in Prop. 3(a) and 4(c)?**
- 3(a) says no single reading depends on c.
- 4(c) says the readings' *law* depends on c via tan θ′ = c·(v/h).
- Is the reader's datum v/h, or the drawn direction θ′? Say which.

**S5. Notation clashes.**
- k is the lay slope (Prop. 9) and the address index (same §9).
- s is the reading (4(d), §7) and the truncation bound (5(d), "readings below s").
- f is an increasing map (§6, Prop. 8), the reciprocal-symmetric map (Prop. 2(b)), f(λ) (Prop. 9), and the density bound f₀.
- L is the lay and L₀ an amount.
- d is a distance and also part labels "(d)".
- None of these is fatal; together they hurt.

**S6. Unstated reliance on the long version.**
- "Cauchy's functional equation … whose increasing solutions are k·ln λ": needs the domain [1, ∞) and monotone ⇒ measurable. Fine, but state it.
- §11 Q4's marginalisation claim ("the substitution η = 1/λ turns one reasoner's likelihood into |y|^(−n) times the other's") is asserted without the setting (what y is, what n is). It cannot be checked from the manuscript.
- "Talacko 1956" for the sech law: fine.
- The intro claim "changing the standpoint changes the addresses without touching the object" is never developed.

**S7. Domains of h and v.**
- On the "capped chart" max(h, v) = 1. On the circle h² + v² = 1. §2 says h, v ∈ [0, 1] "shares of that one length".
- Theorem 5(e) uses "the law of h" on an arbitrary path.
- State once that h and v are coordinates on a chosen curve, and that only [h : v] is invariant.

---

## 5. Internal consistency

- **Cross-references.** Theorem 5, Props. 1–9, 3(b), 3(d), 3(e), 4(c), 5(b), 5(e), 6(a), 6(b) and §§ numbers all resolve. No dangling references found.
- **Abstract vs body.**
  - "Following Jaynes's principle … this law is the turn's own: whatever arrives along a direction cancels from its reading". The body does not derive the cancellation from Jaynes (see A2).
  - "order survives every change of what arrives" matches 5(b).
  - "No reading fixes the size; one amount carried in does" matches Prop. 6, but omits the orientation input (M11).
- **Intro.**
  - "changing the standpoint changes the addresses without touching the object": not proved anywhere.
  - "(Proposition 6)" for the "one amount carried in": fine.
- **Results bullet 3** ("on a drawing with two axes … a Cauchy of scale 1/c"): consistent with 4(c). It should say *half*-Cauchy and name the uniform parameter (M2).
- **"Working back" vs 4(c).** These use different uniform measures (arc length vs drawn angle). 4(c)'s c = 2 law has median 0.5. "Working back"'s c = 2 law has median 0.739. Both are presented as "the page drawn at c = 2".
- **References.**
  - Bertrand (1889) is listed but not cited by year. "Bertrand's chord" is mentioned without citation; add "(Bertrand 1889)".
  - Archimedes is cited only as "Archimedes' hat-box theorem"; add the year.
  - All other in-text citations are in the list and vice versa.
  - Please verify the bibliographic details of Leonard (2011), Liu & Adams (2019) and Cacoullos (2014). I could not confirm them from the manuscript alone. The author name for Leonard 2011 in particular should be checked.
- **Missing literature** for this venue:
  - van Fraassen 1989 (*Laws and Symmetry*);
  - Marinoff 1994 and Shackel 2007 on Bertrand;
  - Seidenfeld 1979;
  - Kass & Wasserman 1996 (selection of priors by formal rules);
  - Berger, Bernardo & Sun on reference priors and invariance;
  - Jaynes's own invariant measure m(x) in the continuous entropy (1968), the nearest analogue of "address measure";
  - Kato & McCullagh (2020) for the spherical Cauchy family.

---

## 6. Overclaiming, with suggested rewording

1. **Abstract.**
   - Current: "this law is the turn's own: whatever arrives along a direction cancels from its reading".
   - Suggested: "the reading of a direction does not depend on the magnitude received along it, so the reference law on readings is fixed before any data."
2. **§6.**
   - Current: "The Cauchy is not a law of anything the reader meets. It is the reader's own layout of directions, counted."
   - Suggested: "Under the uniform measure on angle, the half-Cauchy is the reference law of readings; the law of observed readings is that reference law reweighted by what arrives."
3. **§6.**
   - Current: "a Cauchy variable is a direction, read by its order, never an amount".
   - Suggested: "we propose, as an interpretive heuristic, reading Cauchy variables as projective coordinates where a turn can be identified."
4. **§11 Q3.**
   - Current: "That a reader should sweep by a turn … is what the propositions show, in Jaynes's normative sense."
   - Suggested: "If a reader's ignorance includes all turns, the propositions say which measure it should adopt; whether it should adopt that group is not shown here."
5. **§2.**
   - Current: "consistent with straws tossed since (Liu and Adams 2019)."
   - Suggested: delete, or "Liu and Adams report experiments in which the tossing mechanism selects Jaynes's measure."
6. **§11.**
   - Current: "Each relaxation gives a named alternative rather than no geometry".
   - Suggested: "We illustrate three relaxations." The general claim is not proved.
7. **§7.**
   - Current: "Their product … gives the 1 back."
   - Suggested: "θ/sin θ and its reciprocal multiply to 1 at every θ."
8. **§11 "What the geometry gives free".**
   - "Free" overstates. Each item rests on the premises listed (one length, a uniform measure, (S), a fixed K).
   - Suggested: "follows from the premises with no further choice."
9. **§1.**
   - Current: "the construction says which magnitude it loses … and what restores it, one amount carried in".
   - Suggested: add "together with the relative orientation of standpoints".
10. **§7.**
    - Current: "These are the only two kinds of pivot …"
    - Suggested: "the only two pivots in the closed disc …" (see M5).

---

## 7. Minor and typographical

- Abstract, "carries h into v in a quarter turn": "h" and "v" here are basis directions, not the unit relations defined two sentences earlier.
- l.135: line break inside "What it gives: uniform in θ, once the / sweep is taken" (stray hard wrap). The same happens at l.441 ("is / e^(iπ) = −1. The").
- §6, l.316: "depends only on their order so that for every…": add a comma, or "in the sense that".
- §9, (S): "for all x, λ ≥ 1": say "x ≥ 1, λ ≥ 1".
- §9: "1 + ln x + α(ln x)²" needs α ≥ 0 for monotonicity on [1, ∞).
- §10 step 3: say that the 36 directions span the half turn. 0.6368 is the half-turn value.
- §10 step 2: the "reader's corners" at v/h = ±1 use *signed* readings over the half turn, while the paper's readings are on one quadrant. Say so.
- Prop. 2(a): "(0, 1/a)" should be "(0, 1/a)" open at 0 only if x is allowed to be ∞. Harmless.
- "Cayley–Klein metric (Cayley 1859; Klein 1871)": the distance |ln(c′/c)| between i/c and i/c′ is the Poincaré half-plane distance. Calling it Cayley–Klein is correct in spirit; say "hyperbolic distance".
- Acknowledgements: "checked by exact computation". Exact computation is not visible to the reader. Either supply the scripts as supplementary material or say "numerically verified".
- "Lévy, P. (1925)" is listed after "Lupton" (alphabetisation).
