"""LWS run 3: is a change of chart a chain in disguise? (plans/lws-plan.md, predictions C1-C4.)

The 20 chart laws of runs/lws/sorting.md. For each: is it a bijection of one reading (C1); does the reads' own
composition, moved into its chart, telescope over a five-link chain (C2, an identity: a check of the code); does the
chart carry that composition to plain addition or plain multiplication (C3); and is every additive chart
transcendental and no rational chart additive (C4). mpmath at 50 digits. Run from the repository root.
"""
import mpmath as mp

mp.mp.dps = 50
import sys
RUN = sys.argv[1] if len(sys.argv) > 1 else '3'  # '3b' checks the square map by its angle
TOL = mp.mpf(10) ** -40
I = mp.mpc(0, 1)
pi = mp.pi


def close(a, b):
    return abs(a - b) < TOL * (1 + abs(b))


def tplus(a, b):  # tangent addition, the reads' composition of slopes
    return (a + b) / (1 - a * b)


def vplus(a, b):  # velocity addition
    return (a + b) / (1 + a * b)


def monotone(f, lo, hi, n=400):
    xs = [lo + (hi - lo) * mp.mpf(k) / n for k in range(1, n)]
    ys = [f(x) for x in xs]
    d = [ys[k + 1] - ys[k] for k in range(len(ys) - 1)]
    return all(v > 0 for v in d) or all(v < 0 for v in d)


def w(s):
    return (1 + I * s) / (1 - I * s)


# Each chart: id, name, kind ('chart' of one reading, 'action' a family of maps, 'none' not a bijection), and
# the pieces its checks need. 'target' is what the chart carries the reads' composition to: 'add', 'mult' or a name.
S = [mp.mpf(1) / 7, mp.mpf(1) / 5, mp.mpf(-1) / 9, mp.mpf(1) / 4, mp.mpf(1) / 6, mp.mpf(1) / 3]  # slopes, small
X = [mp.mpf(2), mp.mpf('0.7'), mp.mpf(5), mp.mpf('0.3'), mp.mpf(9), mp.mpf('1.6')]  # scale readings d/H


def chain_check(phi, phiinv, op, inv, reads):
    """In the chart q = phi(read), the step between q_a and q_b is phi(op(phiinv(q_b), inv(phiinv(q_a)))); composing
    the steps along the chain (by the chart's moved composition) gives the step from first to last."""
    qs = [phi(r) for r in reads]
    move = lambda q1, q2: phi(op(phiinv(q1), phiinv(q2)))
    step = lambda qa, qb: phi(op(phiinv(qb), inv(phiinv(qa))))
    acc = step(qs[0], qs[1])
    for j in range(1, len(qs) - 1):
        acc = move(acc, step(qs[j], qs[j + 1]))
    return close(acc, step(qs[0], qs[-1]))


def target_of(phi, op, a, b):
    qa, qb, qab = phi(a), phi(b), phi(op(a, b))
    if close(qab, qa + qb):
        return 'add'
    if close(qab, qa * qb):
        return 'mult'
    return None


res = []


def chart(n, name, phi, phiinv, op, inv, reads, lo, hi, transcendental, mono=None):
    bij = monotone(mono or phi, lo, hi)
    c2 = chain_check(phi, phiinv, op, inv, reads)
    tg = {target_of(phi, op, reads[i], reads[i + 1]) for i in range(len(reads) - 1)}
    tg = tg.pop() if len(tg) == 1 else None
    res.append(dict(n=n, name=name, bij=bij, c2=c2, target=tg, trans=transcendental))


def action(n, name, T, compose_param, params, pts, transcendental, lo, hi):
    """A family of maps T_p: bijections of one reading whose composition is a law on p."""
    bij = all(monotone(lambda t, p=p: T(p, t), lo, hi) for p in params[:2])
    ok = all(close(T(a, T(b, t)), T(compose_param(a, b), t)) for a in params for b in params for t in pts)
    # a five-link chain of maps composes to one map
    acc = params[0]
    for p in params[1:]:
        acc = compose_param(acc, p)
    tot = lambda t: T(acc, t)
    seq = lambda t: [t := T(p, t) for p in reversed(params)][-1]
    c2 = all(close(seq(t), tot(t)) for t in pts)
    # the target: is the parameter's composition plain multiplication or addition?
    a, b = params[0], params[1]
    tg = 'mult' if close(compose_param(a, b), a * b) else ('add' if close(compose_param(a, b), a + b) else None)
    res.append(dict(n=n, name=name, bij=bij, c2=c2 and ok, target=tg, trans=transcendental))


