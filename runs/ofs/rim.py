"""OFS §10 step 3: the two sweeps joined by their rates on the mountain example (CIW on the range's own numbers). Exact (mpmath)."""
import mpmath as mp
mp.mp.dps = 50
ok = {}
H = mp.mpf(1); V = mp.mpf(20); d = mp.mpf(10)        # the writer's amounts, miles
home = mp.mpc(0, 0); M = mp.mpc(0, d); R = V / 2     # the reader, the range's middle, the half-width
ends = [mp.mpc(-V / 2, d), mp.mpc(V / 2, d)]

# the central reader's circle about M through the ends passes through home
ok['circle'] = all(abs(abs(p - M) - R) < mp.mpf('1e-45') for p in ends + [home])
# the reader sees the ends 45 deg either side of straight ahead; the central reader 90 deg either side of the line to home
up = mp.mpc(0, 1)
read = [mp.degrees(abs(mp.arg((p - home) / up))) for p in ends]
cen = [mp.degrees(abs(mp.arg((p - M) / (home - M)))) for p in ends]
ok['angles'] = all(abs(a - 45) < 1e-40 for a in read) and all(abs(a - 90) < 1e-40 for a in cen)

# in the range's radius the reader stands at z = (home - M)/R, on the circle; the inscribed rate is 1/2 at every phi
z = (home - M) / R
def rate(phi):
    zeta = mp.expj(phi)
    return (1 - mp.re(mp.conj(z) * zeta)) / abs(zeta - z)**2
worst = mp.mpf(0); worst_num = mp.mpf(0)
for i in range(1, 360):
    phi = mp.arg(z) + mp.radians(i)
    worst = max(worst, abs(rate(phi) - mp.mpf(1) / 2))
    num = mp.diff(lambda p: mp.arg(mp.expj(p) - z), phi)
    worst_num = max(worst_num, abs(num - mp.mpf(1) / 2))
ok['rate'] = worst < mp.mpf('1e-45') and worst_num < mp.mpf('1e-40')
# so 2 x rate - 1 = 0 away from home; just inside the rim (the reader a hair toward M) the combination's mass gathers at home
def mass_near(eps, w):
    rho = 1 - eps
    c = mp.arg(z)
    F = lambda p: mp.atan((1 + rho) / (1 - rho) * mp.tan((p - c) / 2)) / mp.pi
    return F(c + w) - F(c - w)
masses = [(e, mass_near(mp.mpf(e), mp.radians(1))) for e in ('1e-2', '1e-4', '1e-8')]
ok['spike'] = masses[-1][1] > 1 - mp.mpf('1e-5')

# scaling the world by k moves none of it
worst_k = mp.mpf(0)
for k in (mp.mpf('1e-3'), mp.mpf(7), mp.mpf(1000)):
    zk = (k * home - k * M) / (k * R)
    worst_k = max(worst_k, abs(zk - z))
ok['scale'] = worst_k < mp.mpf('1e-45')

print('the central circle about the middle, radius V*/2 = %s, through both ends and home:' % mp.nstr(R, 3), ok['circle'])
print('ends from home %s deg, from the middle %s deg either side:' % ([mp.nstr(a, 6) for a in read], [mp.nstr(a, 6) for a in cen]), ok['angles'])
print('z = %s (|z| = %s); inscribed rate 1/2 at every phi to %s (numerically %s):'
      % (mp.nstr(z, 4), mp.nstr(abs(z), 6), mp.nstr(worst, 3), mp.nstr(worst_num, 3)), ok['rate'])
print('2 x rate - 1 = 0 away from home; a hair inside, the mass within 1 deg of home:',
      ', '.join('eps %s: %s' % (e, mp.nstr(m, 8)) for e, m in masses), ok['spike'])
print('scaled by 1e-3, 7, 1000, z moves by %s:' % mp.nstr(worst_k, 3), ok['scale'])
print('all', all(ok.values()))
