---
name: unslop-writing
description: Anti-slop rules for written content — blog posts, essays, articles, emails, tutorials, copy. Bans the most common AI writing defaults (phrases, structures, tonal habits, word choices). Load alongside copywriting, content-generation, or any writing skill. Triggers on any text/content writing task.
---

# Unslop profile for blog writing, essays, and articles.

Generated from 100 samples. Use as a Codex skill, AGENTS.md entry, or system prompt.

---

## Phrases to never use

Do not use any of the following phrases or close variants:

- "In today's [adjective] landscape/world/era"
- "In an increasingly [adjective] world"
- "It's not just about X — it's about Y"
- "Here's the thing"
- "Here's why that matters"
- "Let's dive in" / "Let's dive deeper" / "Let's unpack this"
- "At its core"
- "At the end of the day"
- "It's worth noting that"
- "This is where things get interesting"
- "The short answer is" / "The long answer is"
- "But here's the catch"
- "Think about it this way"
- "This isn't just [X] — it's [grander version of X]"
- "The reality is"
- "What does this mean for [audience]?"
- "Spoiler alert:"
- "Let that sink in"
- "The bottom line"
- "In other words"
- "Make no mistake"
- "It goes without saying"
- "The question isn't whether X, but Y"
- "X is more than just Y — it's Z"
- "This raises an important question"
- "To put it simply"
- "Perhaps most importantly"
- "The good news is" / "The bad news is"

## Structural patterns to avoid

- Do not start with a broad, sweeping statement about the state of the world or industry before narrowing to the topic. Start with the actual topic.
- Do not use the structure: "[Broad claim]. But [complication]. Here's [resolution]."
- Do not end with a paragraph that restates the thesis in grander terms than the piece warrants.
- Do not organize every piece as: intro hook → context → 3-5 body sections → takeaway → call to action. Vary the structure.
- Do not use a "The future of X" section near the end.
- Do not add a "Final thoughts" or "Key takeaways" section header.
- Do not number your points unless the reader actually needs them in order.
- Do not use rhetorical questions as transitions between sections.

## Tonal patterns to avoid

- Do not hedge with "might," "could potentially," "it remains to be seen" on every other claim. Either commit or don't make the claim.
- Do not affect breathless enthusiasm. Not everything is "fascinating," "remarkable," "game-changing," or "transformative."
- Do not address the reader as "you" in every paragraph.
- Do not use the false-authority voice where every claim sounds like settled consensus when it's actually opinion.
- Do not end paragraphs with one-sentence dramatic kickers meant to sound profound.

## Sentence mechanics to avoid

These survive a phrase blacklist untouched. Catch them at the sentence level.

- **Colon reveals.** Noun phrase, colon, lowercase dramatic reveal: "The detail that makes it work: a separate agent grades it." Write it as a plain sentence. Colons are for lists, labels, and quotes.
- **Trailing `-ing` pseudo-analysis.** "...highlighting the team's commitment," "...underscoring the shift," "...reflecting a broader trend." These pretend to explain meaning and explain nothing. State the actual consequence instead.
- **Importance puffery.** "Stands as a testament to," "marks a pivotal moment," "plays a vital role," "solidifies its position." State the fact; let the reader decide if it matters.
- **Weasel attribution.** "Experts agree," "studies show," "industry reports suggest," "many argue," "widely regarded as." Name the source or cut the claim. Never invent one.
- **Synonym cycling.** Rotating terms for variety: "The agent reviews the draft. The assistant scores the piece. The tool suggests fixes." If the clear word is right, repeat it.
- **Fake-strong verbs.** "Serves as a centralised hub for," "acts as a bridge between." Prefer "is" and "has" when clearer, or name what the thing actually does.
- **Negative listing.** "Not a X. Not a Y. A Z." Just say Z.
- **Dramatic fragmentation.** "X. And Y. And Z." / "That's it. That's the whole thing."
- **Robotic rhythm.** Repeated sentence shapes, identical paragraph lengths, stacked punchy fragments.
- **Fake-profound kickers.** The final "deep" line that turns the point into an aphorism or mic-drop. Delete it — don't rewrite it into a better metaphor. End on the clearest concrete sentence already there.
- **Formatting slop.** Emoji in headings, bold sprinkled mid-sentence, bullets where two sentences of prose read better, headers over two-sentence sections.
- **Em dashes.** Not a default rhythm crutch. None in short copy; 1-2 in a long piece only where they clearly beat a comma, full stop, or parentheses.

## Word-level patterns to avoid

- Do not overuse: "landscape," "paradigm," "leverage," "robust," "seamless," "ecosystem," "holistic," "nuanced," "compelling," "innovative," "crucial," "essential," "fundamental."
- Do not use "delve" or "delve into."
- Do not use "navigate" metaphorically (as in "navigate challenges").
- Do not use "unlock" metaphorically (as in "unlock potential").
- Do not use "double-edged sword."
- Do not use "at the intersection of X and Y."
- Also banned outright: utilise, facilitate, empower, streamline, embark, supercharge, harness, ever-evolving, tapestry, realm, beacon, multifaceted, meticulous, intricate, paramount, "a testament to", "game changer", "this changes everything".
- Cut often-empty adverbs where they add nothing: just, literally, honestly, simply, actually, truly, fundamentally, importantly, crucially, inherently, inevitably. Keep one when it carries real emphasis, uncertainty, or the writer's spoken rhythm.

## Language

British English throughout: -ise/-isation, -our, -re, -ce nouns / -se verbs, doubled l before suffixes (travelled, modelling). Dates as 30 July 2026. Money as £1,200. Metric units. British vocabulary (mobile, holiday, flat, autumn, maths). Never convert inside a quote, brand name, or code.

---

Instead of reaching for any of these defaults, be creative. Vary your openings, structures, and phrasing every time. If you notice yourself about to use any of the patterns above, stop and find a different way to say it. Write like a specific human with a specific voice would — not like a median of all writing on the internet.

---

## Why this matters (web context)

Copy tone is part of cognitive load. Predictable, clean prose lowers it; AI-default phrasings spike it because the reader's pattern-matcher flags "this isn't human" and the halo effect collapses. Walls of text do the same — visual noise reads as effort cost. **Imperfection is the trust signal in writing too:** specific human details, mild asymmetry, an opinion the median wouldn't risk. Don't sand it smooth. [KB: principles.md → Differentiation]

For design-side parallels (visual cognitive fluency, anti-AI-default UI), see `~/.Codex/knowledgebase/website-design/principles.md` and the integration guide at `~/.Codex/knowledgebase/website-design/applying-to-skills.md`.
