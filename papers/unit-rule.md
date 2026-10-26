# The Unit Rule, read again

### Holding in order with one slot, in the frame of *Observation from Somewhere*

*Working paper, 26 October 2026 (Tom: "lets clean it up with our new framing from ofs."). This is a restatement of
*The Unit Rule* (21 August 2026), which is kept as received in `papers/archive/the-unit-rule.md` and not edited. Section
numbers in brackets, [§7], are the archived paper's. Every number quoted here was measured in that paper and has not
been run again unless it says so. Where this text and the archived one differ, this one stands (SPN R192). Where this
text and OFS differ, OFS stands, and this text is the one to fix (R421).*

---

## 0. What changed, in one list

The archived paper's machinery holds. Its vocabulary came from before 9 October, and seven of its readings are now
out of date. Each one is restated here:

1. **"The fulcrum" is the corner.** The corner is where h = v, the reciprocal's fixed point, the reading 1. OFS has no
   separate "fulcrum" that the corner leads to. The archived chain *relation → corner → fulcrum → cross ratio → local
   geometry* shortens to *relation → corner → geometry*. The corner is found as a crossing, never as a computed
   equality. The archived paper had that right ("equality is not computed here; it is crossed"), and OFS §2 says the
   same.
2. **One corner, then plain levels.** [§5] said every rung of the ladder "is the corner again, at another scale". It
   is not. There is one corner, the split between the near field and the first level past it. Past it the levels are
   plain powers of one step, with no corner of their own and no recursion (R188, R189). Counting rungs is counting
   levels, not counting corners.
3. **A reading is a ratio, unchanged by scaling the world; a sample or a difference is an amount.** [§3]'s test,
   "what survives the unknown gain", is OFS's test "scale the world" (§9). The ratio of two arrivals is a reading. The
   arrival itself, and the difference of two arrivals, are amounts, stated in a unit the reader was never given.
4. **Holding is its own axis.** The archived paper took "reading is serial" as the definition of a reader. OFS no
   longer defines situations 3 and 4 by serial or parallel (R309): what is received decides the situation, and
   holding, at once or in order, is a second axis. This paper is about one corner of that axis: **holding in order,
   with one slot**. It is not about readers in general.
5. **The Cauchy is the turn's, not the stream's.** [§7, "through the lens"] found the register's cell widths falling
   as cos²θ and called that "the Cauchy". That is the uniform turn's own measure on the reading v/h,
   dθ/d(v/h) = cos²θ. It is the address law, and it says nothing about the arrivals (OFS §7.2: an address is not a
   payload). Where the archived paper tested its rules on "a Cauchy stream of median 10", that is a test stream with a
   heavy tail and no mean, and no claim that amounts are Cauchy (R358).
6. **Dropped:**
   - "Exactly 2/π at the fulcrum" [§7]. The aperture there was scaled by 4/π, so the 2/π was put in by hand, and
     reading it as ψ₁ was numerology.
   - Rapidity's corners "at equal steps" [§7]. Doublings are equal steps on the levels ln r. On the rapidity asinh r
     they come at 0.562, 0.651, 0.682, 0.690, 0.692, tending to ln 2 only far out (OFS §6, "One figure, three rulers").
   - "The arrivals have no mean" for a body's elements [§18]. The directions to a bounded body are bounded, have a
     mean, and are not Cauchy. A mass-weighted disk at distance 20 has KS 0.108 against the Cauchy (`plans/archive-gems.md`).
7. **No claim about who reads this way.** [§5] said "biology got there first". That is a claim about readers. OFS says
   only that a reader *should* draw V = H, and leaves open whether any reader does (R261, R262). The many
   logarithmic scales in use (decibels, magnitudes, pH, octaves) are kept here as a pattern worth noticing, not as
   evidence.

The rest of this paper is the archived paper's results, in that order and in these terms.

## 1. The situation

