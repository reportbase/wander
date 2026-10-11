# Each Sees the Other Smaller

### A first course in denominator paradoxes — or, how a number can be true from every seat and contradictory on paper

*A companion to the interactive demo. No background beyond high-school algebra is assumed.*

*Tom Brinkman, with Claude, written in an earlier session; added to `papers/` on 11 October 2026 (two typing slips
corrected, nothing else changed). Read with `vantages.md` §F, which maps it onto the three vantages.*

---

## 1. Start with something you already believe

Two friends, A and B, stand at opposite ends of a field and look at each other.

A sees B as small — much smaller than A's own hand held up at arm's length. B, looking back, sees A as small — much smaller than B's own hand. Both of them are being perfectly accurate. Neither one's eyes are lying.

Now write down what each of them observed, as a claim about the world:

> A: "B is smaller than me."
> B: "A is smaller than me."

Put those two sentences side by side and you have a contradiction. B is smaller than A, *and* A is smaller than B? Both can't be true. Yet you know — without doing any math at all — that nothing is wrong here. Nobody is confused about perspective. If a child said "people shrink when they walk away," you'd gently explain that they only *look* smaller.

Hold on to that feeling of "obviously there's no real problem here," because this whole paper is about one question:

**What exactly went wrong between the two accurate observations and the contradictory sentences?**

The answer turns out to be small, precise, and surprisingly deep — and once you can see it, you will recognize the same mistake hiding inside a century-old physics "paradox," a famous statistical trap, a common courtroom error, and a subtle problem in how inflation gets measured. They are all the same mistake. This paper teaches you to spot it.

## 2. Every measurement is secretly a fraction

Here is the key move, and it's worth slowing down for.

When A "sees how big B is," what is A actually doing? A has no tape measure stretched across the field. What A actually has is two things in view at once: the *apparent* size of B (tiny, far away) and the apparent size of something A carries — their own hand, their own body, their own sense of scale. A's observation is really a comparison:

$$
r_A = \frac{\text{how big B appears}}{\text{how big I appear to myself}}
$$

That's a fraction. The top (the numerator) is the thing being measured. The bottom (the **denominator**) is the ruler it's being measured *against*. In the demo, with A and B each about the same true height and standing 10 units apart, this fraction comes out to something like $r_A = 0.089$: "B appears about 9% of my size."

B does exactly the same thing from the other end of the field and gets $r_B = 0.113$: "A appears about 11% of my size."

Notice something about these two fractions: **they have different denominators.** A measured against A's ruler. B measured against B's ruler. Each denominator is *private* — it belongs to one observer's seat, and the other observer doesn't share it.

Both fractions are correct. Both are less than 1. And "less than 1" means, in each case, "the other one looks smaller than my ruler." So far, no contradiction — just two honest reports from two different seats.

## 3. Where the contradiction is manufactured

Now watch the mistake happen, in slow motion.

Take A's fraction, 0.089, and B's fraction, 0.113, and write them down on the same piece of paper — say, on a number line. Just two dots between 0 and 1. Perfectly innocent-looking.

But something got destroyed in that step. On the number line, 0.089 is just... 0.089. A pure number. Nothing about it records that it was measured *against A's ruler*. The denominator — the private ruler — has been divided away and discarded. The number keeps the quotient and deletes the receipt.

And here is the sneaky part: a number line doesn't just delete the old denominators. It quietly supplies a **replacement**. Every number on a number line is measured against the same thing — the line's unit, the distance from 0 to 1. One line, one unit, one ruler *for every number on it*. So the moment both observations land on the same line, they are being treated as if they were measured against a single shared ruler.

But no such shared ruler ever existed. A used A's; B used B's.

Now the two sentences transform:

- "$r_A < 1$" *used to mean* "B looks smaller **than A's ruler**." On the shared line, it now reads: "B is smaller, **period**."
- "$r_B < 1$" *used to mean* "A looks smaller **than B's ruler**." On the shared line: "A is smaller, **period**."

And *those* two claims contradict each other. The contradiction was not in the field, not in the eyes, not in the fractions. It was manufactured by the notation — by writing two private-denominator measurements on one common scale. The paradox is not a fact about the world. It is a fact about a bookkeeping error.

