# The rulings on V and h, reviewed (9 October 2026)

Tom, 9 October: "we have to rethink all rulings related to V and h." A first pass by Claude (a subagent, checked in part by hand): each ruling sorted as A (unaffected), B (notation only) or C (substance). A reading, not a ruling; line numbers are SPN's as of commit f66ca94.

# Rulings on V and h: review against H/V (breadths) and h/v (fill levels)

SPN = papers/serial-parallel-nowhere.md. Line numbers are SPN's. No repository file was edited.

## Summary

- **Appendix A** has 118 entries. 53 have no h/v/H/V, corner, horizon, breadth or situated content and are left out. Of the other 65: **A 45, B 15, C 5**.
- **In-text dated rulings by Tom** (opening, §§1–3): **A about 31, B 14, C 13**. The two rulings already withdrawn are not counted.

**One issue cuts across the whole review.** Under the new terms, v is "how much of V". In situations 3 and 4, V is not known, so a situated reader cannot form v. Every reading SPN gives a situated reader (s = v/h, "v reaches one h", "v counted in h's") is really **d/H**: a distance or extent counted in the reader's own unit. That makes two different "corners":
- **(i) the fill corner, h = v.** It is the middle of the sweep whatever V is (Prop. 3.2(b), R162, R149).
- **(ii) the unit point, d = H.** It needs only H.

Most B items are (ii) written as v/h. The C items are those that tie either corner to knowing V. (Suggestion: Tom should rule which of the two a situated reader reads, and whether "a reader holding only H can place [the fill corner]" (§1, l.549) means (i) or (ii).)

**The most consequential C items:**
1. **The standing table (l.245) and the dependency diagram (l.196)** list "the corner approached, never found" as **proved**. It rests on the withdrawn §3.1 ruling and the 6 Oct horizon ruling.
2. **"The horizon of a situated reader" (6 Oct, l.1165)** mixes up two different 1s. θ/sin θ and sin θ/θ tend to 1 as the turn shrinks (θ → 0, toward home), but the corner s = 1 sits at θ = 45°, where they read 1.11 and 0.90. Its "true corner … never found" fails on that alone, apart from V.
3. **R158 (l.4865; §3.3 l.1920)**: "values beyond the corner are in terms of the unknown breadth of V". It carries §3.4's Proposition 3.4 setup, §4.1, §13 (l.4490) and R163's gloss.
4. **R137 / "Known breadths, and the corner" (l.967) / the situations table (l.745) / R134** separate situation 1 from 2 by whether V = H, which compares breadths.
5. **"By the corner" (l.120) and its landmark table (l.134).**
6. **"The quarter turn is Archimedes' proof made situated" (9 Oct, l.1242)**: "approaches the line, 1 (the corner), from below".
7. **"In 3 and 4 the corner is simply h" (l.979)**: the "true corner, where v's breadth equals h's" compares breadths.
8. **The lens correction (7 Oct, l.~1000)** demotes the lens to unsituated because it "reaches its corner". It rests on a withdrawn ruling.
9. **R154 / §4.5 (l.3195)**: "landmarks … only found in situation 3, with unknown breadth"; closure "both breadths known and equal".

## A. Unaffected

**Appendix A.**
- **Holds as written:** R37 (v, h "magnitudes on [0, 1]", which fits fill levels exactly), R77, R88, R89 ("a unit can just be you", which is H), R96, R118, R121, R122, R126, R127, R128 ("the breadth is unknown"), R129, R130, R131, R135 ("h breadth known, v breadth unknown", that is, H and V), R136, R138, R139, R140, R141, R145 ("only a common size cancels"), R146 ("h's breadth known", that is, H), R150, R151, R152, R153, R155, R159, R161, R162, R163, R165, R168, R170, R173, R174 ("if h = 0, that is a mathematical horizon": h empty, all of V, a fit), R180, R181, R182, R184.
- **Support the new reading:**
  - **R149** (l.4856): "although the breadth of V is not known, you do know the corner."
  - **R169** (l.4875): home is "all h, no v", the horizon "all v, no h", the corner h = v.
  - **R162**: fairness places the corner at ½ for any V.
