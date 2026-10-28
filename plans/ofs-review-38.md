# Review 38: a fresh referee read of the submission (28 October 2026)

A fresh agent read `papers/ofs-submission.md` alone, as a mathematics or probability journal's referee: major revision,
4/10, every number it could recompute correct. Its report is kept verbatim below the response. Tom: "yes, go with your
recommendations". OFS first, then the submission and the CS companion (R421).

## Response

Made (in OFS, the submission and, where the passage exists, the CS companion):
- 2.1 The corner is fixed by the exchange, not by home and the horizon alone (x ↦ λx keeps both and moves 1); swapping h
  with v asks only that both be shares of the reader's one length H. The referee's "the unit the reader lacks" is wrong:
  the reader holds H, it lacks V*. OFS §4's heading is now "The corner, fixed by the exchange".
- 2.2 An address statistic is one that commutes with every strictly increasing map; "which side of the corner" is kept
  only by increasing maps fixing 1, the exchange's, and left the list.
- 2.3 "Once a Cauchy" and averaging scoped to the signed reading; the half-Cauchy is carried off its arc by a turn and its
  average grows like (2/π)·ln n.
- 2.4 OFS 13(c) / submission 8(c): R defined (bounds H/R ≤ V* ≤ H·R) or a proper law symmetric in log(V*/H); the improper
  dκ/κ alone has no median.
- 2.5 Proposition 1: (0, 1) onto (1, ∞).
- 2.6 The exchange does not commute with turns but is a reflection, so the group is unimodular (submission; OFS said so);
  the turns act on the whole circle, the reader's quarter the restriction.
- 2.7 OFS 11(b) / submission 7(b): directions in one frame; places not in line with both readers.
- 2.8 Theorem 6(e) / 5(e): a continuous path near h = 0 only at its end; with atoms 1 is a median, the only one where the
  law increases strictly through 1.
- 2.9 §4 / §7: the half turn takes zero's landing point, B, to the horizon's, which is home.
- 2.10 The submission says "two kinds of pivot" and takes the radius as 1 (OFS already treats outside pivots).
- 2.11 Theorem 6(c) / 5(c) headed "the mean among them".
- 4.1 The Results bullet and abstract name continuity, linearity, the quarter turn and an inner product, not a measure;
  OFS §12.2 question 2 likewise.
- 5.1 The abstract: the addresses from the restriction and the uniform measure on the turn.
- 5.2 Theorem (a) kept as part (a) (it is cited throughout the corpus), its proof now "holds by construction, a reading
  being a direction; it is stated so that (b)–(e) can be read against it".
- 5.7 PSL(2,ℝ): the Cauchy family is the orbit of the standard Cauchy, on which the group acts transitively.
- Submission §2: the capped chart named as a chart, the reader's circle the main picture (3.1); near field, level (log₂),
  lay and zoom defined (3.4); "defined except at".
- Submission §9: a distance read against H as the direction [H : d], once d/H is had, licenses H·tan(kπ/2K) (3.2).
- §10: the 36 directions at midpoints; Cayley 1859 and Klein 1871 cited at the Cayley–Klein distance; 8(a) f = log₂.
- Venue (Tom, with the recommendation): a foundations of probability or philosophy-of-probability journal, where the
  reading is the contribution, rather than a mathematics journal.

Not taken: §5.3–5.4 (a ratio of normals is a direction, which is the thesis, not an error); 4.5 (§10's walked H is the
amount carried in); 5.14 (the physics is marked as related work); 2.12 (Prop 3(c), (d) as stated in OFS); the remaining
notation clashes and minor items, left for the typesetting pass.

## The report

# Referee report: "Addresses Given, Payloads Met: The Cauchy distribution as the geometry of a situated reader"

Manuscript: `papers/ofs-submission.md` (draft of 27 October 2026). The report reads that file alone. Numbers were recomputed in
`/tmp/claude-0/-home-user/77d2f260-ddc7-5e3a-b202-18b5f494fd0a/scratchpad/checks.py` (mpmath, 30 digits).

