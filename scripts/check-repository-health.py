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
# 402: x402 paywalled endpoints answer Payment Required by design.
# 419: Hacker News rate-limit/anti-bot response for automated fetches.
PROTECTED_STATUSES = {400, 401, 402, 403, 405, 406, 418, 419, 425, 429, 451}


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
    docs_services = ROOT / "docs" / "services"
    missing_pages = [
        service.stem
        for service in services
        if not (docs_services / service.stem / "index.md").is_file()
    ]
    if missing_pages:
        sample = ", ".join(missing_pages[:12])
        more = "" if len(missing_pages) <= 12 else f" (+{len(missing_pages) - 12} more)"
        failures.append(
            "docs/services is missing introduction pages: " + sample + more
        )
        return failures

    failures.extend(check_service_editorials(services))
    from home_editorial import check_sources

    failures.extend(check_sources())
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
            search_fields = {
                "id",
                "slug",
                "name",
                "tagline",
                "category",
                "website",
                "repository",
                "dossier",
                "page",
                "mcp_status",
                "url_onboarding",
                "haystack",
            }
            first = services[0]
            if not isinstance(first, dict) or not search_fields.issubset(first):
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

    source_services = {
        path.stem
        for path in (ROOT / "services").glob("*/*.md")
        if path.name != "README.md"
    }
    built_services = {
        path.parent.name
        for path in (site_dir / "services").glob("*/index.html")
    } | {
        path.name.removesuffix(".html")
        for path in (site_dir / "services").glob("*.html")
        if path.name != "index.html"
    }
    missing_services = sorted(source_services - built_services)
    if missing_services:
        sample = ", ".join(missing_services[:12])
        more = "" if len(missing_services) <= 12 else f" (+{len(missing_services) - 12} more)"
        failures.append(
            "built site is missing service introduction routes: " + sample + more
        )

    failures.extend(check_editorial_pages(site_dir))
    failures.extend(check_built_service_editorials(site_dir))
    failures.extend(check_advertising_disabled(site_dir))
    from home_editorial import check_built_home

    failures.extend(check_built_home(site_dir))

    if not failures:
        print(
            "Built agent endpoints passed: "
            f"{len(required)} endpoints, {len(source_categories)} category routes, "
            f"{len(source_services)} service routes"
        )
    return failures


ADSENSE_CLIENT = "ca-pub-7668037987581637"
# Exact AdSense "code snippet" tag. One copy is allowed, and only inside <head>.
ADSENSE_VERIFICATION_LOADER = (
    '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
    f'?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>'
)
AD_HOSTS = (
    "googlesyndication.com",
    "googleads.g.doubleclick.net",
    "adservice.google.com",
)
# Quotes are optional so both enabled:true and "enabled": true fail.
ENABLED_TRUE_RE = re.compile(
    r"""(?<![A-Za-z0-9_])['"]?enabled['"]?\s*:\s*true\b""",
    re.IGNORECASE,
)
ADSENSE_PUSH_RE = re.compile(
    r"adsbygoogle\s*\.\s*push\b"
    r"|(?:window\.)?adsbygoogle\s*=\s*(?:window\.)?adsbygoogle[\s\S]{0,80}?\.push\s*\(",
    re.IGNORECASE,
)
ADSENSE_UNIT_RE = re.compile(r"<ins\b[^>]*\badsbygoogle\b", re.IGNORECASE)


def verification_loader_in_head(html: str) -> bool:
    """True when the exact verification loader appears once, inside <head>."""
    head_end = html.lower().find("</head>")
    loader_at = html.find(ADSENSE_VERIFICATION_LOADER)
    return (
        head_end >= 0
        and html.count(ADSENSE_VERIFICATION_LOADER) == 1
        and 0 <= loader_at < head_end
    )