- **With a caveat:**
  - **R160**: "the observer does not possess the world's breadth … The corner is where that construction changes regime" holds only if a reason other than R158's is found for the change at the corner.
  - **R164**: holds; its §3 gloss is B (below).
  - **R178**: h² + v² = 1 is the length-cut drawing (§1's table of cuts), not a breadth comparison.

**In-text.**
- **Holds as written:** Situated and unsituated (6 Oct); Geometry is compile time and its corrections (already in d and H); What a sweep is (all but one sentence, see C); The wedge is the primitive; Static and dynamic; A system can change kind; The circle needs no recursion; Angles; The situations restated; Mercator; Depth read against the sweep; π/2 every relation summed; The unit sweep repeated; How a reader tells facings apart; The first level is half the distance; One continuous sweep; A sweep is one hemisphere; Furthest from the line at the corner; The relation forces the logarithm; The situated reader's fisheye; The circle inverts v and h at 45°; the 6 Oct revision putting recursion only past the corner; No turning; Recursion, after the corner; Recursion rejected and the governing account of level of detail (already uses d and H); The same signal, a smaller share; Depth, the slider and the level of detail; The eye is engineering; Tom 1 Oct 21:14, "never arrives because it is the median" (§3.7, already scoped as ordinary sampling).
- **π/2 and 2/π, with 1 between them** (l.1251) holds, but "the corner is also 1" names a second 1. That coincidence is the source of C2.

## B. Notation only (rewording)

**Appendix A**

| Ruling | Key words | Rewording |
|---|---|---|
| R87 | "its corner at D1" | the forward reading's unit point, d = D1 |
| R132, R133 | "h is known, v unknown, expressed in terms of h"; "don't even need a v" | H known, V unknown; the other's extent d counted in H |
| R142 (l.4849; §2.2 l.1592) | "corner … middle of a lay only when the breadths are equal … middle at v/h = b" | the raw-equality point (v_raw = h_raw, i.e. d = H) is the middle only when V = H; the fill corner sits at v_raw/h_raw = V/H = b and is always the middle. The measurement stands, and it confirms the new definition. §2.2's "gap between the corner and the middle" becomes the gap between d = H and the fill corner. |
| R143, R144 | "read through situation 1's assumption"; "different corner position" | the reader takes H in both directions; the position meant is the d = H point |
| R147 | "say v is 2x h … slides the reading by whole rungs" | V = b·H slides d/H by log₂ b rungs; the fill relation does not move |
| R157 | "found with h alone" | the unit point is found with H alone; the fill corner needs no breadth at all |
| R167 | "v from half of h to all of h" | d from ½H to H |
| R172, R175 | "corners at 4ⁿh", "½h and 2h" | 4ⁿH, ½H, 2H |
| R176 | "one step h/N" | H/N |
| R177 | "proportion to its corner (h for breadth …)" | H for breadth |
| R179 | "corner, octaves and horizons come from its own h" | its own H |
| R183 | "h is the invariant … the octave is 2h" | H is the invariant; the level is 2H in place (matches Tom's 9 Oct "H … invariant") |

**In-text**

| Entry (line) | Rewording |
|---|---|
| Units (l.145) | "a doubling is v/h × 2", "corners at 2ⁿh": d/H × 2, 2ⁿH |
| The wholes and the angle (l.612) | "in the situated view V = H": H in both directions (the corner row of its table is C) |
| f is v₂ (l.637); h, v, v₂ (l.646) | "h is what the reader holds (its unit, V = H)", "one h means one step": H |
| Unit line (l.1014); One g (l.1031) | "its unit 1 known (h)", "v over the unit h": H, and d over H |
| Two normalizations (l.1072); How depth comes back (l.1152) | "divide both by h": by H |
| g is the sweep of v over a held h (l.1497) | h → H, "v unbounded" → d unbounded. Note: "home is a limit too, so with h held both ends are approached" conflicts with §1's "all of H is always held". Rule on it. |
| Proportion, depth and recursion (l.836) | "before the corner v is counted in h's": d in H's. Its reason, "whether v's far end is known", survives as "whether the sweep's far end, all of V, is held", and may be the right replacement for R158's reason (suggestion). |
| The level as 2h (l.2120) | 2H; "counts v in h's" → d in H's |
| Smaller drives less detailed (l.2330) | "the single unit that also forces V = H": H in both directions |
| The corner is ordinary, gloss (l.1700) | "where v equals whatever the reader counts as one, and it goes wherever the unit goes": d = H, which moves with H. The fill corner does not move. |
| Prop. 3.1 (l.1705) | "hold h, known, and v, had in terms of h": hold H; s = d/H. Step (5), "needs neither v's breadth nor an outside unit", stands. |

## C. Substance

**Appendix A**

- **R158** (l.4865; restated §3.3 l.1920): "values beyond the corner are in terms of the unknown breadth of V, not the known breadth of H."
  - *What fails:* on either reading, nothing changes breadth at the corner. A fill level v is a fraction of V on both sides. As d/H, past the corner d is just more than one H. So "undefined in proportion past the corner because of V" loses its reason.
  - *Suggestion:* the change is the flip (Prop. 3.2(a): only a = 1 keeps both registers in [0, 1]), or the far end (all of V) being unheld.
  - *Relied on by:*
    - §3.3 l.1946: "What v's unknown breadth takes away past the corner".
    - §3.3 l.2023: "R158 still holds for the far side as a whole: v's breadth is unknown".
    - §3.4 l.2569: "Past the corner every reading is s′ = b · s, with one factor b … v's breadth". A raw factor b would multiply readings on both sides, so "past the corner" comes only from R158. The proposition's mathematics stands; its premise needs a new source, such as rescaling H (§3.8).
    - §4.1 l.3035: "Past the corner there is no baseline for a magnitude (R158)".
    - §13 l.4490: "the change of register coming exactly where the unknown breadth begins (R158)".
    - Appendix C l.4966.
- **R137** (l.4843): "v=h. v!=h and h known, v not known"; "say v's breadth is 2x h's".
  - *What fails:* it separates situations 1 and 2 by comparing V with H.
  - *Suggestion:* 1 is V the same in every direction (the circle), 2 is V varying with direction. That is the pre-6 Oct table's wording at l.869.
  - *Relied on by:* situations table l.745 (situation 1's H "known, equal to V"); l.972 "situation 1 if the breadths are equal"; "Observation, decomposed" l.217 ("are v and h equal"); §2.1 bullet "Both breadths known and equal" (l.755).
- **R134** (l.4840): "in the unit circle the breadth of v and h are known and equal, so we can normalize them to 1."
  - *What fails:* fill levels are each normalized by their own breadth, so equality is not needed.
  - *Suggestion:* "both known, so both normalize".
  - *Relied on by:* §2.1 "Situation 1 … Both breadths known and equal, so both can be normalised to 1 (R134)"; l.892 "the 1 is the normalisation of two breadths known and equal".
- **R154** (l.4861): "there are no landmarks in closure, they are only found in situation 3, with unknown breadth."
  - *What fails:* the fill corner exists whether or not V is known, and Tom (6 Oct) already gave 1 and 2 a corner.
  - *Suggestion:* what is particular to 3 and 4 is holding only H's end of the sweep.
  - *Relied on by:* §4.5 l.3195, "has both breadths known and equal … Landmarks belong to situation 3 or 4 only".
- **R124** (l.4823, already superseded): "g is the ratio between the reader and the world" compares H with V. No action needed beyond confirming no current text revives it.

**In-text (Tom)**

- **By the corner** (7 Oct, l.120; tables l.126, l.134): "a situated reader approaches the corner and never locates it … to know v = h, and so to know v".
  - *What fails:* the corner is placeable without V.
  - *Suggestion:* separate the views by which ends of the sweep they hold. The unsituated view holds both; the situated reader holds H's end (home) only. On that reading, "home … approached" in l.134 is also wrong.
  - *Relied on by:*
    - l.196 diagram: "the corner approached from either side, never found".
    - l.245 standing: "the corner approached, never found" marked **proved**.
    - l.772: "a corner approached, never found".
    - l.632 (§1 table): "approached, never found (§3.1)".
    - l.747–748: corner column.
- **What a sweep is**, one sentence (l.555): "meets the corner from below". It rests on the withdrawn ruling. Strike or rule.
- **Known breadths, and the corner** (6 Oct, l.967): "situation 1 or 2, depending on if they are equal or not". Same failure as R137.
- **In 3 and 4 the corner is simply h** (6 Oct, l.979). Tom's quote is B (simply H). Claude's gloss, "The true corner, where v's breadth equals h's, needs v's breadth … never reach it", is C. It compares breadths, and the corner is never a breadth equality.
- **h as the focus, the 7 Oct correction** (l.~1000): "a real object can sit exactly at 2f, so the lens reaches its corner … corresponds to a whole … not to a situated reader". It rests on the withdrawn "Reaching the corner ends being situated". Suggestion: return the lens to a situated-reader correspondence, pending a ruling. The promoted correspondence that follows is unaffected.
- **The horizon of a situated reader** (6 Oct, l.1165), under review: "outside … from above, inside … from below, neither ever get there … they never find the true corner."
  - *What fails, beyond V:* the two measures approach 1 as θ → 0, which is home, not the corner.
  - *What survives:* both measures, their product 1, and the ×4 closing per halving, as facts about arc and chord.
  - *Relied on by:* l.775 ("approaches the line, 1, from above"), l.1060–1063 ("3, parallel … from above"), §3.1 *Revised* l.1716, §3.7 near horizon *Revised* l.2779 ("known exactly only where both breadths are known"), and the next two items.
- **Why the recursion: the approach to the line** (6 Oct, l.1207): "1 and 2 observe the line, the actual breadth; 3 and 4 … never get there".
  - *Fails:* where it equates the line 1 with the breadth or the corner (see above).
  - *May stand (suggestion):* levels without end toward an unheld far end (all of V).
- **The quarter turn is Archimedes' proof made situated** (9 Oct, l.1242), under review: "approaches the line, 1 (the corner), from below".
  - *What fails:* sin θ/θ → 1 only toward home, and "from below" rests on the withdrawn ruling.
  - *What survives:* the inscribed polygon equals sin θ/θ, and the flip supplies π/2.
- **§3.1 Revised** (6 Oct, l.1716): "approaches the true corner and never finds it: 'found with h alone' holds as a limit". Same failure as the horizon ruling. Proposition 3.1(5) already says the corner needs no breadth.
- **§3.7 near horizon** (6 Oct note, l.2779): "known exactly only where both breadths are known". Same failure. R149, quoted in the same section, says the opposite and fits the new terms.
