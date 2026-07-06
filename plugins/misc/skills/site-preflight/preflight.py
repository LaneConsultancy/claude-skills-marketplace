#!/usr/bin/env python3
"""Pre-deploy preflight audit for a single site (Astro / Next / Eleventy).

Mechanically catches the recurring launch gotchas seen across the site factory:
hardcoded secrets, unignored .env files, placeholder/leftover text, missing
canonical/OG/robots/sitemap, relative OG images, wrong-domain fallbacks, and
title-doubling. Every check is a plain grep/file test — no smart model needed.

Usage:
  python3 preflight.py "/path/to/Site"
  python3 preflight.py "/path/to/Site" --contaminants "greenhithe,01322788418,DA9"
  python3 preflight.py --self-test

--contaminants is a comma-separated list of strings that must NOT appear in a
clone's shipped source (leftover sibling town / phone / postcode). Optional.

Exit 0 = clean (only NOTEs). Exit 1 = at least one FAIL.

# ponytail: grep-based heuristics, not a parser. False positives are cheap to
# eyeball; the point is a weak model can run it and get a real signal.
"""
import sys, re, subprocess, pathlib

SRC_EXTS = {".astro", ".md", ".mdx", ".html", ".njk", ".tsx", ".jsx", ".ts", ".js", ".vue", ".svelte"}
SKIP_DIRS = {"node_modules", "dist", ".git", ".astro", ".next", ".vercel", ".netlify",
             "_site", "out", "build", ".cache", "coverage"}

# Secret patterns (same family the portfolio has leaked before).
SECRET_RES = [
    ("Google API key", re.compile(r"AIza[0-9A-Za-z_\-]{35}")),
    ("Stripe live key", re.compile(r"sk_live_[0-9A-Za-z]{20,}")),
    ("Stripe test key", re.compile(r"sk_test_[0-9A-Za-z]{20,}")),
    ("OpenAI key", re.compile(r"sk-proj-[0-9A-Za-z_\-]{20,}")),
    ("Anthropic key", re.compile(r"sk-ant-api[0-9A-Za-z_\-]{20,}")),
    ("GitHub token", re.compile(r"ghp_[0-9A-Za-z]{36}")),
    ("Slack token", re.compile(r"xox[bp]-[0-9A-Za-z\-]{10,}")),
    ("Twilio SID", re.compile(r"AC[0-9a-f]{32}")),
    ("Mailchimp key", re.compile(r"[0-9a-f]{32}-us[0-9]{1,2}")),
    ("Stripe webhook secret", re.compile(r"whsec_[0-9A-Za-z]{20,}")),
]
# Placeholder / leftover text that should never ship.
PLACEHOLDER_RES = [
    re.compile(r"\blorem ipsum\b", re.I),
    re.compile(r"\bTODO\b|\bFIXME\b"),
    re.compile(r"\[?\bplaceholder\b\]?", re.I),
    re.compile(r"your[ -]town|your[ -]city|your[ -]business name", re.I),
    re.compile(r"NaN years ago"),
    re.compile(r"coming soon", re.I),
    re.compile(r"localhost:\d+"),
    re.compile(r"[a-z0-9\-]+\.vercel\.app"),
    re.compile(r"123456"),           # placeholder phone tail
    re.compile(r"lONG_?KEY|xxx_paste|paste[_ ]full"),
]

def sh(args, cwd):
    try:
        return subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=60).stdout
    except Exception:
        return ""

def is_git(root):
    return (root / ".git").exists() or sh(["git", "rev-parse", "--is-inside-work-tree"], root).strip() == "true"

def iter_src(root):
    for p in root.rglob("*"):
        if p.is_dir():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.suffix.lower() in SRC_EXTS:
            yield p

def read(p):
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""

# Internal docs (not shipped to visitors). Still scanned for secrets & clone
# contamination — those matter anywhere — but skipped for placeholder noise.
_DOC_DIRS = {"plans", "spec", "docs", "briefs", ".prompts", "kickoff-context"}
_DOC_NAME = re.compile(r"^(readme|claude|agents|gemini|changelog|notes|todo|design|product|"
                       r".*[-_](plan|summary|runbook|guide|handoff|context)|.*summary)", re.I)

def is_doc(p, root):
    if any(part.lower() in _DOC_DIRS for part in p.relative_to(root).parts[:-1]):
        return True
    return bool(_DOC_NAME.match(p.stem))

class Report:
    def __init__(self):
        self.fails, self.warns, self.notes = [], [], []
    def fail(self, m): self.fails.append(m)
    def warn(self, m): self.warns.append(m)
    def note(self, m): self.notes.append(m)


