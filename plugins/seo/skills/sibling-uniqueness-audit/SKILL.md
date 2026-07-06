---
name: sibling-uniqueness-audit
description: Use before launching or after editing any rank-and-rent or PBN site that has sibling sites, when writing copy for a site cloned from a source design, or when the user asks to check for duplicate content, shared H2s, or "town-name-swapped" copy between their sites.
---

# Sibling Uniqueness Audit

## Overview

Sibling rank-and-rent sites share design, never copy. Google treats town-name-swapped duplicates as doorway pages. This skill runs a mechanical cross-site overlap check so "I wrote original copy" is verified, not claimed.

## When to Use

- Step 9 of the rank-and-rent factory (`~/.claude/guides/WORKFLOW-TEMPLATES.md`) — blocking gate before launch
- After ANY copy edit to a site that has siblings
- Before launch of a site cloned from a SOURCE design site
- FACTS.md lists the sibling sites — audit against all of them

## Run It

```bash
python3 ~/.claude/skills/sibling-uniqueness-audit/audit.py \
  "/path/to/Site A" "/path/to/Site B" ["/path/to/Site C" ...]
```

- Scans `src/` only (customer-facing `.astro/.md/.mdx/.html`); skips specs, README, CLAUDE.md, node_modules, dist
- Reports per pair: shared headings (h1–h3), identical sentences (≥8 words), near-duplicates (difflib ≥ 0.85)
- Exit 0 = PASS, exit 1 = FAIL

## Reading the Report

| Finding | Action |
|---|---|
| `[HEADING]` any shared heading | FAIL. Rewrite the heading structurally — different angle, not a synonym swap. |
| `[EXACT]` shared sentence | FAIL. Rewrite one side from scratch. |
| `[NEAR]` town-name-swapped sentence | FAIL — this is the classic violation. Rewrite structurally. |
| `[NEAR]` hits that are CSS/class-attribute soup or deliberately shared legal/attribution lines (e.g. "reviews from previous business" disclosure) | Judgement call — note them in the report to the user, don't count toward the verdict. |

A FAIL verdict is blocking, same as a Critical quality-check issue: fix, re-run, only then deploy.

## Fixing Failures

Rewrites must be **structural**: different page skeleton, different heading angles, different sentence rhythm — not paraphrase. Re-run the audit after rewriting; repeat until PASS. Dispatch rewrites with the site's FACTS.md pasted in (see client-intake skill) so originality doesn't come at the cost of fabricated facts.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Auditing only the new site vs its SOURCE | Audit against ALL siblings — pairs the user didn't mention have shipped with shared H2s before. |
| Treating near-duplicates as "close enough to original" | Town-name swaps ARE the failure mode this exists to catch. |
| Running it only at launch | Post-launch edits reintroduce overlap; re-run after copy changes. |
| Trusting a copywriter agent's "all original" claim | Run the script. Claims aren't evidence. |
