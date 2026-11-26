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

