# REA pocket note: the natural linewidth, who owns the Lorentzian

*18 October 2026, SPN R365. Kept in the pocket (R364): a reading, not run, and not for OFS. Tom: "Lets not worry about
phsyics in this paper. but add any useful comments from chatgpt to our pocket."*

## How it came up

1. **Claude's conclusion from the reframing** (`reframed.md`). The rule reframes every entry cleanly, but changes the
   predictions of almost none; the change is "in words, not numbers".
2. **Tom (11:16):** "so your saying that when a cauchy distribution is discovered when measuring a phsyical thing, and you
   attribute that cauchy result to the physical thing, not your measurement, no problem?"
3. **Claude's reply.** No: the attribution is the error, even where every number survives. The atom has
   z = ω₀ + iγ (amounts), and the Lorentzian is how a frequency sweep reads z. So REA's class R has two parts:
   - the numbers, which are kept;
   - the attribution, which is corrected.

## ChatGPT's comments (from Tom, 11:19), the useful points

- **Three things to keep apart:**
  - the payload, z = m + iγ;
  - the reading operation, a frequency sweep through the response;
  - the observed form, the Lorentzian, read here as the address law of the reader's turn.
- **The numbers can survive while the interpretation changes.** An exact Lorentzian fit does not by itself establish that
  the Lorentzian is an intrinsic distribution of the atom.
- **The challenge: does the sweep generate the Lorentzian, or reveal a response the atom's dynamics already implies?**
  Exponential decay gives a Lorentzian through Fourier analysis, which is not usually counted as an artefact of the
  measurement. The stronger claim has to show why the conventional derivation conflates the reader's address law with the
  payload's properties. Noting that the Lorentzian appears during measurement is not enough.
- **Re-evaluation must reconstruct the inference, not rename its terms.**
- **Two claims, not one.** "The atom has z" characterises the payload. "The Lorentzian is how a frequency sweep reads z"
  is the reader-geometry claim, and it needs a derivation connecting the sweep, its phase and the profile.
- **Either outcome is informative.** If the derivation fails, the linewidth marks a limit of the reinterpretation.
- **Verdict:** the right governing question, an excellent test case, the claim not yet established by the example.

## Claude's answer (a derivation, not run)

The excited atom's amplitude is a(t) = e^{(iω₀ − γ)t} for t ≥ 0. Its transform is A(ω) = 1/(γ + i(ω − ω₀)): one pole, at
z = ω₀ + iγ.

1. **The pole is the atom's.** The dynamics fixes z: a frequency and a decay rate.
2. **The Lorentzian is the pole read along a line.** It is |A(ω)|² on the real frequency axis, where a steady probe reads.
   With δ = arctan((ω − ω₀)/γ), γ·|A|² = dδ/dω exactly. So the profile is the rate at which the response's phase turns
   per unit of frequency swept: the turn's address law.
3. **The width is the pole's distance from the reader's line.**
   - A probe that itself decays at rate κ reads along a line off the real axis, and sees a Lorentzian of width γ + κ.
     Instrumental broadening adding Lorentzian widths is classical.
   - Read in time there is no Lorentzian at all, only e^{−γt}.
   - The pole is the same from every reader. TIM's real data has one instance: the lifetime read in time and the width
     read in frequency agree on z, Γ·τ = 1.0010 ± 0.0025.

So "reveals" fits the pole and "generates" fits the Lorentzian. The test of what is intrinsic is what stays the same across
readers.

**Conventional physics already takes this step for resonances.** The Particle Data Group separates the pole mass and width
from the Breit–Wigner parameters, which depend on the model. Gamow states define a resonance by its complex-energy pole.
What it does not do is make it a rule: that every Cauchy's shape is the reading's and its z the thing's.

**The quantum hard case.** A decaying state's |a(E)|² is the pole's trace on the real energy axis, read against the energy
basis; the complex energy E₀ − iΓ/2 is the intrinsic part. That fits the Gamow view, and is less radical than it first
sounded.

**What would establish it.** A run, offered and not taken (Tom: physics is not this paper's concern):
- the width read equals the pole's distance from the reader's line, at several κ;
- the pole is the same from a steady sweep, a decaying probe and the time domain;
- the shapes differ between those readers;
- real data: published instrumental broadening.

A width that failed to track the reader's line would be the limit ChatGPT named.
