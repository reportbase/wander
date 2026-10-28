# Reading and writing: prior work

28 Oct 2026. Tom: "maybe the bigger idea is reader/writer framing not the cauchy mean", then "yes" to a prior-art
search before any outline. The search was made by a fresh agent from abstracts, search snippets, secondary sources
and its own knowledge. philsci-archive, sites.socsci.uci.edu and the Suppes corpus did not resolve from the session,
so **nothing here was read in full**. Each item is marked [abstract], [secondary] or [memory], and must be checked
before the paper cites it.

## The claim being checked

- **Reading.** A reader at a standpoint receives ratios only: directions, angles, ratios of lengths. Everything it
  reads is unchanged when the whole world, the reader's own sizes included, is scaled by k. Reading needs no unit.
- **Writing.** To state amounts (metres, a blueprint) a writer carries amounts in from outside: one for a lone
  reader, and one more for each further reader who must share the unit. The number is countable: the nullity in RWT,
  the rank in Buckingham's theorem.
- **Two tests.**
  - Scale the world: what is unchanged is a reading, what moves by k is a writing.
  - Change what arrives: what is unchanged is the address, what changes is the payload.
- **The geometry before any amount.** The uniform turn's measure is the Cauchy, with its median at the corner.

## 1. Representational measurement theory: meaningfulness is invariance

- **Stevens 1946**, *Science* 103:677 [memory]. Scales are sorted by their admissible transformations. A statistic
  is permissible when it is invariant under them: the median on an ordinal scale, the mean only from interval up. The
  ratio scale's group x ↦ kx is exactly "scale the world".
- **Luce 1959**, *Psych. Rev.* 66:81 [secondary]. Ratio-scale variables under admissible rescalings force power laws.
  The later criticism matters here: a constant that carries units frees the possible forms, and such a constant is an
  amount carried in.
- **Krantz, Luce, Suppes and Tversky 1971–1990**, *Foundations of Measurement* [memory].
  - Meaningfulness is invariance under the structure's automorphisms (vol. 3, ch. 22).
  - Vol. 1, ch. 10 (pp. 454–544) represents the quantities as a finite-dimensional multiplicative vector space with a
    basis, one free change of unit per basis dimension, and derives the Π theorem (§10.3). The wording "the number of
    units is the rank" was **not** found in it (checked, below); it is the textbook form of the Π theorem (Langhaar 1962).
- **Narens 2002**, *Theories of Meaningfulness* [secondary]. Meaningfulness becomes a primitive; Klein's Erlangen
  programme is generalized to families of groups.
- **Falmagne and Narens 1983**, *Synthese* 55:287 [abstract]. Meaningful laws, and "order-meaningful" laws (close to
  OFS Theorem 6(c)).
- Roberts 1979; Ellis 1966 [memory]: textbooks; dimensional constants as convention.

**Verdict.** "A reading is what survives rescaling" is classical meaningfulness, and the paper must say so. Not found
in this tradition:
- the standpoint;
- reading and writing as two acts;
- a count per observer.

## 2. Philosophy of physics: the undetectable rescaling

- **Leibniz–Clarke 1715–16; Poincaré 1908**, *Science and Method*, "The relativity of space": "suppose that in one
  night all the dimensions of the universe became a thousand times larger". This is the canonical "scale the world" and
  must be cited.
- **Dasgupta 2013**, *Oxford Studies in Metaphysics* 8 [secondary]: absolute magnitudes are undetectable, so
  comparativism.
- **Roberts 2008**, *BJPS* 59:143 [secondary]: a quantity that varies under the laws' symmetries is unmeasurable.
- **Baker 2020**, *OSM* 12 [abstract]: the cost of comparativism (indeterminism).
- **Martens 2021, 2022** [read: preprints]: kinematic comparativism, a magnitude reported only relative to a standard
  (quoted below). This is the nearest to "writing needs a standard carried in".
- Wolff 2020, *The Metaphysics of Quantities* [secondary].
- **Jalloh 2025**, *OSM* 14:91–130 [read: preprint]: the symmetries the Π theorem defines (active transformations of
  quantities leaving the Π terms unchanged), not the old argument's doubling of every mass, are the empirical
  symmetries; changes of unit are passive and accepted by all. Must be engaged.
- **Barbour 2003; Barbour, Koslowski and Mercati 2014**, shape dynamics [secondary]: only shape is physical. One
  non-shape degree of freedom had to be put back to match the data, a parallel to the one amount carried in.
- **Duff, Okun and Veneziano 2002**, *JHEP* 03:023 [abstract]: the trialogue on how many dimensional constants there
  are (3, 2, 0). A physics-level count of the amounts.

**Verdict.** The undetectability is well established. It is framed as metaphysics or as detectability under the
laws, never as what a situated reader reads against what a writer states.

