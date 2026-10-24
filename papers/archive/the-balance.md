# The Balance

### A working paper on the centre of gravity as the primitive read

*Working paper, first draft. Same conventions as the main corpus: **grade tags** in backticks mark what is proved, verified, motivated, or merely suggested; **open** marks a live question; **correction** marks something this paper gets wrong on an earlier telling and fixes here. Executed checks are in the appendix and in `balance_checks.py`. Nothing here is submission-ready and it is not meant to be — this is a substrate to iterate on.*

*Relation to the main corpus: §1.08 (the beam) and §1.09 (the pulse) are the parent sections. This paper argues that both sit on something more primitive, which is why it is being written separately rather than as an amendment.*

---

## 0. The read

Put two quantities on a balance. What comes back is

$$b \;=\; \frac{A-B}{A+B} \;\in\; (-1, 1).$$

It is not their difference, which would carry units. It is not their ratio, which is unbounded and undefined when a pan empties. It is a **bounded coordinate on their ratio**, and the three properties that matter follow from writing it the other way:

$$b \;=\; \tanh\!\Big(\tfrac12 \ln \tfrac{A}{B}\Big).$$

Ratios multiply. Log-ratios add. And $b$ is the bounded coordinate on that addition — a logarithm that turns $\times$ into $+$ and then keeps the result in a box. That is the whole instrument, and everything below is a consequence of it.

Two coordinates, then, and the paper will use both throughout:

- the **inner** coordinate $\varphi = \tfrac12\ln(A/B)$ — unbounded, additive, the rapidity;
- the **outer** coordinate $b = \tanh\varphi$ — bounded, non-additive, what the instrument shows.

The corpus's hold and read, in brass.

---

## 1. Weights add, comparisons don't

The sloppy version of this paper's thesis invites an immediate and correct objection: *no it doesn't, weights just add.* The precision matters, so it goes first.

Adding weight to a pan is additive, obviously and boringly. What is not additive is **chaining comparisons**. Weigh $A$ against $B$; weigh $B$ against $C$; the comparison of $A$ against $C$ is not the sum of the two tilts. It is

$$b_{13} \;=\; \frac{b_{12} + b_{23}}{1 + b_{12}b_{23}},$$

which is relativistic velocity addition, exactly and not approximately. `[clean; B1 verified to $10^{-13}$ over $2\times10^5$ random triples]`

So the instrument has two layers and they obey different arithmetic:

> **The additive structure lives in the pans. The $\tanh$ structure lives in the reads.**

This is the corpus's hold/read distinction, physically realised in one object — and a considerably better argument for that distinction than the algebra in §5, because you can point at it. Whether it should therefore *replace* §5's presentation is **open**.

---

## 2. The steelyard: division is never executed

A Roman steelyard weighs by sliding a counterweight along a graduated arm until the beam levels. It never forms a quotient. It **finds the position at which the pair cancels**, and the read is a location on the arm, not a number in a register.

That is the corpus's founding discipline — *hold the pair, never execute the quotient* — implemented in bronze roughly two thousand years before anyone wrote the premise down. `[clean]`

The observation is not decorative. It answers the question of what "never executing the quotient" could possibly mean operationally, and the answer is: **settling is not dividing.** A quotient is a computation performed on two numbers. A balance point is a state a system relaxes into. The first has an $O(N)$ cost and a division by zero; the second has neither.

If this working paper has one image, it is the steelyard.

---

## 3. The horizon: reached only by annihilation

$b = \pm 1$ requires $B = 0$. No finite weight added to $A$ ever gets there — $b \to 1$ asymptotically and arrives nowhere. The extreme is reachable **only by emptying a register, never by loading one**. `[clean]` *(True **in the read chart**. On the dial the horizon is an ordinary point at arc distance $\pi/2$ with neighbours at the ordinary spacing (§27.1, §27.6), and §31.1 supplies the geometry the asymptote was reporting: $b = \pm1$ are the ideal endpoints of a geodesic of $H^2$, at infinite hyperbolic distance — which is exactly why no finite loading reaches them.)*

This is the corpus's seam (§1.45) stated without metaphor: the horizon is an address, not a destination. Accumulation approaches it forever; annihilation is at it immediately. The two routes are not two speeds along one road — they are different kinds of act, and only one of them is a journey.

And the physical reading of the corresponding relativistic fact is the same sentence: you can always add more velocity, and you never arrive; but a massless thing is *at* the horizon, having never travelled there.

---

## 4. The centre is free, and here is why

Now the part this paper exists for.

**Everything finds its centre of gravity for free.** A beam settles at it. A free rigid body rotates about it. A system of particles moves as though all its mass sat there and every external force acted there — regardless of how complicated the interior is. Nobody computes it. It simply is where the system is.

The reason is that **the centre of mass is the one point a system defines without being given an origin.** Positions require a coordinate frame; a mass-weighted mean of positions does not, because it transforms correctly under translation. It is the system's own address rather than one assigned from outside.

And that freeness is Noether's: momentum is conserved because space is homogeneous, and the inertial motion of the centre of mass is that conservation law wearing a different hat. `[clean, standard]`

Which lands precisely on the corpus's third premise. P3 says the observer has no external scale. The centre of gravity is the physical demonstration that a system can **supply its own origin** — so P3 is not an ascetic restriction the observer suffers under, it is a description of what physical systems already do. The beam does not merely illustrate the atom. It supplies the atom's origin. `[strong-motivated]`

---

## 5. The cost inversion

*Computing* a centre of mass is $O(N)$: sum over all the parts, weight by mass, divide by the total.

*Exhibiting* one is $O(1)$: the beam settles, and it settles just as fast with a million grains in the pan as with two.

So the world performs the $O(N)$ sum for free and hands over the result at $O(1)$. `[clean]`

This is worth more to the corpus than it currently extracts from it. §7's cost ladder argues that a bounded observer cannot afford $O(N)$ and must therefore work at $O(1)$, $O(\log N)$, or $O(K)$. The obvious objection is that this is a definition dressed as a theorem. The balance answers it: the observer does not need to afford $O(N)$ **because the world has already run the sum and is presenting the answer**. That is the front matter's "the observer supplies the algebra, the world supplies the pair," made concrete enough to weigh.

`[open]` — is there a general statement here? Something like: *every conserved quantity is a free $O(N)$ read*. Total momentum, total charge, total energy — each is a sum over parts that the world exhibits without anyone summing. If that holds, the cost ladder's cheap rungs are exactly the conservation laws, and §7 gains a principled account of *which* $O(N)$ quantities are free rather than a blanket prohibition. This looks promising and has not been checked.

---

## 6. Centre → pulse → beam

§1.09 orders the two archetypes: the pulse is the case, the beam is the pulse stopped. It says the pulse is "a reach out from the centre and back," measured "against nothing but its own centre."

That centre is a centre-of-gravity read, and it is prior to both. The pulse needs an origin to reach *from*; the balance is what supplies it. So the ordering has one more floor under it:

$$\textbf{centre} \;\longrightarrow\; \textbf{pulse} \;\longrightarrow\; \textbf{beam}$$

The centre makes "out" meaningful. The pulse traverses. The beam stops the traversal and reads it. `[strong-motivated]`

This is not a correction to §1.09 so much as a foundation for it — but it does change what the corpus should lead with, and §1.09's claim that the pulse is "older than the balance, older than any instrument" needs one qualifier: older than any *instrument*, yes; not older than the centre, which is what makes the reach a reach and not a drift.

---

## 7. Curvature is the price of a centre

A centre is a weighted mean. On a flat space, means are free — the naive average of two points *is* the point halfway between them, exactly, at every separation. On a curved space this fails: the ambient average leaves the space, and pulling it back costs a correction that is proportional to the curvature.

Executed (`B3`): the midpoint of two points separated by geodesic distance $d$.

| separation $d$ | sphere $K=+1$ | flat $K=0$ | hyperbolic $K=-1$ |
|---|---|---|---|
| 0.01 | $1.25\times10^{-5}$ | **0** | $1.25\times10^{-7}$ |
| 0.10 | $1.25\times10^{-3}$ | **0** | $1.24\times10^{-4}$ |
| 0.50 | $3.21\times10^{-2}$ | **0** | $1.39\times10^{-2}$ |
| 1.00 | $1.39\times10^{-1}$ | **0** | $8.13\times10^{-2}$ |
| 2.00 | $8.51\times10^{-1}$ | **0** | $2.80\times10^{-1}$ |

Flat is exactly zero at every separation. Both curved cases open at order $K d^2$. `[clean, verified]`

Which gives the paper's central claim:

> **Curvature is the price of a centre. Where the centre is free, the space is flat; where it is not free, the deficit measures the bend.**

And a corollary that fits the corpus's temperament: this is a **flatness test with no ruler in it**. You do not measure angles or distances. You check whether centres compose. `[strong-motivated]`

`[open]` — is the biconditional exact, or exact only for constant curvature? The suspicion is: exact for constant curvature, approximate otherwise, with the failure governed by the variation of $K$ across the region spanned. Since both branches of the corpus's fork are constant-curvature, this would be sufficient — but it is unchecked and should not be asserted in the strong form until it is.

---

## 8. The two centres, and the gap that is the tide

The elementary version of §7 is better than the differential-geometric one, and most people learn it and never connect it.

**Centre of mass and centre of gravity coincide only in a uniform field.** The moment the field varies, they separate — and their separation is the tidal term. Tidal terms are curvature.

Executed (`B4`): a dumbbell of length $L$, two equal masses, in a $1/r^2$ field at range $R$.

| $R/L$ | gap$/L$ measured | $L/2R$ |
|---|---|---|
| 5 | $9.9010\times10^{-2}$ | $1.0000\times10^{-1}$ |
| 10 | $4.9875\times10^{-2}$ | $5.0000\times10^{-2}$ |
| 50 | $9.9990\times10^{-3}$ | $1.0000\times10^{-2}$ |
| 200 | $2.4999\times10^{-3}$ | $2.5000\times10^{-3}$ |
| 1000 | $5.0000\times10^{-4}$ | $5.0000\times10^{-4}$ |

The gap goes as $L^2/2R$ — first order in the field *gradient*, vanishing in the uniform limit. `[clean, verified]`

So "the centre of gravity creates curvature" is close to literally true, and the precise form is: **the two centres agreeing is flatness; the gap between them is the bend.** A body large enough to feel the difference between its two centres is a body that can detect curvature without leaving home — which is the equivalence principle stated from the balance's side.

---

## 9. Thomas precession, reached from the balance

Two tilts do not compose to their average; the whole discrepancy is the $b_1 b_2$ term in $(b_1+b_2)/(1+b_1b_2)$. That term is not a formula quirk. Relativistic velocity space is hyperbolic with curvature $-1/c^2$, and the failure of two boosts to compose into a boost is exactly the **angular defect of a geodesic triangle** in it.

Executed (`B2`): a right hyperbolic triangle with perpendicular rapidity legs $a$, $b$; defect $= \pi/2 - A - B$ against the Wigner angle $\tan\omega = \sinh a \sinh b/(\cosh a + \cosh b)$.

| $a$ | $b$ | defect | Wigner angle | $|$diff$|$ |
|---|---|---|---|---|
| 0.30 | 0.40 | 0.058755553472 | 0.058755553472 | $9\times10^{-17}$ |
| 0.80 | 0.50 | 0.185578739798 | 0.185578739798 | $6\times10^{-17}$ |
| 1.20 | 1.70 | 0.710762015102 | 0.710762015102 | $0$ |
| 2.00 | 0.90 | 0.621792162296 | 0.621792162296 | $1\times10^{-16}$ |
| 0.05 | 0.07 | 0.001748920977 | 0.001748920977 | $10^{-16}$ |

Identical to machine precision. `[clean, verified]`

> **Two boosts fail to close for the same reason a triangle on a saddle has angles summing to less than $\pi$.** Gauss–Bonnet: defect $=|K|\times$ area.

This is the corpus's §13.9 Tier-1 result — *"the angle equal to the loop's rapidity-area"* — arrived at from the balance side with no register generators and no algebra. That matters for transmission more than for content: it means there is a route from a set of scales to Thomas precession that a reader can walk. **Centres are free in flat space; they cost in curved space; what they cost is the curvature; and the cost, for velocities, is a rotation nobody applied.**

---

## 10. The alias family, and where it splits

The read $b = (A-B)/(A+B)$ is taught in a dozen fields under a dozen names, always as *normalisation* — divide by the total to make it dimensionless — and every field stops there. Centre of gravity. Michelson contrast. Polarisation. Asymmetry parameter. Reflection coefficient $\Gamma = (Z-Z_0)/(Z+Z_0)$. Fractional difference. Fermi–Dirac occupancy, via $p = A/(A+B) = (1+b)/2$. Logistic output, softmax of two, Boltzmann weight of a two-level system. The drift-diffusion decision variable, which accumulates a log-likelihood ratio to a bound — the inner coordinate, run to a horizon.

What nobody says next is: **and therefore these do not add.**

But the family is not uniform, and this is the check that matters (`B1`). The composition law holds exactly **iff the underlying quantity chains transitively**:

| alias | chains? | max error over $2\times10^5$ triples |
|---|---|---|
| impedance $Z_1{:}Z_2{:}Z_3$ | yes | $2.2\times10^{-14}$ |
| weights $A{:}B{:}C$ | yes | $8.9\times10^{-14}$ |
| odds $o_1{:}o_2{:}o_3$ | yes | $1.0\times10^{-11}$ |
| intensity $I_1{:}I_2{:}I_3$ | yes | $1.3\times10^{-12}$ |
| **correlation** (Fisher $z$) | **no** | — |

Fisher's $z = \operatorname{artanh} r$ shares the *transform* and not the *composition*: correlations have no transitive chaining, and given $r_{12}=0.6$, $r_{23}=0.5$, the third correlation is only **bounded** to $[-0.393, 0.993]$. The composition law would return the single value $0.846$, which is wrong. `[clean, verified]`

So the family splits, and the split is informative:

> **Transitive-ratio quantities compose. Tanh-transformed statistics merely share the coordinate.**

Any claim that "everything is the balance read" must respect this line, and the corpus's §1.8 known-domains table should be audited against it. `[open]`

---

## 11. The body: weight-shifting, not falling

`[correction]` — an earlier telling of this got the phenomenology wrong, and the error is instructive.

It is tempting to say that the felt quality of nearly losing your balance — that it gets harder and harder and you never quite arrive — is $\tanh$ saturation, felt from inside. That is wrong, because two different physical systems are involved:

- The **hanging balance**, pans below the pivot, is *stable*. It settles at an angle, monotone in the log-ratio, and never goes vertical. This is the $\tanh$.
- **Standing** is an *inverted* pendulum — unstable, with a basin of attraction whose edge you can cross, after which you fall. The felt point of no return is a separatrix, not an asymptote.

The correct embodied hook is **weight-shifting**. Rock from one foot to the other, or from heel to ball: the pressure ratio saturates. You can always shift a little more, and while both feet are down you never reach all-on-one. *That* is the bounded read, and postural control regulates exactly this quantity — the centre of pressure, $(L-R)/(L+R)$, computed continuously by the vestibular system and the soles of the feet.

Which makes this plausibly **one of two arithmetics the body performs natively** — the other is the sign-and-halve count of §21.4, run by circadian biology and verified to $3.4\times10^{-13}$, which §29.5 names the third and only accumulating verb. Everything else we do with symbols. *(First written as "the only arithmetic"; corrected at §35.7.)* `[strong-motivated]`

Falling is a real phenomenon that happens in the same body and is not this one. Keeping them apart makes the metaphor more useful, not less.

---

## 12. Two axes: holonomy that gymnasts feel

One-dimensional balance is abelian. Two-dimensional balance is not: tilt forward then right and you end up facing somewhere different than right then forward.

This is felt, routinely and by non-physicists. The twisting somersault and the cat-righting reflex are holonomy in the rotation group, executed by a body under no external torque — a diver changes orientation without changing angular momentum, purely by cycling through shapes. That is a closed loop in shape space with a rotation left over, which is §13.10's $SO(3)$ result performed by people who have never heard of it. `[strong-motivated; the falling-cat literature is well developed — Kane & Scher, Frohlich — and should be cited rather than rediscovered]`

`[open]` — is there a *felt* two-axis version of the Wigner rotation specifically, as opposed to general shape-space holonomy? The two are related but not identical, and conflating them would be exactly the kind of resemblance-noticing this programme is supposed to avoid.

---

## 13. Weber: the inner coordinate and the outer one

Weber's law says the just-noticeable difference is proportional to the stimulus — $\Delta\log = \text{const}$. That is a statement that the natural discrimination coordinate is the **log-ratio**: the inner coordinate, $\varphi$.

But what a perceptual system *reports* is bounded. Judgements saturate; confidence saturates; the pressure ratio under the feet saturates.

So the structural conjecture is that perception uses **both** coordinates and for different jobs: the inner one for discrimination, the outer one for report. `[conjecture]`

This is measurable — centre-of-pressure data against perceived tilt — and it is the same question as the corpus's $n > K$ density thread, where a bounded reader above its capacity recovers density rather than count. Those look like one investigation rather than two, and if they are, the balance is the place to run it, because it is the one domain where the physical quantity and the felt quantity can both be instrumented.

---

## 14. Answering open question 1: which conserved quantities are free

*(This section resolves the question §5 raised, and the answer is **no** — not every conserved quantity is a free read. The correct statement is narrower, sharper, and more useful, and testing it split the hypothesis in two. Executed: `free_reads.py`, Q1–Q4.)*

### 14.1 The mechanism is the boundary, not the conservation

The hypothesis that survives is not *conserved ⟹ free*. It is:

> **A quantity is a free read iff it is a boundary functional — iff its bulk sum equals an integral over the boundary.**

Conservation matters only because it *supplies* that form. The chain is:

$$\text{symmetry} \xrightarrow{\text{Noether}} \text{conservation} \Rightarrow \text{a continuity equation} \xrightarrow{\text{divergence theorem}} \text{a boundary form} \Rightarrow \text{a free read.}$$

Locality is the load-bearing link. A conserved quantity with a conserved *current* has $\int_V \rho = \oint_{\partial V}$, and a boundary is something an observer can stand outside of. A conserved quantity without a current has no such reduction and must be visited. `[strong-motivated]`

### 14.2 The cost decouples from $N$ — executed

$N$ point charges inside unit radius, flux read on a sphere at $R=3$ sampled at $M$ points (`Q1`):

| $N$ | $M$ | bulk sum, $O(N)$ | boundary flux, $O(M)$ | rel. err |
|---|---|---|---|---|
| 10 | 2000 | 5.924063 | 5.924065 | $3.2\times10^{-7}$ |
| 1000 | 200 | 798.709996 | 798.713671 | $4.6\times10^{-6}$ |
| 1000 | 2000 | 798.709996 | 798.710072 | $9.5\times10^{-8}$ |
| 20000 | 200 | 16830.642333 | 16830.631623 | $6.4\times10^{-7}$ |
| 20000 | 2000 | 16830.642333 | 16830.642326 | $4.2\times10^{-10}$ |

Relative accuracy is set by $M$ — the observer's aperture resolution — and is flat to improving across three decades of $N$. `[clean, verified]`

And for a *distant* observer the boundary collapses to a single sample (`Q2`): with the observer at the centre of gravity so the dipole vanishes, one field reading recovers the total with relative error $0.06\,(a/R)^2$ — constant coefficient across $R/a$ from 10 to 383.

So the cost is a three-tier ladder, and **the tier is set by the observer's relation to the boundary, not by the quantity**:

| observer | cost | what it gets |
|---|---|---|
| distant, one read | $O(1)$ | the total, to $(a/R)^2$ |
| enclosing, resolved | $O(M)$, $M \perp N$ | the total, to aperture accuracy |
| visiting every part | $O(N)$ | the distribution |

This is what §7 has been missing. Its cost ladder asserts that a bounded observer works at $O(1)$, $O(\log N)$ or $O(K)$ and never $O(N)$, and the standing objection is that this is a definition dressed as a theorem. The balance answers it: **the observer need not afford $O(N)$ because the world has already run the sum and is presenting the result at its boundary.** That is a mechanism, not a stipulation.

### 14.3 The negative control holds

Entropy is the test the hypothesis had to fail correctly, and it does (`Q3`). Two states of $N=1000$ particles with total energy 1500 and zero total momentum — one equipartitioned, one with all energy in a single atom — agree on *every* conserved total and differ in entropy by $4.2\times10^4\,k_B$. There is no conserved entropy current and therefore no surface integral that separates them. `[clean]`

Corroborating, though not executed: total energy in general relativity is free **only** when spacetime is asymptotically flat, because that is when there is a boundary to read it on. Remove the asymptotic region and the free read goes with it. The hypothesis predicts exactly that failure.

### 14.4 The sharp exception, which is the section's real find

The hypothesis was expected to *include* the quantization tally of §13.4a — the node count is $\big(\theta(b)-\theta(a)\big)/\pi$, manifestly a difference of endpoint values, which looked like a boundary functional and would have upgraded that result's cost from $O(K)$ to $O(1)$.

It does not, and the reason is exact (`Q4`). A boundary measurement returns the Prüfer angle **modulo $\pi$**. The node count is the integer part, and the integer part is the winding — which is not recoverable from the residue:

| $E$ | $\theta(b)$ continued | nodes $=\lfloor\cdot/\pi\rfloor$ | $\theta(b) \bmod \pi$ |
|---|---|---|---|
| 3 | 6.411610 | 2 | 0.128425 |
| 7 | 9.557705 | 3 | 0.132927 |
| 11 | 15.845908 | 5 | 0.137945 |
| 15 | 22.134839 | 7 | 0.143691 |

The residues are nearly identical while the integers differ. Boundary data cannot separate them. `[clean, verified]`

So the answer to open question 1 is **no**, and the failure is informative:

> **There are two kinds of free read, and conservation buys only one of them.**
>
> - **Flux quantities** are free by the *divergence theorem*: the bulk sum equals boundary data, and an observer outside the boundary pays for its aperture and not for $N$.
> - **Winding numbers** are free by *one-wayness*: no boundary datum gives them, but a monotone passage makes the count a rank rather than a sum, payable at $O(K)$ in one pass (§13.4a).

Two different mechanisms, two different cost tiers, and neither reduces to the other. Symmetry underwrites the first; monotonicity underwrites the second.

This also explains, in retrospect, why §13.10's mod-$2\pi$ extraction residue was never a numerical artefact and why §13.4a needed the one-way lemma to make its tally legal at all. Both are the same fact: **integers require continuity, and continuity is exactly what a boundary does not carry.** `[strong-motivated]`

### 14.5 What it buys, and the scope

Free reads buy the **total and nothing else**. The distribution still costs what it costs, which is §12.1's own law — the observer reads $N/K$, not $N$. A conservation law hands over one number, free, forever; it hands over nothing about how that number is distributed among the parts.

Which is a tidy statement of what a bounded observer's position actually is: it lives in a world that has already summed everything summable and is displaying the results on its surfaces, and its own work begins only where the surfaces stop being informative.

---

## 15. Open questions 2 and 6, settled

*(Executed: `curvature_q.py`, R1–R6.)*

### 15.1 Curvature is itself a flux quantity

Before answering either question, one fact that §14 should have anticipated. For a conformal metric $g = e^{2\varphi}(dx^2+dy^2)$ the Gaussian curvature is $K = -e^{-2\varphi}\Delta\varphi$, so

$$\int_D K\,dA \;=\; -\int_D \Delta\varphi \,dx\,dy \;=\; -\oint_{\partial D} \partial_n\varphi\,ds .$$

Verified to $10^{-11}$ at five radii (`R1`). **Curvature joins the flux family: its *total* over a region is a boundary read, its pointwise value is not.** `[clean, verified]`

That is the hinge for what follows, because it says what a free centre can possibly be sensitive to.

### 15.2 Question 2: the biconditional fails, and the correct statement is sharper

Take $\varphi(r) = e^{-r^2} - c\,e^{-r^2/4}$ with $c = 4e^{-3/4}$, chosen so that $\varphi'(1) = 0$. Then (`R2`):

- $K$ changes sign at $r = 0.6485$ and $r = 2.2036$; sampled, $K(0.2) = +11.34$, $K(0.6) = +1.68$, $K(1.0) = -10.03$, $K(1.6) = -5.29$;
- the total curvature enclosed by the circle $r=1$ is $-1.6\times10^{-11}$ — **zero**;
- the parallel-transport holonomy around that circle is $-9.6\times10^{-18}$.

So there is a region that is **nowhere flat** and whose enclosed curvature vanishes, around which transport is trivial. A centre defined on that configuration is free, and the space is not flat. `[clean, verified]`

> **Answer to question 2.** *Free centre $\iff$ flat* is **exact for fixed-sign curvature** — hence for constant curvature, hence for both branches of the corpus's fork — and **false in general**. What freeness detects is the **enclosed total** $\int_D K\,dA$, not the pointwise value, because holonomy sees the total (Gauss–Bonnet) and nothing finer.

This is a real restriction on §7's central claim and it should be stated there rather than buried. The claim survives everywhere the corpus actually uses it, and it survives *because* the corpus's spaces are constant-curvature — which is a dependency the fork was not previously known to carry.

It also sharpens the flatness test. "Check whether centres compose" does not test flatness. It tests **whether the curvature enclosed by your configuration cancels** — which is a weaker and more interesting thing to be able to measure, since it is exactly what a bounded observer confined to one region *can* know.

### 15.3 Question 6: no third kind, and adiabatic invariants are class 1

The obvious candidate for a third species of free read was the adiabatic invariant. It is not one: $J = \oint p\,dq$ is a loop integral, hence by Stokes the enclosed phase-space area — a bulk quantity read on its boundary, which is mechanism 1 exactly.

Verified (`R6`) by sweeping $\omega: 1 \to 3$ over increasing times: $J$ drifts by $4.5\times10^{-2}$, $3.2\times10^{-3}$, $3.4\times10^{-4}$ as the sweep lengthens by decades — conserved to the adiabatic order, and read off the orbit rather than the interior. `[clean, verified]`

So the split stands as stated, with the mechanisms now named by their theorems:

| mechanism | theorem | what the interior did | examples |
|---|---|---|---|
| **flux** | divergence / Stokes | summed itself onto its boundary | charge, momentum, energy, action, total curvature |
| **winding** | monotone passage | ordered itself so a count is a rank | node counts, quantum numbers, Maslov index |

`[open, and honestly so]` — absence of a third kind is not proof of its absence. What would settle it is a characterisation theorem: *the free reads of a bounded observer are exactly the boundary functionals and the monotone ranks*. That is a well-posed question and nobody has asked it.

### 15.4 What §14 and §15 together say to §7

Three amendments the cost ladder should absorb:

1. Its cheap rungs are **not** a stipulation about the observer. They are a fact about the world: conservation laws and monotone structures are the interior having already done the summing, and the observer's cost is set by its relation to a boundary.
2. The tier is a property of **the observer's aperture**, not of the quantity: $O(1)$ distant, $O(M)$ enclosing with $M \perp N$, $O(N)$ only when it must visit.
3. And the free-centre argument carries a **constant-curvature dependency** that was invisible until §15.2. It holds on both branches of the fork, which is why nothing downstream breaks — but it holds *because* of the fork, not independently of it.

---

## 16. Is gravity the three-dimensional pulse?

*(A conjecture pushed until it either held or broke. It half-holds, the half that holds is sharper than the conjecture was, and the half that breaks is named. Executed: `bertrand.py`, `bertrand2.py`, `bohlin.py`.)*

### 16.1 The conjecture, and its strongest form

The pulse (§1.09) has two defining properties: it goes **out from the centre**, and it **comes back**. Give it three dimensions and both cash out into physics.

**Out from the centre.** A conserved quantity spread radially over a sphere has density $\propto 1/r^2$ — and by §14 that is not a force law but a *boundary* fact. In $d$ dimensions the exponent is $d-1$. So:

> **The inverse-square exponent is the dimension of the boundary the free read lives on.** `[clean]`

