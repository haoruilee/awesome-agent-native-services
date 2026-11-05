---
title: "SageRoute | Agent-Native Services"
service_name: "SageRoute"
description: "A trajectory-aware model router"
permalink: /services/sageroute/
page_kind: service
service_slug: "sageroute"
category_slug: "llm-gateway-and-routing"
category_label: "LLM Gateway & Routing"
hero_image: "/assets/images/editorial-routing.webp"
image: "/assets/images/editorial-routing.webp"
classification: "agent-native"
dossier_path: "services/llm-gateway-and-routing/sageroute.md"
dossier_url: "https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/sageroute.md"
tagline: "A trajectory-aware model router"
verified_at: "2026-09-26"
website: "https://github.com/codejunkie99/sageroute"
repository: "https://github.com/codejunkie99/sageroute"
---

<ul class="service-page__chips">
<li><span class="service-page__chip-label">Collection</span><span class="service-page__chip-value">LLM Gateway &amp; Routing</span></li>
<li><span class="service-page__chip-label">Classification</span><span class="service-page__chip-value">agent-native</span></li>
<li><span class="service-page__chip-label">License</span><span class="service-page__chip-value">MIT</span></li>
<li><span class="service-page__chip-label">MCP</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Agent Skill</span><span class="service-page__chip-value">Unavailable</span></li>
<li><span class="service-page__chip-label">Interfaces</span><span class="service-page__chip-value">CLI · documentation</span></li>
<li><span class="service-page__chip-label">Verified</span><span class="service-page__chip-value">2026-09-26</span></li>
</ul>

<ul class="service-page__links">
<li><a href="https://github.com/codejunkie99/sageroute" rel="noopener noreferrer">Website ↗</a></li>
<li><a href="https://github.com/codejunkie99/sageroute/tree/main/docs" rel="noopener noreferrer">Docs ↗</a></li>
<li><a href="https://github.com/codejunkie99/sageroute" rel="noopener noreferrer">Official repo ↗</a></li>
<li><a href="https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/sageroute.md" rel="noopener noreferrer">Full dossier on GitHub ↗</a></li>
</ul>

## What it does

SageRoute is a proxy that changes models based on an agent's observed execution trajectory instead of classifying only its opening prompt. Every session starts on a cheap model. The router reconstructs tool calls and results from each request, detects loops, repeated error classes, rewrite/retest thrashing, and lack of successful execution, then asks the Levanto Sage decision API whether to continue, switch models, restart with cleaned context, or escalate to a human.

The project is explicitly early. It has no published release/tag, stores session state in one process, and is not battle-tested at scale. The README documents a real cheap-to-strong run but not a multi-task benchmark, aggregate savings study, or live proof for every ladder action. Live decision quality also depends on the external Levanto Sage API; an offline deterministic stub exists for development, and live Sage failures default to continuing rather than taking the agent down.

---

## Agent-facing interfaces

- **Interaction pattern:** OpenAI/Anthropic-compatible proxy
- **Catalog protocols:** CLI, documentation
- **MCP:** ⚠️ No MCP server published. SageRoute is an OpenAI Responses / Chat Completions and Anthropic Messages proxy.
- **Agent Skill:** ⚠️ No official skill published.
- **Onboarding type:** `documentation`

## How agents onboard

**Interaction pattern:** OpenAI/Anthropic-compatible proxy

```bash
git clone https://github.com/codejunkie99/sageroute.git
cd sageroute
bun install
echo "SAGE_API_KEY=lv_..." > .env
bun run serve                     # http://127.0.0.1:8787

export OPENAI_BASE_URL=http://127.0.0.1:8787/v1
export OPENAI_MODEL=sageroute
```

See the [full onboarding section in the dossier](https://github.com/haoruilee/awesome-agent-native-services/blob/main/services/llm-gateway-and-routing/sageroute.md#how-to-use-agent-onboarding).

## Protocol surface

| Interface | Detail |
|---|---|
| `POST /v1/responses` | Native routed path for Codex and OpenAI-compatible clients |
| `POST /v1/messages` | Anthropic Messages adapter for Claude Code, translated into the same evidence model |
| `POST /v1/chat/completions` | Passthrough path for non-routed aliases |
| `GET /v1/models` | Router alias plus configured provider/model names |
| `GET /v1/sageroute/sessions` | Per-session tier, cost ledger, switches, and decision history |
| `GET /health` | Liveness endpoint |
| CLI | `serve`, `init`, `check`, provider selection, and OAuth login/import/status commands |

---

## Verification

Last verified **2026-09-26**.

Sources:
- https://api.github.com/repos/codejunkie99/sageroute

<nav class="service-page__nav" aria-label="Service placement">
  <a href="{{ '/categories/llm-gateway-and-routing/' | relative_url }}"><small>Collection</small><strong>← LLM Gateway &amp; Routing</strong></a>
  <a href="{{ '/' | relative_url }}"><small>Index</small><strong>Agent-Native Index →</strong></a>
</nav>
