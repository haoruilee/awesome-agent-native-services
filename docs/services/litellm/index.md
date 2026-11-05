---
title: "LiteLLM | Agent-Native Services"
service_name: "LiteLLM"
description: "AI Gateway to provide model access, fallbacks and spend tracking across 100+ LLMs. All in the OpenAI format"
permalink: /services/litellm/
page_kind: service
service_slug: "litellm"
category_slug: "llm-gateway-and-routing"
category_label: "LLM Gateway & Routing"
hero_image: "/assets/images/editorial-routing.webp"
image: "/assets/images/editorial-routing.webp"
classification: "agent-native"
dossier_path: "services/llm-gateway-and-routing/litellm.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/litellm.md"
tagline: "AI Gateway to provide model access, fallbacks and spend tracking across 100+ LLMs. All in the OpenAI format"
website: "https://www.litellm.ai"
repository: "https://github.com/BerriAI/litellm"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">LLM Gateway &amp; Routing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · SDK · A2A · http</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://www.litellm.ai" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.litellm.ai" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/BerriAI/litellm" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/litellm.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

LiteLLM is an **open-source AI gateway** that unifies **100+ LLM providers** behind an **OpenAI-compatible** API. Platform teams use it for **virtual keys**, **spend tracking**, **budgets**, **rate limits**, **fallbacks**, **guardrails**, and **logging** (Langfuse, OpenTelemetry, etc.). The **Agent Gateway** adds first-class **A2A (Agent-to-Agent)** routing, **iteration budgets**, **trace grouping** (`X-LiteLLM-Trace-Id`), and **per-agent spend** (`X-LiteLLM-Agent-Id`) for multi-step agents — see [A2A docs](https://docs.litellm.ai/docs/a2a).

---

## Agent-facing interfaces

- **Catalog protocols:** MCP, SDK, A2A, http
- **MCP:** ✅ LiteLLM documents MCP integration on the AI Gateway (pass-through / proxy patterns for MCP servers — see docs index and search "MCP"). Treat as gateway feature rather than a single stdio package name.
- **Agent Skill:** ⚠️ No official AgentSkills repo located; search community:
- **Onboarding type:** `sdk`

## How agents onboard

```bash
pip install litellm
# Deploy proxy per https://docs.litellm.ai/docs/proxy/docker_quick_start
# Point OpenAI SDK base_url at your LiteLLM proxy (e.g. http://localhost:4000)
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/litellm.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| HTTP | OpenAI-compatible chat/completions on proxy |
| A2A | `POST /a2a/{agent_name}/message/send` — see docs |
| Python | `pip install litellm` |
| Deploy | Docker, Kubernetes — see [proxy deploy](https://docs.litellm.ai/docs/proxy/deploy) |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/llm-gateway-and-routing/' | relative_url }}"><small>Collection</small><strong>← LLM Gateway &amp; Routing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
