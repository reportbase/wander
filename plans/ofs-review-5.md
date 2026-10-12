# Evaluation 5 of "Observation from Somewhere" (the foundational axioms)

*Shared by Tom on 12 October 2026 ("gemini response:"), of `papers/observation-from-somewhere.md` as it stands with
PR #89 merged (V = H required, Propositions 3(e) and 5(d), Proposition 14). Kept as received below; the response
follows.*

---

Math and physics reviewers will immediately target the foundational axioms where subjective geometric choices are presented as inevitable consequences of the situated reader's ignorance. While the internal logic is exceptionally tight, the pushback will focus on the unearned introduction of specific metrics and priors.

**The Uniform Angle Prior (The Cauchy Circularity)**
The derivation of the Cauchy distribution relies on the assumption that the reader sweeps in "equal steps of turn" from home. Statisticians and physicists will argue this is circular: the Cauchy distribution is precisely the tangent of a uniformly distributed angle. They will demand to know why a "blind" situated reader must natively sample space evenly by angle rather than sweeping evenly by linear ratio ($v/h$) or some other metric. While you explicitly acknowledge this in Section 7.5 as a "choice of weight," critics will argue this demotes the Cauchy result from a universal law of addressing to a mere consequence of an arbitrary sampling prior.

**The Euclidean Rigid Bar ($V = H$)**
You argue that assigning the mountain the reader's own breadth ($V = H$) is mathematically required because only then does the sweep behave as a "rigid bar" tracing a unit circle. Mathematicians will attack the sudden introduction of Euclidean geometry here. Why must the bar be rigid under the $L_2$ norm? If the observer's space operates under the $L_1$ norm (sum = 1), the geometry traces a flat line; if under the $L_\infty$ norm (largest = 1), it traces a square. You flag this gap in Section 11.2, but without a physical or information-theoretic mandate for the $L_2$ norm, the circle—and everything downstream of it—rests on an aesthetic preference rather than structural necessity.

**The Classical Separation of Address and Payload**
Your central thesis asserts that the geometric address space exists prior to and independently of the payload. Quantum physicists will fiercely reject this as a classical limitation. In quantum mechanics, the measurement context (the "addressing scheme") and the state (the "payload") cannot be decoupled; the act of laying an address fundamentally alters the payload. By isolating the address from the payload to explain why the Cauchy has a median but no mean, the framework ignores the observer effect central to modern physics.

**Condition (S) and the Haar Measure**
To derive the logarithmic layout past the corner, you introduce Condition (S): the premise that the room between $x$ and $\lambda x$ depends only on $\lambda$. Mathematicians will instantly recognize this as the Haar measure for the multiplicative group, which mathematically guarantees a logarithmic outcome. They will argue that Condition (S) is just the definition of a logarithm disguised as a postulate. You justify this by arguing a reader lacking a preferred scale must adopt this invariance, but physicists will counter that real observers *do* have intrinsic preferred scales—whether biological sensory limits, diffraction limits, or the Planck length.

**Dismissing Scale as a "Calibration Error"**
You relegate physical units and absolute amounts to an external construction, framing the discrepancy between the reader's unit and the true magnitude as a "calibration error" that merely shifts the reading across levels. Physicists view dimensional scale ($c$, $G$, $\hbar$) as the fundamental scaffolding of spacetime, not a secondary, arbitrary projection. Treating the true scale of the universe as an unknowable factor that merely offsets a logarithmic layout is a heavily Machian/relationalist stance that will face friction from those who view scale bounds as the primary drivers of physical laws.

Because you have anticipated many of these in the "Assumptions and open questions" section, the easiest way for reviewers to dismiss the paper is to say, "The author admits he chose the priors to get the result." How do you want to bridge the gap between "this is one valid geometric construction" and "this is the necessary geometry of observation"?

---

### Response (12 October, Claude; edits proposed, not yet made)

