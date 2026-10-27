"""TWR: a tower of ratios, built while walking (plans/twr-plan.md).
Exact parts in mpmath at 50 digits; the noisy runs (T5) in mpmath at 20 digits with a seeded generator."""
import math, random, itertools, sys
import mpmath as mp

mp.mp.dps = 50
EXACT = mp.mpf(10) ** -40
ok = {}

# ---------------------------------------------------------------- the referee's world (metres)
def make_world(seed=1):
    rnd = random.Random(seed)
    feats = {}                                   # name -> (x, y) in metres
    for x in (0, 10, 20):
        for y in (0, 8, 16):
            feats[f'C{x},{y}'] = (mp.mpf(x), mp.mpf(y))   # the 9 distinct room corners
    doors = {'D12': (10, 4), 'D34': (10, 12), 'D13': (5, 8), 'D24': (15, 8)}
    for n, (x, y) in doors.items():
        feats[n] = (mp.mpf(x), mp.mpf(y))
    rooms = {1: (0, 0), 2: (10, 0), 3: (0, 8), 4: (10, 8)}
    things = {}
    for r, (x0, y0) in rooms.items():
        placed = []
        while len(placed) < 3:
            w = mp.mpf(rnd.randint(60, 200)) / 100
            d = mp.mpf(rnd.randint(50, 160)) / 100
            cx = x0 + mp.mpf(rnd.randint(150, 850)) / 100
            cy = y0 + mp.mpf(rnd.randint(150, 650)) / 100
            if any(abs(cx - px) < (w + pw) / 2 + mp.mpf('0.3') and abs(cy - py) < (d + pd) / 2 + mp.mpf('0.3')
                   for px, py, pw, pd in placed):
                continue
            placed.append((cx, cy, w, d))
        for i, (cx, cy, w, d) in enumerate(placed):
            name = f'T{r}{i}'
            cs = [(cx - w / 2, cy - d / 2), (cx + w / 2, cy - d / 2), (cx + w / 2, cy + d / 2), (cx - w / 2, cy + d / 2)]
            for j, c in enumerate(cs):
                feats[f'{name}.{j}'] = c
            things[name] = (r, [f'{name}.{j}' for j in range(4)])
    return feats, things, rooms

def make_walk(seed=2, n=32, box=((3, 3), (17, 13))):
    """A closed loop of n stops round a rectangle through the four rooms, seeded jitter."""
    rnd = random.Random(seed)
    (x0, y0), (x1, y1) = box
    per = 2 * ((x1 - x0) + (y1 - y0))
    pts = []
    for i in range(n):
        s = per * i / n
        if s < x1 - x0: p = (x0 + s, y0)
        elif s < (x1 - x0) + (y1 - y0): p = (x1, y0 + s - (x1 - x0))
        elif s < 2 * (x1 - x0) + (y1 - y0): p = (x1 - (s - (x1 - x0) - (y1 - y0)), y1)
        else: p = (x0, y1 - (s - 2 * (x1 - x0) - (y1 - y0)))
        jx, jy = rnd.uniform(-0.5, 0.5), rnd.uniform(-0.5, 0.5)
        pts.append((mp.mpf(p[0]) + mp.mpf(round(jx, 3)), mp.mpf(p[1]) + mp.mpf(round(jy, 3))))
    return pts

# ---------------------------------------------------------------- small geometry
def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def add(a, b): return (a[0] + b[0], a[1] + b[1])
def mul(a, s): return (a[0] * s, a[1] * s)
def cross(a, b): return a[0] * b[1] - a[1] * b[0]
def norm(a): return mp.sqrt(a[0] ** 2 + a[1] ** 2)
def unit(a): n = norm(a); return (a[0] / n, a[1] / n)
def rot(a, t): c, s = mp.cos(t), mp.sin(t); return (c * a[0] - s * a[1], s * a[0] + c * a[1])
def ang(a): return mp.atan2(a[1], a[0])

