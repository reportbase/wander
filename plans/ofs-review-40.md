# Review 40: a third fresh referee read, of the submission as a reading paper (28 October 2026)

A new agent read the expanded `papers/ofs-submission.md` alone (with the background, the worked cases and "What would
follow"), judged as a reading paper for a foundations of probability journal: major revision, 4/10, every number
correct. Three reads under three framings all scored 4; the objections now go to the argument. Tom: "yes".

## Response

Made (OFS first, then the submission):
- My errors: "directions have no sum, so their law has no mean" (in the background and the worked cases) corrected: read
  in the unbounded chart v/h a law of directions has a median and no mean, on a bounded chart (the angle) it has both;
  the missing mean is the chart's. Kass and Wasserman (1996), left uncited by R554's trim, cited again in the background.
  "A sharper answer" withdrawn: the cases' answers are known, the reading says where each answer's facts belong.
- The central objection (every Cauchy the paper illustrates is the law of something observed, matching the reference
  only when what arrives is isotropic; the test cannot fail since any law is a transform of a uniform): a paragraph
  "What is observed, and what the reading predicts" after the worked cases. Counted against what arrives, the readings'
  law is the turn's weighted by how what arrives is spread over directions (OFS §2, in words, no ρ, R347 kept); an
  observed Cauchy-type law has a uniform turn behind it and its departure from the Cauchy is that spread, measurable on
  its own; the median moves only by the exchange-asymmetric part (Theorem 6(e)). The test: no turn to be named, or a
  departure the independently measured spread does not account for, counts against the reading; writing a law as the
  tangent of some uniform variable does not pass it. "What would follow" now points there.
- The group's one invariant measure from O(2) being compact with abelian rescalings (not "the exchange is a reflection").
- "Reference measure" replaced by "invariant measure", Jaynes's m(x) (clash with Bernardo's reference priors).
- "The missing mean need say nothing about the system"; the line-shape bullet softened.
- Related work: Mardia and Jupp (2000), Fraser (1968).

Not taken: the circularity of Proposition 3(e)'s "all of v" (the quarter-period premise is stated, R547); the worked
cases being known (now said); Marinoff's reply to Bertrand from a standpoint (a different problem is the point: the
standpoint is part of the problem); notation, Prop 3(b) and 8(c)'s wording, left for the typesetting pass.

## The report

# Referee report

**Manuscript:** "Addresses Given, Payloads Met: The Cauchy distribution as the geometry of a situated reader" (draft of 27 October 2026)
**Venue type:** foundations / philosophy of probability (Jaynes, transformation groups, objective priors)
**Reviewed:** the manuscript file only. Numbers were recomputed with mpmath/numpy (script `chk.py` in the same scratchpad directory).

---

## 1. Summary and recommendation

