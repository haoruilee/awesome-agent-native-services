---
title: "Galileo | Agent-Native Services"
service_name: "Galileo"
description: "Galileo is the AI observability and eval engineering platform where offline evals become production guardrails"
permalink: /services/galileo/
page_kind: service
service_slug: "galileo"
category_slug: "observability-and-tracing"
category_label: "Observability & Tracing"
hero_image: "/assets/images/editorial-observability.webp"
image: "/assets/images/editorial-observability.webp"
classification: "agent-native"
dossier_path: "services/observability-and-tracing/galileo.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/galileo.md"
tagline: "Galileo is the AI observability and eval engineering platform where offline evals become production guardrails"
website: "https://galileo.ai"
repository: "https://github.com/rungalileo"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Observability &amp; Tracing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Mixed (hosted product + open-source SDKs/examples)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://galileo.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.galileo.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/rungalileo" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/galileo.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Galileo is an observability and evaluation platform for LLM systems, with explicit support for agent workflows. It captures traces, runs evals, surfaces failure patterns (Signals), and provides IDE-integrated remediation workflows via MCP.

The MCP server extends this into coding-time operations: your IDE agent can create datasets, run experiments, inspect Log stream signals, and get integration guidance without leaving the editor.

---

## Agent-facing interfaces

- **Interaction pattern:** MCP (Cursor / VS Code) + Galileo API key
- **Catalog protocols:** MCP, SDK, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ No official npx skills add ... package found.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** MCP (Cursor / VS Code) + Galileo API key

```json
{
  "mcpServers": {
    "galileo_mcp_server": {
      "url": "https://api.galileo.ai/mcp/http/mcp",
      "headers": {
        "Galileo-API-Key": "YOUR-API-KEY",
        "Accept": "text/event-stream"
      }
    }
  }
}
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/galileo.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| MCP (HTTP) | `https://api.galileo.ai/mcp/http/mcp` |
| SDK / API | Python/TypeScript SDKs and API reference under docs |
| Web Console | Hosted UI for traces, metrics, datasets, and experiments |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/observability-and-tracing/' | relative_url }}"><small>Collection</small><strong>← Observability &amp; Tracing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
