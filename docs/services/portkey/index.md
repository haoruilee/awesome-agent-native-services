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

<section class="service-essay" aria-label="Editorial" markdown="1">

### The gateway repository question

Which code is open is unclear from the record. It lists the Python and Node SDK repositories as the official code, while its stars badge points at a separate `Portkey-AI/gateway` repository that the dossier never describes. One use case mentions running Portkey on-prem or in a VPC, but no deployment steps are given, and nothing says whether that is the open gateway or an enterprise build. If running the proxy yourself matters, the [Portkey docs](https://portkey.ai/docs) need to answer that before anything else.

There is no dedicated MCP server and no official Agent Skill. The documented path is the OpenAI-compatible HTTP API, which works with any framework that lets you change a base URL.

### Keys that stand in for keys

The integration in the dossier is a base URL change: `pip install portkey-ai` or the Node package, then point the client at `https://api.portkey.ai/v1` with a virtual key. Portkey stores the real provider keys and hands each agent or project a scoped stand-in, so the provider credential never sits in agent code. Budgets attach to virtual keys, metadata tags, or workspaces, in currency or tokens, with alerts before they run out.

On each request Portkey checks the budget, consults a semantic cache, and routes to a provider. If that provider fails or rate-limits, a configured fallback takes the request. Sticky session routing keeps a multi-turn conversation on the same provider, and load balancing can split traffic by weight or in rotation. Guardrails check inputs and outputs against policy. Every call is logged with cost, tokens, and a trace ID that links the steps of a multi-hop agent chain.

Human approval is out of scope. Budget alerts are the only human-facing control the dossier names.

### Other gateways

[LLM Gateway & Routing](/categories/llm-gateway-and-routing/) has close competitors. The Portkey dossier itself names [LiteLLM](/services/litellm/) as the open-source, self-hosted sibling and positions Portkey as the managed one. [OpenRouter](/services/openrouter/) offers a unified interface for LLMs. [Helicone](/services/helicone/) pairs an AI gateway with LLM observability. [Agentgateway](/services/agentgateway/) is aimed at connecting and securing agentic workflows. Portkey's tagline, "The AI gateway built for production agents.", leans on virtual keys and per-agent budgets as the agent-specific parts. [What makes a service agent-native](/guides/what-makes-a-service-agent-native/) sets out why gateways are listed in this catalog.

### Editor's take

Portkey suits teams that want per-agent keys, budgets, and fallback without operating a proxy fleet, and who are comfortable sending prompt traffic through a vendor. If the traffic must stay on infrastructure you run, LiteLLM is the documented self-hosted route. We assembled this from the dossier and Portkey's public docs; no request was routed through Portkey for it.

</section>

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
