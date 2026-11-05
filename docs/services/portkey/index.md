---
title: "Portkey | Agent-Native Services"
service_name: "Portkey"
description: "The AI gateway built for production agents"
permalink: /services/portkey/
page_kind: service
service_slug: "portkey"
category_slug: "llm-gateway-and-routing"
category_label: "LLM Gateway & Routing"
hero_image: "/assets/images/editorial-routing.webp"
image: "/assets/images/editorial-routing.webp"
classification: "agent-native"
dossier_path: "services/llm-gateway-and-routing/portkey.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/portkey.md"
tagline: "The AI gateway built for production agents"
website: "https://portkey.ai"
repository: "https://github.com/Portkey-AI/portkey-python-sdk"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">LLM Gateway &amp; Routing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://portkey.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://portkey.ai/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Portkey-AI/portkey-python-sdk" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/portkey.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Portkey is an AI gateway that sits between agent code and LLM providers. Agents send requests to Portkey's OpenAI-compatible endpoint; Portkey handles routing, fallback, caching, budget enforcement, and observability — transparently, without the agent needing to know which underlying provider is serving the request.

The key primitives are specifically designed for agent workloads: **virtual keys** (per-agent scoped credentials), **per-agent budget limits**, **sticky session routing** (keep the same agent on the same provider during a multi-turn conversation), and **agent-trace observability** (trace multi-hop agent call chains with cost attribution per step).

---

## Agent-facing interfaces

- **Catalog protocols:** REST, SDK, http, API
- **MCP:** ⚠️ No dedicated MCP server published.
- **Agent Skill:** ⚠️ No official skill published by Portkey yet.
- **Onboarding type:** `sdk`

## Protocol surface

| Interface | Detail |
|---|---|
| REST API | OpenAI-compatible endpoint: `https://api.portkey.ai/v1` |
| Python SDK | `pip install portkey-ai` |
| Node SDK | `npm install portkey-ai` |
| Framework Support | OpenAI Agents SDK, LangChain, CrewAI, AutoGen, LlamaIndex, LangGraph — 2-line integration |
| LLM Coverage | 1,600+ models across 200+ providers |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/llm-gateway-and-routing/' | relative_url }}"><small>Collection</small><strong>← LLM Gateway &amp; Routing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
