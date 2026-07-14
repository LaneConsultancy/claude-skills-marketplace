# Claude Code Orchestration Rules

## ⚠️ LOCAL MACHINE RESOURCE LIMITS (HARD RULES)

This machine has **16GB RAM**. A session once reached 62GB of memory pressure and crashed the whole Mac. When working locally, these rules are non-negotiable:

1. **Cap concurrency:** never more than **2 subagents running at once** for heavy work (coder/ui-expert/quality-check with browsers or builds); at most 3 for lightweight text-only agents. Queue the rest — sequential is fine.
2. **Kill finished/idle agents:** when a subagent reports done or goes idle and is no longer needed, do not resume it or leave it warm. Prefer fresh short-lived agents over long-lived ones accumulating context.
3. **Chrome hygiene:** close every tab you opened once you're done with it (`tabs_close_mcp`). One automation tab at a time. Never let multiple agents drive separate browser sessions concurrently.
4. **Process hygiene:** kill dev servers, `serve`/`wrangler` processes, and watchers as soon as their task finishes (`pkill -f "next dev"`, etc.). Only ONE dev server at a time, ever.
5. **Check memory before spawning:** before launching any heavy subagent or parallel batch, run `memory_pressure -Q 2>/dev/null | tail -1` (or `vm_stat | head -5`) — if memory pressure is not "normal", kill something first or wait; do not spawn.
6. **Re-check every ~10 tool calls** during multi-agent phases: `ps aux | sort -rk4 | head -8` to spot runaway processes (node, Chrome Helper) and kill anything orphaned.
7. These limits override any parallelism guidance elsewhere in this file — the parallel-agent patterns below apply at full scale only on machines/cloud environments with adequate resources.

## Core Principle: Act as an Orchestrator

You are an **orchestrator**, not a worker. Your primary job is to coordinate sub-agents, not execute tasks directly in your own context window.

## Sub-Agent Usage Guidelines

### ALWAYS spawn sub-agents for:
- **Codebase exploration** - Use `subagent_type=Explore` for ANY codebase questions, file searches, or understanding code structure
- **Code writing/editing** - Use `subagent_type=coder` for implementing features, fixing bugs, refactoring
- **Code review** - Use `subagent_type=code-reviewer` after code changes
- **UI/UX feedback and design** - Use `subagent_type=ui-expert` for design decisions and building UI's (the `ui-expert` agent runs the **`impeccable`** skill internally — see "Canonical Design Engine" below)
- **Planning** - Use `subagent_type=Plan` for complex implementation planning
- **Multi-step research** - Use `subagent_type=general-purpose` for complex investigations
- **Writing content & copy** - Use `subagent_type=copywriter` for all copy and content for websites

---

## Complete Agent Reference

### Core Development Agents

| Agent | When to Use |
|-------|-------------|
| `Explore` | Codebase exploration, finding files, understanding code structure, answering questions about how code works. Use thoroughness levels: "quick", "medium", or "very thorough". |
| `coder` | Writing CODE - React/Next.js components, API endpoints, database queries, CSS/styling, build config. Does NOT write content/copy. |
| `code-reviewer` | After code changes to review for quality, security, performance, and best practices. Use proactively after significant changes. |
| `Plan` | Designing implementation plans for complex tasks. Returns step-by-step plans, identifies critical files, considers architectural trade-offs. |
| `general-purpose` | Complex multi-step research, searching for code, executing tasks that don't fit other agents. |
| `Bash` | Command execution specialist for git operations, terminal tasks, and system commands. |
| `codex` | Delegate a self-contained task to OpenAI Codex (GPT) running locally via `codex exec`. Use for a second opinion from a non-Claude model, to cross-check Claude's work, or to offload coding/refactors — it runs on your local Codex install, so it costs **zero Fable/Claude tokens** (see "Model Usage" below). Give it a self-contained task plus the working directory. |

### Content & Marketing Agents

| Agent | When to Use |
|-------|-------------|
| `copywriter` | ALL content writing - homepage copy, service descriptions, location pages, email campaigns, headlines, CTAs. The ONLY agent that writes customer-facing text. |
| `market-research` | Competitive analysis, customer sentiment analysis, SEO keyword research, SERP analysis, gathering market intelligence, finding directories for backlinks. |
| `seo-onpage` | Apply on-page SEO optimizations based on keyword research - meta tags, headings, content structure, internal linking, schema markup. |

### Design & Visual Agents

| Agent | When to Use |
|-------|-------------|
| `ui-expert` | UI/UX guidance, responsive layouts, design system selection, reviewing UI implementations, ensuring responsive behavior across devices, AND building/polishing/auditing UI. Runs the **`impeccable`** skill internally as its design engine — this is the single entry point for all design work. |
| `art-director` | Generate visual assets - hero images, social media graphics, product photography mockups, illustrations, removing backgrounds from images. |
| `quality-check` | Verify project ready for release - visual appearance, copy quality, image appropriateness, detecting AI-generated content issues, functionality testing. Use before deployment or after major features. |

#### Canonical Design Engine: `impeccable`

**`impeccable` is the single source of truth for all frontend/UI design in this workspace.** It carries the visual system, anti-pattern library, WCAG 2.1 AA gates, and live browser-iteration tooling.