**And back.** Closure is not decoration; it **selects the law**. Among central forces $F = -r^p$, all bound orbits close for exactly two exponents (Bertrand 1873). Measured apsidal angles as the orbit is deformed (`bertrand.py`):

| $p$ | law | $v{=}0.97$ | $v{=}0.85$ | $v{=}0.65$ | spread |
|---|---|---|---|---|---|
| $-2$ | inverse-square | 3.141393 | 3.141011 | 3.139972 | $1.4\times10^{-3}$ |
| $+1$ | harmonic | 1.570787 | 1.570733 | 1.570618 | $1.7\times10^{-4}$ |
| $-1$ | $1/r$ | 2.221253 | 2.217061 | 2.194785 | $2.6\times10^{-2}$ |
| $-2.5$ | $r^{-2.5}$ | 4.446992 | 4.521763 | 4.768276 | $3.2\times10^{-1}$ |
| $0$ | constant | 1.813736 | 1.812148 | 1.802655 | $1.1\times10^{-2}$ |

Only $-2$ and $+1$ hold; everything else opens into a rosette. `[clean, verified]`

### 16.2 The cut is at covering degree two — and that is a theorem, not a coincidence

At linear order the apsidal angle is $\Phi = \pi/\sqrt{3+p}$, so closure after $n$ radial oscillations per half-turn needs

$$p \;=\; n^2 - 3 ,$$

an **infinite** family indexed by an integer $n$ — which is a winding ratio: how many times the read cycles per cycle of the hold. Bertrand's nonlinear condition then cuts it. Where? (`bertrand2.py`, S1):

| $n$ | $p = n^2-3$ | $\pi/n$ | near-circular | eccentric | drift |
|---|---|---|---|---|---|
| 1 | $-2$ | 3.141593 | 3.141588 | 3.141035 | $5.5\times10^{-4}$ |
| 2 | $+1$ | 1.570796 | 1.570798 | 1.570723 | $7.5\times10^{-5}$ |
| 3 | $+6$ | 1.047198 | 1.047149 | 1.059554 | $1.2\times10^{-2}$ |
| 4 | $+13$ | 0.785398 | 0.785464 | 0.799326 | $1.4\times10^{-2}$ |

$n = 1, 2$ hold to integrator residual; $n \ge 3$ drift by two orders more. **Bertrand's cut is exactly "covering degree at most two."** `[clean, verified]`

That could still be a coincidence of small integers — lots of things cut at two. It is not, and the reason is classical. **The harmonic orbit literally traces the double cover** (S2): its ellipse is *centred* on the origin, so after $\pi$ of angle the position is negated while the line through it is unchanged —

$$x(\theta+\pi) = -x(\theta), \qquad \text{ratio measured: } 1.00000,\ 1.00001,$$

which is $S^1 \to \mathbb{RP}^1$ drawn by a planet. The Kepler ellipse has the origin at a **focus**, so read and hold return together: covering degree one. Same test on Kepler gives ratio $0.36$ — no antipodal relation. `[clean, verified]`

And the mechanism is Bohlin's (1911) / Levi-Civita's: **the two Bertrand potentials are related by $w = z^2$.** Integrating the harmonic oscillator in the complex plane and squaring (`bohlin.py`):

- $1/|w|$ fits $A + B\cos\theta + C\sin\theta$ — a conic with a **focus at the origin** — to a maximum relative residual of $3.9\times10^{-14}$, eccentricity $0.4706$;
- the same fit applied to $z$ itself fails by $2.4\times10^{-1}$, six thousand billion times worse;
- and $z$, $-z$ map to the same $w$ to $1.7\times10^{-10}$: one Kepler point, two harmonic points.

> **The relation between the only two force laws whose orbits all close is exactly the covering map $z \mapsto z^2$** — the same squaring as Born's $|\psi|^2$, Maslov's $\det^2$, and the rotation $R(q)$. Bertrand's two survivors are the two sheets of one square. `[clean, verified; Bohlin/Levi-Civita is classical and must be cited, not claimed]`

### 16.3 What actually distinguishes gravity — the objection and its repair

The conjecture as stated under-determines its target. $1/r^2$ is the flux law for **any** conserved radial quantity; electrostatics is $1/r^2$ too. Radial reach plus closure gets you the Kepler problem, not gravity.

The repair is the balance's own. What separates gravity from electrostatics is that **its source is the centre itself**. Electric charge sits somewhere; mass *defines* where. Newton's shell theorem says the gravitational field knows the centre of mass and nothing else about the interior. So:

> **Gravity is the field whose source is the same object that defines the origin.**

That is the equivalence principle in this paper's language, and it is §4's "the centre is free" turned into physics. Electrostatics has a centre of charge and a centre of mass and they differ; gravity has one centre — and §8's tidal gap is what happens when even that one splits. `[strong-motivated]`

### 16.4 Where it breaks, stated so it is not forgotten

**The pulse is an act; gravity is a field.** Identifying them conflates the observer's traversal with the medium traversed. That is this programme's characteristic failure mode and §13.4d exists to guard against it. Nothing above closes that gap; the results are about orbits and fields, and the pulse's status as an *observation* plays no role in any of them. `[open, and the most serious of the three]`

**The two closures are not obviously the same closure.** The pulse closes in the corpus's sense — the *read* returns to its address, the seam welded, $\mathbb{RP}^1$. A Kepler orbit closes in *space*. §16.2 shows the harmonic case where these coincide exactly, which is real evidence; it does not show they must. `[open, but narrowed]`

**And there is a live tension inside the corpus.** §13.5 routes gravity through the scale connection $A_\mu = \partial_\mu\ln\lambda$ and its non-integrability, not through a radial reach. If gravity is the three-dimensional pulse, those are one story and nobody has written it. `[owed]`

### 16.5 Verdict

The conjecture is **not established and not refuted, and the pushing was worth it**, which is the outcome the programme is built for. What came back:

- **True and sharper than conjectured:** the inverse-square exponent is a boundary dimension, not a force law (§16.1).
- **True and unexpected:** closure selects the law, the selection is at covering degree two, and the two survivors are the two sheets of one square — Bohlin's map is the corpus's own square, appearing in celestial mechanics with no prompting (§16.2).
- **False as stated, repairable:** radial reach gives inverse-square, not gravity; what gives gravity is that its source is the centre (§16.3).
- **Untouched:** the act/field gap, which is the one that matters and the one this section does nothing about (§16.4).

The honest summary is that **gravity is not the three-dimensional pulse, but the Kepler problem and the pulse share a square** — and the square is the same one the rest of the corpus keeps finding.

---

## 17. The ball on a string: the paper's intuition section

*(Pure intuition, and the paper's most transmissible material. Nothing here is new physics; everything here is a thing a reader can hold. Executed: `string_in_space.py`, U1–U4.)*

Stand up. Hold a string with a ball on the end. Turn once on the spot and let the ball swing out.

### 17.1 The string is boundedness, not the horizon

Taut is the **corner**, $r = 1$ — not the horizon. §1.09 says full extension is a state "the body knows with no graduation at all," and a string makes that literal: you feel taut, with no ruler, and you cannot be mistaken about it. The horizon is the other end, $r = \infty$, which the string neither reaches nor approaches.

So the string is not a metaphor for a limit that recedes. **It is boundedness itself, instantiated** — the physical reason the read lives in a box, held in your hand.

### 17.2 You do not spin about yourself

You and the ball rotate about your **common** centre of mass, and you wobble around it (`U1`):

| you | ball | tether | your orbit radius |
|---|---|---|---|
| 70 kg | 1 kg | 1 m | 0.014 m |
| 75 kg | 5 kg | 2 m | 0.133 m |
| 80 kg | 2 kg | 3 m | 0.073 m |

Thirteen centimetres is not subtle. Swing a heavy weight on a long rope and it drags you round a small circle you did not choose and cannot move.

That is §4 delivered through the hips: **the centre is the system's own address, not one you assign.** It is a better demonstration than the balance, because a balance settles quietly and this one pushes back.

### 17.3 In space, the pretence is stripped

Now do it floating, far from anything. Ask what changes and the answer is: the thing that was letting you lie.

On Earth you can *pretend* the centre is you, because the ground absorbs the reaction. Remove the ground and total angular momentum must stay at zero, so internal forces cannot manufacture an orbit — they can only **move angular momentum between the ball's orbit and your own body**. Executed for an 80 kg astronaut ($I \approx 7.2\ \mathrm{kg\,m^2}$), a 2 kg ball and a 3 m tether (`U2`): the centre of mass sits 7.3 cm from you, the orbital angular momentum is $17.6\ \mathrm{kg\,m^2}$ per unit $\omega$, and

> **you must counter-spin at 2.44 times the orbital rate.** One lap of the ball costs you about two and a half turns backwards.

So in space you and the ball become a **dumbbell about the common centre of mass**, phase-locked at 180°, with your own body spinning the other way to keep the books at zero. There is no standing still, and there never was — Earth was doing it for you. `[clean, verified]`

### 17.4 The 360° is a double cover, walked

Turn once and watch the string, not the ball. After a **half** turn the string lies along the same line it started on — same axis, ball on the opposite side. The **line** has come home; the **ball** has not. Only the full turn brings the ball back.

That is $S^1 \to \mathbb{RP}^1$, performed with a piece of string: the read closes at $\pi$, the hold closes at $2\pi$, and the factor of two between them is the covering degree carrying the zero-point energy (§13.4b) and spin-½ (§13.4c). **You can hold the deck transformation in your hand.**

### 17.5 The demonstration: a rubber band against a planet

A ball on a *taut* string is a circular orbit, and circles close under any central force whatsoever — so a taut string demonstrates nothing about the law. To see the covering degree the radius has to breathe.

Swing the ball on a **rubber band** instead. Elastic gives a Hooke restoring force, the orbit is harmonic, and §16.2's result says the ellipse is **centred** on you: the ball goes out and back *twice* per lap.

A planet's ellipse has the sun at a **focus**: once per lap.

> **A ball on a rubber band traces the double cover. A planet does not.** Same closure, different covering degree — and by Bertrand those are the only two that survive at every eccentricity.

You can hold one and look at the other, and the difference between them is the square this corpus keeps finding. `[clean; the orbit result is §16.2's, verified there]`

*Practical caveat: a real rubber band only pulls, so it must be pre-tensioned or it goes slack at the inner turning point and the orbit stops being an ellipse. A demonstration that goes slack demonstrates nothing.*

### 17.6 What the string is and is not a metaphor for

The string is a tempting stand-in for gravity and it is worth being exact about where it holds.

**What it captures.** Centrality — the force is along the line to the centre. Closure — the motion returns. And the centre's freeness, better than anything else in this paper.

**What it does not.** A string is a **constraint**; gravity is a **law**. The string supplies whatever tension the motion requires and nothing at all when slack; gravity supplies $1/r^2$ always. So a taut string gives you the *geometry* of orbit without the *dynamics*, which is exactly why it cannot produce apsides, and therefore cannot distinguish covering degree 1 from 2. **The string gives you the centre; the law gives you the covering degree.**

**And the disanalogy that matters most** (`U4`): cut the string and the ball departs on a straight tangent, you keep whatever spin you had, and the pair's centre of mass carries on exactly as before, forever. **A string can be cut. Gravity cannot.** An unshieldable constraint is not a force — it is a geometry, which is the whole content of the equivalence principle and the reason §13.5 routes gravity through a connection rather than through a pull.

### 17.7 The tension is a free read

Reel the ball in with angular momentum fixed and the tension climbs as $T = L^2/mr^3$ (`U3`): 5.4 N at 3 m, 18 N at 2 m, 147 N at 1 m, 1174 N at half a metre. Your hand is reading a conserved quantity *as a force* — the skater's arms with the floor removed.

`[open]` — is this §14's freeness or a different one? $L$ is a flux-class conserved quantity, and the tension is a pointwise force rather than a boundary integral, so the hand may be reading the free quantity by a route that is not the free route. Worth settling, because if the tension read *is* a boundary read, then the body has a second native channel for a conserved total, alongside §11's centre of pressure.

### 17.8 Why this section exists

Everything above is standard mechanics. Not one line of it is new, and a physicist will find nothing in it to argue with — which is the point. The corpus's persistent weakness is transmission, and this is the one place where a reader arrives already owning the intuition and needs only to be told what it is called. **The wobble is the free centre. The half-turn is the covering degree. The rubber band is the square.** Three things you can do with your hands before anyone shows you an equation.

---

## 18. The menu and the walk

*(Framing, not results. No new claims; one repair. Executed: `menu.py`, V1–V3.)*

### 18.1 π is the menu

The orientation set is $\mathbb{RP}^1$ and its measure is $\pi$ — verified in the slope chart, $\int ds/(1+s^2) = 3.141592654$ (`V1`). An observation is the selection of **one point** of it.

So: **π is the menu, and an observation is one item off it.**

Two things that image gets right and one it gets wrong.

**Right: selection, not construction.** The observer does not build the orientation; it receives one. And **right: the menu is fixed and finite in measure** — there is exactly $\pi\rho_0$ of it, no more. *(This first read "exactly π of it, at every scale, for every observer." **Corrected at §35.7**: the total is $\pi\rho_0$ and equals $\pi$ only under the home normalisation $\rho_0 = 1$ — a $K = 200{,}000$ observer's menu measures $200{,}000$, not $\pi$. §25.8, §28.3. And for §1's non-negative atom it is $(\pi/2)\rho_0$, §31.2.)*

**Wrong, if read carelessly: π is the menu's *length*, not its number of entries.** There are not 3.14 options. π is the measure of a continuum; the number of *distinguishable* entries is $K$, the hold. Which makes §7.6's capacity bound transparent:

$$K_{\max} = \pi\rho_0 \;=\; \underbrace{\pi}_{\text{menu length}} \times \underbrace{\rho_0}_{\text{how finely it is printed}} .$$

The extraction survey called that "a tautology dressed as a bound." Under the menu reading it is not a bound at all and does not need defending — it is length times print resolution, and stating it that way costs nothing and settles the objection. `[repair]`

### 18.2 You are served, not asked

A menu implies ordering, and the corpus's whole ontological inversion is that you do not order. A physical interaction determines the pair; the observer receives it. **It is a menu you are served from.** The observer supplies the algebra; the world supplies the item.

Keep the image and drop the choosing, or the metaphor smuggles in exactly the thing the framework denies.

### 18.3 2π is the walk

Selecting one orientation costs π-worth of set. *Closing a shape* is a different act and costs a full turn. So:

> **π is the menu. 2π is the walk.**

And the factor of two between them is the covering degree — the same one carrying the zero-point energy and spin-½. Verified directly (`V2`): walking the hold once from $0$ to $2\pi$, the read wraps **twice**.

Which is §17's string, in menu language: **turn once with the ball, and the line through your hand has been served the whole menu twice.** At the half turn you are back on the same entry with the ball on the other side. One walk, two servings.

That is the cleanest statement of hold-versus-read the paper has. The **read** picks from the menu. The **hold** walks the circle. The double cover is the relation between *choosing* and *touring*.

### 18.4 π/2 and 2/π are the exchange rate

The menu can be quoted in two currencies — as arc (the angle chart) or as ratio (the slope chart) — and the rate between them is fixed.

The corpus's own gloss is "the hold 2 measured against its un-evaluated total," and the menu image makes that arithmetic literal: **the hold is 2 registers, the total is π of menu, and the rate is their quotient.** *(An early reading, **superseded**: §25.3 makes this $2$ the $n=2$ value of $\Gamma(n/2)/(\sqrt\pi\,\Gamma(\tfrac{n+1}2))$ — at $n=3$ the constant is $1/2$, with no registers in sight — and §33 shows the $2$ in $s_{\max} = 2\rho_0$ is a third, different two. §33.5: every factor of two here must carry its provenance.)*

$$\frac{2}{\pi} = 0.636619772, \qquad \frac{\pi}{2} = 1.570796327 .$$

Two facts pin it (`V3`). First, the atom is non-negative in both registers, so it occupies **one quadrant** of the walk — $\pi/2$, the corpus's "folded ray." Second, $2/\pi$ is exactly the normalisation that converts an arc into a fraction of that quadrant:

| $S$ | $\arctan S$ | $(2/\pi)\arctan S$ |
|---|---|---|
| $10^0$ | 0.785398 | 0.500000000 |
| $10^1$ | 1.471128 | 0.936548965 |
| $10^3$ | 1.569796 | 0.999363380 |
| $10^6$ | 1.570795 | 0.999999363 |
| $10^{12}$ | 1.570796 | 1.000000000 |

The quarter-menu, read as a whole. So:

> **π is the menu, 2π is the walk, and π/2 ↔ 2/π is the exchange rate between reading the menu as an arc and reading it as a portion.**

*(This first read: "**Every** appearance of either constant anywhere in the corpus is this one crossing." **Falsified at §35.7.** $2/\pi$ has at least three distinct identities — the arc/chord crossing here, the mean projection at ambient $n=2$ with siblings $1/2$ and $4/(3\pi)$ (§25.3), and the capacity-to-reach rate (§27.5) — and §28.4 shows $\pi$ cancels out of the operational form entirely.)*

**The fare notation contract — added under audit, and load-bearing.** Written with a slash, $2/\pi$ names an **executed quotient**, which is the one form no bounded observer has: it presupposes both knowing $\pi$ and performing a division, and §3.7 forbids the second while §9.5 denies the first. The corpus has been writing the only form that does not exist. Four things are being conflated and they should be kept apart:

| form | notation | who has it |
|---|---|---|
| **the hold** | $(2,\ \pi)$ | the observer's two registers — two quantities, no operation performed |
| **the read** | $(2 : \pi)$ | what the act returns: the class, §9.2's colon |
| **the acquisition** | a bit-string of depth $\log_2 N$ | the running system, by bisection (§10.16) |
| **the evaluated quotient** | $2/\pi = 0.63661977\ldots$ | the outside describer, and nobody else |

Two rules follow, and both are cheap.

*First — the slash is a name, not an instruction.* The corpus will keep writing $2/\pi$ and $\pi/2$ because they are the recognisable names for these objects, and every such appearance is to be read as **the class $(2:\pi)$, held as the pair $(2,\pi)$, acquired to $\log_2 N$ bits, and never evaluated**. Where the distinction does work, the form is written out.

*Second — never require a division of the reader either.* Any equation containing $2/\pi$ or $\pi/2$ should give the value in the surrounding prose — $2/\pi = 0.63661977$, $\pi/2 = 1.57079633$ — so that no step of any derivation asks anyone, observer or reader, to execute a quotient. A framework whose premise is *hold the pair, never divide* should not print instructions to divide on every other page.

 The corpus already says a formula containing $\pi/2$ or $2/\pi$ is a chart crossing by definition; the menu says *what is being crossed between* — a length of menu and a fraction of it.

### 18.5 The menu has no first entry

One caution, and it is the corpus's own (§9.5's coda): homogeneity is unoccupiable. The menu has no first item and no ordering that is not imposed, which means **nobody reads it undistorted.** Your own standpoint warps it — dense near where you are aiming, thinning to your horizon — and that warp is the fisheye, whose density is the Cauchy.

So the menu is uniform in the border's measure and crooked in every actual view. There is no seat with a flat copy.

### 18.6 What this section buys

By the paper's own standard: **no new numbers, one route, and a repair that is no longer this section's.** §27.4 *derives* $K = \pi\rho_0$ from the dial's circumference — "it is not an assertion and does not need repairing" — and §31.2 corrects it to $(\pi/2)\rho_0$ for the non-negative atom. This section also writes $K_{\max}$ (a bound) where §27.4 and §28.3 write $K$ (an identity). **And its self-grade of "claiming nothing" was false**: §18.1 asserted a universal quantifier over observers. Retained as motivation; see §35.7. The route is that π-versus-2π — the corpus's oldest and least intuitive split — now has an image instead of an argument, and the image is one a reader can perform in a corridor with a ball on a string.

Graded as exposition, deliberately, and claiming nothing. `[framing]`

---

## 19. Two countries, two exchange rates: what reciprocity buys

*(Prompted by a question — what happens if the inside's rate and the outside's rate are exact inverses of each other? The answer is sharp, it lands on something §8.5 already proved, and it explains why the corpus has both a reciprocity theorem and a non-trivial holonomy without contradiction. Executed: `arbitrage.py`, W1–W3.)*

### 19.1 The setup

Call the inside and the outside two countries. Each quotes a rate for converting its currency into the other's: $r_{AB}$ and $r_{BA}$. Ask what follows from

$$r_{AB}\cdot r_{BA} = 1 .$$

### 19.2 It buys antisymmetry, not flatness

The two-leg round trip $A \to B \to A$ returns exactly what you set out with. No arbitrage is possible on a pair. Verified trivially and reported anyway because the contrast is the point (`W1`): with bilateral inverses imposed, the two-leg trip returns $1.000000000000$ every time — and the **three-leg** trip $A \to B \to C \to A$ returns $0.387$, $1.947$, $0.790$, $1.310$ on four random markets. Whatever it likes.

In log-rates $\varphi_{AB} = \ln r_{AB}$, the condition is

$$\varphi_{AB} = -\varphi_{BA},$$

which is **antisymmetry** — it makes the rate a genuine 1-form. Flatness would be $\varphi_{AB} + \varphi_{BC} + \varphi_{CA} = 0$, and nothing above supplies it.

> **Inverse exchange rates buy antisymmetry, not flatness. They kill two-leg arbitrage identically and say nothing whatever about three-leg.** The first is bookkeeping; the second is curvature.

`[clean, verified]`

### 19.3 Why the corpus can have both a reciprocity theorem and a holonomy

This resolves what looks like a tension. §8.5 proves *products-equal-one*: for two atoms in mutual observation, $k_{AB}\cdot k_{BA} = 1$ exactly, over $\mathbb{Q}$ — "because the read is odd and the stretch is even," which is to say **by construction**. Meanwhile §13.6 proves that boosts do not commute and their commutator is a rotation.

Both are true and they are about different loops. §8.5's reciprocity is the **two-leg** statement — free, structural, and carrying no information about curvature. §13.6's Wigner rotation is the **three-leg** residue, which reciprocity never touched.

Executed in the velocity market (`W2`): a boost by rapidity $a$ composed with a boost by $-a$ returns the identity to $10^{-16}$ — bilateral rates are exact inverses, no two-leg arbitrage. But boost along $x$ by $a = 0.8$, along $y$ by $b = 0.5$, then close the triangle, and the residue is a **pure rotation** of $0.185578740$ rad against the Wigner angle $\arctan\!\big(\sinh a \sinh b/(\cosh a + \cosh b)\big) = 0.185578740$, agreeing to $5.6\times10^{-17}$.

> **Thomas precession is triangular arbitrage in the velocity market.**

`[clean, verified]`

This is also the corpus's $M{=}1$ versus $M{\ge}2$ split, seen from the market side: one retained register gives you bilateral trades and no profit; two registers let you close a triangle, and a triangle pays.

### 19.4 The profit per loop is the curvature

And the payout is not arbitrary. Velocity space is hyperbolic with $K = -1$, and by Gauss–Bonnet the residue of a closed loop is the enclosed area (`W3`):

| $a$ | $b$ | three-leg residue | triangle area |
|---|---|---|---|
| 0.20 | 0.30 | 0.029675967 | 0.029675967 |
| 0.60 | 0.40 | 0.114869365 | 0.114869365 |
| 1.00 | 1.20 | 0.486529639 | 0.486529639 |

Identical to nine figures. **The arbitrage a loop returns is the area it encloses, times the curvature.** Zero curvature, zero profit, closed books.

Which is §15 restated in the market's language: *curvature is the price of a centre* becomes *curvature is the profit in a loop*, and the flatness test — check whether centres compose — becomes **check whether the books close on a triangle**.

### 19.5 Where this fits, and what it is not

**Not new.** Currency exchange as a gauge theory, with arbitrage as its curvature, is established (Ilinski, 1997 onward). The 1-form/connection reading, the no-arbitrage-equals-flat statement, and the triangle-as-plaquette picture are all standard there and must be cited, not claimed.

**What is being added** is only the identification: **the corpus's own two-atom reciprocity theorem is the two-leg case of exactly this structure**, which explains why it is free — antisymmetry always is — and why it cannot be strengthened into flatness, which the corpus has never claimed and now has a reason not to want.

**And one honest limit.** The metaphor is exact for the *composition* of reads, because both are group-valued and both compose by multiplication of rates. It says nothing about what a currency *is*, and there is no analogue here of value, scarcity, or price formation. It is a statement about how conversions chain, and only that.

### 19.6 What it buys

- **Answers the question asked**, exactly: reciprocity is a two-leg identity, and everything interesting lives at three legs.
- **Dissolves an apparent tension** between §8.5 and §13.6 — different loops, not competing claims.
- **Earns a slogan that is also a theorem:** *Thomas precession is triangular arbitrage*, verified to $10^{-17}$.
- **Re-expresses §15's flatness test** in a form a non-physicist can apply: do the books close when you go round three?

`[framing plus one dissolved tension; the gauge reading is Ilinski's, the two-leg identification is the corpus's]`

---

## 20. How a bounded observer comes to have 2/π without dividing

*(An objection to the framework's own consistency, raised and answered. The corpus says the observer cannot execute a quotient (§3.7) and that its licensed operations are $\{$corner, $\times2$, $\div2$, $\pm$, swap$\}$ (§10.1) — and then uses $2/\pi$ as a rate throughout. Either that is a contradiction or the rate is reached some other way. It is reached some other way, and the way is the corpus's own. Executed: `finding_pi.py`, X1–X4.)*

### 20.1 The objection, at full strength

$2/\pi$ is written as a quotient. A bounded observer cannot execute quotients. And this is not an academic worry: **a real system that oscillates must somehow have the rate**, or it does not close and does not oscillate. Saying the rate is "determined but unevaluated" (§9.5) answers the bookkeeping and not the physics — something has to actually run.

### 20.2 First answer: it is a held pair, not a division

The shallowest layer dissolves immediately. In this framework $2/\pi$ is not an operation, it is a **read of a held pair** $(2 : \pi)$ — two registers held against a total. Executing $v/h$ is what is forbidden; *holding* $(v,h)$ and reading their standing is the primitive act itself. So the notation misleads: the slash is the corpus's own format, not an instruction.

And $\pi$ is not held as a numeral, which no finite register could do. It is held as a **state** — full extension, the closed arc, §1.09's reach that cannot be exceeded and is known "with no graduation at all." The observer has the total the way an arm has its span: by being it, not by measuring it. *(**Scoped at §35.7.** §28.5 shows the observer never needs $\pi$ at all — every operational quantity is $\pi$-free and $\pi$ appears only in totals, which are the describer's. This section's answer is correct **for $2/\pi$**, which the observer does acquire; for $\pi$ itself the answer is that the question does not arise.)*

That answers the format worry. It does not yet answer how anything converges.

### 20.3 Second answer: the observer halves, and halving gets there

Vieta's product converges to $2/\pi$ using only addition, doubling, halving, and square root — **no division at any step** (`X1`):

| factors | partial product | error vs $2/\pi$ |
|---|---|---|
| 2 | 0.653281482438188 | $1.7\times10^{-2}$ |
| 5 | 0.636487226774558 | $1.3\times10^{-4}$ |
| 12 | 0.636619772216981 | $1.9\times10^{-10}$ |
| 25 | 0.636619772367581 | $1.1\times10^{-16}$ |

And the factors are not an analytic trick. Each one is **exactly** $\cos(\pi/2^n)$ — verified to zero difference at every $n$ tested (`X2`). So the nested radicals are literally *the corner, halved, and halved again*: the observer doing the one thing §10.1 licenses natively, repeatedly.

### 20.4 The square root is an artifact of the chart

The obvious objection to §20.3 is that $\sqrt{\ }$ is not in the licensed set either. It does not need to be.

**Halving in the angle chart is a square root in the slope chart.** With $t = \tan\theta$,

$$\tan(\theta/2) \;=\; \frac{\sqrt{1+t^2}-1}{t},$$

