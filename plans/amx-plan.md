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
