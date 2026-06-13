#!/usr/bin/env python3
"""TranscriptAPI.com CLI - YouTube transcripts, playlists, channels.

Examples:
  transcript.py video dQw4w9WgXcQ
  transcript.py video https://youtu.be/dQw4w9WgXcQ --metadata
  transcript.py playlist PLxxx --output-dir ./out
  transcript.py channel @TED --latest --output-dir ./ted
  transcript.py search "react hooks" --limit 10
  transcript.py resolve @TED

API key resolution order:
  1. $TRANSCRIPTAPI_KEY environment variable
  2. <skill-dir>/.api-key file
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from pathlib import Path

API_BASE = "https://transcriptapi.com/api/v2"
SKILL_DIR = Path(__file__).resolve().parent.parent
KEY_FILE = SKILL_DIR / ".api-key"


class APIError(Exception):
    def __init__(self, code, detail):
        self.code = code
        self.detail = detail
        super().__init__(f"{code}: {detail}")


def get_api_key():
    key = os.environ.get("TRANSCRIPTAPI_KEY")
    if key:
        return key.strip()
    if KEY_FILE.exists():
        return KEY_FILE.read_text().strip()
    sys.exit(
        "error: no API key found\n"
        f"  set TRANSCRIPTAPI_KEY env var, or\n"
        f"  put your key in {KEY_FILE}"
    )


def api_get(path, params=None):
    """GET with retry on 429/503. Raises APIError on other failures."""
    key = get_api_key()
    url = f"{API_BASE}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)

    for attempt in range(3):
        req = urllib.request.Request(
            url,
            headers={
                "Authorization": f"Bearer {key}",
                "User-Agent": "transcriptapi-cli/1.0 (+https://transcriptapi.com)",
                "Accept": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            try:
                err = json.loads(body)
                detail = err.get("detail", body)
                if isinstance(detail, dict):
                    detail = detail.get("message", json.dumps(detail))
            except Exception:
                detail = body or e.reason

            if e.code in (429, 503, 408) and attempt < 2:
                wait = int(e.headers.get("Retry-After", 5))
                print(f"  rate-limited, waiting {wait}s...", file=sys.stderr)
                time.sleep(wait)
                continue
            raise APIError(e.code, detail)
        except urllib.error.URLError as e:
            raise APIError(0, f"network error: {e.reason}")
    raise APIError(0, "exhausted retries")


def api_get_or_exit(path, params=None):
    """Like api_get but exits on failure."""
    try:
        return api_get(path, params)
    except APIError as e:
        msg = f"error {e.code}: {e.detail}"
        if e.code == 401:
            msg += "\n  check your API key in $TRANSCRIPTAPI_KEY or " + str(KEY_FILE)
        elif e.code == 402:
            msg += "\n  top up credits at https://transcriptapi.com/top-up"
        sys.exit(msg)


def fmt_transcript_text(data, with_timestamps=False):
    """Convert transcript JSON segments to readable text."""
    transcript = data.get("transcript", [])
    if isinstance(transcript, str):
        return transcript
    parts = []
    for seg in transcript:
        if with_timestamps:
            t = int(seg.get("start", 0))
            ts = f"[{t // 60:02d}:{t % 60:02d}]"
            parts.append(f"{ts} {seg.get('text', '')}")
        else:
            parts.append(seg.get("text", ""))
    return ("\n" if with_timestamps else " ").join(parts)


def video_id_of(item):
    """Item id field varies (videoId/video_id/id) across endpoints."""
    return item.get("videoId") or item.get("video_id") or item.get("id") or ""


def safe_filename(name, maxlen=80):
    name = re.sub(r"[^\w\s-]", "", name).strip()
    name = re.sub(r"\s+", "_", name)
    return name[:maxlen] or "untitled"


def write_output(text, output):
    if output:
        Path(output).write_text(text)
        print(f"wrote {output}", file=sys.stderr)
    else:
        sys.stdout.write(text)
        if not text.endswith("\n"):
            sys.stdout.write("\n")


# --- commands -----------------------------------------------------------

def cmd_video(args):
    params = {
        "video_url": args.url,
        "include_timestamp": "true" if args.timestamps else "false",
        "send_metadata": "true" if args.metadata else "false",
        "format": "json",
    }
    data = api_get_or_exit("/youtube/transcript", params)

    if args.json:
        out = json.dumps(data, indent=2, ensure_ascii=False)
    else:
        body = fmt_transcript_text(data, with_timestamps=args.timestamps)
        if args.metadata and "metadata" in data:
            m = data["metadata"]
            header = (
                f"# {m.get('title', '')}\n"
                f"by {m.get('author_name', '')}\n"
                f"{m.get('author_url', '')}\n"
                f"video_id: {data.get('video_id', '')}\n"
                f"language: {data.get('language', '')}\n\n"
            )
            out = header + body
        else:
            out = body
    write_output(out, args.output)


def collect_paginated(path, first_params, limit=None):
    """Walk pagination via continuation_token. Returns list of result items."""
    items = []
    params = dict(first_params)
    while True:
        data = api_get_or_exit(path, params)
        items.extend(data.get("results", []))
        if limit and len(items) >= limit:
            return items[:limit]
        if not data.get("has_more") or not data.get("continuation_token"):
            return items
        params = {"continuation": data["continuation_token"]}


def cmd_playlist(args):
    videos = collect_paginated(
        "/youtube/playlist/videos", {"playlist": args.url}, args.limit
    )
    handle_video_batch(videos, args, source_label=f"playlist {args.url}")


def cmd_channel(args):
    if args.latest:
        data = api_get_or_exit("/youtube/channel/latest", {"channel": args.channel})
        videos = data.get("results", [])
        if args.limit:
            videos = videos[: args.limit]
    else:
        videos = collect_paginated(
            "/youtube/channel/videos", {"channel": args.channel}, args.limit
        )
    handle_video_batch(videos, args, source_label=f"channel {args.channel}")


def handle_video_batch(videos, args, source_label=""):
    if args.list_only:
        for v in videos:
            print(f"{video_id_of(v)}\t{v.get('title', '')}")
        print(f"# {len(videos)} videos in {source_label}", file=sys.stderr)
        return

    output_dir = Path(args.output_dir) if args.output_dir else None
    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)

    print(f"# fetching transcripts for {len(videos)} videos from {source_label}", file=sys.stderr)
    success = failed = 0

    for i, v in enumerate(videos, 1):
        vid = video_id_of(v)
        title = v.get("title", "untitled")
        if not vid:
            continue
        print(f"[{i}/{len(videos)}] {vid} — {title[:70]}", file=sys.stderr)

        try:
            data = api_get(
                "/youtube/transcript",
                {"video_url": vid, "include_timestamp": "false", "format": "json"},
            )
            text = fmt_transcript_text(data)
            success += 1
        except APIError as e:
            print(f"  ! skipped ({e.code}): {e.detail}", file=sys.stderr)
            failed += 1
            continue

        body = (
            f"# {title}\n"
            f"https://youtube.com/watch?v={vid}\n\n"
            f"{text}\n"
        )
        if output_dir:
            fname = output_dir / f"{vid}_{safe_filename(title)}.txt"
            fname.write_text(body)
        else:
            sys.stdout.write("\n" + "=" * 80 + "\n")
            sys.stdout.write(body)

    print(f"# done: {success} ok, {failed} failed", file=sys.stderr)


def cmd_search(args):
    params = {"q": args.query, "type": args.type, "limit": args.limit}
    data = api_get_or_exit("/youtube/search", params)
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return
    for r in data.get("results", []):
        if args.type == "channel":
            cid = r.get("channelId") or r.get("channel_id") or ""
            title = r.get("title", "")
            subs = r.get("subscriberCountText") or r.get("subscriber_count") or ""
            print(f"{cid}\t{subs}\t{title}")
        else:
            vid = video_id_of(r)
            title = r.get("title", "")
            views = r.get("viewCountText") or r.get("view_count") or ""
            channel = r.get("channelTitle") or r.get("channelHandle") or ""
            print(f"{vid}\t{views}\t{channel}\t{title}")


def cmd_latest(args):
    data = api_get_or_exit("/youtube/channel/latest", {"channel": args.channel})
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return
    for v in data.get("results", []):
        vid = video_id_of(v)
        title = v.get("title", "")
        published = v.get("published", "")
        print(f"{vid}\t{published}\t{title}")


def cmd_resolve(args):
    data = api_get_or_exit("/youtube/channel/resolve", {"input": args.input})
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(data.get("channel_id", ""))


# --- argparse wiring ----------------------------------------------------

def main():
    p = argparse.ArgumentParser(
        prog="transcript",
        description="TranscriptAPI.com CLI — fetch YouTube transcripts, playlists, channels.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    pv = sub.add_parser("video", help="transcript for a single video")
    pv.add_argument("url", help="YouTube URL or 11-char video ID")
    pv.add_argument("--json", action="store_true", help="output raw JSON")
    pv.add_argument("--timestamps", action="store_true", help="include [mm:ss] timestamps")
    pv.add_argument("--metadata", action="store_true", help="prepend title/author")
    pv.add_argument("-o", "--output", help="save to file (default: stdout)")
    pv.set_defaults(func=cmd_video)

    pp = sub.add_parser("playlist", help="transcripts for all videos in a playlist")
    pp.add_argument("url", help="playlist URL or ID (PL.../UU.../LL.../FL.../OL...)")
    pp.add_argument("--limit", type=int, help="max videos to process")
    pp.add_argument("--list-only", action="store_true", help="only list videos, don't fetch transcripts")
    pp.add_argument("--output-dir", help="save each transcript as a separate file")
    pp.set_defaults(func=cmd_playlist)

    pc = sub.add_parser("channel", help="transcripts for videos from a channel")
    pc.add_argument("channel", help="@handle, channel URL, or UC... ID")
    pc.add_argument("--latest", action="store_true", help="use free RSS endpoint (last 15 videos)")
    pc.add_argument("--limit", type=int, help="max videos to process")
    pc.add_argument("--list-only", action="store_true")
    pc.add_argument("--output-dir", help="save each transcript as a separate file")
    pc.set_defaults(func=cmd_channel)

    ps = sub.add_parser("search", help="search YouTube videos or channels")
    ps.add_argument("query")
    ps.add_argument("--type", choices=["video", "channel"], default="video")
    ps.add_argument("--limit", type=int, default=20)
    ps.add_argument("--json", action="store_true")
    ps.set_defaults(func=cmd_search)

    pl = sub.add_parser("latest", help="latest 15 videos from a channel (free endpoint)")
    pl.add_argument("channel", help="@handle, channel URL, or UC... ID")
    pl.add_argument("--json", action="store_true")
    pl.set_defaults(func=cmd_latest)

    pr = sub.add_parser("resolve", help="resolve @handle/URL to UC... channel ID (free)")
    pr.add_argument("input", help="@handle, channel URL, or UC... ID")
    pr.add_argument("--json", action="store_true")
    pr.set_defaults(func=cmd_resolve)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