## 1. Summary and recommendation

The paper models a "situated reader" that holds one length H and reads directions [h : v]. It argues four things. The
reciprocal x ↦ 1/x has a distinguished fixed point, "the corner" (Props 1–2). A linear, continuous, returning one-parameter
sweep preserves an inner product, so the reader traces a circle (Prop 3). The uniform turn's readings v/h are half-Cauchy,
with median 1 and quartiles √2 ∓ 1 (Prop 4). Order statistics of readings commute with increasing maps and means do not, so
the Cauchy should be read as a law of "addresses", not of "payloads" (Thm 5). Further sections cover Euclid III.20 and the
Cayley transform (§7), scale invariance of ratios (Props 6–7), median estimation under log loss (Prop 8), a logarithmic
far-field layout from the multiplicative Cauchy equation (Prop 9), and a worked example (§10).

Every stated number I could recompute is correct. The proofs are mostly correct, but each is elementary and classical, and
the paper says as much ("The theorem is elementary; its content is the reading"). The contribution is therefore an
interpretation. That interpretation is hard to evaluate because:
- the paper uses two incompatible parametrisations of (h, v) (the ℓ∞ cap of §2 and the unit circle of §4 and §7);
- several statements are definitional rather than mathematical (Prop 3(a), (b); Thm 5(a));
- a few mathematical claims are wrong as stated (see §2 below: the projective "corner from home and horizon alone", the
  "which side of the corner" address statistic, Cauchy closure applied to quadrant readings, the median of an improper
  prior).

**Recommendation: major revision. Score 4/10.** For a mathematics or probability journal the mathematical novelty is
low. The paper could suit a foundations or philosophy-of-probability venue once the errors below are fixed, the two (h, v)
conventions are reconciled, and the interpretive claims are clearly separated from the theorems.

## 2. Mathematical errors (most severe first)

**2.1 §3, after Prop 1: the corner is *not* fixed by home and the horizon "by projective structure alone".**
Text: "once home and the horizon are given, the corner is fixed by projective structure alone, with no measure."
- This is false. The projective maps fixing 0 and ∞ are x ↦ λx, a one-parameter family that moves 1 to any λ > 0.
- The harmonic-conjugate statement before it is correct: the fixed points ±1 of x ↦ 1/x are harmonic with respect to
  every swapped pair. But it presupposes the involution x ↦ 1/x, that is, a choice of unit pairing h with v.
- Given only {0, ∞}, the pairs harmonic with respect to them are {a, −a} for every a. No point of (0, ∞) is singled out.
- Fix: "once home, the horizon *and the exchange* are given, the corner is determined projectively (as a fixed point of the
  involution), with no measure; the exchange itself encodes the unit."
- This matters for the paper's thesis. The corner needs exactly the third datum (a unit comparing h with v) that the paper
  elsewhere says the reader lacks.

**2.2 §6, definition of address statistic vs Theorem 5(b).**
- The definition lists "which side of the corner each lies on" as an address statistic. Theorem 5(b) says every address
  statistic is preserved under every strictly increasing f.
- An increasing f with f(1) ≠ 1 changes which readings lie below the corner. For example, f(x) = 2x sends 0.7 past it.
- So "side of the corner" is not rank-invariant. It is invariant only under increasing maps that fix 1 (or that commute with
  the reciprocal, f(1/x) = 1/f(x)).
- Fix: drop it from the list, or restrict (b) to maps fixing the corner and say so. The definitions are also not a
  partition: the median "depends on sizes" too, since it is a size. Define address statistics as those *equivariant* under
  increasing maps (T(f(X)) = f(T(X))), and payload statistics as the rest.

**2.3 §6, "Once a Cauchy, always a Cauchy", applied to the reader's readings.**
- The closure facts (real Möbius maps, sums of independent Cauchy variables, "Averaging n readings gives the same Cauchy")
  hold for the *signed* Cauchy on ℝ.
