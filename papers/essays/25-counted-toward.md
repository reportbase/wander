# Counted toward: building π and e from reads, and where they meet

*The twenty-fifth of a series of essays on what can be known from where one stands. Draft, 15 November 2026. It gathers
one exact run (BLD, SPN R1009), its predictions committed before it ran, and the discussion that led to it: where π and e
cancel in the same equation (R1008, `plans/discussion-note.md` item 18), and from which vantage that cancellation is
seen.*

A ratchet wrench clicks. Each click turns the socket the same small amount, and if you want to know how many clicks
take a nut from facing you to facing away, you can count them. Nothing on the wrench is marked in degrees. You do not
need to know what a radian is, or that π exists, to find out that it takes some number of clicks, and that a finer
ratchet takes proportionally more.

This essay asks what that count is. Run it backwards: the series has said for some weeks that π and e belong to the
dual hemispherical vantage (DHV), the view that holds the whole turn and the whole scale at once (R909, R922), and that a
read, from one vantage, never holds either. If that is right, then reads and counts cannot *make* π or e. But they can
be counted toward them. How close does a count come, from which side, and where does it land exactly?

The order: clicks to the horizon (§1), what the count gives (§2), where it lands exactly (§3), e from the other axis
(§4), both on one road (§5), where π and e cancel (§6), from which vantage (§7), how hard a test it was (§8), what is
classical and what is ours (§9), and what it changes (§10).

---

## 1. Clicks to the horizon

Take one small read: a direction of slope 1/m, a little up from home. Compose it with itself. Composing two slopes is
tangent addition, s ⊕ a = (s + a)/(1 − s·a), and it needs no angle. Written as a pair [h : v], composing with slope 1/m
is multiplying h + iv by m + i: the new h is m·h − v, the new v is h + m·v. Whole numbers in, whole numbers out. No
division, no square root, no π.

Start at home, [1 : 0]. Each click turns the pair the same way. Count the clicks until the pair passes the horizon, the
point where h stops being positive. Call that count N(m). It is found by integers alone: raise m + i to the n-th power
and look at the sign of the real part. Because each click turns the same way, the real part stays positive until the
horizon, so a binary search on n finds N(m) with a few dozen exact powers.

That is the whole construction for π. A count of equal small reads, from home to the opposite facing.

## 2. What the count gives

The candidate is that 2N(m)/m tends to π. The run took fourteen values of m, from 1 to 100,000, and predicted before it
ran that:

- the count found by integers equals the count the angle formula gives, ⌈π/(2·arctan(1/m))⌉, at every m;
- N(m) − πm/2 lies strictly between 0 and 1 + 1/m for every m ≥ 2;
- so 2N(m)/m lies above π, by less than 2/m + 2/m².

All held. The count of reads matched the angle's count at all fourteen m, with no angle in the construction. At m = 2 the
count is 4 and 2N/m overshoots π by 0.86; at m = 10, N = 16 and the overshoot is 0.058; at m = 1000, N = 1571 and it is
4·10⁻⁴; at m = 100,000, N = 157,080 and it is 7.3·10⁻⁶. Every one is above π. The count closes in on π from above and
never reaches it: π is irrational, 2N/m is a fraction, so no finite m lands on it.

A warning about those digits. At m = 10ᵏ, 2N/m is just π rounded up at k decimals. That is not the count discovering π's
digits; it is the base chosen for m showing through. What the count gives is a fraction that bounds π from above, with an
error that shrinks as 1/m. The digits are the writer's choice of how to name m.

## 3. Where it lands exactly

There is one m at which the clicks do not pass the horizon but land on it: m = 1. Two clicks of slope 1, (1 + i)² = 2i,
put the pair at [0 : 2], exactly on the horizon. Every other m passes it in between two clicks.

