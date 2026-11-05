---
title: "Langfuse | Agent-Native Services"
service_name: "Langfuse"
description: "Open-source LLM observability, tracing, and evaluation for AI agents"
permalink: /services/langfuse/
page_kind: service
service_slug: "langfuse"
category_slug: "observability-and-tracing"
category_label: "Observability & Tracing"
hero_image: "/assets/images/editorial-observability.webp"
image: "/assets/images/editorial-observability.webp"
classification: "agent-native"
dossier_path: "services/observability-and-tracing/langfuse.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/langfuse.md"
tagline: "Open-source LLM observability, tracing, and evaluation for AI agents"
website: "https://langfuse.com"
repository: "https://github.com/langfuse/langfuse"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Observability &amp; Tracing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Open-source (MIT / enterprise)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">Agent Skill · MCP · SDK · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://langfuse.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://langfuse.com/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/langfuse/langfuse" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/langfuse.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Langfuse provides structured tracing for multi-step agent workflows. It captures the full execution trajectory of an agent — LLM calls, tool invocations, retriever steps, guardrail checks — organized in a typed, hierarchical trace structure. Production traces can be converted to evaluation datasets with one click, and OpenTelemetry integration allows existing monitoring infrastructure to receive agent telemetry.

---

## Agent-facing interfaces

- **Catalog protocols:** Agent Skill, MCP, SDK, API
- **MCP:** ✅ Available
- **Agent Skill:** ✅ Official skill published at langfuse/skills — listed on skills.sh/langfuse/skills
- **Onboarding type:** `agent-skill`

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `langfuse.trace()`, `@observe()` decorator, context manager |
| TypeScript SDK | Equivalent TypeScript API |
| OpenTelemetry | OTEL-compatible; works with any OTEL-instrumented agent framework |
| OpenAI Agents SDK | Native auto-instrumentation |
| Claude SDK | Native auto-instrumentation |
| LangChain | Native callback integration |
| LangGraph | Native integration |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/observability-and-tracing/' | relative_url }}"><small>Collection</small><strong>← Observability &amp; Tracing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
