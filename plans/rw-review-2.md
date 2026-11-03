# Review 2 of *Reads and Writes*: a referee's stress test (3 Nov 2026)

Pasted by Tom on 3 Nov 2026, an outside referee's report (likely ChatGPT), "an independent conceptual and mathematical
stress test" of the draft of 30 October, retitled 2 November, with no message of his own; its last three lines were
the tool's offers to revise its own report. Below it is condensed, followed by Claude's response. Tom: "Proceed". The
edits below were made in the paper, essay 6 and the PXS plan (SPN R629).

## The review, condensed

Verdict: "revise, with the core thesis retained", 8.3/10 (conceptual coherence 9.0, mathematical validity 8.0,
originality of synthesis 8.7, clarity 8.0, technical completeness 7.5, publication readiness 7.8). The governing principle
kept: "A read gives a standpoint its directions; a write joins standpoints and supplies what no single standpoint holds."
Strongest: the scale test, the half-Cauchy from a uniform quarter turn, the depth d = B/(cot a + cot b), reading and
writing as acts. Its points:

1. Address and payload: keep the separation at the right level (a nominal address, the payload, the physical arrival
   direction, the reconstruction); "the payload has no concept of an address" an interpretation, not a theorem.
2. Triangulation assumes matched points and a known displacement.
3. The Cauchy's derivation rests on the uniform turn; the address reading is a separate step.
4. A cutoff's integral (1/π)·ln(1 + M²) is not the conditional mean, ln(1 + M²)/(2·atan M).
5. Closure needs its operation and independence; parameters, random variables and measurements kept apart.
6. Complex parallax: state independence, say the w's are points indexing laws, mark rays not meeting ahead, and test
   general position beyond the corner (whose identity it checks).
7. The place across the line of sight: derive it. With independent Cauchy reads, R = A/(A − B) has density
   ∫|t| f_A(rt) f_B((r − 1)t) dt, singular at r = 0, so not Cauchy.
8. Two quarter turns: the sum of two half-Cauchys has density ~ (4/π²)·s at zero, so it is no half-Cauchy; the depth's
   tail is ~ 4B²/(π²d³), with a finite mean.
9. Repeated reads: the mean of i.i.d. Cauchys does not concentrate, the median does, at π²γ²/(4n); only under i.i.d.
10. Recovery: dividing out gives ρ up to its total and amplifies noise where p is small; undoing the Cauchy blur is unique
    but unstable (e^(γ|k|) on the noise); a payload-weighted mean depends on the payload.
11. Special relativity: D⁴ for a stated set-up; motion from directions under stated conditions.
12. Terminology: "the Cauchy is an address law", "the reader has no amount", "the writer has the whole", "the line is where
    knowing V is" each scoped; "two lengths make square roots" defensible.

## Response

Already in the paper:
- 4: §2 gives "(1/π)·ln(1 + M²) over the share below M, about 8.8 at M = 10⁶", which is the conditional mean,
  ln(10¹²)/(2·atan 10⁶) = 27.63/3.14 = 8.80.
- 11: §3's D⁴ is "for a sky uniform in its own frame, counting total power" (R625).
- 12's square roots: R625, with ∛2 and Wantzel.
- 3: the half-Cauchy is derived from the uniform turn, and the address reading is marked as ours.
- 6's general position: PXS run 1 tested seven targets, two off the bisector, at three γ; the plan's derivation is the
  general Möbius one, not the corner alone.
- 1, 2 and 12's other phrases are framing the paper already keeps (R625's "the world decides what meets each address";
  §8 matches each point in both looks).

Made (SPN R629):
- §8 "Parallax is a sum of reads": the two reads' errors independent; rays not meeting ahead enter as negative depths;
  the two ways out of the family each proved in a line (points 7 and 8: the place's density infinite over each
  standpoint; the quarter turns' depth tail 1/d³, with a mean). Essay 6 §4 the same.
- §2 "The payload is not lost": dividing the address law out gives the distribution up to its total; undoing the blur
  multiplies noise too, unique in principle not the same as stable; averaging the payload totals where that total is
  finite, which is the payload's to say.
- `plans/pxs-plan.md`: a note after its runs with the two derivations and their numerical checks.

Not taken: the scores, and further hedging of phrases the paper already scopes.