# ---------------------------------------------------------------- readings (the reader's own frame)
class Readings:
    """What the reader receives: each leg's heading and each held feature's direction, in its own frame (its first
    heading 0), with an optional normal error eps on every direction. Never a length."""
    def __init__(self, feats, stops, k=1, R=6, eps=0, rng=None, extra=0):
        self.k = mp.mpf(k)
        F = {n: mul(p, self.k) for n, p in feats.items()}
        S = [mul(p, self.k) for p in stops]
        n = len(stops)
        S = S + [S[i % n] for i in range(n, n + extra)]            # walk on past the start (closure)
        self.n = len(S)
        th0 = ang(sub(S[1], S[0]))
        noise = (lambda: mp.mpf(rng.gauss(0, eps))) if eps else (lambda: 0)
        self.u = [unit(rot(sub(S[i + 1], S[i]), -th0 + noise())) for i in range(self.n - 1)]
        self.held, self.b = [], []
        for i in range(self.n):
            hs = {f for f, p in F.items() if norm(sub(p, S[i])) <= R * self.k}
            self.held.append(hs)
            self.b.append({f: unit(rot(sub(F[f], S[i]), -th0 + noise())) for f in hs})
        # the referee's own, kept apart: true map in the reader's frame, divided by the true first leg
        L0 = norm(sub(S[1], S[0]))
        self.truth = {f: mul(rot(sub(p, S[0]), -th0), 1 / L0) for f, p in F.items()}
        self.truth_stops = [mul(rot(sub(p, S[0]), -th0), 1 / L0) for p in S]
        self.true_legs = [norm(sub(S[i + 1], S[i])) / L0 for i in range(self.n - 1)]
        self.L0_m = L0

def triangulate(rays):
    """Least-squares meeting point of rays [(P, b)]."""
    a11 = a12 = a22 = r1 = r2 = 0
    for P, b in rays:
        m11, m12, m22 = 1 - b[0] ** 2, -b[0] * b[1], 1 - b[1] ** 2
        a11 += m11; a12 += m12; a22 += m22
        r1 += m11 * P[0] + m12 * P[1]; r2 += m12 * P[0] + m22 * P[1]
    det = a11 * a22 - a12 ** 2
    return ((a22 * r1 - a12 * r2) / det, (a11 * r2 - a12 * r1) / det)

def build(rd, M=None, window=None, tiny=mp.mpf(10) ** -20):
    """The reader's map from rd alone. M: features remembered (most recently seen); window: rays older than this many
    stops dropped (an open chain). Returns legs, stops, pieces, breaks and a per-step log."""
    P = {0: (mp.mpf(0), mp.mpf(0)), 1: rd.u[0]}
    L = {0: mp.mpf(1)}
    piece = [0] * rd.n
    rays = {}                     # feature -> list of (stop, b)
    last_seen = {}
    X = {}
    pieces = []                   # finished pieces: dict(stops, X)
    breaks, rule = [], []
    cur_piece = 0
    def record(i):
        for f in rd.held[i]:
            rays.setdefault(f, []).append((i, rd.b[i][f]))
            last_seen[f] = i
    def forget(i):
        if window is not None:
            for f in list(rays):
                rays[f] = [(j, b) for j, b in rays[f] if j > i - window]
                if not rays[f]: del rays[f]
        if M is not None:
            keep = sorted(last_seen, key=lambda f: (-last_seen[f], f))[:M]
            for f in list(rays):
                if f not in keep: del rays[f]
            for f in list(last_seen):
                if f not in keep: del last_seen[f]
    def place():
        X.clear()
        for f, rs in rays.items():
            rs2 = [(P[j], b) for j, b in rs if j in P and piece[j] == cur_piece]
            if len(rs2) >= 2 and any(abs(cross(rs2[0][1], b)) > tiny for _, b in rs2[1:]):
                X[f] = triangulate(rs2)
    record(0); record(1); forget(1); place()
    for k in range(1, rd.n - 1):
        u = rd.u[k]; nxt = k + 1
        cand = [f for f in rd.held[nxt] if f in X and abs(cross(rd.b[nxt][f], u)) > tiny]
        rule.append((nxt, len(cand) == 0))
        if cand:
            num = sum(cross(rd.b[nxt][f], sub(X[f], P[k])) * cross(rd.b[nxt][f], u) for f in cand)
            den = sum(cross(rd.b[nxt][f], u) ** 2 for f in cand)
            L[k] = num / den
            P[nxt] = add(P[k], mul(u, L[k]))
            piece[nxt] = cur_piece
        else:
            breaks.append(nxt)
            pieces.append({'stops': {j: P[j] for j in P if piece[j] == cur_piece}, 'X': dict(X)})
            cur_piece += 1
            rays.clear(); last_seen.clear(); X.clear()
            P[nxt] = (mp.mpf(0), mp.mpf(0)); piece[nxt] = cur_piece
            if nxt + 1 < rd.n:                       # the next leg is the new piece's H
                L[nxt] = mp.mpf(1); P[nxt + 1] = rd.u[nxt]; piece[nxt + 1] = cur_piece
        record(nxt); forget(nxt); place()
        if nxt in L and nxt + 1 in P and piece[nxt + 1] == cur_piece and nxt + 1 > k + 1:
            record(nxt + 1); forget(nxt + 1); place()
    pieces.append({'stops': {j: P[j] for j in P if piece[j] == cur_piece}, 'X': dict(X)})
    return {'L': L, 'P': P, 'piece': piece, 'pieces': pieces, 'breaks': breaks, 'rule': rule, 'X': X}

