"""NAT (plans/nat-plan.md). Run from the repository's root: python3 runs/nat/nat.py"""
import json, os
import numpy as np
from scipy import integrate, stats
import torch

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nat-results.json")
torch.set_num_threads(4)


def part_a():
    res = {}
    for n in [2, 3, 4, 8, 16, 32, 64, 128]:
        f = lambda a: np.sin(a) ** (n - 2)
        share = integrate.quad(f, 0, np.pi / 4)[0] / integrate.quad(f, 0, np.pi / 2)[0]
        med = float(np.sqrt((n - 1) * stats.f.median(n - 1, 1))) if n > 1 else None
        # sd of cos alpha for uniform directions on the whole sphere: E[c^2] = 1/n exactly
        c2 = integrate.quad(lambda a: np.cos(a) ** 2 * np.sin(a) ** (n - 2), 0, np.pi)[0] / integrate.quad(lambda a: np.sin(a) ** (n - 2), 0, np.pi)[0]
        res[n] = {"share_in_corner": share, "median_slope": med, "median_over_sqrt": med / np.sqrt(n - 1),
                  "sd_cos_times_sqrt_n": float(np.sqrt(c2 * n))}
    shares = [res[n]["share_in_corner"] for n in res]
    c = 1 / stats.norm.ppf(0.75)
    v = {
        "A1": abs(res[2]["share_in_corner"] - 0.5) < 1e-9 and abs(res[3]["share_in_corner"] - (1 - 2 ** -0.5)) < 1e-9
        and all(x > y for x, y in zip(shares, shares[1:])) and res[16]["share_in_corner"] < 0.01,
        "A2": abs(res[2]["median_slope"] - 1) < 1e-9 and abs(res[3]["median_slope"] - 3 ** 0.5) < 1e-9
        and abs(res[64]["median_over_sqrt"] / c - 1) < 0.02,
        "A3": all(res[n]["median_slope"] > 1 for n in res if n >= 3),
        "A4": all(abs(res[n]["sd_cos_times_sqrt_n"] - 1) < 1e-9 for n in res),
    }
    return res, {k: ("not killed" if x else "KILLED") for k, x in v.items()}, c


N, DV, STEPS, BATCH, LR, SEEDS = 32, 16, 3000, 256, 3e-3, [0, 1, 2]
ARMS = ["nature", "read-3", "softmax-3", "softmax-mlp", "read-mlp"]


def unit(x): return x / x.norm(dim=-1, keepdim=True)


def world(n, g, nthings=N, k=1.0, dirs=None):
    if dirs is None:
        q = unit(torch.randn(n, 3, generator=g)); kd = unit(torch.randn(n, nthings, 3, generator=g))
        val = torch.randn(n, nthings, DV, generator=g)
    else:
        q, kd, val = dirs
    dist = 10 ** (2 * torch.rand(n, nthings, 1, generator=g))
    ans = (kd @ q[..., None]).squeeze(-1).argmax(-1)
    return q, kd * dist * k, val, ans, (q, kd, val)


def read(q, k, logH):
    qn = q / (q.norm(dim=-1, keepdim=True) + 1e-30)
    h = (qn * k).sum(-1); v2 = ((k * k).sum(-1) - h * h).clamp(min=0)
    w = h * h / (h * h + v2 / torch.exp(2 * logH) + 1e-300) * (h > 0)
    return w / (w.sum(-1, keepdim=True) + 1e-300)


class Model(torch.nn.Module):
    def __init__(self, arm):
        super().__init__(); self.arm = arm; d = 64 if "mlp" in arm else 3
        if "mlp" in arm:
            mk = lambda: torch.nn.Sequential(torch.nn.Linear(3, 64), torch.nn.ReLU(), torch.nn.Linear(64, 64))
            self.eq, self.ek = mk(), mk()
        self.Wq = torch.nn.Linear(d, d, bias=False); self.Wk = torch.nn.Linear(d, d, bias=False)
        self.s = torch.nn.Parameter(torch.tensor(0.0))

    def weights(self, q, k):
        if self.arm == "nature":
            return read(q[:, None, :], k, torch.tensor(0.0, dtype=k.dtype))
        if "mlp" in self.arm: q, k = self.eq(q), self.ek(k)
        q = self.Wq(q)[:, None, :]; k = self.Wk(k)
        if self.arm.startswith("softmax"):
            return torch.softmax(torch.exp(self.s) * (q * k).sum(-1), -1)
        return read(q, k, self.s)

    def forward(self, q, k, val):
        w = self.weights(q, k); return (w[..., None] * val).sum(1), w


