# OFS: the tightening pass, a cut list (24 October 2026)

*For Tom, before anything is cut (SPN R479, review 27's edit E). Nothing below is deleted: every item moves, and keeps
its text, its numbers and its citations. Line numbers are OFS as of commit 5a280cd (3,800 lines, about 60,000 words).*

## The rule for what stays in the body

The body carries one line, in review 27's order:
1. the construction (a reader at a standpoint, unit relations, V = H, the two sweeps);
2. the separation (addresses given, payloads met; Theorem 6);
3. the Cauchy with its conditions (median at the corner by reciprocal symmetry, no mean by the horizon, the exact shape
   by the uniform turn; V = H for the standard Cauchy);
4. what one standpoint cannot recover, and how amounts come in (Propositions 7–14, reading and writing);
5. the worked example (the mountain, §10);
then applications and interpretations, marked as such, and the discussion.

A paragraph stays in the body if the line needs it: a definition, a proposition, its proof, or the one example that
makes it clear. Classical connections that confirm a step without carrying it go to an appendix, one paragraph each.

## The new shape

- **Abstract**: from five paragraphs (57 lines) to three, in the order above. The one-sentence thesis kept at the end.
- **§1 Introduction** (179 lines): "Results" (67 lines) shortened to the main line's results, with a pointer to where
  the applications are; the rest stays.
- **§2–§8**: the main line, with the side remarks listed below moved out.
- **§9** (501 lines) split in two:
  - §9 keeps "What the geometry does not give: amounts": geometry first; the amounts' error; Propositions 7–14; designating
    and sizing; what a unit is; two ways to represent; reading and writing; the inscribed reading is the ratio; the
    central sweep places the paint; the test (scale the world); the number line as shared unit.
  - A new **§11 "Applications"**, after the worked example, takes the rest, each marked as an application of the propositions above: a survey; the
    ground (Sedgwick); growth (the calendar tower); units within units and the worked tower; closing a loop; recovered,
    not written; inside a room; moving the furniture; far off, parallax; one standpoint gives no parallax; the outline
    from one place (the visual hull, the fold); §7.8's special relativity sky (the one physics example, kept whole).
- **§10 The worked example** (the mountain), unchanged and still §10.
- **§12 Discussion** (now §12) (Jaynes; assumptions and open questions; related work; what the geometry gives free, its framing
  paragraph only).
- **Appendix A, "Where the geometry already appears"**: the classical connections, one paragraph each.
- **Appendix B, "Engineering read against the geometry"**: §11.4's list.
- **Appendix C**: notation (as now).

## What moves to Appendix A (classical connections)

| from | item | lines now |
|---|---|---|
| §2 "Zero, and a new zero" | Niven and Weyl on repeated steps; no group law on the projective plane; the winding number (one sentence stays: composition is by tangent addition) | ~15 of 56 |
| §3.4 | Cauchy's mean width (one sentence stays: 2/π is the turn's) | 6 |
| §3.4 | "Archimedes' proof, the writer's and the reader's" | 36 |
| §4 | the Cayley transform; Bohlin's square; the three-term Plücker relation; Hilbert's metric; "Series stop at the corner" | ~30 |
| §5 | π_p (in "The Euclidean choice"); Wantzel (in "Why halving"); discrete subgroups; "What the count of orthants borrows"; "Diameter 2" | ~25 |
| §6 | Yaglom's three numbers (in "One figure, three rulers"); the angle doubling not Möbius; "A familiar instance" (floats) | ~20 |
| §7.1 | "Why the payload is Gaussian" (Herschel–Maxwell); "Why a turn and not a boost"; Beltrami | ~40 |
| §7.2 | "Once a Cauchy, always a Cauchy" and "What breaks it" folded into "Three properties of one law" (one paragraph) | ~20 saved |
| §7.4 | the length-per-turn uniqueness (kept in the body until its source is checked; see below) | — |
| §7.6 | Robbins–Monro with averaging | 6 |
| §7.8 | the cross ratio of four stars | 4 |
| §8 | the doubling map; "A point of this plane is a Cauchy law" and "A reader at height γ" (the binary tiling's detail; the section keeps its statement and Böröczky); Boyd's points and Chebyshev's nodes; odd and even K | ~70 |
| §8 | "Other ways to squeeze the line" | 25 |

## What moves to Appendix B (engineering)

§11.4's examples: the depth buffer, the flat screen and the cubemap, the capped charts' bound, the Kalman steady state,
exact composition, Fibonacci hashing, consistent hashing and labels, tables fixed in advance, the centre of directions,
the dial (about 60 lines). §11.4 keeps its framing: what comes free outright, what given a premise, what is the
payload's, and that this is a claim about origins, not performance.

## What stays where it is

Propositions 1–14 and Theorem 6 with their proofs; the separation in brief; given, not performed; the reader's ignorance
as a group; the situations and the two other parties; the hand (the stained-glass window, review 27: "keep it");
"Where the numbers come from"; the reader's line, closed; the corner fixed by home and the horizon (shortened); why 45°;
the arc from the chord; the address points at the payload; why two sweeps; "What V = H means" and the two choices;
Proposition 4 with (S) and its counterexample; reality in 2H; Mercator and the lighthouse (Proposition 5(f), (g));
working back from the Cauchy; the array picture (review 27: keep it, its claims marked); what the floor discards (its
statement); "A fixed count, aimed by H"; "One K"; §10's mountain; §11.1–§11.3.

## One check before the pass

§7.4's "two smooth outlines with the same length per turn are one" (R477) was taken in with no classical source found.
A short search (support functions, polar curves, the intrinsic equation r(s) of a curve) either gives it a citation or
marks it as ours, before an outside reader sees it.

## The result

The body from about 3,400 lines to about 2,900, and the main line visible in the order review 27 asks; the appendices
about 450 lines. Nothing is lost: each moved paragraph is pointed to from where it was by one sentence. The CS
companion takes the same order after OFS settles (R421).

## Made (24 Oct, SPN R480)

As listed, with these kept in the body: "What the floor discards" (R464), "Other ways to squeeze the line" and "Why a
turn and not a boost" (the necessity argument), the floats' instance, "Diameter 2", Cauchy's mean width. The cross ratio
stays with the special relativity sky in §11. §7.2's three paragraphs on the family were not folded together. The
length-per-turn uniqueness is marked as ours. Body (§1–§10) 3,009 lines to 2,708.