def forbidden_ad_markup(relative: str, html: str) -> list[str]:
    """Fail closed after removing the one allowed verification loader.

    publisher.js may still contain a gated adsbygoogle.push. That file is not
    HTML, and this check does not treat it as a live unit.
    """
    failures: list[str] = []
    stripped = html.replace(ADSENSE_VERIFICATION_LOADER, "")
    stripped_lower = stripped.lower()
    for host in AD_HOSTS:
        if host in stripped_lower:
            failures.append(f"{relative} references {host}")
            break
    if (
        "pagead/js/adsbygoogle.js" in stripped_lower
        or "enable_page_level_ads" in stripped_lower
        or re.search(r"<script\b[^>]*\badsbygoogle\b", stripped_lower)
    ):
        failures.append(f"{relative} loads adsbygoogle.js or Auto ads")
    if ADSENSE_PUSH_RE.search(stripped):
        failures.append(f"{relative} calls adsbygoogle.push")
    if (
        'class="adsbygoogle"' in stripped_lower
        or "class='adsbygoogle'" in stripped_lower
        or "data-ad-client=" in stripped_lower
        or ADSENSE_UNIT_RE.search(stripped)
    ):
        failures.append(f"{relative} contains a live AdSense unit")
    if ENABLED_TRUE_RE.search(stripped):
        failures.append(f"{relative} sets AdSense enabled:true")
    return failures


def editorial_prose_words(text: str) -> int:
    """Count words in a commentary, ignoring URLs, code, and markdown marks."""
    stripped = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    stripped = re.sub(r"`[^`]+`", " ", stripped)
    stripped = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", stripped)
    stripped = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", stripped)
    stripped = re.sub(r"https?://\S+", " ", stripped)
    stripped = re.sub(r"[#>*_]+", " ", stripped)
    return len(re.findall(r"[A-Za-z][A-Za-z'’-]{1,}", stripped))


def editorial_sentences(text: str) -> list[str]:
    plain = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    plain = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", plain)
    plain = re.sub(r"[#>*_`]+", " ", plain)
    plain = re.sub(r"\s+", " ", plain).strip().lower()
    parts = re.split(r"(?<=[.!?])\s+", plain)
    sentences: list[str] = []
    for part in parts:
        words = re.findall(r"[a-z][a-z'’-]+", part)
        if len(words) >= 12:
            sentences.append(" ".join(words))
    return sentences


def service_slug_set() -> set[str]:
    return {
        path.stem
        for path in (ROOT / "services").glob("*/*.md")
        if path.name != "README.md"
    }


def guide_paths() -> set[str]:
    found: set[str] = set()
    guides = ROOT / "docs" / "guides"
    for path in guides.glob("*.md"):
        if path.name == "index.md":
            continue
        match = re.search(r"^permalink:\s*(\S+)\s*$", path.read_text(encoding="utf-8"), re.MULTILINE)
        if not match:
            continue
        permalink = match.group(1).strip('"').strip("'")
        if not permalink.endswith("/"):
            permalink += "/"
        found.add(permalink)
    return found


