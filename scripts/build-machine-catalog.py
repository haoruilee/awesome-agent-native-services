#!/usr/bin/env python3
"""Build and validate the catalog's deterministic machine-readable contract.

The service dossiers remain the editorial source of truth. This script extracts
only fields that are explicit in those files, validates catalog invariants, and
writes stable artifacts for both GitHub and the Jekyll site.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
SERVICES_ROOT = ROOT / "services"
SITE_BASE = "https://lihaorui.com/awesome-agent-native-services"
REPOSITORY = "https://github.com/haoruilee/awesome-agent-native-services"
RAW_BASE = "https://raw.githubusercontent.com/haoruilee/awesome-agent-native-services/main"
SCHEMA_URL = f"{SITE_BASE}/catalog.schema.json"
SCHEMA_VERSION = "1.0.0"

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

REQUIRED_SECTIONS = (
    "Official Website",
    "Official Repo",
    "How to Use (Agent Onboarding)",
    "Agent Skills",
    "MCP",
    "What It Does",
    "Why It Is Agent-Native",
    "Primary Primitives",
    "Autonomy Model",
    "Identity and Delegation Model",
    "Protocol Surface",
    "Human-in-the-Loop Support",
    "Why Generic Alternatives Do Not Qualify",
    "Use Cases",
)

ONBOARDING_TYPES = {
    "url",
    "agent-skill",
    "mcp",
    "cli",
    "sdk",
    "api",
    "documentation",
    "other",
    "unspecified",
}

INTEGRATION_STATUSES = {
    "available",
    "optional",
    "planned",
    "unavailable",
    "not-applicable",
    "unknown",
}

PROTOCOL_ORDER = (
    "url-onboarding",
    "agent-skill",
    "mcp",
    "rest",
    "graphql",
    "grpc",
    "websocket",
    "webhook",
    "cli",
    "sdk",
    "a2a",
    "acp",
    "openapi",
    "json-rpc",
    "stdio",
    "http",
    "api",
    "documentation",
)
PROTOCOLS = set(PROTOCOL_ORDER)

URL_RE = re.compile(r"https?://[^\s<>|)`\]]+")
GITHUB_REPO_RE = re.compile(
    r"https://github\.com/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)?"
)
DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class CatalogError(RuntimeError):
    """Raised when a source dossier violates the catalog contract."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def clean_url(value: str) -> str:
    return value.split("$(", 1)[0].rstrip(".,;:'\"")


def first_url(value: str) -> str | None:
    match = URL_RE.search(value)
    return clean_url(match.group(0)) if match else None


def all_urls(value: str) -> list[str]:
    """Return de-duplicated HTTP URLs in source order."""
    values: list[str] = []
    for match in URL_RE.finditer(value):
        url = clean_url(match.group(0))
        if url not in values:
            values.append(url)
    return values


def plain_inline(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = value.replace("**", "").replace("`", "")
    value = re.sub(r"\s+", " ", value).strip()
    return value.strip('"')


def extract_headings(text: str) -> list[tuple[str, int, int]]:
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE))
    return [(match.group(1), match.start(), match.end()) for match in matches]


def section(text: str, name: str) -> str:
    headings = extract_headings(text)
    for index, (heading, _, end) in enumerate(headings):
        normalized = heading.removeprefix("⭐ ")
        if normalized == name:
            finish = headings[index + 1][1] if index + 1 < len(headings) else len(text)
            return text[end:finish].strip()
    raise CatalogError(f"missing required section: {name}")


def validate_section_order(path: Path, text: str) -> None:
    headings = [heading.removeprefix("⭐ ") for heading, _, _ in extract_headings(text)]
    positions: list[int] = []
    for required in REQUIRED_SECTIONS:
        count = headings.count(required)
        if count != 1:
            raise CatalogError(
                f"{relative(path)}: expected one '{required}' section, found {count}"
            )
        positions.append(headings.index(required))
    if positions != sorted(positions):
        raise CatalogError(f"{relative(path)}: required sections are out of order")


