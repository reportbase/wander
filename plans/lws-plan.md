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
