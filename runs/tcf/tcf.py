"""TCF run 1: fit Clark's 2Dt to Bullock et al. (2017)'s raw seed-dispersal kernels and test T1 and T5.

The rule this follows (the kernels that count, the fit, the slope) is in plans/tcf-plan.md, "Before run 1", and was
written before any kernel value was read.

    python3 -I runs/tcf/tcf.py <Plantdispersaldata.csv> <vectors.tsv>     # the run
    python3 -I runs/tcf/tcf.py --selftest                                 # synthetic kernels only, no data

The data are not committed (Dryad doi:10.5061/dryad.mq2ff, CC0; sha256s in the plan).
"""
import csv
import math
import sys

import numpy as np
from scipy.optimize import least_squares

P_LO, P_HI = 0.02, 50.0


def model(theta, r):
    """log rho(r) for theta = (log A, log u, log p)."""
    logA, logu, logp = theta
    p = math.exp(logp)
    return logA - (p + 1.0) * np.log1p(r * r / math.exp(logu))


def fit2dt(r, rho):
    """Unweighted least squares on log rho over (log A, log u, log p), within the plan's bounds, from a grid of starts."""
    r = np.asarray(r, float)
    y = np.log(np.asarray(rho, float))
    rmax = float(r.max())
    u_lo, u_hi = 1e-6 * rmax ** 2, 1e4 * rmax ** 2
    lo = [-np.inf, math.log(u_lo), math.log(P_LO)]
    hi = [np.inf, math.log(u_hi), math.log(P_HI)]
    best = None
    for p0 in (0.1, 0.5, 2.0, 10.0):
        for f in (1e-3, 1e-2, 0.1, 1.0, 10.0):
            u0 = f * rmax ** 2
            A0 = float(np.max(y + (p0 + 1.0) * np.log1p(r * r / u0)))
            x0 = [A0, math.log(u0), math.log(p0)]
            res = least_squares(lambda t: model(t, r) - y, x0, bounds=(lo, hi), method='trf')
            if best is None or res.cost < best.cost:
                best = res
    logA, logu, logp = best.x
    p, u = math.exp(logp), math.exp(logu)
    tol = 1e-3
    on_bound = (abs(logp - lo[2]) < tol or abs(logp - hi[2]) < tol or
                abs(logu - lo[1]) < tol or abs(logu - hi[1]) < tol)
    return {'p': p, 'u': u, 'cost': best.cost, 'on_bound': on_bound, 'n': len(r), 'rmax': rmax}


def tail_slope(r, rho, u):
    """The slope of log rho on log r over the points with r >= 2*sqrt(u); None with fewer than 3 such points."""
    r = np.asarray(r, float)
    rho = np.asarray(rho, float)
    keep = r >= 2.0 * math.sqrt(u)
    if keep.sum() < 3 or len(set(r[keep])) < 3:
        return None
    return float(np.polyfit(np.log(r[keep]), np.log(rho[keep]), 1)[0])


def read_kernels(path):
    """{dataset: {'species', 'source', 'r': [...], 'rho': [...], 'zeros': n, 'kind'}} from Dryad's wide CSV."""
    rows = list(csv.reader(open(path, encoding='latin-1')))[1:]
    out, cur, pending = {}, None, None
    for row in rows:
        if row[0].strip():
            cur = row[0].strip()
            out[cur] = {'species': row[1].strip(), 'source': row[2].strip(), 'r': [], 'rho': [], 'zeros': 0,
                        'dist_rows': 0, 'dens_rows': 0}
            pending = None
        label = row[3].strip()
        vals = row[4:]
        if label.startswith('Distance'):
            out[cur]['dist_rows'] += 1
            pending = vals
        elif label.startswith('Density'):
            out[cur]['dens_rows'] += 1
            for d, x in zip(pending, vals):
                d, x = d.strip(), x.strip()
                if not d or not x:
                    continue
                d, x = float(d), float(x)
                if x > 0:
                    out[cur]['r'].append(d)
                    out[cur]['rho'].append(x)
                else:
                    out[cur]['zeros'] += 1
    for k in out.values():
        k['kind'] = 'individual distances' if k['dens_rows'] == 0 else 'density'
    return out


def read_vectors(path):
    v = {}
    for line in open(path, encoding='utf-8'):
        f = line.rstrip('\n').split('\t')
        if len(f) < 4 or not f[0].strip().isdigit():
            continue
        v[f[0].strip()] = (f[2].strip().lower(), f[3].strip().lower())
    return v


