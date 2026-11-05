---
title: "Helicone | Agent-Native Services"
service_name: "Helicone"
description: "Build Reliable AI Apps — AI Gateway & LLM observability"
permalink: /services/helicone/
page_kind: service
service_slug: "helicone"
category_slug: "llm-gateway-and-routing"
category_label: "LLM Gateway & Routing"
hero_image: "/assets/images/editorial-routing.webp"
image: "/assets/images/editorial-routing.webp"
classification: "agent-native"
dossier_path: "services/llm-gateway-and-routing/helicone.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/helicone.md"
tagline: "Build Reliable AI Apps — AI Gateway & LLM observability"
website: "https://www.helicone.ai"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">LLM Gateway &amp; Routing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">REST · http · documentation</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.helicone.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.helicone.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/helicone.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Helicone provides an **OpenAI-compatible AI Gateway** to **100+ models** (OpenAI, Anthropic, Google, Groq, etc.) with **unified billing / credits**, **automatic fallbacks**, and **full request logging** in the Helicone dashboard. Agents and apps use a **single API key** instead of juggling many provider keys — optional **bring-your-own-key** mode for advanced control — see [Quickstart](https://docs.helicone.ai/).

---

## Agent-facing interfaces

- **Catalog protocols:** REST, http, documentation
- **MCP:** ⚠️ No dedicated Helicone MCP server documented as primary surface.
- **Agent Skill:** ⚠️ No official AgentSkills repo listed.
- **Onboarding type:** `documentation`

## How agents onboard

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://ai-gateway.helicone.ai",
  apiKey: process.env.HELICONE_API_KEY,
});
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/helicone.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST | OpenAI-compatible `chat/completions` at `ai-gateway.helicone.ai` |
| Dashboard | https://us.helicone.ai — keys, requests, providers |
| Docs | https://docs.helicone.ai |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/llm-gateway-and-routing/' | relative_url }}"><small>Collection</small><strong>← LLM Gateway &amp; Routing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