def full_map(rd, res):
    """Every feature placed from every stop of piece 0 that saw it (the reader's map at the end of the walk)."""
    out = {}
    for f in set().union(*rd.held):
        rs = [(res['P'][i], rd.b[i][f]) for i in range(rd.n) if f in rd.held[i] and i in res['P'] and res['piece'][i] == 0]
        if len(rs) >= 2 and any(abs(cross(rs[0][1], b)) > mp.mpf(10) ** -20 for _, b in rs[1:]):
            out[f] = triangulate(rs)
    return out

def maxdiff(a, b, keys):
    return max((norm(sub(a[f], b[f])) for f in keys), default=mp.mpf(0))

# ---------------------------------------------------------------- links (ratios of lengths)
def links(X, things, rooms):
    out = {}
    def d(p, q): return norm(sub(X[p], X[q]))
    def have(*fs): return all(f in X for f in fs)
    rw = {1: ('C0,0', 'C10,0'), 2: ('C10,0', 'C20,0'), 3: ('C0,8', 'C10,8'), 4: ('C10,8', 'C20,8')}
    for t, (r, cs) in things.items():
        if have(*cs[:3]):
            out[f'{t} w/d'] = d(cs[0], cs[1]) / d(cs[1], cs[2])
            if have(*rw[r]):
                out[f'{t} w/room'] = d(cs[0], cs[1]) / d(*rw[r])
    for r in rooms:
        ts = [t for t, (rr, _) in things.items() if rr == r]
        for a, b in itertools.combinations(ts, 2):
            ca, cb = things[a][1], things[b][1]
            if have(*ca, *cb, *rw[r]):
                ma = mul(add(add(X[ca[0]], X[ca[1]]), add(X[ca[2]], X[ca[3]])), mp.mpf(1) / 4)
                mb = mul(add(add(X[cb[0]], X[cb[1]]), add(X[cb[2]], X[cb[3]])), mp.mpf(1) / 4)
                out[f'{a}-{b}/room'] = norm(sub(ma, mb)) / d(*rw[r])
    if have('C0,0', 'C10,0', 'C20,0'):
        out['room/building'] = d('C0,0', 'C10,0') / d('C0,0', 'C20,0')
    return out

feats, things, rooms = make_world()
stops = make_walk()
print(f'world: {len(feats)} features ({len(things)} things, 9 room corners, 4 door points); walk: {len(stops)} stops')

# ---------------------------------------------------------------- T1, T2
rd = Readings(feats, stops)
res = build(rd)
mp_map = full_map(rd, res)
legs_ok = len(res['L']) == rd.n - 1 and not res['breaks']
legerr = max(abs(res['L'][i] - rd.true_legs[i]) for i in res['L'])
stoperr = max(norm(sub(res['P'][i], rd.truth_stops[i])) for i in res['P'])
featerr = maxdiff(mp_map, rd.truth, mp_map)
seen = set().union(*rd.held)
print(f'T1: legs solved {len(res["L"])}/{rd.n - 1}, breaks {res["breaks"]}; features placed {len(mp_map)}/{len(seen)} seen; '
      f'worst leg {mp.nstr(legerr, 3)}, stop {mp.nstr(stoperr, 3)}, feature {mp.nstr(featerr, 3)}')
ok['T1'] = legs_ok and len(mp_map) == len(seen) and max(legerr, stoperr, featerr) < EXACT