**Three of the five points are the paper's own open questions.** The even turn (§7.2, §7.5, §11.2 question 5), the
Euclidean norm (§5 "The Euclidean choice", question 2) and (S) as scale invariance (§6, question 1; §11.1 names the
Haar measures and Jeffreys's prior) are each already marked as assumed. The review's new pushes are the quantum one, the
preferred scales of real observers, and the closing question. Answering it turned up one result that changes the
picture for points 1 and 2.

**A finding: the main result's core does not need the circle.** Sweep each path from all of h to all of v evenly along
its own length, and read v/h (four million draws each):

| path | norm | quartiles of v/h | flip pairs | r·P(v/h > r) at 10², 10³, 10⁴ |
|---|---|---|---|---|
| the quarter circle | L₂ | 0.415, 1.001, 2.415 | to 0.002 | 0.64, 0.63, 0.68 (2/π) |
| the square | L∞ | 0.500, 1.000, 2.000 | to 0.001 | 0.50, 0.51, 0.50 (½) |
| the line h + v = 1 | L₁ | 0.334, 1.001, 3.001 | to 0.002 | 0.99, 1.00, 1.06 (1) |

All three put the median at the corner, all three are unchanged by the flip, and all three fall as c/r, so none has a
mean. Only the exact quartiles √2 ∓ 1, the Cauchy's own shape, need the circle. The reason is short and general: a path
and a weight unchanged by exchanging the parties give v/h the same law as h/v, so the median is 1; and any weight that
does not vanish at the horizon puts mass of order 1/r beyond r, so the mean diverges. So what the paper's main result
uses (order survives, the median sits at the corner, sums fail) rests on the exchange of parties, not on L₂ and not on
the uniform angle. The circle and the even turn give the Cauchy in particular. This is provable in a few lines and
could be added to §7 as a proposition.

**1. The uniform angle prior.** Partly right, and the finding answers most of it. The Cauchy's exact form does follow
from the even turn, which is classical and is said (§7.1). What the paper claims as its main result, Theorem 6, does not
depend on the weight: the reach cancels from every reading, order survives every increasing map, only affine maps
commute with the mean (§7.2, "What does not depend on that choice"). And by the finding, the median at the corner and the
missing mean hold for every exchange-symmetric weight. "Even in v/h" is not an option: v/h runs over [0, ∞), where no
even probability exists. The even turn is the one weight on directions that every turn leaves unchanged; that is the
argument of §7.5, and it is a reason, not a proof.

**2. The Euclidean rigid bar.** The review reads V = H as resting on L₂ rigidity. Since PR #89 it rests on more than
that: Proposition 5(d) gets V = H from the Cauchy by an even turn of direction, whatever the bar's length does, because
readings are directions only (Theorem 6(a); §7.4, "The shape is payload"). The norm enters only through the measure on
directions. With the finding, the core of the main result needs neither. What stays open is narrower than the review
says: why the reader's weight on directions is the turn-invariant one (questions 2 and 5 become one question).

**3. Quantum measurement.** Out of scope, and the paper should say so in one line. Theorem 6(a) assumes that what
arrives is the same whichever address meets it; a reading that disturbs its object, as a quantum measurement does, is
outside the framework. The paper already says it "makes no claim about physics" (§1). Whether quantum mechanics is a
counterexample or a further case (the measurement basis is chosen before the state is met, which is an address laid
first) is a question for `physics.md`, not for this paper.

**4. (S) and the Haar measure.** Agreed that (S) is the multiplicative Haar measure, and the paper says (S) is assumed
(§6, §11.1). On preferred scales: a real reader's step, a diffraction limit or a Planck length set where its lay stops,
the count of levels (§8), not the lay's form within the range it resolves. That is a reading with a testable side:
Weber's law holds over middle ranges and fails near threshold, which is a cut-off at the ends and a logarithm within
(known; whether it holds in the corpus's measured readers is NLE and GRD's business).

**5. Scale as calibration error.** The paper is less Machian than the review reads it. Proposition 8 is the geometry's
form of what dimensional analysis already holds: only ratios are read, and units come from constants. Since 2019 the SI
fixes its units by agreed values of c, h and other constants: these are the outside amounts of Proposition 8(b), agreed
as in §9's "What a unit is". So the constants are not dismissed; they are what fixes the scale. That belongs in
`physics.md` (the dictionary has "a known constant" as a bridge), not in OFS, which has no physics.

**The closing question: conditional necessity.** The paper should not claim "the necessary geometry of observation"
outright, and it does not need to. The defensible claim is necessity relative to a stated ignorance, the way invariance
arguments are made (Jaynes 1968, already cited):
- one premise, the candidate principle of §11.1: the reader does not know its attitude (turns), its scale (dilations) or
  which party is which (the exchange);
- from it, each choice the review calls unearned follows: the even turn (the turns' invariant measure), the logarithm
  past the corner (the dilations'), the corner and the median (the exchange), V = H (the exchange, and Proposition 5(d));
- each relaxation gives a named alternative, not chaos: a preferred direction gives the square's or the line's law; a
  preferred scale, a cut-off; a preferred party, c ≠ 1 and the Cauchy off the corner;
- and the main result's core holds under the exchange alone, whichever weight.

So: necessary given the ignorance, and the address/payload split robust to the weight. That turns "the author chose the
priors" into "the priors are the ignorance, stated once, and the core survives changing them".

### Proposed edits to `observation-from-somewhere.md`

- **(A) A proposition in §7.2 on what survives a change of weight:** for any path and weight unchanged by exchanging the
  parties, the reading's law is unchanged by the flip, its median is the corner, and if the weight does not vanish at the
  horizon its mean diverges; the circle and the even turn give the Cauchy in particular. With the three-path table.
- **(B) §5, "The Euclidean choice":** say that readings are directions only, so the norm enters only through the measure
  on directions; and merge §11.2's questions 2 and 5 into one.
- **(C) §11.1 and the introduction:** state the paper's claim as necessity relative to the stated ignorance, with the
  relaxations and what each gives.
- **(D) §11.2, "Where the conclusions do not follow":** a reading that disturbs what it reads is outside the framework.
- **(E) §8 or §11.2 question 1:** a real reader's preferred scales set where its lay stops, not its form within range.
- **(F) `physics.md`, not OFS:** the SI's constants as the agreed outside amounts of Proposition 8(b).

### Made (12 October, SPN R217; Tom: "Yes, make the proposed edits")

- (A) Theorem 6(e), "The median and the missing mean need only fairness", with its proof; the diamond added to §7.4's
  table (0.500, 1.000, 0.976, 0.976, exact) and the means to its text; a bullet under "What does not depend on that
  choice"; a sentence in the abstract and in the main result's bullet of the introduction.
- (B) "The Euclidean choice" (§5): the norm reaches the readings only through the measure on directions. §11.2's
  questions 2 and 5 made one.
- (C) §11.1, "What is claimed, then": necessity relative to a stated ignorance, with each relaxation's alternative;
  the introduction's last paragraph says so.
- (D) §11.2, "Where the conclusions do not follow": a reading that disturbs what it reads.
- (E) §11.2, question 1: a preferred scale sets where the lay stops, not its form within range.
- (F) `papers/physics.md`: a dictionary row and an iteration note, the SI's constants as the agreed outside amounts.

---

### Second part, shared the same day

*Tom: "essentially the pusback is that there maybe more reader situations with yet more geometries." Then Gemini's
reply, kept as received (stray "MD" markers from the copy removed):*

That is exactly the pressure point. By framing the five situations as an exhaustive binary tree—based on whether there is an h, whether V is known, and whether the system holds still—the paper invites critics to invent physical states that break those binaries, spawning new situations.

If mathematicians and physicists can prove your decision tree is incomplete, they can introduce alternative geometries that don't inevitably lead to the Cauchy distribution or the circle. Here is where they will try to insert new situations:

* The Superposed Situation (Quantum): You define knowledge of V as either held whole (Situation 1/2) or unknown (Situation 3/4). A quantum physicist will argue for a situation where knowledge of V is probabilistic, or where the reader is entangled with the payload. If measuring v fundamentally alters h, the geometry requires a non-commutative algebra, not a simple scalar ratio on a unit circle.

* The Causally Disconnected Situation (Relativistic): Your serial reader sweeps from home to the horizon. A relativist will point out that light cones impose strict boundaries. What is the geometry of a reader when a section of the hemisphere isn't just "turned away" or waiting to be swept, but is fundamentally blocked by a causal horizon? This might require hyperbolic geometries beyond your logarithmic far-field.

* The Fluctuating Thumb: Every situation in your framework assumes H (the thumb) is definitively held by the reader. Critics dealing with fundamental physical limits (like the Planck scale) will ask for the geometry of a reader whose own baseline is uncertain or fluctuating. If H is a distribution rather than a fixed scalar, setting V=H yields a different probability space entirely.

* The N-Dimensional Holographic Situation: You model the sweep as a 1D relation (a turn) or a 2D sphere. If the fundamental bound of observation is a surface area (as in holographic bounds), physicists might argue the fundamental unit relation should be an area ratio, which alters how the Haar measure scales the addresses past the corner.

To defend against the "infinite situations" critique, you essentially have two structural moves you can make before finalizing the draft:
Option A: The Epistemological Shield
Double down on the binary tree. You can argue that regardless of underlying physical weirdness (quantum superposition, relativistic frame-dragging), the act of a reader taking a measurement forces the data into one of these classical cognitive states. The geometry belongs to the address space of the reader's mind/instrument, not the universe, so the physical state of the universe cannot add new branches to the reader's logic tree.

Option B: The Physical Scoping
Explicitly scope the paper to classical, commutative observation. Acknowledge in Section 11.2 that relativistic causal bounds, quantum entanglement, and Planck-scale ruler fluctuations are valid states that break the binary tree, and position the derivation of their specific geometries as the next necessary expansion of the framework.

Which defensive posture feels more aligned with where you want to take the larger theory?

### Response to the second part (12 October, Claude; edit G proposed, not yet made)

**The tree is exhaustive for what it asks, by construction:** three questions, each with two answers. The real pushback
is whether other questions matter. Each of the four proposed lands in something the paper already has: the payload, the
amounts, or a power of the reading. None of them changes the address geometry.

1. **Superposed.**
   - *Knowledge of V as a probability* is the one missing number known within bounds or as a distribution: situation 3
     or 4, with Proposition 13 (§3.8).
   - *Measuring that changes the object* is outside Theorem 6(a)'s premise, now said in §11.2 (edit D). It is a change
     in what arrives, not in where it is laid.
   - *Quantum states may be a case rather than a counterexample* (a reading, for `physics.md`). A real qubit's
     amplitudes are a pair of unit relations on the circle: h² + v² = 1 is the normalisation, and the corner is the equal
     superposition. Numbers from two million draws each:
     - a Haar-random real qubit's amplitude ratio is the Cauchy (quartiles 0.414, 1.001, 2.410);
     - a complex qubit's ratio of shares |b|²/|a|² follows the line's law (0.333, 0.998, 2.997; tail 1.02/r);
     - its ratio of amplitudes |b|/|a| has a mean (tail as 1/r²), because its weight vanishes at the horizon, which is
       Theorem 6(e)'s condition seen from the other side.
2. **Causally disconnected.** A horizon that nothing crosses leaves its addresses laid and empty: payload. The
   hyperbolic geometry of relativity is the levels' own. MOT run 3 showed rapidity is the reader's lay of celerity
   smoothed and a boost a pan in levels, and §11.1's group is PSL(2,ℝ), the hyperbolic plane's.
3. **The fluctuating thumb.**
   - Readings are ratios of amounts in one unit, so H cancels from every reading (Proposition 8(a)), and "setting
     V = H" does not change the readings' probability space.
   - A thumb that changes between looks makes each look a reader of its own. Joining them is §9's shared unit, or
     STC's outside amount.
   - A thumb that wavers within a look blurs the step (§8).
   - So it affects amounts, not the geometry.
4. **Holographic: area ratios.** An area ratio is a power of the reading, (v/h)². Order, the corner (1² = 1), the flip
   and the median are unchanged by any power, and the levels rescale by the exponent: two levels of area per level of
   length, as light's two levels per level of distance (`plans/mag-plan.md`). There is no new geometry.

**Posture: neither A nor B as stated.**
- Option A's "classical cognitive states" and "the reader's mind" claim more than the paper proves, and invite the same
  pushback one level down.
- Option B concedes that relativity, Planck-scale fluctuation and higher dimensions break the tree, which the four
  checks above say they do not.
- The paper's own position is a third: the situations classify **what a reader knows of the two breadths and how it
  holds its readings**, and are exhaustive for that. Physics changes what arrives (payload), the amounts, or the exponent
  of a reading, and the address invariants (the corner, the flip, order, the median, no mean) survive each. One premise
  has an honest edge, the disturbing reading, and is now scoped (edit D).

**(G), proposed.** Extend §3.1's "Cases that look like a sixth reduce to these" with four entries:
- V known as a distribution;
- a horizon that nothing crosses;
- a thumb that changes between looks;
- a reading of an area or another power of the relation.

Each would get one line saying where it lands.
