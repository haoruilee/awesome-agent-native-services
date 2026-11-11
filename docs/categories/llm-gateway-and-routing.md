---
title: "LLM Gateway & Routing | Agent-Native Services"
collection_label: "LLM Gateway & Routing"
description: "Budget-aware model access, routing, caching, policy, and trajectory-sensitive escalation."
hero_image: "/assets/images/editorial-routing.webp"
hero_image_alt: "Parallel gold pipes flowing through dark translucent panels above a winding marble and stone base."
image: "/assets/images/editorial-routing.webp"
permalink: /categories/llm-gateway-and-routing/
page_kind: collection
collection_number: "15"
service_count: 12
---

<p class="collection-source"><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/README.md">Collection notes ↗</a></p>

<div class="collection-essay" markdown="1">

One provider's API is enough for a prototype. An agent in production makes many calls, sometimes across providers, and someone has to cap the spend, fail over, and attribute the cost to that run. The providers' own APIs were not built as a per-agent control plane. This collection is the layer people put in front of them.

OpenRouter, Portkey, LiteLLM, Helicone, Bifrost, and Respan are gateways with routing, logs, or both, as each set of docs describes. Routerly is a self-hosted gateway across providers. XiuRouter presents one API in front of several model families. SageRoute is described in its dossier as trajectory-aware routing, which is a different bet from a static fallback list. Agentgateway's docs include MCP as well as model traffic. Dasha Compute is an OpenAI-compatible inference surface. A unified API, a budget, and a cache are three features that often ship together and do not have to.

The unit of control is the thing to read for. A single key shared by every agent is easy to leak and hard to account for. A virtual key or a budget tied to one agent matches the category's point. Fallback helps only if the agent does not depend on one provider's tool-call dialect, or if the gateway normalizes it. A cache can skip a repeat call and can also return an answer that belonged to a different user. Sending prompts through a third party is a retention decision. Read that vendor's docs before you do it. The gateway is not the memory, the browser, or the sandbox.

</div>

<div class="service-grid">
  <article class="service-card atlas-sheet--service atlas-visual--01">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://agentgateway.dev" rel="noopener noreferrer">Agentgateway</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/agentgateway/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Connect Secure Observe Connect Agentic Workflows.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/agentgateway/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/agentgateway.md">Dossier ↗</a>
      <a href="https://github.com/agentgateway/agentgateway">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--02">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://docs.getbifrost.ai" rel="noopener noreferrer">Bifrost</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/bifrost/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">The fastest way to build AI applications that never go down.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/bifrost/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/bifrost.md">Dossier ↗</a>
      <a href="https://github.com/maximhq/bifrost">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--03">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://lobby.getdasha.com/compute" rel="noopener noreferrer">Dasha Compute</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/dasha-compute/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">OpenAI-compatible inference. A run factory, not a ledger.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/dasha-compute/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/dasha-compute.md">Dossier ↗</a>
      <a href="https://github.com/Uuriko/dasha-desk">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--04">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://www.helicone.ai" rel="noopener noreferrer">Helicone</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/helicone/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Build Reliable AI Apps&quot; — AI Gateway &amp; LLM observability.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/helicone/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/helicone.md">Dossier ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--05">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://hop-base.com" rel="noopener noreferrer">HopBase</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/hopbase/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Built for enterprise — A stable, high-concurrency AI gateway</p>
    <div class="service-card__actions">
      <a href="{{ '/services/hopbase/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/hopbase.md">Dossier ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--06">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://www.litellm.ai" rel="noopener noreferrer">LiteLLM</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/litellm/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">AI Gateway to provide model access, fallbacks and spend tracking across 100+ LLMs. All in the OpenAI format.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/litellm/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/litellm.md">Dossier ↗</a>
      <a href="https://github.com/BerriAI/litellm">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--07">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://openrouter.ai" rel="noopener noreferrer">OpenRouter</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/openrouter/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">The Unified Interface For LLMs.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/openrouter/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/openrouter.md">Dossier ↗</a>
      <a href="https://github.com/OpenRouterTeam">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--08">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://portkey.ai" rel="noopener noreferrer">Portkey</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/portkey/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">The AI gateway built for production agents.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/portkey/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/portkey.md">Dossier ↗</a>
      <a href="https://github.com/Portkey-AI/portkey-python-sdk">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--09">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://www.respan.ai/" rel="noopener noreferrer">Respan (Keywords AI)</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/keywords-ai/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Route, observe, and evaluate every LLM call</p>
    <div class="service-card__actions">
      <a href="{{ '/services/keywords-ai/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/keywords-ai.md">Dossier ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--10">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://github.com/Inebrio/Routerly" rel="noopener noreferrer">Routerly</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/routerly/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Self-hosted LLM gateway that routes requests across AI providers (OpenAI, Anthropic, Gemini, Mistral, Ollama) using intelligent multi-policy scoring — including an LLM-native routing policy. Drop-in compatible: just swap the base URL. No database required, built-in cost tracking, budget enforcement and multi-tenant isolation.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/routerly/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/routerly.md">Dossier ↗</a>
      <a href="https://github.com/Inebrio/Routerly">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card service-card--new atlas-sheet--service atlas-visual--11">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>New · Last 30 days</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://github.com/codejunkie99/sageroute" rel="noopener noreferrer">SageRoute</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/sageroute/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">A trajectory-aware model router.</p>
    <div class="service-card__actions">
      <a href="{{ '/services/sageroute/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/sageroute.md">Dossier ↗</a>
      <a href="https://github.com/codejunkie99/sageroute">Official repo ↗</a>
    </div>
    </div>
  </article>
  <article class="service-card atlas-sheet--service atlas-visual--12">
    <span class="service-card__image" aria-hidden="true"></span>
    <div class="service-card__copy">
    <div class="service-card__overline"><span>Curated dossier</span><span>agent-native</span></div>
    <h2 class="service-card__title"><a href="https://router.xiu.ai/en" rel="noopener noreferrer">XiuRouter</a></h2>
    <p class="listing-source">Listed on <a href="{{ '/services/xiurouter/' | relative_url }}">The Agent-Native Index</a></p>
    <p class="service-card__tagline">Claude, GPT, Gemini, and more through one API</p>
    <div class="service-card__actions">
      <a href="{{ '/services/xiurouter/' | relative_url }}">Introduction</a>
      <a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/xiurouter.md">Dossier ↗</a>
    </div>
    </div>
  </article>
</div>
<nav class="collection-pagination" aria-label="Adjacent collections">
  <a href="{{ '/categories/voice-and-phone/' | relative_url }}"><small>Previous collection</small><strong>← Voice & Phone</strong></a>
  <a href="{{ '/categories/agent-social-network/' | relative_url }}"><small>Next collection</small><strong>Agent Social & Community →</strong></a>
</nav>
