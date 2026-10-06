# An audit of SPN Part I: the proved core, checked

*6 October 2026, by Claude, asked by Tom to stay with the math and geometry. Every proposition and corollary of Part I
(1.1, 2.1, 3.1–3.10, Corollaries 3.5 and 3.9) read with its proof, the central hypothesis's derivation read beside them,
and every number in §3.2–§3.3 and §3.8 recomputed. A review, not a ruling. Applied to SPN the same day at Tom's word
("proceed with edits to papers"), each change marked* Corrected *or* the audit *where it stands, and the open question
added to* v and h *§9. Checks: `python3 plans/audit/part_one_checks.py`.*

## In short

The proved core is sound. Every proposition's proof is correct as mathematics, and every figure in §3.2–§3.3 checks
to the digits given. Most of the core is elementary, as R164 asks it to be. There are six things to fix or restate, one
of which matters well beyond Part I.

| # | where | what | weight |
|---|---|---|---|
| 1 | central hypothesis | the derivation proves the corner is mid-octave for **every** ratio between rungs; it does not single out 2 | changes what the hypothesis says, and what would test it |
| 2 | §3.2, the coil | the coil is **not** of Proposition 3.2(b)'s form: f(1) ≈ 0.35, half at s ≈ 1.30 | a wrong sentence |
| 3 | Proposition 3.4 | premise "F increasing" contradicts its own conclusion, the decreasing share h/v | a wrong premise, easy fix |
| 4 | Proposition 3.8(b) | under R175's octaves (×4, corners at 4ⁿh), "the same edges" holds only for even m | stale after R175 |
| 5 | Proposition 3.2(b), Corollary 3.5(b) | "increasing" must be strict; 3.5(b) uses a different symmetry from the R162 it cites | wording |
| 6 | §3.8's reach table | my count gives one octave fewer on every row | probably a counting convention; check `reach.py` |

## 1. The central hypothesis: the 2 counts halves, not rungs

The derivation (central hypothesis, *Why it holds, if the recursion holds*) puts a place f on [0, 1] across an octave,
reads the front half as ρ = f/½ and the back half as ρ = ½/(1 − f), and notes that the swap ρ ↦ 1/ρ sends f to 1 − f, so
the corner, its fixed point, is at f = ½. "So the front half is one h, and the octave is 2h."

That is Proposition 3.2(b) written in place coordinates: any reading on [0, 1] that treats the facings alike has its
middle at the corner. It holds whatever the ratio between rungs. For an octave with two facings from c/r to rc, the one
projective map sending 1/r, 1 and r to 0, 1 and ∞ is ρ = (rs − 1)/(r − s). It is fair to the facings (ρ(1/s) = 1/ρ(s))
and puts the corner at g = ½, for r = 2, 3, the golden ratio and 10 alike (checked to 10⁻⁹). The step "the octave runs
from a to 2a" is assumed at the start of the derivation and not used again.

So the hypothesis as derived has two parts, of different standing:

- **The corner divides the reader's octave in half** ("h is the front half; the octave is 2h" in the place coordinate).
  This is **proved**, on R162, for every ratio. It needs no test.
- **The ratio between rungs is 2** (the doublings: children at 2ᵏ⁻¹h to 2ᵏh, the octaves of §3.3). This is **not
  derived**. §3.3 says so itself: "The doubling is the reader's ratio between rungs, not the geometry's … a ratio of 3
  gives a ladder in threes" (*The Radix* §5; R176).

The run SPN proposes as the one that "could show it, or fail to" (parents and children on signals built on 2, 3 and
the golden ratio; HRT) tests the second part. The paper's sentence "the 2 comes from the corner sitting at the middle of
the octave under the swap" joins the two. Restated, the hypothesis would read: *the corner is the middle of every
reader's octave (proved), and a reader's ratio between rungs is 2 (open: what fixes it)*. It also explains why HRT
could not reach it: what fixes a ratio between rungs is a choice of the reader's or a fact of the world, and no
simulation that builds the reader can find it for us.

## 2. §3.2: the coil is not an instance

"The on-axis field of a circular coil, s³/(1 + s²)^(3/2), has the same form (about 0.35 of its most at the corner) …
These are cases whose near and far laws take the form of Proposition 3.2(b)."

It does not. f(s) + f(1/s) is 0.81 at s = ½ and 2 and 0.71 at the corner, not 1; f(1) = 2^(−3/2) ≈ 0.354, not ½; it
reaches half its most at s ≈ 1.30. The coil favours one facing, like the paper's own s/(2 + s). What is true is the
sentence before: both are powers of s/√(1 + s²). The disc (power 2) is fair to the facings; the coil (power 3) is not.
Only the even power 2 gives f(s) + f(1/s) = 1. The coil belongs with the counterexamples, and it is a useful one: a
classical near/far law whose middle is not at the corner.

