# MSR: the dial's sorting on measured content

*26 November 2026. Tom: "Yes, write the plan for 1", item 1 of Claude's list after RAH: every test of the day (TBH, RAH,
FAB, DBR) confirmed the sorting on content built for it; this one puts measured content behind the dial. Plan only;
predictions written before any data is fetched or any script (`runs/msr/msr.py`) exists.*

## What can fail here, and what cannot

The bridge's properties are theorems: on any content a window rebuilt as its own bridge is exact at its leaves, costs K
terms a read and carries no N. Measured data cannot contradict them. What measured data can contradict is the claim
about **content**: that something with no size of its own is ratio content, held at the same cost by a window in ratios
wherever along its list the window is put, and that something with a size needs a window in its own units. So the test
takes one measured list believed to have no size of its own and one with a known size, and asks how many leaves each
window needs, centre by centre. If the believed-scale-free list needs a very different K in different decades, it is
not ratio content there, and the sorting has to say so.

## Data

- **Without a size, believed: word frequency by rank.** The training split of WikiText-103 (`Salesforce/wikitext`,
  wikitext-103-raw-v1, Hugging Face; licence CC BY-SA 3.0), split on spaces, case kept; counts sorted into ranks. Zipf's
  law says the count falls as a power of the rank, roughly the same shape in every decade; the literature also reports a
  bend between a head and a tail (two regimes), which is what could break the prediction. Source, retrieval date and
  sha256 recorded under Runs; the data not committed.
- **With a size: a tide.** NOAA's verified hourly water level at San Francisco (station 9414290), calendar year 2025
  (`api.tidesandcurrents.noaa.gov`, the same service as UNR; public domain), metres above MLLW against hours from the
  first sample. Its principal period, 12.42 hours, is a size in hours.

## Set-up

The content is read as a function along its list. Zipf: z(r) = log₁₀ count at rank r, smoothed over ranks within ±2% of r
(a ratio-scale smoothing), interpolated linearly in log r between ranks. Tide: water level, interpolated linearly
between hours. Windows, as in DBR: **in ratios**, x in [c/4, 4c] read in y = (x − c)/(x + c); **in records**, x in
[c − w, c + w]. Leaves at the Chebyshev nodes of the window from the lattice (`runs/dbr/dbr.py`'s `cheb`), rebuilt by the
barycentric formula. For each window, K* is the least K in {6, 8, 12, 16, 24, 32, 48, 64, 96, 128} whose sup error over
2,000 points of the window is within the tolerance τ (Zipf τ = 0.05 in log₁₀ count; tide τ = 0.02 m); "> 128" if none.

## Predictions

- **Z1 (Zipf is ratio content).** In the window in ratios, K* at the seven centres c = 10^1.5, 10², …, 10^4.5 lies within
  a factor 2: largest over smallest ≤ 2.
- **Z2 (the amount does not enter).** With the corpus cut to its first quarter (every count about a quarter, the log
  shifted by about 0.6), K* at each centre from 10^1.5 to 10⁴ is the same or one step of the list away.
- **T1 (the tide has a size).** In the window in ratios, K* at centres c = 24, 96, 384, 1536, 6144 hours grows at least
  ×2.5 for each ×4 in c until it exceeds 128.
- **T2 (its units hold it).** In a window in records of half-width w = 48 hours, K* at the same five centres lies within a
  factor 2.

Each is killed by its own number. Z1 is the one that could go against the sorting: a measured list read as ratio content
whose needed K changes with the decade. Known beforehand: Zipf's law and reports of its two regimes (Ferrer i Cancho and
Solé 2001; Montemurro 2001), from memory and to be checked; the tide's harmonic constants (NOAA). Nothing of the data
was looked at in writing this.

## What would follow, if nothing is killed (a reading, to rule on)

On measured content the dial's sorting holds where the paper says it should: a list with no size of its own is held in
ratios at the same cost in every decade and is unmoved by the amount, and a list with a size is held at fixed cost only
in its own units. If Z1 is killed, the list is not ratio content across those decades, and the run says where its
needed K changes: a size hidden in a list believed to have none.

## Runs

### Run 1 (26 November 2026; `runs/msr/msr.py`, output `runs/msr/msr-run1.txt`)