## 3. Perception

- **Gibson 1979** [memory]: invariants of the optic array; the horizon ratio.
- **Sedgwick 1973, 1986** [secondary]: eye height as the scale (OFS cites Sedgwick 2021).
- **Warren 1984**, *JEP:HPP* 10:683 [abstract]: climbability is riser over leg length, 0.88 for short and tall alike;
  body-scaled "π numbers" (0.88 checked; the term seen only in a textbook quoting him, "after Buckingham" not seen).
- **Mark 1987** [abstract]: eye-height-scaled affordances.
- **Lee 1976** [secondary]: tau, time to contact with no distance or speed. A reading.
- **Bingham 2005**, *Ecological Psychology* 17:193 [abstract]: "in optical patterns, spatial metrics are absent";
  most solutions to the scaling problem add one dimension of the body or its movement. Must cite.
- **Proffitt and Linkenauger 2013** [secondary]: optic flow specifies "unit-less aspects", form and depth order;
  size needs "the body … as perceptual rulers". This is nearly the reader/writer split, in perception's words. Must cite.
- Klatzky 1998; O'Keefe and Nadel 1978 [abstract/memory]: egocentric and allocentric frames. These concern origin
  and orientation, not size; useful only for the vocabulary of standpoint.

**Verdict.** "Angles give form free; one body ruler gives the metric" is established (Bingham, Proffitt). Not found:
a general count, or one per further observer.

## 4. Computer vision and robotics

- **Triggs, McLauchlan, Hartley and Fitzgibbon 2000**, "Bundle adjustment — a modern synthesis" [secondary]: the
  seven-dimensional gauge freedom (3 translation, 3 rotation, 1 scale) is the cost's null space; fixing it fixes a
  datum. This is the counted form, and close to RWT's nullity.
- McLauchlan 2000 on gauge independence [title only]; Hartley and Zisserman 2003 [memory].
- Koenderink and van Doorn 1991; Belhumeur, Kriegman and Yuille 1999 [secondary]: ambiguities beyond scale.
- Monocular SLAM scale drift: Strasdat, Montiel and Davison 2010 [memory]; metric scale needs a further sensor.
  Civera et al. 2008 is already cited in OFS.

**Verdict.** Gauge counting is the engineering form of "count the amounts". Not found: a statement that generalizes
it across fields, or ties it to reading and writing.

## 5. Dimensional analysis and metrology

- **Buckingham 1914** [memory]: the number of π groups is n − r.
- **Bridgman 1922**, "the absolute significance of relative magnitude" [read: quoted below].
- Barenblatt 1996 [memory]; Sterrett 2009, 2017 [abstract]: similarity is "always relative to some system
  behaviour".
