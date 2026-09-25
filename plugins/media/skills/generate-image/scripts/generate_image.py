#!/usr/bin/env python3
"""Generate an image with an OpenAI image model through OpenRouter.

Reads the key from OPENROUTER_API_KEY. Never pass the key on the command line.

  python3 generate_image.py --prompt "..." --out hero.png [--aspect-ratio 16:9]
      [--reference ref.png ...] [--model openai/gpt-5.4-image-2]

Tries the primary model, then the fallback model, then exits non-zero.
"""
import argparse
import base64
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.request

ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"
PRIMARY = os.environ.get("OPENROUTER_IMAGE_MODEL", "openai/gpt-5.4-image-2")
FALLBACK = os.environ.get("OPENROUTER_IMAGE_FALLBACK", "openai/gpt-5-image")


def data_url(path):
    mime = mimetypes.guess_type(path)[0] or "image/png"
    with open(path, "rb") as f:
        return f"data:{mime};base64,{base64.b64encode(f.read()).decode()}"


def generate(model, prompt, refs, aspect, key, timeout):
    if aspect:
        # ponytail: aspect sent both as image_config and in the prompt; models differ in which they honour
        prompt = f"{prompt}\n\nAspect ratio: {aspect}."
    content = [{"type": "text", "text": prompt}]
    content += [{"type": "image_url", "image_url": {"url": data_url(r)}} for r in refs]
    body = {
        "model": model,
        "messages": [{"role": "user", "content": content}],
        "modalities": ["image", "text"],
    }
    if aspect:
        body["image_config"] = {"aspect_ratio": aspect}
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(body).encode(),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "X-Title": "generate-image skill",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.load(resp)
    images = (data.get("choices") or [{}])[0].get("message", {}).get("images") or []
    if not images:
        raise RuntimeError(f"no image in response: {json.dumps(data)[:400]}")
    url = images[0]["image_url"]["url"]
    if url.startswith("data:"):
        return base64.b64decode(url.split(",", 1)[1])
    with urllib.request.urlopen(url, timeout=timeout) as resp:
        return resp.read()


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--prompt", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--aspect-ratio", help="e.g. 1:1, 3:2, 2:3, 16:9")
    p.add_argument("--reference", action="append", default=[], help="reference image path, repeatable")
    p.add_argument("--model", help=f"override model (default {PRIMARY}, fallback {FALLBACK})")
    p.add_argument("--no-fallback", action="store_true")
    p.add_argument("--timeout", type=int, default=300)
    a = p.parse_args()

    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        sys.exit("OPENROUTER_API_KEY is not set. Add `export OPENROUTER_API_KEY=...` to ~/.zshrc.")

    models = [a.model or PRIMARY] + ([] if a.no_fallback or a.model else [FALLBACK])
    for model in models:
        try:
            img = generate(model, a.prompt, a.reference, a.aspect_ratio, key, a.timeout)
        except (urllib.error.URLError, RuntimeError, KeyError, TimeoutError) as e:
            detail = e.read().decode()[:400] if isinstance(e, urllib.error.HTTPError) else str(e)
            print(f"{model} failed: {detail}", file=sys.stderr)
            continue
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        with open(a.out, "wb") as f:
            f.write(img)
        print(f"saved {a.out} ({len(img)} bytes) via {model}")
        return
    sys.exit(1)


if __name__ == "__main__":
    main()
