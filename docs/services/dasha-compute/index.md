---
title: "Dasha Compute | Agent-Native Services"
service_name: "Dasha Compute"
description: "OpenAI-compatible inference. A run factory, not a ledger"
permalink: /services/dasha-compute/
page_kind: service
service_slug: "dasha-compute"
category_slug: "llm-gateway-and-routing"
category_label: "LLM Gateway & Routing"
hero_image: "/assets/images/editorial-routing.webp"
image: "/assets/images/editorial-routing.webp"
classification: "agent-native"
dossier_path: "services/llm-gateway-and-routing/dasha-compute.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/dasha-compute.md"
tagline: "OpenAI-compatible inference. A run factory, not a ledger"
website: "https://lobby.getdasha.com/compute"
repository: "https://github.com/Uuriko/dasha-desk"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">LLM Gateway &amp; Routing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unknown</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Available</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">URL onboarding · Agent Skill · REST · http · API</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://lobby.getdasha.com/compute" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://www.getdasha.com/compute/skill.md" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/Uuriko/dasha-desk" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/dasha-compute.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

Dasha Compute is an **OpenAI-compatible inference marketplace** where AI agents are the primary consumer: agents mint their own 24-hour guest API keys with a single unauthenticated POST, list available models, and run chat completions against a standard `base_url`. Inference is routed to idle community hardware, and the DASHA token (Solana SPL) anchors the ecosystem. The service exposes machine-readable agent surfaces for Compute: `/.well-known/agent.json`, an MCP catalog (`/compute/mcp.json`), and `/compute/skill.md`. The apex `/llms.txt` was a different page on 2026-09-26.

---

## Agent-facing interfaces

- **Catalog protocols:** URL onboarding, Agent Skill, REST, http, API
- **MCP:** ⚠️ Static MCP catalog published at https://www.getdasha.com/compute/mcp.json (HTTP tools + base_url); not a streamable MCP session.
- **Agent Skill:** ✅ Available — the service publishes its own skill document at https://www.getdasha.com/compute/skill.md (also served at https://lobby.getdasha.com/compute/skill.md) and an agent manifest at https://www.getdasha.com/.well-known/agent.json. The apex https://www.getdasha.com/llms.txt did not describe Compute on 2026-09-26.
- **Onboarding type:** `url`

## How agents onboard

```
# URL Onboarding:
Read https://www.getdasha.com/compute/skill.md (or https://www.getdasha.com/.well-known/agent.json) and follow the instructions to register and join. Do not use https://www.getdasha.com/llms.txt for this product: on 2026-09-26 that file described a Solana token site, not Dasha Compute.

# SDK / REST:
# 1. Mint a 24h guest key with a bare POST (no account, no email):
curl -sS -X POST https://lobby.getdasha.com/compute/api/guest-keys -H 'Content-Type: application/json' -d '{}'
# 2. Use the OpenAI SDK with base_url https://lobby.getdasha.com/compute/api/v1 and the guest key as the Bearer token.
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/dasha-compute.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| REST | `https://lobby.getdasha.com/compute/api/v1` — OpenAI-compatible (chat, models) |
| Guest keys | `POST https://lobby.getdasha.com/compute/api/guest-keys` |
| Agent discovery | `/.well-known/agent.json`, `/compute/mcp.json`, `/compute/skill.md` |
| MCP | Static catalog only — not a streamable MCP session |

---

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/llm-gateway-and-routing/' | relative_url }}"><small>Collection</small><strong>← LLM Gateway &amp; Routing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
