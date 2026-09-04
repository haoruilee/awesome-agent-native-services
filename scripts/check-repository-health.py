#!/usr/bin/env python3
"""Check deterministic repository links, inventory, freshness, and public URLs."""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import re
import ssl
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
URL_RE = re.compile(r"https?://[^\s<>\"'`]+")
AUDIT_DATE_RE = re.compile(
    r"^# Research & Freshness Audit\s+[—-]\s+(\d{4}-\d{2}-\d{2})\s*$",
    re.MULTILINE,
)
PROTECTED_STATUSES = {400, 401, 403, 405, 406, 418, 425, 429, 451}


@dataclass(frozen=True)
class LinkResult:
    url: str
    status: int | None
    result: str
    detail: str


def repository_text_files() -> Iterable[Path]:
    ignored_parts = {".git", "_site", "vendor", "node_modules", "_site_test"}
    for suffix in ("*.md", "*.txt"):
        for path in ROOT.rglob(suffix):
            if not ignored_parts.intersection(path.relative_to(ROOT).parts):
                yield path


def clean_destination(raw: str) -> str:
    destination = raw.strip()
    if destination.startswith("<") and ">" in destination:
        destination = destination[1 : destination.index(">")]
    else:
        destination = destination.split(maxsplit=1)[0]
    return destination


def check_local_links() -> list[str]:
    failures: list[str] = []
    checked = 0

    for source in sorted(set(repository_text_files())):
        text = source.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            destination = clean_destination(match.group(1))
            if not destination or destination.startswith(("#", "mailto:")):
                continue
            if "{" in destination or "<" in destination:
                continue

            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc:
                continue

            target_text = unquote(parsed.path)
            if not target_text:
                continue
            # Contribution/skill templates intentionally show paths as they will
            # appear inside a future services/<category>/<service>.md file.
            relative_source = source.relative_to(ROOT)
            if (
                relative_source == Path("CONTRIBUTING.md")
                or relative_source == Path(".skills/add-to-awesome-list/SKILL.md")
            ) and target_text in {"README.md", "../README.md"}:
                continue
            if target_text.startswith("../../issues"):
                continue
            if target_text.startswith("../../blob/main/"):
                target = ROOT / target_text.removeprefix("../../blob/main/")
            elif target_text.startswith("/"):
                # Root-relative links are site routes and are validated after Jekyll.
                continue
            else:
                target = source.parent / target_text

            checked += 1
            if not target.exists():
                failures.append(f"{relative_source}: missing local target {destination}")

    services = sorted(
        path
        for path in (ROOT / "services").glob("*/*.md")
        if path.name != "README.md"
    )
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for service in services:
        category_readme = service.parent / "README.md"
        if not category_readme.is_file():
            failures.append(f"{service.parent.relative_to(ROOT)}: missing README.md")
            continue
        category_text = category_readme.read_text(encoding="utf-8")
        if f"]({service.name})" not in category_text:
            failures.append(
                f"{category_readme.relative_to(ROOT)}: does not link {service.name}"
            )
        if service.relative_to(ROOT).as_posix() not in root_readme:
            failures.append(f"README.md: does not link {service.relative_to(ROOT)}")

    catalog_version_match = re.search(
        r'^version:\s*["\']?([^"\'\n]+)',
        (ROOT / "skill.md").read_text(encoding="utf-8"),
        re.MULTILINE,
    )
    catalog_version = catalog_version_match.group(1) if catalog_version_match else None
    skill_directories = sorted(
        path for path in (ROOT / ".skills").iterdir() if (path / "SKILL.md").is_file()
    )
    for directory in skill_directories:
        skill_text = (directory / "SKILL.md").read_text(encoding="utf-8")
        name_match = re.search(r"^name:\s*(.+?)\s*$", skill_text, re.MULTILINE)
        version_match = re.search(
            r'^\s+catalog-version:\s*["\']?([^"\'\n]+)', skill_text, re.MULTILINE
        )
        if not name_match or name_match.group(1) != directory.name:
            failures.append(f"{directory.relative_to(ROOT)}/SKILL.md: name does not match slug")
        if not catalog_version or not version_match or version_match.group(1) != catalog_version:
            failures.append(
                f"{directory.relative_to(ROOT)}/SKILL.md: catalog-version does not match skill.md"
            )

    if failures:
        return failures
    print(f"Local links and inventory passed: {checked} links, {len(services)} services")
    return []


