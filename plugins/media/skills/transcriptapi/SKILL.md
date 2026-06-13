---
name: transcriptapi
description: Use when the user wants to transcribe, summarise, extract text from, or create documents/articles/notes from a YouTube video, playlist, or channel. Triggers on phrases like "transcribe this YouTube video", "summarise this video", "make notes from", "turn this video into a doc", "get the transcript", "extract text from YouTube", "all videos from this playlist", "transcribe this channel", or any YouTube URL/handle in a content-extraction request. Powered by transcriptapi.com.
---

# transcriptapi.com — YouTube transcripts

Fetch transcripts for single videos, whole playlists, or channel uploads via [transcriptapi.com](https://transcriptapi.com). Use the bundled CLI (`scripts/transcript.py`) for almost everything; only call the HTTP API directly for edge cases the CLI does not cover.

## When to use

- Transcribe a single YouTube video → `video`
- Transcribe every video in a playlist → `playlist`
- Transcribe latest / all uploads from a channel → `channel`
- Summarise / write notes / draft an article from a video → `video`, then summarise the text
- Find videos to transcribe → `search`
- Get the latest 15 videos from a channel without spending credits → `latest` (free)
- Convert `@handle` or channel URL to a `UC…` ID → `resolve` (free)

## CLI quick reference

The bundled CLI handles auth, pagination, retries, and output formatting. Always prefer it.

```bash
SCRIPT=~/.Codex/skills/transcriptapi/scripts/transcript.py

# single video → plain text on stdout (default)
python3 $SCRIPT video dQw4w9WgXcQ
python3 $SCRIPT video https://youtu.be/dQw4w9WgXcQ
python3 $SCRIPT video <url> --metadata             # prepend title/author header
python3 $SCRIPT video <url> --timestamps           # [mm:ss] before each line
python3 $SCRIPT video <url> --json                 # raw API response
python3 $SCRIPT video <url> -o transcript.txt     # save to file

# whole playlist (paginated automatically)
python3 $SCRIPT playlist <playlist-url-or-id>                       # stdout
python3 $SCRIPT playlist <playlist-url-or-id> --output-dir ./out    # one .txt per video
python3 $SCRIPT playlist <playlist-url-or-id> --limit 10            # cap videos
python3 $SCRIPT playlist <playlist-url-or-id> --list-only           # just list IDs

# channel uploads
python3 $SCRIPT channel @TED --latest                  # last 15 (free)
python3 $SCRIPT channel @TED --limit 50 --output-dir ./ted
python3 $SCRIPT channel UCAuUUnT6oDeKwE6v1NGQxug --list-only

# discovery / utilities
python3 $SCRIPT search "react hooks tutorial" --limit 10
python3 $SCRIPT search "veritasium" --type channel
python3 $SCRIPT latest @TED
python3 $SCRIPT resolve @TED                           # → UCAuUUnT6oDeKwE6v1NGQxug
```

Run `python3 $SCRIPT <subcommand> --help` for full flags.

## Common workflows

### Summarise a video
```bash
python3 $SCRIPT video <url> --metadata > /tmp/transcript.txt
```
Then read the file and write the summary in the format the user asked for (bullets, exec summary, blog post, etc.). Default output is plain text with no timestamps — ideal for summarisation.

### Turn a video into a document/article
```bash
python3 $SCRIPT video <url> --metadata --timestamps > /tmp/raw.txt
```
Use timestamps to add chapter markers in the final doc. After writing, render to `.docx` or `.pdf` via the `doc` / `pdf` skills if needed.

### Transcribe a whole playlist or course
```bash
python3 $SCRIPT playlist <url> --output-dir ./course
```
Each video is saved as `<video_id>_<safe_title>.txt` in the directory, with a header containing title and watch URL. Failed videos are logged to stderr and skipped — the run does not abort.

### Process a channel's content for research / repurposing
```bash
# just look first (free, last 15 videos)
python3 $SCRIPT channel @creator --latest --list-only

# then transcribe them
python3 $SCRIPT channel @creator --latest --output-dir ./creator
```

## Authentication

API key resolution order:

1. `$TRANSCRIPTAPI_KEY` env var (overrides everything)
2. `~/.Codex/skills/transcriptapi/.api-key` file (already set up; chmod 600)

To rotate the key, replace the file's contents or set the env var.

## Direct HTTP API

Only needed for things the CLI does not expose. Base URL: `https://transcriptapi.com/api/v2`. Auth: `Authorization: Bearer <key>`.

| Endpoint | Method | Credits | Purpose |
|---|---|---|---|
| `/youtube/transcript` | GET | 1 | Extract video transcript |
| `/youtube/search` | GET | 1 | Search videos / channels |
| `/youtube/channel/resolve` | GET | free* | Resolve `@handle`/URL → `UC…` |
| `/youtube/channel/search` | GET | 1 | Search within a channel |
| `/youtube/channel/videos` | GET | 1/page | Paginated channel uploads |
| `/youtube/channel/latest` | GET | free* | Last 15 videos via RSS |
| `/youtube/playlist/videos` | GET | 1/page | Paginated playlist videos |

*Free endpoints still require auth and ≥1 active credit on the account.

### `/youtube/transcript` params
- `video_url` (required): full URL, short URL, or 11-char video ID
- `format`: `json` (default) or `text`
- `include_timestamp`: `true` (default) | `false`
- `send_metadata`: `false` (default) | `true`

### Pagination
`/youtube/channel/videos` and `/youtube/playlist/videos` return `{ results, continuation_token, has_more, ... }`. Pass `continuation=<token>` (without the `channel`/`playlist` arg) to fetch the next page.

### Example raw call
```bash
KEY=$(cat ~/.Codex/skills/transcriptapi/.api-key)
curl -s "https://transcriptapi.com/api/v2/youtube/transcript?video_url=dQw4w9WgXcQ&format=text" \
  -H "Authorization: Bearer $KEY"
```

## Errors and limits

- **Rate limit:** 300 req/min per key. CLI auto-retries on 429/503 honouring `Retry-After`.
- **Credits:** charged on 200 OK only; not charged on 4xx/5xx errors or 429.
- **402 Payment Required:** out of credits → top up at https://transcriptapi.com/top-up
- **404 / 422:** video unavailable, private, or transcript-disabled — CLI batch mode skips and continues.
- **401:** invalid API key → check `.api-key` file or env var.

## Tips

- For large playlists/channels, use `--list-only` first to confirm scope before spending credits.
- Default text output strips timestamps for cleanest input to summarisation. Add `--timestamps` only if the user wants timestamped notes / chapters.
- For very long transcripts, save to a file and read in chunks rather than piping through stdout.
- Transcripts rarely change — cache the file locally when iterating on a summary or article.
