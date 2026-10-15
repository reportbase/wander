# Evaluation 10 of "Observation from Somewhere" (an overall assessment, ChatGPT)

*Shared by Tom on 15 October 2026 (his local date, about 05:06), prefixed "chatgpt review:". It reads the draft dated
14 October 2026, so it was written before Proposition 5(f) and (g) (the lighthouse and Mercator's map) were added on
15 October. Kept as received below, with the layout tidied: the mathematics, which came as LaTeX, is written once in
plain text; the scorecard is set as a table; headings are set in bold. The response follows.*

---

**Evaluation: Observation from Somewhere.** Draft dated 14 October 2026 · Standalone assessment for external review

**Overall verdict**

This is the most ambitious kind of paper in your project: it is not merely proposing a new formula or a different way
to draw a circle. It is proposing a different account of what geometry does when the observer does not possess the
complete object being described.

The central distinction is clear and consequential:
- Object: what exists independently of an observation.
- Address: a place in the observer's scheme where something can be encountered.
- Payload: the magnitude encountered at that address.

Your claim is that a situated observer constructs addresses from bounded relations before receiving payloads, and that
this construction has its own geometry. Classical geometry remains valid; it describes a completed view, while your
paper studies the geometry available without that completed view.

That is a substantive conceptual framework. The draft also does something important for its credibility: it
acknowledges that the Cauchy distribution does not follow from symmetry alone, that the Euclidean circle requires a
choice of measure, and that the logarithmic layout beyond the corner rests on an additional premise. Those admissions
are essential, not weaknesses to hide.

My overall judgment is a promising, substantial conceptual and mathematical paper that is not yet ready for an
unqualified claim of having established its full framework. The main obstacle is no longer whether the idea can be
explained. It is whether the paper consistently distinguishes what follows mathematically from its definitions, what
follows only under selected assumptions, and what is an interpretation of the mathematics.

**Scorecard**

These are my editorial scores for this version, not a prediction of any particular journal's decision.

| criterion | what it covers | score |
|---|---|---|
| Conceptual originality | The address / payload separation and situated-geometry framing | 9/10 |
| Explanatory power | The corner, flip, near/far distinction and reader vantages | 8.5/10 |
| Mathematical development | Explicit propositions, derivations and treatment of alternative measures | 7.5/10 |
| Logical discipline | Separation of definitions, assumptions, theorems and interpretations | 6.5/10 |
| Readability | Accessible examples, but substantial repetition and conceptual density | 7/10 |
| External-review readiness | Potentially reviewable, but several foundational claims need tighter qualification | 6.5/10 |
| Overall | A strong working paper with a meaningful central idea | 8/10 |

The overall score reflects the framework's promise and the work already done. The lower review-readiness score reflects
the burden of proof imposed by its strongest claims, not a judgment that the central idea is uninteresting.

**1. What is genuinely strong**

*A. The address / payload distinction gives the paper a coherent centre.* The paper's strongest move is to distinguish
the scheme that tells an observer where to put a reading from the magnitude that arrives there.

This is more precise than simply saying that perception is subjective or that coordinates depend on the observer. You
explicitly argue that the addressing scheme can remain unchanged while the payload changes, and that a change in the
sweep can alter the addresses without altering the object.

The formal example in Theorem 6(a) makes this concrete: (ℓ·v)/(ℓ·h) = v/h. For any positive common factor ℓ, the
factor cancels. Thus, under the model's assumptions, the reading is invariant to that common scaling.

That is a sound and useful mathematical observation. It gives the address/payload distinction a clear algebraic
expression.

The more ambitious claim—that this is a useful geometry of a situated reader rather than merely a representation chosen
for convenience—is the framework's main contribution to establish.

*B. The corner and flip are the cleanest part of the mathematics.* The transformation x ↦ 1/x has a unique positive
fixed point, x = 1. It exchanges the intervals below and above 1. This provides a simple, exact basis for your corner
and for treating near and far as two sides of one relation.

Propositions 1 and 2 are especially effective because they separate what follows directly from the algebra from what
requires the additional fairness condition.

The distinction matters. The corner at v = h follows from the exchange symmetry. A reading that assigns the corner to
the midpoint of its output range requires a further symmetry of the reading itself. The draft recognizes this
distinction rather than quietly assuming it.

This is one of the paper's strongest examples of how a simple formal structure can support a broader interpretation
without every part of that interpretation being a theorem.

*C. The Cauchy discussion is more careful than the headline initially suggests.* The paper does not simply announce
that the Cauchy distribution is universal. It eventually specifies the conditions under which the result holds:
- The reader's sweep is laid evenly by direction.
- The geometry uses the circular, Euclidean choice.
- The reading is v/h, with the appropriate normalization.
- The distribution belongs to that way of laying and counting the addresses, not necessarily to the world's payloads.

Under an even angular sweep, the tangent transformation produces the familiar Cauchy law. That is established
mathematics.

More interestingly, the paper distinguishes that exact distribution from the weaker conclusions that survive other fair
sweeps: a median at the corner and, under the stated tail condition, a nonexistent mean.

This qualification is intellectually important. It prevents the Cauchy from being presented as a necessary consequence
of every possible situated geometry.

*D. The paper is strongest when it shows what the framework cannot recover.* The discussion of star-shaped objects and
occlusion is particularly valuable. A single reading per direction can represent a radial outline when each direction
meets it once. It cannot encode multiple surfaces along the same direction without additional information.

That is a real limitation of the representation, not an embarrassing exception. It tells readers what the proposed
geometry retains and what it discards.

Likewise, the paper's scale argument is sound in its basic form: ratios alone cannot recover a common absolute scale. A
calibration length or another external amount is needed to fix that scale.

These limitations make the framework more credible because they give it identifiable boundaries.

**2. The central issue: what has been proved, and what has been chosen?**

This is where I would focus the next revision.

The draft moves among three different kinds of statements:
1. Mathematical consequences: results that follow from definitions and stated premises.
2. Modeling choices: the transformations, measure, norm and representation selected to model a reader.
3. Interpretive claims: statements about what geometry is, what an observer possesses, and what a distribution
   represents.

The paper sometimes moves from the first category to the third without sufficiently marking the transition.

For example, the claim that a situated reader's geometry is an addressing scheme is a productive definition and thesis.
But the fact that a ratio cancels a common factor does not by itself prove that all situated observation has this
architecture, or that the addresses exist independently of payload in every relevant sense.

Similarly, the equal-breadth drawing V = H is central to the construction. The draft argues that it gives a rigid unit
bar, a circle and the Cauchy distribution. But the paper also acknowledges that the Euclidean norm and the even-turn
measure are choices, not consequences of symmetry alone.

Those statements can coexist if the central result is phrased conditionally:

> Given the specified reader model, its equal-breadth drawing and its even angular sweep, the resulting address
> distribution is Cauchy.

That is a strong claim. It is also defensible in a way that the broader assertion that a situated geometry must take
this exact form is not yet shown to be.

The paper's own discussion of Drory's objection and alternative measures already provides the material needed to make
this distinction rigorous. I would elevate that qualification into the main argument, not leave it primarily to the
later discussion of assumptions.

**3. The main mathematical and logical pressure points**

These are the issues I would expect a demanding referee to pursue first.

*1. Is V = H necessary, or necessary for the chosen construction?* The paper makes equal breadths central to the
circle, rigid-bar sweep and standard Cauchy distribution. But it also recognizes that a different norm or sweep can
produce a square, a line, an ellipse or another distribution.

The important distinction is between proving that V = H is required for this particular rigid-bar model and proving
that it is required for a situated geometry at all. The first is defensible under the stated construction; the second
is broader than the premises currently establish.

Revision priority: State the scope of Proposition 3(e) and the conclusion of §5 with particular precision. The paper's
own acknowledgment of alternative constructions is the right foundation.

*2. The address/payload split is a model property; its broader significance needs a bridge.* Theorem 6(a) proves
cancellation of a common positive factor. It does not, by itself, prove that every magnitude arriving at an address is
irrelevant to every possible observation, or that the world is organized into addresses independently of an observer.

The draft partly handles this well: it states what the theorem establishes and what it does not. But other passages use
stronger language, such as calling addresses universal or saying geometry is not shapes.

Revision priority: Keep the strong conceptual thesis, but distinguish the formal result from its interpretation. Explain
what the model contributes beyond the familiar invariance of ratios under common scaling.

*3. The Cauchy result depends on how the sweep is measured.* The paper correctly admits that evenness is a choice. This
is crucial because uniform angle, uniform position along a curve and uniformity under another parameter need not
produce the same distribution.

Theorem 6(e) is useful precisely because it separates the robust result from the specific Cauchy form. But its
conditions should be made as explicit as possible: the exchange symmetry, the induced reading law, and the tail
condition governing the mean.

Revision priority: Put the conditional nature of the Cauchy result in the headline, abstract and principal
theorem—not only in the qualifications afterward.

*4. The normalized sum is not automatically the truth.* Section 2 calls h + v + v₂ = 1 a completed view and says that
the sum shows where the reader stands. Mathematically, normalizing nonnegative coordinates by their sum produces shares
that sum to one. That operation alone does not establish that those shares are the true breadths of an independently
existing system.

This is a critical point because the paper distinguishes unit relations from physical amounts so carefully elsewhere.

Revision priority: Clarify whether the simplex is a normalization of the unit relations, a representation of true
breadths, or a bridge between the two under additional assumptions. Those are different claims.

*5. The logarithmic address space is derived conditionally.* Proposition 4 is a solid result: an increasing function
whose multiplicative increments depend only on the scale factor has logarithmic form. The proof is appropriate.

The more vulnerable part is the claim that a reader with no preferred scale must use those increments. The draft
acknowledges in §11.2 that premise (S) is assumed rather than derived.

Revision priority: Preserve the logarithmic result as a conditional theorem and present the motivation for (S) as a
modeling principle. Do not imply that the functional equation proves the premise that leads to it.

One further technical check is worthwhile: audit every theorem's quantifiers and regularity assumptions. In
particular, Theorem 6(c)'s characterization of functions that commute with the mean should state the domain and
conditions on f clearly. The proof invokes the midpoint functional equation; if the result is intended for unrestricted
functions, monotonicity or another regularity condition must be addressed.

These are targeted mathematical checks, not reasons to discard the framework.

**4. The biggest presentation problem is repetition**

The paper has an unusually large explanatory burden. It introduces the same conceptual structure through the abstract,
introduction, results list, hand analogy, five situations, number-line construction, three vantages, corner, reader's
circle and Cauchy result.

Each presentation adds something, but their cumulative effect is to make it difficult to distinguish the argument's
essential steps from its supporting interpretations.

The strongest sequence is already present in the draft:
1. Define the reader's primitive: two bounded unit relations, h and v.
2. Establish the corner: the flip v/h ↦ h/v fixes the relation at 1.
3. Choose the drawing and measure: equal-breadth Euclidean circle and even angular sweep.
4. Derive the address distribution: the Cauchy law, conditional on that sweep.
5. Establish the limits: scale ambiguity, payload dependence, hidden surfaces and the role of external calibration.

I would use that sequence as the paper's spine. The five reader situations, lighthouse, Mercator, Archimedes, hand
analogy and mountain example can then support the argument where they add distinct value, rather than repeatedly
restating its foundations.

I would also reconsider the abstract. It introduces the transformation-group method, five situations, three vantages,
three breadth readings, the Cauchy distribution, median and mean, and the logarithmic address space before the reader
has a stable mental model. It is technically ambitious but overloaded.

**5. What I would preserve unchanged in principle**

I would not weaken the paper's fundamental ambition, and I would not turn it into a paper solely about the Cauchy
distribution.

The most valuable contribution is the proposed distinction between the observer's addressing structure and what that
structure addresses. The Cauchy distribution is a particularly informative result within that framework, not the entire
framework.

I would preserve these four elements:
- The corner as a structural invariant. It is the simplest, cleanest formal anchor.
- The separation of addresses and payloads. This gives the paper its distinctive thesis.
- The distinction between parallel and serial readings. It offers a concrete way to organize different observational
  standpoints without claiming that they are different physical dimensions.
- The explicit limits of recovery. Scale ambiguity and occlusion make the model's capabilities and limits testable.

The distinction between a completed representation and a situated one is also worth retaining, but it needs careful
language. A blueprint is not literally produced by an observer with no standpoint; it is a representation that
abstracts away from a particular standpoint. That distinction will matter to readers familiar with philosophy of
representation.

**6. Final assessment**

My strongest positive conclusion is that the paper has a coherent mathematical centre. The flip, corner, bounded reading
and conditional Cauchy result fit together. The work is not just a collection of analogies: it contains explicit
definitions, propositions and a principal theorem.

My strongest reservation is that the paper sometimes presents a successful construction as though it were the uniquely
necessary construction. Its own treatment of alternative norms, measures and logarithmic premises demonstrates why those
claims need to be separated.

The best next revision would not add more material. It would tighten the boundary between the mathematics and the
interpretation, audit the technical claims, and reduce repetition so the central derivation becomes unmistakable.

My verdict: 8/10 as a working paper, with real potential for external review after a focused revision. I would not yet
rate it as a fully established new geometry in the strongest sense claimed by its more ambitious passages. But I would
take its central proposal seriously, and I would not recommend abandoning or substantially diluting it. The next step is
to make the paper's strongest claims as rigorous as its best mathematics.

---

## Response (15 October, Claude)

Read against `papers/observation-from-somewhere.md` as it stands on the branch, which adds Proposition 5(f) and (g) to
the draft the review read. The review is fair and careful. Most of its pressure points are already met in the paper,
some in sections it names. It found one real gap, in Theorem 6(c), and two places where the paper's wording claims more
than its proofs.

### Point by point

**§1, what is strong.** Agreed. No action.

**§2, proved, chosen and interpreted; §3.1, is V = H necessary or necessary for the construction?** The paper already
scopes the claim in its propositions:
- Proposition 3(e): the attitudes are turns of one rigid bar *only if* V = H;
- Proposition 5(d): the readings follow the Cauchy at the corner *if and only if* c = 1;
- since 15 October, 5(f) and 5(g): the lighthouse's 45° flash is the corner, and a chart's bearings are true, only if
  c = 1.

Each says what V = H is required *for*. The front claims have been conditional since the ninth review: a chosen group,
and the sweep a rigid bar's turn. But two sentences read as unconditional:
- the abstract's "This is required.";
- the introduction's "its geometry requires that breadth to be its own".

The review is right that a reader could take these for the broader claim. Edit A names what V = H is required for at
those two places, as Tom's own ruling gave it (R215: "V = H is required because that that is what creates the unit
circle and cauchy requires a smooth turn").

**§3.2, the address/payload split needs a bridge; strong language.**
- *"Geometry is not shapes"* is the paper's stated thesis, set off as such in §1 ("Our thesis is this"). It is Tom's,
  from 29 September (SPN R91), and is kept.
- *"The addresses are universal"* (§7.4) says more than §7.4 shows. What it shows is that every shape laid evenly by
  direction opens into the same addresses. Edit C says that.
- *What the model adds beyond ratios being invariant under a common scale:* §7.8 ("What is known") already separates
  the classical facts from what is new, the reading. No edit.

**§3.3, the Cauchy is conditional on the measure; put it in the headline, abstract and principal theorem.**
- The abstract already says "when it sweeps this circle evenly".
- Theorem 6(e) already separates the robust core from the Cauchy's shape, with its conditions stated (a fair path and
  weight; a weight bounded away from 0 near the horizon).
