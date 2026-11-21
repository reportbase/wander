"""GPA post hoc (not a prediction): back share with each query's logits centred on their mean over its keys, and the
keys' participation ratio after centring. python3 runs/gpa/gpa_posthoc.py"""
import json, os
import numpy as np, torch
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
from datasets import load_dataset
torch.set_num_threads(4)
NB, T, L, NH, DH, TMIN = 20, 256, 12, 12, 64, 8
tok = GPT2TokenizerFast.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2", attn_implementation="eager").eval()
text = "\n\n".join(load_dataset("Salesforce/wikitext", "wikitext-2-raw-v1")["validation"]["text"])
ids = tok(text, return_tensors="pt").input_ids[0]
qk = {}
for l, blk in enumerate(model.transformer.h):
    def f(mod, inp, out, l=l):
        q, k, _ = out.split(768, dim=-1)
        qk[l] = (q[0].view(T, NH, DH).transpose(0, 1), k[0].view(T, NH, DH).transpose(0, 1))
    blk.attn.c_attn.register_forward_hook(f)
causal = torch.tril(torch.ones(T, T, dtype=torch.bool))[TMIN:, 1:]
bw = np.zeros((L, NH)); bn = np.zeros((L, NH)); M = np.zeros((L, NH, DH, DH)); S1 = np.zeros((L, NH, DH)); n = 0; nq = 0
with torch.no_grad():
    for i in range(NB):
        out = model(ids[i * T:(i + 1) * T][None], output_attentions=True)
        for l in range(L):
            q, k = qk[l]
            W = out.attentions[l][0][:, TMIN:, 1:] * causal; W = W / W.sum(-1, keepdim=True)
            s = (q @ k.transpose(1, 2))[:, TMIN:, 1:]
            mean = (s * causal).sum(-1, keepdim=True) / causal.sum(-1, keepdim=True)
            back = (s <= mean) & causal
            bw[l] += (W * back).sum(-1).sum(-1).numpy(); bn[l] += (back.sum(-1) / causal.sum(-1)).sum(-1).numpy()
            kk = k.numpy(); M[l] += np.einsum("hti,htj->hij", kk, kk); S1[l] += kk.sum(1)
        n += T; nq += T - TMIN
bw /= nq; bn /= nq
def pr(C):
    ev = np.linalg.eigvalsh(C); return float(ev.sum() ** 2 / (ev ** 2).sum())
prc = np.array([[pr(M[l, h] / n - np.outer(S1[l, h] / n, S1[l, h] / n)) for h in range(NH)] for l in range(L)])
r = {"back_weight_centred_median": float(np.median(bw)), "back_count_centred_median": float(np.median(bn)),
     "back_weight_centred_by_layer": bw.mean(1).tolist(), "pr_keys_centred_median": float(np.median(prc)),
     "pr_keys_centred_by_layer": np.median(prc, 1).tolist()}
json.dump(r, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gpa-posthoc.json"), "w"), indent=1)
print(json.dumps(r, indent=1))
