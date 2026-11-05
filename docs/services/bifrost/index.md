---
title: "Bifrost | Agent-Native Services"
service_name: "Bifrost"
description: "The fastest way to build AI applications that never go down"
permalink: /services/bifrost/
page_kind: service
service_slug: "bifrost"
category_slug: "llm-gateway-and-routing"
category_label: "LLM Gateway & Routing"
hero_image: "/assets/images/editorial-routing.webp"
image: "/assets/images/editorial-routing.webp"
classification: "agent-native"
dossier_path: "services/llm-gateway-and-routing/bifrost.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/bifrost.md"
tagline: "The fastest way to build AI applications that never go down"
verified_at: "2026-10-13"
website: "https://docs.getbifrost.ai"
repository: "https://github.com/maximhq/bifrost"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">LLM Gateway &amp; Routing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">Apache-2.0</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · CLI · SDK · json rpc · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-13</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://docs.getbifrost.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.getbifrost.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/maximhq/bifrost" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/bifrost.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Bifrost is a high-performance, self-hosted AI gateway that provides one OpenAI-compatible interface to more than 23 model providers. It handles provider configuration, request routing, retries, automatic fallbacks, load balancing, semantic caching, and drop-in integrations for common AI SDKs.

For agent systems, Bifrost adds an MCP client and gateway, opt-in Agent Mode for automatic tool execution, per-virtual-key tool filtering, hierarchical budgets and rate limits, and request observability. The gateway can aggregate tools from multiple MCP servers behind one endpoint while keeping provider credentials and governance policies outside agent code.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, CLI, SDK, json rpc, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ No official Agent Skill published by Bifrost yet.
- **Onboarding type:** `cli`

## How agents onboard

```bash
npx -y @maximhq/bifrost
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/bifrost.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| OpenAI-compatible HTTP API | Unified `/v1` API for supported model providers, including chat, responses, streaming, and tool calling where supported. |
| MCP Gateway | `POST /mcp` JSON-RPC tool discovery/execution and `GET /mcp` SSE for external MCP clients. |
| Go SDK | `go get github.com/maximhq/bifrost/core` for direct in-process provider access and tool-calling integrations. |
| Configuration API | Provider, virtual-key, budget, rate-limit, and MCP configuration through the management API. |
| Configuration files | Declarative `config.json` configuration for provider and governance setup. |
| Observability | Request logs, cost/token/latency metadata, Prometheus metrics, and distributed tracing integrations. |

---

## Verification

Last verified **2026-10-13**.

Sources:
- https://github.com/maximhq/bifrost

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/llm-gateway-and-routing/' | relative_url }}"><small>Collection</small><strong>← LLM Gateway &amp; Routing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
