# PHR: is a resonance's line the rate its phase turns?

25 Nov 2026. SPN R1207. Tom: "1 3", to Claude's option 1: test the reading the blind test's resonance cases rest on.

## Why

CMU (R1205) sorted 30 Cauchy cases blind; 15 were resonances, and they count as turns only by R362's reading:
a damped resonance is a phase turning at a steady rate, and its Lorentzian is that turn read per unit of
frequency. That reading can fail on measurements. This plan tests it where both the amplitude and the phase of
a response were measured across one resonance.

## The reading, stated before any data is looked for

For a response with one pole, χ(ω) = A/(ω₀ − ω − iΓ/2) (A complex, a constant phase allowed), the phase is
φ(ω) = arg A + arctan((Γ/2)/(ω₀ − ω)), and

  dφ/dω = (Γ/2)/((ω − ω₀)² + Γ²/4) = (Γ/2)·|χ(ω)|²/|A|².

So the power line |χ|² and the phase's rate of turn dφ/dω are one curve up to a constant. The reading says the
second is what the line is: a turn of the phase through a half turn (π), half of it within one half-width, its
middle the corner. The amplitude is the payload; nothing about the phase's rate needs it.

## Predictions (committed before any data set is chosen or opened)

- **Q1 (exact).** The identity above holds symbolically for one pole; for the driven oscillator
  χ = 1/(ω₀² − ω² − iγω) it holds only to first order in γ/ω₀, the ratio (dφ/dω)/|χ|² varying across ±γ by a
  relative amount of order γ/ω₀.
- **Q2 (data, one resonance).** After the preprocessing below, the measured dφ/dω and the measured |χ|², each
  scaled to its own peak, agree over ω₀ ± 2Γ with an rms difference under 5% of the peak.
  Killed if the difference exceeds 5% where |χ|² alone fits a Lorentzian with rms residual under 2% (that is,
  where the line looks Lorentzian but its phase does not turn as one).
- **Q3.** Γ read from the phase alone (2/peak of dφ/dω, or the frequency span over which φ turns from π/4 to 3π/4
  of its total) equals Γ read from the amplitude alone (the FWHM of |χ|²) within 5%.
- **Q4.** The phase turns by π across the line, within 10°, and by π/2 within ω₀ ± Γ/2, within 5°: half the turn
  inside one half-width either side of the corner.
- **Q5.** Where a data set holds two lines closer than 2Γ, or a line known not to be Lorentzian (inhomogeneous,
  Voigt), the ratio (dφ/dω)/|χ|² is not constant: it varies by more than 20% over ω₀ ± Γ. If no such data set is
  found, Q5 is untested.

Preprocessing, fixed now: a complex background linear in ω is fitted to the outer 20% of the sweep on each side
and subtracted before amplitude and phase are taken; dφ/dω is a centred difference of the unwrapped phase,
smoothed by a running mean over at most Γ/10; nothing else. Data sets: published or open sweeps with both
quadratures (or amplitude and phase) measured, of any kind (electrical, mechanical, optical, NMR, quartz). Each
data set's source, licence and sha256 recorded below before it is analysed.

What a pass shows, stated now: the identity is classical (the Kramers–Kronig pair of a single pole, Breit–Wigner's
phase shift); a pass shows the measured lines are single-pole responses, so that R362's reading is available for
them. It does not show the reading is the only one. A fail where the line looks Lorentzian takes those cases out
of CMU's 15.

## Runs

### Data set 1, recorded before analysis

Lopez et al., dataset of "Performance Study of the Vibrating Wire Technique to Determine Longitudinal Magnetic Field
Profile Using Scans to High Wire Harmonic", Zenodo 10.5281/zenodo.15485044, v2 (21 May 2025), CC BY 4.0.
`VWireStudyData.zip`, 1,755,802 bytes, md5 4e8abe8b2d4b02045dcf481e84bb55e1, sha256
e51699e065b4af05a32f41468b3ee95019d2b6cf7746cd9cf8acd813ce9ec947; not committed. A taut wire carrying an AC current in
a quadrupole's field, swept in frequency through one of its harmonics; two lock-ins read the wire's two transverse
motions as X and Y (columns MeanX1, MeanY1 and MeanX2, MeanY2). Seen before this record: the file list and the first
40 rows of one scan (jan16_fscan_n86.txt), which show a narrow line on a sizeable complex background with noisy
points near the peak.