- The reader's readings live on the closed half-arc, v/h ∈ [0, ∞], and are *half*-Cauchy (§2, Prop 4).
- The half-Cauchy is not closed under averaging. A sum of positive variables with tail ~ 2/(πx) is not half-Cauchy: the
  mean of n of them grows like (2/π) ln n.
- Most Möbius maps, including a turn θ ↦ θ + α, carry [0, ∞) off itself.
- Fix: state explicitly that this paragraph concerns the signed reading over two quadrants (as Prop 4(b)'s last sentence
  does), and that a turn moves readings off the reader's arc. Otherwise drop "Averaging n readings gives the same Cauchy" for
  the reader.

**2.4 Prop 8(c): the median of an improper law.**
- Proof: "The bounds are H/R and H·R, and log(V*/H) has median 0." R is never defined.
- Under total ignorance the paper's measure is dκ/κ (§2), which is improper and has no median. Open question 4 itself says
  dκ/κ "has no total".
- (c) holds for (a) with symmetric bounds H/R, H·R, and for (b) with any *proper* law symmetric in log κ. It does not hold
  for "nothing the reader knows".
- Fix: "(c) If the bounds are H/R ≤ V* ≤ HR for some R ≥ 1, or the reader's law for log(V*/H) is proper and symmetric
  about 0, both give ĉH = H." Delete the implicit appeal to dκ/κ.

**2.5 Prop 1 statement.**
- "The reciprocal carries [0, 1) onto (1, ∞) point for point": 0 has no image in (1, ∞).
- Fix: "(0, 1) onto (1, ∞)", or work on the closed arc and write "[0, 1) onto (1, ∞]" with 1/0 = ∞.
- Relatedly, x ∈ [0, ∞) excludes the horizon. §2 defines the reading space as the closed half-arc, so state Prop 1 there.

**2.6 §2, Haar measure on the reader's group.**
- "The turns and rescalings ... the measure they leave unchanged is dθ·dκ/κ, their Haar measure ... the reader's group has
  one."
  - The group named includes the exchange θ ↦ 90° − θ, which does not commute with turns: it conjugates a turn to its
    inverse.
  - The group generated (an O(2)-type group × ℝ₊) is non-abelian but unimodular, so the conclusion "one invariant measure"
    survives. The stated reason ("commute") does not apply to the full group.
- The domain is also wrong. The reader's θ lives on a quarter turn [0, π/2] (§2: "a closed half-arc"). Turns θ ↦ θ + α do
  not act on that interval. The uniform measure on the quarter is the *restriction* of Haar measure on the circle, not a Haar
  measure of a group acting on the reader's domain.
- The same issue recurs in §5, "Why uniformly by area": "the only probability on the sphere every rotation leaves unchanged
  is uniform area". Rotations do not preserve the octant.
- Fix: state that the invariant measure is taken on the full circle (sphere) and then conditioned on the quadrant
  (octant), and justify that conditioning.

**2.7 Prop 7(b) is missing hypotheses.**
- "two readers whose placement relative to each other is known up to scale fix every place both see" needs both of:
  - the readers' relative *orientation* (a common frame for directions), not only their placement;
  - the exclusion of points on the line through both readers, where the two lines coincide. The proof's "Two non-parallel
    lines from different points meet in one point" fails exactly there.
- Fix: add "with directions read in a common frame" and "for every place not collinear with the two readers".

**2.8 Theorem 5(e) and Prop 2(b): the hypotheses do not quite match.**
- Prop 2(b) assumes f strictly increasing. The law F in (e) need not be, and may have atoms.
- With atoms, the exchange gives F(1/x) = 1 − F(x⁻), not 1 − F(x).
- The conclusion "its median is the corner" should be "1 is a median". It is the unique median only if F is strictly
  increasing at 1.
- The missing-mean step uses "the path ends at all of v, so there are δ > 0 and v₀ > 0 with v ≥ v₀ wherever h < δ". This
  needs the path to be continuous and to approach h = 0 only near its end. A path that returns near h = 0 elsewhere with
  small v breaks it. State these as hypotheses.
