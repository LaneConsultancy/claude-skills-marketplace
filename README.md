# george-skills

A Claude plugin marketplace bundling George Lane's skill library — marketing, SEO, copywriting, CRO, paid ads, development workflow, media, and more. 122 skills across 10 themed plugins.

## Add this marketplace

**Claude Code (CLI):**
```
/plugin marketplace add LaneConsultancy/claude-skills-marketplace
/plugin install copywriting@george-skills
```

**Claude web (claude.ai → Customize → Personal plugins):** add this repo as a plugin source.

## Plugins

| Plugin | Skills | Covers |
|---|---|---|
| `copywriting` | 20 | Sales copy, email, social, voice, editing, anti-slop |
| `seo` | 19 | Audits, technical, schema, sitemaps, local, programmatic |
| `dev-workflow` | 18 | TDD, debugging, planning, code review, git worktrees, security |
| `marketing-strategy` | 16 | Offers, pricing, psychology, ICP, research, launches |
| `ads` | 12 | Google/Meta/Facebook campaigns, ad copy, analytics |
| `cro` | 10 | Landing pages, forms, popups, signup/onboarding, A/B |
| `media` | 9 | Image/video/audio generation, screenshots, transcripts |
| `web-dev` | 9 | Site builders, UI design, Playwright, deploys |
| `business-ops` | 6 | GTD, X/Twitter, Retell AI, Cloudways, Namecheap |
| `reference-docs` | 3 | Doc creation, PDF handling, OpenAI docs |

## Updating

Skills are maintained in `~/.claude/skills/`. After changing a skill, rebuild and push:

```
bash ~/build-skills-marketplace.sh
cd ~/claude-skills-marketplace && git add -A && git commit -m "update skills" && git push
```

Then on each consumer run `/plugin marketplace update george-skills` (or enable auto-update) to pull the latest.

## Note

Some skills depend on local tooling (CLIs, MCP servers, browser automation, subagents) and will only fully run in an environment where those tools exist. They will still appear and trigger on the web, but tool-dependent steps require a local Claude Code setup.
