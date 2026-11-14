# LWS: sorting the laws by the shape of their denominators

14 November 2026. Tom: "yes, sort the laws." (after R985, `plans/discussion-note.md` item 17).

## The question

R985 proposed (Claude's, not ruled) that a geometric law has one of two shapes:

- **P (a chain)**: a product or composition in which every middle denominator cancels, leaving the ends and the last
  "in terms of" (a/b · b/c = a/c; w(a)·w(b) = w(a ⊕ b); w(s)·w(1/s) = −1; the walk's telescoping ratios).
- **S (a shared sum)**: terms over one denominator that stays, the law being that the numerators fill it
  (1/(1 + s²) + s²/(1 + s²) = 1; h² + v² = 1).
- **N (neither)**: anything else. A third shape would be a law whose denominator neither cancels nor is shared.

Is that so for the laws the papers use?

## Method (fixed before the list is seen)

1. A fresh agent, not shown R985, this plan's categories or my guesses, lists every law (a relation stated as
   holding for all values of its variables, not one number) that *Reads and Writes* (`papers/readers-and-writers.md`)
   states, with the formula as written and its section. Written to `runs/lws/laws.md`.
2. I sort each by an operational test, written here first:
   - **P** if, written with each read's own denominator, the law is an identity in which intermediate variables
     (or intermediate denominators) appear in the factors and are absent from the result.
   - **S** if the law says a sum of terms over one common denominator equals a fixed value (1, or a total), the
     denominator present in every term.
   - **N** otherwise; a law that is a limit (needs n → ∞ or an integral to a transcendental value), or a law about a
     remainder (a loop that does not close), is N unless its finite members are P or S, in which case it is marked
     P* or S* (the finite law sorted, the limit noted).
3. Each P and S law is checked in exact arithmetic (fractions, Gaussian fractions) at three or more values in
   `runs/lws/lws.py`.

## Predictions (committed before the list)

- **L1** At least 75% of the listed laws sort as P, P*, S or S*. Kill: under 75%.
- **L2** Every law that composes turns or slopes (tangent addition, Euler's form, the Cayley map's products) is P.
  Kill: one that is not.
- **L3** Every complement or "shares add to one" law is S. Kill: one that is not.
- **L4** N is not empty: at least one listed law is neither (my guess: the holonomy laws, where a loop leaves a
  remainder, and laws among amounts such as the Gaussian). Kill: N empty.
- **L5** Every P and S law checks exactly at three values. Kill: any miss.

## Runs

(appended below as they come out; nothing above this line edited afterwards)

### Run 1 (14 Nov 2026; list `runs/lws/laws.md` by a fresh agent, 125 entries; sorting `runs/lws/sorting.md`; checks `runs/lws/lws.py`, output `runs/lws/lws-run1.txt`)

- **L1 killed.** P 23 (two P*), S 10 (two S*), N 92: 33 of 125, 26%, against the 75% predicted.
- L2 not killed, weakly: every composition of turns or slopes listed (8, 91, 98, 101, 105, 119) is P, but 8, 91, 105
  and 119 only when read as turns between landing points, w(y)/w(x), whose chain cancels; written as a formula alone
  they show no cancellation. That reading is mine.
- L3 not killed: every complement (10, 19, 28, 52, 78, 79, 80, 103, 109, 123) is S.
- L4 not killed: N is most of the list.
- L5 not killed: 86 exact checks on the 33 P and S laws, none failed.

Said plainly: the two shapes describe a small part of what the paper states, not "every geometric law". The agent
listed broadly (densities, charts and formulas as well as identities), which inflates N, but even the identities
split three ways. Post hoc, the 92 N fall into: densities and measures (19, a heat per something, not a relation),
changes of chart or maps (20: tan, gd, sech, the Cayley map, Mercator, aberration; one quantity written in another's
terms), formulas giving one quantity from reads (13: parallax, contact, the walk, a write), a loop's remainder (4: the
holonomy laws, where a chain does not close), limits and series (8), and other (28: invariances, transforms,
factorizations, laws among amounts). Untested reading: the chain and the shared sum are the two shapes a law takes
when it relates reads to each other (composing them, or filling one length with them); a change of chart is a third,
common shape (the same read in another name), where no denominator cancels or is shared because there is only one
read; and the holonomy laws are what a chain leaves when it does not close.

### Runs 2 and 3: predictions (14 Nov 2026, committed before either runs)

Tom: "merge first, than proceed with recommendations." (Claude's recommendation: a blind re-sort, then whether a change
of chart is a chain in disguise.)

**Run 2, the blind re-sort.** A fresh agent gets `runs/lws/laws.md` and this plan's Method step 2 (the test for P, S, N,
P*, S*), but not `runs/lws/sorting.md`, R985, R986 or any of my labels, and sorts all 125. P* counts as P, S* as S.

- **B1** It agrees with my sort (P, S or N) on at least 80% of the 125. Kill: under 80%.
- **B2** Cohen's κ between the two sorts at least 0.6. Kill: under 0.6.
- **B3** Its P + S count within 10 of my 33 (so 23 to 43). Kill: outside.

**Run 3, is a change of chart a chain in disguise?** The 20 laws I put under "a change of chart or a map" (1, 11, 13–18,
20, 21, 30, 44, 45, 49, 53, 56, 59, 94, 97, 111). Said first, so it is not mistaken for a finding: for any bijection φ, a
law moved into another chart, φ∘L∘φ⁻¹, chains with anything through φ⁻¹∘φ = identity, so "transported chains still
telescope" is an identity and cannot fail. What can fail is which chart laws are bijections of one read at all, and
what each chart does to the reads' own composition (tangent addition for directions, multiplication for d/H, velocity
addition for boosts).

- **C1** At least 14 of the 20 state a bijection of one reading onto another coordinate (one variable, strictly monotone
  on its stated domain, checked numerically). My guess at the rest: 14 (a family of lines), 21 (a stretch, a
  derivative), 44's area clause and 111 (a statement about rationality). Kill: fewer than 14.
- **C2** For each bijection, the reads' composition moved into its chart and chained over five links telescopes to the
  ends to 10⁻⁴⁰. Kill: any miss (a check of my code, not of the claim).
- **C3** At least 10 of the bijections carry their reads' composition to plain addition or plain multiplication in the
  new coordinate (q(a∘b) = q(a) + q(b), or ·, to 10⁻⁴⁰): that is, they are group charts, the ones that turn a chain of
  products into a chain of sums (the angle for turns, the logarithm for scales, the rapidity for boosts, w for turns as
  multiplication). Kill: fewer than 10.
- **C4** Every chart that carries composition to plain addition is transcendental (involves an arctangent, a logarithm or
  an exponential), and every rational chart carries it to multiplication or to a Möbius map, never to plain addition.
  Kill: a rational chart that adds, or a transcendental one among the additive that I could not name as arctan, ln or exp.

If C1 and C3 hold, the third shape reads as a chart that turns a chain of products into a chain of sums (gaps that add,
law 75), and "neither" shrinks by the group charts; if they fail, the third shape stands as its own kind.