- The table in §6 ("no mean: … no symmetry needed") should also say that the path must end at all of v.

**2.9 §7, the landing point at the horizon.**
- "At zero, the corner and the horizon the landing point is at +1, i and −1 (times ½): the half turn that brings the
  horizon's landing point to home is e^(iπ) = −1."
- From M, zero's landing point (θ = 0) is B, at +½. The horizon's (θ = 90°) is A = home, at −½.
- So the horizon's landing point already *is* home. The half turn brings *zero's* landing point (B) to home.
- Fix the sentence.

**2.10 §7, "These are the only two pivots from which equal turns cut equal arcs".**
- The argument covers only pivots inside the circle (rate 2t/(t + t′)). Exterior pivots are not treated.
- "The pivot on the circle" is a one-parameter family, not one pivot.
- Normalisation: the rate 2t/(t + t′) is in units of the radius R. In §7 the Thales circle has radius ½, so the rate per
  unit turn is t/(t + t′). State the units.

**2.11 Theorem 5(c): the scope of "Payload statistics do not."**
- The proof covers only the arithmetic mean. The heading and the definition ("the mean, any sum") claim it for all sum
  statistics.
- Either restrict the statement to the mean, or prove it for the class intended (for example, every quasi-arithmetic mean
  except the median-like ones).

**2.12 Prop 3(c), (d): circular reasoning.**
- "the Euclidean norm is, up to scale, the only norm preserved by every turn" is true. But "turn" is already a Euclidean
  rotation, so the argument is circular unless "turn" is defined independently. Part (e) is the non-circular version.
- Part (d) is a tautology: a turn preserves length by definition.
- Present (c)–(d) as consequences of (e), or as definitions.

**Checked and correct:**
- quartiles tan(π/8), tan(3π/8);
- Prop 4(d)'s density and marginal integral;
- Z_n, which normalises for n = 1, 2, 3;
- 0.2326 (near field, uniform in both angles) and 0.3426;
- Bertrand ratio arcsin(R/2D)/arcsin(R/D): ⅓ at D = R, tending to ½;
- the three-path g values 0.250/0.293/0.207 and their per-decade increments (2/π) ln 10, ln 10, ½ ln 10;
- the sin²2θ mean 4/π;
- Talacko's (1/π) sech ξ, and the capped-chart mean ½;
- the ellipse c = 2 quartiles of tan t under uniform arc length: 0.3163, 0.7393, 1.6729;
- Gudermannian doublings 18.43°, 12.53°, 6.91°, 3.55°, 1.79°;
- the in-place lay's level lengths 2^(−j);
- 1.1107, 0.9003, π/2 − 2/π = 0.9342;
- §10: 48.01°, s′ = 10/9, d = 10, V* = 20, log₂ 20 = 4.32;
- the 36-direction mean projection 0.6368, which is correct only for *midpoint* directions (0.6362 for left endpoints,
  0.6185 for endpoints including ±90°), so say which;
- the Cayley identity (tan θ − i)/(tan θ + i) = −e^(2iθ);
- the Lorentzian (1/π) dδ/dν;
- the hyperbolic distance |ln(c′/c)| between i/c and i/c′;
- Prop 3(e) steps 1–5, including the minimality argument that forces ω = 2π/T;
- Prop 9's derivation of the multiplicative Cauchy equation from (S).

## 3. Self-containedness gaps

1. **Two incompatible conventions for (h, v). This is the most serious gap.**
   - §2: "Leaving zero, v rises against h held at 1 until it too reaches 1, at v = h; after that h falls against v held at
     1". This is the ℓ∞ cap (the square's edges), with the corner at (1, 1).
   - §4 (Prop 3(c), (e)) and §7: h² + v² = 1, with the corner at (1/√2, 1/√2). §7 adds: "its distances from A and B are h
     and v".
   - Related work: h and v are interference *amplitudes*, h² + v² = 1.
   - Prop 3(b) ("the corner lies at distance 1 from home") makes sense only on the circle, where every point is at distance
     1. On the §2 square the corner is at √2.
   - Pick one convention for the unit relations. Name the other a chart (the "capped share"), and say which is meant in
     each proposition.
