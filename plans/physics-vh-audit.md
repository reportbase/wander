# The physics correspondences, audited for H/h and V/v (9 October 2026)

Tom, 9 October: "the physics correspondance is a seperate issue. we need to revisit the physics to make sure that it is not making the same conflations of H and h and V and v."; "geometry is v and h. physics is V and H." A first pass by Claude (a subagent, spot-checked by hand). A reading, not a ruling; every rewording is a suggestion; line numbers as of commit 81aca37.

# Physics correspondence: audit for H/h and V/v conflations (read-only, 9 Oct 2026)

Types: (1) h for H, or the reverse · (2) v for a distance, size or amount, or V for a fill level · (3) "corner" for a scale (an amount) · (4) H compared with V, or V needed for the corner · (5) the sweep (fractions) mixed with the reading (amounts).

All rewordings are **suggestions**. Lab rules apply. Predictions and recorded runs (labs.html notes "written before the run", grn-plan.md below its "Runs" line) must not be rewritten. For those, add a dated terminology note ("read 'the corner' here as one step across, the resolution limit; h here is H") and leave the record as it is.

## Summary

**Counts (instances grouped into findings):**

| file | (1) | (2) | (3) | (4) | (5) |
|---|---|---|---|---|---|
| papers/serial-parallel-nowhere.md | 4 | 3 | ~20 (12 findings) | 2 | 3 |
| plans/grn-plan.md | ~12 | ~8 | ~60 | – | – |
| plans/neighbours.md | 4 | 1 | 3 | – | – |
| labs.html | – | – | ~14 (OLB, LAD, BAL, guide comment) | – | – |
| world.js | – | – | 1 | – | – |
| thin.html | – | ~15 (v = distance throughout) | 7 | – | – |
| ladder.html | – | – | ~9 (incl. hook key `corners`) | 2 | – |
| sky.html | – | 3 | 1 | – | – |
| play-points / play-resolve | – | 1 (code var) | 1 / 2 | – | – |
| play-ladder / play-sky | clean | clean | clean | – | – |
| dial.html | ~8 ("h dial", "pixels h wide") | – | ~12 | – | – |
| sphere.html | ~5 ("reader holding h"; v, h, f called breadths) | (fill levels called breadths) | – | – | – |
| demos.html | 4 | 1 | 6 | 1 | – |

**Most consequential findings**

1. **SPN central result, "The corner is where the resolved becomes the unresolved" (l. 277–290)**, type 3. The paragraph says the distance where a thing is one address across "is the corner, s = 1, read physically, and it is why the corner is the reader's and not the world's." That distance is an amount, Δ/(d·ε) = 1, so it cannot be the scale-free corner h = v. The argument that "the corner is the reader's" therefore rests on the conflation. What the paragraph actually shows: **the resolution limit (one step across) is the reader's**. The physics (1/d², GRN run 8's slopes, OLB run 5, LAD run 3) is unaffected.
2. **SPN §3.3 "The law has no corner" (l. 2370–2376)**, type 3. "The corner is the reader's: it comes from the step, H". The scale-free corner cannot come from a scale. Suggest: "*The law has no scale.* … the reader's step brings one: the resolution limit."
3. **SPN §14 "light has a corner too" (l. 4705–4710)**, type 3. The open question, whether "the corner is the reader's" should read "the corner is the smallest unit's", goes away once both are named as what they are: the resolution limit (one step across) and the photon limit (a few quanta). Neither is the corner.
4. **plans/grn-plan.md l. 12 (the definition)**, types 1, 2 and 3 at the root: "Let the reader's grain be h … and the system's apparent size v (its extent over its distance)", with s = v/h and "the corner" at s = 1. Every GRN "corner" (about 60 uses), and dial.html and demos.html after it, inherit this. s is size/step, an amount ratio. Its s = 1 is "one step across".
5. **dial.html and demos.html: "the h dial", "pixels h wide"**, type 1. Tom's own request, quoted at dial.html l. 10, is "the idea that **H** could be optimized … adjust his unit". The dial turns H, not h.
6. **SPN §3.3 "Smaller drives less detailed" (l. 2331–2349)**. "(GRN: pixels h wide)" is type 1. "the single unit that also forces V = H" is type 4. "the in-place sweep's halving past the corner (¾, ⅞, 15/16)" is type 5: it equates halvings of the size Δ/d with the sweep's fractions. "by 4 in two (v and v₂…)" is type 5.
7. **SPN "It is the inverse-square law" and "The same signal" (l. 2355, 2361–2368)**, types 5 and 4. "1/d² in two: the sphere's two parties besides H, V and V₂ … The exponent is the number of those parties", and "(two directions of reading, §1)". The parties of the relation (breadths) are given as the reason for the 2 in 1/d². The 2 comes from the two transverse dimensions of space, or the area of the sphere the signal crosses. Also "with the reader's corner between them" and "size over step = 1, GRN's corner" are type 3.
8. **thin.html (and sky.html)**, type 2. Distance is v throughout: the comment, "distance v", the readout "v = …", 1/v², 4πv², `?v=`. SPN's converted §3.3 already uses d.
9. **ladder.html and demos.html: "each one breadth read against another"**, type 4 in wording. Travel, width and distance are amounts, not H and V. "each giving out at its own corner" is type 3.
10. **labs.html OLB runs 4–5 and LAD run 3**, type 3. "d* … the reader's corner", "past the reader's corner" (about 8 times). These are records, so add a terminology note.