- But Theorem 6 itself opens with no premises. Its parts (a)–(d) lean on Proposition 5's drawing and even sweep without
  saying so. Edit B gives the theorem a lead sentence stating them, and says that (e) drops both.

**§3.4, the normalized sum is not automatically the truth.** This is valid, and it is a case-keeping point the corpus
cares about. §1 says "The sum is where the truth lies", §2 "The sum also shows where a reader stands", and §3.1 "whose
sum h + v + v₂ = 1 holds the truth".

What the paper means is narrower:
- the triangle holds every way three breadths can share a whole;
- the true breadths, taken as shares, would be one point of it;
- normalizing the unit relations by their sum does not find that point. That takes the true breadths, which are amounts
  a situated reader does not read.

The bridge is the amounts; the triangle is geometry. Edit D says this in §2 and softens the two phrases in §1 and §3.1.

**§3.5, the logarithm is conditional.**
- Already so: Proposition 4 is stated "if r is increasing and satisfies (S)".
- §6 says (S) is "scale invariance of the lay's increments, motivated by Proposition 3(b) and assumed, not derived".
- §11.2, question 1, keeps it open.

Only the abstract's "if no scale is preferred, the only consistent layout is logarithmic" could be read as deriving
(S). Edit E names it as a premise there.

**§3, the technical audit: Theorem 6(c).** The review is right, and this is an error, not a wording matter. As written,
"Only an affine f commutes with the mean on every set of readings: for any f that is not affine there is a set X with
mean f(X) ≠ f(mean X)" is false for unrestricted f.
- Take a non-affine solution of Jensen's equation: an additive function A, built on a Hamel basis, plus a constant.
- A is linear over the rationals, so f(x) = A(x) + b commutes with the mean of every finite set:
  (1/n)·Σ(A(xᵢ) + b) = A((1/n)·Σxᵢ) + b.

