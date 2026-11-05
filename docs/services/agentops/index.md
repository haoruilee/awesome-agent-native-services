---
title: "AgentOps | Agent-Native Services"
service_name: "AgentOps"
description: "AgentOps is the developer favorite platform for testing, debugging, and deploying AI agents and LLM apps"
permalink: /services/agentops/
page_kind: service
service_slug: "agentops"
category_slug: "observability-and-tracing"
category_label: "Observability & Tracing"
hero_image: "/assets/images/editorial-observability.webp"
image: "/assets/images/editorial-observability.webp"
classification: "agent-native"
dossier_path: "services/observability-and-tracing/agentops.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/agentops.md"
tagline: "AgentOps is the developer favorite platform for testing, debugging, and deploying AI agents and LLM apps"
website: "https://www.agentops.ai"
repository: "https://github.com/AgentOps-AI/agentops"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Observability &amp; Tracing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.agentops.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.agentops.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/AgentOps-AI/agentops" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/agentops.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

AgentOps instruments **AI agents and LLM apps** with **sessions**, **waterfalls** of LLM/tool events, token/cost breakdowns, and **framework integrations** (LangChain, CrewAI, AutoGen, OpenAI Agents SDK, Google ADK, Smolagents, Haystack, AG2, etc.). It is explicitly positioned for **testing and debugging agents**, with a **public API** to pull trace data into other systems.

---

## Agent-facing interfaces

- **Interaction pattern:** SDK auto-instrumentation + Public REST API + MCP docs helper
- **Catalog protocols:** MCP, REST, SDK, http, API
- **MCP:** ⚠️ Docs MCP for Mintlify (chat with documentation) — not a trace-ingestion MCP. Trace data flows through SDK and REST.
- **Agent Skill:** ⚠️ No official npx skills add agentops/… pack documented as primary.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** SDK auto-instrumentation + Public REST API + MCP docs helper

```python
import agentops
agentops.init("<YOUR API KEY HERE>")
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/observability-and-tracing/agentops.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| Python SDK | `pip install agentops` |
| TypeScript SDK | See docs |
| REST | `https://api.agentops.ai` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/observability-and-tracing/' | relative_url }}"><small>Collection</small><strong>← Observability &amp; Tracing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
