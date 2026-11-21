"""SCT: the scale test on a small learner (plans/sct-plan.md). Run from the repository's root: python3 runs/sct/sct.py"""
import json, math, os
import numpy as np
import torch

torch.set_num_threads(4)
D, N, STEPS, BATCH, LR, A_TRAIN = 16, 32, 4000, 256, 3e-3, 0.5
TESTS, NTEST, SEEDS = [0.5, 1.5, 3.0], 20000, [0, 1, 2, 3, 4]
ARMS = ["softmax", "cauchy-amount", "read-front", "read-both"]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sct-results.json")


def unit(x): return x / x.norm(dim=-1, keepdim=True)


def task(n, a, g, dirs=None):
    """Directions (optionally given), lengths e^U, U ~ (−a, a); answer = key of largest cosine."""
    if dirs is None:
        qd = unit(torch.randn(n, D, generator=g)); kd = unit(torch.randn(n, N, D, generator=g))
        val = torch.randn(n, N, D, generator=g)
    else:
        qd, kd, val = dirs
    lq = torch.exp((torch.rand(n, 1, generator=g) * 2 - 1) * a)
    lk = torch.exp((torch.rand(n, N, 1, generator=g) * 2 - 1) * a)
    ans = (kd @ qd[..., None]).squeeze(-1).argmax(-1)
    return qd * lq, kd * lk, val, ans, (qd, kd, val)


class Model(torch.nn.Module):
    def __init__(self, arm):
        super().__init__()
        self.arm = arm
        self.Wq = torch.nn.Linear(D, D, bias=False); self.Wk = torch.nn.Linear(D, D, bias=False)
        self.s = torch.nn.Parameter(torch.tensor(0.0))  # log of beta, gamma or H

    def weights(self, q, k):
        q = self.Wq(q)[:, None, :]; k = self.Wk(k)
        if self.arm == "softmax":
            return torch.softmax(torch.exp(self.s) * (q * k).sum(-1), -1)
        if self.arm == "cauchy-amount":
            w = 1 / (1 + ((q - k) ** 2).sum(-1) / torch.exp(2 * self.s))
        else:
            qn = q / (q.norm(dim=-1, keepdim=True) + 1e-12)
            h = (qn * k).sum(-1); v2 = ((k * k).sum(-1) - h * h).clamp(min=0)
            w = h * h / (h * h + v2 / torch.exp(2 * self.s) + 1e-12)
            if self.arm == "read-front": w = w * (h > 0)
        return w / (w.sum(-1, keepdim=True) + 1e-12)

    def forward(self, q, k, val):
        w = self.weights(q, k)
        return (w[..., None] * val).sum(1), w


def run(arm, seed):
    torch.manual_seed(seed); g = torch.Generator().manual_seed(1000 + seed)
    m = Model(arm); opt = torch.optim.Adam(m.parameters(), lr=LR)
    for _ in range(STEPS):
        q, k, val, ans, _ = task(BATCH, A_TRAIN, g)
        out, _ = m(q, k, val)
        loss = ((out - val[torch.arange(BATCH), ans]) ** 2).mean()
        opt.zero_grad(); loss.backward(); opt.step()
    gt = torch.Generator().manual_seed(9000 + seed)
    with torch.no_grad():
        base = task(NTEST, A_TRAIN, gt)
        dirs = base[4]
        res, preds = {}, {}
        for a in TESTS:
            q, k, val, ans, _ = task(NTEST, a, torch.Generator().manual_seed(int(5000 + 100 * a + seed)), dirs)
            _, w = m(q, k, val)
            p = w.argmax(-1); preds[a] = p
            res[str(a)] = float((p == ans).double().mean())
        res["same_preds"] = all(bool((preds[a] == preds[TESTS[0]]).all()) for a in TESTS)
    print(arm, seed, res, flush=True)
    return res


def main():
    out = {arm: {str(s): run(arm, s) for s in SEEDS} for arm in ARMS}
    mean = lambda arm, a: float(np.mean([out[arm][str(s)][str(a)] for s in SEEDS]))
    v = {}
    v["S1"] = "not killed" if all(out[a][str(s)]["same_preds"] for a in ("read-front", "read-both") for s in SEEDS) else "KILLED"
    d2 = mean("softmax", 0.5) - mean("softmax", 3.0); v["S2"] = ["not killed" if d2 >= 0.10 else "KILLED", d2]
    d3 = mean("cauchy-amount", 0.5) - mean("cauchy-amount", 3.0); v["S3"] = ["not killed" if d3 >= 0.10 else "KILLED", d3]
    d4 = mean("read-front", 0.5) - mean("softmax", 0.5); v["S4"] = ["not killed" if d4 >= -0.05 else "KILLED", d4]
    out["means"] = {arm: {str(a): mean(arm, a) for a in TESTS} for arm in ARMS}
    out["verdicts"] = v
    json.dump(out, open(OUT, "w"), indent=1)
    print(json.dumps(out["means"], indent=1)); print(json.dumps(v, indent=1))


if __name__ == "__main__":
    main()
