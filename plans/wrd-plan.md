# WRD: what readers actually do — the outline free, the amount carried in

*18 October 2026 (Tom's local date). After CFH, Claude said the result is important inside the corpus and not new outside.
Tom: "it may be important if this is what readers actually do, not engineerd to do." Claude listed four predictions the
geometry makes for real readers, with what the perception literature already has, and offered a prediction-first plan
against published data. Tom: "yes". This is real data, not wander's world; the bridge is named in each prediction.*

## What the geometry says a real reader does

OFS §9 ("From one place: the outline is free, the face is carried in"), CFH and R297/R307 give four claims:

1. **Timing comes free.** A reader times its actions from ratios read off directions, with no distance: τ from the
   looming of what it sees.
2. **Absolute size needs an amount the reader holds.** For an animal that amount is its own body, for instance its eye
   height or the gap between its eyes.
3. **Absolute range from an emitted signal is writing.** The reader trusts a speed it already holds. If the medium's
   speed differs from it, every range is off by exactly one factor, the held speed over the true speed. A ratio of two
   ranges, or a range over its own rate, is unchanged.
4. **Silhouettes show outlines and hide hollows.**

## Known beforehand

- **Claim 1:** Lee (1976); Lee and Reddish (1981). Diving gannets fold their wings at a fixed τ, not at a fixed height.
- **Claim 2:** Ooi, Wu and He (2001): distance on the ground is judged from the angle below the horizon, scaled by eye
  height. Warren (1984): stair climbing is judged by the ratio of riser height to leg length.
- **Claim 2, partial in people.** A search result, read before this plan: Dixon, Wraga, Proffitt and Williams (2000)
  set the virtual eye height to 0.7 of the real one. Size judgments shifted, but the manipulation was about 77%
  effective, not the full scaling a reader with eye height as its only amount would show. Kim and Interrante (2017)
  found no significant effect of ±50 cm. People hold several amounts and weigh them; this plan does not test that.
- **Claim 3:** Simmons (1973): bats read range from echo delay.
  - Amichai et al. (2021, *PNAS*, doi:10.1073/pnas.2024352118): bats reared in normal air and in heliox were flown to
    a target 1.3 m from their roost, in air and in heliox. In the heliox the speed of sound was 15% higher.
  - Read before this plan, from a search summary: adults did not recalibrate over days.
  - Also read before this plan. While extracting the methods I read, by mistake, the opening of the paper's results.
    It says that in heliox both groups judged the target closer, with no difference by rearing (an innate reference),
    and that the bats began their flight already in the approach's final phase.
  - So the direction of the effect and the innate reference are known beforehand. Its size is not: I have not read the
    paper's estimate of the perceived distance (its sections "Estimating the Bats' Sensory Perception", Tables 1–2,
    Figs. 2–4, Dataset S1).
- **Claim 4:** Koenderink (1984): the occluding contour shows the surface's convex parts and hides its hollows.

Claims 1, 2 and 4 are already in the literature, so this plan does not test them. Claim 3's sharp form is the geometry's
own: one factor in every amount, and nothing in the ratios. That is what is tested here, on the one published case
found where the medium's speed was changed.

## Set-up

The source is Amichai et al. (2021), read from PMC (PMC8126842; the page's sha256 is
7e484a369446edca9b17953065c80815c9c1dab0fcdab7e76a3f20e0e3494985, not committed), and its Dataset S1 if it can be had.

**The bridge.** A range read from an echo is the delay times a speed held by the reader, halved. The delay is the true
range times two over the medium's speed. So the range read is the true range × (held speed / medium's speed).

- With the held speed the air's and the medium's 1.15 times it, the range read is 1/1.15 = 0.8696 of the true range,
  13.0% short.
- It is not 15% short; that would be the naive reading of "15% faster".

### Predictions