def check_service_editorials(services: list[Path]) -> list[str]:
    """Commentary files must name a real service and stay specific."""
    failures: list[str] = []
    directory = ROOT / "editorial" / "services"
    if not directory.is_dir():
        return failures

    slugs = service_slug_set()
    categories = {path.name for path in (ROOT / "services").iterdir() if path.is_dir()}
    guides = guide_paths()
    files = sorted(path for path in directory.glob("*.md"))
    seen_sentences: dict[str, str] = {}
    linked_services: set[str] = set()
    prior_sources = [
        *sorted((ROOT / "editorial" / "home").glob("*.md")),
        *sorted((ROOT / "editorial" / "categories").glob("*.md")),
        *sorted((ROOT / "docs" / "guides").glob("*.md")),
        ROOT / "docs" / "about.md",
        ROOT / "docs" / "editorial-policy.md",
    ]
    for source in prior_sources:
        if not source.is_file():
            continue
        for sentence in editorial_sentences(source.read_text(encoding="utf-8")):
            seen_sentences.setdefault(sentence, source.relative_to(ROOT).as_posix())

    for path in files:
        slug = path.stem
        relative = path.relative_to(ROOT).as_posix()
        if slug not in slugs:
            failures.append(f"{relative}: {slug} is not a service slug")
            continue
        text = path.read_text(encoding="utf-8")
        if text.lstrip().startswith("---"):
            failures.append(f"{relative}: commentary files must not use front matter")
        if "### Editor's take" not in text and "### Editor’s take" not in text:
            failures.append(f"{relative}: missing an Editor's take section")
        word_count = editorial_prose_words(text)
        if word_count < 350 or word_count > 700:
            failures.append(f"{relative}: {word_count} words (expected 350–700)")
        lowered = text.lower()
        for banned in (
            "we tested",
            "we measured",
            "in our testing",
            "hands-on test",
            "our benchmark",
        ):
            if banned in lowered:
                failures.append(f"{relative}: contains {banned!r}")
        if re.search(r"\$\s?\d", text):
            failures.append(f"{relative}: contains a dollar amount")
        if re.search(r"\d+(?:\.\d+)?\s*%", text):
            failures.append(f"{relative}: contains a percentage claim")
        if re.search(r"\d{1,3}(?:,\d{3})+", text):
            failures.append(f"{relative}: contains a grouped number")
        if re.search(r"\d+(?:\.\d+)?\s*(?:ms|milliseconds)\b", text, re.IGNORECASE):
            failures.append(f"{relative}: contains a latency figure")
        if re.search(r"\{\{|\{%", text):
            failures.append(f"{relative}: contains Liquid markup")
        if not re.search(r"\]\(https?://", text):
            failures.append(f"{relative}: does not link a vendor URL")

        for destination in LINK_RE.findall(text):
            cleaned = clean_destination(destination)
            parsed = urlsplit(cleaned)
            if parsed.scheme or parsed.netloc:
                continue
            route = unquote(parsed.path)
            service_match = re.fullmatch(r"/services/([a-z0-9-]+)/?", route)
            category_match = re.fullmatch(r"/categories/([a-z0-9-]+)/?", route)
            guide_match = re.fullmatch(r"/guides/([a-z0-9-]+)/?", route)
            if service_match:
                target = service_match.group(1)
                linked_services.add(target)
                if target not in slugs:
                    failures.append(f"{relative}: links unknown service /services/{target}/")
            elif category_match:
                if category_match.group(1) not in categories:
                    failures.append(
                        f"{relative}: links unknown category /categories/{category_match.group(1)}/"
                    )
            elif guide_match:
                canonical = f"/guides/{guide_match.group(1)}/"
                if canonical not in guides:
                    failures.append(f"{relative}: links unknown guide {canonical}")
            elif route.startswith("/"):
                failures.append(f"{relative}: links unrecognized site path {route}")

        page = ROOT / "docs" / "services" / slug / "index.md"
        if not page.is_file() or 'class="service-essay"' not in page.read_text(encoding="utf-8"):
            failures.append(
                f"{relative}: docs/services/{slug}/index.md is missing the rendered essay"
            )

        for sentence in editorial_sentences(text):
            previous = seen_sentences.get(sentence)
            if previous and previous != relative:
                failures.append(
                    f"{relative}: repeats a sentence also used in {previous}"
                )
            else:
                seen_sentences.setdefault(sentence, relative)

    if files and not failures:
        print(
            "Service editorials passed: "
            f"{len(files)} commentaries, {len(linked_services)} neighbor links"
        )
    return failures


def check_built_service_editorials(site_dir: Path) -> list[str]:
    """The built service page must show the commentary as HTML, not raw markdown."""
    failures: list[str] = []
    directory = ROOT / "editorial" / "services"
    if not directory.is_dir():
        return failures
    checked = 0
    for path in sorted(directory.glob("*.md")):
        built = site_dir / "services" / path.stem / "index.html"
        if not built.is_file():
            failures.append(f"built site is missing /services/{path.stem}/ for its editorial")
            continue
        html = built.read_text(encoding="utf-8", errors="ignore")
        checked += 1
        if "service-essay" not in html:
            failures.append(f"/services/{path.stem}/ is missing the editorial section")
            continue
        if "Editor" not in html:
            failures.append(f"/services/{path.stem}/ editorial did not render")
        if "### Editor" in html:
            failures.append(
                f"/services/{path.stem}/ left the editorial heading as raw markdown"
            )
    if checked and not failures:
        print(f"Built service editorials passed: {checked} pages")
    return failures


