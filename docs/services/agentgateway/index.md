---
title: "Agentgateway | Agent-Native Services"
service_name: "Agentgateway"
description: "Connect Secure Observe Connect Agentic Workflows"
permalink: /services/agentgateway/
page_kind: service
service_slug: "agentgateway"
category_slug: "llm-gateway-and-routing"
category_label: "LLM Gateway & Routing"
hero_image: "/assets/images/editorial-routing.webp"
image: "/assets/images/editorial-routing.webp"
classification: "agent-native"
dossier_path: "services/llm-gateway-and-routing/agentgateway.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/agentgateway.md"
tagline: "Connect Secure Observe Connect Agentic Workflows"
website: "https://agentgateway.dev"
repository: "https://github.com/agentgateway/agentgateway"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">LLM Gateway &amp; Routing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">MCP · A2A · STDIO · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://agentgateway.dev" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://agentgateway.dev/docs/" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/agentgateway/agentgateway" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/agentgateway.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Agentgateway is an **open-source proxy** for agentic traffic: it routes **agent-to-LLM** requests through an OpenAI-compatible surface (multi-provider), connects **agent-to-tool** via MCP (including federation and auth), and **agent-to-agent** via the A2A protocol. It adds **JWT/API key auth**, CEL-based **RBAC**, rate limits, prompt guards, and **OpenTelemetry** visibility — positioned as infrastructure for agent workloads rather than a generic HTTP reverse proxy.

---

## Agent-facing interfaces

- **Interaction pattern:** self-hosted proxy (binary, Docker, or Kubernetes) — OpenAI-compatible LLM front door plus MCP and A2A routing
- **Catalog protocols:** MCP, A2A, STDIO, http, API
- **MCP:** ✅ Core protocol (MCP gateway is a primary feature)
- **Agent Skill:** ⚠️ No official SKILL.md / npx skills add … pack for Agentgateway yet.
- **Onboarding type:** `mcp`

## How agents onboard

**Interaction pattern:** self-hosted proxy (binary, Docker, or Kubernetes) — OpenAI-compatible LLM front door plus MCP and A2A routing

```bash
curl https://raw.githubusercontent.com/agentgateway/agentgateway/refs/heads/main/common/scripts/get-agentgateway | bash
curl -sL https://raw.githubusercontent.com/agentgateway/agentgateway/main/examples/basic/config.yaml -o config.yaml
agentgateway -f config.yaml
# Open UI at localhost:15000
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/agentgateway.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| OpenAI-compatible HTTP | Chat completions proxy to many providers |
| MCP | stdio, SSE, Streamable HTTP — client and server federation |
| A2A | Agent-to-agent protocol routing |
| Kubernetes | Gateway API / control-plane deployment options |
| Configuration | YAML locally; CRDs on Kubernetes |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/llm-gateway-and-routing/' | relative_url }}"><small>Collection</small><strong>← LLM Gateway &amp; Routing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