This gives us a definition worth memorizing:

> **A denominator paradox is what you get when measurements made against different private rulers are compared as if they shared one ruler.**

The demo shows this as a three-step cartoon: the two fractions with their denominators visibly attached and color-coded → the division sign that deletes them → the single number line whose unit silently replaces them both, stamping CONTRADICTION. Slide the figures around and you can watch the contradiction appear and disappear. It never touches the field itself; it lives entirely in the last panel.

## 4. Fixing it: the exchange

If the mistake is comparing across private rulers, the fix must be to somehow get a *legitimate* shared quantity. There's a beautiful way to do it, and the demo's "court" panel performs it live.

Suppose A and B phone each other and swap their measurements. Now each of them holds both numbers: $r_A = 0.089$ and $r_B = 0.113$. Neither number alone can answer "who is really bigger" — but *combinations* of them can, because the combinations can be arranged so the unknown stuff cancels.

Write out what the fractions actually contain. If $S_A$ and $S_B$ are the true sizes and $d$ is the distance between them (with each person's self-reference at arm's length, distance $d_0$):

$$
r_A = \frac{S_B / d}{S_A / d_0} = \frac{S_B}{S_A}\cdot\frac{d_0}{d},
\qquad
r_B = \frac{S_A / d}{S_B / d_0} = \frac{S_A}{S_B}\cdot\frac{d_0}{d}
$$

Both reads contain the same distance factor $d_0/d$ — that's the *shared* part, the thing both measurements have in common — multiplied by the size ratio, one way up in $r_A$ and the other way up in $r_B$.

Now two tricks:

**Divide one read by the other.** The shared distance factor cancels completely:

$$
\sqrt{\frac{r_A}{r_B}} = \frac{S_B}{S_A}
$$

Out pops the *true* relative size — exactly, with no rulers, no units, no tape measure. In the demo's default setting this gives 0.8889, and the true answer $1.6/1.8$ is... 0.8889. The question "who is really bigger?" turns out to have a definite answer after all — but it costs something: you can only compute it *after the exchange*. One seat alone can never own it.

**Multiply the reads together.** This time the private sizes cancel:

$$
\sqrt{r_A \cdot r_B} = \frac{d_0}{d}
$$

