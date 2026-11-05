---
title: "AgentEvals | Agent-Native Services"
service_name: "AgentEvals"
description: "Ship Agents Reliably — Benchmark your agents before they hit production. AgentEvals scores performance and inference quality from OpenTelemetry traces — no…"
permalink: /services/agentevals/
page_kind: service
service_slug: "agentevals"
category_slug: "observability-and-tracing"
category_label: "Observability & Tracing"
hero_image: "/assets/images/editorial-observability.webp"
image: "/assets/images/editorial-observability.webp"
classification: "agent-native"
dossier_path: "services/observability-and-tracing/agentevals.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/agentevals.md"
tagline: "Ship Agents Reliably — Benchmark your agents before they hit production. AgentEvals scores performance and inference quality from OpenTelemetry traces — no re-runs, no guesswork"
website: "https://aevals.ai"
repository: "https://github.com/agentevals-dev/agentevals"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Observability &amp; Tracing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Open-source (see repository)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · GRPC · CLI · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://aevals.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://aevals.ai/docs/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/agentevals-dev/agentevals" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/agentevals.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

AgentEvals scores **AI agent behavior** from **OpenTelemetry traces** without re-executing the agent. It ingests OTLP or Jaeger JSON, compares runs against **golden eval sets** (expected tool trajectories, responses), and reports pass/fail metrics suitable for CI. A bundled web UI and OTLP receiver support live streaming during development; Kubernetes Helm chart and Docker image support production-adjacent deployment next to agent workloads.

---

## Agent-facing interfaces

- **Interaction pattern:** CLI + OpenTelemetry + optional MCP + live OTLP receiver
- **Catalog protocols:** MCP, REST, GRPC, CLI, http, API
- **MCP:** ✅ Available (ships with agentevals-cli[live])
- **Agent Skill:** ⚠️ No standalone npx skills add … pack; the upstream repo documents Claude Code slash workflows under .claude/skills/ for repository contributors, not a published ClawHub skill.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** CLI + OpenTelemetry + optional MCP + live OTLP receiver

```bash
pip install agentevals-cli
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/agentevals.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| CLI | `agentevals run`, `agentevals serve`, `agentevals mcp`, `agentevals evaluator list` |
| OTLP | HTTP receiver on **4318** (and gRPC **4317** patterns via Collector) — see upstream README |
| REST API | Embedded in `serve` — `/docs`, `/redoc` |
| MCP | Port **8080** in containerized deployment — [README](https://github.com/agentevals-dev/agentevals/blob/main/README.md) |
| Kubernetes | Helm chart in `charts/agentevals/` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/observability-and-tracing/' | relative_url }}"><small>Collection</small><strong>← Observability &amp; Tracing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
