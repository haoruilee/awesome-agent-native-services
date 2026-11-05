---
title: "XiuRouter | Agent-Native Services"
service_name: "XiuRouter"
description: "Claude, GPT, Gemini, and more through one API"
permalink: /services/xiurouter/
page_kind: service
service_slug: "xiurouter"
category_slug: "llm-gateway-and-routing"
category_label: "LLM Gateway & Routing"
hero_image: "/assets/images/editorial-routing.webp"
image: "/assets/images/editorial-routing.webp"
classification: "agent-native"
dossier_path: "services/llm-gateway-and-routing/xiurouter.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/xiurouter.md"
tagline: "Claude, GPT, Gemini, and more through one API"
website: "https://router.xiu.ai/en"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">LLM Gateway &amp; Routing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · SDK · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://router.xiu.ai/en" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://docs.xiu.ai/en/router/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/xiurouter.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

XiuRouter is a hosted model API for developers and AI agents. One account and scoped API key can call models through OpenAI Chat Completions, OpenAI Responses, Anthropic Messages, or Gemini GenerateContent. The public Agent integrations workspace documents protocol-aware setup and replacement paths for 14 supported clients, including Codex, Claude Code, Cursor, Cline, Continue, OpenClaw, Hermes Agent, Aider, Open WebUI, LibreChat, and Vercel AI SDK.

The control boundary is intentionally narrower than a full agent identity platform. XiuRouter provides constrained keys and request-level usage records, but it does not claim persistent cross-service agent identity, delegated user authorization, automatic provider fallback, or trajectory-level tracing.

---

## Agent-facing interfaces

- **Interaction pattern:** scoped API key + the native protocol used by the agent client.
- **Catalog protocols:** CLI, SDK, http, API
- **MCP:** ⚠️ No official XiuRouter MCP server is published.
- **Agent Skill:** ⚠️ No official XiuRouter Agent Skill is published.
- **Onboarding type:** `cli`

## How agents onboard

**Interaction pattern:** scoped API key + the native protocol used by the agent client.

```bash
export XIUROUTER_API_KEY=...

curl https://router-api.xiu.ai/v1/models \
  -H "Authorization: Bearer $XIUROUTER_API_KEY"
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/xiurouter.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| `GET /v1/models` | Lists models visible to the current API key. |
| `POST /v1/chat/completions` | OpenAI Chat Completions route. |
| `POST /v1/responses` | OpenAI Responses route for Codex and Responses clients. |
| `POST /v1/messages` | Anthropic Messages route for Claude Code and Anthropic SDKs. |
| `POST /v1beta/models/{model}:generateContent` | Gemini GenerateContent route. |
| Agent integrations | Client-specific setup, replacement, rollback, and real-request verification for 14 apps. |

OpenAI-style clients use `https://router-api.xiu.ai/v1`; Messages and Gemini clients use the API root when they append their own route.

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/llm-gateway-and-routing/' | relative_url }}"><small>Collection</small><strong>← LLM Gateway &amp; Routing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
