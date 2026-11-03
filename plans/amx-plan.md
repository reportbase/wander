# AMX: aimed terms mixed into even leaves, on real audio

*Plan written 3 November 2026, before any code for it was written or run. Tom: "tvf was slightly larger than industry
formats for vector graphics and audio. i'm wondering if this could make tvf competitive.", then "yes, do the audio test".
Nothing above the "Runs" line is edited after the first run.*

## The question

draw's `papers/tvf.md` §7 measured TVF on a real audio file: gzipped TVF tied FLAC at the transparent point and was
about twice FLAC at bit-exact. Its weak spot is audio with sharp transients, where it plateaus. EPI (`plans/epi-plan.md`)
and draw's `?lab=aim` (its `papers/labs.md` §58) found that terms aimed at standpoints near the detail (Takenaka–Malmquist,
Qian's greedy) beat even leaves where the detail is in a few places and fine accuracy is wanted, and lose elsewhere. An
attack in a recording is detail in one place in time; a decaying resonance is a pole, which an aimed term holds in one.
Does a mixed reader (even leaves for the broad form, aimed terms for what is left) make audio smaller than even leaves
alone, and how does it then stand against FLAC?

## Known beforehand

- draw `papers/tvf.md` §7: gzipped TVF ≈ FLAC at the transparent point (5 significant digits), ≈ 2× at bit-exact; the
  file and the cascade's settings for that measurement are not recorded. This test does not reproduce the cascade.
- EPI and draw §58: an aimed term costs twice a leaf (4 reals against 2 per complex degree of freedom); aimed terms win by
  about half on few sharp spots at fine accuracy, lose on smooth shapes and on detail everywhere, and lose almost always
  at coarse accuracy (1%).
- FLAC's linear prediction already models a signal as a few resonances (an all-pole filter) per block; its residual is
  Rice-coded. Aimed terms with poles are a related idea, applied per frame to the waveform rather than to the prediction.
- Takenaka–Malmquist approximation of signals and AFD for signal decomposition are in the literature (Qian and Wang
  2011 and after); this test claims nothing new about them, only measures them in TVF's setting.

## Data

From librosa's example data (`librosa.org/data/audio/`, hashes as in librosa's `registry.txt`; not committed):
- `snare-accelerate.ogg`, an accelerating snare drum, Brian McFee from sakebeats' CC0 sample, CC BY 4.0. 22,050 Hz,
  mono, 30 s. sha256 c4b237c784504cec7896e5c4b4e99e0774cf249129b627da94bbbea9e2c6605a. **The first 6 s are used**
  (chosen before looking at the waveform).
- `sorohanro_-_solo-trumpet-06.ogg`, a jazz trumpet loop, Mihai Sorohan, CC BY 3.0. 22,050 Hz, mono, 5.33 s.
  sha256 8374466fd3951d24509da6e799b132a0db0bdeda69d99c69d989a6888d3d727d. All of it.

Both are Vorbis files; the decoded 16-bit PCM (ffmpeg, `-ac 1 -ar 22050 -c:a pcm_s16le`) is the truth. The test is on
that waveform, not on the original recordings.

## Set-up

- Frames of M = 1024 samples (46 ms). In each frame the line through its first and last sample is taken off (2 numbers,
  charged to every reader alike) so the frame wraps without a jump.
