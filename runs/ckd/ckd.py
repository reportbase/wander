"""CKD: the corner's kinds, for COR and BAL. Predictions in plans/ckd-plan.md, written before this script.

Run from the repository's root: python3 runs/ckd/ckd.py
Exact: sympy for identities, mpmath at 50 digits for integrals and roots.
"""
import sympy as sp
import mpmath as mp

mp.mp.dps = 50
s = sp.symbols('s', positive=True)
GRID = [mp.mpf(50) ** (mp.mpf(i - 20) / 20) for i in range(41)]  # 41 values of s in [1/50, 50], log-even
verdict = {}


def say(*a):
    print(*a)


def kind_tests(f, name, grid=GRID):
    """Test the kinds on a grid; f takes an mpf and returns an mpf."""
    tol = mp.mpf('1e-40')
    even = all(abs(f(x) - f(1 / x)) < tol for x in grid)
    comp = len({mp.nstr(f(x) + f(1 / x), 30) for x in grid}) == 1
    sign = all((f(x) == 0 and f(1 / x) == 0) or f(x) * f(1 / x) < 0 for x in grid if abs(x - 1) > tol)
    fold = all(abs(f(x) - f(2 - x)) < tol for x in [mp.mpf(i) / 40 for i in range(1, 80)])
    return dict(even=even, complement=comp, sign_flip=sign, fold=fold)


# ── P1. BAL: the share in BAL's lay (azimuth and elevation each even on [-π/2, π/2]) of the cap of half-angle α ──
say('P1  BAL')


def bal_share(alpha):
    alpha = mp.mpf(alpha)
    if alpha >= mp.pi / 2:
        return mp.mpf(1)
    ca = mp.cos(alpha)
    g = lambda ph: 2 * mp.acos(min(mp.mpf(1), ca / mp.cos(ph)))
    return mp.quad(g, [-alpha, 0, alpha]) / mp.pi ** 2


corner = mp.pi / 4
sh45 = bal_share(corner)
sh90 = bal_share(mp.pi / 2)
s_small = mp.mpf('1e-10')
far = bal_share(mp.asin(s_small)) / s_small ** 2
mid_alpha = mp.findroot(lambda a: bal_share(a) - mp.mpf(1) / 2, (mp.mpf('0.9'), mp.mpf('1.5')), solver='anderson')
mid_s = mp.sin(mid_alpha)
say('   s = a/d ranges [0, 1]; contact is α = 90°, the end of the limb\'s sweep (no s > 1 seen from outside)')
say('   the limb\'s corner: tan α = 1, s =', mp.nstr(mp.sin(corner), 20), '(1/√2)')
say('   share at α = 45°:', mp.nstr(sh45, 20))
say('   share at α = 90°:', mp.nstr(sh90, 20))
say('   share/s² at s = 1e-10 against 1/π:', mp.nstr(far, 25), mp.nstr(1 / mp.pi, 25), ' diff', mp.nstr(abs(far - 1 / mp.pi), 3))
say('   the middle (share ½): α =', mp.nstr(mid_alpha * 180 / mp.pi, 15), '°, s =', mp.nstr(mid_s, 15), ', d/a =', mp.nstr(1 / mid_s, 15))
say('   check against BAL\'s own count (n = 1200) at s = 0.7:', mp.nstr(bal_share(mp.asin(mp.mpf('0.7'))), 10))
p1 = sh45 < mp.mpf(1) / 2 and sh90 == 1 and abs(far - 1 / mp.pi) < mp.mpf('1e-20') and mid_s > mp.sin(corner)
verdict['P1'] = p1
say('   P1', 'not killed' if p1 else 'KILLED')

# ── P2. Two loops ──
say('P2  two loops: f = min(s, 1/s)')
f2 = lambda x: min(x, 1 / x)
k2 = kind_tests(f2, 'loops')
h = mp.mpf('1e-30')
sl_lo = (f2(1 + 0 * h) - f2(1 - h)) / h
sl_hi = (f2(1 + h) - f2(mp.mpf(1))) / h
lsl_lo = (f2(mp.mpf(1)) - f2(mp.e ** -h)) / h   # slope in ln s
lsl_hi = (f2(mp.e ** h) - f2(mp.mpf(1))) / h
say('  ', k2, ' slopes in s', mp.nstr(sl_lo, 10), mp.nstr(sl_hi, 10), ' in ln s', mp.nstr(lsl_lo, 10), mp.nstr(lsl_hi, 10))
p2 = k2['even'] and abs(sl_lo - 1) < 1e-20 and abs(sl_hi + 1) < 1e-20 and abs(lsl_lo - 1) < 1e-20 and abs(lsl_hi + 1) < 1e-20
verdict['P2'] = p2
say('   P2', 'not killed' if p2 else 'KILLED')

# ── P3. Escape: COR's shares, and the energy ∝ s − 1 ──
say('P3  escape')
f3 = lambda x: 1 - x if x <= 1 else 1 - 1 / x
k3 = kind_tests(f3, 'escape shares')
E = lambda x: x - 1
signs = all(E(x) * E(1 / x) < 0 for x in GRID if abs(x - 1) > 1e-40)
odd_value = all(abs(E(x) + E(1 / x)) < 1e-40 for x in GRID)
say('   shares', k3, '; energy sign flips', signs, ', odd in value', odd_value)
x_ = sp.symbols('x', positive=True)
say('   symbolic: (1/s − 1) + (s − 1)/s =', sp.simplify((1 / x_ - 1) + (x_ - 1) / x_))
p3 = k3['even'] and signs and not odd_value
verdict['P3'] = p3
say('   P3', 'not killed' if p3 else 'KILLED')