A screen receives a broadcast: a stream of amounts, one at a time, each multiplied somewhere along the way by a gain
no one recorded. The same broadcast through another chain arrives a thousand times larger. In OFS's terms this is a
writer's account (amounts) reaching a reader that holds no unit for them. The scale of the world, k, is unknown and
cannot be read.

The question [§1]: **what can a reader holding one slot state truthfully about such a stream, and what does it cost
to find the corner in it?**

What the reader has [§2] is to receive an arrival, hold one value, compare the arrival with the held value, emit a
symbol, and count looks. The comparison is settled by something outside both parties: a comparator, or gravity in a
balance. That outside agent qualifies only if it cancels from the result (§3 below). Nothing on the list needs to know
what the stream is.

## 2. What survives the gain: the test, scale the world

Multiply every arrival by k and see what moves [§3]:

- **An arrival moves.** It is an amount.
- **A difference moves.** It is an amount too.
- **A ratio of two arrivals does not move.** It is a reading.

This is OFS §9's test, run on a stream. The first statement the reader can make about the broadcast, rather than
about the chain it came through, is one arrival in terms of another.

The same test applies to the instrument [§3, "turned on the instrument"].
- **A balance passes.** Its field cancels from the equilibrium: sweep the field over twelve decades and the read
  does not move. Bias one side and the read drifts at first order, which shows the cancellation is doing work.
- **A spring scale fails.** It reads mass × field ÷ stiffness, so it must be calibrated, and only locally.

The class of instrument the reader belongs to is defined by this: the settling agent decides *that* a result occurs
and contributes nothing to its value. A second, independent condition is who powers the settling. If the agent
does, looks are free. If the arrival does, each arrival is spent in being read and gives only finitely many looks.
Both are classical.

## 3. One slot: the hold and the arrival as a direction

Holding in order needs something already held to read the arrival against [§4]. Call it **the hold**. Each look
states one reading, the arrival in terms of the hold. In OFS's notation that is the direction **[hold : arrival]**,
with v/h = arrival ÷ hold.

The landmarks are OFS's:
- **home**: the arrival is nothing, v/h = 0, and the screen shows black truthfully;
- **the corner**: the arrival equals the hold, v/h = 1;
- **the horizon**: [0 : 1], approached as the hold becomes small against the arrival.

A bounded register cannot follow the reading to the horizon. Past its last level everything reads the same, and that
clip is the register's edge, not an error.

**The first arrival is not a reading.** Alone it fails the test above. It founds the hold and says nothing.

The archived paper specified the reader as four pieces, each with a price paid in state and never in a unit [§4,
"The reader, specified"]:

| | capability | what it needs |
|---|---|---|
| 0 | reception: arrivals in order | nothing |
| 1 | relation: the arrival read against the hold | one held value |
| 2 | representation: the reading named by its level | a step g (§4) |
| 3 | continuity: something held across the gaps | a carry rule (§5) |
| 4 | landmark: the corner crossed, and counted | a direction bit, two counters |

No row needs the stream's scale. What grows down the table is memory.

## 4. The levels, and the step

The register names each reading by a whole number of steps of a ratio g > 1 [§5]: the level n nearest
log_g(arrival ÷ hold). The run of those numbers is the record.

- **The step is the reader's, not the stream's.** Nothing in the broadcast recommends a g. A finer step buys
  resolution and costs levels.
