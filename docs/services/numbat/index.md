---
title: "numbat | Agent-Native Services"
service_name: "numbat"
description: "Endpoint visibility into AI agent activity, with local detection, optional pre-action blocking, and forensic reconstruction"
permalink: /services/numbat/
page_kind: service
service_slug: "numbat"
category_slug: "observability-and-tracing"
category_label: "Observability & Tracing"
hero_image: "/assets/images/editorial-observability.webp"
image: "/assets/images/editorial-observability.webp"
classification: "agent-native"
dossier_path: "services/observability-and-tracing/numbat.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/numbat.md"
tagline: "Endpoint visibility into AI agent activity, with local detection, optional pre-action blocking, and forensic reconstruction"
verified_at: "2026-09-26"
website: "https://github.com/perplexityai/numbat"
repository: "https://github.com/perplexityai/numbat"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Observability &amp; Tracing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · http</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/perplexityai/numbat" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/perplexityai/numbat/tree/main/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/perplexityai/numbat" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/numbat.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

numbat is endpoint observability and policy infrastructure specifically for AI agents. It discovers supported agent installations, reconstructs existing sessions from on-disk artifacts, receives live activity from agent-native hooks/plugins or OTLP/HTTP, and normalizes all sources into one closed event vocabulary. A shared CEL engine evaluates both live and at-rest events for single-step and multi-step behaviors.

The output is a versioned NDJSON evidence stream: events, findings, enforcement decisions, indicators, and scan summaries retain endpoint, source agent, session/run, tool-call, and evidence references. `timeline` reconstructs session activity; `case build` creates portable evidence bundles with SHA-256 manifests. Optional enforcement can ask supported synchronous pre-action hooks to deny a clean match, while monitor-only behavior remains the default and every shipped rule is non-enforcing.

Coverage is deliberately bounded by each host's published artifacts and hooks. At-rest reconstruction cannot recover unpersisted actions, findings are not proof of compromise, and hook enforcement is not a complete endpoint security boundary.

---

## Agent-facing interfaces

- **Interaction pattern:** endpoint CLI + agent hooks/plugins + OTLP/HTTP
- **Catalog protocols:** CLI, http
- **MCP:** ⚠️ No MCP server is published.
- **Agent Skill:** ⚠️ Not yet published — numbat installs native hook/plugin/extension integrations, not an Agent Skills SKILL.md package.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** endpoint CLI + agent hooks/plugins + OTLP/HTTP

```bash
go install github.com/perplexityai/numbat/cmd/numbat@latest
numbat agents
numbat scan --agent codex
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/numbat.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| **CLI** | `agents`, `scan`, `timeline`, `collect`, `ship`, `hook`, `rules`, `case`, and `version`; JSON/NDJSON-oriented automation and stable exit behavior |
| **Native agent integrations** | Generated hooks, plugins, or extensions for supported CLI, IDE, desktop, and gateway agents |
| **OTLP/HTTP ingest** | Local collector for supported protobuf log exporters; default endpoint pattern `127.0.0.1:4318/v1/logs` |
| **NDJSON output** | Version `0.2.0` typed records to stdout or file |
| **HTTP output** | `application/x-ndjson`, optional gzip, bearer or HMAC-SHA256 auth; direct delivery is not a durable queue |
| **JSON Schema** | Per-record and union-stream schemas under `docs/schema/v0.2.0/` |
| **Rule format** | YAML rules with CEL expressions, sequence steps, tests, versioning, and optional `enforce: true` |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://github.com/perplexityai/numbat/releases/tag/v0.2.0
- https://api.github.com/repos/perplexityai/numbat

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/observability-and-tracing/' | relative_url }}"><small>Collection</small><strong>← Observability &amp; Tracing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
