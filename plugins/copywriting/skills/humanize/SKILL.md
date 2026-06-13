---
name: humanize
description: Rewrite AI-generated text to sound completely human and bypass AI detection. Use when asked to "humanize", "make this sound human", "anti-AI", "rewrite to sound human", "de-AI this", "make this undetectable", or when any text needs to sound less like AI wrote it.
---

# Humanize — AI Text Rewriter

## Core Purpose

This skill rewrites AI-generated text to evade detection by breaking the predictable patterns AI uses: perfect grammar, corporate buzzwords, even pacing, lack of personality. AI text fails the sniff test because it's too polished, too balanced, too nothing. Real human writing has rough edges, opinions, rhythm changes, and a voice that belongs to someone specific. This skill adds all of that back.

---

## Framing Principle

- **Imperfection = trust signal in the AI era.** When the internet floods with AI-perfected output, the imperfections themselves become the proof of humanity — slightly messy phrasing, a specific personal opinion, an off-rhythm sentence, the odd typo left in. Don't sand the humanity off. The rules below aren't ways to mimic humans; they're ways to stop hiding the human that's already there. [KB: principles.md → Differentiation] (See `~/.Codex/knowledgebase/website-design/applying-to-skills.md`.)

---

## The 7 Humanization Rules

### Rule 1: Break the Rhythm

AI writes in metronomic patterns. Humans don't. Mix sentence lengths aggressively. Follow a long compound sentence with a two-word fragment. Start some sentences with "And" or "But". Use one-sentence paragraphs for emphasis. Include the occasional run-on that mimics natural thought.

A paragraph of five identically-structured sentences is a dead giveaway. Smash that pattern. Short. Then long, winding, with a couple of clauses that stack on top of each other before finally arriving at the point. Then medium. Then a fragment that just hangs there.

### Rule 2: Inject Imperfection (Carefully)

Not grammar errors — but human quirks: parenthetical asides (like this one), dashes for interruption — mid-thought pivots, starting sentences with "Look," or "Here's the thing," or "Honestly,". Occasional colloquialisms. The odd sentence fragment that works because humans speak that way.

The goal isn't sloppy writing. It's writing that breathes. Humans pause, reconsider, add caveats. The text should feel like someone actually sat down and wrote it, not like it was generated in 0.3 seconds.

### Rule 3: Kill AI Phrases Dead

Replace every instance of these words and phrases — they are AI fingerprints:

- "delve" — use "dig into", "look at", "explore"
- "harness" — use "use", "tap into", "put to work"
- "landscape" (metaphorical) — use "space", "world", "scene"
- "leverage" — use "use", "make the most of", "lean on"
- "robust" — use "solid", "strong", "reliable"
- "seamless" — use "smooth", "easy", "without the faff"
- "cutting-edge" — use "latest", "newest", "bleeding edge" (sparingly)
- "game-changer" — use "big deal", "shift", or just describe why it matters
- "elevate" — use "improve", "lift", "step up"
- "streamline" — use "simplify", "speed up", "cut the clutter"
- "foster" — use "build", "encourage", "grow"
- "facilitate" — use "help", "make happen", "run"
- "synergy" — just don't. Describe the actual benefit instead.
- "holistic" — use "full-picture", "whole", "complete"
- "paradigm" — use "model", "approach", "way of thinking"
- "empower" — use "give the tools to", "let", "enable"
- "innovative" — use "new", "clever", "fresh" — or better, show don't tell
- "transformative" — use "massive", "fundamental", or describe the actual change
- "navigate the complexities" — use "deal with", "figure out", "work through"
- "at the end of the day" — cut it entirely or use "ultimately", "when it comes down to it"
- "it's important to note" — cut it. Just state the thing.
- "in today's fast-paced world" — cut it. Everyone knows the world is fast-paced.
- "a testament to" — use "proof that", "shows that", "speaks to"
- Em dashes (—) — AI overuses em dashes. Replace with commas, full stops, parentheses, or just restructure the sentence. One or two em dashes in a long piece is fine, but if you find yourself reaching for them every other sentence, that's a tell. Use sparingly if at all.
- "It's not X — it's Y" / "This isn't about X, it's about Y" — AI loves this contrasting pivot structure. It sounds punchy but it's become a fingerprint. Restructure: just state what it IS without the theatrical setup of what it isn't. Or if the contrast genuinely matters, find a different way to frame it.

Read `references/ai-detection-triggers.md` for the full kill list with replacements.

### Rule 4: Add Personality Fingerprints

Humans have opinions. They favour certain phrases. They have pet peeves. Inject:

- A mild opinion ("I think X is overrated")
- A preference ("I'd rather Y than Z")
- A qualification ("This works brilliantly for X, though I'd be careful with Y")
- A moment of honesty ("Full disclosure — I'm biased here because...")

The text should feel like it was written by a person with a point of view, not a machine trying to sound balanced and neutral about everything. Balanced is boring. Balanced is detectable.

### Rule 5: Use Concrete Over Abstract

AI defaults to vague, sweeping statements. Humans use specifics. Replace:

- "many businesses" with "the 3 plumbing companies I spoke to last week"
- "significant improvement" with "a 23% bump"
- "various factors" with "price, timing, and whether the builder actually showed up"
- "a wide range of services" with the actual services
- "numerous benefits" with the actual benefits, named

Specificity is the single strongest signal of human writing. AI hedges. Humans commit.

### Rule 6: Create Natural Transitions

AI uses formulaic transitions ("Furthermore", "Moreover", "Additionally", "In conclusion"). Humans use:

- "So here's where it gets interesting"
- "But wait"
- "The weird thing is"
- "Which brings me to"
- "Now,"
- Or just start the next thought without a transition at all — humans do that.

If your transition sounds like it belongs in a Year 9 essay, rewrite it. "In addition to this" is the written equivalent of a robot wearing a human mask. Just move to the next point.

### Rule 7: Vary Your Register

AI maintains one consistent tone throughout. Humans shift between formal and casual within the same piece. A serious point followed by a dry joke. Technical explanation followed by "basically, it just works". This tonal variation is the hardest thing for AI to replicate naturally.

A paragraph about data security can end with "...which is a fancy way of saying your stuff stays safe." A section about pricing methodology can include "Look, nobody likes talking about money, but here's how it works." These shifts feel human because they are human.

---

## The Process

### Step 1 — Rewrite

Apply all 7 rules to the source text. Read `references/humanization-techniques.md` for detailed technique guidance. Read `references/ai-detection-triggers.md` for the complete phrase kill list.

Go through the text systematically:

1. Identify and replace all AI phrases (Rule 3)
2. Break up any metronomic sentence patterns (Rule 1)
3. Inject human quirks — asides, dashes, fragments (Rule 2)
4. Add at least one opinion, preference, or qualification (Rule 4)
5. Replace abstract/vague claims with concrete specifics (Rule 5)
6. Swap formulaic transitions for natural ones (Rule 6)
7. Vary the register — mix formal and casual (Rule 7)

### Step 2 — Read-Aloud Test

Read the rewritten text as if speaking it aloud. If any sentence sounds like it came from a press release, corporate memo, or AI chatbot, rewrite that sentence. If you wouldn't say it to a mate over coffee, it's not human enough.

Key questions:
- Does this sound like a real person talking?
- Would I actually say this out loud without feeling ridiculous?
- Is there anywhere I'd naturally pause, laugh, or raise an eyebrow?
- Does it have a voice — or does it sound like it could have been written by anyone (or anything)?

### Step 3 — Final Pass

Check for remaining AI fingerprints:

- Are all sentences roughly the same length? (Bad — vary them.)
- Does every paragraph have exactly 3-4 sentences? (Bad — mix it up.)
- Are there any surviving AI phrases from the kill list?
- Is there at least one moment of personality, opinion, or aside?
- Does it sound like one specific person wrote it, or could any AI have produced it?

If the answer to that last question is "any AI could have produced it" — you're not done. Go back to Step 1.

---

## Auto-Calibration

The intensity of humanization should match the content type:

| Content Type | Humanization Level | Notes |
|---|---|---|
| Blog posts, personal essays | Heavy | Full personality, asides, opinions, fragments |
| Landing pages, sales copy | Medium-Heavy | Personality but focused on conversion, less digression |
| Email campaigns | Heavy | Should sound like a real person writing to you |
| Service descriptions | Medium | Professional but warm, avoid corporate feel |
| B2B whitepapers | Light-Medium | Keep authority, add subtle personality, avoid AI phrases |
| Legal/compliance text | Light | Kill AI phrases only, keep structure formal |
| Social media | Maximum | Should be indistinguishable from genuine human posts |

Detect the content type from context and calibrate automatically. If unsure, default to Medium-Heavy.

---

## Output Format

When rewriting text, always provide:

```
## Humanized Version
[The rewritten text]

## Changes Made
- [Bullet list of key changes and why]

## AI Detection Risk
[Low/Medium/High] — [Brief explanation of remaining risk areas, if any]
```
