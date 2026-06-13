---
name: linkedin-post-writer
description: Write LinkedIn posts in George Lane's voice. Warm, honest, direct, British English. Uses an anti-AI writing system with banned words, hook formulas, post type templates, and a pre-publish detection checklist. Triggers when the user asks to write, draft, or create a LinkedIn post, LinkedIn content, or social content specifically for LinkedIn. Also use for LinkedIn content strategy, post optimisation, or turning insights/stories/transcripts into LinkedIn posts.
---

# LinkedIn Post Writer (George Lane)

Write LinkedIn posts that sound like George — warm, honest, direct, British English — and pass an anti-AI detection checklist. Based on Marian Kamenistak's open-source LinkedIn system, voice-calibrated for George.

**Source:** https://github.com/marian-kamenistak/linkedin-post-writing-skill (voice profile replaced with George's)

## Core Workflow

When asked to write a LinkedIn post:

1. **Load the main skill file first:** Read `references/LinkedIn_SKILL.md` for the full voice profile, banned words, post type templates, algorithm strategy, and pre-publish checklist.

2. **Load the anti-AI guide:** Read `references/anti-ai-writing-guide.md` for vocabulary bans, structural rules, tone guidance, and side-by-side rewrites of AI-sounding drafts.

3. **Reference post examples when needed:** Load `references/LinkedIn_POST_EXAMPLES.md` to see annotated examples of what works. Note: the examples in that file are from the original Marian skill and illustrate structure, not George's voice — use them for formatting patterns, not voice calibration.

4. **For weekly content planning:** Load `references/linkedin-weekly-system.md` for the Sunday planning / Tue-Wed-Thu writing rhythm, content mix rules, and backlog integration.

5. **Cross-check with george-voice skill:** If the user's voice needs to be confirmed or refined beyond what's in this skill, the `george-voice` skill has the underlying voice guide. This skill inherits from it.

## Voice Summary (the quick version)

George sounds warm, honest, direct, and personal. British English. Short paragraphs. Contractions. First person. Self-deprecating humour. Explains the "why". Natural imperfections. Never corporate, never hype, never aggressive.

## Non-Negotiable Rules

- **British English always.** Colour, favourite, realise, organise, optimise. No "z" spellings. No American-isms like "awesome", "reach out", "touch base".
- **No AI-smell vocabulary.** Banned: leverage, navigate, unlock, empower, delve, tapestry, landscape, game-changer, ecosystem, seamless, robust, comprehensive, holistic, paradigm, synergy, crucial, vital, utilise, facilitate, elevate, transformative, dive deep, at the end of the day, the truth is, here's the thing, let me share.
- **No aggressive or hype language.** "Brutal truth", "harsh reality", "crush it", "don't miss out!", "limited time only!", "game-changer" — all off-brand for George.
- **No balanced both-sides hedging.** Take a clear position, but warmly. "On the other hand" and "it depends" are AI tells.
- **No dashes as separators.** Em dashes (—) and en dashes (–) are AI tells. Use full stops, commas, or line breaks.
- **Specific over vague.** Real numbers, real situations, real details beat generalisations every time.
- **Read-aloud test.** Every post must sound like something George would actually say to a mate over a coffee. If it sounds like a LinkedIn guru, rewrite it.

## Pre-Publish Checklist

Before delivering any post, verify:
- [ ] Zero banned words present
- [ ] British English throughout (no American spellings)
- [ ] Takes a clear position (warm, not aggressive)
- [ ] At least one specific detail (number, situation, example)
- [ ] Opens with a hook, not a throat-clearing intro
- [ ] Closes warmly (not "what do you think?" or hype CTA)
- [ ] Reads aloud like something George would say
- [ ] No dashes as separators
- [ ] Emojis used sparingly or not at all (default: zero)

## Output Format

Deliver posts as plain text, formatted for LinkedIn (short paragraphs, blank lines between thoughts for mobile readability). Do not include markdown formatting like `**bold**` or `#headers` in the final post. Do not wrap posts in code blocks unless the user asks.

If writing multiple variations, label them clearly (Version A, Version B) and note what's different about each.

After the post, include a short note with: character count, post type, content pillar, funnel position, and save potential.

## Content Pillars

George's likely pillars (confirm with George on first use):
1. Web development & building sites for local businesses
2. AI tools, Codex, agents, automation
3. Running a service business / consultancy

Off-pillar posts should be rare (20% rule).

## When NOT to Use This Skill

- Writing Twitter/X threads, Instagram captions, TikTok scripts — use `social-content` instead
- Writing blog posts, articles, long-form content — use `content-generation-optimization` or `copywriting`
- Writing marketing emails — use `email-campaign-copy` or `email-sequence`
- Writing website copy — use `copywriting` or `conversion-copywriting`
- Rewriting arbitrary AI text to sound human — use `humanize`

This skill is specifically for LinkedIn feed posts (short-form native content) in George's voice.