def visible_word_count(html: str) -> int:
    text = re.sub(r"(?is)<script\b.*?</script>|<style\b.*?</style>", " ", html)
    text = re.sub(r"(?is)<[^>]+>", " ", text)
    return len(re.findall(r"[A-Za-z]{2,}", text))


def check_editorial_pages(site_dir: Path) -> list[str]:
    """Guides, about, and category essays are the original prose on the site."""
    failures: list[str] = []
    required_pages = {
        "about/index.html": "https://theagentnative.com/about/",
        "editorial-policy/index.html": "https://theagentnative.com/editorial-policy/",
        "guides/index.html": "https://theagentnative.com/guides/",
    }
    for relative, loc in required_pages.items():
        path = site_dir / relative
        if not path.is_file():
            failures.append(f"built site is missing /{relative.removesuffix('index.html')}")
            continue
        if visible_word_count(path.read_text(encoding="utf-8", errors="ignore")) < 400:
            failures.append(f"/{relative} has too little visible text for an editorial page")

    guide_pages = sorted((site_dir / "guides").glob("*/index.html"))
    if len(guide_pages) < 6:
        failures.append(f"expected at least 6 guide articles, found {len(guide_pages)}")
    for path in guide_pages:
        if visible_word_count(path.read_text(encoding="utf-8", errors="ignore")) < 900:
            failures.append(f"/guides/{path.parent.name}/ is shorter than a guide article")

    collection_pages = sorted((site_dir / "categories").glob("*/index.html"))
    if len(collection_pages) < 16:
        failures.append(f"expected 16 collection essays, found {len(collection_pages)}")
    for path in collection_pages:
        html = path.read_text(encoding="utf-8", errors="ignore")
        if "collection-essay" not in html:
            failures.append(f"/categories/{path.parent.name}/ is missing its essay")

    sitemap_path = site_dir / "sitemap.xml"
    sitemap = sitemap_path.read_text(encoding="utf-8") if sitemap_path.is_file() else ""
    expected_locs = list(required_pages.values())
    expected_locs.extend(
        f"https://theagentnative.com/guides/{path.parent.name}/" for path in guide_pages
    )
    for loc in expected_locs:
        if loc not in sitemap:
            failures.append(f"sitemap.xml does not list {loc}")

    if not failures:
        print(
            "Editorial pages passed: "
            f"{len(guide_pages)} guides, {len(collection_pages)} collection essays"
        )
    return failures


