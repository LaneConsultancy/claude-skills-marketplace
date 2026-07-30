#!/usr/bin/env python3
"""Cross-site duplicate-content audit for sibling rank-and-rent sites.

Usage: python3 audit.py "/path/to/Site A" "/path/to/Site B" [more sites...]
       python3 audit.py --min-sentences 25 "/path/to/A" "/path/to/B"

Extracts headings (h1-h3) and body sentences from customer-facing files, then
reports exact and near-duplicate overlap between every pair of sites.
Exit code 1 = FAIL (any exact heading match, exact sentence match, >3 near
duplicates, or a coverage floor breach that makes the audit untrustworthy).

WHY THIS SCANS .ts FILES
------------------------
These sites keep every word of page copy in `src/data/services.ts` as HTML
strings, not in .astro templates. An earlier version scanned only
.astro/.md/.mdx/.html and therefore never read a single sentence of the copy it
exists to check -- it returned "PASS -- no significant overlap" for two sites
sharing 100+ identical sentences. A guardrail that fails open is worse than no
guardrail.

WHY IT IS NOT A src/data/ ALLOWLIST
-----------------------------------
An allowlist encodes today's file layout. The next site that puts copy in
src/content/, src/copy/ or src/pages/*.astro inline would silently drop out of
the audit and reproduce exactly the failure above. So the model is:

  include everything by default  ->  subtract known CODE paths

A new *content* location is picked up automatically with no edit here. A new
*code* location shows up as a false positive: loud, cheap, and fixable. That is
the correct direction for the failure mode to point.

Three layers keep shared architecture (explicitly permitted between siblings)
from being reported as shared prose:
  1. CODE_DIRS / CODE_FILES  -- src/lib, src/pages/api, middleware.ts, configs
     and tests are never scanned for code-extension files.
  2. String-literal extraction -- for .ts/.tsx/.js/.jsx only the contents of
     string and template literals are considered. Identifiers, imports, control
     flow and comments can never masquerade as prose.
  3. is_prose() -- drops literals that are class-attribute soup, slugs, URLs, or
     otherwise not sentences a visitor would read.
"""
import sys, re, pathlib, difflib, itertools

MARKUP_EXTS = {".astro", ".md", ".mdx", ".html"}
CODE_EXTS = {".ts", ".tsx", ".js", ".jsx", ".mjs"}
EXTS = MARKUP_EXTS | CODE_EXTS

SKIP_DIRS = {"node_modules", "dist", ".git", ".astro", ".vercel", "public", "coverage"}

# Directory names that hold application code rather than page copy. Applied to
# CODE_EXTS only -- markup files are treated as content wherever they live.
CODE_DIRS = {"lib", "api", "utils", "server", "scripts", "integrations",
             "test", "tests", "__tests__", "node_modules"}
# Exact filenames / patterns that are plumbing regardless of directory.
CODE_FILE_RE = re.compile(
    r"^(middleware|env\.d|.*\.config|.*\.test|.*\.spec|.*\.d)$", re.I)

NEAR = 0.85       # difflib ratio for near-duplicate sentences
MIN_WORDS = 8
NEAR_SAMPLE = 2000  # cap on difflib driver rows per pair
# Coverage floor: below this a site plainly did not get read properly and the
# verdict must not be reported as PASS. Override with --min-sentences.
MIN_SENTENCES = 40

# Blind-spot detector. The original failure was not "too few sentences" -- the
# old script still pulled 93 sentences out of York's .astro files and happily
# printed PASS. What it did was skip a 60KB src/data/services.ts holding every
# word on the site, because .ts was not in EXTS. So the check that actually
# catches this class of bug is: is there a big text file in src/ that this run
# read nothing out of? If so the audit cannot claim to have seen the copy.
BULK_BYTES = 8192   # unknown-extension files at or above this are suspicious
BULK_WORDS = 150    # readable words in a scanned file that produced no sentences
ASSET_EXTS = {".svg", ".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".ico",
              ".woff", ".woff2", ".ttf", ".otf", ".eot", ".mp4", ".webm", ".pdf",
              ".zip", ".lock", ".map", ".xml", ".txt", ".csv"}


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", "", s.lower())).strip()


SKIP_NAMES = re.compile(
    r"^(readme|claude|agents|design|product|spec|plan|notes|build-state|todo)", re.I)

# Tokens that mark a string literal as machine-facing rather than page copy.
NOT_PROSE_RE = re.compile(
    r"(https?://|^[\w-]+\.(?:ts|js|astro|json|css|svg|png|jpe?g|webp)$"
    r"|^[a-z0-9]+(?:-[a-z0-9]+){2,}$)", re.I)
# Tailwind/utility class soup: many short hyphenated tokens, no real sentence.
CLASS_SOUP_RE = re.compile(r"^[\w:./\[\]%-]+(?:\s+[\w:./\[\]%-]+)*$")


