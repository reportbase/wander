"""SRA run 2: A1' (plans/sra-plan.md): the boost as z -> z/k in the stereographic chart, relative error, with the observed
direction from the Lorentz transformation of the photon's momentum. 50 digits. Run from the repository's root."""
import random
import mpmath as mp
mp.mp.dps = 50
random.seed(20261019)
TOL = mp.mpf('1e-45')
worst_rel, worst_az = mp.mpf(0), mp.mpf(0)
for b in (mp.mpf('0.1'), mp.mpf('0.6'), mp.mpf('0.99')):
    g = 1 / mp.sqrt(1 - b * b); k = mp.sqrt((1 + b) / (1 - b))
    for _ in range(1000):
        t, ph = mp.mpf(random.random()) * mp.pi, mp.mpf(random.random()) * 2 * mp.pi
        n = [mp.sin(t) * mp.cos(ph), mp.sin(t) * mp.sin(ph), mp.cos(t)]       # toward the source, sources' frame
        E, p = 1, [-x for x in n]                                           # the photon travels from the source
        E2 = g * (E - b * p[2]); p2 = [p[0], p[1], g * (p[2] - b * E)]      # observer moving +z
        n2 = [-x / E2 for x in p2]
        z = (n[0] + 1j * n[1]) / (1 + n[2]); z2 = (n2[0] + 1j * n2[1]) / (1 + n2[2])
        worst_rel = max(worst_rel, abs(z2 - z / k) / abs(z / k))
        worst_az = max(worst_az, abs(mp.atan2(n2[1], n2[0]) - mp.atan2(n[1], n[0])))
ok = worst_rel < TOL and worst_az < TOL
print(f"A1' z' = z/k, relative: worst {mp.nstr(worst_rel, 3)}; azimuth moved: worst {mp.nstr(worst_az, 3)}  "
      f"{'not killed' if ok else 'KILLED'}")
print("A5'", "not killed" if ok else "KILLED", "(A2, A3 from run 1)")