# ── P4. Sampling's fold ──
say('P4  sampling')


def f4(x):
    m = mp.fmod(x, 2)
    return min(m, 2 - m)


k4 = kind_tests(f4, 'sampling')
say('  ', k4, ' f(½) =', f4(mp.mpf('0.5')), ' f(2) =', f4(mp.mpf(2)))
p4 = (not k4['even']) and (not k4['complement']) and k4['fold']
verdict['P4'] = p4
say('   P4', 'not killed' if p4 else 'KILLED')

# ── P5. Parallax giving out: the far edge where γ = ε against the pair's corner d = B/2 ──
say('P5  parallax')
B = mp.mpf(2)  # half-baseline 1


def give_out(eps):
    # on the bisector the parallax angle is γ = 2·atan((B/2)/d); it gives out where γ = ε
    return (B / 2) / mp.tan(eps / 2)


ok = True
for e in ['1e-2', '1e-3', '1e-4']:
    e = mp.mpf(e)
    r = give_out(e / 2) / give_out(e)
    say('   ε', mp.nstr(e, 3), ' give-out d', mp.nstr(give_out(e), 12), ' ratio when ε halves', mp.nstr(r, 15))
    ok = ok and abs(r - 2) < mp.mpf('1e-6')
sep = mp.log(give_out(mp.mpf('1e-3')) / (B / 2), 2)
pxc = mp.acosh(1 / mp.mpf('1e-3')) / mp.log(2)
say('   levels from the corner (d = B/2) to the give-out at ε = 1e-3:', mp.nstr(sep, 10), '; PXC acosh(1/ε)/ln 2:', mp.nstr(pxc, 10))
p5 = ok and abs(sep - mp.mpf('10.966')) < mp.mpf('1e-3')
verdict['P5'] = p5
say('   P5', 'not killed' if p5 else 'KILLED')

# ── P6. The disc ──
say('P6  the disc')
f6 = lambda x: 1 / (1 + x ** 2)
k6 = kind_tests(f6, 'disc')
foot = max(abs(f6(x) - mp.sin(mp.atan(1 / x)) ** 2) for x in GRID)
d6 = sp.diff(1 / (1 + s ** 2), s).subs(s, 1)
say('  ', k6, ' f(1) =', f6(mp.mpf(1)), " f'(1) =", d6, ' max |f − sin²(rim)|', mp.nstr(foot, 3))
say('   symbolic: f(s) + f(1/s) =', sp.simplify(1 / (1 + s ** 2) + 1 / (1 + 1 / s ** 2)))
p6 = k6['complement'] and foot < mp.mpf('1e-40') and d6 == sp.Rational(-1, 2)
verdict['P6'] = p6
say('   P6', 'not killed' if p6 else 'KILLED')

# ── P7. The filling sky ──
say('P7  the filling sky')
f7 = lambda x: 1 - mp.e ** (-x)
k7 = kind_tests(f7, 'sky')
say('  ', k7, ' f(1) =', mp.nstr(f7(mp.mpf(1)), 12), ' f(2) + f(½) =', mp.nstr(f7(mp.mpf(2)) + f7(mp.mpf('0.5')), 6))
p7 = not any(k7.values())
verdict['P7'] = p7
say('   P7', 'not killed' if p7 else 'KILLED')

# ── P8. The sort ──
sort = {
    'BAL contact': 'E' if verdict['P1'] else '?',
    'two loops': 'C-even kinked' if verdict['P2'] else '?',
    'escape': 'C (shares even kinked; energy regime)' if verdict['P3'] else '?',
    'sampling': 'F (and E at Nyquist)' if verdict['P4'] else '?',
    'parallax': 'R' if verdict['P5'] else '?',
    'disc': 'C-odd, a direction' if verdict['P6'] else '?',
    'sky': 'N' if verdict['P7'] else '?',
}
say('P8  the sort')
for k, v in sort.items():
    say('   ', k.ljust(12), v)
verdict['P8'] = all(v != '?' for v in sort.values())
say('   P8', 'not killed' if verdict['P8'] else 'KILLED')
say()
say('verdicts:', {k: ('not killed' if v else 'KILLED') for k, v in verdict.items()})

# ── Run 2: P5′ (plans/ckd-plan.md, written after run 1's kill) ──
say()
say('RUN 2  P5′  parallax: the give-out moves with ε as cot(ε/2)')
ok2 = True
for e in ['1e-2', '1e-3', '1e-4']:
    e = mp.mpf(e)
    r = give_out(e / 2) / give_out(e)
    exact = 2 / (1 - mp.tan(e / 4) ** 2)
    lead = (r - 2) / 2 / (e ** 2 / 16)
    say('   ε', mp.nstr(e, 3), ' ratio − exact form', mp.nstr(abs(r - exact), 3), ' (ratio/2 − 1)/(ε²/16)', mp.nstr(lead, 12))
    ok2 = ok2 and abs(r - exact) < mp.mpf('1e-40') and abs(lead - 1) < mp.mpf('0.01')
p5b = ok2 and abs(sep - mp.mpf('10.966')) < mp.mpf('1e-3')
say('   separation at ε = 1e-3:', mp.nstr(sep, 10), '; the corner d = B/2 =', B / 2, 'whatever ε')
say('   P5′', 'not killed' if p5b else 'KILLED')
p8b = p5b and all(verdict[k] for k in ['P1', 'P2', 'P3', 'P4', 'P6', 'P7'])
say('   P8′', 'not killed' if p8b else 'KILLED', '(parallax R)')