def is_prose(text):
    """True if a normalised string reads like a sentence a visitor would see."""
    words = text.split()
    if len(words) < MIN_WORDS:
        return False
    # Require a decent share of ordinary dictionary-shaped words. Minified code,
    # concatenated identifiers and class lists fail this.
    wordlike = sum(1 for w in words if w.isalpha() and 2 <= len(w) <= 16)
    return wordlike / len(words) >= 0.7


def literals_from_code(src):
    """Return each string/template literal in a JS/TS source as its own chunk.

    Chunks stay separate so that two adjacent fields -- an image path and its
    alt text, say -- are never concatenated into one pseudo-sentence.

    Hand-rolled scanner rather than a regex so that quotes inside comments and
    comment markers inside strings (https://) cannot be confused. Comments are
    dropped deliberately: developer notes are not customer-facing copy, and the
    sibling sites legitimately share them.
    """
    out, i, n = [], 0, len(src)
    while i < n:
        c = src[i]
        if c == "/" and i + 1 < n and src[i + 1] == "/":
            j = src.find("\n", i)
            i = n if j < 0 else j + 1
        elif c == "/" and i + 1 < n and src[i + 1] == "*":
            j = src.find("*/", i + 2)
            i = n if j < 0 else j + 2
        elif c in "'\"`":
            quote, j, buf = c, i + 1, []
            while j < n:
                if src[j] == "\\":
                    buf.append(" ")
                    j += 2
                    continue
                if src[j] == quote:
                    break
                if quote != "`" and src[j] == "\n":
                    break  # unterminated: not a real literal, bail out safely
                buf.append(src[j])
                j += 1
            lit = "".join(buf)
            # ${...} interpolations are expressions, not prose.
            out.append(re.sub(r"\$\{[^{}]*\}", " ", lit))
            i = j + 1
        else:
            i += 1
    return out


# attr="..." / attr='...' / attr={expr}. Stripped BEFORE tags, because an Astro
# expression that spans a tag boundary -- href={`tel:${site.phoneTel}`} -- makes
# the naive <[^>]+> tag regex desync and spill `aria-label` soup into the prose
# set as if it were a sentence.
ATTR_RE = re.compile(
    r"""\s[a-zA-Z_:][\w:.-]*\s*=\s*("[^"]*"|'[^']*'|\{(?:[^{}]|\{[^{}]*\})*\})""")
# Residual JSX/Astro expression code left over once tags are gone. Removing the
# operators and dotted references rather than the whole {...} keeps genuine
# microcopy inside a conditional ("Call now") in the corpus.
JSX_CODE_RE = re.compile(r"\b[\w$]+(?:\.[\w$]+)+\b|=>|[{}()]|\?\s|\bmap\b")


def to_prose_text(text, is_markup):
    """Reduce a markup/literal chunk to the words a visitor would actually read."""
    text = re.sub(r"<!--.*?-->|\{/\*.*?\*/\}", " ", text, flags=re.S)
    text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", text,
                  flags=re.S | re.I)
    text = ATTR_RE.sub(" ", text)
    # A block-level boundary ends a sentence even with no punctuation, so two
    # adjacent <li> items never fuse into one pseudo-sentence.
    text = re.sub(r"</?(?:p|li|h[1-6]|div|br|td|tr|section|ul|ol)\b[^>]*>",
                  ". ", text, flags=re.I)
    text = re.sub(r"<[^>]*>", " ", text)
    text = JSX_CODE_RE.sub(" ", text)
    if is_markup:
        text = re.sub(r"^\s*(?:import|const|let|var|export) .*$", " ", text,
                      flags=re.M)
    return text


def is_code_path(f, scan_root):
    """True if this file is application plumbing rather than page content."""
    if f.suffix not in CODE_EXTS:
        return False
    try:
        rel = f.relative_to(scan_root)
    except ValueError:
        rel = f
    if any(part in CODE_DIRS for part in rel.parts[:-1]):
        return True
    return bool(CODE_FILE_RE.match(f.stem))


