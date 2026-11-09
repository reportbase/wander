"""HOL run 1, the data part (plans/hol-plan.md H5-H7). Numbers typed from the sources named; sha256s in the plan."""
from mpmath import mp, mpf, sqrt, sin, pi, radians
mp.dps = 30
# H5: Schumacher and Tarbet 2009 (arXiv:0902.1829), Pittsburgh, latitude 40 deg 26' 26"; a short pendulum driven so as to
# be free of ellipsoidal (Airy) precession. Their weighted mean -9.69 +- 0.09 deg/h, simple mean -9.85 +- 0.15 deg/h;
# their sidereal day 23.935 h.
lat = radians(40 + mpf(26)/60 + mpf(26)/3600); day = mpf('23.935')
for name, r, e in (('weighted mean', mpf('9.69'), mpf('0.09')), ('simple mean', mpf('9.85'), mpf('0.15'))):
    v = r * day / sin(lat); ev = e * day / sin(lat)
    print(f'H5 Pittsburgh ({name}): {mp.nstr(v, 5)} +- {mp.nstr(ev, 2)} deg per sidereal day over sin(lat); '
          f'{mp.nstr((v - 360)/ev, 3)} sigma from 360')
print('H5: one site qualifies; the plan asks for three -> untested')
# H7 (reported, not counted): hydrogen n = 2 fine structure, 2P3/2 - 2P1/2, the Dirac value (with Thomas's half)
alpha = 1/mpf('137.035999177'); cR = mpf('3289841960250.8')   # Rydberg frequency, kHz -> R_inf*c in kHz (CODATA 2018)
def dirac(n, j):  # E/(m c^2) - 1
    k = j + mpf(1)/2
    return 1/sqrt(1 + (alpha/(n - k + sqrt(k**2 - alpha**2)))**2) - 1
mc2_over_h = 2*cR/alpha**2                  # m c^2 / h in kHz, since R_inf c = alpha^2 m c^2/(2h)
d = (dirac(2, mpf(3)/2) - dirac(2, mpf(1)/2)) * mc2_over_h / 1000   # MHz
print(f'H7 Dirac 2P3/2 - 2P1/2 (infinite nuclear mass): {mp.nstr(d, 8)} MHz; without Thomas the interval doubles: '
      f'{mp.nstr(2*d, 8)} MHz')
meas = mpf('9911.200') + mpf('1057.845')  # 2S1/2-2P3/2 (Hagley and Pipkin 1994) + Lamb shift 2S1/2-2P1/2; from memory
print(f'H7 measured (from memory, to check): {mp.nstr(meas, 8)} MHz; measured / Dirac {mp.nstr(meas/d, 6)}; '
      f'measured / no-Thomas {mp.nstr(meas/(2*d), 6)}')