- **Even leaves** (TVF's reader, simplified): the frame's band-limited projection with N leaves, the trigonometric
  polynomial of the lowest N/2 frequencies, stored as its N leaf values (N reals). N from 0 to M in steps of 8.
- **Aimed terms**: the frame's analytic part (frequencies ≥ 1) approximated by Qian's greedy (each standpoint a in the
  disc maximising (1 − |a|²)|g(a)|², a grid of 24 rings then Nelder–Mead, |a| ≤ 1 − 10⁻³), the sound 2·Re of it; each
  term 4 reals (a and its coefficient).
- **Mixed**: N even leaves, then aimed terms on what is left. For each frame the cheapest (N, n) meeting the target is
  kept, N over the grid, n up to 64. Pure leaves (n = 0) and pure aimed terms (N = 0) are two of its choices.
- **Target**: every frame's RMS error at most ε times the clip's RMS, so the clip's SNR is at least −20·log₁₀ ε. Three
  targets: 40 dB, 60 dB and **the 16-bit floor** (the error no larger than the PCM's own rounding noise, 2⁻¹⁵/√12 of full
  scale; the transparent point for a comparison with FLAC on the same PCM).
- **Bytes**: each reader's numbers written as TVF writes them, decimal text with d significant digits, a frame a line,
  the whole file gzipped (level 9). d is the smallest, from 2 to 9, at which every frame still meets the target after
  rounding (the encoder aims at 0.9 ε, leaving the rest to rounding); for the aimed terms the rounded a and coefficients
  are put back through the synthesis.
- **FLAC**: `ffmpeg -c:a flac -compression_level 12` on the same 16-bit PCM, and the raw PCM gzipped, for reference.

## Predictions

- **A1 (the snare, mixed against leaves).** At the 16-bit floor, the mixed reader's gzipped bytes are at most 0.8 of
  the even leaves' alone. At 40 dB at least 0.95 (no real gain at coarse accuracy).
- **A2 (the trumpet).** The mixed reader's bytes are at least 0.95 of the leaves' alone at every target (a tonal sound
  is detail everywhere in frequency, the leaves' case).
- **A3 (against FLAC).** At the 16-bit floor the even leaves alone are within 0.7 to 1.5 times FLAC on both clips
  (reproducing §7's tie roughly, by a simpler encoder), and on the snare the mixed reader is under FLAC (below 1.0×).
- **A4 (where the standpoints go).** In snare frames where the mixed reader uses a term with |a| > 0.9 at the 60 dB
  target, its place arg(a)·M/2π lies within 32 samples of the frame's largest |residual after the leaves| in at least 60%
  of those frames.

Kill: any number on the wrong side of its bound. A killed prediction stays killed; a fix is a new run with new
predictions.

## Runs

### Set-up amended before any result was seen (3 Nov)

Run 1 as planned was stopped unfinished (Tom: "that is to long. normally we get results right away."); it printed
nothing. The search is cut to run in minutes. The predictions are unchanged:
- **Shorter clips.** The snare's first 2 s and the trumpet's first 2 s (43 frames each).
- **A coarser grid for mixing.** In the mixed reader, N in steps of 64 (the leaves alone keep steps of 8).
- **A cheaper search per term.** The Nelder–Mead refinement is capped at 60 iterations.

All three changes can only make the mixed reader look worse, never better.

### Run 1 (3 Nov, as amended; `runs/amx/amx-run1.txt`, 5 min on 4 cores)

All three of A1–A3 were killed. At the 16-bit floor no digit count from 2 to 9 met the target on either clip, nor at
60 dB on the snare. A1, A3 and A2's floor clause were killed by my set-up, which was a bug: the even leaves keep
frequencies |k| < N/2, so even at N = M they leave out the top frequency (k = M/2). Wherever a frame carries more there
than the allowance, no rounding can meet the target. A4 was not killed, but on 1 frame of 1.
- **Snare.** At 40 dB the mixed reader chose no aimed term at all, so it equals the leaves alone (18,924 bytes,
  0.972× FLAC). At 60 dB it used 39 aimed terms against 8,856 leaves (0.6% fewer numbers); at the floor 11 against
  10,704.
- **Trumpet.** At 40 dB mixed/leaves was 0.994 (45,521 against 45,794 bytes, 0.83× FLAC). At 60 dB it was 0.959
  (98,410 against 102,656, 1.79× FLAC; 167 terms against 33,160 leaves).
- **References.** FLAC 19,464 bytes (snare) and 54,882 (trumpet). The raw PCM gzipped was 15,187 for the snare, below
  FLAC on so short a clip.

Read after the run: the greedy, given the choice, takes almost no aimed terms on these real frames. Where it takes any
it saves under 5% of the numbers, on the tonal clip more than on the drum.

### Run 2: the top frequency included (predictions written before it ran)

The only change: at N = M the leaves keep every frequency (the frame exactly, with M numbers). A1–A4 are restated
unchanged as B1–B4 for this run, with the same bounds.

### Run 2 (3 Nov; `runs/amx/amx-run2.txt`)

The output was the same as run 1's, number for number. B1–B3 were killed, and the cause was my diagnosis, which was
wrong. Only one frame failed: snare frame 17, which needs every leaf (N = M). There the leaves sit half-way between
samples, at (k + ½)·M/N, and the top frequency cos(πj) is exactly zero at those points. That is TVF's invisible mode,
the first of draw's decoder test vectors. So no leaf value carries it, and the stored numbers could not write the frame
however many digits they had. Run 2 kept it in the projection but not in the numbers written.

### Run 3: the invisible mode stored (predictions written before it ran)

The only change: a frame that takes all M leaves also stores its top-frequency coefficient as one more number
(M + 1 numbers). A1–A4 are restated unchanged as C1–C4, with the same bounds.

### Run 3 (3 Nov; `runs/amx/amx-run3.txt`, 5 min on 4 cores)

Every target met. C1 killed, C2 not killed, C3 killed, C4 not killed, on 1 frame of 1 (too few to mean anything).

| clip, target | leaves alone (bytes, × FLAC) | mixed (bytes, × FLAC) | aimed terms used |
|---|---|---|---|
| snare, 40 dB | 18,924, 0.97 | 18,924, 0.97 | 0 |
| snare, 60 dB | 26,897, 1.38 | 26,787, 1.38 | 39 (against 8,856 leaves) |
| snare, 16-bit floor | 38,925, 2.00 | 38,492, 1.98 | 11 (against 10,704 leaves) |
| trumpet, 40 dB | 45,794, 0.83 | 45,521, 0.83 | 37 |
| trumpet, 60 dB | 102,660, 1.87 | 98,412, 1.79 | 167 |
| trumpet, 16-bit floor | 152,281, 2.78 | 152,281, 2.78 | 0 |

FLAC: 19,464 bytes (snare), 54,882 (trumpet).

- **C1 killed.** On the snare at the floor, mixed/leaves was 0.989, not ≤ 0.8.
- **C3 killed.** At the floor the leaves alone were 2.0× FLAC (snare) and 2.8× FLAC (trumpet), not within 0.7–1.5; and
  the mixed reader did not get under FLAC. This encoder matches §7's "about twice FLAC at bit-exact", not its tie at the
  transparent point. It is not the cascade (§7's file and settings are not recorded), so this does not test §7's tie.

Read after the run:
- **The greedy takes almost no aimed terms.** Even on the drum, an attack in a real 46 ms frame is not one sharp place
  in an otherwise smooth frame. The frame is full of broadband detail (the snare's rattle, the reverb, the codec's noise
  floor), which is the leaves' case. The gain is under 5% wherever there is one, and most on the tonal clip at 60 dB,
  the opposite of the prediction.
- **FLAC wins at fine accuracy for another reason.** Its linear prediction carries each frame's resonances in about 12
  coefficients, and its residual is coded in whole bits. Leaves written as decimal text at 5 digits cost more per
  number; at the floor the numbers alone (10,955 for the snare) are fewer than the 88,064 raw bytes, but each is about
  3.5 bytes once gzipped.
- **At 40 dB TVF-style leaves are under FLAC** (0.97×, 0.83×). That is no win: FLAC is lossless, and any lossy codec is
  smaller at 40 dB.

So aimed terms do not make TVF competitive on audio. What separates it from FLAC at fine accuracy is the cost of each
number (decimal text against prediction and entropy coding), not how the waveform is approximated.

### Run 4: the same leaves, packed as binary (predictions written before it ran)

Tom (3 Nov): "text only can be an option, not a requirement." The leaves alone, the same N per frame as run 3's leaves
at each target, are written as FLAC writes samples. Each number is rounded to a uniform step q, the largest power of two
that still meets every frame's target. Each frame's sequence (its line's two ends, then its leaves, then the top
frequency where N = M) is predicted by the best fixed polynomial predictor of order 0–3, as FLAC's fixed predictors do.
The residuals are Rice coded with the best parameter per frame. A frame's header is 7 bits for N/8, 2 for the order and
5 for the parameter. No aimed terms, no text, no gzip.

- **D1.** At the 16-bit floor, binary leaves are under 1.0× FLAC on the snare and under 1.3× on the trumpet. The leaves
  are fewer than the samples (10,955 of 44,032 numbers, and 43,669) and as predictable.
- **D2.** At every target binary is at most half the bytes of run 3's gzipped text on both clips.

### Run 4 (3 Nov; `runs/amx/amx_bin.py`, `runs/amx/amx-run4.txt`, 19 s)

D1 and D2 not killed.

| clip, target | binary leaves (bytes, × FLAC) | run 3's text (× FLAC) |
|---|---|---|
| snare, 40 dB | 6,450, 0.33 | 0.97 |
| snare, 60 dB | 9,701, 0.50 | 1.38 |
| snare, 16-bit floor | 14,129, 0.73 | 2.00 |
| trumpet, 40 dB | 20,060, 0.37 | 0.83 |
| trumpet, 60 dB | 45,444, 0.83 | 1.87 |
| trumpet, 16-bit floor | 66,947, 1.22 | 2.78 |

Binary is 0.34–0.44 of the gzipped text throughout.

Read after the run, with caveats:
- **The floor is not lossless.** At the 16-bit floor the error equals the PCM's own rounding noise, so the decoded
  sound carries that noise twice over (about 3 dB more). FLAC gives back the PCM bit for bit. The comparison is
  "about as good as the 16-bit file" against "exactly the 16-bit file".
- **The sources were Vorbis.** Both were decoded from Vorbis, which takes off the highest frequencies; the leaves
  exploit that (the snare needs 10,955 numbers for 44,032 samples) and FLAC cannot. On a recording never through a lossy
  codec, the leaves would need more.
- **The bit counts are estimates.** They are the bits of the residuals and the frame headers, with no container; FLAC's
  size includes its headers (under 1% here).
- **Two clips of 2 s each.**

Within those limits, the price of a number is the whole gap: TVF's leaves, packed as FLAC packs samples, come in under
FLAC on the snare and 1.2× on the trumpet at the floor, against 2.0× and 2.8× as text.

### Run 5: a lossless source, bit-exact and against Opus (predictions written before it ran)

Tom (3 Nov): "proceed", on testing a lossless source against FLAC at bit-exact and against a lossy codec.

**Data.** Jan Morgenstern's score for *Sintel* (Blender Foundation), CC BY 3.0, as lossless FLAC from Xiph
(`media.xiph.org/sintel/Jan_Morgenstern-Sintel-FLAC.zip`, 60,258,620 bytes, sha256
f04fd0d69e349901fe087614644d1e759f653c8ddf68d3a2dba9e501bca50ecc; not committed). 16-bit, 44.1 kHz, stereo, mixed to
mono by ffmpeg (`-ac 1`); the mono 16-bit PCM is the truth. Never through a lossy codec.

**Clips, by a rule fixed before any coding.** Each clip is 2 s, in frames of 1024. For every 2 s window starting on a
multiple of 0.5 s, the attack is the largest ratio of one frame's RMS to the frame before it (frames under 10⁻³ of full
scale left out).
- *Percussive*: the window of largest attack in `1-Snow_Fight.flac`.
- *Tonal*: the window of smallest attack in `7-I_Move_On-Sintels_Song.flac`, among windows whose RMS is at least 0.02.

**Coders.**
- Binary leaves as in run 4.
- **Lossless TVF**: the leaves at a target, then the integer remainder (PCM minus the rounded rebuild) coded by the same
  fixed predictor and Rice code. The best of the 40 dB, 60 dB and 16-bit-floor targets is kept, and no leaves (the
  remainder alone) is a fourth choice.
- FLAC level 12.
- Opus (libopus) at 64, 128 and 256 kb/s, decoded and aligned by cross-correlation, its SNR measured. SNR is not what
  Opus aims at: it is a perceptual codec.

**Predictions.**
- **E1.** At the 16-bit floor, binary leaves are at least 1.0× FLAC on both clips. Run 4's win came from Vorbis's
  missing top band.
- **E2.** Lossless TVF is between 1.0× and 1.3× FLAC on both clips.
- **E3.** At 60 dB, binary leaves are under 1.0× FLAC on both clips.
- **E4.** Opus at 128 kb/s gives an SNR under 30 dB on both clips.

### Run 5 (3 Nov; `runs/amx/amx-run5.txt`, 43 s), and a correction to runs 1–4

The windows came out as Snow Fight from 0.0 s (attack 10.0, RMS 0.102) and Sintel's Song from 98.0 s (attack 1.17, RMS
0.074). As printed: E1, E3 and E4 not killed, E2 killed. On the percussive clip, lossless TVF came out at 0.915×
FLAC, and so did the bare PCM by my fixed predictor and Rice code (0.917×).

That second number gave it away. **Every FLAC size in runs 1–5 included ffmpeg's metadata**: STREAMINFO, a
VORBIS_COMMENT and 8,192 bytes of PADDING, about 8.3 KB a file whatever the audio. My coders' counts carry no
container. On 2 s clips that is a large error, all of it in TVF's favour. Run 5 is killed by my set-up. The FLAC sizes
are now its audio frames alone (`flac_audio_bytes`).

**Runs 3–4 corrected** (post hoc, no new run; the predictions stay judged as printed). FLAC's audio bytes are 11,176
(snare) and 46,594 (trumpet), not 19,464 and 54,882.

| target | binary leaves, snare | binary leaves, trumpet | text, snare | text, trumpet |
|---|---|---|---|---|
| 40 dB | 0.58× | 0.43× | 1.69× | 0.98× |
| 60 dB | 0.87× | 0.98× | 2.41× | 2.20× |
| 16-bit floor | **1.26×** | **1.44×** | 3.48× | 3.27× |

So binary leaves at the floor were not under FLAC even on the Vorbis-sourced snare.

### Run 6: run 5 against FLAC's audio bytes (predictions written before it ran)

The only change: FLAC's audio bytes alone. E1–E4 are restated unchanged as F1–F4.

### Run 6 (3 Nov; `runs/amx/amx-run6.txt`, 43 s)

F1, F2 and F4 not killed; F3 killed (the script prints them under run 5's letters E1–E4).

| | percussive (Snow Fight) | tonal (Sintel's Song) |
|---|---|---|
| FLAC, audio bytes | 41,625 | 87,115 |
| binary leaves, 40 dB | 2,742 (0.07×) | 34,282 (0.39×) |
| binary leaves, 60 dB | 11,439 (0.27×) | 89,012 (1.02×, F3 killed) |
| binary leaves, 16-bit floor | 81,804 (1.97×) | 120,122 (1.38×) |
| lossless TVF, best | 45,676 (1.10×, leaves at 40 dB + remainder) | 96,826 (1.11×, no leaves) |
| PCM alone, fixed predictor + Rice | 45,759 (1.10×) | 96,826 (1.11×) |
| Opus 64 / 128 / 256 kb/s, SNR | 27.4 / 29.7 / 29.9 dB | 24.1 / 29.2 / 34.5 dB |
| Opus 64 / 128 / 256 kb/s, size | 0.31 / 0.73 / 1.46× | 0.23 / 0.41 / 0.77× |

Read after the run:
- **Lossless: the leaves add nothing.** The best lossless TVF is the bare PCM by a fixed predictor (or within 0.2% of
  it on the percussive clip). Its 10% over FLAC is FLAC's adaptive linear prediction against fixed polynomials, not
  anything about leaves.
- **Near-transparent: worse than lossless.** On a source never through a lossy codec, binary leaves at the 16-bit floor
  are 1.4–2.0× FLAC. They are larger than the lossless file, so there is no point being "about as good" when being
  exact is cheaper.
- **Lossy, by SNR: leaves far ahead of Opus.** At 40 dB the leaves are 2.7 KB and 34 KB, where Opus at 128 kb/s is
  30 KB and 36 KB at 29–30 dB. But SNR is the leaves' own measure and not Opus's: Opus spends its bits on what the ear
  hears, and no listening test or perceptual measure was run. This says nothing about which sounds better at a size.
- **The percussive window starts the track** (0.0 s). Most of its frames are quiet or low in frequency, which is why
  40 dB costs so little there.

So, with packed binary on a clean source, TVF's leaves are about 1.1× FLAC lossless (the predictor's gap, closable
with FLAC's own adaptive prediction) and no use at near-transparent quality. As a lossy waveform coder they are small
by SNR, but whether they compete with Opus needs a perceptual measure.

### Run 7: a perceptual comparison with Opus (predictions written before it ran)

Tom (3 Nov): "do the perecptual comparison". Run 6's lossy result was by SNR, the leaves' own measure. This run asks
which sounds closer to the original at the same size.

**Measures.** Both compare the coded clip with the original at 48 kHz (everything resampled by ffmpeg) and report a mean
opinion score (MOS, 1–5).
- **Zimtohrli**, the primary measure. Google's psychoacoustic distance (Apache 2.0), from PyPI `zimtohrli` 0.2.1.post1,
  wheel sha256 be6fbb52bc5967970a0dd5159b32812c9dbf7e8d6c9ef85b1b05afc0cf1db05b. Its own mapping `mos_from_zimtohrli` turns the distance into a MOS.
- **ViSQOL**, audio mode, as a check. `visqol-python` 3.8.0, an unofficial pure-Python port of Google's ViSQOL with its
  bundled model; not the reference C++ build.

No listening test with people.

**Clips.** Run 6's two windows: Snow Fight from 0.0 s, Sintel's Song from 98.0 s.

**Coders.**
- **TVF leaves** packed as binary, as in runs 4–6, at targets of 20, 25, 30, 35, 40, 50 and 60 dB SNR, each giving a
  size and a reconstruction.
- **Opus** (libopus) at 24, 32, 48, 64, 96, 128 and 192 kb/s, its size the sum of its packets (no Ogg pages or headers;
  the TVF counts carry no container either), decoded and aligned by cross-correlation.

The two curves (size against MOS) are compared at equal size, by interpolation in log size, at the sizes where both
have points.

**Predictions.**
- **G1.** By Zimtohrli, at every common size, Opus scores higher than the leaves on both clips.
- **G2.** To match Opus's Zimtohrli MOS at 128 kb/s, the leaves need at least 2× Opus's bytes on the tonal clip, or
  never reach it within 60 dB.
- **G3.** By SNR at equal size, the leaves beat Opus on both clips (run 6 again).
- **G4.** ViSQOL agrees with Zimtohrli on which coder wins in at least 75% of the matched-size comparisons.

### Run 7 (3 Nov; `runs/amx/amx_percept.py`, `runs/amx/amx-run7.txt`, 84 s)

G1 killed; G2, G3, G4 not killed. The two clips split.

**Tonal (Sintel's Song): Opus far ahead by ear.** At equal size Opus scores 4.69–5.00 by Zimtohrli where the leaves score
1.89–4.64; by ViSQOL 4.22–4.64 against 1.52–3.90. The leaves reach Opus's 128 kb/s score (4.992, 35,184 bytes) only at
60 dB, 2.53× the bytes (G2 not killed), while beating Opus by SNR at every size (G3).

**Percussive (Snow Fight's opening): the leaves ahead from 5.4 to 11.4 KB.**

| size | leaves (Zimtohrli / ViSQOL) | Opus (Zimtohrli / ViSQOL) |
|---|---|---|
| 5,425 bytes (Opus at 24 kb/s) | 4.45 / 4.34 | 3.73 / 4.44 |
| 7,878 bytes | 4.67 / 4.50 | 4.27 / 4.41 |
| 11,439 bytes (Opus near 64 kb/s) | 4.88 / 4.66 | 4.83 / 4.64 |

That kills G1. ViSQOL agreed on the winner in 16 of 18 comparisons (G4); it disagreed only at the two smallest sizes on the
percussive clip.

Read after the run:
- **Not monotone at low targets.** On the percussive clip the leaves' scores dip from 25 to 35 dB (2.90, 2.82, 2.70)
  before climbing; the rounding's noise and the band edge sit where the ear is sensitive. Not looked into.
- **The percussive window is the track's opening**, low in frequency where the frames are loud. That suits a reader that
  keeps the low leaves and drops the rest, and does not suit a perceptual codec at its lowest rates (24–48 kb/s, where
  Opus spends bits on bandwidth replication and its SNR falls to 15–19 dB). One window, picked by attack, is not a
  percussive repertoire.
- **The common sizes are narrow.** Opus was not run below 24 kb/s, nor the leaves above 60 dB.
- **Caveats on the measures.** Zimtohrli's MOS is its own mapping; the ViSQOL is an unofficial pure-Python port; no
  person listened.

So: on a tonal passage a perceptual codec is far ahead at every size; on a low, loud percussive opening the leaves were
ahead by both measures from 5 to 11 KB. Whether that holds over more percussive material is the next question, and an
ear's.
