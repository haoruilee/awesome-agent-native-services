#!/usr/bin/env python3
"""Refresh editorial/home/github-stars.json from the GitHub API.

The site build does not call GitHub. It renders the committed snapshot so CI
stays reproducible. Run this when the homepage list changes or the counts
should move, then regenerate the site:

    python3 scripts/refresh-github-stars.py
    bash scripts/build-github-pages.sh

Set GITHUB_TOKEN or GH_TOKEN if the anonymous rate limit is too low.
The script reads stargazers_count for the repository named by each dossier
in editorial/home/attention.md. It does not invent a count, and it leaves
the commentary files untouched. A repository the API cannot fetch fails the
run; remove that service from attention.md rather than guessing.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import home_editorial


def github_token() -> str:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""
    if token:
        return token
    try:
        import subprocess

        return subprocess.check_output(["gh", "auth", "token"], text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def fetch_repository(full_name: str, token: str) -> dict[str, object]:
    request = urllib.request.Request(
        f"https://api.github.com/repos/{full_name}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-agent-native-services-star-snapshot",
            "X-GitHub-Api-Version": "2022-11-28",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")[:400]
        raise SystemExit(
            f"GitHub API {error.code} for {full_name}. "
            "Remove the service from editorial/home/attention.md if it has no "
            f"public repository. {detail}"
        ) from error
    except urllib.error.URLError as error:
        raise SystemExit(f"Could not reach GitHub for {full_name}: {error.reason}") from error
    if not isinstance(payload, dict) or "stargazers_count" not in payload:
        raise SystemExit(f"GitHub response for {full_name} did not include stargazers_count")
    count = payload["stargazers_count"]
    canonical = payload.get("full_name")
    html_url = payload.get("html_url")
    if not isinstance(count, int) or not isinstance(canonical, str) or not isinstance(html_url, str):
        raise SystemExit(f"GitHub response for {full_name} had an unexpected shape")
    if canonical.casefold() != full_name.casefold():
        raise SystemExit(
            f"Refusing to record {canonical}: the dossier names {full_name}. "
            "Update the dossier if the repository moved."
        )
    return {
        "full_name": canonical,
        "html_url": html_url,
        "stargazers_count": count,
    }


def main() -> int:
    _title, _lede, items = home_editorial.parse_document(home_editorial.ATTENTION_PATH)
    token = github_token()
    repositories: dict[str, dict[str, object]] = {}
    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for item in items:
        meta = item["meta"]
        assert isinstance(meta, dict)
        slug = str(meta.get("slug", ""))
        dossier = home_editorial.service_path(slug)
        if dossier is None:
            raise SystemExit(f"{slug}: not a single service dossier")
        repo = home_editorial.counted_repository(dossier.read_text(encoding="utf-8"))
        if not repo:
            raise SystemExit(
                f"{slug}: the dossier has no GitHub Stars badge and no "
                "github.com/owner/repo URL under Official Repo. "
                "Remove it from editorial/home/attention.md."
            )
        repositories[slug] = fetch_repository(repo, token)
        recorded = repositories[slug]
        print(f"{slug}\t{recorded['full_name']}\t{recorded['stargazers_count']}")

    payload = {
        "comment": (
            "Snapshot of GitHub stargazers_count for the homepage attention "
            "section. The site build reads this file and does not call the "
            "network. Refresh with: python3 scripts/refresh-github-stars.py"
        ),
        "fetched_at": fetched_at,
        "metric": "stargazers_count",
        "api": "https://api.github.com/repos/{owner}/{repo}",
        "selection": (
            "For each slug in editorial/home/attention.md, count the repository "
            "linked from that dossier's GitHub Stars badge. If the dossier has "
            "no badge, count the first github.com/owner/repo URL under "
            "## Official Repo. These counts measure public interest in that "
            "repository, not traffic, revenue, or quality, and they are not a "
            "ranking of best."
        ),
        "refresh": "python3 scripts/refresh-github-stars.py",
        "repositories": {slug: repositories[slug] for slug in sorted(repositories)},
    }
    home_editorial.STARS_PATH.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {home_editorial.STARS_PATH.relative_to(home_editorial.ROOT)} at {fetched_at}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
