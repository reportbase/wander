# Prior work for "Observation from Somewhere": a literature search

*12 October 2026. Tom: "ok", to a search for prior statements of OFS's results, its address/payload reading above all.
Made by a fresh agent that read `papers/observation-from-somewhere.md` cold (as merged with PR #90) and searched the web.
**Every source below was seen only as a search result** (title, URL, abstract or summary): the proxy here blocks
arXiv, JSTOR, Wikipedia, Crossref and publishers' pages, so no full text was opened. Volume and page details come from
those abstracts and should be checked before they are cited. "Cited" means in OFS's References. Kept as the agent
returned it, its layout tidied; a note from Claude follows.*

---

## 1. Theorem 6, and its reading (§7.2)

- **Gull (1988)**, "Bayesian inductive inference and maximum entropy", in Erickson and Smith (eds), *Maximum Entropy
  and Bayesian Methods*, Kluwer, 53–74 (https://bayes.wustl.edu/sfg/gull.html). The source of the lighthouse problem,
  also told in Sivia's *Data Analysis*. A lamp flashes at evenly spread angles; the flashes land on the shore
  Cauchy-distributed, with scale the lamp's distance. The lesson taught: estimate from the median or the likelihood,
  never the mean. **Same pieces.** But the evenness here comes from the world, the case where OFS says "addresses"
  would be the wrong name. Not cited.
- **Jones (1999)**, "Distributional relationships arising from simple trigonometric formulas", *Am. Stat.* 53(2),
  99–102 (https://oro.open.ac.uk/23926); **Cacoullos (2014)**, "Polar angle tangent vectors follow Cauchy distributions
  under spherical symmetry", *JMVA* 128, 147–153 (https://ideas.repec.org/a/eee/jmvana/v128y2014icp147-153.html). The
  ratio of components of any spherically symmetric vector is Cauchy, because its direction is uniform and independent
  of its radius. **The same statement as 6(a)**: the radial law, OFS's reach ℓ, drops out. Not cited.
- **Stevens (1946)**, "On the theory of scales of measurement", *Science* 103, 677–680. Quoted in a search summary: the
  median keeps its place under every order-preserving transformation, while the mean stays the mean only under linear
  ones. **6(b) and (c) in words.** Not cited.
- **Frank and Smith (2010)**, "Measurement invariance, entropy, and probability", *Entropy* 12, 289–303
  (https://www.mdpi.com/1099-4300/12/3/289); Frank and Smith (2011), *J. Evol. Biol.* 24, 469–484
  (https://arxiv.org/pdf/1010.2267); **Frank (2014)**, "How to read probability distributions as statements about
  process", *Entropy* 16, 6059–6098 (https://arxiv.org/pdf/1409.5196).
  - Their claim: "the natural scaling of a measurement defines the most likely probability distribution".
  - A scale linear for small magnitudes and logarithmic for large ones gives Student's t, the Cauchy its k = 1 case.
  - **The closest reading found:** the distribution belongs to the observer's scale, not the process. The mechanism
    differs (maximum entropy, not cancellation) and there is no split between median and mean. Not cited.
- **Pillai and Meng (2016)**, "An unexpected encounter with Cauchy and Lévy", *Ann. Statist.* 44(5), 2089–2097
  (https://arxiv.org/pdf/1505.01957): Σ w_j X_j/Y_j is standard Cauchy for every covariance (via Williams 1969); the
  Cauchy survives whatever dependence the payload has. Related. Not cited.
- **Akaoka, Okamura and Otobe (2022)**, quasi-arithmetic means of Cauchy variates, *Braz. J. Probab. Stat.* 36(2)
  (projecteuclid.org). Those means exist and estimate the parameters: only the *arithmetic* mean is missing, which
  supports "the missing mean comes from the axis". For 6(c) the classical source is Kolmogorov and Nagumo (1930) on
  quasi-arithmetic means. Not cited.
- **What OFS adds:** each part of 6(a)–(d) is in print; their combination, and the naming of which reader receives the
  law, was not found.

## 2. Theorem 6(e): reciprocal symmetry

- **Seshadri (1965)**, "On random variables which have the same distribution as their reciprocals", *Canad. Math.
  Bull.* 8 (cambridge.org).
- **Jones (2008)**, "On reciprocal symmetry", *JSPI* 138, 3039–3043 (https://oro.open.ac.uk/22523). The standard name
  is **log-symmetry**: X and 1/X have one law exactly when log X is symmetric.
- **Cacoullos and Papadatos (2013)**, "Self-inverse and exchangeable random variables", *Stat. Prob. Lett.* 83, 9–12
  (https://arxiv.org/pdf/1204.1633): X/Y is self-inverse exactly when X and Y are, or can be chosen, exchangeable.
  **6(e)'s first half as a theorem.**
- **Vanegas and Paula (2016)**, "Log-symmetric distributions", *Braz. J. Probab. Stat.* 30(2), 196–220: in this family
  the scale parameter is the median.
- The wine/water paradox is the flip's own paradox, indifference over a ratio against indifference over its reciprocal:
  **Mikkelson (2004)**, "Dissolving the wine/water paradox", *BJPS* 55; **Burock (2005)** (philsci-archive 2487). It
  suits Proposition 2(b) and `papers/vantages.md`.
- **How close:** the same statements; none cited. That a 1/x tail leaves no mean is elementary.

## 3. Proposition 5(d), the ellipse

- **Jones (2008)**, "The distribution of the ratio X/Y for all centred elliptically symmetric distributions", *JMVA*
  99, 572–573 (https://oro.open.ac.uk/22514), with Cacoullos (2014): elliptical symmetry gives a general Cauchy, its
  scale set by the axes. **The forward half of 5(d).** Not cited.
- Nothing found on even steps along an ellipse's arc, or comparing the three kinds of "even". **What OFS adds:** the
  converse, that only c = 1 gives the flip-invariant law. Easy, but apparently new as stated.

## 4. §11.1, the invariance principle

- **Leonard (2011)**, "Estimating a bivariate linear relationship", *Bayesian Analysis* 6(4), 727–754
  (https://arxiv.org/pdf/1202.0957). A prior on a line's slope invariant under rotation must be the Cauchy (uniform in
  angle), and it is then invariant under exchanging and rescaling the coordinates: §11.1's turns, exchange and scale in
  a Bayesian setting. **Same pieces, the nearest match.** Not cited.
- **Jaynes (1973)**, "The well-posed problem", *Found. Phys.* 3, 477–493: transformation groups applied to Bertrand's
  chord. **Drory (2015)**, "Failure and uses of Jaynes' principle of transformation groups", *Found. Phys.*
  (https://arxiv.org/pdf/1503.09072): the same symmetries give different measures depending on how the random selection
  is made. **The strongest objection to OFS's open question 2, and should be answered.** Neither cited (OFS cites Jaynes
  1968 only).
- The Möbius side, beyond the cited Knight and McCullagh: Phillips (Cowles DP 887); Kato and McCullagh (2020),
  *Bernoulli* 26(4), 3224–3248; Letac (1977), "Which functions preserve Cauchy laws?", *PAMS* 67, 277–286; Mendonça and
  Lundell (2025), *Stat. Prob. Lett.* 222 (the Cauchy the only continuous family invariant under projective maps,
  applied to triangulation).
- **No "situated observer" derivation of both the Cauchy and the logarithm was found.**

## 5. Proposition 4, and the two address spaces

- Linear-then-logarithmic scales joined at a unit are common in practice:
  - **Lupton, Gunn and Szalay (1999)**, asinh magnitudes, *AJ* 118, 1406–1410 (astro-ph/9903081): y = asinh, joined at
    a softening parameter, OFS's Mercator form;
  - Parks, Roederer and Moore (2006), the "Logicle" display, *Cytometry A* 69, 541–551;
  - the mel scale, 2595·log₁₀(1 + f/700) (O'Shaughnessy 1987, after Koenig 1949);
  - Frank and Smith's linear-log scale (§1 above).
- The logarithm from scale invariance or optimality: **Koenderink (1984)**, "The structure of images", *Biol. Cybern.*
  50, 363–370; **Portugal and Svaiter (2011)**, *Minds and Machines* 21, 73–81 (the logarithmic scale minimizes the
  largest relative error).
- **How close:** the same shape, chosen for noise or range. None cited; only Schwartz is.
- **What OFS adds:** the join placed at the flip's fixed point with matched slope; not found elsewhere.

## 6. Proposition 13, the best estimate

- All standard, none cited: the posterior median as the Bayes estimate under absolute loss (Laplace); quantiles follow
  monotone maps (**Koenker and Bassett 1978**, "Regression quantiles", *Econometrica* 46, 33–50); the geometric mean of
  the bounds as the minimax estimate for ratio error (**Rall 1980**, MRC TSR 2098, after Olver's relative precision,
  *SIAM J. Numer. Anal.* 15 (1978), 368–393).
- **Caveat raised:** a note (arXiv 1004.0533, "Quantiles equivariance") says quantiles follow a map only under
  continuity conditions. Check the wording of 13(b).

## 7. Proposition 14 and measurement theory

- Luce (1959) is cited. **Aczél, Roberts and Rosenbaum (1986)** solved Luce's functional equation without regularity
  assumptions. **Narens (2002)**, *Theories of Meaningfulness*, includes a foundation for the Erlangen programme; see
  also Falmagne and Narens (1983), *Synthese*.
- **The no-corner point in measurement theory's terms** (the agent's reading, not a quotation): a statement is
  meaningful only if it survives every admissible transformation, so on a ratio scale "x = 1" is meaningless. That is
  OFS's no-corner claim; not found stated in those words.

## 8. The three vantages, and situated geometry

- **van Fraassen (2008)**, *Scientific Representation: Paradoxes of Perspective*, OUP: "indexicality enters
  irreducibly" into measurement. The nearest philosophical statement of OFS's thesis.
- Giere (2006), *Scientific Perspectivism*; Massimi (2022), *Perspectival Realism*; Gibson (1979), the optic array as
  solid angles at a point of observation; Luneburg (1947), visual space as hyperbolic. None cited.
- **No prior reading of π/2 and 2/π as vantages was found.**

## 9. Propositions 7–11

- Buckingham (1914), *Phys. Rev.* 4, 345–376 (dimensional analysis); Longuet-Higgins (1981), *Nature* 293, 133–135 (two
  views recover the scene up to scale: Proposition 11); Lee (1976), *Perception* 5, 437–459 (τ = x/ẋ: Proposition 9);
  Poincaré, *Science and Method*, "The relativity of space" (a universal doubling cannot be detected: Proposition 8(a);
  only the chapter title confirmed). None cited.
- **What OFS adds:** the ordering as a ladder of what each further standpoint buys; nothing new mathematically.

## Unconfirmed, from the agent's memory

Arnold and Brockett (1992), "On distributions whose component ratios are Cauchy", *Am. Stat.* 46 (high confidence);
Williams (1969), *Ann. Math. Stat.* 40, 1083–1085 (high); Aczél, Roberts and Rosenbaum (1986), *J. Math. Anal. Appl.*
119, 389–416 (medium-high); Suppes and Zinnes (1963), "Basic measurement theory" (high); Koenderink and van Doorn (2008,
2012) on visual and pictorial space (seen in a summary, no URL); Heelan (1983), *Space-Perception and the Philosophy of
Science* (medium); Hartley and Zisserman (2003); Bridgman (1922); Berger (1985) (high).

## The agent's verdict

**The address/payload reading of the Cauchy was not found anywhere.** No source treats the missing mean as a property
of the observer's addressing, or names an address/payload split. Its parts are all in print: the cancellation (Jones
1999; Cacoullos 2014), the order/sum asymmetry (Stevens 1946), distributions as the observer's measurement scale with
the Cauchy as a linear-log case (Frank and Smith 2010; Frank 2014, the closest prior reading), and the textbook instance
(Gull's lighthouse). The novelty is interpretive, as OFS claims; it should cite these so a reviewer sees the claim is the
combination. Most important to add: Stevens 1946; Jones 1999 and Cacoullos 2014 (and Jones 2008, *JMVA*); Frank and
Smith 2010 and Frank 2014, discussed, not just cited; Cacoullos and Papadatos 2013 and Jones 2008, *JSPI*; Leonard 2011,
with Jaynes 1973 and Drory 2015; Gull 1988; Lupton et al. 1999; van Fraassen 2008.

---

### Note (12 October, Claude)

- **13(b)'s wording holds.** For a strictly increasing f, f of a median of X is always a median of f(X):
  P(f(X) ≤ f(m)) = P(X ≤ m) ≥ ½ and likewise above. What can fail without continuity is the converse, that every median
  of f(X) is f of a median of X. OFS says "a median is f of a median", which is the safe direction.
- **The search confirms the paper's own framing**: the pieces are classical and cited as such; the reading is the
  contribution. The gap it exposes is in the References, which lack the closest prior statements of 6(a), 6(b)–(c) and
  6(e) and the nearest prior reading (Frank and Smith).
- **Drory (2015) bears on open question 2** and should be answered in OFS: the measure on directions depends on how the
  selection is made, which OFS concedes ("where the evenness comes from is a choice"); Theorem 6(e) is the reply, since
  the median at the corner and the missing mean do not depend on that choice.

### Cited (13 October; Tom: "ok, cite the prior work in OFS")

Each source was checked again before it was cited, by fresh searches: the publisher's or an index's record (DOI,
volume, pages) and its abstract. Full texts stayed out of reach (the proxy blocks arXiv and the publishers), so what each
is cited for rests on its abstract or on how later papers describe it.

| source | where in OFS | checked | corrections to the agent's report |
|---|---|---|---|
| Jones 1999, *Am. Stat.* 53(2), 99–102 | §7.8, 6(a) | DOI 10.1080/00031305.1999.10474439; abstract | none |
| Cacoullos 2014, *JMVA* 128, 147–153 | §7.8; Proposition 5(e) | DOI 10.1016/j.jmva.2014.03.010; abstract (the polar angle's tangent vector Cauchy under spherical symmetry) | none |
| Jones 2008a, *JMVA* 99(3), 572–573 | §7.8, 5(d) forward | DOI 10.1016/j.jmva.2006.05.001; listing | none |
| Stevens 1946, *Science* 103(2684), 677–680 | §7.8, 6(b)–(c) | secondary descriptions (the median for ordinal scales, not the mean) | none |
| Seshadri 1965, *Canad. Math. Bull.* 8, 819–824 | §7.8, 6(e) | Cambridge listing; reference in Cacoullos and Papadatos | the title has "reciprocal", singular |
| Jones 2008b, *JSPI* 138(10), 3039–3043 | §7.8, 6(e) | DOI 10.1016/j.jspi.2007.11.006; abstract (log-symmetry) | none |
| Cacoullos and Papadatos 2013, *SPL* 83(1), 9–12 | §7.8, 6(e) | DOI 10.1016/j.spl.2012.06.032; abstract | none |
| Gull 1988, in Erickson and Smith (eds), vol. 1, 53–74; Sivia and Skilling 2006 | §7.8, the lighthouse | Gull's list of papers; the lighthouse attributed to Gull by Sivia's presentation and later notes | the problem's text in Gull's chapter not seen |
| Frank and Smith 2010, *Entropy* 12(3), 289–303; Frank 2014, *Entropy* 16(11), 6059–6098 | §7.8, the nearest reading | DOI 10.3390/e12030289; abstracts | Smith is D. Eric Smith |
| Leonard 2011, *Bayesian Analysis* 6(4), 727–754 | §11.1 | DOI 10.1214/11-BA627; abstract (the slope's posterior unchanged by exchanging and rescaling); the `leiv` package's manual (the default prior the rotation-invariant Cauchy) | the author is David Leonard |
| Jaynes 1973, *Found. Phys.* 3(4), 477–493 | §11.1, §11.2 Q2 | DOI 10.1007/BF00709116 | the end page is 493 in most records, 492 in some |
| Drory 2015, *Found. Phys.* 45(4), 439–460 | §11.2 Q2, answered | DOI 10.1007/s10701-015-9876-7; arXiv abstract | the start page seen (439), the end page from memory |
| Lupton, Gunn and Szalay 1999, *AJ* 118(3), 1406–1410 | §11.3 | Princeton record; abstract | none |
| van Fraassen 2008, OUP | §11.3 | standard | none |
| Buckingham 1914, *Phys. Rev.* 4(4), 345–376 | §9, after Proposition 8 | standard | none |
| Lee 1976, *Perception* 5(4), 437–459 | §9, Proposition 9 | DOI 10.1068/p050437; abstract | none |
| Longuet-Higgins 1981, *Nature* 293, 133–135 | §9, Proposition 11 | DOI 10.1038/293133a0 | none |
| Aczél, Roberts and Rosenbaum 1986, *JMAA* 119, 389–416 | §9, Proposition 14 | F. S. Roberts's list of publications; a later review's description | cited only as treating the equations in general |

Not cited: Pillai and Meng 2016, Akaoka et al. 2022, Vanegas and Paula 2016, the wine/water papers, the Möbius papers
beyond Knight and McCullagh, Koenderink 1984, Portugal and Svaiter 2011, Koenker and Bassett 1978, Narens 2002, Giere,
Massimi, Gibson, Luneburg, Poincaré. They bear on the working papers more than on OFS's claims.

Drory answered in OFS §11.2, question 2: the selection (the even turn) is a choice, and symmetry alone does not make it;
the median at the corner survives any selection fair to the two parties, and the missing mean any such selection whose
weight does not vanish at the horizon (Theorem 6(e)). (*Corrected* 13 October: the first wording dropped the horizon
condition.)

## The hand as a teaching picture (19 Oct, SPN R391)

Tom (19:49 MDT): "find a paper that uses a metaphore like the hand and fingers to explain cauchy."

Five web searches, two of them in the perception literature, found no hand-and-fingers picture. Every classical teaching
picture found is the same one: something aimed at a uniform angle, with the spot where it lands on a straight line as
the variable.

- **A rotating needle,** its tangent projected onto a line: C. M. Cuadras, "Geometrical understanding of the Cauchy
  distribution", *Qüestiió* 26 (2002) 283–287 (raco.cat/index.php/Questiio/article/view/27030; EuDML 40380).
  - Elementary proofs of the Cauchy's properties from the circle.
  - Igelbrink and Wakolbinger (Mainz) answered its call for a geometric proof that the mean of tangents of uniform
    angles is again Cauchy.
  - The nearest paper built on a picture.
- **A flashlight** spun about its centre, one unit from a line: Larson and Odoni, *Urban Operations Research*, §3.3.3
  (MIT).
- **A light on a wall:** Siegrist, *Random Services*, the Cauchy distribution, X = a + b·tan Θ.
- **A ball kicked toward a wall:** Wikipedia. **A blindfolded archer:** R Views (2017). **A spotlight, with grazing
  beams for the tails:** QuantMemo.
- **Gull's lighthouse (1988),** the Bayesian case; already in OFS Proposition 5(f).
- **Perception:** none found that models a uniform turn of the eye or the hand as laying a Cauchy.
- **Directional statistics:** a circular and spherical projected Cauchy (arXiv 2302.02468) is the nearest family, not
  checked further.

In every picture found, the turn is the mechanism and the landing spot, a position on the line, is the variable: the
Cauchy as what arrives. The hand reverses this: the fingers (the turn's own addresses) are the variable, and what lands
on them, the rings, is the payload. That reading was not found.

Not a survey: it rests on web search results and the pages they returned. The full text of Cuadras could not be fetched
(raco.cat would not resolve).

### Pictures that keep the payload apart from the address (19 Oct, SPN R392)

Tom (19:55 MDT): "i'm am actually persuaded about the swapping idea, I know it works, but reality sweeps and doesnt use
arrays. keep on looking for any cauch metaphore that seperates the payload from the addres."

Three found, each classical, and each splitting what arrives into where (a law fixed by the standpoint alone) and what
(the values found there).

- **Kakutani's walker** (Kakutani 1944; Doyle and Snell, *Random Walks and Electric Networks*, 1984; Lawler's notes;
  the CMU walk-on-spheres lectures).
  - The value at a point (a temperature, a voltage, a payoff) is the average of the boundary's values, weighted by
    where a walker started there first reaches the boundary: u(x) = E[f(B_τ)].
  - The "where" is the harmonic measure, the Poisson kernel. From i over the half-plane it is the standard Cauchy,
    and on a circle the wrapped Cauchy (CMP C1 checked this through the conformal map).
  - The "what" is f, the boundary data, which the kernel never sees.
  - Here the kernel is the addresses, set by the standpoint and the shape alone, and f is the payload. Changing f
    changes no kernel: the swap, with a walk in place of an array.
  - The nearest match found. Not checked: whether any of these texts says the kernel is fixed while f is swapped.
- **Gull's lighthouse** (1988, in its classroom forms: Imperial's ICIC workshop, Heidelberg, Ohio State's Physics
  8820).
  - The detectors on the shore record only that a flash arrived and where, not its brightness or its direction.
  - The problem keeps the addresses and throws the payload away by construction; brightness plays no part.
- **Spectroscopy's strength × profile** (Townsend's line-profile notes; Hanson's EPS 238 notes; the Voigt literature).
  - A line is its strength, the integrated amount, times a profile of unit area. The Lorentzian is the profile.
  - Broadening reshapes the profile and leaves the strength alone; the strength scales the line and leaves the shape
    alone.
  - The payload is the strength, the address law the profile (OFS §7.2 already uses this split).

None of the three is put as "the Cauchy is the address, not the payload". Each carries the split in its equations and
its picture, unnamed. Searched, not surveyed.