**What is fine (physics untouched).** The inverse-square law and its use as an input (SPN *Scope* says so plainly). `lightAt` = L·A/(4πd²). Flux conservation (d²·1/d² constant). Every number: GRN runs 3–8 (P = min(s,1), 1/s looks, 1 + s pixels, (1+s)·max(1,1/s) least at s = 1, log₂(1/s) looks, light^(−0.499), d* ∝ a^0.51 F₀^0.25), OLB run 4–5 shares and (d*/d)², LAD run 3's 0.05% at an eighth of an address, BAL's s²/π, thin/ladder/sky smoke values. The converted terms in SPN §3.3 "The governing account" (ε, Δ, d, n = Δ/(d·ε), "in a situated reader it is its unit H") are correct except for its "at the corner" (below). The phrase "the resolution limit" is already used at SPN l. 2373 and GRN run 7's table and is ready to adopt. play-ladder.html and play-sky.html are clean (D or d, pixel, 1/d²).

## Findings by file

### papers/serial-parallel-nowhere.md (the corpus's own prose unless marked)

- **l. 38–40** (opening note, *Corrected: not a request*): "past the corner a thing is read as Δ/d units of H". Type 3. *Suggest:* "past one step across (the resolution limit), a thing is read as Δ/d units of H".
- **l. 279–290** (central result): "The one scale is the reader's step, H" is fine. "That is the corner, s = 1, read physically, and it is why the corner is the reader's" is type 3. *Suggest:* "That is the resolution limit, one step across (Δ/(d·ε) = 1): a scale the reader brings, not the corner h = v, which has none." Also "distance costing twice past the corner", "the law goes on past the corner", "width giving out at the corner and light going on past it" are type 3. *Suggest:* "past the resolution limit", "width giving out at one address across". The entry's title is Tom-adjacent wording (his "this seems important" is a quote, but the title is Claude's), so suggest renaming it "The resolution limit is where the resolved becomes the unresolved".
- **l. 295** (*Scope*): "a corner appears in the reading where the law has none". Type 3. *Suggest:* "a scale appears in the reading where the law has none".
- **l. 662** and **l. 4712–4714**: "a step that is not square giving each direction its own corner". Type 3. *Suggest:* "its own resolution limit". The same §14 bullet's "whether v and v₂ share one level of detail" is type 5: level of detail belongs to the reading (step across each direction), not to the fill levels. *Suggest:* "whether the two directions of view share one step".
- **l. 2303, 2313** ("A recursion needs…" and "Level of detail puts…"): "its corner at 2ᵏh", "2ᵏh", "⌊log₂(v/h)⌋". Types 1 and 2 (h for the step H, v for a distance). *Suggest:* "2ᵏH", "⌊log₂(d/H)⌋", or keep the text and add an "(H, d since 9 October)" gloss in line with "H and h kept apart".
- **l. 2316–2318** (governing account): "resolved from k = 0, at the corner, where it is one address across (n = 1)". Type 3. *Suggest:* "from k = 0, at the resolution limit, where it is one address across".
- **l. 2324–2326** ("A sweep over the level of detail"): "near field, home to the corner … far field, past the corner". Tom's quote has no "corner". The corpus's gloss puts the sweep's marks on the level-of-detail reading, which is an amount. Types 3 and 5. *Suggest:* "near field, down to one step across … far field, past it".
- **l. 2331–2349** ("Smaller drives less detailed"): "(GRN: pixels h wide)" is type 1, *suggest* "pixels one step (H) wide". "which is the in-place sweep's halving past the corner (¾, ⅞, 15/16)" is type 5, *suggest* deleting it, or "which mirrors, but is not, the sweep's halving". "the single unit that also forces V = H" is type 4, *suggest* "the same H in both directions" (the conversion SPN itself prescribes at l. 566). "by 4 in two (v and v₂, …)" is type 5, *suggest* "by 4 in two directions of view".
- **l. 2355** ("each standpoint captures about 1/d² … (two directions of reading, §1)"). Type 5. *Suggest:* "(two directions across the line of sight)".
- **l. 2362–2368** (*It is the inverse-square law*): "the sphere's two parties besides H, V and V₂ … The exponent is the number of those parties" is types 5 and 4. *Suggest:* "the two directions across the line of sight; the exponent is the dimension of the sphere the signal crosses (Claude's reading, unruled)", with the parties dropped. "with the reader's corner between them" and "size over step = 1, GRN's corner" are type 3. *Suggest:* "with the resolution limit between them", "one step across (GRN's s = 1)".
- **l. 2370–2376** (*The law has no corner* and its *Qualified*). See consequential finding 2. Tom's quote ("does not account for the corner?") stays as he wrote it. *Suggest* adding a gloss: "what he asked about is the resolution limit". Also "a corner on the signal's side" is type 3, *suggest* "a limit on the signal's side, the photon limit".
- **l. 2414** ("In SPN's terms the request is the reader's step, the h it holds"). Type 1. *Suggest:* "the H it holds" (record passage, so a gloss is enough).
- **l. 375–386** (After WHY2): "a reader that cannot know where its corner is", "below the corner", "luck below the corner". Type 3. WHY2's s is size/step too. *Suggest:* "where one step across falls", "below one step across".
- **l. 1209–1211**: GRN's "certain from s = 1" is offered as support for "only the side below" the corner. Type 3 (s is size/step).
- **l. 4705–4723** (§14, from the demos and labs of 9 October). The four bullets use "past the reader's corner", "two corners combine", "the corner is where reading stops being easy", "Most of a sky is past the corner". All type 3. *Suggest:* "past the resolution limit", "the resolution limit and the photon limit combine", "the resolution limit is where reading stops being easy", "Most of a sky is past the resolution limit". The open question in the first bullet can be closed as dissolved.
- **Older, for a ruling (3 Oct material, §3.2 "Physics has the same structure", l. 1849–1912; the COR rows l. 1866–1879; BAL row l. 4014).** h and v are taken as physical amounts: s = a/d for the disc; "h = λ/2π … s = h/r"; "h = √(λL) … v = a"; "Taken as h"; "Parallax against the grain … s = 1, a shift of one address". These are types 1, 2 and 3. The results hold as statements about a dimensionless ratio of two amounts equal to 1. Whether that point is "the corner" now needs Tom's ruling under "Rulings on V and h under review". Flag it there, not as an edit.

