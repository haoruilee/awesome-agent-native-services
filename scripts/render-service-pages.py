#!/usr/bin/env python3
"""Render per-service GitHub Pages introductions from dossiers + catalog.json.

Editorial source of truth remains services/<category>/<slug>.md. This writer
only copies explicit dossier/catalog fields into docs/services/<slug>/index.md
and refreshes the repository-root sitemap.xml. It never invents facts.
"""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SERVICES_ROOT = ROOT / "services"
DOCS_SERVICES = ROOT / "docs" / "services"
CATALOG_PATH = ROOT / "catalog.json"
SITEMAP_PATH = ROOT / "sitemap.xml"
SITE_BASE = "https://theagentnative.com"
REPOSITORY = "https://github.com/haoruilee/awesome-agent-native-services"

CATEGORY_ORDER = (
    "communication",
    "browser-and-web-execution",
    "tool-access-and-integration",
    "oversight-and-approval",
    "commerce-and-payments",
    "agent-runtime-and-infrastructure",
    "agent-harnesses-and-control-planes",
    "memory-and-state",
    "search-and-web-intelligence",
    "code-execution",
    "observability-and-tracing",
    "durable-execution-and-scheduling",
    "meeting-and-conversation",
    "voice-and-phone",
    "llm-gateway-and-routing",
    "agent-social-network",
)

CATEGORY_NAMES = {
    "communication": "Communication",
    "browser-and-web-execution": "Browser & Web Execution",
    "tool-access-and-integration": "Tool Access & Integration",
    "oversight-and-approval": "Oversight & Approval",
    "commerce-and-payments": "Commerce & Payments",
    "agent-runtime-and-infrastructure": "Agent Runtime & Infrastructure",
    "agent-harnesses-and-control-planes": "Agent Harnesses & Operator Surfaces",
    "memory-and-state": "Memory & State",
    "search-and-web-intelligence": "Search & Web Intelligence",
    "code-execution": "Code Execution",
    "observability-and-tracing": "Observability & Tracing",
    "durable-execution-and-scheduling": "Durable Execution & Scheduling",
    "meeting-and-conversation": "Meeting & Conversation",
    "voice-and-phone": "Voice & Phone",
    "llm-gateway-and-routing": "LLM Gateway & Routing",
    "agent-social-network": "Agent Social & Community",
}

CATEGORY_HERO = {
    "communication": "/assets/images/editorial-communication.webp",
    "browser-and-web-execution": "/assets/images/editorial-browser.webp",
    "tool-access-and-integration": "/assets/images/editorial-tools.webp",
    "oversight-and-approval": "/assets/images/editorial-oversight.webp",
    "commerce-and-payments": "/assets/images/editorial-commerce.webp",
    "agent-runtime-and-infrastructure": "/assets/images/editorial-runtime.webp",
    "agent-harnesses-and-control-planes": "/assets/images/editorial-harness.webp",
    "memory-and-state": "/assets/images/editorial-memory.webp",
    "search-and-web-intelligence": "/assets/images/editorial-search.webp",
    "code-execution": "/assets/images/editorial-sandbox.webp",
    "observability-and-tracing": "/assets/images/editorial-observability.webp",
    "durable-execution-and-scheduling": "/assets/images/editorial-durable.webp",
    "meeting-and-conversation": "/assets/images/editorial-meeting.webp",
    "voice-and-phone": "/assets/images/editorial-voice.webp",
    "llm-gateway-and-routing": "/assets/images/editorial-routing.webp",
    "agent-social-network": "/assets/images/editorial-social.webp",
}

FIELD_RE = re.compile(
    r"^\|\s*\*\*(?P<label>[^*]+)\*\*\s*\|\s*(?P<value>.*?)\s*\|\s*$",
    re.MULTILINE,
)
STATUS_RE = re.compile(r"^\*\*Status:\*\*\s*(.+)$", re.MULTILINE)
HEADING_RE = re.compile(r"^## (.+)$", re.MULTILINE)
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
INLINE_CODE_RE = re.compile(r"`([^`]+)`")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def yaml_quote(value: str) -> str:
    """Emit a double-quoted YAML scalar (JSON strings are valid YAML)."""
    return json.dumps(value, ensure_ascii=False)


def strip_inline_markdown(value: str) -> str:
    value = MD_LINK_RE.sub(r"\1", value)
    value = BOLD_RE.sub(r"\1", value)
    value = INLINE_CODE_RE.sub(r"\1", value)
    return re.sub(r"\s+", " ", value).strip()