def summary_fields(text: str) -> dict[str, str]:
    header = text.split("\n---\n", 1)[0]
    fields: dict[str, str] = {}
    for match in re.finditer(
        r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|\s*$", header, re.MULTILINE
    ):
        fields[match.group(1)] = match.group(2)
    return fields


def title_from(text: str, path: Path) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    if not match:
        raise CatalogError(f"{relative(path)}: missing H1 service name")
    return plain_inline(match.group(1))


def tagline_from(text: str) -> str | None:
    match = re.search(r"^>\s+(.+?)\s*$", text, re.MULTILINE)
    return plain_inline(match.group(1)) if match else None


def official_website(text: str, fields: dict[str, str]) -> str | None:
    value = first_url(section(text, "Official Website"))
    if value:
        return value
    for key in ("Website", "AWS Page"):
        value = first_url(fields.get(key, ""))
        if value:
            return value
    return None


def lifecycle_status(text: str, fields: dict[str, str]) -> str:
    """Extract lifecycle only from an explicit dossier statement."""
    website_field = plain_inline(fields.get("Website", "")).lower()
    website_section = plain_inline(section(text, "Official Website")).lower()
    evidence = f"{website_field}\n{website_section}"
    if any(marker in evidence for marker in ("offline", "no longer resolve")) and any(
        marker in evidence for marker in ("no replacement", "former domain", "previously listed")
    ):
        return "offline"
    if any(marker in evidence for marker in ("sunset", "discontinued", "shut down")):
        return "sunset"
    if fields.get("Verified at") and fields.get("Latest-month signal"):
        return "active"
    # A URL is not enough evidence to claim live health at generation time.
    return "unknown"


def official_repository(text: str) -> str | None:
    """Return only a repository explicitly presented in the Official Repo section."""
    repo_section = section(text, "Official Repo")
    first_paragraph = repo_section.split("\n\n", 1)[0].lower()
    negative_markers = (
        "no public",
        "not open-source",
        "not publicly",
        "no canonical",
        "no primary",
        "does not publish",
        "not published as",
        "managed service",
    )
    if any(marker in first_paragraph for marker in negative_markers):
        return None
    match = GITHUB_REPO_RE.search(repo_section)
    return clean_url(match.group(0)).removesuffix(".git") if match else None


def first_code_block(value: str) -> str | None:
    match = re.search(r"```[^\n]*\n(.*?)\n```", value, re.DOTALL)
    return match.group(1).strip() if match else None


def text_after_label(value: str, label: str) -> str | None:
    match = re.search(rf"\*\*{re.escape(label)}:\*\*\s*(.*)", value)
    if not match:
        return None
    remainder = value[match.end() - len(match.group(1)) :].lstrip()
    code = first_code_block(remainder)
    if code:
        return code
    for line in remainder.splitlines():
        candidate = line.strip().removeprefix("> ")
        if candidate and not candidate.startswith("**"):
            return candidate.replace("`", "")
    return None