t2 = True
base_links = links(mp_map, things, rooms)
for k in (mp.mpf('1e-3'), mp.mpf(7), mp.mpf('1e3')):
    rk = Readings(feats, stops, k=k)
    rs = build(rk); mk = full_map(rk, rs); lk = links(mk, things, rooms)
    dm = maxdiff(mk, mp_map, mp_map); dl = max(abs(res['L'][i] - rs['L'][i]) for i in res['L'])
    dk = max(abs(lk[x] - base_links[x]) for x in base_links)
    print(f'T2: k = {mp.nstr(k, 3)}: map {mp.nstr(dm, 3)}, legs {mp.nstr(dl, 3)}, links {mp.nstr(dk, 3)}')
    t2 &= max(dm, dl, dk) < mp.mpf(10) ** -45 and set(lk) == set(base_links)
ok['T2'] = t2

# ---------------------------------------------------------------- T3
churn = True; changes = []
for i in range(1, len(stops)):
    both = rd.held[i] & rd.held[i - 1]
    same = [f for f in both if norm(sub(rd.b[i][f], rd.b[i - 1][f])) < EXACT]
    added, dropped = rd.held[i] - rd.held[i - 1], rd.held[i - 1] - rd.held[i]
    changes.append((len(rd.held[i]), len(added), len(dropped)))
    churn = churn and not same and bool(added or dropped)
true_links = links(rd.truth, things, rooms)
worst, checked, pairs_with = mp.mpf(0), 0, 0
for k in range(len(stops) - 1):
    rs2 = {}
    for f in rd.held[k] & rd.held[k + 1]:
        rays2 = [(res['P'][k], rd.b[k][f]), (res['P'][k + 1], rd.b[k + 1][f])]
        if abs(cross(rays2[0][1], rays2[1][1])) > mp.mpf(10) ** -20:
            rs2[f] = triangulate(rays2)
    lk = links(rs2, things, rooms)
    if lk: pairs_with += 1
    for x, val in lk.items():
        worst = max(worst, abs(val - true_links[x])); checked += 1
held_n = [c[0] for c in changes]
print(f'T3 (a): every direction changed at every step: {churn}; held {min(held_n)}–{max(held_n)} a stop, '
      f'added+dropped {min(a + d for _, a, d in changes)}–{max(a + d for _, a, d in changes)} a step')
print(f'T3 (b): {checked} link readings from {pairs_with} consecutive pairs, {len(true_links)} distinct links; worst {mp.nstr(worst, 3)}')
ok['T3'] = churn and checked > 0 and worst < EXACT

# ---------------------------------------------------------------- T4
t4 = True
for M in (2, 3, 4, 6, 8, 12):
    r4 = build(rd, M=M)
    rule_breaks = [s for s, b in r4['rule'] if b]
    agree = rule_breaks == r4['breaks']
    # (a) links within each piece
    worst_a, n_a = mp.mpf(0), 0
    piece_maps = []
    for pi, pc in enumerate(r4['pieces']):
        st = sorted(pc['stops'])
        # rebuild the piece's map from its own stops (every feature it saw), in its own H
        pm = {}
        for f in set().union(*[rd.held[i] for i in st]):
            rs = [(pc['stops'][i], rd.b[i][f]) for i in st if f in rd.held[i]]
            if len(rs) >= 2 and any(abs(cross(rs[0][1], b)) > mp.mpf(10) ** -20 for _, b in rs[1:]):
                pm[f] = triangulate(rs)
        piece_maps.append((st, pm))
        for x, val in links(pm, things, rooms).items():
            worst_a = max(worst_a, abs(val - true_links[x])); n_a += 1
    # (b) rejoining: the ratio of two pieces' H from one thing (two features) both placed
    worst_b, n_b = mp.mpf(0), 0
    for (sa, ma), (sb, mb) in itertools.combinations(piece_maps, 2):
        common = [t for t, (_, cs) in things.items() if cs[0] in ma and cs[1] in ma and cs[0] in mb and cs[1] in mb]
        if not common: continue
        t = common[0]; c0, c1 = things[t][1][0], things[t][1][1]
        ratio = norm(sub(ma[c0], ma[c1])) / norm(sub(mb[c0], mb[c1]))      # H_b / H_a
        Ha = rd.true_legs[sa[0]] if sa[0] > 0 else mp.mpf(1)
        Hb = rd.true_legs[sb[0]]
        worst_b = max(worst_b, abs(ratio - Hb / Ha)); n_b += 1
    # (c) a link read, forgotten, and read again on the return
    worst_c, n_c = mp.mpf(0), 0
    firsts = {}
    for st, pm in piece_maps:
        for x, val in links(pm, things, rooms).items():
            if x in firsts:
                worst_c = max(worst_c, abs(val - firsts[x])); n_c += 1
            else:
                firsts[x] = val
    print(f'T4 M = {M:2d}: breaks {r4["breaks"]} (rule agrees: {agree}), pieces {len(r4["pieces"])}; '
          f'(a) {n_a} links, worst {mp.nstr(worst_a, 3)}; (b) {n_b} rejoinings, worst {mp.nstr(worst_b, 3)}; '
          f'(c) {n_c} re-readings, worst {mp.nstr(worst_c, 3)}')
    t4 &= agree and len(r4['pieces']) == len(r4['breaks']) + 1 and max(worst_a, worst_b, worst_c) < EXACT