def clean_quoted_prose(value: str) -> str:
    """Normalize dossier/catalog taglines that retain unbalanced quote marks."""
    value = strip_inline_markdown(value).strip()
    quotes = set("\'" + '"' + "“”")
    if len(value) >= 2 and value[0] == value[-1] and value[0] in quotes:
        value = value[1:-1].strip()
    if value.count('"') == 1:
        value = value.replace('"', "")
    return value.strip().strip(".,;")



def extract_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for match in FIELD_RE.finditer(text):
        label = match.group("label").strip()
        value = match.group("value").strip()
        fields.setdefault(label, value)
    return fields


def extract_section(text: str, *titles: str) -> str | None:
    matches = list(HEADING_RE.finditer(text))
    for index, match in enumerate(matches):
        heading = match.group(1).strip()
        # Allow a leading decorative marker such as ⭐ on onboarding headings.
        normalized = heading.lstrip("⭐ ").strip()
        if heading not in titles and normalized not in titles:
            continue
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[start:end]
        # Drop the horizontal rule that usually follows the heading block.
        body = re.sub(r"^\n*---\n*", "\n", body)
        body = body.strip("\n")
        return body.strip() or None
    return None


def extract_status_line(section_body: str | None) -> str | None:
    if not section_body:
        return None
    match = STATUS_RE.search(section_body)
    if not match:
        return None
    return strip_inline_markdown(match.group(1))


def first_paragraph(section_body: str | None, limit: int = 1200) -> str | None:
    """Return the leading prose of a section, stopping before tables/lists/code."""
    if not section_body:
        return None
    chunks: list[str] = []
    for raw_line in section_body.splitlines():
        line = raw_line.rstrip()
        if not line:
            if chunks:
                break
            continue
        if line.startswith(("#", "|", "```", "- ", "* ", "1. ", "> ")):
            if chunks:
                break
            # Skip leading non-prose; keep looking for a paragraph.
            if line.startswith("```"):
                break
            continue
        chunks.append(line)
    if not chunks:
        return None
    paragraph = strip_inline_markdown(" ".join(chunks))
    if len(paragraph) > limit:
        clipped = paragraph[: limit - 1].rsplit(" ", 1)[0]
        paragraph = clipped.rstrip(".,;:") + "…"
    return paragraph or None


def absolutize_relative_links(markdown: str, source_path: str) -> str:
    """Point relative dossier links at the GitHub blob for that dossier."""

    def repl(match: re.Match[str]) -> str:
        label, destination = match.groups()
        if re.match(r"^[a-z][a-z0-9+.-]*:", destination, re.I):
            return match.group(0)
        if destination.startswith(("#", "/", "mailto:", "tel:")):
            return match.group(0)
        path, sep, fragment = destination.partition("#")
        # README.md and sibling files live next to the dossier.
        if path in ("", "."):
            absolute = f"{REPOSITORY}/blob/main/{source_path}"
        elif path.startswith("./"):
            absolute = f"{REPOSITORY}/blob/main/{Path(source_path).parent / path[2:]}"
        else:
            absolute = f"{REPOSITORY}/blob/main/{Path(source_path).parent / path}"
        if sep:
            absolute += f"#{fragment}"
        return f"[{label}]({absolute})"

    return MD_LINK_RE.sub(repl, markdown)


def meta_description(tagline: str | None, what_it_does: str | None, name: str) -> str:
    base = tagline or what_it_does or f"{name} — agent-native service in the Agent-Native Index."
    base = clean_quoted_prose(base)
    if len(base) > 158:
        base = base[:157].rsplit(" ", 1)[0].rstrip(".,;:") + "…"
    return base


def status_label(value: str | None) -> str:
    mapping = {
        "available": "Available",
        "optional": "Optional",
        "planned": "Planned",
        "unavailable": "Unavailable",
        "not-applicable": "Not applicable",
        "unknown": "Unknown",
    }
    if not value:
        return "Unknown"
    return mapping.get(value, value.replace("-", " ").title())


def protocol_labels(protocols: list[str] | None) -> list[str]:
    if not protocols:
        return []
    labels = []
    for item in protocols:
        if item == "mcp":
            labels.append("MCP")
        elif item == "agent-skill":
            labels.append("Agent Skill")
        elif item == "url-onboarding":
            labels.append("URL onboarding")
        elif item == "a2a":
            labels.append("A2A")
        elif item == "acp":
            labels.append("ACP")
        else:
            labels.append(item.upper() if item in {"cli", "sdk", "api", "rest", "graphql", "grpc", "stdio"} else item.replace("-", " "))
    return labels