- **One step, repeated, is the only discrete design.** Every discrete subgroup of the positive reals under
  multiplication is {gⁿ}. Two incommensurate ratios, such as 2 and 3, together are dense (OFS §5, "Levels are one
  ratio repeated").
- **The count of levels is a logarithm in integer form.** "How many steps of g from the hold to the arrival" is
  log_g, rounded. The reader computes no logarithm; the logarithm is the completion of its count. This is the same
  statement as OFS's lay past the corner, 1 + ln s by address count. Restated from [§5], with the corrections of §0:
  the levels are a count of steps, not of corners.
- **A logarithm of one amount is not formed.** A level needs two magnitudes, a hold and an arrival. "The log of five
  metres" is not forbidden; it is not yet a reading.
- **The count does not carry the world's size.** Scaling the stream shifts the hold's level and leaves every reading
  where it was, while a pass over the whole world carries a cost that scales with it. This is OFS's "K apart from N"
  in a stream: the reader's count of levels is fixed and prior to what arrives.

### Odd and even K

The archived paper's §8 is OFS §8's "odd and even K":
- **K even:** the corner, v/h = 1, falls on a boundary between two levels.
- **K odd:** one level is centred on the corner and means *nothing changed*.

For this reader that is not a matter of taste. A one-slot reader shown a still scene is handed its own hold, look
after look, and its reading sits exactly on the corner.
- With 31 levels it returns the hold × 1.00000.
- With 32 it must round half a step one way or the other: × 1.01815, a twitch on every look of a scene that is not
  moving.

So the rule of §5 needs an odd K. In general, OFS takes neither as wrong: odd K gives the corner an address, even K
makes it a boundary found without a length. Only a reader that must name stillness needs the odd one.

## 5. The unit rule

The stock taken at the end of a look [§6]:
- the old hold, in a slot;
- the arrival just read, in a slot;
- the count of looks.

Nowhere is there a rate, a trend or a step toward the future. "Carry the hold forward by s" needs an s, which is an
amount. "Continue the motion" needs a motion, which is a difference, which is also an amount. **The only magnitude
the reader holds is the one that just arrived.**

So the rule [§7]:

> **Hold the arrival that filled you, until the next one says otherwise.**

It is zero-information and not zero-state: it assumes nothing about the stream and costs one slot. Every capability
added later is paid for in state, never in a unit.

**Where the name comes from.** The held value is the reader's unit for the moment. The archived paper also noted
that the rule is silent on a circle read from its centre: every look returns the hold, so the record is nothing at
all.

In OFS terms that last point is a fact about one reading of one figure. Read from its centre with one direction at a
time, a circle gives the same radius in every direction. So the reading stays at the corner and the reader holding
in order has nothing to emit. It is not the general statement that "every rule is quiet on the shape it believes in".
That one is kept in §8 below, scoped.

**Two outputs** [§7, "two outputs"]:
- **A level**: each arrival placed against the hold, which is what makes the stream readable.
- **The corner, as an event**: the look at which the reading crosses 1. This is the same for two readers with
  different steps and different gains, because a crossing of 1 needs no scale.

**Reference and carry are two jobs.** A rule governs either the reference (what the arrival is read against) or the
carry (what is held between looks when nothing arrives). The unit rule does both with one value. The contenders of §6
change the reference and leave the carry alone. A rule told the stream is smooth interpolates the carry and leaves the
reference alone. Only the carry concerns the gaps.

**The space of rules is open, and on the reader's side.** For every known stream some tailored rule beats this one,
and pays for its advantage with information about the stream. The unit rule is the one member a reader given nothing
can run.

### The corner follows the focus: reading is seeking

[§7, "Reading is seeking — the proof"] is OFS §8's "the corner follows the focus" for a reader holding in order. The
premises, in rungs:
- **A1.** The reading is r_n = x_n − y_n, the arrival's level less the hold's.
- **A2.** The register is finite: the reader is reading while |r_n| ≤ R, and clipped otherwise.
- **A3.** The stream steps at most J levels a look, and is told nothing of what the reader holds.
- **A4.** The reader knows no window the stream will stay in, since that would be a unit.

The argument:
- **Lemma.** A hold that never moves is clipped after finitely many looks for some admissible stream.
- **Theorem.** A reader reads every admissible stream exactly when its hold tracks the arrivals, |x_n − y_n| ≤ R. It
  must keep returning to the corner.
- **Corollary.** "Hold while |r_n| ≤ 1, else move the hold to the arrival" keeps |r_n| ≤ J with no model of the stream.
  The price of knowing nothing is a bounded lateness, one of the stream's own steps.

The hysteresis band here, hold until the reading leaves ±1, is the same device as `fpv-plan.md` run 5's hold band.
There it was L = 0.4 nats, re-laying the corner on 5% of looks for 1% more grain. The two are one device found twice:
a reader moves its corner only when the look has left a band about it.

What the snap buys is not accuracy but **stretches of agreement**. At the look where the hold moves, the reading is
exactly 1. Until the next look contradicts it, one statement holds for the whole stretch. The record is the list of
those stretches' ends. A predicting rule moves its hold every look, so it has no stretches and no ends.
- On a random walk, the predictor's reading changes sign at 67% of looks, autocorrelation −0.50: a beat.
- The unit rule's changes sign at 31%, autocorrelation +0.42: a drift. Over 2,000 looks it holds 1,622 and moves 378
  times.
- Where a model is exactly right (a constant trend), the predictor sits at agreement every look and the unit rule
  wobbles ±0.30. A predictor's stillness is borrowed from its premise; the unit rule's holds whenever nothing has left
  the band.

Measured [§7], 20,000 looks, R = 15, J = 1:
- **A fixed hold** is clipped on 18,087 (random walk), 19,975 (trend) and 18,350 (turns every 200) looks.
- **The unit rule** is never clipped. Worst readings 1.99, 1.20, 1.80.
- **A linear predictor** is never clipped. Worst 1.98, 0.60, 1.80. Its advantage is gone once the stream turns.

### The side bit: the median, at the corner

[§7, "the drift of the corner value"]. An arrival above the hold or below it is one bit, and needs no collection.
Step the hold toward whichever side is short and it settles on the arrivals' median. That is Robbins–Monro's sign
rule (OFS §7.6, "a median in two registers").

The median, not the mean, is the reading's centre, since the median commutes with every increasing change of what
arrives and the mean does not (OFS Theorem 6(c)).

On the archived paper's heavy-tailed test stream (a Cauchy of median 10, a test stream only, §0 item 5):
- **The drift's sign** turns exactly at the median: +0.77 a look with the hold at 2, −0.02 at 10, −0.93 at 40.
- **The hold** settles at 9.25 while the running mean wanders to 16.09.
- **On a lognormal**, the hold settles at 1.11 against a median of 1.00, with the mean at 1.69.

**What the horizon does not license.** Once the hold sits at the median, the far arrivals cancel: of 50,335 past 16,
24,145 were above and 26,190 below. That says only that they no longer move the hold. It does not license ignoring
them. Clipping before the hold has settled strands the reader: at four rungs from the start it ignores 99.8% of looks
and leaves the hold at −101 on a stream of median 10. Nor does a lens widen the view. A fisheye respaces the facing it
looks through and leaves the horizon where it is (OFS: a facing reads one sign of each relation; the other facings
are other wedges).

### One facing, four facings

[§7, "what one atom licenses"]. A closed relation, a writer going once round, turns through four facings. A reader
that has found the corner and one turn knows where the other three turns fall and how many there are. It does not
know when they come, since the schedule is the stream's:
- **On a circle** the four facings took 1023, 1024, 1024 and 1025 looks.
- **On a five-point star** they took 1101, 946, 947 and 1102.

It does not know what lies between them either. In OFS's words: one facing is one array, and joining the four is the
writer's, who knows their sizes (§7.3, R368, R369).

**The near field in proportion, the far field in reciprocal** [§7, "the two halves"]. Below the corner θ ≈ v/h
(0.4636 rad against ½ at v/h = ½). Above it π/2 − θ ≈ h/v. The archived table's θ/r and (π/2 − θ)·r are mirror images
about the corner, row by row. Past the corner, the reading becomes the hold as a share of the arrival: the exchange of
the two relations, the reciprocal, fixing the corner (OFS §4).

**The levels are a third ruler.** Doublings at v/h = 1, 2, 4, 8, 16, 32 sit at 45°, 63.43°, 75.96°, 82.87°, 86.42°,
88.21° on the turn, halving toward the horizon, and at equal steps on ln(v/h). The register's ladder, the reader's
turn and the level are OFS §6's three rulers. Name which one a claim is made in.

## 6. The races

[§9–§14] raced the unit rule against rules that were meant to beat it, on 49 recorded test signals. Each signal
returns to where it began, so an honest record should sum to zero. Scores:
- median error in levels;
- worst look;
- closure, the number of records out of 49 that summed to zero;
- the bill, in bits a look.

These are the archived paper's measurements on its own library. They test a writer's question, how closely the held
values track the stream's amounts. They are kept because they price the rule, not because OFS needs them.

| | result |
|---|---|
| **The unit rule's own frontier** [§9] | Median error falls as about 2^−bits with no knee: 0.0132 at 0.635 bits, 0.0064 at 1, 0.00020 at 4.5. Any rival must beat this line, and the unit rule can buy any point on it with levels. |
| **Auto-exposure, a tailored step** [§10], 31 levels | Median 0.0027 against 0.0064 (2.3× better). Worst look 0.0399 against 0.0136 (3× worse). Closure 2 of 49 against 49 of 49. A step that changes during the run states its symbols in different units, and the sum stops telescoping. |
| **Levels instead** [§10] | The unit rule at 63 levels, same bill: median 0.0031, worst look six times better than auto-exposure's, closure 49 of 49. |
| **A second slot** [§10, "the other fork"] | Continuing the motion as a ratio of two held values is legal (no unit). Smooth scenes cheapen (13%, 10%), cornered ones get dearer (54%, 28%), error per look unchanged, and the checksum drifts. Holding k values costs exactly 2^(k−1) times the one-value bill, and every k builds the identical reconstruction (exact integer arithmetic). |
| **The exchange rate, made fairer** [§11] | 5× with a handicapped baseline; 2.34× at matched guarantee; 1.15–1.18× at matched bill; 2.52× only with the certificate given up. |
| **An oracle** [§12] | 28× with the whole schedule in advance. Another scene's schedule 21×, its own shuffled 24×, a constant fine step willing to clip 22.7×: four fifths of it is a finer level. 1,921 levels match its median and beat its worst case 28× at the same bill. Offset by one sample it clips 536 times, worst 0.408, median unmoved. The failure shows only in the channels not watched. |
| **The certificate** [§13] | The adaptive family has a closed-form worst case the register can evaluate. The unit rule is its degenerate case, half a level. At growth exactly 1 the bound diverges, and the register follows it. |

[§14]'s statement stands as it was: **at a matched bill with certificates kept, sophistication buys about 1.2×.**
Every larger figure was levels in disguise, a handicapped baseline, or a surrendered certificate. Beating the rule
costs information about the stream, and when that information is wrong the cost is paid in the worst look, the clip
count and the certificate.

## 7. The corner as a landmark

[§14a] is where the rule wins by more than 1.2×. The question there is not "what was the level" but "where did the
stream turn". A turn is the sign of the reading changing: the arrival stops exceeding the hold and starts falling
short of it. Two readers with different steps and gains agree that it happened.

**Why a landmark matters more than a level.** A count of looks between two turns is a duration in the stream's own
terms. Within it, the corner is found by counting, with no unit. So the reader carries a reference it was never
handed.

In OFS's words: the corner is free, a crossing, and needs no amount (§2). What the archived paper called "founding its
own unit" is designating, not sizing (R214). The landmark is a place in the stream, not a size of anything.

**The race in the gaps.** The rules differ only across missing looks, so looks were dropped, singly and in bursts.
Same machine, same landmark logic; only the carry differs. Error in the corner's place:

| looks dropped | unit rule | carry the trend | decayed blend |
|---|---|---|---|
| none | 1.61% | 1.61% | 2.44% |
| one in five | 2.08% | 2.01% | 2.82% |
| half | **3.01%** | 60.58% | 4.31% |
| four in five | **6.55%** | 27.28% | 8.91% |
| bursts of 20 | **1.72%** | 23.41% | 2.56% |
| bursts of 200 | **1.66%** | 11.24% | 2.51% |

Tested exactly since (UNR, `plans/unr-plan.md`, 26 Oct): the unit rule's turns are unchanged by every strictly
increasing change of what arrives, a trend rule's are not; each carry's turns move under exactly the maps its reference
does not commute with. With noise and a threshold (UNR run 3): an order-only debounce keeps that invariance and pays in
noise; a threshold in levels keeps only the scale of the world, one in amounts neither. The unit rule is flat across burst length. The structural reason: **a carry that extrapolates is most wrong exactly at
a turn**, the one place where "it went on as it was" is false by construction. The unit rule's carry grows wrong in
size across a gap but asserts no direction, and direction is all a turn needs.

**The machine** [§14a, "The machine"]. A rod turning steadily, its projected extent read once a look. A leg runs
between two low reversals, a half turn. The corner of the rod's two projections, where they are equal at 45°, falls a
quarter of the way along the leg.

Four registers find it:
- the hold;
- the direction bit;
- a counter from the last low reversal;
- the previous leg's count.

The quarter needs no division: a counter ticking every fourth look holds the count quartered (a ripple counter's
bit 2).

Count from the low reversals only. A reversal at the top is flat, so it is noticed late; one at the bottom is steep,
so it is noticed promptly: 65 looks late against 11.

Measured:
- **Clean signal:** 1.9%, and 0.2% with the detection lag removed. All of the error is the threshold's lateness.
- **Noisy:** 1.9% at 0.4% noise, 3.1% at 1%, failing at 2%.
- **Self-correction:** correcting its own lateness improves steady streams (1.9% to 1.4%, 3.1% to 1.6%) and worsens
  every unsteady one.
- **Against a reader that keeps every arrival and sorts them:** that reader does better, 0.05%. The four-register
  machine is not more accurate; it is possible on a stream without end, with memory that does not grow.

**When the world supplies no single turning thing** [§14a, "When the world will not supply a circle"]. Six real
signals were tried: four handheld video clips, a chirp, a ride cymbal, a fire alarm, a voice. All were refused, each
for a named reason:
- the video wanders, held flat by automatic exposure;
- the chirp returns only after it stops sweeping;
- the cymbal, the alarm and the voice are several periods at once.

One way through: divide the arrival by its own increment. For anything locally sinusoidal the ratio is the tangent of
the phase, an address, and the gain cancels. From that, cross ratios came back exact to 10⁻¹⁰–10⁻¹⁵ on every stream,
the video included. But it cancels the gain, not the shape:
- **Two components** (f·sin over f·cos) return the same number for four figures, a spread of 0.0000%.
- **One list over its own increment** (f·sin over f′·sin + f·cos) returns four, a spread of 87.6%.

Where the corner falls on this reading is the signed sweep's: with the phase uniform over a signed half turn, the
reading is below 1 three quarters of the time. So home is that range's median and the corner its upper quartile. The
archived paper read those quartiles as home and the corner in general; they are this sweep's. OFS's corner is the
median of one facing.

And the frame is exact over any arrivals at all: white noise gives a crossing and a cross ratio as cleanly as a tone.
**Its exactness is no evidence that it refers to anything.**

### Every rule's corner marks what that rule believes

[§14a, "What the other rules' corners mark"]. Every rule holds something, so every rule has a look where the arrival
meets the hold. What that look is about depends on what is held:
- **The unit rule** holds the last arrival. Its corner says the stream did not change, a statement about the stream.
- **A trend rule** holds a forecast. Its corner says the forecast came true, a statement about the reader.

On a turning rod, corners near a turn against corners on a flank: unit rule 31.5% against 13.4%, trend rule 21.2%
against 41.5%. The unit rule's corners gather at the turns, the trend rule's on the straight stretches.

The same law names the unit rule's blind spot. A stream climbing exactly one level a look is as quiet to it as a
still one: a geometric ramp is all corners under every rule.

## 8. What the record is

**A projection, not a loop** [§15]. Every value the unit rule holds is a level of the lattice anchored at the founding
arrival, and rounding from any level lands on the level nearest the arrival. So the held run is the nearest-level
projection of the stream, independent of path. This was verified in exact integer arithmetic on every sample of 56
scenes. The error in the last tenth of a run against the first is 1.03×, and 1.1× with 5% noise. A held value grows
stale within a gap; it does not decay across a run.

**Continuity is the reader's** [§16]. Arrivals come one at a time; the held run is unbroken because the reader holds
something between looks. What is forced is that there is a carry rule (even "hold nothing" is one, and gives a
strobe). Which rule is not forced. The unit rule is the one a reader given nothing can run. Continuity in the record is
the carry rule, whatever it is.

**Two checksums** [§17], and both are needed:
- **The sum of the symbols** telescopes to zero on a returning scene. It ignores order.
- **The sequence of crossings** (corners passed, clips) must come round to where it began. It keeps order.

Neither implies the other. Both refute and neither confirms: a scene ending within half a level of its start rounds
to "returned".

> **An open record proves the scene did not return. A closed record does not prove it did, and how much it can refute
> is set by the step.**

Closing also needs the horizon resolved [§7, "closing the shape"]. On a loop of 40 levels, every reach from 64 down to
4 closes while the largest step between looks is 1.1 levels. At 40 looks a lap, a reach of 4 is clipped on 152 looks
and the record sums to −30, the same −30 every lap: the excursion past the horizon, lost the same each time. So the
two conditions are separate:
- **The corner agreed:** the hold sits on an arrival's level, so the sum telescopes.
- **The horizon resolved:** no step outruns the reach, so it telescopes to the right total.

## 9. What the archived paper found about periods, in this frame

[§18]'s late results concern one stream divided by its own increment. For a single tone the looks in a cycle are the
corner's count × 2.6026, and the period comes back from 55 Hz to 3 kHz within 0.01–1.01%, unmoved by any scaling of
the list. The resolution check is how many looks a quarter turn gets: 50 for a tone, 9 for a voice, 4 for a cymbal,
0.9 for noise.

In OFS's frame, the ratio is a direction (the phase's address) and the period is order and counting: both readings.
The shape cancels because the reading is a direction. That is Theorem 6(a): the reach of what arrives cancels from
every reading.