The paper takes a reader that holds one length H and does not know the size of what it reads. It separates *addresses* (directions [h : v] from a standpoint) from *payloads* (the magnitudes met along them). It argues that, under a chosen ignorance group (turns, rescalings of the other party's size, and the exchange h ↔ v), the uniform measure on the turn, written in the chart v/h, is a half-Cauchy law. Following Jaynes (1968), it reads this law as the *invariant reference measure m(x)* of the reader's directions, not as a law of anything measured. The formal core is elementary and correct: a direction is unchanged by scaling (Thm 5a); order statistics commute with increasing maps and means do not (5b, 5c); an exchange-symmetric law has its median at the exchange's fixed point, and its mean is missing if the weight stays positive near the horizon (5e). Around this core it gives a periodic-flow lemma (Prop 3e), a scale-cannot-be-read lemma (Prop 6), a logarithmic-lay lemma (Prop 9), and four "worked cases": water and wine, the marginalization paradox, Bertrand from a standpoint, and robust summaries of directions.

**Recommendation: major revision. Score 4/10 for this venue.**

The paper is unusually careful about separating what is assumed, what is derived and what is read. That is to its credit. As a contribution to the philosophy of probability, though, it has three problems:

- **The central reading is not clearly distinguished from the classical "tangent of a uniform angle" reading.** That reading is the paper's own fifth bullet. The paper's distinguishing move, treating the Cauchy as the reference measure m rather than as a distribution p, is asserted rather than argued.
- **That move is in tension with the paper's own applications.** The applications concern Cauchy laws that are distributions of observed quantities (p), not reference measures (m).
- **The worked cases are correct but largely reproduce known resolutions.** The log-uniform answer to water and wine, and right-Haar priors for the marginalization paradox, are known. They do not show what the reading changes.

The proposed "test that can fail" is, as stated, unfalsifiable (§2.3 below).

---

## 2. The argument

### 2.1 (Most serious) The m-versus-p distinction is asserted, and then abandoned in the applications

§2 ("What kind of measure this is") states that the Cauchy is Jaynes's m(x), "neither a belief about what arrives nor a frequency of arrivals", and that "what a reader observes … has a law of its own, which depends on what arrives". This is the paper's key philosophical claim, and it is a coherent one.

Every application then concerns a Cauchy that is a law of something observed:

- the ratio of two centred normals (§1);
- Huber's heavy-tailed data (§6, "Directions are read by their order");
- a spectral line profile (§6, §11);
- "ratio estimates, slopes fitted with error in both coordinates, and bearings" (§11).

In each case the Cauchy is p, the observed law. It coincides with the reference m only because the observed directions happen to be isotropic. For the ratio of normals that is the rotation-invariance of the bivariate normal; for a line profile it is the phase dynamics of the source. Isotropy of what arrives is a fact about the world, which is exactly what the paper says the address law is *not*.

A skeptical philosopher will object along these lines: "You have shown that the Haar measure on directions, in the tan chart, is half-Cauchy. That is the classical reading. To say that the Cauchy *met in practice* is an address law, you need the observed distribution of directions to equal the reference. That equality is an empirical fact about the source, so the Cauchy in your examples is, after all, a law of what is measured." The paper does not anticipate this.

**What is needed:** a section that states precisely when an observed Cauchy p can be identified with m. Presumably that is exactly when the observed directions are uniform in the turn. It should also concede that this identification is itself a substantive claim about the payload. Without it, §6's slogan "The Cauchy is not a law of anything the reader meets" contradicts the examples used to motivate it.

### 2.2 The reading is not separated from the "tangent of a uniform angle" reading it lists as prior work

§1's fifth bullet already makes the law "a fact about directions". The paper says the difference is that those are "the directions of a lamp or a path, not … the places at which a reader meets what it reads."

This is a difference of narrative, not of mathematics or of epistemic status. The lighthouse is the same pushforward of Haar measure by tan. The paper itself grants this in §11 ("whoever turns and whether it receives or sends" is implicit in its use of the lighthouse).

The authors should state one consequence that the address reading entails and the lamp reading does not. Otherwise "what the reading changes" is only a relabelling. The four cases in §6 do not supply such a consequence (§3 below).

### 2.3 The proposed falsification test cannot fail

§11 says: "for any Cauchy met in practice, find the turn and find the amount. A Cauchy-type law for which no turn can be found … counts against it."

By the probability integral transform, every Cauchy(m, γ) variable X can be written X = m + γ·tan(π(U − ½)) with U uniform. A "turn" can therefore always be found mathematically. The test bites only if "turn" means a physical rotation or an independently identified phase. The paper must specify what counts as finding a turn: an operational, non-post-hoc criterion. As written, the claim to falsifiability is empty.

### 2.4 The reader's address space carries no group that fixes the half-Cauchy

The group is defined on the whole circle of attitudes (§2: "The turns act on the whole circle of directions; the reader's quarter is that measure restricted"). The reader's addresses, however, are the quarter [h : v] with h, v ≥ 0, and no nontrivial turn preserves the quarter. §6 concedes that "the reader's half-Cauchy on one quadrant is carried off its arc by a turn".

The only symmetry of the quarter is the exchange, and the paper admits (§5, "Why uniformly by area") that the exchange alone does not fix the law. So the half-Cauchy is not the invariant measure of any group acting on the reader's address space. It is the restriction of a measure invariant under a group acting on a larger space.

That move needs defending in Jaynes's terms. Why is the restriction of the circle's Haar measure the right reference on the quarter, rather than any other exchange-symmetric measure? Otherwise "a reference measure in Jaynes's sense" (abstract) is too strong.

### 2.5 Prop 3(e) builds its conclusion into its premise

Prop 3(e) is offered as deriving "the bar" (V = H) rather than assuming it. But the hypothesis "carries all of h into all of v in a quarter of it" *defines* all-of-v as Φ(T/4)(all-of-h). Any Φ-invariant inner product Q then automatically gives all-of-v the same Q-length as all-of-h.

What the proposition really proves is a classical fact: a periodic one-parameter linear group in ℝ² is conjugate to rotations and preserves an inner product. The substantive assumptions are moved, not removed:

- The motion is time-homogeneous and linear (a one-parameter group).
- The reference measure is uniform in the group parameter t, which is again the Haar choice.

§5 ("Uniform in what") claims that this *fixes* Bertrand's parameter. It fixes it only once one has assumed that the reader's sweep is a one-parameter group and that its own parameter is the one to be uniform in. A van Fraassen-style critic will say this is choosing the parametrisation by fiat.

**Fix:** say plainly that 3(e) reduces the assumption to "the sweep is a continuous linear one-parameter group, and uniformity is in its parameter". Drop "derived rather than assumed".

### 2.6 The response to Drory, van Fraassen, Marinoff and Shackel is thin

These critics are listed in §1. Only Drory receives a reply, in Open question 2, and the reply is that "the core survives the choice", namely the median at the corner.

The surviving core is trivial: any law invariant under an involution x ↦ 1/x has the involution's fixed point as a median (Prop 2b). That is not a vindication of transformation-group reasoning. Everything specific to the Cauchy depends on the chosen group.

The paper should engage the van Fraassen and Shackel line directly. If the group is "chosen, not derived" (§2), in what sense is the resulting reference measure *objective*, and what work does Jaynes's principle do beyond relabelling a choice?

### 2.7 Prop 8(c) is incoherent with H being arbitrary

§2 says that H is "a value it chooses to start from", carrying no information. Prop 8(c) then concludes that, with bounds symmetric about H, "both give ĉH = H".

If H is arbitrary, nothing makes the reader's knowledge symmetric in log(V*/H) about 0. Symmetry about an arbitrarily chosen point is not ignorance; it is an informative assumption tied to an arbitrary choice. This is a standard objection to "the estimate is the reference scale". It deserves a sentence acknowledging that 8(c) has content only if H is chosen *informatively*, for example at the geometric mean of known bounds, which is 8(a).

### 2.8 Ambiguity in "Hence" (abstract)

The abstract runs: "Whatever arrives along a direction cancels from its reading … Hence the median at the corner for any sweep that treats the two parties alike …". The median at the corner does not follow from the cancellation. It follows from exchange symmetry (Theorem 5e). Replace "Hence" with "Separately," or restructure the sentence.

---

## 3. Worked cases and consequences

All numbers were recomputed and are correct; see §3.5. The question is whether the cases show something the usual readings do not.

### 3.1 Water and wine (§6)

The figures 5/8, 15/16, 5/6 and ln 6/ln 9 = 0.81546 all check. The log-uniform answer, though, is the standard Jeffreys/scale-invariance answer and has appeared repeatedly in the literature on this paradox. The paper cites Mikkelson but none of the later responses.

The "every answer that treats them alike puts P(x ≤ 1) = ½" observation is immediate from symmetry and is not specific to the address reading.

There is a substantive gap. "A change of one liquid's unit multiplies x by a constant" is not a symmetry of the stated problem, because the range [1/3, 3] is itself unit-dependent. The scale invariance is therefore doing no work until the extra requirement "one law on every range of x" is imposed. That requirement is Jaynes's own consistency condition and gives the answer by itself. The case does not show what the *address* reading adds. The paper should either say so or name the added content.

### 3.2 Marginalization paradox (§6, Open question 4)

The computation is correct. Numerically I find the two integrals in the ratio |y|^(−n) for n = 3: 0.069250 against 0.069250.

That the right-Haar prior dη/η for a scale nuisance avoids the paradox is, however, the known resolution: it appears in Dawid, Stone and Zidek's discussion and in Jaynes (1980), whom the paper itself credits in Q4. The bullet "Reading the data's direction is reading its address, and the scale's invariant measure is what makes the two agree" relabels this. It does not change it.

The paper should also say that DSZ's paradoxes arise for priors *other than* the right-Haar one. So "under the reader's own measure they cannot" disagree is true by choice of prior, not by the reading.

### 3.3 Bertrand from a standpoint (§2, §6)

The formula arcsin(R/2D)/arcsin(R/D) is correct: ⅓ at D = R; 0.4826 at D = 2R; 0.4994 at D = 10R; tending to ½.

This is the most interesting case. Identifying Jaynes's ½ as the far-standpoint limit, and the random-endpoint ⅓ as the on-circle standpoint, is a nice observation. Philosophically, however, it is Marinoff's point: adding a standpoint is specifying a different problem. It does not adjudicate the original, standpoint-free question.

The paper should say explicitly whether it claims (a) that Bertrand's original question is ill-posed until a standpoint is named, or (b) only that a standpoint version has a unique answer. It should also discuss whether the rays-from-a-point construction is already in the Bertrand literature; I believe variants are. The Liu and Adams citation should be checked: is the "ratio of two lengths" dependence in their straw experiment really the same quantity?

### 3.4 "Directions are read by their order" (§6)

This bullet contains a false general statement, the same one as in §1: "directions have no sum, and their law has a median and no mean for that reason". See Math §4.1 below. The practical advice (average the angle, compose by tangent addition) is standard circular-statistics practice and should cite it (Mardia and Jupp). It does not need the address reading.

### 3.5 Other recomputed numbers (all correct)

- **Half-Cauchy quartiles:** √2 ∓ 1.
- **Page drawn at c = 2:**
  - uniform in the drawn angle: quartiles 0.2071, 0.5, 1.2071;
  - uniform in arclength along the stretched ellipse: 0.31628, 0.73929, 1.67286.
- **Uniform in altitude and azimuth on the octant:** near field 0.2326; v ≤ h 0.3426.
- **Three-path table:** 0.250/0.293/0.207 at 22.5°. Mean growth per decade (2/π) ln 10, ln 10, (ln 10)/2.
- **sin² 2θ weight:** mean 4/π.
- **Gudermannian turns per doubling:** 18.43°, 12.53°, 6.91°, 3.55°, 1.79°.
- **Section 7:**
  - θ/sin θ = 1.1107 and sin θ/θ = 0.9003 at 45°;
  - Cayley map (s − i)/(s + i) = −e^(2iθ) for s = tan θ;
  - pivot rate 2t/(t + t′) is consistent with a chord of length 2 cos α.
- **Worked example:**
  - atan(10/9) = 48.01°;
  - d = 10 and V* = 20;
  - log₂ 20 = 4.32;
  - 36 midpoints of a half turn give a mean |cos| of 0.63682. Over a quarter, 18 midpoints give the same value; 36 midpoints give 0.63667. The text's "0.6367 over a quarter" is right only for 36 points on the quarter, so say so.
- **Prop 9 counterexample** 1 + ln x + α(ln x)²: valid for α ≥ 0.
- **Prop 4(d) and Z_n normalisation:** correct.

### 3.6 "What would follow" (§11)

- The line-shape bullet makes a physical recommendation: "is to be explained as such before it is read as a change in what is emitted". This contradicts §1, "no claim about physics". Pressure, Doppler and collisional broadening are physical mechanisms; telling spectroscopists to explain profile changes as standpoint changes first is unsupported.
- "If so, the missing mean says nothing about the system" overstates. Whether a ratio's law has a mean depends on the denominator's density near 0, which *is* a fact about the system.

---

## 4. Mathematical errors and imprecisions (ranked)

### 4.1 Directions do have means; the missing mean is the chart's

**Where:** §1 "Directions have no sum, only a composition, and a law of directions has a median and no mean for that reason (§6)"; repeated in §6, "Directions are read by their order".

**Problem:** this is false as a general statement. Circular statistics defines a mean direction (the argument of the resultant vector). The paper itself states in §6 ("An address is not a payload") that on the angle chart the uniform turn has mean π/4, on the capped share mean ½, and on the level chart every moment. It concludes "The missing mean is a fact about the chart x = v/h, not about the arc." The §1 sentence contradicts this.

**Fix:** "the median of a law of directions is the same in every monotone chart; the mean depends on the chart, and in the unbounded chart v/h it does not exist."

### 4.2 Prop 3(e) is presented as a derivation

**Where:** "the bar can be derived rather than assumed".

**Problem:** see §2.5. The step "U⁻¹(all of v) = R(π/2)u: the two are square and of one length in Q" is immediate from defining v by the flow.

**Fix:** reword as "reduced to the assumption that the sweep is a periodic one-parameter linear group, with all of v defined as the quarter-period image of all of h".

### 4.3 Euler's form is listed as both derived and not derived

**Where:** the paragraph after Prop 3(e) lists "*Derived*: … Euler's form, h + iv = e^(iωt)" and then ends "Euler's formula is used here, not derived."

**Problem:** self-contradictory.

**Fix:** "Derived: (h, v) = (cos ωt, sin ωt); writing this as e^(iωt) uses Euler's formula."

### 4.4 The unimodularity argument is a non sequitur

**Where:** §2, "The exchange does not commute with the turns but is a reflection, so the whole group is unimodular".

**Problem:** being a reflection does not imply unimodularity. The group is O(2) × ℝ₊, unimodular because O(2) is compact and ℝ₊ is abelian.

**Fix:** state that reason.

### 4.5 Prop 3(b): the corner is a direction, not a distance

**Where:** "the corner lies at distance 1 from home, measured in H".

**Problem:** the corner was defined as the direction v = h. As written, 3(b) mixes the capped-chart point (1, 1), at distance √2 in H, with the circle point (1/√2, 1/√2), at distance 1.

**Fix:** state which chart and which point is meant. The proof ("The corner is one H from home measured in H") is circular as written.

### 4.6 Prop 1 holds only for sweeps that pass 1

**Where:** "every sweep from home passes through x = 1".

**Problem:** this is true only for sweeps that go past 1.

**Fix:** "every continuous sweep from home that passes beyond 1 meets 1 first".

### 4.7 Prop 8(a): log base unspecified

**Where:** "worst error ½·log(V₊/V₋)".

**Fix:** write log₂ (levels), consistent with "in levels (f = log₂)".

### 4.8 Theorem 5(a): the cancellation is an identity, yet it is headlined as "the main result"

**Where:** (ℓv)/(ℓh) = v/h, and the proof note "(a) holds by construction".

**Fix:** stop calling (a) a result ("Nothing that arrives changes the Cauchy"). Call it a definition: the address law is defined independently of the payload. It is fine to keep it, but the front matter should not present it as the main result.

### 4.9 Section 7: the "product 1" is a tautology

**Where:** "Their product, not their difference … gives the 1 back".

**Problem:** the two numbers are arc/chord and chord/arc for the same arc (π/2 and 2/π; θ/sin θ and sin θ/θ). Their product is 1 by definition. Also, "the inscribed sweep as its projection over the turn, 2/π" is the mean of cos θ over a uniform quarter turn, which equals chord/arc for the quarter circle. So it is the same ratio, not an independent reading.

**Fix:** delete, or state it as a definitional identity (as for step 3 of §10).

### 4.10 Section 10, step 2: signed readings outside the paper's domain

**Where:** "its ends are at v/h = ±1".

**Problem:** readings were defined in §2 only for h, v ≥ 0 on a quarter turn. The worked example uses a half turn with signed readings and "the reader's corners" in the plural, without any setup for this.

**Fix:** either define the two-quadrant case, or say it is two quarter-turn readers back to back.

### 4.11 Section 5, "Why a turn and not a boost": scope

**Where:** the claim is right for the whole projective line.

**Problem:** it should be stated that it does not apply to the reader's quarter (§2.4 above), since no elliptic flow preserves the quarter.

### 4.12 Theorem 5(e): add a one-line justification

The statement is correct. The proof's "v ≥ v₀ wherever h < δ" needs that the path is compact and reaches h = 0 only at its end. Say "by continuity and compactness".

---

## 5. Self-containedness, notation, cross-references, references

### 5.1 Terminology clash with reference priors

"Reference measure" collides with Bernardo's *reference priors*, a central concept for this venue. Kass and Wasserman (1996) is in the reference list but never cited. Either cite it and engage (formal rules, Haar priors, reference priors), or remove it. Distinguish "reference measure m(x) in Jaynes's 1968 sense" from Bernardo–Berger reference priors explicitly.

### 5.2 Cited but missing from the references

- Poisson (1824) is cited in §1 and not listed.
- Bienaymé is mentioned; covered by Stigler.

### 5.3 Listed but uncited

- Kass and Wasserman (1996).

### 5.4 Citations to verify

- **Jaynes (1973, §8)** on water and wine: confirm that the section exists and contains the "overdetermined" remark. I could not verify the section number.
- **Jaynes (1968)** "pre-prior": confirm that this is Jaynes's term.
- **Jaynes (1980)** "reports" the group condition: give page or section.
- **Liu and Adams (2019)**: confirm the claimed "ratio of two lengths" dependence.
- **Cacoullos (2014)**: confirm title and pages.

### 5.5 Missing literature relevant to this venue

- **Circular and directional statistics** (Mardia and Jupp, *Directional Statistics*). Needed for the claims about means of directions and the wrapped/spherical Cauchy (Kato and McCullagh).
- **Group-invariance and structural inference:** Fraser's structural inference, Villegas, Eaton's *Group Invariance Applications in Statistics*, Dawid's work on invariant priors, Hartigan. These are the natural home of "invariant measure as reference, not belief".
- **Later water/wine literature** beyond Mikkelson (2004).
- **Bertrand standpoint variants**, if any.

### 5.6 Notation overloads

- **f:** strictly increasing map (Thm 5), density bound f₀ (5e), likelihood f(y/η | ζ) (§6), error transform (Prop 8).
- **t:** flow parameter (Prop 3e) and distances ahead t, t′ (§7).
- **k:** lay slope (Prop 9) and address index k (§9).
- **L:** lay L(x) and supplied amount L₀ (Prop 6).
- **s:** reading and integration limit (§6).
- **Two names for one point:** "zero" (v = 0) in §2 and "home" [1 : 0].
- **Logarithms:** "levels counted in log₂" alongside ln in Prop 9 and the level chart.

### 5.7 Undefined or loosely defined terms

- **"writer"** is defined only by contrast and used throughout.
- **"payload: a wave of some kind"** is physics language in a paper that disclaims physics.
- **"lay"** is introduced in §2 with a forward reference to §9.

### 5.8 Cross-references

These are internally consistent: §§1–11, Theorem 5, Propositions 1–9, Open questions 2 and 4. One weak link: the §1 Results bullet points to §8 for "two standpoints bring back the figure", which is Prop 7. That is fine but could cite Prop 7 directly.

### 5.9 Anonymity and self-containment

The long version is cited as a GitHub URL with the author's name. Check the venue's double-blind policy. Several claims are deferred to it ("full account of the reader"); the submission should not depend on it.

---

## 6. Overclaiming, with suggested rewording

1. **Abstract:** "this law is the group's invariant measure, a reference measure in Jaynes's sense".
   → "this law is the image, in the chart v/h, of the restriction of the circle's invariant measure to the reader's quadrant; we propose to read it as a reference measure in Jaynes's sense."

2. **§6:** "The Cauchy is not a law of anything the reader meets. It is the reader's own layout of directions, counted."
   → "The reference law of the reader's directions is a half-Cauchy; an observed Cauchy coincides with it exactly when the observed directions are uniform in the turn, which is a fact about what arrives."

3. **§1 and §6:** "a law of directions has a median and no mean for that reason".
   → see Math §4.1.

4. **§11:** "If so, the missing mean says nothing about the system".
   → "If so, the missing mean may reflect the chart rather than a peculiarity of the system."

5. **§11 line shapes:** remove "is to be explained as such before it is read as a change in what is emitted", or mark it explicitly as a heuristic outside the paper's scope.

6. **§11:** "What it offers is a test that can fail".
   → only once an operational criterion for "finding the turn" is given (§2.3).

7. **§6:** "Four cases … where reading a Cauchy-type law as the law of addresses gives a sharper answer".
   → "Four cases restated in the address reading", unless a case is added where the answer actually differs from the standard treatment.

8. **§4:** "the bar can be derived rather than assumed".
   → see Math §4.2.

9. **§5:** "So the exact law is forced given the premises of Proposition 3(e)".
   → add "and given that uniformity is taken in the flow's own parameter".

---

## 7. Minor and typographical

- §1 and the abstract: the long sentences with many appositive clauses ("its median at the corner and its quartiles a reciprocal pair") are hard to parse for a philosophy readership. Consider a short glossary table: unit relation, reading, address, payload, corner, horizon, home, writer, lay, level.
- §2: "from all of h (v = 0, *zero*) to all of v (h = 0)". Name the second end "the horizon" here, as it is named a sentence later.
- §3: "(log-symmetric in Jones's terms, 2008)". Jones's term is "reciprocal symmetry"; check the wording.
- §6 table: "the circle weighted by sin² 2θ keeps the median and has a mean, 4/π". Correct; give the one-line computation (∫ 4 sin³θ cos θ dθ / (π/4)).
- §6: "Averaging n signed readings gives the same Cauchy … its average grows like (2/π)·ln n". Say "the average of n half-Cauchy readings grows like (2/π) ln n" so the subject is unambiguous.
- §7: "These are the only two kinds of pivot from which equal turns cut equal arcs: taking the radius as 1, from a pivot inside the circle …". Clarify that the 2t/(t + t′) rate is measured at the forward intersection, in arc per radian of turn.
- §9: "a far amount x = d/H ≥ 1, a distance in units of H (which a reader has only from a second standpoint …)". This makes Prop 9 inapplicable to a single reader; say so up front.
- §10 step 3: "with 36 directions … 0.6368; 0.6367 over a quarter". Specify that it is 36 directions on the quarter (18 give 0.6368).
- Acknowledgements: the AI-assistance disclosure is appropriate. Check the venue's policy on placement.
- References: the Archimedes and Euclid entries are fine. Klein 1871 is cited for the "Cayley–Klein metric", but the distance |ln(c′/c)| used is the Poincaré half-plane metric; either works, but name it consistently.