def render_chips(items: list[tuple[str, str]]) -> str:
    parts = ['<ul class="service-page__chips">']
    for label, value in items:
        parts.append(
            "<li><span class=\"service-page__chip-label\">"
            f"{html.escape(label)}</span>"
            f"<span class=\"service-page__chip-value\">{html.escape(value)}</span></li>"
        )
    parts.append("</ul>")
    return "\n".join(parts)


def render_link_list(links: list[tuple[str, str]]) -> str:
    if not links:
        return ""
    lines = ['<ul class="service-page__links">']
    for label, url in links:
        lines.append(
            f'<li><a href="{html.escape(url, quote=True)}" rel="noopener noreferrer">'
            f"{html.escape(label)} ↗</a></li>"
        )
    lines.append("</ul>")
    return "\n".join(lines)


def build_page(service: dict[str, Any]) -> str:
    source_path = service["source_path"]
    dossier_path = ROOT / source_path
    text = read_text(dossier_path)
    fields = extract_fields(text)

    name = service["name"]
    slug = service["slug"]
    category = service["category"]
    category_label = CATEGORY_NAMES.get(category, category.replace("-", " ").title())
    raw_tagline = service.get("tagline")
    if not raw_tagline:
        quote = re.search(r"^> (.+)$", text, re.MULTILINE)
        raw_tagline = quote.group(1) if quote else ""
    tagline = clean_quoted_prose(raw_tagline) or None

    what = extract_section(text, "What It Does")
    onboarding = extract_section(
        text, "How to Use (Agent Onboarding)", "⭐ How to Use (Agent Onboarding)"
    )
    mcp_section = extract_section(text, "MCP")
    skills_section = extract_section(text, "Agent Skills")
    protocol_section = extract_section(text, "Protocol Surface")

    what_paragraph = first_paragraph(what)
    onboarding_pattern = None
    if onboarding:
        pattern_match = re.search(
            r"\*\*Interaction pattern:\*\*\s*(.+)$", onboarding, re.MULTILINE
        )
        if pattern_match:
            onboarding_pattern = strip_inline_markdown(pattern_match.group(1))

    # Prefer the first fenced quickstart block verbatim (already from dossier).
    quickstart = None
    if onboarding:
        fence = re.search(r"```[^\n]*\n(.*?)```", onboarding, re.DOTALL)
        if fence:
            quickstart = fence.group(0).strip()

    license_value = strip_inline_markdown(fields.get("License", "")) or None
    status_value = strip_inline_markdown(fields.get("Status", "")) or None
    classification = (
        strip_inline_markdown(fields.get("Classification", ""))
        or service.get("classification")
        or "agent-native"
    )
    verified_at = service.get("verified_at")
    website = service.get("website") or strip_inline_markdown(fields.get("Website", "")) or None
    docs_url = strip_inline_markdown(fields.get("Docs", "")) or None
    if docs_url and not docs_url.lower().startswith("http"):
        docs_url = None
    repository = service.get("repository")
    dossier_url = service.get("dossier") or f"{REPOSITORY}/blob/main/{source_path}"

    description = meta_description(tagline, what_paragraph, name)
    hero = CATEGORY_HERO.get(category, "/assets/images/editorial-hero.webp")
    title = f"{name} | Agent-Native Services"

    chips: list[tuple[str, str]] = [
        ("Collection", category_label),
        ("Classification", classification),
    ]
    if license_value:
        chips.append(("License", license_value))
    if status_value:
        chips.append(("Status", status_value))
    chips.append(("MCP", status_label(service.get("mcp_status"))))
    chips.append(("Agent Skill", status_label(service.get("agent_skill_status"))))
    protocols = protocol_labels(service.get("protocols"))
    if protocols:
        chips.append(("Interfaces", " · ".join(protocols)))
    if verified_at:
        chips.append(("Verified", verified_at))

    links: list[tuple[str, str]] = []
    if website and website.lower().startswith("http"):
        links.append(("Website", website))
    if docs_url:
        links.append(("Docs", docs_url))
    if repository and str(repository).lower().startswith("http"):
        links.append(("Official repo", str(repository)))
    links.append(("Full dossier on GitHub", dossier_url))

    # Body sections — markdown, sourced only from the dossier.
    body_parts: list[str] = [
        render_chips(chips),
        "",
        render_link_list(links),
        "",
    ]

    if what_paragraph or what:
        body_parts.append("## What it does")
        body_parts.append("")
        # Prefer the full prose section when short; otherwise first paragraph + note.
        section_for_page = what or ""
        # Avoid dumping enormous evidence tables; stop before nested ## already handled.
        # Keep lists/paragraphs/code but drop the rare trailing horizontal rules.
        cleaned = absolutize_relative_links(section_for_page.strip(), source_path)
        # Cap very long sections by keeping content before the first markdown table
        # only when the table is not the whole section — still dossier text only.
        if len(cleaned) > 4000:
            # Keep leading prose + the first code fence if present, still verbatim.
            prose = first_paragraph(cleaned, limit=2000) or what_paragraph
            body_parts.append(prose or cleaned[:2000])
            body_parts.append("")
            body_parts.append(
                f"_Full write-up in the [dossier on GitHub]({dossier_url})._"
            )
        else:
            body_parts.append(cleaned)
        body_parts.append("")

    body_parts.append("## Agent-facing interfaces")
    body_parts.append("")
    mcp_status_line = extract_status_line(mcp_section)
    skill_status_line = extract_status_line(skills_section)
    if onboarding_pattern:
        body_parts.append(f"- **Interaction pattern:** {onboarding_pattern}")
    if protocols:
        body_parts.append(f"- **Catalog protocols:** {', '.join(protocols)}")
    if mcp_status_line:
        body_parts.append(f"- **MCP:** {mcp_status_line}")
    else:
        body_parts.append(f"- **MCP:** {status_label(service.get('mcp_status'))}")
    if skill_status_line:
        body_parts.append(f"- **Agent Skill:** {skill_status_line}")
    else:
        body_parts.append(
            f"- **Agent Skill:** {status_label(service.get('agent_skill_status'))}"
        )
    onboarding_meta = service.get("onboarding") or {}
    if onboarding_meta.get("type") and onboarding_meta.get("type") != "unspecified":
        body_parts.append(f"- **Onboarding type:** `{onboarding_meta['type']}`")
    body_parts.append("")

    if quickstart or onboarding_pattern:
        body_parts.append("## How agents onboard")
        body_parts.append("")
        if onboarding_pattern:
            body_parts.append(f"**Interaction pattern:** {onboarding_pattern}")
            body_parts.append("")
        if quickstart:
            body_parts.append(absolutize_relative_links(quickstart, source_path))
            body_parts.append("")
        body_parts.append(
            f"See the [full onboarding section in the dossier]({dossier_url}#how-to-use-agent-onboarding)."
        )
        body_parts.append("")

    if protocol_section and len(protocol_section) < 3500:
        body_parts.append("## Protocol surface")
        body_parts.append("")
        body_parts.append(absolutize_relative_links(protocol_section.strip(), source_path))
        body_parts.append("")

    if verified_at:
        sources = service.get("verification_sources") or []
        body_parts.append("## Verification")
        body_parts.append("")
        body_parts.append(f"Last verified **{verified_at}**.")
        if sources:
            body_parts.append("")
            body_parts.append("Sources:")
            for url in sources:
                body_parts.append(f"- {url}")
        body_parts.append("")

    body_parts.extend(
        [
            '<nav class="service-page__nav" aria-label="Service placement">',
            f'  <a href="{{{{ \'/categories/{category}/\' | relative_url }}}}">'
            f"<small>Collection</small><strong>← {html.escape(category_label)}</strong></a>",
            '  <a href="{{ \'/\' | relative_url }}">'
            "<small>Index</small><strong>Agent-Native Index →</strong></a>",
            "</nav>",
            "",
        ]
    )

    front_matter = "\n".join(
        [
            "---",
            f"title: {yaml_quote(title)}",
            f"service_name: {yaml_quote(name)}",
            f"description: {yaml_quote(description)}",
            f'permalink: /services/{slug}/',
            "page_kind: service",
            f"service_slug: {yaml_quote(slug)}",
            f"category_slug: {yaml_quote(category)}",
            f"category_label: {yaml_quote(category_label)}",
            f"hero_image: {yaml_quote(hero)}",
            f"image: {yaml_quote(hero)}",
            f"classification: {yaml_quote(classification)}",
            f"dossier_path: {yaml_quote(source_path)}",
            f"dossier_url: {yaml_quote(dossier_url)}",
        ]
    )
    if tagline:
        front_matter += f"\ntagline: {yaml_quote(tagline)}"
    if verified_at:
        front_matter += f"\nverified_at: {yaml_quote(verified_at)}"
    if website and str(website).lower().startswith("http"):
        front_matter += f"\nwebsite: {yaml_quote(str(website))}"
    if repository and str(repository).lower().startswith("http"):
        front_matter += f"\nrepository: {yaml_quote(str(repository))}"
    front_matter += "\n---\n\n"

    return front_matter + "\n".join(body_parts).rstrip() + "\n"


