"""GPA (plans/gpa-plan.md): GPT-2 small's attention read, forward only. Run from the repository's root:
python3 runs/gpa/gpa.py"""
import json, os
import numpy as np
import torch
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
from datasets import load_dataset

torch.set_num_threads(4)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gpa-results.json")
NB, T, L, NH, DH, DMAX, TMIN = 40, 256, 12, 12, 64, 128, 8

tok = GPT2TokenizerFast.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2", attn_implementation="eager").eval()
text = "\n\n".join(load_dataset("Salesforce/wikitext", "wikitext-2-raw-v1")["validation"]["text"])
ids = tok(text, return_tensors="pt").input_ids[0]
blocks = [ids[i * T:(i + 1) * T] for i in range(NB)]

qk = {}
def hook(layer):
    def f(mod, inp, out):
        q, k, _ = out.split(768, dim=-1)
        qk[layer] = (q[0].view(T, NH, DH).transpose(0, 1), k[0].view(T, NH, DH).transpose(0, 1))
    return f
for l, blk in enumerate(model.transformer.h):
    blk.attn.c_attn.register_forward_hook(hook(l))

back_w = np.zeros((L, NH)); back_n = np.zeros((L, NH)); front_w = np.zeros((L, NH)); front_n = np.zeros((L, NH))
sink = np.zeros((L, NH)); nq = 0
g0_ok = np.ones((L, NH), bool)
dist = np.zeros(DMAX + 1); dist_n = np.zeros(DMAX + 1)
M2k = np.zeros((L, NH, DH, DH)); M2q = np.zeros((L, NH, DH, DH)); ntok = 0
causal = torch.tril(torch.ones(T, T, dtype=torch.bool))
with torch.no_grad():
    for b in blocks:
        out = model(b[None], output_attentions=True)
        ntok += T
        for l in range(L):
            q, k = qk[l]
            A = out.attentions[l][0]                              # NH, T, T
            s = q @ k.transpose(1, 2)                             # raw q·k
            M2k[l] += np.einsum("hti,htj->hij", k.numpy(), k.numpy())
            M2q[l] += np.einsum("hti,htj->hij", q.numpy(), q.numpy())
            sink[l] += A[:, TMIN:, 0].sum(-1).numpy()
            W = A[:, TMIN:, 1:].clone()                           # leave key 0 out
            msk = causal[TMIN:, 1:]
            W = W * msk; W = W / W.sum(-1, keepdim=True)
            S = s[:, TMIN:, 1:]
            back = (S <= 0) & msk; front = (S > 0) & msk
            bw = (W * back).sum(-1); fw = (W * front).sum(-1)
            cnt = msk.sum(-1).float()
            bn = back.sum(-1) / cnt; fn = front.sum(-1) / cnt
            back_w[l] += bw.sum(-1).numpy(); back_n[l] += bn.sum(-1).numpy()
            front_w[l] += fw.sum(-1).numpy(); front_n[l] += fn.sum(-1).numpy()
            g0_ok[l] &= ((fw - fn) >= -1e-6).all(-1).numpy()
            for d in range(1, DMAX + 1):
                rows = torch.arange(TMIN, T); cols = rows - d
                ok = cols >= 1
                vals = W[:, (rows - TMIN)[ok], (cols[ok] - 1)]
                dist[d] += vals.sum().item(); dist_n[d] += vals.numel()
        nq += T - TMIN
back_w /= nq; back_n /= nq; front_w /= nq; front_n /= nq; sink /= nq
dist = dist[1:] / dist_n[1:]
def pr(M):
    ev = np.linalg.eigvalsh(M)
    return (ev.sum() ** 2) / (ev ** 2).sum()
prk = np.array([[pr(M2k[l, h]) for h in range(NH)] for l in range(L)])
prq = np.array([[pr(M2q[l, h]) for h in range(NH)] for l in range(L)])
def slope(lo, hi):
    d = np.arange(1, DMAX + 1); m = (d >= lo) & (d <= hi)
    return float(np.polyfit(np.log(d[m]), np.log(dist[m]), 1)[0])
s1, s2 = slope(1, 8), slope(16, 128)
v = {"G0": bool(g0_ok.all()), "G1": float(np.median(back_w)) < 0.10, "G2": float(np.median(prk)) <= 8,
     "G3": (s2 - s1) >= 0.5, "G4": float(np.median(sink)) >= 0.30}
res = {"tokens": int(ntok), "queries_per_head": int(nq),
       "back_weight_median": float(np.median(back_w)), "back_weight_mean": float(back_w.mean()),
       "back_count_median": float(np.median(back_n)), "back_weight_by_layer": back_w.mean(1).tolist(),
       "back_weight": back_w.tolist(), "back_count": back_n.tolist(),
       "pr_keys_median": float(np.median(prk)), "pr_queries_median": float(np.median(prq)),
       "pr_keys_by_layer": np.median(prk, 1).tolist(), "pr_keys": prk.tolist(), "pr_queries": prq.tolist(),
       "sink_median": float(np.median(sink)), "sink_by_layer": sink.mean(1).tolist(),
       "slope_1_8": s1, "slope_16_128": s2, "dist": dist.tolist(),
       "verdicts": {k: ("not killed" if x else "KILLED") for k, x in v.items()}}
json.dump(res, open(OUT, "w"), indent=1)
print(json.dumps({k: res[k] for k in res if k not in ("back_weight", "back_count", "pr_keys", "pr_queries", "dist")}, indent=1))