def audit(root: pathlib.Path, contaminants):
    r = Report()
    root = root.resolve()
    src_files = list(iter_src(root))
    blob = {p: read(p) for p in src_files}

    # 1. Hardcoded secrets in source.
    for p, text in blob.items():
        for label, rx in SECRET_RES:
            m = rx.search(text)
            if m:
                r.fail(f"SECRET  {label} hardcoded in {p.relative_to(root)} → move to env + ROTATE it")

    # 2. .env hygiene (tracked or not gitignored).
    if is_git(root):
        tracked = sh(["git", "ls-files"], root).splitlines()
        for f in tracked:
            base = f.rsplit("/", 1)[-1]
            if base == ".env" or (base.startswith(".env.") and not base.endswith((".example", ".sample", ".template"))):
                r.fail(f"ENV     {f} is TRACKED in git → git rm --cached + add to .gitignore + rotate")
    for env in root.rglob(".env*"):
        if any(part in SKIP_DIRS for part in env.parts):
            continue
        if env.name.endswith((".example", ".sample", ".template")):
            continue
        if is_git(root):
            ignored = sh(["git", "check-ignore", str(env)], root).strip()
            if not ignored and env.name not in (sh(["git", "ls-files"], root)):
                # not ignored AND not tracked → still a risk (one git add away)
                rel = env.relative_to(root)
                if not sh(["git", "check-ignore", str(rel)], root).strip():
                    r.warn(f"ENV     {rel} exists but isn't gitignored → add to .gitignore")

    # 3. Placeholder / leftover text (shipped content only — docs are noise here).
    for p, text in blob.items():
        if is_doc(p, root):
            continue
        for rx in PLACEHOLDER_RES:
            m = rx.search(text)
            if m:
                line = text[:m.start()].count("\n") + 1
                r.warn(f"PLACEHOLDER  {p.relative_to(root)}:{line}  '{m.group(0)}'")
                break  # one hit per file is enough signal

    # 4. Clone contamination (leftover sibling town/phone/postcode).
    for token in [c.strip() for c in contaminants if c.strip()]:
        low = token.lower()
        for p, text in blob.items():
            if low in text.lower():
                line = text.lower().find(low)
                ln = text[:line].count("\n") + 1
                r.fail(f"CONTAMINATION  '{token}' from a sibling site in {p.relative_to(root)}:{ln}")
                break

    # 5. SEO presence checks (whole-site greps).
    all_text = "\n".join(blob.values())
    if "canonical" not in all_text:
        r.warn("SEO     no rel=canonical found anywhere in source")
    if "og:image" not in all_text and 'property="og:image"' not in all_text and "openGraph" not in all_text:
        r.warn("SEO     no Open Graph tags found anywhere")
    # relative og:image
    for p, text in blob.items():
        m = re.search(r'og:image"[^>]*content="(/[^"]*)"', text) or re.search(r"image:\s*['\"](/[^'\"]+)['\"]", text)
        if m and "openGraph" in text or (m and "og:image" in text):
            r.note(f"SEO     {p.relative_to(root)} uses a relative og:image ('{m.group(1)}') → absolute URL unfurls more reliably")
            break

    # 6. robots / sitemap presence.
    has_robots = (root / "public" / "robots.txt").exists() or any("robots" in p.name for p in src_files if p.suffix in {".ts", ".js"})
    has_sitemap = (root / "public" / "sitemap.xml").exists() or "sitemap" in all_text.lower() \
        or any((root / "public").glob("sitemap*")) if (root / "public").exists() else "sitemap" in all_text.lower()
    if not has_robots:
        r.warn("SEO     no robots.txt (public/robots.txt or a robots route)")
    if not has_sitemap:
        r.warn("SEO     no sitemap found (public/sitemap.xml or a sitemap integration)")

    # 7. Domain config.
    astro_cfg = next(root.glob("astro.config.*"), None)
    if astro_cfg and "site:" not in read(astro_cfg):
        r.warn("DOMAIN  astro.config has no `site:` → canonicals/sitemap fall back to localhost")
    # localhost baked into built output
    for built in ["dist", "_site", "out"]:
        idx = root / built / "index.html"
        if idx.exists() and "localhost" in read(idx):
            r.fail(f"DOMAIN  {built}/index.html contains 'localhost' → wrong canonical/OG shipped")

    # 8. Title-doubling heuristic (Next/Astro).
    tmpl = re.search(r'template:\s*["\`]%s\s*\|\s*([^"\`]+)["\`]', all_text)
    if tmpl:
        suffix = tmpl.group(1).strip()
        for p, text in blob.items():
            if is_doc(p, root):
                continue
            # a page hardcoding "| Suffix" in its own title while the template also appends it
            if re.search(r'title:\s*["\`][^"\`]*\|\s*' + re.escape(suffix), text):
                r.warn(f"TITLE   {p.relative_to(root)} hardcodes '| {suffix}' but the layout template already appends it → doubled title")

    return r


def print_report(name, r):
    print(f"\n===== PREFLIGHT: {name} =====")
    for m in r.fails: print("  [FAIL] " + m)
    for m in r.warns: print("  [WARN] " + m)
    for m in r.notes: print("  [note] " + m)
    verdict = "FAIL" if r.fails else ("WARN" if r.warns else "PASS")
    print(f"  → {verdict}  ({len(r.fails)} fail, {len(r.warns)} warn, {len(r.notes)} note)")
    return verdict


def self_test():
    import tempfile
    d = pathlib.Path(tempfile.mkdtemp())
    (d / "src").mkdir()
    (d / "src" / "page.astro").write_text(
        'const API="' + 'AIza' + 'x' * 35 + '";\n'
        '<title>Home | TODO fix this</title>\n<p>lorem ipsum</p>\n'
    )
    r = audit(d, contaminants=["greenhithe"])
    assert any("SECRET" in m for m in r.fails), "should flag the Google key"
    assert any("PLACEHOLDER" in m for m in r.warns), "should flag TODO/lorem"
    # contaminant present:
    (d / "src" / "leftover.astro").write_text("Serving Greenhithe, Kent")
    r2 = audit(d, contaminants=["greenhithe"])
    assert any("CONTAMINATION" in m for m in r2.fails), "should flag sibling leftover"
    print("self-test OK")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--self-test" in args:
        self_test(); sys.exit(0)
    contaminants = []
    if "--contaminants" in args:
        i = args.index("--contaminants")
        contaminants = args[i + 1].split(",")
        del args[i:i + 2]
    if not args:
        print(__doc__); sys.exit(2)
    site = pathlib.Path(args[0])
    if not site.exists():
        print(f"No such directory: {site}"); sys.exit(2)
    rep = audit(site, contaminants)
    verdict = print_report(site.name, rep)
    sys.exit(1 if rep.fails else 0)
