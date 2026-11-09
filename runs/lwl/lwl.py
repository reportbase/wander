"""LWL run 1 (plans/lwl-plan.md): Γτ for each pair of a width read in frequency and a lifetime read in time.
Every number is typed from the source named beside it (sha256s in the plan). Run: python3 runs/lwl/lwl.py"""
import math
from scipy import stats
HBAR = 6.582119569e-16  # eV s (CODATA, exact by definition of h and e)


def ratio(a, ea, b, eb):
    r = a / b
    return r, r * math.hypot(ea / a, eb / b)


pairs = []
# 1. Na 3p 2P3/2 (D2). Width: Oates, Vogel, Hall 1996, quoted as tau 16.237(35) ns. Time: Volz et al. 1996, 16.254(22) ns.
pairs.append(('Na 3p 2P3/2', *ratio(16.254, 0.022, 16.237, 0.035)))
# 2. pi0. Width: Larin et al. 2020 (PrimEx-II), Gamma(gg) = 7.802 +- 0.052 +- 0.105 eV; B(gg) = 98.823 +- 0.034 %
#    (PDG 2024). Time: Atherton et al. 1985, tau = (8.97 +- 0.22 +- 0.17) e-17 s, direct.
Ggg, eGgg = 7.802, math.hypot(0.052, 0.105)
B, eB = 0.98823, 0.00034
G, eG = Ggg / B, (Ggg / B) * math.hypot(eGgg / Ggg, eB / B)
tau, etau = 8.97e-17, math.hypot(0.22, 0.17) * 1e-17
r = G * tau / HBAR
pairs.append(('pi0', r, r * math.hypot(eG / G, etau / tau)))
# 3. Cd 5s5p 1P1. Width: 2210.11425 (line shape), tau-equivalent 1.60(5) ns. Time: the most precise time-domain value in
#    its Table, beam-foil 1973, 1.90(15) ns.
pairs.append(('Cd 1P1', *ratio(1.90, 0.15, 1.60, 0.05)))
# 4. Kr 3d hole. Width: 88 +- 4 meV (quoted in publications.aob.rs/99, 47-50; its primary measurement not read here).
#    Time: Drescher et al. 2002, 7.9 (+1.0 / -0.9) fs; the mean of the two sides, 0.95 fs, taken as one error.
w, ew = 0.088, 0.004
t, et = 7.9e-15, 0.95e-15
r = w * t / HBAR
pairs.append(('Kr 3d', r, r * math.hypot(ew / w, et / t)))
# 5. Dy 421 nm level. Width: 1009.2962, line shape at zero intensity, 31.9(8) MHz. Time: the same paper's comparison,
#    33.1(17) MHz, from Curry, Den Hartog and Lawler 1997 (time-resolved laser-induced fluorescence; method from memory).
#    Gamma*tau = (Gamma/2pi)_width / (Gamma/2pi)_from-tau.
pairs.append(('Dy 421 nm', *ratio(31.9, 0.8, 33.1, 1.7)))

chi2 = 0.0
print(f"{'pair':14s} {'Gamma*tau':>10s} {'error':>8s} {'sigma from 1':>13s}  L1")
for name, r, e in pairs:
    z = (r - 1) / e
    chi2 += z * z
    print(f'{name:14s} {r:10.4f} {e:8.4f} {z:13.2f}  {"KILLED" if abs(z) > 3 else "not killed"}')
p = stats.chi2.sf(chi2, len(pairs))
print(f'L2: chi2 {chi2:.2f} on {len(pairs)}, p = {p:.3f} -> {"KILLED" if p < 0.001 else "not killed"}')
print('L3: the pion ->', 'KILLED' if abs((pairs[1][1] - 1) / pairs[1][2]) > 3 else 'not killed')
# The alternatives the rules' ties and choices leave, reported, not counted
print('\nReported, not counted:')
for name, a, ea, b, eb in (('Cd, width by Hanle 1964/1969 1.66(5) against beam-foil 1.90(15)', 1.90, 0.15, 1.66, 0.05),
                           ('Cd, width by line shape against time-resolved fluorescence 2004, 1.75(20)', 1.75, 0.20, 1.60, 0.05)):
    r, e = ratio(a, ea, b, eb)
    print(f'  {name}: {r:.4f} +- {e:.4f} ({(r - 1) / e:+.2f} sigma)')
r = Ggg * tau / HBAR
print(f'  pi0 with the gamma-gamma width alone (no branching ratio): {r:.4f}')
