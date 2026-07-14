#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_DEST="${CODEX_SKILLS_DIR:-$HOME/.agents/skills}"
RULES_DEST="${CODEX_RULES_FILE:-$HOME/.codex/AGENTS.md}"
mkdir -p "$SKILL_DEST" "$(dirname "$RULES_DEST")"

installed=0
for source in "$ROOT"/plugins/*/skills/*/; do
  [ -f "$source/SKILL.md" ] || continue
  name="$(basename "$source")"
  target="$SKILL_DEST/$name"
  temp="$SKILL_DEST/.${name}.tmp.$$"
  rm -rf "$temp"
  mkdir -p "$temp"
  rsync -a "$source" "$temp/"
  rm -rf "$target"
  mv "$temp" "$target"
  installed=$((installed+1))
done

rules_temp="${RULES_DEST}.tmp.$$"
cp "$ROOT/codex-global-rules.md" "$rules_temp"
mv "$rules_temp" "$RULES_DEST"
printf 'Installed %s Codex skills and global rules.\n' "$installed"
