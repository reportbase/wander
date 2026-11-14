# PIE: where π and e sit in the laws

14 November 2026. Tom: "merge, than run the PI E tests" (Claude's suggestion after LWS run 3b: is every law that carries
π or e either an additive chart or a limit?).

## The question

LWS run 3b found, post hoc, that the charts which turn the reads' composition into plain addition are the logarithm, the
angle and pseudorapidity, all transcendental, while every rational group chart multiplies. The reading: turning a chain
of products into a chain of sums is what the logarithm and the angle are for, and they bring e or π with them. If so,
π and e should enter the paper's laws only in two ways: through such a chart (a law written in the angle, the
logarithm or the rapidity, or the chart itself), or as a limit (a series, a product without end, an integral to a
transcendental value, including a total that normalizes a density). Not as a ratio of reads, and not in a chain or a
shared sum between reads written rationally.

## Method (fixed before anything runs)

1. **Mechanical flag** (`runs/pie/flag.py`): a law of `runs/lws/laws.md` carries π or e if its formula (the text after
   the name, before the section) contains π, Ω, an exponential (e^, exp), a logarithm (ln, log), a circular function
   (sin, cos, tan, sec, cot, arctan, atan, asin, acos), a hyperbolic one (sinh, cosh, tanh, sech, asinh, atanh), gd or Γ.
2. **Blind classification**: a fresh agent gets the flagged laws and the definitions below, not this plan's predictions,
   R988 or any sort, and classes each as
   - **A** (an additive chart): the law is, or is written in the coordinate of, a chart that carries a composition to
     plain addition: the angle (for turns), the logarithm (for scalings), the rapidity or pseudorapidity (for boosts), the
     exponential or tangent as their inverses;
   - **L** (a limit): the transcendental number arises as the value of a limit, a series, an infinite product, or an
     integral over an unbounded or whole range, including a normalizing total;
   - **X** (neither).
3. Counts against the predictions; LWS run 2's blind sort used for T3.

## Predictions (committed before any run)

- **T1** At least 90% of the flagged laws are A or L. Kill: under 90%.
- **T2** Of the 19 laws the blind sort of LWS run 2 called P or S, at most a third are flagged. Kill: more than 6.
- **T3** Of the flagged laws, at most 10% were called P or S by that blind sort. Kill: more.
- **T4** At least 20% of the flagged laws are A (the chart route is not rare). Kill: under 20%.

## Runs

(appended below as they come out; nothing above this line edited afterwards)