def extract(site):
    heads, sents = set(), set()
    scanned, skipped_code, unread_bulk = [], [], []
    root = pathlib.Path(site)
    # customer-facing content lives in src/; scan whole repo only if no src/
    scan = root / "src" if (root / "src").is_dir() else root
    for f in sorted(scan.rglob("*")):
        if not f.is_file() or any(p in SKIP_DIRS for p in f.parts):
            continue
        if f.suffix not in EXTS:
            # Bulk text this audit has no reader for. Exactly the shape of the
            # original blind spot, so it must be surfaced, not ignored.
            if f.suffix.lower() not in ASSET_EXTS and not f.name.startswith(".") \
                    and not SKIP_NAMES.match(f.stem):
                try:
                    if f.stat().st_size >= BULK_BYTES:
                        unread_bulk.append(
                            (str(f.relative_to(root)), f.stat().st_size,
                             "no reader for this extension"))
                except OSError:
                    pass
            continue
        if SKIP_NAMES.match(f.stem):
            continue
        if is_code_path(f, scan):
            skipped_code.append(str(f.relative_to(root)))
            continue
        try:
            raw = f.read_text(errors="ignore")
        except OSError:
            continue

        if f.suffix in CODE_EXTS:
            chunks = literals_from_code(raw)
        else:
            chunks = [re.sub(r"^---.*?---", "", raw, flags=re.S)]  # frontmatter

        before, prose_words = len(sents), 0
        for text in chunks:
            for m in re.findall(r"<h([1-3])[^>]*>(.*?)</h\1>", text,
                                flags=re.S | re.I):
                h = norm(re.sub(r"<[^>]+>|\{[^}]*\}", "", m[1]))
                if len(h.split()) >= 2:
                    heads.add(h)
            for m in re.findall(r"^#{1,3} +(.+)$", text, flags=re.M):
                h = norm(m)
                if len(h.split()) >= 2:
                    heads.add(h)

            body = to_prose_text(text, f.suffix in MARKUP_EXTS)
            prose_words += len(norm(body).split())
            for s in re.split(r"[.!?]\s", body):
                s = norm(s)
                if is_prose(s) and not NOT_PROSE_RE.search(s):
                    sents.add(s)
        gained = len(sents) - before
        scanned.append((str(f.relative_to(root)), gained))
        # A file carrying plenty of readable words but yielding no sentences
        # means the reader is wrong for it -- the same failure wearing a
        # different hat. Judged on word count after style/script/tags are
        # stripped, not raw bytes, so a 19KB layout that is mostly CSS does not
        # cry wolf.
        if gained == 0 and prose_words >= BULK_WORDS:
            unread_bulk.append((str(f.relative_to(root)), prose_words,
                                "readable words but no extractable sentences"))
    return heads, sents, scanned, skipped_code, unread_bulk


def main(paths, min_sentences):
    data = {}
    coverage_fail = False
    for p in paths:
        heads, sents, scanned, skipped, unread = extract(p)
        data[p] = (heads, sents)
        name = pathlib.Path(p).name
        print(f"\n--- coverage: {name} ---")
        print(f"files scanned: {len(scanned)} | headings: {len(heads)} | "
              f"sentences: {len(sents)} | code files excluded: {len(skipped)}")
        for path, n in sorted(scanned, key=lambda t: -t[1])[:6]:
            print(f"  {n:5d} sentences  {path}")
        if unread:
            print(f"  !! UNREAD BULK: {len(unread)} file(s) contributed no prose "
                  f"to this audit:")
            for path, size, why in sorted(unread, key=lambda t: -t[1])[:10]:
                print(f"     {size:7d}  {path}  ({why})")
            print("     If any of these hold page copy, this audit did not check")
            print("     it. Teach the extractor to read them before trusting a PASS.")
            coverage_fail = True
        if len(sents) < min_sentences:
            print(f"  !! COVERAGE FLOOR BREACH: only {len(sents)} sentences "
                  f"extracted (floor {min_sentences}).")
            print("     The audit did not read this site's copy. Do NOT read the")
            print("     verdict below as a pass -- find where the copy lives and")
            print("     make sure this script reaches it.")
            coverage_fail = True

    fail = coverage_fail
    for a, b in itertools.combinations(paths, 2):
        an, bn = pathlib.Path(a).name, pathlib.Path(b).name
        ha, sa = data[a]
        hb, sb = data[b]
        shared_h = sorted(ha & hb)
        shared_s = sorted(sa & sb)
        # near-duplicate sentences (exact-miss only). Drive the loop from the
        # smaller of the two residual sets so the cap bites as late as possible.
        only_a, only_b = sorted(sa - sb), sorted(sb - sa)
        driver, pool = (only_a, only_b) if len(only_a) <= len(only_b) \
            else (only_b, only_a)
        near = []
        for s in driver[:NEAR_SAMPLE]:
            match = difflib.get_close_matches(s, pool, n=1, cutoff=NEAR)
            if match:
                near.append((s, match[0]))
        truncated = " (sampled)" if len(driver) > NEAR_SAMPLE else ""
        print(f"\n=== {an} vs {bn} ===")
        print(f"shared headings: {len(shared_h)} | identical sentences: "
              f"{len(shared_s)} | near-duplicates: {len(near)}{truncated}")
        for h in shared_h[:20]:
            print(f"  [HEADING] {h}")
        for s in shared_s[:10]:
            print(f"  [EXACT]   {s[:120]}")
        for s, t in near[:10]:
            print(f"  [NEAR]    {s[:100]}\n            ~ {t[:100]}")
        if shared_h or shared_s or len(near) > 3:
            fail = True

    if coverage_fail:
        verdict = "FAIL — coverage floor breached, audit is not trustworthy"
    elif fail:
        verdict = "FAIL — sibling sites share content"
    else:
        verdict = "PASS — no significant overlap"
    print("\nVERDICT:", verdict)
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    args = sys.argv[1:]
    floor = MIN_SENTENCES
    if "--min-sentences" in args:
        i = args.index("--min-sentences")
        floor = int(args[i + 1])
        del args[i:i + 2]
    if len(args) < 2:
        sys.exit("Need at least two site paths.")
    main(args, floor)