How the predictions are judged on it, fixed now: every scan file under `RawScans/Wire/02_Precision` and
`03_FieldReconstr`, each channel separately, the complex response X + iY. A channel is analysed only if its
background-subtracted |χ|² peak stands at least 20 times the rms of |χ|² in the outer 20% (a line, not noise) and
the sweep covers ω₀ ± 2Γ. Γ for the window is the amplitude's FWHM. Q2: among analysed channels where a Lorentzian
fits |χ|² with rms residual under 2% of the peak, killed if more than 10% have the scaled curves differing by more
than 5% rms. Q3 and Q4 judged on the same channels, each killed if more than 10% miss. Q5 untested on this set
unless a channel shows two lines.

### Data set 2, recorded before analysis

Ungerer, Sarmah, Kononov, Ridderbos, Haller, Cheung and Schoenenberger, data of "Performance of high impedance
resonators in dirty dielectric environments", Zenodo 10.5281/zenodo.7602079 (v2, 3 Feb 2023), CC BY 4.0. `data.zip`,
55,091 bytes, md5 760099b1a6a4ce2b71ac6a63cc09211e, sha256 64a2230f393ec492becef482887b0ba07458965f3380845c6ea0e0541eee4244;
not committed. One curve, `Fig1c/resonance_curve.dat`: 150 points of complex S21 (real and imaginary) across a NbTiN
resonator near 4.731 GHz, read in transmission past it (a notch). The other files hold fitted numbers only. Seen before
this record: the headers and the first four rows. The resonant part of a notch is 1 − S21, a single pole in the ideal
model; a mismatch on the line turns that circle about the off-resonance point (an asymmetric line), which a background
linear in ω does not remove. That is a known way for Q2 to fail on this set; the preprocessing is not changed for it.
Judged as set 1, with one channel: each prediction killed if this channel misses.

### Run 1 (`runs/phr/phr.py`, output `phr-run1.txt`): Q1 and data set 1

**Q1 not killed.** For one pole, dφ/dω − (Γ/2)|χ|²/|A|² simplifies to 0. For the driven oscillator
χ = 1/(ω₀² − ω² − iγω), dφ/dω = γ(ω₀² + ω²)/|D|², so (dφ/dω)/|χ|² = γ(ω₀² + ω²). Over ω₀ ± γ that varies by 0.221,
0.0202 and 0.00200 at Q = 10, 100, 1000, against 2γ/ω₀ = 0.2, 0.02, 0.002: first order in γ/ω₀, as predicted. (The run's
first form evaluated the arctangent's derivative on a grid through ω₀, where it is 0/0, and printed nan; replaced by
the closed form, checked symbolically against the arctangent.)

**Data set 1: Q2–Q4 untested by their own condition.** Of 352 channels, 237 passed the line-and-coverage test (86 were
noise, 29 too narrow a sweep). None fitted a Lorentzian with rms residual under 2%: the quartiles were 6.9%, 8.9% and
11.3%. So by the judging fixed beforehand there was no channel to judge. The lines are about 1.5 Hz wide, sampled at
6 to 9 points across Γ, with noise near the peak several times larger than in the wings.

Not judged, recorded as measured over the 237: the scaled curves differed by 30% rms at the median; Γ from the phase's
peak rate was 44% under the amplitude's at the median; the turn within ±Γ/2 was 86° at the median (quartiles 78°,
95°). The total turn read 323° at the median, which is my set-up's fault (see run 2).

### Run 2 (`runs/phr/phr2.py`, output `phr-run2.txt`): data set 2

The notch's line stands 199 times its wings' noise, 6.4 points across Γ = 64.2 kHz, and the sweep covers ±2Γ.

**Q2–Q4 untested by their condition again.** The Lorentzian fitted |χ|² with an rms residual of 4.0%, over the 2%
the judging requires.

Not judged:
- Γ from the phase's peak rate was 3.7% under the amplitude's, inside Q3's 5%.
- The turn within ±Γ/2 was 82.6°, 7.4° short of 90°.
- The scaled curves differed by 20% rms (12% with a three-point smoothing, chosen after the run).
- The total turn read −794°.

**What the runs found about my design.** Two of the measures were impossible as I set them.

- *Q4's total turn and Q3's span method.* Subtracting the background fitted to the outer 20% leaves the response
  there at zero by construction, so its phase in the wings is the noise's. A total turn read from those wings means
  nothing. The phase has to be read about the circle's own centre, not about the subtracted background.
- *Q2's difference of a numerical derivative.* At six points across the line, a centred difference turns a few
  percent of noise into tens of percent.
