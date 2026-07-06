#!/usr/bin/env python3
"""Cross-site duplicate-content audit for sibling rank-and-rent sites.

Usage: python3 audit.py "/path/to/Site A" "/path/to/Site B" [more sites...]
Extracts headings (h1-h3) and body sentences from .astro/.md/.mdx/.html files,
then reports exact and near-duplicate overlap between every pair of sites.
Exit code 1 = FAIL (any exact heading match or sentence overlap above threshold).
"""
import sys, re, pathlib, difflib, itertools

EXTS = {".astro", ".md", ".mdx", ".html"}
SKIP_DIRS = {"node_modules", "dist", ".git", ".astro", "public"}
NEAR = 0.85  # difflib ratio for near-duplicate sentences
MIN_WORDS = 8

def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", "", s.lower())).strip()

SKIP_NAMES = re.compile(r"^(readme|claude|agents|design|product|spec|plan|notes|build-state|todo)", re.I)

def extract(site):
    heads, sents = set(), set()
    root = pathlib.Path(site)
    # customer-facing content lives in src/; scan whole repo only if no src/
    scan = root / "src" if (root / "src").is_dir() else root
    for f in scan.rglob("*"):
        if f.suffix not in EXTS or any(p in SKIP_DIRS for p in f.parts) or SKIP_NAMES.match(f.stem):
            continue
        try:
            text = f.read_text(errors="ignore")
        except OSError:
            continue
        text = re.sub(r"^---.*?---", "", text, flags=re.S)  # frontmatter
        for m in re.findall(r"<h([1-3])[^>]*>(.*?)</h\1>", text, flags=re.S | re.I):
            h = norm(re.sub(r"<[^>]+>|\{[^}]*\}", "", m[1]))
            if len(h.split()) >= 2:
                heads.add(h)
        for m in re.findall(r"^#{1,3} +(.+)$", text, flags=re.M):
            h = norm(m)
            if len(h.split()) >= 2:
                heads.add(h)
        body = re.sub(r"<script.*?</script>|<style.*?</style>", "", text, flags=re.S | re.I)
        body = re.sub(r"<[^>]+>|\{[^}]*\}|^import .*$|^const .*$", " ", body, flags=re.M)
        for s in re.split(r"[.!?]\s", body):
            s = norm(s)
            if len(s.split()) >= MIN_WORDS:
                sents.add(s)
    return heads, sents

def main(paths):
    data = {p: extract(p) for p in paths}
    fail = False
    for a, b in itertools.combinations(paths, 2):
        an, bn = pathlib.Path(a).name, pathlib.Path(b).name
        ha, sa = data[a]; hb, sb = data[b]
        shared_h = sorted(ha & hb)
        shared_s = sorted(sa & sb)
        # near-duplicate sentences (sampled: exact-miss only)
        near = []
        remaining_b = list(sb - sa)
        for s in list(sa - sb)[:400]:
            match = difflib.get_close_matches(s, remaining_b, n=1, cutoff=NEAR)
            if match:
                near.append((s, match[0]))
        print(f"\n=== {an} vs {bn} ===")
        print(f"shared headings: {len(shared_h)} | identical sentences: {len(shared_s)} | near-duplicates: {len(near)}")
        for h in shared_h[:20]:
            print(f"  [HEADING] {h}")
        for s in shared_s[:10]:
            print(f"  [EXACT]   {s[:120]}")
        for s, t in near[:10]:
            print(f"  [NEAR]    {s[:100]}\n            ~ {t[:100]}")
        if shared_h or shared_s or len(near) > 3:
            fail = True
    print("\nVERDICT:", "FAIL — sibling sites share content" if fail else "PASS — no significant overlap")
    sys.exit(1 if fail else 0)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Need at least two site paths.")
    main(sys.argv[1:])
