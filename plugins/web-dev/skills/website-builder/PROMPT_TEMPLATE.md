# Website Builder Prompt Template

## Complete Workflow

```
Step 1: Create your project folder
        mkdir my-client-website && cd my-client-website

Step 2: Start Claude Code in the project folder
        claude

Step 3: Run the website builder with ralph-loop (recommended)
        /ralph-loop [paste prompt below] --max-iterations 30 --completion-promise "BUILD COMPLETE"

        WHY ralph-loop? The website builder runs 10 phases with quality gates.
        A single Claude session may hit context limits before finishing.
        Ralph-loop automatically restarts Claude with the same prompt when a
        session ends, and Claude reads /spec/build-state.md to resume where
        it left off. The build completes when Claude outputs the BUILD COMPLETE
        promise after Phase 9.

        Alternative (small sites only): /website-builder
        For sites with fewer than 10 pages, a single session may suffice.
        Use /website-builder directly — Claude will interview you and build
        the site in one go.

Note: Claude will interview you to gather requirements if no /spec/brief.md exists.
      Alternatively, create /spec/brief.md manually (copy template from SPEC_TEMPLATE.md) to skip the interview.
```

---

## The Prompt (Copy This)

```
Your Role: Website Build Coordinator (NOT a coder)

You orchestrate agents and ENFORCE QUALITY GATES. You do NOT write code yourself.

## AUTONOMOUS EXECUTION
- After Phase 0 brief confirmation, execute ALL remaining phases without stopping for user input
- When a gate PASSES → immediately begin the next phase (no waiting, no summarizing, no asking)
- When a gate FAILS → spawn agents to fix issues, re-run the gate, continue when it passes
- Never ask "shall I proceed?" — just proceed
- If stuck after 3 attempts on the same gate, document the blocker in /spec/build-state.md and skip to next phase

## BUILD STATE TRACKING
- Maintain /spec/build-state.md with current phase, checklist, gate results
- On session start: read /spec/build-state.md FIRST to determine where to resume
- Do not repeat completed phases — check filesystem for existing artifacts

## PRE-FLIGHT (Before any coding)
1. Verify browser automation tools work (navigate + screenshot)
2. If browser tools don't work: STOP and tell me

## BUILD PHASES WITH MANDATORY QUALITY GATES

### Phase 0: Gather Requirements
- Check if /spec/brief.md exists
- If not: interview the user in 5 rounds (business basics, services, locations, design, features)
- Generate /spec/brief.md from answers
- Gate: User confirms the brief

### Phase 1: Content Research
- Spawn market-research agent for competitor/SERP analysis
- Create content-requirements.md and keyword-mapping.md
- Gate: Research files exist with word count requirements

### Phase 1.5: Design Concepting
- Spawn ui-expert agent using /frontend-design:frontend-design thinking framework
- Create /spec/design-concept.md with specific: creative direction, fonts, colors, layout patterns per section, motion approach, component styles
- Gate: Design concept is specific and unique (no generic choices, no "standard" anything)

### Phase 2: Content & Images (Parallel)
- Track A: Spawn copywriter for all page content
- Track B: Spawn art-director for hero/service images (from brief, not content)
- Gate: All content files meet word counts AND images are professional

### Phase 3: Foundation
- Spawn coder(s) for setup
- After: Start dev server, take screenshot, check console
- Gate: Visual verification passes

### Phase 4: Core Pages
- Spawn coder(s) for main pages (WITH REAL CONTENT from /spec/content/)
- After: Spawn quality-check agent
- Gate: Quality check at 375px/768px/1440px passes

### Phase 5: Additional Pages
- Spawn coder(s) for remaining pages (WITH REAL CONTENT)
- After: Spawn quality-check agent
- Gate: All page templates visually verified

### Phase 6: Polish/Animations
- Spawn coder(s) for animations
- After: Spawn quality-check with MULTI-SCREENSHOT test
- Gate: Content visible in ALL screenshots (immediate, 2s delay, scroll, return)

### Phase 7: SEO
- Spawn seo-onpage agent
- After: Quick visual check

### Phase 8: Production Build
- Run npm run build && npm run start
- Screenshot production build
- Gate: Production matches dev

### Phase 9: Final Check
- Spawn quality-check agent
- Must test all viewports, all page types, network tab
- Must answer YES to all three:
  1. Looks like £10k agency work?
  2. Business owner would be proud?
  3. Competes with best in industry?

## CRITICAL RULES
- Code reviewers MUST use browser, not just read code
- Quality-check agents MUST take screenshots
- If quality check says "NOT READY": FIX BEFORE PROCEEDING
- Do NOT skip any gate
- Do NOT trust rubber-stamp approvals

## COMPLETION
Output: <promise>BUILD COMPLETE</promise> ONLY when:
- All gates passed
- Final quality check returned "READY TO SHIP"
- No Critical issues remain

WARNING: Do not output this promise tag unless ALL criteria are genuinely met.
The ralph-loop stop hook watches for this exact string — lying to exit will
produce an incomplete website.

Review the implementation plan in /spec folder and begin.
```

