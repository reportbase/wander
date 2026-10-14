# Evaluation 9 of "Observation from Somewhere" (an adversarial read of the Jaynes reframing)

*14 October 2026 (Tom's local date). After SPN R243–R246 reframed `papers/observation-from-somewhere.md` on Jaynes's
principle of transformation groups, Claude proposed an outside adversarial read before anyone else saw the paper; Tom,
about 14:12: "proceed". The reader was a fresh Claude agent with no part in the writing, briefed as a hostile referee
who knows Jaynes, Jeffreys, Haar measure, McCullagh's Möbius action, Bertrand, the wine/water paradox and the
marginalization paradox. It read the whole paper, checked the algebra and the numbers itself (mpmath), checked every
quotation of Jaynes against his text, and edited nothing. (Evaluation 8, Grok's, was set aside at Tom's word on 14
October, "ignore grok review 8.", and is not kept.) The report is below as received, its layout tidied; the response
follows.*

---

**Findings, most severe first**

1. **Blocking. Two different groups are presented as one.** §2 (l.273–289), §11.1 (l.1813–1824), Q7 (l.1935–1936):
   "Turns and rescalings commute"; "Together they generate PSL(2,ℝ)… It is the right size acting on the reader's two
   unknowns… where it fixes dθ·dκ/κ"; "Its rescaling commutes with the turns acting on what the reader reads". Group 1
   (§2): turns on θ, rescalings on κ = V*/H; by item 2 a rescaling of κ "changes no unit relation", so it acts trivially
   on readings; abelian, Haar measure dθ·dκ/κ. Group 2 (§11.1): Möbius turns on x = v/h plus "a change of the drawn size
   V = cH, x ↦ λx"; these generate PSL(2,ℝ), 3-dimensional, non-abelian. Group 2 does not fix dθ·dκ/κ: its invariant
   measure on the Cauchy family is hyperbolic area dm·dγ/γ², in geodesic polar coordinates about i (r = |ln c|, angle 2θ)
   2·sinh r dr dθ, not dθ·dκ/κ, and it is the left-type (Jeffreys) measure §2 says "does not arise". Group 2 has 3
   parameters vs 2 unknowns, so "as many parameters as the problem" is false for it. Its "rescaling" is the drawing c,
   which the paper requires to be 1, so it is not something the reader is ignorant of; the hyperbolic apparatus rests on
   a transformation outside the stated ignorance, while the rescaling that is ignorance (of κ) does not act on readings at
   all. Fix: keep Group 1 as the ignorance group; present the Möbius/hyperbolic structure as a separate fact about the
   family of drawings; delete "one group", "right size… fixes dθ·dκ/κ", and Q7's "commutes with the turns acting on what
   the reader reads".

2. **Blocking. κ (true size), c (drawing) and c (estimate) are run together.** §2 l.300–301 ("κ = 1, the drawing
   V = H"), intro l.91–92 and l.126–127 ("it gives … the drawing V = H"), remark after Prop. 13 l.1605–1608 ("the even
   turn drawn at V = cH is the Cauchy law at the point i/c … puts i/c at |ln c| from i"), Q6 l.1919–1921. κ = V*/H is the
   true size; the exchange's fixed point κ = 1 is a statement about the estimate (Prop. 13(c)), not the drawing, which
   the paper says is "not a claim about the mountain". Prop. 13's c is the estimate, which "never redraws the circle",
   yet the remark measures the estimate's error by the distance between drawings. §2 item 2 cites Prop. 3(a), which is
   about the drawing c, as support for a claim about κ. Fix: say the exchange acting on the law of readings fixes the
   drawing (Prop. 5(d)); the exchange acting on κ fixes the estimate κ̂ = 1; for the estimate use the law of amounts (in
   amounts the even turn is Cauchy at iκ (§7.2 l.1236) and the estimate's law at ic, so the invariant error is
   |ln(κ/c)|); use distinct letters for drawing and estimate.

3. **Major. v/h treated as V*/H.** §2 l.296–297 ("Even in log κ … Past the corner … this is the logarithmic lay"),
   §11.1 l.1803–1804 ("the rescalings dx/x, every doubling the same number of addresses, premise (S) and so the
   logarithm", with x = v/h). Invariance of a measure on κ says nothing about how readings x are laid, since κ never
   touches a reading; §6 l.952 admits the argument for (S) "passes through amounts, by way of V = H". Q1 (l.1852) still
   says (S) is "assumed rather than derived", contradicting §11.1's "rescalings fix… (S)". Fix: name the bridge
   (κ-invariance applied to amounts v·V* read at V = H), or take (S) and the logarithm off the list of what the group
   fixes and keep Q1 open.

4. **Major. The exchange contradicts the paper's own account of what the reader knows.** §2 l.279–280 ("nothing the
   reader can check tells which party is which") vs §4 l.764 ("the reader's knowledge does not [treat the sides alike],
   since it knows H and not V"), Q4 l.1913–1914 (fairness "more than a choice?") and §11.1 l.1804 (fairness "is the
   exchange's invariance"). In Jaynes's sense an admissible transformation must map a problem to one with the same
   information; κ ↦ 1/κ swaps the breadth the reader holds (H) with the one it lacks (V*). Fix: either confine the
   exchange to readings and drawings (h, v are both unit relations) and leave κ out of it, or call it a chosen fairness
   requirement and answer or update Q4.

5. **Major. Jaynes's location–scale group is misdescribed.** §2 l.282–286: "This is Jaynes's problem of a location and
   a scale"; "In Jaynes's location and scale they do not commute … dμ·dσ/σ, his, is the right-invariant measure".
   Jaynes 1968 eq. (49) is μ′ = μ + b, σ′ = aσ, x′ − μ′ = a(x − μ): that group commutes (and jay-plan transcribes it
   so). The non-commuting group is the family's affine group x ↦ a + bx; Jaynes's 1/σ coincides with its right Haar
   measure but he did not derive it from that group. And in Jaynes the scale acts on the data about the location; here κ
   acts on no reading, so this is two independent problems, not his. Fix: "The location–scale family's own group
   x ↦ a + bx does not commute…; Jaynes's eq. 49 is the commuting product, and its measure coincides with the
   right-invariant one"; "Jaynes's problem" → "analogous to".

6. **Major. The front claims more than the back proves.** Abstract l.12–15 ("fixes the even turn, the logarithm past
   the corner and the corner itself"), intro l.89–92 ("the measure these leave unchanged is the geometry of this
   paper"), Results l.124–129 ("it gives the even turn, the logarithm past the corner, the corner and the drawing
   V = H"). The body says the group is "chosen, not derived" (l.304, l.1834), the smooth join is "an added condition"
   (l.1831), the turns presuppose a rigid bar (l.1832, l.1835), (S) passes through amounts (finding 3), and Q2 grants
   Drory ("symmetry alone does not make it"). "The Euclidean norm is the only norm all turns preserve" (l.1805) is
   circular: turns are already Euclidean; conjugate turns of a V = cH drawing preserve the ellipse. Fix: "the measure left
   unchanged by a group we choose; given turns of a rigid bar…", and drop "and the drawing V = H" from the list.

7. **Major. The even turn is both fixed and not fixed.** Q2 l.1863–1866 ("We grant it. Which selection the reader
   makes, the even turn, is a choice … and symmetry alone does not make it") against §11.1 l.1802 and the abstract (the
   turns fix the even turn). Fix: the group fixes the measure once the selection is parametrised by attitude; choosing
   that parametrisation is exactly Drory's point.

8. **Major. "Forced" error in levels.** Remark after Prop. 13 l.1604–1608, §11.1 l.1818–1820, Q6 l.1919 ("unique up
   to a constant factor"; "Measuring that estimate's error in levels is forced"). Any increasing function of the
   hyperbolic distance is also invariant; uniqueness up to a constant holds only among invariant Riemannian (length)
   metrics. The median of Prop. 13(b) also needs absolute loss; squared loss in levels gives exp E[ln V*], not the
   median. Fix: "invariance forces the error to be a function of |ln(V*/cH)|; with absolute loss this gives the median".

9. **Major. Water and wine is overclaimed and its prior work incomplete.** Q2 l.1897–1911. "Shows the same structure
   and is finished by his method" is undercut by the paragraph's own last sentence ("the problem's statement does not
   say which reading von Mises meant"). The premise "one law on every range (restriction)" is added, Jaynes-like but not
   in the problem. "The missing number is how many levels are held, which is the overdetermination he found" misreads
   Jaynes: his "overdetermined" means no proper law conforms to the group; a missing number is underdetermination.
   Parker and Jeynes (2023, *Entropy* 25, 1242) invoke scale invariance (via Benford) for this exact problem and get
   0.816; wwp-plan read them, the paper does not cite them, nor Deakin (2006, any answer in [½, 1] possible). 25/32 is
   called "proposed since", but Mikkelson presents it as "naïve super-indifference" and rejects it. The 1/3 ≤ x ≤ 3 form
   is Deakin's and Mikkelson's statement; von Mises's own bounds differ, as I recall; check. Fix: "suggests"; cite
   Parker–Jeynes and Deakin; restate the overdetermination correctly; attribute the 1/3–3 form.

10. **Major. Addresses and payload contradict each other between §6 and §7.** §6 l.1044–1047 says the even-direction
    density "belongs to the payload, not to the addresses"; §7's main result says the Cauchy is the addresses. With
    §11.1 now claiming both dx/x (the count of addresses) and the even turn (dθ = dx/(1 + x²)) as the reader's
    addresses, the paper must say which measure on the same reading x is "the addresses": two different measures, each
    invariant under a different subgroup. Fix: rewrite §6's last paragraph.

11. **Major. The near field in §11.1.** l.1808–1811, l.1830–1831. "The measure invariant under shifts gives
    proportion" uses shifts, which are not in the stated group (§2 says being at home "removes the translations").
    "Their spacings… agree at x = 1, so the fixed point of the flip and the meeting of the two spaces coincide"
    contradicts, a paragraph later, "the smooth join … is still an added condition": k·dx/x meets dx at x = k. Fix:
    state the near field's group, and phrase the meeting as a choice of constant.

12. **Major. Domain of the Möbius action.** §2 l.290–295. Turns act on signed v/h over both facings: the standard
    Cauchy at i, median 0 = home. The reader's sweep is one facing, the half-Cauchy with median 1, which equals γ, not m;
    turns do not preserve [0, ∞), and relations are never negative. "Median m … point i" right after "median at the
    corner" mixes the two laws. "The only point every turn leaves where it is" holds only in the V = H drawing; in a
    V = cH drawing, turns act by conjugate maps that fix i/c, so only the exchange selects c = 1. Fix: say this.

13. **Minor. Q7's proof assumes positive amounts.** For the normal μ/σ example the scale-free statistic is ℓᵢ/|ℓ₁|;
    with zᵢ = ℓᵢ/ℓ₁ as written, the ratio law pools both signs and the identity fails. "Checked exactly" was 50-digit
    quadrature; "at no other power" rests on four powers tested, and the gamma case is an exception. Reporting checks of
    a proved result breaks the paper's own rule against them.

14. **Minor. Jaynes 1973 paraphrased loosely.** "Which he derived for a tosser whose 'region of uncertainty'…": he
    derived ½ from invariance; the tosser is his frequency-correspondence argument. "Jaynes's own turn is already an
    observer's facing": his rotation is a passive change of frame, "irrelevant to the distribution of chord lengths".
    "The measures it gives are area, dx·dy, on the plane": area for chord midpoints is Bertrand's ¼, which Jaynes's
    translation step eliminates. "The same dependence" (Liu–Adams): their ratio is straw length to diameter, not
    distance to radius; say "a similar".

15. **Minor. Haar and Ghosh citations.** Haar (1933) proved existence; uniqueness is von Neumann's and Weil's. Exact
    frequentist coverage is attributed to Ghosh 2011; jay-plan sources it to Datta, Ghosh and Mukerjee (2000). Check.

16. **Minor. Q6 l.1919: "H when it knows nothing either way".** Total ignorance, dκ/κ on (0, ∞), has no median, and Q7
    itself says it has no total. Write "when what it knows is symmetric in levels about H".

17. **Minor. Notation clashes.** κ is also the density bound in the proof of Theorem 6(e) (l.1199). c is the drawing,
    the estimate, the lay's slope ("smooth join (c = 1)") and c_n. §3.8 uses b for V*/H where §2 uses κ. a is the
    altitude, v/h in Prop. 5(e), and the factor in z ↦ az. z is the azimuth and a complex number.

18. **Minor. Stale or inconsistent passages.** §7.2 l.1215 points to "(§7.5)" for "the sampling that prefers no
    attitude"; that argument is now in §2. §7.3 l.1260, "the corner is no longer the median", contradicts "every pair
    keeps its corner"; it means |x|. Q2 l.1888, "three such drawings swept evenly": Haldane's (the levels) is not a path
    in the table. §2 item 2, "every amount changes": only the other party's amounts change. "Translations that Jaynes's
    own cases keep": the rate and share cases have none. The dateline still says "11 October". The reference list is out
    of order (Lee before Lambert, Luce before Liu).

**Checked and correct.**
- **Möbius and hyperbolic facts.** A turn acts as x ↦ (x cos α + sin α)/(cos α − x sin α). Turn·rescaling·turn
  factors PSL(2,ℝ), and the flip extends it to PGL(2,ℝ). McCullagh's action holds, and SO(2) fixes only i. V = cH gives
  the law at i/c, and the exchange sends it to ic. The hyperbolic distance between i/c and i/c′ is |ln(c′/c)|.
- **Bertrand.** The situated share arcsin(R/2D)/arcsin(R/D) is ⅓ at D = R, 0.4826 at D = 2R, and rises monotonically
  to ½.
- **Invariant plane measure.** dx·dy/(x² + y²) = dθ·dr/r is invariant under z ↦ az.
- **Water and wine.** The numbers are right: 5/8, 15/16, 25/32, 5/6, 0.7637, ln 6/ln 9 = 0.8155, and 0.8470
  (arctan 2 − arctan ⅓ = π/4 exactly). All the fair answers give P(x ≤ 1) = ½. Restriction plus a change of one
  liquid's unit leaves the powers xᵖ, and the exchange picks dx/x. On [1, 2^L] the answer is 1 − log₂3/L.
- **Marginalization.** The substitution η = ℓ₁/λ does give ℓ₁⁻ⁿ∫λⁿ⁻¹Πg(λzᵢ|ζ)dλ, for positive data.
- **Haar measures.** For location–scale, left is 1/σ² and right is 1/σ. With μ/σ of interest, dσ/σ at fixed ζ is
  dμdσ/σ².
- **Classical priors for a share.** The arcsine (Jeffreys) law follows from the even turn at the foot of the chord.
  Below t = ¼ the three hold ¼, ⅓ and 0.4205.
- **Jaynes quotations, all verbatim and correctly placed.** "facing north or east" (1973 §2); "for, at most, only one
  size of circle" (§3); "region of uncertainty" (§1, §6); translation alone fixes the answer (§5); "overdetermined"
  (§8); "pre-prior" (1968); equal numbers of parameters fix the prior (1968); the share group θ′ = aθ/(1 − θ + aθ).
- **References and style.** Every listed reference is cited and every citation is listed. There are no ruling numbers,
  file paths or standing marks.

**Verdict.** I would not accept the reframing as stated. The method is applied to two incompatible groups that the
paper calls one: the abelian ignorance group on (θ, κ), whose κ never touches a reading; and the PGL(2,ℝ) action on
readings, whose "rescaling" is the drawing the paper says is required, not unknown. On top of that, the true size κ is
repeatedly read as the drawing V = H and as v/h. The single most useful change is to separate them explicitly. Keep
{turns on θ} × {rescalings of κ} × exchange as the stated ignorance, with Haar measure dθ·dκ/κ. Derive the drawing
V = H only from the exchange acting on the law of readings (Prop. 5(d)). Get the logarithm and the error in levels only
through amounts, with the bridge named. Drop "one group", "right size" and "forced". Everything else in the list is
repairable wording.

---

## Response

*Claude, 14 October, after checking each finding against the text. The two blocking findings are right, and both were
my errors in the reframing written the same day: I presented the ignorance group and the Möbius action on readings as
one group, and I ran the true size κ, the drawing c and the estimate c together. Every finding was taken; the edits make
the paper claim less, never more. What changed in `papers/observation-from-somewhere.md`, by finding:*

1. **Taken.** §2 now states one group, the reader's ignorance: turns of θ, rescalings of κ, and the exchange of the unit
   relations; turns and rescalings act on separate unknowns and commute; Haar measure dθ·dκ/κ. §11.1 presents the Möbius
   action on readings (turns and changes of the drawing, generating PSL(2,ℝ), with the flip PGL(2,ℝ)) as a different
   group, "not the reader's ignorance", whose change of drawing the reader does not leave open and which, acting on
   readings alone, is overdetermined in Jaynes's sense; it is "a fact about the family of drawings, and its one use here
   is to measure distances". "One group", "the right size … fixes dθ·dκ/κ" and question 7's "commutes with the turns
   acting on what the reader reads" are gone.
2. **Taken.** The drawing and the estimate now have different letters: the drawing V = cH (required, c = 1); the
   estimate ĉH (Proposition 13 and the passages around it, eleven places). The drawing V = H is derived only from the
   exchange acting on the law of the readings (Proposition 5(d)): §2's first bullet, §11.1, the abstract, the
   introduction, the first result and "What is claimed, then". The estimate's error is measured through amounts: the even
   turn of the true bar is the Cauchy law at iκ and the estimate's at iĉ, at distance |ln(κ/ĉ)| (remark after
   Proposition 13; §11.1). §2 item 2 no longer cites Proposition 3(a).
3. **Taken, by naming the bridge.** §2: dκ/κ "does not lay the readings, which κ never touches. Carried to amounts, a far
   reading taken as an amount at V = H, the same indifference to scale is premise (S) of §6, which gives the logarithmic
   lay past the corner: the bridge is the amount, and (S) stays a premise". §11.1: the rescalings "motivate premise (S)";
   (S) "is still assumed (§11.2, question 1)". Question 1 is now consistent with both.
4. **Taken, the first option.** The exchange acts on readings and drawings, v ↔ h, θ ↦ 90° − θ, not on κ: "the reader
   holds H and not V*, and the two breadths cannot be swapped without changing what it knows". κ and 1/κ alike is "a
   separate premise, used only for the estimate" (Proposition 13(c)). Fairness is "its invariance stated as a rule" on a
   group that is chosen; question 4 stands as asked.
5. **Taken.** §2: "analogous to Jaynes's problem of a location and a scale … though here the scale acts on no reading:
   two problems side by side rather than one"; "Jaynes's own group, μ′ = μ + b with σ′ = aσ (1968, eq. 49), also
   commutes. The location-and-scale family's group, x ↦ a + bx, does not, and has two invariant measures: dμ·dσ/σ, the
   right-invariant one, which coincides with Jaynes's, and dμ·dσ/σ², the left-invariant one, Jeffreys's general rule."
6. **Taken.** The abstract, the introduction's "What we build on" and the first result now say the group is chosen, that
   the even turn follows given that the sweep is the turning of a rigid bar, and that the logarithm is motivated through
   amounts; "the measure these leave unchanged is the geometry of this paper" is gone. §11.1's circular sentence on the
   Euclidean norm is replaced by "with the bar drawn at V = H the attitudes trace the circle (Proposition 3(c)), so the
   circle and the Cauchy rest on one premise, the rigid turn".
7. **Taken.** §2: "once the sweep is taken to be the turning of the bar, an even turn; which variable the evenness is in
   is the choice Drory presses (§11.2, question 2)".
8. **Taken.** "Forced" is gone. The remark after Proposition 13, §11.1 and question 6: any measure of the error the
   Möbius action keeps is a function of the error in levels; unique up to a constant factor only among distances measured
   along curves (Beardon 1983); with absolute loss in levels the best estimate is the median.
9. **Taken.** Question 2: water and wine "shows the same structure, and his method gives an answer once one premise is
   added"; restriction is called "a premise the problem does not state"; the 1/3–3 form is "the form Mikkelson (2004)
   states"; 25/32 is "the mean of 5/8 and 15/16 (which Mikkelson considers and rejects)"; Parker and Jeynes (2023, 0.816,
   scale invariance through Benford's law, not treating the liquids alike) and Deakin (2006, any answer between ½ and 1,
   as Parker and Jeynes report it) are cited; the overdetermination is restated as Jaynes meant it: on the unbounded
   range "no proper law on it is unchanged by a change of unit: his overdetermination. Bounded at 2^L, the levels give
   1 − (log₂ 3)/L, so an answer needs the range held." Von Mises's own bounds were not checked here: his text is not to
   hand; the paper no longer attributes the 1/3–3 form to him.
10. **Taken, with one qualification.** The paper did already separate the reader's own evenness (addresses, §7) from
    the sources' (the lighthouse, payload, the abstract); §6's sentence "If directions are spread evenly" did not say
    which. §6's last paragraph now reads "If what arrives is spread evenly in direction, as a lighthouse's flashes are
    (§7.8)", and adds that the lay and the even turn are different measures on the same reading, the lay placing
    amounts past the reader's breadth, the even turn stepping through attitudes, the reader's when the sweeping is its
    own and the world's when it is the sources'. §2's second bullet says the same.
11. **Taken.** §11.1: inside the corner "one more transformation applies: a shift within H, which no reading prefers";
    "Their spacings, 1 and c/x, agree at x = 1 only for c = 1, the smooth join, which is chosen". §2's near-field sentence
    likewise.
12. **Taken.** §2: "Read as v/h on one facing … the half-Cauchy with its median at the corner …; signed over both
    facings, the standard Cauchy"; the Möbius action is on the signed reading; "the standard Cauchy, at i, is the only one
    every turn leaves where it is. Drawn at V = cH … the turns of that drawing act by the conjugate maps, which fix i/c,
    and the exchange carries i/c to ic. So it is the exchange … that selects the drawing V = H".
13. **Taken.** Question 7's proof now runs through the data's direction u = ℓ/|ℓ| and the substitution η = 1/λ, valid
    for data of either sign; "checked exactly" is gone, and the examples are reported as "at none of the other powers
    η^(−k) we tried", the gamma as the exception.
14. **Taken.** "Jaynes phrases his rotation as the observer's …; here the turn is the bar's attitude"; "the measure it
    gives on lines is Crofton's; on points of the plane, the measure that translations and turns keep is area";
    "which, he argued, is what a tosser whose 'region of uncertainty' is large compared with the circle will see";
    Liu and Adams show "a similar dependence".
15. **Taken in part.** Haar (1933) is kept for the measure's name, with the uniqueness argued directly for this group
    (f(θ + α, λκ)·λ = f(θ, κ) leaves only c/κ), rather than adding von Neumann and Weil. Exact coverage is now "as
    reviewed by Ghosh 2011"; Datta, Ghosh and Mukerjee (2000) is not cited, being unread here.
16. **Taken.** "H when what it knows is symmetric in levels about H" (question 6; the remark after Proposition 13).
17. **Taken in part.** κ in the proof of Theorem 6(e) is now β; the estimate is ĉ; the notation table gives θ, κ (with
    "b in §3.8"), m + iγ (of the signed reading) and c, ĉ; "z ↦ az" is gone from §2. The older clashes (a for the
    altitude, z for the azimuth, c in Proposition 4's lay and c_n) are left as they were.
18. **Taken.** §7.2's pointer is "(§2, §7.5)"; §7.3 now says each pair of readings keeps its median at its own corner
    and the radius |x| does not; question 2 says the three priors come from "two of the paths above swept evenly, and the
    levels"; §2 item 2 says the other party's amounts; the abstract says "the translations that Jaynes's chord keeps";
    the dateline is 14 October; the L references are in order.

Not changed: the referee's checked-and-correct list (the Möbius and hyperbolic facts, Bertrand from home, the plane
measure, the water-and-wine numbers, the marginalization substitution, the Haar measures, the classical priors, the
Jaynes quotations, the references) stands as checked.

## Re-check of the revision

*A second fresh agent, briefed to verify the revision narrowly and to look hardest for errors it introduced, read the
changed passages against this review (commit 96c1d4e). Its verdict: both blocking findings resolved in substance; nothing
blocking introduced; four consistency errors a hostile referee would raise, and smaller points. It redid the algebra:
question 7's substitution and the |ℓ|^n identity (numerically, for a normal with data of both signs, to 30 digits), the
distance |ln(κ/ĉ)|, and §7.3's 1 − 1/√2 and √3, all correct; the water-and-wine numbers again correct; cross-references
resolve; every reference cited and listed. What it found, and what was done:*

1. *The drawing credited to the exchange alone,* though Proposition 3(e)'s rigid turn, kept as a standing premise,
   already forces c = 1, and the relaxation "a preferred party gives c ≠ 1" cannot happen while the bar is rigid. **Fixed:**
   §2 now says the drawing is "selected twice: by the rigid turn … (Proposition 3(e)), and by the exchange acting on the
   law of the readings (Proposition 5(d))", and that turns in a V = cH drawing's plane "do not carry all of h into all
   of v"; §11.1, "What is claimed, then" and the first result likewise; the relaxation reads "a preferred party, with the
   bar no longer rigid, gives c ≠ 1".
2. *"The even turn of the true bar is the Cauchy law at iκ" is ill-posed* (a bar at the true size does not turn rigidly;
   drawn at c = κ its amounts are Cauchy at i). **Fixed:** "the even turn of the drawn bar, read in amounts at the true
   breadth, is the Cauchy law at iκ".
3. *"For the reader's group, which commutes, there is one" is false as stated:* with the exchange, a reflection, the
   group does not commute; it is unimodular, so the conclusion holds. **Fixed:** "its turns and rescalings commute, and its
   exchange is a reflection, so the group is unimodular and the measures unchanged by composing on the left and on the
   right coincide".
4. *The near-field shift contradicts "home removes the translations".* **Fixed:** proportion is now "an indifference
   within the near field, not a translation of home, which stays where it is": no position within H preferred, equal
   differences within H given equal room (§2, §11.1).
5. *The remark after Proposition 13 mixed the two groups again.* **Fixed:** the argument now runs from the reader's
   ignorance alone (an error unchanged when the size and the estimate are rescaled together, and alike for larger and
   smaller, is a function of |ln(κ/ĉ)|; with absolute loss, the median); the Möbius distance appears in §11.1 only as
   "the same quantity as a distance". Question 6 likewise.
6. *Case slip: the lay "places amounts".* **Fixed:** "places far readings, taken as amounts at V = H" (§2, §6).
7. *Notation clashes the new text introduced.* **Fixed:** the constant in the Haar argument and Proposition 4's slope are
   now k (Proposition 4's statement and proof, §6's "smooth join (k = 1)", §11.1); the family's affine group is
   x ↦ p + qx; the density bound in Theorem 6(e)'s proof is q₀ (β being §9's share).
8. *"It does not know two things", then a three-part group.* **Fixed:** "two quantities …; nor, from a reading alone,
   which of the two unit relations the reading was divided by".
9. *Question 7:* a single g did not cover two of the three examples; "a reader of the ratios alone" though the proof uses
   the direction with its sign; and "at none of the other powers we tried" reported trials. **Fixed:** a joint law
   g(w | ζ) for the vector of amounts; "a reader of the data's direction alone …, the ratios with their overall sign"; the
   trials replaced by what DSZ's examples show ("the paradox comes from other powers of η (in Stone and Dawid's
   exponentials, an even prior on the rate)").
10. *Item 3 cited Proposition 1 for more than it proves.* **Fixed:** the exchange "sends a reading to its flip … (Proposition
    1)", the citation now on the flip.
11. *Uncited eponyms.* **Fixed:** Bernardo (1979) and Benford (1938) cited and listed.

Partly resolved majors from the first review, now closed: finding 10 (§6's "the addresses are even" is now "the lay's
addresses", and the sweep's addresses are named as §7's); finding 11 (item 4 above); finding 12's leftover ("within its
sweep" removed from θ's definition).