Data, retrieved 26 November 2026, not committed: WikiText-103 raw train from
`huggingface.co/datasets/Salesforce/wikitext/resolve/main/wikitext-103-raw-v1/train-0000{0,1}-of-00002.parquet`
(sha256 74da360f23826045b3e6ac6375411fdb15f003030aa74f2596ed08b857cb9212 and
ba090ac30dbf5461e8dcbdd1a1b8e6f3cf9c2c756d64f0c1220450acd514f720): 1,801,350 rows, 101,425,671 tokens split on spaces,
623,941 distinct words, count at rank 10⁵ 17 (the first quarter: 25,276,063 tokens, 291,879 distinct, count 4 at rank
10⁵). NOAA hourly height, San Francisco 9414290, 2025, MLLW, metric, GMT (`product=hourly_height`; sha256
760f9480b3fbda312a48fb8346354aee4de68eea59a1b5c12176d4b74d68fa5d): 8,760 values, no gaps, −0.504 to 2.292 m. Read with
`python3 -I`. The plan's last tide centre, 6144 h, has a ratio window reaching 24,576 h, past the year's 8,760: my
set-up.

- **Z1 killed.** K* in the ratio window at c = 10^1.5, 10², 10^2.5, 10³, 10^3.5, 10⁴, 10^4.5: 32, 16, 6, 6, 6, 6, 6.
  Largest over smallest 5.33. From rank about 300 to 10^4.5 (three decades) the list is held at the same cost, 6
  leaves: ratio content. The head is not: the commonest thirty to a hundred words need 32 and 16.
- **Z2 not killed.** The first quarter: 24, 16, 6, 6, 6, 6 at the six centres to 10⁴, each the same or one step away
  (and 16 at 10^4.5, where its counts are about 4 and the Poisson scatter of counts that small enters).
- **T1 not killed, vacuously.** K* in the ratio window: more than 128 at every centre from 24 h on, the fifth centre
  outside the record. The clause "grows until it exceeds 128" is met at once, which tests nothing.
- **T2 killed, by my set-up.** In the records window of half-width 48 h, more than 128 at every centre too. The content
  was the hourly samples joined by straight lines, which kink every hour by about (1/8)·ω²·A·(1 h)² ≈ 0.03 m for the
  semidiurnal tide, more than my τ = 0.02 m: no smooth rebuild meets a kinked function to that tolerance.

### Run 2, predicted before it ran

The tide read as a smooth function of time: the hourly samples joined by a cubic spline (scipy `CubicSpline`, not-a-knot)
in place of straight lines; everything else as run 1.

- **T1′.** In the ratio window K* grows at least ×2.5 from c = 24 h to c = 96 h, and is more than 128 by c = 384 h.
- **T2′.** In the records window of half-width 48 h, K* at c = 24, 96, 384, 1536, 6144 h lies within a factor 2.

### Run 2 (26 November 2026; `runs/msr/msr2.py`, output `runs/msr/msr-run2.txt`)

- **T1′ killed.** K* in the ratio window is more than 128 at c = 24 h already (and at every centre after), so the first
  clause (a finite K* at 24 h, growing ×2.5 by 96 h) fails.
- **T2′ killed.** In the records window of half-width 48 h, K* is 128, more than 128, 128, 128, 96 at c = 24, 96, 384,
  1536, 6144 h.

Both by my tolerance. The measured tide is not smooth at the 2 cm level: the file's own sigma column (the scatter of the
six-minute readings within each hour) has a median of 0.049 m, and the spline passes through every hourly value, wiggles
included. τ = 0.02 m sat below the data's own scatter, so no window, in records or in ratios, holds it there with few
leaves. Not retuned after seeing these numbers; a third run would have to fix τ from the data's sigma before it ran.

### Standing after runs 1–2

Not killed: Z2. Killed: Z1 (the measured result), T2, T1′, T2′ (my tolerance against the tide's own scatter), T1 passed
only vacuously.

What the runs show (a reading, to rule on):
- **Zipf's tail is ratio content; its head is not.** From rank about 300 to rank 30,000 the word list is held in a
  window in ratios by 6 leaves at every centre, and cutting the corpus to a quarter (every count a quarter) changes nothing
  there: the amount does not enter. The commonest words are different: at ranks 30 and 100 the ratio window needs 32 and
  16. There each word is a particular word with its own count, and the list has structure the ratio window has to pay
  for. So the measured list believed to have no size is ratio content over three decades and not over its first two:
  the sorting found where the list is scale-free and where it is not, which the bend between head and tail reported for
  Zipf's law (to be checked) would predict.
- **The tide gave no verdict.** Its own scatter is above the tolerance I set, so neither window held it. The one thing
  the runs do show is the direction the plan expected: the records window came close (96–128 leaves at four of five
  centres) where the ratio window held it nowhere.
