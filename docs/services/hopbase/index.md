---
title: "HopBase | Agent-Native Services"
service_name: "HopBase"
description: "Built for enterprise — A stable, high-concurrency AI gateway"
permalink: /services/hopbase/
page_kind: service
service_slug: "hopbase"
category_slug: "llm-gateway-and-routing"
category_label: "LLM Gateway & Routing"
hero_image: "/assets/images/editorial-routing.webp"
image: "/assets/images/editorial-routing.webp"
classification: "agent-native"
dossier_path: "services/llm-gateway-and-routing/hopbase.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/hopbase.md"
tagline: "Built for enterprise — A stable, high-concurrency AI gateway"
website: "https://hop-base.com"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">LLM Gateway &amp; Routing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · MCP · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://hop-base.com" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://hop-base.com/en/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/hopbase.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

HopBase is a hosted AI gateway. Through one base URL (`https://api.hop-base.com/v1`) it serves chat, image, and video models over OpenAI Chat Completions, OpenAI Responses, Anthropic Messages, and native Gemini routes, so an agent client keeps the wire protocol it already sends. Each API key includes one or more model groups and carries its own spend cap, concurrency limit, expiry, and IP rules.

For agents, HopBase publishes an AI-readable integration contract (`llms.txt` plus per-model-family contracts) and a key-scoped, read-only MCP server. Together they let a coding agent configure itself and check what its key may call, its limits, and its usage before and after it acts.

The control boundary is intentionally narrower than a full agent identity platform. HopBase provides constrained keys and request-level usage records, but it does not mint a cross-service agent identity, KYA token, or delegated user-authorization grant, and an operator must create the key in the console.

---

## Agent-facing interfaces

- **Interaction pattern:** operator-issued API key + agent integration contract + key-scoped MCP.
- **Catalog protocols:** URL onboarding, MCP, SDK, http, API
- **MCP:** ✅ Available (hosted, read-only, API key required)
- **Agent Skill:** ⚠️ No npx skills add package is published.
- **Onboarding type:** `url`

## How agents onboard

**Interaction pattern:** operator-issued API key + agent integration contract + key-scoped MCP.

```
Read https://hop-base.com/llms.txt and follow the AI Integration Contract.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/hopbase.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| `GET /v1/models` | Lists only the model IDs the current key can call; 401 without a key. |
| `POST /v1/chat/completions` | OpenAI Chat Completions route. |
| `POST /v1/responses` | OpenAI Responses route for Codex and Responses clients. |
| `POST /v1/messages` | Anthropic Messages route for Claude Code and Anthropic SDKs. |
| Native Gemini | Gemini-format route for Gemini clients. |
| Image / video tasks | Task endpoints for image and video generation models. |
| MCP | `https://api.hop-base.com/mcp`, Streamable HTTP, read-only, API key required. |

Base URL: `https://api.hop-base.com/v1`. See the [docs](https://hop-base.com/en/docs) for per-route details.

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/llm-gateway-and-routing/' | relative_url }}"><small>Collection</small><strong>← LLM Gateway &amp; Routing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
