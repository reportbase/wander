"""GPA run 2: run 1's post hoc measures as predictions H1-H5, on GPT-2 small and medium, two new texts.
Inference only. python3 runs/gpa/gpa2.py   (book at ~/data/gpa/pp.txt, Project Gutenberg 1342)"""
import json, os, re
import numpy as np, torch
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
from datasets import load_dataset
torch.set_num_threads(4)
NB, T, TMIN, DMAX, DH = 20, 256, 8, 128, 64

def texts():
    wt = "\n\n".join(load_dataset("Salesforce/wikitext", "wikitext-2-raw-v1")["test"]["text"])
    raw = open(os.path.expanduser("~/data/gpa/pp.txt"), encoding="utf-8").read()
    book = raw.split("*** START OF THE PROJECT GUTENBERG EBOOK 1342 ***")[1].split("*** END OF THE PROJECT GUTENBERG EBOOK 1342 ***")[0]
    return {"wikitext-test": wt, "pride-and-prejudice": book}

def pr(C):
    ev = np.linalg.eigvalsh(C); return float(ev.sum() ** 2 / (ev ** 2).sum())

def cell(name, text):
    tok = GPT2TokenizerFast.from_pretrained(name)
    model = GPT2LMHeadModel.from_pretrained(name, attn_implementation="eager").eval()
    L, NH, D = model.config.n_layer, model.config.n_head, model.config.n_embd
    ids = tok(text, return_tensors="pt").input_ids[0]
    assert len(ids) >= (NB + 1) * T, (name, len(ids))
    qk = {}
    for l, blk in enumerate(model.transformer.h):
        def f(mod, inp, out, l=l):
            q, k, _ = out.split(D, dim=-1)
            qk[l] = (q[0].view(T, NH, DH).transpose(0, 1), k[0].view(T, NH, DH).transpose(0, 1))
        blk.attn.c_attn.register_forward_hook(f)
    msk = torch.tril(torch.ones(T, T, dtype=torch.bool))[TMIN:, 1:]
    cnt = msk.sum(-1).float()
    bw = np.zeros((L, NH)); bn = np.zeros((L, NH)); sink = np.zeros((L, NH))
    M = np.zeros((L, NH, DH, DH)); S1 = np.zeros((L, NH, DH)); n = 0; nq = 0
    dist = np.zeros(DMAX + 1); dist_n = np.zeros(DMAX + 1)
    rows = torch.arange(TMIN, T)
    with torch.no_grad():
        for i in range(1, NB + 1):                      # the first block skipped
            out = model(ids[i * T:(i + 1) * T][None], output_attentions=True)
            for l in range(L):
                q, k = qk[l]
                A = out.attentions[l][0]
                sink[l] += A[:, TMIN:, 0].sum(-1).numpy()
                W = A[:, TMIN:, 1:] * msk; W = W / W.sum(-1, keepdim=True)
                s = (q @ k.transpose(1, 2))[:, TMIN:, 1:]
                mean = (s * msk).sum(-1, keepdim=True) / cnt[:, None]
                below = (s <= mean) & msk
                bw[l] += (W * below).sum(-1).sum(-1).numpy(); bn[l] += (below.sum(-1) / cnt).sum(-1).numpy()
                kk = k.numpy(); M[l] += np.einsum("hti,htj->hij", kk, kk); S1[l] += kk.sum(1)
                for d in range(1, DMAX + 1):
                    cols = rows - d; ok = cols >= 1
                    vals = W[:, (rows - TMIN)[ok], cols[ok] - 1]
                    dist[d] += vals.sum().item(); dist_n[d] += vals.numel()
            n += T; nq += T - TMIN
    bw /= nq; bn /= nq; sink /= nq
    prc = np.array([[pr(M[l, h] / n - np.outer(S1[l, h] / n, S1[l, h] / n)) for h in range(NH)] for l in range(L)])
    pru = np.array([[pr(M[l, h] / n) for h in range(NH)] for l in range(L)])
    dist = dist[1:] / dist_n[1:]; d = np.arange(1, DMAX + 1)
    def slope(lo, hi):
        m = (d >= lo) & (d <= hi); return float(np.polyfit(np.log(d[m]), np.log(dist[m]), 1)[0])
    s1, s2 = slope(1, 8), slope(16, 128)
    r = {"layers": L, "heads": NH, "tokens": int(len(ids)),
         "below_weight_median": float(np.median(bw)), "below_count_median": float(np.median(bn)),
         "below_weight_by_layer": bw.mean(1).tolist(),
         "pr_centred_median": float(np.median(prc)), "pr_uncentred_median": float(np.median(pru)),
         "pr_centred_by_layer": np.median(prc, 1).tolist(),
         "sink_median": float(np.median(sink)), "slope_1_8": s1, "slope_16_128": s2}
    r["H1"] = 0.02 <= r["below_weight_median"] <= 0.10 and 0.40 <= r["below_count_median"] <= 0.60
    r["H2"] = 6 <= r["pr_centred_median"] <= 24
    r["H3"] = r["pr_uncentred_median"] < r["pr_centred_median"]
    r["H4"] = r["sink_median"] >= 0.30
    r["H5"] = abs(s1 - s2) < 0.5
    return r

if __name__ == "__main__":
    tx = texts(); res = {}
    for name in ("gpt2", "openai-community/gpt2-medium"):
        for tn, t in tx.items():
            key = f"{name.split('/')[-1]} / {tn}"
            res[key] = cell(name, t)
            print(key, {k: v for k, v in res[key].items() if not k.endswith("by_layer")}, flush=True)
    res["verdicts"] = {h: all(res[c][h] for c in res if c != "verdicts") for h in ("H1", "H2", "H3", "H4", "H5")}
    json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gpa2-results.json"), "w"), indent=1)
    print(json.dumps(res["verdicts"]))