def editorial_sitemap_urls() -> list[tuple[str, str, str]]:
    """Hand-written pages. Jekyll also emits these; this keeps the repo sitemap in step."""
    urls = [
        (f"{SITE_BASE}/about/", "monthly", "0.5"),
        (f"{SITE_BASE}/editorial-policy/", "monthly", "0.5"),
        (f"{SITE_BASE}/guides/", "weekly", "0.8"),
    ]
    guides = ROOT / "docs" / "guides"
    found: list[tuple[str, str, str]] = []
    if not guides.is_dir():
        raise SystemExit("docs/guides is missing")
    for path in sorted(guides.glob("*.md")):
        if path.name == "index.md":
            continue
        match = re.search(r"^permalink:\s*(\S+)\s*$", read_text(path), re.MULTILINE)
        if not match:
            raise SystemExit(f"{path} is missing a permalink")
        permalink = match.group(1).strip('"')
        if not permalink.endswith("/"):
            permalink += "/"
        found.append((f"{SITE_BASE}{permalink}", "monthly", "0.6"))
    if len(found) < 6:
        raise SystemExit(f"expected at least 6 guide permalinks, found {len(found)}")
    return urls + found


def write_sitemap(services: list[dict[str, Any]]) -> None:
    urls: list[tuple[str, str, str]] = [
        (f"{SITE_BASE}/", "daily", "1.0"),
        (f"{SITE_BASE}/categories/", "weekly", "0.8"),
    ]
    for slug in CATEGORY_ORDER:
        urls.append((f"{SITE_BASE}/categories/{slug}/", "weekly", "0.7"))
    urls.extend(editorial_sitemap_urls())
    for service in sorted(services, key=lambda item: item["slug"]):
        urls.append((f"{SITE_BASE}/services/{service['slug']}/", "weekly", "0.6"))
    urls.extend(
        [
            (f"{SITE_BASE}/privacy/", "monthly", "0.4"),
            (f"{SITE_BASE}/skill.md", "weekly", "0.9"),
            (f"{SITE_BASE}/catalog.json", "weekly", "0.9"),
            (f"{SITE_BASE}/llms.txt", "weekly", "0.8"),
        ]
    )
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for loc, changefreq, priority in urls:
        lines.extend(
            [
                "  <url>",
                f"    <loc>{loc}</loc>",
                f"    <changefreq>{changefreq}</changefreq>",
                f"    <priority>{priority}</priority>",
                "  </url>",
            ]
        )
    lines.append("</urlset>")
    lines.append("")
    SITEMAP_PATH.write_text("\n".join(lines), encoding="utf-8")


