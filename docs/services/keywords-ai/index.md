---
title: "Respan (Keywords AI) | Agent-Native Services"
service_name: "Respan (Keywords AI)"
description: "Route, observe, and evaluate every LLM call"
permalink: /services/keywords-ai/
page_kind: service
service_slug: "keywords-ai"
category_slug: "llm-gateway-and-routing"
category_label: "LLM Gateway & Routing"
hero_image: "/assets/images/editorial-routing.webp"
image: "/assets/images/editorial-routing.webp"
classification: "agent-native"
dossier_path: "services/llm-gateway-and-routing/keywords-ai.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/keywords-ai.md"
tagline: "Route, observe, and evaluate every LLM call"
verified_at: "2026-10-19"
website: "https://www.respan.ai/"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">LLM Gateway &amp; Routing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · REST · SDK · http · API</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-10-19</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.respan.ai/" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.respan.ai/docs/documentation/overview" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/keywords-ai.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Respan (formerly Keywords AI) is an **LLM engineering platform**: one gateway to **1,000+ models**, plus tracing, metrics, evals, prompt management, and agent security testing on a shared span model. Homepage H1: *"Route, observe, and evaluate every LLM call."* Docs: *"the full-stack AI engineering platform for LLM and agent products."*

---

## Agent-facing interfaces

- **Interaction pattern:** OpenAI-compatible REST + agent tracing
- **Catalog protocols:** MCP, REST, SDK, http, API
- **MCP:** ✅ Docs advertise an MCP server for AI clients
- **Agent Skill:** ⚠️ No official AgentSkills registry entry documented here.
- **Onboarding type:** `api`

## How agents onboard

**Interaction pattern:** OpenAI-compatible REST + agent tracing

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/keywords-ai.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST | `https://api.respan.ai/api/chat/completions` |
| OpenAI SDK | Drop-in `base_url="https://api.respan.ai/api"` |
| Agents SDK | `OpenAIAgentsInstrumentor` — [docs](https://www.respan.ai/docs/integrations/openai-agents-sdk) |
| MCP | `https://respan.ai/_mcp/server` |

---

## Verification

Last verified **2026-10-19**.

Sources:
- https://www.respan.ai/

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/llm-gateway-and-routing/' | relative_url }}"><small>Collection</small><strong>← LLM Gateway &amp; Routing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
