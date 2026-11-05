---
title: "Routerly | Agent-Native Services"
service_name: "Routerly"
description: "Self-hosted LLM gateway that routes requests across AI providers (OpenAI, Anthropic, Gemini, Mistral, Ollama) using intelligent multi-policy scoring —…"
permalink: /services/routerly/
page_kind: service
service_slug: "routerly"
category_slug: "llm-gateway-and-routing"
category_label: "LLM Gateway & Routing"
hero_image: "/assets/images/editorial-routing.webp"
image: "/assets/images/editorial-routing.webp"
classification: "agent-native"
dossier_path: "services/llm-gateway-and-routing/routerly.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/routerly.md"
tagline: "Self-hosted LLM gateway that routes requests across AI providers (OpenAI, Anthropic, Gemini, Mistral, Ollama) using intelligent multi-policy scoring — including an LLM-native routing policy. Drop-in compatible: just swap the base URL. No database required, built-in cost tracking, budget enforcement and multi-tenant isolation"
website: "https://github.com/Inebrio/Routerly"
repository: "https://github.com/Inebrio/Routerly"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">LLM Gateway &amp; Routing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">AGPL-3.0 · v0.1.5 (March 2026)</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Planned</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/Inebrio/Routerly" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/Inebrio/Routerly#readme" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Inebrio/Routerly" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/routerly.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Routerly is a **self-hosted LLM gateway** with one distinguishing primitive: an **LLM-native routing policy** that uses a small LLM to make per-request routing decisions, alongside conventional rule-based policies (cost, latency, fallback, sticky session). The other policies are familiar — budgets, tenant isolation, cost tracking — but the operational story is unusual: **no database, no Redis**, just a JSON config file. That makes it interesting for small teams running a single agent fleet who want intelligent routing without operating a stateful gateway cluster.

It is drop-in compatible with the OpenAI and Anthropic SDKs (just swap the base URL), and supports OpenAI, Anthropic, Gemini, Mistral, and local Ollama.

---

## Agent-facing interfaces

- **Catalog protocols:** CLI, http
- **MCP:** ⚠️ Not yet published. Routerly fronts LLM endpoints; an MCP-on-MCP routing surface is on the roadmap.
- **Agent Skill:** ⚠️ Not yet published.
- **Onboarding type:** `cli`

## How agents onboard

```
# Run the gateway:
docker run -p 8080:8080 -v ./routerly.json:/config/routerly.json inebrio/routerly:latest

# Point any OpenAI-compatible client at it:
export OPENAI_BASE_URL=http://localhost:8080/v1
export OPENAI_API_KEY=<your tenant key>
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/routerly.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| OpenAI-compatible HTTP | `/v1/chat/completions`, `/v1/completions`, `/v1/embeddings` |
| Anthropic-compatible HTTP | `/v1/messages` |
| JSON Config | Single file — providers, tenants, policies, budgets |
| Docker / single binary | Self-host anywhere |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/llm-gateway-and-routing/' | relative_url }}"><small>Collection</small><strong>← LLM Gateway &amp; Routing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