# 1: a point in two parts, ln(z/H) = ln(d/H) + i*theta: the complex logarithm of the point, products of points to sums
Z = [mp.mpf(2) * mp.expj(0.3), mp.mpf('0.5') * mp.expj(0.2), mp.mpf(3) * mp.expj(-0.1), mp.mpf('1.5') * mp.expj(0.25),
     mp.mpf('0.8') * mp.expj(0.1), mp.mpf(4) * mp.expj(-0.2)]
chart(1, 'ln z', mp.log, mp.exp, lambda a, b: a * b, lambda a: 1 / a, Z, mp.mpf('0.1'), mp.mpf(10), True,
      mono=lambda r: mp.log(r))
# 11, 97: halving a turn / bisecting a direction, t = s/(1 + sqrt(1 + s^2)); carries tangent addition to itself
half = lambda s: s / (1 + mp.sqrt(1 + s * s))
halfinv = lambda t: 2 * t / (1 - t * t)
chart(11, 'halving t = s/(1 + sqrt(1 + s^2))', half, halfinv, tplus, lambda a: -a, S, 0, 20, False)
chart(97, 'bisecting (sqrt(1 + s^2) - 1)/s', lambda s: (mp.sqrt(1 + s * s) - 1) / s if s != 0 else mp.mpf(0),
      halfinv, tplus, lambda a: -a, S, mp.mpf('0.01'), 20, False)
# 13: slope and angle by the half-angle, the chart phi = 2*arctan s
chart(13, 'angle 2*arctan s', lambda s: 2 * mp.atan(s), lambda f: mp.tan(f / 2), tplus, lambda a: -a, S, 0, 20, True)
# 15: the two mirrors; the distance clause d/H -> H/d on scale readings (multiplication)
chart(15, 'mirror x -> 1/x', lambda x: 1 / x, lambda q: 1 / q, lambda a, b: a * b, lambda a: 1 / a, X,
      mp.mpf('0.1'), 10, False)
# 16: the thumb's lay as a turn, (2/pi)*arctan(d/H), on scale readings
chart(16, 'lay (2/pi) arctan x', lambda x: 2 / pi * mp.atan(x), lambda q: mp.tan(q * pi / 2), lambda a, b: a * b,
      lambda a: 1 / a, X, mp.mpf('0.1'), 10, True)
# 17: a larger thumb as a boost of latitudes, tan(chi'/2) = tan(chi/2)/k
action(17, 'boost of latitudes t -> t/k', lambda k, t: t / k, lambda a, b: a * b,
       [mp.mpf(2), mp.mpf(3), mp.mpf('0.5'), mp.mpf(7), mp.mpf('1.25')], [mp.mpf('0.3'), mp.mpf(2)], False, 0, 5)
# 18, 111: the square of the direction, u -> u^2 on unit directions
U = [mp.expj(0.1), mp.expj(0.2), mp.expj(-0.05), mp.expj(0.15), mp.expj(0.05), mp.expj(0.3)]
for n, nm in [(18, 'square (h + iv)^2'), (111, 'squares rational (h^2 - v^2) + 2ihv')]:
    chart(n, nm, lambda u: u * u, mp.sqrt, lambda a, b: a * b, lambda a: 1 / a, U, 0, mp.pi / 2, False,
          mono=(lambda th: mp.im(mp.expj(th) ** 2 / mp.expj(0)) if th < mp.pi / 4 else -mp.re(mp.expj(th) ** 2))
          if RUN == '3' else (lambda th: mp.arg(mp.expj(th) ** 2)))
# 20, 30: Euler's form of the reading / the Cayley map, w(s) = (1 + is)/(1 - is)
winv = lambda q: mp.tan(mp.arg(q) / 2)
for n, nm in [(20, "Euler's form w = (1 + is)/(1 - is)"), (30, 'the Cayley map')]:
    chart(n, nm, w, winv, tplus, lambda a: -a, S, 0, 20, False, mono=lambda s: mp.arg(w(s)))
# 44: Mercator's bearings, tan psi' = tan psi / c (the bearing clause; the area clause is a factor)
action(44, "Mercator's bearings t -> t/c", lambda c, t: t / c, lambda a, b: a * b,
       [mp.mpf(2), mp.mpf('0.6'), mp.mpf(3), mp.mpf('1.5'), mp.mpf('0.9')], [mp.mpf('0.4'), mp.mpf(3)], False, 0, 5)
# 45: aberration cos(theta') = (cos(theta) + beta)/(1 + beta cos(theta)); beta composes by velocity addition
action(45, 'aberration', lambda b, c: (c + b) / (1 + b * c), vplus,
       [mp.mpf('0.3'), mp.mpf('0.5'), mp.mpf('-0.2'), mp.mpf('0.6'), mp.mpf('0.1')], [mp.mpf('0.2'), mp.mpf('-0.7')],
       False, -1, 1)
