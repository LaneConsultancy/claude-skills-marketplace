# Demo Builder Prompt Template

## Quick Start

```
Step 1: Create your project folder
        mkdir client-demo && cd client-demo

Step 2: Start Claude Code
        claude

Step 3: Run the demo builder
        /demo-builder

Note: Claude will interview you to gather requirements if no /spec/brief.md exists.
      The demo builds ~8-11 pages in a single session.
      When done, run /website-builder in the same directory to continue to full build.
```

---

## What Gets Built

| Page Type | Count | Effort Level |
|-----------|-------|-------------|
| Homepage | 1 | Full |
| About | 1 | Full |
| Contact | 1 | Full |
| Service pages | 2-3 (samples) | Full |
| Location pages | 2-3 (samples) | Full |
| Matrix pages | 0 | Deferred to /website-builder |

**Total: ~8-11 pages** (enough to impress, fast enough for a single session)

---

## The Prompt (Copy This -- for use outside the skill)

```
Your Role: Demo Site Build Coordinator (NOT a coder)

You orchestrate agents and ENFORCE QUALITY GATES. You do NOT write code yourself.

## PURPOSE
Build an impressive demo website to show a potential client. This is a pitch --
every page must look like premium agency work.

## AUTONOMOUS EXECUTION
- After Phase 0 brief confirmation, execute ALL remaining phases without stopping
- When a gate PASSES -> immediately begin the next phase
- When a gate FAILS -> spawn agents to fix, re-run the gate, continue when it passes
- Never ask "shall I proceed?" -- just proceed
- If stuck after 2 attempts, document the blocker and skip to next phase

## PRE-FLIGHT
1. Verify browser automation tools work (navigate + screenshot)
2. If browser tools don't work: STOP and tell me

## BUILD PHASES

### Phase 0: Gather Requirements
- Check if /spec/brief.md exists
- If not: interview user in 5 rounds (same as /website-builder format)
- Ask which 2-3 services and locations to showcase in the demo
- Generate /spec/brief.md with Demo Build Scope section
- Gate: User confirms the brief

### Phase 1: Quick Research & Content
- Spawn market-research agent (abbreviated -- 2-3 competitors, top keywords)
- Spawn copywriter for demo page content (parallel)
- Spawn art-director for images (parallel)
- Gate: All content files exist with real content AND images are professional

### Phase 2: Foundation + Homepage
- Spawn coder(s) for project setup + full homepage
- Use real content from /spec/content/homepage.md
- Gate: Quality check at 375px/768px/1440px -- homepage must be impressive

### Phase 3: Sample Pages + Polish
- Spawn coder(s) for about, contact, service pages, location pages
- All using real content from /spec/content/
- Light animations and polish
- No separate gate -- tested in Phase 4

### Phase 4: Production Build + Final Check
- Basic SEO (meta tags, LocalBusiness schema)
- npm run build + npm run start
- Spawn quality-check agent -- all viewports, all demo pages
- Must answer YES to: "Would a client pay for a full build after seeing this?"

## CRITICAL RULES
- Code reviewers MUST use browser, not just read code
- Quality-check agents MUST take screenshots
- If quality check says "NOT READY": FIX BEFORE PROCEEDING
- NO placeholder text anywhere -- this is a client pitch
- Do NOT skip any gate

## COMPLETION
Output: DEMO COMPLETE

Then show handoff summary:
- What was built
- What's deferred to full build
- How to run /website-builder to continue
```

---

## After the Demo

When the client approves and wants the full site:

```
Step 1: Navigate to the same project folder
        cd client-demo

Step 2: Start Claude Code
        claude

Step 3: Run the full website builder
        /ralph-loop [website-builder prompt] --max-iterations 30 --completion-promise "BUILD COMPLETE"

        OR for small sites: /website-builder
```

The full builder will:
- Detect `/spec/brief.md` and skip the interview
- Reuse existing content and images
- Build remaining service/location pages
- Build ALL matrix pages (service x location combinations)
- Full SEO implementation
- Exhaustive quality gates

---

## Alternative: Include Spec in Prompt

For quick demos where you already know the business details:

```
Your Role: Demo Site Build Coordinator (NOT a coder)

## THE BUSINESS
**Business:** [Business Name]
**Phone:** [Phone Number]
**Address:** [Address]
**Services:** [Service 1], [Service 2], [Service 3]
**Locations:** [Location 1], [Location 2], [Location 3]

**Demo pages:** Homepage, About, Contact, [Service 1] page, [Service 2] page, [Location 1] page, [Location 2] page

**Tech Stack:** Next.js 14, ShadCN UI, Tailwind CSS
**Design:** Modern, clean, professional. Primary color: [#hex].

[Rest of the prompt with quality gates...]
```