[§18] put it well and it is kept: **if the shape survived into the reading, the rate could not be recovered**.
- **Swept at one rate and read as a direction,** a circle, an egg, a clover and a burr give one period, a spread of 0.
- **Read keeping the shape,** they spread over seventy percentage points.

A body that swings under its own physics writes its form into its period (the moment of inertia). So five bodies of
one size give periods within 2%, and the ratios of those periods, with no unit and no clock, land within a few
percent of the mechanics.

One reading in [§18] is corrected. The directions to a body's elements locate its centroid (a disk to 0.019%, a bar to
0.028%), and their spread is its angular size times a constant of its arrangement. Those are the payload's moments
(OFS §7.6; `plans/pay-plan.md`'s photocentre). They are not Cauchy, and they have a mean (§0 item 6). The archived
claim that "the mean estimates nothing here" does not hold for a bounded body. The reason to take the median remains
Theorem 6(c), not a missing mean.

## 10. Open, as the archived paper left it

The machinery is closed; its use is not. Three tests would decide it, and none has been run:
1. Does the corner found this way follow a change in the world, or only in the sampling?
2. Do two readers at different rates agree, once each counts in levels from its own corner?
3. Does the frame earn anything where a unit is available anyway?

To these, OFS's frame adds a fourth:

4. **Is holding in order with one slot the reader of `fpv-plan.md` run 5?** The hold band there and the hysteresis
   here are one device, and run 5 already measured its price on a gaze trace. A test would race the unit rule's ±1
   level band against run 5's L on the same trace.

What the paper is, in one sentence:

> **The unit rule is what a reader holding in order with one slot does before it has been told anything. It finds the
> corner as a crossing, keeps the record as a projection, and pays for every further capability in state, never in a
> unit.**
