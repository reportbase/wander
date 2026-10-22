"""LTR run 1, post hoc (not tests): where the SN Ia - FP loop fails, and rung (a)'s two calibrations.
Usage: python3 -I runs/ltr/ltr_posthoc.py path/to/table2.dat   (writes runs/ltr/ltr-run1-posthoc.txt)"""
import sys, math, statistics as st
sys.path.insert(0, "runs/ltr")
import ltr
out = []
def say(s): print(s); out.append(s)
rows = ltr.load(sys.argv[1])
g = [r for r in rows if "SNIa" in r and "FP" in r]
x = [r["x"] for r in g]
for lab in ["SNIa", "FP"]:
    b, se, _ = ltr.olsse(x, [r[lab] - r["x"] for r in g])
    say(f"overlap SNIa&FP (n {len(g)}): {lab} against the flow slope {b:+.4f} +- {se:.4f}")
for lab in ["SNIa", "FP"]:
    rest = [r for r in rows if lab in r and not ("SNIa" in r and "FP" in r)]
    b, se, _ = ltr.olsse([r["x"] for r in rest], [r[lab] - r["x"] for r in rest])
    say(f"{lab} outside the overlap (n {len(rest)}): slope {b:+.4f} +- {se:.4f}")
# FP's own slope by distance band: does its offset curve at its sample's far edge (selection)?
fp = [r for r in rows if "FP" in r]
for lo, hi in [(33, 35), (35, 36), (36, 37), (37, 38.5)]:
    d = [r["FP"] - r["x"] for r in fp if lo <= r["x"] < hi]
    say(f"FP - flow, mu_flow {lo}-{hi}: n {len(d):5d} mean {st.mean(d):+.3f}")
sn = [r for r in rows if "SNIa" in r]
for lo, hi in [(33, 35), (35, 36), (36, 37), (37, 38.5)]:
    d = [r["SNIa"] - r["x"] for r in sn if lo <= r["x"] < hi]
    say(f"SNIa - flow, mu_flow {lo}-{hi}: n {len(d):5d} mean {st.mean(d):+.3f}")
# Hubble rung (a) by calibration: Shapley's Clouds against Hubble's own three
H = ltr.HUB
for name, keys in [("Shapley's Clouds", ["SMC", "LMC"]), ("NGC 6822, M 33, M 31", ["N6822", "N598", "N224"])]:
    rr = [math.log2(H[k][2] / H[k][1]) for k in keys]
    say(f"rung (a), {name}: r mean {st.mean(rr):.3f}, values {', '.join(f'{v:.3f}' for v in rr)}")
b, se, _ = ltr.olsse([math.log2(H[k][2]) for k in ["N6822", "N598", "N224"]], [math.log2(H[k][1]) for k in ["N6822", "N598", "N224"]])
say(f"rung (a), Hubble's own three alone: slope {b:.3f} +- {se:.3f}")
open("runs/ltr/ltr-run1-posthoc.txt", "w").write("\n".join(out) + "\n")