- Tal 2013; Chang 2004 [abstract/memory]: how a unit is fixed by agreement (the corpus's "interaction").
- "Only dimensionless combinations are measurable": Duff 2002; Uzan 2003 [memory].

**Verdict.** Textbook. The corpus's BPI run already maps π groups onto the wedge's directions. What is new is only the
reading per observer.

## What is known, and what was not found

**Known**
1. Invariance under rescaling as the criterion of meaningfulness. Order statistics survive every increasing map.
2. A universal rescaling cannot be detected, so only ratios are read.
3. Only dimensionless groups are observable, and the rank counts the independent units.
4. Angles give form and order; one body dimension gives the scale.
5. Reconstruction from bearings is up to a similarity, and the gauge is a counted null space.
6. Shape is the quotient by similarities (Kendall 1984).
7. Invariant measures from groups (Jaynes 1968), the anchor already.

**Not found** (in abstracts and snippets; full texts unread)
- One test, "scale the world", applied across surveying, reconstruction, parallax, perception and Π theory as the
  boundary between a reading and a written amount. Each field has its own version.
- Reading and writing as two acts of one observer, writing defined by the amounts carried in.
- The count per observer: one for a lone reader, one more for each further reader who must share the unit.
- The second test, change what arrives: address against payload.
- The standpoint tied to the question of scale. The egocentric/allocentric literature is about origin and
  orientation.
- The geometry the reader has before any amount, the uniform turn's Cauchy as the measure of its addresses.

## What a reader/writer paper must cite and engage

1. Stevens 1946; Krantz et al.; Narens 2002. Concede that meaningfulness is theirs; claim the standpoint and the
   count.
2. Luce 1959 and Bridgman 1922: dimensional constants as amounts carried in.
3. Buckingham 1914 and Jalloh 2025.
4. Poincaré 1908, Dasgupta 2013 and Martens 2021/2022 (Baker 2020 for the cost).
5. Duff, Okun and Veneziano 2002.
6. Triggs et al. 2000 and Hartley and Zisserman 2003.
7. Bingham 2005, Warren 1984, Sedgwick, Proffitt.
8. Barbour's shape dynamics and Kendall 1984.

**Read in full before citing:**
- Narens 2002;
- Krantz et al. vol. 1, ch. 10, on whether the count of units is stated;
- Jalloh 2025, its final text;
- Martens' wording;
- Warren 1984, the term "π number";
- Bridgman's exact phrase.

The hosts that would not resolve can be added to the environment's network allow-list.

## Checked against the texts (28 Oct)

A second agent read what it could reach once the missing certificate was supplied (the scans and preprints are in the
scratchpad, not committed). What each item rests on now:

- **Bridgman 1922**, *Dimensional Analysis*, Yale, read in full (archive.org, 1922 edition). P. 18–19: "the ratio of
  the lengths of any two particular objects has an absolute significance independent of the size of the units." P. 20,
  first named as a requirement: "the requirement that the ratio be constant, or we may say the requirement of the
  absolute significance of relative magnitude, is essential to all the systems of measurement in scientific use." P. 73
  names it a principle: "the principle that the ratio of the measures of two concrete examples shall be independent of
  the size of the units." **Confirmed.**
- **Poincaré [1914]**, *Science and Method*, tr. Maitland, Nelson, Book II ch. I, pp. 94–95, read in full: "Suppose
  that in one night all the dimensions of the universe became a thousand times larger. … I shall not notice anything at
  all. The most exact measures will be incapable of revealing anything of this tremendous change, since the
  yard-measures I shall use will have varied in exactly the same proportions." He credits Delbeuf, and adds that
  "my distance from the Pantheon will be equal to the same number of times the length of my body": the body as the
  unit carried in. **Confirmed.**
- **Martens**, "The (un)detectability of absolute Newtonian masses", *Synthese* 198(3):2511–2550 (2021, online 2019),
  and "Machian comparativism about mass", *BJPS* 73(2):325–349 (2022, online 2019), preprints read: "Kinematic
  Comparativism: For any dimensionful determinable, such as mass, the magnitude predicated of any particle can only be
  reported or expressed, non-dynamically, in terms of how this magnitude relates to the magnitude of another particle
  having the same determinable property." And: "A unit is thus merely a relation—to a standard reference body … in
  disguise." He keeps it apart from metaphysical comparativism. Cite the *Synthese* paper for the definition.
  **Confirmed; dates fixed.**
- **Jalloh**, "The Π-theorem as a guide to quantity symmetries and the argument against absolutism", *Oxford Studies
  in Metaphysics* (eds. Bennett and Zimmerman), OUP 2025, pp. 91–130, doi:10.1093/9780198952763.003.0005 (volume 14
  from a snippet only). Preprint read. Unit changes are "representational symmetries accepted by all parties"; the
  Π-defined ones are "unit-independent, ontic symmetries … the class of non-trivial empirical symmetries"; the absolutist
  can reject the amended argument only by "constant necessitism". **Thesis corrected** (it was "Π symmetries, not
  unit changes").
- **Narens**: his own papers read (the encyclopedia draft with Luce, *JMP* 46:746 (2002), the 1987 New Palgrave entry),
  and Suppes's review of the 2002 book (*JMP* 50:421, 2006); the book itself not. "An n-ary relation R on X is said to
  be qualitatively meaningful if and only if it is invariant under the symmetries of X"; automorphism against
  endomorphism invariance; the 2002 book adds meaningfulness as a primitive and families of structures. **No observer,
  standpoint or perspective anywhere in them.** Confirmed; the standpoint is ours.
- **Krantz, Luce, Suppes and Tversky** vol. 1 ch. 10: only search-inside snippets of a lending copy. The vector space
  with a basis and the Π theorem (§10.3, "Similarities", p. 464) are there; "rank", "n − r" and "independent
  dimensionless" returned nothing. **Not verified**; cite them for the structure and the theorem, not for the wording
  of the count, until the book is read.
- **Warren 1984**, *JEP:HPP* 10(5):683–703, doi:10.1037/0096-1523.10.5.683: R/L = 0.88 for short and tall climbers,
  confirmed from his dissertation abstract; "π number" seen only in Gordon's *Theories of Visual Perception* quoting
  him; "after Buckingham" not seen. **Partly verified.**
- **Bingham 2005**, "Allometry and space perception: compression of optical ground texture yields decreasing ability
  to resolve differences in spatial scale", *Ecological Psychology* 17(3–4):193–204,
  doi:10.1080/10407413.2005.9652817. The author's PDF serves the wrong certificate; **the two quotations above are
  not verified**, only the citation.

Still to read before the paper quotes them: Krantz et al. vol. 1 ch. 10, Narens 2002, Warren 1984, Bingham 2005,
Proffitt and Linkenauger 2013. A library copy, or files Tom adds to the session.