def evaluate(m, seed, curve=False):
    gt = torch.Generator().manual_seed(9000 + seed)
    with torch.no_grad():
        q, k, val, ans, dirs = world(20000, gt)
        out, preds = {}, {}
        for name, kk in [("train", 1.0), ("x1e3", 1e3), ("x1e-3", 1e-3)]:
            g2 = torch.Generator().manual_seed(5000 + seed)
            q2, k2, v2, a2, _ = world(20000, g2, k=kk, dirs=dirs)
            p = m(q2.double(), k2.double(), v2.double())[1].argmax(-1) if m.arm == "nature" else m(q2, k2, v2)[1].argmax(-1)
            preds[name] = p; out[name] = float((p == a2).double().mean())
        if not curve:
            q3, k3, v3, a3, _ = world(5000, torch.Generator().manual_seed(7000 + seed), nthings=1024)
            p = m(q3.double(), k3.double(), v3.double())[1].argmax(-1) if m.arm == "nature" else m(q3, k3, v3)[1].argmax(-1)
            out["n1024"] = float((p == a3).double().mean())
            out["same_under_scale"] = bool((preds["x1e3"] == preds["train"]).all() and (preds["x1e-3"] == preds["train"]).all())
    return out


def run(arm, seed):
    torch.manual_seed(seed); g = torch.Generator().manual_seed(1000 + seed)
    m = Model(arm); curve = []
    params = sum(p.numel() for p in m.parameters()) if arm != "nature" else 0
    if arm != "nature":
        opt = torch.optim.Adam(m.parameters(), lr=LR)
        for step in range(1, STEPS + 1):
            q, k, val, ans, _ = world(BATCH, g)
            out, _ = m(q, k, val)
            loss = ((out - val[torch.arange(BATCH), ans]) ** 2).mean()
            opt.zero_grad(); loss.backward(); opt.step()
            if step % 250 == 0: curve.append([step, evaluate(m, seed, curve=True)["train"]])
    r = evaluate(m, seed); r["params"] = params; r["curve"] = curve
    print(arm, seed, {x: r[x] for x in r if x != "curve"}, flush=True)
    return r


def main():
    a, va, c = part_a()
    print(json.dumps(a, indent=1)); print(va)
    out = {"partA": {str(n): x for n, x in a.items()}, "partA_limit": c, "verdictsA": va}
    b = {arm: {str(s): run(arm, s) for s in SEEDS} for arm in ARMS}
    mean = lambda arm, t: float(np.mean([b[arm][str(s)][t] for s in SEEDS]))
    tests = ["train", "x1e3", "x1e-3", "n1024"]
    means = {arm: {t: mean(arm, t) for t in tests} for arm in ARMS}
    v = {}
    v["B1"] = all(means["nature"][t] == 1.0 for t in tests)
    v["B2"] = all(b[arm][str(s)]["same_under_scale"] for arm in ("softmax-3", "read-3") for s in SEEDS)
    v["B3"] = means["softmax-mlp"]["train"] - means["softmax-mlp"]["x1e3"] >= 0.20
    v["B4"] = means["nature"]["train"] - means["softmax-3"]["train"] >= 0.20
    v["B5"] = means["nature"]["n1024"] - means["softmax-mlp"]["n1024"] >= 0.20
    v["B6"] = all(means[arm]["train"] < 0.98 for arm in ARMS if arm != "nature")
    out.update({"partB": b, "meansB": means, "verdictsB": {k: ("not killed" if x else "KILLED") for k, x in v.items()}})
    json.dump(out, open(OUT, "w"), indent=1)
    print(json.dumps(means, indent=1)); print(out["verdictsB"])


if __name__ == "__main__":
    main()