### plans/grn-plan.md (record: add a terminology note, do not edit)
- **l. 12–16** (claim): "the reader's grain be h", "apparent size v", "Below the corner, s = v/h < 1". Types 1, 2 and 3 at the source. *Suggested note at the top:* "Since 9 Oct: GRN's h is the reader's step (H, or ε), its v is a size over distance (Δ/d), and its s = Δ/(d·ε) is size against step. 'The corner, s = 1' throughout means one step across, the resolution limit, not h = v."
- Runs 4–6: "move its h", "h = 1, ½, ¼", "dial h", "s = 1/h", "starts at any h", "a fixed h" (~12). Type 1. Tom's quotes "move his h unit" (l. 167) and "H as a dial" (l. 221) stay as he wrote them. Note that he wrote H in the second.
- Run 8 (l. 366–419): "At distance v", "v*", "v₉₅", "1/v²". Type 2, distance. "the corner is the grain's" and "distance costs twice past the corner" are type 3.
- l. 260 (Claude, run 6): "knowing it would mean knowing v". Type 4: this ties the corner to knowing an amount. Under "v needs no V" the reader always has v. What it lacks is the size Δ/d.

### plans/neighbours.md
- l. 25–28 (Gilinsky): "with h = v_d", "the object is at v_d (the corner)", "plays the part of the reader's h". Types 1 and 3: v_d is a distance, a scale. *Suggest:* "v_d plays the part of a reader's unit H; z_p = v_d is where the normalised reading is ½".
- l. 40 (Schwartz): "with a as the corner". Type 3. *Suggest:* "with a as the switch scale".
- l. 52: "an offset v at distance h". Type 2. *Suggest:* "an offset x at distance d, at f·x/d".
- l. 57–58, 69, 78: "the reader's own h", "a reader's h", "a unit h", "SPN's h as the focus". Type 1. *Suggest:* H.

### labs.html (notes are records: add a terminology note)
- Type 3, about 14 instances: BAL l. 251 (prediction) and l. 1931 "the ball's corner is contact" (s = radius/distance = 1); BAL l. 271, OLB l. 1071 / 1073 / 1075 / 1087, LAD l. 931 / 935, guide comment l. 1553, run strings l. 5181 / 5441 / 5450: "the reader's corner", "past the corner", "d* … the reader's corner". *Suggest:* for the live strings and the comment, "past one cell across" or "the resolution limit"; for the notes, one dated terminology note.
- COR (l. 1293–1311, 6485–6674): "s = its own quantity over the world's", "s = r/(d·ε)". Same open item as SPN §3.2: leave it pending a ruling.