Out pops the distance between them (in units of the arm's-length reference). Two combinations, two cancellations, two facts recovered: the ratio of the reads tells you *who's bigger*, the product tells you *how far apart*. Everything the two seats could honestly want to know is in there — it just isn't in either read alone.

So a denominator paradox has a two-part resolution, and both parts matter:

1. **The contradiction dissolves** the moment you stop pretending the reads share a ruler. Both claims were true as reads; only the absolute versions clashed.
2. **The real answer is purchasable.** Exchange the reads, and combinations that cancel the private parts recover objective facts. The paradox doesn't mean "there's no truth" — it means the truth costs an exchange.

## 5. The famous version: "each sees the other's clock run slow"

Now for the payoff. In Einstein's special relativity there is a result that has bent students' brains for over a century: if two spaceships fly past each other at constant speed, *each* one measures the *other's* clock as ticking slowly. A says B's clock is slow. B says A's clock is slow. Generations of students have hit this and thought: that's impossible — they can't *both* be slower than each other.

Compare it with our field:

| Perspective (nobody's confused) | Relativity (a century of confusion) |
|---|---|
| Each sees the other **smaller** | Each measures the other's clock **slower** |
| Measured against own apparent size | Measured against own clock's ticking |
| Denominator: private (my ruler) | Denominator: private (my clock) |
| "Both smaller than each other" — contradiction? | "Both slower than each other" — paradox? |
| Resolved: distance shrinks appearance; exchange recovers truth | Resolved: exactly the same way |

It is the same shape. *Exactly* the same shape. Each observer's rate-measurement is a fraction whose denominator is their own clock — a private ruler. Both measurements are correct. The "contradiction" only appears when the two reads are written onto one absolute timeline, as if there were a universal master clock they were both measured against. Relativity's whole point is that there isn't one.

And the resolution has the same two parts. First, the contradiction dissolves: "slower" was always "slower *against my clock*," and the two claims, kept in their seats, are compatible. Second, real answers remain purchasable: if the twins actually want to settle who aged less, one of them has to turn around and come back — bringing both clocks to the *same place* so they can be compared side by side, sharing a denominator at last. When that happens, there is a definite answer (the traveler is younger), and no contradiction anywhere.

Here is the question this comparison should leave you with. Why did *nobody ever* call perspective a paradox, while relativity's version spent a hundred years with "paradox" in its name? The physics of the two situations differs, but the logical shape is identical. The difference is us: you learned in early childhood that apparent *size* has a private denominator — you calibrated it watching people walk away and not shrink. You never got the childhood training for *time*, because at walking speeds the effect is a millionth of a millionth. So when the clock version arrived, everyone instinctively wrote both reads on one absolute timeline — committed the notation error — and blamed the resulting contradiction on the theory. The paradox was never in the physics. It was in forgetting which quantities carry a private denominator.

## 6. The rest of relativity's paradox shelf

Reciprocal clocks are only the entry ticket. Relativity keeps a whole shelf of named paradoxes, and generations of students have fought each one separately. The denominator diagnosis handles the shelf all at once: in every case, a claim that *sounds* absolute is secretly a read against a private denominator, and the "contradiction" appears only when that receipt is thrown away.

**The twin paradox.** One twin travels at high speed and returns; relativity says the traveler comes back younger. The paradox, as usually posed: "but from the traveler's seat, it was the stay-home twin who was moving — so shouldn't *each* be younger than the other?" Start with the mid-trip question, "who is older *right now*?" That question has no shared denominator: each twin's age accumulates against their own clock, and "right now," said across a distance, is itself a counterfeit shared ruler (wait for the ladder, next). So mid-trip, the question is as unposed as "who is *really* smaller" was in the field. But the twins then do something our field observers could also do: they **reunite**. Reunion brings both accumulated ages to one place, one event — a genuinely shared seat where the two registers can finally be laid side by side. That purchase produces a definite answer — the traveler is younger; the path that bent kept less time — and no contradiction anywhere. Note that the answer was *bought*, not assumed: the traveler is the one who turned around, and the turnaround is what bends the path. Unanswerable before the purchase, definite after it — the signature of a denominator paradox rather than a real one.

**The ladder and the barn.** A ladder longer than a barn moves toward it at high speed. In the barn's bookkeeping, the moving ladder is length-contracted and fits — both doors can be shut at the same moment with the ladder entirely inside. In the ladder's bookkeeping, it is the *barn* that is contracted, and the ladder never fits at all. Both bookkeepings are internally flawless. Contradiction? Ask what "fits" actually means: *both ends inside at the same time*. That phrase — "at the same time," asserted about two different places (the front door and the back door) — is precisely a demand for a shared denominator: one "now" stretched across two locations. And relativity's deepest lesson is that no such shared now exists — each frame slices its "now" privately, just as each observer in the field held a private ruler. "The doors shut simultaneously" is true against the barn's now and false against the ladder's now, exactly the way "B is smaller" was true against A's ruler and false against B's. The ladder fits *against one denominator*. It was never a fact of the "period" kind.

**Bell's spaceships.** Two ships, one behind the other, joined by a taut string, fire *identical* engines at the *same moment*. The setup sounds perfectly symmetric — surely the gap between them stays fixed and the string survives? It snaps. The diagnosis is one word in the setup: track the denominator of "identical." Identical accelerations *as certified in the launch frame's simultaneity* — a claim stamped against one particular private now, then silently carried into the ships' own frames, where it does not hold. Measured in the ships' own bookkeeping, the lead ship pulls away; the gap grows to γ times the string's natural length, and the string breaks. Attach the receipt and the paradox evaporates: "identical (according to the launch pad)" and "identical (according to the ships)" are different claims, and only the first was ever true.

**Thomas precession**, one sentence for the curious: carry a gyroscope around a closed *loop* of velocity changes and it returns pointing in a slightly different direction, although every individual leg looked rotation-free — a residue that belongs to the whole loop and to no single leg's bookkeeping, exactly like the currency triangle you'll meet in Section 8, where every individual exchange rate looks innocent and only the trip around the closed loop exposes the discrepancy.

Now the table from Section 5 extends down the whole shelf, with the same three columns every time: the claim that *sounds* absolute ("slower," "older," "fits," "identical," "unrotated"); the private denominator it was actually measured against (my clock, my clock again, this frame's now, the launch pad's now, one leg's frame); and the purchase that funds a real answer (exchange the reads, reunite, pay for one frame's now and say which, re-certify in the ships' frames, close the loop and read the residue). Five famous paradoxes, one diagnosis, one repair kit. None of them needed new physics to resolve — each needed the receipt reattached.

## 7. The same trap in a statistics class

You will meet this shape again, probably in your first statistics course, wearing a different costume. It's called **Simpson's paradox**, and it is real medical data (a 1986 study of kidney-stone treatments):

- For small stones: Treatment A succeeds **93%**, Treatment B succeeds 87%. A wins.
- For large stones: Treatment A succeeds **73%**, Treatment B succeeds 69%. A wins again.
- Overall, pooling all patients: Treatment A succeeds 78%... and Treatment B succeeds **83%**. B wins?!

A treatment that is better for every kind of patient looks worse overall. Students meet this and feel the same vertigo as the spaceship clocks. And it is the same mistake.

A success rate is a fraction: successes over patients. The denominator is the *patient group* — and the two treatments had very different ones. Treatment A (surgery) got assigned the hard cases: 75% of its patients had large stones. Treatment B (a less invasive method) got the easy ones: only 23% large stones. Each treatment's success rate is measured against its own private mix of patients — a private denominator. "Pooling" the data adds the numerators and adds the denominators as if the two patient groups were interchangeable rulers. They aren't, and the pooled comparison is exactly the field-paradox's shared number line: a comparison across private denominators dressed up as a comparison on one scale.

The fix is also the same. Either keep the seats separate (compare small stones with small stones, large with large — where A wins both), or genuinely *purchase* a shared denominator: pick one standard patient mix and re-compute both treatments' rates against that same mix. Definite answers exist; they just have to be paid for.

## 8. Once you see it, it's everywhere

**The courtroom version.** A forensic expert testifies: "the probability of this DNA match if the defendant were innocent is one in a million." A juror hears: "the probability the defendant is innocent is one in a million." Those are *different fractions* — they have swapped numerator and denominator populations. In a city of ten million people, about ten innocent people would match by chance, so given only the match, the defendant is roughly 91% likely to be innocent — not one-in-a-million guilty. Mixing up "probability of the evidence, given innocence" with "probability of innocence, given the evidence" is called the *prosecutor's fallacy*, and it has produced real wrongful convictions. It is a denominator error: the two probabilities are reads against different reference populations, and flipping between them for free is exactly like comparing A's ruler to B's without the exchange. (The legitimate flip exists — it's called Bayes' theorem — and its price is knowing the base rates.)

**The percentage version.** A stock falls 50%, then rises 50%. Back to even? No: down to 75. The second percentage was measured against a *different denominator* (the shrunken price) than the first. Percentages always carry a silent "of what," and chaining them as if the "what" stayed fixed is a small denominator paradox you can commit with a calculator.

**The inflation version.** To say "prices rose 8% this year," a statistics bureau must compare this year's prices to last year's — but measured against *which* year's shopping basket? Using last year's basket gives one answer; using this year's gives another (people change what they buy when prices change — the basket is a private denominator of its year). The two answers straddle the truth, one biased each way. The elegant fix, adopted in 1922 and still called the *Fisher ideal index*: take the **geometric mean** of the two — multiply them and take the square root — exactly the $\sqrt{\ }$-combination trick from Section 4, invented independently by economists because it makes the two baskets' biases cancel. Real national price statistics are computed this way today. The court's resolution of our toy paradox is running, right now, inside the machinery that measures inflation.

**The arbitrage version.** Currency exchange rates are ratios: dollars per euro, euros per yen, yen per dollar. If the rates are all honest — each one a ratio of the currencies' true values — then converting around the full triangle must bring you exactly back to where you started: the three ratios multiply to 1. If some rate is miscalibrated, no *single* comparison can detect it (any one rate looks like a plausible rate), but the trip around the closed loop exposes it — the product comes out 1.01, and that 1% is free money, which traders instantly consume until the loop closes again. Detection of a corrupted ratio needs a *third* party closing a loop; two parties alone can't see it. Keep that in mind next time someone tells you two data sources "agree with each other."

## 9. The general lesson

Let's compress everything into a small toolkit you can actually carry into other courses.

**The diagnostic question.** Whenever two measurements are being compared — success rates, clock rates, apparent sizes, percentages, probabilities, indices — ask: *what is each one's denominator, and do they actually share it?* If the denominators are private (each seat's own ruler, own clock, own patient mix, own year's basket, own reference population), then any direct comparison on a common scale is counterfeit, and any "contradiction" it produces is manufactured.

**The two-part resolution.** A genuine denominator paradox resolves in two moves, and you need both. *Dissolve*: restate each claim with its denominator attached ("smaller than my ruler," "slower than my clock," "more successful on my patient mix") — the contradiction evaporates, because the claims were never about the same thing. *Purchase*: if you want an absolute answer, you must buy a shared denominator — exchange the reads and cancel the private parts, reunite the clocks at one place, standardize the patient mix, geometric-mean the two baskets, close the loop with a third party. The answer exists; it has a price; the price is the exchange.

**The notation warning.** The real number line is a wonderful tool with one dangerous property: every number on it silently shares one unit. It has no slot for recording *whose ruler* a value was measured against — the division that produced the value deleted that information. This is usually harmless, because usually all your numbers really do share a denominator. But when they don't, the number line will manufacture contradictions for you with total confidence, and the contradiction will look like it's about the world. A fraction kept as a fraction — numerator and denominator both visible, never divided through — cannot make this error, because the receipt is still attached. Sometimes the sophisticated move is to *not* simplify.

**The humility point.** The paradoxes in this family were not resolved by discovering new facts. Perspective needed no new fact; the twins needed no new fact beyond what relativity already said; Simpson's data was correct all along. Each was resolved by locating a bookkeeping assumption so automatic that nobody noticed they were making it — the assumption of a shared ruler. That is worth remembering beyond mathematics: when two honest observers seem to flatly contradict each other, before deciding one of them must be wrong, check whether their claims were ever actually measured against the same thing.

## 10. Back to the demo

Now the demo panels should read as one story, top to bottom. The **surveyor's view** shows the field as no one in it ever sees it — true sizes on one scale; that god's-eye view is precisely the thing neither observer possesses, and forgetting that is the whole error. The **two seat views** show what A and B actually see: each holds the other, small, against their own reference. The **ledger** states both reads and shows the contradiction appearing only when they're read as absolute. The **court** performs the exchange: ratio cancels the shared distance and recovers who's really bigger; product cancels the sizes and recovers how far apart — definite answers, bought at the price of a phone call. The **real-line panel** replays the crime in slow motion: fractions with their denominators attached, the division that deletes them, the one line whose unit forges a replacement. And the **circle** at the bottom shows the alternative bookkeeping, where a measurement is kept as an un-divided pair; slide the distance and watch the two reads move while the recovered truth — the green dot — stays pinned. Press *sweep* and the pair even glides through the value "infinity" without difficulty, which is a story for another day, but a hint: keeping the receipt doesn't just prevent paradoxes. It makes the arithmetic sturdier everywhere.

One sentence to take with you: **a number with its denominator deleted is a claim with its witness dismissed — and most famous "paradoxes" of comparison are just two such claims, put on one line they never shared.**

---

*The kidney-stone figures are from Charig et al. (1986), the standard classroom example of Simpson's paradox (named for E. H. Simpson, 1951, though known to Yule by 1903). The price-index construction is Irving Fisher's (1922). The relativity paradoxes are the standard set — the twins (Langevin, 1911), the ladder/barn (Rindler's pole-and-barn), the spaceship-and-string problem (Dewan–Beran 1959, popularized by J. S. Bell), and Thomas precession (1926) — with their textbook resolutions restated in denominator form; none is resolved here differently, only uniformly. The perspective/relativity parallel, the exchange-and-cancel resolution, and the number-line diagnosis follow the interactive demo this paper accompanies. Nothing in this paper is new mathematics; its aim is to show that these standard results are one idea.*