2. **"Corner" means three different things:**
   - a direction v = h (Prop 1);
   - a point at "distance 1 from home" (Prop 3(b));
   - a distance d = H in the far-field lay (§9 "x = d/H ≥ 1"; §10 "its corner at 1 mile").
   - The step from a direction to a distance is never given. §9's "K addresses … lie along distance at H·tan(kπ/2K)"
     identifies a reading tan θ with d/H. §2 forbids exactly that identification: "the ratio of unit relations is not the
     ratio of amounts". State the construction (for example, a gnomonic screen at distance H, or a second standpoint) that
     licenses d = H·tan θ.
3. **"Home" is used both as a direction and as a point.**
   - As a direction: "[1 : 0]" (§2).
   - As a point (the standpoint): "lines all pass through home"; "A at home"; "the corner lies at distance 1 from home".
4. **Terms used before or without definition:**
   - "the near field": §1, "What is ours is … the near field and the corner". It is never formally defined; §5 implicitly
     takes it as "h is the largest".
   - "level / levels":
     - §2: "every level of the other's size alike";
     - §8: "a shift in levels";
     - §10: "4.32 levels".
     - It is first defined implicitly in §9, and its base switches between ln and log₂.
   - "zoom": §9, §11; never defined.
   - "lay": §9; never defined beyond L(x).
   - "writer" and "blueprint": §2, §8; informal.
   - "the circle on the chord": Results bullet; defined only in §7.
   - "inscribed sweep": named in §5 before §7 explains it.
   - "the level chart ξ": §6.
   - "(P0)" relies on "a writer" and "its own one length" without formal content.
   - Prop 8(c): R (see 2.4).
   - Open question 4: y and n in "turns one reasoner's likelihood into |y|^(−n) times the other's" are undefined.
5. **Reliance on outside sources and the long version.**
   - §1 points to Brinkman (2026) for "the full account of the reader".
   - The equal-area claim relies on Archimedes and Lambert without a formula. Give Z = sin(altitude) uniform and the azimuth
     uniform.
   - The "group condition Jaynes (1980) reports" is asserted, not stated.
   - Bertrand's chord: the answer arcsin(R/2D)/arcsin(R/D) is given without derivation. One line suffices: a ray at angle φ
     off the centre direction cuts a chord longer than R√3 iff D·sin φ < R/2.
   - The "numerical claims were checked by exact computation" (Acknowledgements), but no code or supplement is provided.
6. **Notation clashes** (each symbol reused with different meanings):
   - c: the page stretch, and ĉ an estimate;
   - k: the slope in Prop 9, the address index in tan(kπ/2K), and confusable with κ;
   - f: the increasing map (Thm 5), the density bound f₀, and the loss transform (Prop 8);
   - L: the lay, and L₀ an amount;
   - s: the reading v/h, and an upper limit of integration (Thm 5(d), §6);
   - t: the sweep parameter, and the distances t, t′ (§7);
   - λ: the rescaling of κ, the scale factor (Prop 6), and the multiplier (Prop 9);
   - γ: the Cauchy scale, and also appears as γ₁, γ₂ heights;
   - θ: the attitude, and the reading's angle;
   - (h, v): unit relations, then distances, then amplitudes (see item 1).
7. **Domain of θ.**
   - The group action θ ↦ θ + α is on a circle. The reader's θ ∈ [0°, 90°]. The exchange's θ ↦ 90° − θ is defined only on
     the quarter. See 2.6.

## 4. Internal consistency

