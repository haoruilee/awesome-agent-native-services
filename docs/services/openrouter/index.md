---
title: "OpenRouter | Agent-Native Services"
service_name: "OpenRouter"
description: "The Unified Interface For LLMs"
permalink: /services/openrouter/
page_kind: service
service_slug: "openrouter"
category_slug: "llm-gateway-and-routing"
category_label: "LLM Gateway & Routing"
hero_image: "/assets/images/editorial-routing.webp"
image: "/assets/images/editorial-routing.webp"
classification: "agent-native"
dossier_path: "services/llm-gateway-and-routing/openrouter.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/openrouter.md"
tagline: "The Unified Interface For LLMs"
website: "https://openrouter.ai"
repository: "https://github.com/OpenRouterTeam"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">LLM Gateway &amp; Routing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · http · API · documentation</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://openrouter.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://openrouter.ai/docs/quickstart" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/OpenRouterTeam" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/openrouter.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

OpenRouter provides a **single OpenAI-compatible API** to access **hundreds of models** from dozens of labs with **routing**, **uptime optimization**, **pricing transparency**, and **usage analytics**. It is widely used for **agentic and multi-model workflows** (tool calling, fallbacks, provider selection) without maintaining separate billing and client integrations per provider — see homepage *"Featured Agents"* and [provider selection](https://openrouter.ai/docs/guides/routing/provider-selection) docs.

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, REST, SDK, http, API, documentation
- **MCP:** ⚠️ No first-party OpenRouter MCP server documented as core product; integration is primarily HTTP / SDK.
- **Agent Skill:** ⚠️ No official AgentSkills catalog entry found.
- **Onboarding type:** `documentation`

## How agents onboard

```bash
# Docs: https://openrouter.ai/docs/quickstart
export OPENROUTER_API_KEY=...
# Use OpenAI SDK with base_url https://openrouter.ai/api/v1
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/openrouter.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST | `https://openrouter.ai/api/v1` — OpenAI-compatible |
| SDKs | TypeScript, Python, Go, Java — https://openrouter.ai/sdk |
| Dashboard | Account, credits, keys — secondary to API |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/llm-gateway-and-routing/' | relative_url }}"><small>Collection</small><strong>← LLM Gateway &amp; Routing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
