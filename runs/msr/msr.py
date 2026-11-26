"""MSR run 1 (plans/msr-plan.md). Run from the repository's root, with the data folder as the argument:
python3 -I runs/msr/msr.py <folder with train-0.parquet, train-1.parquet, tide2025.csv>"""
import sys, math, csv, collections
import numpy as np
import pyarrow.parquet as pq

DATA = sys.argv[1]
src = open('runs/dbr/dbr.py').read().split('# ---------------------------------------------------------------- L2')[0]
g = {}; exec(src, g)
cheb, bary = g['cheb'], g['bary']
KS = [6, 8, 12, 16, 24, 32, 48, 64, 96, 128]
out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

def kstar(fun, lo, hi, tol, coord):
    """least K whose rebuild of fun over [lo, hi] is within tol; coord 'ratio' (y round c) or 'records'."""
    if coord == 'ratio':
        c = math.sqrt(lo * hi); Y = (hi / c - 1) / (hi / c + 1)
        toX = lambda u: c * (1 + Y * u) / (1 - Y * u)
    else:
        m, w = (lo + hi) / 2, (hi - lo) / 2
        toX = lambda u: m + w * u
    uq = np.linspace(-1, 1, 2000)
    fq = fun(toX(uq))
    for K in KS:
        z, w_ = cheb(K)
        p, _ = bary(z, w_, fun(toX(z)), uq)
        if np.abs(p - fq).max() <= tol:
            return K
    return None

def zipf_fun(counts):
    L = np.log10(np.asarray(counts, float))             # rank r = index + 1
    n = len(L); cs = np.concatenate([[0.0], np.cumsum(L)])
    r = np.arange(1, n + 1)
    lo = np.maximum(1, np.ceil(r / 1.02)).astype(int); hi = np.minimum(n, np.floor(r * 1.02)).astype(int)
    S = (cs[hi] - cs[lo - 1]) / (hi - lo + 1)              # mean log count over ranks within 2%
    lr = np.log(r)
    def f(x):
        return np.interp(np.log(x), lr, S)
    return f, n

def word_counts(files, frac=1.0):
    cnt = collections.Counter()
    for fpath in files:
        col = pq.read_table(fpath, columns=['text']).column('text').to_pylist()
        rows = col if frac == 1.0 else None
        yield_rows = col
        cnt_rows = yield_rows
        for line in cnt_rows:
            if line:
                cnt.update(line.split())
    return cnt

say('data:', DATA)
files = [f'{DATA}/train-0.parquet', f'{DATA}/train-1.parquet']
# the whole corpus
cnt = collections.Counter(); rows_all = []
for fpath in files:
    rows_all += pq.read_table(fpath, columns=['text']).column('text').to_pylist()
for line in rows_all:
    if line: cnt.update(line.split())
counts = sorted(cnt.values(), reverse=True)
say(f'WikiText-103 train: {len(rows_all)} rows, {sum(counts)} tokens, {len(counts)} distinct words; count at rank 10^5: {counts[99999]}')
quarter = collections.Counter()
for line in rows_all[:len(rows_all) // 4]:
    if line: quarter.update(line.split())
qcounts = sorted(quarter.values(), reverse=True)
say(f'first quarter: {sum(qcounts)} tokens, {len(qcounts)} distinct; count at rank 10^5: {qcounts[99999] if len(qcounts) > 99999 else None}')

fz, nz = zipf_fun(counts); fq, nq = zipf_fun(qcounts)
cents = [10 ** e for e in (1.5, 2, 2.5, 3, 3.5, 4, 4.5)]
kz = [kstar(fz, c / 4, 4 * c, 0.05, 'ratio') for c in cents]
kq = [kstar(fq, c / 4, 4 * c, 0.05, 'ratio') for c in cents]
say('Z1: K* in the ratio window, c = 10^1.5 … 10^4.5:', kz)
ok1 = all(k is not None for k in kz) and max(kz) / min(kz) <= 2
say('Z1', 'not killed' if ok1 else 'KILLED', '' if not all(k is not None for k in kz) else '(largest / smallest %.2f)' % (max(kz) / min(kz)))
say('Z2: K* for the first quarter:', kq)
ok2 = True
for a, b, c in zip(kz[:6], kq[:6], cents[:6]):
    ok2 &= a is not None and b is not None and abs(KS.index(a) - KS.index(b)) <= 1
say('Z2', 'not killed' if ok2 else 'KILLED')

# the tide
t, h = [], []
with open(f'{DATA}/tide2025.csv') as fh:
    rd = csv.reader(fh); next(rd)
    for i, row in enumerate(rd):
        try: h.append(float(row[1])); t.append(i)
        except ValueError: pass
t = np.array(t, float); h = np.array(h)
say(f'tide: {len(h)} hourly values of 8760 (gaps {8760 - len(h)}), {h.min():.3f} … {h.max():.3f} m')
ftide = lambda x: np.interp(x, t, h)
tc = [24, 96, 384, 1536, 6144]
kt = []
for c in tc:
    if 4 * c > t[-1]:
        kt.append('outside the record'); continue
    kt.append(kstar(ftide, c / 4, 4 * c, 0.02, 'ratio'))
say('T1: K* in the ratio window, c = 24, 96, 384, 1536, 6144 h:', kt)
ok3, prev = True, None
for k in kt:
    if k == 'outside the record':
        ok3 = False; break
    if k is None: break
    if prev is not None and k / prev < 2.5: ok3 = False; break
    prev = k
say('T1', 'not killed' if ok3 else 'KILLED')
kr = [kstar(ftide, c - 48, c + 48, 0.02, 'records') for c in tc]
say('T2: K* in the records window (half-width 48 h):', kr)
ok4 = all(k is not None for k in kr) and max(kr) / min(kr) <= 2
say('T2', 'not killed' if ok4 else 'KILLED')
open('runs/msr/msr-run1.txt', 'w').write('\n'.join(out) + '\n')
