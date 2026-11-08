# TWG run 3: the next order of the small turn and boost loops. Predictions W7-W9 in plans/twg-plan.md.
import mpmath as mp
mp.mp.dps = 90
I = mp.mpc(0, 1)
sig = [mp.matrix([[0, 1], [1, 0]]), mp.matrix([[0, -I], [I, 0]]), mp.matrix([[1, 0], [0, -1]])]
def nd(n): return sum((n[k]*sig[k] for k in range(3)), mp.zeros(2))
def dag(M): return mp.matrix([[mp.conj(M[0,0]), mp.conj(M[1,0])], [mp.conj(M[0,1]), mp.conj(M[1,1])]])
def rot_of(M):  # polar decomposition M = H U; the rotation angle of U from its Pauli part (keeps digits near 0)
    A = M*dag(M); s = mp.sqrt(mp.det(A)); H = (A + s*mp.eye(2))/mp.sqrt(A[0,0] + A[1,1] + 2*s)
    U = mp.inverse(H)*M
    p = mp.sqrt(sum(abs((sig[k]*U)[0,0] + (sig[k]*U)[1,1])**2/4 for k in range(3)))
    return 2*mp.asin(p)
def loop(gen, n1, n2):
    a, b = gen(n1), gen(n2)
    return mp.expm(a)*mp.expm(b)*mp.expm(-a)*mp.expm(-b)
worst = {}
def note(k, v): worst[k] = max(worst.get(k, 0), abs(v))
print('phi   c_B pred      c_B(1e-3)        c_B(1e-4)        dep ratio   c_T(1e-4)')
for deg in [30, 45, 60, 90, 120, 150]:
    phi = mp.radians(deg); n1 = [1, 0, 0]; n2 = [mp.cos(phi), mp.sin(phi), 0]
    cpred = mp.mpf(1)/3 + mp.cos(phi)/4; deps = []; cts = []
    for eps in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')]:
        Ot = rot_of(loop(lambda n: -I*eps/2*nd(n), n1, n2))
        note('W7 exact turn formula', Ot - 4*mp.asin(mp.sin(eps/2)**2*abs(mp.sin(phi))))
        cts.append((Ot/(eps**2*mp.sin(phi)) - 1)/eps**2)
        Ob = rot_of(loop(lambda n: eps/2*nd(n), n1, n2))
        cb = (Ob/(eps**2*mp.sin(phi)) - 1)/eps**2; deps.append(cb - cpred)
    note('W7 c_T + 1/12 at 1e-4', cts[2] + mp.mpf(1)/12)
    note('W8 c_B - pred at 1e-4', deps[2])
    print(deg, mp.nstr(cpred, 10), mp.nstr(cpred + deps[1], 12), mp.nstr(cpred + deps[2], 12),
          mp.nstr(deps[1]/deps[2], 6), mp.nstr(cts[2], 10))
print('\nworst:')
for k, v in worst.items(): print('  %-28s %s' % (k, mp.nstr(v, 3)))
