---
name: hermes-tweet
version: 0.1.6
description: Native Hermes Agent X/Twitter plugin for read-first social listening, account context, and approval-gated actions through Xquik.
homepage: https://github.com/Xquik-dev/hermes-tweet#readme
user-invocable: true
---

# Hermes Tweet

Use Hermes Tweet when a Hermes Agent workflow needs X/Twitter search, account
reads, trend context, monitor context, or explicit posting actions. It is a
native Hermes Agent plugin, published as the `hermes-tweet` Python package and
maintained at <https://github.com/Xquik-dev/hermes-tweet>.

## Install

```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

If the plugin is installed but disabled, enable it explicitly:

```bash
hermes plugins enable hermes-tweet
```

Hermes can also load the package from PyPI inside the Hermes Python
environment:

```bash
uv pip install --python ~/.hermes/hermes-agent/venv/bin/python hermes-tweet
hermes plugins enable hermes-tweet
```

## Configure

Set an Xquik API key in the Hermes runtime environment:

```bash
export XQUIK_API_KEY="<your-xquik-api-key>"
```

Leave actions disabled by default:

```bash
export HERMES_TWEET_ENABLE_ACTIONS="false"
```

Only set `HERMES_TWEET_ENABLE_ACTIONS=true` in sessions that intentionally need
posting, replies, DMs, follows, webhooks, monitors, or media changes.

## Tools

- `tweet_explore` searches the bundled endpoint catalog without an API call.
- `tweet_read` calls catalog-listed read-only endpoints when `XQUIK_API_KEY`
  is configured.
- `tweet_action` handles write-like or private endpoints only when action
  routing is explicitly enabled.

## Workflow

1. Use `tweet_explore` to find the right `/api/v1/...` path.
2. Use `tweet_read` for public or account read routes.
3. Keep `tweet_action` off unless the operator has approved account-changing
   work for the current session.
4. Do not paste API keys into prompts, PR comments, issues, or chat messages.

## Good Fits

- Social listening for launches, competitors, mentions, trends, and accounts.
- Brand or creator research before drafting X/Twitter content.
- Support triage from public mentions and timelines.
- Giveaway, follower, reply, list, media, and draw audits.
- Controlled publishing where the human operator enables actions for the
  session.
