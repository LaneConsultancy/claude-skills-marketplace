#!/usr/bin/env python3
"""Scheduled SERP rank tracker using DataForSEO.

Usage: python3 track.py /path/to/keywords.json
Config format (JSON list):
  [{"keyword": "mobile mechanic york", "domain": "mobilemechanicyork.co.uk",
    "location": "York,England,United Kingdom", "device": "mobile"}]
Env: DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD (or a .env file next to the config).
Appends one JSONL row per keyword to rank-log.jsonl next to the config.
Prints a summary table; flags moves in/out of top 3 vs previous run.
"""
import sys, os, json, base64, pathlib, urllib.request
from datetime import date

API = "https://api.dataforseo.com/v3/serp/google/organic/live/advanced"

def load_env(cfg_dir):
    for d in [cfg_dir, *cfg_dir.parents]:
        envfile = d / ".env"
        if envfile.is_file():
            for line in envfile.read_text().splitlines():
                if "=" in line and not line.lstrip().startswith("#"):
                    k, _, v = line.partition("=")
                    os.environ.setdefault(k.strip(), v.strip())

def check(auth, kw):
    body = json.dumps([{
        "keyword": kw["keyword"],
        "location_name": kw.get("location", "United Kingdom"),
        "language_code": "en",
        "device": kw.get("device", "mobile"),
        "depth": 30,
    }]).encode()
    req = urllib.request.Request(API, data=body, headers={
        "Authorization": f"Basic {auth}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    task = data["tasks"][0]
    if task["status_code"] != 20000:
        raise RuntimeError(f"{kw['keyword']}: {task['status_message']}")
    items = [i for i in (task["result"][0]["items"] or []) if i.get("type") == "organic"]
    dom = kw["domain"].lower().removeprefix("www.")
    pos = absolute = None
    for n, i in enumerate(items, 1):
        if i.get("domain", "").lower().removeprefix("www.") == dom:
            pos, absolute = n, i["rank_absolute"]  # organic rank vs full-SERP rank
            break
    top3 = [i.get("domain") for i in items[:3]]
    return {"date": str(date.today()), "keyword": kw["keyword"], "domain": dom,
            "position": pos, "absolute": absolute, "top3": top3}

def main(cfg_path):
    cfg_path = pathlib.Path(cfg_path).resolve()
    load_env(cfg_path.parent)
    login, pw = os.environ.get("DATAFORSEO_LOGIN"), os.environ.get("DATAFORSEO_PASSWORD")
    if not (login and pw):
        sys.exit("DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD not set")
    auth = base64.b64encode(f"{login}:{pw}".encode()).decode()
    log_path = cfg_path.parent / "rank-log.jsonl"
    prev = {}
    if log_path.is_file():
        for line in log_path.read_text().splitlines():
            row = json.loads(line)
            prev[row["keyword"]] = row  # last row per keyword wins
    rows = []
    for kw in json.loads(cfg_path.read_text()):
        row = check(auth, kw)
        rows.append(row)
        with open(log_path, "a") as f:
            f.write(json.dumps(row) + "\n")
    print(f"{'keyword':<40} {'pos':>4} {'prev':>4}  top3")
    alerts = []
    for r in rows:
        p = prev.get(r["keyword"], {}).get("position")
        print(f"{r['keyword']:<40} {str(r['position'] or '-'):>4} {str(p or '-'):>4}  {', '.join(filter(None, r['top3']))}")
        was3, now3 = (p is not None and p <= 3), (r["position"] is not None and r["position"] <= 3)
        if p is not None and was3 != now3:
            alerts.append(f"{'ENTERED' if now3 else 'LEFT'} TOP 3: {r['keyword']} ({p} -> {r['position']})")
    for a in alerts:
        print("ALERT:", a)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