The disc, the dipole (both its magnetic share and its electric bracket, s⁴P(1/s) = P(s)) and the round opening all
check, as do the photometrist's 1% (0.99% at s = 0.1), the far-field rule (F = 1/8, s = 0.354, 1.3% off) and Leibniz's
1000 terms (0.00025 short). The cautions the paper gives with the waves stand: choosing h = λ/2π rather than λ is what
puts the dipole's boundary at s = 1.

## 3. Proposition 3.4: "increasing" against its own conclusion

The premise is "Let F be a register on the back side, increasing and positive". Part (b) concludes F = c·sᵏ and then
keeps k < 0, the share h/v, which decreases. Under the premise as written, k > 0 and the conclusion is empty. The
proof never uses "increasing" beyond monotonicity (Cauchy's equation needs only that). **Fix:** "monotone and positive".

A smaller gap: the equation is asked for every unknown b > 0, but F lives on the back side, s > 1, and b·s may fall
below 1. Either define F on (0, ∞), or take b ≥ 1 (the equation on a semigroup gives the same forms). Neither changes
the result.

## 4. Proposition 3.8(b) after R175

3.8(b) says a reader at 2ᵐh has "the same edges" as one at h, counted from 2ᵐh, so its ladder is the lower's slid m
octaves. That holds on the doublings (R167), which is how the proof counts. But §3.3 and §14 record R175 as settled:
the octave is ×4 with two facings, corners at 4ⁿh and edges at 2·4ⁿh. On that ladder a reader at 2h has its corners at
2·4ⁿh, exactly where the lower reader's edges are, and its edges where the lower's corners are. The edges coincide only
for even m. **Fix:** state 3.8(b) on the doublings, as the proof does, and add that on R175's octaves it slides by
m/2 octaves for even m; for odd m one reader's corners are the other's edges. (That last is itself a clean fact: a
factor of 2 in unit swaps corners and edges.)

## 5. Wording

- **Proposition 3.2(b):** "f increasing" must be *strictly* increasing for "s < 1 gives f(s) < ½": a non-strict f can
  sit at ½ over an interval round the corner. And f(1/s) at s = 0 is a limit: f(0) + f(∞) = 1.
- **Corollary 3.5(b):** cites R162, f(1/s) = 1 − f(s), but uses share(1/s) = share(s), which is a different condition
  (the share does not tell the sides apart). The proof itself names it "R161's rule applied to the share", which is
  right. Say that R162 is for readings that tell the sides apart and R161's invariance is for the share.
- **Proposition 3.2(a), on what "forced" means.** The registers are s and 1/s *in the unit h*. Registers s/a and a/s stay
  on [0, 1] for every a. So (a) says: invert at your unit. That is what R164 says the corner is (where v equals whatever
  the reader counts as one), and it is worth saying in (a) as well, so that "forced" is not read as more.
- **Proposition 3.2(b), on what is forced.** R162 is itself the inversion symmetry. What 3.2(b) adds is where the middle
  falls (f(1) = ½) and that each side keeps to its half; the inversion is the ruling, and the corner follows from it.
  §3.2's "What is proved, and on what" nearly says this; "the inversion is forced" would read better as "on the ruling,
  the corner is forced as the inversion's middle".

## 6. §3.8's reach table

Laying N addresses evenly in turn and counting doublings past the corner holding at least 8 addresses, I get 3, 6, 9,
13 octaves for N = 100 … 100,000; the table has 4, 7, 10, 14. The last addresses agree exactly (127, 1,273, 12,732,
127,324 = 4N/π). A difference of one on every row looks like a convention (counting the octave the 8th address is
short of, or from the corner's other side); `reach.py` would settle it.

## Checked and sound

Proposition 1.1; 2.1; 3.1; 3.3 (and the reach of the series, the singularities at ±i); 3.6; 3.7; 3.9; 3.10 (the
square's and circle's reaches reciprocal, direction for direction); Corollary 3.5 and additivity giving v/h; §3.3's
projective octave ρ = 2(s − ½)/(2 − s) (unique, fair to 4.7 × 10⁻¹⁵), the shares of an evenly spread world on doublings
and on ×4 octaves, the 0.053 bound against log₄ s + ½ (at s ≈ 0.70 and 1.43), the 0.011 bound against the share (at
s ≈ 1.53), and the address of 1.37h, (0; 1, −1, 0, 1); §3.8's forward shares 0.5000 … 0.9801 and the last address at
4N/π.

## What would come next, in the same line

- **Restate the central hypothesis in its two parts** (finding 1). The first is a theorem; the second is the open
  question, and a sharper one: *what fixes a reader's ratio between rungs?* Candidates the corpus already has: the
  reader's choice (*The Radix*), the step of its lay (R176's floating-point picture, where base 2 is a hardware choice),
  or the world's payloads (Corollary 3.9).
- **Which near/far laws are fair to the facings?** Among powers of s/√(1 + s²), only the square. A short classification
  (which classical near/far laws satisfy f(s) + f(1/s) = 1, which only have a symmetric bracket like the dipole's
  electric field, and which favour a facing like the coil) would replace "physics has the same structure" with a
  count.