This was the other prediction that could have failed, and it is Niven's theorem met from the read's side. At a rational
fraction of a turn, the slope is rational only at 0, 1 and ∞: home, the corner and the horizon. A slope of 1 is the
corner. Two corners make the horizon, i·i = −1 in the landing-point chart (R811, R848). So the only small read that walks
exactly onto the horizon in a whole number of clicks is the corner itself, in two clicks, and no count of any other equal
read ever lands there.

That is a sharper statement than "π is irrational". It says where a count of reads can land at all: on the three places
a read already has.

## 4. e from the other axis

The turn is one axis of Euler's plane, the up one. The other, across, is scale (essay 18). A click on that axis is not a
turn but a fixed share: take what is held and add a fraction 1/m of it. Do it m times and you hold (1 + 1/m)ᵐ times what
you started with, the exact fraction (m + 1)ᵐ/mᵐ. That is Bernoulli's compound interest (essay 15), and it tends to e.

The prediction was that e − (1 + 1/m)ᵐ is about e/(2m), and more exactly that e/2 − m·(e − (1 + 1/m)ᵐ) lies between 0 and
1.25/m for every m ≥ 2. It held. Multiplied by m, that quantity climbed 0.85, 1.14, 1.234, 1.2447, 1.2458 toward
11e/24 = 1.24581, the next term of the classical series, staying under the bound throughout.

So e is approached from below. The two counts close in from opposite sides: π from above along the turn, e from below
along the scale.

## 5. Both on one road

The clicks of §1 were normalized: only the direction of the pair was read. Leave them unnormalized, as 1 + i/m composed
N times, and the pair does not just turn, it grows. Each click multiplies its length by √(1 + 1/m²). After N clicks the
length is (1 + 1/m²)^(N/2). That is the scale axis carried along by the turn, the leftover essay 18 called the length a
count of reads picks up (ELM, R647).

The prediction was that m times the log of that length tends to π/4, within 1/m for every m ≥ 10. It did, within
1.1·10⁻² at m = 10 and 1.8·10⁻⁶ at m = 100,000. Read the other way, the length the turn drags with it is e^(π/(4m)) to
first order, π and e in one expression, each reached only as a count goes on.

## 6. Where π and e cancel

The run began with a question Tom asked before it: when π and e are in the same equation, sometimes they cancel. When?

They cancel along the turn and compound along the scale. Raise e to i times π times a rational r and the result is a root
of unity, an algebraic number, with no π or e left: e^(iπ) = −1, e^(iπ/2) = i, e^(2iπ) = 1. Raise e to π itself, along
the scale, and the result is transcendental (Gelfond and Schneider, 1934); so is e to any nonzero algebraic power
(Lindemann and Weierstrass). Nothing cancels there.

And where the cancellation leaves a rational slope, it lands on §3's three places: home, the corner and the horizon, the
landing points +1, i, −1. Those are exactly the points a read has with no π at all.

The cancellation is also how π's transcendence is proved. Lindemann, 1882: e^(iπ) = −1 is algebraic. If iπ were
algebraic, Lindemann–Weierstrass would make e^(iπ) transcendental. So iπ is not algebraic, and π is transcendental. The
plain landmark −1 is the lever that shows the turn's total is not plain.

One thing that looks like cancelling is not. The normal law (1/2π)·e^(−r²/2) totals 1, but π cancels against the whole
turn's 2π and e against its own radial integral; each constant cancels its own completion, not the other. Where neither
is completed, both stay: Stirling's √(2πn)(n/e)ⁿ keeps π and e side by side.

## 7. From which vantage

Tom's answer to §6 was short: but he considered it from the dual hemispherical vantage. That is right, and it changes how
§6 should be read.

Lindemann, Niven and Gelfond–Schneider all work with the turn completed. They treat iπ as an amount and e^(iπ) as the half
turn swept whole from +1 to −1, holding both facings at once. That is the dual hemispherical vantage, the DHV (R848 found e^(iπ) = −1 the one
member of its family that needs the horizon; R900 the one with no vantage). From the single hemispherical vantage there
is nothing to cancel, because a read never holds π or e. Its −1 is the corner twice, i·i, or w(s)·w(1/s) = −1, rational in
the slope. Its landmarks are given, not reached by carrying e along a turn.