def onboarding_contract(text: str) -> dict[str, Any]:
    content = section(text, "How to Use (Agent Onboarding)")
    pattern_match = re.search(r"\*\*Interaction pattern:\*\*\s*(.+)", content)
    pattern = plain_inline(pattern_match.group(1)) if pattern_match else None

    instruction = text_after_label(content, "One-sentence instruction")
    if instruction is None:
        instruction = text_after_label(content, "Quickest verified path")
    if instruction is None:
        instruction = first_code_block(content)
    if instruction is None:
        for line in content.splitlines():
            candidate = line.strip().removeprefix("> ")
            if candidate and not candidate.startswith(("**", "#", "- ", "|")):
                instruction = candidate.replace("`", "")
                break
    if instruction is not None:
        instruction = instruction.strip()

    lower = f"{pattern or ''}\n{instruction or ''}\n{content[:600]}".lower()
    onboarding_document = instruction and (
        "skill.md" in instruction.lower() or "llms.txt" in instruction.lower()
    )
    if "url onboarding" in lower or onboarding_document:
        onboarding_type = "url"
        pattern = pattern or "URL Onboarding"
    elif "agent skill" in (pattern or "").lower() or "clawhub" in lower or "skills add" in lower:
        onboarding_type = "agent-skill"
    elif "mcp" in (pattern or "").lower() or (
        instruction is not None and "mcp" in instruction.lower()
    ):
        onboarding_type = "mcp"
    elif "cli" in (pattern or "").lower() or (
        instruction
        and re.search(r"\b(?:npx|uvx|docker|brew|curl|[a-z0-9-]+\s+install\s+-g)\b", instruction.lower())
    ):
        onboarding_type = "cli"
    elif "sdk" in (pattern or "").lower() or (
        instruction and re.search(r"\b(?:pip|npm|pnpm|yarn)\s+install\b", instruction.lower())
    ):
        onboarding_type = "sdk"
    elif re.search(r"\b(?:rest|api|webhook)\b", (pattern or "").lower()) or (
        instruction and "curl " in instruction.lower()
    ):
        onboarding_type = "api"
    elif instruction and first_url(instruction):
        onboarding_type = "documentation"
    elif instruction:
        onboarding_type = "other"
    else:
        onboarding_type = "unspecified"

    onboarding_url = first_url(instruction or "") or first_url(content)
    return {
        "type": onboarding_type,
        "pattern": pattern,
        "instruction": instruction,
        "url": onboarding_url,
    }


def integration_status(content: str) -> str:
    match = re.search(r"\*\*Status:\*\*\s*(.+)", content)
    if not match:
        return "unknown"
    status = plain_inline(match.group(1)).lower()
    if "not applicable" in status:
        return "not-applicable"
    if any(term in status for term in ("roadmap", "planned", "future work")):
        return "planned"
    if any(term in status for term in ("community may", "may publish", "not verified")):
        return "unknown"
    if any(
        term in status
        for term in (
            "not yet",
            "not published",
            "no official",
            "no standalone",
            "no dedicated",
            "no mcp",
            "not available",
            "❌",
        )
    ):
        return "unavailable"
    if any(term in status for term in ("optional", "compatibility", "not primary")):
        return "optional"
    if any(
        term in status
        for term in (
            "✅",
            "available",
            "bundled",
            "native",
            "primary",
            "core product",
            "this project is",
            "supported",
        )
    ):
        return "available"
    return "unknown"


def protocol_contract(
    text: str,
    onboarding: dict[str, Any],
    mcp_status: str,
    skill_status: str,
) -> list[str]:
    content = section(text, "Protocol Surface").lower()
    # Protocol dossiers sometimes make explicit negative statements such as
    # "There is no REST API, SDK, or MCP transport." Never turn those tokens
    # into positive capabilities.
    positive_content = "\n".join(
        line
        for line in content.splitlines()
        if not re.search(r"\b(?:no|not|without|unavailable|unsupported)\b", line)
    )
    found: set[str] = set()
    onboarding_protocol = {
        "url": "url-onboarding",
        "agent-skill": "agent-skill",
        "mcp": "mcp",
        "cli": "cli",
        "sdk": "sdk",
        "api": "api",
        "documentation": "documentation",
    }.get(onboarding["type"])
    if onboarding_protocol:
        found.add(onboarding_protocol)
    if mcp_status in {"available", "optional"}:
        found.add("mcp")
    if skill_status in {"available", "optional"}:
        found.add("agent-skill")

    token_patterns = {
        "rest": r"\brest\b",
        "graphql": r"\bgraphql\b",
        "grpc": r"\bgrpc\b",
        "websocket": r"\bwebsockets?\b",
        "webhook": r"\bwebhooks?\b",
        "cli": r"\bcli\b",
        "sdk": r"\bsdks?\b",
        "a2a": r"\ba2a\b",
        "acp": r"\bacp\b",
        "openapi": r"\bopenapi\b",
        "json-rpc": r"\bjson[- ]rpc\b",
        "stdio": r"\bstdio\b",
        "http": r"\bhttps?\b",
        "api": r"\bapi\b",
    }
    for protocol, pattern in token_patterns.items():
        if re.search(pattern, positive_content):
            found.add(protocol)
    if not found:
        found.add("documentation")
    return [protocol for protocol in PROTOCOL_ORDER if protocol in found]