ok['T4'] = t4

# ---------------------------------------------------------------- T6 (exact parts)
t6 = True
def area(X, t):
    cs = things[t][1]
    return norm(sub(X[cs[0]], X[cs[1]])) * norm(sub(X[cs[1]], X[cs[2]]))
def centre(X, t):
    cs = things[t][1]
    return mul(add(add(X[cs[0]], X[cs[1]]), add(X[cs[2]], X[cs[3]])), mp.mpf(1) / 4)
for k in (mp.mpf(1), mp.mpf('1e-3'), mp.mpf(7), mp.mpf('1e3')):
    rk = Readings(feats, stops, k=k); rs = build(rk); mk = full_map(rk, rs)
    T = {n: mul(p, k) for n, p in feats.items()}               # the referee, in metres at this k
    th = list(things)
    a_ok = all((area(mk, a) > area(mk, b)) == (area(T, a) > area(T, b)) for a, b in itertools.combinations(th, 2))
    # (b) routes between diagonal rooms, through the two door orders
    b_ok, nb = True, 0
    for r1, r2, via1, via2 in ((1, 4, ('D12', 'D24'), ('D13', 'D34')), (2, 3, ('D12', 'D13'), ('D24', 'D34'))):
        for ta in [t for t in th if things[t][0] == r1]:
            for tb in [t for t in th if things[t][0] == r2]:
                def rlen(X, via): pts = [centre(X, ta), X[via[0]], X[via[1]], centre(X, tb)]; return sum(norm(sub(pts[i + 1], pts[i])) for i in range(3))
                b_ok &= (rlen(mk, via1) < rlen(mk, via2)) == (rlen(T, via1) < rlen(T, via2)); nb += 1
    # (c) home from every stop, (d) steps (strides of H) to every thing from every stop
    c_err = max(abs(ang(sub(rs['P'][0], rs['P'][i])) - ang(sub(rk.truth_stops[0], rk.truth_stops[i]))) for i in range(1, len(stops)))
    d_err = max(abs(norm(sub(centre(mk, t), rs['P'][i])) - norm(sub(centre(T, t), mul(stops[i], k))) / rk.L0_m)
                for i in range(len(stops)) for t in th)
    # (e) seconds at 1.2 m/s with the first leg's metres carried in
    e_err = max(abs(norm(sub(centre(mk, t), rs['P'][0])) * rk.L0_m / mp.mpf('1.2') - norm(sub(centre(T, t), mul(stops[0], k))) / mp.mpf('1.2')) for t in th)
    print(f'T6 k = {mp.nstr(k, 3)}: (a) {len(th) * (len(th) - 1) // 2} pairs agree {a_ok}; (b) {nb} routes agree {b_ok}; '
          f'(c) home {mp.nstr(c_err, 3)}; (d) steps {mp.nstr(d_err, 3)}; (e) seconds with L0 carried {mp.nstr(e_err, 3)}')
    t6 &= a_ok and b_ok and max(c_err, d_err) < EXACT and e_err < EXACT * 1000