1. **Results bullet vs Prop 3(e).** The bullet says "a sweep that is continuous, composes and returns after a full turn has
   its own Euclidean measure". Prop 3(e) also requires:
   - linearity ("every step the same linear map of the plane");
   - that h is carried into v in a quarter of a turn (needed for step 4, h ⟂ v).
   The abstract repeats the omission. And Prop 3(e) gives an *inner product*, not a "measure".
2. **Results bullet (§7).** It is listed as a result but has no numbered statement. Number it (e.g. Proposition 5½), or move
   it out of the Results list.
3. **The paper says Cauchy throughout, but the reader's law is half-Cauchy.** The abstract and §5 are careful: the reader's
   law is the half-Cauchy. But §6 ("Once a Cauchy …"), §11 (PSL(2,ℝ) acting on "the signed reading") and the title use
   Cauchy facts that hold only for the signed version. See 2.3.
4. **Two different sweeps called "the half turn".**
   - §7: the central sweep's arc of π/2 is a half turn about the centre of the Thales circle, radius ½.
   - §10 step 3: "On the thumb's circle each quarter turn is an arc of π/2 thumbs" (radius 1), then "the half turn gives
     π/2".
   Make the radius and the sweep explicit in both places.
5. **§10 step 6 vs §2 on H.** Step 6 says "Walk one H toward the range … the reader's own H walked once". §2 says H "is not a
   measured size" and the reader's chosen value "sets only the scale". Walking one H presupposes that H is a physical length.
   Say explicitly that the walk turns H into an amount (the "amount carried in" of Prop 6(b)).
6. **The abstract on Jaynes.** "Hence the median at the corner for any sweep that treats the two parties alike" presents
   Thm 5(e) as a consequence of Jaynes's principle. It follows from Prop 2(b) and the symmetry assumption alone.
7. **References.**
   - Listed but never cited: Cayley (1859) and Klein (1871). Cite them in §11, where the hyperbolic-distance remark is the
     Cayley–Klein metric, or remove them.
   - Cited without a year: Archimedes ("Archimedes' hat-box theorem") and Bertrand ("Bertrand's chord").
   - All in-text cross-references (§§, Props 1–9, Thm 5 and its parts) point to existing items.
8. **Bibliographic details to verify:**
   - Jaynes (1973): page range 477–493 (I recall 477–492);
   - Liu and Adams (2019): EJP 40, 065801;
   - Cacoullos (2014): JMVA 128, 147–153.
   - These could not be checked from the manuscript alone.
9. **Jones (2008).** The text says "log-symmetric in Jones's terms". Jones's term in that paper is *reciprocal symmetry*;
   log-symmetry is a different, related notion. Check the wording.

## 5. Overclaiming (with suggested rewording)

1. **Abstract.** "We construct the addresses from that restriction alone."
   - The construction also needs the uniform measure on turn, the linear returning sweep, and a chosen group.
   - Suggest: "We construct the addresses from that restriction together with a uniform measure on the reader's turn."
2. **Theorem 5(a)** ("Nothing that arrives changes the Cauchy").
   - The "proof" is (ℓv)/(ℓh) = v/h: the reading is *defined* as a direction, so it is invariant by construction.
   - Calling this part of a theorem overstates it. Make it a remark or definition: "By construction a reading depends only on
     the direction …".
3. **§6.** "The Cauchy is not a law of anything the reader meets. It is the reader's own layout of directions, counted."
   - This is interpretation. Many Cauchy variables in probability are laws of amounts: the ratio of two independent normals,
     first-passage positions, stable sums.
   - Suggest: "In this model the Cauchy is the law of the reader's directions; nothing in the model assigns it to what
     arrives."
4. **§6.** "We offer the rule, as a test: a Cauchy variable is a direction, read by its order, never an amount."
   - As a general rule this is false, or at least untestable as stated (see item 3). Either drop it or state it as a
     heuristic, with the class of examples it applies to.
5. **§7, "What the two sweeps return".** "Their product … gives the 1 back."
   - The two quantities are x = θ/sin θ and 1/x, so the product is 1 identically.
   - Suggest: "The two readings are reciprocal, so their product is 1 at every θ; this carries no information about any
     breadth."