def source_digest(input_paths: list[Path]) -> dict[str, Any]:
    digest = hashlib.sha256()
    relative_paths: list[str] = []
    for path in input_paths:
        path_string = relative(path)
        relative_paths.append(path_string)
        digest.update(path_string.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return {
        "algorithm": "sha256",
        "value": digest.hexdigest(),
        "input_paths": relative_paths,
    }


def catalog_version() -> str:
    skill = read_text(ROOT / "skill.md")
    match = re.search(r'^version:\s*["\']?([^"\'\n]+)', skill, re.MULTILINE)
    if not match or not DATE_RE.fullmatch(match.group(1)):
        raise CatalogError("skill.md must declare a YYYY-MM-DD version in front matter")
    return match.group(1)


def ordered_category_directories() -> list[Path]:
    directories = sorted(path for path in SERVICES_ROOT.iterdir() if path.is_dir())
    by_slug = {path.name: path for path in directories}
    known = [by_slug[slug] for slug in CATEGORY_ORDER if slug in by_slug]
    unknown = [path for path in directories if path.name not in CATEGORY_ORDER]
    return known + unknown


def build_catalog() -> dict[str, Any]:
    category_directories = ordered_category_directories()
    categories: list[dict[str, Any]] = []
    services: list[dict[str, Any]] = []
    input_paths = [ROOT / "README.md", ROOT / "skill.md"]

    root_readme = read_text(ROOT / "README.md")
    for category_directory in category_directories:
        category_slug = category_directory.name
        if not SLUG_RE.fullmatch(category_slug):
            raise CatalogError(f"invalid category slug: {category_slug}")
        category_readme_path = category_directory / "README.md"
        if not category_readme_path.is_file():
            raise CatalogError(f"{category_slug}: missing category README.md")
        category_readme = read_text(category_readme_path)
        input_paths.append(category_readme_path)
        service_paths = sorted(
            path for path in category_directory.glob("*.md") if path.name != "README.md"
        )
        if not service_paths:
            raise CatalogError(f"{category_slug}: category has no service dossiers")

        heading = title_from(category_readme, category_readme_path)
        description = tagline_from(category_readme)
        if description is None:
            raise CatalogError(f"{relative(category_readme_path)}: missing category summary")
        categories.append(
            {
                "id": category_slug,
                "name": CATEGORY_NAMES.get(category_slug, heading.removesuffix(" Services")),
                "description": description,
                "dossier": f"{REPOSITORY}/blob/main/services/{category_slug}/README.md",
                "service_count": len(service_paths),
            }
        )

        for path in service_paths:
            input_paths.append(path)
            slug = path.stem
            if not SLUG_RE.fullmatch(slug):
                raise CatalogError(f"{relative(path)}: invalid service slug")
            text = read_text(path)
            validate_section_order(path, text)
            fields = summary_fields(text)
            classification = plain_inline(fields.get("Classification", ""))
            if classification != "agent-native":
                raise CatalogError(
                    f"{relative(path)}: expected agent-native classification, got {classification!r}"
                )
            website = official_website(text, fields)
            lifecycle = lifecycle_status(text, fields)
            if website is None and lifecycle not in {"offline", "sunset"}:
                raise CatalogError(
                    f"{relative(path)}: null official website requires an explicit offline lifecycle"
                )
            onboarding = onboarding_contract(text)
            mcp_status = integration_status(section(text, "MCP"))
            skill_status = integration_status(section(text, "Agent Skills"))
            protocols = protocol_contract(text, onboarding, mcp_status, skill_status)
            if lifecycle in {"offline", "sunset"}:
                # Historical prose can preserve former commands and protocol
                # positioning, but an offline record must never export those as
                # currently executable machine capabilities.
                onboarding = {
                    "type": "unspecified",
                    "pattern": "Unavailable",
                    "instruction": None,
                    "url": None,
                }
                mcp_status = "unavailable"
                skill_status = "unavailable"
                protocols = ["documentation"]
            latest_month_signal = (
                plain_inline(fields["Latest-month signal"])
                if "Latest-month signal" in fields
                else None
            )
            verified_at = plain_inline(fields.get("Verified at", "")) or None
            if verified_at is not None and not DATE_RE.fullmatch(verified_at):
                raise CatalogError(f"{relative(path)}: Verified at must be YYYY-MM-DD")
            verification_sources = all_urls(fields.get("Latest-month signal", ""))
            if verified_at is not None and not verification_sources:
                fallback_source = official_repository(text) or website
                if fallback_source:
                    verification_sources = [fallback_source]
            if verified_at is None:
                verification_sources = []
            source_path = relative(path)
            if f"]({source_path})" not in root_readme:
                raise CatalogError(f"README.md does not link catalog service {source_path}")
            if f"]({slug}.md)" not in category_readme:
                raise CatalogError(
                    f"{relative(category_readme_path)} does not link service {slug}.md"
                )

            services.append(
                {
                    "id": f"{category_slug}/{slug}",
                    "slug": slug,
                    "name": title_from(text, path),
                    "tagline": tagline_from(text),
                    "classification": "agent-native",
                    "status": "listed",
                    "lifecycle_status": lifecycle,
                    "category": category_slug,
                    "website": website,
                    "repository": official_repository(text),
                    "dossier": f"{REPOSITORY}/blob/main/{source_path}",
                    "source_path": source_path,
                    "onboarding": onboarding,
                    "protocols": protocols,
                    "mcp_status": mcp_status,
                    "agent_skill_status": skill_status,
                    "latest_month_signal": latest_month_signal,
                    "verified_at": verified_at,
                    "verification_sources": verification_sources,
                }
            )

    version = catalog_version()
    catalog = {
        "$schema": SCHEMA_URL,
        "schema_version": SCHEMA_VERSION,
        "catalog_version": version,
        "generated_at": version,
        "license": "CC0-1.0",
        "source": {
            "repository": REPOSITORY,
            "branch": "main",
            "catalog_path": "skill.md",
            "service_directory": "services",
            "content_digest": source_digest(input_paths),
        },
        "counts": {
            "categories": len(categories),
            "services": len(services),
        },
        "categories": categories,
        "services": services,
    }
    validate_catalog(catalog)
    return catalog


def is_http_url(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate_catalog(catalog: dict[str, Any]) -> None:
    if catalog.get("$schema") != SCHEMA_URL:
        raise CatalogError("catalog schema URL does not match the public contract")
    if catalog.get("schema_version") != SCHEMA_VERSION:
        raise CatalogError("catalog schema version does not match the generator")
    if not DATE_RE.fullmatch(catalog.get("catalog_version", "")):
        raise CatalogError("catalog_version must be a date")
    if catalog.get("generated_at") != catalog.get("catalog_version"):
        raise CatalogError("generated_at must be the deterministic catalog snapshot date")
    categories = catalog.get("categories")
    services = catalog.get("services")
    if not isinstance(categories, list) or not isinstance(services, list):
        raise CatalogError("categories and services must be arrays")
    if catalog.get("counts") != {
        "categories": len(categories),
        "services": len(services),
    }:
        raise CatalogError("catalog counts do not match the generated arrays")

    category_ids = [item.get("id") for item in categories]
    if len(category_ids) != len(set(category_ids)):
        raise CatalogError("duplicate category ID")
    service_ids = [item.get("id") for item in services]
    if len(service_ids) != len(set(service_ids)):
        raise CatalogError("duplicate service ID")
    for category in categories:
        if not SLUG_RE.fullmatch(category.get("id", "")):
            raise CatalogError(f"invalid category ID: {category.get('id')!r}")
        if not is_http_url(category.get("dossier")):
            raise CatalogError(f"{category['id']}: invalid category dossier URL")
        actual_count = sum(1 for service in services if service.get("category") == category["id"])
        if category.get("service_count") != actual_count:
            raise CatalogError(f"{category['id']}: service_count does not match services")

    for service in services:
        service_id = service.get("id", "<unknown>")
        expected_id = f"{service.get('category')}/{service.get('slug')}"
        if service_id != expected_id:
            raise CatalogError(f"{service_id}: ID is not the stable category/slug path")
        if service.get("category") not in category_ids:
            raise CatalogError(f"{service_id}: unknown category")
        if service.get("classification") != "agent-native" or service.get("status") != "listed":
            raise CatalogError(f"{service_id}: invalid classification or listing status")
        lifecycle = service.get("lifecycle_status")
        if lifecycle not in {"active", "offline", "sunset", "unknown"}:
            raise CatalogError(f"{service_id}: invalid lifecycle status")
        for key in ("website", "repository"):
            if service.get(key) is not None and not is_http_url(service[key]):
                raise CatalogError(f"{service_id}: invalid {key} URL")
        if service.get("website") is None and lifecycle not in {"offline", "sunset"}:
            raise CatalogError(f"{service_id}: null website without offline lifecycle")
        if not is_http_url(service.get("dossier")):
            raise CatalogError(f"{service_id}: invalid dossier URL")
        onboarding = service.get("onboarding", {})
        if onboarding.get("type") not in ONBOARDING_TYPES:
            raise CatalogError(f"{service_id}: invalid onboarding type")
        if onboarding.get("url") is not None and not is_http_url(onboarding["url"]):
            raise CatalogError(f"{service_id}: invalid onboarding URL")
        protocols = service.get("protocols")
        if not isinstance(protocols, list) or not protocols or not set(protocols) <= PROTOCOLS:
            raise CatalogError(f"{service_id}: invalid protocol list")
        if len(protocols) != len(set(protocols)):
            raise CatalogError(f"{service_id}: duplicate protocol")
        for key in ("mcp_status", "agent_skill_status"):
            if service.get(key) not in INTEGRATION_STATUSES:
                raise CatalogError(f"{service_id}: invalid {key}")
        verified_at = service.get("verified_at")
        verification_sources = service.get("verification_sources")
        if verified_at is None:
            if verification_sources != []:
                raise CatalogError(f"{service_id}: unverified entry cannot claim verification sources")
        elif not DATE_RE.fullmatch(verified_at):
            raise CatalogError(f"{service_id}: invalid verified_at date")
        elif not verification_sources or not all(is_http_url(url) for url in verification_sources):
            raise CatalogError(f"{service_id}: verified entry needs source URLs")
        elif verified_at > catalog["catalog_version"]:
            raise CatalogError(f"{service_id}: verified_at is after catalog_version")
        if lifecycle == "active" and verified_at is None:
            raise CatalogError(f"{service_id}: active lifecycle needs verification evidence")


def validate_with_json_schema(catalog: dict[str, Any], schema: dict[str, Any]) -> None:
    """Validate the public contract with its declared JSON Schema, fail closed."""
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as error:
        raise CatalogError(
            "jsonschema is required; run: pip install -r requirements-validation.txt"
        ) from error
    Draft202012Validator.check_schema(schema)
    errors = sorted(
        Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(catalog),
        key=lambda error: list(error.absolute_path),
    )
    if errors:
        details = "\n".join(f"- {list(error.absolute_path)}: {error.message}" for error in errors)
        raise CatalogError(f"catalog.json does not satisfy catalog.schema.json:\n{details}")


def strip_front_matter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        raise CatalogError("skill.md has an unterminated YAML front matter block")
    return text[end + len("\n---\n") :].lstrip("\n")


def deploy_skill_text(text: str) -> str:
    """Make the static site copy self-contained outside the repository root."""
    text = strip_front_matter(text)

    def absolutize(match: re.Match[str]) -> str:
        label, destination = match.groups()
        if urlparse(destination).scheme or destination.startswith(("#", "/")):
            return match.group(0)
        path, separator, fragment = destination.partition("#")
        absolute = f"{REPOSITORY}/blob/main/{path}"
        if separator:
            absolute += f"#{fragment}"
        return f"[{label}]({absolute})"

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", absolutize, text)


def build_llms(categories: list[dict[str, Any]], service_count: int) -> str:
    collection_count = len(categories)
    lines = [
        "# Awesome Agent-Native Services",
        "",
        (
            f"> A curated catalog of {service_count} agent-native services across "
            f"{collection_count} collections — infrastructure designed for AI agents "
            "as first-class consumers, plus purpose-built surfaces for operating live "
            "agent systems."
        ),
        "",
        "Use the JSON catalog for deterministic filtering and the discovery skill for task-oriented guidance. Service dossiers contain the full evidence and caveats.",
        "",
        "## Agent entry points",
        "",
        f"- [Discovery skill]({SITE_BASE}/skill.md): Task routing, onboarding guidance, and the full human-readable service index.",
        f"- [Machine-readable catalog]({SITE_BASE}/catalog.json): Versioned JSON records with stable IDs, typed onboarding, protocols, status, and provenance.",
        f"- [Catalog JSON Schema]({SITE_BASE}/catalog.schema.json): Draft 2020-12 validation contract for catalog.json.",
        "",
        "## Documentation",
        "",
        f"- [Collection website]({SITE_BASE}/): Visual catalog and category navigation.",
        f"- [Catalog README]({REPOSITORY}): Complete editorial index and project overview.",
        f"- [Contribution guide]({REPOSITORY}/blob/main/CONTRIBUTING.md): Admission criteria, evidence requirements, and contribution workflow.",
        f"- [Agent instructions]({RAW_BASE}/AGENTS.md): Repository operating contract for coding agents.",
        "",
        "## Collections",
        "",
    ]
    for category in categories:
        lines.append(
            f"- [{category['name']}]({SITE_BASE}/categories/{category['id']}/): "
            f"{category['description']}"
        )
    lines.extend(
        [
            "",
            "## Optional",
            "",
            f"- [Installable Agent Skills]({REPOSITORY}/tree/main/.skills): Find, evaluate, install, or contribute services from an agent host.",
            f"- [Research audit]({REPOSITORY}/blob/main/RESEARCH_AUDIT.md): Catalog research and freshness notes.",
            f"- [Issue intake]({REPOSITORY}/issues/new/choose): Structured proposals, updates, flags, and category requests.",
            "",
        ]
    )
    result = "\n".join(lines)
    validate_llms(result)
    return result


def validate_llms(text: str) -> None:
    """Validate the strict link-list subset consumed by llms.txt parsers."""
    if not text.startswith("# Awesome Agent-Native Services\n\n> "):
        raise CatalogError("llms.txt needs an H1 followed by a blockquote summary")
    if "```" in text or re.search(r"^\|", text, re.MULTILINE):
        raise CatalogError("llms.txt must not contain code fences or tables")
    sections = re.split(r"^##\s+", text, flags=re.MULTILINE)[1:]
    if len(sections) < 2:
        raise CatalogError("llms.txt needs link-list sections")
    link_pattern = re.compile(r"^- \[[^\]]+\]\(https?://[^)]+\): .+$")
    for block in sections:
        lines = block.splitlines()
        if not lines[0].strip():
            raise CatalogError("llms.txt contains an empty H2")
        body = [line for line in lines[1:] if line.strip()]
        if not body or any(not link_pattern.fullmatch(line) for line in body):
            raise CatalogError(
                f"llms.txt section '{lines[0]}' must contain only Markdown link-list items"
            )
    try:
        from llms_txt.core import parse_llms_file
    except ImportError as error:
        raise CatalogError(
            "llms-txt is required; run: pip install -r requirements-validation.txt"
        ) from error
    parsed = parse_llms_file(text)
    if parsed.title != "Awesome Agent-Native Services" or not parsed.sections:
        raise CatalogError("llms.txt failed the reference parser contract")


def url_onboarding_flag(onboarding: dict[str, Any]) -> bool:
    if onboarding.get("type") == "url":
        return True
    pattern = onboarding.get("pattern") or ""
    return "url onboarding" in pattern.lower()


def build_search_index(catalog: dict[str, Any]) -> dict[str, Any]:
    """Emit the compact client search payload used by the GitHub Pages masthead."""
    services: list[dict[str, Any]] = []
    for service in catalog["services"]:
        category = service["category"]
        label = CATEGORY_NAMES.get(category, category.replace("-", " "))
        name = service["name"]
        slug = service["slug"]
        tagline = service.get("tagline") or ""
        service_id = service["id"]
        haystack = " ".join(
            part for part in (name, slug, service_id, tagline, category, label) if part
        ).lower()
        services.append(
            {
                "id": service_id,
                "slug": slug,
                "name": name,
                "tagline": tagline,
                "category": category,
                "website": service.get("website"),
                "repository": service.get("repository"),
                "dossier": service.get("dossier"),
                "mcp_status": service["mcp_status"],
                "url_onboarding": url_onboarding_flag(service.get("onboarding") or {}),
                "haystack": haystack,
            }
        )
    return {
        "catalog_version": catalog["catalog_version"],
        "count": len(services),
        "categories": {slug: CATEGORY_NAMES[slug] for slug in CATEGORY_ORDER},
        "services": services,
    }


def expected_outputs() -> dict[Path, str]:
    schema_path = ROOT / "catalog.schema.json"
    schema_text = read_text(schema_path)
    try:
        schema = json.loads(schema_text)
    except json.JSONDecodeError as error:
        raise CatalogError(f"catalog.schema.json is invalid JSON: {error}") from error
    catalog = build_catalog()
    validate_with_json_schema(catalog, schema)
    catalog_text = json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"
    search_index_text = json.dumps(
        build_search_index(catalog), ensure_ascii=False, separators=(",", ":")
    ) + "\n"
    llms_text = build_llms(catalog["categories"], catalog["counts"]["services"])
    skill_text = deploy_skill_text(read_text(ROOT / "skill.md"))
    return {
        ROOT / "catalog.json": catalog_text,
        ROOT / "llms.txt": llms_text,
        ROOT / "docs" / "catalog.json": catalog_text,
        ROOT / "docs" / "catalog.schema.json": schema_text,
        ROOT / "docs" / "llms.txt": llms_text,
        ROOT / "docs" / "skill.md": skill_text,
        ROOT / "docs" / "assets" / "search-index.json": search_index_text,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate sources and fail if generated artifacts are missing or stale",
    )
    args = parser.parse_args()
    try:
        outputs = expected_outputs()
        if args.check:
            stale = [path for path, content in outputs.items() if not path.is_file() or read_text(path) != content]
            if stale:
                print("Machine catalog artifacts are stale:", file=sys.stderr)
                for path in stale:
                    print(f"- {relative(path)}", file=sys.stderr)
                print("Run: python3 scripts/build-machine-catalog.py", file=sys.stderr)
                return 1
            catalog = json.loads(outputs[ROOT / "catalog.json"])
            print(
                f"Machine catalog is current: {catalog['counts']['services']} services / "
                f"{catalog['counts']['categories']} categories."
            )
            return 0

        changed: list[str] = []
        for path, content in outputs.items():
            if not path.is_file() or read_text(path) != content:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
                changed.append(relative(path))
        catalog = json.loads(outputs[ROOT / "catalog.json"])
        print(
            f"Generated machine catalog: {catalog['counts']['services']} services / "
            f"{catalog['counts']['categories']} categories."
        )
        if changed:
            print("Updated: " + ", ".join(changed))
        else:
            print("All generated artifacts were already current.")
        return 0
    except CatalogError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