The proof uses that f is strictly increasing, which the statement does not say. Monotone (or measurable, or locally
bounded) solutions of Jensen's equation are affine. The payload changes the paper considers are the strictly increasing
maps of 6(b), so restricting 6(c) to them changes nothing downstream. Edit F restricts it, and the proof already
covers that case.

The convexity clause (equality only if f is affine on the smallest interval containing X) is right. If equality holds,
every point of X lies on the supporting line at the mean, and a convex f lying above that line and touching it at
both ends of X agrees with it between them.

The rest of the audit the review asks for, done for the numbered results whose quantifiers carry weight:
- **Proposition 1:** "every sweep from home passes through x = 1" holds for a sweep in the paper's sense, from all of h
  to all of v; the proof uses continuity.
- **Proposition 4:** monotone solutions of the multiplicative Cauchy equation on λ ≥ 1 are logarithms.
- **Proposition 5(d):** as stated.
- **Theorem 6(b):** the converse holds for sets with the same ties.
- **Proposition 13(b):** a median is carried to a median by a strictly increasing f.
- **Proposition 14:** continuity is stated, as Aczél's theorem needs.

No other gap was found.

**§4, repetition and the abstract.** Not proposed. Tom ruled on 11 October that the reader is explained in full and
never folded into a short table (R203), and condensing was declined for the same reason on the seventh review (R232).