# 49: pseudorapidity xi = -ln tan(theta/2); aberration is a slide of xi by the rapidity
xi = lambda th: -mp.log(mp.tan(th / 2))
xiinv = lambda q: 2 * mp.atan(mp.exp(-q))
ab = lambda b, th: mp.acos((mp.cos(th) + b) / (1 + b * mp.cos(th)))
B5 = [mp.mpf('0.3'), mp.mpf('0.5'), mp.mpf('-0.2'), mp.mpf('0.6'), mp.mpf('0.1')]
slides = [[xi(ab(b, th)) - xi(th) for th in [mp.mpf('0.4'), mp.mpf(1), mp.mpf('2.2')]] for b in B5]
const = all(close(s[0], s[1]) and close(s[0], s[2]) for s in slides)
rap = [mp.atanh(b) for b in B5]
adds = all(close(slides[i][0], rap[i]) for i in range(5))
res.append(dict(n=49, name='pseudorapidity (aberration a slide)', bij=monotone(xi, mp.mpf('0.01'), mp.pi - mp.mpf('0.01')),
                c2=const and adds and close(sum(rap), xi(ab(vplus(vplus(vplus(vplus(B5[0], B5[1]), B5[2]), B5[3]), B5[4]),
                                                           mp.mpf(1))) - xi(mp.mpf(1))),
                target='add' if const and adds else None, trans=True))
# 53: Lambert's equal-area radius R = 2 sin(alpha/2), angles off the look added
A = [mp.mpf('0.1'), mp.mpf('0.2'), mp.mpf('0.05'), mp.mpf('0.15'), mp.mpf('0.3'), mp.mpf('0.25')]
chart(53, "Lambert's radius 2 sin(a/2)", lambda a: 2 * mp.sin(a / 2), lambda r: 2 * mp.asin(r / 2),
      lambda a, b: a + b, lambda a: -a, A, 0, mp.pi - mp.mpf('0.01'), True)
# 56: the dial, place sinh(zeta) (and needle gd(zeta)); the push zeta adds
Zt = [mp.mpf('0.2'), mp.mpf('0.5'), mp.mpf('-0.3'), mp.mpf('0.9'), mp.mpf('0.1'), mp.mpf('1.4')]
chart(56, 'the dial, place sinh(zeta)', mp.sinh, mp.asinh, lambda a, b: a + b, lambda a: -a, Zt, -3, 3, True)
# 59: a read from a height as a Cauchy point, w = (c + i g)/(1 - i g c): c composed with i*g by tangent addition
g = mp.mpf('0.3')
p59 = lambda c: (c + I * g) / (1 - I * g * c)
ok59 = all(close(p59(c), tplus(c, I * g)) for c in S)
res.append(dict(n=59, name='a read from a height, c (+) i*gamma', bij=monotone(lambda c: mp.re(p59(c)) , -1, 1),
                c2=ok59, target=None, trans=False))
# 94: rational rotation ((q^2 - p^2), 2pq)/(q^2 + p^2) from t = p/q; tangent addition to complex multiplication
rot = lambda t: mp.mpc(1 - t * t, 2 * t) / (1 + t * t)
chart(94, 'rational rotation', rot, lambda q: mp.tan(mp.arg(q) / 2), tplus, lambda a: -a, S, 0, 1, False,
      mono=lambda t: mp.arg(rot(t)))
# 14 and 21: not bijections of one reading
res.append(dict(n=14, name='a straight line on Euler\'s plane (a family of curves)', bij=False, c2=None, target=None,
                trans=True))
res.append(dict(n=21, name="Lambert's chart turned (a stretch factor)", bij=False, c2=None, target=None, trans=True))

res.sort(key=lambda r: r['n'])
for r in res:
    print(f"{r['n']:>4}  bij {str(r['bij']):5}  C2 {str(r['c2']):5}  target {str(r['target']):5}  "
          f"{'transcendental' if r['trans'] else 'rational/algebraic':18}  {r['name']}")
bij = [r for r in res if r['bij']]
print(f"\nC1 bijections: {len(bij)} of {len(res)} (kill under 14)")
print(f"C2 chains telescope in every bijection: {all(r['c2'] for r in bij)}")
grp = [r for r in bij if r['target'] in ('add', 'mult')]
print(f"C3 group charts (add or mult): {len(grp)} (kill under 10): "
      f"{[(r['n'], r['target']) for r in grp]}")
addc = [r for r in bij if r['target'] == 'add']
c4a = all(r['trans'] for r in addc)
c4b = not any((not r['trans']) and r['target'] == 'add' for r in bij)
print(f"C4 additive charts all transcendental: {c4a}; no rational chart additive: {c4b}: {[r['n'] for r in addc]}")
