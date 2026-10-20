"""A uniform, periodic sweep draws V = H in its own measure.

For observation-from-somewhere.md Proposition 3(g) and the ChatGPT follow-up in plans/ofs-review-10.md (15 October):
does any drawing V = cH with c != 1 keep the sweep smooth? It does (an ellipse is smooth), so smoothness alone cannot single out V = H. The claim checked here
is the stronger statement: if the sweep is uniform (every step the same linear map, a one-parameter group exp(tA)) and
returns after one full turn (exp(2*pi*A) = I), it preserves an inner product, unique up to one factor, and in that
inner product all of h and everything the sweep carries it to (all of v among them) have one length. On the page the
same sweep can show any c. The one free factor is the scale, H.
Random changes of coordinates P give A = P J P^-1; the invariant symmetric forms M solve A^T M + M A = 0.
Run: python3 runs/ofs/periodic.py   (mpmath, 30 digits; a second)
"""
import random
from mpmath import mp, mpf, matrix, expm, pi, sqrt, eye, norm, inverse, eig

mp.dps = 30
random.seed(1)
ok = True
for trial in range(8):
    P = matrix([[mpf(random.gauss(0, 1)) for _ in range(2)] for _ in range(2)])
    A = P * matrix([[0, -1], [1, 0]]) * inverse(P)
    period = norm(expm(2 * pi * A) - eye(2))
    cols = []                                         # the map M -> A^T M + M A on symmetric M, in the basis E11, E12, E22
    for (i, j) in [(0, 0), (0, 1), (1, 1)]:
        E = matrix(2, 2); E[i, j] = 1; E[j, i] = 1
        G = A.T * E + E * A
        cols.append([G[0, 0], G[0, 1], G[1, 0], G[1, 1]])
    L = matrix(4, 3)
    for k in range(3):
        for r in range(4):
            L[r, k] = cols[k][r]
    U, S, V = mp.svd_r(L)
    dim = sum(1 for s in S if abs(s) < mpf(10) ** -20)
    m = V[2, :]
    M = matrix([[m[0], m[1]], [m[1], m[2]]])
    if M[0, 0] < 0:
        M = -M
    own = lambda x: sqrt((x.T * M * x)[0])
    h_all = matrix([1, 0])
    v_all = expm(pi / 2 * A) * h_all                 # where a quarter of the sweep carries all of h
    other = expm(mpf('0.37') * A) * h_all             # any other point the sweep reaches
    page_c = norm(v_all) / norm(h_all)
    ratio, ratio2 = own(v_all) / own(h_all), own(other) / own(h_all)
    pd = all(e.real > 0 for e in eig(M)[0])
    good = period < mpf(10) ** -25 and dim == 1 and pd and abs(ratio - 1) < mpf(10) ** -25 and abs(ratio2 - 1) < mpf(10) ** -25
    ok &= good
    print(f"{'ok ' if good else 'BAD'} invariant inner products: {dim} (up to a factor), positive definite {pd}; on the page "
          f"c = {mp.nstr(page_c, 5)}; in the sweep's own measure all of v / all of h = {mp.nstr(ratio, 15)}")
print('all match' if ok else 'MISMATCH')