def check_advertising_disabled(site_dir: Path) -> list[str]:
    """The verification loader may sit in <head>. Ad delivery stays off."""
    failures: list[str] = []
    adsense_client = ADSENSE_CLIENT
    ads_txt_record = "google.com, pub-7668037987581637, DIRECT, f08c47fec0942fa0"
    adsense_meta = f'<meta name="google-adsense-account" content="{adsense_client}">'
    slot_keys = ("home-banner", "list-banner", "in-content", "content-footer")

    ads_path = site_dir / "ads.txt"
    if not ads_path.is_file() or ads_path.stat().st_size == 0:
        failures.append(f"{ads_path}: missing ads.txt")
    else:
        ads_text = ads_path.read_text(encoding="utf-8")
        lowered = ads_text.lower()
        if "<html" in lowered or "<!doctype" in lowered:
            failures.append("ads.txt must be plain text, not an HTML page")
        stripped = [line.strip() for line in ads_text.splitlines() if line.strip()]
        records = [line for line in stripped if not line.startswith("#")]
        comments = [line for line in stripped if line.startswith("#")]
        if records != [ads_txt_record]:
            failures.append("ads.txt must contain exactly one publisher record: " + ads_txt_record)
        if not any(
            "not enabled" in line.lower() or "disabled" in line.lower() for line in comments
        ):
            failures.append("ads.txt must state that advertising is not enabled")
        if "adsbygoogle" in lowered or "googlesyndication" in lowered:
            failures.append("ads.txt must not reference an ad script")

    privacy_path = site_dir / "privacy" / "index.html"
    if not privacy_path.is_file():
        failures.append("built site is missing /privacy/")
    else:
        privacy_html = privacy_path.read_text(encoding="utf-8")
        for phrase in (
            "An AdSense account exists for this site",
            "Advertising is not enabled",
            adsense_client,
            ads_txt_record,
            "consentIntegration",
            "not_configured",
            "adsbygoogle.js",
            "Auto ads",
            "account verification",
            "Google may set cookies",
            'href="/privacy/"',
        ):
            if phrase not in privacy_html:
                failures.append(f"/privacy/ is missing {phrase!r}")
        if adsense_meta not in privacy_html or privacy_html.find(adsense_meta) > privacy_html.lower().find("</head>"):
            failures.append("/privacy/ is missing the AdSense account meta tag in <head>")
        if "data-ad-slot-key" in privacy_html or 'src="/assets/js/publisher.js' in privacy_html:
            failures.append("/privacy/ must not reserve an ad placement or load publisher.js")

    config_path = site_dir / "publisher-config.json"
    try:
        config_text = config_path.read_text(encoding="utf-8")
        if ENABLED_TRUE_RE.search(config_text):
            failures.append("publisher-config.json sets AdSense enabled:true")
        config = json.loads(config_text)
        adsense = config.get("adsense") if isinstance(config, dict) else None
        slots = adsense.get("slots") if isinstance(adsense, dict) else None
        if (
            not isinstance(adsense, dict)
            or adsense.get("enabled") is not False
            or adsense.get("clientId") != adsense_client
            or adsense.get("consentIntegration") != "not_configured"
            or not isinstance(slots, dict)
            or set(slots) != set(slot_keys)
            or any(slots.get(key) is not None for key in slot_keys)
        ):
            failures.append(
                "publisher-config.json must record "
                + adsense_client
                + " while AdSense stays disabled (enabled false, null slots, consent not_configured)"
            )
    except (OSError, json.JSONDecodeError, AttributeError, TypeError) as error:
        failures.append(f"publisher-config.json: {error}")

    home_path = site_dir / "index.html"
    home = home_path.read_text(encoding="utf-8") if home_path.is_file() else ""
    for key in ("home-banner", "content-footer"):
        if f'data-ad-slot-key="{key}"' not in home:
            failures.append(f"homepage is missing reserved slot {key}")
    if 'data-ad-slot-key="in-content"' in home or 'data-ad-slot-key="list-banner"' in home:
        failures.append("homepage reserved an unexpected ad slot")
    if 'href="/privacy/"' not in home:
        failures.append("homepage does not link to /privacy/")
    if 'src="/assets/js/publisher.js' not in home:
        failures.append("homepage does not load the gated publisher script")
    if "Advertisements" not in home or "Advertising placement reserved" not in home:
        failures.append("homepage placeholder is missing its visible label or copy")

    categories_index = site_dir / "categories" / "index.html"
    if categories_index.is_file():
        categories_html = categories_index.read_text(encoding="utf-8")
        for key in ("list-banner", "content-footer"):
            if f'data-ad-slot-key="{key}"' not in categories_html:
                failures.append(f"categories index is missing reserved slot {key}")
        if 'data-ad-slot-key="in-content"' in categories_html or 'data-ad-slot-key="home-banner"' in categories_html:
            failures.append("categories index reserved an unexpected ad slot")

    collection_pages = list((site_dir / "categories").glob("*/index.html"))
    if not collection_pages:
        collection_pages = [
            path
            for path in (site_dir / "categories").glob("*.html")
            if path.name != "index.html"
        ]
    if not collection_pages:
        failures.append("no collection page available to check list placements")
    else:
        listing = collection_pages[0].read_text(encoding="utf-8")
        for key in ("list-banner", "in-content", "content-footer"):
            if f'data-ad-slot-key="{key}"' not in listing:
                failures.append(
                    f"{collection_pages[0].parent.name} is missing reserved slot {key}"
                )

    service_pages = list((site_dir / "services").glob("*/index.html"))
    if not service_pages:
        failures.append("no service page available to check the in-content placement")
    else:
        guide = service_pages[0].read_text(encoding="utf-8")
        for key in ("in-content", "content-footer"):
            if f'data-ad-slot-key="{key}"' not in guide:
                failures.append(f"{service_pages[0].parent.name} is missing reserved slot {key}")
        if 'data-ad-slot-key="home-banner"' in guide or 'data-ad-slot-key="list-banner"' in guide:
            failures.append(f"{service_pages[0].parent.name} reserved an unexpected banner slot")

    sitemap_path = site_dir / "sitemap.xml"
    if sitemap_path.is_file():
        sitemap = sitemap_path.read_text(encoding="utf-8")
        if "https://theagentnative.com/privacy/" not in sitemap:
            failures.append("sitemap.xml does not list https://theagentnative.com/privacy/")
    else:
        failures.append("sitemap.xml is missing, so /privacy/ cannot be advertised")

    robots_path = site_dir / "robots.txt"
    robots = robots_path.read_text(encoding="utf-8") if robots_path.is_file() else ""
    if re.search(r"(?im)^disallow:\s*/(?:privacy|ads\.txt)", robots):
        failures.append("robots.txt disallows /privacy/ or /ads.txt")
    if "Allow: /privacy/" not in robots or "Allow: /ads.txt" not in robots:
        failures.append("robots.txt does not explicitly allow /privacy/ and /ads.txt")

    checked_html: set[str] = set()
    missing_meta: list[str] = []
    missing_loader: list[str] = []
    for html_path in sorted(site_dir.rglob("*.html")):
        html = html_path.read_text(encoding="utf-8", errors="ignore")
        lowered = html.lower()
        relative = html_path.relative_to(site_dir).as_posix()
        checked_html.add(relative)
        head_end = lowered.find("</head>")
        meta_at = html.find(adsense_meta)
        if meta_at < 0 or head_end < 0 or meta_at > head_end:
            missing_meta.append(relative)
        # /privacy/ uses the same head as every other page.
        if not verification_loader_in_head(html):
            missing_loader.append(relative)
        # A privacy-policy mention of the filename is not a script tag.
        # The exact verification loader above is removed before these checks.
        failures.extend(forbidden_ad_markup(relative, html))
    for required in ("index.html", "privacy/index.html"):
        if required not in checked_html:
            failures.append(f"{required} is missing the AdSense account meta tag")
            failures.append(f"{required} is missing the AdSense verification loader")
        else:
            if required in missing_meta:
                failures.append(f"{required} is missing the AdSense account meta tag in <head>")
            if required in missing_loader:
                failures.append(
                    f"{required} must contain exactly one AdSense verification loader in <head>"
                )
    other_missing = [
        path for path in missing_meta if path not in {"index.html", "privacy/index.html"}
    ]
    if other_missing:
        sample = ", ".join(other_missing[:8])
        more = "" if len(other_missing) <= 8 else f" (+{len(other_missing) - 8} more)"
        failures.append(
            "built pages are missing the AdSense account meta tag: " + sample + more
        )
    other_loader = [
        path for path in missing_loader if path not in {"index.html", "privacy/index.html"}
    ]
    if other_loader:
        sample = ", ".join(other_loader[:8])
        more = "" if len(other_loader) <= 8 else f" (+{len(other_loader) - 8} more)"
        failures.append(
            "built pages must contain exactly one AdSense verification loader in <head>: "
            + sample
            + more
        )

    publisher_path = site_dir / "assets" / "js" / "publisher.js"
    if not publisher_path.is_file():
        failures.append("publisher.js was not copied into the built site")
    else:
        source = publisher_path.read_text(encoding="utf-8")
        if "pagead2.googlesyndication.com" not in source or "adsMayLoad" not in source:
            failures.append("publisher.js is missing the disabled advertising gate")
        if re.search(r"ca-pub-\d", source):
            failures.append("publisher.js hard-codes a publisher id")
        if ENABLED_TRUE_RE.search(source):
            failures.append("publisher.js sets AdSense enabled:true")

    if not failures:
        print(
            "Advertising stays disabled: verification loader, account meta, ads.txt, "
            "privacy page, and reserved slots passed"
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
            "+https://theagentnative.com/)"
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