The review's five-step spine is already the paper's order:
- §3, the reader;
- §4, the corner;
- §5, the drawing and the circle;
- §7, the Cauchy;
- §9, the limits.

Whether the abstract should be shortened is Tom's call. One way would be to move the five situations and three vantages
out of it and keep the drawing, the corner, the Cauchy and the limits. That is not drafted.

**§5, what to preserve.** Agreed. On "a blueprint is not literally produced by an observer with no standpoint", the
review is right about the wording. §1 says "Geometry as usually written is drawn from nowhere ... Nagel (1986) called
this the view from nowhere." Edit G adds that this is a representation that abstracts from every standpoint, not a view
anyone takes.

**§6.** Its reservation ("a successful construction presented as the uniquely necessary one") is what edits A, B and C
answer. The lighthouse and Mercator's map, added since the draft it read, make the same point positively. V = H is
required there for something named (the corner at the 45° flash; true bearings), and the size is left free.

### Edits proposed (none made yet)

- **A.** Abstract and introduction: "This is required" becomes "This is required for the sweep to be a turn", and the
  introduction's item likewise. Only then is the sweep the turn of one rigid bar, the unit circle traced, and the
  Cauchy's median at the corner. Other constructions are in §11.2.
- **B.** Theorem 6 gets a lead sentence: "In (a) to (d) the readings are those of Proposition 5: the drawing V = H and
  an even sweep by direction; (e) drops both."
