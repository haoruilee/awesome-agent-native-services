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

<section class="service-essay" aria-label="Editorial" markdown="1">

Every request an agent sends through this gateway passes through a hosted service that OpenRouter operates, then on to whichever model provider it routes to. Nothing runs on the agent's machine except an OpenAI-compatible client pointed at a different base URL. That places two parties between the agent and its model, and the account's routing and data policy settings decide which second party sees each prompt.

### One base URL, many providers

The vendor's wording is "The Unified Interface For LLMs." In the dossier that means a single OpenAI-compatible chat completions API across models from many labs, with routing, failover between providers, one credit balance, and usage analytics. An agent names a model by its slug, optionally adds routing hints, and OpenRouter picks a provider. Tool calls and multi-turn loops then behave as they would against the OpenAI API, which is why an agent framework can adopt it by changing a base URL and a key.

The documented surfaces are the REST base URL `https://openrouter.ai/api/v1`, official SDKs in TypeScript, Python, Go, and Java, and a dashboard for keys and credits that the dossier calls secondary. The quickstart sets an `OPENROUTER_API_KEY` and points an existing OpenAI client at that base URL. The dossier records no first-party MCP server and no official Agent Skill; HTTP and the SDKs are the path. Start from the [OpenRouter quickstart](https://openrouter.ai/docs/quickstart) and the provider selection guide it links.

### Hosted router versus a gateway you run

The [LLM Gateway & Routing](/categories/llm-gateway-and-routing/) category divides on who runs the router. [LiteLLM](/services/litellm/) is a gateway that keeps model access, fallbacks, and spend tracking in the OpenAI format, and the dossier's comparison table names a self-managed router as the alternative that leaves failover and provider contracts with you. [Portkey](/services/portkey/) positions itself as a gateway for production agents. [Helicone](/services/helicone/) pairs a gateway with LLM observability. [Bifrost](/services/bifrost/) is pitched on keeping applications up. OpenRouter's difference is that it is also the billing relationship: one balance replaces separate accounts with each lab. The guide on [what makes a service agent-native](/guides/what-makes-a-service-agent-native/) covers why programmatic keys and credits matter for unattended agents.

### Account settings to review

API keys belong to users or organizations, and usage is billed to the owner. Check how granular keys can be and whether each agent or environment can get its own key with its own spending ceiling, because an unattended loop can spend quickly.

Data policy is the setting with the most weight. The dossier says it controls what OpenRouter logs and which providers may process prompts. Set it before sending anything sensitive, and read which providers each model may route to. The dossier does not specify how failover handles differences in tool-calling behavior between providers serving the same model, or what happens to a request mid-stream when a provider fails. Test both with your own prompts before relying on automatic failover. Public app listings are optional; decide if you want your usage attributed by name.

### Editor's take

Agents that switch between cheap and frontier models, or that need to keep running when a single lab has an outage, get the most from one key and one bill. Teams that must keep prompts inside their own network, or want the router under their own control, should compare LiteLLM and Portkey, checking which deployment options each one documents. These remarks rest on the dossier and OpenRouter's quickstart and routing docs, not on traffic we have sent through it.

</section>

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