# (e) without the amount: the same readings at k = 1 and 7 (T2), the seconds 7 times apart: no function of the readings
r1 = Readings(feats, stops, k=1); r7 = Readings(feats, stops, k=7)
same_readings = all(norm(sub(r1.b[i][f], r7.b[i][f])) < mp.mpf(10) ** -45 for i in range(len(stops)) for f in r1.held[i])
print(f'T6 (e): readings at k = 1 and 7 identical {same_readings}, seconds 7 times apart: nullity 1 without an amount, 0 with L0 carried')
t6 &= same_readings
# (f) two readers
stopsB = make_walk(seed=5, n=20, box=((2, 2), (13, 7)))
rA, rB = rd, Readings(feats, stopsB)
resB = build(rB); mB = full_map(rB, resB)
common = sorted(set(mp_map) & set(mB))
tcommon = [t for t, (_, cs) in things.items() if cs[0] in common and cs[1] in common]
t = tcommon[0]; c0, c1 = things[t][1][0], things[t][1][1]
zA0, zA1 = mp.mpc(*mp_map[c0]), mp.mpc(*mp_map[c1]); zB0, zB1 = mp.mpc(*mB[c0]), mp.mpc(*mB[c1])
a = (zA1 - zA0) / (zB1 - zB0); bb = zA0 - a * zB0
f_err = max(abs(a * mp.mpc(*mB[f]) + bb - mp.mpc(*mp_map[f])) for f in common)
h_err = abs(abs(a) - rB.L0_m / rA.L0_m)
print(f'T6 (f): readers A ({len(stops)} stops) and B ({len(stopsB)} stops) share {len(common)} features; aligned by {t} '
      f'alone: other features {mp.nstr(f_err, 3)}; H_B/H_A read {mp.nstr(abs(a), 12)} against {mp.nstr(rB.L0_m / rA.L0_m, 12)} '
      f'({mp.nstr(h_err, 3)})')
# with nothing in common: B's world (its own copy) scaled by 7 leaves B's map as it was, so H_A/H_B is free
rB7 = Readings(feats, stopsB, k=7); mB7 = full_map(rB7, build(rB7))
free = maxdiff(mB7, mB, mB) < mp.mpf(10) ** -45 and abs(rB7.L0_m / rA.L0_m - rB.L0_m / rA.L0_m) > 1
print(f'T6 (f): nothing in common (B\'s own world scaled by 7): B\'s map unchanged {free}: the ratio of H\'s undetermined, nullity 1')
t6 &= f_err < EXACT and h_err < EXACT and free
ok['T6'] = t6

# ---------------------------------------------------------------- T5 (noise)
mp.mp.dps = 20
EPS, NW, W = 1e-3, 400, 4
E = []
for s in range(NW):
    rng = random.Random(1000 + s)
    rn = Readings(feats, stops, eps=EPS, rng=rng, extra=2)            # stops 32, 33 are stops 0, 1 again
    rr = build(rn, window=W)
    if rr['breaks']: print('T5: walk', s, 'broke at', rr['breaks']); continue
    E.append([float(mp.log(rr['L'][i] / rn.true_legs[i])) for i in range(rn.n - 1)])
def sd(xs): m = sum(xs) / len(xs); return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))
open_sd = [sd([e[i] for e in E]) for i in range(len(E[0]))]
xs = [math.log(i) for i in range(4, 17)]; ys = [math.log(open_sd[i]) for i in range(4, 17)]
mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
p = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
corr = [[e[i] - (i / 32) * e[32] for i in range(33)] for e in E]
mid_closed = sd([c[16] for c in corr])
r_mid, r_end = mid_closed / open_sd[16], mid_closed / open_sd[32]
print(f'T5: {len(E)} walks, eps {EPS}, rays kept {W} stops (an open chain); sd of the log scale at i = 4, 8, 16, 32: '
      + ', '.join(f'{open_sd[i]:.5f}' for i in (4, 8, 16, 32)))
print(f'T5: growth exponent p = {p:.3f} (4…16); closed at the loop, sd at i = 16 {mid_closed:.5f}: over the open chain there '
      f'{r_mid:.3f} (1/√2 = 0.707), over the open chain at its end {r_end:.3f} (0.5)')
ok['T5'] = abs(p - 0.5) <= 0.1 and abs(r_mid - 1 / math.sqrt(2)) <= 0.1 and abs(r_end - 0.5) <= 0.1

print()
for k in ('T1', 'T2', 'T3', 'T4', 'T5', 'T6'):
    print(k, 'not killed' if ok[k] else 'KILLED')