- **W1 (one factor, the held speed over the medium's).** Where the paper estimates the distance the bats perceived in
  heliox from a 1.3 m target, that estimate is 0.8696 × 1.3 = 1.13 m.
  - It is to fall within [0.80, 0.94] of the true distance (8% to 20% short).
  - Where the paper gives a confidence interval or a spread of individual estimates, 0.8696 is to lie within it.
  - *Killed* if the central estimate falls outside [0.80, 0.94], or if 0.8696 falls outside the paper's interval.
  - *Untested*, and I say so, if the paper gives no estimate of the perceived distance in metres or as a share.
- **W2 (the same factor whatever the rearing).** The perceived share is the same for air-raised and heliox-raised pups,
  and for adults, within 0.05. The factor is set by the speed held, and that speed is innate.
  - Its qualitative form is known beforehand (above). The test is the numbers, if the paper gives them per group.
  - *Killed* if two groups' estimates differ by more than 0.05. *Untested* if the paper does not give them.
- **W3 (ratios untouched, where measured).**
  - The bats still reach the target in heliox: they land on it, not short of it. The geometry places them by direction,
    and a mis-scaled range shifts only when they act, not where they go.
  - If the paper reports landing success in heliox, it is not below that in air by more than half.
  - *Killed* if it is. *Untested* if not reported.

W1 is the test. W2 and W3 are subsidiary, and W3 is the weakest: flight in a denser gas changes more than the sound.

## What would and would not be shown

- **What would be shown:** whether a real reader that ranges by echo holds one amount, a speed, and puts every range
  off by exactly that amount's error. That is what the geometry says a ranging reader is: a writer through one carried-in
  amount.
- **What would not be shown:** whether readers draw V = H; claims 1, 2 and 4 (in the literature already); anything about
  vision.

A pass is consistent with the reading, and is classical physics of echo ranging. What the reading adds is the
classification: the bat's error is an amount's error, and the ratios are free.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (18 Oct, the paper's text, read from PMC8126842 after the predictions were committed)

The rest of the paper was read for what it reports on each prediction.

- **W1 untested in its letter.** The paper gives no perceived distance, in metres or as a share, for the 15% condition. It
  reads the bats' range from two echolocation parameters taken before takeoff: the interstrobe interval (ISI) and the
  call duration (Dur).
  - Its one quantitative comparison is at 27% SOS. There the bats' parameters toward a 1.3 m target were "similar" to
    those toward a 90 cm target in air. The methods call 1.3 m in 27% SOS "equivalent to ∼95 cm in air".
  - That equivalent is 1.3 × (1 − 0.27). The echo's delay gives 1.3/1.27 = 1.024 m, a share of 0.787. The paper's 95 cm
    is the naive form this plan set aside.
  - Two calibration distances (90 and 130 cm) and "similar" cannot tell 0.69, 0.73 and 0.79 apart. No interval is given.
- **W2 untested in its letter.** No per-group share is given.
  - The paper's tests find no difference by rearing: the effect of rearing origin P = 0.62, the response's magnitude
    P = 0.65. Every adult in every heliox level (10%, 15%, 27%) read the target closer, with no change over 3–13 days.
  - Consistent with W2; not a numerical test.
  - The discussion adds: "the bats regarded the object as being 7.5 ms away and not 1.3 m away". That is 2 × 1.3/343 s,
    the delay in air.
- **W3 killed at 27% SOS.** Every flight in air landed. In 10% SOS about 51% landed, half of air's, so W3 passes there by
  a hair. In 27% SOS about 3% landed. At 15%, of the two bats filmed, one landed at all.
  - The paper puts the misses mostly to lift in the lighter gas ("category I": short flights to the floor). Its
    "category II" misses cover the whole distance and pass just under the target, "arguably due to sensory error". Flight
    speed was the same in air and heliox (1.5–1.6 m/s).
  - The plan called W3 its weakest for this reason. It is killed as written.

**Reading.** The published case agrees with claim 3 in kind:
- one held speed;
- every range read short in every heliox level;
- no recalibration, in pups raised in heliox or in adults over days.

The paper's own reading, that bats "encode the world in terms of time and do not translate time into distance", is the
same claim seen from the other side. A reader that holds a fixed speed and one that holds only the delay act alike: in
either case the one amount carried in is never re-measured. The size of the factor is not settled by the text. The data
may settle it (run 2).

### Run 2: the factor from Dataset S1 (written before the dataset is opened)

**The data.** Dataset S1 (`pnas.2024352118.sd01.xlsx`, from PMC; its sha256 to be recorded, not committed): the
per-flight pretakeoff ISI and Dur.

**The method, fixed now.**
- Calibration, per adult bat that flew both targets in air: the median ISI toward 130 cm and toward 90 cm. Distance is
  taken as linear in ISI between them.
- A heliox condition's perceived distance is the distance at which that line gives the median ISI in the heliox
  condition. Its share is that distance over the true distance.
- The same is done with Dur, as a second reading.
- Pooled over bats: the median share and its range across bats.

**The predictions.** The share is 1/(1 + x), for x the SOS increase the paper states:
- 27% SOS (1.3 m target): 0.787, 1.024 m;
- 15% SOS (1.3 m): 0.870;
- 10% SOS (0.9 m target): 0.909, 0.818 m. That lies below the 90 cm calibration, so it is an extrapolation and the
  weakest of the three.

The kill conditions:
- **W1′ (27%):** the pooled ISI share within ±0.06 of 0.787.
  - It is also to lie nearer 0.787 than the paper's 0.731 (95 cm) when that difference exceeds the range across bats;
    otherwise this clause is untested, and I say so.
  - *Killed* if the share falls outside 0.787 ± 0.06.
- **W1″ (15%, 10%):** within ±0.06 of 0.870 and 0.909, where the dataset has the flights. *Killed* if outside.
- **Untested**, and I say so, if the dataset lacks per-flight ISI by condition, target distance and bat.

Run 2 has not run: the dataset could not be reached from this environment. On 18 October:
- PMC answers the file's link with a proof-of-work page, which I did not try to get past;
- Europe PMC says the article is not in its open-access set;
- pnas.org does not resolve.

The predictions above stand as written, for whenever the file can be supplied.