So the cancellation is the DHV's: π and e appear together only because the DHV brings in both, π to complete
the turn and e to complete the scale, and they cancel exactly where the DHV's statement lands back on a point a read
already had. The transcendence of π, read this way, is a statement about the DHV: no finite algebraic step reaches
the completed turn. That is R807 and R808 again, π the DHV's limit, now with a theorem under it.

And the reverse construction of §1 to §5 is the read's side of the same fact. Counts of reads get every member of the
sequence toward π and e exactly, as fractions, and get them from one side only. The limit itself they never make: no
reads or writes, finite or carried to a limit, make the DHV (R922).

## 8. How hard a test it was

Said after the run, as the plan records. Of the six predictions, four could hardly fail once the first held. N(m) is a
ceiling, so if the integer count equals ⌈π/(2·arctan(1/m))⌉, the bounds on N − πm/2 and on 2N/m − π follow by arithmetic,
and so does the length's π/4. The bound on e is the series of (1 + 1/m)ᵐ.

What could have failed was two things. That a count of equal reads, built from whole numbers with no angle, finds the
horizon at the same click the angle says. And that it lands exactly on the horizon only at the corner's two clicks. Both
held at all fourteen m, to m = 100,000, where the pair's coordinates run to about 785,000 digits.

## 9. What is classical and what is ours

Classical, all of it as arithmetic: tangent addition and its Gaussian-integer form, Archimedes' polygons bounding π, Wallis
and the other one-sided approximations, Bernoulli's limit, Niven's theorem, Lindemann, Gelfond–Schneider. The run checked
known facts in a construction with no angle in it.

Ours is the sorting. π is what a count of reads along the turn tends to, from above; e what a count of fixed shares along
the scale tends to, from below. They land on a plain number only at the read's three landmarks, and their meeting in one
equation is the dual hemispherical vantage's (DHV's), since only the DHV completes both. That is a reading, made with the run and not tested
apart from it.

## 10. What it changes

It gives the series' claim that π and e are the dual hemispherical vantage's (DHV's) a construction to stand on. Before, the claim was that no read
holds π. Now there is a count that a read can make, with nothing but whole numbers, and it can be watched closing in on π
and never arriving, and landing exactly only where the corner says.

It also says what a cancellation of π and e is evidence of. When the two vanish into a root of unity, that is not π and e
undoing each other; it is the DHV returning to a landmark a read had from the start. When they do not vanish, as in
e^π or Stirling, both completions are still in play, and the statement is the DHV's through and through.

And it marks the line once more. Every finite count here is exact, a fraction, the same for everyone who counts. The
number it tends to is not a count. A wrench can tell you how many clicks; it cannot tell you π.

---

## Sources

- `../../plans/bld-plan.md`, `../../runs/bld/bld.py`, `../../runs/bld/bld-run1.txt`: the construction, the predictions B0–B5
  committed first, and run 1 (BLD, SPN R1009).
- `../../plans/discussion-note.md` item 18: where π and e cancel (SPN R1008), and Tom's point that it is seen from the dual
  hemispherical vantage (SPN R1010).
- *Reads and Writes* (`../readers-and-writers.md`) §1 "Where π and e are content" and §9 "What is free, and what Ω costs".
- Essay 15 (Bernoulli's bank, what only the dual hemispherical vantage holds), essay 18 (one plane: the turn up, the scale across), essay 24
  (where π and e are only a name).
- Classical: I. Niven, *Irrational Numbers* (1956), the rational values of tan at rational fractions of π; F. Lindemann
  (1882), π transcendental; A. O. Gelfond and T. Schneider (1934), e^π transcendental. Cited as usually stated, not opened.