def selftest():
    """Synthetic kernels with known (p, u), fitted by the same code: the fit returns them, and the slope reads -2(p+1)."""
    rng = np.random.default_rng(7)
    ok = True
    for p, u in ((0.5, 4.0), (0.5, 100.0), (1.5, 1.0), (0.2, 25.0)):
        r = np.geomspace(0.1 * math.sqrt(u), 30 * math.sqrt(u), 14)
        rho = 3.0 * (1 + r * r / u) ** (-(p + 1)) * np.exp(rng.normal(0, 0.05, r.size))
        f = fit2dt(r, rho)
        s = tail_slope(r, rho, f['u'])
        good = abs(f['p'] - p) / p < 0.15 and abs(math.sqrt(f['u']) - math.sqrt(u)) / math.sqrt(u) < 0.15
        ok &= good
        print(f"  p {p} -> {f['p']:.3f}, sqrt(u) {math.sqrt(u):.2f} -> {math.sqrt(f['u']):.2f}, "
              f"tail slope {s:.2f} (exact -2(p+1) = {-2 * (p + 1):.1f} far out), {'ok' if good else 'MISSED'}")
    print('selftest', 'passed' if ok else 'FAILED')
    return ok


def main(csv_path, vec_path):
    K = read_kernels(csv_path)
    V = read_vectors(vec_path)
    rows = []
    for ds, k in sorted(K.items(), key=lambda kv: int(kv[0])):
        vec, conf = V.get(ds, ('missing', ''))
        rec = {'ds': ds, 'species': k['species'], 'vector': vec, 'conf': conf, 'zeros': k['zeros'], 'kind': k['kind']}
        if k['kind'] != 'density' or len(set(k['r'])) < 4:
            rec['why'] = 'no density rows' if k['kind'] != 'density' else 'fewer than 4 distances with density > 0'
            rows.append(rec)
            continue
        f = fit2dt(k['r'], k['rho'])
        rec.update(f)
        rec['slope'] = tail_slope(k['r'], k['rho'], f['u'])
        rows.append(rec)

    def report(name, sel):
        fits = [x for x in sel if 'p' in x]
        ps = np.array([x['p'] for x in fits])
        print(f"\n{name}: {len(sel)} kernels, {len(fits)} fitted, {sum(x.get('on_bound', False) for x in fits)} on a bound")
        if not len(ps):
            return None, None
        med = float(np.median(ps))
        out = float(np.mean((ps < 0.15) | (ps > 1.5)))
        q = np.percentile(ps, [25, 75])
        sl = [x['slope'] for x in fits if x.get('slope') is not None]
        msl = float(np.median(sl)) if sl else None
        print(f"  p: median {med:.3f}, quartiles {q[0]:.3f} {q[1]:.3f}, share outside [0.15, 1.5] {out:.3f}")
        print(f"  tail slope (r >= 2 sqrt u): {len(sl)} kernels, median {msl if msl is None else round(msl, 3)}")
        return med, out, msl

    primary = [x for x in rows if x['vector'] == 'wind' and x['conf'] in ('high', 'medium')]
    print('\n== PRIMARY: wind, high or medium confidence ==')
    for x in primary:
        if 'p' in x:
            s = 'none' if x['slope'] is None else f"{x['slope']:.2f}"
            print(f"  {x['ds']:>4} {x['species'][:34]:34} n {x['n']:>3} rmax {x['rmax']:8.2f} p {x['p']:7.3f} "
                  f"sqrt(u) {math.sqrt(x['u']):8.3f} slope {s}{'  [on bound]' if x['on_bound'] else ''}")
        else:
            print(f"  {x['ds']:>4} {x['species'][:34]:34} not fitted: {x['why']}")
    med, out, msl = report('PRIMARY', primary)
    print('\n== VERDICTS (primary set) ==')
    t1 = med is not None and 0.3 <= med <= 0.8 and out < 1 / 3
    print(f"  T1: median p {med:.3f} in [0.3, 0.8]? {0.3 <= med <= 0.8}; share outside [0.15, 1.5] {out:.3f} < 1/3? "
          f"{out < 1 / 3} -> {'not killed' if t1 else 'KILLED'}")
    if msl is None:
        print('  T5: no kernel had 3 points past 2 sqrt(u): not testable')
    else:
        t5 = -3.6 <= msl <= -2.4
        print(f"  T5: median tail slope {msl:.3f} in [-3.6, -2.4]? -> {'not killed' if t5 else 'KILLED'}")
    print('  T2, T3, T4: untested (no heights in the file)')

    print('\n== reported beside it, deciding nothing ==')
    for vec in ('wind', 'gravity', 'ballistic', 'animal', 'water', 'human/machine', 'unsure'):
        sel = [x for x in rows if x['vector'] == vec and not (vec == 'wind' and x['conf'] in ('high', 'medium'))]
        if sel:
            report(f"{vec}{' (low confidence)' if vec == 'wind' else ''}", sel)
    print(f"\nall: {len(rows)} datasets, {sum('p' in x for x in rows)} fitted; "
          f"zeros dropped {sum(x['zeros'] for x in rows)}; "
          f"not fitted: {[(x['ds'], x['why']) for x in rows if 'why' in x]}")


if __name__ == '__main__':
    if sys.argv[1:] == ['--selftest']:
        sys.exit(0 if selftest() else 1)
    main(sys.argv[1], sys.argv[2])