---

## Using Ralph Loop (Recommended)

Ralph Loop solves the problem of Claude hitting context limits mid-build. It works by:

1. Running your prompt in a Claude session
2. When the session ends (context limit or turn limit), automatically re-feeding the same prompt
3. Claude reads `/spec/build-state.md` on re-entry to know where to resume
4. Repeating until Claude outputs the completion promise (`BUILD COMPLETE`)

### Running the Build

```
/ralph-loop [paste the prompt above] --max-iterations 30 --completion-promise "BUILD COMPLETE"
```

### Choosing `--max-iterations`

| Site Size | Pages | Recommended Iterations |
|-----------|-------|----------------------|
| Small | < 10 pages | 10-15 |
| Medium | 10-50 pages | 20-30 |
| Large | 50-100+ pages | 30-50 |

Each iteration is a full Claude session. Most phases complete within 1-2 iterations. Budget extra for quality gate failures and fixes.

### Monitoring Progress

While ralph-loop runs, you can check progress by reading the build state file:
```
cat [project-folder]/spec/build-state.md
```

This shows the current phase, gate results, and any blockers.

### Stopping Early

To stop the loop before completion:
```
/cancel-ralph
```
The build state is preserved in `/spec/build-state.md`, so you can resume later by re-running the ralph-loop command.

---

## Key Differences from Old Prompt

| Old Prompt | New Prompt |
|------------|------------|
| Manual spec required | Auto-interview if no spec (Phase 0) |
| Images after content | Images parallel with content (Phase 2) |
| No visual verification | Visual verification at every gate |
| Code review only | Code review + quality check |
| No specific viewports | 375px/768px/1440px required |
| No animation testing | Multi-screenshot animation test |
| No production build test | Production build required |
| "ALL TRACKS COMPLETE" | "BUILD COMPLETE" only if READY TO SHIP |

---

## Alternative: Include Spec in Prompt (For Simpler Projects)

For smaller projects, you can include the spec directly in the prompt instead of using a separate file:

```
Your Role: Website Build Coordinator (NOT a coder)

## THE WEBSITE TO BUILD

**Business:** [Business Name]
**Phone:** [Phone Number]
**Address:** [Address]
**Services:** [Service 1], [Service 2], [Service 3]
**Locations:** [Location 1], [Location 2], [Location 3]

**Tech Stack:** Next.js 14, ShadCN UI, Tailwind CSS
**Design:** Modern, clean, professional. Primary color: [#hex].

**Pages Needed:**
- Homepage
- About
- Contact
- Service pages (one per service)
- Location pages (one per location)

[Rest of the prompt with quality gates...]
```

This works for quick projects but for complex sites (100+ pages), use the `/spec/brief.md` approach.

---

## Files Created

| File | Purpose |
|------|---------|
| `~/.claude/skills/website-builder/SKILL.md` | Skill definition with quality gates |
| `~/.claude/skills/website-builder/PROMPT_TEMPLATE.md` | This file - copy-paste prompts |
| `~/.claude/skills/website-builder/SPEC_TEMPLATE.md` | Template for website specifications |
