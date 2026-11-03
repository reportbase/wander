"""ELM run 1 (plans/elm-plan.md): Euler's formula as a count of reads. Exact fractions and mpmath at 50 digits.

    python3 runs/elm/elm.py
"""
from fractions import Fraction as Fr
import mpmath as mp

mp.mp.dps = 50
ok = lambda b: 'not killed' if b else 'KILLED'
verdict = {}

# L1: composed reads by tangent addition, in fractions, against (1 + i s)^n in Q[i]
L1 = True
for th in (Fr(1), Fr(1, 2)):
    for n in range(1, 65):
        s = th / n
        acc = Fr(0)
        for _ in range(n):
            acc = (acc + s) / (1 - acc * s)          # tangent addition (never 1 - acc*s = 0 here: angle < pi/2)
        re, im = Fr(1), Fr(0)                        # (1 + i s)^n in Q[i]
        for _ in range(n):
            re, im = re - im * s, im + re * s
        if not (isinstance(acc, Fr) and acc == im / re):
            L1 = False
print(f'L1 closure: tangent addition = Im/Re of (1 + i s)^n in Q, theta = 1, 1/2, n = 1..64: {ok(L1)}')
verdict['L1'] = L1

# L2: the angle falls short by theta^3/(3 n^2)
L2 = True
for th in (mp.mpf(1), mp.pi / 2, mp.pi):
    n = 100
    short = th - n * mp.atan(th / n)
    r = short * n**2 / (th**3 / 3)
    L2 &= abs(r - 1) < 0.01
    print(f'L2 theta {mp.nstr(th, 6)}: n^2 * shortfall / (theta^3/3) = {mp.nstr(r, 8)} at n = 100')
print(f'L2: {ok(L2)}')
verdict['L2'] = L2

# L3: the length grows by theta^2/(2n); the reading does not see it
L3 = True
for th in (mp.mpf(1), mp.pi / 2, mp.pi):
    n = 1000
    R = (1 + th**2 / n**2) ** (n / 2)
    r = n * (R - 1) / (th**2 / 2)
    L3 &= abs(r - 1) < 0.01
    # reading with and without normalizing each step
    s = th / 100
    z1 = (1 + 1j * 0) ; z1 = mp.mpc(1, 0); z2 = mp.mpc(1, 0)
    step = mp.mpc(1, s)
    for _ in range(100):
        z1 = z1 * step
        z2 = z2 * step / abs(step)
    same = abs(z1.imag / z1.real - z2.imag / z2.real) < mp.mpf(10) ** -40
    L3 &= same
    print(f'L3 theta {mp.nstr(th, 6)}: n(R-1)/(theta^2/2) = {mp.nstr(r, 8)} at n = 1000; reading unchanged by normalizing: {same}')
print(f'L3: {ok(L3)}')
verdict['L3'] = L3

# L4: one limit, two axes
L4 = True
for name, w in (('1 (Bernoulli)', mp.mpc(1, 0)), ('i pi/2', mp.mpc(0, mp.pi / 2)), ('i pi', mp.mpc(0, mp.pi))):
    n = 1000
    En = (1 + w / n) ** n / mp.exp(w)
    lhs = n * (En - 1)
    rhs = -w**2 / 2
    rel = abs(lhs - rhs) / abs(rhs)
    L4 &= rel < 0.01
    land = (1 + w / n) ** n
    print(f'L4 w = {name}: n(E_n - 1) = {mp.nstr(lhs, 8)}, -w^2/2 = {mp.nstr(rhs, 8)}, off {mp.nstr(rel, 4)}; (1 + w/n)^n = {mp.nstr(land, 8)}')
print(f'L4: {ok(L4)}')
verdict['L4'] = L4

# L5: from a standpoint z = m + i gamma
m, g, t, n = mp.mpf('0.5'), mp.mpf('0.3'), mp.mpf(2), 1000
w = 1j * mp.mpc(m, g) * t
lhs = n * ((1 + w / n) ** n / mp.exp(w) - 1)
mine = mp.mpc(m**2 - g**2, 2 * m * g) * t**2 / 2
gem = mp.mpc(g**2 - m**2, 2 * m * g) * t**2 / 2
relm, relg = abs(lhs - mine) / abs(mine), abs(lhs - gem) / abs(gem)
L5 = relm < 0.01 and relm < relg
print(f'L5: n(E_n - 1) = {mp.nstr(lhs, 8)}; predicted {mp.nstr(mine, 6)} (off {mp.nstr(relm, 4)}); '
      f'with the other sign {mp.nstr(gem, 6)} (off {mp.nstr(relg, 4)}): {ok(L5)}')
verdict['L5'] = L5


# L6: turns of space, alternating against symmetric
def rot(axis, a):
    c, s = mp.cos(a), mp.sin(a)
    x, y, z = axis
    C = 1 - c
    return mp.matrix([[c + x*x*C, x*y*C - z*s, x*z*C + y*s],
                      [y*x*C + z*s, c + y*y*C, y*z*C - x*s],
                      [z*x*C - y*s, z*y*C + x*s, c + z*z*C]])


def angle(M):
    tr = (M[0, 0] + M[1, 1] + M[2, 2] - 1) / 2
    tr = max(min(tr, mp.mpf(1)), mp.mpf(-1))
    return mp.acos(tr)


t1, t2 = mp.mpf('0.7'), mp.mpf('0.4')
phi = mp.sqrt(t1**2 + t2**2)
whole = rot((t1 / phi, t2 / phi, 0), phi)
X, Y = (1, 0, 0), (0, 1, 0)
pred = (t1 * t2 / 2) * mp.sin(phi / 2) / (phi / 2)


def power(M, n):
    R = mp.eye(3)
    while n:
        if n & 1:
            R = R * M
        M = M * M
        n >>= 1
    return R


alt = {}
sym = {}
for n in (250, 500, 1000):
    A = power(rot(X, t1 / n) * rot(Y, t2 / n), n)
    S = power(rot(X, t1 / (2 * n)) * rot(Y, t2 / n) * rot(X, t1 / (2 * n)), n)
    alt[n] = angle(whole.T * A) * n
    sym[n] = angle(whole.T * S) * n**2
    print(f'L6 n = {n}: alternating n * leftover = {mp.nstr(alt[n], 8)}; symmetric n^2 * leftover = {mp.nstr(sym[n], 8)}')
# the plane: two turns about one axis alternate with no leftover
Z = (0, 0, 1)
import sys
RUN2 = '--run2' in sys.argv
if RUN2:   # L6': the largest entry of the difference, not acos of a trace near 1
    plane = max(max(abs(x) for x in (power(rot(Z, t1 / n) * rot(Z, t2 / n), n) - rot(Z, t1 + t2))) for n in (1, 7, 64, 1000))
else:
    plane = max(angle(power(rot(Z, t1 / n) * rot(Z, t2 / n), n).T * rot(Z, t1 + t2)) for n in (1, 7, 64, 1000))
a6 = abs(alt[1000] / pred - 1) < 0.02
b6 = max(sym.values()) / min(sym.values()) < 2
c6 = plane < mp.mpf(10) ** -40
L6 = a6 and b6 and c6
print(f'L6: alternating {mp.nstr(alt[1000], 6)} against {mp.nstr(pred, 6)} (off {mp.nstr(abs(alt[1000] / pred - 1), 4)}): {a6}; '
      f'symmetric steady within 2: {b6}; plane leftover {mp.nstr(plane, 3)}: {c6}; {ok(L6)}')
verdict['L6'] = L6

print('\nverdicts: ' + ', '.join(f'{k} {ok(v)}' for k, v in verdict.items()))
