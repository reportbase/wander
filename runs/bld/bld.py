# BLD run 1: pi and e from counts of reads. Construction uses integers only; mpmath only scores.
import sys, time
from mpmath import mp, mpf, pi, e, atan, log, ceil
mp.dps = 60

def gmul(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])

def gpow(z, n):
    r = (1, 0)
    while n:
        if n & 1: r = gmul(r, z)
        n >>= 1
        if n: z = gmul(z, z)
    return r

def count_to_horizon(m):
    z = (m, 1)
    lo, hi = 0, 1          # Re(z^lo) > 0
    while gpow(z, hi)[0] > 0:
        lo, hi = hi, hi * 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if gpow(z, mid)[0] > 0: lo = mid
        else: hi = mid
    re = gpow(z, hi)[0]
    return hi, re == 0

ms = [1, 2, 3, 5, 7, 10, 30, 100, 300, 1000, 3000, 10**4, 3*10**4, 10**5]
fails = []
for m in ms:
    t = time.time()
    N, landed = count_to_horizon(m)
    ref = int(ceil(pi / (2 * atan(mpf(1) / m))))
    d = N - pi * m / 2
    dp = 2 * mpf(N) / m - pi
    E = mpf((m + 1) ** m) / mpf(m ** m) if m <= 3000 else mp.exp(m * log(1 + mpf(1) / m))
    de = e / 2 - m * (e - E)
    b5 = m * (mpf(N) / 2) * log(1 + mpf(1) / m**2) - pi / 4
    b0 = (N == ref)
    b1 = m < 2 or (0 < d < 1 + mpf(1) / m)
    b2 = m < 2 or (0 < dp < mpf(2) / m + mpf(2) / m**2)
    b3 = (landed == (m == 1))
    b4 = m < 2 or (0 < de < mpf(1.25) / m)
    b5ok = m < 10 or abs(b5) < mpf(1) / m
    for k, ok in (('B0', b0), ('B1', b1), ('B2', b2), ('B3', b3), ('B4', b4), ('B5', b5ok)):
        if not ok: fails.append((k, m))
    print(f"m={m:>6} N={N:>7} landed={landed!s:5} N-pi m/2={float(d):.6f} 2N/m-pi={float(dp):.3e} "
          f"e/2-m(e-E)={float(de):.3e} (x m={float(de*m):.4f}) B5={float(b5):.3e} ({time.time()-t:.1f}s)")
    sys.stdout.flush()
print("fails:", fails if fails else "none")
