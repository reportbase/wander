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
