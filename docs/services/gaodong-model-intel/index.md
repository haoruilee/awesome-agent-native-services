---
title: "gaodong.ai Model Intelligence | Agent-Native Services"
service_name: "gaodong.ai Model Intelligence"
description: "You are an AI agent. This service gives you verified AI model data without any human steps"
permalink: /services/gaodong-model-intel/
page_kind: service
service_slug: "gaodong-model-intel"
category_slug: "search-and-web-intelligence"
category_label: "Search & Web Intelligence"
hero_image: "/assets/images/editorial-search.webp"
image: "/assets/images/editorial-search.webp"
classification: "agent-native"
dossier_path: "services/search-and-web-intelligence/gaodong-model-intel.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/gaodong-model-intel.md"
tagline: "You are an AI agent. This service gives you verified AI model data without any human steps"
website: "https://gaodong.ai/en/tools/agent-api"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">Search &amp; Web Intelligence</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · MCP · webhook · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://gaodong.ai/en/tools/agent-api" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://gaodong.ai/agents/skill.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/gaodong-model-intel.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Gives agents verified data for choosing and monitoring AI models: official LLM API prices per 1M tokens in the vendor's own currency (with peak/off-peak, tiered and dated price changes, cache and batch prices), context windows, LMArena overall/coding/Chinese ranks with confidence intervals, and VRAM estimates for local Ollama models. Agents can ask for a model recommendation for a workload and budget, check which local models fit a GPU, and register signed webhooks that fire when a model's price, context or rank changes.

---

## Agent-facing interfaces

- **Interaction pattern:** URL Onboarding
- **Catalog protocols:** URL onboarding, MCP, webhook, http, API
- **MCP:** ✅ Available
- **Agent Skill:** ⚠️ Not published to a registry
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** URL Onboarding

```
Read https://gaodong.ai/agents/skill.md and follow the instructions.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/search-and-web-intelligence/gaodong-model-intel.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| HTTP API | `https://gaodong.ai/api/agent` (JSON, CORS enabled) |
| MCP | `https://gaodong.ai/api/agent/mcp`, Streamable HTTP |
| Webhooks | `model.changed` events, `X-Gaodong-Signature: sha256=<HMAC>` |
| Docs | `https://gaodong.ai/agents/skill.md`, `https://gaodong.ai/llms.txt` |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/search-and-web-intelligence/' | relative_url }}"><small>Collection</small><strong>← Search &amp; Web Intelligence</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