- **C.** §7.4: "The addresses are universal" becomes "The addresses are the same for every shape laid evenly by
  direction".
- **D.** §2: the triangle holds every way the breadths can share a whole; the true breadths, taken as shares, would be
  one point of it, but finding that point needs the breadths, amounts the reader does not read; normalizing the unit
  relations does not supply it. §1's "The sum is where the truth lies" and §3.1's "holds the truth" are softened to
  match.
- **E.** Abstract: "if no scale is preferred" becomes "if no scale is preferred (premise (S), assumed)".
- **F.** Theorem 6(c): stated for strictly increasing f (the maps of (b)), with a sentence noting that without a
  regularity condition the claim fails (non-measurable solutions of Jensen's equation).
- **G.** §1: the view from nowhere is a representation that abstracts from every standpoint, not a view anyone takes.
- **H.** The date line: 15 October 2026 (Proposition 5(f), (g) were added today).

Not proposed: condensing (R203, R232). The abstract's length is Tom's call.

### Made (15 October, about 05:11, at Tom's "yes"; SPN R259)

Edits A–H as proposed. Only the wording listed above changed; the paragraphs touched were re-wrapped, and a word-level
comparison against the previous text shows no other change.
- A in the abstract and the introduction's item. The introduction also says that sweeps which are not turns keep the
  corner and the missing mean but not the Cauchy's shape (Theorem 6(e), §11.2).
- B as Theorem 6's opening sentences.
- C in §7.4.
- D in §1, §2 and §3.1. §3.1's "Both known" entry keeps "the truth is one point of the triangle", since there the
  breadths are in hand.
- E in the abstract.
- F in Theorem 6(c) and its proof.
- G in §1.
- H the date line.

---

## Follow-up: ChatGPT on whether V = H is unique (shared by Tom, 15 October, about 10:32)

*Prefixed "chatgpt:"; a reply in Tom's conversation with ChatGPT after the "two choices" and "should, not does"
exchanges (SPN R260–R262). Kept as received, the LaTeX written plainly.*

Yes. I think that gets closer to the actual argument, and it exposes a weakness in my previous answer.

I treated V ≠ H as a different but still coherent drawing. You are pointing out that a drawing can be internally
consistent yet be a bad geometry for an observer who must sweep the environment smoothly.

Imagine an observer sweeping across a scene, from one direction to the next. The representation needs to preserve a
stable relationship between successive observations. Otherwise, the observer encounters distortions introduced not by
the environment, but by the observer's own representation rule.

If V/H = c ≠ 1 introduces a systematic mismatch, then the consequences could include:
- A displaced corner: the physical event corresponding to the geometric fixed point no longer falls at the intended
  location.
- A distorted sweep: equal changes in the sweep no longer produce the intended relationships between represented
  breadths.
- A broken correspondence: the reader's geometric addresses no longer line up with the landmarks that make the sweep
  coherent.
- Accumulated difficulty: the observer must compensate for distortions that the V = H assignment avoids.

The key point is not that alternative assignments are mathematically impossible. It is that they may impose a cost on
the observer's ability to operate successfully.

*The argument becomes stronger—and more demanding.* I would distinguish two claims:
1. Geometric claim: Under your stated requirements, V = H preserves the desired rigid-bar turn, corner alignment, and
   standard Cauchy reading.
2. Observer claim: A reader that must sweep its environment smoothly has a functional reason to use a representation
   that preserves those relationships.

The second claim explains why the geometry matters. It connects the mathematical construction to the observer's task.

But there is one important step to establish: does every c ≠ 1 actually introduce a sweep distortion, or can some
alternative assignment preserve smoothness while changing the scale or location of the corner? Smoothness alone does not
automatically establish uniqueness. You need to show that the relevant kind of smooth sweep requires the particular
alignments your construction provides.

If you can establish that, the conclusion is more consequential than "V = H is a convenient convention." It becomes:

> The assignment is selected by the operational requirements of successful observation, rather than imposed as an
> arbitrary mathematical preference.

That is the argument I would now stress-test—not the weaker claim that an observer can draw a consistent picture with
any value of c.

### Response (15 October, Claude)

The question is the right one, and its caution is right: **smoothness alone does not single out V = H.**
- Drawn at V = cH, the bar's tip runs on an ellipse, which is as smooth as a circle.
- OFS already notes this (§7.1, "Working back from the Cauchy", step 3): even steps of the ellipse's own parameter give
  the Cauchy at the corner.

What does single it out is something the sweep has beyond smoothness: it is **uniform** (every step the same map) and
it **returns** after one full turn.

**Claim (classical).** Let the sweep be a one-parameter group of linear maps of the (h, v) plane, g(t) = exp(tA), with
A ≠ 0 and g(T) = I for some T > 0. Then g preserves an inner product, unique up to a positive factor. In it, every point
the sweep reaches from all of h has the same length, and all of v is among those points. So the sweep draws V = H in its
own measure. The one free number is the factor, which is H.

*Proof.*
1. A real 2 × 2 matrix with exp(TA) = I has eigenvalues ±iω with ω = 2πk/T, k ≠ 0. A pair of zeros would make A
   nilpotent, and then exp(TA) = I + TA ≠ I.
2. So A = P(ωJ)P⁻¹, with J the quarter-turn generator, and g(t) = P·R(ωt)·P⁻¹. This preserves Q(x) = |P⁻¹x|².
3. Suppose B is any symmetric form preserved by every g(t). Then C = PᵀBP is preserved by every rotation, so it
   commutes with J.
4. Being symmetric, C is a multiple of the identity, so B is a multiple of Q.
5. All points of one orbit have equal Q. ∎

Checked in `ofs/periodic.py` on eight random changes of coordinates:
- the invariant inner product is unique up to a factor and positive definite;
- the page shows c from 0.54 to 27;
- in the sweep's own measure, all of v over all of h is 1 to 25 digits.

**What it means.**
- A drawing with c ≠ 1 is the same uniform sweep described in the page's coordinates rather than its own.
- Laid by the sweep's own parameter, its readings in unit relations are unchanged. What changes is where the page puts
  things, and which steps look even on the page.
- Proposition 5(d)'s c ≠ 1 is evenness taken in the page's angle, not in the sweep's.

So V = H is not one choice among coherent alternatives. It is the sweep's own measure, written down. What is chosen is H,
the factor, which is the "two choices" of R260 made exact.

In the follow-up's own words, the operational requirement is uniformity and return, not smoothness. Under it the
assignment is selected, up to the zoom.

The corner does not move either. v = h in unit relations is the half-way point of the sweep's own parameter. Only
its place on a page drawn at c ≠ 1 moves.

**Where it would go.**
- OFS Proposition 3, a new part (g), with the proof above. It lets (c) and (e) rest on uniformity and return in place of
  "a rigid bar", since the rigidity then follows.
- One sentence in "Two choices, and a number that is not one".

Proposed, not made: Tom set OFS's scope this morning (R258: "that's enough for this paper"), so this waits for his word.

### Made (15 October, about 10:40, at Tom's "yes"; SPN R263)

- **OFS Proposition 3(g)** and its proof. A sweep that is uniform, returns after a full turn and carries all of h into
  all of v in a quarter of it preserves an inner product, unique up to a factor. In it, all of h, all of v and every
  attitude between have one length, all of v is square to all of h, and (h, v) = (cos ωt, sin ωt). The sweep draws
  V = H in its own measure, and the factor is H.
- **Pointers to it:**
  - in "Two choices, and a number that is not one" (a drawing at c ≠ 1 is the same sweep in coordinates other than its
    own);
  - in "The Euclidean choice" (the assumption narrowed to a uniform, linear sweep);
  - in §11.2, question 2.
- **The check:** `ofs/periodic.py` now names 3(g).
- **Text comparison:** a word-level comparison against the previous text shows only these insertions. One rewrap first
  merged question 2's three-path table into its paragraph; it was caught by that comparison and restored before
  committing.
