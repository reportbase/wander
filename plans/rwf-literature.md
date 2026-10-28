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
  - Vol. 1, ch. 10 derives the Π theorem: the rank of the similarity group equals the number of independent units.
    This is the nearest formal counterpart to counting the amounts. **Check whether they state the count as such.**
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
- **Martens 2021, 2022** [secondary]: kinematic comparativism, a magnitude reported only relative to a standard. This
  is the nearest to "writing needs a standard carried in".
- Wolff 2020, *The Metaphysics of Quantities* [secondary].
- **Jalloh 2025**, *OSM* 14:91 [abstract]: the Π theorem's symmetries, not changes of unit, are the right
  rescalings. Must be engaged.
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
  body-scaled "π numbers" after Buckingham ([memory]; **check the term**).
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
- **Bridgman 1922**, "the absolute significance of relative magnitude" [secondary; **check the wording**].
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