6. **§5, "Why a turn and not a boost".** "A measure on directions that treats every place alike and is unchanged by its own
   motion comes only from a turn."
   - "Treats every place alike" is undefined.
   - What is proved: among one-parameter Möbius flows, only elliptic ones admit an invariant probability with full support,
     and that probability is a Cauchy law centred at the flow's fixed point.
   - State that.
7. **§11.** "the Cauchy family is the one family it [PSL(2,ℝ)] carries into itself".
   - Trivially false as worded: point masses, and the set of all laws, are also carried into themselves.
   - Suggest: "… the Cauchy family is the orbit of the uniform law on the circle, on which PSL(2,ℝ) acts transitively
     (Knight 1976; McCullagh 1996)."
8. **§11.** "The geometry is therefore necessary relative to a stated ignorance."
   - It also needs the linearity premise of Prop 3(e) and (S), as §11 later admits.
   - "Each relaxation gives a named alternative rather than no geometry" is asserted, not shown. For example, "a preferred
     direction gives the square's or the line's law" is not derived anywhere.
9. **§1.** "changing the standpoint changes the addresses without touching the object" is never stated or proved. Drop it,
   or point to where it is shown.
10. **§7.** "These are the only two pivots …" is proved only for interior pivots (2.10).
11. **§9.** "H cannot be declined: … where the lay loses its corner and a finite reader loses what it reads" is not proved.
    Mark it as a remark.
12. **"What the geometry gives free".** "addresses for any number of things with no table and no count" is metaphorical.
    Also, a fixed count K identifies things sharing an address, as §9 itself admits.
13. **Results bullet and abstract.** "No reading fixes the size of what is read; one amount carried in does." Prop 6(b) gives
    this only for amounts *linked* by readings to L₀. Add the qualifier.
14. **§11.** The quantum-measurement sentence and the interference-visibility related work are physics, against §1's "no
    claim about physics". Keep them as clearly flagged analogies, or cut them.

## 6. Minor and typographical

- §2: "x = v/h (defined but at the horizon) … y = h/v (defined but at home)". "But" for "except" is ambiguous; write
  "defined except at".
- §2: "consistent with straws tossed since" is unclear; write "consistent with experiments since".
- Prop 2(a): give the registers' ranges as [0, a] and (0, 1/a); stated as such already. Fine, but "x ≤ a" vs "x > a"
  leaves x = a in the first register. Fine.
- Prop 4(d) and its proof: "v/v₂" in the statement, "v₂/v" in the proof. Equivalent by reciprocal invariance; make them
  match.
- Theorem 5(d) repeats Prop 4(b). Cite it instead.
- §5, "Working back from the Cauchy": the c = 2 quartiles (0.316, 0.739, 1.673) are for uniform *arc length* on the
  ellipse (cos t, 2 sin t), with the reading tan t. Say so. Prop 4(c), for uniform *direction*, gives median 1/c = 0.5
  instead, and readers will otherwise think the two disagree.
- §9: "half of them inside H at every H" holds exactly only for an even K and a stated indexing convention (k = 1…K or
  0…K−1). Specify which.
- §10: the "thumb H = 1 mile" is whimsical. Consider "a reference length H = 1 mile".
- §10 step 3: say that the 36 directions are midpoints (see 2, last list).
- Prop 8(a): "f = log" while §10 uses log₂. Fix one base for "levels".
- The table "What depends on what": the second row's condition duplicates the first's. Merge or differentiate.
- §6: "the strengths of separate lines add" is fine; "Spectroscopy reads the profile by its centre and half-width" should
  have a citation for practice, or be flagged as illustration.
- Acknowledgements: provide the exact-computation scripts as supplementary material.
- References: "Lévy" is out of alphabetical order (after Lupton). Euclid's Heath translation is 1908, 2nd edition 1926.
  Fine, but state which is used.
