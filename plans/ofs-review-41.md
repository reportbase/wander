# Review 41: the fourth fresh referee read (28 October 2026), kept as received. Response: SPN R560 and LGO run 3.

# Referee report: "Addresses Given, Payloads Met: the Cauchy distribution as the geometry of a situated reader"

Venue judged against: a journal in the foundations / philosophy of probability (Jaynes, transformation groups, objective priors). The paper is judged as a *reading paper*. Only the manuscript file was read. Numerical checks are in `/tmp/claude-0/-home-user/77d2f260-ddc7-5e3a-b202-18b5f494fd0a/scratchpad/chk.py`.

---

## 1. Summary and recommendation

The manuscript proposes that the Cauchy law should be read as the invariant reference measure (Jaynes's m(x)) on the directions available to a "situated reader": an observer that holds one length H and reads only ratios v/h. On this reading the Cauchy is not the law of any measured quantity. A distinction is drawn between *addresses* (directions, whose law is fixed before data) and *payloads* (what arrives, an amount). The formal core is elementary and mostly classical: the corner x = 1 as the fixed point of x ↦ 1/x; a linear periodic flow is a rotation in some inner product; tan of a uniform angle is half-Cauchy; order statistics commute with increasing maps and means do not; scale cannot be read from ratios; a log lay follows from a Cauchy functional equation. The paper then reinterprets four classical puzzles (water/wine, the marginalization paradox, Bertrand, robust statistics) and three data sets (LIGO, the quasar dipole, single-photon interference). It also states a "test that can fail": any observed Cauchy-type law must have a uniform turn behind it.

**Recommendation: major revision. Score 4/10 for this venue.**

The mathematics is almost entirely correct; I could reproduce every number I checked. The prose is careful, and the paper is unusually honest about what it assumes. The paper falls short in three places, though:

- **(i) The central reading is not shown to change anything.** Every worked case and data case ends with "the answer is known; the reading says where its facts belong". A philosophy-of-probability reader will ask what "belonging" amounts to.
- **(ii) The "test that can fail" is not operational.** As stated, it is either trivially passed or failed by the paper's own examples.
- **(iii) The paper's slogan contradicts its data cases.** It says "The Cauchy is not a law of anything the reader meets", yet the data cases show that an *observed* Cauchy appears exactly when the payload is isotropic, which is a fact about the payload.

The engagement with the indifference literature is decent but thin at the point where it matters most. The log-uniform answer to water/wine and the right-Haar resolution of the marginalization paradox are both known, and the paper does not say how its reading differs from those existing resolutions.

---

## 2. The argument

### 2.1 (Major) The reading's content is underdetermined: "belongs to the addresses" has no criterion

The thesis is that the Cauchy is the invariant measure m(x) of the reader's directions, "not a law of what is measured" (§1, §2 "What kind of measure this is"). That the rotation-invariant measure on the projective line, in the chart x = tan θ, is dx/(π(1+x²)) is textbook (Knight, McCullagh, and in effect Jaynes himself). So the contribution must be the *reading*. Yet the paper never gives a criterion for when a fact about a distribution is an "address fact" and when it is a "payload fact".

The closest it comes is the address-statistic / payload-statistic split in Theorem 5(b)–(c). That split is just "order statistics are equivariant under monotone maps, means are not". It is a property of statistics, not of distributions or of what they are laws of. A skeptical philosopher will say that any law on [0, ∞) can be written as a reference measure times a density. Calling the reference "addresses" and the density "payload" is then a relabelling unless the choice of reference is forced by something beyond the chosen group. The paper concedes the group is chosen (§2, last paragraph; §11). Once that is conceded, the reading reduces to "relative to the group we chose, the Cauchy is the reference measure". That is Jaynes 1968 applied to SO(2) acting on directions.

*Needed:* state explicitly what a reader who accepts the reading will believe or do differently from one who accepts, say, McCullagh's Möbius reading. Then show that difference in at least one case where the answers diverge, not only where "the answers are known".

### 2.2 (Major) The group does not act on the reader's sample space

Jaynes's method needs a group of transformations of the problem. The reader's readings live on the closed quarter arc (h, v ≥ 0). Turns θ ↦ θ + α carry readings off it. The paper handles this by restriction: "The turns act on the whole circle of directions; the reader's quarter is that measure restricted, which the exchange carries onto itself" (§2).

The only transformations that actually act on the quarter are the identity and the exchange. Theorem 5(e) itself shows that this two-element group fixes only the median, not the law. So the step from "the reader's ignorance" to "the uniform measure on the quarter" goes through an action the reader's domain does not support.

A Drory-style critic will press exactly this. The paper's response is in two places:
- "Uniform in what" (§5) says uniform in the flow parameter t of Proposition 3(e).
- "Why a turn and not a boost" argues on the whole line.

Both arguments assume the full circle, or a flow that leaves the quarter. The paper should admit that the quarter's uniform law is inherited from a larger structure the reader does not have. Alternatively, it should argue why the reader is entitled to that structure.

### 2.3 (Major) Proposition 3(e) builds in c = 1 through its hypothesis; "derived rather than assumed" overstates

Proposition 3(e) assumes that the flow "carries all of h into all of v in a quarter of it", i.e. Φ(T/4)e_h = e_v exactly, not c·e_v. With that hypothesis, steps 3–4 make e_h and e_v Q-orthogonal and of equal Q-length. So Q is the standard inner product in the (h, v) coordinates, and the flow is the standard rotation. The equal-length condition (the "V = H" the paper says the reader never sets) is therefore the hypothesis "quarter-turn maps h exactly onto v".

The proof is correct. The rhetoric is not: "the bar can be derived rather than assumed" and "What remains assumed is that the sweep acts linearly … and returns" (§4) omit this third assumption. The "Working back from the Cauchy" passage says "each step is forced by the one before", which is also too strong. The paper itself states the uniqueness claim correctly a few lines later ("Stated as uniqueness and no more").

*Fix:* list the quarter-turn condition among the assumed items in the "Assumed / Derived / Read" paragraph after the proof of Proposition 3, and say plainly that it encodes the equal-length drawing.

### 2.4 (Major) The slogan is contradicted by the data cases

The paper says the Cauchy "is not a law of anything the reader meets. It is the reader's own layout of directions, counted" (§6, after Theorem 5). It also says "the readings' law is the turn's law weighted by how what arrives is spread over the directions". These two statements imply that an *observed* Cauchy (LIGO's direction [H1 : L1]) appears only when the payload happens to be spread uniformly over directions. That is a property of the noise: two independent, equal-variance, centred, rotation-invariant components (Herschel–Maxwell).

So in the LIGO case the observed Cauchy is evidence about the payload's isotropy, not about addresses. The paper's own wording, "a pair of nearly independent noises whose direction is uniform", concedes this.

*Needed:* separate three things the paper currently runs together:
- the reference measure (always Cauchy in the chart v/h, by construction);
- the observed law of readings (Cauchy iff the payload is isotropic);
- the claim that the latter "belongs" to the former.

Without this separation, "the Cauchy is not the payload" reads as false of every observed Cauchy.

### 2.5 (Moderate) The m(x) identification is thinner than presented

Jaynes's m(x) is the base measure in −∫ p ln(p/m). It is defined up to a constant and is meaningful only *relative to the entropy functional and a posterior*. The paper uses m as a stand-alone object whose median and quartiles "mean something" (§11, "the median and the quartiles are the summaries that mean something"). But taking a median of m treats it as a probability, which Jaynes explicitly warned against for the pre-prior and which Norton (cited) argues against.

The paper should say in what sense medians of a reference measure are informative when, by its own §2, the reference "is applied to … as to any measure, and what they say is said of the reference, not of the world". If they say nothing about the world, §11's methodological advice ("take the median") does not follow from the reading.

### 2.6 (Moderate) Objections a skeptical philosopher would raise that are not anticipated

1. **Every continuous law is the push-forward of a uniform variable.** The paper half-anticipates this ("Writing a law as the tangent of some uniform variable does not pass the test; the turn has to be there") but gives no criterion for "there". See §3.1 below.
2. **Chart dependence cuts both ways.** The paper says the missing mean "belongs to the chart" (§1, §6). If so, the median "at the corner" belongs to the exchange and the chart too. Then why is the address law privileged over, say, the sech law on ξ = ln(v/h), which has all moments? The paper needs to explain why v/h is the reader's chart if the mean's absence is "only" chartwise.
3. **Seidenfeld and Kass–Wasserman** are cited but not answered. The standard objection is that the choice of group is itself the prior. The paper accepts this ("conditional"), so its claims of "necessity relative to a stated ignorance" (§11) should be stated without the word "necessary".

---

## 3. Worked cases, data cases, consequences

### 3.1 (Major) The "test that can fail" is not a real test as stated

§6, "What is observed, and what the reading predicts", says that an observed Cauchy-type law must have a uniform turn behind it ("a rotation, a phase advancing steadily, or the direction of a pair of independent amounts of one spread"). It also says its departure from Cauchy must be accounted for by the independently measured spread of what arrives. There are three problems.

- **(a) Counterexample class.** The generalized CLT: sums of iid symmetric variables with P(|X| > x) ~ c/x (e.g. X = ±1/U, U uniform) converge to a Cauchy with no rotation, phase or isotropic pair anywhere. The resonance case also shows that the paper's own rule is satisfied by mere rewriting. In §6, the Lorentzian is written as (1/π)·dδ/dν with tan δ = γ/(ν₀ − ν). That identity holds for *every* Lorentzian, so "the turn is there" is satisfied by rewriting. This is exactly what the paper says does not pass the test. The authors must either:
  - accept the stable-limit case as a failure of the reading, or
  - say what physical feature of the stable limit is the turn (the long version reportedly invokes Brownian landing, but this manuscript does not), and give an operational criterion that excludes the trivial rewriting.
- **(b) Unfalsifiable second clause.** "Its departure from the Cauchy is the spread of what arrives over directions" is a Radon–Nikodym identity: the observed law divided by the Cauchy is by definition a density over directions. It cannot fail unless the "independently measured spread" is specified in a way that does not use the observed law. None of the three data cases measures that spread independently.
- **(c) The LIGO case fails it on its own numbers.** The angle is "within 0.009 of the uniform law in Kolmogorov distance" on N = 2,080,768 samples. The 5% KS critical value is 1.358/√N ≈ 0.00094, so 0.009 is about 9.6 times the critical value (√N·D ≈ 13). Even allowing for serial correlation after whitening, uniformity of the angle is decisively rejected. By the paper's own test, this departure from the Cauchy must be accounted for by an independently measured spread of the noise over directions; the paper reports "uniform" instead. Either the departure is explained (unequal effective variances after whitening, residual cross-correlation, non-Gaussian tails), or the case counts against the reading on the paper's own terms.

### 3.2 (Major) The data cases show the relabelling, not a new consequence

- **LIGO.** That one detector's whitened strain is not Cauchy (t with ν ≈ 16, block means shrinking as n^(−1/2)) is ordinary. That the ratio of two independent, equal-variance, approximately Gaussian channels is Cauchy is ordinary.
  - "Scaling one channel by c moves the median to c exactly" is algebra, not evidence.
  - "the median of |L1/H1| is 0.999" after normalising each channel by its own IQR is close to forced by construction: it follows from symmetry plus equalised scales and needs no Cauchy.
  - Nothing here discriminates the reading from the textbook "ratio of normals" reading, which the paper lists among the five classical readings (§1).
- **Quasar dipole.** Ellis and Baldwin's formula already separates the aberration term (2) from the flux-cut term x(1 + α). Calling them "addresses" and "payload" relabels a split that has been in the literature since 1984.
  - The empirical claim that colour slices disagree is Secrest et al.'s (or a reanalysis of their catalogue). The manuscript does not say who did the slice analysis, with what x and α per slice, or with what error bars. A sentence "three colour slices disagree with one another, which no boost can do" needs numbers and a reference or a methods paragraph.
  - Checks: 3.31 × 10⁻³ / β_CMB (1.234 × 10⁻³) = 2.68, consistent with "2.7 times". The "two thirds of the 0.0074 expected" implies x(1 + α) ≈ 4. This is plausible for CatWISE but not derivable from the text.
- **Single photon.** Visibility ≤ 2hv and V² + P² ≤ 1 are Greenberger–Yasin/Englert; the paper says so ("All of this is classical; the reading is the sort"). The fringe period agreement (fλ/d to 0.3% and 1.7%) is irrelevant to the reading.

*Recommendation:* either cut the data cases to one, used as illustration, or redesign them as genuine discriminating tests. Each should have a prediction the address/payload reading makes and the standard reading does not. The current claim "three cases from published data" overstates what they do.

### 3.3 Worked cases (§6, "What the reading changes")

- **Water and wine.**
  - The numbers are correct: 5/8, 15/16, ln 6/ln 9 = 0.81546, and 5/6 for uniform in the share of wine.
  - The log-uniform (dx/x) answer is well known in this literature (it is the standard "Jeffreys" or scale-invariant proposal, defended by several authors after Mikkelson). The paper presents it as what the reading yields without citing those defences or saying what is new.
  - "A change of one liquid's unit multiplies x by a constant and moves no direction" is false as written. Rescaling one coordinate's unit *does* move the direction [water : wine] in the coordinates in which the problem is posed; it relabels the same physical mixture. It also moves the range [1/3, 3], so the invariance argument needs Jaynes's restriction-consistency condition. That condition is stated only parenthetically.
  - Please verify the citation "Jaynes left it open as overdetermined (1973, §8)". I could not confirm that §8 of "The Well-Posed Problem" treats water/wine.
- **Marginalization paradox.**
  - The derivation is correct. With r = |y|/η, ∫ η^(−n−1) f(y/η) dη = |y|^(−n) ∫ r^(n−1) f(ru) dr.
  - It is the known result that the right-Haar (here scale-invariant) prior avoids the paradox in group models (DSZ 1973 discuss it; Jaynes 1980, which the paper itself cites in open question 4).
  - "they cannot" overclaims beyond the pure-scale model η^(−n) f(y/η | ζ). DSZ's normal μ/σ example has a location-scale nuisance, where the paradox-free prior is not the one the reader's group supplies (the long version reportedly notes Jeffreys's dμ dσ/σ²; this manuscript does not). Scope the claim to pure scale nuisances.
- **Bertrand from a standpoint.**
  - Correct: arcsin(R/2D)/arcsin(R/D) is 1/3 at D = R, 0.4826 at D = 2R and 0.49937 at D = 10R.
  - This is the classical "chords through a fixed external point" family. It is not new, and its D → ∞ limit coinciding with Jaynes's answer is well known.
  - The invocation of dθ·dr/r is idle: only the angular part enters.
  - "an answer that ignores the standpoint is the far reader's" (§11) is a reading, not a consequence.
- **Directions read by their order.** The advice "summarize ratios by median, combine bearings by tangent addition, average angles" is standard directional-statistics practice (Mardia and Jupp, cited). Stated as a consequence of the reading, it needs to say what it adds.

### 3.4 Worked example (§10)

All numbers check:
- d = H·s′/(s′ − s) = 10 and V* = 2sd = 20;
- the half-angle atan(10/9) = 48.0°;
- log₂ 20 = 4.32;
- the mean of |cos| at the 36 midpoints of the half turn is 0.63682, and over 36 midpoints of a quarter it is 0.63667, against 2/π = 0.63662.

Two things to fix:
- **Step 3 is confusing.** "each quarter turn is an arc of π/2 thumbs" (the radius-1 circle) is followed by "Read by the central sweep the half turn gives π/2" (the radius-½ circle on the chord, from §7). These are two different circles. State which circle each number lives on.
- **"over a quarter" is ambiguous.** It means 36 midpoints over a quarter; the 18 quarter-midpoints of the 36-step half turn give 0.63682 again.

---

## 4. Mathematical errors and imprecisions (ranked)

1. **§6 LIGO: the KS distance is presented as agreement.** "within 0.009 of the uniform law in Kolmogorov distance" with N ≈ 2.08 × 10⁶ is a rejection (√N·D ≈ 13). *Fix:* report the KS p-value, or an effective-N estimate given whitening autocorrelation, and explain the departure. Otherwise drop "uniform".
2. **§5, "Uniform in what": "So the exact law is forced given the premises of Proposition 3(e)".** True only with the quarter-turn premise Φ(T/4)e_h = e_v, which is the equal-length condition (see 2.3). *Fix:* name it.
3. **§6 water/wine: "moves no direction".** Incorrect in the problem's own coordinates (see 3.3). *Fix:* "relabels each mixture without changing it; the law must then be the same on the rescaled range", and state the restriction-consistency requirement in the main text.
4. **Proposition 3(b): "the corner lies at distance 1 from home, measured in H".** The corner is a direction, not a point; a distance is undefined. Presumably it means "on the reader's circle, the point at the corner is at distance H from home" (or, on the capped chart, the point (1, 1)·H is at distance √2·H). *Fix:* state which point.
5. **Proof of Proposition 3(e), step 1: "A real 2 × 2 matrix with exp(TA) = I has eigenvalues ±iω, ω = 2π/T".** In general the eigenvalues are ±2πik/T and A must be diagonalisable; minimality of T gives k = 1. The argument is right but skips diagonalisability. *Fix:* add "exp(TA) = I forces A diagonalisable over ℂ with eigenvalues in (2πi/T)ℤ; real and nonzero gives ±2πik/T, and minimality of T gives k = 1".
6. **§6 single photon: "the central sweep's height and foot (§7)".** §7 gives the height as hv (on the chord of length 1) and the foot at h², but V = 2hv and P = |h² − v²|. These are the landing point ½(h² − v², 2hv) scaled by 2 and re-centred, not "height and foot". *Fix:* "twice the central point's coordinates relative to M".
7. **Proposition 8(a): "worst error ½·log(V₊/V₋)".** The base is unspecified; with f = log₂ it is ½·log₂. Minor.
8. **Proposition 4(a): "near zero a step barely changes v/h".** At zero, d(v/h)/dθ = 1, so a step changes v/h by the step itself. "Barely" is misleading; say "changes v/h by about the step, while near upright by the step times 1 + (v/h)²".
9. **Theorem 5(e) statement versus abstract.** The abstract says "the sweep's weight stays above zero near the horizon"; the theorem requires the *law of h* to have a density ≥ f₀ on (0, δ). These are not the same for a path parametrised arbitrarily (weight times |dh/ds|). *Fix:* use the theorem's condition in the abstract and Results.
10. **§2, Haar paragraph.** "with the abelian rescalings the whole group is unimodular". The rescalings act on κ, the exchange and turns on θ; the product O(2) × ℝ₊ is unimodular, fine. But the sentence contrasting "the location-and-scale family's affine group … has two invariant measures" with "the reader's group has one" is misleading. A non-unimodular group has one left and one right Haar measure, each unique up to scale. The point is that they differ, not that there are "two".

Verified correct (no action): Proposition 4(b) quartiles √2 ∓ 1; 4(c) scale 1/c; 4(d) density and marginal; Z_n; near field 1/(n + 1); 0.2326 near field for uniform altitude/azimuth (also P(v ≤ h) = 0.3426); the c = 2 page quartiles 0.207/0.5/1.207 and arc-length quartiles 0.316/0.739/1.673; the three-path g values; per-decade mean growth (2/π)·ln 10, ln 10, (ln 10)/2; the sin² 2θ mean 4/π; the Cayley map −e^(2iθ); the pivot rate 2t/(t + t′); the Gudermannian identity and 18.43°, 12.53°, 6.91°, 3.55°, 1.79°; the in-place lay 2^(−j); π/2 − 2/π = 0.934; 1.1107 × 0.9003 = 1; the Bertrand formula; water/wine values; the marginalization factor |y|^n; 2,080,768 = 508 s × 4096 Hz.

---

## 5. Self-containedness, notation, cross-references, references

**Inconsistencies and cross-references**
- §1: "it draws on physics and data to show what the reading does (one case in data, §6)". §6 has three data cases. The abstract mentions none, though the submission is pitched on them.
- §6: "Counted against what arrives, the readings' law is the turn's law weighted by how what arrives is spread over the directions (§2)". §2 does not state this; it says only that the observed law "depends on what arrives". *Fix:* state and prove the weighting formula where it is first used.
- §1 cites "(Proposition 6)" for "one amount carried in". Correct, but Proposition 6(b) is what is meant.
- "Theorem 5" sits among Propositions 1–4 and 6–9. This is fine, but the title "the main result" is elementary by the paper's own admission ("The theorem is elementary"). Consider calling it a proposition.

**Notation clashes** (substantial for a self-contained paper)
- V is the other party's breadth (§2) and also fringe visibility (§6, V² + P² ≤ 1).
- x is the reading v/h (Proposition 1), the far amount d/H (§9), the counts slope (quasar case), and the generic variable in Theorem 5.
- α is the turn amount (θ ↦ θ + α), the spectral index, the angle off axis (cos³α), and the quadratic coefficient in §9.
- k is the log coefficient (Proposition 9) and the address index (§9, tan(kπ/2K)).
- D is the bracket (§3), the distance to the circle's centre (Bertrand) and, implicitly, the Doppler factor.
- P is the landing point (§7) and predictability (§6).
- s is the reading (§7, Proposition 4(d)) and the walk reading (§10).
- m is Jaynes's m(x) and the Cauchy median in m + iγ.
- H is the reader's length and also "Hanford (H1)".
- c is the drawing ratio throughout, and also "scaling one channel by c" in LIGO, where it is a different object.

*Fix:* a notation table, and renaming visibility, the spectral index and the Bertrand distance.

**Undefined or late-defined terms**
- "home" is first used in §2 "Readings…" as the end [1 : 0] but appears earlier ("lines all pass through home" is only later). Fine. However:
  - "drawing" (as in "two-axis drawing") is never defined;
  - "writer" is introduced in a single sentence and then carries philosophical weight (§8, "A blueprint, the writer's statement in amounts");
  - "lay", "zoom" and "level" are introduced in §2 but used substantively only in §9. For this venue, §9 and the "writer" apparatus could be cut or moved to the long version.

**References**
- Cited in text but missing from the reference list: Poisson (1824); Cauchy (1853) and Bienaymé (given via Stigler 1974, acceptable if made explicit).
- Missing relevant literature: the scale-invariant/log-uniform water–wine answer and its defenders; Eaton–Sudderth or other work on right-Haar priors and marginalization; the generalized CLT for index-1 stable limits (Gnedenko–Kolmogorov), which is needed if the "test" is to address the stable reading; Bertrand's chord through a fixed exterior point.
- Self-citation: "Brinkman (2026)" is a GitHub URL to a long version. For a refereed venue, archive it (Zenodo or arXiv) or drop the reliance on it ("further applications and classical connections").
- All other listed references are cited somewhere in the text.

---

## 6. Overclaiming, with suggested rewording

1. §6: "The Cauchy is not a law of anything the reader meets." → "In the chart v/h the reference measure on directions is Cauchy whatever is met; an *observed* law of readings is Cauchy only when what arrives is spread uniformly over directions."
2. §6 headline box: "The Cauchy is not the payload; it is the address to the payload." → "Read as a reference measure on directions, the Cauchy is an address law; observed Cauchy laws combine it with the payload's spread over directions."
3. §6: "So the reading makes a claim the usual readings do not … That is the test, and it can fail." → Either supply an operational criterion for "a uniform turn behind it" that excludes rewriting (see 3.1), or recast as "a heuristic: look for the turn".
4. §5: "each step is forced by the one before" → "given the turn, each step follows" (the paper's own uniqueness sentence).
5. §4: "the bar can be derived rather than assumed" → "the bar follows from a linear, periodic flow that carries h exactly onto v in a quarter period".
6. §6 marginalization: "Read with the reader's own measure on the other's size, dη/η, they cannot [disagree]." → "For a pure scale nuisance under dη/η they agree, as is known (DSZ; Jaynes 1980)."
7. §11: "The geometry is therefore necessary relative to a stated ignorance" → "follows from" (necessity language invites the Drory/van Fraassen objection the paper elsewhere concedes).
8. §1: "Jaynes points to a different status … This paper puts the Cauchy in that place" → acknowledge that putting the rotation-invariant measure on directions in that place is Jaynes's own move (and McCullagh's); the novelty is the address/payload interpretation.
9. Abstract: "we construct the addresses from that restriction and the uniform measure on the reader's turn". The uniform measure is assumed, not constructed; say so.
10. §6 quasar: "part of the dipole belongs to the sources themselves" → "the colour-slice disagreement suggests a source-dependent contribution (analysis details: …)".

---

## 7. Minor and typographical

- Abstract, l. 14: the long line "Read as v/h, the uniform turn's directions are the half-Cauchy on a quadrant…" is fine, but "its quartiles a reciprocal pair" should say √2 ∓ 1.
- §2: "Breadths are written in uppercase. The reader holds one, H". The "one" is ambiguous (one breadth or one length).
- §3: "Without that, a bounded reading such as x/(2 + x) has its middle at x = 2". "Middle" means f = ½; say so.
- §5 Proposition 4(d): "the reader near in both readings" → "the reading in the near field of both pairs".
- §6, three-paths paragraph: "the mean of the readings below s grows" means the truncated first moment, not the conditional mean. Say "∫₀^s x dF".
- §6: "Even then an added amount of finite spread leaves the tails ~ γ/(πx²)" is true for the convolution, but the scale of the tail term is the Cauchy part's. Fine; add "of the Cauchy component".
- §7: the half-turn landing points "+1, i and −1 (times ½)" are relative to M; say so.
- §9: "H cannot be declined: … an H that favours no value is H at 0 or ∞" is rhetorical; it is unclear what "favours no value" means for a single positive number.
- §10, step 2: "With directions spread uniformly over the half turn". Over the half turn the readings are signed, and the full Cauchy is meant, not the half-Cauchy of Proposition 4. Say so.
- §11, Related work: the one paragraph runs very long; split it.
- References: "Lévy" sorts after "Lupton" in the list; "von Mises" sorts under S ("Secrest … von Mises … Norton"). Alphabetise.
- Acknowledgements: "the numerical claims were checked by exact computation". The LIGO and quasar figures are statistical estimates, not exact; reword.
