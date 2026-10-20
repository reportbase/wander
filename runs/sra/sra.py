"""SRA run 1: special relativity's sky, addresses and payload (plans/sra-plan.md). 50 digits.
Run from the repository's root: python3 runs/sra/sra.py"""
import random
import mpmath as mp
mp.mp.dps = 50
random.seed(20261019)
TOL = mp.mpf('1e-45')

def k_of(b): return mp.sqrt((1 + b) / (1 - b))
def aberr_cos(th, b): return mp.acos((mp.cos(th) + b) / (1 + b * mp.cos(th)))
def aberr_tan(th, b): return 2 * mp.atan(mp.tan(th / 2) / k_of(b))
def D(thp, b): return mp.sqrt(1 - b * b) / (1 - b * mp.cos(thp))

betas = [mp.mpf('0.1'), mp.mpf('0.6'), mp.mpf('0.99')]
thetas = [mp.mpf(random.random()) * mp.pi for _ in range(1000)]

# A1
w = max(abs(aberr_cos(t, b) - aberr_tan(t, b)) for b in betas for t in thetas)
zs = []
for b in betas:
    for _ in range(200):
        t, ph = mp.mpf(random.random()) * mp.pi, mp.mpf(random.random()) * 2 * mp.pi
        z = mp.tan(t / 2) * mp.expj(ph)
        zp = mp.tan(aberr_tan(t, b) / 2) * mp.expj(ph)        # the boost keeps the azimuth
        zs.append(abs(zp - z / k_of(b)))
a1 = w < TOL and max(zs) < TOL
print(f"A1 cosine form against tan(theta'/2) = tan(theta/2)/k: worst {mp.nstr(w, 3)}; stereographic z -> z/k: worst "
      f"{mp.nstr(max(zs), 3)}  {'not killed' if a1 else 'KILLED'}")

# A2
a2 = True
for b in betas:
    k = k_of(b); rho = (k - 1) / (k + 1); eta = mp.atanh(b)
    grid = [mp.pi * j / 400 for j in range(1, 400)]
    # 3+1: push the uniform sphere forward through aberration: density in solid angle
    def push3(tp):
        c = mp.cos(tp); cs = (c - b) / (1 - b * c)               # the source's own cos theta
        return mp.diff(lambda x: (x - b) / (1 - b * x), c) / (4 * mp.pi)   # |d cos theta / d cos theta'| / 4 pi
    km2 = lambda tp: ((1 - rho**2) / (1 + rho**2 - 2 * rho * mp.cos(tp)))**2 / (4 * mp.pi)
    closed = lambda tp: (1 - b * b) / (4 * mp.pi * (1 - b * mp.cos(tp))**2)
    e3 = max(max(abs(push3(t) - closed(t)), abs(closed(t) - km2(t))) for t in grid)
    # 2+1: push the uniform circle forward: d theta / d theta'
    push2 = lambda tp: mp.diff(lambda x: 2 * mp.atan(k * mp.tan(x / 2)), tp) / (2 * mp.pi)
    wc = lambda tp: (1 - rho**2) / (2 * mp.pi * (1 + rho**2 - 2 * rho * mp.cos(tp)))
    e2 = max(abs(push2(t) - wc(t)) for t in grid)
    er = abs(rho - mp.tanh(eta / 2))
    ok = e3 < TOL and e2 < TOL and er < TOL
    a2 &= ok
    print(f"A2 beta {mp.nstr(b, 3)}: rho {mp.nstr(rho, 8)} = tanh(eta/2) to {mp.nstr(er, 2)}; 3+1 spherical Cauchy "
          f"{mp.nstr(e3, 3)}; 2+1 wrapped Cauchy {mp.nstr(e2, 3)}")
print("A2", "not killed" if a2 else "KILLED")

# A3
a3 = True
I0 = lambda nu: nu**3 / mp.expm1(nu)
tot0 = mp.quad(I0, [0, 1, 10, mp.inf])
for b in betas:
    for tp in (mp.mpf('0.3'), mp.mpf('1.2'), mp.mpf('2.8')):
        d = D(tp, b)
        e1 = abs((1 - b * b) / (1 - b * mp.cos(tp))**2 - d**2)
        tot = mp.quad(lambda nu: d**3 * I0(nu / d), [0, d, 10 * d, mp.inf])
        e4 = abs(tot / (d**4 * tot0) - 1)
        a3 &= e1 < TOL and e4 < mp.mpf('1e-40')
    print(f"A3 beta {mp.nstr(b, 3)}: address density = D^2 to {mp.nstr(e1, 2)}; intensity D^4 to {mp.nstr(e4, 2)} "
          f"(D at theta' = 2.8: {mp.nstr(d, 6)})")
print("A3", "not killed" if a3 else "KILLED")

# A4: the aberration has no nu (it is a function of theta and beta alone); a turn about the motion moves no D
a4w = mp.mpf(0)
for b in betas:
    for _ in range(300):
        t, ph, turn = [mp.mpf(random.random()) * s for s in (mp.pi, 2 * mp.pi, 2 * mp.pi)]
        n_src = mp.matrix([mp.sin(t) * mp.cos(ph), mp.sin(t) * mp.sin(ph), mp.cos(t)])
        n_rot = mp.matrix([mp.sin(t) * mp.cos(ph + turn), mp.sin(t) * mp.sin(ph + turn), mp.cos(t)])
        tp1 = aberr_tan(mp.acos(n_src[2]), b); tp2 = aberr_tan(mp.acos(n_rot[2]), b)
        a4w = max(a4w, abs(D(tp1, b) - D(tp2, b)))
a4 = a4w < TOL
print(f"A4 aberration has no frequency in it (by its form); a turn about the motion moves D by {mp.nstr(a4w, 3)}  "
      f"{'not killed' if a4 else 'KILLED'}")
print("A5", "not killed" if (a1 and a2 and a3) else "KILLED")
