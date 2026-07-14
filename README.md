# George Skills Marketplace

Shared public marketplace for Claude and Codex. It currently contains **130 skills** in **11 plugins**.

## Claude

Add this repository as a personal marketplace. Claude Code cloud setup can clone the repository and copy the plugin skills into `~/.claude/skills`.

## Codex desktop / CLI

`codex plugin marketplace add LaneConsultancy/claude-skills-marketplace`

The native Codex marketplace is at `.agents/plugins/marketplace.json`; the legacy Claude marketplace remains at `.claude-plugin/marketplace.json`.

## Codex cloud environment

Use this as both the environment **setup** and **maintenance** script so fresh and cached containers receive the latest skills and global rules:

```bash
set -euo pipefail
tmp_dir="$(mktemp -d)"
git clone --depth 1 https://github.com/LaneConsultancy/claude-skills-marketplace.git "$tmp_dir/skills-marketplace"
bash "$tmp_dir/skills-marketplace/scripts/install-codex-cloud.sh"
rm -rf "$tmp_dir"
```

Repository-specific instructions still belong in each repository's checked-in `AGENTS.md`.

## Published rules

- `global-rules.md`: Claude global rules used by existing SessionStart hooks.
- `codex-global-rules.md`: Codex global rules installed by the cloud bootstrap.

All generated content passes a secret-scan gate before commit and push.
