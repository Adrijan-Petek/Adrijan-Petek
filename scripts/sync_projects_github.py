#!/usr/bin/env python3
"""
Populate `config.json["projects"]` from GitHub repos.

Notes:
- Uses only Python stdlib.
- Requires network access to api.github.com (CI has it; some sandboxes don't).
- Optional: set GITHUB_TOKEN to avoid rate limits.

Usage:
  python3 scripts/sync_projects_github.py --user Adrijan-Petek --top 12
"""

import argparse
import json
import os
import sys
import urllib.request
from typing import Optional


def fetch_repos(user: str, token: Optional[str] = None):
    url = f"https://api.github.com/users/{user}/repos?per_page=100&sort=updated"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "profile-generator")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", required=True)
    parser.add_argument("--top", type=int, default=12)
    parser.add_argument("--config", default="config.json")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    repos = fetch_repos(args.user, token=token)

    # Keep public, non-fork repos; prioritize stars then recency.
    filtered = [
        r
        for r in repos
        if not r.get("private")
        and not r.get("fork")
        and r.get("html_url")
        and r.get("name")
    ]

    filtered.sort(
        key=lambda r: (r.get("stargazers_count", 0), r.get("pushed_at") or ""),
        reverse=True,
    )

    projects = []
    for r in filtered[: args.top]:
        projects.append(
            {
                "name": r["name"],
                "url": r["html_url"],
                "description": (r.get("description") or "").strip() or "—",
            }
        )

    with open(args.config, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    cfg["projects"] = projects

    with open(args.config, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=4, ensure_ascii=False)
        f.write("\n")

    print(f"Wrote {len(projects)} projects to {args.config}")


if __name__ == "__main__":
    raise SystemExit(main())