- *The 2% condition.* It excluded every line in both sets, so the kill could not fire. It was meant to keep out
  lines that are not Lorentzian; at this sampling it also kept out every noisy Lorentzian.

So on these runs R362's reading is neither confirmed nor refuted. A run 3, with new predictions, would fit both
quadratures at once with one pole (a complex amplitude, f₀, Γ and a complex background), and then compare Γ fitted from
the amplitude alone with Γ fitted from the phase alone, taken about the fitted circle's centre. That needs no
derivative and no threshold on the fit.

### Run 3, predictions (25 Nov; Tom: "Merge, then run 3"), committed before the fit is written

The same two data sets and the same selection as runs 1–2 (set 1: every channel that passed run 1's line-and-coverage
test; set 2: its one curve). New method, fixed now:

1. **One-pole fit of both quadratures at once.** z(f) = A/(f₀ − f − iΓ/2) + B₀ + B₁(f − f̄), with A, B₀, B₁ complex,
   by least squares on real and imaginary parts together, started from run 1's estimates. The fit's background is
   subtracted: z_c = z − B₀ − B₁(f − f̄), whose ideal form passes through 0 off resonance.
2. **Γ from the amplitude alone:** a Lorentzian a/((f − f₀)² + Γ²/4) fitted to |z_c|², f₀ and Γ free.
3. **Γ from the phase alone:** φ(f) = φ₀ + atan2(Γ/2, f₀ − f) fitted to the unwrapped arg z_c, f₀, Γ, φ₀ free, each
   point weighted by |z_c| (the phase's noise goes as 1/|z_c|). This is the angle seen from the circle's off-resonance
   point, which is where the reading puts the turn: half a turn across the line, the corner (a quarter) at f₀.
4. **Errors** by a residual bootstrap of step 1 (200 resamples, seeded), steps 2–3 redone on each; σ the combined
   spread of Γ_phase − Γ_amp.

The amplitude and phase fits share step 1's background, so they are not independent measurements; what is tested is
whether the response's size and its angle each, read alone, give one width.

- **R1 (set 2).** Γ_phase/Γ_amp − 1 within 5%, and within 3σ.
- **R2 (set 1).** Among the analysed channels, at most 10% have |Γ_phase − Γ_amp| beyond 3σ + 2% of Γ_amp. Killed past 10%.
- **R3 (set 1, the fit's adequacy).** Set 1 records each point's standard deviations (stdX, stdY). The step-1 fit's χ²
  per degree of freedom, using them, is under 2 for the median channel. Killed if 2 or more. (Set 2 has no noise column;
  untested there.)
- **R4 (the turn).** Fitted from the phase alone, the turn across f₀ ± Γ/2 is 90° by construction of the model; what is
  tested is the data's: the unwrapped arg z_c at f₀ ± Γ_phase/2 differs by 90° ± 10° on set 2 and on the median set-1
  channel. Killed otherwise.

If R1 and R2 hold, the measured lines are single-pole responses whose width can be read from the phase alone, so R362's
reading (the line is the phase's turn read per unit of frequency) is available for these two kinds of resonance. If they
fail where R3 says the one-pole fit is adequate, the reading fails on data.

### Run 3, results (`runs/phr/phr3.py`, output `phr-run3.txt`)

- **R1 killed.** On set 2 Γ_amp 65.09 kHz and Γ_phase 69.85 kHz (the full fit's Γ 67.54 kHz): 7.3% apart, past the 5%
  bound, though only 1.23σ (σ of the difference 3.86 kHz by the bootstrap). The line is 6.8 points wide; the 5% clause
  was tighter than the data could test.
- **R4 not killed on set 2:** the data's own turn across f₀ ± Γ_phase/2 is 86.7°.
- **R3 killed.** Set 1's one-pole fit, χ²/dof with the recorded standard deviations, median 2.08 (quartiles 0.46,
  23.2). Half the channels fit within their noise, a quarter far outside it.
- **R2 and R4 on set 1 void, by my code.** Γ_phase/Γ_amp − 1 came out 0.0000 at the median and both quartiles. Checked
  on one channel afterwards (jan16 n86, channel 1): the amplitude-only fit returned the full fit's Γ to the last digit.
  With |z_c|² near 10⁻¹¹ the least-squares tolerances stop at the start, so on set 1 the two "separate" widths were the
  same number and R2's "0 of 219" tests nothing. Set 2's values are of order 1 and did move (65.09 against 67.54).