def check_site_directory(site_dir: Path) -> list[str]:
    failures: list[str] = []
    required = {
        "index.html": "HTML home page",
        "llms.txt": "LLM discovery manifest",
        "skill.md": "agent onboarding document",
        "catalog.json": "machine catalog",
        "catalog.schema.json": "catalog schema",
        "robots.txt": "crawler policy",
        "sitemap.xml": "site map",
        "assets/search-index.json": "client search index",
    }
    for relative, label in required.items():
        path = site_dir / relative
        if not path.is_file() or path.stat().st_size == 0:
            failures.append(f"{site_dir}/{relative}: missing or empty {label}")

    for relative in ("catalog.json", "catalog.schema.json"):
        path = site_dir / relative
        if path.is_file():
            try:
                value = json.loads(path.read_text(encoding="utf-8"))
                if not isinstance(value, dict) or not value:
                    raise ValueError("expected a non-empty JSON object")
            except (json.JSONDecodeError, UnicodeDecodeError, ValueError) as error:
                failures.append(f"{path}: invalid JSON: {error}")

    search_index_path = site_dir / "assets" / "search-index.json"
    if search_index_path.is_file():
        try:
            index = json.loads(search_index_path.read_text(encoding="utf-8"))
            services = index.get("services") if isinstance(index, dict) else None
            if not isinstance(services, list) or not services:
                raise ValueError("expected a non-empty services list")
            if index.get("count") != len(services):
                raise ValueError("count does not match services")
            required = {
                "id",
                "slug",
                "name",
                "tagline",
                "category",
                "website",
                "repository",
                "dossier",
                "mcp_status",
                "url_onboarding",
                "haystack",
            }
            first = services[0]
            if not isinstance(first, dict) or not required.issubset(first):
                raise ValueError("search records are missing required fields")
        except (json.JSONDecodeError, UnicodeDecodeError, ValueError) as error:
            failures.append(f"{search_index_path}: invalid search index: {error}")

    source_categories = {
        path.name for path in (ROOT / "services").iterdir() if path.is_dir()
    }
    built_categories = {
        path.name
        for path in (site_dir / "categories").glob("*.html")
        if path.name != "index.html"
    } | {
        path.parent.name
        for path in (site_dir / "categories").glob("*/index.html")
    }
    built_categories = {
        name.removesuffix(".html") for name in built_categories
    }
    missing_categories = sorted(source_categories - built_categories)
    if missing_categories:
        failures.append(
            "built site is missing category routes: " + ", ".join(missing_categories)
        )

    if not failures:
        print(
            "Built agent endpoints passed: "
            f"{len(required)} endpoints, {len(source_categories)} category routes"
        )
    return failures


def check_freshness(max_days: int) -> list[str]:
    audit_path = ROOT / "RESEARCH_AUDIT.md"
    text = audit_path.read_text(encoding="utf-8")
    match = AUDIT_DATE_RE.search(text)
    if not match:
        return ["RESEARCH_AUDIT.md: missing dated freshness-audit heading"]
    audit_date = dt.date.fromisoformat(match.group(1))
    age = (dt.datetime.now(dt.timezone.utc).date() - audit_date).days
    if age < 0:
        return [f"RESEARCH_AUDIT.md: audit date is {abs(age)} days in the future"]
    if age > max_days:
        return [
            f"RESEARCH_AUDIT.md: freshness audit is {age} days old "
            f"(maximum {max_days})"
        ]
    failures: list[str] = []
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    verified = [service for service in catalog["services"] if service["verified_at"]]
    recent_signals = [
        service for service in catalog["services"] if service["latest_month_signal"]
    ]
    for service in recent_signals:
        if not service["verified_at"] or not service["verification_sources"]:
            failures.append(f"{service['id']}: latest-month signal lacks source-backed verification")
        elif service["lifecycle_status"] != "active":
            failures.append(f"{service['id']}: verified latest-month signal is not active")
    for service in verified:
        verified_date = dt.date.fromisoformat(service["verified_at"])
        verified_age = (dt.datetime.now(dt.timezone.utc).date() - verified_date).days
        if verified_age < 0:
            failures.append(f"{service['id']}: verified_at is in the future")
        elif verified_age > max_days:
            failures.append(
                f"{service['id']}: verification is {verified_age} days old "
                f"(maximum {max_days})"
            )
    if failures:
        return failures
    print(f"Research freshness passed: {age} days old (maximum {max_days})")
    print(
        "Service verification passed: "
        f"{len(verified)} source-backed records; {len(recent_signals)} latest-month signals"
    )
    return []


def trim_url(url: str) -> str:
    url = url.rstrip(".,;:!?")
    while url.endswith(")") and url.count("(") < url.count(")"):
        url = url[:-1]
    return url


def is_live_external_url(url: str) -> bool:
    """Skip local/self-host examples that are not public catalog dependencies."""
    if "example.com" in url:
        return False
    host = (urlsplit(url).hostname or "").lower()
    return host not in {"localhost", "127.0.0.1", "::1"}