### world.js
- l. 230: "The law has no corner of its own; the reader's grain puts one in". Type 3. *Suggest:* "The law has no scale of its own; the reader's grain brings one (the resolution limit)". l. 228's "aperture A (its own unit)" is fine. `farnessAt(H, clock)` (l. 402) uses H for a history array. That is not wrong, but now that H means the reader's breadth it could mislead. Optional rename to `hist`, which needs a lab rerun per CLAUDE.md.

### thin.html
- Type 2, throughout: comment l. 14–20, "distance v" (l. 68), "1/v²" (l. 95, 223–224), "4πv²" (l. 101–102, 209–210), readout "v = …" (l. 218, 228), `?v=` and the code. *Suggest* d in visible text. Keep `?v=` as an alias, since the smoke test and CLAUDE.md use it.
- Type 3: l. 19 "the switch, at A = 1 … is the reader's grain" (fine) beside "has no corner of its own"; l. 63–64 "The switch is your corner"; l. 74 "at the corner (88.6)"; l. 96 "The dashed line is the corner"; l. 191 chart label 'corner'; l. 228 "The corner, one grain across". *Suggest:* "resolution limit" or "one grain across".

### ladder.html
- l. 12–13, 68–69: "each a reading of one breadth against another". Type 4 (and 2). *Suggest:* "each one length read against another".
- l. 13, 21, 23, 71, 100, 105, 187–190: "its own corner", "light's own corner", "past both corners". Type 3. *Suggest:* "its own limit", "the photon limit". Renaming the hook key `__ladder.corners` touches tests/smoke.mjs (optional).

### sky.html
- l. 14–15, 91: "fainter by 1/v² … numerous by v²", "growing as v²". Type 2, *suggest* d. l. 97: "past the reader's corner". Type 3.

### play pages
- play-points l. 60 "(the corner at one pixel across)"; play-resolve l. 16 "(the reader's corner: its size is now readable)", l. 70 "(the corner at one pixel)". Type 3. *Suggest:* "the resolution limit, one pixel across". play-resolve l. 124 `const v = +$('dist').value` is distance as v, code only. Minor.

### dial.html
- Type 1: title and h1 "The h dial", l. 14 "pixels are h wide", l. 15 and 62 "s = 1/h", l. 61 "pixels, h wide", l. 67 "dial h", l. 75 "slide h", l. 151 "pixel h =". *Suggest:* "The H dial", "pixels H wide", "s = 1/H" (state.h can stay internally). Tom's request at l. 10 already says H.
- Type 3: l. 16–20, 62–63, 87–88, 93–94, 99, 164 (chart label), 200, 242, 246: "below/at/past the corner", "the cheapest setting is the corner". *Suggest:* "below/at/past one pixel across". The finding "the cheapest setting is one pixel across, and the cost is the same at s and 1/s" stays.

### sphere.html (not physics, listed for completeness)
- l. 14, 71, 79, 105–106, 354: "Three breadths (v, h, f) in [0, 1]³, times a scale k". v, h and f range over [0, 1], so they are fill levels, not breadths. Types 1 and 2 inverted (lowercase fill levels called breadths). *Suggest:* "three fill levels (h, v, v₂ in SPN; v, h, f here)". The scale k is what drops out, which is the scale-free point. l. 21, 97, 140, 304: "a reader holding h". Type 1, *suggest* "holding H". The bandW pixel panel is fine.

### demos.html
- l. 79–83 (dial card): "The h dial", "pixels h wide" (type 1); "Below its corner", "from the corner on", "cheapest … at the corner", and the try links "below the corner / at the corner / past it" (type 3).
- l. 89–91 (sphere card): "Three breadths (v, h, f)", "a reader holding h". Type 1.
- l. 106, 108 (thin card): "The switch, at one grain across, is your corner; the law has none". Type 3, *suggest* "is your resolution limit; the law has no scale". Try link "at the corner".
- l. 114–116 (ladder card): "each one breadth read against another" (type 4); "give out at their corner" (type 3).
- l. 71 (sweep card): "Pairs (v, h), each divided by its own h". Not physics. Under the new terms the division is by H, or the pair is already fill levels. Leave it for the sweep review.

*Note, 9 October, after the audit was applied* (Tom: "in a way, any two points can have a sweep between the. sweeping from
point a to point b is itself a sweep."; SPN §1, "Every pair has its own sweep: name the pair"). Where this audit says a
point set by amounts is "not the corner", read: it is the corner of its own pair's sweep (a size against a step, a radius
against a distance), not the corner of the reader's sweep of the other. The error was the unnamed pair. The renamings
stand ("the resolution limit" is the physical name of the size-against-step corner).
