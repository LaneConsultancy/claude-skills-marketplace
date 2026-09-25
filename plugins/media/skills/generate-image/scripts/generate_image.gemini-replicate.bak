#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from PIL import Image


SKILL_DIR = Path(__file__).resolve().parents[1]
SKILL_MD = SKILL_DIR / "SKILL.md"
GEMINI_MODEL = "gemini-3.1-flash-image-preview"
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
REPLICATE_ENDPOINT = "https://api.replicate.com/v1/models/google/nano-banana-pro/predictions"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate an image using the local generate-image skill provider.")
    parser.add_argument("--prompt", required=True, help="Image prompt.")
    parser.add_argument("--out", required=True, help="Output image path.")
    parser.add_argument("--aspect-ratio", default=None, help="Desired aspect ratio, e.g. 1:1, 4:5, 9:16, 16:9.")
    parser.add_argument("--resolution", default="2K", choices=["1K", "2K", "4K"], help="Prompt-level quality hint.")
    parser.add_argument("--reference", action="append", default=[], help="Optional reference image path. May be passed multiple times.")
    parser.add_argument("--fallback", action="store_true", help="Use Replicate fallback if Gemini fails.")
    parser.add_argument("--timeout", type=int, default=180, help="HTTP timeout in seconds.")
    return parser.parse_args()


def find_token(pattern: str) -> str | None:
    if not SKILL_MD.exists():
        return None
    text = SKILL_MD.read_text(encoding="utf-8", errors="ignore")
    match = re.search(pattern, text)
    return match.group(0) if match else None


def gemini_key() -> str | None:
    return os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or find_token(r"AIza[0-9A-Za-z_\-]+")


def replicate_token() -> str | None:
    return os.environ.get("REPLICATE_API_TOKEN") or find_token(r"r8_[0-9A-Za-z_\-]+")


def prompt_with_params(prompt: str, aspect_ratio: str | None, resolution: str) -> str:
    parts = [prompt.strip()]
    if resolution:
        parts.append(f"{resolution} quality.")
    if aspect_ratio:
        parts.append(
            f"Use a {aspect_ratio} canvas composition. This is a layout instruction only; do not render the aspect ratio or any technical instruction as visible text."
        )
    return " ".join(parts)


def inline_reference(path: str) -> dict[str, dict[str, str]]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)
    mime = mimetypes.guess_type(str(p))[0] or "image/png"
    data = base64.b64encode(p.read_bytes()).decode("ascii")
    return {"inlineData": {"mimeType": mime, "data": data}}


def request_json(url: str, payload: dict, headers: dict[str, str], timeout: int) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            return json.loads(res.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc


def generate_gemini(prompt: str, out: Path, references: list[str], timeout: int) -> None:
    key = gemini_key()
    if not key:
        raise RuntimeError("Missing GEMINI_API_KEY or GOOGLE_API_KEY, and no local Gemini token found in SKILL.md.")

    parts: list[dict] = [{"text": prompt}]
    parts.extend(inline_reference(ref) for ref in references)
    payload = {
        "contents": [{"parts": parts}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]},
    }
    body = request_json(
        GEMINI_ENDPOINT,
        payload,
        {"Content-Type": "application/json", "x-goog-api-key": key},
        timeout,
    )
    for candidate in body.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_bytes(base64.b64decode(inline["data"]))
                normalize_output_format(out)
                return
    raise RuntimeError(f"Gemini returned no image. Response starts: {json.dumps(body)[:1000]}")


def generate_replicate(prompt: str, out: Path, aspect_ratio: str | None, timeout: int) -> None:
    token = replicate_token()
    if not token:
        raise RuntimeError("Missing REPLICATE_API_TOKEN and no local Replicate token found in SKILL.md.")
    payload = {
        "input": {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio or "1:1",
            "output_format": out.suffix.lstrip(".") or "png",
        }
    }
    body = request_json(
        REPLICATE_ENDPOINT,
        payload,
        {"Content-Type": "application/json", "Authorization": f"Bearer {token}", "Prefer": "wait"},
        timeout,
    )
    get_url = body.get("urls", {}).get("get")
    status = body.get("status")
    for _ in range(90):
        if status == "succeeded":
            output = body.get("output")
            url = output[0] if isinstance(output, list) else output
            if not url:
                raise RuntimeError(f"Replicate succeeded without output: {json.dumps(body)[:1000]}")
            out.parent.mkdir(parents=True, exist_ok=True)
            with urllib.request.urlopen(url, timeout=timeout) as res:
                out.write_bytes(res.read())
            normalize_output_format(out)
            return
        if status in {"failed", "canceled"}:
            raise RuntimeError(f"Replicate failed: {json.dumps(body)[:1000]}")
        if not get_url:
            raise RuntimeError(f"Replicate response missing polling URL: {json.dumps(body)[:1000]}")
        time.sleep(2)
        req = urllib.request.Request(get_url, headers={"Authorization": f"Bearer {token}"})
        with urllib.request.urlopen(req, timeout=timeout) as res:
            body = json.loads(res.read().decode("utf-8"))
        status = body.get("status")
    raise RuntimeError("Replicate timed out while polling.")


def normalize_output_format(out: Path) -> None:
    suffix = out.suffix.lower()
    if suffix not in {".png", ".jpg", ".jpeg", ".webp"}:
        return
    try:
        im = Image.open(out)
        if suffix == ".png":
            im.save(out, format="PNG")
        elif suffix in {".jpg", ".jpeg"}:
            im.convert("RGB").save(out, format="JPEG", quality=94, optimize=True)
        elif suffix == ".webp":
            im.save(out, format="WEBP", quality=94, method=6)
    except Exception:
        # Keep the provider output if Pillow cannot decode or rewrite it.
        return


def main() -> int:
    args = parse_args()
    out = Path(args.out).expanduser().resolve()
    prompt = prompt_with_params(args.prompt, args.aspect_ratio, args.resolution)
    try:
        generate_gemini(prompt, out, args.reference, args.timeout)
        print(out)
        return 0
    except Exception as gemini_error:
        if not args.fallback:
            print(f"Gemini generation failed: {gemini_error}", file=sys.stderr)
            return 1
        try:
            generate_replicate(prompt, out, args.aspect_ratio, args.timeout)
            print(out)
            return 0
        except Exception as replicate_error:
            print(f"Gemini generation failed: {gemini_error}", file=sys.stderr)
            print(f"Replicate fallback failed: {replicate_error}", file=sys.stderr)
            return 1


if __name__ == "__main__":
    raise SystemExit(main())
