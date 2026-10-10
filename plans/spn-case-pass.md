# SPN, the equation-by-equation case pass (9 October 2026)

*Tom: "yes" to running it (SPN §14, "Burdens of proof", item 5). Four read-only readers, one per slice, checked every equation and symbol-bearing sentence against the 9 October rules (SPN's opening warning; §1, "Checking an argument"). A reading, not a ruling; line numbers as of commit 664741f. Findings are listed as returned; each is checked by hand before any edit.*

=== SLICE A (lines 1-952) ===
Audit of `/home/user/wander/papers/serial-parallel-nowhere.md`, lines 1–952. I edited nothing.

**CERTAIN**

1. **L120 (terms table) and L201 (dependency diagram):** "relation | two breadths, v and h" and "two breadths, v and h".
   - E1. v and h are fill levels, and breadths are H and V (L566–569).
   - Suggestion: "two fill levels, v and h (how much of V, how much of H)".

2. **L126:** "k = log₂(Δ/v), one level per doubling of distance".
   - E1. v is standing in for the distance d (the case L666 names, left unconverted). It is also a log of a size over a fill level (E4).
   - Suggestion: "k = log₂(Δ/(d·ε))", to match L297/L303.

3. **L456–459 (Abstract):** "the light reaching a reader from a glowing disc goes as s²/(1 + s²) … half its maximum at the corner, and the near law is the far law read through the inversion".
   - E2/E3. The disc's s = a/d is a ratio of amounts, and its s = 1 belongs to the radius-against-distance pair (L646). The Abstract leaves the pair unnamed and calls it "the corner".
   - L680 puts §3.2's version under review, but this copy carries no note.
   - Suggestion: "half its maximum where the radius equals the distance (the corner of that pair, §1 'Every pair…'; under review 9 October)".

4. **L662–669, contradictory conversion rule:** "Where earlier text says … '2h in place' … it means H", but L668 says "Relations between fill levels ('v from ½h to h', '2h in place', …) are geometry and stay as written".
   - E1, at the level of a definition. The same phrase is assigned to both cases.
   - Suggestion: drop "2h in place" from the list that means H, or say which reading holds.

5. **L856–861:** "V = H creates the reader's unit circle … That creates a unit circle, with its corner at s = 1 and its sweep: this is why g, the quarter turn, applies to a situated reader at all".
   - E3. It contradicts L749–750 ("V = H does not create the address space … holds no V") and L686–687 ("v needs no V"). It carries no correction mark.
   - Same passage, L860: "v is still unknown" is E1, since what is unknown is V.
   - Suggestion: mark it "*corrected 9 October*: the unit circle is fill levels; V = H only calibrates amounts", and write "V is still unknown".

6. **L878:** "h is what the reader holds (its unit, V = H), v what it reads against it".
   - E1. h is used as the unit H.
   - Suggestion: "H is what the reader holds (its unit); h and v are how full each side is".

7. **L893:** "One h means one step".
   - E1. A step is an amount (H or ε).
   - Suggestion: "One H (the reader's step) means …".

8. **L903–931, the wedge passage:** "a quarter-plane for two breadths", "A facing is a choice of the breadth to divide by: s = v/h", the table columns "two breadths / three breadths", "normalized by the largest breadth", and "Three breadths, as angles. v, h, f in [0, 1]".
   - E1. These are fill levels throughout.
   - Suggestion: replace "breadths" with "fill levels" or "shares" wherever v, h, f are meant.

9. **L467:** "3 and 4 can each be known approximately, v within bounds".
   - E1. v is always in [0, 1], so bounds on it say nothing; what is approximately known is V.
   - Suggestion: "V within bounds".

10. **L498 and L537:** "when nothing is known of v (the Cauchy family…)" and "a reader knowing nothing of v".
    - E1. By L686, the reader has v; what it lacks is V.
    - Suggestion: "nothing known of V".

11. **L946–948:** "divides (v by h, removing their common scale and leaving the relation) … points (each address reaches a magnitude, the scale the division took out)".
    - E1/E3. v and h are fill levels and have no common scale. Only amounts (v·V)/(h·H) carry one, and that scale is V/H, not removed by dividing v by h.
    - Suggestion: "divides (the amounts, leaving the fill levels' relation v/h)" and "the magnitude, v·V, needing V".

**POSSIBLE**

12. **L58 and L67 (opening notes):** "a thing is read as Δ/d units of H … its level of detail is log₂(Δ/d)" and "resolved to k = log₂(Δ/d) levels past one step across".
    - E4. Δ/d is an angle. It equals 1 at Δ = d, not at one step across. A count past the resolution limit needs ε: log₂(Δ/(d·ε)), as at L297.
    - Suggestion: use Δ/(d·ε).

13. **L301:** "The one scale is the reader's step, H (R176…)", while L297/L303 write the step as ε.
    - E1-adjacent. H (breadth) and ε (step) are used for the same thing within one paragraph.
    - Suggestion: "the reader's step, ε".

14. **L512:** "where v is a share of the known whole h".
    - E1. The known whole is H; h is a fill level of it.
    - Suggestion: "v counted in h, the known whole being H".

15. **L474:** "Past the corner, a value is in terms of v's unknown breadth, so in plain proportion it is undefined".
    - E3. The fill-level reading h/v is defined past the corner (L627). Only the amount needs V.
    - Suggestion: "its amount is in terms of V, unknown; the fill-level reading is defined".

16. **L846–848:** "It does have a corner, v = h at 45°, computed from the known breadths".
    - E3. h = v is geometry and needs no breadth (L691). Only its amount, V/H, is computed from the breadths (L853–855).
    - Suggestion: "its amounts there computed from the known breadths".

17. **L330–333 (the hypothesis as promoted):** "whose H is half of the level it lives in", "doubling its H", "the same object at a smaller h", "carry only its own H".
    - E1. H and h are mixed across consecutive bullets, and "H is half of the level" equates an amount with half of the fill-level 2h. "Kept as written" is a record note, not a correction note.

18. **L430 and L432:** candidates (a) and (b) use h for the level, (c) uses H; "What h is not… It is the side whose breadth the reader knows".
    - E1. The side whose breadth is known is H; h is how full it is.

19. **L888–891:** "holds H and reads v and v₂ against it", followed by "f = s/2 … (f₁, f₂) … far walls the edges f = 1".
    - E1. Fill levels are read against h, not H.
    - The letter f is used here for the in-place address, but L885 says f means v₂. That is a symbol clash.

20. **L931:** "A situated reader with three directions has V = H = F".
    - E1. F is undefined, since f is v₂.
    - Suggestion: "V = V₂ = H".

21. **L904:** "the length along it is the scale the division takes out".
    - E3. Along a ray of fill levels the length is fill, not a physical scale.

22. **L140–143 and L159–163 ("By the corner" prose):** "A situated reader approaches the corner and never locates it…" and "What the reader cannot do is identify the moment s = 1".
    - L695 says these are withdrawn and "marked where it stands". Only L138 and the table cells carry the mark; this prose has none of its own.

About 80 equations and symbol-bearing statements checked in lines 1–952.

=== SLICE B (lines 953-1944) ===
**Findings in SPN §2 (lines 953–1944)**

**Certain**

1. **L1155–1157** "**h is the known side by definition** … v arrives, but has no baseline of its own … It cannot be normalised, since one side is unknown". E1: h stands for H (the known breadth), and "baseline" is V. The "cannot be normalised" clause also contradicts the 9 Oct note at L1130, which says each fill level is normalised by its own breadth. Suggestion: "H is the known breadth … V has no known value … the amounts cannot be normalised together."

2. **L1183–1184** "v and h are held as two breadths at right angles". E1. Suggestion: "V and H are held as two breadths; v and h, their fill levels, at right angles."

3. **L1222** "the first cut is whether v is known. Known (with h): situation 1 if the breadths are equal". E1, and L1222 falls outside the 9 Oct note at L1001–1002, which covers only L992 and L1006. Suggestion: "whether V is known. Known (with H) …"

4. **L1230–1233** "The true corner, where V equals H, needs V … they approach it … never reach it … In 1 and 2 … the two corners are one". E2/E3: the corner is h = v. This is the very claim withdrawn at L1440, but no note sits on this paragraph. Suggestion: add a "withdrawn 9 Oct" pointer, or reword to "V = H is the placeholder, not a corner".

5. **L1241 and L1248** "the reader's reference, the magnitude it measures against"; "a lens behaves as a reader whose h is its focal length". E1/E2: h becomes an amount. In the same passage, L1243–1244 uses v as the image distance and f as the focal length, both colliding with the fill-level symbols. Suggestion: "the reader's H, the magnitude it measures against"; "a reader whose H is its focal length"; rename the image distance (u, w′) and the focal length (F).

6. **L1272** "its unit 1 known (h), its size unknown (v's breadth)". E1. Suggestion: "(H) … (V)".

7. **L1277** "A perturbation is v over the unit H". E1/E4: a fill level divided by an amount. Suggestion: "V over the unit H", or "v over h".

8. **L1284–1285** "with v the depth (the perturbation …) and h the unit (… the unit circle's radius)". E1: amounts given to fill levels. Suggestion: "v the fill level of the depth V; h of the unit H".

9. **L1323–1324 and table L1329–1330** "Dividing both by h sends any system (h, v) to (1, v/h) … whatever its scale … the scale is gone"; "needs: h only / h and v both". E1/E2: a system with a scale is (H, V), and L1332 then says "divide by H". Suggestion: "system (H, V) ↦ (1, V/H)"; "needs H only / H and V both".

10. **L1403–1404** "Dividing by h removes the scale and leaves a relation, s = v/h". E1/E2: a fill ratio has no scale to remove; dividing by H does. Suggestion: "Dividing by H removes the scale … the fill ratio v/h is the address."

11. **L1444–1447** "A reader that does not know v … it must hold the line, which is v. So above the corner v is known, at the corner v = h is known … Situation 3 does not know v". E1: "knowing v" means knowing V. This is 9 Oct text with no correction mark. Suggestion: "does not know V"; "at the corner h = v (a fill relation, known to every reader)".

12. **L1543** "(its breadths besides h)". E1. Suggestion: "besides H".

13. **L1666** "Through any middle breadth m, v/h = (v/m)·(m/h)". E1/E4: a breadth chained with fill levels. Suggestion: "any middle fill level m", or the same chain written in amounts, V/H = (V/M)(M/H).

14. **L1672–1674** "Hold the corner, v·h = 1 (the hyperbola …) … (h, v) ↦ (h/√c, √c·v)". E4 (domain): with fill levels in [0, 1], v·h = 1 holds only at (1, 1). Suggestion: write the hyperbola in unbounded coordinates (e.g. x·y = 1, with y/x = s) or in amounts.

15. **L1756–1758** "With h fixed at 1, v climbs … g = π/2 needs v unbounded". E4 (domain): a fill level is never unbounded; s = v/h is. Suggestion: "needs s = v/h unbounded". The L1767 revision fixes the angles only, not this.

16. **L1820 (heading)** "v approximately known", while the body says "V is known within bounds". E1. Suggestion: "V approximately known".

17. **L1834–1835 and L1841** "With nothing known of v"; "a reader that knows nothing of v". E1. Suggestion: "of V".

18. **L1867 (column) and L1878** "middle of v/h" equals b; "reads b from the middle of its arrivals". E2: ellipse readings normalised by their own breadths have middle v/h = 1, so this ratio is the amount ratio V/H, numerically equal only under H = 1. Suggestion: "middle of (v·V)/(h·H)", or "of V/H, with H = 1".

19. **L1889–1890** "once v is counted in a unit of 2ᵏh". E1: an amount in a unit built from a fill level. Suggestion: "once V is counted in a unit of 2ᵏH".

20. **L1900–1901 and table L1905** "stretched in v by b, the readings are v/h = b times the circle's: a Cauchy of scale b"; "rung of v/h". E2: §2.2 itself (L1849) puts scale V/H only in amounts. Suggestion: "(v·V)/(h·H) = b·(v/h)"; "rung of the amount ratio".

21. **L1919** "Opening divides v by h, so a size common to both cancels". E1/E2: fill levels carry no size. Suggestion: "divides V by H".

22. **L1940–1941** "with a placeholder for v … follow an address in terms of h". E1. Suggestion: "for V … in terms of H".

**Possible**

23. **L1095–1097** "whether v's far end is known … in 1 and 2, v is known". E1 (V intended). L1095–1096 "v is counted in h's" is fine.

24. **L1102** "a reader that knows only h cannot tell it from scale". E1 (H).

25. **L1143** "The 1 is the normalisation of two breadths known and equal". This repeats what the L1130 note corrects (equality is not what allows normalising). E3.

26. **L1147–1148** "no single 1 serves both h and v". E1: H and V are meant.

27. **L1151 and L1282** "r(θ) = (1 − m)·1 + m·B(θ)". E4: the dimensionless 1 is added to the breadth B(θ) unless B is normalised. Suggestion: "B(θ)/H".

28. **L1530, L1533, L1535** "pairs (v, h), magnitudes", "triples (h, v, w)", "|v|/|h|"; also **L1578 and L1589–1590** "whose h has always been positive", "signed v and h". E1: the data's amounts and signs are given to fill levels. Suggestion: (V, H) for the data's amounts; signs belong to the facing.

29. **L1480** "closes on the breadth it cannot hold". E3: the line the turn approaches is not V.

30. **L1772–1774** "dividing one by the other leaves a ratio with no scale, which is a direction". E2: an amount ratio laid on a sweep without naming the pair.

31. **L1657** "where one breadth dominates" (h or v alone). E1, minor.

32. **L1816 and L1893** (not E1–E4): "Neither breadth known" and "with H lost too" contradict the table at L985, "H known (H is always H)".

Equations checked: about 75 (formulas, relations and symbol-bearing table headers across L953–1944).

=== SLICE C (lines 1945-3550) ===
Slice 1945–3550 (§3–§4) of `/home/user/wander/papers/serial-parallel-nowhere.md`: 32 findings, 16 certain and 16 possible. Notes dated 9 October cover a good deal of the slice, but several passages after those notes still contradict them.

**CERTAIN**

1. **L1978 vs L1984 (E1).** The statement of Prop 3.1 says "found with h alone", but proof step (5) says "made with H alone: it needs neither V nor an outside unit". v = h is a relation between two fill levels and needs neither breadth. *Suggestion:* "(5) s = 1 is v = h, two fill levels; it needs neither H nor V."
2. **L1997–1998 (E1).** "To know v = h exactly is to know V." Knowing that two fill levels are equal needs no breadth. The *Withdrawn, 9 October* note at L1993 sits before this paragraph and may be meant for it, but as placed it does not clearly cover it. *Suggestion:* move that note below this paragraph, or mark this paragraph withdrawn too.
3. **L2044 (E1).** "Its knowledge does not: h is known and v is not." Knowledge is held of breadths, not fill levels. *Suggestion:* "H is known and V is not."
4. **L2054–2056 (E1).** "the registers are s and 1/s in the reader's unit H … invert at your unit". s = v/h has no scale and no unit. *Suggestion:* "invert at s = 1, the corner".
5. **L2112–2126 (E2).** The disc's s = a/d, a ratio of two amounts, is placed on "the corner", "the front side" and "the back side" without naming the pair. It is also called "the v of the circle's representative pair". The note at L2143 names the pairs only for the COR cases that follow it. *Suggestion:* extend the L2143 note to this passage, and drop "the v of …" or write "the disc pair's own sweep".
6. **L2187–2189 (E3/E1).** "what is measured against changes, from the known H to the unknown V … Expressed in the reader's own unit, H, the inverted reading is the count of doublings". This contradicts the *Resolved, 9 October* note at L2198–2209, which says H stands in for V on both sides and the change of register is the flip's (geometry). The count of doublings is in fill levels. *Suggestion:* "what changes is which part is the whole (the flip); the inverted reading counts doublings of v/h."
7. **L2232–2234 and L2308–2309 (E3).** "What v's unknown breadth takes away past the corner is only which doubling a reading is in" and "V is unknown, so which level a reading is in has to be counted". L2203 says the levels are geometry and untouched by V. *Suggestion:* attribute the counting to the flip and the levels (geometry). V's effect is only the constant offset of log₂(V/H) on amounts.
8. **L2567 (E1).** "at every distance from 4 to 128 h". A distance is an amount. *Suggestion:* "4 to 128 steps" (as in the quotation at L2509), or "H".
9. **L2609–2612 (E2).** "reads level k directly, 2ᵏh, as a float's exponent". This ties the level-of-detail index, which L2621 defines from amounts (n = Δ/(d·ε)), to the sweep's level at v/h = 2ᵏ. *Suggestion:* "reads level k directly, n = 2ᵏ addresses across".
10. **L2865–2876, railway ties (E2/E1).** "reads half-gauge ÷ d. Every tie farther than half a gauge reads less than one h: the front side … between the corner and home … infinite distance lands at reading 0". A ratio of two amounts is put on the reader's sweep, and L3243–3244 itself says this ratio has "no rung at all". *Suggestion:* "reads less than 1 on the half-gauge/distance pair's own sweep", and name that pair.
11. **L2909–2911 (E1).** "the share is h/v, with V one factor in it". h/v is a ratio of fill levels and V does not enter it. *Suggestion:* "the amount ratio (h·H)/(v·V) carries V/H as one factor; the share h/v does not."
12. **L2916–2918 (E3/E1).** "since v is a part of the known whole h … the register changes at the corner because the unknown begins there". The *re-sourced* note at L2887–2889 says the unknown b = V/H is the same on both sides and the register change is the flip's. That note covers only "the proposition below", not this paragraph. *Suggestion:* add a 9 October note, or rewrite as "the register changes at the corner by the flip (Prop 3.2(a))".
13. **L3054–3058 (E1).** "Counted with v in a unit of 2ᵏh … counts v in a unit 2ᵏ times h's". Changing the unit is a change of breadth. *Suggestion:* "counting V in a unit of 2ᵏH".
14. **L3158–3167, Prop 3.6 (E1).** "h is a reader's known breadth … s = v/h for an extent v of the world … m = log₂(h′/h)". The statement says "unit H … λH" but the proof says "λv/(λh) = v/h". *Suggestion:* use H, H′ and an extent X throughout: X/H = λX/(λH).
15. **L3176–3177, L3184–3195, L3197–3199 (E1).** Prop 3.7's proof says "None mentions h except through s". Prop 3.8 uses "units h and 2ᵐh", "[0, 2ᵐh]" and "s′ = v/(2ᵐh)", and L3198 has "a reader at 2h". These are units, so breadths. *Suggestion:* H and 2ᵐH for the units; keep h only where fill levels are compared.
16. **L3236 (E1/E4).** "log₂(L/h) doublings". L is a size, an amount, divided by a fill level. *Suggestion:* log₂(L/H).

**POSSIBLE**

17. **L1966–1967 (E1/E3).** "it is where v equals whatever the reader counts as one, and it goes wherever the unit goes". This suggests the corner moves with H, but h = v has no scale.
18. **L2004, L2326, L2947 (E1).** "the known whole (v < h)", "a share of the known h", "the known whole h". The known whole is H; h is a fill level. *Suggestion:* "the share of h".
19. **L2145 (E2).** "the corner … appears where a reader's own quantity meets the world's". The note at L2143 says these are the pairs' corners, not the reader's sweep of the other. *Suggestion:* "each pair's corner".
20. **L2150–2151 (E2).** Of the "22 where a reader's own quantity meets the world's", 11 are put "within an octave of the corner … the reader's octave with two facings". These are ratios of amounts, but the text calls the octave the reader's and names no pair. There is no terminology note.
21. **L2171 (E1).** "v = a, the opening's radius". The note at L2160 covers only "taken as h"; v is used here as an amount too.
22. **L2166 (E1, symbol clash).** "|H|² ∝ s⁴ + s²" uses H for the magnetic field. *Suggestion:* write |B|², or rename it.
23. **L2179 (E3).** "the wavelength … it is the unit". The corner has no unit; the wavelength is one party of that pair.
24. **L2618–2621 (E4).** ε is set equal to "its unit H" (a breadth), and then n = Δ/(d·ε). Δ/d is a pure ratio (an angle), so n is a count only if ε is an angular step or H = 1 numerically. *Suggestion:* define ε as an angle, or write n = Δ/(d·ε) with ε = H/D for a stated D.
25. **L2634–2636 (E1/E4).** "read as Δ/d units of H … so that is Δ/d addresses too". The two are equal only when H = 1 numerically, which is the conflation the rules warn about.
26. **L2639 (E3).** "They coincide because one H is both the reader's ruler and its step". This claims the halving of amounts coincides with the halving of fill levels, but no bridge (v·V with V known) is named.
27. **L2989–2991 (E1).** "g = 0 … no V expressed; g = 1 … V fully expressed". g is geometry. *Suggestion:* "v empty / v full" (Tom's quoted "breadth" can stay).
28. **L3003 (E1).** "the bar's own H and v". The cases are mixed. *Suggestion:* "h and v".
29. **L3103 (E1).** "the front side is laid in plain proportion, one step H/N". The front side is laid in fill levels. *Suggestion:* h/N, or state the bridge.
30. **L3354–3356 and L3395–3396 (E1/E3).** "keeps v as a magnitude only on the front side … Past the corner there is no baseline for a magnitude (R158)" and "magnitudes stop there". This conflicts with R158 as resolved on 9 October: the baseline is H standing in for V on both sides.
31. **L3147–3148 and L3405 (E2).** "the middle settles at b" and "reads a shape's breadth ratio" b = V/H from the readings of v/h. A distribution of fill ratios is read as an amount ratio, and the bridge is not named.
32. **L3532–3533, L3545 (E1).** "Up to it the reading is a plain share of one h", where c is an amount, and "What the fisheye withholds is v's baseline" (that is V). *Suggestion:* "of one unit c (H)" and "V, v's breadth".

Checked: about 145 equations, formulas and symbol-bearing statements across L1945–3550.

=== SLICE D (lines 3551-5635) ===
**SPN audit, lines 3551–5635 (read-only, no files edited).**

**CERTAIN**

1. **L3802–3803, E1.** "from 4 h to 128 h"; "At 128 h". These are distances counted in the reader's breadth, so the symbol should be H. L3799 in the same set-up says "how many of its own H's". *Suggestion:* "4 H to 128 H", "At 128 H".
2. **L3849, L3855–3859, E1.** "the reader stands at h above the line … Every reader holds the same h"; "period 16 h", "period 4 h", "17 h for the 16 h sine, 4.9 h … 1.9 h", "the same h". These are heights and lengths, so they are amounts. *Suggestion:* use H throughout SIG.
3. **L3915–3916, E1.** "a reading passes as v in agreed units, s_A·h_A = s_B·h_B". Agreed units are physics, and s·h is a fill level, not an amount. *Suggestion:* "passes as an amount in agreed units, s_A·H_A = s_B·H_B (each H in the agreed unit, under each reader's V = H)".
4. **L4209–4211, E1/E2.** "The left is a relation, v the world's magnitude and h the reader's own travel … through a v/h whose h is the reader's own step". The left side is d₀/|b|, a ratio of two amounts, and here it is read as the reader's fill ratio. *Suggestion:* "The left is a ratio of two amounts in one unit, d₀ the world's distance and |b| the reader's own travel (a named pair, not the reader's v/h) … through d₀/|b|".
5. **L3648, E2.** "(h/v rather than v/h)". Nearness is D1/d, an amount ratio, and the text identifies it with a fill ratio. *Suggestion:* "(D1/d rather than d/D1)".
6. **L4008, E2/E3.** "What D1 does is place the reader's corner: it decides which things are in contact (d ≤ D1)". d = D1 is a point set by amounts, which makes it the corner of the pair (d, D1), not the reader's corner h = v. *Suggestion:* "place the corner of the depth pair (d against D1)".
7. **L4381 (NWH row), E1.** "at one breadth, the reader's own H; below h the unsituated view is finer". *Suggestion:* "below H".
8. **L4382 (LIN row), E1/E4.** "a line at h"; "by the bar's own H and v"; "depth × h = 1". The case is mixed: an amount (depth) times a fill level is set equal to an amount. *Suggestion:* "a line at distance H"; "by the bar's own h and v"; "depth × h = H (= 1 under the placeholder)".
9. **L4387 (OCT row), E1.** "proportion to h, then levels". This is the depth lay, whose step is H/N (CAR row L4380, L4887). *Suggestion:* "proportion to H".
10. **L4934–4935, E1.** "with the wave's own size as h". A wavelength is an amount. *Suggestion:* "as the unit of the named pair (aperture or distance against wavelength)".
11. **L5039, E1.** "proportion up to h …; the parts tying h to the familiar range untested". This is a child's counting range on a 0–100 line, so it is an amount. *Suggestion:* use H.
12. **L5389 (kill log), E1.** "at 16 h every family scores flat"; "Both readers know depth relative to their h". *Suggestion:* "16 H"; "relative to their H".
13. **L5562–5569, E3 (unnamed bridge).** "the reader counting v in its own H … with the reader's H as a measure every split is definable … proportional in h's up to the corner … a reader counting in its own unit". The in-place lay is geometry (v counted in h's). Naming H or a unit as its measure makes the ratio 2 rest on a physical breadth without naming the bridge. *Suggestion:* "counting v in h's (geometry; in amounts, V in H's only via v·V, h·H under V = H)", and "with the count in h's as a measure".

**POSSIBLE**

14. **L3656, E2.** "d/D1 is a reading like s, so what §3.3 built on s carries over without a new step". This is acceptable only as its own named pair. *Suggestion:* add "on its own sweep (the pair d, D1), not the reader's s = v/h". The same applies to "Its corner is the reader's unit D1" (L3637) and "its corner where the world is" (L3964).
15. **L4212–4213, E2/E3.** "the corner of Proposition 5.2, 'the reader's own unit', is the distance equal to the reader's own step". *Suggestion:* "the corner of the pair (d, |b|)". The line also cites the withdrawn lay d = D1·tan ψ (see L3639).
16. **L3799 and L5388, E1.** "v is withheld"; "so v was not withheld". What is withheld is the other's amount (V or d). *Suggestion:* "V (the distance) is withheld" (leave Tom's quote as it stands).
17. **L4010–4011, E3.** "the corner falls where n · step = 1". This is a point set by amounts. *Suggestion:* "the front side ends (the pair's corner) where n·step = H".
18. **L3913 and L3919, E3.** "a corner would be one reader's unit"; "past the corner people switch to rulers that count levels". These read the corner as a unit or amount. *Suggestion:* "a unit would favour one reader"; "past the reader's unit".
19. **L4165–4166, E1.** "h and v as magnitudes". These are the components of the unit pair, not amounts. *Suggestion:* "h and v, the unit pair's components".
20. **L4242, E1.** "how its own H runs across the addresses". This is the body's surface coordinate, which the same cell and L4287 write as h. *Suggestion:* "its own h". The same cell's "R = s u − m w" reuses s, the paper's v/h, so a rename such as σ would avoid the clash.
21. **L3846, E1.** "the signs of the tangent's h and v". These are signed components, and fill levels carry no sign. *Suggestion:* "the tangent's two components".
22. **L5040, E2.** "Of the powers of s/√(1 + s²) …". The near/far laws use each law's own amount ratio (a/d, ω/ω₀, …), so each pair should be named. *Suggestion:* "s here each law's named pair, not the reader's v/h".
23. **L5451 and L5455, E1/E3.** "h only sets the units"; "the reader holds its unit (V = H)". This is a physics placeholder inside a geometric inventory. *Suggestion:* "H only sets the units (physics; the stack itself needs no unit)".
24. **L5086, E4.** "log₂(Δ/(d·ε)) are ratios of amounts in one unit". That holds only if ε is an angular step, in which case this is a ratio of two angles (Δ/d against ε). *Suggestion:* say so.
25. **L4873, E4 (minor).** "a constant step in s, h/C". In s the step is 1/C; h/C is the step in v. *Suggestion:* "a constant step in v, h/C (1/C in s)".
26. **L5408, E1.** "The longest hidden stretch is the reader's 2h". A landscape stretch is an amount. *Suggestion:* "2H".
27. **L4018 (minor clash).** "Kept to d digits" uses d, which the paper reserves for distance. *Suggestion:* "k digits".

**Equations checked:** about 95 (Propositions 5.1–5.4, 8.1, 9.2, 9.6, 9.8, D.1; Corollary 9.3; the ρ forms; the depth flips; the lab-table formulas; Appendix D's lay table; the §14 forms).
