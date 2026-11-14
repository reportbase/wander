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