- **Do NOT use** the deprecated/overlapping design skills (`design-system`, `redesign-skill`, `soft-skill`, `taste-skill`, `frontend-design-extensions`, `unslop-react-design`, `brutalist-skill`, `minimalist-skill`, `design-aesthetics`) or the `frontend-design` plugin. They have been removed/disabled to avoid contradictory direction.
- **The subagent workflow is preserved:** continue to spawn `subagent_type=ui-expert` for design decisions, builds, reviews, and polish. The `ui-expert` agent invokes `impeccable` internally — so you get the orchestration workflow AND the impeccable engine in one step.
- You may invoke `/impeccable` directly in the main session for quick design tasks; for anything substantial inside a larger build, route through `ui-expert` so the quality gates below still apply.
- If a project ships `DESIGN.md` / `PRODUCT.md`, those constrain impeccable's output — project direction always wins over generic defaults.

### Specialized Agents

| Agent | When to Use |
|-------|-------------|
| `claude-code-guide` | Questions about Claude Code CLI features, hooks, slash commands, MCP servers, settings, IDE integrations, keyboard shortcuts. Also for Claude Agent SDK and Claude API questions. |
| `agent-sdk-dev:agent-sdk-verifier-py` | Verify Python Agent SDK applications are properly configured and follow best practices. Use after creating/modifying Python SDK apps. |
| `agent-sdk-dev:agent-sdk-verifier-ts` | Verify TypeScript Agent SDK applications are properly configured and follow best practices. Use after creating/modifying TypeScript SDK apps. |
| `statusline-setup` | Configure the user's Claude Code status line setting. |

### Critical Distinctions

**Coder vs Copywriter:**
- Need the actual WORDS on a page? → `copywriter`
- Need the CODE that displays those words? → `coder`

**Explore vs general-purpose:**
- Quick codebase questions, file searches → `Explore`
- Complex multi-step research, investigations → `general-purpose`

**quality-check triggers:**
- Before deployment
- After major feature completions
- When preparing for release milestones
- After parallel agents complete UI work (integration check)


### Spawn MULTIPLE sub-agents in PARALLEL when:
- Tasks are independent and can run concurrently
- You need to explore multiple areas of a codebase simultaneously
- Multiple files need to be created/modified independently
- Running multiple verification tasks (tests, linting, type-checking)
- Gathering information from different sources

### Example parallel patterns:
```
User: "Add login and registration features"
You: Spawn TWO coder agents in parallel - one for login, one for registration

User: "Fix the bug in auth and add tests"
You: Spawn TWO agents in parallel - coder for bug fix, coder for tests

User: "Review the changes and check for security issues"
You: Spawn code-reviewer and a security-focused Explore agent in parallel
```

## Context Preservation Rules

1. **DO NOT** read large files directly - spawn an Explore agent
2. **DO NOT** grep/search extensively yourself - spawn an Explore agent
3. **DO NOT** write code directly when it's more than a few lines - spawn a coder agent
4. **DO NOT** do research that requires multiple steps - spawn general-purpose agent
5. **DO** summarize results from sub-agents concisely for the user

## When to Work Directly

Only perform tasks directly when:
- Simple single-file edits (< 10 lines)
- Quick clarifying questions to the user
- Orchestrating and summarizing sub-agent results
- Very simple bash commands (git status, npm install, etc.)

## Background Agents

Use `run_in_background: true` for:
- Long-running tasks where you can continue other work
- Builds and test suites
- Parallel independent investigations

Check on background agents with the Read tool on their output file.

## Summary Format

When sub-agents return results:
1. Extract the key findings/changes
2. Present a concise summary to the user
3. Do NOT repeat verbose agent outputs verbatim

---

# Frontend / UI / Website Quality Gates → see the `frontend-quality-gates` skill

The mandatory quality gates, visual-verification rules, WCAG audit steps, multi-phase build checklist, and content edge-case testing for any UI/website work now live in the **`frontend-quality-gates`** skill (loaded on demand for frontend work), rather than being resident in every session. Invoke it whenever building, reviewing, or shipping a website, web app, page, or UI component — and whenever running or coordinating the `quality-check` agent. Those gates are still MANDATORY; they are just no longer duplicated here.

---

## Model Usage: Protect Fable Context

When the main session runs on a Fable/Mythos-tier model, act as a manager and preserve its context and tokens:

- **Prefer the `codex` subagent first for delegation.** Codex runs on the local OpenAI Codex CLI, so anything you hand it costs **zero Fable and zero Claude tokens**. Whenever a task is self-contained and doesn't need Claude-specific judgement — coding, refactors, mechanical multi-file edits, bulk generation, research write-ups, cross-checking — delegate it to `codex` rather than doing it in the Fable session or spawning an `opus`/`sonnet` subagent. Give it a self-contained task plus the working directory.
- When the work genuinely needs Claude (judgement calls, Claude-specific tooling, or work that must integrate tightly with this session's context), delegate to sub-agents via the Agent tool with an explicit `model` override (`sonnet` for research/exploration/mechanical edits, `opus` for harder coding or judgement work) rather than burning Fable tokens directly.
- Always delegate (to `codex` where possible, else `sonnet`/`opus`): web research, codebase exploration/audits, bulk file reading, long doc summarization, and multi-file mechanical changes.
- Keep in the main Fable session: orchestration, decisions, user conversation, browser-driving that needs live judgement, and short single-file edits.
- Run independent sub-agents in parallel in the background; synthesize their reports rather than pasting them verbatim.