def canonical_service_urls() -> list[str]:
    urls: set[str] = set()
    heading_re = re.compile(
        r"^## Official (?:Website|Repo)\s*$\n(.*?)(?=^---\s*$|^##\s)",
        re.MULTILINE | re.DOTALL,
    )
    for path in sorted((ROOT / "services").glob("*/*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        for block in heading_re.findall(text):
            match = URL_RE.search(block)
            if match:
                urls.add(trim_url(match.group(0)))
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    for service in catalog["services"]:
        for url in (
            service.get("website"),
            service.get("repository"),
            service.get("onboarding", {}).get("url"),
            *service.get("verification_sources", []),
        ):
            if url:
                urls.add(trim_url(url))
    return sorted(url for url in urls if is_live_external_url(url))


def request_status(url: str, method: str, timeout: int) -> tuple[int, str]:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (compatible; AgentNativeCatalogLinkAudit/1.0; "
            "+https://lihaorui.com/awesome-agent-native-services/)"
        ),
        "Accept": "text/html,application/json,text/plain,*/*;q=0.5",
    }
    if method == "GET":
        headers["Range"] = "bytes=0-0"
    request = Request(
        url,
        method=method,
        headers=headers,
    )
    try:
        with urlopen(request, timeout=timeout, context=ssl.create_default_context()) as response:
            return response.status, response.geturl()
    except HTTPError as error:
        return error.code, error.geturl()


def check_external_url(url: str, timeout: int, retries: int) -> LinkResult:
    last_detail = "unknown error"
    for attempt in range(retries + 1):
        try:
            status, final_url = request_status(url, "HEAD", timeout)
            if status >= 400 and status not in PROTECTED_STATUSES:
                status, final_url = request_status(url, "GET", timeout)
            if 200 <= status < 400:
                return LinkResult(url, status, "ok", final_url)
            if status in PROTECTED_STATUSES:
                return LinkResult(url, status, "protected", final_url)
            last_detail = f"HTTP {status} ({final_url})"
        except (TimeoutError, URLError, OSError, ValueError) as error:
            last_detail = str(error)

        if attempt < retries:
            time.sleep(0.5 * (attempt + 1))

    return LinkResult(url, None, "failed", last_detail)


def check_external_links(
    *, workers: int, timeout: int, retries: int, report_path: Path | None
) -> list[str]:
    urls = canonical_service_urls()
    results: list[LinkResult] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_urls = {
            executor.submit(check_external_url, url, timeout, retries): url for url in urls
        }
        for future in concurrent.futures.as_completed(future_urls):
            result = future.result()
            results.append(result)
            prefix = {"ok": "OK", "protected": "ACCESS", "failed": "FAIL"}[
                result.result
            ]
            print(f"{prefix:6} {result.url} — {result.detail}")

    results.sort(key=lambda result: result.url)
    summary = {
        "checked_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "summary": {
            "checked": len(results),
            "ok": sum(result.result == "ok" for result in results),
            "protected": sum(result.result == "protected" for result in results),
            "failed": sum(result.result == "failed" for result in results),
        },
        "results": [asdict(result) for result in results],
    }
    if report_path:
        report_path.write_text(
            json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    print("External agent-surface summary: " + json.dumps(summary["summary"]))
    return [
        f"{result.url}: {result.detail}"
        for result in results
        if result.result == "failed"
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local", action="store_true", help="check local links and inventory")
    parser.add_argument(
        "--site-dir", type=Path, help="check required files in a built Jekyll directory"
    )
    parser.add_argument(
        "--external-canonical",
        action="store_true",
        help="check canonical websites, repositories, onboarding, and evidence URLs",
    )
    parser.add_argument(
        "--freshness-max-days",
        type=int,
        metavar="DAYS",
        help="fail when RESEARCH_AUDIT.md is older than DAYS",
    )
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--timeout", type=int, default=15)
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument("--report-json", type=Path)
    args = parser.parse_args()
    if not any(
        (
            args.local,
            args.site_dir,
            args.external_canonical,
            args.freshness_max_days is not None,
        )
    ):
        parser.error("select at least one check mode")
    if args.workers < 1 or args.timeout < 1 or args.retries < 0:
        parser.error("workers/timeout must be positive and retries cannot be negative")
    return args


def main() -> int:
    args = parse_args()
    failures: list[str] = []
    if args.local:
        failures.extend(check_local_links())
    if args.site_dir:
        failures.extend(check_site_directory(args.site_dir.resolve()))
    if args.freshness_max_days is not None:
        failures.extend(check_freshness(args.freshness_max_days))
    if args.external_canonical:
        failures.extend(
            check_external_links(
                workers=args.workers,
                timeout=args.timeout,
                retries=args.retries,
                report_path=args.report_json,
            )
        )

    if failures:
        print("\nRepository health checks failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