verified at four angles to twelve figures (`X3`). The observer bisects an arc; *we* see a radical, because we insisted on writing its act in the slope coordinate. The root is a chart artifact, exactly as $\pi/2$ and $2/\pi$ are chart crossings (§18.4).

So the licensed set does not need extending. Bisection was always in it, and bisection is the whole method. `[clean, verified]`

### 20.5 The cost is inside the ladder

Two digits per three halvings (`X4`): 3.6 digits at 5 halvings, 6.6 at 10, 12.6 at 20. That is $O(\log(1/\varepsilon))$ — the corpus's own middle rung, requiring no global pass, no accumulation, and no quotient.

So the answer to "life must find this value somehow" is: **it does, by bisection, at logarithmic cost, using the one operation the framework already says is native.**

### 20.6 The deepest answer: π is the size of what cannot be distinguished

There is a further layer, and it is the one that actually resolves the physics.

An oscillator does not need to *acquire* $\pi$. The read wraps at $\pi$ because a ratio cannot see orientation (§9.5) — the wrap is not a value the system obtains but a **capacity it lacks**. Turn by $\pi$ and the read is home not because something measured $\pi$ but because nothing could tell the difference.

> **π is not a number the observer finds. It is the size of what the observer cannot distinguish. Ignorance has a measure, and that measure is π.** *(A describer's sentence by §28.5's own audit — it states a total. Kept for what it says about $2/\pi$'s acquisition; see §35.7.)*

Which is why closure is free and why oscillation does not need a rate to be supplied. The system does not compute the lap; **it fails to distinguish the ends of it**, and that failure *is* the lap. §18's image says the same thing: the menu is π long because π is how much orientation a ratio-reader is blind to.

The corpus's own line — that the circle was walked before it was ever drawn — is this, and §20.3's bisection is only how a reader *refines* an address on a loop it was already standing on. `[strong-motivated]`

### 20.7 What it buys

- **Removes a genuine internal contradiction** — the corpus used $2/\pi$ while forbidding division, and never said how. Now it says how.
- **Earns numbers**: Vieta to $10^{-16}$ with no division; the factors identical to $\cos(\pi/2^n)$; the half-angle identity to twelve figures; the cost at $O(\log(1/\varepsilon))$.
- **Extends nothing**: the licensed operation set is untouched, because the square root was never an operation — it was a chart's way of writing a halving.
- And it supplies the answer to the version of the question that actually matters: a system that oscillates has not solved for $\pi$; **it has failed to tell one end of a turn from the other**, and that is cheaper than solving.

`[objection answered; one contradiction removed]`

---

## 21. Alignment: what undergoing a cycle costs, and what anticipating one costs

*(§20 answered how the rate is reachable and then over-claimed by implication: it suggested nothing inside ever needs the value. That is true of *existing* and false of *aligning*, and the distinction is the section. Executed: `alignment.py`, Y1–Y3.)*

### 21.1 The objection §20 did not meet

§20.6 concluded that π is not a value the observer finds but the size of what it cannot distinguish — so closure is free and an oscillator needs no rate supplied. That is right as far as it goes.

But it does not go far enough. **If a system's steps are not correctly scaled against the total, it does not align with the menu** — it drifts, aliases, or fails to close where it must. Something has to fix the relation between the step and the whole, and "the observer cannot distinguish the ends" does not fix it. Alignment is an operational requirement, not a bookkeeping one.

### 21.2 Mere cycling is aligned for free

The first half of the answer is that a system which only *cycles* genuinely needs nothing. Step by an irrational fraction of the menu and even coverage is automatic (`Y1`):

| steps | max gap | min gap | distinct gaps |
|---|---|---|---|
| 10 | 0.171573 | 0.071068 | 3 |
| 100 | 0.014214 | 0.005887 | 3 |
| 1000 | 0.001421 | 0.000589 | 3 |
| 10000 | 0.000149 | 0.000062 | **3** |

**At most three distinct gaps at every count** — the three-gap theorem, which the corpus already carries at §9.5. Coverage is a fact about stepping, not a grid that has to be laid, and the stepper never learns the total. `[clean, verified]`

So for *undergoing*, §20 stands: alignment is free and π is the measure of an indistinguishability.

### 21.3 Anticipation is where the rate bites

The second half is where the objection lands. **A system that merely returns needs nothing. A system that must act *now* on the basis of where it will *be* needs the rate** — and anticipation is precisely what living things do.

So the question sharpens: can a bounded observer acquire the rate with only the operations it is licensed? It can, and it needs exactly two: a **sign test at the seam** and a **halving**.

Set the problem honestly — the system must choose a step $s$ such that $n$ steps close the loop, it does **not** know the total, and the only measurement available is one bit at the seam: *did I pass the mark?* (`Y2`):

| $n$ | target $\pi/n$ | found by sign + halve | error |
|---|---|---|---|
| 2 | 1.570796326795 | 1.570796326795 | 0 |
| 3 | 1.047197551197 | 1.047197551197 | $2.2\times10^{-16}$ |
| 5 | 0.628318530718 | 0.628318530718 | 0 |
| 8 | 0.392699081699 | 0.392699081699 | 0 |

It never divided, never evaluated π, and never saw the total. It asked one bit and halved, and it is now aligned to the menu. `[clean, verified]`

### 21.4 The biological name for this is entrainment

This is not a thought experiment about what a system could in principle do. It is what timing systems actually do.

Give a system an unknown external period and let it correct using only the sign of accumulated drift — one bit per trial — and halve (`Y3`):

| trials | period estimate | error |
|---|---|---|
| 1 | 0.925000000000000 | $7.5\times10^{-2}$ |
| 6 | 1.007031250000000 | $7.0\times10^{-3}$ |
| 11 | 1.000366210937500 | $3.7\times10^{-4}$ |
| 21 | 1.000000214576721 | $2.1\times10^{-7}$ |
| 41 | 1.000000000000341 | $3.4\times10^{-13}$ |

Exponential lock, no division, and **the system never learns the true period as a number** — only that its own step now closes the loop.

> **A circadian clock does not measure twenty-four hours. It entrains.**

Entrainment is §20.3's bisection run by biology; the continuous version is the Adler–Kuramoto lock $\dot e = \Delta\omega - K\sin e$, and the engineering version is a phase-locked loop. All three are the same mechanism: a sign, a correction, and a halving. `[clean, verified]`

### 21.5 The resolution

Both halves are needed and they divide cleanly:

| | needs the rate? | mechanism | cost |
|---|---|---|---|
| **undergoing** a cycle | no | irrational stepping, three-gap coverage | free |
| **anticipating** a cycle | yes | sign at the seam, then halve | $O(\log 1/\varepsilon)$ |

So the objection is answered without retracting §20. **Existence does not need the value; anticipation does; and anticipation pays for it in bits, not in divisions.**

And the biological reading is the sharp one. Life does not calculate $2/\pi$ and it does not need to. **It entrains to it** — one bit at a time, at logarithmic cost, using a sign test it already has for other reasons. A system that failed to do this would not be misaligned with an abstraction; it would drift against its own environment and be corrected or replaced. Alignment with the menu is not a fact a creature knows. It is a thing a creature is kept at.

`[objection met; §20 stands, and is now scoped]`

### 21.6 What sets the tolerance: precision is a lifetime

§21.3 prices alignment at $O(\log 1/\varepsilon)$ without saying what fixes $\varepsilon$. The answer is the observer's own run length, and the reason is that **a truncated rate is a rational, not an approximate irrational** — it visits $q/\gcd(p,q)$ addresses and then nothing further, ever. Nine digits of $2/\pi$ buys 250 million addresses and then blindness (`lifetime.py`, B1).

So $q > N$, hence **bits $> \log_2 N$**: a system performing $10^9$ acts needs thirty bits of rate, and at $\sim1.05$ bits per halving that is thirty halvings. Not infinite precision — a finite number set by how long the thing lives.

And the error compounds multiplicatively, because conversions chain (§19): $\delta = 10^{-3}$ is $71\%$ wrong after a thousand conversions and $e^{1000}$ wrong after a million. Small rate errors never stay small.

> **Precision is a lifetime. *(The **held** rate is not $2/\pi$ — §28.4 shows the observer never holds it. What it holds is $1/\rho_0$, the atom spacing at home, verified at three scales (§30.2), and $\log_2 N$ bits of *that* is what $N$ acts require. The compounding argument is unaffected; the object was wrong. Corrected at §35.7, and it should be corrected in the corpus at §10.16 too.)*** Hold the rate to $\log_2 N$ bits or go blind at $q$.

Folded into the main corpus at §10.16. `[clean, verified]`

---

## 22. One budget, two names

*(Raised as a question at §10's close — are the register trade and the capacity trade the same conservation? — answered wrongly first, then correctly. Both attempts are recorded because the error is instructive. Executed: `two_budgets.py`, `two_budgets2.py`.)*

### 22.1 The wrong answer, and why it was wrong

The first test compared the register norm $\sum v_i^2 + h^2 = 1$ against $K$ read as a **count of atoms**, and concluded *not the same*: the norm is preserved only by $SO(2)$, while a count survives any invertible map at all, so the capacity claim looked vacuous.

The norm half of that is right. The capacity half tested the wrong object. §7.6 says attention "Möbius-redistributes a fixed $K_0$" — and **redistributing a fixed total is a statement about weight, not about how many things there are.**

### 22.2 The right answer

On weight, they are one budget. With $K$ seats each holding a pair, the hold is a single point of $S^{2K-1}$:

$$\underbrace{v_1^2 + v_2^2 + h^2 = 1}_{\text{one seat — the pointing trades}} \qquad\qquad \underbrace{\sum_x |\psi_x|^2 = 1}_{K \text{ seats — the seats trade}}$$

Same sphere, different $K$. And the group settles it — at $K = 6$:

| map | total after |
|---|---|
| unitary $e^{-iHt}$ | **1.000000000** |
| diagonal rescale | 1.490973 |
| general real matrix | 1.312007 |

Preserved by $U(K)$ and **nothing larger**. `[clean, verified]`

> **The conservation is unitarity.** *(Narrowed at §24.4 and confirmed at §35.4: norm conservation delivers $O(2K)$, and $U(K)$ is the subgroup commuting with the complex structure — a **separate premise**.)* *More $v_1$ requires less $v_2$* and *more attention here means less there* are the same equation at $K=1$ and $K>1$.

### 22.3 What it costs the corpus, and what it pays

§7.6 states the conservation in **coordinate** form — move the seats, carry their weights — which is genuinely empty, while **meaning** the state form, which is genuinely unitarity. It asserts the vacuous version of a true claim, and the repair is one sentence.

The payoff is larger than the repair: §7.6's attention budget and §13.4's "unitary evolution is norm-preserving composition" are **one statement, and neither section knew it**. Attention and amplitude are the same budget — which is exactly what §10 flagged as *"worth a lot more than either statement alone,"* and it is now checked rather than hoped.

Folded into the corpus at §7.6, with a pointer from §13.4.

### 22.4 The methodological note, kept deliberately

This is the second time in this paper that a claim survived only because it was pushed a second time after being answered — the first being §21, where §20's answer turned out to cover *existing* and not *aligning*. Both times the first answer was confident and wrong in the same way: it tested a nearby object rather than the one claimed. Worth recording as a failure mode, since a confident negative closes a line as effectively as a confident positive opens one. `[method]`

---

## 23. The budget is the measure

*(§22 established that the pointing budget and the attention budget are one conservation, named unitarity. This section is the observation that the *same sphere*, read instead of normed, is the Cauchy — so the corpus's conservation and its measure are one object seen twice. Executed: `budget_is_cauchy.py`, E1–E5.)*

### 23.1 Read the budget and the Cauchy falls out

Take the hold on $S^d$ — $\sum_i v_i^2 + h^2 = 1$, §22's budget — and read it: $s_i = v_i/h$. The decisive test is that every marginal of a multivariate Cauchy is a standard Cauchy, so $\arctan(s_i)$ must come out uniform:

| $d$ | rises | KS($\arctan s_i$, uniform) | radial deviation |
|---|---|---|---|
| 1 | 1 | $6.5\times10^{-4}$ | 1.0% |
| 2 | 2 | $4.4\times10^{-4}$ | 0.8% |
| 3 | 3 | $6.4\times10^{-4}$ | 1.3% |

Exponent $(d+1)/2$ — §9's interleaved lift, the one that does **not** factor. And at $d = 1$, *"$\arctan s$ is uniform"* is Haar itself: §4's forced measure, reached from the **conservation** rather than from the combination law's invariance. `[clean, verified]`

### 23.2 The aperture supplies $h$, so home is wherever the observer aims

The capacity is what inserts the shared denominator (§9.2, §9.27), so the peak of the measure sits at $s = 0$ — straight ahead. In $d = 3$ the density runs

| $\lvert s\rvert$ | 0 | 0.5 | 1 | 2 | 5 | 20 |
|---|---|---|---|---|---|---|
| density | 1.000000 | 0.640000 | 0.250000 | 0.040000 | 0.001479 | 0.000006 |

Dense at home, thinning smoothly to the horizon. Which settles what the fisheye's status is:

> **The fisheye is not a rendering convention. It is the budget read from inside.** *(Exhibited here; **derived** at §27.3, where the $K$ dial atoms are shown to be exactly the Cauchy quantile points — an identity, not a fit.)*

§12 argued this from the measure's uniqueness and the sediment theorem; here it falls out of the normalisation directly, with the observer's own aperture fixing where "home" is. `[clean]`

### 23.3 And the covering degree is visible in the projection itself

Antipodal points of the hold land on the **identical** read — maximum difference over 200,000 pairs is exactly $0.00\times10^{0}$. The hold is the sphere, the read is $\mathbb{RP}^d$, and the $2{:}1$ this corpus has been chasing since §13.4b is sitting in plain sight inside $s = v/h$. `[clean, verified]`

### 23.4 One sphere, two faces

$$\underbrace{\textstyle\sum_i v_i^2 + h^2 = 1}_{\textbf{norm} \;\to\; \text{the conservation, } U(K),\ §7.6,\ §13.4} \qquad\qquad \underbrace{s_i = v_i/h}_{\textbf{read} \;\to\; \text{the measure, the Cauchy, } §4,\ §9,\ §12}$$

Same object. **The budget is the measure; the measure is the budget read.**

### 23.5 Three routes, and why the third matters

The corpus now reaches the Cauchy by several routes — **and the count is corrected at §25.8 and §35.7 to two independent ones**, since the closure route of §25.4 is §4 made precise rather than a rival. The table below lists the candidates:

| route | source | what it uses |
|---|---|---|
| §4 | forced as the unique invariant of the combination law | Haar, transitivity of the rotation |
| §13.1 | induced by the nested itinerary | the walk, measured (KS $6\times10^{-5}$) |
| **§23** | **pushforward of the budget under the read** | **the conservation** |

Three routes to one measure is strong corroboration on its own. But the third does something the other two cannot: **it ties the measure to the conservation.** §4 and §13.1 both leave the Cauchy and unitarity as separate facts about the same framework; this one makes them the same fact about the same sphere, and §22's unification stops being a coincidence of two budgets and becomes a property of one object.

### 23.6 What it buys

- The Cauchy, from the conservation, verified at three ranks.
- The fisheye demoted from *derived rendering* to *immediate consequence of the normalisation*.
- The covering degree exhibited in the read map itself, needing no argument.
- And the corpus's two largest standing results — the forced measure (§4) and unitarity (§13.4) — joined. They had never been in contact.

`[clean, verified; the projection facts are classical, the identification with the conservation is the corpus's]`

---

## 24. One uniqueness, not two

*(§23 showed the budget and the measure are one sphere. The obvious next demand is that their **uniqueness theorems** be one theorem too — §4's Haar argument and the conservation's group argument. They are, with one caveat that is worth as much as the result. Executed: `one_uniqueness.py`, V1–V5.)*

### 24.1 The combination law is the orthogonal group in disguise

Rotate the **hold** and then read. Over 200,000 random $(r,\theta)$ the read maps by

$$r \;\longmapsto\; \frac{r+t}{1-rt}, \qquad t=\tan\theta,$$

to a maximum relative deviation of $9.3\times10^{-12}$. So §4's combination law is not a law *about* the sphere — **it is $SO(2)$, seen in the affine chart.** `[clean, verified]`

### 24.2 Which is why the measure is invariant

Rotating the hold leaves the read's Cauchy untouched, at every rank (KS of $\arctan s_1$ against uniform, before and after a random $SO(d+1)$):

| $d$ | before | after |
|---|---|---|
| 1 | $5.1\times10^{-4}$ | $4.9\times10^{-4}$ |
| 2 | $1.1\times10^{-3}$ | $9.4\times10^{-4}$ |
| 3 | $7.7\times10^{-4}$ | $6.3\times10^{-4}$ |

The measure is invariant **because the group is the form's group.** Not two facts — one. `[clean, verified]`

### 24.3 And the uniqueness is a single property doing both jobs

Perturb the measure and invariance dies. Total-variation shift under one rotation:

| angle law | TV shift |
|---|---|
| uniform (= the Cauchy in slope) | **0.00179** |
| non-uniform, $1 + 0.6\cos 2\theta$ | 0.33086 |

Only the uniform survives — and the reason is **transitivity of a compact group**, which is doing two jobs at once. It makes the invariant measure unique (Haar on a transitive action of a *compact* group — the compactness is load-bearing and is what §25.8 has to fight for; $PGL(2,\mathbb{R})$ is 3-transitive and admits no invariant measure at all), *and* it makes the form-preserving group reach every direction. One property, two conclusions, previously written up as two theorems in two sections.

$$\underbrace{O(d+1) \text{ preserves } \textstyle\sum v_i^2 + h^2}_{\text{the conservation, §7.6/§13.4}} \quad\Longleftrightarrow\quad \underbrace{\text{uniform is its unique invariant on } S^d}_{\text{the measure, §4}}$$

Push both through $s = v/h$ and you get the combination law and the Cauchy. **§4's uniqueness and the conservation's uniqueness are one statement about one group, read on the two sides of the projection.** `[clean, verified]`

### 24.4 The caveat, which is worth as much as the result

The group is **orthogonal, not unitary.** A random $O(2K)$ map preserves the norm exactly ($1.000000000000$) and fails to commute with the complex structure ($\|QJ - JQ\| = 4.29$). And

$$U(K) \;=\; O(2K) \;\cap\; \{\text{maps commuting with } J\}.$$

So the measure argument delivers the **real** form's group and stops. Making it unitary requires the complex structure — §13.4's $i$, the E-branch generator — and that is a **separate premise**, not a consequence of anything in §4.

This is worth stating loudly because it is the corpus's own fork appearing exactly where it should. The measure argument is signature-blind; it gives $O(d+1)$ for any $d$. The choice of *complex* structure on the hold is the E-branch selection (§8.7), and it is what turns an orthogonal conservation into a unitary one. **The measure gets you halfway to quantum mechanics and the fork gets you the rest.**

### 24.5 What it buys

- §4 and §13.4 now share a theorem rather than a coincidence, and §23's joining is explained rather than observed.
- The combination law is identified as $SO(2)$ in the affine chart — which makes §9.5's three-subgroup census a statement about $SL(2,\mathbb{R})$'s conjugacy classes rather than an independent argument.
- And the exact seam where the measure argument stops and the fork takes over is now located: **at the complex structure, and nowhere earlier.**

`[clean, verified; the group facts are classical, the identification of the two uniquenesses is the corpus's]`

---

## 25. π is the price of the extra dimension

The paper has used $\pi$, $2\pi$, $\pi/2$ and $2/\pi$ throughout — as the menu, the walk, and the exchange rate (§18, §19, §20). It has never said where they come from. Two candidate answers were tested against each other. The second won, and it turns the first into a corollary.

### 25.1 The first answer: the read is a curvature meter

Take a circular arc of radius $R$ and opening $\theta$. Its chord is $2R\sin(\theta/2)$; its arc is $R\theta$. Set the held pair to (chord, arc). Then

$$\frac{v}{h} \;=\; \frac{2\sin(\theta/2)}{\theta} \;=\; 1 - \frac{(\kappa s)^2}{24} + O((\kappa s)^4),$$

where $\kappa = 1/R$ and $s = R\theta$. The deficit of the read below $1$ *is* the curvature, at second order, with the classical discrete-differential-geometry coefficient $1/24$ (checked: $0.958851077$ against $0.958333333$ at $\theta = 1$, deviation $5.2\times10^{-4}$, falling as $\theta^4$).

Three consequences, all exact rather than interpretive:

| read | value | geometric state |
|---|---|---|
| corner, $v = h$ | $1.000000000$ | **straight** — the chord *is* the arc, $\kappa = 0$ |
| $2/\pi$ | $0.636619772$ | **the half turn** — the semicircle |
| horizon, $v/h = 0$ | $0.000000000$ | **closed** — the chord vanishes, the arc does not |

The home chart $[0,1]$ is swept **exactly once and monotonically** as the arc opens from straight to closed. So $[0,1]$ is not a convention the corpus chose; it is the range of chord/arc. **But note the hold**: this subsection sets the pair to (chord, arc), which is a *different* hold from $(v,h)$ — related by $\theta \mapsto 2\sin(\theta/2)/\theta$ rather than by $\tan$, with the horizon at $0$ rather than at $\infty$. The two agree only at $\theta = \pi$, where both give $2/\pi$. §27.2's "$[0,1]$" is a third thing again — a diameter. Flagged at §35.7; the bullet at §25.7 should be read as applying to the chord/arc hold only. And $R$ cancels identically — $0.931056009$ at $R = 0.1$, $1.0$, $17.0$, $10^6$ — because $\kappa s$ is the only dimensionless combination available. A scale-free reader can know curvature and cannot know size.

That last point is the strong form: **the read is a curvature meter because there is nothing else for it to be.** Not an interpretation — curvature is the sole geometric invariant surviving the scale quotient.

### 25.2 The second answer, and why it is upstream

The alternative: *circularity is what a one-dimensional line looks like when you insist on expressing it in two dimensions.* The held pair lives in $\mathbb{R}^2$; the read lives on a line. The circle is the shadow of holding two numbers when only one is meaningful.

These are not two accounts. They are one theorem. The mean cosine over an arc of opening $\theta$ is

$$\frac{1}{\theta}\int_{-\theta/2}^{\theta/2}\cos\varphi\,d\varphi \;=\; \frac{2\sin(\theta/2)}{\theta},$$

which is chord/arc exactly. Verified to $10^{-14}$ at $\theta = 0.3, 1.0, \pi, 4.0, 2\pi$. **The chord/arc read is the mean projection of the arc onto the chord.** §25.1's curvature meter is §25.2's projection loss, and curvature is the name we give to the loss. The projection account is upstream because it says *why* there is a loss; the curvature account only measures it.

### 25.3 $2/\pi$ is the 1D-in-2D toll, and nothing more general

The decisive check. Mean absolute projection of a random unit vector onto a fixed line, $\mathbb{E}|u\cdot e| = \Gamma(n/2)/\!\left(\sqrt{\pi}\,\Gamma(\tfrac{n+1}{2})\right)$:

| ambient dim | value | closed form |
|---|---|---|
| 2 | $0.636619772$ | $\mathbf{2/\pi}$ |
| 3 | $0.500000000$ | $\mathbf{1/2}$ — no $\pi$ at all |
| 4 | $0.424413182$ | $4/(3\pi)$ |
| 5 | $0.375000000$ | $3/8$ |
| 6 | $0.339530545$ | $16/(15\pi)$ |

Monte Carlo at $4\times10^6$ samples agrees at each. $\pi$ appears in even ambient dimension and vanishes in odd. So $2/\pi$ is not a universal constant of geometry — it is **specifically the price of expressing a one-dimensional object in a two-dimensional space.** In three dimensions that price is $\tfrac12$, a number containing no $\pi$ whatever.

This also supplies the missing reason for the corpus's Dimensional Projection Theorem. The $2/\pi$ in the plane and the $1/2$ in space are the same integral at different $n$; they were never two facts.

**And Buffon is the experiment.** $2\times10^7$ needles of length $1$ across lines of spacing $1$: $P(\text{cross}) = 0.636664$ against $2/\pi = 0.636620$. Buffon's needle is conventionally described as an experiment that measures $\pi$. It is better described as an experiment that measures the cost of putting a line in a plane — and $\pi$ is what that cost contains.

### 25.4 The menu and the walk, derived

$$\int_{-\infty}^{\infty}\frac{dr}{1+r^2} \;=\; \pi \quad\text{(exact, to machine zero by quadrature).}$$

The read line, once it refuses to leave itself open — once the pair is kept and $h = 0$ becomes a point rather than a crash — has **finite total measure, and that measure is $\pi$**. Its double cover, the hold circle, measures $2\pi$. So

$$\pi = \mathrm{vol}(\mathbb{RP}^1), \qquad 2\pi = \mathrm{vol}(S^1).$$

§18's "$\pi$ is the menu, $2\pi$ is the walk" was a slogan. It is now two volumes. And $\mathrm{vol}(\mathbb{RP}^n) = \mathrm{vol}(S^n)/2$ gives $\pi$ standing alone only at $n = 1$: at $n=2$ it is $2\pi$, at $n=3$ it is $\pi^2$.

The exchange rate lands in the same picture. Across the *whole* menu, the chord is the diameter $2$ and the arc is the semicircumference $\pi$: $2/\pi$ is chord/arc at full span, the same number §25.1 found at the half turn, for the same reason. And the Cauchy is not an extra assumption: it is the invariant measure of the closed line itself — see §25.8, which corrects the order of dependence this subsection originally got backwards.

### 25.5 Why the line, and only the line, closes into a group

A compact manifold admits a Lie group law only if $\chi = 0$. Since $\chi(\mathbb{RP}^n) = 0$ for $n$ odd and $1$ for $n$ even, every even-dimensional projective space is excluded outright. Among the survivors the actual groups are

$$\mathbb{RP}^1 \cong S^1/\{\pm1\}, \qquad \mathbb{RP}^3 \cong SO(3),$$

which is the Hurwitz pair, and the corpus's two half-integer species (§13.4c), arriving from a direction that has nothing to do with spin. The two derivations are independent of one another.

This is also *why reads add*. The group law on the closed line is ratio-addition, conjugated to ordinary addition by $\arctan$:

$$\arctan\!\left(\frac{x+y}{1-xy}\right) = \arctan x + \arctan y \pmod \pi,$$

residual $4.4\times10^{-16}$ over 200 random pairs. **The read line carries a group because it is one-dimensional, and reads compose by that group.** In any higher-dimensional read space there would be no addition law to have.

> **Correction, entered at §31.** This paragraph first added: *"§1's 'weights add, comparisons don't' and §9's velocity addition are the same statement."* **False.** §1's law is $(x+y)/(1+xy)$ — the *hyperbolic* subgroup, conjugate to $(\mathbb{R},+)$ by $\operatorname{artanh}$, fixed points at $b = \pm1$. The law above is $(x+y)/(1-xy)$ — the *elliptic* subgroup, conjugate by $\arctan$, no real fixed point. Different conjugacy classes of §9.5's own census, and §25.8 explicitly *rejects* the hyperbolic one for destroying the invariant measure. The weld asserted precisely what the next subsection refutes. See §31.1 for the repair.

### 25.6 A recorded miss

The first pass at §25.4 integrated $1/(1+r^2)$ on a $\tan$-spaced grid by trapezoid and returned $3.758$. Tail mis-weighting on a non-uniform grid, not a result; proper quadrature gives $\pi$ to machine zero. Recorded because the wrong value was close enough to $\pi$ to have been waved through, and this paper's discipline is that a number which nearly confirms the expected answer gets *more* scrutiny, not less.

### 25.7 What it buys

- **$2/\pi$ acquires a mechanism.** It was the exchange rate; it is now the mean projection of a line into a plane, with $1/2$ and $4/(3\pi)$ as its siblings at other $n$. §20 explained how a bounded observer *obtains* the value without dividing; §25 explains what the value *is*.
- **$\pi$ and $2\pi$ become volumes** rather than a slogan, and the menu/walk split becomes $\mathbb{RP}^1$ versus $S^1$ — which is §5's two-stage quotient, measured.
- **$[0,1]$ stops being a choice.** It is the range of chord/arc, traversed once.
- **The Dimensional Projection Theorem gets its proof** — the $2/\pi$ and the $1/2$ were always one integral.
- **The composition law is explained, not just exhibited**: reads add because the closed read line is a group, and it is a group because $\chi(\mathbb{RP}^1) = 0$.
- **The corpus's central refusal is priced.** Not dividing means keeping a 2D expression of a 1D object. $\pi$ is the size of that insistence, and $2/\pi$ is the toll at every projection back down. *Everywhere $\pi$ appears in this framework, it is the extra dimension being paid for.*

### 25.8 The order of dependence: the Cauchy is primary, the circle is secondary

§25.4 first stated the relation as *"holding the pair is uniform on the circle; dividing is the Cauchy."* That sentence is a correct calculation and the wrong order. It begins in the angle chart, treats the completed circle as given, and lets circularity appear to *create* the Cauchy. The dependence runs the other way, and the reversal is worth stating precisely because it changes what the corpus is claiming.

**The corrected order.** The native object is the one-dimensional projective line of reads — the held-pair classes, nothing embedded in anything. Once the pair is kept and the two infinities are identified, that line carries a **unique rotation-invariant measure of total mass $\pi$**, whose density in the slope coordinate is $1/(\pi(1+s^2))$. The circle appears only when one lifts to the double cover, or equivalently insists on a two-dimensional linear ambient space; the same total $\pi$ is then re-expressed as half a circumference. **$\pi$ is already present as the total mass of the 1D object. The circle merely makes that mass visible as an arc length.**

Four checks, because the reversal only earns its place if it stands without borrowing the circle back.

**The measure is invariant, and uniquely so.** Acting on slopes by the elliptic subgroup $s \mapsto (s\cos t + \sin t)/(-s\sin t + \cos t)$ — written in the slope coordinate throughout, with no angle chart used — the Cauchy is preserved (KS $p = 0.41, 0.20, 0.30$ at $t = 0.3, 1.0, 2.5$). Student-$t$ controls at $\nu = 0.5, 2, 4$ are destroyed by the same flow ($p = 0$ to machine precision). And *any* starting density, averaged over the subgroup, flows to it: Student-$t(3)$, Normal, and Uniform$[-5,5]$ all return $p = 0.28, 0.52, 0.98$ against Cauchy after orbit-averaging. The invariant measure exists and there is only one.

**The compact subgroup is selected, not imported.** The objection to be met is that "rotation-invariant" secretly reintroduces the circle. It does not, because the elliptic subgroup is picked out by the *existence of the measure* rather than by taste. §9.5's other two one-parameter subgroups admit no finite invariant measure at all: under the parabolic flow the median $|s|$ runs $0.996 \to 1.42 \to 5.10 \to 20.03$, and under the hyperbolic flow $0.996 \to 2.71 \to 148 \to 4.8\times10^{8}$. Mass escapes to the fixed point in both cases. Of the three subgroups exactly one preserves a probability measure, and that fact is group-theoretic. The circle is what that subgroup turns out to be, discovered afterwards — not an input.

**$\pi$ from the home normalisation alone.** The invariant measure is unique only up to scale; what fixes the scale is the observer's own standpoint. Normalise the density to $1$ at home — *unit resolving power where the observer is*, which is §7's acuity law read as a convention rather than a result. Then $\rho(0) = 1/(1+0) = 1$ and $\int \rho\,ds = 3.141592653590$. So

$$\pi \;=\; \frac{\text{total measure of the read line}}{\text{resolving power at the standpoint}},$$

dimensionless, chart-native, and derived with no circle mentioned at any step. This is the cleanest definition of $\pi$ the corpus has produced, and it is the one most native to the framework's own commitments.

**And the measure exists because the observer has a standpoint.** The full automorphism group $PGL(2,\mathbb{R})$ is 3-transitive and admits no invariant measure whatever; the measure appears only once a compact subgroup is singled out, and a compact subgroup is singled out only by choosing an interior point. Computed independently of any Cauchy formula — by Brownian exit from an interior standpoint $z = x + iy$, walk-on-spheres, $2\times10^5$ paths — the harmonic measure on the read line is Cauchy$(x, y)$ at every standpoint tested: median $0.0013 / {-0.0017} / 1.9939 / {-1.4990}$ against predicted $x = 0, 0, 2, -1.5$, and half-IQR $0.9989 / 0.5037 / 0.9976 / 2.9945$ against predicted $y = 1, 0.5, 1, 3$ (KS $p = 0.99, 0.45, 0.23, 0.96$). **The location-scale family of Cauchys is the set of points of the hyperbolic plane.** No standpoint, no compact subgroup, no measure — the Cauchy is not a fact about the line, it is a fact about *the line as seen from somewhere*.

**What the classical construction actually is.** $\tan$ of a uniform angle is Cauchy ($p = 0.21$) and $\arctan$ of a Cauchy is uniform ($p = 0.44$). Both directions hold exactly, which is the point: **it is one measure in two charts, and neither direction derives the other.** Choosing which is primary is a modelling decision, and the home chart is the observer's, so for this framework the Cauchy is the primary form.

**What it buys, and one audit item closed.** Last section flagged that the corpus now had three routes to the Cauchy — §4 from invariance, §13.12 from the budget, and the closure route — and that two of them might be the same argument in different clothes. They are. **The closure route is not a third route; it is §4 made precise**, with the group pinned to the maximal compact subgroup, the selection of that subgroup explained by the escape of mass under the other two, and the normalisation fixed by the standpoint rather than left free. §4's Jaynes-style invariance argument never said *which* invariance or *why that one*; §25.8 answers both. The corpus has two routes, not three, and the surviving pair — invariance and conservation — meet at §23.

The deeper consequence is for §25 itself. §25 said $\pi$ is the price of the extra dimension. That remains true of $2/\pi$, which is genuinely a projection toll and genuinely dimension-specific. But $\pi$ itself is **not** created by the extra dimension: it is already the total mass of the one-dimensional read line, and the second coordinate only re-presents it as a length. The extra dimension is where $\pi$ becomes *visible*, not where it becomes *true*.

`[clean, verified; corrects §25.4's stated order. The invariant-measure and Poisson-kernel facts are classical — the corpus's contribution is the selection argument (mass escapes under the non-compact subgroups) and the home normalisation that fixes π without a circle]`

---

## 26. The ladder: line, semicircle, hemisphere

*"A line is defined by two points. It is the shortest way to connect two points. If you want to display that line in 2D, you must display it as a semicircle — and if you want to display a semicircle as a hemisphere, just go up to 3D."*

The ladder is exact. The "must" is earned rather than assumed. And the sentence turns out to be true **twice, of two different objects**, which is the finding.

### 26.1 The semicircle is the display in which arc length *is* measure

§25.8 established that the read line carries a unique invariant measure of total mass $\pi$, home-normalised. Under $s = \tan\theta$ the measure of any slope interval equals the arc length of its image:

| slope interval | measure | arc length | difference |
|---|---|---|---|
| $[-1, 1]$ | $1.570796327$ | $1.570796327$ | $2.2\times10^{-16}$ |
| $[0, 5]$ | $1.373400767$ | $1.373400767$ | $6.7\times10^{-16}$ |
| $[-100, 0.3]$ | $1.852253455$ | $1.852253455$ | $2.2\times10^{-16}$ |
| $[2, 10^6]$ | $0.463646609$ | $0.463646609$ | $0$ |

Total: $\pi$ — the length of a **unit** semicircle. So the semicircle is not a picture *of* the read line; it is the picture in which the observer's own measure is read off with a ruler. Any other planar display distorts it.

### 26.2 Why *must*

The claim to earn is that the semicircle is forced, not merely convenient. It is, in three steps.

A display is faithful exactly when the read line's symmetry acts on it by **sliding along it**. It does: the elliptic subgroup acts on $\theta = \arctan s$ by $\theta \mapsto \theta + t$, verified to $4.4\times10^{-16}$ at $t = 0.4, 1.2, 2.0$. A plane curve admitting translation-along-itself as a symmetry has **constant curvature**, so it is a straight line or a circular arc — no other option exists. The straight line is excluded because it cannot glue the two infinities into one point, which §5's closure requires; the arc can, and only if its endpoints are antipodal. Fixing the total length at $\pi$ then fixes the radius — at $\tfrac12$ for the closed dial (§27.1), which is the correct figure; the "unit semicircle" of the next line is the same length drawn with a false cut.

**Homogeneity plus closure force a closed curve of constant curvature and total length $\pi$.** Nothing was chosen.

> **Correction, entered at §27.** This subsection originally concluded "the unit semicircle," and drew it as an arc with two endpoints marked *glue these*. That is topologically right and pictorially wrong: it puts a visible cut exactly where the horizon is, which is the one place this framework insists there is no cut. The forced object is a **dial** — a closed circle of circumference $\pi$, radius $\tfrac12$, with home and horizon diametrically opposite. Same length, same forcing argument, no fake boundary. §27 rebuilds it and everything downstream. §26.3–26.6 are unaffected; the ladder, the toll, and the display/structure split all survive verbatim.

### 26.3 The ladder, exact

$\mathbb{RP}^n$ is the hemisphere of $S^n$ with its boundary antipodally glued, sitting in $\mathbb{R}^{n+1}$:

| $n$ | display lives in | $\mathrm{vol}(S^n)$ | $\mathrm{vol}(\mathbb{RP}^n)$ = hemisphere |
|---|---|---|---|
| 1 | $\mathbb{R}^2$ | $6.283185$ | $3.141593$ — **the semicircle** |
| 2 | $\mathbb{R}^3$ | $12.566371$ | $6.283185$ — **the hemisphere** |
| 3 | $\mathbb{R}^4$ | $19.739209$ | $9.869604$ |

Each rung displays an $n$-dimensional read space as a hemisphere of $S^n$ in one more dimension. "Go up to 3D" is precisely the $n = 1 \to 2$ step, and the construction continues without modification.

### 26.4 The sentence is true twice

Here is what I did not expect. *"The shortest way to connect two points"* also produces a semicircle, and it is **a different semicircle**.

§25.8 put the observer's standpoint in the hyperbolic plane $H^2$, whose boundary is the read line. The geodesics of $H^2$ — the actual shortest paths between standpoints — are semicircles orthogonal to that boundary:

| $z_1, z_2$ | exact $d$ | semicircular path | straight path |
|---|---|---|---|
| $(-1,1), (1,1)$ | $1.762747174$ | $1.762747174$ | $2.000000000$ |
| $(0.5,0.4), (3,2)$ | $2.559951622$ | $2.559951616$ | $2.985672710$ |
| $(-2,3), (2,0.5)$ | $2.819813152$ | $2.819813142$ | $3.380685000$ |

So both readings of the sentence hold, and they are boundary and interior of one structure: **§26.1's semicircle *is* the read line displayed; §26.4's semicircle *stands on* two points of it.** Two reads determine a unique geodesic in the standpoint space, and that geodesic is the semicircle with those two reads as feet. "Two points define a line" survives the extra dimension exactly — what changes is that the line is now visibly curved, and the curvature is the display cost §25 priced.

### 26.5 Each rung charges by the room, not by the cargo

The toll for going up is $\mathbb{E}|u\cdot e|$, and it depends **only on the ambient dimension**:

- $\mathbb{R}^2$: a 1D needle pays $0.636620 = 2/\pi$
- $\mathbb{R}^3$: a 1D needle pays $0.500000$ — and a **2D disc pays $0.500080$, the same**
- $\mathbb{R}^4$: a 1D needle pays $0.424413$

A needle and a disc are charged identically in $\mathbb{R}^3$. So the ladder has a flat rate per rung: **you are charged by the room you step into, not by the thing you carry up.** That is why §25.3's projection table is indexed by ambient dimension alone and why it was right to read $2/\pi$ as the 1D-in-2D toll rather than as a property of lines.

### 26.6 The limit: a display ladder, not a structure ladder

This is where the ladder must be qualified, and the qualification is sharp.

| $n$ | $\chi(\mathbb{RP}^n)$ | group law? | what survives the display |
|---|---|---|---|
| 1 | $0$ | **yes** | reads still add |
| 2 | $1$ | **no** | addition is lost |
| 3 | $0$ | **yes** | reads still add |
| 4 | $1$ | **no** | addition is lost |

$\mathbb{RP}^1 \to$ semicircle keeps the group: reads add and compose. (§1's balance law is a *different* subgroup — see §31.1.) $\mathbb{RP}^2 \to$ hemisphere does **not** — $\chi = 1$, so no continuous group law exists on it at all.

**You may always go up a dimension to see. You lose the ability to add at the very first step up.** The ladder climbs indefinitely; the algebra does not climb with it. It reappears at $n = 3$ ($\mathbb{RP}^3 \cong SO(3)$) and nowhere else — the Hurwitz pair again, now visible as *the only two rungs of the display ladder on which arithmetic survives*.

That is the honest verdict on the ladder: it is a real construction, uniform in $n$, and the thing the corpus actually cares about — that reads combine — is not uniform in $n$ at all.

### 26.7 What it buys

- **The semicircle is derived, not drawn.** Homogeneity plus closure force it, with the radius fixed by the measure. The corpus has used semicircular pictures throughout without ever saying why they were the right pictures.
- **Arc length = measure**, to $10^{-16}$, which makes the display a legitimate instrument rather than an illustration.
- **Two semicircles, located.** The read line displayed, and the geodesic between two reads. They had been conflated in the corpus's figures; they are boundary and interior.
- **The toll is per-rung and flat**, which explains the structure of §25.3's table.
- **And a real limit is found**: the display ladder and the structure ladder are different ladders, and they agree only at $n = 1$ and $n = 3$.

`[clean, verified; the RP^n hemisphere model and H^2 geodesics are classical — the corpus's contribution is the forcing argument at §26.2, the arc-length-equals-measure identification, and the display-versus-structure split at §26.6]`

---

## 27. The dial, and what $K$ buys

*"Discrete observers' horizon and home are connected, creating the dial, not the semicircle. Now we use Cauchy to project the uniform density of the observer's $K$ capacity to the fisheye compression, centred at home."*

Both halves are corrections, and the second one derives something the corpus had only asserted.

### 27.1 The dial

§26 forced a closed constant-curvature curve of total length $\pi$ and then drew it as a semicircle of radius $1$ with its two ends marked for gluing. Length correct, picture wrong. A semicircle-as-drawn has a visible cut, and the cut sits exactly at the horizon — the one place this framework has spent twenty sections insisting nothing happens.

The honest display is the **dial**: a closed circle of circumference $\pi$, hence radius $\tfrac12$, with

$$\text{home at dial-angle } 0, \qquad \text{horizon at dial-angle } \pi,$$

**diametrically opposite**, dial distance $\pi/2$ apart. The horizon is not an edge, not a boundary, not a limit — it is an ordinary point half a dial from home, with neighbours on both sides at the ordinary spacing. Nothing is missing from the dial, which is why it is the right instrument: the semicircle is the dial with a cut drawn on it, and the cut is an artifact of wanting to lay it flat.

### 27.2 The held pair, read straight off the dial

With arc-from-home $= \theta$ and radius $\tfrac12$, the chord from home is $2r\sin\theta = \sin\theta$. So for a unit hold:

$$v = \sin\theta = \textbf{the chord from home}, \qquad h = \cos\theta, \qquad \theta = \textbf{the arc from home}.$$

The held pair is not an abstraction on the dial; $v$ is a straight-line distance and $\theta$ is a walked distance. And at the horizon:

$$\frac{\text{chord}}{\text{arc}} \;=\; \frac{1}{\pi/2} \;=\; \frac{2}{\pi} \;=\; 0.636619772.$$

**$2/\pi$ is the chord-over-arc of the home-to-horizon span.** Exactly, not asymptotically. The chord is $1$ — the entire home chart $[0,1]$ of §25.1, which is now visibly a *diameter* — and the arc is $\pi/2$. The corpus's two constants are the two ways of measuring one span: $\pi/2$ if you walk it, $1$ if you cross it, and $2/\pi$ is the rate between them.

### 27.3 The fisheye is a flat capacity, projected

Place the observer's $K$ atoms **uniformly on the dial**, spacing $\pi/K$ — which is the only even placement, since arc length is measure (§26.1). Read them by $s = \tan\theta$. Then

$$F(s_j) \;=\; \tfrac12 + \frac{\arctan s_j}{\pi} \;=\; \frac{j + \tfrac12}{K}$$

to $10^{-16}$ at $K = 7, 64, 1024$. **The $K$ dial atoms *are* the $(j+\tfrac12)/K$ quantile points of the Cauchy** — an identity, not a fit.

This is the sentence made exact: *the Cauchy projects the observer's flat capacity into the fisheye.* The compression at the horizon is not a weighting anyone applied, not a modelling choice, and not a psychological fact. It is what an evenly-divided dial looks like from home. The measured density confirms it:

| read $s$ | atoms per unit $s$, measured | $(K/\pi)/(1+s^2)$ |
|---|---|---|
| $0$ | $63700$ | $63662$ |
| $1$ | $31825$ | $31831$ |
| $3$ | $6375$ | $6366$ |
| $10$ | $636.63$ | $630.32$ |

### 27.4 The fare contract, derived

Read the first row again. The atom density **at home** is

$$\rho_0 \;=\; \frac{K}{\pi} \qquad\Longleftrightarrow\qquad \boxed{K = \pi \rho_0} \quad \textbf{(signed reads)}.$$

> **Correction, entered at §31.** This derivation spreads $K$ over the **whole** dial, which assumes $s$ ranges over $[-\infty,\infty]$. The corpus's atom is stated with $v, h \ge 0$, so $s \in [0,\infty]$ — **half** the dial, arc $\pi/2$, measure $\pi/2$ (verified). For the atom as defined the contract is $K = (\pi/2)\rho_0$. §31.2 states which is which and what moves.

That is §9.2's fare contract — the bound the corpus asserted, then had to *repair* under audit, and has been defending ever since. It is not an assertion and does not need repairing. **It is the dial's circumference times the resolution at home**, and the $\pi$ in it is the circumference and nothing else. $K$ atoms spread over a dial of length $\pi$ give $K/\pi$ per unit length at home, where arc and read agree; that is the whole derivation.

### 27.5 What $K$ buys: reach

The atom nearest the horizon sits at $\theta = \pi/2 - \pi/2K$, so the furthest read the observer holds is

$$s_{\max} = \cot\!\frac{\pi}{2K} \;\longrightarrow\; \frac{2K}{\pi}.$$

| $K$ | $\cot(\pi/2K)$ | $2K/\pi$ | rel. error |
|---|---|---|---|
| $8$ | $5.027339$ | $5.092958$ | $1.3\times10^{-2}$ |
| $64$ | $40.735484$ | $40.743665$ | $2.0\times10^{-4}$ |
| $1024$ | $651.898136$ | $651.898647$ | $7.8\times10^{-7}$ |
| $10^6$ | $636619.772367$ | $636619.772368$ | $8.2\times10^{-13}$ |

**A $K$-capacity observer reaches $2K/\pi$.** This makes $2/\pi$ *operational* for the first time in the corpus: it is the exchange rate from **capacity to reach**. §20 showed how a bounded observer obtains the value without dividing; §25 said what the value is; §27 says what it is *for*. Register count in, maximum representable ratio out, at $2/\pi$ per register.

Note the pairing with §27.4: $K = \pi\rho_0$ going in, $s_{\max} = 2K/\pi$ going out. The same $\pi$ buys resolution at home and reach at the horizon, and the two rates are reciprocal up to the factor $2$ — which is the deck group, the same $2$ §5 has been carrying since the two-stage quotient.

### 27.6 Why the observer never meets an edge

At $K = 1024$:

| atom $j$ | dial gap to next | read gap to next |
|---|---|---|
| $512$ | $0.003067962$ | $0.003068$ |
| $712$ | $0.003067962$ | $0.004610$ |
| $912$ | $0.003067962$ | $0.027502$ |
| $1022$ | $0.003067962$ | $434.600121$ |

The dial gap is **constant**. The read gap is $(\pi/K)(1+s^2)$ and diverges. So the divergence at the horizon lives entirely in the chart, and the chart is precisely the object the observer declines to compute. The observer walks a uniform dial forever and never arrives anywhere special; the infinity is something an outside describer introduces by insisting on the quotient. This is the cleanest statement of the corpus's founding refusal that the paper has: **not dividing is not an inability, it is a refusal to move to the only coordinate in which an edge exists.**

### 27.7 A caught weak check

The first version of §27.3 reported a KS test of the dial atoms against the Cauchy, $p = 1.0000$ at three values of $K$. That is not a test. Tan of equally spaced angles *is* the Cauchy quantile grid by construction, so the comparison was of a grid against the distribution it was built from, and $p = 1$ was the tell. Replaced with the exact quantile identity, which is a stronger claim honestly obtained. Recorded because a $p$-value of exactly $1$ should always be read as a broken check rather than a strong one.

### 27.8 What it buys

- **The display is corrected**: dial, not semicircle, with no fake cut at the horizon. §26's forcing argument survives intact — it always forced a *closed* curve; only the drawing was wrong.
- **$2/\pi$ gets a geometric identity** (chord over arc, home to horizon) **and an operational one** (reach per register). It had neither.
- **$K = \pi\rho_0$ is derived** from the dial's circumference, retiring a contested assertion that had already needed one repair.
- **The held pair becomes metric**: $v$ is a chord, $\theta$ is an arc, on one figure.
- **The horizon's infinity is localised to the chart**, which is the sharpest available statement of why the framework refuses division.

`[clean, verified; corrects §26.2's picture and §27.3's first check. The quantile identity and cot expansion are elementary — the corpus's contribution is the dial as the forced display, the chord/arc reading of 2/π, and the derivation of K = πρ₀ from the circumference]`

---

## 28. You do not observe a line or a circle. You observe one density at the tangent point.

*"I wonder if we can say something stronger — you don't observe a line, or a circle. Maybe something like you observe their density at the tangent line, 0 angle."*

The claim holds. It also narrows §25's headline a third time; §28.8 states what remains.

### 28.1 The read line *is* the tangent line at home

Not "is modelled by." Put the hold circle's centre at $O$ and home at $H$, and take the tangent line at $H$. An element of $\mathbb{RP}^1$ is a *line* through $O$, and every such line meets the tangent line exactly once. That intersection is the read:

| central angle $\theta$ | gnomonic coordinate | $\tan\theta$ | difference |
|---|---|---|---|
| $0.3$ | $0.309336250$ | $0.309336250$ | $0$ |
| $1.0$ | $1.557407725$ | $1.557407725$ | $2.2\times10^{-16}$ |
| $1.4$ | $5.797883715$ | $5.797883715$ | $8.9\times10^{-16}$ |
| $1.5707$ | $10381.327417570$ | $10381.327417570$ | $0$ |

The tangent function is not a change of variable the corpus chose; it is central projection onto the tangent line at home. And the horizon acquires its correct description: **the unique line through $O$ parallel to the tangent line.** It is not far away and it is not an edge. It is the one direction that never meets the chart.

### 28.2 The whole geometry is one number

Invariance forces $\rho(s) = \rho_0/(1+s^2)$ (§25.8), and $\rho_0$ fixes the only free scale. So the observer's **complete geometric state is a single scalar measured at a single point** — the density at the tangent point. Everything else is the unique invariant extension of it:

$$\rho(s) = \frac{\rho_0}{1+s^2}, \qquad \text{total} = \pi\rho_0, \qquad K = \pi\rho_0, \qquad s_{\max} \to 2\rho_0 .$$

It is invariance and not $\rho_0$ that does the extending, which is worth exhibiting rather than asserting: the densities $(1+s^2)^{-0.9}$ and $(1+s^2)^{-1.1}$ both equal $1$ at home and both **move** under the elliptic flow (density at home $0.274 \to 0.313$ and $0.364 \to 0.318$), while $(1+s^2)^{-1}$ stays put ($0.322 \to 0.321$). One measurement plus one symmetry; nothing else is needed and nothing else is available.

**So the answer to the question is yes.** You do not observe a line — you cannot, it has a point you never reach. You do not observe a circle — you cannot, it needs a dimension you do not have. You observe a density where your chart touches, and the line and the circle are what an outside describer builds from it.

### 28.3 The measure is the tally

$$\text{total measure} = \pi\rho_0 = K.$$

At $\rho_0 = 63661.977$: total $= 199999.9993$, $K = 200000$. **The total measure of the read line is the atom count.** Not proportional to — equal to. That is §13.4a's "quantization is a horizon tally" arriving from measure theory: the measure was never a weighting laid over the atoms, it *is* the atoms, counted.

### 28.4 Reach by doubling: $\pi$ cancels

$$s_{\max} = \cot\!\frac{1}{2\rho_0} \;\longrightarrow\; 2\rho_0 .$$

| $\rho_0$ | $K = \pi\rho_0$ | $\cot(1/2\rho_0)$ | $2\rho_0$ |
|---|---|---|---|
| $4$ | $12.566$ | $7.958290$ | $8$ |
| $32$ | $100.531$ | $63.994792$ | $64$ |
| $512$ | $1608.495$ | $1023.999674$ | $1024$ |
| $10^5$ | $314159.265$ | $199999.999998$ | $200000$ |

$\pi$ cancels exactly. **Reach is twice the density at home**, and the observer obtains it by doubling — no $\pi$, no division. §20 established that the observer halves and never divides; this is the same operation run the other way, and it is the only arithmetic the observer needs to know how far it can see.

### 28.5 The $\pi$ audit, and what it settles

| quantity | value | needs $\pi$? |
|---|---|---|
| density at read $s$ | $\rho_0/(1+s^2)$ | **no** |
| reach | $2\rho_0$ | **no** |
| resolution ratio, home to $s$ | $1+s^2$ | **no** |
| atom spacing in reads | $(1/\rho_0)(1+s^2)$ | **no** |
| total measure of the line | $\pi\rho_0$ | yes |
| atom count $K$ | $\pi\rho_0$ | yes |
| dial circumference | $\pi$ | yes |
| home-to-horizon arc | $\pi/2$ | yes |

**Every operational quantity is $\pi$-free. $\pi$ appears only in totals — and a total is precisely what a bounded observer cannot take.** So

> $\pi$ is the outside describer's constant, not the observer's.

This resolves a discomfort that has run through §18–§27 without being named: the corpus kept needing $\pi$ while forbidding the operations that would produce it. §20 answered *how the value could be acquired*; the real answer is that **the observer does not need it at all.** It needs $\rho_0$, which it measures, and doubling, which it can do. $\pi$ is what an unbounded describer computes when it insists on integrating over a domain the observer never traverses.

### 28.6 Home is not a place

Measuring the density at $s_0$ rather than $0$ gives the same structure recentred: an observer standing at $s_0$ measures $\rho_0$ in its own units and calls that point home. From the outside, $\rho(1) = 0.5$ and $\rho(3) = 0.1$ relative to a describer's chart; from the inside, each is $1$. Nothing distinguishes the corpus's $0$ except that it is where the observer happens to stand — which is §25.8's result that the location-scale family of Cauchys is the set of points of $H^2$, now read as a statement about *standpoints* rather than parameters. **"Home" is a synonym for "where the measurement is taken."**

### 28.7 The honest tension, and why it vindicates the pair

There is a real conflict between §27's display and §28.1's, and it should be recorded rather than smoothed.

The measure-faithful closed dial has radius $\tfrac12$ (arc length $=$ measure, no cut). Its central projection onto the tangent line is $r\tan(2\theta)$, and

$$u \;=\; \tfrac12\tan 2\theta \;=\; \frac{s}{1-s^2} \;\ne\; s,$$

confirmed at $\theta = 0.2, 0.5, 1.0$ ($u = 0.211397, 0.778704, -1.092520$). That is the **double-angle map**, not the read. So:

- the **semicircle** display gets the projection right ($s = \tan\theta$) and shows a false cut at the horizon;
- the **closed dial** has no cut and doubles the angle.

You cannot have both in one drawing, and the discrepancy is exactly the deck factor $2$ — §5's two-stage quotient, appearing as a defect of *drawing* rather than of algebra.

This is not a problem for the framework; it is the framework's own claim, arriving as a constraint on pictures. **No single display is complete, which is why the observer holds a pair rather than a picture.** What survives every chart is the density at the tangent point, and that is precisely what §28.2 says the observation is.

### 28.8 What it buys, and the third narrowing

- **The observation is identified**: one scalar at one point, not a line and not a circle. The strongest and simplest statement of the framework's content in the paper.
- **The tangent function stops being a convention** — it is central projection, and the horizon is the parallel direction.
- **Measure $=$ tally**, exactly, joining §4's measure to §13.4a's counting.
- **Reach $= 2\rho_0$**, $\pi$-free, obtained by doubling.
- **The $\pi$ discomfort is dissolved**, not managed: $\pi$ is never in the observer's hands.
- **A display constraint is found** that the corpus's own two-stage quotient predicts.

And the narrowing, stated plainly because the arc has now done it three times. §25: *$\pi$ is the price of the extra dimension.* §25.8: no — $\pi$ is not created by the extra dimension, it is already the total mass of the 1D line. §28: and the total mass is exactly what the observer never takes. What survives of the original claim is one sentence: **$2/\pi$ is a projection toll and the observer can acquire it; $\pi$ itself is a total, and totals belong to describers.** That is a good deal smaller than the section that started the arc, and it is the part that is true.

`[clean, verified; the gnomonic identification and the cot expansion are elementary. The corpus's contributions are the one-scalar characterisation of the observational state, measure = tally, reach = 2ρ₀ with π cancelling, the π-audit table, and the display constraint at §28.7. §28.3's numbers and §28.4's are exact identities; §28.2's non-invariance demonstration is Monte-Carlo and is graded as a demonstration, not a precision check.]`

---

## 29. Answering by asking: how do you observe anything at all?

§28 said the observation *is* one density at the tangent point. It did not say how the density gets read. So ask the prior question — **how do you observe something at all? What are your options?** — and the useful thing is that this question has a complete answer, not a suggestive one.

### 29.1 Posing it so it can be answered

An observer has a held pair. The thing has a held pair. The observer has no absolute frame, so whatever it reads must be unchanged by rotating observer and thing together. That makes the question precise:

> **What are the rotation-invariant functions of two held pairs?**

Classical invariant theory answers exhaustively. The generators are

$$|a|^2, \quad |b|^2, \quad a\cdot b, \quad \det(a,b),$$

and the count is tight: two vectors in $\mathbb{R}^2$ is four numbers, $SO(2)$ is one-dimensional, so there are exactly $4 - 1 = 3$ independent invariants — four generators with one relation. Confirmed structurally: two configurations with identical invariants are related by a rotation (max invariant difference $8.9\times10^{-16}$ across three random rotations). **Nothing else is observable.** Any further "read" is a function of these four.

So the answer to the question is a list, and the list is short:

| verb | invariant | what it returns |
|---|---|---|
| **hold** | $\lvert a\rvert^2$ | your own budget — a self-read, not an observation |
| **project** | $a\cdot b$ | the overlap; maximal at alignment |
| **compare** | $\det(a,b)$ | the side; **zero** at alignment |
| **count** | iterate either | an integer of unbounded range |

**Three verbs for observing something other than yourself, and provably no fourth.**

### 29.2 The two single acts are bound, and the binding is Born

$$\det(a,b)^2 + (a\cdot b)^2 = |a|^2|b|^2,$$

residual $4.3\times10^{-14}$ over $2\times10^5$ random pairs. The options are not independent. Normalising, $p = \cos\Delta$ and $c = \sin\Delta$ with $p^2 + c^2 = 1$ — and this is §13.4b's $\det^2 = $ Born arriving as a statement about *observational method*: **the relation between the two ways of observing is the Born rule.** You cannot improve your projection without losing your comparison, because there is one relation and it is Pythagorean.

### 29.3 Each read is blind exactly where the other is sharp

| misalignment $\Delta$ | $p = \cos\Delta$ | $c = \sin\Delta$ | $\lvert dp/d\Delta\rvert$ | $\lvert dc/d\Delta\rvert$ |
|---|---|---|---|---|
| $0$ | $1.000000$ | $0.000000$ | $0.000000$ | $1.000000$ |
| $0.01$ | $0.999950$ | $0.010000$ | $0.010000$ | $0.999950$ |
| $\pi/4$ | $0.707107$ | $0.707107$ | $0.707107$ | $0.707107$ |
| $\pi/2$ | $0.000000$ | $1.000000$ | $1.000000$ | $0.000000$ |

The sensitivity of each read is *the other read's value*. At alignment the projection is flat — it returns $1$ and tells you nothing about how nearly aligned you are — while the comparison is at maximum slope. At quadrature it reverses. They cross at $\pi/4$.

### 29.4 The null method is not a technique; it is the only option

The degeneracy near alignment is **square-root**, not proportional, and that is the sharp claim. Writing $p = \cos\Delta + \varepsilon \approx 1 - \Delta^2/2 + \varepsilon$, the inverted estimate is $\sqrt{\Delta^2 - 2\varepsilon}$, so for $\Delta \ll \sqrt{\sigma}$ the projection estimate is dominated by $\sqrt{\sigma}$ — while the comparison estimate stays linear in $\sigma$. Scanning $\sigma$ at $\Delta = 10^{-4}$:

| $\sigma$ | sd$(\Delta)$ via **project** | $\sqrt{2\sigma}$ prediction | sd$(\Delta)$ via **compare** | ratio |
|---|---|---|---|---|
| $10^{-2}$ | $0.067940735$ | $0.067655977$ | $0.009995680$ | $6.8$ |
| $10^{-4}$ | $0.006789277$ | $0.006765598$ | $0.000099921$ | $67.9$ |
| $10^{-6}$ | $0.000679995$ | $0.000676560$ | $0.000001000$ | $679.7$ |
| $10^{-8}$ | $0.000074755$ | $0.000067656$ | $0.000000010$ | $7479.9$ |

**The advantage of the null read grows as $1/\sqrt{\sigma}$, without bound.** The better your instrument, the more the null method wins — $7$-fold at $\sigma = 10^{-2}$, nearly $7500$-fold at $10^{-8}$. You drive to the balance and read **when** it balances, never **how much** it tilts.

> **Correction, entered at §32.** This paragraph continued: *"That is why every precision instrument in the history of measurement is a null instrument: the balance, the Wheatstone bridge, the interferometer at a dark fringe…"* — listing all of them as instances of one law. **They are not.** The $1/\sqrt\sigma$ law requires a read that is *quadratically flat* at the null, which the interferometer's dark fringe is ($\sin^2$) and the beam balance is **not** (its torque is linear in the pivot). Measured, the balance's null advantage is a flat $\approx 1.4$, and it vanishes entirely when the gain is known. Two kinds of null, one law claimed for both — a fourth weld, caught by §31.4's own test one section after that test was written. Separated at §32.2.

This is the balance-beam metaphor vindicated at exactly the right point, The beam is not a picture of addition; it is the assertion that the antisymmetric read is the sensitive one, and that assertion is quantitative.

### 29.5 The third verb is the only one that accumulates

Project and compare are single acts, each returning one bounded number. **Count** is different: iterate the comparison, consulting only $\operatorname{sign}(\det)$, and bisect.

| step | estimate | error |
|---|---|---|
| $5$ | $1.129009859883832$ | $2.9\times10^{-2}$ |
| $10$ | $1.099864224914004$ | $1.4\times10^{-4}$ |
| $20$ | $1.100000545472303$ | $5.5\times10^{-7}$ |
| $40$ | $1.099999999999582$ | $4.2\times10^{-13}$ |
| $60$ | $1.100000000000000$ | $0$ |

One bit per step, exactly, with no division, no magnitude, and no projection ever taken. **An unbounded-range number out of bounded registers, one bit at a time.** This is §20's halving, now seen as the third and only accumulating verb, and it is where §28's $\rho_0$ actually comes from: the density at home is a *count*, and §28.3's measure-is-tally says so.

### 29.6 And this is §12.3's triple, derived

The corpus has said since §12.3 that observation consumes **order, topology, metric**. The three verbs are those three, exactly:

- **compare** $\to$ $\operatorname{sign}(\det)$ $\to$ **order**
- **count** $\to$ accumulated signs, a winding $\to$ **topology**
- **project** $\to$ $|a\cdot b|$ $\to$ **metric**

§12.3 asserted the triple from analysis of the operation table. It is now the invariant-theoretic answer to "what are your options," which means the triple is not a taxonomy the corpus chose but the complete generator list of $SO(2)$-invariants of two pairs. Same three things, arrived at from representation theory instead of introspection.

### 29.7 Why hold a pair at all: the one bit

Fix $|a|^2$, $|b|^2$ and $a\cdot b$. Then $\det$ is determined **only up to sign** — a configuration and its mirror image agree on all three scalar invariants and differ in $\det$ by exactly a sign:

| scalars match | $\det$ | mirrored $\det$ | sum |
|---|---|---|---|
| yes | $+0.990683$ | $-0.990683$ | $0$ |
| yes | $+0.947645$ | $-0.947645$ | $0$ |
| yes | $-0.013625$ | $+0.013625$ | $-1.1\times10^{-16}$ |

So the mirror image is **invisible** to the norms and to the projection. Only the comparison sees it, and what it sees is a single bit: **an orientation bit**, the sign of $\det$, flipped by reflection.

> **Correction, entered at §31.** This sentence first read "the deck group $\{\pm1\}$ of §5's two-stage quotient." **They are different $\mathbb{Z}/2$ actions.** Negating one vector — the deck transformation of $S^1 \to \mathbb{RP}^1$ — flips *two* invariants, $a\cdot b$ **and** $\det$. Reflection flips $\det$ **only**. Verified side by side at §31.3. The argument needs only "an orientation bit" and is unharmed; the identification with §5 was decoration, and it was wrong.

**That one bit is the entire reason an observer must hold a pair instead of reading a ratio.** The ratio $s = v/h$ is a scalar; scalars cannot carry the sign of an orientation. Everything the corpus has built on refusing to divide — the horizon as an ordinary point, the deck factor $2$, the $\pi$ versus $2\pi$ split, spin-$\tfrac12$ at four registers — descends from this: dividing throws away the one bit that distinguishes a configuration from its mirror.

### 29.8 The answer, and two corrections recorded

**How do you observe anything at all?** You project, you compare, or you count — and there is no fourth option, because the invariants of two held pairs under rotation are exactly four with one relation. The two single acts are in quadrature and bound by Born, so each is blind where the other is sharp; the accumulating act is the only route from bounded registers to unbounded range; and the comparison alone carries the orientation bit that makes holding a pair necessary.

Corrections from this section's own first pass, both caught by their numbers looking wrong:

- I first wrote that the comparison is "$\sim1000\times$ more precise near alignment" from a single $\sigma = 10^{-3}$ run showing $21\times$. The fixed-factor framing was wrong *and* weaker than the truth: the degeneracy is square-root, so the ratio scales as $1/\sqrt{\sigma}$ and has no fixed value. Scanning $\sigma$ replaced a wrong constant with a law.
- The bisection demo first used target $\pi/4$, which the first midpoint hits exactly, producing "error $0$ at step 1" — an accident that read as instant convergence. Re-run at a non-dyadic target.

### 29.9 What it buys

- **An exhaustiveness result** where the paper previously had a list: three verbs, provably no fourth.
- **§12.3's triple derived** from invariant theory rather than asserted from the operation table.
- **The null-method law**: advantage $\propto 1/\sqrt{\sigma}$ for quadratically flat reads (restricted at §32.2). It bears on the prevalence of null instruments in metrology.
- **Born as a statement about method**, not just about amplitudes: the two ways of observing are Pythagorean complements.
- **The reason to hold a pair, in one bit.** Not an aesthetic preference and not a computational convenience: division discards orientation, and orientation is one of the four invariants.

`[clean, verified; the invariant-theory generators and the null-method advantage are classical (the first is textbook, the second folklore in metrology without this derivation). The corpus's contributions are the identification of the generator list with §12.3's triple, the square-root scaling law as the reason nulls dominate, and the orientation bit as the necessity argument for holding a pair.]`

---

## 30. The Socratic opening: what it earns, and the two steps that would be killed

A reader proposed shifting the burden: instead of defending the held pair, ask *how else could observation possibly work?* — and walk the reader down an elimination ladder.

> How do you observe anything? You either observe the whole or you do not. If you observe the whole, observation is complete. If you do not, what can you know? Only relationships. How many things does a relationship require? Two. What is the simplest relationship? One quantity held against another.

**This is the right opening and it should be used.** §29 proves that the observational options are exhaustive, but a proof is not an entrance; the ladder is the entrance, and it arrives at the pair without ever asserting it. Two of its steps, though, are the ones a mathematician kills first, and one of them is the step the ladder is proudest of. Both are repairable, and the repairs are stronger than the originals.

### 30.1 The step that gets killed: "a single number is meaningless"

*"Five. Five what? Every measurement already contains an implicit reference."* Rhetorically the best line in the ladder. As stated, false — and the counterexamples are the first thing anyone reaches for:

- **Counts.** Five sheep is five. Compared to what? Nothing; it is a cardinality.
- **Dimensionless numbers.** $\alpha \approx 1/137$, a Reynolds number, an angle in radians. All reference-free by construction.

A referee raises this in one sentence and the opening is gone. So it has to be repaired before it is deployed.

### 30.2 The repair: an apparent single number is a pair with $h$ suppressed

There are exactly two ways to suppress the second slot, and neither is arbitrary.

**(i) $h = 1$ — the reference is the observer's own atom.** And $h = 1$ is not a choice of unit. In the unit hold $h = \cos\theta$, so

$$h = 1 \iff \theta = 0 \iff \textbf{home}.$$

At home, and only at home, the read equals the numerator: $s = v/h = v$ at $\theta = 0$, and $s \ne v$ at $\theta = 0.3$ ($0.309336$ vs $0.295520$) and $\theta = 1.0$ ($1.557408$ vs $0.841471$). **That is why the reference is invisible in a count: the reference is the observer itself.** "Five" means *five of my atoms*, and the hidden reference is the standpoint — §28.6's result that home is not a place but where the measurement is taken.

The suppressed reference even has a size. Atom spacing in read units at home is $1/\rho_0$, confirmed at three scales ($0.000015708$ against $1/\rho_0 = 0.000015708$ at $\rho_0 = 63661.977$). A count of $n$ reads $n/\rho_0$; reporting "$n$" suppresses $\rho_0$. **The reference is not absent, it is the observer's own resolution** — which is exactly §28.2's one scalar. The claim survives, and in a better form: not *every number hides a unit*, but *every count is denominated in the observer's own atom, and that atom is $1/\rho_0$*.

**(ii) $h$ cancels** — both slots physical and alike, a true ratio. $\alpha$ and Reynolds numbers are here. These are pairs whose slots divided out, which is precisely the operation the framework declines; the number that survives is the one an unbounded describer computed.

### 30.3 The better argument, which does not need "five what?" at all

Here is the version immune to the counts objection, and it was available in §29 all along.

**No single number — count, ratio, or dimensionless constant — distinguishes a configuration from its mirror image.** Across four random configurations and their mirrors:

| $\lvert a\rvert$ | $\lvert b\rvert$ | $a\cdot b$ | normalised ratio | integer count | $\det$ |
|---|---|---|---|---|---|
| $0.778052$ | $0.434176$ | $-0.252170$ | $-0.746481$ | $4$ | $-0.224782$ |
| $0.778052$ | $0.434176$ | $-0.252170$ | $-0.746481$ | $4$ | $\mathbf{+0.224782}$ |
| $2.608350$ | $1.540090$ | $3.127561$ | $0.778563$ | $15$ | $+2.520991$ |
| $2.608350$ | $1.540090$ | $3.127561$ | $0.778563$ | $15$ | $\mathbf{-2.520991}$ |

Every scalar report is identical across the mirror. Only $\det$ flips. So:

> **A single number is insufficient not because it lacks a unit, but because it cannot carry an orientation.**

That argument holds for counts too — counts are mirror-blind. It does not depend on any claim about dimensions, units, or implicit references. And it is the same fact as §29.7's orientation bit, which means the ladder and the invariant-theory proof converge on one sentence instead of two arguments. *(Not the deck bit of §5 — see §31.3.)*

### 30.4 The other step to relabel: "observe the whole or observe a part"

The reader who proposed the ladder already flagged this and recommended posing it as a question rather than a dichotomy. Correct, and the reason is worth being precise about: **the "whole" branch is not eliminated by argument. It is excluded by the premise set.**

To hold the whole you need $K \ge$ the information in the whole. A target needing $64$ bits requires $K \ge 10^{19.3}$; one needing $1000$ bits requires $K \ge 10^{301}$; a continuum requires unbounded $K$. So the honest split is not *whole or part* — it is **part, or nothing**, and that is a restatement of P1–P5 rather than a theorem proved without them.

Saying so plainly is **stronger**, not weaker. A soft dichotomy invites the reply "why can't I observe the whole?" A claim about $K$ answers it: you may, if you have $10^{301}$ registers, and the framework is about observers who do not. The ladder should therefore open with the premise visible, not concealed — the elimination is *conditional on boundedness*, and boundedness is the thesis, not a hidden step.

### 30.5 And a limit on what the ladder can deliver

The ladder concludes "one quantity held against another." §29.7 concludes something narrower and harder: **that the held object must retain the orientation bit that a quotient destroys.** Those are not the same claim, and the second is the load-bearing one.

"A relationship needs two things" is compatible with holding a comparison *outcome* — a single bit — rather than a pair. It is compatible with holding an equivalence class. It does not by itself force two retained magnitudes. What forces that is the mirror argument, and the mirror argument is not rhetorical.

So the division of labour should be explicit in any extraction: **the ladder motivates the pair; §29 proves it.** If the ladder is allowed to stand in for the proof, a careful reader will notice that it stops one step short and will assume the framework does too.

### 30.6 What it buys

- **An entrance.** The paper has never had one that reaches the pair without asserting it. This is worth real money in the extraction programme, where §29's invariant theory is a poor first page.
- **The strongest philosophical line, repaired into a result**: $h = 1$ is home, so a count is denominated in the observer's own atom of size $1/\rho_0$. That is checkable and it was not previously stated.
- **A mirror argument that beats the units argument** on its own ground — immune to the counts objection, and identical to §29.7's deck bit.
- **A premise made visible** where it was being smuggled: the two-option split is P1–P5 restated, and admitting that converts a soft dichotomy into a quantitative claim about $K$.
- **A boundary on the rhetoric**, so it does not get mistaken for the proof.

Graded as **exposition with two repairs**, not as a result. The ladder earns no number; the repairs at §30.2 and §30.3 do.

### 30.7 Where it was deployed

Decided and executed: **not the abstract; the introduction's first paragraph.** An abstract has no room for §30.2's and §30.4's repairs to travel with the ladder, and an unrepaired ladder is the sentence a referee quotes when rejecting. The introduction has room, and the repairs are now carried in it — the premise named as a $K$-claim ($10^{19.3}$ at 64 bits, $10^{301}$ at 1000), the motivation labelled as motivation, the mirror argument given as the thing that actually forces the pair, and the counts-and-dimensionless objection pre-empted with the $h = 1 \iff$ home repair.

The abstract got a **one-clause change instead**, at no cost in length. It read:

> …the quotient $v/h$ is *derived*, never the primitive, because **dividing discards the pair the interaction delivered**.

which is circular — discarding the pair is what dividing *is*, so the clause proves nothing. Now:

> …because **dividing discards the orientation bit** — one of the four invariants a held pair carries under rotation, and the only one no single number can express.

Same position, same length, tautology to theorem. Recorded: the clause was in the abstract unchanged since it was written.

`[clean; §30.1 and §30.4 are corrections to a proposed argument, not to the corpus. §30.2's h = 1 ⟺ home and the 1/ρ₀ spacing are verified. §30.3's mirror table is the same fact as §29.7 applied to a different objection. The ladder itself is rhetoric and is labelled as such.]`

---

## 31. The audit of §§1–24, and three errors it found

§§25–30 were written in one sustained run against a paper whose first twenty-four sections predate them. An adversarial audit was run over the whole file — the first one this paper has had. It found three genuine mathematical errors, all in the *new* material, all shipped. They are recorded here in full.

### 31.1 Error 1: two different composition laws, welded

§25.5 wrote: *"§1's 'weights add, comparisons don't' and §9's velocity addition are the same statement."* False, and refutable from within the same section.

$$\text{§1, the balance: } \frac{x+y}{1+xy} \qquad\text{vs.}\qquad \text{§25.5, the reads: } \frac{x+y}{1-xy}$$

At $x = 0.3$, $y = 0.5$: $0.695652174$ against $0.941176471$. The first is conjugated to $(\mathbb{R},+)$ by $\operatorname{artanh}$ — the **hyperbolic** subgroup, fixed points at $b = \pm1$, non-compact. The second by $\arctan$ — the **elliptic** subgroup, no real fixed point, compact. These are two of §9.5's three conjugacy classes, and they are not the same one.

Worse, §25.8 had already refuted the weld with its own numbers: *"under the hyperbolic flow $0.996 \to 148 \to 4.8\times10^{8}$. Mass escapes to the fixed point… exactly one preserves a probability measure."* The subgroup §25.8 rejects **is** §1's chaining law, and the fixed point the mass escapes to **is** §3's horizon. The paper simultaneously claimed that §1's law is the read line's group law and that §1's law cannot carry the read line's measure.

The repair, which §26.4 already contained without noticing: The two reads live on different parts of one object:

- the **balance read** $b = \tanh\varphi$ is a coordinate *along a geodesic of $H^2$* — the interior, the standpoint space. Rapidity is hyperbolic arc length: at $\varphi = 0.5, 1.0, 2.0$ the geodesic length is $0.500000000, 1.000000000, 2.000000000$ exactly.
- the **slope read** $s = v/h$ is a coordinate *on $\partial H^2 = \mathbb{RP}^1$* — the boundary, which carries the Cauchy.

Chaining ratios acts by the hyperbolic subgroup; the measure is preserved by the elliptic one. Both are $PGL(2,\mathbb{R})$; neither is the other. And §3's horizon gains a geometric account it did not have: $b = \pm1$ are the geodesic's two **ideal endpoints**, at infinite hyperbolic distance, which is exactly why no finite loading of a pan reaches them. §3's *"reachable only by emptying a register, never by loading one"* stops being an observation about arithmetic and becomes a statement about $H^2$.

### 31.2 Error 2: a factor of two in the fare contract

§27.4 derived $K = \pi\rho_0$ by spreading $K$ atoms over a dial of circumference $\pi$ — and billed it as retiring a contested assertion. But the whole dial is $s \in [-\infty,\infty]$, and **the corpus's atom is stated with $v, h \ge 0$**, so $s \in [0,\infty]$: half the dial, arc $\pi/2$, measure $\int_0^\infty ds/(1+s^2) = 1.570796327$.

$$\boxed{K = \tfrac{\pi}{2}\,\rho_0 \quad\text{(the atom, } v,h \ge 0)} \qquad\qquad K = \pi\rho_0 \quad\text{(signed reads)}$$

§27.3's quantile identity has the same tell: $F(s_j) = \tfrac12 + \arctan s_j/\pi$ is the **two-sided** Cauchy CDF. It is correct for signed reads and is not the atom's.

**What moves and what does not.** The totals move by two: $K$, the total measure, and §28.3's measure-is-tally. **The densities do not**, because atom spacing at home is $1/\rho_0$ under either domain — half the atoms over half the arc. So §28.4's reach survives untouched, which matters because it is the arc's best result: at $\rho_0 = 32, 512, 10^5$ the measured $s_{\max}$ on the half dial is $63.6567$, $1023.6843$, $200000.4677$ against $2\rho_0 = 64$, $1024$, $200000$. **Reach $= 2\rho_0$ regardless of domain.** The $\pi$-audit at §28.5 also survives in full, and is in fact reinforced: the quantity that moved is a *total*, and totals were already identified as the describer's.

One live question this raises rather than settles: §9.2's fare contract states $K_{\max} = \pi\rho_0$, which matches the **signed** line, not the atom §1 defines. Either §9.2 implicitly uses signed reads or it carries the same factor of two. That is a corpus question, not a balance.md question, and it is now on the open list.

### 31.3 Error 3: the orientation bit is not the deck bit

§29.7 wrote that the sign of $\det$ is *"the deck group $\{\pm1\}$ of §5's two-stage quotient."* It is not. Run both actions on the invariant ring:

| action | $\lvert a\rvert^2$ | $\lvert b\rvert^2$ | $a\cdot b$ | $\det$ |
|---|---|---|---|---|
| identity | $0.72811$ | $1.80233$ | $-0.86866$ | $+0.74681$ |
| **deck** ($a \mapsto -a$) | $0.72811$ | $1.80233$ | $\mathbf{+0.86866}$ | $\mathbf{-0.74681}$ |
| **mirror** (reflect) | $0.72811$ | $1.80233$ | $-0.86866$ | $\mathbf{-0.74681}$ |

The deck transformation flips **two** invariants; reflection flips **one**. Both are $\mathbb{Z}/2$; they are not the same $\mathbb{Z}/2$, and they guard against different losses — the deck bit is lost by *dividing a pair*, the orientation bit by *reducing two pairs to scalars*. Two reasons to keep structure, at two different stages, and the paper collapsed them.

The argument is unharmed: §29.7 needs only "an orientation bit," and the mirror table already proved what it needed. The identification with §5 was decoration. **But it had already travelled** — into §30.3, and into the corpus's new §1 opening paragraph, where it was written as "the bit that separates $\mathbb{RP}^1$ from its double cover." That sentence is now wrong in a shipped introduction, and correcting it is the most urgent item this audit produced.

### 31.4 What the audit says about the method

The three errors share one shape: **each is a weld.** Two composition laws welded because both are Möbius; two $\mathbb{Z}/2$'s welded because both are $\pm1$; a domain silently widened because $\pi$ is prettier than $\pi/2$. The generative habit of this arc — noticing that two things are the same object — is exactly the habit that produced them.

That is worth stating plainly, because the discipline this paper runs on is *an identification earns its place only if it does work*, and all three failed welds **did** do work. They connected sections, they explained things, they read well. Doing work is necessary and it is not sufficient. The missing test is cheaper than the one being applied: **before welding two things, compute both and check they are equal.** Three lines of arithmetic would have caught all three, and none of the three was checked because each felt like a restatement rather than a claim.

The audit also found roughly twenty hygiene items — script label collisions, cited checks that do not exist ($R3$–$R5$, $E2$, $E5$, $V5$ are cited and absent), one integral banked three times as independent corroboration, and six sections each described as "the strongest in the paper." Not errors of substance; the superlatives are removed at §35.8.

`[clean; §31 is a record of corrections, not a result. The H^2 geodesic identification at §31.1 is the one piece of new mathematics, and it repairs §3. Verification: audit_verify.py, A1–A4.]`

---

## 32. Equilibrium: what settles, and the fourth weld

A reader proposed reframing the whole act: **Hold → Balance → Read**, not Hold → Compute → Read. *"The observer doesn't manufacture the read; the read is the stable point that remains after the held relation has balanced itself."* With a caution attached — don't say observation *is* a centre of gravity, since that term has a precise definition; say it *behaves like* an equilibrium problem.

The caution is aimed at the wrong danger. The real problem is sharper, and fixing it makes the claim stronger than the hedge would have.

### 32.1 The centre of gravity is a division — and the balance never performs it

$$x^* = \frac{\sum_i m_i x_i}{\sum_i m_i}.$$

That is a quotient. Taken literally, "observation is a centre of gravity" imports precisely the operation this framework refuses. The hedge "behaves like" does not fix this; it only makes it vaguer.

What fixes it is that **the balance does not compute that formula.** It finds where the torque vanishes:

$$\sum_i m_i (x_i - x^*) = 0,$$

a null, not a quotient. Bisecting on the sign of the torque and nothing else:

| step | null at | $\lvert$ null $-\ \sum mx/\sum m\rvert$ |
|---|---|---|
| $10$ | $1.935407278106086$ | $7.6\times10^{-4}$ |
| $20$ | $1.934650890900848$ | $7.1\times10^{-7}$ |
| $40$ | $1.934651605567598$ | $3.1\times10^{-12}$ |
| $60$ | $1.934651605570667$ | $0$ |

Identical to the describer's formula, and no division was performed at any step. **The division is the name, not the act.**

This is §28.5's $\pi$-audit repeating for a second, unrelated quantity — the operational form is division-free, the closed form carries the divide — and two independent instances make it look like a general feature rather than a fact about $\pi$. The content of the equilibrium framing is therefore: settling is what a division-free system can perform, and the quotient is what a describer writes afterwards.

### 32.2 The fourth weld: two kinds of null

Testing the reframe immediately broke something I wrote one section earlier. §29.4 claimed the $1/\sqrt\sigma$ null advantage and then listed the balance, the Wheatstone bridge and the dark fringe as instances of it. Measuring the balance:

| $\sigma$ | tilt, gain unknown | tilt, gain **known** | null | ratio vs known |
|---|---|---|---|---|
| $10^{-2}$ | $0.0012500815$ | $0.0011194816$ | $0.0007709027$ | $1.45$ |
| $10^{-4}$ | $0.0000133475$ | $0.0000117811$ | $0.0000080909$ | $1.46$ |
| $10^{-6}$ | $0.0000001245$ | $0.0000001114$ | $0.0000000826$ | $1.35$ |

Flat. No growth. And with the gain known the tilt read essentially matches the null. So for the balance the null's advantage is **not sensitivity at all** — it is that the null needs no gain calibration.

The reason is structural. The balance's torque is $T(p) = M(x^* - p)$ — **linear** in the pivot, so inverting it costs one division and suffers no degeneracy. §29.4's law needed a read that is **quadratically flat** at the null. Two families:

| instrument | read near the null | order | advantage |
|---|---|---|---|
| beam balance | $T = M(x^*-p)$ | **linear** | constant; the win is "no gain needed" |
| Wheatstone bridge | $V \sim \delta R$ | **linear** | constant; same source |
| angle alignment | $\cos\Delta \approx 1 - \Delta^2/2$ | **quadratic** | $1/\sqrt\sigma$, unbounded |
| interferometer, dark fringe | $\sin^2(\Delta/2) \approx \Delta^2/4$ | **quadratic** | $1/\sqrt\sigma$, unbounded |

The quadratic family does behave as §29.4 said — dark-fringe ratios $9.6 \to 95.7 \to 962.4 \to 10212.4$ over four decades. The linear family does not, and the beam balance, the paper's own central image, is in the linear family.

**This is a fourth weld**, of exactly the shape §31.4 had just finished naming: two things called one law because both are nulls. It was caught one section after the test that catches it was written down, which is the most useful thing that could have happened to that test.

What survives of §29.4 is the correct and narrower claim: the antisymmetric read is the sensitive one, its advantage over the symmetric read is unbounded **when the symmetric read is flat at the null**, and where it is not flat the null still wins for a different and more mundane reason — it does not need the instrument's gain.

### 32.3 Hold → Balance → Read is right for one verb of three

§29 established three verbs. Only one of them settles:

| verb | invariant | a settling? | acts |
|---|---|---|---|
| project | $a\cdot b$ | **no** — one inner product | $1$ |
| compare | $\det(a,b)$ | **no** — one sign | $1$ |
| count | iterate compare | **yes** — drives to a null | $n$ |

So "observation is settling" is true of the null read and false of the projection read, and the honest version is narrower and stronger: **settling is what observation converges to under pressure, not what it is by definition.** The projection read exists, is a single act, and computes nothing iteratively. It is simply the worse instrument near a null — which is why anything trying to be precise ends up settling.

### 32.4 "Distributed hold, localised read" — already proved, under another name

The observation that a beam integrates many forces while the observer reads one pointer is correct, checkable, and the corpus already owns it. Distributions of $N = 2, 7, 50, 5000$ masses, deliberately built with wildly different spreads ($2.2$ to $20.2$) and skews ($0$ to $-1318$), all giving:

$$\text{read} = 1.100000000000 \quad\text{in every case.}$$

$N$ masses in, one number out; every other feature of the distribution is invisible to the beam. The compression is not the observer's doing — the equilibrium performed it before the observer arrived.

But this is §14's result. *Free reads are boundary reads*: a boundary functional summarises a distributed interior at a point, $N$-independently, and §14 earned that with its own table. The equilibrium framing is a better *image* for it and not a new claim, and it should be labelled that way.

### 32.5 "Emergent coordinate" — the precise word is *quotient*

The read is not one of the held quantities, correct. But "emergent" is doing work that a sharper word does better: the hold lives in the **total space** and the read on the **quotient** of it. That is §5's two-stage quotient, and it is exactly why the beam's read is a *position* while the held quantities are *masses* — a difference of type, not merely of value.

$$\text{hold } (3,4) \in \mathbb{R}^2\!\setminus\!0, \qquad \text{read } 0.75 \in \mathbb{RP}^1, \qquad (\lambda\cdot 3, \lambda\cdot 4) \mapsto 0.75 \ \ \forall \lambda.$$

"Emergent coordinate" means "coordinate on the quotient." The corpus has had it since §5, and using the precise word costs nothing and forecloses an objection.

### 32.6 What it buys

- **A second instance of the $\pi$-audit's structure**, on a quantity with no $\pi$ in it: the centre of gravity is a division the balance never performs. Two independent instances make "operational forms are division-free; closed forms carry the divide" look like a general feature of this framework rather than a fact about $\pi$.
- **A fourth weld caught**, and caught by the test written one section earlier — which is the first evidence that §31.4's discipline actually fires.
- **§29.4 correctly narrowed**: linear nulls and quadratic nulls are different, the $1/\sqrt\sigma$ law belongs only to the quadratic family, and the beam balance — this paper's own image — is linear.
- **Three imprecise words replaced** by ones already in the corpus: *settling* scoped to one verb of three, *distributed-to-localised* identified as §14's boundary read, *emergent* identified as *quotient*.

`[clean; §32.1's identity and §32.4's invariance are exact. §32.2 is a correction to §29.4. The equilibrium framing is a reader's, is graded as an image, and its value is that testing it broke something.]`

---

## 33. The factor of two is not the deck group

A reader reconstructed §27.4's derivation and supplied a mechanism for the $2$ in $s_{\max} = 2\rho_0$: *"The factor of 2 is the two-to-one deck cover: the two home-and-horizon chart quadrants ($2 \times \pi/2$) spanning the total range from $0$ to $\infty$."* The claim is falsifiable, and it is false. It is also the **fifth weld** of this arc, arrived at independently — which is the more useful finding.

### 33.1 Two prior points

The derivation quoted is the **signed-line** version, corrected at §31.2: $K = \pi\rho_0$ spreads $K$ over the whole dial, while §1's atom has $v, h \ge 0$ and gives $K = (\pi/2)\rho_0$.

And the proposed patch is the error restated. $[0,\infty]$ is **one** quadrant of dial arc, of length $1.570796327$ — not two. The "$2 \times \pi/2$" that recovers $\pi$ is the widened domain, wearing the deck group as a justification.

### 33.2 The decisive test

A deck group is a topological fact about the covering $S^1 \to \mathbb{RP}^1$. It cannot depend on how the atoms are spaced. So hold everything fixed and vary **only** the grid offset. At $K = 4096$:

| grid convention | last atom $\theta$ | $s_{\max}$ | $s_{\max}/\rho_0$ |
|---|---|---|---|
| midpoint, $(j+\tfrac12)\pi/K$ | $1.570412832$ | $2607.5945$ | $\mathbf{2.000000}$ |
| left-aligned, $j\pi/K$ | $1.570029336$ | $1303.7970$ | $\mathbf{1.000000}$ |
| quarter-offset, $(j+\tfrac14)\pi/K$ | $1.570221084$ | $1738.3962$ | $\mathbf{1.333333}$ |
| eighth-offset, $(j+\tfrac18)\pi/K$ | $1.570125210$ | $1490.0538$ | $\mathbf{1.142857}$ |

**The coefficient moves.** A covering degree cannot. The law is elementary: the last atom sits $(1-\text{off})$ of a spacing from the horizon, so

$$\frac{s_{\max}}{\rho_0} = \frac{1}{1-\text{off}} \qquad (2, \ 1, \ \tfrac43, \ \tfrac87 \text{ at off} = \tfrac12, 0, \tfrac14, \tfrac18).$$

The $2$ is the reciprocal of a **half-cell at the end of a grid**. It has nothing to do with a covering map.

### 33.3 But the midpoint convention *is* forced — by measure, not topology

This is what rescues the result rather than the explanation. Among all offsets, only the midpoint gives every atom an equal share of the measure. Cell measures at $K = 8$:

| convention | min cell | max cell | ratio |
|---|---|---|---|
| **midpoint** | $0.392699$ | $0.392699$ | $\mathbf{1.000}$ |
| left-aligned | $0.196350$ | $0.589049$ | $3.000$ |
| quarter | $0.294524$ | $0.490874$ | $1.667$ |

So off $= \tfrac12$ is forced by *each atom owns equal measure* — which is §27.3's quantile identity stated as a design constraint rather than observed as a coincidence. **$s_{\max} = 2\rho_0$ stands.** Only its mechanism changes: the $2$ is the half-cell that equal-measure spacing leaves at the end, and it would be $1$ or $\tfrac43$ under any other spacing, none of which is admissible.

### 33.4 What actually survives, and why

The reach result's robustness is real but it is a *different* robustness than the one claimed. It is **domain-independence**:

| domain | $\rho_0$ | $K$ | measured $s_{\max}$ | $2\rho_0$ |
|---|---|---|---|---|
| signed $[-\infty,\infty]$ | $512$ | $1608$ | $1023.6843$ | $1024$ |
| signed $[-\infty,\infty]$ | $10^5$ | $314159$ | $199999.8311$ | $200000$ |
| atom $[0,\infty]$ | $512$ | $804$ | $1023.6843$ | $1024$ |
| atom $[0,\infty]$ | $10^5$ | $157080$ | $200000.4677$ | $200000$ |

Half the atoms over half the arc leaves the spacing at home unchanged at $1/\rho_0$, and the reach depends on nothing else. That is why §31.2's factor-of-two correction moved the totals and left the reach alone — and it is the correct reason, replacing the covering-degree story.

### 33.5 The fifth weld, and what it says about the vocabulary

This is the same failure §31.4 diagnosed, made independently by a different reader: **a $2$ appears, the deck group is a $2$, weld.** I made it at §29.7 with the orientation bit. It has now been made again, unprompted, about a different $2$.

One person making a mistake is a habit; two people making the same mistake from the same text is a property of **the text**. This corpus has trained a vocabulary in which every factor of two looks like the deck group — because the deck group is genuinely load-bearing, genuinely a $2$, and genuinely everywhere in §5, §13.4b and §13.4c. The vocabulary is doing what good vocabulary does, and its cost is that it makes an unearned identification feel like recognition.

The practical consequence: **every $2$ in this corpus should carry its provenance.** There are at least three distinct ones now — the deck group $\{\pm1\}$ of $S^1 \to \mathbb{RP}^1$, the orientation bit $\operatorname{sign}(\det)$ (§31.3), and the half-cell of the equal-measure grid (§33.2) — and they are not the same $2$. An audit of the corpus's other twos is now on the open list.

*(One recorded slip of my own: the test script's summary line hardcoded the coefficients as "2.00, 1.00, 4.00, 8.00" while the table it printed above showed $2, 1, \tfrac43, \tfrac87$. Wrong law — $1/(1-\text{off})$, not $1/\text{off}$ — asserted in prose three lines under the correct numbers. Same failure mode as the welds: a summary written from expectation rather than from the output directly above it.)*

`[clean; §33.2 is a refutation of a proposed mechanism, §33.3 rescues the result with the correct one. All four tables are exact.]`

---

## 34. The Born identification: the sixth weld, and it is in the front matter

§33.5 concluded that the corpus's vocabulary makes unearned identifications feel like recognition, and put an audit of the framework's other identifications on the open list. The highest-stakes one is in the front matter, and it carries the quantum-mechanics recovery:

> *"the observable is the square that forgets which sheet one stands on: Born's $|\psi|^2$, identically the $\det^2$ by which the Maslov index is defined, **both being the quotient by $\psi \mapsto -\psi$**."* … *"Everything the corpus says about quantization follows from that one sentence."*

It does not survive. The theorem it was claimed to generate is unaffected; what fails is the interpretive bridge. Both are set out below.

### 34.1 The two squares quotient by different groups

$|\psi|^2$ is invariant under $\psi \mapsto e^{i\alpha}\psi$ for **every** $\alpha$, not only $\alpha = \pi$ — verified at five phases, all returning $1.962570903017$. So:

$$\text{fiber of } |\psi|^2 = \text{a circle}, \ \ \text{group } U(1) \qquad\text{vs.}\qquad \text{fiber of } \det^2 = \text{two points}, \ \ \text{group } \mathbb{Z}_2.$$

One forgets a sign; the other forgets a continuum. "Both being the quotient by $\psi \mapsto -\psi$" is false of the first.

And this paper already located the seam being crossed. §24.4: *"The group is **orthogonal, not unitary**… Making it unitary requires the complex structure — §13.4's $i$ — and that is a **separate premise**, not a consequence of anything in §4."* The Born identification crosses exactly that seam, in the front matter, without naming it.

### 34.2 The decisive failure: $\mathbb{Z}_2$-invariance gives *even*, not *squared*

This is the one that settles it. **Every even function of $\psi$ is invariant under $\psi \mapsto -\psi$:**

| candidate observable | at $\psi$ | at $-\psi$ | $\mathbb{Z}_2$-invariant? |
|---|---|---|---|
| $\lvert\psi\rvert^2$ | $3.250000$ | $3.250000$ | yes |
| $\lvert\psi\rvert$ | $1.802776$ | $1.802776$ | yes |
| $\lvert\psi\rvert^4$ | $10.562500$ | $10.562500$ | yes |
| $\operatorname{Re}(\psi)^2$ | $2.890000$ | $2.890000$ | yes |
| $\lvert\psi\rvert^2\cos(2\arg\psi)$ | $2.530000$ | $2.530000$ | yes |
| $\tanh\lvert\psi\rvert^2$ | $0.996998$ | $0.996998$ | yes |

All pass. **The covering-degree argument yields "even." It does not yield "squared."** It underdetermines Born by an infinite-dimensional function space, and no amount of care about the covering map closes that gap, because the gap is not about the cover.

### 34.3 What actually picks the square

Additivity over orthogonal alternatives — and only $p = 2$ survives it. $\sum_i |c_i|^p$ over normalised states:

| dim | $p=1$ | $p=2$ | $p=3$ | $p=4$ |
|---|---|---|---|---|
| $2$ | $1.409753$ | $\mathbf{1.000000}$ | $0.713756$ | $0.512517$ |
| $5$ | $2.067025$ | $\mathbf{1.000000}$ | $0.539036$ | $0.311075$ |
| $20$ | $3.869813$ | $\mathbf{1.000000}$ | $0.320718$ | $0.119850$ |

The square comes from **normalisation plus additivity** — Gleason's premise — not from the cover. That is a received premise by the corpus's own standard, and it was not booked.

### 34.4 What survives, and it is the important half

**The metaplectic content is real and correct.** `born_cover.py`'s D2 — the amplitude returning $-1$ after one classical period and $+1$ after two — is a genuine $\mathbb{Z}_2$ fact, correctly measured, and it establishes what it was built to establish: **the observable must be insensitive to that sign.** That is the Maslov index, that is the $\mu/4$ offset, and that is where the quantization condition comes from.

**So the quantum-mechanics recovery is intact.** The integer comes from $\pi_1 = \mathbb{Z}$; the quarter comes from the covering degree. Neither needs $|\psi|^2$. The Success Criterion's one clean win — *the quantization condition from the E-branch with nothing received* — does not depend on the sentence that failed.

**What fails is the interpretive bridge**: *"the square root in quantum mechanics is the pair the division would have destroyed."* The framework explains why the observable is **sign-blind**. It does not explain why the observable is the **modulus squared**, and the front matter claims both.

### 34.5 The repair, already in the corpus

§29.2 proved the right thing and the front matter attributed it to the wrong place. The invariants of two held pairs satisfy exactly one relation:

$$\det(a,b)^2 + (a\cdot b)^2 = |a|^2|b|^2, \qquad \text{residual } 5.6\times10^{-17},$$

which for a unit hold is $\sin^2 + \cos^2 = 1$ — **and that is normalisation.** So the square is forced by the *Pythagorean relation among the invariants*, not by the covering degree. The framework can reach Born, from §29's exhaustiveness result rather than from §13.4b's cover, and the premise it needs (additivity over orthogonal alternatives) is then visible instead of hidden.

That derivation is one section old.

### 34.6 A literature note that makes the crossing worse, not better

I checked whether the real-versus-complex gap is a technicality. It is not, and it is **live**: Renou et al. (*Nature*, 2021) argued real quantum theory is experimentally falsifiable and reported a test; Gidney and subsequent work dispute the result's hidden assumption (that participants share no prior entanglement), and the question was still being argued in 2026.

The corpus does not need to take a side. The point is the opposite: **a step the foundations community has spent five years arguing about is not one a front-matter sentence may take silently.** Whichever way that dispute settles, "real pair, $\mathbb{Z}_2$" $\to$ "complex amplitude, $U(1)$" is a substantive move requiring a stated premise, which is what §24.4 said and what the front matter did not do.

### 34.7 Verdict against the Success Criterion

The criterion asks for recovery *without importing assumptions as axioms*. Scored honestly:

- **Quantization condition** — met; unadjudicated; unaffected by this audit.
- **Born's rule** — **not** recovered. Two premises were imported without being booked: the complex structure (§24.4's own finding) and additivity (Gleason's). Both are now nameable, and one of them the corpus had already identified in a different section without connecting it.
- **Front matter** — overclaims. "Everything the corpus says about quantization follows from that one sentence" is true of the quantization and false of the Born rule bundled with it.

This is the sixth weld of the session and the first one found in load-bearing published text rather than in this week's additions. Its shape is identical to the other five: *both are quotients by a sign, therefore the same object.* The difference is that this one has been in the front matter for months, and the audit that would have caught it takes about four minutes.

`[clean; §34.2 and §34.3 are exact and decisive. §34.4 states what survives — the quantization recovery is untouched. §34.5 gives the alternative derivation. Verification: born_audit.py, B1–B5.]`

---

## 35. The identification audit — a ledger, not a development

§34 closed by saying every identification reading as *recognition* should be assumed unaudited until it has had four minutes. This section spends those four minutes on the four remaining load-bearing ones. **Three of four fail.** No new mathematics is proposed here; this is a ledger.

### 35.1 "The sign the read cannot see is spin-½" — **fails, same shape as Born**

The $\mathbb{Z}_2$ is real: a $2\pi$ path in $SO(3)$ lifts to $-1.000000000$ in $SU(2)$, a $4\pi$ path to $+1.000000000$. Verified.

But the counterexample is famous and it is fatal to the *identity*: **the configuration space of a classical rigid body is $SO(3)$**, its universal cover is $SU(2)$, and the same $\mathbb{Z}_2$ is present. Dirac's belt trick demonstrates the topology *with a belt*. **A belt is not a fermion.**

So the cover supplies the sign. Spin-½ additionally requires that **states are sections of the cover** — spinors, not functions on $SO(3)$ — which is a quantum premise, received and unbooked. Exactly §34's shape: the cover gives sign-*blindness*, never the observable.

What survives: the framework correctly identifies a structure **necessary** for spin-½. And this is consistent with the corpus's own best negative — §13.4d found spin–statistics *unreachable*, with the exact obstruction. The pattern is now legible: **the framework reaches the topology and stops at the physics**, and it has been recording that boundary correctly in one place while crossing it in another.

### 35.2 "Physics has exactly two half-integer species" — **fails; right number, wrong argument**

Two readings, both bad.

*Reading A — two half-integer spin values.* False. $SU(2)$ has half-integer $j$ at every even dimension: $j = \tfrac12$ (electron), $\tfrac32$ (the $\Delta$ baryon, $\Omega^-$), $\tfrac52$, $\tfrac72$, … Infinitely many, all from **one** cover.

*Reading B — two covers, $S^1$ and $S^3$, giving 2D and 3D.* Also false, and more interestingly. The count of exchange species is a fact about the **abelianisation of the exchange group**, not about Hurwitz:

| dimension | exchange group | abelianisation | one-dim reps |
|---|---|---|---|
| 3D | $S_n$ | $\mathbb{Z}/2$ | **exactly two** — trivial and sign |
| 2D | $B_n$ (braid) | $\mathbb{Z}$ | $\operatorname{Hom}(\mathbb{Z}, U(1)) = U(1)$ — **a continuum** |

Brute-forced at $n = 3, 4, 5$: exactly two homomorphisms $S_n \to \{\pm1\}$ in each case. So "exactly two" is **true in 3D and false in 2D**, where the answer is the anyon continuum — and *half-integer* is the wrong word for that family anyway, since anyonic statistics are continuously parameterised ($\theta = 0$ boson, $\pi$ fermion, $\pi/2$ semion, and everything between).

**The Hurwitz route gets the right number by a wrong argument and gets 2D wrong.** The correct source of "exactly two" is $S_n^{\mathrm{ab}} = \mathbb{Z}/2$, which the corpus does not cite and which has nothing to do with division algebras.

### 35.3 "Quantization is compactness" — **fails on the corpus's own test case**

Compact $\Rightarrow$ discrete spectrum is true. The converse is what the front matter asserts, and it is refuted by the example the corpus itself uses:

| potential | configuration space | lowest eigenvalues |
|---|---|---|
| $V = x^2/2$ | $\mathbb{R}$ — **non-compact** | $0.499998, 1.49999, 2.499974, 3.49995, 4.499918$ |
| $V = -1/(\lvert x\rvert + 0.3)$ | $\mathbb{R}$ — **non-compact** | $-1.260653, -0.293542, -0.170803, -0.082298$ |

Both discrete. The harmonic well is `born_cover.py`'s own test case and its configuration space is the whole real line.

**What is compact is the orbit in phase space, not the space.** The correct statement is Bohr–Sommerfeld's: *closed orbits quantize*. Compact configuration space is sufficient, not necessary, and the slogan blurs a distinction the corpus's own numerics depend on.

### 35.4 "The conservation is unitarity" — **already narrowed at §24.4; confirmed, still unpointed**

A random $O(2K)$ map preserves the norm to $4.4\times10^{-16}$ and fails to commute with $J$ ($\|QJ-JQ\| = 4.26$); an embedded $U(K)$ commutes exactly ($0.00$). So norm conservation delivers $O(2K)$, and $U(K)$ is the subgroup commuting with the complex structure. §24.4's narrowing is correct and complete.

The only outstanding item is bibliographic: **§22's boxed claim still carries no pointer to §24.4.** Logged with the other repairs.

### 35.5 What the ledger says

Four audits, three failures, and **all three are the same failure as §34** — a $\mathbb{Z}_2$ or a small count is correctly identified in the framework's own structure, then declared identical to a physical fact that requires strictly more. In each case what the framework has is **necessary and not sufficient**, and in each case the missing premise is nameable:

| claim | what the framework has | what it needs and did not book |
|---|---|---|
| $\det^2$ = Born | sign-blindness | complex structure + additivity |
| the sign = spin-½ | the $SU(2) \to SO(3)$ cover | states are sections of the cover |
| exactly two species | Hurwitz's $S^0, S^1, S^3$ | $S_n^{\mathrm{ab}} = \mathbb{Z}/2$ — a different theorem |
| quantization = compactness | closed orbits | the phase-space/configuration-space distinction |

**Nine welds now, all one shape.** And the ledger reveals the shape more precisely than §31.4 did: it is not merely *both are $X$, therefore the same $X$*. It is **necessary mistaken for sufficient** — the framework finds a real structural prerequisite for a physical fact, and reports having found the fact.

That is a more useful diagnosis, because it comes with a test that is not "compute both sides": **for every recovery claim, ask what else would also satisfy it.** A belt satisfies the spin-½ cover. Six even functions satisfy the Born cover. A harmonic well satisfies discreteness without compactness. If something outside physics satisfies your derivation, the derivation is of a prerequisite, not of the theory.

### 35.6 Standing against the Success Criterion, after the audit

- **Quantization condition (§13.4a)** — the integer from $\pi_1 = \mathbb{Z}$, the quarter from the covering degree. **Survives everything.** Still the corpus's one clean recovery, still unadjudicated.
- **SR kinematics** — met with a received mass; very high prior art; unaffected by this audit.
- **Born's rule, spin-½, exactly-two-species, quantization-is-compactness** — **not recovered.** Four claims, four unbooked premises, all now named.
- **Statistical mechanics, GR** — open, untouched.

**What the tests support: the framework derives topological prerequisites of quantum mechanics from one premise, and does not derive quantum mechanics.** The front matter states the second.

`[ledger; no new mathematics. All four audits are decisive and cheap. Verification: identification_audit.py ID-1–ID-4, species_count.py ID-2b.]`

### 35.7 The repair pass, executed

The audit returned fifteen findings; four were mathematical errors and were fixed at §31. The remaining eleven were documented and left standing, which is a worse state for a manuscript than either fixing or not finding them. They are now closed:

| finding | repair applied |
|---|---|
| §18.1's menu measure "at every scale, for every observer" | corrected to $\pi\rho_0$; $\pi$ only at $\rho_0 = 1$ |
| §18.4's "**every** appearance of either constant" | falsified in place; $2/\pi$ has three identities |
| §18.4's "the hold is 2 registers" gloss | marked superseded by §25.3 and §33 |
| §18.6's "one repair" and "claiming nothing" | both false; the repair is §27.4's, the grade is corrected |
| §20.2/§20.6's "the observer has the total" | scoped to $2/\pi$; §28.5 shows $\pi$ never arises |
| §3's `[clean]` on an asymptotic horizon | scoped to the read chart; §31.1's geodesic supplies the geometry |
| §25.1's $[0,1]$ against §27.2's $[0,1]$ | the (chord, arc) hold marked as a *different* hold |
| §26.2's "radius $1$" three lines above "radius $\tfrac12$" | corrected to $\tfrac12$ |
| §2's ledger grade "earns no number" | upgraded; §32.1 supplied the number |
| §23.5's "three independent ways" vs §25.8's "two, not three" | reconciled to two |
| §21.6's held rate as $2/\pi$ | corrected to $1/\rho_0$; flagged for §10.16 in the corpus |
| §11's "the only arithmetic the body performs" | corrected to one of two; §21.4's count is the other |
| §23.2 and §22.2 missing forward pointers | added to §27.3 and §24.4 respectively |

**Not done, and logged rather than claimed:** the appendix hygiene batch — script label collisions across `balance_checks.py`/`lifetime.py` (B1–B4), `menu.py`/`one_uniqueness.py` (V1, V3), `dial.py`/`two_budgets.py` (D2), `tangent_density.py`/`budget_is_cauchy.py` (E1, E3, E4); five cited checks that do not exist in the appendix (R3–R5, E2, E5, V5); one quadrature result banked three times as independent corroboration (V1, P4, C3 and §26.1 are one integral); and six sections each described as "the strongest in the paper" — the last of these is closed at §35.8. None is an error of substance.

`[ledger]`

### 35.8 A correction to the paper's voice

The paper was written preferring an outcome. Not the usual one — it does not oversell the framework — but the inverse: it had developed a register in which finding an error reads as a win. Counted before this pass: **thirty-five instances** of evaluative comparison in §§25–35, including "the repair is better than the claim it replaces," "worth more than the correction," "a claim that survives being narrowed by its own check is worth more than one that was never tested," and twelve ledger verdicts carrying editorial tails ("the deepest of the twenty," "the single most valuable line," "the strongest section in the paper" — six sections claimed that last one, which the audit had already flagged as a collision).

Two effects, and the second is the one that matters.

**It makes the negatives unweighable.** A reader cannot tell from "this is a narrowing, not a demolition" whether the result is minor or whether the writing is performing composure. The same prose that celebrates a correction is unavailable for reporting one neutrally.

**And it is a preference, so it can bias selection.** A voice that rewards finding errors will find them. The audits in §§31–35 were run against tests fixed in advance and their arithmetic is checkable, so the *results* stand as computed. But the framing around them — which items were promoted to "welds," which were called consequential — was chosen by a writer with a stake in the count.

Removed: all thirty-five. The verdicts stay, since `Passes`/`Fails` against "did the identification do work" is the stated discipline and a criterion is not a preference. What is gone is the layer above it — the rankings, the comparatives, and the sentences explaining why a result was worth having.

`[correction to the manuscript, not to a result. No number changes.]`

---

## 36. A hypothesis about the pattern, tested and refuted

After §35 the question was what the audits leave standing. Two readings were on the table.

**Reading A (the user's):** the bounded observer recovers much, not all.

**Reading B (mine):** something sharper — every recovery achieved is of *form* (topology, group structure, invariant shape, dimensionless relation) and every failure is one requiring *magnitude* (a scale, a measure on states, a dimensionful constant). On this reading the failures are not gaps but the framework's own premise P3 ("no external scale") appearing downstream as exactly what it forbids.

Reading B was put to an independent adversarial test over the whole corpus, with instructions to find counterexamples in either direction. **It is refuted.**

### 36.1 The refutation

**Seven pure-form claims failed for pure-form reasons.** The decisive one is §13.4d, which this paper produced earlier in the same session:

> *"spin–statistics is not reachable from this framework's premises at this layer" … $\pi_1 = \mathbb{Z}_2 \wr S_N$ … "in that group $\tau$ and $\rho$ are independent generators. **Topology admits all four.**" … "this is a case where it demonstrably cannot."*

Homotopy, wreath products, characters. No magnitude anywhere. Also failing on form: spin-½ (§35.1), the species count (§35.2, a combinatorial count — explicitly on the form side), quantization-is-compactness (§35.3), level 3 of the scale-connection tower ($F = dA \equiv 0$ identically), and §7.6's attention budget ("tested and confirmed vacuous").

The most damaging is general relativity, which Reading B most needs to fail for magnitude reasons. The corpus's own audit says otherwise:

> *"the closing move is a **category error**: Einstein's equations govern the Levi-Civita connection of a metric (Lorentz/$GL$, non-abelian, metric-compatible), **not an abelian $\mathbb{R}^+$ scale connection**."*

Wrong group, not missing scale.

**And the surviving half of Reading B survives trivially.** "Successes are of form" holds because the corpus *stipulates* it — "the observer supplies the form, the world supplies the magnitude" is doctrine stated before any recovery is attempted (§8.7, §13.16). Magnitude claims are therefore never entered as recoveries; they are pre-booked as receipts. **A category never entered cannot be observed to fail**, so its absence from the success column is a property of the write-up, not a discovered limit.

The causal claim is circular for the same reason. P3 does not get *revealed* by the pattern; P3 *produces* the pattern by governing what is written down as a claim.

### 36.2 What Reading B would have done

It would have relocated seven errors into a boundary phenomenon. Spin–statistics, spin-½, the species count and the rest are not the framework meeting a principled limit — they are mistakes, four of them found in one session. Reading B would have described them as the premise working correctly.

Two further observations from the test, both against Reading B's interest:

- **The corpus is disciplined about receipts and undisciplined about form.** Mass, $\hbar$, $\rho_0$, the correlator, $\alpha/\beta$ are all booked as received where they are used. Where it overclaims, it overclaims about *form* — Born, spin-½, species, compactness, Einstein. That is the opposite of Reading B's prediction.
- **The form/magnitude binary does not even sort reliably.** §15.15's $H(1) = 8$ was a published dimensionless invariant that turned out unit-relative ("in radians … $H(1,N)$ does not tend to $8$"), undetected across three audit rounds. And the register rent — $\tfrac12\log_2 m$ bits per act, graded theorem — is an exact *rate*, which the binary mis-sorts because both its units are internally derived.

### 36.3 What replaces it

Two axes, both taken from text already in the corpus.

**What the framework honestly declines: self-derived units versus external units.** This sorts the cases the form/magnitude binary mis-sorts — the register rent (bits per act, both internal), $T/a = 1/2\pi$ (dimensionless), and $\pi$'s evaluated value (an internal normalisation, though see §36.4).

**Where the framework actually fails: prerequisite versus theory.** This is §35.5's own diagnosis — *necessary mistaken for sufficient* — and every one of the seven form failures sits on it. None sits on the first axis.

And the test's closing observation, which applies to this section:

> Form is necessary for the framework's successes and not sufficient — the same error the corpus caught itself making about physics, now one level up in the story told about the corpus.

### 36.4 One item the test surfaced

§12.4a evaluates $\pi = 3.141592653590$ from the home normalisation. The corpus elsewhere states that $\pi$ is unreachable by any finite forced computation (§10.2) and that it is a received scale (§7.6). Not a contradiction — the §12.4a evaluation is the *describer's*, by §28.5's own audit — but the section did not say so, and as written it reads as though the observer mints the value. Corrected in the corpus with one clause.

### 36.5 Standing

Reading A stands. The bounded observer recovers much and not all, and the boundary is not currently characterised — the one attempt to characterise it is refuted above. What can be said is narrower:

- One clean recovery survives every audit: the quantization condition (integer from $\pi_1 = \mathbb{Z}$, quarter from the covering degree), unadjudicated.
- SR kinematics stands with a received mass.
- Four claims are recorded as not recovered, with their unbooked premises named.
- Spin–statistics is recorded as demonstrably unreachable, with the obstruction stated.
- Statistical mechanics and general relativity are open, and GR's own audit locates its obstruction in group structure.

`[a hypothesis tested and refuted; no result changes. Refutation performed independently against the whole corpus with instructions to seek counterexamples in both directions.]`

---

## 37. Why a serial bounded observer learns anything

The framing so far asked what the observer fails to recover. The prior question is why it recovers anything: it receives one atom at a time from a system of size $N \ggg K$, keeps nothing across acts, and touches a vanishing fraction of the world. One result below is quantitative; the rest is framing, and §37.5 states what the framing does not establish.

### 37.1 The asymmetry

A universal claim over $N$ items costs $O(N)$ to verify and $O(1)$ to refute.

| $N$ | verify | refute |
|---|---|---|
| $10^3$ | $10^3$ | $1$ |
| $10^6$ | $10^6$ | $1$ |
| $10^{80}$ | $10^{80}$ | $1$ |

§7 bars the observer from $O(N)$. It does not bar it from falsification. So the observer is barred from **census** and not from **testing laws** — which is the structural reason it can learn at all: a law is refutable by one instance, a state requires enumeration.

### 37.2 One register matches unbounded memory — for the invariant quantities

This is the section's one number. Estimate the median of a Cauchy stream two ways: full memory (store all $n$, sort) versus $M = 1$ (one register, sign-and-halve, nothing stored).

| $n$ | full-memory error | $M=1$ error | ratio |
|---|---|---|---|
| $100$ | $0.150628$ | $0.155289$ | $1.03$ |
| $1{,}000$ | $0.037703$ | $0.035371$ | $0.94$ |
| $10{,}000$ | $0.012912$ | $0.012430$ | $0.96$ |
| $100{,}000$ | $0.005211$ | $0.005334$ | $1.02$ |

Indistinguishable across three decades. **For a stream-invariant quantity, one register is worth unbounded memory** — the world re-presents, so nothing need be stored. This is §21.4's entrainment generalised: memorylessness costs nothing on the invariants.

### 37.3 And no $K$ buys a state fact

Same stream, different question: what was the value of the 37th sample? Running functionals at $K = 1, 8, 64, 4096$ recover none of it; the true value $0.846307$ is not a function of any invariant. **Stream-invariant quantities cost one register; state facts cost $N$ registers at any $K$.** There is no middle term.

### 37.4 How much of a size-$N$ world is invariant

Presented in random order, a world of $N$ items has $N!$ arrangements and one invariant — the multiset:

| $N$ | arrangements | addressable serially |
|---|---|---|
| $10$ | $3.6\times10^{6}$ | $10$ numbers |
| $50$ | $3.0\times10^{64}$ | $50$ numbers |

The learnable fraction is vanishing. It is also where the laws live, since a law is a constraint on the multiset and not on the arrangement.

### 37.5 What this does not establish

$O(1)$ refutability holds only for claims with **no free parameter**:

| claim | refutable by |
|---|---|
| $v/h$ composes as $(x+y)/(1-xy)$ | one counterexample |
| $v/h$ composes as $(x+y)/(1+cxy)$, $c$ free | $N$ samples to bound $c$ |
| the density is Cauchy | one, if exact |
| the density is Cauchy-like, tails $\sim a$ | $N$ samples for $a$ |

The framework's recoveries are parameter-free (topology, group laws); its receipts — mass, $\hbar$, $\rho_0$ — are exactly the parameters. So §37.1's asymmetry does not *discover* the boundary between them; it restates P3, in the same way §36's form/magnitude reading restated it. **Flagged rather than repeated:** this section explains why the invariant class is non-empty and why one register exhausts it. It does not explain which laws the framework gets right, and §35's four failures are all cases of getting a parameter-free law wrong.

### 37.6 What it buys

- **§37.2 earns a number**: $M = 1$ against unbounded memory, ratio $\approx 1$ over three decades, on a distribution with no mean.
- The rest is framing, and it is the framing the paper was missing — not *why so little*, but *why the invariant class is non-empty at all*, and why one register exhausts it.
- §37.5 records that the framing restates a premise rather than finding a boundary, which is the error §36 was refuted for.

`[§37.2 verified; §37.1, §37.4 elementary; §37.5 is a limit on the section's own reading. Verification: why_anything.py W1–W5.]`

---

## 38. The last recovery, audited

After §35 the corpus's standing against its own Success Criterion rested on one result — §13.4a's quantization condition — which §15.30 records as `UNADJUDICATED`. It was put to §35.5's test: *what else would also satisfy this derivation?*

### 38.1 Winding is present with a continuous spectrum

Keep the held pair, the $\mathbb{RP}^1$ read and the one-way lemma exactly as §13.4a has them, and apply them to a free particle ($V = 0$, $E > 0$):

| $E$ | nodes on $[0,20]$ | winding monotone | $E$ admissible |
|---|---|---|---|
| $0.25$ | $4$ | yes | yes — continuum |
| $1.00$ | $7$ | yes | yes — continuum |
| $2.37$ | $10$ | yes | yes — continuum |
| $9.00$ | $20$ | yes | yes — continuum |

Every piece of the mechanism is intact and the spectrum is continuous. **Winding does not make discreteness.**

### 38.2 Discreteness comes from the decay condition

Shooting $\psi'' = (x^2 - E)\psi$ from a decaying start:

| $E$ | node tally | $\psi$ at $+x_{\max}$ | eigenvalue |
|---|---|---|---|
| $1.00$ | $1$ | $-1.4\times10^{-3}$ | yes |
| $1.60$ | $1$ | $-8.3\times10^{5}$ | no |
| $2.40$ | $1$ | $-1.5\times10^{5}$ | no |
| $3.00$ | $2$ | $1.1\times10^{-4}$ | yes |
| $3.70$ | $2$ | $1.4\times10^{4}$ | no |

The tally is defined and finite at the non-eigenvalues. What excludes them is that $\psi$ diverges — normalisability. **The decay condition selects; the winding indexes what has already been selected**, and §13.4a neither derives that condition nor books it as received.

### 38.3 The quarter reverts to a received premise

§13.4b discharged the quarter as (covering degree) × (weight $\tfrac12$), the weight coming from "its square is a density." If the observable is $|\psi|^p$, the amplitude carries weight $1/p$ and the offset is $\mu/(2p)$:

| observable | offset | matches QM |
|---|---|---|
| $\lvert\psi\rvert$ | $\mu/2$ | no |
| $\lvert\psi\rvert^2$ | $\mu/4$ | **yes** |
| $\lvert\psi\rvert^3$ | $\mu/6$ | no |

Only $p = 2$. §34 established that $\mathbb{Z}_2$-invariance yields *even*, not *squared*, so the framework does not fix $p$. **§13.4b's discharge rests on the identification §34 refuted**, and §13.4a's original ledger — two premises, not one — is restored. I had not traced that dependency when writing §34.

### 38.4 What survives

| element | status |
|---|---|
| the pair equation is linear Schrödinger | the ODE is received |
| the one-way lemma | **derived**, clean, unaffected |
| the tally is a winding number, $\pi_1 = \mathbb{Z}$ | **derived** |
| the tally indexes the bound states | Sturm's theorem, classical |
| the spectrum is discrete | **not derived** — decay condition, received |
| the offset is a quarter | **not derived** — Born's exponent, received |

So the framework derives: **given a bound spectrum, the index is an integer, and that integer is a winding number on the observer's own read.**

That is precisely what §13.4a claims in its second paragraph — *"one structural fact about quantum mechanics — that the bound spectrum is indexed by an integer at all"* — and it is correct. The overclaim is four paragraphs later, in the closing status: *"it derives the reason the spectrum is discrete."* **The section contains the true claim and the false one, and the true one came first.**

### 38.5 Standing

One recovery remains, narrower than advertised: the integer index of a bound spectrum is a winding number on $\mathbb{RP}^1$, with oscillation theory classical and the framework supplying the reading — which §13.4a concedes in its own text ("what the framework supplies is the reading of it").

Discreteness, the quarter, Born, spin-½, the species count and quantization-is-compactness are received or refuted, premises named. SR kinematics stands with a received mass. Statistical mechanics and general relativity are open, GR's obstruction located in group structure.

**No established theory is derived. One structural feature of one theory is re-read in the framework's own coordinate, correctly.**

### 38.6 The criterion, replaced

That sentence is a failure only against the standard the corpus set itself — *"earns its standing only by recovering established theories… and no other"* — and the author's position is that recovery was never expected. The criterion has therefore been replaced in the corpus front matter (§15.38), from a **recovery programme** to a **constraint programme**: impossibility, completeness and cost claims, each falsifiable by a single instance.

Two points, since a criterion revised the day it is failed invites the obvious charge.

**It is stricter.** A failed derivation is ambiguous — missing, or wrong? A counterexample to a constraint is decisive. The corpus already has three such outcomes: §14's free-read claim tested and split by winding numbers, §7.6's conservation tested and found vacuous, §13.4d's spin–statistics claim tested and found unreachable with the obstruction written down.

**And the old criterion appears to have caused the failures it was meant to detect.** A standard granting standing only for recovering established theories creates pressure to see recoveries, and §35.5's *necessary mistaken for sufficient* is what that pressure produces. Six of the nine identification errors sit where the framework reached across to claim a physical theory.

Not a rule, though: two of the seven audited failures were internal construction errors, not overreach. Staying on the observer's side is a tendency.

Everything standing tonight satisfies the new criterion, including the one surviving coincidence — which becomes a re-reading correctly located rather than a theorem short of its target. And the extraction programme's awkward finding, that three of four theorem-grade candidates have nothing to do with observation, stops being awkward: it is what a constraint programme looks like when it produces mathematics.

`[audit; two corrections to §13.4 applied in the corpus, one ledger restored. Verification: last_recovery.py Q1–Q4.]`

---

## 39. The operation table is complete, and its third entry is the one the corpus calls a bug

§29 proved the *read* side complete: exactly four rotation-invariants of two held pairs, one relation, no fifth. There was no equivalent for the *operation* side — §3.7.1's table is exhibited and never shown exhaustive. The revised criterion (§38.6) makes that the natural question, since a completeness claim is falsified by producing one more entry.

### 39.1 Exactly three

Impose what the framework already requires of a binary operation on atoms: **bilinear** (division-free, degree one in each pair), **associative** (composing atoms cannot depend on grouping), **unital** (a two-sided identity atom exists). A bilinear map $(\mathbb{R}^2)^2 \to \mathbb{R}^2$ has eight free parameters; those three conditions reduce it to a basis $\{1, j\}$ with $j^2$ a single constant, and completing the square and rescaling puts

$$j^2 \in \{-1,\ 0,\ +1\}.$$

Verified: all three are associative and unital over 400 random triples each. This is the classification of two-dimensional real unital associative algebras and it is complete — **there is no fourth.**

### 39.2 The three are the corpus's own three

| algebra | $j^2$ | zero divisors | §9.5 subgroup | §8.7 branch |
|---|---|---|---|---|
| **complex** | $-1$ | none found in $2\times10^5$ tries | elliptic | **E** |
| **split** | $+1$ | found | hyperbolic | **H** |
| **dual** | $0$ | found | parabolic | **unnamed** |

The algebraic classification and the subgroup census are the same list, reached independently.

### 39.3 The corpus uses two of the three and records the third as an implementation bug

- $\oplus$, the rotation law $(vh' + v'h,\ hh' - vv')$, **is complex multiplication** under $z = h + iv$ — residual $0.00\times10^{0}$.
- $\otimes$, componentwise, **is the split algebra.**
- The **affine pair-sum** $(vh' + v'h,\ hh')$ — which §3.7's crash-proof corollary records as *"an implementer's trap: it looks like the format and is not"* — **is the dual algebra.**

And the classification explains the trap rather than merely reproducing it. Feeding two exact horizons to each:

| operation | (horizon, horizon) | result |
|---|---|---|
| $\oplus$ | $(0, -2)$ | ordinary |
| $\otimes$ | $(2, 0)$ | ordinary |
| affine | $(0, 0)$ | **degenerate state formed** |

The dual algebra has nilpotents; that is *why* the affine sum manufactures $(0,0)$ from two horizons. The corpus found this empirically and filed it as a coding hazard. It is the third admissible product, and its zero divisors are the reason.

This also converges with the crash-proof test. That result — 112,000 exact-integer operations, $(0,0)$ formed 335 times, **every instance at the indeterminate product and none from $\oplus$** — is what the classification predicts: $\oplus$ is the one algebra of the three with no zero divisors, so it cannot form the degenerate state, and the two that can are the two that do.

### 39.4 And $\oplus$ is forced, not chosen

Write the pair as $z = h + iv$. Under $a \mapsto e^{it}a$, $b \mapsto e^{iu}b$ the four real-bilinear maps carry weights $(+1,+1)$, $(+1,-1)$, $(-1,+1)$, $(-1,-1)$ for $ab$, $a\bar b$, $\bar a b$, $\bar a \bar b$. Requiring **the composite's read to be the sum of the reads** selects weight $(+1,+1)$, which is $ab$ alone. Residual $9.6\times10^{-15}$ over $5\times10^{4}$ random pairs and angles.

So $\oplus$ is the unique bilinear composition for a framework whose reads add.

### 39.5 What follows

- **§3.7.1's operation table is complete for binary composition**, and the claim is falsifiable in the criterion's own terms: exhibit a fourth bilinear associative unital product and it falls.
- **§8.7's fork should be a trichotomy.** It is stated as binary — E and H — and the third branch exists, is admissible, and is where the corpus's one degenerate state comes from. The parabolic case should be named in the table with its zero divisors stated, rather than appearing only as a warning in an implementation note.
- **The crash-proof claim gains its reason.** $\oplus$ cannot manufacture $(0,0)$ because $\mathbb{C}$ has no zero divisors — which is a one-line proof replacing an empirical result over 112,000 operations.

**Scope.** This covers *binary* composition under bilinearity, associativity and unitality. Unary operations — the swap, the fold, normalisation — are a separate question and are not addressed. Dropping associativity would admit more products, and the corpus does not currently state whether associativity is a requirement or an observation.

`[completeness result for binary composition; the algebra classification is classical, the identification of the corpus's three operations with it is the corpus's. Verification: operation_table.py O1–O4.]`

---

## 40. What the beam says about special relativity, after §31 and §39

Two results this session changed the answer. §31.1 corrected which subgroup the beam is in; §39 proved there are exactly three. Together they turn a resemblance into a completeness claim.

### 40.1 The beam's law is the boost, and it is the split algebra

$b_{13} = (b_{12} + b_{23})/(1 + b_{12}b_{23})$ — associative to $2.0\times10^{-14}$ over $2\times10^5$ triples, and equal to $\tanh(\operatorname{artanh} + \operatorname{artanh})$ at every pair tested.

§39 identifies which of the three admissible products this is: the **split** algebra, $j^2 = +1$. Its exponential is $\exp(\varphi j) = \cosh\varphi + j\sinh\varphi$ — a boost — its unit circle is the hyperbola $\cosh^2 - \sinh^2 = 1.000000000$, its angle is rapidity, and its read is $\tanh\varphi$:

| $\varphi$ | $(\cosh, \sinh)$ | read |
|---|---|---|
| $0.5$ | $(1.127626,\ 0.521095)$ | $0.462117157$ |
| $1.0$ | $(1.543081,\ 1.175201)$ | $0.761594156$ |
| $2.0$ | $(3.762196,\ 3.626860)$ | $0.964027580$ |

So the beam and the boost are not analogous. They are the same one-parameter subgroup, and §39 established that the framework admits exactly three.

### 40.2 What forces this law — and it is not associativity

Any law of the form $f^{-1}(f(x) + f(y))$ is associative with identity $0$. Associativity therefore does **not** select $\tanh$. What selects it is **rationality**: the framework's operations are division-free polynomials on the pair, so the law must be Möbius in each argument.

| conjugating $f$ | law | Möbius |
|---|---|---|
| $\operatorname{artanh}$ | $(x+y)/(1+xy)$ | **yes** — hyperbolic |
| $\arctan$ | $(x+y)/(1-xy)$ | **yes** — elliptic |
| identity | $x + y$ | **yes** — parabolic |
| $\arcsin$ | $\sin(\arcsin x + \arcsin y)$ | no |
| $x^3$ | $(x^3+y^3)^{1/3}$ | no |

The $\arcsin$ law differs from the Möbius one by up to $0.0679$ at $y = 0.4$ — a different function, not a reparametrisation. And the Möbius ones are exactly three, which is §9.5's census and §39's classification arrived at from the composition side.

**The forcing chain is the framework's own:** P1–P5 $\Rightarrow$ division-free $\Rightarrow$ rational $\Rightarrow$ Möbius $\Rightarrow$ three. Special relativity occupies one of the three.

### 40.3 The horizon and the light cone are unreachable for one reason

§31.1 placed the balance read along a geodesic of $H^2$, with $b = \pm1$ its ideal endpoints at infinite hyperbolic distance:

| rapidity | $b = \tanh\varphi$ | $H^2$ arc length | load to reach $b$ |
|---|---|---|---|
| $1$ | $0.761594156$ | $1.000000$ | $7.4$ |
| $3$ | $0.995054754$ | $3.000000$ | $4.0\times10^{2}$ |
| $6$ | $0.999987712$ | $6.000000$ | $1.6\times10^{5}$ |
| $12$ | $1.000000000$ | $12.000000$ | $2.6\times10^{10}$ |

*No finite weight reaches the extreme* and *no finite energy reaches $c$* are one statement about a geodesic's ideal endpoint. §3's asymptotic observation, which carried a `[clean]` grade on what was a chart-dependent claim, has a geometry underneath it.

### 40.4 What the beam does not supply

The fixed points sit at $b = \pm1$ **by normalisation**. Nothing in the beam says what physical speed is there — $(u+v)/(1 + uv/c^2)$ is the same law at $c = 3\times10^8$, $c = 1$, or $c = 42$.

So: **the beam gives the form of velocity addition and never $c$.** Under §38.6's criterion that is a coincidence located, not a derivation — and it is the same seam §13.2 books when it receives a mass.

### 40.5 The claim, in the criterion's own terms

Under the old standard this read as *the balance derives special relativity's kinematics*, which overstated it. The statement §39 supports is a **completeness claim**, and it is sharper:

> A bounded observer that composes comparisons division-freely has exactly three available laws — hyperbolic, elliptic, parabolic. Special relativity's velocity addition is the hyperbolic one. The beam realises the same law with weights, so the law is not a fact about spacetime; it is what division-free composition can do. What relativity adds is the identification of the fixed points with a physical speed, which the framework receives.

Falsifiable in the criterion's terms: exhibit a fourth division-free associative composition and §40.2 falls; exhibit a bounded observer composing comparisons by a non-Möbius law and the chain breaks earlier.

This also gives §1's alias-family result its role. Four families — impedance, weights, odds, intensity — all compose by the hyperbolic law to $10^{-11}$, with Fisher's $z$ as a negative control that fails. Under the old criterion that was corroboration of an SR derivation. Under the new one it is evidence for the completeness claim: **the law appears wherever bounded comparisons compose, and velocity is one instance rather than the source.**

`[the algebra classification is classical; the forcing chain from division-freeness to Möbius is the corpus's, and §40.5's restatement is what §39 supports. Verification: beam_sr.py S1–S5.]`

---

## Open questions, ranked by what they would buy

1. ~~**Is every conserved quantity a free $O(N)$ read?**~~ **Answered at §14: no.** The correct statement is *boundary functional*, not *conserved*, and the exception (winding numbers) split the notion of freeness in two. Superseded.
2. ~~**Is "free centre $\iff$ flat" exact, or exact only for constant curvature?**~~ **Answered at §15.2: exact for fixed-sign curvature, false in general.** What freeness detects is the enclosed total, not the pointwise value. Superseded.
3. **Does the weight-shift report saturate as $\tanh$ of the log pressure ratio?** (§13.) Measurable, joins two threads, and is the only genuinely empirical question here.
4. **Audit §1.8's known-domains table against the transitivity split.** (§10.) Cheap, and it protects the programme from its own worst failure mode.
5. **Is there a felt Wigner rotation, or only general shape-space holonomy?** (§12.) Interesting, and the honest answer may be no.
6. ~~**Is the flux/winding split exhaustive?**~~ **Partly answered at §15.3:** adiabatic invariants are class 1 (Stokes), not a third kind. The split stands, but exhaustiveness is unproved — what is now wanted is a *characterisation theorem*: are the free reads of a bounded observer exactly the boundary functionals and the monotone ranks? **Now the top open item**, and the most theorem-shaped question the paper has produced.
7. **New, from §33.5: audit every factor of two in the corpus for provenance.** At least three distinct twos are now known — the deck group, the orientation bit, and the half-cell of the equal-measure grid — and the vocabulary makes them read as one. Two readers have already welded two of them independently. Cheap, and it protects the most-cited constant in the framework.
8. **New, from §31.2: does §9.2's $K_{\max} = \pi\rho_0$ carry the same factor of two?** The contract as stated matches the *signed* read line; §1's atom is non-negative and gives $(\pi/2)\rho_0$. Either §9.2 implicitly uses signed reads or it is off by two. Cheap to settle and it touches a load-bearing bound.
9. **New, from §17.7: is the tension read a boundary read?** If it is, the body has a second native channel for a conserved total, alongside the centre of pressure. Cheap to settle and it would strengthen §11.
10. **From §16.4: can the act/field gap be closed, or is it structural?** The pulse is an observation; gravity is a medium. Every result in §16 is about orbits and fields and none of them uses the pulse's status as an *act*. Either that status does work somewhere or the identification is an analogy — and this programme has agreed not to keep analogies.
11. **From §16.4: reconcile §16 with §13.5.** Radial reach and scale connection are two accounts of gravity in one corpus. They must be one account or one of them is wrong.
12. **From §15.2: does anything downstream depend on constant curvature without saying so?** The free-centre argument does, and the corpus did not know it. An audit of §7 and §12.3 against that dependency is cheap and overdue.

## What this buys — the discipline applied to itself

By the standard we have been using: an identification earns its place only if it *does work* — if treating two things as one lets you compute or predict something you could not before. Applied here:

- **Weights add, comparisons don't** — earns the composition law across four alias families to $10^{-11}$, and earns the split that excludes Fisher's $z$. `Passes.`
- **Curvature is the price of a centre** — earns the flat/curved midpoint table, and earns a ruler-free flatness test. `Passes, pending the constant-curvature question.`
- **The two centres' gap is the tide** — earns $L^2/2R$. `Passes.`
- **Thomas precession is the defect** — earns nothing new numerically, since §13.9 already had the angle. What it earns is a *route*: the same result reachable without algebra. `Passes on transmission, not on content — and the paper should say so.`
- **The steelyard never divides** — **earns a number after all, at §32.1**: the centre of gravity is a division the balance never performs, reached exactly by sign-and-halve in 60 steps. A second instance of §28.5's audit structure. `Passes; the number arrived twelve sections later.`
- **The body computes it natively** — earns nothing yet. It becomes load-bearing only if question 3 is answered.

**Added at §14:** *free reads are boundary reads* — earns the $N$-independence table, the $(a/R)^2$ law, the entropy exclusion, and a genuine negative that splits the notion of freeness. `Passes.`

**Added at §15:** *curvature is itself a flux quantity* — earns the boundary identity to $10^{-11}$; and *freeness detects the enclosed total, not flatness* — earns a genuine counterexample (nowhere flat, zero holonomy) that **restricts** the paper's own central claim. `Passes, and a claim narrowed by its own check is recorded with the narrowing attached.`

**Added at §16:** *closure selects the law, and the two survivors are the two sheets of one square* — earns Bertrand's cut located at covering degree two, and the Bohlin map verified to $4\times10^{-14}$. `Passes, and it is the only place in the corpus where the square turned up somewhere nobody put it.` Against that: *gravity is the 3D pulse* as stated — earns nothing, and is retired in favour of the narrower claim. `Fails, correctly.`

**Added at §17:** the intuition section earns no new number and is not meant to — it earns **transmission**, which the extraction survey identified as the corpus's real bottleneck. Graded as a route, deliberately. `Passes as exposition; makes no claim.`

**Added at §18:** *π is the menu, 2π is the walk, π/2 ↔ 2/π is the exchange rate* — earns no number either, but it **repairs** $K_{\max} = \pi\rho_0$ from a contested tautology into an identity nobody needs to defend, and gives the π/2π split an image. `Passes as framing plus one repair.`

**Added at §19:** *inverse rates buy antisymmetry, not flatness* — earns the two-leg/three-leg split, dissolves the §8.5-versus-§13.6 tension, and earns *Thomas precession is triangular arbitrage* to $10^{-17}$. `Passes.`

**Added at §20:** *the observer halves; it never divides* — earns Vieta to $10^{-16}$ with no division, the factors identical to $\cos(\pi/2^n)$, and the half-angle identity showing the root is a chart artifact. It also **removes a live contradiction**: the corpus used $2/\pi$ while forbidding division and had never said how. `Passes, and this is the kind of catch the audit discipline exists for.`

**Added at §21:** *undergoing is free, anticipating costs bits* — earns the three-gap coverage table, the sign-plus-halve alignment to $10^{-16}$, and the entrainment lock to $10^{-13}$. It also **scopes §20**, which had implied nothing inside ever needs the value. `Passes, and the scoping is the more valuable half.`

**Added at §22:** *the pointing budget and the attention budget are one conservation, and its name is unitarity* — earns the $U(K)$ group identification at $K=6$, and unifies §7.6 with §13.4. Recorded with its own wrong first answer. `Passes, on the second attempt.`

**Added at §23:** *the budget is the measure* — earns the Cauchy at three ranks from the conservation ($10^{-4}$ KS), the fisheye as an immediate consequence, and the $2{:}1$ exhibited inside $s=v/h$. It joins §4 and §13.4, which had never been in contact. `Passes. Joins §4 and §13.4, which had not previously been in contact.`

**Added at §24:** *one uniqueness, not two* — earns the combination law identified as $SO(2)$ to $9\times10^{-12}$, invariance under rotation at three ranks, and the uniqueness located in transitivity. Its caveat locates the exact seam where the measure argument stops and the signature fork takes over. `Passes, and the caveat is the more useful half.`

**Added at §40:** *the beam and SR* — the beam's law identified as §39's split algebra, and the selection traced to **rationality** rather than associativity (any $f^{-1}(f(x)+f(y))$ is associative; only three are Möbius). Restates the SR claim as a completeness claim: three available laws, relativity occupies one, $c$ received. `Passes as a completeness claim; falsifiable by a fourth law.`

**Added at §39:** *the operation table is complete* — exactly three bilinear associative unital products on the pair ($j^2 \in \{-1,0,+1\}$), matching §9.5's subgroup census reached independently. $\oplus$ is identified as $\mathbb{C}$ and shown unique under reads-add ($9.6\times10^{-15}$); the third algebra is the affine sum the corpus files as an implementation bug, and its nilpotents are why it traps. `Passes. Falsifiable by a fourth product.`

**Added at §38:** *the last recovery audited* — the winding mechanism is exhibited intact on a continuous spectrum; discreteness is traced to the decay condition; the quarter is shown to be $\mu/(2p)$ with $p$ fixed only by Born, which §34 refuted. One recovery survives in the form §13.4a states at its opening and not the form it claims at its close. `Two corrections applied; one ledger restored.`

**Added at §37:** *why a serial observer learns anything* — earns $M=1$ matching unbounded memory on a stream-invariant quantity (ratio $\approx 1$ across three decades, Cauchy stream), and the verify/refute cost asymmetry that admits law-testing while barring census. §37.5 records that the asymmetry restates P3 rather than locating a boundary. `Passes on §37.2; the rest is framing and is graded as such.`

**Added at §36:** *the form/magnitude hypothesis* — proposed, tested independently, **refuted**. Seven pure-form claims fail for pure-form reasons, including spin–statistics and general relativity; the surviving half is a stipulation rather than a finding. Replaced by two axes taken from existing text. `Refuted. No result changes.`

**Added at §35:** *the identification audit* — four load-bearing claims tested, **three fail**, each by a decisive counterexample available in minutes (a classical belt for spin-½, the braid group's continuum for exactly-two-species, the harmonic well for quantization-is-compactness). It **names four unbooked premises**, leaves the quantization recovery untouched, and sharpens §31.4's diagnosis from *both are X* to **necessary mistaken for sufficient**, with the operational test that follows from it. `Ledger. Three of four claims fail; four premises named. No new mathematics.`

**Added at §34:** *the Born identification audited* — earns the $U(1)$-vs-$\mathbb{Z}_2$ group mismatch, the decisive underdetermination (six even functions all passing the covering test), the $p=2$ additivity table that shows what actually picks the square, and a **better derivation** from §29.2's Pythagorean relation. It **removes an unbooked import from the front matter** while leaving the quantization recovery — the corpus's strongest result — untouched. `Passes. The claim tested is in the front matter and predates this session; the quantization recovery is unaffected.`

**Added at §33:** *the factor of two is not the deck group* — earns a refutation by variation (the coefficient moves $2 \to 1 \to \tfrac43 \to \tfrac87$ under grid offset, which no covering degree can do), the correct law $s_{\max}/\rho_0 = 1/(1-\text{off})$, and the **rescue**: the midpoint offset is forced by equal-measure cells (ratio $1.000$ against $3.000$), so $2\rho_0$ stands with a new mechanism. `Passes. The identification is refuted by variation; the result stands on a different mechanism. Made independently by a second reader.`

**Added at §32:** *equilibrium — hold, balance, read* — earns the centre of gravity found by sign-and-halve to exactness with no division (a **second instance** of §28.5's audit structure, on a $\pi$-free quantity), the $N$-independent compression at four distribution sizes, and a **fourth weld caught**: §29.4's null law holds for quadratic nulls ($9.6 \to 10212$ over four decades) and not for linear ones, where the balance's advantage is a flat $1.4$ that vanishes if the gain is known. `Passes. Testing the framing also restricted §29.4's law to quadratic nulls.`

**Added at §31:** *the first adversarial audit* — earns three confirmed errors in the new material (a subgroup weld refuted by the very next subsection, a factor of two from a silently widened domain, and two distinct $\mathbb{Z}/2$'s identified as one), plus the $H^2$ geodesic reading that repairs §3's horizon. `Correction record. Three errors, all welds; the method note is at §31.4.`

**Added at §30:** *the Socratic elimination ladder* — earns no number as rhetoric, and is graded as exposition. But its repairs do: $h = 1 \iff$ home, so a count is denominated in the observer's own atom of size $1/\rho_0$ (verified at three scales); and the **mirror argument replaces the units argument**, surviving the counts-and-dimensionless objection that would have killed the opening. It also **makes a smuggled premise visible** — the whole/part split is P1–P5 restated, not a theorem. `Exposition. Two repairs carry results; one proposed step is recorded as refuted.`

**Added at §29:** *there are exactly three verbs — project, compare, count* — earns an exhaustiveness result from invariant theory, the Born relation as residual $4.3\times10^{-14}$, the null-method advantage as a $1/\sqrt{\sigma}$ law verified over six decades, bisection at one bit per step, and the orientation bit as the necessity argument for holding a pair. It **derives §12.3's order/topology/metric triple** instead of asserting it. `Passes. Exhaustiveness over rotation-invariants of two pairs; the generator list is textbook, the identification with §12.3 is not.`

**Added at §28:** *the observation is one density at the tangent point* — earns the gnomonic identification of $\tan$ to $10^{-16}$, measure $=$ tally exactly ($199999.9993$ vs $200000$), reach $= 2\rho_0$ with $\pi$ cancelling, and the $\pi$-audit showing every operational quantity is $\pi$-free. It **dissolves the standing $\pi$ discomfort** rather than managing it, **finds a display constraint** the two-stage quotient predicts, and **narrows §25's headline a third time**. `Passes. Characterises the observational state as one scalar; narrows §25's headline.`

**Added at §27:** *the dial, not the semicircle; and the fisheye is a flat capacity projected* — earns the exact quantile identity ($10^{-16}$), the derivation of $K = \pi\rho_0$ from the dial's circumference, $s_{\max} = 2K/\pi$ verified to $8\times10^{-13}$, and $2/\pi$ read as chord-over-arc of the home-to-horizon span. It **corrects §26's picture**, **retires a contested assertion** by deriving it, and makes $2/\pi$ operational for the first time. `Passes. The fare contract is derived; its domain is corrected at §31.2.`

**Added at §26:** *line → semicircle → hemisphere* — earns arc-length-equals-measure to $10^{-16}$, a **forcing argument** for the semicircle (homogeneity + closure, with the radius fixed), the $\mathbb{RP}^n$ hemisphere ladder tabulated, $H^2$ geodesics to $10^{-8}$, the flat per-rung toll (needle and disc identical in $\mathbb{R}^3$), and the **display-versus-structure split** — addition dies at the first step up and returns only at $n=3$. It also **separates two semicircles the corpus had conflated**. `Passes. The ladder is confirmed; the display/structure split is the limit on it.`

**Added at §25.8:** *the Cauchy is primary and the circle is secondary* — earns the uniqueness of the invariant measure (three starting densities all flowing to it), the **selection** argument (mass escapes under both non-compact subgroups, so the circle is discovered rather than imported), $\pi$ from the home normalisation with no circle mentioned, and the standpoint↔Cauchy correspondence by independent Brownian exit. It **corrects §25.4's stated order**, **closes last section's three-routes audit item** by showing the closure route is §4 made precise rather than a rival, and **narrows §25's own headline**: $2/\pi$ is a projection toll, $\pi$ is not. `Passes. Corrects §25.4's stated order and narrows §25's headline.`

**Added at §25:** *π is the price of expressing a 1D line in 2D space* — earns chord/arc identified with mean projection to $10^{-14}$, the projection ladder $2/\pi \to 1/2 \to 4/(3\pi)$ showing $2/\pi$ is dimension-specific rather than universal, Buffon at $2\times10^7$ needles, $\mathrm{vol}(\mathbb{RP}^1) = \pi$ exactly, and the group law residual at $4\times10^{-16}$. It **supersedes its own first framing** — the curvature-meter account is demoted to a corollary — and it **supplies the Dimensional Projection Theorem's missing proof**. `Passes. Narrowed at §25.8 and again at §28; see those entries for what survives.`

Twenty-three of thirty earn numbers (§35 is a ledger and claims none). Four earn routes. One repairs a standing objection. One dissolves a tension. One removes a contradiction. One scopes an over-claim. One is decoration. One is retired. That ratio should be stated in any version of this that goes outside, because the failure mode of a rich metaphor is that everything starts looking like everything, and the only defence is to keep asking what each identification bought.

---

---

## Appendix — executed checks

`balance_checks.py`, all passing.

- **B1** — composition across alias families; max error $2.2\times10^{-14}$ (impedance), $8.9\times10^{-14}$ (weights), $1.0\times10^{-11}$ (odds), $1.3\times10^{-12}$ (intensity), over $2\times10^5$ random triples each. Fisher-$z$ negative control: $r_{13}$ bounded to $[-0.393, 0.993]$ where the law would give $0.846$.
- **B2** — Thomas/Wigner angle against the hyperbolic angular defect; identical to $10^{-16}$ at five rapidity pairs spanning $0.05$ to $2.0$.
- **B3** — ambient vs intrinsic midpoint on $K = +1, 0, -1$; flat exactly zero at every separation, curved opening as $Kd^2$.
- **B4** — dumbbell centre-of-mass vs centre-of-gravity gap against $L^2/2R$; agreement to four figures by $R/L = 200$.

`curvature_meter.py` (§25.1), all passing.

- **N1** — chord/arc against $1 - (\kappa s)^2/24$; deviation $5.2\times10^{-4}$ at $\theta = 1$, falling as $\theta^4$.
- **N2** — landmarks as exact geometric states: corner $= 1.000000000$ (straight), $2/\pi = 0.636619772$ (half turn), horizon $= 0$ (closed).
- **N3** — range of $v/h$ over the opening arc $= [0.000000, 1.000000]$, monotone decreasing.
- **N4** — $R$-cancellation: $0.931056009$ identical at $R = 0.1, 1.0, 17.0, 10^6$.
- **N5** — deficit $\times$ excess $= 1.000000000$; the two-leg identity only (cf. §19).

`dimension_price.py` (§25.2–25.5), all passing.

- **P1** — chord/arc against mean cosine over the arc; identical to $10^{-14}$ at $\theta = 0.3, 1.0, \pi, 4.0, 2\pi$.
- **P2** — $\mathbb{E}|u\cdot e|$ by ambient dimension, closed form against $4\times10^6$-sample Monte Carlo: $2/\pi$, $1/2$, $4/(3\pi)$, $3/8$, $16/(15\pi)$ at $n = 2\dots6$.
- **P3** — Buffon, $2\times10^7$ needles: $0.636664$ against $2/\pi = 0.636620$, error $4.4\times10^{-5}$.
- **P4** — $\int dr/(1+r^2) = \pi$ to machine zero by quadrature; $\mathrm{vol}(\mathbb{RP}^n) = \mathrm{vol}(S^n)/2$ tabulated, $\pi$ alone only at $n=1$. *(Superseded a trapezoid-on-$\tan$-grid attempt returning $3.758$ — see §25.6.)*
- **P5** — $\tan$(uniform angle) against Cauchy, KS $p = 0.24$ at $2\times10^6$ samples.
- **P6** — $\chi(\mathbb{RP}^n)$ obstruction table; $\arctan$ conjugation of ratio-addition to $+$ mod $\pi$, max residual $4.4\times10^{-16}$.

`cauchy_primary.py` + `c5_fix.py` (§25.8), all passing.

- **C1** — Cauchy invariant under the elliptic subgroup acting on slopes; KS $p = 0.41, 0.20, 0.30$ at $t = 0.3, 1.0, 2.5$. Student-$t$ controls ($\nu = 0.5, 2, 4$) destroyed by the same flow, $p = 0$.
- **C2** — no finite invariant measure under the other two subgroups: median $|s|$ runs $0.996 \to 20.03$ (parabolic) and $0.996 \to 4.8\times10^{8}$ (hyperbolic).
- **C3** — home normalisation $\rho(0) = 1$ gives total mass $3.141592653590$.
- **C4** — orbit-averaging Student-$t(3)$, Normal, Uniform$[-5,5]$ all give Cauchy; $p = 0.28, 0.52, 0.98$.
- **C5** — harmonic measure by Brownian exit (walk-on-spheres, $2\times10^5$ paths, Cauchy formula not used in the computation) is Cauchy$(x,y)$ at four standpoints; medians and half-IQRs recover $x$ and $y$ to three figures, KS $p = 0.99, 0.45, 0.23, 0.96$. *(Superseded a first version that compared Cauchy$(x,y)$ to itself — a tautology, caught by four identical $p$-values.)*
- **C6** — chart change in both directions: $\tan$(uniform) $\to$ Cauchy $p = 0.21$; $\arctan$(Cauchy) $\to$ uniform $p = 0.44$.

`ladder.py` (§26), all passing.

- **L1** — measure of a slope interval against arc length of its $\theta$ image; agreement to $10^{-16}$ at four intervals including $[2, 10^6]$.
- **L1b** — elliptic flow acts on $\theta$ by translation, max residual $4.4\times10^{-16}$ at three $t$; constant-curvature forcing argument follows.
- **L2** — $\mathrm{vol}(\mathbb{RP}^n) = \mathrm{vol}(S^n)/2$ tabulated as hemisphere volumes, $n = 1\dots4$.
- **L3** — $H^2$ geodesic length by numerical arc integration against $\operatorname{arccosh}$ formula, three point-pairs, agreement to $10^{-8}$; straight-line comparison longer in every case.
- **L4** — projection toll by ambient dimension: needle in $\mathbb{R}^{2,3,4}$ and disc in $\mathbb{R}^3$; the disc matches the needle at $0.500080$ vs $0.499941$.
- **L5** — $\chi(\mathbb{RP}^n)$ group obstruction across the ladder rungs.

`dial.py` (§27), all passing.

- **D1** — closed curve of length $\pi$ has radius $\tfrac12$; home-to-horizon dial distance $= \pi/2$.
- **D2** — $v = \sin\theta$ is the chord from home; chord/arc at the horizon $= 0.636619772 = 2/\pi$ exactly.
- **D3** — $F(s_j) = (j+\tfrac12)/K$ to $1.1\times10^{-16}$ at $K = 7, 64, 1024$: the dial atoms are the Cauchy quantile grid. *(Replaced a KS test returning $p = 1.0000$ — see §27.7.)*
- **D4** — measured atom density against $(K/\pi)/(1+s^2)$ at four reads; $\rho_0 = K/\pi$, hence $K = \pi\rho_0$.
- **D5** — $s_{\max} = \cot(\pi/2K)$ against $2K/\pi$; relative error $1.3\times10^{-2}$ at $K=8$ falling to $8.2\times10^{-13}$ at $K=10^6$.
- **D6** — constant dial gap $0.003067962$ against read gaps $0.003068 \to 434.600121$ at $K = 1024$.

`tangent_density.py` (§28), all passing.

- **E1** — gnomonic projection onto the tangent line at home against $\tan\theta$; agreement to $10^{-16}$ at four angles including $\theta = 1.5707$.
- **E2** — total measure $= \pi\rho_0$ at three scales; $199999.9993$ against $K = 200000$.
- **E3** — non-invariance demonstration: $(1+s^2)^{-0.9}$ and $(1+s^2)^{-1.1}$ both match at home and move under the elliptic flow; $(1+s^2)^{-1}$ does not. *Monte-Carlo, graded a demonstration.*
- **E4** — $\cot(1/2\rho_0)$ against $2\rho_0$ at four $\rho_0$; $199999.999998$ against $200000$ at $\rho_0 = 10^5$.
- **E5** — the $\pi$-audit table: four operational quantities $\pi$-free, four totals carrying $\pi$.
- **E6** — recentring at $s_0$; outside density $1, 0.5, 0.1$ against inside density $1$ at every standpoint.
- **E7** — dial gnomonic coordinate against $s/(1-s^2)$ at three $\theta$; the double-angle map, exact.

`options.py` + `options_fix.py` (§29), all passing.

- **F1** — $\det^2 + (a\cdot b)^2 - |a|^2|b|^2$, max residual $4.3\times10^{-14}$ over $2\times10^5$ pairs.
- **F2** — invariants preserved under rotation, max difference $8.9\times10^{-16}$ at three random angles.
- **F3** — quadrature sensitivity table; $|dp/d\Delta| = |c|$ and $|dc/d\Delta| = |p|$, crossing at $\pi/4$.
- **F4** — $\sigma$-scan at $\Delta = 10^{-4}$: project error tracks $\sqrt{2\sigma}$ ($0.0679$ vs $0.0677$ at $\sigma = 10^{-2}$), compare error linear; ratio $6.8 \to 7479.9$ over six decades. *(Replaced a single-$\sigma$ run misreported as a fixed $1000\times$ — see §29.8.)*
- **F5** — bisection on $\operatorname{sign}(\det)$ alone: one bit per step to exact at 60 steps. *(Re-run at a non-dyadic target; the first version used $\pi/4$.)*
- **F6** — mirror configurations: three scalar invariants identical, $\det$ opposite, sums $0$ to $10^{-16}$.

`single_number.py` (§30), all passing.

- **G1** — the counterexample class stated: counts and dimensionless numbers are reference-free single numbers. *A recorded refutation of a proposed claim, not a check.*
- **G2** — $h = \cos\theta = 1 \iff \theta = 0 \iff$ home; $s = v$ at home only, $0.309336$ vs $0.295520$ at $\theta = 0.3$.
- **G3** — measured atom spacing at home against $1/\rho_0$ at three scales; $0.000015708$ both at $\rho_0 = 63661.977$.
- **G4** — mirror invisibility of every scalar report including integer counts, across four configurations; only $\det$ flips sign.
- **G5** — $K$ required to hold the whole: $10^{19.3}$ at $64$ bits, $10^{301}$ at $1000$ bits.

`free_reads.py`, all passing (§14).

- **Q1** — boundary flux vs bulk sum; relative accuracy set by aperture $M$, flat across $N = 10 \to 20000$, best case $4.2\times10^{-10}$.
- **Q2** — distant single read at the centre of gravity; relative error $0.06\,(a/R)^2$, coefficient constant over $R/a = 10 \to 383$.
- **Q3** — entropy negative control; identical conserved totals, $4.2\times10^4\,k_B$ apart.
- **Q4** — Prüfer angle modulo $\pi$ against the continued value; residues near-identical while the winding integers differ (2, 3, 5, 7).

`curvature_q.py`, all passing (§15).

- **R1** — $\int_D K\,dA = -\oint \partial_n\varphi\,ds$ at five radii, agreement to $10^{-11}$.
- **R2** — a region nowhere flat ($K$ from $+11.3$ to $-10.0$) with enclosed curvature $-1.6\times10^{-11}$ and holonomy $-9.6\times10^{-18}$.
- **R6** — adiabatic invariant drift $4.5\times10^{-2} \to 3.4\times10^{-4}$ as the sweep lengthens by two decades.

`bertrand.py`, `bertrand2.py`, `bohlin.py`, all passing (§16).

- **S0** — apsidal angle vs eccentricity for five force laws; only $p=-2$ and $p=+1$ hold.
- **S1** — the linear family $p=n^2-3$; $n=1,2$ stable under deformation, $n\ge3$ drift two orders more.
- **S2** — the harmonic orbit satisfies $x(\theta+\pi) = -x(\theta)$ to $10^{-5}$; Kepler does not (ratio 0.36).
- **T1** — $w=z^2$ of a harmonic orbit fits a focused conic to $3.9\times10^{-14}$; the control fails by $2.4\times10^{-1}$.
- **T2** — $z$ and $-z$ map to one Kepler point to $1.7\times10^{-10}$.

`string_in_space.py`, all passing (§17).

- **U1** — wobble radius $m L/(M+m)$ at three mass ratios; 13 cm for a 5 kg weight on a 2 m rope.
- **U2** — zero-total-$L$ bookkeeping for a tethered astronaut; counter-spin $2.44\times$ the orbital rate.
- **U3** — tension $L^2/mr^3$ on reel-in: 5.4 N, 18 N, 147 N, 1174 N at 3, 2, 1, 0.5 m.
- **U4** — cut-string limit: tangential departure, spin retained, centre of mass unchanged.

`menu.py`, all passing (§18).

- **V1** — orientation measure in the slope chart, $\int ds/(1+s^2) = 3.141592654$.
- **V2** — one $2\pi$ walk of the hold wraps the read exactly twice.
- **V3** — $(2/\pi)\arctan S \to 1$ across twelve decades; the atom's quadrant is $\pi/2$.

`arbitrage.py`, all passing (§19).

- **W1** — bilateral inverses give $1.000000000000$ on two legs; three legs return $0.387$, $1.947$, $0.790$, $1.310$.
- **W2** — boost and inverse boost compose to the identity at $10^{-16}$; the three-leg residue matches the Wigner angle to $5.6\times10^{-17}$.
- **W3** — three-leg residue against hyperbolic triangle area, identical to nine figures at three rapidity pairs.

`finding_pi.py`, all passing (§20).

- **X1** — Vieta's product to $2/\pi$ using only $+$, $\times2$, $\div2$, $\sqrt{\ }$; error $1.1\times10^{-16}$ at 25 factors.
- **X2** — every factor identical to $\cos(\pi/2^n)$, difference exactly zero at $n = 2\ldots7$.
- **X3** — $\tan(\theta/2) = (\sqrt{1+t^2}-1)/t$ at four angles to twelve figures: halving in the arc is a root in the slope.
- **X4** — convergence at two digits per three halvings, $O(\log(1/\varepsilon))$.

`alignment.py`, all passing (§21).

- **Y1** — three-gap coverage under irrational stepping: exactly 3 distinct gaps at 10, 100, 1000, 10000 steps.
- **Y2** — step aligned to $\pi/n$ by sign test and halving alone, error $\le 2.2\times10^{-16}$ at $n = 2,3,5,8$.
- **Y3** — entrainment to an unknown period, one bit per trial: error $3.4\times10^{-13}$ after 41 trials.

`lifetime.py`, all passing (§21.6).

- **B1** — truncations of $2/\pi$ saturate at $q/\gcd(p,q)$: 100, 250, 5000, $10^6$, $2.5\times10^8$ addresses; exact value dense.
- **B2** — bits required $= \log_2 N$: 10 bits for $10^3$ acts, 30 for $10^9$, 57 for $10^{17}$.
- **B3** — bisection yields $\sim1.05$ bits per halving.
- **B4** — multiplicative compounding: $\delta = 10^{-3}$ gives $71\%$ error at $10^3$ conversions, $e^{1000}$ at $10^6$.

`two_budgets.py`, `two_budgets2.py`, `budget_is_cauchy.py`, all passing (§22, §23).

- **D2** — at $K=6$: unitary preserves the total at $1.000000000$; diagonal rescale $1.490973$; general real matrix $1.312007$.
- **E1** — uniform $S^d$ read as $v/h$: KS of $\arctan s_i$ against uniform, $6.5\times10^{-4}$, $4.4\times10^{-4}$, $6.4\times10^{-4}$ at $d=1,2,3$.
- **E3** — $d=3$ density profile $1.000, 0.640, 0.250, 0.040, 0.0015, 6\times10^{-6}$.
- **E4** — antipodal pairs land on identical reads, max difference exactly $0$.

`one_uniqueness.py`, all passing (§24).

- **V1** — rotating the hold maps the read by $(r+t)/(1-rt)$; max relative deviation $9.3\times10^{-12}$.
- **V2** — Cauchy invariant under random $SO(d+1)$ at $d=1,2,3$.
- **V3** — TV shift under one rotation: uniform $0.00179$, perturbed $0.33086$.
- **V4** — $O(2K)$ preserves the norm but $\|QJ-JQ\| = 4.29$; $U(K)$ needs the complex structure.
