"""DVJ step 1-2 (plans/dvj-plan.md): fetch ten Wikipedia articles' wikitext, record revision id and sha256,
and pull every <math> or {{math|...}} block carrying pi or e in any form into runs/dvj/candidates.md.
Wikitext saved to the directory given as argv[1] (not committed). Run from the repository root."""
import hashlib, json, os, re, sys, urllib.request, urllib.parse, urllib.error
PAGES = ["Law of cosines", "Spherical trigonometry", "Rotation (mathematics)", "Cylindrical coordinate system",
         "Euler's formula", "Conic section", "Parabola", "Elliptic orbit", "Mohr's circle", "Ellipsometry"]
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
UA = {"User-Agent": "research-script/1.0"}
import time
def get(url):
    for k in range(6):
        try:
            time.sleep(2)
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA)).read()
        except urllib.error.HTTPError as e:
            if e.code != 429: raise
            time.sleep(30 * (k + 1))
    raise RuntimeError("rate limited: " + url)
PAT = re.compile(r"\\pi\b|π|e\^|\\mathrm\{e\}\^|\\exp\b|\\ln\b|\\log\b|\\(?:arc)?(?:sin|cos|tan|cot|sec|csc)h?\b"
                 r"|\\operatorname\{(?:arc)?(?:sin|cos|tan|cot|sec|csc|exp|ln|log)h?\}|\bexp\(|\bln\(|\b(?:sin|cos|tan|sinh|cosh|tanh)\b")
rows, meta = [], []
titles = "|".join(p.replace(" ", "_") for p in PAGES)
info = json.loads(get("https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=ids|timestamp&format=json&titles="
                      + urllib.parse.quote(titles, safe="|")))
norm = {n["to"]: n["from"] for n in info["query"].get("normalized", [])}
revs = {}
for pg in info["query"]["pages"].values():
    revs[norm.get(pg["title"], pg["title"]).replace("_", " ")] = pg["revisions"][0]
for p in PAGES:
    t = urllib.parse.quote(p.replace(" ", "_"))
    path = os.path.join(out, p.replace(" ", "_") + ".wiki")
    if os.path.exists(path): raw = open(path, "rb").read()
    else:
        raw = get(f"https://en.wikipedia.org/w/index.php?title={t}&action=raw")
        open(path, "wb").write(raw)
    rev = revs[p]
    meta.append((p, rev["revid"], rev["timestamp"], hashlib.sha256(raw).hexdigest()))
    text = raw.decode("utf-8")
    heading = ""
    pos = 0
    blocks = []
    for m in re.finditer(r"^(=+)\s*(.*?)\s*\1\s*$|<math[^>]*>(.*?)</math>|\{\{math\|(.*?)\}\}", text, re.S | re.M):
        if m.group(2) is not None:
            heading = m.group(2); continue
        body = (m.group(3) if m.group(3) is not None else m.group(4)).strip()
        if PAT.search(body):
            line_start = text.rfind("\n", 0, m.start()) + 1
            line_end = text.find("\n", m.end())
            ctx = re.sub(r"<math[^>]*>.*?</math>|\{\{math\|.*?\}\}|\[\[(?:[^|\]]*\|)?([^\]]*)\]\]|'''?|<[^>]+>|\{\{[^}]*\}\}",
                         lambda k: k.group(1) or " ", text[line_start:line_end], flags=re.S)
            ctx = re.sub(r"\s+", " ", ctx).strip(" |!-")[:160]
            rows.append((p, heading, ctx, " ".join(body.split())))
seen, out_rows = set(), []
for r in rows:
    if (r[0], r[3]) in seen: continue
    seen.add((r[0], r[3])); out_rows.append(r)
with open("runs/dvj/candidates.md", "w", encoding="utf-8") as f:
    f.write("# Candidates: math blocks carrying pi or e, from ten Wikipedia articles (DVJ)\n\n")
    for i, (p, h, c, b) in enumerate(out_rows, 1):
        f.write(f"{i}. [{p} / {h}] {c}\n   `{b}`\n")
for m in meta: print("|".join(map(str, m)))
print("candidates", len(out_rows), "of", len(rows), "blocks")
