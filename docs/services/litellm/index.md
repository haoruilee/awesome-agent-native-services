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

<section class="service-essay" aria-label="Editorial" markdown="1">

### You run it

Nobody else operates LiteLLM in this catalog record. The documented path is a proxy you deploy yourself from the Python package, a Docker image, or Kubernetes, then point the OpenAI SDK's base URL at. That puts the provider keys, the logs, and the uptime on your side. What the dossier leaves open is the line between the open-source proxy and paid features: virtual keys with budgets and RBAC carry an Enterprise note, and audit through SSO is described only by reference to the enterprise docs. Check the [LiteLLM docs](https://docs.litellm.ai) for which controls you get without a license before designing around them.

MCP support is also hard to pin down. The dossier describes it as a gateway feature, with pass-through and proxy patterns for MCP servers, rather than as a package a coding agent can install, and it gives no single page for it. There is no official Agent Skill.

### Agents as routes

Beyond model routing, the Agent Gateway treats agents themselves as destinations. You register A2A-compatible agents, such as ones on Vertex Agent Engine, Bedrock AgentCore, LangGraph, or Pydantic AI, and invoke them through A2A JSON-RPC at `POST /a2a/{agent_name}/message/send` or through the OpenAI SDK with an `a2a/` model prefix. That is the clearest difference from gateways that only proxy model calls.

Two headers carry agent identity through nested calls. `X-LiteLLM-Trace-Id` groups the calls of one run, and `X-LiteLLM-Agent-Id` attributes spend to an agent. Iteration budgets cap how many loops an agent can make at the gateway, a stop for runaway agents that does not depend on the agent's own code behaving.

The rest is standard gateway work: fallbacks, load balancing, budgets, rate limits, guardrail hooks, and log export to OpenTelemetry, S3, or Langfuse. An Admin UI and REST APIs sit beside the proxy.

### Next to managed gateways

In [LLM Gateway & Routing](/categories/llm-gateway-and-routing/), the usual comparison is [Portkey](/services/portkey/), the AI gateway built for production agents, which its own dossier frames as the managed alternative. [Bifrost](/services/bifrost/) pitches applications that never go down. [Agentgateway](/services/agentgateway/) aims at connecting and securing agentic workflows, which overlaps with the A2A routing here. [OpenRouter](/services/openrouter/) offers a unified interface to models as a service. The vendor tagline stresses model access, fallbacks, and spend tracking in the OpenAI format. The listing criteria are explained in [What makes a service agent-native](/guides/what-makes-a-service-agent-native/).

### Editor's take

LiteLLM is the default for platform teams that must keep model traffic inside their own VPC and want A2A agents behind the same proxy as model calls. Teams that would rather not operate a gateway at all should evaluate Portkey or OpenRouter instead. We formed this view from the catalog record and LiteLLM's docs, without standing up the proxy.

</section>

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