def clean_service_docs(keep_slugs: set[str]) -> None:
    if not DOCS_SERVICES.exists():
        return
    for child in sorted(DOCS_SERVICES.iterdir()):
        if not child.is_dir():
            if child.name != "README.md":
                child.unlink()
            continue
        if child.name not in keep_slugs:
            for path in sorted(child.rglob("*"), reverse=True):
                if path.is_file():
                    path.unlink()
                elif path.is_dir():
                    path.rmdir()
            child.rmdir()


def main() -> int:
    if not CATALOG_PATH.is_file():
        print(f"Missing {CATALOG_PATH}; run build-machine-catalog.py first", file=sys.stderr)
        return 1
    catalog = json.loads(read_text(CATALOG_PATH))
    services = catalog.get("services")
    if not isinstance(services, list) or not services:
        print("catalog.json has no services", file=sys.stderr)
        return 1

    DOCS_SERVICES.mkdir(parents=True, exist_ok=True)
    keep: set[str] = set()
    written = 0
    for service in sorted(services, key=lambda item: item["slug"]):
        slug = service["slug"]
        keep.add(slug)
        out_dir = DOCS_SERVICES / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        page = build_page(service)
        out_path = out_dir / "index.md"
        out_path.write_text(page, encoding="utf-8")
        written += 1

    clean_service_docs(keep)
    write_sitemap(services)
    readme = DOCS_SERVICES / "README.md"
    readme.write_text(
        (
            "# Service introduction pages\n\n"
            "Generated by `scripts/render-service-pages.py` via "
            "`scripts/build-github-pages.sh` from `services/**/*.md` and "
            "`catalog.json`. Do not edit by hand.\n"
        ),
        encoding="utf-8",
    )
    print(f"Wrote {written} service pages under {DOCS_SERVICES.relative_to(ROOT)}")
    print(f"Wrote {SITEMAP_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
