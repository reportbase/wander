# A worked example: parallax in three dimensions with two thumbs (Reads and Writes §10, SPN R617).
# Exact (fractions). Run from the repo root: python3 runs/two/two_thumbs.py
# The reader looks along h; one thumb reads up (v/h), the other across (v2/h). H = 1 thumb.
from fractions import Fraction as F

def read(P, at):                       # the two thumbs' readings of point P from standpoint `at`
    h, v2, v = (P[i] - at[i] for i in range(3))
    return (v / h, v2 / h)             # (up, across)

def cross(rA, rB, step):               # place a point from two readings and a known step (in thumbs)
    # P = A + h*(1, a2, a1) = B + h'*(1, b2, b1), with B = A + step, h' = h - sh. Each transverse row gives
    #   across: h*(a2 - b2) = s2 - sh*b2      up: h*(a1 - b1) = s1 - sh*b1
    # A thumb whose reading moved gives the distance h; every row must then hold: its residual is the check
    # (the epipolar condition: the reading moves only along the step's own transverse direction).
    (a1, a2), (b1, b2) = rA, rB
    sh, s2, s1 = step
    rows = [(a2 - b2, s2 - sh * b2), (a1 - b1, s1 - sh * b1)]
    hs = [r / c for c, r in rows if c != 0]
    h = hs[0]
    resid = [c * h - r for c, r in rows]
    return hs, resid

A = (F(0), F(0), F(0))
tower = {'top': (F(12), F(4), F(3)), 'foot': (F(12), F(4), F(0))}   # (along, across, up), the writer's truth in thumbs
steps = {'across': (F(0), F(1), F(0)), 'up': (F(0), F(0), F(1)),
         'forward': (F(1), F(0), F(0)), 'diagonal': (F(0), F(1), F(1))}

for name, P in tower.items():
    print(name, 'from A (up, across):', read(P, A))
for sname, st in steps.items():
    print('\nstep', sname, st)
    for name, P in tower.items():
        rA, rB = read(P, A), read(P, st)
        hs, resid = cross(rA, rB, st)
        d = hs[0]
        place = (d, d * rA[1], d * rA[0])
        # the check: the change in the two readings lies along the step's own transverse direction
        print(f'  {name}: B reads {rB}; distance from each thumb that moved {hs}; check {resid}; place {place}; == truth {place == P}')
# scale the world (and the step) by k: no reading moves, no place in steps moves
k = F(7)
for name, P in tower.items():
    Pk = tuple(k * x for x in P); st = tuple(k * x for x in steps['across'])
    assert read(Pk, A) == read(P, A) and read(Pk, st) == read(P, steps['across'])
print('\nscaled by 7 (the step too): every reading the same')
# a misreading the second thumb catches: the step taken across, but the walker thinks it was diagonal
rA, rB = read(tower['top'], A), read(tower['top'], steps['across'])
hs, resid = cross(rA, rB, steps['diagonal'])
print('step across taken for diagonal: distance', hs, 'check', resid, '(the unmoved up thumb says no: caught)')
